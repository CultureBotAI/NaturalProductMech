# Local evidence review: α-acorenol

- Review: 20261103T163601Z-acorenol
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T16:10:24.089090Z
- Finished UTC: 2026-11-03T16:36:01.263326Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified partial review: the exact stereochemically incomplete α-acorenol representation and retained source assertions are traceable. Fungal strain production stays distinct from fungal species and two Lantana occurrences; canonical agreement does not resolve the unassigned center.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2260; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-026b84f2dc | data/natural_products/terpenoids/acorenol.yaml | generated | α-acorenol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-026b84f2dc | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-026b84f2dc | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-026b84f2dc | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-026b84f2dc | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-026b84f2dc | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-026b84f2dc | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-026b84f2dc | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-026b84f2dc | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding

identity: supported. Targets: naturalproductmech:mibig-026b84f2dc.

The MINTED owner naturalproductmech:mibig-026b84f2dc retains full key XDVDHFJMCJWDPI-YOYPFHDYSA-N from BGC0001481 version 3, with source compound_index=1 and label α-acorenol. The admitted exact-full-key ChEBI query has no match and the direct-companion map is empty. Neither the α label nor a database cross-source match supplies the stereochemistry left undefined in the stored structure.

### Stored representation and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-026b84f2dc.

Both forms yield neutral C15H26O, 16 heavy atoms and 17 bonds with equal standard InChI/full key and canonical isomeric/nonisomeric SMILES. Each retains two specified tetrahedral centers and one unspecified center: SMILES atom 4 corresponds to InChI atom 12, and the literal InChI layer includes /t12-,13?,15-. The stored stereo_complete:false faithfully preserves that limitation. Canonical agreement and one saved atom correspondence do not fill the center, prove one natural stereoisomer or establish independent full graph identity.

### Producer, locus, taxon and strain roles

provenance: supported. Targets: naturalproductmech:mibig-026b84f2dc.

MIBiG BGC0001481 version 3 is active, source quality questionable and completeness unknown. Fusarium fujikuroi IMI 58289 strain NCBITaxon:1279085 is SOURCE_ASSERTION; the locus is CLUSTER_UNSTATED with no methods stated. HF679032.1 coordinates 374418..375674 are retained. LOTUS fungal occurrence is species F. fujikuroi 5127, while the two plant occurrences are Lantana camara 126435 and Lantana strigocamara 649173. These cached taxon labels are not an experimental producer upgrade or independent contemporary taxonomy resolution.

### Citation placement and primary-source limits

evidence: supported. Targets: naturalproductmech:mibig-026b84f2dc.

MIBiG producer/locus evidence retains entry-level PMID:23335243 as DATABASE_ASSERTION. The fungal occurrence cites DOI:10.1002/CBIC.201200695. Both Lantana occurrences carry the same literal DOI:10.1002/(SICI)1099-1026(199901/02)14:1&lt;15::AID-FFJ777&gt;3.0.CO;2-M; two taxon rows therefore do not establish two independent studies. All citations remain retained source assertions, with no newly inspected article or live identifier response.

### Occurrence and assay boundaries

scope: supported. Targets: naturalproductmech:mibig-026b84f2dc.

Three written occurrence objects preserve two Lantana taxa and Fusarium fujikuroi species 5127, separately from the strain-level fungal producer. Admitted PubChem, BindingDB, related-corpus, CyanometDB and ChEBI-origin queries are empty in their declared exact-key/identifier scope. No activity summary, assay or molecular target is written. There is no selected mechanism root/component; this review neither invents an enzyme/pathway nor claims that none is known elsewhere.

### Computed classification and complete saved topology

other: supported. Targets: naturalproductmech:mibig-026b84f2dc.

NPClassifier returns Terpenoids / Sesquiterpenoids / Acorane sesquiterpenoids with is_glycoside:false. The complete saved graph has five- and six-membered carbon rings sharing a spiro atom, one internal alkene and an exocyclic tertiary alcohol C12-O15 in SMILES numbering. It has no carbonyl, nitrogen, phosphorus, ether bridge or sugar-ring candidate. The class is compatible with the represented C15 topology; the versioned prediction does not establish the unresolved stereochemistry or biosynthetic atom provenance.

### Review completion and unavailable verification

completeness: unknown. Targets: naturalproductmech:mibig-026b84f2dc.

This is a partial scientific review of the exact admitted owner and retained source scope. Five local commands and original saved chemistry were accepted; FullQC and complete OAK were unavailable. No selected maintained reader is applicable because all four mechanism roots are absent; unselected context does not change applicability. No primary publication, live identifier/taxonomy/protein response or independent natural identity was verified, and this review does not set native REVIEWED status.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2260-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/acorenol.yaml; lines 1–107 | supports | Whole current plaintext owner and all 2 history events. Literal identifier naturalproductmech:mibig-026b84f2dc, label α-acorenol and full key XDVDHFJMCJWDPI-YOYPFHDYSA-N. Historical annotations remain retained claims, not fresh scientific verification. |
| support-2260-capture | /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json; /records/9/owner_document; /records/9/owner_pin | supports | Exact captured complete owner, including structure, provenance, written occurrences, computed classification, mechanism annotations where present and complete history. |
| support-2260-source-plan | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9 | supports | Complete admitted selected source context: nine retained query frames with full copied payloads, 37 inputs and 0 direct companion paths. This is a bounded local inventory scope. |
| support-2260-intake | /private/tmp/npm-review-work/shared-next-batch226/intakes/2260-inspect-001.json; /status; /source; /targets | supports | Original canonical inspection of the exact target and maintained ownership roles with input snapshots; inspection is not a scientific verdict. |
| support-2260-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-input-plan-acceptance-001.json; /accepted; /plan; /inventory; /source_notes; /source_placements; /unique_source_paths; /selected_reader_orders | supports | ROOT accepts the actual plan with 448 input placements and 72 unique paths; selected reader orders are 2256 and 2259. |
| support-2260-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-intake-ready-001.json; /accepted; /status; /intake_summary; /intakes_execution; /source_placements; /unique_source_paths; /mechanism_owner_orders | supports | ROOT accepts the ten original canonical intakes and exact 448/72 input scope; only 2256 and 2259 have selected mechanism-reader applicability. |
| support-2260-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-local-diagnostics-acceptance-001.json; /status; /DATA; /execution; /successful_forms; /comparison_flags_true; /comparison_flags_false; /global_stderr_warnings; /full_QC_and_OAK | supports | ROOT accepts the original twenty saved form computations. There are 98 true comparison flags, with only 2257 canonical isomeric/nonisomeric comparisons false. Eight global omitted-undefined-stereo warnings remain unassigned; FullQC and complete OAK are unavailable. |
| support-2260-native-gates | /private/tmp/npm-review-work/shared-next-batch226/root-native-five-gates-acceptance-001.json; /accepted; /ledger; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /scope | supports | ROOT accepts five successful local commands within the receipt's stated scope; unavailable required gates prevent a claim of complete validation. |
| support-2260-chemistry-execution | /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-execution-001.json; /started_at; /finished_at; /exit_code; /DATA; /stdout; /stderr; /external_requests; /retries | supports | Original ROOT-owned diagnostic execution returned zero once. Exact DATA/stdout/stderr pins preserve the original stream, without reattribution or replay; there was no retry or external request. |
| support-2260-chemistry | /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json; /records/9/declared_structure; /records/9/smiles/computed; /records/9/inchi/computed; /records/9/comparisons; /records/9/atom_correspondence; /records/9/smiles/status; /records/9/inchi/status | supports | Both forms yield neutral C15H26O, 16 heavy atoms and 17 bonds with equal standard InChI/full key and canonical isomeric/nonisomeric SMILES. Each retains two specified tetrahedral centers and one unspecified center: SMILES atom 4 corresponds to InChI atom 12, and the literal InChI layer includes /t12-,13?,15-. The stored stereo_complete:false faithfully preserves that limitation. Canonical agreement and one saved atom correspondence do not fill the center, prove one natural stereoisomer or establish independent full graph identity. |
| support-2260-topology | /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles/computed; /records/9/inchi/computed | supports | Both complete paired tables describe neutral C15H26O with five- and six-carbon rings sharing a spiro atom, one internal alkene and an exocyclic tertiary alcohol. SMILES C12-O15 bears the hydroxyl. Two tetrahedral centers are specified and one remains unspecified. There is no carbonyl, nitrogen, phosphorus, ether bridge or saturated C5O candidate. |
| support-2260-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–173 | supports | Maintained structure_fields parses the source SMILES, derives standard InChI/key and sets stereo_complete by checking undefined tetrahedral centers with FindMolChiralCenters. That implementation is narrower than every possible geometric or tautomeric ambiguity. |
| support-2260-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 982–1025 | supports | Maintained seeder copies the lead structure and completeness flag, uses a returned classification to choose filing, and preserves named tool/version plus pathway/superclass/class/glycoside predictions. |
| support-2260-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392–425 | supports | Schema documents undefined stereocentres and requires computed classification to retain named tool/version. Computed classification is not a source assertion or an admission rationale. |
| support-2260-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; lines 35–57 | supports | Review profile separates source evidence, computed classification, producer/occurrence claims and complete maintained mechanism reading. Source corrections belong in maintained owners; reserved decisions.tsv is not consumed. A saved review does not promote native status or append history. |
| support-2260-source-notes | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-scope-notes-001.json; /reading; /curation; /cautions; /totals | supports | Complete saved-source reading is attributed between BGC and Support, with prior raw carries by exact bytes. The bounded 84-token eight-table curation scan had zero hits; PubChem exclusions were supplemental/unadmitted because no actual AID is present. This does not establish global absence. |
| support-2260-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/source_scope_inventory/source_taxa; /records/9/source_scope_inventory/forward_taxon_merge_matches; /records/9/source_scope_inventory/nonorganism_matches | supports | Exact selected source-taxon set and bounded forward-merge/nonorganism routes. The forward-merge and nonorganism match lists are empty here; cached labels retain their historical scope and do not constitute live taxonomy verification. |
| support-2260-mechanism-scope | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/declared_mechanism_roots_literal; /records/9/component_paths; /records/9/literal_mechanism_inventory; /records/9/proposed_companion_paths | supports | Selected literal mechanism roots and direct context membership for 2260; component list is empty. Positive unselected companions do not create an additional selected maintained-reader route. |
| support-2260-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/source_scope_inventory/joins/mibig_compounds | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 1}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2260-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 1796–1796 | supports | Complete retained row payload: {"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "α-acorenol", "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "HF679032.1", "locus_evidence_methods": "", "locus_from": "374418", "locus_to": "375674", "mibig_accession": "BGC0001481", "primary_reference": "PMID:23335243", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "C[C@H]1CCC([C@@]12CCC(=CC2)C)C(C)(C)O", "standard_inchi": "InChI=1S/C15H26O/c1-11-7-9-15(10-8-11)12(2)5-6-13(15)14(3,4)16/h7,12-13,16H,5-6,8-10H2,1-4H3/t12-,13?,15-/m0/s1", "standard_inchi_key": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "stereo_complete": "false", "taxon_id": "NCBITaxon:1279085", "taxon_label": "Fusarium fujikuroi IMI 58289"} |
| support-2260-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/source_scope_inventory/joins/chebi_structures | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2260-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/source_scope_inventory/joins/lotus_occurrences | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 3}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2260-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 9532–9532 | supports | Complete retained row payload: {"organism_name": "Lantana camara", "organism_wikidata": "http://www.wikidata.org/entity/Q332469", "reference_doi": "10.1002/(SICI)1099-1026(199901/02)14:1&lt;15::AID-FFJ777&gt;3.0.CO;2-M", "standard_inchi_key": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q105326088", "taxon_id": "NCBITaxon:126435"} |
| support-2260-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 9533–9533 | supports | Complete retained row payload: {"organism_name": "Fusarium fujikuroi", "organism_wikidata": "http://www.wikidata.org/entity/Q10500328", "reference_doi": "10.1002/CBIC.201200695", "standard_inchi_key": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q105326088", "taxon_id": "NCBITaxon:5127"} |
| support-2260-row-lotus_occurrences-2 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 9534–9534 | supports | Complete retained row payload: {"organism_name": "Lantana strigocamara", "organism_wikidata": "http://www.wikidata.org/entity/Q15431779", "reference_doi": "10.1002/(SICI)1099-1026(199901/02)14:1&lt;15::AID-FFJ777&gt;3.0.CO;2-M", "standard_inchi_key": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q105326088", "taxon_id": "NCBITaxon:649173"} |
| support-2260-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/source_scope_inventory/joins/cyanometdb_occurrences | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2260-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/source_scope_inventory/joins/npclassifier | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 1}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2260-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2750–2750 | supports | Complete retained row payload: {"class_results": "Acorane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "C[C@H]1CCC([C@@]12CCC(=CC2)C)C(C)(C)O", "standard_inchi_key": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "superclass_results": "Sesquiterpenoids"} |
| support-2260-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/source_scope_inventory/joins/pubchem_bioassay | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2260-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/source_scope_inventory/joins/bindingdb_targets | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2260-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2260-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/source_scope_inventory/joins/chebi_origins | supports | Retained local query frame: {"predicate": "exact chebi_id from exact full-key structure rows", "query": [], "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2260-cache-5127 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; physical lines 8039–8044 | supports | Complete cached stanza, not a fresh taxonomy response:<br>[Term]<br>id: NCBITaxon:5127<br>name: Fusarium fujikuroi<br>synonym: "Gibberella fujikuroi" EXACT []<br>synonym: "Lisea fujikuroi" EXACT []<br><br> |
| support-2260-cache-126435 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; physical lines 47644–47647 | supports | Complete cached stanza, not a fresh taxonomy response:<br>[Term]<br>id: NCBITaxon:126435<br>name: Lantana camara<br><br> |
| support-2260-cache-649173 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; physical lines 105656–105659 | supports | Complete cached stanza, not a fresh taxonomy response:<br>[Term]<br>id: NCBITaxon:649173<br>name: Lantana strigocamara<br><br> |
| support-2260-cache-1279085 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; physical lines 125091–125096 | supports | Complete cached stanza, not a fresh taxonomy response:<br>[Term]<br>id: NCBITaxon:1279085<br>name: Fusarium fujikuroi IMI 58289<br>synonym: "Fusarium fujikuroi IMI58289" EXACT []<br>synonym: "Gibberella fujikuroi IMI 58289" EXACT []<br><br> |
| support-2260-companions | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/9/proposed_companion_paths; /records/9/direct_companion_predicates | supports | Exactly 0 direct companion placements admitted under the saved root/full-key/owned-BGC predicates; no recursive expansion or activity/mechanism transfer is claimed. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-226/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-226/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-226/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-226/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-226/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- FullQC and complete OAK were unavailable; five successful local commands do not establish scientific completeness.
- No external retrieval or live identifier, taxonomy, protein or publication query was performed. These assessments use original saved owner-form computations; no additional molecular parses occurred during fragment authoring.
- The original chemistry stream contains eight omitted-undefined-stereo warnings. They are global and are not attributed to owners from timing or inference.
- Retained source grades, database citations, cached taxonomy and versioned predictions keep their own scopes. Representation agreement does not establish natural identity, publication independence or complete natural stereochemistry.
- No scientific source record or curation history was edited. Canonical persistence and campaign operations remain ROOT-owned.
- The unassigned tetrahedral center remains unresolved; neither the α-acorenol label nor cross-source occurrence claims fill it.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- All four selected mechanism roots and component references are absent; positive unselected context remains context only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T163601Z-acorenol
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: α-acorenol'
started_at: '2026-11-03T16:10:24.089090Z'
finished_at: '2026-11-03T16:36:01.263326Z'
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
summary: 'Qualified partial review: the exact stereochemically incomplete α-acorenol
  representation and retained source assertions are traceable. Fungal strain production
  stays distinct from fungal species and two Lantana occurrences; canonical agreement
  does not resolve the unassigned center.'
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
  - path: data/natural_products/terpenoids/acorenol.yaml
    sha256: 37e3725209e3ba62531be94c3f92878a4db1096d46af27f44a28ee3877b54977
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
  selection: Campaign path order 2260; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-026b84f2dc
targets:
- target_id: naturalproductmech:mibig-026b84f2dc
  path: data/natural_products/terpenoids/acorenol.yaml
  label: α-acorenol
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
  - naturalproductmech:mibig-026b84f2dc
  command: just validate-strict data/natural_products/terpenoids/6-anteisoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/6-anteisoheptadecyl-4-o-geranyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/6-isoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/6-isoheptadecyl-4-o-geranyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/6-isopalmityl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/6-isopalmityl-4-o-geranyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/7-deoxypactamycin.yaml data/natural_products/terpenoids/8-9-epibotrydial.yaml
    data/natural_products/terpenoids/8-hydroxy-6-protoilludene.yaml data/natural_products/terpenoids/acorenol.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-226/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-026b84f2dc
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-226/validate-all-001.tsv
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
  - naturalproductmech:mibig-026b84f2dc
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
  - naturalproductmech:mibig-026b84f2dc
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
  - naturalproductmech:mibig-026b84f2dc
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-226/review-queue-001.tsv
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
  - naturalproductmech:mibig-026b84f2dc
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-026b84f2dc
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-026b84f2dc
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2260-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/acorenol.yaml
  locator: lines 1–107
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Whole current plaintext owner and all 2 history events. Literal identifier
    naturalproductmech:mibig-026b84f2dc, label α-acorenol and full key XDVDHFJMCJWDPI-YOYPFHDYSA-N.
    Historical annotations remain retained claims, not fresh scientific verification.
  snapshot_sha256: 37e3725209e3ba62531be94c3f92878a4db1096d46af27f44a28ee3877b54977
- evidence_id: support-2260-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json
  locator: /records/9/owner_document; /records/9/owner_pin
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Exact captured complete owner, including structure, provenance, written
    occurrences, computed classification, mechanism annotations where present and
    complete history.
  snapshot_sha256: 39a09efef203ca9e288817223f63671042244ab58ffd48c19989979b25cdf028
- evidence_id: support-2260-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete admitted selected source context: nine retained query frames
    with full copied payloads, 37 inputs and 0 direct companion paths. This is a bounded
    local inventory scope.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch226/intakes/2260-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Original canonical inspection of the exact target and maintained ownership
    roles with input snapshots; inspection is not a scientific verdict.
  snapshot_sha256: 008d6101069bd92372271f9162a7fe3067e34aafb6ed9fc6aecf11e4af3b1410
- evidence_id: support-2260-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-input-plan-acceptance-001.json
  locator: /accepted; /plan; /inventory; /source_notes; /source_placements; /unique_source_paths;
    /selected_reader_orders
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: ROOT accepts the actual plan with 448 input placements and 72 unique paths;
    selected reader orders are 2256 and 2259.
  snapshot_sha256: c4eb227ed6d0e6bf96877c3b5f15e9275f07ebb86aff2d4edf7d9749a8871251
- evidence_id: support-2260-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-intake-ready-001.json
  locator: /accepted; /status; /intake_summary; /intakes_execution; /source_placements;
    /unique_source_paths; /mechanism_owner_orders
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: ROOT accepts the ten original canonical intakes and exact 448/72 input
    scope; only 2256 and 2259 have selected mechanism-reader applicability.
  snapshot_sha256: cee04496c89499477fb14b1f5bd349baff9a19879f761f843ba1ef13423cfc52
- evidence_id: support-2260-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-local-diagnostics-acceptance-001.json
  locator: /status; /DATA; /execution; /successful_forms; /comparison_flags_true;
    /comparison_flags_false; /global_stderr_warnings; /full_QC_and_OAK
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: ROOT accepts the original twenty saved form computations. There are 98
    true comparison flags, with only 2257 canonical isomeric/nonisomeric comparisons
    false. Eight global omitted-undefined-stereo warnings remain unassigned; FullQC
    and complete OAK are unavailable.
  snapshot_sha256: 67c8acc7ddac7662cd7f52c95e058806b4dfc64ee849c335a75ab601fecc35cf
- evidence_id: support-2260-native-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-native-five-gates-acceptance-001.json
  locator: /accepted; /ledger; /five_local_commands_passed; /all_native_gates_passed;
    /unavailable_required_gates; /scope
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: ROOT accepts five successful local commands within the receipt's stated
    scope; unavailable required gates prevent a claim of complete validation.
  snapshot_sha256: 66ab88f5308b0868c13d372cd15007e234fd6213978218e700b8b4998ae0ee5a
- evidence_id: support-2260-chemistry-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-execution-001.json
  locator: /started_at; /finished_at; /exit_code; /DATA; /stdout; /stderr; /external_requests;
    /retries
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Original ROOT-owned diagnostic execution returned zero once. Exact DATA/stdout/stderr
    pins preserve the original stream, without reattribution or replay; there was
    no retry or external request.
  snapshot_sha256: 31d79354b21eee031db3ba3dcf19679c5c456728ccf47fccd7ae84163f290d61
- evidence_id: support-2260-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/declared_structure; /records/9/smiles/computed; /records/9/inchi/computed;
    /records/9/comparisons; /records/9/atom_correspondence; /records/9/smiles/status;
    /records/9/inchi/status
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Both forms yield neutral C15H26O, 16 heavy atoms and 17 bonds with equal
    standard InChI/full key and canonical isomeric/nonisomeric SMILES. Each retains
    two specified tetrahedral centers and one unspecified center: SMILES atom 4 corresponds
    to InChI atom 12, and the literal InChI layer includes /t12-,13?,15-. The stored
    stereo_complete:false faithfully preserves that limitation. Canonical agreement
    and one saved atom correspondence do not fill the center, prove one natural stereoisomer
    or establish independent full graph identity.'
  snapshot_sha256: 9402e619ad45ee271669f7c409f81b7af6e2e529a58aed6239da2c56d05b22e2
- evidence_id: support-2260-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles/computed; /records/9/inchi/computed
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Both complete paired tables describe neutral C15H26O with five- and six-carbon
    rings sharing a spiro atom, one internal alkene and an exocyclic tertiary alcohol.
    SMILES C12-O15 bears the hydroxyl. Two tetrahedral centers are specified and one
    remains unspecified. There is no carbonyl, nitrogen, phosphorus, ether bridge
    or saturated C5O candidate.
  snapshot_sha256: 9402e619ad45ee271669f7c409f81b7af6e2e529a58aed6239da2c56d05b22e2
- evidence_id: support-2260-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–173
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Maintained structure_fields parses the source SMILES, derives standard
    InChI/key and sets stereo_complete by checking undefined tetrahedral centers with
    FindMolChiralCenters. That implementation is narrower than every possible geometric
    or tautomeric ambiguity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2260-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 982–1025
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Maintained seeder copies the lead structure and completeness flag, uses
    a returned classification to choose filing, and preserves named tool/version plus
    pathway/superclass/class/glycoside predictions.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2260-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 392–425
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Schema documents undefined stereocentres and requires computed classification
    to retain named tool/version. Computed classification is not a source assertion
    or an admission rationale.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2260-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: lines 35–57
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Review profile separates source evidence, computed classification, producer/occurrence
    claims and complete maintained mechanism reading. Source corrections belong in
    maintained owners; reserved decisions.tsv is not consumed. A saved review does
    not promote native status or append history.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2260-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-scope-notes-001.json
  locator: /reading; /curation; /cautions; /totals
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Complete saved-source reading is attributed between BGC and Support, with
    prior raw carries by exact bytes. The bounded 84-token eight-table curation scan
    had zero hits; PubChem exclusions were supplemental/unadmitted because no actual
    AID is present. This does not establish global absence.
  snapshot_sha256: 1597c81b8311af685af0357a207d5e49353a00216d5c48d722f31a05f06be0b4
- evidence_id: support-2260-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/source_scope_inventory/source_taxa; /records/9/source_scope_inventory/forward_taxon_merge_matches;
    /records/9/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Exact selected source-taxon set and bounded forward-merge/nonorganism routes.
    The forward-merge and nonorganism match lists are empty here; cached labels retain
    their historical scope and do not constitute live taxonomy verification.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-mechanism-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/declared_mechanism_roots_literal; /records/9/component_paths;
    /records/9/literal_mechanism_inventory; /records/9/proposed_companion_paths
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Selected literal mechanism roots and direct context membership for 2260;
    component list is empty. Positive unselected companions do not create an additional
    selected maintained-reader route.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 1}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 1796–1796
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete retained row payload: {"bgc_classes": "terpene", "bgc_subclasses":
    "Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes":
    "", "compound_index": "1", "compound_name": "α-acorenol", "database_ids": "",
    "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status":
    "active", "entry_version": "3", "genome_accession": "HF679032.1", "locus_evidence_methods":
    "", "locus_from": "374418", "locus_to": "375674", "mibig_accession": "BGC0001481",
    "primary_reference": "PMID:23335243", "producer_evidence_basis": "SOURCE_ASSERTION",
    "reference_basis": "ENTRY", "smiles": "C[C@H]1CCC([C@@]12CCC(=CC2)C)C(C)(C)O",
    "standard_inchi": "InChI=1S/C15H26O/c1-11-7-9-15(10-8-11)12(2)5-6-13(15)14(3,4)16/h7,12-13,16H,5-6,8-10H2,1-4H3/t12-,13?,15-/m0/s1",
    "standard_inchi_key": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "stereo_complete": "false",
    "taxon_id": "NCBITaxon:1279085", "taxon_label": "Fusarium fujikuroi IMI 58289"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2260-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 0}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 3}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 9532–9532
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete retained row payload: {"organism_name": "Lantana camara", "organism_wikidata":
    "http://www.wikidata.org/entity/Q332469", "reference_doi": "10.1002/(SICI)1099-1026(199901/02)14:1<15::AID-FFJ777>3.0.CO;2-M",
    "standard_inchi_key": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q105326088",
    "taxon_id": "NCBITaxon:126435"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2260-row-lotus_occurrences-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 9533–9533
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete retained row payload: {"organism_name": "Fusarium fujikuroi",
    "organism_wikidata": "http://www.wikidata.org/entity/Q10500328", "reference_doi":
    "10.1002/CBIC.201200695", "standard_inchi_key": "XDVDHFJMCJWDPI-YOYPFHDYSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q105326088", "taxon_id":
    "NCBITaxon:5127"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2260-row-lotus_occurrences-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 9534–9534
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete retained row payload: {"organism_name": "Lantana strigocamara",
    "organism_wikidata": "http://www.wikidata.org/entity/Q15431779", "reference_doi":
    "10.1002/(SICI)1099-1026(199901/02)14:1<15::AID-FFJ777>3.0.CO;2-M", "standard_inchi_key":
    "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q105326088",
    "taxon_id": "NCBITaxon:649173"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2260-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 0}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 1}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2750–2750
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete retained row payload: {"class_results": "Acorane sesquiterpenoids",
    "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "C[C@H]1CCC([C@@]12CCC(=CC2)C)C(C)(C)O",
    "standard_inchi_key": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "superclass_results": "Sesquiterpenoids"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2260-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 0}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 0}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "XDVDHFJMCJWDPI-YOYPFHDYSA-N", "positive_row_count": 0}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact chebi_id from exact full-key
    structure rows", "query": [], "positive_row_count": 0}. Empty results are scoped
    to this predicate and retained table, not the wider literature or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2260-cache-5127
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: physical lines 8039–8044
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete cached stanza, not a fresh taxonomy response:

    [Term]

    id: NCBITaxon:5127

    name: Fusarium fujikuroi

    synonym: "Gibberella fujikuroi" EXACT []

    synonym: "Lisea fujikuroi" EXACT []


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2260-cache-126435
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: physical lines 47644–47647
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete cached stanza, not a fresh taxonomy response:

    [Term]

    id: NCBITaxon:126435

    name: Lantana camara


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2260-cache-649173
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: physical lines 105656–105659
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete cached stanza, not a fresh taxonomy response:

    [Term]

    id: NCBITaxon:649173

    name: Lantana strigocamara


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2260-cache-1279085
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: physical lines 125091–125096
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete cached stanza, not a fresh taxonomy response:

    [Term]

    id: NCBITaxon:1279085

    name: Fusarium fujikuroi IMI 58289

    synonym: "Fusarium fujikuroi IMI58289" EXACT []

    synonym: "Gibberella fujikuroi IMI 58289" EXACT []


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2260-companions
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/9/proposed_companion_paths; /records/9/direct_companion_predicates
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Exactly 0 direct companion placements admitted under the saved root/full-key/owned-BGC
    predicates; no recursive expansion or activity/mechanism transfer is claimed.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-226/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json
  accessed_at: '2026-11-03T16:11:35.707228Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 3fa23498b91d1b30f655811c3728349e2862f93bc03bc07753c393f7ca5481c4
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-226/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json
  accessed_at: '2026-11-03T16:12:01.451422Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 48c2f4b016834c4f1144f8443efbd602f5e144b6e9f62e4980e5d8de20ea3584
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-226/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json
  accessed_at: '2026-11-03T16:12:21.633510Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-226/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json
  accessed_at: '2026-11-03T16:12:56.658279Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-226/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json
  accessed_at: '2026-11-03T16:13:08.681619Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 471651bc2d9c52a88f0d76e62dd1d43baf68fe35de766f6346cf3befbab82970
assessments:
- assessment_id: support-2260-A1
  area: identity
  topic: Exact structure concept and grounding
  outcome: supported
  summary: The MINTED owner naturalproductmech:mibig-026b84f2dc retains full key XDVDHFJMCJWDPI-YOYPFHDYSA-N
    from BGC0001481 version 3, with source compound_index=1 and label α-acorenol.
    The admitted exact-full-key ChEBI query has no match and the direct-companion
    map is empty. Neither the α label nor a database cross-source match supplies the
    stereochemistry left undefined in the stored structure.
  target_ids:
  - naturalproductmech:mibig-026b84f2dc
  evidence_ids:
  - support-2260-owner
  - support-2260-capture
  - support-2260-source-plan
  - support-2260-query-chebi_structures
  - support-2260-row-mibig_compounds-0
  - support-2260-companions
  dimensions:
  - name: standard_inchi_key
    value: XDVDHFJMCJWDPI-YOYPFHDYSA-N
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-owner
    - support-2260-capture
    - support-2260-source-plan
    - support-2260-query-chebi_structures
    - support-2260-row-mibig_compounds-0
    - support-2260-companions
  - name: grounding_scope
    value: The MINTED owner naturalproductmech:mibig-026b84f2dc retains full key XDVDHFJMCJWDPI-YOYPFHDYSA-N
      from BGC0001481 version 3, with source compound_index=1 and label α-acorenol.
      The admitted exact-full-key ChEBI query has no match and the direct-companion
      map is empty. Neither the α label nor a database cross-source match supplies
      the stereochemistry left undefined in the stored structure.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-owner
    - support-2260-capture
    - support-2260-source-plan
    - support-2260-query-chebi_structures
    - support-2260-row-mibig_compounds-0
    - support-2260-companions
- assessment_id: support-2260-A2
  area: representation
  topic: Stored representation and stereochemistry
  outcome: supported
  summary: 'Both forms yield neutral C15H26O, 16 heavy atoms and 17 bonds with equal
    standard InChI/full key and canonical isomeric/nonisomeric SMILES. Each retains
    two specified tetrahedral centers and one unspecified center: SMILES atom 4 corresponds
    to InChI atom 12, and the literal InChI layer includes /t12-,13?,15-. The stored
    stereo_complete:false faithfully preserves that limitation. Canonical agreement
    and one saved atom correspondence do not fill the center, prove one natural stereoisomer
    or establish independent full graph identity.'
  target_ids:
  - naturalproductmech:mibig-026b84f2dc
  evidence_ids:
  - support-2260-owner
  - support-2260-chemistry
  - support-2260-stereo-method
  - support-2260-seeder
  - support-2260-structure-schema
  dimensions:
  - name: stereochemical_resolution
    value: Two specified tetrahedral centers plus one unresolved center; stereo_complete:false
      and InChI question mark preserved.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-owner
    - support-2260-chemistry
    - support-2260-stereo-method
    - support-2260-seeder
    - support-2260-structure-schema
  - name: representation_correspondence
    value: 'Both forms yield neutral C15H26O, 16 heavy atoms and 17 bonds with equal
      standard InChI/full key and canonical isomeric/nonisomeric SMILES. Each retains
      two specified tetrahedral centers and one unspecified center: SMILES atom 4
      corresponds to InChI atom 12, and the literal InChI layer includes /t12-,13?,15-.
      The stored stereo_complete:false faithfully preserves that limitation. Canonical
      agreement and one saved atom correspondence do not fill the center, prove one
      natural stereoisomer or establish independent full graph identity.'
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-owner
    - support-2260-chemistry
    - support-2260-stereo-method
    - support-2260-seeder
    - support-2260-structure-schema
- assessment_id: support-2260-A3
  area: provenance
  topic: Producer, locus, taxon and strain roles
  outcome: supported
  summary: MIBiG BGC0001481 version 3 is active, source quality questionable and completeness
    unknown. Fusarium fujikuroi IMI 58289 strain NCBITaxon:1279085 is SOURCE_ASSERTION;
    the locus is CLUSTER_UNSTATED with no methods stated. HF679032.1 coordinates 374418..375674
    are retained. LOTUS fungal occurrence is species F. fujikuroi 5127, while the
    two plant occurrences are Lantana camara 126435 and Lantana strigocamara 649173.
    These cached taxon labels are not an experimental producer upgrade or independent
    contemporary taxonomy resolution.
  target_ids:
  - naturalproductmech:mibig-026b84f2dc
  evidence_ids:
  - support-2260-owner
  - support-2260-capture
  - support-2260-source-plan
  - support-2260-row-mibig_compounds-0
  - support-2260-row-lotus_occurrences-0
  - support-2260-row-lotus_occurrences-1
  - support-2260-row-lotus_occurrences-2
  - support-2260-taxonomy-routes
  - support-2260-cache-5127
  - support-2260-cache-126435
  - support-2260-cache-649173
  - support-2260-cache-1279085
  - support-2260-source-notes
  dimensions:
  - name: taxon_and_strain_scope
    value: MIBiG BGC0001481 version 3 is active, source quality questionable and completeness
      unknown. Fusarium fujikuroi IMI 58289 strain NCBITaxon:1279085 is SOURCE_ASSERTION;
      the locus is CLUSTER_UNSTATED with no methods stated. HF679032.1 coordinates
      374418..375674 are retained. LOTUS fungal occurrence is species F. fujikuroi
      5127, while the two plant occurrences are Lantana camara 126435 and Lantana
      strigocamara 649173. These cached taxon labels are not an experimental producer
      upgrade or independent contemporary taxonomy resolution.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-owner
    - support-2260-capture
    - support-2260-source-plan
    - support-2260-row-mibig_compounds-0
    - support-2260-row-lotus_occurrences-0
    - support-2260-row-lotus_occurrences-1
    - support-2260-row-lotus_occurrences-2
    - support-2260-taxonomy-routes
    - support-2260-cache-5127
    - support-2260-cache-126435
    - support-2260-cache-649173
    - support-2260-cache-1279085
    - support-2260-source-notes
  - name: producer_evidence_tier
    value: SOURCE_ASSERTION; Fusarium fujikuroi IMI 58289 strain 1279085, separate
      from species 5127 and plant occurrences.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-owner
    - support-2260-capture
    - support-2260-source-plan
    - support-2260-row-mibig_compounds-0
    - support-2260-row-lotus_occurrences-0
    - support-2260-row-lotus_occurrences-1
    - support-2260-row-lotus_occurrences-2
    - support-2260-taxonomy-routes
    - support-2260-cache-5127
    - support-2260-cache-126435
    - support-2260-cache-649173
    - support-2260-cache-1279085
    - support-2260-source-notes
  - name: locus_evidence_tier
    value: CLUSTER_UNSTATED; BGC0001481 v3 active; no methods stated.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-owner
    - support-2260-capture
    - support-2260-source-plan
    - support-2260-row-mibig_compounds-0
    - support-2260-row-lotus_occurrences-0
    - support-2260-row-lotus_occurrences-1
    - support-2260-row-lotus_occurrences-2
    - support-2260-taxonomy-routes
    - support-2260-cache-5127
    - support-2260-cache-126435
    - support-2260-cache-649173
    - support-2260-cache-1279085
    - support-2260-source-notes
- assessment_id: support-2260-A4
  area: evidence
  topic: Citation placement and primary-source limits
  outcome: supported
  summary: MIBiG producer/locus evidence retains entry-level PMID:23335243 as DATABASE_ASSERTION.
    The fungal occurrence cites DOI:10.1002/CBIC.201200695. Both Lantana occurrences
    carry the same literal DOI:10.1002/(SICI)1099-1026(199901/02)14:1<15::AID-FFJ777>3.0.CO;2-M;
    two taxon rows therefore do not establish two independent studies. All citations
    remain retained source assertions, with no newly inspected article or live identifier
    response.
  target_ids:
  - naturalproductmech:mibig-026b84f2dc
  evidence_ids:
  - support-2260-owner
  - support-2260-capture
  - support-2260-source-plan
  - support-2260-row-mibig_compounds-0
  - support-2260-row-lotus_occurrences-0
  - support-2260-row-lotus_occurrences-1
  - support-2260-row-lotus_occurrences-2
  dimensions:
  - name: citation_scope
    value: MIBiG producer/locus evidence retains entry-level PMID:23335243 as DATABASE_ASSERTION.
      The fungal occurrence cites DOI:10.1002/CBIC.201200695. Both Lantana occurrences
      carry the same literal DOI:10.1002/(SICI)1099-1026(199901/02)14:1<15::AID-FFJ777>3.0.CO;2-M;
      two taxon rows therefore do not establish two independent studies. All citations
      remain retained source assertions, with no newly inspected article or live identifier
      response.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-owner
    - support-2260-capture
    - support-2260-source-plan
    - support-2260-row-mibig_compounds-0
    - support-2260-row-lotus_occurrences-0
    - support-2260-row-lotus_occurrences-1
    - support-2260-row-lotus_occurrences-2
- assessment_id: support-2260-A5
  area: scope
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: Three written occurrence objects preserve two Lantana taxa and Fusarium
    fujikuroi species 5127, separately from the strain-level fungal producer. Admitted
    PubChem, BindingDB, related-corpus, CyanometDB and ChEBI-origin queries are empty
    in their declared exact-key/identifier scope. No activity summary, assay or molecular
    target is written. There is no selected mechanism root/component; this review
    neither invents an enzyme/pathway nor claims that none is known elsewhere.
  target_ids:
  - naturalproductmech:mibig-026b84f2dc
  evidence_ids:
  - support-2260-owner
  - support-2260-capture
  - support-2260-source-plan
  - support-2260-query-mibig_compounds
  - support-2260-query-chebi_structures
  - support-2260-query-lotus_occurrences
  - support-2260-query-cyanometdb_occurrences
  - support-2260-query-npclassifier
  - support-2260-query-pubchem_bioassay
  - support-2260-query-bindingdb_targets
  - support-2260-query-antibioticmech_inchikeys
  - support-2260-query-chebi_origins
  - support-2260-row-lotus_occurrences-0
  - support-2260-row-lotus_occurrences-1
  - support-2260-row-lotus_occurrences-2
  - support-2260-mechanism-scope
  - support-2260-companions
  dimensions:
  - name: occurrence_scope
    value: Three written occurrence objects preserve two Lantana taxa and Fusarium
      fujikuroi species 5127, separately from the strain-level fungal producer. Admitted
      PubChem, BindingDB, related-corpus, CyanometDB and ChEBI-origin queries are
      empty in their declared exact-key/identifier scope. No activity summary, assay
      or molecular target is written. There is no selected mechanism root/component;
      this review neither invents an enzyme/pathway nor claims that none is known
      elsewhere.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-owner
    - support-2260-capture
    - support-2260-source-plan
    - support-2260-query-mibig_compounds
    - support-2260-query-chebi_structures
    - support-2260-query-lotus_occurrences
    - support-2260-query-cyanometdb_occurrences
    - support-2260-query-npclassifier
    - support-2260-query-pubchem_bioassay
    - support-2260-query-bindingdb_targets
    - support-2260-query-antibioticmech_inchikeys
    - support-2260-query-chebi_origins
    - support-2260-row-lotus_occurrences-0
    - support-2260-row-lotus_occurrences-1
    - support-2260-row-lotus_occurrences-2
    - support-2260-mechanism-scope
    - support-2260-companions
  - name: assay_scope
    value: Three written occurrence objects preserve two Lantana taxa and Fusarium
      fujikuroi species 5127, separately from the strain-level fungal producer. Admitted
      PubChem, BindingDB, related-corpus, CyanometDB and ChEBI-origin queries are
      empty in their declared exact-key/identifier scope. No activity summary, assay
      or molecular target is written. There is no selected mechanism root/component;
      this review neither invents an enzyme/pathway nor claims that none is known
      elsewhere.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-owner
    - support-2260-capture
    - support-2260-source-plan
    - support-2260-query-mibig_compounds
    - support-2260-query-chebi_structures
    - support-2260-query-lotus_occurrences
    - support-2260-query-cyanometdb_occurrences
    - support-2260-query-npclassifier
    - support-2260-query-pubchem_bioassay
    - support-2260-query-bindingdb_targets
    - support-2260-query-antibioticmech_inchikeys
    - support-2260-query-chebi_origins
    - support-2260-row-lotus_occurrences-0
    - support-2260-row-lotus_occurrences-1
    - support-2260-row-lotus_occurrences-2
    - support-2260-mechanism-scope
    - support-2260-companions
- assessment_id: support-2260-A6
  area: other
  topic: Computed classification and complete saved topology
  outcome: supported
  summary: NPClassifier returns Terpenoids / Sesquiterpenoids / Acorane sesquiterpenoids
    with is_glycoside:false. The complete saved graph has five- and six-membered carbon
    rings sharing a spiro atom, one internal alkene and an exocyclic tertiary alcohol
    C12-O15 in SMILES numbering. It has no carbonyl, nitrogen, phosphorus, ether bridge
    or sugar-ring candidate. The class is compatible with the represented C15 topology;
    the versioned prediction does not establish the unresolved stereochemistry or
    biosynthetic atom provenance.
  target_ids:
  - naturalproductmech:mibig-026b84f2dc
  evidence_ids:
  - support-2260-capture
  - support-2260-topology
  - support-2260-row-npclassifier-0
  - support-2260-row-mibig_compounds-0
  - support-2260-seeder
  - support-2260-structure-schema
  dimensions:
  - name: computed_classification
    value: NPClassifier returns Terpenoids / Sesquiterpenoids / Acorane sesquiterpenoids
      with is_glycoside:false. The complete saved graph has five- and six-membered
      carbon rings sharing a spiro atom, one internal alkene and an exocyclic tertiary
      alcohol C12-O15 in SMILES numbering. It has no carbonyl, nitrogen, phosphorus,
      ether bridge or sugar-ring candidate. The class is compatible with the represented
      C15 topology; the versioned prediction does not establish the unresolved stereochemistry
      or biosynthetic atom provenance.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-capture
    - support-2260-topology
    - support-2260-row-npclassifier-0
    - support-2260-row-mibig_compounds-0
    - support-2260-seeder
    - support-2260-structure-schema
- assessment_id: support-2260-A7
  area: completeness
  topic: Review completion and unavailable verification
  outcome: unknown
  summary: This is a partial scientific review of the exact admitted owner and retained
    source scope. Five local commands and original saved chemistry were accepted;
    FullQC and complete OAK were unavailable. No selected maintained reader is applicable
    because all four mechanism roots are absent; unselected context does not change
    applicability. No primary publication, live identifier/taxonomy/protein response
    or independent natural identity was verified, and this review does not set native
    REVIEWED status.
  target_ids:
  - naturalproductmech:mibig-026b84f2dc
  evidence_ids:
  - support-2260-intake
  - support-2260-plan-acceptance
  - support-2260-intake-acceptance
  - support-2260-diagnostic-acceptance
  - support-2260-native-gates
  - support-2260-chemistry-execution
  - support-2260-review-profile
  - support-2260-source-notes
  dimensions:
  - name: review_completion
    value: This is a partial scientific review of the exact admitted owner and retained
      source scope. Five local commands and original saved chemistry were accepted;
      FullQC and complete OAK were unavailable. No selected maintained reader is applicable
      because all four mechanism roots are absent; unselected context does not change
      applicability. No primary publication, live identifier/taxonomy/protein response
      or independent natural identity was verified, and this review does not set native
      REVIEWED status.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2260-intake
    - support-2260-plan-acceptance
    - support-2260-intake-acceptance
    - support-2260-diagnostic-acceptance
    - support-2260-native-gates
    - support-2260-chemistry-execution
    - support-2260-review-profile
    - support-2260-source-notes
findings: []
actions: []
limitations:
- FullQC and complete OAK were unavailable; five successful local commands do not
  establish scientific completeness.
- No external retrieval or live identifier, taxonomy, protein or publication query
  was performed. These assessments use original saved owner-form computations; no
  additional molecular parses occurred during fragment authoring.
- The original chemistry stream contains eight omitted-undefined-stereo warnings.
  They are global and are not attributed to owners from timing or inference.
- Retained source grades, database citations, cached taxonomy and versioned predictions
  keep their own scopes. Representation agreement does not establish natural identity,
  publication independence or complete natural stereochemistry.
- No scientific source record or curation history was edited. Canonical persistence
  and campaign operations remain ROOT-owned.
- The unassigned tetrahedral center remains unresolved; neither the α-acorenol label
  nor cross-source occurrence claims fill it.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- All four selected mechanism roots and component references are absent; positive
  unselected context remains context only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-226
```
