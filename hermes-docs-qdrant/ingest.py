"""Ingest the scraped Hermes docs corpus into Qdrant.

    python ingest.py --chunks <data home>/corpus/chunks.jsonl --recreate
    python ingest.py --url http://localhost:6333 --collection hermes_docs
    python ingest.py --check          # connectivity + point count only

Embeddings: dense via OpenRouter qwen/qwen3-embedding-4b (2,560 dim),
sparse via FastEmbed Qdrant/bm25. Reuses pipeline/embedder.py when available.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from store import DEFAULT_COLLECTION, DocsStore, Settings, ingest  # noqa: E402
from pipeline import paths  # noqa: E402


def load_dotenv() -> None:
    """Load the plugin's own .env, then the process env. Real env vars win."""
    for candidate in (paths.env_file(), Path(__file__).resolve().parent.parent / ".env"):
        if not candidate.exists():
            continue
        for line in candidate.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def main() -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--chunks",
        type=Path,
        default=paths.corpus_dir() / "chunks.jsonl",
    )
    parser.add_argument("--url", default=os.getenv("QDRANT_URL"))
    parser.add_argument("--api-key", default=os.getenv("QDRANT_API_KEY"))
    parser.add_argument("--path", default=os.getenv("QDRANT_PATH"))
    parser.add_argument("--collection", default=os.getenv("HERMES_DOCS_COLLECTION", DEFAULT_COLLECTION))
    parser.add_argument("--recreate", action="store_true", help="build and publish a replacement collection")
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--limit", type=int, default=None, help="ingest only the first N chunks")
    parser.add_argument("--check", action="store_true", help="connectivity check only")
    parser.add_argument(
        "--query", default=None, help="run a test query after ingest"
    )
    parser.add_argument("--data-dir", default=os.getenv("HERMES_DOCS_DATA"))
    args = parser.parse_args()

    if args.data_dir:
        os.environ["HERMES_DOCS_DATA"] = args.data_dir

    settings = Settings.resolve(
        {
            "url": args.url,
            "api_key": args.api_key,
            "path": args.path,
            "collection": args.collection,
        }
    )

    if args.check:
        store = DocsStore(settings)
        ok, detail = store.health()
        target = settings.url or settings.path
        print(f"{'OK' if ok else 'FAIL'}  collection={settings.collection}  target={target}\n      {detail}")
        return 0 if ok else 1

    if not args.chunks.exists():
        print(f"chunks file not found: {args.chunks}", file=sys.stderr)
        return 1

    def progress(done: int, total: int) -> None:
        if done % 256 == 0 or done == total:
            print(f"  upserted {done}/{total}", flush=True)

    stats = ingest(
        args.chunks,
        settings,
        recreate=args.recreate,
        batch_size=args.batch_size,
        limit=args.limit,
        progress=progress,
    )
    print(
        f"ingested {stats['upserted']} points into '{stats['collection']}' "
        f"in {stats['seconds']}s (sparse={stats['sparse']})"
    )

    if args.query:
        results = DocsStore(settings).search(args.query)
        print(f"\nquery: {args.query}")
        for n, r in enumerate(results, 1):
            print(f"  [{n}] {r['score']:.3f}  {r['title']} > {r['heading']}")
            print(f"      {r['source_url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
