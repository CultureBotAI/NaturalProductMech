"""The curation backlog's queues (#52), and the drift detection #43 asked for.

Each queue is a claim about what needs a curator's decision, so each is tested
on a record built to sit in it and a record built not to.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location(
    "curation_worklist", REPO_ROOT / "scripts" / "curation_worklist.py")
worklist = importlib.util.module_from_spec(_spec)
sys.modules["curation_worklist"] = worklist
_spec.loader.exec_module(worklist)

PATH = Path("data/natural_products/polyketides/x.yaml")


def rec(**fields):
    return (REPO_ROOT / PATH, {"identifier": "CHEBI:1", "label": "x", **fields})


def test_a_producer_claim_with_no_causal_basis_is_queued():
    rows = worklist.queue_producer_evidence(
        [rec(producer_organisms=[{"evidence_basis": "SOURCE_ASSERTION"}])], None)
    assert [r["queue"] for r in rows] == ["producer-evidence"]


def test_a_characterized_producer_is_not_queued():
    rows = worklist.queue_producer_evidence(
        [rec(producer_organisms=[{"evidence_basis": "BGC_CHARACTERIZED"}])], None)
    assert rows == []


def test_a_record_with_no_producer_at_all_is_not_in_the_producer_queue():
    """It belongs in occurrence-only, or nowhere. Queueing it here would say a
    claim is weak when no claim was made."""
    assert worklist.queue_producer_evidence([rec()], None) == []


def test_occurrences_without_a_producer_are_queued():
    rows = worklist.queue_occurrence_only([rec(occurrences=[{"taxon_id": "NCBITaxon:1"}])], None)
    assert [r["queue"] for r in rows] == ["occurrence-only"]
    assert worklist.queue_occurrence_only(
        [rec(occurrences=[{}], producer_organisms=[{"evidence_basis": "SOURCE_ASSERTION"}])],
        None) == []


def test_biosynthesis_ranks_by_the_evidence_already_waiting():
    strong = rec(label="strong",
                 biosynthetic_gene_clusters=[{"link_evidence_basis": "CLUSTER_DEMONSTRATED"}],
                 producer_organisms=[{"evidence_basis": "BGC_CHARACTERIZED"}])
    weak = rec(label="weak",
               biosynthetic_gene_clusters=[{"link_evidence_basis": "CLUSTER_UNSTATED"}],
               producer_organisms=[{"evidence_basis": "BGC_CHARACTERIZED"}])
    rows = worklist.queue_biosynthesis([weak, strong], None)
    assert {r["label"] for r in rows} == {"strong", "weak"}
    assert int(dict(zip([r["label"] for r in rows], [r["rank"] for r in rows],
                        strict=True))["strong"]) > int(
        dict(zip([r["label"] for r in rows], [r["rank"] for r in rows], strict=True))["weak"])


def test_a_record_that_already_has_a_pathway_is_not_queued_for_biosynthesis():
    rows = worklist.queue_biosynthesis(
        [rec(biosynthetic_pathway=[{"step": 1}],
             biosynthetic_gene_clusters=[{"link_evidence_basis": "CLUSTER_DEMONSTRATED"}])], None)
    assert rows == []


def test_a_resolved_discussion_leaves_its_queue():
    build = worklist.discussion_queue("structure-disagreement", "structure-disagreement")
    open_row = rec(discussions=[{"discussion_id": "structure-disagreement",
                                 "status": "OPEN", "prompt": "q"}])
    done_row = rec(discussions=[{"discussion_id": "structure-disagreement",
                                 "status": "RESOLVED", "prompt": "q"}])
    assert len(build([open_row], None)) == 1
    assert build([done_row], None) == []


def test_stereo_incomplete_is_queued_only_when_the_flag_is_false():
    assert len(worklist.queue_stereo_incomplete(
        [rec(chemical_structure={"stereo_complete": False, "standard_inchi_key": "K"})], None)) == 1
    assert worklist.queue_stereo_incomplete(
        [rec(chemical_structure={"stereo_complete": True, "standard_inchi_key": "K"})], None) == []


def test_every_declared_queue_is_reachable_from_the_cli():
    """A queue nobody can ask for is a queue nobody will work."""
    assert set(worklist.QUEUE_ORDER) == set(worklist.QUEUES)
