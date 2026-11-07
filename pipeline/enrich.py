"""Stage 2 - Enrich clean documents with retrieval metadata.

Reads:  clean/**/*.md, llms.txt
Writes: corpus/documents.jsonl
"""

from __future__ import annotations

import sys

from common import (
    body_hash,
    breadcrumb_for,
    classify_doc,
    iter_raw_docs,
    load_llms_index,
    parse_front_matter,
    path_for,
    write_jsonl,
)

# Pages whose body is rendered client-side; a sidecar supplement may be needed.
STUB_MARKERS = ("Loading blueprints", "Loading plugins", "Loading skills")


def main() -> int:
    clean_root = path_for("clean_docs")
    llms = load_llms_index()

    def documents():
        for path in sorted(clean_root.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            meta, body = parse_front_matter(text)
            doc_id = path.relative_to(clean_root).with_suffix("").as_posix()
            source = meta.get("source", "").rstrip("/")
            entry = llms.get(source, {})

            yield {
                "doc_id": doc_id,
                "title": meta.get("title") or entry.get("title") or doc_id,
                "source_url": source,
                "section": entry.get("section", ""),
                "doc_summary": entry.get("summary", ""),
                "breadcrumb": breadcrumb_for(doc_id),
                "doc_type": classify_doc(doc_id),
                "lang": "en",
                "content_hash": meta.get("content_hash") or body_hash(body),
                "is_stub": any(marker in body for marker in STUB_MARKERS),
                "char_count": len(body),
                "body": body,
            }

    out_path = path_for("corpus") / "documents.jsonl"
    n = write_jsonl(out_path, documents())
    print(f"enriched {n} documents -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
