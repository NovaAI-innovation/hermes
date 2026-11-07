"""hermes-docs-qdrant - Qdrant retrieval over the Hermes documentation corpus."""

from __future__ import annotations

import logging

from . import schemas, tools

logger = logging.getLogger(__name__)

__version__ = "1.1.0"


def _load_config(ctx) -> dict:
    """Read this plugin's config namespace, tolerating older host signatures."""
    for attempt in (
        lambda: ctx.get_config(),
        lambda: ctx.get_config("hermes-docs-qdrant"),
        lambda: {},
    ):
        try:
            value = attempt()
            if isinstance(value, dict):
                return value
        except Exception:  # noqa: BLE001 - host API differences are expected
            continue
    return {}


def _available() -> bool:
    """check_fn: hide tools when the corpus is unreachable."""
    try:
        store = tools._store_or_error()
        if store is None:
            return False
        ok, _ = store.health()
        return ok
    except Exception:  # noqa: BLE001
        return False


def register(ctx):
    tools.configure(_load_config(ctx))

    ctx.register_tool(
        name="docs_search",
        toolset="hermes_docs",
        schema=schemas.SEARCH,
        handler=tools.docs_search,
        check_fn=_available,
    )
    ctx.register_tool(
        name="docs_read",
        toolset="hermes_docs",
        schema=schemas.READ,
        handler=tools.docs_read,
        check_fn=_available,
    )
    ctx.register_tool(
        name="docs_outline",
        toolset="hermes_docs",
        schema=schemas.OUTLINE,
        handler=tools.docs_outline,
        check_fn=_available,
    )
    ctx.register_tool(
        name="docs_search_many",
        toolset="hermes_docs",
        schema=schemas.SEARCH_MANY,
        handler=tools.docs_search_many,
        check_fn=_available,
    )
    ctx.register_tool(
        name="docs_list",
        toolset="hermes_docs",
        schema=schemas.LIST_DOCS,
        handler=tools.docs_list,
        check_fn=_available,
    )
    ctx.register_tool(
        name="docs_stats",
        toolset="hermes_docs",
        schema=schemas.STATS,
        handler=tools.docs_stats,
        check_fn=_available,
    )
    ctx.register_tool(
        name="docs_rebuild",
        toolset="hermes_docs",
        schema=schemas.REBUILD,
        handler=tools.docs_rebuild,
        # Rebuild must stay callable even when the collection is empty or
        # unreachable -- that is precisely when it is needed.
        check_fn=None,
    )

    logger.info("hermes-docs-qdrant registered 7 tools")


__all__ = ["register", "schemas", "tools", "__version__"]
