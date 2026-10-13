"""Scoped resolutions must preserve predecessor findings and population coverage."""

import gzip
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-yersiniabactin-remediation"
PUBLICATION = ROOT / "reviews/evidence/20261013-yersiniabactin-publication"


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def checkpoint():
    manifest = json.loads((PUBLICATION / "manifest.json").read_text())
    stored = (PUBLICATION / manifest["checkpoint"]).read_bytes()
    assert digest(stored) == manifest["stored_sha256"]
    blob = gzip.decompress(stored)
    assert digest(blob) == manifest["sha256"] and len(blob) == manifest["bytes"]
    return manifest, json.loads(blob)


def test_remediation_artifacts_and_native_check_receipts():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    expected = set()
    for row in manifest["files"]:
        assert Path(row["path"]).name == row["path"]
        path = ARCHIVE / row["path"]
        assert path.is_file() and not path.is_symlink()
        assert digest(path.read_bytes()) == row["sha256"]
        assert path.stat().st_size == row["bytes"]
        expected.add(path)
    assert expected == {p for p in ARCHIVE.iterdir() if p.name != "manifest.json"}
    for path in ARCHIVE.glob("*.receipt.json"):
        receipt = json.loads(path.read_text())
        assert receipt["started_at"] <= receipt["finished_at"]
        assert digest((ARCHIVE / Path(receipt["log"]).name).read_bytes()) == receipt["log_sha256"]
    assert json.loads((ARCHIVE / "qc.receipt.json").read_text())["exit_code"] != 0
    assert json.loads((ARCHIVE / "qc-final.receipt.json").read_text())["exit_code"] == 0


def test_successors_resolve_only_supported_findings():
    manifest, state = checkpoint()
    assert len(manifest["reviews"]) == 2
    statuses = {}
    for row in manifest["reviews"]:
        raw = (ROOT / row["yaml"]).read_bytes()
        assert digest(raw) == row["yaml_sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
        review = yaml.safe_load(raw)
        assert review["completion"] == "partial" and review["scientific_review"]
        assert review["source"]["git_revision"] == state["base"]
        assert review["source"]["state"] == "working_tree"
        target, = review["targets"]
        owner = (ARCHIVE / (Path(target["path"]).stem + "-owner.yaml")).read_bytes()
        captured = next(i for i in review["source"]["inputs"] if i["path"] == target["path"])
        assert digest(owner) == captured["sha256"]
        assert yaml.safe_load(owner)["curation_status"] == "SEEDED"
        for finding in review["findings"]:
            previous, = finding["previous_occurrences"]
            old_path = ROOT / "reviews/structured" / previous["review_id"] / "review.yaml"
            old = yaml.safe_load(old_path.read_text())
            predecessor = next(f for f in old["findings"] if f["finding_id"] == previous["finding_id"])
            assert predecessor["issue_key"] == finding["issue_key"]
            assert predecessor["target_ids"] == finding["target_ids"] == [target["target_id"]]
            statuses[finding["issue_key"]] = finding["status"]
    assert statuses == {
        "yersiniabactin-BGC0001055-producer-strain": "resolved",
        "yersiniabactin-BGC0000467-producer-strain": "resolved",
        "yersiniabactin-JHYVWAMMAMCUIR-pubchem5462519-equivalence": "resolved",
        "yersiniabactin-lotus-ecoli-genomic-citation": "open",
    }


def test_full_population_and_unfinished_science_retained():
    _, state = checkpoint()
    owners = {r["path"]: r for r in state["records"]}
    partial = {r["path"] for r in state["reviews"]}
    pending = state["pending_in_priority_order"]
    assert len(owners) == state["population"] == 3115
    assert sum(len(r["graph_components"]) for r in owners.values()) == 243
    assert len(partial) == state["partial_reviews"] == 14
    assert len(pending) == len(set(pending)) == state["unassessed_records"] == 3101
    assert partial.isdisjoint(pending) and partial | set(pending) == owners.keys()
    assert set(state["partial_followups"]) == partial
    assert state["completed_scientific_reviews"] == 0
    assert state["scientific_review_bundles"] == len(state["all_review_observations"]) == 21
    assert state["findings"] == {"blocker": 4, "major": 5}
    assert len(state["new_access_stops"]) == 18
    for row in state["all_review_observations"]:
        assert digest((ROOT / row["yaml"]).read_bytes()) == row["yaml_sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
