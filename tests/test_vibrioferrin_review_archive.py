"""Published vibrioferrin reviews retain reproducible evidence and campaign scope."""

import gzip
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-vibrioferrin"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def test_archive_bytes_receipts_and_review_snapshots():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    rows = {r["original_path"]: r for r in manifest["artifacts"]}
    refs = {r["original_path"]: r for r in manifest["reference_only_sources"]}
    assert len(rows) == len(manifest["artifacts"]) and not rows.keys() & refs.keys()
    blobs, paths = {}, set()
    for original, row in rows.items():
        relative = PurePosixPath(row["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert relative.parts[0] == "artifacts"
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
        if original.endswith(".receipt.json"):
            receipt = json.loads(raw)
            assert receipt["started_at"] <= receipt["finished_at"]
            if "log" in receipt:
                assert (rows | refs)[receipt["log"]]["sha256"] == receipt["log_sha256"]
            elif "url" in receipt:
                payload = (rows | refs)[original.removesuffix(".receipt.json")]
                assert payload["sha256"] == receipt["sha256"] and payload["bytes"] == receipt["bytes"]
    for review in manifest["reviews"]:
        raw = (ROOT / review["path"]).read_bytes()
        assert digest(raw) == review["sha256"]
        assert digest((ROOT / review["markdown"]).read_bytes()) == review["markdown_sha256"]
        doc = yaml.safe_load(raw)
        temporary = {p.rstrip(".") for p in re.findall(r"/private/tmp/[A-Za-z0-9_./-]+", raw.decode())}
        assert temporary <= rows.keys() | refs.keys() | set(manifest["runtime_directories"])
        snapshots = {r["evidence_id"]: r for r in review["evidence_snapshots"]}
        assert snapshots.keys() == {e["evidence_id"] for e in doc["evidence"] if "snapshot_sha256" in e}
        for ev in doc["evidence"]:
            if "snapshot_sha256" in ev:
                snapshot = snapshots[ev["evidence_id"]]
                assert snapshot["sha256"] == ev["snapshot_sha256"]
                assert (rows | refs)[snapshot["original_path"]]["sha256"] == snapshot["sha256"]
        owner = doc["targets"][0]["path"]
        original = subprocess.check_output(["git", "show", f"{review['source_base']}:{owner}"], cwd=ROOT)
        assert blobs[owner] == original
    checkpoint = json.loads(blobs[manifest["checkpoint"]])
    owners = {r["path"] for r in checkpoint["records"]}
    reviewed = {r["path"] for r in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(owners) == checkpoint["population"] == 3115
    assert sum(len(r["graph_components"]) for r in checkpoint["records"]) == 243
    assert len(reviewed) == 27 and checkpoint["partial_reviews"] == 26
    assert checkpoint["completed_scientific_reviews"] == 1
    assert len(checkpoint["all_review_observations"]) == 40
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3088
    assert reviewed.isdisjoint(pending) and reviewed | set(pending) == owners
    assert len(checkpoint["access_stops_no_alternate_retrieval"]) == 218
    assert checkpoint["findings"] == {"blocker": 9, "major": 9, "minor": 3}
    assert rows[checkpoint["prior_checkpoint"]]["sha256"] == checkpoint["prior_checkpoint_sha256"]
    for review in checkpoint["all_review_observations"]:
        assert digest((ROOT / review["yaml"]).read_bytes()) == review["yaml_sha256"]
        assert digest((ROOT / review["markdown"]).read_bytes()) == review["markdown_sha256"]
