"""Versioned BpsA sequence evidence must not accept an unrelated UniParc entry."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "reviews/evidence/20261109-bpsa-uniparc"


def source(name: str) -> dict:
    return json.loads((EVIDENCE / f"{name}.json").read_text())


def test_source_snapshots_match_captured_hashes():
    for entry in source("manifest")["files"]:
        raw = (EVIDENCE / entry["name"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == entry["sha256"]


def test_revised_bpsa_archive_has_the_exact_versioned_reference_sequence():
    revised = source("UPI000444B524")
    sequence = revised["sequence"]["value"]
    assert revised["uniParcId"] == "UPI000444B524"
    assert len(sequence) == 1283
    assert sequence[384] == "T"
    assert sequence == source("A0A2K8PVS5")["sequence"]["value"]
    references = {(row["database"], row["id"], row.get("version"), row["active"])
                  for row in revised["uniParcCrossReferences"]}
    assert ("EMBL", "ACK77757", 2, True) in references
    assert ("EMBL", "ATZ29785", 1, True) in references
    assert ("UniProtKB/TrEMBL", "A0A2K8PVS5", 1, True) in references


def test_historical_bpsa_is_preserved_as_a_distinct_sequence_version():
    historical = source("UPI0001895A6C")["sequence"]["value"]
    revised = source("UPI000444B524")["sequence"]["value"]
    assert len(historical) == len(revised) == 1283
    assert historical[384] == "A"
    assert [i + 1 for i, (old, new) in enumerate(zip(historical, revised, strict=True))
            if old != new] == [385]


def test_previously_cited_archive_cannot_identify_bpsa():
    wrong = source("UPI0001DE5E11")
    assert wrong["uniParcId"] == "UPI0001DE5E11"
    assert len(wrong["sequence"]["value"]) == 146
    assert not any(row["id"] in {"ACK77757", "ATZ29785", "A0A2K8PVS5"}
                   for row in wrong["uniParcCrossReferences"])


@pytest.mark.parametrize("append_later_event", [False, True])
def test_current_indigoidine_assertions_and_history_preserve_identity_boundaries(append_later_event):
    doc = yaml.safe_load((ROOT / "data/natural_products/alkaloids/indigoidine.yaml").read_text())
    if append_later_event:
        doc["curation_history"].append({
            "timestamp": "2026-11-10T00:00:00Z",
            "curator": "offline_test_fixture",
            "action": "ADDED_DISCUSSION",
            "changes": "Synthetic unrelated follow-up for test robustness only.",
        })
    graph = next(row for row in doc["causal_graphs"]
                 if row["graph_id"] == "indigoidine-ccm3239-bpsa-interventions")
    edge = next(row for row in graph["edges"]
                if row["subject"] == "bpsa_historical" and row["object"] == "bpsa_deletion")
    assertions = {row["reference"]: row for row in edge["evidence"]}
    old = assertions["https://rest.uniprot.org/uniparc/UPI0001895A6C.json"]
    assert "ACK77757.1 (Ala385 version 1)" in old["notes"]
    assert "ACK77757.2 (Thr385, UPI000444B524)" in old["notes"]
    assert "UPI0001DE5E11" not in old["notes"]
    revised = assertions["https://rest.uniprot.org/uniparc/UPI000444B524.json"]
    assert revised["evidence_type"] == "DATABASE_ASSERTION"
    assert "1283 aa, Thr385" in revised["notes"]
    assert "not proof of the experimental parental allele" in revised["notes"]
    assert "not proof of the tested parental allele" in edge["notes"]
    nodes = {row["node_id"]: row for row in graph["nodes"]}
    assert nodes["bpsa_historical"]["identifier"] == "NCBIProtein:ACK77757.1"
    # Retain the old event verbatim as historical provenance, and append its correction.
    history = doc["curation_history"]
    historical_index, historical_event = next(
        (index, event) for index, event in enumerate(history)
        if event["action"] == "ADDED_UNIPROT_PROTEIN_EXAMPLES"
        and "#1055" in event["changes"]
        and "UPI0001DE5E11" in event["changes"]
    )
    correction_index, correction_event = next(
        (index, event) for index, event in enumerate(history)
        if event["action"] == "CORRECTED_UNIPARC_REFERENCE"
        and "#1244" in event["changes"]
        and "UPI000444B524" in event["changes"]
    )
    assert historical_index < correction_index
    assert "ACK77757.1" in historical_event["changes"]
    assert "preserved all prior history" in correction_event["changes"]
