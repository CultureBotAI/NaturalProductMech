"""Keep the partial aborycin observations auditable independently of /tmp."""

import gzip
import hashlib
import json
import re
import shlex
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/evidence/20261013-aborycin"


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def load():
    manifest = json.loads((ARCHIVE / "manifest.json").read_text())
    rows = {row["original_path"]: row for row in manifest["artifacts"]}
    assert len(rows) == len(manifest["artifacts"])
    return manifest, rows


def content(row):
    return gzip.decompress((ARCHIVE / row["path"]).read_bytes())


def test_archive_integrity_and_snapshot_representations():
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
    reference_only = {r["original_path"]: r for r in manifest["reference_only_sources"]}
    assert len(reference_only) == 3
    assert not rows.keys() & reference_only.keys()
    for row in reference_only.values():
        assert row["source_url"].startswith("https://") and "path" not in row
    for row in manifest["reviews"]:
        blob = (ROOT / row["path"]).read_bytes()
        assert digest(blob) == row["sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]
        doc = yaml.safe_load(blob)
        assert doc["completion"] == "partial" and doc["verdict"] == "needs_curation"
        assert doc["source"]["git_revision"] == manifest["corpus_base"]
        references = {p.rstrip(".") for p in re.findall(r"/private/tmp/[A-Za-z0-9_./-]+", blob.decode())}
        assert references <= rows.keys() | reference_only.keys() | set(manifest["runtime_directories"])
        snapshots = {r["evidence_id"]: r for r in row["evidence_snapshots"]}
        assert len(snapshots) == len(row["evidence_snapshots"])
        assert snapshots.keys() == {e["evidence_id"] for e in doc["evidence"] if "snapshot_sha256" in e}
        for evidence in doc["evidence"]:
            if "snapshot_sha256" not in evidence:
                continue
            snapshot = snapshots[evidence["evidence_id"]]
            assert snapshot["sha256"] == evidence["snapshot_sha256"]
            source = (rows | reference_only)[snapshot["original_path"]]
            assert source["sha256"] == snapshot["sha256"]
        owner = doc["targets"][0]["path"]
        raw = subprocess.check_output(["git", "show", f"{manifest['corpus_base']}:{owner}"], cwd=ROOT)
        assert digest(raw) == next(r["sha256"] for r in doc["source"]["inputs"] if r["path"] == owner)
        resolved = json.loads(content(rows[snapshots["owner"]["original_path"]]))
        assert resolved == yaml.safe_load(raw)
        assert snapshots["owner"]["sha256"] != digest(raw)
        for check in doc["checks"]:
            if "exit_code" not in check:
                continue
            receipt_path = str(Path(snapshots["owner"]["original_path"])
                               .with_name(check["check_id"] + ".receipt.json"))
            receipt = json.loads(content(rows[receipt_path]))
            assert receipt["exit_code"] == check["exit_code"]
            assert shlex.join(receipt["command"]) == check["command"]


def test_receipts_preserve_failures_and_source_checksums():
    manifest, rows = load()
    references = {r["original_path"]: r for r in manifest["reference_only_sources"]}
    failed = set()
    for original, row in rows.items():
        if not original.endswith(".receipt.json"):
            continue
        receipt = json.loads(content(row))
        assert receipt["started_at"] <= receipt["finished_at"]
        if "command" in receipt:
            assert receipt["command"]
            assert digest(content(rows[receipt["log"]])) == receipt["log_sha256"]
            if receipt["exit_code"]:
                failed.add(Path(original).name)
        else:
            snapshot = (rows | references)[original.removesuffix(".receipt.json")]
            assert snapshot["sha256"] == receipt["sha256"]
            assert snapshot["bytes"] == receipt["bytes"]
    assert failed == {"sequence-audit.receipt.json", "validate-drafts.receipt.json"}


def test_historical_campaign_denominator_and_lineage():
    manifest, rows = load()
    checkpoint = json.loads(content(rows[manifest["checkpoint"]]))
    owners = {r["path"]: r for r in checkpoint["records"]}
    assert len(owners) == checkpoint["population"] == 3115
    assert sum(len(r["graph_components"]) for r in owners.values()) == 243
    reviewed = {r["path"] for r in checkpoint["reviews"]}
    pending = checkpoint["pending_in_priority_order"]
    assert len(reviewed) == checkpoint["partial_reviews"] == 16
    assert len(checkpoint["all_review_observations"]) == 23
    assert len(pending) == len(set(pending)) == checkpoint["unassessed_records"] == 3099
    assert reviewed.isdisjoint(pending) and reviewed | set(pending) == owners.keys()
    assert set(checkpoint["partial_followups"]) == reviewed
    assert checkpoint["completed_scientific_reviews"] == 0
    assert checkpoint["findings"] == {"blocker": 5, "major": 6}
    assert rows[checkpoint["prior_checkpoint"]]["sha256"] == checkpoint["prior_checkpoint_sha256"]
    inherited = checkpoint["inherited_scientific_access_stops"]
    assert rows[inherited["checkpoint"]]["sha256"] == inherited["sha256"]
    assert len(json.loads(content(rows[inherited["checkpoint"]]))[
        "access_stops_no_alternate_retrieval"]) == 162
    assert len(checkpoint["new_access_stops"]) == 20
    for row in checkpoint["all_review_observations"]:
        assert digest((ROOT / row["yaml"]).read_bytes()) == row["yaml_sha256"]
        assert digest((ROOT / row["markdown"]).read_bytes()) == row["markdown_sha256"]


def test_bounded_precursor_search_from_retained_sequence():
    _, rows = load()
    by_name = {Path(k).name: v for k, v in rows.items()}
    source = content(by_name["sequences-with-parts.xml"])
    audit = json.loads(content(by_name["sequence-audit.json"]))
    assert digest(source) == audit["input_sha256"]
    sequences = {r.findtext("GBSeq_accession-version"): r.findtext("GBSeq_sequence").upper()
                 for r in ET.fromstring(source).findall("GBSeq")}
    precursor = sequences["NZ_MKCP01000039.1"][22745:22874]
    assert len(precursor) == audit["precursor_nucleotide_length"] == 129
    reverse = precursor.translate(str.maketrans("ACGT", "TGCA"))[::-1]
    for record in audit["records"]:
        dna = sequences[record["accession"]]
        assert len(dna) == record["length"]
        for strand, query in [("forward", precursor), ("reverse_complement", reverse)]:
            matches = [i + 1 for i in range(len(dna)) if dna.startswith(query, i)]
            assert matches == record["exact_precursor_nucleotide_matches"][strand]
        low, high = record["claimed_interval"]
        assert digest(dna[low - 1:high].encode()) == record["interval_sha256"]
