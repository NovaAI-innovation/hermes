"""Behavioural test: a hard dependency failure disables the tools loudly, a
soft dependency failure does not.

This is the regression test for the defect that made the plugin's tools vanish
from a session with no error: every tool carried a check_fn that returned False
for a missing optional package, and nothing was logged.

Run: python test_availability.py
"""

from __future__ import annotations

import builtins
import importlib
import importlib.util
import os
import sys
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO))

import compat  # noqa: E402


class _Block:
    """Refuse to import the named modules for the duration of the context."""

    def __init__(self, *names: str):
        self.names = set(names)
        self._real = builtins.__import__

    def __enter__(self):
        real = self._real
        blocked = self.names

        def guard(name, globals=None, locals=None, fromlist=(), level=0):
            root = name.split(".")[0]
            if root in blocked:
                raise ModuleNotFoundError(f"No module named '{root}'")
            return real(name, globals, locals, fromlist, level)

        builtins.__import__ = guard
        for module in list(sys.modules):
            if module.split(".")[0] in blocked:
                sys.modules.pop(module, None)
        compat.importlib.invalidate_caches()
        return self

    def __exit__(self, *exc):
        builtins.__import__ = self._real
        compat.importlib.invalidate_caches()
        return False


def test_hard_missing_hides_and_reports() -> None:
    with _Block("qdrant_client"):
        env = compat.check_environment()
    assert env["ok"] is False, "a missing hard dependency must disable the tools"
    assert any("qdrant-client" in p for p in env["problems"]), env["problems"]
    assert env["remediation"], "a broken environment must say how to fix itself"
    assert env["modules"]["qdrant_client"]["hard"] is True
    assert env["modules"]["qdrant_client"]["error"], "the import error must be kept"
    print("  hard failure -> tools disabled, problem + remediation reported")


def test_soft_missing_keeps_tools() -> None:
    with _Block("fastembed", "yaml"):
        env = compat.check_environment()
    assert env["ok"] is True, (
        "a missing optional package must not hide retrieval; "
        f"problems={env['problems']}"
    )
    assert env["warnings"], "a soft failure must be reported as a warning"
    assert env["modules"]["fastembed"]["hard"] is False
    print("  soft failure -> tools stay available, warned not hidden")


def test_too_old_version_is_a_hard_failure() -> None:
    assert not compat.satisfies("1.9.0", "1.10.0")
    assert compat.satisfies("1.10.0", "1.10.0")
    assert compat.satisfies("1.18.0", "1.10.0")
    assert compat.satisfies("2.0.0", "1.10.0")
    print("  version comparison rejects 1.9.0 against the 1.10.0 floor")


def test_qdrant_apis_present_in_installed_client() -> None:
    try:
        from qdrant_client.http import models as qm
    except ImportError:
        print("  qdrant-client not installed here; capability check skipped")
        return
    missing = [name for name in compat.QDRANT_APIS if not hasattr(qm, name)]
    assert not missing, f"installed qdrant-client is missing {missing}"
    print(f"  installed qdrant-client provides {', '.join(compat.QDRANT_APIS)}")


def _import_plugin() -> types.ModuleType:
    """Import the plugin as a package regardless of its hyphenated directory.

    The directory is ``hermes-docs-qdrant``, which is not a valid module name,
    so the parent is put on sys.path and the directory is loaded under the
    underscore alias. Hermes does the same thing at install time
    (``hermes_plugins.hermes_docs_qdrant``).
    """
    import types as _types  # noqa: F401 - keeps the alias import explicit

    if "hermes_docs_qdrant" in sys.modules:
        return sys.modules["hermes_docs_qdrant"]
    spec = importlib.util.spec_from_file_location(
        "hermes_docs_qdrant",
        HERE / "__init__.py",
        submodule_search_locations=[str(HERE)],
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["hermes_docs_qdrant"] = module
    spec.loader.exec_module(module)
    return module


def test_diagnostics_callable_when_broken() -> None:
    """docs_diagnostics must answer in the state that hides every other tool."""
    with _Block("qdrant_client"):
        package = _import_plugin()
        importlib.reload(compat)
        package.compat = compat
        payload = package.tools.docs_diagnostics({})
    assert '"ok": true' in payload.lower(), payload[:300]
    assert "qdrant-client" in payload, "diagnostics must name the missing package"
    assert "false" in payload.lower(), "diagnostics must report the disabled state"
    print("  docs_diagnostics answers and names the missing package while broken")


def test_missing_key_is_named_not_keyerror() -> None:
    """A missing embedding key must be an actionable message, not a bare KeyError."""
    try:
        package = _import_plugin()
    except Exception as exc:  # noqa: BLE001
        print(f"  plugin import unavailable here ({exc.__class__.__name__}); skipped")
        return
    embedder = package.store.QueryEmbedder()
    saved = os.environ.pop("OPENROUTER_API_KEY", None)
    try:
        embedder._get_client()
    except RuntimeError as exc:
        assert "OPENROUTER_API_KEY" in str(exc)
        assert "docs_diagnostics" in str(exc), "the message must name the next step"
        print("  missing key -> named RuntimeError with a remediation hint")
        return
    except KeyError:
        raise AssertionError("a missing key still surfaces as a bare KeyError")
    finally:
        if saved is not None:
            os.environ["OPENROUTER_API_KEY"] = saved
    raise AssertionError("QueryEmbedder built a client with no API key")


def main() -> int:
    tests = [
        test_hard_missing_hides_and_reports,
        test_soft_missing_keeps_tools,
        test_too_old_version_is_a_hard_failure,
        test_qdrant_apis_present_in_installed_client,
        test_diagnostics_callable_when_broken,
        test_missing_key_is_named_not_keyerror,
    ]
    failures = 0
    for test in tests:
        print(f"- {test.__name__}")
        try:
            test()
        except AssertionError as exc:
            failures += 1
            print(f"    FAILED: {exc}")
    if failures:
        print(f"\nAVAILABILITY TEST FAILED ({failures})")
        return 1
    print("\nAVAILABILITY TEST PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
