"""Withhold individually reviewed assay rows without erasing raw provenance."""

from __future__ import annotations

import re
from datetime import date
from urllib.parse import urlsplit

from naturalproductmech.curate.structure_corrections import row_digest

AssayKey = tuple[str, str, str]


def assay_key(row: dict[str, str]) -> AssayKey:
    return row["standard_inchi_key"], row["cid"], row["aid"]


def load_bioassay_exclusions(
    source_rows: list[dict[str, str]],
    decisions: list[dict[str, str]],
) -> dict[AssayKey, dict[str, str]]:
    """Require one exact structure/CID/AID row and pin all of its source fields."""
    required = {
        "standard_inchi_key", "cid", "aid", "expected_source_row_sha256",
        "reference", "curator", "date", "rationale",
    }
    result: dict[AssayKey, dict[str, str]] = {}
    for item in decisions:
        if set(item) != required or any(
            not isinstance(item[field], str) or not item[field].strip()
            or item[field] != item[field].strip() for field in required
        ):
            raise ValueError("bioassay exclusion requires exact fields, source pin and attribution")
        key = assay_key(item)
        if not re.fullmatch(r"[A-Z]{14}-[A-Z]{10}-[A-Z]", key[0]) or any(
            not re.fullmatch(r"[1-9]\d*", value) for value in key[1:]
        ):
            raise ValueError("bioassay exclusion requires an exact InChIKey, CID and AID")
        if key in result:
            raise ValueError(f"{key}: duplicate bioassay exclusion")
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
        matches = [row for row in source_rows if assay_key(row) == key]
        if len(matches) != 1:
            raise ValueError(f"{key}: exclusion requires exactly one source row")
        if row_digest(matches[0]) != item["expected_source_row_sha256"]:
            raise ValueError(f"{key}: bioassay exclusion source drift")
        result[key] = dict(item)
    return result


def bioassay_exclusion_discussion(decision: dict[str, str]) -> dict:
    key, cid, aid = assay_key(decision)
    note = (
        f"PubChem BioAssay source row {key}, CID {cid}, AID {aid} is withheld "
        f"from bioactivities; the raw inventory is unchanged. {decision['rationale']} "
        f"Source row SHA256 {decision['expected_source_row_sha256']}. "
        f"Curator: {decision['curator']}; date: {decision['date']}."
    )
    return {
        "discussion_id": f"source-bioassay-exclusion-{cid}-{aid}",
        "kind": "CONTROVERSY", "status": "RESOLVED",
        "prompt": f"Does imported PubChem AID {aid}, CID {cid} support activity of this structure?",
        "resolution_note": note,
        "evidence": [{"reference": decision["reference"],
                      "evidence_source": "database assay protocol; curator interpretation",
                      "notes": note}],
    }
