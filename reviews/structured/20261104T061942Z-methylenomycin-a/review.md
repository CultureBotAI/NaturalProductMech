# Local evidence review: methylenomycin A

- Review: 20261104T061942Z-methylenomycin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T05:39:54.333765Z
- Finished UTC: 2026-11-04T06:19:42.026997Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The retained methylenomycin A structure and source identifier are locally consistent, with an explicitly limited source-only producer claim and 24 cited occurrence placements. The saved molecular forms describe the same epoxy cyclopentanone carboxylic acid at three specified tetrahedral centers. Neither the versioned Terpenoids prediction nor the diagnostic's composite C5O cycle establishes biosynthetic origin or a sugar residue. Natural identity, primary citations, source activity and current external grounding remain unverified; this is a qualified partial review.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2356; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-697eb70f76 | data/natural_products/terpenoids/methylenomycin-a.yaml | generated | methylenomycin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-697eb70f76 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-697eb70f76 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-697eb70f76 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-697eb70f76 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-697eb70f76 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-697eb70f76 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-697eb70f76 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-697eb70f76 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained structure and identifier correspondence

identity: supported. Targets: naturalproductmech:mibig-697eb70f76.

The exact target is minted naturalproductmech:mibig-697eb70f76, full key HBECYYFDLZZMPL-WLGLDCGKSA-N, with source concept BGC0000914 version 5 and retained NPAtlas xref NPA013552. The locally captured source structure, identifier and label agree with their saved inventory row. No exact-key ChEBI match is returned by the retained query; that is bounded snapshot scope, not proof that no such concept exists. Both original stored-form diagnostics reproduce the declared key and canonical representations. The NPAtlas link and the natural compound denoted by the label were not freshly resolved, and standardized agreement is not independent experimental identity proof.

### Stored representation and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-697eb70f76.

Both stored forms parse to neutral C9H10O4 with 13 heavy atoms and 14 bonds. The complete tables show an epoxide sharing its carbon-carbon edge with a five-membered carbocycle, a ring ketone, an exocyclic methylene and a carboxylic acid. The SMILES centers 1S, 3S and 9R map to the saved InChI centers 7S, 8S and 4R; both potential-stereo tables contain three specified tetrahedral centers. All ten comparison flags are true, but the saved correspondence is only one chirality-aware substructure match and explicitly does not establish independent full-graph or natural identity. The motif's six-membered C5O perimeter [1,2,3,5,7,9] traverses the epoxide oxygen and the longer cyclopentanone path; the direct 1-3 carbon bond remains. This composite cycle is not an identified sugar residue or glycosidic linkage. The source stereo flag is a retained extractor result, not a new determination of natural stereochemistry.

### Producer and locus evidence

provenance: supported. Targets: naturalproductmech:mibig-697eb70f76.

BGC0000914 version 5 is retained as active with questionable quality and unknown completeness metadata, OTHER class, and Streptomyces coelicolor A3(2), NCBITaxon:100226. Producer SOURCE_ASSERTION and locus CLUSTER_UNSTATED remain distinct: no locus method is stated in this saved row. Those values support faithful local attribution, not newly demonstrated biosynthesis. Quality and completeness metadata do not independently certify or refute the science. Occurrence taxa S. albidoflavus, S. coelicolor and S. violaceoruber are separate retained occurrence claims; species or strain labels and shared citations cannot upgrade producer evidence.

### Citation roles

evidence: supported. Targets: naturalproductmech:mibig-697eb70f76.

The cluster row attaches PMID:19054329 in the ENTRY role. All 24 LOTUS occurrence rows are preserved with their literal DOI strings, including eleven DOI strings repeated under each of two species and two further S. violaceoruber rows. Entry provenance, occurrence citations and a named-compound label do not establish that each publication independently supports every assertion. No primary publication, NPAtlas page or identifier resolver was accessed in this review. The complete local rows are evidence for retained assertion placement only.

### Occurrence and activity scope

evidence: supported. Targets: naturalproductmech:mibig-697eb70f76.

The saved LOTUS query returns 24 exact-key placements: eleven for NCBITaxon:1886, eleven for NCBITaxon:1902 and two for NCBITaxon:1935. The repeated DOI strings across taxa are not 24 independent studies or proof that all taxa biosynthesize the compound. There is no retained positive assay, molecular-target or sibling-mechanism row for this owner, and the captured owner has no bioactivity summary or molecular-target root. This finite local absence does not show biological inactivity or global absence of literature. The common antibiotic name does not substitute for a pure-compound assay or mechanism.

### Versioned classification applicability

consistency: unknown. Targets: naturalproductmech:mibig-697eb70f76.

NPClassifier npclassifier.gnps2.org@2026-09-07 supplies Terpenoids with empty superclass/class arrays and is_glycoside:false; MIBiG separately supplies OTHER. The stored C9 oxygenated epoxy cyclopentanone framework and absence of a separately identifiable sugar do not determine the biosynthetic pathway. In particular, the diagnostic's composite C5O cycle does not contradict the false glycoside prediction by itself. Filing and model provenance are faithfully retained, but the Terpenoids applicability and natural biosynthetic class remain unverified rather than silently converted to a source assertion or corrected from carbon count alone.

### Review completion

completeness: unknown. Targets: naturalproductmech:mibig-697eb70f76.

The complete owner and its two history events, exact saved source queries and routes, accepted canonical intake and both original molecular forms have been reviewed. Positive local structure/identifier correspondence and preservation of source claim grades support a qualified assessment. No maintained mechanism reader applies to this owner's absent graph/pathway/component roots. Full QC, complete OAK authority coverage and fresh external verification remain unavailable, so completion is partial; no native status, source record or history is changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2356-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/methylenomycin-a.yaml; Whole current plaintext; complete curation_history | supports | Whole owner and all 2 history events retain exact prior reading attribution. Native status remains SEEDED; no record edit was made. |
| support-2356-capture | /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json; /records/5/owner_document | supports | The accepted original whole-owner capture preserves all fields and optional-root presence; it is separate from later maintained resolution. |
| support-2356-grounding-owner | /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json; /records/5/owner_document/identifier; /records/5/owner_document/label; /records/5/owner_document/chemical_structure; /records/5/owner_document/grounding_status; /records/5/owner_document/grounding_notes; /records/5/owner_document/source_concepts; /records/5/owner_document/xrefs | supports | Exact retained identity, full key, structures, source definition and grounding scope; natural identity is not freshly authenticated. |
| support-2356-origin-owner | /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json; /records/5/owner_document/producer_organisms; /records/5/owner_document/biosynthetic_gene_clusters; /records/5/owner_document/producer_taxon_groups | supports | Producer and locus assertions retain their separate recorded grades, methods and citation roles. |
| support-2356-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json; /records/5/owner_document/occurrences; /records/5/owner_document/occurrence_taxon_groups | supports | Written occurrence placements are retained as database observations, not independent experiments. |
| support-2356-classification-owner | /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json; /records/5/owner_document/np_pathway; /records/5/owner_document/np_classification; /records/5/owner_document/bgc_class | supports | Versioned model outputs and source BGC classes remain separate assertions. |
| support-2356-assay-owner | /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json; /records/5/owner_document | supports | Complete captured owner establishes the absence of authored bioactivity, summary and molecular-target roots in this owner; biosynthetic enzymes are not assay targets. |
| support-2356-chemistry | /private/tmp/npm-review-work/shared-next-batch236/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/comparisons; /records/5/atom_correspondence; /records/5/formula_comparison_scope | supports | The original stored forms, all ten comparison flags and complete saved mapping are preserved. All comparisons are true; full_graph_identity_established remains false. |
| support-2356-topology | /private/tmp/npm-review-work/shared-next-batch236/chemistry-local/diagnostic-DATA-001.json; /records/5/smiles/computed; /records/5/inchi/computed; /records/5/declared_structure; /records/5/comparisons; /records/5/atom_correspondence | supports | Both saved forms encode the neutral C9H10O4 graph with three specified tetrahedral centers, an epoxide fused to a five-membered carbocycle, ring ketone, exomethylene and carboxylic acid. The reported six-member C5O candidate is a composite perimeter with the direct 1–3 bond retained; it does not identify a sugar residue. |
| support-2356-intake | /private/tmp/npm-review-work/shared-next-batch236/intakes/2356-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake identifies exact current source inputs, target scope and maintained correction ownership. |
| support-2356-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch236/root-intake-native-acceptance-001.json; /accepted; /status; /counts; /unavailable_required_checks | supports | ROOT accepts ten original intakes and five local gates. Full QC, complete OAK coverage and fresh external verification remain unavailable. |
| support-2356-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch236/root-source-inventory-acceptance-001.json; /accepted; /status; /totals | supports | ROOT accepts the original local inventory; its source meanings remain separately attributed. |
| support-2356-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch236/root-source-plan-acceptance-001.json; /accepted; /status; /verification | supports | ROOT accepts the exact saved plan and current intake alignment; no scientific conclusion is implied. |
| support-2356-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch236/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /status; /records/5; /scope; /original_tools | supports | ROOT accepts the single twenty-form diagnostic, including this owner’s saved scalars and all true comparisons. Warnings remain unassigned. |
| support-2356-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch236/chemistry-local/diagnostic-execution-001.json; Whole original execution receipt | supports | ROOT operated the diagnostic once; actual process, streams and input lineage remain saved. Scientific authoring performs no replay. |
| support-2356-diagnostic-warnings | /private/tmp/npm-review-work/shared-next-batch236/chemistry-local/diagnostic-original-001.stderr; Whole original stderr stream | supports | Ten omitted-undefined-stereo warnings, two also reporting charge rearrangement, are global and unassigned; no warning is attributed to a particular owner. |
| support-2356-plan | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-target-input-plan-001.json; /records/5; /source_placement_count; /unique_source_path_count | supports | Accepted unchanged input plan: 37 inputs for this owner, within 393 cohort placements and 56 paths. |
| support-2356-source-notes | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete saved source meanings and exact raw/history carries are explicitly attributed to Support and BGC; no source query was repeated. |
| support-2356-curation-scope | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-scope-notes-001.json; /curation; /curation_source_receipt | supports | ROOT’s bounded scan opened seven applicable implemented tables, including ignored files. The sole taxonomy-1931 textual hit belongs to unrelated BGC1648 and supplies no transferable correction; reserved decisions.tsv was unconsumed. |
| support-2356-source-routes | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/matched_chebi_ids; /contexts/11/source_scope_inventory/source_taxa; /contexts/11/source_scope_inventory/forward_taxon_merge_matches; /contexts/11/source_scope_inventory/nonorganism_matches; /contexts/11/source_scope_inventory/actual_assay_rows; /contexts/11/source_scope_inventory/blank_AID_sentinels; /contexts/11/source_scope_inventory/related_corpus_rows | supports | Exact saved source predicates and routes distinguish no-match frames, taxon merges and assay/sentinel scope. There are no actual assays or blank-AID sentinels for this owner. |
| support-2356-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/5; /cached_taxonomy/whole_stanzas/7; /cached_taxonomy/whole_stanzas/14 | supports | Relevant whole cached taxonomy stanzas retain names and synonyms as local authority only. BGC personally read the complete cache; these selected stanzas retain the source taxonomic context. |
| support-2356-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/mibig_compounds | supports | The complete retained mibig_compounds query frame has 1 positive row placements under its exact saved predicates; no query replay or wider absence claim. |
| support-2356-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 996–996, row_sha256 a1b37f42e7df594ebc8b5d6f91b43e18bafd11d2f03a17f1c62ae0df1b66a206 | supports | All 1 physical mibig_compounds rows and every field match the pinned saved frame. Their claim-specific interpretation is stated in the linked assessment, without transferring source roles. |
| support-2356-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/chebi_structures | supports | The complete retained chebi_structures query frame has 0 positive row placements under its exact saved predicates; no query replay or wider absence claim. |
| support-2356-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/lotus_occurrences | supports | The complete retained lotus_occurrences query frame has 24 positive row placements under its exact saved predicates; no query replay or wider absence claim. |
| support-2356-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 2239–2239, row_sha256 d0d2defc6b9abff9e6fac4e99e60cf6116f0437f015240ffa767d3d000ce29f9; physical lines 2240–2240, row_sha256 29e3a661106980f07bbed9669167e210ead195086984c3d67c1d29c6bce01bd8; physical lines 2241–2241, row_sha256 f211153ac6d0304e9a869c3b69f2e5391622de4bcc87d7b1d37bdf60dd97afe3; physical lines 2242–2242, row_sha256 47e4d60f8aad695d81b9964dd52888e8cb00b9a9f7924cf6609cda090df6f913; physical lines 2243–2243, row_sha256 d177ded23f5641a811d71eb113045e440c3b92562b3e5e66a3e69f38f939e048; physical lines 2244–2244, row_sha256 f40ff5c17860d365e33ac36788cc7e4384ae8d5b0be361b2e22ec67eac214ecb; physical lines 2245–2245, row_sha256 00157dca81b8331d7ca0ad2e37c1f3931c80fdc6221be5197c573aabeb9705d8; physical lines 2246–2246, row_sha256 135791860bb53fc0e2fc96ee933f7621c06bc4670f8c7a9b0a48ec84fff4ff4a; physical lines 2247–2247, row_sha256 f75403a6616f94589109060051908fa66557bc4ef3fd917bde9943e9e3a3f135; physical lines 2248–2248, row_sha256 68da8f3718f52b23274702fff8eff43c1300e55acad025045a2a28627a4fd64e; physical lines 2249–2249, row_sha256 373c1b7aaf4704b50b6d4837914a35dde02e4cd4cc241adfdb5490e2d8e8aa82; physical lines 2250–2250, row_sha256 c1d2d1fa922836d4e4e2fbcf678db03fd9ec534fabe93a2305568ac73b79adbc; physical lines 2251–2251, row_sha256 db9ac4e21d1bb80a2ae236d63fc598ae8df3b7a26fa5110503ca3dc5e022e1a6; physical lines 2252–2252, row_sha256 589651ba79f3f61f0d04090c90569f8a4338e1d1fd6a02dfbcf629939e5363bd; physical lines 2253–2253, row_sha256 21038a384e411824d9822f453c77ad27ff398625891b5f2a5cebeda44b39362a; physical lines 2254–2254, row_sha256 160f0065638ff44f7b212d5ac38e98873817051ed212bf94b305af2e4638727c; physical lines 2255–2255, row_sha256 93e126c8cc79287b3b1b7b69e9cfe738e07f3e2186cc57f0f085821cd85319f7; physical lines 2256–2256, row_sha256 7839931499e8f3efb931c5340f72351542955420ef125f66cba641f0956832a8; physical lines 2257–2257, row_sha256 e9d410329dcc84b9fa16feb1ab15492434e1e85c991699b64c3d1ccb52ec9748; physical lines 2258–2258, row_sha256 4424aefd4462cdb44882c0c10b7ce64568fd6a8d6de599d49130665f8c966540; physical lines 2259–2259, row_sha256 ae789ec434cc8fd92d43ef9fcf5e1f9be378906681a3f87cf6d2ddb66752900c; physical lines 2260–2260, row_sha256 7b2a4fe2fc35c69a26d64980892fab8ccc48e423f1bac3026bd8fc1da3a69e44; physical lines 2261–2261, row_sha256 b0f047ce368c9dd662e8aabbaa421eb22860ffa3d7de6d30585e03055fe17344; physical lines 2262–2262, row_sha256 b30d7526e604893edf2ad7fb82d86e07f09b3a8e0bf6005944efa2b85c3a5893 | supports | All 24 physical lotus_occurrences rows and every field match the pinned saved frame. Their claim-specific interpretation is stated in the linked assessment, without transferring source roles. |
| support-2356-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/cyanometdb_occurrences | supports | The complete retained cyanometdb_occurrences query frame has 0 positive row placements under its exact saved predicates; no query replay or wider absence claim. |
| support-2356-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/npclassifier | supports | The complete retained npclassifier query frame has 1 positive row placements under its exact saved predicates; no query replay or wider absence claim. |
| support-2356-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 778–778, row_sha256 390747c2894245549e25a2c673a1e3130b199c821573bf10832c7759d1457c00 | supports | All 1 physical npclassifier rows and every field match the pinned saved frame. Their claim-specific interpretation is stated in the linked assessment, without transferring source roles. |
| support-2356-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/pubchem_bioassay | supports | The complete retained pubchem_bioassay query frame has 0 positive row placements under its exact saved predicates; no query replay or wider absence claim. |
| support-2356-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/bindingdb_targets | supports | The complete retained bindingdb_targets query frame has 0 positive row placements under its exact saved predicates; no query replay or wider absence claim. |
| support-2356-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/antibioticmech_inchikeys | supports | The complete retained antibioticmech_inchikeys query frame has 0 positive row placements under its exact saved predicates; no query replay or wider absence claim. |
| support-2356-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/chebi_origins | supports | The complete retained chebi_origins query frame has 0 positive row placements under its exact saved predicates; no query replay or wider absence claim. |
| support-2356-direct-contexts | /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json; /records/5/direct_companion_paths; /records/5/direct_companion_predicates | supports | This owner has no additional one-hop companion path in the admitted plan; cohort companion claims are not transferred. |
| support-2356-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 175–200; lines 368–435 | supports | Schema separates structures and partial stereochemistry from faithful versioned model predictions. |
| support-2356-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 145–174 | supports | The retained stereo_complete predicate checks unassigned tetrahedral centers from source SMILES. It does not test all alkene stereochemistry or experimental identity. |
| support-2356-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 296–307; lines 982–1020 | supports | The maintained seeder copies source structures, stereo flags and versioned classification arrays; no regeneration was run. |
| support-2356-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | The twelve scientific dimensions and qualified partial completion reflect actual evidence and required-check access. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-236/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-236/native-current236-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-236/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-236/native-current236-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-236/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-236/native-current236-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-236/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-236/native-current236-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-236/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-236/native-current236-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally; no external publication, taxonomy, identifier, sequence or natural stereochemical assertion was refreshed.
- Full QC, complete OAK authority coverage and fresh external verification remain unavailable. Gates, stored-form parsing and maintained-view preservation establish only their stated scope.
- Exact no-match queries are bounded by saved predicates and snapshots. Shared loci, names, taxa or citations do not transfer identity, production, activity or mechanism.
- Ten original undefined-stereo warnings, two also reporting charge rearrangement, remain global and unassigned. No molecular or YAML parse, source query or target invocation occurred during authoring.
- Source records, native status and history remain unchanged. Model applicability concerns do not automatically establish maintained-source defects.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read all five complete raw owners/history, actual intakes, all ten saved molecular forms and the complete assigned source payloads. Exact prior raw carries and BGC complementary cache readings remain explicitly attributed.
- Saved molecular reading covers 256 atom and 272 bond rows plus every scalar, ring, stereo, motif and mapping field. Original correspondence limits remain; no new graph computation or parser was used.
- ROOT operated capture, inventory/composer, intakes and the diagnostic; Native operated gates and maintained readers under ROOT admission. ROOT separately accepted actual results. Scientific authoring invoked none of these targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T061942Z-methylenomycin-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: methylenomycin A'
started_at: '2026-11-04T05:39:54.333765Z'
finished_at: '2026-11-04T06:19:42.026997Z'
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
summary: The retained methylenomycin A structure and source identifier are locally
  consistent, with an explicitly limited source-only producer claim and 24 cited occurrence
  placements. The saved molecular forms describe the same epoxy cyclopentanone carboxylic
  acid at three specified tetrahedral centers. Neither the versioned Terpenoids prediction
  nor the diagnostic's composite C5O cycle establishes biosynthetic origin or a sugar
  residue. Natural identity, primary citations, source activity and current external
  grounding remain unverified; this is a qualified partial review.
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
  - path: data/natural_products/terpenoids/methylenomycin-a.yaml
    sha256: 4cf1e6fb15a935a931323e1e80462ae003e05fa6db4628cb693c0ce30b5030bb
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
  selection: Campaign path order 2356; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-697eb70f76
targets:
- target_id: naturalproductmech:mibig-697eb70f76
  path: data/natural_products/terpenoids/methylenomycin-a.yaml
  label: methylenomycin A
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
  - naturalproductmech:mibig-697eb70f76
  command: just validate-strict data/natural_products/terpenoids/marinoterpin-b.yaml
    data/natural_products/terpenoids/marinoterpin-c.yaml data/natural_products/terpenoids/marneral.yaml
    data/natural_products/terpenoids/merochlorin-a.yaml data/natural_products/terpenoids/merochlorin-b.yaml
    data/natural_products/terpenoids/methylenomycin-a.yaml data/natural_products/terpenoids/mk-8.yaml
    data/natural_products/terpenoids/momilactone-b.yaml data/natural_products/terpenoids/muurolol.yaml
    data/natural_products/terpenoids/naematolin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-236/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-697eb70f76
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-236/validate-all-001.tsv
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
  - naturalproductmech:mibig-697eb70f76
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
  - naturalproductmech:mibig-697eb70f76
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
  - naturalproductmech:mibig-697eb70f76
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-236/review-queue-001.tsv
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
  - naturalproductmech:mibig-697eb70f76
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-697eb70f76
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-697eb70f76
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2356-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/methylenomycin-a.yaml
  locator: Whole current plaintext; complete curation_history
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Whole owner and all 2 history events retain exact prior reading attribution.
    Native status remains SEEDED; no record edit was made.
  snapshot_sha256: 4cf1e6fb15a935a931323e1e80462ae003e05fa6db4628cb693c0ce30b5030bb
- evidence_id: support-2356-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json
  locator: /records/5/owner_document
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The accepted original whole-owner capture preserves all fields and optional-root
    presence; it is separate from later maintained resolution.
  snapshot_sha256: 4b4c82577273533ebae6ec08b65204c3189df06dfb16e0af6e7205527b87f9d8
- evidence_id: support-2356-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json
  locator: /records/5/owner_document/identifier; /records/5/owner_document/label;
    /records/5/owner_document/chemical_structure; /records/5/owner_document/grounding_status;
    /records/5/owner_document/grounding_notes; /records/5/owner_document/source_concepts;
    /records/5/owner_document/xrefs
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Exact retained identity, full key, structures, source definition and grounding
    scope; natural identity is not freshly authenticated.
  snapshot_sha256: 4b4c82577273533ebae6ec08b65204c3189df06dfb16e0af6e7205527b87f9d8
- evidence_id: support-2356-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json
  locator: /records/5/owner_document/producer_organisms; /records/5/owner_document/biosynthetic_gene_clusters;
    /records/5/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Producer and locus assertions retain their separate recorded grades, methods
    and citation roles.
  snapshot_sha256: 4b4c82577273533ebae6ec08b65204c3189df06dfb16e0af6e7205527b87f9d8
- evidence_id: support-2356-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json
  locator: /records/5/owner_document/occurrences; /records/5/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Written occurrence placements are retained as database observations, not
    independent experiments.
  snapshot_sha256: 4b4c82577273533ebae6ec08b65204c3189df06dfb16e0af6e7205527b87f9d8
- evidence_id: support-2356-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json
  locator: /records/5/owner_document/np_pathway; /records/5/owner_document/np_classification;
    /records/5/owner_document/bgc_class
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Versioned model outputs and source BGC classes remain separate assertions.
  snapshot_sha256: 4b4c82577273533ebae6ec08b65204c3189df06dfb16e0af6e7205527b87f9d8
- evidence_id: support-2356-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/owner-capture-DATA-001.json
  locator: /records/5/owner_document
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Complete captured owner establishes the absence of authored bioactivity,
    summary and molecular-target roots in this owner; biosynthetic enzymes are not
    assay targets.
  snapshot_sha256: 4b4c82577273533ebae6ec08b65204c3189df06dfb16e0af6e7205527b87f9d8
- evidence_id: support-2356-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/comparisons; /records/5/atom_correspondence;
    /records/5/formula_comparison_scope
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The original stored forms, all ten comparison flags and complete saved
    mapping are preserved. All comparisons are true; full_graph_identity_established
    remains false.
  snapshot_sha256: 310b58ca194e19bbc6277ca363cbf09c436b5fb7204facc5df1db877fe898eaa
- evidence_id: support-2356-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/smiles/computed; /records/5/inchi/computed; /records/5/declared_structure;
    /records/5/comparisons; /records/5/atom_correspondence
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Both saved forms encode the neutral C9H10O4 graph with three specified
    tetrahedral centers, an epoxide fused to a five-membered carbocycle, ring ketone,
    exomethylene and carboxylic acid. The reported six-member C5O candidate is a composite
    perimeter with the direct 1–3 bond retained; it does not identify a sugar residue.
  snapshot_sha256: 310b58ca194e19bbc6277ca363cbf09c436b5fb7204facc5df1db877fe898eaa
- evidence_id: support-2356-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/intakes/2356-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Actual canonical intake identifies exact current source inputs, target
    scope and maintained correction ownership.
  snapshot_sha256: fc720a212cca991c26ccd5a34a17986e56a21f9ce6c961f031c79eaefa5a25d8
- evidence_id: support-2356-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/root-intake-native-acceptance-001.json
  locator: /accepted; /status; /counts; /unavailable_required_checks
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: ROOT accepts ten original intakes and five local gates. Full QC, complete
    OAK coverage and fresh external verification remain unavailable.
  snapshot_sha256: 9fb5ea136fb1108c567c87a0efbe602ee148042ece07ef45421c26c7d9e895b8
- evidence_id: support-2356-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/root-source-inventory-acceptance-001.json
  locator: /accepted; /status; /totals
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: ROOT accepts the original local inventory; its source meanings remain separately
    attributed.
  snapshot_sha256: 8f40449a606e8ee78df4a752975e8cee72e20d58d58f83de9d54b3dbb6d656f9
- evidence_id: support-2356-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/root-source-plan-acceptance-001.json
  locator: /accepted; /status; /verification
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: ROOT accepts the exact saved plan and current intake alignment; no scientific
    conclusion is implied.
  snapshot_sha256: f4db11233277dabad87533357828bb01f5a0b54f709ca3e2558ca01c3c1cabec
- evidence_id: support-2356-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /status; /records/5; /scope; /original_tools
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: ROOT accepts the single twenty-form diagnostic, including this owner’s
    saved scalars and all true comparisons. Warnings remain unassigned.
  snapshot_sha256: ac7243d527ce492a891bca9b1bd9b0668ec5864a2c4bad131f1165337b5eb76e
- evidence_id: support-2356-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/chemistry-local/diagnostic-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: ROOT operated the diagnostic once; actual process, streams and input lineage
    remain saved. Scientific authoring performs no replay.
  snapshot_sha256: d61ae0287657e96133311e8b05d91cbe8c4f829267bd54e9722b35e1a22eaaf1
- evidence_id: support-2356-diagnostic-warnings
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr stream
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Ten omitted-undefined-stereo warnings, two also reporting charge rearrangement,
    are global and unassigned; no warning is attributed to a particular owner.
  snapshot_sha256: edd14bdffddee49b0857212ff968a9f9f108d398a602ed7bf1c819bbd9fe3329
- evidence_id: support-2356-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-target-input-plan-001.json
  locator: /records/5; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: 'Accepted unchanged input plan: 37 inputs for this owner, within 393 cohort
    placements and 56 paths.'
  snapshot_sha256: 6133ef3a4c0374f6f94055115b6a611af51bbeb17b50b37a36a9c535c9d8468b
- evidence_id: support-2356-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Complete saved source meanings and exact raw/history carries are explicitly
    attributed to Support and BGC; no source query was repeated.
  snapshot_sha256: 30628d7bbaae53042c3012eb9a02ec207728dbc95e4afde0998b3f634591997c
- evidence_id: support-2356-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-scope-notes-001.json
  locator: /curation; /curation_source_receipt
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: ROOT’s bounded scan opened seven applicable implemented tables, including
    ignored files. The sole taxonomy-1931 textual hit belongs to unrelated BGC1648
    and supplies no transferable correction; reserved decisions.tsv was unconsumed.
  snapshot_sha256: 30628d7bbaae53042c3012eb9a02ec207728dbc95e4afde0998b3f634591997c
- evidence_id: support-2356-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/matched_chebi_ids; /contexts/11/source_scope_inventory/source_taxa;
    /contexts/11/source_scope_inventory/forward_taxon_merge_matches; /contexts/11/source_scope_inventory/nonorganism_matches;
    /contexts/11/source_scope_inventory/actual_assay_rows; /contexts/11/source_scope_inventory/blank_AID_sentinels;
    /contexts/11/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Exact saved source predicates and routes distinguish no-match frames, taxon
    merges and assay/sentinel scope. There are no actual assays or blank-AID sentinels
    for this owner.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/5; /cached_taxonomy/whole_stanzas/7;
    /cached_taxonomy/whole_stanzas/14
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Relevant whole cached taxonomy stanzas retain names and synonyms as local
    authority only. BGC personally read the complete cache; these selected stanzas
    retain the source taxonomic context.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The complete retained mibig_compounds query frame has 1 positive row placements
    under its exact saved predicates; no query replay or wider absence claim.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 996–996, row_sha256 a1b37f42e7df594ebc8b5d6f91b43e18bafd11d2f03a17f1c62ae0df1b66a206
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: All 1 physical mibig_compounds rows and every field match the pinned saved
    frame. Their claim-specific interpretation is stated in the linked assessment,
    without transferring source roles.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2356-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The complete retained chebi_structures query frame has 0 positive row placements
    under its exact saved predicates; no query replay or wider absence claim.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The complete retained lotus_occurrences query frame has 24 positive row
    placements under its exact saved predicates; no query replay or wider absence
    claim.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 2239–2239, row_sha256 d0d2defc6b9abff9e6fac4e99e60cf6116f0437f015240ffa767d3d000ce29f9;
    physical lines 2240–2240, row_sha256 29e3a661106980f07bbed9669167e210ead195086984c3d67c1d29c6bce01bd8;
    physical lines 2241–2241, row_sha256 f211153ac6d0304e9a869c3b69f2e5391622de4bcc87d7b1d37bdf60dd97afe3;
    physical lines 2242–2242, row_sha256 47e4d60f8aad695d81b9964dd52888e8cb00b9a9f7924cf6609cda090df6f913;
    physical lines 2243–2243, row_sha256 d177ded23f5641a811d71eb113045e440c3b92562b3e5e66a3e69f38f939e048;
    physical lines 2244–2244, row_sha256 f40ff5c17860d365e33ac36788cc7e4384ae8d5b0be361b2e22ec67eac214ecb;
    physical lines 2245–2245, row_sha256 00157dca81b8331d7ca0ad2e37c1f3931c80fdc6221be5197c573aabeb9705d8;
    physical lines 2246–2246, row_sha256 135791860bb53fc0e2fc96ee933f7621c06bc4670f8c7a9b0a48ec84fff4ff4a;
    physical lines 2247–2247, row_sha256 f75403a6616f94589109060051908fa66557bc4ef3fd917bde9943e9e3a3f135;
    physical lines 2248–2248, row_sha256 68da8f3718f52b23274702fff8eff43c1300e55acad025045a2a28627a4fd64e;
    physical lines 2249–2249, row_sha256 373c1b7aaf4704b50b6d4837914a35dde02e4cd4cc241adfdb5490e2d8e8aa82;
    physical lines 2250–2250, row_sha256 c1d2d1fa922836d4e4e2fbcf678db03fd9ec534fabe93a2305568ac73b79adbc;
    physical lines 2251–2251, row_sha256 db9ac4e21d1bb80a2ae236d63fc598ae8df3b7a26fa5110503ca3dc5e022e1a6;
    physical lines 2252–2252, row_sha256 589651ba79f3f61f0d04090c90569f8a4338e1d1fd6a02dfbcf629939e5363bd;
    physical lines 2253–2253, row_sha256 21038a384e411824d9822f453c77ad27ff398625891b5f2a5cebeda44b39362a;
    physical lines 2254–2254, row_sha256 160f0065638ff44f7b212d5ac38e98873817051ed212bf94b305af2e4638727c;
    physical lines 2255–2255, row_sha256 93e126c8cc79287b3b1b7b69e9cfe738e07f3e2186cc57f0f085821cd85319f7;
    physical lines 2256–2256, row_sha256 7839931499e8f3efb931c5340f72351542955420ef125f66cba641f0956832a8;
    physical lines 2257–2257, row_sha256 e9d410329dcc84b9fa16feb1ab15492434e1e85c991699b64c3d1ccb52ec9748;
    physical lines 2258–2258, row_sha256 4424aefd4462cdb44882c0c10b7ce64568fd6a8d6de599d49130665f8c966540;
    physical lines 2259–2259, row_sha256 ae789ec434cc8fd92d43ef9fcf5e1f9be378906681a3f87cf6d2ddb66752900c;
    physical lines 2260–2260, row_sha256 7b2a4fe2fc35c69a26d64980892fab8ccc48e423f1bac3026bd8fc1da3a69e44;
    physical lines 2261–2261, row_sha256 b0f047ce368c9dd662e8aabbaa421eb22860ffa3d7de6d30585e03055fe17344;
    physical lines 2262–2262, row_sha256 b30d7526e604893edf2ad7fb82d86e07f09b3a8e0bf6005944efa2b85c3a5893
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: All 24 physical lotus_occurrences rows and every field match the pinned
    saved frame. Their claim-specific interpretation is stated in the linked assessment,
    without transferring source roles.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2356-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The complete retained cyanometdb_occurrences query frame has 0 positive
    row placements under its exact saved predicates; no query replay or wider absence
    claim.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The complete retained npclassifier query frame has 1 positive row placements
    under its exact saved predicates; no query replay or wider absence claim.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 778–778, row_sha256 390747c2894245549e25a2c673a1e3130b199c821573bf10832c7759d1457c00
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: All 1 physical npclassifier rows and every field match the pinned saved
    frame. Their claim-specific interpretation is stated in the linked assessment,
    without transferring source roles.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2356-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The complete retained pubchem_bioassay query frame has 0 positive row placements
    under its exact saved predicates; no query replay or wider absence claim.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The complete retained bindingdb_targets query frame has 0 positive row
    placements under its exact saved predicates; no query replay or wider absence
    claim.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The complete retained antibioticmech_inchikeys query frame has 0 positive
    row placements under its exact saved predicates; no query replay or wider absence
    claim.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The complete retained chebi_origins query frame has 0 positive row placements
    under its exact saved predicates; no query replay or wider absence claim.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch236-tentative/bgc-prep/bgc-conditional236-source-inventory-DATA-001.json
  locator: /records/5/direct_companion_paths; /records/5/direct_companion_predicates
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: This owner has no additional one-hop companion path in the admitted plan;
    cohort companion claims are not transferred.
  snapshot_sha256: 93a256fac633f347e144aecf96a1cd83178e7743ade79c2557bb78f67341f12a
- evidence_id: support-2356-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 175–200; lines 368–435
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: Schema separates structures and partial stereochemistry from faithful versioned
    model predictions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2356-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 145–174
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The retained stereo_complete predicate checks unassigned tetrahedral centers
    from source SMILES. It does not test all alkene stereochemistry or experimental
    identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2356-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 296–307; lines 982–1020
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The maintained seeder copies source structures, stereo flags and versioned
    classification arrays; no regeneration was run.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2356-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-04T06:07:43.353500Z'
  support: supports
  summary: The twelve scientific dimensions and qualified partial completion reflect
    actual evidence and required-check access.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-236/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-236/native-current236-five-gates-execution-001.json
  accessed_at: '2026-11-04T05:43:16.781562Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 4a893f8c103547489f95eec4544cedded404f096b89a014cd8cd0b946dedf203
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-236/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-236/native-current236-five-gates-execution-001.json
  accessed_at: '2026-11-04T05:43:44.197435Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 2f837a3cf4764bc15fd96ac8eb183e44270459efdfc25d77a42f6f09fda24e55
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-236/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-236/native-current236-five-gates-execution-001.json
  accessed_at: '2026-11-04T05:44:04.509410Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-236/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-236/native-current236-five-gates-execution-001.json
  accessed_at: '2026-11-04T05:44:39.496584Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-236/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-236/native-current236-five-gates-execution-001.json
  accessed_at: '2026-11-04T05:44:51.825171Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 85f60bfe3261f9bfbe397d0497cfa225523d8b6677db35510a4ec927f5d7a111
assessments:
- assessment_id: support-2356-identity
  area: identity
  topic: Retained structure and identifier correspondence
  outcome: supported
  summary: The exact target is minted naturalproductmech:mibig-697eb70f76, full key
    HBECYYFDLZZMPL-WLGLDCGKSA-N, with source concept BGC0000914 version 5 and retained
    NPAtlas xref NPA013552. The locally captured source structure, identifier and
    label agree with their saved inventory row. No exact-key ChEBI match is returned
    by the retained query; that is bounded snapshot scope, not proof that no such
    concept exists. Both original stored-form diagnostics reproduce the declared key
    and canonical representations. The NPAtlas link and the natural compound denoted
    by the label were not freshly resolved, and standardized agreement is not independent
    experimental identity proof.
  target_ids:
  - naturalproductmech:mibig-697eb70f76
  evidence_ids:
  - support-2356-grounding-owner
  - support-2356-source-mibig_compounds
  - support-2356-query-chebi_structures
  - support-2356-chemistry
  - support-2356-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: HBECYYFDLZZMPL-WLGLDCGKSA-N; exact retained full key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - support-2356-grounding-owner
    - support-2356-source-mibig_compounds
    - support-2356-query-chebi_structures
    - support-2356-chemistry
    - support-2356-direct-contexts
  - name: grounding_scope
    value: The exact target is minted naturalproductmech:mibig-697eb70f76, full key
      HBECYYFDLZZMPL-WLGLDCGKSA-N, with source concept BGC0000914 version 5 and retained
      NPAtlas xref NPA013552. The locally captured source structure, identifier and
      label agree with their saved inventory row. No exact-key ChEBI match is returned
      by the retained query; that is bounded snapshot scope, not proof that no such
      concept exists. Both original stored-form diagnostics reproduce the declared
      key and canonical representations. The NPAtlas link and the natural compound
      denoted by the label were not freshly resolved, and standardized agreement is
      not independent experimental identity proof.
    definition: Retained local grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2356-grounding-owner
    - support-2356-source-mibig_compounds
    - support-2356-query-chebi_structures
    - support-2356-chemistry
    - support-2356-direct-contexts
- assessment_id: support-2356-representation
  area: representation
  topic: Stored representation and stereochemical scope
  outcome: supported
  summary: Both stored forms parse to neutral C9H10O4 with 13 heavy atoms and 14 bonds.
    The complete tables show an epoxide sharing its carbon-carbon edge with a five-membered
    carbocycle, a ring ketone, an exocyclic methylene and a carboxylic acid. The SMILES
    centers 1S, 3S and 9R map to the saved InChI centers 7S, 8S and 4R; both potential-stereo
    tables contain three specified tetrahedral centers. All ten comparison flags are
    true, but the saved correspondence is only one chirality-aware substructure match
    and explicitly does not establish independent full-graph or natural identity.
    The motif's six-membered C5O perimeter [1,2,3,5,7,9] traverses the epoxide oxygen
    and the longer cyclopentanone path; the direct 1-3 carbon bond remains. This composite
    cycle is not an identified sugar residue or glycosidic linkage. The source stereo
    flag is a retained extractor result, not a new determination of natural stereochemistry.
  target_ids:
  - naturalproductmech:mibig-697eb70f76
  evidence_ids:
  - support-2356-grounding-owner
  - support-2356-chemistry
  - support-2356-topology
  - support-2356-diagnostic-acceptance
  - support-2356-structure-schema
  - support-2356-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both stored forms parse to neutral C9H10O4 with 13 heavy atoms and 14 bonds.
      The complete tables show an epoxide sharing its carbon-carbon edge with a five-membered
      carbocycle, a ring ketone, an exocyclic methylene and a carboxylic acid. The
      SMILES centers 1S, 3S and 9R map to the saved InChI centers 7S, 8S and 4R; both
      potential-stereo tables contain three specified tetrahedral centers. All ten
      comparison flags are true, but the saved correspondence is only one chirality-aware
      substructure match and explicitly does not establish independent full-graph
      or natural identity. The motif's six-membered C5O perimeter [1,2,3,5,7,9] traverses
      the epoxide oxygen and the longer cyclopentanone path; the direct 1-3 carbon
      bond remains. This composite cycle is not an identified sugar residue or glycosidic
      linkage. The source stereo flag is a retained extractor result, not a new determination
      of natural stereochemistry.
    definition: Complete saved stereo, atom and bond interpretation; no new parse
      or experimental assignment.
    evidence_ids:
    - support-2356-grounding-owner
    - support-2356-chemistry
    - support-2356-topology
    - support-2356-diagnostic-acceptance
    - support-2356-structure-schema
    - support-2356-stereo-method
  - name: representation_correspondence
    value: Both stored forms parse to neutral C9H10O4 with 13 heavy atoms and 14 bonds.
      The complete tables show an epoxide sharing its carbon-carbon edge with a five-membered
      carbocycle, a ring ketone, an exocyclic methylene and a carboxylic acid. The
      SMILES centers 1S, 3S and 9R map to the saved InChI centers 7S, 8S and 4R; both
      potential-stereo tables contain three specified tetrahedral centers. All ten
      comparison flags are true, but the saved correspondence is only one chirality-aware
      substructure match and explicitly does not establish independent full-graph
      or natural identity. The motif's six-membered C5O perimeter [1,2,3,5,7,9] traverses
      the epoxide oxygen and the longer cyclopentanone path; the direct 1-3 carbon
      bond remains. This composite cycle is not an identified sugar residue or glycosidic
      linkage. The source stereo flag is a retained extractor result, not a new determination
      of natural stereochemistry.
    definition: Normalized identifier agreement does not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2356-grounding-owner
    - support-2356-chemistry
    - support-2356-topology
    - support-2356-diagnostic-acceptance
    - support-2356-structure-schema
    - support-2356-stereo-method
- assessment_id: support-2356-provenance
  area: provenance
  topic: Producer and locus evidence
  outcome: supported
  summary: 'BGC0000914 version 5 is retained as active with questionable quality and
    unknown completeness metadata, OTHER class, and Streptomyces coelicolor A3(2),
    NCBITaxon:100226. Producer SOURCE_ASSERTION and locus CLUSTER_UNSTATED remain
    distinct: no locus method is stated in this saved row. Those values support faithful
    local attribution, not newly demonstrated biosynthesis. Quality and completeness
    metadata do not independently certify or refute the science. Occurrence taxa S.
    albidoflavus, S. coelicolor and S. violaceoruber are separate retained occurrence
    claims; species or strain labels and shared citations cannot upgrade producer
    evidence.'
  target_ids:
  - naturalproductmech:mibig-697eb70f76
  evidence_ids:
  - support-2356-origin-owner
  - support-2356-source-mibig_compounds
  - support-2356-cached-taxonomy
  - support-2356-source-routes
  - support-2356-direct-contexts
  dimensions:
  - name: taxon_scope
    value: 'BGC0000914 version 5 is retained as active with questionable quality and
      unknown completeness metadata, OTHER class, and Streptomyces coelicolor A3(2),
      NCBITaxon:100226. Producer SOURCE_ASSERTION and locus CLUSTER_UNSTATED remain
      distinct: no locus method is stated in this saved row. Those values support
      faithful local attribution, not newly demonstrated biosynthesis. Quality and
      completeness metadata do not independently certify or refute the science. Occurrence
      taxa S. albidoflavus, S. coelicolor and S. violaceoruber are separate retained
      occurrence claims; species or strain labels and shared citations cannot upgrade
      producer evidence.'
    definition: Producer, occurrence, species, strain and unresolved labels retain
      separate scope; cached labels are not fresh authority.
    evidence_ids:
    - support-2356-origin-owner
    - support-2356-source-mibig_compounds
    - support-2356-cached-taxonomy
    - support-2356-source-routes
    - support-2356-direct-contexts
  - name: producer_evidence
    value: 'BGC0000914 version 5 is retained as active with questionable quality and
      unknown completeness metadata, OTHER class, and Streptomyces coelicolor A3(2),
      NCBITaxon:100226. Producer SOURCE_ASSERTION and locus CLUSTER_UNSTATED remain
      distinct: no locus method is stated in this saved row. Those values support
      faithful local attribution, not newly demonstrated biosynthesis. Quality and
      completeness metadata do not independently certify or refute the science. Occurrence
      taxa S. albidoflavus, S. coelicolor and S. violaceoruber are separate retained
      occurrence claims; species or strain labels and shared citations cannot upgrade
      producer evidence.'
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - support-2356-origin-owner
    - support-2356-source-mibig_compounds
    - support-2356-cached-taxonomy
    - support-2356-source-routes
    - support-2356-direct-contexts
  - name: locus_evidence
    value: 'BGC0000914 version 5 is retained as active with questionable quality and
      unknown completeness metadata, OTHER class, and Streptomyces coelicolor A3(2),
      NCBITaxon:100226. Producer SOURCE_ASSERTION and locus CLUSTER_UNSTATED remain
      distinct: no locus method is stated in this saved row. Those values support
      faithful local attribution, not newly demonstrated biosynthesis. Quality and
      completeness metadata do not independently certify or refute the science. Occurrence
      taxa S. albidoflavus, S. coelicolor and S. violaceoruber are separate retained
      occurrence claims; species or strain labels and shared citations cannot upgrade
      producer evidence.'
    definition: Source version, status, method and grade are not a complete pathway
      or fresh primary verification.
    evidence_ids:
    - support-2356-origin-owner
    - support-2356-source-mibig_compounds
    - support-2356-cached-taxonomy
    - support-2356-source-routes
    - support-2356-direct-contexts
- assessment_id: support-2356-citations
  area: evidence
  topic: Citation roles
  outcome: supported
  summary: The cluster row attaches PMID:19054329 in the ENTRY role. All 24 LOTUS
    occurrence rows are preserved with their literal DOI strings, including eleven
    DOI strings repeated under each of two species and two further S. violaceoruber
    rows. Entry provenance, occurrence citations and a named-compound label do not
    establish that each publication independently supports every assertion. No primary
    publication, NPAtlas page or identifier resolver was accessed in this review.
    The complete local rows are evidence for retained assertion placement only.
  target_ids:
  - naturalproductmech:mibig-697eb70f76
  evidence_ids:
  - support-2356-origin-owner
  - support-2356-occurrence-owner
  - support-2356-source-mibig_compounds
  - support-2356-source-notes
  - support-2356-source-lotus_occurrences
  dimensions:
  - name: citation_scope
    value: The cluster row attaches PMID:19054329 in the ENTRY role. All 24 LOTUS
      occurrence rows are preserved with their literal DOI strings, including eleven
      DOI strings repeated under each of two species and two further S. violaceoruber
      rows. Entry provenance, occurrence citations and a named-compound label do not
      establish that each publication independently supports every assertion. No primary
      publication, NPAtlas page or identifier resolver was accessed in this review.
      The complete local rows are evidence for retained assertion placement only.
    definition: Database provenance, historical primary-experiment support and occurrence
      citations retain distinct roles; no publication independence or fresh access
      is assumed.
    evidence_ids:
    - support-2356-origin-owner
    - support-2356-occurrence-owner
    - support-2356-source-mibig_compounds
    - support-2356-source-notes
    - support-2356-source-lotus_occurrences
- assessment_id: support-2356-occurrence
  area: evidence
  topic: Occurrence and activity scope
  outcome: supported
  summary: 'The saved LOTUS query returns 24 exact-key placements: eleven for NCBITaxon:1886,
    eleven for NCBITaxon:1902 and two for NCBITaxon:1935. The repeated DOI strings
    across taxa are not 24 independent studies or proof that all taxa biosynthesize
    the compound. There is no retained positive assay, molecular-target or sibling-mechanism
    row for this owner, and the captured owner has no bioactivity summary or molecular-target
    root. This finite local absence does not show biological inactivity or global
    absence of literature. The common antibiotic name does not substitute for a pure-compound
    assay or mechanism.'
  target_ids:
  - naturalproductmech:mibig-697eb70f76
  evidence_ids:
  - support-2356-occurrence-owner
  - support-2356-assay-owner
  - support-2356-source-routes
  - support-2356-cached-taxonomy
  - support-2356-query-lotus_occurrences
  - support-2356-query-chebi_origins
  - support-2356-query-cyanometdb_occurrences
  - support-2356-query-pubchem_bioassay
  - support-2356-query-bindingdb_targets
  - support-2356-query-antibioticmech_inchikeys
  dimensions:
  - name: occurrence_scope
    value: 'The saved LOTUS query returns 24 exact-key placements: eleven for NCBITaxon:1886,
      eleven for NCBITaxon:1902 and two for NCBITaxon:1935. The repeated DOI strings
      across taxa are not 24 independent studies or proof that all taxa biosynthesize
      the compound. There is no retained positive assay, molecular-target or sibling-mechanism
      row for this owner, and the captured owner has no bioactivity summary or molecular-target
      root. This finite local absence does not show biological inactivity or global
      absence of literature. The common antibiotic name does not substitute for a
      pure-compound assay or mechanism.'
    definition: Occurrence placements are not counts of independent experiments or
      demonstrated producers.
    evidence_ids:
    - support-2356-occurrence-owner
    - support-2356-assay-owner
    - support-2356-source-routes
    - support-2356-cached-taxonomy
    - support-2356-query-lotus_occurrences
    - support-2356-query-chebi_origins
    - support-2356-query-cyanometdb_occurrences
    - support-2356-query-pubchem_bioassay
    - support-2356-query-bindingdb_targets
    - support-2356-query-antibioticmech_inchikeys
  - name: assay_target_scope
    value: 'The saved LOTUS query returns 24 exact-key placements: eleven for NCBITaxon:1886,
      eleven for NCBITaxon:1902 and two for NCBITaxon:1935. The repeated DOI strings
      across taxa are not 24 independent studies or proof that all taxa biosynthesize
      the compound. There is no retained positive assay, molecular-target or sibling-mechanism
      row for this owner, and the captured owner has no bioactivity summary or molecular-target
      root. This finite local absence does not show biological inactivity or global
      absence of literature. The common antibiotic name does not substitute for a
      pure-compound assay or mechanism.'
    definition: Retained assay and target assertions are bounded; biosynthetic proteins
      are not pharmacological target evidence.
    evidence_ids:
    - support-2356-occurrence-owner
    - support-2356-assay-owner
    - support-2356-source-routes
    - support-2356-cached-taxonomy
    - support-2356-query-lotus_occurrences
    - support-2356-query-chebi_origins
    - support-2356-query-cyanometdb_occurrences
    - support-2356-query-pubchem_bioassay
    - support-2356-query-bindingdb_targets
    - support-2356-query-antibioticmech_inchikeys
- assessment_id: support-2356-classification
  area: consistency
  topic: Versioned classification applicability
  outcome: unknown
  summary: NPClassifier npclassifier.gnps2.org@2026-09-07 supplies Terpenoids with
    empty superclass/class arrays and is_glycoside:false; MIBiG separately supplies
    OTHER. The stored C9 oxygenated epoxy cyclopentanone framework and absence of
    a separately identifiable sugar do not determine the biosynthetic pathway. In
    particular, the diagnostic's composite C5O cycle does not contradict the false
    glycoside prediction by itself. Filing and model provenance are faithfully retained,
    but the Terpenoids applicability and natural biosynthetic class remain unverified
    rather than silently converted to a source assertion or corrected from carbon
    count alone.
  target_ids:
  - naturalproductmech:mibig-697eb70f76
  evidence_ids:
  - support-2356-classification-owner
  - support-2356-source-mibig_compounds
  - support-2356-source-npclassifier
  - support-2356-chemistry
  - support-2356-topology
  - support-2356-structure-schema
  - support-2356-classification-seeder
  dimensions:
  - name: classification_applicability
    value: NPClassifier npclassifier.gnps2.org@2026-09-07 supplies Terpenoids with
      empty superclass/class arrays and is_glycoside:false; MIBiG separately supplies
      OTHER. The stored C9 oxygenated epoxy cyclopentanone framework and absence of
      a separately identifiable sugar do not determine the biosynthetic pathway. In
      particular, the diagnostic's composite C5O cycle does not contradict the false
      glycoside prediction by itself. Filing and model provenance are faithfully retained,
      but the Terpenoids applicability and natural biosynthetic class remain unverified
      rather than silently converted to a source assertion or corrected from carbon
      count alone.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct evidence types.
    evidence_ids:
    - support-2356-classification-owner
    - support-2356-source-mibig_compounds
    - support-2356-source-npclassifier
    - support-2356-chemistry
    - support-2356-topology
    - support-2356-structure-schema
    - support-2356-classification-seeder
- assessment_id: support-2356-completion
  area: completeness
  topic: Review completion
  outcome: unknown
  summary: The complete owner and its two history events, exact saved source queries
    and routes, accepted canonical intake and both original molecular forms have been
    reviewed. Positive local structure/identifier correspondence and preservation
    of source claim grades support a qualified assessment. No maintained mechanism
    reader applies to this owner's absent graph/pathway/component roots. Full QC,
    complete OAK authority coverage and fresh external verification remain unavailable,
    so completion is partial; no native status, source record or history is changed.
  target_ids:
  - naturalproductmech:mibig-697eb70f76
  evidence_ids:
  - support-2356-owner
  - support-2356-capture
  - support-2356-intake
  - support-2356-intake-acceptance
  - support-2356-inventory-acceptance
  - support-2356-plan
  - support-2356-plan-acceptance
  - support-2356-source-notes
  - support-2356-curation-scope
  - support-2356-diagnostic-execution
  - support-2356-diagnostic-warnings
  - support-2356-diagnostic-acceptance
  - support-2356-review-profile
  - support-2356-query-mibig_compounds
  - support-2356-query-chebi_structures
  - support-2356-query-lotus_occurrences
  - support-2356-query-cyanometdb_occurrences
  - support-2356-query-npclassifier
  - support-2356-query-pubchem_bioassay
  - support-2356-query-bindingdb_targets
  - support-2356-query-antibioticmech_inchikeys
  - support-2356-query-chebi_origins
  dimensions:
  - name: review_completion
    value: The complete owner and its two history events, exact saved source queries
      and routes, accepted canonical intake and both original molecular forms have
      been reviewed. Positive local structure/identifier correspondence and preservation
      of source claim grades support a qualified assessment. No maintained mechanism
      reader applies to this owner's absent graph/pathway/component roots. Full QC,
      complete OAK authority coverage and fresh external verification remain unavailable,
      so completion is partial; no native status, source record or history is changed.
    definition: Completion reflects actual access and required-check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - support-2356-owner
    - support-2356-capture
    - support-2356-intake
    - support-2356-intake-acceptance
    - support-2356-inventory-acceptance
    - support-2356-plan
    - support-2356-plan-acceptance
    - support-2356-source-notes
    - support-2356-curation-scope
    - support-2356-diagnostic-execution
    - support-2356-diagnostic-warnings
    - support-2356-diagnostic-acceptance
    - support-2356-review-profile
    - support-2356-query-mibig_compounds
    - support-2356-query-chebi_structures
    - support-2356-query-lotus_occurrences
    - support-2356-query-cyanometdb_occurrences
    - support-2356-query-npclassifier
    - support-2356-query-pubchem_bioassay
    - support-2356-query-bindingdb_targets
    - support-2356-query-antibioticmech_inchikeys
    - support-2356-query-chebi_origins
findings: []
actions: []
limitations:
- All evidence is retained locally; no external publication, taxonomy, identifier,
  sequence or natural stereochemical assertion was refreshed.
- Full QC, complete OAK authority coverage and fresh external verification remain
  unavailable. Gates, stored-form parsing and maintained-view preservation establish
  only their stated scope.
- Exact no-match queries are bounded by saved predicates and snapshots. Shared loci,
  names, taxa or citations do not transfer identity, production, activity or mechanism.
- Ten original undefined-stereo warnings, two also reporting charge rearrangement,
  remain global and unassigned. No molecular or YAML parse, source query or target
  invocation occurred during authoring.
- Source records, native status and history remain unchanged. Model applicability
  concerns do not automatically establish maintained-source defects.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support personally read all five complete raw owners/history, actual intakes, all
  ten saved molecular forms and the complete assigned source payloads. Exact prior
  raw carries and BGC complementary cache readings remain explicitly attributed.
- Saved molecular reading covers 256 atom and 272 bond rows plus every scalar, ring,
  stereo, motif and mapping field. Original correspondence limits remain; no new graph
  computation or parser was used.
- ROOT operated capture, inventory/composer, intakes and the diagnostic; Native operated
  gates and maintained readers under ROOT admission. ROOT separately accepted actual
  results. Scientific authoring invoked none of these targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-236
```
