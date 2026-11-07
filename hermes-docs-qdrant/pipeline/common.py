"""Shared helpers for the post-scrape RAG pipeline."""

from __future__ import annotations

import hashlib
import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterator

import yaml

import paths
from sources import Source, iter_sources, load_sources

ROOT = paths.PLUGIN_DIR
DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent / "config.yaml"


@lru_cache(maxsize=1)
def load_config() -> dict[str, Any]:
    with DEFAULT_CONFIG_PATH.open("r", encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh) or {}
    cfg["_root"] = str(paths.home())
    return cfg


_PATHS = {
    "sources": paths.sources_root,
    "corpus": paths.corpus_dir,
    "eval": lambda: paths.ensure_home() / "eval",
}


def path_for(key: str) -> Path:
    """Resolve a configured output path inside the plugin data home.

    Directories are never resolved relative to the install tree: the install
    tree is replaced on `hermes plugins update`.
    """
    resolver = _PATHS.get(key)
    if resolver is not None:
        return resolver().resolve()
    cfg = load_config()
    return (paths.ensure_home() / cfg["paths"][key]).resolve()


FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Return (front matter dict, body). Tolerates missing front matter."""
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text
    raw = match.group(1)
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, text[match.end() :]


def body_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


@lru_cache(maxsize=1)
def _encoder():
    import tiktoken

    return tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    return len(_encoder().encode(text, disallowed_special=()))


def slugify(text: str, limit: int = 60) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:limit] or "section"


def write_jsonl(path: Path, rows: Iterator[dict] | list[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            n += 1
    return n


def read_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def iter_raw_docs() -> Iterator[Path]:
    """Every scraped markdown file across all sources."""
    for source in iter_sources():
        if not source.docs_dir.exists():
            continue
        for path in sorted(source.docs_dir.rglob("*.md")):
            yield path


# ---------------------------------------------------------------- llms.txt

# Generic markdown link: [title](url) with an optional ": description" suffix.
# Matches any absolute http(s) URL so non-Hermes llms.txt files work too.
LLMS_LINK_RE = re.compile(
    r"\[([^\]]+)\]\((https?://[^)\s]+)\)(?::\s*(.*))?"
)


def load_llms_index(path: Path, source=None) -> dict[str, dict[str, str]]:
    """Map normalized URL -> {section, title, summary} from one llms.txt.

    When a Source is supplied, its include/exclude rules are applied so the
    index matches exactly what will be scraped.
    """
    index: dict[str, dict[str, str]] = {}
    if not path.exists():
        return index
    section = ""
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        heading = re.match(r"^(#{2,3})\s+(.*)$", stripped)
        if heading:
            section = heading.group(2).strip()
            continue
        for title, url, summary in LLMS_LINK_RE.findall(line):
            url = url.rstrip("/")
            if source is not None and not source.allows(url):
                continue
            index.setdefault(
                url,
                {
                    "section": section,
                    "title": title.strip(),
                    "summary": (summary or "").strip(),
                },
            )
    return index


def breadcrumb_for(doc_id: str) -> list[str]:
    return [part.replace("-", " ").title() for part in doc_id.split("/")]


def _strip_ext(url: str) -> str:
    return re.sub(r"\.(md|mdx|markdown|html?)$", "", url, flags=re.IGNORECASE)


def lookup_llms_entry(llms: dict[str, dict[str, str]], source_url: str) -> dict[str, str]:
    """Match a page to its llms.txt entry, tolerating .md/.html suffixes.

    llms.txt commonly lists `.../page.md` while the scraped front matter records
    the canonical `.../page`. Normalize both sides before comparing.
    """
    if not source_url:
        return {}
    url = source_url.rstrip("/")
    for candidate in (url, _strip_ext(url)):
        if candidate in llms:
            return llms[candidate]
        # llms index keys may themselves carry an extension.
        stripped = _strip_ext(candidate)
        for key, entry in llms.items():
            if _strip_ext(key.rstrip("/")) == stripped:
                return entry
    return {}
    """Source-qualified doc id: '<source>:<path>'. Idempotent."""
    if not source_name or doc_id.startswith(f"{source_name}:"):
        return doc_id
def qualify(doc_id: str, source_name: str | None) -> str:
    """Source-qualified doc id: '<source>:<path>'. Idempotent."""
    if not source_name or doc_id.startswith(f"{source_name}:"):
        return doc_id
    return f"{source_name}:{doc_id}"


def split_doc_id(doc_id: str) -> tuple[str | None, str]:
    """'hermes:user-guide/cli' -> ('hermes', 'user-guide/cli')."""
    source, sep, rest = doc_id.partition(":")
    if sep and "/" not in source and rest:
        return source, rest
    return None, doc_id
