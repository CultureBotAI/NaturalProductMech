# Local evidence review: 8,9-epibotrydial

- Review: 20261103T163601Z-8-9-epibotrydial
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T16:10:24.079904Z
- Finished UTC: 2026-11-03T16:36:01.237038Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified partial review: the represented six-center dialdehyde/acetate owner and source grades are traceable. Botrytis strain production remains distinct from species occurrence, and the 20 direct congeners supply no transferable mechanism, activity or stereochemistry.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2258; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-a2b74a45ae | data/natural_products/terpenoids/8-9-epibotrydial.yaml | generated | 8,9-epibotrydial |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-a2b74a45ae | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-a2b74a45ae | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-a2b74a45ae | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-a2b74a45ae | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-a2b74a45ae | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-a2b74a45ae | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-a2b74a45ae | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-a2b74a45ae | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding

identity: supported. Targets: naturalproductmech:mibig-a2b74a45ae.

The MINTED owner naturalproductmech:mibig-a2b74a45ae retains full key SJFIYVCSGNWVPJ-PQVRDHEWSA-N from BGC0000631 version 5 with source compound_index=2. The admitted ChEBI exact-full-key query has no match. Its 20 direct BGC0000631 companions have separate identities; Botrydial CHEBI:3159 has key SJFIYVCSGNWVPJ-GKKOWQTJSA-N, sharing a connectivity block but differing in stereochemical scope. That companion is not an interchangeable grounding for 8,9-epibotrydial.

### Stored representation and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-a2b74a45ae.

Both stored forms give neutral C17H26O5, 22 heavy atoms and 23 bonds with equal standard InChI/full key and canonical isomeric/nonisomeric SMILES. Six potential tetrahedral centers are specified in each form; stereo_complete:true is consistent with those represented centers. Saved local tags differ with atom order, while the isomeric representation agrees. The supplied correspondence is one chirality-aware match and explicitly does not establish independent full graph or natural identity, absolute configuration from primary data, or identity with a stereochemical congener.

### Producer, locus, taxon and strain roles

provenance: supported. Targets: naturalproductmech:mibig-a2b74a45ae.

MIBiG BGC0000631 version 5 is active with source quality questionable and completeness complete. The producer Botrytis cinerea B05.10 strain NCBITaxon:332648 is BGC_CHARACTERIZED; its locus is separately CLUSTER_DEMONSTRATED with Knock-out studies. CP009816.1 coordinates 2216500..2246000 are retained. The two LOTUS occurrences instead refer to species Botrytis cinerea 40559. The cached strain and species labels support the written distinction, not an upgrade or fresh taxonomic/experimental verification.

### Citation placement and primary-source limits

evidence: supported. Targets: naturalproductmech:mibig-a2b74a45ae.

The source producer/locus claim retains compound-level DOI:10.1016/s0040-4020(99)00032-0 as DATABASE_ASSERTION. The two LOTUS triples cite DOI:10.1016/0006-2952(75)90029-5 and DOI:10.1016/S0040-4020(99)00032-0. The case-varied 1999 DOI is not independent corroboration of the MIBiG citation. Companion publications and Botrydial's mechanism evidence retain their own owners and roles; no primary paper was inspected anew.

### Occurrence and assay boundaries

scope: supported. Targets: naturalproductmech:mibig-a2b74a45ae.

Both written occurrence objects concern Botrytis cinerea species 40559 and preserve their separate retained references. PubChem, BindingDB, related-corpus, CyanometDB and ChEBI-origin queries contain no selected-key positive row in this inventory scope. No activity summary, assay object or molecular target is written for the owner. Botrydial's cytotoxic definition, mechanism assertions and other companion observations do not establish this epimer's biological activity or pathway; no such transfer is made.

### Computed classification and complete saved topology

other: supported. Targets: naturalproductmech:mibig-a2b74a45ae.

NPClassifier returns Terpenoids / Sesquiterpenoids / Botryane sesquiterpenoids and is_glycoside:false at the recorded model version. The complete saved SMILES graph has fused six- and five-carbon rings, six specified centers, two aldehydes C7(=O8)H and C15(=O16)H, a tertiary hydroxyl at C5 and acetate C19(=O20)-O18-C3. The InChI-derived form preserves these features with different indices. No nitrogen, phosphorus, aromatic ring or sugar candidate is present. The model label is compatible with this structural description but remains a computed prediction, not independent biosynthetic or natural-identity evidence.

### Review completion and unavailable verification

completeness: unknown. Targets: naturalproductmech:mibig-a2b74a45ae.

This is a partial scientific review of the exact admitted owner and retained source scope. Five local commands and original saved chemistry were accepted; FullQC and complete OAK were unavailable. No selected maintained reader is applicable because all four mechanism roots are absent; unselected context does not change applicability. No primary publication, live identifier/taxonomy/protein response or independent natural identity was verified, and this review does not set native REVIEWED status.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2258-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/8-9-epibotrydial.yaml; lines 1–102 | supports | Whole current plaintext owner and all 2 history events. Literal identifier naturalproductmech:mibig-a2b74a45ae, label 8,9-epibotrydial and full key SJFIYVCSGNWVPJ-PQVRDHEWSA-N. Historical annotations remain retained claims, not fresh scientific verification. |
| support-2258-capture | /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json; /records/7/owner_document; /records/7/owner_pin | supports | Exact captured complete owner, including structure, provenance, written occurrences, computed classification, mechanism annotations where present and complete history. |
| support-2258-source-plan | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7 | supports | Complete admitted selected source context: nine retained query frames with full copied payloads, 57 inputs and 20 direct companion paths. This is a bounded local inventory scope. |
| support-2258-intake | /private/tmp/npm-review-work/shared-next-batch226/intakes/2258-inspect-001.json; /status; /source; /targets | supports | Original canonical inspection of the exact target and maintained ownership roles with input snapshots; inspection is not a scientific verdict. |
| support-2258-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-input-plan-acceptance-001.json; /accepted; /plan; /inventory; /source_notes; /source_placements; /unique_source_paths; /selected_reader_orders | supports | ROOT accepts the actual plan with 448 input placements and 72 unique paths; selected reader orders are 2256 and 2259. |
| support-2258-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-intake-ready-001.json; /accepted; /status; /intake_summary; /intakes_execution; /source_placements; /unique_source_paths; /mechanism_owner_orders | supports | ROOT accepts the ten original canonical intakes and exact 448/72 input scope; only 2256 and 2259 have selected mechanism-reader applicability. |
| support-2258-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-local-diagnostics-acceptance-001.json; /status; /DATA; /execution; /successful_forms; /comparison_flags_true; /comparison_flags_false; /global_stderr_warnings; /full_QC_and_OAK | supports | ROOT accepts the original twenty saved form computations. There are 98 true comparison flags, with only 2257 canonical isomeric/nonisomeric comparisons false. Eight global omitted-undefined-stereo warnings remain unassigned; FullQC and complete OAK are unavailable. |
| support-2258-native-gates | /private/tmp/npm-review-work/shared-next-batch226/root-native-five-gates-acceptance-001.json; /accepted; /ledger; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /scope | supports | ROOT accepts five successful local commands within the receipt's stated scope; unavailable required gates prevent a claim of complete validation. |
| support-2258-chemistry-execution | /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-execution-001.json; /started_at; /finished_at; /exit_code; /DATA; /stdout; /stderr; /external_requests; /retries | supports | Original ROOT-owned diagnostic execution returned zero once. Exact DATA/stdout/stderr pins preserve the original stream, without reattribution or replay; there was no retry or external request. |
| support-2258-chemistry | /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/smiles/computed; /records/7/inchi/computed; /records/7/comparisons; /records/7/atom_correspondence; /records/7/smiles/status; /records/7/inchi/status | supports | Both stored forms give neutral C17H26O5, 22 heavy atoms and 23 bonds with equal standard InChI/full key and canonical isomeric/nonisomeric SMILES. Six potential tetrahedral centers are specified in each form; stereo_complete:true is consistent with those represented centers. Saved local tags differ with atom order, while the isomeric representation agrees. The supplied correspondence is one chirality-aware match and explicitly does not establish independent full graph or natural identity, absolute configuration from primary data, or identity with a stereochemical congener. |
| support-2258-topology | /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed; /records/7/inchi/computed | supports | Both complete paired tables describe fused six- and five-carbon rings, six specified tetrahedral centers, two aldehydes, a tertiary hydroxyl and one acetate ester. SMILES aldehydes are C7(=O8)H and C15(=O16)H, and acetate is C19(=O20)-O18-C3. No nitrogen, phosphorus, aromatic ring or saturated C5O candidate is present. |
| support-2258-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–173 | supports | Maintained structure_fields parses the source SMILES, derives standard InChI/key and sets stereo_complete by checking undefined tetrahedral centers with FindMolChiralCenters. That implementation is narrower than every possible geometric or tautomeric ambiguity. |
| support-2258-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 982–1025 | supports | Maintained seeder copies the lead structure and completeness flag, uses a returned classification to choose filing, and preserves named tool/version plus pathway/superclass/class/glycoside predictions. |
| support-2258-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392–425 | supports | Schema documents undefined stereocentres and requires computed classification to retain named tool/version. Computed classification is not a source assertion or an admission rationale. |
| support-2258-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; lines 35–57 | supports | Review profile separates source evidence, computed classification, producer/occurrence claims and complete maintained mechanism reading. Source corrections belong in maintained owners; reserved decisions.tsv is not consumed. A saved review does not promote native status or append history. |
| support-2258-source-notes | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-scope-notes-001.json; /reading; /curation; /cautions; /totals | supports | Complete saved-source reading is attributed between BGC and Support, with prior raw carries by exact bytes. The bounded 84-token eight-table curation scan had zero hits; PubChem exclusions were supplemental/unadmitted because no actual AID is present. This does not establish global absence. |
| support-2258-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/source_scope_inventory/source_taxa; /records/7/source_scope_inventory/forward_taxon_merge_matches; /records/7/source_scope_inventory/nonorganism_matches | supports | Exact selected source-taxon set and bounded forward-merge/nonorganism routes. The forward-merge and nonorganism match lists are empty here; cached labels retain their historical scope and do not constitute live taxonomy verification. |
| support-2258-mechanism-scope | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/declared_mechanism_roots_literal; /records/7/component_paths; /records/7/literal_mechanism_inventory; /records/7/proposed_companion_paths | supports | Selected literal mechanism roots and direct context membership for 2258; component list is empty. Positive unselected companions do not create an additional selected maintained-reader route. |
| support-2258-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/source_scope_inventory/joins/mibig_compounds | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 1}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2258-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 728–728 | supports | Complete retained row payload: {"bgc_classes": "terpene", "bgc_subclasses": "Sesquiterpene", "cluster_link_evidence_basis": "CLUSTER_DEMONSTRATED", "compound_classes": "", "compound_index": "2", "compound_name": "8,9-epibotrydial", "database_ids": "npatlas:NPA019653", "entry_completeness": "complete", "entry_quality": "questionable", "entry_status": "active", "entry_version": "5", "genome_accession": "CP009816.1", "locus_evidence_methods": "Knock-out studies", "locus_from": "2216500", "locus_to": "2246000", "mibig_accession": "BGC0000631", "primary_reference": "DOI:10.1016/s0040-4020(99)00032-0", "producer_evidence_basis": "BGC_CHARACTERIZED", "reference_basis": "COMPOUND_EVIDENCE", "smiles": "C[C@@H]1C[C@@H]([C@@H]2[C@@]([C@H]1C=O)([C@](CC2(C)C)(C)C=O)O)OC(=O)C", "standard_inchi": "InChI=1S/C17H26O5/c1-10-6-13(22-11(2)20)14-15(3,4)8-16(5,9-19)17(14,21)12(10)7-18/h7,9-10,12-14,21H,6,8H2,1-5H3/t10-,12+,13+,14+,16+,17+/m1/s1", "standard_inchi_key": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:332648", "taxon_label": "Botrytis cinerea B05.10"} |
| support-2258-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/source_scope_inventory/joins/chebi_structures | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2258-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/source_scope_inventory/joins/lotus_occurrences | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 2}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2258-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 8412–8412 | supports | Complete retained row payload: {"organism_name": "Botrytis cinerea", "organism_wikidata": "http://www.wikidata.org/entity/Q1135851", "reference_doi": "10.1016/0006-2952(75)90029-5", "standard_inchi_key": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q105254261", "taxon_id": "NCBITaxon:40559"} |
| support-2258-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 8413–8413 | supports | Complete retained row payload: {"organism_name": "Botrytis cinerea", "organism_wikidata": "http://www.wikidata.org/entity/Q1135851", "reference_doi": "10.1016/S0040-4020(99)00032-0", "standard_inchi_key": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q105254261", "taxon_id": "NCBITaxon:40559"} |
| support-2258-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/source_scope_inventory/joins/cyanometdb_occurrences | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2258-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/source_scope_inventory/joins/npclassifier | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 1}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2258-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2253–2253 | supports | Complete retained row payload: {"class_results": "Botryane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "C[C@@H]1C[C@@H]([C@@H]2[C@@]([C@H]1C=O)([C@](CC2(C)C)(C)C=O)O)OC(=O)C", "standard_inchi_key": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "superclass_results": "Sesquiterpenoids"} |
| support-2258-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/source_scope_inventory/joins/pubchem_bioassay | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2258-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/source_scope_inventory/joins/bindingdb_targets | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2258-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Retained local query frame: {"predicate": "exact complete standard_inchi_key equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2258-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/source_scope_inventory/joins/chebi_origins | supports | Retained local query frame: {"predicate": "exact chebi_id from exact full-key structure rows", "query": [], "positive_row_count": 0}. Empty results are scoped to this predicate and retained table, not the wider literature or live database. |
| support-2258-cache-40559 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; physical lines 18031–18038 | supports | Complete cached stanza, not a fresh taxonomy response:<br>[Term]<br>id: NCBITaxon:40559<br>name: Botrytis cinerea<br>synonym: "Botryotinia fuckeliana" EXACT []<br>synonym: "Botrytis cinerea Pers., 1801" EXACT []<br>synonym: "Peziza fuckeliana" EXACT []<br>synonym: "Sclerotinia fuckeliana" EXACT []<br><br> |
| support-2258-cache-332648 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; physical lines 83758–83762 | supports | Complete cached stanza, not a fresh taxonomy response:<br>[Term]<br>id: NCBITaxon:332648<br>name: Botrytis cinerea B05.10<br>synonym: "Botryotinia fuckeliana B05.10" EXACT []<br><br> |
| support-2258-companion-0 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/4 | supports | Retained direct context naturalproductmech:mibig-acc775e1b7 (1-epibotrydial), full key SJFIYVCSGNWVPJ-SDLFRHKASA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-1 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/5 | supports | Retained direct context naturalproductmech:mibig-1e06238f05 (10-dehydroxy dihydrobotrydialone), full key MBHVNAKPTPFWNG-MYFMSEKESA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-2 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/6 | supports | Retained direct context naturalproductmech:mibig-7950af79c1 (10-epi-dihydrobotrydial), full key QUGYVDURDBEQRB-VZJVBFQISA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-3 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/7 | supports | Retained direct context naturalproductmech:mibig-e2d62600f5 (10-Oxo-dihydrobotrydial), full key MFOUCDNLAFNKML-SVLWDWOGSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-4 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/8 | supports | Retained direct context naturalproductmech:mibig-7b45e48275 (10-Oxodehydrodihydrobotrydial), full key CAMCSBCRRUTMEK-OAHLLOKOSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-5 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/9 | supports | Retained direct context naturalproductmech:mibig-8b4cd14741 (10-Oxodihydrobotry-1(9),4(5)-diendial), full key PCEVLQFNPPWJEB-RFAUZJTJSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-6 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/10 | supports | Retained direct context naturalproductmech:mibig-bbb6f44666 (11-Hydroxydehydrobotrydienol), full key JUCMRFKOKIZVPS-OAHLLOKOSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-7 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/11 | supports | Retained direct context naturalproductmech:mibig-10fda622fe (12-hydroxydehydrobotrydienol), full key YPJRKTIWVUVMDI-LSDHHAIUSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-8 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/12 | supports | Retained direct context naturalproductmech:mibig-0bd6ab53bc (4β-Acetoxytetrahydrobotryslactone), full key RVXLTRZIAMMATE-JMTSMVSISA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-9 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/13 | supports | Retained direct context CHEBI:3159 (botrydial), full key SJFIYVCSGNWVPJ-GKKOWQTJSA-N, with complete plaintext and all 3 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-10 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/14 | supports | Retained direct context naturalproductmech:mibig-a1c6942987 (Botrydienal), full key CFAMAVBUWMXYLX-MEBBXXQBSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-11 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/15 | supports | Retained direct context naturalproductmech:mibig-d567f1a1cd (Botryenalol), full key DSVSTMJOGQEZJX-BYLNDYCFSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-12 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/16 | supports | Retained direct context naturalproductmech:mibig-79ce4aca52 (Botryendial), full key QWZKEROSOALLJP-BYLNDYCFSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-13 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/17 | supports | Retained direct context naturalproductmech:mibig-247120aa23 (Dehydrobotrydienol), full key UQQKKLVKVVJDEX-OAHLLOKOSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-14 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/18 | supports | Retained direct context naturalproductmech:mibig-b5ca742a5e (Dihydrobotrydial), full key QUGYVDURDBEQRB-CJNHKLDISA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-15 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/19 | supports | Retained direct context naturalproductmech:mibig-9b040d7e03 (Norbotrydialone acetate), full key OMZUEHMZFLBHNI-PCKWUFTNSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-16 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/20 | supports | Retained direct context naturalproductmech:mibig-2cef442430 (Secobotrydiene-3,10,15-triol), full key GYABYKLKVQPSPD-NVWZYQMFSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-17 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/21 | supports | Retained direct context naturalproductmech:mibig-f478b3a4f7 (Secobotrydiene-3,4,10,15-tetraol), full key GNMCOKDZWITFBO-MGNGBMTDSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-18 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/22 | supports | Retained direct context naturalproductmech:mibig-ff72b656ae (Secobotrytriendiol), full key BHNACKMCMDASDB-UJNBGNEJSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companion-19 | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /raw_unselected_companions/23 | supports | Retained direct context naturalproductmech:mibig-1c14174a30 (Secobotrytriene-10,12,15-triol), full key WLPOYIWCPMYYGM-KGRKPJGKSA-N, with complete plaintext and all 2 history events plus its bounded source context. Its distinct owner assertions, stereochemistry, activity and mechanism annotations are not transferred to this selected owner. |
| support-2258-companions | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/7/proposed_companion_paths; /records/7/direct_companion_predicates | supports | Exactly 20 direct companion placements admitted under the saved root/full-key/owned-BGC predicates; no recursive expansion or activity/mechanism transfer is claimed. |
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
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- All four selected mechanism roots and component references are absent; positive unselected context remains context only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T163601Z-8-9-epibotrydial
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: 8,9-epibotrydial'
started_at: '2026-11-03T16:10:24.079904Z'
finished_at: '2026-11-03T16:36:01.237038Z'
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
summary: 'Qualified partial review: the represented six-center dialdehyde/acetate
  owner and source grades are traceable. Botrytis strain production remains distinct
  from species occurrence, and the 20 direct congeners supply no transferable mechanism,
  activity or stereochemistry.'
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
    role: target
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
    role: context
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
  selection: Campaign path order 2258; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-a2b74a45ae
targets:
- target_id: naturalproductmech:mibig-a2b74a45ae
  path: data/natural_products/terpenoids/8-9-epibotrydial.yaml
  label: 8,9-epibotrydial
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
  - naturalproductmech:mibig-a2b74a45ae
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
  - naturalproductmech:mibig-a2b74a45ae
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
  - naturalproductmech:mibig-a2b74a45ae
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
  - naturalproductmech:mibig-a2b74a45ae
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
  - naturalproductmech:mibig-a2b74a45ae
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
  - naturalproductmech:mibig-a2b74a45ae
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-a2b74a45ae
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-a2b74a45ae
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2258-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/8-9-epibotrydial.yaml
  locator: lines 1–102
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Whole current plaintext owner and all 2 history events. Literal identifier
    naturalproductmech:mibig-a2b74a45ae, label 8,9-epibotrydial and full key SJFIYVCSGNWVPJ-PQVRDHEWSA-N.
    Historical annotations remain retained claims, not fresh scientific verification.
  snapshot_sha256: 11f0440d7c378d961befc6e158afa3f9a839110ce672438ad032baa487a9cc33
- evidence_id: support-2258-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json
  locator: /records/7/owner_document; /records/7/owner_pin
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Exact captured complete owner, including structure, provenance, written
    occurrences, computed classification, mechanism annotations where present and
    complete history.
  snapshot_sha256: 39a09efef203ca9e288817223f63671042244ab58ffd48c19989979b25cdf028
- evidence_id: support-2258-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete admitted selected source context: nine retained query frames
    with full copied payloads, 57 inputs and 20 direct companion paths. This is a
    bounded local inventory scope.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch226/intakes/2258-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Original canonical inspection of the exact target and maintained ownership
    roles with input snapshots; inspection is not a scientific verdict.
  snapshot_sha256: 62bd1dc25c3c0b57e3ec9a5cf32b0d59d1b44f7fd412d4ea4a4456790492967f
- evidence_id: support-2258-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-input-plan-acceptance-001.json
  locator: /accepted; /plan; /inventory; /source_notes; /source_placements; /unique_source_paths;
    /selected_reader_orders
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: ROOT accepts the actual plan with 448 input placements and 72 unique paths;
    selected reader orders are 2256 and 2259.
  snapshot_sha256: c4eb227ed6d0e6bf96877c3b5f15e9275f07ebb86aff2d4edf7d9749a8871251
- evidence_id: support-2258-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-intake-ready-001.json
  locator: /accepted; /status; /intake_summary; /intakes_execution; /source_placements;
    /unique_source_paths; /mechanism_owner_orders
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: ROOT accepts the ten original canonical intakes and exact 448/72 input
    scope; only 2256 and 2259 have selected mechanism-reader applicability.
  snapshot_sha256: cee04496c89499477fb14b1f5bd349baff9a19879f761f843ba1ef13423cfc52
- evidence_id: support-2258-diagnostic-acceptance
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
- evidence_id: support-2258-native-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-native-five-gates-acceptance-001.json
  locator: /accepted; /ledger; /five_local_commands_passed; /all_native_gates_passed;
    /unavailable_required_gates; /scope
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: ROOT accepts five successful local commands within the receipt's stated
    scope; unavailable required gates prevent a claim of complete validation.
  snapshot_sha256: 66ab88f5308b0868c13d372cd15007e234fd6213978218e700b8b4998ae0ee5a
- evidence_id: support-2258-chemistry-execution
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
- evidence_id: support-2258-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/smiles/computed; /records/7/inchi/computed;
    /records/7/comparisons; /records/7/atom_correspondence; /records/7/smiles/status;
    /records/7/inchi/status
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Both stored forms give neutral C17H26O5, 22 heavy atoms and 23 bonds with
    equal standard InChI/full key and canonical isomeric/nonisomeric SMILES. Six potential
    tetrahedral centers are specified in each form; stereo_complete:true is consistent
    with those represented centers. Saved local tags differ with atom order, while
    the isomeric representation agrees. The supplied correspondence is one chirality-aware
    match and explicitly does not establish independent full graph or natural identity,
    absolute configuration from primary data, or identity with a stereochemical congener.
  snapshot_sha256: 9402e619ad45ee271669f7c409f81b7af6e2e529a58aed6239da2c56d05b22e2
- evidence_id: support-2258-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed; /records/7/inchi/computed
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Both complete paired tables describe fused six- and five-carbon rings,
    six specified tetrahedral centers, two aldehydes, a tertiary hydroxyl and one
    acetate ester. SMILES aldehydes are C7(=O8)H and C15(=O16)H, and acetate is C19(=O20)-O18-C3.
    No nitrogen, phosphorus, aromatic ring or saturated C5O candidate is present.
  snapshot_sha256: 9402e619ad45ee271669f7c409f81b7af6e2e529a58aed6239da2c56d05b22e2
- evidence_id: support-2258-stereo-method
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
- evidence_id: support-2258-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 982–1025
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Maintained seeder copies the lead structure and completeness flag, uses
    a returned classification to choose filing, and preserves named tool/version plus
    pathway/superclass/class/glycoside predictions.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2258-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 392–425
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Schema documents undefined stereocentres and requires computed classification
    to retain named tool/version. Computed classification is not a source assertion
    or an admission rationale.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2258-review-profile
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
- evidence_id: support-2258-source-notes
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
- evidence_id: support-2258-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/source_taxa; /records/7/source_scope_inventory/forward_taxon_merge_matches;
    /records/7/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Exact selected source-taxon set and bounded forward-merge/nonorganism routes.
    The forward-merge and nonorganism match lists are empty here; cached labels retain
    their historical scope and do not constitute live taxonomy verification.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-mechanism-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/declared_mechanism_roots_literal; /records/7/component_paths;
    /records/7/literal_mechanism_inventory; /records/7/proposed_companion_paths
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Selected literal mechanism roots and direct context membership for 2258;
    component list is empty. Positive unselected companions do not create an additional
    selected maintained-reader route.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 1}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 728–728
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete retained row payload: {"bgc_classes": "terpene", "bgc_subclasses":
    "Sesquiterpene", "cluster_link_evidence_basis": "CLUSTER_DEMONSTRATED", "compound_classes":
    "", "compound_index": "2", "compound_name": "8,9-epibotrydial", "database_ids":
    "npatlas:NPA019653", "entry_completeness": "complete", "entry_quality": "questionable",
    "entry_status": "active", "entry_version": "5", "genome_accession": "CP009816.1",
    "locus_evidence_methods": "Knock-out studies", "locus_from": "2216500", "locus_to":
    "2246000", "mibig_accession": "BGC0000631", "primary_reference": "DOI:10.1016/s0040-4020(99)00032-0",
    "producer_evidence_basis": "BGC_CHARACTERIZED", "reference_basis": "COMPOUND_EVIDENCE",
    "smiles": "C[C@@H]1C[C@@H]([C@@H]2[C@@]([C@H]1C=O)([C@](CC2(C)C)(C)C=O)O)OC(=O)C",
    "standard_inchi": "InChI=1S/C17H26O5/c1-10-6-13(22-11(2)20)14-15(3,4)8-16(5,9-19)17(14,21)12(10)7-18/h7,9-10,12-14,21H,6,8H2,1-5H3/t10-,12+,13+,14+,16+,17+/m1/s1",
    "standard_inchi_key": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:332648", "taxon_label": "Botrytis cinerea B05.10"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2258-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 0}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 2}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 8412–8412
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete retained row payload: {"organism_name": "Botrytis cinerea", "organism_wikidata":
    "http://www.wikidata.org/entity/Q1135851", "reference_doi": "10.1016/0006-2952(75)90029-5",
    "standard_inchi_key": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q105254261",
    "taxon_id": "NCBITaxon:40559"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2258-row-lotus_occurrences-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 8413–8413
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete retained row payload: {"organism_name": "Botrytis cinerea", "organism_wikidata":
    "http://www.wikidata.org/entity/Q1135851", "reference_doi": "10.1016/S0040-4020(99)00032-0",
    "standard_inchi_key": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q105254261",
    "taxon_id": "NCBITaxon:40559"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2258-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 0}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 1}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2253–2253
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete retained row payload: {"class_results": "Botryane sesquiterpenoids",
    "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "C[C@@H]1C[C@@H]([C@@H]2[C@@]([C@H]1C=O)([C@](CC2(C)C)(C)C=O)O)OC(=O)C",
    "standard_inchi_key": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "superclass_results": "Sesquiterpenoids"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2258-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 0}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 0}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact complete standard_inchi_key
    equality", "query": "SJFIYVCSGNWVPJ-PQVRDHEWSA-N", "positive_row_count": 0}. Empty
    results are scoped to this predicate and retained table, not the wider literature
    or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Retained local query frame: {"predicate": "exact chebi_id from exact full-key
    structure rows", "query": [], "positive_row_count": 0}. Empty results are scoped
    to this predicate and retained table, not the wider literature or live database.'
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-cache-40559
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: physical lines 18031–18038
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete cached stanza, not a fresh taxonomy response:

    [Term]

    id: NCBITaxon:40559

    name: Botrytis cinerea

    synonym: "Botryotinia fuckeliana" EXACT []

    synonym: "Botrytis cinerea Pers., 1801" EXACT []

    synonym: "Peziza fuckeliana" EXACT []

    synonym: "Sclerotinia fuckeliana" EXACT []


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2258-cache-332648
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: physical lines 83758–83762
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: 'Complete cached stanza, not a fresh taxonomy response:

    [Term]

    id: NCBITaxon:332648

    name: Botrytis cinerea B05.10

    synonym: "Botryotinia fuckeliana B05.10" EXACT []


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2258-companion-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/4
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-acc775e1b7 (1-epibotrydial),
    full key SJFIYVCSGNWVPJ-SDLFRHKASA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-1
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/5
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-1e06238f05 (10-dehydroxy
    dihydrobotrydialone), full key MBHVNAKPTPFWNG-MYFMSEKESA-N, with complete plaintext
    and all 2 history events plus its bounded source context. Its distinct owner assertions,
    stereochemistry, activity and mechanism annotations are not transferred to this
    selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-2
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/6
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-7950af79c1 (10-epi-dihydrobotrydial),
    full key QUGYVDURDBEQRB-VZJVBFQISA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-3
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/7
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-e2d62600f5 (10-Oxo-dihydrobotrydial),
    full key MFOUCDNLAFNKML-SVLWDWOGSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-4
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/8
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-7b45e48275 (10-Oxodehydrodihydrobotrydial),
    full key CAMCSBCRRUTMEK-OAHLLOKOSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-5
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/9
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-8b4cd14741 (10-Oxodihydrobotry-1(9),4(5)-diendial),
    full key PCEVLQFNPPWJEB-RFAUZJTJSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-6
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/10
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-bbb6f44666 (11-Hydroxydehydrobotrydienol),
    full key JUCMRFKOKIZVPS-OAHLLOKOSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-7
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/11
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-10fda622fe (12-hydroxydehydrobotrydienol),
    full key YPJRKTIWVUVMDI-LSDHHAIUSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-8
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/12
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-0bd6ab53bc (4β-Acetoxytetrahydrobotryslactone),
    full key RVXLTRZIAMMATE-JMTSMVSISA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-9
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/13
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context CHEBI:3159 (botrydial), full key SJFIYVCSGNWVPJ-GKKOWQTJSA-N,
    with complete plaintext and all 3 history events plus its bounded source context.
    Its distinct owner assertions, stereochemistry, activity and mechanism annotations
    are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-10
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/14
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-a1c6942987 (Botrydienal),
    full key CFAMAVBUWMXYLX-MEBBXXQBSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-11
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/15
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-d567f1a1cd (Botryenalol),
    full key DSVSTMJOGQEZJX-BYLNDYCFSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-12
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/16
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-79ce4aca52 (Botryendial),
    full key QWZKEROSOALLJP-BYLNDYCFSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-13
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/17
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-247120aa23 (Dehydrobotrydienol),
    full key UQQKKLVKVVJDEX-OAHLLOKOSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-14
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/18
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-b5ca742a5e (Dihydrobotrydial),
    full key QUGYVDURDBEQRB-CJNHKLDISA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-15
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/19
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-9b040d7e03 (Norbotrydialone
    acetate), full key OMZUEHMZFLBHNI-PCKWUFTNSA-N, with complete plaintext and all
    2 history events plus its bounded source context. Its distinct owner assertions,
    stereochemistry, activity and mechanism annotations are not transferred to this
    selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-16
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/20
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-2cef442430 (Secobotrydiene-3,10,15-triol),
    full key GYABYKLKVQPSPD-NVWZYQMFSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-17
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/21
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-f478b3a4f7 (Secobotrydiene-3,4,10,15-tetraol),
    full key GNMCOKDZWITFBO-MGNGBMTDSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-18
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/22
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-ff72b656ae (Secobotrytriendiol),
    full key BHNACKMCMDASDB-UJNBGNEJSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companion-19
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /raw_unselected_companions/23
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Retained direct context naturalproductmech:mibig-1c14174a30 (Secobotrytriene-10,12,15-triol),
    full key WLPOYIWCPMYYGM-KGRKPJGKSA-N, with complete plaintext and all 2 history
    events plus its bounded source context. Its distinct owner assertions, stereochemistry,
    activity and mechanism annotations are not transferred to this selected owner.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: support-2258-companions
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/7/proposed_companion_paths; /records/7/direct_companion_predicates
  accessed_at: '2026-11-03T16:30:19.393654Z'
  support: supports
  summary: Exactly 20 direct companion placements admitted under the saved root/full-key/owned-BGC
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
- assessment_id: support-2258-A1
  area: identity
  topic: Exact structure concept and grounding
  outcome: supported
  summary: The MINTED owner naturalproductmech:mibig-a2b74a45ae retains full key SJFIYVCSGNWVPJ-PQVRDHEWSA-N
    from BGC0000631 version 5 with source compound_index=2. The admitted ChEBI exact-full-key
    query has no match. Its 20 direct BGC0000631 companions have separate identities;
    Botrydial CHEBI:3159 has key SJFIYVCSGNWVPJ-GKKOWQTJSA-N, sharing a connectivity
    block but differing in stereochemical scope. That companion is not an interchangeable
    grounding for 8,9-epibotrydial.
  target_ids:
  - naturalproductmech:mibig-a2b74a45ae
  evidence_ids:
  - support-2258-owner
  - support-2258-capture
  - support-2258-source-plan
  - support-2258-query-chebi_structures
  - support-2258-row-mibig_compounds-0
  - support-2258-companions
  - support-2258-companion-0
  - support-2258-companion-1
  - support-2258-companion-2
  - support-2258-companion-3
  - support-2258-companion-4
  - support-2258-companion-5
  - support-2258-companion-6
  - support-2258-companion-7
  - support-2258-companion-8
  - support-2258-companion-9
  - support-2258-companion-10
  - support-2258-companion-11
  - support-2258-companion-12
  - support-2258-companion-13
  - support-2258-companion-14
  - support-2258-companion-15
  - support-2258-companion-16
  - support-2258-companion-17
  - support-2258-companion-18
  - support-2258-companion-19
  dimensions:
  - name: standard_inchi_key
    value: SJFIYVCSGNWVPJ-PQVRDHEWSA-N
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-owner
    - support-2258-capture
    - support-2258-source-plan
    - support-2258-query-chebi_structures
    - support-2258-row-mibig_compounds-0
    - support-2258-companions
    - support-2258-companion-0
    - support-2258-companion-1
    - support-2258-companion-2
    - support-2258-companion-3
    - support-2258-companion-4
    - support-2258-companion-5
    - support-2258-companion-6
    - support-2258-companion-7
    - support-2258-companion-8
    - support-2258-companion-9
    - support-2258-companion-10
    - support-2258-companion-11
    - support-2258-companion-12
    - support-2258-companion-13
    - support-2258-companion-14
    - support-2258-companion-15
    - support-2258-companion-16
    - support-2258-companion-17
    - support-2258-companion-18
    - support-2258-companion-19
  - name: grounding_scope
    value: The MINTED owner naturalproductmech:mibig-a2b74a45ae retains full key SJFIYVCSGNWVPJ-PQVRDHEWSA-N
      from BGC0000631 version 5 with source compound_index=2. The admitted ChEBI exact-full-key
      query has no match. Its 20 direct BGC0000631 companions have separate identities;
      Botrydial CHEBI:3159 has key SJFIYVCSGNWVPJ-GKKOWQTJSA-N, sharing a connectivity
      block but differing in stereochemical scope. That companion is not an interchangeable
      grounding for 8,9-epibotrydial.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-owner
    - support-2258-capture
    - support-2258-source-plan
    - support-2258-query-chebi_structures
    - support-2258-row-mibig_compounds-0
    - support-2258-companions
    - support-2258-companion-0
    - support-2258-companion-1
    - support-2258-companion-2
    - support-2258-companion-3
    - support-2258-companion-4
    - support-2258-companion-5
    - support-2258-companion-6
    - support-2258-companion-7
    - support-2258-companion-8
    - support-2258-companion-9
    - support-2258-companion-10
    - support-2258-companion-11
    - support-2258-companion-12
    - support-2258-companion-13
    - support-2258-companion-14
    - support-2258-companion-15
    - support-2258-companion-16
    - support-2258-companion-17
    - support-2258-companion-18
    - support-2258-companion-19
- assessment_id: support-2258-A2
  area: representation
  topic: Stored representation and stereochemistry
  outcome: supported
  summary: Both stored forms give neutral C17H26O5, 22 heavy atoms and 23 bonds with
    equal standard InChI/full key and canonical isomeric/nonisomeric SMILES. Six potential
    tetrahedral centers are specified in each form; stereo_complete:true is consistent
    with those represented centers. Saved local tags differ with atom order, while
    the isomeric representation agrees. The supplied correspondence is one chirality-aware
    match and explicitly does not establish independent full graph or natural identity,
    absolute configuration from primary data, or identity with a stereochemical congener.
  target_ids:
  - naturalproductmech:mibig-a2b74a45ae
  evidence_ids:
  - support-2258-owner
  - support-2258-chemistry
  - support-2258-stereo-method
  - support-2258-seeder
  - support-2258-structure-schema
  dimensions:
  - name: stereochemical_resolution
    value: Six specified tetrahedral centers; both canonical comparisons true; no
      epimer transfer.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-owner
    - support-2258-chemistry
    - support-2258-stereo-method
    - support-2258-seeder
    - support-2258-structure-schema
  - name: representation_correspondence
    value: Both stored forms give neutral C17H26O5, 22 heavy atoms and 23 bonds with
      equal standard InChI/full key and canonical isomeric/nonisomeric SMILES. Six
      potential tetrahedral centers are specified in each form; stereo_complete:true
      is consistent with those represented centers. Saved local tags differ with atom
      order, while the isomeric representation agrees. The supplied correspondence
      is one chirality-aware match and explicitly does not establish independent full
      graph or natural identity, absolute configuration from primary data, or identity
      with a stereochemical congener.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-owner
    - support-2258-chemistry
    - support-2258-stereo-method
    - support-2258-seeder
    - support-2258-structure-schema
- assessment_id: support-2258-A3
  area: provenance
  topic: Producer, locus, taxon and strain roles
  outcome: supported
  summary: MIBiG BGC0000631 version 5 is active with source quality questionable and
    completeness complete. The producer Botrytis cinerea B05.10 strain NCBITaxon:332648
    is BGC_CHARACTERIZED; its locus is separately CLUSTER_DEMONSTRATED with Knock-out
    studies. CP009816.1 coordinates 2216500..2246000 are retained. The two LOTUS occurrences
    instead refer to species Botrytis cinerea 40559. The cached strain and species
    labels support the written distinction, not an upgrade or fresh taxonomic/experimental
    verification.
  target_ids:
  - naturalproductmech:mibig-a2b74a45ae
  evidence_ids:
  - support-2258-owner
  - support-2258-capture
  - support-2258-source-plan
  - support-2258-row-mibig_compounds-0
  - support-2258-row-lotus_occurrences-0
  - support-2258-row-lotus_occurrences-1
  - support-2258-taxonomy-routes
  - support-2258-cache-40559
  - support-2258-cache-332648
  - support-2258-source-notes
  dimensions:
  - name: taxon_and_strain_scope
    value: MIBiG BGC0000631 version 5 is active with source quality questionable and
      completeness complete. The producer Botrytis cinerea B05.10 strain NCBITaxon:332648
      is BGC_CHARACTERIZED; its locus is separately CLUSTER_DEMONSTRATED with Knock-out
      studies. CP009816.1 coordinates 2216500..2246000 are retained. The two LOTUS
      occurrences instead refer to species Botrytis cinerea 40559. The cached strain
      and species labels support the written distinction, not an upgrade or fresh
      taxonomic/experimental verification.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-owner
    - support-2258-capture
    - support-2258-source-plan
    - support-2258-row-mibig_compounds-0
    - support-2258-row-lotus_occurrences-0
    - support-2258-row-lotus_occurrences-1
    - support-2258-taxonomy-routes
    - support-2258-cache-40559
    - support-2258-cache-332648
    - support-2258-source-notes
  - name: producer_evidence_tier
    value: BGC_CHARACTERIZED; Botrytis cinerea B05.10 strain 332648, distinct from
      occurrence species 40559.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-owner
    - support-2258-capture
    - support-2258-source-plan
    - support-2258-row-mibig_compounds-0
    - support-2258-row-lotus_occurrences-0
    - support-2258-row-lotus_occurrences-1
    - support-2258-taxonomy-routes
    - support-2258-cache-40559
    - support-2258-cache-332648
    - support-2258-source-notes
  - name: locus_evidence_tier
    value: CLUSTER_DEMONSTRATED; BGC0000631 v5 active; Knock-out studies retained.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-owner
    - support-2258-capture
    - support-2258-source-plan
    - support-2258-row-mibig_compounds-0
    - support-2258-row-lotus_occurrences-0
    - support-2258-row-lotus_occurrences-1
    - support-2258-taxonomy-routes
    - support-2258-cache-40559
    - support-2258-cache-332648
    - support-2258-source-notes
- assessment_id: support-2258-A4
  area: evidence
  topic: Citation placement and primary-source limits
  outcome: supported
  summary: The source producer/locus claim retains compound-level DOI:10.1016/s0040-4020(99)00032-0
    as DATABASE_ASSERTION. The two LOTUS triples cite DOI:10.1016/0006-2952(75)90029-5
    and DOI:10.1016/S0040-4020(99)00032-0. The case-varied 1999 DOI is not independent
    corroboration of the MIBiG citation. Companion publications and Botrydial's mechanism
    evidence retain their own owners and roles; no primary paper was inspected anew.
  target_ids:
  - naturalproductmech:mibig-a2b74a45ae
  evidence_ids:
  - support-2258-owner
  - support-2258-capture
  - support-2258-source-plan
  - support-2258-row-mibig_compounds-0
  - support-2258-row-lotus_occurrences-0
  - support-2258-row-lotus_occurrences-1
  dimensions:
  - name: citation_scope
    value: The source producer/locus claim retains compound-level DOI:10.1016/s0040-4020(99)00032-0
      as DATABASE_ASSERTION. The two LOTUS triples cite DOI:10.1016/0006-2952(75)90029-5
      and DOI:10.1016/S0040-4020(99)00032-0. The case-varied 1999 DOI is not independent
      corroboration of the MIBiG citation. Companion publications and Botrydial's
      mechanism evidence retain their own owners and roles; no primary paper was inspected
      anew.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-owner
    - support-2258-capture
    - support-2258-source-plan
    - support-2258-row-mibig_compounds-0
    - support-2258-row-lotus_occurrences-0
    - support-2258-row-lotus_occurrences-1
- assessment_id: support-2258-A5
  area: scope
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: Both written occurrence objects concern Botrytis cinerea species 40559
    and preserve their separate retained references. PubChem, BindingDB, related-corpus,
    CyanometDB and ChEBI-origin queries contain no selected-key positive row in this
    inventory scope. No activity summary, assay object or molecular target is written
    for the owner. Botrydial's cytotoxic definition, mechanism assertions and other
    companion observations do not establish this epimer's biological activity or pathway;
    no such transfer is made.
  target_ids:
  - naturalproductmech:mibig-a2b74a45ae
  evidence_ids:
  - support-2258-owner
  - support-2258-capture
  - support-2258-source-plan
  - support-2258-query-mibig_compounds
  - support-2258-query-chebi_structures
  - support-2258-query-lotus_occurrences
  - support-2258-query-cyanometdb_occurrences
  - support-2258-query-npclassifier
  - support-2258-query-pubchem_bioassay
  - support-2258-query-bindingdb_targets
  - support-2258-query-antibioticmech_inchikeys
  - support-2258-query-chebi_origins
  - support-2258-row-lotus_occurrences-0
  - support-2258-row-lotus_occurrences-1
  - support-2258-mechanism-scope
  - support-2258-companions
  - support-2258-companion-0
  - support-2258-companion-1
  - support-2258-companion-2
  - support-2258-companion-3
  - support-2258-companion-4
  - support-2258-companion-5
  - support-2258-companion-6
  - support-2258-companion-7
  - support-2258-companion-8
  - support-2258-companion-9
  - support-2258-companion-10
  - support-2258-companion-11
  - support-2258-companion-12
  - support-2258-companion-13
  - support-2258-companion-14
  - support-2258-companion-15
  - support-2258-companion-16
  - support-2258-companion-17
  - support-2258-companion-18
  - support-2258-companion-19
  dimensions:
  - name: occurrence_scope
    value: Both written occurrence objects concern Botrytis cinerea species 40559
      and preserve their separate retained references. PubChem, BindingDB, related-corpus,
      CyanometDB and ChEBI-origin queries contain no selected-key positive row in
      this inventory scope. No activity summary, assay object or molecular target
      is written for the owner. Botrydial's cytotoxic definition, mechanism assertions
      and other companion observations do not establish this epimer's biological activity
      or pathway; no such transfer is made.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-owner
    - support-2258-capture
    - support-2258-source-plan
    - support-2258-query-mibig_compounds
    - support-2258-query-chebi_structures
    - support-2258-query-lotus_occurrences
    - support-2258-query-cyanometdb_occurrences
    - support-2258-query-npclassifier
    - support-2258-query-pubchem_bioassay
    - support-2258-query-bindingdb_targets
    - support-2258-query-antibioticmech_inchikeys
    - support-2258-query-chebi_origins
    - support-2258-row-lotus_occurrences-0
    - support-2258-row-lotus_occurrences-1
    - support-2258-mechanism-scope
    - support-2258-companions
    - support-2258-companion-0
    - support-2258-companion-1
    - support-2258-companion-2
    - support-2258-companion-3
    - support-2258-companion-4
    - support-2258-companion-5
    - support-2258-companion-6
    - support-2258-companion-7
    - support-2258-companion-8
    - support-2258-companion-9
    - support-2258-companion-10
    - support-2258-companion-11
    - support-2258-companion-12
    - support-2258-companion-13
    - support-2258-companion-14
    - support-2258-companion-15
    - support-2258-companion-16
    - support-2258-companion-17
    - support-2258-companion-18
    - support-2258-companion-19
  - name: assay_scope
    value: Both written occurrence objects concern Botrytis cinerea species 40559
      and preserve their separate retained references. PubChem, BindingDB, related-corpus,
      CyanometDB and ChEBI-origin queries contain no selected-key positive row in
      this inventory scope. No activity summary, assay object or molecular target
      is written for the owner. Botrydial's cytotoxic definition, mechanism assertions
      and other companion observations do not establish this epimer's biological activity
      or pathway; no such transfer is made.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-owner
    - support-2258-capture
    - support-2258-source-plan
    - support-2258-query-mibig_compounds
    - support-2258-query-chebi_structures
    - support-2258-query-lotus_occurrences
    - support-2258-query-cyanometdb_occurrences
    - support-2258-query-npclassifier
    - support-2258-query-pubchem_bioassay
    - support-2258-query-bindingdb_targets
    - support-2258-query-antibioticmech_inchikeys
    - support-2258-query-chebi_origins
    - support-2258-row-lotus_occurrences-0
    - support-2258-row-lotus_occurrences-1
    - support-2258-mechanism-scope
    - support-2258-companions
    - support-2258-companion-0
    - support-2258-companion-1
    - support-2258-companion-2
    - support-2258-companion-3
    - support-2258-companion-4
    - support-2258-companion-5
    - support-2258-companion-6
    - support-2258-companion-7
    - support-2258-companion-8
    - support-2258-companion-9
    - support-2258-companion-10
    - support-2258-companion-11
    - support-2258-companion-12
    - support-2258-companion-13
    - support-2258-companion-14
    - support-2258-companion-15
    - support-2258-companion-16
    - support-2258-companion-17
    - support-2258-companion-18
    - support-2258-companion-19
- assessment_id: support-2258-A6
  area: other
  topic: Computed classification and complete saved topology
  outcome: supported
  summary: NPClassifier returns Terpenoids / Sesquiterpenoids / Botryane sesquiterpenoids
    and is_glycoside:false at the recorded model version. The complete saved SMILES
    graph has fused six- and five-carbon rings, six specified centers, two aldehydes
    C7(=O8)H and C15(=O16)H, a tertiary hydroxyl at C5 and acetate C19(=O20)-O18-C3.
    The InChI-derived form preserves these features with different indices. No nitrogen,
    phosphorus, aromatic ring or sugar candidate is present. The model label is compatible
    with this structural description but remains a computed prediction, not independent
    biosynthetic or natural-identity evidence.
  target_ids:
  - naturalproductmech:mibig-a2b74a45ae
  evidence_ids:
  - support-2258-capture
  - support-2258-topology
  - support-2258-row-npclassifier-0
  - support-2258-row-mibig_compounds-0
  - support-2258-seeder
  - support-2258-structure-schema
  dimensions:
  - name: computed_classification
    value: NPClassifier returns Terpenoids / Sesquiterpenoids / Botryane sesquiterpenoids
      and is_glycoside:false at the recorded model version. The complete saved SMILES
      graph has fused six- and five-carbon rings, six specified centers, two aldehydes
      C7(=O8)H and C15(=O16)H, a tertiary hydroxyl at C5 and acetate C19(=O20)-O18-C3.
      The InChI-derived form preserves these features with different indices. No nitrogen,
      phosphorus, aromatic ring or sugar candidate is present. The model label is
      compatible with this structural description but remains a computed prediction,
      not independent biosynthetic or natural-identity evidence.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2258-capture
    - support-2258-topology
    - support-2258-row-npclassifier-0
    - support-2258-row-mibig_compounds-0
    - support-2258-seeder
    - support-2258-structure-schema
- assessment_id: support-2258-A7
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
  - naturalproductmech:mibig-a2b74a45ae
  evidence_ids:
  - support-2258-intake
  - support-2258-plan-acceptance
  - support-2258-intake-acceptance
  - support-2258-diagnostic-acceptance
  - support-2258-native-gates
  - support-2258-chemistry-execution
  - support-2258-review-profile
  - support-2258-source-notes
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
    - support-2258-intake
    - support-2258-plan-acceptance
    - support-2258-intake-acceptance
    - support-2258-diagnostic-acceptance
    - support-2258-native-gates
    - support-2258-chemistry-execution
    - support-2258-review-profile
    - support-2258-source-notes
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
