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
    canonicalize_top_level_keys,
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


def test_a_record_carrying_a_discussion_and_a_dataset_validates(
    minimal_record, host_symbiont_discussion, producer_genome_dataset
):
    """The vendored shared classes are reachable from a record, and the shapes
    the fixtures document are the ones that pass (#14).

    Nothing exercised `Discussion` or `Dataset` before, while both the curation
    doc and an integrity test depend on them — so the requirement and the shape
    it requires had never been checked together.
    """
    minimal_record["discussions"] = [host_symbiont_discussion]
    minimal_record["datasets"] = [producer_genome_dataset]
    assert validate_natural_product(minimal_record) == []


def test_a_discussion_without_its_required_fields_is_refused(minimal_record):
    """`local_id` is the plausible guess and it is wrong."""
    minimal_record["discussions"] = [{"local_id": "d1", "prompt": "who makes it?"}]
    assert validate_natural_product(minimal_record)


def test_source_discussions_canonicalize_before_curator_pathway_and_graphs(
    tmp_path, minimal_record
):
    """If a curation script inserts `biosynthetic_pathway` or `causal_graphs`
    before a source-generated `discussions` section (or appends `curation_history`
    before mutating another slot), `write_validated_natural_product` must emit
    top-level keys in the exact seeder/reproduction order (#999).
    """
    minimal_record["curation_history"] = [
        {
            "timestamp": "2026-10-19T00:00:00Z",
            "curator": "test-curator",
            "action": "RECORD_CURATED",
            "changes": "Curated pathway and graph.",
        }
    ]
    minimal_record["causal_graphs"] = [
        {
            "graph_id": "biosynthesis",
            "scope": "BIOSYNTHESIS",
            "nodes": [{"node_id": "n1", "label": "node 1", "node_type": "COMPOUND"}],
            "edges": [],
        }
    ]
    minimal_record["biosynthetic_pathway"] = [
        {
            "step_number": 1,
            "notes": "step 1",
            "evidence": [{"reference": "PMID:9770448", "evidence_type": "PRIMARY_EXPERIMENT"}],
        }
    ]
    minimal_record["discussions"] = [
        {
            "discussion_id": "source-structure-correction",
            "kind": "CONTROVERSY",
            "status": "OPEN",
            "prompt": "Upstream structure was split via curation table.",
        }
    ]

    target = tmp_path / "record.yaml"
    write_validated_natural_product(minimal_record, target)
    reloaded = yaml.safe_load(target.read_text(encoding="utf-8"))
    keys = list(reloaded.keys())
    assert keys.index("curation_status") < keys.index("discussions")
    assert keys.index("discussions") < keys.index("biosynthetic_pathway")
    assert keys.index("biosynthetic_pathway") < keys.index("causal_graphs")
    assert keys[-1] == "curation_history"


def test_curator_only_discussions_canonicalize_after_curator_graphs(
    tmp_path, minimal_record, host_symbiont_discussion
):
    """Curator-only `discussions` (`discussion_id` starting with `curator-`)
    are carried by the seeder after `biosynthetic_pathway`, `causal_graphs`,
    and `causal_graph_refs` (#999).
    """
    minimal_record["discussions"] = [host_symbiont_discussion]
    minimal_record["biosynthetic_pathway"] = [
        {
            "step_number": 1,
            "notes": "step 1",
            "evidence": [{"reference": "PMID:9770448", "evidence_type": "PRIMARY_EXPERIMENT"}],
        }
    ]
    minimal_record["causal_graphs"] = [
        {
            "graph_id": "biosynthesis",
            "scope": "BIOSYNTHESIS",
            "nodes": [{"node_id": "n1", "label": "node 1", "node_type": "COMPOUND"}],
            "edges": [],
        }
    ]
    minimal_record["curation_history"] = [
        {
            "timestamp": "2026-10-19T00:00:00Z",
            "curator": "test-curator",
            "action": "RECORD_CURATED",
            "changes": "Added curator discussion.",
        }
    ]

    target = tmp_path / "record.yaml"
    write_validated_natural_product(minimal_record, target)
    reloaded = yaml.safe_load(target.read_text(encoding="utf-8"))
    keys = list(reloaded.keys())
    assert keys.index("curation_status") < keys.index("biosynthetic_pathway")
    assert keys.index("biosynthetic_pathway") < keys.index("causal_graphs")
    assert keys.index("causal_graphs") < keys.index("discussions")
    assert keys[-1] == "curation_history"


def test_molecular_targets_placement_distinguishes_imported_from_curator_only(
    minimal_record,
):
    """Imported `molecular_targets` emit in the seeder's mid-record position
    (before `related_records`), while curator-only `molecular_targets` emit
    in the carried curator section after `curation_status` (#999).
    """
    curator_doc = dict(minimal_record)
    curator_doc["related_records"] = ["antibioticmech:AM0001"]
    curator_doc["molecular_targets"] = [
        {
            "target_name": "23S rRNA peptidyl transferase center",
            "source": "CURATOR",
            "evidence": [{"reference": "PMID:12345678", "evidence_type": "EXPERIMENTAL"}],
        }
    ]
    curator_keys = list(canonicalize_top_level_keys(curator_doc).keys())
    assert curator_keys.index("related_records") < curator_keys.index("curation_status")
    assert curator_keys.index("curation_status") < curator_keys.index("molecular_targets")

    imported_doc = dict(minimal_record)
    imported_doc["related_records"] = ["antibioticmech:AM0001"]
    imported_doc["molecular_targets"] = [
        {
            "target_name": "Bacterial 50S ribosomal subunit",
            "source": "CHEMBL",
            "evidence": [{"reference": "chembl:CHEMBL532", "evidence_type": "DATABASE_ASSERTION"}],
        }
    ]
    imported_keys = list(canonicalize_top_level_keys(imported_doc).keys())
    assert imported_keys.index("molecular_targets") < imported_keys.index("related_records")


def test_causal_graph_document_key_order_is_canonicalized():
    """Component `CausalGraphDocument` payloads canonicalize `record_id`,
    `standard_inchi_key`, `graph`, and `curation_history` last.
    """
    component_doc = {
        "curation_history": [
            {
                "timestamp": "2026-10-19T00:00:00Z",
                "curator": "test-curator",
                "action": "RECORD_CURATED",
                "changes": "Component graph.",
            }
        ],
        "graph": {
            "id": "biosynthesis",
            "name": "Test graph",
            "nodes": [{"id": "n1", "label": "node 1", "element_type": "COMPOUND"}],
            "edges": [],
        },
        "standard_inchi_key": "ULGZDMOVFRHVEP-RWJQBGPGSA-N",
        "record_id": "CHEBI:42355",
    }
    assert list(canonicalize_top_level_keys(component_doc).keys()) == [
        "record_id",
        "standard_inchi_key",
        "graph",
        "curation_history",
    ]

