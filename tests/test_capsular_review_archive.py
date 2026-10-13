"""Capsule review captures and campaign coverage remain independently checkable."""

import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-capsular"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def test_archive_receipts_snapshots_and_campaign_scope():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    rows = {r["original_path"]: r for r in manifest["artifacts"]}
    refs = {r["original_path"]: r for r in manifest["reference_only_sources"]}
    assert len(rows) == len(manifest["artifacts"]) and not rows.keys() & refs.keys()
    blobs, paths = {}, set()
    for original, r in rows.items():
        relative = PurePosixPath(r["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert relative.parts[0] == "artifacts"
        path = ARCHIVE / relative
        assert not any(p.is_symlink() for p in (path, *path.parents))
        assert path.resolve().is_relative_to(ARCHIVE.resolve())
        stored = path.read_bytes()
        raw = gzip.decompress(stored)
        assert digest(stored) == r["stored_sha256"] and len(stored) == r["stored_bytes"]
        assert digest(raw) == r["sha256"] and len(raw) == r["bytes"]
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
    assert len(manifest["reviews"]) == 6
    for row in manifest["reviews"]:
        raw = (ROOT / row["path"]).read_bytes()
        assert digest(raw) == row["sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
        doc = yaml.safe_load(raw)
        snapshots = {e["evidence_id"]: e for e in row["evidence_snapshots"]}
        assert snapshots.keys() == {e["evidence_id"] for e in doc["evidence"] if "snapshot_sha256" in e}
        for ev in doc["evidence"]:
            if "snapshot_sha256" in ev:
                item = snapshots[ev["evidence_id"]]
                assert ev["snapshot_sha256"] == item["sha256"]
                assert (rows | refs)[item["original_path"]]["sha256"] == item["sha256"]
    checkpoint = json.loads(blobs[manifest["checkpoint"]])
    owners = {r["path"] for r in checkpoint["records"]}
    assessed = {r["path"] for r in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(owners) == checkpoint["population"] == 3115
    assert sum(len(r["graph_components"]) for r in checkpoint["records"]) == 243
    assert len(assessed) == 30 and checkpoint["partial_reviews"] == 29
    assert checkpoint["completed_scientific_reviews"] == 1
    assert len(checkpoint["all_review_observations"]) == 48
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3085
    assert assessed.isdisjoint(pending) and assessed | set(pending) == owners
    prior = json.loads(blobs[checkpoint["prior_checkpoint"]])
    assert (checkpoint["access_stops_no_alternate_retrieval"][:224]
            == prior["access_stops_no_alternate_retrieval"])
    assert checkpoint["findings"] == {"blocker": 12, "major": 7, "minor": 1}
    assert rows[checkpoint["prior_checkpoint"]]["sha256"] == checkpoint["prior_checkpoint_sha256"]
    for row in checkpoint["all_review_observations"]:
        assert digest((ROOT / row["yaml"]).read_bytes()) == row["yaml_sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
