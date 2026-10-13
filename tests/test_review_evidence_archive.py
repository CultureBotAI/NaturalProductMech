"""Published review checkpoints remain auditable without temporary workspaces."""

import gzip
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVES = {
    "20261013-first-two-records": {
        "published": 2, "partial": 2, "pending": 3113,
        "findings": {"blocker": 2, "major": 1},
        "failed_receipts": {"inspect.receipt.json", "draft-validation.receipt.json"},
    },
    "20261013-2mib-heme": {
        "published": 3, "partial": 5, "pending": 3110,
        "findings": {"blocker": 3, "major": 2}, "failed_receipts": set(),
    },
    "20261013-indigoidine": {
        "published": 2, "partial": 7, "pending": 3108,
        "findings": {"blocker": 4, "major": 2}, "failed_receipts": set(),
        "previous_archives": ["20261013-first-two-records", "20261013-2mib-heme"],
    },
    "20261013-mycophenolic": {
        "published": 1, "partial": 8, "pending": 3107,
        "findings": {"blocker": 4, "major": 4}, "failed_receipts": set(),
        "previous_archives": [
            "20261013-first-two-records", "20261013-2mib-heme", "20261013-indigoidine",
        ],
    },
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture(scope="module")
def manifest(archive):
    return json.loads((archive / "manifest.json").read_text())


@pytest.fixture(scope="module", params=ARCHIVES)
def archive(request):
    return ROOT / "reviews/evidence" / request.param


def artifact_bytes(archive, row):
    content = (archive / row["path"]).read_bytes()
    return gzip.decompress(content) if row.get("encoding") == "gzip" else content


@pytest.fixture(scope="module")
def artifacts(manifest):
    return {row["original_path"]: row for row in manifest["artifacts"]}


def test_archive_bytes_and_paths(archive, manifest, artifacts):
    assert manifest["schema_version"] == 1
    assert len(artifacts) == len(manifest["artifacts"])
    paths = set()
    for row in artifacts.values():
        relative = PurePosixPath(row["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert relative.parts[0] == "artifacts"
        path = archive / relative
        assert path.resolve().is_relative_to(archive.resolve())
        assert not any(p.is_symlink() for p in (path, *path.parents))
        assert path.is_file()
        assert row.get("encoding") in (None, "gzip")
        assert path.stat().st_size == row.get("stored_bytes", row["bytes"])
        assert digest(path) == row.get("stored_sha256", row["sha256"])
        content = artifact_bytes(archive, row)
        assert len(content) == row["bytes"]
        assert hashlib.sha256(content).hexdigest() == row["sha256"]
        paths.add(path)
    assert len(paths) == len(artifacts)
    assert paths == {p for p in (archive / "artifacts").rglob("*") if p.is_file()}


def test_all_report_local_artifacts_are_archived(archive, manifest, artifacts):
    pattern = re.compile(r"/private/tmp/[A-Za-z0-9_./-]+")
    reference_only = {row["original_path"] for row in manifest.get("reference_only_sources", [])}
    assert len(manifest["reviews"]) == ARCHIVES[archive.name]["published"]
    for saved in manifest["reviews"]:
        path = ROOT / saved["path"]
        assert digest(path) == saved["sha256"]
        assert digest(ROOT / saved["markdown"]) == saved["markdown_sha256"]
        body = path.read_text()
        references = {value.rstrip(".") for value in pattern.findall(body)}
        references.discard(manifest["source_workspace"])
        assert references and references <= artifacts.keys() | reference_only
        review = yaml.safe_load(body)
        assert review["completion"] == "partial"
        blocked = {"20261013T054205Z-heme-d1", "20261013T064413Z-indigoidine"}
        expected = "blocked" if saved["review_id"] in blocked else "needs_curation"
        assert review["verdict"] == expected
        assert review["source"]["git_revision"] == manifest["corpus_base"]
        for evidence in review["evidence"]:
            if evidence["reference"] in artifacts and "snapshot_sha256" in evidence:
                assert evidence["snapshot_sha256"] == artifacts[evidence["reference"]]["sha256"]


def test_receipts_match_archived_outputs(archive, artifacts):
    receipts = [row for row in artifacts.values() if row["path"].endswith(".receipt.json")]
    assert receipts
    failed = set()
    for row in receipts:
        receipt = json.loads(artifact_bytes(archive, row))
        if "stdout" in receipt:
            # Saver receipts retain captured streams rather than a separate log.
            output = json.loads(receipt["stdout"])
            saved = yaml.safe_load(artifact_bytes(archive, artifacts[receipt["command"][-1]]))
            relative = f"reviews/structured/{saved['review_id']}/review.yaml"
            assert output["review"].endswith("/" + relative)
            assert output["markdown"].endswith("/" + relative.removesuffix(".yaml") + ".md")
            assert yaml.safe_load((ROOT / relative).read_text()) == saved
        elif receipt.get("log") in artifacts:
            assert artifacts[receipt["log"]]["sha256"] == receipt.get("sha256", receipt.get("log_sha256"))
        else:
            original_log = row["original_path"].removesuffix(".receipt.json") + ".log"
            log = artifact_bytes(archive, artifacts[original_log])
            if "output" in receipt or "log" in receipt:
                assert log.decode() == receipt.get("output", receipt.get("log"))
            assert hashlib.sha256(log).hexdigest() == receipt["log_sha256"]
        assert receipt["command"] and receipt["started_at"] <= receipt["finished_at"]
        if receipt["exit_code"]:
            failed.add(Path(row["path"]).name)
    assert failed == ARCHIVES[archive.name]["failed_receipts"]


def test_campaign_preserves_full_population(archive, manifest):
    checkpoint = json.loads((archive / manifest.get(
        "checkpoint", "artifacts/review-campaign-checkpoint.json"
    )).read_text())
    population = checkpoint if "checkpoint" in manifest else json.loads(
        (archive / "artifacts/population.json").read_text()
    )
    expected_counts = ARCHIVES[archive.name]
    assert checkpoint["base"] == population["base"] == manifest["corpus_base"]
    owners = {row["path"]: row for row in population["records"]}
    assert len(owners) == len(population["records"]) == checkpoint["population"] == 3115
    components = {c["path"]: c for r in owners.values() for c in r["graph_components"]}
    assert len(components) == checkpoint["graph_components"] == 242
    assert len({r["identifier"] for r in owners.values()}) == len(owners)
    reviewed = {r["path"] for r in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(reviewed) == checkpoint["partial_reviews"] == checkpoint["scientific_review_bundles"]
    assert len(reviewed) == expected_counts["partial"]
    assert checkpoint["completed_scientific_reviews"] == 0
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"]
    assert len(pending) == expected_counts["pending"]
    assert not reviewed.intersection(pending)
    assert reviewed | set(pending) == owners.keys()
    states = {row["path"]: row["review_state"] for row in checkpoint["records"]}
    # The first archive used longer state names; its immutable vocabulary stays valid.
    partial_states = {"partial", "partial_scientific_review_saved"}
    pending_states = {"unassessed", "not_scientifically_reviewed"}
    assert {path for path, state in states.items() if state in partial_states} == reviewed
    assert {path for path, state in states.items() if state in pending_states} == set(pending)
    assert checkpoint["findings"] == expected_counts["findings"]
    assert checkpoint["goal_status"] == "active"
    previous = set()
    if "checkpoint" in manifest:
        for previous_archive in expected_counts.get("previous_archives", ["20261013-first-two-records"]):
            previous_manifest = json.loads((archive.parent / previous_archive / "manifest.json").read_text())
            previous.update(r["review_id"] for r in previous_manifest["reviews"])
        for row in checkpoint["reviews"]:
            assert digest(ROOT / row["yaml"]) == row["yaml_sha256"]
            assert digest(ROOT / row["markdown"]) == row["markdown_sha256"]
    assert {r["review_id"] for r in checkpoint["reviews"]} == previous | {
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
    assert_historical_bytes(base, expected)


def assert_historical_bytes(base, expected):
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


def test_review_context_matches_historical_inputs(manifest):
    inputs = {}
    for row in manifest["reviews"]:
        review = yaml.safe_load((ROOT / row["path"]).read_text())
        for item in review["source"]["inputs"]:
            if item["path"] in inputs:
                assert inputs[item["path"]]["sha256"] == item["sha256"]
            inputs[item["path"]] = item
    assert inputs
    assert_historical_bytes(manifest["corpus_base"], inputs)


def test_cached_sources_match_report_attestations():
    archive = ROOT / "reviews/evidence/20261013-2mib-heme"
    manifest = json.loads((archive / "manifest.json").read_text())
    artifacts = {row["original_path"]: row for row in manifest["artifacts"]}
    audit = json.loads((archive / "artifacts/workspace/cached-sequence-audit.json").read_text())
    assert len(audit["proteins"]) == 13
    assert len(audit["source_hashes"]) == 27
    for original, expected in audit["source_hashes"].items():
        assert artifacts[original]["sha256"] == expected
        assert hashlib.sha256(artifact_bytes(archive, artifacts[original])).hexdigest() == expected
    review = yaml.safe_load((ROOT / manifest["reviews"][0]["path"]).read_text())
    attestation = next(note.split("manifest: ", 1)[1] for note in review["limitations"]
                       if "raw-source SHA-256 manifest: " in note)
    assert json.loads(attestation) == audit["source_hashes"]
    checkpoint = json.loads((archive / manifest["checkpoint"]).read_text())
    inherited = checkpoint["inherited_scientific_access_stops"]
    raw = artifacts[inherited["checkpoint"]]
    assert raw["sha256"] == inherited["sha256"]
    stops = json.loads(artifact_bytes(archive, raw))
    assert len(stops["access_stops_no_alternate_retrieval"]) == inherited["count"] == 162
    assert stops["access_stop_aliases_no_alternate_retrieval"]


def test_indigoidine_sources_and_reference_only_limits():
    archive = ROOT / "reviews/evidence/20261013-indigoidine"
    manifest = json.loads((archive / "manifest.json").read_text())
    artifacts = {row["original_path"]: row for row in manifest["artifacts"]}
    reference_only = {row["original_path"]: row for row in manifest["reference_only_sources"]}
    assert not artifacts.keys() & reference_only.keys()
    assert len(reference_only) == 5
    assert {Path(path).name for path in reference_only} == {
        "bitok2017.pdf", "ccm3239-2026-primary.html", "ccm3239-2026-si.pdf",
        "ccm3239-2026-fig1.png", "PMID28533156.xml",
    }
    for row in reference_only.values():
        assert row["reason"] == "Redistribution rights not established; retain citation and hash only."
        assert row["source_url"].startswith("https://")
        assert "path" not in row

    workspace = manifest["source_workspace"]
    evidence = json.loads(artifact_bytes(archive, artifacts[workspace + "/evidence-audit.json"]))
    protein = json.loads(artifact_bytes(archive, artifacts[workspace + "/protein-audit.json"]))
    assert len(evidence["artifacts"]) == 27
    assert len(protein["cds"]) == 10
    for row in evidence["artifacts"]:
        retained = artifacts.get(row["path"], reference_only.get(row["path"]))
        assert retained is not None
        assert retained["sha256"] == row["sha256"]
        assert retained["bytes"] == row["bytes"]
        assert row["receipt_verified"]
    for original, expected in protein["source_hashes"].items():
        assert artifacts[original]["sha256"] == expected
    assert artifacts[workspace + "/K4MP98.json"]["sha256"] == evidence["sc_indc"]["raw_sha256"]

    saved = next(r for r in manifest["reviews"] if r["review_id"] == "20261013T064413Z-indigoidine")
    review = yaml.safe_load((ROOT / saved["path"]).read_text())
    sources = next(e for e in review["evidence"] if e["evidence_id"] == "source-integrity")
    attestation = sources["summary"].split("Original source URLs and hashes: ", 1)[1]
    reported, _ = json.JSONDecoder().raw_decode(attestation)
    assert reported == evidence["artifacts"]
    assert sources["snapshot_sha256"] == artifacts[workspace + "/evidence-audit.json"]["sha256"]
    by_id = {e["evidence_id"]: e for e in review["evidence"]}
    assert by_id["native-sequences"]["snapshot_sha256"] == artifacts[
        workspace + "/protein-audit.json"
    ]["sha256"]
    for evidence_id, filename in [
        ("bitok2017", "bitok2017.pdf"), ("fri5", "PMID28533156.xml"),
        ("ccm2026", "ccm3239-2026-primary.html"),
    ]:
        row = next(r for p, r in reference_only.items() if Path(p).name == filename)
        assert by_id[evidence_id]["snapshot_sha256"] == row["sha256"]

    checkpoint = json.loads((archive / manifest["checkpoint"]).read_text())
    inherited = checkpoint["inherited_scientific_access_stops"]
    assert artifacts[inherited["checkpoint"]]["sha256"] == inherited["sha256"]
    stops = json.loads(artifact_bytes(archive, artifacts[inherited["checkpoint"]]))
    assert len(stops["access_stops_no_alternate_retrieval"]) == inherited["count"] == 162
    assert stops["access_stop_aliases_no_alternate_retrieval"]
