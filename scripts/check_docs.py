#!/usr/bin/env python3
"""Keep README's generated statistics block in step with the corpus.

A README figure that has drifted is not cosmetic here: the fleet's own review
history shows counts moving by thousands inside one session, and issues quote
them. `--check` fails when the block is stale; `--write` regenerates it.

    python scripts/check_docs.py --check
    python scripts/check_docs.py --write
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
README = REPO_ROOT / "README.md"
BEGIN = "<!-- BEGIN GENERATED CORPUS STATS -->"
END = "<!-- END GENERATED CORPUS STATS -->"


def generate() -> str:
    """The block, built from the report so there is one source of truth."""
    out = subprocess.run(
        [sys.executable, "scripts/np_report.py"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    ).stdout.strip()
    return f"{BEGIN}\n\n```\n{out}\n```\n\n{END}"


def replace_block(text: str, block: str) -> str:
    start, end = text.index(BEGIN), text.index(END) + len(END)
    return text[:start] + block + text[end:]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    text = README.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        print(f"README.md has no generated statistics block ({BEGIN})", file=sys.stderr)
        return 1

    block = generate()
    updated = replace_block(text, block)

    if args.write:
        README.write_text(updated, encoding="utf-8")
        print("README statistics block refreshed")
        return 0

    if updated != text:
        print("README statistics block is stale; run `just docs-stats`", file=sys.stderr)
        return 1
    print("README statistics block is current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
