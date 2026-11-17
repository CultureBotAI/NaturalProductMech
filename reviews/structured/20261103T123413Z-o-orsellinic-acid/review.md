# Local evidence review: o-orsellinic acid

- Review: 20261103T123413Z-o-orsellinic-acid
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T12:06:20.536618Z
- Finished UTC: 2026-11-03T12:34:13.252111Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

o-Orsellinic acid is coherent within exact stored structure and bounded multi-locus source scope. The accepted maintained view preserves separate OrsA synthesis and AscA substrate-prenylation contexts. Historical sequence and reaction assertions remain unrefreshed; the review is qualified and partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2214; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:32807 | data/natural_products/shikimates_and_phenylpropanoids/o-orsellinic-acid.yaml | generated | o-orsellinic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for o-orsellinic acid | passed | True | CHEBI:32807 | Complete original offline maintained owner view accepted: 2 graphs, 8 node placements and 6 edges; source support remains separately assessed. |
| strict_ten | passed | True | CHEBI:32807 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:32807 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:32807 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:32807 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:32807 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:32807 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:32807 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:32807 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: CHEBI:32807.

CHEBI:32807 and five MIBiG concepts join exact key AMKYESDOVDKZKV-UHFFFAOYSA-N. The encoded 2,4-dihydroxy-6-methylbenzoic acid matches the retained definition. Existing name-disagreement and shared-structure discussions remain open; source-key agreement does not independently settle their historical identity questions. The pathway's o-orsellinate product is a distinct ionic form, not a replacement owner.

### Representation

representation: supported. Targets: CHEBI:32807.

Both forms give neutral C8H8O4 with 12 atoms and 12 bonds, one aromatic ring, a carboxylic acid, two phenolic OH groups and a methyl substituent. No potential stereoelement is returned. All ten comparisons are true and the saved correspondence is complete. This supports the stored representation while leaving full natural-identity verification outside the diagnostic.

### Origin

provenance: supported. Targets: CHEBI:32807.

BGC0000057 v5 (FGSC A4/227321) and BGC0002594 v2 (PH-1/229533) retain BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED from knockout and expression evidence. BGC0002812 v2 (IMI349063/759273) is BGC_CORRELATED/CLUSTER_CORRELATED. BGC0002212 v3 (MCA2997/1381753) and BGC0002596 v2 (20.1/1111077) remain SOURCE_ASSERTION/CLUSTER_UNSTATED. AscA's F-1392 reference is a substrate-consumption context and is not promoted into this producer list.

### Citations

evidence: unknown. Targets: CHEBI:32807.

Imported references have distinct entry versus compound-evidence roles: BGC0000057/2594/2596 cite entry PMIDs 20174687/25011010/33130255; BGC0002212 cites DOI:10.1126/sciadv.aar5459 and 2812 DOI:10.1016/j.ymben.2023.10.002 at compound level. OrsA historical primary annotations and the separately database-scoped AscA evidence remain attributed. The AscA source's truncated DOI and historically inaccessible paper are not silently resolved by this local review.

### Bioactivity

evidence: supported. Targets: CHEBI:32807.

The owner writes five assay placements: two inconclusive EPAC1 rows, inactive APE1 and CYP3A4-activator rows, and an ACTIVE CYP3A4 inhibitors-and-substrates screen; it writes no activity_class or summary. Generic Potency remains OTHER, not IC50, and the active mixed screen is not promoted to a specific inhibitory mechanism. Occurrences include a retained ChEBI Penicillium purpurogenum label whose old taxon 28575 forwards to 1266744; the cache names Talaromyces purpureogenus. Source label, current cached identifier and JS03 21 context remain distinguishable.

### Classification

consistency: supported. Targets: CHEBI:32807.

The aromatic ring bears COOH at the reference carbon, OH at positions 2 and 4 and methyl at 6; there is no sugar or ester linkage in the neutral owner. The simple-phenolic-acid model label is consistent with this topology but remains computed. PKS and TERPENE are imported locus classifications, not proof of two complete production routes. Prenylated, esterified and decarboxylated direct companions remain distinct structures and do not donate their activities or mechanisms.

### Completion

completeness: unknown. Targets: CHEBI:32807.

No supported local curation defect is established within the inspected scope. Complete owner/history, selected/direct source context, actual intake and all paired saved molecular tables were reviewed. The complete maintained reader result was separately accepted. Five local gates passed, while full QC, OAK and external primary-source/taxonomy/sequence verification remain unavailable. This review is partial; no source record or native curation status was changed.

### Mechanism

graph: unknown. Targets: CHEBI:32807.

The accepted complete owner contains two graphs with eight node placements and six edges plus one OrsA pathway step. OrsA uses acetyl-CoA and three malonyl-CoA units to form the conjugate-base o-orsellinate in the retained RHEA:62973 annotation. The separate AscA graph consumes exact neutral owner acid in a MITE example and leaves its intermediate product ungrounded with unspecified geometry. It does not replace OrsA synthesis or transfer BGC0001923, producer status, downstream finality or activity from companions.

### Protein

grounding: unknown. Targets: CHEBI:32807.

OrsA Q5AUX1, EAA59563.1, AN7909.2 and the 2103-aa identity claim remain historical retained annotations. AscA A0A455R413/BBF25313.1 is the reported native 336-aa F-1392 reference; the LC406756.1 reverse-CDS equality claim is not newly recomputed here. Database function and sequence correspondence do not identify the historical assay construct. Mg2+ is explicitly by similarity; no measured occupancy, localization, kinetics or physical complex is inferred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2214-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/o-orsellinic-acid.yaml; Whole owner plaintext and complete curation_history | supports | Complete owner plaintext and its full append-only curation history, read from this exact saved raw file. |
| bgc-2214-capture | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/3/owner_pin; /records/3/owner_document | supports | Complete captured owner for order 2214, with all native source fields, mechanism roots and history preserved. |
| bgc-2214-intake | /private/tmp/npm-review-work/shared-next-batch222/intakes/2214-inspect-001.json; /source; /targets | supports | Actual canonical intake source identity and complete ordered input/target scope. |
| bgc-2214-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-intake-ready-001.json; /status | supports | ROOT acceptance of the original ten canonical intakes; no replay. |
| bgc-2214-grounding-owner | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status; /records/3/owner_document/definition; /records/3/owner_document/definition_source | supports | Written structure, source concepts and grounding status; no external identity refresh. |
| bgc-2214-origin-owner | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters | supports | Complete written producer and locus claims, including versions, evidence methods, grades and citation roles. |
| bgc-2214-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/3/owner_document/occurrences | supports | Complete written occurrences and their source labels, citations and scope notes. |
| bgc-2214-assay-owner | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete captured owner supports its written assay, target, summary and mechanism fields or their absence; this evidence does not assert omitted source-query content. |
| bgc-2214-classification-owner | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/3/owner_document/np_classification; /records/3/owner_document/bgc_class | supports | Written named-model prediction and source BGC classes, retained as separate axes. |
| bgc-2214-source-plan | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3 | supports | Complete selected source context, direct companion paths and exact proposed map, later joined to actual intake. |
| bgc-2214-source-notes | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-scope-notes-001.json; /reading; /cautions; /curation | supports | Whole source-reading attribution, precise direct-context limits and bounded eight-table curation scan; complementary reading is explicitly attributed. |
| bgc-2214-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-target-input-plan-acceptance-001.json; /status; /plan; /inventory; /source_notes; /per_order | supports | ROOT accepted original input plan and retained inventory/notes provenance with exact per-order counts. |
| bgc-2214-chemistry | /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json; /records/3/declared_structure; /records/3/comparisons; /records/3/smiles; /records/3/inchi; /records/3/atom_correspondence | supports | Both complete saved molecular profiles, all atom/bond/stereo/motif fields and literal comparison/mapping results; no new molecular parse. |
| bgc-2214-topology | /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed/atoms; /records/3/smiles/computed/bonds; /records/3/smiles/computed/rings; /records/3/smiles/computed/motifs; /records/3/smiles/computed/potential_stereo; /records/3/smiles/computed/stereo_counts; /records/3/inchi/computed/atoms; /records/3/inchi/computed/bonds; /records/3/inchi/computed/rings; /records/3/inchi/computed/motifs; /records/3/inchi/computed/potential_stereo; /records/3/inchi/computed/stereo_counts; /records/3/atom_correspondence; /records/3/declared_structure | supports | Complete indexed local topology and stereochemistry in both saved forms. Motifs are bounded structural patterns, not residue, natural-identity or experimental assignments. |
| bgc-2214-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-chemistry-acceptance-001.json; /status; /DATA; /execution; /false_comparisons; /warning_scope | supports | ROOT accepted the original twenty-form diagnostic; four global warnings are unassigned and no scientific identity verdict is implied. |
| bgc-2214-native-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-native-gates-acceptance-001.json; /status; /local_commands_passed; /selected_queue_rows; /unavailable_required_gates | supports | Five original local gates passed. Selected queue flags retain their literal scope; full QC and OAK remain unavailable. |
| bgc-2214-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3/source_scope_inventory/joins/mibig_compounds | supports | Complete saved query frame with 5 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned mibig_compounds table; no query replay or external lookup. |
| bgc-2214-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 74, 2640, 3302, 3304, 3435 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":74,"row_sha256":"35bd0d466ddbeec27c31ddb59e22c77876f4875fd1d556cf3270b7463bc05223","row":{"mibig_accession":"BGC0000057","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"partial","compound_name":"orsellinic acid","compound_index":"3","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","standard_inchi":"InChI=1S/C8H8O4/c1-4-2-5(9)3-6(10)7(4)8(11)12/h2-3,9-10H,1H3,(H,11,12)","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:68072","taxon_id":"NCBITaxon:227321","taxon_label":"Aspergillus nidulans FGSC A4","bgc_classes":"PKS","bgc_subclasses":"Iterative type I","genome_accession":"AACD01000135.1","locus_from":"122623","locus_to":"149174","locus_evidence_methods":"Knock-out studies&#124;Gene expression correlated with compound production","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:20174687","reference_basis":"ENTRY"}},{"physical_line":2640,"row_sha256":"ae96b9da832d6605dae51d18fc2524312bfeebea47576fb8f680bc0dceff6102","row":{"mibig_accession":"BGC0002212","entry_version":"3","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"Orsellinic acid","compound_index":"1","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","standard_inchi":"InChI=1S/C8H8O4/c1-4-2-5(9)3-6(10)7(4)8(11)12/h2-3,9-10H,1H3,(H,11,12)","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:68072","taxon_id":"NCBITaxon:1381753","taxon_label":"Moniliophthora roreri MCA 2997","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"AWSO01000045.1","locus_from":"179446","locus_to":"203577","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"DOI:10.1126/sciadv.aar5459","reference_basis":"COMPOUND_EVIDENCE"}},{"physical_line":3302,"row_sha256":"55d99c24b4aadad07e3503baded5592be56b432c8ce722a68240672f959140ef","row":{"mibig_accession":"BGC0002594","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"orsellinic acid","compound_index":"2","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","standard_inchi":"InChI=1S/C8H8O4/c1-4-2-5(9)3-6(10)7(4)8(11)12/h2-3,9-10H,1H3,(H,11,12)","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA024876","taxon_id":"NCBITaxon:229533","taxon_label":"Fusarium graminearum PH-1","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"CM000575.1","locus_from":"5522657","locus_to":"5554323","locus_evidence_methods":"Knock-out studies&#124;Gene expression correlated with compound production","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:25011010","reference_basis":"ENTRY"}},{"physical_line":3304,"row_sha256":"19555d722d0624a85212427ba8a85ec30b7316a0fff336e6fb67745cb70b1ebc","row":{"mibig_accession":"BGC0002596","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"orsellinic acid","compound_index":"2","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","standard_inchi":"InChI=1S/C8H8O4/c1-4-2-5(9)3-6(10)7(4)8(11)12/h2-3,9-10H,1H3,(H,11,12)","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA024876","taxon_id":"NCBITaxon:1111077","taxon_label":"Claviceps purpurea 20.1","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"CAGA01000059.1","locus_from":"98653","locus_to":"131937","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:33130255","reference_basis":"ENTRY"}},{"physical_line":3435,"row_sha256":"2b40221376965d2ed836a33edc11c5ad38c441ad0e841c9de321e24e7c313274","row":{"mibig_accession":"BGC0002812","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"Orsellinic acid","compound_index":"7","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","standard_inchi":"InChI=1S/C8H8O4/c1-4-2-5(9)3-6(10)7(4)8(11)12/h2-3,9-10H,1H3,(H,11,12)","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"Alkylresorcinol/phloroglucinol polyketide","database_ids":"chembl:CHEMBL457583&#124;pubchem:68072","taxon_id":"NCBITaxon:759273","taxon_label":"Colletotrichum higginsianum IMI 349063","bgc_classes":"PKS&#124;terpene","bgc_subclasses":"Type I&#124;Monoterpene","genome_accession":"LTAN01000004.1","locus_from":"389265","locus_to":"404974","locus_evidence_methods":"Correlation of genomic and metabolomic data","producer_evidence_basis":"BGC_CORRELATED","cluster_link_evidence_basis":"CLUSTER_CORRELATED","primary_reference":"DOI:10.1016/j.ymben.2023.10.002","reference_basis":"COMPOUND_EVIDENCE"}}] |
| bgc-2214-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3/source_scope_inventory/joins/chebi_structures | supports | Complete saved query frame with 1 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned chebi_structures table; no query replay or external lookup. |
| bgc-2214-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Physical TSV lines 8527 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":8527,"row_sha256":"173a035cad43a578645d6b1236b625acccc507cb0111d19bf903391d69c225ff","row":{"chebi_id":"CHEBI:32807","name":"o-orsellinic acid","definition":"A dihydroxybenzoic acid that is 2,4-dihydroxybenzoic acid in which the hydrogen at position 6 is replaced by a methyl group.","stars":"3","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","smiles":"Cc1cc(O)cc(O)c1C(=O)O"}}] |
| bgc-2214-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved query frame with 20 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned lotus_occurrences table; no query replay or external lookup. |
| bgc-2214-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":184,"row_sha256":"b3deb61168e1abe5276bdb464f0767dc7c23434edb0a5da512c4318e9d2c5b57","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Nidularia pulvinata","taxon_id":"NCBITaxon:1081941","organism_wikidata":"http://www.wikidata.org/entity/Q10600580","reference_doi":"10.1515/ZNC-1997-5-606","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":185,"row_sha256":"ec70fa6467bded35c4de11b7ab555d1e44e5fc89b8a400df958dc39d256833d1","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Hypoxylon rubiginosum","taxon_id":"NCBITaxon:110542","organism_wikidata":"http://www.wikidata.org/entity/Q2604190","reference_doi":"10.1021/NP040063L","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":186,"row_sha256":"2de22ab4c6f81f3cc8985855f93070223ffc649d86307a29e64d1f18a16f43bb","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus nidulans","taxon_id":"NCBITaxon:162425","organism_wikidata":"http://www.wikidata.org/entity/Q683881","reference_doi":"10.1073/PNAS.0901870106","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":187,"row_sha256":"cd2f201544dc1aea4019e073730ea19ffd41054b32f7a74e5b850494c63e9350","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Parmotrema stuppeum","taxon_id":"NCBITaxon:2041279","organism_wikidata":"http://www.wikidata.org/entity/Q10620935","reference_doi":"10.1515/ZNC-2000-11-1227","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":188,"row_sha256":"462d49e0c4924f08852c919349a62fd5f6db080191545c51be066358e7759e13","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Parmotrema tinctorum","taxon_id":"NCBITaxon:235862","organism_wikidata":"http://www.wikidata.org/entity/Q7139222","reference_doi":"10.4268/CJCMM20141620","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":189,"row_sha256":"986307573be1e38e9e1d855fa7514a08eae0a8f93e7623974cfd70350528aafb","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Dolichousnea longissima","taxon_id":"NCBITaxon:281306","organism_wikidata":"http://www.wikidata.org/entity/Q1809933","reference_doi":"10.1016/S0031-9422(00)82466-8","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":190,"row_sha256":"6f559fc187ff5eae76cbb7e881586137d96fed34c65b33d19e45ffd461a099af","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Parmotrema cooperi","taxon_id":"NCBITaxon:2910500","organism_wikidata":"http://www.wikidata.org/entity/Q10620728","reference_doi":"10.1007/S11426-011-4436-2","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":191,"row_sha256":"bc42a794a6e30d23483c043a9d2201199a1b8f946a96565310a824e5d688384c","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus terreus","taxon_id":"NCBITaxon:33178","organism_wikidata":"http://www.wikidata.org/entity/Q3798237","reference_doi":"10.1016/J.PHYTOL.2015.02.009","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":192,"row_sha256":"5f3e155398751350a1c4c63531bac900c18f9057cdc25d05a3c647c047f34ccd","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus terreus","taxon_id":"NCBITaxon:33178","organism_wikidata":"http://www.wikidata.org/entity/Q3798237","reference_doi":"10.1039/C39720000391","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":193,"row_sha256":"4d347b7b3ed93bb7424ae4e3529c81a11d0c4983327986ad939240b85afb1e67","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Penicillium aurantiogriseum","taxon_id":"NCBITaxon:36655","organism_wikidata":"http://www.wikidata.org/entity/Q7162856","reference_doi":"10.1039/C39920000646","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":194,"row_sha256":"537b06fc15be5fd9a46f8dae2bdf7c0c9f26b5891c988bde7f4952abe9f99eb8","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Chaetomium globosum","taxon_id":"NCBITaxon:38033","organism_wikidata":"http://www.wikidata.org/entity/Q2947551","reference_doi":"10.1021/NP058014B","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":195,"row_sha256":"7fef90c8359167d056db49bb3231f44138d71baf176061221aa4d0ea5cfc7ad6","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Umbilicaria torrefacta","taxon_id":"NCBITaxon:392743","organism_wikidata":"http://www.wikidata.org/entity/Q10667752","reference_doi":"10.1016/0031-9422(90)83052-3","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":196,"row_sha256":"d5ec47c15bf4c8bdd6018451f174b3b735edba90c2ce134f420d85a11998b1d8","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus flavus","taxon_id":"NCBITaxon:5059","organism_wikidata":"http://www.wikidata.org/entity/Q137096","reference_doi":"10.1271/BBB.63.820","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":197,"row_sha256":"9633ea56dbfefbfa94a34bb8c441372aaaacc62abe9276bb283f9be2786195d3","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Penicillium","taxon_id":"NCBITaxon:5073","organism_wikidata":"http://www.wikidata.org/entity/Q843136","reference_doi":"10.1021/NP500885F","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":198,"row_sha256":"d5fd2b719da4970b5fbd355d0767252499cb0b7a825aed616f7799f3eaecaa83","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Escherichia coli","taxon_id":"NCBITaxon:562","organism_wikidata":"http://www.wikidata.org/entity/Q25419","reference_doi":"10.1073/PNAS.0901870106","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":199,"row_sha256":"f7b35b2fb410d76ef3fdaf72bab88a576ae11d0151a1b78ce911c855688cd2f7","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Penicillium cyclopium","taxon_id":"NCBITaxon:60167","organism_wikidata":"http://www.wikidata.org/entity/Q104083838","reference_doi":"10.1039/C39920000646","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":200,"row_sha256":"30aee3451e80f774cc4dfdfc95344daccad3feeacab9a25068b178682379d692","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus fumigatus","taxon_id":"NCBITaxon:746128","organism_wikidata":"http://www.wikidata.org/entity/Q134359","reference_doi":"10.1042/BJ0970321","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":201,"row_sha256":"20302888b21642bf97d60b1a51da2538ded7a6a8cc680f534ef84737f0baaf0b","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus fumigatus","taxon_id":"NCBITaxon:746128","organism_wikidata":"http://www.wikidata.org/entity/Q134359","reference_doi":"10.1042/BJ0980353","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":202,"row_sha256":"c84916f88a343173ca081d198ac98f2256253f5d6882991c237e4f24ce2bec2d","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus fumigatus","taxon_id":"NCBITaxon:746128","organism_wikidata":"http://www.wikidata.org/entity/Q134359","reference_doi":"10.1080/13693780802307720","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":203,"row_sha256":"a36bd5f89920b4f87010a1c993806ca992acec85238ef10be8ebe3bb3fa94003","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Stachybotrys cylindrospora","taxon_id":"NCBITaxon:80386","organism_wikidata":"http://www.wikidata.org/entity/Q10676890","reference_doi":"10.1139/V93-069","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}}] |
| bgc-2214-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved query frame with 0 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned cyanometdb_occurrences table; no query replay or external lookup. |
| bgc-2214-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3/source_scope_inventory/joins/npclassifier | supports | Complete saved query frame with 1 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned npclassifier table; no query replay or external lookup. |
| bgc-2214-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 69 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":69,"row_sha256":"321bb05768a1da671b40fbd28fcbe07307095196ecbbf502749bda222d706b04","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Phenolic acids (C6-C1)","class_results":"Simple phenolic acids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}] |
| bgc-2214-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved query frame with 5 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned pubchem_bioassay table; no query replay or external lookup. |
| bgc-2214-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 170, 171, 172, 173, 174 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":170,"row_sha256":"d6cc563ddb22451204ade52699b0c8036de190d4bffa8f2bcff0863b1a6814b8","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","cid":"68072","aid":"1645883","assay_name":"Validation qHTS for agonist of cAMP-regulated guanine nucleotide exchange factor 3 (EPAC1)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"89.1251","target_accession":"","reference":""}},{"physical_line":171,"row_sha256":"cb9dfe913bf6fa2fe44d8219577ca7790828733624b3509be057d3b1c4b222f1","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","cid":"68072","aid":"1645883","assay_name":"Validation qHTS for agonist of cAMP-regulated guanine nucleotide exchange factor 3 (EPAC1)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"89.1251","target_accession":"O95398","reference":""}},{"physical_line":172,"row_sha256":"642f5ad5d982ec28086721d44c72e959cea304fd28323f435f859816628a5aa6","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","cid":"68072","aid":"2517","assay_name":"qHTS Assay for Inhibitors of the Human Apurinic/apyrimidinic Endonuclease 1 (APE1)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"0.0089","target_accession":"1DE9_A","reference":""}},{"physical_line":173,"row_sha256":"ae58a8414c50c9e8775b61fb47cefecbd63f503b80a15ad4e01043e93ad31157","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","cid":"68072","aid":"884","assay_name":"qHTS Assay for Inhibitors and Substrates of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Active","activity_name":"Potency","activity_value_um":"25.1189","target_accession":"NP_059488","reference":""}},{"physical_line":174,"row_sha256":"5310f06da0b121f76a6ba14bce0ac4b8d8dd2038c3c6e0801dda20bce406462c","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","cid":"68072","aid":"885","assay_name":"qHTS Assay for Activators of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"25.1189","target_accession":"NP_059488","reference":""}}] |
| bgc-2214-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved query frame with 0 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned bindingdb_targets table; no query replay or external lookup. |
| bgc-2214-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved query frame with 0 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned antibioticmech_inchikeys table; no query replay or external lookup. |
| bgc-2214-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3/source_scope_inventory/joins/chebi_origins | supports | Complete saved query frame with 2 positive placements. Exact saved predicate exact chebi_id from exact full-key structure rows with query ["CHEBI:32807"] against the pinned chebi_origins table; no query replay or external lookup. |
| bgc-2214-source-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Physical TSV lines 4699, 4700 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":4699,"row_sha256":"b7692b794d73b99dc96dc72f18a349518a1941068d14699200b3994109aa17be","row":{"chebi_id":"CHEBI:32807","species_text":"Ascomycota sp. Ind19F07","species_accession":"1583058","component_text":"","strain_text":"","source_accession":"25537370","comments":""}},{"physical_line":4700,"row_sha256":"d65ab4af495b8f61b7a7d5dc3eabf60e5071eb55929649b8ae466cb41a8cc15e","row":{"chebi_id":"CHEBI:32807","species_text":"Penicillium purpurogenum","species_accession":"28575","component_text":"mycelium","strain_text":"JS03 21","source_accession":"21879714","comments":"Ethylacetate extract of fermentation broth and acetone extract of mycelia"}}] |
| bgc-2214-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/1; /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/whole_stanzas/11; /cached_taxonomy/whole_stanzas/20; /cached_taxonomy/whole_stanzas/22; /cached_taxonomy/whole_stanzas/25; /cached_taxonomy/whole_stanzas/39; /cached_taxonomy/whole_stanzas/50; /cached_taxonomy/whole_stanzas/70; /cached_taxonomy/whole_stanzas/92; /cached_taxonomy/whole_stanzas/104; /cached_taxonomy/whole_stanzas/105; /cached_taxonomy/whole_stanzas/109; /cached_taxonomy/whole_stanzas/114; /cached_taxonomy/whole_stanzas/130; /cached_taxonomy/whole_stanzas/142; /cached_taxonomy/whole_stanzas/143; /cached_taxonomy/whole_stanzas/152; /cached_taxonomy/whole_stanzas/153; /cached_taxonomy/whole_stanzas/155; /cached_taxonomy/whole_stanzas/163; /cached_taxonomy/whole_stanzas/166; /cached_taxonomy/whole_stanzas/173; /cached_taxonomy/whole_stanzas/180 | supports | Complete personally read cached name/synonym stanzas for selected source taxa: [{"id":"NCBITaxon:562","physical_line":881,"complete_stanza":"[Term]\nid: NCBITaxon:562\nname: Escherichia coli\nsynonym: \"Bacillus coli\" EXACT []\nsynonym: \"Bacterium coli\" EXACT []\nsynonym: \"Bacterium coli commune\" EXACT []\nsynonym: \"Enterococcus coli\" EXACT []\nsynonym: \"Escherichia/Shigella coli\" EXACT []\n\n"},{"id":"NCBITaxon:5059","physical_line":7866,"complete_stanza":"[Term]\nid: NCBITaxon:5059\nname: Aspergillus flavus\nsynonym: \"Aspergillus flavus var. parvisclerotigenus\" EXACT []\nsynonym: \"Aspergillus parvisclerotigenus\" EXACT []\nsynonym: \"Petromyces flavus\" EXACT []\n\n"},{"id":"NCBITaxon:5073","physical_line":7923,"complete_stanza":"[Term]\nid: NCBITaxon:5073\nname: Penicillium\nsynonym: \"Eupenicillium\" EXACT []\n\n"},{"id":"NCBITaxon:33178","physical_line":14562,"complete_stanza":"[Term]\nid: NCBITaxon:33178\nname: Aspergillus terreus\nsynonym: \"Aspergillus terrestris\" EXACT []\n\n"},{"id":"NCBITaxon:36655","physical_line":15999,"complete_stanza":"[Term]\nid: NCBITaxon:36655\nname: Penicillium aurantiogriseum\n\n"},{"id":"NCBITaxon:38033","physical_line":16592,"complete_stanza":"[Term]\nid: NCBITaxon:38033\nname: Chaetomium globosum\nsynonym: \"Chaetomium rectum\" EXACT []\n\n"},{"id":"NCBITaxon:60167","physical_line":27608,"complete_stanza":"[Term]\nid: NCBITaxon:60167\nname: Penicillium cyclopium\nsynonym: \"Penicillium verrucosum var. cyclopium\" EXACT []\n\n"},{"id":"NCBITaxon:80386","physical_line":35899,"complete_stanza":"[Term]\nid: NCBITaxon:80386\nname: Stachybotrys cylindrospora\n\n"},{"id":"NCBITaxon:110542","physical_line":44030,"complete_stanza":"[Term]\nid: NCBITaxon:110542\nname: Hypoxylon rubiginosum\nsynonym: \"Sphaeria rubiginosa\" EXACT []\n\n"},{"id":"NCBITaxon:162425","physical_line":55539,"complete_stanza":"[Term]\nid: NCBITaxon:162425\nname: Aspergillus nidulans\nsynonym: \"Aspergillus nidulans (Eidam) G. Winter, 1884\" EXACT []\nsynonym: \"Aspergillus nidulellus\" EXACT []\nsynonym: \"Emericella nidulans\" EXACT []\nsynonym: \"Sterigmatocystis nidulans\" EXACT []\n\n"},{"id":"NCBITaxon:227321","physical_line":69073,"complete_stanza":"[Term]\nid: NCBITaxon:227321\nname: Aspergillus nidulans FGSC A4\nsynonym: \"Emericella nidulans FGSC A4\" EXACT []\n\n"},{"id":"NCBITaxon:229533","physical_line":69588,"complete_stanza":"[Term]\nid: NCBITaxon:229533\nname: Fusarium graminearum PH-1\nsynonym: \"Gibberella zeae PH-1\" EXACT []\n\n"},{"id":"NCBITaxon:235862","physical_line":70513,"complete_stanza":"[Term]\nid: NCBITaxon:235862\nname: Parmotrema tinctorum\nsynonym: \"Parmelia tinctorum\" EXACT []\nsynonym: \"Parmotrema tinctorum (Despr. ex Nyl.) Hale, 1974\" EXACT []\n\n"},{"id":"NCBITaxon:281306","physical_line":77060,"complete_stanza":"[Term]\nid: NCBITaxon:281306\nname: Dolichousnea longissima\nsynonym: \"Usnea longissima\" EXACT []\n\n"},{"id":"NCBITaxon:392743","physical_line":90225,"complete_stanza":"[Term]\nid: NCBITaxon:392743\nname: Umbilicaria torrefacta\nsynonym: \"Lichen torrefactus\" EXACT []\n\n"},{"id":"NCBITaxon:746128","physical_line":109335,"complete_stanza":"[Term]\nid: NCBITaxon:746128\nname: Aspergillus fumigatus\nsynonym: \"Aspergillus fumigatus Fresen., 1863\" EXACT []\nsynonym: \"Aspergillus fumigatus var. ellipticus\" EXACT []\nsynonym: \"Aspergillus neoellipticus\" EXACT []\nsynonym: \"Neosartorya fumigata\" EXACT []\nsynonym: \"Sartorya fumigata\" EXACT []\n\n"},{"id":"NCBITaxon:759273","physical_line":110037,"complete_stanza":"[Term]\nid: NCBITaxon:759273\nname: Colletotrichum higginsianum IMI 349063\n\n"},{"id":"NCBITaxon:1081941","physical_line":117808,"complete_stanza":"[Term]\nid: NCBITaxon:1081941\nname: Nidularia pulvinata\nsynonym: \"Cyathus pulvinatus\" EXACT []\n\n"},{"id":"NCBITaxon:1111077","physical_line":118627,"complete_stanza":"[Term]\nid: NCBITaxon:1111077\nname: Claviceps purpurea 20.1\n\n"},{"id":"NCBITaxon:1266744","physical_line":124644,"complete_stanza":"[Term]\nid: NCBITaxon:1266744\nname: Talaromyces purpureogenus\nsynonym: \"Penicillium crateriforme\" EXACT []\nsynonym: \"Penicillium purpureogenum Stoll, 1904\" EXACT []\nsynonym: \"Penicillium purpureogenum var. rubri-sclerotium\" EXACT []\nsynonym: \"Penicillium sanguineum\" EXACT []\n\n"},{"id":"NCBITaxon:1381753","physical_line":127759,"complete_stanza":"[Term]\nid: NCBITaxon:1381753\nname: Moniliophthora roreri MCA 2997\n\n"},{"id":"NCBITaxon:1583058","physical_line":133924,"complete_stanza":"[Term]\nid: NCBITaxon:1583058\nname: Ascomycota sp. Ind19F07\n\n"},{"id":"NCBITaxon:2041279","physical_line":143906,"complete_stanza":"[Term]\nid: NCBITaxon:2041279\nname: Parmotrema stuppeum\nsynonym: \"Parmelia stuppea\" EXACT []\n\n"},{"id":"NCBITaxon:2910500","physical_line":153767,"complete_stanza":"[Term]\nid: NCBITaxon:2910500\nname: Parmotrema cooperi\nsynonym: \"Parmelia cooperi\" EXACT []\n\n"}]. No hierarchy or fresh taxonomy verification is inferred. |
| bgc-2214-source-routes | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/3/source_scope_inventory/source_taxa; /records/3/source_scope_inventory/forward_taxon_merge_matches; /records/3/source_scope_inventory/nonorganism_matches | supports | Exact saved source-taxon and forward-merge/nonorganism route lists. Old ID 28575 forwards to 1266744; absence of its own cached stanza is not loss of the admitted merge route. |
| bgc-2214-direct-owner-0 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/1/complete_raw_text; /contexts/1/complete_raw_history; /contexts/1/source_scope_inventory | supports | Complete directly admitted companion F9775A, key KEHZWGZVOZXIKE-UHFFFAOYSA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-direct-owner-1 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/2/complete_raw_text; /contexts/2/complete_raw_history; /contexts/2/source_scope_inventory | supports | Complete directly admitted companion F9775B, key ZFYMCYAXXOXUHT-UHFFFAOYSA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-direct-owner-2 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/3/complete_raw_text; /contexts/3/complete_raw_history; /contexts/3/source_scope_inventory | supports | Complete directly admitted companion o-orsellinate depside, key HEMSJKZDHNSSEW-UHFFFAOYSA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-direct-owner-3 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/10/complete_raw_text; /contexts/10/complete_raw_history; /contexts/10/source_scope_inventory | supports | Complete directly admitted companion Colletorin D acid, key FZLIGQLGBRLYQX-UHFFFAOYSA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-direct-owner-4 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/32/complete_raw_text; /contexts/32/complete_raw_history; /contexts/32/source_scope_inventory | supports | Complete directly admitted companion Colletochlorin A, key BZMLULUMBUVADU-AZWQULSGSA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-direct-owner-5 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/33/complete_raw_text; /contexts/33/complete_raw_history; /contexts/33/source_scope_inventory | supports | Complete directly admitted companion Colletochlorin B, key UEUMAXMCCDEOIJ-XYOKQWHBSA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-direct-owner-6 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/34/complete_raw_text; /contexts/34/complete_raw_history; /contexts/34/source_scope_inventory | supports | Complete directly admitted companion Colletochlorin D, key JQJZJLLBOLNQAF-UHFFFAOYSA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-direct-owner-7 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/35/complete_raw_text; /contexts/35/complete_raw_history; /contexts/35/source_scope_inventory | supports | Complete directly admitted companion Colletorin A, key QXFKEGZSZLPBGD-VZUCSPMQSA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-direct-owner-8 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/36/complete_raw_text; /contexts/36/complete_raw_history; /contexts/36/source_scope_inventory | supports | Complete directly admitted companion Colletorin B, key SXOCWLUWTFGULD-MDWZMJQESA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-direct-owner-9 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/37/complete_raw_text; /contexts/37/complete_raw_history; /contexts/37/source_scope_inventory | supports | Complete directly admitted companion Colletorin D, key ITDNZOGHXSEHSE-UHFFFAOYSA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-direct-owner-10 | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /contexts/38/complete_raw_text; /contexts/38/complete_raw_history; /contexts/38/source_scope_inventory | supports | Complete directly admitted companion orcinol, key OIPPWFOQEKKFEE-UHFFFAOYSA-N, with its own history/source context. Reading attribution is in source notes; no transitive, mechanism, activity or identity transfer. |
| bgc-2214-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Workflow; Output | supports | Immutable claim-level review, local evidence scope, honest partial completion and actionable ownership. |
| bgc-2214-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Complete maintained review profile | supports | Source qualification, producer/occurrence distinctions, computed-classification limits and evidence-backed issue normalization. |
| bgc-2214-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 376–432 | supports | Structure and stereo encoding plus explicitly computed NPClassifier fields; model outputs are not source assertions. |
| bgc-2214-activity-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 632–665; lines 920–947 | supports | Optional observation activity_class and coarse activity buckets require backing; no dedicated cytotoxic or enzyme-inhibitor definition is supplied. |
| bgc-2214-activity-classifier | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 127–179; lines 1310–1382 | supports | Maintained classifier unambiguity intent, generic title patterns, ACTIVE-only class assignment and written-observation summary derivation. |
| bgc-2214-definition-owner | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 985–1005 | supports | Maintained seeder copies a unique retained ChEBI definition and its source identifier; a correction must preserve honest provenance. |
| bgc-2214-reader-DATA | /private/tmp/npm-review-work/shared-next-batch222/native-current222-o-orsellinic-acid-maintained-reader-DATA-001.json; /resolved_view; /raw_owner; /expected_view; /counts; /returned_view_equals_expected_complete_owner; /review_check_metadata | supports | Complete original maintained owner view equals the captured owner, preserving every graph/pathway/target/history field; no scientific evidence is upgraded by reader success. |
| bgc-2214-reader-execution | /private/tmp/npm-review-work/shared-next-batch222/native-current222-o-orsellinic-acid-reader-execution-001.json; /exit_code; /command; /stdout; /stderr; /original_tool | supports | Original maintained-reader execution receipt, streams and exact invocation provenance. |
| bgc-2214-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-o-orsellinic-acid-maintained-reader-acceptance-001.json; /status; /verification; /review_check_contract | supports | ROOT acceptance of exact complete-owner/positive-content equality and original terminal success; expected capability construction was denied before action, with no external request. |
| bgc-2214-graph-0 | /private/tmp/npm-review-work/shared-next-batch222/native-current222-o-orsellinic-acid-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/0 | supports | Complete graph o-orsellinic-acid-orsa-biosynthesis: 4 node placements and 3 edges, every evidence item and limitation retained. Retained graph description: Partial Aspergillus nidulans o-orsellinic acid biosynthesis graph for OrsA condensation of acetyl-CoA and malonyl-CoA units to o-orsellinate. |
| bgc-2214-graph-1 | /private/tmp/npm-review-work/shared-next-batch222/native-current222-o-orsellinic-acid-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/1 | supports | Complete graph o-orsellinic-acid-asca-database-substrate-prenylation: 4 node placements and 3 edges, every evidence item and limitation retained. Retained graph description: MITE-reported farnesyl-prenylation of exact o-orsellinic acid as substrate. AscA is the sequence-verified native Acremonium egyptiacum F-1392 reference. This separate database context consumes the owner compound and does not replace its Aspergillus nidulans OrsA synthesis pathway or transfer producer or BGC assertions. Functional evidence remains database-level; the primary paper was inaccessible. Product geometry and ionic-form limits remain explicit; existing open discussions and SEEDED status are preserved. |
| bgc-2214-pathway | /private/tmp/npm-review-work/shared-next-batch222/native-current222-o-orsellinic-acid-maintained-reader-DATA-001.json; /resolved_view/biosynthetic_pathway | supports | Whole retained OrsA pathway step, exact ionic product and all four evidence items; no fresh reaction or protein resolution. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-222/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-222/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-222/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-222/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-222/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-222/native-current222-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External compound/taxon/protein/accession and primary-paper verification was unavailable under the absolute local-only restriction; retained historical claims are attributed, not refreshed.
- Full QC and OAK were unavailable. Successful local gates, parsing and maintained-reader checks establish their declared mechanical scope only.
- Source-query results are bounded by exact full-key/direct-owned-BGC/source-taxon predicates and the saved cohort; negative joins are not global absence claims.
- No additional molecular or YAML parse was performed during fragment authoring. Source records, raw snapshots, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Source reading uses the complete selected payloads and explicit complementary/direct-context attribution in pinned notes. All first-five paired molecular tables and selected owner histories were personally read.
- Four diagnostic warnings remain global and unassigned; no per-record warning inference.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T123413Z-o-orsellinic-acid
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: o-orsellinic acid'
started_at: '2026-11-03T12:06:20.536618Z'
finished_at: '2026-11-03T12:34:13.252111Z'
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
summary: o-Orsellinic acid is coherent within exact stored structure and bounded multi-locus
  source scope. The accepted maintained view preserves separate OrsA synthesis and
  AscA substrate-prenylation contexts. Historical sequence and reaction assertions
  remain unrefreshed; the review is qualified and partial.
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
  - path: data/natural_products/polyketides/f9775a.yaml
    sha256: b71f4d7b45aec4d89d516868243054dd631a59599f3aef4e815e28eb20432ebd
    role: context
  - path: data/natural_products/polyketides/f9775b.yaml
    sha256: 34c1d9d1a7adfb089abc1252c6e2b25b8555c0f8d090d38fb50b6b212cb022bd
    role: context
  - path: data/natural_products/polyketides/o-orsellinate-depside.yaml
    sha256: 59d4a5e4e8976c90d53d457fe8e18692c512ffb79a409dc011308c12e6254a49
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/colletorin-d-acid.yaml
    sha256: 64938c71025b05e94eec2d6bc07f6e45d61affad9aabd46d02b264e274d01a65
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/o-orsellinic-acid.yaml
    sha256: 01d99f2ce8a8be87d0217b9e43bbcbad5cf2efb660ee762e999af8e6125c4a62
    role: target
  - path: data/natural_products/unclassified/colletochlorin-a.yaml
    sha256: 2d843838d8977ec0519fbeb1d47601443318e5056daac733bd63af47b79abe5a
    role: context
  - path: data/natural_products/unclassified/colletochlorin-b.yaml
    sha256: 5a1975dc5cd9ae8323b0a36b3c3cb23c22e4fbb24306f772550e0015efb4304f
    role: context
  - path: data/natural_products/unclassified/colletochlorin-d.yaml
    sha256: 8bfb85c57473ccdfdb5a30508ce7f0ef3cb29cb9efcd46e62b584eb1909044e8
    role: context
  - path: data/natural_products/unclassified/colletorin-a.yaml
    sha256: 3732b9c37f6a09456e0faa351279410354a1aca7e5ec3dbc5ebe50b10c8b4100
    role: context
  - path: data/natural_products/unclassified/colletorin-b.yaml
    sha256: 7b9c0d25d65a62dbc9b57cf4209506f2c3888b8b8d2b0cee51c280e8c1cda584
    role: context
  - path: data/natural_products/unclassified/colletorin-d.yaml
    sha256: 9c8bbe6ba53d9c522b5a17a911f24c0a1d6353b36c63fd5c33330763fbd482e8
    role: context
  - path: data/natural_products/unclassified/orcinol.yaml
    sha256: e87f5d151175f928393cf26377665768835b19f278c59341a731d081781ceb70
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
  - path: data/raw/taxon_merged.tsv
    sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
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
  selection: Campaign path order 2214; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:32807
targets:
- target_id: CHEBI:32807
  path: data/natural_products/shikimates_and_phenylpropanoids/o-orsellinic-acid.yaml
  label: o-orsellinic acid
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
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Exact assay identity exclusion decisions for selected/direct source context.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_merged.tsv
    role: Exact retained selected/direct taxon decision; no fresh authority.
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
    path: data/natural_products/shikimates_and_phenylpropanoids/o-orsellinic-acid.yaml
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
  name: Complete offline maintained reader for o-orsellinic acid
  status: passed
  required: true
  target_ids:
  - CHEBI:32807
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch222/read-selected-mechanism-guarded-001.py
    2214 8715749ac3fc8e01b4d7d0b4a76c8b13542fa0210f8aec76aaee058005ec3bf6 45849b3cbd9947cf83521ae61c15e5cdfeee276efc58b8e3540dba3f88c04704
    28be4db832f40820b47da073c6ed3f945d86998f30f6335dfdc5be2d5d537856 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
    deb31a6decd5b83371e50c68e20749010ef3603bb5360f563c913df51cb754b9
  exit_code: 0
  evidence_ids:
  - bgc-2214-reader-DATA
  - bgc-2214-reader-execution
  - bgc-2214-reader-acceptance
  summary: 'Complete original offline maintained owner view accepted: 2 graphs, 8
    node placements and 6 edges; source support remains separately assessed.'
  scope_note: Exact selected owner only; no external requests or fresh scientific
    verification.
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:32807
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
  - CHEBI:32807
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
  - CHEBI:32807
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
  - CHEBI:32807
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
  - CHEBI:32807
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
  - CHEBI:32807
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:32807
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:32807
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2214-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/o-orsellinic-acid.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete owner plaintext and its full append-only curation history, read
    from this exact saved raw file.
  snapshot_sha256: 01d99f2ce8a8be87d0217b9e43bbcbad5cf2efb660ee762e999af8e6125c4a62
- evidence_id: bgc-2214-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/3/owner_pin; /records/3/owner_document
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete captured owner for order 2214, with all native source fields,
    mechanism roots and history preserved.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2214-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/intakes/2214-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Actual canonical intake source identity and complete ordered input/target
    scope.
  snapshot_sha256: 45849b3cbd9947cf83521ae61c15e5cdfeee276efc58b8e3540dba3f88c04704
- evidence_id: bgc-2214-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-intake-ready-001.json
  locator: /status
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: ROOT acceptance of the original ten canonical intakes; no replay.
  snapshot_sha256: ffb4558e78e080f45baf4ccb369e72778c7e34de1c5b2fea82d2433818ea225a
- evidence_id: bgc-2214-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts;
    /records/3/owner_document/grounding_status; /records/3/owner_document/definition;
    /records/3/owner_document/definition_source
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Written structure, source concepts and grounding status; no external identity
    refresh.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2214-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete written producer and locus claims, including versions, evidence
    methods, grades and citation roles.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2214-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/3/owner_document/occurrences
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete written occurrences and their source labels, citations and scope
    notes.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2214-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete captured owner supports its written assay, target, summary and
    mechanism fields or their absence; this evidence does not assert omitted source-query
    content.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2214-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_classification; /records/3/owner_document/bgc_class
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Written named-model prediction and source BGC classes, retained as separate
    axes.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2214-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete selected source context, direct companion paths and exact proposed
    map, later joined to actual intake.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: bgc-2214-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-scope-notes-001.json
  locator: /reading; /cautions; /curation
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Whole source-reading attribution, precise direct-context limits and bounded
    eight-table curation scan; complementary reading is explicitly attributed.
  snapshot_sha256: 462e1f8450cc46b50f7e764c6be3a6fec2300b65d200898c74a5e562934ad86e
- evidence_id: bgc-2214-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-target-input-plan-acceptance-001.json
  locator: /status; /plan; /inventory; /source_notes; /per_order
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: ROOT accepted original input plan and retained inventory/notes provenance
    with exact per-order counts.
  snapshot_sha256: 87cb8226f49b19e0cf589a83c45de342083de01cee4ee071fdbbf31209fdc719
- evidence_id: bgc-2214-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/declared_structure; /records/3/comparisons; /records/3/smiles;
    /records/3/inchi; /records/3/atom_correspondence
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Both complete saved molecular profiles, all atom/bond/stereo/motif fields
    and literal comparison/mapping results; no new molecular parse.
  snapshot_sha256: d6777b269b79f346e064435d16f6783b96b6dc0d84d181802a8be587185ebc61
- evidence_id: bgc-2214-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed/atoms; /records/3/smiles/computed/bonds; /records/3/smiles/computed/rings;
    /records/3/smiles/computed/motifs; /records/3/smiles/computed/potential_stereo;
    /records/3/smiles/computed/stereo_counts; /records/3/inchi/computed/atoms; /records/3/inchi/computed/bonds;
    /records/3/inchi/computed/rings; /records/3/inchi/computed/motifs; /records/3/inchi/computed/potential_stereo;
    /records/3/inchi/computed/stereo_counts; /records/3/atom_correspondence; /records/3/declared_structure
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete indexed local topology and stereochemistry in both saved forms.
    Motifs are bounded structural patterns, not residue, natural-identity or experimental
    assignments.
  snapshot_sha256: d6777b269b79f346e064435d16f6783b96b6dc0d84d181802a8be587185ebc61
- evidence_id: bgc-2214-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-chemistry-acceptance-001.json
  locator: /status; /DATA; /execution; /false_comparisons; /warning_scope
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: ROOT accepted the original twenty-form diagnostic; four global warnings
    are unassigned and no scientific identity verdict is implied.
  snapshot_sha256: ed41c7b477fc10da9308cd55cfe70fe0b682312dec7fc5d153d824d02ad41ad8
- evidence_id: bgc-2214-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-native-gates-acceptance-001.json
  locator: /status; /local_commands_passed; /selected_queue_rows; /unavailable_required_gates
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Five original local gates passed. Selected queue flags retain their literal
    scope; full QC and OAK remain unavailable.
  snapshot_sha256: c2001fae878fca8947ab9a9a883c8f4c8bb09101fd0bed77c7e7c90c4d87f9a7
- evidence_id: bgc-2214-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 5 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N"
    against the pinned mibig_compounds table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned mibig_compounds table;
    no query replay or external lookup.
- evidence_id: bgc-2214-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 74, 2640, 3302, 3304, 3435
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":74,"row_sha256":"35bd0d466ddbeec27c31ddb59e22c77876f4875fd1d556cf3270b7463bc05223","row":{"mibig_accession":"BGC0000057","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"partial","compound_name":"orsellinic
    acid","compound_index":"3","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","standard_inchi":"InChI=1S/C8H8O4/c1-4-2-5(9)3-6(10)7(4)8(11)12/h2-3,9-10H,1H3,(H,11,12)","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:68072","taxon_id":"NCBITaxon:227321","taxon_label":"Aspergillus
    nidulans FGSC A4","bgc_classes":"PKS","bgc_subclasses":"Iterative type I","genome_accession":"AACD01000135.1","locus_from":"122623","locus_to":"149174","locus_evidence_methods":"Knock-out
    studies|Gene expression correlated with compound production","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:20174687","reference_basis":"ENTRY"}},{"physical_line":2640,"row_sha256":"ae96b9da832d6605dae51d18fc2524312bfeebea47576fb8f680bc0dceff6102","row":{"mibig_accession":"BGC0002212","entry_version":"3","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"Orsellinic
    acid","compound_index":"1","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","standard_inchi":"InChI=1S/C8H8O4/c1-4-2-5(9)3-6(10)7(4)8(11)12/h2-3,9-10H,1H3,(H,11,12)","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:68072","taxon_id":"NCBITaxon:1381753","taxon_label":"Moniliophthora
    roreri MCA 2997","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"AWSO01000045.1","locus_from":"179446","locus_to":"203577","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"DOI:10.1126/sciadv.aar5459","reference_basis":"COMPOUND_EVIDENCE"}},{"physical_line":3302,"row_sha256":"55d99c24b4aadad07e3503baded5592be56b432c8ce722a68240672f959140ef","row":{"mibig_accession":"BGC0002594","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"orsellinic
    acid","compound_index":"2","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","standard_inchi":"InChI=1S/C8H8O4/c1-4-2-5(9)3-6(10)7(4)8(11)12/h2-3,9-10H,1H3,(H,11,12)","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA024876","taxon_id":"NCBITaxon:229533","taxon_label":"Fusarium
    graminearum PH-1","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"CM000575.1","locus_from":"5522657","locus_to":"5554323","locus_evidence_methods":"Knock-out
    studies|Gene expression correlated with compound production","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:25011010","reference_basis":"ENTRY"}},{"physical_line":3304,"row_sha256":"19555d722d0624a85212427ba8a85ec30b7316a0fff336e6fb67745cb70b1ebc","row":{"mibig_accession":"BGC0002596","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"orsellinic
    acid","compound_index":"2","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","standard_inchi":"InChI=1S/C8H8O4/c1-4-2-5(9)3-6(10)7(4)8(11)12/h2-3,9-10H,1H3,(H,11,12)","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA024876","taxon_id":"NCBITaxon:1111077","taxon_label":"Claviceps
    purpurea 20.1","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"CAGA01000059.1","locus_from":"98653","locus_to":"131937","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:33130255","reference_basis":"ENTRY"}},{"physical_line":3435,"row_sha256":"2b40221376965d2ed836a33edc11c5ad38c441ad0e841c9de321e24e7c313274","row":{"mibig_accession":"BGC0002812","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"Orsellinic
    acid","compound_index":"7","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","standard_inchi":"InChI=1S/C8H8O4/c1-4-2-5(9)3-6(10)7(4)8(11)12/h2-3,9-10H,1H3,(H,11,12)","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"Alkylresorcinol/phloroglucinol
    polyketide","database_ids":"chembl:CHEMBL457583|pubchem:68072","taxon_id":"NCBITaxon:759273","taxon_label":"Colletotrichum
    higginsianum IMI 349063","bgc_classes":"PKS|terpene","bgc_subclasses":"Type I|Monoterpene","genome_accession":"LTAN01000004.1","locus_from":"389265","locus_to":"404974","locus_evidence_methods":"Correlation
    of genomic and metabolomic data","producer_evidence_basis":"BGC_CORRELATED","cluster_link_evidence_basis":"CLUSTER_CORRELATED","primary_reference":"DOI:10.1016/j.ymben.2023.10.002","reference_basis":"COMPOUND_EVIDENCE"}}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2214-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 1 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N"
    against the pinned chebi_structures table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned chebi_structures table;
    no query replay or external lookup.
- evidence_id: bgc-2214-source-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Physical TSV lines 8527
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":8527,"row_sha256":"173a035cad43a578645d6b1236b625acccc507cb0111d19bf903391d69c225ff","row":{"chebi_id":"CHEBI:32807","name":"o-orsellinic
    acid","definition":"A dihydroxybenzoic acid that is 2,4-dihydroxybenzoic acid
    in which the hydrogen at position 6 is replaced by a methyl group.","stars":"3","standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","smiles":"Cc1cc(O)cc(O)c1C(=O)O"}}]'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2214-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 20 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N"
    against the pinned lotus_occurrences table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned lotus_occurrences table;
    no query replay or external lookup.
- evidence_id: bgc-2214-source-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
    195, 196, 197, 198, 199, 200, 201, 202, 203
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":184,"row_sha256":"b3deb61168e1abe5276bdb464f0767dc7c23434edb0a5da512c4318e9d2c5b57","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Nidularia
    pulvinata","taxon_id":"NCBITaxon:1081941","organism_wikidata":"http://www.wikidata.org/entity/Q10600580","reference_doi":"10.1515/ZNC-1997-5-606","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":185,"row_sha256":"ec70fa6467bded35c4de11b7ab555d1e44e5fc89b8a400df958dc39d256833d1","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Hypoxylon
    rubiginosum","taxon_id":"NCBITaxon:110542","organism_wikidata":"http://www.wikidata.org/entity/Q2604190","reference_doi":"10.1021/NP040063L","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":186,"row_sha256":"2de22ab4c6f81f3cc8985855f93070223ffc649d86307a29e64d1f18a16f43bb","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus
    nidulans","taxon_id":"NCBITaxon:162425","organism_wikidata":"http://www.wikidata.org/entity/Q683881","reference_doi":"10.1073/PNAS.0901870106","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":187,"row_sha256":"cd2f201544dc1aea4019e073730ea19ffd41054b32f7a74e5b850494c63e9350","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Parmotrema
    stuppeum","taxon_id":"NCBITaxon:2041279","organism_wikidata":"http://www.wikidata.org/entity/Q10620935","reference_doi":"10.1515/ZNC-2000-11-1227","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":188,"row_sha256":"462d49e0c4924f08852c919349a62fd5f6db080191545c51be066358e7759e13","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Parmotrema
    tinctorum","taxon_id":"NCBITaxon:235862","organism_wikidata":"http://www.wikidata.org/entity/Q7139222","reference_doi":"10.4268/CJCMM20141620","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":189,"row_sha256":"986307573be1e38e9e1d855fa7514a08eae0a8f93e7623974cfd70350528aafb","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Dolichousnea
    longissima","taxon_id":"NCBITaxon:281306","organism_wikidata":"http://www.wikidata.org/entity/Q1809933","reference_doi":"10.1016/S0031-9422(00)82466-8","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":190,"row_sha256":"6f559fc187ff5eae76cbb7e881586137d96fed34c65b33d19e45ffd461a099af","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Parmotrema
    cooperi","taxon_id":"NCBITaxon:2910500","organism_wikidata":"http://www.wikidata.org/entity/Q10620728","reference_doi":"10.1007/S11426-011-4436-2","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":191,"row_sha256":"bc42a794a6e30d23483c043a9d2201199a1b8f946a96565310a824e5d688384c","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus
    terreus","taxon_id":"NCBITaxon:33178","organism_wikidata":"http://www.wikidata.org/entity/Q3798237","reference_doi":"10.1016/J.PHYTOL.2015.02.009","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":192,"row_sha256":"5f3e155398751350a1c4c63531bac900c18f9057cdc25d05a3c647c047f34ccd","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus
    terreus","taxon_id":"NCBITaxon:33178","organism_wikidata":"http://www.wikidata.org/entity/Q3798237","reference_doi":"10.1039/C39720000391","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":193,"row_sha256":"4d347b7b3ed93bb7424ae4e3529c81a11d0c4983327986ad939240b85afb1e67","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Penicillium
    aurantiogriseum","taxon_id":"NCBITaxon:36655","organism_wikidata":"http://www.wikidata.org/entity/Q7162856","reference_doi":"10.1039/C39920000646","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":194,"row_sha256":"537b06fc15be5fd9a46f8dae2bdf7c0c9f26b5891c988bde7f4952abe9f99eb8","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Chaetomium
    globosum","taxon_id":"NCBITaxon:38033","organism_wikidata":"http://www.wikidata.org/entity/Q2947551","reference_doi":"10.1021/NP058014B","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":195,"row_sha256":"7fef90c8359167d056db49bb3231f44138d71baf176061221aa4d0ea5cfc7ad6","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Umbilicaria
    torrefacta","taxon_id":"NCBITaxon:392743","organism_wikidata":"http://www.wikidata.org/entity/Q10667752","reference_doi":"10.1016/0031-9422(90)83052-3","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":196,"row_sha256":"d5ec47c15bf4c8bdd6018451f174b3b735edba90c2ce134f420d85a11998b1d8","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus
    flavus","taxon_id":"NCBITaxon:5059","organism_wikidata":"http://www.wikidata.org/entity/Q137096","reference_doi":"10.1271/BBB.63.820","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":197,"row_sha256":"9633ea56dbfefbfa94a34bb8c441372aaaacc62abe9276bb283f9be2786195d3","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Penicillium","taxon_id":"NCBITaxon:5073","organism_wikidata":"http://www.wikidata.org/entity/Q843136","reference_doi":"10.1021/NP500885F","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":198,"row_sha256":"d5fd2b719da4970b5fbd355d0767252499cb0b7a825aed616f7799f3eaecaa83","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Escherichia
    coli","taxon_id":"NCBITaxon:562","organism_wikidata":"http://www.wikidata.org/entity/Q25419","reference_doi":"10.1073/PNAS.0901870106","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":199,"row_sha256":"f7b35b2fb410d76ef3fdaf72bab88a576ae11d0151a1b78ce911c855688cd2f7","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Penicillium
    cyclopium","taxon_id":"NCBITaxon:60167","organism_wikidata":"http://www.wikidata.org/entity/Q104083838","reference_doi":"10.1039/C39920000646","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":200,"row_sha256":"30aee3451e80f774cc4dfdfc95344daccad3feeacab9a25068b178682379d692","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus
    fumigatus","taxon_id":"NCBITaxon:746128","organism_wikidata":"http://www.wikidata.org/entity/Q134359","reference_doi":"10.1042/BJ0970321","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":201,"row_sha256":"20302888b21642bf97d60b1a51da2538ded7a6a8cc680f534ef84737f0baaf0b","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus
    fumigatus","taxon_id":"NCBITaxon:746128","organism_wikidata":"http://www.wikidata.org/entity/Q134359","reference_doi":"10.1042/BJ0980353","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":202,"row_sha256":"c84916f88a343173ca081d198ac98f2256253f5d6882991c237e4f24ce2bec2d","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Aspergillus
    fumigatus","taxon_id":"NCBITaxon:746128","organism_wikidata":"http://www.wikidata.org/entity/Q134359","reference_doi":"10.1080/13693780802307720","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}},{"physical_line":203,"row_sha256":"a36bd5f89920b4f87010a1c993806ca992acec85238ef10be8ebe3bb3fa94003","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","organism_name":"Stachybotrys
    cylindrospora","taxon_id":"NCBITaxon:80386","organism_wikidata":"http://www.wikidata.org/entity/Q10676890","reference_doi":"10.1139/V93-069","structure_wikidata":"http://www.wikidata.org/entity/Q414421"}}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2214-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 0 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N"
    against the pinned cyanometdb_occurrences table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned cyanometdb_occurrences
    table; no query replay or external lookup.
- evidence_id: bgc-2214-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 1 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N"
    against the pinned npclassifier table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned npclassifier table; no
    query replay or external lookup.
- evidence_id: bgc-2214-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 69
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":69,"row_sha256":"321bb05768a1da671b40fbd28fcbe07307095196ecbbf502749bda222d706b04","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","smiles":"CC1=CC(=CC(=C1C(=O)O)O)O","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Phenolic acids (C6-C1)","class_results":"Simple
    phenolic acids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2214-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 5 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N"
    against the pinned pubchem_bioassay table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned pubchem_bioassay table;
    no query replay or external lookup.
- evidence_id: bgc-2214-source-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 170, 171, 172, 173, 174
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":170,"row_sha256":"d6cc563ddb22451204ade52699b0c8036de190d4bffa8f2bcff0863b1a6814b8","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","cid":"68072","aid":"1645883","assay_name":"Validation
    qHTS for agonist of cAMP-regulated guanine nucleotide exchange factor 3 (EPAC1)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"89.1251","target_accession":"","reference":""}},{"physical_line":171,"row_sha256":"cb9dfe913bf6fa2fe44d8219577ca7790828733624b3509be057d3b1c4b222f1","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","cid":"68072","aid":"1645883","assay_name":"Validation
    qHTS for agonist of cAMP-regulated guanine nucleotide exchange factor 3 (EPAC1)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"89.1251","target_accession":"O95398","reference":""}},{"physical_line":172,"row_sha256":"642f5ad5d982ec28086721d44c72e959cea304fd28323f435f859816628a5aa6","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","cid":"68072","aid":"2517","assay_name":"qHTS
    Assay for Inhibitors of the Human Apurinic/apyrimidinic Endonuclease 1 (APE1)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"0.0089","target_accession":"1DE9_A","reference":""}},{"physical_line":173,"row_sha256":"ae58a8414c50c9e8775b61fb47cefecbd63f503b80a15ad4e01043e93ad31157","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","cid":"68072","aid":"884","assay_name":"qHTS
    Assay for Inhibitors and Substrates of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Active","activity_name":"Potency","activity_value_um":"25.1189","target_accession":"NP_059488","reference":""}},{"physical_line":174,"row_sha256":"5310f06da0b121f76a6ba14bce0ac4b8d8dd2038c3c6e0801dda20bce406462c","row":{"standard_inchi_key":"AMKYESDOVDKZKV-UHFFFAOYSA-N","cid":"68072","aid":"885","assay_name":"qHTS
    Assay for Activators of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"25.1189","target_accession":"NP_059488","reference":""}}]'
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2214-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 0 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N"
    against the pinned bindingdb_targets table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned bindingdb_targets table;
    no query replay or external lookup.
- evidence_id: bgc-2214-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 0 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "AMKYESDOVDKZKV-UHFFFAOYSA-N"
    against the pinned antibioticmech_inchikeys table; no query replay or external
    lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "AMKYESDOVDKZKV-UHFFFAOYSA-N" against the pinned antibioticmech_inchikeys
    table; no query replay or external lookup.
- evidence_id: bgc-2214-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 2 positive placements. Exact saved predicate
    exact chebi_id from exact full-key structure rows with query ["CHEBI:32807"] against
    the pinned chebi_origins table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact chebi_id from exact full-key structure
    rows with query ["CHEBI:32807"] against the pinned chebi_origins table; no query
    replay or external lookup.
- evidence_id: bgc-2214-source-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Physical TSV lines 4699, 4700
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":4699,"row_sha256":"b7692b794d73b99dc96dc72f18a349518a1941068d14699200b3994109aa17be","row":{"chebi_id":"CHEBI:32807","species_text":"Ascomycota
    sp. Ind19F07","species_accession":"1583058","component_text":"","strain_text":"","source_accession":"25537370","comments":""}},{"physical_line":4700,"row_sha256":"d65ab4af495b8f61b7a7d5dc3eabf60e5071eb55929649b8ae466cb41a8cc15e","row":{"chebi_id":"CHEBI:32807","species_text":"Penicillium
    purpurogenum","species_accession":"28575","component_text":"mycelium","strain_text":"JS03
    21","source_accession":"21879714","comments":"Ethylacetate extract of fermentation
    broth and acetone extract of mycelia"}}]'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: bgc-2214-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/1; /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/whole_stanzas/11;
    /cached_taxonomy/whole_stanzas/20; /cached_taxonomy/whole_stanzas/22; /cached_taxonomy/whole_stanzas/25;
    /cached_taxonomy/whole_stanzas/39; /cached_taxonomy/whole_stanzas/50; /cached_taxonomy/whole_stanzas/70;
    /cached_taxonomy/whole_stanzas/92; /cached_taxonomy/whole_stanzas/104; /cached_taxonomy/whole_stanzas/105;
    /cached_taxonomy/whole_stanzas/109; /cached_taxonomy/whole_stanzas/114; /cached_taxonomy/whole_stanzas/130;
    /cached_taxonomy/whole_stanzas/142; /cached_taxonomy/whole_stanzas/143; /cached_taxonomy/whole_stanzas/152;
    /cached_taxonomy/whole_stanzas/153; /cached_taxonomy/whole_stanzas/155; /cached_taxonomy/whole_stanzas/163;
    /cached_taxonomy/whole_stanzas/166; /cached_taxonomy/whole_stanzas/173; /cached_taxonomy/whole_stanzas/180
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete personally read cached name/synonym stanzas for selected source
    taxa: [{"id":"NCBITaxon:562","physical_line":881,"complete_stanza":"[Term]\nid:
    NCBITaxon:562\nname: Escherichia coli\nsynonym: \"Bacillus coli\" EXACT []\nsynonym:
    \"Bacterium coli\" EXACT []\nsynonym: \"Bacterium coli commune\" EXACT []\nsynonym:
    \"Enterococcus coli\" EXACT []\nsynonym: \"Escherichia/Shigella coli\" EXACT []\n\n"},{"id":"NCBITaxon:5059","physical_line":7866,"complete_stanza":"[Term]\nid:
    NCBITaxon:5059\nname: Aspergillus flavus\nsynonym: \"Aspergillus flavus var. parvisclerotigenus\"
    EXACT []\nsynonym: \"Aspergillus parvisclerotigenus\" EXACT []\nsynonym: \"Petromyces
    flavus\" EXACT []\n\n"},{"id":"NCBITaxon:5073","physical_line":7923,"complete_stanza":"[Term]\nid:
    NCBITaxon:5073\nname: Penicillium\nsynonym: \"Eupenicillium\" EXACT []\n\n"},{"id":"NCBITaxon:33178","physical_line":14562,"complete_stanza":"[Term]\nid:
    NCBITaxon:33178\nname: Aspergillus terreus\nsynonym: \"Aspergillus terrestris\"
    EXACT []\n\n"},{"id":"NCBITaxon:36655","physical_line":15999,"complete_stanza":"[Term]\nid:
    NCBITaxon:36655\nname: Penicillium aurantiogriseum\n\n"},{"id":"NCBITaxon:38033","physical_line":16592,"complete_stanza":"[Term]\nid:
    NCBITaxon:38033\nname: Chaetomium globosum\nsynonym: \"Chaetomium rectum\" EXACT
    []\n\n"},{"id":"NCBITaxon:60167","physical_line":27608,"complete_stanza":"[Term]\nid:
    NCBITaxon:60167\nname: Penicillium cyclopium\nsynonym: \"Penicillium verrucosum
    var. cyclopium\" EXACT []\n\n"},{"id":"NCBITaxon:80386","physical_line":35899,"complete_stanza":"[Term]\nid:
    NCBITaxon:80386\nname: Stachybotrys cylindrospora\n\n"},{"id":"NCBITaxon:110542","physical_line":44030,"complete_stanza":"[Term]\nid:
    NCBITaxon:110542\nname: Hypoxylon rubiginosum\nsynonym: \"Sphaeria rubiginosa\"
    EXACT []\n\n"},{"id":"NCBITaxon:162425","physical_line":55539,"complete_stanza":"[Term]\nid:
    NCBITaxon:162425\nname: Aspergillus nidulans\nsynonym: \"Aspergillus nidulans
    (Eidam) G. Winter, 1884\" EXACT []\nsynonym: \"Aspergillus nidulellus\" EXACT
    []\nsynonym: \"Emericella nidulans\" EXACT []\nsynonym: \"Sterigmatocystis nidulans\"
    EXACT []\n\n"},{"id":"NCBITaxon:227321","physical_line":69073,"complete_stanza":"[Term]\nid:
    NCBITaxon:227321\nname: Aspergillus nidulans FGSC A4\nsynonym: \"Emericella nidulans
    FGSC A4\" EXACT []\n\n"},{"id":"NCBITaxon:229533","physical_line":69588,"complete_stanza":"[Term]\nid:
    NCBITaxon:229533\nname: Fusarium graminearum PH-1\nsynonym: \"Gibberella zeae
    PH-1\" EXACT []\n\n"},{"id":"NCBITaxon:235862","physical_line":70513,"complete_stanza":"[Term]\nid:
    NCBITaxon:235862\nname: Parmotrema tinctorum\nsynonym: \"Parmelia tinctorum\"
    EXACT []\nsynonym: \"Parmotrema tinctorum (Despr. ex Nyl.) Hale, 1974\" EXACT
    []\n\n"},{"id":"NCBITaxon:281306","physical_line":77060,"complete_stanza":"[Term]\nid:
    NCBITaxon:281306\nname: Dolichousnea longissima\nsynonym: \"Usnea longissima\"
    EXACT []\n\n"},{"id":"NCBITaxon:392743","physical_line":90225,"complete_stanza":"[Term]\nid:
    NCBITaxon:392743\nname: Umbilicaria torrefacta\nsynonym: \"Lichen torrefactus\"
    EXACT []\n\n"},{"id":"NCBITaxon:746128","physical_line":109335,"complete_stanza":"[Term]\nid:
    NCBITaxon:746128\nname: Aspergillus fumigatus\nsynonym: \"Aspergillus fumigatus
    Fresen., 1863\" EXACT []\nsynonym: \"Aspergillus fumigatus var. ellipticus\" EXACT
    []\nsynonym: \"Aspergillus neoellipticus\" EXACT []\nsynonym: \"Neosartorya fumigata\"
    EXACT []\nsynonym: \"Sartorya fumigata\" EXACT []\n\n"},{"id":"NCBITaxon:759273","physical_line":110037,"complete_stanza":"[Term]\nid:
    NCBITaxon:759273\nname: Colletotrichum higginsianum IMI 349063\n\n"},{"id":"NCBITaxon:1081941","physical_line":117808,"complete_stanza":"[Term]\nid:
    NCBITaxon:1081941\nname: Nidularia pulvinata\nsynonym: \"Cyathus pulvinatus\"
    EXACT []\n\n"},{"id":"NCBITaxon:1111077","physical_line":118627,"complete_stanza":"[Term]\nid:
    NCBITaxon:1111077\nname: Claviceps purpurea 20.1\n\n"},{"id":"NCBITaxon:1266744","physical_line":124644,"complete_stanza":"[Term]\nid:
    NCBITaxon:1266744\nname: Talaromyces purpureogenus\nsynonym: \"Penicillium crateriforme\"
    EXACT []\nsynonym: \"Penicillium purpureogenum Stoll, 1904\" EXACT []\nsynonym:
    \"Penicillium purpureogenum var. rubri-sclerotium\" EXACT []\nsynonym: \"Penicillium
    sanguineum\" EXACT []\n\n"},{"id":"NCBITaxon:1381753","physical_line":127759,"complete_stanza":"[Term]\nid:
    NCBITaxon:1381753\nname: Moniliophthora roreri MCA 2997\n\n"},{"id":"NCBITaxon:1583058","physical_line":133924,"complete_stanza":"[Term]\nid:
    NCBITaxon:1583058\nname: Ascomycota sp. Ind19F07\n\n"},{"id":"NCBITaxon:2041279","physical_line":143906,"complete_stanza":"[Term]\nid:
    NCBITaxon:2041279\nname: Parmotrema stuppeum\nsynonym: \"Parmelia stuppea\" EXACT
    []\n\n"},{"id":"NCBITaxon:2910500","physical_line":153767,"complete_stanza":"[Term]\nid:
    NCBITaxon:2910500\nname: Parmotrema cooperi\nsynonym: \"Parmelia cooperi\" EXACT
    []\n\n"}]. No hierarchy or fresh taxonomy verification is inferred.'
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/source_taxa; /records/3/source_scope_inventory/forward_taxon_merge_matches;
    /records/3/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Exact saved source-taxon and forward-merge/nonorganism route lists. Old
    ID 28575 forwards to 1266744; absence of its own cached stanza is not loss of
    the admitted merge route.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: bgc-2214-direct-owner-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/1/complete_raw_text; /contexts/1/complete_raw_history; /contexts/1/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion F9775A, key KEHZWGZVOZXIKE-UHFFFAOYSA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-direct-owner-1
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/2/complete_raw_text; /contexts/2/complete_raw_history; /contexts/2/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion F9775B, key ZFYMCYAXXOXUHT-UHFFFAOYSA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-direct-owner-2
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/3/complete_raw_text; /contexts/3/complete_raw_history; /contexts/3/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion o-orsellinate depside, key HEMSJKZDHNSSEW-UHFFFAOYSA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-direct-owner-3
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/10/complete_raw_text; /contexts/10/complete_raw_history; /contexts/10/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion Colletorin D acid, key FZLIGQLGBRLYQX-UHFFFAOYSA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-direct-owner-4
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/32/complete_raw_text; /contexts/32/complete_raw_history; /contexts/32/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion Colletochlorin A, key BZMLULUMBUVADU-AZWQULSGSA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-direct-owner-5
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/33/complete_raw_text; /contexts/33/complete_raw_history; /contexts/33/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion Colletochlorin B, key UEUMAXMCCDEOIJ-XYOKQWHBSA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-direct-owner-6
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/34/complete_raw_text; /contexts/34/complete_raw_history; /contexts/34/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion Colletochlorin D, key JQJZJLLBOLNQAF-UHFFFAOYSA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-direct-owner-7
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/35/complete_raw_text; /contexts/35/complete_raw_history; /contexts/35/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion Colletorin A, key QXFKEGZSZLPBGD-VZUCSPMQSA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-direct-owner-8
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/36/complete_raw_text; /contexts/36/complete_raw_history; /contexts/36/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion Colletorin B, key SXOCWLUWTFGULD-MDWZMJQESA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-direct-owner-9
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/37/complete_raw_text; /contexts/37/complete_raw_history; /contexts/37/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion Colletorin D, key ITDNZOGHXSEHSE-UHFFFAOYSA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-direct-owner-10
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /contexts/38/complete_raw_text; /contexts/38/complete_raw_history; /contexts/38/source_scope_inventory
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete directly admitted companion orcinol, key OIPPWFOQEKKFEE-UHFFFAOYSA-N,
    with its own history/source context. Reading attribution is in source notes; no
    transitive, mechanism, activity or identity transfer.
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2214-review-skill
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Workflow; Output
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Immutable claim-level review, local evidence scope, honest partial completion
    and actionable ownership.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2214-review-profile
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Complete maintained review profile
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Source qualification, producer/occurrence distinctions, computed-classification
    limits and evidence-backed issue normalization.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2214-structure-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 376–432
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Structure and stereo encoding plus explicitly computed NPClassifier fields;
    model outputs are not source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2214-activity-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 632–665; lines 920–947
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Optional observation activity_class and coarse activity buckets require
    backing; no dedicated cytotoxic or enzyme-inhibitor definition is supplied.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2214-activity-classifier
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 127–179; lines 1310–1382
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Maintained classifier unambiguity intent, generic title patterns, ACTIVE-only
    class assignment and written-observation summary derivation.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2214-definition-owner
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 985–1005
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Maintained seeder copies a unique retained ChEBI definition and its source
    identifier; a correction must preserve honest provenance.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2214-reader-DATA
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-o-orsellinic-acid-maintained-reader-DATA-001.json
  locator: /resolved_view; /raw_owner; /expected_view; /counts; /returned_view_equals_expected_complete_owner;
    /review_check_metadata
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete original maintained owner view equals the captured owner, preserving
    every graph/pathway/target/history field; no scientific evidence is upgraded by
    reader success.
  snapshot_sha256: 2b1b503a9d8c4dab14208a0768b1eae3ca55aa5adbe45be09911e4673a8425a6
- evidence_id: bgc-2214-reader-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-o-orsellinic-acid-reader-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /original_tool
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Original maintained-reader execution receipt, streams and exact invocation
    provenance.
  snapshot_sha256: 2b814b41a094a2bbbfe4c3389f0dd8337fcc6e3c5890aee128542d07b7b2c91f
- evidence_id: bgc-2214-reader-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-o-orsellinic-acid-maintained-reader-acceptance-001.json
  locator: /status; /verification; /review_check_contract
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: ROOT acceptance of exact complete-owner/positive-content equality and original
    terminal success; expected capability construction was denied before action, with
    no external request.
  snapshot_sha256: 75dfc476b45c8af74fafc68b00e597eef394596ba72e4ed0653dacd99399acfb
- evidence_id: bgc-2214-graph-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-o-orsellinic-acid-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/0
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete graph o-orsellinic-acid-orsa-biosynthesis: 4 node placements
    and 3 edges, every evidence item and limitation retained. Retained graph description:
    Partial Aspergillus nidulans o-orsellinic acid biosynthesis graph for OrsA condensation
    of acetyl-CoA and malonyl-CoA units to o-orsellinate.'
  snapshot_sha256: 2b1b503a9d8c4dab14208a0768b1eae3ca55aa5adbe45be09911e4673a8425a6
- evidence_id: bgc-2214-graph-1
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-o-orsellinic-acid-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/1
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete graph o-orsellinic-acid-asca-database-substrate-prenylation:
    4 node placements and 3 edges, every evidence item and limitation retained. Retained
    graph description: MITE-reported farnesyl-prenylation of exact o-orsellinic acid
    as substrate. AscA is the sequence-verified native Acremonium egyptiacum F-1392
    reference. This separate database context consumes the owner compound and does
    not replace its Aspergillus nidulans OrsA synthesis pathway or transfer producer
    or BGC assertions. Functional evidence remains database-level; the primary paper
    was inaccessible. Product geometry and ionic-form limits remain explicit; existing
    open discussions and SEEDED status are preserved.'
  snapshot_sha256: 2b1b503a9d8c4dab14208a0768b1eae3ca55aa5adbe45be09911e4673a8425a6
- evidence_id: bgc-2214-pathway
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-o-orsellinic-acid-maintained-reader-DATA-001.json
  locator: /resolved_view/biosynthetic_pathway
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Whole retained OrsA pathway step, exact ionic product and all four evidence
    items; no fresh reaction or protein resolution.
  snapshot_sha256: 2b1b503a9d8c4dab14208a0768b1eae3ca55aa5adbe45be09911e4673a8425a6
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
- assessment_id: bgc-2214-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: CHEBI:32807 and five MIBiG concepts join exact key AMKYESDOVDKZKV-UHFFFAOYSA-N.
    The encoded 2,4-dihydroxy-6-methylbenzoic acid matches the retained definition.
    Existing name-disagreement and shared-structure discussions remain open; source-key
    agreement does not independently settle their historical identity questions. The
    pathway's o-orsellinate product is a distinct ionic form, not a replacement owner.
  target_ids:
  - CHEBI:32807
  evidence_ids:
  - bgc-2214-owner
  - bgc-2214-capture
  - bgc-2214-intake
  - bgc-2214-grounding-owner
  - bgc-2214-source-plan
  - bgc-2214-plan-acceptance
  - bgc-2214-query-chebi_structures
  - bgc-2214-source-chebi_structures
  - bgc-2214-source-mibig_compounds
  - bgc-2214-chemistry
  - bgc-2214-direct-owner-0
  - bgc-2214-direct-owner-1
  - bgc-2214-direct-owner-2
  - bgc-2214-direct-owner-3
  - bgc-2214-direct-owner-4
  - bgc-2214-direct-owner-5
  - bgc-2214-direct-owner-6
  - bgc-2214-direct-owner-7
  - bgc-2214-direct-owner-8
  - bgc-2214-direct-owner-9
  - bgc-2214-direct-owner-10
  dimensions:
  - name: standard_inchi_key
    value: AMKYESDOVDKZKV-UHFFFAOYSA-N
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2214-owner
    - bgc-2214-capture
    - bgc-2214-intake
    - bgc-2214-grounding-owner
    - bgc-2214-source-plan
    - bgc-2214-plan-acceptance
    - bgc-2214-query-chebi_structures
    - bgc-2214-source-chebi_structures
    - bgc-2214-source-mibig_compounds
    - bgc-2214-chemistry
    - bgc-2214-direct-owner-0
    - bgc-2214-direct-owner-1
    - bgc-2214-direct-owner-2
    - bgc-2214-direct-owner-3
    - bgc-2214-direct-owner-4
    - bgc-2214-direct-owner-5
    - bgc-2214-direct-owner-6
    - bgc-2214-direct-owner-7
    - bgc-2214-direct-owner-8
    - bgc-2214-direct-owner-9
    - bgc-2214-direct-owner-10
  - name: grounding_scope
    value: Five source BGC concepts share the key; existing name/shared-structure
      discussions are not closed.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2214-owner
    - bgc-2214-capture
    - bgc-2214-intake
    - bgc-2214-grounding-owner
    - bgc-2214-source-plan
    - bgc-2214-plan-acceptance
    - bgc-2214-query-chebi_structures
    - bgc-2214-source-chebi_structures
    - bgc-2214-source-mibig_compounds
    - bgc-2214-chemistry
    - bgc-2214-direct-owner-0
    - bgc-2214-direct-owner-1
    - bgc-2214-direct-owner-2
    - bgc-2214-direct-owner-3
    - bgc-2214-direct-owner-4
    - bgc-2214-direct-owner-5
    - bgc-2214-direct-owner-6
    - bgc-2214-direct-owner-7
    - bgc-2214-direct-owner-8
    - bgc-2214-direct-owner-9
    - bgc-2214-direct-owner-10
- assessment_id: bgc-2214-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both forms give neutral C8H8O4 with 12 atoms and 12 bonds, one aromatic
    ring, a carboxylic acid, two phenolic OH groups and a methyl substituent. No potential
    stereoelement is returned. All ten comparisons are true and the saved correspondence
    is complete. This supports the stored representation while leaving full natural-identity
    verification outside the diagnostic.
  target_ids:
  - CHEBI:32807
  evidence_ids:
  - bgc-2214-chemistry
  - bgc-2214-topology
  - bgc-2214-diagnostic-acceptance
  - bgc-2214-structure-schema
  dimensions:
  - name: stereochemistry_scope
    value: No potential tetrahedral or double-bond stereoelement in either saved form.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2214-chemistry
    - bgc-2214-topology
    - bgc-2214-diagnostic-acceptance
    - bgc-2214-structure-schema
  - name: representation_correspondence
    value: Ten comparisons true; neutral carboxylic-acid owner preserved separately
      from pathway anion.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2214-chemistry
    - bgc-2214-topology
    - bgc-2214-diagnostic-acceptance
    - bgc-2214-structure-schema
- assessment_id: bgc-2214-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: BGC0000057 v5 (FGSC A4/227321) and BGC0002594 v2 (PH-1/229533) retain BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED
    from knockout and expression evidence. BGC0002812 v2 (IMI349063/759273) is BGC_CORRELATED/CLUSTER_CORRELATED.
    BGC0002212 v3 (MCA2997/1381753) and BGC0002596 v2 (20.1/1111077) remain SOURCE_ASSERTION/CLUSTER_UNSTATED.
    AscA's F-1392 reference is a substrate-consumption context and is not promoted
    into this producer list.
  target_ids:
  - CHEBI:32807
  evidence_ids:
  - bgc-2214-origin-owner
  - bgc-2214-occurrence-owner
  - bgc-2214-source-mibig_compounds
  - bgc-2214-source-lotus_occurrences
  - bgc-2214-source-chebi_origins
  - bgc-2214-cached-taxonomy
  - bgc-2214-source-routes
  - bgc-2214-review-profile
  - bgc-2214-reader-DATA
  - bgc-2214-reader-execution
  - bgc-2214-reader-acceptance
  - bgc-2214-graph-0
  - bgc-2214-graph-1
  - bgc-2214-pathway
  dimensions:
  - name: taxon_scope
    value: Five locus-specific organism scopes; occurrences and AscA substrate organism
      are separate.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2214-origin-owner
    - bgc-2214-occurrence-owner
    - bgc-2214-source-mibig_compounds
    - bgc-2214-source-lotus_occurrences
    - bgc-2214-source-chebi_origins
    - bgc-2214-cached-taxonomy
    - bgc-2214-source-routes
    - bgc-2214-review-profile
    - bgc-2214-reader-DATA
    - bgc-2214-reader-execution
    - bgc-2214-reader-acceptance
    - bgc-2214-graph-0
    - bgc-2214-graph-1
    - bgc-2214-pathway
  - name: producer_evidence
    value: Two characterized, one correlated and two source-assertion producer grades
      retained.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2214-origin-owner
    - bgc-2214-occurrence-owner
    - bgc-2214-source-mibig_compounds
    - bgc-2214-source-lotus_occurrences
    - bgc-2214-source-chebi_origins
    - bgc-2214-cached-taxonomy
    - bgc-2214-source-routes
    - bgc-2214-review-profile
    - bgc-2214-reader-DATA
    - bgc-2214-reader-execution
    - bgc-2214-reader-acceptance
    - bgc-2214-graph-0
    - bgc-2214-graph-1
    - bgc-2214-pathway
  - name: locus_evidence
    value: Two demonstrated, one correlated and two unstated locus grades; versions
      preserved.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2214-origin-owner
    - bgc-2214-occurrence-owner
    - bgc-2214-source-mibig_compounds
    - bgc-2214-source-lotus_occurrences
    - bgc-2214-source-chebi_origins
    - bgc-2214-cached-taxonomy
    - bgc-2214-source-routes
    - bgc-2214-review-profile
    - bgc-2214-reader-DATA
    - bgc-2214-reader-execution
    - bgc-2214-reader-acceptance
    - bgc-2214-graph-0
    - bgc-2214-graph-1
    - bgc-2214-pathway
- assessment_id: bgc-2214-citations
  area: evidence
  topic: Citations
  outcome: unknown
  summary: 'Imported references have distinct entry versus compound-evidence roles:
    BGC0000057/2594/2596 cite entry PMIDs 20174687/25011010/33130255; BGC0002212 cites
    DOI:10.1126/sciadv.aar5459 and 2812 DOI:10.1016/j.ymben.2023.10.002 at compound
    level. OrsA historical primary annotations and the separately database-scoped
    AscA evidence remain attributed. The AscA source''s truncated DOI and historically
    inaccessible paper are not silently resolved by this local review.'
  target_ids:
  - CHEBI:32807
  evidence_ids:
  - bgc-2214-origin-owner
  - bgc-2214-occurrence-owner
  - bgc-2214-assay-owner
  - bgc-2214-source-mibig_compounds
  - bgc-2214-source-lotus_occurrences
  - bgc-2214-source-chebi_origins
  - bgc-2214-source-pubchem_bioassay
  - bgc-2214-direct-owner-0
  - bgc-2214-direct-owner-1
  - bgc-2214-direct-owner-2
  - bgc-2214-direct-owner-3
  - bgc-2214-direct-owner-4
  - bgc-2214-direct-owner-5
  - bgc-2214-direct-owner-6
  - bgc-2214-direct-owner-7
  - bgc-2214-direct-owner-8
  - bgc-2214-direct-owner-9
  - bgc-2214-direct-owner-10
  - bgc-2214-reader-DATA
  - bgc-2214-reader-execution
  - bgc-2214-reader-acceptance
  - bgc-2214-graph-0
  - bgc-2214-graph-1
  - bgc-2214-pathway
  dimensions:
  - name: citation_scope
    value: Entry, compound-evidence, historical primary and database substrate references
      remain distinct.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2214-origin-owner
    - bgc-2214-occurrence-owner
    - bgc-2214-assay-owner
    - bgc-2214-source-mibig_compounds
    - bgc-2214-source-lotus_occurrences
    - bgc-2214-source-chebi_origins
    - bgc-2214-source-pubchem_bioassay
    - bgc-2214-direct-owner-0
    - bgc-2214-direct-owner-1
    - bgc-2214-direct-owner-2
    - bgc-2214-direct-owner-3
    - bgc-2214-direct-owner-4
    - bgc-2214-direct-owner-5
    - bgc-2214-direct-owner-6
    - bgc-2214-direct-owner-7
    - bgc-2214-direct-owner-8
    - bgc-2214-direct-owner-9
    - bgc-2214-direct-owner-10
    - bgc-2214-reader-DATA
    - bgc-2214-reader-execution
    - bgc-2214-reader-acceptance
    - bgc-2214-graph-0
    - bgc-2214-graph-1
    - bgc-2214-pathway
- assessment_id: bgc-2214-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: 'The owner writes five assay placements: two inconclusive EPAC1 rows, inactive
    APE1 and CYP3A4-activator rows, and an ACTIVE CYP3A4 inhibitors-and-substrates
    screen; it writes no activity_class or summary. Generic Potency remains OTHER,
    not IC50, and the active mixed screen is not promoted to a specific inhibitory
    mechanism. Occurrences include a retained ChEBI Penicillium purpurogenum label
    whose old taxon 28575 forwards to 1266744; the cache names Talaromyces purpureogenus.
    Source label, current cached identifier and JS03 21 context remain distinguishable.'
  target_ids:
  - CHEBI:32807
  evidence_ids:
  - bgc-2214-assay-owner
  - bgc-2214-occurrence-owner
  - bgc-2214-query-lotus_occurrences
  - bgc-2214-source-lotus_occurrences
  - bgc-2214-query-chebi_origins
  - bgc-2214-source-chebi_origins
  - bgc-2214-query-pubchem_bioassay
  - bgc-2214-source-pubchem_bioassay
  - bgc-2214-query-bindingdb_targets
  - bgc-2214-query-antibioticmech_inchikeys
  - bgc-2214-source-plan
  - bgc-2214-source-routes
  - bgc-2214-cached-taxonomy
  - bgc-2214-activity-classifier
  - bgc-2214-activity-schema
  - bgc-2214-direct-owner-0
  - bgc-2214-direct-owner-1
  - bgc-2214-direct-owner-2
  - bgc-2214-direct-owner-3
  - bgc-2214-direct-owner-4
  - bgc-2214-direct-owner-5
  - bgc-2214-direct-owner-6
  - bgc-2214-direct-owner-7
  - bgc-2214-direct-owner-8
  - bgc-2214-direct-owner-9
  - bgc-2214-direct-owner-10
  - bgc-2214-reader-DATA
  - bgc-2214-reader-execution
  - bgc-2214-reader-acceptance
  - bgc-2214-graph-0
  - bgc-2214-graph-1
  - bgc-2214-pathway
  dimensions:
  - name: occurrence_scope
    value: 20 LOTUS rows and two ChEBI-origin assertions; explicit old-ID forward
      merge, no producer upgrade.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2214-assay-owner
    - bgc-2214-occurrence-owner
    - bgc-2214-query-lotus_occurrences
    - bgc-2214-source-lotus_occurrences
    - bgc-2214-query-chebi_origins
    - bgc-2214-source-chebi_origins
    - bgc-2214-query-pubchem_bioassay
    - bgc-2214-source-pubchem_bioassay
    - bgc-2214-query-bindingdb_targets
    - bgc-2214-query-antibioticmech_inchikeys
    - bgc-2214-source-plan
    - bgc-2214-source-routes
    - bgc-2214-cached-taxonomy
    - bgc-2214-activity-classifier
    - bgc-2214-activity-schema
    - bgc-2214-direct-owner-0
    - bgc-2214-direct-owner-1
    - bgc-2214-direct-owner-2
    - bgc-2214-direct-owner-3
    - bgc-2214-direct-owner-4
    - bgc-2214-direct-owner-5
    - bgc-2214-direct-owner-6
    - bgc-2214-direct-owner-7
    - bgc-2214-direct-owner-8
    - bgc-2214-direct-owner-9
    - bgc-2214-direct-owner-10
    - bgc-2214-reader-DATA
    - bgc-2214-reader-execution
    - bgc-2214-reader-acceptance
    - bgc-2214-graph-0
    - bgc-2214-graph-1
    - bgc-2214-pathway
  - name: assay_target_scope
    value: Five written assay placements preserve inconclusive/inactive/active distinctions
      and Potency scope.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2214-assay-owner
    - bgc-2214-occurrence-owner
    - bgc-2214-query-lotus_occurrences
    - bgc-2214-source-lotus_occurrences
    - bgc-2214-query-chebi_origins
    - bgc-2214-source-chebi_origins
    - bgc-2214-query-pubchem_bioassay
    - bgc-2214-source-pubchem_bioassay
    - bgc-2214-query-bindingdb_targets
    - bgc-2214-query-antibioticmech_inchikeys
    - bgc-2214-source-plan
    - bgc-2214-source-routes
    - bgc-2214-cached-taxonomy
    - bgc-2214-activity-classifier
    - bgc-2214-activity-schema
    - bgc-2214-direct-owner-0
    - bgc-2214-direct-owner-1
    - bgc-2214-direct-owner-2
    - bgc-2214-direct-owner-3
    - bgc-2214-direct-owner-4
    - bgc-2214-direct-owner-5
    - bgc-2214-direct-owner-6
    - bgc-2214-direct-owner-7
    - bgc-2214-direct-owner-8
    - bgc-2214-direct-owner-9
    - bgc-2214-direct-owner-10
    - bgc-2214-reader-DATA
    - bgc-2214-reader-execution
    - bgc-2214-reader-acceptance
    - bgc-2214-graph-0
    - bgc-2214-graph-1
    - bgc-2214-pathway
- assessment_id: bgc-2214-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The aromatic ring bears COOH at the reference carbon, OH at positions 2
    and 4 and methyl at 6; there is no sugar or ester linkage in the neutral owner.
    The simple-phenolic-acid model label is consistent with this topology but remains
    computed. PKS and TERPENE are imported locus classifications, not proof of two
    complete production routes. Prenylated, esterified and decarboxylated direct companions
    remain distinct structures and do not donate their activities or mechanisms.
  target_ids:
  - CHEBI:32807
  evidence_ids:
  - bgc-2214-classification-owner
  - bgc-2214-source-npclassifier
  - bgc-2214-source-mibig_compounds
  - bgc-2214-chemistry
  - bgc-2214-topology
  - bgc-2214-review-profile
  - bgc-2214-direct-owner-0
  - bgc-2214-direct-owner-1
  - bgc-2214-direct-owner-2
  - bgc-2214-direct-owner-3
  - bgc-2214-direct-owner-4
  - bgc-2214-direct-owner-5
  - bgc-2214-direct-owner-6
  - bgc-2214-direct-owner-7
  - bgc-2214-direct-owner-8
  - bgc-2214-direct-owner-9
  - bgc-2214-direct-owner-10
  dimensions:
  - name: classification_applicability
    value: Simple phenolic acid topology; source locus classes and companion chemistry
      remain separate.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2214-classification-owner
    - bgc-2214-source-npclassifier
    - bgc-2214-source-mibig_compounds
    - bgc-2214-chemistry
    - bgc-2214-topology
    - bgc-2214-review-profile
    - bgc-2214-direct-owner-0
    - bgc-2214-direct-owner-1
    - bgc-2214-direct-owner-2
    - bgc-2214-direct-owner-3
    - bgc-2214-direct-owner-4
    - bgc-2214-direct-owner-5
    - bgc-2214-direct-owner-6
    - bgc-2214-direct-owner-7
    - bgc-2214-direct-owner-8
    - bgc-2214-direct-owner-9
    - bgc-2214-direct-owner-10
- assessment_id: bgc-2214-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: No supported local curation defect is established within the inspected
    scope. Complete owner/history, selected/direct source context, actual intake and
    all paired saved molecular tables were reviewed. The complete maintained reader
    result was separately accepted. Five local gates passed, while full QC, OAK and
    external primary-source/taxonomy/sequence verification remain unavailable. This
    review is partial; no source record or native curation status was changed.
  target_ids:
  - CHEBI:32807
  evidence_ids:
  - bgc-2214-owner
  - bgc-2214-intake
  - bgc-2214-intake-acceptance
  - bgc-2214-source-notes
  - bgc-2214-native-acceptance
  - bgc-2214-diagnostic-acceptance
  - bgc-2214-source-plan
  - bgc-2214-plan-acceptance
  - bgc-2214-review-skill
  - bgc-2214-review-profile
  - bgc-2214-direct-owner-0
  - bgc-2214-direct-owner-1
  - bgc-2214-direct-owner-2
  - bgc-2214-direct-owner-3
  - bgc-2214-direct-owner-4
  - bgc-2214-direct-owner-5
  - bgc-2214-direct-owner-6
  - bgc-2214-direct-owner-7
  - bgc-2214-direct-owner-8
  - bgc-2214-direct-owner-9
  - bgc-2214-direct-owner-10
  - bgc-2214-reader-DATA
  - bgc-2214-reader-execution
  - bgc-2214-reader-acceptance
  - bgc-2214-graph-0
  - bgc-2214-graph-1
  - bgc-2214-pathway
  dimensions:
  - name: review_completion
    value: Partial; qualified local result; external verification, full QC and OAK
      unavailable.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2214-owner
    - bgc-2214-intake
    - bgc-2214-intake-acceptance
    - bgc-2214-source-notes
    - bgc-2214-native-acceptance
    - bgc-2214-diagnostic-acceptance
    - bgc-2214-source-plan
    - bgc-2214-plan-acceptance
    - bgc-2214-review-skill
    - bgc-2214-review-profile
    - bgc-2214-direct-owner-0
    - bgc-2214-direct-owner-1
    - bgc-2214-direct-owner-2
    - bgc-2214-direct-owner-3
    - bgc-2214-direct-owner-4
    - bgc-2214-direct-owner-5
    - bgc-2214-direct-owner-6
    - bgc-2214-direct-owner-7
    - bgc-2214-direct-owner-8
    - bgc-2214-direct-owner-9
    - bgc-2214-direct-owner-10
    - bgc-2214-reader-DATA
    - bgc-2214-reader-execution
    - bgc-2214-reader-acceptance
    - bgc-2214-graph-0
    - bgc-2214-graph-1
    - bgc-2214-pathway
- assessment_id: bgc-2214-mechanism
  area: graph
  topic: Mechanism
  outcome: unknown
  summary: The accepted complete owner contains two graphs with eight node placements
    and six edges plus one OrsA pathway step. OrsA uses acetyl-CoA and three malonyl-CoA
    units to form the conjugate-base o-orsellinate in the retained RHEA:62973 annotation.
    The separate AscA graph consumes exact neutral owner acid in a MITE example and
    leaves its intermediate product ungrounded with unspecified geometry. It does
    not replace OrsA synthesis or transfer BGC0001923, producer status, downstream
    finality or activity from companions.
  target_ids:
  - CHEBI:32807
  evidence_ids:
  - bgc-2214-reader-DATA
  - bgc-2214-reader-execution
  - bgc-2214-reader-acceptance
  - bgc-2214-graph-0
  - bgc-2214-graph-1
  - bgc-2214-pathway
  - bgc-2214-assay-owner
  - bgc-2214-source-pubchem_bioassay
  - bgc-2214-source-mibig_compounds
  - bgc-2214-direct-owner-0
  - bgc-2214-direct-owner-1
  - bgc-2214-direct-owner-2
  - bgc-2214-direct-owner-3
  - bgc-2214-direct-owner-4
  - bgc-2214-direct-owner-5
  - bgc-2214-direct-owner-6
  - bgc-2214-direct-owner-7
  - bgc-2214-direct-owner-8
  - bgc-2214-direct-owner-9
  - bgc-2214-direct-owner-10
- assessment_id: bgc-2214-protein
  area: grounding
  topic: Protein
  outcome: unknown
  summary: OrsA Q5AUX1, EAA59563.1, AN7909.2 and the 2103-aa identity claim remain
    historical retained annotations. AscA A0A455R413/BBF25313.1 is the reported native
    336-aa F-1392 reference; the LC406756.1 reverse-CDS equality claim is not newly
    recomputed here. Database function and sequence correspondence do not identify
    the historical assay construct. Mg2+ is explicitly by similarity; no measured
    occupancy, localization, kinetics or physical complex is inferred.
  target_ids:
  - CHEBI:32807
  evidence_ids:
  - bgc-2214-reader-DATA
  - bgc-2214-reader-execution
  - bgc-2214-reader-acceptance
  - bgc-2214-graph-0
  - bgc-2214-graph-1
  - bgc-2214-pathway
  - bgc-2214-source-pubchem_bioassay
  - bgc-2214-origin-owner
findings: []
actions: []
limitations:
- External compound/taxon/protein/accession and primary-paper verification was unavailable
  under the absolute local-only restriction; retained historical claims are attributed,
  not refreshed.
- Full QC and OAK were unavailable. Successful local gates, parsing and maintained-reader
  checks establish their declared mechanical scope only.
- Source-query results are bounded by exact full-key/direct-owned-BGC/source-taxon
  predicates and the saved cohort; negative joins are not global absence claims.
- No additional molecular or YAML parse was performed during fragment authoring. Source
  records, raw snapshots, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Source reading uses the complete selected payloads and explicit complementary/direct-context
  attribution in pinned notes. All first-five paired molecular tables and selected
  owner histories were personally read.
- Four diagnostic warnings remain global and unassigned; no per-record warning inference.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-222
```
