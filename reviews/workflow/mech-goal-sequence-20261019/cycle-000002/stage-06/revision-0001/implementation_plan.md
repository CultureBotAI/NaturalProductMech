# Cycle 2 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2` (`cycle-000002`)
- **Stage**: `6` (`stage-06`, `infrastructure`)
- **Frozen `INFRA_TASKS.md` Cutoff**: `2026-10-23T16:39:58Z`
- **Frozen `INFRA_TASKS.md` SHA-256**: `9f4566436225fff27bce53bbd6ed8761028b474167e5b9d35a1353946bf9ce96`
- **Frozen Task Count**: `2` (`naturalproductmech-infra-0001` previously resolved in Cycle 1 Stage 6; `naturalproductmech-infra-0002` open and selected for implementation in Cycle 2 Stage 6)

## 1. Frozen Intake Inventory and Dependency Analysis

| Task ID | Origin Goal | Status at Cutoff | GitHub Issue | Dependencies | Selected Disposition |
| --- | --- | --- | --- | --- | --- |
| `naturalproductmech-infra-0001` | `mech-goal-sequence-20261019 / cycle-000001 / stage-05 (remediation)` | `resolved` | [#999](https://github.com/Knowledge-Graph-Hub/NaturalProductMech/issues/999) | None | Retained as `resolved` (implemented and verified in PR [#1003](https://github.com/Knowledge-Graph-Hub/NaturalProductMech/pull/1003)) |
| `naturalproductmech-infra-0002` | `mech-goal-sequence-20261019 / cycle-000002 / stage-02 (remediation)` | `open` | [#1015](https://github.com/Knowledge-Graph-Hub/NaturalProductMech/issues/1015) | Builds on `src/naturalproductmech/curate/structure_corrections.py` and `scripts/seed_from_sources.py` (which received `SPLIT_SHARED_WITH_CHEBI` in `naturalproductmech-infra-0001`) | Implement in Cycle 2 Stage 6 and mark `resolved` |

No frozen tasks are deferred or blocked.

## 2. Technical Design for `naturalproductmech-infra-0002` (#1015)

### Problem Statement
`src/naturalproductmech/curate/structure_corrections.py` currently supports two actions:
- `REPLACE_WITH_CHEBI`, which requires `source_keys[old_key] == 1` (single-owner replacement).
- `SPLIT_SHARED_WITH_CHEBI`, which requires `source_keys[old_key] >= 2` and `remaining_owners[old_key] >= 1` (so at least one row remains on the upstream `standard_inchi_key`).

During Cycle 2 Stage 1 (`NP_010796` / `BGC0000404:1` + `BGC0000405:3` sharing flat `YGCODSQGfBVMFX-UHFFFAOYSA-N` vs stereochemically complete 3-star `CHEBI:18208` `(4S)-4-hydroxy-1-pyrroline-2-carboxylic acid`) and Cycle 2 Stage 4 (`NP_017987` / `BGC0001053:1` + `BGC0002496:1` sharing flat `HEKGBDCRHYILPL-UHFFFAOYSA-N` vs stereochemically complete 3-star `CHEBI:64109` `nocardicin A`), records were identified where **every** `mibig_compounds.tsv` row sharing the flat upstream `standard_inchi_key` denotes the identical stereochemically complete 3-star ChEBI compound. Neither `REPLACE_WITH_CHEBI` (blocked by `source_keys[old_key] != 1`) nor `SPLIT_SHARED_WITH_CHEBI` (blocked by `remaining_owners[old_key] < 1` and single-`new_key` uniqueness across corrections) can replace all rows sharing `old_key` with the same 3-star ChEBI target.

### Design & Invariants
1. **`src/naturalproductmech/curate/structure_corrections.py`**:
   - Add `"REPLACE_SHARED_WITH_CHEBI"` to `ALLOWED_ACTIONS`.
   - Enforce group completeness and homogeneity for `REPLACE_SHARED_WITH_CHEBI`:
     - `source_keys[old_key]` must be `>= 2`; otherwise raise `ValueError(f"{source_id}: shared structure replacement requires a shared source key")`.
     - Every row in `rows` with `row["standard_inchi_key"] == old_key` must have a corresponding `REPLACE_SHARED_WITH_CHEBI` correction in `corrections` (`remaining_owners[old_key] == 0` and no mixed `SPLIT_SHARED_WITH_CHEBI` / `REPLACE_SHARED_WITH_CHEBI` actions on `old_key`). If any row sharing `old_key` is omitted or uses a different action, raise `ValueError`.
     - All `REPLACE_SHARED_WITH_CHEBI` rows sharing `old_key` must specify identical `(target_chebi_id, expected_target_row_sha256, standard_inchi, stereo_complete)` values; otherwise raise `ValueError`.
     - The target `new_key` must not already exist in `source_keys`, must map to a unique 3-star ChEBI row in `chebi_rows`, and must not collide with any correction for a *different* `old_key` (`new_keys_by_old_key`).
   - Record `result[index]["structure_correction_old_key"] = old_key` on each replaced row (matching `REPLACE_WITH_CHEBI`, since no row remains on `old_key` and the old record owner is replaced rather than split).
2. **`scripts/seed_from_sources.py`**:
   - When multiple `mibig_compounds.tsv` rows merge into a single corrected record under `REPLACE_SHARED_WITH_CHEBI`, aggregate their `structure_correction_note` and `structure_correction_reference` values into a single `"discussion_id": "source-structure-correction"` entry (preserving every row's note and evidence reference item without emitting duplicate `"discussion_id": "source-structure-correction"` entries on the same record).
   - For single-row corrections (`REPLACE_WITH_CHEBI` and `SPLIT_SHARED_WITH_CHEBI`), the single-discussion output remains byte-for-byte identical.
3. **Tests (`tests/test_structure_corrections.py`)**:
   - Add unit tests covering:
     - Atomic 2-row `REPLACE_SHARED_WITH_CHEBI` replacement in `apply_mibig_structure_corrections` and end-to-end `seed.build_records` consolidation into a single `CHEBI:*` record with both `source_concepts`, both `producer_organisms`, both `biosynthetic_gene_clusters`, `_previous_standard_inchi_key == old_key`, a single `source-structure-correction` discussion containing both evidence items, and LinkML schema validation.
     - Rejection when `REPLACE_SHARED_WITH_CHEBI` is applied to a single-owner key (`source_keys[old_key] == 1`).
     - Rejection when `REPLACE_SHARED_WITH_CHEBI` covers only a subset of rows sharing `old_key` (partial group replacement).
     - Rejection when `REPLACE_SHARED_WITH_CHEBI` rows sharing `old_key` disagree on `target_chebi_id` or chemistry.
     - Rejection when `REPLACE_SHARED_WITH_CHEBI` collides with another correction's `new_key`.
4. **Documentation (`docs/CURATION.md`) & Ledger (`INFRA_TASKS.md`)**:
   - Document `REPLACE_SHARED_WITH_CHEBI` and its atomic group invariants in `docs/CURATION.md` under `## MIBiG structure corrections`.
   - Update `INFRA_TASKS.md` to mark `naturalproductmech-infra-0002` as `status: resolved` with full resolution evidence.

## 3. Validation Plan
1. `uv run ruff check src/naturalproductmech/curate/structure_corrections.py scripts/seed_from_sources.py tests/test_structure_corrections.py`
2. `uv run ruff format --check src/naturalproductmech/curate/structure_corrections.py scripts/seed_from_sources.py tests/test_structure_corrections.py`
3. `uv run pytest -q`
4. `uv run python scripts/check_reproduction.py`
5. `uv run python scripts/verify_corpus.py`
6. `uv run python scripts/check_docs.py --check`
7. `uv run python scripts/record_review.py check`
8. `uv run --with-editable /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe-workflows kg_microbe_workflows validate-evidence --workflow /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/naturalproductmech/effective-workflow.json --manifest reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/evidence.yaml --repo-root /Users/marcin/Documents/VIMSS/ontology/Mechs/NaturalProductMech`
