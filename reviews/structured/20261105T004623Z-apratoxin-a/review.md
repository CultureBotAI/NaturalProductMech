# Local evidence review: apratoxin A

- Review: 20261105T004623Z-apratoxin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T23:57:06.275589Z
- Finished UTC: 2026-11-05T00:46:23.192141Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Apratoxin A retains a specified depsipeptide structure with one representation-dependent amide/imidic shift. The locus grade, source producer assertion and Lyngbya occurrence remain distinct; case-varied DOI strings are one publication. No supported source correction is identified within partial local coverage.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2489; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-1b1273b287 | data/natural_products/unclassified/apratoxin-a.yaml | generated | apratoxin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-1b1273b287 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-1b1273b287 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-1b1273b287 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-1b1273b287 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-1b1273b287 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-1b1273b287 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-1b1273b287 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-1b1273b287 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and source correspondence

identity: supported. Targets: naturalproductmech:mibig-1b1273b287.

The minted identifier naturalproductmech:mibig-1b1273b287, full key KXUJXPZXILTXDA-JHMIWIOGSA-N and NPA012281 cross-reference remain tied to the MIBiG BGC0002542 apratoxin A source concept. Exact source correspondence does not independently verify the natural compound, producing strain or external cross-reference.

### Stored molecular forms and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-1b1273b287.

Both forms parse as neutral C45H69N5O8S, 59 atoms and 62 bonds. Eight comparisons agree, the two canonical SMILES comparisons are false and the direct map is empty. The SMILES-derived form has a 25-membered macrocycle, proline and thiazoline five-membered rings, an aryl ring, four amides and one ester. One C(=O)N site becomes C(O)=N on InChI reconstruction, leaving three amide motifs and an additional unspecified C=N bond. Ten specified tetrahedral centres and the E alkene persist. Ordering-dependent Cis/Trans potential-stereo descriptors do not override the unchanged E bond label. The source true flag describes extractor tetrahedral scope; full-graph and natural identity remain unestablished.

### Producer and locus evidence grades

provenance: supported. Targets: naturalproductmech:mibig-1b1273b287.

MIBiG BGC0002542 version 2 keeps Moorena bouillonii bAprat14 (2530358) at SOURCE_ASSERTION and MG890637.1 at CLUSTER_DEMONSTRATED through enzymatic assays, without retained locus coordinates. Source PKS/NRPS classes and locus evidence do not upgrade the native taxon claim. LOTUS Lyngbya majuscula (158786) occurrence is a different retained organism assertion, not proof that the named species and strain are interchangeable.

### Citation tier and history

evidence: supported. Targets: naturalproductmech:mibig-1b1273b287.

MIBiG DOI:10.1021/ja010453j is explicitly COMPOUND_BIOACTIVITY-level, while LOTUS retains DOI:10.1021/JA010453J. Case variants do not create independent publications. A bioactivity-level citation does not itself establish a specific native strain or a complete biosynthetic experiment. The two seed histories and SEEDED status remain unchanged.

### Occurrence and assay evidence scope

evidence: supported. Targets: naturalproductmech:mibig-1b1273b287.

The one LOTUS row reports Lyngbya majuscula occurrence; it does not independently demonstrate production by Moorena bouillonii bAprat14. No bioactivities, molecular_targets, causal graphs, pathway or components are present in the current owner. The raw citation tier is retained without inventing a numerical pharmacological assay from it, and the exact negative target/activity frames do not prove inactivity.

### Versioned classification applicability

consistency: supported. Targets: naturalproductmech:mibig-1b1273b287.

The versioned cyclic-peptide/depsipeptide classes are broadly compatible with the saved macrocycle, amide-bearing residues and ester linkage, while the tautomer-specific motif counts remain explicit. Model amino-acid/peptide and polyketide pathways are distinct from the source PKS/NRPS classes. No C5O sugar candidate is reported; glycoside=false remains a model annotation, not independent experimental proof.

### Review completion

completeness: unknown. Targets: naturalproductmech:mibig-1b1273b287.

The whole owner and two seed events, nine selected source frames with three positive rows, 37 accepted canonical inputs and both complete saved molecular forms were read. No supported finding or action follows solely from the disclosed representation difference. Coverage remains partial without fresh primary, taxonomy, native sequence/construct, full QC or complete OAK verification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2489-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/apratoxin-a.yaml; Whole current plaintext including complete curation_history | supports | Complete owner and all 2 history events personally read; current exact bytes retained. |
| support-2489-capture | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete captured owner, all present roots and history; absent roots are not replaced by inferred assertions. |
| support-2489-grounding-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/8/owner_document/identifier; /records/8/owner_document/label; /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts; /records/8/owner_document/xrefs; /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes | supports | Retained identifier, full key, source structure and exact present grounding/cross-reference fields. Fresh natural identity is not established. |
| support-2489-origin-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters; /records/8/owner_document/producer_taxon_groups | supports | Complete producer and locus assertions with separate grades, methods, coordinates and source classes where present. |
| support-2489-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete owner preserves present occurrences where any and absent bioactivity, molecular-target and mechanism roots; absence is scoped to this captured document. |
| support-2489-classification-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification; /records/8/owner_document/bgc_class; /records/8/owner_document/biosynthesis_origin | supports | Versioned model output, source BGC classes and UNCLASSIFIED filing remain separate assertions. |
| support-2489-direct-contexts | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json; /records/8/proposed_companion_paths; /records/8/direct_companion_predicates; /records/8/identity_comparison_paths; /records/8/additional_context_roles | context_only | Exact admitted context roles: no direct-BGC companion links; reciprocal Antimycin selected-owner comparison and A1B supplemental rule inputs are separately labelled where applicable. |
| support-2489-intake | /private/tmp/npm-review-work/shared-next-batch249/intakes/2489-inspect-001.json; /targets; /source | supports | Actual canonical target, source inputs and maintained ownership are retained. |
| support-2489-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch249/root-intake-acceptance-001.json; /status; /records/8; /source_plan; /verification | supports | ROOT accepts this original intake and the exact supplemented source plan. |
| support-2489-intake-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/support-prep/support-current249-last-five-molecular-intake-reading-001.json; /reading; /records/3/target; /records/3/intake; /coverage | supports | Support personally read all five target/ownership documents and 191 current input placements across 47 paths. |
| support-2489-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch249/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /verification | supports | ROOT accepts the retained original inventory; extraction is not primary-source verification. |
| support-2489-plan | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json; /records/8/proposed_input_paths; /records/8/proposed_input_count | supports | Final accepted input map agrees with this canonical intake. |
| support-2489-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch249/root-target-input-plan-acceptance-001.json; /status; /accepted; /verification | supports | ROOT accepts the original composed plan plus the separately preserved three-file A1B review-input supplement. |
| support-2489-source-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/support-prep/support-current249-assigned-source-reading-001.json; /primary_context_indices; /coverage; /primary_counts; /complete_reading_scope; /physical_verification; /per_owner_cautions; /global_limits | supports | Support personally read contexts 5–9: 45 frames, 15 positive rows and 200 fields, with exact physical/current joins. Other source-reading credits remain attributed. |
| support-2489-ROOT-source-reading | /private/tmp/npm-review-work/shared-next-batch249/root-current249-source-row-reading-001.json; /context_indices; /context_paths; /named_query_frames; /positive_row_placements; /positive_row_fields; /whole_payload_readings; /scientific_cautions | context_only | ROOT personally read Antimycin A context 4: nine frames, 185 rows and 1990 fields. Its broad-compound assay corpus is context only and does not transfer to A1B. |
| support-2489-source-notes | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | context_only | Joint notes preserve disjoint BGC 22/ROOT 185/Support 15/Native 0 source-row credits and exact source/curation boundaries. |
| support-2489-molecular-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/support-prep/support-current249-last-five-molecular-intake-reading-001.json; /reading; /coverage; /records/3; /representation_notes; /limits | supports | Support personally read all ten forms: 484 atom and 492 bond rows, all stereo/motif/map fields and 191 intake placements; no new molecular parse. |
| support-2489-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/15; /cached_taxonomy/whole_stanzas/25 | context_only | Complete relevant retained cache stanzas preserve taxon names and synonyms; they do not establish an assayed strain, native producer or fresh taxonomy. |
| support-2489-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-cached-taxonomy-reading-001.json; /scope; /complete_readings; /counts; /interpretation | context_only | Native complete cache/route interpretation remains attributed; Support separately read ten complete relevant selected stanzas. |
| support-2489-curation-scope | /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation; /assay_scope | context_only | The bounded implemented-table scan found no exact applicable replacement for these owners; lexical hits are not imported as record-specific evidence. |
| support-2489-chemistry | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/formula_comparison_scope; /records/8/comparisons; /records/8/atom_correspondence | supports | Eight true comparisons, two false canonical SMILES comparisons and an empty direct map; normalized identifiers do not establish fixed-form identity. |
| support-2489-topology | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json; /records/8/smiles; /records/8/inchi | supports | Complete saved atom/bond/ring/stereo/motif tables preserve representation-specific counts and every declared stereochemical assignment. No new parse or natural-state claim. |
| support-2489-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/8; /global_warning_count; /interpretation_boundary | supports | ROOT accepts this actual diagnostic record, preserving false comparisons where present and four global unassigned warnings. |
| support-2489-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Exact original diagnostic command/source, zero exit and streams, no retry or external request. |
| support-2489-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | supports | Four original undefined-stereo warnings remain global and unassigned to records. |
| support-2489-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2489-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2489-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2489-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2489-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame contains 1 positive placements; zeros are bounded to the retained exact predicate. |
| support-2489-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Complete retained physical row 3204, all 25 fields: BGC0002542 version 2; Moorena bouillonii bAprat14 SOURCE_ASSERTION, locus CLUSTER_DEMONSTRATED; DOI:10.1021/ja010453j at COMPOUND_BIOACTIVITY scope. Source structure, coordinates, methods and classes remain exact. |
| support-2489-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 3204 | context_only | Every retained field joins these exact current physical table rows; primary source-reading credits remain disjoint. |
| support-2489-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame contains 0 positive placements; zeros are bounded to the retained exact predicate. |
| support-2489-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame contains 1 positive placements; zeros are bounded to the retained exact predicate. |
| support-2489-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Complete retained physical row 3772, all 6 fields: Lyngbya majuscula (NCBITaxon:158786), DOI:10.1021/JA010453J; occurrence rather than demonstrated production or independent-study proof. |
| support-2489-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 3772 | context_only | Every retained field joins these exact current physical table rows; primary source-reading credits remain disjoint. |
| support-2489-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame contains 0 positive placements; zeros are bounded to the retained exact predicate. |
| support-2489-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame contains 1 positive placements; zeros are bounded to the retained exact predicate. |
| support-2489-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/npclassifier/matches/0 | supports | Complete retained physical row 1307, all 7 fields: npclassifier.gnps2.org@2026-09-07: Amino acids and Peptides&#124;Polyketides/Oligopeptides/Cyclic peptides&#124;Depsipeptides, glycoside=false; model assertion only. |
| support-2489-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 1307 | context_only | Every retained field joins these exact current physical table rows; primary source-reading credits remain disjoint. |
| support-2489-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame contains 0 positive placements; zeros are bounded to the retained exact predicate. |
| support-2489-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame contains 0 positive placements; zeros are bounded to the retained exact predicate. |
| support-2489-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame contains 0 positive placements; zeros are bounded to the retained exact predicate. |
| support-2489-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame contains 0 positive placements; zeros are bounded to the retained exact predicate. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-249/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-249/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-249/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-249/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-249/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; fresh papers, taxonomy, native sequences/constructs, assay protocols and natural identity were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Full-graph identity was not established. Both canonical SMILES comparisons are false and the direct atom map is empty; representation-specific motifs and unspecified stereo remain explicit.
- Four undefined-stereo warnings are global and unassigned. Producer, occurrence, locus, citation, model and assay scopes remain distinct; no source/status/history mutation was performed.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Whole selected raw/history and complete paired molecular tables were personally read. Support source credit15/200/45 remains separate from ROOT185/1990/9 and BGC22/225/36; Native0 source rows.
- Support read all191 last-five input placements47paths and ten complete relevant cache stanzas; Native taxonomy/curation interpretation and ROOT Antimycin A payload reading remain attributed.
- Support operated canonical intakes; Native operated original diagnostic/readers under ROOT delegation. Historical observer labels do not change operator attribution. All review/evidence timestamps use literal UTC Z.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T004623Z-apratoxin-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: apratoxin A'
started_at: '2026-11-04T23:57:06.275589Z'
finished_at: '2026-11-05T00:46:23.192141Z'
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
summary: Apratoxin A retains a specified depsipeptide structure with one representation-dependent
  amide/imidic shift. The locus grade, source producer assertion and Lyngbya occurrence
  remain distinct; case-varied DOI strings are one publication. No supported source
  correction is identified within partial local coverage.
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
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/unclassified/apratoxin-a.yaml
    sha256: 117447d3e1640c71f8171ad0a2cbf6afd5a688b75a4c5f0ec821fa73fdc11f73
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
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2489; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-1b1273b287
targets:
- target_id: naturalproductmech:mibig-1b1273b287
  path: data/natural_products/unclassified/apratoxin-a.yaml
  label: apratoxin A
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
  - naturalproductmech:mibig-1b1273b287
  command: just validate-strict data/natural_products/unclassified/andalusicin-a.yaml
    data/natural_products/unclassified/anditomin.yaml data/natural_products/unclassified/andrastin-a.yaml
    data/natural_products/unclassified/antalid.yaml data/natural_products/unclassified/antimycin-a.yaml
    data/natural_products/unclassified/antimycin-a1b.yaml data/natural_products/unclassified/ape-ec.yaml
    data/natural_products/unclassified/ape-vf.yaml data/natural_products/unclassified/apratoxin-a.yaml
    data/natural_products/unclassified/arthrofactin-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-249/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-1b1273b287
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-249/validate-all-001.tsv
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
  - naturalproductmech:mibig-1b1273b287
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
  - naturalproductmech:mibig-1b1273b287
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
  - naturalproductmech:mibig-1b1273b287
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-249/review-queue-001.tsv
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
  - naturalproductmech:mibig-1b1273b287
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-1b1273b287
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-1b1273b287
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2489-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/apratoxin-a.yaml
  locator: Whole current plaintext including complete curation_history
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Complete owner and all 2 history events personally read; current exact
    bytes retained.
  snapshot_sha256: 117447d3e1640c71f8171ad0a2cbf6afd5a688b75a4c5f0ec821fa73fdc11f73
- evidence_id: support-2489-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Complete captured owner, all present roots and history; absent roots are
    not replaced by inferred assertions.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: support-2489-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/8/owner_document/identifier; /records/8/owner_document/label;
    /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts;
    /records/8/owner_document/xrefs; /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Retained identifier, full key, source structure and exact present grounding/cross-reference
    fields. Fresh natural identity is not established.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: support-2489-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters;
    /records/8/owner_document/producer_taxon_groups
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Complete producer and locus assertions with separate grades, methods, coordinates
    and source classes where present.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: support-2489-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Complete owner preserves present occurrences where any and absent bioactivity,
    molecular-target and mechanism roots; absence is scoped to this captured document.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: support-2489-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification;
    /records/8/owner_document/bgc_class; /records/8/owner_document/biosynthesis_origin
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Versioned model output, source BGC classes and UNCLASSIFIED filing remain
    separate assertions.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: support-2489-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json
  locator: /records/8/proposed_companion_paths; /records/8/direct_companion_predicates;
    /records/8/identity_comparison_paths; /records/8/additional_context_roles
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: 'Exact admitted context roles: no direct-BGC companion links; reciprocal
    Antimycin selected-owner comparison and A1B supplemental rule inputs are separately
    labelled where applicable.'
  snapshot_sha256: 4c92dba7f8c9b89c7fe05a9e64e3721282d76814855c144975ff46e930b901b0
- evidence_id: support-2489-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249/intakes/2489-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Actual canonical target, source inputs and maintained ownership are retained.
  snapshot_sha256: fccc604ffbbe28918b92c3c17eb87452125458a95f0858defdc8d8a4285cd45d
- evidence_id: support-2489-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-intake-acceptance-001.json
  locator: /status; /records/8; /source_plan; /verification
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: ROOT accepts this original intake and the exact supplemented source plan.
  snapshot_sha256: f4ee1f9dc4160c60cc3201b9246bb2ee1bd3ec750d96493dccd37dbd1725a6e5
- evidence_id: support-2489-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/support-prep/support-current249-last-five-molecular-intake-reading-001.json
  locator: /reading; /records/3/target; /records/3/intake; /coverage
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Support personally read all five target/ownership documents and 191 current
    input placements across 47 paths.
  snapshot_sha256: 3b313ac5ae784dd7a10bdfb15cefb2d3a8fed8b1e645fccac63836e1d2bc7cb1
- evidence_id: support-2489-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /verification
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: ROOT accepts the retained original inventory; extraction is not primary-source
    verification.
  snapshot_sha256: b1a3f92b8d3520b9d2b9340020262955da8f1ff56b198036a88533e1d3c5f6cb
- evidence_id: support-2489-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json
  locator: /records/8/proposed_input_paths; /records/8/proposed_input_count
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Final accepted input map agrees with this canonical intake.
  snapshot_sha256: 4c92dba7f8c9b89c7fe05a9e64e3721282d76814855c144975ff46e930b901b0
- evidence_id: support-2489-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-target-input-plan-acceptance-001.json
  locator: /status; /accepted; /verification
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: ROOT accepts the original composed plan plus the separately preserved three-file
    A1B review-input supplement.
  snapshot_sha256: 68262c91ae1a1ebc2517faaa1f59c227db9a7d17f53a0a47f108b614d968ac7b
- evidence_id: support-2489-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/support-prep/support-current249-assigned-source-reading-001.json
  locator: /primary_context_indices; /coverage; /primary_counts; /complete_reading_scope;
    /physical_verification; /per_owner_cautions; /global_limits
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: 'Support personally read contexts 5–9: 45 frames, 15 positive rows and
    200 fields, with exact physical/current joins. Other source-reading credits remain
    attributed.'
  snapshot_sha256: dcb5ef9d60a191220d7a5f7f0b29b794fe08ba0f6d56d622d4b88a7eba609665
- evidence_id: support-2489-ROOT-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-current249-source-row-reading-001.json
  locator: /context_indices; /context_paths; /named_query_frames; /positive_row_placements;
    /positive_row_fields; /whole_payload_readings; /scientific_cautions
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: 'ROOT personally read Antimycin A context 4: nine frames, 185 rows and
    1990 fields. Its broad-compound assay corpus is context only and does not transfer
    to A1B.'
  snapshot_sha256: 60a0d18b4dde9699fff69bc1c459a499b0e01e003cc7156c2bb90af82b35d44d
- evidence_id: support-2489-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: Joint notes preserve disjoint BGC 22/ROOT 185/Support 15/Native 0 source-row
    credits and exact source/curation boundaries.
  snapshot_sha256: b326cf0f50a7ed128bba21bf3e4554fac446e8a221bdddcb80d0c6390818f2fb
- evidence_id: support-2489-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/support-prep/support-current249-last-five-molecular-intake-reading-001.json
  locator: /reading; /coverage; /records/3; /representation_notes; /limits
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: 'Support personally read all ten forms: 484 atom and 492 bond rows, all
    stereo/motif/map fields and 191 intake placements; no new molecular parse.'
  snapshot_sha256: 3b313ac5ae784dd7a10bdfb15cefb2d3a8fed8b1e645fccac63836e1d2bc7cb1
- evidence_id: support-2489-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/15; /cached_taxonomy/whole_stanzas/25
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: Complete relevant retained cache stanzas preserve taxon names and synonyms;
    they do not establish an assayed strain, native producer or fresh taxonomy.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: support-2489-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-cached-taxonomy-reading-001.json
  locator: /scope; /complete_readings; /counts; /interpretation
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: Native complete cache/route interpretation remains attributed; Support
    separately read ten complete relevant selected stanzas.
  snapshot_sha256: 781f62e73b1694225f8ccdca96b95bbc58bea281997f4ef1152a7ccf2d5ecc88
- evidence_id: support-2489-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation; /assay_scope
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: The bounded implemented-table scan found no exact applicable replacement
    for these owners; lexical hits are not imported as record-specific evidence.
  snapshot_sha256: 0cfa769044caf4976e7fec895a44e667bf21c3bc8d9a0cabd465916034f98ed1
  search_scope: '{"selected_identifier": "naturalproductmech:mibig-1b1273b287", "selected_full_key":
    "KXUJXPZXILTXDA-JHMIWIOGSA-N", "scope": "Eleven implemented retained tables and
    exact predicates; ignored-file-independent specified-file inventory, not a universal
    absence claim."}'
- evidence_id: support-2489-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/formula_comparison_scope;
    /records/8/comparisons; /records/8/atom_correspondence
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Eight true comparisons, two false canonical SMILES comparisons and an empty
    direct map; normalized identifiers do not establish fixed-form identity.
  snapshot_sha256: 352a767f6e142ac6b3ecad138717d8d108483f61c6631a3480518d2a833285e5
- evidence_id: support-2489-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/smiles; /records/8/inchi
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Complete saved atom/bond/ring/stereo/motif tables preserve representation-specific
    counts and every declared stereochemical assignment. No new parse or natural-state
    claim.
  snapshot_sha256: 352a767f6e142ac6b3ecad138717d8d108483f61c6631a3480518d2a833285e5
- evidence_id: support-2489-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/8; /global_warning_count; /interpretation_boundary
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: ROOT accepts this actual diagnostic record, preserving false comparisons
    where present and four global unassigned warnings.
  snapshot_sha256: 85f657ea1d785c1aca4e78bdcf54056041799b0913a9df5155fb43b6ed51e491
- evidence_id: support-2489-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Exact original diagnostic command/source, zero exit and streams, no retry
    or external request.
  snapshot_sha256: 7955c4e94046cc4fedde2ebda7bd56f32eb9cb544f5367b1955b30ae11d58c88
- evidence_id: support-2489-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Four original undefined-stereo warnings remain global and unassigned to
    records.
  snapshot_sha256: 630f8763242550c202276628c55519c500ae0c599aa5f666704d6e11be6016ab
- evidence_id: support-2489-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2489-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2489-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2489-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2489-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Saved mibig_compounds frame contains 1 positive placements; zeros are bounded
    to the retained exact predicate.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "KXUJXPZXILTXDA-JHMIWIOGSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/mibig_compounds",
    "scope": "Retained local inventory only, no replay or universal absence claim."}'
- evidence_id: support-2489-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: 'Complete retained physical row 3204, all 25 fields: BGC0002542 version
    2; Moorena bouillonii bAprat14 SOURCE_ASSERTION, locus CLUSTER_DEMONSTRATED; DOI:10.1021/ja010453j
    at COMPOUND_BIOACTIVITY scope. Source structure, coordinates, methods and classes
    remain exact.'
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: support-2489-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 3204
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: Every retained field joins these exact current physical table rows; primary
    source-reading credits remain disjoint.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2489-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Saved chebi_structures frame contains 0 positive placements; zeros are
    bounded to the retained exact predicate.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "KXUJXPZXILTXDA-JHMIWIOGSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/chebi_structures",
    "scope": "Retained local inventory only, no replay or universal absence claim."}'
- evidence_id: support-2489-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Saved lotus_occurrences frame contains 1 positive placements; zeros are
    bounded to the retained exact predicate.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "KXUJXPZXILTXDA-JHMIWIOGSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Retained local inventory only, no replay or universal absence claim."}'
- evidence_id: support-2489-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: 'Complete retained physical row 3772, all 6 fields: Lyngbya majuscula (NCBITaxon:158786),
    DOI:10.1021/JA010453J; occurrence rather than demonstrated production or independent-study
    proof.'
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: support-2489-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 3772
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: Every retained field joins these exact current physical table rows; primary
    source-reading credits remain disjoint.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2489-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame contains 0 positive placements; zeros
    are bounded to the retained exact predicate.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "KXUJXPZXILTXDA-JHMIWIOGSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Retained local inventory only, no replay or universal absence claim."}'
- evidence_id: support-2489-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Saved npclassifier frame contains 1 positive placements; zeros are bounded
    to the retained exact predicate.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "KXUJXPZXILTXDA-JHMIWIOGSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/npclassifier",
    "scope": "Retained local inventory only, no replay or universal absence claim."}'
- evidence_id: support-2489-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: 'Complete retained physical row 1307, all 7 fields: npclassifier.gnps2.org@2026-09-07:
    Amino acids and Peptides|Polyketides/Oligopeptides/Cyclic peptides|Depsipeptides,
    glycoside=false; model assertion only.'
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: support-2489-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 1307
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: context_only
  summary: Every retained field joins these exact current physical table rows; primary
    source-reading credits remain disjoint.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2489-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Saved pubchem_bioassay frame contains 0 positive placements; zeros are
    bounded to the retained exact predicate.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "KXUJXPZXILTXDA-JHMIWIOGSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Retained local inventory only, no replay or universal absence claim."}'
- evidence_id: support-2489-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Saved bindingdb_targets frame contains 0 positive placements; zeros are
    bounded to the retained exact predicate.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "KXUJXPZXILTXDA-JHMIWIOGSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Retained local inventory only, no replay or universal absence claim."}'
- evidence_id: support-2489-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame contains 0 positive placements; zeros
    are bounded to the retained exact predicate.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "KXUJXPZXILTXDA-JHMIWIOGSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Retained local inventory only, no replay or universal absence claim."}'
- evidence_id: support-2489-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T00:35:36.539194Z'
  support: supports
  summary: Saved chebi_origins frame contains 0 positive placements; zeros are bounded
    to the retained exact predicate.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/8/source_scope_inventory/joins/chebi_origins",
    "scope": "Retained local inventory only, no replay or universal absence claim."}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-249/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json
  accessed_at: '2026-11-05T00:00:36.010567Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 27ebd661adce0e3ead194e6f0d627ebecf75c8d49a30ea4594cbe1d40e3eaf61
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-249/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json
  accessed_at: '2026-11-05T00:01:00.665052Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: ad956e928d3adb01dc4ca3be63be5560456a61997bb7d9463bd40e44e29a321e
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-249/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json
  accessed_at: '2026-11-05T00:01:21.006602Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-249/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json
  accessed_at: '2026-11-05T00:01:56.490347Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-249/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json
  accessed_at: '2026-11-05T00:02:08.678647Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 37db480802437fd52339442d7179165d3a7097a76a08ad575413b5858998667f
assessments:
- area: identity
  topic: Retained identity and source correspondence
  outcome: supported
  summary: The minted identifier naturalproductmech:mibig-1b1273b287, full key KXUJXPZXILTXDA-JHMIWIOGSA-N
    and NPA012281 cross-reference remain tied to the MIBiG BGC0002542 apratoxin A
    source concept. Exact source correspondence does not independently verify the
    natural compound, producing strain or external cross-reference.
  assessment_id: support-2489-identity
  target_ids:
  - naturalproductmech:mibig-1b1273b287
  evidence_ids:
  - support-2489-grounding-owner
  - support-2489-chemistry
  - support-2489-direct-contexts
  - support-2489-source-reading
  - support-2489-query-chebi_structures
  - support-2489-source-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: KXUJXPZXILTXDA-JHMIWIOGSA-N; retained full key, not independently established
      natural identity.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2489-grounding-owner
    - support-2489-chemistry
    - support-2489-direct-contexts
    - support-2489-source-reading
    - support-2489-query-chebi_structures
    - support-2489-source-mibig_compounds-0
  - name: grounding_scope
    value: The minted identifier naturalproductmech:mibig-1b1273b287, full key KXUJXPZXILTXDA-JHMIWIOGSA-N
      and NPA012281 cross-reference remain tied to the MIBiG BGC0002542 apratoxin
      A source concept. Exact source correspondence does not independently verify
      the natural compound, producing strain or external cross-reference.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2489-grounding-owner
    - support-2489-chemistry
    - support-2489-direct-contexts
    - support-2489-source-reading
    - support-2489-query-chebi_structures
    - support-2489-source-mibig_compounds-0
- area: representation
  topic: Stored molecular forms and stereochemistry
  outcome: supported
  summary: Both forms parse as neutral C45H69N5O8S, 59 atoms and 62 bonds. Eight comparisons
    agree, the two canonical SMILES comparisons are false and the direct map is empty.
    The SMILES-derived form has a 25-membered macrocycle, proline and thiazoline five-membered
    rings, an aryl ring, four amides and one ester. One C(=O)N site becomes C(O)=N
    on InChI reconstruction, leaving three amide motifs and an additional unspecified
    C=N bond. Ten specified tetrahedral centres and the E alkene persist. Ordering-dependent
    Cis/Trans potential-stereo descriptors do not override the unchanged E bond label.
    The source true flag describes extractor tetrahedral scope; full-graph and natural
    identity remain unestablished.
  assessment_id: support-2489-representation
  target_ids:
  - naturalproductmech:mibig-1b1273b287
  evidence_ids:
  - support-2489-grounding-owner
  - support-2489-chemistry
  - support-2489-topology
  - support-2489-molecular-reading
  - support-2489-diagnostic-acceptance
  - support-2489-structure-schema
  - support-2489-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both forms parse as neutral C45H69N5O8S, 59 atoms and 62 bonds. Eight comparisons
      agree, the two canonical SMILES comparisons are false and the direct map is
      empty. The SMILES-derived form has a 25-membered macrocycle, proline and thiazoline
      five-membered rings, an aryl ring, four amides and one ester. One C(=O)N site
      becomes C(O)=N on InChI reconstruction, leaving three amide motifs and an additional
      unspecified C=N bond. Ten specified tetrahedral centres and the E alkene persist.
      Ordering-dependent Cis/Trans potential-stereo descriptors do not override the
      unchanged E bond label. The source true flag describes extractor tetrahedral
      scope; full-graph and natural identity remain unestablished.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2489-grounding-owner
    - support-2489-chemistry
    - support-2489-topology
    - support-2489-molecular-reading
    - support-2489-diagnostic-acceptance
    - support-2489-structure-schema
    - support-2489-stereo-method
  - name: representation_correspondence
    value: Both forms parse as neutral C45H69N5O8S, 59 atoms and 62 bonds. Eight comparisons
      agree, the two canonical SMILES comparisons are false and the direct map is
      empty. The SMILES-derived form has a 25-membered macrocycle, proline and thiazoline
      five-membered rings, an aryl ring, four amides and one ester. One C(=O)N site
      becomes C(O)=N on InChI reconstruction, leaving three amide motifs and an additional
      unspecified C=N bond. Ten specified tetrahedral centres and the E alkene persist.
      Ordering-dependent Cis/Trans potential-stereo descriptors do not override the
      unchanged E bond label. The source true flag describes extractor tetrahedral
      scope; full-graph and natural identity remain unestablished.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2489-grounding-owner
    - support-2489-chemistry
    - support-2489-topology
    - support-2489-molecular-reading
    - support-2489-diagnostic-acceptance
    - support-2489-structure-schema
    - support-2489-stereo-method
- area: provenance
  topic: Producer and locus evidence grades
  outcome: supported
  summary: MIBiG BGC0002542 version 2 keeps Moorena bouillonii bAprat14 (2530358)
    at SOURCE_ASSERTION and MG890637.1 at CLUSTER_DEMONSTRATED through enzymatic assays,
    without retained locus coordinates. Source PKS/NRPS classes and locus evidence
    do not upgrade the native taxon claim. LOTUS Lyngbya majuscula (158786) occurrence
    is a different retained organism assertion, not proof that the named species and
    strain are interchangeable.
  assessment_id: support-2489-provenance
  target_ids:
  - naturalproductmech:mibig-1b1273b287
  evidence_ids:
  - support-2489-origin-owner
  - support-2489-source-reading
  - support-2489-direct-contexts
  - support-2489-cached-taxonomy
  - support-2489-taxonomy-reading
  - support-2489-curation-scope
  - support-2489-source-mibig_compounds-0
  - support-2489-source-lotus_occurrences-0
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0002542 version 2 keeps Moorena bouillonii bAprat14 (2530358)
      at SOURCE_ASSERTION and MG890637.1 at CLUSTER_DEMONSTRATED through enzymatic
      assays, without retained locus coordinates. Source PKS/NRPS classes and locus
      evidence do not upgrade the native taxon claim. LOTUS Lyngbya majuscula (158786)
      occurrence is a different retained organism assertion, not proof that the named
      species and strain are interchangeable.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2489-origin-owner
    - support-2489-source-reading
    - support-2489-direct-contexts
    - support-2489-cached-taxonomy
    - support-2489-taxonomy-reading
    - support-2489-curation-scope
    - support-2489-source-mibig_compounds-0
    - support-2489-source-lotus_occurrences-0
  - name: producer_evidence
    value: MIBiG BGC0002542 version 2 keeps Moorena bouillonii bAprat14 (2530358)
      at SOURCE_ASSERTION and MG890637.1 at CLUSTER_DEMONSTRATED through enzymatic
      assays, without retained locus coordinates. Source PKS/NRPS classes and locus
      evidence do not upgrade the native taxon claim. LOTUS Lyngbya majuscula (158786)
      occurrence is a different retained organism assertion, not proof that the named
      species and strain are interchangeable.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2489-origin-owner
    - support-2489-source-reading
    - support-2489-direct-contexts
    - support-2489-cached-taxonomy
    - support-2489-taxonomy-reading
    - support-2489-curation-scope
    - support-2489-source-mibig_compounds-0
    - support-2489-source-lotus_occurrences-0
  - name: locus_evidence
    value: MIBiG BGC0002542 version 2 keeps Moorena bouillonii bAprat14 (2530358)
      at SOURCE_ASSERTION and MG890637.1 at CLUSTER_DEMONSTRATED through enzymatic
      assays, without retained locus coordinates. Source PKS/NRPS classes and locus
      evidence do not upgrade the native taxon claim. LOTUS Lyngbya majuscula (158786)
      occurrence is a different retained organism assertion, not proof that the named
      species and strain are interchangeable.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2489-origin-owner
    - support-2489-source-reading
    - support-2489-direct-contexts
    - support-2489-cached-taxonomy
    - support-2489-taxonomy-reading
    - support-2489-curation-scope
    - support-2489-source-mibig_compounds-0
    - support-2489-source-lotus_occurrences-0
- area: evidence
  topic: Citation tier and history
  outcome: supported
  summary: MIBiG DOI:10.1021/ja010453j is explicitly COMPOUND_BIOACTIVITY-level, while
    LOTUS retains DOI:10.1021/JA010453J. Case variants do not create independent publications.
    A bioactivity-level citation does not itself establish a specific native strain
    or a complete biosynthetic experiment. The two seed histories and SEEDED status
    remain unchanged.
  assessment_id: support-2489-citations
  target_ids:
  - naturalproductmech:mibig-1b1273b287
  evidence_ids:
  - support-2489-owner
  - support-2489-origin-owner
  - support-2489-occurrence-activity-owner
  - support-2489-source-reading
  - support-2489-direct-contexts
  - support-2489-source-mibig_compounds-0
  - support-2489-source-lotus_occurrences-0
  - support-2489-source-npclassifier-0
  dimensions:
  - name: citation_scope
    value: MIBiG DOI:10.1021/ja010453j is explicitly COMPOUND_BIOACTIVITY-level, while
      LOTUS retains DOI:10.1021/JA010453J. Case variants do not create independent
      publications. A bioactivity-level citation does not itself establish a specific
      native strain or a complete biosynthetic experiment. The two seed histories
      and SEEDED status remain unchanged.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2489-owner
    - support-2489-origin-owner
    - support-2489-occurrence-activity-owner
    - support-2489-source-reading
    - support-2489-direct-contexts
    - support-2489-source-mibig_compounds-0
    - support-2489-source-lotus_occurrences-0
    - support-2489-source-npclassifier-0
- area: evidence
  topic: Occurrence and assay evidence scope
  outcome: supported
  summary: The one LOTUS row reports Lyngbya majuscula occurrence; it does not independently
    demonstrate production by Moorena bouillonii bAprat14. No bioactivities, molecular_targets,
    causal graphs, pathway or components are present in the current owner. The raw
    citation tier is retained without inventing a numerical pharmacological assay
    from it, and the exact negative target/activity frames do not prove inactivity.
  assessment_id: support-2489-occurrence
  target_ids:
  - naturalproductmech:mibig-1b1273b287
  evidence_ids:
  - support-2489-occurrence-activity-owner
  - support-2489-direct-contexts
  - support-2489-cached-taxonomy
  - support-2489-taxonomy-reading
  - support-2489-curation-scope
  - support-2489-source-reading
  - support-2489-query-lotus_occurrences
  - support-2489-query-chebi_origins
  - support-2489-query-cyanometdb_occurrences
  - support-2489-query-pubchem_bioassay
  - support-2489-query-bindingdb_targets
  - support-2489-query-antibioticmech_inchikeys
  - support-2489-source-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    value: The one LOTUS row reports Lyngbya majuscula occurrence; it does not independently
      demonstrate production by Moorena bouillonii bAprat14. No bioactivities, molecular_targets,
      causal graphs, pathway or components are present in the current owner. The raw
      citation tier is retained without inventing a numerical pharmacological assay
      from it, and the exact negative target/activity frames do not prove inactivity.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2489-occurrence-activity-owner
    - support-2489-direct-contexts
    - support-2489-cached-taxonomy
    - support-2489-taxonomy-reading
    - support-2489-curation-scope
    - support-2489-source-reading
    - support-2489-query-lotus_occurrences
    - support-2489-query-chebi_origins
    - support-2489-query-cyanometdb_occurrences
    - support-2489-query-pubchem_bioassay
    - support-2489-query-bindingdb_targets
    - support-2489-query-antibioticmech_inchikeys
    - support-2489-source-lotus_occurrences-0
  - name: assay_target_scope
    value: The one LOTUS row reports Lyngbya majuscula occurrence; it does not independently
      demonstrate production by Moorena bouillonii bAprat14. No bioactivities, molecular_targets,
      causal graphs, pathway or components are present in the current owner. The raw
      citation tier is retained without inventing a numerical pharmacological assay
      from it, and the exact negative target/activity frames do not prove inactivity.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2489-occurrence-activity-owner
    - support-2489-direct-contexts
    - support-2489-cached-taxonomy
    - support-2489-taxonomy-reading
    - support-2489-curation-scope
    - support-2489-source-reading
    - support-2489-query-lotus_occurrences
    - support-2489-query-chebi_origins
    - support-2489-query-cyanometdb_occurrences
    - support-2489-query-pubchem_bioassay
    - support-2489-query-bindingdb_targets
    - support-2489-query-antibioticmech_inchikeys
    - support-2489-source-lotus_occurrences-0
- area: consistency
  topic: Versioned classification applicability
  outcome: supported
  summary: The versioned cyclic-peptide/depsipeptide classes are broadly compatible
    with the saved macrocycle, amide-bearing residues and ester linkage, while the
    tautomer-specific motif counts remain explicit. Model amino-acid/peptide and polyketide
    pathways are distinct from the source PKS/NRPS classes. No C5O sugar candidate
    is reported; glycoside=false remains a model annotation, not independent experimental
    proof.
  assessment_id: support-2489-classification
  target_ids:
  - naturalproductmech:mibig-1b1273b287
  evidence_ids:
  - support-2489-classification-owner
  - support-2489-chemistry
  - support-2489-topology
  - support-2489-classification-seeder
  - support-2489-source-mibig_compounds-0
  - support-2489-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: The versioned cyclic-peptide/depsipeptide classes are broadly compatible
      with the saved macrocycle, amide-bearing residues and ester linkage, while the
      tautomer-specific motif counts remain explicit. Model amino-acid/peptide and
      polyketide pathways are distinct from the source PKS/NRPS classes. No C5O sugar
      candidate is reported; glycoside=false remains a model annotation, not independent
      experimental proof.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2489-classification-owner
    - support-2489-chemistry
    - support-2489-topology
    - support-2489-classification-seeder
    - support-2489-source-mibig_compounds-0
    - support-2489-source-npclassifier-0
- area: completeness
  topic: Review completion
  outcome: unknown
  summary: The whole owner and two seed events, nine selected source frames with three
    positive rows, 37 accepted canonical inputs and both complete saved molecular
    forms were read. No supported finding or action follows solely from the disclosed
    representation difference. Coverage remains partial without fresh primary, taxonomy,
    native sequence/construct, full QC or complete OAK verification.
  assessment_id: support-2489-completion
  target_ids:
  - naturalproductmech:mibig-1b1273b287
  evidence_ids:
  - support-2489-owner
  - support-2489-capture
  - support-2489-intake
  - support-2489-intake-acceptance
  - support-2489-intake-reading
  - support-2489-inventory-acceptance
  - support-2489-plan
  - support-2489-plan-acceptance
  - support-2489-source-reading
  - support-2489-source-notes
  - support-2489-molecular-reading
  - support-2489-diagnostic-acceptance
  - support-2489-diagnostic-execution
  - support-2489-diagnostic-stderr
  - support-2489-review-profile
  dimensions:
  - name: review_completion
    value: The whole owner and two seed events, nine selected source frames with three
      positive rows, 37 accepted canonical inputs and both complete saved molecular
      forms were read. No supported finding or action follows solely from the disclosed
      representation difference. Coverage remains partial without fresh primary, taxonomy,
      native sequence/construct, full QC or complete OAK verification.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2489-owner
    - support-2489-capture
    - support-2489-intake
    - support-2489-intake-acceptance
    - support-2489-intake-reading
    - support-2489-inventory-acceptance
    - support-2489-plan
    - support-2489-plan-acceptance
    - support-2489-source-reading
    - support-2489-source-notes
    - support-2489-molecular-reading
    - support-2489-diagnostic-acceptance
    - support-2489-diagnostic-execution
    - support-2489-diagnostic-stderr
    - support-2489-review-profile
findings: []
actions: []
limitations:
- Retained local evidence only; fresh papers, taxonomy, native sequences/constructs,
  assay protocols and natural identity were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Full-graph identity was not established. Both canonical SMILES comparisons are false
  and the direct atom map is empty; representation-specific motifs and unspecified
  stereo remain explicit.
- Four undefined-stereo warnings are global and unassigned. Producer, occurrence,
  locus, citation, model and assay scopes remain distinct; no source/status/history
  mutation was performed.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Whole selected raw/history and complete paired molecular tables were personally
  read. Support source credit15/200/45 remains separate from ROOT185/1990/9 and BGC22/225/36;
  Native0 source rows.
- Support read all191 last-five input placements47paths and ten complete relevant
  cache stanzas; Native taxonomy/curation interpretation and ROOT Antimycin A payload
  reading remain attributed.
- Support operated canonical intakes; Native operated original diagnostic/readers
  under ROOT delegation. Historical observer labels do not change operator attribution.
  All review/evidence timestamps use literal UTC Z.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-249
```
