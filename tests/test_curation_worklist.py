"""The curation backlog's queues (#52), and the drift detection #43 asked for.

Each queue is a claim about what needs a curator's decision, so each is tested
on a record built to sit in it and a record built not to.
"""

from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path

import pytest

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


@pytest.fixture
def review_records(monkeypatch):
    monkeypatch.setattr(worklist, "read_tsv", lambda _path: [])

    def load(*records):
        monkeypatch.setattr(worklist, "load_records", lambda: list(records))

    return load


@pytest.mark.parametrize("status", ["SEEDED", "PROPOSED", None])
def test_review_checkpoint_includes_records_without_findings(review_records, status):
    review_records(rec(curation_status=status))
    assert worklist.build(None) == []
    rows = worklist.build(None, review_records=True)
    assert [r["path"] for r in rows] == [str(PATH)]
    assert rows[0]["queue"] == "record-review"
    assert "full-record review pending" in rows[0]["detail"]


@pytest.mark.parametrize("status", ["REVIEWED", "DEPRECATED"])
def test_review_checkpoint_excludes_completed_records_even_with_findings(review_records, status):
    review_records(rec(curation_status=status, chemical_structure={"stereo_complete": False}))
    assert len(worklist.build(None)) == 1
    assert worklist.build(None, review_records=True) == []


def test_review_checkpoint_keeps_specialized_priority_without_duplicate_fallback(review_records):
    flagged = rec(curation_status="SEEDED", producer_organisms=[{"evidence_basis": "SOURCE_ASSERTION"}])
    unflagged = (REPO_ROOT / "data/natural_products/terpenoids/y.yaml",
                 {"identifier": "CHEBI:2", "label": "y", "curation_status": "PROPOSED"})
    review_records(unflagged, flagged)
    rows = worklist.build(None, review_records=True)
    assert [r["queue"] for r in rows] == ["producer-evidence", "record-review"]
    assert [r["identifier"] for r in rows] == ["CHEBI:1", "CHEBI:2"]


def test_review_fallback_order_is_deterministic(review_records):
    records = [(REPO_ROOT / f"data/natural_products/terpenoids/{name}.yaml",
                {"identifier": "CHEBI:2", "label": "same", "curation_status": "SEEDED"})
               for name in ("z", "a")]
    review_records(*records)
    first = worklist.build(None, review_records=True)
    review_records(*reversed(records))
    assert worklist.build(None, review_records=True) == first
    assert [r["path"] for r in first] == sorted(r["path"] for r in first)


def test_review_cli_writes_all_pending_rows_even_with_display_limit(review_records, monkeypatch,
                                                                 tmp_path, capsys):
    extra = (REPO_ROOT / "data/natural_products/terpenoids/y.yaml",
             {"identifier": "CHEBI:2", "label": "y", "curation_status": "SEEDED"})
    review_records(rec(curation_status="SEEDED"), extra)
    target = tmp_path / "review.tsv"
    monkeypatch.setattr(sys, "argv", ["curation_worklist.py", "--review-records", "--limit", "1",
                                      "--tsv", str(target)])
    assert worklist.main() == 0
    with target.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    assert len(rows) == 2
    assert {r["identifier"] for r in rows} == {"CHEBI:1", "CHEBI:2"}
    assert "record-review  (2)" in capsys.readouterr().out


def test_review_mode_cannot_be_narrowed_to_one_queue(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["curation_worklist.py", "--review-records", "--queue",
                                      "producer-evidence"])
    with pytest.raises(SystemExit) as error:
        worklist.main()
    assert error.value.code == 2
    with pytest.raises(ValueError, match="exhaustive"):
        worklist.build("producer-evidence", review_records=True)


def test_review_recipe_enables_exhaustive_mode():
    assert "python scripts/curation_worklist.py --review-records --limit 0" in (
        REPO_ROOT / "justfile").read_text()
