"""Source registry: turns sources.yaml into resolved, on-disk source entries.

Every pipeline stage iterates sources rather than a single hardcoded doc site.
A source is a described llms.txt plus the directories it owns on disk:

    sources/<name>/llms.txt
    sources/<name>/docs/...
    sources/<name>/clean/...
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator, Protocol
from urllib.parse import urlparse

import yaml

if __package__:
    from . import paths
else:
    import paths

# Version strings used as path segments by versioned documentation sites,
# e.g. 2024-11-05, 2026-07-28, v1.2, 5.0.
VERSION_SEGMENT_RE = re.compile(r"^(?:v?\d+(?:\.\d+)*|\d{4}-\d{2}-\d{2})$")


class DocLinkLike(Protocol):
    url: str


def _version_key(version: str) -> tuple:
    """Sort key so '2026-07-28' > '2025-11-25' > 'v1.10' > 'v1.9'."""
    return tuple(int(n) for n in re.findall(r"\d+", version)) or (0,)


@dataclass
class Source:
    name: str
    title: str
    llms_txt: str
    include: list[str] = field(default_factory=list)
    exclude: list[str] = field(default_factory=list)
    doc_types: list[tuple[str, str]] = field(default_factory=list)
    normalize: dict[str, Any] = field(default_factory=dict)
    prefer_latest_version: bool = False
    # Host whose links count as "own site" for path construction. Defaults to
    # the llms.txt host; set it when the index and the docs live on different
    # hosts (e.g. a regional index pointing at the primary docs domain).
    doc_host: str = ""
    root: Path = field(default_factory=Path)

    # -- paths ----------------------------------------------------------
    @property
    def dir(self) -> Path:
        return self.root / self.name

    @property
    def llms_path(self) -> Path:
        return self.dir / "llms.txt"

    @property
    def docs_dir(self) -> Path:
        return self.dir / "docs"

    @property
    def clean_dir(self) -> Path:
        return self.dir / "clean"

    @property
    def is_remote(self) -> bool:
        return self.llms_txt.startswith(("http://", "https://"))

    # -- matching -------------------------------------------------------
    def allows(self, url: str) -> bool:
        if self.include and not any(re.search(p, url) for p in self.include):
            return False
        return not any(re.search(p, url) for p in self.exclude)

    def doc_type(self, doc_id: str) -> str:
        """Match on source-relative path, then the full id, first rule wins."""
        for prefix, kind in self.doc_types:
            if doc_id.startswith(prefix) or f"/{prefix}" in doc_id:
                return kind
        return "default"

    def section_for(self, doc_id: str, llms_section: str = "") -> str:
        """llms.txt section heading, else the first meaningful path segment."""
        if llms_section:
            return llms_section
        for part in doc_id.split("/"):
            if VERSION_SEGMENT_RE.fullmatch(part):
                continue
            if part and part not in {"docs", "documentation"}:
                return part.replace("-", " ").replace("_", " ").title()
        return self.title

    def prune_versions(self, links: list["DocLinkLike"]) -> list["DocLinkLike"]:
        """Keep one version tree when the docs ship several.

        llms.txt files frequently list every API version (`2024-11-05/...`,
        `2026-07-28/...`). Indexing all of them multiplies the corpus with
        near-duplicate text and splits retrieval scores across versions, so we
        keep the globally newest version plus every unversioned page.
        """
        if not self.prefer_latest_version:
            return links

        def version_of(url: str) -> str | None:
            for segment in urlparse(url).path.split("/"):
                if VERSION_SEGMENT_RE.fullmatch(segment):
                    return segment
            return None

        versions = {v for v in (version_of(link.url) for link in links) if v}
        if not versions:
            return links

        newest = max(versions, key=_version_key)
        kept: list[DocLinkLike] = []
        seen: set[str] = set()
        for link in links:
            version = version_of(link.url)
            if version is not None and version != newest:
                continue
            key = link.url.rstrip("/")
            if key in seen:
                continue
            seen.add(key)
            kept.append(link)
        return kept

    def __repr__(self) -> str:  # pragma: no cover - debug aid
        return f"<Source {self.name} llms_txt={self.llms_txt!r}>"


def _compile_rules(mapping: dict[str, str] | None) -> list[tuple[str, str]]:
    if not mapping:
        return []
    # Preserve YAML order; longer prefixes first so 'a/b/' beats 'a/'.
    items = sorted(mapping.items(), key=lambda kv: -len(kv[0]))
    return [(str(k), str(v)) for k, v in items]


def load_sources(path: Path | None = None, root_override: Path | None = None) -> list[Source]:
    """Parse sources.yaml into Source objects. Raises on malformed input."""
    path = path or paths.sources_yaml()
    if not path.exists():
        raise FileNotFoundError(f"source registry not found: {path}")

    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    defaults = raw.get("defaults") or {}
    rows = raw.get("sources") or []

    # Where each source's directories live: sources/<name>/{llms.txt,docs/,clean/}
    root_decl = raw.get("root") or "sources"
    root = Path(root_decl)
    if not root.is_absolute():
        base = root_override or path.resolve().parent
        root = (base / root).resolve()

    base_dir = defaults.get("doc_types") or {}
    base_exclude = list(defaults.get("exclude") or [])
    base_include = list(defaults.get("include") or [])

    sources: list[Source] = []
    seen: set[str] = set()
    for row in rows:
        name = str(row.get("name") or "").strip()
        if not name:
            raise ValueError("every source needs a name")
        if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", name):
            raise ValueError(
                f"source name '{name}' must be lowercase alphanumeric with . _ -"
            )
        if name in seen:
            raise ValueError(f"duplicate source name: {name}")
        seen.add(name)

        llms = str(row.get("llms_txt") or "").strip()
        if not llms:
            raise ValueError(f"source '{name}' is missing llms_txt")
        if not llms.startswith(("http://", "https://")):
            local = Path(llms).expanduser()
            relative_to_registry = path.resolve().parent / local
            legacy = root / local
            llms = str(legacy if not relative_to_registry.exists() and legacy.is_file() else relative_to_registry)

        doc_types = {**base_dir, **(row.get("doc_types") or {})}
        sources.append(
            Source(
                name=name,
                title=str(row.get("title") or name),
                llms_txt=llms,
                include=list(row.get("include") or base_include),
                exclude=list(row.get("exclude") or []) + base_exclude,
                doc_types=_compile_rules(doc_types),
                normalize=dict(row.get("normalize") or {}),
                prefer_latest_version=bool(row.get("prefer_latest_version", False)),
                doc_host=str(row.get("doc_host") or ""),
                root=root,
            )
        )
    return sources


def get_source(name: str) -> Source:
    for source in load_sources():
        if source.name == name:
            return source
    raise KeyError(f"unknown source '{name}'")


def iter_sources() -> Iterator[Source]:
    yield from load_sources()
