# Local evidence review: Fulvuthiacene A

- Review: 20261106T055627Z-fulvuthiacene-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T05:23:02.213249Z
- Finished UTC: 2026-11-06T05:56:27.711983Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Fulvuthiacene A has matching stored molecular representations and preserves its distinct thiazole-containing chain, full identifier and source provenance. Shared-BGC comparison with B retains the chain-length distinction without transferring biological claims. These encoded-consistency positives support a qualified partial pass.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2661; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-02f0c67532 | data/natural_products/unclassified/fulvuthiacene-a.yaml | generated | Fulvuthiacene A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-02f0c67532 | The accepted original diagnostic parsed both stored forms and retained every comparison flag. Formula, net charge, Standard InChI and full key agree within this owner. |
| strict_ten | passed | True | naturalproductmech:mibig-02f0c67532 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-02f0c67532 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-02f0c67532 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-02f0c67532 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-02f0c67532 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-02f0c67532 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-02f0c67532 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-02f0c67532 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### identity

identity: supported. Targets: naturalproductmech:mibig-02f0c67532.

Fulvuthiacene A preserves BGC0001941 compound 1, formula C24H39NO4S and full key XFAGIUVJPOMBNU-YLHPCDMOSA-N. The exact MIBiG row and both original diagnostic forms agree. The separately captured B owner has a distinct full key and chain length; shared BGC membership does not establish equivalent identity. NPA025855 is a retained xref, not freshly resolved authority.

### representation

representation: supported. Targets: naturalproductmech:mibig-02f0c67532.

Fulvuthiacene A is encoded as a neutral, acyclic substituted chain attached to one aromatic five-membered N/S thiazole ring. Both forms have one methyl ester and two additional methoxy bridges, with no amide motif or sugar-ring candidate. The two original tetrahedra have R/S assignments and both alkene geometries are specified E/Z. Both canonical strings agree and the 30-index one-way match is complete, while full_graph_identity_established remains false. Relative to the separately retained B owner, the written alkyl branch has two additional methylene units and the formula differs by C2H4; neither record is merged or used as independent biological evidence for the other.

### provenance

provenance: unknown. Targets: naturalproductmech:mibig-02f0c67532.

Active BGC0001941 version 3 retains questionable entry quality and unknown completeness. Myxococcus fulvus, NCBITaxon:33, is SOURCE_ASSERTION; MH069655.1 is separately CLUSTER_UNSTATED without retained bounds or methods. The shared source entry does not upgrade either compound to demonstrated production or assign pathway steps.

### citations

evidence: unknown. Targets: naturalproductmech:mibig-02f0c67532.

DOI:10.1021/acschembio.8b00948 is retained at COMPOUND_EVIDENCE grain in MIBiG. LOTUS retains the same DOI with uppercase spelling. These are database representations of a reference, not two independent publications or a fresh primary-paper reading.

### occurrence_activity

evidence: unknown. Targets: naturalproductmech:mibig-02f0c67532.

One exact-key LOTUS row reports Myxococcus fulvus, NCBITaxon:33. It is an occurrence assertion distinct from demonstrated production. All saved assay and target query scopes are empty, with no AID sentinel or owner activity root; no potency, enzyme activity or molecular target is inferred.

### classification

consistency: unknown. Targets: naturalproductmech:mibig-02f0c67532.

The encoded thiazole-bearing unsaturated chain and methyl ester are consistent with a broad polyketide-like structural description; no amide backbone or sugar-ring candidate is present. The source class PKS and subclass Type I remain distinct. NPClassifier reports Amino acids and Peptides, Polyketides, Linear polyketides, and Melithiazole and Myxothiazole derivatives with is_glycoside false. The exact named family and amino-acid biosynthetic contribution remain model-level assertions, not independently established mechanisms.

### completion

completeness: unknown. Targets: naturalproductmech:mibig-02f0c67532.

The complete current owner and history, all nine saved query frames and both complete saved molecular forms were read; 45 actual input hashes and ownership declarations were verified. This is part of the accepted 443-input/54-path batch. Five local gates passed; full QC, complete OAK authority and fresh source verification remain unavailable. No selected maintained reader applies, and completion remains partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2661-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/fulvuthiacene-a.yaml; Complete plaintext and curation_history | supports | The complete current owner and every history entry were personally read; historical assertions do not confer fresh authority access. |
| bgc-2661-identity | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/label; /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status | supports | Exact current identity, structure encodings, source concepts and grounding; natural identity remains separate. |
| bgc-2661-history | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/0/owner_document/curation_history | supports | All 3 retained history entries preserve their original scope; no primary-publication access is inherited. |
| bgc-2661-provenance | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts | supports | Producer and locus assertions retain separate evidence grades, genomic scope and reference grain. |
| bgc-2661-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/0/owner_document/occurrences | supports | Current owner occurrence assertions are retained at their recorded granularity; occurrence does not establish production, activity or molecular mechanism. |
| bgc-2661-xrefs | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/0/owner_document/xrefs | supports | Literal cross-references are retained as assertions; current external authority content was not accessed. |
| bgc-2661-classification-owner | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/0/owner_document/np_pathway; /records/0/owner_document/biosynthesis_origin; /records/0/owner_document/np_classification; /records/0/owner_document/bgc_class | supports | Retained filing, normalized BGC classes and computed classification fields; raw subclasses remain separately scoped. |
| bgc-2661-mechanism-activity-scope | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/0/owner_document | context_only | This complete owner has no mechanism, pathway, molecular-target, declared-component or bioactivity root; no maintained reader applies. |
| bgc-2661-intake | /private/tmp/npm-review-work/shared-next-batch267/intakes-001/2661-inspect-001.json; /source; /targets | supports | Actual canonical inspection preserves all 45 current input hashes and complete ownership declarations. Input capture is not whole-table scientific reading. |
| bgc-2661-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch267/root-current267-intake-acceptance-001.json; /accepted; /summary | supports | ROOT accepted the original canonical inspections and exact 443-input/54-path scope. |
| bgc-2661-plan | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-target-input-plan-001.json; /records/0; /source_placement_count; /unique_source_path_count | supports | The accepted original input plan equals this actual intake, including exact companion and additional roles. |
| bgc-2661-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch267/root-current267-source-plan-acceptance-001.json; /accepted; /plan | supports | ROOT accepted the original composed plan; no composition was replayed. |
| bgc-2661-chemistry | /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnostic-DATA-001.json; /records/0 | supports | Both complete saved forms and all atom, bond, ring, stereo and motif fields were personally read. Both canonical comparisons agree and the one-way atom match covers the recorded atom count; full graph identity remains false. |
| bgc-2661-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/root-diagnostic-result-acceptance-001.json; /accepted; /DATA; /execution; /interpretation_limits | supports | ROOT accepted the original diagnostic evidence; acceptance does not establish natural identity or complete graph correspondence. |
| bgc-2661-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr | supports | The original twenty-form diagnostic closed once with exit 0 and preserved genuine command and streams. |
| bgc-2661-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnostic-original-001.stderr; Complete original stderr | context_only | Two undefined-stereo and two charge-rearrangement warning blocks remain global and unassigned to individual forms. |
| bgc-2661-molecular-reading | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-current267-first-five-molecular-intake-reading-001.json; /records/0; /reading_attribution; /limitations | supports | Personal whole saved-table and actual-intake reading, including exact form-specific topology and stereochemistry. |
| bgc-2661-gates | /private/tmp/npm-review-work/shared-next-batch267/root-native-gates-acceptance-001.json; /checks_passed; /all_native_gates_passed; /unavailable_required_gates; /complete_selected_queue_rows | supports | Five local checks passed; full QC and OAK remain unavailable. Queue rows are leads, not independently confirmed scientific defects. |
| bgc-2661-source-reading | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-current267-assigned-source-reading-001.json; /records/0; /full_meaning_scope; /boundaries | supports | All assigned positive dictionaries and negative query boundaries for this owner were personally read; retained citations are not freshly read papers. |
| bgc-2661-source-notes | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /reading_boundaries | supports | Disjoint complete source reading preserves 17 BGC and 22 Support row placements, with zero Native primary-row credit. |
| bgc-2661-taxonomy | /private/tmp/npm-review-work/shared-next-batch267-tentative/native-prep/native-current267-cached-taxonomy-reading-001.json; /context_interpretations/1; /interpretation | partial | Owner-local retained taxonomy labels, IDs and cached synonyms; no new rank, lineage or freshness verification. |
| bgc-2661-curation | /private/tmp/npm-review-work/shared-next-batch267-tentative/native-prep/native-current267-implemented-curation-scan-001.json; /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope; /interpretation | context_only | The bounded implemented-curation scan has no exact applicable predicate; this is not proof that all possible scientific issues are absent. |
| bgc-2661-assay-curation | /private/tmp/npm-review-work/shared-next-batch267-tentative/native-prep/native-current267-implemented-curation-scan-001.json; /assay_scope | context_only | No actual AID occurs in the accepted batch. Two blank sentinels concern other selected/companion contexts; none belongs to the first five. |
| bgc-2661-stereo-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392-396: stereo_complete description | context_only | The maintained flag concerns undefined stereocentres, not complete double-bond geometry. |
| bgc-2661-stereo-extractor | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters predicate | context_only | The retained extractor flag uses unassigned tetrahedral tags; no extractor was invoked. |
| bgc-2661-stereo-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; line 995: stereo_complete assignment | context_only | The maintained seeder copies the stored atom-centred flag; no independent stereochemical experiment is implied. |
| bgc-2661-direct-contexts | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-target-input-plan-001.json; /records/0/proposed_companion_paths; /records/0/direct_companion_predicates | context_only | 1 immediate shared-BGC companion inputs are present. Shared locus context does not establish equivalent identity, independent experiments or transferable activity. |
| bgc-2661-companion-0 | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/2 | context_only | The current counterpart owner and complete saved query scope were personally read within the first-five partition; distinct keys and chain lengths remain separate. |
| bgc-2661-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/mibig_compounds | supports | The complete saved mibig_compounds frame contains 1 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2661-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 2253-2253; raw record sha256 eb9e026f747c2156ee777b6586aee7e484d074d0ff9af8ae03ab5c81ffd378a0 | supports | All 25 fields of the exact physical source record were read. This is retained database content, not fresh primary-paper evidence. |
| bgc-2661-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/chebi_structures | context_only | The complete saved chebi_structures frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2661-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/lotus_occurrences | supports | The complete saved lotus_occurrences frame contains 1 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2661-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 9541-9541; raw record sha256 8142b44a3b6b71363d8c55781ac4949b909f014b64ca81a0a93b0c78bb78b6b5 | supports | All 6 fields of the exact physical source record were read. This is retained database content, not fresh primary-paper evidence. |
| bgc-2661-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/cyanometdb_occurrences | context_only | The complete saved cyanometdb_occurrences frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2661-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/npclassifier | supports | The complete saved npclassifier frame contains 1 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2661-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2760-2760; raw record sha256 2e70c3cfd7c125409fd9ad773b5b3fdb47b26497fceb67c5d53ebf3d8d5efe1d | supports | All 7 fields of the exact physical source record were read. This is retained database content, not fresh primary-paper evidence. |
| bgc-2661-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/pubchem_bioassay | context_only | The complete saved pubchem_bioassay frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2661-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/bindingdb_targets | context_only | The complete saved bindingdb_targets frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2661-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | The complete saved antibioticmech_inchikeys frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| bgc-2661-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/chebi_origins | context_only | The complete saved chebi_origins frame contains 0 positive row placements. All fields and exact query bounds were read; empty cells and repeated placements retain their original meaning. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-267/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-267/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-267/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-267/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-267/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Fresh database, primary-literature and complete ontology authority verification were unavailable under the no-request instruction. Retained source assertions and historical references are distinguished from freshly verified experiments.
- Both stored forms were inspected from the accepted original diagnostic only. Normalized identifiers, local motifs and a one-way atom match do not independently establish natural identity or complete graph identity; all false flags are retained.
- The four original warning blocks—two undefined-stereo and two charge-rearrangement warnings—are global and cannot be assigned to a particular owner or form from this stream.
- No mechanism, pathway, molecular target or component root occurs in these selected owners. No maintained reader applies. Full QC and complete OAK coverage remain unavailable, so scientific completion is partial.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- The differently reported local Cis/Trans descriptors depend on stereo-atom conventions; the saved bond E/Z labels and canonical strings agree across forms.
- The A/B formula difference is C2H4 and the written alkyl branches differ by two methylene units; no enzymatic conversion is inferred.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T055627Z-fulvuthiacene-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: Fulvuthiacene A'
started_at: '2026-11-06T05:23:02.213249Z'
finished_at: '2026-11-06T05:56:27.711983Z'
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
summary: Fulvuthiacene A has matching stored molecular representations and preserves
  its distinct thiazole-containing chain, full identifier and source provenance. Shared-BGC
  comparison with B retains the chain-length distinction without transferring biological
  claims. These encoded-consistency positives support a qualified partial pass.
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
  - path: data/natural_products/unclassified/fulvuthiacene-a.yaml
    sha256: acdb5c9648978a03db730fe1598b1ae9a48067304156909f58abfca0ad213073
    role: target
  - path: data/natural_products/unclassified/fulvuthiacene-b.yaml
    sha256: 164155d01b28009a1f369e9fd29c8bc8d709fd46812099e48aec58e221d467c6
    role: context
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
  selection: Campaign path order 2661; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-02f0c67532
targets:
- target_id: naturalproductmech:mibig-02f0c67532
  path: data/natural_products/unclassified/fulvuthiacene-a.yaml
  label: Fulvuthiacene A
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnose267-001.py
    0edaba57176b70b985dfb78386d05d3813763a646b2c417a8306268773fface5 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
    8ba52bcc99d104c0fc5cb751807bdf52de9433ae9ffff9f012d4151e1dbc2731
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The accepted original diagnostic parsed both stored forms and retained
    every comparison flag. Formula, net charge, Standard InChI and full key agree
    within this owner.
  scope_note: Shared original twenty-form execution, without rerun. Both canonical
    comparisons agree and the one-way atom match covers the recorded atom count; full
    graph identity remains false. No natural-identity, complete stereochemical or
    biological-function certification follows.
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  evidence_ids:
  - bgc-2661-chemistry
  - bgc-2661-diagnostic-acceptance
  - bgc-2661-diagnostic-execution
  - bgc-2661-diagnostic-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  command: just validate-strict data/natural_products/unclassified/fulvuthiacene-a.yaml
    data/natural_products/unclassified/fulvuthiacene-b.yaml data/natural_products/unclassified/fusaricidin-b.yaml
    data/natural_products/unclassified/fusaristatin-a.yaml data/natural_products/unclassified/gacamide-a.yaml
    data/natural_products/unclassified/gibepyrone-d.yaml data/natural_products/unclassified/gliovirin.yaml
    data/natural_products/unclassified/gramibactin.yaml data/natural_products/unclassified/griselimycin.yaml
    data/natural_products/unclassified/grisemycin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-267/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-02f0c67532
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-267/validate-all-001.tsv
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
  - naturalproductmech:mibig-02f0c67532
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
  - naturalproductmech:mibig-02f0c67532
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
  - naturalproductmech:mibig-02f0c67532
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-267/review-queue-001.tsv
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
  - naturalproductmech:mibig-02f0c67532
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2661-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/fulvuthiacene-a.yaml
  locator: Complete plaintext and curation_history
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: The complete current owner and every history entry were personally read;
    historical assertions do not confer fresh authority access.
  snapshot_sha256: acdb5c9648978a03db730fe1598b1ae9a48067304156909f58abfca0ad213073
- evidence_id: bgc-2661-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/label;
    /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts;
    /records/0/owner_document/grounding_status
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: Exact current identity, structure encodings, source concepts and grounding;
    natural identity remains separate.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: bgc-2661-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/0/owner_document/curation_history
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: All 3 retained history entries preserve their original scope; no primary-publication
    access is inherited.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: bgc-2661-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters;
    /records/0/owner_document/source_concepts
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: Producer and locus assertions retain separate evidence grades, genomic
    scope and reference grain.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: bgc-2661-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/0/owner_document/occurrences
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: Current owner occurrence assertions are retained at their recorded granularity;
    occurrence does not establish production, activity or molecular mechanism.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: bgc-2661-xrefs
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/0/owner_document/xrefs
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: Literal cross-references are retained as assertions; current external authority
    content was not accessed.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: bgc-2661-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_pathway; /records/0/owner_document/biosynthesis_origin;
    /records/0/owner_document/np_classification; /records/0/owner_document/bgc_class
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: Retained filing, normalized BGC classes and computed classification fields;
    raw subclasses remain separately scoped.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: bgc-2661-mechanism-activity-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: This complete owner has no mechanism, pathway, molecular-target, declared-component
    or bioactivity root; no maintained reader applies.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
  search_scope: Literal root presence in the exact current selected capture; no inference
    of biological inactivity or absence of a natural mechanism.
- evidence_id: bgc-2661-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/intakes-001/2661-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: Actual canonical inspection preserves all 45 current input hashes and complete
    ownership declarations. Input capture is not whole-table scientific reading.
  snapshot_sha256: e4b8d80acc79f45819bfc6574690da017facf3f6c75a729a204f777f89afa6d7
- evidence_id: bgc-2661-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/root-current267-intake-acceptance-001.json
  locator: /accepted; /summary
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: ROOT accepted the original canonical inspections and exact 443-input/54-path
    scope.
  snapshot_sha256: f292e156d50caea7274697f897681baab83bb25c772d8ff8ed2751c192d74a57
- evidence_id: bgc-2661-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-target-input-plan-001.json
  locator: /records/0; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: The accepted original input plan equals this actual intake, including exact
    companion and additional roles.
  snapshot_sha256: 9d3bb7ebc200cc291d785e33eb1bf51e4bb76ecabcdc943153205fbe56b06657
- evidence_id: bgc-2661-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/root-current267-source-plan-acceptance-001.json
  locator: /accepted; /plan
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: ROOT accepted the original composed plan; no composition was replayed.
  snapshot_sha256: 97d98ee1ecfc06f90fbdfc8ad2ccf2a38ab78ae423410b6a824cb928d13b8051
- evidence_id: bgc-2661-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: Both complete saved forms and all atom, bond, ring, stereo and motif fields
    were personally read. Both canonical comparisons agree and the one-way atom match
    covers the recorded atom count; full graph identity remains false.
  snapshot_sha256: 3fea1ec0393d289bfbf7e75bf538d367fac7471c79f90564952de3e0be7e91a0
- evidence_id: bgc-2661-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/root-diagnostic-result-acceptance-001.json
  locator: /accepted; /DATA; /execution; /interpretation_limits
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: ROOT accepted the original diagnostic evidence; acceptance does not establish
    natural identity or complete graph correspondence.
  snapshot_sha256: 34342ef403d82e4a6112037a844fcb9f574eb6999e86108bc77aeb685840dec7
- evidence_id: bgc-2661-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: The original twenty-form diagnostic closed once with exit 0 and preserved
    genuine command and streams.
  snapshot_sha256: 557939b2cbb7aa99e65a38f092c1b57fce96fb3393b36cd94f5a2c5e6b2868fd
- evidence_id: bgc-2661-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: Two undefined-stereo and two charge-rearrangement warning blocks remain
    global and unassigned to individual forms.
  snapshot_sha256: 6e778c0f8dd0614b8f98c2997b5d08e9c8260f4239834ee31d6e7000c6fd45eb
- evidence_id: bgc-2661-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-current267-first-five-molecular-intake-reading-001.json
  locator: /records/0; /reading_attribution; /limitations
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: Personal whole saved-table and actual-intake reading, including exact form-specific
    topology and stereochemistry.
  snapshot_sha256: 2fc3159fad67cf6a7a396a4b4cad191cbdd3d6ee5a4a4119e646d264c6c5b825
- evidence_id: bgc-2661-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/root-native-gates-acceptance-001.json
  locator: /checks_passed; /all_native_gates_passed; /unavailable_required_gates;
    /complete_selected_queue_rows
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: Five local checks passed; full QC and OAK remain unavailable. Queue rows
    are leads, not independently confirmed scientific defects.
  snapshot_sha256: 50ea7d1b4e1955899f97f52176bdfe71e00713ebc89293aac111dfed02c9b225
- evidence_id: bgc-2661-source-reading
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-current267-assigned-source-reading-001.json
  locator: /records/0; /full_meaning_scope; /boundaries
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: All assigned positive dictionaries and negative query boundaries for this
    owner were personally read; retained citations are not freshly read papers.
  snapshot_sha256: a87f5ce2cf5c55efb4d6de21dead70fcf4bb7c81322405fbd320ec18df17b190
- evidence_id: bgc-2661-source-notes
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: Disjoint complete source reading preserves 17 BGC and 22 Support row placements,
    with zero Native primary-row credit.
  snapshot_sha256: d73c4fcacc581e4eda06b1e52854b82f6f38530ef14d61d1ba65b093aa03524e
- evidence_id: bgc-2661-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/native-prep/native-current267-cached-taxonomy-reading-001.json
  locator: /context_interpretations/1; /interpretation
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: partial
  summary: Owner-local retained taxonomy labels, IDs and cached synonyms; no new rank,
    lineage or freshness verification.
  snapshot_sha256: 8606d838c23979d0f94dbba0440d4852810e7a52d3a6f283bd22e1a94f13c527
- evidence_id: bgc-2661-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/native-prep/native-current267-implemented-curation-scan-001.json
  locator: /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope;
    /interpretation
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The bounded implemented-curation scan has no exact applicable predicate;
    this is not proof that all possible scientific issues are absent.
  snapshot_sha256: fca61cd560e376fadcad5ce2eba4e186a81afdafdc94f8d06548ab975ce6b7c6
  search_scope: Nine implemented tables and three broad lexical candidates, with complete
    exact current predicates and fifteen retained exclusions; no global absence claim.
- evidence_id: bgc-2661-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/native-prep/native-current267-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: No actual AID occurs in the accepted batch. Two blank sentinels concern
    other selected/companion contexts; none belongs to the first five.
  snapshot_sha256: fca61cd560e376fadcad5ce2eba4e186a81afdafdc94f8d06548ab975ce6b7c6
  search_scope: Actual saved inventory full-key/CID/AID scope and all fifteen retained
    exact exclusion decisions.
- evidence_id: bgc-2661-stereo-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: 'lines 392-396: stereo_complete description'
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The maintained flag concerns undefined stereocentres, not complete double-bond
    geometry.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2661-stereo-extractor
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters predicate'
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The retained extractor flag uses unassigned tetrahedral tags; no extractor
    was invoked.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2661-stereo-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'line 995: stereo_complete assignment'
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The maintained seeder copies the stored atom-centred flag; no independent
    stereochemical experiment is implied.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2661-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-target-input-plan-001.json
  locator: /records/0/proposed_companion_paths; /records/0/direct_companion_predicates
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: 1 immediate shared-BGC companion inputs are present. Shared locus context
    does not establish equivalent identity, independent experiments or transferable
    activity.
  snapshot_sha256: 9d3bb7ebc200cc291d785e33eb1bf51e4bb76ecabcdc943153205fbe56b06657
- evidence_id: bgc-2661-companion-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/2
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The current counterpart owner and complete saved query scope were personally
    read within the first-five partition; distinct keys and chain lengths remain separate.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
- evidence_id: bgc-2661-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: The complete saved mibig_compounds frame contains 1 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
- evidence_id: bgc-2661-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 2253-2253; raw record sha256 eb9e026f747c2156ee777b6586aee7e484d074d0ff9af8ae03ab5c81ffd378a0
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: All 25 fields of the exact physical source record were read. This is retained
    database content, not fresh primary-paper evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2661-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The complete saved chebi_structures frame contains 0 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/fulvuthiacene-a.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "XFAGIUVJPOMBNU-YLHPCDMOSA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2661-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: The complete saved lotus_occurrences frame contains 1 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
- evidence_id: bgc-2661-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 9541-9541; raw record sha256 8142b44a3b6b71363d8c55781ac4949b909f014b64ca81a0a93b0c78bb78b6b5
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: All 6 fields of the exact physical source record were read. This is retained
    database content, not fresh primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2661-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The complete saved cyanometdb_occurrences frame contains 0 positive row
    placements. All fields and exact query bounds were read; empty cells and repeated
    placements retain their original meaning.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/fulvuthiacene-a.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "XFAGIUVJPOMBNU-YLHPCDMOSA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2661-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: The complete saved npclassifier frame contains 1 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
- evidence_id: bgc-2661-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2760-2760; raw record sha256 2e70c3cfd7c125409fd9ad773b5b3fdb47b26497fceb67c5d53ebf3d8d5efe1d
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: supports
  summary: All 7 fields of the exact physical source record were read. This is retained
    database content, not fresh primary-paper evidence.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2661-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The complete saved pubchem_bioassay frame contains 0 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/fulvuthiacene-a.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "XFAGIUVJPOMBNU-YLHPCDMOSA-N",
    "table": "pubchem_bioassay"}'
- evidence_id: bgc-2661-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The complete saved bindingdb_targets frame contains 0 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/fulvuthiacene-a.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "XFAGIUVJPOMBNU-YLHPCDMOSA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2661-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The complete saved antibioticmech_inchikeys frame contains 0 positive row
    placements. All fields and exact query bounds were read; empty cells and repeated
    placements retain their original meaning.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/fulvuthiacene-a.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "XFAGIUVJPOMBNU-YLHPCDMOSA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2661-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T05:54:36.902765Z'
  support: context_only
  summary: The complete saved chebi_origins frame contains 0 positive row placements.
    All fields and exact query bounds were read; empty cells and repeated placements
    retain their original meaning.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/fulvuthiacene-a.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-267/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json
  accessed_at: '2026-11-06T05:29:44.430051Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: e8a8ccd61409d224cc4e2ca0b760e5990a95fd97fa1e31c77a90caf62da00270
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-267/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json
  accessed_at: '2026-11-06T05:30:08.494903Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: fec95e98129e97314acfed6406b99b941fe0504915d7421354d149107d563720
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-267/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json
  accessed_at: '2026-11-06T05:30:27.738268Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-267/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json
  accessed_at: '2026-11-06T05:31:01.614008Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-267/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json
  accessed_at: '2026-11-06T05:31:13.231506Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 0f1b40f1483b7fbcd9547da82a4b53dc71d40cbde3e076c145fc2c77c9693cff
assessments:
- assessment_id: bgc-2661-identity
  area: identity
  topic: identity
  outcome: supported
  summary: Fulvuthiacene A preserves BGC0001941 compound 1, formula C24H39NO4S and
    full key XFAGIUVJPOMBNU-YLHPCDMOSA-N. The exact MIBiG row and both original diagnostic
    forms agree. The separately captured B owner has a distinct full key and chain
    length; shared BGC membership does not establish equivalent identity. NPA025855
    is a retained xref, not freshly resolved authority.
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  evidence_ids:
  - bgc-2661-identity
  - bgc-2661-xrefs
  - bgc-2661-chemistry
  - bgc-2661-query-mibig_compounds
  - bgc-2661-query-chebi_structures
  - bgc-2661-query-antibioticmech_inchikeys
  - bgc-2661-direct-contexts
  - bgc-2661-row-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: XFAGIUVJPOMBNU-YLHPCDMOSA-N; both saved forms regenerate this full key
    definition: Exact retained full key and original regeneration scope.
    evidence_ids:
    - bgc-2661-identity
    - bgc-2661-xrefs
    - bgc-2661-chemistry
    - bgc-2661-query-mibig_compounds
    - bgc-2661-query-chebi_structures
    - bgc-2661-query-antibioticmech_inchikeys
    - bgc-2661-direct-contexts
    - bgc-2661-row-mibig_compounds-0
  - name: grounding_scope
    value: MINTED naturalproductmech:mibig-02f0c67532; independent natural-material
      identity unverified
    definition: Recorded grounding distinguished from natural-material identity.
    evidence_ids:
    - bgc-2661-identity
    - bgc-2661-xrefs
    - bgc-2661-chemistry
    - bgc-2661-query-mibig_compounds
    - bgc-2661-query-chebi_structures
    - bgc-2661-query-antibioticmech_inchikeys
    - bgc-2661-direct-contexts
    - bgc-2661-row-mibig_compounds-0
- assessment_id: bgc-2661-representation
  area: representation
  topic: representation
  outcome: supported
  summary: Fulvuthiacene A is encoded as a neutral, acyclic substituted chain attached
    to one aromatic five-membered N/S thiazole ring. Both forms have one methyl ester
    and two additional methoxy bridges, with no amide motif or sugar-ring candidate.
    The two original tetrahedra have R/S assignments and both alkene geometries are
    specified E/Z. Both canonical strings agree and the 30-index one-way match is
    complete, while full_graph_identity_established remains false. Relative to the
    separately retained B owner, the written alkyl branch has two additional methylene
    units and the formula differs by C2H4; neither record is merged or used as independent
    biological evidence for the other.
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  evidence_ids:
  - bgc-2661-identity
  - bgc-2661-chemistry
  - bgc-2661-molecular-reading
  - bgc-2661-diagnostic-acceptance
  - bgc-2661-diagnostic-stderr
  - bgc-2661-stereo-schema
  - bgc-2661-stereo-extractor
  - bgc-2661-stereo-seeder
  dimensions:
  - name: stereochemistry_scope
    value: Two specified tetrahedral centres, R/S, and specified E/Z alkene bonds;
      no unknown tetrahedra
    definition: Original tetrahedral specification and geometric limits, separated
      from reconstructed imines.
    evidence_ids:
    - bgc-2661-identity
    - bgc-2661-chemistry
    - bgc-2661-molecular-reading
    - bgc-2661-diagnostic-acceptance
    - bgc-2661-diagnostic-stderr
    - bgc-2661-stereo-schema
    - bgc-2661-stereo-extractor
    - bgc-2661-stereo-seeder
  - name: representation_correspondence
    value: Both canonical comparisons true; complete 30-index one-way match; full-graph
      flag false
    definition: Canonical comparisons and attempted atom map, distinct from normalized
      identity.
    evidence_ids:
    - bgc-2661-identity
    - bgc-2661-chemistry
    - bgc-2661-molecular-reading
    - bgc-2661-diagnostic-acceptance
    - bgc-2661-diagnostic-stderr
    - bgc-2661-stereo-schema
    - bgc-2661-stereo-extractor
    - bgc-2661-stereo-seeder
- assessment_id: bgc-2661-provenance
  area: provenance
  topic: provenance
  outcome: unknown
  summary: Active BGC0001941 version 3 retains questionable entry quality and unknown
    completeness. Myxococcus fulvus, NCBITaxon:33, is SOURCE_ASSERTION; MH069655.1
    is separately CLUSTER_UNSTATED without retained bounds or methods. The shared
    source entry does not upgrade either compound to demonstrated production or assign
    pathway steps.
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  evidence_ids:
  - bgc-2661-provenance
  - bgc-2661-query-mibig_compounds
  - bgc-2661-taxonomy
  - bgc-2661-curation
  - bgc-2661-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    value: Myxococcus fulvus, NCBITaxon:33; retained producer and occurrence labels
    definition: Source labels, identifiers and cached taxonomy without new rank or
      lineage verification.
    evidence_ids:
    - bgc-2661-provenance
    - bgc-2661-query-mibig_compounds
    - bgc-2661-taxonomy
    - bgc-2661-curation
    - bgc-2661-row-mibig_compounds-0
  - name: producer_evidence
    value: SOURCE_ASSERTION
    definition: Literal producer assertion grade.
    evidence_ids:
    - bgc-2661-provenance
    - bgc-2661-query-mibig_compounds
    - bgc-2661-taxonomy
    - bgc-2661-curation
    - bgc-2661-row-mibig_compounds-0
  - name: locus_evidence
    value: 'BGC0001941: CLUSTER_UNSTATED; MH069655.1 without bounds or methods'
    definition: Literal locus-to-compound grade and source method.
    evidence_ids:
    - bgc-2661-provenance
    - bgc-2661-query-mibig_compounds
    - bgc-2661-taxonomy
    - bgc-2661-curation
    - bgc-2661-row-mibig_compounds-0
- assessment_id: bgc-2661-citations
  area: evidence
  topic: citations
  outcome: unknown
  summary: DOI:10.1021/acschembio.8b00948 is retained at COMPOUND_EVIDENCE grain in
    MIBiG. LOTUS retains the same DOI with uppercase spelling. These are database
    representations of a reference, not two independent publications or a fresh primary-paper
    reading.
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  evidence_ids:
  - bgc-2661-provenance
  - bgc-2661-occurrence-owner
  - bgc-2661-query-mibig_compounds
  - bgc-2661-query-lotus_occurrences
  - bgc-2661-source-reading
  - bgc-2661-row-mibig_compounds-0
  - bgc-2661-row-lotus_occurrences-0
  dimensions:
  - name: citation_scope
    value: COMPOUND_EVIDENCE DOI:10.1021/acschembio.8b00948; LOTUS case variant is
      not independent support
    definition: Reference grain and independence limits.
    evidence_ids:
    - bgc-2661-provenance
    - bgc-2661-occurrence-owner
    - bgc-2661-query-mibig_compounds
    - bgc-2661-query-lotus_occurrences
    - bgc-2661-source-reading
    - bgc-2661-row-mibig_compounds-0
    - bgc-2661-row-lotus_occurrences-0
- assessment_id: bgc-2661-occurrence_activity
  area: evidence
  topic: occurrence_activity
  outcome: unknown
  summary: One exact-key LOTUS row reports Myxococcus fulvus, NCBITaxon:33. It is
    an occurrence assertion distinct from demonstrated production. All saved assay
    and target query scopes are empty, with no AID sentinel or owner activity root;
    no potency, enzyme activity or molecular target is inferred.
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  evidence_ids:
  - bgc-2661-occurrence-owner
  - bgc-2661-mechanism-activity-scope
  - bgc-2661-query-lotus_occurrences
  - bgc-2661-query-pubchem_bioassay
  - bgc-2661-query-bindingdb_targets
  - bgc-2661-assay-curation
  - bgc-2661-chemistry
  - bgc-2661-row-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    value: One same-taxon LOTUS row; occurrence is not demonstrated production
    definition: Occurrence evidence separated from strain production.
    evidence_ids:
    - bgc-2661-occurrence-owner
    - bgc-2661-mechanism-activity-scope
    - bgc-2661-query-lotus_occurrences
    - bgc-2661-query-pubchem_bioassay
    - bgc-2661-query-bindingdb_targets
    - bgc-2661-assay-curation
    - bgc-2661-chemistry
    - bgc-2661-row-lotus_occurrences-0
  - name: assay_target_scope
    value: No retained exact-key AID, target or activity assertion
    definition: Retained assay scope and molecular-target limits.
    evidence_ids:
    - bgc-2661-occurrence-owner
    - bgc-2661-mechanism-activity-scope
    - bgc-2661-query-lotus_occurrences
    - bgc-2661-query-pubchem_bioassay
    - bgc-2661-query-bindingdb_targets
    - bgc-2661-assay-curation
    - bgc-2661-chemistry
    - bgc-2661-row-lotus_occurrences-0
- assessment_id: bgc-2661-classification
  area: consistency
  topic: classification
  outcome: unknown
  summary: The encoded thiazole-bearing unsaturated chain and methyl ester are consistent
    with a broad polyketide-like structural description; no amide backbone or sugar-ring
    candidate is present. The source class PKS and subclass Type I remain distinct.
    NPClassifier reports Amino acids and Peptides, Polyketides, Linear polyketides,
    and Melithiazole and Myxothiazole derivatives with is_glycoside false. The exact
    named family and amino-acid biosynthetic contribution remain model-level assertions,
    not independently established mechanisms.
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  evidence_ids:
  - bgc-2661-classification-owner
  - bgc-2661-chemistry
  - bgc-2661-query-npclassifier
  - bgc-2661-query-mibig_compounds
  - bgc-2661-row-npclassifier-0
  - bgc-2661-row-mibig_compounds-0
  dimensions:
  - name: classification_applicability
    value: Thiazole/ester chain observed; exact model family and biosynthetic contribution
      unverified
    definition: Encoded topology separated from exact model-family or biosynthetic
      proof.
    evidence_ids:
    - bgc-2661-classification-owner
    - bgc-2661-chemistry
    - bgc-2661-query-npclassifier
    - bgc-2661-query-mibig_compounds
    - bgc-2661-row-npclassifier-0
    - bgc-2661-row-mibig_compounds-0
- assessment_id: bgc-2661-completion
  area: completeness
  topic: completion
  outcome: unknown
  summary: The complete current owner and history, all nine saved query frames and
    both complete saved molecular forms were read; 45 actual input hashes and ownership
    declarations were verified. This is part of the accepted 443-input/54-path batch.
    Five local gates passed; full QC, complete OAK authority and fresh source verification
    remain unavailable. No selected maintained reader applies, and completion remains
    partial.
  target_ids:
  - naturalproductmech:mibig-02f0c67532
  evidence_ids:
  - bgc-2661-owner
  - bgc-2661-history
  - bgc-2661-intake
  - bgc-2661-intake-acceptance
  - bgc-2661-plan
  - bgc-2661-plan-acceptance
  - bgc-2661-gates
  - bgc-2661-source-reading
  - bgc-2661-source-notes
  - bgc-2661-molecular-reading
  - bgc-2661-mechanism-activity-scope
  dimensions:
  - name: review_completion
    value: Partial; complete owner, retained source scope, two saved forms and 45
      actual inputs
    definition: Actual local evidence coverage and unavailable verification.
    evidence_ids:
    - bgc-2661-owner
    - bgc-2661-history
    - bgc-2661-intake
    - bgc-2661-intake-acceptance
    - bgc-2661-plan
    - bgc-2661-plan-acceptance
    - bgc-2661-gates
    - bgc-2661-source-reading
    - bgc-2661-source-notes
    - bgc-2661-molecular-reading
    - bgc-2661-mechanism-activity-scope
findings: []
actions: []
limitations:
- Fresh database, primary-literature and complete ontology authority verification
  were unavailable under the no-request instruction. Retained source assertions and
  historical references are distinguished from freshly verified experiments.
- Both stored forms were inspected from the accepted original diagnostic only. Normalized
  identifiers, local motifs and a one-way atom match do not independently establish
  natural identity or complete graph identity; all false flags are retained.
- The four original warning blocks—two undefined-stereo and two charge-rearrangement
  warnings—are global and cannot be assigned to a particular owner or form from this
  stream.
- No mechanism, pathway, molecular target or component root occurs in these selected
  owners. No maintained reader applies. Full QC and complete OAK coverage remain unavailable,
  so scientific completion is partial.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- The differently reported local Cis/Trans descriptors depend on stereo-atom conventions;
  the saved bond E/Z labels and canonical strings agree across forms.
- The A/B formula difference is C2H4 and the written alkyl branches differ by two
  methylene units; no enzymatic conversion is inferred.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-267
```
