# Local evidence review: ilicicolin B

- Review: 20261106T133430Z-ilicicolin-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T12:38:14.164535Z
- Finished UTC: 2026-11-06T13:34:30.932191Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Ilicicolin B has matching stored-form canonical strings and an exact retained ChEBI target, while the OPEN LL-Z1272beta naming discussion remains unresolved. Coarse antimicrobial and occurrence evidence are retained without assay or mechanism transfer.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2713; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:146153 | data/natural_products/unclassified/ilicicolin-b.yaml | generated | ilicicolin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | CHEBI:146153 | Both stored forms parsed in the original twenty-attempt execution; within-owner formula, charge, Standard InChI and complete key agree. |
| strict_ten | passed | True | CHEBI:146153 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:146153 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:146153 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:146153 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:146153 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:146153 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:146153 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:146153 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: CHEBI:146153.

CHEBI:146153 is the exact selected target with QAPOXOGEDXIOHD-VZRGJMDUSA-N. Retained ChEBI 3-star and MIBiG BGC0001390 compound1 source concepts share this full key but name it Ilicicolin B and LL-Z1272beta respectively. The existing OPEN name-disagreement remains explicit; matching local canonical strings do not decide synonymy or which source name is correct.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: CHEBI:146153.

Both forms encode one aromatic six-membered ring, an aldehyde and two phenolic OH groups, with a branched unsaturated side chain. Two alkenes are specified E; the other side-chain double bond has equivalent methyl substituents at one end and is not an omitted stereogenic alkene. No amide, ester or sugar-ring candidate is returned. There are no tetrahedral centres and two specified E alkenes in both saved forms. The third side-chain alkene is nonstereogenic because one end has equivalent methyl groups. The stored true flag and literal alkene layers are retained; no natural stereochemical assignment was newly measured. C23H32O3, neutral charge, Standard InChI, full key and both canonical SMILES agree. The saved one-way chirality-aware match covers all 26 atoms, while full_graph_identity_established remains false. This bounded agreement does not adjudicate the retained Ilicicolin B versus LL-Z1272beta naming discussion or certify natural identity.

### Producer assertion versus locus evidence

provenance: supported. Targets: CHEBI:146153.

MIBiG entry3 is active/questionable/unknown, SOURCE_ASSERTION for Stachybotrys bisbyi80385, with NRPS&#124;PKS and Type I&#124;Unknown, genome LC125467.1 but blank locus bounds/methods and CLUSTER_UNSTATED. DOI:10.1016/j.bbabio.2008.11.016 is COMPOUND_BIOACTIVITY grain and cannot be promoted to biosynthetic proof.

### Citation grain and attributed history

evidence: supported. Targets: CHEBI:146153.

DOI:10.1016/j.bbabio.2008.11.016 / COMPOUND_BIOACTIVITY; all 2 complete history events are seeder-attributed provenance, not fresh primary reading. Citation presence does not imply that the underlying article was newly read.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: CHEBI:146153.

Two exact-key LOTUS rows: Albatrellus ovinus/139090 with DOI:10.1016/S0223-5234(97)89088-5 and Neonectria coccinea/57153 with DOI:10.1039/P19720002136. Their distinct occurrence claims do not establish the MIBiG producer or biosynthesis. The exact-key AntibioticMech CHEBI:146153 link retains ANTIMICROBIAL_UNSPECIFIED from the pinned sibling inventory. This coarse summary is not an AID, target, affinity or demonstrated mechanism. No current AID, blank sentinel or BindingDB row matches; the related-corpus projection is not an extra independent measurement.

### Computed filing and asserted class applicability

consistency: supported. Targets: CHEBI:146153.

Meroterpenoids/Tetraketide meroterpenoids is a computed classification compatible at a broad level with the phenolic ring and branched unsaturated side chain. Neither the model nor the MIBiG NRPS&#124;PKS label proves a four-ketide contribution, enzymatic route or natural identity. The saved forms contain no glycosidic candidate, consistent with the retained false prediction at this limited scope. Each record retains two computed pathway labels, so maintained choose_pathway files it UNCLASSIFIED while preserving both labels. This is consistent filing, not a claim of biological absence or an erased classification.

### Local completion and maintained ownership

completeness: supported. Targets: CHEBI:146153.

Complete owner/history, all nine saved query frames (6 positive placements/56 fields) and both complete saved molecular forms were personally read. The 44 actual input hashes and ownership declarations were verified; this does not claim semantic reading of entire corpus input files. Required native local gates passed; full QC, OAK, live authority and primary-paper verification are unavailable. No selected mechanism root or component requires a maintained reader. Corrections belong in maintained inputs/extractors or the seeder; no record edit is proposed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2713-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/ilicicolin-b.yaml; Complete plaintext and all curation_history entries | supports | Whole current owner/history personally read; generated source assertions remain distinct from fresh primary evidence. |
| bgc-2713-identity | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/2/owner_document/identifier; /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status | supports | CHEBI:146153 is the exact selected target with QAPOXOGEDXIOHD-VZRGJMDUSA-N. Retained ChEBI 3-star and MIBiG BGC0001390 compound1 source concepts share this full key but name it Ilicicolin B and LL-Z1272beta respectively. The existing OPEN name-disagreement remains explicit; matching local canonical strings do not decide synonymy or which source name is correct. |
| bgc-2713-history | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/2/owner_document/curation_history | supports | DOI:10.1016/j.bbabio.2008.11.016 / COMPOUND_BIOACTIVITY; all 2 complete history events are seeder-attributed provenance, not fresh primary reading. Citation presence does not imply that the underlying article was newly read. |
| bgc-2713-provenance | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters | supports | MIBiG entry3 is active/questionable/unknown, SOURCE_ASSERTION for Stachybotrys bisbyi80385, with NRPS&#124;PKS and Type I&#124;Unknown, genome LC125467.1 but blank locus bounds/methods and CLUSTER_UNSTATED. DOI:10.1016/j.bbabio.2008.11.016 is COMPOUND_BIOACTIVITY grain and cannot be promoted to biosynthetic proof. |
| bgc-2713-classification-owner | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/2/owner_document/np_pathway; /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class | supports | Meroterpenoids/Tetraketide meroterpenoids is a computed classification compatible at a broad level with the phenolic ring and branched unsaturated side chain. Neither the model nor the MIBiG NRPS&#124;PKS label proves a four-ketide contribution, enzymatic route or natural identity. The saved forms contain no glycosidic candidate, consistent with the retained false prediction at this limited scope. Each record retains two computed pathway labels, so maintained choose_pathway files it UNCLASSIFIED while preserving both labels. This is consistent filing, not a claim of biological absence or an erased classification. |
| bgc-2713-owner-absence | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-target-input-plan-001.json; /records/2/declared_mechanism_roots_literal; /records/2/component_paths; /records/2/literal_bioactivities_root; /records/2/complete_root_keys | context_only | No selected mechanism root, component, molecular target or measured bioactivity array is present. Ilicicolin has a separately scoped coarse activity summary; negative roots do not establish inactivity. |
| bgc-2713-chemistry | /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnostic-DATA-001.json; /records/2/smiles/computed; /records/2/inchi/computed; /records/2/comparisons; /records/2/atom_correspondence; /records/2/literal_InChI_layers | supports | Both forms encode one aromatic six-membered ring, an aldehyde and two phenolic OH groups, with a branched unsaturated side chain. Two alkenes are specified E; the other side-chain double bond has equivalent methyl substituents at one end and is not an omitted stereogenic alkene. No amide, ester or sugar-ring candidate is returned. There are no tetrahedral centres and two specified E alkenes in both saved forms. The third side-chain alkene is nonstereogenic because one end has equivalent methyl groups. The stored true flag and literal alkene layers are retained; no natural stereochemical assignment was newly measured. C23H32O3, neutral charge, Standard InChI, full key and both canonical SMILES agree. The saved one-way chirality-aware match covers all 26 atoms, while full_graph_identity_established remains false. This bounded agreement does not adjudicate the retained Ilicicolin B versus LL-Z1272beta naming discussion or certify natural identity. |
| bgc-2713-molecular-reading | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-current272-first-five-molecular-intake-reading-001.json; /records/2; /scope; /warnings_scope | supports | Complete assigned saved tables and current intake input/ownership joins were read and retained; no new parse or primary-source-row credit. |
| bgc-2713-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted | supports | ROOT accepted the single original local diagnostic; acceptance is an execution/evidence gate rather than natural-identity certification. |
| bgc-2713-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnostic-execution-001.json; /command; /exit_code | supports | Exact original twenty-form diagnostic command and zero exit; command is reused only as a retained check description. |
| bgc-2713-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnostic-original-001.stderr; Complete original stderr, eight warnings | context_only | Four charge-rearrangement and four undefined-stereo messages remain globally unassigned, with no per-record attribution. |
| bgc-2713-intake | /private/tmp/npm-review-work/shared-next-batch272/intakes-001/2713-inspect-001.json; /targets; /source/inputs | supports | Exactly one selected target, 44 current captured inputs and the explicit maintained ownership declarations. |
| bgc-2713-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch272/root-intake-acceptance-001.json; /status; /accepted | supports | ROOT accepted ten canonical inspections with actual current input maps; this owner is one exact selected target. |
| bgc-2713-plan | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-target-input-plan-001.json; /records/2 | supports | Current accepted source scopes, direct companions and exact input paths for this owner. |
| bgc-2713-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch272/root-current272-source-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepted the original source plan after complete attributed retained-source reading. |
| bgc-2713-gates | /private/tmp/npm-review-work/shared-next-batch272/root-native-five-gates-acceptance-001.json; /all_five_commands_exit_zero; /unavailable_required_gates; /selected_queue_rows | context_only | Five local native checks passed; QC and OAK remain unavailable. Queue entries are leads, not independent scientific findings. |
| bgc-2713-source-reading | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-current272-assigned-source-reading-001.json; /contexts/6; /totals; /row_attribution | supports | Complete selected payloads and negative predicates have personally attributed reading; full input-file semantic coverage is not claimed. |
| bgc-2713-source-notes | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-scope-notes-001.json; /totals; /reading_reconciliation; /cautions | context_only | Complete batch source partition is 33 BGC plus 27 Support positive placements and zero Native primary credit; this review uses its own exact selected subset. |
| bgc-2713-taxonomy | /private/tmp/npm-review-work/shared-next-batch272-tentative/native-prep/native-current272-cached-taxonomy-reading-001.json; /scope; /routes; /context_interpretations; /interpretation | context_only | Retained cached names and exact ID routes were read; no missing/forward-merge/nonorganism match or fresh rank/strain verification is inferred. |
| bgc-2713-curation | /private/tmp/npm-review-work/shared-next-batch272-tentative/native-prep/native-current272-implemented-curation-scan-001.json; /scope; /counts; /exact_predicates; /applied_rows; /interpretation | context_only | Nine substantive tables give sixteen generic Streptomyces lexical hits but zero exact applicable predicates. Census-only extras are outside this scientific input scope. |
| bgc-2713-assay-curation | /private/tmp/npm-review-work/shared-next-batch272-tentative/native-prep/native-current272-implemented-curation-scan-001.json; /assay_scope | context_only | This selected owner has no actual AID or blank sentinel. The batch has zero actual AIDs and three blank sentinels in other contexts; neither absence nor exclusions demonstrate inactivity. |
| bgc-2713-stereo-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392-396: stereo_complete | context_only | Undefined source stereocentres are retained rather than invented. |
| bgc-2713-stereo-extractor | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters | context_only | The retained MIBiG flag uses unassigned atom-centred chirality. Reconstructed imidic-double geometry is a separate representation issue. |
| bgc-2713-filing-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306: choose_pathway | context_only | Each record retains two computed pathway labels, so maintained choose_pathway files it UNCLASSIFIED while preserving both labels. This is consistent filing, not a claim of biological absence or an erased classification. |
| bgc-2713-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/mibig_compounds | supports | All fields and the exact saved predicate of this mibig_compounds frame were read: 1 positive placements. Empty scope is bounded to these pinned retained tables. |
| bgc-2713-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 1682-1682; raw record sha256 a7acb651e777e58c8bcac22f07b1736870e9f0c5e24eb221b77af3bed8318345 | supports | All 25 fields of this exact retained physical row were personally read and joined. Citation and evidence grades remain literal database content. |
| bgc-2713-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_structures | supports | All fields and the exact saved predicate of this chebi_structures frame were read: 1 positive placements. Empty scope is bounded to these pinned retained tables. |
| bgc-2713-row-chebi_structures-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; physical lines 41737-41737; raw record sha256 31196233947a18f92baa2ec9eb18a16a51affdbaf2839659aba624c710964350 | supports | All 6 fields of this exact retained physical row were personally read and joined. Citation and evidence grades remain literal database content. |
| bgc-2713-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences | supports | All fields and the exact saved predicate of this lotus_occurrences frame were read: 2 positive placements. Empty scope is bounded to these pinned retained tables. |
| bgc-2713-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7167-7167; raw record sha256 5cd94ab49b95c03c62bf9278f4d757d9165de9155bd61e9d296a1aefc1b8758d | supports | All 6 fields of this exact retained physical row were personally read and joined. Citation and evidence grades remain literal database content. |
| bgc-2713-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7168-7168; raw record sha256 7e0bd24558e5c6dd843d1dfce76ad5494229890d31e919f1cdcdf6313e22a16e | supports | All 6 fields of this exact retained physical row were personally read and joined. Citation and evidence grades remain literal database content. |
| bgc-2713-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences | context_only | All fields and the exact saved predicate of this cyanometdb_occurrences frame were read: 0 positive placements. Empty scope is bounded to these pinned retained tables. |
| bgc-2713-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/npclassifier | supports | All fields and the exact saved predicate of this npclassifier frame were read: 1 positive placements. Empty scope is bounded to these pinned retained tables. |
| bgc-2713-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 1959-1959; raw record sha256 16c4ce0bc2d2cf70071393bccd8df3989d165b53f00a2ad373e3a57d800870bf | supports | All 7 fields of this exact retained physical row were personally read and joined. Citation and evidence grades remain literal database content. |
| bgc-2713-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/pubchem_bioassay | context_only | All fields and the exact saved predicate of this pubchem_bioassay frame were read: 0 positive placements. Empty scope is bounded to these pinned retained tables. |
| bgc-2713-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/bindingdb_targets | context_only | All fields and the exact saved predicate of this bindingdb_targets frame were read: 0 positive placements. Empty scope is bounded to these pinned retained tables. |
| bgc-2713-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys | supports | All fields and the exact saved predicate of this antibioticmech_inchikeys frame were read: 1 positive placements. Empty scope is bounded to these pinned retained tables. |
| bgc-2713-row-antibioticmech_inchikeys-0 | /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv; physical lines 1789-1789; raw record sha256 006e282fb7ad7a728a559db35a6cfbef7215c91f9d4ee5aa8a0017cac6cd4d29 | supports | All 6 fields of this exact retained physical row were personally read and joined. Citation and evidence grades remain literal database content. |
| bgc-2713-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins | context_only | All fields and the exact saved predicate of this chebi_origins frame were read: 0 positive placements. Empty scope is bounded to these pinned retained tables. |
| bgc-2713-open-discussion | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/2/owner_document/discussions | context_only | The existing OPEN Ilicicolin B versus LL-Z1272beta name disagreement remains unresolved. |
| bgc-2713-coarse-activity | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/2/owner_document/bioactivity_summary; /records/2/owner_document/related_records | context_only | ANTIMICROBIAL_UNSPECIFIED and exact-key AntibioticMech link are retained coarse annotations, not a measured target or mechanism. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-272/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-272/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-272/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-272/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-272/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Only current retained source content and saved local outputs were reviewed. Primary papers, fresh authority/taxonomy lookups, full QC and OAK are unavailable; source producer assertions and CLUSTER_UNSTATED loci are not upgraded to experimental proof.
- C23H32O3, neutral charge, Standard InChI, full key and both canonical SMILES agree. The saved one-way chirality-aware match covers all 26 atoms, while full_graph_identity_established remains false. This bounded agreement does not adjudicate the retained Ilicicolin B versus LL-Z1272beta naming discussion or certify natural identity.
- All eight original diagnostic warnings (four charge-rearrangement and four undefined-stereo messages) remain globally unassigned. Neither warning type is attributed to this owner. Full graph identity remains unestablished, including when a limited map is complete.
- The pre-existing OPEN Ilicicolin B/LL-Z1272beta naming discussion remains unresolved; no replacement identifier, merge or source correction is chosen.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- All atom indices are local to their saved form. No new molecule parse, alternate input, maintained reader, query replay or outbound request occurred in this authoring lane.
- Whole-owner and selected source-payload reading is distinct from input-file digest/ownership verification. Source primary-row attribution is 18 selected placements/208 fields, within the separately retained 33-row assigned reading.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T133430Z-ilicicolin-b
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: ilicicolin B'
started_at: '2026-11-06T12:38:14.164535Z'
finished_at: '2026-11-06T13:34:30.932191Z'
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
summary: Ilicicolin B has matching stored-form canonical strings and an exact retained
  ChEBI target, while the OPEN LL-Z1272beta naming discussion remains unresolved.
  Coarse antimicrobial and occurrence evidence are retained without assay or mechanism
  transfer.
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
  - path: data/natural_products/unclassified/ilicicolin-b.yaml
    sha256: 3cf920015b9fdf4028b96d44d0f80722653c440db9f8317ffc8ed84112cc9ded
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
  selection: Campaign path order 2713; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:146153
targets:
- target_id: CHEBI:146153
  path: data/natural_products/unclassified/ilicicolin-b.yaml
  label: ilicicolin B
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
    path: data/raw/chebi_structures.tsv
    role: Retained ChEBI identifiers, definitions and exact chemical forms.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Retained cited occurrence assertions, distinct from demonstrated production.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned full-key AntibioticMech structure links and coarse activity summaries;
      no transfer of mechanism.
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnose272-001.py
    0cb2578b19e493e9249755546918ab75743c353b19d38062e893ebab5314f402 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
    511c5c899beeb5cde2fdff1e9d7148a34c04f2076e2e2e674b19adbcf1da5db7
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed in the original twenty-attempt execution; within-owner
    formula, charge, Standard InChI and complete key agree.
  scope_note: C23H32O3, neutral charge, Standard InChI, full key and both canonical
    SMILES agree. The saved one-way chirality-aware match covers all 26 atoms, while
    full_graph_identity_established remains false. This bounded agreement does not
    adjudicate the retained Ilicicolin B versus LL-Z1272beta naming discussion or
    certify natural identity. Eight original warnings remain globally unassigned.
    This check provides no natural-identity, primary biological or full graph certification.
  target_ids:
  - CHEBI:146153
  evidence_ids:
  - bgc-2713-chemistry
  - bgc-2713-diagnostic-acceptance
  - bgc-2713-diagnostic-execution
  - bgc-2713-diagnostic-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:146153
  command: just validate-strict data/natural_products/unclassified/ilamycin-c1.yaml
    data/natural_products/unclassified/ilamycin-c2.yaml data/natural_products/unclassified/ilicicolin-b.yaml
    data/natural_products/unclassified/incarnatapeptin-b.yaml data/natural_products/unclassified/incednine.yaml
    data/natural_products/unclassified/irciniastatin-b.yaml data/natural_products/unclassified/isoterrein.yaml
    data/natural_products/unclassified/jagaricin.yaml data/natural_products/unclassified/jamaicamide-a.yaml
    data/natural_products/unclassified/jamaicamide-b.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-272/validate-strict-selected10-001.tsv
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
  - CHEBI:146153
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-272/validate-all-001.tsv
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
  - CHEBI:146153
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
  - CHEBI:146153
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
  - CHEBI:146153
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-272/review-queue-001.tsv
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
  - CHEBI:146153
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:146153
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:146153
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2713-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/ilicicolin-b.yaml
  locator: Complete plaintext and all curation_history entries
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: Whole current owner/history personally read; generated source assertions
    remain distinct from fresh primary evidence.
  snapshot_sha256: 3cf920015b9fdf4028b96d44d0f80722653c440db9f8317ffc8ed84112cc9ded
- evidence_id: bgc-2713-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/2/owner_document/identifier; /records/2/owner_document/chemical_structure;
    /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: CHEBI:146153 is the exact selected target with QAPOXOGEDXIOHD-VZRGJMDUSA-N.
    Retained ChEBI 3-star and MIBiG BGC0001390 compound1 source concepts share this
    full key but name it Ilicicolin B and LL-Z1272beta respectively. The existing
    OPEN name-disagreement remains explicit; matching local canonical strings do not
    decide synonymy or which source name is correct.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: bgc-2713-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/2/owner_document/curation_history
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: DOI:10.1016/j.bbabio.2008.11.016 / COMPOUND_BIOACTIVITY; all 2 complete
    history events are seeder-attributed provenance, not fresh primary reading. Citation
    presence does not imply that the underlying article was newly read.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: bgc-2713-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: MIBiG entry3 is active/questionable/unknown, SOURCE_ASSERTION for Stachybotrys
    bisbyi80385, with NRPS|PKS and Type I|Unknown, genome LC125467.1 but blank locus
    bounds/methods and CLUSTER_UNSTATED. DOI:10.1016/j.bbabio.2008.11.016 is COMPOUND_BIOACTIVITY
    grain and cannot be promoted to biosynthetic proof.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: bgc-2713-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_pathway; /records/2/owner_document/np_classification;
    /records/2/owner_document/bgc_class
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: Meroterpenoids/Tetraketide meroterpenoids is a computed classification
    compatible at a broad level with the phenolic ring and branched unsaturated side
    chain. Neither the model nor the MIBiG NRPS|PKS label proves a four-ketide contribution,
    enzymatic route or natural identity. The saved forms contain no glycosidic candidate,
    consistent with the retained false prediction at this limited scope. Each record
    retains two computed pathway labels, so maintained choose_pathway files it UNCLASSIFIED
    while preserving both labels. This is consistent filing, not a claim of biological
    absence or an erased classification.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: bgc-2713-owner-absence
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-target-input-plan-001.json
  locator: /records/2/declared_mechanism_roots_literal; /records/2/component_paths;
    /records/2/literal_bioactivities_root; /records/2/complete_root_keys
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: No selected mechanism root, component, molecular target or measured bioactivity
    array is present. Ilicicolin has a separately scoped coarse activity summary;
    negative roots do not establish inactivity.
  snapshot_sha256: 88b8e4da369b51ff7ba70fbd6c6f9e584601e9c106daee1c3e8eba2406851cb3
  search_scope: Complete captured owner root set and exact current plan literal scopes;
    no name-based or companion mechanism transfer.
- evidence_id: bgc-2713-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/smiles/computed; /records/2/inchi/computed; /records/2/comparisons;
    /records/2/atom_correspondence; /records/2/literal_InChI_layers
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: Both forms encode one aromatic six-membered ring, an aldehyde and two phenolic
    OH groups, with a branched unsaturated side chain. Two alkenes are specified E;
    the other side-chain double bond has equivalent methyl substituents at one end
    and is not an omitted stereogenic alkene. No amide, ester or sugar-ring candidate
    is returned. There are no tetrahedral centres and two specified E alkenes in both
    saved forms. The third side-chain alkene is nonstereogenic because one end has
    equivalent methyl groups. The stored true flag and literal alkene layers are retained;
    no natural stereochemical assignment was newly measured. C23H32O3, neutral charge,
    Standard InChI, full key and both canonical SMILES agree. The saved one-way chirality-aware
    match covers all 26 atoms, while full_graph_identity_established remains false.
    This bounded agreement does not adjudicate the retained Ilicicolin B versus LL-Z1272beta
    naming discussion or certify natural identity.
  snapshot_sha256: bb91cc8d0e213bdc89d27c74eeb34cebef9d7b2b0d18bfe8a1f48e201f497c8e
- evidence_id: bgc-2713-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-current272-first-five-molecular-intake-reading-001.json
  locator: /records/2; /scope; /warnings_scope
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: Complete assigned saved tables and current intake input/ownership joins
    were read and retained; no new parse or primary-source-row credit.
  snapshot_sha256: aa1405a45bcf67bea271ea7e88a9e0941b7ceb53c0eeb004787a96f2340457e6
- evidence_id: bgc-2713-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: ROOT accepted the single original local diagnostic; acceptance is an execution/evidence
    gate rather than natural-identity certification.
  snapshot_sha256: 1aa9f9ca7b5c5f3293ef344dc9e2ebf8987395ceebf7c1142c413afedf44f380
- evidence_id: bgc-2713-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: Exact original twenty-form diagnostic command and zero exit; command is
    reused only as a retained check description.
  snapshot_sha256: 335d822411906e6b33c46d5a94157b9e76fbfd92034a04ac911ac138e38cfc69
- evidence_id: bgc-2713-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr, eight warnings
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: Four charge-rearrangement and four undefined-stereo messages remain globally
    unassigned, with no per-record attribution.
  snapshot_sha256: a967bebdd9388142e1fac938e16e322d2671b8d87e2afb650155976176f65125
- evidence_id: bgc-2713-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/intakes-001/2713-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: Exactly one selected target, 44 current captured inputs and the explicit
    maintained ownership declarations.
  snapshot_sha256: f872f07227888fc7c1fba188eb8eac23f7dc062ee5902ca5e56bf43fa3deedc2
- evidence_id: bgc-2713-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/root-intake-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: ROOT accepted ten canonical inspections with actual current input maps;
    this owner is one exact selected target.
  snapshot_sha256: 801e9a99db5b2826fd4355b9527ff19648873390bf43fa1224336bfb8a0ffabe
- evidence_id: bgc-2713-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-target-input-plan-001.json
  locator: /records/2
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: Current accepted source scopes, direct companions and exact input paths
    for this owner.
  snapshot_sha256: 88b8e4da369b51ff7ba70fbd6c6f9e584601e9c106daee1c3e8eba2406851cb3
- evidence_id: bgc-2713-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/root-current272-source-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: ROOT accepted the original source plan after complete attributed retained-source
    reading.
  snapshot_sha256: d81d9507e202fa0c3eac7c74f2bb61aad22a3d42a95091cf47d4da887823aa33
- evidence_id: bgc-2713-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/root-native-five-gates-acceptance-001.json
  locator: /all_five_commands_exit_zero; /unavailable_required_gates; /selected_queue_rows
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: Five local native checks passed; QC and OAK remain unavailable. Queue entries
    are leads, not independent scientific findings.
  snapshot_sha256: 7f601817efeea14be333affd31eb25acaf490f1f4449a89d71c78d6bd018cfa0
- evidence_id: bgc-2713-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-current272-assigned-source-reading-001.json
  locator: /contexts/6; /totals; /row_attribution
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: Complete selected payloads and negative predicates have personally attributed
    reading; full input-file semantic coverage is not claimed.
  snapshot_sha256: dbbc72aedb0e8690124bda067c2d8885d084a45ab56f2f51b62db73e4d1afba6
- evidence_id: bgc-2713-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /cautions
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: Complete batch source partition is 33 BGC plus 27 Support positive placements
    and zero Native primary credit; this review uses its own exact selected subset.
  snapshot_sha256: 3fbbc507013f5e09915ebbab660ac6757a56b402499ab2187ec384c9aa010b4e
- evidence_id: bgc-2713-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/native-prep/native-current272-cached-taxonomy-reading-001.json
  locator: /scope; /routes; /context_interpretations; /interpretation
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: Retained cached names and exact ID routes were read; no missing/forward-merge/nonorganism
    match or fresh rank/strain verification is inferred.
  snapshot_sha256: a8b0ac542d9758a6e7205450e57e04968f18e69dd61358f5b16716c06e410435
  search_scope: Current sixteen cached stanzas and exact saved context routes; retained
    cache only, no OAK or live taxonomy request.
- evidence_id: bgc-2713-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/native-prep/native-current272-implemented-curation-scan-001.json
  locator: /scope; /counts; /exact_predicates; /applied_rows; /interpretation
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: Nine substantive tables give sixteen generic Streptomyces lexical hits
    but zero exact applicable predicates. Census-only extras are outside this scientific
    input scope.
  snapshot_sha256: b9aaad338ba894d766d71c50336f9cf0056fdf4a6bb5f26a2b2ca188cf906bfe
  search_scope: Nine retained substantive tables/3422 rows, all sixteen complete candidate
    payloads and six exact identity predicates, without applying any decision.
- evidence_id: bgc-2713-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/native-prep/native-current272-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: This selected owner has no actual AID or blank sentinel. The batch has
    zero actual AIDs and three blank sentinels in other contexts; neither absence
    nor exclusions demonstrate inactivity.
  snapshot_sha256: b9aaad338ba894d766d71c50336f9cf0056fdf4a6bb5f26a2b2ca188cf906bfe
  search_scope: Actual saved exact-key/CID/AID routes and fifteen retained exclusion
    decisions; no assay transfer from siblings or blank identifiers.
- evidence_id: bgc-2713-stereo-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: 'lines 392-396: stereo_complete'
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: Undefined source stereocentres are retained rather than invented.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2713-stereo-extractor
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters'
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: The retained MIBiG flag uses unassigned atom-centred chirality. Reconstructed
    imidic-double geometry is a separate representation issue.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2713-filing-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines 295-306: choose_pathway'
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: Each record retains two computed pathway labels, so maintained choose_pathway
    files it UNCLASSIFIED while preserving both labels. This is consistent filing,
    not a claim of biological absence or an erased classification.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2713-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: 'All fields and the exact saved predicate of this mibig_compounds frame
    were read: 1 positive placements. Empty scope is bounded to these pinned retained
    tables.'
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
- evidence_id: bgc-2713-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 1682-1682; raw record sha256 a7acb651e777e58c8bcac22f07b1736870e9f0c5e24eb221b77af3bed8318345
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: All 25 fields of this exact retained physical row were personally read
    and joined. Citation and evidence grades remain literal database content.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2713-query-chebi_structures
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: 'All fields and the exact saved predicate of this chebi_structures frame
    were read: 1 positive placements. Empty scope is bounded to these pinned retained
    tables.'
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
- evidence_id: bgc-2713-row-chebi_structures-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: physical lines 41737-41737; raw record sha256 31196233947a18f92baa2ec9eb18a16a51affdbaf2839659aba624c710964350
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: All 6 fields of this exact retained physical row were personally read and
    joined. Citation and evidence grades remain literal database content.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2713-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: 'All fields and the exact saved predicate of this lotus_occurrences frame
    were read: 2 positive placements. Empty scope is bounded to these pinned retained
    tables.'
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
- evidence_id: bgc-2713-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7167-7167; raw record sha256 5cd94ab49b95c03c62bf9278f4d757d9165de9155bd61e9d296a1aefc1b8758d
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: All 6 fields of this exact retained physical row were personally read and
    joined. Citation and evidence grades remain literal database content.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2713-row-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7168-7168; raw record sha256 7e0bd24558e5c6dd843d1dfce76ad5494229890d31e919f1cdcdf6313e22a16e
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: All 6 fields of this exact retained physical row were personally read and
    joined. Citation and evidence grades remain literal database content.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2713-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: 'All fields and the exact saved predicate of this cyanometdb_occurrences
    frame were read: 0 positive placements. Empty scope is bounded to these pinned
    retained tables.'
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"owner": "data/natural_products/unclassified/ilicicolin-b.yaml",
    "table": "cyanometdb_occurrences", "predicate": "exact complete standard_inchi_key
    equality", "query": "QAPOXOGEDXIOHD-VZRGJMDUSA-N", "matches": 0}'
- evidence_id: bgc-2713-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: 'All fields and the exact saved predicate of this npclassifier frame were
    read: 1 positive placements. Empty scope is bounded to these pinned retained tables.'
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
- evidence_id: bgc-2713-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 1959-1959; raw record sha256 16c4ce0bc2d2cf70071393bccd8df3989d165b53f00a2ad373e3a57d800870bf
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: All 7 fields of this exact retained physical row were personally read and
    joined. Citation and evidence grades remain literal database content.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2713-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: 'All fields and the exact saved predicate of this pubchem_bioassay frame
    were read: 0 positive placements. Empty scope is bounded to these pinned retained
    tables.'
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"owner": "data/natural_products/unclassified/ilicicolin-b.yaml",
    "table": "pubchem_bioassay", "predicate": "exact complete standard_inchi_key equality",
    "query": "QAPOXOGEDXIOHD-VZRGJMDUSA-N", "matches": 0}'
- evidence_id: bgc-2713-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: 'All fields and the exact saved predicate of this bindingdb_targets frame
    were read: 0 positive placements. Empty scope is bounded to these pinned retained
    tables.'
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"owner": "data/natural_products/unclassified/ilicicolin-b.yaml",
    "table": "bindingdb_targets", "predicate": "exact complete standard_inchi_key
    equality", "query": "QAPOXOGEDXIOHD-VZRGJMDUSA-N", "matches": 0}'
- evidence_id: bgc-2713-query-antibioticmech_inchikeys
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: 'All fields and the exact saved predicate of this antibioticmech_inchikeys
    frame were read: 1 positive placements. Empty scope is bounded to these pinned
    retained tables.'
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
- evidence_id: bgc-2713-row-antibioticmech_inchikeys-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv
  locator: physical lines 1789-1789; raw record sha256 006e282fb7ad7a728a559db35a6cfbef7215c91f9d4ee5aa8a0017cac6cd4d29
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: supports
  summary: All 6 fields of this exact retained physical row were personally read and
    joined. Citation and evidence grades remain literal database content.
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
- evidence_id: bgc-2713-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: 'All fields and the exact saved predicate of this chebi_origins frame were
    read: 0 positive placements. Empty scope is bounded to these pinned retained tables.'
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"owner": "data/natural_products/unclassified/ilicicolin-b.yaml",
    "table": "chebi_origins", "predicate": "exact chebi_id from exact full-key structure
    rows", "query": ["CHEBI:146153"], "matches": 0}'
- evidence_id: bgc-2713-open-discussion
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/2/owner_document/discussions
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: The existing OPEN Ilicicolin B versus LL-Z1272beta name disagreement remains
    unresolved.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: bgc-2713-coarse-activity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/2/owner_document/bioactivity_summary; /records/2/owner_document/related_records
  accessed_at: '2026-11-06T13:19:29.839223Z'
  support: context_only
  summary: ANTIMICROBIAL_UNSPECIFIED and exact-key AntibioticMech link are retained
    coarse annotations, not a measured target or mechanism.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-272/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json
  accessed_at: '2026-11-06T12:48:19.529888Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: fd0cb34130c3476f25db169b5325777ebb89e90a074ab9e1f366e3f2457ccedd
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-272/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json
  accessed_at: '2026-11-06T12:48:43.420906Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: c1d32476a8c22a015b77eee75bb463a26856281054e90ab736ad3a6daa2ddb31
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-272/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json
  accessed_at: '2026-11-06T12:49:02.369675Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-272/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json
  accessed_at: '2026-11-06T12:49:35.366970Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-272/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json
  accessed_at: '2026-11-06T12:49:46.753813Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: bbd68fc20f1f48e4ea8a6a703a235b662c04e17f7a9e47c3fcef4bc064c02e09
assessments:
- assessment_id: bgc-2713-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: CHEBI:146153 is the exact selected target with QAPOXOGEDXIOHD-VZRGJMDUSA-N.
    Retained ChEBI 3-star and MIBiG BGC0001390 compound1 source concepts share this
    full key but name it Ilicicolin B and LL-Z1272beta respectively. The existing
    OPEN name-disagreement remains explicit; matching local canonical strings do not
    decide synonymy or which source name is correct.
  target_ids:
  - CHEBI:146153
  evidence_ids:
  - bgc-2713-identity
  - bgc-2713-chemistry
  - bgc-2713-query-mibig_compounds
  - bgc-2713-query-chebi_structures
  - bgc-2713-plan
  - bgc-2713-row-mibig_compounds-0
  - bgc-2713-row-chebi_structures-0
  - bgc-2713-open-discussion
  dimensions:
  - name: standard_inchi_key
    value: QAPOXOGEDXIOHD-VZRGJMDUSA-N
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    evidence_ids:
    - bgc-2713-identity
    - bgc-2713-chemistry
    - bgc-2713-query-mibig_compounds
    - bgc-2713-query-chebi_structures
    - bgc-2713-plan
    - bgc-2713-row-mibig_compounds-0
    - bgc-2713-row-chebi_structures-0
    - bgc-2713-open-discussion
  - name: grounding_scope
    value: CHEBI:146153 is the exact selected target with QAPOXOGEDXIOHD-VZRGJMDUSA-N.
      Retained ChEBI 3-star and MIBiG BGC0001390 compound1 source concepts share this
      full key but name it Ilicicolin B and LL-Z1272beta respectively. The existing
      OPEN name-disagreement remains explicit; matching local canonical strings do
      not decide synonymy or which source name is correct.
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    evidence_ids:
    - bgc-2713-identity
    - bgc-2713-chemistry
    - bgc-2713-query-mibig_compounds
    - bgc-2713-query-chebi_structures
    - bgc-2713-plan
    - bgc-2713-row-mibig_compounds-0
    - bgc-2713-row-chebi_structures-0
    - bgc-2713-open-discussion
- assessment_id: bgc-2713-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: Both forms encode one aromatic six-membered ring, an aldehyde and two phenolic
    OH groups, with a branched unsaturated side chain. Two alkenes are specified E;
    the other side-chain double bond has equivalent methyl substituents at one end
    and is not an omitted stereogenic alkene. No amide, ester or sugar-ring candidate
    is returned. There are no tetrahedral centres and two specified E alkenes in both
    saved forms. The third side-chain alkene is nonstereogenic because one end has
    equivalent methyl groups. The stored true flag and literal alkene layers are retained;
    no natural stereochemical assignment was newly measured. C23H32O3, neutral charge,
    Standard InChI, full key and both canonical SMILES agree. The saved one-way chirality-aware
    match covers all 26 atoms, while full_graph_identity_established remains false.
    This bounded agreement does not adjudicate the retained Ilicicolin B versus LL-Z1272beta
    naming discussion or certify natural identity.
  target_ids:
  - CHEBI:146153
  evidence_ids:
  - bgc-2713-identity
  - bgc-2713-chemistry
  - bgc-2713-molecular-reading
  - bgc-2713-diagnostic-acceptance
  - bgc-2713-diagnostic-stderr
  - bgc-2713-stereo-schema
  - bgc-2713-stereo-extractor
  dimensions:
  - name: stereochemistry_scope
    value: There are no tetrahedral centres and two specified E alkenes in both saved
      forms. The third side-chain alkene is nonstereogenic because one end has equivalent
      methyl groups. The stored true flag and literal alkene layers are retained;
      no natural stereochemical assignment was newly measured.
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    evidence_ids:
    - bgc-2713-identity
    - bgc-2713-chemistry
    - bgc-2713-molecular-reading
    - bgc-2713-diagnostic-acceptance
    - bgc-2713-diagnostic-stderr
    - bgc-2713-stereo-schema
    - bgc-2713-stereo-extractor
  - name: representation_correspondence
    value: C23H32O3, neutral charge, Standard InChI, full key and both canonical SMILES
      agree. The saved one-way chirality-aware match covers all 26 atoms, while full_graph_identity_established
      remains false. This bounded agreement does not adjudicate the retained Ilicicolin
      B versus LL-Z1272beta naming discussion or certify natural identity.
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    evidence_ids:
    - bgc-2713-identity
    - bgc-2713-chemistry
    - bgc-2713-molecular-reading
    - bgc-2713-diagnostic-acceptance
    - bgc-2713-diagnostic-stderr
    - bgc-2713-stereo-schema
    - bgc-2713-stereo-extractor
- assessment_id: bgc-2713-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: MIBiG entry3 is active/questionable/unknown, SOURCE_ASSERTION for Stachybotrys
    bisbyi80385, with NRPS|PKS and Type I|Unknown, genome LC125467.1 but blank locus
    bounds/methods and CLUSTER_UNSTATED. DOI:10.1016/j.bbabio.2008.11.016 is COMPOUND_BIOACTIVITY
    grain and cannot be promoted to biosynthetic proof.
  target_ids:
  - CHEBI:146153
  evidence_ids:
  - bgc-2713-provenance
  - bgc-2713-query-mibig_compounds
  - bgc-2713-taxonomy
  - bgc-2713-curation
  - bgc-2713-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    value: Source producer Stachybotrys bisbyi NCBITaxon:80385; separate LOTUS occurrences
      Albatrellus ovinus NCBITaxon:139090 and Neonectria coccinea NCBITaxon:57153.
      These occurrence taxa are not transferred to the producer claim.
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    evidence_ids:
    - bgc-2713-provenance
    - bgc-2713-query-mibig_compounds
    - bgc-2713-taxonomy
    - bgc-2713-curation
    - bgc-2713-row-mibig_compounds-0
  - name: producer_evidence
    value: 'Stachybotrys bisbyi (NCBITaxon:80385): SOURCE_ASSERTION'
    definition: Producer evidence grade and its demonstrated or asserted scope.
    evidence_ids:
    - bgc-2713-provenance
    - bgc-2713-query-mibig_compounds
    - bgc-2713-taxonomy
    - bgc-2713-curation
    - bgc-2713-row-mibig_compounds-0
  - name: locus_evidence
    value: '{"mibig_accession": "BGC0001390", "entry_version": "3", "entry_status":
      "active", "entry_quality": "questionable", "entry_completeness": "unknown",
      "genome_accession": "LC125467.1", "locus_from": "", "locus_to": "", "locus_evidence_methods":
      "", "cluster_link_evidence_basis": "CLUSTER_UNSTATED"}'
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    evidence_ids:
    - bgc-2713-provenance
    - bgc-2713-query-mibig_compounds
    - bgc-2713-taxonomy
    - bgc-2713-curation
    - bgc-2713-row-mibig_compounds-0
- assessment_id: bgc-2713-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: DOI:10.1016/j.bbabio.2008.11.016 / COMPOUND_BIOACTIVITY; all 2 complete
    history events are seeder-attributed provenance, not fresh primary reading. Citation
    presence does not imply that the underlying article was newly read.
  target_ids:
  - CHEBI:146153
  evidence_ids:
  - bgc-2713-provenance
  - bgc-2713-history
  - bgc-2713-source-reading
  - bgc-2713-query-mibig_compounds
  - bgc-2713-row-mibig_compounds-0
  dimensions:
  - name: citation_scope
    value: DOI:10.1016/j.bbabio.2008.11.016 / COMPOUND_BIOACTIVITY; all 2 complete
      history events are seeder-attributed provenance, not fresh primary reading.
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    evidence_ids:
    - bgc-2713-provenance
    - bgc-2713-history
    - bgc-2713-source-reading
    - bgc-2713-query-mibig_compounds
    - bgc-2713-row-mibig_compounds-0
- assessment_id: bgc-2713-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: 'Two exact-key LOTUS rows: Albatrellus ovinus/139090 with DOI:10.1016/S0223-5234(97)89088-5
    and Neonectria coccinea/57153 with DOI:10.1039/P19720002136. Their distinct occurrence
    claims do not establish the MIBiG producer or biosynthesis. The exact-key AntibioticMech
    CHEBI:146153 link retains ANTIMICROBIAL_UNSPECIFIED from the pinned sibling inventory.
    This coarse summary is not an AID, target, affinity or demonstrated mechanism.
    No current AID, blank sentinel or BindingDB row matches; the related-corpus projection
    is not an extra independent measurement.'
  target_ids:
  - CHEBI:146153
  evidence_ids:
  - bgc-2713-owner-absence
  - bgc-2713-query-lotus_occurrences
  - bgc-2713-query-cyanometdb_occurrences
  - bgc-2713-query-pubchem_bioassay
  - bgc-2713-query-bindingdb_targets
  - bgc-2713-query-antibioticmech_inchikeys
  - bgc-2713-assay-curation
  - bgc-2713-row-lotus_occurrences-0
  - bgc-2713-row-lotus_occurrences-1
  - bgc-2713-row-antibioticmech_inchikeys-0
  - bgc-2713-coarse-activity
  dimensions:
  - name: occurrence_scope
    value: 'Two exact-key LOTUS rows: Albatrellus ovinus/139090 with DOI:10.1016/S0223-5234(97)89088-5
      and Neonectria coccinea/57153 with DOI:10.1039/P19720002136. Their distinct
      occurrence claims do not establish the MIBiG producer or biosynthesis.'
    definition: Exact retained occurrence tuples and limits on production/independence.
    evidence_ids:
    - bgc-2713-owner-absence
    - bgc-2713-query-lotus_occurrences
    - bgc-2713-query-cyanometdb_occurrences
    - bgc-2713-query-pubchem_bioassay
    - bgc-2713-query-bindingdb_targets
    - bgc-2713-query-antibioticmech_inchikeys
    - bgc-2713-assay-curation
    - bgc-2713-row-lotus_occurrences-0
    - bgc-2713-row-lotus_occurrences-1
    - bgc-2713-row-antibioticmech_inchikeys-0
    - bgc-2713-coarse-activity
  - name: assay_target_scope
    value: The exact-key AntibioticMech CHEBI:146153 link retains ANTIMICROBIAL_UNSPECIFIED
      from the pinned sibling inventory. This coarse summary is not an AID, target,
      affinity or demonstrated mechanism. No current AID, blank sentinel or BindingDB
      row matches; the related-corpus projection is not an extra independent measurement.
    definition: Retained activity/assay/target positives and bounded negative queries.
    evidence_ids:
    - bgc-2713-owner-absence
    - bgc-2713-query-lotus_occurrences
    - bgc-2713-query-cyanometdb_occurrences
    - bgc-2713-query-pubchem_bioassay
    - bgc-2713-query-bindingdb_targets
    - bgc-2713-query-antibioticmech_inchikeys
    - bgc-2713-assay-curation
    - bgc-2713-row-lotus_occurrences-0
    - bgc-2713-row-lotus_occurrences-1
    - bgc-2713-row-antibioticmech_inchikeys-0
    - bgc-2713-coarse-activity
- assessment_id: bgc-2713-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: Meroterpenoids/Tetraketide meroterpenoids is a computed classification
    compatible at a broad level with the phenolic ring and branched unsaturated side
    chain. Neither the model nor the MIBiG NRPS|PKS label proves a four-ketide contribution,
    enzymatic route or natural identity. The saved forms contain no glycosidic candidate,
    consistent with the retained false prediction at this limited scope. Each record
    retains two computed pathway labels, so maintained choose_pathway files it UNCLASSIFIED
    while preserving both labels. This is consistent filing, not a claim of biological
    absence or an erased classification.
  target_ids:
  - CHEBI:146153
  evidence_ids:
  - bgc-2713-classification-owner
  - bgc-2713-chemistry
  - bgc-2713-query-npclassifier
  - bgc-2713-query-mibig_compounds
  - bgc-2713-filing-seeder
  - bgc-2713-row-npclassifier-0
  - bgc-2713-row-mibig_compounds-0
  dimensions:
  - name: classification_applicability
    value: Meroterpenoids/Tetraketide meroterpenoids is a computed classification
      compatible at a broad level with the phenolic ring and branched unsaturated
      side chain. Neither the model nor the MIBiG NRPS|PKS label proves a four-ketide
      contribution, enzymatic route or natural identity. The saved forms contain no
      glycosidic candidate, consistent with the retained false prediction at this
      limited scope. Each record retains two computed pathway labels, so maintained
      choose_pathway files it UNCLASSIFIED while preserving both labels. This is consistent
      filing, not a claim of biological absence or an erased classification.
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    evidence_ids:
    - bgc-2713-classification-owner
    - bgc-2713-chemistry
    - bgc-2713-query-npclassifier
    - bgc-2713-query-mibig_compounds
    - bgc-2713-filing-seeder
    - bgc-2713-row-npclassifier-0
    - bgc-2713-row-mibig_compounds-0
- assessment_id: bgc-2713-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: supported
  summary: Complete owner/history, all nine saved query frames (6 positive placements/56
    fields) and both complete saved molecular forms were personally read. The 44 actual
    input hashes and ownership declarations were verified; this does not claim semantic
    reading of entire corpus input files. Required native local gates passed; full
    QC, OAK, live authority and primary-paper verification are unavailable. No selected
    mechanism root or component requires a maintained reader. Corrections belong in
    maintained inputs/extractors or the seeder; no record edit is proposed.
  target_ids:
  - CHEBI:146153
  evidence_ids:
  - bgc-2713-owner
  - bgc-2713-history
  - bgc-2713-intake
  - bgc-2713-intake-acceptance
  - bgc-2713-plan
  - bgc-2713-plan-acceptance
  - bgc-2713-gates
  - bgc-2713-source-reading
  - bgc-2713-source-notes
  - bgc-2713-molecular-reading
  - bgc-2713-owner-absence
  dimensions:
  - name: review_completion
    value: Complete owner/history, all nine saved query frames (6 positive placements/56
      fields) and both complete saved molecular forms were personally read. The 44
      actual input hashes and ownership declarations were verified; this does not
      claim semantic reading of entire corpus input files. Required native local gates
      passed; full QC, OAK, live authority and primary-paper verification are unavailable.
      No selected mechanism root or component requires a maintained reader. Corrections
      belong in maintained inputs/extractors or the seeder; no record edit is proposed.
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    evidence_ids:
    - bgc-2713-owner
    - bgc-2713-history
    - bgc-2713-intake
    - bgc-2713-intake-acceptance
    - bgc-2713-plan
    - bgc-2713-plan-acceptance
    - bgc-2713-gates
    - bgc-2713-source-reading
    - bgc-2713-source-notes
    - bgc-2713-molecular-reading
    - bgc-2713-owner-absence
findings: []
actions: []
limitations:
- Only current retained source content and saved local outputs were reviewed. Primary
  papers, fresh authority/taxonomy lookups, full QC and OAK are unavailable; source
  producer assertions and CLUSTER_UNSTATED loci are not upgraded to experimental proof.
- C23H32O3, neutral charge, Standard InChI, full key and both canonical SMILES agree.
  The saved one-way chirality-aware match covers all 26 atoms, while full_graph_identity_established
  remains false. This bounded agreement does not adjudicate the retained Ilicicolin
  B versus LL-Z1272beta naming discussion or certify natural identity.
- All eight original diagnostic warnings (four charge-rearrangement and four undefined-stereo
  messages) remain globally unassigned. Neither warning type is attributed to this
  owner. Full graph identity remains unestablished, including when a limited map is
  complete.
- The pre-existing OPEN Ilicicolin B/LL-Z1272beta naming discussion remains unresolved;
  no replacement identifier, merge or source correction is chosen.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- All atom indices are local to their saved form. No new molecule parse, alternate
  input, maintained reader, query replay or outbound request occurred in this authoring
  lane.
- Whole-owner and selected source-payload reading is distinct from input-file digest/ownership
  verification. Source primary-row attribution is 18 selected placements/208 fields,
  within the separately retained 33-row assigned reading.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-272
```
