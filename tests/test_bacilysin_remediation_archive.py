"""Retain reproducible scope and validation evidence for the bounded xref fix."""

import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-bacilysin-remediation"


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def load():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    rows = {r["original_path"]: r for r in manifest["artifacts"]}
    assert len(rows) == len(manifest["artifacts"])
    return rows


def content(row):
    return gzip.decompress((ARCHIVE / row["path"]).read_bytes())


def test_remediation_artifacts_and_receipts_are_complete():
    rows = load()
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
        if row["original_path"].endswith(".receipt.json"):
            receipt = json.loads(content(row))
            assert receipt["started_at"] <= receipt["finished_at"]
            if "log" in receipt:
                assert digest(content(rows[receipt["log"]])) == receipt["log_sha256"]
    assert actual == {p for p in (ARCHIVE / "artifacts").rglob("*") if p.is_file()}


def test_only_xrefs_discussions_and_history_changed():
    by_name = {Path(k).name: v for k, v in load().items()}
    raw = content(by_name["successor-owner.yaml"])
    after = yaml.safe_load(raw)
    assert after == json.loads(content(by_name["successor-owner.json"]))
    historical = ROOT / "reviews/evidence/20261013-bacilysin/artifacts/bacilysin-2-raw.yaml.gz"
    before_raw = gzip.decompress(historical.read_bytes())
    before = yaml.safe_load(before_raw)
    scope = json.loads(content(by_name["scope-audit.json"]))
    assert scope["population"] == 3115 and scope["components"] == 243
    assert scope["old_owner_sha256"] == digest(before_raw)
    assert scope["owner_sha256"] == digest(raw)
    assert scope["unchanged_old_reviews"] == 25
    assert before.pop("xrefs") == ["npatlas:NPA015870", "pubchem:160175"]
    assert "xrefs" not in after
    assert len(after.pop("discussions")) == 2
    assert after["curation_history"].pop()["action"] == "SEEDED_FROM_SOURCES"
    assert after == before
    assert after["curation_status"] == "SEEDED"
    capture = json.loads(content(by_name["successor-inspect.json"]))
    owner_input, = [r for r in capture["source"]["inputs"] if r["role"] == "target"]
    assert owner_input["sha256"] == digest(raw)
    assert json.loads(content(by_name["qc-final.receipt.json"]))["exit_code"] == 0
    assert b"All NaturalProductMech quality gates passed." in content(by_name["qc-final.log"])
    assert b"55 passed" in content(by_name["focused.log"])
