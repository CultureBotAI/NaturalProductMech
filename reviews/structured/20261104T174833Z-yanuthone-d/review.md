# Local evidence review: yanuthone D

- Review: 20261104T174833Z-yanuthone-d
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T16:43:12.852179Z
- Finished UTC: 2026-11-04T17:48:33.936302Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Yanuthone D has consistent retained structure/key encodings with two unresolved tetrahedral centers. Its source-qualified ATCC 1015 producer/locus claim, species occurrences and blank-assay sentinel remain distinct.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2426; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-03f1e441c0 | data/natural_products/terpenoids/yanuthone-d.yaml | generated | yanuthone D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-03f1e441c0 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-03f1e441c0 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-03f1e441c0 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-03f1e441c0 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-03f1e441c0 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-03f1e441c0 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-03f1e441c0 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-03f1e441c0 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identifier and structure correspondence

identity: supported. Targets: naturalproductmech:mibig-03f1e441c0.

Yanuthone D retains minted identifier naturalproductmech:mibig-03f1e441c0, full key NIBXHVDVUJEQPO-OFWAVEGMSA-N, npatlas:NPA013738 and pubchem:10436112. Its exact retained MIBiG structure and both accepted stored forms reproduce the key; the saved exact-key ChEBI structure join is empty. This supports the local MINTED route without establishing global ChEBI absence, a stereochemically complete natural molecule or external cross-reference validity.

### Stored topology and stereochemical limits

representation: supported. Targets: naturalproductmech:mibig-03f1e441c0.

Both stored forms give neutral C28H38O8, 36 heavy atoms and 37 bonds, with one specified and two unspecified tetrahedral centers plus two specified double bonds. The complete topology retains a three-membered epoxide, an unsaturated carbon six-ring, four carbonyls including an ester and a carboxylic acid, and the unsaturated carbon side chain; no saturated C5O cycle occurs. All ten comparisons and the supplied 36-atom match are consistent, while full_graph_identity_established remains false. The retained stereo_complete false and InChI question marks are not repaired by agreement between the two stored forms.

### Producer and locus evidence grades

provenance: supported. Targets: naturalproductmech:mibig-03f1e441c0.

MIBiG BGC0000170 version 3 is active with questionable quality and unknown completeness. Aspergillus niger ATCC 1015 (NCBITaxon:380704) remains a SOURCE_ASSERTION producer; ACJE01000012.1:25033–49030 remains CLUSTER_UNSTATED with no retained locus methods. Coordinates and the separate species-level occurrence do not upgrade this to demonstrated production or a resolved biosynthetic pathway.

### Citation tier and history scope

evidence: supported. Targets: naturalproductmech:mibig-03f1e441c0.

The producer/locus citation DOI:10.1016/j.chembiol.2014.01.013 is retained at COMPOUND_BIOACTIVITY level. Two LOTUS occurrences cite DOI:10.1016/J.CHEMBIOL.2014.01.013 and DOI:10.1021/JO0006831; case variants and repeated placement do not establish independent experiments. A compound-bioactivity citation does not itself provide a measured assay, potency, target or mechanism. The two seeding history events record provenance, and no primary article was freshly read.

### Occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-03f1e441c0.

Two retained LOTUS rows describe Aspergillus niger (NCBITaxon:5061), distinct from the ATCC 1015 producer assertion. CID10436112 has a blank-AID (no assay data) sentinel, with no measured outcome, potency, target or reference; it is not an inactivity result. CheBI origin, CyanometDB, BindingDB and AntibioticMech joins are empty in the exact saved scopes, and no bioactivity or molecular-target root exists. Those limits do not establish biological absence or transfer a biosynthetic role into pharmacology.

### Versioned classification applicability

consistency: supported. Targets: naturalproductmech:mibig-03f1e441c0.

NPClassifier npclassifier.gnps2.org@2026-09-07 retains Terpenoids/Meroterpenoids/Merosesquiterpenoids with is_glycoside false, while MIBiG independently records PKS. The unsaturated carbon side chain, oxygenated ring system and absence of a C5O candidate are compatible with the broad nonglycosidic meroterpenoid model scope. Model chemical classification and source BGC class answer different questions; their labels alone show no source-copying defect, and exact biosynthetic origin is not independently demonstrated.

### Review completion

completeness: unknown. Targets: naturalproductmech:mibig-03f1e441c0.

Complete current owner/history, accepted canonical intake, retained source scopes and both accepted saved molecular forms were read. No causal graph, pathway, declared component or molecular target is present, so no maintained reader applies to this owner. Source-qualified correspondence is supported, but unresolved stereochemistry, unavailable full QC/OAK coverage and absent fresh primary verification keep this review partial. No supported source-edit finding or action is established.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2426-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/yanuthone-d.yaml; Whole current plaintext and complete curation_history | supports | Complete owner and 2 history events personally read; current source/status preserved. |
| support-2426-capture | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/5/owner_document | supports | Whole captured owner retains exact present and absent roots. No causal graph, pathway, declared component or molecular target is present in this owner; no maintained reader applies. |
| support-2426-grounding-owner | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/5/owner_document/identifier; /records/5/owner_document/label; /records/5/owner_document/chemical_structure; /records/5/owner_document/source_concepts; /records/5/owner_document/xrefs; /records/5/owner_document/grounding_status; /records/5/owner_document/grounding_notes | supports | Retained identifier/full key, source structure, source concepts and grounding status. Only present roots are cited; no fresh external identity or cross-reference verification. |
| support-2426-origin-owner | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/5/owner_document/producer_organisms; /records/5/owner_document/biosynthetic_gene_clusters; /records/5/owner_document/producer_taxon_groups | supports | Producer and locus grades, versions, genome coordinates and citation tiers remain separate. No locus methods are retained. |
| support-2426-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/5/owner_document | supports | Two retained species-level occurrences; no related-record, bioactivity or molecular-target root. Whole-owner absence is bounded to this captured record; no universal biological absence is claimed. |
| support-2426-classification-owner | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/5/owner_document/np_pathway; /records/5/owner_document/np_classification; /records/5/owner_document/bgc_class; /records/5/owner_document/biosynthesis_origin | supports | Versioned model classification/glycoside output and source BGC/filing assertions remain distinct. |
| support-2426-direct-contexts | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-target-input-plan-001.json; /records/5/proposed_companion_paths; /records/5/direct_companion_predicates; /records/5/additional_context_roles | context_only | Exact one-hop context predicates and input roles; no transitive expansion or transfer of identity, production, activity or reaction evidence. |
| support-2426-intake | /private/tmp/npm-review-work/shared-next-batch243/intakes/2426-inspect-001.json; /targets; /source | supports | Actual canonical single-target inspection, complete ownership and immutable input roles. |
| support-2426-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch243/root-intake-acceptance-001.json; /status; /summary; /intakes/5; /source_plan; /verification | supports | ROOT accepts this original canonical intake and all ten source-aligned input maps. |
| support-2426-intake-reading | /private/tmp/npm-review-work/shared-next-batch243-tentative/support-prep/support-current243-last-five-intake-reading-001.json; /reading; /records/0; /input_placements; /unique_input_paths | supports | Complete last-five intake reading with exact shared-baseline factoring: 201 placements over 42 paths. ROOT operated the original controller. |
| support-2426-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch243/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /scope | supports | Original local extraction is accepted; its retained assertions are not fresh primary verification. |
| support-2426-plan | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-target-input-plan-001.json; /records/5/proposed_input_paths; /records/5/proposed_input_count | supports | Actual immutable input plan agrees with this canonical intake. |
| support-2426-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch243/root-source-plan-acceptance-001.json; /status; /plan; /verification | supports | ROOT accepts the composed source plan and exact inventory/notes/input reconciliation. |
| support-2426-source-reading | /private/tmp/npm-review-work/shared-next-batch243-tentative/support-prep/support-current243-source-reading-002.json; /division; /reading; /contexts; /cautions | supports | Support personally read 45 selected query frames, 13 positive rows and 183 fields, plus the unselected Yossoside V context with 9 frames, 2 rows and 32 fields. Complete raw/history carries and Native/BGC attributions remain explicit; no replay or duplicate row credit. |
| support-2426-source-notes | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /limitations | context_only | Joint notes preserve disjoint source reading, exact companion scope and Native cache/curation attribution; retained assertions remain bounded. |
| support-2426-molecular-reading | /private/tmp/npm-review-work/shared-next-batch243-tentative/support-prep/support-current243-last-five-molecular-reading-001.json; /reading; /coverage; /records/0; /limits | supports | Support personally read all ten last-five saved forms: 658 atom rows and 720 bond rows, complete strings, stereo/rings/motifs and correspondence, with lossless table presentation. |
| support-2426-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /cached_taxonomy | context_only | Retained cache keeps Aspergillus niger species5061 and ATCC 1015 strain380704 distinct. No unmatched/forward-merge route exists in this saved scope; cache names do not prove production or fresh taxonomy. |
| support-2426-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch243-tentative/native-prep/native-current243-cached-taxonomy-reading-001.json; /scope; /taxonomy; /interpretation; /reading_outputs; /limitations | context_only | Native complete eight-stanza and route reading is attributed; cached name/synonym correspondence is not fresh taxonomy or production evidence. |
| support-2426-curation-scope | /private/tmp/npm-review-work/shared-next-batch243-tentative/native-prep/native-current243-implemented-curation-scan-001.json; /scope; /table_pins; /positive_lexical_matches; /applicable_corrections_or_exclusions; /assays; /guidance | context_only | Native saved scan found no applicable correction/exclusion; four lexical hits were unrelated. No assay or scientific validation follows from an empty applicable set. |
| support-2426-chemistry | /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/literal_InChI_layers; /records/5/formula_comparison_scope; /records/5/comparisons; /records/5/atom_correspondence | supports | All ten owner comparisons are true and the supplied chirality-aware atom-count match is complete; full_graph_identity_established remains false. Retained unresolved stereochemistry persists. |
| support-2426-topology | /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-DATA-001.json; /records/5/smiles; /records/5/inchi; /records/5/comparisons; /records/5/atom_correspondence; /records/5/declared_structure | supports | Both stored forms give neutral C28H38O8, 36 heavy atoms and 37 bonds, with one specified and two unspecified tetrahedral centers plus two specified double bonds. The complete topology retains a three-membered epoxide, an unsaturated carbon six-ring, four carbonyls including an ester and a carboxylic acid, and the unsaturated carbon side chain; no saturated C5O cycle occurs. All ten comparisons and the supplied 36-atom match are consistent, while full_graph_identity_established remains false. The retained stereo_complete false and InChI question marks are not repaired by agreement between the two stored forms. |
| support-2426-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /verification; /scalar_results/5; /warnings; /limitations | supports | ROOT accepts the original twenty-form diagnostic. This owner has ten true comparison flags; the cohort’s false Xanthan formula flag and four unassigned global warnings remain preserved. |
| support-2426-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic exit 0 with preserved streams, no retry or external request. |
| support-2426-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-original-001.stderr; Whole original stderr (182 bytes) | context_only | Two proton and two undefined-stereo warnings are global and unassigned; no owner-specific attribution or empty-stderr claim. |
| support-2426-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2426-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2426-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2426-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2426-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame: 1 matched placements. Empty results are limited to the exact retained predicate. |
| support-2426-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Retained physical row 217: BGC0000170 v3, compound 1 yanuthone D; active/questionable/unknown; Aspergillus niger ATCC 1015 (NCBITaxon:380704) SOURCE_ASSERTION, locus CLUSTER_UNSTATED; DOI:10.1016/j.chembiol.2014.01.013 at COMPOUND_BIOACTIVITY level. Full structure, coordinates and methods remain source-scoped in this row. |
| support-2426-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 217 | context_only | Every saved source field matches the exact physical retained row; no source query. |
| support-2426-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame: 0 matched placements. Empty results are limited to the exact retained predicate. |
| support-2426-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame: 2 matched placements. Empty results are limited to the exact retained predicate. |
| support-2426-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Retained physical row 6000: Aspergillus niger (NCBITaxon:5061), DOI:10.1016/J.CHEMBIOL.2014.01.013; exact-full-key occurrence assertion, not production or independent-experiment proof. |
| support-2426-source-lotus_occurrences-1 | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/lotus_occurrences/matches/1 | supports | Retained physical row 6001: Aspergillus niger (NCBITaxon:5061), DOI:10.1021/JO0006831; exact-full-key occurrence assertion, not production or independent-experiment proof. |
| support-2426-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 6000, 6001 | context_only | Every saved source field matches the exact physical retained row; no source query. |
| support-2426-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame: 0 matched placements. Empty results are limited to the exact retained predicate. |
| support-2426-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame: 1 matched placements. Empty results are limited to the exact retained predicate. |
| support-2426-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/npclassifier/matches/0 | supports | Retained physical row 1606: npclassifier.gnps2.org@2026-09-07: Terpenoids/Meroterpenoids/Merosesquiterpenoids; is_glycoside=false. Model output remains distinct from source assertion. |
| support-2426-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 1606 | context_only | Every saved source field matches the exact physical retained row; no source query. |
| support-2426-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame: 1 matched placements. Empty results are limited to the exact retained predicate. |
| support-2426-source-pubchem_bioassay-0 | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/pubchem_bioassay/matches/0 | supports | Retained physical row 4465: CID10436112, blank AID and (no assay data) sentinel; no measured outcome, potency, target or reference. |
| support-2426-physical-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 4465 | context_only | Every saved source field matches the exact physical retained row; no source query. |
| support-2426-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame: 0 matched placements. Empty results are limited to the exact retained predicate. |
| support-2426-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame: 0 matched placements. Empty results are limited to the exact retained predicate. |
| support-2426-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame: 0 matched placements. Empty results are limited to the exact retained predicate. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-243/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-243/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-243/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-243/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-243/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; primary literature, current taxonomy, natural identity and external cross-references were not freshly verified.
- Full QC and complete OAK authority coverage remain unavailable. Local checks do not replace those authorities.
- All five stored structures disclose incomplete tetrahedral stereochemistry. All full-graph-identity flags remain false; four global diagnostic warnings remain unassigned.
- Producer, occurrence, locus, model, citation, companion and assay scopes remain separate. No record edit or pharmacological mechanism is inferred.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five whole selected owners/history, 45 selected frames/13 rows/183 fields, plus unselected Yossoside V with 9 frames/2 rows/32 fields. BGC other-source and Native cache/curation credit remain separate.
- All ten last-five stored forms were personally read: 658 atom rows and 720 bond rows with complete strings/stereo/rings/motifs/maps; no new parse.
- ROOT operated the original canonical intake; native_checks operated the original molecular diagnostic under ROOT delegation. This half has 201 actual intake placements across 42 paths. No maintained reader applies to these five owners; the cohort’s 2422 reader is separate.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T174833Z-yanuthone-d
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: yanuthone D'
started_at: '2026-11-04T16:43:12.852179Z'
finished_at: '2026-11-04T17:48:33.936302Z'
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
summary: Yanuthone D has consistent retained structure/key encodings with two unresolved
  tetrahedral centers. Its source-qualified ATCC 1015 producer/locus claim, species
  occurrences and blank-assay sentinel remain distinct.
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
  - path: data/natural_products/terpenoids/yanuthone-d.yaml
    sha256: 31dea0846e8b484b9167ae83114f89cf49415d7f0613eb3e0c4149912b7ba7c9
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
  selection: Campaign path order 2426; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-03f1e441c0
targets:
- target_id: naturalproductmech:mibig-03f1e441c0
  path: data/natural_products/terpenoids/yanuthone-d.yaml
  label: yanuthone D
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
  - naturalproductmech:mibig-03f1e441c0
  command: just validate-strict data/natural_products/terpenoids/trehangelin.yaml
    data/natural_products/terpenoids/trichobrasilenol.yaml data/natural_products/terpenoids/viguiepinol.yaml
    data/natural_products/terpenoids/xanthan.yaml data/natural_products/terpenoids/xylarenic-acid-b.yaml
    data/natural_products/terpenoids/yanuthone-d.yaml data/natural_products/terpenoids/yossoside-i.yaml
    data/natural_products/terpenoids/yossoside-ii.yaml data/natural_products/terpenoids/yossoside-iii.yaml
    data/natural_products/terpenoids/yossoside-iv.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-243/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-03f1e441c0
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-243/validate-all-001.tsv
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
  - naturalproductmech:mibig-03f1e441c0
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
  - naturalproductmech:mibig-03f1e441c0
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
  - naturalproductmech:mibig-03f1e441c0
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-243/review-queue-001.tsv
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
  - naturalproductmech:mibig-03f1e441c0
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-03f1e441c0
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-03f1e441c0
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2426-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/yanuthone-d.yaml
  locator: Whole current plaintext and complete curation_history
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Complete owner and 2 history events personally read; current source/status
    preserved.
  snapshot_sha256: 31dea0846e8b484b9167ae83114f89cf49415d7f0613eb3e0c4149912b7ba7c9
- evidence_id: support-2426-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/5/owner_document
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Whole captured owner retains exact present and absent roots. No causal
    graph, pathway, declared component or molecular target is present in this owner;
    no maintained reader applies.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: support-2426-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/5/owner_document/identifier; /records/5/owner_document/label;
    /records/5/owner_document/chemical_structure; /records/5/owner_document/source_concepts;
    /records/5/owner_document/xrefs; /records/5/owner_document/grounding_status; /records/5/owner_document/grounding_notes
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Retained identifier/full key, source structure, source concepts and grounding
    status. Only present roots are cited; no fresh external identity or cross-reference
    verification.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: support-2426-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/5/owner_document/producer_organisms; /records/5/owner_document/biosynthetic_gene_clusters;
    /records/5/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Producer and locus grades, versions, genome coordinates and citation tiers
    remain separate. No locus methods are retained.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: support-2426-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/5/owner_document
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Two retained species-level occurrences; no related-record, bioactivity
    or molecular-target root. Whole-owner absence is bounded to this captured record;
    no universal biological absence is claimed.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: support-2426-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/5/owner_document/np_pathway; /records/5/owner_document/np_classification;
    /records/5/owner_document/bgc_class; /records/5/owner_document/biosynthesis_origin
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Versioned model classification/glycoside output and source BGC/filing assertions
    remain distinct.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: support-2426-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-target-input-plan-001.json
  locator: /records/5/proposed_companion_paths; /records/5/direct_companion_predicates;
    /records/5/additional_context_roles
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Exact one-hop context predicates and input roles; no transitive expansion
    or transfer of identity, production, activity or reaction evidence.
  snapshot_sha256: 91ac3acc1e6264332df09dbaac2293537c6c971feaddfd56c7c06d905026a0cd
- evidence_id: support-2426-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243/intakes/2426-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Actual canonical single-target inspection, complete ownership and immutable
    input roles.
  snapshot_sha256: f898a00333ba1f9cf7c13c5ac3c086eb093ed6058472b09c83371d11c7208054
- evidence_id: support-2426-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243/root-intake-acceptance-001.json
  locator: /status; /summary; /intakes/5; /source_plan; /verification
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: ROOT accepts this original canonical intake and all ten source-aligned
    input maps.
  snapshot_sha256: b147ca209359c57adf20c4cd992acef2e7e20a63a82f6736763f7bcc4f9ba609
- evidence_id: support-2426-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/support-prep/support-current243-last-five-intake-reading-001.json
  locator: /reading; /records/0; /input_placements; /unique_input_paths
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Complete last-five intake reading with exact shared-baseline factoring:
    201 placements over 42 paths. ROOT operated the original controller.'
  snapshot_sha256: 0eb1044d531387a4f3261be0d5d76ba004bae83fe307161a84a48304896bf0fb
- evidence_id: support-2426-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /scope
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Original local extraction is accepted; its retained assertions are not
    fresh primary verification.
  snapshot_sha256: 185a21da0cf68b366f8d56d4fc35dcb4b8e44c6f08e136ba79a7d71f1fc01e45
- evidence_id: support-2426-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-target-input-plan-001.json
  locator: /records/5/proposed_input_paths; /records/5/proposed_input_count
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Actual immutable input plan agrees with this canonical intake.
  snapshot_sha256: 91ac3acc1e6264332df09dbaac2293537c6c971feaddfd56c7c06d905026a0cd
- evidence_id: support-2426-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243/root-source-plan-acceptance-001.json
  locator: /status; /plan; /verification
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: ROOT accepts the composed source plan and exact inventory/notes/input reconciliation.
  snapshot_sha256: 3654dc31a31787379bb3afc90c454264eead72eb18553e3b753539911bb06391
- evidence_id: support-2426-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/support-prep/support-current243-source-reading-002.json
  locator: /division; /reading; /contexts; /cautions
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Support personally read 45 selected query frames, 13 positive rows and
    183 fields, plus the unselected Yossoside V context with 9 frames, 2 rows and
    32 fields. Complete raw/history carries and Native/BGC attributions remain explicit;
    no replay or duplicate row credit.
  snapshot_sha256: 03c37b10dd24d06fd043419ef5a2b231357359f1e5a2db071a2eb4e5b9b6939d
- evidence_id: support-2426-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /limitations
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Joint notes preserve disjoint source reading, exact companion scope and
    Native cache/curation attribution; retained assertions remain bounded.
  snapshot_sha256: f9cb956d084c97bd6e0eda881981ffd6089e8271792437c1b94188d8afd65a40
- evidence_id: support-2426-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/support-prep/support-current243-last-five-molecular-reading-001.json
  locator: /reading; /coverage; /records/0; /limits
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Support personally read all ten last-five saved forms: 658 atom rows and
    720 bond rows, complete strings, stereo/rings/motifs and correspondence, with
    lossless table presentation.'
  snapshot_sha256: 1d69609edf4ebacb94e69a2382930c9eae40454f0df83fbfd1c3d1c11c8ec911
- evidence_id: support-2426-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /cached_taxonomy
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Retained cache keeps Aspergillus niger species5061 and ATCC 1015 strain380704
    distinct. No unmatched/forward-merge route exists in this saved scope; cache names
    do not prove production or fresh taxonomy.
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
- evidence_id: support-2426-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/native-prep/native-current243-cached-taxonomy-reading-001.json
  locator: /scope; /taxonomy; /interpretation; /reading_outputs; /limitations
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Native complete eight-stanza and route reading is attributed; cached name/synonym
    correspondence is not fresh taxonomy or production evidence.
  snapshot_sha256: 7eb3dc20b9bb5259d999c82830a794576f16aee4c95cd1b69d0f07145000e7ee
- evidence_id: support-2426-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/native-prep/native-current243-implemented-curation-scan-001.json
  locator: /scope; /table_pins; /positive_lexical_matches; /applicable_corrections_or_exclusions;
    /assays; /guidance
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Native saved scan found no applicable correction/exclusion; four lexical
    hits were unrelated. No assay or scientific validation follows from an empty applicable
    set.
  snapshot_sha256: b6f3bec95f889d74d38d39907c3c311b066e0611ca3512cf3e6e73d719eb4aa7
  search_scope: '{"claim": "No exact applicable correction in this bounded saved identity
    scope; not universal absence.", "contexts": 15, "diagnostic_rows": 3329, "diagnostic_tables":
    1, "full_key": "NIBXHVDVUJEQPO-OFWAVEGMSA-N", "ignored_files_included": true,
    "implemented_rows": 93, "implemented_tables": 8, "owner": "naturalproductmech:mibig-03f1e441c0",
    "retained_scan": "/private/tmp/npm-review-work/shared-next-batch243-tentative/native-prep/native-current243-implemented-curation-scan-001.json#/scope",
    "tokens": 120}'
- evidence_id: support-2426-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/literal_InChI_layers; /records/5/formula_comparison_scope;
    /records/5/comparisons; /records/5/atom_correspondence
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: All ten owner comparisons are true and the supplied chirality-aware atom-count
    match is complete; full_graph_identity_established remains false. Retained unresolved
    stereochemistry persists.
  snapshot_sha256: 69a149d2f7c4a56aecea9a32f5ae0456c00a18f05bc12f14b0a0fbd95911976f
- evidence_id: support-2426-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/smiles; /records/5/inchi; /records/5/comparisons; /records/5/atom_correspondence;
    /records/5/declared_structure
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Both stored forms give neutral C28H38O8, 36 heavy atoms and 37 bonds, with
    one specified and two unspecified tetrahedral centers plus two specified double
    bonds. The complete topology retains a three-membered epoxide, an unsaturated
    carbon six-ring, four carbonyls including an ester and a carboxylic acid, and
    the unsaturated carbon side chain; no saturated C5O cycle occurs. All ten comparisons
    and the supplied 36-atom match are consistent, while full_graph_identity_established
    remains false. The retained stereo_complete false and InChI question marks are
    not repaired by agreement between the two stored forms.
  snapshot_sha256: 69a149d2f7c4a56aecea9a32f5ae0456c00a18f05bc12f14b0a0fbd95911976f
- evidence_id: support-2426-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /verification; /scalar_results/5; /warnings;
    /limitations
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: ROOT accepts the original twenty-form diagnostic. This owner has ten true
    comparison flags; the cohort’s false Xanthan formula flag and four unassigned
    global warnings remain preserved.
  snapshot_sha256: a93e9d5429154ef3e54a1049299fd86065e7551df82beb9c49e91b848fa65787
- evidence_id: support-2426-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: Original diagnostic exit 0 with preserved streams, no retry or external
    request.
  snapshot_sha256: 0129f39cb4f9773ffa73ced786859b7d33905900d2c1d092d54ed2839f17d6d4
- evidence_id: support-2426-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr (182 bytes)
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Two proton and two undefined-stereo warnings are global and unassigned;
    no owner-specific attribution or empty-stderr claim.
  snapshot_sha256: d0ceeac20ba707de6d92f53f5fcc172936f73802c999710e38f50ec0447e15d9
- evidence_id: support-2426-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2426-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2426-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2426-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2426-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Saved mibig_compounds frame: 1 matched placements. Empty results are limited
    to the exact retained predicate.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "NIBXHVDVUJEQPO-OFWAVEGMSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/mibig_compounds",
    "scope": "Immutable retained local inventory only; no replay, external request
    or universal absence claim."}'
- evidence_id: support-2426-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Retained physical row 217: BGC0000170 v3, compound 1 yanuthone D; active/questionable/unknown;
    Aspergillus niger ATCC 1015 (NCBITaxon:380704) SOURCE_ASSERTION, locus CLUSTER_UNSTATED;
    DOI:10.1016/j.chembiol.2014.01.013 at COMPOUND_BIOACTIVITY level. Full structure,
    coordinates and methods remain source-scoped in this row.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
- evidence_id: support-2426-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 217
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Every saved source field matches the exact physical retained row; no source
    query.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2426-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Saved chebi_structures frame: 0 matched placements. Empty results are
    limited to the exact retained predicate.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "NIBXHVDVUJEQPO-OFWAVEGMSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/chebi_structures",
    "scope": "Immutable retained local inventory only; no replay, external request
    or universal absence claim."}'
- evidence_id: support-2426-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Saved lotus_occurrences frame: 2 matched placements. Empty results are
    limited to the exact retained predicate.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "NIBXHVDVUJEQPO-OFWAVEGMSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Immutable retained local inventory only; no replay, external request
    or universal absence claim."}'
- evidence_id: support-2426-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Retained physical row 6000: Aspergillus niger (NCBITaxon:5061), DOI:10.1016/J.CHEMBIOL.2014.01.013;
    exact-full-key occurrence assertion, not production or independent-experiment
    proof.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
- evidence_id: support-2426-source-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/lotus_occurrences/matches/1
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Retained physical row 6001: Aspergillus niger (NCBITaxon:5061), DOI:10.1021/JO0006831;
    exact-full-key occurrence assertion, not production or independent-experiment
    proof.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
- evidence_id: support-2426-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 6000, 6001
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Every saved source field matches the exact physical retained row; no source
    query.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2426-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Saved cyanometdb_occurrences frame: 0 matched placements. Empty results
    are limited to the exact retained predicate.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "NIBXHVDVUJEQPO-OFWAVEGMSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Immutable retained local inventory only; no replay, external request
    or universal absence claim."}'
- evidence_id: support-2426-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Saved npclassifier frame: 1 matched placements. Empty results are limited
    to the exact retained predicate.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "NIBXHVDVUJEQPO-OFWAVEGMSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/npclassifier",
    "scope": "Immutable retained local inventory only; no replay, external request
    or universal absence claim."}'
- evidence_id: support-2426-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Retained physical row 1606: npclassifier.gnps2.org@2026-09-07: Terpenoids/Meroterpenoids/Merosesquiterpenoids;
    is_glycoside=false. Model output remains distinct from source assertion.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
- evidence_id: support-2426-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 1606
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Every saved source field matches the exact physical retained row; no source
    query.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2426-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Saved pubchem_bioassay frame: 1 matched placements. Empty results are
    limited to the exact retained predicate.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "NIBXHVDVUJEQPO-OFWAVEGMSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Immutable retained local inventory only; no replay, external request
    or universal absence claim."}'
- evidence_id: support-2426-source-pubchem_bioassay-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/pubchem_bioassay/matches/0
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Retained physical row 4465: CID10436112, blank AID and (no assay data)
    sentinel; no measured outcome, potency, target or reference.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
- evidence_id: support-2426-physical-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 4465
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: context_only
  summary: Every saved source field matches the exact physical retained row; no source
    query.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2426-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Saved bindingdb_targets frame: 0 matched placements. Empty results are
    limited to the exact retained predicate.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "NIBXHVDVUJEQPO-OFWAVEGMSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Immutable retained local inventory only; no replay, external request
    or universal absence claim."}'
- evidence_id: support-2426-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Saved antibioticmech_inchikeys frame: 0 matched placements. Empty results
    are limited to the exact retained predicate.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "NIBXHVDVUJEQPO-OFWAVEGMSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Immutable retained local inventory only; no replay, external request
    or universal absence claim."}'
- evidence_id: support-2426-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T17:33:24.728915Z'
  support: supports
  summary: 'Saved chebi_origins frame: 0 matched placements. Empty results are limited
    to the exact retained predicate.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/9/source_scope_inventory/joins/chebi_origins",
    "scope": "Immutable retained local inventory only; no replay, external request
    or universal absence claim."}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-243/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json
  accessed_at: '2026-11-04T16:55:02.739193Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: d4bd86d11da0cdff7ea8d2f5e606f7acf91688bd00ade940fd6f64bed0849036
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-243/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json
  accessed_at: '2026-11-04T16:55:27.551506Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 0fc23d99fc43282086aac001026995a6b725d41dd7ca97d430a2d4af2e8cad4b
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-243/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json
  accessed_at: '2026-11-04T16:55:47.023037Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-243/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json
  accessed_at: '2026-11-04T16:56:20.820932Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-243/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json
  accessed_at: '2026-11-04T16:56:32.540355Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: c1ffddf8e5ee40c30ec339073c0402934ebfb573993911f7fc890b95e4ac8fe5
assessments:
- area: identity
  topic: Retained identifier and structure correspondence
  outcome: supported
  summary: Yanuthone D retains minted identifier naturalproductmech:mibig-03f1e441c0,
    full key NIBXHVDVUJEQPO-OFWAVEGMSA-N, npatlas:NPA013738 and pubchem:10436112.
    Its exact retained MIBiG structure and both accepted stored forms reproduce the
    key; the saved exact-key ChEBI structure join is empty. This supports the local
    MINTED route without establishing global ChEBI absence, a stereochemically complete
    natural molecule or external cross-reference validity.
  assessment_id: support-2426-identity
  target_ids:
  - naturalproductmech:mibig-03f1e441c0
  evidence_ids:
  - support-2426-grounding-owner
  - support-2426-chemistry
  - support-2426-direct-contexts
  - support-2426-query-chebi_structures
  - support-2426-source-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: NIBXHVDVUJEQPO-OFWAVEGMSA-N; retained exact full key, not independent natural
      identity.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2426-grounding-owner
    - support-2426-chemistry
    - support-2426-direct-contexts
    - support-2426-query-chebi_structures
    - support-2426-source-mibig_compounds-0
  - name: grounding_scope
    value: Yanuthone D retains minted identifier naturalproductmech:mibig-03f1e441c0,
      full key NIBXHVDVUJEQPO-OFWAVEGMSA-N, npatlas:NPA013738 and pubchem:10436112.
      Its exact retained MIBiG structure and both accepted stored forms reproduce
      the key; the saved exact-key ChEBI structure join is empty. This supports the
      local MINTED route without establishing global ChEBI absence, a stereochemically
      complete natural molecule or external cross-reference validity.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2426-grounding-owner
    - support-2426-chemistry
    - support-2426-direct-contexts
    - support-2426-query-chebi_structures
    - support-2426-source-mibig_compounds-0
- area: representation
  topic: Stored topology and stereochemical limits
  outcome: supported
  summary: Both stored forms give neutral C28H38O8, 36 heavy atoms and 37 bonds, with
    one specified and two unspecified tetrahedral centers plus two specified double
    bonds. The complete topology retains a three-membered epoxide, an unsaturated
    carbon six-ring, four carbonyls including an ester and a carboxylic acid, and
    the unsaturated carbon side chain; no saturated C5O cycle occurs. All ten comparisons
    and the supplied 36-atom match are consistent, while full_graph_identity_established
    remains false. The retained stereo_complete false and InChI question marks are
    not repaired by agreement between the two stored forms.
  assessment_id: support-2426-representation
  target_ids:
  - naturalproductmech:mibig-03f1e441c0
  evidence_ids:
  - support-2426-grounding-owner
  - support-2426-chemistry
  - support-2426-topology
  - support-2426-molecular-reading
  - support-2426-diagnostic-acceptance
  - support-2426-structure-schema
  - support-2426-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both stored forms give neutral C28H38O8, 36 heavy atoms and 37 bonds, with
      one specified and two unspecified tetrahedral centers plus two specified double
      bonds. The complete topology retains a three-membered epoxide, an unsaturated
      carbon six-ring, four carbonyls including an ester and a carboxylic acid, and
      the unsaturated carbon side chain; no saturated C5O cycle occurs. All ten comparisons
      and the supplied 36-atom match are consistent, while full_graph_identity_established
      remains false. The retained stereo_complete false and InChI question marks are
      not repaired by agreement between the two stored forms.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2426-grounding-owner
    - support-2426-chemistry
    - support-2426-topology
    - support-2426-molecular-reading
    - support-2426-diagnostic-acceptance
    - support-2426-structure-schema
    - support-2426-stereo-method
  - name: representation_correspondence
    value: All ten saved comparisons and supplied atom-count match are true; full_graph_identity_established
      is false. Neither agreement nor the map resolves absent stereochemistry.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2426-grounding-owner
    - support-2426-chemistry
    - support-2426-topology
    - support-2426-molecular-reading
    - support-2426-diagnostic-acceptance
    - support-2426-structure-schema
    - support-2426-stereo-method
- area: provenance
  topic: Producer and locus evidence grades
  outcome: supported
  summary: MIBiG BGC0000170 version 3 is active with questionable quality and unknown
    completeness. Aspergillus niger ATCC 1015 (NCBITaxon:380704) remains a SOURCE_ASSERTION
    producer; ACJE01000012.1:25033–49030 remains CLUSTER_UNSTATED with no retained
    locus methods. Coordinates and the separate species-level occurrence do not upgrade
    this to demonstrated production or a resolved biosynthetic pathway.
  assessment_id: support-2426-provenance
  target_ids:
  - naturalproductmech:mibig-03f1e441c0
  evidence_ids:
  - support-2426-origin-owner
  - support-2426-source-reading
  - support-2426-direct-contexts
  - support-2426-cached-taxonomy
  - support-2426-taxonomy-reading
  - support-2426-curation-scope
  - support-2426-source-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0000170 version 3 is active with questionable quality and unknown
      completeness. Aspergillus niger ATCC 1015 (NCBITaxon:380704) remains a SOURCE_ASSERTION
      producer; ACJE01000012.1:25033–49030 remains CLUSTER_UNSTATED with no retained
      locus methods. Coordinates and the separate species-level occurrence do not
      upgrade this to demonstrated production or a resolved biosynthetic pathway.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2426-origin-owner
    - support-2426-source-reading
    - support-2426-direct-contexts
    - support-2426-cached-taxonomy
    - support-2426-taxonomy-reading
    - support-2426-curation-scope
    - support-2426-source-mibig_compounds-0
  - name: producer_evidence
    value: MIBiG BGC0000170 version 3 is active with questionable quality and unknown
      completeness. Aspergillus niger ATCC 1015 (NCBITaxon:380704) remains a SOURCE_ASSERTION
      producer; ACJE01000012.1:25033–49030 remains CLUSTER_UNSTATED with no retained
      locus methods. Coordinates and the separate species-level occurrence do not
      upgrade this to demonstrated production or a resolved biosynthetic pathway.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2426-origin-owner
    - support-2426-source-reading
    - support-2426-direct-contexts
    - support-2426-cached-taxonomy
    - support-2426-taxonomy-reading
    - support-2426-curation-scope
    - support-2426-source-mibig_compounds-0
  - name: locus_evidence
    value: MIBiG BGC0000170 version 3 is active with questionable quality and unknown
      completeness. Aspergillus niger ATCC 1015 (NCBITaxon:380704) remains a SOURCE_ASSERTION
      producer; ACJE01000012.1:25033–49030 remains CLUSTER_UNSTATED with no retained
      locus methods. Coordinates and the separate species-level occurrence do not
      upgrade this to demonstrated production or a resolved biosynthetic pathway.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2426-origin-owner
    - support-2426-source-reading
    - support-2426-direct-contexts
    - support-2426-cached-taxonomy
    - support-2426-taxonomy-reading
    - support-2426-curation-scope
    - support-2426-source-mibig_compounds-0
- area: evidence
  topic: Citation tier and history scope
  outcome: supported
  summary: The producer/locus citation DOI:10.1016/j.chembiol.2014.01.013 is retained
    at COMPOUND_BIOACTIVITY level. Two LOTUS occurrences cite DOI:10.1016/J.CHEMBIOL.2014.01.013
    and DOI:10.1021/JO0006831; case variants and repeated placement do not establish
    independent experiments. A compound-bioactivity citation does not itself provide
    a measured assay, potency, target or mechanism. The two seeding history events
    record provenance, and no primary article was freshly read.
  assessment_id: support-2426-citations
  target_ids:
  - naturalproductmech:mibig-03f1e441c0
  evidence_ids:
  - support-2426-grounding-owner
  - support-2426-origin-owner
  - support-2426-occurrence-activity-owner
  - support-2426-source-reading
  - support-2426-direct-contexts
  - support-2426-source-mibig_compounds-0
  - support-2426-source-lotus_occurrences-0
  - support-2426-source-lotus_occurrences-1
  - support-2426-source-npclassifier-0
  - support-2426-source-pubchem_bioassay-0
  dimensions:
  - name: citation_scope
    value: The producer/locus citation DOI:10.1016/j.chembiol.2014.01.013 is retained
      at COMPOUND_BIOACTIVITY level. Two LOTUS occurrences cite DOI:10.1016/J.CHEMBIOL.2014.01.013
      and DOI:10.1021/JO0006831; case variants and repeated placement do not establish
      independent experiments. A compound-bioactivity citation does not itself provide
      a measured assay, potency, target or mechanism. The two seeding history events
      record provenance, and no primary article was freshly read.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2426-grounding-owner
    - support-2426-origin-owner
    - support-2426-occurrence-activity-owner
    - support-2426-source-reading
    - support-2426-direct-contexts
    - support-2426-source-mibig_compounds-0
    - support-2426-source-lotus_occurrences-0
    - support-2426-source-lotus_occurrences-1
    - support-2426-source-npclassifier-0
    - support-2426-source-pubchem_bioassay-0
- area: evidence
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: Two retained LOTUS rows describe Aspergillus niger (NCBITaxon:5061), distinct
    from the ATCC 1015 producer assertion. CID10436112 has a blank-AID (no assay data)
    sentinel, with no measured outcome, potency, target or reference; it is not an
    inactivity result. CheBI origin, CyanometDB, BindingDB and AntibioticMech joins
    are empty in the exact saved scopes, and no bioactivity or molecular-target root
    exists. Those limits do not establish biological absence or transfer a biosynthetic
    role into pharmacology.
  assessment_id: support-2426-occurrence
  target_ids:
  - naturalproductmech:mibig-03f1e441c0
  evidence_ids:
  - support-2426-occurrence-activity-owner
  - support-2426-direct-contexts
  - support-2426-cached-taxonomy
  - support-2426-curation-scope
  - support-2426-query-lotus_occurrences
  - support-2426-query-chebi_origins
  - support-2426-query-cyanometdb_occurrences
  - support-2426-query-pubchem_bioassay
  - support-2426-query-bindingdb_targets
  - support-2426-query-antibioticmech_inchikeys
  - support-2426-source-lotus_occurrences-0
  - support-2426-source-lotus_occurrences-1
  - support-2426-source-pubchem_bioassay-0
  dimensions:
  - name: occurrence_scope
    value: Two retained LOTUS rows describe Aspergillus niger (NCBITaxon:5061), distinct
      from the ATCC 1015 producer assertion. CID10436112 has a blank-AID (no assay
      data) sentinel, with no measured outcome, potency, target or reference; it is
      not an inactivity result. CheBI origin, CyanometDB, BindingDB and AntibioticMech
      joins are empty in the exact saved scopes, and no bioactivity or molecular-target
      root exists. Those limits do not establish biological absence or transfer a
      biosynthetic role into pharmacology.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2426-occurrence-activity-owner
    - support-2426-direct-contexts
    - support-2426-cached-taxonomy
    - support-2426-curation-scope
    - support-2426-query-lotus_occurrences
    - support-2426-query-chebi_origins
    - support-2426-query-cyanometdb_occurrences
    - support-2426-query-pubchem_bioassay
    - support-2426-query-bindingdb_targets
    - support-2426-query-antibioticmech_inchikeys
    - support-2426-source-lotus_occurrences-0
    - support-2426-source-lotus_occurrences-1
    - support-2426-source-pubchem_bioassay-0
  - name: assay_target_scope
    value: One blank-AID PubChem sentinel; no measured assay, potency or target. The
      compound-bioactivity citation is not an assay result.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2426-occurrence-activity-owner
    - support-2426-direct-contexts
    - support-2426-cached-taxonomy
    - support-2426-curation-scope
    - support-2426-query-lotus_occurrences
    - support-2426-query-chebi_origins
    - support-2426-query-cyanometdb_occurrences
    - support-2426-query-pubchem_bioassay
    - support-2426-query-bindingdb_targets
    - support-2426-query-antibioticmech_inchikeys
    - support-2426-source-lotus_occurrences-0
    - support-2426-source-lotus_occurrences-1
    - support-2426-source-pubchem_bioassay-0
- area: consistency
  topic: Versioned classification applicability
  outcome: supported
  summary: NPClassifier npclassifier.gnps2.org@2026-09-07 retains Terpenoids/Meroterpenoids/Merosesquiterpenoids
    with is_glycoside false, while MIBiG independently records PKS. The unsaturated
    carbon side chain, oxygenated ring system and absence of a C5O candidate are compatible
    with the broad nonglycosidic meroterpenoid model scope. Model chemical classification
    and source BGC class answer different questions; their labels alone show no source-copying
    defect, and exact biosynthetic origin is not independently demonstrated.
  assessment_id: support-2426-classification
  target_ids:
  - naturalproductmech:mibig-03f1e441c0
  evidence_ids:
  - support-2426-classification-owner
  - support-2426-chemistry
  - support-2426-topology
  - support-2426-structure-schema
  - support-2426-classification-seeder
  - support-2426-source-mibig_compounds-0
  - support-2426-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: NPClassifier npclassifier.gnps2.org@2026-09-07 retains Terpenoids/Meroterpenoids/Merosesquiterpenoids
      with is_glycoside false, while MIBiG independently records PKS. The unsaturated
      carbon side chain, oxygenated ring system and absence of a C5O candidate are
      compatible with the broad nonglycosidic meroterpenoid model scope. Model chemical
      classification and source BGC class answer different questions; their labels
      alone show no source-copying defect, and exact biosynthetic origin is not independently
      demonstrated.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2426-classification-owner
    - support-2426-chemistry
    - support-2426-topology
    - support-2426-structure-schema
    - support-2426-classification-seeder
    - support-2426-source-mibig_compounds-0
    - support-2426-source-npclassifier-0
- area: completeness
  topic: Review completion
  outcome: unknown
  summary: Complete current owner/history, accepted canonical intake, retained source
    scopes and both accepted saved molecular forms were read. No causal graph, pathway,
    declared component or molecular target is present, so no maintained reader applies
    to this owner. Source-qualified correspondence is supported, but unresolved stereochemistry,
    unavailable full QC/OAK coverage and absent fresh primary verification keep this
    review partial. No supported source-edit finding or action is established.
  assessment_id: support-2426-completion
  target_ids:
  - naturalproductmech:mibig-03f1e441c0
  evidence_ids:
  - support-2426-owner
  - support-2426-capture
  - support-2426-intake
  - support-2426-intake-acceptance
  - support-2426-intake-reading
  - support-2426-inventory-acceptance
  - support-2426-plan
  - support-2426-plan-acceptance
  - support-2426-source-reading
  - support-2426-source-notes
  - support-2426-molecular-reading
  - support-2426-diagnostic-acceptance
  - support-2426-diagnostic-execution
  - support-2426-diagnostic-stderr
  - support-2426-review-profile
  dimensions:
  - name: review_completion
    value: Complete current owner/history, accepted canonical intake, retained source
      scopes and both accepted saved molecular forms were read. No causal graph, pathway,
      declared component or molecular target is present, so no maintained reader applies
      to this owner. Source-qualified correspondence is supported, but unresolved
      stereochemistry, unavailable full QC/OAK coverage and absent fresh primary verification
      keep this review partial. No supported source-edit finding or action is established.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2426-owner
    - support-2426-capture
    - support-2426-intake
    - support-2426-intake-acceptance
    - support-2426-intake-reading
    - support-2426-inventory-acceptance
    - support-2426-plan
    - support-2426-plan-acceptance
    - support-2426-source-reading
    - support-2426-source-notes
    - support-2426-molecular-reading
    - support-2426-diagnostic-acceptance
    - support-2426-diagnostic-execution
    - support-2426-diagnostic-stderr
    - support-2426-review-profile
findings: []
actions: []
limitations:
- Retained local evidence only; primary literature, current taxonomy, natural identity
  and external cross-references were not freshly verified.
- Full QC and complete OAK authority coverage remain unavailable. Local checks do
  not replace those authorities.
- All five stored structures disclose incomplete tetrahedral stereochemistry. All
  full-graph-identity flags remain false; four global diagnostic warnings remain unassigned.
- Producer, occurrence, locus, model, citation, companion and assay scopes remain
  separate. No record edit or pharmacological mechanism is inferred.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support personally read five whole selected owners/history, 45 selected frames/13
  rows/183 fields, plus unselected Yossoside V with 9 frames/2 rows/32 fields. BGC
  other-source and Native cache/curation credit remain separate.
- 'All ten last-five stored forms were personally read: 658 atom rows and 720 bond
  rows with complete strings/stereo/rings/motifs/maps; no new parse.'
- ROOT operated the original canonical intake; native_checks operated the original
  molecular diagnostic under ROOT delegation. This half has 201 actual intake placements
  across 42 paths. No maintained reader applies to these five owners; the cohort’s
  2422 reader is separate.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-243
```
