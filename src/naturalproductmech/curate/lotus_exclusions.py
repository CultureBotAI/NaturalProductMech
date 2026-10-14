"""Withhold a reviewed LOTUS triple while retaining the raw assertion."""

from __future__ import annotations

import re
from datetime import date
from urllib.parse import urlsplit

from naturalproductmech.curate.structure_corrections import row_digest

LotusKey = tuple[str, str, str]


def lotus_key(row: dict[str, str]) -> LotusKey:
    return row["standard_inchi_key"], row["taxon_id"], row["reference_doi"]


def load_lotus_exclusions(
    source_rows: list[dict[str, str]], decisions: list[dict[str, str]],
) -> dict[LotusKey, dict[str, str]]:
    """Require a unique exact triple and pin every source field, including empty ones."""
    required = {"standard_inchi_key", "taxon_id", "reference_doi",
                "expected_source_row_sha256", "reference", "curator", "date", "rationale"}
    result: dict[LotusKey, dict[str, str]] = {}
    for item in decisions:
        if set(item) != required or any(
            not isinstance(item[field], str) or not item[field].strip()
            or item[field] != item[field].strip() for field in required
        ):
            raise ValueError("LOTUS exclusion requires exact fields, source pin and attribution")
        key = lotus_key(item)
        if not (re.fullmatch(r"[A-Z]{14}-[A-Z]{10}-[A-Z]", key[0])
                and re.fullmatch(r"NCBITaxon:[1-9]\d*", key[1])
                and re.fullmatch(r"10\.\d{4,9}/\S+", key[2])):
            raise ValueError("LOTUS exclusion requires an exact InChIKey, taxon and DOI")
        if key in result:
            raise ValueError(f"{key}: duplicate LOTUS exclusion")
        if not re.fullmatch(r"[a-f0-9]{64}", item["expected_source_row_sha256"]):
            raise ValueError(f"{key}: invalid source digest")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", item["date"]):
            raise ValueError(f"{key}: invalid exclusion date")
        date.fromisoformat(item["date"])
        reference = item["reference"]
        url = urlsplit(reference)
        if not (re.fullmatch(r"(?:DOI:10\.\d{4,9}/\S+|PMID:\d+)", reference) or (
            url.scheme == "https" and url.hostname and not re.search(r"\s", reference)
        )):
            raise ValueError(f"{key}: exclusion requires a stable reference")
        matches = [row for row in source_rows if lotus_key(row) == key]
        if len(matches) != 1:
            raise ValueError(f"{key}: exclusion requires exactly one source row")
        if row_digest(matches[0]) != item["expected_source_row_sha256"]:
            raise ValueError(f"{key}: LOTUS exclusion source drift")
        result[key] = dict(item)
    return result


def lotus_exclusion_discussion(decision: dict[str, str]) -> dict:
    key, taxon, doi = lotus_key(decision)
    note = (
        f"LOTUS source triple {key}, {taxon}, DOI:{doi} is withheld from occurrences; "
        f"the raw inventory is unchanged. {decision['rationale']} "
        f"Source row SHA256 {decision['expected_source_row_sha256']}. "
        f"Curator: {decision['curator']}; date: {decision['date']}."
    )
    return {
        "discussion_id": f"source-lotus-exclusion-{decision['expected_source_row_sha256']}",
        "kind": "CONTROVERSY", "status": "RESOLVED",
        "prompt": f"Does DOI:{doi} support occurrence of this structure in {taxon}?",
        "resolution_note": note,
        "evidence": [{"reference": decision["reference"],
                      "evidence_source": "primary source; curator interpretation", "notes": note}],
    }
