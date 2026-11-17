# Local evidence review: Botryendial

- Review: 20261103T194802Z-botryendial
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T19:22:18.966523Z
- Finished UTC: 2026-11-03T19:48:02.541516Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Botryendial is locally consistent with its complete retained MIBiG key, encoded stereochemistry and compound-specific database citation. Producer strain, species occurrences and companion mechanisms remain distinct. Scientific completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2281; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-79ce4aca52 | data/natural_products/terpenoids/botryendial.yaml | generated | Botryendial |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-79ce4aca52 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-79ce4aca52 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-79ce4aca52 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-79ce4aca52 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-79ce4aca52 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-79ce4aca52 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-79ce4aca52 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-79ce4aca52 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-79ce4aca52.

The MINTED identifier retains the exact complete key QWZKEROSOALLJP-BYLNDYCFSA-N and source name from BGC0000631 version 5, compound index 8. The exact retained ChEBI structure join is empty, supporting the bounded minted-grounding explanation. Both saved forms reproduce C17H24O4 and the declared standardized key. Distinct direct congeners and their mechanisms do not resolve natural identity or justify a structure substitution.

### Representation

representation: supported. Targets: naturalproductmech:mibig-79ce4aca52.

Both saved forms are neutral C17H24O4 with 21 atoms, 22 bonds and one fragment. Four tetrahedral centres are specified with no unspecified potential centre in the saved tables. The two aldehydes, acetate and six/five-membered bicyclic framework are explicit. All ten comparison flags and the stored correspondence agree, while full_graph_identity_established remains false. The true stereo_complete flag is consistent with its centre-based scope, without establishing an experimentally verified natural stereoisomer.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-79ce4aca52.

BGC0000631 version 5 is active, questionable quality and complete in the retained source. Botrytis cinerea B05.10 (332648) has BGC_CHARACTERIZED producer support; Knock-out studies separately grade the locus CLUSTER_DEMONSTRATED. The retained interval is CP009816.1:2216500–2246000. The strain remains distinct from species-level 40559 occurrences. Cached Botryotinia fuckeliana/Botrytis cinerea synonyms preserve retained name continuity without fresh taxonomy or production verification.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-79ce4aca52.

DOI:10.1016/0031-9422(95)00643-5 is explicitly COMPOUND_EVIDENCE for Botryendial in MIBiG and is reused in written producer/locus evidence as DATABASE_ASSERTION. The same DOI also appears among three LOTUS occurrence assertions, alongside 10.1016/S0040-4020(99)00032-0 and 10.1021/NP980104B. These are retained citation placements, not verified independent experiments. Other Botry-family compound citations and Botrydial graph evidence remain separate.

### Occurrence and activity

evidence: supported. Targets: naturalproductmech:mibig-79ce4aca52.

Three LOTUS assertions place Botryendial in species-level Botrytis cinerea (40559); they do not by themselves establish B05.10 production or three independent experiments. The retained exact PubChem query is empty. There are no written bioactivities, molecular targets or mechanism roots. Exact BindingDB and AntibioticMech joins are empty. This bounds the saved evidence only; no biological inactivity or global pathway absence follows, and unselected companion mechanisms remain context.

### Classification

consistency: supported. Targets: naturalproductmech:mibig-79ce4aca52.

The source BGC class TERPENE and NPClassifier Terpenoids / Sesquiterpenoids / Botryane sesquiterpenoids output are separate assertions. The named model reports is_glycoside:false. Complete topology shows an oxygenated sesquiterpenoid framework with two aldehydes and an acetate, without a sugar residue or glycosidic linkage. This supports local applicability of the broad structural/model labels without proving a complete biosynthetic route or borrowing Botrydial's mechanism.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-79ce4aca52.

All twelve scientific dimensions were assessed against the current owner/history, actual intake, retained source payloads and complete paired molecular tables. Five local commands passed, while full QC, complete OAK authority coverage and fresh external verification remain unavailable. No selected mechanism reader is applicable. The exact bounded curation scan found no matching row in its declared scope, without a global absence claim. No supported local curation defect was established; scientific completion remains partial and native curation status is unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2281-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/botryendial.yaml; Whole owner plaintext and complete curation_history | supports | Complete current owner and all 2 history entries personally read; native curation_status remains SEEDED. |
| bgc-2281-capture | /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json; /records/0/owner_pin; /records/0/owner_document | supports | Exact complete captured owner, including all written fields and history. |
| bgc-2281-intake | /private/tmp/npm-review-work/shared-next-batch229/intakes/2281-inspect-001.json; /source; /targets | supports | Actual canonical one-record intake for naturalproductmech:mibig-79ce4aca52, with 57 current source inputs and explicit maintained field ownership. |
| bgc-2281-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch229/root-intake-ready-001.json; /status; /intake_summary; /source_placements; /unique_source_paths; /selection_and_complete_owner_equality | supports | ROOT accepts the original ten canonical intakes and their exact current owner/input maps. |
| bgc-2281-grounding-owner | /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json; /records/0/owner_document | supports | Complete written identity, grounding and source provenance: {"chemical_structure":{"smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi":"InChI=1S/C17H24O4/c1-10-6-13(21-11(2)20)15-14(12(10)7-18)17(5,9-19)8-16(15,3)4/h7,9-10,13,15H,6,8H2,1-5H3/t10-,13+,15-,17-/m1/s1","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000631"},"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-79ce4aca52","label":"Botryendial","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-79ce4aca52","source":"MIBIG","source_id":"BGC0000631","source_label":"Botryendial","source_version":"5"}],"xrefs":["npatlas:NPA007962"]} |
| bgc-2281-origin-owner | /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json; /records/0/owner_document | supports | Complete written producer and locus claims with separate grades: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0000631","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"5","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0000631 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1016/0031-9422(95)00643-5"}],"genome_accession":"genbank:CP009816.1","link_evidence_basis":"CLUSTER_DEMONSTRATED","locus_evidence_methods":["Knock-out studies"],"locus_from":2216500,"locus_to":2246000,"organism_label":"Botrytis cinerea B05.10","organism_taxon_id":"NCBITaxon:332648"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0000631","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0000631 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1016/0031-9422(95)00643-5"}],"evidence_basis":"BGC_CHARACTERIZED","notes":"Locus evidence: Knock-out studies. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"5","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis cinerea B05.10"}],"producer_taxon_groups":["FUNGAL"]} |
| bgc-2281-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json; /records/0/owner_document | supports | Complete written occurrences; omitted fields are absent in this complete captured owner: {"occurrence_taxon_groups":["FUNGAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/0031-9422(95)00643-5"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis cinerea","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/S0040-4020(99)00032-0"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis cinerea","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1021/NP980104B"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis cinerea","taxon_source":"NCBITaxon"}]} |
| bgc-2281-assay-owner | /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json; /records/0/owner_document | supports | Complete owner establishes no written assay, target or mechanism roots; no biological absence is inferred: {} |
| bgc-2281-classification-owner | /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json; /records/0/owner_document | supports | Literal source BGC class and named/versioned computed classification: {"bgc_class":["TERPENE"],"np_classification":{"class_results":["Botryane sesquiterpenoids"],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Sesquiterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"} |
| bgc-2281-chemistry | /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/smiles/status; /records/0/inchi/status; /records/0/smiles/computed; /records/0/inchi/computed; /records/0/comparisons; /records/0/atom_correspondence | supports | Both saved forms parsed. Complete atom/bond/ring/stereo/motif tables were personally read. Saved comparison facts: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim.","smiles_to_inchi_atom_indices":[0,9,5,12,14,13,11,6,17,16,7,15,2,3,4,8,18,20,10,19,1]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"declared_structure":{"smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi":"InChI=1S/C17H24O4/c1-10-6-13(21-11(2)20)15-14(12(10)7-18)17(5,9-19)8-16(15,3)4/h7,9-10,13,15H,6,8H2,1-5H3/t10-,13+,15-,17-/m1/s1","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000631"},"inchi_formula":"C17H24O4","smiles_formula":"C17H24O4"} |
| bgc-2281-topology | /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json; /records/0/smiles/computed; /records/0/inchi/computed; /records/0/atom_correspondence | supports | SMILES atoms 7(=O8) and 15(=O16) are aldehyde carbons, each with one hydrogen. The acetate is C3–O17–C18(=O19)–C20. The six- and five-membered rings share the C4–C5 bond. Four specified tetrahedral centres are C1 R, C3 S, C4 S and C9 S. The complete counterpart tables and stored atom correspondence preserve these represented features; no independent natural stereochemical identity is established. |
| bgc-2281-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-execution-001.json; /command; /cwd; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr; /external_requests; /retries | supports | Original process receipt retains exit 0, command, clocks, source and stdout/stderr pins, without retries or external requests. |
| bgc-2281-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/root-diagnostic-acceptance-001.json; /observer; /recorded_at; /batch; /status; /DATA; /execution; /original_tools; /source_adoption; /intake_ready; /original_terminal; /actual_parse_attempts; /parsed_forms; /records; /denied_events; /input_pin_count; /current_pins_and_capture_intake_strings_exact; /false_comparisons; /stderr_scope; /reading_scope; /authorization; /external_requests; /record_changes; /scientific_verdicts | supports | ROOT accepts the original 20 stored-form parses and current inputs. The two original undefined-stereo warnings are global, without per-record stream attribution. This receipt does not establish natural identity. |
| bgc-2281-native-acceptance | /private/tmp/npm-review-work/shared-next-batch229/root-native-gates-acceptance-001.json; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows; /strict_error_rows | supports | Five local commands passed; all_native_gates_passed is false because full QC and OAK authority coverage remain unavailable. Selected queue entries are review aids, not new scientific findings. |
| bgc-2281-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch229-tentative/root-source-inventory-acceptance-001.json; /observer; /recorded_at; /status; /inventory; /execution; /original_tools; /source_adoption; /original_terminal; /root_saved_execution_metadata_and_scope_reading; /verification; /scope; /actual229_target_authorities; /external_requests; /target_invocations_by_observer | supports | ROOT accepts the original retained source inventory and current maps; complete source-payload meaning is separately attributed. |
| bgc-2281-plan | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/0; /source_placement_count; /unique_source_path_count | supports | Accepted source plan retains the exact owner and context/input roles within 414 source placements and 72 unique paths. |
| bgc-2281-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch229/root-input-plan-acceptance-001.json; /status; /input_plan; /source_notes; /source_placements; /unique_source_paths; /selected_reader_orders | supports | ROOT accepts the actual source plan and its input/owner joins; no selected maintained reader applies. |
| bgc-2281-source-notes | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-scope-notes-001.json; /reading; /curation; /cautions | supports | Complete personal and delegated retained-source readings, exact prior raw/history carries, curation scope and limitations are explicitly attributed. No fresh external source access is implied. |
| bgc-2281-direct-contexts | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /records/0/direct_companion_paths; /records/0/direct_companion_predicates | supports | Exact one-hop context predicates, without mechanism, activity or identity transfer: {"direct_companion_paths":["data/natural_products/terpenoids/1-epibotrydial.yaml","data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml","data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml","data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml","data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml","data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml","data/natural_products/terpenoids/8-9-epibotrydial.yaml","data/natural_products/terpenoids/botrydial.yaml","data/natural_products/terpenoids/botrydienal.yaml","data/natural_products/terpenoids/botryenalol.yaml","data/natural_products/terpenoids/dehydrobotrydienol.yaml","data/natural_products/terpenoids/dihydrobotrydial.yaml","data/natural_products/terpenoids/norbotrydialone-acetate.yaml","data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml","data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml","data/natural_products/terpenoids/secobotrytriendiol.yaml","data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/terpenoids/1-epibotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/8-9-epibotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botrydienal.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botryenalol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/dehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/dihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/norbotrydialone-acetate.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrytriendiol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]}]} |
| bgc-2281-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/mibig_compounds | supports | Complete retained predicate/query frame and physical matched payloads: {"matches":[{"last_physical_line":734,"physical_line":734,"raw_tsv_record":"BGC0000631\t5\tactive\tquestionable\tcomplete\tBotryendial\t8\tC[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C\tInChI=1S/C17H24O4/c1-10-6-13(21-11(2)20)15-14(12(10)7-18)17(5,9-19)8-16(15,3)4/h7,9-10,13,15H,6,8H2,1-5H3/t10-,13+,15-,17-/m1/s1\tQWZKEROSOALLJP-BYLNDYCFSA-N\ttrue\t\tnpatlas:NPA007962\tNCBITaxon:332648\tBotrytis cinerea B05.10\tterpene\tSesquiterpene\tCP009816.1\t2216500\t2246000\tKnock-out studies\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tDOI:10.1016/0031-9422(95)00643-5\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Sesquiterpene","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"8","compound_name":"Botryendial","database_ids":"npatlas:NPA007962","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"CP009816.1","locus_evidence_methods":"Knock-out studies","locus_from":"2216500","locus_to":"2246000","mibig_accession":"BGC0000631","primary_reference":"DOI:10.1016/0031-9422(95)00643-5","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi":"InChI=1S/C17H24O4/c1-10-6-13(21-11(2)20)15-14(12(10)7-18)17(5,9-19)8-16(15,3)4/h7,9-10,13,15H,6,8H2,1-5H3/t10-,13+,15-,17-/m1/s1","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis cinerea B05.10"},"row_sha256":"e388a60bd1548fd47c646b0409d678e7a25cdfde77f9cc86215049bbfa922dcd"}],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"} |
| bgc-2281-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 734–734; row_sha256 e388a60bd1548fd47c646b0409d678e7a25cdfde77f9cc86215049bbfa922dcd | supports | Complete physical source payloads, all fields read and joined to the current pinned table: [{"bgc_classes":"terpene","bgc_subclasses":"Sesquiterpene","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"8","compound_name":"Botryendial","database_ids":"npatlas:NPA007962","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"CP009816.1","locus_evidence_methods":"Knock-out studies","locus_from":"2216500","locus_to":"2246000","mibig_accession":"BGC0000631","primary_reference":"DOI:10.1016/0031-9422(95)00643-5","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi":"InChI=1S/C17H24O4/c1-10-6-13(21-11(2)20)15-14(12(10)7-18)17(5,9-19)8-16(15,3)4/h7,9-10,13,15H,6,8H2,1-5H3/t10-,13+,15-,17-/m1/s1","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis cinerea B05.10"}] |
| bgc-2281-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/chebi_structures | supports | Complete retained predicate/query frame and physical matched payloads: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"} |
| bgc-2281-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained predicate/query frame and physical matched payloads: {"matches":[{"last_physical_line":7581,"physical_line":7581,"raw_tsv_record":"QWZKEROSOALLJP-BYLNDYCFSA-N\tBotrytis cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1016/0031-9422(95)00643-5\thttp://www.wikidata.org/entity/Q77420122\n","row":{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(95)00643-5","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"},"row_sha256":"f55ad3ec58d89fb76092d9668edfb08a32664d8f663741c0a99d039202ba77e6"},{"last_physical_line":7582,"physical_line":7582,"raw_tsv_record":"QWZKEROSOALLJP-BYLNDYCFSA-N\tBotrytis cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1016/S0040-4020(99)00032-0\thttp://www.wikidata.org/entity/Q77420122\n","row":{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/S0040-4020(99)00032-0","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"},"row_sha256":"bd2f6fd35f9cfb8fcef13a753e33a4f82767978486b5b063064adbb96e40e612"},{"last_physical_line":7583,"physical_line":7583,"raw_tsv_record":"QWZKEROSOALLJP-BYLNDYCFSA-N\tBotrytis cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1021/NP980104B\thttp://www.wikidata.org/entity/Q77420122\n","row":{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1021/NP980104B","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"},"row_sha256":"493307ca675b1f90dae440299ddc7dddbe33d0dbc0d9aaabc4711d6d94f63b8f"}],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"} |
| bgc-2281-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 7581–7581; row_sha256 f55ad3ec58d89fb76092d9668edfb08a32664d8f663741c0a99d039202ba77e6; physical lines 7582–7582; row_sha256 bd2f6fd35f9cfb8fcef13a753e33a4f82767978486b5b063064adbb96e40e612; physical lines 7583–7583; row_sha256 493307ca675b1f90dae440299ddc7dddbe33d0dbc0d9aaabc4711d6d94f63b8f | supports | Complete physical source payloads, all fields read and joined to the current pinned table: [{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(95)00643-5","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"},{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/S0040-4020(99)00032-0","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"},{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1021/NP980104B","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"}] |
| bgc-2281-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained predicate/query frame and physical matched payloads: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"} |
| bgc-2281-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/npclassifier | supports | Complete retained predicate/query frame and physical matched payloads: {"matches":[{"last_physical_line":2055,"physical_line":2055,"raw_tsv_record":"QWZKEROSOALLJP-BYLNDYCFSA-N\tC[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C\tTerpenoids\tSesquiterpenoids\tBotryane sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Botryane sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","superclass_results":"Sesquiterpenoids"},"row_sha256":"7bed2ac4fda04a45bda1ecee0d99a126135016a86e684cfd8bfdb2294604e659"}],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"} |
| bgc-2281-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 2055–2055; row_sha256 7bed2ac4fda04a45bda1ecee0d99a126135016a86e684cfd8bfdb2294604e659 | supports | Complete physical source payloads, all fields read and joined to the current pinned table: [{"class_results":"Botryane sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","superclass_results":"Sesquiterpenoids"}] |
| bgc-2281-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained predicate/query frame and physical matched payloads: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"} |
| bgc-2281-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained predicate/query frame and physical matched payloads: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"} |
| bgc-2281-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained predicate/query frame and physical matched payloads: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"} |
| bgc-2281-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/chebi_origins | supports | Complete retained predicate/query frame and physical matched payloads: {"matches":[],"predicate":"exact chebi_id from exact full-key structure rows","query":[]} |
| bgc-2281-source-routes | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/source_taxa; /contexts/13/source_scope_inventory/forward_taxon_merge_matches; /contexts/13/source_scope_inventory/nonorganism_matches; /contexts/13/source_scope_inventory/actual_assay_rows; /contexts/13/source_scope_inventory/blank_AID_sentinels; /contexts/13/source_scope_inventory/related_corpus_rows | supports | Exact source taxa and complete route lists; blank AIDs are distinguished from actual assays: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:332648","NCBITaxon:40559"]} |
| bgc-2281-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/unmatched_ids; /cached_taxonomy/whole_stanzas/4; /cached_taxonomy/whole_stanzas/9 | supports | Whole retained stanzas for this source-taxon scope, with global misses retained separately; no fresh taxonomy or ancestry inference: [{"complete_stanza":"[Term]\nid: NCBITaxon:40559\nname: Botrytis cinerea\nsynonym: \"Botryotinia fuckeliana\" EXACT []\nsynonym: \"Botrytis cinerea Pers., 1801\" EXACT []\nsynonym: \"Peziza fuckeliana\" EXACT []\nsynonym: \"Sclerotinia fuckeliana\" EXACT []\n\n","id":"NCBITaxon:40559","physical_line":18031},{"complete_stanza":"[Term]\nid: NCBITaxon:332648\nname: Botrytis cinerea B05.10\nsynonym: \"Botryotinia fuckeliana B05.10\" EXACT []\n\n","id":"NCBITaxon:332648","physical_line":83758}] |
| bgc-2281-curation-scope | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-scope-notes-001.json; /curation | supports | The completed direct-open, ignore-independent scan tested 92 exact cohort literals against eight named implemented curation tables and 93 data rows. Zero hits is limited to that scope. Reserved decisions.tsv was not consumed; PubChem exclusions were only a supplementary reading dependency because no actual AID matched. |
| bgc-2281-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure preserves source SMILES and unspecified stereocentres; normalized keys have explicit limits. ComputedClassification is named/versioned model output, not source assertion or admission evidence. |
| bgc-2281-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | The maintained extractor derives stereo_complete only from FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False) and question-mark tags; it does not test every double-bond geometry. No extractor ran in this authoring step. |
| bgc-2281-origin-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 1067–1196 | supports | Producer and locus claims/grades are copied separately with explicit taxon and qualification handling. ChEBI occurrence is not promoted to production. |
| bgc-2281-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 974–1065 | supports | Minted grounding, named model prediction projection, source concepts, BGC classes and retained cross-references have distinct maintained roles. |
| bgc-2281-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole profile | supports | The current profile requires claim-level evidence and all scientific dimensions without promoting unavailable checks. |
| bgc-2281-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole skill | supports | The one-record review procedure requires truthful source access and completion limits; this review edits no source record and makes no external request. |
| bgc-2281-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json; /contexts/0/identifier; /contexts/0/standard_inchi_key; /contexts/0/owned_bgc_ids; /contexts/0/complete_raw_text; /contexts/0/literal_mechanism_inventory; /contexts/1/identifier; /contexts/1/standard_inchi_key; /contexts/1/owned_bgc_ids; /contexts/1/complete_raw_text; /contexts/1/literal_mechanism_inventory; /contexts/2/identifier; /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids; /contexts/2/complete_raw_text; /contexts/2/literal_mechanism_inventory; /contexts/3/identifier; /contexts/3/standard_inchi_key; /contexts/3/owned_bgc_ids; /contexts/3/complete_raw_text; /contexts/3/literal_mechanism_inventory; /contexts/4/identifier; /contexts/4/standard_inchi_key; /contexts/4/owned_bgc_ids; /contexts/4/complete_raw_text; /contexts/4/literal_mechanism_inventory; /contexts/5/identifier; /contexts/5/standard_inchi_key; /contexts/5/owned_bgc_ids; /contexts/5/complete_raw_text; /contexts/5/literal_mechanism_inventory; /contexts/6/identifier; /contexts/6/standard_inchi_key; /contexts/6/owned_bgc_ids; /contexts/6/complete_raw_text; /contexts/6/literal_mechanism_inventory; /contexts/7/identifier; /contexts/7/standard_inchi_key; /contexts/7/owned_bgc_ids; /contexts/7/complete_raw_text; /contexts/7/literal_mechanism_inventory; /contexts/8/identifier; /contexts/8/standard_inchi_key; /contexts/8/owned_bgc_ids; /contexts/8/complete_raw_text; /contexts/8/literal_mechanism_inventory; /contexts/9/identifier; /contexts/9/standard_inchi_key; /contexts/9/owned_bgc_ids; /contexts/9/complete_raw_text; /contexts/9/literal_mechanism_inventory; /contexts/10/identifier; /contexts/10/standard_inchi_key; /contexts/10/owned_bgc_ids; /contexts/10/complete_raw_text; /contexts/10/literal_mechanism_inventory; /contexts/11/identifier; /contexts/11/standard_inchi_key; /contexts/11/owned_bgc_ids; /contexts/11/complete_raw_text; /contexts/11/literal_mechanism_inventory; /contexts/12/identifier; /contexts/12/standard_inchi_key; /contexts/12/owned_bgc_ids; /contexts/12/complete_raw_text; /contexts/12/literal_mechanism_inventory; /contexts/25/identifier; /contexts/25/standard_inchi_key; /contexts/25/owned_bgc_ids; /contexts/25/complete_raw_text; /contexts/25/literal_mechanism_inventory; /contexts/26/identifier; /contexts/26/standard_inchi_key; /contexts/26/owned_bgc_ids; /contexts/26/complete_raw_text; /contexts/26/literal_mechanism_inventory; /contexts/28/identifier; /contexts/28/standard_inchi_key; /contexts/28/owned_bgc_ids; /contexts/28/complete_raw_text; /contexts/28/literal_mechanism_inventory; /contexts/29/identifier; /contexts/29/standard_inchi_key; /contexts/29/owned_bgc_ids; /contexts/29/complete_raw_text; /contexts/29/literal_mechanism_inventory; /contexts/30/identifier; /contexts/30/standard_inchi_key; /contexts/30/owned_bgc_ids; /contexts/30/complete_raw_text; /contexts/30/literal_mechanism_inventory; /contexts/31/identifier; /contexts/31/standard_inchi_key; /contexts/31/owned_bgc_ids; /contexts/31/complete_raw_text; /contexts/31/literal_mechanism_inventory; /contexts/32/identifier; /contexts/32/standard_inchi_key; /contexts/32/owned_bgc_ids; /contexts/32/complete_raw_text; /contexts/32/literal_mechanism_inventory | supports | Direct compounds retain distinct complete keys. Whole companion raw/history reading and exact prior carries are attributed in the source notes. Unselected Botrydial or Trichobrasilenol mechanism/protein assertions remain context only. Exact identities and literal graph scopes: [{"identifier":"naturalproductmech:mibig-acc775e1b7","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"SJFIYVCSGNWVPJ-SDLFRHKASA-N"},{"identifier":"naturalproductmech:mibig-1e06238f05","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"MBHVNAKPTPFWNG-MYFMSEKESA-N"},{"identifier":"naturalproductmech:mibig-7950af79c1","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"QUGYVDURDBEQRB-VZJVBFQISA-N"},{"identifier":"naturalproductmech:mibig-e2d62600f5","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"MFOUCDNLAFNKML-SVLWDWOGSA-N"},{"identifier":"naturalproductmech:mibig-7b45e48275","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"CAMCSBCRRUTMEK-OAHLLOKOSA-N"},{"identifier":"naturalproductmech:mibig-8b4cd14741","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"PCEVLQFNPPWJEB-RFAUZJTJSA-N"},{"identifier":"naturalproductmech:mibig-bbb6f44666","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"JUCMRFKOKIZVPS-OAHLLOKOSA-N"},{"identifier":"naturalproductmech:mibig-10fda622fe","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"YPJRKTIWVUVMDI-LSDHHAIUSA-N"},{"identifier":"naturalproductmech:mibig-0bd6ab53bc","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"RVXLTRZIAMMATE-JMTSMVSISA-N"},{"identifier":"naturalproductmech:mibig-a2b74a45ae","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"SJFIYVCSGNWVPJ-PQVRDHEWSA-N"},{"identifier":"CHEBI:3159","literal_mechanism_inventory":{"edges":10,"graph_ids":["botrydial-bcbot-biosynthesis"],"graph_reference_placements":30,"graph_refs":[],"graphs":1,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":11,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"SJFIYVCSGNWVPJ-GKKOWQTJSA-N"},{"identifier":"naturalproductmech:mibig-a1c6942987","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"CFAMAVBUWMXYLX-MEBBXXQBSA-N"},{"identifier":"naturalproductmech:mibig-d567f1a1cd","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"DSVSTMJOGQEZJX-BYLNDYCFSA-N"},{"identifier":"naturalproductmech:mibig-247120aa23","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"UQQKKLVKVVJDEX-OAHLLOKOSA-N"},{"identifier":"naturalproductmech:mibig-b5ca742a5e","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N"},{"identifier":"naturalproductmech:mibig-9b040d7e03","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"OMZUEHMZFLBHNI-PCKWUFTNSA-N"},{"identifier":"naturalproductmech:mibig-2cef442430","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"GYABYKLKVQPSPD-NVWZYQMFSA-N"},{"identifier":"naturalproductmech:mibig-f478b3a4f7","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"GNMCOKDZWITFBO-MGNGBMTDSA-N"},{"identifier":"naturalproductmech:mibig-ff72b656ae","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"BHNACKMCMDASDB-UJNBGNEJSA-N"},{"identifier":"naturalproductmech:mibig-1c14174a30","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"WLPOYIWCPMYYGM-KGRKPJGKSA-N"}] |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-229/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-229/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-229/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-229/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-229/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-229/native-current229-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External identifiers, taxonomy, genome accessions and primary publications were not refreshed under the absolute no-request instruction. Historical and database assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and stored-form parsing establish only their declared mechanical scope.
- Empty joins refer only to retained exact predicates and snapshots; they do not establish biological absence. Shared loci, citations and congeners do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source records, native curation status and histories were not edited.
- Historical unselected Botrydial and Trichobrasilenol mechanisms are context-only. No compound-specific pathway, protein sequence, construct or activity is transferred to this owner.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- All current owner/history text, complete actual intake and both complete saved molecular tables were personally read. Retained source/companion reading and exact prior carries are attributed in the pinned source notes.
- The original diagnostic's two undefined-stereo warnings remain global and unassigned. No additional molecular/YAML parse, source query or target invocation occurred during authoring.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T194802Z-botryendial
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: Botryendial'
started_at: '2026-11-03T19:22:18.966523Z'
finished_at: '2026-11-03T19:48:02.541516Z'
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
summary: Botryendial is locally consistent with its complete retained MIBiG key, encoded
  stereochemistry and compound-specific database citation. Producer strain, species
  occurrences and companion mechanisms remain distinct. Scientific completion is partial.
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
  - path: data/natural_products/terpenoids/1-epibotrydial.yaml
    sha256: de27183b14aeebdaa766502e80b533dae2b4fea8cbb8a1a1c3d3623793f80775
    role: context
  - path: data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml
    sha256: 755ae0d04e75ed4fb5510c53f3ac3d011a77064305a8e5e22f5fb24a2b4fc2c6
    role: context
  - path: data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml
    sha256: 5a35280153870595b8fa92396c1a4803d341f3618f91ff32c5c49fcab4044e48
    role: context
  - path: data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml
    sha256: 600744b216155b8a5c6e7e2cec0f0d47be3fb23ddf7d291b353035f0392b6bed
    role: context
  - path: data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml
    sha256: c3a205986d77c29236528a192299e9ce2f2d7011d6cb38300b7e07ec2865143f
    role: context
  - path: data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml
    sha256: 583c51cc539f04fc68e99a0fe5b1b86e7e2e0c76235227e5a19356847929bf0d
    role: context
  - path: data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml
    sha256: c25e2696521c9381fbaebaf01deac68cdc70cab04a9b7ab03eda82c595b0a561
    role: context
  - path: data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml
    sha256: d8a363fb5c558056a1c7ed69312e113e2310f8bfbbf787f8eb07a0030745ec54
    role: context
  - path: data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml
    sha256: c4c9d1c900ad07aac687e0b9ec51c5ba589e9e065c4f0116446a248ba366112e
    role: context
  - path: data/natural_products/terpenoids/8-9-epibotrydial.yaml
    sha256: 11f0440d7c378d961befc6e158afa3f9a839110ce672438ad032baa487a9cc33
    role: context
  - path: data/natural_products/terpenoids/botrydial.yaml
    sha256: f12d22645ff34656cf446630d1b2c838db1ffa59c978182a42c5e10fcd5134cd
    role: context
  - path: data/natural_products/terpenoids/botrydienal.yaml
    sha256: 7f18efdecb4f12ebcf7c8e9710f0cb70d630b33cad1ba3c79b2aa8f8db7af839
    role: context
  - path: data/natural_products/terpenoids/botryenalol.yaml
    sha256: 473ebf066845fe74c1373996eceff8390a4e4ee3583cd69b3cf751683b936add
    role: context
  - path: data/natural_products/terpenoids/botryendial.yaml
    sha256: 3c5281cc27c72cdcd4b4c0ff933483687532e1be9378618a7cf209a691a98761
    role: target
  - path: data/natural_products/terpenoids/dehydrobotrydienol.yaml
    sha256: 8a56db9386bde355c12ccb9e3b6a333857a96ccbb7db253a52765213ec4538b5
    role: context
  - path: data/natural_products/terpenoids/dihydrobotrydial.yaml
    sha256: aa738c13a340ea710c01fb6d36f9a794537660a87237bd1a576db8a9c2c9de9b
    role: context
  - path: data/natural_products/terpenoids/norbotrydialone-acetate.yaml
    sha256: 347f7627931387555bad558583abf5d0edd65f74374c37f7e462a24684485e97
    role: context
  - path: data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml
    sha256: 37a54d9f76ef5c6ff47b82d4852a012c27e62412d542e7e351cbf351bdbb6fc4
    role: context
  - path: data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml
    sha256: a650f624eca66433eda385fe89540aa42d5e2116b8cdd6f5af761e77b90c9478
    role: context
  - path: data/natural_products/terpenoids/secobotrytriendiol.yaml
    sha256: acd560fe75765a0826a9cdbebef3eee34e941dea669b57b331da785a71da0760
    role: context
  - path: data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml
    sha256: 8ef90288327387e143f9995ee7eef0e33ce55a8c01d323b9aeb2f0f603b01f70
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
  selection: Campaign path order 2281; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-79ce4aca52
targets:
- target_id: naturalproductmech:mibig-79ce4aca52
  path: data/natural_products/terpenoids/botryendial.yaml
  label: Botryendial
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
  - naturalproductmech:mibig-79ce4aca52
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
  - naturalproductmech:mibig-79ce4aca52
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
  - naturalproductmech:mibig-79ce4aca52
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
  - naturalproductmech:mibig-79ce4aca52
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
  - naturalproductmech:mibig-79ce4aca52
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
  - naturalproductmech:mibig-79ce4aca52
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-79ce4aca52
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-79ce4aca52
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2281-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/botryendial.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: Complete current owner and all 2 history entries personally read; native
    curation_status remains SEEDED.
  snapshot_sha256: 3c5281cc27c72cdcd4b4c0ff933483687532e1be9378618a7cf209a691a98761
- evidence_id: bgc-2281-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json
  locator: /records/0/owner_pin; /records/0/owner_document
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: Exact complete captured owner, including all written fields and history.
  snapshot_sha256: c19fe825f5846fe8372e2f5c050eeabb32956de4867a1840e7c835ecf74003b1
- evidence_id: bgc-2281-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/intakes/2281-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: Actual canonical one-record intake for naturalproductmech:mibig-79ce4aca52,
    with 57 current source inputs and explicit maintained field ownership.
  snapshot_sha256: 0742e200e5c2524ba0ce7f959833fc047407b09ec1a59cd1270563406cee098c
- evidence_id: bgc-2281-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/root-intake-ready-001.json
  locator: /status; /intake_summary; /source_placements; /unique_source_paths; /selection_and_complete_owner_equality
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: ROOT accepts the original ten canonical intakes and their exact current
    owner/input maps.
  snapshot_sha256: 1b60455490dbc60704a7f7a0ff7e5b04ec2263c9b06d4d0b3dbbbc45596f141c
- evidence_id: bgc-2281-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete written identity, grounding and source provenance: {"chemical_structure":{"smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi":"InChI=1S/C17H24O4/c1-10-6-13(21-11(2)20)15-14(12(10)7-18)17(5,9-19)8-16(15,3)4/h7,9-10,13,15H,6,8H2,1-5H3/t10-,13+,15-,17-/m1/s1","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000631"},"grounding_notes":"No
    3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-79ce4aca52","label":"Botryendial","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-79ce4aca52","source":"MIBIG","source_id":"BGC0000631","source_label":"Botryendial","source_version":"5"}],"xrefs":["npatlas:NPA007962"]}'
  snapshot_sha256: c19fe825f5846fe8372e2f5c050eeabb32956de4867a1840e7c835ecf74003b1
- evidence_id: bgc-2281-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete written producer and locus claims with separate grades: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0000631","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"5","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0000631 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1016/0031-9422(95)00643-5"}],"genome_accession":"genbank:CP009816.1","link_evidence_basis":"CLUSTER_DEMONSTRATED","locus_evidence_methods":["Knock-out
    studies"],"locus_from":2216500,"locus_to":2246000,"organism_label":"Botrytis cinerea
    B05.10","organism_taxon_id":"NCBITaxon:332648"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0000631","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0000631 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1016/0031-9422(95)00643-5"}],"evidence_basis":"BGC_CHARACTERIZED","notes":"Locus
    evidence: Knock-out studies. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED;
    this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"5","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis
    cinerea B05.10"}],"producer_taxon_groups":["FUNGAL"]}'
  snapshot_sha256: c19fe825f5846fe8372e2f5c050eeabb32956de4867a1840e7c835ecf74003b1
- evidence_id: bgc-2281-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete written occurrences; omitted fields are absent in this complete
    captured owner: {"occurrence_taxon_groups":["FUNGAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/0031-9422(95)00643-5"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis
    cinerea","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/S0040-4020(99)00032-0"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis
    cinerea","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1021/NP980104B"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis
    cinerea","taxon_source":"NCBITaxon"}]}'
  snapshot_sha256: c19fe825f5846fe8372e2f5c050eeabb32956de4867a1840e7c835ecf74003b1
- evidence_id: bgc-2281-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete owner establishes no written assay, target or mechanism roots;
    no biological absence is inferred: {}'
  snapshot_sha256: c19fe825f5846fe8372e2f5c050eeabb32956de4867a1840e7c835ecf74003b1
- evidence_id: bgc-2281-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Literal source BGC class and named/versioned computed classification:
    {"bgc_class":["TERPENE"],"np_classification":{"class_results":["Botryane sesquiterpenoids"],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Sesquiterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"}'
  snapshot_sha256: c19fe825f5846fe8372e2f5c050eeabb32956de4867a1840e7c835ecf74003b1
- evidence_id: bgc-2281-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/smiles/status; /records/0/inchi/status;
    /records/0/smiles/computed; /records/0/inchi/computed; /records/0/comparisons;
    /records/0/atom_correspondence
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Both saved forms parsed. Complete atom/bond/ring/stereo/motif tables were
    personally read. Saved comparison facts: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim.","smiles_to_inchi_atom_indices":[0,9,5,12,14,13,11,6,17,16,7,15,2,3,4,8,18,20,10,19,1]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"declared_structure":{"smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi":"InChI=1S/C17H24O4/c1-10-6-13(21-11(2)20)15-14(12(10)7-18)17(5,9-19)8-16(15,3)4/h7,9-10,13,15H,6,8H2,1-5H3/t10-,13+,15-,17-/m1/s1","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000631"},"inchi_formula":"C17H24O4","smiles_formula":"C17H24O4"}'
  snapshot_sha256: 87fcd140466643697a72eeee9855fbcce9cbab4c39f9a234b683bc50809610da
- evidence_id: bgc-2281-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/smiles/computed; /records/0/inchi/computed; /records/0/atom_correspondence
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: SMILES atoms 7(=O8) and 15(=O16) are aldehyde carbons, each with one hydrogen.
    The acetate is C3–O17–C18(=O19)–C20. The six- and five-membered rings share the
    C4–C5 bond. Four specified tetrahedral centres are C1 R, C3 S, C4 S and C9 S.
    The complete counterpart tables and stored atom correspondence preserve these
    represented features; no independent natural stereochemical identity is established.
  snapshot_sha256: 87fcd140466643697a72eeee9855fbcce9cbab4c39f9a234b683bc50809610da
- evidence_id: bgc-2281-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-execution-001.json
  locator: /command; /cwd; /started_at; /finished_at; /exit_code; /source; /stdout;
    /stderr; /external_requests; /retries
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: Original process receipt retains exit 0, command, clocks, source and stdout/stderr
    pins, without retries or external requests.
  snapshot_sha256: 743992f3d1155964856885c91b5f364d151a9bbc7cf2cfb13cacd7ed43132552
- evidence_id: bgc-2281-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /observer; /recorded_at; /batch; /status; /DATA; /execution; /original_tools;
    /source_adoption; /intake_ready; /original_terminal; /actual_parse_attempts; /parsed_forms;
    /records; /denied_events; /input_pin_count; /current_pins_and_capture_intake_strings_exact;
    /false_comparisons; /stderr_scope; /reading_scope; /authorization; /external_requests;
    /record_changes; /scientific_verdicts
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: ROOT accepts the original 20 stored-form parses and current inputs. The
    two original undefined-stereo warnings are global, without per-record stream attribution.
    This receipt does not establish natural identity.
  snapshot_sha256: 3380fc981ad567d2ee44084ef8ec9675d2365aa945df29bce1b4a2c9bd215edd
- evidence_id: bgc-2281-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/root-native-gates-acceptance-001.json
  locator: /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /selected_queue_rows; /strict_error_rows
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: Five local commands passed; all_native_gates_passed is false because full
    QC and OAK authority coverage remain unavailable. Selected queue entries are review
    aids, not new scientific findings.
  snapshot_sha256: 6541455b28c210e07fb0d909bc7c062af31c1c73367724db8ad863dd7b338cc2
- evidence_id: bgc-2281-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/root-source-inventory-acceptance-001.json
  locator: /observer; /recorded_at; /status; /inventory; /execution; /original_tools;
    /source_adoption; /original_terminal; /root_saved_execution_metadata_and_scope_reading;
    /verification; /scope; /actual229_target_authorities; /external_requests; /target_invocations_by_observer
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: ROOT accepts the original retained source inventory and current maps; complete
    source-payload meaning is separately attributed.
  snapshot_sha256: 1933ea3b15ed9e2862e35aa69aedcacee2dc9b0caabaefdea96b47895d212e9c
- evidence_id: bgc-2281-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/0; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: Accepted source plan retains the exact owner and context/input roles within
    414 source placements and 72 unique paths.
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: bgc-2281-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/root-input-plan-acceptance-001.json
  locator: /status; /input_plan; /source_notes; /source_placements; /unique_source_paths;
    /selected_reader_orders
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: ROOT accepts the actual source plan and its input/owner joins; no selected
    maintained reader applies.
  snapshot_sha256: 788133f553f90cd741c62f133484bb771e3f84cf815c49abe689e4b178958fb2
- evidence_id: bgc-2281-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-scope-notes-001.json
  locator: /reading; /curation; /cautions
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: Complete personal and delegated retained-source readings, exact prior raw/history
    carries, curation scope and limitations are explicitly attributed. No fresh external
    source access is implied.
  snapshot_sha256: d00fa7ab4a0f2141a9b2feb6db406422149c1a23eb7a8c0a140ba26724474b1f
- evidence_id: bgc-2281-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /records/0/direct_companion_paths; /records/0/direct_companion_predicates
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Exact one-hop context predicates, without mechanism, activity or identity
    transfer: {"direct_companion_paths":["data/natural_products/terpenoids/1-epibotrydial.yaml","data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml","data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml","data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml","data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml","data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml","data/natural_products/terpenoids/8-9-epibotrydial.yaml","data/natural_products/terpenoids/botrydial.yaml","data/natural_products/terpenoids/botrydienal.yaml","data/natural_products/terpenoids/botryenalol.yaml","data/natural_products/terpenoids/dehydrobotrydienol.yaml","data/natural_products/terpenoids/dihydrobotrydial.yaml","data/natural_products/terpenoids/norbotrydialone-acetate.yaml","data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml","data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml","data/natural_products/terpenoids/secobotrytriendiol.yaml","data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/terpenoids/1-epibotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/8-9-epibotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botrydienal.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botryenalol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/dehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/dihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/norbotrydialone-acetate.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrytriendiol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]}]}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete retained predicate/query frame and physical matched payloads:
    {"matches":[{"last_physical_line":734,"physical_line":734,"raw_tsv_record":"BGC0000631\t5\tactive\tquestionable\tcomplete\tBotryendial\t8\tC[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C\tInChI=1S/C17H24O4/c1-10-6-13(21-11(2)20)15-14(12(10)7-18)17(5,9-19)8-16(15,3)4/h7,9-10,13,15H,6,8H2,1-5H3/t10-,13+,15-,17-/m1/s1\tQWZKEROSOALLJP-BYLNDYCFSA-N\ttrue\t\tnpatlas:NPA007962\tNCBITaxon:332648\tBotrytis
    cinerea B05.10\tterpene\tSesquiterpene\tCP009816.1\t2216500\t2246000\tKnock-out
    studies\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tDOI:10.1016/0031-9422(95)00643-5\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Sesquiterpene","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"8","compound_name":"Botryendial","database_ids":"npatlas:NPA007962","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"CP009816.1","locus_evidence_methods":"Knock-out
    studies","locus_from":"2216500","locus_to":"2246000","mibig_accession":"BGC0000631","primary_reference":"DOI:10.1016/0031-9422(95)00643-5","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi":"InChI=1S/C17H24O4/c1-10-6-13(21-11(2)20)15-14(12(10)7-18)17(5,9-19)8-16(15,3)4/h7,9-10,13,15H,6,8H2,1-5H3/t10-,13+,15-,17-/m1/s1","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis
    cinerea B05.10"},"row_sha256":"e388a60bd1548fd47c646b0409d678e7a25cdfde77f9cc86215049bbfa922dcd"}],"predicate":"exact
    complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 734–734; row_sha256 e388a60bd1548fd47c646b0409d678e7a25cdfde77f9cc86215049bbfa922dcd
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete physical source payloads, all fields read and joined to the current
    pinned table: [{"bgc_classes":"terpene","bgc_subclasses":"Sesquiterpene","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"8","compound_name":"Botryendial","database_ids":"npatlas:NPA007962","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"CP009816.1","locus_evidence_methods":"Knock-out
    studies","locus_from":"2216500","locus_to":"2246000","mibig_accession":"BGC0000631","primary_reference":"DOI:10.1016/0031-9422(95)00643-5","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi":"InChI=1S/C17H24O4/c1-10-6-13(21-11(2)20)15-14(12(10)7-18)17(5,9-19)8-16(15,3)4/h7,9-10,13,15H,6,8H2,1-5H3/t10-,13+,15-,17-/m1/s1","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis
    cinerea B05.10"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2281-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete retained predicate/query frame and physical matched payloads:
    {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete retained predicate/query frame and physical matched payloads:
    {"matches":[{"last_physical_line":7581,"physical_line":7581,"raw_tsv_record":"QWZKEROSOALLJP-BYLNDYCFSA-N\tBotrytis
    cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1016/0031-9422(95)00643-5\thttp://www.wikidata.org/entity/Q77420122\n","row":{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(95)00643-5","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"},"row_sha256":"f55ad3ec58d89fb76092d9668edfb08a32664d8f663741c0a99d039202ba77e6"},{"last_physical_line":7582,"physical_line":7582,"raw_tsv_record":"QWZKEROSOALLJP-BYLNDYCFSA-N\tBotrytis
    cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1016/S0040-4020(99)00032-0\thttp://www.wikidata.org/entity/Q77420122\n","row":{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/S0040-4020(99)00032-0","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"},"row_sha256":"bd2f6fd35f9cfb8fcef13a753e33a4f82767978486b5b063064adbb96e40e612"},{"last_physical_line":7583,"physical_line":7583,"raw_tsv_record":"QWZKEROSOALLJP-BYLNDYCFSA-N\tBotrytis
    cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1021/NP980104B\thttp://www.wikidata.org/entity/Q77420122\n","row":{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1021/NP980104B","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"},"row_sha256":"493307ca675b1f90dae440299ddc7dddbe33d0dbc0d9aaabc4711d6d94f63b8f"}],"predicate":"exact
    complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 7581–7581; row_sha256 f55ad3ec58d89fb76092d9668edfb08a32664d8f663741c0a99d039202ba77e6;
    physical lines 7582–7582; row_sha256 bd2f6fd35f9cfb8fcef13a753e33a4f82767978486b5b063064adbb96e40e612;
    physical lines 7583–7583; row_sha256 493307ca675b1f90dae440299ddc7dddbe33d0dbc0d9aaabc4711d6d94f63b8f
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete physical source payloads, all fields read and joined to the current
    pinned table: [{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(95)00643-5","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"},{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/S0040-4020(99)00032-0","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"},{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1021/NP980104B","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77420122","taxon_id":"NCBITaxon:40559"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2281-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete retained predicate/query frame and physical matched payloads:
    {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete retained predicate/query frame and physical matched payloads:
    {"matches":[{"last_physical_line":2055,"physical_line":2055,"raw_tsv_record":"QWZKEROSOALLJP-BYLNDYCFSA-N\tC[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C\tTerpenoids\tSesquiterpenoids\tBotryane
    sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Botryane
    sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","superclass_results":"Sesquiterpenoids"},"row_sha256":"7bed2ac4fda04a45bda1ecee0d99a126135016a86e684cfd8bfdb2294604e659"}],"predicate":"exact
    complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 2055–2055; row_sha256 7bed2ac4fda04a45bda1ecee0d99a126135016a86e684cfd8bfdb2294604e659
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete physical source payloads, all fields read and joined to the current
    pinned table: [{"class_results":"Botryane sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1C=O)[C@@](CC2(C)C)(C)C=O)OC(=O)C","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N","superclass_results":"Sesquiterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2281-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete retained predicate/query frame and physical matched payloads:
    {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete retained predicate/query frame and physical matched payloads:
    {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete retained predicate/query frame and physical matched payloads:
    {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QWZKEROSOALLJP-BYLNDYCFSA-N"}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Complete retained predicate/query frame and physical matched payloads:
    {"matches":[],"predicate":"exact chebi_id from exact full-key structure rows","query":[]}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/source_taxa; /contexts/13/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/13/source_scope_inventory/nonorganism_matches; /contexts/13/source_scope_inventory/actual_assay_rows;
    /contexts/13/source_scope_inventory/blank_AID_sentinels; /contexts/13/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Exact source taxa and complete route lists; blank AIDs are distinguished
    from actual assays: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:332648","NCBITaxon:40559"]}'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/unmatched_ids; /cached_taxonomy/whole_stanzas/4;
    /cached_taxonomy/whole_stanzas/9
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Whole retained stanzas for this source-taxon scope, with global misses
    retained separately; no fresh taxonomy or ancestry inference: [{"complete_stanza":"[Term]\nid:
    NCBITaxon:40559\nname: Botrytis cinerea\nsynonym: \"Botryotinia fuckeliana\" EXACT
    []\nsynonym: \"Botrytis cinerea Pers., 1801\" EXACT []\nsynonym: \"Peziza fuckeliana\"
    EXACT []\nsynonym: \"Sclerotinia fuckeliana\" EXACT []\n\n","id":"NCBITaxon:40559","physical_line":18031},{"complete_stanza":"[Term]\nid:
    NCBITaxon:332648\nname: Botrytis cinerea B05.10\nsynonym: \"Botryotinia fuckeliana
    B05.10\" EXACT []\n\n","id":"NCBITaxon:332648","physical_line":83758}]'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
- evidence_id: bgc-2281-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: The completed direct-open, ignore-independent scan tested 92 exact cohort
    literals against eight named implemented curation tables and 93 data rows. Zero
    hits is limited to that scope. Reserved decisions.tsv was not consumed; PubChem
    exclusions were only a supplementary reading dependency because no actual AID
    matched.
  snapshot_sha256: d00fa7ab4a0f2141a9b2feb6db406422149c1a23eb7a8c0a140ba26724474b1f
- evidence_id: bgc-2281-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: ChemicalStructure preserves source SMILES and unspecified stereocentres;
    normalized keys have explicit limits. ComputedClassification is named/versioned
    model output, not source assertion or admission evidence.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2281-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: The maintained extractor derives stereo_complete only from FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False)
    and question-mark tags; it does not test every double-bond geometry. No extractor
    ran in this authoring step.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2281-origin-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 1067–1196
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: Producer and locus claims/grades are copied separately with explicit taxon
    and qualification handling. ChEBI occurrence is not promoted to production.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2281-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 974–1065
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: Minted grounding, named model prediction projection, source concepts, BGC
    classes and retained cross-references have distinct maintained roles.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2281-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole profile
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: The current profile requires claim-level evidence and all scientific dimensions
    without promoting unavailable checks.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2281-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole skill
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: The one-record review procedure requires truthful source access and completion
    limits; this review edits no source record and makes no external request.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2281-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-inventory-DATA-001.json
  locator: /contexts/0/identifier; /contexts/0/standard_inchi_key; /contexts/0/owned_bgc_ids;
    /contexts/0/complete_raw_text; /contexts/0/literal_mechanism_inventory; /contexts/1/identifier;
    /contexts/1/standard_inchi_key; /contexts/1/owned_bgc_ids; /contexts/1/complete_raw_text;
    /contexts/1/literal_mechanism_inventory; /contexts/2/identifier; /contexts/2/standard_inchi_key;
    /contexts/2/owned_bgc_ids; /contexts/2/complete_raw_text; /contexts/2/literal_mechanism_inventory;
    /contexts/3/identifier; /contexts/3/standard_inchi_key; /contexts/3/owned_bgc_ids;
    /contexts/3/complete_raw_text; /contexts/3/literal_mechanism_inventory; /contexts/4/identifier;
    /contexts/4/standard_inchi_key; /contexts/4/owned_bgc_ids; /contexts/4/complete_raw_text;
    /contexts/4/literal_mechanism_inventory; /contexts/5/identifier; /contexts/5/standard_inchi_key;
    /contexts/5/owned_bgc_ids; /contexts/5/complete_raw_text; /contexts/5/literal_mechanism_inventory;
    /contexts/6/identifier; /contexts/6/standard_inchi_key; /contexts/6/owned_bgc_ids;
    /contexts/6/complete_raw_text; /contexts/6/literal_mechanism_inventory; /contexts/7/identifier;
    /contexts/7/standard_inchi_key; /contexts/7/owned_bgc_ids; /contexts/7/complete_raw_text;
    /contexts/7/literal_mechanism_inventory; /contexts/8/identifier; /contexts/8/standard_inchi_key;
    /contexts/8/owned_bgc_ids; /contexts/8/complete_raw_text; /contexts/8/literal_mechanism_inventory;
    /contexts/9/identifier; /contexts/9/standard_inchi_key; /contexts/9/owned_bgc_ids;
    /contexts/9/complete_raw_text; /contexts/9/literal_mechanism_inventory; /contexts/10/identifier;
    /contexts/10/standard_inchi_key; /contexts/10/owned_bgc_ids; /contexts/10/complete_raw_text;
    /contexts/10/literal_mechanism_inventory; /contexts/11/identifier; /contexts/11/standard_inchi_key;
    /contexts/11/owned_bgc_ids; /contexts/11/complete_raw_text; /contexts/11/literal_mechanism_inventory;
    /contexts/12/identifier; /contexts/12/standard_inchi_key; /contexts/12/owned_bgc_ids;
    /contexts/12/complete_raw_text; /contexts/12/literal_mechanism_inventory; /contexts/25/identifier;
    /contexts/25/standard_inchi_key; /contexts/25/owned_bgc_ids; /contexts/25/complete_raw_text;
    /contexts/25/literal_mechanism_inventory; /contexts/26/identifier; /contexts/26/standard_inchi_key;
    /contexts/26/owned_bgc_ids; /contexts/26/complete_raw_text; /contexts/26/literal_mechanism_inventory;
    /contexts/28/identifier; /contexts/28/standard_inchi_key; /contexts/28/owned_bgc_ids;
    /contexts/28/complete_raw_text; /contexts/28/literal_mechanism_inventory; /contexts/29/identifier;
    /contexts/29/standard_inchi_key; /contexts/29/owned_bgc_ids; /contexts/29/complete_raw_text;
    /contexts/29/literal_mechanism_inventory; /contexts/30/identifier; /contexts/30/standard_inchi_key;
    /contexts/30/owned_bgc_ids; /contexts/30/complete_raw_text; /contexts/30/literal_mechanism_inventory;
    /contexts/31/identifier; /contexts/31/standard_inchi_key; /contexts/31/owned_bgc_ids;
    /contexts/31/complete_raw_text; /contexts/31/literal_mechanism_inventory; /contexts/32/identifier;
    /contexts/32/standard_inchi_key; /contexts/32/owned_bgc_ids; /contexts/32/complete_raw_text;
    /contexts/32/literal_mechanism_inventory
  accessed_at: '2026-11-03T19:41:29.610497Z'
  support: supports
  summary: 'Direct compounds retain distinct complete keys. Whole companion raw/history
    reading and exact prior carries are attributed in the source notes. Unselected
    Botrydial or Trichobrasilenol mechanism/protein assertions remain context only.
    Exact identities and literal graph scopes: [{"identifier":"naturalproductmech:mibig-acc775e1b7","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"SJFIYVCSGNWVPJ-SDLFRHKASA-N"},{"identifier":"naturalproductmech:mibig-1e06238f05","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"MBHVNAKPTPFWNG-MYFMSEKESA-N"},{"identifier":"naturalproductmech:mibig-7950af79c1","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"QUGYVDURDBEQRB-VZJVBFQISA-N"},{"identifier":"naturalproductmech:mibig-e2d62600f5","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"MFOUCDNLAFNKML-SVLWDWOGSA-N"},{"identifier":"naturalproductmech:mibig-7b45e48275","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"CAMCSBCRRUTMEK-OAHLLOKOSA-N"},{"identifier":"naturalproductmech:mibig-8b4cd14741","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"PCEVLQFNPPWJEB-RFAUZJTJSA-N"},{"identifier":"naturalproductmech:mibig-bbb6f44666","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"JUCMRFKOKIZVPS-OAHLLOKOSA-N"},{"identifier":"naturalproductmech:mibig-10fda622fe","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"YPJRKTIWVUVMDI-LSDHHAIUSA-N"},{"identifier":"naturalproductmech:mibig-0bd6ab53bc","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"RVXLTRZIAMMATE-JMTSMVSISA-N"},{"identifier":"naturalproductmech:mibig-a2b74a45ae","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"SJFIYVCSGNWVPJ-PQVRDHEWSA-N"},{"identifier":"CHEBI:3159","literal_mechanism_inventory":{"edges":10,"graph_ids":["botrydial-bcbot-biosynthesis"],"graph_reference_placements":30,"graph_refs":[],"graphs":1,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":11,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"SJFIYVCSGNWVPJ-GKKOWQTJSA-N"},{"identifier":"naturalproductmech:mibig-a1c6942987","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"CFAMAVBUWMXYLX-MEBBXXQBSA-N"},{"identifier":"naturalproductmech:mibig-d567f1a1cd","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"DSVSTMJOGQEZJX-BYLNDYCFSA-N"},{"identifier":"naturalproductmech:mibig-247120aa23","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"UQQKKLVKVVJDEX-OAHLLOKOSA-N"},{"identifier":"naturalproductmech:mibig-b5ca742a5e","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N"},{"identifier":"naturalproductmech:mibig-9b040d7e03","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"OMZUEHMZFLBHNI-PCKWUFTNSA-N"},{"identifier":"naturalproductmech:mibig-2cef442430","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"GYABYKLKVQPSPD-NVWZYQMFSA-N"},{"identifier":"naturalproductmech:mibig-f478b3a4f7","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"GNMCOKDZWITFBO-MGNGBMTDSA-N"},{"identifier":"naturalproductmech:mibig-ff72b656ae","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"BHNACKMCMDASDB-UJNBGNEJSA-N"},{"identifier":"naturalproductmech:mibig-1c14174a30","literal_mechanism_inventory":{"edges":0,"graph_ids":[],"graph_reference_placements":0,"graph_refs":[],"graphs":0,"molecular_target_reference_placements":0,"molecular_targets":0,"nodes":0,"pathway_reference_placements":0,"pathway_steps":0},"owned_bgc_ids":["BGC0000631"],"standard_inchi_key":"WLPOYIWCPMYYGM-KGRKPJGKSA-N"}]'
  snapshot_sha256: 70ff45fba7b447080f1402810ebb9e57138b2077ba92f4af4efeba4e4b3c8ad4
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
- assessment_id: bgc-2281-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The MINTED identifier retains the exact complete key QWZKEROSOALLJP-BYLNDYCFSA-N
    and source name from BGC0000631 version 5, compound index 8. The exact retained
    ChEBI structure join is empty, supporting the bounded minted-grounding explanation.
    Both saved forms reproduce C17H24O4 and the declared standardized key. Distinct
    direct congeners and their mechanisms do not resolve natural identity or justify
    a structure substitution.
  target_ids:
  - naturalproductmech:mibig-79ce4aca52
  evidence_ids:
  - bgc-2281-grounding-owner
  - bgc-2281-source-mibig_compounds
  - bgc-2281-query-chebi_structures
  - bgc-2281-chemistry
  - bgc-2281-direct-contexts
  - bgc-2281-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: QWZKEROSOALLJP-BYLNDYCFSA-N; exact complete retained MIBiG key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2281-grounding-owner
    - bgc-2281-source-mibig_compounds
    - bgc-2281-query-chebi_structures
    - bgc-2281-chemistry
    - bgc-2281-direct-contexts
    - bgc-2281-companion-boundaries
  - name: grounding_scope
    value: MINTED; no exact retained ChEBI structure match or congener substitution.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2281-grounding-owner
    - bgc-2281-source-mibig_compounds
    - bgc-2281-query-chebi_structures
    - bgc-2281-chemistry
    - bgc-2281-direct-contexts
    - bgc-2281-companion-boundaries
- assessment_id: bgc-2281-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both saved forms are neutral C17H24O4 with 21 atoms, 22 bonds and one fragment.
    Four tetrahedral centres are specified with no unspecified potential centre in
    the saved tables. The two aldehydes, acetate and six/five-membered bicyclic framework
    are explicit. All ten comparison flags and the stored correspondence agree, while
    full_graph_identity_established remains false. The true stereo_complete flag is
    consistent with its centre-based scope, without establishing an experimentally
    verified natural stereoisomer.
  target_ids:
  - naturalproductmech:mibig-79ce4aca52
  evidence_ids:
  - bgc-2281-grounding-owner
  - bgc-2281-chemistry
  - bgc-2281-topology
  - bgc-2281-diagnostic-acceptance
  - bgc-2281-structure-schema
  - bgc-2281-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Four specified tetrahedral centres; no unspecified potential centre.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2281-grounding-owner
    - bgc-2281-chemistry
    - bgc-2281-topology
    - bgc-2281-diagnostic-acceptance
    - bgc-2281-structure-schema
    - bgc-2281-stereo-method
  - name: representation_correspondence
    value: Ten true comparison flags and complete stored correspondence; no independent
      full-graph/natural identity.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2281-grounding-owner
    - bgc-2281-chemistry
    - bgc-2281-topology
    - bgc-2281-diagnostic-acceptance
    - bgc-2281-structure-schema
    - bgc-2281-stereo-method
- assessment_id: bgc-2281-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: BGC0000631 version 5 is active, questionable quality and complete in the
    retained source. Botrytis cinerea B05.10 (332648) has BGC_CHARACTERIZED producer
    support; Knock-out studies separately grade the locus CLUSTER_DEMONSTRATED. The
    retained interval is CP009816.1:2216500–2246000. The strain remains distinct from
    species-level 40559 occurrences. Cached Botryotinia fuckeliana/Botrytis cinerea
    synonyms preserve retained name continuity without fresh taxonomy or production
    verification.
  target_ids:
  - naturalproductmech:mibig-79ce4aca52
  evidence_ids:
  - bgc-2281-origin-owner
  - bgc-2281-source-mibig_compounds
  - bgc-2281-cached-taxonomy
  - bgc-2281-source-routes
  - bgc-2281-origin-seeder
  - bgc-2281-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: B05.10 strain 332648 versus species 40559 occurrence; retained synonym
      scope.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2281-origin-owner
    - bgc-2281-source-mibig_compounds
    - bgc-2281-cached-taxonomy
    - bgc-2281-source-routes
    - bgc-2281-origin-seeder
    - bgc-2281-companion-boundaries
  - name: producer_evidence
    value: BGC_CHARACTERIZED for Botrytis cinerea B05.10.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2281-origin-owner
    - bgc-2281-source-mibig_compounds
    - bgc-2281-cached-taxonomy
    - bgc-2281-source-routes
    - bgc-2281-origin-seeder
    - bgc-2281-companion-boundaries
  - name: locus_evidence
    value: BGC0000631 v5 active/questionable/complete; Knock-out studies, CLUSTER_DEMONSTRATED.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2281-origin-owner
    - bgc-2281-source-mibig_compounds
    - bgc-2281-cached-taxonomy
    - bgc-2281-source-routes
    - bgc-2281-origin-seeder
    - bgc-2281-companion-boundaries
- assessment_id: bgc-2281-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: DOI:10.1016/0031-9422(95)00643-5 is explicitly COMPOUND_EVIDENCE for Botryendial
    in MIBiG and is reused in written producer/locus evidence as DATABASE_ASSERTION.
    The same DOI also appears among three LOTUS occurrence assertions, alongside 10.1016/S0040-4020(99)00032-0
    and 10.1021/NP980104B. These are retained citation placements, not verified independent
    experiments. Other Botry-family compound citations and Botrydial graph evidence
    remain separate.
  target_ids:
  - naturalproductmech:mibig-79ce4aca52
  evidence_ids:
  - bgc-2281-origin-owner
  - bgc-2281-occurrence-owner
  - bgc-2281-source-mibig_compounds
  - bgc-2281-query-lotus_occurrences
  - bgc-2281-source-notes
  - bgc-2281-direct-contexts
  - bgc-2281-companion-boundaries
  dimensions:
  - name: citation_scope
    value: COMPOUND_EVIDENCE DOI and three LOTUS citation placements; no study independence
      inferred.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2281-origin-owner
    - bgc-2281-occurrence-owner
    - bgc-2281-source-mibig_compounds
    - bgc-2281-query-lotus_occurrences
    - bgc-2281-source-notes
    - bgc-2281-direct-contexts
    - bgc-2281-companion-boundaries
- assessment_id: bgc-2281-bioactivity
  area: evidence
  topic: Occurrence and activity
  outcome: supported
  summary: Three LOTUS assertions place Botryendial in species-level Botrytis cinerea
    (40559); they do not by themselves establish B05.10 production or three independent
    experiments. The retained exact PubChem query is empty. There are no written bioactivities,
    molecular targets or mechanism roots. Exact BindingDB and AntibioticMech joins
    are empty. This bounds the saved evidence only; no biological inactivity or global
    pathway absence follows, and unselected companion mechanisms remain context.
  target_ids:
  - naturalproductmech:mibig-79ce4aca52
  evidence_ids:
  - bgc-2281-occurrence-owner
  - bgc-2281-assay-owner
  - bgc-2281-source-routes
  - bgc-2281-cached-taxonomy
  - bgc-2281-query-lotus_occurrences
  - bgc-2281-query-chebi_origins
  - bgc-2281-query-cyanometdb_occurrences
  - bgc-2281-query-pubchem_bioassay
  - bgc-2281-query-bindingdb_targets
  - bgc-2281-query-antibioticmech_inchikeys
  - bgc-2281-companion-boundaries
  dimensions:
  - name: occurrence_scope
    value: Three species-level LOTUS citation assertions; not three independent producer
      experiments.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2281-occurrence-owner
    - bgc-2281-assay-owner
    - bgc-2281-source-routes
    - bgc-2281-cached-taxonomy
    - bgc-2281-query-lotus_occurrences
    - bgc-2281-query-chebi_origins
    - bgc-2281-query-cyanometdb_occurrences
    - bgc-2281-query-pubchem_bioassay
    - bgc-2281-query-bindingdb_targets
    - bgc-2281-query-antibioticmech_inchikeys
    - bgc-2281-companion-boundaries
  - name: assay_target_scope
    value: No written activity/targets and bounded empty assay/target joins; no inactivity
      claim.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2281-occurrence-owner
    - bgc-2281-assay-owner
    - bgc-2281-source-routes
    - bgc-2281-cached-taxonomy
    - bgc-2281-query-lotus_occurrences
    - bgc-2281-query-chebi_origins
    - bgc-2281-query-cyanometdb_occurrences
    - bgc-2281-query-pubchem_bioassay
    - bgc-2281-query-bindingdb_targets
    - bgc-2281-query-antibioticmech_inchikeys
    - bgc-2281-companion-boundaries
- assessment_id: bgc-2281-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The source BGC class TERPENE and NPClassifier Terpenoids / Sesquiterpenoids
    / Botryane sesquiterpenoids output are separate assertions. The named model reports
    is_glycoside:false. Complete topology shows an oxygenated sesquiterpenoid framework
    with two aldehydes and an acetate, without a sugar residue or glycosidic linkage.
    This supports local applicability of the broad structural/model labels without
    proving a complete biosynthetic route or borrowing Botrydial's mechanism.
  target_ids:
  - naturalproductmech:mibig-79ce4aca52
  evidence_ids:
  - bgc-2281-classification-owner
  - bgc-2281-source-mibig_compounds
  - bgc-2281-source-npclassifier
  - bgc-2281-chemistry
  - bgc-2281-topology
  - bgc-2281-structure-schema
  - bgc-2281-classification-seeder
  dimensions:
  - name: classification_applicability
    value: Botryane/sesquiterpenoid computed label; false glycoside prediction agrees
      with absence of sugar topology.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2281-classification-owner
    - bgc-2281-source-mibig_compounds
    - bgc-2281-source-npclassifier
    - bgc-2281-chemistry
    - bgc-2281-topology
    - bgc-2281-structure-schema
    - bgc-2281-classification-seeder
- assessment_id: bgc-2281-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: All twelve scientific dimensions were assessed against the current owner/history,
    actual intake, retained source payloads and complete paired molecular tables.
    Five local commands passed, while full QC, complete OAK authority coverage and
    fresh external verification remain unavailable. No selected mechanism reader is
    applicable. The exact bounded curation scan found no matching row in its declared
    scope, without a global absence claim. No supported local curation defect was
    established; scientific completion remains partial and native curation status
    is unchanged.
  target_ids:
  - naturalproductmech:mibig-79ce4aca52
  evidence_ids:
  - bgc-2281-owner
  - bgc-2281-intake
  - bgc-2281-intake-acceptance
  - bgc-2281-inventory-acceptance
  - bgc-2281-plan
  - bgc-2281-plan-acceptance
  - bgc-2281-source-notes
  - bgc-2281-curation-scope
  - bgc-2281-diagnostic-execution
  - bgc-2281-diagnostic-acceptance
  - bgc-2281-native-acceptance
  - bgc-2281-review-profile
  - bgc-2281-review-skill
  dimensions:
  - name: review_completion
    value: Partial scientific review; local source fidelity and saved-form interpretation
      supported, natural identity/primary verification and unavailable QC/OAK unresolved.
      No curation change proposed.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2281-owner
    - bgc-2281-intake
    - bgc-2281-intake-acceptance
    - bgc-2281-inventory-acceptance
    - bgc-2281-plan
    - bgc-2281-plan-acceptance
    - bgc-2281-source-notes
    - bgc-2281-curation-scope
    - bgc-2281-diagnostic-execution
    - bgc-2281-diagnostic-acceptance
    - bgc-2281-native-acceptance
    - bgc-2281-review-profile
    - bgc-2281-review-skill
findings: []
actions: []
limitations:
- External identifiers, taxonomy, genome accessions and primary publications were
  not refreshed under the absolute no-request instruction. Historical and database
  assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and stored-form
  parsing establish only their declared mechanical scope.
- Empty joins refer only to retained exact predicates and snapshots; they do not establish
  biological absence. Shared loci, citations and congeners do not transfer compound-specific
  claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source
  records, native curation status and histories were not edited.
- Historical unselected Botrydial and Trichobrasilenol mechanisms are context-only.
  No compound-specific pathway, protein sequence, construct or activity is transferred
  to this owner.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- All current owner/history text, complete actual intake and both complete saved molecular
  tables were personally read. Retained source/companion reading and exact prior carries
  are attributed in the pinned source notes.
- The original diagnostic's two undefined-stereo warnings remain global and unassigned.
  No additional molecular/YAML parse, source query or target invocation occurred during
  authoring.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-229
```
