# Local evidence review: gliovirin

- Review: 20261106T055627Z-gliovirin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T05:23:02.223677Z
- Finished UTC: 2026-11-06T05:56:27.777096Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Gliovirin retains source-asserted fungal production and separately scoped fungal, genus and Plectris occurrences. Its saved disulfide-bridged diketopiperazine topology supports the broad model family, with one unresolved tetrahedral center. The two stored representations share normalized identifiers but differ at one amide/imidic-acid site. The animal occurrence supplies no evidence of beetle production or a resolved host association.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2667; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-5730bd08ca | data/natural_products/unclassified/gliovirin.yaml | generated | gliovirin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-5730bd08ca | The original diagnostic parsed both stored forms and preserved all actual comparison flags. Formula, charge, StandardInChI and full key agree within this owner. |
| strict_ten | passed | True | naturalproductmech:mibig-5730bd08ca | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-5730bd08ca | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-5730bd08ca | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-5730bd08ca | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-5730bd08ca | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-5730bd08ca | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-5730bd08ca | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-5730bd08ca | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and grounding

identity: supported. Targets: naturalproductmech:mibig-5730bd08ca.

The minted identifier, complete key and npatlas:NPA016022 preserve BGC0001609 version 4, compound 1. The exact ChEBI source frame is empty and does not independently prove natural identity or current identifier resolution. The stored incomplete-stereochemistry flag remains explicit. Both saved forms regenerate the declared StandardInChI and full key, supporting stored mapping without independent natural-identity verification.

### Stored forms and stereochemistry

representation: unknown. Targets: naturalproductmech:mibig-5730bd08ca.

Both saved forms contain 32 atoms and 37 bonds, formula C20H20N2O8S2, zero net charge and no charged atoms. StandardInChI, full key, formula and charge agree, but both canonical SMILES comparisons are false and the saved one-way map is empty. The reported seven ring rows include a three-membered epoxide and the bridged disulfide/diketopiperazine framework; the connected cycle rank is six, so seven reported rings are not seven independent cycles. The original two amide and two carbonyl motifs become one amide and one carbonyl plus one C(OH)=N site with a terminal hydroxyl oxygen in the InChI reconstruction. The other, substituted amide remains. This is consistent with a local amide/imidic-acid representation change, without proving complete fixed-form identity. Six specified and one unspecified tetrahedral centers remain in both forms; no potential double-bond stereo entry is reported for the ring imine. Atom indices and CIP labels remain form-specific because no cross-form map is available. Neither form has a carbonyl ester motif. Two original undefined-stereo and two charge-rearrangement warnings remain globally unassigned; they are not attached to an individual record.

### Producer, taxonomy and locus grades

provenance: supported. Targets: naturalproductmech:mibig-5730bd08ca.

Trichoderma virens Gv29-8/NCBITaxon:413071 retains SOURCE_ASSERTION producer support, while ABDF02000047.1 remains CLUSTER_UNSTATED with no stated coordinates or methods. LOTUS occurrence ID 1331945 has source label Trichoderma virens but the retained cache labels it Trichoderma virens FT-333. Those different IDs and label scopes are not transferred to the Gv29-8 producer. Genus and animal occurrences do not strengthen strain-production evidence.

### Citation and history scope

evidence: supported. Targets: naturalproductmech:mibig-5730bd08ca.

MIBiG uses ENTRY DOI:10.1002/slct.201700262, also present in uppercase on one LOTUS occurrence. The Trichoderma-genus and Plectris rows share DOI:10.1021/ACS.JNATPROD.5B00669. Repeated or differently cased references are preserved without counting independent experiments, and the underlying papers were not reopened.

### Occurrence, assay and target boundaries

evidence: supported. Targets: naturalproductmech:mibig-5730bd08ca.

Three LOTUS placements remain distinct: taxon 1331945, genus Trichoderma/5543 and Plectris/980945. The Plectris placement is an occurrence-only source assertion sharing a citation with the fungal-genus row; animal production and host-associated origin are unresolved. No exact actual AID, sentinel or target measurement is retained for this owner. Those bounded negative frames do not demonstrate biological inactivity.

### Classification and saved topology

consistency: unknown. Targets: naturalproductmech:mibig-5730bd08ca.

The retained source class is NRPS and the separate subclass is Type I; that subclass is not an additional PKS claim. The saved disulfide linkage and diketopiperazine framework support the broad thiodiketopiperazine description. NPClassifier's Peptide alkaloids and Thiodiketopiperazine alkaloids remain model provenance, with exact natural identity and the unresolved configuration outside this retained-data review. Seven reported ring rows are not seven independent cycles.

### Scientific completion and ownership

completeness: unknown. Targets: naturalproductmech:mibig-5730bd08ca.

The whole selected owner/history, complete retained source payloads and negative query bounds, both saved molecular forms and actual intake claims have been read. Current input hashes and ownership declarations match the accepted plan. Five local gates passed, but full QC and OAK remain unavailable and no live authority was consulted. No maintained reader applies. Completion remains partial; positive assessments concern retained mapping, source-grade fidelity and bounded local topology.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2667-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/gliovirin.yaml; Whole current plaintext including every curation_history entry | supports | Complete personally read selected owner and history; retained contents do not imply fresh source access. |
| support-2667-capture | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/6/owner_document | supports | Complete actual captured owner, including all written claims and exact present/absent mechanism and component roots. |
| support-2667-grounding-owner | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/6/owner_document/identifier; /records/6/owner_document/label; /records/6/owner_document/chemical_structure; /records/6/owner_document/source_concepts; /records/6/owner_document/grounding_status; /records/6/owner_document/grounding_notes | supports | Exact owner-local identifier, structure and grounding/definition fields; retained mapping is distinct from natural-identity proof. |
| support-2667-provenance-owner | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters; /records/6/owner_document/producer_taxon_groups; /records/6/owner_document/bgc_class | supports | Stored producer and locus grades, coordinates and citations are preserved as distinct assertions. |
| support-2667-citations-history | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/6/owner_document/source_concepts; /records/6/owner_document/biosynthetic_gene_clusters; /records/6/owner_document/curation_history | supports | Exact retained source concepts, citation grain and complete seeding history; no primary-paper reopening. |
| support-2667-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/6/owner_document/occurrences; /records/6/owner_document/occurrence_taxon_groups; /records/6/owner_document/xrefs | supports | Owner-local occurrence and identifier placements; no causal production inference. |
| support-2667-activity-owner | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/6/owner_document | supports | Complete owner has no written bioactivity or molecular-target roots; bounded retained absence only. |
| support-2667-classification-owner | /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json; /records/6/owner_document/np_pathway; /records/6/owner_document/np_classification; /records/6/owner_document/biosynthesis_origin; /records/6/owner_document/bgc_class | supports | Owner-local filing and computed classifier values; source class/subclass and local topology are separately evidenced. |
| support-2667-intake | /private/tmp/npm-review-work/shared-next-batch267/intakes-001/2667-inspect-001.json; /status; /source; /targets | supports | Actual inspection-only hashes and target ownership declarations; no scientific reading of entire captured corpus files is implied. |
| support-2667-intake-execution | /private/tmp/npm-review-work/shared-next-batch267/intakes-001/2667-inspect-execution-001.json; /exit_code; /command; /actual_environment; /stdout; /stderr | supports | Original canonical inspection exit 0 and empty stderr for this owner. |
| support-2667-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch267/root-current267-intake-acceptance-001.json; /accepted; /status; /summary; /source_plan_acceptance; /verification | supports | ROOT accepted all ten original inspections and the exact 443 input placements across 54 paths. |
| support-2667-direct-contexts | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-target-input-plan-001.json; /records/6/proposed_companion_paths; /records/6/direct_companion_predicates; /records/6/identity_comparison_paths; /records/6/additional_context_paths; /records/6/additional_context_roles; /records/6/reader_implementation_paths; /records/6/proposed_input_paths; /records/6/proposed_input_count | supports | Exact owner-local companion, seven diagnostic/implementation roles and literal reader implementation inputs where applicable. Captured input presence is distinct from positive scientific evidence. |
| support-2667-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch267/root-current267-source-plan-acceptance-001.json; /status; /plan | supports | ROOT acceptance of the one original operative source plan. |
| support-2667-source-reading | /private/tmp/npm-review-work/shared-next-batch267-tentative/support-prep/support-current267-assigned-source-reading-001.json; /contexts/2 | supports | Personally read every saved frame and full positive row dictionary for this owner; complete companion attribution remains separately scoped. |
| support-2667-raw-reading | /private/tmp/npm-review-work/shared-next-batch267-tentative/support-prep/support-current267-last-five-whole-owner-reading-001.json; /records/1 | supports | Support personally read this whole raw owner and all history entries; no primary source was reopened. |
| support-2667-source-notes | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | supports | Attributed reading reconciliation preserves 17 BGC plus 22 Support row placements and zero Native primary row credit; negative and blank boundaries remain explicit. |
| support-2667-taxonomy | /private/tmp/npm-review-work/shared-next-batch267-tentative/native-prep/native-current267-cached-taxonomy-reading-001.json; /context_interpretations/7; /interpretation; /counts | supports | Owner-local cached labels/synonyms and retained routes; no fresh rank, lineage or production authority. |
| support-2667-curation-scope | /private/tmp/npm-review-work/shared-next-batch267-tentative/native-prep/native-current267-implemented-curation-scan-001.json; /counts; /exact_applicability_resolution; /interpretation; /implementation_scope | supports | Exact implemented-curation and source-identity resolution; lexical matches do not establish an applicable correction or exclusion for this owner. |
| support-2667-chemistry | /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnostic-DATA-001.json; /records/6 | supports | Complete two-form saved molecular tables, scalars, stereo, motifs and comparisons for this owner; normalized equality is not full fixed-form or natural identity proof. |
| support-2667-molecular-reading | /private/tmp/npm-review-work/shared-next-batch267-tentative/support-prep/support-current267-last-five-molecular-intake-reading-001.json; /records/1 | supports | Support personally read every saved atom/bond field and all ring, stereo and motif fields for both forms; no new molecular parse. |
| support-2667-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/root-diagnostic-result-acceptance-001.json; /accepted; /DATA; /execution; /verification; /interpretation_limits | supports | ROOT acceptance of the one original diagnostic, preserving false comparisons and global warning scope. |
| support-2667-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnostic-execution-001.json; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic exit 0 with no retries; two undefined-stereo and two charge-rearrangement warnings remain global and are not assigned to particular owners. |
| support-2667-stereo-implementation | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–172 | supports | The retained stereo_complete calculation uses FindMolChiralCenters with includeUnassigned=True and useLegacyImplementation=False on source SMILES; reconstructed double-bond potential stereo is outside that calculation. |
| support-2667-native-gates | /private/tmp/npm-review-work/shared-next-batch267/root-native-gates-acceptance-001.json; /accepted; /checks_passed; /all_native_gates_passed; /unavailable_required_gates; /complete_selected_queue_rows | supports | Five local gates passed; full QC and OAK remain unavailable. Queue rows are leads, not scientific verdicts. |
| support-2667-reader-applicability | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-selected-mechanism-profile-001.json; /mechanisms; /selected_reader_orders | supports | All ten selected owners have no literal mechanism or component roots; no maintained reader applies. |
| support-2667-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds query frame with all 1 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2667-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/7/source_scope_inventory/joins/mibig_compounds/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2667-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2667-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences query frame with all 3 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2667-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/7/source_scope_inventory/joins/lotus_occurrences/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2667-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2667-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier query frame with all 1 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2667-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/7/source_scope_inventory/joins/npclassifier/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2667-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2667-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2667-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2667-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2667-taxon-query-scope | /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/source_taxa; /contexts/7/source_scope_inventory/forward_taxon_merge_matches; /contexts/7/source_scope_inventory/nonorganism_matches | supports | Exact owner-local source taxon IDs and retained positive/negative diagnostic routes; companion route placements are not additional independent decisions. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-267/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-267/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-267/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-267/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-267/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-267/native-current267-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained owners and saved source payloads only; no fresh primary-paper, taxonomy, sequence or external identifier resolution.
- Gliovirin, Gramibactin, Griselimycin and Grisemycin have unequal canonical strings and empty saved maps. Gibepyrone D has a complete limited map; all five full-identity flags remain false. Unresolved stereochemistry and form-specific atom labels remain explicit.
- Two original undefined-stereo and two charge-rearrangement warnings remain globally unassigned. Full QC and OAK are unavailable; source grades, occurrence grain and computed-family limitations remain explicit.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five complete selected owners/history and ten saved molecular forms: 624 atom rows, 644 bond rows and 32 reported ring rows. Selected source coverage is 45 frames, 17 positive placements and 207 fields; the primary partition including Prolipyrone B is 54 frames, 22 placements and 262 fields. Other contexts retain separate primary attribution.
- Verified 221 actual input placements across 49 paths and their target ownership declarations. Input hashes do not imply scientific reading of whole corpus files. No generated record, native status or history was edited, and no outbound request was sent.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T055627Z-gliovirin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: gliovirin'
started_at: '2026-11-06T05:23:02.223677Z'
finished_at: '2026-11-06T05:56:27.777096Z'
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
summary: Gliovirin retains source-asserted fungal production and separately scoped
  fungal, genus and Plectris occurrences. Its saved disulfide-bridged diketopiperazine
  topology supports the broad model family, with one unresolved tetrahedral center.
  The two stored representations share normalized identifiers but differ at one amide/imidic-acid
  site. The animal occurrence supplies no evidence of beetle production or a resolved
  host association.
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
  - path: data/natural_products/unclassified/gliovirin.yaml
    sha256: a185e20a9b32cadfcabda74b28819ad2894c864de03e506930bdeb91a33bdc10
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
  selection: Campaign path order 2667; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-5730bd08ca
targets:
- target_id: naturalproductmech:mibig-5730bd08ca
  path: data/natural_products/unclassified/gliovirin.yaml
  label: gliovirin
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
  summary: The original diagnostic parsed both stored forms and preserved all actual
    comparison flags. Formula, charge, StandardInChI and full key agree within this
    owner.
  scope_note: Original shared twenty-form execution; no rerun. False canonical comparisons,
    empty maps and unspecified stereochemistry remain explicit. This passed execution
    check does not certify full graph or natural identity.
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
  evidence_ids:
  - support-2667-chemistry
  - support-2667-diagnostic-acceptance
  - support-2667-diagnostic-execution
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
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
  - naturalproductmech:mibig-5730bd08ca
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
  - naturalproductmech:mibig-5730bd08ca
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
  - naturalproductmech:mibig-5730bd08ca
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
  - naturalproductmech:mibig-5730bd08ca
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
  - naturalproductmech:mibig-5730bd08ca
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2667-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/gliovirin.yaml
  locator: Whole current plaintext including every curation_history entry
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete personally read selected owner and history; retained contents
    do not imply fresh source access.
  snapshot_sha256: a185e20a9b32cadfcabda74b28819ad2894c864de03e506930bdeb91a33bdc10
- evidence_id: support-2667-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete actual captured owner, including all written claims and exact
    present/absent mechanism and component roots.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: support-2667-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/6/owner_document/identifier; /records/6/owner_document/label;
    /records/6/owner_document/chemical_structure; /records/6/owner_document/source_concepts;
    /records/6/owner_document/grounding_status; /records/6/owner_document/grounding_notes
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Exact owner-local identifier, structure and grounding/definition fields;
    retained mapping is distinct from natural-identity proof.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: support-2667-provenance-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters;
    /records/6/owner_document/producer_taxon_groups; /records/6/owner_document/bgc_class
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Stored producer and locus grades, coordinates and citations are preserved
    as distinct assertions.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: support-2667-citations-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/6/owner_document/source_concepts; /records/6/owner_document/biosynthetic_gene_clusters;
    /records/6/owner_document/curation_history
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Exact retained source concepts, citation grain and complete seeding history;
    no primary-paper reopening.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: support-2667-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/6/owner_document/occurrences; /records/6/owner_document/occurrence_taxon_groups;
    /records/6/owner_document/xrefs
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Owner-local occurrence and identifier placements; no causal production
    inference.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: support-2667-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete owner has no written bioactivity or molecular-target roots; bounded
    retained absence only.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: support-2667-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267/owner-capture-DATA-001.json
  locator: /records/6/owner_document/np_pathway; /records/6/owner_document/np_classification;
    /records/6/owner_document/biosynthesis_origin; /records/6/owner_document/bgc_class
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Owner-local filing and computed classifier values; source class/subclass
    and local topology are separately evidenced.
  snapshot_sha256: 470d8b87a95db55e4b184fd1261b4d1cc5d01a0a3072ce7687752f42a52d5191
- evidence_id: support-2667-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/intakes-001/2667-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Actual inspection-only hashes and target ownership declarations; no scientific
    reading of entire captured corpus files is implied.
  snapshot_sha256: 876632a5196bc7a2627b4dfd2f997cb02b354150e615453514995ee4b936a465
- evidence_id: support-2667-intake-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/intakes-001/2667-inspect-execution-001.json
  locator: /exit_code; /command; /actual_environment; /stdout; /stderr
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Original canonical inspection exit 0 and empty stderr for this owner.
  snapshot_sha256: d1e3f01cd94c7f352a9ffcae2a11440dde2f2ab21be24f2878ec358ba75b4c9a
- evidence_id: support-2667-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/root-current267-intake-acceptance-001.json
  locator: /accepted; /status; /summary; /source_plan_acceptance; /verification
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: ROOT accepted all ten original inspections and the exact 443 input placements
    across 54 paths.
  snapshot_sha256: f292e156d50caea7274697f897681baab83bb25c772d8ff8ed2751c192d74a57
- evidence_id: support-2667-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-target-input-plan-001.json
  locator: /records/6/proposed_companion_paths; /records/6/direct_companion_predicates;
    /records/6/identity_comparison_paths; /records/6/additional_context_paths; /records/6/additional_context_roles;
    /records/6/reader_implementation_paths; /records/6/proposed_input_paths; /records/6/proposed_input_count
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Exact owner-local companion, seven diagnostic/implementation roles and
    literal reader implementation inputs where applicable. Captured input presence
    is distinct from positive scientific evidence.
  snapshot_sha256: 9d3bb7ebc200cc291d785e33eb1bf51e4bb76ecabcdc943153205fbe56b06657
- evidence_id: support-2667-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/root-current267-source-plan-acceptance-001.json
  locator: /status; /plan
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: ROOT acceptance of the one original operative source plan.
  snapshot_sha256: 97d98ee1ecfc06f90fbdfc8ad2ccf2a38ab78ae423410b6a824cb928d13b8051
- evidence_id: support-2667-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/support-prep/support-current267-assigned-source-reading-001.json
  locator: /contexts/2
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Personally read every saved frame and full positive row dictionary for
    this owner; complete companion attribution remains separately scoped.
  snapshot_sha256: 90e4ccf74e2ae1ce260168f161b89c5dbb55df88ff39d7baee361dd6ac6aaa82
- evidence_id: support-2667-raw-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/support-prep/support-current267-last-five-whole-owner-reading-001.json
  locator: /records/1
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Support personally read this whole raw owner and all history entries; no
    primary source was reopened.
  snapshot_sha256: cd2fd584e509871b214df92dee6a6a1d50e4d10362ea72294647a69373ebf2e0
- evidence_id: support-2667-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Attributed reading reconciliation preserves 17 BGC plus 22 Support row
    placements and zero Native primary row credit; negative and blank boundaries remain
    explicit.
  snapshot_sha256: d73c4fcacc581e4eda06b1e52854b82f6f38530ef14d61d1ba65b093aa03524e
- evidence_id: support-2667-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/native-prep/native-current267-cached-taxonomy-reading-001.json
  locator: /context_interpretations/7; /interpretation; /counts
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Owner-local cached labels/synonyms and retained routes; no fresh rank,
    lineage or production authority.
  snapshot_sha256: 8606d838c23979d0f94dbba0440d4852810e7a52d3a6f283bd22e1a94f13c527
- evidence_id: support-2667-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/native-prep/native-current267-implemented-curation-scan-001.json
  locator: /counts; /exact_applicability_resolution; /interpretation; /implementation_scope
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Exact implemented-curation and source-identity resolution; lexical matches
    do not establish an applicable correction or exclusion for this owner.
  snapshot_sha256: fca61cd560e376fadcad5ce2eba4e186a81afdafdc94f8d06548ab975ce6b7c6
  search_scope: '{"owner": "data/natural_products/unclassified/gliovirin.yaml", "primary_source_row_credit":
    0, "scope": "Retained exact identity/digest predicates; lexical candidates remain
    separate"}'
- evidence_id: support-2667-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete two-form saved molecular tables, scalars, stereo, motifs and comparisons
    for this owner; normalized equality is not full fixed-form or natural identity
    proof.
  snapshot_sha256: 3fea1ec0393d289bfbf7e75bf538d367fac7471c79f90564952de3e0be7e91a0
- evidence_id: support-2667-molecular-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/support-prep/support-current267-last-five-molecular-intake-reading-001.json
  locator: /records/1
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Support personally read every saved atom/bond field and all ring, stereo
    and motif fields for both forms; no new molecular parse.
  snapshot_sha256: 84e0a0c736683c8c338f461105f37b7bb4cefca5e00aa2cf0b59a5fb2308ebdc
- evidence_id: support-2667-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/root-diagnostic-result-acceptance-001.json
  locator: /accepted; /DATA; /execution; /verification; /interpretation_limits
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: ROOT acceptance of the one original diagnostic, preserving false comparisons
    and global warning scope.
  snapshot_sha256: 34342ef403d82e4a6112037a844fcb9f574eb6999e86108bc77aeb685840dec7
- evidence_id: support-2667-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Original diagnostic exit 0 with no retries; two undefined-stereo and two
    charge-rearrangement warnings remain global and are not assigned to particular
    owners.
  snapshot_sha256: 557939b2cbb7aa99e65a38f092c1b57fce96fb3393b36cd94f5a2c5e6b2868fd
- evidence_id: support-2667-stereo-implementation
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–172
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: The retained stereo_complete calculation uses FindMolChiralCenters with
    includeUnassigned=True and useLegacyImplementation=False on source SMILES; reconstructed
    double-bond potential stereo is outside that calculation.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2667-native-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch267/root-native-gates-acceptance-001.json
  locator: /accepted; /checks_passed; /all_native_gates_passed; /unavailable_required_gates;
    /complete_selected_queue_rows
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Five local gates passed; full QC and OAK remain unavailable. Queue rows
    are leads, not scientific verdicts.
  snapshot_sha256: 50ea7d1b4e1955899f97f52176bdfe71e00713ebc89293aac111dfed02c9b225
- evidence_id: support-2667-reader-applicability
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-selected-mechanism-profile-001.json
  locator: /mechanisms; /selected_reader_orders
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: All ten selected owners have no literal mechanism or component roots; no
    maintained reader applies.
  snapshot_sha256: b4ca516c891b016ba262bd3a2612bfaacdce735bc0f4028adae90586d10cf331
- evidence_id: support-2667-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete saved mibig_compounds query frame with all 1 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "VZUFPCHAVLFFAY-QEZWNWIZSA-N"}'
- evidence_id: support-2667-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/7/source_scope_inventory/joins/mibig_compounds/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2667-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete saved chebi_structures query frame with all 0 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "VZUFPCHAVLFFAY-QEZWNWIZSA-N"}'
- evidence_id: support-2667-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete saved lotus_occurrences query frame with all 3 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matched_placements": 3, "predicate": "exact complete standard_inchi_key
    equality", "query": "VZUFPCHAVLFFAY-QEZWNWIZSA-N"}'
- evidence_id: support-2667-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/7/source_scope_inventory/joins/lotus_occurrences/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2667-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences query frame with all 0 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "VZUFPCHAVLFFAY-QEZWNWIZSA-N"}'
- evidence_id: support-2667-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete saved npclassifier query frame with all 1 row placements and full
    fields. A negative frame is limited to its recorded predicate; repeated rows are
    not independent experiments.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "VZUFPCHAVLFFAY-QEZWNWIZSA-N"}'
- evidence_id: support-2667-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/7/source_scope_inventory/joins/npclassifier/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2667-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete saved pubchem_bioassay query frame with all 0 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "VZUFPCHAVLFFAY-QEZWNWIZSA-N"}'
- evidence_id: support-2667-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete saved bindingdb_targets query frame with all 0 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "VZUFPCHAVLFFAY-QEZWNWIZSA-N"}'
- evidence_id: support-2667-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys query frame with all 0 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "VZUFPCHAVLFFAY-QEZWNWIZSA-N"}'
- evidence_id: support-2667-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Complete saved chebi_origins query frame with all 0 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"matched_placements": 0, "predicate": "exact chebi_id from exact
    full-key structure rows", "query": []}'
- evidence_id: support-2667-taxon-query-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch267-tentative/bgc-prep/bgc-conditional267-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/source_taxa; /contexts/7/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/7/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-06T05:53:49.048887Z'
  support: supports
  summary: Exact owner-local source taxon IDs and retained positive/negative diagnostic
    routes; companion route placements are not additional independent decisions.
  snapshot_sha256: 91eeec20df917ed3c65c59e05b27b3f8baeef925bd38bed53df844a1c5835d62
  search_scope: '{"forward_merge_placements": 0, "nonorganism_placements": 0, "predicate":
    "Exact retained taxon IDs against both captured diagnostic tables", "source_taxa":
    ["NCBITaxon:1331945", "NCBITaxon:413071", "NCBITaxon:5543", "NCBITaxon:980945"]}'
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
- area: identity
  topic: Retained identity and grounding
  dimensions:
  - name: standard_inchi_key
    definition: Exact full key; no prefix or name substitution.
    value: VZUFPCHAVLFFAY-QEZWNWIZSA-N
    evidence_ids:
    - support-2667-grounding-owner
    - support-2667-chemistry
    - support-2667-query-mibig_compounds
    - support-2667-query-chebi_structures
    - support-2667-direct-contexts
    - support-2667-source-reading
  - name: grounding_scope
    definition: Stored grounding fidelity is distinct from fresh natural-identity
      verification.
    value: MINTED retained mapping; no independent natural-identity proof
    evidence_ids:
    - support-2667-grounding-owner
    - support-2667-chemistry
    - support-2667-query-mibig_compounds
    - support-2667-query-chebi_structures
    - support-2667-direct-contexts
    - support-2667-source-reading
  assessment_id: support-2667-identity
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
  evidence_ids:
  - support-2667-grounding-owner
  - support-2667-chemistry
  - support-2667-query-mibig_compounds
  - support-2667-query-chebi_structures
  - support-2667-direct-contexts
  - support-2667-source-reading
  outcome: supported
  summary: The minted identifier, complete key and npatlas:NPA016022 preserve BGC0001609
    version 4, compound 1. The exact ChEBI source frame is empty and does not independently
    prove natural identity or current identifier resolution. The stored incomplete-stereochemistry
    flag remains explicit. Both saved forms regenerate the declared StandardInChI
    and full key, supporting stored mapping without independent natural-identity verification.
- area: representation
  topic: Stored forms and stereochemistry
  dimensions:
  - name: stereochemistry_scope
    definition: Saved original atom-center and double-bond scope; no natural stereochemistry
      proof.
    value: Six specified and one unspecified tetrahedral centers in both forms; no
      potential double-bond stereo entries
    evidence_ids:
    - support-2667-grounding-owner
    - support-2667-chemistry
    - support-2667-molecular-reading
    - support-2667-diagnostic-acceptance
    - support-2667-diagnostic-execution
    - support-2667-stereo-implementation
  - name: representation_correspondence
    definition: Normalized InChI/key agreement does not prove full fixed-form graph
      equivalence.
    value: Eight of ten comparisons true; one amide/imidic-acid change; unequal canonical
      strings and empty saved map
    evidence_ids:
    - support-2667-grounding-owner
    - support-2667-chemistry
    - support-2667-molecular-reading
    - support-2667-diagnostic-acceptance
    - support-2667-diagnostic-execution
    - support-2667-stereo-implementation
  assessment_id: support-2667-representation
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
  evidence_ids:
  - support-2667-grounding-owner
  - support-2667-chemistry
  - support-2667-molecular-reading
  - support-2667-diagnostic-acceptance
  - support-2667-diagnostic-execution
  - support-2667-stereo-implementation
  outcome: unknown
  summary: Both saved forms contain 32 atoms and 37 bonds, formula C20H20N2O8S2, zero
    net charge and no charged atoms. StandardInChI, full key, formula and charge agree,
    but both canonical SMILES comparisons are false and the saved one-way map is empty.
    The reported seven ring rows include a three-membered epoxide and the bridged
    disulfide/diketopiperazine framework; the connected cycle rank is six, so seven
    reported rings are not seven independent cycles. The original two amide and two
    carbonyl motifs become one amide and one carbonyl plus one C(OH)=N site with a
    terminal hydroxyl oxygen in the InChI reconstruction. The other, substituted amide
    remains. This is consistent with a local amide/imidic-acid representation change,
    without proving complete fixed-form identity. Six specified and one unspecified
    tetrahedral centers remain in both forms; no potential double-bond stereo entry
    is reported for the ring imine. Atom indices and CIP labels remain form-specific
    because no cross-form map is available. Neither form has a carbonyl ester motif.
    Two original undefined-stereo and two charge-rearrangement warnings remain globally
    unassigned; they are not attached to an individual record.
- area: provenance
  topic: Producer, taxonomy and locus grades
  dimensions:
  - name: taxon_scope
    definition: Cached IDs/names/synonyms are distinct from verified rank, lineage
      or strain identity.
    value: Gv29-8 producer 413071; source/cache label difference at 1331945; genus
      5543 and Plectris 980945 occurrences
    evidence_ids:
    - support-2667-provenance-owner
    - support-2667-taxonomy
    - support-2667-taxon-query-scope
    - support-2667-curation-scope
    - support-2667-query-mibig_compounds
  - name: producer_evidence
    definition: Retained producer grade, not inferred from occurrence or locus association.
    value: SOURCE_ASSERTION; BGC0001609 version 4; no occurrence-to-production upgrade
    evidence_ids:
    - support-2667-provenance-owner
    - support-2667-taxonomy
    - support-2667-taxon-query-scope
    - support-2667-curation-scope
    - support-2667-query-mibig_compounds
  - name: locus_evidence
    definition: Retained compound-specific cluster-link grade and source methods.
    value: CLUSTER_UNSTATED; ABDF02000047.1; coordinates and methods absent
    evidence_ids:
    - support-2667-provenance-owner
    - support-2667-taxonomy
    - support-2667-taxon-query-scope
    - support-2667-curation-scope
    - support-2667-query-mibig_compounds
  assessment_id: support-2667-provenance
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
  evidence_ids:
  - support-2667-provenance-owner
  - support-2667-taxonomy
  - support-2667-taxon-query-scope
  - support-2667-curation-scope
  - support-2667-query-mibig_compounds
  outcome: supported
  summary: Trichoderma virens Gv29-8/NCBITaxon:413071 retains SOURCE_ASSERTION producer
    support, while ABDF02000047.1 remains CLUSTER_UNSTATED with no stated coordinates
    or methods. LOTUS occurrence ID 1331945 has source label Trichoderma virens but
    the retained cache labels it Trichoderma virens FT-333. Those different IDs and
    label scopes are not transferred to the Gv29-8 producer. Genus and animal occurrences
    do not strengthen strain-production evidence.
- area: evidence
  topic: Citation and history scope
  dimensions:
  - name: citation_scope
    definition: Exact retained citation basis; no implied new primary-source access.
    value: ENTRY DOI:10.1002/slct.201700262; repeated DOI:10.1021/ACS.JNATPROD.5B00669
      is not independent support
    evidence_ids:
    - support-2667-citations-history
    - support-2667-source-reading
    - support-2667-source-notes
    - support-2667-source-mibig_compounds
    - support-2667-source-lotus_occurrences
    - support-2667-source-npclassifier
    - support-2667-query-mibig_compounds
    - support-2667-query-chebi_structures
    - support-2667-query-lotus_occurrences
    - support-2667-query-cyanometdb_occurrences
    - support-2667-query-npclassifier
    - support-2667-query-pubchem_bioassay
    - support-2667-query-bindingdb_targets
    - support-2667-query-antibioticmech_inchikeys
    - support-2667-query-chebi_origins
  assessment_id: support-2667-citations
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
  evidence_ids:
  - support-2667-citations-history
  - support-2667-source-reading
  - support-2667-source-notes
  - support-2667-source-mibig_compounds
  - support-2667-source-lotus_occurrences
  - support-2667-source-npclassifier
  - support-2667-query-mibig_compounds
  - support-2667-query-chebi_structures
  - support-2667-query-lotus_occurrences
  - support-2667-query-cyanometdb_occurrences
  - support-2667-query-npclassifier
  - support-2667-query-pubchem_bioassay
  - support-2667-query-bindingdb_targets
  - support-2667-query-antibioticmech_inchikeys
  - support-2667-query-chebi_origins
  outcome: supported
  summary: MIBiG uses ENTRY DOI:10.1002/slct.201700262, also present in uppercase
    on one LOTUS occurrence. The Trichoderma-genus and Plectris rows share DOI:10.1021/ACS.JNATPROD.5B00669.
    Repeated or differently cased references are preserved without counting independent
    experiments, and the underlying papers were not reopened.
- area: evidence
  topic: Occurrence, assay and target boundaries
  dimensions:
  - name: occurrence_scope
    definition: Source placements and shared citations are not independent production
      experiments.
    value: Three retained occurrences; animal production and host association unresolved
    evidence_ids:
    - support-2667-occurrence-owner
    - support-2667-activity-owner
    - support-2667-source-reading
    - support-2667-curation-scope
    - support-2667-taxon-query-scope
    - support-2667-source-mibig_compounds
    - support-2667-source-lotus_occurrences
    - support-2667-source-npclassifier
    - support-2667-query-mibig_compounds
    - support-2667-query-chebi_structures
    - support-2667-query-lotus_occurrences
    - support-2667-query-cyanometdb_occurrences
    - support-2667-query-npclassifier
    - support-2667-query-pubchem_bioassay
    - support-2667-query-bindingdb_targets
    - support-2667-query-antibioticmech_inchikeys
    - support-2667-query-chebi_origins
  - name: assay_target_scope
    definition: Actual AIDs, blank sentinels and bounded negative target queries remain
      distinct.
    value: No actual AID or sentinel; bounded negative retained target queries
    evidence_ids:
    - support-2667-occurrence-owner
    - support-2667-activity-owner
    - support-2667-source-reading
    - support-2667-curation-scope
    - support-2667-taxon-query-scope
    - support-2667-source-mibig_compounds
    - support-2667-source-lotus_occurrences
    - support-2667-source-npclassifier
    - support-2667-query-mibig_compounds
    - support-2667-query-chebi_structures
    - support-2667-query-lotus_occurrences
    - support-2667-query-cyanometdb_occurrences
    - support-2667-query-npclassifier
    - support-2667-query-pubchem_bioassay
    - support-2667-query-bindingdb_targets
    - support-2667-query-antibioticmech_inchikeys
    - support-2667-query-chebi_origins
  assessment_id: support-2667-occurrence-activity
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
  evidence_ids:
  - support-2667-occurrence-owner
  - support-2667-activity-owner
  - support-2667-source-reading
  - support-2667-curation-scope
  - support-2667-taxon-query-scope
  - support-2667-source-mibig_compounds
  - support-2667-source-lotus_occurrences
  - support-2667-source-npclassifier
  - support-2667-query-mibig_compounds
  - support-2667-query-chebi_structures
  - support-2667-query-lotus_occurrences
  - support-2667-query-cyanometdb_occurrences
  - support-2667-query-npclassifier
  - support-2667-query-pubchem_bioassay
  - support-2667-query-bindingdb_targets
  - support-2667-query-antibioticmech_inchikeys
  - support-2667-query-chebi_origins
  outcome: supported
  summary: 'Three LOTUS placements remain distinct: taxon 1331945, genus Trichoderma/5543
    and Plectris/980945. The Plectris placement is an occurrence-only source assertion
    sharing a citation with the fungal-genus row; animal production and host-associated
    origin are unresolved. No exact actual AID, sentinel or target measurement is
    retained for this owner. Those bounded negative frames do not demonstrate biological
    inactivity.'
- area: consistency
  topic: Classification and saved topology
  dimensions:
  - name: classification_applicability
    definition: Local encoded topology can support a broad description without validating
      a model-derived pathway or natural identity.
    value: Disulfide/diketopiperazine framework supports the broad model family; exact
      natural identity remains qualified
    evidence_ids:
    - support-2667-classification-owner
    - support-2667-chemistry
    - support-2667-molecular-reading
    - support-2667-query-npclassifier
    - support-2667-query-mibig_compounds
  assessment_id: support-2667-classification
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
  evidence_ids:
  - support-2667-classification-owner
  - support-2667-chemistry
  - support-2667-molecular-reading
  - support-2667-query-npclassifier
  - support-2667-query-mibig_compounds
  outcome: unknown
  summary: The retained source class is NRPS and the separate subclass is Type I;
    that subclass is not an additional PKS claim. The saved disulfide linkage and
    diketopiperazine framework support the broad thiodiketopiperazine description.
    NPClassifier's Peptide alkaloids and Thiodiketopiperazine alkaloids remain model
    provenance, with exact natural identity and the unresolved configuration outside
    this retained-data review. Seven reported ring rows are not seven independent
    cycles.
- area: completeness
  topic: Scientific completion and ownership
  dimensions:
  - name: review_completion
    definition: Coverage of a whole record is distinct from all required checks and
      independent external verification.
    value: partial; five local gates passed; QC/OAK unavailable; no applicable reader
    evidence_ids:
    - support-2667-owner
    - support-2667-capture
    - support-2667-intake
    - support-2667-intake-execution
    - support-2667-intake-acceptance
    - support-2667-plan-acceptance
    - support-2667-source-reading
    - support-2667-raw-reading
    - support-2667-source-notes
    - support-2667-diagnostic-acceptance
    - support-2667-molecular-reading
    - support-2667-native-gates
    - support-2667-reader-applicability
  assessment_id: support-2667-completion
  target_ids:
  - naturalproductmech:mibig-5730bd08ca
  evidence_ids:
  - support-2667-owner
  - support-2667-capture
  - support-2667-intake
  - support-2667-intake-execution
  - support-2667-intake-acceptance
  - support-2667-plan-acceptance
  - support-2667-source-reading
  - support-2667-raw-reading
  - support-2667-source-notes
  - support-2667-diagnostic-acceptance
  - support-2667-molecular-reading
  - support-2667-native-gates
  - support-2667-reader-applicability
  outcome: unknown
  summary: The whole selected owner/history, complete retained source payloads and
    negative query bounds, both saved molecular forms and actual intake claims have
    been read. Current input hashes and ownership declarations match the accepted
    plan. Five local gates passed, but full QC and OAK remain unavailable and no live
    authority was consulted. No maintained reader applies. Completion remains partial;
    positive assessments concern retained mapping, source-grade fidelity and bounded
    local topology.
findings: []
actions: []
limitations:
- Retained owners and saved source payloads only; no fresh primary-paper, taxonomy,
  sequence or external identifier resolution.
- Gliovirin, Gramibactin, Griselimycin and Grisemycin have unequal canonical strings
  and empty saved maps. Gibepyrone D has a complete limited map; all five full-identity
  flags remain false. Unresolved stereochemistry and form-specific atom labels remain
  explicit.
- Two original undefined-stereo and two charge-rearrangement warnings remain globally
  unassigned. Full QC and OAK are unavailable; source grades, occurrence grain and
  computed-family limitations remain explicit.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'Support personally read five complete selected owners/history and ten saved molecular
  forms: 624 atom rows, 644 bond rows and 32 reported ring rows. Selected source coverage
  is 45 frames, 17 positive placements and 207 fields; the primary partition including
  Prolipyrone B is 54 frames, 22 placements and 262 fields. Other contexts retain
  separate primary attribution.'
- Verified 221 actual input placements across 49 paths and their target ownership
  declarations. Input hashes do not imply scientific reading of whole corpus files.
  No generated record, native status or history was edited, and no outbound request
  was sent.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-267
```
