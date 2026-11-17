# Local evidence review: naringenin

- Review: 20261103T123413Z-naringenin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T12:06:20.516813Z
- Finished UTC: 2026-11-03T12:34:13.213455Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Naringenin retains a coherent but stereochemically unspecified flavanone representation. The local review identifies a wrong hydroxyl locant in its retained definition and unsupported cytotoxic typing of its aromatase assay. All source quantities and curated target evidence remain unchanged; external verification is unavailable.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2211; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:50202 | data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml | generated | naringenin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for naringenin | passed | True | CHEBI:50202 | Complete original offline maintained owner view accepted: 2 graphs, 8 node placements and 6 edges; source support remains separately assessed. |
| strict_ten | passed | True | CHEBI:50202 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:50202 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:50202 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:50202 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:50202 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:50202 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:50202 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:50202 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: concern. Targets: CHEBI:50202.

The complete key FTVWIRXFELQLPI-UHFFFAOYSA-N joins MIBiG BGC0001310 v5 and the retained three-star CHEBI:50202 row. Both stored forms and that row encode 5,7,4′-trihydroxyflavanone, but the owner and retained definition say 5,6,4′. This is a supported definition–structure conflict, not evidence that the stored structure should be replaced. No enantiomer-specific natural identity is established.

### Representation

representation: supported. Targets: CHEBI:50202.

Both saved forms give neutral C15H12O5, 20 atoms and 22 bonds; all ten comparisons are true and the saved atom correspondence is complete. The tetrahedral C2 centre is unspecified in both forms, consistent with stereo_complete=false. The diagnostic explicitly does not establish full graph or natural identity; neither the key nor generic name selects an enantiomer.

### Origin

provenance: supported. Targets: CHEBI:50202.

The imported BGC0001310 v5 producer is SOURCE_ASSERTION and its locus CLUSTER_UNSTATED, with no stated locus method. The label includes ATCC 27064, while taxon 1901 is the cached Streptomyces clavuligerus species concept; the strain wording is not a separate verified strain identity. The many plant/fungal occurrence assertions remain distinct from this bacterial producer claim and from one another.

### Citations

evidence: unknown. Targets: CHEBI:50202.

PMID:26553209 is the imported MIBiG entry reference. The carbonic-anhydrase graph cites DOI:10.3109/14756366.2011.651464 and the aromatase graph DOI:10.1111/j.1747-0285.2012.01439.x; their PRIMARY_EXPERIMENT labels are retained historical annotations, not newly inspected papers. BindingDB-deposited PubChem and BindingDB target rows share publications and may describe the same experiments. Repeated LOTUS taxa/citations are not independent confirmations.

### Bioactivity

evidence: concern. Targets: CHEBI:50202.

The owner writes 25 of 44 retained assay placements and 25 occurrences with an explicit 51-further-occurrence note. Nine BindingDB targets are separately retained. Written assay[2], AID1799798, is an ACTIVE aromatase Ki of 1.09662e−06 µM, yet it is typed CYTOTOXIC from cancer wording in the article title. That class and its sole written summary backing lack a cytotoxic measurement. Preserve the exact value, qualifier and overlapping 0.00109662 nM target/graph assertion; its surprising magnitude is not a licence to repair it by intuition. Five carbonic-anhydrase assays separately support ENZYME_INHIBITOR.

### Classification

consistency: supported. Targets: CHEBI:50202.

The complete tables show a flavanone carbonyl, one heterocyclic ether and three phenolic OH groups, without a sugar ring. For SMILES atom indices, O1=2, C2=1, C3=0, C4=9 and C4a=8; the fused aromatic path is C5=7 bearing O11, C6=6 bearing H, C7=5 bearing O12, C8=4 bearing H, C8a=3. The pendant-ring para carbon 16 bears O19. Thus the OH locants are 5,7,4′. NPClassifier Flavanones and non-glycoside output are model predictions assessed against this topology, not experimental origin evidence.

### Completion

completeness: concern. Targets: CHEBI:50202.

Supported local curation findings remain open; the scientific verdict is needs_curation. Complete owner/history, selected/direct source context, actual intake and all paired saved molecular tables were reviewed. The complete maintained reader result was separately accepted. Five local gates passed, while full QC, OAK and external primary-source/taxonomy/sequence verification remain unavailable. This review is partial; no source record or native curation status was changed.

### Mechanism

graph: unknown. Targets: CHEBI:50202.

The complete maintained view preserves two bioactivity graphs with eight node placements, six edges and nine molecular targets, without components or biosynthetic steps. Five edges retain isoenzyme-specific carbonic-anhydrase inhibition and one retains the aromatase claim. These local source assertions do not establish an entire therapeutic mechanism, cellular cytotoxicity, a natural enantiomer, or independent experiments for overlapping database rows. No graph is treated as fresh primary-source verification.

### Protein

grounding: unknown. Targets: CHEBI:50202.

The five carbonic-anhydrase examples distinguish human P00915/P00918/P22748/P23280 from bovine Q3SZX4. Aromatase P11511 is human; the other target entries retain guinea-pig H9TB17 and human estrogen-receptor P03372/Q92731 scopes. Their BINDS relations and Ki/IC50 measurements are source-specific; no current sequence, construct, isoform or species transfer was verified. The historical accession-resolution statements remain attributed.

## Findings

### bgc-2211-definition-locants: Retained definition gives the wrong A-ring hydroxyl locant

major / open / confirmed; issue key: naringenin-definition-hydroxyl-locants-5-6-versus-5-7.

The owner and retained CHEBI:50202 physical row13755 define hydroxy substitution at5,6,4′, but both stored forms and the same source row's structure encode5,7,4′. Indexed SMILES C4=9/C4a=8 fixes aromatic positions C5=7(OH11), C6=6(H), C7=5(OH12), C8=4(H), C8a=3; pendant para C16 bears OH19. Thus the wording describes a different positional isomer. The seeder faithfully copies this source definition, so correcting prose must not falsely present a curator correction as an unchanged source quotation or alter the correct stored structure.

Disposition: Confirmed local evidence conflict, not an inference from unavailable external verification. Native found no same-owner prior issue_key in the declared ignored-inclusive saved-review scopes.

### bgc-2211-aromatase-cytotoxic-class: Aromatase Ki assay is unsupported as cytotoxic evidence

major / open / confirmed; issue key: naringenin-aromatase-ki-cytotoxic-class-overstatement.

Written bioactivities[2], AID1799798, joins PubChem row1623 and reports ACTIVE aromatase Ki1.09662e−06µM against P11511. Cancer wording in the cited article title triggers CYTOTOXIC although the retained observation measures aromatase activity, not cytotoxicity. This is the sole written CYTOTOXIC summary backing. The corresponding BindingDB/graph value0.00109662nM is numerically consistent and may represent the same experiment; its extreme magnitude is not independently verified or corrected. The five carbonic-anhydrase assays separately retain ENZYME_INHIBITOR support.

Disposition: Confirmed local evidence conflict, not an inference from unavailable external verification. Native found no same-owner prior issue_key in the declared ignored-inclusive saved-review scopes.

## Recommended Actions And Acceptance Checks

### bgc-2211-repair-definition-locants

Provide a narrowly scoped maintained definition correction or an explicit provenance-preserving conflict/omission route for this exact source concept and structure. If curator-corrected prose is emitted, describe5,7,4′ substitution and distinguish its provenance from the retained source's5,6,4′ wording. Preserve the original source snapshot, current structural strings/key and unspecified C2 stereochemistry. Do not use reserved decisions.tsv or edit only the generated YAML.

- Preserve exact structure, source identifiers, raw source provenance and unaffected claims.
- Regression coverage reproduces the precise evidence boundary and retains original calls, endpoint spelling, values, units, targets and references.
- After authorized implementation, regenerate through maintained code and pass the required validation, reproduction and review gates.

### bgc-2211-repair-aromatase-cytotoxic-class

Narrow maintained classification for exact AID1799798/title so article-topic cancer wording does not assert CYTOTOXIC without an appropriate measured endpoint. Omit that optional class unless separately supported; preserve ACTIVE, KI, exact1.09662e−06µM, P11511, PMID22726671 and the existing target/graph quantity and qualifier. Recompute the summary: its CYTOTOXIC backing needs correction, while the five written carbonic-anhydrase assays preserve ENZYME_INHIBITOR. Do not infer a lack of biological cytotoxicity, change units by intuition or count overlapping databases as independent experiments.

- Preserve exact structure, source identifiers, raw source provenance and unaffected claims.
- Regression coverage reproduces the precise evidence boundary and retains original calls, endpoint spelling, values, units, targets and references.
- After authorized implementation, regenerate through maintained code and pass the required validation, reproduction and review gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2211-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml; Whole owner plaintext and complete curation_history | supports | Complete owner plaintext and its full append-only curation history, read from this exact saved raw file. |
| bgc-2211-capture | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/0/owner_pin; /records/0/owner_document | supports | Complete captured owner for order 2211, with all native source fields, mechanism roots and history preserved. |
| bgc-2211-intake | /private/tmp/npm-review-work/shared-next-batch222/intakes/2211-inspect-001.json; /source; /targets | supports | Actual canonical intake source identity and complete ordered input/target scope. |
| bgc-2211-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-intake-ready-001.json; /status | supports | ROOT acceptance of the original ten canonical intakes; no replay. |
| bgc-2211-grounding-owner | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status; /records/0/owner_document/definition; /records/0/owner_document/definition_source | supports | Written structure, source concepts and grounding status; no external identity refresh. |
| bgc-2211-origin-owner | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters | supports | Complete written producer and locus claims, including versions, evidence methods, grades and citation roles. |
| bgc-2211-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/0/owner_document/occurrences | supports | Complete written occurrences and their source labels, citations and scope notes. |
| bgc-2211-assay-owner | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/0/owner_document | supports | Complete captured owner supports its written assay, target, summary and mechanism fields or their absence; this evidence does not assert omitted source-query content. |
| bgc-2211-classification-owner | /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json; /records/0/owner_document/np_classification; /records/0/owner_document/bgc_class | supports | Written named-model prediction and source BGC classes, retained as separate axes. |
| bgc-2211-source-plan | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0 | supports | Complete selected source context, direct companion paths and exact proposed map, later joined to actual intake. |
| bgc-2211-source-notes | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-scope-notes-001.json; /reading; /cautions; /curation | supports | Whole source-reading attribution, precise direct-context limits and bounded eight-table curation scan; complementary reading is explicitly attributed. |
| bgc-2211-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-target-input-plan-acceptance-001.json; /status; /plan; /inventory; /source_notes; /per_order | supports | ROOT accepted original input plan and retained inventory/notes provenance with exact per-order counts. |
| bgc-2211-chemistry | /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/comparisons; /records/0/smiles; /records/0/inchi; /records/0/atom_correspondence | supports | Both complete saved molecular profiles, all atom/bond/stereo/motif fields and literal comparison/mapping results; no new molecular parse. |
| bgc-2211-topology | /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds; /records/0/smiles/computed/rings; /records/0/smiles/computed/motifs; /records/0/smiles/computed/potential_stereo; /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings; /records/0/inchi/computed/motifs; /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/stereo_counts; /records/0/atom_correspondence; /records/0/declared_structure | supports | Complete indexed local topology and stereochemistry in both saved forms. Motifs are bounded structural patterns, not residue, natural-identity or experimental assignments. |
| bgc-2211-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-chemistry-acceptance-001.json; /status; /DATA; /execution; /false_comparisons; /warning_scope | supports | ROOT accepted the original twenty-form diagnostic; four global warnings are unassigned and no scientific identity verdict is implied. |
| bgc-2211-native-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-native-gates-acceptance-001.json; /status; /local_commands_passed; /selected_queue_rows; /unavailable_required_gates | supports | Five original local gates passed. Selected queue flags retain their literal scope; full QC and OAK remain unavailable. |
| bgc-2211-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0/source_scope_inventory/joins/mibig_compounds | supports | Complete saved query frame with 1 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned mibig_compounds table; no query replay or external lookup. |
| bgc-2211-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 1541 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":1541,"row_sha256":"fcf3412f0f632ad483e0f532e87407dcf907280c59f473e08c6f30ebb27ae506","row":{"mibig_accession":"BGC0001310","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"naringenin","compound_index":"1","smiles":"C1C(OC2=CC(=CC(=C2C1=O)O)O)C3=CC=C(C=C3)O","standard_inchi":"InChI=1S/C15H12O5/c16-9-3-1-8(2-4-9)13-7-12(19)15-11(18)5-10(17)6-14(15)20-13/h1-6,13,16-18H,7H2","standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","stereo_complete":"false","compound_classes":"","database_ids":"pubchem:932","taxon_id":"NCBITaxon:1901","taxon_label":"Streptomyces clavuligerus ATCC 27064","bgc_classes":"PKS","bgc_subclasses":"Type III","genome_accession":"CM000913.1","locus_from":"6460418","locus_to":"6463122","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:26553209","reference_basis":"ENTRY"}}] |
| bgc-2211-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0/source_scope_inventory/joins/chebi_structures | supports | Complete saved query frame with 1 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned chebi_structures table; no query replay or external lookup. |
| bgc-2211-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Physical TSV lines 13755 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":13755,"row_sha256":"641bd42fb52cc5259e7a33ca354de6bca252f99fbf01fdce9bec007bec7bfbb3","row":{"chebi_id":"CHEBI:50202","name":"naringenin","definition":"A trihydroxyflavanone that is flavanone substituted by hydroxy groups at positions 5, 6 and 4'.","stars":"3","standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","smiles":"O=C1CC(c2ccc(O)cc2)Oc2cc(O)cc(O)c21"}}] |
| bgc-2211-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved query frame with 80 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned lotus_occurrences table; no query replay or external lookup. |
| bgc-2211-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":1561,"row_sha256":"b39d50a6cae38194fa823713b53b16c75f339d82af8d9f5dcb733fb703d5ac94","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus mume","taxon_id":"NCBITaxon:102107","organism_wikidata":"http://www.wikidata.org/entity/Q157763","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1562,"row_sha256":"1b6d11f9332797485a3f3f76578dd124db46e0530f374fe3b484c17ef54dc437","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum cephaloideum","taxon_id":"NCBITaxon:112358","organism_wikidata":"http://www.wikidata.org/entity/Q15578590","reference_doi":"10.1002/CBER.19731060432","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1563,"row_sha256":"3bb72bdabae82449b27045185b81d71b85d9f42a8199980c955f3a417b97fc79","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum cephaloideum","taxon_id":"NCBITaxon:112358","organism_wikidata":"http://www.wikidata.org/entity/Q15578590","reference_doi":"10.1515/ZNC-1983-11-1201","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1564,"row_sha256":"855f49511a01e3cbfdf01094fe992f930ba8d16ca4e90c5863f8b0f9997c1e70","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium fimbriatum","taxon_id":"NCBITaxon:117953","organism_wikidata":"http://www.wikidata.org/entity/Q7990065","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1565,"row_sha256":"27ab3c97e92e67751fe5fc340ee6b35e5eb828d3dc3aa876e218c7050f51fa8a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium loddigesii","taxon_id":"NCBITaxon:117954","organism_wikidata":"http://www.wikidata.org/entity/Q5220983","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1566,"row_sha256":"03cd6552cd3700044c87275867ac15424b32adbb530c3b09efd1ce666579d5d5","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus lycioides","taxon_id":"NCBITaxon:1284230","organism_wikidata":"http://www.wikidata.org/entity/Q17271747","reference_doi":"10.3390/MOLECULES17021665","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1567,"row_sha256":"d8fdec729ebd61fae6d69bd4ba5bc619303cbfe10697fb7c6aaa2b6a4e4538a8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dalbergia parviflora","taxon_id":"NCBITaxon:1353466","organism_wikidata":"http://www.wikidata.org/entity/Q15531989","reference_doi":"10.1039/P19730001737","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1568,"row_sha256":"dd6d4071c1f91c448a2b980a9c60507a6214d2175f54936f40c9b4434c2288c7","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus campanulata","taxon_id":"NCBITaxon:136465","organism_wikidata":"http://www.wikidata.org/entity/Q149633","reference_doi":"10.1021/JA01650A088","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1569,"row_sha256":"8efa39cfb904fefb646c07b34629c82bdd429d4556859b8279df52ecc3cd6b27","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Rhynchosia beddomei","taxon_id":"NCBITaxon:1378005","organism_wikidata":"http://www.wikidata.org/entity/Q15532686","reference_doi":"10.1016/0031-9422(80)83211-0","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1570,"row_sha256":"46e4213995dc06c8517a7b9fccc35552d83963fa0f322a75e5f16455eb939bc9","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium moniliforme","taxon_id":"NCBITaxon:142614","organism_wikidata":"http://www.wikidata.org/entity/Q163663","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1571,"row_sha256":"33102310498e03aa1cdced6df029450c414e24d78fe0c05c6c4fdeb322fc4c9b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium officinale","taxon_id":"NCBITaxon:142615","organism_wikidata":"http://www.wikidata.org/entity/Q50839974","reference_doi":"10.1155/2017/7436259","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1572,"row_sha256":"5688a5bb003d9913aaf8385fac8b1be7f5a8a2f04e9d4a32a89e14ac48fca3bf","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus davidiana","taxon_id":"NCBITaxon:151430","organism_wikidata":"http://www.wikidata.org/entity/Q3408638","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1573,"row_sha256":"b0608830c24c71143a9b8d3764b7269640b401508505adcade6490fa79c5cf19","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium chrysanthum","taxon_id":"NCBITaxon:154291","organism_wikidata":"http://www.wikidata.org/entity/Q5223343","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1574,"row_sha256":"b00c33cb3ff4b5347737d993b8ec5045ea484dbf1dab2d10fc0a0559e84902da","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium chrysotoxum","taxon_id":"NCBITaxon:161865","organism_wikidata":"http://www.wikidata.org/entity/Q3335823","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1575,"row_sha256":"f9f46c0c29dd8688fbf04444a372ffd919d314bee6123afcbc230291e3b9d327","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Intsia","taxon_id":"NCBITaxon:162811","organism_wikidata":"http://www.wikidata.org/entity/Q631100","reference_doi":"10.1016/0031-9422(73)80461-3","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1576,"row_sha256":"a1c8cc3085cfaed452f0aaecc888814b8a39b15e4e75fb45b047bd676d694cfd","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Brosimum acutifolium","taxon_id":"NCBITaxon:1835378","organism_wikidata":"http://www.wikidata.org/entity/Q15471077","reference_doi":"10.1021/NP010389J","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1577,"row_sha256":"35b222b79f86bf5ad0dfd3958922f3000f35a79aed66970dd4c6731105f1389f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Streptomyces clavuligerus","taxon_id":"NCBITaxon:1901","organism_wikidata":"http://www.wikidata.org/entity/Q7623381","reference_doi":"10.1186/S12934-015-0373-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1578,"row_sha256":"2fd0a0c0db35b8d41cd014dcf0bb961d949ea4d9b5a3de1063cf38e4a46e4f66","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Maclura cochinchinensis","taxon_id":"NCBITaxon:194324","organism_wikidata":"http://www.wikidata.org/entity/Q5402484","reference_doi":"10.1021/NP030127C","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1579,"row_sha256":"0849bd9c941a5202bab2790442eafceda37f8cb307c3125712727d4b42ffa7f7","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Maclura tricuspidata","taxon_id":"NCBITaxon:210328","organism_wikidata":"http://www.wikidata.org/entity/Q602322","reference_doi":"10.1016/0031-9422(95)00277-E","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1580,"row_sha256":"980b22c1c4047bb5f2c94015e0af2850d6ec71064cb438f53e68227fab6e5428","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Maclura tricuspidata","taxon_id":"NCBITaxon:210328","organism_wikidata":"http://www.wikidata.org/entity/Q602322","reference_doi":"10.1021/NP030127C","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1581,"row_sha256":"dcb72d18546c5712edc231de8790d683f3937acb644d557d524eeff22ee761eb","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium longicornu","taxon_id":"NCBITaxon:257357","organism_wikidata":"http://www.wikidata.org/entity/Q5224593","reference_doi":"10.1055/S-2008-1074492","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1582,"row_sha256":"1070ff82dd7c43a4eafc648a34b72bfca8c5f7faa947f5d337b111b7cc6ef9cb","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium trigonopus","taxon_id":"NCBITaxon:257360","organism_wikidata":"http://www.wikidata.org/entity/Q4037209","reference_doi":"10.1080/10286020802133605","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1583,"row_sha256":"01b039f783761a1258b66cb47f3d53c1bce3427b4fd3ecad1a960afc1fe16456","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum arenarium","taxon_id":"NCBITaxon:261776","organism_wikidata":"http://www.wikidata.org/entity/Q27984","reference_doi":"10.1002/CBER.19731060432","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1584,"row_sha256":"edb107c598ed9e7ac0ccefe5fa1a8182dba49df7b3f48fac928b895de17c3de4","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum arenarium","taxon_id":"NCBITaxon:261776","organism_wikidata":"http://www.wikidata.org/entity/Q27984","reference_doi":"10.1515/ZNC-1983-11-1201","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1585,"row_sha256":"2dcaa8d9c862c4a5da759be7ad6dcdd8a4cac10c5a68d9849739b9aa43ab6884","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Ageratina havanensis","taxon_id":"NCBITaxon:2773069","organism_wikidata":"http://www.wikidata.org/entity/Q4692124","reference_doi":"10.1021/NP50048A063","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1586,"row_sha256":"740a840da2dde1d7e671f6cbaacb4c35429fa9b0c8553c9c7e2478e551a58e25","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Senecio adenophyllus","taxon_id":"NCBITaxon:2841764","organism_wikidata":"http://www.wikidata.org/entity/Q15588331","reference_doi":"10.1016/0031-9422(77)83033-1","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1587,"row_sha256":"1775739e27c72cebe32606bd80ed26fb1d19893c477316ad549496183552d6d7","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Daphne aurantiaca","taxon_id":"NCBITaxon:2918710","organism_wikidata":"http://www.wikidata.org/entity/Q11122021","reference_doi":"10.1248/CPB.59.653","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1588,"row_sha256":"944187ac1f75eb0c960ba1d323efe556e031daa3094424b053f19ee1da87215d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus itosakura","taxon_id":"NCBITaxon:2986971","organism_wikidata":"http://www.wikidata.org/entity/Q51117378","reference_doi":"10.1021/JA01564A056","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1589,"row_sha256":"ae91be770f8ba90c45f722e82ae9a2722cb54153ddacdd2a23f870be3d6fb5f6","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Euphorbia hirta","taxon_id":"NCBITaxon:318062","organism_wikidata":"http://www.wikidata.org/entity/Q36177","reference_doi":"10.1248/CPB.54.1037","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1590,"row_sha256":"f5410fc7868cff75f1a2962758d1e6ad8eada122a8639ebe0c520bdfd2bc80d8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Aloe barbadensis","taxon_id":"NCBITaxon:34199","organism_wikidata":"http://www.wikidata.org/entity/Q50826551","reference_doi":"10.1007/S11130-020-00822-2","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1591,"row_sha256":"9fa5025709cfa74548b59c7a1e642aee2827e158c99d25facbe05a99e0a6a4c1","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Aloe vera","taxon_id":"NCBITaxon:34199","organism_wikidata":"http://www.wikidata.org/entity/Q80079","reference_doi":"10.1007/S11130-020-00822-2","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1592,"row_sha256":"b2498b54d18aa9709076702de82ad857c3a8c9fbdf3220c1f854cef6048421e4","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Centaurea pallescens","taxon_id":"NCBITaxon:363441","organism_wikidata":"http://www.wikidata.org/entity/Q15569632","reference_doi":"10.1016/S0031-9422(00)85282-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1593,"row_sha256":"5bc08152c98e79f8104d964ec04c15f8f3f630ca76b500b581268fd61ee8ce43","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus grandis","taxon_id":"NCBITaxon:37334","organism_wikidata":"http://www.wikidata.org/entity/Q21004587","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1594,"row_sha256":"5c3b9a131a3197b6dc1ce5057c8a2d6a44cf2696986704c51758613ab12c5341","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus maxima","taxon_id":"NCBITaxon:37334","organism_wikidata":"http://www.wikidata.org/entity/Q80024","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1595,"row_sha256":"b5a2255d47caa24ca4790826945026ffdf21ec98f71eb84739379daa44e40ba3","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus grandis","taxon_id":"NCBITaxon:37334","organism_wikidata":"http://www.wikidata.org/entity/Q21004587","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1596,"row_sha256":"57f293cd4198ad0a214f5a66496c9cee2cc68d7c66a32a6b62a02e4d630a6d85","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus maxima","taxon_id":"NCBITaxon:37334","organism_wikidata":"http://www.wikidata.org/entity/Q80024","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1597,"row_sha256":"057dd0131b1a56c03ae9d29c8c7cc946dceefc90e7deb3596e2fe0ed1a8777f4","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus persica","taxon_id":"NCBITaxon:3760","organism_wikidata":"http://www.wikidata.org/entity/Q13189","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1598,"row_sha256":"a24a5259624d3f7045cd30aaa4c806a744ebe5915543b9d1b6bee99d9265c0a8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Poncirus trifoliata","taxon_id":"NCBITaxon:37690","organism_wikidata":"http://www.wikidata.org/entity/Q859433","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1599,"row_sha256":"fd6e307fc453865821a0cb2b3b23f2bc15488792818d575d6ec201bd6cdbe19b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Poncirus trifoliata","taxon_id":"NCBITaxon:37690","organism_wikidata":"http://www.wikidata.org/entity/Q859433","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1600,"row_sha256":"6fcf8f05240169fe210df574ed6e78f340cfeaf70dfd8178b0ea51bccaae59cc","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Centaurea hyalolepis","taxon_id":"NCBITaxon:3769976","organism_wikidata":"http://www.wikidata.org/entity/Q1053486","reference_doi":"10.1016/S0031-9422(00)85282-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1601,"row_sha256":"733cc27a5ba77d4e765821ed6d8da2e00d67e47d9434ec9a6fd83b5949a66221","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Euphorbia amygdaloides","taxon_id":"NCBITaxon:38843","organism_wikidata":"http://www.wikidata.org/entity/Q149367","reference_doi":"10.1248/CPB.54.1037","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1602,"row_sha256":"d71d34f68e8295ee9a5f24f066c2414481bf5ff85108b1fadf9802d244630be0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Vigna angularis","taxon_id":"NCBITaxon:3914","organism_wikidata":"http://www.wikidata.org/entity/Q380279","reference_doi":"10.1080/00021369.1987.10868021","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1603,"row_sha256":"4fbc39f0b90c021e530ee958c39aec9bc3519c5541cafbfb53b9ce2c3a4e69d8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Centaurea","taxon_id":"NCBITaxon:41503","organism_wikidata":"http://www.wikidata.org/entity/Q156414","reference_doi":"10.1002/CBER.19731060707","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1604,"row_sha256":"14cb307e681be74ab3103632936fe9b6020df7b3fa7baea3b5e7b95114392ae2","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Centaurea calcitrapa","taxon_id":"NCBITaxon:41511","organism_wikidata":"http://www.wikidata.org/entity/Q1763537","reference_doi":"10.1016/S0031-9422(00)85282-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1605,"row_sha256":"9db73d48b222b6f7ff6075ad24304f0e9f5559f14ba74aad2353abd5934c4ae2","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Chrysanthemum morifolium","taxon_id":"NCBITaxon:41568","organism_wikidata":"http://www.wikidata.org/entity/Q15530181","reference_doi":"10.1002/CBER.19731061202","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1606,"row_sha256":"a202e536b94fc17a3c43816899586d6f4cffdafd991f096961762aebaec045cf","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Chrysanthemum morifolium","taxon_id":"NCBITaxon:41568","organism_wikidata":"http://www.wikidata.org/entity/Q15530181","reference_doi":"10.1016/0031-9422(77)83035-5","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1607,"row_sha256":"3dfce4f409d6890130485621bc39befeb96bd8470f622fa00a62f4bd8798dcd6","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus avium","taxon_id":"NCBITaxon:42229","organism_wikidata":"http://www.wikidata.org/entity/Q165137","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1608,"row_sha256":"460848d1526bbb35651db465c57b6b4a9a275eb504308fdd4e6f825c0366e8c9","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium candidum","taxon_id":"NCBITaxon:431188","organism_wikidata":"http://www.wikidata.org/entity/Q104908039","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1609,"row_sha256":"5c824489994c5bea191aef6c636430c49d900bf37355cd0e087042c49643567d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Xanthorrhoea preissii","taxon_id":"NCBITaxon:470286","organism_wikidata":"http://www.wikidata.org/entity/Q8043105","reference_doi":"10.1071/CH9740331","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1610,"row_sha256":"4c1ed6040d1fae29e27e7d3afb3ad98e984a100899eca25f468d9aab10254e11","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Smilax china","taxon_id":"NCBITaxon:49657","organism_wikidata":"http://www.wikidata.org/entity/Q163095","reference_doi":"10.1016/J.PHYTOCHEM.2008.01.002","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1611,"row_sha256":"8c67a3386bc3235c70a9b5f0faca187230bc4222c4e34f7e6021f58b05d84d07","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Xanthorrhoea resinosa","taxon_id":"NCBITaxon:49740","organism_wikidata":"http://www.wikidata.org/entity/Q8043107","reference_doi":"10.1071/CH9740331","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1612,"row_sha256":"586f722e6f9d24922d49393e0111e655bb29275ffba50cc6df93f5808460907d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dalbergia odorifera","taxon_id":"NCBITaxon:499988","organism_wikidata":"http://www.wikidata.org/entity/Q3012291","reference_doi":"10.1039/P19730001737","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1613,"row_sha256":"9f7115afc1d3891c07d2ef98bd3b534604d8f2ba58a09e27e78249e7da02451c","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus unshiu","taxon_id":"NCBITaxon:55188","organism_wikidata":"http://www.wikidata.org/entity/Q875262","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1614,"row_sha256":"8a95e3ad0d734cfc6f86e0ef07ba54af93edab17bd3afeb724292e9b92c92579","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus unshiu","taxon_id":"NCBITaxon:55188","organism_wikidata":"http://www.wikidata.org/entity/Q875262","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1615,"row_sha256":"4fda03fec348c307cd6ffe034cdc094445cf3452deb971f8032c7d911a0748bc","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus deliciosa","taxon_id":"NCBITaxon:558547","organism_wikidata":"http://www.wikidata.org/entity/Q20686225","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1616,"row_sha256":"111161d64f1a7fe1dea781b7d510f8a77d642fa0963599614e3ab8b18d566b20","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus deliciosa","taxon_id":"NCBITaxon:558547","organism_wikidata":"http://www.wikidata.org/entity/Q20686225","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1617,"row_sha256":"de694043fd646b346df585c5948c5d92507d252255145817df99f5a9c3af8cfc","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Phyllanthus","taxon_id":"NCBITaxon:58880","organism_wikidata":"http://www.wikidata.org/entity/Q310927","reference_doi":"10.1248/CPB.50.841","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1618,"row_sha256":"0e727e3900c28b5e05f7692f1db13d44686bb57265505375476503d1d2a794c0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum graveolens","taxon_id":"NCBITaxon:630307","organism_wikidata":"http://www.wikidata.org/entity/Q4085815","reference_doi":"10.1002/CBER.19731060432","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1619,"row_sha256":"62db8827dd6219994b23cec9f9fea1283dbcb745c61c3e39f2f63a14d0377f73","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum graveolens","taxon_id":"NCBITaxon:630307","organism_wikidata":"http://www.wikidata.org/entity/Q4085815","reference_doi":"10.1515/ZNC-1983-11-1201","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1620,"row_sha256":"18804c8486cde4454c8f969cbd027781b5a574c5c4ada1bc59d91a0d04ca674a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Broussonetia","taxon_id":"NCBITaxon:66379","organism_wikidata":"http://www.wikidata.org/entity/Q600114","reference_doi":"10.1021/NP010288L","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1621,"row_sha256":"3ebbadb567e29022911d180e3f5b0a7d421fffd47a3b2aba09414b7ac970f6e5","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Lespedeza cyrtobotrya","taxon_id":"NCBITaxon:701533","organism_wikidata":"http://www.wikidata.org/entity/Q12618570","reference_doi":"10.1021/NP800395J","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1622,"row_sha256":"507c54170723798b0cd618f9eb1ab7be7083f724d63e55a315f2b69152f8e6ee","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Smilax glabra","taxon_id":"NCBITaxon:703614","organism_wikidata":"http://www.wikidata.org/entity/Q3658986","reference_doi":"10.1016/J.PHYTOCHEM.2008.01.002","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1623,"row_sha256":"f3f79b1dd267fa1c907e216e2453dfdb2e81344de0e22266a419b8cdbc2ecb3d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Artemisia absinthium","taxon_id":"NCBITaxon:72332","organism_wikidata":"http://www.wikidata.org/entity/Q25686","reference_doi":"10.1002/CBER.19731060919","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1624,"row_sha256":"840569efd3b4753995b781e919f7967152066db2b00285c2c0b92257ff308336","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Artemisia absinthium","taxon_id":"NCBITaxon:72332","organism_wikidata":"http://www.wikidata.org/entity/Q25686","reference_doi":"10.1016/S0031-9422(98)00180-0","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1625,"row_sha256":"b11085a6c6c1efba3d9e8201cc9b1748bab643dcf8db266742feccaa3a8949b3","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Artemisia absinthium","taxon_id":"NCBITaxon:72332","organism_wikidata":"http://www.wikidata.org/entity/Q25686","reference_doi":"10.1021/NP000005+","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1626,"row_sha256":"4e5ff9cc1167943b58e23b68d442021ac91073d9f6803daab77726163e485623","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Artemisia crithmifolia","taxon_id":"NCBITaxon:72340","organism_wikidata":"http://www.wikidata.org/entity/Q21871162","reference_doi":"10.1002/CBER.19731060919","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1627,"row_sha256":"b959c84c421e2851e634f3c2970c9038caec16fcc32d0c47bb28d1aa8e3cda30","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Artemisia crithmifolia","taxon_id":"NCBITaxon:72340","organism_wikidata":"http://www.wikidata.org/entity/Q21871162","reference_doi":"10.1021/NP000005+","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1628,"row_sha256":"f1db9115d3eeb22e86b073b6f2c7c93ba5452fd241aa0502c6ba96aff9cc81f0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Xanthorrhoea australis","taxon_id":"NCBITaxon:72655","organism_wikidata":"http://www.wikidata.org/entity/Q8043098","reference_doi":"10.1071/CH9740331","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1629,"row_sha256":"c5e146fca896f4125342379763edc8b41b6bd7409715fe7f349fe0b4dedccb1c","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Glycyrrhiza uralensis","taxon_id":"NCBITaxon:74613","organism_wikidata":"http://www.wikidata.org/entity/Q1196166","reference_doi":"10.1007/BF00574601","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1630,"row_sha256":"82c1aa1249da63c6f28f45a869f74a079b43bdd168327c8450d59772b0ac784b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Glycyrrhiza uralensis","taxon_id":"NCBITaxon:74613","organism_wikidata":"http://www.wikidata.org/entity/Q1196166","reference_doi":"10.1021/NP050034Q","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1631,"row_sha256":"53aa022b007dfe63ccd84092fe8425ecf8db9fe749efe2b12f5c75858a823211","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Glycyrrhiza inflata","taxon_id":"NCBITaxon:74614","organism_wikidata":"http://www.wikidata.org/entity/Q5572787","reference_doi":"10.1007/BF00574601","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1632,"row_sha256":"71d8d54e0585ef2121b9dba91d140906b6270c4f0cc7ae6abf6d5a811eed778a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Glycyrrhiza inflata","taxon_id":"NCBITaxon:74614","organism_wikidata":"http://www.wikidata.org/entity/Q5572787","reference_doi":"10.1021/NP050034Q","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1633,"row_sha256":"d77d180139ed350fedc8ec25f73dc84a594bc5cfbfde52bcf879b02de07ec463","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus reticulata","taxon_id":"NCBITaxon:85571","organism_wikidata":"http://www.wikidata.org/entity/Q125337","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1634,"row_sha256":"593cad86a1777dc27e2daea518436df5cd3c4c92a3e7e2d89158380b88d71cb3","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus reticulata","taxon_id":"NCBITaxon:85571","organism_wikidata":"http://www.wikidata.org/entity/Q125337","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1635,"row_sha256":"7d665f7e52227e7f2954f56109ab26b13586bbf1f2569d8562d7a238462b5dcb","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Cadophora gregata","taxon_id":"NCBITaxon:86000","organism_wikidata":"http://www.wikidata.org/entity/Q104096589","reference_doi":"10.1271/BBB1961.51.349","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1636,"row_sha256":"ccaec21b765fa62927cf91c5f9f6c5dab6e9dcf2b7fc6ff8d6c6da6e8ff24ca6","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Drynaria roosii","taxon_id":"NCBITaxon:872542","organism_wikidata":"http://www.wikidata.org/entity/Q5309744","reference_doi":"10.1080/14786410902991860","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1637,"row_sha256":"489449a28b34452e09d643597722787dede52aa358bcf22539cf6f2441a08c1f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium nobile","taxon_id":"NCBITaxon:94219","organism_wikidata":"http://www.wikidata.org/entity/Q636713","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1638,"row_sha256":"152ec4f5aece1787ce64c277732a7d22028df8183b369559e3174b6ad445a098","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Senna sophera","taxon_id":"NCBITaxon:948718","organism_wikidata":"http://www.wikidata.org/entity/Q2724545","reference_doi":"10.1248/CPB.42.2588","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1639,"row_sha256":"013d70debeff8b125fcd2b804126327e98aba2039c329fa931b1f8300ce126c9","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus serrulata var. spontanea","taxon_id":"NCBITaxon:97325","organism_wikidata":"http://www.wikidata.org/entity/Q3408652","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1640,"row_sha256":"6248f3c9bde868e7ecc23639f4319bd85b6b2c0cff8f7667696267b78a0c76b3","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus serrulata f. spontanea","taxon_id":"NCBITaxon:97325","organism_wikidata":"http://www.wikidata.org/entity/Q43374956","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}}] |
| bgc-2211-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved query frame with 0 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned cyanometdb_occurrences table; no query replay or external lookup. |
| bgc-2211-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0/source_scope_inventory/joins/npclassifier | supports | Complete saved query frame with 1 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned npclassifier table; no query replay or external lookup. |
| bgc-2211-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 608 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":608,"row_sha256":"94b1b7471a6e3a1c947999206a36cf4d3afdd36fc10990cab630e3d43dd29f9e","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","smiles":"C1C(OC2=CC(=CC(=C2C1=O)O)O)C3=CC=C(C=C3)O","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Flavonoids","class_results":"Flavanones","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}] |
| bgc-2211-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved query frame with 44 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned pubchem_bioassay table; no query replay or external lookup. |
| bgc-2211-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":1612,"row_sha256":"9f3fef636a3cda546d8b502acb9d1e973a4921938aad104af76db18199a6e465","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1159524","assay_name":"High Throughput Screening for Foot and Mouth Disease Virus Antivirals","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"14.1254","target_accession":"","reference":""}},{"physical_line":1613,"row_sha256":"0b2eae10a2bdb0bf979d152d2cc0627f0b321139c61608878aa75c912fd338c0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1452","assay_name":"qHTS Assay for Inhibitors of 12-hLO (12-human lipoxygenase)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"35.4813","target_accession":"NP_000688","reference":""}},{"physical_line":1614,"row_sha256":"2f92dd465ce54cae5069073d362f7369ad92adc9d9436aad5e5a931e0c68dd34","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1519","assay_name":"qHTS Assay for Lipid Storage Modulators","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"31.6228","target_accession":"","reference":""}},{"physical_line":1615,"row_sha256":"94cb6391bcacfb1626e663ed88db68a61457b51f35411961a513f42b6fc99d3a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1671190","assay_name":"Primary qHTS assay for inhibitors of human arachidonate 12S-lipoxygenase (ALOX12): Round 2","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"44.6684","target_accession":"","reference":""}},{"physical_line":1616,"row_sha256":"f21ec8205da3f74115b82fdaae133d25af4fe394180216ff5db726dccdaf9f18","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1671190","assay_name":"Primary qHTS assay for inhibitors of human arachidonate 12S-lipoxygenase (ALOX12): Round 2","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"44.6684","target_accession":"P18054","reference":""}},{"physical_line":1617,"row_sha256":"ef13c0a11cfd6506e1ae466a21d64135da57ef2dd268eda20efaab5016f5c8b8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1768","assay_name":"qHTS Assay for Inhibitors Targeting the Menin-MLL Interaction in MLL Related Leukemias: Competition With Texas Red Labeled MLL-derived Mutant Peptide","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"25.1189","target_accession":"NP_000235","reference":""}},{"physical_line":1618,"row_sha256":"362bdd1b19b0f8f31171c14a1eb42ffa90958f324f6f118a8d12fe12bf4e89c1","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1768","assay_name":"qHTS Assay for Inhibitors Targeting the Menin-MLL Interaction in MLL Related Leukemias: Competition With Texas Red Labeled MLL-derived Mutant Peptide","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"25.1189","target_accession":"NP_005924","reference":""}},{"physical_line":1619,"row_sha256":"9063e704ce2efb73279cd2a38e4be9c1e5e0f10d8276ba526d9fee386cb5a80a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1768","assay_name":"qHTS Assay for Inhibitors Targeting the Menin-MLL Interaction in MLL Related Leukemias: Competition With Texas Red Labeled MLL-derived Mutant Peptide","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"39.8107","target_accession":"NP_000235","reference":""}},{"physical_line":1620,"row_sha256":"5107003195563ca82676470a877bc51b322aff78dd3103ee14a409a653fc840b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1768","assay_name":"qHTS Assay for Inhibitors Targeting the Menin-MLL Interaction in MLL Related Leukemias: Competition With Texas Red Labeled MLL-derived Mutant Peptide","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"39.8107","target_accession":"NP_005924","reference":""}},{"physical_line":1621,"row_sha256":"4e9ae59f9626804e77f9d5c776ed468b2c71410b072f8873e1a4e7c28e9a9df6","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1797856","assay_name":"Competition-Based Ligand Binding Assay. from Article 10.1021/jm060692n: \"Subtle side-chain modifications of the hop phytoestrogen 8-prenylnaringenin result in distinct agonist/antagonist activity profiles for estrogen receptors alpha and beta.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Inactive","activity_name":"IC50","activity_value_um":"72.302","target_accession":"P03372","reference":"PMID:17149865"}},{"physical_line":1622,"row_sha256":"3ec858e2440383cf52f3971b33ff637e48e8e98dcee04a8d3d9a32b6f2b5bc4f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1797856","assay_name":"Competition-Based Ligand Binding Assay. from Article 10.1021/jm060692n: \"Subtle side-chain modifications of the hop phytoestrogen 8-prenylnaringenin result in distinct agonist/antagonist activity profiles for estrogen receptors alpha and beta.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Inactive","activity_name":"IC50","activity_value_um":"13.473","target_accession":"Q92731","reference":"PMID:17149865"}},{"physical_line":1623,"row_sha256":"a64423356600ecad90971a0d65aa802e24eb314bf3410213667ca48ec1726eb8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1799798","assay_name":"Aromatase Assay from Article 10.1111/j.1747-0285.2012.01439.x: \"Neoflavonoids and Tetrahydroquinolones as Possible Cancer Chemopreventive Agents.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"1.09662e-06","target_accession":"P11511","reference":"PMID:22726671"}},{"physical_line":1624,"row_sha256":"dec43574955f6709cebc151b6dbf0a8ba8350a55b0956f08d4f65fc258428b9d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1801531","assay_name":"AO Enzyme Assay from Article 10.1016/j.bioorg.2015.12.004: \"Inhibition of guinea pig aldehyde oxidase activity by different flavonoid compounds: An in vitro study.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Inactive","activity_name":"Ki","activity_value_um":"148","target_accession":"H9TB17","reference":"PMID:26722818"}},{"physical_line":1625,"row_sha256":"9168dbc42a49a14366165846f619aef4d637ccc29c1c035b878dbea242e71f1f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1803217","assay_name":"Esterase Activity Assay from Article 10.3109/14756366.2011.651464: \"Analysis of saponins and phenolic compounds as inhibitors of a-carbonic anhydrase isoenzymes.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"0.97","target_accession":"P00915","reference":"PMID:22299585"}},{"physical_line":1626,"row_sha256":"8aa2c7875ef0a87c04826722d5f70752414beb8b48e3271065bce93a6ed1e8da","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1803217","assay_name":"Esterase Activity Assay from Article 10.3109/14756366.2011.651464: \"Analysis of saponins and phenolic compounds as inhibitors of a-carbonic anhydrase isoenzymes.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"0.113","target_accession":"P00918","reference":"PMID:22299585"}},{"physical_line":1627,"row_sha256":"e8612f3220e705b3de210afebfd22613b9ae7efe300ec03fcf4f2f922ec27f9f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1803217","assay_name":"Esterase Activity Assay from Article 10.3109/14756366.2011.651464: \"Analysis of saponins and phenolic compounds as inhibitors of a-carbonic anhydrase isoenzymes.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"1.12","target_accession":"P22748","reference":"PMID:22299585"}},{"physical_line":1628,"row_sha256":"35699815e513895874e31e651df931d009ecdff5654a58955a744dbc910a5d4a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1803217","assay_name":"Esterase Activity Assay from Article 10.3109/14756366.2011.651464: \"Analysis of saponins and phenolic compounds as inhibitors of a-carbonic anhydrase isoenzymes.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"1.49","target_accession":"P23280","reference":"PMID:22299585"}},{"physical_line":1629,"row_sha256":"3a11cc0c51266ce3ca7ba1fd1eb477abc692a2e7867d1da6271a53fca792fea4","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1803217","assay_name":"Esterase Activity Assay from Article 10.3109/14756366.2011.651464: \"Analysis of saponins and phenolic compounds as inhibitors of a-carbonic anhydrase isoenzymes.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"2.21","target_accession":"Q3SZX4","reference":"PMID:22299585"}},{"physical_line":1630,"row_sha256":"ada787db3d8afa375237d4fce81749ff5419c8c15b76938399b77f3bd6da3954","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1948","assay_name":"qHTS Assay for Compounds that Induce Erasure of Genomic Imprints","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"12.5893","target_accession":"","reference":""}},{"physical_line":1631,"row_sha256":"bfb4dd30830769639c968ea6bd268202313bb2e90e3915a267871961f5427511","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1948","assay_name":"qHTS Assay for Compounds that Induce Erasure of Genomic Imprints","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"15.8489","target_accession":"","reference":""}},{"physical_line":1632,"row_sha256":"a2e59000768e21342f222680d333c330e81f746035a80abd2445af8fc4eb00b9","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2101","assay_name":"qHTS Assay for Inhibitors and Activators of N370S glucocerebrosidase as a Potential Chaperone Treatment of Gaucher Disease","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"11.2202","target_accession":"BAA02545","reference":""}},{"physical_line":1633,"row_sha256":"2e9cebd4e1b0f4b3fb9ad8b97f514bd2259389570c2e275caacdb755c2c2ac9c","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2101","assay_name":"qHTS Assay for Inhibitors and Activators of N370S glucocerebrosidase as a Potential Chaperone Treatment of Gaucher Disease","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"22.3872","target_accession":"BAA02545","reference":""}},{"physical_line":1634,"row_sha256":"218c6102b6a91a80e5c65c74cfb86c96ee9674b19d789b15583b455448ae7e06","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2288","assay_name":"qHTS Assay for Modulators of miRNAs and/orActivators of miR-21","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"9.2683","target_accession":"","reference":""}},{"physical_line":1635,"row_sha256":"74c17abacdd68986bafcf2bc30a70a6c1e93703177441041e1ea3218cce618b9","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2289","assay_name":"qHTS Assay for Modulators of miRNAs and/or Inhibitors of miR-21","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"9.2683","target_accession":"","reference":""}},{"physical_line":1636,"row_sha256":"e3165eb22200a8ca44dfa0262c39595cc094e4d08a6100618f740138188f92f5","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2314","assay_name":"Cycloheximide Counterscreen for Small Molecule Inhibitors of Shiga Toxin","assay_type":"Screening","depositor":"NCGC","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"BAC78637","reference":""}},{"physical_line":1637,"row_sha256":"712cd7082760ae0e5d94a472e15391001cf41b48410d897150937add87525b8e","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2314","assay_name":"Cycloheximide Counterscreen for Small Molecule Inhibitors of Shiga Toxin","assay_type":"Screening","depositor":"NCGC","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"BAC78638","reference":""}},{"physical_line":1638,"row_sha256":"4f55464a785ce2911403b63effc82d46eb197fe349c7a1a8f10fc3c4852e90a2","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2517","assay_name":"qHTS Assay for Inhibitors of the Human Apurinic/apyrimidinic Endonuclease 1 (APE1)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"199.526","target_accession":"1DE9_A","reference":""}},{"physical_line":1639,"row_sha256":"e8ded9e199e495f9313c7002df64df95bb7f97f5e8ab4708695ddef5cacf17bc","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2551","assay_name":"qHTS for inhibitors of ROR gamma transcriptional activity","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"35.4813","target_accession":"NP_035411","reference":""}},{"physical_line":1640,"row_sha256":"6ae62bb6834a956263c23cfd1dd460f0aa3ddafdf992be8c8de2ef0c2218aa6f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2551","assay_name":"qHTS for inhibitors of ROR gamma transcriptional activity","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"15.8489","target_accession":"NP_035411","reference":""}},{"physical_line":1641,"row_sha256":"c9dd9fccfffffafb96eef05d7ca5e7cb1692bad2f2936aaaec105c1bda7c0dad","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"388","assay_name":"Compound Screen Assay, Human HPGD","assay_type":"Screening","depositor":"SGCOxCompounds","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"AAA89174","reference":""}},{"physical_line":1642,"row_sha256":"3b6ba545a68371646444ddde5e06c50fbdc6a784df4989a4d6642d2159ee23a4","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"485281","assay_name":"qHTS Assay for Identification of Novel General Anesthetics","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"28.1838","target_accession":"3F32_A","reference":""}},{"physical_line":1643,"row_sha256":"308c778a4dfbe36c77e6969ae60467e67fdbb7b6a5e462e2f60df69775f0bbea","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"485317","assay_name":"HTS-Luminescent assay for inhibitors of ALR by detection of hydrogen peroxide production Measured in Biochemical System Using Plate Reader - 2036-02_Inhibitor_SinglePoint_HTS","assay_type":"Screening","depositor":"Broad Institute","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"NP_005253","reference":""}},{"physical_line":1644,"row_sha256":"e824fbcfac6aa5fda51d7027af2092b7b369f3ddee7f0d0471e5fe980e06790f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"485367","assay_name":"qHTS Assay to Find Inhibitors of T. brucei phosphofructokinase","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"0.7569","target_accession":"XP_843920","reference":""}},{"physical_line":1645,"row_sha256":"0fee31af74fd9d51d32d88fa6cb6e8a49d65a82505906f17d57d83aea88c4afc","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"504832","assay_name":"Primary qHTS for delayed death inhibitors of the malarial parasite plastid, 48 hour incubation","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"2.6169","target_accession":"","reference":""}},{"physical_line":1646,"row_sha256":"f4d04e9dda7abaed40344bc1858836788687b7708056cdf49f5eb95fb3f7afe0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"504834","assay_name":"Primary qHTS for delayed death inhibitors of the malarial parasite plastid, 96 hour incubation","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"6.5733","target_accession":"","reference":""}},{"physical_line":1647,"row_sha256":"7ca9c1252b1be25bb1773f4494b77927b6ef08183150fdb4f721bc6b884024a7","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"588342","assay_name":"qHTS profiling assay for firefly luciferase inhibitor/activator using purifed enzyme and Km concentrations of substrates (counterscreen for miR-21 project)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"30.1313","target_accession":"AAA29795","reference":""}},{"physical_line":1648,"row_sha256":"35f268327a444e006c523f6a487c1ec7126c9ea818f3ed2f916c82cbe0cd5e8d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"588590","assay_name":"qHTS for Inhibitors of Polymerase Iota","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"0.631","target_accession":"NP_009126","reference":""}},{"physical_line":1649,"row_sha256":"137b865f92e7340574438c1adf2c678621ae578ab9c157cdeb0528cd18ffc683","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"624297","assay_name":"A quantitative high throughput screen for small molecules that induce DNA re-replication in SW480 colon adenocarcinoma cells.","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"2.5119","target_accession":"NP_056979","reference":""}},{"physical_line":1650,"row_sha256":"c0daa8bb5b9c48abae4b14e4b75b303003b206004aed0dedc3e49c72cf36d37a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"720532","assay_name":"qHTS for Inhibitors of binding or entry into cells for Marburg Virus","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"35.4813","target_accession":"B45705","reference":""}},{"physical_line":1651,"row_sha256":"8debce75d6ba8474591bb974cfb27840a369bceea3073e86c59c95a1ab932d2b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"720532","assay_name":"qHTS for Inhibitors of binding or entry into cells for Marburg Virus","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"14.1254","target_accession":"B45705","reference":""}},{"physical_line":1652,"row_sha256":"adda963159cffb945808f36fc37871eb2820689314382687a13a16090316db03","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"884","assay_name":"qHTS Assay for Inhibitors and Substrates of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Active","activity_name":"Potency","activity_value_um":"10","target_accession":"NP_059488","reference":""}},{"physical_line":1653,"row_sha256":"e23b5e02a71dfacab9e964aacc448be7656e2950c83f889473b1402242b2aaa0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"884","assay_name":"qHTS Assay for Inhibitors and Substrates of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Active","activity_name":"Potency","activity_value_um":"12.5893","target_accession":"NP_059488","reference":""}},{"physical_line":1654,"row_sha256":"fc1f969b8f24b7dea393883b4f4ed518baa5f38a5f762270265bf73970f7bf1b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"885","assay_name":"qHTS Assay for Activators of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"10","target_accession":"NP_059488","reference":""}},{"physical_line":1655,"row_sha256":"551bc2016293417bbee2eab0dada0f1483407a7d42087f67d7b966bd0c94d6d1","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"885","assay_name":"qHTS Assay for Activators of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"12.5893","target_accession":"NP_059488","reference":""}}] |
| bgc-2211-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved query frame with 9 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned bindingdb_targets table; no query replay or external lookup. |
| bgc-2211-source-bindingdb_targets | /private/tmp/npm-record-reviews-20261021/data/raw/bindingdb_targets.tsv; Physical TSV lines 14, 15, 16, 17, 18, 19, 20, 21, 22 | supports | Complete retained fields, including blanks, and exact physical-frame hashes: [{"physical_line":14,"row_sha256":"97fe0b7aa354d44c76a818d1ab1144b642712e3651360ff065099ebf82d15d8d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Aldehyde oxidase 1","target_organism":"Cavia porcellus","uniprot":"H9TB17","measurement_type":"KI","measurement_value_nm":"148000","measurement_qualifier":"EQUAL","ph":"7.0000","temperature_c":"","reference":"PMID:26722818","curation_source":"Curated from the literature by BindingDB"}},{"physical_line":15,"row_sha256":"fee7eda52c387c32b21984115620a25a3636066f30d606d7af67a46e7bbaa030","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Aromatase","target_organism":"Homo sapiens","uniprot":"P11511","measurement_type":"KI","measurement_value_nm":"0.00109662","measurement_qualifier":"EQUAL","ph":"","temperature_c":"","reference":"PMID:22726671","curation_source":"Curated from the literature by BindingDB"}},{"physical_line":16,"row_sha256":"759ec3ba158ca0912c9e57e98ddb4b59d887acf1ab6a365f469b204bf19a9a09","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Carbonic anhydrase 1","target_organism":"Homo sapiens","uniprot":"P00915","measurement_type":"KI","measurement_value_nm":"970","measurement_qualifier":"EQUAL","ph":"7.4000","temperature_c":"","reference":"PMID:22299585","curation_source":"Curated from the literature by BindingDB"}},{"physical_line":17,"row_sha256":"07a9e89c7719ad02277168e160de1a71445b74f73384abaddff5fda08b721884","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Carbonic anhydrase 2","target_organism":"Homo sapiens","uniprot":"P00918","measurement_type":"KI","measurement_value_nm":"113","measurement_qualifier":"EQUAL","ph":"7.4000","temperature_c":"","reference":"PMID:22299585","curation_source":"Curated from the literature by BindingDB"}},{"physical_line":18,"row_sha256":"f9ca50845f2c7c145c4ec98d0c82c4ec58e74e981771a56569a4d24fe8991be7","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Carbonic anhydrase 3","target_organism":"Bos taurus","uniprot":"Q3SZX4","measurement_type":"KI","measurement_value_nm":"2210","measurement_qualifier":"EQUAL","ph":"7.4000","temperature_c":"","reference":"PMID:22299585","curation_source":"Curated from the literature by BindingDB"}},{"physical_line":19,"row_sha256":"8179a7a41b72fbd2cef87d3d0b2e55ea23b87956484894a570d6aa25a043c68c","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Carbonic anhydrase 4","target_organism":"Homo sapiens","uniprot":"P22748","measurement_type":"KI","measurement_value_nm":"1120","measurement_qualifier":"EQUAL","ph":"7.4000","temperature_c":"","reference":"PMID:22299585","curation_source":"Curated from the literature by BindingDB"}},{"physical_line":20,"row_sha256":"9a093ad5763193868168b894f506f2ab24740b3fb92a1d0a2c3d77d349104138","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Carbonic anhydrase 6","target_organism":"Homo sapiens","uniprot":"P23280","measurement_type":"KI","measurement_value_nm":"1490","measurement_qualifier":"EQUAL","ph":"7.4000","temperature_c":"","reference":"PMID:22299585","curation_source":"Curated from the literature by BindingDB"}},{"physical_line":21,"row_sha256":"fe13f6054c429af66a36e5a0baab615d993541b7e098b986a45d9651bd125c09","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Estrogen receptor","target_organism":"Homo sapiens","uniprot":"P03372","measurement_type":"IC50","measurement_value_nm":"72302","measurement_qualifier":"EQUAL","ph":"7.6000","temperature_c":"22.00 C","reference":"PMID:17149865","curation_source":"Curated from the literature by BindingDB"}},{"physical_line":22,"row_sha256":"bf268d38d1b853438db72e4e2536c9db874d0c0edeb3a9b79c2d5a215eed89f5","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Estrogen receptor beta","target_organism":"Homo sapiens","uniprot":"Q92731","measurement_type":"IC50","measurement_value_nm":"13473","measurement_qualifier":"EQUAL","ph":"7.6000","temperature_c":"22.00 C","reference":"PMID:17149865","curation_source":"Curated from the literature by BindingDB"}}] |
| bgc-2211-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved query frame with 0 positive placements. Exact saved predicate exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned antibioticmech_inchikeys table; no query replay or external lookup. |
| bgc-2211-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0/source_scope_inventory/joins/chebi_origins | supports | Complete saved query frame with 0 positive placements. Exact saved predicate exact chebi_id from exact full-key structure rows with query ["CHEBI:50202"] against the pinned chebi_origins table; no query replay or external lookup. |
| bgc-2211-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/5; /cached_taxonomy/whole_stanzas/7; /cached_taxonomy/whole_stanzas/15; /cached_taxonomy/whole_stanzas/16; /cached_taxonomy/whole_stanzas/17; /cached_taxonomy/whole_stanzas/21; /cached_taxonomy/whole_stanzas/23; /cached_taxonomy/whole_stanzas/24; /cached_taxonomy/whole_stanzas/26; /cached_taxonomy/whole_stanzas/29; /cached_taxonomy/whole_stanzas/30; /cached_taxonomy/whole_stanzas/31; /cached_taxonomy/whole_stanzas/32; /cached_taxonomy/whole_stanzas/35; /cached_taxonomy/whole_stanzas/36; /cached_taxonomy/whole_stanzas/37; /cached_taxonomy/whole_stanzas/38; /cached_taxonomy/whole_stanzas/41; /cached_taxonomy/whole_stanzas/42; /cached_taxonomy/whole_stanzas/43; /cached_taxonomy/whole_stanzas/44; /cached_taxonomy/whole_stanzas/45; /cached_taxonomy/whole_stanzas/46; /cached_taxonomy/whole_stanzas/53; /cached_taxonomy/whole_stanzas/54; /cached_taxonomy/whole_stanzas/63; /cached_taxonomy/whole_stanzas/66; /cached_taxonomy/whole_stanzas/68; /cached_taxonomy/whole_stanzas/71; /cached_taxonomy/whole_stanzas/75; /cached_taxonomy/whole_stanzas/76; /cached_taxonomy/whole_stanzas/80; /cached_taxonomy/whole_stanzas/83; /cached_taxonomy/whole_stanzas/84; /cached_taxonomy/whole_stanzas/85; /cached_taxonomy/whole_stanzas/86; /cached_taxonomy/whole_stanzas/90; /cached_taxonomy/whole_stanzas/93; /cached_taxonomy/whole_stanzas/99; /cached_taxonomy/whole_stanzas/101; /cached_taxonomy/whole_stanzas/110; /cached_taxonomy/whole_stanzas/111; /cached_taxonomy/whole_stanzas/113; /cached_taxonomy/whole_stanzas/122; /cached_taxonomy/whole_stanzas/128; /cached_taxonomy/whole_stanzas/131; /cached_taxonomy/whole_stanzas/132; /cached_taxonomy/whole_stanzas/134; /cached_taxonomy/whole_stanzas/135; /cached_taxonomy/whole_stanzas/137; /cached_taxonomy/whole_stanzas/139; /cached_taxonomy/whole_stanzas/140; /cached_taxonomy/whole_stanzas/145; /cached_taxonomy/whole_stanzas/150; /cached_taxonomy/whole_stanzas/156; /cached_taxonomy/whole_stanzas/160; /cached_taxonomy/whole_stanzas/162; /cached_taxonomy/whole_stanzas/169; /cached_taxonomy/whole_stanzas/178; /cached_taxonomy/whole_stanzas/179; /cached_taxonomy/whole_stanzas/181; /cached_taxonomy/whole_stanzas/182; /cached_taxonomy/whole_stanzas/184 | supports | Complete personally read cached name/synonym stanzas for selected source taxa: [{"id":"NCBITaxon:1901","physical_line":2911,"complete_stanza":"[Term]\nid: NCBITaxon:1901\nname: Streptomyces clavuligerus\n\n"},{"id":"NCBITaxon:3760","physical_line":5437,"complete_stanza":"[Term]\nid: NCBITaxon:3760\nname: Prunus persica\nsynonym: \"Amygdalus persica\" EXACT []\nsynonym: \"Persica vulgaris\" EXACT []\nsynonym: \"Prunus persica var. densa\" EXACT []\n\n"},{"id":"NCBITaxon:3914","physical_line":5905,"complete_stanza":"[Term]\nid: NCBITaxon:3914\nname: Vigna angularis\nsynonym: \"Phaseolus angularis\" EXACT []\n\n"},{"id":"NCBITaxon:9606","physical_line":10335,"complete_stanza":"[Term]\nid: NCBITaxon:9606\nname: Homo sapiens\n\n"},{"id":"NCBITaxon:9913","physical_line":10452,"complete_stanza":"[Term]\nid: NCBITaxon:9913\nname: Bos taurus\nsynonym: \"Bos bovis\" EXACT []\nsynonym: \"Bos primigenius taurus\" EXACT []\n\n"},{"id":"NCBITaxon:10141","physical_line":10510,"complete_stanza":"[Term]\nid: NCBITaxon:10141\nname: Cavia porcellus\nsynonym: \"Cavia aperea porcellus\" EXACT []\nsynonym: \"Cavia cobaya\" EXACT []\nsynonym: \"Mus porcellus\" EXACT []\n\n"},{"id":"NCBITaxon:34199","physical_line":14887,"complete_stanza":"[Term]\nid: NCBITaxon:34199\nname: Aloe vera\nsynonym: \"Aloe barbadensis\" EXACT []\nsynonym: \"Aloe perfoliata var. vera\" EXACT []\n\n"},{"id":"NCBITaxon:37334","physical_line":16255,"complete_stanza":"[Term]\nid: NCBITaxon:37334\nname: Citrus maxima\nsynonym: \"Aurantium maximum\" EXACT []\nsynonym: \"Citrus decumana\" EXACT []\nsynonym: \"Citrus decumanus\" EXACT []\nsynonym: \"Citrus grandis\" EXACT []\n\n"},{"id":"NCBITaxon:37690","physical_line":16440,"complete_stanza":"[Term]\nid: NCBITaxon:37690\nname: Citrus trifoliata\nsynonym: \"Poncirus trifoliata\" EXACT []\nsynonym: \"Poncirus trifoliatus\" EXACT []\n\n"},{"id":"NCBITaxon:38843","physical_line":16879,"complete_stanza":"[Term]\nid: NCBITaxon:38843\nname: Euphorbia amygdaloides\n\n"},{"id":"NCBITaxon:41503","physical_line":18720,"complete_stanza":"[Term]\nid: NCBITaxon:41503\nname: Centaurea\nsynonym: \"Aegialophila\" EXACT []\nsynonym: \"Colymbada\" EXACT []\nsynonym: \"Cyanus\" EXACT []\nsynonym: \"Hyalea\" EXACT []\nsynonym: \"Stephanochilus\" EXACT []\n\n"},{"id":"NCBITaxon:41511","physical_line":18742,"complete_stanza":"[Term]\nid: NCBITaxon:41511\nname: Centaurea calcitrapa\n\n"},{"id":"NCBITaxon:41568","physical_line":18822,"complete_stanza":"[Term]\nid: NCBITaxon:41568\nname: Chrysanthemum x morifolium\nsynonym: \"Chrysanthemum hortorum\" EXACT []\nsynonym: \"Chrysanthemum morifolium\" EXACT []\nsynonym: \"Dendranthema grandiflora\" EXACT []\nsynonym: \"Dendranthema morifolium\" EXACT []\nsynonym: \"Dendranthema x grandiflorum\" EXACT []\nsynonym: \"Dendranthema x morifolium\" EXACT []\nsynonym: \"Matricaria morifolia\" EXACT []\n\n"},{"id":"NCBITaxon:42229","physical_line":19307,"complete_stanza":"[Term]\nid: NCBITaxon:42229\nname: Prunus avium\nsynonym: \"Cerasus avium\" EXACT []\nsynonym: \"Prunus cerasus var. avium\" EXACT []\n\n"},{"id":"NCBITaxon:49657","physical_line":22590,"complete_stanza":"[Term]\nid: NCBITaxon:49657\nname: Smilax china\n\n"},{"id":"NCBITaxon:49740","physical_line":22645,"complete_stanza":"[Term]\nid: NCBITaxon:49740\nname: Xanthorrhoea resinosa\nsynonym: \"Xanthorrhoea hastilis\" EXACT []\n\n"},{"id":"NCBITaxon:55188","physical_line":25581,"complete_stanza":"[Term]\nid: NCBITaxon:55188\nname: Citrus unshiu\nsynonym: \"Citrus nobilis var. unshiu\" EXACT []\nsynonym: \"Citrus unshiu var. praecox\" EXACT []\n\n"},{"id":"NCBITaxon:58880","physical_line":27031,"complete_stanza":"[Term]\nid: NCBITaxon:58880\nname: Phyllanthus\nsynonym: \"Reverchonia\" EXACT []\n\n"},{"id":"NCBITaxon:66379","physical_line":29521,"complete_stanza":"[Term]\nid: NCBITaxon:66379\nname: Broussonetia\n\n"},{"id":"NCBITaxon:72332","physical_line":32504,"complete_stanza":"[Term]\nid: NCBITaxon:72332\nname: Artemisia absinthium\n\n"},{"id":"NCBITaxon:72340","physical_line":32532,"complete_stanza":"[Term]\nid: NCBITaxon:72340\nname: Artemisia crithmifolia\n\n"},{"id":"NCBITaxon:72655","physical_line":32704,"complete_stanza":"[Term]\nid: NCBITaxon:72655\nname: Xanthorrhoea australis\n\n"},{"id":"NCBITaxon:74613","physical_line":33600,"complete_stanza":"[Term]\nid: NCBITaxon:74613\nname: Glycyrrhiza uralensis\n\n"},{"id":"NCBITaxon:74614","physical_line":33604,"complete_stanza":"[Term]\nid: NCBITaxon:74614\nname: Glycyrrhiza inflata\n\n"},{"id":"NCBITaxon:85571","physical_line":37630,"complete_stanza":"[Term]\nid: NCBITaxon:85571\nname: Citrus reticulata\nsynonym: \"Citrus poonensis\" EXACT []\n\n"},{"id":"NCBITaxon:86000","physical_line":37858,"complete_stanza":"[Term]\nid: NCBITaxon:86000\nname: Cadophora gregata f. sp. adzukicola\nsynonym: \"Phialophora gregata f. sp. adzukicola\" EXACT []\n\n"},{"id":"NCBITaxon:94219","physical_line":40124,"complete_stanza":"[Term]\nid: NCBITaxon:94219\nname: Dendrobium nobile\n\n"},{"id":"NCBITaxon:97325","physical_line":40715,"complete_stanza":"[Term]\nid: NCBITaxon:97325\nname: Prunus jamasakura\nsynonym: \"Cerasus jamasakura\" EXACT []\nsynonym: \"Prunus serrulata f. spontanea\" EXACT []\nsynonym: \"Prunus serrulata var. spontanea\" EXACT []\n\n"},{"id":"NCBITaxon:102107","physical_line":41949,"complete_stanza":"[Term]\nid: NCBITaxon:102107\nname: Prunus mume\nsynonym: \"Armeniaca mume\" EXACT []\n\n"},{"id":"NCBITaxon:112358","physical_line":44405,"complete_stanza":"[Term]\nid: NCBITaxon:112358\nname: Helichrysum cephaloideum\n\n"},{"id":"NCBITaxon:117953","physical_line":45581,"complete_stanza":"[Term]\nid: NCBITaxon:117953\nname: Dendrobium fimbriatum\n\n"},{"id":"NCBITaxon:117954","physical_line":45585,"complete_stanza":"[Term]\nid: NCBITaxon:117954\nname: Dendrobium loddigesii\n\n"},{"id":"NCBITaxon:136465","physical_line":49480,"complete_stanza":"[Term]\nid: NCBITaxon:136465\nname: Prunus campanulata\nsynonym: \"Cerasus campanulata\" EXACT []\nsynonym: \"Prunus cerasoides var. campanulata\" EXACT []\n\n"},{"id":"NCBITaxon:142614","physical_line":51061,"complete_stanza":"[Term]\nid: NCBITaxon:142614\nname: Dendrobium moniliforme\nsynonym: \"Epidendrum moniliforme\" EXACT []\n\n"},{"id":"NCBITaxon:142615","physical_line":51066,"complete_stanza":"[Term]\nid: NCBITaxon:142615\nname: Dendrobium officinale\nsynonym: \"Dendrobium funiushanense\" EXACT []\nsynonym: \"Dendrobium tosaense\" EXACT []\n\n"},{"id":"NCBITaxon:151430","physical_line":52673,"complete_stanza":"[Term]\nid: NCBITaxon:151430\nname: Prunus davidiana\nsynonym: \"Amygdalus davidiana\" EXACT []\nsynonym: \"Persica davidiana\" EXACT []\n\n"},{"id":"NCBITaxon:154291","physical_line":53456,"complete_stanza":"[Term]\nid: NCBITaxon:154291\nname: Dendrobium chrysanthum\n\n"},{"id":"NCBITaxon:161865","physical_line":55319,"complete_stanza":"[Term]\nid: NCBITaxon:161865\nname: Dendrobium chrysotoxum\n\n"},{"id":"NCBITaxon:162811","physical_line":55653,"complete_stanza":"[Term]\nid: NCBITaxon:162811\nname: Intsia\n\n"},{"id":"NCBITaxon:194324","physical_line":62977,"complete_stanza":"[Term]\nid: NCBITaxon:194324\nname: Maclura cochinchinensis\nsynonym: \"Cudrania cochinchinensis\" EXACT []\n\n"},{"id":"NCBITaxon:210328","physical_line":66395,"complete_stanza":"[Term]\nid: NCBITaxon:210328\nname: Maclura tricuspidata\nsynonym: \"Cudrania tricuspidata\" EXACT []\n\n"},{"id":"NCBITaxon:257357","physical_line":73411,"complete_stanza":"[Term]\nid: NCBITaxon:257357\nname: Dendrobium longicornu\n\n"},{"id":"NCBITaxon:257360","physical_line":73415,"complete_stanza":"[Term]\nid: NCBITaxon:257360\nname: Dendrobium trigonopus\n\n"},{"id":"NCBITaxon:261776","physical_line":74253,"complete_stanza":"[Term]\nid: NCBITaxon:261776\nname: Helichrysum arenarium\nsynonym: \"Gnaphalium arenarium\" EXACT []\n\n"},{"id":"NCBITaxon:318062","physical_line":82057,"complete_stanza":"[Term]\nid: NCBITaxon:318062\nname: Euphorbia hirta\nsynonym: \"Chamaesyce hirta\" EXACT []\nsynonym: \"Euphorbia pilulifera\" EXACT []\n\n"},{"id":"NCBITaxon:363441","physical_line":86836,"complete_stanza":"[Term]\nid: NCBITaxon:363441\nname: Centaurea pallescens\n\n"},{"id":"NCBITaxon:431188","physical_line":93240,"complete_stanza":"[Term]\nid: NCBITaxon:431188\nname: Dendrobium candidum\n\n"},{"id":"NCBITaxon:470286","physical_line":97012,"complete_stanza":"[Term]\nid: NCBITaxon:470286\nname: Xanthorrhoea preissii\n\n"},{"id":"NCBITaxon:499988","physical_line":99242,"complete_stanza":"[Term]\nid: NCBITaxon:499988\nname: Dalbergia odorifera\n\n"},{"id":"NCBITaxon:558547","physical_line":102314,"complete_stanza":"[Term]\nid: NCBITaxon:558547\nname: Citrus x aurantium f. deliciosa\nsynonym: \"Citrus deliciosa\" EXACT []\nsynonym: \"Citrus nobilis var. deliciosa\" EXACT []\nsynonym: \"Citrus reticulata subsp. deliciosa\" EXACT []\n\n"},{"id":"NCBITaxon:630307","physical_line":104857,"complete_stanza":"[Term]\nid: NCBITaxon:630307\nname: Helichrysum graveolens\nsynonym: \"Gnaphalium graveolens\" EXACT []\n\n"},{"id":"NCBITaxon:701533","physical_line":108331,"complete_stanza":"[Term]\nid: NCBITaxon:701533\nname: Lespedeza cyrtobotrya\n\n"},{"id":"NCBITaxon:703614","physical_line":108412,"complete_stanza":"[Term]\nid: NCBITaxon:703614\nname: Smilax glabra\n\n"},{"id":"NCBITaxon:872542","physical_line":111649,"complete_stanza":"[Term]\nid: NCBITaxon:872542\nname: Aglaomorpha fortunei\nsynonym: \"Drynaria fortunei (Kunze ex Mett.) J.Sm., 1857, non T.Moore, 1855\" EXACT []\nsynonym: \"Drynaria roosii\" EXACT []\nsynonym: \"Polypodium fortunei\" EXACT []\n\n"},{"id":"NCBITaxon:948718","physical_line":113769,"complete_stanza":"[Term]\nid: NCBITaxon:948718\nname: Senna sophera\nsynonym: \"Cassia sophera\" EXACT []\n\n"},{"id":"NCBITaxon:1284230","physical_line":125248,"complete_stanza":"[Term]\nid: NCBITaxon:1284230\nname: Prunus lycioides\nsynonym: \"Amygdalus horrida\" EXACT []\nsynonym: \"Amygdalus lycioides\" EXACT []\nsynonym: \"Amygdalus lycioides Spach\" EXACT []\nsynonym: \"Amygdalus lycioides var. horrida\" EXACT []\nsynonym: \"Amygdalus lycioides var. lycioides\" EXACT []\n\n"},{"id":"NCBITaxon:1353466","physical_line":127313,"complete_stanza":"[Term]\nid: NCBITaxon:1353466\nname: Dalbergia parviflora\n\n"},{"id":"NCBITaxon:1378005","physical_line":127692,"complete_stanza":"[Term]\nid: NCBITaxon:1378005\nname: Rhynchosia beddomei\n\n"},{"id":"NCBITaxon:1835378","physical_line":139240,"complete_stanza":"[Term]\nid: NCBITaxon:1835378\nname: Brosimum acutifolium\n\n"},{"id":"NCBITaxon:2773069","physical_line":151344,"complete_stanza":"[Term]\nid: NCBITaxon:2773069\nname: Ageratina havanensis\nsynonym: \"Eupatorium havanense\" EXACT []\n\n"},{"id":"NCBITaxon:2841764","physical_line":152628,"complete_stanza":"[Term]\nid: NCBITaxon:2841764\nname: Senecio adenophyllus\n\n"},{"id":"NCBITaxon:2918710","physical_line":153877,"complete_stanza":"[Term]\nid: NCBITaxon:2918710\nname: Daphne aurantiaca\n\n"},{"id":"NCBITaxon:2986971","physical_line":154862,"complete_stanza":"[Term]\nid: NCBITaxon:2986971\nname: Prunus itosakura\nsynonym: \"Cerasus itosakura\" EXACT []\nsynonym: \"Prunus taiwaniana\" EXACT []\n\n"},{"id":"NCBITaxon:3769976","physical_line":161829,"complete_stanza":"[Term]\nid: NCBITaxon:3769976\nname: Centaurea hyalolepis\n\n"}]. No hierarchy or fresh taxonomy verification is inferred. |
| bgc-2211-source-routes | /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json; /records/0/source_scope_inventory/source_taxa; /records/0/source_scope_inventory/forward_taxon_merge_matches; /records/0/source_scope_inventory/nonorganism_matches | supports | Exact saved source-taxon and forward-merge/nonorganism route lists. No selected forward-merge or nonorganism match is retained. |
| bgc-2211-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Workflow; Output | supports | Immutable claim-level review, local evidence scope, honest partial completion and actionable ownership. |
| bgc-2211-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Complete maintained review profile | supports | Source qualification, producer/occurrence distinctions, computed-classification limits and evidence-backed issue normalization. |
| bgc-2211-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 376–432 | supports | Structure and stereo encoding plus explicitly computed NPClassifier fields; model outputs are not source assertions. |
| bgc-2211-activity-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 632–665; lines 920–947 | supports | Optional observation activity_class and coarse activity buckets require backing; no dedicated cytotoxic or enzyme-inhibitor definition is supplied. |
| bgc-2211-activity-classifier | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 127–179; lines 1310–1382 | supports | Maintained classifier unambiguity intent, generic title patterns, ACTIVE-only class assignment and written-observation summary derivation. |
| bgc-2211-definition-owner | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 985–1005 | supports | Maintained seeder copies a unique retained ChEBI definition and its source identifier; a correction must preserve honest provenance. |
| bgc-2211-reader-DATA | /private/tmp/npm-review-work/shared-next-batch222/native-current222-naringenin-maintained-reader-DATA-001.json; /resolved_view; /raw_owner; /expected_view; /counts; /returned_view_equals_expected_complete_owner; /review_check_metadata | supports | Complete original maintained owner view equals the captured owner, preserving every graph/pathway/target/history field; no scientific evidence is upgraded by reader success. |
| bgc-2211-reader-execution | /private/tmp/npm-review-work/shared-next-batch222/native-current222-naringenin-reader-execution-001.json; /exit_code; /command; /stdout; /stderr; /original_tool | supports | Original maintained-reader execution receipt, streams and exact invocation provenance. |
| bgc-2211-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch222/root-naringenin-maintained-reader-acceptance-001.json; /status; /verification; /review_check_contract | supports | ROOT acceptance of exact complete-owner/positive-content equality and original terminal success; expected capability construction was denied before action, with no external request. |
| bgc-2211-graph-0 | /private/tmp/npm-review-work/shared-next-batch222/native-current222-naringenin-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/0 | supports | Complete graph naringenin-carbonic-anhydrase-inhibition: 6 node placements and 5 edges, every evidence item and limitation retained. Retained graph description: Naringenin inhibits human and bovine carbonic anhydrase isoenzymes. |
| bgc-2211-graph-1 | /private/tmp/npm-review-work/shared-next-batch222/native-current222-naringenin-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/1 | supports | Complete graph naringenin-aromatase-inhibition: 2 node placements and 1 edges, every evidence item and limitation retained. Retained graph description: Naringenin inhibits human aromatase. |
| bgc-2211-targets | /private/tmp/npm-review-work/shared-next-batch222/native-current222-naringenin-maintained-reader-DATA-001.json; /resolved_view/molecular_targets | supports | All nine retained affinity targets with exact protein/taxon/measurement/qualifier/reference scope; no unique-experiment or fresh protein-identity claim. |
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
review_id: 20261103T123413Z-naringenin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: naringenin'
started_at: '2026-11-03T12:06:20.516813Z'
finished_at: '2026-11-03T12:34:13.213455Z'
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
summary: Naringenin retains a coherent but stereochemically unspecified flavanone
  representation. The local review identifies a wrong hydroxyl locant in its retained
  definition and unsupported cytotoxic typing of its aromatase assay. All source quantities
  and curated target evidence remain unchanged; external verification is unavailable.
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml
    sha256: 30439c876d49bfb6eab5bd078633b3ab9402e2c1c29c2db74bfbc0275c0775dc
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
  selection: Campaign path order 2211; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:50202
targets:
- target_id: CHEBI:50202
  path: data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml
  label: naringenin
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
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/bindingdb_targets.tsv
    role: Imported target measurements and evidence retain their source inventory
      ownership; complete raw targets are preserved without a new mechanism claim.
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
    path: data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml
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
  name: Complete offline maintained reader for naringenin
  status: passed
  required: true
  target_ids:
  - CHEBI:50202
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch222/read-selected-mechanism-guarded-001.py
    2211 8715749ac3fc8e01b4d7d0b4a76c8b13542fa0210f8aec76aaee058005ec3bf6 b63b364a932d135aa61239199423459be9e70a8858abdd25f1ac9626efce7f15
    28be4db832f40820b47da073c6ed3f945d86998f30f6335dfdc5be2d5d537856 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
    deb31a6decd5b83371e50c68e20749010ef3603bb5360f563c913df51cb754b9
  exit_code: 0
  evidence_ids:
  - bgc-2211-reader-DATA
  - bgc-2211-reader-execution
  - bgc-2211-reader-acceptance
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
  - CHEBI:50202
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
  - CHEBI:50202
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
  - CHEBI:50202
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
  - CHEBI:50202
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
  - CHEBI:50202
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
  - CHEBI:50202
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:50202
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:50202
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2211-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete owner plaintext and its full append-only curation history, read
    from this exact saved raw file.
  snapshot_sha256: 30439c876d49bfb6eab5bd078633b3ab9402e2c1c29c2db74bfbc0275c0775dc
- evidence_id: bgc-2211-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/0/owner_pin; /records/0/owner_document
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete captured owner for order 2211, with all native source fields,
    mechanism roots and history preserved.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2211-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/intakes/2211-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Actual canonical intake source identity and complete ordered input/target
    scope.
  snapshot_sha256: b63b364a932d135aa61239199423459be9e70a8858abdd25f1ac9626efce7f15
- evidence_id: bgc-2211-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-intake-ready-001.json
  locator: /status
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: ROOT acceptance of the original ten canonical intakes; no replay.
  snapshot_sha256: ffb4558e78e080f45baf4ccb369e72778c7e34de1c5b2fea82d2433818ea225a
- evidence_id: bgc-2211-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts;
    /records/0/owner_document/grounding_status; /records/0/owner_document/definition;
    /records/0/owner_document/definition_source
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Written structure, source concepts and grounding status; no external identity
    refresh.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2211-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete written producer and locus claims, including versions, evidence
    methods, grades and citation roles.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2211-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/0/owner_document/occurrences
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete written occurrences and their source labels, citations and scope
    notes.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2211-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete captured owner supports its written assay, target, summary and
    mechanism fields or their absence; this evidence does not assert omitted source-query
    content.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2211-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_classification; /records/0/owner_document/bgc_class
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Written named-model prediction and source BGC classes, retained as separate
    axes.
  snapshot_sha256: 8f3c7faa3c074d96294074f49d3ea758f9a532414e66fe32d6ef2af428173134
- evidence_id: bgc-2211-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete selected source context, direct companion paths and exact proposed
    map, later joined to actual intake.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: bgc-2211-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-scope-notes-001.json
  locator: /reading; /cautions; /curation
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Whole source-reading attribution, precise direct-context limits and bounded
    eight-table curation scan; complementary reading is explicitly attributed.
  snapshot_sha256: 462e1f8450cc46b50f7e764c6be3a6fec2300b65d200898c74a5e562934ad86e
- evidence_id: bgc-2211-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-target-input-plan-acceptance-001.json
  locator: /status; /plan; /inventory; /source_notes; /per_order
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: ROOT accepted original input plan and retained inventory/notes provenance
    with exact per-order counts.
  snapshot_sha256: 87cb8226f49b19e0cf589a83c45de342083de01cee4ee071fdbbf31209fdc719
- evidence_id: bgc-2211-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/comparisons; /records/0/smiles;
    /records/0/inchi; /records/0/atom_correspondence
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Both complete saved molecular profiles, all atom/bond/stereo/motif fields
    and literal comparison/mapping results; no new molecular parse.
  snapshot_sha256: d6777b269b79f346e064435d16f6783b96b6dc0d84d181802a8be587185ebc61
- evidence_id: bgc-2211-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds; /records/0/smiles/computed/rings;
    /records/0/smiles/computed/motifs; /records/0/smiles/computed/potential_stereo;
    /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds;
    /records/0/inchi/computed/rings; /records/0/inchi/computed/motifs; /records/0/inchi/computed/potential_stereo;
    /records/0/inchi/computed/stereo_counts; /records/0/atom_correspondence; /records/0/declared_structure
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete indexed local topology and stereochemistry in both saved forms.
    Motifs are bounded structural patterns, not residue, natural-identity or experimental
    assignments.
  snapshot_sha256: d6777b269b79f346e064435d16f6783b96b6dc0d84d181802a8be587185ebc61
- evidence_id: bgc-2211-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-chemistry-acceptance-001.json
  locator: /status; /DATA; /execution; /false_comparisons; /warning_scope
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: ROOT accepted the original twenty-form diagnostic; four global warnings
    are unassigned and no scientific identity verdict is implied.
  snapshot_sha256: ed41c7b477fc10da9308cd55cfe70fe0b682312dec7fc5d153d824d02ad41ad8
- evidence_id: bgc-2211-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-native-gates-acceptance-001.json
  locator: /status; /local_commands_passed; /selected_queue_rows; /unavailable_required_gates
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Five original local gates passed. Selected queue flags retain their literal
    scope; full QC and OAK remain unavailable.
  snapshot_sha256: c2001fae878fca8947ab9a9a883c8f4c8bb09101fd0bed77c7e7c90c4d87f9a7
- evidence_id: bgc-2211-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 1 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N"
    against the pinned mibig_compounds table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned mibig_compounds table;
    no query replay or external lookup.
- evidence_id: bgc-2211-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 1541
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":1541,"row_sha256":"fcf3412f0f632ad483e0f532e87407dcf907280c59f473e08c6f30ebb27ae506","row":{"mibig_accession":"BGC0001310","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"naringenin","compound_index":"1","smiles":"C1C(OC2=CC(=CC(=C2C1=O)O)O)C3=CC=C(C=C3)O","standard_inchi":"InChI=1S/C15H12O5/c16-9-3-1-8(2-4-9)13-7-12(19)15-11(18)5-10(17)6-14(15)20-13/h1-6,13,16-18H,7H2","standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","stereo_complete":"false","compound_classes":"","database_ids":"pubchem:932","taxon_id":"NCBITaxon:1901","taxon_label":"Streptomyces
    clavuligerus ATCC 27064","bgc_classes":"PKS","bgc_subclasses":"Type III","genome_accession":"CM000913.1","locus_from":"6460418","locus_to":"6463122","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:26553209","reference_basis":"ENTRY"}}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2211-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 1 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N"
    against the pinned chebi_structures table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned chebi_structures table;
    no query replay or external lookup.
- evidence_id: bgc-2211-source-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Physical TSV lines 13755
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":13755,"row_sha256":"641bd42fb52cc5259e7a33ca354de6bca252f99fbf01fdce9bec007bec7bfbb3","row":{"chebi_id":"CHEBI:50202","name":"naringenin","definition":"A
    trihydroxyflavanone that is flavanone substituted by hydroxy groups at positions
    5, 6 and 4''.","stars":"3","standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","smiles":"O=C1CC(c2ccc(O)cc2)Oc2cc(O)cc(O)c21"}}]'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2211-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 80 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N"
    against the pinned lotus_occurrences table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned lotus_occurrences table;
    no query replay or external lookup.
- evidence_id: bgc-2211-source-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569,
    1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582,
    1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595,
    1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608,
    1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621,
    1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634,
    1635, 1636, 1637, 1638, 1639, 1640
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":1561,"row_sha256":"b39d50a6cae38194fa823713b53b16c75f339d82af8d9f5dcb733fb703d5ac94","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus
    mume","taxon_id":"NCBITaxon:102107","organism_wikidata":"http://www.wikidata.org/entity/Q157763","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1562,"row_sha256":"1b6d11f9332797485a3f3f76578dd124db46e0530f374fe3b484c17ef54dc437","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum
    cephaloideum","taxon_id":"NCBITaxon:112358","organism_wikidata":"http://www.wikidata.org/entity/Q15578590","reference_doi":"10.1002/CBER.19731060432","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1563,"row_sha256":"3bb72bdabae82449b27045185b81d71b85d9f42a8199980c955f3a417b97fc79","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum
    cephaloideum","taxon_id":"NCBITaxon:112358","organism_wikidata":"http://www.wikidata.org/entity/Q15578590","reference_doi":"10.1515/ZNC-1983-11-1201","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1564,"row_sha256":"855f49511a01e3cbfdf01094fe992f930ba8d16ca4e90c5863f8b0f9997c1e70","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium
    fimbriatum","taxon_id":"NCBITaxon:117953","organism_wikidata":"http://www.wikidata.org/entity/Q7990065","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1565,"row_sha256":"27ab3c97e92e67751fe5fc340ee6b35e5eb828d3dc3aa876e218c7050f51fa8a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium
    loddigesii","taxon_id":"NCBITaxon:117954","organism_wikidata":"http://www.wikidata.org/entity/Q5220983","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1566,"row_sha256":"03cd6552cd3700044c87275867ac15424b32adbb530c3b09efd1ce666579d5d5","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus
    lycioides","taxon_id":"NCBITaxon:1284230","organism_wikidata":"http://www.wikidata.org/entity/Q17271747","reference_doi":"10.3390/MOLECULES17021665","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1567,"row_sha256":"d8fdec729ebd61fae6d69bd4ba5bc619303cbfe10697fb7c6aaa2b6a4e4538a8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dalbergia
    parviflora","taxon_id":"NCBITaxon:1353466","organism_wikidata":"http://www.wikidata.org/entity/Q15531989","reference_doi":"10.1039/P19730001737","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1568,"row_sha256":"dd6d4071c1f91c448a2b980a9c60507a6214d2175f54936f40c9b4434c2288c7","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus
    campanulata","taxon_id":"NCBITaxon:136465","organism_wikidata":"http://www.wikidata.org/entity/Q149633","reference_doi":"10.1021/JA01650A088","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1569,"row_sha256":"8efa39cfb904fefb646c07b34629c82bdd429d4556859b8279df52ecc3cd6b27","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Rhynchosia
    beddomei","taxon_id":"NCBITaxon:1378005","organism_wikidata":"http://www.wikidata.org/entity/Q15532686","reference_doi":"10.1016/0031-9422(80)83211-0","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1570,"row_sha256":"46e4213995dc06c8517a7b9fccc35552d83963fa0f322a75e5f16455eb939bc9","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium
    moniliforme","taxon_id":"NCBITaxon:142614","organism_wikidata":"http://www.wikidata.org/entity/Q163663","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1571,"row_sha256":"33102310498e03aa1cdced6df029450c414e24d78fe0c05c6c4fdeb322fc4c9b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium
    officinale","taxon_id":"NCBITaxon:142615","organism_wikidata":"http://www.wikidata.org/entity/Q50839974","reference_doi":"10.1155/2017/7436259","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1572,"row_sha256":"5688a5bb003d9913aaf8385fac8b1be7f5a8a2f04e9d4a32a89e14ac48fca3bf","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus
    davidiana","taxon_id":"NCBITaxon:151430","organism_wikidata":"http://www.wikidata.org/entity/Q3408638","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1573,"row_sha256":"b0608830c24c71143a9b8d3764b7269640b401508505adcade6490fa79c5cf19","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium
    chrysanthum","taxon_id":"NCBITaxon:154291","organism_wikidata":"http://www.wikidata.org/entity/Q5223343","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1574,"row_sha256":"b00c33cb3ff4b5347737d993b8ec5045ea484dbf1dab2d10fc0a0559e84902da","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium
    chrysotoxum","taxon_id":"NCBITaxon:161865","organism_wikidata":"http://www.wikidata.org/entity/Q3335823","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1575,"row_sha256":"f9f46c0c29dd8688fbf04444a372ffd919d314bee6123afcbc230291e3b9d327","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Intsia","taxon_id":"NCBITaxon:162811","organism_wikidata":"http://www.wikidata.org/entity/Q631100","reference_doi":"10.1016/0031-9422(73)80461-3","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1576,"row_sha256":"a1c8cc3085cfaed452f0aaecc888814b8a39b15e4e75fb45b047bd676d694cfd","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Brosimum
    acutifolium","taxon_id":"NCBITaxon:1835378","organism_wikidata":"http://www.wikidata.org/entity/Q15471077","reference_doi":"10.1021/NP010389J","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1577,"row_sha256":"35b222b79f86bf5ad0dfd3958922f3000f35a79aed66970dd4c6731105f1389f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Streptomyces
    clavuligerus","taxon_id":"NCBITaxon:1901","organism_wikidata":"http://www.wikidata.org/entity/Q7623381","reference_doi":"10.1186/S12934-015-0373-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1578,"row_sha256":"2fd0a0c0db35b8d41cd014dcf0bb961d949ea4d9b5a3de1063cf38e4a46e4f66","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Maclura
    cochinchinensis","taxon_id":"NCBITaxon:194324","organism_wikidata":"http://www.wikidata.org/entity/Q5402484","reference_doi":"10.1021/NP030127C","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1579,"row_sha256":"0849bd9c941a5202bab2790442eafceda37f8cb307c3125712727d4b42ffa7f7","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Maclura
    tricuspidata","taxon_id":"NCBITaxon:210328","organism_wikidata":"http://www.wikidata.org/entity/Q602322","reference_doi":"10.1016/0031-9422(95)00277-E","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1580,"row_sha256":"980b22c1c4047bb5f2c94015e0af2850d6ec71064cb438f53e68227fab6e5428","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Maclura
    tricuspidata","taxon_id":"NCBITaxon:210328","organism_wikidata":"http://www.wikidata.org/entity/Q602322","reference_doi":"10.1021/NP030127C","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1581,"row_sha256":"dcb72d18546c5712edc231de8790d683f3937acb644d557d524eeff22ee761eb","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium
    longicornu","taxon_id":"NCBITaxon:257357","organism_wikidata":"http://www.wikidata.org/entity/Q5224593","reference_doi":"10.1055/S-2008-1074492","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1582,"row_sha256":"1070ff82dd7c43a4eafc648a34b72bfca8c5f7faa947f5d337b111b7cc6ef9cb","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium
    trigonopus","taxon_id":"NCBITaxon:257360","organism_wikidata":"http://www.wikidata.org/entity/Q4037209","reference_doi":"10.1080/10286020802133605","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1583,"row_sha256":"01b039f783761a1258b66cb47f3d53c1bce3427b4fd3ecad1a960afc1fe16456","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum
    arenarium","taxon_id":"NCBITaxon:261776","organism_wikidata":"http://www.wikidata.org/entity/Q27984","reference_doi":"10.1002/CBER.19731060432","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1584,"row_sha256":"edb107c598ed9e7ac0ccefe5fa1a8182dba49df7b3f48fac928b895de17c3de4","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum
    arenarium","taxon_id":"NCBITaxon:261776","organism_wikidata":"http://www.wikidata.org/entity/Q27984","reference_doi":"10.1515/ZNC-1983-11-1201","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1585,"row_sha256":"2dcaa8d9c862c4a5da759be7ad6dcdd8a4cac10c5a68d9849739b9aa43ab6884","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Ageratina
    havanensis","taxon_id":"NCBITaxon:2773069","organism_wikidata":"http://www.wikidata.org/entity/Q4692124","reference_doi":"10.1021/NP50048A063","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1586,"row_sha256":"740a840da2dde1d7e671f6cbaacb4c35429fa9b0c8553c9c7e2478e551a58e25","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Senecio
    adenophyllus","taxon_id":"NCBITaxon:2841764","organism_wikidata":"http://www.wikidata.org/entity/Q15588331","reference_doi":"10.1016/0031-9422(77)83033-1","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1587,"row_sha256":"1775739e27c72cebe32606bd80ed26fb1d19893c477316ad549496183552d6d7","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Daphne
    aurantiaca","taxon_id":"NCBITaxon:2918710","organism_wikidata":"http://www.wikidata.org/entity/Q11122021","reference_doi":"10.1248/CPB.59.653","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1588,"row_sha256":"944187ac1f75eb0c960ba1d323efe556e031daa3094424b053f19ee1da87215d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus
    itosakura","taxon_id":"NCBITaxon:2986971","organism_wikidata":"http://www.wikidata.org/entity/Q51117378","reference_doi":"10.1021/JA01564A056","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1589,"row_sha256":"ae91be770f8ba90c45f722e82ae9a2722cb54153ddacdd2a23f870be3d6fb5f6","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Euphorbia
    hirta","taxon_id":"NCBITaxon:318062","organism_wikidata":"http://www.wikidata.org/entity/Q36177","reference_doi":"10.1248/CPB.54.1037","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1590,"row_sha256":"f5410fc7868cff75f1a2962758d1e6ad8eada122a8639ebe0c520bdfd2bc80d8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Aloe
    barbadensis","taxon_id":"NCBITaxon:34199","organism_wikidata":"http://www.wikidata.org/entity/Q50826551","reference_doi":"10.1007/S11130-020-00822-2","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1591,"row_sha256":"9fa5025709cfa74548b59c7a1e642aee2827e158c99d25facbe05a99e0a6a4c1","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Aloe
    vera","taxon_id":"NCBITaxon:34199","organism_wikidata":"http://www.wikidata.org/entity/Q80079","reference_doi":"10.1007/S11130-020-00822-2","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1592,"row_sha256":"b2498b54d18aa9709076702de82ad857c3a8c9fbdf3220c1f854cef6048421e4","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Centaurea
    pallescens","taxon_id":"NCBITaxon:363441","organism_wikidata":"http://www.wikidata.org/entity/Q15569632","reference_doi":"10.1016/S0031-9422(00)85282-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1593,"row_sha256":"5bc08152c98e79f8104d964ec04c15f8f3f630ca76b500b581268fd61ee8ce43","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus
    grandis","taxon_id":"NCBITaxon:37334","organism_wikidata":"http://www.wikidata.org/entity/Q21004587","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1594,"row_sha256":"5c3b9a131a3197b6dc1ce5057c8a2d6a44cf2696986704c51758613ab12c5341","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus
    maxima","taxon_id":"NCBITaxon:37334","organism_wikidata":"http://www.wikidata.org/entity/Q80024","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1595,"row_sha256":"b5a2255d47caa24ca4790826945026ffdf21ec98f71eb84739379daa44e40ba3","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus
    grandis","taxon_id":"NCBITaxon:37334","organism_wikidata":"http://www.wikidata.org/entity/Q21004587","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1596,"row_sha256":"57f293cd4198ad0a214f5a66496c9cee2cc68d7c66a32a6b62a02e4d630a6d85","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus
    maxima","taxon_id":"NCBITaxon:37334","organism_wikidata":"http://www.wikidata.org/entity/Q80024","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1597,"row_sha256":"057dd0131b1a56c03ae9d29c8c7cc946dceefc90e7deb3596e2fe0ed1a8777f4","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus
    persica","taxon_id":"NCBITaxon:3760","organism_wikidata":"http://www.wikidata.org/entity/Q13189","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1598,"row_sha256":"a24a5259624d3f7045cd30aaa4c806a744ebe5915543b9d1b6bee99d9265c0a8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Poncirus
    trifoliata","taxon_id":"NCBITaxon:37690","organism_wikidata":"http://www.wikidata.org/entity/Q859433","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1599,"row_sha256":"fd6e307fc453865821a0cb2b3b23f2bc15488792818d575d6ec201bd6cdbe19b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Poncirus
    trifoliata","taxon_id":"NCBITaxon:37690","organism_wikidata":"http://www.wikidata.org/entity/Q859433","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1600,"row_sha256":"6fcf8f05240169fe210df574ed6e78f340cfeaf70dfd8178b0ea51bccaae59cc","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Centaurea
    hyalolepis","taxon_id":"NCBITaxon:3769976","organism_wikidata":"http://www.wikidata.org/entity/Q1053486","reference_doi":"10.1016/S0031-9422(00)85282-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1601,"row_sha256":"733cc27a5ba77d4e765821ed6d8da2e00d67e47d9434ec9a6fd83b5949a66221","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Euphorbia
    amygdaloides","taxon_id":"NCBITaxon:38843","organism_wikidata":"http://www.wikidata.org/entity/Q149367","reference_doi":"10.1248/CPB.54.1037","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1602,"row_sha256":"d71d34f68e8295ee9a5f24f066c2414481bf5ff85108b1fadf9802d244630be0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Vigna
    angularis","taxon_id":"NCBITaxon:3914","organism_wikidata":"http://www.wikidata.org/entity/Q380279","reference_doi":"10.1080/00021369.1987.10868021","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1603,"row_sha256":"4fbc39f0b90c021e530ee958c39aec9bc3519c5541cafbfb53b9ce2c3a4e69d8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Centaurea","taxon_id":"NCBITaxon:41503","organism_wikidata":"http://www.wikidata.org/entity/Q156414","reference_doi":"10.1002/CBER.19731060707","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1604,"row_sha256":"14cb307e681be74ab3103632936fe9b6020df7b3fa7baea3b5e7b95114392ae2","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Centaurea
    calcitrapa","taxon_id":"NCBITaxon:41511","organism_wikidata":"http://www.wikidata.org/entity/Q1763537","reference_doi":"10.1016/S0031-9422(00)85282-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1605,"row_sha256":"9db73d48b222b6f7ff6075ad24304f0e9f5559f14ba74aad2353abd5934c4ae2","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Chrysanthemum
    morifolium","taxon_id":"NCBITaxon:41568","organism_wikidata":"http://www.wikidata.org/entity/Q15530181","reference_doi":"10.1002/CBER.19731061202","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1606,"row_sha256":"a202e536b94fc17a3c43816899586d6f4cffdafd991f096961762aebaec045cf","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Chrysanthemum
    morifolium","taxon_id":"NCBITaxon:41568","organism_wikidata":"http://www.wikidata.org/entity/Q15530181","reference_doi":"10.1016/0031-9422(77)83035-5","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1607,"row_sha256":"3dfce4f409d6890130485621bc39befeb96bd8470f622fa00a62f4bd8798dcd6","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus
    avium","taxon_id":"NCBITaxon:42229","organism_wikidata":"http://www.wikidata.org/entity/Q165137","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1608,"row_sha256":"460848d1526bbb35651db465c57b6b4a9a275eb504308fdd4e6f825c0366e8c9","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium
    candidum","taxon_id":"NCBITaxon:431188","organism_wikidata":"http://www.wikidata.org/entity/Q104908039","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1609,"row_sha256":"5c824489994c5bea191aef6c636430c49d900bf37355cd0e087042c49643567d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Xanthorrhoea
    preissii","taxon_id":"NCBITaxon:470286","organism_wikidata":"http://www.wikidata.org/entity/Q8043105","reference_doi":"10.1071/CH9740331","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1610,"row_sha256":"4c1ed6040d1fae29e27e7d3afb3ad98e984a100899eca25f468d9aab10254e11","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Smilax
    china","taxon_id":"NCBITaxon:49657","organism_wikidata":"http://www.wikidata.org/entity/Q163095","reference_doi":"10.1016/J.PHYTOCHEM.2008.01.002","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1611,"row_sha256":"8c67a3386bc3235c70a9b5f0faca187230bc4222c4e34f7e6021f58b05d84d07","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Xanthorrhoea
    resinosa","taxon_id":"NCBITaxon:49740","organism_wikidata":"http://www.wikidata.org/entity/Q8043107","reference_doi":"10.1071/CH9740331","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1612,"row_sha256":"586f722e6f9d24922d49393e0111e655bb29275ffba50cc6df93f5808460907d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dalbergia
    odorifera","taxon_id":"NCBITaxon:499988","organism_wikidata":"http://www.wikidata.org/entity/Q3012291","reference_doi":"10.1039/P19730001737","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1613,"row_sha256":"9f7115afc1d3891c07d2ef98bd3b534604d8f2ba58a09e27e78249e7da02451c","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus
    unshiu","taxon_id":"NCBITaxon:55188","organism_wikidata":"http://www.wikidata.org/entity/Q875262","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1614,"row_sha256":"8a95e3ad0d734cfc6f86e0ef07ba54af93edab17bd3afeb724292e9b92c92579","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus
    unshiu","taxon_id":"NCBITaxon:55188","organism_wikidata":"http://www.wikidata.org/entity/Q875262","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1615,"row_sha256":"4fda03fec348c307cd6ffe034cdc094445cf3452deb971f8032c7d911a0748bc","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus
    deliciosa","taxon_id":"NCBITaxon:558547","organism_wikidata":"http://www.wikidata.org/entity/Q20686225","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1616,"row_sha256":"111161d64f1a7fe1dea781b7d510f8a77d642fa0963599614e3ab8b18d566b20","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus
    deliciosa","taxon_id":"NCBITaxon:558547","organism_wikidata":"http://www.wikidata.org/entity/Q20686225","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1617,"row_sha256":"de694043fd646b346df585c5948c5d92507d252255145817df99f5a9c3af8cfc","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Phyllanthus","taxon_id":"NCBITaxon:58880","organism_wikidata":"http://www.wikidata.org/entity/Q310927","reference_doi":"10.1248/CPB.50.841","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1618,"row_sha256":"0e727e3900c28b5e05f7692f1db13d44686bb57265505375476503d1d2a794c0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum
    graveolens","taxon_id":"NCBITaxon:630307","organism_wikidata":"http://www.wikidata.org/entity/Q4085815","reference_doi":"10.1002/CBER.19731060432","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1619,"row_sha256":"62db8827dd6219994b23cec9f9fea1283dbcb745c61c3e39f2f63a14d0377f73","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Helichrysum
    graveolens","taxon_id":"NCBITaxon:630307","organism_wikidata":"http://www.wikidata.org/entity/Q4085815","reference_doi":"10.1515/ZNC-1983-11-1201","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1620,"row_sha256":"18804c8486cde4454c8f969cbd027781b5a574c5c4ada1bc59d91a0d04ca674a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Broussonetia","taxon_id":"NCBITaxon:66379","organism_wikidata":"http://www.wikidata.org/entity/Q600114","reference_doi":"10.1021/NP010288L","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1621,"row_sha256":"3ebbadb567e29022911d180e3f5b0a7d421fffd47a3b2aba09414b7ac970f6e5","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Lespedeza
    cyrtobotrya","taxon_id":"NCBITaxon:701533","organism_wikidata":"http://www.wikidata.org/entity/Q12618570","reference_doi":"10.1021/NP800395J","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1622,"row_sha256":"507c54170723798b0cd618f9eb1ab7be7083f724d63e55a315f2b69152f8e6ee","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Smilax
    glabra","taxon_id":"NCBITaxon:703614","organism_wikidata":"http://www.wikidata.org/entity/Q3658986","reference_doi":"10.1016/J.PHYTOCHEM.2008.01.002","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1623,"row_sha256":"f3f79b1dd267fa1c907e216e2453dfdb2e81344de0e22266a419b8cdbc2ecb3d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Artemisia
    absinthium","taxon_id":"NCBITaxon:72332","organism_wikidata":"http://www.wikidata.org/entity/Q25686","reference_doi":"10.1002/CBER.19731060919","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1624,"row_sha256":"840569efd3b4753995b781e919f7967152066db2b00285c2c0b92257ff308336","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Artemisia
    absinthium","taxon_id":"NCBITaxon:72332","organism_wikidata":"http://www.wikidata.org/entity/Q25686","reference_doi":"10.1016/S0031-9422(98)00180-0","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1625,"row_sha256":"b11085a6c6c1efba3d9e8201cc9b1748bab643dcf8db266742feccaa3a8949b3","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Artemisia
    absinthium","taxon_id":"NCBITaxon:72332","organism_wikidata":"http://www.wikidata.org/entity/Q25686","reference_doi":"10.1021/NP000005+","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1626,"row_sha256":"4e5ff9cc1167943b58e23b68d442021ac91073d9f6803daab77726163e485623","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Artemisia
    crithmifolia","taxon_id":"NCBITaxon:72340","organism_wikidata":"http://www.wikidata.org/entity/Q21871162","reference_doi":"10.1002/CBER.19731060919","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1627,"row_sha256":"b959c84c421e2851e634f3c2970c9038caec16fcc32d0c47bb28d1aa8e3cda30","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Artemisia
    crithmifolia","taxon_id":"NCBITaxon:72340","organism_wikidata":"http://www.wikidata.org/entity/Q21871162","reference_doi":"10.1021/NP000005+","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1628,"row_sha256":"f1db9115d3eeb22e86b073b6f2c7c93ba5452fd241aa0502c6ba96aff9cc81f0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Xanthorrhoea
    australis","taxon_id":"NCBITaxon:72655","organism_wikidata":"http://www.wikidata.org/entity/Q8043098","reference_doi":"10.1071/CH9740331","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1629,"row_sha256":"c5e146fca896f4125342379763edc8b41b6bd7409715fe7f349fe0b4dedccb1c","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Glycyrrhiza
    uralensis","taxon_id":"NCBITaxon:74613","organism_wikidata":"http://www.wikidata.org/entity/Q1196166","reference_doi":"10.1007/BF00574601","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1630,"row_sha256":"82c1aa1249da63c6f28f45a869f74a079b43bdd168327c8450d59772b0ac784b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Glycyrrhiza
    uralensis","taxon_id":"NCBITaxon:74613","organism_wikidata":"http://www.wikidata.org/entity/Q1196166","reference_doi":"10.1021/NP050034Q","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1631,"row_sha256":"53aa022b007dfe63ccd84092fe8425ecf8db9fe749efe2b12f5c75858a823211","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Glycyrrhiza
    inflata","taxon_id":"NCBITaxon:74614","organism_wikidata":"http://www.wikidata.org/entity/Q5572787","reference_doi":"10.1007/BF00574601","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1632,"row_sha256":"71d8d54e0585ef2121b9dba91d140906b6270c4f0cc7ae6abf6d5a811eed778a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Glycyrrhiza
    inflata","taxon_id":"NCBITaxon:74614","organism_wikidata":"http://www.wikidata.org/entity/Q5572787","reference_doi":"10.1021/NP050034Q","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1633,"row_sha256":"d77d180139ed350fedc8ec25f73dc84a594bc5cfbfde52bcf879b02de07ec463","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus
    reticulata","taxon_id":"NCBITaxon:85571","organism_wikidata":"http://www.wikidata.org/entity/Q125337","reference_doi":"10.1002/PCA.771","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1634,"row_sha256":"593cad86a1777dc27e2daea518436df5cd3c4c92a3e7e2d89158380b88d71cb3","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Citrus
    reticulata","taxon_id":"NCBITaxon:85571","organism_wikidata":"http://www.wikidata.org/entity/Q125337","reference_doi":"10.1016/S0031-9422(00)85805-7","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1635,"row_sha256":"7d665f7e52227e7f2954f56109ab26b13586bbf1f2569d8562d7a238462b5dcb","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Cadophora
    gregata","taxon_id":"NCBITaxon:86000","organism_wikidata":"http://www.wikidata.org/entity/Q104096589","reference_doi":"10.1271/BBB1961.51.349","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1636,"row_sha256":"ccaec21b765fa62927cf91c5f9f6c5dab6e9dcf2b7fc6ff8d6c6da6e8ff24ca6","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Drynaria
    roosii","taxon_id":"NCBITaxon:872542","organism_wikidata":"http://www.wikidata.org/entity/Q5309744","reference_doi":"10.1080/14786410902991860","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1637,"row_sha256":"489449a28b34452e09d643597722787dede52aa358bcf22539cf6f2441a08c1f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Dendrobium
    nobile","taxon_id":"NCBITaxon:94219","organism_wikidata":"http://www.wikidata.org/entity/Q636713","reference_doi":"10.1016/S0031-9422(01)00168-6","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1638,"row_sha256":"152ec4f5aece1787ce64c277732a7d22028df8183b369559e3174b6ad445a098","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Senna
    sophera","taxon_id":"NCBITaxon:948718","organism_wikidata":"http://www.wikidata.org/entity/Q2724545","reference_doi":"10.1248/CPB.42.2588","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1639,"row_sha256":"013d70debeff8b125fcd2b804126327e98aba2039c329fa931b1f8300ce126c9","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus
    serrulata var. spontanea","taxon_id":"NCBITaxon:97325","organism_wikidata":"http://www.wikidata.org/entity/Q3408652","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}},{"physical_line":1640,"row_sha256":"6248f3c9bde868e7ecc23639f4319bd85b6b2c0cff8f7667696267b78a0c76b3","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","organism_name":"Prunus
    serrulata f. spontanea","taxon_id":"NCBITaxon:97325","organism_wikidata":"http://www.wikidata.org/entity/Q43374956","reference_doi":"10.1021/JF980936F","structure_wikidata":"http://www.wikidata.org/entity/Q57826857"}}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2211-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 0 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N"
    against the pinned cyanometdb_occurrences table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned cyanometdb_occurrences
    table; no query replay or external lookup.
- evidence_id: bgc-2211-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 1 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N"
    against the pinned npclassifier table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned npclassifier table; no
    query replay or external lookup.
- evidence_id: bgc-2211-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 608
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":608,"row_sha256":"94b1b7471a6e3a1c947999206a36cf4d3afdd36fc10990cab630e3d43dd29f9e","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","smiles":"C1C(OC2=CC(=CC(=C2C1=O)O)O)C3=CC=C(C=C3)O","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Flavonoids","class_results":"Flavanones","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2211-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 44 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N"
    against the pinned pubchem_bioassay table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned pubchem_bioassay table;
    no query replay or external lookup.
- evidence_id: bgc-2211-source-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620,
    1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633,
    1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646,
    1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":1612,"row_sha256":"9f3fef636a3cda546d8b502acb9d1e973a4921938aad104af76db18199a6e465","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1159524","assay_name":"High
    Throughput Screening for Foot and Mouth Disease Virus Antivirals","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"14.1254","target_accession":"","reference":""}},{"physical_line":1613,"row_sha256":"0b2eae10a2bdb0bf979d152d2cc0627f0b321139c61608878aa75c912fd338c0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1452","assay_name":"qHTS
    Assay for Inhibitors of 12-hLO (12-human lipoxygenase)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"35.4813","target_accession":"NP_000688","reference":""}},{"physical_line":1614,"row_sha256":"2f92dd465ce54cae5069073d362f7369ad92adc9d9436aad5e5a931e0c68dd34","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1519","assay_name":"qHTS
    Assay for Lipid Storage Modulators","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"31.6228","target_accession":"","reference":""}},{"physical_line":1615,"row_sha256":"94cb6391bcacfb1626e663ed88db68a61457b51f35411961a513f42b6fc99d3a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1671190","assay_name":"Primary
    qHTS assay for inhibitors of human arachidonate 12S-lipoxygenase (ALOX12): Round
    2","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"44.6684","target_accession":"","reference":""}},{"physical_line":1616,"row_sha256":"f21ec8205da3f74115b82fdaae133d25af4fe394180216ff5db726dccdaf9f18","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1671190","assay_name":"Primary
    qHTS assay for inhibitors of human arachidonate 12S-lipoxygenase (ALOX12): Round
    2","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"44.6684","target_accession":"P18054","reference":""}},{"physical_line":1617,"row_sha256":"ef13c0a11cfd6506e1ae466a21d64135da57ef2dd268eda20efaab5016f5c8b8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1768","assay_name":"qHTS
    Assay for Inhibitors Targeting the Menin-MLL Interaction in MLL Related Leukemias:
    Competition With Texas Red Labeled MLL-derived Mutant Peptide","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"25.1189","target_accession":"NP_000235","reference":""}},{"physical_line":1618,"row_sha256":"362bdd1b19b0f8f31171c14a1eb42ffa90958f324f6f118a8d12fe12bf4e89c1","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1768","assay_name":"qHTS
    Assay for Inhibitors Targeting the Menin-MLL Interaction in MLL Related Leukemias:
    Competition With Texas Red Labeled MLL-derived Mutant Peptide","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"25.1189","target_accession":"NP_005924","reference":""}},{"physical_line":1619,"row_sha256":"9063e704ce2efb73279cd2a38e4be9c1e5e0f10d8276ba526d9fee386cb5a80a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1768","assay_name":"qHTS
    Assay for Inhibitors Targeting the Menin-MLL Interaction in MLL Related Leukemias:
    Competition With Texas Red Labeled MLL-derived Mutant Peptide","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"39.8107","target_accession":"NP_000235","reference":""}},{"physical_line":1620,"row_sha256":"5107003195563ca82676470a877bc51b322aff78dd3103ee14a409a653fc840b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1768","assay_name":"qHTS
    Assay for Inhibitors Targeting the Menin-MLL Interaction in MLL Related Leukemias:
    Competition With Texas Red Labeled MLL-derived Mutant Peptide","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"39.8107","target_accession":"NP_005924","reference":""}},{"physical_line":1621,"row_sha256":"4e9ae59f9626804e77f9d5c776ed468b2c71410b072f8873e1a4e7c28e9a9df6","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1797856","assay_name":"Competition-Based
    Ligand Binding Assay. from Article 10.1021/jm060692n: \"Subtle side-chain modifications
    of the hop phytoestrogen 8-prenylnaringenin result in distinct agonist/antagonist
    activity profiles for estrogen receptors alpha and beta.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Inactive","activity_name":"IC50","activity_value_um":"72.302","target_accession":"P03372","reference":"PMID:17149865"}},{"physical_line":1622,"row_sha256":"3ec858e2440383cf52f3971b33ff637e48e8e98dcee04a8d3d9a32b6f2b5bc4f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1797856","assay_name":"Competition-Based
    Ligand Binding Assay. from Article 10.1021/jm060692n: \"Subtle side-chain modifications
    of the hop phytoestrogen 8-prenylnaringenin result in distinct agonist/antagonist
    activity profiles for estrogen receptors alpha and beta.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Inactive","activity_name":"IC50","activity_value_um":"13.473","target_accession":"Q92731","reference":"PMID:17149865"}},{"physical_line":1623,"row_sha256":"a64423356600ecad90971a0d65aa802e24eb314bf3410213667ca48ec1726eb8","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1799798","assay_name":"Aromatase
    Assay from Article 10.1111/j.1747-0285.2012.01439.x: \"Neoflavonoids and Tetrahydroquinolones
    as Possible Cancer Chemopreventive Agents.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"1.09662e-06","target_accession":"P11511","reference":"PMID:22726671"}},{"physical_line":1624,"row_sha256":"dec43574955f6709cebc151b6dbf0a8ba8350a55b0956f08d4f65fc258428b9d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1801531","assay_name":"AO
    Enzyme Assay from Article 10.1016/j.bioorg.2015.12.004: \"Inhibition of guinea
    pig aldehyde oxidase activity by different flavonoid compounds: An in vitro study.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Inactive","activity_name":"Ki","activity_value_um":"148","target_accession":"H9TB17","reference":"PMID:26722818"}},{"physical_line":1625,"row_sha256":"9168dbc42a49a14366165846f619aef4d637ccc29c1c035b878dbea242e71f1f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1803217","assay_name":"Esterase
    Activity Assay from Article 10.3109/14756366.2011.651464: \"Analysis of saponins
    and phenolic compounds as inhibitors of a-carbonic anhydrase isoenzymes.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"0.97","target_accession":"P00915","reference":"PMID:22299585"}},{"physical_line":1626,"row_sha256":"8aa2c7875ef0a87c04826722d5f70752414beb8b48e3271065bce93a6ed1e8da","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1803217","assay_name":"Esterase
    Activity Assay from Article 10.3109/14756366.2011.651464: \"Analysis of saponins
    and phenolic compounds as inhibitors of a-carbonic anhydrase isoenzymes.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"0.113","target_accession":"P00918","reference":"PMID:22299585"}},{"physical_line":1627,"row_sha256":"e8612f3220e705b3de210afebfd22613b9ae7efe300ec03fcf4f2f922ec27f9f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1803217","assay_name":"Esterase
    Activity Assay from Article 10.3109/14756366.2011.651464: \"Analysis of saponins
    and phenolic compounds as inhibitors of a-carbonic anhydrase isoenzymes.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"1.12","target_accession":"P22748","reference":"PMID:22299585"}},{"physical_line":1628,"row_sha256":"35699815e513895874e31e651df931d009ecdff5654a58955a744dbc910a5d4a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1803217","assay_name":"Esterase
    Activity Assay from Article 10.3109/14756366.2011.651464: \"Analysis of saponins
    and phenolic compounds as inhibitors of a-carbonic anhydrase isoenzymes.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"1.49","target_accession":"P23280","reference":"PMID:22299585"}},{"physical_line":1629,"row_sha256":"3a11cc0c51266ce3ca7ba1fd1eb477abc692a2e7867d1da6271a53fca792fea4","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1803217","assay_name":"Esterase
    Activity Assay from Article 10.3109/14756366.2011.651464: \"Analysis of saponins
    and phenolic compounds as inhibitors of a-carbonic anhydrase isoenzymes.\"","assay_type":"Confirmatory","depositor":"BindingDB","activity_outcome":"Active","activity_name":"Ki","activity_value_um":"2.21","target_accession":"Q3SZX4","reference":"PMID:22299585"}},{"physical_line":1630,"row_sha256":"ada787db3d8afa375237d4fce81749ff5419c8c15b76938399b77f3bd6da3954","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1948","assay_name":"qHTS
    Assay for Compounds that Induce Erasure of Genomic Imprints","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"12.5893","target_accession":"","reference":""}},{"physical_line":1631,"row_sha256":"bfb4dd30830769639c968ea6bd268202313bb2e90e3915a267871961f5427511","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"1948","assay_name":"qHTS
    Assay for Compounds that Induce Erasure of Genomic Imprints","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"15.8489","target_accession":"","reference":""}},{"physical_line":1632,"row_sha256":"a2e59000768e21342f222680d333c330e81f746035a80abd2445af8fc4eb00b9","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2101","assay_name":"qHTS
    Assay for Inhibitors and Activators of N370S glucocerebrosidase as a Potential
    Chaperone Treatment of Gaucher Disease","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"11.2202","target_accession":"BAA02545","reference":""}},{"physical_line":1633,"row_sha256":"2e9cebd4e1b0f4b3fb9ad8b97f514bd2259389570c2e275caacdb755c2c2ac9c","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2101","assay_name":"qHTS
    Assay for Inhibitors and Activators of N370S glucocerebrosidase as a Potential
    Chaperone Treatment of Gaucher Disease","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"22.3872","target_accession":"BAA02545","reference":""}},{"physical_line":1634,"row_sha256":"218c6102b6a91a80e5c65c74cfb86c96ee9674b19d789b15583b455448ae7e06","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2288","assay_name":"qHTS
    Assay for Modulators of miRNAs and/orActivators of miR-21","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"9.2683","target_accession":"","reference":""}},{"physical_line":1635,"row_sha256":"74c17abacdd68986bafcf2bc30a70a6c1e93703177441041e1ea3218cce618b9","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2289","assay_name":"qHTS
    Assay for Modulators of miRNAs and/or Inhibitors of miR-21","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"9.2683","target_accession":"","reference":""}},{"physical_line":1636,"row_sha256":"e3165eb22200a8ca44dfa0262c39595cc094e4d08a6100618f740138188f92f5","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2314","assay_name":"Cycloheximide
    Counterscreen for Small Molecule Inhibitors of Shiga Toxin","assay_type":"Screening","depositor":"NCGC","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"BAC78637","reference":""}},{"physical_line":1637,"row_sha256":"712cd7082760ae0e5d94a472e15391001cf41b48410d897150937add87525b8e","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2314","assay_name":"Cycloheximide
    Counterscreen for Small Molecule Inhibitors of Shiga Toxin","assay_type":"Screening","depositor":"NCGC","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"BAC78638","reference":""}},{"physical_line":1638,"row_sha256":"4f55464a785ce2911403b63effc82d46eb197fe349c7a1a8f10fc3c4852e90a2","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2517","assay_name":"qHTS
    Assay for Inhibitors of the Human Apurinic/apyrimidinic Endonuclease 1 (APE1)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"199.526","target_accession":"1DE9_A","reference":""}},{"physical_line":1639,"row_sha256":"e8ded9e199e495f9313c7002df64df95bb7f97f5e8ab4708695ddef5cacf17bc","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2551","assay_name":"qHTS
    for inhibitors of ROR gamma transcriptional activity","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"35.4813","target_accession":"NP_035411","reference":""}},{"physical_line":1640,"row_sha256":"6ae62bb6834a956263c23cfd1dd460f0aa3ddafdf992be8c8de2ef0c2218aa6f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"2551","assay_name":"qHTS
    for inhibitors of ROR gamma transcriptional activity","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"15.8489","target_accession":"NP_035411","reference":""}},{"physical_line":1641,"row_sha256":"c9dd9fccfffffafb96eef05d7ca5e7cb1692bad2f2936aaaec105c1bda7c0dad","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"388","assay_name":"Compound
    Screen Assay, Human HPGD","assay_type":"Screening","depositor":"SGCOxCompounds","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"AAA89174","reference":""}},{"physical_line":1642,"row_sha256":"3b6ba545a68371646444ddde5e06c50fbdc6a784df4989a4d6642d2159ee23a4","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"485281","assay_name":"qHTS
    Assay for Identification of Novel General Anesthetics","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"28.1838","target_accession":"3F32_A","reference":""}},{"physical_line":1643,"row_sha256":"308c778a4dfbe36c77e6969ae60467e67fdbb7b6a5e462e2f60df69775f0bbea","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"485317","assay_name":"HTS-Luminescent
    assay for inhibitors of ALR by detection of hydrogen peroxide production Measured
    in Biochemical System Using Plate Reader - 2036-02_Inhibitor_SinglePoint_HTS","assay_type":"Screening","depositor":"Broad
    Institute","activity_outcome":"Active","activity_name":"","activity_value_um":"","target_accession":"NP_005253","reference":""}},{"physical_line":1644,"row_sha256":"e824fbcfac6aa5fda51d7027af2092b7b369f3ddee7f0d0471e5fe980e06790f","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"485367","assay_name":"qHTS
    Assay to Find Inhibitors of T. brucei phosphofructokinase","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"0.7569","target_accession":"XP_843920","reference":""}},{"physical_line":1645,"row_sha256":"0fee31af74fd9d51d32d88fa6cb6e8a49d65a82505906f17d57d83aea88c4afc","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"504832","assay_name":"Primary
    qHTS for delayed death inhibitors of the malarial parasite plastid, 48 hour incubation","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"2.6169","target_accession":"","reference":""}},{"physical_line":1646,"row_sha256":"f4d04e9dda7abaed40344bc1858836788687b7708056cdf49f5eb95fb3f7afe0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"504834","assay_name":"Primary
    qHTS for delayed death inhibitors of the malarial parasite plastid, 96 hour incubation","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"6.5733","target_accession":"","reference":""}},{"physical_line":1647,"row_sha256":"7ca9c1252b1be25bb1773f4494b77927b6ef08183150fdb4f721bc6b884024a7","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"588342","assay_name":"qHTS
    profiling assay for firefly luciferase inhibitor/activator using purifed enzyme
    and Km concentrations of substrates (counterscreen for miR-21 project)","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inconclusive","activity_name":"Potency","activity_value_um":"30.1313","target_accession":"AAA29795","reference":""}},{"physical_line":1648,"row_sha256":"35f268327a444e006c523f6a487c1ec7126c9ea818f3ed2f916c82cbe0cd5e8d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"588590","assay_name":"qHTS
    for Inhibitors of Polymerase Iota","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"0.631","target_accession":"NP_009126","reference":""}},{"physical_line":1649,"row_sha256":"137b865f92e7340574438c1adf2c678621ae578ab9c157cdeb0528cd18ffc683","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"624297","assay_name":"A
    quantitative high throughput screen for small molecules that induce DNA re-replication
    in SW480 colon adenocarcinoma cells.","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"2.5119","target_accession":"NP_056979","reference":""}},{"physical_line":1650,"row_sha256":"c0daa8bb5b9c48abae4b14e4b75b303003b206004aed0dedc3e49c72cf36d37a","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"720532","assay_name":"qHTS
    for Inhibitors of binding or entry into cells for Marburg Virus","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"35.4813","target_accession":"B45705","reference":""}},{"physical_line":1651,"row_sha256":"8debce75d6ba8474591bb974cfb27840a369bceea3073e86c59c95a1ab932d2b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"720532","assay_name":"qHTS
    for Inhibitors of binding or entry into cells for Marburg Virus","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"14.1254","target_accession":"B45705","reference":""}},{"physical_line":1652,"row_sha256":"adda963159cffb945808f36fc37871eb2820689314382687a13a16090316db03","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"884","assay_name":"qHTS
    Assay for Inhibitors and Substrates of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Active","activity_name":"Potency","activity_value_um":"10","target_accession":"NP_059488","reference":""}},{"physical_line":1653,"row_sha256":"e23b5e02a71dfacab9e964aacc448be7656e2950c83f889473b1402242b2aaa0","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"884","assay_name":"qHTS
    Assay for Inhibitors and Substrates of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Active","activity_name":"Potency","activity_value_um":"12.5893","target_accession":"NP_059488","reference":""}},{"physical_line":1654,"row_sha256":"fc1f969b8f24b7dea393883b4f4ed518baa5f38a5f762270265bf73970f7bf1b","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"885","assay_name":"qHTS
    Assay for Activators of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"10","target_accession":"NP_059488","reference":""}},{"physical_line":1655,"row_sha256":"551bc2016293417bbee2eab0dada0f1483407a7d42087f67d7b966bd0c94d6d1","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","cid":"932","aid":"885","assay_name":"qHTS
    Assay for Activators of Cytochrome P450 3A4","assay_type":"Confirmatory","depositor":"NCGC","activity_outcome":"Inactive","activity_name":"Potency","activity_value_um":"12.5893","target_accession":"NP_059488","reference":""}}]'
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2211-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 9 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N"
    against the pinned bindingdb_targets table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned bindingdb_targets table;
    no query replay or external lookup.
- evidence_id: bgc-2211-source-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/bindingdb_targets.tsv
  locator: Physical TSV lines 14, 15, 16, 17, 18, 19, 20, 21, 22
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and exact physical-frame hashes:
    [{"physical_line":14,"row_sha256":"97fe0b7aa354d44c76a818d1ab1144b642712e3651360ff065099ebf82d15d8d","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Aldehyde
    oxidase 1","target_organism":"Cavia porcellus","uniprot":"H9TB17","measurement_type":"KI","measurement_value_nm":"148000","measurement_qualifier":"EQUAL","ph":"7.0000","temperature_c":"","reference":"PMID:26722818","curation_source":"Curated
    from the literature by BindingDB"}},{"physical_line":15,"row_sha256":"fee7eda52c387c32b21984115620a25a3636066f30d606d7af67a46e7bbaa030","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Aromatase","target_organism":"Homo
    sapiens","uniprot":"P11511","measurement_type":"KI","measurement_value_nm":"0.00109662","measurement_qualifier":"EQUAL","ph":"","temperature_c":"","reference":"PMID:22726671","curation_source":"Curated
    from the literature by BindingDB"}},{"physical_line":16,"row_sha256":"759ec3ba158ca0912c9e57e98ddb4b59d887acf1ab6a365f469b204bf19a9a09","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Carbonic
    anhydrase 1","target_organism":"Homo sapiens","uniprot":"P00915","measurement_type":"KI","measurement_value_nm":"970","measurement_qualifier":"EQUAL","ph":"7.4000","temperature_c":"","reference":"PMID:22299585","curation_source":"Curated
    from the literature by BindingDB"}},{"physical_line":17,"row_sha256":"07a9e89c7719ad02277168e160de1a71445b74f73384abaddff5fda08b721884","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Carbonic
    anhydrase 2","target_organism":"Homo sapiens","uniprot":"P00918","measurement_type":"KI","measurement_value_nm":"113","measurement_qualifier":"EQUAL","ph":"7.4000","temperature_c":"","reference":"PMID:22299585","curation_source":"Curated
    from the literature by BindingDB"}},{"physical_line":18,"row_sha256":"f9ca50845f2c7c145c4ec98d0c82c4ec58e74e981771a56569a4d24fe8991be7","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Carbonic
    anhydrase 3","target_organism":"Bos taurus","uniprot":"Q3SZX4","measurement_type":"KI","measurement_value_nm":"2210","measurement_qualifier":"EQUAL","ph":"7.4000","temperature_c":"","reference":"PMID:22299585","curation_source":"Curated
    from the literature by BindingDB"}},{"physical_line":19,"row_sha256":"8179a7a41b72fbd2cef87d3d0b2e55ea23b87956484894a570d6aa25a043c68c","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Carbonic
    anhydrase 4","target_organism":"Homo sapiens","uniprot":"P22748","measurement_type":"KI","measurement_value_nm":"1120","measurement_qualifier":"EQUAL","ph":"7.4000","temperature_c":"","reference":"PMID:22299585","curation_source":"Curated
    from the literature by BindingDB"}},{"physical_line":20,"row_sha256":"9a093ad5763193868168b894f506f2ab24740b3fb92a1d0a2c3d77d349104138","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Carbonic
    anhydrase 6","target_organism":"Homo sapiens","uniprot":"P23280","measurement_type":"KI","measurement_value_nm":"1490","measurement_qualifier":"EQUAL","ph":"7.4000","temperature_c":"","reference":"PMID:22299585","curation_source":"Curated
    from the literature by BindingDB"}},{"physical_line":21,"row_sha256":"fe13f6054c429af66a36e5a0baab615d993541b7e098b986a45d9651bd125c09","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Estrogen
    receptor","target_organism":"Homo sapiens","uniprot":"P03372","measurement_type":"IC50","measurement_value_nm":"72302","measurement_qualifier":"EQUAL","ph":"7.6000","temperature_c":"22.00
    C","reference":"PMID:17149865","curation_source":"Curated from the literature
    by BindingDB"}},{"physical_line":22,"row_sha256":"bf268d38d1b853438db72e4e2536c9db874d0c0edeb3a9b79c2d5a215eed89f5","row":{"standard_inchi_key":"FTVWIRXFELQLPI-UHFFFAOYSA-N","target_name":"Estrogen
    receptor beta","target_organism":"Homo sapiens","uniprot":"Q92731","measurement_type":"IC50","measurement_value_nm":"13473","measurement_qualifier":"EQUAL","ph":"7.6000","temperature_c":"22.00
    C","reference":"PMID:17149865","curation_source":"Curated from the literature
    by BindingDB"}}]'
  snapshot_sha256: 3cff45281c35a8b14d4d7784bc4b7af80e8e27779a5667a0292f0d9b022a22c1
- evidence_id: bgc-2211-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 0 positive placements. Exact saved predicate
    exact complete standard_inchi_key equality with query "FTVWIRXFELQLPI-UHFFFAOYSA-N"
    against the pinned antibioticmech_inchikeys table; no query replay or external
    lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "FTVWIRXFELQLPI-UHFFFAOYSA-N" against the pinned antibioticmech_inchikeys
    table; no query replay or external lookup.
- evidence_id: bgc-2211-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete saved query frame with 0 positive placements. Exact saved predicate
    exact chebi_id from exact full-key structure rows with query ["CHEBI:50202"] against
    the pinned chebi_origins table; no query replay or external lookup.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
  search_scope: Exact saved predicate exact chebi_id from exact full-key structure
    rows with query ["CHEBI:50202"] against the pinned chebi_origins table; no query
    replay or external lookup.
- evidence_id: bgc-2211-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/5; /cached_taxonomy/whole_stanzas/7;
    /cached_taxonomy/whole_stanzas/15; /cached_taxonomy/whole_stanzas/16; /cached_taxonomy/whole_stanzas/17;
    /cached_taxonomy/whole_stanzas/21; /cached_taxonomy/whole_stanzas/23; /cached_taxonomy/whole_stanzas/24;
    /cached_taxonomy/whole_stanzas/26; /cached_taxonomy/whole_stanzas/29; /cached_taxonomy/whole_stanzas/30;
    /cached_taxonomy/whole_stanzas/31; /cached_taxonomy/whole_stanzas/32; /cached_taxonomy/whole_stanzas/35;
    /cached_taxonomy/whole_stanzas/36; /cached_taxonomy/whole_stanzas/37; /cached_taxonomy/whole_stanzas/38;
    /cached_taxonomy/whole_stanzas/41; /cached_taxonomy/whole_stanzas/42; /cached_taxonomy/whole_stanzas/43;
    /cached_taxonomy/whole_stanzas/44; /cached_taxonomy/whole_stanzas/45; /cached_taxonomy/whole_stanzas/46;
    /cached_taxonomy/whole_stanzas/53; /cached_taxonomy/whole_stanzas/54; /cached_taxonomy/whole_stanzas/63;
    /cached_taxonomy/whole_stanzas/66; /cached_taxonomy/whole_stanzas/68; /cached_taxonomy/whole_stanzas/71;
    /cached_taxonomy/whole_stanzas/75; /cached_taxonomy/whole_stanzas/76; /cached_taxonomy/whole_stanzas/80;
    /cached_taxonomy/whole_stanzas/83; /cached_taxonomy/whole_stanzas/84; /cached_taxonomy/whole_stanzas/85;
    /cached_taxonomy/whole_stanzas/86; /cached_taxonomy/whole_stanzas/90; /cached_taxonomy/whole_stanzas/93;
    /cached_taxonomy/whole_stanzas/99; /cached_taxonomy/whole_stanzas/101; /cached_taxonomy/whole_stanzas/110;
    /cached_taxonomy/whole_stanzas/111; /cached_taxonomy/whole_stanzas/113; /cached_taxonomy/whole_stanzas/122;
    /cached_taxonomy/whole_stanzas/128; /cached_taxonomy/whole_stanzas/131; /cached_taxonomy/whole_stanzas/132;
    /cached_taxonomy/whole_stanzas/134; /cached_taxonomy/whole_stanzas/135; /cached_taxonomy/whole_stanzas/137;
    /cached_taxonomy/whole_stanzas/139; /cached_taxonomy/whole_stanzas/140; /cached_taxonomy/whole_stanzas/145;
    /cached_taxonomy/whole_stanzas/150; /cached_taxonomy/whole_stanzas/156; /cached_taxonomy/whole_stanzas/160;
    /cached_taxonomy/whole_stanzas/162; /cached_taxonomy/whole_stanzas/169; /cached_taxonomy/whole_stanzas/178;
    /cached_taxonomy/whole_stanzas/179; /cached_taxonomy/whole_stanzas/181; /cached_taxonomy/whole_stanzas/182;
    /cached_taxonomy/whole_stanzas/184
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete personally read cached name/synonym stanzas for selected source
    taxa: [{"id":"NCBITaxon:1901","physical_line":2911,"complete_stanza":"[Term]\nid:
    NCBITaxon:1901\nname: Streptomyces clavuligerus\n\n"},{"id":"NCBITaxon:3760","physical_line":5437,"complete_stanza":"[Term]\nid:
    NCBITaxon:3760\nname: Prunus persica\nsynonym: \"Amygdalus persica\" EXACT []\nsynonym:
    \"Persica vulgaris\" EXACT []\nsynonym: \"Prunus persica var. densa\" EXACT []\n\n"},{"id":"NCBITaxon:3914","physical_line":5905,"complete_stanza":"[Term]\nid:
    NCBITaxon:3914\nname: Vigna angularis\nsynonym: \"Phaseolus angularis\" EXACT
    []\n\n"},{"id":"NCBITaxon:9606","physical_line":10335,"complete_stanza":"[Term]\nid:
    NCBITaxon:9606\nname: Homo sapiens\n\n"},{"id":"NCBITaxon:9913","physical_line":10452,"complete_stanza":"[Term]\nid:
    NCBITaxon:9913\nname: Bos taurus\nsynonym: \"Bos bovis\" EXACT []\nsynonym: \"Bos
    primigenius taurus\" EXACT []\n\n"},{"id":"NCBITaxon:10141","physical_line":10510,"complete_stanza":"[Term]\nid:
    NCBITaxon:10141\nname: Cavia porcellus\nsynonym: \"Cavia aperea porcellus\" EXACT
    []\nsynonym: \"Cavia cobaya\" EXACT []\nsynonym: \"Mus porcellus\" EXACT []\n\n"},{"id":"NCBITaxon:34199","physical_line":14887,"complete_stanza":"[Term]\nid:
    NCBITaxon:34199\nname: Aloe vera\nsynonym: \"Aloe barbadensis\" EXACT []\nsynonym:
    \"Aloe perfoliata var. vera\" EXACT []\n\n"},{"id":"NCBITaxon:37334","physical_line":16255,"complete_stanza":"[Term]\nid:
    NCBITaxon:37334\nname: Citrus maxima\nsynonym: \"Aurantium maximum\" EXACT []\nsynonym:
    \"Citrus decumana\" EXACT []\nsynonym: \"Citrus decumanus\" EXACT []\nsynonym:
    \"Citrus grandis\" EXACT []\n\n"},{"id":"NCBITaxon:37690","physical_line":16440,"complete_stanza":"[Term]\nid:
    NCBITaxon:37690\nname: Citrus trifoliata\nsynonym: \"Poncirus trifoliata\" EXACT
    []\nsynonym: \"Poncirus trifoliatus\" EXACT []\n\n"},{"id":"NCBITaxon:38843","physical_line":16879,"complete_stanza":"[Term]\nid:
    NCBITaxon:38843\nname: Euphorbia amygdaloides\n\n"},{"id":"NCBITaxon:41503","physical_line":18720,"complete_stanza":"[Term]\nid:
    NCBITaxon:41503\nname: Centaurea\nsynonym: \"Aegialophila\" EXACT []\nsynonym:
    \"Colymbada\" EXACT []\nsynonym: \"Cyanus\" EXACT []\nsynonym: \"Hyalea\" EXACT
    []\nsynonym: \"Stephanochilus\" EXACT []\n\n"},{"id":"NCBITaxon:41511","physical_line":18742,"complete_stanza":"[Term]\nid:
    NCBITaxon:41511\nname: Centaurea calcitrapa\n\n"},{"id":"NCBITaxon:41568","physical_line":18822,"complete_stanza":"[Term]\nid:
    NCBITaxon:41568\nname: Chrysanthemum x morifolium\nsynonym: \"Chrysanthemum hortorum\"
    EXACT []\nsynonym: \"Chrysanthemum morifolium\" EXACT []\nsynonym: \"Dendranthema
    grandiflora\" EXACT []\nsynonym: \"Dendranthema morifolium\" EXACT []\nsynonym:
    \"Dendranthema x grandiflorum\" EXACT []\nsynonym: \"Dendranthema x morifolium\"
    EXACT []\nsynonym: \"Matricaria morifolia\" EXACT []\n\n"},{"id":"NCBITaxon:42229","physical_line":19307,"complete_stanza":"[Term]\nid:
    NCBITaxon:42229\nname: Prunus avium\nsynonym: \"Cerasus avium\" EXACT []\nsynonym:
    \"Prunus cerasus var. avium\" EXACT []\n\n"},{"id":"NCBITaxon:49657","physical_line":22590,"complete_stanza":"[Term]\nid:
    NCBITaxon:49657\nname: Smilax china\n\n"},{"id":"NCBITaxon:49740","physical_line":22645,"complete_stanza":"[Term]\nid:
    NCBITaxon:49740\nname: Xanthorrhoea resinosa\nsynonym: \"Xanthorrhoea hastilis\"
    EXACT []\n\n"},{"id":"NCBITaxon:55188","physical_line":25581,"complete_stanza":"[Term]\nid:
    NCBITaxon:55188\nname: Citrus unshiu\nsynonym: \"Citrus nobilis var. unshiu\"
    EXACT []\nsynonym: \"Citrus unshiu var. praecox\" EXACT []\n\n"},{"id":"NCBITaxon:58880","physical_line":27031,"complete_stanza":"[Term]\nid:
    NCBITaxon:58880\nname: Phyllanthus\nsynonym: \"Reverchonia\" EXACT []\n\n"},{"id":"NCBITaxon:66379","physical_line":29521,"complete_stanza":"[Term]\nid:
    NCBITaxon:66379\nname: Broussonetia\n\n"},{"id":"NCBITaxon:72332","physical_line":32504,"complete_stanza":"[Term]\nid:
    NCBITaxon:72332\nname: Artemisia absinthium\n\n"},{"id":"NCBITaxon:72340","physical_line":32532,"complete_stanza":"[Term]\nid:
    NCBITaxon:72340\nname: Artemisia crithmifolia\n\n"},{"id":"NCBITaxon:72655","physical_line":32704,"complete_stanza":"[Term]\nid:
    NCBITaxon:72655\nname: Xanthorrhoea australis\n\n"},{"id":"NCBITaxon:74613","physical_line":33600,"complete_stanza":"[Term]\nid:
    NCBITaxon:74613\nname: Glycyrrhiza uralensis\n\n"},{"id":"NCBITaxon:74614","physical_line":33604,"complete_stanza":"[Term]\nid:
    NCBITaxon:74614\nname: Glycyrrhiza inflata\n\n"},{"id":"NCBITaxon:85571","physical_line":37630,"complete_stanza":"[Term]\nid:
    NCBITaxon:85571\nname: Citrus reticulata\nsynonym: \"Citrus poonensis\" EXACT
    []\n\n"},{"id":"NCBITaxon:86000","physical_line":37858,"complete_stanza":"[Term]\nid:
    NCBITaxon:86000\nname: Cadophora gregata f. sp. adzukicola\nsynonym: \"Phialophora
    gregata f. sp. adzukicola\" EXACT []\n\n"},{"id":"NCBITaxon:94219","physical_line":40124,"complete_stanza":"[Term]\nid:
    NCBITaxon:94219\nname: Dendrobium nobile\n\n"},{"id":"NCBITaxon:97325","physical_line":40715,"complete_stanza":"[Term]\nid:
    NCBITaxon:97325\nname: Prunus jamasakura\nsynonym: \"Cerasus jamasakura\" EXACT
    []\nsynonym: \"Prunus serrulata f. spontanea\" EXACT []\nsynonym: \"Prunus serrulata
    var. spontanea\" EXACT []\n\n"},{"id":"NCBITaxon:102107","physical_line":41949,"complete_stanza":"[Term]\nid:
    NCBITaxon:102107\nname: Prunus mume\nsynonym: \"Armeniaca mume\" EXACT []\n\n"},{"id":"NCBITaxon:112358","physical_line":44405,"complete_stanza":"[Term]\nid:
    NCBITaxon:112358\nname: Helichrysum cephaloideum\n\n"},{"id":"NCBITaxon:117953","physical_line":45581,"complete_stanza":"[Term]\nid:
    NCBITaxon:117953\nname: Dendrobium fimbriatum\n\n"},{"id":"NCBITaxon:117954","physical_line":45585,"complete_stanza":"[Term]\nid:
    NCBITaxon:117954\nname: Dendrobium loddigesii\n\n"},{"id":"NCBITaxon:136465","physical_line":49480,"complete_stanza":"[Term]\nid:
    NCBITaxon:136465\nname: Prunus campanulata\nsynonym: \"Cerasus campanulata\" EXACT
    []\nsynonym: \"Prunus cerasoides var. campanulata\" EXACT []\n\n"},{"id":"NCBITaxon:142614","physical_line":51061,"complete_stanza":"[Term]\nid:
    NCBITaxon:142614\nname: Dendrobium moniliforme\nsynonym: \"Epidendrum moniliforme\"
    EXACT []\n\n"},{"id":"NCBITaxon:142615","physical_line":51066,"complete_stanza":"[Term]\nid:
    NCBITaxon:142615\nname: Dendrobium officinale\nsynonym: \"Dendrobium funiushanense\"
    EXACT []\nsynonym: \"Dendrobium tosaense\" EXACT []\n\n"},{"id":"NCBITaxon:151430","physical_line":52673,"complete_stanza":"[Term]\nid:
    NCBITaxon:151430\nname: Prunus davidiana\nsynonym: \"Amygdalus davidiana\" EXACT
    []\nsynonym: \"Persica davidiana\" EXACT []\n\n"},{"id":"NCBITaxon:154291","physical_line":53456,"complete_stanza":"[Term]\nid:
    NCBITaxon:154291\nname: Dendrobium chrysanthum\n\n"},{"id":"NCBITaxon:161865","physical_line":55319,"complete_stanza":"[Term]\nid:
    NCBITaxon:161865\nname: Dendrobium chrysotoxum\n\n"},{"id":"NCBITaxon:162811","physical_line":55653,"complete_stanza":"[Term]\nid:
    NCBITaxon:162811\nname: Intsia\n\n"},{"id":"NCBITaxon:194324","physical_line":62977,"complete_stanza":"[Term]\nid:
    NCBITaxon:194324\nname: Maclura cochinchinensis\nsynonym: \"Cudrania cochinchinensis\"
    EXACT []\n\n"},{"id":"NCBITaxon:210328","physical_line":66395,"complete_stanza":"[Term]\nid:
    NCBITaxon:210328\nname: Maclura tricuspidata\nsynonym: \"Cudrania tricuspidata\"
    EXACT []\n\n"},{"id":"NCBITaxon:257357","physical_line":73411,"complete_stanza":"[Term]\nid:
    NCBITaxon:257357\nname: Dendrobium longicornu\n\n"},{"id":"NCBITaxon:257360","physical_line":73415,"complete_stanza":"[Term]\nid:
    NCBITaxon:257360\nname: Dendrobium trigonopus\n\n"},{"id":"NCBITaxon:261776","physical_line":74253,"complete_stanza":"[Term]\nid:
    NCBITaxon:261776\nname: Helichrysum arenarium\nsynonym: \"Gnaphalium arenarium\"
    EXACT []\n\n"},{"id":"NCBITaxon:318062","physical_line":82057,"complete_stanza":"[Term]\nid:
    NCBITaxon:318062\nname: Euphorbia hirta\nsynonym: \"Chamaesyce hirta\" EXACT []\nsynonym:
    \"Euphorbia pilulifera\" EXACT []\n\n"},{"id":"NCBITaxon:363441","physical_line":86836,"complete_stanza":"[Term]\nid:
    NCBITaxon:363441\nname: Centaurea pallescens\n\n"},{"id":"NCBITaxon:431188","physical_line":93240,"complete_stanza":"[Term]\nid:
    NCBITaxon:431188\nname: Dendrobium candidum\n\n"},{"id":"NCBITaxon:470286","physical_line":97012,"complete_stanza":"[Term]\nid:
    NCBITaxon:470286\nname: Xanthorrhoea preissii\n\n"},{"id":"NCBITaxon:499988","physical_line":99242,"complete_stanza":"[Term]\nid:
    NCBITaxon:499988\nname: Dalbergia odorifera\n\n"},{"id":"NCBITaxon:558547","physical_line":102314,"complete_stanza":"[Term]\nid:
    NCBITaxon:558547\nname: Citrus x aurantium f. deliciosa\nsynonym: \"Citrus deliciosa\"
    EXACT []\nsynonym: \"Citrus nobilis var. deliciosa\" EXACT []\nsynonym: \"Citrus
    reticulata subsp. deliciosa\" EXACT []\n\n"},{"id":"NCBITaxon:630307","physical_line":104857,"complete_stanza":"[Term]\nid:
    NCBITaxon:630307\nname: Helichrysum graveolens\nsynonym: \"Gnaphalium graveolens\"
    EXACT []\n\n"},{"id":"NCBITaxon:701533","physical_line":108331,"complete_stanza":"[Term]\nid:
    NCBITaxon:701533\nname: Lespedeza cyrtobotrya\n\n"},{"id":"NCBITaxon:703614","physical_line":108412,"complete_stanza":"[Term]\nid:
    NCBITaxon:703614\nname: Smilax glabra\n\n"},{"id":"NCBITaxon:872542","physical_line":111649,"complete_stanza":"[Term]\nid:
    NCBITaxon:872542\nname: Aglaomorpha fortunei\nsynonym: \"Drynaria fortunei (Kunze
    ex Mett.) J.Sm., 1857, non T.Moore, 1855\" EXACT []\nsynonym: \"Drynaria roosii\"
    EXACT []\nsynonym: \"Polypodium fortunei\" EXACT []\n\n"},{"id":"NCBITaxon:948718","physical_line":113769,"complete_stanza":"[Term]\nid:
    NCBITaxon:948718\nname: Senna sophera\nsynonym: \"Cassia sophera\" EXACT []\n\n"},{"id":"NCBITaxon:1284230","physical_line":125248,"complete_stanza":"[Term]\nid:
    NCBITaxon:1284230\nname: Prunus lycioides\nsynonym: \"Amygdalus horrida\" EXACT
    []\nsynonym: \"Amygdalus lycioides\" EXACT []\nsynonym: \"Amygdalus lycioides
    Spach\" EXACT []\nsynonym: \"Amygdalus lycioides var. horrida\" EXACT []\nsynonym:
    \"Amygdalus lycioides var. lycioides\" EXACT []\n\n"},{"id":"NCBITaxon:1353466","physical_line":127313,"complete_stanza":"[Term]\nid:
    NCBITaxon:1353466\nname: Dalbergia parviflora\n\n"},{"id":"NCBITaxon:1378005","physical_line":127692,"complete_stanza":"[Term]\nid:
    NCBITaxon:1378005\nname: Rhynchosia beddomei\n\n"},{"id":"NCBITaxon:1835378","physical_line":139240,"complete_stanza":"[Term]\nid:
    NCBITaxon:1835378\nname: Brosimum acutifolium\n\n"},{"id":"NCBITaxon:2773069","physical_line":151344,"complete_stanza":"[Term]\nid:
    NCBITaxon:2773069\nname: Ageratina havanensis\nsynonym: \"Eupatorium havanense\"
    EXACT []\n\n"},{"id":"NCBITaxon:2841764","physical_line":152628,"complete_stanza":"[Term]\nid:
    NCBITaxon:2841764\nname: Senecio adenophyllus\n\n"},{"id":"NCBITaxon:2918710","physical_line":153877,"complete_stanza":"[Term]\nid:
    NCBITaxon:2918710\nname: Daphne aurantiaca\n\n"},{"id":"NCBITaxon:2986971","physical_line":154862,"complete_stanza":"[Term]\nid:
    NCBITaxon:2986971\nname: Prunus itosakura\nsynonym: \"Cerasus itosakura\" EXACT
    []\nsynonym: \"Prunus taiwaniana\" EXACT []\n\n"},{"id":"NCBITaxon:3769976","physical_line":161829,"complete_stanza":"[Term]\nid:
    NCBITaxon:3769976\nname: Centaurea hyalolepis\n\n"}]. No hierarchy or fresh taxonomy
    verification is inferred.'
  snapshot_sha256: 050759ee81e134a5c80d93845e5d3c7f8a92e971733d27fe90f7a095107e1554
- evidence_id: bgc-2211-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222-tentative/bgc-prep/bgc-conditional222-target-input-plan-001.json
  locator: /records/0/source_scope_inventory/source_taxa; /records/0/source_scope_inventory/forward_taxon_merge_matches;
    /records/0/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Exact saved source-taxon and forward-merge/nonorganism route lists. No
    selected forward-merge or nonorganism match is retained.
  snapshot_sha256: 9bb9f8fa7c09f7684412974e84449711c4ea7bb3180d6243703e8dc935f89d9a
- evidence_id: bgc-2211-review-skill
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Workflow; Output
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Immutable claim-level review, local evidence scope, honest partial completion
    and actionable ownership.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2211-review-profile
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Complete maintained review profile
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Source qualification, producer/occurrence distinctions, computed-classification
    limits and evidence-backed issue normalization.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2211-structure-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 376–432
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Structure and stereo encoding plus explicitly computed NPClassifier fields;
    model outputs are not source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2211-activity-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 632–665; lines 920–947
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Optional observation activity_class and coarse activity buckets require
    backing; no dedicated cytotoxic or enzyme-inhibitor definition is supplied.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2211-activity-classifier
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 127–179; lines 1310–1382
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Maintained classifier unambiguity intent, generic title patterns, ACTIVE-only
    class assignment and written-observation summary derivation.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2211-definition-owner
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 985–1005
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Maintained seeder copies a unique retained ChEBI definition and its source
    identifier; a correction must preserve honest provenance.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2211-reader-DATA
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-naringenin-maintained-reader-DATA-001.json
  locator: /resolved_view; /raw_owner; /expected_view; /counts; /returned_view_equals_expected_complete_owner;
    /review_check_metadata
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Complete original maintained owner view equals the captured owner, preserving
    every graph/pathway/target/history field; no scientific evidence is upgraded by
    reader success.
  snapshot_sha256: 8c01fd74594f4f6dc3cbdf618e1ea33460c2eb26be7408b2ff5442a515706e8c
- evidence_id: bgc-2211-reader-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-naringenin-reader-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /original_tool
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: Original maintained-reader execution receipt, streams and exact invocation
    provenance.
  snapshot_sha256: 21518d9209e83a3171b0cb1dbbb57b31b9e2d847ffc130a5cb0e1d188d9e0c7e
- evidence_id: bgc-2211-reader-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/root-naringenin-maintained-reader-acceptance-001.json
  locator: /status; /verification; /review_check_contract
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: ROOT acceptance of exact complete-owner/positive-content equality and original
    terminal success; expected capability construction was denied before action, with
    no external request.
  snapshot_sha256: f2f70ea3702892b5b32d9c813f30c54ce5ccd473bc274a6b109e5934d50b4925
- evidence_id: bgc-2211-graph-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-naringenin-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/0
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete graph naringenin-carbonic-anhydrase-inhibition: 6 node placements
    and 5 edges, every evidence item and limitation retained. Retained graph description:
    Naringenin inhibits human and bovine carbonic anhydrase isoenzymes.'
  snapshot_sha256: 8c01fd74594f4f6dc3cbdf618e1ea33460c2eb26be7408b2ff5442a515706e8c
- evidence_id: bgc-2211-graph-1
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-naringenin-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/1
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: 'Complete graph naringenin-aromatase-inhibition: 2 node placements and
    1 edges, every evidence item and limitation retained. Retained graph description:
    Naringenin inhibits human aromatase.'
  snapshot_sha256: 8c01fd74594f4f6dc3cbdf618e1ea33460c2eb26be7408b2ff5442a515706e8c
- evidence_id: bgc-2211-targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch222/native-current222-naringenin-maintained-reader-DATA-001.json
  locator: /resolved_view/molecular_targets
  accessed_at: '2026-11-03T12:24:37.669560Z'
  support: supports
  summary: All nine retained affinity targets with exact protein/taxon/measurement/qualifier/reference
    scope; no unique-experiment or fresh protein-identity claim.
  snapshot_sha256: 8c01fd74594f4f6dc3cbdf618e1ea33460c2eb26be7408b2ff5442a515706e8c
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
- assessment_id: bgc-2211-identity
  area: identity
  topic: Identity
  outcome: concern
  summary: The complete key FTVWIRXFELQLPI-UHFFFAOYSA-N joins MIBiG BGC0001310 v5
    and the retained three-star CHEBI:50202 row. Both stored forms and that row encode
    5,7,4′-trihydroxyflavanone, but the owner and retained definition say 5,6,4′.
    This is a supported definition–structure conflict, not evidence that the stored
    structure should be replaced. No enantiomer-specific natural identity is established.
  target_ids:
  - CHEBI:50202
  evidence_ids:
  - bgc-2211-owner
  - bgc-2211-capture
  - bgc-2211-intake
  - bgc-2211-grounding-owner
  - bgc-2211-source-plan
  - bgc-2211-plan-acceptance
  - bgc-2211-query-chebi_structures
  - bgc-2211-source-chebi_structures
  - bgc-2211-source-mibig_compounds
  - bgc-2211-chemistry
  - bgc-2211-topology
  - bgc-2211-definition-owner
  dimensions:
  - name: standard_inchi_key
    value: FTVWIRXFELQLPI-UHFFFAOYSA-N
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2211-owner
    - bgc-2211-capture
    - bgc-2211-intake
    - bgc-2211-grounding-owner
    - bgc-2211-source-plan
    - bgc-2211-plan-acceptance
    - bgc-2211-query-chebi_structures
    - bgc-2211-source-chebi_structures
    - bgc-2211-source-mibig_compounds
    - bgc-2211-chemistry
    - bgc-2211-topology
    - bgc-2211-definition-owner
  - name: grounding_scope
    value: Exact retained grounding is preserved; the definition locant conflicts
      with its own structure.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2211-owner
    - bgc-2211-capture
    - bgc-2211-intake
    - bgc-2211-grounding-owner
    - bgc-2211-source-plan
    - bgc-2211-plan-acceptance
    - bgc-2211-query-chebi_structures
    - bgc-2211-source-chebi_structures
    - bgc-2211-source-mibig_compounds
    - bgc-2211-chemistry
    - bgc-2211-topology
    - bgc-2211-definition-owner
- assessment_id: bgc-2211-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both saved forms give neutral C15H12O5, 20 atoms and 22 bonds; all ten
    comparisons are true and the saved atom correspondence is complete. The tetrahedral
    C2 centre is unspecified in both forms, consistent with stereo_complete=false.
    The diagnostic explicitly does not establish full graph or natural identity; neither
    the key nor generic name selects an enantiomer.
  target_ids:
  - CHEBI:50202
  evidence_ids:
  - bgc-2211-chemistry
  - bgc-2211-topology
  - bgc-2211-diagnostic-acceptance
  - bgc-2211-structure-schema
  dimensions:
  - name: stereochemistry_scope
    value: One unspecified tetrahedral centre at flavanone C2 in each form.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2211-chemistry
    - bgc-2211-topology
    - bgc-2211-diagnostic-acceptance
    - bgc-2211-structure-schema
  - name: representation_correspondence
    value: Ten comparisons true; complete saved match, with independent full-graph
      identity unestablished.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2211-chemistry
    - bgc-2211-topology
    - bgc-2211-diagnostic-acceptance
    - bgc-2211-structure-schema
- assessment_id: bgc-2211-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: The imported BGC0001310 v5 producer is SOURCE_ASSERTION and its locus CLUSTER_UNSTATED,
    with no stated locus method. The label includes ATCC 27064, while taxon 1901 is
    the cached Streptomyces clavuligerus species concept; the strain wording is not
    a separate verified strain identity. The many plant/fungal occurrence assertions
    remain distinct from this bacterial producer claim and from one another.
  target_ids:
  - CHEBI:50202
  evidence_ids:
  - bgc-2211-origin-owner
  - bgc-2211-occurrence-owner
  - bgc-2211-source-mibig_compounds
  - bgc-2211-source-lotus_occurrences
  - bgc-2211-cached-taxonomy
  - bgc-2211-source-routes
  - bgc-2211-review-profile
  - bgc-2211-reader-DATA
  - bgc-2211-reader-execution
  - bgc-2211-reader-acceptance
  - bgc-2211-graph-0
  - bgc-2211-graph-1
  - bgc-2211-targets
  dimensions:
  - name: taxon_scope
    value: Source taxon 1901 is species-level despite strain text; occurrence taxa
      retain their own scopes.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2211-origin-owner
    - bgc-2211-occurrence-owner
    - bgc-2211-source-mibig_compounds
    - bgc-2211-source-lotus_occurrences
    - bgc-2211-cached-taxonomy
    - bgc-2211-source-routes
    - bgc-2211-review-profile
    - bgc-2211-reader-DATA
    - bgc-2211-reader-execution
    - bgc-2211-reader-acceptance
    - bgc-2211-graph-0
    - bgc-2211-graph-1
    - bgc-2211-targets
  - name: producer_evidence
    value: SOURCE_ASSERTION from MIBiG v5; no fresh producer experiment verified.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2211-origin-owner
    - bgc-2211-occurrence-owner
    - bgc-2211-source-mibig_compounds
    - bgc-2211-source-lotus_occurrences
    - bgc-2211-cached-taxonomy
    - bgc-2211-source-routes
    - bgc-2211-review-profile
    - bgc-2211-reader-DATA
    - bgc-2211-reader-execution
    - bgc-2211-reader-acceptance
    - bgc-2211-graph-0
    - bgc-2211-graph-1
    - bgc-2211-targets
  - name: locus_evidence
    value: BGC0001310 CLUSTER_UNSTATED; no complete biosynthetic pathway inferred.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2211-origin-owner
    - bgc-2211-occurrence-owner
    - bgc-2211-source-mibig_compounds
    - bgc-2211-source-lotus_occurrences
    - bgc-2211-cached-taxonomy
    - bgc-2211-source-routes
    - bgc-2211-review-profile
    - bgc-2211-reader-DATA
    - bgc-2211-reader-execution
    - bgc-2211-reader-acceptance
    - bgc-2211-graph-0
    - bgc-2211-graph-1
    - bgc-2211-targets
- assessment_id: bgc-2211-citations
  area: evidence
  topic: Citations
  outcome: unknown
  summary: PMID:26553209 is the imported MIBiG entry reference. The carbonic-anhydrase
    graph cites DOI:10.3109/14756366.2011.651464 and the aromatase graph DOI:10.1111/j.1747-0285.2012.01439.x;
    their PRIMARY_EXPERIMENT labels are retained historical annotations, not newly
    inspected papers. BindingDB-deposited PubChem and BindingDB target rows share
    publications and may describe the same experiments. Repeated LOTUS taxa/citations
    are not independent confirmations.
  target_ids:
  - CHEBI:50202
  evidence_ids:
  - bgc-2211-origin-owner
  - bgc-2211-occurrence-owner
  - bgc-2211-assay-owner
  - bgc-2211-source-mibig_compounds
  - bgc-2211-source-lotus_occurrences
  - bgc-2211-source-pubchem_bioassay
  - bgc-2211-source-bindingdb_targets
  - bgc-2211-reader-DATA
  - bgc-2211-reader-execution
  - bgc-2211-reader-acceptance
  - bgc-2211-graph-0
  - bgc-2211-graph-1
  - bgc-2211-targets
  dimensions:
  - name: citation_scope
    value: Entry, occurrence, affinity and historical graph references have different
      roles; overlap is preserved.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2211-origin-owner
    - bgc-2211-occurrence-owner
    - bgc-2211-assay-owner
    - bgc-2211-source-mibig_compounds
    - bgc-2211-source-lotus_occurrences
    - bgc-2211-source-pubchem_bioassay
    - bgc-2211-source-bindingdb_targets
    - bgc-2211-reader-DATA
    - bgc-2211-reader-execution
    - bgc-2211-reader-acceptance
    - bgc-2211-graph-0
    - bgc-2211-graph-1
    - bgc-2211-targets
- assessment_id: bgc-2211-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: concern
  summary: The owner writes 25 of 44 retained assay placements and 25 occurrences
    with an explicit 51-further-occurrence note. Nine BindingDB targets are separately
    retained. Written assay[2], AID1799798, is an ACTIVE aromatase Ki of 1.09662e−06
    µM, yet it is typed CYTOTOXIC from cancer wording in the article title. That class
    and its sole written summary backing lack a cytotoxic measurement. Preserve the
    exact value, qualifier and overlapping 0.00109662 nM target/graph assertion; its
    surprising magnitude is not a licence to repair it by intuition. Five carbonic-anhydrase
    assays separately support ENZYME_INHIBITOR.
  target_ids:
  - CHEBI:50202
  evidence_ids:
  - bgc-2211-assay-owner
  - bgc-2211-occurrence-owner
  - bgc-2211-query-lotus_occurrences
  - bgc-2211-source-lotus_occurrences
  - bgc-2211-query-chebi_origins
  - bgc-2211-query-pubchem_bioassay
  - bgc-2211-source-pubchem_bioassay
  - bgc-2211-query-bindingdb_targets
  - bgc-2211-source-bindingdb_targets
  - bgc-2211-query-antibioticmech_inchikeys
  - bgc-2211-source-plan
  - bgc-2211-source-routes
  - bgc-2211-cached-taxonomy
  - bgc-2211-activity-classifier
  - bgc-2211-activity-schema
  - bgc-2211-reader-DATA
  - bgc-2211-reader-execution
  - bgc-2211-reader-acceptance
  - bgc-2211-graph-0
  - bgc-2211-graph-1
  - bgc-2211-targets
  dimensions:
  - name: occurrence_scope
    value: 25 written occurrences plus 51 noted omissions; source synonyms/repeated
      citations are not independent studies.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2211-assay-owner
    - bgc-2211-occurrence-owner
    - bgc-2211-query-lotus_occurrences
    - bgc-2211-source-lotus_occurrences
    - bgc-2211-query-chebi_origins
    - bgc-2211-query-pubchem_bioassay
    - bgc-2211-source-pubchem_bioassay
    - bgc-2211-query-bindingdb_targets
    - bgc-2211-source-bindingdb_targets
    - bgc-2211-query-antibioticmech_inchikeys
    - bgc-2211-source-plan
    - bgc-2211-source-routes
    - bgc-2211-cached-taxonomy
    - bgc-2211-activity-classifier
    - bgc-2211-activity-schema
    - bgc-2211-reader-DATA
    - bgc-2211-reader-execution
    - bgc-2211-reader-acceptance
    - bgc-2211-graph-0
    - bgc-2211-graph-1
    - bgc-2211-targets
  - name: assay_target_scope
    value: One unsupported CYTOTOXIC class; preserve all calls, quantities and 19
      omitted-assay boundary.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2211-assay-owner
    - bgc-2211-occurrence-owner
    - bgc-2211-query-lotus_occurrences
    - bgc-2211-source-lotus_occurrences
    - bgc-2211-query-chebi_origins
    - bgc-2211-query-pubchem_bioassay
    - bgc-2211-source-pubchem_bioassay
    - bgc-2211-query-bindingdb_targets
    - bgc-2211-source-bindingdb_targets
    - bgc-2211-query-antibioticmech_inchikeys
    - bgc-2211-source-plan
    - bgc-2211-source-routes
    - bgc-2211-cached-taxonomy
    - bgc-2211-activity-classifier
    - bgc-2211-activity-schema
    - bgc-2211-reader-DATA
    - bgc-2211-reader-execution
    - bgc-2211-reader-acceptance
    - bgc-2211-graph-0
    - bgc-2211-graph-1
    - bgc-2211-targets
- assessment_id: bgc-2211-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The complete tables show a flavanone carbonyl, one heterocyclic ether and
    three phenolic OH groups, without a sugar ring. For SMILES atom indices, O1=2,
    C2=1, C3=0, C4=9 and C4a=8; the fused aromatic path is C5=7 bearing O11, C6=6
    bearing H, C7=5 bearing O12, C8=4 bearing H, C8a=3. The pendant-ring para carbon
    16 bears O19. Thus the OH locants are 5,7,4′. NPClassifier Flavanones and non-glycoside
    output are model predictions assessed against this topology, not experimental
    origin evidence.
  target_ids:
  - CHEBI:50202
  evidence_ids:
  - bgc-2211-classification-owner
  - bgc-2211-source-npclassifier
  - bgc-2211-source-mibig_compounds
  - bgc-2211-chemistry
  - bgc-2211-topology
  - bgc-2211-review-profile
  - bgc-2211-source-chebi_structures
  - bgc-2211-definition-owner
  dimensions:
  - name: classification_applicability
    value: Saved indexed topology supports flavanone 5,7,4′ substitution and no glycoside
      assignment.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2211-classification-owner
    - bgc-2211-source-npclassifier
    - bgc-2211-source-mibig_compounds
    - bgc-2211-chemistry
    - bgc-2211-topology
    - bgc-2211-review-profile
    - bgc-2211-source-chebi_structures
    - bgc-2211-definition-owner
- assessment_id: bgc-2211-completion
  area: completeness
  topic: Completion
  outcome: concern
  summary: Supported local curation findings remain open; the scientific verdict is
    needs_curation. Complete owner/history, selected/direct source context, actual
    intake and all paired saved molecular tables were reviewed. The complete maintained
    reader result was separately accepted. Five local gates passed, while full QC,
    OAK and external primary-source/taxonomy/sequence verification remain unavailable.
    This review is partial; no source record or native curation status was changed.
  target_ids:
  - CHEBI:50202
  evidence_ids:
  - bgc-2211-owner
  - bgc-2211-intake
  - bgc-2211-intake-acceptance
  - bgc-2211-source-notes
  - bgc-2211-native-acceptance
  - bgc-2211-diagnostic-acceptance
  - bgc-2211-source-plan
  - bgc-2211-plan-acceptance
  - bgc-2211-review-skill
  - bgc-2211-review-profile
  - bgc-2211-reader-DATA
  - bgc-2211-reader-execution
  - bgc-2211-reader-acceptance
  - bgc-2211-graph-0
  - bgc-2211-graph-1
  - bgc-2211-targets
  dimensions:
  - name: review_completion
    value: Partial; open supported curation findings; external verification, full
      QC and OAK unavailable.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2211-owner
    - bgc-2211-intake
    - bgc-2211-intake-acceptance
    - bgc-2211-source-notes
    - bgc-2211-native-acceptance
    - bgc-2211-diagnostic-acceptance
    - bgc-2211-source-plan
    - bgc-2211-plan-acceptance
    - bgc-2211-review-skill
    - bgc-2211-review-profile
    - bgc-2211-reader-DATA
    - bgc-2211-reader-execution
    - bgc-2211-reader-acceptance
    - bgc-2211-graph-0
    - bgc-2211-graph-1
    - bgc-2211-targets
- assessment_id: bgc-2211-mechanism
  area: graph
  topic: Mechanism
  outcome: unknown
  summary: The complete maintained view preserves two bioactivity graphs with eight
    node placements, six edges and nine molecular targets, without components or biosynthetic
    steps. Five edges retain isoenzyme-specific carbonic-anhydrase inhibition and
    one retains the aromatase claim. These local source assertions do not establish
    an entire therapeutic mechanism, cellular cytotoxicity, a natural enantiomer,
    or independent experiments for overlapping database rows. No graph is treated
    as fresh primary-source verification.
  target_ids:
  - CHEBI:50202
  evidence_ids:
  - bgc-2211-reader-DATA
  - bgc-2211-reader-execution
  - bgc-2211-reader-acceptance
  - bgc-2211-graph-0
  - bgc-2211-graph-1
  - bgc-2211-targets
  - bgc-2211-assay-owner
  - bgc-2211-source-pubchem_bioassay
  - bgc-2211-source-bindingdb_targets
  - bgc-2211-source-mibig_compounds
- assessment_id: bgc-2211-protein
  area: grounding
  topic: Protein
  outcome: unknown
  summary: The five carbonic-anhydrase examples distinguish human P00915/P00918/P22748/P23280
    from bovine Q3SZX4. Aromatase P11511 is human; the other target entries retain
    guinea-pig H9TB17 and human estrogen-receptor P03372/Q92731 scopes. Their BINDS
    relations and Ki/IC50 measurements are source-specific; no current sequence, construct,
    isoform or species transfer was verified. The historical accession-resolution
    statements remain attributed.
  target_ids:
  - CHEBI:50202
  evidence_ids:
  - bgc-2211-reader-DATA
  - bgc-2211-reader-execution
  - bgc-2211-reader-acceptance
  - bgc-2211-graph-0
  - bgc-2211-graph-1
  - bgc-2211-targets
  - bgc-2211-source-bindingdb_targets
  - bgc-2211-source-pubchem_bioassay
  - bgc-2211-origin-owner
findings:
- finding_id: bgc-2211-definition-locants
  issue_key: naringenin-definition-hydroxyl-locants-5-6-versus-5-7
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Retained definition gives the wrong A-ring hydroxyl locant
  description: The owner and retained CHEBI:50202 physical row13755 define hydroxy
    substitution at5,6,4′, but both stored forms and the same source row's structure
    encode5,7,4′. Indexed SMILES C4=9/C4a=8 fixes aromatic positions C5=7(OH11), C6=6(H),
    C7=5(OH12), C8=4(H), C8a=3; pendant para C16 bears OH19. Thus the wording describes
    a different positional isomer. The seeder faithfully copies this source definition,
    so correcting prose must not falsely present a curator correction as an unchanged
    source quotation or alter the correct stored structure.
  target_ids:
  - CHEBI:50202
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - bgc-2211-grounding-owner
  - bgc-2211-source-chebi_structures
  - bgc-2211-query-chebi_structures
  - bgc-2211-chemistry
  - bgc-2211-topology
  - bgc-2211-definition-owner
  - bgc-2211-review-skill
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained definition-copying and future provenance-aware correction boundary
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Preserve original source wording and structure provenance
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml
    role: Affected generated definition; structure is not the requested repair
  ownership_note: Future maintained-source correction only; generated YAML and retained
    raw source snapshots remain unchanged. Reserved/nonconsumed decisions.tsv is not
    a correction route.
  normalization_reason: Major scientific claim inconsistency or support-scope overstatement
    established by exact local evidence; passing mechanical checks do not resolve
    it.
  disposition_reason: Confirmed local evidence conflict, not an inference from unavailable
    external verification. Native found no same-owner prior issue_key in the declared
    ignored-inclusive saved-review scopes.
- finding_id: bgc-2211-aromatase-cytotoxic-class
  issue_key: naringenin-aromatase-ki-cytotoxic-class-overstatement
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Aromatase Ki assay is unsupported as cytotoxic evidence
  description: Written bioactivities[2], AID1799798, joins PubChem row1623 and reports
    ACTIVE aromatase Ki1.09662e−06µM against P11511. Cancer wording in the cited article
    title triggers CYTOTOXIC although the retained observation measures aromatase
    activity, not cytotoxicity. This is the sole written CYTOTOXIC summary backing.
    The corresponding BindingDB/graph value0.00109662nM is numerically consistent
    and may represent the same experiment; its extreme magnitude is not independently
    verified or corrected. The five carbonic-anhydrase assays separately retain ENZYME_INHIBITOR
    support.
  target_ids:
  - CHEBI:50202
  field_paths:
  - bioactivities[2].activity_class
  - bioactivity_summary
  evidence_ids:
  - bgc-2211-assay-owner
  - bgc-2211-source-pubchem_bioassay
  - bgc-2211-query-pubchem_bioassay
  - bgc-2211-source-bindingdb_targets
  - bgc-2211-reader-DATA
  - bgc-2211-activity-classifier
  - bgc-2211-activity-schema
  - bgc-2211-review-profile
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained generated-claim classification and summary derivation
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml
    role: Affected generated owner; regenerate after maintained correction
  ownership_note: Future maintained-source correction only; generated YAML and retained
    raw source snapshots remain unchanged. Reserved/nonconsumed decisions.tsv is not
    a correction route.
  normalization_reason: Major scientific claim inconsistency or support-scope overstatement
    established by exact local evidence; passing mechanical checks do not resolve
    it.
  disposition_reason: Confirmed local evidence conflict, not an inference from unavailable
    external verification. Native found no same-owner prior issue_key in the declared
    ignored-inclusive saved-review scopes.
actions:
- action_id: bgc-2211-repair-definition-locants
  description: Provide a narrowly scoped maintained definition correction or an explicit
    provenance-preserving conflict/omission route for this exact source concept and
    structure. If curator-corrected prose is emitted, describe5,7,4′ substitution
    and distinguish its provenance from the retained source's5,6,4′ wording. Preserve
    the original source snapshot, current structural strings/key and unspecified C2
    stereochemistry. Do not use reserved decisions.tsv or edit only the generated
    YAML.
  finding_ids:
  - bgc-2211-definition-locants
  target_ids:
  - CHEBI:50202
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained definition-copying and future provenance-aware correction boundary
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Preserve original source wording and structure provenance
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml
    role: Affected generated definition; structure is not the requested repair
  ownership_note: Proposed follow-up only; no implementation, source edits or external
    lookup occurred.
  acceptance_checks:
  - Preserve exact structure, source identifiers, raw source provenance and unaffected
    claims.
  - Regression coverage reproduces the precise evidence boundary and retains original
    calls, endpoint spelling, values, units, targets and references.
  - After authorized implementation, regenerate through maintained code and pass the
    required validation, reproduction and review gates.
  generator: scripts/seed_from_sources.py
- action_id: bgc-2211-repair-aromatase-cytotoxic-class
  description: 'Narrow maintained classification for exact AID1799798/title so article-topic
    cancer wording does not assert CYTOTOXIC without an appropriate measured endpoint.
    Omit that optional class unless separately supported; preserve ACTIVE, KI, exact1.09662e−06µM,
    P11511, PMID22726671 and the existing target/graph quantity and qualifier. Recompute
    the summary: its CYTOTOXIC backing needs correction, while the five written carbonic-anhydrase
    assays preserve ENZYME_INHIBITOR. Do not infer a lack of biological cytotoxicity,
    change units by intuition or count overlapping databases as independent experiments.'
  finding_ids:
  - bgc-2211-aromatase-cytotoxic-class
  target_ids:
  - CHEBI:50202
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained generated-claim classification and summary derivation
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/shikimates_and_phenylpropanoids/naringenin.yaml
    role: Affected generated owner; regenerate after maintained correction
  ownership_note: Proposed follow-up only; no implementation, source edits or external
    lookup occurred.
  acceptance_checks:
  - Preserve exact structure, source identifiers, raw source provenance and unaffected
    claims.
  - Regression coverage reproduces the precise evidence boundary and retains original
    calls, endpoint spelling, values, units, targets and references.
  - After authorized implementation, regenerate through maintained code and pass the
    required validation, reproduction and review gates.
  generator: scripts/seed_from_sources.py
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
