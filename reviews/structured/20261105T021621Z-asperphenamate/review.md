# Local evidence review: asperphenamate

- Review: 20261105T021621Z-asperphenamate
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T01:29:51.259452Z
- Finished UTC: 2026-11-05T02:16:21.865200Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Asperphenamate retains its formal ester/benzamide topology, two encoded S centres and separately scoped fungal/plant occurrences. Amide–imidic representation differences and unverified primary producer/locus evidence keep the review partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2496; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:145105 | data/natural_products/unclassified/asperphenamate.yaml | generated | asperphenamate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:145105 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:145105 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:145105 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:145105 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:145105 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:145105 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:145105 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:145105 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and source correspondence

identity: supported. Targets: CHEBI:145105.

CHEBI:145105 and full key CVULDJMCSSACEO-VMPREFPWSA-N are retained from the exact MIBiG/ChEBI mapping. The saved topology supports the ChEBI description of the formal ester of N-benzoyl-L-phenylalanine and N-benzoyl-L-phenylalaninol at encoded structural scope. This is not independent verification of natural identity, biosynthesis or the configuration of an isolated sample.

### Stored molecular forms and stereochemistry

representation: supported. Targets: CHEBI:145105.

Both stored forms parse as neutral C32H30N2O4 with 38 atoms and 41 bonds. Eight comparisons agree; both canonical SMILES comparisons are false and the direct atom map is empty. The SMILES-derived table contains four benzene rings, one ester and two benzamides. InChI reconstruction retains the ester but replaces both C(=O)N sites by C(O)=N; it adds two unspecified C=N stereo candidates. Each form independently retains two S tetrahedral assignments (SMILES atoms 7/12; InChI atoms 27/28). This supports a bounded amide/imidic representation interpretation. Equal Standard InChI/full key does not establish fixed-form graph identity or natural stereochemistry.

### Producer and locus evidence grades

provenance: supported. Targets: CHEBI:145105.

BGC0001517 version 3 names Aspergillus terreus NIH2624 (341663) at NT_165937.1:159865–184270. The retained methods field is empty, producer evidence is SOURCE_ASSERTION and the locus grade is CLUSTER_UNSTATED. Its DOI:10.1016/j.taap.2012.05.018 is attributed to COMPOUND_BIOACTIVITY; it does not itself establish characterized production or a demonstrated biosynthetic locus.

### Citation tier and history

evidence: supported. Targets: CHEBI:145105.

The MIBiG DOI:10.1016/j.taap.2012.05.018 is specifically a COMPOUND_BIOACTIVITY reference, while LOTUS and ChEBI origins retain their own occurrence citations and specimen comments. Citation presence does not establish a demonstrated NIH2624 locus, identify a producer for every plant isolation, or turn a retained source description into primary experimental verification. Both history events are seed_from_sources events; no curator-owned graph or current status/history edit was made.

### Occurrence and assay evidence scope

evidence: supported. Targets: CHEBI:145105.

All 13 LOTUS and five ChEBI origin rows are retained separately. They span fungal and plant occurrences; the ChEBI rows preserve A. flavipes ATCC11013 cell suspension culture, Ficus mucuso bark, P. brevicompactum, P. spathulatum B35 and Piptadenia gonoacantha branches/leaves. The general ChEBI endophytic-fungus interpretation does not assign a fungal producer to every plant record. Cached NIH2624 also lists FGSC A1156 as a synonym; source Penicillium megasporum maps to cached Pseudopenicillium megasporum at the same 69778 identifier. These retained names do not upgrade production evidence or provide fresh taxonomy. The complete selected owner has no bioactivities, molecular_targets, causal graphs, pathway or component roots. Exact retained activity/target queries are negative within their saved predicates; this does not establish inactivity or absence of a mechanism. No fresh paper, assay protocol or sequence/construct evidence was obtained.

### Versioned classification applicability

consistency: unknown. Targets: CHEBI:145105.

The versioned NPClassifier pathway, superclass and class arrays are empty; no named family is asserted by that model result. Its is_glycoside=false output is distinct from the stored MIBiG NRPS class and UNCLASSIFIED filing. The four phenyl rings, ester and two representation-dependent benzamides are compatible with the ChEBI formal-ester description, but neither that description nor motif detection experimentally establishes a biosynthetic route or family.

### Review completion

completeness: supported. Targets: CHEBI:145105.

The whole selected owner and both history events, nine saved source frames, all 37 accepted canonical input placements and both complete molecular tables were read. Direct companion raw/source readings, where applicable, remain context only. No supported source-edit finding was established at this retained-evidence scope. Fresh primary papers, natural identity/stereochemistry, complete QC and full OAK coverage remain unavailable; completion is partial and no source/status/history change was made.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2496-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/asperphenamate.yaml; Whole current plaintext including complete curation_history | supports | Complete current selected owner and both seed history events; no native record/status/history changes. |
| support-2496-capture | /private/tmp/npm-review-work/shared-next-batch250/owner-capture-DATA-001.json; /records/5/owner_document | supports | Complete captured owner and every present root. Absent mechanism, activity and target roots are retained as absence in this document. |
| support-2496-grounding-owner | /private/tmp/npm-review-work/shared-next-batch250/owner-capture-DATA-001.json; /records/5/owner_document/identifier; /records/5/owner_document/label; /records/5/owner_document/chemical_structure; /records/5/owner_document/definition; /records/5/owner_document/source_concepts; /records/5/owner_document/grounding_status | supports | Exact retained identifier, full key, source structure and present source/grounding fields; no fresh natural identity validation. |
| support-2496-origin-owner | /private/tmp/npm-review-work/shared-next-batch250/owner-capture-DATA-001.json; /records/5/owner_document/producer_organisms; /records/5/owner_document/biosynthetic_gene_clusters; /records/5/owner_document/producer_taxon_groups | supports | Complete producer and locus claims with separate evidence grades, methods, coordinates and source classes. |
| support-2496-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch250/owner-capture-DATA-001.json; /records/5/owner_document | supports | Complete owner preserves present occurrences and absent bioactivity, molecular-target and mechanism roots; absence is limited to this captured document. |
| support-2496-classification-owner | /private/tmp/npm-review-work/shared-next-batch250/owner-capture-DATA-001.json; /records/5/owner_document/np_pathway; /records/5/owner_document/np_classification; /records/5/owner_document/bgc_class; /records/5/owner_document/biosynthesis_origin | supports | Versioned model output, source BGC classes and UNCLASSIFIED filing remain separate assertions. |
| support-2496-direct-contexts | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-target-input-plan-001.json; /records/5/proposed_companion_paths; /records/5/direct_companion_predicates; /records/5/identity_comparison_paths; /records/5/additional_context_roles | context_only | Exact admitted direct-BGC context links and additional input roles; no extra selected-identity comparison roles. Companion facts do not become selected coverage. |
| support-2496-intake | /private/tmp/npm-review-work/shared-next-batch250/intakes/2496-inspect-001.json; /targets; /source | supports | Actual canonical target, source inputs and maintained ownership are retained. |
| support-2496-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch250/root-intake-acceptance-001.json; /status; /records/5; /source_plan; /verification | supports | ROOT accepts this original canonical intake and its exact source-plan/input joins. |
| support-2496-intake-reading | /private/tmp/npm-review-work/shared-next-batch250-tentative/support-prep/support-current250-last-five-molecular-intake-reading-001.json; /reading; /records/0/target; /records/0/intake; /coverage | supports | Support personally read all last-five canonical target/ownership documents and 188 current input placements across 44 paths. |
| support-2496-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch250/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /verification | supports | ROOT accepts the original retained local inventory; this is not primary-paper verification. |
| support-2496-plan | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-target-input-plan-001.json; /records/5/proposed_input_paths; /records/5/proposed_input_count | supports | The accepted input map agrees exactly with this canonical intake. |
| support-2496-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch250/root-target-input-plan-acceptance-002.json; /status; /accepted; /verification; /correction | supports | Preferred ROOT acceptance002 retains the unchanged actual plan and precise source-binding/output-verification attribution. |
| support-2496-source-reading | /private/tmp/npm-review-work/shared-next-batch250-tentative/support-prep/support-current250-assigned-source-reading-001.json; /contexts; /coverage; /whole_raw_history_carry; /personal_readings; /physical_join_verification; /cautions; /limits | supports | Support read eight assigned contexts: 72 frames, 47 rows and 447 fields. Selected last-five credit is 45 frames/36 rows/321 fields; three companions contribute 27/11/126 context-only. |
| support-2496-source-notes | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | context_only | Joint notes retain disjoint BGC36/ROOT8/Support47/Native0 source-row credits and exact bounded interpretations. |
| support-2496-molecular-reading | /private/tmp/npm-review-work/shared-next-batch250-tentative/support-prep/support-current250-last-five-molecular-intake-reading-001.json; /reading; /coverage; /records/0; /representation_notes; /limits | supports | Support read ten complete saved forms: 384 atom and 417 bond rows, all stereo/motif/map fields and 188 intake placements. No new molecular parse. |
| support-2496-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/7; /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/whole_stanzas/11; /cached_taxonomy/whole_stanzas/12; /cached_taxonomy/whole_stanzas/14; /cached_taxonomy/whole_stanzas/17; /cached_taxonomy/whole_stanzas/21; /cached_taxonomy/whole_stanzas/22; /cached_taxonomy/whole_stanzas/23; /cached_taxonomy/whole_stanzas/25; /cached_taxonomy/whole_stanzas/30; /cached_taxonomy/whole_stanzas/34; /cached_taxonomy/whole_stanzas/35; /cached_taxonomy/whole_stanzas/36 | context_only | Complete relevant retained cache stanzas preserve names and synonyms; these do not prove native production, strain identity or fresh taxonomy. |
| support-2496-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch250-tentative/native-prep/native-current250-cached-taxonomy-reading-001.json; /scope; /complete_readings; /counts; /interpretation; /source_taxon_routes | context_only | Native complete cache and route interpretation remains attributed. |
| support-2496-curation-scope | /private/tmp/npm-review-work/shared-next-batch250-tentative/native-prep/native-current250-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation; /assay_scope | context_only | The bounded implemented-table scan found no applicable exact replacement for these owners; unrelated lexical hits are not imported as owner evidence. |
| support-2496-chemistry | /private/tmp/npm-review-work/shared-next-batch250/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/literal_InChI_layers; /records/5/formula_comparison_scope; /records/5/comparisons; /records/5/atom_correspondence | supports | Eight true comparisons, two false canonical SMILES comparisons and an empty direct atom map; normalized identity is not fixed-form graph proof. |
| support-2496-topology | /private/tmp/npm-review-work/shared-next-batch250/chemistry-local/diagnostic-DATA-001.json; /records/5/smiles; /records/5/inchi | supports | Complete saved atom/bond/ring/stereo/motif tables retain representation-specific counts and stereochemical assignments; no new parse or natural-state claim. |
| support-2496-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch250/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /verification; /global_warning_count; /interpretation_boundary | supports | ROOT accepts the actual diagnostic evidence, preserving false comparisons and five global unassigned warnings. |
| support-2496-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch250/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Exact original diagnostic command/source, terminal exit and stream pins; no retry or external request. |
| support-2496-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch250/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | supports | Five retained warnings, including metal disconnection, remain global and unassigned to records. |
| support-2496-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2496-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2496-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2496-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2496-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2496-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Complete retained physical row 1826, all 25 fields: BGC0001517 version 3; Aspergillus terreus NIH2624, producer SOURCE_ASSERTION, locus CLUSTER_UNSTATED; DOI:10.1016/j.taap.2012.05.018 at COMPOUND_BIOACTIVITY scope. Source structure, methods and classes remain exact. |
| support-2496-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 1826 | context_only | Every complete retained field joins the exact current physical rows; primary source-reading credits remain disjoint. |
| support-2496-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2496-source-chebi_structures-0 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_structures/matches/0 | supports | Complete retained physical row 41278, all 6 fields: CHEBI:145105, asperphenamate; exact full key, source SMILES, definition and stars retained as database assertions. |
| support-2496-physical-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Physical TSV lines 41278 | context_only | Every complete retained field joins the exact current physical rows; primary source-reading credits remain disjoint. |
| support-2496-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame has 13 positive placements; a zero is bounded to its exact retained predicate. |
| support-2496-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Complete retained physical row 911, all 6 fields: Penicillium spathulatum (NCBITaxon:1263194), DOI:10.1055/S-0042-111393; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-1 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/1 | supports | Complete retained physical row 912, all 6 fields: Penicillium spathulatum (NCBITaxon:1263194), DOI:10.1055/S-0042-111394; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-2 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/2 | supports | Complete retained physical row 913, all 6 fields: Melastoma malabathricum (NCBITaxon:128733), DOI:10.1007/S11418-010-0431-8; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-3 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/3 | supports | Complete retained physical row 914, all 6 fields: Croton hieronymi (NCBITaxon:2896018), DOI:10.1016/S0031-9422(03)00202-4; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-4 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/4 | supports | Complete retained physical row 915, all 6 fields: Anaphalis subumbellata (NCBITaxon:3749087), DOI:10.1021/NP50025A017; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-5 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/5 | supports | Complete retained physical row 916, all 6 fields: Sapium rigidifolium (NCBITaxon:3877711), DOI:10.1016/0031-9422(93)85112-5; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-6 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/6 | supports | Complete retained physical row 917, all 6 fields: Aspergillus flavipes (NCBITaxon:41900), DOI:10.1016/0014-5793(68)80090-0; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-7 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/7 | supports | Complete retained physical row 918, all 6 fields: Leucas aspera (NCBITaxon:483811), DOI:10.1021/NP058118M; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-8 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/8 | supports | Complete retained physical row 919, all 6 fields: Penicillium brevicompactum (NCBITaxon:5074), DOI:10.1016/0031-9422(82)85217-5; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-9 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/9 | supports | Complete retained physical row 920, all 6 fields: Penicillium megasporum (NCBITaxon:69778), DOI:10.1016/0031-9422(89)80145-1; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-10 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/10 | supports | Complete retained physical row 921, all 6 fields: Artemisia anomala (NCBITaxon:714449), DOI:10.1016/S0031-9422(00)83589-X; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-11 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/11 | supports | Complete retained physical row 922, all 6 fields: Grangea maderaspatana (NCBITaxon:72940), DOI:10.1016/S0031-9422(99)00388-X; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-source-lotus_occurrences-12 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/12 | supports | Complete retained physical row 923, all 6 fields: Begonia nantoensis (NCBITaxon:78253), DOI:10.1002/CHIN.200434239; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2496-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923 | context_only | Every complete retained field joins the exact current physical rows; primary source-reading credits remain disjoint. |
| support-2496-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2496-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2496-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/npclassifier/matches/0 | supports | Complete retained physical row 350, all 7 fields: npclassifier.gnps2.org@2026-09-07: //; glycoside=false, model assertion only. |
| support-2496-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 350 | context_only | Every complete retained field joins the exact current physical rows; primary source-reading credits remain disjoint. |
| support-2496-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2496-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2496-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2496-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame has 5 positive placements; a zero is bounded to its exact retained predicate. |
| support-2496-source-chebi_origins-0 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins/matches/0 | supports | Complete retained physical row 16632, all 7 fields: CHEBI:145105, species Aspergillus flavipes, component cell suspension culture, strain ATCC 11013; all comments/source accessions retained without merging their scopes. |
| support-2496-source-chebi_origins-1 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins/matches/1 | supports | Complete retained physical row 16633, all 7 fields: CHEBI:145105, species Ficus mucuso, component bark, strain ; all comments/source accessions retained without merging their scopes. |
| support-2496-source-chebi_origins-2 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins/matches/2 | supports | Complete retained physical row 16634, all 7 fields: CHEBI:145105, species Penicillium brevicompactum, component , strain ; all comments/source accessions retained without merging their scopes. |
| support-2496-source-chebi_origins-3 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins/matches/3 | supports | Complete retained physical row 16635, all 7 fields: CHEBI:145105, species Penicillium spathulatum, component , strain B35; all comments/source accessions retained without merging their scopes. |
| support-2496-source-chebi_origins-4 | /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins/matches/4 | supports | Complete retained physical row 16636, all 7 fields: CHEBI:145105, species Piptadenia gonoacantha, component , strain ; all comments/source accessions retained without merging their scopes. |
| support-2496-physical-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Physical TSV lines 16632, 16633, 16634, 16635, 16636 | context_only | Every complete retained field joins the exact current physical rows; primary source-reading credits remain disjoint. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-250/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-250/native-current250-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-250/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-250/native-current250-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-250/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-250/native-current250-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-250/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-250/native-current250-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-250/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-250/native-current250-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; fresh papers, taxonomy, sequence/constructs, assay protocols and natural identity were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Both canonical SMILES comparisons are false and the direct atom map is empty. Full-graph identity was not established; motifs and tautomer/coordination representations remain explicit.
- Five diagnostic warnings remain global and unassigned. Source producer, occurrence, locus, model and citation scopes are separate; no source/status/history edit was made.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Whole selected raw/history and all complete paired molecular tables were personally read. Support source credit47/447/72 includes selected36/321/45 plus companion11/126/27; BGC36/322/36 and ROOT8/87/9 remain separately attributed. Native has zero positive source-row credit.
- Support read 188 last-five canonical input placements across 44 paths and 24 complete assigned selected/companion cache stanzas. Companion mechanism claims do not become selected coverage.
- Support operated canonical intakes; Native operated the original diagnostic under ROOT delegation. No last-five mechanism reader is applicable because all five owners lack mechanism roots. Evidence timestamps use literal UTC Z.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T021621Z-asperphenamate
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: asperphenamate'
started_at: '2026-11-05T01:29:51.259452Z'
finished_at: '2026-11-05T02:16:21.865200Z'
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
summary: Asperphenamate retains its formal ester/benzamide topology, two encoded S
  centres and separately scoped fungal/plant occurrences. Amide–imidic representation
  differences and unverified primary producer/locus evidence keep the review partial.
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
  - path: data/natural_products/unclassified/asperphenamate.yaml
    sha256: a4aad72b4073564aa416b4cee10694bdcd6f1bfc1e61675c12495fe2c8ddfb36
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
  selection: Campaign path order 2496; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:145105
targets:
- target_id: CHEBI:145105
  path: data/natural_products/unclassified/asperphenamate.yaml
  label: asperphenamate
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
    path: data/raw/chebi_origins.tsv
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
  - CHEBI:145105
  command: just validate-strict data/natural_products/unclassified/ascochlorin.yaml
    data/natural_products/unclassified/ascofuranone.yaml data/natural_products/unclassified/ashimide-a.yaml
    data/natural_products/unclassified/ashimide-b.yaml data/natural_products/unclassified/aspergillic-acid.yaml
    data/natural_products/unclassified/asperphenamate.yaml data/natural_products/unclassified/aspirochlorine.yaml
    data/natural_products/unclassified/astechrome.yaml data/natural_products/unclassified/asterrelenin.yaml
    data/natural_products/unclassified/atpenin-b.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-250/validate-strict-selected10-001.tsv
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
  - CHEBI:145105
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-250/validate-all-001.tsv
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
  - CHEBI:145105
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
  - CHEBI:145105
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
  - CHEBI:145105
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-250/review-queue-001.tsv
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
  - CHEBI:145105
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:145105
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:145105
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2496-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/asperphenamate.yaml
  locator: Whole current plaintext including complete curation_history
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Complete current selected owner and both seed history events; no native
    record/status/history changes.
  snapshot_sha256: a4aad72b4073564aa416b4cee10694bdcd6f1bfc1e61675c12495fe2c8ddfb36
- evidence_id: support-2496-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch250/owner-capture-DATA-001.json
  locator: /records/5/owner_document
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Complete captured owner and every present root. Absent mechanism, activity
    and target roots are retained as absence in this document.
  snapshot_sha256: 4d6daf8dbccad51d9a8cb3fb31ca09277886d82d36b47dcc3ee57e919ca49e78
- evidence_id: support-2496-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch250/owner-capture-DATA-001.json
  locator: /records/5/owner_document/identifier; /records/5/owner_document/label;
    /records/5/owner_document/chemical_structure; /records/5/owner_document/definition;
    /records/5/owner_document/source_concepts; /records/5/owner_document/grounding_status
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Exact retained identifier, full key, source structure and present source/grounding
    fields; no fresh natural identity validation.
  snapshot_sha256: 4d6daf8dbccad51d9a8cb3fb31ca09277886d82d36b47dcc3ee57e919ca49e78
- evidence_id: support-2496-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch250/owner-capture-DATA-001.json
  locator: /records/5/owner_document/producer_organisms; /records/5/owner_document/biosynthetic_gene_clusters;
    /records/5/owner_document/producer_taxon_groups
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Complete producer and locus claims with separate evidence grades, methods,
    coordinates and source classes.
  snapshot_sha256: 4d6daf8dbccad51d9a8cb3fb31ca09277886d82d36b47dcc3ee57e919ca49e78
- evidence_id: support-2496-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch250/owner-capture-DATA-001.json
  locator: /records/5/owner_document
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Complete owner preserves present occurrences and absent bioactivity, molecular-target
    and mechanism roots; absence is limited to this captured document.
  snapshot_sha256: 4d6daf8dbccad51d9a8cb3fb31ca09277886d82d36b47dcc3ee57e919ca49e78
- evidence_id: support-2496-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch250/owner-capture-DATA-001.json
  locator: /records/5/owner_document/np_pathway; /records/5/owner_document/np_classification;
    /records/5/owner_document/bgc_class; /records/5/owner_document/biosynthesis_origin
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Versioned model output, source BGC classes and UNCLASSIFIED filing remain
    separate assertions.
  snapshot_sha256: 4d6daf8dbccad51d9a8cb3fb31ca09277886d82d36b47dcc3ee57e919ca49e78
- evidence_id: support-2496-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-target-input-plan-001.json
  locator: /records/5/proposed_companion_paths; /records/5/direct_companion_predicates;
    /records/5/identity_comparison_paths; /records/5/additional_context_roles
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Exact admitted direct-BGC context links and additional input roles; no
    extra selected-identity comparison roles. Companion facts do not become selected
    coverage.
  snapshot_sha256: 0fb26cf4e67e2f96da97f0e5f97e71503c3d0cadc54316dcf58feff8ca1469a0
- evidence_id: support-2496-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250/intakes/2496-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Actual canonical target, source inputs and maintained ownership are retained.
  snapshot_sha256: 5abe21790a2990472037eeba62da36245e36db69d95b87e41b476c9d59999e43
- evidence_id: support-2496-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250/root-intake-acceptance-001.json
  locator: /status; /records/5; /source_plan; /verification
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: ROOT accepts this original canonical intake and its exact source-plan/input
    joins.
  snapshot_sha256: 8bdc0d6183e4f2cf160cb68056734ed04420920e5e05e24c44d8f80c0c233485
- evidence_id: support-2496-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/support-prep/support-current250-last-five-molecular-intake-reading-001.json
  locator: /reading; /records/0/target; /records/0/intake; /coverage
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Support personally read all last-five canonical target/ownership documents
    and 188 current input placements across 44 paths.
  snapshot_sha256: 2d5ecbdb72d01b5407de56a0051e79ec99f32186c83c70ebea9d2946b5b4d4bf
- evidence_id: support-2496-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /verification
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: ROOT accepts the original retained local inventory; this is not primary-paper
    verification.
  snapshot_sha256: 451802ad33325d43651a4d9bfddf27ce11944350457d192bc45a26b02ba6ac08
- evidence_id: support-2496-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-target-input-plan-001.json
  locator: /records/5/proposed_input_paths; /records/5/proposed_input_count
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: The accepted input map agrees exactly with this canonical intake.
  snapshot_sha256: 0fb26cf4e67e2f96da97f0e5f97e71503c3d0cadc54316dcf58feff8ca1469a0
- evidence_id: support-2496-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250/root-target-input-plan-acceptance-002.json
  locator: /status; /accepted; /verification; /correction
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Preferred ROOT acceptance002 retains the unchanged actual plan and precise
    source-binding/output-verification attribution.
  snapshot_sha256: c090bf00892303885d9bb8835aedf2dca270f1a738b5ff4d9c8dfd0232ae5e5e
- evidence_id: support-2496-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/support-prep/support-current250-assigned-source-reading-001.json
  locator: /contexts; /coverage; /whole_raw_history_carry; /personal_readings; /physical_join_verification;
    /cautions; /limits
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Support read eight assigned contexts: 72 frames, 47 rows and 447 fields.
    Selected last-five credit is 45 frames/36 rows/321 fields; three companions contribute
    27/11/126 context-only.'
  snapshot_sha256: 7909b88906addb16a860e71b4aea88022973bc229a49185a8c6ab02a87926742
- evidence_id: support-2496-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Joint notes retain disjoint BGC36/ROOT8/Support47/Native0 source-row credits
    and exact bounded interpretations.
  snapshot_sha256: 14d01b96efca99188f236e25dcf4466d0151b0cf5a04158f85faad07287768e1
- evidence_id: support-2496-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/support-prep/support-current250-last-five-molecular-intake-reading-001.json
  locator: /reading; /coverage; /records/0; /representation_notes; /limits
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Support read ten complete saved forms: 384 atom and 417 bond rows, all
    stereo/motif/map fields and 188 intake placements. No new molecular parse.'
  snapshot_sha256: 2d5ecbdb72d01b5407de56a0051e79ec99f32186c83c70ebea9d2946b5b4d4bf
- evidence_id: support-2496-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/7; /cached_taxonomy/whole_stanzas/9;
    /cached_taxonomy/whole_stanzas/11; /cached_taxonomy/whole_stanzas/12; /cached_taxonomy/whole_stanzas/14;
    /cached_taxonomy/whole_stanzas/17; /cached_taxonomy/whole_stanzas/21; /cached_taxonomy/whole_stanzas/22;
    /cached_taxonomy/whole_stanzas/23; /cached_taxonomy/whole_stanzas/25; /cached_taxonomy/whole_stanzas/30;
    /cached_taxonomy/whole_stanzas/34; /cached_taxonomy/whole_stanzas/35; /cached_taxonomy/whole_stanzas/36
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Complete relevant retained cache stanzas preserve names and synonyms; these
    do not prove native production, strain identity or fresh taxonomy.
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/native-prep/native-current250-cached-taxonomy-reading-001.json
  locator: /scope; /complete_readings; /counts; /interpretation; /source_taxon_routes
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Native complete cache and route interpretation remains attributed.
  snapshot_sha256: 36dabf3ca34552d0d30005d52f8262bfc7c122a545349af57ba70251505e67a8
- evidence_id: support-2496-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/native-prep/native-current250-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation; /assay_scope
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: The bounded implemented-table scan found no applicable exact replacement
    for these owners; unrelated lexical hits are not imported as owner evidence.
  snapshot_sha256: 58dd78da516fa3ff0eae7142bd4dfcd62b44680b472473a54e12f90e3f677ab1
  search_scope: '{"selected_identifier": "CHEBI:145105", "full_key": "CVULDJMCSSACEO-VMPREFPWSA-N",
    "scope": "Eleven implemented retained tables and exact predicates, including ignored-file-independent
    table inspection; not universal absence."}'
- evidence_id: support-2496-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/literal_InChI_layers; /records/5/formula_comparison_scope;
    /records/5/comparisons; /records/5/atom_correspondence
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Eight true comparisons, two false canonical SMILES comparisons and an empty
    direct atom map; normalized identity is not fixed-form graph proof.
  snapshot_sha256: 14745d9e87f420276668031a3dc74f56af348bb3ec45bcd606ab588dd09fce42
- evidence_id: support-2496-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/smiles; /records/5/inchi
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Complete saved atom/bond/ring/stereo/motif tables retain representation-specific
    counts and stereochemical assignments; no new parse or natural-state claim.
  snapshot_sha256: 14745d9e87f420276668031a3dc74f56af348bb3ec45bcd606ab588dd09fce42
- evidence_id: support-2496-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /verification; /global_warning_count; /interpretation_boundary
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: ROOT accepts the actual diagnostic evidence, preserving false comparisons
    and five global unassigned warnings.
  snapshot_sha256: 2959ab7c34a972c06459ab0123bceda1727a8acd74a69ad21cbef2bee780df15
- evidence_id: support-2496-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Exact original diagnostic command/source, terminal exit and stream pins;
    no retry or external request.
  snapshot_sha256: 8c63231a1c8d9448344e82c2eef01d2d70e122bb8d2822ecf404eb9c0465b9e5
- evidence_id: support-2496-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch250/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Five retained warnings, including metal disconnection, remain global and
    unassigned to records.
  snapshot_sha256: 74afd66a7b94861bc54ee7ecba27f530218e5686fb357e6eef4fe4c572845b20
- evidence_id: support-2496-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2496-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2496-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2496-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2496-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Saved mibig_compounds frame has 1 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "CVULDJMCSSACEO-VMPREFPWSA-N", "saved_frame": "/contexts/6/source_scope_inventory/joins/mibig_compounds",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2496-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 1826, all 25 fields: BGC0001517 version
    3; Aspergillus terreus NIH2624, producer SOURCE_ASSERTION, locus CLUSTER_UNSTATED;
    DOI:10.1016/j.taap.2012.05.018 at COMPOUND_BIOACTIVITY scope. Source structure,
    methods and classes remain exact.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 1826
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; primary
    source-reading credits remain disjoint.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2496-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Saved chebi_structures frame has 1 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "CVULDJMCSSACEO-VMPREFPWSA-N", "saved_frame": "/contexts/6/source_scope_inventory/joins/chebi_structures",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2496-source-chebi_structures-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_structures/matches/0
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 41278, all 6 fields: CHEBI:145105, asperphenamate;
    exact full key, source SMILES, definition and stars retained as database assertions.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-physical-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Physical TSV lines 41278
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; primary
    source-reading credits remain disjoint.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: support-2496-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Saved lotus_occurrences frame has 13 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "CVULDJMCSSACEO-VMPREFPWSA-N", "saved_frame": "/contexts/6/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2496-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 911, all 6 fields: Penicillium spathulatum
    (NCBITaxon:1263194), DOI:10.1055/S-0042-111393; occurrence is distinct from demonstrated
    production and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/1
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 912, all 6 fields: Penicillium spathulatum
    (NCBITaxon:1263194), DOI:10.1055/S-0042-111394; occurrence is distinct from demonstrated
    production and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-2
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/2
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 913, all 6 fields: Melastoma malabathricum
    (NCBITaxon:128733), DOI:10.1007/S11418-010-0431-8; occurrence is distinct from
    demonstrated production and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-3
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/3
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 914, all 6 fields: Croton hieronymi (NCBITaxon:2896018),
    DOI:10.1016/S0031-9422(03)00202-4; occurrence is distinct from demonstrated production
    and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-4
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/4
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 915, all 6 fields: Anaphalis subumbellata
    (NCBITaxon:3749087), DOI:10.1021/NP50025A017; occurrence is distinct from demonstrated
    production and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-5
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/5
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 916, all 6 fields: Sapium rigidifolium
    (NCBITaxon:3877711), DOI:10.1016/0031-9422(93)85112-5; occurrence is distinct
    from demonstrated production and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-6
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/6
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 917, all 6 fields: Aspergillus flavipes
    (NCBITaxon:41900), DOI:10.1016/0014-5793(68)80090-0; occurrence is distinct from
    demonstrated production and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-7
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/7
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 918, all 6 fields: Leucas aspera (NCBITaxon:483811),
    DOI:10.1021/NP058118M; occurrence is distinct from demonstrated production and
    independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-8
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/8
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 919, all 6 fields: Penicillium brevicompactum
    (NCBITaxon:5074), DOI:10.1016/0031-9422(82)85217-5; occurrence is distinct from
    demonstrated production and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-9
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/9
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 920, all 6 fields: Penicillium megasporum
    (NCBITaxon:69778), DOI:10.1016/0031-9422(89)80145-1; occurrence is distinct from
    demonstrated production and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-10
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/10
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 921, all 6 fields: Artemisia anomala (NCBITaxon:714449),
    DOI:10.1016/S0031-9422(00)83589-X; occurrence is distinct from demonstrated production
    and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-11
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/11
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 922, all 6 fields: Grangea maderaspatana
    (NCBITaxon:72940), DOI:10.1016/S0031-9422(99)00388-X; occurrence is distinct from
    demonstrated production and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-lotus_occurrences-12
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/12
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 923, all 6 fields: Begonia nantoensis (NCBITaxon:78253),
    DOI:10.1002/CHIN.200434239; occurrence is distinct from demonstrated production
    and independent-study corroboration.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921,
    922, 923
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; primary
    source-reading credits remain disjoint.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2496-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame has 0 positive placements; a zero is
    bounded to its exact retained predicate.
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "CVULDJMCSSACEO-VMPREFPWSA-N", "saved_frame": "/contexts/6/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2496-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Saved npclassifier frame has 1 positive placements; a zero is bounded to
    its exact retained predicate.
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "CVULDJMCSSACEO-VMPREFPWSA-N", "saved_frame": "/contexts/6/source_scope_inventory/joins/npclassifier",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2496-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 350, all 7 fields: npclassifier.gnps2.org@2026-09-07:
    //; glycoside=false, model assertion only.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 350
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; primary
    source-reading credits remain disjoint.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2496-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Saved pubchem_bioassay frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "CVULDJMCSSACEO-VMPREFPWSA-N", "saved_frame": "/contexts/6/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2496-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Saved bindingdb_targets frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "CVULDJMCSSACEO-VMPREFPWSA-N", "saved_frame": "/contexts/6/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2496-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame has 0 positive placements; a zero
    is bounded to its exact retained predicate.
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "CVULDJMCSSACEO-VMPREFPWSA-N", "saved_frame": "/contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2496-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: Saved chebi_origins frame has 5 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": ["CHEBI:145105"], "saved_frame": "/contexts/6/source_scope_inventory/joins/chebi_origins",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2496-source-chebi_origins-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins/matches/0
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 16632, all 7 fields: CHEBI:145105, species
    Aspergillus flavipes, component cell suspension culture, strain ATCC 11013; all
    comments/source accessions retained without merging their scopes.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-chebi_origins-1
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins/matches/1
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 16633, all 7 fields: CHEBI:145105, species
    Ficus mucuso, component bark, strain ; all comments/source accessions retained
    without merging their scopes.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-chebi_origins-2
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins/matches/2
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 16634, all 7 fields: CHEBI:145105, species
    Penicillium brevicompactum, component , strain ; all comments/source accessions
    retained without merging their scopes.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-chebi_origins-3
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins/matches/3
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 16635, all 7 fields: CHEBI:145105, species
    Penicillium spathulatum, component , strain B35; all comments/source accessions
    retained without merging their scopes.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-source-chebi_origins-4
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch250-tentative/bgc-prep/bgc-conditional250-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins/matches/4
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: supports
  summary: 'Complete retained physical row 16636, all 7 fields: CHEBI:145105, species
    Piptadenia gonoacantha, component , strain ; all comments/source accessions retained
    without merging their scopes.'
  snapshot_sha256: e9669b4e3648e5fc3e04d36596992836d9ede8e75b776f945f6ba24bc60145d0
- evidence_id: support-2496-physical-chebi_origins
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Physical TSV lines 16632, 16633, 16634, 16635, 16636
  accessed_at: '2026-11-05T02:10:08.737913Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; primary
    source-reading credits remain disjoint.
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-250/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-250/native-current250-five-gates-execution-001.json
  accessed_at: '2026-11-05T01:39:04.348559Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 0afc6bea485a268ae91b522dc65e1897c97eab30efe94f3f57da5824f6640fee
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-250/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-250/native-current250-five-gates-execution-001.json
  accessed_at: '2026-11-05T01:39:28.380882Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 125768848976f8acdf9bc72a794155259c76d49d1a6b5eebc1ba80f0730bdab9
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-250/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-250/native-current250-five-gates-execution-001.json
  accessed_at: '2026-11-05T01:39:48.162924Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-250/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-250/native-current250-five-gates-execution-001.json
  accessed_at: '2026-11-05T01:40:22.000837Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-250/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-250/native-current250-five-gates-execution-001.json
  accessed_at: '2026-11-05T01:40:33.579925Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 4b34a7c9f7c5b1c02cd9294f6c2c775e69ec9821938268b17e85d885c1dc4db6
assessments:
- area: identity
  topic: Retained identity and source correspondence
  outcome: supported
  summary: CHEBI:145105 and full key CVULDJMCSSACEO-VMPREFPWSA-N are retained from
    the exact MIBiG/ChEBI mapping. The saved topology supports the ChEBI description
    of the formal ester of N-benzoyl-L-phenylalanine and N-benzoyl-L-phenylalaninol
    at encoded structural scope. This is not independent verification of natural identity,
    biosynthesis or the configuration of an isolated sample.
  assessment_id: support-2496-identity
  target_ids:
  - CHEBI:145105
  evidence_ids:
  - support-2496-grounding-owner
  - support-2496-chemistry
  - support-2496-topology
  - support-2496-direct-contexts
  - support-2496-source-reading
  - support-2496-query-chebi_structures
  - support-2496-source-mibig_compounds-0
  - support-2496-source-chebi_structures-0
  dimensions:
  - name: standard_inchi_key
    value: CVULDJMCSSACEO-VMPREFPWSA-N; retained full key, not independently established
      natural identity.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2496-grounding-owner
    - support-2496-chemistry
    - support-2496-topology
    - support-2496-direct-contexts
    - support-2496-source-reading
    - support-2496-query-chebi_structures
    - support-2496-source-mibig_compounds-0
    - support-2496-source-chebi_structures-0
  - name: grounding_scope
    value: CHEBI:145105 and full key CVULDJMCSSACEO-VMPREFPWSA-N are retained from
      the exact MIBiG/ChEBI mapping. The saved topology supports the ChEBI description
      of the formal ester of N-benzoyl-L-phenylalanine and N-benzoyl-L-phenylalaninol
      at encoded structural scope. This is not independent verification of natural
      identity, biosynthesis or the configuration of an isolated sample.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2496-grounding-owner
    - support-2496-chemistry
    - support-2496-topology
    - support-2496-direct-contexts
    - support-2496-source-reading
    - support-2496-query-chebi_structures
    - support-2496-source-mibig_compounds-0
    - support-2496-source-chebi_structures-0
- area: representation
  topic: Stored molecular forms and stereochemistry
  outcome: supported
  summary: Both stored forms parse as neutral C32H30N2O4 with 38 atoms and 41 bonds.
    Eight comparisons agree; both canonical SMILES comparisons are false and the direct
    atom map is empty. The SMILES-derived table contains four benzene rings, one ester
    and two benzamides. InChI reconstruction retains the ester but replaces both C(=O)N
    sites by C(O)=N; it adds two unspecified C=N stereo candidates. Each form independently
    retains two S tetrahedral assignments (SMILES atoms 7/12; InChI atoms 27/28).
    This supports a bounded amide/imidic representation interpretation. Equal Standard
    InChI/full key does not establish fixed-form graph identity or natural stereochemistry.
  assessment_id: support-2496-representation
  target_ids:
  - CHEBI:145105
  evidence_ids:
  - support-2496-grounding-owner
  - support-2496-chemistry
  - support-2496-topology
  - support-2496-molecular-reading
  - support-2496-diagnostic-acceptance
  - support-2496-structure-schema
  - support-2496-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both stored forms parse as neutral C32H30N2O4 with 38 atoms and 41 bonds.
      Eight comparisons agree; both canonical SMILES comparisons are false and the
      direct atom map is empty. The SMILES-derived table contains four benzene rings,
      one ester and two benzamides. InChI reconstruction retains the ester but replaces
      both C(=O)N sites by C(O)=N; it adds two unspecified C=N stereo candidates.
      Each form independently retains two S tetrahedral assignments (SMILES atoms
      7/12; InChI atoms 27/28). This supports a bounded amide/imidic representation
      interpretation. Equal Standard InChI/full key does not establish fixed-form
      graph identity or natural stereochemistry.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2496-grounding-owner
    - support-2496-chemistry
    - support-2496-topology
    - support-2496-molecular-reading
    - support-2496-diagnostic-acceptance
    - support-2496-structure-schema
    - support-2496-stereo-method
  - name: representation_correspondence
    value: Both stored forms parse as neutral C32H30N2O4 with 38 atoms and 41 bonds.
      Eight comparisons agree; both canonical SMILES comparisons are false and the
      direct atom map is empty. The SMILES-derived table contains four benzene rings,
      one ester and two benzamides. InChI reconstruction retains the ester but replaces
      both C(=O)N sites by C(O)=N; it adds two unspecified C=N stereo candidates.
      Each form independently retains two S tetrahedral assignments (SMILES atoms
      7/12; InChI atoms 27/28). This supports a bounded amide/imidic representation
      interpretation. Equal Standard InChI/full key does not establish fixed-form
      graph identity or natural stereochemistry.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2496-grounding-owner
    - support-2496-chemistry
    - support-2496-topology
    - support-2496-molecular-reading
    - support-2496-diagnostic-acceptance
    - support-2496-structure-schema
    - support-2496-stereo-method
- area: provenance
  topic: Producer and locus evidence grades
  outcome: supported
  summary: BGC0001517 version 3 names Aspergillus terreus NIH2624 (341663) at NT_165937.1:159865–184270.
    The retained methods field is empty, producer evidence is SOURCE_ASSERTION and
    the locus grade is CLUSTER_UNSTATED. Its DOI:10.1016/j.taap.2012.05.018 is attributed
    to COMPOUND_BIOACTIVITY; it does not itself establish characterized production
    or a demonstrated biosynthetic locus.
  assessment_id: support-2496-provenance
  target_ids:
  - CHEBI:145105
  evidence_ids:
  - support-2496-origin-owner
  - support-2496-source-reading
  - support-2496-direct-contexts
  - support-2496-cached-taxonomy
  - support-2496-taxonomy-reading
  - support-2496-curation-scope
  - support-2496-source-mibig_compounds-0
  - support-2496-source-lotus_occurrences-0
  - support-2496-source-lotus_occurrences-1
  - support-2496-source-lotus_occurrences-2
  - support-2496-source-lotus_occurrences-3
  - support-2496-source-lotus_occurrences-4
  - support-2496-source-lotus_occurrences-5
  - support-2496-source-lotus_occurrences-6
  - support-2496-source-lotus_occurrences-7
  - support-2496-source-lotus_occurrences-8
  - support-2496-source-lotus_occurrences-9
  - support-2496-source-lotus_occurrences-10
  - support-2496-source-lotus_occurrences-11
  - support-2496-source-lotus_occurrences-12
  dimensions:
  - name: taxon_scope
    value: BGC0001517 version 3 names Aspergillus terreus NIH2624 (341663) at NT_165937.1:159865–184270.
      The retained methods field is empty, producer evidence is SOURCE_ASSERTION and
      the locus grade is CLUSTER_UNSTATED. Its DOI:10.1016/j.taap.2012.05.018 is attributed
      to COMPOUND_BIOACTIVITY; it does not itself establish characterized production
      or a demonstrated biosynthetic locus.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2496-origin-owner
    - support-2496-source-reading
    - support-2496-direct-contexts
    - support-2496-cached-taxonomy
    - support-2496-taxonomy-reading
    - support-2496-curation-scope
    - support-2496-source-mibig_compounds-0
    - support-2496-source-lotus_occurrences-0
    - support-2496-source-lotus_occurrences-1
    - support-2496-source-lotus_occurrences-2
    - support-2496-source-lotus_occurrences-3
    - support-2496-source-lotus_occurrences-4
    - support-2496-source-lotus_occurrences-5
    - support-2496-source-lotus_occurrences-6
    - support-2496-source-lotus_occurrences-7
    - support-2496-source-lotus_occurrences-8
    - support-2496-source-lotus_occurrences-9
    - support-2496-source-lotus_occurrences-10
    - support-2496-source-lotus_occurrences-11
    - support-2496-source-lotus_occurrences-12
  - name: producer_evidence
    value: BGC0001517 version 3 names Aspergillus terreus NIH2624 (341663) at NT_165937.1:159865–184270.
      The retained methods field is empty, producer evidence is SOURCE_ASSERTION and
      the locus grade is CLUSTER_UNSTATED. Its DOI:10.1016/j.taap.2012.05.018 is attributed
      to COMPOUND_BIOACTIVITY; it does not itself establish characterized production
      or a demonstrated biosynthetic locus.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2496-origin-owner
    - support-2496-source-reading
    - support-2496-direct-contexts
    - support-2496-cached-taxonomy
    - support-2496-taxonomy-reading
    - support-2496-curation-scope
    - support-2496-source-mibig_compounds-0
    - support-2496-source-lotus_occurrences-0
    - support-2496-source-lotus_occurrences-1
    - support-2496-source-lotus_occurrences-2
    - support-2496-source-lotus_occurrences-3
    - support-2496-source-lotus_occurrences-4
    - support-2496-source-lotus_occurrences-5
    - support-2496-source-lotus_occurrences-6
    - support-2496-source-lotus_occurrences-7
    - support-2496-source-lotus_occurrences-8
    - support-2496-source-lotus_occurrences-9
    - support-2496-source-lotus_occurrences-10
    - support-2496-source-lotus_occurrences-11
    - support-2496-source-lotus_occurrences-12
  - name: locus_evidence
    value: BGC0001517 version 3 names Aspergillus terreus NIH2624 (341663) at NT_165937.1:159865–184270.
      The retained methods field is empty, producer evidence is SOURCE_ASSERTION and
      the locus grade is CLUSTER_UNSTATED. Its DOI:10.1016/j.taap.2012.05.018 is attributed
      to COMPOUND_BIOACTIVITY; it does not itself establish characterized production
      or a demonstrated biosynthetic locus.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2496-origin-owner
    - support-2496-source-reading
    - support-2496-direct-contexts
    - support-2496-cached-taxonomy
    - support-2496-taxonomy-reading
    - support-2496-curation-scope
    - support-2496-source-mibig_compounds-0
    - support-2496-source-lotus_occurrences-0
    - support-2496-source-lotus_occurrences-1
    - support-2496-source-lotus_occurrences-2
    - support-2496-source-lotus_occurrences-3
    - support-2496-source-lotus_occurrences-4
    - support-2496-source-lotus_occurrences-5
    - support-2496-source-lotus_occurrences-6
    - support-2496-source-lotus_occurrences-7
    - support-2496-source-lotus_occurrences-8
    - support-2496-source-lotus_occurrences-9
    - support-2496-source-lotus_occurrences-10
    - support-2496-source-lotus_occurrences-11
    - support-2496-source-lotus_occurrences-12
- area: evidence
  topic: Citation tier and history
  outcome: supported
  summary: The MIBiG DOI:10.1016/j.taap.2012.05.018 is specifically a COMPOUND_BIOACTIVITY
    reference, while LOTUS and ChEBI origins retain their own occurrence citations
    and specimen comments. Citation presence does not establish a demonstrated NIH2624
    locus, identify a producer for every plant isolation, or turn a retained source
    description into primary experimental verification. Both history events are seed_from_sources
    events; no curator-owned graph or current status/history edit was made.
  assessment_id: support-2496-citations
  target_ids:
  - CHEBI:145105
  evidence_ids:
  - support-2496-owner
  - support-2496-origin-owner
  - support-2496-occurrence-activity-owner
  - support-2496-source-reading
  - support-2496-direct-contexts
  - support-2496-source-mibig_compounds-0
  - support-2496-source-chebi_structures-0
  - support-2496-source-lotus_occurrences-0
  - support-2496-source-lotus_occurrences-1
  - support-2496-source-lotus_occurrences-2
  - support-2496-source-lotus_occurrences-3
  - support-2496-source-lotus_occurrences-4
  - support-2496-source-lotus_occurrences-5
  - support-2496-source-lotus_occurrences-6
  - support-2496-source-lotus_occurrences-7
  - support-2496-source-lotus_occurrences-8
  - support-2496-source-lotus_occurrences-9
  - support-2496-source-lotus_occurrences-10
  - support-2496-source-lotus_occurrences-11
  - support-2496-source-lotus_occurrences-12
  - support-2496-source-npclassifier-0
  - support-2496-source-chebi_origins-0
  - support-2496-source-chebi_origins-1
  - support-2496-source-chebi_origins-2
  - support-2496-source-chebi_origins-3
  - support-2496-source-chebi_origins-4
  dimensions:
  - name: citation_scope
    value: The MIBiG DOI:10.1016/j.taap.2012.05.018 is specifically a COMPOUND_BIOACTIVITY
      reference, while LOTUS and ChEBI origins retain their own occurrence citations
      and specimen comments. Citation presence does not establish a demonstrated NIH2624
      locus, identify a producer for every plant isolation, or turn a retained source
      description into primary experimental verification. Both history events are
      seed_from_sources events; no curator-owned graph or current status/history edit
      was made.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2496-owner
    - support-2496-origin-owner
    - support-2496-occurrence-activity-owner
    - support-2496-source-reading
    - support-2496-direct-contexts
    - support-2496-source-mibig_compounds-0
    - support-2496-source-chebi_structures-0
    - support-2496-source-lotus_occurrences-0
    - support-2496-source-lotus_occurrences-1
    - support-2496-source-lotus_occurrences-2
    - support-2496-source-lotus_occurrences-3
    - support-2496-source-lotus_occurrences-4
    - support-2496-source-lotus_occurrences-5
    - support-2496-source-lotus_occurrences-6
    - support-2496-source-lotus_occurrences-7
    - support-2496-source-lotus_occurrences-8
    - support-2496-source-lotus_occurrences-9
    - support-2496-source-lotus_occurrences-10
    - support-2496-source-lotus_occurrences-11
    - support-2496-source-lotus_occurrences-12
    - support-2496-source-npclassifier-0
    - support-2496-source-chebi_origins-0
    - support-2496-source-chebi_origins-1
    - support-2496-source-chebi_origins-2
    - support-2496-source-chebi_origins-3
    - support-2496-source-chebi_origins-4
- area: evidence
  topic: Occurrence and assay evidence scope
  outcome: supported
  summary: All 13 LOTUS and five ChEBI origin rows are retained separately. They span
    fungal and plant occurrences; the ChEBI rows preserve A. flavipes ATCC11013 cell
    suspension culture, Ficus mucuso bark, P. brevicompactum, P. spathulatum B35 and
    Piptadenia gonoacantha branches/leaves. The general ChEBI endophytic-fungus interpretation
    does not assign a fungal producer to every plant record. Cached NIH2624 also lists
    FGSC A1156 as a synonym; source Penicillium megasporum maps to cached Pseudopenicillium
    megasporum at the same 69778 identifier. These retained names do not upgrade production
    evidence or provide fresh taxonomy. The complete selected owner has no bioactivities,
    molecular_targets, causal graphs, pathway or component roots. Exact retained activity/target
    queries are negative within their saved predicates; this does not establish inactivity
    or absence of a mechanism. No fresh paper, assay protocol or sequence/construct
    evidence was obtained.
  assessment_id: support-2496-occurrence
  target_ids:
  - CHEBI:145105
  evidence_ids:
  - support-2496-occurrence-activity-owner
  - support-2496-direct-contexts
  - support-2496-cached-taxonomy
  - support-2496-taxonomy-reading
  - support-2496-curation-scope
  - support-2496-source-reading
  - support-2496-query-lotus_occurrences
  - support-2496-query-chebi_origins
  - support-2496-query-cyanometdb_occurrences
  - support-2496-query-pubchem_bioassay
  - support-2496-query-bindingdb_targets
  - support-2496-query-antibioticmech_inchikeys
  - support-2496-source-lotus_occurrences-0
  - support-2496-source-lotus_occurrences-1
  - support-2496-source-lotus_occurrences-2
  - support-2496-source-lotus_occurrences-3
  - support-2496-source-lotus_occurrences-4
  - support-2496-source-lotus_occurrences-5
  - support-2496-source-lotus_occurrences-6
  - support-2496-source-lotus_occurrences-7
  - support-2496-source-lotus_occurrences-8
  - support-2496-source-lotus_occurrences-9
  - support-2496-source-lotus_occurrences-10
  - support-2496-source-lotus_occurrences-11
  - support-2496-source-lotus_occurrences-12
  - support-2496-source-chebi_origins-0
  - support-2496-source-chebi_origins-1
  - support-2496-source-chebi_origins-2
  - support-2496-source-chebi_origins-3
  - support-2496-source-chebi_origins-4
  - support-2496-source-chebi_structures-0
  dimensions:
  - name: occurrence_scope
    value: All 13 LOTUS and five ChEBI origin rows are retained separately. They span
      fungal and plant occurrences; the ChEBI rows preserve A. flavipes ATCC11013
      cell suspension culture, Ficus mucuso bark, P. brevicompactum, P. spathulatum
      B35 and Piptadenia gonoacantha branches/leaves. The general ChEBI endophytic-fungus
      interpretation does not assign a fungal producer to every plant record. Cached
      NIH2624 also lists FGSC A1156 as a synonym; source Penicillium megasporum maps
      to cached Pseudopenicillium megasporum at the same 69778 identifier. These retained
      names do not upgrade production evidence or provide fresh taxonomy. The complete
      selected owner has no bioactivities, molecular_targets, causal graphs, pathway
      or component roots. Exact retained activity/target queries are negative within
      their saved predicates; this does not establish inactivity or absence of a mechanism.
      No fresh paper, assay protocol or sequence/construct evidence was obtained.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2496-occurrence-activity-owner
    - support-2496-direct-contexts
    - support-2496-cached-taxonomy
    - support-2496-taxonomy-reading
    - support-2496-curation-scope
    - support-2496-source-reading
    - support-2496-query-lotus_occurrences
    - support-2496-query-chebi_origins
    - support-2496-query-cyanometdb_occurrences
    - support-2496-query-pubchem_bioassay
    - support-2496-query-bindingdb_targets
    - support-2496-query-antibioticmech_inchikeys
    - support-2496-source-lotus_occurrences-0
    - support-2496-source-lotus_occurrences-1
    - support-2496-source-lotus_occurrences-2
    - support-2496-source-lotus_occurrences-3
    - support-2496-source-lotus_occurrences-4
    - support-2496-source-lotus_occurrences-5
    - support-2496-source-lotus_occurrences-6
    - support-2496-source-lotus_occurrences-7
    - support-2496-source-lotus_occurrences-8
    - support-2496-source-lotus_occurrences-9
    - support-2496-source-lotus_occurrences-10
    - support-2496-source-lotus_occurrences-11
    - support-2496-source-lotus_occurrences-12
    - support-2496-source-chebi_origins-0
    - support-2496-source-chebi_origins-1
    - support-2496-source-chebi_origins-2
    - support-2496-source-chebi_origins-3
    - support-2496-source-chebi_origins-4
    - support-2496-source-chebi_structures-0
  - name: assay_target_scope
    value: The complete selected owner has no bioactivities, molecular_targets, causal
      graphs, pathway or component roots. Exact retained activity/target queries are
      negative within their saved predicates; this does not establish inactivity or
      absence of a mechanism. No fresh paper, assay protocol or sequence/construct
      evidence was obtained.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2496-occurrence-activity-owner
    - support-2496-direct-contexts
    - support-2496-cached-taxonomy
    - support-2496-taxonomy-reading
    - support-2496-curation-scope
    - support-2496-source-reading
    - support-2496-query-lotus_occurrences
    - support-2496-query-chebi_origins
    - support-2496-query-cyanometdb_occurrences
    - support-2496-query-pubchem_bioassay
    - support-2496-query-bindingdb_targets
    - support-2496-query-antibioticmech_inchikeys
    - support-2496-source-lotus_occurrences-0
    - support-2496-source-lotus_occurrences-1
    - support-2496-source-lotus_occurrences-2
    - support-2496-source-lotus_occurrences-3
    - support-2496-source-lotus_occurrences-4
    - support-2496-source-lotus_occurrences-5
    - support-2496-source-lotus_occurrences-6
    - support-2496-source-lotus_occurrences-7
    - support-2496-source-lotus_occurrences-8
    - support-2496-source-lotus_occurrences-9
    - support-2496-source-lotus_occurrences-10
    - support-2496-source-lotus_occurrences-11
    - support-2496-source-lotus_occurrences-12
    - support-2496-source-chebi_origins-0
    - support-2496-source-chebi_origins-1
    - support-2496-source-chebi_origins-2
    - support-2496-source-chebi_origins-3
    - support-2496-source-chebi_origins-4
    - support-2496-source-chebi_structures-0
- area: consistency
  topic: Versioned classification applicability
  outcome: unknown
  summary: The versioned NPClassifier pathway, superclass and class arrays are empty;
    no named family is asserted by that model result. Its is_glycoside=false output
    is distinct from the stored MIBiG NRPS class and UNCLASSIFIED filing. The four
    phenyl rings, ester and two representation-dependent benzamides are compatible
    with the ChEBI formal-ester description, but neither that description nor motif
    detection experimentally establishes a biosynthetic route or family.
  assessment_id: support-2496-classification
  target_ids:
  - CHEBI:145105
  evidence_ids:
  - support-2496-classification-owner
  - support-2496-chemistry
  - support-2496-topology
  - support-2496-classification-seeder
  - support-2496-source-reading
  - support-2496-source-mibig_compounds-0
  - support-2496-source-npclassifier-0
  - support-2496-source-chebi_structures-0
  dimensions:
  - name: classification_applicability
    value: The versioned NPClassifier pathway, superclass and class arrays are empty;
      no named family is asserted by that model result. Its is_glycoside=false output
      is distinct from the stored MIBiG NRPS class and UNCLASSIFIED filing. The four
      phenyl rings, ester and two representation-dependent benzamides are compatible
      with the ChEBI formal-ester description, but neither that description nor motif
      detection experimentally establishes a biosynthetic route or family.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2496-classification-owner
    - support-2496-chemistry
    - support-2496-topology
    - support-2496-classification-seeder
    - support-2496-source-reading
    - support-2496-source-mibig_compounds-0
    - support-2496-source-npclassifier-0
    - support-2496-source-chebi_structures-0
- area: completeness
  topic: Review completion
  outcome: supported
  summary: The whole selected owner and both history events, nine saved source frames,
    all 37 accepted canonical input placements and both complete molecular tables
    were read. Direct companion raw/source readings, where applicable, remain context
    only. No supported source-edit finding was established at this retained-evidence
    scope. Fresh primary papers, natural identity/stereochemistry, complete QC and
    full OAK coverage remain unavailable; completion is partial and no source/status/history
    change was made.
  assessment_id: support-2496-completion
  target_ids:
  - CHEBI:145105
  evidence_ids:
  - support-2496-owner
  - support-2496-capture
  - support-2496-intake
  - support-2496-intake-acceptance
  - support-2496-intake-reading
  - support-2496-inventory-acceptance
  - support-2496-plan
  - support-2496-plan-acceptance
  - support-2496-source-reading
  - support-2496-source-notes
  - support-2496-molecular-reading
  - support-2496-diagnostic-acceptance
  - support-2496-diagnostic-execution
  - support-2496-diagnostic-stderr
  - support-2496-review-profile
  dimensions:
  - name: review_completion
    value: The whole selected owner and both history events, nine saved source frames,
      all 37 accepted canonical input placements and both complete molecular tables
      were read. Direct companion raw/source readings, where applicable, remain context
      only. No supported source-edit finding was established at this retained-evidence
      scope. Fresh primary papers, natural identity/stereochemistry, complete QC and
      full OAK coverage remain unavailable; completion is partial and no source/status/history
      change was made.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2496-owner
    - support-2496-capture
    - support-2496-intake
    - support-2496-intake-acceptance
    - support-2496-intake-reading
    - support-2496-inventory-acceptance
    - support-2496-plan
    - support-2496-plan-acceptance
    - support-2496-source-reading
    - support-2496-source-notes
    - support-2496-molecular-reading
    - support-2496-diagnostic-acceptance
    - support-2496-diagnostic-execution
    - support-2496-diagnostic-stderr
    - support-2496-review-profile
findings: []
actions: []
limitations:
- Retained local evidence only; fresh papers, taxonomy, sequence/constructs, assay
  protocols and natural identity were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Both canonical SMILES comparisons are false and the direct atom map is empty. Full-graph
  identity was not established; motifs and tautomer/coordination representations remain
  explicit.
- Five diagnostic warnings remain global and unassigned. Source producer, occurrence,
  locus, model and citation scopes are separate; no source/status/history edit was
  made.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Whole selected raw/history and all complete paired molecular tables were personally
  read. Support source credit47/447/72 includes selected36/321/45 plus companion11/126/27;
  BGC36/322/36 and ROOT8/87/9 remain separately attributed. Native has zero positive
  source-row credit.
- Support read 188 last-five canonical input placements across 44 paths and 24 complete
  assigned selected/companion cache stanzas. Companion mechanism claims do not become
  selected coverage.
- Support operated canonical intakes; Native operated the original diagnostic under
  ROOT delegation. No last-five mechanism reader is applicable because all five owners
  lack mechanism roots. Evidence timestamps use literal UTC Z.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-250
```
