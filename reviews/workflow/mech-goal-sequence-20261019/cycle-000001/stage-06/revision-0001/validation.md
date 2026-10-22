# Stage 6 Infrastructure Validation Report — Cycle 1

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Source Revision (`main`)**: `0c3046c72a70a53898c94e403bf4daa7f1e25f1a`
- **Scope Frozen At**: `2026-10-22T04:52:54Z`
- **Frozen `INFRA_TASKS.md` Snapshot SHA-256**: `72912d45e04c287bdd1dd1324b4a047fcb8950b60de781f8b16197ce79552a40`

## 1. Validation Summary for `naturalproductmech-infra-0001` (#999)

| Check | Command | Outcome |
|---|---|---|
| Guarded writer unit tests (`tests/test_write_validated.py`) | `.venv/bin/python -m pytest tests/test_write_validated.py -v` | **PASS** (`17 passed` — including 4 new canonical top-level key ordering tests for source vs. curator `discussions`, imported vs. curator-only `molecular_targets`, `curation_history` placement, and `CausalGraphDocument` keys) |
| Seeder & component integration tests | `.venv/bin/python -m pytest tests/test_seed_skeleton.py tests/test_graph_components.py -v` | **PASS** (`199 passed`, including `test_reseed_preserves_evidence_aliases_across_curator_sections` and `test_committed_components_are_complete_reviewable_and_canonical`) |
| Corpus-wide emission parity (`NaturalProductRecord` + `CausalGraphDocument`) | `emit_natural_product_yaml(yaml.safe_load(p.read_text())).encode() == p.read_bytes()` across all corpus and component YAML files | **PASS** (`records=3116 r_diff=0`, `components=246 c_diff=0`) |
| Full corpus reproduction (`scripts/check_reproduction.py`) | `.venv/bin/python scripts/check_reproduction.py` | **PASS** (`corpus reproduction OK: 3116 records are byte-identical to what the seeder builds from data/raw/`) |
| Structured review inventory validation (`scripts/record_review.py check`) | `.venv/bin/python scripts/record_review.py check` | **PASS** (`valid_reviews: 96`, `coverage: declared_scopes_only`) |
| Lint check (`ruff`) | `.venv/bin/python -m ruff check --no-cache src/naturalproductmech/validation/write_validated.py tests/test_write_validated.py` | **PASS** (`All checks passed!`) |

## 2. Detailed Verification Evidence

1. **Top-Level Key Ordering Parity (`src/naturalproductmech/validation/write_validated.py`)**:
   - `canonicalize_top_level_keys(doc)` orders `NaturalProductRecord` top-level slots to match `scripts/seed_from_sources.py` (`carry_existing_curator_owned_fields` / `CURATOR_OWNED_CARRIED_FIELDS`) and `scripts/check_reproduction.py`.
   - Verified across all 3,116 committed records in `data/natural_products/` and all 246 component files in `data/causal_graphs/`: 0 byte diffs when re-emitted through `emit_natural_product_yaml`.
   - Verified in `tests/test_write_validated.py`:
     - `test_source_discussions_canonicalize_before_curator_pathway_and_graphs`: when `curation_history`, `causal_graphs`, `biosynthetic_pathway`, and source-generated `discussions` (`source-structure-correction`) are inserted out of order, `write_validated_natural_product` emits `curation_status` -> `discussions` -> `biosynthetic_pathway` -> `causal_graphs` -> `curation_history`.
     - `test_curator_only_discussions_canonicalize_after_curator_graphs`: when curator-only `discussions` (`curator-producer-attribution`) are inserted before `biosynthetic_pathway` and `causal_graphs`, `write_validated_natural_product` emits `curation_status` -> `biosynthetic_pathway` -> `causal_graphs` -> `discussions` -> `curation_history`.
     - `test_molecular_targets_placement_distinguishes_imported_from_curator_only`: imported `molecular_targets` (`source != "CURATOR"`) emit before `related_records`, whereas curator-only `molecular_targets` (`source == "CURATOR"`) emit after `curation_status`.
     - `test_causal_graph_document_key_order_is_canonicalized`: component `CausalGraphDocument` dicts emit `record_id`, `standard_inchi_key`, `graph`, and `curation_history` last.
2. **Multi-Component Enzyme Convention (`docs/CURATION.md`)**:
   - Documented under `### Inline record writes` in `docs/CURATION.md` that obligate two-component or multi-subunit enzymatic steps lacking a ComplexPortal entry (such as *Streptomyces venezuelae* `DesVII`/`DesVIII`, `UniProtKB:Q9ZGH7` + `UniProtKB:Q9ZGH8`) ground `PathwayStep.enzyme_id` and `enzyme_label` to the primary catalytic subunit, name the auxiliary subunit in `PathwayStep.notes`, and represent both subunits and their assembly in `causal_graphs` (`PROTEIN_COMPLEX` + subunit edges).
3. **Ledger & Issue Reconciliation (`INFRA_TASKS.md`)**:
   - `naturalproductmech-infra-0001` ([CultureBotAI/NaturalProductMech#999](https://github.com/CultureBotAI/NaturalProductMech/issues/999)) is marked `status: resolved` with full resolution evidence and disposition in both `INFRA_TASKS.md` and `evidence.yaml`.
   - Remaining unresolved / deferred tasks: `0` (`carry_forward_ids: []`).
