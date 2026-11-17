# Local evidence review: tropodithietic acid

- Review: 20261103T133012Z-tropodithietic-acid
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T13:02:50.368088Z
- Finished UTC: 2026-11-03T13:30:12.795292Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Tropodithietic acid has coherent retained ChEBI/MIBiG structure and bounded source provenance. Its 25 written cell-growth observations, 16 omitted retained results and exact sibling ANTIBACTERIAL assertion remain distinct. No supported local curation defect is established within the saved evidence; the review is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2225; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156455 | data/natural_products/shikimates_and_phenylpropanoids/tropodithietic-acid.yaml | generated | tropodithietic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:156455 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:156455 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:156455 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:156455 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:156455 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:156455 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:156455 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:156455 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: CHEBI:156455.

CHEBI:156455, its three-star retained structure row and the MIBiG BGC0000932 v5 compound match BLFCMITWMARUSM-UHFFFAOYSA-N and both saved forms. The bicyclic sulfur-containing carboxylic-acid part of the ChEBI definition agrees with the observed topology. Its broad-spectrum antibiotic, producer and low-concentration signalling wording remains an attributed database definition, not fresh functional verification. The hydroxylated same-locus companion has a different full key and is not substituted for this owner.

### Representation

representation: supported. Targets: CHEBI:156455.

Both forms give neutral C8H4O3S2, 13 atoms and 14 bonds, with no potential stereo element reported. All ten comparisons are true and the saved atom correspondence is complete. The seven-carbon ring and fused four-membered C2S2 ring, including the S–S bond, are preserved; carboxylic acid and ring carbonyl are explicit. Aromatic normalization and identifier agreement do not establish a solution-state tautomer, redox mechanism or natural sample identity.

### Origin

provenance: supported. Targets: CHEBI:156455.

MIBiG BGC0000932 v5 attributes Phaeobacter inhibens DSM17395 (391619) at SOURCE_ASSERTION grade and its CP002977.1 locus at CLUSTER_UNSTATED; the entry is active/questionable with unknown completeness. The six written occurrences comprise three LOTUS and three ChEBI-origin assertions across species221822, species60890, strain391619 and genus2433. The producer/occurrence overlap is explicitly qualified for publication independence. Cached strain391619 has the historical P. gallaeciensis DSM17395 synonym; it does not merge species60890 with P. inhibens or collapse strain and genus scopes.

### Citations

evidence: unknown. Targets: CHEBI:156455.

PMID:24723119 is the MIBiG entry citation. LOTUS retains DOI:10.1039/C4CC01924E, DOI:10.1128/MBIO.02118-15 and DOI:10.1128/AEM.70.4.2560-2565.2003; ChEBI origins retain PMIDs21430694,28389641 and25161739. These assertion roles and possible overlap are preserved without counting independent papers. PubChem rows cite their AIDs because the retained reference field is blank. The exact AntibioticMech full-key row is a separate coarse activity assertion, not a primary assay or target mechanism.

### Bioactivity

evidence: supported. Targets: CHEBI:156455.

All 41 retained PubChem rows are Active single-concentration NCI human-tumor cell-growth screens. The owner writes 25 ACTIVE/CYTOTOXIC observations and explicitly notes 16 omitted results. The retained endpoint, value, target accession and reference fields are blank: no IC50, dose response, molecular target or cell-killing mechanism can be inferred. The coarse CYTOTOXIC bucket is supported at the stated cell-growth-screen level, without equating growth inhibition with proven cell death. Several literal assay titles repeat a lung-cell descriptor across differently named lines; these source labels are preserved without a fresh lineage correction. ANTIBACTERIAL is separately backed by the exact-key AntibioticMech row159 and SAME_STRUCTURE link. No selected target/mechanism root is written, and none transfers from the hydroxylated companion.

### Classification

consistency: unknown. Targets: CHEBI:156455.

The topology is a seven-membered tropone-like carbon ring fused to a four-membered ring containing two adjacent sulfurs, with one carboxylic acid and one ring carbonyl. No sugar, amide or amino group is present in the complete tables. NPClassifier Tropolones/Tropolones and derivatives (Shikimate) is compatible as a computed scaffold description, while the MIBiG OTHER source BGC class remains a separate assertion. Neither the classifier nor the sulfur motif demonstrates a biochemical reaction mechanism.

### Completion

completeness: unknown. Targets: CHEBI:156455.

The complete owner/history, admitted source context, actual intake and all paired saved molecular tables were reviewed. No supported local curation defect is established within this scope. Five local gates passed, while full QC, OAK and external primary-source/taxonomy/accession verification were unavailable. The review remains partial; no record, native curation status or history was changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2225-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/tropodithietic-acid.yaml; Whole owner plaintext and complete curation_history | supports | Complete owner and append-only history, personally read as exact saved plaintext and rejoined to this current raw pin. |
| bgc-2225-capture | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/4/owner_pin; /records/4/owner_document | supports | Complete captured owner and its exact source pin; no source fields or native history were edited. |
| bgc-2225-intake | /private/tmp/npm-review-work/shared-next-batch223/intakes/2225-inspect-001.json; /source; /targets | supports | Actual canonical intake source, complete input map and target/maintained-owner scope. |
| bgc-2225-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-intake-ready-001.json; /status; /intake_summary | supports | ROOT acceptance of the original ten canonical intakes, with no replay. |
| bgc-2225-grounding-owner | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/4/owner_document/chemical_structure; /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status | supports | Written structure, source concepts and grounding decision, without fresh external resolution. |
| bgc-2225-origin-owner | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters | supports | Complete written producer and locus assertions, including evidence grades, source versions, methods and references. |
| bgc-2225-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/4/owner_document/occurrences | supports | Complete written occurrences and their cited scope. |
| bgc-2225-assay-owner | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete captured owner supports the written assay, summary, target and mechanism fields or their absence; source-query-only facts belong to separate evidence. |
| bgc-2225-classification-owner | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/4/owner_document/np_classification; /records/4/owner_document/bgc_class | supports | Named-model prediction and source BGC class are preserved as separate assertions. |
| bgc-2225-source-plan | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4 | supports | Complete admitted selected context, direct companions, raw/history and exact input map. |
| bgc-2225-source-notes | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-scope-notes-001.json; /reading; /curation; /cautions | supports | Complete reading attribution and bounded curation scope: 135 literal tokens across eight explicit files, with five out-of-scope shared-taxon hits rather than zero textual matches. |
| bgc-2225-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-input-plan-acceptance-001.json; /status; /plan; /notes; /inventory; /per_order_counts | supports | ROOT acceptance of this original saved source plan, notes and exact per-order input counts. |
| bgc-2225-chemistry | /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/smiles; /records/4/inchi; /records/4/comparisons; /records/4/atom_correspondence | supports | Both complete saved molecular forms, all comparison flags and literal atom correspondence. All ten comparisons are true for this owner; full_graph_identity_established remains false. |
| bgc-2225-topology | /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json; /records/4/smiles/computed/atoms; /records/4/smiles/computed/bonds; /records/4/smiles/computed/rings; /records/4/smiles/computed/motifs; /records/4/smiles/computed/potential_stereo; /records/4/smiles/computed/stereo_counts; /records/4/inchi/computed/atoms; /records/4/inchi/computed/bonds; /records/4/inchi/computed/rings; /records/4/inchi/computed/motifs; /records/4/inchi/computed/potential_stereo; /records/4/inchi/computed/stereo_counts; /records/4/atom_correspondence; /records/4/declared_structure | supports | Complete indexed topology and stereochemistry in both saved forms. Structural motifs are bounded patterns, not natural-identity or experimental assignments. |
| bgc-2225-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-local-diagnostics-acceptance-001.json; /status; /chemistry_DATA; /chemistry_execution; /results; /unavailable | supports | ROOT acceptance of the original ordinary molecular diagnostic, with four globally unassigned warnings; scientific interpretation remains separately scoped. |
| bgc-2225-native-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-local-diagnostics-acceptance-001.json; /status; /native_ledger; /results; /unavailable | supports | ROOT acceptance of the five original local gates; full QC and OAK remain unavailable as separately recorded. |
| bgc-2225-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4/source_scope_inventory/joins/mibig_compounds | supports | Complete saved query frame with 1 positive row placements. Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against the exact pinned mibig_compounds table. No query replay or external lookup. |
| bgc-2225-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 1012 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":1012,"row_sha256":"5ab5076870ada22e7d83d501ce0aa06b89bee3d2533ff65095a38358fa8bb95d","row":{"mibig_accession":"BGC0000932","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"tropodithietic acid","compound_index":"1","smiles":"C1=CC(=O)C(=C2C(=C1)SS2)C(=O)O","standard_inchi":"InChI=1S/C8H4O3S2/c9-4-2-1-3-5-7(13-12-5)6(4)8(10)11/h1-3H,(H,10,11)","standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:44632924","taxon_id":"NCBITaxon:391619","taxon_label":"Phaeobacter inhibens DSM 17395","bgc_classes":"other","bgc_subclasses":"other","genome_accession":"CP002977.1","locus_from":"88772","locus_to":"108389","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:24723119","reference_basis":"ENTRY"}}] |
| bgc-2225-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4/source_scope_inventory/joins/chebi_structures | supports | Complete saved query frame with 1 positive row placements. Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against the exact pinned chebi_structures table. No query replay or external lookup. |
| bgc-2225-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Physical TSV lines 43119 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":43119,"row_sha256":"dc595c09d9a8eb1d798c392306397949401dab35733513abaea6d79ff0f6f779","row":{"chebi_id":"CHEBI:156455","name":"tropodithietic acid","definition":"A monocarboxylic acid that is 8,9-dithiabicyclo[5.2.0]nona-1,3,6-triene substituted by a carboxy group at position 2 and an oxo group at position 3. It is a broad spectrum antibiotic produced by the marine bacterium Phaeobacter inhibens that also acts as a signalling molecule at lower concentrations.","stars":"3","standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","smiles":"O=C(O)c1c(=O)cccc2ssc12"}}] |
| bgc-2225-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved query frame with 3 positive row placements. Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against the exact pinned lotus_occurrences table. No query replay or external lookup. |
| bgc-2225-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 544,545,546 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":544,"row_sha256":"59117a121a126ef6551aa11995af86a3fc85bcded6f35dcb00f360068c53c3d6","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","organism_name":"Phaeobacter inhibens","taxon_id":"NCBITaxon:221822","organism_wikidata":"http://www.wikidata.org/entity/Q26270932","reference_doi":"10.1039/C4CC01924E","structure_wikidata":"http://www.wikidata.org/entity/Q72515630"}},{"physical_line":545,"row_sha256":"73b7bf8e57d728e8dacd8ab8943ee5840f8ab2a4b3d54c9da2eb6c53944cfce5","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","organism_name":"Phaeobacter inhibens","taxon_id":"NCBITaxon:221822","organism_wikidata":"http://www.wikidata.org/entity/Q26270932","reference_doi":"10.1128/MBIO.02118-15","structure_wikidata":"http://www.wikidata.org/entity/Q72515630"}},{"physical_line":546,"row_sha256":"d40b10db33d89ba43d3e898f4e71a1ba8547d19453d187fc2185bbabf7bc201e","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","organism_name":"Roseobacter","taxon_id":"NCBITaxon:2433","organism_wikidata":"http://www.wikidata.org/entity/Q7368622","reference_doi":"10.1128/AEM.70.4.2560-2565.2003","structure_wikidata":"http://www.wikidata.org/entity/Q72515630"}}] |
| bgc-2225-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved query frame with 0 positive row placements. Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against the exact pinned cyanometdb_occurrences table. No query replay or external lookup. |
| bgc-2225-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4/source_scope_inventory/joins/npclassifier | supports | Complete saved query frame with 1 positive row placements. Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against the exact pinned npclassifier table. No query replay or external lookup. |
| bgc-2225-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 190 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":190,"row_sha256":"80a938e54c991cae99e9f38b70723e0a96eb1be27c2b46b83e099119a1899edf","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","smiles":"C1=CC(=O)C(=C2C(=C1)SS2)C(=O)O","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Tropolones","class_results":"Tropolones and derivatives (Shikimate)","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}] |
| bgc-2225-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved query frame with 41 positive row placements. Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against the exact pinned pubchem_bioassay table. No query replay or external lookup. |
| bgc-2225-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":676,"row_sha256":"e1dae56a5a50adc5bc6fe9adfe1d2bb7405350e9b8625d7c75f76f6ae74f72b1","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794731","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the NCI-H23 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":677,"row_sha256":"46cf33672a7c35640f2f07ae5c9e7f43be9025f7442a4861e3a7c70ff560252d","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794732","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the NCI-H226 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":678,"row_sha256":"21a14e4ba793aa582325b396c39ac3485d338cc83de70c7b6a698fc996f2bca3","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794735","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the HOP-62 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":679,"row_sha256":"40ee6304f7fb03808e35f140b67b2555dcf4dedb6fafa8f130cf26ef37c08c2d","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794736","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the NCI-H460 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":680,"row_sha256":"514276361c58e4a54ba1475e68a3b26829a086d097b69e0b45c871ad164363ac","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794738","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the HOP-92 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":681,"row_sha256":"187b6943792771042c71ece7d63ce9c6a92f44005e34bccdeff265a878110432","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794739","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the NCI-H522 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":682,"row_sha256":"cef5d2b1b8456818e81e1b5faa970ecc293ac2ce08bd9d1142af8896691d367a","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794740","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the A549/ATCC Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":683,"row_sha256":"b0e7cdea6c1850154701349f496107162443a44eac3ff569f23f9b64f474b3eb","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794742","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the COLO 205 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":684,"row_sha256":"9e5239d62f27ff0a5f705e8eb03656ab3d415f70656a2c79b357bbf2fda69fe2","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794745","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the M14 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":685,"row_sha256":"997dfff4dab983bdeaa8dde3e5f5363100b07ee71e459b413d9045eaef8e7c3c","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794746","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the HCT-15 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":686,"row_sha256":"320ca8ebb27d068a1d0c619569ae01a30617c70ae0b4527a26f9c69487a679ea","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794748","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the HT29 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":687,"row_sha256":"e219dac3216ca9c6c535dc09bdecff6f2de6642ab45285e5c4d15c85022164cb","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794751","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the SNB-19 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":688,"row_sha256":"e657018638b441e66c6996c13d61d40f3fd6f46aaf0f60fc503a191b802ab1a0","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794752","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the SF-539 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":689,"row_sha256":"c19758e6fe2d897e1377f0d521e641c3dfa31147c25fc250001ae2762be52413","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794753","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the U251 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":690,"row_sha256":"cd8ead4e5613a1a018570f945807e3836be441437e102530aed6e2ad8ce4d842","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794754","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the PC-3 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":691,"row_sha256":"d31e9b12c1430eb9fcf95196040989df167d5f51f5498b95fd41f132bad24d9d","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794757","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the LOX IMVI Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":692,"row_sha256":"890cdf90193c62c847ac8482949203fe713f76c861bbc0868b093a6c79a4f041","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794758","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the SF-295 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":693,"row_sha256":"670db287df6e3eb889534872ebc2e2db14252d504408d34f37ba911f3c95f7b9","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794759","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the SF-268 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":694,"row_sha256":"0ff81daa4564164b80f3555965f9521dc364418fd30d2ae1d2fdb367c0f88ee5","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794760","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the DU-145 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":695,"row_sha256":"415fa1e7c575a9dbf868cdb3a103b555e02c93b038956552a9de4d6489e3b107","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794766","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the MALME-3M Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":696,"row_sha256":"9389ccf5cbd5ac46042f0a2a75fc808b259c571724d42543e12e42eba6fd6255","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794769","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the TK-10 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":697,"row_sha256":"7bceaf8333a4658f22a09763f209a15819ee619eb1bd8afe634a2c01ef10e278","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794771","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the ACHN Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":698,"row_sha256":"b93ba9a03980e597ae89abe25174f16b2a35a14b14edaec8c31a271a2e860131","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794773","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the RXF 393 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":699,"row_sha256":"3f85d5bb5bf29d230501416850cce003e7039dcfbfde3a09d6d1d45274eda15e","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794774","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the A498 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":700,"row_sha256":"801b8490de9c6b8b7941bc133bf136ccf959a04abc18ee383e78dcd11b69e4d8","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794775","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the 786-0 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":701,"row_sha256":"1f40fe3cc0583bce76c1e9e918b9bee0d84344d9d3d7fd724ae7d7d353053acb","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794776","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the HL-60(TB) Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":702,"row_sha256":"be5300b7a6fd3ae2ffb0995d36208a8177492a3c55de3f73dc6fc22aaca9f3e7","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794777","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the K-562 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":703,"row_sha256":"caface4c9ee671dffcf47e7ca979c2fd2ba8de95714ab8c903ffa4c2a986de86","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794778","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the CCRF-CEM Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":704,"row_sha256":"2dc5157032cfee37b6e504925e2c9afb45742b5287d1f1f382b59699fcfca3a3","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794779","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the MOLT-4 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":705,"row_sha256":"1444b193795cb452687238d9dbe95e8a5bad31081cc00d279662d67b79be352b","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794780","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the SR Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":706,"row_sha256":"07b2be8057284541979e627f27c59754fef7c7b2e0d332c4111e75e02dba7493","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794781","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the RPMI-8226 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":707,"row_sha256":"daa7da65efb8ab34a44e2171ea9a29867b11c8df9ed65e466f8c9d8631551ea5","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794783","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the OVCAR-5 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":708,"row_sha256":"2115f604ad8c32272cb0e531176bd15fea85737c32d191a73c96ee9268d54eb0","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794784","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the OVCAR-4 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":709,"row_sha256":"43499c7e4f769762b547a963c8e333c1c1756686de89bf75403989e7c2db04b6","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794787","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the OVCAR-3 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":710,"row_sha256":"2fc868a43443eebd2eddc1f195ba526066636cd40fb772fd78790e250a2f1dbe","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794789","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the MDA-MB-231/ATCC Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":711,"row_sha256":"b4e5f068d26c4a97076d0851c71f3063b654189649268c32b603803cd4882670","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794792","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the T-47D Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":712,"row_sha256":"0efd4e572e805a5c187f3c21d0ce5df27e89b2144ffb1c5720e499f75e16a80e","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794795","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the SW-620 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":713,"row_sha256":"2bfad1bd3e19b4e5ede05c37682e8009656884f38912c281d80fce402b309047","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794796","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the MCF7 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":714,"row_sha256":"7327a9a4a5ecd15c7f865c59884cefdc2fea0f664c339e0847ef72529ae0e0b1","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794798","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the HCT-116 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":715,"row_sha256":"be7a6b27d33373f5cb6f91c043df7f34a478dbd10f2d7a6f6bed8927b1832daa","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794800","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the KM12 Non-Small Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":716,"row_sha256":"45b83f5f3e8c8f5ddf99db1766fefcdbe02d4e5f5aabb7d02787fc8b86e90073","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"2202374","assay_name":"NCI human tumor cell line growth inhibition assay. Data for the MDA-MB-468 Breast cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}}] |
| bgc-2225-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved query frame with 0 positive row placements. Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against the exact pinned bindingdb_targets table. No query replay or external lookup. |
| bgc-2225-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved query frame with 1 positive row placements. Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against the exact pinned antibioticmech_inchikeys table. No query replay or external lookup. |
| bgc-2225-source-antibioticmech_inchikeys | /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv; Physical TSV lines 159 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":159,"row_sha256":"ad1e809204e8d8bbef7c5471142b384accf2d94e4e7a7457e999c00c602a9dd6","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","identifier":"CHEBI:156455","label":"tropodithietic acid","antimicrobial_class":"ANTIBACTERIAL","slug":"tropodithietic-acid","corpus_commit":"74f6cc8362498900f2fe2c13d0b6fdb66dd30976"}}] |
| bgc-2225-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4/source_scope_inventory/joins/chebi_origins | supports | Complete saved query frame with 3 positive row placements. Saved exact chebi_id from exact full-key structure rows, query ["CHEBI:156455"], against the exact pinned chebi_origins table. No query replay or external lookup. |
| bgc-2225-source-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Physical TSV lines 17059,17060,17061 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":17059,"row_sha256":"2ddf0dcd68c103c9b9d48c2627e5dd978217943d53e670dcab34cea4cea138f8","row":{"chebi_id":"CHEBI:156455","species_text":"Phaeobacter gallaeciensis","species_accession":"60890","component_text":"","strain_text":"","source_accession":"21430694","comments":""}},{"physical_line":17060,"row_sha256":"412e49e733d88fa9690ef643b6f2393e788fd6f01703e2db9d88e3232ce90b7c","row":{"chebi_id":"CHEBI:156455","species_text":"Phaeobacter inhibens","species_accession":"221822","component_text":"","strain_text":"","source_accession":"28389641","comments":""}},{"physical_line":17061,"row_sha256":"e502162c0d93818ef761b9fac6b76079808e0ec9c948ee565bb2803f0f8c0fd5","row":{"chebi_id":"CHEBI:156455","species_text":"Phaeobacter inhibens DSM 17395","species_accession":"391619","component_text":"","strain_text":"","source_accession":"25161739","comments":""}}] |
| bgc-2225-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/4; /cached_taxonomy/whole_stanzas/11; /cached_taxonomy/whole_stanzas/13; /cached_taxonomy/whole_stanzas/15 | supports | Complete personally read retained name/synonym stanzas: [{"id":"NCBITaxon:2433","physical_line":3598,"complete_stanza":"[Term]\nid: NCBITaxon:2433\nname: Roseobacter\n\n"},{"id":"NCBITaxon:60890","physical_line":27799,"complete_stanza":"[Term]\nid: NCBITaxon:60890\nname: Phaeobacter gallaeciensis\nsynonym: \"Roseobacter gallaeciensis\" EXACT []\n\n"},{"id":"NCBITaxon:221822","physical_line":68093,"complete_stanza":"[Term]\nid: NCBITaxon:221822\nname: Phaeobacter inhibens\n\n"},{"id":"NCBITaxon:391619","physical_line":90073,"complete_stanza":"[Term]\nid: NCBITaxon:391619\nname: Phaeobacter inhibens DSM 17395\nsynonym: \"Phaeobacter gallaeciensis DSM 17395\" EXACT []\n\n"}]. No current external taxonomy or ancestry is inferred. |
| bgc-2225-source-routes | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/4/source_scope_inventory/source_taxa; /records/4/source_scope_inventory/forward_taxon_merge_matches; /records/4/source_scope_inventory/nonorganism_matches | supports | Exact selected source taxa and forward/nonorganism route sets; both match lists are empty in this saved scope. |
| bgc-2225-direct-owner-0 | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-inventory-DATA-001.json; /contexts/8/complete_raw_text; /contexts/8/complete_raw_history; /contexts/8/source_scope_inventory | supports | Complete directly admitted companion hydroxytropodithietic acid, full key BCXSWKYTDHBUIH-UHFFFAOYSA-N, and its own source/history context. Whole-reading attribution is explicit in source notes; no recursive or identity/activity/mechanism transfer. |
| bgc-2225-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Workflow; Output | supports | Claim-level review, immutable records and honest partial completion under actual evidence-access limits. |
| bgc-2225-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Complete maintained review profile | supports | Producer/occurrence distinctions, evidence grades, source ownership and qualified computed classifications. |
| bgc-2225-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 376–432 | supports | Identifier/stereo limitations and the explicit computed-not-source status of NPClassifier fields. |
| bgc-2225-activity-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 632–665; lines 920–947 | supports | Optional observation activity class and coarse backed activity buckets; no dedicated cell-killing definition is supplied. |
| bgc-2225-activity-classifier | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 127–179; lines 1310–1382 | supports | Maintained title classifier, ACTIVE-only class assignment, 25-observation cap and summary derivation from written observations. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-223/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-223/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-223/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-223/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-223/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External identifiers, taxonomy, accessions and primary publications were not refreshed under the absolute no-request instruction; historical and database assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and parsing establish their declared mechanical scope only.
- Negative source joins apply only to the exact retained predicates and source snapshots. Shared loci, citations and companion records do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source records, raw snapshots, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete selected source payloads and explicit direct-context reading attribution are preserved in the pinned source notes. All five owner histories, actual intakes and ten paired molecular tables were personally read.
- Four original diagnostic warnings remain global and unassigned; no warning is attributed to an individual owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T133012Z-tropodithietic-acid
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: tropodithietic acid'
started_at: '2026-11-03T13:02:50.368088Z'
finished_at: '2026-11-03T13:30:12.795292Z'
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
summary: Tropodithietic acid has coherent retained ChEBI/MIBiG structure and bounded
  source provenance. Its 25 written cell-growth observations, 16 omitted retained
  results and exact sibling ANTIBACTERIAL assertion remain distinct. No supported
  local curation defect is established within the saved evidence; the review is partial.
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/hydroxytropodithietic-acid.yaml
    sha256: 25be23ff65846f4b97b04e321a6a289d9b4a16663fbec55527280c77492cd3f5
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/tropodithietic-acid.yaml
    sha256: caa7269f6191218c02cf6e334c6f97684fe4c09655cc92ba37a3353a8a80a1f6
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2225; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156455
targets:
- target_id: CHEBI:156455
  path: data/natural_products/shikimates_and_phenylpropanoids/tropodithietic-acid.yaml
  label: tropodithietic acid
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
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned full-key AntibioticMech structure links and coarse activity summaries;
      no transfer of mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Exact assay identity exclusion decisions for selected/direct source context.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Maintained source-row identity/digest guard; text-only dependency.
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
  - CHEBI:156455
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/s2507.yaml
    data/natural_products/shikimates_and_phenylpropanoids/semivioxanthin.yaml data/natural_products/shikimates_and_phenylpropanoids/stipitatic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/sungeidine-d.yaml data/natural_products/shikimates_and_phenylpropanoids/tropodithietic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/venemycin.yaml data/natural_products/shikimates_and_phenylpropanoids/xenocoumacin-1.yaml
    data/natural_products/shikimates_and_phenylpropanoids/xenocoumacin-ii.yaml data/natural_products/shikimates_and_phenylpropanoids/z-6-undecenyltyrazolone.yaml
    data/natural_products/terpenoids/1-epibotrydial.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-223/validate-strict-selected10-001.tsv
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
  - CHEBI:156455
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-223/validate-all-001.tsv
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
  - CHEBI:156455
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
  - CHEBI:156455
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
  - CHEBI:156455
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-223/review-queue-001.tsv
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
  - CHEBI:156455
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:156455
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:156455
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2225-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/tropodithietic-acid.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete owner and append-only history, personally read as exact saved
    plaintext and rejoined to this current raw pin.
  snapshot_sha256: caa7269f6191218c02cf6e334c6f97684fe4c09655cc92ba37a3353a8a80a1f6
- evidence_id: bgc-2225-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/4/owner_pin; /records/4/owner_document
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete captured owner and its exact source pin; no source fields or native
    history were edited.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2225-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/intakes/2225-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Actual canonical intake source, complete input map and target/maintained-owner
    scope.
  snapshot_sha256: 74c3df9ff2420a848e33dd41694ed5f5e2d6694560b0f7c7bd580e9f909670bf
- evidence_id: bgc-2225-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-intake-ready-001.json
  locator: /status; /intake_summary
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: ROOT acceptance of the original ten canonical intakes, with no replay.
  snapshot_sha256: f4a1f4b715e664d404565e45fe7359127911e5c1349b6e9f0df7c7ce4a4519a7
- evidence_id: bgc-2225-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/4/owner_document/chemical_structure; /records/4/owner_document/source_concepts;
    /records/4/owner_document/grounding_status
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Written structure, source concepts and grounding decision, without fresh
    external resolution.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2225-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete written producer and locus assertions, including evidence grades,
    source versions, methods and references.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2225-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/4/owner_document/occurrences
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete written occurrences and their cited scope.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2225-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete captured owner supports the written assay, summary, target and
    mechanism fields or their absence; source-query-only facts belong to separate
    evidence.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2225-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/4/owner_document/np_classification; /records/4/owner_document/bgc_class
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Named-model prediction and source BGC class are preserved as separate assertions.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2225-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete admitted selected context, direct companions, raw/history and
    exact input map.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: bgc-2225-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-scope-notes-001.json
  locator: /reading; /curation; /cautions
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete reading attribution and bounded curation scope: 135 literal tokens
    across eight explicit files, with five out-of-scope shared-taxon hits rather than
    zero textual matches.'
  snapshot_sha256: 589a3b0bfdd9afec556e285580c4102a2e3fa8d9735e3364d7ea42d9827eee41
- evidence_id: bgc-2225-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-input-plan-acceptance-001.json
  locator: /status; /plan; /notes; /inventory; /per_order_counts
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: ROOT acceptance of this original saved source plan, notes and exact per-order
    input counts.
  snapshot_sha256: 4428e2ef161f4bb098750e9bbcdd4dd8841c2332e7bc64b01c75f1cc8aacdaf0
- evidence_id: bgc-2225-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/declared_structure; /records/4/smiles; /records/4/inchi; /records/4/comparisons;
    /records/4/atom_correspondence
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Both complete saved molecular forms, all comparison flags and literal atom
    correspondence. All ten comparisons are true for this owner; full_graph_identity_established
    remains false.
  snapshot_sha256: 1723f79377c00369ddbb345f4b472f98b3ef855db093e27f59998345d4779937
- evidence_id: bgc-2225-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/smiles/computed/atoms; /records/4/smiles/computed/bonds; /records/4/smiles/computed/rings;
    /records/4/smiles/computed/motifs; /records/4/smiles/computed/potential_stereo;
    /records/4/smiles/computed/stereo_counts; /records/4/inchi/computed/atoms; /records/4/inchi/computed/bonds;
    /records/4/inchi/computed/rings; /records/4/inchi/computed/motifs; /records/4/inchi/computed/potential_stereo;
    /records/4/inchi/computed/stereo_counts; /records/4/atom_correspondence; /records/4/declared_structure
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete indexed topology and stereochemistry in both saved forms. Structural
    motifs are bounded patterns, not natural-identity or experimental assignments.
  snapshot_sha256: 1723f79377c00369ddbb345f4b472f98b3ef855db093e27f59998345d4779937
- evidence_id: bgc-2225-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-local-diagnostics-acceptance-001.json
  locator: /status; /chemistry_DATA; /chemistry_execution; /results; /unavailable
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: ROOT acceptance of the original ordinary molecular diagnostic, with four
    globally unassigned warnings; scientific interpretation remains separately scoped.
  snapshot_sha256: 05cfab1ce4207e65f6e1a2f6f010bb822ee4db74b3c8277597c5b7707e04fb7a
- evidence_id: bgc-2225-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-local-diagnostics-acceptance-001.json
  locator: /status; /native_ledger; /results; /unavailable
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: ROOT acceptance of the five original local gates; full QC and OAK remain
    unavailable as separately recorded.
  snapshot_sha256: 05cfab1ce4207e65f6e1a2f6f010bb822ee4db74b3c8277597c5b7707e04fb7a
- evidence_id: bgc-2225-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 1 positive row placements. Saved exact
    complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against
    the exact pinned mibig_compounds table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N",
    against the exact pinned mibig_compounds table. No query replay or external lookup.
- evidence_id: bgc-2225-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 1012
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":1012,"row_sha256":"5ab5076870ada22e7d83d501ce0aa06b89bee3d2533ff65095a38358fa8bb95d","row":{"mibig_accession":"BGC0000932","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"tropodithietic
    acid","compound_index":"1","smiles":"C1=CC(=O)C(=C2C(=C1)SS2)C(=O)O","standard_inchi":"InChI=1S/C8H4O3S2/c9-4-2-1-3-5-7(13-12-5)6(4)8(10)11/h1-3H,(H,10,11)","standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:44632924","taxon_id":"NCBITaxon:391619","taxon_label":"Phaeobacter
    inhibens DSM 17395","bgc_classes":"other","bgc_subclasses":"other","genome_accession":"CP002977.1","locus_from":"88772","locus_to":"108389","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:24723119","reference_basis":"ENTRY"}}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2225-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 1 positive row placements. Saved exact
    complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against
    the exact pinned chebi_structures table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N",
    against the exact pinned chebi_structures table. No query replay or external lookup.
- evidence_id: bgc-2225-source-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Physical TSV lines 43119
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":43119,"row_sha256":"dc595c09d9a8eb1d798c392306397949401dab35733513abaea6d79ff0f6f779","row":{"chebi_id":"CHEBI:156455","name":"tropodithietic
    acid","definition":"A monocarboxylic acid that is 8,9-dithiabicyclo[5.2.0]nona-1,3,6-triene
    substituted by a carboxy group at position 2 and an oxo group at position 3. It
    is a broad spectrum antibiotic produced by the marine bacterium Phaeobacter inhibens
    that also acts as a signalling molecule at lower concentrations.","stars":"3","standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","smiles":"O=C(O)c1c(=O)cccc2ssc12"}}]'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2225-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 3 positive row placements. Saved exact
    complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against
    the exact pinned lotus_occurrences table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N",
    against the exact pinned lotus_occurrences table. No query replay or external
    lookup.
- evidence_id: bgc-2225-source-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 544,545,546
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":544,"row_sha256":"59117a121a126ef6551aa11995af86a3fc85bcded6f35dcb00f360068c53c3d6","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","organism_name":"Phaeobacter
    inhibens","taxon_id":"NCBITaxon:221822","organism_wikidata":"http://www.wikidata.org/entity/Q26270932","reference_doi":"10.1039/C4CC01924E","structure_wikidata":"http://www.wikidata.org/entity/Q72515630"}},{"physical_line":545,"row_sha256":"73b7bf8e57d728e8dacd8ab8943ee5840f8ab2a4b3d54c9da2eb6c53944cfce5","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","organism_name":"Phaeobacter
    inhibens","taxon_id":"NCBITaxon:221822","organism_wikidata":"http://www.wikidata.org/entity/Q26270932","reference_doi":"10.1128/MBIO.02118-15","structure_wikidata":"http://www.wikidata.org/entity/Q72515630"}},{"physical_line":546,"row_sha256":"d40b10db33d89ba43d3e898f4e71a1ba8547d19453d187fc2185bbabf7bc201e","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","organism_name":"Roseobacter","taxon_id":"NCBITaxon:2433","organism_wikidata":"http://www.wikidata.org/entity/Q7368622","reference_doi":"10.1128/AEM.70.4.2560-2565.2003","structure_wikidata":"http://www.wikidata.org/entity/Q72515630"}}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2225-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 0 positive row placements. Saved exact
    complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against
    the exact pinned cyanometdb_occurrences table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N",
    against the exact pinned cyanometdb_occurrences table. No query replay or external
    lookup.
- evidence_id: bgc-2225-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 1 positive row placements. Saved exact
    complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against
    the exact pinned npclassifier table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N",
    against the exact pinned npclassifier table. No query replay or external lookup.
- evidence_id: bgc-2225-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 190
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":190,"row_sha256":"80a938e54c991cae99e9f38b70723e0a96eb1be27c2b46b83e099119a1899edf","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","smiles":"C1=CC(=O)C(=C2C(=C1)SS2)C(=O)O","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Tropolones","class_results":"Tropolones
    and derivatives (Shikimate)","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2225-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 41 positive row placements. Saved exact
    complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against
    the exact pinned pubchem_bioassay table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N",
    against the exact pinned pubchem_bioassay table. No query replay or external lookup.
- evidence_id: bgc-2225-source-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":676,"row_sha256":"e1dae56a5a50adc5bc6fe9adfe1d2bb7405350e9b8625d7c75f76f6ae74f72b1","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794731","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the NCI-H23 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":677,"row_sha256":"46cf33672a7c35640f2f07ae5c9e7f43be9025f7442a4861e3a7c70ff560252d","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794732","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the NCI-H226 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":678,"row_sha256":"21a14e4ba793aa582325b396c39ac3485d338cc83de70c7b6a698fc996f2bca3","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794735","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the HOP-62 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":679,"row_sha256":"40ee6304f7fb03808e35f140b67b2555dcf4dedb6fafa8f130cf26ef37c08c2d","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794736","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the NCI-H460 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":680,"row_sha256":"514276361c58e4a54ba1475e68a3b26829a086d097b69e0b45c871ad164363ac","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794738","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the HOP-92 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":681,"row_sha256":"187b6943792771042c71ece7d63ce9c6a92f44005e34bccdeff265a878110432","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794739","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the NCI-H522 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":682,"row_sha256":"cef5d2b1b8456818e81e1b5faa970ecc293ac2ce08bd9d1142af8896691d367a","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794740","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the A549/ATCC Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":683,"row_sha256":"b0e7cdea6c1850154701349f496107162443a44eac3ff569f23f9b64f474b3eb","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794742","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the COLO 205 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":684,"row_sha256":"9e5239d62f27ff0a5f705e8eb03656ab3d415f70656a2c79b357bbf2fda69fe2","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794745","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the M14 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":685,"row_sha256":"997dfff4dab983bdeaa8dde3e5f5363100b07ee71e459b413d9045eaef8e7c3c","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794746","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the HCT-15 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":686,"row_sha256":"320ca8ebb27d068a1d0c619569ae01a30617c70ae0b4527a26f9c69487a679ea","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794748","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the HT29 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":687,"row_sha256":"e219dac3216ca9c6c535dc09bdecff6f2de6642ab45285e5c4d15c85022164cb","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794751","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the SNB-19 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":688,"row_sha256":"e657018638b441e66c6996c13d61d40f3fd6f46aaf0f60fc503a191b802ab1a0","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794752","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the SF-539 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":689,"row_sha256":"c19758e6fe2d897e1377f0d521e641c3dfa31147c25fc250001ae2762be52413","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794753","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the U251 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":690,"row_sha256":"cd8ead4e5613a1a018570f945807e3836be441437e102530aed6e2ad8ce4d842","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794754","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the PC-3 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":691,"row_sha256":"d31e9b12c1430eb9fcf95196040989df167d5f51f5498b95fd41f132bad24d9d","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794757","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the LOX IMVI Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":692,"row_sha256":"890cdf90193c62c847ac8482949203fe713f76c861bbc0868b093a6c79a4f041","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794758","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the SF-295 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":693,"row_sha256":"670db287df6e3eb889534872ebc2e2db14252d504408d34f37ba911f3c95f7b9","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794759","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the SF-268 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":694,"row_sha256":"0ff81daa4564164b80f3555965f9521dc364418fd30d2ae1d2fdb367c0f88ee5","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794760","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the DU-145 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":695,"row_sha256":"415fa1e7c575a9dbf868cdb3a103b555e02c93b038956552a9de4d6489e3b107","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794766","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the MALME-3M Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":696,"row_sha256":"9389ccf5cbd5ac46042f0a2a75fc808b259c571724d42543e12e42eba6fd6255","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794769","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the TK-10 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":697,"row_sha256":"7bceaf8333a4658f22a09763f209a15819ee619eb1bd8afe634a2c01ef10e278","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794771","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the ACHN Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":698,"row_sha256":"b93ba9a03980e597ae89abe25174f16b2a35a14b14edaec8c31a271a2e860131","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794773","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the RXF 393 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":699,"row_sha256":"3f85d5bb5bf29d230501416850cce003e7039dcfbfde3a09d6d1d45274eda15e","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794774","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the A498 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":700,"row_sha256":"801b8490de9c6b8b7941bc133bf136ccf959a04abc18ee383e78dcd11b69e4d8","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794775","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the 786-0 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":701,"row_sha256":"1f40fe3cc0583bce76c1e9e918b9bee0d84344d9d3d7fd724ae7d7d353053acb","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794776","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the HL-60(TB) Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":702,"row_sha256":"be5300b7a6fd3ae2ffb0995d36208a8177492a3c55de3f73dc6fc22aaca9f3e7","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794777","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the K-562 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":703,"row_sha256":"caface4c9ee671dffcf47e7ca979c2fd2ba8de95714ab8c903ffa4c2a986de86","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794778","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the CCRF-CEM Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":704,"row_sha256":"2dc5157032cfee37b6e504925e2c9afb45742b5287d1f1f382b59699fcfca3a3","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794779","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the MOLT-4 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":705,"row_sha256":"1444b193795cb452687238d9dbe95e8a5bad31081cc00d279662d67b79be352b","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794780","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the SR Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":706,"row_sha256":"07b2be8057284541979e627f27c59754fef7c7b2e0d332c4111e75e02dba7493","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794781","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the RPMI-8226 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":707,"row_sha256":"daa7da65efb8ab34a44e2171ea9a29867b11c8df9ed65e466f8c9d8631551ea5","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794783","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the OVCAR-5 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":708,"row_sha256":"2115f604ad8c32272cb0e531176bd15fea85737c32d191a73c96ee9268d54eb0","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794784","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the OVCAR-4 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":709,"row_sha256":"43499c7e4f769762b547a963c8e333c1c1756686de89bf75403989e7c2db04b6","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794787","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the OVCAR-3 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":710,"row_sha256":"2fc868a43443eebd2eddc1f195ba526066636cd40fb772fd78790e250a2f1dbe","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794789","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the MDA-MB-231/ATCC Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":711,"row_sha256":"b4e5f068d26c4a97076d0851c71f3063b654189649268c32b603803cd4882670","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794792","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the T-47D Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":712,"row_sha256":"0efd4e572e805a5c187f3c21d0ce5df27e89b2144ffb1c5720e499f75e16a80e","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794795","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the SW-620 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":713,"row_sha256":"2bfad1bd3e19b4e5ede05c37682e8009656884f38912c281d80fce402b309047","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794796","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the MCF7 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":714,"row_sha256":"7327a9a4a5ecd15c7f865c59884cefdc2fea0f664c339e0847ef72529ae0e0b1","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794798","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the HCT-116 Non-Small
    Cell Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":715,"row_sha256":"be7a6b27d33373f5cb6f91c043df7f34a478dbd10f2d7a6f6bed8927b1832daa","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"1794800","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the KM12 Non-Small Cell
    Lung cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}},{"physical_line":716,"row_sha256":"45b83f5f3e8c8f5ddf99db1766fefcdbe02d4e5f5aabb7d02787fc8b86e90073","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","cid":"44632924","aid":"2202374","assay_name":"NCI
    human tumor cell line growth inhibition assay. Data for the MDA-MB-468 Breast
    cell line, single concentration","assay_type":"Screening","depositor":"DTP/NCI","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"","reference":""}}]'
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2225-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 0 positive row placements. Saved exact
    complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against
    the exact pinned bindingdb_targets table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N",
    against the exact pinned bindingdb_targets table. No query replay or external
    lookup.
- evidence_id: bgc-2225-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 1 positive row placements. Saved exact
    complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N", against
    the exact pinned antibioticmech_inchikeys table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "BLFCMITWMARUSM-UHFFFAOYSA-N",
    against the exact pinned antibioticmech_inchikeys table. No query replay or external
    lookup.
- evidence_id: bgc-2225-source-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv
  locator: Physical TSV lines 159
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":159,"row_sha256":"ad1e809204e8d8bbef7c5471142b384accf2d94e4e7a7457e999c00c602a9dd6","row":{"standard_inchi_key":"BLFCMITWMARUSM-UHFFFAOYSA-N","identifier":"CHEBI:156455","label":"tropodithietic
    acid","antimicrobial_class":"ANTIBACTERIAL","slug":"tropodithietic-acid","corpus_commit":"74f6cc8362498900f2fe2c13d0b6fdb66dd30976"}}]'
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
- evidence_id: bgc-2225-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 3 positive row placements. Saved exact
    chebi_id from exact full-key structure rows, query ["CHEBI:156455"], against the
    exact pinned chebi_origins table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact chebi_id from exact full-key structure rows, query ["CHEBI:156455"],
    against the exact pinned chebi_origins table. No query replay or external lookup.
- evidence_id: bgc-2225-source-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Physical TSV lines 17059,17060,17061
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":17059,"row_sha256":"2ddf0dcd68c103c9b9d48c2627e5dd978217943d53e670dcab34cea4cea138f8","row":{"chebi_id":"CHEBI:156455","species_text":"Phaeobacter
    gallaeciensis","species_accession":"60890","component_text":"","strain_text":"","source_accession":"21430694","comments":""}},{"physical_line":17060,"row_sha256":"412e49e733d88fa9690ef643b6f2393e788fd6f01703e2db9d88e3232ce90b7c","row":{"chebi_id":"CHEBI:156455","species_text":"Phaeobacter
    inhibens","species_accession":"221822","component_text":"","strain_text":"","source_accession":"28389641","comments":""}},{"physical_line":17061,"row_sha256":"e502162c0d93818ef761b9fac6b76079808e0ec9c948ee565bb2803f0f8c0fd5","row":{"chebi_id":"CHEBI:156455","species_text":"Phaeobacter
    inhibens DSM 17395","species_accession":"391619","component_text":"","strain_text":"","source_accession":"25161739","comments":""}}]'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: bgc-2225-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/4; /cached_taxonomy/whole_stanzas/11; /cached_taxonomy/whole_stanzas/13;
    /cached_taxonomy/whole_stanzas/15
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete personally read retained name/synonym stanzas: [{"id":"NCBITaxon:2433","physical_line":3598,"complete_stanza":"[Term]\nid:
    NCBITaxon:2433\nname: Roseobacter\n\n"},{"id":"NCBITaxon:60890","physical_line":27799,"complete_stanza":"[Term]\nid:
    NCBITaxon:60890\nname: Phaeobacter gallaeciensis\nsynonym: \"Roseobacter gallaeciensis\"
    EXACT []\n\n"},{"id":"NCBITaxon:221822","physical_line":68093,"complete_stanza":"[Term]\nid:
    NCBITaxon:221822\nname: Phaeobacter inhibens\n\n"},{"id":"NCBITaxon:391619","physical_line":90073,"complete_stanza":"[Term]\nid:
    NCBITaxon:391619\nname: Phaeobacter inhibens DSM 17395\nsynonym: \"Phaeobacter
    gallaeciensis DSM 17395\" EXACT []\n\n"}]. No current external taxonomy or ancestry
    is inferred.'
  snapshot_sha256: 2908ca392787234d35ba65232b790613208e64ba9ee046c5977f3083ca6d2184
- evidence_id: bgc-2225-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/source_taxa; /records/4/source_scope_inventory/forward_taxon_merge_matches;
    /records/4/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Exact selected source taxa and forward/nonorganism route sets; both match
    lists are empty in this saved scope.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: bgc-2225-direct-owner-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-inventory-DATA-001.json
  locator: /contexts/8/complete_raw_text; /contexts/8/complete_raw_history; /contexts/8/source_scope_inventory
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete directly admitted companion hydroxytropodithietic acid, full key
    BCXSWKYTDHBUIH-UHFFFAOYSA-N, and its own source/history context. Whole-reading
    attribution is explicit in source notes; no recursive or identity/activity/mechanism
    transfer.
  snapshot_sha256: 2908ca392787234d35ba65232b790613208e64ba9ee046c5977f3083ca6d2184
- evidence_id: bgc-2225-review-skill
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Workflow; Output
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Claim-level review, immutable records and honest partial completion under
    actual evidence-access limits.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2225-review-profile
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Complete maintained review profile
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Producer/occurrence distinctions, evidence grades, source ownership and
    qualified computed classifications.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2225-structure-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 376–432
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Identifier/stereo limitations and the explicit computed-not-source status
    of NPClassifier fields.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2225-activity-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 632–665; lines 920–947
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Optional observation activity class and coarse backed activity buckets;
    no dedicated cell-killing definition is supplied.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2225-activity-classifier
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 127–179; lines 1310–1382
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Maintained title classifier, ACTIVE-only class assignment, 25-observation
    cap and summary derivation from written observations.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:04:37.883893Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 66324cb2f94b0ce47e3f280f083307555671c644c60bd8f537eca77bd779fb7e
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:05:07.558356Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 57dad69fca1e4915ddaa2cfc5cf058591111722e4e624616dadf9a79e2ddb244
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:05:29.643887Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:06:05.240084Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:06:18.573110Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: cfbaccb0dbd803cbeac03b9148b9355a7e6393913f208ea1a9c6d5c53927cf9b
assessments:
- assessment_id: bgc-2225-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: CHEBI:156455, its three-star retained structure row and the MIBiG BGC0000932
    v5 compound match BLFCMITWMARUSM-UHFFFAOYSA-N and both saved forms. The bicyclic
    sulfur-containing carboxylic-acid part of the ChEBI definition agrees with the
    observed topology. Its broad-spectrum antibiotic, producer and low-concentration
    signalling wording remains an attributed database definition, not fresh functional
    verification. The hydroxylated same-locus companion has a different full key and
    is not substituted for this owner.
  target_ids:
  - CHEBI:156455
  evidence_ids:
  - bgc-2225-grounding-owner
  - bgc-2225-source-plan
  - bgc-2225-plan-acceptance
  - bgc-2225-query-chebi_structures
  - bgc-2225-source-chebi_structures
  - bgc-2225-source-mibig_compounds
  - bgc-2225-chemistry
  - bgc-2225-direct-owner-0
  dimensions:
  - name: standard_inchi_key
    value: Full key BLFCMITWMARUSM-UHFFFAOYSA-N and retained CHEBI:156455 structure.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2225-grounding-owner
    - bgc-2225-source-plan
    - bgc-2225-plan-acceptance
    - bgc-2225-query-chebi_structures
    - bgc-2225-source-chebi_structures
    - bgc-2225-source-mibig_compounds
    - bgc-2225-chemistry
    - bgc-2225-direct-owner-0
  - name: grounding_scope
    value: EXACT is locally coherent; functional ChEBI definition wording remains
      attributed and unverified.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2225-grounding-owner
    - bgc-2225-source-plan
    - bgc-2225-plan-acceptance
    - bgc-2225-query-chebi_structures
    - bgc-2225-source-chebi_structures
    - bgc-2225-source-mibig_compounds
    - bgc-2225-chemistry
    - bgc-2225-direct-owner-0
- assessment_id: bgc-2225-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both forms give neutral C8H4O3S2, 13 atoms and 14 bonds, with no potential
    stereo element reported. All ten comparisons are true and the saved atom correspondence
    is complete. The seven-carbon ring and fused four-membered C2S2 ring, including
    the S–S bond, are preserved; carboxylic acid and ring carbonyl are explicit. Aromatic
    normalization and identifier agreement do not establish a solution-state tautomer,
    redox mechanism or natural sample identity.
  target_ids:
  - CHEBI:156455
  evidence_ids:
  - bgc-2225-chemistry
  - bgc-2225-topology
  - bgc-2225-diagnostic-acceptance
  - bgc-2225-structure-schema
  dimensions:
  - name: stereochemistry_scope
    value: No potential stereo element in the saved neutral representation.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2225-chemistry
    - bgc-2225-topology
    - bgc-2225-diagnostic-acceptance
    - bgc-2225-structure-schema
  - name: representation_correspondence
    value: Ten true comparisons and complete match; no solution-state, redox or natural-identity
      proof.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2225-chemistry
    - bgc-2225-topology
    - bgc-2225-diagnostic-acceptance
    - bgc-2225-structure-schema
- assessment_id: bgc-2225-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: MIBiG BGC0000932 v5 attributes Phaeobacter inhibens DSM17395 (391619) at
    SOURCE_ASSERTION grade and its CP002977.1 locus at CLUSTER_UNSTATED; the entry
    is active/questionable with unknown completeness. The six written occurrences
    comprise three LOTUS and three ChEBI-origin assertions across species221822, species60890,
    strain391619 and genus2433. The producer/occurrence overlap is explicitly qualified
    for publication independence. Cached strain391619 has the historical P. gallaeciensis
    DSM17395 synonym; it does not merge species60890 with P. inhibens or collapse
    strain and genus scopes.
  target_ids:
  - CHEBI:156455
  evidence_ids:
  - bgc-2225-origin-owner
  - bgc-2225-occurrence-owner
  - bgc-2225-source-mibig_compounds
  - bgc-2225-source-lotus_occurrences
  - bgc-2225-source-chebi_origins
  - bgc-2225-cached-taxonomy
  - bgc-2225-source-routes
  - bgc-2225-review-profile
  - bgc-2225-direct-owner-0
  dimensions:
  - name: taxon_scope
    value: Strain391619, species221822/60890 and genus2433 remain distinct; cached
      synonym is bounded.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2225-origin-owner
    - bgc-2225-occurrence-owner
    - bgc-2225-source-mibig_compounds
    - bgc-2225-source-lotus_occurrences
    - bgc-2225-source-chebi_origins
    - bgc-2225-cached-taxonomy
    - bgc-2225-source-routes
    - bgc-2225-review-profile
    - bgc-2225-direct-owner-0
  - name: producer_evidence
    value: SOURCE_ASSERTION for the retained strain producer claim.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2225-origin-owner
    - bgc-2225-occurrence-owner
    - bgc-2225-source-mibig_compounds
    - bgc-2225-source-lotus_occurrences
    - bgc-2225-source-chebi_origins
    - bgc-2225-cached-taxonomy
    - bgc-2225-source-routes
    - bgc-2225-review-profile
    - bgc-2225-direct-owner-0
  - name: locus_evidence
    value: BGC0000932 v5 CLUSTER_UNSTATED; active/questionable/unknown entry scope
      retained.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2225-origin-owner
    - bgc-2225-occurrence-owner
    - bgc-2225-source-mibig_compounds
    - bgc-2225-source-lotus_occurrences
    - bgc-2225-source-chebi_origins
    - bgc-2225-cached-taxonomy
    - bgc-2225-source-routes
    - bgc-2225-review-profile
    - bgc-2225-direct-owner-0
- assessment_id: bgc-2225-citations
  area: evidence
  topic: Citations
  outcome: unknown
  summary: PMID:24723119 is the MIBiG entry citation. LOTUS retains DOI:10.1039/C4CC01924E,
    DOI:10.1128/MBIO.02118-15 and DOI:10.1128/AEM.70.4.2560-2565.2003; ChEBI origins
    retain PMIDs21430694,28389641 and25161739. These assertion roles and possible
    overlap are preserved without counting independent papers. PubChem rows cite their
    AIDs because the retained reference field is blank. The exact AntibioticMech full-key
    row is a separate coarse activity assertion, not a primary assay or target mechanism.
  target_ids:
  - CHEBI:156455
  evidence_ids:
  - bgc-2225-origin-owner
  - bgc-2225-occurrence-owner
  - bgc-2225-assay-owner
  - bgc-2225-source-mibig_compounds
  - bgc-2225-source-lotus_occurrences
  - bgc-2225-source-chebi_origins
  - bgc-2225-source-pubchem_bioassay
  - bgc-2225-source-antibioticmech_inchikeys
  - bgc-2225-source-notes
  - bgc-2225-direct-owner-0
  dimensions:
  - name: citation_scope
    value: Entry, occurrence, AID and sibling references have distinct roles and unverified
      independence.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2225-origin-owner
    - bgc-2225-occurrence-owner
    - bgc-2225-assay-owner
    - bgc-2225-source-mibig_compounds
    - bgc-2225-source-lotus_occurrences
    - bgc-2225-source-chebi_origins
    - bgc-2225-source-pubchem_bioassay
    - bgc-2225-source-antibioticmech_inchikeys
    - bgc-2225-source-notes
    - bgc-2225-direct-owner-0
- assessment_id: bgc-2225-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: 'All 41 retained PubChem rows are Active single-concentration NCI human-tumor
    cell-growth screens. The owner writes 25 ACTIVE/CYTOTOXIC observations and explicitly
    notes 16 omitted results. The retained endpoint, value, target accession and reference
    fields are blank: no IC50, dose response, molecular target or cell-killing mechanism
    can be inferred. The coarse CYTOTOXIC bucket is supported at the stated cell-growth-screen
    level, without equating growth inhibition with proven cell death. Several literal
    assay titles repeat a lung-cell descriptor across differently named lines; these
    source labels are preserved without a fresh lineage correction. ANTIBACTERIAL
    is separately backed by the exact-key AntibioticMech row159 and SAME_STRUCTURE
    link. No selected target/mechanism root is written, and none transfers from the
    hydroxylated companion.'
  target_ids:
  - CHEBI:156455
  evidence_ids:
  - bgc-2225-assay-owner
  - bgc-2225-occurrence-owner
  - bgc-2225-query-lotus_occurrences
  - bgc-2225-source-lotus_occurrences
  - bgc-2225-query-chebi_origins
  - bgc-2225-source-chebi_origins
  - bgc-2225-query-pubchem_bioassay
  - bgc-2225-source-pubchem_bioassay
  - bgc-2225-query-bindingdb_targets
  - bgc-2225-query-antibioticmech_inchikeys
  - bgc-2225-source-antibioticmech_inchikeys
  - bgc-2225-source-chebi_structures
  - bgc-2225-source-plan
  - bgc-2225-source-routes
  - bgc-2225-cached-taxonomy
  - bgc-2225-activity-classifier
  - bgc-2225-activity-schema
  - bgc-2225-direct-owner-0
  dimensions:
  - name: occurrence_scope
    value: Six occurrences are three LOTUS plus three ChEBI-origin assertions, not
      six producer experiments.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2225-assay-owner
    - bgc-2225-occurrence-owner
    - bgc-2225-query-lotus_occurrences
    - bgc-2225-source-lotus_occurrences
    - bgc-2225-query-chebi_origins
    - bgc-2225-source-chebi_origins
    - bgc-2225-query-pubchem_bioassay
    - bgc-2225-source-pubchem_bioassay
    - bgc-2225-query-bindingdb_targets
    - bgc-2225-query-antibioticmech_inchikeys
    - bgc-2225-source-antibioticmech_inchikeys
    - bgc-2225-source-chebi_structures
    - bgc-2225-source-plan
    - bgc-2225-source-routes
    - bgc-2225-cached-taxonomy
    - bgc-2225-activity-classifier
    - bgc-2225-activity-schema
    - bgc-2225-direct-owner-0
  - name: assay_target_scope
    value: 41 Active screens,25 written/16 omitted; blank quantitative/target fields;
      coarse activity backing remains scoped.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2225-assay-owner
    - bgc-2225-occurrence-owner
    - bgc-2225-query-lotus_occurrences
    - bgc-2225-source-lotus_occurrences
    - bgc-2225-query-chebi_origins
    - bgc-2225-source-chebi_origins
    - bgc-2225-query-pubchem_bioassay
    - bgc-2225-source-pubchem_bioassay
    - bgc-2225-query-bindingdb_targets
    - bgc-2225-query-antibioticmech_inchikeys
    - bgc-2225-source-antibioticmech_inchikeys
    - bgc-2225-source-chebi_structures
    - bgc-2225-source-plan
    - bgc-2225-source-routes
    - bgc-2225-cached-taxonomy
    - bgc-2225-activity-classifier
    - bgc-2225-activity-schema
    - bgc-2225-direct-owner-0
- assessment_id: bgc-2225-classification
  area: consistency
  topic: Classification
  outcome: unknown
  summary: The topology is a seven-membered tropone-like carbon ring fused to a four-membered
    ring containing two adjacent sulfurs, with one carboxylic acid and one ring carbonyl.
    No sugar, amide or amino group is present in the complete tables. NPClassifier
    Tropolones/Tropolones and derivatives (Shikimate) is compatible as a computed
    scaffold description, while the MIBiG OTHER source BGC class remains a separate
    assertion. Neither the classifier nor the sulfur motif demonstrates a biochemical
    reaction mechanism.
  target_ids:
  - CHEBI:156455
  evidence_ids:
  - bgc-2225-classification-owner
  - bgc-2225-source-npclassifier
  - bgc-2225-source-mibig_compounds
  - bgc-2225-chemistry
  - bgc-2225-topology
  - bgc-2225-structure-schema
  - bgc-2225-review-profile
  - bgc-2225-direct-owner-0
  dimensions:
  - name: classification_applicability
    value: Tropone/C2S2 bicyclic carboxylic-acid topology; model scaffold label and
      source OTHER class remain distinct.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2225-classification-owner
    - bgc-2225-source-npclassifier
    - bgc-2225-source-mibig_compounds
    - bgc-2225-chemistry
    - bgc-2225-topology
    - bgc-2225-structure-schema
    - bgc-2225-review-profile
    - bgc-2225-direct-owner-0
- assessment_id: bgc-2225-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: The complete owner/history, admitted source context, actual intake and
    all paired saved molecular tables were reviewed. No supported local curation defect
    is established within this scope. Five local gates passed, while full QC, OAK
    and external primary-source/taxonomy/accession verification were unavailable.
    The review remains partial; no record, native curation status or history was changed.
  target_ids:
  - CHEBI:156455
  evidence_ids:
  - bgc-2225-owner
  - bgc-2225-intake
  - bgc-2225-intake-acceptance
  - bgc-2225-source-notes
  - bgc-2225-native-acceptance
  - bgc-2225-diagnostic-acceptance
  - bgc-2225-source-plan
  - bgc-2225-plan-acceptance
  - bgc-2225-review-skill
  - bgc-2225-review-profile
  - bgc-2225-direct-owner-0
  dimensions:
  - name: review_completion
    value: Partial; qualified local result with external verification, full QC and
      OAK unavailable.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2225-owner
    - bgc-2225-intake
    - bgc-2225-intake-acceptance
    - bgc-2225-source-notes
    - bgc-2225-native-acceptance
    - bgc-2225-diagnostic-acceptance
    - bgc-2225-source-plan
    - bgc-2225-plan-acceptance
    - bgc-2225-review-skill
    - bgc-2225-review-profile
    - bgc-2225-direct-owner-0
findings: []
actions: []
limitations:
- External identifiers, taxonomy, accessions and primary publications were not refreshed
  under the absolute no-request instruction; historical and database assertions remain
  attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and parsing
  establish their declared mechanical scope only.
- Negative source joins apply only to the exact retained predicates and source snapshots.
  Shared loci, citations and companion records do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source
  records, raw snapshots, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete selected source payloads and explicit direct-context reading attribution
  are preserved in the pinned source notes. All five owner histories, actual intakes
  and ten paired molecular tables were personally read.
- Four original diagnostic warnings remain global and unassigned; no warning is attributed
  to an individual owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-223
```
