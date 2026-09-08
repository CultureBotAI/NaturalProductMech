"""The schema says what the repository claims it says.

These assert the semantic invariants in CLAUDE.md, not LinkML's own correctness.
Each one exists because losing it would let the corpus assert something untrue
while every other gate stayed green.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = REPO_ROOT / "src" / "naturalproductmech" / "schema"
ANTIBIOTICMECH_SHARED = REPO_ROOT.parent / "AntibioticMech" / "src" / "antibioticmech" / "schema"


def test_root_class_is_the_record(schema):
    assert schema["classes"]["NaturalProductRecord"]["tree_root"] is True


def test_a_record_cannot_exist_without_a_structure(schema):
    """No InChIKey, no record. The corpus's first rule."""
    record = schema["classes"]["NaturalProductRecord"]["attributes"]
    assert record["chemical_structure"]["required"] is True
    structure = schema["classes"]["ChemicalStructure"]["attributes"]
    assert structure["standard_inchi_key"]["required"] is True


def test_producer_and_occurrence_are_separate_fields(schema):
    """The distinction the corpus exists to keep. Merging them would let an
    isolation report masquerade as a biosynthesis claim."""
    record = schema["classes"]["NaturalProductRecord"]["attributes"]
    assert "producer_organisms" in record
    assert "occurrences" in record
    assert record["producer_organisms"]["range"] == "ProducerOrganism"
    assert record["occurrences"]["range"] == "Occurrence"


def test_a_producer_claim_states_its_evidence_grade(schema):
    producer = schema["classes"]["ProducerOrganism"]["attributes"]
    assert producer["evidence_basis"]["required"] is True
    assert producer["evidence"]["required"] is True


def test_correlational_and_causal_producer_bases_are_distinguishable(schema):
    """Collapsing these would reintroduce the overstatement one level down."""
    values = schema["enums"]["ProducerEvidenceBasisEnum"]["permissible_values"]
    assert "BGC_CHARACTERIZED" in values
    assert "BGC_CORRELATED" in values


@pytest.mark.parametrize(
    "class_name",
    [
        "ProducerOrganism",
        "Occurrence",
        "BiosyntheticGeneCluster",
        "PathwayStep",
        "BioactivityObservation",
        "MolecularTarget",
        "ClinicalStatusAssertion",
        "CausalEdge",
    ],
)
def test_every_claim_class_requires_its_own_evidence(schema, class_name):
    """Record-level evidence never satisfies a claim-level obligation."""
    attributes = schema["classes"][class_name]["attributes"]
    assert attributes["evidence"]["required"] is True, f"{class_name} may carry an uncited claim"


def test_the_filing_pathway_is_required_and_has_an_unclassified_bucket(schema):
    """A multi-label classifier result must have somewhere honest to go."""
    record = schema["classes"]["NaturalProductRecord"]["attributes"]
    assert record["np_pathway"]["required"] is True
    assert "UNCLASSIFIED" in schema["enums"]["NPPathwayEnum"]["permissible_values"]


def test_a_computed_classification_names_its_tool_and_version(schema):
    """Computed is never presented as asserted, and a computed value whose
    producer is unknown cannot be reproduced or superseded."""
    computed = schema["classes"]["ComputedClassification"]["attributes"]
    assert computed["tool"]["required"] is True
    assert computed["tool_version"]["required"] is True


def test_bgc_class_is_the_mibig_4_vocabulary(schema):
    """MIBiG 4.0 removed `alkaloid` as a biosynthetic class when it separated
    cluster classification from compound classification."""
    values = set(schema["enums"]["BGCClassEnum"]["permissible_values"])
    assert values == {"PKS", "NRPS", "RIBOSOMAL", "TERPENE", "SACCHARIDE", "OTHER"}
    assert "ALKALOID" not in values


def test_source_concepts_are_required_because_attribution_is_per_record(schema):
    record = schema["classes"]["NaturalProductRecord"]["attributes"]
    assert record["source_concepts"]["required"] is True


# sha256 of the claw-governed modules at the pinned ref in
# scripts/.vendored_canon_ref. Pinned here rather than only compared against a
# sibling checkout, because CI checks out one repository and the sibling
# comparison therefore always skipped there — guarding drift exactly where it
# could not see it (#12). Changing a vendored file means changing it in claw and
# advancing the pin; updating a hash without that is the mistake this catches.
VENDORED_SHA256 = {
    "mech_shared.yaml": "1a5e21eb2ee9f3584ff6af3a6906b1d442e18c41de405b1bf907c20f44eafa2a",
    "history.yaml": "b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d",
}


@pytest.mark.parametrize("name", sorted(VENDORED_SHA256))
def test_vendored_schema_modules_match_the_pinned_hash(name):
    """Runs everywhere, including CI. No sibling checkout required."""
    actual = hashlib.sha256((SCHEMA_DIR / name).read_bytes()).hexdigest()
    assert actual == VENDORED_SHA256[name], (
        f"{name} has drifted from the vendored copy at "
        f"{(Path(__file__).resolve().parents[1] / 'scripts' / '.vendored_canon_ref').read_text().strip()}; "
        f"edit it in claw and advance the pin, do not edit it here"
    )


def test_shared_mech_modules_are_byte_identical_to_the_fleet():
    """The extra fleet-wide check, when a sibling checkout is available.

    A pinned hash proves this repository has not drifted. This proves the fleet
    has not drifted apart, which a pinned hash cannot.
    """
    if not ANTIBIOTICMECH_SHARED.exists():
        pytest.skip("sibling AntibioticMech checkout not present")
    for name in ("mech_shared.yaml", "history.yaml"):
        ours = (SCHEMA_DIR / name).read_bytes()
        theirs = (ANTIBIOTICMECH_SHARED / name).read_bytes()
        assert hashlib.sha256(ours).hexdigest() == hashlib.sha256(theirs).hexdigest(), (
            f"{name} has drifted from the vendored copy; edit it in claw, not here"
        )
