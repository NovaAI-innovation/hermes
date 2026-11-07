"""Stage 5 - Hybrid retrieval over the built indexes.

Usage:
    python retrieve.py "how do I schedule a recurring cron job"
    python retrieve.py --json "telegram gateway setup"

Prints ranked chunks with citation URLs.
"""

from __future__ import annotations

import argparse
import json
import pickle
import sys

from common import load_config, path_for, read_jsonl

_CACHE: dict = {}


def load_indexes():
    if _CACHE:
        return _CACHE

    import faiss

    from embedder import get_embedder

    cfg = load_config()
    corpus = path_for("corpus")
    index_dir = corpus / "index"

    manifest = json.loads((index_dir / "manifest.json").read_text(encoding="utf-8"))
    with (index_dir / "bm25.pkl").open("rb") as fh:
        bm25_blob = pickle.load(fh)

    embedder = get_embedder()
    if embedder.signature != manifest["embed_signature"]:
        raise RuntimeError(
            f"embedding mismatch: index built with '{manifest['embed_signature']}', "
            f"config says '{embedder.signature}'. Re-run index.py."
        )

    _CACHE.update(
        cfg=cfg,
        chunks=read_jsonl(corpus / "chunks.jsonl"),
        manifest=manifest,
        faiss=faiss.read_index(str(index_dir / "dense.faiss")),
        bm25=bm25_blob["bm25"],
        embedder=embedder,
    )
    return _CACHE


def tokenize(text: str) -> list[str]:
    return [t for t in text.lower().split() if any(c.isalnum() for c in t)]


def normalize_scores(scores) -> list[float]:
    import numpy as np

    arr = np.asarray(scores, dtype="float32")
    if arr.size == 0:
        return []
    lo, hi = float(arr.min()), float(arr.max())
    if hi - lo < 1e-9:
        return [0.0 for _ in arr]
    return ((arr - lo) / (hi - lo)).tolist()


def search(
    query: str,
    top_k: int | None = None,
    final_k: int | None = None,
    doc_type: str | None = None,
) -> list[dict]:
    state = load_indexes()
    cfg = state["cfg"]
    chunks = state["chunks"]
    top_k = top_k or cfg["retrieve"]["top_k"]
    final_k = final_k or cfg["retrieve"]["final_k"]

    allowed = {
        i for i, c in enumerate(chunks) if not doc_type or c["doc_type"] == doc_type
    }

    # Dense
    import numpy as np

    query_vec = np.asarray([state["embedder"].embed_query(query)], dtype="float32")
    if state["manifest"]["normalized"]:
        import faiss

        faiss.normalize_L2(query_vec)
    dense_scores, dense_idx = state["faiss"].search(query_vec, min(len(chunks), top_k * 4))
    dense = {
        int(i): float(s)
        for i, s in zip(dense_idx[0], dense_scores[0])
        if int(i) in allowed
    }

    # Sparse
    bm25_scores = state["bm25"].get_scores(tokenize(query))
    sparse = {i: float(bm25_scores[i]) for i in allowed if bm25_scores[i] > 0}

    weight = cfg["retrieve"]["dense_weight"]
    dn = normalize_scores(list(dense.values()))
    dense_norm = {i: s for i, s in zip(dense.keys(), dn)}
    sparse_norm = {i: s for i, s in zip(sparse.keys(), normalize_scores(list(sparse.values())))}

    combined: dict[int, float] = {}
    for i, score in dense_norm.items():
        combined[i] = weight * score
    for i, score in sparse_norm.items():
        combined[i] = combined.get(i, 0.0) + (1 - weight) * score

    ranked = sorted(combined.items(), key=lambda kv: kv[1], reverse=True)

    # De-duplicate near-identical adjacent pieces from the same section.
    results: list[dict] = []
    seen: set[str] = set()
    for i, score in ranked:
        chunk = chunks[i]
        base_id = chunk["chunk_id"].split("~")[0]
        if base_id in seen:
            continue
        seen.add(base_id)
        results.append({**chunk, "score": round(score, 4)})
        if len(results) >= final_k:
            break

    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Hybrid retrieval over the Hermes docs corpus")
    parser.add_argument("query")
    parser.add_argument("--top-k", type=int, default=None)
    parser.add_argument("--final-k", type=int, default=None)
    parser.add_argument("--doc-type", default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    results = search(args.query, args.top_k, args.final_k, args.doc_type)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0

    for n, r in enumerate(results, 1):
        print(f"\n[{n}] {r['score']:.3f}  {r['title']}  >  {r['heading']}")
        print(f"    {r['source_url']}#{r['chunk_id'].split('#')[-1]}")
        snippet = r["text"][:400].replace("\n", " ")
        print(f"    {snippet}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
