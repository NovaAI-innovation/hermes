"""Exercise the registered rebuild tool with HTTP sources and embedded Qdrant."""

from __future__ import annotations

import json
import os
import sys
import unittest
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Thread
from unittest.mock import patch

import portalocker

from test_offline import _FakeOpenAI
from test_registration import REGISTERED, _Ctx, _load_package


class QuietHTTPHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


class RebuildTest(unittest.TestCase):
    def test_rebuild_and_retrieve(self):
        package = _load_package()
        store_mod = package.store
        with TemporaryDirectory() as tmp:
            home = Path(tmp)
            site = home / "http"
            site.mkdir()
            handler = partial(QuietHTTPHandler, directory=str(site))
            with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
                worker = Thread(target=server.serve_forever, daemon=True)
                worker.start()
                try:
                    self.exercise(home, site, server.server_port, package, store_mod)
                finally:
                    server.shutdown()
                    worker.join()

    def exercise(self, home, site, port, package, store_mod):
        base = f"http://127.0.0.1:{port}"
        (home / "sources.yaml").write_text(
            f"sources:\n  - name: alpha\n    llms_txt: {base}/alpha.txt\n"
            f"  - name: beta\n    llms_txt: beta.txt\n    doc_host: 127.0.0.1:{port}\n",
            encoding="utf-8",
        )
        alpha = site / "alpha.txt"
        alpha.write_text(f"## Guides\n- [Setup]({base}/setup.md)\n- [Old]({base}/old.md)\n", encoding="utf-8")
        (home / "beta.txt").write_text(f"## Reference\n- [Other]({base}/other.md)\n", encoding="utf-8")
        body = "Configure the example gateway with a dedicated test token. Verify the gateway connection before saving the settings. " * 5
        for name in ("setup", "old", "other"):
            (site / f"{name}.md").write_text(f"# {name}\n\n## Zebra\n\n{body}\n\n## Apple\n\n{body}", encoding="utf-8")

        config = {
            "path": str(home / "store"),
            "collection": "configured_docs",
            "corpus_dir": str(home / "output"),
            "build_python": sys.executable,
        }
        with (
            patch.dict(os.environ, {
                "HERMES_DOCS_HOME": str(home), "OPENROUTER_API_KEY": "offline",
                "QDRANT_URL": "http://example.invalid", "NO_PROXY": "127.0.0.1",
            }),
            patch("openai.OpenAI", _FakeOpenAI),
            patch.object(store_mod.SparseEmbedder, "available", return_value=True),
            patch.object(store_mod.SparseEmbedder, "embed", side_effect=lambda texts: [([1], [1.0])] * len(texts)),
            patch.object(_Ctx, "get_config", return_value=config),
            patch.dict(REGISTERED, clear=True),
        ):
            package.register(_Ctx())
            store = package.tools._store_or_error()
            try:
                store.ensure_collection(config["collection"])
                self.assertTrue(store.health()[0])
                self.assertIsNone(REGISTERED["docs_rebuild"]["check_fn"])
                with portalocker.Lock(home / ".rebuild.lock", mode="a", timeout=0):
                    busy = self.call("docs_rebuild")
                self.assertIn("already running", busy["error"])

                empty = self.call("docs_rebuild", scrape=False)
                self.assertEqual(empty["failed_stage"], "validate", empty)
                self.assertEqual(store.active_collection(), config["collection"])

                built = self.call("docs_rebuild")
                self.assertTrue(built["ok"], built)
                self.assertEqual(built["scraped_sources"], ["alpha", "beta"])
                self.assertEqual(set(built["chunks_by_source"]), {"alpha", "beta"})
                self.assertEqual(store.active_collection(), built["active_collection"])
                self.assertTrue(store.client().collection_exists(config["collection"]))
                self.assertIs(store, package.tools._store_or_error())

                outline = self.call("docs_outline", doc_id="alpha:setup")
                self.assertEqual(outline["headings"], ["Zebra", "Apple"])
                read = self.call("docs_read", doc_id="alpha:setup")
                self.assertLess(read["content"].index("Zebra"), read["content"].index("Apple"))
                search = self.call("docs_search", query="gateway", source="alpha", section="Guides")
                self.assertEqual(search["mode"], "hybrid", search)
                self.assertTrue(search["results"], search)
                self.assertTrue(all(row["source"] == "alpha" and row["source_url"] for row in search["results"]))
                with patch.object(store._dense, "embed_query", side_effect=RuntimeError("provider down")):
                    fallback = self.call("docs_search", query="gateway", source="beta", section="Reference")
                    self.assertEqual(fallback["mode"], "bm25", fallback)
                    self.assertTrue(fallback["warnings"] and fallback["results"], fallback)
                    self.assertTrue(all(row["source"] == "beta" for row in fallback["results"]))

                search_fn = store.search

                def fail_one(query, **kwargs):
                    if query == "fail":
                        raise RuntimeError("simulated failure")
                    return search_fn(query, **kwargs)

                with patch.object(store, "search", side_effect=fail_one):
                    batch = self.call("docs_search_many", queries=["gateway", "fail", "gateway"], section="Guides")
                    self.assertTrue(batch["ok"], batch)
                    self.assertEqual(batch["queries"], ["gateway", "fail"])
                    self.assertTrue(batch["results"]["gateway"])
                    self.assertEqual(batch["errors"], {"fail": "simulated failure"})

                alpha.write_text(f"## Guides\n- [Setup]({base}/setup.md)\n", encoding="utf-8")
                updated = self.call("docs_rebuild", sources=["alpha"], refresh=True)
                self.assertTrue(updated["ok"], updated)
                self.assertEqual(updated["scraped_sources"], ["alpha"])
                self.assertTrue(store.client().collection_exists(built["active_collection"]))
                docs = self.call("docs_list")["documents"]
                self.assertEqual({doc["doc_id"] for doc in docs}, {"alpha:setup", "beta:other"})

                alpha.write_text(f"## Guides\n- [Missing]({base}/missing.md)\n", encoding="utf-8")
                failed = self.call("docs_rebuild", sources=["alpha"])
                self.assertEqual(failed["failed_stage"], "scrape", failed)
                self.assertEqual(store.active_collection(), updated["active_collection"])
                self.assertIn("missing.md", " ".join(failed["stages"][-1]["stderr"]))

                with patch("openai.OpenAI", side_effect=ValueError("embedding failure")):
                    failed = self.call("docs_rebuild", scrape=False)
                self.assertEqual(failed["failed_stage"], "index", failed)
                self.assertEqual(store.active_collection(), updated["active_collection"])

                with patch.dict(os.environ, {"OPENROUTER_API_KEY": ""}):
                    cached = self.call("docs_rebuild", scrape=False, reindex=False)
                self.assertTrue(cached["ok"], cached)
                self.assertFalse(cached["indexed"])
                self.assertEqual(store.active_collection(), updated["active_collection"])
                self.assertNotIn("manifest", self.call("docs_stats"))
                self.assertFalse(self.call("docs_rebuild", refresh="false")["ok"])
                self.assertIn("Unknown sources", self.call("docs_rebuild", sources=["unknown"])["error"])
            finally:
                store.close()

    @staticmethod
    def call(name, **args):
        return json.loads(REGISTERED[name]["handler"](args))


if __name__ == "__main__":
    unittest.main()
