# Cycle 3 Stage 6 Infrastructure Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3` (`cycle-000003`)
- **Stage**: `6` (`stage-06`, `infrastructure`)
- **Validated At**: `2026-10-30T06:43:27Z`
- **Implemented Issue**: [#1047](https://github.com/CultureBotAI/NaturalProductMech/issues/1047) (`naturalproductmech-infra-0003`)

## 1. Summary of Implemented Changes

1. **`src/naturalproductmech/curate/claim_references.py`**:
   - Updated `correct_claim_reference` so a structure-corrected row (`row.get("structure_correction_note")`) is permitted when `row.get("structure_source_id")` is non-empty and explicitly named in `decision["rationale"]` (matching `producer_strains` in `scripts/seed_from_sources.py`), and still raises `ValueError(f"{decision['source_id']}: claim references need review after structure correction")` when `structure_source_id` is absent or omitted from `decision["rationale"]`.
2. **`tests/test_claim_references.py`**:
   - Extended `test_decision_cannot_silently_disappear_or_cross_identity` (`"structure_unacknowledged_chebi"`) to verify that a structure-corrected row with `structure_source_id="CHEBI:18208"` is rejected when `CHEBI:18208` is omitted from `decision["rationale"]`.
   - Added `test_structure_corrected_row_accepted_when_rationale_names_structure_source_id` verifying that when `row["structure_source_id"]` (`"CHEBI:18208"`) is explicitly named in `decision["rationale"]`, `seed.build_records` succeeds and retains the routed `DATABASE_ASSERTION`, the structure-correction `CURATOR_INFERENCE`, and the citation-routing `CURATOR_INFERENCE` on both `producer_organisms` and `biosynthetic_gene_clusters` (`34 passed` total in `tests/test_claim_references.py`).
3. **`docs/CURATION.md` & `INFRA_TASKS.md`**:
   - Documented in `docs/CURATION.md` under `## MIBiG claim-specific reference corrections` that a concurrent structure replacement is rejected unless `rationale` explicitly names the replacement target `structure_source_id` (`CHEBI:...`).
   - Updated `INFRA_TASKS.md` so `naturalproductmech-infra-0003` has `status: resolved` with full resolution evidence.

## 2. Validation Gate Results

| Validation Gate | Command | Result |
| --- | --- | --- |
| Ruff lint | `.venv/bin/python -m ruff check --no-cache src/naturalproductmech/curate/claim_references.py tests/test_claim_references.py` | `All checks passed!` (exit `0`) |
| Claim reference unit tests | `.venv/bin/python -m pytest tests/test_claim_references.py -q` | `34 passed` (exit `0`) |
| Full pytest suite | `.venv/bin/python -m pytest -p no:cacheprovider -q` | `1060 passed, 3 skipped` (exit `0`) |
| Seeder reproduction gate | `.venv/bin/python scripts/check_reproduction.py` | `corpus reproduction OK: 3116 records are byte-identical to what the seeder builds from data/raw/` (exit `0`) |
| Corpus & lockfile integrity | `.venv/bin/python scripts/verify_corpus.py` | `lockfile integrity OK: 3116 records, each filed where PATHS.tsv pins it` (exit `0`) |
| Documentation statistics check | `.venv/bin/python scripts/check_docs.py --check` | `README statistics block is current` (exit `0`) |
| Structured review contract check | `.venv/bin/python scripts/record_review.py check` | `{"repository": "CultureBotAI/NaturalProductMech", "valid_reviews": 102, "coverage": "declared_scopes_only"}` (exit `0`) |
