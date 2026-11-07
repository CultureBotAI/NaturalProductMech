# Local evidence review: histidyltryptophanyldiketopiperazine

- Review: 20261106T102656Z-histidyltryptophanyldiketopiperazine
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T09:35:23.177066Z
- Finished UTC: 2026-11-06T10:26:56.840865Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Histidyltryptophanyldiketopiperazine supports a qualified pass for faithful source mapping and graded producer/locus evidence. The cyclic dipeptide, imidazole and indole topology is explicit, but two atom centers remain unspecified and the stored forms differ in amide/imidic and imidazole proton placement. Normalized identifier agreement does not resolve those fixed-form or natural-stereochemistry limits.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2699; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-facad00852 | data/natural_products/unclassified/histidyltryptophanyldiketopiperazine.yaml | generated | histidyltryptophanyldiketopiperazine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-facad00852 | The original diagnostic parsed both stored forms; formula, charge, StandardInChI and full key agree within this owner. |
| strict_ten | passed | True | naturalproductmech:mibig-facad00852 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-facad00852 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-facad00852 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-facad00852 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-facad00852 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-facad00852 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-facad00852 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-facad00852 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and grounding

identity: supported. Targets: naturalproductmech:mibig-facad00852.

The minted identifier and exact YNHVZXATNGMVNC-UHFFFAOYSA-N key retain the BGC0000420 version 5 compound placement. No database identifiers are provided in that source row and no owner xrefs are written; the exact-key ChEBI frame is also empty. The six shared-BGC companions are diagnostic context only. In particular, glandicoline B and meleagrine mechanism roots do not become this selected owner’s mechanism or evidence. Both original stored forms regenerate the declared StandardInChI and full key; that supports retained mapping without independent natural-identity proof.

### Stored forms and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-facad00852.

Both saved forms have C17H17N5O2, 24 atoms, 27 bonds and four rings of sizes 6, 5, 6 and 5, with zero net and individual atom charge. Formula, charge, StandardInChI and full-key comparisons agree, but both canonical SMILES comparisons are false and the saved map is empty; full_graph_identity_established is false. Source carbonyls C1=O0 and C22=O23 are attached to ring nitrogens N14 and N3, giving the two diketopiperazine amide sites. In the InChI form, C15=N21/O22H and C16=N20/O23H replace them; both hydroxyl oxygens have degree one and H1, while the imine nitrogens have H0. The imidazole [nH] location also changes between the canonical forms. Two unspecified tetrahedral centers persist (source 2 and 15; InChI 13 and 14), agreeing with stereo_complete false. Neither new ring C=N is listed as potential double-bond stereo. No ester, candidate C5O ring or glycosidic linkage is established. Two warnings in the original shared stderr stream are globally unassigned; none is attributed to this owner.

### Producer, taxonomy and locus grades

provenance: supported. Targets: naturalproductmech:mibig-facad00852.

Penicillium rubens Wisconsin 54-1255, NCBITaxon:500485, retains BGC_CHARACTERIZED producer evidence from the stated knock-out studies. The separate BGC0000420 locus link is CLUSTER_DEMONSTRATED at AM920436.1, coordinates 3,638,081–3,658,739, with NRPS source classification. The version 5 entry is active, questionable in quality and complete in source completeness. That source metadata and the maintained grade table support the retained grades, without constituting an independent rereading of the experiment or a complete enzymatic route.

### Citation and history scope

evidence: supported. Targets: naturalproductmech:mibig-facad00852.

DOI:10.1002/cbic.201402686 is retained at COMPOUND_EVIDENCE grain for this exact compound placement. It is not promoted from an entry-level citation or borrowed from another shared-BGC owner. Both curation-history entries were read. No primary paper or live taxonomic authority was reopened.

### Occurrence, assay and target boundaries

evidence: supported. Targets: naturalproductmech:mibig-facad00852.

All saved non-MIBiG/non-classifier frames are negative for this owner, including occurrence, assay and target sources. No occurrence, bioactivity or molecular-target root is written. The plant and microbial occurrence placements of roquefortine companions remain those companions’ context and do not establish production or occurrence of this diketopiperazine. No assay sentinel or actual AID is present for this owner.

### Classification and saved topology

consistency: unknown. Targets: naturalproductmech:mibig-facad00852.

The source class Histidine-derived is retained separately from NPClassifier Histidine alkaloids/Small peptides and Dipeptides/Imidazole alkaloids. The six-membered two-amide ring plus imidazole and indole side chains supports a bounded cyclic-dipeptide description; it does not establish absolute configurations, precursor experiments or a complete biosynthetic route. The is_glycoside false prediction is consistent with the absence of a sugar/linkage motif. Two model pathways, Alkaloids and Amino acids and Peptides, correctly produce UNCLASSIFIED under the current filing rule.

### Scientific completion and ownership

completeness: unknown. Targets: naturalproductmech:mibig-facad00852.

The whole selected owner/history, every saved source payload and negative frame, both complete saved molecular forms and actual intake claims have been read. Input hashes and ownership declarations match the accepted plan; this is distinct from reading entire corpus files. Positive conclusions concern retained mapping, source-grade fidelity and bounded encoded topology. Five local checks passed, but full QC/OAK and live authorities are unavailable. No maintained reader applies, so completion remains partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2699-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/histidyltryptophanyldiketopiperazine.yaml; Whole current plaintext, including all curation_history entries | supports | Personally read the complete current owner and history; no fresh primary-source access. |
| support-2699-capture | /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete actual owner with all written claims and absent mechanism/activity roots. |
| support-2699-grounding-owner | /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json; /records/8/owner_document/identifier; /records/8/owner_document/label; /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts; /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes | supports | Exact owner-local full identity, source mappings and any OPEN discussion; no independent natural-identity proof. |
| support-2699-provenance-owner | /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json; /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters; /records/8/owner_document/producer_taxon_groups; /records/8/owner_document/bgc_class | supports | Producer and compound-specific locus assertions retain distinct grades, source routes and citation grain. |
| support-2699-citations-history | /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json; /records/8/owner_document/source_concepts; /records/8/owner_document/biosynthetic_gene_clusters; /records/8/owner_document/curation_history | supports | All retained source concepts, citation-bearing locus fields and whole seeding history. |
| support-2699-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json; /records/8/owner_document | supports | Exact written occurrence and xref placements; absence and occurrence are distinct from production. |
| support-2699-activity-owner | /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete captured owner has no written bioactivity or molecular-target root; bounded retained absence only. |
| support-2699-classification-owner | /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json; /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification; /records/8/owner_document/biosynthesis_origin; /records/8/owner_document/compound_classes; /records/8/owner_document/bgc_class | supports | Literal filing, model predictions and any asserted source compound class are preserved separately. |
| support-2699-intake | /private/tmp/npm-review-work/shared-next-batch270/intakes-001/2699-inspect-001.json; /status; /source; /targets | supports | Original inspection-only input hashes and target ownership declarations; input presence does not imply whole corpus reading. |
| support-2699-intake-execution | /private/tmp/npm-review-work/shared-next-batch270/intakes-001/2699-inspect-execution-001.json; /exit_code; /command; /actual_environment; /stdout; /stderr | supports | Original owner inspection exit 0 with empty stderr. |
| support-2699-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch270/root-intake-acceptance-001.json; /accepted; /summary; /all_expected_maps_exact; /all_stderr_empty | supports | ROOT accepted the ten original intakes and exact 486 placements across 63 paths. |
| support-2699-direct-contexts | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-target-input-plan-001.json; /records/8/proposed_companion_paths; /records/8/direct_companion_predicates; /records/8/identity_comparison_paths; /records/8/additional_context_paths; /records/8/additional_context_roles; /records/8/reader_implementation_paths; /records/8/proposed_input_paths; /records/8/proposed_input_count | supports | Owner-local direct contexts and seven additional diagnostic/implementation roles; no transfer of another owner's source assertions. |
| support-2699-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch270/root-current270-source-plan-acceptance-001.json; /accepted; /status; /plan | supports | ROOT accepted the one original operative source plan. |
| support-2699-source-reading | /private/tmp/npm-review-work/shared-next-batch270-tentative/support-prep/support-current270-assigned-source-reading-001.json; /contexts/11; /selected_source_to_owner_reconciliation; /raw_owner_reading | supports | Personally read this complete saved frame set and all positive dictionaries; current source-to-owner placements reconciled without extra primary credit. |
| support-2699-source-notes | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | supports | Disjoint 16 BGC plus 68 Support primary rows and zero Native source-row credit; blank and negative scope remain explicit. |
| support-2699-taxonomy | /private/tmp/npm-review-work/shared-next-batch270-tentative/native-prep/native-current270-cached-taxonomy-reading-001.json; /context_interpretations/16; /interpretation; /counts | supports | Owner-local cached labels and unresolved strain-spelling scope; no fresh taxonomy or producer authority. |
| support-2699-curation-scope | /private/tmp/npm-review-work/shared-next-batch270-tentative/native-prep/native-current270-implemented-curation-scan-001.json; /counts; /exact_applicability_resolution; /interpretation; /implementation_scope | supports | Exact retained identity/digest predicates establish no applicable correction, exclusion or qualification for this owner; lexical candidates are separate. |
| support-2699-chemistry | /private/tmp/npm-review-work/shared-next-batch270/chemistry-local/diagnostic-DATA-001.json; /records/8 | supports | Complete saved two-form atom/bond/ring/stereo/motif tables, comparisons and existing map for this owner; normalized equality is not natural identity. |
| support-2699-molecular-reading | /private/tmp/npm-review-work/shared-next-batch270-tentative/support-prep/support-current270-last-five-molecular-intake-reading-002.json; /records/3 | supports | Personal whole saved-table reading and form-specific interpretation; no new molecular parse or map. |
| support-2699-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch270/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /warning_lines; /warnings_assigned_to_records | supports | ROOT accepted the original twenty-form diagnostic; two undefined-stereo warnings remain globally unassigned. |
| support-2699-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch270/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic exit 0, two unassigned stderr warnings, no retries or external requests. |
| support-2699-stereo-implementation | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–172 | supports | stereo_complete is computed from source-SMILES FindMolChiralCenters(includeUnassigned=True, useLegacyImplementation=False); it does not certify all double-bond geometry. |
| support-2699-producer-grade-policy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; lines 1–40 | supports | Maintained grade table separates cluster-only heterologous/enzymatic evidence from organism-and-cluster correlation evidence. |
| support-2699-filing-implementation | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295–306 | supports | choose_pathway returns UNCLASSIFIED for zero or multiple model pathway labels; a single supported label is the separate branch. |
| support-2699-native-gates | /private/tmp/npm-review-work/shared-next-batch270/root-native-gates-acceptance-001.json; /accepted; /five_local_commands_passed; /all_required_native_gates_passed; /unavailable_required_gates; /queue | supports | Five local child commands passed once, with no preflight failure or child repeat. Full QC/OAK are unavailable and queue rows remain leads. |
| support-2699-reader-applicability | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-selected-mechanism-profile-001.json; /mechanisms; /selected_reader_orders | supports | No literal selected mechanism/component roots and no maintained reader applies. |
| support-2699-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds predicate and full payloads for 1 placements; negatives are finite and rows are not independent experiments. |
| support-2699-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Complete physical row chunks/dictionaries at /contexts/16/source_scope_inventory/joins/mibig_compounds/matches in the pinned inventory; physical_line, last_physical_line and row_sha256 preserved there | supports | Retained table backing all personally read positive fields; exact physical joins are retained in the source-reading receipt. |
| support-2699-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2699-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2699-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2699-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier predicate and full payloads for 1 placements; negatives are finite and rows are not independent experiments. |
| support-2699-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Complete physical row chunks/dictionaries at /contexts/16/source_scope_inventory/joins/npclassifier/matches in the pinned inventory; physical_line, last_physical_line and row_sha256 preserved there | supports | Retained table backing all personally read positive fields; exact physical joins are retained in the source-reading receipt. |
| support-2699-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2699-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2699-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2699-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2699-taxon-query-scope | /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/source_taxa; /contexts/16/source_scope_inventory/forward_taxon_merge_matches; /contexts/16/source_scope_inventory/nonorganism_matches | supports | Exact owner-local taxon routes and retained diagnostic negatives; no companion route or independent decision is inferred. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-270/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-270/native-current270-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-270/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-270/native-current270-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-270/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-270/native-current270-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-270/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-270/native-current270-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-270/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-270/native-current270-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained owner, source rows and saved diagnostics only; no fresh primary-paper, taxonomy, sequence or external identifier resolution.
- Histidyltryptophanyldiketopiperazine retains two undefined atom centers and empty cross-form mapping. StandardInChI/key agreement does not prove a unique solution tautomer, natural stereochemistry or full fixed-form graph identity.
- Two undefined-stereo warnings remain unassigned to owners. Full QC and OAK are unavailable; recorded grades, citation grain, model predictions and existing source discussions retain their stated limits.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- The complete owner/history, both saved molecular tables and all owner-local saved query frames were personally read. Physical row placements are not independent experiments and input hash verification is not whole-corpus scientific reading.
- This review proposes no source, generated record, curation status or history edit. No outbound request, new molecular parse or target execution was performed in this authoring lane.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T102656Z-histidyltryptophanyldiketopiperazine
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: histidyltryptophanyldiketopiperazine'
started_at: '2026-11-06T09:35:23.177066Z'
finished_at: '2026-11-06T10:26:56.840865Z'
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
summary: Histidyltryptophanyldiketopiperazine supports a qualified pass for faithful
  source mapping and graded producer/locus evidence. The cyclic dipeptide, imidazole
  and indole topology is explicit, but two atom centers remain unspecified and the
  stored forms differ in amide/imidic and imidazole proton placement. Normalized identifier
  agreement does not resolve those fixed-form or natural-stereochemistry limits.
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
  - path: data/natural_products/alkaloids/dehydrohistidyltryptophanyldiketopiperazine.yaml
    sha256: 2c289074bbcca634022e442b51bd80bf9aff59948d35d1f37fd051a3aca3a37a
    role: context
  - path: data/natural_products/alkaloids/glandicoline-a.yaml
    sha256: 661c320e2d349c03e909e5b1b4a3cf9e01680d67f3a4e5890c5b3525ccdc9f19
    role: context
  - path: data/natural_products/alkaloids/glandicoline-b.yaml
    sha256: 73ca2e9fb9294c499e06f695a510a2b27a83365aeffa173cce8b2484f7a9b2e9
    role: context
  - path: data/natural_products/alkaloids/meleagrine.yaml
    sha256: 1b00a87404a9dcdc1353fc84b465fcd49401f0a75ecabf1032d0692ab0beb765
    role: context
  - path: data/natural_products/unclassified/histidyltryptophanyldiketopiperazine.yaml
    sha256: 2e5946c1c8ed3a099a11a94c0fc3e600bcd9006122ea8540874fc3fb385bd6c2
    role: target
  - path: data/natural_products/unclassified/roquefortine-c.yaml
    sha256: f98ea7187781309e0d91e8dca48059b61614ae5ad84053d7421df823446af839
    role: context
  - path: data/natural_products/unclassified/roquefortine-d.yaml
    sha256: 9b50d017574e3499ae09e49220ad243c027b9240f1fa7799713df0fd6006be67
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
  selection: Campaign path order 2699; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-facad00852
targets:
- target_id: naturalproductmech:mibig-facad00852
  path: data/natural_products/unclassified/histidyltryptophanyldiketopiperazine.yaml
  label: histidyltryptophanyldiketopiperazine
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch270/chemistry-local/diagnose270-001.py
    0fcfd99adbd7baf3a7a789eda6114c021185565822c1106c7687617ba87c402c 424299f29d004cc005641f23fd43c53cac13aa1014c75ce0c398dca3bc8f2341
    0df48a006d66faa945cfa3819428578f279112f61b9b8f3725cafa5fad7cca60
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The original diagnostic parsed both stored forms; formula, charge, StandardInChI
    and full key agree within this owner.
  scope_note: Original shared twenty-form execution, no rerun. Both owner canonical
    SMILES comparison flags are false; the other eight are true, with an empty saved
    map and an amide/imidic-OH representation difference. The full-identity flag remains
    false and two stderr warnings are globally unassigned. A passed execution does
    not establish full graph or natural identity.
  target_ids:
  - naturalproductmech:mibig-facad00852
  evidence_ids:
  - support-2699-chemistry
  - support-2699-diagnostic-acceptance
  - support-2699-diagnostic-execution
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-facad00852
  command: just validate-strict data/natural_products/unclassified/heronamide-d.yaml
    data/natural_products/unclassified/heronamide-e.yaml data/natural_products/unclassified/heronamide-f.yaml
    data/natural_products/unclassified/higginsianin-a.yaml data/natural_products/unclassified/higginsianin-b.yaml
    data/natural_products/unclassified/higginsianin-c.yaml data/natural_products/unclassified/higginsianin-d.yaml
    data/natural_products/unclassified/higginsianin-e.yaml data/natural_products/unclassified/histidyltryptophanyldiketopiperazine.yaml
    data/natural_products/unclassified/hitachimycin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-270/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-facad00852
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-270/validate-all-001.tsv
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
  - naturalproductmech:mibig-facad00852
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
  - naturalproductmech:mibig-facad00852
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
  - naturalproductmech:mibig-facad00852
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-270/review-queue-001.tsv
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
  - naturalproductmech:mibig-facad00852
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-facad00852
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-facad00852
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2699-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/histidyltryptophanyldiketopiperazine.yaml
  locator: Whole current plaintext, including all curation_history entries
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Personally read the complete current owner and history; no fresh primary-source
    access.
  snapshot_sha256: 2e5946c1c8ed3a099a11a94c0fc3e600bcd9006122ea8540874fc3fb385bd6c2
- evidence_id: support-2699-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete actual owner with all written claims and absent mechanism/activity
    roots.
  snapshot_sha256: 424299f29d004cc005641f23fd43c53cac13aa1014c75ce0c398dca3bc8f2341
- evidence_id: support-2699-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json
  locator: /records/8/owner_document/identifier; /records/8/owner_document/label;
    /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts;
    /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Exact owner-local full identity, source mappings and any OPEN discussion;
    no independent natural-identity proof.
  snapshot_sha256: 424299f29d004cc005641f23fd43c53cac13aa1014c75ce0c398dca3bc8f2341
- evidence_id: support-2699-provenance-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json
  locator: /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters;
    /records/8/owner_document/producer_taxon_groups; /records/8/owner_document/bgc_class
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Producer and compound-specific locus assertions retain distinct grades,
    source routes and citation grain.
  snapshot_sha256: 424299f29d004cc005641f23fd43c53cac13aa1014c75ce0c398dca3bc8f2341
- evidence_id: support-2699-citations-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json
  locator: /records/8/owner_document/source_concepts; /records/8/owner_document/biosynthetic_gene_clusters;
    /records/8/owner_document/curation_history
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: All retained source concepts, citation-bearing locus fields and whole seeding
    history.
  snapshot_sha256: 424299f29d004cc005641f23fd43c53cac13aa1014c75ce0c398dca3bc8f2341
- evidence_id: support-2699-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Exact written occurrence and xref placements; absence and occurrence are
    distinct from production.
  snapshot_sha256: 424299f29d004cc005641f23fd43c53cac13aa1014c75ce0c398dca3bc8f2341
- evidence_id: support-2699-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete captured owner has no written bioactivity or molecular-target
    root; bounded retained absence only.
  snapshot_sha256: 424299f29d004cc005641f23fd43c53cac13aa1014c75ce0c398dca3bc8f2341
- evidence_id: support-2699-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270/owner-capture-DATA-001.json
  locator: /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification;
    /records/8/owner_document/biosynthesis_origin; /records/8/owner_document/compound_classes;
    /records/8/owner_document/bgc_class
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Literal filing, model predictions and any asserted source compound class
    are preserved separately.
  snapshot_sha256: 424299f29d004cc005641f23fd43c53cac13aa1014c75ce0c398dca3bc8f2341
- evidence_id: support-2699-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch270/intakes-001/2699-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Original inspection-only input hashes and target ownership declarations;
    input presence does not imply whole corpus reading.
  snapshot_sha256: cab2ad147241fb180e14f00a2587de8754c8ea1867cafaa1012882207b28e688
- evidence_id: support-2699-intake-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch270/intakes-001/2699-inspect-execution-001.json
  locator: /exit_code; /command; /actual_environment; /stdout; /stderr
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Original owner inspection exit 0 with empty stderr.
  snapshot_sha256: 809ef873133484ae3480c52f2110e04e317404a5461a9a34cca89dcd37371996
- evidence_id: support-2699-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch270/root-intake-acceptance-001.json
  locator: /accepted; /summary; /all_expected_maps_exact; /all_stderr_empty
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: ROOT accepted the ten original intakes and exact 486 placements across
    63 paths.
  snapshot_sha256: 711c49c78686735079fdd177c6097a42d20802cd262a2fc6c60017f8170ec8ad
- evidence_id: support-2699-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-target-input-plan-001.json
  locator: /records/8/proposed_companion_paths; /records/8/direct_companion_predicates;
    /records/8/identity_comparison_paths; /records/8/additional_context_paths; /records/8/additional_context_roles;
    /records/8/reader_implementation_paths; /records/8/proposed_input_paths; /records/8/proposed_input_count
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Owner-local direct contexts and seven additional diagnostic/implementation
    roles; no transfer of another owner's source assertions.
  snapshot_sha256: ebab7ef6d59deb4089bb7c69b60e7ef49c3f4d8fafab471c45c20cddd6f8bf7b
- evidence_id: support-2699-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch270/root-current270-source-plan-acceptance-001.json
  locator: /accepted; /status; /plan
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: ROOT accepted the one original operative source plan.
  snapshot_sha256: 2214b51c7ceb1adcbf95fb461e42f0b895e2007bb6031e3e14b8fe76e94d603d
- evidence_id: support-2699-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/support-prep/support-current270-assigned-source-reading-001.json
  locator: /contexts/11; /selected_source_to_owner_reconciliation; /raw_owner_reading
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Personally read this complete saved frame set and all positive dictionaries;
    current source-to-owner placements reconciled without extra primary credit.
  snapshot_sha256: 261ab50bfa6bfa006fdbdfb224ec7e704828ac02c182857e710ee6ba16e3cc74
- evidence_id: support-2699-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Disjoint 16 BGC plus 68 Support primary rows and zero Native source-row
    credit; blank and negative scope remain explicit.
  snapshot_sha256: cf6ace22ab6353112a95583500316678a0a768eecbc85f3dca27545c9a889b2a
- evidence_id: support-2699-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/native-prep/native-current270-cached-taxonomy-reading-001.json
  locator: /context_interpretations/16; /interpretation; /counts
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Owner-local cached labels and unresolved strain-spelling scope; no fresh
    taxonomy or producer authority.
  snapshot_sha256: 1d91c744ef017e7118ec618441ab147ce413124a40fc5b8bf5fd401c74075a1f
- evidence_id: support-2699-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/native-prep/native-current270-implemented-curation-scan-001.json
  locator: /counts; /exact_applicability_resolution; /interpretation; /implementation_scope
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Exact retained identity/digest predicates establish no applicable correction,
    exclusion or qualification for this owner; lexical candidates are separate.
  snapshot_sha256: 1127375862acc6fee4accf633cdbce7e86b921db8d253c2f54cf629edb888e17
  search_scope: '{"owner": "data/natural_products/unclassified/histidyltryptophanyldiketopiperazine.yaml",
    "primary_source_rows": 0, "scope": "Retained finite identity/digest and source-row
    predicates; no new source query"}'
- evidence_id: support-2699-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch270/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete saved two-form atom/bond/ring/stereo/motif tables, comparisons
    and existing map for this owner; normalized equality is not natural identity.
  snapshot_sha256: d4bb13f243c5e57f7159ada0915b2cc2897a436e530e42c2a181fb87692554e9
- evidence_id: support-2699-molecular-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/support-prep/support-current270-last-five-molecular-intake-reading-002.json
  locator: /records/3
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Personal whole saved-table reading and form-specific interpretation; no
    new molecular parse or map.
  snapshot_sha256: c523c06e8d44cf752e2413837f45334426e6e748ca3913a97ec6dc08d6aca9e5
- evidence_id: support-2699-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch270/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /warning_lines; /warnings_assigned_to_records
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: ROOT accepted the original twenty-form diagnostic; two undefined-stereo
    warnings remain globally unassigned.
  snapshot_sha256: 14f71b9287494b128c01d41895b04c739bcd01ad65939dab865e04d4a0a5d45f
- evidence_id: support-2699-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch270/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Original diagnostic exit 0, two unassigned stderr warnings, no retries
    or external requests.
  snapshot_sha256: 83e309ab06d72a548dc652104c5096b4246a1c112b1f7b59e77490dc39d7003e
- evidence_id: support-2699-stereo-implementation
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–172
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: stereo_complete is computed from source-SMILES FindMolChiralCenters(includeUnassigned=True,
    useLegacyImplementation=False); it does not certify all double-bond geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2699-producer-grade-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: lines 1–40
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Maintained grade table separates cluster-only heterologous/enzymatic evidence
    from organism-and-cluster correlation evidence.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2699-filing-implementation
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295–306
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: choose_pathway returns UNCLASSIFIED for zero or multiple model pathway
    labels; a single supported label is the separate branch.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2699-native-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch270/root-native-gates-acceptance-001.json
  locator: /accepted; /five_local_commands_passed; /all_required_native_gates_passed;
    /unavailable_required_gates; /queue
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Five local child commands passed once, with no preflight failure or child
    repeat. Full QC/OAK are unavailable and queue rows remain leads.
  snapshot_sha256: 60e5f7308774d6eb141dd987554eae3b555d2fe83a6f01629ad316aa746c0656
- evidence_id: support-2699-reader-applicability
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-selected-mechanism-profile-001.json
  locator: /mechanisms; /selected_reader_orders
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: No literal selected mechanism/component roots and no maintained reader
    applies.
  snapshot_sha256: e84cfb7c5e610154f1b2a0438ae4623ebb15e2a5194e5c6c08f04ba505637ebb
- evidence_id: support-2699-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete saved mibig_compounds predicate and full payloads for 1 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 8343a4e91faeb21b99ea043033d63770bea557285cd08bd70f6f9cb9808e9fb8
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "YNHVZXATNGMVNC-UHFFFAOYSA-N"}'
- evidence_id: support-2699-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Complete physical row chunks/dictionaries at /contexts/16/source_scope_inventory/joins/mibig_compounds/matches
    in the pinned inventory; physical_line, last_physical_line and row_sha256 preserved
    there
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Retained table backing all personally read positive fields; exact physical
    joins are retained in the source-reading receipt.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2699-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete saved chebi_structures predicate and full payloads for 0 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 8343a4e91faeb21b99ea043033d63770bea557285cd08bd70f6f9cb9808e9fb8
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "YNHVZXATNGMVNC-UHFFFAOYSA-N"}'
- evidence_id: support-2699-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete saved lotus_occurrences predicate and full payloads for 0 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 8343a4e91faeb21b99ea043033d63770bea557285cd08bd70f6f9cb9808e9fb8
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "YNHVZXATNGMVNC-UHFFFAOYSA-N"}'
- evidence_id: support-2699-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences predicate and full payloads for 0
    placements; negatives are finite and rows are not independent experiments.
  snapshot_sha256: 8343a4e91faeb21b99ea043033d63770bea557285cd08bd70f6f9cb9808e9fb8
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "YNHVZXATNGMVNC-UHFFFAOYSA-N"}'
- evidence_id: support-2699-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete saved npclassifier predicate and full payloads for 1 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 8343a4e91faeb21b99ea043033d63770bea557285cd08bd70f6f9cb9808e9fb8
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "YNHVZXATNGMVNC-UHFFFAOYSA-N"}'
- evidence_id: support-2699-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Complete physical row chunks/dictionaries at /contexts/16/source_scope_inventory/joins/npclassifier/matches
    in the pinned inventory; physical_line, last_physical_line and row_sha256 preserved
    there
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Retained table backing all personally read positive fields; exact physical
    joins are retained in the source-reading receipt.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2699-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete saved pubchem_bioassay predicate and full payloads for 0 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 8343a4e91faeb21b99ea043033d63770bea557285cd08bd70f6f9cb9808e9fb8
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "YNHVZXATNGMVNC-UHFFFAOYSA-N"}'
- evidence_id: support-2699-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete saved bindingdb_targets predicate and full payloads for 0 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 8343a4e91faeb21b99ea043033d63770bea557285cd08bd70f6f9cb9808e9fb8
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "YNHVZXATNGMVNC-UHFFFAOYSA-N"}'
- evidence_id: support-2699-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys predicate and full payloads for
    0 placements; negatives are finite and rows are not independent experiments.
  snapshot_sha256: 8343a4e91faeb21b99ea043033d63770bea557285cd08bd70f6f9cb9808e9fb8
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "YNHVZXATNGMVNC-UHFFFAOYSA-N"}'
- evidence_id: support-2699-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Complete saved chebi_origins predicate and full payloads for 0 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 8343a4e91faeb21b99ea043033d63770bea557285cd08bd70f6f9cb9808e9fb8
  search_scope: '{"matched_placements": 0, "predicate": "exact chebi_id from exact
    full-key structure rows", "query": []}'
- evidence_id: support-2699-taxon-query-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch270-tentative/bgc-prep/bgc-conditional270-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/source_taxa; /contexts/16/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/16/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-06T10:21:26.334213Z'
  support: supports
  summary: Exact owner-local taxon routes and retained diagnostic negatives; no companion
    route or independent decision is inferred.
  snapshot_sha256: 8343a4e91faeb21b99ea043033d63770bea557285cd08bd70f6f9cb9808e9fb8
  search_scope: '{"forward_merge_placements": 0, "nonorganism_placements": 0, "source_taxa":
    ["NCBITaxon:500485"]}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-270/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-270/native-current270-five-gates-execution-001.json
  accessed_at: '2026-11-06T09:43:06.501056Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 8a9e9811aa37002400febfda7942cdaf92486c0b6c9951792c2a9fc68f1d70f3
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-270/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-270/native-current270-five-gates-execution-001.json
  accessed_at: '2026-11-06T09:43:31.196726Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 809b678602c7fcea1b9a1674b29fb5409704c1e66c6d66df16f1333384214724
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-270/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-270/native-current270-five-gates-execution-001.json
  accessed_at: '2026-11-06T09:43:50.420191Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-270/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-270/native-current270-five-gates-execution-001.json
  accessed_at: '2026-11-06T09:44:24.146239Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-270/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-270/native-current270-five-gates-execution-001.json
  accessed_at: '2026-11-06T09:44:35.749562Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 734c8f9370ca88fb6e7a20cc6b2a0078f4e7df3c22d87f879eeca1cf4ab4f1d1
assessments:
- area: identity
  topic: Retained identity and grounding
  dimensions:
  - name: standard_inchi_key
    definition: Exact full key; no prefix or name substitution.
    value: YNHVZXATNGMVNC-UHFFFAOYSA-N
    evidence_ids:
    - support-2699-grounding-owner
    - support-2699-chemistry
    - support-2699-query-mibig_compounds
    - support-2699-query-chebi_structures
    - support-2699-direct-contexts
    - support-2699-source-reading
  - name: grounding_scope
    definition: Stored grounding fidelity is distinct from fresh natural-identity
      verification.
    value: MINTED retained mapping; no independent natural-identity proof
    evidence_ids:
    - support-2699-grounding-owner
    - support-2699-chemistry
    - support-2699-query-mibig_compounds
    - support-2699-query-chebi_structures
    - support-2699-direct-contexts
    - support-2699-source-reading
  assessment_id: support-2699-identity
  target_ids:
  - naturalproductmech:mibig-facad00852
  evidence_ids:
  - support-2699-grounding-owner
  - support-2699-chemistry
  - support-2699-query-mibig_compounds
  - support-2699-query-chebi_structures
  - support-2699-direct-contexts
  - support-2699-source-reading
  outcome: supported
  summary: The minted identifier and exact YNHVZXATNGMVNC-UHFFFAOYSA-N key retain
    the BGC0000420 version 5 compound placement. No database identifiers are provided
    in that source row and no owner xrefs are written; the exact-key ChEBI frame is
    also empty. The six shared-BGC companions are diagnostic context only. In particular,
    glandicoline B and meleagrine mechanism roots do not become this selected owner’s
    mechanism or evidence. Both original stored forms regenerate the declared StandardInChI
    and full key; that supports retained mapping without independent natural-identity
    proof.
- area: representation
  topic: Stored forms and stereochemistry
  dimensions:
  - name: stereochemistry_scope
    definition: Saved original atom-center and double-bond scope; no natural stereochemistry
      proof.
    value: Two unspecified tetrahedral centers in both forms; source stereo_complete
      false; no potential double stereo listed
    evidence_ids:
    - support-2699-grounding-owner
    - support-2699-chemistry
    - support-2699-molecular-reading
    - support-2699-diagnostic-acceptance
    - support-2699-diagnostic-execution
    - support-2699-stereo-implementation
  - name: representation_correspondence
    definition: Normalized InChI/key agreement does not prove full fixed-form graph
      equivalence.
    value: Eight flags true and both canonical flags false; empty map; two amide/imidic
      sites and imidazole proton relocation
    evidence_ids:
    - support-2699-grounding-owner
    - support-2699-chemistry
    - support-2699-molecular-reading
    - support-2699-diagnostic-acceptance
    - support-2699-diagnostic-execution
    - support-2699-stereo-implementation
  assessment_id: support-2699-representation
  target_ids:
  - naturalproductmech:mibig-facad00852
  evidence_ids:
  - support-2699-grounding-owner
  - support-2699-chemistry
  - support-2699-molecular-reading
  - support-2699-diagnostic-acceptance
  - support-2699-diagnostic-execution
  - support-2699-stereo-implementation
  outcome: supported
  summary: Both saved forms have C17H17N5O2, 24 atoms, 27 bonds and four rings of
    sizes 6, 5, 6 and 5, with zero net and individual atom charge. Formula, charge,
    StandardInChI and full-key comparisons agree, but both canonical SMILES comparisons
    are false and the saved map is empty; full_graph_identity_established is false.
    Source carbonyls C1=O0 and C22=O23 are attached to ring nitrogens N14 and N3,
    giving the two diketopiperazine amide sites. In the InChI form, C15=N21/O22H and
    C16=N20/O23H replace them; both hydroxyl oxygens have degree one and H1, while
    the imine nitrogens have H0. The imidazole [nH] location also changes between
    the canonical forms. Two unspecified tetrahedral centers persist (source 2 and
    15; InChI 13 and 14), agreeing with stereo_complete false. Neither new ring C=N
    is listed as potential double-bond stereo. No ester, candidate C5O ring or glycosidic
    linkage is established. Two warnings in the original shared stderr stream are
    globally unassigned; none is attributed to this owner.
- area: provenance
  topic: Producer, taxonomy and locus grades
  dimensions:
  - name: taxon_scope
    definition: Cached IDs/names/synonyms are distinct from verified rank, lineage
      or strain identity.
    value: Only selected producer strain 500485; companion occurrence/target identities
      do not transfer
    evidence_ids:
    - support-2699-provenance-owner
    - support-2699-taxonomy
    - support-2699-taxon-query-scope
    - support-2699-curation-scope
    - support-2699-producer-grade-policy
    - support-2699-query-mibig_compounds
  - name: producer_evidence
    definition: Retained producer grade, not inferred from occurrence or locus association.
    value: BGC_CHARACTERIZED from retained knock-out-study source evidence
    evidence_ids:
    - support-2699-provenance-owner
    - support-2699-taxonomy
    - support-2699-taxon-query-scope
    - support-2699-curation-scope
    - support-2699-producer-grade-policy
    - support-2699-query-mibig_compounds
  - name: locus_evidence
    definition: Retained compound-specific cluster-link grade and source methods.
    value: CLUSTER_DEMONSTRATED; AM920436.1 3,638,081–3,658,739; questionable quality
      and complete source entry
    evidence_ids:
    - support-2699-provenance-owner
    - support-2699-taxonomy
    - support-2699-taxon-query-scope
    - support-2699-curation-scope
    - support-2699-producer-grade-policy
    - support-2699-query-mibig_compounds
  assessment_id: support-2699-provenance
  target_ids:
  - naturalproductmech:mibig-facad00852
  evidence_ids:
  - support-2699-provenance-owner
  - support-2699-taxonomy
  - support-2699-taxon-query-scope
  - support-2699-curation-scope
  - support-2699-producer-grade-policy
  - support-2699-query-mibig_compounds
  outcome: supported
  summary: Penicillium rubens Wisconsin 54-1255, NCBITaxon:500485, retains BGC_CHARACTERIZED
    producer evidence from the stated knock-out studies. The separate BGC0000420 locus
    link is CLUSTER_DEMONSTRATED at AM920436.1, coordinates 3,638,081–3,658,739, with
    NRPS source classification. The version 5 entry is active, questionable in quality
    and complete in source completeness. That source metadata and the maintained grade
    table support the retained grades, without constituting an independent rereading
    of the experiment or a complete enzymatic route.
- area: evidence
  topic: Citation and history scope
  dimensions:
  - name: citation_scope
    definition: Exact retained citation basis; no implied new primary-source access.
    value: COMPOUND_EVIDENCE DOI 10.1002/cbic.201402686; no fresh paper access
    evidence_ids:
    - support-2699-citations-history
    - support-2699-source-reading
    - support-2699-source-notes
    - support-2699-source-mibig_compounds
    - support-2699-source-npclassifier
    - support-2699-query-mibig_compounds
    - support-2699-query-chebi_structures
    - support-2699-query-lotus_occurrences
    - support-2699-query-cyanometdb_occurrences
    - support-2699-query-npclassifier
    - support-2699-query-pubchem_bioassay
    - support-2699-query-bindingdb_targets
    - support-2699-query-antibioticmech_inchikeys
    - support-2699-query-chebi_origins
  assessment_id: support-2699-citations
  target_ids:
  - naturalproductmech:mibig-facad00852
  evidence_ids:
  - support-2699-citations-history
  - support-2699-source-reading
  - support-2699-source-notes
  - support-2699-source-mibig_compounds
  - support-2699-source-npclassifier
  - support-2699-query-mibig_compounds
  - support-2699-query-chebi_structures
  - support-2699-query-lotus_occurrences
  - support-2699-query-cyanometdb_occurrences
  - support-2699-query-npclassifier
  - support-2699-query-pubchem_bioassay
  - support-2699-query-bindingdb_targets
  - support-2699-query-antibioticmech_inchikeys
  - support-2699-query-chebi_origins
  outcome: supported
  summary: DOI:10.1002/cbic.201402686 is retained at COMPOUND_EVIDENCE grain for this
    exact compound placement. It is not promoted from an entry-level citation or borrowed
    from another shared-BGC owner. Both curation-history entries were read. No primary
    paper or live taxonomic authority was reopened.
- area: evidence
  topic: Occurrence, assay and target boundaries
  dimensions:
  - name: occurrence_scope
    definition: Source placements and shared citations are not independent production
      experiments.
    value: No selected occurrence rows; companion plant/microbial placements remain
      context only
    evidence_ids:
    - support-2699-occurrence-owner
    - support-2699-activity-owner
    - support-2699-source-reading
    - support-2699-curation-scope
    - support-2699-taxon-query-scope
    - support-2699-source-mibig_compounds
    - support-2699-source-npclassifier
    - support-2699-query-mibig_compounds
    - support-2699-query-chebi_structures
    - support-2699-query-lotus_occurrences
    - support-2699-query-cyanometdb_occurrences
    - support-2699-query-npclassifier
    - support-2699-query-pubchem_bioassay
    - support-2699-query-bindingdb_targets
    - support-2699-query-antibioticmech_inchikeys
    - support-2699-query-chebi_origins
  - name: assay_target_scope
    definition: Actual AIDs, blank sentinels and bounded negative target queries remain
      distinct.
    value: No actual assay, blank sentinel or target-source positive within retained
      selected scope
    evidence_ids:
    - support-2699-occurrence-owner
    - support-2699-activity-owner
    - support-2699-source-reading
    - support-2699-curation-scope
    - support-2699-taxon-query-scope
    - support-2699-source-mibig_compounds
    - support-2699-source-npclassifier
    - support-2699-query-mibig_compounds
    - support-2699-query-chebi_structures
    - support-2699-query-lotus_occurrences
    - support-2699-query-cyanometdb_occurrences
    - support-2699-query-npclassifier
    - support-2699-query-pubchem_bioassay
    - support-2699-query-bindingdb_targets
    - support-2699-query-antibioticmech_inchikeys
    - support-2699-query-chebi_origins
  assessment_id: support-2699-occurrence-activity
  target_ids:
  - naturalproductmech:mibig-facad00852
  evidence_ids:
  - support-2699-occurrence-owner
  - support-2699-activity-owner
  - support-2699-source-reading
  - support-2699-curation-scope
  - support-2699-taxon-query-scope
  - support-2699-source-mibig_compounds
  - support-2699-source-npclassifier
  - support-2699-query-mibig_compounds
  - support-2699-query-chebi_structures
  - support-2699-query-lotus_occurrences
  - support-2699-query-cyanometdb_occurrences
  - support-2699-query-npclassifier
  - support-2699-query-pubchem_bioassay
  - support-2699-query-bindingdb_targets
  - support-2699-query-antibioticmech_inchikeys
  - support-2699-query-chebi_origins
  outcome: supported
  summary: All saved non-MIBiG/non-classifier frames are negative for this owner,
    including occurrence, assay and target sources. No occurrence, bioactivity or
    molecular-target root is written. The plant and microbial occurrence placements
    of roquefortine companions remain those companions’ context and do not establish
    production or occurrence of this diketopiperazine. No assay sentinel or actual
    AID is present for this owner.
- area: consistency
  topic: Classification and saved topology
  dimensions:
  - name: classification_applicability
    definition: Local encoded topology can support a broad description without validating
      a model-derived pathway or natural identity.
    value: Cyclic dipeptide/imidazole topology supported; full family/route qualification
      remains unknown; two-label UNCLASSIFIED filing correct
    evidence_ids:
    - support-2699-classification-owner
    - support-2699-chemistry
    - support-2699-molecular-reading
    - support-2699-filing-implementation
    - support-2699-query-npclassifier
    - support-2699-query-mibig_compounds
  assessment_id: support-2699-classification
  target_ids:
  - naturalproductmech:mibig-facad00852
  evidence_ids:
  - support-2699-classification-owner
  - support-2699-chemistry
  - support-2699-molecular-reading
  - support-2699-filing-implementation
  - support-2699-query-npclassifier
  - support-2699-query-mibig_compounds
  outcome: unknown
  summary: The source class Histidine-derived is retained separately from NPClassifier
    Histidine alkaloids/Small peptides and Dipeptides/Imidazole alkaloids. The six-membered
    two-amide ring plus imidazole and indole side chains supports a bounded cyclic-dipeptide
    description; it does not establish absolute configurations, precursor experiments
    or a complete biosynthetic route. The is_glycoside false prediction is consistent
    with the absence of a sugar/linkage motif. Two model pathways, Alkaloids and Amino
    acids and Peptides, correctly produce UNCLASSIFIED under the current filing rule.
- area: completeness
  topic: Scientific completion and ownership
  dimensions:
  - name: review_completion
    definition: Coverage of a whole record is distinct from all required checks and
      independent external verification.
    value: partial; five local gates passed; QC/OAK and live authorities unavailable;
      no applicable reader
    evidence_ids:
    - support-2699-owner
    - support-2699-capture
    - support-2699-intake
    - support-2699-intake-execution
    - support-2699-intake-acceptance
    - support-2699-plan-acceptance
    - support-2699-source-reading
    - support-2699-source-notes
    - support-2699-diagnostic-acceptance
    - support-2699-molecular-reading
    - support-2699-native-gates
    - support-2699-reader-applicability
  assessment_id: support-2699-completion
  target_ids:
  - naturalproductmech:mibig-facad00852
  evidence_ids:
  - support-2699-owner
  - support-2699-capture
  - support-2699-intake
  - support-2699-intake-execution
  - support-2699-intake-acceptance
  - support-2699-plan-acceptance
  - support-2699-source-reading
  - support-2699-source-notes
  - support-2699-diagnostic-acceptance
  - support-2699-molecular-reading
  - support-2699-native-gates
  - support-2699-reader-applicability
  outcome: unknown
  summary: The whole selected owner/history, every saved source payload and negative
    frame, both complete saved molecular forms and actual intake claims have been
    read. Input hashes and ownership declarations match the accepted plan; this is
    distinct from reading entire corpus files. Positive conclusions concern retained
    mapping, source-grade fidelity and bounded encoded topology. Five local checks
    passed, but full QC/OAK and live authorities are unavailable. No maintained reader
    applies, so completion remains partial.
findings: []
actions: []
limitations:
- Retained owner, source rows and saved diagnostics only; no fresh primary-paper,
  taxonomy, sequence or external identifier resolution.
- Histidyltryptophanyldiketopiperazine retains two undefined atom centers and empty
  cross-form mapping. StandardInChI/key agreement does not prove a unique solution
  tautomer, natural stereochemistry or full fixed-form graph identity.
- Two undefined-stereo warnings remain unassigned to owners. Full QC and OAK are unavailable;
  recorded grades, citation grain, model predictions and existing source discussions
  retain their stated limits.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- The complete owner/history, both saved molecular tables and all owner-local saved
  query frames were personally read. Physical row placements are not independent experiments
  and input hash verification is not whole-corpus scientific reading.
- This review proposes no source, generated record, curation status or history edit.
  No outbound request, new molecular parse or target execution was performed in this
  authoring lane.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-270
```
