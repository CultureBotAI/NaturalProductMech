"""The first review checkpoint remains auditable without its temporary workspace."""

import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-first-two-records"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture(scope="module")
def manifest():
    return json.loads((ARCHIVE / "manifest.json").read_text())


@pytest.fixture(scope="module")
def artifacts(manifest):
    return {row["original_path"]: row for row in manifest["artifacts"]}


def test_archive_bytes_and_paths(manifest, artifacts):
    assert manifest["schema_version"] == 1
    assert len(artifacts) == len(manifest["artifacts"])
    paths = set()
    for row in artifacts.values():
        relative = PurePosixPath(row["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert relative.parts[0] == "artifacts"
        path = ARCHIVE / relative
        assert not path.is_symlink() and path.is_file()
        assert path.stat().st_size == row["bytes"]
        assert digest(path) == row["sha256"]
        paths.add(path)
    assert len(paths) == len(artifacts)
    assert paths == {p for p in (ARCHIVE / "artifacts").rglob("*") if p.is_file()}


def test_all_report_local_artifacts_are_archived(manifest, artifacts):
    prefix = manifest["source_workspace"] + "/"
    pattern = re.compile(re.escape(prefix) + r"[A-Za-z0-9_.-]+")
    assert len(manifest["reviews"]) == 2
    for saved in manifest["reviews"]:
        path = ROOT / saved["path"]
        assert digest(path) == saved["sha256"]
        assert digest(ROOT / saved["markdown"]) == saved["markdown_sha256"]
        body = path.read_text()
        references = set(pattern.findall(body))
        assert references and references <= artifacts.keys()
        review = yaml.safe_load(body)
        assert review["completion"] == "partial"
        assert review["verdict"] == "needs_curation"
        assert review["source"]["git_revision"] == manifest["corpus_base"]
        for evidence in review["evidence"]:
            if evidence["reference"] in artifacts and "snapshot_sha256" in evidence:
                assert evidence["snapshot_sha256"] == artifacts[evidence["reference"]]["sha256"]


def test_receipts_match_archived_outputs(artifacts):
    receipts = [row for row in artifacts.values() if row["path"].endswith(".receipt.json")]
    assert receipts
    failed = set()
    for row in receipts:
        receipt = json.loads((ARCHIVE / row["path"]).read_text())
        assert receipt["log"] in artifacts
        assert artifacts[receipt["log"]]["sha256"] == receipt["sha256"]
        assert receipt["command"] and receipt["started_at"] <= receipt["finished_at"]
        if receipt["exit_code"]:
            failed.add(Path(row["path"]).name)
    assert failed == {"inspect.receipt.json", "draft-validation.receipt.json"}


def test_campaign_preserves_full_population(manifest):
    checkpoint = json.loads((ARCHIVE / "artifacts/review-campaign-checkpoint.json").read_text())
    population = json.loads((ARCHIVE / "artifacts/population.json").read_text())
    assert checkpoint["base"] == population["base"] == manifest["corpus_base"]
    owners = {row["path"]: row for row in population["records"]}
    assert len(owners) == len(population["records"]) == checkpoint["population"] == 3115
    components = {c["path"]: c for r in owners.values() for c in r["graph_components"]}
    assert len(components) == checkpoint["graph_components"] == 242
    assert len({r["identifier"] for r in owners.values()}) == len(owners)
    reviewed = {r["path"] for r in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(reviewed) == checkpoint["partial_reviews"] == checkpoint["scientific_review_bundles"] == 2
    assert checkpoint["completed_scientific_reviews"] == 0
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3113
    assert not reviewed.intersection(pending)
    assert reviewed | set(pending) == owners.keys()
    assert checkpoint["findings"] == {"blocker": 2, "major": 1}
    assert checkpoint["goal_status"] == "active"
    assert {r["review_id"] for r in checkpoint["reviews"]} == {
        r["review_id"] for r in manifest["reviews"]
    }
    assert {r["path"]: r["sha256"] for r in checkpoint["records"]} == {
        path: row["sha256"] for path, row in owners.items()
    }

    # Verify historical bytes, not today's corpus: later legitimate curation must
    # not invalidate this immutable observation. One batch avoids per-file git calls.
    expected = owners | components
    base = manifest["corpus_base"]
    tracked = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", base, "--", "data/natural_products", "data/causal_graphs"],
        cwd=ROOT, text=True,
    ).splitlines()
    assert {path for path in tracked if path.endswith(".yaml")} == expected.keys()
    request = "".join(f"{base}:{path}\n" for path in expected).encode()
    output = subprocess.check_output(["git", "cat-file", "--batch"], input=request, cwd=ROOT)
    offset = 0
    for row in expected.values():
        end = output.index(b"\n", offset)
        _, kind, size = output[offset:end].split()
        assert kind == b"blob"
        offset = end + 1
        blob = output[offset:offset + int(size)]
        assert hashlib.sha256(blob).hexdigest() == row["sha256"]
        offset += int(size)
        assert output[offset:offset + 1] == b"\n"
        offset += 1
    assert offset == len(output)
