"""The exact-match candidates tried for a UniProt-style organism name (#72).

Every candidate is still matched exactly against names.dmp; these pin what is
TRIED, which is the part that decides whether 15 molecular targets are grounded
or name-only.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location(
    "extract_ncbi_taxonomy", REPO_ROOT / "scripts" / "extract_ncbi_taxonomy.py")
taxonomy = importlib.util.module_from_spec(_spec)
sys.modules["extract_ncbi_taxonomy"] = taxonomy
_spec.loader.exec_module(taxonomy)


def test_a_plain_name_is_tried_unchanged_and_nothing_else():
    assert taxonomy.organism_name_variants("Streptomyces griseus") == ["Streptomyces griseus"]


def test_the_source_spelling_is_always_tried_first():
    """Exactness first: a name NCBI happens to carry verbatim must not be
    resolved through a rewritten variant instead."""
    variants = taxonomy.organism_name_variants("Escherichia coli (strain K12)")
    assert variants[0] == "Escherichia coli (strain K12)"


def test_a_strain_suffix_is_tried_the_way_ncbi_writes_it():
    variants = taxonomy.organism_name_variants("Escherichia coli (strain K12)")
    assert "Escherichia coli K-12" in variants   # NCBI's scientific name, taxid 83333


def test_each_collection_number_is_tried_separately():
    """UniProt lists several deposits for one strain; NCBI knows one of them."""
    variants = taxonomy.organism_name_variants(
        "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)")
    assert "Saccharomyces cerevisiae ATCC 204508" in variants
    assert "Saccharomyces cerevisiae S288c" in variants


def test_no_common_names_are_tried():
    """`Human` stays unresolved on purpose. NCBI's genbank common names would
    resolve it and bring 45,565 names with it, 621 ambiguous across taxa and 53
    colliding with another taxon's scientific name."""
    assert taxonomy.organism_name_variants("Human") == ["Human"]


def test_an_empty_name_yields_nothing_to_try():
    assert taxonomy.organism_name_variants("") == []
    assert taxonomy.organism_name_variants("   ") == []
