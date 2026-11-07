"""hermes-docs-qdrant - Qdrant retrieval over the Hermes documentation corpus."""

from __future__ import annotations

import logging

from . import schemas, tools

logger = logging.getLogger(__name__)

__version__ = "2.2.0"

# Cached so a broken environment is reported once per process, not once per
# tool availability check (Hermes calls check_fn frequently).
_ENV: dict | None = None


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


def environment() -> dict:
    """Memoised dependency report; see compat.check_environment."""
    global _ENV
    if _ENV is None:
        from . import compat

        _ENV = compat.check_environment()
        if _ENV["ok"]:
            logger.info("hermes-docs-qdrant: %s", compat.summary(_ENV))
            for warning in _ENV["warnings"]:
                logger.warning("hermes-docs-qdrant degraded: %s", warning)
        else:
            # Loud on purpose: a silent False here is what made these tools
            # vanish with no explanation.
            logger.error(
                "hermes-docs-qdrant tools disabled: %s | fix: %s",
                "; ".join(_ENV["problems"]),
                _ENV["remediation"],
            )
    return _ENV


def reset_environment() -> None:
    """Drop the cache after a dependency install or rebuild."""
    global _ENV
    _ENV = None


def _dependencies_ok() -> bool:
    try:
        return bool(environment()["ok"])
    except Exception:  # noqa: BLE001 - never break host startup
        return False


def _available() -> bool:
    """check_fn: gate on HARD dependencies, then on collection health.

    A hard dependency failure (qdrant-client, openai absent or too old) hides
    the tools — they cannot work. A soft failure (fastembed, pyyaml) does not:
    it is reported by docs_diagnostics and degrades a feature, not retrieval.
    """
    if not _dependencies_ok():
        return False
    try:
        store = tools._store_or_error()
        if store is None:
            return False
        ok, detail = store.health()
        if not ok:
            logger.warning("hermes-docs-qdrant collection unreachable: %s", detail)
        return ok
    except Exception as exc:  # noqa: BLE001
        logger.warning("hermes-docs-qdrant availability check failed: %s", exc)
        return False


def register(ctx):
    tools.configure(_load_config(ctx))
    environment()

    ctx.register_tool(
        name="docs_search",
        toolset="hermes_docs",
        schema=schemas.SEARCH,
        handler=tools.docs_search,
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
    # Diagnostics must stay callable in exactly the state that needs them:
    # dependencies broken, collection empty, or store unreachable.
    ctx.register_tool(
        name="docs_diagnostics",
        toolset="hermes_docs",
        schema=schemas.DIAGNOSTICS,
        handler=tools.docs_diagnostics,
        check_fn=None,
    )
    ctx.register_tool(
        name="docs_rebuild",
        toolset="hermes_docs",
        schema=schemas.REBUILD,
        handler=tools.docs_rebuild,
        check_fn=None,
    )

    logger.info("hermes-docs-qdrant registered 8 tools")


__all__ = ["register", "schemas", "tools", "environment", "__version__"]
