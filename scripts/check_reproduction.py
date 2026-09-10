#!/usr/bin/env python3
"""Prove every record is what the seeder produces from the committed inventories.

`verify_corpus.py` checks the lockfile — what exists and where it is filed — and
says in its own docstring that it is NOT a reproduction check, because when it
was written the harmonizer did not exist. It does now, and this is the check
that docstring promised (#85).

What it compares, and why bytes rather than fields
--------------------------------------------------
For each record the seeder builds, this rebuilds the exact payload
``write_records`` would write — including carrying the curator-owned fields
forward from disk, which is what the writer does — serialises it through the
same emitter, and compares it to the file. Byte comparison rather than a field
walk, for two reasons: the emission contract IS byte-identity
(``tests/test_write_validated.py``), and a field walk cannot see key ORDER.
That is not hypothetical — erythromycin A sat on `main` with its keys in an
order the seeder does not emit, through a green gate, and only an unrelated
re-seed surfaced it.

What it deliberately does not compare
-------------------------------------
`biosynthetic_pathway`, `causal_graphs` and `curation_history` are
curator-owned: the seeder carries them across a re-seed rather than producing
them, so comparing them against a rebuild would make this check permanently red
the first time anyone curated anything. They are taken from the file, exactly as
the writer takes them.

And it still cannot catch a FABRICATED claim. A hand-added producer citing an
invented PMID reproduces perfectly, because the inventory says so. That is what
review is for.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from naturalproductmech.validation.write_validated import (  # noqa: E402
    emit_natural_product_yaml,
)


def load_seeder():
    name = "seed_from_sources"
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(
        name, REPO_ROOT / "scripts" / "seed_from_sources.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def first_difference(expected: str, actual: str) -> str:
    """The first line that differs, which is what a reader needs to act."""
    expected_lines, actual_lines = expected.splitlines(), actual.splitlines()
    for number, (want, got) in enumerate(zip(expected_lines, actual_lines, strict=False), start=1):
        if want != got:
            return f"line {number}: expected {want!r}, found {got!r}"
    if len(expected_lines) != len(actual_lines):
        return (f"length differs: the seeder emits {len(expected_lines)} lines, "
                f"the file has {len(actual_lines)}")
    return "files differ only in trailing bytes"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", action="store_true",
                        help="counts only, no per-record detail")
    args = parser.parse_args()

    seed = load_seeder()
    inventories = seed.read_inventories()
    if not inventories:
        print("no inventories in data/raw/, so there is nothing to reproduce from.",
              file=sys.stderr)
        return 0

    records = seed.build_records(inventories)
    problems: list[str] = []
    checked = 0
    on_disk_expected: set[Path] = set()

    for doc in records:
        path = seed.record_path(doc["np_pathway"], doc["_slug"])
        on_disk_expected.add(path)
        payload = {k: v for k, v in doc.items()
                   if not k.startswith(seed.INTERNAL_PREFIX)}
        seed.carry_existing_curator_owned_fields(payload, path)
        previous = seed.read_record(path)
        if previous is None:
            problems.append(f"  {path.relative_to(REPO_ROOT)}: the seeder builds this "
                            f"record and there is no file")
            continue
        # The trail is the writer's, not the seeder's: taking it from disk is
        # what makes a content difference show up as a content difference
        # rather than as a timestamp.
        payload["curation_history"] = previous.get("curation_history", [])
        expected = emit_natural_product_yaml(payload)
        actual = path.read_text(encoding="utf-8")
        checked += 1
        if expected != actual:
            problems.append(f"  {path.relative_to(REPO_ROOT)}: does not reproduce — "
                            f"{first_difference(expected, actual)}")

    for path in sorted(seed.CORPUS_DIR.rglob("*.yaml")):
        if path not in on_disk_expected:
            problems.append(f"  {path.relative_to(REPO_ROOT)}: on disk but the seeder "
                            f"does not build it")

    if problems:
        print("corpus reproduction FAILED:", file=sys.stderr)
        shown = problems if not args.summary else problems[:10]
        for problem in shown:
            print(problem, file=sys.stderr)
        if args.summary and len(problems) > len(shown):
            print(f"  … and {len(problems) - len(shown)} more", file=sys.stderr)
        print(f"\n{len(problems)} record(s) differ from what the seeder produces. "
              f"Re-run `just seed-apply`, or find out why the corpus drifted.",
              file=sys.stderr)
        return 1

    print(f"corpus reproduction OK: {checked} records are byte-identical to what "
          f"the seeder builds from data/raw/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
