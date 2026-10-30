# Cycle 3 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3` (`cycle-000003`)
- **Stage**: `6` (`stage-06`, `infrastructure`)
- **Frozen `INFRA_TASKS.md` Cutoff**: `2026-10-30T06:21:01Z`
- **Frozen `INFRA_TASKS.md` SHA-256**: `eb12fdfbb7424d5f010501d1be4c50c4a24cab868f86dfa0ae24a9bfda44559d`
- **Frozen Task Count**: `3` (`naturalproductmech-infra-0001` resolved in Cycle 1 Stage 6; `naturalproductmech-infra-0002` resolved in Cycle 2 Stage 6; `naturalproductmech-infra-0003` open and selected for implementation in Cycle 3 Stage 6)

## 1. Frozen Intake Inventory and Dependency Analysis

| Task ID | Origin Goal | Status at Cutoff | GitHub Issue | Dependencies | Selected Disposition |
| --- | --- | --- | --- | --- | --- |
| `naturalproductmech-infra-0001` | `mech-goal-sequence-20261019 / cycle-000001 / stage-02 (causal_graphs)` | `resolved` | [#999](https://github.com/CultureBotAI/NaturalProductMech/issues/999) | None | Retained as `resolved` (implemented and verified in PR [#1014](https://github.com/CultureBotAI/NaturalProductMech/pull/1014)) |
| `naturalproductmech-infra-0002` | `mech-goal-sequence-20261019 / cycle-000002 / stage-01 (add_records)` | `resolved` | [#1015](https://github.com/CultureBotAI/NaturalProductMech/issues/1015) | None | Retained as `resolved` (implemented and verified in PR [#1027](https://github.com/CultureBotAI/NaturalProductMech/pull/1027)) |
| `naturalproductmech-infra-0003` | `mech-goal-sequence-20261019 / cycle-000003 / stage-05 (resolve_review_findings)` | `open` | [#1047](https://github.com/CultureBotAI/NaturalProductMech/issues/1047) | Builds on `naturalproductmech-infra-0002` ([#1015](https://github.com/CultureBotAI/NaturalProductMech/issues/1015)) and `src/naturalproductmech/curate/claim_references.py` | Implement in Cycle 3 Stage 6 and mark `resolved` |

No frozen tasks are deferred or blocked.

## 2. Technical Design for `naturalproductmech-infra-0003` (#1047)

### Problem Statement
In `scripts/seed_from_sources.py` (lines 1119–1124), `producer_strains` permits a structure-corrected MIBiG compound row (`row.get("structure_correction_note")`) when `row.get("structure_source_id")` is non-empty and explicitly named in `qualification["rationale"]`. By contrast, `correct_claim_reference` in `src/naturalproductmech/curate/claim_references.py` (lines 56–57) unconditionally raises `ValueError(f"{decision['source_id']}: claim references need review after structure correction")` whenever `row.get("structure_correction_note")` is present. Because `BGC0000404:1` and `BGC0000405:3` (`benzylpenicillin-sodium.yaml`, `CHEBI:51765`) have active `curation/mibig_claim_references.tsv` entries (`#1023`), any structure replacement on those rows is rejected even when the claim-reference rationale explicitly acknowledges the replacement `CHEBI:...` target.

### Design & Invariants
1. **`src/naturalproductmech/curate/claim_references.py`**:
   - Update `correct_claim_reference(claim, row, decision, *, field)` so a row with `row.get("structure_correction_note")` is permitted when `row.get("structure_source_id")` is non-empty and `row["structure_source_id"] in decision["rationale"]`.
   - Continue raising `ValueError(f"{decision['source_id']}: claim references need review after structure correction")` whenever `row.get("structure_correction_note")` is truthy and `row.get("structure_source_id")` is missing/empty or omitted from `decision["rationale"]`.
   - Preserve both the structure-correction `CURATOR_INFERENCE` evidence item (`claim["evidence"][1]`) and the appended citation-routing `CURATOR_INFERENCE` evidence item (`claim["evidence"][-1]`) alongside the routed `DATABASE_ASSERTION` at `claim["evidence"][0]`.
2. **Tests (`tests/test_claim_references.py`)**:
   - Extend `test_decision_cannot_silently_disappear_or_cross_identity` with `"structure_unacknowledged_chebi"` to verify that a structure-corrected row with `structure_source_id="CHEBI:18208"` is still rejected when `CHEBI:18208` is not named in `decision["rationale"]`.
   - Add `test_structure_corrected_row_accepted_when_rationale_names_structure_source_id` verifying that when `row["structure_source_id"]` (`"CHEBI:18208"`) is explicitly named in `decision["rationale"]`, `seed.build_records` succeeds and retains the routed `DATABASE_ASSERTION`, the structure-correction `CURATOR_INFERENCE`, and the citation-routing `CURATOR_INFERENCE` on both `producer_organisms` and `biosynthetic_gene_clusters`.
3. **Documentation (`docs/CURATION.md`) & Ledger (`INFRA_TASKS.md`)**:
   - Document in `docs/CURATION.md` under `## MIBiG claim-specific reference corrections` that a concurrent structure replacement is rejected unless `rationale` explicitly names the replacement target `structure_source_id` (`CHEBI:...`).
   - Update `INFRA_TASKS.md` to mark `naturalproductmech-infra-0003` as `status: resolved` with full resolution evidence.

## 3. Acceptance Criteria and Validation Plan
1. `.venv/bin/python -m ruff check --no-cache src/naturalproductmech/curate/claim_references.py tests/test_claim_references.py` passes with zero errors.
2. `.venv/bin/python -m pytest tests/test_claim_references.py -q` passes (`34 passed`).
3. `.venv/bin/python -m pytest -p no:cacheprovider -q` passes across the entire test suite.
4. `.venv/bin/python scripts/check_reproduction.py` confirms all 3,116 records are byte-identical to what the seeder builds from `data/raw/`.
5. `.venv/bin/python scripts/verify_corpus.py`, `.venv/bin/python scripts/check_docs.py --check`, and `.venv/bin/python scripts/record_review.py check` pass.
6. `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src .venv/bin/python -m kg_microbe_workflows validate-evidence --root . --required-output infra_snapshot --required-output implementation_plan --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/evidence.yaml` passes.
