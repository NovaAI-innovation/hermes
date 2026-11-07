"""Shared helpers for the post-scrape RAG pipeline."""

from __future__ import annotations

import hashlib
import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterator

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent / "config.yaml"


@lru_cache(maxsize=1)
def load_config() -> dict[str, Any]:
    with DEFAULT_CONFIG_PATH.open("r", encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh) or {}
    cfg["_root"] = str(ROOT)
    return cfg


def path_for(key: str) -> Path:
    cfg = load_config()
    return (ROOT / cfg["paths"][key]).resolve()


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


def doc_id_from_path(path: Path) -> str:
    rel = path.relative_to(path_for("raw_docs")).with_suffix("")
    return rel.as_posix()


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
    root = path_for("raw_docs")
    for path in sorted(root.rglob("*.md")):
        yield path


# ---------------------------------------------------------------- llms.txt

LLMS_LINK_RE = re.compile(
    r"\[([^\]]+)\]\((https://hermes-agent\.nousresearch\.com/docs/[^)]+)\)(?::\s*(.*))?"
)


def load_llms_index() -> dict[str, dict[str, str]]:
    """Map normalized URL -> {section, title, summary} from llms.txt."""
    index_path = path_for("llms_index")
    index: dict[str, dict[str, str]] = {}
    if not index_path.exists():
        return index
    section = ""
    for line in index_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            section = stripped[3:].strip()
            continue
        for title, url, summary in LLMS_LINK_RE.findall(line):
            index[url.rstrip("/")] = {
                "section": section,
                "title": title.strip(),
                "summary": (summary or "").strip(),
            }
    return index


DOC_TYPE_RULES: list[tuple[str, str]] = [
    ("reference/", "reference"),
    ("developer-guide/", "developer"),
    ("user-guide/messaging/", "messaging"),
    ("user-guide/features/", "feature"),
    ("user-guide/", "guide"),
    ("getting-started/", "getting-started"),
    ("guides/", "guide"),
    ("integrations/", "guide"),
]


def classify_doc(doc_id: str) -> str:
    for prefix, kind in DOC_TYPE_RULES:
        if doc_id.startswith(prefix):
            return kind
    return "default"


def breadcrumb_for(doc_id: str) -> list[str]:
    return [part.replace("-", " ").title() for part in doc_id.split("/")]
