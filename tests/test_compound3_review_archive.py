"""Compound 3 publication retains evidence provenance and full campaign scope."""

import gzip
import hashlib
import json
import re
import shlex
import subprocess
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-compound3"


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def load():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    rows = {r["original_path"]: r for r in manifest["artifacts"]}
    assert len(rows) == len(manifest["artifacts"])
    return manifest, rows


def content(row):
    return gzip.decompress((ARCHIVE / row["path"]).read_bytes())


def test_integrity_and_complete_evidence_snapshot_mapping():
    manifest, rows = load()
    actual = set()
    for row in rows.values():
        relative = PurePosixPath(row["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert relative.parts[0] == "artifacts"
        path = ARCHIVE / relative
        assert not any(p.is_symlink() for p in (path, *path.parents))
        assert path.resolve().is_relative_to(ARCHIVE.resolve())
        assert digest(path.read_bytes()) == row["stored_sha256"]
        assert path.stat().st_size == row["stored_bytes"]
        assert digest(content(row)) == row["sha256"]
        assert len(content(row)) == row["bytes"]
        actual.add(path)
    assert actual == {p for p in (ARCHIVE / "artifacts").rglob("*") if p.is_file()}
    references = {r["original_path"]: r for r in manifest["reference_only_sources"]}
    assert len(references) == 11 and not rows.keys() & references.keys()
    for row in references.values():
        assert row["source_url"].startswith("https://") and "path" not in row
    assert len(manifest["reviews"]) == 3
    for row in manifest["reviews"]:
        blob = (ROOT / row["path"]).read_bytes()
        assert digest(blob) == row["sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
        doc = yaml.safe_load(blob)
        assert doc["source"]["git_revision"] == row["source_base"] == manifest["corpus_base"]
        paths = {p.rstrip(".") for p in re.findall(r"/private/tmp/[A-Za-z0-9_./-]+", blob.decode())}
        assert paths <= rows.keys() | references.keys() | set(manifest["runtime_directories"])
        snapshots = {r["evidence_id"]: r for r in row["evidence_snapshots"]}
        assert len(snapshots) == len(row["evidence_snapshots"])
        assert snapshots.keys() == {e["evidence_id"] for e in doc["evidence"] if "snapshot_sha256" in e}
        for evidence in doc["evidence"]:
            if "snapshot_sha256" in evidence:
                snapshot = snapshots[evidence["evidence_id"]]
                assert snapshot["sha256"] == evidence["snapshot_sha256"]
                assert (rows | references)[snapshot["original_path"]]["sha256"] == snapshot["sha256"]
        owner = doc["targets"][0]["path"]
        raw = subprocess.check_output(["git", "show", f"{row['source_base']}:{owner}"], cwd=ROOT)
        assert content(rows[owner]) == raw
        assert snapshots["owner"]["sha256"] == digest(raw)
        resolved = json.loads(content(rows[snapshots["resolved"]["original_path"]]))
        assert resolved == yaml.safe_load(raw)
        work = Path(snapshots["resolved"]["original_path"]).parent
        for check in doc["checks"]:
            if "exit_code" in check:
                receipt = json.loads(content(rows[str(work / (check["check_id"] + ".receipt.json"))]))
                assert receipt["exit_code"] == check["exit_code"]
                assert shlex.join(receipt["command"]) == check["command"]


def test_receipts_logs_and_reference_only_digests():
    manifest, rows = load()
    references = {r["original_path"]: r for r in manifest["reference_only_sources"]}
    for original, row in rows.items():
        if not original.endswith(".receipt.json"):
            continue
        receipt = json.loads(content(row))
        assert receipt["started_at"] <= receipt["finished_at"]
        if "command" in receipt:
            assert digest(content(rows[receipt["log"]])) == receipt["log_sha256"]
        else:
            snapshot = (rows | references)[original.removesuffix(".receipt.json")]
            assert snapshot["sha256"] == receipt["sha256"]
            assert snapshot["bytes"] == receipt["bytes"]


def test_historical_campaign_preserves_population_and_limits():
    manifest, rows = load()
    checkpoint = json.loads(content(rows[manifest["checkpoint"]]))
    owners = {r["path"]: r for r in checkpoint["records"]}
    assert len(owners) == checkpoint["population"] == 3115
    assert sum(len(r["graph_components"]) for r in owners.values()) == 243
    reviewed = {r["path"] for r in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(reviewed) == 21
    assert checkpoint["partial_reviews"] == 20
    assert checkpoint["completed_scientific_reviews"] == 1
    assert len(checkpoint["all_review_observations"]) == 29
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3094
    assert reviewed.isdisjoint(pending) and reviewed | set(pending) == owners.keys()
    assert len(checkpoint["access_stops_no_alternate_retrieval"]) == 195
    assert checkpoint["findings"] == {"blocker": 6, "major": 7, "minor": 1}
    assert rows[checkpoint["prior_checkpoint"]]["sha256"] == checkpoint["prior_checkpoint_sha256"]
    inherited = checkpoint["inherited_scientific_access_stops"]
    assert rows[inherited["checkpoint"]]["sha256"] == inherited["sha256"]
    for row in checkpoint["all_review_observations"]:
        assert digest((ROOT / row["yaml"]).read_bytes()) == row["yaml_sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
