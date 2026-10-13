"""Vibriobactin review evidence must survive removal of its temporary workspace."""

import gzip
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-vibriobactin"


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def load():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    rows = {row["original_path"]: row for row in manifest["artifacts"]}
    assert len(rows) == len(manifest["artifacts"])
    return manifest, rows


def content(row):
    return gzip.decompress((ARCHIVE / row["path"]).read_bytes())


def test_archive_integrity_paths_and_review_references():
    manifest, rows = load()
    files = set()
    for row in rows.values():
        relative = PurePosixPath(row["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert relative.parts[0] == "artifacts"
        path = ARCHIVE / relative
        assert not any(p.is_symlink() for p in (path, *path.parents))
        assert path.resolve().is_relative_to(ARCHIVE.resolve())
        assert row["encoding"] == "gzip"
        assert digest(path.read_bytes()) == row["stored_sha256"]
        assert path.stat().st_size == row["stored_bytes"]
        assert digest(content(row)) == row["sha256"]
        assert len(content(row)) == row["bytes"]
        files.add(path)
    assert files == {p for p in (ARCHIVE / "artifacts").rglob("*") if p.is_file()}
    assert len(manifest["reviews"]) == 2
    for row in manifest["reviews"]:
        blob = (ROOT / row["path"]).read_bytes()
        assert digest(blob) == row["sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
        review = yaml.safe_load(blob)
        assert review["completion"] == "partial" and review["scientific_review"]
        references = {p.rstrip(".") for p in re.findall(r"/private/tmp/[A-Za-z0-9_./-]+", blob.decode())}
        assert references <= rows.keys() | set(manifest["runtime_directories"])


def test_receipts_and_protein_source_pins_are_retrievable():
    manifest, rows = load()
    failed = set()
    for original, row in rows.items():
        if original.endswith(".receipt.json"):
            receipt = json.loads(content(row))
            assert receipt["command"] and receipt["started_at"] <= receipt["finished_at"]
            log = receipt.get("log", original.removesuffix(".receipt.json") + ".json")
            assert digest(content(rows[log])) == receipt["log_sha256"]
            if receipt["exit_code"]:
                failed.add(Path(original).name)
    assert failed == {"chemistry.receipt.json", "validate-vibriobactin.receipt.json",
                      "validate-vibriobactin-2.receipt.json", "validate-final-vibriobactin.receipt.json",
                      "validate-final-vibriobactin-2.receipt.json"}
    proteins = json.loads(content(rows[manifest["source_workspace"] + "/proteins-current.json"]))
    assert len(proteins["proteins"]) == 11
    for path, sha in proteins["source_pins"].items():
        assert digest(content(rows[path])) == sha


def test_full_population_checkpoint_and_access_stops_are_preserved():
    manifest, rows = load()
    checkpoint = json.loads(content(rows[manifest["checkpoint"]]))
    owners = {row["path"]: row for row in checkpoint["records"]}
    assert len(owners) == checkpoint["population"] == 3115
    assert sum(len(row["graph_components"]) for row in owners.values()) == 243
    reviewed = {row["path"] for row in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(reviewed) == checkpoint["partial_reviews"] == 12
    assert len(checkpoint["all_review_observations"]) == 15
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3103
    assert reviewed.isdisjoint(pending) and reviewed | set(pending) == owners.keys()
    assert checkpoint["completed_scientific_reviews"] == 0
    assert checkpoint["findings"] == {"blocker": 4, "major": 5, "minor": 2}
    assert rows[checkpoint["prior_checkpoint"]]["sha256"] == checkpoint["prior_checkpoint_sha256"]
    inherited = checkpoint["inherited_scientific_access_stops"]
    assert rows[inherited["checkpoint"]]["sha256"] == inherited["sha256"]
    assert len(json.loads(content(rows[inherited["checkpoint"]]))[
        "access_stops_no_alternate_retrieval"]) == 162
    for row in checkpoint["all_review_observations"]:
        assert digest((ROOT / row["yaml"]).read_bytes()) == row["yaml_sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
