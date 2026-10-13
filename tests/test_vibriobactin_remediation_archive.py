"""Scoped successors preserve evidence times, lineage and campaign coverage."""

import gzip
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-vibriobactin-remediation"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_remediation_archive_and_execution_receipts():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    paths = set()
    for row in manifest["files"]:
        assert Path(row["path"]).name == row["path"]
        path = ARCHIVE / row["path"]
        assert path.is_file() and not path.is_symlink()
        assert digest(path) == row["sha256"]
        assert path.stat().st_size == row["bytes"]
        paths.add(path)
    assert paths == {p for p in ARCHIVE.iterdir() if p.name != "manifest.json"}
    for path in ARCHIVE.glob("*.receipt.json"):
        receipt = json.loads(path.read_text())
        assert receipt["exit_code"] == 0
        assert receipt["started_at"] <= receipt["finished_at"]
        assert digest(ARCHIVE / Path(receipt["log"]).name) == receipt["log_sha256"]


def test_successors_retain_exact_lineage_and_evidence_access_times():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    assert len(manifest["reviews"]) == 2
    for row in manifest["reviews"]:
        assert digest(ROOT / row["yaml"]) == row["yaml_sha256"]
        assert digest(ROOT / row["markdown"]) == row["markdown_sha256"]
        review = yaml.safe_load((ROOT / row["yaml"]).read_text())
        assert review["completion"] == "partial"
        assert review["source"]["git_revision"] == manifest["corpus_base"]
        assert review["source"]["state"] == "working_tree"
        previous, = review["related_reviews"]
        prior_path = ROOT / "reviews/structured" / previous["review_id"] / "review.yaml"
        prior = yaml.safe_load(prior_path.read_text())
        evidence = {e["evidence_id"]: e for e in review["evidence"]}
        if row["target_id"] == "CHEBI:9973":
            assert review["verdict"] == "pass_with_limitations"
            assert len(review["findings"]) == 3
            for finding, old in zip(review["findings"], prior["findings"], strict=True):
                assert finding["issue_key"] == old["issue_key"]
                assert finding["status"] == "resolved" and old["status"] == "open"
                occurrence, = finding["previous_occurrences"]
                assert occurrence["review_id"] == prior["review_id"]
                assert occurrence["finding_id"] == old["finding_id"]
            primary, = [e for e in prior["evidence"] if e["evidence_id"] == "wyckoff1999"]
            assert evidence["primary"]["accessed_at"] == primary["accessed_at"]
        else:
            assert review["verdict"] == "blocked" and review["findings"] == []
            native = evidence["native"]
            assert native["reference"].startswith("reviews/evidence/")
            assert digest(ROOT / native["reference"]) == native["snapshot_sha256"]
            assert "Not a new external retrieval" in native["locator"]
            assert any(i["path"] == native["reference"] and i["sha256"] == native["snapshot_sha256"]
                       for i in review["source"]["inputs"])
            assert any("VC_2209" in limit and "no nonproduction conclusion" in limit
                       for limit in review["limitations"])


def test_remediation_checkpoint_does_not_inflate_coverage():
    checkpoint = json.loads(gzip.decompress((ARCHIVE / "pre-merge-campaign-checkpoint.json.gz").read_bytes()))
    owners = {r["path"]: r for r in checkpoint["records"]}
    reviewed = {r["path"] for r in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(owners) == checkpoint["population"] == 3115
    assert sum(len(r["graph_components"]) for r in owners.values()) == 243
    assert len(reviewed) == checkpoint["partial_reviews"] == 12
    assert len(checkpoint["all_review_observations"]) == checkpoint["scientific_review_bundles"] == 17
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3103
    assert reviewed.isdisjoint(pending) and reviewed | set(pending) == owners.keys()
    assert checkpoint["completed_scientific_reviews"] == 0
    assert checkpoint["findings"] == {"blocker": 4, "major": 4}
    assert checkpoint["corpus_state"] == "working_tree"
    for row in checkpoint["all_review_observations"]:
        assert digest(ROOT / row["yaml"]) == row["yaml_sha256"]
        assert digest(ROOT / row["markdown"]) == row["markdown_sha256"]
    for slug in ("vibriobactin", "vibriobactin-2"):
        path = "data/natural_products/alkaloids/" + slug + ".yaml"
        assert digest(ARCHIVE / (slug + "-owner.yaml")) == owners[path]["sha256"]
    audit = json.loads((ARCHIVE / "scope-audit.json").read_text())
    assert audit["changed_owners"] == 732 and audit["changed_occurrence_notes"] == 1474
