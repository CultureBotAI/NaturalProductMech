# Local evidence review: daptomycin

- Review: 20261105T202323Z-daptomycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T19:33:20.883636Z
- Finished UTC: 2026-11-05T20:23:23.369506Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Daptomycin retains consistent normalized identifiers and an encoded cyclic lipo-depsipeptide topology. Canonical representation differences and source-level producer/locus grades remain explicit; no clinical mechanism is inferred.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2594; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-d4998c3d5b | data/natural_products/unclassified/daptomycin.yaml | generated | daptomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-d4998c3d5b | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-d4998c3d5b | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-d4998c3d5b | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-d4998c3d5b | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-d4998c3d5b | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-d4998c3d5b | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-d4998c3d5b | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-d4998c3d5b | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### identity

identity: supported. Targets: naturalproductmech:mibig-d4998c3d5b.

The minted daptomycin record faithfully maps to BGC0000336 compound 1 and retains its PubChem 21585658 cross-reference. Both original stored forms regenerate DOAKLVKFURWEDJ-QCMAZARJSA-N. These checks support the encoded retained-source association without importing familiar clinical identity or mechanism claims.

### representation

representation: supported. Targets: naturalproductmech:mibig-d4998c3d5b.

C72H101N17O26, net charge 0 and the standard identifiers agree across 115-atom/118-bond forms. The original 31-membered ester-containing macrocycle, 14 amide sites, separate acyl tail and 13 specified tetrahedral centers support a cyclic lipo-depsipeptide representation. Reconstruction expresses 14 C(OH)=N sites and 14 unspecified imine descriptors. Canonical comparisons remain false and the atom map empty; these changes do not establish an erroneous stored form.

### provenance

provenance: supported. Targets: naturalproductmech:mibig-d4998c3d5b.

The source producer Streptomyces filamentosus NRRL11379 (457430) is SOURCE_ASSERTION. BGC0000336/AY787762.1:45828..108856 remains CLUSTER_UNSTATED with no stored experimental locus method. LOTUS S. filamentosus (67294) is separate occurrence naming. Cached labels do not independently verify species/strain rank or ancestry; coordinates alone do not strengthen the evidence grade.

### citations

evidence: supported. Targets: naturalproductmech:mibig-d4998c3d5b.

PMID:15870461 is ENTRY-level MIBiG support; DOI 10.1099/MIC.0.27757-0 belongs to the retained LOTUS occurrence. Neither reference was newly accessed. The citation inventory does not itself establish compound-specific locus demonstration or clinical mechanism.

### occurrence_activity

evidence: supported. Targets: naturalproductmech:mibig-d4998c3d5b.

One LOTUS occurrence names S. filamentosus (67294). No exact retained assay, BindingDB target, ChEBI or related-corpus match is available for this full key. No clinical or mechanistic facts are imported from the familiar name; the saved negatives are limited to the retained tables and query predicates.

### classification

consistency: supported. Targets: naturalproductmech:mibig-d4998c3d5b.

The saved macrocycle contains an ester and multiple amides, with a separate acyl tail, supporting the encoded Cyclic peptides/Depsipeptides/Lipopeptides descriptors. NPClassifier’s broader Polyketides pathway remains model provenance rather than demonstrated biosynthesis. MIBiG NRPS class and Type I subclass are preserved separately.

### completion

completeness: unknown. Targets: naturalproductmech:mibig-d4998c3d5b.

Partial scientific review: complete owner/history, both saved molecular forms and assigned retained source payloads were read. All 44 captured input hashes and ownership declarations were verified against the accepted 455-input/63-path plan. Five local checks passed; full QC and OAK were unavailable. No fresh primary sources, taxonomy request, source query or record edit was made.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2594-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/daptomycin.yaml; Complete plaintext including every curation_history entry | supports | Complete current owner and all 2 history entries were personally read. Historical curator assertions do not confer fresh source-access credit. |
| bgc-2594-capture | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/3 | supports | Actual complete owner capture preserves current local content; it is not an independent scientific validation. |
| bgc-2594-identity | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/3/owner_document/identifier; /records/3/owner_document/label; /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status | supports | Exact stored identity, source concepts, grounding and chemical encodings; natural identity is assessed separately. |
| bgc-2594-history | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/3/owner_document/curation_history | supports | All 2 current history entries retain their original source and curation scope; no inherited paper access is claimed. |
| bgc-2594-provenance | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters; /records/3/owner_document/source_concepts | supports | Owner-specific producer, locus and source-concept assertions preserve their distinct grades and references. |
| bgc-2594-activity-owner | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/3/owner_document/occurrences; /records/3/owner_document/xrefs | supports | Current owner occurrence, activity and cross-reference content is retained at its recorded granularity; no unstated mechanism or potency is inferred. |
| bgc-2594-classification-owner | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/3/owner_document/np_pathway; /records/3/owner_document/biosynthesis_origin; /records/3/owner_document/np_classification; /records/3/owner_document/bgc_class | supports | Recorded classification/model labels and BGC class content; exact source subclasses remain separately visible in the retained MIBiG row. |
| bgc-2594-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/3/owner_document | context_only | This complete captured owner has no causal_graphs, biosynthetic_pathway or declared-component root; there is no applicable maintained-reader result. |
| bgc-2594-intake | /private/tmp/npm-review-work/shared-next-batch260/intakes-001/2594-inspect-001.json; /targets; /source | supports | Actual canonical inspection captures 44 current input hashes and complete target ownership declarations. Hash capture does not imply whole scientific reading of each input table. |
| bgc-2594-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch260/root-intake-acceptance-001.json; /accepted; /status; /summary | supports | ROOT accepted the ten actual canonical inspections and their exact 455-input/63-path scope. |
| bgc-2594-plan | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-target-input-plan-001.json; /records/3; /source_placement_count; /unique_source_path_count | supports | This owner has 44 exact planned inputs, now matched to its accepted actual canonical inspection; the full plan has 455 placements/63 paths. |
| bgc-2594-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch260/root-source-plan-acceptance-001.json; /accepted; /status; /plan | supports | ROOT accepted the original local composed input plan; all current input paths and roles are preserved. |
| bgc-2594-chemistry | /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-DATA-001.json; /records/3 | supports | Both complete saved forms, all atom/bond/ring/motif/stereo fields, comparisons and limited atom correspondence were personally read. No alternative parse was performed. |
| bgc-2594-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /status; /DATA; /execution | supports | ROOT accepted the once-only offline diagnostic execution and saved outputs; this does not establish natural identity or full graph equivalence. |
| bgc-2594-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-execution-001.json; /exit_code; /stdout; /stderr | supports | Actual diagnostic execution closed with exit 0 and preserved original stdout/stderr; no diagnostic replay was made. |
| bgc-2594-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-original-001.stderr; Complete original stderr | context_only | Exactly four original charge-rearrangement warnings are globally retained and are not attributed to an individual owner. |
| bgc-2594-molecular-reading | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-current260-first-five-molecular-intake-reading-001.json; /records/3; /reading_method; /warnings_scope; /limits | supports | Owner-specific complete saved-table reading and interpretation, with normalized identifiers distinguished from canonical correspondence and natural identity. |
| bgc-2594-gates | /private/tmp/npm-review-work/shared-next-batch260/root-native-gates-acceptance-001.json; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /records | supports | Five local checks passed. Full QC and OAK remain unavailable, so native completion and scientific completion are not promoted. |
| bgc-2594-source-reading | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-current260-assigned-source-reading-001.json; /records/3; /full_meaning_scope; /boundaries | supports | Assigned retained-row meanings and all query metadata for this owner were read. References remain retained database assertions rather than newly inspected primary papers. |
| bgc-2594-source-notes | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /reading_boundaries | supports | Original 455-input/63-path source notes preserve disjoint positive-row reading credit 55 BGC + 42 Support + 0 Native. Actual intake acceptance is supported separately. |
| bgc-2594-taxonomy | /private/tmp/npm-review-work/shared-next-batch260-tentative/native-prep/native-current260-cached-taxonomy-reading-001.json; /context_interpretations/6; /interpretation | partial | Owner-local retained taxonomy routes, names and synonyms, with no current rank, lineage or freshness verification. |
| bgc-2594-curation | /private/tmp/npm-review-work/shared-next-batch260-tentative/native-prep/native-current260-implemented-curation-scan-001.json; /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope; /interpretation | context_only | Ignored-inclusive retained curation scope found no exact applicable correction. The producer-strain and row-digest implementation readings retain their bounded scope. |
| bgc-2594-assay-curation | /private/tmp/npm-review-work/shared-next-batch260-tentative/native-prep/native-current260-implemented-curation-scan-001.json; /assay_scope | context_only | The all-context retained exclusion scan covers 19 distinct selected Cystothiazole A tuples and eight blank-AID sentinels, with no exact exclusion. This is the receipt-wide scope, not an owner-specific assay assertion. |
| bgc-2594-direct-contexts | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-target-input-plan-001.json; /records/3/proposed_companion_paths; /records/3/direct_companion_predicates | context_only | This owner has 0 immediate shared-BGC context input(s); the exact predicates do not establish equivalent identity, independent experimental evidence or source transfer. |
| bgc-2594-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2594-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 455-455; raw record sha256 60853689963c9b65651c68c4e689b7df514671e86b6f514849c9544d2e6aa59f | supports | Assigned retained-row reading of all 25 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2594-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2594-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2594-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 1157-1157; raw record sha256 c230bd1bd041d5cca9c039192abf6b1cabfe490217fee9125bd40769b4ef5210 | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2594-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2594-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2594-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 452-452; raw record sha256 2268fbd4be172e31b909ed75bd33c592947664eddb193d2c4a82bd3670fe86b1 | supports | Assigned retained-row reading of all 7 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2594-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/pubchem_bioassay | context_only | Complete saved pubchem_bioassay query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2594-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2594-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2594-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2594-additional-0 | /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained exclusion-table diagnostic context captured for every review; applicable exact assay exclusions and biological rows must be derived from actual retained inventory, not file presence.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2594-additional-1 | /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained unresolved-taxon diagnostic context used by the bounded curation scan; no fresh taxonomy, forward-merge decision or producer confirmation.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2594-additional-2 | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained explicit forward-merge table used by positive and negative taxon queries for each owner; historical route evidence only, no fresh taxonomy.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2594-additional-3 | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_non_organism.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained non-organism table used by positive and negative taxon queries for each owner; diagnostic scope only, not a taxon verdict from file presence.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2594-additional-4 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Maintained exclusion identity, source-row digest and attributed-rationale implementation context; no execution or new assay evidence.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2594-additional-5 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/producer_strains.py; load_producer_strains lines 12-17; _load_qualifications lines 28-62; qualify_producer lines 65-68; _append_evidence lines 78-89 | context_only | Captured additional input role: Maintained producer-strain qualification implementation: source-row and digest predicate, strain-only CURATOR_INFERENCE scope; plaintext dependency, no execution or grade/taxon upgrade.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2594-additional-6 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py; row_digest lines 19-23 only | context_only | Captured additional input role: Maintained row_digest implementation used by qualification guards: sorted ensure_ascii JSON digest only; input presence does not claim an audit or application of other structure-correction behavior.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-260/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-260/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-260/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-260/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-260/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- No newly accessed primary paper or taxonomy authority; retained references and historical curator assertions keep their original scope.
- Full QC and OAK were unavailable. Local gate passes and normalized identifiers do not establish natural identity or experimental mechanism.
- The diagnostic attempts one limited chirality-aware substructure match; empty results and full graph identity limits are retained. Four original charge-rearrangement warnings remain globally scoped.
- Negative source results are bounded by the exact saved query frames; they are not general biological absence claims.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Partial scientific review: complete owner/history, both saved molecular forms and assigned retained source payloads were read. All 44 captured input hashes and ownership declarations were verified against the accepted 455-input/63-path plan. Five local checks passed; full QC and OAK were unavailable. No fresh primary sources, taxonomy request, source query or record edit was made.
- No selected mechanism, pathway, molecular-target or component root applies; maintained-reader checks are not applicable. Native gate status is preserved.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T202323Z-daptomycin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: daptomycin'
started_at: '2026-11-05T19:33:20.883636Z'
finished_at: '2026-11-05T20:23:23.369506Z'
reviewer:
  identity: Codex root with native_checks, bgc_science and review_support peer agents
  kind: agent
  independence: independent
  independence_basis: This review team inspected existing owner and retained source
    bytes without editing them; scientific fragments were cross-checked separately
    from their author. Local validation is not treated as scientific proof.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Daptomycin retains consistent normalized identifiers and an encoded cyclic
  lipo-depsipeptide topology. Canonical representation differences and source-level
  producer/locus grades remain explicit; no clinical mechanism is inferred.
source:
  git_revision: ce6a5498df5be51116bd5e0c119023ee62bb5464
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: AGENTS.md
    sha256: 69e4037f8dc97d4b00bb7bb83b41ceca025f6ef578d5c0bf8086f3400becde0b
    role: context
  - path: conf/id_label_targets.yaml
    sha256: 24235903e0e8df5793a30e92c551082c71c1c67739ea4e3b5fb0f68853a805e6
    role: context
  - path: conf/producer_evidence.tsv
    sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
    role: context
  - path: conf/record_review.yaml
    sha256: e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8
    role: context
  - path: curation/lotus_occurrence_exclusions.tsv
    sha256: d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
    role: context
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: curation/unresolved_taxa.tsv
    sha256: 86efbda9c09388723a4f24da35e18404032f1549a9088192fbd2020cb846fa43
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/unclassified/daptomycin.yaml
    sha256: c955275448d3c77dc28ee1684d0cb27aa2e27e6d97b59d95d72a9c7eeddf25b0
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
    role: context
  - path: data/raw/antibioticmech_inchikeys.tsv
    sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
    role: context
  - path: data/raw/bindingdb_targets.tsv
    sha256: 3cff45281c35a8b14d4d7784bc4b7af80e8e27779a5667a0292f0d9b022a22c1
    role: context
  - path: data/raw/chebi_origins.tsv
    sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
    role: context
  - path: data/raw/chebi_structures.tsv
    sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
    role: context
  - path: data/raw/corpus_taxa.obo
    sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
    role: context
  - path: data/raw/cyanometdb_occurrences.tsv
    sha256: f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8
    role: context
  - path: data/raw/lotus_occurrences.tsv
    sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
    role: context
  - path: data/raw/mibig_compounds.tsv
    sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
    role: context
  - path: data/raw/npclassifier.tsv
    sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
    role: context
  - path: data/raw/pubchem_bioassay.tsv
    sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
    role: context
  - path: data/raw/taxon_merged.tsv
    sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
    role: context
  - path: data/raw/taxon_non_organism.tsv
    sha256: f2c1ee257bbbcb0854528196ab1f809d658c27f1c7b2036f7f71f088b52935bb
    role: context
  - path: docs/CURATION.md
    sha256: c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa
    role: context
  - path: docs/HARMONIZATION.md
    sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
    role: context
  - path: docs/record-review-profile.md
    sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 4f9057e3e54656dd46f2ded4d3a8f0804acad348d2605d436405e1fcfb6af550
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_chebi.py
    sha256: 46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
    role: context
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2594; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-d4998c3d5b
targets:
- target_id: naturalproductmech:mibig-d4998c3d5b
  path: data/natural_products/unclassified/daptomycin.yaml
  label: daptomycin
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained harmonization generator; seeded fields are corrected through
      maintained inputs and validated regeneration.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Retained MIBiG structure, producer and compound-specific locus assertions.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned computed classification and filing assertions.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Maintained extraction of MIBiG compound names, structures, stereochemistry
      flags and source provenance.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Retained cited occurrence assertions, distinct from demonstrated production.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Retained exclusion-table diagnostic context captured for every review; applicable
      exact assay exclusions and biological rows must be derived from actual retained
      inventory, not file presence.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/unresolved_taxa.tsv
    role: Retained unresolved-taxon diagnostic context used by the bounded curation
      scan; no fresh taxonomy, forward-merge decision or producer confirmation.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_merged.tsv
    role: Retained explicit forward-merge table used by positive and negative taxon
      queries for each owner; historical route evidence only, no fresh taxonomy.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_non_organism.tsv
    role: Retained non-organism table used by positive and negative taxon queries
      for each owner; diagnostic scope only, not a taxon verdict from file presence.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Maintained exclusion identity, source-row digest and attributed-rationale
      implementation context; no execution or new assay evidence.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: 'Maintained producer-strain qualification implementation: source-row and
      digest predicate, strain-only CURATOR_INFERENCE scope; plaintext dependency,
      no execution or grade/taxon upgrade.'
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: 'Maintained row_digest implementation used by qualification guards: sorted
      ensure_ascii JSON digest only; input presence does not claim an audit or application
      of other structure-correction behavior.'
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners.
checks:
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  command: just validate-strict data/natural_products/unclassified/cystobactamid-919-1.yaml
    data/natural_products/unclassified/cystobactamid-919-2.yaml data/natural_products/unclassified/cystothiazole-a.yaml
    data/natural_products/unclassified/daptomycin.yaml data/natural_products/unclassified/dehydrodidemnin-b-aplidine.yaml
    data/natural_products/unclassified/deoxyhangtaimycin.yaml data/natural_products/unclassified/depsibosamycin-d.yaml
    data/natural_products/unclassified/deschlorosvetamycin-a.yaml data/natural_products/unclassified/desmamide-a.yaml
    data/natural_products/unclassified/desmamide-b.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-260/validate-strict-selected10-001.tsv
  exit_code: 0
  evidence_ids:
  - root-native-strict_ten
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-strict_full
  name: strict_full
  status: passed
  required: true
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-260/validate-all-001.tsv
  exit_code: 0
  evidence_ids:
  - root-native-strict_full
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-lockfile
  name: lockfile
  status: passed
  required: true
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  command: just verify-corpus --summary
  exit_code: 0
  evidence_ids:
  - root-native-lockfile
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-reproduction
  name: reproduction
  status: passed
  required: true
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  command: just verify-reproduction
  exit_code: 0
  evidence_ids:
  - root-native-reproduction
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-queue
  name: queue
  status: passed
  required: true
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-260/review-queue-001.tsv
  exit_code: 0
  evidence_ids:
  - root-native-queue
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-full-qc
  name: Full just qc
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2594-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/daptomycin.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Complete current owner and all 2 history entries were personally read.
    Historical curator assertions do not confer fresh source-access credit.
  snapshot_sha256: c955275448d3c77dc28ee1684d0cb27aa2e27e6d97b59d95d72a9c7eeddf25b0
- evidence_id: bgc-2594-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/3
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Actual complete owner capture preserves current local content; it is not
    an independent scientific validation.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: bgc-2594-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/3/owner_document/identifier; /records/3/owner_document/label;
    /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts;
    /records/3/owner_document/grounding_status
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Exact stored identity, source concepts, grounding and chemical encodings;
    natural identity is assessed separately.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: bgc-2594-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/3/owner_document/curation_history
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: All 2 current history entries retain their original source and curation
    scope; no inherited paper access is claimed.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: bgc-2594-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters;
    /records/3/owner_document/source_concepts
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Owner-specific producer, locus and source-concept assertions preserve their
    distinct grades and references.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: bgc-2594-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/3/owner_document/occurrences; /records/3/owner_document/xrefs
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Current owner occurrence, activity and cross-reference content is retained
    at its recorded granularity; no unstated mechanism or potency is inferred.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: bgc-2594-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_pathway; /records/3/owner_document/biosynthesis_origin;
    /records/3/owner_document/np_classification; /records/3/owner_document/bgc_class
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Recorded classification/model labels and BGC class content; exact source
    subclasses remain separately visible in the retained MIBiG row.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: bgc-2594-mechanism-absence
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: This complete captured owner has no causal_graphs, biosynthetic_pathway
    or declared-component root; there is no applicable maintained-reader result.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
  search_scope: Exact literal root-presence inspection of this complete captured owner
    only; no molecular mechanism or biological absence inference.
- evidence_id: bgc-2594-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/intakes-001/2594-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Actual canonical inspection captures 44 current input hashes and complete
    target ownership declarations. Hash capture does not imply whole scientific reading
    of each input table.
  snapshot_sha256: acaf400c5f6823897bb7c897da7b97df5527d1eda51a8813205d92cce7daf766
- evidence_id: bgc-2594-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/root-intake-acceptance-001.json
  locator: /accepted; /status; /summary
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: ROOT accepted the ten actual canonical inspections and their exact 455-input/63-path
    scope.
  snapshot_sha256: 48c0dd3874d34a3fe56e6f43d6ecc044efb43d0fed97cf8713507ed05d70ed41
- evidence_id: bgc-2594-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-target-input-plan-001.json
  locator: /records/3; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: This owner has 44 exact planned inputs, now matched to its accepted actual
    canonical inspection; the full plan has 455 placements/63 paths.
  snapshot_sha256: 31543a1f8d8477dfd89c147a1d95a836b39146176a2f6d6f0887c064b79dacc3
- evidence_id: bgc-2594-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/root-source-plan-acceptance-001.json
  locator: /accepted; /status; /plan
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: ROOT accepted the original local composed input plan; all current input
    paths and roles are preserved.
  snapshot_sha256: 32343815aa82a0d56f226d32975ee77e9ab34c667376058dcf1b53d881b61295
- evidence_id: bgc-2594-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Both complete saved forms, all atom/bond/ring/motif/stereo fields, comparisons
    and limited atom correspondence were personally read. No alternative parse was
    performed.
  snapshot_sha256: e9c8abdeb50c79ef4be2bbec545f99015ee724587ba4f9892b51b2e5f0e16258
- evidence_id: bgc-2594-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /status; /DATA; /execution
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: ROOT accepted the once-only offline diagnostic execution and saved outputs;
    this does not establish natural identity or full graph equivalence.
  snapshot_sha256: b394d34147477dca214f38d6a5bb7bc193b47109faa3869755d34a87bacde21d
- evidence_id: bgc-2594-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /stdout; /stderr
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Actual diagnostic execution closed with exit 0 and preserved original stdout/stderr;
    no diagnostic replay was made.
  snapshot_sha256: 06354cc95be3de2c172fc46d09cd63e24d02d4078f16df4fd7497ab7ab70f79b
- evidence_id: bgc-2594-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: Exactly four original charge-rearrangement warnings are globally retained
    and are not attributed to an individual owner.
  snapshot_sha256: e0263f4ce817649b46746d132adabdbe19605d646917a72a73bbca39dfa9ec1b
- evidence_id: bgc-2594-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-current260-first-five-molecular-intake-reading-001.json
  locator: /records/3; /reading_method; /warnings_scope; /limits
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Owner-specific complete saved-table reading and interpretation, with normalized
    identifiers distinguished from canonical correspondence and natural identity.
  snapshot_sha256: fcdac6b7e21ddfd254b25b5de2f39c75fa89227650bb6a1dff357b39f9b0f047
- evidence_id: bgc-2594-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/root-native-gates-acceptance-001.json
  locator: /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /records
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Five local checks passed. Full QC and OAK remain unavailable, so native
    completion and scientific completion are not promoted.
  snapshot_sha256: 20997a8aa70b4d2ffd564963e2dd1e8d9de39018545b1226b31f26f6bf984bb4
- evidence_id: bgc-2594-source-reading
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-current260-assigned-source-reading-001.json
  locator: /records/3; /full_meaning_scope; /boundaries
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Assigned retained-row meanings and all query metadata for this owner were
    read. References remain retained database assertions rather than newly inspected
    primary papers.
  snapshot_sha256: 90a2a40510c5bed5678408808ebc3b19c170e248709ce89098980b3ed8dfb10b
- evidence_id: bgc-2594-source-notes
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Original 455-input/63-path source notes preserve disjoint positive-row
    reading credit 55 BGC + 42 Support + 0 Native. Actual intake acceptance is supported
    separately.
  snapshot_sha256: 740dbb3ff3e48483ca7251ca1d6c0e98d5fb0c1994a38c71045fdcd84d071dc0
- evidence_id: bgc-2594-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/native-prep/native-current260-cached-taxonomy-reading-001.json
  locator: /context_interpretations/6; /interpretation
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: partial
  summary: Owner-local retained taxonomy routes, names and synonyms, with no current
    rank, lineage or freshness verification.
  snapshot_sha256: 341eb459cc59fbcb70393b278b9b5de0cdcf48817d9641c97f49d08ee6e4da50
- evidence_id: bgc-2594-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/native-prep/native-current260-implemented-curation-scan-001.json
  locator: /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope;
    /interpretation
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: Ignored-inclusive retained curation scope found no exact applicable correction.
    The producer-strain and row-digest implementation readings retain their bounded
    scope.
  snapshot_sha256: 1f7fd8a5c9f7bc3fd10d464aa2b443adad2dfc5faf417010b98d0dda8f87b8e8
  search_scope: Nine implemented curation/diagnostic tables among eleven enumerated;
    decisions/source_queue excluded. Exact current context predicates applied after
    broad lexical screening; no general absence claim.
- evidence_id: bgc-2594-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/native-prep/native-current260-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: The all-context retained exclusion scan covers 19 distinct selected Cystothiazole
    A tuples and eight blank-AID sentinels, with no exact exclusion. This is the receipt-wide
    scope, not an owner-specific assay assertion.
  snapshot_sha256: 1f7fd8a5c9f7bc3fd10d464aa2b443adad2dfc5faf417010b98d0dda8f87b8e8
  search_scope: All fifteen retained exclusion decisions under the implemented exact
    full-key/CID/AID/source-provenance guards; owner assay counts are recorded in
    its own saved query frame.
- evidence_id: bgc-2594-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-target-input-plan-001.json
  locator: /records/3/proposed_companion_paths; /records/3/direct_companion_predicates
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: This owner has 0 immediate shared-BGC context input(s); the exact predicates
    do not establish equivalent identity, independent experimental evidence or source
    transfer.
  snapshot_sha256: 31543a1f8d8477dfd89c147a1d95a836b39146176a2f6d6f0887c064b79dacc3
- evidence_id: bgc-2594-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: 'Complete saved mibig_compounds query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
- evidence_id: bgc-2594-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 455-455; raw record sha256 60853689963c9b65651c68c4e689b7df514671e86b6f514849c9544d2e6aa59f
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Assigned retained-row reading of all 25 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2594-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Complete saved chebi_structures query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"context_path": "data/natural_products/unclassified/daptomycin.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "DOAKLVKFURWEDJ-QCMAZARJSA-N", "table": "chebi_structures"}'
- evidence_id: bgc-2594-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: 'Complete saved lotus_occurrences query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
- evidence_id: bgc-2594-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 1157-1157; raw record sha256 c230bd1bd041d5cca9c039192abf6b1cabfe490217fee9125bd40769b4ef5210
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2594-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"context_path": "data/natural_products/unclassified/daptomycin.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "DOAKLVKFURWEDJ-QCMAZARJSA-N", "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2594-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: 'Complete saved npclassifier query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
- evidence_id: bgc-2594-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 452-452; raw record sha256 2268fbd4be172e31b909ed75bd33c592947664eddb193d2c4a82bd3670fe86b1
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: supports
  summary: Assigned retained-row reading of all 7 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2594-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Complete saved pubchem_bioassay query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"context_path": "data/natural_products/unclassified/daptomycin.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "DOAKLVKFURWEDJ-QCMAZARJSA-N", "table": "pubchem_bioassay"}'
- evidence_id: bgc-2594-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"context_path": "data/natural_products/unclassified/daptomycin.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "DOAKLVKFURWEDJ-QCMAZARJSA-N", "table": "bindingdb_targets"}'
- evidence_id: bgc-2594-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"context_path": "data/natural_products/unclassified/daptomycin.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "DOAKLVKFURWEDJ-QCMAZARJSA-N", "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2594-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Complete saved chebi_origins query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"context_path": "data/natural_products/unclassified/daptomycin.yaml",
    "matches": 0, "predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "table": "chebi_origins"}'
- evidence_id: bgc-2594-additional-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Captured additional input role: Retained exclusion-table diagnostic context
    captured for every review; applicable exact assay exclusions and biological rows
    must be derived from actual retained inventory, not file presence.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
- evidence_id: bgc-2594-additional-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Captured additional input role: Retained unresolved-taxon diagnostic context
    used by the bounded curation scan; no fresh taxonomy, forward-merge decision or
    producer confirmation.. File presence itself confers no positive source-row, AID,
    taxon-rank or correction applicability credit.'
  snapshot_sha256: 86efbda9c09388723a4f24da35e18404032f1549a9088192fbd2020cb846fa43
- evidence_id: bgc-2594-additional-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Captured additional input role: Retained explicit forward-merge table
    used by positive and negative taxon queries for each owner; historical route evidence
    only, no fresh taxonomy.. File presence itself confers no positive source-row,
    AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
- evidence_id: bgc-2594-additional-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_non_organism.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Captured additional input role: Retained non-organism table used by positive
    and negative taxon queries for each owner; diagnostic scope only, not a taxon
    verdict from file presence.. File presence itself confers no positive source-row,
    AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: f2c1ee257bbbcb0854528196ab1f809d658c27f1c7b2036f7f71f088b52935bb
- evidence_id: bgc-2594-additional-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Captured additional input role: Maintained exclusion identity, source-row
    digest and attributed-rationale implementation context; no execution or new assay
    evidence.. File presence itself confers no positive source-row, AID, taxon-rank
    or correction applicability credit.'
  snapshot_sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
- evidence_id: bgc-2594-additional-5
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/producer_strains.py
  locator: load_producer_strains lines 12-17; _load_qualifications lines 28-62; qualify_producer
    lines 65-68; _append_evidence lines 78-89
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Captured additional input role: Maintained producer-strain qualification
    implementation: source-row and digest predicate, strain-only CURATOR_INFERENCE
    scope; plaintext dependency, no execution or grade/taxon upgrade.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
- evidence_id: bgc-2594-additional-6
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py
  locator: row_digest lines 19-23 only
  accessed_at: '2026-11-05T20:16:46.957720Z'
  support: context_only
  summary: 'Captured additional input role: Maintained row_digest implementation used
    by qualification guards: sorted ensure_ascii JSON digest only; input presence
    does not claim an audit or application of other structure-correction behavior..
    File presence itself confers no positive source-row, AID, taxon-rank or correction
    applicability credit.'
  snapshot_sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-260/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json
  accessed_at: '2026-11-05T19:35:58.108095Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 6942ae586a37f1f6b0bfb953bb033d936740f6cadc8e55613e9606147d21e0b5
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-260/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json
  accessed_at: '2026-11-05T19:36:23.921683Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 1c748ba7fbed98b1a37bc11eeaf650da93dae7b9457394d90018afccdabb0508
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-260/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json
  accessed_at: '2026-11-05T19:36:44.647940Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-260/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json
  accessed_at: '2026-11-05T19:37:19.990709Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-260/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json
  accessed_at: '2026-11-05T19:37:32.297786Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: d16d92e0251bd183ccd4e5ea14ba7888a14b7eaeb33b2b3635fb5cec93f057b0
assessments:
- assessment_id: bgc-2594-identity
  area: identity
  topic: identity
  outcome: supported
  summary: The minted daptomycin record faithfully maps to BGC0000336 compound 1 and
    retains its PubChem 21585658 cross-reference. Both original stored forms regenerate
    DOAKLVKFURWEDJ-QCMAZARJSA-N. These checks support the encoded retained-source
    association without importing familiar clinical identity or mechanism claims.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  evidence_ids:
  - bgc-2594-identity
  - bgc-2594-chemistry
  - bgc-2594-diagnostic-acceptance
  - bgc-2594-query-mibig_compounds
  - bgc-2594-query-chebi_structures
  - bgc-2594-query-antibioticmech_inchikeys
  - bgc-2594-direct-contexts
  - bgc-2594-row-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: DOAKLVKFURWEDJ-QCMAZARJSA-N
    definition: Literal retained full key and accepted saved regeneration scope.
    evidence_ids:
    - bgc-2594-identity
    - bgc-2594-chemistry
    - bgc-2594-diagnostic-acceptance
    - bgc-2594-query-mibig_compounds
    - bgc-2594-query-chebi_structures
    - bgc-2594-query-antibioticmech_inchikeys
    - bgc-2594-direct-contexts
    - bgc-2594-row-mibig_compounds-0
  - name: grounding_scope
    value: MINTED; exact retained source mapping, natural identity not independently
      established
    definition: Recorded grounding category, separated from independent natural identity.
    evidence_ids:
    - bgc-2594-identity
    - bgc-2594-chemistry
    - bgc-2594-diagnostic-acceptance
    - bgc-2594-query-mibig_compounds
    - bgc-2594-query-chebi_structures
    - bgc-2594-query-antibioticmech_inchikeys
    - bgc-2594-direct-contexts
    - bgc-2594-row-mibig_compounds-0
- assessment_id: bgc-2594-representation
  area: representation
  topic: representation
  outcome: supported
  summary: C72H101N17O26, net charge 0 and the standard identifiers agree across 115-atom/118-bond
    forms. The original 31-membered ester-containing macrocycle, 14 amide sites, separate
    acyl tail and 13 specified tetrahedral centers support a cyclic lipo-depsipeptide
    representation. Reconstruction expresses 14 C(OH)=N sites and 14 unspecified imine
    descriptors. Canonical comparisons remain false and the atom map empty; these
    changes do not establish an erroneous stored form.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  evidence_ids:
  - bgc-2594-identity
  - bgc-2594-chemistry
  - bgc-2594-molecular-reading
  - bgc-2594-diagnostic-acceptance
  - bgc-2594-diagnostic-stderr
  - bgc-2594-row-mibig_compounds-0
  dimensions:
  - name: stereochemistry_scope
    value: 13 specified tetrahedral centers; reconstructed +14 unspecified imines
    definition: Specified original centers and bond geometry, separated from reconstructed
      imine descriptors.
    evidence_ids:
    - bgc-2594-identity
    - bgc-2594-chemistry
    - bgc-2594-molecular-reading
    - bgc-2594-diagnostic-acceptance
    - bgc-2594-diagnostic-stderr
    - bgc-2594-row-mibig_compounds-0
  - name: representation_correspondence
    value: Both canonical comparisons false; atom match empty; normalized identifiers
      equal
    definition: Saved canonical comparisons and limited atom-match result; normalized
      identifiers are not full graph proof.
    evidence_ids:
    - bgc-2594-identity
    - bgc-2594-chemistry
    - bgc-2594-molecular-reading
    - bgc-2594-diagnostic-acceptance
    - bgc-2594-diagnostic-stderr
    - bgc-2594-row-mibig_compounds-0
- assessment_id: bgc-2594-provenance
  area: provenance
  topic: provenance
  outcome: supported
  summary: The source producer Streptomyces filamentosus NRRL11379 (457430) is SOURCE_ASSERTION.
    BGC0000336/AY787762.1:45828..108856 remains CLUSTER_UNSTATED with no stored experimental
    locus method. LOTUS S. filamentosus (67294) is separate occurrence naming. Cached
    labels do not independently verify species/strain rank or ancestry; coordinates
    alone do not strengthen the evidence grade.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  evidence_ids:
  - bgc-2594-owner
  - bgc-2594-provenance
  - bgc-2594-query-mibig_compounds
  - bgc-2594-query-lotus_occurrences
  - bgc-2594-taxonomy
  - bgc-2594-curation
  - bgc-2594-direct-contexts
  - bgc-2594-row-mibig_compounds-0
  - bgc-2594-row-lotus_occurrences-0
  dimensions:
  - name: taxon_scope
    value: NCBITaxon:457430; NCBITaxon:67294; retained names, no fresh rank/lineage
    definition: Retained names, IDs and synonyms; current rank and ancestry are not
      independently established.
    evidence_ids:
    - bgc-2594-owner
    - bgc-2594-provenance
    - bgc-2594-query-mibig_compounds
    - bgc-2594-query-lotus_occurrences
    - bgc-2594-taxonomy
    - bgc-2594-curation
    - bgc-2594-direct-contexts
    - bgc-2594-row-mibig_compounds-0
    - bgc-2594-row-lotus_occurrences-0
  - name: producer_evidence
    value: SOURCE_ASSERTION
    definition: Literal source grade for the compound producer assertion.
    evidence_ids:
    - bgc-2594-owner
    - bgc-2594-provenance
    - bgc-2594-query-mibig_compounds
    - bgc-2594-query-lotus_occurrences
    - bgc-2594-taxonomy
    - bgc-2594-curation
    - bgc-2594-direct-contexts
    - bgc-2594-row-mibig_compounds-0
    - bgc-2594-row-lotus_occurrences-0
  - name: locus_evidence
    value: CLUSTER_UNSTATED
    definition: Literal source grade for the locus-to-compound assertion.
    evidence_ids:
    - bgc-2594-owner
    - bgc-2594-provenance
    - bgc-2594-query-mibig_compounds
    - bgc-2594-query-lotus_occurrences
    - bgc-2594-taxonomy
    - bgc-2594-curation
    - bgc-2594-direct-contexts
    - bgc-2594-row-mibig_compounds-0
    - bgc-2594-row-lotus_occurrences-0
- assessment_id: bgc-2594-citations
  area: evidence
  topic: citations
  outcome: supported
  summary: PMID:15870461 is ENTRY-level MIBiG support; DOI 10.1099/MIC.0.27757-0 belongs
    to the retained LOTUS occurrence. Neither reference was newly accessed. The citation
    inventory does not itself establish compound-specific locus demonstration or clinical
    mechanism.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  evidence_ids:
  - bgc-2594-provenance
  - bgc-2594-query-mibig_compounds
  - bgc-2594-query-lotus_occurrences
  - bgc-2594-query-chebi_origins
  - bgc-2594-source-reading
  - bgc-2594-history
  - bgc-2594-row-mibig_compounds-0
  - bgc-2594-row-lotus_occurrences-0
  dimensions:
  - name: citation_scope
    value: PMID:15870461 [ENTRY]; retained source scope
    definition: Reference grain in the retained source rows; no inherited primary-paper
      access.
    evidence_ids:
    - bgc-2594-provenance
    - bgc-2594-query-mibig_compounds
    - bgc-2594-query-lotus_occurrences
    - bgc-2594-query-chebi_origins
    - bgc-2594-source-reading
    - bgc-2594-history
    - bgc-2594-row-mibig_compounds-0
    - bgc-2594-row-lotus_occurrences-0
- assessment_id: bgc-2594-occurrence_activity
  area: evidence
  topic: occurrence_activity
  outcome: supported
  summary: One LOTUS occurrence names S. filamentosus (67294). No exact retained assay,
    BindingDB target, ChEBI or related-corpus match is available for this full key.
    No clinical or mechanistic facts are imported from the familiar name; the saved
    negatives are limited to the retained tables and query predicates.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  evidence_ids:
  - bgc-2594-activity-owner
  - bgc-2594-query-lotus_occurrences
  - bgc-2594-query-chebi_origins
  - bgc-2594-query-cyanometdb_occurrences
  - bgc-2594-query-pubchem_bioassay
  - bgc-2594-query-bindingdb_targets
  - bgc-2594-query-antibioticmech_inchikeys
  - bgc-2594-assay-curation
  - bgc-2594-direct-contexts
  - bgc-2594-row-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    value: 1 retained occurrence placement; no independent-producer inference
    definition: Exact retained occurrence query scope, without production or independence
      transfer.
    evidence_ids:
    - bgc-2594-activity-owner
    - bgc-2594-query-lotus_occurrences
    - bgc-2594-query-chebi_origins
    - bgc-2594-query-cyanometdb_occurrences
    - bgc-2594-query-pubchem_bioassay
    - bgc-2594-query-bindingdb_targets
    - bgc-2594-query-antibioticmech_inchikeys
    - bgc-2594-assay-curation
    - bgc-2594-direct-contexts
    - bgc-2594-row-lotus_occurrences-0
  - name: assay_target_scope
    value: 0 actual AIDs; 0 blank sentinels; no direct target established
    definition: Actual AID, endpoint and direct-target scope, including sentinels
      and exclusions.
    evidence_ids:
    - bgc-2594-activity-owner
    - bgc-2594-query-lotus_occurrences
    - bgc-2594-query-chebi_origins
    - bgc-2594-query-cyanometdb_occurrences
    - bgc-2594-query-pubchem_bioassay
    - bgc-2594-query-bindingdb_targets
    - bgc-2594-query-antibioticmech_inchikeys
    - bgc-2594-assay-curation
    - bgc-2594-direct-contexts
    - bgc-2594-row-lotus_occurrences-0
- assessment_id: bgc-2594-classification
  area: consistency
  topic: classification
  outcome: supported
  summary: The saved macrocycle contains an ester and multiple amides, with a separate
    acyl tail, supporting the encoded Cyclic peptides/Depsipeptides/Lipopeptides descriptors.
    NPClassifier’s broader Polyketides pathway remains model provenance rather than
    demonstrated biosynthesis. MIBiG NRPS class and Type I subclass are preserved
    separately.
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  evidence_ids:
  - bgc-2594-classification-owner
  - bgc-2594-query-npclassifier
  - bgc-2594-query-mibig_compounds
  - bgc-2594-chemistry
  - bgc-2594-molecular-reading
  - bgc-2594-row-npclassifier-0
  - bgc-2594-row-mibig_compounds-0
  dimensions:
  - name: classification_applicability
    value: Encoded Cyclic peptides/Depsipeptides/Lipopeptides supported; broader model
      pathway qualified
    definition: Encoded motif support separated from exact computed model-family or
      biosynthesis claims.
    evidence_ids:
    - bgc-2594-classification-owner
    - bgc-2594-query-npclassifier
    - bgc-2594-query-mibig_compounds
    - bgc-2594-chemistry
    - bgc-2594-molecular-reading
    - bgc-2594-row-npclassifier-0
    - bgc-2594-row-mibig_compounds-0
- assessment_id: bgc-2594-completion
  area: completeness
  topic: completion
  outcome: unknown
  summary: 'Partial scientific review: complete owner/history, both saved molecular
    forms and assigned retained source payloads were read. All 44 captured input hashes
    and ownership declarations were verified against the accepted 455-input/63-path
    plan. Five local checks passed; full QC and OAK were unavailable. No fresh primary
    sources, taxonomy request, source query or record edit was made.'
  target_ids:
  - naturalproductmech:mibig-d4998c3d5b
  evidence_ids:
  - bgc-2594-intake
  - bgc-2594-intake-acceptance
  - bgc-2594-plan
  - bgc-2594-plan-acceptance
  - bgc-2594-gates
  - bgc-2594-source-reading
  - bgc-2594-source-notes
  - bgc-2594-molecular-reading
  - bgc-2594-diagnostic-acceptance
  - bgc-2594-mechanism-absence
  dimensions:
  - name: review_completion
    value: Partial; 44 actual input hashes/ownership verified; full QC/OAK unavailable
    definition: Actual local review scope and unavailable required gates.
    evidence_ids:
    - bgc-2594-intake
    - bgc-2594-intake-acceptance
    - bgc-2594-plan
    - bgc-2594-plan-acceptance
    - bgc-2594-gates
    - bgc-2594-source-reading
    - bgc-2594-source-notes
    - bgc-2594-molecular-reading
    - bgc-2594-diagnostic-acceptance
    - bgc-2594-mechanism-absence
findings: []
actions: []
limitations:
- No newly accessed primary paper or taxonomy authority; retained references and historical
  curator assertions keep their original scope.
- Full QC and OAK were unavailable. Local gate passes and normalized identifiers do
  not establish natural identity or experimental mechanism.
- The diagnostic attempts one limited chirality-aware substructure match; empty results
  and full graph identity limits are retained. Four original charge-rearrangement
  warnings remain globally scoped.
- Negative source results are bounded by the exact saved query frames; they are not
  general biological absence claims.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'Partial scientific review: complete owner/history, both saved molecular forms and
  assigned retained source payloads were read. All 44 captured input hashes and ownership
  declarations were verified against the accepted 455-input/63-path plan. Five local
  checks passed; full QC and OAK were unavailable. No fresh primary sources, taxonomy
  request, source query or record edit was made.'
- No selected mechanism, pathway, molecular-target or component root applies; maintained-reader
  checks are not applicable. Native gate status is preserved.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-260
```
