"""Every claw-governed artifact matches claw's manifest at the pinned ref — offline.

Why this exists (#51). `just vendored-sync` resolves this repository's identity
through claw's consumer registry *before* it compares a single byte, and
NaturalProductMech is not registered until M4 admission. Until then that gate
tests registration and nothing else: eleven of the thirteen fleet-wide
artifacts had no drift guard at all, because ``tests/test_schema.py`` hash-pins
the two schema modules only. The checker itself, its launcher, the id-label
validator, ``chem_formula.py`` and five vendored contract tests could be edited
on ``main`` with every gate green.

``scripts/.vendored_manifest.json`` is claw's ``vendored_artifacts.json`` at the
commit in ``scripts/.vendored_canon_ref``, committed byte-for-byte. These tests
run the checker's own comparison — its fail-closed ``parse_manifest``, its
``expand_target`` — against that snapshot, with identity replaced by a synthetic
consumer whose package path is this repository's. Bytes and mode, per artifact.

A re-pin is three things in one PR: advance the ref, re-snapshot the manifest,
re-vendor whatever the new manifest hashes differently. The network test at the
bottom is what keeps the snapshot honest.

When admission lands, ``just vendored-sync`` joins ``just qc`` and these stay: a
pinned snapshot proves this repository has not drifted, the live check proves
the fleet has not, and ``test_this_repository_is_not_yet_a_registered_consumer``
flips to tell whoever is holding the PR that the gate can now be added.
"""

from __future__ import annotations

import hashlib
import importlib.util
import sys
import urllib.error
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = REPO_ROOT / "scripts" / ".vendored_manifest.json"
PACKAGE_PATH = "src/naturalproductmech"


def _load_checker():
    name = "check_vendored_sync"
    spec = importlib.util.spec_from_file_location(
        name, REPO_ROOT / "scripts" / "check_vendored_sync.py")
    module = importlib.util.module_from_spec(spec)
    # ``@dataclass`` resolves annotations through ``sys.modules[cls.__module__]``,
    # so an unregistered standalone module fails to import on Python 3.13.
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


checker = _load_checker()
MANIFEST = checker.parse_manifest(SNAPSHOT.read_bytes())
CONSUMER = checker.Consumer(
    key="naturalproductmech",
    github="CultureBotAI/NaturalProductMech",
    package_path=PACKAGE_PATH,
)
APPLICABLE = MANIFEST.artifacts_for(CONSUMER)


def test_snapshot_is_the_canonical_repository_manifest():
    assert MANIFEST.canonical_repository == checker.CANONICAL_REPOSITORY
    assert MANIFEST.pin_path == checker.DEFAULT_PIN_PATH


def test_pin_file_is_well_formed():
    """``read_pin`` is the checker's own reader: regular file, not executable,
    exactly one 40-character SHA, nothing else."""
    assert len(checker.read_pin(REPO_ROOT)) == 40


def test_this_repository_is_a_registered_consumer():
    """Admission landed at the pinned ref (culturebotai-claw#395, 2026-09-11).
    Until then this test asserted the opposite, and ``CONSUMER`` above stood in
    for a registry entry that did not exist. Now the registry is authoritative
    and the constant is checked against it, so a drift in either direction --
    a renamed package path here, or a re-registration there -- fails here."""
    registered = MANIFEST.consumer_for("CultureBotAI/NaturalProductMech")
    assert registered.key == CONSUMER.key
    assert registered.github == CONSUMER.github
    assert registered.package_path == CONSUMER.package_path


def test_every_fleet_wide_artifact_applies_here():
    """An artifact with no consumer restriction is governed for every Mech,
    admitted or not. Nothing fleet-wide may be silently out of scope."""
    fleet_wide = {a for a in MANIFEST.artifacts if not a.consumers}
    assert fleet_wide, "manifest declares no fleet-wide artifacts"
    assert fleet_wide <= set(APPLICABLE)


@pytest.mark.parametrize("artifact", APPLICABLE, ids=lambda a: a.artifact_id)
def test_governed_artifact_matches_the_manifest_at_the_pin(artifact):
    """Bytes and mode. A missing file is drift too: a newer manifest that
    governs a new artifact fails here until that artifact is vendored."""
    relative = checker.expand_target(artifact, CONSUMER)
    target = REPO_ROOT / relative
    assert target.is_file(), f"{artifact.artifact_id}: {relative} is not vendored"
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    assert digest == artifact.sha256, (
        f"{relative} has drifted from claw at {checker.read_pin(REPO_ROOT)}; "
        f"change it in claw and re-pin, do not edit it here"
    )
    mode = target.stat().st_mode & 0o777
    assert mode == artifact.mode, f"{relative}: mode {mode:o} != manifest {artifact.mode:o}"


def test_snapshot_matches_claw_at_the_pin():
    """Network. Proves the committed snapshot is what claw holds at the pinned
    commit, so the offline comparisons above are against the real manifest and
    not a stale or hand-edited copy. Skips only when the fetch itself fails —
    a mismatch is a failure, not a skip."""
    pin = checker.read_pin(REPO_ROOT)
    url = checker.raw_url(pin, checker.CANONICAL_MANIFEST_PATH)
    try:
        canonical = checker.fetch_url(url)
    except (checker.CanonicalFetchError, urllib.error.URLError, OSError) as exc:
        pytest.skip(f"could not reach claw: {exc}")
    assert canonical == SNAPSHOT.read_bytes(), (
        "scripts/.vendored_manifest.json is not claw's manifest at the pin; "
        "re-snapshot it when re-pinning"
    )
