"""Tool handlers. Contract: (args, **kwargs) -> JSON string; never raise."""

from __future__ import annotations

import json
import logging

from . import store as store_mod

logger = logging.getLogger(__name__)

_STORE: store_mod.DocsStore | None = None


def configure(config: dict | None) -> None:
    """Called once from register() with the plugin's config namespace."""
    global _STORE
    settings = store_mod.Settings.resolve(config)
    _STORE = store_mod.DocsStore(settings)
    logger.info("hermes-docs-qdrant store: %s", settings.url or settings.path)


def _store_or_error() -> store_mod.DocsStore | None:
    if _STORE is None:
        configure({})
    if _STORE is None:  # pragma: no cover - configure always sets it
        return None
    return _STORE


def _error(message: str, **extra) -> str:
    return json.dumps({"ok": False, "error": message, **extra})


def docs_search(args: dict, **kwargs) -> str:
    try:
        query = (args or {}).get("query", "").strip()
        if not query:
            return _error("query is required")

        limit = min(int((args or {}).get("limit") or 0) or _STORE.settings.top_k, 20)
        store = _store_or_error()
        results = store.search(
            query,
            limit=limit,
            doc_type=(args or {}).get("doc_type") or None,
            section=(args or {}).get("section") or None,
        )
        return json.dumps(
            {
                "ok": True,
                "query": query,
                "count": len(results),
                "results": results,
            },
            ensure_ascii=False,
        )
    except Exception as exc:  # noqa: BLE001
        logger.exception("docs_search failed")
        return _error(f"{exc.__class__.__name__}: {exc}")


def docs_read(args: dict, **kwargs) -> str:
    try:
        doc_id = (args or {}).get("doc_id", "").strip().strip("/")
        if not doc_id:
            return _error("doc_id is required")
        max_chars = int((args or {}).get("max_chars") or 12000)

        store = _store_or_error()
        rows = store.get_doc_chunks(doc_id)
        if not rows:
            return _error(f"no document with doc_id '{doc_id}'", hint="call docs_outline")

        parts = []
        for row in rows:
            text = row["text"]
            if row.get("heading") and not text.lstrip().startswith("#"):
                text = f"## {row['heading']}\n\n{text}"
            parts.append(text)

        body = "\n\n".join(parts)
        truncated = len(body) > max_chars
        return json.dumps(
            {
                "ok": True,
                "doc_id": doc_id,
                "title": rows[0]["title"],
                "source_url": rows[0]["source_url"],
                "chunks": len(rows),
                "truncated": truncated,
                "content": body[:max_chars],
            },
            ensure_ascii=False,
        )
    except Exception as exc:  # noqa: BLE001
        logger.exception("docs_read failed")
        return _error(f"{exc.__class__.__name__}: {exc}")


def docs_outline(args: dict, **kwargs) -> str:
    try:
        doc_id = ((args or {}).get("doc_id") or "").strip().strip("/")
        store = _store_or_error()

        if doc_id:
            rows = store.get_doc_chunks(doc_id)
            if not rows:
                return _error(f"no document with doc_id '{doc_id}'")
            return json.dumps(
                {
                    "ok": True,
                    "doc_id": doc_id,
                    "title": rows[0]["title"],
                    "source_url": rows[0]["source_url"],
                    "headings": [r["heading"] for r in rows if r.get("heading")],
                },
                ensure_ascii=False,
            )

        ok, detail = store.health()
        return json.dumps(
            {
                "ok": True,
                "collection": store.settings.collection,
                "reachable": ok,
                "detail": detail,
                "sections": store.list_sections(),
            },
            ensure_ascii=False,
        )
    except Exception as exc:  # noqa: BLE001
        logger.exception("docs_outline failed")
        return _error(f"{exc.__class__.__name__}: {exc}")
