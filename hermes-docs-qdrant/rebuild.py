"""Corpus rebuild driven from inside the plugin (used by the rebuild tool).

Runs the vendored pipeline stages as subprocesses so a long rebuild never
blocks the agent's own import path and a failed stage cannot corrupt the
running process. The scrape stage is optional per-request and may be skipped
when only local content changed.

Contract: `rebuild()` returns a JSON-serialisable dict and never raises.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent
PIPELINE_DIR = PLUGIN_DIR / "pipeline"


def _run_stage(script: Path, args: list[str] | None = None, timeout: int = 3600) -> dict:
    started = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, str(script), *(args or [])],
            cwd=str(script.parent),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return {
            "stage": script.stem,
            "ok": False,
            "error": f"timed out after {timeout}s",
            "seconds": round(time.time() - started, 1),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "stage": script.stem,
            "ok": False,
            "error": f"{exc.__class__.__name__}: {exc}",
            "seconds": round(time.time() - started, 1),
        }

    tail = (proc.stdout or "").strip().splitlines()[-8:]
    return {
        "stage": script.stem,
        "ok": proc.returncode == 0,
        "returncode": proc.returncode,
        "seconds": round(time.time() - started, 1),
        "tail": tail,
        "stderr": (proc.stderr or "").strip().splitlines()[-5:],
    }


def rebuild(
    scrape: bool = False,
    sources: list[str] | None = None,
    reindex: bool = True,
    refresh: bool = False,
) -> dict:
    """Scrape (optional) -> normalize -> enrich -> chunk -> index.

    Args:
        scrape:  also re-download every configured llms.txt source.
        sources: restrict scraping to these source names.
        reindex: rebuild the Qdrant collection after chunking.
        refresh: force re-download of pages that already exist.
    """
    started = time.time()
    stages: list[dict] = []

    if scrape:
        args: list[str] = []
        for name in sources or []:
            args += ["--source", name]
        if refresh:
            args.append("--refresh")
        result = _run_stage(PIPELINE_DIR / "scrape.py", args, timeout=7200)
        stages.append(result)
        if not result["ok"]:
            return _summary(stages, started, failed=result["stage"])

    for stage_name in ("normalize", "enrich", "chunk"):
        result = _run_stage(PIPELINE_DIR / f"{stage_name}.py")
        stages.append(result)
        if not result["ok"]:
            return _summary(stages, started, failed=stage_name)

    if reindex:
        result = _run_stage(PLUGIN_DIR / "ingest.py", ["--recreate"], timeout=7200)
        stages.append(result)
        if not result["ok"]:
            return _summary(stages, started, failed="index")

    return _summary(stages, started, failed=None)


def _summary(stages: list[dict], started: float, failed: str | None) -> dict:
    return {
        "ok": failed is None,
        "failed_stage": failed,
        "seconds": round(time.time() - started, 1),
        "stages": stages,
    }


if __name__ == "__main__":  # manual smoke test
    print(json.dumps(rebuild(scrape=False, reindex=False), indent=2))
