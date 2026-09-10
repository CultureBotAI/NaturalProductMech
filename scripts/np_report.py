#!/usr/bin/env python3
"""Corpus report: records per pathway, grounding, and origin-evidence coverage.

The columns this prints are chosen to make the corpus's central distinction
visible at a glance. `producer_organisms` and `occurrences` are counted
separately, and producer claims are broken out by evidence basis, because a
corpus that reported them together would hide exactly the overstatement the
schema exists to prevent.

    python scripts/np_report.py
    python scripts/np_report.py --json
"""

from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
SCHEMA_PATH = REPO_ROOT / "src" / "naturalproductmech" / "schema" / "naturalproductmech.yaml"

sys.path.insert(0, str(REPO_ROOT / "src"))

from naturalproductmech.grading import CAUSAL_BASES  # noqa: E402


def load_records(root: Path) -> list[dict[str, Any]]:
    records = []
    for path in sorted(root.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and "identifier" in doc:
            records.append(doc)
    return records


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_pathway: collections.Counter[str] = collections.Counter()
    by_status: collections.Counter[str] = collections.Counter()
    by_grounding: collections.Counter[str] = collections.Counter()
    producer_bases: collections.Counter[str] = collections.Counter()
    cluster_bases: collections.Counter[str] = collections.Counter()
    corroborated = [0]
    field_coverage: collections.Counter[str] = collections.Counter()
    inchikeys: set[str] = set()
    stereo_incomplete = 0

    counted_fields = [
        "producer_organisms",
        "occurrences",
        "biosynthetic_gene_clusters",
        "biosynthetic_pathway",
        "bioactivities",
        "bioactivity_summary",
        "molecular_targets",
        "causal_graphs",
        "related_records",
        "discussions",
    ]

    for doc in records:
        by_pathway[doc.get("np_pathway") or "ABSENT"] += 1
        by_status[doc.get("curation_status") or "ABSENT"] += 1
        by_grounding[doc.get("grounding_status") or "ABSENT"] += 1
        structure = doc.get("chemical_structure") or {}
        key = structure.get("standard_inchi_key")
        if key:
            inchikeys.add(key)
        if structure.get("stereo_complete") is False:
            stereo_incomplete += 1
        for field in counted_fields:
            if doc.get(field):
                field_coverage[field] += 1
        producer_taxa = {p.get("taxon_id") for p in doc.get("producer_organisms") or []}
        occurrence_taxa = {o.get("taxon_id") for o in doc.get("occurrences") or []}
        if producer_taxa & occurrence_taxa:
            corroborated[0] += 1
        for producer in doc.get("producer_organisms") or []:
            producer_bases[producer.get("evidence_basis") or "ABSENT"] += 1
        for cluster in doc.get("biosynthetic_gene_clusters") or []:
            cluster_bases[cluster.get("link_evidence_basis") or "ABSENT"] += 1

    causal = sum(n for basis, n in producer_bases.items() if basis in CAUSAL_BASES)
    correlated = producer_bases.get("BGC_CORRELATED", 0)

    return {
        "records": len(records),
        "unique_inchikeys": len(inchikeys),
        "stereo_incomplete": stereo_incomplete,
        "by_pathway": dict(sorted(by_pathway.items())),
        "by_curation_status": dict(sorted(by_status.items())),
        "by_grounding_status": dict(sorted(by_grounding.items())),
        "field_coverage": {f: field_coverage.get(f, 0) for f in counted_fields},
        "producer_claims": {
            "total": sum(producer_bases.values()),
            "causal": causal,
            "correlated": correlated,
            "by_basis": dict(sorted(producer_bases.items())),
        },
        "producers_corroborated_by_an_occurrence": corroborated[0],
        # A record whose origin rests only on a gene cluster whose host NCBI
        # does not name. Counted because otherwise withholding those producer
        # claims (#62, #68) reads as a hole in producer_organisms coverage
        # rather than as what it is: the compound has a characterized locus
        # and an anonymous producer, which for a sponge symbiont is the
        # honest state and not a gap to be filled.
        "origin_only_from_an_unnamed_host": sum(
            1 for record in records
            if not (record.get("producer_organisms") or [])
            and not (record.get("occurrences") or [])
            and (record.get("biosynthetic_gene_clusters") or [])
        ),
        "cluster_link_claims": {
            "total": sum(cluster_bases.values()),
            "demonstrated": cluster_bases.get("CLUSTER_DEMONSTRATED", 0),
            "by_basis": dict(sorted(cluster_bases.items())),
        },
    }


def render(summary: dict[str, Any]) -> str:
    lines = [f"records: {summary['records']}"]
    if not summary["records"]:
        lines.append("")
        lines.append("The corpus is empty. That is the expected M1 state: the schema, the")
        lines.append("validation path and the gates exist, and M2 seeds the first records")
        lines.append("from MIBiG and ChEBI. See PLAN.md section 7.")
        return "\n".join(lines)

    lines.append(f"unique InChIKeys: {summary['unique_inchikeys']}")
    lines.append(f"structures with undefined stereocentres: {summary['stereo_incomplete']}")
    lines.append("")
    lines.append("by pathway (the filing decision, computed):")
    for key, count in summary["by_pathway"].items():
        lines.append(f"  {key:<34} {count:>6}")
    lines.append("")
    lines.append("by curation status:")
    for key, count in summary["by_curation_status"].items():
        lines.append(f"  {key:<34} {count:>6}")
    lines.append("")
    lines.append("by grounding status:")
    for key, count in summary["by_grounding_status"].items():
        lines.append(f"  {key:<34} {count:>6}")
    lines.append("")
    lines.append("field coverage (records carrying at least one item):")
    for key, count in summary["field_coverage"].items():
        lines.append(f"  {key:<34} {count:>6}")
    claims = summary["producer_claims"]
    lines.append("")
    lines.append(f"producer claims: {claims['total']} "
                 f"({claims['causal']} causal, {claims['correlated']} correlational)")
    for key, count in claims["by_basis"].items():
        lines.append(f"  {key:<34} {count:>6}")
    links = summary["cluster_link_claims"]
    lines.append("")
    lines.append(f"cluster link claims: {links['total']} "
                 f"({links['demonstrated']} demonstrated)")
    for key, count in links["by_basis"].items():
        lines.append(f"  {key:<34} {count:>6}")
    lines.append("")
    lines.append(f"records where a producer taxon is independently corroborated by a "
                 f"cited occurrence: {summary['producers_corroborated_by_an_occurrence']}")
    lines.append(f"records whose only origin evidence is a gene cluster with no named "
                 f"host: {summary['origin_only_from_an_unnamed_host']}")
    lines.append("")
    lines.append("These grade two different questions and they come apart. A producer")
    lines.append("claim says this TAXON makes the compound; a cluster link says this")
    lines.append("LOCUS does. Heterologous expression settles the second and leaves the")
    lines.append("first exactly where the isolation report left it.")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit the summary as JSON")
    args = parser.parse_args()

    if not CORPUS_DIR.exists():
        print(f"missing {CORPUS_DIR}", file=sys.stderr)
        return 1
    summary = summarize(load_records(CORPUS_DIR))
    print(json.dumps(summary, indent=2) if args.json else render(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
