# Cycle 2 Stage 6 Infrastructure Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2` (`cycle-000002`)
- **Stage**: `6` (`stage-06`, `infrastructure`)
- **Validated At**: `2026-10-23T17:18:01Z`
- **Implemented Issue**: [#1015](https://github.com/Knowledge-Graph-Hub/NaturalProductMech/issues/1015) (`naturalproductmech-infra-0002`)

## 1. Summary of Implemented Changes

1. **`src/naturalproductmech/curate/structure_corrections.py`**:
   - Added `REPLACE_SHARED_WITH_CHEBI` to `ALLOWED_ACTIONS`.
   - Extended `apply_structure_corrections` to validate and apply atomic multi-row structure replacements for shared upstream `standard_inchi_key` groups:
     - Requires `source_keys[old_key] >= 2`.
     - Requires complete group coverage (`count == source_keys[old_key]` and `remaining_source_keys[old_key] == 0`).
     - Rejects mixed structure-correction actions (`REPLACE_SHARED_WITH_CHEBI` + `SPLIT_SHARED_WITH_CHEBI`) on the same `old_key`.
     - Requires identical `(target_chebi_id, expected_target_row_sha256, standard_inchi, stereo_complete)` across all rows in the group.
     - Rejects `new_key` collisions across distinct `old_key` groups while permitting rows within the same `REPLACE_SHARED_WITH_CHEBI` group to share `new_key`.
     - Records `structure_correction_old_key = old_key` on each replaced row so `scripts/seed_from_sources.py` sets `_previous_standard_inchi_key = old_key` and enforces explicit owner migration if an old owner file remains on disk.
2. **`scripts/seed_from_sources.py`**:
   - Consolidated `structure_correction_note` and `structure_correction_reference` across all corrected rows contributing to a record into a single `discussion_id: source-structure-correction` entry, preserving every row's note and evidence item without emitting duplicate `discussion_id` entries when multiple rows merge under `REPLACE_SHARED_WITH_CHEBI`.
3. **`tests/test_structure_corrections.py`**:
   - Added 5 unit tests (`78 passed` total in `tests/test_structure_corrections.py`) covering:
     - `test_replace_shared_requires_shared_source_key`
     - `test_replace_shared_rejects_partial_group_or_mixed_actions`
     - `test_replace_shared_rejects_disagreeing_target_chemistry`
     - `test_replace_shared_rejects_target_collision_with_other_source_key`
     - `test_replace_shared_structure_replaces_entire_shared_group_atomically`
4. **`docs/CURATION.md` & `INFRA_TASKS.md`**:
   - Documented `REPLACE_SHARED_WITH_CHEBI` in `docs/CURATION.md`.
   - Updated `INFRA_TASKS.md` so `naturalproductmech-infra-0002` has `status: resolved` with full resolution evidence.

## 2. Validation Gate Results

| Validation Gate | Command | Result |
| --- | --- | --- |
| Ruff lint | `.venv/bin/python -m ruff check --no-cache src/naturalproductmech/curate/structure_corrections.py scripts/seed_from_sources.py tests/test_structure_corrections.py` | `All checks passed!` (exit `0`) |
| Structure correction unit tests | `.venv/bin/python -m pytest tests/test_structure_corrections.py -q` | `78 passed` (exit `0`) |
| Full pytest suite | `.venv/bin/python -m pytest -q` | `1053 passed, 3 skipped` (exit `0`) |
| Seeder reproduction gate | `.venv/bin/python scripts/check_reproduction.py` | `corpus reproduction OK: 3116 records are byte-identical to what the seeder builds from data/raw/` (exit `0`) |
| Corpus & lockfile integrity | `.venv/bin/python scripts/verify_corpus.py` | `lockfile integrity OK: 3116 records, each filed where PATHS.tsv pins it` (exit `0`) |
| Documentation statistics check | `.venv/bin/python scripts/check_docs.py --check` | `README statistics block is current` (exit `0`) |
| Structured review contract check | `.venv/bin/python scripts/record_review.py check` | `{"repository": "CultureBotAI/NaturalProductMech", "valid_reviews": 99, "coverage": "declared_scopes_only"}` (exit `0`) |
