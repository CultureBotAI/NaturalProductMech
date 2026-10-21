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
  status: note
  issue_url: https://github.com/CultureBotAI/NaturalProductMech/issues/999
  disposition: Recorded during cycle 1 stage 2 (causal_graphs) for stage 6 triage
```
<!-- mech-infra-tasks:end -->

## Tasks

### `naturalproductmech-infra-0001` — Canonicalize curator-owned top-level key ordering in `write_validated_natural_product` and evaluate multi-component enzyme support in `PathwayStep`

- **Origin**: `mech-goal-sequence-20261019`, cycle `1`, stage `2` (`causal_graphs`, `goal-2193`)
- **Status**: `note` (pending Stage 6 implementation triage; tracked in https://github.com/CultureBotAI/NaturalProductMech/issues/999)
- **Priority**: P2
- **Dependencies**: None
- **Evidence paths**:
  - `src/naturalproductmech/validation/write_validated.py` (`write_validated_natural_product`)
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

