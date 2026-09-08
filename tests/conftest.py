"""Shared fixtures: the schema, the corpus, and a minimal valid record."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "src" / "naturalproductmech" / "schema" / "naturalproductmech.yaml"
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"


@pytest.fixture(scope="session")
def schema() -> dict[str, Any]:
    return yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def record_paths() -> list[Path]:
    return sorted(CORPUS_DIR.rglob("*.yaml"))


@pytest.fixture(scope="session")
def records(record_paths: list[Path]) -> list[dict[str, Any]]:
    docs = []
    for path in record_paths:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and "identifier" in doc:
            docs.append(doc)
    return docs


@pytest.fixture
def minimal_record() -> dict[str, Any]:
    """The smallest record the schema accepts.

    Every required field and nothing else, so a test that adds one field is
    testing that field. Erythromycin A, because it is the canary in CLAUDE.md
    and exercises the AntibioticMech join.
    """
    return {
        "identifier": "CHEBI:42355",
        "label": "erythromycin A",
        "chemical_structure": {
            "standard_inchi_key": "ULGZDMOVFRHVEP-RWJQBGPGSA-N",
        },
        "np_pathway": "POLYKETIDES",
        "source_concepts": [
            {
                "source": "CHEBI",
                "source_id": "CHEBI:42355",
                "source_label": "erythromycin A",
                "minted_identifier": "naturalproductmech:chebi-0123456789",
            }
        ],
        "grounding_status": "EXACT",
        "curation_status": "SEEDED",
    }
