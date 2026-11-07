"""Install or repair the hermes-docs-qdrant runtime in one command.

    python install.py                # verify + install runtime deps + report
    python install.py --check        # verify only, change nothing
    python install.py --with-build   # also install the corpus build toolchain
    python install.py --restart      # restart the Hermes gateway afterwards

Why this exists: `hermes plugins install` resolves plugin.yaml, but a running
Hermes process never switches dependency environments. The plugin registers its
tools and then hides every one of them because the *running* interpreter cannot
import qdrant_client. That failure is silent, which is how the tools went
missing in the first place. This script makes the state explicit and the repair
a single command.

The corpus build toolchain is deliberately separate: crawl4ai pins
snowballstemmer<3 and is unsatisfiable against Hermes core on Python >= 3.14.
Installing it into the Hermes environment breaks dependency resolution for
every plugin, so --with-build creates its own venv instead.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import venv
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
RUNTIME = REPO / "requirements-runtime.txt"
BUILD = REPO / "requirements-build.txt"
BUILD_VENV = REPO / ".venv-build"


def _run(cmd: list[str], label: str) -> int:
    print(f"\n$ {' '.join(cmd)}", flush=True)
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        print(f"  {label} failed (exit {proc.returncode})", file=sys.stderr, flush=True)
    return proc.returncode


def _hermes_binary() -> str | None:
    for name in ("hermes", "hermes.exe", "hermes.cmd"):
        for directory in os.getenv("PATH", "").split(os.pathsep):
            candidate = Path(directory) / name
            if candidate.exists():
                return str(candidate)
    return None


def verify() -> int:
    """Run the contract, availability and registration tests."""
    failures = 0
    for script in (
        "test_contract.py",
        "test_availability.py",
        "test_registration.py",
    ):
        if _run([sys.executable, str(HERE / script)], script) != 0:
            failures += 1
    return failures


def doctor() -> int:
    return _run([sys.executable, str(HERE / "cli.py"), "doctor"], "doctor")


def install_runtime() -> int:
    if not RUNTIME.exists():
        print(f"missing {RUNTIME}", file=sys.stderr)
        return 1
    return _run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--upgrade",
            "--upgrade-strategy",
            "only-if-needed",
            "-r",
            str(RUNTIME),
        ],
        "install",
    )


def install_build_toolchain() -> int:
    if not BUILD.exists():
        print(f"missing {BUILD}", file=sys.stderr)
        return 1
    if not BUILD_VENV.exists():
        print(f"\ncreating build venv at {BUILD_VENV}")
        venv.EnvBuilder(with_pip=True, clear=False).create(BUILD_VENV)
    python = BUILD_VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    return _run(
        [str(python), "-m", "pip", "install", "--upgrade", "-r", str(BUILD)],
        "build toolchain",
    )


def restart_gateway() -> int:
    hermes = _hermes_binary()
    if not hermes:
        print(
            "\nhermes binary not on PATH. Restart it yourself:\n"
            "  hermes gateway restart",
            file=sys.stderr,
        )
        return 1
    return _run([hermes, "gateway", "restart"], "gateway restart")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--check", action="store_true", help="verify only")
    parser.add_argument(
        "--with-build",
        action="store_true",
        help="also install the corpus toolchain into .venv-build",
    )
    parser.add_argument(
        "--restart",
        action="store_true",
        help="restart the Hermes gateway so the new environment is loaded",
    )
    parser.add_argument(
        "--skip-install",
        action="store_true",
        help="verify with the current environment, do not pip install",
    )
    args = parser.parse_args()

    print(f"plugin   : {HERE}")
    print(f"python   : {sys.executable}")
    print(f"runtime  : {RUNTIME}")
    print(f"build    : {BUILD}")

    if args.check:
        code = verify()
        doctor()
        return code

    if not args.skip_install:
        install_runtime()

    failures = verify()
    doctor_code = doctor()

    if args.with_build:
        install_build_toolchain()

    if args.restart:
        restart_gateway()

    if failures or doctor_code:
        print(
            "\nnot healthy. Read the FAIL lines above; the doctor section names\n"
            "the exact package and the remediation command.",
            file=sys.stderr,
        )
        return 1

    print(
        "\ninstall: healthy\n"
        "\nNext steps in Hermes (a running process never switches envs):\n"
        "  hermes plugins install .\n"
        "  hermes plugins enable hermes-docs-qdrant\n"
        "  hermes gateway restart\n"
        "  # then, once, to build the corpus:\n"
        "  python cli.py fetch --recreate   (use .venv-build python when scraping)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
