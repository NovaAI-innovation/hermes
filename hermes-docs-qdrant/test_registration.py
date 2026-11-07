"""End-to-end: register against a stub host and exercise docs_search.

Proves the registration contract (8 tools, 6 gated + 2 ungated) and that a
search through the registered handler returns cited passages, which is what
"the tools are available" actually has to mean.

Run: python test_registration.py
"""

from __future__ import annotations

import importlib
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

REGISTERED: dict[str, dict] = {}


class _Ctx:
    """Minimal stand-in for the Hermes plugin context."""

    def get_config(self, *_args):
        return {}

    def register_tool(self, name, toolset, schema, handler, check_fn=None):
        REGISTERED[name] = {
            "toolset": toolset,
            "schema": schema,
            "handler": handler,
            "check_fn": check_fn,
        }


def _load_package():
    if "hermes_docs_qdrant" in sys.modules:
        return sys.modules["hermes_docs_qdrant"]
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "hermes_docs_qdrant",
        HERE / "__init__.py",
        submodule_search_locations=[str(HERE)],
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["hermes_docs_qdrant"] = module
    spec.loader.exec_module(module)
    return module


def _patch_offline_embedder(package) -> None:
    """Swap in a deterministic query embedder, matching test_offline.py.

    The corpus was indexed with real vectors, so offline scores are not
    meaningful; this asserts the *path* works (client -> query -> payload ->
    citation), not the ranking quality.
    """
    import hashlib
    from types import SimpleNamespace

    dim = package.store.EMBED_DIM

    def fake(text: str) -> list[float]:
        seed = hashlib.sha256(text.encode("utf-8")).digest()
        vals = [(seed[i % len(seed)] / 255.0) - 0.5 for i in range(dim)]
        norm = sum(v * v for v in vals) ** 0.5
        return [v / norm for v in vals]

    class _Embeddings:
        def create(self, model=None, input=None):
            return SimpleNamespace(
                data=[
                    SimpleNamespace(index=i, embedding=fake(t))
                    for i, t in enumerate(input)
                ]
            )

    class _Client:
        def __init__(self, *a, **kw):
            self.embeddings = _Embeddings()

    store_mod = package.tools.store_mod
    store_mod.QueryEmbedder._get_client = lambda self: _Client()
    os.environ.setdefault("OPENROUTER_API_KEY", "")


def main() -> int:
    package = _load_package()
    package.register(_Ctx())

    expected = {
        "docs_search",
        "docs_search_many",
        "docs_read",
        "docs_outline",
        "docs_list",
        "docs_stats",
        "docs_diagnostics",
        "docs_rebuild",
    }
    problems: list[str] = []

    missing = expected - set(REGISTERED)
    if missing:
        problems.append(f"not registered: {sorted(missing)}")
    extra = set(REGISTERED) - expected
    if extra:
        problems.append(f"registered but not declared: {sorted(extra)}")
    for name in ("docs_diagnostics", "docs_rebuild"):
        entry = REGISTERED.get(name)
        if entry and entry["check_fn"] is not None:
            problems.append(f"{name} must be ungated (check_fn is not None)")
    for name in expected - {"docs_diagnostics", "docs_rebuild"}:
        entry = REGISTERED.get(name)
        if entry and entry["check_fn"] is None:
            problems.append(f"{name} must be gated (check_fn is None)")

    print(f"registered {len(REGISTERED)} tools on toolset "
          f"{sorted({v['toolset'] for v in REGISTERED.values()})}")
    for name in sorted(REGISTERED):
        gated = REGISTERED[name]["check_fn"] is not None
        print(f"  {name:18} gated={gated}")

    # Every gated tool must be visible in a healthy environment.
    available = [n for n, v in REGISTERED.items()
                 if v["check_fn"] is None or v["check_fn"]()]
    print(f"available in this environment: {len(available)}/{len(REGISTERED)}")
    for name in sorted(expected):
        if name not in available:
            problems.append(f"{name} is hidden though the environment is healthy")

    # Exercise real retrieval through the registered handler. Without an API
    # key the query embedder is replaced by the deterministic offline one, so
    # this proves the search path end to end rather than only that it imports.
    if not os.getenv("OPENROUTER_API_KEY"):
        _patch_offline_embedder(package)
        print("docs_search: OPENROUTER_API_KEY unset; using the offline embedder")

    search = REGISTERED["docs_search"]["handler"]
    payload = json.loads(search({"query": "connect telegram gateway", "limit": 3}))
    if not payload.get("ok"):
        problems.append(f"docs_search failed: {payload.get('error')}")
    results = payload.get("results") or []
    print(f"docs_search -> {len(results)} result(s)")
    for hit in results[:3]:
        print(f"  [{hit['score']:.3f}] {hit['title']} -> {hit['source_url']}")
    if not results:
        problems.append("docs_search returned no passages; is the corpus indexed?")
    if results and not all(hit.get("source_url") for hit in results):
        problems.append("results must carry source_url citations")

    stats = json.loads(REGISTERED["docs_stats"]["handler"]({}))
    if stats.get("ok") and stats.get("total_chunks"):
        print(f"corpus: {stats['total_chunks']} chunks, "
              f"{stats['total_documents']} documents")

    diag = json.loads(REGISTERED["docs_diagnostics"]["handler"]({}))
    if not diag.get("ok"):
        problems.append("docs_diagnostics failed in a healthy environment")

    if problems:
        print("\nREGISTRATION TEST FAILED")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("\nREGISTRATION TEST PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
