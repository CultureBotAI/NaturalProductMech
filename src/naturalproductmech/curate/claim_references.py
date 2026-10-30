"""Reviewed citation routing for exact MIBiG producer and locus assertions."""

from __future__ import annotations

import re
from datetime import date
from urllib.parse import urlsplit

from naturalproductmech.curate.structure_corrections import row_digest


def load_claim_references(source_rows: list[dict[str, str]], decisions: list[dict[str, str]]) -> dict:
    """Reject stale or ambiguous decisions before changing any emitted claim."""
    result = {}
    required = {
        "source_id", "expected_source_row_sha256", "producer_reference", "locus_reference",
        "source_reference", "curator", "date", "rationale",
    }
    for item in decisions:
        if set(item) != required or any(
            not isinstance(item[field], str) or not item[field].strip()
            or item[field] != item[field].strip() for field in required
        ):
            raise ValueError("claim references require exact fields, source pin and attribution")
        source_id = item["source_id"]
        if not re.fullmatch(r"BGC\d{7}:[1-9]\d*", source_id) or source_id in result:
            raise ValueError(f"{source_id}: invalid or duplicate claim references")
        if not re.fullmatch(r"[a-f0-9]{64}", item["expected_source_row_sha256"]):
            raise ValueError(f"{source_id}: invalid source digest")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", item["date"]):
            raise ValueError(f"{source_id}: invalid reference correction date")
        date.fromisoformat(item["date"])
        for field in ("producer_reference", "locus_reference", "source_reference"):
            reference = item[field]
            url = urlsplit(reference)
            if not (re.fullmatch(r"(?:DOI:10\.\d{4,9}/\S+|PMID:[1-9]\d*)", reference) or (
                url.scheme == "https" and url.hostname and not re.search(r"\s", reference)
            )):
                raise ValueError(f"{source_id}: {field} requires a stable reference")
        matches = [row for row in source_rows
                   if f"{row['mibig_accession']}:{row['compound_index']}" == source_id]
        if len(matches) != 1:
            raise ValueError(f"{source_id}: claim references require exactly one source row")
        if row_digest(matches[0]) != item["expected_source_row_sha256"]:
            raise ValueError(f"{source_id}: claim reference source drift")
        if not matches[0].get("taxon_id"):
            raise ValueError(f"{source_id}: cannot route a reference to an unnamed producer")
        result[source_id] = dict(item)
    return result


def correct_claim_reference(claim: dict, row: dict, decision: dict, *, field: str) -> None:
    """Keep database evidence distinct from the curator's citation-routing decision."""
    if field not in {"producer_reference", "locus_reference"}:
        raise ValueError("unsupported claim reference field")
    if row.get("structure_correction_note") and (
        not row.get("structure_source_id")
        or row["structure_source_id"] not in decision["rationale"]
    ):
        raise ValueError(f"{decision['source_id']}: claim references need review after structure correction")
    claim["evidence"][0] = {
        "reference": decision[field],
        "evidence_type": "DATABASE_ASSERTION",
        "notes": (
            f"MIBiG {row['mibig_accession']} entry version {row['entry_version']}; "
            f"claim-specific citation selected through a reviewed {field} correction. "
            "This remains a database assertion, not independently graded experimental evidence."
        ),
    }
    claim["evidence"].append({
        "reference": decision["source_reference"],
        "evidence_type": "CURATOR_INFERENCE",
        "notes": (
            f"Citation routing only. {decision['rationale']} "
            f"Original imported citation {row['primary_reference']} "
            f"({row['reference_basis']}) remains in the raw inventory, not as support for this claim. "
            f"MIBiG source row {decision['source_id']}; SHA256 {decision['expected_source_row_sha256']}. "
            f"Curator: {decision['curator']}; date: {decision['date']}. "
            "Taxon, locus, chemistry and evidence grades are unchanged."
        ),
    })
