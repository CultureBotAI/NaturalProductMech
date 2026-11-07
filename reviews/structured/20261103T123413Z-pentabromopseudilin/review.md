# Local evidence review: pentabromopseudilin

- Review: 20261103T123413Z-pentabromopseudilin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T12:06:20.567919Z
- Finished UTC: 2026-11-03T12:34:13.287898Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

pentabromopseudilin: partial review requires curation of unsupported activity typing; identity, source grades and maintained biosynthetic scope remain bounded.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2217; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-005498ea51 | data/natural_products/shikimates_and_phenylpropanoids/pentabromopseudilin.yaml | generated | pentabromopseudilin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for pentabromopseudilin | passed | True | naturalproductmech:mibig-005498ea51 | Original single offline maintained call preserved the complete owner, one graph/five nodes/four edges/eight graph references and one step/five pathway references. No components. This does not freshly verify mechanism science, proteins, primary sources or pharmacological activity. |
| strict_ten | passed | True | naturalproductmech:mibig-005498ea51 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-005498ea51 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-005498ea51 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-005498ea51 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-005498ea51 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-005498ea51 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-005498ea51 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-005498ea51 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding scope

identity: supported. Targets: naturalproductmech:mibig-005498ea51.

Pentabromopseudilin retains the complete key LXMNWKJHYOZUQL-UHFFFAOYSA-N and C10H4Br5NO across three MIBiG source entries. Its retained exact-key ChEBI query is empty and the minted identifier is preserved. The shared-structure discussion remains open; agreeing keys alone do not independently adjudicate all upstream entry identities. Bistribromopyrrole and bromophene share BGC0001465 but have different full keys and structures, so their activities and source concepts do not transfer.

### Paired representations and stereochemical limits

representation: supported. Targets: naturalproductmech:mibig-005498ea51.

Both stored forms agree on formula, charge, standardized identifiers and canonical isomeric/nonisomeric SMILES. The complete 17-atom correspondence remains a bounded substructure match, with full_graph_identity_established:false. Neither saved form reports potential tetrahedral or double-bond stereo; literal stereo_complete:true remains an atom-centred source flag. No additional parse or natural-isolate stereochemical proof was performed.

### Producer, occurrence and locus evidence grades

provenance: supported. Targets: naturalproductmech:mibig-005498ea51.

BGC0000891 version 4 retains Pseudoalteromonas luteoviolacea 2ta16/1353533 as BGC_CORRELATED and its enzymatic/heterologous/expression evidence as CLUSTER_DEMONSTRATED, at AUSV01000133.1:32483–43745. BGC0000890 version 5 retains P. phenolica O-BC30/1315281 as SOURCE_ASSERTION with a demonstrated heterologous locus on KF540211.1 and unstated coordinates. BGC0001465 version 5 retains Marinomonas mediterranea MMB-1/717774 as SOURCE_ASSERTION with CLUSTER_UNSTATED at NC_015276.1:4521275–4533494. Two LOTUS species 43657 occurrences are distinct from these strain-specific producer assertions.

### Citation placement and historical verification scope

evidence: supported. Targets: naturalproductmech:mibig-005498ea51.

All three MIBiG producer/locus assertions use ENTRY PMID:24974229 as DATABASE_ASSERTION; the two LOTUS DOI triples retain occurrence scope. The activity row cites PMID:24446431. The curator-owned Bmp7 graph/pathway separately preserves historical PRIMARY_EXPERIMENT snippets from DOI:10.1038/nchembio.1564 and database assertions for V4HJ73, ESP90850.1 and AUSV01000133.1. These citations and snippets were read as saved evidence, not freshly retrieved primary text, sequence verification or independent publication counts.

### Occurrence, assay and companion boundaries

scope: concern. Targets: naturalproductmech:mibig-005498ea51.

The sole retained selected PubChem row, physical line 3813 / AID 977608, reports an Active PDB protein–ligand binding-affinity IC50 of 1.4 uM, assay type Other, with blank target accession. The generated observation and sole bioactivity_summary both add ENZYME_INHIBITOR via the maintained IC50/binding-name fallback. That inference is not supported by an identified enzyme-inhibition method in this retained row. Preserve the literal assay, Active call, value, units and citation; omit the optional inferred class and rederive the summary unless separately inspected evidence supports it. This support gap does not establish inactivity or deny real inhibitory pharmacology. Empty BindingDB/sibling matches and the biosynthetic Bmp7 graph provide no alternative activity backing here.

### Computed classification and full-table topology limits

other: concern. Targets: naturalproductmech:mibig-005498ea51.

Both complete graphs contain a brominated phenyl ring joined directly by C–C to a brominated [nH] pyrrole, with a terminal phenolic oxygen and five bromines. There is no C–O–C ether bridge; the single oxygen is not a diphenyl-ether linker. NPClassifier's Diphenyl ethers/Marine-bacterial DPEs is therefore a model-applicability concern, retained explicitly as a versioned prediction rather than asserted topology or evidence of wrong compound identity. No raw prediction is overwritten.

### Partial completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-005498ea51.

The accepted maintained reader is required for this selected owner and its one inline Bmp7 graph plus pathway step; its saved result establishes complete-owner preservation within the local read contract. It does not verify the historical chemistry, protein databases or activity interpretation. The unsupported activity-class inference requires curation; the review remains partial because full QC/OAK and fresh primary/authority verification are unavailable. Proposed repair belongs to the maintained classifier and regeneration, not hand-editing generated observations or raw source calls.

### Complete maintained Bmp7 biosynthetic scope

graph: supported. Targets: naturalproductmech:mibig-005498ea51.

The complete accepted owner preserves one BIOSYNTHESIS graph with 5 nodes, 4 edges and 8 graph-evidence placements and one pathway step with 5 evidence placements; there are no component references or molecular targets. The graph distinguishes dibromophenol and ungrounded tribromopyrrole precursors, Bmp7, the oxidative-heterocoupling process and the exact minted product. Historical notes describe purified Bmp7 with Bmp9/Bmp10/NADH and authentic-standard comparison. Those scoped biosynthetic assertions do not make Bmp7 a pharmacological target or support ENZYME_INHIBITOR. The pathway's historical one-substrate explanation is not treated as a statement of the current schema's capabilities.

### Organism-specific protein assertions and verification limits

grounding: unknown. Targets: naturalproductmech:mibig-005498ea51.

The saved curator assertions identify P. luteoviolacea 2ta16 Bmp7 as UniProtKB:V4HJ73, locus PL2TA16_01241 and NCBI_Protein:ESP90850.1, with AUSV01000133.1:42270–43745 inside the stated BGC0000891 interval. These identifiers describe the same asserted organism-specific enzyme example within the saved record; ungrounded substrate/process nodes remain explicit. No original article/API response or protein sequence was inspected in this review, and the maintained reader does not independently establish sequence, enzymatic specificity or present database status.

## Findings

### support-2217-binding-class-scope: Generic PDB binding observation does not support the inferred enzyme-inhibitor class

major / open / confirmed; issue key: pentabromopseudilin-pdb-binding-enzyme-inhibitor-overstatement.

The sole written observation at bioactivities[0] is retained PubChem physical row3813/AID977608: Active, IC50=1.4uM, assay type Other, protein–ligand complexes derived from PDB, blank target accession and PMID:24446431. The maintained IC50/binding-name fallback adds ENZYME_INHIBITOR without an identified enzyme-inhibition method in that row, then derives the sole matching summary. The support gap concerns that inferred class and summary, not the literal measurement or whether Pentabromopseudilin can inhibit an enzyme in other evidence. No selected BindingDB/sibling result or pharmacological target backs the class here; the Bmp7 graph is biosynthetic and cannot substitute for such backing.

Disposition: Confirmed source-to-generated-inference gap, rather than a claim of inactivity or a consequence of unavailable external sources.

## Recommended Actions And Acceptance Checks

### support-2217-repair-binding-classification

Narrow maintained classify_activity so this exact generic PDB-binding title does not receive ENZYME_INHIBITOR solely from IC50 or binding. Omit the optional activity_class unless independently inspected appropriate evidence supports it. Preserve the Active call, full title, AID977608, IC50=1.4uM, blank target and PMID:24446431. Recompute the summary from justified written/target/sibling support; with only the currently retained observation corrected and no alternative backing here, ENZYME_INHIBITOR no longer has support in the summary. Preserve the biosynthetic Bmp7 graph/pathway and all source/history content.

- The exact retained assay observation survives unchanged except omission of its unsupported optional activity_class.
- The sole unsupported ENZYME_INHIBITOR summary is removed on regeneration unless separately inspected and appropriately admitted evidence provides backing.
- Regression checks distinguish generic PDB binding from explicitly supported enzyme-inhibition observations; do not discard activity calls or transfer companion claims.
- After future authorized implementation, regenerate through the maintained seeder and run required strict/reproduction/corpus/review checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2217-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/pentabromopseudilin.yaml; Complete raw owner, lines 1-323. | supports | Complete selected owner and all 4 history events personally read; unchanged exact raw bytes. |
| support-2217-capture | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/6 | supports | Original complete owner capture; graph/pathway/target/history fields retain their own source and curator attribution. |
| support-2217-intake | /private/tmp/npm-review-work/shared-next-batch222/intakes/2217-inspect-001.json; /targets; /source | supports | Original canonical inspection of the exact selected target and 43 current inputs; inspection alone is not scientific completion. |
| support-2217-intake-ready | /private/tmp/npm-review-work/shared-next-batch222/root-intake-ready-001.json; /status; /intakes; /source_placements; /unique_source_paths; /mechanism_owner_orders | supports | ROOT accepted ten original intakes with 418 source placements and 81 unique paths; mechanism scope is explicit. |
| support-2217-source-plan | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6 | supports | Complete accepted selected source scope, exact query frames and full matched payloads, direct companions, additional roles and input map. |
| support-2217-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-target-input-plan-acceptance-001.json; /status; /plan; /source_notes; /source_placements; /unique_source_paths; /per_order | supports | ROOT accepted original source plan; exact maps and current pins joined to actual inventory. |
| support-2217-source-notes | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-scope-notes-001.json; /reading; /cautions | supports | Complete team reading attribution and source-grade/citation/assay limits. Support personally read its 35 contexts/315 frames/221 payloads/86 cached stanzas; BGC owns the disjoint first-five payload/cache partition. |
| support-2217-curation-scope | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-scope-notes-001.json; /curation | supports | Bounded 290-token, case-sensitive literal scan over all physical lines of eight explicitly opened admitted curation tables, including ignored files, found no matches; not a global absence claim. |
| support-2217-chemistry | /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json; /records/6/declared_structure; /records/6/smiles; /records/6/inchi; /records/6/comparisons; /records/6/atom_correspondence | supports | Both stored forms agree on formula, charge, standardized identifiers and canonical isomeric/nonisomeric SMILES. The complete 17-atom correspondence remains a bounded substructure match, with full_graph_identity_established:false. Neither saved form reports potential tetrahedral or double-bond stereo, and literal stereo_complete:true is retained. These saved fields do not establish natural-isolate stereochemistry. |
| support-2217-topology | /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed; /records/6/inchi/computed | supports | Complete paired atom/bond/neighborhood/charge/isotope/stereo/ring/motif tables personally read. Formula C10H4Br5NO; atom/bond counts 17/18. These saved computations do not establish natural identity. |
| support-2217-chemistry-execution | /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stdout; /stderr; /external_requests; /retries | supports | Original ROOT 20 stored-form diagnostic completed once with exit 0; original stderr is separately retained, not silently assigned by owner. |
| support-2217-chemistry-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-chemistry-acceptance-001.json; /status; /DATA; /execution; /molecular_parse_attempts; /false_comparisons; /warning_count; /warning_scope | supports | ROOT accepted original 20-form run; four original global undefined-stereo warnings remain unassigned. All last-five comparisons are true, without full-identity inference. |
| support-2217-warnings | /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-001.stderr; Complete original stderr, lines 1-8. | supports | Four original undefined-stereo warnings are global, without a record assignment. |
| support-2217-native-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-native-gates-acceptance-001.json; /status; /local_commands_passed; /selected_queue_rows; /unavailable_required_gates; /all_native_gates_passed | supports | Five local native commands passed. Full QC and ontology-consistency/OAK remain unavailable; all-native-gates-passed is false. |
| support-2217-source-ownership | /private/tmp/npm-review-work/shared-next-batch222/intakes/2217-inspect-001.json; /targets/0/owner_paths; /targets/0/ownership_note | supports | Exact maintained ownership from actual intake; seeded facts belong to inventories/extractors/seeder and curator graphs/history remain separate. |
| support-2217-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165-173. | supports | Maintained stereo_complete derives from unassigned atom-centre detection; it does not independently establish all geometric, axial or natural stereochemistry. |
| support-2217-classification-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 406-432. | supports | ComputedClassification explicitly represents a named/versioned prediction, never a source assertion or admission reason. |
| support-2217-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 1011-1019. | supports | Maintained seeder preserves the classifier model/version and reported labels/glycoside Boolean. |
| support-2217-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Lines 35-57. | supports | Review scope distinguishes exact structure, source grades, computed classification and maintained ownership; reserved decisions.tsv is not an effective repair owner. |
| support-2217-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6/source_scope_inventory/joins/mibig_compounds | supports | Retained query predicate: exact complete standard_inchi_key equality; query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 3 complete matched rows. Empty matches are limited to this saved source query. |
| support-2217-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 970-970; exact row SHA256 4d5ba7804629a2d073bbc1c101dbc9df5a84874172db7203deb2f52c2be2ad94. | supports | Complete retained mibig_compounds payload: {"mibig_accession":"BGC0000890","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"pentabromopseudilin","compound_index":"1","smiles":"C1=C(C=C(C(=C1C2=C(C(=C(N2)Br)Br)Br)O)Br)Br","standard_inchi":"InChI=1S/C10H4Br5NO/c11-3-1-4(9(17)5(12)2-3)8-6(13)7(14)10(15)16-8/h1-2,16-17H","standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:324093","taxon_id":"NCBITaxon:1315281","taxon_label":"Pseudoalteromonas phenolica O-BC30","bgc_classes":"other","bgc_subclasses":"aminocoumarin","genome_accession":"KF540211.1","locus_from":"","locus_to":"","locus_evidence_methods":"Heterologous expression","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:24974229","reference_basis":"ENTRY"} |
| support-2217-row-mibig_compounds-1 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 971-971; exact row SHA256 8a8585f03dde595ac075866339ae9c400fbd4f62160cea885a28f32883c2b2f5. | supports | Complete retained mibig_compounds payload: {"mibig_accession":"BGC0000891","entry_version":"4","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"pentabromopseudilin","compound_index":"1","smiles":"C1=C(C=C(C(=C1Br)O)C2=C(C(=C(N2)Br)Br)Br)Br","standard_inchi":"InChI=1S/C10H4Br5NO/c11-3-1-4(9(17)5(12)2-3)8-6(13)7(14)10(15)16-8/h1-2,16-17H","standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"","taxon_id":"NCBITaxon:1353533","taxon_label":"Pseudoalteromonas luteoviolacea 2ta16","bgc_classes":"other","bgc_subclasses":"aminocoumarin","genome_accession":"AUSV01000133.1","locus_from":"32483","locus_to":"43745","locus_evidence_methods":"Enzymatic assays&#124;Heterologous expression&#124;Gene expression correlated with compound production","producer_evidence_basis":"BGC_CORRELATED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:24974229","reference_basis":"ENTRY"} |
| support-2217-row-mibig_compounds-2 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 1778-1778; exact row SHA256 3b1a7b2f1c9d6df02ba25eca0d7d92df5bc81338eefed37d63f4e620639c4b40. | supports | Complete retained mibig_compounds payload: {"mibig_accession":"BGC0001465","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"pentabromopseudilin","compound_index":"3","smiles":"C1=C(C=C(C(=C1C2=C(C(=C(N2)Br)Br)Br)O)Br)Br","standard_inchi":"InChI=1S/C10H4Br5NO/c11-3-1-4(9(17)5(12)2-3)8-6(13)7(14)10(15)16-8/h1-2,16-17H","standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:324093","taxon_id":"NCBITaxon:717774","taxon_label":"Marinomonas mediterranea MMB-1","bgc_classes":"other","bgc_subclasses":"other","genome_accession":"NC_015276.1","locus_from":"4521275","locus_to":"4533494","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:24974229","reference_basis":"ENTRY"} |
| support-2217-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6/source_scope_inventory/joins/chebi_structures | supports | Retained query predicate: exact complete standard_inchi_key equality; query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 0 complete matched rows. Empty matches are limited to this saved source query. |
| support-2217-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6/source_scope_inventory/joins/lotus_occurrences | supports | Retained query predicate: exact complete standard_inchi_key equality; query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 2 complete matched rows. Empty matches are limited to this saved source query. |
| support-2217-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 4325-4325; exact row SHA256 66d9caaceaab43e8e9cdd3840781708ad1d3c346c27f7052adfcfef51efced91. | supports | Complete retained lotus_occurrences payload: {"standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","organism_name":"Pseudoalteromonas luteoviolacea","taxon_id":"NCBITaxon:43657","organism_wikidata":"http://www.wikidata.org/entity/Q7254487","reference_doi":"10.1021/JO00092A020","structure_wikidata":"http://www.wikidata.org/entity/Q27138952"} |
| support-2217-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 4326-4326; exact row SHA256 9bb2ec1b974b3462f4a8a847c0aa8db74b061006252752a49ada85a8ab4b3802. | supports | Complete retained lotus_occurrences payload: {"standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","organism_name":"Pseudoalteromonas luteoviolacea","taxon_id":"NCBITaxon:43657","organism_wikidata":"http://www.wikidata.org/entity/Q7254487","reference_doi":"10.1021/NP100506Z","structure_wikidata":"http://www.wikidata.org/entity/Q27138952"} |
| support-2217-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6/source_scope_inventory/joins/cyanometdb_occurrences | supports | Retained query predicate: exact complete standard_inchi_key equality; query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 0 complete matched rows. Empty matches are limited to this saved source query. |
| support-2217-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6/source_scope_inventory/joins/npclassifier | supports | Retained query predicate: exact complete standard_inchi_key equality; query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 1 complete matched rows. Empty matches are limited to this saved source query. |
| support-2217-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 1429-1429; exact row SHA256 beb18c608485e63721849f3db019b1abf86b19a6d98b5b873f55ba3e52a119c1. | supports | Complete retained npclassifier payload: {"standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","smiles":"C1=C(C=C(C(=C1C2=C(C(=C(N2)Br)Br)Br)O)Br)Br","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Diphenyl ethers (DPEs)","class_results":"Marine-bacterial DPEs","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"} |
| support-2217-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6/source_scope_inventory/joins/pubchem_bioassay | supports | Retained query predicate: exact complete standard_inchi_key equality; query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 1 complete matched rows. Empty matches are limited to this saved source query. |
| support-2217-row-pubchem_bioassay-0 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 3813-3813; exact row SHA256 d777329f267f281991aef980ec86f24b67d490732117db3cccd218c9c48bc074. | supports | Complete retained pubchem_bioassay payload: {"standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","cid":"324093","aid":"977608","assay_name":"Experimentally measured binding affinity data (IC50) for protein-ligand complexes derived from PDB","assay_type":"Other","depositor":"Shanghai Institute of Organic Chemistry","activity_outcome":"Active","activity_name":"IC50","activity_value_um":"1.4","target_accession":"","reference":"PMID:24446431"} |
| support-2217-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6/source_scope_inventory/joins/bindingdb_targets | supports | Retained query predicate: exact complete standard_inchi_key equality; query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 0 complete matched rows. Empty matches are limited to this saved source query. |
| support-2217-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Retained query predicate: exact complete standard_inchi_key equality; query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 0 complete matched rows. Empty matches are limited to this saved source query. |
| support-2217-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6/source_scope_inventory/joins/chebi_origins | supports | Retained query predicate: exact chebi_id from exact full-key structure rows; query=[]; 0 complete matched rows. Empty matches are limited to this saved source query. |
| support-2217-taxon-43657 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; Complete OBO stanza, physical lines 19827-19833. | supports | Complete pinned cached stanza: [Term]<br>id: NCBITaxon:43657<br>name: Pseudoalteromonas luteoviolacea<br>synonym: "Alteromonas luteiviolacea" EXACT []<br>synonym: "Alteromonas luteo-violaceus" EXACT []<br>synonym: "Alteromonas luteoviolacea" EXACT []. No fresh taxonomy authority request was made. |
| support-2217-taxon-717774 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; Complete OBO stanza, physical lines 109081-109086. | supports | Complete pinned cached stanza: [Term]<br>id: NCBITaxon:717774<br>name: Marinomonas mediterranea MMB-1<br>synonym: "Marinomonas mediterranea str. MMB-1" EXACT []<br>synonym: "Marinomonas mediterranea strain MMB-1" EXACT []. No fresh taxonomy authority request was made. |
| support-2217-taxon-1315281 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; Complete OBO stanza, physical lines 126091-126094. | supports | Complete pinned cached stanza: [Term]<br>id: NCBITaxon:1315281<br>name: Pseudoalteromonas phenolica O-BC30. No fresh taxonomy authority request was made. |
| support-2217-taxon-1353533 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; Complete OBO stanza, physical lines 127330-127333. | supports | Complete pinned cached stanza: [Term]<br>id: NCBITaxon:1353533<br>name: Pseudoalteromonas luteoviolacea 2ta16. No fresh taxonomy authority request was made. |
| support-2217-taxon-routes | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/6/source_scope_inventory/source_taxa; /records/6/source_scope_inventory/forward_taxon_merge_matches; /records/6/source_scope_inventory/nonorganism_matches | supports | Exact selected source taxon IDs and saved forward-merge/nonorganism route matches; all five selected last-five routes have no such matched rows. |
| support-2217-companion-0 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /raw_unselected_companions/0 | context_only | Complete direct-context owner/history and retained source scope for bistribromopyrrole, key CKUAYXRLIBAUTH-UHFFFAOYSA-N. Its distinct structure, grades, citations and activity are context only; whole raw reading is attributed in source notes. |
| support-2217-companion-9 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /raw_unselected_companions/9 | context_only | Complete direct-context owner/history and retained source scope for bromophene, key TXODBIOSWNNKJM-UHFFFAOYSA-N. Its distinct structure, grades, citations and activity are context only; whole raw reading is attributed in source notes. |
| support-2217-activity-classifier | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 128-178; 1310-1381; 1456-1468. | supports | IC50/Ki/binding-title fallback assigns ENZYME_INHIBITOR to Active rows; positive summary derives from classified written observations and separately admitted sibling classes. |
| support-2217-activity-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 273-285; 631-653; 920-940. | supports | activity_class is optional; every asserted activity class and summary needs supporting evidence. The enum has no dedicated enzyme-inhibitor definition; the present concern follows source method and classifier support scope. |
| support-2217-activity-written | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/6/owner_document/bioactivities; /records/6/owner_document/bioactivity_summary | supports | One exact written observation: AID 977608, Active binding IC50=1.4 uM, with inferred ENZYME_INHIBITOR and sole summary. |
| support-2217-reader-data | /private/tmp/npm-review-work/shared-next-batch222/native-current222-pentabromopseudilin-maintained-reader-DATA-001.json; /raw_owner; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner; /counts; /review_check_metadata; /denials; /unexpected_denials; /errors; /limitations | supports | Original single maintained call preserved every owner field and history, one 5-node/4-edge graph and one pathway step; zero components/targets. One known socket capability probe was denied before action, no requests or unexpected denials. Scientific assertions remain historical. |
| support-2217-reader-execution | /private/tmp/npm-review-work/shared-next-batch222/native-current222-pentabromopseudilin-reader-execution-001.json; /command; /source; /configuration; /stdout; /stderr; /exit_code; /original_tool; /original_start_tool; /DATA; /external_requests | supports | Native original 940c4a/session60327→b80152/exit 0, no replay; full execution and saved streams retain provenance. |
| support-2217-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-pentabromopseudilin-maintained-reader-acceptance-001.json; /status; /DATA; /execution; /verification; /review_check_contract | supports | ROOT accepted exact complete-owner equality and original exit 0; the strict review-check name/command/status is inherited. |
| support-2217-mechanism-graph | /private/tmp/npm-review-work/shared-next-batch222/native-current222-pentabromopseudilin-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/0 | supports | Complete Bmp7 graph personally read: five nodes, four edges, eight reference placements. Historical primary snippets and protein/database assertions retain their original source scopes. |
| support-2217-mechanism-pathway | /private/tmp/npm-review-work/shared-next-batch222/native-current222-pentabromopseudilin-maintained-reader-DATA-001.json; /resolved_view/biosynthetic_pathway/0; /resolved_view/curation_history | supports | Complete Bmp7 pathway step and five evidence placements plus all four owner-history events; no fresh sequence/API/primary verification. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-222/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-222/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-222/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-222/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-222/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Full QC and complete ontology authority coverage/OAK were unavailable; passing five local gates does not establish scientific completeness.
- No external retrieval, live taxonomy/identifier/protein queries or publication verification was performed. These assessments use the original saved owner-form computations; no additional molecular parses were performed during fragment authoring.
- Database citations, cached taxonomy, historical primary labels and versioned model predictions retain their stated evidence types. Matching stored identifiers does not establish natural identity, independent publication support or complete natural stereochemistry.
- No source record or curation history was edited by this review. Canonical review persistence and campaign operations are separately ROOT-owned.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Selected mechanism scope is the complete accepted Bmp7 graph/pathway, with no components; this is distinct from fresh primary/protein/pharmacology verification.
- Native ignored-inclusive saved-review continuity search 674c12/873852 and exact-hit read 72416e found only a prior bromophene companion mention, not a same-owner review/issue_key within W review.yaml/completed-review.yaml and R/reviews/structured. No global absence claim or other-owner issue-key reuse.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T123413Z-pentabromopseudilin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: pentabromopseudilin'
started_at: '2026-11-03T12:06:20.567919Z'
finished_at: '2026-11-03T12:34:13.287898Z'
reviewer:
  identity: Codex root with native_checks, bgc_science and review_support peer agents
  kind: agent
  independence: independent
  independence_basis: This review team inspected existing owner and retained source
    bytes without editing them; scientific fragments were cross-checked separately
    from their author. Local validation is not treated as scientific proof.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'pentabromopseudilin: partial review requires curation of unsupported activity
  typing; identity, source grades and maintained biosynthetic scope remain bounded.'
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
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/alkaloids/bistribromopyrrole.yaml
    sha256: 8b3c8887fe4dbe182936e0ee4f4883028e3f11a6dfbab7aff87a8e887ef95bdf
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/bromophene.yaml
    sha256: 59027979fbfb4cd3b7263a6ca4bc9c6dd2f36d4b0c9792661b9262e9823832bc
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/pentabromopseudilin.yaml
    sha256: ace546ff07e8dcdc1f238e4a2cf711ad3b236474c1d182e0fe633a30b630812b
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
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
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
  selection: Campaign path order 2217; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-005498ea51
targets:
- target_id: naturalproductmech:mibig-005498ea51
  path: data/natural_products/shikimates_and_phenylpropanoids/pentabromopseudilin.yaml
  label: pentabromopseudilin
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
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Exact assay identity exclusion decisions for selected/direct source context.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Maintained source-row identity/digest guard; text-only dependency.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/shikimates_and_phenylpropanoids/pentabromopseudilin.yaml
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
  name: Complete offline maintained reader for pentabromopseudilin
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch222/read-selected-mechanism-guarded-001.py
    2217 8715749ac3fc8e01b4d7d0b4a76c8b13542fa0210f8aec76aaee058005ec3bf6 3d1149fb63bd4f492f60e7fc528e524a94ab69a3b25bfbceeea41c6ba28e6596
    28be4db832f40820b47da073c6ed3f945d86998f30f6335dfdc5be2d5d537856 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
    deb31a6decd5b83371e50c68e20749010ef3603bb5360f563c913df51cb754b9
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-005498ea51
  evidence_ids:
  - support-2217-reader-data
  - support-2217-reader-execution
  - support-2217-reader-acceptance
  summary: Original single offline maintained call preserved the complete owner, one
    graph/five nodes/four edges/eight graph references and one step/five pathway references.
    No components. This does not freshly verify mechanism science, proteins, primary
    sources or pharmacological activity.
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-005498ea51
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-a.yaml data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-b.yaml
    data/natural_products/shikimates_and_phenylpropanoids/o-orsellinic-acid.yaml data/natural_products/shikimates_and_phenylpropanoids/ochratoxin-a.yaml
    data/natural_products/shikimates_and_phenylpropanoids/paerucumarin.yaml data/natural_products/shikimates_and_phenylpropanoids/pentabromopseudilin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/phenguignardic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/prenylhydroquinone.yaml
    data/natural_products/shikimates_and_phenylpropanoids/s2502.yaml --workers 1 --out
    /private/tmp/npm-native-checks/batch-222/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-005498ea51
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-222/validate-all-001.tsv
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
  - naturalproductmech:mibig-005498ea51
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
  - naturalproductmech:mibig-005498ea51
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
  - naturalproductmech:mibig-005498ea51
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-222/review-queue-001.tsv
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
  - naturalproductmech:mibig-005498ea51
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-005498ea51
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-005498ea51
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2217-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/pentabromopseudilin.yaml
  locator: Complete raw owner, lines 1-323.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Complete selected owner and all 4 history events personally read; unchanged
    exact raw bytes.
  snapshot_sha256: ace546ff07e8dcdc1f238e4a2cf711ad3b236474c1d182e0fe633a30b630812b
- evidence_id: support-2217-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/6
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Original complete owner capture; graph/pathway/target/history fields retain
    their own source and curator attribution.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: support-2217-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/intakes/2217-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Original canonical inspection of the exact selected target and 43 current
    inputs; inspection alone is not scientific completion.
  snapshot_sha256: 3d1149fb63bd4f492f60e7fc528e524a94ab69a3b25bfbceeea41c6ba28e6596
- evidence_id: support-2217-intake-ready
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-intake-ready-001.json
  locator: /status; /intakes; /source_placements; /unique_source_paths; /mechanism_owner_orders
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: ROOT accepted ten original intakes with 418 source placements and 81 unique
    paths; mechanism scope is explicit.
  snapshot_sha256: ffb4558e78e080f45baf4ccb369e72778c7e34de1c5b2fea82d2433818ea225a
- evidence_id: support-2217-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Complete accepted selected source scope, exact query frames and full matched
    payloads, direct companions, additional roles and input map.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-target-input-plan-acceptance-001.json
  locator: /status; /plan; /source_notes; /source_placements; /unique_source_paths;
    /per_order
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: ROOT accepted original source plan; exact maps and current pins joined
    to actual inventory.
  snapshot_sha256: 87cb8226f49b19e0cf589a83c45de342083de01cee4ee071fdbbf31209fdc719
- evidence_id: support-2217-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-scope-notes-001.json
  locator: /reading; /cautions
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Complete team reading attribution and source-grade/citation/assay limits.
    Support personally read its 35 contexts/315 frames/221 payloads/86 cached stanzas;
    BGC owns the disjoint first-five payload/cache partition.
  snapshot_sha256: 462e1f8450cc46b50f7e764c6be3a6fec2300b65d200898c74a5e562934ad86e
- evidence_id: support-2217-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Bounded 290-token, case-sensitive literal scan over all physical lines
    of eight explicitly opened admitted curation tables, including ignored files,
    found no matches; not a global absence claim.
  snapshot_sha256: 462e1f8450cc46b50f7e764c6be3a6fec2300b65d200898c74a5e562934ad86e
- evidence_id: support-2217-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/declared_structure; /records/6/smiles; /records/6/inchi; /records/6/comparisons;
    /records/6/atom_correspondence
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Both stored forms agree on formula, charge, standardized identifiers and
    canonical isomeric/nonisomeric SMILES. The complete 17-atom correspondence remains
    a bounded substructure match, with full_graph_identity_established:false. Neither
    saved form reports potential tetrahedral or double-bond stereo, and literal stereo_complete:true
    is retained. These saved fields do not establish natural-isolate stereochemistry.
  snapshot_sha256: d6777b269b79f346e064435d16f6783b96b6dc0d84d181802a8be587185ebc61
- evidence_id: support-2217-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed; /records/6/inchi/computed
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Complete paired atom/bond/neighborhood/charge/isotope/stereo/ring/motif
    tables personally read. Formula C10H4Br5NO; atom/bond counts 17/18. These saved
    computations do not establish natural identity.
  snapshot_sha256: d6777b269b79f346e064435d16f6783b96b6dc0d84d181802a8be587185ebc61
- evidence_id: support-2217-chemistry-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /external_requests; /retries
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Original ROOT 20 stored-form diagnostic completed once with exit 0; original
    stderr is separately retained, not silently assigned by owner.
  snapshot_sha256: 85c80b572f1dfcc5327af049840e7782ce70bd60561981e190e188f70b4ef340
- evidence_id: support-2217-chemistry-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-chemistry-acceptance-001.json
  locator: /status; /DATA; /execution; /molecular_parse_attempts; /false_comparisons;
    /warning_count; /warning_scope
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: ROOT accepted original 20-form run; four original global undefined-stereo
    warnings remain unassigned. All last-five comparisons are true, without full-identity
    inference.
  snapshot_sha256: ed41c7b477fc10da9308cd55cfe70fe0b682312dec7fc5d153d824d02ad41ad8
- evidence_id: support-2217-warnings
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-001.stderr
  locator: Complete original stderr, lines 1-8.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Four original undefined-stereo warnings are global, without a record assignment.
  snapshot_sha256: 1d81eb6af324b1767157c521ae036b492f4e95c03c0e07b6d37c63335d1b01a3
- evidence_id: support-2217-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-native-gates-acceptance-001.json
  locator: /status; /local_commands_passed; /selected_queue_rows; /unavailable_required_gates;
    /all_native_gates_passed
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Five local native commands passed. Full QC and ontology-consistency/OAK
    remain unavailable; all-native-gates-passed is false.
  snapshot_sha256: c2001fae878fca8947ab9a9a883c8f4c8bb09101fd0bed77c7e7c90c4d87f9a7
- evidence_id: support-2217-source-ownership
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/intakes/2217-inspect-001.json
  locator: /targets/0/owner_paths; /targets/0/ownership_note
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Exact maintained ownership from actual intake; seeded facts belong to inventories/extractors/seeder
    and curator graphs/history remain separate.
  snapshot_sha256: 3d1149fb63bd4f492f60e7fc528e524a94ab69a3b25bfbceeea41c6ba28e6596
- evidence_id: support-2217-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165-173.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Maintained stereo_complete derives from unassigned atom-centre detection;
    it does not independently establish all geometric, axial or natural stereochemistry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2217-classification-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 406-432.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: ComputedClassification explicitly represents a named/versioned prediction,
    never a source assertion or admission reason.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2217-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 1011-1019.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Maintained seeder preserves the classifier model/version and reported labels/glycoside
    Boolean.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2217-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Lines 35-57.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Review scope distinguishes exact structure, source grades, computed classification
    and maintained ownership; reserved decisions.tsv is not an effective repair owner.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2217-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Retained query predicate: exact complete standard_inchi_key equality;
    query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 3 complete matched rows. Empty matches are
    limited to this saved source query.'
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 970-970; exact row SHA256 4d5ba7804629a2d073bbc1c101dbc9df5a84874172db7203deb2f52c2be2ad94.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete retained mibig_compounds payload: {"mibig_accession":"BGC0000890","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"pentabromopseudilin","compound_index":"1","smiles":"C1=C(C=C(C(=C1C2=C(C(=C(N2)Br)Br)Br)O)Br)Br","standard_inchi":"InChI=1S/C10H4Br5NO/c11-3-1-4(9(17)5(12)2-3)8-6(13)7(14)10(15)16-8/h1-2,16-17H","standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:324093","taxon_id":"NCBITaxon:1315281","taxon_label":"Pseudoalteromonas
    phenolica O-BC30","bgc_classes":"other","bgc_subclasses":"aminocoumarin","genome_accession":"KF540211.1","locus_from":"","locus_to":"","locus_evidence_methods":"Heterologous
    expression","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:24974229","reference_basis":"ENTRY"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2217-row-mibig_compounds-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 971-971; exact row SHA256 8a8585f03dde595ac075866339ae9c400fbd4f62160cea885a28f32883c2b2f5.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete retained mibig_compounds payload: {"mibig_accession":"BGC0000891","entry_version":"4","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"pentabromopseudilin","compound_index":"1","smiles":"C1=C(C=C(C(=C1Br)O)C2=C(C(=C(N2)Br)Br)Br)Br","standard_inchi":"InChI=1S/C10H4Br5NO/c11-3-1-4(9(17)5(12)2-3)8-6(13)7(14)10(15)16-8/h1-2,16-17H","standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"","taxon_id":"NCBITaxon:1353533","taxon_label":"Pseudoalteromonas
    luteoviolacea 2ta16","bgc_classes":"other","bgc_subclasses":"aminocoumarin","genome_accession":"AUSV01000133.1","locus_from":"32483","locus_to":"43745","locus_evidence_methods":"Enzymatic
    assays|Heterologous expression|Gene expression correlated with compound production","producer_evidence_basis":"BGC_CORRELATED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:24974229","reference_basis":"ENTRY"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2217-row-mibig_compounds-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 1778-1778; exact row SHA256 3b1a7b2f1c9d6df02ba25eca0d7d92df5bc81338eefed37d63f4e620639c4b40.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete retained mibig_compounds payload: {"mibig_accession":"BGC0001465","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"pentabromopseudilin","compound_index":"3","smiles":"C1=C(C=C(C(=C1C2=C(C(=C(N2)Br)Br)Br)O)Br)Br","standard_inchi":"InChI=1S/C10H4Br5NO/c11-3-1-4(9(17)5(12)2-3)8-6(13)7(14)10(15)16-8/h1-2,16-17H","standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:324093","taxon_id":"NCBITaxon:717774","taxon_label":"Marinomonas
    mediterranea MMB-1","bgc_classes":"other","bgc_subclasses":"other","genome_accession":"NC_015276.1","locus_from":"4521275","locus_to":"4533494","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:24974229","reference_basis":"ENTRY"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2217-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Retained query predicate: exact complete standard_inchi_key equality;
    query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 0 complete matched rows. Empty matches are
    limited to this saved source query.'
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Retained query predicate: exact complete standard_inchi_key equality;
    query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 2 complete matched rows. Empty matches are
    limited to this saved source query.'
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 4325-4325; exact row SHA256 66d9caaceaab43e8e9cdd3840781708ad1d3c346c27f7052adfcfef51efced91.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete retained lotus_occurrences payload: {"standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","organism_name":"Pseudoalteromonas
    luteoviolacea","taxon_id":"NCBITaxon:43657","organism_wikidata":"http://www.wikidata.org/entity/Q7254487","reference_doi":"10.1021/JO00092A020","structure_wikidata":"http://www.wikidata.org/entity/Q27138952"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2217-row-lotus_occurrences-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 4326-4326; exact row SHA256 9bb2ec1b974b3462f4a8a847c0aa8db74b061006252752a49ada85a8ab4b3802.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete retained lotus_occurrences payload: {"standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","organism_name":"Pseudoalteromonas
    luteoviolacea","taxon_id":"NCBITaxon:43657","organism_wikidata":"http://www.wikidata.org/entity/Q7254487","reference_doi":"10.1021/NP100506Z","structure_wikidata":"http://www.wikidata.org/entity/Q27138952"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2217-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Retained query predicate: exact complete standard_inchi_key equality;
    query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 0 complete matched rows. Empty matches are
    limited to this saved source query.'
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Retained query predicate: exact complete standard_inchi_key equality;
    query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 1 complete matched rows. Empty matches are
    limited to this saved source query.'
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 1429-1429; exact row SHA256 beb18c608485e63721849f3db019b1abf86b19a6d98b5b873f55ba3e52a119c1.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete retained npclassifier payload: {"standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","smiles":"C1=C(C=C(C(=C1C2=C(C(=C(N2)Br)Br)Br)O)Br)Br","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Diphenyl ethers (DPEs)","class_results":"Marine-bacterial
    DPEs","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2217-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Retained query predicate: exact complete standard_inchi_key equality;
    query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 1 complete matched rows. Empty matches are
    limited to this saved source query.'
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-row-pubchem_bioassay-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 3813-3813; exact row SHA256 d777329f267f281991aef980ec86f24b67d490732117db3cccd218c9c48bc074.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete retained pubchem_bioassay payload: {"standard_inchi_key":"LXMNWKJHYOZUQL-UHFFFAOYSA-N","cid":"324093","aid":"977608","assay_name":"Experimentally
    measured binding affinity data (IC50) for protein-ligand complexes derived from
    PDB","assay_type":"Other","depositor":"Shanghai Institute of Organic Chemistry","activity_outcome":"Active","activity_name":"IC50","activity_value_um":"1.4","target_accession":"","reference":"PMID:24446431"}'
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2217-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Retained query predicate: exact complete standard_inchi_key equality;
    query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 0 complete matched rows. Empty matches are
    limited to this saved source query.'
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Retained query predicate: exact complete standard_inchi_key equality;
    query="LXMNWKJHYOZUQL-UHFFFAOYSA-N"; 0 complete matched rows. Empty matches are
    limited to this saved source query.'
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Retained query predicate: exact chebi_id from exact full-key structure
    rows; query=[]; 0 complete matched rows. Empty matches are limited to this saved
    source query.'
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-taxon-43657
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: Complete OBO stanza, physical lines 19827-19833.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete pinned cached stanza: [Term]

    id: NCBITaxon:43657

    name: Pseudoalteromonas luteoviolacea

    synonym: "Alteromonas luteiviolacea" EXACT []

    synonym: "Alteromonas luteo-violaceus" EXACT []

    synonym: "Alteromonas luteoviolacea" EXACT []. No fresh taxonomy authority request
    was made.'
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2217-taxon-717774
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: Complete OBO stanza, physical lines 109081-109086.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete pinned cached stanza: [Term]

    id: NCBITaxon:717774

    name: Marinomonas mediterranea MMB-1

    synonym: "Marinomonas mediterranea str. MMB-1" EXACT []

    synonym: "Marinomonas mediterranea strain MMB-1" EXACT []. No fresh taxonomy authority
    request was made.'
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2217-taxon-1315281
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: Complete OBO stanza, physical lines 126091-126094.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete pinned cached stanza: [Term]

    id: NCBITaxon:1315281

    name: Pseudoalteromonas phenolica O-BC30. No fresh taxonomy authority request
    was made.'
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2217-taxon-1353533
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: Complete OBO stanza, physical lines 127330-127333.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete pinned cached stanza: [Term]

    id: NCBITaxon:1353533

    name: Pseudoalteromonas luteoviolacea 2ta16. No fresh taxonomy authority request
    was made.'
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2217-taxon-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/source_taxa; /records/6/source_scope_inventory/forward_taxon_merge_matches;
    /records/6/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Exact selected source taxon IDs and saved forward-merge/nonorganism route
    matches; all five selected last-five routes have no such matched rows.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-companion-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /raw_unselected_companions/0
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: context_only
  summary: Complete direct-context owner/history and retained source scope for bistribromopyrrole,
    key CKUAYXRLIBAUTH-UHFFFAOYSA-N. Its distinct structure, grades, citations and
    activity are context only; whole raw reading is attributed in source notes.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-companion-9
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /raw_unselected_companions/9
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: context_only
  summary: Complete direct-context owner/history and retained source scope for bromophene,
    key TXODBIOSWNNKJM-UHFFFAOYSA-N. Its distinct structure, grades, citations and
    activity are context only; whole raw reading is attributed in source notes.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: support-2217-activity-classifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 128-178; 1310-1381; 1456-1468.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: IC50/Ki/binding-title fallback assigns ENZYME_INHIBITOR to Active rows;
    positive summary derives from classified written observations and separately admitted
    sibling classes.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2217-activity-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 273-285; 631-653; 920-940.
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: activity_class is optional; every asserted activity class and summary needs
    supporting evidence. The enum has no dedicated enzyme-inhibitor definition; the
    present concern follows source method and classifier support scope.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2217-activity-written
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/6/owner_document/bioactivities; /records/6/owner_document/bioactivity_summary
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'One exact written observation: AID 977608, Active binding IC50=1.4 uM,
    with inferred ENZYME_INHIBITOR and sole summary.'
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: support-2217-reader-data
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-pentabromopseudilin-maintained-reader-DATA-001.json
  locator: /raw_owner; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner;
    /counts; /review_check_metadata; /denials; /unexpected_denials; /errors; /limitations
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Original single maintained call preserved every owner field and history,
    one 5-node/4-edge graph and one pathway step; zero components/targets. One known
    socket capability probe was denied before action, no requests or unexpected denials.
    Scientific assertions remain historical.
  snapshot_sha256: 7af0b792cd29d6fd4cf3f23629bd14f78c409ae80ac59f87121bbad16012566e
- evidence_id: support-2217-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-pentabromopseudilin-reader-execution-001.json
  locator: /command; /source; /configuration; /stdout; /stderr; /exit_code; /original_tool;
    /original_start_tool; /DATA; /external_requests
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Native original 940c4a/session60327→b80152/exit 0, no replay; full execution
    and saved streams retain provenance.
  snapshot_sha256: 04037e74c2c2914a915eae0e578399b91320bf9094f5d970540081bbee68e6aa
- evidence_id: support-2217-reader-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-pentabromopseudilin-maintained-reader-acceptance-001.json
  locator: /status; /DATA; /execution; /verification; /review_check_contract
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: ROOT accepted exact complete-owner equality and original exit 0; the strict
    review-check name/command/status is inherited.
  snapshot_sha256: c6bbc06bff2bb388657deb50894dcd34595b68e33be8fae9c83d519b4d9fa744
- evidence_id: support-2217-mechanism-graph
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-pentabromopseudilin-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/0
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: 'Complete Bmp7 graph personally read: five nodes, four edges, eight reference
    placements. Historical primary snippets and protein/database assertions retain
    their original source scopes.'
  snapshot_sha256: 7af0b792cd29d6fd4cf3f23629bd14f78c409ae80ac59f87121bbad16012566e
- evidence_id: support-2217-mechanism-pathway
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-pentabromopseudilin-maintained-reader-DATA-001.json
  locator: /resolved_view/biosynthetic_pathway/0; /resolved_view/curation_history
  accessed_at: '2026-11-03T12:23:30.457436Z'
  support: supports
  summary: Complete Bmp7 pathway step and five evidence placements plus all four owner-history
    events; no fresh sequence/API/primary verification.
  snapshot_sha256: 7af0b792cd29d6fd4cf3f23629bd14f78c409ae80ac59f87121bbad16012566e
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-222/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json
  accessed_at: '2026-11-03T12:07:39.701654Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 4f6c07dfc2254087e012d48e7a6d242e51e6b195e095bdc2467229664d4c931c
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-222/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json
  accessed_at: '2026-11-03T12:08:04.813276Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 818559c0ff31aaea2f5d6a6a1740192ce9592adb54e148b1ebc667bd3eb7ff12
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-222/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json
  accessed_at: '2026-11-03T12:08:24.829512Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-222/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json
  accessed_at: '2026-11-03T12:09:00.348743Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-222/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json
  accessed_at: '2026-11-03T12:09:12.342177Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: b39c06db8b8558cb63af7a2e2c475e60a3655c7289406305ecad80ab597ae7a4
assessments:
- assessment_id: support-2217-A1
  area: identity
  topic: Exact structure concept and grounding scope
  outcome: supported
  summary: Pentabromopseudilin retains the complete key LXMNWKJHYOZUQL-UHFFFAOYSA-N
    and C10H4Br5NO across three MIBiG source entries. Its retained exact-key ChEBI
    query is empty and the minted identifier is preserved. The shared-structure discussion
    remains open; agreeing keys alone do not independently adjudicate all upstream
    entry identities. Bistribromopyrrole and bromophene share BGC0001465 but have
    different full keys and structures, so their activities and source concepts do
    not transfer.
  target_ids:
  - naturalproductmech:mibig-005498ea51
  evidence_ids:
  - support-2217-owner
  - support-2217-capture
  - support-2217-intake
  - support-2217-source-plan
  - support-2217-plan-acceptance
  - support-2217-chemistry
  - support-2217-query-mibig_compounds
  - support-2217-query-chebi_structures
  - support-2217-row-mibig_compounds-0
  - support-2217-row-mibig_compounds-1
  - support-2217-row-mibig_compounds-2
  - support-2217-companion-0
  - support-2217-companion-9
  dimensions:
  - name: standard_inchi_key
    value: LXMNWKJHYOZUQL-UHFFFAOYSA-N
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-chemistry
    - support-2217-query-mibig_compounds
    - support-2217-query-chebi_structures
    - support-2217-row-mibig_compounds-0
    - support-2217-row-mibig_compounds-1
    - support-2217-row-mibig_compounds-2
    - support-2217-companion-0
    - support-2217-companion-9
  - name: grounding_scope
    value: MINTED; retained exact-key ChEBI query empty; three MIBiG entries
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-chemistry
    - support-2217-query-mibig_compounds
    - support-2217-query-chebi_structures
    - support-2217-row-mibig_compounds-0
    - support-2217-row-mibig_compounds-1
    - support-2217-row-mibig_compounds-2
    - support-2217-companion-0
    - support-2217-companion-9
- assessment_id: support-2217-A2
  area: representation
  topic: Paired representations and stereochemical limits
  outcome: supported
  summary: Both stored forms agree on formula, charge, standardized identifiers and
    canonical isomeric/nonisomeric SMILES. The complete 17-atom correspondence remains
    a bounded substructure match, with full_graph_identity_established:false. Neither
    saved form reports potential tetrahedral or double-bond stereo; literal stereo_complete:true
    remains an atom-centred source flag. No additional parse or natural-isolate stereochemical
    proof was performed.
  target_ids:
  - naturalproductmech:mibig-005498ea51
  evidence_ids:
  - support-2217-owner
  - support-2217-capture
  - support-2217-intake
  - support-2217-source-plan
  - support-2217-plan-acceptance
  - support-2217-chemistry
  - support-2217-stereo-method
  - support-2217-warnings
  - support-2217-chemistry-execution
  - support-2217-chemistry-acceptance
  dimensions:
  - name: stereochemical_resolution
    value: No potential stereo; literal true within atom-centre scope
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-chemistry
    - support-2217-stereo-method
    - support-2217-warnings
    - support-2217-chemistry-execution
    - support-2217-chemistry-acceptance
  - name: representation_correspondence
    value: All comparisons true; complete 17-atom map; full identity unproved
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-chemistry
    - support-2217-stereo-method
    - support-2217-warnings
    - support-2217-chemistry-execution
    - support-2217-chemistry-acceptance
- assessment_id: support-2217-A3
  area: provenance
  topic: Producer, occurrence and locus evidence grades
  outcome: supported
  summary: BGC0000891 version 4 retains Pseudoalteromonas luteoviolacea 2ta16/1353533
    as BGC_CORRELATED and its enzymatic/heterologous/expression evidence as CLUSTER_DEMONSTRATED,
    at AUSV01000133.1:32483–43745. BGC0000890 version 5 retains P. phenolica O-BC30/1315281
    as SOURCE_ASSERTION with a demonstrated heterologous locus on KF540211.1 and unstated
    coordinates. BGC0001465 version 5 retains Marinomonas mediterranea MMB-1/717774
    as SOURCE_ASSERTION with CLUSTER_UNSTATED at NC_015276.1:4521275–4533494. Two
    LOTUS species 43657 occurrences are distinct from these strain-specific producer
    assertions.
  target_ids:
  - naturalproductmech:mibig-005498ea51
  evidence_ids:
  - support-2217-owner
  - support-2217-capture
  - support-2217-intake
  - support-2217-source-plan
  - support-2217-plan-acceptance
  - support-2217-query-mibig_compounds
  - support-2217-query-lotus_occurrences
  - support-2217-query-chebi_origins
  - support-2217-taxon-routes
  - support-2217-source-notes
  - support-2217-row-mibig_compounds-0
  - support-2217-row-mibig_compounds-1
  - support-2217-row-mibig_compounds-2
  - support-2217-row-lotus_occurrences-0
  - support-2217-row-lotus_occurrences-1
  - support-2217-taxon-43657
  - support-2217-taxon-717774
  - support-2217-taxon-1315281
  - support-2217-taxon-1353533
  dimensions:
  - name: taxon_and_strain_scope
    value: Three strain taxa 1353533/1315281/717774; occurrence species 43657
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-query-mibig_compounds
    - support-2217-query-lotus_occurrences
    - support-2217-query-chebi_origins
    - support-2217-taxon-routes
    - support-2217-source-notes
    - support-2217-row-mibig_compounds-0
    - support-2217-row-mibig_compounds-1
    - support-2217-row-mibig_compounds-2
    - support-2217-row-lotus_occurrences-0
    - support-2217-row-lotus_occurrences-1
    - support-2217-taxon-43657
    - support-2217-taxon-717774
    - support-2217-taxon-1315281
    - support-2217-taxon-1353533
  - name: producer_evidence_tier
    value: BGC_CORRELATED for 0891; SOURCE_ASSERTION for 0890/1465
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-query-mibig_compounds
    - support-2217-query-lotus_occurrences
    - support-2217-query-chebi_origins
    - support-2217-taxon-routes
    - support-2217-source-notes
    - support-2217-row-mibig_compounds-0
    - support-2217-row-mibig_compounds-1
    - support-2217-row-mibig_compounds-2
    - support-2217-row-lotus_occurrences-0
    - support-2217-row-lotus_occurrences-1
    - support-2217-taxon-43657
    - support-2217-taxon-717774
    - support-2217-taxon-1315281
    - support-2217-taxon-1353533
  - name: locus_evidence_tier
    value: 0890/0891 CLUSTER_DEMONSTRATED; 1465 CLUSTER_UNSTATED
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-query-mibig_compounds
    - support-2217-query-lotus_occurrences
    - support-2217-query-chebi_origins
    - support-2217-taxon-routes
    - support-2217-source-notes
    - support-2217-row-mibig_compounds-0
    - support-2217-row-mibig_compounds-1
    - support-2217-row-mibig_compounds-2
    - support-2217-row-lotus_occurrences-0
    - support-2217-row-lotus_occurrences-1
    - support-2217-taxon-43657
    - support-2217-taxon-717774
    - support-2217-taxon-1315281
    - support-2217-taxon-1353533
- assessment_id: support-2217-A4
  area: evidence
  topic: Citation placement and historical verification scope
  outcome: supported
  summary: All three MIBiG producer/locus assertions use ENTRY PMID:24974229 as DATABASE_ASSERTION;
    the two LOTUS DOI triples retain occurrence scope. The activity row cites PMID:24446431.
    The curator-owned Bmp7 graph/pathway separately preserves historical PRIMARY_EXPERIMENT
    snippets from DOI:10.1038/nchembio.1564 and database assertions for V4HJ73, ESP90850.1
    and AUSV01000133.1. These citations and snippets were read as saved evidence,
    not freshly retrieved primary text, sequence verification or independent publication
    counts.
  target_ids:
  - naturalproductmech:mibig-005498ea51
  evidence_ids:
  - support-2217-owner
  - support-2217-capture
  - support-2217-intake
  - support-2217-source-plan
  - support-2217-plan-acceptance
  - support-2217-source-notes
  - support-2217-row-mibig_compounds-0
  - support-2217-row-mibig_compounds-1
  - support-2217-row-mibig_compounds-2
  - support-2217-row-lotus_occurrences-0
  - support-2217-row-lotus_occurrences-1
  - support-2217-row-npclassifier-0
  - support-2217-row-pubchem_bioassay-0
  - support-2217-taxon-43657
  - support-2217-taxon-717774
  - support-2217-taxon-1315281
  - support-2217-taxon-1353533
  - support-2217-companion-0
  - support-2217-companion-9
  - support-2217-reader-data
  - support-2217-reader-execution
  - support-2217-reader-acceptance
  dimensions:
  - name: citation_scope
    value: ENTRY PMID:24974229; historical Bmp7 primary/database assertions; assay
      PMID:24446431
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-source-notes
    - support-2217-row-mibig_compounds-0
    - support-2217-row-mibig_compounds-1
    - support-2217-row-mibig_compounds-2
    - support-2217-row-lotus_occurrences-0
    - support-2217-row-lotus_occurrences-1
    - support-2217-row-npclassifier-0
    - support-2217-row-pubchem_bioassay-0
    - support-2217-taxon-43657
    - support-2217-taxon-717774
    - support-2217-taxon-1315281
    - support-2217-taxon-1353533
    - support-2217-companion-0
    - support-2217-companion-9
    - support-2217-reader-data
    - support-2217-reader-execution
    - support-2217-reader-acceptance
- assessment_id: support-2217-A5
  area: scope
  topic: Occurrence, assay and companion boundaries
  outcome: concern
  summary: The sole retained selected PubChem row, physical line 3813 / AID 977608,
    reports an Active PDB protein–ligand binding-affinity IC50 of 1.4 uM, assay type
    Other, with blank target accession. The generated observation and sole bioactivity_summary
    both add ENZYME_INHIBITOR via the maintained IC50/binding-name fallback. That
    inference is not supported by an identified enzyme-inhibition method in this retained
    row. Preserve the literal assay, Active call, value, units and citation; omit
    the optional inferred class and rederive the summary unless separately inspected
    evidence supports it. This support gap does not establish inactivity or deny real
    inhibitory pharmacology. Empty BindingDB/sibling matches and the biosynthetic
    Bmp7 graph provide no alternative activity backing here.
  target_ids:
  - naturalproductmech:mibig-005498ea51
  evidence_ids:
  - support-2217-owner
  - support-2217-capture
  - support-2217-intake
  - support-2217-source-plan
  - support-2217-plan-acceptance
  - support-2217-query-mibig_compounds
  - support-2217-query-chebi_structures
  - support-2217-query-lotus_occurrences
  - support-2217-query-cyanometdb_occurrences
  - support-2217-query-npclassifier
  - support-2217-query-pubchem_bioassay
  - support-2217-query-bindingdb_targets
  - support-2217-query-antibioticmech_inchikeys
  - support-2217-query-chebi_origins
  - support-2217-row-mibig_compounds-0
  - support-2217-row-mibig_compounds-1
  - support-2217-row-mibig_compounds-2
  - support-2217-row-lotus_occurrences-0
  - support-2217-row-lotus_occurrences-1
  - support-2217-row-npclassifier-0
  - support-2217-row-pubchem_bioassay-0
  - support-2217-companion-0
  - support-2217-companion-9
  - support-2217-taxon-43657
  - support-2217-taxon-717774
  - support-2217-taxon-1315281
  - support-2217-taxon-1353533
  - support-2217-activity-written
  - support-2217-activity-classifier
  - support-2217-activity-schema
  dimensions:
  - name: occurrence_scope
    value: Two LOTUS occurrence assertions; two distinct-key direct companions
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-query-mibig_compounds
    - support-2217-query-chebi_structures
    - support-2217-query-lotus_occurrences
    - support-2217-query-cyanometdb_occurrences
    - support-2217-query-npclassifier
    - support-2217-query-pubchem_bioassay
    - support-2217-query-bindingdb_targets
    - support-2217-query-antibioticmech_inchikeys
    - support-2217-query-chebi_origins
    - support-2217-row-mibig_compounds-0
    - support-2217-row-mibig_compounds-1
    - support-2217-row-mibig_compounds-2
    - support-2217-row-lotus_occurrences-0
    - support-2217-row-lotus_occurrences-1
    - support-2217-row-npclassifier-0
    - support-2217-row-pubchem_bioassay-0
    - support-2217-companion-0
    - support-2217-companion-9
    - support-2217-taxon-43657
    - support-2217-taxon-717774
    - support-2217-taxon-1315281
    - support-2217-taxon-1353533
    - support-2217-activity-written
    - support-2217-activity-classifier
    - support-2217-activity-schema
  - name: assay_scope
    value: One Active PDB-binding IC50; unsupported ENZYME_INHIBITOR class/summary
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-query-mibig_compounds
    - support-2217-query-chebi_structures
    - support-2217-query-lotus_occurrences
    - support-2217-query-cyanometdb_occurrences
    - support-2217-query-npclassifier
    - support-2217-query-pubchem_bioassay
    - support-2217-query-bindingdb_targets
    - support-2217-query-antibioticmech_inchikeys
    - support-2217-query-chebi_origins
    - support-2217-row-mibig_compounds-0
    - support-2217-row-mibig_compounds-1
    - support-2217-row-mibig_compounds-2
    - support-2217-row-lotus_occurrences-0
    - support-2217-row-lotus_occurrences-1
    - support-2217-row-npclassifier-0
    - support-2217-row-pubchem_bioassay-0
    - support-2217-companion-0
    - support-2217-companion-9
    - support-2217-taxon-43657
    - support-2217-taxon-717774
    - support-2217-taxon-1315281
    - support-2217-taxon-1353533
    - support-2217-activity-written
    - support-2217-activity-classifier
    - support-2217-activity-schema
- assessment_id: support-2217-A6
  area: other
  topic: Computed classification and full-table topology limits
  outcome: concern
  summary: Both complete graphs contain a brominated phenyl ring joined directly by
    C–C to a brominated [nH] pyrrole, with a terminal phenolic oxygen and five bromines.
    There is no C–O–C ether bridge; the single oxygen is not a diphenyl-ether linker.
    NPClassifier's Diphenyl ethers/Marine-bacterial DPEs is therefore a model-applicability
    concern, retained explicitly as a versioned prediction rather than asserted topology
    or evidence of wrong compound identity. No raw prediction is overwritten.
  target_ids:
  - naturalproductmech:mibig-005498ea51
  evidence_ids:
  - support-2217-owner
  - support-2217-capture
  - support-2217-intake
  - support-2217-source-plan
  - support-2217-plan-acceptance
  - support-2217-chemistry
  - support-2217-topology
  - support-2217-classification-schema
  - support-2217-classification-seeder
  - support-2217-query-npclassifier
  - support-2217-row-npclassifier-0
  dimensions:
  - name: computed_classification
    value: Versioned DPE prediction conflicts with phenyl–pyrrole C–C topology
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-chemistry
    - support-2217-topology
    - support-2217-classification-schema
    - support-2217-classification-seeder
    - support-2217-query-npclassifier
    - support-2217-row-npclassifier-0
- assessment_id: support-2217-A7
  area: completeness
  topic: Partial completion and maintained ownership
  outcome: unknown
  summary: The accepted maintained reader is required for this selected owner and
    its one inline Bmp7 graph plus pathway step; its saved result establishes complete-owner
    preservation within the local read contract. It does not verify the historical
    chemistry, protein databases or activity interpretation. The unsupported activity-class
    inference requires curation; the review remains partial because full QC/OAK and
    fresh primary/authority verification are unavailable. Proposed repair belongs
    to the maintained classifier and regeneration, not hand-editing generated observations
    or raw source calls.
  target_ids:
  - naturalproductmech:mibig-005498ea51
  evidence_ids:
  - support-2217-owner
  - support-2217-capture
  - support-2217-intake
  - support-2217-source-plan
  - support-2217-plan-acceptance
  - support-2217-intake-ready
  - support-2217-native-acceptance
  - support-2217-source-ownership
  - support-2217-source-notes
  - support-2217-curation-scope
  - support-2217-chemistry-acceptance
  - support-2217-review-profile
  - support-2217-reader-data
  - support-2217-reader-execution
  - support-2217-reader-acceptance
  dimensions:
  - name: review_completion
    value: partial; accepted complete-owner reader; scoped activity curation required
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2217-owner
    - support-2217-capture
    - support-2217-intake
    - support-2217-source-plan
    - support-2217-plan-acceptance
    - support-2217-intake-ready
    - support-2217-native-acceptance
    - support-2217-source-ownership
    - support-2217-source-notes
    - support-2217-curation-scope
    - support-2217-chemistry-acceptance
    - support-2217-review-profile
    - support-2217-reader-data
    - support-2217-reader-execution
    - support-2217-reader-acceptance
- assessment_id: support-2217-A8
  area: graph
  topic: Complete maintained Bmp7 biosynthetic scope
  outcome: supported
  summary: The complete accepted owner preserves one BIOSYNTHESIS graph with 5 nodes,
    4 edges and 8 graph-evidence placements and one pathway step with 5 evidence placements;
    there are no component references or molecular targets. The graph distinguishes
    dibromophenol and ungrounded tribromopyrrole precursors, Bmp7, the oxidative-heterocoupling
    process and the exact minted product. Historical notes describe purified Bmp7
    with Bmp9/Bmp10/NADH and authentic-standard comparison. Those scoped biosynthetic
    assertions do not make Bmp7 a pharmacological target or support ENZYME_INHIBITOR.
    The pathway's historical one-substrate explanation is not treated as a statement
    of the current schema's capabilities.
  target_ids:
  - naturalproductmech:mibig-005498ea51
  evidence_ids:
  - support-2217-owner
  - support-2217-capture
  - support-2217-intake
  - support-2217-source-plan
  - support-2217-plan-acceptance
  - support-2217-reader-data
  - support-2217-reader-execution
  - support-2217-reader-acceptance
  - support-2217-mechanism-graph
  - support-2217-mechanism-pathway
  - support-2217-source-ownership
  - support-2217-query-mibig_compounds
  - support-2217-row-mibig_compounds-0
  - support-2217-row-mibig_compounds-1
  - support-2217-row-mibig_compounds-2
  dimensions: []
- assessment_id: support-2217-A9
  area: grounding
  topic: Organism-specific protein assertions and verification limits
  outcome: unknown
  summary: The saved curator assertions identify P. luteoviolacea 2ta16 Bmp7 as UniProtKB:V4HJ73,
    locus PL2TA16_01241 and NCBI_Protein:ESP90850.1, with AUSV01000133.1:42270–43745
    inside the stated BGC0000891 interval. These identifiers describe the same asserted
    organism-specific enzyme example within the saved record; ungrounded substrate/process
    nodes remain explicit. No original article/API response or protein sequence was
    inspected in this review, and the maintained reader does not independently establish
    sequence, enzymatic specificity or present database status.
  target_ids:
  - naturalproductmech:mibig-005498ea51
  evidence_ids:
  - support-2217-owner
  - support-2217-capture
  - support-2217-intake
  - support-2217-source-plan
  - support-2217-plan-acceptance
  - support-2217-reader-data
  - support-2217-reader-execution
  - support-2217-reader-acceptance
  - support-2217-mechanism-graph
  - support-2217-mechanism-pathway
  - support-2217-source-ownership
  - support-2217-query-mibig_compounds
  - support-2217-row-mibig_compounds-0
  - support-2217-row-mibig_compounds-1
  - support-2217-row-mibig_compounds-2
  dimensions: []
findings:
- finding_id: support-2217-binding-class-scope
  issue_key: pentabromopseudilin-pdb-binding-enzyme-inhibitor-overstatement
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Generic PDB binding observation does not support the inferred enzyme-inhibitor
    class
  description: 'The sole written observation at bioactivities[0] is retained PubChem
    physical row3813/AID977608: Active, IC50=1.4uM, assay type Other, protein–ligand
    complexes derived from PDB, blank target accession and PMID:24446431. The maintained
    IC50/binding-name fallback adds ENZYME_INHIBITOR without an identified enzyme-inhibition
    method in that row, then derives the sole matching summary. The support gap concerns
    that inferred class and summary, not the literal measurement or whether Pentabromopseudilin
    can inhibit an enzyme in other evidence. No selected BindingDB/sibling result
    or pharmacological target backs the class here; the Bmp7 graph is biosynthetic
    and cannot substitute for such backing.'
  target_ids:
  - naturalproductmech:mibig-005498ea51
  field_paths:
  - bioactivities[0].activity_class
  - bioactivity_summary[0]
  evidence_ids:
  - support-2217-activity-written
  - support-2217-row-pubchem_bioassay-0
  - support-2217-query-pubchem_bioassay
  - support-2217-activity-classifier
  - support-2217-activity-schema
  - support-2217-review-profile
  - support-2217-query-bindingdb_targets
  - support-2217-query-antibioticmech_inchikeys
  - support-2217-mechanism-graph
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained activity classifier, observation insertion and derived-summary
      owner
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/shikimates_and_phenylpropanoids/pentabromopseudilin.yaml
    role: Generated affected observation and summary; regenerate after maintained
      correction
  ownership_note: Repair maintained classifier support scope and regenerate. Preserve
    the raw assay observation; excluding the whole assay through the exclusion table
    would discard supported source data. Reserved decisions.tsv is not consumed.
  normalization_reason: Major unsupported scientific activity typing despite passing
    local schema/reproduction gates. The enum has no dedicated ENZYME_INHIBITOR definition;
    the finding rests on exact retained assay scope and the classifier unambiguity
    contract.
  disposition_reason: Confirmed source-to-generated-inference gap, rather than a claim
    of inactivity or a consequence of unavailable external sources.
actions:
- action_id: support-2217-repair-binding-classification
  description: Narrow maintained classify_activity so this exact generic PDB-binding
    title does not receive ENZYME_INHIBITOR solely from IC50 or binding. Omit the
    optional activity_class unless independently inspected appropriate evidence supports
    it. Preserve the Active call, full title, AID977608, IC50=1.4uM, blank target
    and PMID:24446431. Recompute the summary from justified written/target/sibling
    support; with only the currently retained observation corrected and no alternative
    backing here, ENZYME_INHIBITOR no longer has support in the summary. Preserve
    the biosynthetic Bmp7 graph/pathway and all source/history content.
  finding_ids:
  - support-2217-binding-class-scope
  target_ids:
  - naturalproductmech:mibig-005498ea51
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained activity classifier, observation insertion and derived-summary
      owner
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/shikimates_and_phenylpropanoids/pentabromopseudilin.yaml
    role: Generated affected observation and summary; regenerate after maintained
      correction
  ownership_note: Proposed maintained-source correction only; no record/source edit
    or additional retrieval was performed.
  acceptance_checks:
  - The exact retained assay observation survives unchanged except omission of its
    unsupported optional activity_class.
  - The sole unsupported ENZYME_INHIBITOR summary is removed on regeneration unless
    separately inspected and appropriately admitted evidence provides backing.
  - Regression checks distinguish generic PDB binding from explicitly supported enzyme-inhibition
    observations; do not discard activity calls or transfer companion claims.
  - After future authorized implementation, regenerate through the maintained seeder
    and run required strict/reproduction/corpus/review checks.
  generator: scripts/seed_from_sources.py
limitations:
- Full QC and complete ontology authority coverage/OAK were unavailable; passing five
  local gates does not establish scientific completeness.
- No external retrieval, live taxonomy/identifier/protein queries or publication verification
  was performed. These assessments use the original saved owner-form computations;
  no additional molecular parses were performed during fragment authoring.
- Database citations, cached taxonomy, historical primary labels and versioned model
  predictions retain their stated evidence types. Matching stored identifiers does
  not establish natural identity, independent publication support or complete natural
  stereochemistry.
- No source record or curation history was edited by this review. Canonical review
  persistence and campaign operations are separately ROOT-owned.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Selected mechanism scope is the complete accepted Bmp7 graph/pathway, with no components;
  this is distinct from fresh primary/protein/pharmacology verification.
- Native ignored-inclusive saved-review continuity search 674c12/873852 and exact-hit
  read 72416e found only a prior bromophene companion mention, not a same-owner review/issue_key
  within W review.yaml/completed-review.yaml and R/reviews/structured. No global absence
  claim or other-owner issue-key reuse.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-222
```
