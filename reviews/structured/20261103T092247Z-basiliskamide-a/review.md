# Local evidence review: Basiliskamide A

- Review: 20261103T092247Z-basiliskamide-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T08:49:42.187283Z
- Finished UTC: 2026-11-03T09:22:47.675679Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Basiliskamide A: qualified partial review retaining source evidence grades, exact representation boundaries and owner-local assay and computed-model limits.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2186; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-c9b993f6e0 | data/natural_products/shikimates_and_phenylpropanoids/basiliskamide-a.yaml | generated | Basiliskamide A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-c9b993f6e0 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-c9b993f6e0 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-c9b993f6e0 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-c9b993f6e0 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-c9b993f6e0 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-c9b993f6e0 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-c9b993f6e0 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-c9b993f6e0 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding scope

identity: supported. Targets: naturalproductmech:mibig-c9b993f6e0.

Basiliskamide A retains the exact MIBiG-derived full key QAHZDGAHECEVRM-HXKCHMFGSA-N and neutral C23H31NO4. The saved exact-key ChEBI frame is empty, supporting MINTED only within that retained source scope. Active BGC0000172 version 5 names this compound at index 1; questionable quality and unknown completeness are source metadata, not a scientific rejection. Basiliskamide B is a direct same-BGC context with a different connectivity key and ester position, despite the same formula and stereochemical-layer pattern. The two NPAtlas spellings are retained source xrefs, not freshly resolved identities.

### Paired molecular representations and stereochemical limits

representation: supported. Targets: naturalproductmech:mibig-c9b993f6e0.

Both stored forms parsed as neutral C23H31NO4, 28 atoms and 28 bonds. Standard InChI, full key, formula, charge and atom/bond counts agree, but both canonical SMILES comparisons are false and the chirality-aware atom map is empty. The saved SMILES has terminal amide C13(=O14)–N15H2; the InChI-derived form has C20(–O25H)=N23H. This is a bounded amide/imidic-acid representation difference, not proof of wrong molecular identity or independently established tautomer equivalence. Both forms retain four specified tetrahedral centers (SMILES 2R,4S,5R,7R) and three specified C=C bonds (SMILES bonds 9E,11Z,20E); only the InChI form adds unspecified C=N bond 23. Literal stereo_complete:true follows the maintained atom-centered rule and does not establish every geometric or natural stereochemical assignment. Original diagnostic stderr is empty.

### Producer, occurrence and locus evidence grades

provenance: supported. Targets: naturalproductmech:mibig-c9b993f6e0.

The retained MIBiG producer is Brevibacillus laterosporus PE36, NCBITaxon:1399144, graded SOURCE_ASSERTION; BGC0000172 is CLUSTER_UNSTATED with no locus experiment stated. AXBT01000013.1 coordinates 84598–132409 are retained locus provenance. The two LOTUS statements concern species-level Brevibacillus laterosporus, NCBITaxon:1465, and do not upgrade the PE36 producer or establish two independent production experiments. Cache labels are locally consistent at their stated species/strain levels.

### Citation placement and historical verification scope

evidence: supported. Targets: naturalproductmech:mibig-c9b993f6e0.

DOI:10.1021/ol048574m is explicitly the MIBiG COMPOUND_EVIDENCE citation. DOI:10.1021/NP0201321 and DOI:10.1371/JOURNAL.PONE.0090124 belong to the two LOTUS occurrence assertions. Citation presence and normalization do not establish publication independence or upgrade source producer/locus grades. No original article, live accession or protein sequence was inspected in this review.

### Occurrence, assay and companion boundaries

scope: supported. Targets: naturalproductmech:mibig-c9b993f6e0.

Two species-level LOTUS occurrence assertions remain distinct from the PE36 producer. No owner bioactivities, molecular targets, bioactivity summary or mechanism roots are present. Exact selected PubChem, BindingDB and AntibioticMech joins are empty: zero actual AIDs and zero blank-AID sentinels. The direct Basiliskamide B context contributes no transferred activity or stereochemistry. These finite negatives do not establish inactivity or literature-wide absence.

### Computed classification and full-table topology limits

other: supported. Targets: naturalproductmech:mibig-c9b993f6e0.

NPClassifier reports Shikimates and Phenylpropanoids / Phenylpropanoids (C6-C3) / Cinnamic acids and derivatives, is_glycoside=false. The saved SMILES has a cinnamoyl ester C18(=O19)–O17–C4, one benzene ring and the separately described terminal amide. No saturated C5O candidate sugar ring is present. The cinnamoyl substructure supports a bounded model-family interpretation; MIBiG PKS and the computational filing label remain different axes, not competing experimental pathway assignments.

### Partial scientific completion and maintained ownership

completeness: supported. Targets: naturalproductmech:mibig-c9b993f6e0.

All seven core areas and twelve dimensions were assessed against actual intake, whole raw/history, retained source rows/cache and both complete saved chemical forms. Five local gates passed; full QC/OAK and external verification remain unavailable. This owner has no selected mechanism roots/components and no maintained reader applies. The inspected source assertions and bounded local structure facts provide positive support; no concrete source-record contradiction requiring a curation finding was established. Native SEEDED status/history and all corpus/source bytes remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2186-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/basiliskamide-a.yaml; Complete raw owner, lines 1-101. | supports | Whole selected owner and 2 history events personally read; current exact bytes match retained inventory and capture. |
| support-2186-capture | /private/tmp/npm-review-work/shared-next-batch219/owner-capture-DATA-001.json; /records/5/owner_document; /records/5/owner_pin; /records/5/read_started_at; /records/5/read_finished_at | supports | Complete actual captured owner and original access clocks; component resolution is assessed separately where applicable. |
| support-2186-intake | /private/tmp/npm-review-work/shared-next-batch219/intakes/2186-inspect-001.json; /status; /source; /targets/0 | supports | Original inspection-only intake with 38 current inputs and explicit maintained ownership. |
| support-2186-source-plan | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-target-input-plan-001.json; /records/5; /source_placement_count; /unique_source_path_count | supports | Exact current selected raw/history/source frames and input map equal the retained inventory and actual intake; cohort 422 placements/94 paths. |
| support-2186-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch219/root-target-input-plan-acceptance-001.json; /status; /plan; /notes; /actual_intake_acceptance; /source_placements; /unique_source_paths | supports | ROOT accepts exact saved source-plan and intake equality; this is not a scientific verdict. |
| support-2186-history | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/complete_raw_history; /contexts/6/history_count | supports | All 2 owner history events preserved; historical verification annotations are not new verification. |
| support-2186-direct-contexts | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-target-input-plan-001.json; /records/5/proposed_companion_paths; /records/5/direct_companion_predicates; /records/5/declared_mechanism_roots_literal; /records/5/component_paths | supports | 1 admitted direct companions; selected mechanism applicability and component paths retained without transitive expansion. |
| support-2186-source-notes | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-scope-notes-001.json; /reading/review_support; /reading/bgc_science; /reading/components; /cautions; /curation | supports | Whole source-reading attribution and bounded 65-token/eight-table zero-hit curation scan. The11 complementary cache stanzas are my reading; shared 341663/41900 stanzas are BGC reading. No new external or corpus-wide absence assertion. |
| support-2186-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/mibig_compounds | supports | Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N"; 1 retained rows. Empty results have only this exact pinned scope. |
| support-2186-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 219-219; exact retained row /contexts/6/source_scope_inventory/joins/mibig_compounds/matches/0 in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; raw row SHA256 8a100b26350e45756e6b159ace33d12eebbfef330bdc98f2643eaba5beedc520. | supports | Retained row fields (structure strings remain in the exact cited row): {"mibig_accession":"BGC0000172","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"Basiliskamide A","compound_index":"1","standard_inchi_key":"QAHZDGAHECEVRM-HXKCHMFGSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA07306&#124;npatlas:NPA007306","taxon_id":"NCBITaxon:1399144","taxon_label":"Brevibacillus laterosporus PE36","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"AXBT01000013.1","locus_from":"84598","locus_to":"132409","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"DOI:10.1021/ol048574m","reference_basis":"COMPOUND_EVIDENCE"} |
| support-2186-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_structures | supports | Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N"; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences | supports | Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N"; 2 retained rows. Empty results have only this exact pinned scope. |
| support-2186-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 7158-7158; exact retained row /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/0 in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; raw row SHA256 178b04054a9ef3ae5ce638c443a5f25f94ed616f7269f1ba195c1293d719ad12. | supports | Retained row fields (structure strings remain in the exact cited row): {"standard_inchi_key":"QAHZDGAHECEVRM-HXKCHMFGSA-N","organism_name":"Brevibacillus laterosporus","taxon_id":"NCBITaxon:1465","organism_wikidata":"http://www.wikidata.org/entity/Q25840601","reference_doi":"10.1021/NP0201321","structure_wikidata":"http://www.wikidata.org/entity/Q59247254"} |
| support-2186-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 7159-7159; exact retained row /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/1 in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; raw row SHA256 bdcf2287ec5c9b66479c2f4666baa6f61a7e8be6782a541383ccacfa9c59c308. | supports | Retained row fields (structure strings remain in the exact cited row): {"standard_inchi_key":"QAHZDGAHECEVRM-HXKCHMFGSA-N","organism_name":"Brevibacillus laterosporus","taxon_id":"NCBITaxon:1465","organism_wikidata":"http://www.wikidata.org/entity/Q25840601","reference_doi":"10.1371/JOURNAL.PONE.0090124","structure_wikidata":"http://www.wikidata.org/entity/Q59247254"} |
| support-2186-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N"; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/npclassifier | supports | Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N"; 1 retained rows. Empty results have only this exact pinned scope. |
| support-2186-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 1957-1957; exact retained row /contexts/6/source_scope_inventory/joins/npclassifier/matches/0 in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; raw row SHA256 5fa558b263f873a2f9a201981369f3813c66ef4b57dd3facabd1bd4acbaec07e. | supports | Retained row fields (structure strings remain in the exact cited row): {"standard_inchi_key":"QAHZDGAHECEVRM-HXKCHMFGSA-N","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Phenylpropanoids (C6-C3)","class_results":"Cinnamic acids and derivatives","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"} |
| support-2186-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/pubchem_bioassay | supports | Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N"; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/bindingdb_targets | supports | Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N"; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N"; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins | supports | Saved predicate exact chebi_id from exact full-key structure rows; query []; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-companion-12 | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/12 | supports | Complete directly admitted companion Basiliskamide B, full keyHCZNVGHFFHRIFM-HXKCHMFGSA-N, 2 histories; no identity/activity/producer transfer. |
| support-2186-companion-12-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/mibig_compounds | supports | Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N"; 1 retained rows. Empty results have only this exact pinned scope. |
| support-2186-companion-12-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 220-220; exact retained row /contexts/12/source_scope_inventory/joins/mibig_compounds/matches/0 in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; raw row SHA256 c1997f4270b1a9362c9a9b37d7e80b04bbedb21395460e5ad3695efbb92e8436. | supports | Retained row fields (structure strings remain in the exact cited row): {"mibig_accession":"BGC0000172","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"Basiliskamide B","compound_index":"2","standard_inchi_key":"HCZNVGHFFHRIFM-HXKCHMFGSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA018193","taxon_id":"NCBITaxon:1399144","taxon_label":"Brevibacillus laterosporus PE36","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"AXBT01000013.1","locus_from":"84598","locus_to":"132409","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"DOI:10.1021/ol048574m","reference_basis":"COMPOUND_EVIDENCE"} |
| support-2186-companion-12-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/chebi_structures | supports | Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N"; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-companion-12-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/lotus_occurrences | supports | Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N"; 1 retained rows. Empty results have only this exact pinned scope. |
| support-2186-companion-12-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 2315-2315; exact retained row /contexts/12/source_scope_inventory/joins/lotus_occurrences/matches/0 in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; raw row SHA256 a4363d83aa4868fba687749766a6a14e5fa1b457caac6cea444a6366d72080b7. | supports | Retained row fields (structure strings remain in the exact cited row): {"standard_inchi_key":"HCZNVGHFFHRIFM-HXKCHMFGSA-N","organism_name":"Brevibacillus laterosporus","taxon_id":"NCBITaxon:1465","organism_wikidata":"http://www.wikidata.org/entity/Q25840601","reference_doi":"10.1021/NP0201321","structure_wikidata":"http://www.wikidata.org/entity/Q57751679"} |
| support-2186-companion-12-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N"; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-companion-12-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/npclassifier | supports | Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N"; 1 retained rows. Empty results have only this exact pinned scope. |
| support-2186-companion-12-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 791-791; exact retained row /contexts/12/source_scope_inventory/joins/npclassifier/matches/0 in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; raw row SHA256 2ddefbbd103abf8834574c3b5ccec11ec4919b1940a355c64c224c413131294d. | supports | Retained row fields (structure strings remain in the exact cited row): {"standard_inchi_key":"HCZNVGHFFHRIFM-HXKCHMFGSA-N","pathway_results":"Polyketides&#124;Shikimates and Phenylpropanoids","superclass_results":"Phenylpropanoids (C6-C3)&#124;Linear polyketides","class_results":"Cinnamic acids and derivatives&#124;Open-chain polyketides","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"} |
| support-2186-companion-12-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/pubchem_bioassay | supports | Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N"; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-companion-12-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/bindingdb_targets | supports | Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N"; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-companion-12-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N"; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-companion-12-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/chebi_origins | supports | Saved predicate exact chebi_id from exact full-key structure rows; query []; 0 retained rows. Empty results have only this exact pinned scope. |
| support-2186-taxon-routes | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/source_taxa; /contexts/6/source_scope_inventory/forward_taxon_merge_matches; /contexts/6/source_scope_inventory/nonorganism_matches; /cached_taxonomy/unmatched_ids | supports | Exact selected taxon routes: no forward-merge/nonorganism matches and no unmatched cached IDs. This is cached routing, not live taxonomy or proof of production. |
| support-2186-taxon-1399144 | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/27 | supports | Complete cached stanza NCBITaxon:1399144, physical corpus_taxa.obo lines 128366-128369. Whole stanza personally read. Cached labels/synonyms retain taxonomic scope, not experimentally established producer identity. |
| support-2186-taxon-1465 | /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/1 | supports | Complete cached stanza NCBITaxon:1465, physical corpus_taxa.obo lines 2207-2211. Whole stanza personally read. Cached labels/synonyms retain taxonomic scope, not experimentally established producer identity. |
| support-2186-chemistry | /private/tmp/npm-review-work/shared-next-batch219/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/smiles; /records/5/inchi; /records/5/comparisons; /records/5/atom_correspondence | supports | Both stored forms parsed as neutral C23H31NO4, 28 atoms and 28 bonds. Standard InChI, full key, formula, charge and atom/bond counts agree, but both canonical SMILES comparisons are false and the chirality-aware atom map is empty. The saved SMILES has terminal amide C13(=O14)–N15H2; the InChI-derived form has C20(–O25H)=N23H. This is a bounded amide/imidic-acid representation difference, not proof of wrong molecular identity or independently established tautomer equivalence. Both forms retain four specified tetrahedral centers (SMILES 2R,4S,5R,7R) and three specified C=C bonds (SMILES bonds 9E,11Z,20E); only the InChI form adds unspecified C=N bond 23. Literal stereo_complete:true does not establish every geometric or natural stereochemical assignment. |
| support-2186-stereo | /private/tmp/npm-review-work/shared-next-batch219/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/smiles/computed/potential_stereo; /records/5/smiles/computed/stereo_counts; /records/5/inchi/computed/potential_stereo; /records/5/inchi/computed/stereo_counts; /records/5/smiles/computed/atoms; /records/5/smiles/computed/bonds; /records/5/inchi/computed/atoms; /records/5/inchi/computed/bonds | supports | Four specified tetrahedral centers and three specified C=C bonds in both forms; extra unspecified C=N only in InChI-derived form; literal stereo_complete:true is atom-centered. |
| support-2186-topology | /private/tmp/npm-review-work/shared-next-batch219/chemistry-local/diagnostic-DATA-001.json; /records/5/smiles/computed; /records/5/inchi/computed; /records/5/atom_correspondence | supports | Saved SMILES: one benzene ring, ester C18(=O19)–O17–C4, terminal amide C13(=O14)–N15, no saturated C5O candidate sugar ring. InChI-derived terminal imidic-acid representation and empty map are preserved. |
| support-2186-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165-172. | supports | The maintained stereo_complete derivation asks FindMolChiralCenters for unassigned atom centers; it is not a universal geometric/axial/natural-stereo assertion. |
| support-2186-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch219/chemistry-local/diagnostic-execution-001.json; Complete original JSON execution receipt. | supports | Original single diagnostic execution receipt and its saved stdout/stderr; no repeat computation. |
| support-2186-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch219/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /original_terminal; /false_comparisons; /stderr_bytes; /limitations | supports | ROOT accepts the original 20-form local computation, with empty stderr and explicit canonical/identity limitations. |
| support-2186-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch219/root-intake-ready-001.json; /status; /intake_summary; /source_placements; /unique_source_paths; /per_order_counts; /mechanism_owner_orders | supports | ROOT accepts ten original intakes and exact 422/94 source map; no scientific verdict. |
| support-2186-native-acceptance | /private/tmp/npm-review-work/shared-next-batch219/root-native-checks-acceptance-001.json; /status; /ledger; /local_checks_passed; /queue_rows; /selected_queue_rows; /unavailable | supports | Five original local gates passed; queue 8922 total/13 selected rows. Full QC and OAK unavailable; local gate success is not scientific sign-off. |
| support-2186-source-ownership | /private/tmp/npm-review-work/shared-next-batch219/intakes/2186-inspect-001.json; /targets/0/owner_paths; /targets/0/ownership_note | supports | Generated inventory/seeder fields and, where present, curator-owned mechanism components retain distinct maintained owners. No source record or native status/history was edited. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-219/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-219/native-current219-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-219/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-219/native-current219-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-219/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-219/native-current219-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-219/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-219/native-current219-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-219/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-219/native-current219-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- No external requests or fresh primary-literature/API/ontology/taxonomy/accession verification. Source xrefs and historical citations remain assertions at their stated resolution.
- The empty atom map and canonical differences remain unresolved at full graph-identity level; normalized identifier equality does not independently prove tautomer equivalence.
- Full QC and complete OAK authority coverage were unavailable. Local validation and reproduction do not prove biological claims or justify native status promotion.
- No source record, generated owner, component or curation history was edited in this review.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Personal whole reading covers the selected owner/history, admitted direct companions, assigned full source payloads and both saved molecular tables; cache/components carry explicitly identified team attribution.
- Author previously prepared controller/diagnostic/assembler sources; scientific interpretation is not an independent source-mechanics peer. Independent scientific peer remains separate.
- Original stderr is empty; no global warning has been assigned to this owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T092247Z-basiliskamide-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: Basiliskamide A'
started_at: '2026-11-03T08:49:42.187283Z'
finished_at: '2026-11-03T09:22:47.675679Z'
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
summary: 'Basiliskamide A: qualified partial review retaining source evidence grades,
  exact representation boundaries and owner-local assay and computed-model limits.'
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/basiliskamide-a.yaml
    sha256: ebcfc2430bbd7e261a7eebe9a8509387ccf9f7999f4a0b4d32055c0e08a324ec
    role: target
  - path: data/natural_products/unclassified/basiliskamide-b.yaml
    sha256: c606b2f6dc6cbde6afebff6ec94da7c8251dcdebbc50cadafefdbe4b65d7b107
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
  selection: Campaign path order 2186; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-c9b993f6e0
targets:
- target_id: naturalproductmech:mibig-c9b993f6e0
  path: data/natural_products/shikimates_and_phenylpropanoids/basiliskamide-a.yaml
  label: Basiliskamide A
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
  - naturalproductmech:mibig-c9b993f6e0
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/aspulvinone-h.yaml
    data/natural_products/shikimates_and_phenylpropanoids/atromentin.yaml data/natural_products/shikimates_and_phenylpropanoids/bactobolin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/bagremycin-a.yaml data/natural_products/shikimates_and_phenylpropanoids/bagremycin-b.yaml
    data/natural_products/shikimates_and_phenylpropanoids/basiliskamide-a.yaml data/natural_products/shikimates_and_phenylpropanoids/bromophene.yaml
    data/natural_products/shikimates_and_phenylpropanoids/butyrolactone-i.yaml data/natural_products/shikimates_and_phenylpropanoids/cacibiocin-b.yaml
    data/natural_products/shikimates_and_phenylpropanoids/cathomycin.yaml --workers
    1 --out /private/tmp/npm-native-checks/batch-219/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-c9b993f6e0
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-219/validate-all-001.tsv
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
  - naturalproductmech:mibig-c9b993f6e0
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
  - naturalproductmech:mibig-c9b993f6e0
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
  - naturalproductmech:mibig-c9b993f6e0
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-219/review-queue-001.tsv
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
  - naturalproductmech:mibig-c9b993f6e0
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-c9b993f6e0
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-c9b993f6e0
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2186-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/basiliskamide-a.yaml
  locator: Complete raw owner, lines 1-101.
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Whole selected owner and 2 history events personally read; current exact
    bytes match retained inventory and capture.
  snapshot_sha256: ebcfc2430bbd7e261a7eebe9a8509387ccf9f7999f4a0b4d32055c0e08a324ec
- evidence_id: support-2186-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219/owner-capture-DATA-001.json
  locator: /records/5/owner_document; /records/5/owner_pin; /records/5/read_started_at;
    /records/5/read_finished_at
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Complete actual captured owner and original access clocks; component resolution
    is assessed separately where applicable.
  snapshot_sha256: e871b113838998b9a0a0e5826413b641567cf80f250dccfc9747e3bd082d6845
- evidence_id: support-2186-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch219/intakes/2186-inspect-001.json
  locator: /status; /source; /targets/0
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Original inspection-only intake with 38 current inputs and explicit maintained
    ownership.
  snapshot_sha256: 8f25aab38f981e6aefecdee5ec28b61a27a66baf892eca73bafc4dc4c1c1d60b
- evidence_id: support-2186-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-target-input-plan-001.json
  locator: /records/5; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Exact current selected raw/history/source frames and input map equal the
    retained inventory and actual intake; cohort 422 placements/94 paths.
  snapshot_sha256: e916ee57bc5ec554e1146cde7cd06bd547c949795e818e70aa9b763769bbab5e
- evidence_id: support-2186-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch219/root-target-input-plan-acceptance-001.json
  locator: /status; /plan; /notes; /actual_intake_acceptance; /source_placements;
    /unique_source_paths
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: ROOT accepts exact saved source-plan and intake equality; this is not a
    scientific verdict.
  snapshot_sha256: 696f459a9a2d88da915d93d977343d7304f9448f71cd29ac63d0f26fd57d261a
- evidence_id: support-2186-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/complete_raw_history; /contexts/6/history_count
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: All 2 owner history events preserved; historical verification annotations
    are not new verification.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-target-input-plan-001.json
  locator: /records/5/proposed_companion_paths; /records/5/direct_companion_predicates;
    /records/5/declared_mechanism_roots_literal; /records/5/component_paths
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: 1 admitted direct companions; selected mechanism applicability and component
    paths retained without transitive expansion.
  snapshot_sha256: e916ee57bc5ec554e1146cde7cd06bd547c949795e818e70aa9b763769bbab5e
- evidence_id: support-2186-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-scope-notes-001.json
  locator: /reading/review_support; /reading/bgc_science; /reading/components; /cautions;
    /curation
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Whole source-reading attribution and bounded 65-token/eight-table zero-hit
    curation scan. The11 complementary cache stanzas are my reading; shared 341663/41900
    stanzas are BGC reading. No new external or corpus-wide absence assertion.
  snapshot_sha256: 58207f6cd3ec20557a15cee20a157352a42c86c9b884ed61e2af20e298c36eb8
- evidence_id: support-2186-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N";
    1 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 219-219; exact retained row /contexts/6/source_scope_inventory/joins/mibig_compounds/matches/0
    in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json;
    raw row SHA256 8a100b26350e45756e6b159ace33d12eebbfef330bdc98f2643eaba5beedc520.
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: 'Retained row fields (structure strings remain in the exact cited row):
    {"mibig_accession":"BGC0000172","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"Basiliskamide
    A","compound_index":"1","standard_inchi_key":"QAHZDGAHECEVRM-HXKCHMFGSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA07306|npatlas:NPA007306","taxon_id":"NCBITaxon:1399144","taxon_label":"Brevibacillus
    laterosporus PE36","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"AXBT01000013.1","locus_from":"84598","locus_to":"132409","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"DOI:10.1021/ol048574m","reference_basis":"COMPOUND_EVIDENCE"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2186-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N";
    0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N";
    2 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 7158-7158; exact retained row /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/0
    in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json;
    raw row SHA256 178b04054a9ef3ae5ce638c443a5f25f94ed616f7269f1ba195c1293d719ad12.
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: 'Retained row fields (structure strings remain in the exact cited row):
    {"standard_inchi_key":"QAHZDGAHECEVRM-HXKCHMFGSA-N","organism_name":"Brevibacillus
    laterosporus","taxon_id":"NCBITaxon:1465","organism_wikidata":"http://www.wikidata.org/entity/Q25840601","reference_doi":"10.1021/NP0201321","structure_wikidata":"http://www.wikidata.org/entity/Q59247254"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2186-row-lotus_occurrences-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 7159-7159; exact retained row /contexts/6/source_scope_inventory/joins/lotus_occurrences/matches/1
    in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json;
    raw row SHA256 bdcf2287ec5c9b66479c2f4666baa6f61a7e8be6782a541383ccacfa9c59c308.
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: 'Retained row fields (structure strings remain in the exact cited row):
    {"standard_inchi_key":"QAHZDGAHECEVRM-HXKCHMFGSA-N","organism_name":"Brevibacillus
    laterosporus","taxon_id":"NCBITaxon:1465","organism_wikidata":"http://www.wikidata.org/entity/Q25840601","reference_doi":"10.1371/JOURNAL.PONE.0090124","structure_wikidata":"http://www.wikidata.org/entity/Q59247254"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2186-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N";
    0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N";
    1 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 1957-1957; exact retained row /contexts/6/source_scope_inventory/joins/npclassifier/matches/0
    in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json;
    raw row SHA256 5fa558b263f873a2f9a201981369f3813c66ef4b57dd3facabd1bd4acbaec07e.
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: 'Retained row fields (structure strings remain in the exact cited row):
    {"standard_inchi_key":"QAHZDGAHECEVRM-HXKCHMFGSA-N","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Phenylpropanoids (C6-C3)","class_results":"Cinnamic
    acids and derivatives","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2186-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N";
    0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N";
    0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "QAHZDGAHECEVRM-HXKCHMFGSA-N";
    0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact chebi_id from exact full-key structure rows; query
    []; 0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-companion-12
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/12
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Complete directly admitted companion Basiliskamide B, full keyHCZNVGHFFHRIFM-HXKCHMFGSA-N,
    2 histories; no identity/activity/producer transfer.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-companion-12-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N";
    1 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-companion-12-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 220-220; exact retained row /contexts/12/source_scope_inventory/joins/mibig_compounds/matches/0
    in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json;
    raw row SHA256 c1997f4270b1a9362c9a9b37d7e80b04bbedb21395460e5ad3695efbb92e8436.
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: 'Retained row fields (structure strings remain in the exact cited row):
    {"mibig_accession":"BGC0000172","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"Basiliskamide
    B","compound_index":"2","standard_inchi_key":"HCZNVGHFFHRIFM-HXKCHMFGSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA018193","taxon_id":"NCBITaxon:1399144","taxon_label":"Brevibacillus
    laterosporus PE36","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"AXBT01000013.1","locus_from":"84598","locus_to":"132409","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"DOI:10.1021/ol048574m","reference_basis":"COMPOUND_EVIDENCE"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2186-companion-12-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N";
    0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-companion-12-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N";
    1 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-companion-12-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 2315-2315; exact retained row /contexts/12/source_scope_inventory/joins/lotus_occurrences/matches/0
    in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json;
    raw row SHA256 a4363d83aa4868fba687749766a6a14e5fa1b457caac6cea444a6366d72080b7.
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: 'Retained row fields (structure strings remain in the exact cited row):
    {"standard_inchi_key":"HCZNVGHFFHRIFM-HXKCHMFGSA-N","organism_name":"Brevibacillus
    laterosporus","taxon_id":"NCBITaxon:1465","organism_wikidata":"http://www.wikidata.org/entity/Q25840601","reference_doi":"10.1021/NP0201321","structure_wikidata":"http://www.wikidata.org/entity/Q57751679"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2186-companion-12-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N";
    0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-companion-12-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N";
    1 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-companion-12-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 791-791; exact retained row /contexts/12/source_scope_inventory/joins/npclassifier/matches/0
    in /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json;
    raw row SHA256 2ddefbbd103abf8834574c3b5ccec11ec4919b1940a355c64c224c413131294d.
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: 'Retained row fields (structure strings remain in the exact cited row):
    {"standard_inchi_key":"HCZNVGHFFHRIFM-HXKCHMFGSA-N","pathway_results":"Polyketides|Shikimates
    and Phenylpropanoids","superclass_results":"Phenylpropanoids (C6-C3)|Linear polyketides","class_results":"Cinnamic
    acids and derivatives|Open-chain polyketides","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2186-companion-12-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N";
    0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-companion-12-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N";
    0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-companion-12-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "HCZNVGHFFHRIFM-HXKCHMFGSA-N";
    0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-companion-12-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Saved predicate exact chebi_id from exact full-key structure rows; query
    []; 0 retained rows. Empty results have only this exact pinned scope.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-taxon-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/source_taxa; /contexts/6/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/6/source_scope_inventory/nonorganism_matches; /cached_taxonomy/unmatched_ids
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: 'Exact selected taxon routes: no forward-merge/nonorganism matches and
    no unmatched cached IDs. This is cached routing, not live taxonomy or proof of
    production.'
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-taxon-1399144
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/27
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Complete cached stanza NCBITaxon:1399144, physical corpus_taxa.obo lines
    128366-128369. Whole stanza personally read. Cached labels/synonyms retain taxonomic
    scope, not experimentally established producer identity.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-taxon-1465
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219-tentative/bgc-prep/bgc-conditional219-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/1
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Complete cached stanza NCBITaxon:1465, physical corpus_taxa.obo lines 2207-2211.
    Whole stanza personally read. Cached labels/synonyms retain taxonomic scope, not
    experimentally established producer identity.
  snapshot_sha256: 98c6f456b593a33826ade882fe92e436ac71759ffc086279544719fe56da2c1d
- evidence_id: support-2186-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch219/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/smiles; /records/5/inchi; /records/5/comparisons;
    /records/5/atom_correspondence
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Both stored forms parsed as neutral C23H31NO4, 28 atoms and 28 bonds. Standard
    InChI, full key, formula, charge and atom/bond counts agree, but both canonical
    SMILES comparisons are false and the chirality-aware atom map is empty. The saved
    SMILES has terminal amide C13(=O14)–N15H2; the InChI-derived form has C20(–O25H)=N23H.
    This is a bounded amide/imidic-acid representation difference, not proof of wrong
    molecular identity or independently established tautomer equivalence. Both forms
    retain four specified tetrahedral centers (SMILES 2R,4S,5R,7R) and three specified
    C=C bonds (SMILES bonds 9E,11Z,20E); only the InChI form adds unspecified C=N
    bond 23. Literal stereo_complete:true does not establish every geometric or natural
    stereochemical assignment.
  snapshot_sha256: 4c9a084d7b80a7634173a635f8576b06db26a025f5c996902bbe36ab20e22187
- evidence_id: support-2186-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch219/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/smiles/computed/potential_stereo;
    /records/5/smiles/computed/stereo_counts; /records/5/inchi/computed/potential_stereo;
    /records/5/inchi/computed/stereo_counts; /records/5/smiles/computed/atoms; /records/5/smiles/computed/bonds;
    /records/5/inchi/computed/atoms; /records/5/inchi/computed/bonds
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Four specified tetrahedral centers and three specified C=C bonds in both
    forms; extra unspecified C=N only in InChI-derived form; literal stereo_complete:true
    is atom-centered.
  snapshot_sha256: 4c9a084d7b80a7634173a635f8576b06db26a025f5c996902bbe36ab20e22187
- evidence_id: support-2186-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch219/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/smiles/computed; /records/5/inchi/computed; /records/5/atom_correspondence
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: 'Saved SMILES: one benzene ring, ester C18(=O19)–O17–C4, terminal amide
    C13(=O14)–N15, no saturated C5O candidate sugar ring. InChI-derived terminal imidic-acid
    representation and empty map are preserved.'
  snapshot_sha256: 4c9a084d7b80a7634173a635f8576b06db26a025f5c996902bbe36ab20e22187
- evidence_id: support-2186-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165-172.
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: The maintained stereo_complete derivation asks FindMolChiralCenters for
    unassigned atom centers; it is not a universal geometric/axial/natural-stereo
    assertion.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2186-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch219/chemistry-local/diagnostic-execution-001.json
  locator: Complete original JSON execution receipt.
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Original single diagnostic execution receipt and its saved stdout/stderr;
    no repeat computation.
  snapshot_sha256: 65a232c4f9e76cdcba0d36f2b2afdeb2b1ff6bd3948423186dc66d8a8d83c329
- evidence_id: support-2186-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch219/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /original_terminal; /false_comparisons; /stderr_bytes;
    /limitations
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: ROOT accepts the original 20-form local computation, with empty stderr
    and explicit canonical/identity limitations.
  snapshot_sha256: 9d86c46cc594b27eb7d8af2b459a505806fab0fe879924bcb82d8915ea91c6c0
- evidence_id: support-2186-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch219/root-intake-ready-001.json
  locator: /status; /intake_summary; /source_placements; /unique_source_paths; /per_order_counts;
    /mechanism_owner_orders
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: ROOT accepts ten original intakes and exact 422/94 source map; no scientific
    verdict.
  snapshot_sha256: b55a9ac100bcb962b17d4ea2de485fca21016491c09d0c2c0fdf309c4cf0e5f4
- evidence_id: support-2186-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch219/root-native-checks-acceptance-001.json
  locator: /status; /ledger; /local_checks_passed; /queue_rows; /selected_queue_rows;
    /unavailable
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Five original local gates passed; queue 8922 total/13 selected rows. Full
    QC and OAK unavailable; local gate success is not scientific sign-off.
  snapshot_sha256: 1970e7734ae524688ab1064cfba1f840b5619df82803cd1a59297ba45438a4ef
- evidence_id: support-2186-source-ownership
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch219/intakes/2186-inspect-001.json
  locator: /targets/0/owner_paths; /targets/0/ownership_note
  accessed_at: '2026-11-03T09:08:16.729606Z'
  support: supports
  summary: Generated inventory/seeder fields and, where present, curator-owned mechanism
    components retain distinct maintained owners. No source record or native status/history
    was edited.
  snapshot_sha256: 8f25aab38f981e6aefecdee5ec28b61a27a66baf892eca73bafc4dc4c1c1d60b
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-219/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-219/native-current219-five-gates-execution-001.json
  accessed_at: '2026-11-03T08:54:55.683305Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 4924b09f392ce3a7de40076e78b039af61006aab5babfc7336809c1d1a7066df
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-219/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-219/native-current219-five-gates-execution-001.json
  accessed_at: '2026-11-03T08:55:22.353823Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 95bff207615fa197d63e6a572adfc1000494959736ef2bbf81763964ad50960a
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-219/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-219/native-current219-five-gates-execution-001.json
  accessed_at: '2026-11-03T08:55:44.349599Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-219/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-219/native-current219-five-gates-execution-001.json
  accessed_at: '2026-11-03T08:56:21.949336Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-219/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-219/native-current219-five-gates-execution-001.json
  accessed_at: '2026-11-03T08:56:34.961048Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 42dcce392aeabee4644ffdf1db140ee988d03426e6bedea09bdba7dfc54b24c9
assessments:
- assessment_id: support-2186-A1
  area: identity
  topic: Exact structure concept and grounding scope
  outcome: supported
  summary: Basiliskamide A retains the exact MIBiG-derived full key QAHZDGAHECEVRM-HXKCHMFGSA-N
    and neutral C23H31NO4. The saved exact-key ChEBI frame is empty, supporting MINTED
    only within that retained source scope. Active BGC0000172 version 5 names this
    compound at index 1; questionable quality and unknown completeness are source
    metadata, not a scientific rejection. Basiliskamide B is a direct same-BGC context
    with a different connectivity key and ester position, despite the same formula
    and stereochemical-layer pattern. The two NPAtlas spellings are retained source
    xrefs, not freshly resolved identities.
  target_ids:
  - naturalproductmech:mibig-c9b993f6e0
  evidence_ids:
  - support-2186-owner
  - support-2186-capture
  - support-2186-intake
  - support-2186-source-plan
  - support-2186-plan-acceptance
  - support-2186-direct-contexts
  - support-2186-query-chebi_structures
  - support-2186-row-mibig_compounds-0
  - support-2186-companion-12
  - support-2186-companion-12-row-mibig_compounds-0
  - support-2186-companion-12-row-lotus_occurrences-0
  - support-2186-companion-12-row-npclassifier-0
  dimensions:
  - name: standard_inchi_key
    value: QAHZDGAHECEVRM-HXKCHMFGSA-N
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-direct-contexts
    - support-2186-query-chebi_structures
    - support-2186-row-mibig_compounds-0
    - support-2186-companion-12
    - support-2186-companion-12-row-mibig_compounds-0
    - support-2186-companion-12-row-lotus_occurrences-0
    - support-2186-companion-12-row-npclassifier-0
  - name: grounding_scope
    value: MINTED; no retained exact-key ChEBI hit; no fresh xref resolution
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-direct-contexts
    - support-2186-query-chebi_structures
    - support-2186-row-mibig_compounds-0
    - support-2186-companion-12
    - support-2186-companion-12-row-mibig_compounds-0
    - support-2186-companion-12-row-lotus_occurrences-0
    - support-2186-companion-12-row-npclassifier-0
- assessment_id: support-2186-A2
  area: representation
  topic: Paired molecular representations and stereochemical limits
  outcome: supported
  summary: Both stored forms parsed as neutral C23H31NO4, 28 atoms and 28 bonds. Standard
    InChI, full key, formula, charge and atom/bond counts agree, but both canonical
    SMILES comparisons are false and the chirality-aware atom map is empty. The saved
    SMILES has terminal amide C13(=O14)–N15H2; the InChI-derived form has C20(–O25H)=N23H.
    This is a bounded amide/imidic-acid representation difference, not proof of wrong
    molecular identity or independently established tautomer equivalence. Both forms
    retain four specified tetrahedral centers (SMILES 2R,4S,5R,7R) and three specified
    C=C bonds (SMILES bonds 9E,11Z,20E); only the InChI form adds unspecified C=N
    bond 23. Literal stereo_complete:true follows the maintained atom-centered rule
    and does not establish every geometric or natural stereochemical assignment. Original
    diagnostic stderr is empty.
  target_ids:
  - naturalproductmech:mibig-c9b993f6e0
  evidence_ids:
  - support-2186-owner
  - support-2186-capture
  - support-2186-intake
  - support-2186-source-plan
  - support-2186-plan-acceptance
  - support-2186-chemistry
  - support-2186-stereo
  - support-2186-stereo-method
  - support-2186-diagnostic-execution
  - support-2186-diagnostic-acceptance
  dimensions:
  - name: stereochemical_resolution
    value: Four specified tetrahedral centers and three specified C=C bonds in both
      forms; extra unspecified C=N only in InChI-derived form; literal stereo_complete:true
      is atom-centered.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-chemistry
    - support-2186-stereo
    - support-2186-stereo-method
    - support-2186-diagnostic-execution
    - support-2186-diagnostic-acceptance
  - name: representation_correspondence
    value: Canonical isomeric/nonisomeric comparisons false; empty chirality-aware
      map; normalized identifiers agree; full_graph_identity_established:false.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-chemistry
    - support-2186-stereo
    - support-2186-stereo-method
    - support-2186-diagnostic-execution
    - support-2186-diagnostic-acceptance
- assessment_id: support-2186-A3
  area: provenance
  topic: Producer, occurrence and locus evidence grades
  outcome: supported
  summary: The retained MIBiG producer is Brevibacillus laterosporus PE36, NCBITaxon:1399144,
    graded SOURCE_ASSERTION; BGC0000172 is CLUSTER_UNSTATED with no locus experiment
    stated. AXBT01000013.1 coordinates 84598–132409 are retained locus provenance.
    The two LOTUS statements concern species-level Brevibacillus laterosporus, NCBITaxon:1465,
    and do not upgrade the PE36 producer or establish two independent production experiments.
    Cache labels are locally consistent at their stated species/strain levels.
  target_ids:
  - naturalproductmech:mibig-c9b993f6e0
  evidence_ids:
  - support-2186-owner
  - support-2186-capture
  - support-2186-intake
  - support-2186-source-plan
  - support-2186-plan-acceptance
  - support-2186-row-mibig_compounds-0
  - support-2186-row-lotus_occurrences-0
  - support-2186-row-lotus_occurrences-1
  - support-2186-taxon-routes
  - support-2186-taxon-1399144
  - support-2186-taxon-1465
  dimensions:
  - name: taxon_and_strain_scope
    value: NCBITaxon:1399144; NCBITaxon:1465; cached/source scope only
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-row-mibig_compounds-0
    - support-2186-row-lotus_occurrences-0
    - support-2186-row-lotus_occurrences-1
    - support-2186-taxon-routes
    - support-2186-taxon-1399144
    - support-2186-taxon-1465
  - name: producer_evidence_tier
    value: SOURCE_ASSERTION; PE36 strain1399144 distinct from occurrence species1465
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-row-mibig_compounds-0
    - support-2186-row-lotus_occurrences-0
    - support-2186-row-lotus_occurrences-1
    - support-2186-taxon-routes
    - support-2186-taxon-1399144
    - support-2186-taxon-1465
  - name: locus_evidence_tier
    value: CLUSTER_UNSTATED; no locus experiment stated
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-row-mibig_compounds-0
    - support-2186-row-lotus_occurrences-0
    - support-2186-row-lotus_occurrences-1
    - support-2186-taxon-routes
    - support-2186-taxon-1399144
    - support-2186-taxon-1465
- assessment_id: support-2186-A4
  area: evidence
  topic: Citation placement and historical verification scope
  outcome: supported
  summary: DOI:10.1021/ol048574m is explicitly the MIBiG COMPOUND_EVIDENCE citation.
    DOI:10.1021/NP0201321 and DOI:10.1371/JOURNAL.PONE.0090124 belong to the two LOTUS
    occurrence assertions. Citation presence and normalization do not establish publication
    independence or upgrade source producer/locus grades. No original article, live
    accession or protein sequence was inspected in this review.
  target_ids:
  - naturalproductmech:mibig-c9b993f6e0
  evidence_ids:
  - support-2186-owner
  - support-2186-capture
  - support-2186-intake
  - support-2186-source-plan
  - support-2186-plan-acceptance
  - support-2186-history
  - support-2186-source-notes
  - support-2186-row-mibig_compounds-0
  - support-2186-row-lotus_occurrences-0
  - support-2186-row-lotus_occurrences-1
  dimensions:
  - name: citation_scope
    value: COMPOUND_EVIDENCE DOI:10.1021/ol048574m; two separate LOTUS DOI assertions
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-history
    - support-2186-source-notes
    - support-2186-row-mibig_compounds-0
    - support-2186-row-lotus_occurrences-0
    - support-2186-row-lotus_occurrences-1
- assessment_id: support-2186-A5
  area: scope
  topic: Occurrence, assay and companion boundaries
  outcome: supported
  summary: 'Two species-level LOTUS occurrence assertions remain distinct from the
    PE36 producer. No owner bioactivities, molecular targets, bioactivity summary
    or mechanism roots are present. Exact selected PubChem, BindingDB and AntibioticMech
    joins are empty: zero actual AIDs and zero blank-AID sentinels. The direct Basiliskamide
    B context contributes no transferred activity or stereochemistry. These finite
    negatives do not establish inactivity or literature-wide absence.'
  target_ids:
  - naturalproductmech:mibig-c9b993f6e0
  evidence_ids:
  - support-2186-owner
  - support-2186-capture
  - support-2186-intake
  - support-2186-source-plan
  - support-2186-plan-acceptance
  - support-2186-query-lotus_occurrences
  - support-2186-query-cyanometdb_occurrences
  - support-2186-query-pubchem_bioassay
  - support-2186-query-bindingdb_targets
  - support-2186-query-antibioticmech_inchikeys
  - support-2186-query-chebi_origins
  - support-2186-row-lotus_occurrences-0
  - support-2186-row-lotus_occurrences-1
  - support-2186-companion-12
  - support-2186-companion-12-row-mibig_compounds-0
  - support-2186-companion-12-row-lotus_occurrences-0
  - support-2186-companion-12-row-npclassifier-0
  dimensions:
  - name: occurrence_scope
    value: Two LOTUS species-level assertions; one separately graded strain producer
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-query-lotus_occurrences
    - support-2186-query-cyanometdb_occurrences
    - support-2186-query-pubchem_bioassay
    - support-2186-query-bindingdb_targets
    - support-2186-query-antibioticmech_inchikeys
    - support-2186-query-chebi_origins
    - support-2186-row-lotus_occurrences-0
    - support-2186-row-lotus_occurrences-1
    - support-2186-companion-12
    - support-2186-companion-12-row-mibig_compounds-0
    - support-2186-companion-12-row-lotus_occurrences-0
    - support-2186-companion-12-row-npclassifier-0
  - name: assay_scope
    value: No selected retained assay/target/sibling rows; no congener transfer or
      inactivity inference
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-query-lotus_occurrences
    - support-2186-query-cyanometdb_occurrences
    - support-2186-query-pubchem_bioassay
    - support-2186-query-bindingdb_targets
    - support-2186-query-antibioticmech_inchikeys
    - support-2186-query-chebi_origins
    - support-2186-row-lotus_occurrences-0
    - support-2186-row-lotus_occurrences-1
    - support-2186-companion-12
    - support-2186-companion-12-row-mibig_compounds-0
    - support-2186-companion-12-row-lotus_occurrences-0
    - support-2186-companion-12-row-npclassifier-0
- assessment_id: support-2186-A6
  area: other
  topic: Computed classification and full-table topology limits
  outcome: supported
  summary: NPClassifier reports Shikimates and Phenylpropanoids / Phenylpropanoids
    (C6-C3) / Cinnamic acids and derivatives, is_glycoside=false. The saved SMILES
    has a cinnamoyl ester C18(=O19)–O17–C4, one benzene ring and the separately described
    terminal amide. No saturated C5O candidate sugar ring is present. The cinnamoyl
    substructure supports a bounded model-family interpretation; MIBiG PKS and the
    computational filing label remain different axes, not competing experimental pathway
    assignments.
  target_ids:
  - naturalproductmech:mibig-c9b993f6e0
  evidence_ids:
  - support-2186-owner
  - support-2186-capture
  - support-2186-intake
  - support-2186-source-plan
  - support-2186-plan-acceptance
  - support-2186-topology
  - support-2186-chemistry
  - support-2186-row-npclassifier-0
  - support-2186-row-mibig_compounds-0
  dimensions:
  - name: computed_classification
    value: Shikimates and Phenylpropanoids / Phenylpropanoids (C6-C3) / Cinnamic acids
      and derivatives; glycoside=false; npclassifier.gnps2.org@2026-09-07
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-topology
    - support-2186-chemistry
    - support-2186-row-npclassifier-0
    - support-2186-row-mibig_compounds-0
- assessment_id: support-2186-A7
  area: completeness
  topic: Partial scientific completion and maintained ownership
  outcome: supported
  summary: All seven core areas and twelve dimensions were assessed against actual
    intake, whole raw/history, retained source rows/cache and both complete saved
    chemical forms. Five local gates passed; full QC/OAK and external verification
    remain unavailable. This owner has no selected mechanism roots/components and
    no maintained reader applies. The inspected source assertions and bounded local
    structure facts provide positive support; no concrete source-record contradiction
    requiring a curation finding was established. Native SEEDED status/history and
    all corpus/source bytes remain unchanged.
  target_ids:
  - naturalproductmech:mibig-c9b993f6e0
  evidence_ids:
  - support-2186-owner
  - support-2186-capture
  - support-2186-intake
  - support-2186-source-plan
  - support-2186-plan-acceptance
  - support-2186-history
  - support-2186-source-notes
  - support-2186-direct-contexts
  - support-2186-intake-acceptance
  - support-2186-native-acceptance
  - support-2186-diagnostic-acceptance
  - support-2186-source-ownership
  dimensions:
  - name: review_completion
    value: partial; full QC/OAK/external verification unavailable; no native status/history
      or source edits
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2186-owner
    - support-2186-capture
    - support-2186-intake
    - support-2186-source-plan
    - support-2186-plan-acceptance
    - support-2186-history
    - support-2186-source-notes
    - support-2186-direct-contexts
    - support-2186-intake-acceptance
    - support-2186-native-acceptance
    - support-2186-diagnostic-acceptance
    - support-2186-source-ownership
findings: []
actions: []
limitations:
- No external requests or fresh primary-literature/API/ontology/taxonomy/accession
  verification. Source xrefs and historical citations remain assertions at their stated
  resolution.
- The empty atom map and canonical differences remain unresolved at full graph-identity
  level; normalized identifier equality does not independently prove tautomer equivalence.
- Full QC and complete OAK authority coverage were unavailable. Local validation and
  reproduction do not prove biological claims or justify native status promotion.
- No source record, generated owner, component or curation history was edited in this
  review.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Personal whole reading covers the selected owner/history, admitted direct companions,
  assigned full source payloads and both saved molecular tables; cache/components
  carry explicitly identified team attribution.
- Author previously prepared controller/diagnostic/assembler sources; scientific interpretation
  is not an independent source-mechanics peer. Independent scientific peer remains
  separate.
- Original stderr is empty; no global warning has been assigned to this owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-219
```
