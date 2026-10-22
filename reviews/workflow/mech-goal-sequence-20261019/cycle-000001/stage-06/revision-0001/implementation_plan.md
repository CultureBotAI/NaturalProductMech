# Stage 6 Infrastructure Implementation Plan — Cycle 1

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Source Revision (`main`)**: `0c3046c72a70a53898c94e403bf4daa7f1e25f1a`
- **Scope Frozen At**: `2026-10-22T04:52:54Z`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md`
- **Frozen Snapshot SHA-256**: `72912d45e04c287bdd1dd1324b4a047fcb8950b60de781f8b16197ce79552a40`

## 1. Frozen Intake Inventory & Dependency Graph

At the `2026-10-22T04:52:54Z` cutoff, `INFRA_TASKS.md` contains one non-resolved infrastructure task:

| Task ID | Issue | Priority | Dependencies | Frozen Status | Target Stage 6 Status |
|---|---|---|---|---|---|
| `naturalproductmech-infra-0001` | [CultureBotAI/NaturalProductMech#999](https://github.com/CultureBotAI/NaturalProductMech/issues/999) | P2 | None | `note` | `resolved` |

No other tasks are open, noted, or deferred in the frozen ledger. `naturalproductmech-infra-0001` has no blocking upstream dependencies and is selected for full implementation and closure in Stage 6.

## 2. Technical Analysis & Implementation Design for `naturalproductmech-infra-0001` (#999)

### 2.1 Part A: Canonicalizing Top-Level Key Order in `write_validated_natural_product`

#### Problem Statement
`scripts/seed_from_sources.py` constructs `NaturalProductRecord` dictionaries in a deterministic slot sequence:
1. Core compound and source-seeded fields (`identifier`, `label`, `chemical_structure`, `np_pathway`, `biosynthesis_origin`, `definition`, `definition_source`, `synonyms`, `np_classification`, `occurrence_taxon_groups`, `occurrences`, `bioactivities`, imported `molecular_targets`, `related_records`, `bioactivity_summary`, `bgc_class`, `compound_classes`, `xrefs`, `producer_taxon_groups`, `producer_organisms`, `biosynthetic_gene_clusters`, `source_concepts`, `grounding_status`, `grounding_notes`, `curation_status`).
2. Source-generated `discussions` (such as `source-structure-correction` or `host-symbiont-*`), emitted immediately after `curation_status` whenever at least one source-generated discussion thread is present.
3. Carried curator-owned sections from `CURATOR_OWNED_CARRIED_FIELDS` (`biosynthetic_pathway`, `causal_graphs`, `causal_graph_refs`), plus curator-only `molecular_targets` (when no imported targets exist) before `biosynthetic_pathway` and curator-only `discussions` (when all `discussion_id` values begin with `curator-`) after `causal_graph_refs`.
4. `curation_history` last.

Previously, `emit_natural_product_yaml` and `write_validated_natural_product` in `src/naturalproductmech/validation/write_validated.py` serialized caller dictionaries directly in their Python insertion order (`sort_keys=False`). If a curation script added `biosynthetic_pathway` or `causal_graphs` to a record before a source-generated `discussions` block (or appended `curation_history` before adding a new curator section), `write_validated_natural_product` succeeded and LinkML validation passed, but `scripts/check_reproduction.py` failed with a top-level key-ordering diff against the re-seeded payload.

Additionally, `tests/test_seed_skeleton.py::test_reseed_preserves_evidence_aliases_across_curator_sections` explicitly tests that intentionally shared in-memory `evidence` list references across curator-owned sections are preserved on re-seed, while `tests/test_write_validated.py::test_emission_options_are_shared_not_reimplemented` enforces that `EMIT_OPTS` remains `{"default_flow_style": False, "sort_keys": False, "allow_unicode": True}`.

#### Design & Acceptance Criteria
1. Implement `canonicalize_top_level_keys(doc: dict[str, Any]) -> dict[str, Any]` in `src/naturalproductmech/validation/write_validated.py`:
   - For component `CausalGraphDocument` payloads (`"record_id" in doc and "graph" in doc`), emit `record_id`, `standard_inchi_key`, `graph`, any additional slots in relative order, and `curation_history` last.
   - For `NaturalProductRecord` payloads, distinguish:
     - `has_imported_targets`: at least one `molecular_targets` entry has `source != "CURATOR"` (placed after `bioactivities`, before `related_records`) vs. curator-only `molecular_targets` (placed after `curation_status` and any source-generated `discussions`, before `biosynthetic_pathway`).
     - `has_source_discussions`: at least one `discussions` entry has a `discussion_id` that is not a `curator-<id>` thread (placed immediately after `curation_status`, before carried curator sections) vs. curator-only `discussions` (placed after `causal_graph_refs`, before `curation_history`).
   - Preserve exact value object references (`ordered[key] = doc[key]`) so intentional in-memory object sharing tested by `test_reseed_preserves_evidence_aliases_across_curator_sections` is untouched.
2. Call `canonicalize_top_level_keys(doc)` inside `emit_natural_product_yaml(doc, yaml_kwargs)`.
3. Verify zero key-order mismatches across all 3,116 records in `data/natural_products/` and all component files in `data/causal_graphs/`.
4. Add unit tests in `tests/test_write_validated.py` covering out-of-order insertion of:
   - source-generated `discussions` vs. `biosynthetic_pathway` and `causal_graphs`
   - curator-only `discussions` vs. `biosynthetic_pathway` and `causal_graphs`
   - imported vs. curator-only `molecular_targets`
   - `curation_history` inserted before curator mutations
   - `CausalGraphDocument` top-level keys.

### 2.2 Part B: Evaluation of Multi-Component Enzyme Support in `PathwayStep`

#### Problem Statement
In `src/naturalproductmech/schema/naturalproductmech.yaml`, `PathwayStep` defines single-valued `enzyme_id` (`range: curie`) and `enzyme_label` (`range: string`). Certain biosynthetic steps are catalyzed by obligate two-component enzyme systems that lack a ComplexPortal entry — notably the *Streptomyces venezuelae* `DesVII`/`DesVIII` macrolide glycosyltransferase complex (`UniProtKB:Q9ZGH7` catalytic glycosyltransferase subunit + `UniProtKB:Q9ZGH8` auxiliary tautomerase/chaperone subunit) in `narbomycin`, `pikromycin`, `methymycin`, and `neomethymycin`.

#### Architectural Evaluation & Decision
We evaluated two options:
- **Option 1 (Schema extension)**: Add an optional multivalued `auxiliary_proteins` slot to `PathwayStep` in `src/naturalproductmech/schema/naturalproductmech.yaml`.
- **Option 2 (Retain single catalytic subunit in `PathwayStep` + explicit `PROTEIN_COMPLEX` assembly in `causal_graphs`, documented in `docs/CURATION.md`)**: Keep `PathwayStep.enzyme_id` and `enzyme_label` single-valued for the catalytic subunit (or ComplexPortal CURIE when one exists), name any obligate auxiliary subunit in `PathwayStep.notes`, and model both subunits (`ENZYME` / `PROTEIN` nodes with `protein_examples`) and their assembly (`PART_OF` / `BINDS` edges into a `PROTEIN_COMPLEX` node) in `causal_graphs`.

**Decision**: Adopt **Option 2**.
- **Rationale**:
  1. `PathwayStep` is a flat tabular summary of sequential reactions (`step_number`, `enzyme_id`, `enzyme_label`, `reaction_id`, `substrate`, `product`), whereas `causal_graphs` is the repository's dedicated mechanistic representation for multi-component assembly, regulatory/chaperone roles, and directional causal edges (`PART_OF`, `BINDS`, `CATALYZES`).
  2. Duplicating subunit lists inside `PathwayStep` would create a second unlinked place to maintain `UniProtKB` groundings without capturing how the auxiliary protein interacts with the catalytic subunit.
  3. All four macrolide glycoside records (`narbomycin`, `pikromycin`, `methymycin`, `neomethymycin`) already follow Option 2 cleanly and pass closed-schema LinkML validation, OAK label correspondence, and `record_review.py` audits.
- **Documentation Deliverable**: Document this convention explicitly in `docs/CURATION.md` under `### Inline record writes` alongside the new `canonicalize_top_level_keys` guarantee.

## 3. Carry-Forward & Deferred Tasks

- **Carried forward / deferred tasks**: None (`carry_forward_ids: []`).
- All tasks in the frozen `INFRA_TASKS.md` snapshot (`naturalproductmech-infra-0001`) are resolved in this stage.
