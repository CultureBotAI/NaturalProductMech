"""Remediation receipts and finding lineage remain independently checkable."""

import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-compound3-remediation"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def test_remediation_receipts_and_scoped_dispositions():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    artifacts = {}
    paths = set()
    for row in manifest["artifacts"]:
        relative = PurePosixPath(row["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert relative.parts[0] == "artifacts"
        path = ARCHIVE / relative
        assert not any(p.is_symlink() for p in (path, *path.parents))
        assert path.resolve().is_relative_to(ARCHIVE.resolve())
        raw = path.read_bytes()
        assert len(raw) == row["stored_bytes"] and digest(raw) == row["stored_sha256"]
        unpacked = gzip.decompress(raw)
        assert len(unpacked) == row["bytes"] and digest(unpacked) == row["sha256"]
        assert row["original_path"] not in artifacts
        artifacts[row["original_path"]] = unpacked
        paths.add(path)
    assert paths == {p for p in (ARCHIVE / "artifacts").rglob("*") if p.is_file()}
    for path, raw in artifacts.items():
        if path.endswith(".receipt.json"):
            receipt = json.loads(raw)
            assert receipt["started_at"] <= receipt["finished_at"]
            if "log" in receipt:
                assert digest(artifacts[receipt["log"]]) == receipt["log_sha256"]
    scope, = [json.loads(raw) for path, raw in artifacts.items() if path.endswith("/scope-audit.json")]
    assert scope["owners"] == 3115 and scope["components"] == 243
    assert scope["unchanged_owners"] == 3114 and scope["immutable_prior_observations"] == 29
    qc, = [json.loads(raw) for path, raw in artifacts.items() if path.endswith("/qc.receipt.json")]
    assert qc["exit_code"] == 0
    assert "745 passed, 4 skipped" in artifacts[qc["log"]].decode()
    path = ROOT / "reviews/structured" / manifest["review_id"] / "review.yaml"
    review = yaml.safe_load(path.read_text())
    assert review["source"]["git_revision"] == manifest["source_revision"]
    assert review["completion"] == "partial" and review["verdict"] == "pass_with_limitations"
    assert {f["finding_id"] for f in review["findings"]} == {"F1", "F2"}
    for finding in review["findings"]:
        assert finding["status"] == "resolved"
        assert finding["previous_occurrences"] == [{
            "repository": "CultureBotAI/NaturalProductMech",
            "review_id": "20261013T152822Z-compound-3",
            "finding_id": finding["finding_id"],
        }]
