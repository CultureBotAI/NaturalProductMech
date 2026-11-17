# Local evidence review: biscognienyne B

- Review: 20261103T185022Z-biscognienyne-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T18:10:20.616322Z
- Finished UTC: 2026-11-03T18:50:22.012199Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

biscognienyne B: stored forms and retained source scope are coherent within admitted local evidence. No selected mechanism reader applies; source, occurrence and prediction limits remain explicit. Qualified partial review with no new supported finding.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2277; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:167050 | data/natural_products/terpenoids/biscognienyne-b.yaml | generated | biscognienyne B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:167050 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:167050 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:167050 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:167050 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:167050 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:167050 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:167050 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:167050 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding

identity: supported. Targets: CHEBI:167050.

The EXACT CHEBI:167050 owner retains full key UAAPCPSYCUMTPM-LVQVYYBASA-N, matching the admitted exact-key ChEBI row. MIBiG BGC0002290 version 2 records source compound_index=1. Its eleven admitted BGC companions retain distinct identifiers and structures rather than becoming Biscognienyne B synonyms.

### Stored representation and stereochemistry

representation: supported. Targets: CHEBI:167050.

Both saved forms agree in neutral formula C16H20O3, standard InChI, full key and both canonical SMILES strings, with 19 atoms and 20 bonds. Four tetrahedral centres are specified in the SMILES table: 4 R, 5 S, 7 R and 10 R. The complete graph has a fused epoxide/carbocycle, two hydroxyls, one alkyne and three alkenes; no additional unresolved potential E/Z entry is listed. Stored matching and representation equality do not independently establish experimental stereochemistry or natural identity.

### Producer, locus, taxon and strain roles

provenance: supported. Targets: CHEBI:167050.

MIBiG asserts Biscogniauxia sp., NCBITaxon:1896107, as producer with SOURCE_ASSERTION. Heterologous expression supports CLUSTER_DEMONSTRATED for BGC0002290 and MT109335.1:1–37984, with retained OTHER BGC class. The entry remains active/questionable/unknown. ChEBI origin adds strain/detection context 71-10-1-1, while LOTUS uses the broader genus NCBITaxon:97376. These taxon and strain scopes remain distinct.

### Citation placement and primary-source limits

evidence: supported. Targets: CHEBI:167050.

PMID:32364293 is the MIBiG ENTRY citation and the ChEBI-origin citation, so their placements do not establish independent publications. LOTUS cites DOI:10.1021/ACS.ORGLETT.6B03264. Among direct BGC2290 companions, Compound 15 has its own COMPOUND_BIOACTIVITY citation role; not every companion citation has the selected ENTRY role. No paper or experimental construct was freshly verified.

### Occurrence and assay boundaries

scope: supported. Targets: CHEBI:167050.

Two occurrences are written: a LOTUS genus-level Biscogniauxia assertion and a ChEBI Biscogniauxia sp. origin with strain context 71-10-1-1. Occurrence remains distinct from production even when citations/taxa overlap. Saved PubChem, BindingDB and AntibioticMech routes have no selected-owner assay payload. This bounded absence does not imply inactivity or authorize transfer from the eleven companions.

### Computed classification and complete saved topology

other: supported. Targets: CHEBI:167050.

NPClassifier retains Terpenoids / Meroterpenoids / Miscellaneous meroterpenoids with is_glycoside=false. The complete topology has a three-member epoxide fused to a six-carbon ring, two hydroxyls, an alkyne and alkenes, with no carbonyl. Its sole C–O–C bridge is the epoxide, not a glycosidic linkage. The retained ChEBI epoxide definition and computed meroterpenoid class are structurally compatible within this limited review; biosynthetic origin was not independently proved.

### Review completion and unavailable verification

completeness: unknown. Targets: CHEBI:167050.

The complete owner, actual 48-input intake, all nine source frames and five positive rows, applicable cached taxa, eleven direct companions and both saved forms were reviewed. No selected graph, pathway, target or component is declared. Local checks and chemistry are accepted; FullQC, full OAK and primary/identifier verification remain unavailable. This is a qualified partial review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2277-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/biscognienyne-b.yaml; lines 1–115 | supports | Whole current plaintext owner and all 3 history events; literal identifier CHEBI:167050, label biscognienyne B, full key UAAPCPSYCUMTPM-LVQVYYBASA-N. Historical annotations remain retained claims. |
| support-2277-capture | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/6/owner_document; /records/6/owner_pin | supports | Complete captured owner, including all written identity, source, occurrence, classification, mechanism and history fields that are present. |
| support-2277-source-plan | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6 | supports | Complete admitted selected context, all nine query frames/full payloads, direct companions and 48 planned inputs; source-scope authority is not proof of scientific correctness. |
| support-2277-intake | /private/tmp/npm-review-work/shared-next-batch228/intakes/2277-inspect-001.json; /targets; /source; /status | supports | Complete actual canonical intake target list, source-input ownership and inspection-only status. |
| support-2277-intake-ready | /private/tmp/npm-review-work/shared-next-batch228/root-intake-ready-001.json; /status; /accepted; /intake_summary; /verification; /limits | supports | ROOT acceptance of the original actual intakes and exact current input maps, retaining limits. |
| support-2277-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-input-plan-acceptance-001.json; /status; /accepted; /plan; /source_notes; /per_order_counts; /source_placements; /unique_source_paths | supports | ROOT acceptance of the original composition and complete input maps. |
| support-2277-source-notes | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-scope-notes-001.json; /observer; /recorded_at; /batch; /status; /inventory; /inventory_ROOT_acceptance; /inventory_ROOT_acceptance_inventory_key; /collector_source; /collector_source_adoption; /collector_original_tools; /collector_original_terminal; /prior_final_acceptance; /prior_final_expected_status; /accepted_prior_remaining; /frozen_remaining; /actual_frozen228_remaining; /requirements; /selected_profile; /totals; /per_order_input_counts; /reading; /curation; /cautions; /current_inventory_input_pin_count; /future_actual_roles; /independent_actual_selection_capture_authority; /scientific_verdicts; /external_requests; /source_records_modified; /target_invocations_by_this_step | supports | Complete source-reading attribution and bounded curation scan, with source grades, cached taxonomy and historical limits; not a new primary observation. |
| support-2277-chemistry | /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json; /records/6/declared_structure; /records/6/smiles/computed; /records/6/inchi/computed; /records/6/comparisons; /records/6/atom_correspondence | supports | Original saved paired computations: all ten comparison flags are true and both forms retain the declared full key; atom correspondence explicitly does not establish full graph identity. No experimental identity conclusion follows. |
| support-2277-topology | /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed; /records/6/inchi/computed | supports | Complete computed tables show an epoxide fused to a six-carbon ring, two hydroxyls, one alkyne and three alkenes, with no carbonyl; the sole C–O–C bridge is the epoxide. All atom, bond, ring, stereo and motif fields were read. |
| support-2277-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-local-diagnostics-acceptance-001.json; /observer; /observed_at; /status; /accepted; /DATA; /execution; /original_tools; /source_adoption; /runtime_authorization; /intake_ready; /original_terminal; /verification; /unspecified_stereo; /ROOT_reading; /limits; /external_requests; /target_invocations_by_this_acceptance | supports | ROOT acceptance of the original 20-form diagnostic and current inputs; two original undefined-stereo warnings remain global and unassigned. |
| support-2277-native-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-native-five-gates-acceptance-001.json; /observer; /recorded_at; /batch; /status; /execution; /original_tools; /native_saved_readback; /source_adoption; /selection_authority; /original_terminal; /five_exits; /strict_selected_records; /strict_full_records; /validation_error_rows; /lock_records; /reproduced_byte_identical_records; /queue_rows; /queue_groups; /selected_queue_rows; /root_reading; /queue_complete_byte_proof_attribution; /all_current_pins_checked; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /observer_correction; /external_requests; /target_reexecutions; /record_or_LIVE_changes | supports | ROOT acceptance of five original local gates; FullQC and full OAK remain unavailable. |
| support-2277-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/source_scope_inventory/joins/mibig_compounds | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2277-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; lines 2771–2771 | supports | Complete physical TSV payload decoded without changing blank fields: {"mibig_accession":"BGC0002290","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"biscognienyne B","compound_index":"1","smiles":"CC(=CC[C@@]12[C@@H](O1)[C@@H](C=C([C@H]2O)C#CC(=C)C)O)C","standard_inchi":"InChI=1S/C16H20O3/c1-10(2)5-6-12-9-13(17)15-16(19-15,14(12)18)8-7-11(3)4/h7,9,13-15,17-18H,1,8H2,2-4H3/t13-,14-,15+,16-/m1/s1","standard_inchi_key":"UAAPCPSYCUMTPM-LVQVYYBASA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA023808","taxon_id":"NCBITaxon:1896107","taxon_label":"Biscogniauxia sp.","bgc_classes":"other","bgc_subclasses":"other","genome_accession":"MT109335.1","locus_from":"1","locus_to":"37984","locus_evidence_methods":"Heterologous expression","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:32364293","reference_basis":"ENTRY"} |
| support-2277-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/source_scope_inventory/joins/chebi_structures | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2277-row-chebi_structures-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; lines 43315–43315 | supports | Complete physical TSV payload decoded without changing blank fields: {"chebi_id":"CHEBI:167050","name":"biscognienyne B","definition":"A member of the class of epoxides that is (1R,6S)-7-oxabicyclo[4.1.0]hept-3-ene substituted by 3-methylbut-2-en-1-yl, hydroxy, 2-methylbut-1-en-3-yn-4-yl, and hydroxy groups at positions 1, 2R, 3 and 5R. It is a meroterpenoid natural product synthesized by the Ascomycota fungus Biscogniauxia sp.","stars":"3","standard_inchi_key":"UAAPCPSYCUMTPM-LVQVYYBASA-N","smiles":"C=C(C)C#CC1=C[C@@H](O)[C@@H]2O[C@]2(CC=C(C)C)[C@@H]1O"} |
| support-2277-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/source_scope_inventory/joins/lotus_occurrences | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2277-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; lines 8594–8594 | supports | Complete physical TSV payload decoded without changing blank fields: {"standard_inchi_key":"UAAPCPSYCUMTPM-LVQVYYBASA-N","organism_name":"Biscogniauxia","taxon_id":"NCBITaxon:97376","organism_wikidata":"http://www.wikidata.org/entity/Q2153376","reference_doi":"10.1021/ACS.ORGLETT.6B03264","structure_wikidata":"http://www.wikidata.org/entity/Q105268528"} |
| support-2277-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2277-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/source_scope_inventory/joins/npclassifier | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2277-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; lines 2361–2361 | supports | Complete physical TSV payload decoded without changing blank fields: {"standard_inchi_key":"UAAPCPSYCUMTPM-LVQVYYBASA-N","smiles":"CC(=CC[C@@]12[C@@H](O1)[C@@H](C=C([C@H]2O)C#CC(=C)C)O)C","pathway_results":"Terpenoids","superclass_results":"Meroterpenoids","class_results":"Miscellaneous meroterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"} |
| support-2277-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/source_scope_inventory/joins/pubchem_bioassay | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2277-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/source_scope_inventory/joins/bindingdb_targets | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2277-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2277-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/source_scope_inventory/joins/chebi_origins | supports | Saved frame: predicate=exact chebi_id from exact full-key structure rows; query=['CHEBI:167050']; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2277-row-chebi_origins-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; lines 17153–17153 | supports | Complete physical TSV payload decoded without changing blank fields: {"chebi_id":"CHEBI:167050","species_text":"Biscogniauxia sp.","species_accession":"1896107","component_text":"","strain_text":"71-10-1-1","source_accession":"32364293","comments":"GenBank: MT109335.1"} |
| support-2277-routes | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/source_scope_inventory/matched_chebi_ids; /records/6/source_scope_inventory/source_taxa; /records/6/source_scope_inventory/forward_taxon_merge_matches; /records/6/source_scope_inventory/nonorganism_matches; /records/6/source_scope_inventory/actual_assay_rows; /records/6/source_scope_inventory/blank_AID_sentinels; /records/6/source_scope_inventory/related_corpus_rows | supports | Complete saved non-query route fields: {"matched_chebi_ids":["CHEBI:167050"],"source_taxa":["NCBITaxon:1896107","NCBITaxon:97376"],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"actual_assay_rows":[],"blank_AID_sentinels":[],"related_corpus_rows":[]} |
| support-2277-cache-1896107 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/69 | supports | Complete cached stanza with literal names/synonyms and local scope: [Term]<br>id: NCBITaxon:1896107<br>name: Biscogniauxia sp.<br><br> |
| support-2277-cache-97376 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/26 | supports | Complete cached stanza with literal names/synonyms and local scope: [Term]<br>id: NCBITaxon:97376<br>name: Biscogniauxia<br><br> |
| support-2277-companions | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/6/proposed_companion_paths; /records/6/direct_companion_predicates | supports | Exact 11 direct companions and predicates establish comparison scope, not transferable assays or mechanisms. |
| support-2277-companion-0 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/0 | supports | Complete admitted companion raw/history and saved source context: 3,4-dihydroxy-5-polyprenylbenzoic acid; identifier CHEBI:64921; full key NMAKQSXJWYBYRF-UHFFFAOYSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| support-2277-companion-1 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/1 | supports | Complete admitted companion raw/history and saved source context: 4-hydroxy-3-prenylbenzoic acid; identifier naturalproductmech:mibig-b4ad51fa2f; full key LBSJJNAMGVDGCU-UHFFFAOYSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| support-2277-companion-2 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/2 | supports | Complete admitted companion raw/history and saved source context: compound 7; identifier naturalproductmech:mibig-92c7bb9c67; full key ITBNIRGMDWCANJ-UHFFFAOYSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| support-2277-companion-3 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/3 | supports | Complete admitted companion raw/history and saved source context: compound 8; identifier naturalproductmech:mibig-007406ddf9; full key HHJKLMAAAQXSLU-UHFFFAOYSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| support-2277-companion-4 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/4 | supports | Complete admitted companion raw/history and saved source context: prenylhydroquinone; identifier naturalproductmech:mibig-8029a6a4d2; full key RPIWRSVHAHNACM-UHFFFAOYSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| support-2277-companion-5 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/16 | supports | Complete admitted companion raw/history and saved source context: compound 11; identifier naturalproductmech:mibig-21c4af6890; full key XRWGLEWIDBKJHA-UHFFFAOYSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| support-2277-companion-6 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/17 | supports | Complete admitted companion raw/history and saved source context: compound 12; identifier naturalproductmech:mibig-5cc4b239f3; full key IAAUFTNAVRJTIR-UHFFFAOYSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| support-2277-companion-7 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/18 | supports | Complete admitted companion raw/history and saved source context: compound 15; identifier naturalproductmech:mibig-fb29c28c86; full key DYVDEFLXDOLVQF-HOTGVXAUSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| support-2277-companion-8 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/19 | supports | Complete admitted companion raw/history and saved source context: compound 6; identifier naturalproductmech:mibig-c9721b757b; full key LMSXLLMHAAGBSJ-UHFFFAOYSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| support-2277-companion-9 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/22 | supports | Complete admitted companion raw/history and saved source context: eutypinic acid; identifier naturalproductmech:mibig-a75acad16f; full key HFSFSKBQIGXUEY-UHFFFAOYSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| support-2277-companion-10 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /raw_unselected_companions/24 | supports | Complete admitted companion raw/history and saved source context: pestalodiol E; identifier naturalproductmech:mibig-2b8aee01b5; full key XLJZQTJROGTDLX-UHFFFAOYSA-N; owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-228/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-228/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-228/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-228/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-228/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- FullQC and full OAK were unavailable; five accepted local commands do not establish scientific completeness.
- No external retrieval or live identifier, taxonomy, protein or publication request was performed. These assessments use original saved owner-form computations; no additional molecular or YAML parses occurred during fragment authoring.
- Two undefined-stereo warnings belong to the original global diagnostic stream and cannot be assigned to this owner. Stored agreement does not establish natural identity, primary evidence or complete natural stereochemistry.
- Retained grades, cached taxonomy, citations and versioned predictions preserve their own scopes; publication independence was not established.
- No scientific source record or curation history was edited. Canonical persistence and campaign operations remain ROOT-owned.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Selected mechanism scope is complete as admitted; companion graphs and assays are not transferred to this owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T185022Z-biscognienyne-b
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: biscognienyne B'
started_at: '2026-11-03T18:10:20.616322Z'
finished_at: '2026-11-03T18:50:22.012199Z'
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
summary: 'biscognienyne B: stored forms and retained source scope are coherent within
  admitted local evidence. No selected mechanism reader applies; source, occurrence
  and prediction limits remain explicit. Qualified partial review with no new supported
  finding.'
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/3-4-dihydroxy-5-polyprenylbenzoic-acid.yaml
    sha256: 81e523462ebb0540e1de3b9eb19f88bc87266f0c7a4dcabbacae3556ccbdb91d
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/4-hydroxy-3-prenylbenzoic-acid.yaml
    sha256: 7ea7276c7e9cd0e4510ea28aa8076911d173a70ec9b80bd3ae7803749a5b53de
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml
    sha256: 5b2493967d1774d28d023edd8500fbf16a14cfbe5139e0ff65abb0d471302e56
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/compound-8.yaml
    sha256: 996d80d8c8f8eb32b5ee5a074da9d5390601d56585fbacde28b84e3315a246c9
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/prenylhydroquinone.yaml
    sha256: 9e180def1be87dc17c2f604712ad8ce85162e4fb8ef3af415887e619dc1dd6ac
    role: context
  - path: data/natural_products/terpenoids/biscognienyne-b.yaml
    sha256: ed9704a4411299b7c325c3ed9017a2aeabe6cfcb5600f5a13d923adc8361e3df
    role: target
  - path: data/natural_products/terpenoids/compound-11.yaml
    sha256: c6b1144ed2ccd49b3eb15d81e70c396bee614094e11074ed50076687ec64a29a
    role: context
  - path: data/natural_products/terpenoids/compound-12.yaml
    sha256: 68523e625132f3a958ba5ad4f2bad5984bfbc7d33f8a0f73e46e9ec109b21fd9
    role: context
  - path: data/natural_products/terpenoids/compound-15.yaml
    sha256: 86ed50b1cb3aeb1170f1e40e4c1d365b90cf94937cb27d36376882cda4b327ce
    role: context
  - path: data/natural_products/terpenoids/compound-6.yaml
    sha256: 4db168bf9a510a55403f4087abc00f8eee30b59a886a13a49daa8322eaa3b5cd
    role: context
  - path: data/natural_products/terpenoids/eutypinic-acid.yaml
    sha256: a2fbde14564e24a58cdf68e5c5b12fca09bb50874a8708eaf2904e684cfc6158
    role: context
  - path: data/natural_products/terpenoids/pestalodiol-e.yaml
    sha256: 6ee7a6ba26b1c13ea95adc492d1e200f9aefc45e3f700b3c53608e5960fc4e0b
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
  selection: Campaign path order 2277; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:167050
targets:
- target_id: CHEBI:167050
  path: data/natural_products/terpenoids/biscognienyne-b.yaml
  label: biscognienyne B
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
  - CHEBI:167050
  command: just validate-strict data/natural_products/terpenoids/aspterric-acid.yaml
    data/natural_products/terpenoids/astaxanthin.yaml data/natural_products/terpenoids/astellolide-a.yaml
    data/natural_products/terpenoids/avermitilol.yaml data/natural_products/terpenoids/betaestacin-i.yaml
    data/natural_products/terpenoids/betaestacin-ii.yaml data/natural_products/terpenoids/biscognienyne-b.yaml
    data/natural_products/terpenoids/botrydial.yaml data/natural_products/terpenoids/botrydienal.yaml
    data/natural_products/terpenoids/botryenalol.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-228/validate-strict-selected10-001.tsv
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
  - CHEBI:167050
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-228/validate-all-001.tsv
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
  - CHEBI:167050
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
  - CHEBI:167050
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
  - CHEBI:167050
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-228/review-queue-001.tsv
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
  - CHEBI:167050
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:167050
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:167050
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2277-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/biscognienyne-b.yaml
  locator: lines 1–115
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: Whole current plaintext owner and all 3 history events; literal identifier
    CHEBI:167050, label biscognienyne B, full key UAAPCPSYCUMTPM-LVQVYYBASA-N. Historical
    annotations remain retained claims.
  snapshot_sha256: ed9704a4411299b7c325c3ed9017a2aeabe6cfcb5600f5a13d923adc8361e3df
- evidence_id: support-2277-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/6/owner_document; /records/6/owner_pin
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: Complete captured owner, including all written identity, source, occurrence,
    classification, mechanism and history fields that are present.
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: support-2277-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: Complete admitted selected context, all nine query frames/full payloads,
    direct companions and 48 planned inputs; source-scope authority is not proof of
    scientific correctness.
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/intakes/2277-inspect-001.json
  locator: /targets; /source; /status
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: Complete actual canonical intake target list, source-input ownership and
    inspection-only status.
  snapshot_sha256: 26906402fbc576ed3f148045d5e324a523b5008d6bd61d125425eddf24b3cdc7
- evidence_id: support-2277-intake-ready
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-intake-ready-001.json
  locator: /status; /accepted; /intake_summary; /verification; /limits
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: ROOT acceptance of the original actual intakes and exact current input
    maps, retaining limits.
  snapshot_sha256: c2c258d6da649f48e76d7d8994bfdef5dd2afa511e1762a008b8f65ef40f8501
- evidence_id: support-2277-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-input-plan-acceptance-001.json
  locator: /status; /accepted; /plan; /source_notes; /per_order_counts; /source_placements;
    /unique_source_paths
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: ROOT acceptance of the original composition and complete input maps.
  snapshot_sha256: 006b60c3550a7c223f1a10b5a127034d9429c714d72ff96363275b808fe1a2d6
- evidence_id: support-2277-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-scope-notes-001.json
  locator: /observer; /recorded_at; /batch; /status; /inventory; /inventory_ROOT_acceptance;
    /inventory_ROOT_acceptance_inventory_key; /collector_source; /collector_source_adoption;
    /collector_original_tools; /collector_original_terminal; /prior_final_acceptance;
    /prior_final_expected_status; /accepted_prior_remaining; /frozen_remaining; /actual_frozen228_remaining;
    /requirements; /selected_profile; /totals; /per_order_input_counts; /reading;
    /curation; /cautions; /current_inventory_input_pin_count; /future_actual_roles;
    /independent_actual_selection_capture_authority; /scientific_verdicts; /external_requests;
    /source_records_modified; /target_invocations_by_this_step
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: Complete source-reading attribution and bounded curation scan, with source
    grades, cached taxonomy and historical limits; not a new primary observation.
  snapshot_sha256: 63a4685a365402d997d4f20d1b80d7dce1b7f62d2d2264c93dae7fa581e52df5
- evidence_id: support-2277-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/declared_structure; /records/6/smiles/computed; /records/6/inchi/computed;
    /records/6/comparisons; /records/6/atom_correspondence
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Original saved paired computations: all ten comparison flags are true
    and both forms retain the declared full key; atom correspondence explicitly does
    not establish full graph identity. No experimental identity conclusion follows.'
  snapshot_sha256: d4c6eb70f0eb830267ca6a459d5b3f2f1ed0903dbbd02a6ea6cea1104beb62f9
- evidence_id: support-2277-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed; /records/6/inchi/computed
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: Complete computed tables show an epoxide fused to a six-carbon ring, two
    hydroxyls, one alkyne and three alkenes, with no carbonyl; the sole C–O–C bridge
    is the epoxide. All atom, bond, ring, stereo and motif fields were read.
  snapshot_sha256: d4c6eb70f0eb830267ca6a459d5b3f2f1ed0903dbbd02a6ea6cea1104beb62f9
- evidence_id: support-2277-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-local-diagnostics-acceptance-001.json
  locator: /observer; /observed_at; /status; /accepted; /DATA; /execution; /original_tools;
    /source_adoption; /runtime_authorization; /intake_ready; /original_terminal; /verification;
    /unspecified_stereo; /ROOT_reading; /limits; /external_requests; /target_invocations_by_this_acceptance
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: ROOT acceptance of the original 20-form diagnostic and current inputs;
    two original undefined-stereo warnings remain global and unassigned.
  snapshot_sha256: 538d4571fceb926adea82c64cc91c2cb0d058ceb5018e3d3261297b43223fcf8
- evidence_id: support-2277-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-native-five-gates-acceptance-001.json
  locator: /observer; /recorded_at; /batch; /status; /execution; /original_tools;
    /native_saved_readback; /source_adoption; /selection_authority; /original_terminal;
    /five_exits; /strict_selected_records; /strict_full_records; /validation_error_rows;
    /lock_records; /reproduced_byte_identical_records; /queue_rows; /queue_groups;
    /selected_queue_rows; /root_reading; /queue_complete_byte_proof_attribution; /all_current_pins_checked;
    /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /observer_correction; /external_requests; /target_reexecutions; /record_or_LIVE_changes
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: ROOT acceptance of five original local gates; FullQC and full OAK remain
    unavailable.
  snapshot_sha256: 46a484e5df5e5ff5b717dd9fbef5c00cc5bc1843abdf9cab2629b498187c780a
- evidence_id: support-2277-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N;
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: lines 2771–2771
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete physical TSV payload decoded without changing blank fields: {"mibig_accession":"BGC0002290","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"biscognienyne
    B","compound_index":"1","smiles":"CC(=CC[C@@]12[C@@H](O1)[C@@H](C=C([C@H]2O)C#CC(=C)C)O)C","standard_inchi":"InChI=1S/C16H20O3/c1-10(2)5-6-12-9-13(17)15-16(19-15,14(12)18)8-7-11(3)4/h7,9,13-15,17-18H,1,8H2,2-4H3/t13-,14-,15+,16-/m1/s1","standard_inchi_key":"UAAPCPSYCUMTPM-LVQVYYBASA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA023808","taxon_id":"NCBITaxon:1896107","taxon_label":"Biscogniauxia
    sp.","bgc_classes":"other","bgc_subclasses":"other","genome_accession":"MT109335.1","locus_from":"1","locus_to":"37984","locus_evidence_methods":"Heterologous
    expression","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:32364293","reference_basis":"ENTRY"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2277-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N;
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-row-chebi_structures-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: lines 43315–43315
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete physical TSV payload decoded without changing blank fields: {"chebi_id":"CHEBI:167050","name":"biscognienyne
    B","definition":"A member of the class of epoxides that is (1R,6S)-7-oxabicyclo[4.1.0]hept-3-ene
    substituted by 3-methylbut-2-en-1-yl, hydroxy, 2-methylbut-1-en-3-yn-4-yl, and
    hydroxy groups at positions 1, 2R, 3 and 5R. It is a meroterpenoid natural product
    synthesized by the Ascomycota fungus Biscogniauxia sp.","stars":"3","standard_inchi_key":"UAAPCPSYCUMTPM-LVQVYYBASA-N","smiles":"C=C(C)C#CC1=C[C@@H](O)[C@@H]2O[C@]2(CC=C(C)C)[C@@H]1O"}'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: support-2277-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N;
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: lines 8594–8594
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete physical TSV payload decoded without changing blank fields: {"standard_inchi_key":"UAAPCPSYCUMTPM-LVQVYYBASA-N","organism_name":"Biscogniauxia","taxon_id":"NCBITaxon:97376","organism_wikidata":"http://www.wikidata.org/entity/Q2153376","reference_doi":"10.1021/ACS.ORGLETT.6B03264","structure_wikidata":"http://www.wikidata.org/entity/Q105268528"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2277-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N;
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N;
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: lines 2361–2361
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete physical TSV payload decoded without changing blank fields: {"standard_inchi_key":"UAAPCPSYCUMTPM-LVQVYYBASA-N","smiles":"CC(=CC[C@@]12[C@@H](O1)[C@@H](C=C([C@H]2O)C#CC(=C)C)O)C","pathway_results":"Terpenoids","superclass_results":"Meroterpenoids","class_results":"Miscellaneous
    meroterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2277-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N;
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N;
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query=UAAPCPSYCUMTPM-LVQVYYBASA-N;
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Saved frame: predicate=exact chebi_id from exact full-key structure rows;
    query=[''CHEBI:167050'']; positive placements=1. Zero matches are bounded to this
    snapshot.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-row-chebi_origins-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: lines 17153–17153
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete physical TSV payload decoded without changing blank fields: {"chebi_id":"CHEBI:167050","species_text":"Biscogniauxia
    sp.","species_accession":"1896107","component_text":"","strain_text":"71-10-1-1","source_accession":"32364293","comments":"GenBank:
    MT109335.1"}'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: support-2277-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/matched_chebi_ids; /records/6/source_scope_inventory/source_taxa;
    /records/6/source_scope_inventory/forward_taxon_merge_matches; /records/6/source_scope_inventory/nonorganism_matches;
    /records/6/source_scope_inventory/actual_assay_rows; /records/6/source_scope_inventory/blank_AID_sentinels;
    /records/6/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete saved non-query route fields: {"matched_chebi_ids":["CHEBI:167050"],"source_taxa":["NCBITaxon:1896107","NCBITaxon:97376"],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"actual_assay_rows":[],"blank_AID_sentinels":[],"related_corpus_rows":[]}'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-cache-1896107
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/69
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete cached stanza with literal names/synonyms and local scope: [Term]

    id: NCBITaxon:1896107

    name: Biscogniauxia sp.


    '
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: support-2277-cache-97376
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/26
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete cached stanza with literal names/synonyms and local scope: [Term]

    id: NCBITaxon:97376

    name: Biscogniauxia


    '
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: support-2277-companions
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/6/proposed_companion_paths; /records/6/direct_companion_predicates
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: Exact 11 direct companions and predicates establish comparison scope, not
    transferable assays or mechanisms.
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/0
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: 3,4-dihydroxy-5-polyprenylbenzoic
    acid; identifier CHEBI:64921; full key NMAKQSXJWYBYRF-UHFFFAOYSA-N; owned BGCs
    ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-1
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/1
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: 4-hydroxy-3-prenylbenzoic
    acid; identifier naturalproductmech:mibig-b4ad51fa2f; full key LBSJJNAMGVDGCU-UHFFFAOYSA-N;
    owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-2
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/2
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: compound
    7; identifier naturalproductmech:mibig-92c7bb9c67; full key ITBNIRGMDWCANJ-UHFFFAOYSA-N;
    owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-3
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/3
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: compound
    8; identifier naturalproductmech:mibig-007406ddf9; full key HHJKLMAAAQXSLU-UHFFFAOYSA-N;
    owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-4
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/4
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: prenylhydroquinone;
    identifier naturalproductmech:mibig-8029a6a4d2; full key RPIWRSVHAHNACM-UHFFFAOYSA-N;
    owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-5
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/16
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: compound
    11; identifier naturalproductmech:mibig-21c4af6890; full key XRWGLEWIDBKJHA-UHFFFAOYSA-N;
    owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-6
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/17
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: compound
    12; identifier naturalproductmech:mibig-5cc4b239f3; full key IAAUFTNAVRJTIR-UHFFFAOYSA-N;
    owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-7
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/18
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: compound
    15; identifier naturalproductmech:mibig-fb29c28c86; full key DYVDEFLXDOLVQF-HOTGVXAUSA-N;
    owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-8
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/19
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: compound
    6; identifier naturalproductmech:mibig-c9721b757b; full key LMSXLLMHAAGBSJ-UHFFFAOYSA-N;
    owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-9
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/22
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: eutypinic
    acid; identifier naturalproductmech:mibig-a75acad16f; full key HFSFSKBQIGXUEY-UHFFFAOYSA-N;
    owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: support-2277-companion-10
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /raw_unselected_companions/24
  accessed_at: '2026-11-03T18:41:00.134730Z'
  support: supports
  summary: 'Complete admitted companion raw/history and saved source context: pestalodiol
    E; identifier naturalproductmech:mibig-2b8aee01b5; full key XLJZQTJROGTDLX-UHFFFAOYSA-N;
    owned BGCs ["BGC0002290"]. No selected claim is inferred from this relationship.'
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:12:47.775053Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: c21e163f3196cf186958794725f1b00a467ef5cca041142eb77868d0f57002a8
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:13:12.316523Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 87b8d13781a6e8b29a6548c0231420c70cfb7201c9942069049f0adfaa3a91dc
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:13:32.394271Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:14:07.640893Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:14:19.806834Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 8a9b4b2d4725b4513fcae189afd5e5e6f81b1ec228cdd2b2b100ff2dd2472a63
assessments:
- assessment_id: support-2277-A1
  area: identity
  topic: Exact structure concept and grounding
  outcome: supported
  summary: The EXACT CHEBI:167050 owner retains full key UAAPCPSYCUMTPM-LVQVYYBASA-N,
    matching the admitted exact-key ChEBI row. MIBiG BGC0002290 version 2 records
    source compound_index=1. Its eleven admitted BGC companions retain distinct identifiers
    and structures rather than becoming Biscognienyne B synonyms.
  target_ids:
  - CHEBI:167050
  evidence_ids:
  - support-2277-owner
  - support-2277-capture
  - support-2277-source-plan
  - support-2277-query-mibig_compounds
  - support-2277-query-chebi_structures
  - support-2277-row-mibig_compounds-0
  - support-2277-row-chebi_structures-0
  - support-2277-companions
  - support-2277-companion-0
  - support-2277-companion-1
  - support-2277-companion-2
  - support-2277-companion-3
  - support-2277-companion-4
  - support-2277-companion-5
  - support-2277-companion-6
  - support-2277-companion-7
  - support-2277-companion-8
  - support-2277-companion-9
  - support-2277-companion-10
  dimensions:
  - name: standard_inchi_key
    value: UAAPCPSYCUMTPM-LVQVYYBASA-N
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-owner
    - support-2277-capture
    - support-2277-source-plan
    - support-2277-query-mibig_compounds
    - support-2277-query-chebi_structures
    - support-2277-row-mibig_compounds-0
    - support-2277-row-chebi_structures-0
    - support-2277-companions
    - support-2277-companion-0
    - support-2277-companion-1
    - support-2277-companion-2
    - support-2277-companion-3
    - support-2277-companion-4
    - support-2277-companion-5
    - support-2277-companion-6
    - support-2277-companion-7
    - support-2277-companion-8
    - support-2277-companion-9
    - support-2277-companion-10
  - name: grounding_scope
    value: The EXACT CHEBI:167050 owner retains full key UAAPCPSYCUMTPM-LVQVYYBASA-N,
      matching the admitted exact-key ChEBI row. MIBiG BGC0002290 version 2 records
      source compound_index=1. Its eleven admitted BGC companions retain distinct
      identifiers and structures rather than becoming Biscognienyne B synonyms.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-owner
    - support-2277-capture
    - support-2277-source-plan
    - support-2277-query-mibig_compounds
    - support-2277-query-chebi_structures
    - support-2277-row-mibig_compounds-0
    - support-2277-row-chebi_structures-0
    - support-2277-companions
    - support-2277-companion-0
    - support-2277-companion-1
    - support-2277-companion-2
    - support-2277-companion-3
    - support-2277-companion-4
    - support-2277-companion-5
    - support-2277-companion-6
    - support-2277-companion-7
    - support-2277-companion-8
    - support-2277-companion-9
    - support-2277-companion-10
- assessment_id: support-2277-A2
  area: representation
  topic: Stored representation and stereochemistry
  outcome: supported
  summary: 'Both saved forms agree in neutral formula C16H20O3, standard InChI, full
    key and both canonical SMILES strings, with 19 atoms and 20 bonds. Four tetrahedral
    centres are specified in the SMILES table: 4 R, 5 S, 7 R and 10 R. The complete
    graph has a fused epoxide/carbocycle, two hydroxyls, one alkyne and three alkenes;
    no additional unresolved potential E/Z entry is listed. Stored matching and representation
    equality do not independently establish experimental stereochemistry or natural
    identity.'
  target_ids:
  - CHEBI:167050
  evidence_ids:
  - support-2277-owner
  - support-2277-capture
  - support-2277-chemistry
  - support-2277-topology
  - support-2277-diagnostic-acceptance
  dimensions:
  - name: stereochemical_resolution
    value: 'Both saved forms agree in neutral formula C16H20O3, standard InChI, full
      key and both canonical SMILES strings, with 19 atoms and 20 bonds. Four tetrahedral
      centres are specified in the SMILES table: 4 R, 5 S, 7 R and 10 R. The complete
      graph has a fused epoxide/carbocycle, two hydroxyls, one alkyne and three alkenes;
      no additional unresolved potential E/Z entry is listed. Stored matching and
      representation equality do not independently establish experimental stereochemistry
      or natural identity.'
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-owner
    - support-2277-capture
    - support-2277-chemistry
    - support-2277-topology
    - support-2277-diagnostic-acceptance
  - name: representation_correspondence
    value: 'Both saved forms agree in neutral formula C16H20O3, standard InChI, full
      key and both canonical SMILES strings, with 19 atoms and 20 bonds. Four tetrahedral
      centres are specified in the SMILES table: 4 R, 5 S, 7 R and 10 R. The complete
      graph has a fused epoxide/carbocycle, two hydroxyls, one alkyne and three alkenes;
      no additional unresolved potential E/Z entry is listed. Stored matching and
      representation equality do not independently establish experimental stereochemistry
      or natural identity.'
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-owner
    - support-2277-capture
    - support-2277-chemistry
    - support-2277-topology
    - support-2277-diagnostic-acceptance
- assessment_id: support-2277-A3
  area: provenance
  topic: Producer, locus, taxon and strain roles
  outcome: supported
  summary: MIBiG asserts Biscogniauxia sp., NCBITaxon:1896107, as producer with SOURCE_ASSERTION.
    Heterologous expression supports CLUSTER_DEMONSTRATED for BGC0002290 and MT109335.1:1–37984,
    with retained OTHER BGC class. The entry remains active/questionable/unknown.
    ChEBI origin adds strain/detection context 71-10-1-1, while LOTUS uses the broader
    genus NCBITaxon:97376. These taxon and strain scopes remain distinct.
  target_ids:
  - CHEBI:167050
  evidence_ids:
  - support-2277-capture
  - support-2277-source-plan
  - support-2277-row-mibig_compounds-0
  - support-2277-row-chebi_origins-0
  - support-2277-row-lotus_occurrences-0
  - support-2277-routes
  - support-2277-cache-1896107
  - support-2277-cache-97376
  - support-2277-source-notes
  dimensions:
  - name: taxon_and_strain_scope
    value: MIBiG asserts Biscogniauxia sp., NCBITaxon:1896107, as producer with SOURCE_ASSERTION.
      Heterologous expression supports CLUSTER_DEMONSTRATED for BGC0002290 and MT109335.1:1–37984,
      with retained OTHER BGC class. The entry remains active/questionable/unknown.
      ChEBI origin adds strain/detection context 71-10-1-1, while LOTUS uses the broader
      genus NCBITaxon:97376. These taxon and strain scopes remain distinct.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-capture
    - support-2277-source-plan
    - support-2277-row-mibig_compounds-0
    - support-2277-row-chebi_origins-0
    - support-2277-row-lotus_occurrences-0
    - support-2277-routes
    - support-2277-cache-1896107
    - support-2277-cache-97376
    - support-2277-source-notes
  - name: producer_evidence_tier
    value: MIBiG asserts Biscogniauxia sp., NCBITaxon:1896107, as producer with SOURCE_ASSERTION.
      Heterologous expression supports CLUSTER_DEMONSTRATED for BGC0002290 and MT109335.1:1–37984,
      with retained OTHER BGC class. The entry remains active/questionable/unknown.
      ChEBI origin adds strain/detection context 71-10-1-1, while LOTUS uses the broader
      genus NCBITaxon:97376. These taxon and strain scopes remain distinct.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-capture
    - support-2277-source-plan
    - support-2277-row-mibig_compounds-0
    - support-2277-row-chebi_origins-0
    - support-2277-row-lotus_occurrences-0
    - support-2277-routes
    - support-2277-cache-1896107
    - support-2277-cache-97376
    - support-2277-source-notes
  - name: locus_evidence_tier
    value: MIBiG asserts Biscogniauxia sp., NCBITaxon:1896107, as producer with SOURCE_ASSERTION.
      Heterologous expression supports CLUSTER_DEMONSTRATED for BGC0002290 and MT109335.1:1–37984,
      with retained OTHER BGC class. The entry remains active/questionable/unknown.
      ChEBI origin adds strain/detection context 71-10-1-1, while LOTUS uses the broader
      genus NCBITaxon:97376. These taxon and strain scopes remain distinct.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-capture
    - support-2277-source-plan
    - support-2277-row-mibig_compounds-0
    - support-2277-row-chebi_origins-0
    - support-2277-row-lotus_occurrences-0
    - support-2277-routes
    - support-2277-cache-1896107
    - support-2277-cache-97376
    - support-2277-source-notes
- assessment_id: support-2277-A4
  area: evidence
  topic: Citation placement and primary-source limits
  outcome: supported
  summary: PMID:32364293 is the MIBiG ENTRY citation and the ChEBI-origin citation,
    so their placements do not establish independent publications. LOTUS cites DOI:10.1021/ACS.ORGLETT.6B03264.
    Among direct BGC2290 companions, Compound 15 has its own COMPOUND_BIOACTIVITY
    citation role; not every companion citation has the selected ENTRY role. No paper
    or experimental construct was freshly verified.
  target_ids:
  - CHEBI:167050
  evidence_ids:
  - support-2277-capture
  - support-2277-source-plan
  - support-2277-row-mibig_compounds-0
  - support-2277-row-chebi_structures-0
  - support-2277-row-lotus_occurrences-0
  - support-2277-row-npclassifier-0
  - support-2277-row-chebi_origins-0
  - support-2277-companions
  - support-2277-companion-0
  - support-2277-companion-1
  - support-2277-companion-2
  - support-2277-companion-3
  - support-2277-companion-4
  - support-2277-companion-5
  - support-2277-companion-6
  - support-2277-companion-7
  - support-2277-companion-8
  - support-2277-companion-9
  - support-2277-companion-10
  - support-2277-source-notes
  dimensions:
  - name: citation_scope
    value: PMID:32364293 is the MIBiG ENTRY citation and the ChEBI-origin citation,
      so their placements do not establish independent publications. LOTUS cites DOI:10.1021/ACS.ORGLETT.6B03264.
      Among direct BGC2290 companions, Compound 15 has its own COMPOUND_BIOACTIVITY
      citation role; not every companion citation has the selected ENTRY role. No
      paper or experimental construct was freshly verified.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-capture
    - support-2277-source-plan
    - support-2277-row-mibig_compounds-0
    - support-2277-row-chebi_structures-0
    - support-2277-row-lotus_occurrences-0
    - support-2277-row-npclassifier-0
    - support-2277-row-chebi_origins-0
    - support-2277-companions
    - support-2277-companion-0
    - support-2277-companion-1
    - support-2277-companion-2
    - support-2277-companion-3
    - support-2277-companion-4
    - support-2277-companion-5
    - support-2277-companion-6
    - support-2277-companion-7
    - support-2277-companion-8
    - support-2277-companion-9
    - support-2277-companion-10
    - support-2277-source-notes
- assessment_id: support-2277-A5
  area: scope
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: 'Two occurrences are written: a LOTUS genus-level Biscogniauxia assertion
    and a ChEBI Biscogniauxia sp. origin with strain context 71-10-1-1. Occurrence
    remains distinct from production even when citations/taxa overlap. Saved PubChem,
    BindingDB and AntibioticMech routes have no selected-owner assay payload. This
    bounded absence does not imply inactivity or authorize transfer from the eleven
    companions.'
  target_ids:
  - CHEBI:167050
  evidence_ids:
  - support-2277-capture
  - support-2277-source-plan
  - support-2277-query-mibig_compounds
  - support-2277-query-chebi_structures
  - support-2277-query-lotus_occurrences
  - support-2277-query-cyanometdb_occurrences
  - support-2277-query-npclassifier
  - support-2277-query-pubchem_bioassay
  - support-2277-query-bindingdb_targets
  - support-2277-query-antibioticmech_inchikeys
  - support-2277-query-chebi_origins
  - support-2277-row-mibig_compounds-0
  - support-2277-row-chebi_structures-0
  - support-2277-row-lotus_occurrences-0
  - support-2277-row-npclassifier-0
  - support-2277-row-chebi_origins-0
  - support-2277-routes
  - support-2277-cache-1896107
  - support-2277-cache-97376
  - support-2277-companions
  - support-2277-companion-0
  - support-2277-companion-1
  - support-2277-companion-2
  - support-2277-companion-3
  - support-2277-companion-4
  - support-2277-companion-5
  - support-2277-companion-6
  - support-2277-companion-7
  - support-2277-companion-8
  - support-2277-companion-9
  - support-2277-companion-10
  dimensions:
  - name: occurrence_scope
    value: 'Two occurrences are written: a LOTUS genus-level Biscogniauxia assertion
      and a ChEBI Biscogniauxia sp. origin with strain context 71-10-1-1. Occurrence
      remains distinct from production even when citations/taxa overlap. Saved PubChem,
      BindingDB and AntibioticMech routes have no selected-owner assay payload. This
      bounded absence does not imply inactivity or authorize transfer from the eleven
      companions.'
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-capture
    - support-2277-source-plan
    - support-2277-query-mibig_compounds
    - support-2277-query-chebi_structures
    - support-2277-query-lotus_occurrences
    - support-2277-query-cyanometdb_occurrences
    - support-2277-query-npclassifier
    - support-2277-query-pubchem_bioassay
    - support-2277-query-bindingdb_targets
    - support-2277-query-antibioticmech_inchikeys
    - support-2277-query-chebi_origins
    - support-2277-row-mibig_compounds-0
    - support-2277-row-chebi_structures-0
    - support-2277-row-lotus_occurrences-0
    - support-2277-row-npclassifier-0
    - support-2277-row-chebi_origins-0
    - support-2277-routes
    - support-2277-cache-1896107
    - support-2277-cache-97376
    - support-2277-companions
    - support-2277-companion-0
    - support-2277-companion-1
    - support-2277-companion-2
    - support-2277-companion-3
    - support-2277-companion-4
    - support-2277-companion-5
    - support-2277-companion-6
    - support-2277-companion-7
    - support-2277-companion-8
    - support-2277-companion-9
    - support-2277-companion-10
  - name: assay_scope
    value: 'Two occurrences are written: a LOTUS genus-level Biscogniauxia assertion
      and a ChEBI Biscogniauxia sp. origin with strain context 71-10-1-1. Occurrence
      remains distinct from production even when citations/taxa overlap. Saved PubChem,
      BindingDB and AntibioticMech routes have no selected-owner assay payload. This
      bounded absence does not imply inactivity or authorize transfer from the eleven
      companions.'
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-capture
    - support-2277-source-plan
    - support-2277-query-mibig_compounds
    - support-2277-query-chebi_structures
    - support-2277-query-lotus_occurrences
    - support-2277-query-cyanometdb_occurrences
    - support-2277-query-npclassifier
    - support-2277-query-pubchem_bioassay
    - support-2277-query-bindingdb_targets
    - support-2277-query-antibioticmech_inchikeys
    - support-2277-query-chebi_origins
    - support-2277-row-mibig_compounds-0
    - support-2277-row-chebi_structures-0
    - support-2277-row-lotus_occurrences-0
    - support-2277-row-npclassifier-0
    - support-2277-row-chebi_origins-0
    - support-2277-routes
    - support-2277-cache-1896107
    - support-2277-cache-97376
    - support-2277-companions
    - support-2277-companion-0
    - support-2277-companion-1
    - support-2277-companion-2
    - support-2277-companion-3
    - support-2277-companion-4
    - support-2277-companion-5
    - support-2277-companion-6
    - support-2277-companion-7
    - support-2277-companion-8
    - support-2277-companion-9
    - support-2277-companion-10
- assessment_id: support-2277-A6
  area: other
  topic: Computed classification and complete saved topology
  outcome: supported
  summary: NPClassifier retains Terpenoids / Meroterpenoids / Miscellaneous meroterpenoids
    with is_glycoside=false. The complete topology has a three-member epoxide fused
    to a six-carbon ring, two hydroxyls, an alkyne and alkenes, with no carbonyl.
    Its sole C–O–C bridge is the epoxide, not a glycosidic linkage. The retained ChEBI
    epoxide definition and computed meroterpenoid class are structurally compatible
    within this limited review; biosynthetic origin was not independently proved.
  target_ids:
  - CHEBI:167050
  evidence_ids:
  - support-2277-capture
  - support-2277-row-npclassifier-0
  - support-2277-chemistry
  - support-2277-topology
  - support-2277-row-chebi_structures-0
  dimensions:
  - name: computed_classification
    value: NPClassifier retains Terpenoids / Meroterpenoids / Miscellaneous meroterpenoids
      with is_glycoside=false. The complete topology has a three-member epoxide fused
      to a six-carbon ring, two hydroxyls, an alkyne and alkenes, with no carbonyl.
      Its sole C–O–C bridge is the epoxide, not a glycosidic linkage. The retained
      ChEBI epoxide definition and computed meroterpenoid class are structurally compatible
      within this limited review; biosynthetic origin was not independently proved.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-capture
    - support-2277-row-npclassifier-0
    - support-2277-chemistry
    - support-2277-topology
    - support-2277-row-chebi_structures-0
- assessment_id: support-2277-A7
  area: completeness
  topic: Review completion and unavailable verification
  outcome: unknown
  summary: The complete owner, actual 48-input intake, all nine source frames and
    five positive rows, applicable cached taxa, eleven direct companions and both
    saved forms were reviewed. No selected graph, pathway, target or component is
    declared. Local checks and chemistry are accepted; FullQC, full OAK and primary/identifier
    verification remain unavailable. This is a qualified partial review.
  target_ids:
  - CHEBI:167050
  evidence_ids:
  - support-2277-owner
  - support-2277-capture
  - support-2277-source-plan
  - support-2277-intake
  - support-2277-intake-ready
  - support-2277-plan-acceptance
  - support-2277-source-notes
  - support-2277-chemistry
  - support-2277-diagnostic-acceptance
  - support-2277-native-acceptance
  dimensions:
  - name: review_completion
    value: The complete owner, actual 48-input intake, all nine source frames and
      five positive rows, applicable cached taxa, eleven direct companions and both
      saved forms were reviewed. No selected graph, pathway, target or component is
      declared. Local checks and chemistry are accepted; FullQC, full OAK and primary/identifier
      verification remain unavailable. This is a qualified partial review.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2277-owner
    - support-2277-capture
    - support-2277-source-plan
    - support-2277-intake
    - support-2277-intake-ready
    - support-2277-plan-acceptance
    - support-2277-source-notes
    - support-2277-chemistry
    - support-2277-diagnostic-acceptance
    - support-2277-native-acceptance
findings: []
actions: []
limitations:
- FullQC and full OAK were unavailable; five accepted local commands do not establish
  scientific completeness.
- No external retrieval or live identifier, taxonomy, protein or publication request
  was performed. These assessments use original saved owner-form computations; no
  additional molecular or YAML parses occurred during fragment authoring.
- Two undefined-stereo warnings belong to the original global diagnostic stream and
  cannot be assigned to this owner. Stored agreement does not establish natural identity,
  primary evidence or complete natural stereochemistry.
- Retained grades, cached taxonomy, citations and versioned predictions preserve their
  own scopes; publication independence was not established.
- No scientific source record or curation history was edited. Canonical persistence
  and campaign operations remain ROOT-owned.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Selected mechanism scope is complete as admitted; companion graphs and assays are
  not transferred to this owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-228
```
