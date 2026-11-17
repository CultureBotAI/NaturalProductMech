# Local evidence review: hancockiamide F

- Review: 20261106T072452Z-hancockiamide-f
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T06:34:52.568402Z
- Finished UTC: 2026-11-06T07:24:52.284926Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Hancockiamide F retains a distinct acyclic nitrogen framework with an N-acetyl amide, a ketone and a second amide. Its stored forms regenerate the same declared key but differ at the secondary amide/imidic-acid representation. Both canonical comparisons remain false and the atom map is empty; this bounded difference does not establish an incorrect source structure or natural identity.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2673; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-feede3fe88 | data/natural_products/unclassified/hancockiamide-f.yaml | generated | hancockiamide F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-feede3fe88 | The accepted original diagnostic parsed both stored forms and retained every comparison flag. Formula, net charge, Standard InChI and full key agree within this owner. |
| strict_ten | passed | True | naturalproductmech:mibig-feede3fe88 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-feede3fe88 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-feede3fe88 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-feede3fe88 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-feede3fe88 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-feede3fe88 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-feede3fe88 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-feede3fe88 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### identity

identity: supported. Targets: naturalproductmech:mibig-feede3fe88.

Both saved forms regenerate KBQGWSPBIGCQSN-ODUIWNOOSA-N, with equal formula, net charge and Standard InChI. The MIBiG full key and NPA033184 assertion are retained. Matching normalized identifiers supports local encoded consistency but does not adjudicate natural identity or a particular tautomer.

### representation

representation: supported. Targets: naturalproductmech:mibig-feede3fe88.

The SMILES form has three benzene rings and a fused five-membered methylenedioxy ring, with no nitrogen-containing ring. Its acyclic chain contains a ketone, a tertiary N-acetyl amide and a secondary amide. In the InChI reconstruction, the latter appears as C(OH)=N with a terminal hydroxyl oxygen; the ketone and N-acetyl amide remain. Carbonyl counts change from three to two and amide counts from two to one. The five-membered methylenedioxy ring shares an aromatic bond. The single S tetrahedral centre persists at SMILES atom 13 and InChI atom 25, and the E alkene remains specified. The reconstructed imidic C=N contributes one new unspecified double-bond entry. This representation-bound geometry does not contradict the source stereo_complete=true flag, whose maintained scope concerns undefined tetrahedral centres. Formula C31H32N2O6, neutral charge, Standard InChI and full declared key agree, as do atom and bond counts. Both canonical comparisons are false and the attempted atom map is empty. The saved mobile-hydrogen layer and the paired amide/imidic motif support a normalization explanation, without proving a complete cross-form graph match or the biologically correct tautomer.

### provenance

provenance: supported. Targets: naturalproductmech:mibig-feede3fe88.

Hancockiamide F retains Aspergillus hancockii (NCBITaxon:1873369) with SOURCE_ASSERTION producer support and the BGC0002264 locus MBFL02000005.1:62010–93497 with CLUSTER_DEMONSTRATED support. Heterologous expression and enzymatic assays are retained source method labels, not newly verified experiments in this review.

### citations

evidence: supported. Targets: naturalproductmech:mibig-feede3fe88.

F is compound index 6 in the questionable, unknown-completeness BGC0002264 version 3 entry. PMID:33242032 is entry-level, and the LOTUS occurrence cites DOI:10.1039/D0OB02243H. Neither is treated as a freshly inspected compound-specific mechanism paper.

### occurrence_activity

evidence: supported. Targets: naturalproductmech:mibig-feede3fe88.

The single LOTUS occurrence names Aspergillus hancockii. It does not establish strain-specific production or a molecular target. No actual AID or BindingDB target match is present in the saved exact-query frames; owner-root absence is not a claim of inactivity.

### classification

consistency: supported. Targets: naturalproductmech:mibig-feede3fe88.

The acyclic amide-containing chain and aromatic substitution are compatible with the broad retained Amino acids and Peptides and Shikimates and Phenylpropanoids outputs. Its topology differs from A’s and E’s piperazine framework. Empty family fields remain literal and the model labels do not assign a biosynthetic step. The current np_pathway=UNCLASSIFIED follows the maintained filing rule for two returned pathway labels: both predictions are retained in np_classification. This is consistent filing and does not imply missing classifications or biological pathway absence.

### completion

completeness: supported. Targets: naturalproductmech:mibig-feede3fe88.

The complete owner and history, all nine saved query frames and both complete saved molecular forms were read; 49 actual input hashes and ownership declarations were verified. The review preserves the accepted local diagnostic and five native checks, while full QC, OAK, primary-publication access and live authority verification remain unavailable. There is no declared mechanism, component or pathway requiring a maintained reader.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2673-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/hancockiamide-f.yaml; Complete plaintext and curation_history | supports | The complete current owner and every history entry were personally read; historical assertions do not confer fresh authority access. |
| bgc-2673-identity | /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json; /records/2/owner_document/identifier; /records/2/owner_document/label; /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status | supports | Exact current identity, structure encodings, source concepts and grounding; natural identity remains separate. |
| bgc-2673-history | /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json; /records/2/owner_document/curation_history | supports | All 3 retained history entries preserve their original scope; no primary-publication access is inherited. |
| bgc-2673-provenance | /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/source_concepts | supports | Producer and locus assertions retain separate evidence grades, genomic scope and reference grain. |
| bgc-2673-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json; /records/2/owner_document/occurrences | supports | Current owner occurrence assertions are retained at their recorded granularity; occurrence does not establish production, activity or molecular mechanism. |
| bgc-2673-xrefs | /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json; /records/2/owner_document/xrefs | supports | Literal cross-references are retained as assertions; current external authority content was not accessed. |
| bgc-2673-classification-owner | /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json; /records/2/owner_document/np_pathway; /records/2/owner_document/biosynthesis_origin; /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class | supports | Retained filing, normalized BGC classes and computed classification fields; raw subclasses remain separately scoped. |
| bgc-2673-mechanism-activity-scope | /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json; /records/2/owner_document | context_only | This complete owner has no mechanism, pathway, molecular-target, declared-component or bioactivity root; no maintained reader applies. |
| bgc-2673-intake | /private/tmp/npm-review-work/shared-next-batch268/intakes-001/2673-inspect-001.json; /source; /targets | supports | Actual canonical inspection preserves all 49 current input hashes and complete ownership declarations. Input capture is not whole-table scientific reading. |
| bgc-2673-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch268/root-current268-intake-acceptance-001.json; /accepted; /summary | supports | ROOT accepted the original canonical inspections and exact 486-input/57-path scope. |
| bgc-2673-plan | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-target-input-plan-001.json; /records/2; /source_placement_count; /unique_source_path_count | supports | The accepted original input plan equals this actual intake, including exact companion and additional roles. |
| bgc-2673-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch268/root-current268-source-plan-acceptance-001.json; /accepted; /plan | supports | ROOT accepted the original composed plan; no composition was replayed. |
| bgc-2673-chemistry | /private/tmp/npm-review-work/shared-next-batch268/chemistry-local/diagnostic-DATA-001.json; /records/2 | supports | Both complete saved forms and all atom, bond, ring, stereo and motif fields were personally read. Both canonical comparisons remain false and the attempted atom map is empty; normalized identifier equality does not establish full graph identity. |
| bgc-2673-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch268/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /full_graph_identity_established; /scientific_verdict_claimed | supports | ROOT accepted the original diagnostic evidence; acceptance does not establish natural identity or complete graph correspondence. |
| bgc-2673-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch268/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr | supports | The original twenty-form diagnostic closed once with exit 0 and preserved genuine command and streams. |
| bgc-2673-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch268/chemistry-local/diagnostic-original-001.stderr; Complete original stderr | context_only | The complete original stderr is empty. No warning is assigned or carried from a prior batch. |
| bgc-2673-molecular-reading | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-current268-first-five-molecular-intake-reading-001.json; /records/2; /reading_attribution; /limitations | supports | Personal whole saved-table and actual-intake reading, including exact form-specific topology and stereochemistry. |
| bgc-2673-gates | /private/tmp/npm-review-work/shared-next-batch268/root-native-gates-acceptance-001.json; /checks_passed; /all_native_gates_passed; /unavailable_required_gates; /complete_selected_queue_rows | supports | Five local checks passed; full QC and OAK remain unavailable. Queue rows are leads, not independently confirmed scientific defects. |
| bgc-2673-source-reading | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-current268-assigned-source-reading-001.json; /records/2; /full_meaning_scope; /boundaries | supports | All assigned positive dictionaries and negative query boundaries for this owner were personally read; retained citations are not freshly read papers. |
| bgc-2673-source-notes | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /reading_boundaries | supports | Disjoint complete source reading preserves 19 BGC and 29 Support row placements, with zero Native primary-row credit. |
| bgc-2673-taxonomy | /private/tmp/npm-review-work/shared-next-batch268-tentative/native-prep/native-current268-cached-taxonomy-reading-001.json; /context_interpretations/6; /interpretation | partial | Owner-local retained taxonomy labels and IDs; these six cached stanzas have no synonym lines, and no new rank, lineage or freshness verification is inferred. |
| bgc-2673-curation | /private/tmp/npm-review-work/shared-next-batch268-tentative/native-prep/native-current268-implemented-curation-scan-001.json; /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope; /interpretation | context_only | The bounded implemented-curation scan has no exact applicable predicate; this is not proof that all possible scientific issues are absent. |
| bgc-2673-assay-curation | /private/tmp/npm-review-work/shared-next-batch268-tentative/native-prep/native-current268-implemented-curation-scan-001.json; /assay_scope | context_only | No actual AID occurs in the accepted batch. Its sole blank-AID sentinel belongs to selected Hangtaimycin and is not an assay or inactivity result. |
| bgc-2673-stereo-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392-396: stereo_complete description | context_only | The maintained flag concerns undefined stereocentres, not complete double-bond geometry. |
| bgc-2673-stereo-extractor | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters predicate | context_only | The retained extractor flag uses unassigned tetrahedral tags; no extractor was invoked. |
| bgc-2673-stereo-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; line 995: stereo_complete assignment | context_only | The maintained seeder copies the stored atom-centred flag; no independent stereochemical experiment is implied. |
| bgc-2673-direct-contexts | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-target-input-plan-001.json; /records/2/proposed_companion_paths; /records/2/direct_companion_predicates | context_only | 5 immediate shared-BGC companion inputs are present. Shared locus context does not establish equivalent identity, independent experiments or transferable activity. |
| bgc-2673-companion-0 | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/0 | context_only | This exact shared-BGC context is captured as a separate owner. Selected first-five reading is mine; the other selected and unselected context reading is separately attributed to Support. No structure, activity or experimental claim is transferred. |
| bgc-2673-companion-1 | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/1 | context_only | This exact shared-BGC context is captured as a separate owner. Selected first-five reading is mine; the other selected and unselected context reading is separately attributed to Support. No structure, activity or experimental claim is transferred. |
| bgc-2673-companion-2 | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/2 | context_only | This exact shared-BGC context is captured as a separate owner. Selected first-five reading is mine; the other selected and unselected context reading is separately attributed to Support. No structure, activity or experimental claim is transferred. |
| bgc-2673-companion-3 | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/4 | context_only | This exact shared-BGC context is captured as a separate owner. Selected first-five reading is mine; the other selected and unselected context reading is separately attributed to Support. No structure, activity or experimental claim is transferred. |
| bgc-2673-companion-4 | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/5 | context_only | This exact shared-BGC context is captured as a separate owner. Selected first-five reading is mine; the other selected and unselected context reading is separately attributed to Support. No structure, activity or experimental claim is transferred. |
| bgc-2673-support-context-reading | /private/tmp/npm-review-work/shared-next-batch268-tentative/support-prep/support-current268-assigned-source-reading-002.json; /contexts; /cautions | context_only | Support separately read the complete last-five and four unselected query contexts. This evidence retains that attribution without adding primary row credit to this review. |
| bgc-2673-support-companion-reading | /private/tmp/npm-review-work/shared-next-batch268-tentative/support-prep/support-current268-four-companion-whole-reading-001.json; Complete attributed raw-owner/history reading receipt | context_only | Support separately read the four complete unselected companion owners and histories; this is context, not equivalent identity or fresh experimental support. |
| bgc-2673-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/mibig_compounds | supports | The complete saved mibig_compounds frame contains 1 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2673-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 2735-2735; raw record sha256 83de795f0f270797556be5505bde2b72e9200c7a98c13f3676093ba95505b193 | supports | All 25 fields of the exact physical source record were read. This is retained database content, not fresh primary-paper evidence. |
| bgc-2673-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_structures | context_only | The complete saved chebi_structures frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2673-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences | supports | The complete saved lotus_occurrences frame contains 1 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2673-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 3569-3569; raw record sha256 14a6ecde3d5812890f76c415c77565a7488de064c15122abf9b10086668f58f7 | supports | All 6 fields of the exact physical source record were read. This is retained database content, not fresh primary-paper evidence. |
| bgc-2673-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences | context_only | The complete saved cyanometdb_occurrences frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2673-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/npclassifier | supports | The complete saved npclassifier frame contains 1 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2673-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 1220-1220; raw record sha256 32c8f10582c4cbdea417e5fcc096530a3b2acc3f9b8da40e810f81911f73fef8 | supports | All 7 fields of the exact physical source record were read. This is retained database content, not fresh primary-paper evidence. |
| bgc-2673-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/pubchem_bioassay | context_only | The complete saved pubchem_bioassay frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2673-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/bindingdb_targets | context_only | The complete saved bindingdb_targets frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2673-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | The complete saved antibioticmech_inchikeys frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2673-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins | context_only | The complete saved chebi_origins frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2673-filing-rule | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295–306: choose_pathway | supports | The maintained seeder files two returned pathway labels as UNCLASSIFIED while retaining both in np_classification. This explains the current filing without claiming biological pathway absence. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-268/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-268/native-current268-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-268/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-268/native-current268-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-268/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-268/native-current268-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-268/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-268/native-current268-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-268/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-268/native-current268-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Local stored-form consistency does not independently establish natural identity, biological activity or primary experimental mechanism.
- Source producer, locus and citation grades remain at their recorded granularity; no source independence or strain experiment is inferred.
- Full QC and OAK checks, live authorities and primary-paper verification remain unavailable under the outbound hold.
- Both canonical comparisons and the attempted atom map remain unresolved for Hancockiamide F; its observed secondary-amide/imidic change is explicitly scoped.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Five shared-BGC companions are contextual inputs. F’s full key, C31H32N2O6 formula and NPA033184 identifier remain distinct; a common source entry does not supply an unrecorded conversion from another Hancockiamide.
- Original diagnostic stderr is empty. No previous-batch warning, finding or scientific verdict is carried.
- Companion whole-owner and query reading is separately attributed to Support where outside the selected first-five scope; no companion activity or stereochemistry is transferred.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T072452Z-hancockiamide-f
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: hancockiamide F'
started_at: '2026-11-06T06:34:52.568402Z'
finished_at: '2026-11-06T07:24:52.284926Z'
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
summary: Hancockiamide F retains a distinct acyclic nitrogen framework with an N-acetyl
  amide, a ketone and a second amide. Its stored forms regenerate the same declared
  key but differ at the secondary amide/imidic-acid representation. Both canonical
  comparisons remain false and the atom map is empty; this bounded difference does
  not establish an incorrect source structure or natural identity.
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
  - path: data/natural_products/alkaloids/hancockiamide-b.yaml
    sha256: 58b9d5b380eacc91cc1d3aab37d029a47c688385e40dc571ac81f02500765eb2
    role: context
  - path: data/natural_products/alkaloids/hancockiamide-c.yaml
    sha256: f5455801d553581ab6b134955ecb527b48fcdc2aa4e10c86e498aee815ed3335
    role: context
  - path: data/natural_products/alkaloids/hancockiamide-d.yaml
    sha256: 758bf46b4fe8f6572a482e563b64e2899f1d012dcd59d74cb761270fdc8e741f
    role: context
  - path: data/natural_products/unclassified/hancockiamide-a.yaml
    sha256: 8946f2d9f892afac115ce082b338dfe441e6bab7061aa0578e69dbb49d1d1b00
    role: context
  - path: data/natural_products/unclassified/hancockiamide-e.yaml
    sha256: aa9e6d889b312a13eebc993e9897fad99e6d6d4f9fbd2d3320e1794e7986fab8
    role: context
  - path: data/natural_products/unclassified/hancockiamide-f.yaml
    sha256: 0a76a30e92f1ab582337d7b45edb041b954d396f7014bcb34d111714c8c740d4
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
  selection: Campaign path order 2673; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-feede3fe88
targets:
- target_id: naturalproductmech:mibig-feede3fe88
  path: data/natural_products/unclassified/hancockiamide-f.yaml
  label: hancockiamide F
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
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch268/chemistry-local/diagnose268-001.py
    3595628d557b45770a6c93211614701b3bf8a92ece3acf31087307508f2d2816 803cb2ee908d0d1c3a6f0a7ae1306caf8f05181e6918d0d3792452d8a2593b3d
    f593c4784faf3618eba98cf9ae5505d49a1d3096bc4836320a3e6740a1672de1
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The accepted original diagnostic parsed both stored forms and retained
    every comparison flag. Formula, net charge, Standard InChI and full key agree
    within this owner.
  scope_note: Shared original twenty-form execution, without rerun. Both canonical
    comparisons remain false and the attempted atom map is empty; normalized identifier
    equality does not establish full graph identity. No natural-identity, complete
    stereochemical or biological-function certification follows.
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  evidence_ids:
  - bgc-2673-chemistry
  - bgc-2673-diagnostic-acceptance
  - bgc-2673-diagnostic-execution
  - bgc-2673-diagnostic-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  command: just validate-strict data/natural_products/unclassified/hancockiamide-a.yaml
    data/natural_products/unclassified/hancockiamide-e.yaml data/natural_products/unclassified/hancockiamide-f.yaml
    data/natural_products/unclassified/hangtaimycin.yaml data/natural_products/unclassified/hapalosin-a.yaml
    data/natural_products/unclassified/hapalosin-c.yaml data/natural_products/unclassified/hapalosin-d.yaml
    data/natural_products/unclassified/hapalosin-e.yaml data/natural_products/unclassified/hapalosin-f.yaml
    data/natural_products/unclassified/hapalosin-g.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-268/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-feede3fe88
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-268/validate-all-001.tsv
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
  - naturalproductmech:mibig-feede3fe88
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
  - naturalproductmech:mibig-feede3fe88
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
  - naturalproductmech:mibig-feede3fe88
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-268/review-queue-001.tsv
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
  - naturalproductmech:mibig-feede3fe88
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2673-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/hancockiamide-f.yaml
  locator: Complete plaintext and curation_history
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: The complete current owner and every history entry were personally read;
    historical assertions do not confer fresh authority access.
  snapshot_sha256: 0a76a30e92f1ab582337d7b45edb041b954d396f7014bcb34d111714c8c740d4
- evidence_id: bgc-2673-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json
  locator: /records/2/owner_document/identifier; /records/2/owner_document/label;
    /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts;
    /records/2/owner_document/grounding_status
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: Exact current identity, structure encodings, source concepts and grounding;
    natural identity remains separate.
  snapshot_sha256: 803cb2ee908d0d1c3a6f0a7ae1306caf8f05181e6918d0d3792452d8a2593b3d
- evidence_id: bgc-2673-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json
  locator: /records/2/owner_document/curation_history
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: All 3 retained history entries preserve their original scope; no primary-publication
    access is inherited.
  snapshot_sha256: 803cb2ee908d0d1c3a6f0a7ae1306caf8f05181e6918d0d3792452d8a2593b3d
- evidence_id: bgc-2673-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters;
    /records/2/owner_document/source_concepts
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: Producer and locus assertions retain separate evidence grades, genomic
    scope and reference grain.
  snapshot_sha256: 803cb2ee908d0d1c3a6f0a7ae1306caf8f05181e6918d0d3792452d8a2593b3d
- evidence_id: bgc-2673-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json
  locator: /records/2/owner_document/occurrences
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: Current owner occurrence assertions are retained at their recorded granularity;
    occurrence does not establish production, activity or molecular mechanism.
  snapshot_sha256: 803cb2ee908d0d1c3a6f0a7ae1306caf8f05181e6918d0d3792452d8a2593b3d
- evidence_id: bgc-2673-xrefs
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json
  locator: /records/2/owner_document/xrefs
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: Literal cross-references are retained as assertions; current external authority
    content was not accessed.
  snapshot_sha256: 803cb2ee908d0d1c3a6f0a7ae1306caf8f05181e6918d0d3792452d8a2593b3d
- evidence_id: bgc-2673-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_pathway; /records/2/owner_document/biosynthesis_origin;
    /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: Retained filing, normalized BGC classes and computed classification fields;
    raw subclasses remain separately scoped.
  snapshot_sha256: 803cb2ee908d0d1c3a6f0a7ae1306caf8f05181e6918d0d3792452d8a2593b3d
- evidence_id: bgc-2673-mechanism-activity-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch268/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: This complete owner has no mechanism, pathway, molecular-target, declared-component
    or bioactivity root; no maintained reader applies.
  snapshot_sha256: 803cb2ee908d0d1c3a6f0a7ae1306caf8f05181e6918d0d3792452d8a2593b3d
  search_scope: Literal root presence in the exact current selected capture; no inference
    of biological inactivity or absence of a natural mechanism.
- evidence_id: bgc-2673-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268/intakes-001/2673-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: Actual canonical inspection preserves all 49 current input hashes and complete
    ownership declarations. Input capture is not whole-table scientific reading.
  snapshot_sha256: 395f445f26140f804ba475ee20da4c1bdac7b4b419bc1a018ee4970d7b24c593
- evidence_id: bgc-2673-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268/root-current268-intake-acceptance-001.json
  locator: /accepted; /summary
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: ROOT accepted the original canonical inspections and exact 486-input/57-path
    scope.
  snapshot_sha256: 0399aacabf22a1293ff7cce8d0290a448e3d48bede14b61d8e866e65ebe334d5
- evidence_id: bgc-2673-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-target-input-plan-001.json
  locator: /records/2; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: The accepted original input plan equals this actual intake, including exact
    companion and additional roles.
  snapshot_sha256: 9faf0a294fe39ebac4947d3d6084334630cba7ebc359a925d56710e20cd52887
- evidence_id: bgc-2673-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268/root-current268-source-plan-acceptance-001.json
  locator: /accepted; /plan
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: ROOT accepted the original composed plan; no composition was replayed.
  snapshot_sha256: f117d816201f12111b69a2f10dc47c016f207ddc800475cff5c157bd8522e8e0
- evidence_id: bgc-2673-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: Both complete saved forms and all atom, bond, ring, stereo and motif fields
    were personally read. Both canonical comparisons remain false and the attempted
    atom map is empty; normalized identifier equality does not establish full graph
    identity.
  snapshot_sha256: a5697cdbdae198619461a7b33d346032c21e31641a2dc4a16272975d4bf39a07
- evidence_id: bgc-2673-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /full_graph_identity_established; /scientific_verdict_claimed
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: ROOT accepted the original diagnostic evidence; acceptance does not establish
    natural identity or complete graph correspondence.
  snapshot_sha256: 507785873410f913dcfcfac25381e94a2a9a23808625c41693c159c241fc22d1
- evidence_id: bgc-2673-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: The original twenty-form diagnostic closed once with exit 0 and preserved
    genuine command and streams.
  snapshot_sha256: 2c538ee421c0708269a555999d17a84ae24c9d7cf8fc6b8dd295aa1b845cc2e3
- evidence_id: bgc-2673-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The complete original stderr is empty. No warning is assigned or carried
    from a prior batch.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: bgc-2673-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-current268-first-five-molecular-intake-reading-001.json
  locator: /records/2; /reading_attribution; /limitations
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: Personal whole saved-table and actual-intake reading, including exact form-specific
    topology and stereochemistry.
  snapshot_sha256: 00aecd66cc344732aeb53ade6f63011e833eee81e6e737df012f3776acd1416a
- evidence_id: bgc-2673-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268/root-native-gates-acceptance-001.json
  locator: /checks_passed; /all_native_gates_passed; /unavailable_required_gates;
    /complete_selected_queue_rows
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: Five local checks passed; full QC and OAK remain unavailable. Queue rows
    are leads, not independently confirmed scientific defects.
  snapshot_sha256: 7efe67eae2fdb56b2883e24a04d956908dcbd39d37da32b38990a23e9cfd169b
- evidence_id: bgc-2673-source-reading
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-current268-assigned-source-reading-001.json
  locator: /records/2; /full_meaning_scope; /boundaries
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: All assigned positive dictionaries and negative query boundaries for this
    owner were personally read; retained citations are not freshly read papers.
  snapshot_sha256: 5e8eeded8a676ad3cea165f1b0519a8e51c72ab647f1d36d86ea503749102e1e
- evidence_id: bgc-2673-source-notes
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: Disjoint complete source reading preserves 19 BGC and 29 Support row placements,
    with zero Native primary-row credit.
  snapshot_sha256: 93f8a31983717d9f846e3497642a7ae330d635a42dd34e05ce2a8f2cb9b4446e
- evidence_id: bgc-2673-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/native-prep/native-current268-cached-taxonomy-reading-001.json
  locator: /context_interpretations/6; /interpretation
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: partial
  summary: Owner-local retained taxonomy labels and IDs; these six cached stanzas
    have no synonym lines, and no new rank, lineage or freshness verification is inferred.
  snapshot_sha256: 5fa6d92c80787fe0db4823dd56378aff78c75750203be9b1e6f32f62ba6e47b6
- evidence_id: bgc-2673-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/native-prep/native-current268-implemented-curation-scan-001.json
  locator: /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope;
    /interpretation
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The bounded implemented-curation scan has no exact applicable predicate;
    this is not proof that all possible scientific issues are absent.
  snapshot_sha256: eeb8f1aa0d14f69e34dc675adccdf9c8919f28d9d5175cb0ef8359b65e29669b
  search_scope: Nine implemented tables and four broad unresolved Fischerella lexical
    candidates, with complete exact current predicates and fifteen retained exclusions;
    no global absence claim.
- evidence_id: bgc-2673-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/native-prep/native-current268-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: No actual AID occurs in the accepted batch. Its sole blank-AID sentinel
    belongs to selected Hangtaimycin and is not an assay or inactivity result.
  snapshot_sha256: eeb8f1aa0d14f69e34dc675adccdf9c8919f28d9d5175cb0ef8359b65e29669b
  search_scope: Actual saved inventory full-key/CID/AID scope and all fifteen retained
    exact exclusion decisions.
- evidence_id: bgc-2673-stereo-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: 'lines 392-396: stereo_complete description'
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The maintained flag concerns undefined stereocentres, not complete double-bond
    geometry.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2673-stereo-extractor
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters predicate'
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The retained extractor flag uses unassigned tetrahedral tags; no extractor
    was invoked.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2673-stereo-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'line 995: stereo_complete assignment'
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The maintained seeder copies the stored atom-centred flag; no independent
    stereochemical experiment is implied.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2673-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-target-input-plan-001.json
  locator: /records/2/proposed_companion_paths; /records/2/direct_companion_predicates
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: 5 immediate shared-BGC companion inputs are present. Shared locus context
    does not establish equivalent identity, independent experiments or transferable
    activity.
  snapshot_sha256: 9faf0a294fe39ebac4947d3d6084334630cba7ebc359a925d56710e20cd52887
- evidence_id: bgc-2673-companion-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/0
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: This exact shared-BGC context is captured as a separate owner. Selected
    first-five reading is mine; the other selected and unselected context reading
    is separately attributed to Support. No structure, activity or experimental claim
    is transferred.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
- evidence_id: bgc-2673-companion-1
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/1
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: This exact shared-BGC context is captured as a separate owner. Selected
    first-five reading is mine; the other selected and unselected context reading
    is separately attributed to Support. No structure, activity or experimental claim
    is transferred.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
- evidence_id: bgc-2673-companion-2
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/2
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: This exact shared-BGC context is captured as a separate owner. Selected
    first-five reading is mine; the other selected and unselected context reading
    is separately attributed to Support. No structure, activity or experimental claim
    is transferred.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
- evidence_id: bgc-2673-companion-3
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/4
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: This exact shared-BGC context is captured as a separate owner. Selected
    first-five reading is mine; the other selected and unselected context reading
    is separately attributed to Support. No structure, activity or experimental claim
    is transferred.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
- evidence_id: bgc-2673-companion-4
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/5
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: This exact shared-BGC context is captured as a separate owner. Selected
    first-five reading is mine; the other selected and unselected context reading
    is separately attributed to Support. No structure, activity or experimental claim
    is transferred.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
- evidence_id: bgc-2673-support-context-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/support-prep/support-current268-assigned-source-reading-002.json
  locator: /contexts; /cautions
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: Support separately read the complete last-five and four unselected query
    contexts. This evidence retains that attribution without adding primary row credit
    to this review.
  snapshot_sha256: 80f3d00eb4c30ac87e449c0891402fdcf335370bd1e0077555c86788a3967bce
- evidence_id: bgc-2673-support-companion-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/support-prep/support-current268-four-companion-whole-reading-001.json
  locator: Complete attributed raw-owner/history reading receipt
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: Support separately read the four complete unselected companion owners and
    histories; this is context, not equivalent identity or fresh experimental support.
  snapshot_sha256: 0e11556f99a1b1e9dd261f68aa5d7e0929f5650f3f1850847319a9d70cf8330b
- evidence_id: bgc-2673-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: The complete saved mibig_compounds frame contains 1 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
- evidence_id: bgc-2673-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 2735-2735; raw record sha256 83de795f0f270797556be5505bde2b72e9200c7a98c13f3676093ba95505b193
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: All 25 fields of the exact physical source record were read. This is retained
    database content, not fresh primary-paper evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2673-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The complete saved chebi_structures frame contains 0 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/hancockiamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "KBQGWSPBIGCQSN-ODUIWNOOSA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2673-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: The complete saved lotus_occurrences frame contains 1 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
- evidence_id: bgc-2673-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 3569-3569; raw record sha256 14a6ecde3d5812890f76c415c77565a7488de064c15122abf9b10086668f58f7
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: All 6 fields of the exact physical source record were read. This is retained
    database content, not fresh primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2673-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The complete saved cyanometdb_occurrences frame contains 0 positive row
    placements. All fields and exact query bounds were read; empty cells and repeated
    placements retain their original meaning.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/hancockiamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "KBQGWSPBIGCQSN-ODUIWNOOSA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2673-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: The complete saved npclassifier frame contains 1 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
- evidence_id: bgc-2673-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 1220-1220; raw record sha256 32c8f10582c4cbdea417e5fcc096530a3b2acc3f9b8da40e810f81911f73fef8
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: supports
  summary: All 7 fields of the exact physical source record were read. This is retained
    database content, not fresh primary-paper evidence.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2673-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The complete saved pubchem_bioassay frame contains 0 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/hancockiamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "KBQGWSPBIGCQSN-ODUIWNOOSA-N",
    "table": "pubchem_bioassay"}'
- evidence_id: bgc-2673-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The complete saved bindingdb_targets frame contains 0 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/hancockiamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "KBQGWSPBIGCQSN-ODUIWNOOSA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2673-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The complete saved antibioticmech_inchikeys frame contains 0 positive row
    placements. All fields and exact query bounds were read; empty cells and repeated
    placements retain their original meaning.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/hancockiamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "KBQGWSPBIGCQSN-ODUIWNOOSA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2673-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch268-tentative/bgc-prep/bgc-conditional268-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T07:12:55.365187Z'
  support: context_only
  summary: The complete saved chebi_origins frame contains 0 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 4a56188986496c4871bd6e52d9e69d41ee738d6f01252696d2057e54e4dc01a1
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/hancockiamide-f.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: bgc-2673-filing-rule
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines 295–306: choose_pathway'
  accessed_at: '2026-11-06T07:20:36.997884Z'
  support: supports
  summary: The maintained seeder files two returned pathway labels as UNCLASSIFIED
    while retaining both in np_classification. This explains the current filing without
    claiming biological pathway absence.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-268/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-268/native-current268-five-gates-execution-001.json
  accessed_at: '2026-11-06T06:42:54.517849Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 733d8f723d7dcb58f082aaa9b16c2e2bf7e9b6ff7697febb17cedcd8023a5233
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-268/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-268/native-current268-five-gates-execution-001.json
  accessed_at: '2026-11-06T06:43:19.791502Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 72ec9608630502739773e39731a04f345a648ec24a3d8ce19ee1cac8293b4616
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-268/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-268/native-current268-five-gates-execution-001.json
  accessed_at: '2026-11-06T06:43:40.399821Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-268/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-268/native-current268-five-gates-execution-001.json
  accessed_at: '2026-11-06T06:44:14.796975Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-268/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-268/native-current268-five-gates-execution-001.json
  accessed_at: '2026-11-06T06:44:26.610753Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 6f5ae7500e52d5f70a3b65c97ddeb2a618ef450144eafd1420da8c6b2189e56e
assessments:
- assessment_id: bgc-2673-identity
  area: identity
  topic: identity
  outcome: supported
  summary: Both saved forms regenerate KBQGWSPBIGCQSN-ODUIWNOOSA-N, with equal formula,
    net charge and Standard InChI. The MIBiG full key and NPA033184 assertion are
    retained. Matching normalized identifiers supports local encoded consistency but
    does not adjudicate natural identity or a particular tautomer.
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  evidence_ids:
  - bgc-2673-identity
  - bgc-2673-xrefs
  - bgc-2673-chemistry
  - bgc-2673-query-mibig_compounds
  - bgc-2673-query-chebi_structures
  - bgc-2673-query-antibioticmech_inchikeys
  - bgc-2673-direct-contexts
  - bgc-2673-row-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: KBQGWSPBIGCQSN-ODUIWNOOSA-N is regenerated from both stored forms; this
      supports encoded consistency within the retained form scope.
    definition: Exact retained full key and original regeneration scope.
    evidence_ids:
    - bgc-2673-identity
    - bgc-2673-xrefs
    - bgc-2673-chemistry
    - bgc-2673-query-mibig_compounds
    - bgc-2673-query-chebi_structures
    - bgc-2673-query-antibioticmech_inchikeys
    - bgc-2673-direct-contexts
    - bgc-2673-row-mibig_compounds-0
  - name: grounding_scope
    value: The MIBiG full key and NPA033184 assertion are retained. Matching normalized
      identifiers supports local encoded consistency but does not adjudicate natural
      identity or a particular tautomer.
    definition: Recorded grounding distinguished from natural-material identity.
    evidence_ids:
    - bgc-2673-identity
    - bgc-2673-xrefs
    - bgc-2673-chemistry
    - bgc-2673-query-mibig_compounds
    - bgc-2673-query-chebi_structures
    - bgc-2673-query-antibioticmech_inchikeys
    - bgc-2673-direct-contexts
    - bgc-2673-row-mibig_compounds-0
- assessment_id: bgc-2673-representation
  area: representation
  topic: representation
  outcome: supported
  summary: The SMILES form has three benzene rings and a fused five-membered methylenedioxy
    ring, with no nitrogen-containing ring. Its acyclic chain contains a ketone, a
    tertiary N-acetyl amide and a secondary amide. In the InChI reconstruction, the
    latter appears as C(OH)=N with a terminal hydroxyl oxygen; the ketone and N-acetyl
    amide remain. Carbonyl counts change from three to two and amide counts from two
    to one. The five-membered methylenedioxy ring shares an aromatic bond. The single
    S tetrahedral centre persists at SMILES atom 13 and InChI atom 25, and the E alkene
    remains specified. The reconstructed imidic C=N contributes one new unspecified
    double-bond entry. This representation-bound geometry does not contradict the
    source stereo_complete=true flag, whose maintained scope concerns undefined tetrahedral
    centres. Formula C31H32N2O6, neutral charge, Standard InChI and full declared
    key agree, as do atom and bond counts. Both canonical comparisons are false and
    the attempted atom map is empty. The saved mobile-hydrogen layer and the paired
    amide/imidic motif support a normalization explanation, without proving a complete
    cross-form graph match or the biologically correct tautomer.
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  evidence_ids:
  - bgc-2673-identity
  - bgc-2673-chemistry
  - bgc-2673-molecular-reading
  - bgc-2673-diagnostic-acceptance
  - bgc-2673-diagnostic-stderr
  - bgc-2673-stereo-schema
  - bgc-2673-stereo-extractor
  - bgc-2673-stereo-seeder
  dimensions:
  - name: stereochemistry_scope
    value: One specified S tetrahedral centre and one E alkene persist. One reconstructed
      C=N is unspecified; it is a representation-dependent geometric site, not an
      additional unassigned source tetrahedral centre.
    definition: Original tetrahedral specification and geometric limits, separated
      from reconstructed imines.
    evidence_ids:
    - bgc-2673-identity
    - bgc-2673-chemistry
    - bgc-2673-molecular-reading
    - bgc-2673-diagnostic-acceptance
    - bgc-2673-diagnostic-stderr
    - bgc-2673-stereo-schema
    - bgc-2673-stereo-extractor
    - bgc-2673-stereo-seeder
  - name: representation_correspondence
    value: The secondary amide becomes C(OH)=N with a terminal hydroxyl oxygen, while
      the N-acetyl amide and ketone remain. Both canonical comparisons stay false
      and the map stays empty despite equal formula, neutral charge, Standard InChI
      and full key.
    definition: Canonical comparisons and attempted atom map, distinct from normalized
      identity.
    evidence_ids:
    - bgc-2673-identity
    - bgc-2673-chemistry
    - bgc-2673-molecular-reading
    - bgc-2673-diagnostic-acceptance
    - bgc-2673-diagnostic-stderr
    - bgc-2673-stereo-schema
    - bgc-2673-stereo-extractor
    - bgc-2673-stereo-seeder
- assessment_id: bgc-2673-provenance
  area: provenance
  topic: provenance
  outcome: supported
  summary: Hancockiamide F retains Aspergillus hancockii (NCBITaxon:1873369) with
    SOURCE_ASSERTION producer support and the BGC0002264 locus MBFL02000005.1:62010–93497
    with CLUSTER_DEMONSTRATED support. Heterologous expression and enzymatic assays
    are retained source method labels, not newly verified experiments in this review.
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  evidence_ids:
  - bgc-2673-provenance
  - bgc-2673-query-mibig_compounds
  - bgc-2673-taxonomy
  - bgc-2673-curation
  - bgc-2673-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    value: Hancockiamide F retains Aspergillus hancockii (NCBITaxon:1873369) with
      SOURCE_ASSERTION producer support and the BGC0002264 locus MBFL02000005.1:62010–93497
      with CLUSTER_DEMONSTRATED support. Cached labels/IDs are retained; rank, lineage,
      freshness and strain validity were not freshly verified.
    definition: Source labels, identifiers and cached taxonomy without new rank or
      lineage verification.
    evidence_ids:
    - bgc-2673-provenance
    - bgc-2673-query-mibig_compounds
    - bgc-2673-taxonomy
    - bgc-2673-curation
    - bgc-2673-row-mibig_compounds-0
  - name: producer_evidence
    value: Hancockiamide F retains Aspergillus hancockii (NCBITaxon:1873369) with
      SOURCE_ASSERTION producer support and the BGC0002264 locus MBFL02000005.1:62010–93497
      with CLUSTER_DEMONSTRATED support. Heterologous expression and enzymatic assays
      are retained source method labels, not newly verified experiments in this review.
    definition: Literal producer assertion grade.
    evidence_ids:
    - bgc-2673-provenance
    - bgc-2673-query-mibig_compounds
    - bgc-2673-taxonomy
    - bgc-2673-curation
    - bgc-2673-row-mibig_compounds-0
  - name: locus_evidence
    value: Hancockiamide F retains Aspergillus hancockii (NCBITaxon:1873369) with
      SOURCE_ASSERTION producer support and the BGC0002264 locus MBFL02000005.1:62010–93497
      with CLUSTER_DEMONSTRATED support. Heterologous expression and enzymatic assays
      are retained source method labels, not newly verified experiments in this review.
      Shared-BGC companion records do not add independent experimental support.
    definition: Literal locus-to-compound grade and source method.
    evidence_ids:
    - bgc-2673-provenance
    - bgc-2673-query-mibig_compounds
    - bgc-2673-taxonomy
    - bgc-2673-curation
    - bgc-2673-row-mibig_compounds-0
- assessment_id: bgc-2673-citations
  area: evidence
  topic: citations
  outcome: supported
  summary: F is compound index 6 in the questionable, unknown-completeness BGC0002264
    version 3 entry. PMID:33242032 is entry-level, and the LOTUS occurrence cites
    DOI:10.1039/D0OB02243H. Neither is treated as a freshly inspected compound-specific
    mechanism paper.
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  evidence_ids:
  - bgc-2673-provenance
  - bgc-2673-occurrence-owner
  - bgc-2673-query-mibig_compounds
  - bgc-2673-query-lotus_occurrences
  - bgc-2673-query-cyanometdb_occurrences
  - bgc-2673-source-reading
  - bgc-2673-row-mibig_compounds-0
  - bgc-2673-row-lotus_occurrences-0
  dimensions:
  - name: citation_scope
    value: F is compound index 6 in the questionable, unknown-completeness BGC0002264
      version 3 entry. PMID:33242032 is entry-level, and the LOTUS occurrence cites
      DOI:10.1039/D0OB02243H. Neither is treated as a freshly inspected compound-specific
      mechanism paper.
    definition: Reference grain and independence limits.
    evidence_ids:
    - bgc-2673-provenance
    - bgc-2673-occurrence-owner
    - bgc-2673-query-mibig_compounds
    - bgc-2673-query-lotus_occurrences
    - bgc-2673-query-cyanometdb_occurrences
    - bgc-2673-source-reading
    - bgc-2673-row-mibig_compounds-0
    - bgc-2673-row-lotus_occurrences-0
- assessment_id: bgc-2673-occurrence_activity
  area: evidence
  topic: occurrence_activity
  outcome: supported
  summary: The single LOTUS occurrence names Aspergillus hancockii. It does not establish
    strain-specific production or a molecular target. No actual AID or BindingDB target
    match is present in the saved exact-query frames; owner-root absence is not a
    claim of inactivity.
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  evidence_ids:
  - bgc-2673-occurrence-owner
  - bgc-2673-mechanism-activity-scope
  - bgc-2673-query-lotus_occurrences
  - bgc-2673-query-cyanometdb_occurrences
  - bgc-2673-query-pubchem_bioassay
  - bgc-2673-query-bindingdb_targets
  - bgc-2673-assay-curation
  - bgc-2673-chemistry
  - bgc-2673-row-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    value: The single LOTUS occurrence names Aspergillus hancockii. It does not establish
      strain-specific production or a molecular target. No actual AID or BindingDB
      target match is present in the saved exact-query frames; owner-root absence
      is not a claim of inactivity.
    definition: Occurrence evidence separated from strain production.
    evidence_ids:
    - bgc-2673-occurrence-owner
    - bgc-2673-mechanism-activity-scope
    - bgc-2673-query-lotus_occurrences
    - bgc-2673-query-cyanometdb_occurrences
    - bgc-2673-query-pubchem_bioassay
    - bgc-2673-query-bindingdb_targets
    - bgc-2673-assay-curation
    - bgc-2673-chemistry
    - bgc-2673-row-lotus_occurrences-0
  - name: assay_target_scope
    value: No actual AID or BindingDB target row is present in the exact retained
      scope. Owner-root absence and negative saved queries do not establish inactivity
      or absence of biological targets.
    definition: Retained assay scope and molecular-target limits.
    evidence_ids:
    - bgc-2673-occurrence-owner
    - bgc-2673-mechanism-activity-scope
    - bgc-2673-query-lotus_occurrences
    - bgc-2673-query-cyanometdb_occurrences
    - bgc-2673-query-pubchem_bioassay
    - bgc-2673-query-bindingdb_targets
    - bgc-2673-assay-curation
    - bgc-2673-chemistry
    - bgc-2673-row-lotus_occurrences-0
- assessment_id: bgc-2673-classification
  area: consistency
  topic: classification
  outcome: supported
  summary: 'The acyclic amide-containing chain and aromatic substitution are compatible
    with the broad retained Amino acids and Peptides and Shikimates and Phenylpropanoids
    outputs. Its topology differs from A’s and E’s piperazine framework. Empty family
    fields remain literal and the model labels do not assign a biosynthetic step.
    The current np_pathway=UNCLASSIFIED follows the maintained filing rule for two
    returned pathway labels: both predictions are retained in np_classification. This
    is consistent filing and does not imply missing classifications or biological
    pathway absence.'
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  evidence_ids:
  - bgc-2673-classification-owner
  - bgc-2673-chemistry
  - bgc-2673-query-npclassifier
  - bgc-2673-query-mibig_compounds
  - bgc-2673-row-npclassifier-0
  - bgc-2673-row-mibig_compounds-0
  - bgc-2673-filing-rule
  dimensions:
  - name: classification_applicability
    value: 'The acyclic amide-containing chain and aromatic substitution are compatible
      with the broad retained Amino acids and Peptides and Shikimates and Phenylpropanoids
      outputs. Its topology differs from A’s and E’s piperazine framework. Empty family
      fields remain literal and the model labels do not assign a biosynthetic step.
      The current np_pathway=UNCLASSIFIED follows the maintained filing rule for two
      returned pathway labels: both predictions are retained in np_classification.
      This is consistent filing and does not imply missing classifications or biological
      pathway absence.'
    definition: Encoded topology separated from exact model-family or biosynthetic
      proof.
    evidence_ids:
    - bgc-2673-classification-owner
    - bgc-2673-chemistry
    - bgc-2673-query-npclassifier
    - bgc-2673-query-mibig_compounds
    - bgc-2673-row-npclassifier-0
    - bgc-2673-row-mibig_compounds-0
    - bgc-2673-filing-rule
- assessment_id: bgc-2673-completion
  area: completeness
  topic: completion
  outcome: supported
  summary: The complete owner and history, all nine saved query frames and both complete
    saved molecular forms were read; 49 actual input hashes and ownership declarations
    were verified. The review preserves the accepted local diagnostic and five native
    checks, while full QC, OAK, primary-publication access and live authority verification
    remain unavailable. There is no declared mechanism, component or pathway requiring
    a maintained reader.
  target_ids:
  - naturalproductmech:mibig-feede3fe88
  evidence_ids:
  - bgc-2673-owner
  - bgc-2673-history
  - bgc-2673-intake
  - bgc-2673-intake-acceptance
  - bgc-2673-plan
  - bgc-2673-plan-acceptance
  - bgc-2673-gates
  - bgc-2673-source-reading
  - bgc-2673-source-notes
  - bgc-2673-molecular-reading
  - bgc-2673-mechanism-activity-scope
  dimensions:
  - name: review_completion
    value: The complete owner and history, all nine saved query frames and both complete
      saved molecular forms were read; 49 actual input hashes and ownership declarations
      were verified. The review preserves the accepted local diagnostic and five native
      checks, while full QC, OAK, primary-publication access and live authority verification
      remain unavailable. There is no declared mechanism, component or pathway requiring
      a maintained reader.
    definition: Actual local evidence coverage and unavailable verification.
    evidence_ids:
    - bgc-2673-owner
    - bgc-2673-history
    - bgc-2673-intake
    - bgc-2673-intake-acceptance
    - bgc-2673-plan
    - bgc-2673-plan-acceptance
    - bgc-2673-gates
    - bgc-2673-source-reading
    - bgc-2673-source-notes
    - bgc-2673-molecular-reading
    - bgc-2673-mechanism-activity-scope
findings: []
actions: []
limitations:
- Local stored-form consistency does not independently establish natural identity,
  biological activity or primary experimental mechanism.
- Source producer, locus and citation grades remain at their recorded granularity;
  no source independence or strain experiment is inferred.
- Full QC and OAK checks, live authorities and primary-paper verification remain unavailable
  under the outbound hold.
- Both canonical comparisons and the attempted atom map remain unresolved for Hancockiamide
  F; its observed secondary-amide/imidic change is explicitly scoped.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Five shared-BGC companions are contextual inputs. F’s full key, C31H32N2O6 formula
  and NPA033184 identifier remain distinct; a common source entry does not supply
  an unrecorded conversion from another Hancockiamide.
- Original diagnostic stderr is empty. No previous-batch warning, finding or scientific
  verdict is carried.
- Companion whole-owner and query reading is separately attributed to Support where
  outside the selected first-five scope; no companion activity or stereochemistry
  is transferred.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-268
```
