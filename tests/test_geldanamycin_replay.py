"""Standalone evidence replay must bind snapshots to the claimed Git owners."""

import json
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "reviews/evidence/20261014-geldanamycin"
spec = spec_from_file_location("geldanamycin_replay", PACK / "replay_sources.py")
replay = module_from_spec(spec)
spec.loader.exec_module(replay)
BASE = "06fe27d721baac64909b12adc272528735c5a30a"


def test_retained_snapshots_match_historical_owners():
    replay.verify_owner_snapshots(ROOT, PACK, BASE)


@pytest.mark.parametrize("field", ["label", "chemical_structure", "causal_graphs"])
def test_internally_consistent_snapshot_cannot_replace_historical_owner(tmp_path, field):
    for slug in ("geldanamycin-2", "geldanamycin"):
        data = json.loads((PACK / (slug + "-resolved.json")).read_text())
        if slug == "geldanamycin-2":
            data[field] = "different revision"
        (tmp_path / (slug + "-resolved.json")).write_text(json.dumps(data))
    with pytest.raises(ValueError, match="exact historical inline owner"):
        replay.verify_owner_snapshots(ROOT, tmp_path, BASE)


def test_graph_refs_cannot_be_silently_treated_as_inline(monkeypatch, tmp_path):
    owner = {"label": "test", "causal_graph_refs": ["external"]}
    monkeypatch.setattr(replay.subprocess, "check_output", lambda args: yaml.safe_dump(owner).encode())
    (tmp_path / "geldanamycin-2-resolved.json").write_text(json.dumps(owner))
    with pytest.raises(ValueError, match="exact historical inline owner"):
        replay.verify_owner_snapshots(ROOT, tmp_path, BASE)
