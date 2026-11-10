#!/usr/bin/env python3
"""Evaluate CAS Common Chemistry hits for NaturalProductMech REVIEW_NEEDED records.

Purpose:
  An EVALUATOR, not an extractor. CAS Common Chemistry is licensed under
  CC BY-NC 4.0 (https://commonchemistry.cas.org/terms), and this corpus's record
  content is CC BY 4.0, so `scripts/check_source_queue.py` blocks seeding under
  `NON_COMMERCIAL` terms.

  What proceeds without redistributing CC BY-NC data is evaluating how the 9
  `REVIEW_NEEDED` records (where two 3-star ChEBI entries share one Standard
  InChIKey because ChEBI keeps a neutral parent and its zwitterion separate)
  align with CAS Common Chemistry and with the candidate 3-star ChEBI entries in
  `data/raw/chebi_structures.tsv`.

Inputs:
  - Enriched CAS Common Chemistry TSV (`--cas-tsv`)
  - NaturalProductMech corpus (`data/natural_products/**/*.yaml`)
  - `data/raw/chebi_structures.tsv`

Outputs:
  - Summary report to stdout and optional TSV (`--output-tsv` outside
    `data/raw/` and `data/natural_products/`).

Date: 2026-11-09
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
CHEBI_STRUCTURES_TSV = REPO_ROOT / "data" / "raw" / "chebi_structures.tsv"
DEFAULT_CAS_TSV = (
    REPO_ROOT.parent
    / "XMechBay"
    / ".temp"
    / "mech-chemicals-and-acs-dois"
    / "cas_common_chemistry_enriched.tsv"
)

CAS_LICENSE = "CC-BY-NC-4.0"
CORPUS_LICENSE = "CC-BY-4.0"
REDISTRIBUTION_CLASS = "NON_COMMERCIAL"

INCHIKEY_PREFIX_RE = re.compile(r"^InChIKey=", re.IGNORECASE)
ZWITTERION_SIGNAL_RE = re.compile(r"\[\w+\+\].*\[\w+-\]|\[\w+-\].*\[\w+\+\]")


def strip_inchikey_prefix(value: str) -> str:
    """Normalize `InChIKey=XXXX-YYYY-Z` to standard 27-character `XXXX-YYYY-Z`."""
    return INCHIKEY_PREFIX_RE.sub("", (value or "").strip())


def is_zwitterionic_smiles(smiles: str) -> bool:
    """Return True if a SMILES carries both formal positive and negative charges."""
    return bool(ZWITTERION_SIGNAL_RE.search(smiles or ""))


def validate_output_path_is_outside_corpus(output_path: Path, repo_root: Path = REPO_ROOT) -> None:
    """Refuse to write CC BY-NC 4.0 evaluation output inside `data/raw/` or `data/natural_products/`."""
    resolved = output_path.resolve()
    forbidden_roots = (
        (repo_root / "data" / "raw").resolve(),
        (repo_root / "data" / "natural_products").resolve(),
    )
    for forbidden in forbidden_roots:
        if resolved == forbidden or resolved.is_relative_to(forbidden):
            raise ValueError(
                f"Refusing to write {CAS_LICENSE} evaluation output inside {forbidden}: "
                f"{REDISTRIBUTION_CLASS} sources cannot be seeded into {CORPUS_LICENSE} corpus."
            )


def load_chebi_candidates_by_inchikey(
    path: Path = CHEBI_STRUCTURES_TSV,
) -> dict[str, list[dict[str, str]]]:
    """Return all 3-star ChEBI structure rows grouped by `standard_inchi_key`."""
    grouped: dict[str, list[dict[str, str]]] = {}
    if not path.exists():
        return grouped
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            ik = (row.get("standard_inchi_key") or "").strip()
            if ik:
                grouped.setdefault(ik, []).append(row)
    return grouped


def load_review_needed_records(corpus_dir: Path = CORPUS_DIR) -> dict[str, dict]:
    """Load `REVIEW_NEEDED` NaturalProductMech records keyed by `identifier`."""
    records: dict[str, dict] = {}
    if not corpus_dir.exists():
        return records
    for yaml_path in sorted(corpus_dir.rglob("*.yaml")):
        doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        if doc.get("grounding_status") == "REVIEW_NEEDED" and doc.get("identifier"):
            records[doc["identifier"]] = doc
    return records


def evaluate_review_needed_rows(
    cas_rows: list[dict[str, str]],
    review_needed_by_id: dict[str, dict],
    chebi_by_ik: dict[str, list[dict[str, str]]],
) -> list[dict[str, str]]:
    """Compare CAS Common Chemistry structures for REVIEW_NEEDED records against ChEBI candidates."""
    results: list[dict[str, str]] = []
    for row in cas_rows:
        if row.get("mech") != "NaturalProductMech":
            continue
        identifier = (row.get("identifier") or "").strip()
        rec = review_needed_by_id.get(identifier, {})
        cs = rec.get("chemical_structure") or {}
        corpus_ik = (cs.get("standard_inchi_key") or "").strip()
        cas_ik = strip_inchikey_prefix(row.get("inchikey") or "")
        cas_smiles = (row.get("canonical_smiles") or "").strip()
        cas_zwitterion = is_zwitterionic_smiles(cas_smiles)

        candidates = chebi_by_ik.get(corpus_ik or cas_ik, [])
        neutral_chebi = [
            c["chebi_id"]
            for c in candidates
            if not is_zwitterionic_smiles(c.get("smiles") or "")
            and "zwitterion" not in (c.get("name") or "").lower()
        ]
        zwitterion_chebi = [
            c["chebi_id"]
            for c in candidates
            if is_zwitterionic_smiles(c.get("smiles") or "")
            or "zwitterion" in (c.get("name") or "").lower()
        ]

        preferred_chebi = (
            neutral_chebi[0]
            if (not cas_zwitterion and neutral_chebi)
            else (zwitterion_chebi[0] if cas_zwitterion and zwitterion_chebi else "")
        )

        results.append(
            {
                "identifier": identifier,
                "label": (rec.get("label") or row.get("query_name") or "").strip(),
                "cas_rn": (row.get("cas_rn") or "").strip(),
                "cas_name": (row.get("cas_name") or "").strip(),
                "corpus_inchikey": corpus_ik,
                "cas_inchikey": cas_ik,
                "inchikey_agreement": "AGREES" if corpus_ik == cas_ik else "DIFFERS",
                "cas_charge_state": "ZWITTERION" if cas_zwitterion else "NEUTRAL",
                "neutral_chebi_candidates": "|".join(neutral_chebi),
                "zwitterion_chebi_candidates": "|".join(zwitterion_chebi),
                "cas_aligned_chebi_id": preferred_chebi,
            }
        )
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cas-tsv",
        type=Path,
        default=DEFAULT_CAS_TSV,
        help="Path to cas_common_chemistry_enriched.tsv",
    )
    parser.add_argument(
        "--output-tsv",
        type=Path,
        default=None,
        help="Optional output TSV path (must be outside data/raw/ and data/natural_products/)",
    )
    args = parser.parse_args(argv)

    if not args.cas_tsv.exists():
        print(f"missing {args.cas_tsv}; run query_cas_common_chemistry.py first", file=sys.stderr)
        return 1

    if args.output_tsv is not None:
        validate_output_path_is_outside_corpus(args.output_tsv)

    with args.cas_tsv.open(newline="", encoding="utf-8") as fh:
        cas_rows = list(csv.DictReader(fh, delimiter="\t"))

    review_needed = load_review_needed_records(CORPUS_DIR)
    chebi_by_ik = load_chebi_candidates_by_inchikey(CHEBI_STRUCTURES_TSV)
    evaluated = evaluate_review_needed_rows(cas_rows, review_needed, chebi_by_ik)

    print(f"REVIEW_NEEDED records in corpus        : {len(review_needed)}")
    print(f"CAS Common Chemistry hits evaluated    : {len(evaluated)}")
    print()
    for item in evaluated:
        print(
            f"  {item['identifier']} ({item['label']}) -> CAS {item['cas_rn']} "
            f"[{item['cas_charge_state']}] aligns with {item['cas_aligned_chebi_id']} "
            f"(neutral={item['neutral_chebi_candidates']}, "
            f"zwitterion={item['zwitterion_chebi_candidates']})"
        )
    print()
    print("NOT WRITTEN. CAS Common Chemistry is CC BY-NC 4.0, so nothing from it")
    print("enters data/raw/ or the corpus. ChEBI candidate selection remains governed")
    print("by CC BY 4.0 ChEBI structures.")

    if args.output_tsv is not None:
        args.output_tsv.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = [
            "identifier",
            "label",
            "cas_rn",
            "cas_name",
            "corpus_inchikey",
            "cas_inchikey",
            "inchikey_agreement",
            "cas_charge_state",
            "neutral_chebi_candidates",
            "zwitterion_chebi_candidates",
            "cas_aligned_chebi_id",
        ]
        with args.output_tsv.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(
                fh, fieldnames=fieldnames, delimiter="\t", lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(evaluated)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
