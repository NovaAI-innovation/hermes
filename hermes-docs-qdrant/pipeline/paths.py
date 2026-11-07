"""Resolve the plugin's on-disk home for sources, corpus and the Qdrant store.

Everything the pipeline writes must live outside the plugin install tree:
`hermes plugins update` git-pulls it and `hermes plugins remove` deletes it, so
data written under `__file__` is destroyed on upgrade. Hermes sanctions
`<HERMES_HOME>/plugin-data/<name>/` for exactly this, via
`plugins.plugin_storage.plugin_data_dir`.

Resolution order:
  1. HERMES_DOCS_HOME        explicit override (what CI and tests set)
  2. <HERMES_HOME>/plugin-data/hermes-docs-qdrant   when running inside Hermes
  3. <plugin>/.data          standalone checkout, no Hermes installed

Layout under the resolved home:

    <home>/sources.yaml
    <home>/sources/<name>/{llms.txt,docs/,clean/}
    <home>/corpus/{documents,chunks,parents}.jsonl
    <home>/.env                (optional, standalone only)
    <home>/qdrant/             embedded Qdrant store
"""

from __future__ import annotations

import os
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent.parent
PLUGIN_NAME = "hermes-docs-qdrant"


def _hermes_plugin_data_dir() -> Path | None:
    """Ask Hermes for the sanctioned per-plugin data dir, if we are inside one."""
    try:
        from plugins.plugin_storage import plugin_data_dir  # type: ignore
    except Exception:  # noqa: BLE001 - not running inside Hermes
        return None
    try:
        return Path(plugin_data_dir(PLUGIN_NAME))
    except Exception:  # noqa: BLE001
        return None


def home() -> Path:
    """Root directory for all generated data. Created on first use."""
    override = os.getenv("HERMES_DOCS_HOME") or os.getenv("HERMES_DOCS_DATA")
    if override:
        return Path(override).expanduser().resolve()

    managed = _hermes_plugin_data_dir()
    if managed is not None:
        return managed

    return PLUGIN_DIR / ".data"


def ensure_home() -> Path:
    root = home()
    root.mkdir(parents=True, exist_ok=True)
    return root


def sources_yaml() -> Path:
    """User-editable registry; seeded from the packaged default on first use."""
    root = ensure_home()
    user = root / "sources.yaml"
    if not user.exists():
        bundled = PLUGIN_DIR / "default_sources.yaml"
        if bundled.exists():
            user.write_text(bundled.read_text(encoding="utf-8"), encoding="utf-8")
    return user


def sources_root() -> Path:
    return ensure_home() / "sources"


def corpus_dir() -> Path:
    return ensure_home() / "corpus"


def qdrant_dir() -> Path:
    return ensure_home() / "qdrant"


def env_file() -> Path:
    return ensure_home() / ".env"


def describe() -> dict[str, str]:
    root = home()
    return {
        "home": str(root),
        "sources_yaml": str(root / "sources.yaml"),
        "sources": str(root / "sources"),
        "corpus": str(root / "corpus"),
        "qdrant": str(root / "qdrant"),
    }
