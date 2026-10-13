"""The immutable review evidence and historical campaign remain recoverable."""

import gzip
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-myxochromide"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    return manifest, {r["original_path"]: r for r in manifest["artifacts"]}


def content(row):
    return gzip.decompress((ARCHIVE / row["path"]).read_bytes())


def test_integrity_and_all_snapshot_mappings():
    manifest, rows = load()
    assert len(rows) == len(manifest["artifacts"])
    paths = set()
    for row in rows.values():
        relative = PurePosixPath(row["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert relative.parts[0] == "artifacts"
        path = ARCHIVE / relative
        assert not any(p.is_symlink() for p in (path, *path.parents))
        assert path.resolve().is_relative_to(ARCHIVE.resolve())
        assert digest(path.read_bytes()) == row["stored_sha256"]
        assert path.stat().st_size == row["stored_bytes"]
        assert digest(content(row)) == row["sha256"] and len(content(row)) == row["bytes"]
        paths.add(path)
    assert paths == {p for p in (ARCHIVE / "artifacts").rglob("*") if p.is_file()}
    refs = {r["original_path"]: r for r in manifest["reference_only_sources"]}
    assert not rows.keys() & refs.keys()
    for row in refs.values():
        assert row["source_url"].startswith("https://") and "path" not in row
    missing = {r["original_path"] for r in manifest["unavailable_artifacts"]}
    assert missing == {"/private/tmp/npmech-myxochromide-resume-A59XD1/strict.tsv"}
    for review in manifest["reviews"]:
        raw = (ROOT / review["path"]).read_bytes()
        assert digest(raw) == review["sha256"]
        assert digest((ROOT / review["markdown"]).read_bytes()) == review["markdown_sha256"]
        doc = yaml.safe_load(raw)
        assert doc["source"]["git_revision"] == review["source_base"] == manifest["corpus_base"]
        temporary = {p.rstrip(".") for p in re.findall(r"/private/tmp/[A-Za-z0-9_./-]+", raw.decode())}
        assert temporary <= rows.keys() | refs.keys() | missing | set(manifest["runtime_directories"])
        snapshots = {r["evidence_id"]: r for r in review["evidence_snapshots"]}
        assert snapshots.keys() == {e["evidence_id"] for e in doc["evidence"] if "snapshot_sha256" in e}
        for ev in doc["evidence"]:
            if "snapshot_sha256" in ev:
                row = snapshots[ev["evidence_id"]]
                assert row["sha256"] == ev["snapshot_sha256"]
                assert (rows | refs)[row["original_path"]]["sha256"] == row["sha256"]
        owner = doc["targets"][0]["path"]
        original = subprocess.check_output(["git", "show", f"{review['source_base']}:{owner}"], cwd=ROOT)
        assert content(rows[owner]) == original


def test_receipts_preserve_actual_logs_and_payload_hashes():
    manifest, rows = load()
    refs = {r["original_path"]: r for r in manifest["reference_only_sources"]}
    for original, row in rows.items():
        if not original.endswith(".receipt.json"):
            continue
        receipt = json.loads(content(row))
        assert receipt["started_at"] <= receipt["finished_at"]
        if "log" in receipt:
            assert digest(content(rows[receipt["log"]])) == receipt["log_sha256"]
        elif "url" in receipt:
            payload = (rows | refs)[original.removesuffix(".receipt.json")]
            assert payload["sha256"] == receipt["sha256"] and payload["bytes"] == receipt["bytes"]


def test_historical_campaign_retains_all_unfinished_work():
    manifest, rows = load()
    checkpoint = json.loads(content(rows[manifest["checkpoint"]]))
    owners = {r["path"] for r in checkpoint["records"]}
    assert len(owners) == checkpoint["population"] == 3115
    assert sum(len(r["graph_components"]) for r in checkpoint["records"]) == 243
    reviewed = {r["path"] for r in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(reviewed) == 25 and checkpoint["partial_reviews"] == 24
    assert checkpoint["completed_scientific_reviews"] == 1
    assert len(checkpoint["all_review_observations"]) == 36
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3090
    assert reviewed.isdisjoint(pending) and reviewed | set(pending) == owners
    assert len(checkpoint["access_stops_no_alternate_retrieval"]) == 206
    assert checkpoint["findings"] == {"blocker": 8, "major": 7, "minor": 1}
    assert rows[checkpoint["prior_checkpoint"]]["sha256"] == checkpoint["prior_checkpoint_sha256"]
    for review in checkpoint["all_review_observations"]:
        assert digest((ROOT / review["yaml"]).read_bytes()) == review["yaml_sha256"]
        assert digest((ROOT / review["markdown"]).read_bytes()) == review["markdown_sha256"]
