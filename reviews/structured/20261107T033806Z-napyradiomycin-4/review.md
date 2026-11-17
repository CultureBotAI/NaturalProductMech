# Local evidence review: napyradiomycin 4

- Review: 20261107T033806Z-napyradiomycin-4
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T02:55:59.694290Z
- Finished UTC: 2026-11-07T03:38:06.820273Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Napyradiomycin 4 retains the hydroxylated ring-junction form, five specified atom centres and one unresolved centre. Its source production/locus grades and bounded absence of occurrence data remain explicit. No congener occurrence or stereochemistry is transferred; review completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2814; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-128f11885c | data/natural_products/unclassified/napyradiomycin-4.yaml | generated | napyradiomycin 4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-128f11885c | Both exact stored forms parsed in the original twenty-attempt diagnostic and agree in formula, charge, normalized Standard InChI and complete key. |
| strict_ten | passed | True | naturalproductmech:mibig-128f11885c | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-128f11885c | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-128f11885c | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-128f11885c | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-128f11885c | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-128f11885c | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-128f11885c | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-128f11885c | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: naturalproductmech:mibig-128f11885c.

napyradiomycin 4 retains exact identifier naturalproductmech:mibig-128f11885c, complete key NLLBVEYNGJBFKB-JBPAMENMSA-N, and source rows BGC0001079 v5 compound index 4. No cross-references are retained. Both saved forms normalize to C26H34Cl2O7 and the declared full key. Distinct source compounds and direct companions retain their own full keys; no identity, experimental grade or stereochemistry is transferred.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-128f11885c.

The saved forms are neutral single-fragment C26H34Cl2O7 graphs with four six-membered rings, two ketone carbonyls, two phenolic hydroxyls, two tertiary alcohol sites and a saturated six-membered C5O ring. Both chlorines are aliphatic. Compared with the separately captured napyradiomycin 3 context, a ring-junction C-H is replaced by C-OH, accounting for the additional oxygen without a formula hydrogen increase. The local C5O motif does not establish a sugar assignment or glycosidic linkage. Both saved forms have five specified tetrahedral centres and one unspecified centre, corresponding to /t15? in the literal InChI. The hydroxyl-bearing ring junction is specified, while the separate carbocycle centre remains unresolved. stereo_complete:false is preserved and no configuration is transferred from the other napyradiomycins. Both original stored strings parsed with all ten saved comparisons true and a complete limited 35-atom chirality-aware map. The unresolved centre and separate full source key remain material. full_graph_identity_established remains false; no natural identity or congener equivalence is established.

### Producer assertion versus locus evidence

provenance: supported. Targets: naturalproductmech:mibig-128f11885c.

The retained producer is Streptomyces aculeolatus (NCBITaxon:270689), graded SOURCE_ASSERTION. No occurrence is imported into this owner from the other napyradiomycins; cached taxonomy alone does not strengthen the source production claim. BGC0001079 retains EF397638.1 with blank bounds, CLUSTER_DEMONSTRATED and source methods Enzymatic assays/Heterologous expression, separately from SOURCE_ASSERTION production. Active/complete status and questionable source quality do not establish every oxygenation or stereochemical step for this indexed chemical form.

### Citation grain and attributed history

evidence: supported. Targets: naturalproductmech:mibig-128f11885c.

BGC0001079: PMID:17392281 at ENTRY grain. These are attributed database citations, not newly examined primary bodies. DOI case variants and repeated placements do not create independent evidence. All 2 histories were read: 2 are seeder-attributed SEEDED_FROM_SOURCES events.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: naturalproductmech:mibig-128f11885c.

The complete owner has no occurrences root and its saved LOTUS frame has no match. That bounded retained-source absence is not absence in nature or permission to borrow occurrences from napyradiomycins 2 or 3. The saved PubChem BioAssay frame has no row or blank sentinel for this owner. No actual AID or molecular target is captured. ChEBI structure/origin, CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not global absence, inactivity, potency or target-mechanism proof.

### Computed filing and asserted class applicability

consistency: supported. Targets: naturalproductmech:mibig-128f11885c.

NPClassifier returns Polyketides plus Terpenoids with empty superclass/class arrays and isglycoside:false. The C5O ring and additional hydroxyl do not establish glycosylation. Multiple model pathways explain UNCLASSIFIED; the model cannot resolve the missing stereocentre or specific biosynthetic reactions.

### Local completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-128f11885c.

The complete current owner is carried from ROOT’s attributed whole-owner reading and exact current raw/capture equality. All 2 histories, nine saved source frames (2 positive placements/32 fields and 7 negatives), and both complete saved molecular forms were personally read. All 47 actual input hashes and maintained ownership paths join the accepted plan. Input pinning is not a claim to have substantively read every entire corpus. Five original local gates passed. The complete owner root set has no positive graph, pathway, component or molecular-target root, so no maintained reader applies. Full QC/OAK, fresh source-authority checks and independent primary confirmation remain unavailable; completion is partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2814-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/napyradiomycin-4.yaml; Complete plaintext, every root and all curation_history entries | supports | Complete current owner carried from ROOT’s attributed whole reading and joined exactly to capture; current source/history meanings were personally read. |
| bgc-2814-whole-owner-attribution | /private/tmp/npm-review-work/shared-next-batch282-tentative/root-conditional282-whole-owner-reading-001.json; /records | context_only | ROOT’s complete selected-owner reading is carried through exact current raw/capture equality; it is not additional BGC personal whole-owner credit. |
| bgc-2814-identity | /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json; /records/3/owner_document/identifier; /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status | supports | napyradiomycin 4 retains exact identifier naturalproductmech:mibig-128f11885c, complete key NLLBVEYNGJBFKB-JBPAMENMSA-N, and source rows BGC0001079 v5 compound index 4. No cross-references are retained. Both saved forms normalize to C26H34Cl2O7 and the declared full key. Distinct source compounds and direct companions retain their own full keys; no identity, experimental grade or stereochemistry is transferred. |
| bgc-2814-history | /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json; /records/3/owner_document/curation_history | supports | BGC0001079: PMID:17392281 at ENTRY grain. These are attributed database citations, not newly examined primary bodies. DOI case variants and repeated placements do not create independent evidence. All 2 histories were read: 2 are seeder-attributed SEEDED_FROM_SOURCES events. |
| bgc-2814-provenance | /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters | supports | The retained producer is Streptomyces aculeolatus (NCBITaxon:270689), graded SOURCE_ASSERTION. No occurrence is imported into this owner from the other napyradiomycins; cached taxonomy alone does not strengthen the source production claim. BGC0001079 retains EF397638.1 with blank bounds, CLUSTER_DEMONSTRATED and source methods Enzymatic assays/Heterologous expression, separately from SOURCE_ASSERTION production. Active/complete status and questionable source quality do not establish every oxygenation or stereochemical step for this indexed chemical form. |
| bgc-2814-classification | /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json; /records/3/owner_document/np_classification; /records/3/owner_document/np_pathway; /records/3/owner_document/bgc_class | supports | NPClassifier returns Polyketides plus Terpenoids with empty superclass/class arrays and isglycoside:false. The C5O ring and additional hydroxyl do not establish glycosylation. Multiple model pathways explain UNCLASSIFIED; the model cannot resolve the missing stereocentre or specific biosynthetic reactions. |
| bgc-2814-roots | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/13/complete_root_keys; /contexts/13/declared_mechanism_roots_literal; /contexts/13/literal_bioactivities_root | context_only | The complete owner root set has no positive graph, pathway, component or molecular-target root, so no maintained reader applies. |
| bgc-2814-chemistry | /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons; /records/3/atom_correspondence; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/declared_structure | supports | The saved forms are neutral single-fragment C26H34Cl2O7 graphs with four six-membered rings, two ketone carbonyls, two phenolic hydroxyls, two tertiary alcohol sites and a saturated six-membered C5O ring. Both chlorines are aliphatic. Compared with the separately captured napyradiomycin 3 context, a ring-junction C-H is replaced by C-OH, accounting for the additional oxygen without a formula hydrogen increase. The local C5O motif does not establish a sugar assignment or glycosidic linkage. Both saved forms have five specified tetrahedral centres and one unspecified centre, corresponding to /t15? in the literal InChI. The hydroxyl-bearing ring junction is specified, while the separate carbocycle centre remains unresolved. stereo_complete:false is preserved and no configuration is transferred from the other napyradiomycins. Both original stored strings parsed with all ten saved comparisons true and a complete limited 35-atom chirality-aware map. The unresolved centre and separate full source key remain material. full_graph_identity_established remains false; no natural identity or congener equivalence is established. |
| bgc-2814-molecular-reading | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-current282-first-five-molecular-intake-reading-001.json; /records/3; /personal_reading_scope; /global_cautions | supports | Complete saved tables personally read and interpreted without a new parse. |
| bgc-2814-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/root-current282-diagnostic-acceptance-001.json; /status; /accepted; /diagnostic; /molecular_parse_attempts; /limits | supports | ROOT accepted the original twenty stored-form attempts; exact representation and identity limits remain. |
| bgc-2814-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-execution-001.json; /command; /exit_code | supports | Original ROOT diagnostic command and exit zero; no replay. |
| bgc-2814-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-original-001.stderr; Complete original stderr including blank separators | context_only | Six undefined-stereo warnings remain globally unassigned; no message is attributed to this owner. |
| bgc-2814-intake | /private/tmp/npm-review-work/shared-next-batch282/intakes-001/2814-inspect-001.json; /targets; /source/inputs | supports | One exact target, 47 current inputs and explicit maintained ownership paths. |
| bgc-2814-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch282/root-current282-intake-acceptance-001.json; /accepted; /intake_summary; /records; /source_placements; /unique_source_paths | supports | All ten original inspections exited zero with empty stderr and 460 placements/65 paths. |
| bgc-2814-plan | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-target-input-plan-001.json; /records/3 | supports | Exact current input map, 3 direct companions and the literal reader applicability. |
| bgc-2814-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch282/root-current282-input-plan-acceptance-001.json; /accepted; /input_plan; /source_placements; /unique_source_paths | supports | ROOT accepted the current source input plan. |
| bgc-2814-gates | /private/tmp/npm-review-work/shared-next-batch282/root-current282-five-gates-acceptance-001.json; /records; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows | context_only | Five local gates passed; queue rows are review leads, not findings. Full QC/OAK remain unavailable. |
| bgc-2814-source-reading | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-current282-assigned-source-reading-001.json; /contexts/7; /counts; /reading_attribution | supports | All 2 complete positive dictionaries/32 fields and 7 bounded negative frames were personally read in the attributed source pass. |
| bgc-2814-source-notes | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-scope-notes-001.json; /totals; /reading_reconciliation; /reading_boundaries | context_only | The original 63 source placements/793 fields retain disjoint BGC 26 and Support 37 primary-row attribution. Native has no primary-row credit; ROOT’s overlapping two-assay-row reading adds no disjoint credit. |
| bgc-2814-taxonomy | /private/tmp/npm-review-work/shared-next-batch282-tentative/native-prep/native-current282-cached-taxonomy-reading-001.json; /scope; /context_interpretations/13; /interpretation | context_only | The retained producer is Streptomyces aculeolatus (NCBITaxon:270689), graded SOURCE_ASSERTION. No occurrence is imported into this owner from the other napyradiomycins; cached taxonomy alone does not strengthen the source production claim. Cached names do not independently supply rank, lineage or strain-level evidence. |
| bgc-2814-curation | /private/tmp/npm-review-work/shared-next-batch282-tentative/native-prep/native-current282-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation | context_only | Nine substantive tables/3,422 rows were scanned by Native; 18 lexical candidates yield zero exact applicable decisions. Two reserved census-only tables are excluded. |
| bgc-2814-assay-curation | /private/tmp/npm-review-work/shared-next-batch282-tentative/native-prep/native-current282-implemented-curation-scan-001.json; /assay_scope | context_only | The saved PubChem BioAssay frame has no row or blank sentinel for this owner. No actual AID or molecular target is captured. ChEBI structure/origin, CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not global absence, inactivity, potency or target-mechanism proof. |
| bgc-2814-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters(includeUnassigned=True) | context_only | The source stereo_complete flag tests unassigned atom-centred chirality, not all double-bond geometry or natural identity. |
| bgc-2814-stereo-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392-397: chemical_structure.stereo_complete | context_only | Schema preserves undefined stereocentres rather than inventing them; the maintained source extractor defines the actual atom-centre test. |
| bgc-2814-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306: choose_pathway | context_only | Exactly one supported mapped pathway selects filing; zero, unsupported single or multiple labels retain UNCLASSIFIED. |
| bgc-2814-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 positive placements, with all fields and bounded query meanings read. |
| bgc-2814-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 1256-1256; raw record sha256 ae057be4291425ebc7e4eafabe1e6ca4ee3c8009f7ffd8b530524b740b4c4e8e | supports | All 25 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2814-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2814-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/lotus_occurrences | context_only | Complete saved lotus_occurrences frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2814-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2814-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 positive placements, with all fields and bounded query meanings read. |
| bgc-2814-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 1623-1623; raw record sha256 6dbeef948af3c96ff23da294e493a066f940a6a544dc596b513e13b16f334146 | supports | All 7 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2814-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/pubchem_bioassay | context_only | Complete saved pubchem_bioassay frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2814-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2814-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2814-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2814-congener-0 | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/napyradiomycin-a80915c.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2814-congener-1 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/napyradiomycin-2.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2814-congener-2 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/napyradiomycin-3.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-282/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-282/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-282/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-282/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-282/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Fresh source-authority, primary publication, sequence and strain verification remain unavailable. Full QC/OAK were not run; retained experimental grades stay source-attributed.
- Both original stored strings parsed with all ten saved comparisons true and a complete limited 35-atom chirality-aware map. The unresolved centre and separate full source key remain material. full_graph_identity_established remains false; no natural identity or congener equivalence is established. Six undefined-stereo warnings remain globally unassigned; no message is attributed to this owner.
- Both saved forms have five specified tetrahedral centres and one unspecified centre, corresponding to /t15? in the literal InChI. The hydroxyl-bearing ring junction is specified, while the separate carbocycle centre remains unresolved. stereo_complete:false is preserved and no configuration is transferred from the other napyradiomycins.
- Saved topology supports the encoded molecule without independently establishing every natural residue, biosynthetic reaction or pharmacological mechanism.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- No record, source table, native scientific status or curation history is modified. Corrections, if later justified, belong in maintained source/curation/extractor ownership; curated mechanism changes require validated writing and attributed history.
- This author interpreted retained original outputs only, with zero molecular parses, source-query replays, target runs or outbound requests.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T033806Z-napyradiomycin-4
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: napyradiomycin 4'
started_at: '2026-11-07T02:55:59.694290Z'
finished_at: '2026-11-07T03:38:06.820273Z'
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
summary: Napyradiomycin 4 retains the hydroxylated ring-junction form, five specified
  atom centres and one unresolved centre. Its source production/locus grades and bounded
  absence of occurrence data remain explicit. No congener occurrence or stereochemistry
  is transferred; review completion is partial.
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
  - path: data/natural_products/terpenoids/napyradiomycin-a80915c.yaml
    sha256: 874e987f5d10a6f50e6ddb69eaaee9d2d1546585973e5c17e523ccbad0ce2f6a
    role: context
  - path: data/natural_products/unclassified/napyradiomycin-2.yaml
    sha256: 18ed9e81be4048777e9f483c31c350c9b9404986b72e6c6e01c165094db6a635
    role: context
  - path: data/natural_products/unclassified/napyradiomycin-3.yaml
    sha256: 05cc3846adf9347fb4d37b91236f6f305587405596bc7d0fe36e4f3673524b67
    role: context
  - path: data/natural_products/unclassified/napyradiomycin-4.yaml
    sha256: cea76506a39fea5e465fde3ac6908fa7d3cc464dcb0cf5d89d0e1055223a831d
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
  selection: Campaign path order 2814; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-128f11885c
targets:
- target_id: naturalproductmech:mibig-128f11885c
  path: data/natural_products/unclassified/napyradiomycin-4.yaml
  label: napyradiomycin 4
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnose282-001.py
    ddb26c5b49b323471e1246a18352bf9cf19325f959be014bba541e3c5a780d10 2a94e2ad0338b4b959ef7a27e176ebdb67a903ecd83f041068dac2a3e1f8cd35
    9f93ed9b2ebbecda2375829542ce823524b14b89071b27fd29f512838c8c18fb
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both exact stored forms parsed in the original twenty-attempt diagnostic
    and agree in formula, charge, normalized Standard InChI and complete key.
  scope_note: Both original stored strings parsed with all ten saved comparisons true
    and a complete limited 35-atom chirality-aware map. The unresolved centre and
    separate full source key remain material. full_graph_identity_established remains
    false; no natural identity or congener equivalence is established. Six undefined-stereo
    warnings remain globally unassigned; no message is attributed to this owner.
  target_ids:
  - naturalproductmech:mibig-128f11885c
  evidence_ids:
  - bgc-2814-chemistry
  - bgc-2814-diagnostic-acceptance
  - bgc-2814-diagnostic-execution
  - bgc-2814-diagnostic-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-128f11885c
  command: just validate-strict data/natural_products/unclassified/nannocystin-a.yaml
    data/natural_products/unclassified/napyradiomycin-2.yaml data/natural_products/unclassified/napyradiomycin-3.yaml
    data/natural_products/unclassified/napyradiomycin-4.yaml data/natural_products/unclassified/necroxime-b.yaml
    data/natural_products/unclassified/neoantimycin-2.yaml data/natural_products/unclassified/neoantimycin.yaml
    data/natural_products/unclassified/neocarzinostatin-chromophore.yaml data/natural_products/unclassified/neomediomycin-b.yaml
    data/natural_products/unclassified/nigrifactin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-282/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-128f11885c
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-282/validate-all-001.tsv
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
  - naturalproductmech:mibig-128f11885c
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
  - naturalproductmech:mibig-128f11885c
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
  - naturalproductmech:mibig-128f11885c
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-282/review-queue-001.tsv
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
  - naturalproductmech:mibig-128f11885c
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-128f11885c
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-128f11885c
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2814-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/napyradiomycin-4.yaml
  locator: Complete plaintext, every root and all curation_history entries
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: Complete current owner carried from ROOT’s attributed whole reading and
    joined exactly to capture; current source/history meanings were personally read.
  snapshot_sha256: cea76506a39fea5e465fde3ac6908fa7d3cc464dcb0cf5d89d0e1055223a831d
- evidence_id: bgc-2814-whole-owner-attribution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/root-conditional282-whole-owner-reading-001.json
  locator: /records
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: ROOT’s complete selected-owner reading is carried through exact current
    raw/capture equality; it is not additional BGC personal whole-owner credit.
  snapshot_sha256: 7ccbff8ec7f7200e131cc543de05fee533d8756fc396d9eed3074e7286e7f6b7
- evidence_id: bgc-2814-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json
  locator: /records/3/owner_document/identifier; /records/3/owner_document/chemical_structure;
    /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: napyradiomycin 4 retains exact identifier naturalproductmech:mibig-128f11885c,
    complete key NLLBVEYNGJBFKB-JBPAMENMSA-N, and source rows BGC0001079 v5 compound
    index 4. No cross-references are retained. Both saved forms normalize to C26H34Cl2O7
    and the declared full key. Distinct source compounds and direct companions retain
    their own full keys; no identity, experimental grade or stereochemistry is transferred.
  snapshot_sha256: 2a94e2ad0338b4b959ef7a27e176ebdb67a903ecd83f041068dac2a3e1f8cd35
- evidence_id: bgc-2814-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json
  locator: /records/3/owner_document/curation_history
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: 'BGC0001079: PMID:17392281 at ENTRY grain. These are attributed database
    citations, not newly examined primary bodies. DOI case variants and repeated placements
    do not create independent evidence. All 2 histories were read: 2 are seeder-attributed
    SEEDED_FROM_SOURCES events.'
  snapshot_sha256: 2a94e2ad0338b4b959ef7a27e176ebdb67a903ecd83f041068dac2a3e1f8cd35
- evidence_id: bgc-2814-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: The retained producer is Streptomyces aculeolatus (NCBITaxon:270689), graded
    SOURCE_ASSERTION. No occurrence is imported into this owner from the other napyradiomycins;
    cached taxonomy alone does not strengthen the source production claim. BGC0001079
    retains EF397638.1 with blank bounds, CLUSTER_DEMONSTRATED and source methods
    Enzymatic assays/Heterologous expression, separately from SOURCE_ASSERTION production.
    Active/complete status and questionable source quality do not establish every
    oxygenation or stereochemical step for this indexed chemical form.
  snapshot_sha256: 2a94e2ad0338b4b959ef7a27e176ebdb67a903ecd83f041068dac2a3e1f8cd35
- evidence_id: bgc-2814-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_classification; /records/3/owner_document/np_pathway;
    /records/3/owner_document/bgc_class
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: NPClassifier returns Polyketides plus Terpenoids with empty superclass/class
    arrays and isglycoside:false. The C5O ring and additional hydroxyl do not establish
    glycosylation. Multiple model pathways explain UNCLASSIFIED; the model cannot
    resolve the missing stereocentre or specific biosynthetic reactions.
  snapshot_sha256: 2a94e2ad0338b4b959ef7a27e176ebdb67a903ecd83f041068dac2a3e1f8cd35
- evidence_id: bgc-2814-roots
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/13/complete_root_keys; /contexts/13/declared_mechanism_roots_literal;
    /contexts/13/literal_bioactivities_root
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: The complete owner root set has no positive graph, pathway, component or
    molecular-target root, so no maintained reader applies.
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: Complete captured owner root set, not a biological absence claim.
- evidence_id: bgc-2814-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons;
    /records/3/atom_correspondence; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds;
    /records/2/declared_structure
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: The saved forms are neutral single-fragment C26H34Cl2O7 graphs with four
    six-membered rings, two ketone carbonyls, two phenolic hydroxyls, two tertiary
    alcohol sites and a saturated six-membered C5O ring. Both chlorines are aliphatic.
    Compared with the separately captured napyradiomycin 3 context, a ring-junction
    C-H is replaced by C-OH, accounting for the additional oxygen without a formula
    hydrogen increase. The local C5O motif does not establish a sugar assignment or
    glycosidic linkage. Both saved forms have five specified tetrahedral centres and
    one unspecified centre, corresponding to /t15? in the literal InChI. The hydroxyl-bearing
    ring junction is specified, while the separate carbocycle centre remains unresolved.
    stereo_complete:false is preserved and no configuration is transferred from the
    other napyradiomycins. Both original stored strings parsed with all ten saved
    comparisons true and a complete limited 35-atom chirality-aware map. The unresolved
    centre and separate full source key remain material. full_graph_identity_established
    remains false; no natural identity or congener equivalence is established.
  snapshot_sha256: b8723a2c2f820f7bded66a674a1aa9228bf11d19c25f92fb816090125edecfc9
- evidence_id: bgc-2814-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-current282-first-five-molecular-intake-reading-001.json
  locator: /records/3; /personal_reading_scope; /global_cautions
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: Complete saved tables personally read and interpreted without a new parse.
  snapshot_sha256: 835e7170c9d0a7f50fc3c723247989260a0b2b9adb9beda6ede429c36bf68a46
- evidence_id: bgc-2814-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/root-current282-diagnostic-acceptance-001.json
  locator: /status; /accepted; /diagnostic; /molecular_parse_attempts; /limits
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form attempts; exact representation
    and identity limits remain.
  snapshot_sha256: aa0cfe84870e49a819a87cbbc8094e2522a8e8b0143bd6bb21bcb29d1211679b
- evidence_id: bgc-2814-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: Original ROOT diagnostic command and exit zero; no replay.
  snapshot_sha256: edbe8e835223207019e1654a83719f8f5a4356c9c4ce4bf65b3416defeeced22
- evidence_id: bgc-2814-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr including blank separators
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: Six undefined-stereo warnings remain globally unassigned; no message is
    attributed to this owner.
  snapshot_sha256: da9c0e81ec69521d5ee373f4100f63c8d2d23091a4f6562a0e39bfafc12e03f6
- evidence_id: bgc-2814-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/intakes-001/2814-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: One exact target, 47 current inputs and explicit maintained ownership paths.
  snapshot_sha256: 63216af8fdf9f914a34c64bd20197a84f05b2a9931fb8642e3be453b00e09a67
- evidence_id: bgc-2814-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/root-current282-intake-acceptance-001.json
  locator: /accepted; /intake_summary; /records; /source_placements; /unique_source_paths
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: All ten original inspections exited zero with empty stderr and 460 placements/65
    paths.
  snapshot_sha256: bcc44a28603093d5698cc3314edd9fcd4d00da9d335f3d01c0fd69bb09375907
- evidence_id: bgc-2814-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-target-input-plan-001.json
  locator: /records/3
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: Exact current input map, 3 direct companions and the literal reader applicability.
  snapshot_sha256: 92b2c735b1716c07a2fea1c7c34caf4ad63fa45e2b2be7236ccf7ad97beaa06b
- evidence_id: bgc-2814-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/root-current282-input-plan-acceptance-001.json
  locator: /accepted; /input_plan; /source_placements; /unique_source_paths
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: ROOT accepted the current source input plan.
  snapshot_sha256: 8b8a6476268a7af1cc5b9cae8af2eb5909613b261055a9801dad3be298d4a294
- evidence_id: bgc-2814-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/root-current282-five-gates-acceptance-001.json
  locator: /records; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: Five local gates passed; queue rows are review leads, not findings. Full
    QC/OAK remain unavailable.
  snapshot_sha256: c371d0597706c9c881bd2f515a1314108d3eaa162d3ff8d18acd48b74db9239e
- evidence_id: bgc-2814-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-current282-assigned-source-reading-001.json
  locator: /contexts/7; /counts; /reading_attribution
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: All 2 complete positive dictionaries/32 fields and 7 bounded negative frames
    were personally read in the attributed source pass.
  snapshot_sha256: d664b3fb73062b9714dacc31dfe5690784b23b60f707a54f9f43da7cb3ac8004
- evidence_id: bgc-2814-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: The original 63 source placements/793 fields retain disjoint BGC 26 and
    Support 37 primary-row attribution. Native has no primary-row credit; ROOT’s overlapping
    two-assay-row reading adds no disjoint credit.
  snapshot_sha256: 6a37d82b406b849e574c64989542ecd594b7ba449e5b64126cc88856c975164d
- evidence_id: bgc-2814-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/native-prep/native-current282-cached-taxonomy-reading-001.json
  locator: /scope; /context_interpretations/13; /interpretation
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: The retained producer is Streptomyces aculeolatus (NCBITaxon:270689), graded
    SOURCE_ASSERTION. No occurrence is imported into this owner from the other napyradiomycins;
    cached taxonomy alone does not strengthen the source production claim. Cached
    names do not independently supply rank, lineage or strain-level evidence.
  snapshot_sha256: 1af1cb0b6cd2ad65ea34a03d0f9c8a746e250c6b9e51cd28c7bc15238b82c98a
  search_scope: Exact current taxon route and retained cached names/synonyms; no fresh
    external taxonomy or inferred hierarchy.
- evidence_id: bgc-2814-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/native-prep/native-current282-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: Nine substantive tables/3,422 rows were scanned by Native; 18 lexical candidates
    yield zero exact applicable decisions. Two reserved census-only tables are excluded.
  snapshot_sha256: f6c068d113e15f780e75e277a2f18431aca40b12e9343964db87f8043c2c7fd5
  search_scope: Actual captured table inputs and exact identity/source/occurrence/assay
    predicates; no decision from lexical similarity.
- evidence_id: bgc-2814-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/native-prep/native-current282-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: The saved PubChem BioAssay frame has no row or blank sentinel for this
    owner. No actual AID or molecular target is captured. ChEBI structure/origin,
    CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not
    global absence, inactivity, potency or target-mechanism proof.
  snapshot_sha256: f6c068d113e15f780e75e277a2f18431aca40b12e9343964db87f8043c2c7fd5
  search_scope: Exact owner full-key/CID scope; blank-AID rows are sentinels. No other-owner
    assay is transferred.
- evidence_id: bgc-2814-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters(includeUnassigned=True)'
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: The source stereo_complete flag tests unassigned atom-centred chirality,
    not all double-bond geometry or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2814-stereo-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: 'lines 392-397: chemical_structure.stereo_complete'
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: Schema preserves undefined stereocentres rather than inventing them; the
    maintained source extractor defines the actual atom-centre test.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2814-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines 295-306: choose_pathway'
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: Exactly one supported mapped pathway selects filing; zero, unsupported
    single or multiple labels retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2814-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
- evidence_id: bgc-2814-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 1256-1256; raw record sha256 ae057be4291425ebc7e4eafabe1e6ca4ee3c8009f7ffd8b530524b740b4c4e8e
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: All 25 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2814-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: 'Complete saved chebi_structures frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/napyradiomycin-4.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "NLLBVEYNGJBFKB-JBPAMENMSA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2814-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: 'Complete saved lotus_occurrences frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/napyradiomycin-4.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "NLLBVEYNGJBFKB-JBPAMENMSA-N",
    "table": "lotus_occurrences"}'
- evidence_id: bgc-2814-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences frame: 0 positive placements, with
    all fields and bounded query meanings read.'
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/napyradiomycin-4.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "NLLBVEYNGJBFKB-JBPAMENMSA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2814-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 positive placements, with all fields
    and bounded query meanings read.'
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
- evidence_id: bgc-2814-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 1623-1623; raw record sha256 6dbeef948af3c96ff23da294e493a066f940a6a544dc596b513e13b16f334146
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: supports
  summary: All 7 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2814-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: 'Complete saved pubchem_bioassay frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/napyradiomycin-4.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "NLLBVEYNGJBFKB-JBPAMENMSA-N",
    "table": "pubchem_bioassay"}'
- evidence_id: bgc-2814-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/napyradiomycin-4.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "NLLBVEYNGJBFKB-JBPAMENMSA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2814-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 positive placements,
    with all fields and bounded query meanings read.'
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/napyradiomycin-4.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "NLLBVEYNGJBFKB-JBPAMENMSA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2814-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: 'Complete saved chebi_origins frame: 0 positive placements, with all fields
    and bounded query meanings read.'
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/napyradiomycin-4.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: bgc-2814-congener-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/napyradiomycin-a80915c.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 874e987f5d10a6f50e6ddb69eaaee9d2d1546585973e5c17e523ccbad0ce2f6a
- evidence_id: bgc-2814-congener-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/napyradiomycin-2.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 18ed9e81be4048777e9f483c31c350c9b9404986b72e6c6e01c165094db6a635
- evidence_id: bgc-2814-congener-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/napyradiomycin-3.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T03:24:38.972140Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 05cc3846adf9347fb4d37b91236f6f305587405596bc7d0fe36e4f3673524b67
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-282/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json
  accessed_at: '2026-11-07T02:57:33.203784Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 64d3574e79778146d92ca263450b21c2b1069ed2e3c619de74334e87646ea9bb
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-282/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json
  accessed_at: '2026-11-07T02:57:58.096578Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: fe9b4651b4ba89812db89378bcc5bd759f45f66d8d27a8bae471ff3e72ef0180
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-282/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json
  accessed_at: '2026-11-07T02:58:17.725128Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-282/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json
  accessed_at: '2026-11-07T02:58:51.640951Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-282/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json
  accessed_at: '2026-11-07T02:59:03.312006Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 242feea98ad824bbb95284fc6ee693a3464fd1917a299d276b43d18e23f24d2a
assessments:
- assessment_id: bgc-2814-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: napyradiomycin 4 retains exact identifier naturalproductmech:mibig-128f11885c,
    complete key NLLBVEYNGJBFKB-JBPAMENMSA-N, and source rows BGC0001079 v5 compound
    index 4. No cross-references are retained. Both saved forms normalize to C26H34Cl2O7
    and the declared full key. Distinct source compounds and direct companions retain
    their own full keys; no identity, experimental grade or stereochemistry is transferred.
  target_ids:
  - naturalproductmech:mibig-128f11885c
  evidence_ids:
  - bgc-2814-identity
  - bgc-2814-whole-owner-attribution
  - bgc-2814-chemistry
  - bgc-2814-query-mibig_compounds
  - bgc-2814-plan
  - bgc-2814-row-mibig_compounds-0
  - bgc-2814-congener-0
  - bgc-2814-congener-1
  - bgc-2814-congener-2
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    value: NLLBVEYNGJBFKB-JBPAMENMSA-N
    evidence_ids:
    - bgc-2814-identity
    - bgc-2814-whole-owner-attribution
    - bgc-2814-chemistry
    - bgc-2814-query-mibig_compounds
    - bgc-2814-plan
    - bgc-2814-row-mibig_compounds-0
    - bgc-2814-congener-0
    - bgc-2814-congener-1
    - bgc-2814-congener-2
  - name: grounding_scope
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    value: napyradiomycin 4 retains exact identifier naturalproductmech:mibig-128f11885c,
      complete key NLLBVEYNGJBFKB-JBPAMENMSA-N, and source rows BGC0001079 v5 compound
      index 4. No cross-references are retained. Both saved forms normalize to C26H34Cl2O7
      and the declared full key. Distinct source compounds and direct companions retain
      their own full keys; no identity, experimental grade or stereochemistry is transferred.
    evidence_ids:
    - bgc-2814-identity
    - bgc-2814-whole-owner-attribution
    - bgc-2814-chemistry
    - bgc-2814-query-mibig_compounds
    - bgc-2814-plan
    - bgc-2814-row-mibig_compounds-0
    - bgc-2814-congener-0
    - bgc-2814-congener-1
    - bgc-2814-congener-2
- assessment_id: bgc-2814-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: The saved forms are neutral single-fragment C26H34Cl2O7 graphs with four
    six-membered rings, two ketone carbonyls, two phenolic hydroxyls, two tertiary
    alcohol sites and a saturated six-membered C5O ring. Both chlorines are aliphatic.
    Compared with the separately captured napyradiomycin 3 context, a ring-junction
    C-H is replaced by C-OH, accounting for the additional oxygen without a formula
    hydrogen increase. The local C5O motif does not establish a sugar assignment or
    glycosidic linkage. Both saved forms have five specified tetrahedral centres and
    one unspecified centre, corresponding to /t15? in the literal InChI. The hydroxyl-bearing
    ring junction is specified, while the separate carbocycle centre remains unresolved.
    stereo_complete:false is preserved and no configuration is transferred from the
    other napyradiomycins. Both original stored strings parsed with all ten saved
    comparisons true and a complete limited 35-atom chirality-aware map. The unresolved
    centre and separate full source key remain material. full_graph_identity_established
    remains false; no natural identity or congener equivalence is established.
  target_ids:
  - naturalproductmech:mibig-128f11885c
  evidence_ids:
  - bgc-2814-identity
  - bgc-2814-chemistry
  - bgc-2814-molecular-reading
  - bgc-2814-diagnostic-acceptance
  - bgc-2814-diagnostic-stderr
  - bgc-2814-stereo-policy
  - bgc-2814-stereo-schema
  dimensions:
  - name: stereochemistry_scope
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    value: Both saved forms have five specified tetrahedral centres and one unspecified
      centre, corresponding to /t15? in the literal InChI. The hydroxyl-bearing ring
      junction is specified, while the separate carbocycle centre remains unresolved.
      stereo_complete:false is preserved and no configuration is transferred from
      the other napyradiomycins.
    evidence_ids:
    - bgc-2814-identity
    - bgc-2814-chemistry
    - bgc-2814-molecular-reading
    - bgc-2814-diagnostic-acceptance
    - bgc-2814-diagnostic-stderr
    - bgc-2814-stereo-policy
    - bgc-2814-stereo-schema
  - name: representation_correspondence
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    value: Both original stored strings parsed with all ten saved comparisons true
      and a complete limited 35-atom chirality-aware map. The unresolved centre and
      separate full source key remain material. full_graph_identity_established remains
      false; no natural identity or congener equivalence is established.
    evidence_ids:
    - bgc-2814-identity
    - bgc-2814-chemistry
    - bgc-2814-molecular-reading
    - bgc-2814-diagnostic-acceptance
    - bgc-2814-diagnostic-stderr
    - bgc-2814-stereo-policy
    - bgc-2814-stereo-schema
- assessment_id: bgc-2814-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: The retained producer is Streptomyces aculeolatus (NCBITaxon:270689), graded
    SOURCE_ASSERTION. No occurrence is imported into this owner from the other napyradiomycins;
    cached taxonomy alone does not strengthen the source production claim. BGC0001079
    retains EF397638.1 with blank bounds, CLUSTER_DEMONSTRATED and source methods
    Enzymatic assays/Heterologous expression, separately from SOURCE_ASSERTION production.
    Active/complete status and questionable source quality do not establish every
    oxygenation or stereochemical step for this indexed chemical form.
  target_ids:
  - naturalproductmech:mibig-128f11885c
  evidence_ids:
  - bgc-2814-provenance
  - bgc-2814-query-mibig_compounds
  - bgc-2814-taxonomy
  - bgc-2814-curation
  - bgc-2814-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    value: The retained producer is Streptomyces aculeolatus (NCBITaxon:270689), graded
      SOURCE_ASSERTION. No occurrence is imported into this owner from the other napyradiomycins;
      cached taxonomy alone does not strengthen the source production claim.
    evidence_ids:
    - bgc-2814-provenance
    - bgc-2814-query-mibig_compounds
    - bgc-2814-taxonomy
    - bgc-2814-curation
    - bgc-2814-row-mibig_compounds-0
  - name: producer_evidence
    definition: Producer evidence grade and its demonstrated or asserted scope.
    value: The retained producer is Streptomyces aculeolatus (NCBITaxon:270689), graded
      SOURCE_ASSERTION. No occurrence is imported into this owner from the other napyradiomycins;
      cached taxonomy alone does not strengthen the source production claim.
    evidence_ids:
    - bgc-2814-provenance
    - bgc-2814-query-mibig_compounds
    - bgc-2814-taxonomy
    - bgc-2814-curation
    - bgc-2814-row-mibig_compounds-0
  - name: locus_evidence
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    value: BGC0001079 retains EF397638.1 with blank bounds, CLUSTER_DEMONSTRATED and
      source methods Enzymatic assays/Heterologous expression, separately from SOURCE_ASSERTION
      production. Active/complete status and questionable source quality do not establish
      every oxygenation or stereochemical step for this indexed chemical form.
    evidence_ids:
    - bgc-2814-provenance
    - bgc-2814-query-mibig_compounds
    - bgc-2814-taxonomy
    - bgc-2814-curation
    - bgc-2814-row-mibig_compounds-0
- assessment_id: bgc-2814-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: 'BGC0001079: PMID:17392281 at ENTRY grain. These are attributed database
    citations, not newly examined primary bodies. DOI case variants and repeated placements
    do not create independent evidence. All 2 histories were read: 2 are seeder-attributed
    SEEDED_FROM_SOURCES events.'
  target_ids:
  - naturalproductmech:mibig-128f11885c
  evidence_ids:
  - bgc-2814-history
  - bgc-2814-source-reading
  - bgc-2814-query-mibig_compounds
  - bgc-2814-row-mibig_compounds-0
  dimensions:
  - name: citation_scope
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    value: 'BGC0001079: PMID:17392281 at ENTRY grain. These are attributed database
      citations, not newly examined primary bodies. DOI case variants and repeated
      placements do not create independent evidence. All 2 histories were read: 2
      are seeder-attributed SEEDED_FROM_SOURCES events.'
    evidence_ids:
    - bgc-2814-history
    - bgc-2814-source-reading
    - bgc-2814-query-mibig_compounds
    - bgc-2814-row-mibig_compounds-0
- assessment_id: bgc-2814-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: The complete owner has no occurrences root and its saved LOTUS frame has
    no match. That bounded retained-source absence is not absence in nature or permission
    to borrow occurrences from napyradiomycins 2 or 3. The saved PubChem BioAssay
    frame has no row or blank sentinel for this owner. No actual AID or molecular
    target is captured. ChEBI structure/origin, CyanoMetDB, BindingDB and AntibioticMech
    frames are bounded local negatives, not global absence, inactivity, potency or
    target-mechanism proof.
  target_ids:
  - naturalproductmech:mibig-128f11885c
  evidence_ids:
  - bgc-2814-roots
  - bgc-2814-query-lotus_occurrences
  - bgc-2814-query-chebi_origins
  - bgc-2814-query-cyanometdb_occurrences
  - bgc-2814-query-pubchem_bioassay
  - bgc-2814-query-bindingdb_targets
  - bgc-2814-query-antibioticmech_inchikeys
  - bgc-2814-assay-curation
  dimensions:
  - name: occurrence_scope
    definition: Exact retained occurrence tuples and limits on production/independence.
    value: The complete owner has no occurrences root and its saved LOTUS frame has
      no match. That bounded retained-source absence is not absence in nature or permission
      to borrow occurrences from napyradiomycins 2 or 3.
    evidence_ids:
    - bgc-2814-roots
    - bgc-2814-query-lotus_occurrences
    - bgc-2814-query-chebi_origins
    - bgc-2814-query-cyanometdb_occurrences
    - bgc-2814-query-pubchem_bioassay
    - bgc-2814-query-bindingdb_targets
    - bgc-2814-query-antibioticmech_inchikeys
    - bgc-2814-assay-curation
  - name: assay_target_scope
    definition: Retained activity/assay/target positives and bounded negative queries.
    value: The saved PubChem BioAssay frame has no row or blank sentinel for this
      owner. No actual AID or molecular target is captured. ChEBI structure/origin,
      CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives,
      not global absence, inactivity, potency or target-mechanism proof.
    evidence_ids:
    - bgc-2814-roots
    - bgc-2814-query-lotus_occurrences
    - bgc-2814-query-chebi_origins
    - bgc-2814-query-cyanometdb_occurrences
    - bgc-2814-query-pubchem_bioassay
    - bgc-2814-query-bindingdb_targets
    - bgc-2814-query-antibioticmech_inchikeys
    - bgc-2814-assay-curation
- assessment_id: bgc-2814-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: NPClassifier returns Polyketides plus Terpenoids with empty superclass/class
    arrays and isglycoside:false. The C5O ring and additional hydroxyl do not establish
    glycosylation. Multiple model pathways explain UNCLASSIFIED; the model cannot
    resolve the missing stereocentre or specific biosynthetic reactions.
  target_ids:
  - naturalproductmech:mibig-128f11885c
  evidence_ids:
  - bgc-2814-classification
  - bgc-2814-chemistry
  - bgc-2814-query-npclassifier
  - bgc-2814-query-mibig_compounds
  - bgc-2814-filing-policy
  - bgc-2814-row-npclassifier-0
  - bgc-2814-row-mibig_compounds-0
  dimensions:
  - name: classification_applicability
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    value: NPClassifier returns Polyketides plus Terpenoids with empty superclass/class
      arrays and isglycoside:false. The C5O ring and additional hydroxyl do not establish
      glycosylation. Multiple model pathways explain UNCLASSIFIED; the model cannot
      resolve the missing stereocentre or specific biosynthetic reactions.
    evidence_ids:
    - bgc-2814-classification
    - bgc-2814-chemistry
    - bgc-2814-query-npclassifier
    - bgc-2814-query-mibig_compounds
    - bgc-2814-filing-policy
    - bgc-2814-row-npclassifier-0
    - bgc-2814-row-mibig_compounds-0
- assessment_id: bgc-2814-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: unknown
  summary: The complete current owner is carried from ROOT’s attributed whole-owner
    reading and exact current raw/capture equality. All 2 histories, nine saved source
    frames (2 positive placements/32 fields and 7 negatives), and both complete saved
    molecular forms were personally read. All 47 actual input hashes and maintained
    ownership paths join the accepted plan. Input pinning is not a claim to have substantively
    read every entire corpus. Five original local gates passed. The complete owner
    root set has no positive graph, pathway, component or molecular-target root, so
    no maintained reader applies. Full QC/OAK, fresh source-authority checks and independent
    primary confirmation remain unavailable; completion is partial.
  target_ids:
  - naturalproductmech:mibig-128f11885c
  evidence_ids:
  - bgc-2814-owner
  - bgc-2814-whole-owner-attribution
  - bgc-2814-history
  - bgc-2814-intake
  - bgc-2814-intake-acceptance
  - bgc-2814-plan
  - bgc-2814-plan-acceptance
  - bgc-2814-gates
  - bgc-2814-source-reading
  - bgc-2814-source-notes
  - bgc-2814-molecular-reading
  - bgc-2814-roots
  dimensions:
  - name: review_completion
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    value: The complete current owner is carried from ROOT’s attributed whole-owner
      reading and exact current raw/capture equality. All 2 histories, nine saved
      source frames (2 positive placements/32 fields and 7 negatives), and both complete
      saved molecular forms were personally read. All 47 actual input hashes and maintained
      ownership paths join the accepted plan. Input pinning is not a claim to have
      substantively read every entire corpus. Five original local gates passed. The
      complete owner root set has no positive graph, pathway, component or molecular-target
      root, so no maintained reader applies. Full QC/OAK, fresh source-authority checks
      and independent primary confirmation remain unavailable; completion is partial.
    evidence_ids:
    - bgc-2814-owner
    - bgc-2814-whole-owner-attribution
    - bgc-2814-history
    - bgc-2814-intake
    - bgc-2814-intake-acceptance
    - bgc-2814-plan
    - bgc-2814-plan-acceptance
    - bgc-2814-gates
    - bgc-2814-source-reading
    - bgc-2814-source-notes
    - bgc-2814-molecular-reading
    - bgc-2814-roots
findings: []
actions: []
limitations:
- Fresh source-authority, primary publication, sequence and strain verification remain
  unavailable. Full QC/OAK were not run; retained experimental grades stay source-attributed.
- Both original stored strings parsed with all ten saved comparisons true and a complete
  limited 35-atom chirality-aware map. The unresolved centre and separate full source
  key remain material. full_graph_identity_established remains false; no natural identity
  or congener equivalence is established. Six undefined-stereo warnings remain globally
  unassigned; no message is attributed to this owner.
- Both saved forms have five specified tetrahedral centres and one unspecified centre,
  corresponding to /t15? in the literal InChI. The hydroxyl-bearing ring junction
  is specified, while the separate carbocycle centre remains unresolved. stereo_complete:false
  is preserved and no configuration is transferred from the other napyradiomycins.
- Saved topology supports the encoded molecule without independently establishing
  every natural residue, biosynthetic reaction or pharmacological mechanism.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- No record, source table, native scientific status or curation history is modified.
  Corrections, if later justified, belong in maintained source/curation/extractor
  ownership; curated mechanism changes require validated writing and attributed history.
- This author interpreted retained original outputs only, with zero molecular parses,
  source-query replays, target runs or outbound requests.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-282
```
