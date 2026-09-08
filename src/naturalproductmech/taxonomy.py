"""Resolve an organism name to an NCBI taxonomy identifier.

One implementation, imported by every extractor whose source names organisms
without identifying them. Three of them do, and they must resolve identically:
a name that becomes NCBITaxon:1126 in one inventory and nothing in another
would put the same organism in the corpus twice, once resolvable and once not.

The table is ``data/raw/taxon_names.tsv``, built by
``scripts/extract_ncbi_taxonomy.py`` from NCBI's public-domain taxdump and
restricted to the names the adopted sources actually use.
"""

from __future__ import annotations

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TAXON_NAMES_PATH = REPO_ROOT / "data" / "raw" / "taxon_names.tsv"


def load_taxon_names(path: Path = TAXON_NAMES_PATH) -> dict[str, str]:
    """Lower-cased organism name -> NCBITaxon CURIE.

    Returns an empty mapping when the inventory is absent, so an extractor runs
    before the taxonomy source is adopted rather than failing — it simply
    resolves nothing extra, which is the state the corpus was in before.
    """
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        return {
            row["organism_name"].lower(): row["taxon_id"]
            for row in csv.DictReader(fh, delimiter="\t")
        }


def resolve_name(name: str, table: dict[str, str]) -> str | None:
    """The NCBITaxon CURIE for an organism name, or None.

    Exact match on the full name only. There is deliberately no genus fallback:
    writing a genus identifier under a species label puts an id and a label
    that denote different things on one record, which is what
    ``test_taxon_labels_stay_consistent_for_an_id`` exists to catch.
    """
    cleaned = " ".join((name or "").split())
    return table.get(cleaned.lower()) if cleaned else None
