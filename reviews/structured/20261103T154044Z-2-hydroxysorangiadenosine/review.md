# Local evidence review: 2-hydroxysorangiadenosine

- Review: 20261103T154044Z-2-hydroxysorangiadenosine
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T15:06:55.213212Z
- Finished UTC: 2026-11-03T15:40:44.978554Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

2-hydroxysorangiadenosine has locally matching stored identifiers, nine specified tetrahedral centres and a clear N-linked ribofuranosyl substructure. The retained classifier's false glycoside prediction has limited structural applicability and remains attributed as computed output. Producer and occurrence assertions are source-bound; no new biological activity or pathway is inferred.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2243; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-b7d597b9df | data/natural_products/terpenoids/2-hydroxysorangiadenosine.yaml | generated | 2-hydroxysorangiadenosine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-b7d597b9df | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-b7d597b9df | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-b7d597b9df | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-b7d597b9df | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-b7d597b9df | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-b7d597b9df | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-b7d597b9df | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-b7d597b9df | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-b7d597b9df.

The minted naturalproductmech:mibig-b7d597b9df identity follows MIBiG BGC0002339 compound index 1 and full key VMGXJYLNXQJWLG-QPUJKJSISA-N. Its retained ChEBI structure query is empty. The inherited NPAtlas NPA031448 cross-reference is supported as a source assertion in the MIBiG row, but its external structure was not independently resolved. The exact written stereochemical structure is retained without substitution from the compound name or classifier.

### Representation

representation: supported. Targets: naturalproductmech:mibig-b7d597b9df.

Both saved forms give neutral C25H37N5O5, 35 atoms and 39 bonds, with all ten comparisons true and complete stored correspondence. Nine detected tetrahedral centres are specified. The full tables show a hydroxylated carbon bicyclic moiety attached through N14 to the purine system, and an N19–C20 linkage to a five-membered C4O ring with two hydroxyl substituents and a hydroxymethyl group. This supports an N-ribofuranosyl structural interpretation at the encoded resolution; no additional experimental sugar or natural-form assignment is made.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-b7d597b9df.

MIBiG BGC0002339 version 3 is active, questionable and of unknown completeness. Vitiosangium cumulatum, taxon 1867796, is a SOURCE_ASSERTION producer; linkage on MT520811.1:1–27920 remains CLUSTER_UNSTATED with no recorded method. The single LOTUS occurrence uses the same taxon and a separately placed DOI. Shared organism identity does not turn occurrence into an independent production experiment or establish a complete pathway.

### Citations

evidence: unknown. Targets: naturalproductmech:mibig-b7d597b9df.

PMID:32527018 is the MIBiG ENTRY citation for producer/locus assertions; DOI:10.3390/MOLECULES25112676 backs the LOTUS occurrence. Their possible publication overlap was not resolved and no independent-experiment count is inferred. NPAtlas NPA031448 remains an inherited external cross-reference, not a freshly verified identity. No primary article, accession or protein sequence was retrieved under the no-request constraint.

### Bioactivity

evidence: supported. Targets: naturalproductmech:mibig-b7d597b9df.

The owner writes one Vitiosangium cumulatum occurrence and no assay observations, activity summary, molecular targets or mechanism roots. Exact retained PubChem, BindingDB and sibling-corpus queries are empty. These negatives apply to the admitted local sources only and do not establish inactivity. The nucleoside-like structural motif is not used to infer a molecular target or pharmacology.

### Classification

consistency: unknown. Targets: naturalproductmech:mibig-b7d597b9df.

The versioned NPClassifier output is TERPENOIDS/Diterpenoids with no class results and is_glycoside:false. The false prediction should not be read as a statement that the structure lacks a sugar moiety: the complete tables show a saturated C4O ring, two ring-carbon hydroxyls, a hydroxymethyl substituent and an anomeric carbon bonded to purine N. The narrow diagnostic helper searches six-membered C5O cycles and therefore cannot detect this five-membered ring. Schema and seeder define the field as named/versioned computed output and faithfully copy it; the review records an applicability limitation without overwriting the prediction or alleging an identity defect.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-b7d597b9df.

The complete owner/history, accepted source context, actual intake and both full saved molecular tables were reviewed. No supported local curation defect is established in this bounded scope. Five local gates passed; full QC, complete OAK and fresh external primary-source/taxonomy/accession verification were unavailable. The record remains scientifically partial, and its native curation status/history were not changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2243-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/2-hydroxysorangiadenosine.yaml; Whole owner plaintext and complete curation_history | supports | Complete 2-hydroxysorangiadenosine owner with 3 written history events, current full key VMGXJYLNXQJWLG-QPUJKJSISA-N and native status SEEDED. |
| bgc-2243-capture | /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json; /records/2/owner_pin; /records/2/owner_document | supports | Complete saved owner and exact raw pin for order 2243. |
| bgc-2243-intake | /private/tmp/npm-review-work/shared-next-batch225/intakes/2243-inspect-001.json; /source; /targets | supports | Actual inspection-only intake retains one target naturalproductmech:mibig-b7d597b9df and 37 source input placements with owner paths and ownership notes. |
| bgc-2243-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch225/root-intake-ready-001.json; /status; /intake_summary; /input_plan | supports | ROOT accepts the original ten canonical intakes and their current exact source maps; this is intake authority, not a scientific verdict. |
| bgc-2243-grounding-owner | /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json; /records/2/owner_document/identifier; /records/2/owner_document/label; /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status; /records/2/owner_document/grounding_notes; /records/2/owner_document/xrefs | supports | Written identity, structure, grounding and any definition, cross-reference or source discussion are retained exactly. {"identifier":"naturalproductmech:mibig-b7d597b9df","grounding_status":"MINTED"} |
| bgc-2243-origin-owner | /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters | supports | Written producer and locus assertions, grades, methods, references and any curator attribution: {"producer_organisms":[{"taxon_id":"NCBITaxon:1867796","taxon_label":"Vitiosangium cumulatum","evidence_basis":"SOURCE_ASSERTION","biosynthetic_gene_cluster":"mibig:BGC0002339","source":"MIBIG","source_version":"3","notes":"Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.","evidence":[{"reference":"PMID:32527018","evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0002339 entry version 3; citation taken from the entry level"}]}],"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0002339","entry_version":"3","entry_status":"active","organism_taxon_id":"NCBITaxon:1867796","organism_label":"Vitiosangium cumulatum","evidence":[{"reference":"PMID:32527018","evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0002339 entry version 3; citation taken from the entry level"}],"genome_accession":"genbank:MT520811.1","locus_from":1,"locus_to":27920,"bgc_class":["TERPENE"],"link_evidence_basis":"CLUSTER_UNSTATED"}]} |
| bgc-2243-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json; /records/2/owner_document/occurrences; /records/2/owner_document/occurrence_taxon_groups | supports | Written occurrence scope: {"occurrences":[{"taxon_id":"NCBITaxon:1867796","taxon_label":"Vitiosangium cumulatum","taxon_source":"NCBITaxon","source":"LOTUS","evidence":[{"reference":"DOI:10.3390/MOLECULES25112676","evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it."}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q62895080 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established."}],"occurrence_taxon_groups":["MYXOBACTERIAL"]}. No occurrence fields are inferred when absent. |
| bgc-2243-assay-owner | /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json; /records/2/owner_document | supports | Written activity and mechanism fields: {}. Mechanism roots present: []. |
| bgc-2243-classification-owner | /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json; /records/2/owner_document/np_pathway; /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class; /records/2/owner_document/biosynthesis_origin; /records/2/owner_document/producer_taxon_groups; /records/2/owner_document/occurrence_taxon_groups | supports | Retained owner classifications and taxon-group labels: {"np_pathway":"TERPENOIDS","np_classification":{"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":["Terpenoids"],"superclass_results":["Diterpenoids"],"class_results":[],"is_glycoside":false},"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","producer_taxon_groups":["MYXOBACTERIAL"],"occurrence_taxon_groups":["MYXOBACTERIAL"]} |
| bgc-2243-source-plan | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2 | supports | Accepted selected-record source projection, complete raw history, exact joins and proposed input map; the actual intake is separately cited. |
| bgc-2243-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch225/root-input-plan-acceptance-001.json; /status; /plan; /inventory; /source_notes; /source_placements; /unique_source_paths; /per_order_counts | supports | ROOT accepts actual plan 412 placements/77 paths and the complete selected/direct projections, with future maintained-reader results separate. |
| bgc-2243-source-notes | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-source-scope-notes-001.json; /reading; /curation; /cautions | supports | Complete BGC/Support whole-source reading attribution, bounded curation scan and source qualifications. The sole applicable token hit is the Pristinol locus override; reserved decisions.tsv was not consumed. |
| bgc-2243-chemistry | /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/smiles; /records/2/inchi; /records/2/comparisons; /records/2/atom_correspondence | supports | Saved original paired forms and all computed fields: {"order":2243,"declared":{"smiles":"C=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1","standard_inchi":"InChI=1S/C25H37N5O5/c1-13(2)14-5-6-24(3)8-15(32)9-25(4,17(24)7-14)29-21-18-22(27-11-26-21)30(12-28-18)23-20(34)19(33)16(10-31)35-23/h11-12,14-17,19-20,23,31-34H,1,5-10H2,2-4H3,(H,26,27,29)/t14-,15-,16-,17-,19-,20-,23-,24+,25-/m1/s1","standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0002339"},"smiles_status":"parsed","inchi_status":"parsed","comparisons":{"formula_equal":true,"formal_charge_equal":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"smiles_formula_equals_literal_InChI_main_layer":true},"map":{"smiles_to_inchi_atom_indices":[0,12,1,13,4,5,23,2,7,14,31,8,24,3,28,20,17,27,11,29,22,34,15,9,30,18,32,19,33,21,26,10,25,16,6],"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim."}}. |
| bgc-2243-topology | /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-DATA-001.json; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/smiles/computed/rings; /records/2/smiles/computed/motifs; /records/2/smiles/computed/potential_stereo; /records/2/smiles/computed/stereo_counts; /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds; /records/2/inchi/computed/rings; /records/2/inchi/computed/motifs; /records/2/inchi/computed/potential_stereo; /records/2/inchi/computed/stereo_counts; /records/2/atom_correspondence; /records/2/declared_structure | supports | The SMILES ring C20–O21–C22–C25–C27 has C22–C23–O24 hydroxymethyl, C25–O26 and C27–O28 hydroxyl groups, with anomeric C20 bonded to purine N19. All these bonds and stereochemical centres have corresponding InChI-table entries via the complete saved map. The saturated_six_membered_C5O_cycles helper is empty because this ring has four carbons and one oxygen, not because the full structure lacks a sugar moiety. |
| bgc-2243-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-execution-001.json; /exit_code; /DATA; /stdout; /stderr; /external_requests; /retries | supports | ROOT's original diagnostic execution exited zero, retains exact DATA and original stream pins, reports no external request and zero retries. |
| bgc-2243-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-001.stderr; Complete original stderr (both warnings) | supports | Two original 'Omitted undefined stereo' warnings occur in the batch-level stream; neither is assigned to an owner or representation. |
| bgc-2243-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch225/root-local-diagnostics-acceptance-001.json; /status; /DATA; /execution; /limits | supports | ROOT accepts the original saved chemistry in its stated mechanical scope; source/natural identity and scientific completion remain separate. |
| bgc-2243-native-acceptance | /private/tmp/npm-review-work/shared-next-batch225/root-native-five-gates-acceptance-001.json; /status; /ledger; /results; /full_QC_available; /complete_OAK_authority_available; /all_native_gates_passed | supports | Five local commands passed; full QC and complete OAK authority were unavailable, so all_native_gates_passed remains false. |
| bgc-2243-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2/source_scope_inventory/joins/mibig_compounds | supports | Exact retained query frame: {"predicate":"exact complete standard_inchi_key equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[{"physical_line":2848,"last_physical_line":2848,"row":{"mibig_accession":"BGC0002339","entry_version":"3","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"2-hydroxysorangiadenosine","compound_index":"1","smiles":"C=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1","standard_inchi":"InChI=1S/C25H37N5O5/c1-13(2)14-5-6-24(3)8-15(32)9-25(4,17(24)7-14)29-21-18-22(27-11-26-21)30(12-28-18)23-20(34)19(33)16(10-31)35-23/h11-12,14-17,19-20,23,31-34H,1,5-10H2,2-4H3,(H,26,27,29)/t14-,15-,16-,17-,19-,20-,23-,24+,25-/m1/s1","standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA031448","taxon_id":"NCBITaxon:1867796","taxon_label":"Vitiosangium cumulatum","bgc_classes":"terpene","bgc_subclasses":"Unknown","genome_accession":"MT520811.1","locus_from":"1","locus_to":"27920","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:32527018","reference_basis":"ENTRY"},"raw_tsv_record":"BGC0002339\t3\tactive\tquestionable\tunknown\t2-hydroxysorangiadenosine\t1\tC=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1\tInChI=1S/C25H37N5O5/c1-13(2)14-5-6-24(3)8-15(32)9-25(4,17(24)7-14)29-21-18-22(27-11-26-21)30(12-28-18)23-20(34)19(33)16(10-31)35-23/h11-12,14-17,19-20,23,31-34H,1,5-10H2,2-4H3,(H,26,27,29)/t14-,15-,16-,17-,19-,20-,23-,24+,25-/m1/s1\tVMGXJYLNXQJWLG-QPUJKJSISA-N\ttrue\t\tnpatlas:NPA031448\tNCBITaxon:1867796\tVitiosangium cumulatum\tterpene\tUnknown\tMT520811.1\t1\t27920\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:32527018\tENTRY\n","row_sha256":"051ff0baecf0310e91792bb1ce3b033c8be74eafd3d131048e791ffda9b008ae"}]} |
| bgc-2243-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 2848 | supports | Complete retained physical source payloads, with each original line and full CSV fields: [{"physical_line":2848,"last_physical_line":2848,"row":{"mibig_accession":"BGC0002339","entry_version":"3","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"2-hydroxysorangiadenosine","compound_index":"1","smiles":"C=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1","standard_inchi":"InChI=1S/C25H37N5O5/c1-13(2)14-5-6-24(3)8-15(32)9-25(4,17(24)7-14)29-21-18-22(27-11-26-21)30(12-28-18)23-20(34)19(33)16(10-31)35-23/h11-12,14-17,19-20,23,31-34H,1,5-10H2,2-4H3,(H,26,27,29)/t14-,15-,16-,17-,19-,20-,23-,24+,25-/m1/s1","standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA031448","taxon_id":"NCBITaxon:1867796","taxon_label":"Vitiosangium cumulatum","bgc_classes":"terpene","bgc_subclasses":"Unknown","genome_accession":"MT520811.1","locus_from":"1","locus_to":"27920","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:32527018","reference_basis":"ENTRY"},"row_sha256":"051ff0baecf0310e91792bb1ce3b033c8be74eafd3d131048e791ffda9b008ae"}] |
| bgc-2243-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2/source_scope_inventory/joins/chebi_structures | supports | Exact retained query frame: {"predicate":"exact complete standard_inchi_key equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[]} |
| bgc-2243-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2/source_scope_inventory/joins/lotus_occurrences | supports | Exact retained query frame: {"predicate":"exact complete standard_inchi_key equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[{"physical_line":9065,"last_physical_line":9065,"row":{"standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","organism_name":"Vitiosangium cumulatum","taxon_id":"NCBITaxon:1867796","organism_wikidata":"http://www.wikidata.org/entity/Q62895080","reference_doi":"10.3390/MOLECULES25112676","structure_wikidata":"http://www.wikidata.org/entity/Q110171401"},"raw_tsv_record":"VMGXJYLNXQJWLG-QPUJKJSISA-N\tVitiosangium cumulatum\tNCBITaxon:1867796\thttp://www.wikidata.org/entity/Q62895080\t10.3390/MOLECULES25112676\thttp://www.wikidata.org/entity/Q110171401\n","row_sha256":"a79234c259910b3956e5ee1d3102d890f0e54ff5cdef3cfc1d6ef1ed23bdedbf"}]} |
| bgc-2243-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 9065 | supports | Complete retained physical source payloads, with each original line and full CSV fields: [{"physical_line":9065,"last_physical_line":9065,"row":{"standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","organism_name":"Vitiosangium cumulatum","taxon_id":"NCBITaxon:1867796","organism_wikidata":"http://www.wikidata.org/entity/Q62895080","reference_doi":"10.3390/MOLECULES25112676","structure_wikidata":"http://www.wikidata.org/entity/Q110171401"},"row_sha256":"a79234c259910b3956e5ee1d3102d890f0e54ff5cdef3cfc1d6ef1ed23bdedbf"}] |
| bgc-2243-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2/source_scope_inventory/joins/cyanometdb_occurrences | supports | Exact retained query frame: {"predicate":"exact complete standard_inchi_key equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[]} |
| bgc-2243-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2/source_scope_inventory/joins/npclassifier | supports | Exact retained query frame: {"predicate":"exact complete standard_inchi_key equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[{"physical_line":2543,"last_physical_line":2543,"row":{"standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","smiles":"C=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1","pathway_results":"Terpenoids","superclass_results":"Diterpenoids","class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"},"raw_tsv_record":"VMGXJYLNXQJWLG-QPUJKJSISA-N\tC=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1\tTerpenoids\tDiterpenoids\t\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row_sha256":"f26ac505e36e21108151cddd673b72c1aba68e893f43a7e334ac69cc2aa17d45"}]} |
| bgc-2243-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 2543 | supports | Complete retained physical source payloads, with each original line and full CSV fields: [{"physical_line":2543,"last_physical_line":2543,"row":{"standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","smiles":"C=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1","pathway_results":"Terpenoids","superclass_results":"Diterpenoids","class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"},"row_sha256":"f26ac505e36e21108151cddd673b72c1aba68e893f43a7e334ac69cc2aa17d45"}] |
| bgc-2243-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2/source_scope_inventory/joins/pubchem_bioassay | supports | Exact retained query frame: {"predicate":"exact complete standard_inchi_key equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[]} |
| bgc-2243-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2/source_scope_inventory/joins/bindingdb_targets | supports | Exact retained query frame: {"predicate":"exact complete standard_inchi_key equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[]} |
| bgc-2243-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Exact retained query frame: {"predicate":"exact complete standard_inchi_key equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[]} |
| bgc-2243-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2/source_scope_inventory/joins/chebi_origins | supports | Exact retained query frame: {"predicate":"exact chebi_id from exact full-key structure rows","query":[],"matches":[]} |
| bgc-2243-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/23 | supports | Complete retained cached stanza scope: [{"id":"NCBITaxon:1867796","physical_line":139737,"complete_stanza":"[Term]\nid: NCBITaxon:1867796\nname: Vitiosangium cumulatum\n\n"}]. Cached names/synonyms do not constitute a fresh taxonomy request. |
| bgc-2243-source-routes | /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json; /records/2/source_scope_inventory/source_taxa; /records/2/source_scope_inventory/forward_taxon_merge_matches; /records/2/source_scope_inventory/nonorganism_matches | supports | Exact selected-record source taxa and retained forward/nonorganism route sets: {"source_taxa":["NCBITaxon:1867796"],"forward_taxon_merge_matches":[],"nonorganism_matches":[]} |
| bgc-2243-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Workflow; Output | supports | Maintained local review recipe requires claim-specific source support and qualified completion; external retrieval is overridden by the absolute no-request instruction. |
| bgc-2243-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Complete maintained review profile | supports | Maintained dimensions, producer/occurrence and source-versus-computed scope, one-record review and partial completion requirements. |
| bgc-2243-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 376–432 | supports | ChemicalStructure stereo flag description and ComputedClassification named/versioned output semantics; is_glycoside is a computed boolean, not a source assertion. |
| bgc-2243-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 145–175 | supports | Maintained MIBiG extractor derives standardized identifiers and the stereo_complete flag from FindMolChiralCenters including unassigned centres; no experiment or complete geometric-stereo authentication is performed by this method. |
| bgc-2243-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 980–1030 | supports | Seeder preserves the selected structure, exact ChEBI definition and named/versioned classifier results, including the literal glycoside prediction. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-225/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-225/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-225/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-225/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-225/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-225/native-current225-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External identifiers, taxonomy, accessions and primary publications were not refreshed under the absolute no-request instruction; historical and database assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and parsing establish their declared mechanical scope only.
- Negative source joins apply only to exact retained predicates and snapshots. Shared loci, citations and companions do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source records, raw snapshots, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete source payloads and personal/delegated direct-context whole-reading attribution are retained in the pinned source notes. Assigned actual intakes, complete selected owners/history and every paired saved molecular table were personally read.
- Two original batch-level undefined-stereo warnings remain globally unassigned. True comparison flags and a complete correspondence do not override full_graph_identity_established:false.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T154044Z-2-hydroxysorangiadenosine
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: 2-hydroxysorangiadenosine'
started_at: '2026-11-03T15:06:55.213212Z'
finished_at: '2026-11-03T15:40:44.978554Z'
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
summary: 2-hydroxysorangiadenosine has locally matching stored identifiers, nine specified
  tetrahedral centres and a clear N-linked ribofuranosyl substructure. The retained
  classifier's false glycoside prediction has limited structural applicability and
  remains attributed as computed output. Producer and occurrence assertions are source-bound;
  no new biological activity or pathway is inferred.
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
  - path: data/natural_products/terpenoids/2-hydroxysorangiadenosine.yaml
    sha256: 3d5825a17a51dd089e794693c3262581e5661a41c4f634384c8e6852f163c774
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
  selection: Campaign path order 2243; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-b7d597b9df
targets:
- target_id: naturalproductmech:mibig-b7d597b9df
  path: data/natural_products/terpenoids/2-hydroxysorangiadenosine.yaml
  label: 2-hydroxysorangiadenosine
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
  - naturalproductmech:mibig-b7d597b9df
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
  - naturalproductmech:mibig-b7d597b9df
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
  - naturalproductmech:mibig-b7d597b9df
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
  - naturalproductmech:mibig-b7d597b9df
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
  - naturalproductmech:mibig-b7d597b9df
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
  - naturalproductmech:mibig-b7d597b9df
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b7d597b9df
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b7d597b9df
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2243-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/2-hydroxysorangiadenosine.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Complete 2-hydroxysorangiadenosine owner with 3 written history events,
    current full key VMGXJYLNXQJWLG-QPUJKJSISA-N and native status SEEDED.
  snapshot_sha256: 3d5825a17a51dd089e794693c3262581e5661a41c4f634384c8e6852f163c774
- evidence_id: bgc-2243-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json
  locator: /records/2/owner_pin; /records/2/owner_document
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Complete saved owner and exact raw pin for order 2243.
  snapshot_sha256: 0e9d3e869f9ce737ea339dd4952cbb014b2b826c4f2822ee7db6b4f5a1a28533
- evidence_id: bgc-2243-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/intakes/2243-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Actual inspection-only intake retains one target naturalproductmech:mibig-b7d597b9df
    and 37 source input placements with owner paths and ownership notes.
  snapshot_sha256: 2a2e503172518c92d5004c6c0b451f344c7ef01b9a6b56ac31927f3ac7b5594c
- evidence_id: bgc-2243-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/root-intake-ready-001.json
  locator: /status; /intake_summary; /input_plan
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: ROOT accepts the original ten canonical intakes and their current exact
    source maps; this is intake authority, not a scientific verdict.
  snapshot_sha256: 6f3cca33d9d1304a058b16e62e10dd34951397c511d1e28efd688778eb0a591f
- evidence_id: bgc-2243-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json
  locator: /records/2/owner_document/identifier; /records/2/owner_document/label;
    /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts;
    /records/2/owner_document/grounding_status; /records/2/owner_document/grounding_notes;
    /records/2/owner_document/xrefs
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Written identity, structure, grounding and any definition, cross-reference
    or source discussion are retained exactly. {"identifier":"naturalproductmech:mibig-b7d597b9df","grounding_status":"MINTED"}
  snapshot_sha256: 0e9d3e869f9ce737ea339dd4952cbb014b2b826c4f2822ee7db6b4f5a1a28533
- evidence_id: bgc-2243-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Written producer and locus assertions, grades, methods, references and
    any curator attribution: {"producer_organisms":[{"taxon_id":"NCBITaxon:1867796","taxon_label":"Vitiosangium
    cumulatum","evidence_basis":"SOURCE_ASSERTION","biosynthetic_gene_cluster":"mibig:BGC0002339","source":"MIBIG","source_version":"3","notes":"Locus
    evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this
    field grades the taxon claim, which is a different question.","evidence":[{"reference":"PMID:32527018","evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0002339 entry version 3; citation taken from the entry level"}]}],"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0002339","entry_version":"3","entry_status":"active","organism_taxon_id":"NCBITaxon:1867796","organism_label":"Vitiosangium
    cumulatum","evidence":[{"reference":"PMID:32527018","evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0002339 entry version 3; citation taken from the entry level"}],"genome_accession":"genbank:MT520811.1","locus_from":1,"locus_to":27920,"bgc_class":["TERPENE"],"link_evidence_basis":"CLUSTER_UNSTATED"}]}'
  snapshot_sha256: 0e9d3e869f9ce737ea339dd4952cbb014b2b826c4f2822ee7db6b4f5a1a28533
- evidence_id: bgc-2243-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json
  locator: /records/2/owner_document/occurrences; /records/2/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Written occurrence scope: {"occurrences":[{"taxon_id":"NCBITaxon:1867796","taxon_label":"Vitiosangium
    cumulatum","taxon_source":"NCBITaxon","source":"LOTUS","evidence":[{"reference":"DOI:10.3390/MOLECULES25112676","evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it."}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q62895080 This taxon is also recorded
    as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established."}],"occurrence_taxon_groups":["MYXOBACTERIAL"]}.
    No occurrence fields are inferred when absent.'
  snapshot_sha256: 0e9d3e869f9ce737ea339dd4952cbb014b2b826c4f2822ee7db6b4f5a1a28533
- evidence_id: bgc-2243-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Written activity and mechanism fields: {}. Mechanism roots present: [].'
  snapshot_sha256: 0e9d3e869f9ce737ea339dd4952cbb014b2b826c4f2822ee7db6b4f5a1a28533
- evidence_id: bgc-2243-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_pathway; /records/2/owner_document/np_classification;
    /records/2/owner_document/bgc_class; /records/2/owner_document/biosynthesis_origin;
    /records/2/owner_document/producer_taxon_groups; /records/2/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Retained owner classifications and taxon-group labels: {"np_pathway":"TERPENOIDS","np_classification":{"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":["Terpenoids"],"superclass_results":["Diterpenoids"],"class_results":[],"is_glycoside":false},"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","producer_taxon_groups":["MYXOBACTERIAL"],"occurrence_taxon_groups":["MYXOBACTERIAL"]}'
  snapshot_sha256: 0e9d3e869f9ce737ea339dd4952cbb014b2b826c4f2822ee7db6b4f5a1a28533
- evidence_id: bgc-2243-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Accepted selected-record source projection, complete raw history, exact
    joins and proposed input map; the actual intake is separately cited.
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/root-input-plan-acceptance-001.json
  locator: /status; /plan; /inventory; /source_notes; /source_placements; /unique_source_paths;
    /per_order_counts
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: ROOT accepts actual plan 412 placements/77 paths and the complete selected/direct
    projections, with future maintained-reader results separate.
  snapshot_sha256: 8b553f64807b674d1731148a3995b48ceca2b42aa4cd763c5f306ef84992a96d
- evidence_id: bgc-2243-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-source-scope-notes-001.json
  locator: /reading; /curation; /cautions
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Complete BGC/Support whole-source reading attribution, bounded curation
    scan and source qualifications. The sole applicable token hit is the Pristinol
    locus override; reserved decisions.tsv was not consumed.
  snapshot_sha256: 08f2dd0c94feafa1b7201db4b7fff3d4218aade05b41a8b71c566de4f60ed0ed
- evidence_id: bgc-2243-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/smiles; /records/2/inchi; /records/2/comparisons;
    /records/2/atom_correspondence
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Saved original paired forms and all computed fields: {"order":2243,"declared":{"smiles":"C=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1","standard_inchi":"InChI=1S/C25H37N5O5/c1-13(2)14-5-6-24(3)8-15(32)9-25(4,17(24)7-14)29-21-18-22(27-11-26-21)30(12-28-18)23-20(34)19(33)16(10-31)35-23/h11-12,14-17,19-20,23,31-34H,1,5-10H2,2-4H3,(H,26,27,29)/t14-,15-,16-,17-,19-,20-,23-,24+,25-/m1/s1","standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0002339"},"smiles_status":"parsed","inchi_status":"parsed","comparisons":{"formula_equal":true,"formal_charge_equal":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"smiles_formula_equals_literal_InChI_main_layer":true},"map":{"smiles_to_inchi_atom_indices":[0,12,1,13,4,5,23,2,7,14,31,8,24,3,28,20,17,27,11,29,22,34,15,9,30,18,32,19,33,21,26,10,25,16,6],"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim."}}.'
  snapshot_sha256: 2c67ccbf2df2c8fee5fd0761d179566903ed7db15c60650d2cff295cbac068a7
- evidence_id: bgc-2243-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/smiles/computed/rings;
    /records/2/smiles/computed/motifs; /records/2/smiles/computed/potential_stereo;
    /records/2/smiles/computed/stereo_counts; /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds;
    /records/2/inchi/computed/rings; /records/2/inchi/computed/motifs; /records/2/inchi/computed/potential_stereo;
    /records/2/inchi/computed/stereo_counts; /records/2/atom_correspondence; /records/2/declared_structure
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: The SMILES ring C20–O21–C22–C25–C27 has C22–C23–O24 hydroxymethyl, C25–O26
    and C27–O28 hydroxyl groups, with anomeric C20 bonded to purine N19. All these
    bonds and stereochemical centres have corresponding InChI-table entries via the
    complete saved map. The saturated_six_membered_C5O_cycles helper is empty because
    this ring has four carbons and one oxygen, not because the full structure lacks
    a sugar moiety.
  snapshot_sha256: 2c67ccbf2df2c8fee5fd0761d179566903ed7db15c60650d2cff295cbac068a7
- evidence_id: bgc-2243-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /DATA; /stdout; /stderr; /external_requests; /retries
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: ROOT's original diagnostic execution exited zero, retains exact DATA and
    original stream pins, reports no external request and zero retries.
  snapshot_sha256: 78ad622a43d40672797351398f42ca4e4d960b9d268915937dd62a54571c00fa
- evidence_id: bgc-2243-diagnostic-stderr
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/chemistry-local/diagnostic-001.stderr
  locator: Complete original stderr (both warnings)
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Two original 'Omitted undefined stereo' warnings occur in the batch-level
    stream; neither is assigned to an owner or representation.
  snapshot_sha256: 7447721aa4c9980e1edf852cb15b182da2b510529ddd5ecabec31c40b6ecf085
- evidence_id: bgc-2243-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/root-local-diagnostics-acceptance-001.json
  locator: /status; /DATA; /execution; /limits
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: ROOT accepts the original saved chemistry in its stated mechanical scope;
    source/natural identity and scientific completion remain separate.
  snapshot_sha256: 9bc1a44f264ea5a8261064ea20b2d3ced43e1608a6bebdeb0b235c4476564e9f
- evidence_id: bgc-2243-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225/root-native-five-gates-acceptance-001.json
  locator: /status; /ledger; /results; /full_QC_available; /complete_OAK_authority_available;
    /all_native_gates_passed
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Five local commands passed; full QC and complete OAK authority were unavailable,
    so all_native_gates_passed remains false.
  snapshot_sha256: e5b971aac7d6c7f0502248a9f3b9a6554500b2b131c408cdca84f95fd4229b0f
- evidence_id: bgc-2243-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Exact retained query frame: {"predicate":"exact complete standard_inchi_key
    equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[{"physical_line":2848,"last_physical_line":2848,"row":{"mibig_accession":"BGC0002339","entry_version":"3","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"2-hydroxysorangiadenosine","compound_index":"1","smiles":"C=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1","standard_inchi":"InChI=1S/C25H37N5O5/c1-13(2)14-5-6-24(3)8-15(32)9-25(4,17(24)7-14)29-21-18-22(27-11-26-21)30(12-28-18)23-20(34)19(33)16(10-31)35-23/h11-12,14-17,19-20,23,31-34H,1,5-10H2,2-4H3,(H,26,27,29)/t14-,15-,16-,17-,19-,20-,23-,24+,25-/m1/s1","standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA031448","taxon_id":"NCBITaxon:1867796","taxon_label":"Vitiosangium
    cumulatum","bgc_classes":"terpene","bgc_subclasses":"Unknown","genome_accession":"MT520811.1","locus_from":"1","locus_to":"27920","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:32527018","reference_basis":"ENTRY"},"raw_tsv_record":"BGC0002339\t3\tactive\tquestionable\tunknown\t2-hydroxysorangiadenosine\t1\tC=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1\tInChI=1S/C25H37N5O5/c1-13(2)14-5-6-24(3)8-15(32)9-25(4,17(24)7-14)29-21-18-22(27-11-26-21)30(12-28-18)23-20(34)19(33)16(10-31)35-23/h11-12,14-17,19-20,23,31-34H,1,5-10H2,2-4H3,(H,26,27,29)/t14-,15-,16-,17-,19-,20-,23-,24+,25-/m1/s1\tVMGXJYLNXQJWLG-QPUJKJSISA-N\ttrue\t\tnpatlas:NPA031448\tNCBITaxon:1867796\tVitiosangium
    cumulatum\tterpene\tUnknown\tMT520811.1\t1\t27920\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:32527018\tENTRY\n","row_sha256":"051ff0baecf0310e91792bb1ce3b033c8be74eafd3d131048e791ffda9b008ae"}]}'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 2848
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Complete retained physical source payloads, with each original line and
    full CSV fields: [{"physical_line":2848,"last_physical_line":2848,"row":{"mibig_accession":"BGC0002339","entry_version":"3","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"2-hydroxysorangiadenosine","compound_index":"1","smiles":"C=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1","standard_inchi":"InChI=1S/C25H37N5O5/c1-13(2)14-5-6-24(3)8-15(32)9-25(4,17(24)7-14)29-21-18-22(27-11-26-21)30(12-28-18)23-20(34)19(33)16(10-31)35-23/h11-12,14-17,19-20,23,31-34H,1,5-10H2,2-4H3,(H,26,27,29)/t14-,15-,16-,17-,19-,20-,23-,24+,25-/m1/s1","standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA031448","taxon_id":"NCBITaxon:1867796","taxon_label":"Vitiosangium
    cumulatum","bgc_classes":"terpene","bgc_subclasses":"Unknown","genome_accession":"MT520811.1","locus_from":"1","locus_to":"27920","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:32527018","reference_basis":"ENTRY"},"row_sha256":"051ff0baecf0310e91792bb1ce3b033c8be74eafd3d131048e791ffda9b008ae"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2243-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Exact retained query frame: {"predicate":"exact complete standard_inchi_key
    equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[]}'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Exact retained query frame: {"predicate":"exact complete standard_inchi_key
    equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[{"physical_line":9065,"last_physical_line":9065,"row":{"standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","organism_name":"Vitiosangium
    cumulatum","taxon_id":"NCBITaxon:1867796","organism_wikidata":"http://www.wikidata.org/entity/Q62895080","reference_doi":"10.3390/MOLECULES25112676","structure_wikidata":"http://www.wikidata.org/entity/Q110171401"},"raw_tsv_record":"VMGXJYLNXQJWLG-QPUJKJSISA-N\tVitiosangium
    cumulatum\tNCBITaxon:1867796\thttp://www.wikidata.org/entity/Q62895080\t10.3390/MOLECULES25112676\thttp://www.wikidata.org/entity/Q110171401\n","row_sha256":"a79234c259910b3956e5ee1d3102d890f0e54ff5cdef3cfc1d6ef1ed23bdedbf"}]}'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-source-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 9065
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Complete retained physical source payloads, with each original line and
    full CSV fields: [{"physical_line":9065,"last_physical_line":9065,"row":{"standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","organism_name":"Vitiosangium
    cumulatum","taxon_id":"NCBITaxon:1867796","organism_wikidata":"http://www.wikidata.org/entity/Q62895080","reference_doi":"10.3390/MOLECULES25112676","structure_wikidata":"http://www.wikidata.org/entity/Q110171401"},"row_sha256":"a79234c259910b3956e5ee1d3102d890f0e54ff5cdef3cfc1d6ef1ed23bdedbf"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2243-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Exact retained query frame: {"predicate":"exact complete standard_inchi_key
    equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[]}'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Exact retained query frame: {"predicate":"exact complete standard_inchi_key
    equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[{"physical_line":2543,"last_physical_line":2543,"row":{"standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","smiles":"C=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1","pathway_results":"Terpenoids","superclass_results":"Diterpenoids","class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"},"raw_tsv_record":"VMGXJYLNXQJWLG-QPUJKJSISA-N\tC=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1\tTerpenoids\tDiterpenoids\t\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row_sha256":"f26ac505e36e21108151cddd673b72c1aba68e893f43a7e334ac69cc2aa17d45"}]}'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 2543
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Complete retained physical source payloads, with each original line and
    full CSV fields: [{"physical_line":2543,"last_physical_line":2543,"row":{"standard_inchi_key":"VMGXJYLNXQJWLG-QPUJKJSISA-N","smiles":"C=C(C)[C@@H]1CC[C@@]2(C)C[C@@H](O)C[C@@](C)(NC3=C4N=CN([C@@H]5O[C@H](CO)[C@@H](O)[C@H]5O)C4=NC=N3)[C@@H]2C1","pathway_results":"Terpenoids","superclass_results":"Diterpenoids","class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"},"row_sha256":"f26ac505e36e21108151cddd673b72c1aba68e893f43a7e334ac69cc2aa17d45"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2243-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Exact retained query frame: {"predicate":"exact complete standard_inchi_key
    equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[]}'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Exact retained query frame: {"predicate":"exact complete standard_inchi_key
    equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[]}'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Exact retained query frame: {"predicate":"exact complete standard_inchi_key
    equality","query":"VMGXJYLNXQJWLG-QPUJKJSISA-N","matches":[]}'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Exact retained query frame: {"predicate":"exact chebi_id from exact full-key
    structure rows","query":[],"matches":[]}'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/23
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Complete retained cached stanza scope: [{"id":"NCBITaxon:1867796","physical_line":139737,"complete_stanza":"[Term]\nid:
    NCBITaxon:1867796\nname: Vitiosangium cumulatum\n\n"}]. Cached names/synonyms
    do not constitute a fresh taxonomy request.'
  snapshot_sha256: b814a5b49ac654cfd225277d7051ab2f340aeb58b4813f4d490ee23cb81ba5d7
- evidence_id: bgc-2243-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch225-tentative/bgc-prep/bgc-conditional225-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/source_taxa; /records/2/source_scope_inventory/forward_taxon_merge_matches;
    /records/2/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: 'Exact selected-record source taxa and retained forward/nonorganism route
    sets: {"source_taxa":["NCBITaxon:1867796"],"forward_taxon_merge_matches":[],"nonorganism_matches":[]}'
  snapshot_sha256: ea79b0d33c11111a64d6c66fb00ee86bd6a5db54bc5c2277f8e767926e012e9f
- evidence_id: bgc-2243-review-skill
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Workflow; Output
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Maintained local review recipe requires claim-specific source support and
    qualified completion; external retrieval is overridden by the absolute no-request
    instruction.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2243-review-profile
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Complete maintained review profile
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Maintained dimensions, producer/occurrence and source-versus-computed scope,
    one-record review and partial completion requirements.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2243-structure-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 376–432
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: ChemicalStructure stereo flag description and ComputedClassification named/versioned
    output semantics; is_glycoside is a computed boolean, not a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2243-stereo-method
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 145–175
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Maintained MIBiG extractor derives standardized identifiers and the stereo_complete
    flag from FindMolChiralCenters including unassigned centres; no experiment or
    complete geometric-stereo authentication is performed by this method.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2243-classification-seeder
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 980–1030
  accessed_at: '2026-11-03T15:28:51.475150Z'
  support: supports
  summary: Seeder preserves the selected structure, exact ChEBI definition and named/versioned
    classifier results, including the literal glycoside prediction.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
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
- assessment_id: bgc-2243-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The minted naturalproductmech:mibig-b7d597b9df identity follows MIBiG BGC0002339
    compound index 1 and full key VMGXJYLNXQJWLG-QPUJKJSISA-N. Its retained ChEBI
    structure query is empty. The inherited NPAtlas NPA031448 cross-reference is supported
    as a source assertion in the MIBiG row, but its external structure was not independently
    resolved. The exact written stereochemical structure is retained without substitution
    from the compound name or classifier.
  target_ids:
  - naturalproductmech:mibig-b7d597b9df
  evidence_ids:
  - bgc-2243-grounding-owner
  - bgc-2243-chemistry
  - bgc-2243-query-chebi_structures
  - bgc-2243-source-mibig_compounds
  dimensions:
  - name: standard_inchi_key
    value: VMGXJYLNXQJWLG-QPUJKJSISA-N; exact retained MIBiG owner.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2243-grounding-owner
    - bgc-2243-chemistry
    - bgc-2243-query-chebi_structures
    - bgc-2243-source-mibig_compounds
  - name: grounding_scope
    value: Minted identity with no retained ChEBI match; NPAtlas link remains unrefreshed.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2243-grounding-owner
    - bgc-2243-chemistry
    - bgc-2243-query-chebi_structures
    - bgc-2243-source-mibig_compounds
- assessment_id: bgc-2243-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both saved forms give neutral C25H37N5O5, 35 atoms and 39 bonds, with all
    ten comparisons true and complete stored correspondence. Nine detected tetrahedral
    centres are specified. The full tables show a hydroxylated carbon bicyclic moiety
    attached through N14 to the purine system, and an N19–C20 linkage to a five-membered
    C4O ring with two hydroxyl substituents and a hydroxymethyl group. This supports
    an N-ribofuranosyl structural interpretation at the encoded resolution; no additional
    experimental sugar or natural-form assignment is made.
  target_ids:
  - naturalproductmech:mibig-b7d597b9df
  evidence_ids:
  - bgc-2243-grounding-owner
  - bgc-2243-chemistry
  - bgc-2243-topology
  - bgc-2243-diagnostic-acceptance
  - bgc-2243-structure-schema
  - bgc-2243-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Nine specified tetrahedral centres; N-ribofuranosyl configuration remains
      the encoded structure, not new experimental evidence.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2243-grounding-owner
    - bgc-2243-chemistry
    - bgc-2243-topology
    - bgc-2243-diagnostic-acceptance
    - bgc-2243-structure-schema
    - bgc-2243-stereo-method
  - name: representation_correspondence
    value: All ten flags true; complete stored correspondence, without an independent
      natural-identity claim.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2243-grounding-owner
    - bgc-2243-chemistry
    - bgc-2243-topology
    - bgc-2243-diagnostic-acceptance
    - bgc-2243-structure-schema
    - bgc-2243-stereo-method
- assessment_id: bgc-2243-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: MIBiG BGC0002339 version 3 is active, questionable and of unknown completeness.
    Vitiosangium cumulatum, taxon 1867796, is a SOURCE_ASSERTION producer; linkage
    on MT520811.1:1–27920 remains CLUSTER_UNSTATED with no recorded method. The single
    LOTUS occurrence uses the same taxon and a separately placed DOI. Shared organism
    identity does not turn occurrence into an independent production experiment or
    establish a complete pathway.
  target_ids:
  - naturalproductmech:mibig-b7d597b9df
  evidence_ids:
  - bgc-2243-origin-owner
  - bgc-2243-occurrence-owner
  - bgc-2243-source-mibig_compounds
  - bgc-2243-source-lotus_occurrences
  - bgc-2243-cached-taxonomy
  - bgc-2243-source-routes
  - bgc-2243-review-profile
  dimensions:
  - name: taxon_scope
    value: Producer and occurrence use Vitiosangium cumulatum 1867796, with claim
      roles kept distinct.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2243-origin-owner
    - bgc-2243-occurrence-owner
    - bgc-2243-source-mibig_compounds
    - bgc-2243-source-lotus_occurrences
    - bgc-2243-cached-taxonomy
    - bgc-2243-source-routes
    - bgc-2243-review-profile
  - name: producer_evidence
    value: SOURCE_ASSERTION is preserved; occurrence does not upgrade it.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2243-origin-owner
    - bgc-2243-occurrence-owner
    - bgc-2243-source-mibig_compounds
    - bgc-2243-source-lotus_occurrences
    - bgc-2243-cached-taxonomy
    - bgc-2243-source-routes
    - bgc-2243-review-profile
  - name: locus_evidence
    value: Active BGC0002339 version 3; CLUSTER_UNSTATED, questionable/unknown entry.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2243-origin-owner
    - bgc-2243-occurrence-owner
    - bgc-2243-source-mibig_compounds
    - bgc-2243-source-lotus_occurrences
    - bgc-2243-cached-taxonomy
    - bgc-2243-source-routes
    - bgc-2243-review-profile
- assessment_id: bgc-2243-citations
  area: evidence
  topic: Citations
  outcome: unknown
  summary: PMID:32527018 is the MIBiG ENTRY citation for producer/locus assertions;
    DOI:10.3390/MOLECULES25112676 backs the LOTUS occurrence. Their possible publication
    overlap was not resolved and no independent-experiment count is inferred. NPAtlas
    NPA031448 remains an inherited external cross-reference, not a freshly verified
    identity. No primary article, accession or protein sequence was retrieved under
    the no-request constraint.
  target_ids:
  - naturalproductmech:mibig-b7d597b9df
  evidence_ids:
  - bgc-2243-grounding-owner
  - bgc-2243-origin-owner
  - bgc-2243-occurrence-owner
  - bgc-2243-assay-owner
  - bgc-2243-source-mibig_compounds
  - bgc-2243-source-lotus_occurrences
  - bgc-2243-source-notes
  dimensions:
  - name: citation_scope
    value: ENTRY PMID:32527018 and occurrence DOI:10.3390/MOLECULES25112676 remain
      attributed; independence unverified.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2243-grounding-owner
    - bgc-2243-origin-owner
    - bgc-2243-occurrence-owner
    - bgc-2243-assay-owner
    - bgc-2243-source-mibig_compounds
    - bgc-2243-source-lotus_occurrences
    - bgc-2243-source-notes
- assessment_id: bgc-2243-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: The owner writes one Vitiosangium cumulatum occurrence and no assay observations,
    activity summary, molecular targets or mechanism roots. Exact retained PubChem,
    BindingDB and sibling-corpus queries are empty. These negatives apply to the admitted
    local sources only and do not establish inactivity. The nucleoside-like structural
    motif is not used to infer a molecular target or pharmacology.
  target_ids:
  - naturalproductmech:mibig-b7d597b9df
  evidence_ids:
  - bgc-2243-assay-owner
  - bgc-2243-occurrence-owner
  - bgc-2243-query-lotus_occurrences
  - bgc-2243-source-lotus_occurrences
  - bgc-2243-query-chebi_origins
  - bgc-2243-query-cyanometdb_occurrences
  - bgc-2243-query-pubchem_bioassay
  - bgc-2243-query-bindingdb_targets
  - bgc-2243-query-antibioticmech_inchikeys
  - bgc-2243-source-plan
  - bgc-2243-source-routes
  - bgc-2243-cached-taxonomy
  dimensions:
  - name: occurrence_scope
    value: One written occurrence, not a separate demonstrated producer experiment.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2243-assay-owner
    - bgc-2243-occurrence-owner
    - bgc-2243-query-lotus_occurrences
    - bgc-2243-source-lotus_occurrences
    - bgc-2243-query-chebi_origins
    - bgc-2243-query-cyanometdb_occurrences
    - bgc-2243-query-pubchem_bioassay
    - bgc-2243-query-bindingdb_targets
    - bgc-2243-query-antibioticmech_inchikeys
    - bgc-2243-source-plan
    - bgc-2243-source-routes
    - bgc-2243-cached-taxonomy
  - name: assay_target_scope
    value: No written assays, targets or mechanisms and exact saved activity routes
      empty.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2243-assay-owner
    - bgc-2243-occurrence-owner
    - bgc-2243-query-lotus_occurrences
    - bgc-2243-source-lotus_occurrences
    - bgc-2243-query-chebi_origins
    - bgc-2243-query-cyanometdb_occurrences
    - bgc-2243-query-pubchem_bioassay
    - bgc-2243-query-bindingdb_targets
    - bgc-2243-query-antibioticmech_inchikeys
    - bgc-2243-source-plan
    - bgc-2243-source-routes
    - bgc-2243-cached-taxonomy
- assessment_id: bgc-2243-classification
  area: consistency
  topic: Classification
  outcome: unknown
  summary: 'The versioned NPClassifier output is TERPENOIDS/Diterpenoids with no class
    results and is_glycoside:false. The false prediction should not be read as a statement
    that the structure lacks a sugar moiety: the complete tables show a saturated
    C4O ring, two ring-carbon hydroxyls, a hydroxymethyl substituent and an anomeric
    carbon bonded to purine N. The narrow diagnostic helper searches six-membered
    C5O cycles and therefore cannot detect this five-membered ring. Schema and seeder
    define the field as named/versioned computed output and faithfully copy it; the
    review records an applicability limitation without overwriting the prediction
    or alleging an identity defect.'
  target_ids:
  - naturalproductmech:mibig-b7d597b9df
  evidence_ids:
  - bgc-2243-classification-owner
  - bgc-2243-source-npclassifier
  - bgc-2243-source-mibig_compounds
  - bgc-2243-chemistry
  - bgc-2243-topology
  - bgc-2243-structure-schema
  - bgc-2243-classification-seeder
  - bgc-2243-review-profile
  dimensions:
  - name: classification_applicability
    value: False model glycoside prediction has limited applicability to the observed
      N-ribofuranosyl substructure; computed provenance retained.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2243-classification-owner
    - bgc-2243-source-npclassifier
    - bgc-2243-source-mibig_compounds
    - bgc-2243-chemistry
    - bgc-2243-topology
    - bgc-2243-structure-schema
    - bgc-2243-classification-seeder
    - bgc-2243-review-profile
- assessment_id: bgc-2243-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: The complete owner/history, accepted source context, actual intake and
    both full saved molecular tables were reviewed. No supported local curation defect
    is established in this bounded scope. Five local gates passed; full QC, complete
    OAK and fresh external primary-source/taxonomy/accession verification were unavailable.
    The record remains scientifically partial, and its native curation status/history
    were not changed.
  target_ids:
  - naturalproductmech:mibig-b7d597b9df
  evidence_ids:
  - bgc-2243-owner
  - bgc-2243-capture
  - bgc-2243-intake
  - bgc-2243-intake-acceptance
  - bgc-2243-source-notes
  - bgc-2243-native-acceptance
  - bgc-2243-diagnostic-execution
  - bgc-2243-diagnostic-stderr
  - bgc-2243-diagnostic-acceptance
  - bgc-2243-source-plan
  - bgc-2243-plan-acceptance
  - bgc-2243-review-skill
  - bgc-2243-review-profile
  dimensions:
  - name: review_completion
    value: Partial; qualified local result with external verification, full QC and
      complete OAK unavailable.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2243-owner
    - bgc-2243-capture
    - bgc-2243-intake
    - bgc-2243-intake-acceptance
    - bgc-2243-source-notes
    - bgc-2243-native-acceptance
    - bgc-2243-diagnostic-execution
    - bgc-2243-diagnostic-stderr
    - bgc-2243-diagnostic-acceptance
    - bgc-2243-source-plan
    - bgc-2243-plan-acceptance
    - bgc-2243-review-skill
    - bgc-2243-review-profile
findings: []
actions: []
limitations:
- External identifiers, taxonomy, accessions and primary publications were not refreshed
  under the absolute no-request instruction; historical and database assertions remain
  attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and parsing
  establish their declared mechanical scope only.
- Negative source joins apply only to exact retained predicates and snapshots. Shared
  loci, citations and companions do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source
  records, raw snapshots, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete source payloads and personal/delegated direct-context whole-reading attribution
  are retained in the pinned source notes. Assigned actual intakes, complete selected
  owners/history and every paired saved molecular table were personally read.
- Two original batch-level undefined-stereo warnings remain globally unassigned. True
  comparison flags and a complete correspondence do not override full_graph_identity_established:false.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-225
```
