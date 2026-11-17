# Local evidence review: (−)-δ-cadinene

- Review: 20261103T194802Z-cadinene
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T19:22:18.979539Z
- Finished UTC: 2026-11-03T19:48:02.624284Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified partial review of the retained CHEBI:63703 Cadinene form, preserving encoded stereochemistry, unverified optical sign, source-only production and the exact historical liverwort taxon merge.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2289; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:63703 | data/natural_products/terpenoids/cadinene.yaml | generated | (−)-δ-cadinene |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:63703 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:63703 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:63703 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:63703 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:63703 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:63703 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:63703 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:63703 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding

identity: supported. Targets: CHEBI:63703.

The owner is exactly grounded to retained three-star CHEBI:63703 with full key FUCYIEXQVQJBKY-UKRRQHHQSA-N, while its chemical strings come from MIBiG BGC0000674 version 5, source compound_index=1. The saved ChEBI row has that same complete key and supplies the definition and Unicode-minus label; the ASCII-minus MIBiG synonym remains attributed. This supports the local exact-structure join. The source optical-sign label and PubChem cross-reference are not independently verified physical measurements or freshly resolved identities.

### Stored representation and stereochemistry

representation: supported. Targets: CHEBI:63703.

Both stored forms agree on neutral C15H24, 15 atoms, 16 bonds, Standard InChI/key and both canonical SMILES comparisons. The complete graph has two six-membered carbon rings and two ring double bonds, with two specified tetrahedral centres: SMILES C4 R and C3 S, corresponding to InChI C12 R and C14 S. Their connectivity is compatible with the retained ChEBI 1R,8aS definition and its adjacent isopropyl/bridgehead relation. The cis wording remains the retained source stereochemical description; no independent experimental relative-configuration determination is claimed. Optical rotation sign cannot be inferred solely from CIP assignments, and no rotation measurement was inspected. The source stereo_complete flag is bounded to the encoded assignments.

### Producer, locus, taxon and strain roles

provenance: supported. Targets: CHEBI:63703.

MIBiG asserts Streptomyces clavuligerus ATCC 27064 with SOURCE_ASSERTION and taxon NCBITaxon:1901, whose cached stanza is species-level. The strain qualifier is preserved without claiming independent strain resolution. BGC0000674 version 5 is active/questionable/unknown, DS570637.1:74962–79952, with no locus method and CLUSTER_UNSTATED. The source taxon and locus grades remain separate from occurrence evidence. The retained 53029→2729092 route reconciles historical Preissia quadrata to cached Marchantia quadrata locally; it does not authorize a new taxonomy claim beyond this snapshot.

### Citation placement and primary-source limits

evidence: supported. Targets: CHEBI:63703.

PMID:21276937 has MIBiG ENTRY scope. The ChEBI definition is attributed to CHEBI:63703; LOTUS retains DOI:10.1016/J.CHEMBIOL.2010.11.008, DOI:10.1016/0031-9422(96)00354-8 and DOI:10.1021/JF60200A011. The same liverwort DOI appears under two raw taxon names and is not two independently established experiments. Primary text, optical rotation, source stereochemistry and database identities were not retrieved. The record already distinguishes occurrence from production and notes possible publication overlap for the producer taxon.

### Occurrence and assay boundaries

scope: supported. Targets: CHEBI:63703.

Four raw LOTUS placements become three written occurrence items: Streptomyces clavuligerus, Gossypium hirsutum and Marchantia quadrata. The Preissia quadrata row uses old taxon 53029; exact retained taxon_merged row 78 maps it to 2729092, whose cache stanza includes Preissia quadrata as a synonym. The duplicate DOI/taxon-normalized placement is not additional independent evidence. PubChem row 1657 is a blank-AID '(no assay data)' sentinel for CID 12306055, not inactivity. The selected ChEBI-origin, CyanometDB, BindingDB and sibling-corpus routes add no observations in this saved scope.

### Computed classification and complete saved topology

other: supported. Targets: CHEBI:63703.

NPClassifier retains Terpenoids / Sesquiterpenoids / Cadinane sesquiterpenoids and is_glycoside=false. The complete C15 hydrocarbon graph with two carbon rings, two alkenes and no heteroatoms is structurally compatible with a nonglycosylated sesquiterpene scope. The model's class label remains computed, the MIBiG TERPENE BGC class remains source-asserted, and the optical-sign label remains independently unverified; none supplies an experimentally established biosynthetic sequence.

### Review completion and unavailable verification

completeness: unknown. Targets: CHEBI:63703.

The complete owner/history, actual 38-input intake, nine saved query frames, 8 positive source placements, applicable cached taxonomy and both complete original molecular forms were reviewed. No causal_graphs, causal_graph_refs, biosynthetic_pathway or molecular_targets root is present; no selected maintained-reader route applies. Five local gates and original chemistry have ROOT acceptance. FullQC, full OAK and fresh primary/identifier/taxonomy verification remain unavailable, so this is a qualified partial review and does not promote SEEDED status. Optional mechanism absence is not proof that biosynthesis is unknown in the literature.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2289-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/cadinene.yaml; lines 1–126 | supports | Whole current plaintext owner and all 3 history events; exact identifier CHEBI:63703, label (−)-δ-cadinene and full key FUCYIEXQVQJBKY-UKRRQHHQSA-N. Retained annotations are not fresh primary verification. |
| support-2289-capture | /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json; /records/8/owner_document; /records/8/owner_pin | supports | Complete accepted captured owner and current raw pin, including all present claims and history. |
| support-2289-source-plan | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8 | supports | Complete admitted selected context, nine saved query frames/full payloads and 38 planned inputs. Plan acceptance establishes scope, not scientific truth. |
| support-2289-intake | /private/tmp/npm-review-work/shared-next-batch229/intakes/2289-inspect-001.json; /targets; /source; /status | supports | Complete actual inspection-only intake, exact target, maintained owners and current context inputs. |
| support-2289-intake-ready | /private/tmp/npm-review-work/shared-next-batch229/root-intake-ready-001.json; /observer; /recorded_at; /batch; /status; /intake_summary; /execution; /original_tools; /selection_ready; /input_plan_acceptance; /native_acceptance; /original_terminal; /ROOT_readback; /source_placements; /unique_source_paths; /per_order_counts; /selection_and_complete_owner_equality; /mechanism_owner_orders; /required_component_inputs; /maintained_reader_invocations; /authorization; /external_requests; /record_changes; /scientific_verdicts | supports | ROOT acceptance of the original ten canonical intakes and their exact input maps; no scientific verdict supplied. |
| support-2289-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch229/root-input-plan-acceptance-001.json; /observer; /recorded_at; /batch; /status; /input_plan; /derivation; /source_notes; /source_adoption; /composer_execution; /composer_original_tools; /selection_ready; /original_terminal; /metadata_and_derivation_reading; /notes_whole_reading; /ROOT_current_input_and_whole_derivation_check; /source_placements; /unique_source_paths; /per_order_counts; /selected_records; /unselected_direct_contexts; /direct_companion_placements; /additional_context_placements; /selected_reader_orders; /components; /all_selected_mechanism_roots_absent; /assay_rows; /blank_AID_sentinels; /forward_merge_orders; /future_actual_roles_unbound; /authorization; /limitations; /external_requests; /record_changes; /scientific_verdicts | supports | ROOT acceptance of the original actual input plan, complete maps and current source bytes. |
| support-2289-source-notes | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-scope-notes-001.json; /observer; /recorded_at; /batch; /status; /inventory; /inventory_ROOT_acceptance; /inventory_ROOT_acceptance_inventory_key; /collector_source; /collector_source_adoption; /collector_execution; /collector_original_tools; /collector_original_terminal; /prior_final_acceptance; /prior_final_expected_status; /accepted_prior_remaining; /frozen_remaining; /actual_frozen229_remaining; /requirements; /selected_profile; /totals; /per_order_input_counts; /reading; /curation; /cautions; /current_inventory_input_pin_count; /future_actual_roles; /selected_reader_orders; /scientific_verdicts; /external_requests; /source_records_modified; /target_invocations_by_this_step | supports | Complete source-reading attribution, exact retained routes, source cautions and bounded implemented-curation scan; no new primary observation. |
| support-2289-chemistry | /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/smiles/computed; /records/8/inchi/computed; /records/8/comparisons; /records/8/atom_correspondence | supports | All ten saved comparison flags are true, with declared full key retained; the stored correspondence explicitly does not independently establish full graph or natural identity. |
| support-2289-topology | /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json; /records/8/smiles/computed; /records/8/inchi/computed | supports | Both complete saved forms are single-fragment C15H24 hydrocarbon graphs with two six-membered rings, two ring C=C bonds and no oxygen, nitrogen, carbonyl or sugar-ring motif. SMILES centres C4 R/C3 S correspond to InChI C12 R/C14 S. All bond stereo fields are STEREONONE and no potential unspecified double-bond stereoelement is reported; this is the saved local stereo inventory, not an optical-rotation calculation. |
| support-2289-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/root-diagnostic-acceptance-001.json; /observer; /recorded_at; /batch; /status; /DATA; /execution; /original_tools; /source_adoption; /intake_ready; /original_terminal; /actual_parse_attempts; /parsed_forms; /records; /denied_events; /input_pin_count; /current_pins_and_capture_intake_strings_exact; /false_comparisons; /stderr_scope; /reading_scope; /authorization; /external_requests; /record_changes; /scientific_verdicts | supports | ROOT acceptance of the original twenty-form observation and current pins; two original undefined-stereo warnings remain global and unassigned. |
| support-2289-native-acceptance | /private/tmp/npm-review-work/shared-next-batch229/root-native-gates-acceptance-001.json; /observer; /recorded_at; /batch; /status; /execution; /original_tools; /source_adoption; /selection_ready; /original_terminal; /ROOT_reading; /observer_recovery; /strict_selected_files; /strict_full_files; /strict_error_rows; /reproduction_records; /reproduction_byte_identical; /queue_rows; /queue_categories; /selected_queue_rows; /all_checked_input_bytes_unchanged; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /external_requests; /record_changes; /scientific_verdicts | supports | ROOT acceptance of five original local gates; FullQC and full OAK are explicitly unavailable, not passed. |
| support-2289-classification-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 375–432 | supports | The schema states Standard InChIKey limitations, the undefined-stereocentre flag scope, and that ComputedClassification is a versioned model result, never a source assertion. |
| support-2289-structure-extractor | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–173 | supports | Maintained structure_fields computes the stereo flag from FindMolChiralCenters(includeUnassigned=True); this is a tetrahedral-centre convention, not experimental stereochemical verification. |
| support-2289-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 990–1025 | supports | The seeder retains source structure strings/stereo flag and copies the named NPClassifier row, model version and boolean glycoside result into computed classification. |
| support-2289-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/source_scope_inventory/joins/mibig_compounds | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N"; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2289-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; lines 809–809 | supports | Complete retained source payload: {"mibig_accession":"BGC0000674","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"(-)-δ-cadinene","compound_index":"1","smiles":"CC1=C[C@@H]2[C@H](CCC(=C2CC1)C)C(C)C","standard_inchi":"InChI=1S/C15H24/c1-10(2)13-8-6-12(4)14-7-5-11(3)9-15(13)14/h9-10,13,15H,5-8H2,1-4H3/t13-,15-/m1/s1","standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:12306055","taxon_id":"NCBITaxon:1901","taxon_label":"Streptomyces clavuligerus ATCC 27064","bgc_classes":"terpene","bgc_subclasses":"Unknown","genome_accession":"DS570637.1","locus_from":"74962","locus_to":"79952","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:21276937","reference_basis":"ENTRY"} |
| support-2289-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/source_scope_inventory/joins/chebi_structures | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N"; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2289-row-chebi_structures-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; lines 20441–20441 | supports | Complete retained source payload: {"chebi_id":"CHEBI:63703","name":"(−)-δ-cadinene","definition":"A member of the cadinene family of sesquiterpenes in which the double bonds are located at the 4-4a and 7-8 positions, and in which the isopropyl group at position 1 is cis to the hydrogen at the adjacent bridgehead carbon (the 1R,8aS-enantiomer).","stars":"3","standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","smiles":"[H][C@]12C=C(C)CCC1=C(C)CC[C@@H]2C(C)C"} |
| support-2289-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/source_scope_inventory/joins/lotus_occurrences | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N"; positive placements=4. Zero matches are bounded to this snapshot. |
| support-2289-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; lines 1642–1642 | supports | Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","organism_name":"Streptomyces clavuligerus","taxon_id":"NCBITaxon:1901","organism_wikidata":"http://www.wikidata.org/entity/Q7623381","reference_doi":"10.1016/J.CHEMBIOL.2010.11.008","structure_wikidata":"http://www.wikidata.org/entity/Q27132741"} |
| support-2289-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; lines 1643–1643 | supports | Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","organism_name":"Marchantia quadrata","taxon_id":"NCBITaxon:2729092","organism_wikidata":"http://www.wikidata.org/entity/Q38318377","reference_doi":"10.1016/0031-9422(96)00354-8","structure_wikidata":"http://www.wikidata.org/entity/Q27132741"} |
| support-2289-row-lotus_occurrences-2 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; lines 1644–1644 | supports | Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","organism_name":"Gossypium hirsutum","taxon_id":"NCBITaxon:3635","organism_wikidata":"http://www.wikidata.org/entity/Q133481","reference_doi":"10.1021/JF60200A011","structure_wikidata":"http://www.wikidata.org/entity/Q27132741"} |
| support-2289-row-lotus_occurrences-3 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; lines 1645–1645 | supports | Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","organism_name":"Preissia quadrata","taxon_id":"NCBITaxon:53029","organism_wikidata":"http://www.wikidata.org/entity/Q2108505","reference_doi":"10.1016/0031-9422(96)00354-8","structure_wikidata":"http://www.wikidata.org/entity/Q27132741"} |
| support-2289-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N"; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2289-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/source_scope_inventory/joins/npclassifier | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N"; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2289-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; lines 610–610 | supports | Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","smiles":"CC1=C[C@@H]2[C@H](CCC(=C2CC1)C)C(C)C","pathway_results":"Terpenoids","superclass_results":"Sesquiterpenoids","class_results":"Cadinane sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"} |
| support-2289-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/source_scope_inventory/joins/pubchem_bioassay | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N"; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2289-row-pubchem_bioassay-0 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; lines 1657–1657 | supports | Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","cid":"12306055","aid":"","assay_name":"(no assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""} |
| support-2289-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/source_scope_inventory/joins/bindingdb_targets | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N"; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2289-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N"; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2289-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/source_scope_inventory/joins/chebi_origins | supports | Saved frame: predicate=exact chebi_id from exact full-key structure rows; query=["CHEBI:63703"]; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2289-routes | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/source_scope_inventory/matched_chebi_ids; /records/8/source_scope_inventory/source_taxa; /records/8/source_scope_inventory/forward_taxon_merge_matches; /records/8/source_scope_inventory/nonorganism_matches; /records/8/source_scope_inventory/actual_assay_rows; /records/8/source_scope_inventory/blank_AID_sentinels; /records/8/source_scope_inventory/related_corpus_rows | supports | Complete saved route fields: {"matched_chebi_ids":["CHEBI:63703"],"source_taxa":["NCBITaxon:1901","NCBITaxon:2729092","NCBITaxon:3635","NCBITaxon:53029"],"forward_taxon_merge_matches":[{"physical_line":78,"last_physical_line":78,"row":{"old_taxon_id":"NCBITaxon:53029","new_taxon_id":"NCBITaxon:2729092","requested_by":"lotus"},"raw_tsv_record":"NCBITaxon:53029\tNCBITaxon:2729092\tlotus\n","row_sha256":"5f131aeaa061e4b6025c1f1be93fd8025bd4bbdf42929fbac3c75cb165485db4"}],"nonorganism_matches":[],"actual_assay_rows":[],"blank_AID_sentinels":[{"physical_line":1657,"last_physical_line":1657,"row":{"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","cid":"12306055","aid":"","assay_name":"(no assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""},"raw_tsv_record":"FUCYIEXQVQJBKY-UKRRQHHQSA-N\t12306055\t\t(no assay data)\t\t\t\t\t\t\t\n","row_sha256":"cbf6c4a8abe722e78729bbe10275647a5d9be762d5b5d7c5db46d8294edf71db"}],"related_corpus_rows":[]} |
| support-2289-cache-1901 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; lines 2911–2914 | supports | Complete retained local taxonomy stanza: [Term]<br>id: NCBITaxon:1901<br>name: Streptomyces clavuligerus<br><br> |
| support-2289-cache-3635 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; lines 5039–5045 | supports | Complete retained local taxonomy stanza: [Term]<br>id: NCBITaxon:3635<br>name: Gossypium hirsutum<br>synonym: "Gossypium hirsutum subsp. mexicanum" EXACT []<br>synonym: "Gossypium lanceolatum" EXACT []<br>synonym: "Gossypium purpurascens" EXACT []<br><br> |
| support-2289-cache-2729092 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; lines 150382–150386 | supports | Complete retained local taxonomy stanza: [Term]<br>id: NCBITaxon:2729092<br>name: Marchantia quadrata<br>synonym: "Preissia quadrata (Scop.) Nees, 1838" EXACT []<br><br> |
| support-2289-taxon-merge-0 | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv; lines 78–78 | supports | Complete retained merge payload: {"old_taxon_id":"NCBITaxon:53029","new_taxon_id":"NCBITaxon:2729092","requested_by":"lotus"} |
| support-2289-companions | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/8/proposed_companion_paths; /records/8/direct_companion_predicates | supports | Exact admitted one-hop companion paths and predicates; membership alone does not transfer identity, assays or biosynthetic claims. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-229/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-229/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-229/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-229/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-229/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- FullQC and full OAK were unavailable. Five accepted local gates establish their stated technical results and do not establish scientific truth.
- No external retrieval, source-query replay or additional molecular/YAML parse occurred during fragment authoring. This review uses the original saved owner-form computations; their two global undefined-stereo warnings remain unassigned.
- Stored structure agreement, source full-key matching and local cached taxonomy do not independently establish the natural isolate, primary stereochemical assignment, optical rotation, current database identity or experimental mechanism.
- Producer and locus grades, occurrences, entry citations, source cross-references and named-model predictions remain distinct. No generated record, status, history, reserved decision table or source inventory was changed.
- The negative optical-sign label remains source-attributed; CIP assignments do not calculate optical rotation. The historical 53029→2729092 merge is supported only by the retained local row/cache.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- All findings/actions are empty within this bounded inspected scope; this does not certify every unverified source claim or create a native REVIEWED status.
- Maintained ownership remains in the admitted inventories, implemented curation tables, extractors and seeder. The reserved decisions.tsv is not a consumed correction mechanism.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T194802Z-cadinene
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: (−)-δ-cadinene'
started_at: '2026-11-03T19:22:18.979539Z'
finished_at: '2026-11-03T19:48:02.624284Z'
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
summary: Qualified partial review of the retained CHEBI:63703 Cadinene form, preserving
  encoded stereochemistry, unverified optical sign, source-only production and the
  exact historical liverwort taxon merge.
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
  - path: data/natural_products/terpenoids/cadinene.yaml
    sha256: d350d4d047a57ad1e663b2a59eee6875b0839aa82473a1db074a269cfe33b794
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
  selection: Campaign path order 2289; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:63703
targets:
- target_id: CHEBI:63703
  path: data/natural_products/terpenoids/cadinene.yaml
  label: (−)-δ-cadinene
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
  - CHEBI:63703
  command: just validate-strict data/natural_products/terpenoids/botryendial.yaml
    data/natural_products/terpenoids/brasilane-a.yaml data/natural_products/terpenoids/brasilane-d.yaml
    data/natural_products/terpenoids/brasilane-e.yaml data/natural_products/terpenoids/brasilane-f.yaml
    data/natural_products/terpenoids/brasilicardin-a.yaml data/natural_products/terpenoids/brassicicene-c.yaml
    data/natural_products/terpenoids/brevione-e.yaml data/natural_products/terpenoids/cadinene.yaml
    data/natural_products/terpenoids/calidoustene-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-229/validate-strict-selected10-001.tsv
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
  - CHEBI:63703
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-229/validate-all-001.tsv
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
  - CHEBI:63703
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
  - CHEBI:63703
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
  - CHEBI:63703
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-229/review-queue-001.tsv
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
  - CHEBI:63703
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:63703
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:63703
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2289-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/cadinene.yaml
  locator: lines 1–126
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Whole current plaintext owner and all 3 history events; exact identifier
    CHEBI:63703, label (−)-δ-cadinene and full key FUCYIEXQVQJBKY-UKRRQHHQSA-N. Retained
    annotations are not fresh primary verification.
  snapshot_sha256: d350d4d047a57ad1e663b2a59eee6875b0839aa82473a1db074a269cfe33b794
- evidence_id: support-2289-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json
  locator: /records/8/owner_document; /records/8/owner_pin
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Complete accepted captured owner and current raw pin, including all present
    claims and history.
  snapshot_sha256: c19fe825f5846fe8372e2f5c050eeabb32956de4867a1840e7c835ecf74003b1
- evidence_id: support-2289-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Complete admitted selected context, nine saved query frames/full payloads
    and 38 planned inputs. Plan acceptance establishes scope, not scientific truth.
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/intakes/2289-inspect-001.json
  locator: /targets; /source; /status
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Complete actual inspection-only intake, exact target, maintained owners
    and current context inputs.
  snapshot_sha256: 678286f425183d1de2537c28fc455b71f01afcadf29e657d512bf07671810aa7
- evidence_id: support-2289-intake-ready
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch229/root-intake-ready-001.json
  locator: /observer; /recorded_at; /batch; /status; /intake_summary; /execution;
    /original_tools; /selection_ready; /input_plan_acceptance; /native_acceptance;
    /original_terminal; /ROOT_readback; /source_placements; /unique_source_paths;
    /per_order_counts; /selection_and_complete_owner_equality; /mechanism_owner_orders;
    /required_component_inputs; /maintained_reader_invocations; /authorization; /external_requests;
    /record_changes; /scientific_verdicts
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: ROOT acceptance of the original ten canonical intakes and their exact input
    maps; no scientific verdict supplied.
  snapshot_sha256: 1b60455490dbc60704a7f7a0ff7e5b04ec2263c9b06d4d0b3dbbbc45596f141c
- evidence_id: support-2289-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch229/root-input-plan-acceptance-001.json
  locator: /observer; /recorded_at; /batch; /status; /input_plan; /derivation; /source_notes;
    /source_adoption; /composer_execution; /composer_original_tools; /selection_ready;
    /original_terminal; /metadata_and_derivation_reading; /notes_whole_reading; /ROOT_current_input_and_whole_derivation_check;
    /source_placements; /unique_source_paths; /per_order_counts; /selected_records;
    /unselected_direct_contexts; /direct_companion_placements; /additional_context_placements;
    /selected_reader_orders; /components; /all_selected_mechanism_roots_absent; /assay_rows;
    /blank_AID_sentinels; /forward_merge_orders; /future_actual_roles_unbound; /authorization;
    /limitations; /external_requests; /record_changes; /scientific_verdicts
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: ROOT acceptance of the original actual input plan, complete maps and current
    source bytes.
  snapshot_sha256: 788133f553f90cd741c62f133484bb771e3f84cf815c49abe689e4b178958fb2
- evidence_id: support-2289-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-scope-notes-001.json
  locator: /observer; /recorded_at; /batch; /status; /inventory; /inventory_ROOT_acceptance;
    /inventory_ROOT_acceptance_inventory_key; /collector_source; /collector_source_adoption;
    /collector_execution; /collector_original_tools; /collector_original_terminal;
    /prior_final_acceptance; /prior_final_expected_status; /accepted_prior_remaining;
    /frozen_remaining; /actual_frozen229_remaining; /requirements; /selected_profile;
    /totals; /per_order_input_counts; /reading; /curation; /cautions; /current_inventory_input_pin_count;
    /future_actual_roles; /selected_reader_orders; /scientific_verdicts; /external_requests;
    /source_records_modified; /target_invocations_by_this_step
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Complete source-reading attribution, exact retained routes, source cautions
    and bounded implemented-curation scan; no new primary observation.
  snapshot_sha256: d00fa7ab4a0f2141a9b2feb6db406422149c1a23eb7a8c0a140ba26724474b1f
- evidence_id: support-2289-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/smiles/computed; /records/8/inchi/computed;
    /records/8/comparisons; /records/8/atom_correspondence
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: All ten saved comparison flags are true, with declared full key retained;
    the stored correspondence explicitly does not independently establish full graph
    or natural identity.
  snapshot_sha256: 87fcd140466643697a72eeee9855fbcce9cbab4c39f9a234b683bc50809610da
- evidence_id: support-2289-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/smiles/computed; /records/8/inchi/computed
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Both complete saved forms are single-fragment C15H24 hydrocarbon graphs
    with two six-membered rings, two ring C=C bonds and no oxygen, nitrogen, carbonyl
    or sugar-ring motif. SMILES centres C4 R/C3 S correspond to InChI C12 R/C14 S.
    All bond stereo fields are STEREONONE and no potential unspecified double-bond
    stereoelement is reported; this is the saved local stereo inventory, not an optical-rotation
    calculation.
  snapshot_sha256: 87fcd140466643697a72eeee9855fbcce9cbab4c39f9a234b683bc50809610da
- evidence_id: support-2289-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /observer; /recorded_at; /batch; /status; /DATA; /execution; /original_tools;
    /source_adoption; /intake_ready; /original_terminal; /actual_parse_attempts; /parsed_forms;
    /records; /denied_events; /input_pin_count; /current_pins_and_capture_intake_strings_exact;
    /false_comparisons; /stderr_scope; /reading_scope; /authorization; /external_requests;
    /record_changes; /scientific_verdicts
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: ROOT acceptance of the original twenty-form observation and current pins;
    two original undefined-stereo warnings remain global and unassigned.
  snapshot_sha256: 3380fc981ad567d2ee44084ef8ec9675d2365aa945df29bce1b4a2c9bd215edd
- evidence_id: support-2289-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch229/root-native-gates-acceptance-001.json
  locator: /observer; /recorded_at; /batch; /status; /execution; /original_tools;
    /source_adoption; /selection_ready; /original_terminal; /ROOT_reading; /observer_recovery;
    /strict_selected_files; /strict_full_files; /strict_error_rows; /reproduction_records;
    /reproduction_byte_identical; /queue_rows; /queue_categories; /selected_queue_rows;
    /all_checked_input_bytes_unchanged; /five_local_commands_passed; /all_native_gates_passed;
    /unavailable_required_gates; /external_requests; /record_changes; /scientific_verdicts
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: ROOT acceptance of five original local gates; FullQC and full OAK are explicitly
    unavailable, not passed.
  snapshot_sha256: 6541455b28c210e07fb0d909bc7c062af31c1c73367724db8ad863dd7b338cc2
- evidence_id: support-2289-classification-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 375–432
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: The schema states Standard InChIKey limitations, the undefined-stereocentre
    flag scope, and that ComputedClassification is a versioned model result, never
    a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2289-structure-extractor
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–173
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Maintained structure_fields computes the stereo flag from FindMolChiralCenters(includeUnassigned=True);
    this is a tetrahedral-centre convention, not experimental stereochemical verification.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2289-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 990–1025
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: The seeder retains source structure strings/stereo flag and copies the
    named NPClassifier row, model version and boolean glycoside result into computed
    classification.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2289-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N";
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: lines 809–809
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"mibig_accession":"BGC0000674","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"(-)-δ-cadinene","compound_index":"1","smiles":"CC1=C[C@@H]2[C@H](CCC(=C2CC1)C)C(C)C","standard_inchi":"InChI=1S/C15H24/c1-10(2)13-8-6-12(4)14-7-5-11(3)9-15(13)14/h9-10,13,15H,5-8H2,1-4H3/t13-,15-/m1/s1","standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:12306055","taxon_id":"NCBITaxon:1901","taxon_label":"Streptomyces
    clavuligerus ATCC 27064","bgc_classes":"terpene","bgc_subclasses":"Unknown","genome_accession":"DS570637.1","locus_from":"74962","locus_to":"79952","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:21276937","reference_basis":"ENTRY"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2289-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N";
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-row-chebi_structures-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: lines 20441–20441
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"chebi_id":"CHEBI:63703","name":"(−)-δ-cadinene","definition":"A
    member of the cadinene family of sesquiterpenes in which the double bonds are
    located at the 4-4a and 7-8 positions, and in which the isopropyl group at position
    1 is cis to the hydrogen at the adjacent bridgehead carbon (the 1R,8aS-enantiomer).","stars":"3","standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","smiles":"[H][C@]12C=C(C)CCC1=C(C)CC[C@@H]2C(C)C"}'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: support-2289-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N";
    positive placements=4. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: lines 1642–1642
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","organism_name":"Streptomyces
    clavuligerus","taxon_id":"NCBITaxon:1901","organism_wikidata":"http://www.wikidata.org/entity/Q7623381","reference_doi":"10.1016/J.CHEMBIOL.2010.11.008","structure_wikidata":"http://www.wikidata.org/entity/Q27132741"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2289-row-lotus_occurrences-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: lines 1643–1643
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","organism_name":"Marchantia
    quadrata","taxon_id":"NCBITaxon:2729092","organism_wikidata":"http://www.wikidata.org/entity/Q38318377","reference_doi":"10.1016/0031-9422(96)00354-8","structure_wikidata":"http://www.wikidata.org/entity/Q27132741"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2289-row-lotus_occurrences-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: lines 1644–1644
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","organism_name":"Gossypium
    hirsutum","taxon_id":"NCBITaxon:3635","organism_wikidata":"http://www.wikidata.org/entity/Q133481","reference_doi":"10.1021/JF60200A011","structure_wikidata":"http://www.wikidata.org/entity/Q27132741"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2289-row-lotus_occurrences-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: lines 1645–1645
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","organism_name":"Preissia
    quadrata","taxon_id":"NCBITaxon:53029","organism_wikidata":"http://www.wikidata.org/entity/Q2108505","reference_doi":"10.1016/0031-9422(96)00354-8","structure_wikidata":"http://www.wikidata.org/entity/Q27132741"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2289-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N";
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N";
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: lines 610–610
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","smiles":"CC1=C[C@@H]2[C@H](CCC(=C2CC1)C)C(C)C","pathway_results":"Terpenoids","superclass_results":"Sesquiterpenoids","class_results":"Cadinane
    sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2289-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N";
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-row-pubchem_bioassay-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: lines 1657–1657
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","cid":"12306055","aid":"","assay_name":"(no
    assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""}'
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2289-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N";
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="FUCYIEXQVQJBKY-UKRRQHHQSA-N";
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact chebi_id from exact full-key structure rows;
    query=["CHEBI:63703"]; positive placements=0. Zero matches are bounded to this
    snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/source_scope_inventory/matched_chebi_ids; /records/8/source_scope_inventory/source_taxa;
    /records/8/source_scope_inventory/forward_taxon_merge_matches; /records/8/source_scope_inventory/nonorganism_matches;
    /records/8/source_scope_inventory/actual_assay_rows; /records/8/source_scope_inventory/blank_AID_sentinels;
    /records/8/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete saved route fields: {"matched_chebi_ids":["CHEBI:63703"],"source_taxa":["NCBITaxon:1901","NCBITaxon:2729092","NCBITaxon:3635","NCBITaxon:53029"],"forward_taxon_merge_matches":[{"physical_line":78,"last_physical_line":78,"row":{"old_taxon_id":"NCBITaxon:53029","new_taxon_id":"NCBITaxon:2729092","requested_by":"lotus"},"raw_tsv_record":"NCBITaxon:53029\tNCBITaxon:2729092\tlotus\n","row_sha256":"5f131aeaa061e4b6025c1f1be93fd8025bd4bbdf42929fbac3c75cb165485db4"}],"nonorganism_matches":[],"actual_assay_rows":[],"blank_AID_sentinels":[{"physical_line":1657,"last_physical_line":1657,"row":{"standard_inchi_key":"FUCYIEXQVQJBKY-UKRRQHHQSA-N","cid":"12306055","aid":"","assay_name":"(no
    assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""},"raw_tsv_record":"FUCYIEXQVQJBKY-UKRRQHHQSA-N\t12306055\t\t(no
    assay data)\t\t\t\t\t\t\t\n","row_sha256":"cbf6c4a8abe722e78729bbe10275647a5d9be762d5b5d7c5db46d8294edf71db"}],"related_corpus_rows":[]}'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2289-cache-1901
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: lines 2911–2914
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained local taxonomy stanza: [Term]

    id: NCBITaxon:1901

    name: Streptomyces clavuligerus


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2289-cache-3635
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: lines 5039–5045
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained local taxonomy stanza: [Term]

    id: NCBITaxon:3635

    name: Gossypium hirsutum

    synonym: "Gossypium hirsutum subsp. mexicanum" EXACT []

    synonym: "Gossypium lanceolatum" EXACT []

    synonym: "Gossypium purpurascens" EXACT []


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2289-cache-2729092
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: lines 150382–150386
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained local taxonomy stanza: [Term]

    id: NCBITaxon:2729092

    name: Marchantia quadrata

    synonym: "Preissia quadrata (Scop.) Nees, 1838" EXACT []


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2289-taxon-merge-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv
  locator: lines 78–78
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained merge payload: {"old_taxon_id":"NCBITaxon:53029","new_taxon_id":"NCBITaxon:2729092","requested_by":"lotus"}'
  snapshot_sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
- evidence_id: support-2289-companions
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/8/proposed_companion_paths; /records/8/direct_companion_predicates
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Exact admitted one-hop companion paths and predicates; membership alone
    does not transfer identity, assays or biosynthetic claims.
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-229/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json
  accessed_at: '2026-11-03T19:28:25.338690Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 8e76f523713143a050ad676d41e522571b00026df39ecade9edff35ae2b42c4f
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-229/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json
  accessed_at: '2026-11-03T19:28:51.405876Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 3418f061afb76c3d844e93d09ff706565af91b88ff9fcf592414bf5a4e71945e
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-229/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json
  accessed_at: '2026-11-03T19:29:11.399869Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-229/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json
  accessed_at: '2026-11-03T19:29:45.881063Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-229/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json
  accessed_at: '2026-11-03T19:29:57.736867Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 22ee87d5bc726fe92eaff82d6be77c49174e9b41a264952c4c5aaf3557afca8a
assessments:
- assessment_id: support-2289-A1
  area: identity
  topic: Exact structure concept and grounding
  outcome: supported
  summary: The owner is exactly grounded to retained three-star CHEBI:63703 with full
    key FUCYIEXQVQJBKY-UKRRQHHQSA-N, while its chemical strings come from MIBiG BGC0000674
    version 5, source compound_index=1. The saved ChEBI row has that same complete
    key and supplies the definition and Unicode-minus label; the ASCII-minus MIBiG
    synonym remains attributed. This supports the local exact-structure join. The
    source optical-sign label and PubChem cross-reference are not independently verified
    physical measurements or freshly resolved identities.
  target_ids:
  - CHEBI:63703
  evidence_ids:
  - support-2289-owner
  - support-2289-capture
  - support-2289-source-plan
  - support-2289-query-mibig_compounds
  - support-2289-query-chebi_structures
  - support-2289-companions
  - support-2289-row-mibig_compounds-0
  - support-2289-row-chebi_structures-0
  dimensions:
  - name: standard_inchi_key
    value: FUCYIEXQVQJBKY-UKRRQHHQSA-N
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-owner
    - support-2289-capture
    - support-2289-source-plan
    - support-2289-query-mibig_compounds
    - support-2289-query-chebi_structures
    - support-2289-companions
    - support-2289-row-mibig_compounds-0
    - support-2289-row-chebi_structures-0
  - name: grounding_scope
    value: The owner is exactly grounded to retained three-star CHEBI:63703 with full
      key FUCYIEXQVQJBKY-UKRRQHHQSA-N, while its chemical strings come from MIBiG
      BGC0000674 version 5, source compound_index=1. The saved ChEBI row has that
      same complete key and supplies the definition and Unicode-minus label; the ASCII-minus
      MIBiG synonym remains attributed. This supports the local exact-structure join.
      The source optical-sign label and PubChem cross-reference are not independently
      verified physical measurements or freshly resolved identities.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-owner
    - support-2289-capture
    - support-2289-source-plan
    - support-2289-query-mibig_compounds
    - support-2289-query-chebi_structures
    - support-2289-companions
    - support-2289-row-mibig_compounds-0
    - support-2289-row-chebi_structures-0
- assessment_id: support-2289-A2
  area: representation
  topic: Stored representation and stereochemistry
  outcome: supported
  summary: 'Both stored forms agree on neutral C15H24, 15 atoms, 16 bonds, Standard
    InChI/key and both canonical SMILES comparisons. The complete graph has two six-membered
    carbon rings and two ring double bonds, with two specified tetrahedral centres:
    SMILES C4 R and C3 S, corresponding to InChI C12 R and C14 S. Their connectivity
    is compatible with the retained ChEBI 1R,8aS definition and its adjacent isopropyl/bridgehead
    relation. The cis wording remains the retained source stereochemical description;
    no independent experimental relative-configuration determination is claimed. Optical
    rotation sign cannot be inferred solely from CIP assignments, and no rotation
    measurement was inspected. The source stereo_complete flag is bounded to the encoded
    assignments.'
  target_ids:
  - CHEBI:63703
  evidence_ids:
  - support-2289-owner
  - support-2289-capture
  - support-2289-chemistry
  - support-2289-topology
  - support-2289-diagnostic-acceptance
  - support-2289-classification-schema
  - support-2289-structure-extractor
  - support-2289-row-chebi_structures-0
  dimensions:
  - name: stereochemical_resolution
    value: 'Both stored forms agree on neutral C15H24, 15 atoms, 16 bonds, Standard
      InChI/key and both canonical SMILES comparisons. The complete graph has two
      six-membered carbon rings and two ring double bonds, with two specified tetrahedral
      centres: SMILES C4 R and C3 S, corresponding to InChI C12 R and C14 S. Their
      connectivity is compatible with the retained ChEBI 1R,8aS definition and its
      adjacent isopropyl/bridgehead relation. The cis wording remains the retained
      source stereochemical description; no independent experimental relative-configuration
      determination is claimed. Optical rotation sign cannot be inferred solely from
      CIP assignments, and no rotation measurement was inspected. The source stereo_complete
      flag is bounded to the encoded assignments.'
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-owner
    - support-2289-capture
    - support-2289-chemistry
    - support-2289-topology
    - support-2289-diagnostic-acceptance
    - support-2289-classification-schema
    - support-2289-structure-extractor
    - support-2289-row-chebi_structures-0
  - name: representation_correspondence
    value: 'Both stored forms agree on neutral C15H24, 15 atoms, 16 bonds, Standard
      InChI/key and both canonical SMILES comparisons. The complete graph has two
      six-membered carbon rings and two ring double bonds, with two specified tetrahedral
      centres: SMILES C4 R and C3 S, corresponding to InChI C12 R and C14 S. Their
      connectivity is compatible with the retained ChEBI 1R,8aS definition and its
      adjacent isopropyl/bridgehead relation. The cis wording remains the retained
      source stereochemical description; no independent experimental relative-configuration
      determination is claimed. Optical rotation sign cannot be inferred solely from
      CIP assignments, and no rotation measurement was inspected. The source stereo_complete
      flag is bounded to the encoded assignments.'
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-owner
    - support-2289-capture
    - support-2289-chemistry
    - support-2289-topology
    - support-2289-diagnostic-acceptance
    - support-2289-classification-schema
    - support-2289-structure-extractor
    - support-2289-row-chebi_structures-0
- assessment_id: support-2289-A3
  area: provenance
  topic: Producer, locus, taxon and strain roles
  outcome: supported
  summary: MIBiG asserts Streptomyces clavuligerus ATCC 27064 with SOURCE_ASSERTION
    and taxon NCBITaxon:1901, whose cached stanza is species-level. The strain qualifier
    is preserved without claiming independent strain resolution. BGC0000674 version
    5 is active/questionable/unknown, DS570637.1:74962–79952, with no locus method
    and CLUSTER_UNSTATED. The source taxon and locus grades remain separate from occurrence
    evidence. The retained 53029→2729092 route reconciles historical Preissia quadrata
    to cached Marchantia quadrata locally; it does not authorize a new taxonomy claim
    beyond this snapshot.
  target_ids:
  - CHEBI:63703
  evidence_ids:
  - support-2289-capture
  - support-2289-source-plan
  - support-2289-routes
  - support-2289-source-notes
  - support-2289-row-mibig_compounds-0
  - support-2289-cache-1901
  - support-2289-cache-3635
  - support-2289-cache-2729092
  - support-2289-taxon-merge-0
  dimensions:
  - name: taxon_and_strain_scope
    value: MIBiG asserts Streptomyces clavuligerus ATCC 27064 with SOURCE_ASSERTION
      and taxon NCBITaxon:1901, whose cached stanza is species-level. The strain qualifier
      is preserved without claiming independent strain resolution. BGC0000674 version
      5 is active/questionable/unknown, DS570637.1:74962–79952, with no locus method
      and CLUSTER_UNSTATED. The source taxon and locus grades remain separate from
      occurrence evidence. The retained 53029→2729092 route reconciles historical
      Preissia quadrata to cached Marchantia quadrata locally; it does not authorize
      a new taxonomy claim beyond this snapshot.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-capture
    - support-2289-source-plan
    - support-2289-routes
    - support-2289-source-notes
    - support-2289-row-mibig_compounds-0
    - support-2289-cache-1901
    - support-2289-cache-3635
    - support-2289-cache-2729092
    - support-2289-taxon-merge-0
  - name: producer_evidence_tier
    value: MIBiG asserts Streptomyces clavuligerus ATCC 27064 with SOURCE_ASSERTION
      and taxon NCBITaxon:1901, whose cached stanza is species-level. The strain qualifier
      is preserved without claiming independent strain resolution. BGC0000674 version
      5 is active/questionable/unknown, DS570637.1:74962–79952, with no locus method
      and CLUSTER_UNSTATED. The source taxon and locus grades remain separate from
      occurrence evidence. The retained 53029→2729092 route reconciles historical
      Preissia quadrata to cached Marchantia quadrata locally; it does not authorize
      a new taxonomy claim beyond this snapshot.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-capture
    - support-2289-source-plan
    - support-2289-routes
    - support-2289-source-notes
    - support-2289-row-mibig_compounds-0
    - support-2289-cache-1901
    - support-2289-cache-3635
    - support-2289-cache-2729092
    - support-2289-taxon-merge-0
  - name: locus_evidence_tier
    value: MIBiG asserts Streptomyces clavuligerus ATCC 27064 with SOURCE_ASSERTION
      and taxon NCBITaxon:1901, whose cached stanza is species-level. The strain qualifier
      is preserved without claiming independent strain resolution. BGC0000674 version
      5 is active/questionable/unknown, DS570637.1:74962–79952, with no locus method
      and CLUSTER_UNSTATED. The source taxon and locus grades remain separate from
      occurrence evidence. The retained 53029→2729092 route reconciles historical
      Preissia quadrata to cached Marchantia quadrata locally; it does not authorize
      a new taxonomy claim beyond this snapshot.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-capture
    - support-2289-source-plan
    - support-2289-routes
    - support-2289-source-notes
    - support-2289-row-mibig_compounds-0
    - support-2289-cache-1901
    - support-2289-cache-3635
    - support-2289-cache-2729092
    - support-2289-taxon-merge-0
- assessment_id: support-2289-A4
  area: evidence
  topic: Citation placement and primary-source limits
  outcome: supported
  summary: PMID:21276937 has MIBiG ENTRY scope. The ChEBI definition is attributed
    to CHEBI:63703; LOTUS retains DOI:10.1016/J.CHEMBIOL.2010.11.008, DOI:10.1016/0031-9422(96)00354-8
    and DOI:10.1021/JF60200A011. The same liverwort DOI appears under two raw taxon
    names and is not two independently established experiments. Primary text, optical
    rotation, source stereochemistry and database identities were not retrieved. The
    record already distinguishes occurrence from production and notes possible publication
    overlap for the producer taxon.
  target_ids:
  - CHEBI:63703
  evidence_ids:
  - support-2289-capture
  - support-2289-source-plan
  - support-2289-source-notes
  - support-2289-companions
  - support-2289-row-mibig_compounds-0
  - support-2289-row-chebi_structures-0
  - support-2289-row-lotus_occurrences-0
  - support-2289-row-lotus_occurrences-1
  - support-2289-row-lotus_occurrences-2
  - support-2289-row-lotus_occurrences-3
  - support-2289-row-npclassifier-0
  - support-2289-row-pubchem_bioassay-0
  dimensions:
  - name: citation_scope
    value: PMID:21276937 has MIBiG ENTRY scope. The ChEBI definition is attributed
      to CHEBI:63703; LOTUS retains DOI:10.1016/J.CHEMBIOL.2010.11.008, DOI:10.1016/0031-9422(96)00354-8
      and DOI:10.1021/JF60200A011. The same liverwort DOI appears under two raw taxon
      names and is not two independently established experiments. Primary text, optical
      rotation, source stereochemistry and database identities were not retrieved.
      The record already distinguishes occurrence from production and notes possible
      publication overlap for the producer taxon.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-capture
    - support-2289-source-plan
    - support-2289-source-notes
    - support-2289-companions
    - support-2289-row-mibig_compounds-0
    - support-2289-row-chebi_structures-0
    - support-2289-row-lotus_occurrences-0
    - support-2289-row-lotus_occurrences-1
    - support-2289-row-lotus_occurrences-2
    - support-2289-row-lotus_occurrences-3
    - support-2289-row-npclassifier-0
    - support-2289-row-pubchem_bioassay-0
- assessment_id: support-2289-A5
  area: scope
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: 'Four raw LOTUS placements become three written occurrence items: Streptomyces
    clavuligerus, Gossypium hirsutum and Marchantia quadrata. The Preissia quadrata
    row uses old taxon 53029; exact retained taxon_merged row 78 maps it to 2729092,
    whose cache stanza includes Preissia quadrata as a synonym. The duplicate DOI/taxon-normalized
    placement is not additional independent evidence. PubChem row 1657 is a blank-AID
    ''(no assay data)'' sentinel for CID 12306055, not inactivity. The selected ChEBI-origin,
    CyanometDB, BindingDB and sibling-corpus routes add no observations in this saved
    scope.'
  target_ids:
  - CHEBI:63703
  evidence_ids:
  - support-2289-capture
  - support-2289-source-plan
  - support-2289-routes
  - support-2289-companions
  - support-2289-query-mibig_compounds
  - support-2289-query-chebi_structures
  - support-2289-query-lotus_occurrences
  - support-2289-query-cyanometdb_occurrences
  - support-2289-query-npclassifier
  - support-2289-query-pubchem_bioassay
  - support-2289-query-bindingdb_targets
  - support-2289-query-antibioticmech_inchikeys
  - support-2289-query-chebi_origins
  - support-2289-row-mibig_compounds-0
  - support-2289-row-chebi_structures-0
  - support-2289-row-lotus_occurrences-0
  - support-2289-row-lotus_occurrences-1
  - support-2289-row-lotus_occurrences-2
  - support-2289-row-lotus_occurrences-3
  - support-2289-row-npclassifier-0
  - support-2289-row-pubchem_bioassay-0
  - support-2289-cache-1901
  - support-2289-cache-3635
  - support-2289-cache-2729092
  - support-2289-taxon-merge-0
  dimensions:
  - name: occurrence_scope
    value: 'Four raw LOTUS placements become three written occurrence items: Streptomyces
      clavuligerus, Gossypium hirsutum and Marchantia quadrata. The Preissia quadrata
      row uses old taxon 53029; exact retained taxon_merged row 78 maps it to 2729092,
      whose cache stanza includes Preissia quadrata as a synonym. The duplicate DOI/taxon-normalized
      placement is not additional independent evidence. PubChem row 1657 is a blank-AID
      ''(no assay data)'' sentinel for CID 12306055, not inactivity. The selected
      ChEBI-origin, CyanometDB, BindingDB and sibling-corpus routes add no observations
      in this saved scope.'
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-capture
    - support-2289-source-plan
    - support-2289-routes
    - support-2289-companions
    - support-2289-query-mibig_compounds
    - support-2289-query-chebi_structures
    - support-2289-query-lotus_occurrences
    - support-2289-query-cyanometdb_occurrences
    - support-2289-query-npclassifier
    - support-2289-query-pubchem_bioassay
    - support-2289-query-bindingdb_targets
    - support-2289-query-antibioticmech_inchikeys
    - support-2289-query-chebi_origins
    - support-2289-row-mibig_compounds-0
    - support-2289-row-chebi_structures-0
    - support-2289-row-lotus_occurrences-0
    - support-2289-row-lotus_occurrences-1
    - support-2289-row-lotus_occurrences-2
    - support-2289-row-lotus_occurrences-3
    - support-2289-row-npclassifier-0
    - support-2289-row-pubchem_bioassay-0
    - support-2289-cache-1901
    - support-2289-cache-3635
    - support-2289-cache-2729092
    - support-2289-taxon-merge-0
  - name: assay_scope
    value: 'Four raw LOTUS placements become three written occurrence items: Streptomyces
      clavuligerus, Gossypium hirsutum and Marchantia quadrata. The Preissia quadrata
      row uses old taxon 53029; exact retained taxon_merged row 78 maps it to 2729092,
      whose cache stanza includes Preissia quadrata as a synonym. The duplicate DOI/taxon-normalized
      placement is not additional independent evidence. PubChem row 1657 is a blank-AID
      ''(no assay data)'' sentinel for CID 12306055, not inactivity. The selected
      ChEBI-origin, CyanometDB, BindingDB and sibling-corpus routes add no observations
      in this saved scope.'
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-capture
    - support-2289-source-plan
    - support-2289-routes
    - support-2289-companions
    - support-2289-query-mibig_compounds
    - support-2289-query-chebi_structures
    - support-2289-query-lotus_occurrences
    - support-2289-query-cyanometdb_occurrences
    - support-2289-query-npclassifier
    - support-2289-query-pubchem_bioassay
    - support-2289-query-bindingdb_targets
    - support-2289-query-antibioticmech_inchikeys
    - support-2289-query-chebi_origins
    - support-2289-row-mibig_compounds-0
    - support-2289-row-chebi_structures-0
    - support-2289-row-lotus_occurrences-0
    - support-2289-row-lotus_occurrences-1
    - support-2289-row-lotus_occurrences-2
    - support-2289-row-lotus_occurrences-3
    - support-2289-row-npclassifier-0
    - support-2289-row-pubchem_bioassay-0
    - support-2289-cache-1901
    - support-2289-cache-3635
    - support-2289-cache-2729092
    - support-2289-taxon-merge-0
- assessment_id: support-2289-A6
  area: other
  topic: Computed classification and complete saved topology
  outcome: supported
  summary: NPClassifier retains Terpenoids / Sesquiterpenoids / Cadinane sesquiterpenoids
    and is_glycoside=false. The complete C15 hydrocarbon graph with two carbon rings,
    two alkenes and no heteroatoms is structurally compatible with a nonglycosylated
    sesquiterpene scope. The model's class label remains computed, the MIBiG TERPENE
    BGC class remains source-asserted, and the optical-sign label remains independently
    unverified; none supplies an experimentally established biosynthetic sequence.
  target_ids:
  - CHEBI:63703
  evidence_ids:
  - support-2289-capture
  - support-2289-chemistry
  - support-2289-topology
  - support-2289-classification-schema
  - support-2289-classification-seeder
  - support-2289-row-npclassifier-0
  - support-2289-row-mibig_compounds-0
  dimensions:
  - name: computed_classification
    value: NPClassifier retains Terpenoids / Sesquiterpenoids / Cadinane sesquiterpenoids
      and is_glycoside=false. The complete C15 hydrocarbon graph with two carbon rings,
      two alkenes and no heteroatoms is structurally compatible with a nonglycosylated
      sesquiterpene scope. The model's class label remains computed, the MIBiG TERPENE
      BGC class remains source-asserted, and the optical-sign label remains independently
      unverified; none supplies an experimentally established biosynthetic sequence.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-capture
    - support-2289-chemistry
    - support-2289-topology
    - support-2289-classification-schema
    - support-2289-classification-seeder
    - support-2289-row-npclassifier-0
    - support-2289-row-mibig_compounds-0
- assessment_id: support-2289-A7
  area: completeness
  topic: Review completion and unavailable verification
  outcome: unknown
  summary: The complete owner/history, actual 38-input intake, nine saved query frames,
    8 positive source placements, applicable cached taxonomy and both complete original
    molecular forms were reviewed. No causal_graphs, causal_graph_refs, biosynthetic_pathway
    or molecular_targets root is present; no selected maintained-reader route applies.
    Five local gates and original chemistry have ROOT acceptance. FullQC, full OAK
    and fresh primary/identifier/taxonomy verification remain unavailable, so this
    is a qualified partial review and does not promote SEEDED status. Optional mechanism
    absence is not proof that biosynthesis is unknown in the literature.
  target_ids:
  - CHEBI:63703
  evidence_ids:
  - support-2289-owner
  - support-2289-capture
  - support-2289-source-plan
  - support-2289-intake
  - support-2289-intake-ready
  - support-2289-plan-acceptance
  - support-2289-source-notes
  - support-2289-chemistry
  - support-2289-diagnostic-acceptance
  - support-2289-native-acceptance
  dimensions:
  - name: review_completion
    value: The complete owner/history, actual 38-input intake, nine saved query frames,
      8 positive source placements, applicable cached taxonomy and both complete original
      molecular forms were reviewed. No causal_graphs, causal_graph_refs, biosynthetic_pathway
      or molecular_targets root is present; no selected maintained-reader route applies.
      Five local gates and original chemistry have ROOT acceptance. FullQC, full OAK
      and fresh primary/identifier/taxonomy verification remain unavailable, so this
      is a qualified partial review and does not promote SEEDED status. Optional mechanism
      absence is not proof that biosynthesis is unknown in the literature.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2289-owner
    - support-2289-capture
    - support-2289-source-plan
    - support-2289-intake
    - support-2289-intake-ready
    - support-2289-plan-acceptance
    - support-2289-source-notes
    - support-2289-chemistry
    - support-2289-diagnostic-acceptance
    - support-2289-native-acceptance
findings: []
actions: []
limitations:
- FullQC and full OAK were unavailable. Five accepted local gates establish their
  stated technical results and do not establish scientific truth.
- No external retrieval, source-query replay or additional molecular/YAML parse occurred
  during fragment authoring. This review uses the original saved owner-form computations;
  their two global undefined-stereo warnings remain unassigned.
- Stored structure agreement, source full-key matching and local cached taxonomy do
  not independently establish the natural isolate, primary stereochemical assignment,
  optical rotation, current database identity or experimental mechanism.
- Producer and locus grades, occurrences, entry citations, source cross-references
  and named-model predictions remain distinct. No generated record, status, history,
  reserved decision table or source inventory was changed.
- The negative optical-sign label remains source-attributed; CIP assignments do not
  calculate optical rotation. The historical 53029→2729092 merge is supported only
  by the retained local row/cache.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- All findings/actions are empty within this bounded inspected scope; this does not
  certify every unverified source claim or create a native REVIEWED status.
- Maintained ownership remains in the admitted inventories, implemented curation tables,
  extractors and seeder. The reserved decisions.tsv is not a consumed correction mechanism.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-229
```
