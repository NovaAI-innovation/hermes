"""Offline test: proves the Qdrant write/read/hybrid-query path without API keys.

Uses a deterministic hash-based embedder in place of OpenRouter so the storage
schema and query logic are exercised end to end.
"""

from __future__ import annotations

import hashlib
import json
import sys
import types
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import store as S  # noqa: E402

from pipeline import paths  # noqa: E402

DIM = S.EMBED_DIM


def fake_vector(text: str) -> list[float]:
    seed = hashlib.sha256(text.encode("utf-8")).digest()
    vals = []
    for i in range(DIM):
        byte = seed[i % len(seed)]
        vals.append((byte / 255.0) - 0.5)
    norm = sum(v * v for v in vals) ** 0.5
    return [v / norm for v in vals]


class _FakeEmbeddings:
    def create(self, model=None, input=None):
        data = [
            types.SimpleNamespace(index=i, embedding=fake_vector(t))
            for i, t in enumerate(input)
        ]
        return types.SimpleNamespace(data=data)


class _FakeOpenAI:
    def __init__(self, *a, **kw):
        self.embeddings = _FakeEmbeddings()


def patch_openai():
    mod = types.ModuleType("openai")
    mod.OpenAI = _FakeOpenAI
    sys.modules["openai"] = mod


def main() -> int:
    patch_openai()
    import os

    os.environ["OPENROUTER_API_KEY"] = "offline-test"

    chunks = paths.corpus_dir() / "chunks.jsonl"
    if not chunks.exists():
        print(f"missing {chunks}")
        return 1

    data_dir = Path(__file__).resolve().parent / ".data-offline"
    settings = S.Settings.resolve(
        {"path": str(data_dir / "qdrant"), "collection": "hermes_docs_test"}
    )

    stats = S.ingest(chunks, settings, recreate=True, limit=80, batch_size=16)
    print(f"ingest: {stats}")

    st = S.DocsStore(settings)
    ok, detail = st.health()
    print(f"health: ok={ok} {detail}")

    results = st.search("connect telegram gateway", limit=3)
    print(f"search: {len(results)} results")
    for r in results:
        print(f"  {r['score']:.3f} {r['title']} > {r['heading']}  [{r['doc_type']}]")

    filtered = st.search("cli commands", limit=3, doc_type="reference")
    print(f"filtered doc_type=reference: {len(filtered)} results")
    for r in filtered:
        print(f"  {r['score']:.3f} {r['title']} [{r['doc_type']}]")

    if results:
        doc_id = results[0]["doc_id"]
        rows = st.get_doc_chunks(doc_id)
        print(f"read {doc_id}: {len(rows)} chunks, title={rows[0]['title']}")

    sections = st.list_sections()
    print(f"sections: {len(sections)} -> {sections[:3]}")

    # Newer surfaces: multi-query, catalog, stats, source filter.
    many = st.search_many(["telegram", "cron"], limit=2)
    print(f"search_many: {[(k, len(v)) for k, v in many.items()]}")

    docs = st.list_documents(limit=200)
    print(f"list_documents: {len(docs)} docs")

    corpus = st.corpus_stats()
    print(
        f"corpus_stats: {corpus['total_documents']} docs, "
        f"{corpus['total_chunks']} chunks"
    )

    sources = {d.get("source") for d in docs if d.get("source")}
    filtered_by_source = st.search("gateway", limit=2, source=sorted(sources)[0]) if sources else []
    print(f"filtered source={sorted(sources)[0] if sources else '-'}: {len(filtered_by_source)} results")

    assert ok, "collection should be reachable"
    assert results, "search should return results"
    assert all(r["source_url"] for r in results), "results must carry citations"
    assert many and all(many.values()), "search_many should answer every query"
    assert docs, "list_documents should return the catalog"
    assert corpus["total_chunks"] >= len(rows), "stats should see every chunk"
    assert all(r["source"] == sorted(sources)[0] for r in filtered_by_source), "source filter must be honored"
    print("\nOFFLINE TEST PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
