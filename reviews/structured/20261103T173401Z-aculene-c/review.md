# Local evidence review: aculene C

- Review: 20261103T173401Z-aculene-c
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T17:10:56.590299Z
- Finished UTC: 2026-11-03T17:34:01.055377Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Aculene C retains a consistent full-key identity, two specified centres and a partial historical AneA conversion from aculene D. Producer, occurrence and source grades remain separate; reader preservation does not establish fresh primary support. Scientific completion remains partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2263; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:155912 | data/natural_products/terpenoids/aculene-c.yaml | generated | aculene C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for aculene C | passed | True | CHEBI:155912 | One original offline maintained call preserved the complete owner and historically attributed mechanism content. Mechanical preservation is distinct from fresh scientific validation. |
| strict_ten | passed | True | CHEBI:155912 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:155912 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:155912 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:155912 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:155912 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:155912 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:155912 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:155912 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: CHEBI:155912.

CHEBI:155912 is locally grounded by exact complete-key agreement UCCFSWQSMDQYHO-GXTWGEPZSA-N between MIBiG BGC0002225 version 3 compound index 3 and the three-star ChEBI row. The stored ketone, hydroxy group and fused five/seven-membered core are consistent with the retained aculene C definition, including the S hydroxy-bearing and R methyl-bearing bridgehead centres. Aculene congeners are not interchangeable merely because they share the same cluster.

### Representation

representation: supported. Targets: CHEBI:155912.

Both stored forms give neutral C14H18O2 with 16 atoms, 17 bonds and one fragment. The two specified centres are SMILES C6 R and C12 S, corresponding to InChI C13 R and C11 S. The core C7=C8 bond is double, in addition to C2=C3 and C9=C10; the carbonyl is C4=O5 and C12 bears OH13. All ten comparisons and the complete stored chirality-aware map agree. No external structure or isolated natural stereochemistry has been independently established.

### Origin

provenance: supported. Targets: CHEBI:155912.

The source retains Aspergillus aculeatus ATCC 16872, taxon 690307, as BGC_CHARACTERIZED and BGC0002225 version 3 as CLUSTER_DEMONSTRATED from heterologous expression and knock-out studies. Entry quality is questionable and completeness unknown. Genbank:KV878977.1 interval 1125505–1144430 is the source locus. Aspergillus aculeatus species 5053 and Penicillium sp. SCS-KFD08 taxon 1808020 are separately retained occurrence taxa; their cached labels do not make Penicillium a producer of this Aspergillus locus.

### Citations

evidence: supported. Targets: CHEBI:155912.

MIBiG producer/locus support remains ENTRY PMID:31618514. Occurrence assertions retain LOTUS DOI:10.3390/MOLECULES190810898, ChEBI Aspergillus PMID:25547729 and Penicillium PMID:27709333. The graph and pathway separately retain DOI:10.1002/anie.201910200 as PRIMARY_EXPERIMENT, DOI:10.1039/D1NP00074H as REVIEW, and dated MIBiG/UniProt/Rhea database assertions. These locally preserved citations and snippets have not been freshly accessed; the reader confirms preservation rather than experimental sufficiency.

### Bioactivity

evidence: supported. Targets: CHEBI:155912.

The owner writes three occurrence objects: a Penicillium ChEBI assertion and separate LOTUS/ChEBI Aspergillus assertions. PubChem physical row 8042 for CID 139586350 is a blank-AID '(no assay data)' sentinel, not an activity observation. No pharmacological bioactivity or molecular-target root is written, and the exact BindingDB/AntibioticMech joins are empty. The AneA biosynthesis annotation is a substrate-to-product claim, not a pharmacological target assay.

### Classification

consistency: supported. Targets: CHEBI:155912.

The saved C14 fused carbocyclic ketone/alcohol topology is compatible with the retained broad terpene filing. MIBiG TERPENE and NPClassifier npclassifier.gnps2.org@2026-09-07 Terpenoids / Sesquiterpenoids / Daucane sesquiterpenoids remain different evidence axes. The copied is_glycoside:false prediction is consistent with the absence of a sugar linkage in the saved complete tables. Neither classifier output nor class membership makes the partial AneA reaction a complete biosynthetic pathway.

### Completion

completeness: supported. Targets: CHEBI:155912.

Partial scientific review from complete local source and saved molecular evidence; five local gates passed, full QC/OAK and fresh external verification unavailable. The exact original maintained reader passed for this positive owner; historical evidence limits remain.

### Partial AneA reaction and owner direction

graph: supported. Targets: CHEBI:155912.

The accepted maintained view preserves one graph, three nodes, two edges, ten graph evidence placements and one pathway step with five evidence placements. AneA is annotated to desaturate aculene D into aculene C, with RHEA:65112 listing 2-oxoglutarate and O2 as cosubstrates and succinate, CO2 and water among products. The owner is the product aculene C. The retained gene-inactivation, feeding and heterologous-reconstitution description is a historical source annotation. No complete pathway, native flux or fresh primary-paper validation follows from reader success.

### Protein identity, evidence and construct limits

grounding: supported. Targets: CHEBI:155912.

UniProtKB:A0A1L9WUX8 is retained as the 298-residue A. aculeatus ATCC 16872 AneA reference, linked historically to OJJ99912.1, ASPACDRAFT_119783, KV878977 and RHEA:65112. The graph distinguishes primary-experiment/review annotations from dated MIBiG, UniProt and Rhea database assertions. Those local claims are not a newly inspected sequence or proof that a native reference equals every experimental construct. Exact assay construct, kinetics, cofactor occupancy and native complex/flux were not established in this offline review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2263-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/aculene-c.yaml; Whole owner plaintext and complete curation_history | supports | Complete current owner and its 3 ordered history events, personally read. Native curation_status remains SEEDED. |
| bgc-2263-capture | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/2/owner_pin; /records/2/owner_document | supports | Exact captured owner, including all written nonmechanistic fields, roots and history. |
| bgc-2263-intake | /private/tmp/npm-review-work/shared-next-batch227/intakes/2263-inspect-001.json; /source; /targets | supports | Actual one-record canonical inspection with 44 source inputs and target CHEBI:155912; current owner and context roles are retained. |
| bgc-2263-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch227/root-intake-ready-001.json; /accepted; /intake_summary; /verification | supports | ROOT accepts all ten original canonical intakes, their exact target/source maps and current dependency pins. |
| bgc-2263-grounding-owner | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/2/owner_document/identifier; /records/2/owner_document/label; /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status; /records/2/owner_document/definition; /records/2/owner_document/definition_source | supports | Written identity/structure/grounding fields and definition when present: {"chemical_structure": {"smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C", "standard_inchi": "InChI=1S/C14H18O2/c1-4-10-8-13(16)14(3)11(10)6-5-9(2)7-12(14)15/h5-6,8,12,15H,4,7H2,1-3H3/t12-,14+/m0/s1", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002225"}, "definition": "A sesquiterpenoid that is 8,8a-dihydroazulen-1(7H)-one substituted by an ethyl, methyl, hydroxy and methyl groups at positions 3, 6, 8S, and 8aR, respectively. It is a fungal metabolite isolated from Penicillium sp. SCS-KFD08 and Aspergillus aculeatus.", "definition_source": "CHEBI:155912", "grounding_status": "EXACT", "identifier": "CHEBI:155912", "label": "aculene C", "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-9c98bc7a0d", "source": "MIBIG", "source_id": "BGC0002225", "source_label": "aculene C", "source_version": "3"}, {"minted_identifier": "naturalproductmech:chebi-fc49794a70", "source": "CHEBI", "source_id": "CHEBI:155912", "source_label": "aculene C", "source_version": "3-star"}]} |
| bgc-2263-origin-owner | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/producer_taxon_groups; /records/2/owner_document/bgc_class | supports | Written producer and locus fields, including source versions, methods, citation roles and taxon groups: {"bgc_class": ["TERPENE"], "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002225", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002225 entry version 3; citation taken from the entry level", "reference": "PMID:31618514"}], "genome_accession": "genbank:KV878977.1", "link_evidence_basis": "CLUSTER_DEMONSTRATED", "locus_evidence_methods": ["Heterologous expression", "Knock-out studies"], "locus_from": 1125505, "locus_to": 1144430, "organism_label": "Aspergillus aculeatus ATCC 16872", "organism_taxon_id": "NCBITaxon:690307"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0002225", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002225 entry version 3; citation taken from the entry level", "reference": "PMID:31618514"}], "evidence_basis": "BGC_CHARACTERIZED", "notes": "Locus evidence: Heterologous expression&#124;Knock-out studies. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC 16872"}], "producer_taxon_groups": ["FUNGAL"]} |
| bgc-2263-assay-owner | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/2/owner_document | supports | The complete captured owner has no bioactivities or molecular_targets root. It retains one biosynthetic graph and one pathway entry. |
| bgc-2263-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/2/owner_document/occurrences; /records/2/owner_document/occurrence_taxon_groups | supports | All written occurrences and occurrence groups: {"occurrence_taxon_groups": ["FUNGAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "ChEBI compound origin for CHEBI:155912", "reference": "PMID:27709333"}], "notes": "cell suspension culture", "source": "CHEBI", "taxon_id": "NCBITaxon:1808020", "taxon_label": "Penicillium sp. SCS-KFD08", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.3390/MOLECULES190810898"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q4807886", "source": "LOTUS", "taxon_id": "NCBITaxon:5053", "taxon_label": "Aspergillus aculeatus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "ChEBI compound origin for CHEBI:155912", "reference": "PMID:25547729"}], "notes": "cell suspension culture", "source": "CHEBI", "taxon_id": "NCBITaxon:5053", "taxon_label": "Aspergillus aculeatus", "taxon_source": "NCBITaxon"}]} |
| bgc-2263-classification-owner | /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json; /records/2/owner_document/np_pathway; /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class | supports | Literal written model/version/results and separate source BGC classification: {"bgc_class": ["TERPENE"], "np_classification": {"class_results": ["Daucane sesquiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Sesquiterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS"} |
| bgc-2263-chemistry | /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/smiles/status; /records/2/inchi/status; /records/2/smiles/computed; /records/2/inchi/computed; /records/2/comparisons; /records/2/atom_correspondence | supports | Both saved forms parsed. They give C14H18O2, charge 0, 16 atoms and 17 bonds each. All ten comparison flags are true; a complete stored chirality-aware correspondence is retained, with full_graph_identity_established:false. Stereo counts: {"Atom_Tetrahedral:Specified": 2}. |
| bgc-2263-topology | /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-DATA-001.json; /records/2/smiles/computed; /records/2/inchi/computed; /records/2/atom_correspondence | supports | SMILES C4(=O5) is the ketone, C12–OH13 the alcohol and C7=C8 the additional core double bond. The fused rings are [2,3,4,6,7] and [8,7,6,12,11,10,9]. Saved motifs and all atom/bond rows show no ester, amide or sugar linkage. |
| bgc-2263-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr; /external_requests | supports | The original ROOT-owned diagnostic execution returned zero and retained its command and exact stdout/stderr pins; stderr is empty and no external request is reported. |
| bgc-2263-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch227/root-local-diagnostics-acceptance-001.json; /accepted; /DATA; /execution; /verification; /limits | supports | ROOT accepts the original saved 20-form diagnostic and current inputs; its mechanical comparison and preservation checks do not establish fresh natural identity. |
| bgc-2263-native-acceptance | /private/tmp/npm-review-work/shared-next-batch227/root-native-five-gates-acceptance-001.json; /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable; /verification | supports | Five original local commands passed. all_native_gates_passed remains false, with full QC and OAK unavailable. Queue and reproduction checks have their recorded mechanical scope. |
| bgc-2263-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch227-tentative/root-source-inventory-acceptance-001.json; /accepted; /inventory | supports | ROOT accepts this exact saved inventory. Source-payload interpretation is separately attributed in the source notes. |
| bgc-2263-source-plan | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-target-input-plan-001.json; /records/2; /source_placement_count; /unique_source_path_count | supports | Accepted source plan retains this record and its exact input projection, within the batch totals of 418 placements and 53 paths. |
| bgc-2263-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch227/root-input-plan-acceptance-001.json; /accepted; /input_plan; /notes; /verification | supports | ROOT accepts the actual composed source plan and pinned source-reading notes with exact source/current input joins. |
| bgc-2263-source-notes | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-scope-notes-001.json; /reading; /curation; /cautions; /inventory_ROOT_acceptance | supports | Complete source-reading attribution: BGC contexts 0–6, 63 frames and 38 positive rows; Support contexts 7–11, 45 frames and 138 rows. All 15 cached stanzas are assigned. The bounded ignored-inclusive eight-table, 44-literal curation scan found no matching rows; this is limited to its declared exact-token scope. |
| bgc-2263-direct-contexts | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /records/2/direct_companion_predicates; /contexts/2/identifier; /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids; /contexts/2/declared_mechanism_roots_literal; /contexts/3/identifier; /contexts/3/standard_inchi_key; /contexts/3/owned_bgc_ids; /contexts/3/declared_mechanism_roots_literal; /contexts/5/identifier; /contexts/5/standard_inchi_key; /contexts/5/owned_bgc_ids; /contexts/5/declared_mechanism_roots_literal; /contexts/10/identifier; /contexts/10/standard_inchi_key; /contexts/10/owned_bgc_ids; /contexts/10/declared_mechanism_roots_literal; /contexts/11/identifier; /contexts/11/standard_inchi_key; /contexts/11/owned_bgc_ids; /contexts/11/declared_mechanism_roots_literal | supports | Exact one-hop predicate and owner profiles; these do not transfer identity, activity or mechanism: [{"declared_mechanism_roots_literal": [], "identifier": "CHEBI:156057", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-a.yaml", "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"}, {"declared_mechanism_roots_literal": [], "identifier": "CHEBI:156056", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-b.yaml", "standard_inchi_key": "DLPUOZGNMZKXKB-YEWFCNIMSA-N"}, {"declared_mechanism_roots_literal": ["causal_graphs", "biosynthetic_pathway"], "identifier": "CHEBI:155910", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-d.yaml", "standard_inchi_key": "IIQOUDJDCRTCJY-MBNYWOFBSA-N"}, {"declared_mechanism_roots_literal": [], "identifier": "naturalproductmech:mibig-0e7dc695d0", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/asperaculane-a.yaml", "standard_inchi_key": "JDBMOJWYGWGAIH-DZBCAUDPSA-N"}, {"declared_mechanism_roots_literal": [], "identifier": "naturalproductmech:mibig-d4c2d69c3b", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/asperaculane-b.yaml", "standard_inchi_key": "GFYHPKUYDFUKNL-MBNYWOFBSA-N"}] |
| bgc-2263-companion-2 | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/2/input; /contexts/2/complete_raw_text; /contexts/2/complete_raw_history | supports | Complete direct companion plaintext and history, retained as separate owner CHEBI:156057 with full key LOOAMPJDSIVZQC-IEZWGBDMSA-N. Source reading is attributed in the source notes; no congener claim transfer. |
| bgc-2263-companion-3 | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/3/input; /contexts/3/complete_raw_text; /contexts/3/complete_raw_history | supports | Complete direct companion plaintext and history, retained as separate owner CHEBI:156056 with full key DLPUOZGNMZKXKB-YEWFCNIMSA-N. Source reading is attributed in the source notes; no congener claim transfer. |
| bgc-2263-companion-5 | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/5/input; /contexts/5/complete_raw_text; /contexts/5/complete_raw_history | supports | Complete direct companion plaintext and history, retained as separate owner CHEBI:155910 with full key IIQOUDJDCRTCJY-MBNYWOFBSA-N. Source reading is attributed in the source notes; no congener claim transfer. |
| bgc-2263-companion-10 | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/10/input; /contexts/10/complete_raw_text; /contexts/10/complete_raw_history | supports | Complete direct companion plaintext and history, retained as separate owner naturalproductmech:mibig-0e7dc695d0 with full key JDBMOJWYGWGAIH-DZBCAUDPSA-N. Source reading is attributed in the source notes; no congener claim transfer. |
| bgc-2263-companion-11 | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/11/input; /contexts/11/complete_raw_text; /contexts/11/complete_raw_history | supports | Complete direct companion plaintext and history, retained as separate owner naturalproductmech:mibig-d4c2d69c3b with full key GFYHPKUYDFUKNL-MBNYWOFBSA-N. Source reading is attributed in the source notes; no congener claim transfer. |
| bgc-2263-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/11; /cached_taxonomy/whole_stanzas/12 | supports | Complete retained OBO stanzas for source taxa; no fresh taxonomy or ancestry inference: [{"complete_stanza": "[Term]\nid: NCBITaxon:5053\nname: Aspergillus aculeatus\nsynonym: \"Aspergillus japonicus var. aculeatus\" EXACT []\n\n", "id": "NCBITaxon:5053", "physical_line": 7851}, {"complete_stanza": "[Term]\nid: NCBITaxon:690307\nname: Aspergillus aculeatus ATCC 16872\n\n", "id": "NCBITaxon:690307", "physical_line": 107651}, {"complete_stanza": "[Term]\nid: NCBITaxon:1808020\nname: Penicillium sp. SCS-KFD08\n\n", "id": "NCBITaxon:1808020", "physical_line": 138630}] |
| bgc-2263-source-routes | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/source_taxa; /contexts/4/source_scope_inventory/forward_taxon_merge_matches; /contexts/4/source_scope_inventory/nonorganism_matches; /contexts/4/source_scope_inventory/actual_assay_rows; /contexts/4/source_scope_inventory/blank_AID_sentinels; /contexts/4/source_scope_inventory/related_corpus_rows | supports | Exact retained route sets, distinguishing nonempty source taxa from empty forward/nonorganism matches and blank sentinels from actual assays: {"actual_assay_rows": [], "blank_AID_sentinels": [{"last_physical_line": 8042, "physical_line": 8042, "raw_tsv_record": "UCCFSWQSMDQYHO-GXTWGEPZSA-N\t139586350\t\t(no assay data)\t\t\t\t\t\t\t\n", "row": {"activity_name": "", "activity_outcome": "", "activity_value_um": "", "aid": "", "assay_name": "(no assay data)", "assay_type": "", "cid": "139586350", "depositor": "", "reference": "", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "target_accession": ""}, "row_sha256": "a1457709246ed305f64eef40e31562108f90098c4a7c98e3559351f4d88536c0"}], "forward_taxon_merge_matches": [], "nonorganism_matches": [], "related_corpus_rows": [], "source_taxa": ["NCBITaxon:1808020", "NCBITaxon:5053", "NCBITaxon:690307"]} |
| bgc-2263-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/mibig_compounds | supports | Complete saved exact query frame with predicate, query and all 1 positive placements. {"matches": [{"last_physical_line": 2649, "physical_line": 2649, "raw_tsv_record": "BGC0002225\t3\tactive\tquestionable\tunknown\taculene C\t3\tCCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C\tInChI=1S/C14H18O2/c1-4-10-8-13(16)14(3)11(10)6-5-9(2)7-12(14)15/h5-6,8,12,15H,4,7H2,1-3H3/t12-,14+/m0/s1\tUCCFSWQSMDQYHO-GXTWGEPZSA-N\ttrue\t\tnpatlas:NPA011710&#124;pubchem:139586350\tNCBITaxon:690307\tAspergillus aculeatus ATCC 16872\tterpene\tUnknown\tKV878977.1\t1125505\t1144430\tHeterologous expression&#124;Knock-out studies\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tPMID:31618514\tENTRY\n", "row": {"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis": "CLUSTER_DEMONSTRATED", "compound_classes": "", "compound_index": "3", "compound_name": "aculene C", "database_ids": "npatlas:NPA011710&#124;pubchem:139586350", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "KV878977.1", "locus_evidence_methods": "Heterologous expression&#124;Knock-out studies", "locus_from": "1125505", "locus_to": "1144430", "mibig_accession": "BGC0002225", "primary_reference": "PMID:31618514", "producer_evidence_basis": "BGC_CHARACTERIZED", "reference_basis": "ENTRY", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C", "standard_inchi": "InChI=1S/C14H18O2/c1-4-10-8-13(16)14(3)11(10)6-5-9(2)7-12(14)15/h5-6,8,12,15H,4,7H2,1-3H3/t12-,14+/m0/s1", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC 16872"}, "row_sha256": "93b87b9d9d3552949c8a78eb31177d232b661e6b2d87bc11c34ff2adf6c25091"}], "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"} |
| bgc-2263-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2649–2649; row_sha256 93b87b9d9d3552949c8a78eb31177d232b661e6b2d87bc11c34ff2adf6c25091 | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis": "CLUSTER_DEMONSTRATED", "compound_classes": "", "compound_index": "3", "compound_name": "aculene C", "database_ids": "npatlas:NPA011710&#124;pubchem:139586350", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "KV878977.1", "locus_evidence_methods": "Heterologous expression&#124;Knock-out studies", "locus_from": "1125505", "locus_to": "1144430", "mibig_accession": "BGC0002225", "primary_reference": "PMID:31618514", "producer_evidence_basis": "BGC_CHARACTERIZED", "reference_basis": "ENTRY", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C", "standard_inchi": "InChI=1S/C14H18O2/c1-4-10-8-13(16)14(3)11(10)6-5-9(2)7-12(14)15/h5-6,8,12,15H,4,7H2,1-3H3/t12-,14+/m0/s1", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC 16872"}] |
| bgc-2263-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_structures | supports | Complete saved exact query frame with predicate, query and all 1 positive placements. {"matches": [{"last_physical_line": 42958, "physical_line": 42958, "raw_tsv_record": "CHEBI:155912\taculene C\tA sesquiterpenoid that is 8,8a-dihydroazulen-1(7H)-one substituted by an ethyl, methyl, hydroxy and methyl groups at positions 3, 6, 8S, and 8aR, respectively. It is a fungal metabolite isolated from Penicillium sp. SCS-KFD08 and Aspergillus aculeatus.\t3\tUCCFSWQSMDQYHO-GXTWGEPZSA-N\tCCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2O\n", "row": {"chebi_id": "CHEBI:155912", "definition": "A sesquiterpenoid that is 8,8a-dihydroazulen-1(7H)-one substituted by an ethyl, methyl, hydroxy and methyl groups at positions 3, 6, 8S, and 8aR, respectively. It is a fungal metabolite isolated from Penicillium sp. SCS-KFD08 and Aspergillus aculeatus.", "name": "aculene C", "smiles": "CCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2O", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "stars": "3"}, "row_sha256": "b45694373fca2241190cf9622ddb9a3a85ec7d3f000df17e47180cf008306e89"}], "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"} |
| bgc-2263-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line 1; physical lines 42958–42958; row_sha256 b45694373fca2241190cf9622ddb9a3a85ec7d3f000df17e47180cf008306e89 | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"chebi_id": "CHEBI:155912", "definition": "A sesquiterpenoid that is 8,8a-dihydroazulen-1(7H)-one substituted by an ethyl, methyl, hydroxy and methyl groups at positions 3, 6, 8S, and 8aR, respectively. It is a fungal metabolite isolated from Penicillium sp. SCS-KFD08 and Aspergillus aculeatus.", "name": "aculene C", "smiles": "CCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2O", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "stars": "3"}] |
| bgc-2263-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved exact query frame with predicate, query and all 1 positive placements. {"matches": [{"last_physical_line": 8639, "physical_line": 8639, "raw_tsv_record": "UCCFSWQSMDQYHO-GXTWGEPZSA-N\tAspergillus aculeatus\tNCBITaxon:5053\thttp://www.wikidata.org/entity/Q4807886\t10.3390/MOLECULES190810898\thttp://www.wikidata.org/entity/Q77504727\n", "row": {"organism_name": "Aspergillus aculeatus", "organism_wikidata": "http://www.wikidata.org/entity/Q4807886", "reference_doi": "10.3390/MOLECULES190810898", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q77504727", "taxon_id": "NCBITaxon:5053"}, "row_sha256": "b0f236eb3993fb6a3c8b120987468645b0bcf8e73009efbfc9583271969ba43e"}], "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"} |
| bgc-2263-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 8639–8639; row_sha256 b0f236eb3993fb6a3c8b120987468645b0bcf8e73009efbfc9583271969ba43e | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"organism_name": "Aspergillus aculeatus", "organism_wikidata": "http://www.wikidata.org/entity/Q4807886", "reference_doi": "10.3390/MOLECULES190810898", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q77504727", "taxon_id": "NCBITaxon:5053"}] |
| bgc-2263-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved exact query frame with predicate, query and all 0 positive placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"} |
| bgc-2263-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/npclassifier | supports | Complete saved exact query frame with predicate, query and all 1 positive placements. {"matches": [{"last_physical_line": 2373, "physical_line": 2373, "raw_tsv_record": "UCCFSWQSMDQYHO-GXTWGEPZSA-N\tCCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C\tTerpenoids\tSesquiterpenoids\tDaucane sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results": "Daucane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "superclass_results": "Sesquiterpenoids"}, "row_sha256": "06ebb48594f7e155c4543f863e4ba71410e2400d20e83d6da3a82c811e5b845f"}], "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"} |
| bgc-2263-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 2373–2373; row_sha256 06ebb48594f7e155c4543f863e4ba71410e2400d20e83d6da3a82c811e5b845f | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"class_results": "Daucane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "superclass_results": "Sesquiterpenoids"}] |
| bgc-2263-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved exact query frame with predicate, query and all 1 positive placements. {"matches": [{"last_physical_line": 8042, "physical_line": 8042, "raw_tsv_record": "UCCFSWQSMDQYHO-GXTWGEPZSA-N\t139586350\t\t(no assay data)\t\t\t\t\t\t\t\n", "row": {"activity_name": "", "activity_outcome": "", "activity_value_um": "", "aid": "", "assay_name": "(no assay data)", "assay_type": "", "cid": "139586350", "depositor": "", "reference": "", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "target_accession": ""}, "row_sha256": "a1457709246ed305f64eef40e31562108f90098c4a7c98e3559351f4d88536c0"}], "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"} |
| bgc-2263-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Header line 1; physical lines 8042–8042; row_sha256 a1457709246ed305f64eef40e31562108f90098c4a7c98e3559351f4d88536c0 | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"activity_name": "", "activity_outcome": "", "activity_value_um": "", "aid": "", "assay_name": "(no assay data)", "assay_type": "", "cid": "139586350", "depositor": "", "reference": "", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "target_accession": ""}] |
| bgc-2263-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved exact query frame with predicate, query and all 0 positive placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"} |
| bgc-2263-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved exact query frame with predicate, query and all 0 positive placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"} |
| bgc-2263-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_origins | supports | Complete saved exact query frame with predicate, query and all 2 positive placements. {"matches": [{"last_physical_line": 16908, "physical_line": 16908, "raw_tsv_record": "CHEBI:155912\tAspergillus aculeatus\t5053\tcell suspension culture\t\t25547729\t\n", "row": {"chebi_id": "CHEBI:155912", "comments": "", "component_text": "cell suspension culture", "source_accession": "25547729", "species_accession": "5053", "species_text": "Aspergillus aculeatus", "strain_text": ""}, "row_sha256": "6bbf1676d6eec4f936e595c9c5de89fef977ec97ddcfa3fbe0d7fe4bd57d2107"}, {"last_physical_line": 16909, "physical_line": 16909, "raw_tsv_record": "CHEBI:155912\tPenicillium sp. SCS-KFD08\t1808020\tcell suspension culture\t\t27709333\t\n", "row": {"chebi_id": "CHEBI:155912", "comments": "", "component_text": "cell suspension culture", "source_accession": "27709333", "species_accession": "1808020", "species_text": "Penicillium sp. SCS-KFD08", "strain_text": ""}, "row_sha256": "683a9b731097c565487488adb9981320667023484175014e0054a3a4e7aa17cd"}], "predicate": "exact chebi_id from exact full-key structure rows", "query": ["CHEBI:155912"]} |
| bgc-2263-source-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Header line 1; physical lines 16908–16908; row_sha256 6bbf1676d6eec4f936e595c9c5de89fef977ec97ddcfa3fbe0d7fe4bd57d2107; physical lines 16909–16909; row_sha256 683a9b731097c565487488adb9981320667023484175014e0054a3a4e7aa17cd | supports | Complete retained physical source rows (all fields), read and joined to the current pinned table: [{"chebi_id": "CHEBI:155912", "comments": "", "component_text": "cell suspension culture", "source_accession": "25547729", "species_accession": "5053", "species_text": "Aspergillus aculeatus", "strain_text": ""}, {"chebi_id": "CHEBI:155912", "comments": "", "component_text": "cell suspension culture", "source_accession": "27709333", "species_accession": "1808020", "species_text": "Penicillium sp. SCS-KFD08", "strain_text": ""}] |
| bgc-2263-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure distinguishes normalized identity and unspecified stereochemistry. ComputedClassification is explicitly a named/versioned prediction, never a source assertion or record-admission reason. |
| bgc-2263-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | The maintained extractor derives the stereo_complete flag from unassigned chiral centres; no new extractor call occurred in this review. |
| bgc-2263-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 971–1037 | supports | The seeder retains the exact structure/definition source and copies named NPClassifier results including is_glycoside. A prediction is not promoted to experimental evidence. |
| bgc-2263-origin-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 1093–1151 | supports | Producer evidence and locus methods/link grades remain separately copied; merges and applicable local qualifications have distinct handling. |
| bgc-2263-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole profile | supports | Current review profile requires one-record identity, evidence, provenance, representation and completion dimensions without promoting unavailable verification. |
| bgc-2263-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole review skill | supports | Current one-record review scope distinguishes local evidence review from scientific completeness, preserves source records, and requires concrete supported findings. |
| bgc-2263-reader-DATA | /private/tmp/npm-review-work/shared-next-batch227/native-current227-aculene-c-maintained-reader-DATA-001.json; /resolved_view; /review_check_metadata | supports | The original maintained reader preserves the complete captured owner, including one graph with three nodes/two edges, one pathway entry and all three history events. The resolved view and exact check metadata do not freshly validate the historical mechanism evidence. |
| bgc-2263-reader-execution | /private/tmp/npm-review-work/shared-next-batch227/native-current227-aculene-c-reader-execution-001.json; /exit_code; /stdout; /stderr; /external_requests; /retries | supports | Original Native-owned maintained reader returned zero once; exact streams, no retries and no external requests are retained. |
| bgc-2263-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch227/root-2263-maintained-reader-acceptance-001.json; /review_check_contract; /verification; /limits | supports | ROOT accepts the exact original complete-owner result and its current dependencies; the check contract is authoritative for this maintained-reader check. |
| bgc-2263-causal_graphs-complete | /private/tmp/npm-review-work/shared-next-batch227/native-current227-aculene-c-maintained-reader-DATA-001.json; /resolved_view/causal_graphs | supports | Complete retained causal_graphs content, with historical evidence grades and limitations rather than new verification: [{"description": "Partial A. aculeatus aculene C biosynthesis graph for AneA-catalyzed desaturation of aculene D.", "edges": [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "Lee et al. identified the Aspergillus aculeatus aculene biosynthetic gene cluster, inactivated aneA, and used Saccharomyces cerevisiae and Aspergillus oryzae heterologous reconstitution to connect AneA to 5,6-desaturation of aculene D into aculene C.", "reference": "DOI:10.1002/anie.201910200", "snippet": "characterized the biosynthetic pathway based on gene inactivation, feeding experiments, and heterologous reconstitution"}, {"evidence_type": "REVIEW", "notes": "Wang et al. summarize Lee et al.'s aneA deletion phenotype and place AneA after A. oryzae reconstitution of AneC/F/D/G to aculene D in the published aculene A-C pathway.", "reference": "DOI:10.1039/D1NP00074H", "snippet": "the unsaturation is catalyzed by AneA"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002225.3 maps the A. aculeatus ATCC 16872 KV878977 aculene region to CDS OJJ99912.1 at locus ASPACDRAFT_119783.", "reference": "https://mibig.secondarymetabolites.org/repository/BGC0002225.3/BGC0002225.gbk", "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "Reviewed UniProtKB:A0A1L9WUX8 is the 298 aa A. aculeatus ATCC 16872 Dioxygenase aneA, cross-references KV878977 protein OJJ99912.1, and annotates RHEA:65112 from PMID:31618514.", "reference": "https://www.uniprot.org/uniprotkb/A0A1L9WUX8", "retrieved_on": "2026-09-30", "snippet": "The dioxygenase aneA converts aculene D into aculene C"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "The Rhea Swiss-Prot mapping links UniProtKB:A0A1L9WUX8 to RHEA:65112, the aculene D 2-oxoglutarate-dependent desaturation reaction.", "reference": "https://ftp.expasy.org/databases/rhea/tsv/rhea2uniprot_sprot.tsv", "retrieved_on": "2026-09-30"}], "notes": "AneA desaturates aculene D between C5 and C6.", "object": "anea", "predicate": "is desaturated by", "subject": "aculene_d"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "Lee et al. identified the Aspergillus aculeatus aculene biosynthetic gene cluster, inactivated aneA, and used Saccharomyces cerevisiae and Aspergillus oryzae heterologous reconstitution to connect AneA to 5,6-desaturation of aculene D into aculene C.", "reference": "DOI:10.1002/anie.201910200", "snippet": "characterized the biosynthetic pathway based on gene inactivation, feeding experiments, and heterologous reconstitution"}, {"evidence_type": "REVIEW", "notes": "Wang et al. summarize Lee et al.'s aneA deletion phenotype and place AneA after A. oryzae reconstitution of AneC/F/D/G to aculene D in the published aculene A-C pathway.", "reference": "DOI:10.1039/D1NP00074H", "snippet": "the unsaturation is catalyzed by AneA"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002225.3 maps the A. aculeatus ATCC 16872 KV878977 aculene region to CDS OJJ99912.1 at locus ASPACDRAFT_119783.", "reference": "https://mibig.secondarymetabolites.org/repository/BGC0002225.3/BGC0002225.gbk", "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "Reviewed UniProtKB:A0A1L9WUX8 is the 298 aa A. aculeatus ATCC 16872 Dioxygenase aneA, cross-references KV878977 protein OJJ99912.1, and annotates RHEA:65112 from PMID:31618514.", "reference": "https://www.uniprot.org/uniprotkb/A0A1L9WUX8", "retrieved_on": "2026-09-30", "snippet": "The dioxygenase aneA converts aculene D into aculene C"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "The Rhea Swiss-Prot mapping links UniProtKB:A0A1L9WUX8 to RHEA:65112, the aculene D 2-oxoglutarate-dependent desaturation reaction.", "reference": "https://ftp.expasy.org/databases/rhea/tsv/rhea2uniprot_sprot.tsv", "retrieved_on": "2026-09-30"}], "notes": "The AneA dioxygenase reaction yields aculene C from aculene D.", "object": "aculene_c", "predicate": "forms", "subject": "anea"}], "graph_id": "aculene-c-anea-desaturation", "nodes": [{"grounding_status": "GROUNDED", "identifier": "CHEBI:155910", "label": "aculene D", "node_id": "aculene_d", "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED", "identifier": "UniProtKB:A0A1L9WUX8", "label": "AneA aculene D dioxygenase", "node_id": "anea", "node_type": "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:155912", "label": "aculene C", "node_id": "aculene_c", "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"}] |
| bgc-2263-biosynthetic_pathway-complete | /private/tmp/npm-review-work/shared-next-batch227/native-current227-aculene-c-maintained-reader-DATA-001.json; /resolved_view/biosynthetic_pathway | supports | Complete retained biosynthetic_pathway content, with historical evidence grades and limitations rather than new verification: [{"enzyme_id": "UniProtKB:A0A1L9WUX8", "enzyme_label": "AneA aculene D dioxygenase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "Lee et al. identified the Aspergillus aculeatus aculene biosynthetic gene cluster, inactivated aneA, and used Saccharomyces cerevisiae and Aspergillus oryzae heterologous reconstitution to connect AneA to 5,6-desaturation of aculene D into aculene C.", "reference": "DOI:10.1002/anie.201910200", "snippet": "characterized the biosynthetic pathway based on gene inactivation, feeding experiments, and heterologous reconstitution"}, {"evidence_type": "REVIEW", "notes": "Wang et al. summarize Lee et al.'s aneA deletion phenotype and place AneA after A. oryzae reconstitution of AneC/F/D/G to aculene D in the published aculene A-C pathway.", "reference": "DOI:10.1039/D1NP00074H", "snippet": "the unsaturation is catalyzed by AneA"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002225.3 maps the A. aculeatus ATCC 16872 KV878977 aculene region to CDS OJJ99912.1 at locus ASPACDRAFT_119783.", "reference": "https://mibig.secondarymetabolites.org/repository/BGC0002225.3/BGC0002225.gbk", "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "Reviewed UniProtKB:A0A1L9WUX8 is the 298 aa A. aculeatus ATCC 16872 Dioxygenase aneA, cross-references KV878977 protein OJJ99912.1, and annotates RHEA:65112 from PMID:31618514.", "reference": "https://www.uniprot.org/uniprotkb/A0A1L9WUX8", "retrieved_on": "2026-09-30", "snippet": "The dioxygenase aneA converts aculene D into aculene C"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "The Rhea Swiss-Prot mapping links UniProtKB:A0A1L9WUX8 to RHEA:65112, the aculene D 2-oxoglutarate-dependent desaturation reaction.", "reference": "https://ftp.expasy.org/databases/rhea/tsv/rhea2uniprot_sprot.tsv", "retrieved_on": "2026-09-30"}], "notes": "AneA introduces the 5,6-alkene into aculene D to form aculene C; RHEA:65112 grounds the full 2-oxoglutarate- and O2-dependent dioxygenase reaction.", "products": ["CHEBI:155912", "CHEBI:30031", "CHEBI:16526", "CHEBI:15377"], "reaction_id": "RHEA:65112", "step_number": 1, "substrates": ["CHEBI:155910", "CHEBI:16810", "CHEBI:15379"]}] |
| bgc-2263-curation_history-complete | /private/tmp/npm-review-work/shared-next-batch227/native-current227-aculene-c-maintained-reader-DATA-001.json; /resolved_view/curation_history | supports | Complete retained curation_history content, with historical evidence grades and limitations rather than new verification: [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:13Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:27Z"}, {"action": "ADD_BIOSYNTHETIC_PROTEIN_GRAPH", "changes": "Added exact UniProtKB:A0A1L9WUX8 AneA grounding, the RHEA:65112 aculene D desaturation step, and a BIOSYNTHESIS causal graph for aculene C.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-30T15:14:56Z"}] |
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
review_id: 20261103T173401Z-aculene-c
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: aculene C'
started_at: '2026-11-03T17:10:56.590299Z'
finished_at: '2026-11-03T17:34:01.055377Z'
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
summary: Aculene C retains a consistent full-key identity, two specified centres and
  a partial historical AneA conversion from aculene D. Producer, occurrence and source
  grades remain separate; reader preservation does not establish fresh primary support.
  Scientific completion remains partial.
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
    role: context
  - path: data/natural_products/terpenoids/aculene-b.yaml
    sha256: 2f85a5ba0c8c4e73048d53e7189562ad9ec6274c328a3d54e6d714cb13b2cbf1
    role: context
  - path: data/natural_products/terpenoids/aculene-c.yaml
    sha256: 97baa4b9ddc30459f9513d453485eeb4fff412afe057e658192e0ba54ef62653
    role: target
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
  - path: src/naturalproductmech/graph_components.py
    sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: src/naturalproductmech/validation/write_validated.py
    sha256: 4b7648fc5d2e7a5d26ad8bb168dbcae609aaa2694434a8ed5cfcb33fb66ff80a
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2263; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:155912
targets:
- target_id: CHEBI:155912
  path: data/natural_products/terpenoids/aculene-c.yaml
  label: aculene C
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
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/terpenoids/aculene-c.yaml
    role: Curator-owned declared graphs, graph references, pathway steps and history;
      imported molecular-target assertions and other seeded fields retain inventory
      ownership. Curated graph/pathway changes require the validated writer and a
      curation event.
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners. This mechanism-bearing owner requires separately
    authorized complete maintained resolution before scientific assessment and draft
    assembly. Raw owner capture is not a maintained resolved view.
checks:
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for aculene C
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch227/read-selected-mechanism-guarded-001.py
    2263 2c1354901c89ced9f3b78249933ea91ee8a67da8453ae2b5fafac9a8138be74c 1217577c8a8fe5c95b549529e115504249ca3bca00015a75f356c0d565df800e
    83618dd2b5359705b73a8c2f7455bed442da451e34e7a850139a7205be9b3f9f 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
    b8839ae73bf6cc45d3a8252e13f3f01080d55c93ac8beb8533e93c11693ab350
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CHEBI:155912
  evidence_ids:
  - bgc-2263-reader-DATA
  - bgc-2263-reader-execution
  - bgc-2263-reader-acceptance
  summary: One original offline maintained call preserved the complete owner and historically
    attributed mechanism content. Mechanical preservation is distinct from fresh scientific
    validation.
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:155912
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
  - CHEBI:155912
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
  - CHEBI:155912
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
  - CHEBI:155912
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
  - CHEBI:155912
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
  - CHEBI:155912
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:155912
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:155912
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2263-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/aculene-c.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete current owner and its 3 ordered history events, personally read.
    Native curation_status remains SEEDED.
  snapshot_sha256: 97baa4b9ddc30459f9513d453485eeb4fff412afe057e658192e0ba54ef62653
- evidence_id: bgc-2263-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/2/owner_pin; /records/2/owner_document
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Exact captured owner, including all written nonmechanistic fields, roots
    and history.
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2263-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/intakes/2263-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Actual one-record canonical inspection with 44 source inputs and target
    CHEBI:155912; current owner and context roles are retained.
  snapshot_sha256: 1217577c8a8fe5c95b549529e115504249ca3bca00015a75f356c0d565df800e
- evidence_id: bgc-2263-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/root-intake-ready-001.json
  locator: /accepted; /intake_summary; /verification
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ROOT accepts all ten original canonical intakes, their exact target/source
    maps and current dependency pins.
  snapshot_sha256: 8a1dce2c5b8f17939c216983455dbc1ebad823ae10e6bd9cce0c093a142af697
- evidence_id: bgc-2263-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/2/owner_document/identifier; /records/2/owner_document/label;
    /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts;
    /records/2/owner_document/grounding_status; /records/2/owner_document/definition;
    /records/2/owner_document/definition_source
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Written identity/structure/grounding fields and definition when present:
    {"chemical_structure": {"smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C", "standard_inchi":
    "InChI=1S/C14H18O2/c1-4-10-8-13(16)14(3)11(10)6-5-9(2)7-12(14)15/h5-6,8,12,15H,4,7H2,1-3H3/t12-,14+/m0/s1",
    "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002225"}, "definition":
    "A sesquiterpenoid that is 8,8a-dihydroazulen-1(7H)-one substituted by an ethyl,
    methyl, hydroxy and methyl groups at positions 3, 6, 8S, and 8aR, respectively.
    It is a fungal metabolite isolated from Penicillium sp. SCS-KFD08 and Aspergillus
    aculeatus.", "definition_source": "CHEBI:155912", "grounding_status": "EXACT",
    "identifier": "CHEBI:155912", "label": "aculene C", "source_concepts": [{"minted_identifier":
    "naturalproductmech:mibig-9c98bc7a0d", "source": "MIBIG", "source_id": "BGC0002225",
    "source_label": "aculene C", "source_version": "3"}, {"minted_identifier": "naturalproductmech:chebi-fc49794a70",
    "source": "CHEBI", "source_id": "CHEBI:155912", "source_label": "aculene C", "source_version":
    "3-star"}]}'
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2263-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters;
    /records/2/owner_document/producer_taxon_groups; /records/2/owner_document/bgc_class
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
- evidence_id: bgc-2263-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: The complete captured owner has no bioactivities or molecular_targets root.
    It retains one biosynthetic graph and one pathway entry.
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2263-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/2/owner_document/occurrences; /records/2/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'All written occurrences and occurrence groups: {"occurrence_taxon_groups":
    ["FUNGAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "ChEBI compound origin for CHEBI:155912", "reference": "PMID:27709333"}],
    "notes": "cell suspension culture", "source": "CHEBI", "taxon_id": "NCBITaxon:1808020",
    "taxon_label": "Penicillium sp. SCS-KFD08", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.3390/MOLECULES190810898"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q4807886", "source":
    "LOTUS", "taxon_id": "NCBITaxon:5053", "taxon_label": "Aspergillus aculeatus",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "ChEBI compound origin for CHEBI:155912", "reference": "PMID:25547729"}],
    "notes": "cell suspension culture", "source": "CHEBI", "taxon_id": "NCBITaxon:5053",
    "taxon_label": "Aspergillus aculeatus", "taxon_source": "NCBITaxon"}]}'
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2263-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_pathway; /records/2/owner_document/np_classification;
    /records/2/owner_document/bgc_class
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Literal written model/version/results and separate source BGC classification:
    {"bgc_class": ["TERPENE"], "np_classification": {"class_results": ["Daucane sesquiterpenoids"],
    "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results":
    ["Sesquiterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS"}'
  snapshot_sha256: 9d49efe4d919c526ff2bebd821217647650195b32d951150f15b9f3bc7913026
- evidence_id: bgc-2263-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/smiles/status; /records/2/inchi/status;
    /records/2/smiles/computed; /records/2/inchi/computed; /records/2/comparisons;
    /records/2/atom_correspondence
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Both saved forms parsed. They give C14H18O2, charge 0, 16 atoms and 17
    bonds each. All ten comparison flags are true; a complete stored chirality-aware
    correspondence is retained, with full_graph_identity_established:false. Stereo
    counts: {"Atom_Tetrahedral:Specified": 2}.'
  snapshot_sha256: 310fb39c1a9fad6c657cd7aa0986819b02834117d6db86c6b88fd2ddc774a9f2
- evidence_id: bgc-2263-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/smiles/computed; /records/2/inchi/computed; /records/2/atom_correspondence
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: SMILES C4(=O5) is the ketone, C12–OH13 the alcohol and C7=C8 the additional
    core double bond. The fused rings are [2,3,4,6,7] and [8,7,6,12,11,10,9]. Saved
    motifs and all atom/bond rows show no ester, amide or sugar linkage.
  snapshot_sha256: 310fb39c1a9fad6c657cd7aa0986819b02834117d6db86c6b88fd2ddc774a9f2
- evidence_id: bgc-2263-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /external_requests
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: The original ROOT-owned diagnostic execution returned zero and retained
    its command and exact stdout/stderr pins; stderr is empty and no external request
    is reported.
  snapshot_sha256: cd7c3ddbf99f1e149846db81d2e8927177241049dc9316408da347ef0b73d8c6
- evidence_id: bgc-2263-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/root-local-diagnostics-acceptance-001.json
  locator: /accepted; /DATA; /execution; /verification; /limits
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ROOT accepts the original saved 20-form diagnostic and current inputs;
    its mechanical comparison and preservation checks do not establish fresh natural
    identity.
  snapshot_sha256: 14967c4d38b8f806e2c49ea51068afd81aa23e83df4ac04f451efd2729cbba96
- evidence_id: bgc-2263-native-acceptance
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
- evidence_id: bgc-2263-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/root-source-inventory-acceptance-001.json
  locator: /accepted; /inventory
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ROOT accepts this exact saved inventory. Source-payload interpretation
    is separately attributed in the source notes.
  snapshot_sha256: eb38369e8b3d32ba55eaa5ceedfe21446cc123c911691cab66901e7e2bf1f99a
- evidence_id: bgc-2263-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-target-input-plan-001.json
  locator: /records/2; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Accepted source plan retains this record and its exact input projection,
    within the batch totals of 418 placements and 53 paths.
  snapshot_sha256: 5537c37fdf8a54893bcbd0c967e1d857f8ac7004044a38e11d9ce2174146ba11
- evidence_id: bgc-2263-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/root-input-plan-acceptance-001.json
  locator: /accepted; /input_plan; /notes; /verification
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ROOT accepts the actual composed source plan and pinned source-reading
    notes with exact source/current input joins.
  snapshot_sha256: eca63a2e032e35c9bb8f233056b0bc6257aad535a61d7fdc9b33db1aa7f1b302
- evidence_id: bgc-2263-source-notes
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
- evidence_id: bgc-2263-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /records/2/direct_companion_predicates; /contexts/2/identifier; /contexts/2/standard_inchi_key;
    /contexts/2/owned_bgc_ids; /contexts/2/declared_mechanism_roots_literal; /contexts/3/identifier;
    /contexts/3/standard_inchi_key; /contexts/3/owned_bgc_ids; /contexts/3/declared_mechanism_roots_literal;
    /contexts/5/identifier; /contexts/5/standard_inchi_key; /contexts/5/owned_bgc_ids;
    /contexts/5/declared_mechanism_roots_literal; /contexts/10/identifier; /contexts/10/standard_inchi_key;
    /contexts/10/owned_bgc_ids; /contexts/10/declared_mechanism_roots_literal; /contexts/11/identifier;
    /contexts/11/standard_inchi_key; /contexts/11/owned_bgc_ids; /contexts/11/declared_mechanism_roots_literal
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Exact one-hop predicate and owner profiles; these do not transfer identity,
    activity or mechanism: [{"declared_mechanism_roots_literal": [], "identifier":
    "CHEBI:156057", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-a.yaml",
    "standard_inchi_key": "LOOAMPJDSIVZQC-IEZWGBDMSA-N"}, {"declared_mechanism_roots_literal":
    [], "identifier": "CHEBI:156056", "owned_bgc_ids": ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-b.yaml",
    "standard_inchi_key": "DLPUOZGNMZKXKB-YEWFCNIMSA-N"}, {"declared_mechanism_roots_literal":
    ["causal_graphs", "biosynthetic_pathway"], "identifier": "CHEBI:155910", "owned_bgc_ids":
    ["BGC0002225"], "path": "data/natural_products/terpenoids/aculene-d.yaml", "standard_inchi_key":
    "IIQOUDJDCRTCJY-MBNYWOFBSA-N"}, {"declared_mechanism_roots_literal": [], "identifier":
    "naturalproductmech:mibig-0e7dc695d0", "owned_bgc_ids": ["BGC0002225"], "path":
    "data/natural_products/terpenoids/asperaculane-a.yaml", "standard_inchi_key":
    "JDBMOJWYGWGAIH-DZBCAUDPSA-N"}, {"declared_mechanism_roots_literal": [], "identifier":
    "naturalproductmech:mibig-d4c2d69c3b", "owned_bgc_ids": ["BGC0002225"], "path":
    "data/natural_products/terpenoids/asperaculane-b.yaml", "standard_inchi_key":
    "GFYHPKUYDFUKNL-MBNYWOFBSA-N"}]'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-companion-2
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/2/input; /contexts/2/complete_raw_text; /contexts/2/complete_raw_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete direct companion plaintext and history, retained as separate owner
    CHEBI:156057 with full key LOOAMPJDSIVZQC-IEZWGBDMSA-N. Source reading is attributed
    in the source notes; no congener claim transfer.
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-companion-3
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/3/input; /contexts/3/complete_raw_text; /contexts/3/complete_raw_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete direct companion plaintext and history, retained as separate owner
    CHEBI:156056 with full key DLPUOZGNMZKXKB-YEWFCNIMSA-N. Source reading is attributed
    in the source notes; no congener claim transfer.
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-companion-5
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/5/input; /contexts/5/complete_raw_text; /contexts/5/complete_raw_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete direct companion plaintext and history, retained as separate owner
    CHEBI:155910 with full key IIQOUDJDCRTCJY-MBNYWOFBSA-N. Source reading is attributed
    in the source notes; no congener claim transfer.
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-companion-10
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/10/input; /contexts/10/complete_raw_text; /contexts/10/complete_raw_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete direct companion plaintext and history, retained as separate owner
    naturalproductmech:mibig-0e7dc695d0 with full key JDBMOJWYGWGAIH-DZBCAUDPSA-N.
    Source reading is attributed in the source notes; no congener claim transfer.
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-companion-11
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/11/input; /contexts/11/complete_raw_text; /contexts/11/complete_raw_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Complete direct companion plaintext and history, retained as separate owner
    naturalproductmech:mibig-d4c2d69c3b with full key GFYHPKUYDFUKNL-MBNYWOFBSA-N.
    Source reading is attributed in the source notes; no congener claim transfer.
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/11;
    /cached_taxonomy/whole_stanzas/12
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained OBO stanzas for source taxa; no fresh taxonomy or ancestry
    inference: [{"complete_stanza": "[Term]\nid: NCBITaxon:5053\nname: Aspergillus
    aculeatus\nsynonym: \"Aspergillus japonicus var. aculeatus\" EXACT []\n\n", "id":
    "NCBITaxon:5053", "physical_line": 7851}, {"complete_stanza": "[Term]\nid: NCBITaxon:690307\nname:
    Aspergillus aculeatus ATCC 16872\n\n", "id": "NCBITaxon:690307", "physical_line":
    107651}, {"complete_stanza": "[Term]\nid: NCBITaxon:1808020\nname: Penicillium
    sp. SCS-KFD08\n\n", "id": "NCBITaxon:1808020", "physical_line": 138630}]'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/source_taxa; /contexts/4/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/4/source_scope_inventory/nonorganism_matches; /contexts/4/source_scope_inventory/actual_assay_rows;
    /contexts/4/source_scope_inventory/blank_AID_sentinels; /contexts/4/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Exact retained route sets, distinguishing nonempty source taxa from empty
    forward/nonorganism matches and blank sentinels from actual assays: {"actual_assay_rows":
    [], "blank_AID_sentinels": [{"last_physical_line": 8042, "physical_line": 8042,
    "raw_tsv_record": "UCCFSWQSMDQYHO-GXTWGEPZSA-N\t139586350\t\t(no assay data)\t\t\t\t\t\t\t\n",
    "row": {"activity_name": "", "activity_outcome": "", "activity_value_um": "",
    "aid": "", "assay_name": "(no assay data)", "assay_type": "", "cid": "139586350",
    "depositor": "", "reference": "", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N",
    "target_accession": ""}, "row_sha256": "a1457709246ed305f64eef40e31562108f90098c4a7c98e3559351f4d88536c0"}],
    "forward_taxon_merge_matches": [], "nonorganism_matches": [], "related_corpus_rows":
    [], "source_taxa": ["NCBITaxon:1808020", "NCBITaxon:5053", "NCBITaxon:690307"]}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 1 positive
    placements. {"matches": [{"last_physical_line": 2649, "physical_line": 2649, "raw_tsv_record":
    "BGC0002225\t3\tactive\tquestionable\tunknown\taculene C\t3\tCCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C\tInChI=1S/C14H18O2/c1-4-10-8-13(16)14(3)11(10)6-5-9(2)7-12(14)15/h5-6,8,12,15H,4,7H2,1-3H3/t12-,14+/m0/s1\tUCCFSWQSMDQYHO-GXTWGEPZSA-N\ttrue\t\tnpatlas:NPA011710|pubchem:139586350\tNCBITaxon:690307\tAspergillus
    aculeatus ATCC 16872\tterpene\tUnknown\tKV878977.1\t1125505\t1144430\tHeterologous
    expression|Knock-out studies\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tPMID:31618514\tENTRY\n",
    "row": {"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis":
    "CLUSTER_DEMONSTRATED", "compound_classes": "", "compound_index": "3", "compound_name":
    "aculene C", "database_ids": "npatlas:NPA011710|pubchem:139586350", "entry_completeness":
    "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version":
    "3", "genome_accession": "KV878977.1", "locus_evidence_methods": "Heterologous
    expression|Knock-out studies", "locus_from": "1125505", "locus_to": "1144430",
    "mibig_accession": "BGC0002225", "primary_reference": "PMID:31618514", "producer_evidence_basis":
    "BGC_CHARACTERIZED", "reference_basis": "ENTRY", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C",
    "standard_inchi": "InChI=1S/C14H18O2/c1-4-10-8-13(16)14(3)11(10)6-5-9(2)7-12(14)15/h5-6,8,12,15H,4,7H2,1-3H3/t12-,14+/m0/s1",
    "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC 16872"},
    "row_sha256": "93b87b9d9d3552949c8a78eb31177d232b661e6b2d87bc11c34ff2adf6c25091"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2649–2649; row_sha256 93b87b9d9d3552949c8a78eb31177d232b661e6b2d87bc11c34ff2adf6c25091
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"bgc_classes": "terpene", "bgc_subclasses": "Unknown",
    "cluster_link_evidence_basis": "CLUSTER_DEMONSTRATED", "compound_classes": "",
    "compound_index": "3", "compound_name": "aculene C", "database_ids": "npatlas:NPA011710|pubchem:139586350",
    "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status":
    "active", "entry_version": "3", "genome_accession": "KV878977.1", "locus_evidence_methods":
    "Heterologous expression|Knock-out studies", "locus_from": "1125505", "locus_to":
    "1144430", "mibig_accession": "BGC0002225", "primary_reference": "PMID:31618514",
    "producer_evidence_basis": "BGC_CHARACTERIZED", "reference_basis": "ENTRY", "smiles":
    "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C", "standard_inchi": "InChI=1S/C14H18O2/c1-4-10-8-13(16)14(3)11(10)6-5-9(2)7-12(14)15/h5-6,8,12,15H,4,7H2,1-3H3/t12-,14+/m0/s1",
    "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:690307", "taxon_label": "Aspergillus aculeatus ATCC 16872"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2263-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 1 positive
    placements. {"matches": [{"last_physical_line": 42958, "physical_line": 42958,
    "raw_tsv_record": "CHEBI:155912\taculene C\tA sesquiterpenoid that is 8,8a-dihydroazulen-1(7H)-one
    substituted by an ethyl, methyl, hydroxy and methyl groups at positions 3, 6,
    8S, and 8aR, respectively. It is a fungal metabolite isolated from Penicillium
    sp. SCS-KFD08 and Aspergillus aculeatus.\t3\tUCCFSWQSMDQYHO-GXTWGEPZSA-N\tCCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2O\n",
    "row": {"chebi_id": "CHEBI:155912", "definition": "A sesquiterpenoid that is 8,8a-dihydroazulen-1(7H)-one
    substituted by an ethyl, methyl, hydroxy and methyl groups at positions 3, 6,
    8S, and 8aR, respectively. It is a fungal metabolite isolated from Penicillium
    sp. SCS-KFD08 and Aspergillus aculeatus.", "name": "aculene C", "smiles": "CCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2O",
    "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "stars": "3"}, "row_sha256":
    "b45694373fca2241190cf9622ddb9a3a85ec7d3f000df17e47180cf008306e89"}], "predicate":
    "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-source-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line 1; physical lines 42958–42958; row_sha256 b45694373fca2241190cf9622ddb9a3a85ec7d3f000df17e47180cf008306e89
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"chebi_id": "CHEBI:155912", "definition": "A sesquiterpenoid
    that is 8,8a-dihydroazulen-1(7H)-one substituted by an ethyl, methyl, hydroxy
    and methyl groups at positions 3, 6, 8S, and 8aR, respectively. It is a fungal
    metabolite isolated from Penicillium sp. SCS-KFD08 and Aspergillus aculeatus.",
    "name": "aculene C", "smiles": "CCC1=CC(=O)[C@]2(C)C1=CC=C(C)C[C@@H]2O", "standard_inchi_key":
    "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "stars": "3"}]'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2263-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 1 positive
    placements. {"matches": [{"last_physical_line": 8639, "physical_line": 8639, "raw_tsv_record":
    "UCCFSWQSMDQYHO-GXTWGEPZSA-N\tAspergillus aculeatus\tNCBITaxon:5053\thttp://www.wikidata.org/entity/Q4807886\t10.3390/MOLECULES190810898\thttp://www.wikidata.org/entity/Q77504727\n",
    "row": {"organism_name": "Aspergillus aculeatus", "organism_wikidata": "http://www.wikidata.org/entity/Q4807886",
    "reference_doi": "10.3390/MOLECULES190810898", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q77504727", "taxon_id":
    "NCBITaxon:5053"}, "row_sha256": "b0f236eb3993fb6a3c8b120987468645b0bcf8e73009efbfc9583271969ba43e"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-source-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 8639–8639; row_sha256 b0f236eb3993fb6a3c8b120987468645b0bcf8e73009efbfc9583271969ba43e
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"organism_name": "Aspergillus aculeatus", "organism_wikidata":
    "http://www.wikidata.org/entity/Q4807886", "reference_doi": "10.3390/MOLECULES190810898",
    "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q77504727",
    "taxon_id": "NCBITaxon:5053"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2263-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 0 positive
    placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality",
    "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 1 positive
    placements. {"matches": [{"last_physical_line": 2373, "physical_line": 2373, "raw_tsv_record":
    "UCCFSWQSMDQYHO-GXTWGEPZSA-N\tCCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C\tTerpenoids\tSesquiterpenoids\tDaucane
    sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results":
    "Daucane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C",
    "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "superclass_results": "Sesquiterpenoids"},
    "row_sha256": "06ebb48594f7e155c4543f863e4ba71410e2400d20e83d6da3a82c811e5b845f"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 2373–2373; row_sha256 06ebb48594f7e155c4543f863e4ba71410e2400d20e83d6da3a82c811e5b845f
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"class_results": "Daucane sesquiterpenoids", "is_glycoside":
    "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results":
    "Terpenoids", "smiles": "CCC1=CC(=O)[C@@]2(C1=CC=C(C[C@@H]2O)C)C", "standard_inchi_key":
    "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "superclass_results": "Sesquiterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2263-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 1 positive
    placements. {"matches": [{"last_physical_line": 8042, "physical_line": 8042, "raw_tsv_record":
    "UCCFSWQSMDQYHO-GXTWGEPZSA-N\t139586350\t\t(no assay data)\t\t\t\t\t\t\t\n", "row":
    {"activity_name": "", "activity_outcome": "", "activity_value_um": "", "aid":
    "", "assay_name": "(no assay data)", "assay_type": "", "cid": "139586350", "depositor":
    "", "reference": "", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N", "target_accession":
    ""}, "row_sha256": "a1457709246ed305f64eef40e31562108f90098c4a7c98e3559351f4d88536c0"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-source-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Header line 1; physical lines 8042–8042; row_sha256 a1457709246ed305f64eef40e31562108f90098c4a7c98e3559351f4d88536c0
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"activity_name": "", "activity_outcome": "", "activity_value_um":
    "", "aid": "", "assay_name": "(no assay data)", "assay_type": "", "cid": "139586350",
    "depositor": "", "reference": "", "standard_inchi_key": "UCCFSWQSMDQYHO-GXTWGEPZSA-N",
    "target_accession": ""}]'
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2263-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 0 positive
    placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality",
    "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 0 positive
    placements. {"matches": [], "predicate": "exact complete standard_inchi_key equality",
    "query": "UCCFSWQSMDQYHO-GXTWGEPZSA-N"}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227-tentative/bgc-prep/bgc-conditional227-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete saved exact query frame with predicate, query and all 2 positive
    placements. {"matches": [{"last_physical_line": 16908, "physical_line": 16908,
    "raw_tsv_record": "CHEBI:155912\tAspergillus aculeatus\t5053\tcell suspension
    culture\t\t25547729\t\n", "row": {"chebi_id": "CHEBI:155912", "comments": "",
    "component_text": "cell suspension culture", "source_accession": "25547729", "species_accession":
    "5053", "species_text": "Aspergillus aculeatus", "strain_text": ""}, "row_sha256":
    "6bbf1676d6eec4f936e595c9c5de89fef977ec97ddcfa3fbe0d7fe4bd57d2107"}, {"last_physical_line":
    16909, "physical_line": 16909, "raw_tsv_record": "CHEBI:155912\tPenicillium sp.
    SCS-KFD08\t1808020\tcell suspension culture\t\t27709333\t\n", "row": {"chebi_id":
    "CHEBI:155912", "comments": "", "component_text": "cell suspension culture", "source_accession":
    "27709333", "species_accession": "1808020", "species_text": "Penicillium sp. SCS-KFD08",
    "strain_text": ""}, "row_sha256": "683a9b731097c565487488adb9981320667023484175014e0054a3a4e7aa17cd"}],
    "predicate": "exact chebi_id from exact full-key structure rows", "query": ["CHEBI:155912"]}'
  snapshot_sha256: 228f6bd3fa90fd866e8fd96fd968caef263ed94de91ddbe85f9194d89617ac50
- evidence_id: bgc-2263-source-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Header line 1; physical lines 16908–16908; row_sha256 6bbf1676d6eec4f936e595c9c5de89fef977ec97ddcfa3fbe0d7fe4bd57d2107;
    physical lines 16909–16909; row_sha256 683a9b731097c565487488adb9981320667023484175014e0054a3a4e7aa17cd
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained physical source rows (all fields), read and joined to
    the current pinned table: [{"chebi_id": "CHEBI:155912", "comments": "", "component_text":
    "cell suspension culture", "source_accession": "25547729", "species_accession":
    "5053", "species_text": "Aspergillus aculeatus", "strain_text": ""}, {"chebi_id":
    "CHEBI:155912", "comments": "", "component_text": "cell suspension culture", "source_accession":
    "27709333", "species_accession": "1808020", "species_text": "Penicillium sp. SCS-KFD08",
    "strain_text": ""}]'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: bgc-2263-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ChemicalStructure distinguishes normalized identity and unspecified stereochemistry.
    ComputedClassification is explicitly a named/versioned prediction, never a source
    assertion or record-admission reason.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2263-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: The maintained extractor derives the stereo_complete flag from unassigned
    chiral centres; no new extractor call occurred in this review.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2263-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 971–1037
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: The seeder retains the exact structure/definition source and copies named
    NPClassifier results including is_glycoside. A prediction is not promoted to experimental
    evidence.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2263-origin-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 1093–1151
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Producer evidence and locus methods/link grades remain separately copied;
    merges and applicable local qualifications have distinct handling.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2263-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole profile
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Current review profile requires one-record identity, evidence, provenance,
    representation and completion dimensions without promoting unavailable verification.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2263-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole review skill
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Current one-record review scope distinguishes local evidence review from
    scientific completeness, preserves source records, and requires concrete supported
    findings.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2263-reader-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch227/native-current227-aculene-c-maintained-reader-DATA-001.json
  locator: /resolved_view; /review_check_metadata
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: The original maintained reader preserves the complete captured owner, including
    one graph with three nodes/two edges, one pathway entry and all three history
    events. The resolved view and exact check metadata do not freshly validate the
    historical mechanism evidence.
  snapshot_sha256: 29876ec3878028e4944a80595cc503cfc263fb11b68a78f9e1b3a928bcb40ef9
- evidence_id: bgc-2263-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch227/native-current227-aculene-c-reader-execution-001.json
  locator: /exit_code; /stdout; /stderr; /external_requests; /retries
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: Original Native-owned maintained reader returned zero once; exact streams,
    no retries and no external requests are retained.
  snapshot_sha256: dd2f9e2fdf941456c14e40d33adf63f316040cc27ee9dfba25b2ff4fb4405760
- evidence_id: bgc-2263-reader-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch227/root-2263-maintained-reader-acceptance-001.json
  locator: /review_check_contract; /verification; /limits
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: ROOT accepts the exact original complete-owner result and its current dependencies;
    the check contract is authoritative for this maintained-reader check.
  snapshot_sha256: ea0ec6563350240d690775811605cc4f3bf1fae66dca00d1453cc7bd0ba83b73
- evidence_id: bgc-2263-causal_graphs-complete
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/native-current227-aculene-c-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained causal_graphs content, with historical evidence grades
    and limitations rather than new verification: [{"description": "Partial A. aculeatus
    aculene C biosynthesis graph for AneA-catalyzed desaturation of aculene D.", "edges":
    [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "Lee et al. identified
    the Aspergillus aculeatus aculene biosynthetic gene cluster, inactivated aneA,
    and used Saccharomyces cerevisiae and Aspergillus oryzae heterologous reconstitution
    to connect AneA to 5,6-desaturation of aculene D into aculene C.", "reference":
    "DOI:10.1002/anie.201910200", "snippet": "characterized the biosynthetic pathway
    based on gene inactivation, feeding experiments, and heterologous reconstitution"},
    {"evidence_type": "REVIEW", "notes": "Wang et al. summarize Lee et al.''s aneA
    deletion phenotype and place AneA after A. oryzae reconstitution of AneC/F/D/G
    to aculene D in the published aculene A-C pathway.", "reference": "DOI:10.1039/D1NP00074H",
    "snippet": "the unsaturation is catalyzed by AneA"}, {"evidence_type": "DATABASE_ASSERTION",
    "notes": "MIBiG BGC0002225.3 maps the A. aculeatus ATCC 16872 KV878977 aculene
    region to CDS OJJ99912.1 at locus ASPACDRAFT_119783.", "reference": "https://mibig.secondarymetabolites.org/repository/BGC0002225.3/BGC0002225.gbk",
    "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes":
    "Reviewed UniProtKB:A0A1L9WUX8 is the 298 aa A. aculeatus ATCC 16872 Dioxygenase
    aneA, cross-references KV878977 protein OJJ99912.1, and annotates RHEA:65112 from
    PMID:31618514.", "reference": "https://www.uniprot.org/uniprotkb/A0A1L9WUX8",
    "retrieved_on": "2026-09-30", "snippet": "The dioxygenase aneA converts aculene
    D into aculene C"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "The Rhea
    Swiss-Prot mapping links UniProtKB:A0A1L9WUX8 to RHEA:65112, the aculene D 2-oxoglutarate-dependent
    desaturation reaction.", "reference": "https://ftp.expasy.org/databases/rhea/tsv/rhea2uniprot_sprot.tsv",
    "retrieved_on": "2026-09-30"}], "notes": "AneA desaturates aculene D between C5
    and C6.", "object": "anea", "predicate": "is desaturated by", "subject": "aculene_d"},
    {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "Lee et al. identified
    the Aspergillus aculeatus aculene biosynthetic gene cluster, inactivated aneA,
    and used Saccharomyces cerevisiae and Aspergillus oryzae heterologous reconstitution
    to connect AneA to 5,6-desaturation of aculene D into aculene C.", "reference":
    "DOI:10.1002/anie.201910200", "snippet": "characterized the biosynthetic pathway
    based on gene inactivation, feeding experiments, and heterologous reconstitution"},
    {"evidence_type": "REVIEW", "notes": "Wang et al. summarize Lee et al.''s aneA
    deletion phenotype and place AneA after A. oryzae reconstitution of AneC/F/D/G
    to aculene D in the published aculene A-C pathway.", "reference": "DOI:10.1039/D1NP00074H",
    "snippet": "the unsaturation is catalyzed by AneA"}, {"evidence_type": "DATABASE_ASSERTION",
    "notes": "MIBiG BGC0002225.3 maps the A. aculeatus ATCC 16872 KV878977 aculene
    region to CDS OJJ99912.1 at locus ASPACDRAFT_119783.", "reference": "https://mibig.secondarymetabolites.org/repository/BGC0002225.3/BGC0002225.gbk",
    "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes":
    "Reviewed UniProtKB:A0A1L9WUX8 is the 298 aa A. aculeatus ATCC 16872 Dioxygenase
    aneA, cross-references KV878977 protein OJJ99912.1, and annotates RHEA:65112 from
    PMID:31618514.", "reference": "https://www.uniprot.org/uniprotkb/A0A1L9WUX8",
    "retrieved_on": "2026-09-30", "snippet": "The dioxygenase aneA converts aculene
    D into aculene C"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "The Rhea
    Swiss-Prot mapping links UniProtKB:A0A1L9WUX8 to RHEA:65112, the aculene D 2-oxoglutarate-dependent
    desaturation reaction.", "reference": "https://ftp.expasy.org/databases/rhea/tsv/rhea2uniprot_sprot.tsv",
    "retrieved_on": "2026-09-30"}], "notes": "The AneA dioxygenase reaction yields
    aculene C from aculene D.", "object": "aculene_c", "predicate": "forms", "subject":
    "anea"}], "graph_id": "aculene-c-anea-desaturation", "nodes": [{"grounding_status":
    "GROUNDED", "identifier": "CHEBI:155910", "label": "aculene D", "node_id": "aculene_d",
    "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED", "identifier": "UniProtKB:A0A1L9WUX8",
    "label": "AneA aculene D dioxygenase", "node_id": "anea", "node_type": "ENZYME"},
    {"grounding_status": "GROUNDED", "identifier": "CHEBI:155912", "label": "aculene
    C", "node_id": "aculene_c", "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"}]'
  snapshot_sha256: 29876ec3878028e4944a80595cc503cfc263fb11b68a78f9e1b3a928bcb40ef9
- evidence_id: bgc-2263-biosynthetic_pathway-complete
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/native-current227-aculene-c-maintained-reader-DATA-001.json
  locator: /resolved_view/biosynthetic_pathway
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained biosynthetic_pathway content, with historical evidence
    grades and limitations rather than new verification: [{"enzyme_id": "UniProtKB:A0A1L9WUX8",
    "enzyme_label": "AneA aculene D dioxygenase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT",
    "notes": "Lee et al. identified the Aspergillus aculeatus aculene biosynthetic
    gene cluster, inactivated aneA, and used Saccharomyces cerevisiae and Aspergillus
    oryzae heterologous reconstitution to connect AneA to 5,6-desaturation of aculene
    D into aculene C.", "reference": "DOI:10.1002/anie.201910200", "snippet": "characterized
    the biosynthetic pathway based on gene inactivation, feeding experiments, and
    heterologous reconstitution"}, {"evidence_type": "REVIEW", "notes": "Wang et al.
    summarize Lee et al.''s aneA deletion phenotype and place AneA after A. oryzae
    reconstitution of AneC/F/D/G to aculene D in the published aculene A-C pathway.",
    "reference": "DOI:10.1039/D1NP00074H", "snippet": "the unsaturation is catalyzed
    by AneA"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002225.3
    maps the A. aculeatus ATCC 16872 KV878977 aculene region to CDS OJJ99912.1 at
    locus ASPACDRAFT_119783.", "reference": "https://mibig.secondarymetabolites.org/repository/BGC0002225.3/BGC0002225.gbk",
    "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes":
    "Reviewed UniProtKB:A0A1L9WUX8 is the 298 aa A. aculeatus ATCC 16872 Dioxygenase
    aneA, cross-references KV878977 protein OJJ99912.1, and annotates RHEA:65112 from
    PMID:31618514.", "reference": "https://www.uniprot.org/uniprotkb/A0A1L9WUX8",
    "retrieved_on": "2026-09-30", "snippet": "The dioxygenase aneA converts aculene
    D into aculene C"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "The Rhea
    Swiss-Prot mapping links UniProtKB:A0A1L9WUX8 to RHEA:65112, the aculene D 2-oxoglutarate-dependent
    desaturation reaction.", "reference": "https://ftp.expasy.org/databases/rhea/tsv/rhea2uniprot_sprot.tsv",
    "retrieved_on": "2026-09-30"}], "notes": "AneA introduces the 5,6-alkene into
    aculene D to form aculene C; RHEA:65112 grounds the full 2-oxoglutarate- and O2-dependent
    dioxygenase reaction.", "products": ["CHEBI:155912", "CHEBI:30031", "CHEBI:16526",
    "CHEBI:15377"], "reaction_id": "RHEA:65112", "step_number": 1, "substrates": ["CHEBI:155910",
    "CHEBI:16810", "CHEBI:15379"]}]'
  snapshot_sha256: 29876ec3878028e4944a80595cc503cfc263fb11b68a78f9e1b3a928bcb40ef9
- evidence_id: bgc-2263-curation_history-complete
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch227/native-current227-aculene-c-maintained-reader-DATA-001.json
  locator: /resolved_view/curation_history
  accessed_at: '2026-11-03T17:25:34.020346Z'
  support: supports
  summary: 'Complete retained curation_history content, with historical evidence grades
    and limitations rather than new verification: [{"action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources",
    "timestamp": "2026-09-10T05:54:13Z"}, {"action": "SEEDED_FROM_SOURCES", "changes":
    "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources",
    "timestamp": "2026-09-25T03:03:27Z"}, {"action": "ADD_BIOSYNTHETIC_PROTEIN_GRAPH",
    "changes": "Added exact UniProtKB:A0A1L9WUX8 AneA grounding, the RHEA:65112 aculene
    D desaturation step, and a BIOSYNTHESIS causal graph for aculene C.", "curator":
    "codex", "llm_assisted": true, "timestamp": "2026-09-30T15:14:56Z"}]'
  snapshot_sha256: 29876ec3878028e4944a80595cc503cfc263fb11b68a78f9e1b3a928bcb40ef9
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
- assessment_id: bgc-2263-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: CHEBI:155912 is locally grounded by exact complete-key agreement UCCFSWQSMDQYHO-GXTWGEPZSA-N
    between MIBiG BGC0002225 version 3 compound index 3 and the three-star ChEBI row.
    The stored ketone, hydroxy group and fused five/seven-membered core are consistent
    with the retained aculene C definition, including the S hydroxy-bearing and R
    methyl-bearing bridgehead centres. Aculene congeners are not interchangeable merely
    because they share the same cluster.
  target_ids:
  - CHEBI:155912
  evidence_ids:
  - bgc-2263-grounding-owner
  - bgc-2263-source-mibig_compounds
  - bgc-2263-source-chebi_structures
  - bgc-2263-query-chebi_structures
  - bgc-2263-chemistry
  - bgc-2263-topology
  - bgc-2263-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: UCCFSWQSMDQYHO-GXTWGEPZSA-N; exact complete source key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2263-grounding-owner
    - bgc-2263-source-mibig_compounds
    - bgc-2263-source-chebi_structures
    - bgc-2263-query-chebi_structures
    - bgc-2263-chemistry
    - bgc-2263-topology
    - bgc-2263-direct-contexts
  - name: grounding_scope
    value: EXACT CHEBI:155912, MIBiG BGC0002225 version 3 compound index 3; no congener
      substitution.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2263-grounding-owner
    - bgc-2263-source-mibig_compounds
    - bgc-2263-source-chebi_structures
    - bgc-2263-query-chebi_structures
    - bgc-2263-chemistry
    - bgc-2263-topology
    - bgc-2263-direct-contexts
- assessment_id: bgc-2263-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both stored forms give neutral C14H18O2 with 16 atoms, 17 bonds and one
    fragment. The two specified centres are SMILES C6 R and C12 S, corresponding to
    InChI C13 R and C11 S. The core C7=C8 bond is double, in addition to C2=C3 and
    C9=C10; the carbonyl is C4=O5 and C12 bears OH13. All ten comparisons and the
    complete stored chirality-aware map agree. No external structure or isolated natural
    stereochemistry has been independently established.
  target_ids:
  - CHEBI:155912
  evidence_ids:
  - bgc-2263-grounding-owner
  - bgc-2263-chemistry
  - bgc-2263-topology
  - bgc-2263-diagnostic-acceptance
  - bgc-2263-structure-schema
  - bgc-2263-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: 'Two specified tetrahedral centres: SMILES C6 R and C12 S; retained true
      flag, without experimental stereochemical authentication.'
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2263-grounding-owner
    - bgc-2263-chemistry
    - bgc-2263-topology
    - bgc-2263-diagnostic-acceptance
    - bgc-2263-structure-schema
    - bgc-2263-stereo-method
  - name: representation_correspondence
    value: Ten true flags and a complete stored chirality-aware map; no independent
      full-graph or natural identity claim.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2263-grounding-owner
    - bgc-2263-chemistry
    - bgc-2263-topology
    - bgc-2263-diagnostic-acceptance
    - bgc-2263-structure-schema
    - bgc-2263-stereo-method
- assessment_id: bgc-2263-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: The source retains Aspergillus aculeatus ATCC 16872, taxon 690307, as BGC_CHARACTERIZED
    and BGC0002225 version 3 as CLUSTER_DEMONSTRATED from heterologous expression
    and knock-out studies. Entry quality is questionable and completeness unknown.
    Genbank:KV878977.1 interval 1125505–1144430 is the source locus. Aspergillus aculeatus
    species 5053 and Penicillium sp. SCS-KFD08 taxon 1808020 are separately retained
    occurrence taxa; their cached labels do not make Penicillium a producer of this
    Aspergillus locus.
  target_ids:
  - CHEBI:155912
  evidence_ids:
  - bgc-2263-origin-owner
  - bgc-2263-source-mibig_compounds
  - bgc-2263-cached-taxonomy
  - bgc-2263-source-routes
  - bgc-2263-origin-seeder
  - bgc-2263-reader-DATA
  - bgc-2263-reader-acceptance
  - bgc-2263-causal_graphs-complete
  - bgc-2263-biosynthetic_pathway-complete
  dimensions:
  - name: taxon_scope
    value: Producer strain 690307; occurrence species 5053 and Penicillium isolate
      1808020.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2263-origin-owner
    - bgc-2263-source-mibig_compounds
    - bgc-2263-cached-taxonomy
    - bgc-2263-source-routes
    - bgc-2263-origin-seeder
    - bgc-2263-reader-DATA
    - bgc-2263-reader-acceptance
    - bgc-2263-causal_graphs-complete
    - bgc-2263-biosynthetic_pathway-complete
  - name: producer_evidence
    value: BGC_CHARACTERIZED from the retained MIBiG claim; distinct from species-level
      occurrences.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2263-origin-owner
    - bgc-2263-source-mibig_compounds
    - bgc-2263-cached-taxonomy
    - bgc-2263-source-routes
    - bgc-2263-origin-seeder
    - bgc-2263-reader-DATA
    - bgc-2263-reader-acceptance
    - bgc-2263-causal_graphs-complete
    - bgc-2263-biosynthetic_pathway-complete
  - name: locus_evidence
    value: BGC0002225 version 3, questionable/unknown, CLUSTER_DEMONSTRATED from heterologous
      expression and knock-out studies.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2263-origin-owner
    - bgc-2263-source-mibig_compounds
    - bgc-2263-cached-taxonomy
    - bgc-2263-source-routes
    - bgc-2263-origin-seeder
    - bgc-2263-reader-DATA
    - bgc-2263-reader-acceptance
    - bgc-2263-causal_graphs-complete
    - bgc-2263-biosynthetic_pathway-complete
- assessment_id: bgc-2263-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: MIBiG producer/locus support remains ENTRY PMID:31618514. Occurrence assertions
    retain LOTUS DOI:10.3390/MOLECULES190810898, ChEBI Aspergillus PMID:25547729 and
    Penicillium PMID:27709333. The graph and pathway separately retain DOI:10.1002/anie.201910200
    as PRIMARY_EXPERIMENT, DOI:10.1039/D1NP00074H as REVIEW, and dated MIBiG/UniProt/Rhea
    database assertions. These locally preserved citations and snippets have not been
    freshly accessed; the reader confirms preservation rather than experimental sufficiency.
  target_ids:
  - CHEBI:155912
  evidence_ids:
  - bgc-2263-origin-owner
  - bgc-2263-occurrence-owner
  - bgc-2263-source-mibig_compounds
  - bgc-2263-source-lotus_occurrences
  - bgc-2263-query-chebi_origins
  - bgc-2263-source-notes
  - bgc-2263-direct-contexts
  - bgc-2263-source-chebi_structures
  - bgc-2263-reader-DATA
  - bgc-2263-reader-acceptance
  - bgc-2263-causal_graphs-complete
  - bgc-2263-biosynthetic_pathway-complete
  dimensions:
  - name: citation_scope
    value: ENTRY PMID:31618514; distinct LOTUS/ChEBI origins and historically attributed
      primary/review/database graph evidence.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2263-origin-owner
    - bgc-2263-occurrence-owner
    - bgc-2263-source-mibig_compounds
    - bgc-2263-source-lotus_occurrences
    - bgc-2263-query-chebi_origins
    - bgc-2263-source-notes
    - bgc-2263-direct-contexts
    - bgc-2263-source-chebi_structures
    - bgc-2263-reader-DATA
    - bgc-2263-reader-acceptance
    - bgc-2263-causal_graphs-complete
    - bgc-2263-biosynthetic_pathway-complete
- assessment_id: bgc-2263-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: 'The owner writes three occurrence objects: a Penicillium ChEBI assertion
    and separate LOTUS/ChEBI Aspergillus assertions. PubChem physical row 8042 for
    CID 139586350 is a blank-AID ''(no assay data)'' sentinel, not an activity observation.
    No pharmacological bioactivity or molecular-target root is written, and the exact
    BindingDB/AntibioticMech joins are empty. The AneA biosynthesis annotation is
    a substrate-to-product claim, not a pharmacological target assay.'
  target_ids:
  - CHEBI:155912
  evidence_ids:
  - bgc-2263-assay-owner
  - bgc-2263-occurrence-owner
  - bgc-2263-source-lotus_occurrences
  - bgc-2263-query-chebi_origins
  - bgc-2263-query-pubchem_bioassay
  - bgc-2263-query-bindingdb_targets
  - bgc-2263-query-antibioticmech_inchikeys
  - bgc-2263-query-cyanometdb_occurrences
  - bgc-2263-source-routes
  - bgc-2263-cached-taxonomy
  - bgc-2263-source-pubchem_bioassay
  dimensions:
  - name: occurrence_scope
    value: Three written occurrence assertions across Aspergillus species 5053 and
      Penicillium isolate 1808020; distinct from producer strain 690307.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2263-assay-owner
    - bgc-2263-occurrence-owner
    - bgc-2263-source-lotus_occurrences
    - bgc-2263-query-chebi_origins
    - bgc-2263-query-pubchem_bioassay
    - bgc-2263-query-bindingdb_targets
    - bgc-2263-query-antibioticmech_inchikeys
    - bgc-2263-query-cyanometdb_occurrences
    - bgc-2263-source-routes
    - bgc-2263-cached-taxonomy
    - bgc-2263-source-pubchem_bioassay
  - name: assay_target_scope
    value: No written pharmacological assays/targets and no actual retained AID rows;
      one blank-AID sentinel is not inactivity.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2263-assay-owner
    - bgc-2263-occurrence-owner
    - bgc-2263-source-lotus_occurrences
    - bgc-2263-query-chebi_origins
    - bgc-2263-query-pubchem_bioassay
    - bgc-2263-query-bindingdb_targets
    - bgc-2263-query-antibioticmech_inchikeys
    - bgc-2263-query-cyanometdb_occurrences
    - bgc-2263-source-routes
    - bgc-2263-cached-taxonomy
    - bgc-2263-source-pubchem_bioassay
- assessment_id: bgc-2263-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The saved C14 fused carbocyclic ketone/alcohol topology is compatible with
    the retained broad terpene filing. MIBiG TERPENE and NPClassifier npclassifier.gnps2.org@2026-09-07
    Terpenoids / Sesquiterpenoids / Daucane sesquiterpenoids remain different evidence
    axes. The copied is_glycoside:false prediction is consistent with the absence
    of a sugar linkage in the saved complete tables. Neither classifier output nor
    class membership makes the partial AneA reaction a complete biosynthetic pathway.
  target_ids:
  - CHEBI:155912
  evidence_ids:
  - bgc-2263-classification-owner
  - bgc-2263-source-npclassifier
  - bgc-2263-source-mibig_compounds
  - bgc-2263-chemistry
  - bgc-2263-topology
  - bgc-2263-structure-schema
  - bgc-2263-classification-seeder
  - bgc-2263-reader-DATA
  - bgc-2263-reader-acceptance
  - bgc-2263-causal_graphs-complete
  - bgc-2263-biosynthetic_pathway-complete
  dimensions:
  - name: classification_applicability
    value: Retained model and BGC labels remain distinct; false glycoside prediction
      is compatible with saved topology, without proving biosynthesis.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2263-classification-owner
    - bgc-2263-source-npclassifier
    - bgc-2263-source-mibig_compounds
    - bgc-2263-chemistry
    - bgc-2263-topology
    - bgc-2263-structure-schema
    - bgc-2263-classification-seeder
    - bgc-2263-reader-DATA
    - bgc-2263-reader-acceptance
    - bgc-2263-causal_graphs-complete
    - bgc-2263-biosynthetic_pathway-complete
- assessment_id: bgc-2263-completion
  area: completeness
  topic: Completion
  outcome: supported
  summary: Partial scientific review from complete local source and saved molecular
    evidence; five local gates passed, full QC/OAK and fresh external verification
    unavailable. The exact original maintained reader passed for this positive owner;
    historical evidence limits remain.
  target_ids:
  - CHEBI:155912
  evidence_ids:
  - bgc-2263-owner
  - bgc-2263-capture
  - bgc-2263-intake
  - bgc-2263-intake-acceptance
  - bgc-2263-source-plan
  - bgc-2263-plan-acceptance
  - bgc-2263-source-notes
  - bgc-2263-inventory-acceptance
  - bgc-2263-diagnostic-execution
  - bgc-2263-diagnostic-acceptance
  - bgc-2263-native-acceptance
  - bgc-2263-review-profile
  - bgc-2263-review-skill
  - bgc-2263-reader-DATA
  - bgc-2263-reader-acceptance
  - bgc-2263-causal_graphs-complete
  - bgc-2263-biosynthetic_pathway-complete
  dimensions:
  - name: review_completion
    value: Partial scientific review from complete local source and saved molecular
      evidence; five local gates passed, full QC/OAK and fresh external verification
      unavailable. Accepted original maintained reader preserves the complete positive
      owner.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2263-owner
    - bgc-2263-capture
    - bgc-2263-intake
    - bgc-2263-intake-acceptance
    - bgc-2263-source-plan
    - bgc-2263-plan-acceptance
    - bgc-2263-source-notes
    - bgc-2263-inventory-acceptance
    - bgc-2263-diagnostic-execution
    - bgc-2263-diagnostic-acceptance
    - bgc-2263-native-acceptance
    - bgc-2263-review-profile
    - bgc-2263-review-skill
    - bgc-2263-reader-DATA
    - bgc-2263-reader-acceptance
    - bgc-2263-causal_graphs-complete
    - bgc-2263-biosynthetic_pathway-complete
- assessment_id: bgc-2263-mechanism
  area: graph
  topic: Partial AneA reaction and owner direction
  outcome: supported
  summary: The accepted maintained view preserves one graph, three nodes, two edges,
    ten graph evidence placements and one pathway step with five evidence placements.
    AneA is annotated to desaturate aculene D into aculene C, with RHEA:65112 listing
    2-oxoglutarate and O2 as cosubstrates and succinate, CO2 and water among products.
    The owner is the product aculene C. The retained gene-inactivation, feeding and
    heterologous-reconstitution description is a historical source annotation. No
    complete pathway, native flux or fresh primary-paper validation follows from reader
    success.
  target_ids:
  - CHEBI:155912
  evidence_ids:
  - bgc-2263-owner
  - bgc-2263-capture
  - bgc-2263-reader-DATA
  - bgc-2263-reader-execution
  - bgc-2263-reader-acceptance
  - bgc-2263-causal_graphs-complete
  - bgc-2263-biosynthetic_pathway-complete
  - bgc-2263-curation_history-complete
  - bgc-2263-source-mibig_compounds
  dimensions: []
- assessment_id: bgc-2263-protein
  area: grounding
  topic: Protein identity, evidence and construct limits
  outcome: supported
  summary: UniProtKB:A0A1L9WUX8 is retained as the 298-residue A. aculeatus ATCC 16872
    AneA reference, linked historically to OJJ99912.1, ASPACDRAFT_119783, KV878977
    and RHEA:65112. The graph distinguishes primary-experiment/review annotations
    from dated MIBiG, UniProt and Rhea database assertions. Those local claims are
    not a newly inspected sequence or proof that a native reference equals every experimental
    construct. Exact assay construct, kinetics, cofactor occupancy and native complex/flux
    were not established in this offline review.
  target_ids:
  - CHEBI:155912
  evidence_ids:
  - bgc-2263-owner
  - bgc-2263-capture
  - bgc-2263-reader-DATA
  - bgc-2263-reader-execution
  - bgc-2263-reader-acceptance
  - bgc-2263-causal_graphs-complete
  - bgc-2263-biosynthetic_pathway-complete
  - bgc-2263-curation_history-complete
  - bgc-2263-source-mibig_compounds
  dimensions: []
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
