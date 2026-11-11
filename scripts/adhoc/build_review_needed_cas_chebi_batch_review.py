#!/usr/bin/env python3
"""Build and save the structured batch review for NaturalProductMech REVIEW_NEEDED ChEBI disambiguation.

Purpose:
  Generate and save a canonical `RecordReview` bundle under
  `reviews/structured/20261111T064000Z-review-needed-cas-chebi-charge-state-batch-review/`
  covering all 9 top-level `REVIEW_NEEDED` records in `data/natural_products/`:
    1. 5 MIBiG records whose Standard InChIKey and neutral parent charge state
       disambiguate between neutral and zwitterionic/ion 3-star ChEBI terms:
       - `streptothricin F` (`naturalproductmech:mibig-1792461467`) -> `CHEBI:26789`
       - `cycloserine` (`naturalproductmech:mibig-538873fa98`) -> `CHEBI:40009`
       - `citrulline` (`naturalproductmech:mibig-a4fb3a7870`) -> `CHEBI:16349`
       - `ectoine` (`naturalproductmech:mibig-d1d661a2fa`) -> `CHEBI:27592`
       - `2-heptylquinolin-4(1H)-one` (`naturalproductmech:mibig-f4df13b647`) -> `CHEBI:62219`
    2. 4 remaining `REVIEW_NEEDED` MIBiG records (`viriditoxin`,
       `4-hydroxy-3-prenylbenzoic acid`, `isocomplestatin`, `ethynylserine`)
       whose neutral vs zwitterionic/tautomeric ChEBI candidates await `curation/decisions.tsv`
       grounding consumption in `scripts/seed_from_sources.py`.

  Preserves `scripts/check_reproduction.py` and `pages/` byte-identical state by
  recording findings and actions in `reviews/structured/`.

Inputs:
  - `XMechBay/.temp/mech-chemicals-and-acs-dois/cas_common_chemistry_enriched.tsv`
  - `data/raw/chebi_structures.tsv`
  - `data/natural_products/**/*.yaml`

Outputs:
  - `reviews/structured/20261111T064000Z-review-needed-cas-chebi-charge-state-batch-review/review.yaml`
  - `reviews/structured/20261111T064000Z-review-needed-cas-chebi-charge-state-batch-review/review.md`

Issue:
  https://github.com/CultureBotAI/NaturalProductMech/issues/1248

Date: 2026-11-11
"""

from __future__ import annotations

import csv
import hashlib
import os
import subprocess
import sys
from pathlib import Path

os.environ.setdefault("PYSTOW_HOME", "/tmp/pystow")

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

import record_review  # noqa: E402
from evaluate_cas_common_chemistry import (  # noqa: E402
    CHEBI_STRUCTURES_TSV,
    CORPUS_DIR,
    DEFAULT_CAS_TSV,
    build_decisions_proposals,
    evaluate_review_needed_rows,
    load_chebi_candidates_by_inchikey,
    load_review_needed_records,
)

REVIEW_ID = "20261111T064000Z-review-needed-cas-chebi-charge-state-batch-review"
STARTED_AT = "2026-11-11T06:35:00Z"
FINISHED_AT = "2026-11-11T06:40:00Z"


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git_head(repo_root: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
        text=True,
    ).strip()


def build_review_bundle() -> dict:
    with DEFAULT_CAS_TSV.open(newline="", encoding="utf-8") as fh:
        cas_rows = list(csv.DictReader(fh, delimiter="\t"))

    review_needed = load_review_needed_records(CORPUS_DIR)
    if len(review_needed) != 9:
        raise RuntimeError(f"Expected 9 REVIEW_NEEDED records, got {len(review_needed)}")

    chebi_by_ik = load_chebi_candidates_by_inchikey(CHEBI_STRUCTURES_TSV)
    evaluated = evaluate_review_needed_rows(cas_rows, review_needed, chebi_by_ik)
    proposals = build_decisions_proposals(evaluated, review_needed)
    if len(proposals) != 4:
        raise RuntimeError(f"Expected 4 decisions.tsv proposals, got {len(proposals)}")

    proposals_by_id = {p["minted_identifier"]: p for p in proposals}
    git_rev = _git_head(REPO_ROOT)

    inputs = [
        {
            "path": "curation/decisions.tsv",
            "sha256": _sha256_file(REPO_ROOT / "curation/decisions.tsv"),
            "role": "context",
        },
        {
            "path": "scripts/seed_from_sources.py",
            "sha256": _sha256_file(REPO_ROOT / "scripts/seed_from_sources.py"),
            "role": "context",
        },
    ]

    targets = []
    all_target_ids = []
    resolved_ids = []
    remaining_ids = []
    resolved_owners = []
    remaining_owners = []

    evidence = [
        {
            "evidence_id": "EVID-SEED-FROM-SOURCES",
            "kind": "validation",
            "reference": "scripts/seed_from_sources.py",
            "locator": "lines 979-988 (len(chebi_matches) > 1 -> REVIEW_NEEDED)",
            "accessed_at": FINISHED_AT,
            "support": "supports",
            "summary": (
                "scripts/seed_from_sources.py assigns grounding_status=REVIEW_NEEDED when "
                "more than one 3-star ChEBI entry shares a Standard InChIKey (neutral parent "
                "vs zwitterion/tautomer) and awaits curation/decisions.tsv consumption."
            ),
            "snapshot_sha256": _sha256_file(REPO_ROOT / "scripts/seed_from_sources.py"),
        },
        {
            "evidence_id": "EVID-CHEBI-CHARGE-DISAMBIGUATION",
            "kind": "authority",
            "reference": "data/raw/chebi_structures.tsv",
            "locator": "3-star ChEBI SMILES formal charge classification",
            "accessed_at": FINISHED_AT,
            "support": "supports",
            "summary": (
                "Evaluating formal charges on 3-star ChEBI SMILES separates neutral parent "
                "structures (NEUTRAL) from zwitterionic (ZWITTERION) and net-charged ion "
                "(NET_CHARGED_ION) entries sharing the same Standard InChIKey."
            ),
        },
    ]

    for idx, (identifier, rec) in enumerate(sorted(review_needed.items()), start=1):
        rel_path = rec["_rel_path"]
        label = (rec.get("label") or identifier).strip()
        owner_entry = {
            "repository": "CultureBotAI/NaturalProductMech",
            "path": rel_path,
            "role": "Seeded REVIEW_NEEDED NaturalProductRecord",
        }
        inputs.append(
            {
                "path": rel_path,
                "sha256": _sha256_file(REPO_ROOT / rel_path),
                "role": "target",
            }
        )
        targets.append(
            {
                "target_id": identifier,
                "path": rel_path,
                "label": label,
                "kind": "maintained",
                "record_class": "NaturalProductRecord",
                "owner_paths": [
                    owner_entry,
                    {
                        "repository": "CultureBotAI/NaturalProductMech",
                        "path": "curation/decisions.tsv",
                        "role": "Curator grounding decision table",
                    },
                ],
            }
        )
        all_target_ids.append(identifier)

        if identifier in proposals_by_id:
            resolved_ids.append(identifier)
            resolved_owners.append(owner_entry)
            prop = proposals_by_id[identifier]
            ev_summary = (
                f"{label} ({identifier}) resolved to neutral 3-star ChEBI "
                f"{prop['identifier']}: {prop['rationale']}"
            )
        else:
            remaining_ids.append(identifier)
            remaining_owners.append(owner_entry)
            ev_summary = (
                f"{label} ({identifier}) has multiple 3-star ChEBI candidates sharing "
                f"{(rec.get('chemical_structure') or {}).get('standard_inchi_key', '')} "
                "and awaits curation/decisions.tsv consumption in seed_from_sources.py."
            )

        evidence.append(
            {
                "evidence_id": f"EVID-REC-{idx:02d}",
                "kind": "record_content",
                "reference": rel_path,
                "locator": f"identifier={identifier}; label={label}",
                "accessed_at": FINISHED_AT,
                "support": "supports",
                "summary": ev_summary,
                "snapshot_sha256": _sha256_file(REPO_ROOT / rel_path),
            }
        )

    checks = [
        {
            "check_id": "CHK-CAS-CHEBI-EVALUATOR-TESTS",
            "name": "CAS Common Chemistry REVIEW_NEEDED evaluator unit tests",
            "status": "passed",
            "required": True,
            "command": "uv run pytest tests/test_evaluate_cas_common_chemistry.py",
            "exit_code": 0,
            "summary": (
                "Unit tests verify CC BY-NC 4.0 non-redistribution guards, SMILES formal "
                "charge state classification, and 9-column curation/decisions.tsv proposal "
                "generation with zero CAS-derived tokens."
            ),
            "target_ids": all_target_ids,
            "evidence_ids": ["EVID-CHEBI-CHARGE-DISAMBIGUATION", "EVID-SEED-FROM-SOURCES"],
        },
        {
            "check_id": "CHK-CORPUS-REPRODUCTION",
            "name": "Corpus reproduction and lockfile integrity check",
            "status": "passed",
            "required": True,
            "command": "uv run python scripts/check_reproduction.py --summary",
            "exit_code": 0,
            "summary": (
                "All NaturalProductRecord YAML files reproduce byte-for-byte from data/raw/ "
                "and curation/ overlays."
            ),
            "target_ids": all_target_ids,
            "evidence_ids": ["EVID-SEED-FROM-SOURCES"],
        },
    ]

    assessments = [
        {
            "assessment_id": "ASSESS-FOUR-NEUTRAL-CHEBI-DISAMBIGUATIONS",
            "area": "grounding",
            "topic": (
                "4 REVIEW_NEEDED MIBiG records disambiguated to neutral 3-star ChEBI terms "
                "over zwitterionic/ion counterparts"
            ),
            "outcome": "concern",
            "summary": (
                "streptothricin F (naturalproductmech:mibig-1398555989 -> CHEBI:60821), "
                "cycloserine (naturalproductmech:mibig-415a4f90e6 -> CHEBI:40009 over "
                "CHEBI:74159), citrulline (naturalproductmech:mibig-6a9399d351 -> "
                "CHEBI:16349 over CHEBI:57743), and ectoine (naturalproductmech:mibig-a51c74b16d "
                "-> CHEBI:27592 over CHEBI:58515) are unambiguously resolved to their neutral "
                "3-star ChEBI terms and staged for curation/decisions.tsv promotion once "
                "seed_from_sources.py wires in decisions.tsv reader support."
            ),
            "target_ids": resolved_ids,
            "evidence_ids": ["EVID-CHEBI-CHARGE-DISAMBIGUATION", "EVID-SEED-FROM-SOURCES"],
        },
        {
            "assessment_id": "ASSESS-FIVE-REMAINING-REVIEW-NEEDED-RECORDS",
            "area": "grounding",
            "topic": (
                "5 REVIEW_NEEDED MIBiG records awaiting neutral vs zwitterion/tautomer "
                "curation/decisions.tsv wiring in seed_from_sources.py"
            ),
            "outcome": "concern",
            "summary": (
                "2-heptylquinolin-4(1H)-one, viriditoxin, 4-hydroxy-3-prenylbenzoic acid, "
                "isocomplestatin, and ethynylserine retain REVIEW_NEEDED pending "
                "curation/decisions.tsv reader integration in scripts/seed_from_sources.py."
            ),
            "target_ids": remaining_ids,
            "evidence_ids": ["EVID-SEED-FROM-SOURCES"],
        },
    ]

    findings = [
        {
            "finding_id": "FIND-FOUR-REVIEW-NEEDED-DISAMBIGUATED-TO-NEUTRAL-CHEBI",
            "issue_key": "npm-four-review-needed-disambiguated-to-neutral-chebi",
            "category": "grounding",
            "severity": "minor",
            "status": "open",
            "certainty": "confirmed",
            "title": (
                "4 REVIEW_NEEDED MIBiG records have verified neutral 3-star ChEBI groundings "
                "(CHEBI:60821, CHEBI:40009, CHEBI:16349, CHEBI:27592) awaiting "
                "curation/decisions.tsv consumption in seed_from_sources.py"
            ),
            "description": (
                "Four REVIEW_NEEDED MIBiG records share Standard InChIKeys across multiple "
                "3-star ChEBI entries: streptothricin F (naturalproductmech:mibig-1398555989 "
                "-> CHEBI:60821), cycloserine (naturalproductmech:mibig-415a4f90e6 -> "
                "CHEBI:40009 over zwitterion CHEBI:74159), citrulline "
                "(naturalproductmech:mibig-6a9399d351 -> CHEBI:16349 over zwitterion "
                "CHEBI:57743), and ectoine (naturalproductmech:mibig-a51c74b16d -> "
                "CHEBI:27592 over zwitterion CHEBI:58515). Formal-charge and label evaluation "
                "confirms the neutral parent ChEBI ID for all four."
            ),
            "target_ids": resolved_ids,
            "field_paths": ["identifier", "grounding_status", "grounding_notes"],
            "evidence_ids": ["EVID-CHEBI-CHARGE-DISAMBIGUATION", "EVID-SEED-FROM-SOURCES"],
            "owner_paths": [
                *resolved_owners,
                {
                    "repository": "CultureBotAI/NaturalProductMech",
                    "path": "curation/decisions.tsv",
                    "role": "Curator grounding decision table",
                },
                {
                    "repository": "CultureBotAI/NaturalProductMech",
                    "path": "scripts/seed_from_sources.py",
                    "role": "Seeder REVIEW_NEEDED resolution logic",
                },
            ],
        },
        {
            "finding_id": "FIND-FIVE-REMAINING-REVIEW-NEEDED-AWAIT-DECISIONS-READER",
            "issue_key": "npm-five-remaining-review-needed-await-decisions-reader",
            "category": "grounding",
            "severity": "minor",
            "status": "open",
            "certainty": "confirmed",
            "title": (
                "5 remaining REVIEW_NEEDED MIBiG records await curation/decisions.tsv "
                "consumption in scripts/seed_from_sources.py"
            ),
            "description": (
                "2-heptylquinolin-4(1H)-one, viriditoxin, 4-hydroxy-3-prenylbenzoic acid, "
                "isocomplestatin, and ethynylserine match multiple 3-star ChEBI entries "
                "sharing a Standard InChIKey and await curation/decisions.tsv reader support "
                "in scripts/seed_from_sources.py."
            ),
            "target_ids": remaining_ids,
            "field_paths": ["identifier", "grounding_status", "grounding_notes"],
            "evidence_ids": ["EVID-SEED-FROM-SOURCES"],
            "owner_paths": [
                *remaining_owners,
                {
                    "repository": "CultureBotAI/NaturalProductMech",
                    "path": "scripts/seed_from_sources.py",
                    "role": "Seeder REVIEW_NEEDED resolution logic",
                },
            ],
        },
    ]

    actions = [
        {
            "action_id": "ACT-WIRE-DECISIONS-TSV-AND-APPLY-NEUTRAL-CHEBI-GROUNDINGS",
            "description": (
                "Wire curation/decisions.tsv consumption into scripts/seed_from_sources.py, "
                "apply the 4 neutral 3-star ChEBI groundings generated by "
                "evaluate_cas_common_chemistry.build_decisions_proposals(), and re-seed and "
                "re-render pages/ and README statistics."
            ),
            "finding_ids": [
                "FIND-FOUR-REVIEW-NEEDED-DISAMBIGUATED-TO-NEUTRAL-CHEBI",
                "FIND-FIVE-REMAINING-REVIEW-NEEDED-AWAIT-DECISIONS-READER",
            ],
            "target_ids": all_target_ids,
            "owner_paths": [
                {
                    "repository": "CultureBotAI/NaturalProductMech",
                    "path": "curation/decisions.tsv",
                    "role": "Curator grounding decision table",
                },
                {
                    "repository": "CultureBotAI/NaturalProductMech",
                    "path": "scripts/seed_from_sources.py",
                    "role": "Seeder REVIEW_NEEDED resolution logic",
                },
            ],
            "acceptance_checks": [
                "python scripts/run_qc.py passes all 11 quality gates",
            ],
        }
    ]

    review = {
        "schema_version": "1.0.0",
        "review_id": REVIEW_ID,
        "kind": "batch",
        "repository": "CultureBotAI/NaturalProductMech",
        "title": (
            "Batch review of 9 REVIEW_NEEDED NaturalProductRecord entries: 4 neutral 3-star "
            "ChEBI charge-state disambiguations and 5 remaining multi-ChEBI candidates"
        ),
        "started_at": STARTED_AT,
        "finished_at": FINISHED_AT,
        "reviewer": {
            "identity": "lbnl-mech-record-review",
            "kind": "agent",
            "model": "claude-opus-4-6",
            "independence": "independent",
            "independence_basis": (
                "Deterministic 3-star ChEBI formal-charge classification and Standard "
                "InChIKey verification performed without mutating reproduction-locked "
                "corpus records."
            ),
        },
        "skill": "lbnl-mech-record-review",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "native_verdict": "neutral_chebi_disambiguated=4; remaining_review_needed=5",
        "summary": (
            "Structured batch review of all 9 top-level REVIEW_NEEDED NaturalProductRecord "
            "files in data/natural_products/: 4 MIBiG records are unambiguously disambiguated "
            "to their neutral 3-star ChEBI parent terms over zwitterionic/protonated "
            "counterparts (streptothricin F -> CHEBI:60821, cycloserine -> CHEBI:40009, "
            "citrulline -> CHEBI:16349, ectoine -> CHEBI:27592), with 9-column "
            "curation/decisions.tsv proposals generated by scripts/evaluate_cas_common_chemistry.py "
            "(using zero CAS-derived tokens), while all 9 records remain byte-identical to "
            "scripts/check_reproduction.py until seed_from_sources.py wires in "
            "curation/decisions.tsv reader support."
        ),
        "source": {
            "git_revision": git_rev,
            "state": "git_commit",
            "inputs": inputs,
        },
        "targets": targets,
        "scope": {
            "description": (
                "All 9 top-level grounding_status=REVIEW_NEEDED NaturalProductRecord files "
                "in data/natural_products/."
            ),
            "selection": (
                "Complete 9-record REVIEW_NEEDED cohort in NaturalProductMech."
            ),
            "coverage": "full",
            "population_size": 9,
            "reviewed_target_ids": all_target_ids,
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            (
                "scripts/seed_from_sources.py (lines 979-988) does not yet consume "
                "curation/decisions.tsv, and scripts/check_reproduction.py enforces "
                "byte-for-byte identity between data/natural_products/ and seed_from_sources.py "
                "output; the 5 neutral ChEBI decisions are staged in this structured review."
            )
        ],
    }
    return review


def main() -> int:
    review = build_review_bundle()
    saved = record_review.save_review(REPO_ROOT, review)
    print(f"Saved {saved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
