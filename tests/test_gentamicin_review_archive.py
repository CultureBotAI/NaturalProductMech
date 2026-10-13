"""Saved gentamicin evidence and dispositions preserve provenance and scope."""

import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-gentamicin"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def test_gentamicin_archive_and_scoped_dispositions():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    rows = {r["original_path"]: r for r in manifest["artifacts"]}
    refs = {r["original_path"]: r for r in manifest["reference_only_sources"]}
    assert len(rows) == len(manifest["artifacts"]) and not rows.keys() & refs.keys()
    blobs, paths = {}, set()
    for original, row in rows.items():
        relative = PurePosixPath(row["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert relative.parts[0] == "artifacts"
        assert not any(c in relative.name for c in '<>:"\\|?*')
        path = ARCHIVE / relative
        assert not any(p.is_symlink() for p in (path, *path.parents))
        assert path.resolve().is_relative_to(ARCHIVE.resolve())
        stored = path.read_bytes()
        raw = gzip.decompress(stored)
        assert digest(stored) == row["stored_sha256"] and len(stored) == row["stored_bytes"]
        assert digest(raw) == row["sha256"] and len(raw) == row["bytes"]
        blobs[original] = raw
        paths.add(path)
    assert paths == {p for p in (ARCHIVE / "artifacts").rglob("*") if p.is_file()}
    for row in refs.values():
        assert row["source_url"].startswith("https://") and "path" not in row
    for original, raw in blobs.items():
        if not original.endswith(".receipt.json"):
            continue
        receipt = json.loads(raw)
        assert receipt["started_at"] <= receipt["finished_at"]
        if "log" in receipt:
            assert (rows | refs)[receipt["log"]]["sha256"] == receipt["log_sha256"]
        elif "url" in receipt:
            payload = (rows | refs)[original.removesuffix(".receipt.json")]
            assert payload["sha256"] == receipt["sha256"] and payload["bytes"] == receipt["bytes"]
    assert len(manifest["reviews"]) == 4
    for row in manifest["reviews"]:
        raw = (ROOT / row["path"]).read_bytes()
        assert digest(raw) == row["sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
        review = yaml.safe_load(raw)
        assert review["completion"] == "partial" and review["verdict"] == "needs_curation"
        snapshots = {e["evidence_id"]: e for e in row["evidence_snapshots"]}
        assert snapshots.keys() == {e["evidence_id"] for e in review["evidence"] if "snapshot_sha256" in e}
        for ev in review["evidence"]:
            if "snapshot_sha256" in ev:
                snapshot = snapshots[ev["evidence_id"]]
                assert ev["snapshot_sha256"] == snapshot["sha256"]
                assert (rows | refs)[snapshot["original_path"]]["sha256"] == snapshot["sha256"]
        if "scoped-disposition" in review["review_id"]:
            for finding in review["findings"]:
                assert len(finding["previous_occurrences"]) == 1
                previous = finding["previous_occurrences"][0]
                assert previous["repository"] == "CultureBotAI/NaturalProductMech"
                original_path = ROOT / "reviews/structured" / previous["review_id"] / "review.yaml"
                original = yaml.safe_load(original_path.read_text())
                prior, = [f for f in original["findings"] if f["finding_id"] == previous["finding_id"]]
                assert finding["issue_key"] == prior["issue_key"]
                assert finding["target_ids"] == prior["target_ids"]
                assert finding["status"] == ("open" if finding["finding_id"] == "F1" else "resolved")
    checkpoint = json.loads(blobs[manifest["checkpoint"]])
    prior = json.loads(blobs[checkpoint["prior_checkpoint"]])
    assert rows[checkpoint["prior_checkpoint"]]["sha256"] == checkpoint["prior_checkpoint_sha256"]
    assert (checkpoint["access_stops_no_alternate_retrieval"][:234]
            == prior["access_stops_no_alternate_retrieval"])
    assert len(checkpoint["all_review_observations"]) == 52
    assert len(checkpoint["reviews"]) == 32 and checkpoint["partial_reviews"] == 31
    assert checkpoint["completed_scientific_reviews"] == 1
    assert checkpoint["findings"] == {"blocker": 13, "major": 8, "minor": 1}
    owners = {r["path"] for r in checkpoint["records"]}
    assessed = {r["path"] for r in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(owners) == checkpoint["population"] == 3115
    assert sum(len(r["graph_components"]) for r in checkpoint["records"]) == 243
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3083
    assert assessed.isdisjoint(pending) and assessed | set(pending) == owners
    assert checkpoint["unpublished_research_handoff"]["saved_reviews"] == 0
    for row in checkpoint["all_review_observations"]:
        assert digest((ROOT / row["yaml"]).read_bytes()) == row["yaml_sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
    if "final_qc" in manifest:
        qc = json.loads(blobs[manifest["final_qc"]])
        assert qc["exit_code"] == 0
        assert "All NaturalProductMech quality gates passed." in blobs[qc["log"]].decode()
