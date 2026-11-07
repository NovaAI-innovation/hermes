"""Build a configured documentation corpus and publish it to the active store."""

from __future__ import annotations

import json
import logging
import os
import subprocess
import sys
import time
from pathlib import Path
from tempfile import TemporaryDirectory

if __package__:
    from .pipeline import paths
    from .store import DocsStore, Settings, ingest
else:
    from pipeline import paths
    from store import DocsStore, Settings, ingest

logger = logging.getLogger(__name__)
PIPELINE_DIR = Path(__file__).resolve().parent / "pipeline"


def _run_stage(stage: str, python: str, env: dict, args: list[str], timeout: int) -> dict:
    started = time.monotonic()
    logger.info("Documentation rebuild stage: %s", stage)
    try:
        proc = subprocess.run(
            [python, str(PIPELINE_DIR / f"{stage}.py"), *args],
            cwd=PIPELINE_DIR, env=env, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return {"stage": stage, "ok": False, "error": f"Timed out after {timeout}s"}
    return {
        "stage": stage,
        "ok": proc.returncode == 0,
        "returncode": proc.returncode,
        "seconds": round(time.monotonic() - started, 1),
        "tail": proc.stdout.splitlines()[-8:],
        "stderr": proc.stderr.splitlines()[-6:],
    }


def rebuild(
    scrape: bool = True,
    sources: list[str] | None = None,
    reindex: bool = True,
    refresh: bool = False,
    *,
    store: DocsStore | None = None,
) -> dict:
    """Refresh selected sources, then build and optionally publish the combined corpus."""
    started = time.monotonic()
    stages = []
    stage = "prepare"
    owns_store = store is None
    try:
        import portalocker
    except ImportError as exc:
        return _failure(stage, f"Qdrant's file-lock dependency is unavailable: {exc}", stages, started)

    try:
        if __package__:
            from .pipeline.sources import load_sources
        else:
            from pipeline.sources import load_sources

        store = store or DocsStore(Settings.resolve())
        data_home = paths.ensure_home().resolve()
        corpus = Path(store.settings.corpus_dir or paths.corpus_dir()).expanduser().resolve()
        build_python = store.settings.extras.get("build_python") or os.getenv("HERMES_DOCS_BUILD_PYTHON")
        if build_python:
            executable = Path(build_python).expanduser().resolve()
            if not executable.is_file():
                raise ValueError(f"Build interpreter does not exist: {executable}")
            build_python = str(executable)
        else:
            build_python = sys.executable

        if not scrape and (sources is not None or refresh):
            raise ValueError("sources and refresh require scrape=true")
        with portalocker.Lock(data_home / ".rebuild.lock", mode="a", timeout=0, fail_when_locked=True):
            registry = paths.sources_yaml()
            snapshot = registry.read_bytes()
            configured = [source.name for source in load_sources(registry)]
            if not configured:
                raise ValueError("No documentation sources are configured in sources.yaml")
            requested = list(dict.fromkeys(sources)) if sources is not None else configured
            if not requested:
                raise ValueError("sources must contain at least one configured source name")
            unknown = set(requested) - set(configured)
            if unknown:
                raise ValueError(f"Unknown sources: {', '.join(sorted(unknown))}. Configured: {', '.join(configured)}")
            if reindex and not os.getenv("OPENROUTER_API_KEY"):
                raise ValueError("OPENROUTER_API_KEY is required to index the corpus. Set it in the Hermes environment.")

            corpus.mkdir(parents=True, exist_ok=True)
            with TemporaryDirectory(prefix=".rebuild-", dir=corpus) as temp:
                staging = Path(temp)
                env = {
                    **os.environ,
                    "HERMES_DOCS_HOME": str(data_home),
                    "HERMES_DOCS_CORPUS": str(staging),
                    "PYTHONIOENCODING": "utf-8",
                }
                stages_to_run = []
                if scrape:
                    args = [arg for name in requested for arg in ("--source", name)]
                    if refresh:
                        args.append("--refresh")
                    stages_to_run.append(("scrape", args, 7200))
                stages_to_run.extend((name, [], 3600) for name in ("normalize", "enrich", "chunk"))
                for stage, args, timeout in stages_to_run:
                    result = _run_stage(stage, build_python, env, args, timeout)
                    stages.append(result)
                    if not result["ok"]:
                        detail = result.get("error") or "See the failed stage output."
                        if stage in {"scrape", "chunk"}:
                            detail += " For missing build packages, set HERMES_DOCS_BUILD_PYTHON to the corpus build environment."
                        return _failure(stage, detail, stages, started)

                stage = "validate"
                chunks = staging / "chunks.jsonl"
                counts: dict[str, int] = {}
                with chunks.open(encoding="utf-8") as handle:
                    for line in handle:
                        source = json.loads(line)["corpus_source"]
                        counts[source] = counts.get(source, 0) + 1
                if not counts:
                    raise ValueError("No indexable chunks were produced. Check the configured sources and cached pages.")
                if scrape and (missing := set(requested) - counts.keys()):
                    raise ValueError(f"No indexable chunks for requested sources: {', '.join(sorted(missing))}")
                if snapshot != registry.read_bytes():
                    raise ValueError("sources.yaml changed during the build. Retry with the current configuration.")

                stage = "index"
                index = None
                if reindex:
                    index = ingest(chunks, store.settings, recreate=True, store=store)
                    stages.append({"stage": stage, "ok": True, **index})

                report = {
                    "ok": True,
                    "failed_stage": None,
                    "stages": stages,
                    "seconds": round(time.monotonic() - started, 1),
                    "configured_sources": configured,
                    "scraped_sources": requested if scrape else [],
                    "chunks_by_source": counts,
                    "sources_without_chunks": sorted(set(configured) - counts.keys()),
                    "indexed": reindex,
                }
                if index:
                    report["active_collection"] = index["active_collection"]
                try:
                    manifest = staging / "manifest.json"
                    manifest.write_text(json.dumps(report, indent=2), encoding="utf-8")
                    for name in ("normalize_report.json", "documents.jsonl", "parents.jsonl", "chunks.jsonl", "manifest.json"):
                        (staging / name).replace(corpus / name)
                except OSError as exc:
                    if not index:
                        return _failure("artifacts", str(exc), stages, started)
                    report["warnings"] = [f"The index is active. Saving the local corpus artifacts failed: {exc}"]
                return report
    except portalocker.exceptions.AlreadyLocked:
        return _failure(stage, "A corpus rebuild is already running for this data home.", stages, started)
    except Exception as exc:
        return _failure(stage, str(exc), stages, started)
    finally:
        if owns_store and store is not None:
            store.close()


def _failure(stage: str, error: str, stages: list[dict], started: float) -> dict:
    return {
        "ok": False,
        "failed_stage": stage,
        "error": error,
        "seconds": round(time.monotonic() - started, 1),
        "stages": stages,
    }
