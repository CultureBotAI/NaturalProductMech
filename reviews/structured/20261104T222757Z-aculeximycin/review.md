# Local evidence review: aculeximycin

- Review: 20261104T222757Z-aculeximycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T22:00:09.906237Z
- Finished UTC: 2026-11-04T22:27:57.996865Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Aculeximycin retains a partially specified glycosylated macrolide-like encoding and matching stored forms. The exact historical 43357→47990 merge and separate DSM 43870 producer taxon are preserved. A blank-AID row supplies no assay evidence; no source edit is supported.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2468; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-559e9d03ee | data/natural_products/unclassified/aculeximycin.yaml | generated | aculeximycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-559e9d03ee | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-559e9d03ee | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-559e9d03ee | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-559e9d03ee | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-559e9d03ee | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-559e9d03ee | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-559e9d03ee | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-559e9d03ee | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and exact source correspondence

identity: supported. Targets: naturalproductmech:mibig-559e9d03ee.

The minted identifier naturalproductmech:mibig-559e9d03ee, full key VJKZKLDZOAFAEE-QIESNYARSA-N, BGC0000002 version 5, literal NPA09222 and PubChem CID6449919 join retained source assertions. The exact ChEBI structure query is empty. Neither a full-key match nor a database cross-reference independently establishes natural identity.

### Stored forms and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-559e9d03ee.

Both forms parse as neutral C81H144N2O33, 116 atoms/122 bonds, with ten true comparisons and a complete supplied atom match. Both retain 23 specified and 21 unspecified tetrahedral centres and three E double bonds; ordering-dependent Cis/Trans descriptors are not a change of E geometry. A 28-membered macrocycle and six saturated C5O cycles are encoded. One C5O cycle is an aglycone pyran intersecting the macrocycle; the remaining attachments are compatible with glycosylation but do not identify six sugars, residue names or anomeric configurations. One macrocyclic ester and two primary amines are present. Source stereo_complete=false remains explicit; full-graph identity was not established.

### Producer and locus evidence grades

provenance: supported. Targets: naturalproductmech:mibig-559e9d03ee.

BGC0000002 version 5 is active/questionable with unknown completeness. Kutzneria albida DSM 43870 taxon 1449976 is SOURCE_ASSERTION; CP007155.1:7362971–7504512 is CLUSTER_UNSTATED. LOTUS used 43357, and physical merge row 59 maps it to species 47990. The current cache lacks 43357 and names 47990 Kutzneria viridogrisea with albida aliases; strain 1449976 separately names K. viridogrisea DSM 43870 with an albida alias. This retained route explains local names, not a fresh taxonomy or strain-production upgrade.

### Citation tier and history scope

evidence: supported. Targets: naturalproductmech:mibig-559e9d03ee.

PMID25301375 is an ENTRY-level MIBiG citation and DOI 10.1186/1471-2164-15-885 is the retained LOTUS attribution. Identifier duplication across sources does not establish independent studies. Two seed-history events and the historical merge preserve processing provenance; they are not new experimental verification.

### Occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-559e9d03ee.

The single LOTUS occurrence is routed through the exact retained 43357→47990 merge. PubChem physical row 8521 has CID6449919 but a blank AID and no assay data, not an active or inactive result. No owner bioactivity, molecular-target or mechanism root is declared. Other retained occurrence/assay/target frames are empty within their predicates.

### Versioned classification applicability

consistency: unknown. Targets: naturalproductmech:mibig-559e9d03ee.

NPClassifier’s family arrays are empty and is_glycoside=true. Several attached O-containing rings and O bridges are compatible with glycosylation, while one of six C5O candidates is an aglycone pyran. Bounded motif counts do not identify exact sugar residues or independently assign a biosynthetic family. Empty model arrays are not a source defect; the source PKS class and UNCLASSIFIED filing remain separately attributed.

### Review completion

completeness: unknown. Targets: naturalproductmech:mibig-559e9d03ee.

The complete current owner and all 2 history events, all nine selected source frames, 38 accepted canonical input placements and both original molecular forms were read. No mechanism root is declared, so no maintained-reader call applies. The review remains partial/pass_with_limitations: full QC/OAK, fresh primary papers, taxonomy and natural-state verification remain unavailable. No supported source/status/history edit, finding or action is proposed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2468-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/aculeximycin.yaml; Whole current plaintext including complete curation_history | supports | Complete owner and all 2 history events personally read; current exact bytes retained. |
| support-2468-capture | /private/tmp/npm-review-work/shared-next-batch247/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete raw captured owner, including exact root absence and history. No graph, pathway, external component or molecular-target root is declared. |
| support-2468-grounding-owner | /private/tmp/npm-review-work/shared-next-batch247/owner-capture-DATA-001.json; /records/7/owner_document/identifier; /records/7/owner_document/label; /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts; /records/7/owner_document/xrefs; /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes | supports | Retained minted identifier, full key, source structure, source concepts and grounding text. Any present cross-reference remains a retained assertion, not fresh external identity verification. |
| support-2468-origin-owner | /private/tmp/npm-review-work/shared-next-batch247/owner-capture-DATA-001.json; /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters; /records/7/owner_document/producer_taxon_groups | supports | Complete current producer/locus assertions, distinct grades, coordinates and methods where present; source and implemented-curation scopes remain separate. |
| support-2468-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch247/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete owner retains its occurrence assertions and absence of bioactivities, molecular_targets and mechanism roots. Locus-evidence methods do not supply a pharmacological assay. |
| support-2468-classification-owner | /private/tmp/npm-review-work/shared-next-batch247/owner-capture-DATA-001.json; /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification; /records/7/owner_document/bgc_class; /records/7/owner_document/biosynthesis_origin | supports | Versioned model output and pinned filing are retained separately from source BGC/compound-class assertions. |
| support-2468-direct-contexts | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-target-input-plan-001.json; /records/7/proposed_companion_paths; /records/7/direct_companion_predicates; /records/7/identity_comparison_paths; /records/7/additional_context_roles | context_only | Exact retained direct BGC companion paths and predicate metadata. Shared locus is context only and does not establish molecular identity, assay activity or transfer of evidence; identity-comparison paths are empty. |
| support-2468-intake | /private/tmp/npm-review-work/shared-next-batch247/intakes/2468-inspect-001.json; /targets; /source | supports | Actual canonical intake preserves the single target, input roles and future correction ownership. |
| support-2468-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch247/root-intake-acceptance-001.json; /status; /records; /source_plan; /verification | supports | ROOT accepts the ten original canonical intakes and this exact composed plan. |
| support-2468-intake-reading | /private/tmp/npm-review-work/shared-next-batch247-tentative/support-prep/support-current247-last-five-molecular-intake-reading-001.json; /reading; /records/2/target; /records/2/intake; /coverage | supports | Support personally read all five actual target/ownership documents and 195 input placements across 51 paths. |
| support-2468-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch247/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /verification | supports | ROOT accepts the original retained local inventory; extraction is not fresh primary verification. |
| support-2468-plan | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-target-input-plan-001.json; /records/7/proposed_input_paths; /records/7/proposed_input_count | supports | Actual input map agrees with this canonical intake. |
| support-2468-plan-execution | /private/tmp/npm-review-work/shared-next-batch247/bgc-source-plan-execution-001.json; /plan; /original_exit_code; /terminal_chunk; /original_tools | supports | Original composer exited zero once; ROOT intake acceptance supplies the exact plan authority. |
| support-2468-source-reading | /private/tmp/npm-review-work/shared-next-batch247-tentative/support-prep/support-current247-last-five-source-reading-001.json; /source_partition; /records; /whole_reading; /physical_join_verification; /limits | supports | Support personally read all 45 selected frames, 17 positive row placements and 212 fields, plus the separately counted three-field historical taxon-merge row. ROOT companion readings remain attributed, with no duplicate source-row credit. |
| support-2468-source-notes | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | context_only | Joint notes preserve disjoint BGC/ROOT/Support source credit and Native cache/curation interpretation. |
| support-2468-molecular-reading | /private/tmp/npm-review-work/shared-next-batch247-tentative/support-prep/support-current247-last-five-molecular-intake-reading-001.json; /reading; /coverage; /records/2; /representation_notes; /limits | supports | Support personally read all ten paired forms: 524 atom rows and 552 bond rows, every stereo/motif/map field and all 195 actual intake roles. Acidobactin B preserves false canonical comparisons and an empty direct map; no reparse. |
| support-2468-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/7; /cached_taxonomy/whole_stanzas/17 | context_only | Relevant complete cached taxon stanzas preserve names and synonyms. Cached names do not independently establish producing strains or fresh taxonomy. |
| support-2468-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch247-tentative/native-prep/native-current247-cached-taxonomy-reading-001.json; /scope; /complete_readings; /counts; /interpretation | context_only | Native complete cache/merge reading remains explicitly attributed; Support separately read the nine relevant selected stanzas. |
| support-2468-curation-scope | /private/tmp/npm-review-work/shared-next-batch247-tentative/native-prep/native-current247-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation | context_only | Native exact implemented scan found no applicable current predicates. Twenty genus-only Penicillium lexical matches do not establish strain, grade or structure corrections for these owners. |
| support-2468-chemistry | /private/tmp/npm-review-work/shared-next-batch247/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/literal_InChI_layers; /records/7/formula_comparison_scope; /records/7/comparisons; /records/7/atom_correspondence | supports | Ten true stored-form comparisons and a complete supplied chirality-aware match; full_graph_identity_established remains false. |
| support-2468-topology | /private/tmp/npm-review-work/shared-next-batch247/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/smiles; /records/7/inchi; /records/7/comparisons; /records/7/atom_correspondence | supports | Both forms parse as neutral C81H144N2O33, 116 atoms/122 bonds, with ten true comparisons and a complete supplied atom match. Both retain 23 specified and 21 unspecified tetrahedral centres and three E double bonds; ordering-dependent Cis/Trans descriptors are not a change of E geometry. A 28-membered macrocycle and six saturated C5O cycles are encoded. One C5O cycle is an aglycone pyran intersecting the macrocycle; the remaining attachments are compatible with glycosylation but do not identify six sugars, residue names or anomeric configurations. One macrocyclic ester and two primary amines are present. Source stereo_complete=false remains explicit; full-graph identity was not established. |
| support-2468-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch247/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/7; /global_warning_count; /interpretation_boundary | supports | ROOT accepts this original diagnostic outcome, preserving any false canonical comparisons and the six global undefined-stereo warnings without assigning them to individual records. |
| support-2468-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch247/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic command, source, exit zero and exact streams, with no retry or external request. |
| support-2468-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch247/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | supports | Six original undefined-stereo warning lines are retained globally. No warning is assigned to an individual owner. |
| support-2468-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2468-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2468-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2468-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2468-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame has 1 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2468-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Physical row 4: BGC0000002 version 5, aculeximycin; Kutzneria albida DSM 43870 SOURCE_ASSERTION, locus CLUSTER_UNSTATED; PMID:25301375 at ENTRY scope. All retained structure, coordinates, methods and source classes remain in the exact row. |
| support-2468-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 4 | context_only | All fields in these positive placements join the current physical retained table. |
| support-2468-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2468-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame has 1 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2468-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Physical row 9041: Kutzneria albida (NCBITaxon:43357), DOI:10.1186/1471-2164-15-885; occurrence, not demonstrated production or independent-study proof. |
| support-2468-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 9041 | context_only | All fields in these positive placements join the current physical retained table. |
| support-2468-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2468-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame has 1 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2468-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/npclassifier/matches/0 | supports | Physical row 2525: npclassifier.gnps2.org@2026-09-07: //, glycoside=true; model assertion only. |
| support-2468-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 2525 | context_only | All fields in these positive placements join the current physical retained table. |
| support-2468-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame has 1 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2468-source-pubchem_bioassay-0 | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/pubchem_bioassay/matches/0 | supports | Physical row 8521: CID6449919, blank AID and no assay data; no activity/inactivity or measurement. |
| support-2468-physical-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 8521 | context_only | All fields in these positive placements join the current physical retained table. |
| support-2468-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2468-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2468-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2468-taxon-merge | /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/forward_taxon_merge_matches | context_only | Exact retained historical merge row59 maps NCBITaxon:43357 to47990, separately from producer strain1449976. This is a local retained route, not a fresh taxonomy assertion. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-247/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-247/native-current247-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-247/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-247/native-current247-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-247/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-247/native-current247-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-247/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-247/native-current247-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-247/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-247/native-current247-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; primary papers, fresh taxonomy, sequence/construct identity and natural stereochemistry were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Full-graph identity was not established. All ten comparisons agree and the supplied atom match is complete; any unspecified stereochemistry and bounded motif scope remain explicit.
- Six undefined-stereo warnings are global and unassigned to individual records. Producer, occurrence, locus, citation, classifier and assay scopes remain distinct; no source/status/history edit is proposed.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support whole selected owners/history carry exact current bytes. Source credit is BGC 9 + ROOT 36 + Support 17 + Native 0 positive placements. ROOT owns all eight companion whole readings; no duplicate source-row credit.
- Support personally read all ten saved last-five forms: 524 atom rows/552 bond rows, complete fields and maps, plus 195 intake placements across 51 paths. Exact raw/source and cached-taxonomy roles remain distinct.
- Support operated canonical intakes; Native operated the diagnostic under ROOT delegation. Historical execution observer labels do not change operator attribution. No selected last-five owner has an applicable maintained-reader route.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T222757Z-aculeximycin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: aculeximycin'
started_at: '2026-11-04T22:00:09.906237Z'
finished_at: '2026-11-04T22:27:57.996865Z'
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
summary: Aculeximycin retains a partially specified glycosylated macrolide-like encoding
  and matching stored forms. The exact historical 43357→47990 merge and separate DSM
  43870 producer taxon are preserved. A blank-AID row supplies no assay evidence;
  no source edit is supported.
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
  - path: data/natural_products/unclassified/aculeximycin.yaml
    sha256: 2eb2c66b4a000c95217d6e89f7d76f7b17d3778e88f2c0f72a7b5eecea6fe8e6
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
  selection: Campaign path order 2468; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-559e9d03ee
targets:
- target_id: naturalproductmech:mibig-559e9d03ee
  path: data/natural_products/unclassified/aculeximycin.yaml
  label: aculeximycin
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
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_merged.tsv
    role: Exact retained selected/direct taxon decision; no fresh authority.
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
  - naturalproductmech:mibig-559e9d03ee
  command: just validate-strict data/natural_products/unclassified/acetylaszonalenin.yaml
    data/natural_products/unclassified/acidobactamide-a.yaml data/natural_products/unclassified/acidobactamide-b.yaml
    data/natural_products/unclassified/acidobactamide-c.yaml data/natural_products/unclassified/acidobactin-a.yaml
    data/natural_products/unclassified/acidobactin-b.yaml data/natural_products/unclassified/acu-dioxomorpholine-b.yaml
    data/natural_products/unclassified/aculeximycin.yaml data/natural_products/unclassified/adametizine-a.yaml
    data/natural_products/unclassified/af-toxin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-247/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-559e9d03ee
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-247/validate-all-001.tsv
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
  - naturalproductmech:mibig-559e9d03ee
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
  - naturalproductmech:mibig-559e9d03ee
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
  - naturalproductmech:mibig-559e9d03ee
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-247/review-queue-001.tsv
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
  - naturalproductmech:mibig-559e9d03ee
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-559e9d03ee
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-559e9d03ee
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2468-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/aculeximycin.yaml
  locator: Whole current plaintext including complete curation_history
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Complete owner and all 2 history events personally read; current exact
    bytes retained.
  snapshot_sha256: 2eb2c66b4a000c95217d6e89f7d76f7b17d3778e88f2c0f72a7b5eecea6fe8e6
- evidence_id: support-2468-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch247/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Complete raw captured owner, including exact root absence and history.
    No graph, pathway, external component or molecular-target root is declared.
  snapshot_sha256: a95e97ba1076f0b4b4ea916b4cd1cffd0865938cc479cc55105609f63e8396fe
- evidence_id: support-2468-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch247/owner-capture-DATA-001.json
  locator: /records/7/owner_document/identifier; /records/7/owner_document/label;
    /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts;
    /records/7/owner_document/xrefs; /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Retained minted identifier, full key, source structure, source concepts
    and grounding text. Any present cross-reference remains a retained assertion,
    not fresh external identity verification.
  snapshot_sha256: a95e97ba1076f0b4b4ea916b4cd1cffd0865938cc479cc55105609f63e8396fe
- evidence_id: support-2468-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch247/owner-capture-DATA-001.json
  locator: /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters;
    /records/7/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Complete current producer/locus assertions, distinct grades, coordinates
    and methods where present; source and implemented-curation scopes remain separate.
  snapshot_sha256: a95e97ba1076f0b4b4ea916b4cd1cffd0865938cc479cc55105609f63e8396fe
- evidence_id: support-2468-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch247/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Complete owner retains its occurrence assertions and absence of bioactivities,
    molecular_targets and mechanism roots. Locus-evidence methods do not supply a
    pharmacological assay.
  snapshot_sha256: a95e97ba1076f0b4b4ea916b4cd1cffd0865938cc479cc55105609f63e8396fe
- evidence_id: support-2468-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch247/owner-capture-DATA-001.json
  locator: /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification;
    /records/7/owner_document/bgc_class; /records/7/owner_document/biosynthesis_origin
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Versioned model output and pinned filing are retained separately from source
    BGC/compound-class assertions.
  snapshot_sha256: a95e97ba1076f0b4b4ea916b4cd1cffd0865938cc479cc55105609f63e8396fe
- evidence_id: support-2468-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-target-input-plan-001.json
  locator: /records/7/proposed_companion_paths; /records/7/direct_companion_predicates;
    /records/7/identity_comparison_paths; /records/7/additional_context_roles
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: Exact retained direct BGC companion paths and predicate metadata. Shared
    locus is context only and does not establish molecular identity, assay activity
    or transfer of evidence; identity-comparison paths are empty.
  snapshot_sha256: c55927698c26e05614741c99f4f5135fd28151a8d2a493fbfbea874d6de4b761
- evidence_id: support-2468-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247/intakes/2468-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Actual canonical intake preserves the single target, input roles and future
    correction ownership.
  snapshot_sha256: b6391d1264ab14456de780b74ae06add0f23b5df2daec5984cc0321ce19389b4
- evidence_id: support-2468-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247/root-intake-acceptance-001.json
  locator: /status; /records; /source_plan; /verification
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: ROOT accepts the ten original canonical intakes and this exact composed
    plan.
  snapshot_sha256: c611b766ef67bb5bd914fc96c6641af38354e93c9dfff44f754edbd5bd5d1f34
- evidence_id: support-2468-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/support-prep/support-current247-last-five-molecular-intake-reading-001.json
  locator: /reading; /records/2/target; /records/2/intake; /coverage
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Support personally read all five actual target/ownership documents and
    195 input placements across 51 paths.
  snapshot_sha256: 865bfad92d3ef8aebc709aac50c171b54977dc541737b8606c878c85e2945198
- evidence_id: support-2468-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /verification
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: ROOT accepts the original retained local inventory; extraction is not fresh
    primary verification.
  snapshot_sha256: 244acce21c71843ae43bef1e86fff233db615710e8b1f26d82d110a4c5c66fc0
- evidence_id: support-2468-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-target-input-plan-001.json
  locator: /records/7/proposed_input_paths; /records/7/proposed_input_count
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Actual input map agrees with this canonical intake.
  snapshot_sha256: c55927698c26e05614741c99f4f5135fd28151a8d2a493fbfbea874d6de4b761
- evidence_id: support-2468-plan-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247/bgc-source-plan-execution-001.json
  locator: /plan; /original_exit_code; /terminal_chunk; /original_tools
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Original composer exited zero once; ROOT intake acceptance supplies the
    exact plan authority.
  snapshot_sha256: fa0b2a91bc1d1d276af27b613f5a59312e6069e441e6a5c11805cafd985e27b9
- evidence_id: support-2468-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/support-prep/support-current247-last-five-source-reading-001.json
  locator: /source_partition; /records; /whole_reading; /physical_join_verification;
    /limits
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Support personally read all 45 selected frames, 17 positive row placements
    and 212 fields, plus the separately counted three-field historical taxon-merge
    row. ROOT companion readings remain attributed, with no duplicate source-row credit.
  snapshot_sha256: ac9013982f1ed4d29830093b4a52e93fd6aae74ecd47fa53a6174fa6c10538f2
- evidence_id: support-2468-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: Joint notes preserve disjoint BGC/ROOT/Support source credit and Native
    cache/curation interpretation.
  snapshot_sha256: 148096fae026e2bb6e5dabdc8c76652bd45f1e9ac09c35117df95ed1b40cd048
- evidence_id: support-2468-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/support-prep/support-current247-last-five-molecular-intake-reading-001.json
  locator: /reading; /coverage; /records/2; /representation_notes; /limits
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: 'Support personally read all ten paired forms: 524 atom rows and 552 bond
    rows, every stereo/motif/map field and all 195 actual intake roles. Acidobactin
    B preserves false canonical comparisons and an empty direct map; no reparse.'
  snapshot_sha256: 865bfad92d3ef8aebc709aac50c171b54977dc541737b8606c878c85e2945198
- evidence_id: support-2468-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/7; /cached_taxonomy/whole_stanzas/17
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: Relevant complete cached taxon stanzas preserve names and synonyms. Cached
    names do not independently establish producing strains or fresh taxonomy.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
- evidence_id: support-2468-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/native-prep/native-current247-cached-taxonomy-reading-001.json
  locator: /scope; /complete_readings; /counts; /interpretation
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: Native complete cache/merge reading remains explicitly attributed; Support
    separately read the nine relevant selected stanzas.
  snapshot_sha256: 3c2939628c419c8da3fd320fc29f02b4657f439995633382a4658d75f817997e
- evidence_id: support-2468-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/native-prep/native-current247-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: Native exact implemented scan found no applicable current predicates. Twenty
    genus-only Penicillium lexical matches do not establish strain, grade or structure
    corrections for these owners.
  snapshot_sha256: 933ab99998702d95ba9cf32b87221d946b0797c3e664306ff815757440b97203
  search_scope: '{"whole_ignored_inclusive_scan": "/private/tmp/npm-review-work/shared-next-batch247-tentative/native-prep/native-current247-implemented-curation-scan-001.json",
    "selected_identifier": "naturalproductmech:mibig-559e9d03ee", "selected_full_key":
    "VJKZKLDZOAFAEE-QIESNYARSA-N", "scope": "Retained implemented tables and exact
    applicability, not universal evidence absence."}'
- evidence_id: support-2468-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/literal_InChI_layers; /records/7/formula_comparison_scope;
    /records/7/comparisons; /records/7/atom_correspondence
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Ten true stored-form comparisons and a complete supplied chirality-aware
    match; full_graph_identity_established remains false.
  snapshot_sha256: af66629efd2af695116b9fb1858d2499a3667ccbbcebeaf5887714b0824e7fc5
- evidence_id: support-2468-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/smiles; /records/7/inchi; /records/7/comparisons;
    /records/7/atom_correspondence
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Both forms parse as neutral C81H144N2O33, 116 atoms/122 bonds, with ten
    true comparisons and a complete supplied atom match. Both retain 23 specified
    and 21 unspecified tetrahedral centres and three E double bonds; ordering-dependent
    Cis/Trans descriptors are not a change of E geometry. A 28-membered macrocycle
    and six saturated C5O cycles are encoded. One C5O cycle is an aglycone pyran intersecting
    the macrocycle; the remaining attachments are compatible with glycosylation but
    do not identify six sugars, residue names or anomeric configurations. One macrocyclic
    ester and two primary amines are present. Source stereo_complete=false remains
    explicit; full-graph identity was not established.
  snapshot_sha256: af66629efd2af695116b9fb1858d2499a3667ccbbcebeaf5887714b0824e7fc5
- evidence_id: support-2468-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/7; /global_warning_count; /interpretation_boundary
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: ROOT accepts this original diagnostic outcome, preserving any false canonical
    comparisons and the six global undefined-stereo warnings without assigning them
    to individual records.
  snapshot_sha256: 6fae8d5d7bfa6a4222d37634324be2f867b84505537e3911c150bc9d317decee
- evidence_id: support-2468-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Original diagnostic command, source, exit zero and exact streams, with
    no retry or external request.
  snapshot_sha256: d57bc57926befa4a3d69c9bf622e3a5c7a44f3a978fdf68aa14d9d10fdd698ea
- evidence_id: support-2468-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch247/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Six original undefined-stereo warning lines are retained globally. No warning
    is assigned to an individual owner.
  snapshot_sha256: 771080f3c7bafefe7b2f079eb48b2799b903140a6fa4b8cd25f02acbfd85b368
- evidence_id: support-2468-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2468-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2468-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2468-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2468-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Saved mibig_compounds frame has 1 positive placements; any zero result
    is bounded to its exact retained predicate.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "VJKZKLDZOAFAEE-QIESNYARSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/mibig_compounds",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2468-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: 'Physical row 4: BGC0000002 version 5, aculeximycin; Kutzneria albida DSM
    43870 SOURCE_ASSERTION, locus CLUSTER_UNSTATED; PMID:25301375 at ENTRY scope.
    All retained structure, coordinates, methods and source classes remain in the
    exact row.'
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
- evidence_id: support-2468-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 4
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: All fields in these positive placements join the current physical retained
    table.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2468-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Saved chebi_structures frame has 0 positive placements; any zero result
    is bounded to its exact retained predicate.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "VJKZKLDZOAFAEE-QIESNYARSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/chebi_structures",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2468-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Saved lotus_occurrences frame has 1 positive placements; any zero result
    is bounded to its exact retained predicate.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "VJKZKLDZOAFAEE-QIESNYARSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2468-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: 'Physical row 9041: Kutzneria albida (NCBITaxon:43357), DOI:10.1186/1471-2164-15-885;
    occurrence, not demonstrated production or independent-study proof.'
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
- evidence_id: support-2468-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 9041
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: All fields in these positive placements join the current physical retained
    table.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2468-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame has 0 positive placements; any zero
    result is bounded to its exact retained predicate.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "VJKZKLDZOAFAEE-QIESNYARSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2468-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Saved npclassifier frame has 1 positive placements; any zero result is
    bounded to its exact retained predicate.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "VJKZKLDZOAFAEE-QIESNYARSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/npclassifier",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2468-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: 'Physical row 2525: npclassifier.gnps2.org@2026-09-07: //, glycoside=true;
    model assertion only.'
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
- evidence_id: support-2468-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 2525
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: All fields in these positive placements join the current physical retained
    table.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2468-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Saved pubchem_bioassay frame has 1 positive placements; any zero result
    is bounded to its exact retained predicate.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "VJKZKLDZOAFAEE-QIESNYARSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2468-source-pubchem_bioassay-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/pubchem_bioassay/matches/0
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: 'Physical row 8521: CID6449919, blank AID and no assay data; no activity/inactivity
    or measurement.'
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
- evidence_id: support-2468-physical-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 8521
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: All fields in these positive placements join the current physical retained
    table.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2468-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Saved bindingdb_targets frame has 0 positive placements; any zero result
    is bounded to its exact retained predicate.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "VJKZKLDZOAFAEE-QIESNYARSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2468-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame has 0 positive placements; any zero
    result is bounded to its exact retained predicate.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "VJKZKLDZOAFAEE-QIESNYARSA-N", "saved_frame": "/contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2468-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: supports
  summary: Saved chebi_origins frame has 0 positive placements; any zero result is
    bounded to its exact retained predicate.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/8/source_scope_inventory/joins/chebi_origins",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2468-taxon-merge
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch247-tentative/bgc-prep/bgc-conditional247-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/forward_taxon_merge_matches
  accessed_at: '2026-11-04T22:20:38.260401Z'
  support: context_only
  summary: Exact retained historical merge row59 maps NCBITaxon:43357 to47990, separately
    from producer strain1449976. This is a local retained route, not a fresh taxonomy
    assertion.
  snapshot_sha256: 4cf615082a0abb0ada7646d1cb2af2015dc5bf46fc0f5264976966c35e13c00c
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-247/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-247/native-current247-five-gates-execution-001.json
  accessed_at: '2026-11-04T22:06:05.707513Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 74e912a7e438842c4b13831059dd5cc6555a0e71c310b619fcbdc8c114bbd913
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-247/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-247/native-current247-five-gates-execution-001.json
  accessed_at: '2026-11-04T22:06:31.331269Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 12d39e1f971e29cdf35ab2f2dca9e5c236aec9f67b762f8ae4f73bf826b7f43b
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-247/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-247/native-current247-five-gates-execution-001.json
  accessed_at: '2026-11-04T22:06:51.630634Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-247/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-247/native-current247-five-gates-execution-001.json
  accessed_at: '2026-11-04T22:07:27.061264Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-247/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-247/native-current247-five-gates-execution-001.json
  accessed_at: '2026-11-04T22:07:39.326649Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 9cba3c133e53ad09f293ac21736d102b33a31b82ef423c17781c5a4473c39e73
assessments:
- area: identity
  topic: Retained identity and exact source correspondence
  outcome: supported
  summary: The minted identifier naturalproductmech:mibig-559e9d03ee, full key VJKZKLDZOAFAEE-QIESNYARSA-N,
    BGC0000002 version 5, literal NPA09222 and PubChem CID6449919 join retained source
    assertions. The exact ChEBI structure query is empty. Neither a full-key match
    nor a database cross-reference independently establishes natural identity.
  assessment_id: support-2468-identity
  target_ids:
  - naturalproductmech:mibig-559e9d03ee
  evidence_ids:
  - support-2468-grounding-owner
  - support-2468-chemistry
  - support-2468-direct-contexts
  - support-2468-query-chebi_structures
  - support-2468-source-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: VJKZKLDZOAFAEE-QIESNYARSA-N; retained full key, not independent natural
      identity.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2468-grounding-owner
    - support-2468-chemistry
    - support-2468-direct-contexts
    - support-2468-query-chebi_structures
    - support-2468-source-mibig_compounds-0
  - name: grounding_scope
    value: The minted identifier naturalproductmech:mibig-559e9d03ee, full key VJKZKLDZOAFAEE-QIESNYARSA-N,
      BGC0000002 version 5, literal NPA09222 and PubChem CID6449919 join retained
      source assertions. The exact ChEBI structure query is empty. Neither a full-key
      match nor a database cross-reference independently establishes natural identity.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2468-grounding-owner
    - support-2468-chemistry
    - support-2468-direct-contexts
    - support-2468-query-chebi_structures
    - support-2468-source-mibig_compounds-0
- area: representation
  topic: Stored forms and stereochemistry
  outcome: supported
  summary: Both forms parse as neutral C81H144N2O33, 116 atoms/122 bonds, with ten
    true comparisons and a complete supplied atom match. Both retain 23 specified
    and 21 unspecified tetrahedral centres and three E double bonds; ordering-dependent
    Cis/Trans descriptors are not a change of E geometry. A 28-membered macrocycle
    and six saturated C5O cycles are encoded. One C5O cycle is an aglycone pyran intersecting
    the macrocycle; the remaining attachments are compatible with glycosylation but
    do not identify six sugars, residue names or anomeric configurations. One macrocyclic
    ester and two primary amines are present. Source stereo_complete=false remains
    explicit; full-graph identity was not established.
  assessment_id: support-2468-representation
  target_ids:
  - naturalproductmech:mibig-559e9d03ee
  evidence_ids:
  - support-2468-grounding-owner
  - support-2468-chemistry
  - support-2468-topology
  - support-2468-molecular-reading
  - support-2468-diagnostic-acceptance
  - support-2468-structure-schema
  - support-2468-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both forms parse as neutral C81H144N2O33, 116 atoms/122 bonds, with ten
      true comparisons and a complete supplied atom match. Both retain 23 specified
      and 21 unspecified tetrahedral centres and three E double bonds; ordering-dependent
      Cis/Trans descriptors are not a change of E geometry. A 28-membered macrocycle
      and six saturated C5O cycles are encoded. One C5O cycle is an aglycone pyran
      intersecting the macrocycle; the remaining attachments are compatible with glycosylation
      but do not identify six sugars, residue names or anomeric configurations. One
      macrocyclic ester and two primary amines are present. Source stereo_complete=false
      remains explicit; full-graph identity was not established.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2468-grounding-owner
    - support-2468-chemistry
    - support-2468-topology
    - support-2468-molecular-reading
    - support-2468-diagnostic-acceptance
    - support-2468-structure-schema
    - support-2468-stereo-method
  - name: representation_correspondence
    value: Both forms parse as neutral C81H144N2O33, 116 atoms/122 bonds, with ten
      true comparisons and a complete supplied atom match. Both retain 23 specified
      and 21 unspecified tetrahedral centres and three E double bonds; ordering-dependent
      Cis/Trans descriptors are not a change of E geometry. A 28-membered macrocycle
      and six saturated C5O cycles are encoded. One C5O cycle is an aglycone pyran
      intersecting the macrocycle; the remaining attachments are compatible with glycosylation
      but do not identify six sugars, residue names or anomeric configurations. One
      macrocyclic ester and two primary amines are present. Source stereo_complete=false
      remains explicit; full-graph identity was not established.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2468-grounding-owner
    - support-2468-chemistry
    - support-2468-topology
    - support-2468-molecular-reading
    - support-2468-diagnostic-acceptance
    - support-2468-structure-schema
    - support-2468-stereo-method
- area: provenance
  topic: Producer and locus evidence grades
  outcome: supported
  summary: BGC0000002 version 5 is active/questionable with unknown completeness.
    Kutzneria albida DSM 43870 taxon 1449976 is SOURCE_ASSERTION; CP007155.1:7362971–7504512
    is CLUSTER_UNSTATED. LOTUS used 43357, and physical merge row 59 maps it to species
    47990. The current cache lacks 43357 and names 47990 Kutzneria viridogrisea with
    albida aliases; strain 1449976 separately names K. viridogrisea DSM 43870 with
    an albida alias. This retained route explains local names, not a fresh taxonomy
    or strain-production upgrade.
  assessment_id: support-2468-provenance
  target_ids:
  - naturalproductmech:mibig-559e9d03ee
  evidence_ids:
  - support-2468-origin-owner
  - support-2468-source-reading
  - support-2468-direct-contexts
  - support-2468-cached-taxonomy
  - support-2468-taxonomy-reading
  - support-2468-curation-scope
  - support-2468-source-mibig_compounds-0
  - support-2468-source-lotus_occurrences-0
  - support-2468-taxon-merge
  dimensions:
  - name: taxon_scope
    value: BGC0000002 version 5 is active/questionable with unknown completeness.
      Kutzneria albida DSM 43870 taxon 1449976 is SOURCE_ASSERTION; CP007155.1:7362971–7504512
      is CLUSTER_UNSTATED. LOTUS used 43357, and physical merge row 59 maps it to
      species 47990. The current cache lacks 43357 and names 47990 Kutzneria viridogrisea
      with albida aliases; strain 1449976 separately names K. viridogrisea DSM 43870
      with an albida alias. This retained route explains local names, not a fresh
      taxonomy or strain-production upgrade.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2468-origin-owner
    - support-2468-source-reading
    - support-2468-direct-contexts
    - support-2468-cached-taxonomy
    - support-2468-taxonomy-reading
    - support-2468-curation-scope
    - support-2468-source-mibig_compounds-0
    - support-2468-source-lotus_occurrences-0
    - support-2468-taxon-merge
  - name: producer_evidence
    value: BGC0000002 version 5 is active/questionable with unknown completeness.
      Kutzneria albida DSM 43870 taxon 1449976 is SOURCE_ASSERTION; CP007155.1:7362971–7504512
      is CLUSTER_UNSTATED. LOTUS used 43357, and physical merge row 59 maps it to
      species 47990. The current cache lacks 43357 and names 47990 Kutzneria viridogrisea
      with albida aliases; strain 1449976 separately names K. viridogrisea DSM 43870
      with an albida alias. This retained route explains local names, not a fresh
      taxonomy or strain-production upgrade.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2468-origin-owner
    - support-2468-source-reading
    - support-2468-direct-contexts
    - support-2468-cached-taxonomy
    - support-2468-taxonomy-reading
    - support-2468-curation-scope
    - support-2468-source-mibig_compounds-0
    - support-2468-source-lotus_occurrences-0
    - support-2468-taxon-merge
  - name: locus_evidence
    value: BGC0000002 version 5 is active/questionable with unknown completeness.
      Kutzneria albida DSM 43870 taxon 1449976 is SOURCE_ASSERTION; CP007155.1:7362971–7504512
      is CLUSTER_UNSTATED. LOTUS used 43357, and physical merge row 59 maps it to
      species 47990. The current cache lacks 43357 and names 47990 Kutzneria viridogrisea
      with albida aliases; strain 1449976 separately names K. viridogrisea DSM 43870
      with an albida alias. This retained route explains local names, not a fresh
      taxonomy or strain-production upgrade.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2468-origin-owner
    - support-2468-source-reading
    - support-2468-direct-contexts
    - support-2468-cached-taxonomy
    - support-2468-taxonomy-reading
    - support-2468-curation-scope
    - support-2468-source-mibig_compounds-0
    - support-2468-source-lotus_occurrences-0
    - support-2468-taxon-merge
- area: evidence
  topic: Citation tier and history scope
  outcome: supported
  summary: PMID25301375 is an ENTRY-level MIBiG citation and DOI 10.1186/1471-2164-15-885
    is the retained LOTUS attribution. Identifier duplication across sources does
    not establish independent studies. Two seed-history events and the historical
    merge preserve processing provenance; they are not new experimental verification.
  assessment_id: support-2468-citations
  target_ids:
  - naturalproductmech:mibig-559e9d03ee
  evidence_ids:
  - support-2468-owner
  - support-2468-origin-owner
  - support-2468-occurrence-activity-owner
  - support-2468-source-reading
  - support-2468-direct-contexts
  - support-2468-source-mibig_compounds-0
  - support-2468-source-lotus_occurrences-0
  - support-2468-source-npclassifier-0
  - support-2468-source-pubchem_bioassay-0
  - support-2468-taxon-merge
  dimensions:
  - name: citation_scope
    value: PMID25301375 is an ENTRY-level MIBiG citation and DOI 10.1186/1471-2164-15-885
      is the retained LOTUS attribution. Identifier duplication across sources does
      not establish independent studies. Two seed-history events and the historical
      merge preserve processing provenance; they are not new experimental verification.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2468-owner
    - support-2468-origin-owner
    - support-2468-occurrence-activity-owner
    - support-2468-source-reading
    - support-2468-direct-contexts
    - support-2468-source-mibig_compounds-0
    - support-2468-source-lotus_occurrences-0
    - support-2468-source-npclassifier-0
    - support-2468-source-pubchem_bioassay-0
    - support-2468-taxon-merge
- area: evidence
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: The single LOTUS occurrence is routed through the exact retained 43357→47990
    merge. PubChem physical row 8521 has CID6449919 but a blank AID and no assay data,
    not an active or inactive result. No owner bioactivity, molecular-target or mechanism
    root is declared. Other retained occurrence/assay/target frames are empty within
    their predicates.
  assessment_id: support-2468-occurrence
  target_ids:
  - naturalproductmech:mibig-559e9d03ee
  evidence_ids:
  - support-2468-occurrence-activity-owner
  - support-2468-direct-contexts
  - support-2468-cached-taxonomy
  - support-2468-curation-scope
  - support-2468-query-lotus_occurrences
  - support-2468-query-chebi_origins
  - support-2468-query-cyanometdb_occurrences
  - support-2468-query-pubchem_bioassay
  - support-2468-query-bindingdb_targets
  - support-2468-query-antibioticmech_inchikeys
  - support-2468-source-lotus_occurrences-0
  - support-2468-source-pubchem_bioassay-0
  - support-2468-taxon-merge
  - support-2468-source-reading
  dimensions:
  - name: occurrence_scope
    value: The single LOTUS occurrence is routed through the exact retained 43357→47990
      merge. PubChem physical row 8521 has CID6449919 but a blank AID and no assay
      data, not an active or inactive result. No owner bioactivity, molecular-target
      or mechanism root is declared. Other retained occurrence/assay/target frames
      are empty within their predicates.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2468-occurrence-activity-owner
    - support-2468-direct-contexts
    - support-2468-cached-taxonomy
    - support-2468-curation-scope
    - support-2468-query-lotus_occurrences
    - support-2468-query-chebi_origins
    - support-2468-query-cyanometdb_occurrences
    - support-2468-query-pubchem_bioassay
    - support-2468-query-bindingdb_targets
    - support-2468-query-antibioticmech_inchikeys
    - support-2468-source-lotus_occurrences-0
    - support-2468-source-pubchem_bioassay-0
    - support-2468-taxon-merge
    - support-2468-source-reading
  - name: assay_target_scope
    value: One blank-AID PubChem no-assay-data sentinel; no activity, inactivity,
      pharmacological target or curated mechanism is established.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2468-occurrence-activity-owner
    - support-2468-direct-contexts
    - support-2468-cached-taxonomy
    - support-2468-curation-scope
    - support-2468-query-lotus_occurrences
    - support-2468-query-chebi_origins
    - support-2468-query-cyanometdb_occurrences
    - support-2468-query-pubchem_bioassay
    - support-2468-query-bindingdb_targets
    - support-2468-query-antibioticmech_inchikeys
    - support-2468-source-lotus_occurrences-0
    - support-2468-source-pubchem_bioassay-0
    - support-2468-taxon-merge
    - support-2468-source-reading
- area: consistency
  topic: Versioned classification applicability
  outcome: unknown
  summary: NPClassifier’s family arrays are empty and is_glycoside=true. Several attached
    O-containing rings and O bridges are compatible with glycosylation, while one
    of six C5O candidates is an aglycone pyran. Bounded motif counts do not identify
    exact sugar residues or independently assign a biosynthetic family. Empty model
    arrays are not a source defect; the source PKS class and UNCLASSIFIED filing remain
    separately attributed.
  assessment_id: support-2468-classification
  target_ids:
  - naturalproductmech:mibig-559e9d03ee
  evidence_ids:
  - support-2468-classification-owner
  - support-2468-chemistry
  - support-2468-topology
  - support-2468-classification-seeder
  - support-2468-source-mibig_compounds-0
  - support-2468-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: NPClassifier’s family arrays are empty and is_glycoside=true. Several attached
      O-containing rings and O bridges are compatible with glycosylation, while one
      of six C5O candidates is an aglycone pyran. Bounded motif counts do not identify
      exact sugar residues or independently assign a biosynthetic family. Empty model
      arrays are not a source defect; the source PKS class and UNCLASSIFIED filing
      remain separately attributed.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2468-classification-owner
    - support-2468-chemistry
    - support-2468-topology
    - support-2468-classification-seeder
    - support-2468-source-mibig_compounds-0
    - support-2468-source-npclassifier-0
- area: completeness
  topic: Review completion
  outcome: unknown
  summary: 'The complete current owner and all 2 history events, all nine selected
    source frames, 38 accepted canonical input placements and both original molecular
    forms were read. No mechanism root is declared, so no maintained-reader call applies.
    The review remains partial/pass_with_limitations: full QC/OAK, fresh primary papers,
    taxonomy and natural-state verification remain unavailable. No supported source/status/history
    edit, finding or action is proposed.'
  assessment_id: support-2468-completion
  target_ids:
  - naturalproductmech:mibig-559e9d03ee
  evidence_ids:
  - support-2468-owner
  - support-2468-capture
  - support-2468-intake
  - support-2468-intake-acceptance
  - support-2468-intake-reading
  - support-2468-inventory-acceptance
  - support-2468-plan
  - support-2468-plan-execution
  - support-2468-source-reading
  - support-2468-source-notes
  - support-2468-molecular-reading
  - support-2468-diagnostic-acceptance
  - support-2468-diagnostic-execution
  - support-2468-diagnostic-stderr
  - support-2468-review-profile
  dimensions:
  - name: review_completion
    value: 'The complete current owner and all 2 history events, all nine selected
      source frames, 38 accepted canonical input placements and both original molecular
      forms were read. No mechanism root is declared, so no maintained-reader call
      applies. The review remains partial/pass_with_limitations: full QC/OAK, fresh
      primary papers, taxonomy and natural-state verification remain unavailable.
      No supported source/status/history edit, finding or action is proposed.'
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2468-owner
    - support-2468-capture
    - support-2468-intake
    - support-2468-intake-acceptance
    - support-2468-intake-reading
    - support-2468-inventory-acceptance
    - support-2468-plan
    - support-2468-plan-execution
    - support-2468-source-reading
    - support-2468-source-notes
    - support-2468-molecular-reading
    - support-2468-diagnostic-acceptance
    - support-2468-diagnostic-execution
    - support-2468-diagnostic-stderr
    - support-2468-review-profile
findings: []
actions: []
limitations:
- Retained local evidence only; primary papers, fresh taxonomy, sequence/construct
  identity and natural stereochemistry were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Full-graph identity was not established. All ten comparisons agree and the supplied
  atom match is complete; any unspecified stereochemistry and bounded motif scope
  remain explicit.
- Six undefined-stereo warnings are global and unassigned to individual records. Producer,
  occurrence, locus, citation, classifier and assay scopes remain distinct; no source/status/history
  edit is proposed.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support whole selected owners/history carry exact current bytes. Source credit is
  BGC 9 + ROOT 36 + Support 17 + Native 0 positive placements. ROOT owns all eight
  companion whole readings; no duplicate source-row credit.
- 'Support personally read all ten saved last-five forms: 524 atom rows/552 bond rows,
  complete fields and maps, plus 195 intake placements across 51 paths. Exact raw/source
  and cached-taxonomy roles remain distinct.'
- Support operated canonical intakes; Native operated the diagnostic under ROOT delegation.
  Historical execution observer labels do not change operator attribution. No selected
  last-five owner has an applicable maintained-reader route.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-247
```
