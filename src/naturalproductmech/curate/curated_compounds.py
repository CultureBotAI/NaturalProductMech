"""Pinned, explicit curator-seeded ChEBI natural products with causal producer evidence."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from datetime import date

from naturalproductmech.curate.structure_corrections import row_digest
from naturalproductmech.grading import CAUSAL_BASES

CURATED_COMPOUND_COLUMNS = (
    "chebi_id",
    "expected_chebi_row_sha256",
    "standard_inchi",
    "standard_inchi_key",
    "stereo_complete",
    "taxon_id",
    "taxon_label",
    "strain",
    "producer_evidence_basis",
    "mibig_accession",
    "reference",
    "evidence_type",
    "snippet",
    "notes",
    "curator",
    "date",
)

ALLOWED_EVIDENCE_TYPES = {"PRIMARY_EXPERIMENT", "REVIEW"}


def load_curated_compounds(
    rows: list[dict[str, str]],
    chebi_rows: list[dict[str, str]],
    mibig_rows: list[dict[str, str]],
) -> dict[str, list[dict[str, str]]]:
    """Validate curator-seeded ChEBI compounds and group their producer claims by InChIKey.

    Each row pins a 3-star structured ChEBI row by SHA-256 digest and supplies a
    causal producer claim (`BGC_CHARACTERIZED`, `ISOTOPE_FEEDING`, or
    `AXENIC_CULTURE`) backed by a primary experiment or review citation.
    Structures already owned by MIBiG or shared by multiple 3-star ChEBI entries
    are rejected.
    """
    if not rows:
        return {}

    chebi_by_id = {row["chebi_id"]: row for row in chebi_rows}
    chebi_key_counts = Counter(
        row["standard_inchi_key"] for row in chebi_rows if row.get("standard_inchi_key")
    )
    mibig_keys = {
        row["standard_inchi_key"] for row in mibig_rows if row.get("standard_inchi_key")
    }
    mibig_accs = {
        row["mibig_accession"] for row in mibig_rows if row.get("mibig_accession")
    }

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    chem_signature_by_key: dict[str, tuple[str, str, str, str, str]] = {}
    seen_claims: set[tuple[str, str, str, str]] = set()

    required_nonempty = (
        "chebi_id",
        "expected_chebi_row_sha256",
        "standard_inchi",
        "standard_inchi_key",
        "stereo_complete",
        "taxon_id",
        "taxon_label",
        "producer_evidence_basis",
        "reference",
        "evidence_type",
        "notes",
        "curator",
        "date",
    )

    for row in rows:
        if set(row.keys()) != set(CURATED_COMPOUND_COLUMNS):
            raise ValueError("curated compound row has unexpected or missing columns")
        if any(
            not isinstance(row.get(field), str) or not row[field].strip()
            for field in required_nonempty
        ):
            raise ValueError("curated compound requires complete pins, chemistry, producer and citation")
        for optional_field in ("strain", "mibig_accession", "snippet"):
            if not isinstance(row.get(optional_field), str):
                raise ValueError(f"curated compound {optional_field} must be a string")

        chebi_id = row["chebi_id"]
        if not re.fullmatch(r"CHEBI:\d+", chebi_id):
            raise ValueError(f"{chebi_id}: invalid ChEBI CURIE")
        if not re.fullmatch(r"[a-f0-9]{64}", row["expected_chebi_row_sha256"]):
            raise ValueError(f"{chebi_id}: invalid ChEBI row digest")
        if not re.fullmatch(r"InChI=1S/\S+", row["standard_inchi"]):
            raise ValueError(f"{chebi_id}: invalid standard_inchi")
        key = row["standard_inchi_key"]
        if not re.fullmatch(r"[A-Z]{14}-[A-Z]{10}-[A-Z]", key):
            raise ValueError(f"{chebi_id}: invalid standard_inchi_key")
        if row["stereo_complete"] not in {"true", "false"}:
            raise ValueError(f"{chebi_id}: invalid stereo_complete flag")
        if not re.fullmatch(r"NCBITaxon:\d+", row["taxon_id"]):
            raise ValueError(f"{chebi_id}: invalid NCBITaxon CURIE")
        if row["producer_evidence_basis"] not in CAUSAL_BASES:
            raise ValueError(
                f"{chebi_id}: curated compound requires a causal producer_evidence_basis"
            )
        if row["mibig_accession"]:
            if not re.fullmatch(r"BGC\d{7}", row["mibig_accession"]):
                raise ValueError(f"{chebi_id}: invalid mibig_accession")
            if row["producer_evidence_basis"] != "BGC_CHARACTERIZED":
                raise ValueError(
                    f"{chebi_id}: mibig_accession requires producer_evidence_basis BGC_CHARACTERIZED"
                )
            if mibig_accs and row["mibig_accession"] not in mibig_accs:
                raise ValueError(
                    f"{chebi_id}: mibig_accession {row['mibig_accession']} not found in mibig_compounds.tsv"
                )
        if not re.fullmatch(r"(?:DOI:10\.\d{4,9}/\S+|PMID:\d+)", row["reference"]):
            raise ValueError(f"{chebi_id}: curated compound requires a DOI or PMID reference")
        if row["evidence_type"] not in ALLOWED_EVIDENCE_TYPES:
            raise ValueError(f"{chebi_id}: invalid evidence_type")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row["date"]):
            raise ValueError(f"{chebi_id}: invalid ISO date")
        date.fromisoformat(row["date"])

        target = chebi_by_id.get(chebi_id)
        if target is None:
            raise ValueError(f"{chebi_id}: ChEBI row not found in chebi_structures.tsv")
        if row_digest(target) != row["expected_chebi_row_sha256"]:
            raise ValueError(f"{chebi_id}: ChEBI row digest drift")
        if (
            target.get("stars") != "3"
            or not target.get("smiles")
            or target.get("standard_inchi_key") != key
        ):
            raise ValueError(f"{chebi_id}: target must be a structured 3-star ChEBI entry matching key")
        if chebi_key_counts[key] != 1:
            raise ValueError(f"{chebi_id}: target InChIKey {key} is shared by multiple ChEBI entries")
        if key in mibig_keys:
            raise ValueError(f"{chebi_id}: structure {key} is already owned by MIBiG")

        sig = (
            chebi_id,
            row["expected_chebi_row_sha256"],
            row["standard_inchi"],
            key,
            row["stereo_complete"],
        )
        if key in chem_signature_by_key and chem_signature_by_key[key] != sig:
            raise ValueError(f"{chebi_id}: inconsistent chemistry across rows for {key}")
        chem_signature_by_key[key] = sig

        claim_key = (key, row["taxon_id"], row["strain"], row["reference"])
        if claim_key in seen_claims:
            raise ValueError(f"{chebi_id}: duplicate curated producer claim for {claim_key}")
        seen_claims.add(claim_key)

        grouped[key].append(dict(row))

    return dict(grouped)
