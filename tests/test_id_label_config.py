"""conf/id_label_targets.yaml is live config for a gate that runs in its own
workflow, not in `just qc`. These run in `just qc` so the config cannot rot
between label-correspondence runs.

Three things can go wrong in it silently: a key the validator does not read
(`exclude_key:` for `exclude_keys:` is a weaker gate behind a green build —
the validator now rejects that, and this proves the rejection runs); a target
glob that matches nothing (`required: true` catches it at run time, but only
at run time); and an exception for an (id, label) pair the corpus no longer
carries, which is dead config nobody will notice until the label drifts back.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG = REPO_ROOT / "conf" / "id_label_targets.yaml"


def _load_validator():
    name = "validate_id_label_correspondence"
    spec = importlib.util.spec_from_file_location(
        name, REPO_ROOT / "scripts" / "validate_id_label_correspondence.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


validator = _load_validator()


def test_config_passes_the_validators_strict_key_check():
    """`load_config` raises SystemExit on any key it does not read."""
    cfg = validator.load_config(CONFIG)
    assert cfg["targets"], "no targets configured"


def test_every_target_glob_matches_at_least_one_file():
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    for target in cfg["targets"]:
        matched = list(REPO_ROOT.glob(target["glob"]))
        assert matched, f"target {target['name']!r}: glob {target['glob']!r} matches nothing"


def _corpus_pairs(pairs: list[list[str]]) -> set[tuple[str, str]]:
    found: set[tuple[str, str]] = set()
    for path in (REPO_ROOT / "data" / "natural_products").rglob("*.yaml"):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        for _locator, curie, label, _waived, _override in validator._walk_yaml(
                doc, [(a, b) for a, b in pairs], path.name):
            found.add((curie, label))
    return found


def test_every_exception_names_a_pair_the_corpus_still_carries():
    """An exception is an exact (id, label) pair. One the corpus no longer
    carries is dead config: delete it, or the next drift back to that label
    is silently accepted."""
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    for target in cfg["targets"]:
        exceptions = target.get("exceptions") or []
        if not exceptions:
            continue
        live = _corpus_pairs(target["pairs"])
        dead = [(e["id"], e["label"]) for e in exceptions if (e["id"], e["label"]) not in live]
        assert not dead, f"target {target['name']!r}: exceptions for pairs not in the corpus: {dead}"


def test_every_exception_states_a_reason():
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    for target in cfg["targets"]:
        for e in target.get("exceptions") or []:
            assert e.get("reason", "").strip(), f"{e['id']}: exception without a reason"


@pytest.mark.parametrize("bad_key", ["exclude_key", "excpetions"])
def test_a_misspelt_target_key_is_rejected(tmp_path, bad_key):
    """The check the validator gained upstream (culturebotai-claw#369), proven
    against this config's shape rather than assumed."""
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    cfg["targets"][0][bad_key] = []
    broken = tmp_path / "targets.yaml"
    broken.write_text(yaml.safe_dump(cfg, allow_unicode=True), encoding="utf-8")
    with pytest.raises(SystemExit):
        validator.load_config(broken)


def test_the_taxonomy_adapter_covers_every_taxon_the_corpus_names():
    """`corpus_taxa.obo` is the id-label gate's NCBITaxon adapter (#64). A
    taxon the corpus names that is missing from it would be reported as
    ID_NOT_FOUND — a fatal verdict at any severity — for a record that is
    perfectly good. The OBO is deliberately a superset of the corpus, so this
    should hold with room to spare; the test is here because a re-seed that
    introduced a new taxon without re-running the taxonomy extractor is
    exactly how it would stop holding.
    """
    obo = REPO_ROOT / "data" / "raw" / "corpus_taxa.obo"
    assert obo.exists(), "corpus_taxa.obo missing; run `just extract-taxonomy`"
    covered = {line[len("id: "):].strip()
               for line in obo.read_text(encoding="utf-8").splitlines()
               if line.startswith("id: ")}

    named: set[str] = set()
    for path in (REPO_ROOT / "data" / "natural_products").rglob("*.yaml"):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        for field, key in (("producer_organisms", "taxon_id"),
                           ("occurrences", "taxon_id"),
                           ("biosynthetic_gene_clusters", "organism_taxon_id"),
                           ("molecular_targets", "taxon_id"),
                           ("bioactivities", "target_organism_id")):
            for item in doc.get(field) or []:
                if item.get(key):
                    named.add(item[key])

    missing = sorted(named - covered)
    assert not missing, (
        f"{len(missing)} taxa the corpus names are absent from the gate's adapter, "
        f"so they would report ID_NOT_FOUND: {missing[:6]}"
    )
