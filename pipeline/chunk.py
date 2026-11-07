"""Stage 3 - Header-aware chunking into retrieval units.

Reads:  corpus/documents.jsonl
Writes: corpus/chunks.jsonl, corpus/parents.jsonl
"""

from __future__ import annotations

import re
import sys

from common import (
    count_tokens,
    load_config,
    path_for,
    read_jsonl,
    slugify,
    write_jsonl,
)

HEADING_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def split_sections(body: str) -> list[tuple[str, str, str]]:
    """Split markdown into (level, heading, text) with the heading included in text.

    Sections start at H2; H3/H4 stay with their parent section and are only
    split further when a section exceeds the hard token cap.
    """
    lines = body.splitlines()
    sections: list[tuple[str, str, str]] = []
    current_heading = ""
    current = []
    in_fence = False
    seen_h2 = False

    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence

        if not in_fence:
            match = HEADING_RE.match(line)
            if match:
                level, title = match.group(1), match.group(2)
                if len(level) == 2:
                    if seen_h2 or current:
                        sections.append(("preamble", current_heading, "\n".join(current).strip()))
                    current = [line]
                    current_heading = title
                    seen_h2 = True
                    continue
                if not seen_h2 and not current_heading:
                    current_heading = title
        current.append(line)

    if current:
        sections.append(("section", current_heading, "\n".join(current).strip()))

    return [s for s in sections if s[2].strip()]


def split_long(text: str, heading: str, target_max: int) -> list[str]:
    """Split an oversized section at H3/H4 boundaries, then by paragraph."""
    lines = text.splitlines()
    parts: list[list[str]] = []
    current: list[str] = []
    in_fence = False

    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
        if not in_fence and re.match(r"^#{3,4}\s+", line) and current:
            parts.append(current)
            current = [line]
            continue
        current.append(line)
    if current:
        parts.append(current)

    chunks: list[str] = []
    for part in parts:
        blob = "\n".join(part).strip()
        if not blob:
            continue
        if count_tokens(blob) <= target_max:
            chunks.append(blob)
            continue
        # Paragraph fallback, keeping fenced blocks intact.
        buf: list[str] = []
        in_fence = False
        for para in re.split(r"\n\s*\n", blob):
            if FENCE_RE.search(para.splitlines()[0] if para.splitlines() else ""):
                in_fence = not in_fence
            candidate = "\n\n".join([*buf, para]) if buf else para
            if count_tokens(candidate) > target_max and buf:
                chunks.append("\n\n".join(buf).strip())
                buf = [para]
            else:
                buf.append(para)
        if buf:
            chunks.append("\n\n".join(buf).strip())

    return chunks


TABLE_ROW_RE = re.compile(r"^\s*\|")


def hard_split(text: str, target_max: int) -> list[str]:
    """Last-resort split by lines for pages with no headings or paragraphs.

    Table rows are packed individually and the header/separator is repeated on
    every continued piece so each chunk stays readable on its own.
    """
    lines = text.splitlines()
    header: list[str] = []
    if len(lines) >= 2 and TABLE_ROW_RE.match(lines[0]) and TABLE_ROW_RE.match(lines[1]):
        header = lines[:2]
        lines = lines[2:]

    # Prefer splitting before folded list items / headings / blank lines.
    chunks: list[str] = []
    buf: list[str] = list(header)
    buf_tokens = count_tokens("\n".join(buf))
    in_fence = False

    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
        cost = count_tokens(line) + 1
        if buf_tokens + cost > target_max and len(buf) > len(header):
            chunks.append("\n".join(buf).strip())
            buf = list(header)
            buf_tokens = count_tokens("\n".join(buf))
        buf.append(line)
        buf_tokens += cost

    if buf:
        chunks.append("\n".join(buf).strip())

    # Final fallback: a single unbroken line (e.g. a scraped tile blob).
    final: list[str] = []
    for chunk in chunks:
        if count_tokens(chunk) <= target_max:
            final.append(chunk)
            continue
        final.extend(split_by_sentence(chunk, target_max))

    return [c for c in final if c]


SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")


def split_by_sentence(text: str, target_max: int) -> list[str]:
    pieces = SENTENCE_SPLIT_RE.split(text)
    out: list[str] = []
    buf: list[str] = []
    for piece in pieces:
        candidate = " ".join([*buf, piece]) if buf else piece
        if count_tokens(candidate) > target_max and buf:
            out.append(" ".join(buf).strip())
            buf = [piece]
        else:
            buf.append(piece)
    if buf:
        out.append(" ".join(buf).strip())

    # Last resort: hard word windows.
    result: list[str] = []
    for chunk in out:
        if count_tokens(chunk) <= target_max:
            result.append(chunk)
            continue
        words = chunk.split()
        window: list[str] = []
        for word in words:
            candidate = " ".join([*window, word]) if window else word
            if count_tokens(candidate) > target_max and window:
                result.append(" ".join(window))
                window = [word]
            else:
                window.append(word)
        if window:
            result.append(" ".join(window))
    return result


def main() -> int:
    cfg = load_config()
    doc_cfg = cfg["chunk"]
    targets = doc_cfg["targets"]
    hard_max = doc_cfg["max_tokens_hard"]
    prefix_summary = doc_cfg["prefix_doc_summary"]

    documents = read_jsonl(path_for("corpus") / "documents.jsonl")

    def parents():
        for doc in documents:
            yield {
                "chunk_id": f"{doc['doc_id']}#__parent__",
                "doc_id": doc["doc_id"],
                "chunk_type": "parent",
                "title": doc["title"],
                "heading": doc["title"],
                "text": f"{doc['title']}. {doc['doc_summary']}".strip(),
                "source_url": doc["source_url"],
                "section": doc["section"],
                "breadcrumb": doc["breadcrumb"],
                "doc_summary": doc["doc_summary"],
                "doc_type": doc["doc_type"],
            }

    def chunks():
        for doc in documents:
            _, target_max = targets.get(doc["doc_type"], targets["default"])
            sections = split_sections(doc["body"])
            body_heading_counts: dict[str, int] = {}

            for kind, heading, text in sections:
                pieces = (
                    [text]
                    if count_tokens(text) <= hard_max
                    else split_long(text, heading, target_max)
                )
                for piece in pieces:
                    if count_tokens(piece) > hard_max:
                        piece_list = hard_split(piece, hard_max)
                    else:
                        piece_list = [piece]
                    for piece in piece_list:
                        if count_tokens(piece) < 25:
                            continue  # drop stubs like "Loading..."
                        slug = slugify(heading or doc["title"])
                        n = body_heading_counts.get(slug, 0)
                        body_heading_counts[slug] = n + 1
                        suffix = f"~{n}" if n else ""
                        embed_text = (
                            f"{doc['title']} - {doc['doc_summary']}\n\n{piece}"
                            if prefix_summary and doc["doc_summary"]
                            else piece
                        )
                        yield {
                            "chunk_id": f"{doc['doc_id']}#{slug}{suffix}",
                            "doc_id": doc["doc_id"],
                            "chunk_type": "section" if kind != "preamble" else "preamble",
                            "title": doc["title"],
                            "heading": heading or doc["title"],
                            "text": piece,
                            "embed_text": embed_text,
                            "source_url": doc["source_url"],
                            "section": doc["section"],
                            "breadcrumb": doc["breadcrumb"],
                            "doc_summary": doc["doc_summary"],
                            "doc_type": doc["doc_type"],
                            "token_count": count_tokens(piece),
                            "content_hash": doc["content_hash"],
                        }

    corpus = path_for("corpus")
    n_parents = write_jsonl(corpus / "parents.jsonl", parents())
    n_chunks = write_jsonl(corpus / "chunks.jsonl", chunks())
    print(f"wrote {n_chunks} chunks and {n_parents} parent docs -> {corpus}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
