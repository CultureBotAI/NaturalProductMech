# Local evidence review: 4β-Acetoxytetrahydrobotryslactone

- Review: 20261103T154045Z-4-acetoxytetrahydrobotryslactone
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T15:06:55.226329Z
- Finished UTC: 2026-11-03T15:40:45.030452Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified partial review: the lactone/acetate topology and exact paired forms agree, while strain-level BGC evidence remains distinct from the single species occurrence. The twenty congeners and Botrydial graph are context only.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2248; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-0bd6ab53bc | data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml | generated | 4β-Acetoxytetrahydrobotryslactone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-0bd6ab53bc | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-0bd6ab53bc | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-0bd6ab53bc | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-0bd6ab53bc | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-0bd6ab53bc | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-0bd6ab53bc | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-0bd6ab53bc | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-0bd6ab53bc | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding

identity: supported. Targets: naturalproductmech:mibig-0bd6ab53bc.

The MINTED owner naturalproductmech:mibig-0bd6ab53bc retains label 4β-Acetoxytetrahydrobotryslactone and full key RVXLTRZIAMMATE-JMTSMVSISA-N from BGC0000631 version 5, source compound_index=21. The exact full-key ChEBI predicate is empty. Twenty distinct direct congeners contextualize this source cluster without resolving nomenclature or supplying a different structure.

### Stored representations and stereo resolution

representation: supported. Targets: naturalproductmech:mibig-0bd6ab53bc.

Both saved forms are neutral C20H30O6 with 26 atoms and 28 bonds. Six tetrahedral centers are specified and no unspecified potential entry is reported; literal stereo_complete:true is retained. SMILES centers C1 R, C3 S, C4 S, C7 S, C9 R and C14 S describe this stored form. Ring C5=C6 is not an unassigned potential double bond in the saved table. No natural stereochemical assignment is newly established. All ten saved paired comparisons pass; complete stored atom correspondence is explicitly limited to a chirality-aware match and does not establish independent full-graph or natural identity.

### Producer, locus and taxonomy scope

provenance: supported. Targets: naturalproductmech:mibig-0bd6ab53bc.

Botrytis cinerea B05.10 NCBITaxon:332648 is graded BGC_CHARACTERIZED. BGC0000631 version 5, active/questionable/complete, spans CP009816.1:2216500–2246000 and retains knockout evidence with CLUSTER_DEMONSTRATED. A separate LOTUS occurrence uses Botrytis cinerea species NCBITaxon:40559. Cached Botryotinia fuckeliana synonyms preserve the species and B05.10 strain scopes separately; they do not collapse occurrence into a strain-level producer claim.

### Citation placement and historical verification scope

evidence: supported. Targets: naturalproductmech:mibig-0bd6ab53bc.

DOI:10.1021/np020107v is a COMPOUND_EVIDENCE reference in MIBiG. The single LOTUS DOI:10.1021/NP020107V differs only in case and does not establish an independent experiment. Generated evidence remains DATABASE_ASSERTION; no original article or sequence was inspected.

### Occurrence, assay and companion boundaries

scope: supported. Targets: naturalproductmech:mibig-0bd6ab53bc.

One retained LOTUS species occurrence is written. The exact selected PubChem, BindingDB, AntibioticMech, CyanoMetDB and ChEBI-origin queries are empty. Twenty direct BGC0000631 congeners have distinct full keys and remain context. In particular, unselected Botrydial's inline causal graph is not this compound's pathway, protein, producer or assay evidence; no selected maintained reader applies.

### Computed classification and complete-table topology limits

other: supported. Targets: naturalproductmech:mibig-0bd6ab53bc.

The saved graph contains a five-membered lactone C10(=O11)–O12–C7 in ring [7,8,9,10,12] and a separate acetate C23(=O24)–O22–C3 with methyl C25. Hydroxyl O13 is attached to C9 and O21 to CH2 C20. Three perceived rings and ring alkene C5=C6 remain explicit. The C5O candidate list is empty; no sugar residue is assigned. These graph facts support a bounded lactone/acetate interpretation without proving natural-product naming or a biosynthetic pathway. NPClassifier npclassifier.gnps2.org@2026-09-07 reports Terpenoids, Sesquiterpenoids, Botryane sesquiterpenoids and is_glycoside:false. This is a versioned computed prediction, distinct from retained BGC/compound-class assertions and from independently established biosynthesis.

### Partial completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-0bd6ab53bc.

The actual 57-input canonical intake, admitted plan and original paired computation support a partial scientific review. No selected mechanism root or component is present, so no selected maintained reader applies. Five local gates passed; FullQC, complete OAK and fresh external primary-source verification remain unavailable. No scientific source record or curation history was edited.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2248-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml; lines 1–92 | supports | Whole current plaintext owner and all 2 history events. Literal identifier naturalproductmech:mibig-0bd6ab53bc, label 4β-Acetoxytetrahydrobotryslactone and full key RVXLTRZIAMMATE-JMTSMVSISA-N. Historical events remain retained claims, not fresh scientific verification. |
| support-2248-capture | /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json; /records/7/owner_document; /records/7/owner_pin | supports | Exact captured complete owner, including structure, provenance, occurrences or assays where written, computed classification, grounding and history. |
| support-2248-source-plan | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7 | supports | Complete admitted selected source context, including all nine retained query frames and full payloads, 57 inputs and 20 direct companion paths. This is a local inventory scope. |
| support-2248-intake | /private/tmp/npm-review-work/shared-next-batch225/intakes/2248-inspect-001.json; /status; /source; /targets | supports | Original canonical inspection of exact target and source ownership with current input snapshots; inspection is not a scientific verdict. |
| support-2248-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch225/root-input-plan-acceptance-001.json; /accepted; /status; /plan; /inventory; /source_notes; /source_placements; /unique_source_paths | supports | ROOT accepts the actual saved plan with 412 input placements and 77 unique paths. |
| support-2248-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch225/root-intake-ready-001.json; /accepted; /status; /intake_summary; /intakes_execution; /source_placements; /unique_source_paths; /mechanism_owner_orders | supports | ROOT accepts all ten original canonical intakes and exact 412/77 snapshots; only 2245 is a selected mechanism owner. |
| support-2248-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch225/root-local-diagnostics-acceptance-001.json; /status; /DATA; /execution; /native_gate_acceptance; /successful_forms; /comparison_flags_true; /global_stderr_warnings; /full_QC_and_OAK | supports | ROOT accepts the original twenty stored-form parses and 100 true paired comparisons with current inputs. The two stderr warnings remain global and unassigned. FullQC and complete OAK are unavailable; the separate native gate receipt is linked. |
| support-2248-native-gates | /private/tmp/npm-review-work/shared-next-batch225/root-native-five-gates-acceptance-001.json; /accepted; /status; /results; /full_QC_available; /complete_OAK_authority_available; /all_native_gates_passed | supports | Five local commands passed; FullQC and complete OAK remain unavailable, so all_native_gates_passed is false. This mechanical acceptance does not establish scientific completeness. |
| support-2248-chemistry-execution | /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-execution-001.json; /started_at; /finished_at; /exit_code; /DATA; /stdout; /stderr; /external_requests; /retries | supports | Original saved chemistry execution exited zero. The original stdout and 92-byte stderr stream are pinned separately; no retry or external request is recorded. |
| support-2248-chemistry | /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/smiles/computed; /records/7/inchi/computed; /records/7/comparisons; /records/7/atom_correspondence; /records/7/smiles/status; /records/7/inchi/status | supports | Both saved forms parsed; all ten paired comparison flags are true, including full key, formula and both canonical SMILES comparisons. A complete chirality-aware atom match is stored, with full_graph_identity_established:false. Literal stereo_complete:true. Both saved forms are neutral C20H30O6 with 26 atoms and 28 bonds. Six tetrahedral centers are specified and no unspecified potential entry is reported; literal stereo_complete:true is retained. SMILES centers C1 R, C3 S, C4 S, C7 S, C9 R and C14 S describe this stored form. Ring C5=C6 is not an unassigned potential double bond in the saved table. No natural stereochemical assignment is newly established. |
| support-2248-topology | /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed; /records/7/inchi/computed | supports | The saved graph contains a five-membered lactone C10(=O11)–O12–C7 in ring [7,8,9,10,12] and a separate acetate C23(=O24)–O22–C3 with methyl C25. Hydroxyl O13 is attached to C9 and O21 to CH2 C20. Three perceived rings and ring alkene C5=C6 remain explicit. The C5O candidate list is empty; no sugar residue is assigned. These graph facts support a bounded lactone/acetate interpretation without proving natural-product naming or a biosynthetic pathway. |
| support-2248-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–173 | supports | The maintained structure_fields calculation uses FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False) and sets stereo_complete by absence of ? atom-center labels. It does not separately test potential double-bond geometry. |
| support-2248-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 982–1019 | supports | The maintained seeder retains lead structure/key, copies stereo_complete, stores the matched ChEBI definition, and records versioned NPClassifier output separately. Code reading only; no new extraction or seeding. |
| support-2248-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392–425 | supports | The stereo_complete description addresses undefined stereocentres; ComputedClassification explicitly denotes a named/versioned prediction, never a source assertion or record-admission reason. |
| support-2248-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; lines 35–57 | supports | The local review profile separates exact structure, provenance, evidence tiers and computed filing classification. Seeded content belongs to maintained inventories/extractors/seeder; reserved decisions.tsv is not consumed. Saving a review does not promote native status or append history. |
| support-2248-source-notes | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-source-scope-notes-001.json; /reading; /curation; /cautions; /totals | supports | The source notes attribute the disjoint complete reading of 36 current contexts, 324 query frames and 272 positive placements, 26 cached stanzas and bounded implemented-curation scan. Source assertions, companion claims, model predictions and cached taxonomy remain separately scoped. |
| support-2248-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/source_scope_inventory/source_taxa; /records/7/source_scope_inventory/forward_taxon_merge_matches; /records/7/source_scope_inventory/nonorganism_matches | supports | Selected source taxa ["NCBITaxon:332648", "NCBITaxon:40559"]. Forward-merge matches []; non-organism matches []. No live taxonomy query. |
| support-2248-mechanism-scope | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/declared_mechanism_roots_literal; /records/7/component_paths; /records/7/literal_mechanism_inventory; /records/7/proposed_companion_paths | supports | The selected owner has no pathway, graph, component-reference or molecular-target root. Positive unselected context does not create selected reader applicability or verified biological absence. |
| support-2248-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/source_scope_inventory/joins/mibig_compounds | supports | Saved query frame: predicate="exact complete standard_inchi_key equality"; query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=1. Empty results are limited to this saved predicate and inventory. |
| support-2248-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 747–747 | supports | Complete retained physical TSV payload: {"mibig_accession":"BGC0000631","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"4β-Acetoxytetrahydrobotryslactone","compound_index":"21","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1[C@@H]3C[C@H](C(=O)O3)O)[C@@](CC2(C)C)(C)CO)OC(=O)C","standard_inchi":"InChI=1S/C20H30O6/c1-10-6-14(25-11(2)22)16-17(20(5,9-21)8-19(16,3)4)15(10)13-7-12(23)18(24)26-13/h10,12-14,16,21,23H,6-9H2,1-5H3/t10-,12-,13+,14+,16-,20-/m1/s1","standard_inchi_key":"RVXLTRZIAMMATE-JMTSMVSISA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA002526","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis cinerea B05.10","bgc_classes":"terpene","bgc_subclasses":"Sesquiterpene","genome_accession":"CP009816.1","locus_from":"2216500","locus_to":"2246000","locus_evidence_methods":"Knock-out studies","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"DOI:10.1021/np020107v","reference_basis":"COMPOUND_EVIDENCE"} |
| support-2248-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/source_scope_inventory/joins/chebi_structures | supports | Saved query frame: predicate="exact complete standard_inchi_key equality"; query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=0. Empty results are limited to this saved predicate and inventory. |
| support-2248-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/source_scope_inventory/joins/lotus_occurrences | supports | Saved query frame: predicate="exact complete standard_inchi_key equality"; query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=1. Empty results are limited to this saved predicate and inventory. |
| support-2248-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 8247–8247 | supports | Complete retained physical TSV payload: {"standard_inchi_key":"RVXLTRZIAMMATE-JMTSMVSISA-N","organism_name":"Botrytis cinerea","taxon_id":"NCBITaxon:40559","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1021/NP020107V","structure_wikidata":"http://www.wikidata.org/entity/Q75067586"} |
| support-2248-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved query frame: predicate="exact complete standard_inchi_key equality"; query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=0. Empty results are limited to this saved predicate and inventory. |
| support-2248-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/source_scope_inventory/joins/npclassifier | supports | Saved query frame: predicate="exact complete standard_inchi_key equality"; query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=1. Empty results are limited to this saved predicate and inventory. |
| support-2248-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2184–2184 | supports | Complete retained physical TSV payload: {"standard_inchi_key":"RVXLTRZIAMMATE-JMTSMVSISA-N","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1[C@@H]3C[C@H](C(=O)O3)O)[C@@](CC2(C)C)(C)CO)OC(=O)C","pathway_results":"Terpenoids","superclass_results":"Sesquiterpenoids","class_results":"Botryane sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"} |
| support-2248-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/source_scope_inventory/joins/pubchem_bioassay | supports | Saved query frame: predicate="exact complete standard_inchi_key equality"; query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=0. Empty results are limited to this saved predicate and inventory. |
| support-2248-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/source_scope_inventory/joins/bindingdb_targets | supports | Saved query frame: predicate="exact complete standard_inchi_key equality"; query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=0. Empty results are limited to this saved predicate and inventory. |
| support-2248-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved query frame: predicate="exact complete standard_inchi_key equality"; query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=0. Empty results are limited to this saved predicate and inventory. |
| support-2248-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/source_scope_inventory/joins/chebi_origins | supports | Saved query frame: predicate="exact chebi_id from exact full-key structure rows"; query=[]; complete positive match count=0. Empty results are limited to this saved predicate and inventory. |
| support-2248-cache-40559 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; physical lines 18031–18038 | supports | Whole cached stanza, including literal synonym scope; not live taxonomy: [Term]<br>id: NCBITaxon:40559<br>name: Botrytis cinerea<br>synonym: "Botryotinia fuckeliana" EXACT []<br>synonym: "Botrytis cinerea Pers., 1801" EXACT []<br>synonym: "Peziza fuckeliana" EXACT []<br>synonym: "Sclerotinia fuckeliana" EXACT []<br><br> |
| support-2248-cache-332648 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; physical lines 83758–83762 | supports | Whole cached stanza, including literal synonym scope; not live taxonomy: [Term]<br>id: NCBITaxon:332648<br>name: Botrytis cinerea B05.10<br>synonym: "Botryotinia fuckeliana B05.10" EXACT []<br><br> |
| support-2248-companion-0 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/0 | supports | Complete admitted companion raw text/history and retained source scope for 1-epibotrydial (naturalproductmech:mibig-acc775e1b7), full key SJFIYVCSGNWVPJ-SDLFRHKASA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-1 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/1 | supports | Complete admitted companion raw text/history and retained source scope for 10-dehydroxy dihydrobotrydialone (naturalproductmech:mibig-1e06238f05), full key MBHVNAKPTPFWNG-MYFMSEKESA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-2 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/2 | supports | Complete admitted companion raw text/history and retained source scope for 10-epi-dihydrobotrydial (naturalproductmech:mibig-7950af79c1), full key QUGYVDURDBEQRB-VZJVBFQISA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-3 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/3 | supports | Complete admitted companion raw text/history and retained source scope for 10-Oxo-dihydrobotrydial (naturalproductmech:mibig-e2d62600f5), full key MFOUCDNLAFNKML-SVLWDWOGSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-4 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/4 | supports | Complete admitted companion raw text/history and retained source scope for 10-Oxodehydrodihydrobotrydial (naturalproductmech:mibig-7b45e48275), full key CAMCSBCRRUTMEK-OAHLLOKOSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-5 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/5 | supports | Complete admitted companion raw text/history and retained source scope for 10-Oxodihydrobotry-1(9),4(5)-diendial (naturalproductmech:mibig-8b4cd14741), full key PCEVLQFNPPWJEB-RFAUZJTJSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-6 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/6 | supports | Complete admitted companion raw text/history and retained source scope for 11-Hydroxydehydrobotrydienol (naturalproductmech:mibig-bbb6f44666), full key JUCMRFKOKIZVPS-OAHLLOKOSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-7 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/7 | supports | Complete admitted companion raw text/history and retained source scope for 12-hydroxydehydrobotrydienol (naturalproductmech:mibig-10fda622fe), full key YPJRKTIWVUVMDI-LSDHHAIUSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-8 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/9 | supports | Complete admitted companion raw text/history and retained source scope for 8,9-epibotrydial (naturalproductmech:mibig-a2b74a45ae), full key SJFIYVCSGNWVPJ-PQVRDHEWSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-9 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/12 | supports | Complete admitted companion raw text/history and retained source scope for botrydial (CHEBI:3159), full key SJFIYVCSGNWVPJ-GKKOWQTJSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-10 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/13 | supports | Complete admitted companion raw text/history and retained source scope for Botrydienal (naturalproductmech:mibig-a1c6942987), full key CFAMAVBUWMXYLX-MEBBXXQBSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-11 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/14 | supports | Complete admitted companion raw text/history and retained source scope for Botryenalol (naturalproductmech:mibig-d567f1a1cd), full key DSVSTMJOGQEZJX-BYLNDYCFSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-12 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/15 | supports | Complete admitted companion raw text/history and retained source scope for Botryendial (naturalproductmech:mibig-79ce4aca52), full key QWZKEROSOALLJP-BYLNDYCFSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-13 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/17 | supports | Complete admitted companion raw text/history and retained source scope for Dehydrobotrydienol (naturalproductmech:mibig-247120aa23), full key UQQKKLVKVVJDEX-OAHLLOKOSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-14 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/18 | supports | Complete admitted companion raw text/history and retained source scope for Dihydrobotrydial (naturalproductmech:mibig-b5ca742a5e), full key QUGYVDURDBEQRB-CJNHKLDISA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-15 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/21 | supports | Complete admitted companion raw text/history and retained source scope for Norbotrydialone acetate (naturalproductmech:mibig-9b040d7e03), full key OMZUEHMZFLBHNI-PCKWUFTNSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-16 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/22 | supports | Complete admitted companion raw text/history and retained source scope for Secobotrydiene-3,10,15-triol (naturalproductmech:mibig-2cef442430), full key GYABYKLKVQPSPD-NVWZYQMFSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-17 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/23 | supports | Complete admitted companion raw text/history and retained source scope for Secobotrydiene-3,4,10,15-tetraol (naturalproductmech:mibig-f478b3a4f7), full key GNMCOKDZWITFBO-MGNGBMTDSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-18 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/24 | supports | Complete admitted companion raw text/history and retained source scope for Secobotrytriendiol (naturalproductmech:mibig-ff72b656ae), full key BHNACKMCMDASDB-UJNBGNEJSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companion-19 | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /raw_unselected_companions/25 | supports | Complete admitted companion raw text/history and retained source scope for Secobotrytriene-10,12,15-triol (naturalproductmech:mibig-1c14174a30), full key WLPOYIWCPMYYGM-KGRKPJGKSA-N. It is direct context, not a selected assay, mechanism or stereochemistry transfer. |
| support-2248-companions | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/7/proposed_companion_paths; /records/7/direct_companion_predicates; /raw_unselected_companions | supports | Exact direct context under the admitted one-hop predicates. Distinct owner identities: [{"path":"data/natural_products/terpenoids/1-epibotrydial.yaml","identifier":"naturalproductmech:mibig-acc775e1b7","label":"1-epibotrydial","standard_inchi_key":"SJFIYVCSGNWVPJ-SDLFRHKASA-N"},{"path":"data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml","identifier":"naturalproductmech:mibig-1e06238f05","label":"10-dehydroxy dihydrobotrydialone","standard_inchi_key":"MBHVNAKPTPFWNG-MYFMSEKESA-N"},{"path":"data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml","identifier":"naturalproductmech:mibig-7950af79c1","label":"10-epi-dihydrobotrydial","standard_inchi_key":"QUGYVDURDBEQRB-VZJVBFQISA-N"},{"path":"data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml","identifier":"naturalproductmech:mibig-e2d62600f5","label":"10-Oxo-dihydrobotrydial","standard_inchi_key":"MFOUCDNLAFNKML-SVLWDWOGSA-N"},{"path":"data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml","identifier":"naturalproductmech:mibig-7b45e48275","label":"10-Oxodehydrodihydrobotrydial","standard_inchi_key":"CAMCSBCRRUTMEK-OAHLLOKOSA-N"},{"path":"data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml","identifier":"naturalproductmech:mibig-8b4cd14741","label":"10-Oxodihydrobotry-1(9),4(5)-diendial","standard_inchi_key":"PCEVLQFNPPWJEB-RFAUZJTJSA-N"},{"path":"data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml","identifier":"naturalproductmech:mibig-bbb6f44666","label":"11-Hydroxydehydrobotrydienol","standard_inchi_key":"JUCMRFKOKIZVPS-OAHLLOKOSA-N"},{"path":"data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml","identifier":"naturalproductmech:mibig-10fda622fe","label":"12-hydroxydehydrobotrydienol","standard_inchi_key":"YPJRKTIWVUVMDI-LSDHHAIUSA-N"},{"path":"data/natural_products/terpenoids/8-9-epibotrydial.yaml","identifier":"naturalproductmech:mibig-a2b74a45ae","label":"8,9-epibotrydial","standard_inchi_key":"SJFIYVCSGNWVPJ-PQVRDHEWSA-N"},{"path":"data/natural_products/terpenoids/botrydial.yaml","identifier":"CHEBI:3159","label":"botrydial","standard_inchi_key":"SJFIYVCSGNWVPJ-GKKOWQTJSA-N"},{"path":"data/natural_products/terpenoids/botrydienal.yaml","identifier":"naturalproductmech:mibig-a1c6942987","label":"Botrydienal","standard_inchi_key":"CFAMAVBUWMXYLX-MEBBXXQBSA-N"},{"path":"data/natural_products/terpenoids/botryenalol.yaml","identifier":"naturalproductmech:mibig-d567f1a1cd","label":"Botryenalol","standard_inchi_key":"DSVSTMJOGQEZJX-BYLNDYCFSA-N"},{"path":"data/natural_products/terpenoids/botryendial.yaml","identifier":"naturalproductmech:mibig-79ce4aca52","label":"Botryendial","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N"},{"path":"data/natural_products/terpenoids/dehydrobotrydienol.yaml","identifier":"naturalproductmech:mibig-247120aa23","label":"Dehydrobotrydienol","standard_inchi_key":"UQQKKLVKVVJDEX-OAHLLOKOSA-N"},{"path":"data/natural_products/terpenoids/dihydrobotrydial.yaml","identifier":"naturalproductmech:mibig-b5ca742a5e","label":"Dihydrobotrydial","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N"},{"path":"data/natural_products/terpenoids/norbotrydialone-acetate.yaml","identifier":"naturalproductmech:mibig-9b040d7e03","label":"Norbotrydialone acetate","standard_inchi_key":"OMZUEHMZFLBHNI-PCKWUFTNSA-N"},{"path":"data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml","identifier":"naturalproductmech:mibig-2cef442430","label":"Secobotrydiene-3,10,15-triol","standard_inchi_key":"GYABYKLKVQPSPD-NVWZYQMFSA-N"},{"path":"data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml","identifier":"naturalproductmech:mibig-f478b3a4f7","label":"Secobotrydiene-3,4,10,15-tetraol","standard_inchi_key":"GNMCOKDZWITFBO-MGNGBMTDSA-N"},{"path":"data/natural_products/terpenoids/secobotrytriendiol.yaml","identifier":"naturalproductmech:mibig-ff72b656ae","label":"Secobotrytriendiol","standard_inchi_key":"BHNACKMCMDASDB-UJNBGNEJSA-N"},{"path":"data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml","identifier":"naturalproductmech:mibig-1c14174a30","label":"Secobotrytriene-10,12,15-triol","standard_inchi_key":"WLPOYIWCPMYYGM-KGRKPJGKSA-N"}]. Shared BGC alone does not transfer properties. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-225/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-225/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-225/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-225/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-225/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- FullQC and complete OAK were unavailable; five successful local gates do not establish scientific completeness.
- No external retrieval or live identifier, taxonomy, protein or publication query was performed. These assessments use the original saved owner-form computations; no additional molecular parses occurred during fragment authoring.
- The original chemistry stream contains two omitted-undefined-stereo warnings. They are global and are not attributed to specific owners from timing or inference.
- Retained source grades, database citations, cached taxonomy and versioned predictions keep their own scopes. Representation agreement does not prove natural identity, publication independence or complete natural stereochemistry.
- No scientific source record or curation history was edited. Canonical persistence and campaign operations remain ROOT-owned.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- This selected owner has no four mechanism roots or components. No selected maintained reader applies; positive unselected annotations remain context only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T154045Z-4-acetoxytetrahydrobotryslactone
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: 4β-Acetoxytetrahydrobotryslactone'
started_at: '2026-11-03T15:06:55.226329Z'
finished_at: '2026-11-03T15:40:45.030452Z'
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
summary: 'Qualified partial review: the lactone/acetate topology and exact paired
  forms agree, while strain-level BGC evidence remains distinct from the single species
  occurrence. The twenty congeners and Botrydial graph are context only.'
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
    role: target
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
  selection: Campaign path order 2248; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-0bd6ab53bc
targets:
- target_id: naturalproductmech:mibig-0bd6ab53bc
  path: data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml
  label: 4β-Acetoxytetrahydrobotryslactone
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
  - naturalproductmech:mibig-0bd6ab53bc
  command: just validate-strict data/natural_products/terpenoids/17-deoxyaphidicolin.yaml
    data/natural_products/terpenoids/2-cis-abscisic-acid.yaml data/natural_products/terpenoids/2-hydroxysorangiadenosine.yaml
    data/natural_products/terpenoids/21-h-hopane-3beta-22-diol.yaml data/natural_products/terpenoids/2s-3r-9r-pristinol.yaml
    data/natural_products/terpenoids/3-decalonectrin.yaml data/natural_products/terpenoids/3-deoxyaphidicolin.yaml
    data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml data/natural_products/terpenoids/4-acetylnivalenol.yaml
    data/natural_products/terpenoids/5-9-10-labda-8-20-13-dien-15-yl-diphosphate.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-225/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-0bd6ab53bc
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-225/validate-all-001.tsv
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
  - naturalproductmech:mibig-0bd6ab53bc
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
  - naturalproductmech:mibig-0bd6ab53bc
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
  - naturalproductmech:mibig-0bd6ab53bc
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-225/review-queue-001.tsv
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
  - naturalproductmech:mibig-0bd6ab53bc
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-0bd6ab53bc
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-0bd6ab53bc
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2248-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml
  locator: lines 1–92
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Whole current plaintext owner and all 2 history events. Literal identifier
    naturalproductmech:mibig-0bd6ab53bc, label 4β-Acetoxytetrahydrobotryslactone and
    full key RVXLTRZIAMMATE-JMTSMVSISA-N. Historical events remain retained claims,
    not fresh scientific verification.
  snapshot_sha256: c4c9d1c900ad07aac687e0b9ec51c5ba589e9e065c4f0116446a248ba366112e
- evidence_id: support-2248-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json
  locator: /records/7/owner_document; /records/7/owner_pin
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Exact captured complete owner, including structure, provenance, occurrences
    or assays where written, computed classification, grounding and history.
  snapshot_sha256: 0e9d3e869f9ce737ea339dd4952cbb014b2b826c4f2822ee7db6b4f5a1a28533
- evidence_id: support-2248-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted selected source context, including all nine retained
    query frames and full payloads, 57 inputs and 20 direct companion paths. This
    is a local inventory scope.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch225/intakes/2248-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Original canonical inspection of exact target and source ownership with
    current input snapshots; inspection is not a scientific verdict.
  snapshot_sha256: 10f2d0cbc5b47ab1aab39c2ccc70525e6e9fcbefd6a0dcf382953124ea0376ed
- evidence_id: support-2248-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch225/root-input-plan-acceptance-001.json
  locator: /accepted; /status; /plan; /inventory; /source_notes; /source_placements;
    /unique_source_paths
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: ROOT accepts the actual saved plan with 412 input placements and 77 unique
    paths.
  snapshot_sha256: 8b553f64807b674d1731148a3995b48ceca2b42aa4cd763c5f306ef84992a96d
- evidence_id: support-2248-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch225/root-intake-ready-001.json
  locator: /accepted; /status; /intake_summary; /intakes_execution; /source_placements;
    /unique_source_paths; /mechanism_owner_orders
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: ROOT accepts all ten original canonical intakes and exact 412/77 snapshots;
    only 2245 is a selected mechanism owner.
  snapshot_sha256: 6f3cca33d9d1304a058b16e62e10dd34951397c511d1e28efd688778eb0a591f
- evidence_id: support-2248-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch225/root-local-diagnostics-acceptance-001.json
  locator: /status; /DATA; /execution; /native_gate_acceptance; /successful_forms;
    /comparison_flags_true; /global_stderr_warnings; /full_QC_and_OAK
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: ROOT accepts the original twenty stored-form parses and 100 true paired
    comparisons with current inputs. The two stderr warnings remain global and unassigned.
    FullQC and complete OAK are unavailable; the separate native gate receipt is linked.
  snapshot_sha256: 9bc1a44f264ea5a8261064ea20b2d3ced43e1608a6bebdeb0b235c4476564e9f
- evidence_id: support-2248-native-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch225/root-native-five-gates-acceptance-001.json
  locator: /accepted; /status; /results; /full_QC_available; /complete_OAK_authority_available;
    /all_native_gates_passed
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Five local commands passed; FullQC and complete OAK remain unavailable,
    so all_native_gates_passed is false. This mechanical acceptance does not establish
    scientific completeness.
  snapshot_sha256: e5b971aac7d6c7f0502248a9f3b9a6554500b2b131c408cdca84f95fd4229b0f
- evidence_id: support-2248-chemistry-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-execution-001.json
  locator: /started_at; /finished_at; /exit_code; /DATA; /stdout; /stderr; /external_requests;
    /retries
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Original saved chemistry execution exited zero. The original stdout and
    92-byte stderr stream are pinned separately; no retry or external request is recorded.
  snapshot_sha256: 78ad622a43d40672797351398f42ca4e4d960b9d268915937dd62a54571c00fa
- evidence_id: support-2248-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/smiles/computed; /records/7/inchi/computed;
    /records/7/comparisons; /records/7/atom_correspondence; /records/7/smiles/status;
    /records/7/inchi/status
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Both saved forms parsed; all ten paired comparison flags are true, including
    full key, formula and both canonical SMILES comparisons. A complete chirality-aware
    atom match is stored, with full_graph_identity_established:false. Literal stereo_complete:true.
    Both saved forms are neutral C20H30O6 with 26 atoms and 28 bonds. Six tetrahedral
    centers are specified and no unspecified potential entry is reported; literal
    stereo_complete:true is retained. SMILES centers C1 R, C3 S, C4 S, C7 S, C9 R
    and C14 S describe this stored form. Ring C5=C6 is not an unassigned potential
    double bond in the saved table. No natural stereochemical assignment is newly
    established.
  snapshot_sha256: 2c67ccbf2df2c8fee5fd0761d179566903ed7db15c60650d2cff295cbac068a7
- evidence_id: support-2248-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed; /records/7/inchi/computed
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: The saved graph contains a five-membered lactone C10(=O11)–O12–C7 in ring
    [7,8,9,10,12] and a separate acetate C23(=O24)–O22–C3 with methyl C25. Hydroxyl
    O13 is attached to C9 and O21 to CH2 C20. Three perceived rings and ring alkene
    C5=C6 remain explicit. The C5O candidate list is empty; no sugar residue is assigned.
    These graph facts support a bounded lactone/acetate interpretation without proving
    natural-product naming or a biosynthetic pathway.
  snapshot_sha256: 2c67ccbf2df2c8fee5fd0761d179566903ed7db15c60650d2cff295cbac068a7
- evidence_id: support-2248-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–173
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: The maintained structure_fields calculation uses FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False)
    and sets stereo_complete by absence of ? atom-center labels. It does not separately
    test potential double-bond geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2248-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 982–1019
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: The maintained seeder retains lead structure/key, copies stereo_complete,
    stores the matched ChEBI definition, and records versioned NPClassifier output
    separately. Code reading only; no new extraction or seeding.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2248-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 392–425
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: The stereo_complete description addresses undefined stereocentres; ComputedClassification
    explicitly denotes a named/versioned prediction, never a source assertion or record-admission
    reason.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2248-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: lines 35–57
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: The local review profile separates exact structure, provenance, evidence
    tiers and computed filing classification. Seeded content belongs to maintained
    inventories/extractors/seeder; reserved decisions.tsv is not consumed. Saving
    a review does not promote native status or append history.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2248-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-source-scope-notes-001.json
  locator: /reading; /curation; /cautions; /totals
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: The source notes attribute the disjoint complete reading of 36 current
    contexts, 324 query frames and 272 positive placements, 26 cached stanzas and
    bounded implemented-curation scan. Source assertions, companion claims, model
    predictions and cached taxonomy remain separately scoped.
  snapshot_sha256: 08f2dd0c94feafa1b7201db4b7fff3d4218aade05b41a8b71c566de4f60ed0ed
- evidence_id: support-2248-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/source_taxa; /records/7/source_scope_inventory/forward_taxon_merge_matches;
    /records/7/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Selected source taxa ["NCBITaxon:332648", "NCBITaxon:40559"]. Forward-merge
    matches []; non-organism matches []. No live taxonomy query.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-mechanism-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/declared_mechanism_roots_literal; /records/7/component_paths;
    /records/7/literal_mechanism_inventory; /records/7/proposed_companion_paths
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: The selected owner has no pathway, graph, component-reference or molecular-target
    root. Positive unselected context does not create selected reader applicability
    or verified biological absence.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Saved query frame: predicate="exact complete standard_inchi_key equality";
    query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=1. Empty results
    are limited to this saved predicate and inventory.'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 747–747
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Complete retained physical TSV payload: {"mibig_accession":"BGC0000631","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"4β-Acetoxytetrahydrobotryslactone","compound_index":"21","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1[C@@H]3C[C@H](C(=O)O3)O)[C@@](CC2(C)C)(C)CO)OC(=O)C","standard_inchi":"InChI=1S/C20H30O6/c1-10-6-14(25-11(2)22)16-17(20(5,9-21)8-19(16,3)4)15(10)13-7-12(23)18(24)26-13/h10,12-14,16,21,23H,6-9H2,1-5H3/t10-,12-,13+,14+,16-,20-/m1/s1","standard_inchi_key":"RVXLTRZIAMMATE-JMTSMVSISA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA002526","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis
    cinerea B05.10","bgc_classes":"terpene","bgc_subclasses":"Sesquiterpene","genome_accession":"CP009816.1","locus_from":"2216500","locus_to":"2246000","locus_evidence_methods":"Knock-out
    studies","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"DOI:10.1021/np020107v","reference_basis":"COMPOUND_EVIDENCE"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2248-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Saved query frame: predicate="exact complete standard_inchi_key equality";
    query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=0. Empty results
    are limited to this saved predicate and inventory.'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Saved query frame: predicate="exact complete standard_inchi_key equality";
    query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=1. Empty results
    are limited to this saved predicate and inventory.'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 8247–8247
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Complete retained physical TSV payload: {"standard_inchi_key":"RVXLTRZIAMMATE-JMTSMVSISA-N","organism_name":"Botrytis
    cinerea","taxon_id":"NCBITaxon:40559","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1021/NP020107V","structure_wikidata":"http://www.wikidata.org/entity/Q75067586"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2248-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Saved query frame: predicate="exact complete standard_inchi_key equality";
    query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=0. Empty results
    are limited to this saved predicate and inventory.'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Saved query frame: predicate="exact complete standard_inchi_key equality";
    query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=1. Empty results
    are limited to this saved predicate and inventory.'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2184–2184
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Complete retained physical TSV payload: {"standard_inchi_key":"RVXLTRZIAMMATE-JMTSMVSISA-N","smiles":"C[C@@H]1C[C@@H]([C@@H]2C(=C1[C@@H]3C[C@H](C(=O)O3)O)[C@@](CC2(C)C)(C)CO)OC(=O)C","pathway_results":"Terpenoids","superclass_results":"Sesquiterpenoids","class_results":"Botryane
    sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2248-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Saved query frame: predicate="exact complete standard_inchi_key equality";
    query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=0. Empty results
    are limited to this saved predicate and inventory.'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Saved query frame: predicate="exact complete standard_inchi_key equality";
    query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=0. Empty results
    are limited to this saved predicate and inventory.'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Saved query frame: predicate="exact complete standard_inchi_key equality";
    query="RVXLTRZIAMMATE-JMTSMVSISA-N"; complete positive match count=0. Empty results
    are limited to this saved predicate and inventory.'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Saved query frame: predicate="exact chebi_id from exact full-key structure
    rows"; query=[]; complete positive match count=0. Empty results are limited to
    this saved predicate and inventory.'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-cache-40559
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: physical lines 18031–18038
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Whole cached stanza, including literal synonym scope; not live taxonomy:
    [Term]

    id: NCBITaxon:40559

    name: Botrytis cinerea

    synonym: "Botryotinia fuckeliana" EXACT []

    synonym: "Botrytis cinerea Pers., 1801" EXACT []

    synonym: "Peziza fuckeliana" EXACT []

    synonym: "Sclerotinia fuckeliana" EXACT []


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2248-cache-332648
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: physical lines 83758–83762
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Whole cached stanza, including literal synonym scope; not live taxonomy:
    [Term]

    id: NCBITaxon:332648

    name: Botrytis cinerea B05.10

    synonym: "Botryotinia fuckeliana B05.10" EXACT []


    '
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2248-companion-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/0
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for 1-epibotrydial (naturalproductmech:mibig-acc775e1b7), full key SJFIYVCSGNWVPJ-SDLFRHKASA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-1
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/1
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for 10-dehydroxy dihydrobotrydialone (naturalproductmech:mibig-1e06238f05), full
    key MBHVNAKPTPFWNG-MYFMSEKESA-N. It is direct context, not a selected assay, mechanism
    or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-2
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/2
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for 10-epi-dihydrobotrydial (naturalproductmech:mibig-7950af79c1), full key QUGYVDURDBEQRB-VZJVBFQISA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-3
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/3
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for 10-Oxo-dihydrobotrydial (naturalproductmech:mibig-e2d62600f5), full key MFOUCDNLAFNKML-SVLWDWOGSA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-4
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/4
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for 10-Oxodehydrodihydrobotrydial (naturalproductmech:mibig-7b45e48275), full
    key CAMCSBCRRUTMEK-OAHLLOKOSA-N. It is direct context, not a selected assay, mechanism
    or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-5
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/5
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for 10-Oxodihydrobotry-1(9),4(5)-diendial (naturalproductmech:mibig-8b4cd14741),
    full key PCEVLQFNPPWJEB-RFAUZJTJSA-N. It is direct context, not a selected assay,
    mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-6
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/6
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for 11-Hydroxydehydrobotrydienol (naturalproductmech:mibig-bbb6f44666), full key
    JUCMRFKOKIZVPS-OAHLLOKOSA-N. It is direct context, not a selected assay, mechanism
    or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-7
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/7
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for 12-hydroxydehydrobotrydienol (naturalproductmech:mibig-10fda622fe), full key
    YPJRKTIWVUVMDI-LSDHHAIUSA-N. It is direct context, not a selected assay, mechanism
    or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-8
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/9
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for 8,9-epibotrydial (naturalproductmech:mibig-a2b74a45ae), full key SJFIYVCSGNWVPJ-PQVRDHEWSA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-9
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/12
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for botrydial (CHEBI:3159), full key SJFIYVCSGNWVPJ-GKKOWQTJSA-N. It is direct
    context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-10
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/13
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for Botrydienal (naturalproductmech:mibig-a1c6942987), full key CFAMAVBUWMXYLX-MEBBXXQBSA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-11
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/14
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for Botryenalol (naturalproductmech:mibig-d567f1a1cd), full key DSVSTMJOGQEZJX-BYLNDYCFSA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-12
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/15
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for Botryendial (naturalproductmech:mibig-79ce4aca52), full key QWZKEROSOALLJP-BYLNDYCFSA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-13
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/17
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for Dehydrobotrydienol (naturalproductmech:mibig-247120aa23), full key UQQKKLVKVVJDEX-OAHLLOKOSA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-14
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/18
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for Dihydrobotrydial (naturalproductmech:mibig-b5ca742a5e), full key QUGYVDURDBEQRB-CJNHKLDISA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-15
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/21
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for Norbotrydialone acetate (naturalproductmech:mibig-9b040d7e03), full key OMZUEHMZFLBHNI-PCKWUFTNSA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-16
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/22
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for Secobotrydiene-3,10,15-triol (naturalproductmech:mibig-2cef442430), full key
    GYABYKLKVQPSPD-NVWZYQMFSA-N. It is direct context, not a selected assay, mechanism
    or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-17
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/23
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for Secobotrydiene-3,4,10,15-tetraol (naturalproductmech:mibig-f478b3a4f7), full
    key GNMCOKDZWITFBO-MGNGBMTDSA-N. It is direct context, not a selected assay, mechanism
    or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-18
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/24
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for Secobotrytriendiol (naturalproductmech:mibig-ff72b656ae), full key BHNACKMCMDASDB-UJNBGNEJSA-N.
    It is direct context, not a selected assay, mechanism or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companion-19
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /raw_unselected_companions/25
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: Complete admitted companion raw text/history and retained source scope
    for Secobotrytriene-10,12,15-triol (naturalproductmech:mibig-1c14174a30), full
    key WLPOYIWCPMYYGM-KGRKPJGKSA-N. It is direct context, not a selected assay, mechanism
    or stereochemistry transfer.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: support-2248-companions
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/7/proposed_companion_paths; /records/7/direct_companion_predicates;
    /raw_unselected_companions
  accessed_at: '2026-11-03T15:30:31.434695Z'
  support: supports
  summary: 'Exact direct context under the admitted one-hop predicates. Distinct owner
    identities: [{"path":"data/natural_products/terpenoids/1-epibotrydial.yaml","identifier":"naturalproductmech:mibig-acc775e1b7","label":"1-epibotrydial","standard_inchi_key":"SJFIYVCSGNWVPJ-SDLFRHKASA-N"},{"path":"data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml","identifier":"naturalproductmech:mibig-1e06238f05","label":"10-dehydroxy
    dihydrobotrydialone","standard_inchi_key":"MBHVNAKPTPFWNG-MYFMSEKESA-N"},{"path":"data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml","identifier":"naturalproductmech:mibig-7950af79c1","label":"10-epi-dihydrobotrydial","standard_inchi_key":"QUGYVDURDBEQRB-VZJVBFQISA-N"},{"path":"data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml","identifier":"naturalproductmech:mibig-e2d62600f5","label":"10-Oxo-dihydrobotrydial","standard_inchi_key":"MFOUCDNLAFNKML-SVLWDWOGSA-N"},{"path":"data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml","identifier":"naturalproductmech:mibig-7b45e48275","label":"10-Oxodehydrodihydrobotrydial","standard_inchi_key":"CAMCSBCRRUTMEK-OAHLLOKOSA-N"},{"path":"data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml","identifier":"naturalproductmech:mibig-8b4cd14741","label":"10-Oxodihydrobotry-1(9),4(5)-diendial","standard_inchi_key":"PCEVLQFNPPWJEB-RFAUZJTJSA-N"},{"path":"data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml","identifier":"naturalproductmech:mibig-bbb6f44666","label":"11-Hydroxydehydrobotrydienol","standard_inchi_key":"JUCMRFKOKIZVPS-OAHLLOKOSA-N"},{"path":"data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml","identifier":"naturalproductmech:mibig-10fda622fe","label":"12-hydroxydehydrobotrydienol","standard_inchi_key":"YPJRKTIWVUVMDI-LSDHHAIUSA-N"},{"path":"data/natural_products/terpenoids/8-9-epibotrydial.yaml","identifier":"naturalproductmech:mibig-a2b74a45ae","label":"8,9-epibotrydial","standard_inchi_key":"SJFIYVCSGNWVPJ-PQVRDHEWSA-N"},{"path":"data/natural_products/terpenoids/botrydial.yaml","identifier":"CHEBI:3159","label":"botrydial","standard_inchi_key":"SJFIYVCSGNWVPJ-GKKOWQTJSA-N"},{"path":"data/natural_products/terpenoids/botrydienal.yaml","identifier":"naturalproductmech:mibig-a1c6942987","label":"Botrydienal","standard_inchi_key":"CFAMAVBUWMXYLX-MEBBXXQBSA-N"},{"path":"data/natural_products/terpenoids/botryenalol.yaml","identifier":"naturalproductmech:mibig-d567f1a1cd","label":"Botryenalol","standard_inchi_key":"DSVSTMJOGQEZJX-BYLNDYCFSA-N"},{"path":"data/natural_products/terpenoids/botryendial.yaml","identifier":"naturalproductmech:mibig-79ce4aca52","label":"Botryendial","standard_inchi_key":"QWZKEROSOALLJP-BYLNDYCFSA-N"},{"path":"data/natural_products/terpenoids/dehydrobotrydienol.yaml","identifier":"naturalproductmech:mibig-247120aa23","label":"Dehydrobotrydienol","standard_inchi_key":"UQQKKLVKVVJDEX-OAHLLOKOSA-N"},{"path":"data/natural_products/terpenoids/dihydrobotrydial.yaml","identifier":"naturalproductmech:mibig-b5ca742a5e","label":"Dihydrobotrydial","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N"},{"path":"data/natural_products/terpenoids/norbotrydialone-acetate.yaml","identifier":"naturalproductmech:mibig-9b040d7e03","label":"Norbotrydialone
    acetate","standard_inchi_key":"OMZUEHMZFLBHNI-PCKWUFTNSA-N"},{"path":"data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml","identifier":"naturalproductmech:mibig-2cef442430","label":"Secobotrydiene-3,10,15-triol","standard_inchi_key":"GYABYKLKVQPSPD-NVWZYQMFSA-N"},{"path":"data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml","identifier":"naturalproductmech:mibig-f478b3a4f7","label":"Secobotrydiene-3,4,10,15-tetraol","standard_inchi_key":"GNMCOKDZWITFBO-MGNGBMTDSA-N"},{"path":"data/natural_products/terpenoids/secobotrytriendiol.yaml","identifier":"naturalproductmech:mibig-ff72b656ae","label":"Secobotrytriendiol","standard_inchi_key":"BHNACKMCMDASDB-UJNBGNEJSA-N"},{"path":"data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml","identifier":"naturalproductmech:mibig-1c14174a30","label":"Secobotrytriene-10,12,15-triol","standard_inchi_key":"WLPOYIWCPMYYGM-KGRKPJGKSA-N"}].
    Shared BGC alone does not transfer properties.'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-225/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json
  accessed_at: '2026-11-03T15:08:40.038173Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: b1de93f00ae41f97306f80a1bc1ad1e662083a600933708905899bcf66fab1b9
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-225/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json
  accessed_at: '2026-11-03T15:09:06.064639Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: c73c0e1fb5f397d9d622cc2237a0d705daa1732bee63b4df6b1b16ea59e9970d
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-225/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json
  accessed_at: '2026-11-03T15:09:26.342067Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-225/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json
  accessed_at: '2026-11-03T15:10:01.232424Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-225/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json
  accessed_at: '2026-11-03T15:10:12.957939Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 77d40d08e42713a235950bd02ad7525c549543775e160f34f23626b8ef01a308
assessments:
- assessment_id: support-2248-A1
  area: identity
  topic: Exact structure concept and grounding
  outcome: supported
  summary: The MINTED owner naturalproductmech:mibig-0bd6ab53bc retains label 4β-Acetoxytetrahydrobotryslactone
    and full key RVXLTRZIAMMATE-JMTSMVSISA-N from BGC0000631 version 5, source compound_index=21.
    The exact full-key ChEBI predicate is empty. Twenty distinct direct congeners
    contextualize this source cluster without resolving nomenclature or supplying
    a different structure.
  target_ids:
  - naturalproductmech:mibig-0bd6ab53bc
  evidence_ids:
  - support-2248-owner
  - support-2248-capture
  - support-2248-source-plan
  - support-2248-companions
  - support-2248-row-mibig_compounds-0
  - support-2248-companion-0
  - support-2248-companion-1
  - support-2248-companion-2
  - support-2248-companion-3
  - support-2248-companion-4
  - support-2248-companion-5
  - support-2248-companion-6
  - support-2248-companion-7
  - support-2248-companion-8
  - support-2248-companion-9
  - support-2248-companion-10
  - support-2248-companion-11
  - support-2248-companion-12
  - support-2248-companion-13
  - support-2248-companion-14
  - support-2248-companion-15
  - support-2248-companion-16
  - support-2248-companion-17
  - support-2248-companion-18
  - support-2248-companion-19
  dimensions:
  - name: standard_inchi_key
    value: RVXLTRZIAMMATE-JMTSMVSISA-N
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-owner
    - support-2248-capture
    - support-2248-source-plan
    - support-2248-companions
    - support-2248-row-mibig_compounds-0
    - support-2248-companion-0
    - support-2248-companion-1
    - support-2248-companion-2
    - support-2248-companion-3
    - support-2248-companion-4
    - support-2248-companion-5
    - support-2248-companion-6
    - support-2248-companion-7
    - support-2248-companion-8
    - support-2248-companion-9
    - support-2248-companion-10
    - support-2248-companion-11
    - support-2248-companion-12
    - support-2248-companion-13
    - support-2248-companion-14
    - support-2248-companion-15
    - support-2248-companion-16
    - support-2248-companion-17
    - support-2248-companion-18
    - support-2248-companion-19
  - name: grounding_scope
    value: The MINTED owner naturalproductmech:mibig-0bd6ab53bc retains label 4β-Acetoxytetrahydrobotryslactone
      and full key RVXLTRZIAMMATE-JMTSMVSISA-N from BGC0000631 version 5, source compound_index=21.
      The exact full-key ChEBI predicate is empty. Twenty distinct direct congeners
      contextualize this source cluster without resolving nomenclature or supplying
      a different structure.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-owner
    - support-2248-capture
    - support-2248-source-plan
    - support-2248-companions
    - support-2248-row-mibig_compounds-0
    - support-2248-companion-0
    - support-2248-companion-1
    - support-2248-companion-2
    - support-2248-companion-3
    - support-2248-companion-4
    - support-2248-companion-5
    - support-2248-companion-6
    - support-2248-companion-7
    - support-2248-companion-8
    - support-2248-companion-9
    - support-2248-companion-10
    - support-2248-companion-11
    - support-2248-companion-12
    - support-2248-companion-13
    - support-2248-companion-14
    - support-2248-companion-15
    - support-2248-companion-16
    - support-2248-companion-17
    - support-2248-companion-18
    - support-2248-companion-19
- assessment_id: support-2248-A2
  area: representation
  topic: Stored representations and stereo resolution
  outcome: supported
  summary: Both saved forms are neutral C20H30O6 with 26 atoms and 28 bonds. Six tetrahedral
    centers are specified and no unspecified potential entry is reported; literal
    stereo_complete:true is retained. SMILES centers C1 R, C3 S, C4 S, C7 S, C9 R
    and C14 S describe this stored form. Ring C5=C6 is not an unassigned potential
    double bond in the saved table. No natural stereochemical assignment is newly
    established. All ten saved paired comparisons pass; complete stored atom correspondence
    is explicitly limited to a chirality-aware match and does not establish independent
    full-graph or natural identity.
  target_ids:
  - naturalproductmech:mibig-0bd6ab53bc
  evidence_ids:
  - support-2248-capture
  - support-2248-chemistry
  - support-2248-chemistry-execution
  - support-2248-stereo-method
  - support-2248-structure-schema
  dimensions:
  - name: stereochemical_resolution
    value: Both saved forms are neutral C20H30O6 with 26 atoms and 28 bonds. Six tetrahedral
      centers are specified and no unspecified potential entry is reported; literal
      stereo_complete:true is retained. SMILES centers C1 R, C3 S, C4 S, C7 S, C9
      R and C14 S describe this stored form. Ring C5=C6 is not an unassigned potential
      double bond in the saved table. No natural stereochemical assignment is newly
      established.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-capture
    - support-2248-chemistry
    - support-2248-chemistry-execution
    - support-2248-stereo-method
    - support-2248-structure-schema
  - name: representation_correspondence
    value: All ten saved paired comparisons pass; complete stored atom correspondence
      is explicitly limited to a chirality-aware match and does not establish independent
      full-graph or natural identity.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-capture
    - support-2248-chemistry
    - support-2248-chemistry-execution
    - support-2248-stereo-method
    - support-2248-structure-schema
- assessment_id: support-2248-A3
  area: provenance
  topic: Producer, locus and taxonomy scope
  outcome: supported
  summary: Botrytis cinerea B05.10 NCBITaxon:332648 is graded BGC_CHARACTERIZED. BGC0000631
    version 5, active/questionable/complete, spans CP009816.1:2216500–2246000 and
    retains knockout evidence with CLUSTER_DEMONSTRATED. A separate LOTUS occurrence
    uses Botrytis cinerea species NCBITaxon:40559. Cached Botryotinia fuckeliana synonyms
    preserve the species and B05.10 strain scopes separately; they do not collapse
    occurrence into a strain-level producer claim.
  target_ids:
  - naturalproductmech:mibig-0bd6ab53bc
  evidence_ids:
  - support-2248-capture
  - support-2248-taxonomy-routes
  - support-2248-source-notes
  - support-2248-row-mibig_compounds-0
  - support-2248-row-lotus_occurrences-0
  - support-2248-cache-40559
  - support-2248-cache-332648
  dimensions:
  - name: taxon_and_strain_scope
    value: Botrytis cinerea B05.10 NCBITaxon:332648 is graded BGC_CHARACTERIZED. BGC0000631
      version 5, active/questionable/complete, spans CP009816.1:2216500–2246000 and
      retains knockout evidence with CLUSTER_DEMONSTRATED. A separate LOTUS occurrence
      uses Botrytis cinerea species NCBITaxon:40559. Cached Botryotinia fuckeliana
      synonyms preserve the species and B05.10 strain scopes separately; they do not
      collapse occurrence into a strain-level producer claim.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-capture
    - support-2248-taxonomy-routes
    - support-2248-source-notes
    - support-2248-row-mibig_compounds-0
    - support-2248-row-lotus_occurrences-0
    - support-2248-cache-40559
    - support-2248-cache-332648
  - name: producer_evidence_tier
    value: BGC_CHARACTERIZED for Botrytis cinerea B05.10, taxon 332648; distinct species
      occurrence at 40559.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-capture
    - support-2248-taxonomy-routes
    - support-2248-source-notes
    - support-2248-row-mibig_compounds-0
    - support-2248-row-lotus_occurrences-0
    - support-2248-cache-40559
    - support-2248-cache-332648
  - name: locus_evidence_tier
    value: BGC0000631 v5, CP009816.1:2216500–2246000, CLUSTER_DEMONSTRATED from retained
      knockout evidence.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-capture
    - support-2248-taxonomy-routes
    - support-2248-source-notes
    - support-2248-row-mibig_compounds-0
    - support-2248-row-lotus_occurrences-0
    - support-2248-cache-40559
    - support-2248-cache-332648
- assessment_id: support-2248-A4
  area: evidence
  topic: Citation placement and historical verification scope
  outcome: supported
  summary: DOI:10.1021/np020107v is a COMPOUND_EVIDENCE reference in MIBiG. The single
    LOTUS DOI:10.1021/NP020107V differs only in case and does not establish an independent
    experiment. Generated evidence remains DATABASE_ASSERTION; no original article
    or sequence was inspected.
  target_ids:
  - naturalproductmech:mibig-0bd6ab53bc
  evidence_ids:
  - support-2248-capture
  - support-2248-source-notes
  - support-2248-row-mibig_compounds-0
  - support-2248-row-lotus_occurrences-0
  dimensions:
  - name: citation_scope
    value: DOI:10.1021/np020107v is a COMPOUND_EVIDENCE reference in MIBiG. The single
      LOTUS DOI:10.1021/NP020107V differs only in case and does not establish an independent
      experiment. Generated evidence remains DATABASE_ASSERTION; no original article
      or sequence was inspected.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-capture
    - support-2248-source-notes
    - support-2248-row-mibig_compounds-0
    - support-2248-row-lotus_occurrences-0
- assessment_id: support-2248-A5
  area: scope
  topic: Occurrence, assay and companion boundaries
  outcome: supported
  summary: One retained LOTUS species occurrence is written. The exact selected PubChem,
    BindingDB, AntibioticMech, CyanoMetDB and ChEBI-origin queries are empty. Twenty
    direct BGC0000631 congeners have distinct full keys and remain context. In particular,
    unselected Botrydial's inline causal graph is not this compound's pathway, protein,
    producer or assay evidence; no selected maintained reader applies.
  target_ids:
  - naturalproductmech:mibig-0bd6ab53bc
  evidence_ids:
  - support-2248-capture
  - support-2248-source-plan
  - support-2248-mechanism-scope
  - support-2248-companions
  - support-2248-source-notes
  - support-2248-query-mibig_compounds
  - support-2248-query-chebi_structures
  - support-2248-query-lotus_occurrences
  - support-2248-query-cyanometdb_occurrences
  - support-2248-query-npclassifier
  - support-2248-query-pubchem_bioassay
  - support-2248-query-bindingdb_targets
  - support-2248-query-antibioticmech_inchikeys
  - support-2248-query-chebi_origins
  - support-2248-row-lotus_occurrences-0
  - support-2248-companion-0
  - support-2248-companion-1
  - support-2248-companion-2
  - support-2248-companion-3
  - support-2248-companion-4
  - support-2248-companion-5
  - support-2248-companion-6
  - support-2248-companion-7
  - support-2248-companion-8
  - support-2248-companion-9
  - support-2248-companion-10
  - support-2248-companion-11
  - support-2248-companion-12
  - support-2248-companion-13
  - support-2248-companion-14
  - support-2248-companion-15
  - support-2248-companion-16
  - support-2248-companion-17
  - support-2248-companion-18
  - support-2248-companion-19
  dimensions:
  - name: occurrence_scope
    value: One retained LOTUS species occurrence is written. The exact selected PubChem,
      BindingDB, AntibioticMech, CyanoMetDB and ChEBI-origin queries are empty. Twenty
      direct BGC0000631 congeners have distinct full keys and remain context. In particular,
      unselected Botrydial's inline causal graph is not this compound's pathway, protein,
      producer or assay evidence; no selected maintained reader applies.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-capture
    - support-2248-source-plan
    - support-2248-mechanism-scope
    - support-2248-companions
    - support-2248-source-notes
    - support-2248-query-mibig_compounds
    - support-2248-query-chebi_structures
    - support-2248-query-lotus_occurrences
    - support-2248-query-cyanometdb_occurrences
    - support-2248-query-npclassifier
    - support-2248-query-pubchem_bioassay
    - support-2248-query-bindingdb_targets
    - support-2248-query-antibioticmech_inchikeys
    - support-2248-query-chebi_origins
    - support-2248-row-lotus_occurrences-0
    - support-2248-companion-0
    - support-2248-companion-1
    - support-2248-companion-2
    - support-2248-companion-3
    - support-2248-companion-4
    - support-2248-companion-5
    - support-2248-companion-6
    - support-2248-companion-7
    - support-2248-companion-8
    - support-2248-companion-9
    - support-2248-companion-10
    - support-2248-companion-11
    - support-2248-companion-12
    - support-2248-companion-13
    - support-2248-companion-14
    - support-2248-companion-15
    - support-2248-companion-16
    - support-2248-companion-17
    - support-2248-companion-18
    - support-2248-companion-19
  - name: assay_scope
    value: No selected assay/target matches in the admitted local predicates; no activity
      absence or transfer from twenty congeners is asserted.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-capture
    - support-2248-source-plan
    - support-2248-mechanism-scope
    - support-2248-companions
    - support-2248-source-notes
    - support-2248-query-mibig_compounds
    - support-2248-query-chebi_structures
    - support-2248-query-lotus_occurrences
    - support-2248-query-cyanometdb_occurrences
    - support-2248-query-npclassifier
    - support-2248-query-pubchem_bioassay
    - support-2248-query-bindingdb_targets
    - support-2248-query-antibioticmech_inchikeys
    - support-2248-query-chebi_origins
    - support-2248-row-lotus_occurrences-0
    - support-2248-companion-0
    - support-2248-companion-1
    - support-2248-companion-2
    - support-2248-companion-3
    - support-2248-companion-4
    - support-2248-companion-5
    - support-2248-companion-6
    - support-2248-companion-7
    - support-2248-companion-8
    - support-2248-companion-9
    - support-2248-companion-10
    - support-2248-companion-11
    - support-2248-companion-12
    - support-2248-companion-13
    - support-2248-companion-14
    - support-2248-companion-15
    - support-2248-companion-16
    - support-2248-companion-17
    - support-2248-companion-18
    - support-2248-companion-19
- assessment_id: support-2248-A6
  area: other
  topic: Computed classification and complete-table topology limits
  outcome: supported
  summary: The saved graph contains a five-membered lactone C10(=O11)–O12–C7 in ring
    [7,8,9,10,12] and a separate acetate C23(=O24)–O22–C3 with methyl C25. Hydroxyl
    O13 is attached to C9 and O21 to CH2 C20. Three perceived rings and ring alkene
    C5=C6 remain explicit. The C5O candidate list is empty; no sugar residue is assigned.
    These graph facts support a bounded lactone/acetate interpretation without proving
    natural-product naming or a biosynthetic pathway. NPClassifier npclassifier.gnps2.org@2026-09-07
    reports Terpenoids, Sesquiterpenoids, Botryane sesquiterpenoids and is_glycoside:false.
    This is a versioned computed prediction, distinct from retained BGC/compound-class
    assertions and from independently established biosynthesis.
  target_ids:
  - naturalproductmech:mibig-0bd6ab53bc
  evidence_ids:
  - support-2248-capture
  - support-2248-topology
  - support-2248-structure-schema
  - support-2248-seeder
  - support-2248-row-npclassifier-0
  - support-2248-row-mibig_compounds-0
  dimensions:
  - name: computed_classification
    value: NPClassifier npclassifier.gnps2.org@2026-09-07 reports Terpenoids, Sesquiterpenoids,
      Botryane sesquiterpenoids and is_glycoside:false. This is a versioned computed
      prediction, distinct from retained BGC/compound-class assertions and from independently
      established biosynthesis.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-capture
    - support-2248-topology
    - support-2248-structure-schema
    - support-2248-seeder
    - support-2248-row-npclassifier-0
    - support-2248-row-mibig_compounds-0
- assessment_id: support-2248-A7
  area: completeness
  topic: Partial completion and maintained ownership
  outcome: unknown
  summary: The actual 57-input canonical intake, admitted plan and original paired
    computation support a partial scientific review. No selected mechanism root or
    component is present, so no selected maintained reader applies. Five local gates
    passed; FullQC, complete OAK and fresh external primary-source verification remain
    unavailable. No scientific source record or curation history was edited.
  target_ids:
  - naturalproductmech:mibig-0bd6ab53bc
  evidence_ids:
  - support-2248-intake
  - support-2248-intake-acceptance
  - support-2248-plan-acceptance
  - support-2248-diagnostic-acceptance
  - support-2248-native-gates
  - support-2248-review-profile
  - support-2248-mechanism-scope
  - support-2248-source-notes
  dimensions:
  - name: review_completion
    value: The actual 57-input canonical intake, admitted plan and original paired
      computation support a partial scientific review. No selected mechanism root
      or component is present, so no selected maintained reader applies. Five local
      gates passed; FullQC, complete OAK and fresh external primary-source verification
      remain unavailable. No scientific source record or curation history was edited.
    definition: Exact inspected scope; retained source assertions, original saved
      computation and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2248-intake
    - support-2248-intake-acceptance
    - support-2248-plan-acceptance
    - support-2248-diagnostic-acceptance
    - support-2248-native-gates
    - support-2248-review-profile
    - support-2248-mechanism-scope
    - support-2248-source-notes
findings: []
actions: []
limitations:
- FullQC and complete OAK were unavailable; five successful local gates do not establish
  scientific completeness.
- No external retrieval or live identifier, taxonomy, protein or publication query
  was performed. These assessments use the original saved owner-form computations;
  no additional molecular parses occurred during fragment authoring.
- The original chemistry stream contains two omitted-undefined-stereo warnings. They
  are global and are not attributed to specific owners from timing or inference.
- Retained source grades, database citations, cached taxonomy and versioned predictions
  keep their own scopes. Representation agreement does not prove natural identity,
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
- This selected owner has no four mechanism roots or components. No selected maintained
  reader applies; positive unselected annotations remain context only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-225
```
