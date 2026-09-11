#!/usr/bin/env python3
"""Run the authoritative NaturalProductMech quality gate locally and in CI.

One executable definition of "green", so a passing local run and a passing CI
run mean the same thing.

The claw vendored-sync check joined this gate at admission (culturebotai-claw
#395, 2026-09-11). Before that it was deliberately absent: its checker resolves
this repository's identity through claw's consumer registry, and until the
manifest declared NaturalProductMech the check failed on identity rather than
on content. The governed files were vendored byte-identically throughout.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

COMMANDS = [
    (
        "lint",
        [sys.executable, "-m", "ruff", "check", "."],
        "Fail fast on syntax, import, and style defects before expensive checks.",
    ),
    (
        "vendored-sync",
        ["bash", "scripts/check_vendored_sync.sh"],
        "Governed files must be byte-identical to claw at the pinned ref.",
    ),
    (
        "documentation",
        [sys.executable, "scripts/check_docs.py", "--check"],
        "README's generated statistics must match the corpus a reader would download.",
    ),
    (
        "raw-data provenance",
        [sys.executable, "scripts/check_provenance.py"],
        "Every committed inventory must retain its source metadata and integrity hash.",
    ),
    (
        "source queue",
        [sys.executable, "scripts/check_source_queue.py"],
        "An ADOPTED source must be one the pipeline reads under verified redistribution terms.",
    ),
    (
        "tests",
        [sys.executable, "-m", "pytest", "-q"],
        "Tests cover harmonization rules and corpus-wide invariants validation cannot see.",
    ),
    (
        "schema validation",
        [sys.executable, "scripts/validate_strict.py", "--quiet"],
        "Closed-mode validation checks every record's shape, including unknown fields.",
    ),
    (
        "generated site",
        [sys.executable, "scripts/render_pages.py", "--check"],
        "pages/ is in step with the corpus. The site is committed, so it goes stale "
        "exactly as a record could go stale against data/raw/ (#53).",
    ),
    (
        "corpus reproduction",
        [sys.executable, "scripts/check_reproduction.py", "--summary"],
        "Every record is byte-identical to what the seeder builds from data/raw/. "
        "The check verify_corpus.py's docstring promised once the harmonizer existed (#85); "
        "curator-owned fields are taken from the file, as the writer takes them.",
    ),
    (
        "lockfile integrity",
        [sys.executable, "scripts/verify_corpus.py"],
        "Every record is recorded in PATHS.tsv and filed where its pinned pathway says. "
        "Reproduction from data/raw/ is the separate check above.",
    ),
    (
        "corpus report",
        [sys.executable, "scripts/np_report.py"],
        "Exercise the report and finish with the live coverage summary.",
    ),
]


def main() -> int:
    for name, command, rationale in COMMANDS:
        print(f"\n=== qc: {name} ===", flush=True)
        print(f"why: {rationale}", flush=True)
        completed = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if completed.returncode:
            print(f"qc stopped: {name} failed with exit code {completed.returncode}",
                  file=sys.stderr)
            return completed.returncode
    print("\nAll NaturalProductMech quality gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
