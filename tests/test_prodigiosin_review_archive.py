"""The prodigiosin checkpoint remains auditable without its capture workspace."""

import gzip
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-prodigiosin"


def load_archive():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    artifacts = {r["original_path"]: r for r in manifest["artifacts"]}
    assert len(artifacts) == len(manifest["artifacts"])
    return manifest, artifacts


def content(row):
    blob = (ARCHIVE / row["path"]).read_bytes()
    return gzip.decompress(blob) if row.get("encoding") == "gzip" else blob


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def test_archive_integrity_and_no_unlisted_files():
    manifest, artifacts = load_archive()
    actual = set()
    for row in artifacts.values():
        path = PurePosixPath(row["path"])
        assert not path.is_absolute() and ".." not in path.parts
        assert path.parts[0] == "artifacts"
        stored = ARCHIVE / path
        assert not any(p.is_symlink() for p in (stored, *stored.parents))
        assert stored.resolve().is_relative_to(ARCHIVE.resolve())
        assert digest(stored.read_bytes()) == row.get("stored_sha256", row["sha256"])
        assert stored.stat().st_size == row.get("stored_bytes", row["bytes"])
        assert digest(content(row)) == row["sha256"]
        assert len(content(row)) == row["bytes"]
        actual.add(stored)
    assert actual == {p for p in (ARCHIVE / "artifacts").rglob("*") if p.is_file()}
    assert len(manifest["reference_only_sources"]) == 7
    assert not artifacts.keys() & {r["original_path"] for r in manifest["reference_only_sources"]}
    for row in manifest["reference_only_sources"]:
        assert row["source_url"].startswith("https://")
        assert "path" not in row


def test_receipts_preserve_failed_attempts_and_output_hashes():
    _, artifacts = load_archive()
    failed = set()
    for path, row in artifacts.items():
        if not path.endswith(".receipt.json"):
            continue
        receipt = json.loads(content(row))
        assert receipt["command"] and receipt["started_at"] <= receipt["finished_at"]
        log = receipt.get("log", path.removesuffix(".receipt.json") + ".json")
        assert digest(content(artifacts[log])) == receipt["log_sha256"]
        if receipt["exit_code"]:
            failed.add(Path(path).name)
    assert failed == {
        "20261013T085526Z-prodigiosin-2-validate.receipt.json",
        "20261013T085600Z-prodigiosin-validate.receipt.json",
        "mibig-258.receipt.json", "pinned-chemistry.receipt.json", "qc.receipt.json",
        "strict-prodigiosin-2-retry.receipt.json", "strict-prodigiosin-2.receipt.json",
        "strict-prodigiosin-retry.receipt.json", "strict-prodigiosin.receipt.json",
    }


def test_observations_and_full_historical_population():
    manifest, artifacts = load_archive()
    checkpoint_row = next(r for r in artifacts.values() if r["path"] == manifest["checkpoint"])
    checkpoint = json.loads(content(checkpoint_row))
    owners = {r["path"]: r for r in checkpoint["records"]}
    components = {c["path"]: c for r in owners.values() for c in r["graph_components"]}
    assert len(owners) == checkpoint["population"] == 3115
    assert len(components) == checkpoint["graph_components"] == 243
    assert len(checkpoint["reviews"]) == checkpoint["partial_reviews"] == 10
    assert len(checkpoint["all_review_observations"]) == checkpoint["scientific_review_bundles"] == 11
    assert checkpoint["completed_scientific_reviews"] == 0
    pending = checkpoint["pending_in_priority_order"]
    reviewed = {r["path"] for r in checkpoint["reviews"]}
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3105
    assert reviewed.isdisjoint(pending) and reviewed | set(pending) == owners.keys()
    assert {p for p, r in owners.items() if r["review_state"] == "partial"} == reviewed
    assert {p for p, r in owners.items() if r["review_state"] == "unassessed"} == set(pending)
    assert set(checkpoint["partial_followups"]) == reviewed
    assert checkpoint["findings"] == {"blocker": 4, "major": 4, "minor": 2}
    assert checkpoint["goal_status"] == "active"
    assert len(checkpoint["new_access_stops"]) == 7
    inherited = checkpoint["inherited_scientific_access_stops"]
    stops = artifacts[inherited["checkpoint"]]
    assert stops["sha256"] == inherited["sha256"]
    assert len(json.loads(content(stops))["access_stops_no_alternate_retrieval"]) == 162
    assert artifacts[checkpoint["prior_checkpoint"]]["sha256"] == checkpoint["prior_checkpoint_sha256"]
    expected = owners | components
    base = manifest["corpus_base"]
    tracked = subprocess.check_output([
        "git", "ls-tree", "-r", "--name-only", base, "--",
        "data/natural_products", "data/causal_graphs",
    ], cwd=ROOT, text=True).splitlines()
    assert {p for p in tracked if p.endswith(".yaml")} == expected.keys()
    output = subprocess.check_output(["git", "cat-file", "--batch"], cwd=ROOT,
                                     input="".join(f"{base}:{p}\n" for p in expected).encode())
    offset = 0
    for row in expected.values():
        end = output.index(b"\n", offset)
        _, kind, size = output[offset:end].split()
        assert kind == b"blob"
        offset = end + 1
        assert digest(output[offset:offset + int(size)]) == row["sha256"]
        offset += int(size) + 1
    assert offset == len(output)
    for row in checkpoint["all_review_observations"]:
        assert digest((ROOT / row["yaml"]).read_bytes()) == row["yaml_sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]


def test_published_review_artifacts_have_durable_mappings():
    manifest, artifacts = load_archive()
    reference_only = {r["original_path"] for r in manifest["reference_only_sources"]}
    for row in manifest["reviews"]:
        body = (ROOT / row["path"]).read_bytes()
        assert digest(body) == row["sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
        review = yaml.safe_load(body)
        assert review["source"]["git_revision"] == manifest["corpus_base"]
        assert review["completion"] == "partial" and review["verdict"] == "needs_curation"
        references = {p.rstrip(".") for p in re.findall(r"/private/tmp/[A-Za-z0-9_./-]+", body.decode())}
        references -= {manifest["source_workspace"], manifest["source_workspace"] + "/uv-cache"}
        assert references <= artifacts.keys() | reference_only


def test_strain_resolution_archive_and_campaign_lineage():
    archive = ROOT / "reviews/evidence/20261013-prodigiosin-remediation"
    manifest = json.loads((archive / "manifest.json").read_text())
    paths = set()
    for row in manifest["files"]:
        assert Path(row["path"]).name == row["path"]
        path = archive / row["path"]
        assert path.is_file() and not path.is_symlink()
        assert digest(path.read_bytes()) == row["sha256"]
        assert path.stat().st_size == row["bytes"]
        paths.add(path)
    assert paths == {p for p in archive.iterdir() if p.name != "manifest.json"}
    for path in archive.glob("*.receipt.json"):
        receipt = json.loads(path.read_text())
        assert digest((archive / Path(receipt["log"]).name).read_bytes()) == receipt["log_sha256"]
        assert receipt["started_at"] <= receipt["finished_at"]
    checkpoint = json.loads(gzip.decompress((archive / "pre-merge-campaign-checkpoint.json.gz").read_bytes()))
    assert checkpoint["corpus_state"] == "working_tree"
    assert checkpoint["scientific_review_bundles"] == len(checkpoint["all_review_observations"]) == 13
    assert checkpoint["partial_reviews"] == len(checkpoint["reviews"]) == 10
    assert checkpoint["unassessed_records"] == len(checkpoint["pending_in_priority_order"]) == 3105
    assert checkpoint["completed_scientific_reviews"] == 0
    assert checkpoint["findings"] == {"blocker": 4, "major": 4}
    assert checkpoint["goal_status"] == "active"
    owners = {r["path"]: r for r in checkpoint["records"]}
    reviewed = {r["path"] for r in checkpoint["reviews"]}
    pending = set(checkpoint["pending_in_priority_order"])
    assert len(owners) == 3115 and reviewed.isdisjoint(pending)
    assert reviewed | pending == owners.keys()
    assert {p for p, r in owners.items() if r["review_state"] == "partial"} == reviewed
    assert {p for p, r in owners.items() if r["review_state"] == "unassessed"} == pending
    assert len(manifest["reviews"]) == 2
    for row in manifest["reviews"]:
        path = ROOT / row["path"]
        assert digest(path.read_bytes()) == row["sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
        review = yaml.safe_load(path.read_text())
        assert review["completion"] == "partial" and review["verdict"] == "pass_with_limitations"
        assert review["source"]["git_revision"] == manifest["corpus_base"]
        assert review["source"]["state"] == "working_tree"
        finding, = review["findings"]
        assert finding["finding_id"] == "F2" and finding["status"] == "resolved"
        previous, = finding["previous_occurrences"]
        assert previous["finding_id"] == "F2"
        previous_path = ROOT / "reviews/structured" / previous["review_id"] / "review.yaml"
        prior = yaml.safe_load(previous_path.read_text())
        assert prior["findings"][0]["finding_id"] == "F1" and prior["findings"][0]["status"] == "open"
        assert prior["findings"][1]["issue_key"] == finding["issue_key"]
        target = review["targets"][0]["path"]
        snapshot = archive / (Path(target).stem + "-owner.yaml")
        assert digest(snapshot.read_bytes()) == owners[target]["sha256"]
        assert yaml.safe_load(snapshot.read_text())["curation_status"] == "SEEDED"
    open_keys = {f["issue_key"] for f in checkpoint["latest_finding_heads"] if f["status"] == "open"}
    assert {"prodigiosin-lotus-congener-attribution", "prodigiosin-williamson-occurrence-taxon"} <= open_keys
    assert not {"prodigiosin-serratia-strain-provenance", "prodigiosin-s4059-strain-provenance"} & open_keys
