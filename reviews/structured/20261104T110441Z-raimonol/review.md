# Local evidence review: raimonol

- Review: 20261104T110441Z-raimonol
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T10:10:44.120247Z
- Finished UTC: 2026-11-04T11:04:41.891257Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Raimonol has consistent retained structure/identifier correspondence and four specified tetrahedral centers in both saved forms. The Streptomyces anulatus producer assertion and Streptomyces avermitilis occurrence remain distinct; the blank-AID PubChem sentinel establishes no assay result. No supported source-edit finding is established, and this remains a qualified partial review.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2388; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-a3569df257 | data/natural_products/terpenoids/raimonol.yaml | generated | raimonol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-a3569df257 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-a3569df257 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-a3569df257 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-a3569df257 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-a3569df257 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-a3569df257 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-a3569df257 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-a3569df257 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained structure and identifier correspondence

identity: supported. Targets: naturalproductmech:mibig-a3569df257.

The minted owner naturalproductmech:mibig-a3569df257 retains full key UITXFWAOWQMNFN-UMJMDWPGSA-N from MIBiG BGC0001911 version 3, compound 1, with PubChem:102297697 as a source cross-reference. Both stored-form diagnostics reproduce the key. The local no-3-star-ChEBI-match rationale remains a bounded retained join, not worldwide or current external absence. Source identifiers and structural consistency support local correspondence without independently establishing natural identity.

### Stored topology and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-a3569df257.

Both saved forms are neutral C20H32O, with 21 heavy atoms and 22 bonds. All ten comparison flags are true and the chirality-aware match spans every atom; full_graph_identity_established stays false. Complete tables show fused six-membered carbocyclic rings, one hydroxyl group, one E-labelled side-chain alkene and two terminal methylene/vinyl double bonds. Four tetrahedral centers are specified with no unspecified potential stereo. The terminal double bonds do not require an E/Z assignment; their unlabeled status is not a missing-stereochemistry defect. The source stereo_complete true flag is consistent with this stored representation.

### Producer and locus evidence

provenance: supported. Targets: naturalproductmech:mibig-a3569df257.

MIBiG BGC0001911 version 3 retains Streptomyces anulatus, NCBITaxon:1892, as SOURCE_ASSERTION. LC064029.1 has no recorded locus endpoints or demonstration method, and the locus grade remains CLUSTER_UNSTATED. The separate Streptomyces avermitilis occurrence does not fill those gaps, identify a producer strain or justify importing the unrelated avermitilol locus override found by Native's bounded curation scan.

### Historical citation roles

evidence: supported. Targets: naturalproductmech:mibig-a3569df257.

PMID:26507838 is retained as MIBiG entry-level DATABASE_ASSERTION provenance. DOI:10.1007/S10295-015-1694-6 belongs to the LOTUS organism-reference occurrence. Their roles remain distinct, and neither has been freshly accessed or counted as independent experimental corroboration. Source quality/completeness metadata do not add primary verification.

### Occurrence and activity scope

evidence: supported. Targets: naturalproductmech:mibig-a3569df257.

One exact-key LOTUS row records occurrence in Streptomyces avermitilis, NCBITaxon:33903. This is not the Streptomyces anulatus producer assertion, and no strain equivalence is inferred. The retained PubChem CID102297697 row has a blank AID and “(no assay data)”, with no target or measurement: it is a sentinel, not an assay or an inactivity result. Other retained assay/target joins are empty within their declared local scopes.

### Versioned classification applicability

consistency: supported. Targets: naturalproductmech:mibig-a3569df257.

The versioned Terpenoids / Diterpenoids / Labdane diterpenoids prediction is locally compatible with the C20 fused carbocyclic framework and hydroxyl substituent; precise scaffold and biosynthetic assignments remain subject to primary verification. The single oxygen is terminal, with no represented sugar or glycosidic linkage, supporting is_glycoside false locally. The TERPENE BGC class remains a separate source assertion.

### Review completion

completeness: unknown. Targets: naturalproductmech:mibig-a3569df257.

The complete owner/history, accepted canonical intake, retained source rows and both saved molecular forms were personally read. No causal_graphs, causal_graph_refs, biosynthetic_pathway or molecular_targets root is present in this owner, so no selected maintained-reader call applies. Full QC, complete OAK authority coverage and fresh external verification remain unavailable. No source-edit finding or action is established; completion remains partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2388-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/raimonol.yaml; Whole current plaintext and complete curation_history | supports | Complete owner and 2 history events personally read; immutable source record. |
| support-2388-capture | /private/tmp/npm-review-work/shared-next-batch239/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete accepted owner; exact root presence and all historical annotations preserved. All four mechanism-related roots are absent; no selected reader applies. |
| support-2388-grounding-owner | /private/tmp/npm-review-work/shared-next-batch239/owner-capture-DATA-001.json; /records/7/owner_document/identifier; /records/7/owner_document/label; /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts; /records/7/owner_document/xrefs; /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes | supports | Exact retained identifier/key, stored structure, source concepts and grounding status; no independent natural-identity proof. |
| support-2388-origin-owner | /private/tmp/npm-review-work/shared-next-batch239/owner-capture-DATA-001.json; /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters; /records/7/owner_document/producer_taxon_groups | supports | Complete retained producer and locus claims with separate source grades, versions and historical evidence roles; Raimonol locus coordinates and demonstration methods are absent. |
| support-2388-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch239/owner-capture-DATA-001.json; /records/7/owner_document | supports | Whole owner establishes the retained occurrence/assay/target fields and their absences; it does not establish biological absence outside this record. |
| support-2388-classification-owner | /private/tmp/npm-review-work/shared-next-batch239/owner-capture-DATA-001.json; /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification; /records/7/owner_document/bgc_class; /records/7/owner_document/biosynthesis_origin | supports | Versioned NPClassifier predictions, glycoside flag and source terpene class remain separate assertions. |
| support-2388-direct-contexts | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-target-input-plan-001.json; /records/7/proposed_companion_paths; /records/7/direct_companion_predicates; /records/7/additional_context_roles | context_only | Exact one-hop same-BGC/full-key context selection and input roles; companion claims do not transfer to this owner. |
| support-2388-intake | /private/tmp/npm-review-work/shared-next-batch239/intakes/2388-inspect-001.json; /targets; /source | supports | Actual canonical intake preserves the single target, generated/maintained ownership routes and exact source input map. |
| support-2388-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch239/root-intake-acceptance-001.json; /status; /accepted; /summary | supports | ROOT accepts the ten original canonical intakes and exact source-plan alignment. |
| support-2388-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch239/root-source-inventory-acceptance-001.json; /status; /inventory | supports | Accepted original local extraction; retained rows and scopes are not fresh source verification. |
| support-2388-plan | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-target-input-plan-001.json; /records/7/proposed_input_paths; /records/7/proposed_input_count | supports | Actual immutable input plan for this owner, reconciled to its canonical intake. |
| support-2388-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch239/root-input-plan-acceptance-001.json; /status; /accepted; /plan | supports | ROOT accepts the original complete local plan; input maps are fixed. |
| support-2388-source-reading | /private/tmp/npm-review-work/shared-next-batch239-tentative/support-prep/support-current239-last-five-source-reading-001.json; /scope; /reading; /division | supports | Support complete selected-row/query reading; complementary companion, cache and curation readings remain attributed. |
| support-2388-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch239-tentative/native-prep/native-current239-cached-taxonomy-reading-001.json; /scope; /verification/forward_routes; /verification/unmatched; /limitations | context_only | Native personally read all 19 whole saved stanzas. The two old Sinularia IDs remain unmatched; retained forward destinations have the old names as EXACT synonyms. Cached labels are not live authority. |
| support-2388-curation-scope | /private/tmp/npm-review-work/shared-next-batch239-tentative/native-prep/native-current239-implemented-curation-scan-001.json; /scope; /ignored_files_included; /scanned_tables; /scanned_rows; /applicable_rows; /lexical_positive; /exclusion_conclusion; /limitations | context_only | Native bounded implemented-curation scan found no applicable correction; the sole avermitilol lexical hit is unrelated to these owner identities. |
| support-2388-chemistry | /private/tmp/npm-review-work/shared-next-batch239/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/literal_InChI_layers; /records/7/formula_comparison_scope; /records/7/comparisons; /records/7/atom_correspondence | supports | Both accepted stored forms reproduce the declared normalized identifiers and all ten comparison flags are true for this owner. The complete atom-count match remains distinct from full_graph_identity_established false. |
| support-2388-topology | /private/tmp/npm-review-work/shared-next-batch239/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles; /records/7/inchi | supports | Complete personally read atom, bond, ring, stereo, motif, formula and string tables for both saved forms; no new parse or natural-identity inference. |
| support-2388-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch239/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /DATA; /execution; /verification; /warnings; /limits | supports | ROOT accepts the single original twenty-form diagnostic. Two undefined-stereo warnings are global and unassigned; scientific interpretation uses the complete saved tables. |
| support-2388-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch239/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic exit0, exact saved streams and no retry or external request. |
| support-2388-diagnostic-warnings | /private/tmp/npm-review-work/shared-next-batch239/chemistry-local/diagnostic-original-001.stderr; Whole original stderr stream | context_only | Two original omitted-undefined-stereo warnings remain global; neither is attributed to this owner. |
| support-2388-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2388-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2388-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2388-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2388-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds query frame, including 1 matching row placements; negative results remain limited to this retained source and predicate. |
| support-2388-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Complete retained mibig_compounds payload at physical line 2236 through 2236, including all 25 fields; source assertions and citation roles remain bounded. |
| support-2388-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 2236 | context_only | Exact complete physical rows and every field were joined to the saved matches and current table bytes; no source query was replayed. |
| support-2388-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures query frame, including 0 matching row placements; negative results remain limited to this retained source and predicate. |
| support-2388-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences query frame, including 1 matching row placements; negative results remain limited to this retained source and predicate. |
| support-2388-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Complete retained lotus_occurrences payload at physical line 8763 through 8763, including all 6 fields; source assertions and citation roles remain bounded. |
| support-2388-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 8763 | context_only | Exact complete physical rows and every field were joined to the saved matches and current table bytes; no source query was replayed. |
| support-2388-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences query frame, including 0 matching row placements; negative results remain limited to this retained source and predicate. |
| support-2388-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier query frame, including 1 matching row placements; negative results remain limited to this retained source and predicate. |
| support-2388-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/npclassifier/matches/0 | supports | Complete retained npclassifier payload at physical line 2406 through 2406, including all 7 fields; source assertions and citation roles remain bounded. |
| support-2388-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 2406 | context_only | Exact complete physical rows and every field were joined to the saved matches and current table bytes; no source query was replayed. |
| support-2388-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay query frame, including 1 matching row placements; negative results remain limited to this retained source and predicate. |
| support-2388-source-pubchem_bioassay-0 | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/pubchem_bioassay/matches/0 | supports | Complete retained pubchem_bioassay payload at physical line 8237 through 8237, including all 11 fields; source assertions and citation roles remain bounded. |
| support-2388-physical-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 8237 | context_only | Exact complete physical rows and every field were joined to the saved matches and current table bytes; no source query was replayed. |
| support-2388-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets query frame, including 0 matching row placements; negative results remain limited to this retained source and predicate. |
| support-2388-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys query frame, including 0 matching row placements; negative results remain limited to this retained source and predicate. |
| support-2388-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins query frame, including 0 matching row placements; negative results remain limited to this retained source and predicate. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-239/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-239/native-current239-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-239/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-239/native-current239-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-239/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-239/native-current239-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-239/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-239/native-current239-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-239/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-239/native-current239-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. Natural identity, primary publications, current taxonomy and external identifiers were not freshly verified.
- Full QC, complete OAK authority coverage and fresh external verification remain unavailable; local parsing and gates do not replace them.
- Normalized identifier and atom-match agreement do not establish full fixed-graph or natural-form identity; saved stereo limitations remain explicit.
- Two original omitted-undefined-stereo warnings remain global and unassigned to owners.
- Occurrence, producer, locus, model, companion and assay claims retain their separate scopes.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five complete owners/history, 45 selected query frames and 21 positive source rows / 231 fields, plus 2 forward-merge rows/6 fields. Complementary companion/source and Native cache/curation readings remain explicitly attributed.
- All ten paired saved forms were personally read: 216 atom rows and 220 bond rows plus complete strings, scalars, rings, stereo, motifs and correspondence, using lossless factoring. No additional molecular parse.
- Actual last-five canonical intakes contain 231 input placements over 66 paths. ROOT operated the original diagnostic/intakes; Native operated the sole maintained reader. This authoring invoked no target or request.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T110441Z-raimonol
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: raimonol'
started_at: '2026-11-04T10:10:44.120247Z'
finished_at: '2026-11-04T11:04:41.891257Z'
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
summary: Raimonol has consistent retained structure/identifier correspondence and
  four specified tetrahedral centers in both saved forms. The Streptomyces anulatus
  producer assertion and Streptomyces avermitilis occurrence remain distinct; the
  blank-AID PubChem sentinel establishes no assay result. No supported source-edit
  finding is established, and this remains a qualified partial review.
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
  - path: data/natural_products/terpenoids/raimonol.yaml
    sha256: 87fed410a182affa1ef5ed6f429280dd724a58bf98c57f6e7e0735307f2dcc76
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
  selection: Campaign path order 2388; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-a3569df257
targets:
- target_id: naturalproductmech:mibig-a3569df257
  path: data/natural_products/terpenoids/raimonol.yaml
  label: raimonol
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
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
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
  - naturalproductmech:mibig-a3569df257
  command: just validate-strict data/natural_products/terpenoids/platensimycin.yaml
    data/natural_products/terpenoids/pleuromutilin.yaml data/natural_products/terpenoids/pr-toxin.yaml
    data/natural_products/terpenoids/preterpestacin-1.yaml data/natural_products/terpenoids/preterpestacin-2.yaml
    data/natural_products/terpenoids/preterpestacin-3.yaml data/natural_products/terpenoids/r-nephthenol.yaml
    data/natural_products/terpenoids/raimonol.yaml data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml
    data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml --workers
    1 --out /private/tmp/npm-native-checks/batch-239/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-a3569df257
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-239/validate-all-001.tsv
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
  - naturalproductmech:mibig-a3569df257
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
  - naturalproductmech:mibig-a3569df257
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
  - naturalproductmech:mibig-a3569df257
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-239/review-queue-001.tsv
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
  - naturalproductmech:mibig-a3569df257
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-a3569df257
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-a3569df257
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2388-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/raimonol.yaml
  locator: Whole current plaintext and complete curation_history
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete owner and 2 history events personally read; immutable source record.
  snapshot_sha256: 87fed410a182affa1ef5ed6f429280dd724a58bf98c57f6e7e0735307f2dcc76
- evidence_id: support-2388-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch239/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete accepted owner; exact root presence and all historical annotations
    preserved. All four mechanism-related roots are absent; no selected reader applies.
  snapshot_sha256: 5bf8c1a52008352740ca3b8d77d2dfc3db08b8029786fa63f103ccd943afc103
- evidence_id: support-2388-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch239/owner-capture-DATA-001.json
  locator: /records/7/owner_document/identifier; /records/7/owner_document/label;
    /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts;
    /records/7/owner_document/xrefs; /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Exact retained identifier/key, stored structure, source concepts and grounding
    status; no independent natural-identity proof.
  snapshot_sha256: 5bf8c1a52008352740ca3b8d77d2dfc3db08b8029786fa63f103ccd943afc103
- evidence_id: support-2388-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch239/owner-capture-DATA-001.json
  locator: /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters;
    /records/7/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete retained producer and locus claims with separate source grades,
    versions and historical evidence roles; Raimonol locus coordinates and demonstration
    methods are absent.
  snapshot_sha256: 5bf8c1a52008352740ca3b8d77d2dfc3db08b8029786fa63f103ccd943afc103
- evidence_id: support-2388-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch239/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Whole owner establishes the retained occurrence/assay/target fields and
    their absences; it does not establish biological absence outside this record.
  snapshot_sha256: 5bf8c1a52008352740ca3b8d77d2dfc3db08b8029786fa63f103ccd943afc103
- evidence_id: support-2388-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch239/owner-capture-DATA-001.json
  locator: /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification;
    /records/7/owner_document/bgc_class; /records/7/owner_document/biosynthesis_origin
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Versioned NPClassifier predictions, glycoside flag and source terpene class
    remain separate assertions.
  snapshot_sha256: 5bf8c1a52008352740ca3b8d77d2dfc3db08b8029786fa63f103ccd943afc103
- evidence_id: support-2388-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-target-input-plan-001.json
  locator: /records/7/proposed_companion_paths; /records/7/direct_companion_predicates;
    /records/7/additional_context_roles
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Exact one-hop same-BGC/full-key context selection and input roles; companion
    claims do not transfer to this owner.
  snapshot_sha256: 51613e793e23e684da3a4908d2aeaf2ddb1ab48180431340ab176f6af159fa36
- evidence_id: support-2388-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch239/intakes/2388-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Actual canonical intake preserves the single target, generated/maintained
    ownership routes and exact source input map.
  snapshot_sha256: 6dff1fdd126a164d555135f2f04bc48f9083b71499c6c5cce05371a57cdbb540
- evidence_id: support-2388-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch239/root-intake-acceptance-001.json
  locator: /status; /accepted; /summary
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: ROOT accepts the ten original canonical intakes and exact source-plan alignment.
  snapshot_sha256: 350575244fe7b01f84f6d56d2a1658d2088c37cef88e403ceb8d44d3845b6ce8
- evidence_id: support-2388-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch239/root-source-inventory-acceptance-001.json
  locator: /status; /inventory
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Accepted original local extraction; retained rows and scopes are not fresh
    source verification.
  snapshot_sha256: bbab885f7341ee2aabae7800368aa34b8555f972bb38e3c783d7e2724f8fcbef
- evidence_id: support-2388-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-target-input-plan-001.json
  locator: /records/7/proposed_input_paths; /records/7/proposed_input_count
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Actual immutable input plan for this owner, reconciled to its canonical
    intake.
  snapshot_sha256: 51613e793e23e684da3a4908d2aeaf2ddb1ab48180431340ab176f6af159fa36
- evidence_id: support-2388-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch239/root-input-plan-acceptance-001.json
  locator: /status; /accepted; /plan
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: ROOT accepts the original complete local plan; input maps are fixed.
  snapshot_sha256: b39e2a8e4ff486df96f3e58584775fb6346f5ec92bf4dd5a3cb19538a1bbb8e9
- evidence_id: support-2388-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/support-prep/support-current239-last-five-source-reading-001.json
  locator: /scope; /reading; /division
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Support complete selected-row/query reading; complementary companion, cache
    and curation readings remain attributed.
  snapshot_sha256: 535774845feb498cbd36a2d0c7f62f7a7575316104b99a896e7c96bde522ced5
- evidence_id: support-2388-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/native-prep/native-current239-cached-taxonomy-reading-001.json
  locator: /scope; /verification/forward_routes; /verification/unmatched; /limitations
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Native personally read all 19 whole saved stanzas. The two old Sinularia
    IDs remain unmatched; retained forward destinations have the old names as EXACT
    synonyms. Cached labels are not live authority.
  snapshot_sha256: bce4d3e803dd18e8d355e58dd2825e3b2e389e312ff30f862a95f8115c273623
- evidence_id: support-2388-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/native-prep/native-current239-implemented-curation-scan-001.json
  locator: /scope; /ignored_files_included; /scanned_tables; /scanned_rows; /applicable_rows;
    /lexical_positive; /exclusion_conclusion; /limitations
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Native bounded implemented-curation scan found no applicable correction;
    the sole avermitilol lexical hit is unrelated to these owner identities.
  snapshot_sha256: 4e7628d9cfeb2bfc28e4ea4953a113227dca7b88903ddf11262f7a538a5be13b
  search_scope: All35 current owner contexts, complete owner/source IDs, fullkeys,
    ownedBGCs, labels/slugs, source names/taxa/chemicalIDs,35 exact BGC:compound IDs
    and both actual assay tuples. Case-insensitive literal token matches over all
    complete rows of9 relevant curation TSVs; Path.rglob enumerated all11 TSVs including
    ignored files.
- evidence_id: support-2388-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch239/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/literal_InChI_layers; /records/7/formula_comparison_scope;
    /records/7/comparisons; /records/7/atom_correspondence
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Both accepted stored forms reproduce the declared normalized identifiers
    and all ten comparison flags are true for this owner. The complete atom-count
    match remains distinct from full_graph_identity_established false.
  snapshot_sha256: b513dc6970f5ec24dc276a66fa64186b58d914bfdaad87f718ba19b1b2dd8982
- evidence_id: support-2388-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch239/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles; /records/7/inchi
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete personally read atom, bond, ring, stereo, motif, formula and string
    tables for both saved forms; no new parse or natural-identity inference.
  snapshot_sha256: b513dc6970f5ec24dc276a66fa64186b58d914bfdaad87f718ba19b1b2dd8982
- evidence_id: support-2388-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch239/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /DATA; /execution; /verification; /warnings; /limits
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: ROOT accepts the single original twenty-form diagnostic. Two undefined-stereo
    warnings are global and unassigned; scientific interpretation uses the complete
    saved tables.
  snapshot_sha256: 4c6595be2082336ca615617558150e2b4c1ef382a3befab5b16280f45175281d
- evidence_id: support-2388-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch239/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Original diagnostic exit0, exact saved streams and no retry or external
    request.
  snapshot_sha256: d339b7b71fe6c35f2fcf36ac835a67bad7695dd43295cdd35831f72f7943b669
- evidence_id: support-2388-diagnostic-warnings
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch239/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr stream
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Two original omitted-undefined-stereo warnings remain global; neither is
    attributed to this owner.
  snapshot_sha256: d8a86d11ed753fb4990e471b63625a2376f528e3b1b998baebaed33110b89b8e
- evidence_id: support-2388-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2388-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2388-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2388-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2388-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete saved mibig_compounds query frame, including 1 matching row placements;
    negative results remain limited to this retained source and predicate.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "UITXFWAOWQMNFN-UMJMDWPGSA-N", "saved_frame": "/contexts/26/source_scope_inventory/joins/mibig_compounds",
    "scope": "Immutable local source inventory only; no live request, retry or broader
    absence claim."}'
- evidence_id: support-2388-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete retained mibig_compounds payload at physical line 2236 through
    2236, including all 25 fields; source assertions and citation roles remain bounded.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
- evidence_id: support-2388-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 2236
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Exact complete physical rows and every field were joined to the saved matches
    and current table bytes; no source query was replayed.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2388-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete saved chebi_structures query frame, including 0 matching row placements;
    negative results remain limited to this retained source and predicate.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "UITXFWAOWQMNFN-UMJMDWPGSA-N", "saved_frame": "/contexts/26/source_scope_inventory/joins/chebi_structures",
    "scope": "Immutable local source inventory only; no live request, retry or broader
    absence claim."}'
- evidence_id: support-2388-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete saved lotus_occurrences query frame, including 1 matching row
    placements; negative results remain limited to this retained source and predicate.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "UITXFWAOWQMNFN-UMJMDWPGSA-N", "saved_frame": "/contexts/26/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Immutable local source inventory only; no live request, retry or broader
    absence claim."}'
- evidence_id: support-2388-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete retained lotus_occurrences payload at physical line 8763 through
    8763, including all 6 fields; source assertions and citation roles remain bounded.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
- evidence_id: support-2388-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 8763
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Exact complete physical rows and every field were joined to the saved matches
    and current table bytes; no source query was replayed.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2388-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences query frame, including 0 matching
    row placements; negative results remain limited to this retained source and predicate.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "UITXFWAOWQMNFN-UMJMDWPGSA-N", "saved_frame": "/contexts/26/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Immutable local source inventory only; no live request, retry or broader
    absence claim."}'
- evidence_id: support-2388-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete saved npclassifier query frame, including 1 matching row placements;
    negative results remain limited to this retained source and predicate.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "UITXFWAOWQMNFN-UMJMDWPGSA-N", "saved_frame": "/contexts/26/source_scope_inventory/joins/npclassifier",
    "scope": "Immutable local source inventory only; no live request, retry or broader
    absence claim."}'
- evidence_id: support-2388-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete retained npclassifier payload at physical line 2406 through 2406,
    including all 7 fields; source assertions and citation roles remain bounded.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
- evidence_id: support-2388-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 2406
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Exact complete physical rows and every field were joined to the saved matches
    and current table bytes; no source query was replayed.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2388-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete saved pubchem_bioassay query frame, including 1 matching row placements;
    negative results remain limited to this retained source and predicate.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "UITXFWAOWQMNFN-UMJMDWPGSA-N", "saved_frame": "/contexts/26/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Immutable local source inventory only; no live request, retry or broader
    absence claim."}'
- evidence_id: support-2388-source-pubchem_bioassay-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/pubchem_bioassay/matches/0
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete retained pubchem_bioassay payload at physical line 8237 through
    8237, including all 11 fields; source assertions and citation roles remain bounded.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
- evidence_id: support-2388-physical-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 8237
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: context_only
  summary: Exact complete physical rows and every field were joined to the saved matches
    and current table bytes; no source query was replayed.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2388-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete saved bindingdb_targets query frame, including 0 matching row
    placements; negative results remain limited to this retained source and predicate.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "UITXFWAOWQMNFN-UMJMDWPGSA-N", "saved_frame": "/contexts/26/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Immutable local source inventory only; no live request, retry or broader
    absence claim."}'
- evidence_id: support-2388-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys query frame, including 0 matching
    row placements; negative results remain limited to this retained source and predicate.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "UITXFWAOWQMNFN-UMJMDWPGSA-N", "saved_frame": "/contexts/26/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Immutable local source inventory only; no live request, retry or broader
    absence claim."}'
- evidence_id: support-2388-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch239-tentative/bgc-prep/bgc-conditional239-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T10:52:01.319839Z'
  support: supports
  summary: Complete saved chebi_origins query frame, including 0 matching row placements;
    negative results remain limited to this retained source and predicate.
  snapshot_sha256: 288d87faa1a3f2be7afd219f99c648f058c2e7d18f8413e1645059e918e3b92f
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/26/source_scope_inventory/joins/chebi_origins",
    "scope": "Immutable local source inventory only; no live request, retry or broader
    absence claim."}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-239/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-239/native-current239-five-gates-execution-001.json
  accessed_at: '2026-11-04T10:13:59.465062Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 6c9fa9fc3cb9c570f115742477d7278d41e70e3fa19af3cb59f6878e155901e1
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-239/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-239/native-current239-five-gates-execution-001.json
  accessed_at: '2026-11-04T10:14:23.840684Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 1c13fae87804619630e74c0f8e4b0ca8d3ba2e6f462b08d8d4d37e5fe6471bd6
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-239/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-239/native-current239-five-gates-execution-001.json
  accessed_at: '2026-11-04T10:14:43.088429Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-239/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-239/native-current239-five-gates-execution-001.json
  accessed_at: '2026-11-04T10:15:16.788787Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-239/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-239/native-current239-five-gates-execution-001.json
  accessed_at: '2026-11-04T10:15:28.437519Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: e0d126565a91f34d66b7d7b52dd11605e4c58010a29b412a0ff0ef35493eab2b
assessments:
- area: identity
  topic: Retained structure and identifier correspondence
  outcome: supported
  summary: The minted owner naturalproductmech:mibig-a3569df257 retains full key UITXFWAOWQMNFN-UMJMDWPGSA-N
    from MIBiG BGC0001911 version 3, compound 1, with PubChem:102297697 as a source
    cross-reference. Both stored-form diagnostics reproduce the key. The local no-3-star-ChEBI-match
    rationale remains a bounded retained join, not worldwide or current external absence.
    Source identifiers and structural consistency support local correspondence without
    independently establishing natural identity.
  assessment_id: support-2388-identity
  target_ids:
  - naturalproductmech:mibig-a3569df257
  evidence_ids:
  - support-2388-grounding-owner
  - support-2388-chemistry
  - support-2388-direct-contexts
  - support-2388-query-chebi_structures
  - support-2388-source-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: UITXFWAOWQMNFN-UMJMDWPGSA-N; exact complete retained key.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2388-grounding-owner
    - support-2388-chemistry
    - support-2388-direct-contexts
    - support-2388-query-chebi_structures
    - support-2388-source-mibig_compounds-0
  - name: grounding_scope
    value: MINTED in the retained owner/inventory; natural identity and current external
      grounding unverified.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2388-grounding-owner
    - support-2388-chemistry
    - support-2388-direct-contexts
    - support-2388-query-chebi_structures
    - support-2388-source-mibig_compounds-0
- area: representation
  topic: Stored topology and stereochemical scope
  outcome: supported
  summary: Both saved forms are neutral C20H32O, with 21 heavy atoms and 22 bonds.
    All ten comparison flags are true and the chirality-aware match spans every atom;
    full_graph_identity_established stays false. Complete tables show fused six-membered
    carbocyclic rings, one hydroxyl group, one E-labelled side-chain alkene and two
    terminal methylene/vinyl double bonds. Four tetrahedral centers are specified
    with no unspecified potential stereo. The terminal double bonds do not require
    an E/Z assignment; their unlabeled status is not a missing-stereochemistry defect.
    The source stereo_complete true flag is consistent with this stored representation.
  assessment_id: support-2388-representation
  target_ids:
  - naturalproductmech:mibig-a3569df257
  evidence_ids:
  - support-2388-grounding-owner
  - support-2388-chemistry
  - support-2388-topology
  - support-2388-diagnostic-acceptance
  - support-2388-structure-schema
  - support-2388-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Four specified tetrahedral centers, one E-labelled alkene and two terminal
      double bonds; no unspecified potential stereo.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2388-grounding-owner
    - support-2388-chemistry
    - support-2388-topology
    - support-2388-diagnostic-acceptance
    - support-2388-structure-schema
    - support-2388-stereo-method
  - name: representation_correspondence
    value: All ten saved comparison flags true; complete chirality-aware atom-count
      match. full_graph_identity_established remains false; no independent natural-form
      proof.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2388-grounding-owner
    - support-2388-chemistry
    - support-2388-topology
    - support-2388-diagnostic-acceptance
    - support-2388-structure-schema
    - support-2388-stereo-method
- area: provenance
  topic: Producer and locus evidence
  outcome: supported
  summary: MIBiG BGC0001911 version 3 retains Streptomyces anulatus, NCBITaxon:1892,
    as SOURCE_ASSERTION. LC064029.1 has no recorded locus endpoints or demonstration
    method, and the locus grade remains CLUSTER_UNSTATED. The separate Streptomyces
    avermitilis occurrence does not fill those gaps, identify a producer strain or
    justify importing the unrelated avermitilol locus override found by Native's bounded
    curation scan.
  assessment_id: support-2388-provenance
  target_ids:
  - naturalproductmech:mibig-a3569df257
  evidence_ids:
  - support-2388-origin-owner
  - support-2388-source-reading
  - support-2388-direct-contexts
  - support-2388-cached-taxonomy
  - support-2388-curation-scope
  - support-2388-source-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    value: Streptomyces anulatus (NCBITaxon:1892) producer assertion; 1 retained occurrence
      placements keep their own organism/strain and reference scope.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2388-origin-owner
    - support-2388-source-reading
    - support-2388-direct-contexts
    - support-2388-cached-taxonomy
    - support-2388-curation-scope
    - support-2388-source-mibig_compounds-0
  - name: producer_evidence
    value: SOURCE_ASSERTION from MIBiG version 3; no upgrade from locus or occurrence
      support.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2388-origin-owner
    - support-2388-source-reading
    - support-2388-direct-contexts
    - support-2388-cached-taxonomy
    - support-2388-curation-scope
    - support-2388-source-mibig_compounds-0
  - name: locus_evidence
    value: mibig:BGC0001911 version 3; CLUSTER_UNSTATED, endpoints and demonstration
      method absent.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2388-origin-owner
    - support-2388-source-reading
    - support-2388-direct-contexts
    - support-2388-cached-taxonomy
    - support-2388-curation-scope
    - support-2388-source-mibig_compounds-0
- area: evidence
  topic: Historical citation roles
  outcome: supported
  summary: PMID:26507838 is retained as MIBiG entry-level DATABASE_ASSERTION provenance.
    DOI:10.1007/S10295-015-1694-6 belongs to the LOTUS organism-reference occurrence.
    Their roles remain distinct, and neither has been freshly accessed or counted
    as independent experimental corroboration. Source quality/completeness metadata
    do not add primary verification.
  assessment_id: support-2388-citations
  target_ids:
  - naturalproductmech:mibig-a3569df257
  evidence_ids:
  - support-2388-origin-owner
  - support-2388-occurrence-activity-owner
  - support-2388-source-reading
  - support-2388-direct-contexts
  - support-2388-source-mibig_compounds-0
  - support-2388-source-lotus_occurrences-0
  - support-2388-source-npclassifier-0
  - support-2388-source-pubchem_bioassay-0
  dimensions:
  - name: citation_scope
    value: PMID:26507838 is retained as MIBiG entry-level DATABASE_ASSERTION provenance.
      DOI:10.1007/S10295-015-1694-6 belongs to the LOTUS organism-reference occurrence.
      Their roles remain distinct, and neither has been freshly accessed or counted
      as independent experimental corroboration. Source quality/completeness metadata
      do not add primary verification.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2388-origin-owner
    - support-2388-occurrence-activity-owner
    - support-2388-source-reading
    - support-2388-direct-contexts
    - support-2388-source-mibig_compounds-0
    - support-2388-source-lotus_occurrences-0
    - support-2388-source-npclassifier-0
    - support-2388-source-pubchem_bioassay-0
- area: evidence
  topic: Occurrence and activity scope
  outcome: supported
  summary: 'One exact-key LOTUS row records occurrence in Streptomyces avermitilis,
    NCBITaxon:33903. This is not the Streptomyces anulatus producer assertion, and
    no strain equivalence is inferred. The retained PubChem CID102297697 row has a
    blank AID and “(no assay data)”, with no target or measurement: it is a sentinel,
    not an assay or an inactivity result. Other retained assay/target joins are empty
    within their declared local scopes.'
  assessment_id: support-2388-occurrence
  target_ids:
  - naturalproductmech:mibig-a3569df257
  evidence_ids:
  - support-2388-occurrence-activity-owner
  - support-2388-direct-contexts
  - support-2388-cached-taxonomy
  - support-2388-curation-scope
  - support-2388-query-lotus_occurrences
  - support-2388-query-chebi_origins
  - support-2388-query-cyanometdb_occurrences
  - support-2388-query-pubchem_bioassay
  - support-2388-query-bindingdb_targets
  - support-2388-query-antibioticmech_inchikeys
  - support-2388-source-lotus_occurrences-0
  - support-2388-source-pubchem_bioassay-0
  dimensions:
  - name: occurrence_scope
    value: 1 retained owner occurrences; exact-key source placements do not establish
      native production or independent experiments.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2388-occurrence-activity-owner
    - support-2388-direct-contexts
    - support-2388-cached-taxonomy
    - support-2388-curation-scope
    - support-2388-query-lotus_occurrences
    - support-2388-query-chebi_origins
    - support-2388-query-cyanometdb_occurrences
    - support-2388-query-pubchem_bioassay
    - support-2388-query-bindingdb_targets
    - support-2388-query-antibioticmech_inchikeys
    - support-2388-source-lotus_occurrences-0
    - support-2388-source-pubchem_bioassay-0
  - name: assay_target_scope
    value: One PubChem blank-AID sentinel for CID102297697; zero retained actual assays
      or target measurements, with no inactivity inference.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2388-occurrence-activity-owner
    - support-2388-direct-contexts
    - support-2388-cached-taxonomy
    - support-2388-curation-scope
    - support-2388-query-lotus_occurrences
    - support-2388-query-chebi_origins
    - support-2388-query-cyanometdb_occurrences
    - support-2388-query-pubchem_bioassay
    - support-2388-query-bindingdb_targets
    - support-2388-query-antibioticmech_inchikeys
    - support-2388-source-lotus_occurrences-0
    - support-2388-source-pubchem_bioassay-0
- area: consistency
  topic: Versioned classification applicability
  outcome: supported
  summary: The versioned Terpenoids / Diterpenoids / Labdane diterpenoids prediction
    is locally compatible with the C20 fused carbocyclic framework and hydroxyl substituent;
    precise scaffold and biosynthetic assignments remain subject to primary verification.
    The single oxygen is terminal, with no represented sugar or glycosidic linkage,
    supporting is_glycoside false locally. The TERPENE BGC class remains a separate
    source assertion.
  assessment_id: support-2388-classification
  target_ids:
  - naturalproductmech:mibig-a3569df257
  evidence_ids:
  - support-2388-classification-owner
  - support-2388-chemistry
  - support-2388-topology
  - support-2388-structure-schema
  - support-2388-classification-seeder
  - support-2388-source-mibig_compounds-0
  - support-2388-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: The versioned Terpenoids / Diterpenoids / Labdane diterpenoids prediction
      is locally compatible with the C20 fused carbocyclic framework and hydroxyl
      substituent; precise scaffold and biosynthetic assignments remain subject to
      primary verification. The single oxygen is terminal, with no represented sugar
      or glycosidic linkage, supporting is_glycoside false locally. The TERPENE BGC
      class remains a separate source assertion.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2388-classification-owner
    - support-2388-chemistry
    - support-2388-topology
    - support-2388-structure-schema
    - support-2388-classification-seeder
    - support-2388-source-mibig_compounds-0
    - support-2388-source-npclassifier-0
- area: completeness
  topic: Review completion
  outcome: unknown
  summary: The complete owner/history, accepted canonical intake, retained source
    rows and both saved molecular forms were personally read. No causal_graphs, causal_graph_refs,
    biosynthetic_pathway or molecular_targets root is present in this owner, so no
    selected maintained-reader call applies. Full QC, complete OAK authority coverage
    and fresh external verification remain unavailable. No source-edit finding or
    action is established; completion remains partial.
  assessment_id: support-2388-completion
  target_ids:
  - naturalproductmech:mibig-a3569df257
  evidence_ids:
  - support-2388-owner
  - support-2388-capture
  - support-2388-intake
  - support-2388-intake-acceptance
  - support-2388-inventory-acceptance
  - support-2388-plan
  - support-2388-plan-acceptance
  - support-2388-source-reading
  - support-2388-diagnostic-acceptance
  - support-2388-diagnostic-execution
  - support-2388-diagnostic-warnings
  - support-2388-review-profile
  dimensions:
  - name: review_completion
    value: Partial, pass_with_limitations. Complete local assigned source/intake/molecular
      readings and no applicable selected maintained reader; Full QC, complete OAK
      and fresh external verification unavailable.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2388-owner
    - support-2388-capture
    - support-2388-intake
    - support-2388-intake-acceptance
    - support-2388-inventory-acceptance
    - support-2388-plan
    - support-2388-plan-acceptance
    - support-2388-source-reading
    - support-2388-diagnostic-acceptance
    - support-2388-diagnostic-execution
    - support-2388-diagnostic-warnings
    - support-2388-review-profile
findings: []
actions: []
limitations:
- All evidence is retained locally. Natural identity, primary publications, current
  taxonomy and external identifiers were not freshly verified.
- Full QC, complete OAK authority coverage and fresh external verification remain
  unavailable; local parsing and gates do not replace them.
- Normalized identifier and atom-match agreement do not establish full fixed-graph
  or natural-form identity; saved stereo limitations remain explicit.
- Two original omitted-undefined-stereo warnings remain global and unassigned to owners.
- Occurrence, producer, locus, model, companion and assay claims retain their separate
  scopes.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support personally read five complete owners/history, 45 selected query frames and
  21 positive source rows / 231 fields, plus 2 forward-merge rows/6 fields. Complementary
  companion/source and Native cache/curation readings remain explicitly attributed.
- 'All ten paired saved forms were personally read: 216 atom rows and 220 bond rows
  plus complete strings, scalars, rings, stereo, motifs and correspondence, using
  lossless factoring. No additional molecular parse.'
- Actual last-five canonical intakes contain 231 input placements over 66 paths. ROOT
  operated the original diagnostic/intakes; Native operated the sole maintained reader.
  This authoring invoked no target or request.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-239
```
