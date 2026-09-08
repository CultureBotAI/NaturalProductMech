"""Grade a production claim from a source's own evidence vocabulary.

One implementation, imported by both the MIBiG extractor and the seeder. It
lived in two places briefly and that is a drift waiting to happen: the two
copies disagreed about the empty case, which is the single largest bucket in
MIBiG.

The mapping itself is data, in ``conf/producer_evidence.tsv``, so the grading
can be argued with without editing code.
"""

from __future__ import annotations

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PRODUCER_EVIDENCE_PATH = REPO_ROOT / "conf" / "producer_evidence.tsv"

#: What a source asserts when it states no experiment. See `grade_production`.
SOURCE_ASSERTION = "SOURCE_ASSERTION"

#: Bases that rest on demonstration rather than association or assertion.
#: Producer bases that rest on demonstration rather than assertion. Imported
#: by the report rather than restated there, so the headline figure and the
#: grader cannot disagree. Heterologous expression is deliberately absent: it
#: demonstrates the cluster, not the organism.
CAUSAL_BASES = frozenset({
    "BGC_CHARACTERIZED",
    "ISOTOPE_FEEDING",
    "AXENIC_CULTURE",
})


def load_evidence_map(path: Path = PRODUCER_EVIDENCE_PATH) -> dict[str, dict[str, str]]:
    """Source evidence method -> its grades for both claims, from the TSV.

    Leading ``#`` lines are stripped before parsing. The file carries a long
    header explaining the distinction it exists for, and csv.DictReader would
    otherwise take the first comment line as the column names — which it did,
    silently, until the extractor crashed on a missing column.
    """
    lines = [
        line for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    return {
        row["mibig_method"]: {
            "supports": row["supports"],
            "producer_basis": row["producer_basis"],
            "cluster_basis": row["cluster_basis"],
        }
        for row in csv.DictReader(lines, delimiter="\t")
    }


def grade_production(methods: list[str], evidence_map: dict[str, dict[str, str]]) -> str | None:
    """How well supported is the claim that THIS TAXON makes the compound.

    Only methods marked ``organism+cluster`` in the table can raise this grade.
    Heterologous expression, enzymatic assays and in-vitro work establish what a
    cloned locus can do; they say nothing new about the native producer, whose
    claim rests on the isolation report either way.

    * A qualifying method present — the strongest it supports.
    * No qualifying method — ``SOURCE_ASSERTION``. The source asserts
      production, citing a report nobody here has read. It is the commonest
      grade by far, and it is honest: it covers the legacy entries whose
      evidence was never migrated AND the entries whose evidence only ever
      addressed the cluster.

    There is no ``None`` case. A MIBiG entry always asserts that the organism
    makes the compound; what varies is how well the LOCUS attribution is
    supported, and that is :func:`grade_cluster_link`'s job.
    """
    best: str | None = None
    for method in methods:
        entry = evidence_map.get(method)
        if not entry or entry["supports"] != "organism+cluster":
            continue
        basis = entry["producer_basis"]
        if basis == "BGC_CHARACTERIZED":
            return basis
        best = best or (basis or None)
    return best or SOURCE_ASSERTION


def grade_cluster_link(methods: list[str], evidence_map: dict[str, dict[str, str]]) -> str:
    """How well supported is the claim that THIS LOCUS makes the compound.

    This is what MIBiG's locus evidence actually grades, so the full vocabulary
    speaks here. An unrecognised method fails closed to ``CLUSTER_UNSTATED``
    rather than being read as a demonstration.
    """
    rank = {"CLUSTER_DEMONSTRATED": 0, "CLUSTER_CORRELATED": 1, "CLUSTER_PREDICTED": 2}
    best: str | None = None
    for method in methods:
        entry = evidence_map.get(method)
        basis = entry["cluster_basis"] if entry else ""
        if not basis:
            continue
        if best is None or rank[basis] < rank[best]:
            best = basis
    return best or "CLUSTER_UNSTATED"
