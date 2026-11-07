"""Stage 1 - Normalize scraped markdown: strip generator chrome, keep article body.

Reads:  sources/<name>/docs/**/*.md
Writes: sources/<name>/clean/**/*.md
        corpus/normalize_report.json

Chrome patterns are configurable per source in sources.yaml under
`normalize.footer_markers`; defaults cover Docusaurus and most doc sites.
"""

from __future__ import annotations

import json
import re
import sys

from common import body_hash, iter_sources, load_config, parse_front_matter, path_for

# --- generic chrome patterns ----------------------------------------------

# Heading permalink junk: ## Title[](url "Direct link to Title")
ANCHOR_RE = re.compile(r'\[[^\]]*\]\([^)]*?(?:"Direct link to [^"]*"|"[^"]*anchor[^"]*")\)')
EMPTY_LINK_RE = re.compile(r"\[\s*\u200b?\s*\]\([^)]*\)")
ZWSP_RE = re.compile(r"\u200b")
H1_RE = re.compile(r"^# \S")
SKIP_TO_CONTENT_RE = re.compile(r"^\[Skip to main content\]")
ON_THIS_PAGE_RE = re.compile(r"^On this page\s*$")
SIDEBAR_BULLET_RE = re.compile(
    r"^\s*[\*\-]\s+\[[^\]]+\]\(https?://[^)]+\)\s*$"
)

DEFAULT_FOOTER_MARKERS = [
    r"^\[.*\]\(https://github\.com/[^)]*/edit/",
    r"^Built by \[",
    r"^Docs\s*$",
    r"^Community\s*$",
    r"^More\s*$",
]


def footer_patterns(source) -> list[re.Pattern]:
    markers = (source.normalize or {}).get("footer_markers") or DEFAULT_FOOTER_MARKERS
    return [re.compile(m) for m in markers]


def slice_body(
    lines: list[str], footers: list[re.Pattern], strip_sidebar: bool = True
) -> tuple[list[str], int, int]:
    """Return (content lines, lines stripped from head, lines stripped from tail)."""
    start = 0
    tail = len(lines)

    h1 = next((i for i, line in enumerate(lines) if H1_RE.match(line)), None)
    if h1 is not None:
        start = h1
    else:
        on_page = next(
            (i for i, line in enumerate(lines) if ON_THIS_PAGE_RE.match(line)), None
        )
        if on_page is not None:
            start = on_page + 1
        else:
            skip = next(
                (i for i, line in enumerate(lines) if SKIP_TO_CONTENT_RE.match(line)),
                None,
            )
            start = 0 if skip is None else skip + 1

    for i in range(start, len(lines)):
        if any(p.match(lines[i]) for p in footers):
            tail = i
            break

    content = lines[start:tail]
    if strip_sidebar:
        content = [line for line in content if not SIDEBAR_BULLET_RE.match(line)]
    return content, start, len(lines) - tail


def clean_text(text: str) -> str:
    text = ANCHOR_RE.sub("", text)
    text = EMPTY_LINK_RE.sub("", text)
    text = ZWSP_RE.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return text.strip() + "\n"


def render_front_matter(meta: dict[str, str]) -> str:
    fields = ["title", "source", "scraped_at", "doc_id", "content_hash", "corpus_source"]
    out = ["---"]
    for key in fields:
        if meta.get(key):
            out.append(f'{key}: "{str(meta[key]).replace(chr(34), chr(39))}"')
    out.append("---")
    return "\n".join(out) + "\n\n"


def main() -> int:
    cfg = load_config()
    corpus = path_for("corpus")
    report: dict = {"sources": {}, "warnings": [], "skipped": []}

    for source in iter_sources():
        if not source.docs_dir.exists():
            report["sources"][source.name] = {"documents": 0, "missing": True}
            print(f"  {source.name}: no scraped docs, skipping")
            continue

        footers = footer_patterns(source)
        docs = 0
        raw_bytes = clean_bytes = 0
        written: set[Path] = set()
        manifest = source.dir / "pages.json"
        active = set(json.loads(manifest.read_text(encoding="utf-8"))) if manifest.is_file() else None

        for raw_path in sorted(source.docs_dir.rglob("*.md")):
            rel = raw_path.relative_to(source.docs_dir)
            if active is not None and rel.as_posix() not in active:
                continue
            meta, body = parse_front_matter(raw_path.read_text(encoding="utf-8"))
            if meta.get("source") and not source.allows(meta["source"]):
                continue

            if meta.get("success", "True").lower() == "false":
                report["skipped"].append(
                    {"source": source.name, "path": rel.as_posix(), "reason": "scrape failed"}
                )
                continue

            content, head_cut, tail_cut = slice_body(
                body.splitlines(), footers, cfg["normalize"].get("strip_sidebar", True)
            )
            cleaned = clean_text("\n".join(content))
            if len(cleaned) < 200:
                report["warnings"].append(
                    {
                        "source": source.name,
                        "path": rel.as_posix(),
                        "chars": len(cleaned),
                    }
                )

            doc_id = rel.with_suffix("").as_posix()
            out_meta = {
                "title": meta.get("title", doc_id),
                "source": meta.get("source", ""),
                "scraped_at": meta.get("scraped_at", ""),
                "doc_id": doc_id,
                "content_hash": body_hash(cleaned),
                "corpus_source": source.name,
            }

            out_path = source.clean_dir / rel
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(render_front_matter(out_meta) + cleaned, encoding="utf-8")
            written.add(out_path)

            docs += 1
            raw_bytes += len(body)
            clean_bytes += len(cleaned)
            report["sources"].setdefault(source.name, {})
            report["sources"][source.name].update(
                {
                    "documents": docs,
                    "raw_chars": raw_bytes,
                    "clean_chars": clean_bytes,
                    "last_head_stripped": head_cut,
                    "last_tail_stripped": tail_cut,
                }
            )

        pct = 100 * (1 - clean_bytes / raw_bytes) if raw_bytes else 0.0
        print(f"  {source.name}: {docs} docs, {raw_bytes:,} -> {clean_bytes:,} chars ({pct:.1f}% removed)")

        # Remove normalized files whose source page no longer exists (pruned
        # versions, dropped URLs). Without this, deleted pages keep feeding the
        # corpus from stale clean/ output.
        removed = 0
        if source.clean_dir.exists():
            for stale in source.clean_dir.rglob("*.md"):
                if stale not in written:
                    stale.unlink()
                    removed += 1
            for folder in sorted(source.clean_dir.rglob("*"), reverse=True):
                if folder.is_dir() and not any(folder.iterdir()):
                    folder.rmdir()
        if removed:
            print(f"  {source.name}: removed {removed} stale normalized files")

    report_path = corpus / "normalize_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"normalize report -> {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
