"""Scoped ferrichrome dispositions retain evidence and do not close identity."""

import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-ferrichrome-remediation"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def test_remediation_integrity_and_scoped_finding_lineage():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    upstream_path = ROOT / manifest["upstream_manifest"]
    assert digest(upstream_path.read_bytes()) == manifest["upstream_sha256"]
    upstream = json.loads(upstream_path.read_text())
    upstream_rows = {r["original_path"]: r
                     for r in upstream["artifacts"] + upstream["reference_only_sources"]}
    artifacts, rows, paths = {}, {}, set()
    for row in manifest["artifacts"]:
        relative = PurePosixPath(row["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert relative.parts[0] == "artifacts"
        path = ARCHIVE / relative
        assert not any(p.is_symlink() for p in (path, *path.parents))
        assert path.resolve().is_relative_to(ARCHIVE.resolve())
        stored = path.read_bytes()
        raw = gzip.decompress(stored)
        assert len(stored) == row["stored_bytes"] and digest(stored) == row["stored_sha256"]
        assert len(raw) == row["bytes"] and digest(raw) == row["sha256"]
        assert row["original_path"] not in artifacts
        artifacts[row["original_path"]] = raw
        rows[row["original_path"]] = row
        paths.add(path)
    assert paths == {p for p in (ARCHIVE / "artifacts").rglob("*") if p.is_file()}
    for original, raw in artifacts.items():
        if original.endswith(".receipt.json"):
            receipt = json.loads(raw)
            assert receipt["started_at"] <= receipt["finished_at"]
            if "log" in receipt:
                assert digest(artifacts[receipt["log"]]) == receipt["log_sha256"]
    qc, = [json.loads(raw) for path, raw in artifacts.items() if path.endswith("/qc-final.receipt.json")]
    assert qc["exit_code"] == 0
    assert "All NaturalProductMech quality gates passed." in artifacts[qc["log"]].decode()
    scope, = [json.loads(raw) for path, raw in artifacts.items() if path.endswith("/scope-audit.json")]
    assert scope["owners"] == 3115 and scope["components"] == 243
    assert scope["unchanged_owners"] == 3113 and scope["immutable_prior_observations"] == 32
    assert len(manifest["reviews"]) == 2
    for row in manifest["reviews"]:
        raw = (ROOT / row["path"]).read_bytes()
        assert digest(raw) == row["sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
        review = yaml.safe_load(raw)
        assert review["source"]["git_revision"] == row["source_base"]
        assert review["completion"] == "partial"
        snapshots = {r["evidence_id"]: r for r in row["evidence_snapshots"]}
        assert snapshots.keys() == {e["evidence_id"] for e in review["evidence"] if "snapshot_sha256" in e}
        for evidence in review["evidence"]:
            if "snapshot_sha256" in evidence:
                snapshot = snapshots[evidence["evidence_id"]]
                source = rows if snapshot["archive"] == "current" else upstream_rows
                assert snapshot["sha256"] == evidence["snapshot_sha256"]
                assert source[snapshot["original_path"]]["sha256"] == snapshot["sha256"]
        c26 = review["targets"][0]["target_id"] == "naturalproductmech:mibig-ab69cdf6e5"
        prior = "20261013T170121Z-ferrichrome-2" if c26 else "20261013T170122Z-ferrichrome"
        for finding in review["findings"]:
            assert finding["status"] == ("open" if c26 and finding["finding_id"] == "F1" else "resolved")
            assert finding["previous_occurrences"] == [{
                "repository": "CultureBotAI/NaturalProductMech", "review_id": prior,
                "finding_id": finding["finding_id"],
            }]
        assert review["verdict"] == ("needs_curation" if c26 else "pass_with_limitations")
