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


def _ok(**payload) -> str:
    return json.dumps({"ok": True, **payload}, ensure_ascii=False)


def _int_arg(args: dict, key: str, default: int, maximum: int) -> int:
    value = (args or {}).get(key)
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return default
    return max(1, min(parsed, maximum))


# ------------------------------------------------------------------ retrieval


def docs_search(args: dict, **kwargs) -> str:
    try:
        query = ((args or {}).get("query") or "").strip()
        if not query:
            return _error("query is required")

        store = _store_or_error()
        limit = _int_arg(args, "limit", store.settings.top_k, 20)
        results = store.search(
            query,
            limit=limit,
            doc_type=(args or {}).get("doc_type") or None,
            section=(args or {}).get("section") or None,
            source=(args or {}).get("source") or None,
        )
        used = {
            k: v
            for k, v in {
                "source": (args or {}).get("source"),
                "doc_type": (args or {}).get("doc_type"),
                "section": (args or {}).get("section"),
            }.items()
            if v
        }
        payload = {"query": query, "count": len(results), "results": results}
        if used:
            payload["filters"] = used
        if not results:
            payload["hint"] = "no matches; try docs_outline to see sources and doc types"
        return _ok(**payload)
    except Exception as exc:  # noqa: BLE001
        logger.exception("docs_search failed")
        return _error(f"{exc.__class__.__name__}: {exc}")


def docs_search_many(args: dict, **kwargs) -> str:
    try:
        raw = (args or {}).get("queries") or []
        if isinstance(raw, str):
            raw = [raw]
        queries = [q.strip() for q in raw if isinstance(q, str) and q.strip()]
        if not queries:
            return _error("queries must contain at least one non-empty string")
        if len(queries) > 10:
            return _error("at most 10 queries per call")

        store = _store_or_error()
        limit = _int_arg(args, "limit", 4, 10)
        grouped = store.search_many(
            queries,
            limit=limit,
            doc_type=(args or {}).get("doc_type") or None,
            source=(args or {}).get("source") or None,
        )
        return _ok(
            queries=list(grouped),
            limit=limit,
            results=grouped,
            counts={q: len(v) for q, v in grouped.items()},
        )
    except Exception as exc:  # noqa: BLE001
        logger.exception("docs_search_many failed")
        return _error(f"{exc.__class__.__name__}: {exc}")


def docs_read(args: dict, **kwargs) -> str:
    try:
        doc_id = ((args or {}).get("doc_id") or "").strip().strip("/")
        if not doc_id:
            return _error("doc_id is required")
        max_chars = _int_arg(args, "max_chars", 12000, 60000)

        store = _store_or_error()
        rows = store.get_doc_chunks(doc_id, limit=400)
        if not rows:
            hint = "call docs_outline or docs_list to find a valid doc_id"
            if ":" not in doc_id:
                hint = (
                    "doc_id is source-qualified, e.g. 'hermes:user-guide/cli'. "
                    "Call docs_list to find the right id."
                )
            return _error(f"no document with doc_id '{doc_id}'", hint=hint)

        parts = []
        for row in rows:
            text = row["text"]
            if row.get("heading") and not text.lstrip().startswith("#"):
                text = f"## {row['heading']}\n\n{text}"
            parts.append(text)

        body = "\n\n".join(parts)
        truncated = len(body) > max_chars
        return _ok(
            doc_id=doc_id,
            title=rows[0]["title"],
            source=rows[0].get("source", ""),
            source_url=rows[0]["source_url"],
            chunks=len(rows),
            truncated=truncated,
            content=body[:max_chars],
        )
    except Exception as exc:  # noqa: BLE001
        logger.exception("docs_read failed")
        return _error(f"{exc.__class__.__name__}: {exc}")


# --------------------------------------------------------------- discovery


def docs_outline(args: dict, **kwargs) -> str:
    try:
        doc_id = ((args or {}).get("doc_id") or "").strip().strip("/")
        store = _store_or_error()

        if doc_id:
            rows = store.get_doc_chunks(doc_id, limit=400)
            if not rows:
                return _error(f"no document with doc_id '{doc_id}'")
            return _ok(
                doc_id=doc_id,
                title=rows[0]["title"],
                source=rows[0].get("source", ""),
                source_url=rows[0]["source_url"],
                headings=[r["heading"] for r in rows if r.get("heading")],
            )

        stats = store.corpus_stats()
        stats["sections"] = store.list_sections()
        return _ok(**stats)
    except Exception as exc:  # noqa: BLE001
        logger.exception("docs_outline failed")
        return _error(f"{exc.__class__.__name__}: {exc}")


def docs_list(args: dict, **kwargs) -> str:
    try:
        store = _store_or_error()
        limit = _int_arg(args, "limit", 100, 500)
        docs = store.list_documents(
            source=(args or {}).get("source") or None,
            doc_type=(args or {}).get("doc_type") or None,
            prefix=(args or {}).get("prefix") or None,
            limit=limit,
        )
        return _ok(count=len(docs), documents=docs, truncated=len(docs) >= limit)
    except Exception as exc:  # noqa: BLE001
        logger.exception("docs_list failed")
        return _error(f"{exc.__class__.__name__}: {exc}")


def docs_stats(args: dict, **kwargs) -> str:
    try:
        store = _store_or_error()
        stats = store.corpus_stats()
        manifest = store.collection_manifest()
        if manifest:
            stats["manifest"] = manifest
        return _ok(**stats)
    except Exception as exc:  # noqa: BLE001
        logger.exception("docs_stats failed")
        return _error(f"{exc.__class__.__name__}: {exc}")


# ------------------------------------------------------------------ rebuild


def docs_rebuild(args: dict, **kwargs) -> str:
    try:
        from . import rebuild as rebuild_mod

        sources = (args or {}).get("sources") or None
        if isinstance(sources, str):
            sources = [sources]
        clean_sources = [s for s in (sources or []) if isinstance(s, str)] or None
        result = rebuild_mod.rebuild(
            scrape=bool((args or {}).get("scrape", False)),
            sources=clean_sources,
            reindex=bool((args or {}).get("reindex", True)),
            refresh=bool((args or {}).get("refresh", False)),
        )
        # A successful index rebuild invalidates any cached store handle.
        if result.get("ok"):
            configure(None)
        return _ok(**result)
    except Exception as exc:  # noqa: BLE001
        logger.exception("docs_rebuild failed")
        return _error(f"{exc.__class__.__name__}: {exc}")
