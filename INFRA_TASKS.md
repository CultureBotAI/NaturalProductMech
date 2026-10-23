# NaturalProductMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `naturalproductmech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/NaturalProductMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
- task_id: naturalproductmech-infra-0001
  summary: Canonicalize curator-owned top-level key ordering in write_validated_natural_product and evaluate multi-component enzyme support in PathwayStep
  status: resolved
  issue_url: https://github.com/CultureBotAI/NaturalProductMech/issues/999
  disposition: >-
    Resolved in cycle 1 stage 6 (#999): added canonicalize_top_level_keys in write_validated.py with unit tests and
    documented the single-catalytic-subunit PathwayStep + PROTEIN_COMPLEX causal_graphs convention in docs/CURATION.md.
- task_id: naturalproductmech-infra-0002
  summary: Support atomic multi-row REPLACE_SHARED_WITH_CHEBI structure replacement in structure_corrections.py
  status: resolved
  issue_url: https://github.com/CultureBotAI/NaturalProductMech/issues/1015
  disposition: >-
    Resolved in cycle 2 stage 6 (#1015): added REPLACE_SHARED_WITH_CHEBI in src/naturalproductmech/curate/structure_corrections.py
    and consolidated multi-row structure-correction discussions in scripts/seed_from_sources.py, with 5 unit tests in
    tests/test_structure_corrections.py and documentation in docs/CURATION.md.
```
<!-- mech-infra-tasks:end -->

## Tasks

### `naturalproductmech-infra-0001` — Canonicalize curator-owned top-level key ordering in `write_validated_natural_product` and evaluate multi-component enzyme support in `PathwayStep`

- **Origin**: `mech-goal-sequence-20261019`, cycle `1`, stage `2` (`causal_graphs`, `goal-2193`)
- **Status**: `resolved` (implemented and verified in cycle `1`, stage `6`; tracked in https://github.com/CultureBotAI/NaturalProductMech/issues/999)
- **Priority**: P2
- **Dependencies**: None
- **Evidence paths**:
  - `src/naturalproductmech/validation/write_validated.py` (`canonicalize_top_level_keys`, `emit_natural_product_yaml`, `write_validated_natural_product`)
  - `tests/test_write_validated.py`
  - `docs/CURATION.md`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/implementation_plan.md`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/validation.md`
  - `scripts/seed_from_sources.py` (`carry_existing_curator_owned_fields`, `CURATOR_OWNED_CARRIED_FIELDS`)
  - `scripts/check_reproduction.py`
  - `src/naturalproductmech/schema/naturalproductmech.yaml` (`NaturalProductRecord`, `PathwayStep`)
  - `data/natural_products/carbohydrates/desosamine-2.yaml`
  - `data/natural_products/polyketides/narbomycin.yaml`
  - `data/natural_products/polyketides/pikromycin.yaml`
  - `data/natural_products/polyketides/methymycin.yaml`
  - `data/natural_products/polyketides/neomethymycin.yaml`
- **Observation**:
  1. **Writer key-ordering vs. `check_reproduction.py`**: `scripts/seed_from_sources.py` populates `doc["discussions"]` *before* calling `carry_existing_curator_owned_fields` (which appends `biosynthetic_pathway`, `causal_graphs`, and `causal_graph_refs` from `CURATOR_OWNED_CARRIED_FIELDS` immediately before `curation_history`). However, `write_validated_natural_product` (`src/naturalproductmech/validation/write_validated.py`) serializes dict keys in the caller's insertion order (`sort_keys=False`) without canonicalizing top-level slot order. If a curation script inserts `biosynthetic_pathway` or `causal_graphs` before `discussions`, `write_validated_natural_product` succeeds, `verify_corpus.py` passes, and `validate_id_label_correspondence.py` passes, but `scripts/check_reproduction.py` fails with a line-level ordering diff (`expected 'discussions:', found 'biosynthetic_pathway:'`).
  2. **Two-component enzymatic steps in `PathwayStep`**: In `src/naturalproductmech/schema/naturalproductmech.yaml`, `PathwayStep` defines single-valued `enzyme_id` (`range: curie`) and `enzyme_label` (`range: string`) without `multivalued: true` or an `auxiliary_proteins` / `protein_complex` slot. For obligate two-component enzyme systems that lack a ComplexPortal entry — such as the *Streptomyces venezuelae* `DesVII`/`DesVIII` macrolide glycosyltransferase complex (`UniProtKB:Q9ZGH7` catalytic subunit + `UniProtKB:Q9ZGH8` auxiliary chaperone/tautomerase subunit) curated in `narbomycin`, `pikromycin`, `methymycin`, and `neomethymycin` — `PathwayStep.enzyme_id` can only ground the catalytic subunit (`UniProtKB:Q9ZGH7`), while the auxiliary subunit (`UniProtKB:Q9ZGH8`) and complex assembly must be represented in `causal_graphs` (`PROTEIN_COMPLEX` + `ENZYME` / `PROTEIN` -> `PROTEIN_COMPLEX` edges) and `PathwayStep.notes`.
- **Desired outcome**:
  1. Update `write_validated_natural_product` in `src/naturalproductmech/validation/write_validated.py` (with unit tests) to canonicalize top-level `NaturalProductRecord` slot ordering to match `seed_from_sources.py` and clone shared nested structures before `yaml.safe_dump` so YAML anchors (`&id001` / `*id001`) are never emitted.
  2. Evaluate at Stage 6 whether `PathwayStep` should remain single-enzyme-grounded (deferring multi-subunit assembly to `causal_graphs`) or add an optional multivalued `auxiliary_proteins` / `coenzymes` slot.
- **Resolution & Disposition**:
  1. Implemented `canonicalize_top_level_keys(doc)` in `src/naturalproductmech/validation/write_validated.py` and wired it into `emit_natural_product_yaml` / `write_validated_natural_product`. It enforces exact top-level key parity with `scripts/seed_from_sources.py` across all 3,116 `NaturalProductRecord` files and component `CausalGraphDocument` files while preserving existing value object references (satisfying `tests/test_seed_skeleton.py::test_reseed_preserves_evidence_aliases_across_curator_sections`). Added 4 unit tests in `tests/test_write_validated.py`.
  2. Evaluated `PathwayStep` multi-component enzyme modeling: retained single-valued `PathwayStep.enzyme_id` / `enzyme_label` for the catalytic subunit and documented the canonical `PathwayStep` + `causal_graphs` (`PROTEIN_COMPLEX` with subunit edges) pattern in `docs/CURATION.md`.

### `naturalproductmech-infra-0002` — Support atomic multi-row `REPLACE_SHARED_WITH_CHEBI` structure replacement in `structure_corrections.py`

- **Origin**: `mech-goal-sequence-20261019`, cycle `2`, stage `1` (`add_records`, `goal-5690`)
- **Status**: `resolved` (implemented and verified in cycle `2`, stage `6`; tracked in https://github.com/CultureBotAI/NaturalProductMech/issues/1015)
- **Priority**: P2
- **Dependencies**: None
- **Evidence paths**:
  - `src/naturalproductmech/curate/structure_corrections.py` (`ALLOWED_ACTIONS`, `apply_structure_corrections`)
  - `scripts/seed_from_sources.py` (`build_records`)
  - `curation/mibig_structure_corrections.tsv`
  - `tests/test_structure_corrections.py`
  - `docs/CURATION.md`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/implementation_plan.md`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/validation.md`
  - `data/raw/mibig_compounds.tsv` (`BGC0000404:1`, `BGC0000405:3`, `BGC0002095:2`, `BGC0002134:1`, `BGC0000076:1`, `BGC0000077:1`, `BGC0000955:1`, `BGC0001415:1`)
  - `data/raw/chebi_structures.tsv` (`CHEBI:18208`, `CHEBI:51765`, `CHEBI:6426`, `CHEBI:83275`, `CHEBI:157683`)
  - `data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml`
  - `data/natural_products/amino_acids_and_peptides/isopenicillin-n.yaml`
  - `data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml`
  - `data/natural_products/amino_acids_and_peptides/leupeptin-a.yaml`
- **Observation**:
  1. During the Cycle 2 Stage 1 bounded-frontier audit of all 230 shared-InChIKey groups in `data/raw/mibig_compounds.tsv` against 3-star ChEBI structures in `data/raw/chebi_structures.tsv`, we found that `src/naturalproductmech/curate/structure_corrections.py` supports only two actions:
     - `REPLACE_WITH_CHEBI`, which requires `len(by_inchi_key[old_key]) == 1` (single-row upstream InChIKey), and
     - `SPLIT_SHARED_WITH_CHEBI`, which requires `len(by_inchi_key[old_key]) >= 2` and removes one row at a time from `by_inchi_key[old_key]`, requiring at least one row to remain on the upstream InChIKey.
  2. When multiple MIBiG rows share the same upstream salt, stereo-incomplete, or wrong-connectivity InChIKey for the **same** natural product and a 3-star ChEBI structure exists — such as `BGC0000404:1` (`penicillin`) + `BGC0000405:3` (`benzylpenicillin`) sharing the sodium salt `FCPVYOBCFFNJFS-LQDWTQKMSA-M` (`CHEBI:51765`) instead of the neutral parent `CHEBI:18208`, or `BGC0002095:2` (`leupeptin Ac`) + `BGC0002134:1` (`leupeptin A`) sharing stereo-incomplete `GDBQQVLCIARPGH-BSOSBYQFSA-N` instead of 3-star `CHEBI:6426` — splitting only one row via `SPLIT_SHARED_WITH_CHEBI` would violate the non-duplication rule by creating duplicate records for a single compound, whereas applying `REPLACE_WITH_CHEBI` or `SPLIT_SHARED_WITH_CHEBI` across all rows in the group raises `StructureCorrectionError`.
  3. During Cycle 2 Stage 2 (`causal_graphs`), this structure-correction blocker also prevents curating the terminal `mibig:BGC0000405` *Penicillium chrysogenum* / *Penicillium rubens* Wisconsin 54-1255 acyl-CoA:isopenicillin N acyltransferase step (`PenDE` / `AatA`, `UniProtKB:P15802`, `RHEA:19249`, `CHEBI:18165` `isopenicillin N` -> `CHEBI:18208` `benzylpenicillin` / `CHEBI:58435` `benzylpenicillin(1-)`) onto `data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml` (`CHEBI:51765`), because the record is still grounded to the sodium salt `CHEBI:51765` rather than the neutral parent `CHEBI:18208`. Once `REPLACE_SHARED_WITH_CHEBI` (#1015) replaces `BGC0000404:1` + `BGC0000405:3` with `CHEBI:18208`, the 3-step `PcbAB -> IpnA -> PenDE` `BIOSYNTHESIS` pathway and causal graph can be completed on the neutral `benzylpenicillin` record.
- **Desired outcome**:
  1. Add a group-validated `REPLACE_SHARED_WITH_CHEBI` action in `src/naturalproductmech/curate/structure_corrections.py` (with unit tests in `tests/test_structure_corrections.py` and documentation in `docs/CURATION.md`) that verifies all `mibig_compounds.tsv` rows sharing the upstream `standard_inchi_key` are declared in `curation/mibig_structure_corrections.tsv` with the same `target_chebi_id` and replaces the entire shared group atomically without splitting or stranding a row.
- **Resolution & Disposition**:
  1. Added `REPLACE_SHARED_WITH_CHEBI` to `ALLOWED_ACTIONS` and `apply_structure_corrections` in `src/naturalproductmech/curate/structure_corrections.py`, enforcing shared-key multiplicity (`source_keys[old_key] >= 2`), complete group coverage (`count == source_keys[old_key]` and `remaining_source_keys[old_key] == 0`), action homogeneity per `old_key`, identical target ChEBI and derived chemistry across all rows in the group, and target-key collision rejection across distinct source keys, while recording `structure_correction_old_key = old_key` on each replaced row.
  2. Updated `scripts/seed_from_sources.py` so multi-row structure replacements emit a single consolidated `source-structure-correction` discussion preserving every row's `structure_correction_note` and evidence item without duplicate `discussion_id` entries.
  3. Added 5 unit tests in `tests/test_structure_corrections.py` and documented `REPLACE_SHARED_WITH_CHEBI` in `docs/CURATION.md`.
