# Local evidence review: merochlorin D

- Review: 20261106T222000Z-merochlorin-d
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T21:54:39.761044Z
- Finished UTC: 2026-11-06T22:20:00.234471Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Merochlorin D retains compound index 7 and its distinct full key within BGC0001083. Both saved forms agree, but two atom centres and one potential double-bond configuration remain unspecified. Retained knockout evidence supports the source grades without resolving these configurations or transferring congener identity; the review is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2778; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-c4912c165f | data/natural_products/unclassified/merochlorin-d.yaml | generated | merochlorin D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-c4912c165f | Both stored forms parsed and match the declared normalized key/formula and each other canonically; the existing complete atom map has limited scope. |
| strict_ten | passed | True | naturalproductmech:mibig-c4912c165f | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-c4912c165f | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-c4912c165f | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-c4912c165f | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-c4912c165f | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-c4912c165f | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-c4912c165f | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-c4912c165f | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained compound grounding

identity: supported. Targets: naturalproductmech:mibig-c4912c165f.

MIBiG BGC0001083 version 5, compound index 7, grounds merochlorin D by its complete key. The active entry has questionable quality and complete entry status. Seven direct same-BGC companions remain distinct context; their names, chlorination patterns, configurations and experiments are not transferred to this target.

### Saved molecular forms, stereochemistry and motif scope

representation: supported. Targets: naturalproductmech:mibig-c4912c165f.

Each saved form has 32 atoms, 33 bonds, charge zero and formula C26H33ClO5. Two fused six-rings comprise one aromatic ring and a nonaromatic ring bearing two ketones. A single chlorine and three hydroxyl oxygens are explicit. No strict ester, amide, terminal C(OH)=N, saturated C5O cycle or ether bridge is returned. The source rings are 12-26-24-17-16-14 and 18-20-21-23-16-17, sharing edge 16-17. C26-Cl28 is the chlorine attachment; carbonyl sites are C14=O15 and C24=O25. O13 is attached to C12 and O19/O22 are phenolic. The unresolved alkene C6=C8 is distinct from C1=C3 and C10=C29, whose repeated substituents prevent additional geometric-stereo candidates. All ten saved comparison flags are true for this pair, including standard InChI, complete key, formula, formal charge and canonical isomeric/nonisomeric SMILES. The saved chirality-aware substructure map covers every atom and complete_atom_count_match is true. Its explicit full_graph_identity_established value remains false: this limited calculation does not independently prove full graph, natural-sample or experimental stereochemical identity.

### Producer, taxon and compound-specific locus

provenance: supported. Targets: naturalproductmech:mibig-c4912c165f.

Streptomyces sp. CNH189 NCBITaxon:1136432 retains BGC_CHARACTERIZED producer evidence because the stored methods include Knock-out studies. Enzymatic assays and Heterologous expression supplement cluster support; they are not independently upgraded organism evidence. The exact compound row links BGC0001083 to JX186999.1 with CLUSTER_DEMONSTRATED evidence and Knock-out studies, Enzymatic assays and Heterologous expression. PKS/terpene and Type III/Sesquiterpene source classes remain separate from model classification. No full gene-level pathway is present or newly verified.

### Reference grain and historical provenance

evidence: supported. Targets: naturalproductmech:mibig-c4912c165f.

PMID:22784372 is attributed at ENTRY grain, repeated in producer/locus claims rather than independently verified per placement. Both seeding-history events are provenance. Primary experiments and sequences were not reopened, and congener rows do not supply additional target-specific primary proof.

### Occurrence and retained assay limits

evidence: supported. Targets: naturalproductmech:mibig-c4912c165f.

No exact full-key LOTUS or CyanoMetDB occurrence row is retained for merochlorin D. The owner has no occurrence root. This bounded absence does not establish absence from organisms or literature, and occurrence in a companion does not fill the gap. Every one of the nine saved query frames was read. Exact-key ChEBI, CyanoMetDB, PubChem bioassay, BindingDB and AntibioticMech frames, including the derived empty ChEBI-origin query, return no rows for this owner. There is no actual AID or blank-AID sentinel. These retained-file negatives do not establish inactivity, absence from literature, potency or absence of biological targets.

### Classification, filing and literal mechanism scope

consistency: supported. Targets: naturalproductmech:mibig-c4912c165f.

NPClassifier returns Polyketides and Terpenoids with empty superclass and class fields. Empty strings are preserved as model output, not a missing model row. The two pathways explain UNCLASSIFIED filing. The retained fused-ring and chlorine features do not choose a single biosynthetic class or justify congener merging.

### Earned review and unavailable authority

completeness: supported. Targets: naturalproductmech:mibig-c4912c165f.

The complete current owner and exact source rows were read, actual canonical intake fixed current ownership and input hashes, and the one original saved molecular computation was assessed without replay. Literal mechanism, pathway, component, target, activity and related-record roots are absent; no maintained reader is assigned. Five local native commands passed, but full QC, complete OAK checks and external primary verification remain unavailable. Completion is partial; native SEEDED status and generated records remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2778-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/merochlorin-d.yaml; complete file: chemical_structure, source_concepts, producer_organisms, biosynthetic_gene_clusters, classification and history | supports | Complete current generated owner read; no record or native status edit. |
| support-2778-capture | /private/tmp/npm-review-work/shared-next-batch278/owner-capture-DATA-001.json; /records/7/owner_document; /records/7/component_captures | supports | Accepted complete owner/history capture and empty selected component scope; raw capture is not a maintained-reader invocation. |
| support-2778-source | /private/tmp/npm-review-work/shared-next-batch278-tentative/support-prep/support-current278-assigned-source-reading-001.json; /contexts/2; /totals; /global_cautions | supports | Complete nine-frame assigned source context, all physical positive rows, fields and negative predicates personally read. Own primary credit is 16 rows/196 fields across these five selected contexts; no BGC or Native row duplication. |
| support-2778-plan | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-target-input-plan-001.json; /records/7; /source_placement_count; /unique_source_path_count | supports | Actual original plan retains owner and direct-context inputs; global scope is 467 placements/74 paths, with no additional reviewed-target credit. |
| support-2778-planaccept | /private/tmp/npm-review-work/shared-next-batch278/root-current278-input-plan-acceptance-001.json; /status; /accepted; /input_plan; /source_placements; /unique_source_paths | supports | ROOT accepted the original current source plan. |
| support-2778-notes | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /curation | supports | Current source notes preserve disjoint BGC/Support source readings and Native taxonomy/curation attribution without new primary proof. |
| support-2778-intake | /private/tmp/npm-review-work/shared-next-batch278/intakes-001/2778-inspect-001.json; /status; /source; /targets | supports | Actual canonical intake preserves this generated target, maintained owners and complete current input hash map. |
| support-2778-intakeaccept | /private/tmp/npm-review-work/shared-next-batch278/root-current278-intake-acceptance-001.json; /status; /accepted; /intake_summary; /records; /source_placements; /unique_source_paths | supports | ROOT accepted all ten original canonical intakes; this scientific review uses only its assigned target. |
| support-2778-data | /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles; /records/7/inchi; /records/7/comparisons; /records/7/atom_correspondence | supports | Each saved form has 32 atoms, 33 bonds, charge zero and formula C26H33ClO5. Two fused six-rings comprise one aromatic ring and a nonaromatic ring bearing two ketones. A single chlorine and three hydroxyl oxygens are explicit. No strict ester, amide, terminal C(OH)=N, saturated C5O cycle or ether bridge is returned. All ten saved comparison flags are true for this pair, including standard InChI, complete key, formula, formal charge and canonical isomeric/nonisomeric SMILES. The saved chirality-aware substructure map covers every atom and complete_atom_count_match is true. Its explicit full_graph_identity_established value remains false: this limited calculation does not independently prove full graph, natural-sample or experimental stereochemical identity. |
| support-2778-stereo | /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/smiles/computed/potential_stereo; /records/7/inchi/computed/potential_stereo; /records/7/smiles/computed/atoms; /records/7/inchi/computed/atoms | supports | Both saved forms have two unspecified tetrahedral centres and one unspecified double-bond candidate, with no specified stereo entries. Source centres 12 and 26 map to InChI-derived centres 25 and 24. The unspecified source bond is C6=C8. The other two alkenes have repeated substituents at one end and are not additional E/Z candidates. The false source atom-stereo flag does not resolve any of these configurations. |
| support-2778-motifs | /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed/motifs; /records/7/smiles/computed/rings; /records/7/smiles/computed/bonds; /records/7/inchi/computed/motifs; /records/7/inchi/computed/rings; /records/7/inchi/computed/bonds | supports | The source rings are 12-26-24-17-16-14 and 18-20-21-23-16-17, sharing edge 16-17. C26-Cl28 is the chlorine attachment; carbonyl sites are C14=O15 and C24=O25. O13 is attached to C12 and O19/O22 are phenolic. The unresolved alkene C6=C8 is distinct from C1=C3 and C10=C29, whose repeated substituents prevent additional geometric-stereo candidates. |
| support-2778-molecularreading | /private/tmp/npm-review-work/shared-next-batch278-tentative/support-prep/support-current278-last-five-molecular-intake-reading-001.json; /records/2; /counts; /warnings | supports | Complete ten assigned saved forms and actual intakes retained; no molecular replay. Four undefined-stereo warnings remain globally unassigned. |
| support-2778-execution | /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries | supports | Single original diagnostic exited zero, with exact command/streams and no retry. Process success is not a natural-identity result. |
| support-2778-diagaccept | /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /DATA; /execution | supports | ROOT accepted the original saved diagnostic; no additional parse was performed for this review. |
| support-2778-stderr | /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnostic-original-001.stderr; complete original stderr, four warning lines | supports | Four undefined-stereo warning lines are globally unassigned to records. They are not used as four record-specific defects. |
| support-2778-taxonomy | /private/tmp/npm-review-work/shared-next-batch278-tentative/native-prep/native-current278-cached-taxonomy-reading-002.json; /context_interpretations/26; /whole_stanzas; /physical_negative_query_scopes/26 | supports | Preserve Streptomyces sp. CNH189 (1136432), including the cached CNH-189 spelling. Where present, separate Streptomyces spectabilis (68270) or broader Streptomyces (1883) occurrence context remains separately attributed. Shared locus, producer or names do not merge the chlorination/regioisomer congeners or transfer evidence grades. |
| support-2778-curation | /private/tmp/npm-review-work/shared-next-batch278-tentative/native-prep/native-current278-implemented-curation-scan-002.json; /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows; /implementation_scope; /input_ownership | supports | Native found no exact applicable implemented curation decision; lexical numerical/name hits do not establish applicability. |
| support-2778-producerpolicy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; complete retained method grading table | supports | The method table distinguishes organism+cluster knockout support from cluster-only enzymatic or heterologous evidence, and preserves the unstated-method grade. |
| support-2778-stereopolicy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172, FindMolChiralCenters(includeUnassigned=True, useLegacyImplementation=False) | supports | The source stereo_complete predicate checks unassigned atom centres. It does not establish complete natural-product geometry. |
| support-2778-filingpolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306, choose_pathway | supports | Exactly one supported normalized pathway label selects a directory; multiple, empty or unsupported labels retain UNCLASSIFIED. All model labels are preserved separately. |
| support-2778-gates | /private/tmp/npm-review-work/shared-next-batch278/root-current278-five-gates-acceptance-001.json; /records; /selected_queue_rows; /full_native_checks_passed; /unavailable_checks; /scope | supports | Five local command results passed; full QC/OAK remain unavailable. Current producer, pathway, biosynthesis and stereo queue rows are scoped diagnostic leads, not automatic findings. |
| support-2778-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame has 1 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2778-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2778-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2778-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2778-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame has 1 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2778-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2778-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2778-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2778-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2778-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical line 1267, raw UTF-8 row SHA-256 e72184324cc2ccf4ab139eb1ea37badaeeb9bd94417769484886b1601dd4dc27 | supports | MIBiG BGC0001083 version 5, compound index 7, grounds merochlorin D by its complete key. The active entry has questionable quality and complete entry status. Seven direct same-BGC companions remain distinct context; their names, chlorination patterns, configurations and experiments are not transferred to this target. |
| support-2778-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical line 2464, raw UTF-8 row SHA-256 d6d0bade825a470cccc905f738d4331b78792845d7a8fe05477bed9a27172fde | supports | NPClassifier returns Polyketides and Terpenoids with empty superclass and class fields. Empty strings are preserved as model output, not a missing model row. The two pathways explain UNCLASSIFIED filing. The retained fused-ring and chlorine features do not choose a single biosynthetic class or justify congener merging. |
| support-2778-history | /private/tmp/npm-review-work/shared-next-batch278/owner-capture-DATA-001.json; /records/7/owner_document/curation_history; /records/7/owner_document/source_concepts | supports | PMID:22784372 is attributed at ENTRY grain, repeated in producer/locus claims rather than independently verified per placement. Both seeding-history events are provenance. Primary experiments and sequences were not reopened, and congener rows do not supply additional target-specific primary proof. |
| support-2778-scope | /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-target-input-plan-001.json; /records/7/complete_root_keys; /records/7/declared_mechanism_roots_literal; /records/7/component_paths; /records/7/literal_related_record_corpora | supports | Literal selected mechanism/pathway/component/target/activity/related roots are absent. This is not evidence of biological absence and assigns no maintained reader. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-278/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-278/native-current278-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-278/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-278/native-current278-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-278/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-278/native-current278-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-278/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-278/native-current278-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-278/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-278/native-current278-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Primary papers, spectra, sequences, live taxonomy and natural-product identity were not independently verified. Full QC, complete OAK and external primary checks remain unavailable.
- All ten saved comparison flags are true for this pair, including standard InChI, complete key, formula, formal charge and canonical isomeric/nonisomeric SMILES. The saved chirality-aware substructure map covers every atom and complete_atom_count_match is true. Its explicit full_graph_identity_established value remains false: this limited calculation does not independently prove full graph, natural-sample or experimental stereochemical identity. Both saved forms have two unspecified tetrahedral centres and one unspecified double-bond candidate, with no specified stereo entries. Source centres 12 and 26 map to InChI-derived centres 25 and 24. The unspecified source bond is C6=C8. The other two alkenes have repeated substituents at one end and are not additional E/Z candidates. The false source atom-stereo flag does not resolve any of these configurations.
- Four undefined-stereo warning lines are globally unassigned. Exact-key negatives and literal root absence do not establish inactivity or universal absence.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh current 278 scientific judgments use current retained owner/source/intake/diagnostic evidence; earlier batches supply interface logic only.
- No generated record, source inventory, native status or campaign artifact was edited. No query, molecular parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual local native checks and three required unavailable checks. No maintained-reader check belongs to these zero-reader targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T222000Z-merochlorin-d
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: merochlorin D'
started_at: '2026-11-06T21:54:39.761044Z'
finished_at: '2026-11-06T22:20:00.234471Z'
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
summary: Merochlorin D retains compound index 7 and its distinct full key within BGC0001083.
  Both saved forms agree, but two atom centres and one potential double-bond configuration
  remain unspecified. Retained knockout evidence supports the source grades without
  resolving these configurations or transferring congener identity; the review is
  partial.
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
  - path: data/natural_products/polyketides/merochlorin-c.yaml
    sha256: 3e3d91c69b7ff7dc12102d2c28aa5267a49f938615bf1f8445638a6fbfb67502
    role: context
  - path: data/natural_products/terpenoids/deschloro-merochlorin-a.yaml
    sha256: e8782e84d691092b21c0606b59853e892c707bcd68363b8d8e0e9843cc04bfa0
    role: context
  - path: data/natural_products/terpenoids/deschloro-merochlorin-b.yaml
    sha256: 2dfae52c5da621f4c133e1f53bbd0dc7cb01000e981f0f896f35cafec19238bd
    role: context
  - path: data/natural_products/terpenoids/dichloro-merochlorin-b.yaml
    sha256: 0d3ea9b9a219c5975803da7af0a2777cf5939b0ae43efd4ceca427e25b6f54d7
    role: context
  - path: data/natural_products/terpenoids/isochloro-merochlorin-b.yaml
    sha256: d5109a5f1fbf5cb13df2952d7e9aab18fc28b9c5179e5996304ccdf15df34783
    role: context
  - path: data/natural_products/terpenoids/merochlorin-a.yaml
    sha256: 50a1a834c9ff778705522eb0c45c7bbf30236472166c7a24fd3239c9c4c03d4b
    role: context
  - path: data/natural_products/terpenoids/merochlorin-b.yaml
    sha256: 5278f665d49c9fdba55b81ae7e8da6df4f0dc44878f5894dc45f58bee4c873bd
    role: context
  - path: data/natural_products/unclassified/merochlorin-d.yaml
    sha256: 98edb35394bea516eb74973c015e837c00e58072946a0b7f2a73d4ec3604e5e3
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
  selection: Campaign path order 2778; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-c4912c165f
targets:
- target_id: naturalproductmech:mibig-c4912c165f
  path: data/natural_products/unclassified/merochlorin-d.yaml
  label: merochlorin D
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
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnose278-001.py
    b616406f31681c7e084d6bb4dbcd5075d807765a01de20135749948da4297c0f ac22a68f3393c243386a90a2a9ceff1b03c86a3d3d2b86543ced0f0e87153ce7
    ef363897b2a391a3cd6abfd7ef2371617f527f0569d7b769530dd09102659f9a
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed and match the declared normalized key/formula
    and each other canonically; the existing complete atom map has limited scope.
  scope_note: 'All ten saved comparison flags are true for this pair, including standard
    InChI, complete key, formula, formal charge and canonical isomeric/nonisomeric
    SMILES. The saved chirality-aware substructure map covers every atom and complete_atom_count_match
    is true. Its explicit full_graph_identity_established value remains false: this
    limited calculation does not independently prove full graph, natural-sample or
    experimental stereochemical identity. Both saved forms have two unspecified tetrahedral
    centres and one unspecified double-bond candidate, with no specified stereo entries.
    Source centres 12 and 26 map to InChI-derived centres 25 and 24. The unspecified
    source bond is C6=C8. The other two alkenes have repeated substituents at one
    end and are not additional E/Z candidates. The false source atom-stereo flag does
    not resolve any of these configurations. Four original warning lines remain globally
    unassigned; no replay.'
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  evidence_ids:
  - support-2778-data
  - support-2778-execution
  - support-2778-diagaccept
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  command: just validate-strict data/natural_products/unclassified/marformycin-e.yaml
    data/natural_products/unclassified/marformycin-f.yaml data/natural_products/unclassified/marinostatin.yaml
    data/natural_products/unclassified/massiliachelin.yaml data/natural_products/unclassified/megapolibactin-bcyc.yaml
    data/natural_products/unclassified/melinacidin-iv.yaml data/natural_products/unclassified/melithiazol-a.yaml
    data/natural_products/unclassified/merochlorin-d.yaml data/natural_products/unclassified/metarhizin-a.yaml
    data/natural_products/unclassified/micacocidin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-278/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-c4912c165f
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-278/validate-all-001.tsv
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
  - naturalproductmech:mibig-c4912c165f
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
  - naturalproductmech:mibig-c4912c165f
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
  - naturalproductmech:mibig-c4912c165f
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-278/review-queue-001.tsv
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
  - naturalproductmech:mibig-c4912c165f
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2778-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/merochlorin-d.yaml
  locator: 'complete file: chemical_structure, source_concepts, producer_organisms,
    biosynthetic_gene_clusters, classification and history'
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Complete current generated owner read; no record or native status edit.
  snapshot_sha256: 98edb35394bea516eb74973c015e837c00e58072946a0b7f2a73d4ec3604e5e3
- evidence_id: support-2778-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch278/owner-capture-DATA-001.json
  locator: /records/7/owner_document; /records/7/component_captures
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Accepted complete owner/history capture and empty selected component scope;
    raw capture is not a maintained-reader invocation.
  snapshot_sha256: ac22a68f3393c243386a90a2a9ceff1b03c86a3d3d2b86543ced0f0e87153ce7
- evidence_id: support-2778-source
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/support-prep/support-current278-assigned-source-reading-001.json
  locator: /contexts/2; /totals; /global_cautions
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Complete nine-frame assigned source context, all physical positive rows,
    fields and negative predicates personally read. Own primary credit is 16 rows/196
    fields across these five selected contexts; no BGC or Native row duplication.
  snapshot_sha256: 6eb9b139409dbbf0fbcdb7f5dd82bdc921d632bebc7c0977ba204f4cce1967d2
- evidence_id: support-2778-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-target-input-plan-001.json
  locator: /records/7; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Actual original plan retains owner and direct-context inputs; global scope
    is 467 placements/74 paths, with no additional reviewed-target credit.
  snapshot_sha256: 0e8e9a2c21683b195910cb33916053826309c3bd7a6ec8a0addf1b30d6cce942
- evidence_id: support-2778-planaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278/root-current278-input-plan-acceptance-001.json
  locator: /status; /accepted; /input_plan; /source_placements; /unique_source_paths
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: ROOT accepted the original current source plan.
  snapshot_sha256: 91c150ea38289213de142d2be5351ac7e7c817386a8aa99caeb3d3fa7ab3eb81
- evidence_id: support-2778-notes
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /curation
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Current source notes preserve disjoint BGC/Support source readings and
    Native taxonomy/curation attribution without new primary proof.
  snapshot_sha256: 9f39649caafe1da1c0f73d8ad97af2baf643d101f1571ab773e355f5a5079010
- evidence_id: support-2778-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278/intakes-001/2778-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Actual canonical intake preserves this generated target, maintained owners
    and complete current input hash map.
  snapshot_sha256: 0f9dcf9e11c36f1bf485dbffd97ec3c29739c594417cb89507bcb8cbddaeae54
- evidence_id: support-2778-intakeaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278/root-current278-intake-acceptance-001.json
  locator: /status; /accepted; /intake_summary; /records; /source_placements; /unique_source_paths
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: ROOT accepted all ten original canonical intakes; this scientific review
    uses only its assigned target.
  snapshot_sha256: d18210f2bddf10c901a49667274a3f344fffa1ea0dea560daee452c6591474a5
- evidence_id: support-2778-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles; /records/7/inchi; /records/7/comparisons; /records/7/atom_correspondence
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: 'Each saved form has 32 atoms, 33 bonds, charge zero and formula C26H33ClO5.
    Two fused six-rings comprise one aromatic ring and a nonaromatic ring bearing
    two ketones. A single chlorine and three hydroxyl oxygens are explicit. No strict
    ester, amide, terminal C(OH)=N, saturated C5O cycle or ether bridge is returned.
    All ten saved comparison flags are true for this pair, including standard InChI,
    complete key, formula, formal charge and canonical isomeric/nonisomeric SMILES.
    The saved chirality-aware substructure map covers every atom and complete_atom_count_match
    is true. Its explicit full_graph_identity_established value remains false: this
    limited calculation does not independently prove full graph, natural-sample or
    experimental stereochemical identity.'
  snapshot_sha256: 43c5a336036f532c17479dd24aef8680928459dec064ed12ed4bc98f8860998a
- evidence_id: support-2778-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/smiles/computed/potential_stereo;
    /records/7/inchi/computed/potential_stereo; /records/7/smiles/computed/atoms;
    /records/7/inchi/computed/atoms
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Both saved forms have two unspecified tetrahedral centres and one unspecified
    double-bond candidate, with no specified stereo entries. Source centres 12 and
    26 map to InChI-derived centres 25 and 24. The unspecified source bond is C6=C8.
    The other two alkenes have repeated substituents at one end and are not additional
    E/Z candidates. The false source atom-stereo flag does not resolve any of these
    configurations.
  snapshot_sha256: 43c5a336036f532c17479dd24aef8680928459dec064ed12ed4bc98f8860998a
- evidence_id: support-2778-motifs
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed/motifs; /records/7/smiles/computed/rings; /records/7/smiles/computed/bonds;
    /records/7/inchi/computed/motifs; /records/7/inchi/computed/rings; /records/7/inchi/computed/bonds
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: The source rings are 12-26-24-17-16-14 and 18-20-21-23-16-17, sharing edge
    16-17. C26-Cl28 is the chlorine attachment; carbonyl sites are C14=O15 and C24=O25.
    O13 is attached to C12 and O19/O22 are phenolic. The unresolved alkene C6=C8 is
    distinct from C1=C3 and C10=C29, whose repeated substituents prevent additional
    geometric-stereo candidates.
  snapshot_sha256: 43c5a336036f532c17479dd24aef8680928459dec064ed12ed4bc98f8860998a
- evidence_id: support-2778-molecularreading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/support-prep/support-current278-last-five-molecular-intake-reading-001.json
  locator: /records/2; /counts; /warnings
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Complete ten assigned saved forms and actual intakes retained; no molecular
    replay. Four undefined-stereo warnings remain globally unassigned.
  snapshot_sha256: 42242004be10c5916d1ee34d5222fec8cb67a02614f6b804296cb4df857829aa
- evidence_id: support-2778-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Single original diagnostic exited zero, with exact command/streams and
    no retry. Process success is not a natural-identity result.
  snapshot_sha256: 9c1ed9ea316d0f93f69536e7a1d54e9d47ee873b6873c829ebc0b8a76ddfbb54
- evidence_id: support-2778-diagaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /DATA; /execution
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: ROOT accepted the original saved diagnostic; no additional parse was performed
    for this review.
  snapshot_sha256: 042a3682cb12c5be5354c6d584bd9701b3a513f35a7974cdc1c2504f39635122
- evidence_id: support-2778-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278/chemistry-local/diagnostic-original-001.stderr
  locator: complete original stderr, four warning lines
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Four undefined-stereo warning lines are globally unassigned to records.
    They are not used as four record-specific defects.
  snapshot_sha256: 78daa2f0eb7d1f49993af2b4ef9c4ca4275944e98d00b325ddcc4d81dd5a1a2c
- evidence_id: support-2778-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/native-prep/native-current278-cached-taxonomy-reading-002.json
  locator: /context_interpretations/26; /whole_stanzas; /physical_negative_query_scopes/26
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Preserve Streptomyces sp. CNH189 (1136432), including the cached CNH-189
    spelling. Where present, separate Streptomyces spectabilis (68270) or broader
    Streptomyces (1883) occurrence context remains separately attributed. Shared locus,
    producer or names do not merge the chlorination/regioisomer congeners or transfer
    evidence grades.
  snapshot_sha256: fd710a3c023d9f6e0faf312cbdf7009176c91648be92ce2424ae59e2e63da6a3
- evidence_id: support-2778-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/native-prep/native-current278-implemented-curation-scan-002.json
  locator: /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows;
    /implementation_scope; /input_ownership
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Native found no exact applicable implemented curation decision; lexical
    numerical/name hits do not establish applicability.
  snapshot_sha256: 90f082a3b0552070fde19b885ce442f394d98af0cc694dcd59977a2febbe3fb5
  search_scope: Nine retained substantive tables, exact owner/source compound/BGC/full-key/occurrence/assay
    predicates; two reserved census-only tables excluded. No new source query or universal
    absence claim.
- evidence_id: support-2778-producerpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: complete retained method grading table
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: The method table distinguishes organism+cluster knockout support from cluster-only
    enzymatic or heterologous evidence, and preserves the unstated-method grade.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2778-stereopolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 165-172, FindMolChiralCenters(includeUnassigned=True, useLegacyImplementation=False)
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: The source stereo_complete predicate checks unassigned atom centres. It
    does not establish complete natural-product geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2778-filingpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295-306, choose_pathway
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Exactly one supported normalized pathway label selects a directory; multiple,
    empty or unsupported labels retain UNCLASSIFIED. All model labels are preserved
    separately.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2778-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch278/root-current278-five-gates-acceptance-001.json
  locator: /records; /selected_queue_rows; /full_native_checks_passed; /unavailable_checks;
    /scope
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Five local command results passed; full QC/OAK remain unavailable. Current
    producer, pathway, biosynthesis and stereo queue rows are scoped diagnostic leads,
    not automatic findings.
  snapshot_sha256: 8533294fd972f7f64e4972c56ef5ccd625342d25670abea22c198809f95923a9
- evidence_id: support-2778-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Saved mibig_compounds frame has 1 positive placements; complete rows or
    the complete empty predicate frame were read.
  snapshot_sha256: 72ed8eb6b8daee50b2eef5d1a6b3afe9fedb97a6d03854efa1a66fe181c6854a
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "UUMRLFAHEFYGJM-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2778-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Saved chebi_structures frame has 0 positive placements; complete rows or
    the complete empty predicate frame were read.
  snapshot_sha256: 72ed8eb6b8daee50b2eef5d1a6b3afe9fedb97a6d03854efa1a66fe181c6854a
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "UUMRLFAHEFYGJM-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2778-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Saved lotus_occurrences frame has 0 positive placements; complete rows
    or the complete empty predicate frame were read.
  snapshot_sha256: 72ed8eb6b8daee50b2eef5d1a6b3afe9fedb97a6d03854efa1a66fe181c6854a
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "UUMRLFAHEFYGJM-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2778-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame has 0 positive placements; complete
    rows or the complete empty predicate frame were read.
  snapshot_sha256: 72ed8eb6b8daee50b2eef5d1a6b3afe9fedb97a6d03854efa1a66fe181c6854a
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "UUMRLFAHEFYGJM-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2778-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Saved npclassifier frame has 1 positive placements; complete rows or the
    complete empty predicate frame were read.
  snapshot_sha256: 72ed8eb6b8daee50b2eef5d1a6b3afe9fedb97a6d03854efa1a66fe181c6854a
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "UUMRLFAHEFYGJM-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2778-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Saved pubchem_bioassay frame has 0 positive placements; complete rows or
    the complete empty predicate frame were read.
  snapshot_sha256: 72ed8eb6b8daee50b2eef5d1a6b3afe9fedb97a6d03854efa1a66fe181c6854a
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "UUMRLFAHEFYGJM-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2778-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Saved bindingdb_targets frame has 0 positive placements; complete rows
    or the complete empty predicate frame were read.
  snapshot_sha256: 72ed8eb6b8daee50b2eef5d1a6b3afe9fedb97a6d03854efa1a66fe181c6854a
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "UUMRLFAHEFYGJM-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2778-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame has 0 positive placements; complete
    rows or the complete empty predicate frame were read.
  snapshot_sha256: 72ed8eb6b8daee50b2eef5d1a6b3afe9fedb97a6d03854efa1a66fe181c6854a
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "UUMRLFAHEFYGJM-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2778-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Saved chebi_origins frame has 0 positive placements; complete rows or the
    complete empty predicate frame were read.
  snapshot_sha256: 72ed8eb6b8daee50b2eef5d1a6b3afe9fedb97a6d03854efa1a66fe181c6854a
  search_scope: Explicit retained input only; predicate exact chebi_id from exact
    full-key structure rows; query []. No cap, query replay or universal literature/biological
    absence claim.
- evidence_id: support-2778-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical line 1267, raw UTF-8 row SHA-256 e72184324cc2ccf4ab139eb1ea37badaeeb9bd94417769484886b1601dd4dc27
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: MIBiG BGC0001083 version 5, compound index 7, grounds merochlorin D by
    its complete key. The active entry has questionable quality and complete entry
    status. Seven direct same-BGC companions remain distinct context; their names,
    chlorination patterns, configurations and experiments are not transferred to this
    target.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2778-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical line 2464, raw UTF-8 row SHA-256 d6d0bade825a470cccc905f738d4331b78792845d7a8fe05477bed9a27172fde
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: NPClassifier returns Polyketides and Terpenoids with empty superclass and
    class fields. Empty strings are preserved as model output, not a missing model
    row. The two pathways explain UNCLASSIFIED filing. The retained fused-ring and
    chlorine features do not choose a single biosynthetic class or justify congener
    merging.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2778-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch278/owner-capture-DATA-001.json
  locator: /records/7/owner_document/curation_history; /records/7/owner_document/source_concepts
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: PMID:22784372 is attributed at ENTRY grain, repeated in producer/locus
    claims rather than independently verified per placement. Both seeding-history
    events are provenance. Primary experiments and sequences were not reopened, and
    congener rows do not supply additional target-specific primary proof.
  snapshot_sha256: ac22a68f3393c243386a90a2a9ceff1b03c86a3d3d2b86543ced0f0e87153ce7
- evidence_id: support-2778-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch278-tentative/bgc-prep/bgc-conditional278-target-input-plan-001.json
  locator: /records/7/complete_root_keys; /records/7/declared_mechanism_roots_literal;
    /records/7/component_paths; /records/7/literal_related_record_corpora
  accessed_at: '2026-11-06T22:13:19.723725Z'
  support: supports
  summary: Literal selected mechanism/pathway/component/target/activity/related roots
    are absent. This is not evidence of biological absence and assigns no maintained
    reader.
  snapshot_sha256: 0e8e9a2c21683b195910cb33916053826309c3bd7a6ec8a0addf1b30d6cce942
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-278/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-278/native-current278-five-gates-execution-001.json
  accessed_at: '2026-11-06T21:55:05.626125Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: f7c35e93394fa00e1e00031839c1947db808acabf3531893791bee8b58c942b4
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-278/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-278/native-current278-five-gates-execution-001.json
  accessed_at: '2026-11-06T21:55:30.771188Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 5be36d3ba4fa69da075201b411fbf3fe74d70b5d12a75a3fcf490f35844fcb7a
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-278/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-278/native-current278-five-gates-execution-001.json
  accessed_at: '2026-11-06T21:55:50.428045Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-278/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-278/native-current278-five-gates-execution-001.json
  accessed_at: '2026-11-06T21:56:24.412875Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-278/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-278/native-current278-five-gates-execution-001.json
  accessed_at: '2026-11-06T21:56:36.158587Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 81b7ca24e46d151e4ea35fac6f7ea50d86b8790c5b63185de47713e2b53ecfad
assessments:
- assessment_id: support-2778-identity-assessment
  area: identity
  topic: Exact retained compound grounding
  summary: MIBiG BGC0001083 version 5, compound index 7, grounds merochlorin D by
    its complete key. The active entry has questionable quality and complete entry
    status. Seven direct same-BGC companions remain distinct context; their names,
    chlorination patterns, configurations and experiments are not transferred to this
    target.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  evidence_ids:
  - support-2778-owner
  - support-2778-capture
  - support-2778-source
  - support-2778-plan
  - support-2778-intake
  - support-2778-curation
  - support-2778-table-mibig_compounds
  - support-2778-table-npclassifier
  dimensions:
  - name: standard_inchi_key
    definition: Complete key, not name or connectivity-prefix matching.
    value: UUMRLFAHEFYGJM-UHFFFAOYSA-N
    evidence_ids:
    - support-2778-owner
    - support-2778-capture
    - support-2778-source
    - support-2778-plan
    - support-2778-intake
    - support-2778-curation
    - support-2778-table-mibig_compounds
    - support-2778-table-npclassifier
  - name: grounding_scope
    definition: Database grounding is distinct from natural-sample identity.
    value: MIBiG BGC0001083 version 5, compound index 7, grounds merochlorin D by
      its complete key. The active entry has questionable quality and complete entry
      status. Seven direct same-BGC companions remain distinct context; their names,
      chlorination patterns, configurations and experiments are not transferred to
      this target.
    evidence_ids:
    - support-2778-owner
    - support-2778-capture
    - support-2778-source
    - support-2778-plan
    - support-2778-intake
    - support-2778-curation
    - support-2778-table-mibig_compounds
    - support-2778-table-npclassifier
- assessment_id: support-2778-representation-assessment
  area: representation
  topic: Saved molecular forms, stereochemistry and motif scope
  summary: 'Each saved form has 32 atoms, 33 bonds, charge zero and formula C26H33ClO5.
    Two fused six-rings comprise one aromatic ring and a nonaromatic ring bearing
    two ketones. A single chlorine and three hydroxyl oxygens are explicit. No strict
    ester, amide, terminal C(OH)=N, saturated C5O cycle or ether bridge is returned.
    The source rings are 12-26-24-17-16-14 and 18-20-21-23-16-17, sharing edge 16-17.
    C26-Cl28 is the chlorine attachment; carbonyl sites are C14=O15 and C24=O25. O13
    is attached to C12 and O19/O22 are phenolic. The unresolved alkene C6=C8 is distinct
    from C1=C3 and C10=C29, whose repeated substituents prevent additional geometric-stereo
    candidates. All ten saved comparison flags are true for this pair, including standard
    InChI, complete key, formula, formal charge and canonical isomeric/nonisomeric
    SMILES. The saved chirality-aware substructure map covers every atom and complete_atom_count_match
    is true. Its explicit full_graph_identity_established value remains false: this
    limited calculation does not independently prove full graph, natural-sample or
    experimental stereochemical identity.'
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  evidence_ids:
  - support-2778-data
  - support-2778-stereo
  - support-2778-motifs
  - support-2778-molecularreading
  - support-2778-execution
  - support-2778-diagaccept
  - support-2778-stereopolicy
  dimensions:
  - name: stereochemistry_scope
    definition: Saved configurations and unspecified candidates remain distinct.
    value: Both saved forms have two unspecified tetrahedral centres and one unspecified
      double-bond candidate, with no specified stereo entries. Source centres 12 and
      26 map to InChI-derived centres 25 and 24. The unspecified source bond is C6=C8.
      The other two alkenes have repeated substituents at one end and are not additional
      E/Z candidates. The false source atom-stereo flag does not resolve any of these
      configurations.
    evidence_ids:
    - support-2778-data
    - support-2778-stereo
    - support-2778-motifs
    - support-2778-molecularreading
    - support-2778-execution
    - support-2778-diagaccept
    - support-2778-stereopolicy
  - name: representation_correspondence
    definition: Limited saved calculation, without independent full/natural identity.
    value: 'All ten saved comparison flags are true for this pair, including standard
      InChI, complete key, formula, formal charge and canonical isomeric/nonisomeric
      SMILES. The saved chirality-aware substructure map covers every atom and complete_atom_count_match
      is true. Its explicit full_graph_identity_established value remains false: this
      limited calculation does not independently prove full graph, natural-sample
      or experimental stereochemical identity.'
    evidence_ids:
    - support-2778-data
    - support-2778-stereo
    - support-2778-motifs
    - support-2778-molecularreading
    - support-2778-execution
    - support-2778-diagaccept
    - support-2778-stereopolicy
- assessment_id: support-2778-provenance-assessment
  area: provenance
  topic: Producer, taxon and compound-specific locus
  summary: Streptomyces sp. CNH189 NCBITaxon:1136432 retains BGC_CHARACTERIZED producer
    evidence because the stored methods include Knock-out studies. Enzymatic assays
    and Heterologous expression supplement cluster support; they are not independently
    upgraded organism evidence. The exact compound row links BGC0001083 to JX186999.1
    with CLUSTER_DEMONSTRATED evidence and Knock-out studies, Enzymatic assays and
    Heterologous expression. PKS/terpene and Type III/Sesquiterpene source classes
    remain separate from model classification. No full gene-level pathway is present
    or newly verified.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  evidence_ids:
  - support-2778-owner
  - support-2778-capture
  - support-2778-source
  - support-2778-taxonomy
  - support-2778-curation
  - support-2778-producerpolicy
  - support-2778-table-mibig_compounds
  dimensions:
  - name: taxon_scope
    definition: Cached naming does not establish current taxonomy or role transfer.
    value: Preserve Streptomyces sp. CNH189 (1136432), including the cached CNH-189
      spelling. Where present, separate Streptomyces spectabilis (68270) or broader
      Streptomyces (1883) occurrence context remains separately attributed. Shared
      locus, producer or names do not merge the chlorination/regioisomer congeners
      or transfer evidence grades.
    evidence_ids:
    - support-2778-owner
    - support-2778-capture
    - support-2778-source
    - support-2778-taxonomy
    - support-2778-curation
    - support-2778-producerpolicy
    - support-2778-table-mibig_compounds
  - name: producer_evidence
    definition: Source-organism evidence is separate from locus evidence.
    value: Streptomyces sp. CNH189 NCBITaxon:1136432 retains BGC_CHARACTERIZED producer
      evidence because the stored methods include Knock-out studies. Enzymatic assays
      and Heterologous expression supplement cluster support; they are not independently
      upgraded organism evidence.
    evidence_ids:
    - support-2778-owner
    - support-2778-capture
    - support-2778-source
    - support-2778-taxonomy
    - support-2778-curation
    - support-2778-producerpolicy
    - support-2778-table-mibig_compounds
  - name: locus_evidence
    definition: Exact compound version, locus and methods delimit the claim.
    value: The exact compound row links BGC0001083 to JX186999.1 with CLUSTER_DEMONSTRATED
      evidence and Knock-out studies, Enzymatic assays and Heterologous expression.
      PKS/terpene and Type III/Sesquiterpene source classes remain separate from model
      classification. No full gene-level pathway is present or newly verified.
    evidence_ids:
    - support-2778-owner
    - support-2778-capture
    - support-2778-source
    - support-2778-taxonomy
    - support-2778-curation
    - support-2778-producerpolicy
    - support-2778-table-mibig_compounds
- assessment_id: support-2778-citations-assessment
  area: evidence
  topic: Reference grain and historical provenance
  summary: PMID:22784372 is attributed at ENTRY grain, repeated in producer/locus
    claims rather than independently verified per placement. Both seeding-history
    events are provenance. Primary experiments and sequences were not reopened, and
    congener rows do not supply additional target-specific primary proof.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  evidence_ids:
  - support-2778-owner
  - support-2778-capture
  - support-2778-source
  - support-2778-history
  - support-2778-table-mibig_compounds
  - support-2778-table-npclassifier
  dimensions:
  - name: citation_scope
    definition: Repeated attribution does not equal independent primary proof.
    value: PMID:22784372 is attributed at ENTRY grain, repeated in producer/locus
      claims rather than independently verified per placement. Both seeding-history
      events are provenance. Primary experiments and sequences were not reopened,
      and congener rows do not supply additional target-specific primary proof.
    evidence_ids:
    - support-2778-owner
    - support-2778-capture
    - support-2778-source
    - support-2778-history
    - support-2778-table-mibig_compounds
    - support-2778-table-npclassifier
- assessment_id: support-2778-occurrence-assay-assessment
  area: evidence
  topic: Occurrence and retained assay limits
  summary: No exact full-key LOTUS or CyanoMetDB occurrence row is retained for merochlorin
    D. The owner has no occurrence root. This bounded absence does not establish absence
    from organisms or literature, and occurrence in a companion does not fill the
    gap. Every one of the nine saved query frames was read. Exact-key ChEBI, CyanoMetDB,
    PubChem bioassay, BindingDB and AntibioticMech frames, including the derived empty
    ChEBI-origin query, return no rows for this owner. There is no actual AID or blank-AID
    sentinel. These retained-file negatives do not establish inactivity, absence from
    literature, potency or absence of biological targets.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  evidence_ids:
  - support-2778-source
  - support-2778-taxonomy
  - support-2778-curation
  - support-2778-scope
  - support-2778-query-mibig_compounds
  - support-2778-query-chebi_structures
  - support-2778-query-lotus_occurrences
  - support-2778-query-cyanometdb_occurrences
  - support-2778-query-npclassifier
  - support-2778-query-pubchem_bioassay
  - support-2778-query-bindingdb_targets
  - support-2778-query-antibioticmech_inchikeys
  - support-2778-query-chebi_origins
  dimensions:
  - name: occurrence_scope
    definition: Occurrence alone does not establish biosynthesis.
    value: No exact full-key LOTUS or CyanoMetDB occurrence row is retained for merochlorin
      D. The owner has no occurrence root. This bounded absence does not establish
      absence from organisms or literature, and occurrence in a companion does not
      fill the gap.
    evidence_ids:
    - support-2778-source
    - support-2778-taxonomy
    - support-2778-curation
    - support-2778-scope
    - support-2778-query-mibig_compounds
    - support-2778-query-chebi_structures
    - support-2778-query-lotus_occurrences
    - support-2778-query-cyanometdb_occurrences
    - support-2778-query-npclassifier
    - support-2778-query-pubchem_bioassay
    - support-2778-query-bindingdb_targets
    - support-2778-query-antibioticmech_inchikeys
    - support-2778-query-chebi_origins
  - name: assay_target_scope
    definition: Retained negatives are bounded predicates, not biological negatives.
    value: Every one of the nine saved query frames was read. Exact-key ChEBI, CyanoMetDB,
      PubChem bioassay, BindingDB and AntibioticMech frames, including the derived
      empty ChEBI-origin query, return no rows for this owner. There is no actual
      AID or blank-AID sentinel. These retained-file negatives do not establish inactivity,
      absence from literature, potency or absence of biological targets.
    evidence_ids:
    - support-2778-source
    - support-2778-taxonomy
    - support-2778-curation
    - support-2778-scope
    - support-2778-query-mibig_compounds
    - support-2778-query-chebi_structures
    - support-2778-query-lotus_occurrences
    - support-2778-query-cyanometdb_occurrences
    - support-2778-query-npclassifier
    - support-2778-query-pubchem_bioassay
    - support-2778-query-bindingdb_targets
    - support-2778-query-antibioticmech_inchikeys
    - support-2778-query-chebi_origins
- assessment_id: support-2778-classification-assessment
  area: consistency
  topic: Classification, filing and literal mechanism scope
  summary: NPClassifier returns Polyketides and Terpenoids with empty superclass and
    class fields. Empty strings are preserved as model output, not a missing model
    row. The two pathways explain UNCLASSIFIED filing. The retained fused-ring and
    chlorine features do not choose a single biosynthetic class or justify congener
    merging.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  evidence_ids:
  - support-2778-owner
  - support-2778-source
  - support-2778-filingpolicy
  - support-2778-motifs
  - support-2778-gates
  - support-2778-scope
  - support-2778-table-npclassifier
  dimensions:
  - name: classification_applicability
    definition: Source classes, model labels and graph observations remain distinct.
    value: NPClassifier returns Polyketides and Terpenoids with empty superclass and
      class fields. Empty strings are preserved as model output, not a missing model
      row. The two pathways explain UNCLASSIFIED filing. The retained fused-ring and
      chlorine features do not choose a single biosynthetic class or justify congener
      merging.
    evidence_ids:
    - support-2778-owner
    - support-2778-source
    - support-2778-filingpolicy
    - support-2778-motifs
    - support-2778-gates
    - support-2778-scope
    - support-2778-table-npclassifier
- assessment_id: support-2778-completion-assessment
  area: completeness
  topic: Earned review and unavailable authority
  summary: The complete current owner and exact source rows were read, actual canonical
    intake fixed current ownership and input hashes, and the one original saved molecular
    computation was assessed without replay. Literal mechanism, pathway, component,
    target, activity and related-record roots are absent; no maintained reader is
    assigned. Five local native commands passed, but full QC, complete OAK checks
    and external primary verification remain unavailable. Completion is partial; native
    SEEDED status and generated records remain unchanged.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-c4912c165f
  evidence_ids:
  - support-2778-intake
  - support-2778-intakeaccept
  - support-2778-plan
  - support-2778-planaccept
  - support-2778-notes
  - support-2778-gates
  - support-2778-data
  - support-2778-execution
  - support-2778-diagaccept
  - support-2778-scope
  dimensions:
  - name: review_completion
    definition: Scientific review does not promote native status or claim full external
      QC.
    value: The complete current owner and exact source rows were read, actual canonical
      intake fixed current ownership and input hashes, and the one original saved
      molecular computation was assessed without replay. Literal mechanism, pathway,
      component, target, activity and related-record roots are absent; no maintained
      reader is assigned. Five local native commands passed, but full QC, complete
      OAK checks and external primary verification remain unavailable. Completion
      is partial; native SEEDED status and generated records remain unchanged.
    evidence_ids:
    - support-2778-intake
    - support-2778-intakeaccept
    - support-2778-plan
    - support-2778-planaccept
    - support-2778-notes
    - support-2778-gates
    - support-2778-data
    - support-2778-execution
    - support-2778-diagaccept
    - support-2778-scope
findings: []
actions: []
limitations:
- Primary papers, spectra, sequences, live taxonomy and natural-product identity were
  not independently verified. Full QC, complete OAK and external primary checks remain
  unavailable.
- 'All ten saved comparison flags are true for this pair, including standard InChI,
  complete key, formula, formal charge and canonical isomeric/nonisomeric SMILES.
  The saved chirality-aware substructure map covers every atom and complete_atom_count_match
  is true. Its explicit full_graph_identity_established value remains false: this
  limited calculation does not independently prove full graph, natural-sample or experimental
  stereochemical identity. Both saved forms have two unspecified tetrahedral centres
  and one unspecified double-bond candidate, with no specified stereo entries. Source
  centres 12 and 26 map to InChI-derived centres 25 and 24. The unspecified source
  bond is C6=C8. The other two alkenes have repeated substituents at one end and are
  not additional E/Z candidates. The false source atom-stereo flag does not resolve
  any of these configurations.'
- Four undefined-stereo warning lines are globally unassigned. Exact-key negatives
  and literal root absence do not establish inactivity or universal absence.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh current 278 scientific judgments use current retained owner/source/intake/diagnostic
  evidence; earlier batches supply interface logic only.
- No generated record, source inventory, native status or campaign artifact was edited.
  No query, molecular parse, target invocation or outbound request occurred in this
  lane.
- ROOT appends five actual local native checks and three required unavailable checks.
  No maintained-reader check belongs to these zero-reader targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-278
```
