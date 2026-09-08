"""The guarded write path: validate before writing, and emit stably.

The emission contract matters as much as the validation: re-writing an
unchanged record must be byte-identical, or a script that touches one field
buries the change in reflow churn and review stops working.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from naturalproductmech.validation.write_validated import (  # noqa: E402
    EMIT_OPTS,
    ValidationFailedError,
    emit_natural_product_yaml,
    validate_natural_product,
    write_validated_natural_product,
)


def test_a_minimal_record_validates(minimal_record):
    assert validate_natural_product(minimal_record) == []


def test_an_unknown_field_is_an_error_not_a_shrug(minimal_record):
    """Closed-mode validation. Open mode would accept a typo'd field name and
    silently drop the value."""
    minimal_record["producer_organism"] = []  # singular: a plausible typo
    assert validate_natural_product(minimal_record)


def test_a_record_without_a_structure_is_refused(minimal_record):
    del minimal_record["chemical_structure"]
    assert validate_natural_product(minimal_record)


def test_a_malformed_inchikey_is_refused(minimal_record):
    minimal_record["chemical_structure"]["standard_inchi_key"] = "not-an-inchikey"
    assert validate_natural_product(minimal_record)


def test_a_producer_without_evidence_is_refused(minimal_record):
    """The claim-level evidence rule, enforced rather than documented."""
    minimal_record["producer_organisms"] = [{
        "taxon_id": "NCBITaxon:1836",
        "taxon_label": "Saccharopolyspora erythraea",
        "evidence_basis": "BGC_CHARACTERIZED",
    }]
    assert validate_natural_product(minimal_record)


def test_a_producer_with_evidence_is_accepted(minimal_record):
    minimal_record["producer_organisms"] = [{
        "taxon_id": "NCBITaxon:1836",
        "taxon_label": "Saccharopolyspora erythraea",
        "evidence_basis": "BGC_CHARACTERIZED",
        "evidence": [{"reference": "mibig:BGC0000055", "evidence_type": "DATABASE_ASSERTION"}],
    }]
    assert validate_natural_product(minimal_record) == []


def test_an_occurrence_without_evidence_is_refused(minimal_record):
    minimal_record["occurrences"] = [{
        "taxon_id": "NCBITaxon:1836",
        "taxon_label": "Saccharopolyspora erythraea",
    }]
    assert validate_natural_product(minimal_record)


def test_an_invalid_producer_basis_is_refused(minimal_record):
    """A basis outside the enum would let a grading mistake through as a value."""
    minimal_record["producer_organisms"] = [{
        "taxon_id": "NCBITaxon:1836",
        "taxon_label": "Saccharopolyspora erythraea",
        "evidence_basis": "PROBABLY",
        "evidence": [{"reference": "PMID:12345678"}],
    }]
    assert validate_natural_product(minimal_record)


def test_write_refuses_an_invalid_record_without_writing(tmp_path, minimal_record):
    del minimal_record["label"]
    target = tmp_path / "bad.yaml"
    with pytest.raises(ValidationFailedError):
        write_validated_natural_product(minimal_record, target)
    assert not target.exists(), "an invalid record reached disk"


def test_rewriting_an_unchanged_record_is_byte_identical(tmp_path, minimal_record):
    target = tmp_path / "record.yaml"
    write_validated_natural_product(minimal_record, target)
    first = target.read_bytes()
    reloaded = yaml.safe_load(target.read_text(encoding="utf-8"))
    write_validated_natural_product(reloaded, target)
    assert target.read_bytes() == first


def test_emission_options_are_shared_not_reimplemented(minimal_record):
    """A test that re-declared its own dump options would drift from what we
    actually write, and then prove nothing."""
    assert EMIT_OPTS["sort_keys"] is False
    assert emit_natural_product_yaml(minimal_record) == yaml.safe_dump(minimal_record, **EMIT_OPTS)
