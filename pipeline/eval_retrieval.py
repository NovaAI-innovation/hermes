"""Stage 6 - Retrieval evaluation harness.

Reads:  eval/queries.jsonl  ({"query": ..., "expected_doc_ids": [...]})
Writes: eval/last_run.json

Usage:
    python eval_retrieval.py
"""

from __future__ import annotations

import json
import sys

from common import path_for
from retrieve import search

K = 10


def main() -> int:
    eval_path = path_for("eval") / "queries.jsonl"
    if not eval_path.exists():
        print(f"missing {eval_path}", file=sys.stderr)
        return 1

    queries = [json.loads(line) for line in eval_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    rows = []
    hits = 0

    for item in queries:
        results = search(item["query"], top_k=30, final_k=K)
        got = [r["doc_id"] for r in results]
        expected = set(item["expected_doc_ids"])
        hit = bool(expected & set(got))
        hits += hit
        rank = next((i + 1 for i, d in enumerate(got) if d in expected), None)
        rows.append(
            {
                "query": item["query"],
                "expected": sorted(expected),
                "got": got,
                "hit": hit,
                "first_rank": rank,
            }
        )
        status = "PASS" if hit else "FAIL"
        print(f"[{status}] rank={rank} {item['query']}")

    summary = {
        "queries": len(queries),
        "hits": hits,
        f"recall@{K}": round(hits / max(len(queries), 1), 3),
        "misses": [r["query"] for r in rows if not r["hit"]],
        "k": K,
    }
    out = path_for("eval") / "last_run.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"summary": summary, "rows": rows}, indent=2), encoding="utf-8")

    print(f"\nrecall@{K} = {summary[f'recall@{K}']} ({hits}/{len(queries)}) -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
