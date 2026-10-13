"""Withhold reviewed PubChem equivalences without changing raw source assertions."""

from __future__ import annotations

import re
from datetime import date
from urllib.parse import urlsplit

from naturalproductmech.curate.structure_corrections import row_digest


def load_xref_exclusions(
    source_rows: list[dict[str, str]],
    decisions: list[dict[str, str]],
) -> dict[str, list[dict[str, str]]]:
    """Pin each decision to one complete MIBiG row and one literal PubChem xref."""
    result: dict[str, list[dict[str, str]]] = {}
    seen = set()
    required = {
        "source_id", "expected_source_row_sha256", "xref", "reference",
        "curator", "date", "rationale",
    }
    for item in decisions:
        if set(item) != required or any(
            not isinstance(item[field], str) or not item[field].strip()
            or item[field] != item[field].strip() for field in required
        ):
            raise ValueError("xref exclusion requires exact fields, source pin and attribution")
        source_id, xref = item["source_id"], item["xref"]
        if not re.fullmatch(r"BGC\d{7}:[1-9]\d*", source_id):
            raise ValueError("xref exclusion requires an exact MIBiG compound source_id")
        if not re.fullmatch(r"pubchem:[1-9]\d*", xref):
            raise ValueError(f"{source_id}: only literal PubChem xref exclusions are supported")
        if (source_id, xref) in seen:
            raise ValueError(f"{source_id}: duplicate xref exclusion")
        seen.add((source_id, xref))
        if not re.fullmatch(r"[a-f0-9]{64}", item["expected_source_row_sha256"]):
            raise ValueError(f"{source_id}: invalid source digest")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", item["date"]):
            raise ValueError(f"{source_id}: invalid exclusion date")
        date.fromisoformat(item["date"])
        reference = item["reference"]
        url = urlsplit(reference)
        if not (re.fullmatch(r"(?:DOI:10\.\d{4,9}/\S+|PMID:\d+)", reference) or (
            url.scheme == "https" and url.hostname and not re.search(r"\s", reference)
        )):
            raise ValueError(f"{source_id}: exclusion requires a stable reference")
        matches = [row for row in source_rows
                   if f"{row['mibig_accession']}:{row['compound_index']}" == source_id]
        if len(matches) != 1:
            raise ValueError(f"{source_id}: exclusion requires exactly one source row")
        row = matches[0]
        if row_digest(row) != item["expected_source_row_sha256"]:
            raise ValueError(f"{source_id}: xref exclusion source drift")
        if xref not in row.get("database_ids", "").split("|"):
            raise ValueError(f"{source_id}: excluded xref is not asserted by the source")
        result.setdefault(source_id, []).append(dict(item))
    return result


def exclusion_discussion(decision: dict[str, str]) -> dict:
    """Retain source assertion and curator adjudication outside exact-equivalence xrefs."""
    source_id, xref = decision["source_id"], decision["xref"]
    note = (
        f"MIBiG source row {source_id} asserts {xref}; the raw inventory is unchanged. "
        f"This xref is withheld from exact equivalence. {decision['rationale']} "
        f"Source row SHA256 {decision['expected_source_row_sha256']}. "
        f"Curator: {decision['curator']}; date: {decision['date']}."
    )
    return {
        "discussion_id": "source-xref-exclusion-" + (source_id + "-" + xref).replace(":", "-"),
        "kind": "CONTROVERSY", "status": "RESOLVED",
        "prompt": f"Does the imported {xref} identify this exact structure?",
        "resolution_note": note,
        "evidence": [{"reference": decision["reference"],
                      "evidence_source": "database structure; curator interpretation",
                      "notes": note}],
    }
