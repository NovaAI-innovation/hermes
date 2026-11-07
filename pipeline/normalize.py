"""Stage 1 - Normalize scraped markdown: strip Docusaurus chrome, keep article body.

Reads:  docs/**/*.md
Writes: clean/**/*.md  (article-only markdown with YAML front matter)
        corpus/normalize_report.json
"""

from __future__ import annotations

import json
import re
import sys

from common import (
    body_hash,
    iter_raw_docs,
    load_config,
    parse_front_matter,
    path_for,
)

# --- chrome patterns -------------------------------------------------------

# Heading permalink junk: ## Title[​](https://... "Direct link to Title")
ANCHOR_RE = re.compile(r'\[[^\]]*\]\([^)]*?"Direct link to [^"]*"\)')
# Anchor-only links ([] (url)) and zero-width-space link text
EMPTY_LINK_RE = re.compile(r"\[\s*\u200b?\s*\]\([^)]*\)")
ZWSP_RE = re.compile(r"\u200b")

# Sidebar/nav bullets all point at site URLs; the article body rarely starts
# with one. Content starts at the first H1 outside a fence.
H1_RE = re.compile(r"^# \S")
SKIP_TO_CONTENT_RE = re.compile(r"^\[Skip to main content\]")
ON_THIS_PAGE_RE = re.compile(r"^On this page\s*$")

# Footer markers, in priority order.
FOOTER_MARKERS = [
    re.compile(r"^\[.*\]\(https://github\.com/NousResearch/hermes-agent/edit/"),
    re.compile(r"^Docs\s*$"),
    re.compile(r"^Built by \[Nous Research\]"),
]

BREADCRUMB_ROOT_RE = re.compile(
    r"^\s*\* \[\]\(https://hermes-agent\.nousresearch\.com/docs/?\)\s*$"
)

SITE_PREFIX = "https://hermes-agent.nousresearch.com/docs/"
SITE_LINK_RE = re.compile(r"\]\(" + re.escape(SITE_PREFIX) + r"([^)\s]*)\)")


def slice_body(lines: list[str]) -> tuple[list[str], int, int]:
    """Return (content lines, lines strip from head, lines stripped from tail)."""
    start = 0
    tail = len(lines)

    # Head: prefer the breadcrumb root block that precedes the article H1,
    # else the first H1, else just after "On this page".
    h1 = next(
        (i for i, line in enumerate(lines) if H1_RE.match(line)),
        None,
    )
    if h1 is not None:
        start = h1
    else:
        on_page = next(
            (i for i, line in enumerate(lines) if ON_THIS_PAGE_RE.match(line)),
            None,
        )
        if on_page is not None:
            start = on_page + 1
        else:
            skip = next(
                (i for i, line in enumerate(lines) if SKIP_TO_CONTENT_RE.match(line)),
                None,
            )
            start = 0 if skip is None else skip

    # Tail: first footer marker after the content starts.
    for i in range(start, len(lines)):
        if any(marker.match(lines[i]) for marker in FOOTER_MARKERS):
            tail = i
            break

    return lines[start:tail], start, len(lines) - tail


def clean_text(text: str) -> str:
    text = ANCHOR_RE.sub("", text)
    text = EMPTY_LINK_RE.sub("", text)
    text = ZWSP_RE.sub("", text)
    # Same-site absolute URLs -> site-relative, cheaper tokens and no nav noise
    text = SITE_LINK_RE.sub(r"](/docs/\1)", text)
    text = text.replace(SITE_PREFIX.rstrip("/"), "/docs")
    # Collapse >2 blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Trim trailing spaces on lines
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return text.strip() + "\n"


def render_front_matter(meta: dict[str, str]) -> str:
    fields = ["title", "source", "scraped_at", "doc_id", "content_hash"]
    out = ["---"]
    for key in fields:
        if meta.get(key):
            value = meta[key].replace('"', "'")
            out.append(f'{key}: "{value}"')
    out.append("---")
    return "\n".join(out) + "\n\n"


def main() -> int:
    cfg = load_config()
    raw_root = path_for("raw_docs")
    clean_root = path_for("clean_docs")
    report: dict = {"documents": 0, "skipped": [], "warnings": [], "bytes": {}}

    for raw_path in iter_raw_docs():
        rel = raw_path.relative_to(raw_root)
        if cfg["normalize"]["drop_zh_hans"] and "zh-Hans" in rel.as_posix():
            report["skipped"].append({"path": rel.as_posix(), "reason": "zh-Hans"})
            continue

        text = raw_path.read_text(encoding="utf-8")
        meta, body = parse_front_matter(text)

        if meta.get("success", "True").lower() == "false":
            report["skipped"].append({"path": rel.as_posix(), "reason": "scrape failed"})
            continue

        content, head_cut, tail_cut = slice_body(body.splitlines())
        cleaned = clean_text("\n".join(content))

        if len(cleaned) < 200:
            report["warnings"].append(
                {"path": rel.as_posix(), "reason": "short after clean", "chars": len(cleaned)}
            )

        doc_id = rel.with_suffix("").as_posix()
        out_meta = {
            "title": meta.get("title", doc_id),
            "source": meta.get("source", ""),
            "scraped_at": meta.get("scraped_at", ""),
            "doc_id": doc_id,
            "content_hash": body_hash(cleaned),
        }

        out_path = clean_root / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(render_front_matter(out_meta) + cleaned, encoding="utf-8")

        report["documents"] += 1
        report["bytes"][doc_id] = {
            "raw": len(body),
            "clean": len(cleaned),
            "head_stripped": head_cut,
            "tail_stripped": tail_cut,
        }

    report_path = path_for("corpus") / "normalize_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    total_raw = sum(v["raw"] for v in report["bytes"].values()) or 1
    total_clean = sum(v["clean"] for v in report["bytes"].values())
    print(
        f"normalized {report['documents']} docs -> {clean_root}\n"
        f"chars: {total_raw:,} -> {total_clean:,} "
        f"({100 * (1 - total_clean / total_raw):.1f}% removed), "
        f"{len(report['warnings'])} warnings, {len(report['skipped'])} skipped"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
