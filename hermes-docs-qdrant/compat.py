"""Runtime dependency contract for the docs plugin.

Why this module exists
----------------------
Hermes hides any tool whose ``check_fn`` returns False. That makes a broken
dependency environment indistinguishable from a plugin that never registered:
the tools simply are not there, with no error, no log line, and no way for the
agent to ask what happened.

Two failures produced exactly that:

* ``plugin.yaml`` declared ``qdrant-client>=1.9.0`` while ``store.py`` calls
  ``query_points`` / ``Prefetch`` / ``FusionQuery``, which first shipped in
  ``1.10.0``. A resolver could satisfy the manifest and still install a client
  the code cannot drive.
* A single flat dependency set meant a missing *optional* package (``yaml`` for
  the CLI, ``fastembed`` for sparse fusion) hid *all* tools, including
  ``docs_search`` which needs neither.

So: hard dependencies gate the tools; soft dependencies degrade a feature and
must never hide retrieval. ``check_environment`` is stdlib-only and safe to run
before any third-party import succeeds.
"""

from __future__ import annotations

import importlib
import os
import sys
from typing import Any

# These bounds are duplicated in plugin.yaml and requirements-runtime.txt.
# test_contract.py asserts the three agree, so edit them together.
MIN_QDRANT_CLIENT = "1.10.0"
MIN_OPENAI = "1.40.0"
MIN_FASTEMBED = "0.4.0"
MIN_PYYAML = "6.0"
MIN_HTTPX = "0.27.0"

# import name -> (minimum version, hard requirement, distribution name)
REQUIRED: dict[str, tuple[str, bool, str]] = {
    "qdrant_client": (MIN_QDRANT_CLIENT, True, "qdrant-client"),
    "openai": (MIN_OPENAI, True, "openai"),
    "fastembed": (MIN_FASTEMBED, False, "fastembed"),
    "yaml": (MIN_PYYAML, False, "PyYAML"),
    "httpx": (MIN_HTTPX, False, "httpx"),
}

# Capabilities the qdrant-client floor exists to guarantee. Checking the
# attribute is what actually catches a floor set too low; the version string
# alone does not.
QDRANT_APIS = ("Prefetch", "FusionQuery", "Fusion")


def parse_version(value: str) -> tuple[int, ...]:
    """Coerce '1.10.0rc1' / '1.10' / '1.10.0' to a comparable tuple."""
    parts: list[int] = []
    for chunk in str(value).split("."):
        digits = ""
        for char in chunk:
            if char.isdigit():
                digits += char
            else:
                break
        if not digits:
            break
        parts.append(int(digits))
    return tuple(parts)


def _version_tuple(value: str) -> tuple[int, ...]:
    return parse_version(value)


def satisfies(installed: str, minimum: str) -> bool:
    """True when installed >= minimum, comparing numeric segments only."""
    left = list(_version_tuple(installed))
    right = list(_version_tuple(minimum))
    width = max(len(left), len(right))
    left += [0] * (width - len(left))
    right += [0] * (width - len(right))
    return tuple(left) >= tuple(right)


def installed_version(dist_name: str, module: Any = None) -> str | None:
    """Distribution version, falling back to the module's own __version__."""
    try:
        from importlib.metadata import version as _dist_version

        return _dist_version(dist_name)
    except Exception:  # noqa: BLE001 - not installed as a distribution
        pass
    value = getattr(module, "__version__", None)
    return str(value) if value else None


def _check_qdrant_apis() -> list[str]:
    """Return the capabilities this qdrant-client build is missing."""
    try:
        from qdrant_client.http import models as qm
    except Exception:  # noqa: BLE001 - import failure is reported elsewhere
        return []
    return [name for name in QDRANT_APIS if not hasattr(qm, name)]


def check_environment() -> dict[str, Any]:
    """Report every runtime dependency and whether the tools can run.

    ``ok`` is False only when a *hard* dependency is missing, too old, or lacks
    a required capability. Soft failures are reported in ``warnings`` and never
    disable retrieval.
    """
    modules: dict[str, dict[str, Any]] = {}
    problems: list[str] = []
    warnings: list[str] = []

    for import_name, (minimum, hard, dist_name) in REQUIRED.items():
        entry: dict[str, Any] = {
            "import_name": import_name,
            "distribution": dist_name,
            "required": minimum,
            "hard": hard,
            "installed": None,
            "ok": False,
            "error": None,
        }
        try:
            module = importlib.import_module(import_name)
        except Exception as exc:  # noqa: BLE001 - report, never raise
            entry["error"] = f"{exc.__class__.__name__}: {exc}"
            message = f"{dist_name}>={minimum} is not importable ({entry['error']})"
            (problems if hard else warnings).append(message)
            modules[import_name] = entry
            continue

        found = installed_version(dist_name, module)
        entry["installed"] = found
        if found is None:
            # Importable but unversioned: accept it, the capability check below
            # is the real gate for qdrant.
            entry["ok"] = True
        elif satisfies(found, minimum):
            entry["ok"] = True
        else:
            entry["error"] = f"installed {found} < required {minimum}"
            message = f"{dist_name}={found} is older than the required {minimum}"
            (problems if hard else warnings).append(message)
        modules[import_name] = entry

    qdrant = modules.get("qdrant_client", {})
    if qdrant.get("ok"):
        missing = _check_qdrant_apis()
        if missing:
            qdrant["ok"] = False
            qdrant["missing_apis"] = missing
            problems.append(
                "qdrant-client is missing "
                + ", ".join(missing)
                + f"; store.py requires >= {MIN_QDRANT_CLIENT}"
            )

    # Query embedding needs a key; without it every search fails at call time
    # with a bare KeyError. It is not a *dependency* failure, so it warns
    # rather than disabling the tools, but it must be visible in diagnostics.
    embed_key = os.getenv("OPENROUTER_API_KEY")
    credentials = {
        "OPENROUTER_API_KEY": {
            "present": bool(embed_key),
            "purpose": f"embed queries with {os.getenv('HERMES_DOCS_EMBED_MODEL', 'qwen/qwen3-embedding-4b')}",
        }
    }
    if not embed_key:
        warnings.append(
            "OPENROUTER_API_KEY is not set: retrieval cannot embed queries "
            "(docs_search will report a missing key at call time)"
        )

    return {
        "ok": not problems,
        "python": sys.version.split()[0],
        "executable": sys.executable,
        "modules": modules,
        "credentials": credentials,
        "problems": problems,
        "warnings": warnings,
        "remediation": (
            None
            if not problems
            else "python -m pip install -r requirements-runtime.txt "
            "&& hermes gateway restart"
        ),
    }


def hard_failures(env: dict[str, Any] | None = None) -> list[str]:
    """The subset of problems that must hide the tools."""
    env = env or check_environment()
    return list(env.get("problems") or [])


def summary(env: dict[str, Any] | None = None) -> str:
    """One line suitable for a log record."""
    env = env or check_environment()
    if env["ok"]:
        degraded = f" ({len(env['warnings'])} warning(s))" if env["warnings"] else ""
        return f"dependencies ok on Python {env['python']}{degraded}"
    return "dependencies broken: " + "; ".join(env["problems"])
