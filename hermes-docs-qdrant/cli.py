#!/usr/bin/env python3
"""One entry point for the whole corpus lifecycle.

    python cli.py init                 # seed sources.yaml + show the data home
    python cli.py sources              # list registered sources
    python cli.py scrape [--source X]  # llms.txt -> sources/<name>/docs/
    python cli.py build                # normalize -> enrich -> chunk
    python cli.py index [--recreate]   # chunks.jsonl -> Qdrant
    python cli.py fetch                # scrape + build + index (first install)
    python cli.py status               # where data lives + what is present
    python cli.py search "query"       # smoke-test retrieval

Every path resolves through `pipeline/paths.py`, so the same commands work from
a git checkout and from `<HERMES_HOME>/plugin-data/hermes-docs-qdrant/`.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIPELINE_DIR = HERE / "pipeline"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PIPELINE_DIR))

from pipeline import paths  # noqa: E402

STAGES = ["normalize", "enrich", "chunk"]


def _run(script: Path, *args: str, label: str = "") -> int:
    print(f"\n=== {label or script.stem} ===", flush=True)
    started = time.time()
    proc = subprocess.run(
        [sys.executable, str(script), *args], cwd=str(script.parent)
    )
    if proc.returncode != 0:
        print(
            f"stage '{label or script.stem}' failed (exit {proc.returncode})",
            file=sys.stderr,
        )
        return proc.returncode
    print(f"--- {label or script.stem} ok in {time.time() - started:.1f}s")
    return 0


def cmd_init(_args) -> int:
    print("data home:", paths.ensure_home())
    print("registry :", paths.sources_yaml())
    print("sources  :", paths.sources_root())
    print("corpus   :", paths.corpus_dir())
    print("qdrant   :", paths.qdrant_dir())
    print("\nSet HERMES_DOCS_HOME to relocate. OpenRouter key goes in the")
    print("process env or <data home>/.env -- never in the plugin directory.")
    return 0


def cmd_sources(_args) -> int:
    from sources import load_sources

    for src in load_sources():
        print(f"{src.name:20} {src.title}")
        print(f"{'':20} {src.llms_txt}")
        print(f"{'':20} -> {src.dir}")
    return 0


def cmd_scrape(args) -> int:
    argv = []
    for name in args.source or []:
        argv += ["--source", name]
    if args.refresh:
        argv.append("--refresh")
    if args.list:
        argv.append("--list")
    return _run(PIPELINE_DIR / "scrape.py", *argv, label="scrape")


def cmd_build(_args) -> int:
    for stage in STAGES:
        code = _run(PIPELINE_DIR / f"{stage}.py", label=stage)
        if code:
            return code
    return 0


def cmd_index(args) -> int:
    argv = []
    if args.recreate:
        argv.append("--recreate")
    if args.check:
        argv.append("--check")
    return _run(HERE / "ingest.py", *argv, label="index")


def cmd_fetch(args) -> int:
    code = cmd_scrape(args)
    if code:
        return code
    code = cmd_build(args)
    if code:
        return code
    return cmd_index(args)


def cmd_status(_args) -> int:
    from pipeline.common import read_jsonl

    root = paths.ensure_home()
    print(f"data home : {root}")
    print(f"registry  : {paths.sources_yaml()} (exists={paths.sources_yaml().exists()})")

    src_root = paths.sources_root()
    if src_root.exists():
        for sub in sorted(p for p in src_root.iterdir() if p.is_dir()):
            raw = len(list((sub / "docs").rglob("*.md"))) if (sub / "docs").exists() else 0
            clean = len(list((sub / "clean").rglob("*.md"))) if (sub / "clean").exists() else 0
            print(f"  source {sub.name:12} docs={raw:<5} clean={clean}")
    else:
        print("  sources/  : not created yet")

    chunks = paths.corpus_dir() / "chunks.jsonl"
    if chunks.exists():
        rows = read_jsonl(chunks)
        by_source: dict[str, int] = {}
        for row in rows:
            by_source[row["corpus_source"]] = by_source.get(row["corpus_source"], 0) + 1
        print(f"  chunks    : {len(rows)} {by_source}")
    else:
        print("  chunks    : not built yet")

    qdrant = paths.qdrant_dir()
    print(f"  qdrant    : {qdrant} (exists={qdrant.exists()})")

    try:
        from store import DocsStore, Settings

        store = DocsStore(Settings.resolve())
        ok, info = store.health()
        print(f"  collection: {'OK ' if ok else 'FAIL'} {info}")
    except Exception as exc:  # noqa: BLE001
        print(f"  collection: unreachable ({exc.__class__.__name__}: {exc})")
    return 0


def cmd_search(args) -> int:
    from ingest import load_dotenv

    load_dotenv()
    from store import DocsStore, Settings

    store = DocsStore(Settings.resolve())
    results = store.search(
        args.query,
        limit=args.limit,
        doc_type=args.doc_type or None,
        source=args.source_filter or None,
    )
    if not results:
        print("no results")
        return 1
    for hit in results:
        print(f"[{hit['score']:.3f}] {hit['source']} | {hit['title']}")
        print(f"         {hit['source_url']}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="create the data home and seed sources.yaml").set_defaults(func=cmd_init)
    sub.add_parser("sources", help="list registered sources").set_defaults(func=cmd_sources)
    sub.add_parser("build", help="normalize -> enrich -> chunk").set_defaults(func=cmd_build)
    sub.add_parser("status", help="data home + corpus + collection state").set_defaults(func=cmd_status)

    p_scrape = sub.add_parser("scrape", help="download every llms.txt source")
    p_scrape.add_argument("--source", action="append")
    p_scrape.add_argument("--refresh", action="store_true")
    p_scrape.add_argument("--list", action="store_true")
    p_scrape.set_defaults(func=cmd_scrape)

    p_index = sub.add_parser("index", help="embed chunks.jsonl into Qdrant")
    p_index.add_argument("--recreate", action="store_true")
    p_index.add_argument("--check", action="store_true")
    p_index.set_defaults(func=cmd_index)

    p_fetch = sub.add_parser("fetch", help="scrape + build + index")
    p_fetch.add_argument("--source", action="append")
    p_fetch.add_argument("--refresh", action="store_true")
    p_fetch.add_argument("--list", action="store_true")
    p_fetch.add_argument("--recreate", action="store_true")
    p_fetch.add_argument("--check", action="store_true")
    p_fetch.set_defaults(func=cmd_fetch)

    p_search = sub.add_parser("search", help="run a retrieval smoke test")
    p_search.add_argument("query")
    p_search.add_argument("--limit", type=int, default=5)
    p_search.add_argument("--doc-type", dest="doc_type")
    p_search.add_argument("--from-source", dest="source_filter")
    p_search.set_defaults(func=cmd_search)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
