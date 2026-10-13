"""Published partial observations remain auditable without temporary workspaces."""

import gzip
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-yersiniabactin"


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def load():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    rows = {r["original_path"]: r for r in manifest["artifacts"]}
    assert len(rows) == len(manifest["artifacts"])
    return manifest, rows


def content(row):
    return gzip.decompress((ARCHIVE / row["path"]).read_bytes())


def test_archive_integrity_and_review_references():
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
    reference_only = {r["original_path"] for r in manifest["reference_only_sources"]}
    assert not rows.keys() & reference_only
    for row in manifest["reference_only_sources"]:
        assert row["source_url"].startswith("https://") and "path" not in row
    for row in manifest["reviews"]:
        blob = (ROOT / row["path"]).read_bytes()
        assert digest(blob) == row["sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
        doc = yaml.safe_load(blob)
        assert doc["completion"] == "partial" and doc["verdict"] == "needs_curation"
        assert doc["source"]["git_revision"] == manifest["corpus_base"]
        references = {p.rstrip(".") for p in re.findall(r"/private/tmp/[A-Za-z0-9_./-]+", blob.decode())}
        assert references <= rows.keys() | reference_only | set(manifest["runtime_directories"])


def test_checks_include_failures_and_exact_logs():
    _, rows = load()
    failed = set()
    for original, row in rows.items():
        if original.endswith(".receipt.json"):
            receipt = json.loads(content(row))
            assert receipt["command"] and receipt["started_at"] <= receipt["finished_at"]
            log = receipt.get("log", original.removesuffix(".receipt.json") + ".json")
            assert digest(content(rows[log])) == receipt["log_sha256"]
            if receipt["exit_code"]:
                failed.add(Path(original).name)
    assert failed == {"strict-1.receipt.json", "strict-2.receipt.json", "chemistry.receipt.json",
                      "review-validate.receipt.json", "review-validate-final.receipt.json",
                      "review-validate-ready.receipt.json"}


def test_full_historical_population_and_restrictions():
    manifest, rows = load()
    checkpoint = json.loads(content(rows[manifest["checkpoint"]]))
    owners = {r["path"]: r for r in checkpoint["records"]}
    assert len(owners) == checkpoint["population"] == 3115
    assert sum(len(r["graph_components"]) for r in owners.values()) == 243
    reviewed = {r["path"] for r in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(reviewed) == checkpoint["partial_reviews"] == 14
    assert len(checkpoint["all_review_observations"]) == 19
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3101
    assert reviewed.isdisjoint(pending) and reviewed | set(pending) == owners.keys()
    assert set(checkpoint["partial_followups"]) == reviewed
    assert checkpoint["completed_scientific_reviews"] == 0
    assert checkpoint["findings"] == {"blocker": 4, "major": 6, "minor": 2}
    assert rows[checkpoint["prior_checkpoint"]]["sha256"] == checkpoint["prior_checkpoint_sha256"]
    inherited = checkpoint["inherited_scientific_access_stops"]
    assert rows[inherited["checkpoint"]]["sha256"] == inherited["sha256"]
    assert len(json.loads(content(rows[inherited["checkpoint"]]))[
        "access_stops_no_alternate_retrieval"]) == 162
    assert len(checkpoint["new_access_stops"]) == 18
    for row in checkpoint["all_review_observations"]:
        assert digest((ROOT / row["yaml"]).read_bytes()) == row["yaml_sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
