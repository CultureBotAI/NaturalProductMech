# Local evidence review: brevione E

- Review: 20261103T194802Z-brevione-e
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T19:22:18.978134Z
- Finished UTC: 2026-11-03T19:48:02.614351Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified partial review of Brevione E: exact selected form and distinct Isobrevione E companion are preserved; the glycoside=true prediction has an explicit applicability concern without a source-identity or schema finding.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2288; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-6295b1addd | data/natural_products/terpenoids/brevione-e.yaml | generated | brevione E |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-6295b1addd | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-6295b1addd | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-6295b1addd | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-6295b1addd | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-6295b1addd | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-6295b1addd | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-6295b1addd | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-6295b1addd | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding

identity: supported. Targets: naturalproductmech:mibig-6295b1addd.

The MINTED Brevione E owner retains MIBiG BGC0002759 version 2, source compound_index=1 and full key JNDQPDZQDHPEAE-WTAVCZOCSA-N. Its directly admitted Isobrevione E companion is source compound_index=2 with the same connectivity block but a different complete key, JNDQPDZQDHPEAE-WCVIEGAVSA-N. They remain distinct stereochemical records; a shared locus or model result does not make them synonyms. The selected exact ChEBI query is empty, and retained NPAtlas/PubChem cross-references were not independently resolved.

### Stored representation and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-6295b1addd.

Both stored forms agree on neutral C28H34O7, 35 atoms, 40 bonds, the declared Standard InChI/key and both canonical SMILES comparisons. Nine tetrahedral centres and one E double bond are specified. The SMILES centres are 3 R, 5 R, 6 S, 7 S, 8 S, 18 S, 25 S, 26 S and 28 S; bond 11 (10–12) is E, corresponding to InChI bond 20 (14–19). These are complete retained assignments compatible with the source stereo_complete flag, not an independent determination of the natural stereoisomer or of the distinct companion's stereochemistry.

### Producer, locus, taxon and strain roles

provenance: supported. Targets: naturalproductmech:mibig-6295b1addd.

MIBiG retains Penicillium bialowiezense CBS 227.28 with taxon NCBITaxon:293381 and producer SOURCE_ASSERTION. The cached stanza identifies the species, so the strain qualifier is retained source text rather than an independently strain-specific taxon resolution. BGC0002759 version 2 is active/questionable/complete, LC719581.1:1–41588, with Heterologous expression and CLUSTER_DEMONSTRATED. The locus experiment does not upgrade native producer evidence. TERPENE/PKS classes and Sesquiterpene/Iterative type I source subclasses describe their own source axis.

### Citation placement and primary-source limits

evidence: supported. Targets: naturalproductmech:mibig-6295b1addd.

DOI:10.1002/anie.202210938 is retained with MIBiG ENTRY scope for the producer/locus; the Isobrevione E companion shares this entry context but remains a distinct compound. NPAtlas NPA019168, PubChem 101092881 and the source-row ChemSpider cross-reference are historical database links, not newly checked identities. No primary isolation, heterologous construct or stereochemical experiment was retrieved. The versioned NPClassifier row is computed provenance rather than a primary chemical assertion.

### Occurrence and assay boundaries

scope: supported. Targets: naturalproductmech:mibig-6295b1addd.

The selected LOTUS, CyanometDB and matched-ChEBI-origin routes are empty and no occurrence item is written. PubChem row 3357 has CID 101092881, blank AID and '(no assay data)' with blank observation fields; this is a sentinel, not inactivity. BindingDB and sibling-corpus matches are also absent in the bounded saved queries. Neither occurrence nor pharmacology transfers from Isobrevione E merely because the BGC is shared.

### Computed classification and complete saved topology

other: concern. Targets: naturalproductmech:mibig-6295b1addd.

NPClassifier retains Terpenoids / Diterpenoids / Breviane diterpenoids and is_glycoside=true. The maintained schema explicitly makes this a named-model prediction and the seeder faithfully copies the retained true value. The complete saved graph instead establishes a densely connected polycyclic ether/acetal framework, an acetate ester and two ketones; it does not establish a distinct glycosyl residue or glycosidic substituent. The empty saturated-C5O motif list alone is not a general test for all glycosides. Thus the glycoside prediction has an unresolved applicability limitation and must not be presented as an experimentally asserted chemical class. No source-identity defect, schema violation, or justified replacement value follows from this local review; the literal model result is preserved.

### Review completion and unavailable verification

completeness: unknown. Targets: naturalproductmech:mibig-6295b1addd.

The complete owner/history, actual 38-input intake, nine saved query frames, 3 positive source placements, applicable cached taxonomy and both complete original molecular forms were reviewed. No causal_graphs, causal_graph_refs, biosynthetic_pathway or molecular_targets root is present; no selected maintained-reader route applies. Five local gates and original chemistry have ROOT acceptance. FullQC, full OAK and fresh primary/identifier/taxonomy verification remain unavailable, so this is a qualified partial review and does not promote SEEDED status. Optional mechanism absence is not proof that biosynthesis is unknown in the literature.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2288-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/brevione-e.yaml; lines 1–81 | supports | Whole current plaintext owner and all 2 history events; exact identifier naturalproductmech:mibig-6295b1addd, label brevione E and full key JNDQPDZQDHPEAE-WTAVCZOCSA-N. Retained annotations are not fresh primary verification. |
| support-2288-capture | /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json; /records/7/owner_document; /records/7/owner_pin | supports | Complete accepted captured owner and current raw pin, including all present claims and history. |
| support-2288-source-plan | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7 | supports | Complete admitted selected context, nine saved query frames/full payloads and 38 planned inputs. Plan acceptance establishes scope, not scientific truth. |
| support-2288-intake | /private/tmp/npm-review-work/shared-next-batch229/intakes/2288-inspect-001.json; /targets; /source; /status | supports | Complete actual inspection-only intake, exact target, maintained owners and current context inputs. |
| support-2288-intake-ready | /private/tmp/npm-review-work/shared-next-batch229/root-intake-ready-001.json; /observer; /recorded_at; /batch; /status; /intake_summary; /execution; /original_tools; /selection_ready; /input_plan_acceptance; /native_acceptance; /original_terminal; /ROOT_readback; /source_placements; /unique_source_paths; /per_order_counts; /selection_and_complete_owner_equality; /mechanism_owner_orders; /required_component_inputs; /maintained_reader_invocations; /authorization; /external_requests; /record_changes; /scientific_verdicts | supports | ROOT acceptance of the original ten canonical intakes and their exact input maps; no scientific verdict supplied. |
| support-2288-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch229/root-input-plan-acceptance-001.json; /observer; /recorded_at; /batch; /status; /input_plan; /derivation; /source_notes; /source_adoption; /composer_execution; /composer_original_tools; /selection_ready; /original_terminal; /metadata_and_derivation_reading; /notes_whole_reading; /ROOT_current_input_and_whole_derivation_check; /source_placements; /unique_source_paths; /per_order_counts; /selected_records; /unselected_direct_contexts; /direct_companion_placements; /additional_context_placements; /selected_reader_orders; /components; /all_selected_mechanism_roots_absent; /assay_rows; /blank_AID_sentinels; /forward_merge_orders; /future_actual_roles_unbound; /authorization; /limitations; /external_requests; /record_changes; /scientific_verdicts | supports | ROOT acceptance of the original actual input plan, complete maps and current source bytes. |
| support-2288-source-notes | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-source-scope-notes-001.json; /observer; /recorded_at; /batch; /status; /inventory; /inventory_ROOT_acceptance; /inventory_ROOT_acceptance_inventory_key; /collector_source; /collector_source_adoption; /collector_execution; /collector_original_tools; /collector_original_terminal; /prior_final_acceptance; /prior_final_expected_status; /accepted_prior_remaining; /frozen_remaining; /actual_frozen229_remaining; /requirements; /selected_profile; /totals; /per_order_input_counts; /reading; /curation; /cautions; /current_inventory_input_pin_count; /future_actual_roles; /selected_reader_orders; /scientific_verdicts; /external_requests; /source_records_modified; /target_invocations_by_this_step | supports | Complete source-reading attribution, exact retained routes, source cautions and bounded implemented-curation scan; no new primary observation. |
| support-2288-chemistry | /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/smiles/computed; /records/7/inchi/computed; /records/7/comparisons; /records/7/atom_correspondence | supports | All ten saved comparison flags are true, with declared full key retained; the stored correspondence explicitly does not independently establish full graph or natural identity. |
| support-2288-topology | /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed; /records/7/inchi/computed | supports | The complete saved graph has six reported cycles, three internal C–O–C bridges (SMILES O4, O11, O17), and an acetate ester through O19–C20=O22. The other carbonyls are C14=O16 and C30=O34. There are no saturated six-membered C5O candidate cycles; internal acetal/ether connectivity is explicit, but no distinct glycosyl residue is established from these tables. All nine tetrahedral assignments and the specified E double bond were read. |
| support-2288-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/root-diagnostic-acceptance-001.json; /observer; /recorded_at; /batch; /status; /DATA; /execution; /original_tools; /source_adoption; /intake_ready; /original_terminal; /actual_parse_attempts; /parsed_forms; /records; /denied_events; /input_pin_count; /current_pins_and_capture_intake_strings_exact; /false_comparisons; /stderr_scope; /reading_scope; /authorization; /external_requests; /record_changes; /scientific_verdicts | supports | ROOT acceptance of the original twenty-form observation and current pins; two original undefined-stereo warnings remain global and unassigned. |
| support-2288-native-acceptance | /private/tmp/npm-review-work/shared-next-batch229/root-native-gates-acceptance-001.json; /observer; /recorded_at; /batch; /status; /execution; /original_tools; /source_adoption; /selection_ready; /original_terminal; /ROOT_reading; /observer_recovery; /strict_selected_files; /strict_full_files; /strict_error_rows; /reproduction_records; /reproduction_byte_identical; /queue_rows; /queue_categories; /selected_queue_rows; /all_checked_input_bytes_unchanged; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /external_requests; /record_changes; /scientific_verdicts | supports | ROOT acceptance of five original local gates; FullQC and full OAK are explicitly unavailable, not passed. |
| support-2288-classification-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 375–432 | supports | The schema states Standard InChIKey limitations, the undefined-stereocentre flag scope, and that ComputedClassification is a versioned model result, never a source assertion. |
| support-2288-structure-extractor | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–173 | supports | Maintained structure_fields computes the stereo flag from FindMolChiralCenters(includeUnassigned=True); this is a tetrahedral-centre convention, not experimental stereochemical verification. |
| support-2288-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 990–1025 | supports | The seeder retains source structure strings/stereo flag and copies the named NPClassifier row, model version and boolean glycoside result into computed classification. |
| support-2288-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/source_scope_inventory/joins/mibig_compounds | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N"; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2288-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; lines 3413–3413 | supports | Complete retained source payload: {"mibig_accession":"BGC0002759","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"brevione E","compound_index":"1","smiles":"CC1=C[C@](O2)([H])[C@@]3([H])[C@]4([C@]15[C@@](C/C(O5)=C(C)\\C(C)=O)([H])O[C@H]4OC(C)=O)CC[C@]6([H])[C@]3(C)[C@]2([H])CC(C=C6C)=O","standard_inchi":"InChI=1S/C28H34O7/c1-13-9-18(31)11-22-26(6)19(13)7-8-27-24(26)21(33-22)10-14(2)28(27)23(34-25(27)32-17(5)30)12-20(35-28)15(3)16(4)29/h9-10,19,21-25H,7-8,11-12H2,1-6H3/b20-15+/t19-,21+,22-,23-,24+,25+,26+,27+,28+/m0/s1","standard_inchi_key":"JNDQPDZQDHPEAE-WTAVCZOCSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA019168&#124;pubchem:101092881&#124;chemspider:78436213","taxon_id":"NCBITaxon:293381","taxon_label":"Penicillium bialowiezense CBS 227.28","bgc_classes":"terpene&#124;PKS","bgc_subclasses":"Sesquiterpene&#124;Iterative type I","genome_accession":"LC719581.1","locus_from":"1","locus_to":"41588","locus_evidence_methods":"Heterologous expression","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"DOI:10.1002/anie.202210938","reference_basis":"ENTRY"} |
| support-2288-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/source_scope_inventory/joins/chebi_structures | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N"; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2288-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/source_scope_inventory/joins/lotus_occurrences | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N"; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2288-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N"; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2288-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/source_scope_inventory/joins/npclassifier | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N"; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2288-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; lines 1137–1137 | supports | Complete retained source payload: {"standard_inchi_key":"JNDQPDZQDHPEAE-WTAVCZOCSA-N","smiles":"CC1=C[C@](O2)([H])[C@@]3([H])[C@]4([C@]15[C@@](C/C(O5)=C(C)\\C(C)=O)([H])O[C@H]4OC(C)=O)CC[C@]6([H])[C@]3(C)[C@]2([H])CC(C=C6C)=O","pathway_results":"Terpenoids","superclass_results":"Diterpenoids","class_results":"Breviane diterpenoids","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07"} |
| support-2288-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/source_scope_inventory/joins/pubchem_bioassay | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N"; positive placements=1. Zero matches are bounded to this snapshot. |
| support-2288-row-pubchem_bioassay-0 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; lines 3357–3357 | supports | Complete retained source payload: {"standard_inchi_key":"JNDQPDZQDHPEAE-WTAVCZOCSA-N","cid":"101092881","aid":"","assay_name":"(no assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""} |
| support-2288-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/source_scope_inventory/joins/bindingdb_targets | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N"; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2288-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N"; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2288-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/source_scope_inventory/joins/chebi_origins | supports | Saved frame: predicate=exact chebi_id from exact full-key structure rows; query=[]; positive placements=0. Zero matches are bounded to this snapshot. |
| support-2288-routes | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/source_scope_inventory/matched_chebi_ids; /records/7/source_scope_inventory/source_taxa; /records/7/source_scope_inventory/forward_taxon_merge_matches; /records/7/source_scope_inventory/nonorganism_matches; /records/7/source_scope_inventory/actual_assay_rows; /records/7/source_scope_inventory/blank_AID_sentinels; /records/7/source_scope_inventory/related_corpus_rows | supports | Complete saved route fields: {"matched_chebi_ids":[],"source_taxa":["NCBITaxon:293381"],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"actual_assay_rows":[],"blank_AID_sentinels":[{"physical_line":3357,"last_physical_line":3357,"row":{"standard_inchi_key":"JNDQPDZQDHPEAE-WTAVCZOCSA-N","cid":"101092881","aid":"","assay_name":"(no assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""},"raw_tsv_record":"JNDQPDZQDHPEAE-WTAVCZOCSA-N\t101092881\t\t(no assay data)\t\t\t\t\t\t\t\n","row_sha256":"01a19223a75baf8563039323988c6e82599a19854dfae0bec8c0496407caaee0"}],"related_corpus_rows":[]} |
| support-2288-cache-293381 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; lines 79140–79143 | supports | Complete retained local taxonomy stanza: [Term]<br>id: NCBITaxon:293381<br>name: Penicillium bialowiezense<br><br> |
| support-2288-companions | /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json; /records/7/proposed_companion_paths; /records/7/direct_companion_predicates | supports | Exact admitted one-hop companion paths and predicates; membership alone does not transfer identity, assays or biosynthetic claims. |
| support-2288-companion-0 | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/isobrevione-e.yaml; lines 1–78 | supports | Complete exact companion plaintext/history: isobrevione E; naturalproductmech:mibig-c3a21dacb9; key JNDQPDZQDHPEAE-WCVIEGAVSA-N; owned BGCs ["BGC0002759"]; 2 history events. Distinct companion scope, not an assay or identity transfer. |
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
- The glycoside=true model prediction is retained with an explicit applicability concern; local ring motifs do not supply a comprehensive glycoside definition or justify overwriting the model output.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- All findings/actions are empty within this bounded inspected scope; this does not certify every unverified source claim or create a native REVIEWED status.
- Maintained ownership remains in the admitted inventories, implemented curation tables, extractors and seeder. The reserved decisions.tsv is not a consumed correction mechanism.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T194802Z-brevione-e
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: brevione E'
started_at: '2026-11-03T19:22:18.978134Z'
finished_at: '2026-11-03T19:48:02.614351Z'
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
summary: 'Qualified partial review of Brevione E: exact selected form and distinct
  Isobrevione E companion are preserved; the glycoside=true prediction has an explicit
  applicability concern without a source-identity or schema finding.'
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
  - path: data/natural_products/terpenoids/brevione-e.yaml
    sha256: e46b01d5ecb65b5ba90dd1c21a334145751c8d310af6689a79f1667f0ad39bd2
    role: target
  - path: data/natural_products/terpenoids/isobrevione-e.yaml
    sha256: 05882c133edbc6d74fc681cb7a9a308f9ec2b7703426e529c782da3570b9cb3b
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
  selection: Campaign path order 2288; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-6295b1addd
targets:
- target_id: naturalproductmech:mibig-6295b1addd
  path: data/natural_products/terpenoids/brevione-e.yaml
  label: brevione E
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
  - naturalproductmech:mibig-6295b1addd
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
  - naturalproductmech:mibig-6295b1addd
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
  - naturalproductmech:mibig-6295b1addd
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
  - naturalproductmech:mibig-6295b1addd
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
  - naturalproductmech:mibig-6295b1addd
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
  - naturalproductmech:mibig-6295b1addd
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-6295b1addd
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-6295b1addd
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2288-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/brevione-e.yaml
  locator: lines 1–81
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Whole current plaintext owner and all 2 history events; exact identifier
    naturalproductmech:mibig-6295b1addd, label brevione E and full key JNDQPDZQDHPEAE-WTAVCZOCSA-N.
    Retained annotations are not fresh primary verification.
  snapshot_sha256: e46b01d5ecb65b5ba90dd1c21a334145751c8d310af6689a79f1667f0ad39bd2
- evidence_id: support-2288-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/owner-capture-DATA-001.json
  locator: /records/7/owner_document; /records/7/owner_pin
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Complete accepted captured owner and current raw pin, including all present
    claims and history.
  snapshot_sha256: c19fe825f5846fe8372e2f5c050eeabb32956de4867a1840e7c835ecf74003b1
- evidence_id: support-2288-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Complete admitted selected context, nine saved query frames/full payloads
    and 38 planned inputs. Plan acceptance establishes scope, not scientific truth.
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/intakes/2288-inspect-001.json
  locator: /targets; /source; /status
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Complete actual inspection-only intake, exact target, maintained owners
    and current context inputs.
  snapshot_sha256: e38b92c0d1dd19473eeabf32c36c119d0d268afda34ab40fc989e79e42e49c5f
- evidence_id: support-2288-intake-ready
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
- evidence_id: support-2288-plan-acceptance
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
- evidence_id: support-2288-source-notes
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
- evidence_id: support-2288-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/smiles/computed; /records/7/inchi/computed;
    /records/7/comparisons; /records/7/atom_correspondence
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: All ten saved comparison flags are true, with declared full key retained;
    the stored correspondence explicitly does not independently establish full graph
    or natural identity.
  snapshot_sha256: 87fcd140466643697a72eeee9855fbcce9cbab4c39f9a234b683bc50809610da
- evidence_id: support-2288-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed; /records/7/inchi/computed
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: The complete saved graph has six reported cycles, three internal C–O–C
    bridges (SMILES O4, O11, O17), and an acetate ester through O19–C20=O22. The other
    carbonyls are C14=O16 and C30=O34. There are no saturated six-membered C5O candidate
    cycles; internal acetal/ether connectivity is explicit, but no distinct glycosyl
    residue is established from these tables. All nine tetrahedral assignments and
    the specified E double bond were read.
  snapshot_sha256: 87fcd140466643697a72eeee9855fbcce9cbab4c39f9a234b683bc50809610da
- evidence_id: support-2288-diagnostic-acceptance
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
- evidence_id: support-2288-native-acceptance
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
- evidence_id: support-2288-classification-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 375–432
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: The schema states Standard InChIKey limitations, the undefined-stereocentre
    flag scope, and that ComputedClassification is a versioned model result, never
    a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2288-structure-extractor
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–173
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Maintained structure_fields computes the stereo flag from FindMolChiralCenters(includeUnassigned=True);
    this is a tetrahedral-centre convention, not experimental stereochemical verification.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2288-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 990–1025
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: The seeder retains source structure strings/stereo flag and copies the
    named NPClassifier row, model version and boolean glycoside result into computed
    classification.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2288-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N";
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: lines 3413–3413
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"mibig_accession":"BGC0002759","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"brevione
    E","compound_index":"1","smiles":"CC1=C[C@](O2)([H])[C@@]3([H])[C@]4([C@]15[C@@](C/C(O5)=C(C)\\C(C)=O)([H])O[C@H]4OC(C)=O)CC[C@]6([H])[C@]3(C)[C@]2([H])CC(C=C6C)=O","standard_inchi":"InChI=1S/C28H34O7/c1-13-9-18(31)11-22-26(6)19(13)7-8-27-24(26)21(33-22)10-14(2)28(27)23(34-25(27)32-17(5)30)12-20(35-28)15(3)16(4)29/h9-10,19,21-25H,7-8,11-12H2,1-6H3/b20-15+/t19-,21+,22-,23-,24+,25+,26+,27+,28+/m0/s1","standard_inchi_key":"JNDQPDZQDHPEAE-WTAVCZOCSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA019168|pubchem:101092881|chemspider:78436213","taxon_id":"NCBITaxon:293381","taxon_label":"Penicillium
    bialowiezense CBS 227.28","bgc_classes":"terpene|PKS","bgc_subclasses":"Sesquiterpene|Iterative
    type I","genome_accession":"LC719581.1","locus_from":"1","locus_to":"41588","locus_evidence_methods":"Heterologous
    expression","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"DOI:10.1002/anie.202210938","reference_basis":"ENTRY"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2288-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N";
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N";
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N";
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N";
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: lines 1137–1137
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"standard_inchi_key":"JNDQPDZQDHPEAE-WTAVCZOCSA-N","smiles":"CC1=C[C@](O2)([H])[C@@]3([H])[C@]4([C@]15[C@@](C/C(O5)=C(C)\\C(C)=O)([H])O[C@H]4OC(C)=O)CC[C@]6([H])[C@]3(C)[C@]2([H])CC(C=C6C)=O","pathway_results":"Terpenoids","superclass_results":"Diterpenoids","class_results":"Breviane
    diterpenoids","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2288-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N";
    positive placements=1. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-row-pubchem_bioassay-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: lines 3357–3357
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained source payload: {"standard_inchi_key":"JNDQPDZQDHPEAE-WTAVCZOCSA-N","cid":"101092881","aid":"","assay_name":"(no
    assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""}'
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2288-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N";
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact complete standard_inchi_key equality; query="JNDQPDZQDHPEAE-WTAVCZOCSA-N";
    positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Saved frame: predicate=exact chebi_id from exact full-key structure rows;
    query=[]; positive placements=0. Zero matches are bounded to this snapshot.'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/matched_chebi_ids; /records/7/source_scope_inventory/source_taxa;
    /records/7/source_scope_inventory/forward_taxon_merge_matches; /records/7/source_scope_inventory/nonorganism_matches;
    /records/7/source_scope_inventory/actual_assay_rows; /records/7/source_scope_inventory/blank_AID_sentinels;
    /records/7/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete saved route fields: {"matched_chebi_ids":[],"source_taxa":["NCBITaxon:293381"],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"actual_assay_rows":[],"blank_AID_sentinels":[{"physical_line":3357,"last_physical_line":3357,"row":{"standard_inchi_key":"JNDQPDZQDHPEAE-WTAVCZOCSA-N","cid":"101092881","aid":"","assay_name":"(no
    assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""},"raw_tsv_record":"JNDQPDZQDHPEAE-WTAVCZOCSA-N\t101092881\t\t(no
    assay data)\t\t\t\t\t\t\t\n","row_sha256":"01a19223a75baf8563039323988c6e82599a19854dfae0bec8c0496407caaee0"}],"related_corpus_rows":[]}'
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-cache-293381
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: lines 79140–79143
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete retained local taxonomy stanza: [Term]

    id: NCBITaxon:293381

    name: Penicillium bialowiezense


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2288-companions
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch229-tentative/bgc-prep/bgc-conditional229-target-input-plan-001.json
  locator: /records/7/proposed_companion_paths; /records/7/direct_companion_predicates
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: Exact admitted one-hop companion paths and predicates; membership alone
    does not transfer identity, assays or biosynthetic claims.
  snapshot_sha256: 64486b806ec170c06bde1ff0f8c769cfbda77eeaf2fd0f2fdc98e8094f05469d
- evidence_id: support-2288-companion-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/isobrevione-e.yaml
  locator: lines 1–78
  accessed_at: '2026-11-03T19:42:26.788816Z'
  support: supports
  summary: 'Complete exact companion plaintext/history: isobrevione E; naturalproductmech:mibig-c3a21dacb9;
    key JNDQPDZQDHPEAE-WCVIEGAVSA-N; owned BGCs ["BGC0002759"]; 2 history events.
    Distinct companion scope, not an assay or identity transfer.'
  snapshot_sha256: 05882c133edbc6d74fc681cb7a9a308f9ec2b7703426e529c782da3570b9cb3b
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
- assessment_id: support-2288-A1
  area: identity
  topic: Exact structure concept and grounding
  outcome: supported
  summary: The MINTED Brevione E owner retains MIBiG BGC0002759 version 2, source
    compound_index=1 and full key JNDQPDZQDHPEAE-WTAVCZOCSA-N. Its directly admitted
    Isobrevione E companion is source compound_index=2 with the same connectivity
    block but a different complete key, JNDQPDZQDHPEAE-WCVIEGAVSA-N. They remain distinct
    stereochemical records; a shared locus or model result does not make them synonyms.
    The selected exact ChEBI query is empty, and retained NPAtlas/PubChem cross-references
    were not independently resolved.
  target_ids:
  - naturalproductmech:mibig-6295b1addd
  evidence_ids:
  - support-2288-owner
  - support-2288-capture
  - support-2288-source-plan
  - support-2288-query-mibig_compounds
  - support-2288-query-chebi_structures
  - support-2288-companions
  - support-2288-row-mibig_compounds-0
  - support-2288-companion-0
  dimensions:
  - name: standard_inchi_key
    value: JNDQPDZQDHPEAE-WTAVCZOCSA-N
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-owner
    - support-2288-capture
    - support-2288-source-plan
    - support-2288-query-mibig_compounds
    - support-2288-query-chebi_structures
    - support-2288-companions
    - support-2288-row-mibig_compounds-0
    - support-2288-companion-0
  - name: grounding_scope
    value: The MINTED Brevione E owner retains MIBiG BGC0002759 version 2, source
      compound_index=1 and full key JNDQPDZQDHPEAE-WTAVCZOCSA-N. Its directly admitted
      Isobrevione E companion is source compound_index=2 with the same connectivity
      block but a different complete key, JNDQPDZQDHPEAE-WCVIEGAVSA-N. They remain
      distinct stereochemical records; a shared locus or model result does not make
      them synonyms. The selected exact ChEBI query is empty, and retained NPAtlas/PubChem
      cross-references were not independently resolved.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-owner
    - support-2288-capture
    - support-2288-source-plan
    - support-2288-query-mibig_compounds
    - support-2288-query-chebi_structures
    - support-2288-companions
    - support-2288-row-mibig_compounds-0
    - support-2288-companion-0
- assessment_id: support-2288-A2
  area: representation
  topic: Stored representation and stereochemistry
  outcome: supported
  summary: Both stored forms agree on neutral C28H34O7, 35 atoms, 40 bonds, the declared
    Standard InChI/key and both canonical SMILES comparisons. Nine tetrahedral centres
    and one E double bond are specified. The SMILES centres are 3 R, 5 R, 6 S, 7 S,
    8 S, 18 S, 25 S, 26 S and 28 S; bond 11 (10–12) is E, corresponding to InChI bond
    20 (14–19). These are complete retained assignments compatible with the source
    stereo_complete flag, not an independent determination of the natural stereoisomer
    or of the distinct companion's stereochemistry.
  target_ids:
  - naturalproductmech:mibig-6295b1addd
  evidence_ids:
  - support-2288-owner
  - support-2288-capture
  - support-2288-chemistry
  - support-2288-topology
  - support-2288-diagnostic-acceptance
  - support-2288-classification-schema
  - support-2288-structure-extractor
  dimensions:
  - name: stereochemical_resolution
    value: Both stored forms agree on neutral C28H34O7, 35 atoms, 40 bonds, the declared
      Standard InChI/key and both canonical SMILES comparisons. Nine tetrahedral centres
      and one E double bond are specified. The SMILES centres are 3 R, 5 R, 6 S, 7
      S, 8 S, 18 S, 25 S, 26 S and 28 S; bond 11 (10–12) is E, corresponding to InChI
      bond 20 (14–19). These are complete retained assignments compatible with the
      source stereo_complete flag, not an independent determination of the natural
      stereoisomer or of the distinct companion's stereochemistry.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-owner
    - support-2288-capture
    - support-2288-chemistry
    - support-2288-topology
    - support-2288-diagnostic-acceptance
    - support-2288-classification-schema
    - support-2288-structure-extractor
  - name: representation_correspondence
    value: Both stored forms agree on neutral C28H34O7, 35 atoms, 40 bonds, the declared
      Standard InChI/key and both canonical SMILES comparisons. Nine tetrahedral centres
      and one E double bond are specified. The SMILES centres are 3 R, 5 R, 6 S, 7
      S, 8 S, 18 S, 25 S, 26 S and 28 S; bond 11 (10–12) is E, corresponding to InChI
      bond 20 (14–19). These are complete retained assignments compatible with the
      source stereo_complete flag, not an independent determination of the natural
      stereoisomer or of the distinct companion's stereochemistry.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-owner
    - support-2288-capture
    - support-2288-chemistry
    - support-2288-topology
    - support-2288-diagnostic-acceptance
    - support-2288-classification-schema
    - support-2288-structure-extractor
- assessment_id: support-2288-A3
  area: provenance
  topic: Producer, locus, taxon and strain roles
  outcome: supported
  summary: MIBiG retains Penicillium bialowiezense CBS 227.28 with taxon NCBITaxon:293381
    and producer SOURCE_ASSERTION. The cached stanza identifies the species, so the
    strain qualifier is retained source text rather than an independently strain-specific
    taxon resolution. BGC0002759 version 2 is active/questionable/complete, LC719581.1:1–41588,
    with Heterologous expression and CLUSTER_DEMONSTRATED. The locus experiment does
    not upgrade native producer evidence. TERPENE/PKS classes and Sesquiterpene/Iterative
    type I source subclasses describe their own source axis.
  target_ids:
  - naturalproductmech:mibig-6295b1addd
  evidence_ids:
  - support-2288-capture
  - support-2288-source-plan
  - support-2288-routes
  - support-2288-source-notes
  - support-2288-row-mibig_compounds-0
  - support-2288-cache-293381
  dimensions:
  - name: taxon_and_strain_scope
    value: MIBiG retains Penicillium bialowiezense CBS 227.28 with taxon NCBITaxon:293381
      and producer SOURCE_ASSERTION. The cached stanza identifies the species, so
      the strain qualifier is retained source text rather than an independently strain-specific
      taxon resolution. BGC0002759 version 2 is active/questionable/complete, LC719581.1:1–41588,
      with Heterologous expression and CLUSTER_DEMONSTRATED. The locus experiment
      does not upgrade native producer evidence. TERPENE/PKS classes and Sesquiterpene/Iterative
      type I source subclasses describe their own source axis.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-capture
    - support-2288-source-plan
    - support-2288-routes
    - support-2288-source-notes
    - support-2288-row-mibig_compounds-0
    - support-2288-cache-293381
  - name: producer_evidence_tier
    value: MIBiG retains Penicillium bialowiezense CBS 227.28 with taxon NCBITaxon:293381
      and producer SOURCE_ASSERTION. The cached stanza identifies the species, so
      the strain qualifier is retained source text rather than an independently strain-specific
      taxon resolution. BGC0002759 version 2 is active/questionable/complete, LC719581.1:1–41588,
      with Heterologous expression and CLUSTER_DEMONSTRATED. The locus experiment
      does not upgrade native producer evidence. TERPENE/PKS classes and Sesquiterpene/Iterative
      type I source subclasses describe their own source axis.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-capture
    - support-2288-source-plan
    - support-2288-routes
    - support-2288-source-notes
    - support-2288-row-mibig_compounds-0
    - support-2288-cache-293381
  - name: locus_evidence_tier
    value: MIBiG retains Penicillium bialowiezense CBS 227.28 with taxon NCBITaxon:293381
      and producer SOURCE_ASSERTION. The cached stanza identifies the species, so
      the strain qualifier is retained source text rather than an independently strain-specific
      taxon resolution. BGC0002759 version 2 is active/questionable/complete, LC719581.1:1–41588,
      with Heterologous expression and CLUSTER_DEMONSTRATED. The locus experiment
      does not upgrade native producer evidence. TERPENE/PKS classes and Sesquiterpene/Iterative
      type I source subclasses describe their own source axis.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-capture
    - support-2288-source-plan
    - support-2288-routes
    - support-2288-source-notes
    - support-2288-row-mibig_compounds-0
    - support-2288-cache-293381
- assessment_id: support-2288-A4
  area: evidence
  topic: Citation placement and primary-source limits
  outcome: supported
  summary: DOI:10.1002/anie.202210938 is retained with MIBiG ENTRY scope for the producer/locus;
    the Isobrevione E companion shares this entry context but remains a distinct compound.
    NPAtlas NPA019168, PubChem 101092881 and the source-row ChemSpider cross-reference
    are historical database links, not newly checked identities. No primary isolation,
    heterologous construct or stereochemical experiment was retrieved. The versioned
    NPClassifier row is computed provenance rather than a primary chemical assertion.
  target_ids:
  - naturalproductmech:mibig-6295b1addd
  evidence_ids:
  - support-2288-capture
  - support-2288-source-plan
  - support-2288-source-notes
  - support-2288-companions
  - support-2288-row-mibig_compounds-0
  - support-2288-row-npclassifier-0
  - support-2288-row-pubchem_bioassay-0
  - support-2288-companion-0
  dimensions:
  - name: citation_scope
    value: DOI:10.1002/anie.202210938 is retained with MIBiG ENTRY scope for the producer/locus;
      the Isobrevione E companion shares this entry context but remains a distinct
      compound. NPAtlas NPA019168, PubChem 101092881 and the source-row ChemSpider
      cross-reference are historical database links, not newly checked identities.
      No primary isolation, heterologous construct or stereochemical experiment was
      retrieved. The versioned NPClassifier row is computed provenance rather than
      a primary chemical assertion.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-capture
    - support-2288-source-plan
    - support-2288-source-notes
    - support-2288-companions
    - support-2288-row-mibig_compounds-0
    - support-2288-row-npclassifier-0
    - support-2288-row-pubchem_bioassay-0
    - support-2288-companion-0
- assessment_id: support-2288-A5
  area: scope
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: The selected LOTUS, CyanometDB and matched-ChEBI-origin routes are empty
    and no occurrence item is written. PubChem row 3357 has CID 101092881, blank AID
    and '(no assay data)' with blank observation fields; this is a sentinel, not inactivity.
    BindingDB and sibling-corpus matches are also absent in the bounded saved queries.
    Neither occurrence nor pharmacology transfers from Isobrevione E merely because
    the BGC is shared.
  target_ids:
  - naturalproductmech:mibig-6295b1addd
  evidence_ids:
  - support-2288-capture
  - support-2288-source-plan
  - support-2288-routes
  - support-2288-companions
  - support-2288-query-mibig_compounds
  - support-2288-query-chebi_structures
  - support-2288-query-lotus_occurrences
  - support-2288-query-cyanometdb_occurrences
  - support-2288-query-npclassifier
  - support-2288-query-pubchem_bioassay
  - support-2288-query-bindingdb_targets
  - support-2288-query-antibioticmech_inchikeys
  - support-2288-query-chebi_origins
  - support-2288-row-mibig_compounds-0
  - support-2288-row-npclassifier-0
  - support-2288-row-pubchem_bioassay-0
  - support-2288-cache-293381
  - support-2288-companion-0
  dimensions:
  - name: occurrence_scope
    value: The selected LOTUS, CyanometDB and matched-ChEBI-origin routes are empty
      and no occurrence item is written. PubChem row 3357 has CID 101092881, blank
      AID and '(no assay data)' with blank observation fields; this is a sentinel,
      not inactivity. BindingDB and sibling-corpus matches are also absent in the
      bounded saved queries. Neither occurrence nor pharmacology transfers from Isobrevione
      E merely because the BGC is shared.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-capture
    - support-2288-source-plan
    - support-2288-routes
    - support-2288-companions
    - support-2288-query-mibig_compounds
    - support-2288-query-chebi_structures
    - support-2288-query-lotus_occurrences
    - support-2288-query-cyanometdb_occurrences
    - support-2288-query-npclassifier
    - support-2288-query-pubchem_bioassay
    - support-2288-query-bindingdb_targets
    - support-2288-query-antibioticmech_inchikeys
    - support-2288-query-chebi_origins
    - support-2288-row-mibig_compounds-0
    - support-2288-row-npclassifier-0
    - support-2288-row-pubchem_bioassay-0
    - support-2288-cache-293381
    - support-2288-companion-0
  - name: assay_scope
    value: The selected LOTUS, CyanometDB and matched-ChEBI-origin routes are empty
      and no occurrence item is written. PubChem row 3357 has CID 101092881, blank
      AID and '(no assay data)' with blank observation fields; this is a sentinel,
      not inactivity. BindingDB and sibling-corpus matches are also absent in the
      bounded saved queries. Neither occurrence nor pharmacology transfers from Isobrevione
      E merely because the BGC is shared.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-capture
    - support-2288-source-plan
    - support-2288-routes
    - support-2288-companions
    - support-2288-query-mibig_compounds
    - support-2288-query-chebi_structures
    - support-2288-query-lotus_occurrences
    - support-2288-query-cyanometdb_occurrences
    - support-2288-query-npclassifier
    - support-2288-query-pubchem_bioassay
    - support-2288-query-bindingdb_targets
    - support-2288-query-antibioticmech_inchikeys
    - support-2288-query-chebi_origins
    - support-2288-row-mibig_compounds-0
    - support-2288-row-npclassifier-0
    - support-2288-row-pubchem_bioassay-0
    - support-2288-cache-293381
    - support-2288-companion-0
- assessment_id: support-2288-A6
  area: other
  topic: Computed classification and complete saved topology
  outcome: concern
  summary: NPClassifier retains Terpenoids / Diterpenoids / Breviane diterpenoids
    and is_glycoside=true. The maintained schema explicitly makes this a named-model
    prediction and the seeder faithfully copies the retained true value. The complete
    saved graph instead establishes a densely connected polycyclic ether/acetal framework,
    an acetate ester and two ketones; it does not establish a distinct glycosyl residue
    or glycosidic substituent. The empty saturated-C5O motif list alone is not a general
    test for all glycosides. Thus the glycoside prediction has an unresolved applicability
    limitation and must not be presented as an experimentally asserted chemical class.
    No source-identity defect, schema violation, or justified replacement value follows
    from this local review; the literal model result is preserved.
  target_ids:
  - naturalproductmech:mibig-6295b1addd
  evidence_ids:
  - support-2288-capture
  - support-2288-chemistry
  - support-2288-topology
  - support-2288-classification-schema
  - support-2288-classification-seeder
  - support-2288-row-npclassifier-0
  - support-2288-row-mibig_compounds-0
  dimensions:
  - name: computed_classification
    value: NPClassifier retains Terpenoids / Diterpenoids / Breviane diterpenoids
      and is_glycoside=true. The maintained schema explicitly makes this a named-model
      prediction and the seeder faithfully copies the retained true value. The complete
      saved graph instead establishes a densely connected polycyclic ether/acetal
      framework, an acetate ester and two ketones; it does not establish a distinct
      glycosyl residue or glycosidic substituent. The empty saturated-C5O motif list
      alone is not a general test for all glycosides. Thus the glycoside prediction
      has an unresolved applicability limitation and must not be presented as an experimentally
      asserted chemical class. No source-identity defect, schema violation, or justified
      replacement value follows from this local review; the literal model result is
      preserved.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-capture
    - support-2288-chemistry
    - support-2288-topology
    - support-2288-classification-schema
    - support-2288-classification-seeder
    - support-2288-row-npclassifier-0
    - support-2288-row-mibig_compounds-0
- assessment_id: support-2288-A7
  area: completeness
  topic: Review completion and unavailable verification
  outcome: unknown
  summary: The complete owner/history, actual 38-input intake, nine saved query frames,
    3 positive source placements, applicable cached taxonomy and both complete original
    molecular forms were reviewed. No causal_graphs, causal_graph_refs, biosynthetic_pathway
    or molecular_targets root is present; no selected maintained-reader route applies.
    Five local gates and original chemistry have ROOT acceptance. FullQC, full OAK
    and fresh primary/identifier/taxonomy verification remain unavailable, so this
    is a qualified partial review and does not promote SEEDED status. Optional mechanism
    absence is not proof that biosynthesis is unknown in the literature.
  target_ids:
  - naturalproductmech:mibig-6295b1addd
  evidence_ids:
  - support-2288-owner
  - support-2288-capture
  - support-2288-source-plan
  - support-2288-intake
  - support-2288-intake-ready
  - support-2288-plan-acceptance
  - support-2288-source-notes
  - support-2288-chemistry
  - support-2288-diagnostic-acceptance
  - support-2288-native-acceptance
  dimensions:
  - name: review_completion
    value: The complete owner/history, actual 38-input intake, nine saved query frames,
      3 positive source placements, applicable cached taxonomy and both complete original
      molecular forms were reviewed. No causal_graphs, causal_graph_refs, biosynthetic_pathway
      or molecular_targets root is present; no selected maintained-reader route applies.
      Five local gates and original chemistry have ROOT acceptance. FullQC, full OAK
      and fresh primary/identifier/taxonomy verification remain unavailable, so this
      is a qualified partial review and does not promote SEEDED status. Optional mechanism
      absence is not proof that biosynthesis is unknown in the literature.
    definition: Exact inspected scope; retained source assertions, original saved
      computations and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2288-owner
    - support-2288-capture
    - support-2288-source-plan
    - support-2288-intake
    - support-2288-intake-ready
    - support-2288-plan-acceptance
    - support-2288-source-notes
    - support-2288-chemistry
    - support-2288-diagnostic-acceptance
    - support-2288-native-acceptance
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
- The glycoside=true model prediction is retained with an explicit applicability concern;
  local ring motifs do not supply a comprehensive glycoside definition or justify
  overwriting the model output.
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
