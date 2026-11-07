"""Stage 7 - Orchestrate the full post-scrape pipeline.

Usage:
    python run_pipeline.py              # normalize -> enrich -> chunk -> index
    python run_pipeline.py --eval       # ... plus retrieval evaluation
    python run_pipeline.py --from chunk # resume from a stage
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

STAGES = ["normalize", "enrich", "chunk", "index"]
SCRIPT_DIR = Path(__file__).resolve().parent


def run(stage: str) -> None:
    script = SCRIPT_DIR / f"{stage}.py"
    print(f"\n=== {stage} ===", flush=True)
    started = time.time()
    proc = subprocess.run([sys.executable, str(script)], cwd=SCRIPT_DIR)
    if proc.returncode != 0:
        print(f"stage '{stage}' failed (exit {proc.returncode})", file=sys.stderr)
        sys.exit(proc.returncode)
    print(f"--- {stage} ok in {time.time() - started:.1f}s")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from", dest="start", choices=STAGES, default="normalize")
    parser.add_argument("--only", choices=STAGES, default=None)
    parser.add_argument("--eval", action="store_true")
    args = parser.parse_args()

    stages = STAGES[STAGES.index(args.start) :]
    if args.only:
        stages = [args.only]

    started = time.time()
    for stage in stages:
        run(stage)

    if args.eval:
        run_eval = SCRIPT_DIR / "eval_retrieval.py"
        print("\n=== eval ===", flush=True)
        subprocess.run([sys.executable, str(run_eval)], cwd=SCRIPT_DIR)

    print(f"\npipeline complete in {time.time() - started:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
