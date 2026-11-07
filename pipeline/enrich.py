"""Stage 2 - Enrich clean documents with retrieval metadata.

Reads:  sources/<name>/clean/**/*.md, sources/<name>/llms.txt
Writes: corpus/documents.jsonl  (one row per page, all sources)

Doc ids are source-qualified: `<source>:<path>`. Payloads carry `corpus_source`
so retrieval can filter or cite across a multi-source corpus.
"""

from __future__ import annotations

import sys

from common import (
    body_hash,
    breadcrumb_for,
    iter_sources,
    load_llms_index,
    lookup_llms_entry,
    parse_front_matter,
    path_for,
    qualify,
    write_jsonl,
)

# Pages whose body is rendered client-side; a supplement may be needed later.
STUB_MARKERS = ("Loading blueprints", "Loading plugins", "Loading skills")


def main() -> int:
    corpus = path_for("corpus")

    def documents():
        for source in iter_sources():
            if not source.clean_dir.exists():
                continue
            llms = load_llms_index(source.llms_path, source)

            for path in sorted(source.clean_dir.rglob("*.md")):
                text = path.read_text(encoding="utf-8")
                meta, body = parse_front_matter(text)
                rel_id = path.relative_to(source.clean_dir).with_suffix("").as_posix()
                doc_id = qualify(rel_id, source.name)
                source_url = meta.get("source", "").rstrip("/")
                entry = lookup_llms_entry(llms, source_url)

                yield {
                    "doc_id": doc_id,
                    "corpus_source": source.name,
                    "source_title": source.title,
                    "title": meta.get("title") or entry.get("title") or rel_id,
                    "source_url": source_url,
                "section": entry.get("section") or source.section_for(rel_id),
                "doc_summary": entry.get("summary", ""),
                    "breadcrumb": breadcrumb_for(rel_id),
                    "doc_type": source.doc_type(rel_id),
                    "lang": "en",
                    "content_hash": meta.get("content_hash") or body_hash(body),
                    "is_stub": any(marker in body for marker in STUB_MARKERS),
                    "char_count": len(body),
                    "body": body,
                }

    out_path = corpus / "documents.jsonl"
    n = write_jsonl(out_path, documents())
    print(f"enriched {n} documents across all sources -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
