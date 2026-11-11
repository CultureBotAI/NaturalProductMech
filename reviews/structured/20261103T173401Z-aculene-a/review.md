# Local evidence review: aculene A

- Review: 20261103T173401Z-aculene-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T17:10:56.586492Z
- Finished UTC: 2026-11-03T17:34:01.027468Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Aculene A is locally consistent with its full-key ChEBI/MIBiG grounding and proline-ester definition. Three specified centres and the retained source grades remain distinct from fresh natural-identity or pathway verification. Scientific completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2261; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156057 | data/natural_products/terpenoids/aculene-a.yaml | generated | aculene A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:156057 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:156057 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:156057 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:156057 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:156057 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:156057 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:156057 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:156057 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: CHEBI:156057.

The retained EXACT grounding CHEBI:156057 joins MIBiG BGC0002225 version 3 compound index 1 and the three-star ChEBI row by the complete key LOOAMPJDSIVZQC-IEZWGBDMSA-N. The definition describes formal esterification of aculene C with L-proline; the saved topology has the corresponding alcohol-derived O–C(=O)–pyrrolidine connection and an S proline alpha carbon. This supports local definition/structure consistency, not a claim that the esterification was experimentally demonstrated. Five direct BGC companions retain different complete keys.

### Representation

representation: supported. Targets: CHEBI:156057.

Both stored forms give neutral C19H25NO3 with 23 atoms, 25 bonds, one fragment and three specified tetrahedral centres. In the SMILES table C6 is R, C12 is S and C16 is S; the corresponding InChI atoms 18, 16 and 14 retain those assignments. The five- and seven-membered fused carbon rings coexist with a separate pyrrolidine ring. All ten comparison flags and the complete stored chirality-aware correspondence agree. The diagnostic explicitly leaves independent full-graph and natural identity unestablished.

### Origin

provenance: supported. Targets: CHEBI:156057.

MIBiG BGC0002225 version 3 is active, of questionable quality and unknown completeness. Aspergillus aculeatus ATCC 16872, NCBITaxon:690307, is graded BGC_CHARACTERIZED, while the locus is separately CLUSTER_DEMONSTRATED from heterologous expression and knock-out studies. The retained interval is genbank:KV878977.1, 1125505–1144430. The species-level occurrence taxon 5053 is distinct from the producing-strain assertion. Complete cached stanzas preserve these labels; they are not a fresh taxonomy or genome verification.

### Citations

evidence: supported. Targets: CHEBI:156057.

The MIBiG producer and locus citations both retain ENTRY-level PMID:31618514. The LOTUS occurrence cites DOI:10.3390/MOLECULES190810898 and the ChEBI origin cites PMID:25068785 with cell-suspension-culture text. These are retained source assertions with distinct claim roles; different citation identifiers do not establish independent experiments. The definition is attributed to CHEBI:156057. The historical AneA annotations on direct C/D companions do not become an A-specific enzyme assay.

### Bioactivity

evidence: supported. Targets: CHEBI:156057.

The owner writes two occurrences for Aspergillus aculeatus taxon 5053, one from LOTUS and one from ChEBI. They are occurrence assertions rather than two proven producer experiments. No bioactivities, molecular targets or mechanism roots are written in this owner. Its exact saved PubChem, BindingDB and AntibioticMech joins are empty, as is the CyanometDB occurrence join. This is bounded absence in the retained snapshot, not proof of biological inactivity or absence of a pathway.

### Classification

consistency: supported. Targets: CHEBI:156057.

The retained source BGC class is TERPENE. NPClassifier version npclassifier.gnps2.org@2026-09-07 supplies Terpenoids / Sesquiterpenoids / Daucane sesquiterpenoids and is_glycoside:false. The saved fused carbocyclic core, ketone and proline ester support a local structural interpretation compatible with that broad filing; no sugar residue or glycosidic linkage is established. The amino-acid-derived ester does not by itself establish a peptide biosynthetic class. The model and BGC labels remain distinct from direct biosynthetic evidence.

### Completion

completeness: supported. Targets: CHEBI:156057.

Partial scientific review from complete local source and saved molecular evidence; five local gates passed, full QC/OAK and fresh external verification unavailable.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2261-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/aculene-a.yaml; Whole owner plaintext and complete curation_history | supports | Complete current owner and its 2 ordered history events, personally read. Native curation_status remains SEEDED. |
| bgc-2261-capture | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/0/owner_pin; /records/0/owner_document | supports | Exact captured owner, including all written nonmechanistic fields, roots and history. |
| bgc-2261-intake | /private/tmp/npm-review-work/shared-next-batch227/intakes/2261-inspect-001.json; /source; /targets | supports | Actual one-record canonical inspection with 42 source inputs and target CHEBI:156057; current owner and context roles are retained. |
| bgc-2261-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch227/root-intake-ready-001.json; /accepted; /intake_summary; /verification | supports | ROOT accepts all ten original canonical intakes, their exact target/source maps and current dependency pins. |
| bgc-2261-grounding-owner | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/label; /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status; /records/0/owner_document/definition; /records/0/owner_document/definition_source | supports | Written identity/structure/grounding fields and definition when present: {"chemical_structure": {"smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C", "standard_inchi": "InChI=1S/C19H25NO3/c1-4-13-11-16(21)19(3)14(13)8-7-12(2)10-17(19)23-18(22)15-6-5-9-20-15/h7-8,11,15,17,20H,4-6,9-10H2,1-3H3/t15-,17-,19-/m0/s1", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002225"}, "definition": "A carboxylic ester resulting from the formal condensation of the hydroxy group of aculene C with the carboxylic acid group of L-proline. It is a sesquiterpenoid isolated from the fungus Aspergillus aculeatus.", "definition_source": "CHEBI:156057", "grounding_status": "EXACT", "identifier": "CHEBI:156057", "label": "aculene A", "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-0981bd201c", "source": "MIBIG", "source_id": "BGC0002225", "source_label": "aculene A", "source_version": "3"}, {"minted_identifier": "naturalproductmech:chebi-d3a95578c6", "source": "CHEBI", "source_id": "CHEBI:156057", "source_label": "aculene A", "source_version": "3-star"}]} |
| bgc-2261-origin-owner | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/producer_taxon_groups; /records/0/owner_document/bgc_class | supports | Written producer and locus fields, including source versions, methods, citation roles and taxon groups: {"bgc_class": ["TERPENE"], "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002225", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002225 entry version 3; citation taken from the entry level", "reference": "PMID:31618514"}], "genome_accession": "genbank:KV878977.1", "link_evidence_basis": "CLUSTER_DEMONSTRATED", "locus_evidence_methods": ["Heterologous expression", "Knock-out studies"], "locus_from": 1125505, "locus_to": 1144430, "organism_label": "Aspergillus aculeatus ATCC 16872", "organism_taxon_id": "NCBITaxon:690307"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0002225", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002225 entry version 3; citation taken from the entry level", "reference": "PMID:31618514"}], "evidence_basis": "BGC_CHARACTERIZED", "notes": "Locus evidence: Heterologous expression&#124;Knock-out studies. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC 16872"}], "producer_taxon_groups": ["FUNGAL"]} |
| bgc-2261-assay-owner | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/0/owner_document | supports | The complete captured owner has no bioactivities or molecular_targets root. It has no causal_graphs, causal_graph_refs or biosynthetic_pathway root. |
| bgc-2261-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/0/owner_document/occurrences; /records/0/owner_document/occurrence_taxon_groups | supports | All written occurrences and occurrence groups: {"occurrence_taxon_groups": ["FUNGAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.3390/MOLECULES190810898"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q4807886", "source": "LOTUS", "taxon_id": "NCBITaxon:5053", "taxon_label": "Aspergillus aculeatus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "ChEBI compound origin for CHEBI:156057", "reference": "PMID:25068785"}], "notes": "cell suspension culture", "source": "CHEBI", "taxon_id": "NCBITaxon:5053", "taxon_label": "Aspergillus aculeatus", "taxon_source": "NCBITaxon"}]} |
| bgc-2261-classification-owner | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/0/owner_document/np_pathway; /records/0/owner_document/np_classification; /records/0/owner_document/bgc_class | supports | Literal written model/version/results and separate source BGC classification: {"bgc_class": ["TERPENE"], "np_classification": {"class_results": ["Daucane sesquiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Sesquiterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS"} |
| bgc-2261-chemistry | /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/smiles/status; /records/0/inchi/status; /records/0/smiles/computed; /records/0/inchi/computed; /records/0/comparisons; /records/0/atom_correspondence | supports | Both saved forms parsed. They give C19H25NO3, charge 0, 23 atoms and 25 bonds each. All ten comparison flags are true; a complete stored chirality-aware correspondence is retained, with full_graph_identity_established:false. Stereo counts: {"Atom_Tetrahedral:Specified": 3}. |
| bgc-2261-topology | /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-DATA-001.json; /records/0/smiles/computed; /records/0/inchi/computed; /records/0/atom_correspondence | supports | SMILES C4(=O5) is the core ketone; C12–O13–C14(=O15)–C16 is the ester connection. C16–C17–C18–C19–N20 is the proline ring, with C16 S. No C5O candidate ring is returned, and complete atom/bond inspection shows no sugar linkage. |
| bgc-2261-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr; /external_requests | supports | The original ROOT-owned diagnostic execution returned zero and retained its command and exact stdout/stderr pins; stderr is empty and no external request is reported. |
| bgc-2261-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch227/root-local-diagnostics-acceptance-001.json; /accepted; /DATA; /execution; /verification; /limits | supports | ROOT accepts the original saved 20-form diagnostic and current inputs; its mechanical comparison and preservation checks do not establish fresh natural identity. |
| bgc-2261-native-acceptance | /private/tmp/npm-review-work/shared-next-batch227/root-native-five-gates-acceptance-001.json; /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable; /verification | supports | Five original local commands passed. all_native_gates_passed remains false, with full QC and OAK unavailable. Queue and reproduction checks have their recorded mechanical scope. |
| bgc-2261-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch227-tentative/root-source-inventory-acceptance-001.json; /accepted; /inventory | supports | ROOT accepts this exact saved inventory. Source-payload interpretation is separately attributed in the source notes. |
| bgc-2261-source-plan | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-target-input-plan-001.json; /records/0; /source_placement_count; /unique_source_path_count | supports | Accepted source plan retains this record and its exact input projection, within the batch totals of 418 placements and 53 paths. |
| bgc-2261-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch227/root-input-plan-acceptance-001.json; /accepted; /input_plan; /notes; /verification | supports | ROOT accepts the actual composed source plan and pinned source-reading notes with exact source/current input joins. |
| bgc-2261-source-notes | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-scope-notes-001.json; /reading; /curation; /cautions; /inventory_ROOT_acceptance | supports | Complete source-reading attribution: BGC contexts 0–6, 63 frames and 38 positive rows; Support contexts 7–11, 45 frames and 138 rows. All 15 cached stanzas are assigned. The bounded ignored-inclusive eight-table, 44-literal curation scan found no matching rows; this is limited to its declared exact-token scope. |
| bgc-2261-direct-contexts | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /records/0/direct_companion_predicates; /contexts/3/identifier; /contexts/3/standard_inchi_key; /contexts/3/owned_bgc_ids; /contexts/3/declared_mechanism_roots_literal; /contexts/4/identifier; /contexts/4/standard_inchi_key; /contexts/4/owned_bgc_ids; /contexts/4/declared_mechanism_roots_literal; /contexts/5/identifier; /contexts/5/standard_inchi_key; /contexts/5/owned_bgc_ids; /contexts/5/declared_mechanism_roots_literal; /contexts/10/identifier; /contexts/10/standard_inchi_key; /contexts/10/owned_bgc_ids; /contexts/10/declared_mechanism_roots_literal; /contexts/11/identifier; /contexts/11/standard_inchi_key; /contexts/11/owned_bgc_ids; /contexts/11/declared_mechanism_roots_literal | supports | Exact one-hop predicate and owner profiles; these do not transfer identity, activity or mechanism: [{"declared_mechanism_roots_literal": [], "identifier": "CHEBI:156056", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-b.yaml", "standard_inchi_key": "DLPUOZGNMZKXKB-YEWFCNIMSA-N"}, {"declared_mechanism_roots_literal": ["causal_graphs", "biosynthetic_pathway"], "identifier": "CHEBI:155912", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-c.yaml", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"}, {"declared_mechanism_roots_literal": ["causal_graphs", "biosynthetic_pathway"], "identifier": "CHEBI:155910", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-d.yaml", "standard_inchi_key": "IIQOUDJDCRTCJY-MBNYWOFBSA-N"}, {"declared_mechanism_roots_literal": [], "identifier": "naturalproductmech:mibig-0e7dc695d0", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/asperaculane-a.yaml", "standard_inchi_key": "JDBMOJWYGWGAIH-DZBCAUDPSA-N"}, {"declared_mechanism_roots_literal": [], "identifier": "naturalproductmech:mibig-d4c2d69c3b", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/asperaculane-b.yaml", "standard_inchi_key": "GFYHPKUYDFUKNL-MBNYWOFBSA-N"}] |
| bgc-2261-companion-3 | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/3/input; /contexts/3/complete_raw_text; /contexts/3/complete_raw_history | supports | Complete direct companion plaintext and history, retained as separate owner CHEBI:156056 with full key DLPUOZGNMZKXKB-YEWFCNIMSA-N. Source reading is attributed in the source notes; no congener claim transfer. |
| bgc-2261-companion-4 | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/input; /contexts/4/complete_raw_text; /contexts/4/complete_raw_history | supports | Complete direct companion plaintext and history, retained as separate owner CHEBI:155912 with full key UCCFSWQSMDQYHO-GXTWGEPZSA-N. Source reading is attributed in the source notes; no congener claim transfer. |
| bgc-2261-companion-5 | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/5/input; /contexts/5/complete_raw_text; /contexts/5/complete_raw_history | supports | Complete direct companion plaintext and history, retained as separate owner CHEBI:155910 with full key IIQOUDJDCRTCJY-MBNYWOFBSA-N. Source reading is attributed in the source notes; no congener claim transfer. |
| bgc-2261-companion-10 | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/10/input; /contexts/10/complete_raw_text; /contexts/10/complete_raw_history | supports | Complete direct companion plaintext and history, retained as separate owner naturalproductmech:mibig-0e7dc695d0 with full key JDBMOJWYGWGAIH-DZBCAUDPSA-N. Source reading is attributed in the source notes; no congener claim transfer. |
| bgc-2261-companion-11 | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/11/input; /contexts/11/complete_raw_text; /contexts/11/complete_raw_history | supports | Complete direct companion plaintext and history, retained as separate owner naturalproductmech:mibig-d4c2d69c3b with full key GFYHPKUYDFUKNL-MBNYWOFBSA-N. Source reading is attributed in the source notes; no congener claim transfer. |
| bgc-2261-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/11 | supports | Complete retained OBO stanzas for source taxa; no fresh taxonomy or ancestry inference: [{"complete_stanza": "[Term]\nid: NCBITaxon:5053\nname: Aspergillus aculeatus\nsynonym: \"Aspergillus japonicus var. aculeatus\" EXACT []\n\n", "id": "NCBITaxon:5053", "physical_line": 7851}, {"complete_stanza": "[Term]\nid: NCBITaxon:690307\nname: Aspergillus aculeatus ATCC 16872\n\n", "id": "NCBITaxon:690307", "physical_line": 107651}] |
| bgc-2261-source-routes | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/source_taxa; /contexts/2/source_scope_inventory/forward_taxon_merge_matches; /contexts/2/source_scope_inventory/nonorganism_matches; /contexts/2/source_scope_inventory/actual_assay_rows; /contexts/2/source_scope_inventory/blank_AID_sentinels; /contexts/2/source_scope_inventory/related_corpus_rows | supports | Exact retained route sets, distinguishing nonempty source taxa from empty forward/nonorganism matches and blank sentinels from actual assays: {"actual_assay_rows": [], "blank_AID_sentinels": [], "forward_taxon_merge_matches": [], "nonorganism_matches": [], "related_corpus_rows": [], "source_taxa": ["NCBITaxon:5053", "NCBITaxon:690307"]} |
| bgc-2261-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/mibig_compounds | supports | Complete saved exact query frame with predicate, query and all 1 positive placements. {"matches": [{"last_physical_line": 2647, "physical_line": 2647, "raw_tsv_record": "BGC0002225\t3\tactive\tquestionable\tunknown\taculene A\t1\tCCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C\tInChI=1S/C19H25NO3/c1-4-13-11-16(21)19(3)14(13)8-7-12(2)10-17(19)23-18(22)15-6-5-9-20-15/h7-8,11,15,17,20H,4-6,9-10H2,1-3H3/t15-,17-,19-/m0/s1\tLOOAMPJDSIVZQC-IEZWGBDMSA-N\ttrue\t\tnpatlas:NPA007875\tNCBITaxon:690307\tAspergillus aculeatus ATCC 16872\tterpene\tUnknown\tKV878977.1\t1125505\t1144430\tHeterologous expression&#124;Knock-out studies\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tPMID:31618514\tENTRY\n", "row": {"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis": "CLUSTER_DEMONSTRATED", "compound_classes": "", "compound_index": "1", "compound_name": "aculene A", "database_ids": "npatlas:NPA007875", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "KV878977.1", "locus_evidence_methods": "Heterologous expression&#124;Knock-out studies", "locus_from": "1125505", "locus_to": "1144430", "mibig_accession": "BGC0002225", "primary_reference": "PMID:31618514", "producer_evidence_basis": "BGC_CHARACTERIZED", "reference_basis": "ENTRY", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C", "standard_inchi": "InChI=1S/C19H25NO3/c1-4-13-11-16(21)19(3)14(13)8-7-12(2)10-17(19)23-18(22)15-6-5-9-20-15/h7-8,11,15,17,20H,4-6,9-10H2,1-3H3/t15-,17-,19-/m0/s1", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC 16872"}, "row_sha256": "6ddf8f2e64a3fec2c3a60c5f9c2f093ab8bc5ba1a654f3356dc234919455ca59"}], "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"} |
| bgc-2261-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2647–2647; row_sha256 6ddf8f2e64a3fec2c3a60c5f9c2f093ab8bc5ba1a654f3356dc234919455ca59 | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis": "CLUSTER_DEMONSTRATED", "compound_classes": "", "compound_index": "1", "compound_name": "aculene A", "database_ids": "npatlas:NPA007875", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "KV878977.1", "locus_evidence_methods": "Heterologous expression&#124;Knock-out studies", "locus_from": "1125505", "locus_to": "1144430", "mibig_accession": "BGC0002225", "primary_reference": "PMID:31618514", "producer_evidence_basis": "BGC_CHARACTERIZED", "reference_basis": "ENTRY", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C", "standard_inchi": "InChI=1S/C19H25NO3/c1-4-13-11-16(21)19(3)14(13)8-7-12(2)10-17(19)23-18(22)15-6-5-9-20-15/h7-8,11,15,17,20H,4-6,9-10H2,1-3H3/t15-,17-,19-/m0/s1", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC 16872"}] |
| bgc-2261-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/chebi_structures | supports | Complete saved exact query frame with predicate, query and all 1 positive placements. {"matches": [{"last_physical_line": 42974, "physical_line": 42974, "raw_tsv_record": "CHEBI:156057\taculene A\tA carboxylic ester resulting from the formal condensation of the hydroxy group of aculene C with the carboxylic acid group of L-proline. It is a sesquiterpenoid isolated from the fungus Aspergillus aculeatus.\t3\tLOOAMPJDSIVZQC-IEZWGBDMSA-N\tCCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2OC(=O)[C@@H]1CCCN1\n", "row": {"chebi_id": "CHEBI:156057", "definition": "A carboxylic ester resulting from the formal condensation of the hydroxy group of aculene C with the carboxylic acid group of L-proline. It is a sesquiterpenoid isolated from the fungus Aspergillus aculeatus.", "name": "aculene A", "smiles": "CCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2OC(=O)[C@@H]1CCCN1", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "stars": "3"}, "row_sha256": "c7b4cc92c659d4aa084e5ff4e8ee7ff6a432f7708a6d864db4520e856d176cd0"}], "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"} |
| bgc-2261-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line 1; physical lines 42974–42974; row_sha256 c7b4cc92c659d4aa084e5ff4e8ee7ff6a432f7708a6d864db4520e856d176cd0 | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"chebi_id": "CHEBI:156057", "definition": "A carboxylic ester resulting from the formal condensation of the hydroxy group of aculene C with the carboxylic acid group of L-proline. It is a sesquiterpenoid isolated from the fungus Aspergillus aculeatus.", "name": "aculene A", "smiles": "CCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2OC(=O)[C@@H]1CCCN1", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "stars": "3"}] |
| bgc-2261-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved exact query frame with predicate, query and all 1 positive placements. {"matches": [{"last_physical_line": 4236, "physical_line": 4236, "raw_tsv_record": "LOOAMPJDSIVZQC-IEZWGBDMSA-N\tAspergillus aculeatus\tNCBITaxon:5053\thttp://www.wikidata.org/entity/Q4807886\t10.3390/MOLECULES190810898\thttp://www.wikidata.org/entity/Q77419757\n", "row": {"organism_name": "Aspergillus aculeatus", "organism_wikidata": "http://www.wikidata.org/entity/Q4807886", "reference_doi": "10.3390/MOLECULES190810898", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q77419757", "taxon_id": "NCBITaxon:5053"}, "row_sha256": "8247d07b1c0a369b96c97f54055d2a8eff305322e55fa4038df67319f58ae9a8"}], "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"} |
| bgc-2261-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 4236–4236; row_sha256 8247d07b1c0a369b96c97f54055d2a8eff305322e55fa4038df67319f58ae9a8 | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"organism_name": "Aspergillus aculeatus", "organism_wikidata": "http://www.wikidata.org/entity/Q4807886", "reference_doi": "10.3390/MOLECULES190810898", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q77419757", "taxon_id": "NCBITaxon:5053"}] |
| bgc-2261-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved exact query frame with predicate, query and all 0 positive placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"} |
| bgc-2261-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/npclassifier | supports | Complete saved exact query frame with predicate, query and all 1 positive placements. {"matches": [{"last_physical_line": 1389, "physical_line": 1389, "raw_tsv_record": "LOOAMPJDSIVZQC-IEZWGBDMSA-N\tCCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C\tTerpenoids\tSesquiterpenoids\tDaucane sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results": "Daucane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "superclass_results": "Sesquiterpenoids"}, "row_sha256": "112ea9533d8310a62e032f97cf08e6806fd23dcad50b660633670a014f1fa20c"}], "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"} |
| bgc-2261-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 1389–1389; row_sha256 112ea9533d8310a62e032f97cf08e6806fd23dcad50b660633670a014f1fa20c | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"class_results": "Daucane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "superclass_results": "Sesquiterpenoids"}] |
| bgc-2261-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved exact query frame with predicate, query and all 0 positive placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"} |
| bgc-2261-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved exact query frame with predicate, query and all 0 positive placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"} |
| bgc-2261-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved exact query frame with predicate, query and all 0 positive placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"} |
| bgc-2261-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/chebi_origins | supports | Complete saved exact query frame with predicate, query and all 1 positive placements. {"matches": [{"last_physical_line": 16917, "physical_line": 16917, "raw_tsv_record": "CHEBI:156057\tAspergillus aculeatus\t5053\tcell suspension culture\t\t25068785\t\n", "row": {"chebi_id": "CHEBI:156057", "comments": "", "component_text": "cell suspension culture", "source_accession": "25068785", "species_accession": "5053", "species_text": "Aspergillus aculeatus", "strain_text": ""}, "row_sha256": "1f5b03c1406915f5ec2a906679e575ceed7d4688200f218d8b347c5701d146f8"}], "predicate": "exact chebi_id from exact full-key structure rows", "query": ["CHEBI:156057"]} |
| bgc-2261-source-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Header line 1; physical lines 16917–16917; row_sha256 1f5b03c1406915f5ec2a906679e575ceed7d4688200f218d8b347c5701d146f8 | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"chebi_id": "CHEBI:156057", "comments": "", "component_text": "cell suspension culture", "source_accession": "25068785", "species_accession": "5053", "species_text": "Aspergillus aculeatus", "strain_text": ""}] |
| bgc-2261-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure distinguishes normalized identity and unspecified stereochemistry. ComputedClassification is explicitly a named/versioned prediction, never a source assertion or record-admission reason. |
| bgc-2261-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | The maintained extractor derives the stereo_complete flag from unassigned chiral centres; no new extractor call occurred in this review. |
| bgc-2261-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 971–1037 | supports | The seeder retains the exact structure/definition source and copies named NPClassifier results including is_glycoside. A prediction is not promoted to experimental evidence. |
| bgc-2261-origin-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 1093–1151 | supports | Producer evidence and locus methods/link grades remain separately copied; merges and applicable local qualifications have distinct handling. |
| bgc-2261-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole profile | supports | Current review profile requires one-record identity, evidence, provenance, representation and completion dimensions without promoting unavailable verification. |
| bgc-2261-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole review skill | supports | Current one-record review scope distinguishes local evidence review from scientific completeness, preserves source records, and requires concrete supported findings. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-227/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-227/native-current227-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-227/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-227/native-current227-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-227/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-227/native-current227-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-227/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-227/native-current227-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-227/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-227/native-current227-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External identifiers, taxonomy, genome accessions and primary publications were not refreshed under the absolute no-request instruction. Historical and database assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and stored-form parsing establish only their declared mechanical scope.
- Empty joins refer only to the retained exact predicates and snapshots; they do not establish biological absence. Shared loci, citations and congeners do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source records, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- The complete owner/history, actual intake, exact retained query/source payloads and both full paired molecular tables were personally read. Complementary companion/cached-source reading is explicitly attributed in the pinned notes.
- The original batch diagnostic stderr is empty. All true comparison flags leave full_graph_identity_established:false unchanged.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T173401Z-aculene-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: aculene A'
started_at: '2026-11-03T17:10:56.586492Z'
finished_at: '2026-11-03T17:34:01.027468Z'
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
summary: Aculene A is locally consistent with its full-key ChEBI/MIBiG grounding and
  proline-ester definition. Three specified centres and the retained source grades
  remain distinct from fresh natural-identity or pathway verification. Scientific
  completion is partial.
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
  - path: data/natural_products/terpenoids/aculene-a.yaml
    sha256: 88c7a924ba918b8f1594f44f9149e9b1c0dd1e34f30251fbafd76e2d94036294
    role: target
  - path: data/natural_products/terpenoids/aculene-b.yaml
    sha256: 2f85a5ba0c8c4e73048d53e7189562ad9ec6274c328a3d54e6d714cb13b2cbf1
    role: context
  - path: data/natural_products/terpenoids/aculene-c.yaml
    sha256: 97baa4b9ddc30459f9513d453485eeb4fff412afe057e658192e0ba54ef62653
    role: context
  - path: data/natural_products/terpenoids/aculene-d.yaml
    sha256: 7313cad7683490867e552f13dd4c3b280667701a3253b08a4e4cff46aac1c2cf
    role: context
  - path: data/natural_products/terpenoids/asperaculane-a.yaml
    sha256: 2a33ce8f708d4220914b239cf104e3ddd8780af009eac2c09e2790b28f21bc5d
    role: context
  - path: data/natural_products/terpenoids/asperaculane-b.yaml
    sha256: 1afdd7bfd9a2c791051e40488ca5d755b3b2d57948cb7d23388560323a80277c
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
  selection: Campaign path order 2261; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156057
targets:
- target_id: CHEBI:156057
  path: data/natural_products/terpenoids/aculene-a.yaml
  label: aculene A
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
  - CHEBI:156057
  command: just validate-strict data/natural_products/terpenoids/aculene-a.yaml data/natural_products/terpenoids/aculene-b.yaml
    data/natural_products/terpenoids/aculene-c.yaml data/natural_products/terpenoids/aculene-d.yaml
    data/natural_products/terpenoids/aculin-a.yaml data/natural_products/terpenoids/albaflavenone.yaml
    data/natural_products/terpenoids/aphidicolan-16-ol.yaml data/natural_products/terpenoids/aphidicolin.yaml
    data/natural_products/terpenoids/asperaculane-a.yaml data/natural_products/terpenoids/asperaculane-b.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-227/validate-strict-selected10-001.tsv
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
  - CHEBI:156057
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-227/validate-all-001.tsv
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
  - CHEBI:156057
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
  - CHEBI:156057
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
  - CHEBI:156057
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-227/review-queue-001.tsv
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
  - CHEBI:156057
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:156057
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:156057
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2261-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/aculene-a.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete current owner and its 2 ordered history events, personally read.
    Native curation_status remains SEEDED.
  snapshot_sha256: 88c7a924ba918b8f1594f44f9149e9b1c0dd1e34f30251fbafd76e2d94036294
- evidence_id: bgc-2261-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/0/owner_pin; /records/0/owner_document
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Exact captured owner, including all written nonmechanistic fields, roots
    and history.
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2261-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/intakes/2261-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Actual one-record canonical inspection with 42 source inputs and target
    CHEBI:156057; current owner and context roles are retained.
  snapshot_sha256: 9e3a972f54a3a19c803da5f60f30c96e291ae6ff73355fb17b703dff298302b6
- evidence_id: bgc-2261-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/root-intake-ready-001.json
  locator: /accepted; /intake_summary; /verification
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ROOT accepts all ten original canonical intakes, their exact target/source
    maps and current dependency pins.
  snapshot_sha256: 8a1dce2c5b8f17939c216983455dbc1ebad823ae10e6bd9cce0c093a142af697
- evidence_id: bgc-2261-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/label;
    /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts;
    /records/0/owner_document/grounding_status; /records/0/owner_document/definition;
    /records/0/owner_document/definition_source
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Written identity/structure/grounding fields and definition when present:
    {"chemical_structure": {"smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C",
    "standard_inchi": "InChI=1S/C19H25NO3/c1-4-13-11-16(21)19(3)14(13)8-7-12(2)10-17(19)23-18(22)15-6-5-9-20-15/h7-8,11,15,17,20H,4-6,9-10H2,1-3H3/t15-,17-,19-/m0/s1",
    "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002225"}, "definition":
    "A carboxylic ester resulting from the formal condensation of the hydroxy group
    of aculene C with the carboxylic acid group of L-proline. It is a sesquiterpenoid
    isolated from the fungus Aspergillus aculeatus.", "definition_source": "CHEBI:156057",
    "grounding_status": "EXACT", "identifier": "CHEBI:156057", "label": "aculene A",
    "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-0981bd201c",
    "source": "MIBIG", "source_id": "BGC0002225", "source_label": "aculene A", "source_version":
    "3"}, {"minted_identifier": "naturalproductmech:chebi-d3a95578c6", "source": "CHEBI",
    "source_id": "CHEBI:156057", "source_label": "aculene A", "source_version": "3-star"}]}'
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2261-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters;
    /records/0/owner_document/producer_taxon_groups; /records/0/owner_document/bgc_class
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Written producer and locus fields, including source versions, methods,
    citation roles and taxon groups: {"bgc_class": ["TERPENE"], "biosynthetic_gene_clusters":
    [{"accession": "mibig:BGC0002225", "bgc_class": ["TERPENE"], "entry_status": "active",
    "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0002225 entry version 3; citation taken from the entry level", "reference":
    "PMID:31618514"}], "genome_accession": "genbank:KV878977.1", "link_evidence_basis":
    "CLUSTER_DEMONSTRATED", "locus_evidence_methods": ["Heterologous expression",
    "Knock-out studies"], "locus_from": 1125505, "locus_to": 1144430, "organism_label":
    "Aspergillus aculeatus ATCC 16872", "organism_taxon_id": "NCBITaxon:690307"}],
    "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0002225", "evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002225 entry version
    3; citation taken from the entry level", "reference": "PMID:31618514"}], "evidence_basis":
    "BGC_CHARACTERIZED", "notes": "Locus evidence: Heterologous expression|Knock-out
    studies. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED; this field grades
    the taxon claim, which is a different question.", "source": "MIBIG", "source_version":
    "3", "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC
    16872"}], "producer_taxon_groups": ["FUNGAL"]}'
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2261-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: The complete captured owner has no bioactivities or molecular_targets root.
    It has no causal_graphs, causal_graph_refs or biosynthetic_pathway root.
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2261-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/0/owner_document/occurrences; /records/0/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'All written occurrences and occurrence groups: {"occurrence_taxon_groups":
    ["FUNGAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.3390/MOLECULES190810898"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q4807886",
    "source": "LOTUS", "taxon_id": "NCBITaxon:5053", "taxon_label": "Aspergillus aculeatus",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "ChEBI compound origin for CHEBI:156057", "reference": "PMID:25068785"}],
    "notes": "cell suspension culture", "source": "CHEBI", "taxon_id": "NCBITaxon:5053",
    "taxon_label": "Aspergillus aculeatus", "taxon_source": "NCBITaxon"}]}'
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2261-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_pathway; /records/0/owner_document/np_classification;
    /records/0/owner_document/bgc_class
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Literal written model/version/results and separate source BGC classification:
    {"bgc_class": ["TERPENE"], "np_classification": {"class_results": ["Daucane sesquiterpenoids"],
    "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results":
    ["Sesquiterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS"}'
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2261-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/smiles/status; /records/0/inchi/status;
    /records/0/smiles/computed; /records/0/inchi/computed; /records/0/comparisons;
    /records/0/atom_correspondence
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Both saved forms parsed. They give C19H25NO3, charge 0, 23 atoms and 25
    bonds each. All ten comparison flags are true; a complete stored chirality-aware
    correspondence is retained, with full_graph_identity_established:false. Stereo
    counts: {"Atom_Tetrahedral:Specified": 3}.'
  snapshot_sha256: 310fb39c1a9fad6c657cd7aa0986819b02834117d6db86c6b88fd2ddc774a9f2
- evidence_id: bgc-2261-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/smiles/computed; /records/0/inchi/computed; /records/0/atom_correspondence
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: SMILES C4(=O5) is the core ketone; C12–O13–C14(=O15)–C16 is the ester connection.
    C16–C17–C18–C19–N20 is the proline ring, with C16 S. No C5O candidate ring is
    returned, and complete atom/bond inspection shows no sugar linkage.
  snapshot_sha256: 310fb39c1a9fad6c657cd7aa0986819b02834117d6db86c6b88fd2ddc774a9f2
- evidence_id: bgc-2261-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /external_requests
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: The original ROOT-owned diagnostic execution returned zero and retained
    its command and exact stdout/stderr pins; stderr is empty and no external request
    is reported.
  snapshot_sha256: cd7c3ddbf99f1e149846db81d2e8927177241049dc9316408da347ef0b73d8c6
- evidence_id: bgc-2261-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/root-local-diagnostics-acceptance-001.json
  locator: /accepted; /DATA; /execution; /verification; /limits
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ROOT accepts the original saved 20-form diagnostic and current inputs;
    its mechanical comparison and preservation checks do not establish fresh natural
    identity.
  snapshot_sha256: 14967c4d38b8f806e2c49ea51068afd81aa23e83df4ac04f451efd2729cbba96
- evidence_id: bgc-2261-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/root-native-five-gates-acceptance-001.json
  locator: /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable;
    /verification
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Five original local commands passed. all_native_gates_passed remains false,
    with full QC and OAK unavailable. Queue and reproduction checks have their recorded
    mechanical scope.
  snapshot_sha256: cb9726f77bbd42dd0c0f0a205c3a6b2ab9e79d41c1d386a92117ce95e15b33e1
- evidence_id: bgc-2261-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/root-source-inventory-acceptance-001.json
  locator: /accepted; /inventory
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ROOT accepts this exact saved inventory. Source-payload interpretation
    is separately attributed in the source notes.
  snapshot_sha256: eb38369e8b3d32ba55eaa5ceedfe21446cc123c911691cab66901e7e2bf1f99a
- evidence_id: bgc-2261-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-target-input-plan-001.json
  locator: /records/0; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Accepted source plan retains this record and its exact input projection,
    within the batch totals of 418 placements and 53 paths.
  snapshot_sha256: 5537c37fdf8a54893bcbd0c967e1d857f8ac7004044a38e11d9ce2174146ba11
- evidence_id: bgc-2261-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/root-input-plan-acceptance-001.json
  locator: /accepted; /input_plan; /notes; /verification
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ROOT accepts the actual composed source plan and pinned source-reading
    notes with exact source/current input joins.
  snapshot_sha256: eca63a2e032e35c9bb8f233056b0bc6257aad535a61d7fdc9b33db1aa7f1b302
- evidence_id: bgc-2261-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-scope-notes-001.json
  locator: /reading; /curation; /cautions; /inventory_ROOT_acceptance
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete source-reading attribution: BGC contexts 0–6, 63 frames and 38
    positive rows; Support contexts 7–11, 45 frames and 138 rows. All 15 cached stanzas
    are assigned. The bounded ignored-inclusive eight-table, 44-literal curation scan
    found no matching rows; this is limited to its declared exact-token scope.'
  snapshot_sha256: 08d4d93cb884f9de019060f9073cf0078f34762b7f0e197c80633692a65b08b0
- evidence_id: bgc-2261-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /records/0/direct_companion_predicates; /contexts/3/identifier; /contexts/3/standard_inchi_key;
    /contexts/3/owned_bgc_ids; /contexts/3/declared_mechanism_roots_literal; /contexts/4/identifier;
    /contexts/4/standard_inchi_key; /contexts/4/owned_bgc_ids; /contexts/4/declared_mechanism_roots_literal;
    /contexts/5/identifier; /contexts/5/standard_inchi_key; /contexts/5/owned_bgc_ids;
    /contexts/5/declared_mechanism_roots_literal; /contexts/10/identifier; /contexts/10/standard_inchi_key;
    /contexts/10/owned_bgc_ids; /contexts/10/declared_mechanism_roots_literal; /contexts/11/identifier;
    /contexts/11/standard_inchi_key; /contexts/11/owned_bgc_ids; /contexts/11/declared_mechanism_roots_literal
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Exact one-hop predicate and owner profiles; these do not transfer identity,
    activity or mechanism: [{"declared_mechanism_roots_literal": [], "identifier":
    "CHEBI:156056", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-b.yaml",
    "standard_inchi_key": "DLPUOZGNMZKXKB-YEWFCNIMSA-N"}, {"declared_mechanism_roots_literal":
    ["causal_graphs", "biosynthetic_pathway"], "identifier": "CHEBI:155912", "owned_bgc_ids":
    ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-c.yaml", "standard_inchi_key":
    "UCCFSWQSMDQYHO-GXTWGEPZSA-N"}, {"declared_mechanism_roots_literal": ["causal_graphs",
    "biosynthetic_pathway"], "identifier": "CHEBI:155910", "owned_bgc_ids": ["BGC0002225"],
    "path": "data/natural_products/terpenoids/aculene-d.yaml", "standard_inchi_key":
    "IIQOUDJDCRTCJY-MBNYWOFBSA-N"}, {"declared_mechanism_roots_literal": [], "identifier":
    "naturalproductmech:mibig-0e7dc695d0", "owned_bgc_ids": ["BGC0002225"], "path":
    "data/natural_products/terpenoids/asperaculane-a.yaml", "standard_inchi_key":
    "JDBMOJWYGWGAIH-DZBCAUDPSA-N"}, {"declared_mechanism_roots_literal": [], "identifier":
    "naturalproductmech:mibig-d4c2d69c3b", "owned_bgc_ids": ["BGC0002225"], "path":
    "data/natural_products/terpenoids/asperaculane-b.yaml", "standard_inchi_key":
    "GFYHPKUYDFUKNL-MBNYWOFBSA-N"}]'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-companion-3
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/3/input; /contexts/3/complete_raw_text; /contexts/3/complete_raw_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete direct companion plaintext and history, retained as separate owner
    CHEBI:156056 with full key DLPUOZGNMZKXKB-YEWFCNIMSA-N. Source reading is attributed
    in the source notes; no congener claim transfer.
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-companion-4
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/input; /contexts/4/complete_raw_text; /contexts/4/complete_raw_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete direct companion plaintext and history, retained as separate owner
    CHEBI:155912 with full key UCCFSWQSMDQYHO-GXTWGEPZSA-N. Source reading is attributed
    in the source notes; no congener claim transfer.
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-companion-5
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/5/input; /contexts/5/complete_raw_text; /contexts/5/complete_raw_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete direct companion plaintext and history, retained as separate owner
    CHEBI:155910 with full key IIQOUDJDCRTCJY-MBNYWOFBSA-N. Source reading is attributed
    in the source notes; no congener claim transfer.
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-companion-10
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/10/input; /contexts/10/complete_raw_text; /contexts/10/complete_raw_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete direct companion plaintext and history, retained as separate owner
    naturalproductmech:mibig-0e7dc695d0 with full key JDBMOJWYGWGAIH-DZBCAUDPSA-N.
    Source reading is attributed in the source notes; no congener claim transfer.
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-companion-11
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/11/input; /contexts/11/complete_raw_text; /contexts/11/complete_raw_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete direct companion plaintext and history, retained as separate owner
    naturalproductmech:mibig-d4c2d69c3b with full key GFYHPKUYDFUKNL-MBNYWOFBSA-N.
    Source reading is attributed in the source notes; no congener claim transfer.
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/11
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained OBO stanzas for source taxa; no fresh taxonomy or ancestry
    inference: [{"complete_stanza": "[Term]\nid: NCBITaxon:5053\nname: Aspergillus
    aculeatus\nsynonym: \"Aspergillus japonicus var. aculeatus\" EXACT []\n\n", "id":
    "NCBITaxon:5053", "physical_line": 7851}, {"complete_stanza": "[Term]\nid: NCBITaxon:690307\nname:
    Aspergillus aculeatus ATCC 16872\n\n", "id": "NCBITaxon:690307", "physical_line":
    107651}]'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/source_taxa; /contexts/2/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/2/source_scope_inventory/nonorganism_matches; /contexts/2/source_scope_inventory/actual_assay_rows;
    /contexts/2/source_scope_inventory/blank_AID_sentinels; /contexts/2/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Exact retained route sets, distinguishing nonempty source taxa from empty
    forward/nonorganism matches and blank sentinels from actual assays: {"actual_assay_rows":
    [], "blank_AID_sentinels": [], "forward_taxon_merge_matches": [], "nonorganism_matches":
    [], "related_corpus_rows": [], "source_taxa": ["NCBITaxon:5053", "NCBITaxon:690307"]}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 1 positive
    placements. {"matches": [{"last_physical_line": 2647, "physical_line": 2647, "raw_tsv_record":
    "BGC0002225\t3\tactive\tquestionable\tunknown\taculene A\t1\tCCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C\tInChI=1S/C19H25NO3/c1-4-13-11-16(21)19(3)14(13)8-7-12(2)10-17(19)23-18(22)15-6-5-9-20-15/h7-8,11,15,17,20H,4-6,9-10H2,1-3H3/t15-,17-,19-/m0/s1\tLOOAMPJDSIVZQC-IEZWGBDMSA-N\ttrue\t\tnpatlas:NPA007875\tNCBITaxon:690307\tAspergillus
    aculeatus ATCC 16872\tterpene\tUnknown\tKV878977.1\t1125505\t1144430\tHeterologous
    expression|Knock-out studies\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tPMID:31618514\tENTRY\n",
    "row": {"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis":
    "CLUSTER_DEMONSTRATED", "compound_classes": "", "compound_index": "1", "compound_name":
    "aculene A", "database_ids": "npatlas:NPA007875", "entry_completeness": "unknown",
    "entry_quality": "questionable", "entry_status": "active", "entry_version": "3",
    "genome_accession": "KV878977.1", "locus_evidence_methods": "Heterologous expression|Knock-out
    studies", "locus_from": "1125505", "locus_to": "1144430", "mibig_accession": "BGC0002225",
    "primary_reference": "PMID:31618514", "producer_evidence_basis": "BGC_CHARACTERIZED",
    "reference_basis": "ENTRY", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C",
    "standard_inchi": "InChI=1S/C19H25NO3/c1-4-13-11-16(21)19(3)14(13)8-7-12(2)10-17(19)23-18(22)15-6-5-9-20-15/h7-8,11,15,17,20H,4-6,9-10H2,1-3H3/t15-,17-,19-/m0/s1",
    "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC 16872"},
    "row_sha256": "6ddf8f2e64a3fec2c3a60c5f9c2f093ab8bc5ba1a654f3356dc234919455ca59"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2647–2647; row_sha256 6ddf8f2e64a3fec2c3a60c5f9c2f093ab8bc5ba1a654f3356dc234919455ca59
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"bgc_classes": "terpene", "bgc_subclasses": "Unknown",
    "cluster_link_evidence_basis": "CLUSTER_DEMONSTRATED", "compound_classes": "",
    "compound_index": "1", "compound_name": "aculene A", "database_ids": "npatlas:NPA007875",
    "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status":
    "active", "entry_version": "3", "genome_accession": "KV878977.1", "locus_evidence_methods":
    "Heterologous expression|Knock-out studies", "locus_from": "1125505", "locus_to":
    "1144430", "mibig_accession": "BGC0002225", "primary_reference": "PMID:31618514",
    "producer_evidence_basis": "BGC_CHARACTERIZED", "reference_basis": "ENTRY", "smiles":
    "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C", "standard_inchi":
    "InChI=1S/C19H25NO3/c1-4-13-11-16(21)19(3)14(13)8-7-12(2)10-17(19)23-18(22)15-6-5-9-20-15/h7-8,11,15,17,20H,4-6,9-10H2,1-3H3/t15-,17-,19-/m0/s1",
    "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC 16872"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2261-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 1 positive
    placements. {"matches": [{"last_physical_line": 42974, "physical_line": 42974,
    "raw_tsv_record": "CHEBI:156057\taculene A\tA carboxylic ester resulting from
    the formal condensation of the hydroxy group of aculene C with the carboxylic
    acid group of L-proline. It is a sesquiterpenoid isolated from the fungus Aspergillus
    aculeatus.\t3\tLOOAMPJDSIVZQC-IEZWGBDMSA-N\tCCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2OC(=O)[C@@H]1CCCN1\n",
    "row": {"chebi_id": "CHEBI:156057", "definition": "A carboxylic ester resulting
    from the formal condensation of the hydroxy group of aculene C with the carboxylic
    acid group of L-proline. It is a sesquiterpenoid isolated from the fungus Aspergillus
    aculeatus.", "name": "aculene A", "smiles": "CCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2OC(=O)[C@@H]1CCCN1",
    "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "stars": "3"}, "row_sha256":
    "c7b4cc92c659d4aa084e5ff4e8ee7ff6a432f7708a6d864db4520e856d176cd0"}], "predicate":
    "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-source-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line 1; physical lines 42974–42974; row_sha256 c7b4cc92c659d4aa084e5ff4e8ee7ff6a432f7708a6d864db4520e856d176cd0
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"chebi_id": "CHEBI:156057", "definition": "A carboxylic
    ester resulting from the formal condensation of the hydroxy group of aculene C
    with the carboxylic acid group of L-proline. It is a sesquiterpenoid isolated
    from the fungus Aspergillus aculeatus.", "name": "aculene A", "smiles": "CCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2OC(=O)[C@@H]1CCCN1",
    "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "stars": "3"}]'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2261-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 1 positive
    placements. {"matches": [{"last_physical_line": 4236, "physical_line": 4236, "raw_tsv_record":
    "LOOAMPJDSIVZQC-IEZWGBDMSA-N\tAspergillus aculeatus\tNCBITaxon:5053\thttp://www.wikidata.org/entity/Q4807886\t10.3390/MOLECULES190810898\thttp://www.wikidata.org/entity/Q77419757\n",
    "row": {"organism_name": "Aspergillus aculeatus", "organism_wikidata": "http://www.wikidata.org/entity/Q4807886",
    "reference_doi": "10.3390/MOLECULES190810898", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q77419757", "taxon_id":
    "NCBITaxon:5053"}, "row_sha256": "8247d07b1c0a369b96c97f54055d2a8eff305322e55fa4038df67319f58ae9a8"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-source-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 4236–4236; row_sha256 8247d07b1c0a369b96c97f54055d2a8eff305322e55fa4038df67319f58ae9a8
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"organism_name": "Aspergillus aculeatus", "organism_wikidata":
    "http://www.wikidata.org/entity/Q4807886", "reference_doi": "10.3390/MOLECULES190810898",
    "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q77419757",
    "taxon_id": "NCBITaxon:5053"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2261-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 0 positive
    placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality",
    "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 1 positive
    placements. {"matches": [{"last_physical_line": 1389, "physical_line": 1389, "raw_tsv_record":
    "LOOAMPJDSIVZQC-IEZWGBDMSA-N\tCCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C\tTerpenoids\tSesquiterpenoids\tDaucane
    sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results":
    "Daucane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C",
    "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "superclass_results": "Sesquiterpenoids"},
    "row_sha256": "112ea9533d8310a62e032f97cf08e6806fd23dcad50b660633670a014f1fa20c"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 1389–1389; row_sha256 112ea9533d8310a62e032f97cf08e6806fd23dcad50b660633670a014f1fa20c
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"class_results": "Daucane sesquiterpenoids", "is_glycoside":
    "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results":
    "Terpenoids", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2OC(=O)[C@@H]3CCCN3)C)C",
    "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N", "superclass_results": "Sesquiterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2261-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 0 positive
    placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality",
    "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 0 positive
    placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality",
    "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 0 positive
    placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality",
    "query": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 1 positive
    placements. {"matches": [{"last_physical_line": 16917, "physical_line": 16917,
    "raw_tsv_record": "CHEBI:156057\tAspergillus aculeatus\t5053\tcell suspension
    culture\t\t25068785\t\n", "row": {"chebi_id": "CHEBI:156057", "comments": "",
    "component_text": "cell suspension culture", "source_accession": "25068785", "species_accession":
    "5053", "species_text": "Aspergillus aculeatus", "strain_text": ""}, "row_sha256":
    "1f5b03c1406915f5ec2a906679e575ceed7d4688200f218d8b347c5701d146f8"}], "predicate":
    "exact chebi_id from exact full-key structure rows", "query": ["CHEBI:156057"]}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2261-source-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Header line 1; physical lines 16917–16917; row_sha256 1f5b03c1406915f5ec2a906679e575ceed7d4688200f218d8b347c5701d146f8
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"chebi_id": "CHEBI:156057", "comments": "", "component_text":
    "cell suspension culture", "source_accession": "25068785", "species_accession":
    "5053", "species_text": "Aspergillus aculeatus", "strain_text": ""}]'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: bgc-2261-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ChemicalStructure distinguishes normalized identity and unspecified stereochemistry.
    ComputedClassification is explicitly a named/versioned prediction, never a source
    assertion or record-admission reason.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2261-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: The maintained extractor derives the stereo_complete flag from unassigned
    chiral centres; no new extractor call occurred in this review.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2261-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 971–1037
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: The seeder retains the exact structure/definition source and copies named
    NPClassifier results including is_glycoside. A prediction is not promoted to experimental
    evidence.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2261-origin-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 1093–1151
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Producer evidence and locus methods/link grades remain separately copied;
    merges and applicable local qualifications have distinct handling.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2261-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole profile
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Current review profile requires one-record identity, evidence, provenance,
    representation and completion dimensions without promoting unavailable verification.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2261-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole review skill
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Current one-record review scope distinguishes local evidence review from
    scientific completeness, preserves source records, and requires concrete supported
    findings.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-227/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-227/native-current227-five-gates-execution-001.json
  accessed_at: '2026-11-03T17:12:11.356673Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: e8998673dfc66cfe5e88cee01e9e8af72040248e60a1d519e5001d28b6da7542
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-227/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-227/native-current227-five-gates-execution-001.json
  accessed_at: '2026-11-03T17:12:37.686250Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 4b9cab24405253d6b4fb56ff59f013dcdf9ea9c1a980935a83cbbc661d9d7b8c
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-227/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-227/native-current227-five-gates-execution-001.json
  accessed_at: '2026-11-03T17:12:58.213877Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-227/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-227/native-current227-five-gates-execution-001.json
  accessed_at: '2026-11-03T17:13:32.681472Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-227/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-227/native-current227-five-gates-execution-001.json
  accessed_at: '2026-11-03T17:13:44.564564Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 68832113362bd405215bb25de9aacdabbbd0adafee48e333f4dd6f64da397bbd
assessments:
- assessment_id: bgc-2261-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The retained EXACT grounding CHEBI:156057 joins MIBiG BGC0002225 version
    3 compound index 1 and the three-star ChEBI row by the complete key LOOAMPJDSIVZQC-IEZWGBDMSA-N.
    The definition describes formal esterification of aculene C with L-proline; the
    saved topology has the corresponding alcohol-derived O–C(=O)–pyrrolidine connection
    and an S proline alpha carbon. This supports local definition/structure consistency,
    not a claim that the esterification was experimentally demonstrated. Five direct
    BGC companions retain different complete keys.
  target_ids:
  - CHEBI:156057
  evidence_ids:
  - bgc-2261-grounding-owner
  - bgc-2261-source-mibig_compounds
  - bgc-2261-source-chebi_structures
  - bgc-2261-query-chebi_structures
  - bgc-2261-chemistry
  - bgc-2261-topology
  - bgc-2261-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: LOOAMPJDSIVZQC-IEZWGBDMSA-N; exact complete source key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2261-grounding-owner
    - bgc-2261-source-mibig_compounds
    - bgc-2261-source-chebi_structures
    - bgc-2261-query-chebi_structures
    - bgc-2261-chemistry
    - bgc-2261-topology
    - bgc-2261-direct-contexts
  - name: grounding_scope
    value: EXACT CHEBI:156057; full-key MIBiG/three-star ChEBI agreement and locally
      consistent ester definition.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2261-grounding-owner
    - bgc-2261-source-mibig_compounds
    - bgc-2261-source-chebi_structures
    - bgc-2261-query-chebi_structures
    - bgc-2261-chemistry
    - bgc-2261-topology
    - bgc-2261-direct-contexts
- assessment_id: bgc-2261-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both stored forms give neutral C19H25NO3 with 23 atoms, 25 bonds, one fragment
    and three specified tetrahedral centres. In the SMILES table C6 is R, C12 is S
    and C16 is S; the corresponding InChI atoms 18, 16 and 14 retain those assignments.
    The five- and seven-membered fused carbon rings coexist with a separate pyrrolidine
    ring. All ten comparison flags and the complete stored chirality-aware correspondence
    agree. The diagnostic explicitly leaves independent full-graph and natural identity
    unestablished.
  target_ids:
  - CHEBI:156057
  evidence_ids:
  - bgc-2261-grounding-owner
  - bgc-2261-chemistry
  - bgc-2261-topology
  - bgc-2261-diagnostic-acceptance
  - bgc-2261-structure-schema
  - bgc-2261-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: 'Three specified tetrahedral centres: SMILES C6 R, C12 S and C16 S; retained
      true flag within the extractor''s centre-based scope.'
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2261-grounding-owner
    - bgc-2261-chemistry
    - bgc-2261-topology
    - bgc-2261-diagnostic-acceptance
    - bgc-2261-structure-schema
    - bgc-2261-stereo-method
  - name: representation_correspondence
    value: Ten true flags and a complete stored chirality-aware map; no independent
      full-graph or natural identity claim.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2261-grounding-owner
    - bgc-2261-chemistry
    - bgc-2261-topology
    - bgc-2261-diagnostic-acceptance
    - bgc-2261-structure-schema
    - bgc-2261-stereo-method
- assessment_id: bgc-2261-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: MIBiG BGC0002225 version 3 is active, of questionable quality and unknown
    completeness. Aspergillus aculeatus ATCC 16872, NCBITaxon:690307, is graded BGC_CHARACTERIZED,
    while the locus is separately CLUSTER_DEMONSTRATED from heterologous expression
    and knock-out studies. The retained interval is genbank:KV878977.1, 1125505–1144430.
    The species-level occurrence taxon 5053 is distinct from the producing-strain
    assertion. Complete cached stanzas preserve these labels; they are not a fresh
    taxonomy or genome verification.
  target_ids:
  - CHEBI:156057
  evidence_ids:
  - bgc-2261-origin-owner
  - bgc-2261-source-mibig_compounds
  - bgc-2261-cached-taxonomy
  - bgc-2261-source-routes
  - bgc-2261-origin-seeder
  dimensions:
  - name: taxon_scope
    value: Producer strain 690307; occurrence species 5053.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2261-origin-owner
    - bgc-2261-source-mibig_compounds
    - bgc-2261-cached-taxonomy
    - bgc-2261-source-routes
    - bgc-2261-origin-seeder
  - name: producer_evidence
    value: BGC_CHARACTERIZED from the retained MIBiG claim; distinct from species-level
      occurrences.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2261-origin-owner
    - bgc-2261-source-mibig_compounds
    - bgc-2261-cached-taxonomy
    - bgc-2261-source-routes
    - bgc-2261-origin-seeder
  - name: locus_evidence
    value: BGC0002225 version 3, questionable/unknown, CLUSTER_DEMONSTRATED from heterologous
      expression and knock-out studies.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2261-origin-owner
    - bgc-2261-source-mibig_compounds
    - bgc-2261-cached-taxonomy
    - bgc-2261-source-routes
    - bgc-2261-origin-seeder
- assessment_id: bgc-2261-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: The MIBiG producer and locus citations both retain ENTRY-level PMID:31618514.
    The LOTUS occurrence cites DOI:10.3390/MOLECULES190810898 and the ChEBI origin
    cites PMID:25068785 with cell-suspension-culture text. These are retained source
    assertions with distinct claim roles; different citation identifiers do not establish
    independent experiments. The definition is attributed to CHEBI:156057. The historical
    AneA annotations on direct C/D companions do not become an A-specific enzyme assay.
  target_ids:
  - CHEBI:156057
  evidence_ids:
  - bgc-2261-origin-owner
  - bgc-2261-occurrence-owner
  - bgc-2261-source-mibig_compounds
  - bgc-2261-source-lotus_occurrences
  - bgc-2261-query-chebi_origins
  - bgc-2261-source-notes
  - bgc-2261-direct-contexts
  - bgc-2261-source-chebi_structures
  - bgc-2261-companion-4
  - bgc-2261-companion-5
  dimensions:
  - name: citation_scope
    value: ENTRY PMID:31618514; occurrence DOI:10.3390/MOLECULES190810898 and PMID:25068785;
      definition CHEBI:156057.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2261-origin-owner
    - bgc-2261-occurrence-owner
    - bgc-2261-source-mibig_compounds
    - bgc-2261-source-lotus_occurrences
    - bgc-2261-query-chebi_origins
    - bgc-2261-source-notes
    - bgc-2261-direct-contexts
    - bgc-2261-source-chebi_structures
    - bgc-2261-companion-4
    - bgc-2261-companion-5
- assessment_id: bgc-2261-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: The owner writes two occurrences for Aspergillus aculeatus taxon 5053,
    one from LOTUS and one from ChEBI. They are occurrence assertions rather than
    two proven producer experiments. No bioactivities, molecular targets or mechanism
    roots are written in this owner. Its exact saved PubChem, BindingDB and AntibioticMech
    joins are empty, as is the CyanometDB occurrence join. This is bounded absence
    in the retained snapshot, not proof of biological inactivity or absence of a pathway.
  target_ids:
  - CHEBI:156057
  evidence_ids:
  - bgc-2261-assay-owner
  - bgc-2261-occurrence-owner
  - bgc-2261-source-lotus_occurrences
  - bgc-2261-query-chebi_origins
  - bgc-2261-query-pubchem_bioassay
  - bgc-2261-query-bindingdb_targets
  - bgc-2261-query-antibioticmech_inchikeys
  - bgc-2261-query-cyanometdb_occurrences
  - bgc-2261-source-routes
  - bgc-2261-cached-taxonomy
  dimensions:
  - name: occurrence_scope
    value: Two written species-level occurrences, one LOTUS and one ChEBI; no independent-experiment
      count.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2261-assay-owner
    - bgc-2261-occurrence-owner
    - bgc-2261-source-lotus_occurrences
    - bgc-2261-query-chebi_origins
    - bgc-2261-query-pubchem_bioassay
    - bgc-2261-query-bindingdb_targets
    - bgc-2261-query-antibioticmech_inchikeys
    - bgc-2261-query-cyanometdb_occurrences
    - bgc-2261-source-routes
    - bgc-2261-cached-taxonomy
  - name: assay_target_scope
    value: No written pharmacological assays/targets and no actual retained AID rows;
      bounded empty exact assay/target joins.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2261-assay-owner
    - bgc-2261-occurrence-owner
    - bgc-2261-source-lotus_occurrences
    - bgc-2261-query-chebi_origins
    - bgc-2261-query-pubchem_bioassay
    - bgc-2261-query-bindingdb_targets
    - bgc-2261-query-antibioticmech_inchikeys
    - bgc-2261-query-cyanometdb_occurrences
    - bgc-2261-source-routes
    - bgc-2261-cached-taxonomy
- assessment_id: bgc-2261-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The retained source BGC class is TERPENE. NPClassifier version npclassifier.gnps2.org@2026-09-07
    supplies Terpenoids / Sesquiterpenoids / Daucane sesquiterpenoids and is_glycoside:false.
    The saved fused carbocyclic core, ketone and proline ester support a local structural
    interpretation compatible with that broad filing; no sugar residue or glycosidic
    linkage is established. The amino-acid-derived ester does not by itself establish
    a peptide biosynthetic class. The model and BGC labels remain distinct from direct
    biosynthetic evidence.
  target_ids:
  - CHEBI:156057
  evidence_ids:
  - bgc-2261-classification-owner
  - bgc-2261-source-npclassifier
  - bgc-2261-source-mibig_compounds
  - bgc-2261-chemistry
  - bgc-2261-topology
  - bgc-2261-structure-schema
  - bgc-2261-classification-seeder
  dimensions:
  - name: classification_applicability
    value: Retained model and BGC labels remain distinct; false glycoside prediction
      is compatible with saved topology, without proving biosynthesis.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2261-classification-owner
    - bgc-2261-source-npclassifier
    - bgc-2261-source-mibig_compounds
    - bgc-2261-chemistry
    - bgc-2261-topology
    - bgc-2261-structure-schema
    - bgc-2261-classification-seeder
- assessment_id: bgc-2261-completion
  area: completeness
  topic: Completion
  outcome: supported
  summary: Partial scientific review from complete local source and saved molecular
    evidence; five local gates passed, full QC/OAK and fresh external verification
    unavailable.
  target_ids:
  - CHEBI:156057
  evidence_ids:
  - bgc-2261-owner
  - bgc-2261-capture
  - bgc-2261-intake
  - bgc-2261-intake-acceptance
  - bgc-2261-source-plan
  - bgc-2261-plan-acceptance
  - bgc-2261-source-notes
  - bgc-2261-inventory-acceptance
  - bgc-2261-diagnostic-execution
  - bgc-2261-diagnostic-acceptance
  - bgc-2261-native-acceptance
  - bgc-2261-review-profile
  - bgc-2261-review-skill
  dimensions:
  - name: review_completion
    value: Partial scientific review from complete local source and saved molecular
      evidence; five local gates passed, full QC/OAK and fresh external verification
      unavailable.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2261-owner
    - bgc-2261-capture
    - bgc-2261-intake
    - bgc-2261-intake-acceptance
    - bgc-2261-source-plan
    - bgc-2261-plan-acceptance
    - bgc-2261-source-notes
    - bgc-2261-inventory-acceptance
    - bgc-2261-diagnostic-execution
    - bgc-2261-diagnostic-acceptance
    - bgc-2261-native-acceptance
    - bgc-2261-review-profile
    - bgc-2261-review-skill
findings: []
actions: []
limitations:
- External identifiers, taxonomy, genome accessions and primary publications were
  not refreshed under the absolute no-request instruction. Historical and database
  assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and stored-form
  parsing establish only their declared mechanical scope.
- Empty joins refer only to the retained exact predicates and snapshots; they do not
  establish biological absence. Shared loci, citations and congeners do not transfer
  compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source
  records, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- The complete owner/history, actual intake, exact retained query/source payloads
  and both full paired molecular tables were personally read. Complementary companion/cached-source
  reading is explicitly attributed in the pinned notes.
- The original batch diagnostic stderr is empty. All true comparison flags leave full_graph_identity_established:false
  unchanged.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-227
```
