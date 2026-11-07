"""Contract test: the declared dependency bounds match what the code requires.

Fails when the three places that state a dependency floor drift apart:
plugin.yaml (what Hermes resolves), requirements-runtime.txt (what a repair
installs), and compat.py (what the tools report). It also asserts the
qdrant-client floor actually covers the APIs store.py calls — the defect that
made the tools silently unavailable.

Run: python test_contract.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))

import compat  # noqa: E402

RUNTIME_FILE = REPO / "requirements-runtime.txt"
BUILD_FILE = REPO / "requirements-build.txt"
CONSTRAINTS_FILE = HERE / "constraints.txt"


def _parse_requirements(path: Path) -> dict[str, str]:
    """Map distribution name (lowercased) -> full specifier, ignoring comments."""
    found: dict[str, str] = {}
    if not path.exists():
        return found
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or line.startswith("-"):
            continue
        match = re.match(r"^([A-Za-z0-9_.\-]+)\s*(\[[^\]]+\])?\s*(.*)$", line)
        if not match:
            continue
        found[match.group(1).lower().replace("_", "-")] = match.group(3).strip()
    return found


def _floor_from_specifier(specifier: str) -> str | None:
    match = re.search(r">=\s*([0-9][0-9A-Za-z.\-]*)", specifier or "")
    return match.group(1) if match else None


def check_versions_agree() -> list[str]:
    problems: list[str] = []
    runtime = _parse_requirements(RUNTIME_FILE)

    # compat.py is the source of truth for what the code checks at runtime.
    expected = {
        "qdrant-client": compat.MIN_QDRANT_CLIENT,
        "fastembed": compat.MIN_FASTEMBED,
        "openai": compat.MIN_OPENAI,
        "pyyaml": compat.MIN_PYYAML,
        "httpx": compat.MIN_HTTPX,
    }
    for dist, floor in expected.items():
        if dist not in runtime:
            problems.append(f"{RUNTIME_FILE.name} is missing {dist}")
            continue
        declared = _floor_from_specifier(runtime[dist])
        if declared != floor:
            problems.append(
                f"{dist}: compat.py says >= {floor}, "
                f"{RUNTIME_FILE.name} says >= {declared}"
            )

    plugin_yaml = (HERE / "plugin.yaml").read_text(encoding="utf-8")
    for dist, floor in expected.items():
        pattern = item = re.escape(dist) + r">=\s*([0-9][0-9A-Za-z.\-]*)"
        match = re.search(pattern, plugin_yaml, re.IGNORECASE)
        if not match:
            problems.append(f"plugin.yaml is missing {dist}")
        elif match.group(1) != floor:
            problems.append(
                f"{dist}: compat.py says >= {floor}, "
                f"plugin.yaml says >= {match.group(1)}"
            )
    return problems


def check_qdrant_floor_covers_apis() -> list[str]:
    """The floor must be >= the release that introduced every API store.py uses."""
    problems: list[str] = []
    store = (HERE / "store.py").read_text(encoding="utf-8")
    uses = {
        "query_points": "1.10.0",
        "Prefetch": "1.10.0",
        "FusionQuery": "1.10.0",
    }
    for symbol, introduced in uses.items():
        if symbol in store and not compat.satisfies(
            compat.MIN_QDRANT_CLIENT, introduced
        ):
            problems.append(
                f"store.py uses {symbol} (needs qdrant-client >= {introduced}) "
                f"but the declared floor is {compat.MIN_QDRANT_CLIENT}"
            )
    return problems


def check_build_toolchain_isolated() -> list[str]:
    """crawl4ai must never appear in the runtime set — it breaks resolution."""
    problems: list[str] = []
    runtime_text = RUNTIME_FILE.read_text(encoding="utf-8").lower()
    for line in runtime_text.splitlines():
        stripped = line.split("#", 1)[0].strip()
        if stripped.startswith("crawl4ai"):
            problems.append(
                "crawl4ai is declared in requirements-runtime.txt; it pins "
                "snowballstemmer<3 and breaks resolution against Hermes core"
            )
    if BUILD_FILE.exists():
        build = _parse_requirements(BUILD_FILE)
        if "crawl4ai" not in build:
            problems.append("requirements-build.txt should declare crawl4ai")
    return problems


def check_constraints_match() -> list[str]:
    """constraints.txt must agree with plugin.yaml, not silently contradict it."""
    problems: list[str] = []
    constraints = _parse_requirements(CONSTRAINTS_FILE)
    if "qdrant-client" not in constraints:
        problems.append(f"{CONSTRAINTS_FILE.name} must pin qdrant-client")
        return problems
    floor = _floor_from_specifier(constraints["qdrant-client"])
    if floor != compat.MIN_QDRANT_CLIENT:
        problems.append(
            f"constraints.txt says qdrant-client >= {floor}, "
            f"compat.py says >= {compat.MIN_QDRANT_CLIENT}"
        )
    return problems


def check_environment_shape() -> list[str]:
    """check_environment must always return a usable report, even when broken."""
    problems: list[str] = []
    env = compat.check_environment()
    for key in ("ok", "python", "executable", "modules", "problems", "warnings"):
        if key not in env:
            problems.append(f"check_environment() is missing '{key}'")
    if not env.get("ok") and not env.get("problems"):
        problems.append("check_environment() reported failure with no problems")
    if not env.get("ok") and not env.get("remediation"):
        problems.append("a broken environment must carry a remediation command")
    return problems


def check_registration_contract() -> list[str]:
    """Diagnostics and rebuild must not be gated; retrieval must be."""
    problems: list[str] = []
    init = (HERE / "__init__.py").read_text(encoding="utf-8")
    for name in ("docs_diagnostics", "docs_rebuild"):
        block = init.split(f'name="{name}"', 1)
        if len(block) < 2:
            problems.append(f"{name} is not registered in __init__.py")
            continue
        tail = block[1][:400]
        if "check_fn=None" not in tail:
            problems.append(
                f"{name} must register with check_fn=None so it stays callable "
                "in exactly the state that needs it"
            )
    return problems


def main() -> int:
    checks = {
        "versions agree": check_versions_agree,
        "qdrant floor covers APIs": check_qdrant_floor_covers_apis,
        "build toolchain isolated": check_build_toolchain_isolated,
        "constraints agree": check_constraints_match,
        "environment report shape": check_environment_shape,
        "registration contract": check_registration_contract,
    }
    failures: list[str] = []
    for label, check in checks.items():
        problems = check()
        status = "ok" if not problems else "FAIL"
        print(f"[{status:4}] {label}")
        for problem in problems:
            print(f"       - {problem}")
        failures.extend(problems)

    env = compat.check_environment()
    print(f"\nruntime: {compat.summary(env)}")
    for module, info in env["modules"].items():
        state = "ok" if info["ok"] else "MISSING"
        print(
            f"  {module:14} {state:8} installed={info['installed']} "
            f"required>={info['required']} hard={info['hard']}"
        )

    if failures:
        print(f"\nCONTRACT TEST FAILED ({len(failures)} problem(s))")
        return 1
    print("\nCONTRACT TEST PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
