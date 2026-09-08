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

#: The TSV value marking a method that is not producer-grade at all.
NOT_PRODUCER_GRADE = "NOT_PRODUCER_GRADE"

#: What a source asserts when it states no experiment. See `grade_production`.
SOURCE_ASSERTION = "SOURCE_ASSERTION"

#: Bases that rest on demonstration rather than association or assertion.
CAUSAL_BASES = frozenset({
    "BGC_CHARACTERIZED",
    "HETEROLOGOUS_EXPRESSION",
    "ISOTOPE_FEEDING",
    "AXENIC_CULTURE",
})


def load_producer_evidence_map(path: Path = PRODUCER_EVIDENCE_PATH) -> dict[str, str]:
    """Source evidence method -> ``evidence_basis``, from the committed TSV.

    Leading ``#`` lines are stripped before parsing. The file carries a long
    header explaining the case the table cannot express, and csv.DictReader
    would otherwise take the first comment line as the column names — which it
    did, silently, until the extractor crashed on a missing column.
    """
    lines = [
        line for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    return {
        row["mibig_method"]: row["evidence_basis"]
        for row in csv.DictReader(lines, delimiter="\t")
    }


def grade_production(methods: list[str], evidence_map: dict[str, str]) -> str | None:
    """The best ``evidence_basis`` a locus's evidence methods support.

    Three cases, and the third is the one that needed measuring:

    * **A producer-grade method is present** — return the strongest.
      ``BGC_CHARACTERIZED`` beats ``BGC_CORRELATED``.
    * **Methods are present but none is producer-grade** — return ``None``. In
      MIBiG 4.0 this is homology-based prediction, and it applies to 2 active
      entries. A prediction is not evidence of production, so the claim goes to
      the worklist rather than into ``producer_organisms``.
    * **No method is stated at all** — return ``SOURCE_ASSERTION``. This is
      1,627 of MIBiG's 2,437 active entries, so how it is handled decides most
      of the corpus. Dropping them would discard two thirds of the anchor
      source over a field MIBiG simply does not fill; promoting them to
      ``BGC_CHARACTERIZED`` would claim experiments nobody reported. The honest
      middle is what the enum already calls SOURCE_ASSERTION: a curated
      database asserts production without stating the experiment. It is a
      producer claim, it cites MIBiG as a database assertion, and a consumer
      wanting demonstrated production filters for ``CAUSAL_BASES``.

    An unrecognised method fails closed rather than being admitted by default:
    a vocabulary that grew upstream should be looked at, not waved through.
    """
    if not methods:
        return SOURCE_ASSERTION
    best: str | None = None
    for method in methods:
        basis = evidence_map.get(method)
        if basis is None or basis == NOT_PRODUCER_GRADE:
            continue
        if basis == "BGC_CHARACTERIZED":
            return basis
        best = best or basis
    return best
