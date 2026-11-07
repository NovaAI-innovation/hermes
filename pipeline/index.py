"""Stage 4 - Build hybrid indexes (dense FAISS + sparse BM25).

Reads:  corpus/chunks.jsonl
Writes: corpus/index/dense.faiss, corpus/index/bm25.pkl, corpus/index/manifest.json
"""

from __future__ import annotations

import json
import pickle
import sys
import time

from common import load_config, path_for, read_jsonl

DENSE_INDEX = "dense.faiss"
BM25_INDEX = "bm25.pkl"


def main() -> int:
    cfg = load_config()
    embed_cfg = cfg["embed"]
    corpus = path_for("corpus")
    index_dir = corpus / "index"
    index_dir.mkdir(parents=True, exist_ok=True)

    chunks = read_jsonl(corpus / "chunks.jsonl")
    if not chunks:
        print("no chunks found; run chunk.py first", file=sys.stderr)
        return 1

    # --- BM25 ------------------------------------------------------------
    from rank_bm25 import BM25Okapi

    def tokenize(text: str) -> list[str]:
        return [t for t in text.lower().split() if t.isalnum() or any(c.isalnum() for c in t)]

    bm25_corpus = [tokenize(c["text"] + "\n" + c["title"] + "\n" + c["heading"]) for c in chunks]
    bm25 = BM25Okapi(
        bm25_corpus,
        k1=cfg["bm25"]["k1"],
        b=cfg["bm25"]["b"],
    )
    with (index_dir / BM25_INDEX).open("wb") as fh:
        pickle.dump({"bm25": bm25, "chunk_ids": [c["chunk_id"] for c in chunks]}, fh)
    print(f"bm25 built over {len(chunks)} chunks")

    # --- Dense -----------------------------------------------------------
    import faiss
    import numpy as np

    from embedder import get_embedder

    started = time.time()
    embedder = get_embedder()
    texts = [c.get("embed_text") or c["text"] for c in chunks]
    print(f"embedding {len(texts)} chunks with {embedder.describe()}")

    vectors = np.asarray(embedder.embed_documents(texts), dtype="float32")
    if embed_cfg["normalize"]:
        faiss.normalize_L2(vectors)

    dim = vectors.shape[1]
    faiss_index = faiss.IndexFlatIP(dim) if embed_cfg["normalize"] else faiss.IndexFlatL2(dim)
    faiss_index.add(vectors)
    faiss.write_index(faiss_index, str(index_dir / DENSE_INDEX))

    manifest = {
        "chunk_count": len(chunks),
        "embed_provider": embedder.provider,
        "embedding_model": embedder.model_name,
        "embed_signature": embedder.signature,
        "dimension": dim,
        "normalized": embed_cfg["normalize"],
        "metric": "inner_product" if embed_cfg["normalize"] else "l2",
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "build_seconds": round(time.time() - started, 1),
        "chunk_ids_file": "chunk_ids.jsonl",
    }
    with (index_dir / "chunk_ids.jsonl").open("w", encoding="utf-8") as fh:
        for c in chunks:
            fh.write(json.dumps({"chunk_id": c["chunk_id"]}, ensure_ascii=False) + "\n")

    (index_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(
        f"dense index: {len(chunks)} vectors, dim {dim}, "
        f"{manifest['build_seconds']}s -> {index_dir}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
