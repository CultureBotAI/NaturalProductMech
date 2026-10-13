"""Source-pinned strain/isolate context without changing taxon or evidence grades."""

from __future__ import annotations

import re
from datetime import date
from urllib.parse import urlsplit

from naturalproductmech.curate.structure_corrections import row_digest


def load_producer_strains(
    source_rows: list[dict[str, str]],
    qualifications: list[dict[str, str]],
) -> dict[str, dict[str, str]]:
    """Resolve each qualification against exactly one complete raw compound row."""
    return _load_qualifications(source_rows, qualifications, qualifier="strain")


def load_producer_isolates(
    source_rows: list[dict[str, str]],
    qualifications: list[dict[str, str]],
) -> dict[str, dict[str, str]]:
    """Keep deposit isolate qualifiers distinct from cultured-strain assertions."""
    return _load_qualifications(source_rows, qualifications, qualifier="isolate")


def _load_qualifications(source_rows, qualifications, *, qualifier):
    result = {}
    required = {
        "source_id", "expected_source_row_sha256", qualifier, "reference",
        "curator", "date", "rationale",
    }
    for item in qualifications:
        if set(item) != required or any(
            not isinstance(item[field], str) or not item[field].strip() for field in required
        ):
            raise ValueError(f"producer {qualifier} requires exact fields, source pin and attribution")
        source_id = item["source_id"]
        if not re.fullmatch(r"BGC\d{7}:\d+", source_id) or source_id in result:
            raise ValueError(f"{source_id}: invalid or duplicate producer {qualifier} qualification")
        if not re.fullmatch(r"[a-f0-9]{64}", item["expected_source_row_sha256"]):
            raise ValueError(f"{source_id}: invalid source digest")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", item["date"]):
            raise ValueError(f"{source_id}: invalid qualification date")
        date.fromisoformat(item["date"])
        reference = item["reference"]
        url = urlsplit(reference)
        if not (re.fullmatch(r"(?:DOI:10\.\d{4,9}/\S+|PMID:\d+)", reference) or (
            url.scheme == "https" and url.hostname and not re.search(r"\s", reference)
        )):
            raise ValueError(f"{source_id}: qualification requires a stable reference")
        matches = [row for row in source_rows
                   if f"{row['mibig_accession']}:{row['compound_index']}" == source_id]
        if len(matches) != 1:
            raise ValueError(f"{source_id}: qualification requires exactly one source row")
        if row_digest(matches[0]) != item["expected_source_row_sha256"]:
            raise ValueError(f"{source_id}: producer {qualifier} source drift")
        if not matches[0].get("taxon_id"):
            raise ValueError(f"{source_id}: cannot qualify an unnamed producer")
        result[source_id] = dict(item)
    return result


def qualify_producer(producer: dict, qualification: dict[str, str]) -> None:
    """Attach the curator's interpretation only to the producer claim it scopes."""
    producer["strain"] = qualification["strain"]
    _append_evidence(producer, qualification, qualifier="strain")


def qualify_producer_isolate(producer: dict, qualification: dict[str, str]) -> None:
    """Preserve literal isolate context in notes, never in the strain field."""
    context = f"Deposited isolate: {qualification['isolate']}."
    producer["notes"] = " ".join(filter(None, [producer.get("notes"), context]))
    _append_evidence(producer, qualification, qualifier="isolate")


def _append_evidence(producer, qualification, *, qualifier):
    producer["evidence"].append({
        "reference": qualification["reference"],
        "evidence_type": "CURATOR_INFERENCE",
        "notes": (
            f"{qualifier.capitalize()} context: {qualification[qualifier]}. {qualification['rationale']} "
            "Taxon identity and evidence grade are unchanged; this is not a species-wide experiment. "
            f"MIBiG source row {qualification['source_id']}; "
            f"SHA256 {qualification['expected_source_row_sha256']}. "
            f"Curator: {qualification['curator']}; date: {qualification['date']}."
        ),
    })
