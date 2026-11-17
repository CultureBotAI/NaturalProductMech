# Local evidence review: (−)-geosmin

- Review: 20261104T021206Z-geosmin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T01:29:01.338323Z
- Finished UTC: 2026-11-04T02:12:06.205399Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

(−)-Geosmin retains its exact local ChEBI grounding, consistent fully specified stored structure and a preserved partial two-domain Cyc2 mechanism. Historical experiment and protein claims remain qualified; scientific completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2328; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:46702 | data/natural_products/terpenoids/geosmin.yaml | generated | (−)-geosmin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for geosmin | passed | True | CHEBI:46702 | One original offline maintained call preserves the complete Geosmin owner, one graph/four nodes/four edges, two pathway entries and four history events; historical science remains independently qualified. |
| strict_ten | passed | True | CHEBI:46702 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:46702 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:46702 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:46702 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:46702 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:46702 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:46702 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:46702 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: CHEBI:46702.

CHEBI:46702 and the retained (−)-geosmin label are grounded by the complete key JLPUXFOGCDVKGO-TUAOUCFPSA-N and the exact three-star ChEBI structure row. The definition’s 4S,4aS,8aR configuration is compatible with the saved structure: SMILES atoms 1,6,5 respectively carry S,S,R. The optical sign is a retained source assertion and cannot be deduced from R/S labels. MIBiG BGC0001181 uses the related name geosmin; no broader isomer equivalence is inferred.

### Representation

representation: supported. Targets: CHEBI:46702.

Both forms are neutral C12H22O with 13 atoms and 14 bonds. Two saturated six-membered carbocycles share one edge, with two methyl substituents and a tertiary bridgehead alcohol. Three tetrahedral centers are specified; no carbonyl or sugar-ring motif is present. All ten comparisons are true and the original atom correspondence is complete, while full_graph_identity_established remains false. Different local chiral tag orderings do not contradict the identical canonical stereochemical representation; neither local parsing nor the full key proves natural optical rotation or sample purity.

### Origin

provenance: supported. Targets: CHEBI:46702.

Streptomyces coelicolor A3(2) NCBITaxon:100226 is SOURCE_ASSERTION from BGC0001181 version 4, whose source locus link remains CLUSTER_UNSTATED with no stated method. Its active/questionable/unknown metadata does not erase or upgrade the separately curated historical Cyc2 experiments. Forty-one LOTUS rows across broad taxa remain occurrence claims, not a reconstruction of production in every organism.

### Citations

evidence: supported. Targets: CHEBI:46702.

The MIBiG producer/locus citation DOI:10.1038/s41564-020-0697-x is COMPOUND_BIOACTIVITY provenance. Historical mechanism DOI:10.1073/pnas.0337625100 supports the N-terminal germacradienol-forming role, while DOI:10.1038/nchembio.2007.29 supports the domain-resolved geosmin-forming role. The history records replacement of the latter evidence. Those retained PRIMARY_EXPERIMENT placements are distinct from database and LOTUS occurrence assertions; none was freshly accessed or sequence-verified.

### Activity

evidence: supported. Targets: CHEBI:46702.

The complete retained LOTUS scope has 41 rows, represented by 25 written occurrences plus a sixteen-further note. Repeated taxon/publication placements are not independent experiments. Local cached Cortinarius/Phlegmacium and Physarum/Badhamia names retain synonym scope only. No written bioactivity or molecular target and no exact retained PubChem, BindingDB or sibling activity match is present. A COMPOUND_BIOACTIVITY citation on the MIBiG source is not itself a structured assay or proof of inactivity.

### Classification

consistency: supported. Targets: CHEBI:46702.

NPClassifier retains Terpenoids / Sesquiterpenoids with both Eudesmane and Noreudesmane class strings and is_glycoside:false at its named version. The C12 bicyclic alcohol and retained C15-precursor conversion are compatible with a limited degraded-sesquiterpenoid discussion. Neither carbon count nor model labels alone establishes the natural pathway. Source TERPENE, historical Cyc2 mechanism and computed filing remain separately attributed.

### Completion

completeness: unknown. Targets: CHEBI:46702.

All twelve scientific dimensions were assessed against the complete owner/history, actual intake, complete retained source scope and both saved molecular forms. Five original local commands passed; full QC, complete OAK authority coverage and fresh primary/taxonomic verification remain unavailable. The selected Geosmin maintained reader returned once and preserved the complete owner and historical mechanism. No new supported maintained-source correction is established in this bounded evidence scope. Scientific completion remains partial; native status/history are unchanged.

### Pathway

graph: supported. Targets: CHEBI:46702.

The two preserved steps use the same UniProtKB:Q9X839 Cyc2 protein: N-terminal conversion of CHEBI:175763 farnesyl diphosphate to CHEBI:46734 germacradienol with RHEA:22436, then C-terminal conversion to CHEBI:46702 with RHEA:30371. Two separate historical experiment citations are retained. This is an explicitly partial pathway, not complete upstream metabolism or newly verified reaction stoichiometry. SCO6073, AL939126/CAB41566.1 and domain mapping remain historical claims; no fresh protein sequence, construct, processing or strain-stock equality is established.

### Graph

graph: supported. Targets: CHEBI:46702.

The accepted maintained reader preserves the complete owner, one inline BIOSYNTHESIS graph, four grounded nodes, four evidence-bearing edges, two pathway entries and all four history events. The graph separates substrate cyclization/germacradienol formation from conversion/geosmin formation through the same bifunctional Cyc2 node. Four edge evidence placements reuse two citations and do not represent four independent experiments. No component or molecular-target root is declared. Reader preservation establishes representation fidelity, not fresh validation of the biological claims.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2328-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/geosmin.yaml; Whole current owner plaintext and complete curation_history | supports | Complete owner and all 4 history entries are covered by current exact whole-reading attribution. Native curation_status remains SEEDED. |
| support-2328-capture | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/7 | supports | Complete original captured owner and exact literal mechanism/component presence, distinct from maintained resolution. Exact copied saved values: {"/records/7": {"component_captures": [], "mechanism_capture_scope": "raw_owner_and_declared_components_only_not_maintained_resolution", "order": 2328, "owner_document": {"bgc_class": ["TERPENE"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001181", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "4", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001181 entry version 4; citation taken from the compound bioactivity level", "reference": "DOI:10.1038/s41564-020-0697-x"}], "genome_accession": "genbank:AL645882.2", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 6666219, "locus_to": 6668399, "organism_label": "Streptomyces coelicolor A3(2)", "organism_taxon_id": "NCBITaxon:100226"}], "biosynthetic_pathway": [{"enzyme_id": "UniProtKB:Q9X839", "enzyme_label": "Cyc2 germacradienol/germacrene D synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "notes": "The N-terminal domain of bifunctional Cyc2 cyclizes (2E,6E)-farnesyl diphosphate to germacradienol, the sesquiterpene alcohol intermediate in geosmin biosynthesis.", "product": "CHEBI:46734", "reaction_id": "RHEA:22436", "step_number": 1, "substrate": "CHEBI:175763"}, {"enzyme_id": "UniProtKB:Q9X839", "enzyme_label": "Cyc2 geosmin synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "notes": "The C-terminal domain of bifunctional Cyc2 converts germacradienol to (−)-geosmin.", "product": "CHEBI:46702", "reaction_id": "RHEA:30371", "step_number": 2, "substrate": "CHEBI:46734"}], "causal_graphs": [{"description": "Partial Streptomyces coelicolor geosmin biosynthesis graph for bifunctional Cyc2 conversion of farnesyl diphosphate to (−)-geosmin through germacradienol.", "edges": [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "object": "cyc2", "predicate": "is cyclized by", "subject": "farnesyl_diphosphate"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "object": "germacradienol", "predicate": "forms", "subject": "cyc2"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "object": "cyc2", "predicate": "is converted by", "subject": "germacradienol"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "object": "geosmin", "predicate": "forms", "subject": "cyc2"}], "graph_id": "geosmin-cyc2-biosynthesis", "nodes": [{"grounding_status": "GROUNDED", "identifier": "CHEBI:175763", "label": "(2E,6E)-farnesyl diphosphate", "node_id": "farnesyl_diphosphate", "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED", "identifier": "UniProtKB:Q9X839", "label": "Cyc2", "node_id": "cyc2", "node_type": "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46734", "label": "germacradienol", "node_id": "germacradienol", "node_type": "COMPOUND"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46702", "label": "(−)-geosmin", "node_id": "geosmin", "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"}], "chemical_structure": {"smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001181"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:08Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:02:26Z"}, {"action": "RECORD_CURATED", "changes": "Added a two-step BIOSYNTHESIS pathway and causal graph for geosmin biosynthesis; grounded the Streptomyces coelicolor bifunctional Cyc2 enzyme to UniProtKB:Q9X839 via SCO6073; and cited the experimentally characterized RHEA:22436 and RHEA:30371 reactions.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-26T22:48:26Z"}, {"action": "RECORD_CURATED", "changes": "Replaced the geosmin-forming Cyc2 step and edge evidence with the domain-resolved bifunctional geosmin synthase paper, DOI:10.1038/nchembio.2007.29.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-26T23:08:49Z"}], "curation_status": "SEEDED", "definition": "The (−)-stereoisomer of geosmin, having 4S,4aS,8aR configuration.", "definition_source": "CHEBI:46702", "grounding_status": "EXACT", "identifier": "CHEBI:46702", "label": "(−)-geosmin", "np_classification": {"class_results": ["Eudesmane sesquiterpenoids", "Noreudesmane sesquiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Sesquiterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["ACTINOBACTERIAL", "CYANOBACTERIAL", "FUNGAL", "LAND_PLANT"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/S002170100305"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q47685", "source": "LOTUS", "taxon_id": "NCBITaxon:13443", "taxon_label": "Coffea arabica", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q84325870", "source": "LOTUS", "taxon_id": "NCBITaxon:1586124", "taxon_label": "Cortinarius herculeus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q84325870", "source": "LOTUS", "taxon_id": "NCBITaxon:1586124", "taxon_label": "Cortinarius herculeus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JF60204A059"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q165191", "source": "LOTUS", "taxon_id": "NCBITaxon:161934", "taxon_label": "Beta vulgaris", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/BF00416598"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q39087436", "source": "LOTUS", "taxon_id": "NCBITaxon:177969", "taxon_label": "Oscillatoria brevis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q470766", "source": "LOTUS", "taxon_id": "NCBITaxon:182063", "taxon_label": "Cystoderma amianthinum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q470766", "source": "LOTUS", "taxon_id": "NCBITaxon:182063", "taxon_label": "Cystoderma amianthinum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/J.YMBEN.2018.09.004"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1144013", "source": "LOTUS", "taxon_id": "NCBITaxon:1883", "taxon_label": "Streptomyces", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JA062669X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.47.434"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JA062669X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1111/J.1365-2672.1992.TB01818.X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q7623385", "source": "LOTUS", "taxon_id": "NCBITaxon:1911", "taxon_label": "Streptomyces griseus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JF00013A023"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292941", "source": "LOTUS", "taxon_id": "NCBITaxon:1932", "taxon_label": "Streptomyces tendae", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1128/AEM.57.12.3429-3432.1991"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292941", "source": "LOTUS", "taxon_id": "NCBITaxon:1932", "taxon_label": "Streptomyces tendae", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/SJ.JIM.7000121"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22665882", "source": "LOTUS", "taxon_id": "NCBITaxon:1944", "taxon_label": "Streptomyces halstedii", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/BF02932133"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562", "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces avermitilis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/JA.2006.66"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562 16 further cited occurrences are recorded in data/raw/lotus_occurrences.tsv and data/raw/chebi_origins.tsv but not written here: a record carrying hundreds of them cannot be reviewed. The inventories are the complete record.", "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces avermitilis", "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001181", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001181 entry version 4; citation taken from the compound bioactivity level", "reference": "DOI:10.1038/s41564-020-0697-x"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "4", "taxon_id": "NCBITaxon:100226", "taxon_label": "Streptomyces coelicolor A3(2)"}], "producer_taxon_groups": ["ACTINOBACTERIAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-0349656c0d", "source": "MIBIG", "source_id": "BGC0001181", "source_label": "geosmin", "source_version": "4"}, {"minted_identifier": "naturalproductmech:chebi-cea96d6d0a", "source": "CHEBI", "source_id": "CHEBI:46702", "source_label": "(−)-geosmin", "source_version": "3-star"}], "synonyms": [{"source": "mibig:BGC0001181", "synonym_type": "RELATED_SYNONYM", "value": "geosmin"}]}, "owner_pin": {"bytes": 19003, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/geosmin.yaml", "sha256": "c026509c83990c5cda6a01008a0346bc2997fdc5b6d2fde3ba2ac5522a8f429a"}, "path": "data/natural_products/terpenoids/geosmin.yaml", "read_finished_at": "2026-11-04T01:29:01.346830Z", "read_started_at": "2026-11-04T01:29:01.338323Z"}} |
| support-2328-grounding-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/7/owner_document/identifier; /records/7/owner_document/label; /records/7/owner_document/chemical_structure; /records/7/owner_document/definition; /records/7/owner_document/definition_source; /records/7/owner_document/synonyms; /records/7/owner_document/grounding_status; /records/7/owner_document/source_concepts | supports | Exact identity, source definition and grounding fields, including retained unresolved discussion where present. Exact copied saved values: {"/records/7/owner_document/chemical_structure": {"smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001181"}, "/records/7/owner_document/definition": "The (−)-stereoisomer of geosmin, having 4S,4aS,8aR configuration.", "/records/7/owner_document/definition_source": "CHEBI:46702", "/records/7/owner_document/grounding_status": "EXACT", "/records/7/owner_document/identifier": "CHEBI:46702", "/records/7/owner_document/label": "(−)-geosmin", "/records/7/owner_document/source_concepts": [{"minted_identifier": "naturalproductmech:mibig-0349656c0d", "source": "MIBIG", "source_id": "BGC0001181", "source_label": "geosmin", "source_version": "4"}, {"minted_identifier": "naturalproductmech:chebi-cea96d6d0a", "source": "CHEBI", "source_id": "CHEBI:46702", "source_label": "(−)-geosmin", "source_version": "3-star"}], "/records/7/owner_document/synonyms": [{"source": "mibig:BGC0001181", "synonym_type": "RELATED_SYNONYM", "value": "geosmin"}]} |
| support-2328-origin-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters; /records/7/owner_document/producer_taxon_groups | supports | Separately graded producer and locus source assertions. Exact copied saved values: {"/records/7/owner_document/biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001181", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "4", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001181 entry version 4; citation taken from the compound bioactivity level", "reference": "DOI:10.1038/s41564-020-0697-x"}], "genome_accession": "genbank:AL645882.2", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 6666219, "locus_to": 6668399, "organism_label": "Streptomyces coelicolor A3(2)", "organism_taxon_id": "NCBITaxon:100226"}], "/records/7/owner_document/producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001181", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001181 entry version 4; citation taken from the compound bioactivity level", "reference": "DOI:10.1038/s41564-020-0697-x"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "4", "taxon_id": "NCBITaxon:100226", "taxon_label": "Streptomyces coelicolor A3(2)"}], "/records/7/owner_document/producer_taxon_groups": ["ACTINOBACTERIAL"]} |
| support-2328-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/7/owner_document/occurrences; /records/7/owner_document/occurrence_taxon_groups | supports | Written occurrence placements and retained further-row notes. Exact copied saved values: {"/records/7/owner_document/occurrence_taxon_groups": ["ACTINOBACTERIAL", "CYANOBACTERIAL", "FUNGAL", "LAND_PLANT"], "/records/7/owner_document/occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/S002170100305"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q47685", "source": "LOTUS", "taxon_id": "NCBITaxon:13443", "taxon_label": "Coffea arabica", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q84325870", "source": "LOTUS", "taxon_id": "NCBITaxon:1586124", "taxon_label": "Cortinarius herculeus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q84325870", "source": "LOTUS", "taxon_id": "NCBITaxon:1586124", "taxon_label": "Cortinarius herculeus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JF60204A059"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q165191", "source": "LOTUS", "taxon_id": "NCBITaxon:161934", "taxon_label": "Beta vulgaris", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/BF00416598"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q39087436", "source": "LOTUS", "taxon_id": "NCBITaxon:177969", "taxon_label": "Oscillatoria brevis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q470766", "source": "LOTUS", "taxon_id": "NCBITaxon:182063", "taxon_label": "Cystoderma amianthinum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q470766", "source": "LOTUS", "taxon_id": "NCBITaxon:182063", "taxon_label": "Cystoderma amianthinum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/J.YMBEN.2018.09.004"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1144013", "source": "LOTUS", "taxon_id": "NCBITaxon:1883", "taxon_label": "Streptomyces", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JA062669X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.47.434"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JA062669X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1111/J.1365-2672.1992.TB01818.X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q7623385", "source": "LOTUS", "taxon_id": "NCBITaxon:1911", "taxon_label": "Streptomyces griseus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JF00013A023"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292941", "source": "LOTUS", "taxon_id": "NCBITaxon:1932", "taxon_label": "Streptomyces tendae", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1128/AEM.57.12.3429-3432.1991"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292941", "source": "LOTUS", "taxon_id": "NCBITaxon:1932", "taxon_label": "Streptomyces tendae", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/SJ.JIM.7000121"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22665882", "source": "LOTUS", "taxon_id": "NCBITaxon:1944", "taxon_label": "Streptomyces halstedii", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/BF02932133"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562", "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces avermitilis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/JA.2006.66"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562 16 further cited occurrences are recorded in data/raw/lotus_occurrences.tsv and data/raw/chebi_origins.tsv but not written here: a record carrying hundreds of them cannot be reviewed. The inventories are the complete record.", "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces avermitilis", "taxon_source": "NCBITaxon"}]} |
| support-2328-assay-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/7/owner_document | supports | Written observations and coarse activity summary; whole owner selector proves absent optional roots without a global absence claim. Exact copied saved values: {"/records/7/owner_document": {"bgc_class": ["TERPENE"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001181", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "4", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001181 entry version 4; citation taken from the compound bioactivity level", "reference": "DOI:10.1038/s41564-020-0697-x"}], "genome_accession": "genbank:AL645882.2", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 6666219, "locus_to": 6668399, "organism_label": "Streptomyces coelicolor A3(2)", "organism_taxon_id": "NCBITaxon:100226"}], "biosynthetic_pathway": [{"enzyme_id": "UniProtKB:Q9X839", "enzyme_label": "Cyc2 germacradienol/germacrene D synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "notes": "The N-terminal domain of bifunctional Cyc2 cyclizes (2E,6E)-farnesyl diphosphate to germacradienol, the sesquiterpene alcohol intermediate in geosmin biosynthesis.", "product": "CHEBI:46734", "reaction_id": "RHEA:22436", "step_number": 1, "substrate": "CHEBI:175763"}, {"enzyme_id": "UniProtKB:Q9X839", "enzyme_label": "Cyc2 geosmin synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "notes": "The C-terminal domain of bifunctional Cyc2 converts germacradienol to (−)-geosmin.", "product": "CHEBI:46702", "reaction_id": "RHEA:30371", "step_number": 2, "substrate": "CHEBI:46734"}], "causal_graphs": [{"description": "Partial Streptomyces coelicolor geosmin biosynthesis graph for bifunctional Cyc2 conversion of farnesyl diphosphate to (−)-geosmin through germacradienol.", "edges": [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "object": "cyc2", "predicate": "is cyclized by", "subject": "farnesyl_diphosphate"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "object": "germacradienol", "predicate": "forms", "subject": "cyc2"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "object": "cyc2", "predicate": "is converted by", "subject": "germacradienol"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "object": "geosmin", "predicate": "forms", "subject": "cyc2"}], "graph_id": "geosmin-cyc2-biosynthesis", "nodes": [{"grounding_status": "GROUNDED", "identifier": "CHEBI:175763", "label": "(2E,6E)-farnesyl diphosphate", "node_id": "farnesyl_diphosphate", "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED", "identifier": "UniProtKB:Q9X839", "label": "Cyc2", "node_id": "cyc2", "node_type": "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46734", "label": "germacradienol", "node_id": "germacradienol", "node_type": "COMPOUND"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46702", "label": "(−)-geosmin", "node_id": "geosmin", "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"}], "chemical_structure": {"smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001181"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:08Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:02:26Z"}, {"action": "RECORD_CURATED", "changes": "Added a two-step BIOSYNTHESIS pathway and causal graph for geosmin biosynthesis; grounded the Streptomyces coelicolor bifunctional Cyc2 enzyme to UniProtKB:Q9X839 via SCO6073; and cited the experimentally characterized RHEA:22436 and RHEA:30371 reactions.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-26T22:48:26Z"}, {"action": "RECORD_CURATED", "changes": "Replaced the geosmin-forming Cyc2 step and edge evidence with the domain-resolved bifunctional geosmin synthase paper, DOI:10.1038/nchembio.2007.29.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-26T23:08:49Z"}], "curation_status": "SEEDED", "definition": "The (−)-stereoisomer of geosmin, having 4S,4aS,8aR configuration.", "definition_source": "CHEBI:46702", "grounding_status": "EXACT", "identifier": "CHEBI:46702", "label": "(−)-geosmin", "np_classification": {"class_results": ["Eudesmane sesquiterpenoids", "Noreudesmane sesquiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Sesquiterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["ACTINOBACTERIAL", "CYANOBACTERIAL", "FUNGAL", "LAND_PLANT"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/S002170100305"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q47685", "source": "LOTUS", "taxon_id": "NCBITaxon:13443", "taxon_label": "Coffea arabica", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q84325870", "source": "LOTUS", "taxon_id": "NCBITaxon:1586124", "taxon_label": "Cortinarius herculeus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q84325870", "source": "LOTUS", "taxon_id": "NCBITaxon:1586124", "taxon_label": "Cortinarius herculeus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JF60204A059"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q165191", "source": "LOTUS", "taxon_id": "NCBITaxon:161934", "taxon_label": "Beta vulgaris", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/BF00416598"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q39087436", "source": "LOTUS", "taxon_id": "NCBITaxon:177969", "taxon_label": "Oscillatoria brevis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q470766", "source": "LOTUS", "taxon_id": "NCBITaxon:182063", "taxon_label": "Cystoderma amianthinum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q470766", "source": "LOTUS", "taxon_id": "NCBITaxon:182063", "taxon_label": "Cystoderma amianthinum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/J.YMBEN.2018.09.004"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1144013", "source": "LOTUS", "taxon_id": "NCBITaxon:1883", "taxon_label": "Streptomyces", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JA062669X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.47.434"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JA062669X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1111/J.1365-2672.1992.TB01818.X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q7623385", "source": "LOTUS", "taxon_id": "NCBITaxon:1911", "taxon_label": "Streptomyces griseus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JF00013A023"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292941", "source": "LOTUS", "taxon_id": "NCBITaxon:1932", "taxon_label": "Streptomyces tendae", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1128/AEM.57.12.3429-3432.1991"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292941", "source": "LOTUS", "taxon_id": "NCBITaxon:1932", "taxon_label": "Streptomyces tendae", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/SJ.JIM.7000121"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22665882", "source": "LOTUS", "taxon_id": "NCBITaxon:1944", "taxon_label": "Streptomyces halstedii", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1007/BF02932133"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562", "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces avermitilis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/JA.2006.66"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562 16 further cited occurrences are recorded in data/raw/lotus_occurrences.tsv and data/raw/chebi_origins.tsv but not written here: a record carrying hundreds of them cannot be reviewed. The inventories are the complete record.", "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces avermitilis", "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001181", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001181 entry version 4; citation taken from the compound bioactivity level", "reference": "DOI:10.1038/s41564-020-0697-x"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "4", "taxon_id": "NCBITaxon:100226", "taxon_label": "Streptomyces coelicolor A3(2)"}], "producer_taxon_groups": ["ACTINOBACTERIAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-0349656c0d", "source": "MIBIG", "source_id": "BGC0001181", "source_label": "geosmin", "source_version": "4"}, {"minted_identifier": "naturalproductmech:chebi-cea96d6d0a", "source": "CHEBI", "source_id": "CHEBI:46702", "source_label": "(−)-geosmin", "source_version": "3-star"}], "synonyms": [{"source": "mibig:BGC0001181", "synonym_type": "RELATED_SYNONYM", "value": "geosmin"}]}} |
| support-2328-classification-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification; /records/7/owner_document/bgc_class | supports | Versioned computed filing and separately asserted BGC/compound classes. Exact copied saved values: {"/records/7/owner_document/bgc_class": ["TERPENE"], "/records/7/owner_document/np_classification": {"class_results": ["Eudesmane sesquiterpenoids", "Noreudesmane sesquiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Sesquiterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "/records/7/owner_document/np_pathway": "TERPENOIDS"} |
| support-2328-chemistry | /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/comparisons; /records/7/atom_correspondence | supports | Complete original declared forms/comparisons/map, unchanged. Exact copied saved values: {"/records/7/atom_correspondence": {"complete_atom_count_match": true, "full_graph_identity_established": false, "scope": "One chirality-aware substructure match; no independent full graph or natural identity claim.", "smiles_to_inchi_atom_indices": [0, 9, 5, 4, 7, 10, 11, 8, 3, 2, 6, 12, 1]}, "/records/7/comparisons": {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared": true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal": true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer": true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "/records/7/declared_structure": {"smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001181"}} |
| support-2328-topology | /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed; /records/7/inchi/computed; /records/7/declared_structure; /records/7/comparisons; /records/7/atom_correspondence | supports | Both forms are neutral C12H22O with 13 atoms and 14 bonds. Two saturated six-membered carbocycles share one edge, with two methyl substituents and a tertiary bridgehead alcohol. Three tetrahedral centers are specified; no carbonyl or sugar-ring motif is present. All ten comparisons are true and the original atom correspondence is complete, while full_graph_identity_established remains false. Different local chiral tag orderings do not contradict the identical canonical stereochemical representation; neither local parsing nor the full key proves natural optical rotation or sample purity. |
| support-2328-intake | /private/tmp/npm-review-work/shared-next-batch233/intakes/2328-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake, all admitted input roles and maintained correction ownership. Exact copied saved values: {"/repository": "CultureBotAI/NaturalProductMech", "/source": {"git_revision": "ce6a5498df5be51116bd5e0c119023ee62bb5464", "inputs": [{"path": ".claude/skills/curate-yaml-record/references/review-checklist.md", "role": "context", "sha256": "13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9"}, {"path": ".claude/skills/review-yaml-record/SKILL.md", "role": "context", "sha256": "493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae"}, {"path": "AGENTS.md", "role": "context", "sha256": "69e4037f8dc97d4b00bb7bb83b41ceca025f6ef578d5c0bf8086f3400becde0b"}, {"path": "conf/id_label_targets.yaml", "role": "context", "sha256": "24235903e0e8df5793a30e92c551082c71c1c67739ea4e3b5fb0f68853a805e6"}, {"path": "conf/producer_evidence.tsv", "role": "context", "sha256": "67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131"}, {"path": "conf/record_review.yaml", "role": "context", "sha256": "e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8"}, {"path": "curation/lotus_occurrence_exclusions.tsv", "role": "context", "sha256": "d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d"}, {"path": "curation/mibig_claim_references.tsv", "role": "context", "sha256": "bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029"}, {"path": "curation/mibig_locus_evidence_overrides.tsv", "role": "context", "sha256": "7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e"}, {"path": "curation/mibig_producer_isolates.tsv", "role": "context", "sha256": "8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8"}, {"path": "curation/mibig_producer_strains.tsv", "role": "context", "sha256": "bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae"}, {"path": "curation/mibig_structure_corrections.tsv", "role": "context", "sha256": "c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0"}, {"path": "curation/mibig_xref_exclusions.tsv", "role": "context", "sha256": "cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c"}, {"path": "data/natural_products/PATHS.tsv", "role": "context", "sha256": "2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3"}, {"path": "data/natural_products/terpenoids/geosmin.yaml", "role": "target", "sha256": "c026509c83990c5cda6a01008a0346bc2997fdc5b6d2fde3ba2ac5522a8f429a"}, {"path": "data/raw/MANIFEST.yaml", "role": "context", "sha256": "b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3"}, {"path": "data/raw/antibioticmech_inchikeys.tsv", "role": "context", "sha256": "ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6"}, {"path": "data/raw/bindingdb_targets.tsv", "role": "context", "sha256": "3cff45281c35a8b14d4d7784bc4b7af80e8e27779a5667a0292f0d9b022a22c1"}, {"path": "data/raw/chebi_origins.tsv", "role": "context", "sha256": "fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8"}, {"path": "data/raw/chebi_structures.tsv", "role": "context", "sha256": "62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2"}, {"path": "data/raw/corpus_taxa.obo", "role": "context", "sha256": "8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9"}, {"path": "data/raw/cyanometdb_occurrences.tsv", "role": "context", "sha256": "f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8"}, {"path": "data/raw/lotus_occurrences.tsv", "role": "context", "sha256": "ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94"}, {"path": "data/raw/mibig_compounds.tsv", "role": "context", "sha256": "e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6"}, {"path": "data/raw/npclassifier.tsv", "role": "context", "sha256": "acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3"}, {"path": "data/raw/pubchem_bioassay.tsv", "role": "context", "sha256": "6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b"}, {"path": "docs/CURATION.md", "role": "context", "sha256": "c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa"}, {"path": "docs/HARMONIZATION.md", "role": "context", "sha256": "c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79"}, {"path": "docs/record-review-profile.md", "role": "context", "sha256": "1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a"}, {"path": "docs/record-reviews.md", "role": "context", "sha256": "452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b"}, {"path": "justfile", "role": "context", "sha256": "4f9057e3e54656dd46f2ded4d3a8f0804acad348d2605d436405e1fcfb6af550"}, {"path": "schema/record_review.yaml", "role": "context", "sha256": "229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb"}, {"path": "scripts/extract_chebi.py", "role": "context", "sha256": "46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f"}, {"path": "scripts/extract_mibig.py", "role": "context", "sha256": "e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c"}, {"path": "scripts/seed_from_sources.py", "role": "context", "sha256": "5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5"}, {"path": "src/naturalproductmech/curate/claim_references.py", "role": "context", "sha256": "0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3"}, {"path": "src/naturalproductmech/graph_components.py", "role": "context", "sha256": "10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17"}, {"path": "src/naturalproductmech/schema/naturalproductmech.yaml", "role": "context", "sha256": "9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d"}, {"path": "src/naturalproductmech/validation/write_validated.py", "role": "context", "sha256": "4b7648fc5d2e7a5d26ad8bb168dbcae609aaa2694434a8ed5cfcb33fb66ff80a"}], "state": "working_tree"}, "/status": "inspection_only", "/targets": [{"kind": "generated", "label": "(−)-geosmin", "owner_paths": [{"path": "scripts/seed_from_sources.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained harmonization generator; seeded fields are corrected through maintained inputs and validated regeneration."}, {"path": "data/raw/mibig_compounds.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Retained MIBiG structure, producer and compound-specific locus assertions."}, {"path": "data/raw/npclassifier.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Pinned computed classification and filing assertions."}, {"path": "scripts/extract_mibig.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained extraction of MIBiG compound names, structures, stereochemistry flags and source provenance."}, {"path": "data/raw/chebi_structures.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Retained ChEBI identifiers, definitions and exact chemical forms."}, {"path": "data/raw/lotus_occurrences.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Retained cited occurrence assertions, distinct from demonstrated production."}, {"path": "src/naturalproductmech/graph_components.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Future maintained complete-owner reader implementation; not invoked in this plan."}, {"path": "src/naturalproductmech/validation/write_validated.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Future maintained complete-owner reader implementation; not invoked in this plan."}, {"path": "data/natural_products/terpenoids/geosmin.yaml", "repository": "CultureBotAI/NaturalProductMech", "role": "Curator-owned declared graphs, graph references, pathway steps and history; imported molecular-target assertions and other seeded fields retain inventory ownership. Curated graph/pathway changes require the validated writer and a curation event."}], "ownership_note": "This review proposes no record edit. Source corrections belong in maintained inventories, implemented curation tables, extractors or the seeder; generated pages are not owners. This mechanism-bearing owner requires separately authorized complete maintained resolution before scientific assessment and draft assembly. Raw owner capture is not a maintained resolved view.", "path": "data/natural_products/terpenoids/geosmin.yaml", "record_class": "NaturalProductRecord", "target_id": "CHEBI:46702"}]} |
| support-2328-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-intake-acceptance-001.json; /status; /accepted; /source_placements; /unique_source_paths | supports | ROOT accepts all ten original canonical intakes, with 396 source placements and 68 distinct paths. |
| support-2328-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-source-inventory-acceptance-001.json; /status; /accepted | supports | ROOT accepts the original local inventory; source meanings are separately attributed. |
| support-2328-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-input-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepts the original input plan, not a scientific verdict. |
| support-2328-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-diagnostic-acceptance-001.json; /status; /accepted; /verified; /records; /warnings; /warning_scope | supports | ROOT accepts twenty original stored parses, all paired comparisons and declared keys. Two original undefined-stereo warnings remain global and unassigned. |
| support-2328-native-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-native-gates-acceptance-001.json; /status; /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates | supports | Five original local commands passed; full QC and complete OAK authority coverage remain unavailable. |
| support-2328-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-execution-001.json; Whole original execution receipt | supports | ROOT operated the one accepted diagnostic. No replay, alternate parse or owner-specific warning attribution is introduced by scientific authoring. |
| support-2328-plan | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-target-input-plan-001.json; /records/7; /source_placement_count; /unique_source_path_count | supports | Complete accepted per-owner input plan; cohort totals 396 placements / 68 paths, owner 39 placements. |
| support-2328-source-notes | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Joint complete source reading and exact raw/history carry attribution, source-specific cautions and access limits; the notes precede scientific adjudication. |
| support-2328-curation-scope | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json; /curation | supports | BGC performed one bounded 169-literal scan of eight directly opened implemented tables, including ignored files, with zero textual hits. Reserved decisions.tsv was unconsumed; no global absence claim follows. |
| support-2328-source-routes | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/matched_chebi_ids; /contexts/24/source_scope_inventory/source_taxa; /contexts/24/source_scope_inventory/forward_taxon_merge_matches; /contexts/24/source_scope_inventory/nonorganism_matches; /contexts/24/source_scope_inventory/actual_assay_rows; /contexts/24/source_scope_inventory/blank_AID_sentinels; /contexts/24/source_scope_inventory/related_corpus_rows | supports | Complete retained route metadata, including assay/sentinel distinctions and exact empty routes. Exact copied saved values: {"/contexts/24/source_scope_inventory/actual_assay_rows": [], "/contexts/24/source_scope_inventory/blank_AID_sentinels": [], "/contexts/24/source_scope_inventory/forward_taxon_merge_matches": [], "/contexts/24/source_scope_inventory/matched_chebi_ids": ["CHEBI:46702"], "/contexts/24/source_scope_inventory/nonorganism_matches": [], "/contexts/24/source_scope_inventory/related_corpus_rows": [], "/contexts/24/source_scope_inventory/source_taxa": ["NCBITaxon:100226", "NCBITaxon:13443", "NCBITaxon:1586124", "NCBITaxon:161934", "NCBITaxon:177969", "NCBITaxon:182063", "NCBITaxon:1883", "NCBITaxon:1886", "NCBITaxon:1902", "NCBITaxon:1911", "NCBITaxon:1932", "NCBITaxon:1944", "NCBITaxon:33903", "NCBITaxon:3589", "NCBITaxon:38033", "NCBITaxon:3885", "NCBITaxon:40318", "NCBITaxon:42684", "NCBITaxon:4577", "NCBITaxon:511157", "NCBITaxon:53033", "NCBITaxon:5791", "NCBITaxon:59299", "NCBITaxon:67267", "NCBITaxon:68280"]} |
| support-2328-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/4; /cached_taxonomy/whole_stanzas/5; /cached_taxonomy/whole_stanzas/6; /cached_taxonomy/whole_stanzas/7; /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/whole_stanzas/19; /cached_taxonomy/whole_stanzas/23; /cached_taxonomy/whole_stanzas/27; /cached_taxonomy/whole_stanzas/28; /cached_taxonomy/whole_stanzas/30; /cached_taxonomy/whole_stanzas/31; /cached_taxonomy/whole_stanzas/32; /cached_taxonomy/whole_stanzas/35; /cached_taxonomy/whole_stanzas/36; /cached_taxonomy/whole_stanzas/37; /cached_taxonomy/whole_stanzas/39; /cached_taxonomy/whole_stanzas/40; /cached_taxonomy/whole_stanzas/43; /cached_taxonomy/whole_stanzas/50; /cached_taxonomy/whole_stanzas/52; /cached_taxonomy/whole_stanzas/53; /cached_taxonomy/whole_stanzas/74; /cached_taxonomy/whole_stanzas/91 | supports | All applicable cached stanzas copied in full; names/synonyms remain local snapshots. Exact copied saved values: {"/cached_taxonomy/whole_stanzas/19": {"complete_stanza": "[Term]\nid: NCBITaxon:3885\nname: Phaseolus vulgaris\n\n", "id": "NCBITaxon:3885", "physical_line": 5800}, "/cached_taxonomy/whole_stanzas/2": {"complete_stanza": "[Term]\nid: NCBITaxon:1883\nname: Streptomyces\nsynonym: \"\\\"Microstreptospora\\\" Yan et al.\" EXACT []\nsynonym: \"Actinopycnidium Krasil'nikov 1962\" EXACT []\nsynonym: \"Actinosporangium Krasil'nikov and Yuan 1961\" EXACT []\nsynonym: \"Chainia\" EXACT []\nsynonym: \"Elytrosporangium Falcao de Morais et al. 1966\" EXACT []\nsynonym: \"Kitasatoa Matsumae and Hata 1968 (Approved Lists 1980)\" EXACT []\nsynonym: \"Microellobosporia\" EXACT []\nsynonym: \"Streptoverticillium Baldacci 1958\" EXACT []\n\n", "id": "NCBITaxon:1883", "physical_line": 2798}, "/cached_taxonomy/whole_stanzas/23": {"complete_stanza": "[Term]\nid: NCBITaxon:4577\nname: Zea mays\nsynonym: \"Zea mays var. japonica\" EXACT []\n\n", "id": "NCBITaxon:4577", "physical_line": 7255}, "/cached_taxonomy/whole_stanzas/27": {"complete_stanza": "[Term]\nid: NCBITaxon:5791\nname: Badhamia polycephala\nsynonym: \"Physarum polycephalum\" EXACT []\n\n", "id": "NCBITaxon:5791", "physical_line": 8915}, "/cached_taxonomy/whole_stanzas/28": {"complete_stanza": "[Term]\nid: NCBITaxon:13443\nname: Coffea arabica\n\n", "id": "NCBITaxon:13443", "physical_line": 10977}, "/cached_taxonomy/whole_stanzas/3": {"complete_stanza": "[Term]\nid: NCBITaxon:1886\nname: Streptomyces albidoflavus\nsynonym: \"Actinomyces albidoflavus\" EXACT []\nsynonym: \"Actinomyces globisporus var. caucasicus\" EXACT []\nsynonym: \"Cladothrix albido-flava\" EXACT []\nsynonym: \"Streptomyces albidoflavus (Rossi Doria 1891) Waksman and Henrici 1948 (Approved Lists 1980)\" EXACT []\nsynonym: \"Streptomyces globisporus subsp. caucasicus\" EXACT []\n\n", "id": "NCBITaxon:1886", "physical_line": 2820}, "/cached_taxonomy/whole_stanzas/30": {"complete_stanza": "[Term]\nid: NCBITaxon:33903\nname: Streptomyces avermitilis\nsynonym: \"Streptomyces avermectinius\" EXACT []\n\n", "id": "NCBITaxon:33903", "physical_line": 14687}, "/cached_taxonomy/whole_stanzas/31": {"complete_stanza": "[Term]\nid: NCBITaxon:38033\nname: Chaetomium globosum\nsynonym: \"Chaetomium rectum\" EXACT []\n\n", "id": "NCBITaxon:38033", "physical_line": 16592}, "/cached_taxonomy/whole_stanzas/32": {"complete_stanza": "[Term]\nid: NCBITaxon:40318\nname: Streptomyces nodosus\n\n", "id": "NCBITaxon:40318", "physical_line": 17770}, "/cached_taxonomy/whole_stanzas/35": {"complete_stanza": "[Term]\nid: NCBITaxon:42684\nname: Streptomyces collinus\n\n", "id": "NCBITaxon:42684", "physical_line": 19479}, "/cached_taxonomy/whole_stanzas/36": {"complete_stanza": "[Term]\nid: NCBITaxon:53033\nname: Symphyogyna brongniartii\n\n", "id": "NCBITaxon:53033", "physical_line": 24297}, "/cached_taxonomy/whole_stanzas/37": {"complete_stanza": "[Term]\nid: NCBITaxon:59299\nname: Streptomyces thermocarboxydus\n\n", "id": "NCBITaxon:59299", "physical_line": 27256}, "/cached_taxonomy/whole_stanzas/39": {"complete_stanza": "[Term]\nid: NCBITaxon:67267\nname: Streptomyces alboflavus\nsynonym: \"Actinomyces alboflavus\" EXACT []\nsynonym: \"Streptomyces albiflavus\" EXACT []\n\n", "id": "NCBITaxon:67267", "physical_line": 29939}, "/cached_taxonomy/whole_stanzas/4": {"complete_stanza": "[Term]\nid: NCBITaxon:1902\nname: Streptomyces coelicolor\nsynonym: \"Actinomyces coelicolor\" EXACT []\nsynonym: \"Cladothrix coelicolor\" EXACT []\nsynonym: \"Nocardia coelicolor\" EXACT []\nsynonym: \"Streptomyces coelicolor (Muller 1908) Waksman and Henrici 1948 (Approved Lists 1980)\" EXACT []\nsynonym: \"Streptomyces coelicolor subspecies coelicolor\" EXACT []\n\n", "id": "NCBITaxon:1902", "physical_line": 2915}, "/cached_taxonomy/whole_stanzas/40": {"complete_stanza": "[Term]\nid: NCBITaxon:68280\nname: Streptomyces violaceusniger\nsynonym: \"\\\"Streptomyces violaceo-niger\\\" (Waksman and Curtis 1916) Waksman and Henrici 1948\" EXACT []\nsynonym: \"Actinomyces violaceus-niger\" EXACT []\nsynonym: \"Streptomyces violaceiniger\" EXACT []\nsynonym: \"Streptomyces violaceoniger\" EXACT []\nsynonym: \"Streptomyces violaceus-niger\" EXACT []\n\n", "id": "NCBITaxon:68280", "physical_line": 30810}, "/cached_taxonomy/whole_stanzas/43": {"complete_stanza": "[Term]\nid: NCBITaxon:100226\nname: Streptomyces coelicolor A3(2)\n\n", "id": "NCBITaxon:100226", "physical_line": 41549}, "/cached_taxonomy/whole_stanzas/5": {"complete_stanza": "[Term]\nid: NCBITaxon:1911\nname: Streptomyces griseus\nsynonym: \"Streptomyces cavourensis subsp. washingtonensis\" EXACT []\nsynonym: \"Streptomyces fimicarius\" EXACT []\nsynonym: \"Streptomyces fimicarius (Duche 1934) Waksman and Henrici 1948 (Approved Lists 1980)\" EXACT []\nsynonym: \"Streptomyces griseus (Krainsky 1914) Waksman and Henrici 1948 (Approved Lists 1980)\" EXACT []\nsynonym: \"Streptomyces setonii\" EXACT []\nsynonym: \"Streptomyces setonii (Millard and Burr 1926) Waksman 1953 (Approved Lists 1980)\" EXACT []\n\n", "id": "NCBITaxon:1911", "physical_line": 2971}, "/cached_taxonomy/whole_stanzas/50": {"complete_stanza": "[Term]\nid: NCBITaxon:161934\nname: Beta vulgaris\nsynonym: \"Beta altissima\" EXACT []\n\n", "id": "NCBITaxon:161934", "physical_line": 55335}, "/cached_taxonomy/whole_stanzas/52": {"complete_stanza": "[Term]\nid: NCBITaxon:177969\nname: Oscillatoria brevis\n\n", "id": "NCBITaxon:177969", "physical_line": 59083}, "/cached_taxonomy/whole_stanzas/53": {"complete_stanza": "[Term]\nid: NCBITaxon:182063\nname: Cystoderma amianthinum\nsynonym: \"Agaricus amianthinus\" EXACT []\n\n", "id": "NCBITaxon:182063", "physical_line": 60234}, "/cached_taxonomy/whole_stanzas/6": {"complete_stanza": "[Term]\nid: NCBITaxon:1932\nname: Streptomyces tendae\n\n", "id": "NCBITaxon:1932", "physical_line": 3078}, "/cached_taxonomy/whole_stanzas/7": {"complete_stanza": "[Term]\nid: NCBITaxon:1944\nname: Streptomyces halstedii\nsynonym: \"Actinomyces halstedii\" EXACT []\n\n", "id": "NCBITaxon:1944", "physical_line": 3136}, "/cached_taxonomy/whole_stanzas/74": {"complete_stanza": "[Term]\nid: NCBITaxon:511157\nname: Cystoderma carcharias\nsynonym: \"Agaricus carcharias\" EXACT []\nsynonym: \"Cystoderma carcharias var. carcharias\" EXACT []\n\n", "id": "NCBITaxon:511157", "physical_line": 99997}, "/cached_taxonomy/whole_stanzas/9": {"complete_stanza": "[Term]\nid: NCBITaxon:3589\nname: Basella alba\n\n", "id": "NCBITaxon:3589", "physical_line": 4941}, "/cached_taxonomy/whole_stanzas/91": {"complete_stanza": "[Term]\nid: NCBITaxon:1586124\nname: Phlegmacium herculeum\nsynonym: \"Cortinarius herculeus\" EXACT []\n\n", "id": "NCBITaxon:1586124", "physical_line": 133979}} |
| support-2328-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/mibig_compounds": {"matches": [{"last_physical_line": 1404, "physical_line": 1404, "raw_tsv_record": "BGC0001181\t4\tactive\tquestionable\tunknown\tgeosmin\t1\tC[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C\tInChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1\tJLPUXFOGCDVKGO-TUAOUCFPSA-N\ttrue\t\t\tNCBITaxon:100226\tStreptomyces coelicolor A3(2)\tterpene\tSesquiterpene\tAL645882.2\t6666219\t6668399\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1038/s41564-020-0697-x\tCOMPOUND_BIOACTIVITY\n", "row": {"bgc_classes": "terpene", "bgc_subclasses": "Sesquiterpene", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "geosmin", "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "4", "genome_accession": "AL645882.2", "locus_evidence_methods": "", "locus_from": "6666219", "locus_to": "6668399", "mibig_accession": "BGC0001181", "primary_reference": "DOI:10.1038/s41564-020-0697-x", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "COMPOUND_BIOACTIVITY", "smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:100226", "taxon_label": "Streptomyces coelicolor A3(2)"}, "row_sha256": "6704a99b28e0eb8375c36f67355e689d61466deffcb2f0a9ee54edf98d764ad6"}], "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}} |
| support-2328-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 1404–1404, row_sha256 6704a99b28e0eb8375c36f67355e689d61466deffcb2f0a9ee54edf98d764ad6 | supports | Complete retained physical row fields: [{"bgc_classes": "terpene", "bgc_subclasses": "Sesquiterpene", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "geosmin", "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "4", "genome_accession": "AL645882.2", "locus_evidence_methods": "", "locus_from": "6666219", "locus_to": "6668399", "mibig_accession": "BGC0001181", "primary_reference": "DOI:10.1038/s41564-020-0697-x", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "COMPOUND_BIOACTIVITY", "smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:100226", "taxon_label": "Streptomyces coelicolor A3(2)"}] |
| support-2328-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/chebi_structures": {"matches": [{"last_physical_line": 12450, "physical_line": 12450, "raw_tsv_record": "CHEBI:46702\t(−)-geosmin\tThe (−)-stereoisomer of geosmin, having 4S,4aS,8aR configuration.\t3\tJLPUXFOGCDVKGO-TUAOUCFPSA-N\tC[C@H]1CCC[C@@]2(C)CCCC[C@]12O\n", "row": {"chebi_id": "CHEBI:46702", "definition": "The (−)-stereoisomer of geosmin, having 4S,4aS,8aR configuration.", "name": "(−)-geosmin", "smiles": "C[C@H]1CCC[C@@]2(C)CCCC[C@]12O", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stars": "3"}, "row_sha256": "76866239889b583a5ce6fdaa036a2a7ad89e6004a762f614e039bb206fd7e094"}], "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}} |
| support-2328-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line 1; physical lines 12450–12450, row_sha256 76866239889b583a5ce6fdaa036a2a7ad89e6004a762f614e039bb206fd7e094 | supports | Complete retained physical row fields: [{"chebi_id": "CHEBI:46702", "definition": "The (−)-stereoisomer of geosmin, having 4S,4aS,8aR configuration.", "name": "(−)-geosmin", "smiles": "C[C@H]1CCC[C@@]2(C)CCCC[C@]12O", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stars": "3"}] |
| support-2328-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/lotus_occurrences": {"matches": [{"last_physical_line": 3400, "physical_line": 3400, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCoffea arabica\tNCBITaxon:13443\thttp://www.wikidata.org/entity/Q47685\t10.1007/S002170100305\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Coffea arabica", "organism_wikidata": "http://www.wikidata.org/entity/Q47685", "reference_doi": "10.1007/S002170100305", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:13443"}, "row_sha256": "f39c8894cd66b13bcf803bd3645fff0697a9ea6a90d6cd542b640c5e544e4851"}, {"last_physical_line": 3401, "physical_line": 3401, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCortinarius herculeus\tNCBITaxon:1586124\thttp://www.wikidata.org/entity/Q84325870\t10.1080/00275514.1999.12060999\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Cortinarius herculeus", "organism_wikidata": "http://www.wikidata.org/entity/Q84325870", "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1586124"}, "row_sha256": "853e818c627de61a1f130746bf13f1a431e19b8673f6a2f7e63e1786670895e7"}, {"last_physical_line": 3402, "physical_line": 3402, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCortinarius herculeus\tNCBITaxon:1586124\thttp://www.wikidata.org/entity/Q84325870\t10.2307/3761199\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Cortinarius herculeus", "organism_wikidata": "http://www.wikidata.org/entity/Q84325870", "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1586124"}, "row_sha256": "f7d1581b4962994647e99120bdca4f6cf152b4ae9393fcf72969717c73267747"}, {"last_physical_line": 3403, "physical_line": 3403, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tBeta vulgaris\tNCBITaxon:161934\thttp://www.wikidata.org/entity/Q165191\t10.1021/JF60204A059\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Beta vulgaris", "organism_wikidata": "http://www.wikidata.org/entity/Q165191", "reference_doi": "10.1021/JF60204A059", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:161934"}, "row_sha256": "85ae3b7d13f9008263b8eaa5a5756d739c445a12c52c9705c4e3ed17f04b552e"}, {"last_physical_line": 3404, "physical_line": 3404, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tOscillatoria brevis\tNCBITaxon:177969\thttp://www.wikidata.org/entity/Q39087436\t10.1007/BF00416598\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Oscillatoria brevis", "organism_wikidata": "http://www.wikidata.org/entity/Q39087436", "reference_doi": "10.1007/BF00416598", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:177969"}, "row_sha256": "a675146489fd8da933fdb3eefd846ede4962f6a46c2f3d14323d0f6ca38ca775"}, {"last_physical_line": 3405, "physical_line": 3405, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCystoderma amianthinum\tNCBITaxon:182063\thttp://www.wikidata.org/entity/Q470766\t10.1080/00275514.1999.12060999\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Cystoderma amianthinum", "organism_wikidata": "http://www.wikidata.org/entity/Q470766", "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:182063"}, "row_sha256": "d4e32c23e78cf6c8eb737bca2a7e1f104c9c22bc99f5d13760d45249cf9ad385"}, {"last_physical_line": 3406, "physical_line": 3406, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCystoderma amianthinum\tNCBITaxon:182063\thttp://www.wikidata.org/entity/Q470766\t10.2307/3761199\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Cystoderma amianthinum", "organism_wikidata": "http://www.wikidata.org/entity/Q470766", "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:182063"}, "row_sha256": "7099822ac917ac35022ebdcb47dda5a2f6691606aa34b6ed1f0f26d0ec822645"}, {"last_physical_line": 3407, "physical_line": 3407, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces\tNCBITaxon:1883\thttp://www.wikidata.org/entity/Q1144013\t10.1016/J.YMBEN.2018.09.004\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces", "organism_wikidata": "http://www.wikidata.org/entity/Q1144013", "reference_doi": "10.1016/J.YMBEN.2018.09.004", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1883"}, "row_sha256": "95a5af39ae07f3a86a47b7700cc0a1fa7e09de4201444298d33155068e50c285"}, {"last_physical_line": 3408, "physical_line": 3408, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.1007/S10295-013-1383-2\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.1007/S10295-013-1383-2", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, "row_sha256": "566422294c2282e2b959f44d4c3125ea28e9e491c8801605970cc8dda41d3332"}, {"last_physical_line": 3409, "physical_line": 3409, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.1016/B978-0-12-404634-4.00014-0\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.1016/B978-0-12-404634-4.00014-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, "row_sha256": "21e457a613f7ce6f69a3b88731200fd74a766a7a626be163a58bc876bc0ef1fd"}, {"last_physical_line": 3410, "physical_line": 3410, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.1021/JA062669X\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.1021/JA062669X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, "row_sha256": "3c516ccb9ab97d4cd1576721f86438b9b1766c3f1e3f63ad5b1b5cc291386b7e"}, {"last_physical_line": 3411, "physical_line": 3411, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.1038/NCHEMBIO.2007.29\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.1038/NCHEMBIO.2007.29", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, "row_sha256": "99e9b351b0392ac5a4bbb8cd0b765620743456548b729dd4ebb5b29cf93a5f17"}, {"last_physical_line": 3412, "physical_line": 3412, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.1371/JOURNAL.PONE.0060665\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.1371/JOURNAL.PONE.0060665", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, "row_sha256": "bf071144c166ed8425b104d63e98ec364b4e125c6ab6d05171db6507d4bdf296"}, {"last_physical_line": 3413, "physical_line": 3413, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.7164/ANTIBIOTICS.47.434\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.7164/ANTIBIOTICS.47.434", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, "row_sha256": "02a068b81663e63db6789cc1f4185b5ecf2d3f4a70f3f35bb5167c2e6929d8d6"}, {"last_physical_line": 3414, "physical_line": 3414, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces coelicolor\tNCBITaxon:1902\thttp://www.wikidata.org/entity/Q2355919\t10.1007/S10295-013-1383-2\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919", "reference_doi": "10.1007/S10295-013-1383-2", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"}, "row_sha256": "1f890a991496e8905b030e038d4ac45cdafed7483aa3e6171300b6c4f3f518bb"}, {"last_physical_line": 3415, "physical_line": 3415, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces coelicolor\tNCBITaxon:1902\thttp://www.wikidata.org/entity/Q2355919\t10.1016/B978-0-12-404634-4.00014-0\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919", "reference_doi": "10.1016/B978-0-12-404634-4.00014-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"}, "row_sha256": "ecc92e79bf7a18729488c6376c06cdfb5120795582adadefd4b88b73a9de849c"}, {"last_physical_line": 3416, "physical_line": 3416, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces coelicolor\tNCBITaxon:1902\thttp://www.wikidata.org/entity/Q2355919\t10.1021/JA062669X\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919", "reference_doi": "10.1021/JA062669X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"}, "row_sha256": "6d38a8437c1b1f607271dd42f890d80660dd59acbdf766d69af993f40d7d4632"}, {"last_physical_line": 3417, "physical_line": 3417, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces coelicolor\tNCBITaxon:1902\thttp://www.wikidata.org/entity/Q2355919\t10.1038/NCHEMBIO.2007.29\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919", "reference_doi": "10.1038/NCHEMBIO.2007.29", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"}, "row_sha256": "ce92ad966f3d83defd6be290bfd8fc658c74664a418d049601db6b79e50d5916"}, {"last_physical_line": 3418, "physical_line": 3418, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces coelicolor\tNCBITaxon:1902\thttp://www.wikidata.org/entity/Q2355919\t10.1371/JOURNAL.PONE.0060665\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919", "reference_doi": "10.1371/JOURNAL.PONE.0060665", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"}, "row_sha256": "9caf9d4eecbf52bd7469ef8979a78864b01732a08378b3b8f03054202f1df44f"}, {"last_physical_line": 3419, "physical_line": 3419, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces griseus\tNCBITaxon:1911\thttp://www.wikidata.org/entity/Q7623385\t10.1111/J.1365-2672.1992.TB01818.X\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces griseus", "organism_wikidata": "http://www.wikidata.org/entity/Q7623385", "reference_doi": "10.1111/J.1365-2672.1992.TB01818.X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1911"}, "row_sha256": "248c59284d20d9a59fd6f76dda150ca1c0f286a73ac6ccc80635f33454b0c13a"}, {"last_physical_line": 3420, "physical_line": 3420, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces tendae\tNCBITaxon:1932\thttp://www.wikidata.org/entity/Q26292941\t10.1021/JF00013A023\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces tendae", "organism_wikidata": "http://www.wikidata.org/entity/Q26292941", "reference_doi": "10.1021/JF00013A023", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1932"}, "row_sha256": "f48204609c585a373b268b5bfa820380c67438be301fe905596458bc8edccffb"}, {"last_physical_line": 3421, "physical_line": 3421, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces tendae\tNCBITaxon:1932\thttp://www.wikidata.org/entity/Q26292941\t10.1128/AEM.57.12.3429-3432.1991\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces tendae", "organism_wikidata": "http://www.wikidata.org/entity/Q26292941", "reference_doi": "10.1128/AEM.57.12.3429-3432.1991", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1932"}, "row_sha256": "157461c537f7ab0da7e9b4607668ee0ae13f1a5e1016f579093d6954499ca0bc"}, {"last_physical_line": 3422, "physical_line": 3422, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces halstedii\tNCBITaxon:1944\thttp://www.wikidata.org/entity/Q22665882\t10.1038/SJ.JIM.7000121\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces halstedii", "organism_wikidata": "http://www.wikidata.org/entity/Q22665882", "reference_doi": "10.1038/SJ.JIM.7000121", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1944"}, "row_sha256": "2f597a7a73224b7d4f246a3e5810500c3ebcc453fd524b97e55f304e69db0f26"}, {"last_physical_line": 3423, "physical_line": 3423, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces avermitilis\tNCBITaxon:33903\thttp://www.wikidata.org/entity/Q1946562\t10.1007/BF02932133\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562", "reference_doi": "10.1007/BF02932133", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:33903"}, "row_sha256": "779eec39f7b00feb8acabaa993b20f6784196620098e5de893c37fce4ee7d871"}, {"last_physical_line": 3424, "physical_line": 3424, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces avermitilis\tNCBITaxon:33903\thttp://www.wikidata.org/entity/Q1946562\t10.1038/JA.2006.66\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562", "reference_doi": "10.1038/JA.2006.66", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:33903"}, "row_sha256": "bfabd1276aa3dcfef734119a8c7da4ba9eb2f9c0ffd920568614bd4218751315"}, {"last_physical_line": 3425, "physical_line": 3425, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tBasella alba\tNCBITaxon:3589\thttp://www.wikidata.org/entity/Q1130368\t10.1016/0889-1575(91)90017-Z\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Basella alba", "organism_wikidata": "http://www.wikidata.org/entity/Q1130368", "reference_doi": "10.1016/0889-1575(91)90017-Z", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:3589"}, "row_sha256": "ab9e8cbb6ee1a05314c4710d462928a560decf314681ba2f8db1b8829820f889"}, {"last_physical_line": 3426, "physical_line": 3426, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tChaetomium globosum\tNCBITaxon:38033\thttp://www.wikidata.org/entity/Q2947551\t10.1248/CPB.29.1782\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Chaetomium globosum", "organism_wikidata": "http://www.wikidata.org/entity/Q2947551", "reference_doi": "10.1248/CPB.29.1782", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:38033"}, "row_sha256": "02c65c91a5769170c16facadcb501e97e83e389c554f69c71b9d77d03610969a"}, {"last_physical_line": 3427, "physical_line": 3427, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tChaetomium globosum\tNCBITaxon:38033\thttp://www.wikidata.org/entity/Q2947551\t10.1248/CPB.31.659\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Chaetomium globosum", "organism_wikidata": "http://www.wikidata.org/entity/Q2947551", "reference_doi": "10.1248/CPB.31.659", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:38033"}, "row_sha256": "d052d91d92526058cc3e69f52ea1344d1cd30595e1d0ebe7c533beacf3de2664"}, {"last_physical_line": 3428, "physical_line": 3428, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tPhaseolus vulgaris\tNCBITaxon:3885\thttp://www.wikidata.org/entity/Q42339\t10.1021/JF60204A050\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Phaseolus vulgaris", "organism_wikidata": "http://www.wikidata.org/entity/Q42339", "reference_doi": "10.1021/JF60204A050", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:3885"}, "row_sha256": "a9ae78c91d53d7d5cd8d40f56b284e88cd4ee0bb7b0e1691be8d26c3172d8e3d"}, {"last_physical_line": 3429, "physical_line": 3429, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces nodosus\tNCBITaxon:40318\thttp://www.wikidata.org/entity/Q16759083\t10.1007/S00253-015-7060-9\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces nodosus", "organism_wikidata": "http://www.wikidata.org/entity/Q16759083", "reference_doi": "10.1007/S00253-015-7060-9", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:40318"}, "row_sha256": "01ce925e9fe51ba8393a352587ccac012437a9aa565f9c523a92c38d9f153e5f"}, {"last_physical_line": 3430, "physical_line": 3430, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces nodosus\tNCBITaxon:40318\thttp://www.wikidata.org/entity/Q16759083\t10.1016/S0031-9422(02)00282-0\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces nodosus", "organism_wikidata": "http://www.wikidata.org/entity/Q16759083", "reference_doi": "10.1016/S0031-9422(02)00282-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:40318"}, "row_sha256": "30f6aa62ec38509dadb35027f807133845faf3aa6a4b9cb9e55708675af566b8"}, {"last_physical_line": 3431, "physical_line": 3431, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces collinus\tNCBITaxon:42684\thttp://www.wikidata.org/entity/Q22287122\t10.1007/S10295-015-1685-7\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces collinus", "organism_wikidata": "http://www.wikidata.org/entity/Q22287122", "reference_doi": "10.1007/S10295-015-1685-7", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:42684"}, "row_sha256": "6909114cdaa1bc7e56c0ff9ecab414072d3928549b453f0e1633fc9061937c75"}, {"last_physical_line": 3432, "physical_line": 3432, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tZea mays\tNCBITaxon:4577\thttp://www.wikidata.org/entity/Q11575\t10.1021/JF60218A022\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Zea mays", "organism_wikidata": "http://www.wikidata.org/entity/Q11575", "reference_doi": "10.1021/JF60218A022", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:4577"}, "row_sha256": "40ca61bf73b706b01f9797afd0f3f0edc56a6d405cd69999d1d2e44ca265cbdd"}, {"last_physical_line": 3433, "physical_line": 3433, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tZea mays\tNCBITaxon:4577\thttp://www.wikidata.org/entity/Q11575\t10.1021/JF60220A012\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Zea mays", "organism_wikidata": "http://www.wikidata.org/entity/Q11575", "reference_doi": "10.1021/JF60220A012", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:4577"}, "row_sha256": "4aeddbf3e4f114f5a13100df1b77d4c17b3e35a5a2d17b9bbc0b1aee5dda684d"}, {"last_physical_line": 3434, "physical_line": 3434, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCystoderma carcharias\tNCBITaxon:511157\thttp://www.wikidata.org/entity/Q2640662\t10.1080/00275514.1999.12060999\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Cystoderma carcharias", "organism_wikidata": "http://www.wikidata.org/entity/Q2640662", "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:511157"}, "row_sha256": "628094eba90ad4db960756763055ea96b9da1e0fa041d59f393867034f130fd0"}, {"last_physical_line": 3435, "physical_line": 3435, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCystoderma carcharias\tNCBITaxon:511157\thttp://www.wikidata.org/entity/Q2640662\t10.2307/3761199\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Cystoderma carcharias", "organism_wikidata": "http://www.wikidata.org/entity/Q2640662", "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:511157"}, "row_sha256": "cb57ed522a0ef4fda608802169abc5c0b1a1e7b133f4bbee2bd8e795ee75ab57"}, {"last_physical_line": 3436, "physical_line": 3436, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tSymphyogyna brongniartii\tNCBITaxon:53033\thttp://www.wikidata.org/entity/Q17268765\t10.1515/ZNC-1991-3-404\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Symphyogyna brongniartii", "organism_wikidata": "http://www.wikidata.org/entity/Q17268765", "reference_doi": "10.1515/ZNC-1991-3-404", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:53033"}, "row_sha256": "16697d76b4a0dd3f6aa126c9de6f8601d74231ef6da9a8091e8128f79a13e866"}, {"last_physical_line": 3437, "physical_line": 3437, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tPhysarum polycephalum\tNCBITaxon:5791\thttp://www.wikidata.org/entity/Q134950\t10.1248/CPB.32.797\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Physarum polycephalum", "organism_wikidata": "http://www.wikidata.org/entity/Q134950", "reference_doi": "10.1248/CPB.32.797", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:5791"}, "row_sha256": "8ee7a4b00c045b2f2da9448f366f16a80d5172ad445346bee273faec07f95829"}, {"last_physical_line": 3438, "physical_line": 3438, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces thermocarboxydus\tNCBITaxon:59299\thttp://www.wikidata.org/entity/Q16992819\t10.1007/S00253-019-10240-3\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces thermocarboxydus", "organism_wikidata": "http://www.wikidata.org/entity/Q16992819", "reference_doi": "10.1007/S00253-019-10240-3", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:59299"}, "row_sha256": "aedfb016c3fc799bb52079a8ce9281c74b2006a43844379a67368d6438f4f4a6"}, {"last_physical_line": 3439, "physical_line": 3439, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces alboflavus\tNCBITaxon:67267\thttp://www.wikidata.org/entity/Q22286851\t10.1111/1574-6968.12088\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces alboflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286851", "reference_doi": "10.1111/1574-6968.12088", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:67267"}, "row_sha256": "3daf3a2b747d942c3dd4e1c403b6fb30715bf4c90652b01bf4b3aedf7ef90d3f"}, {"last_physical_line": 3440, "physical_line": 3440, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces violaceusniger\tNCBITaxon:68280\thttp://www.wikidata.org/entity/Q26293318\t10.1039/C4CC00177J\thttp://www.wikidata.org/entity/Q420233\n", "row": {"organism_name": "Streptomyces violaceusniger", "organism_wikidata": "http://www.wikidata.org/entity/Q26293318", "reference_doi": "10.1039/C4CC00177J", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:68280"}, "row_sha256": "bdd70c803dc6ea84e1a782b3949fd50d70308c0180dacad7dc222e35b7353edb"}], "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}} |
| support-2328-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 3400–3400, row_sha256 f39c8894cd66b13bcf803bd3645fff0697a9ea6a90d6cd542b640c5e544e4851; physical lines 3401–3401, row_sha256 853e818c627de61a1f130746bf13f1a431e19b8673f6a2f7e63e1786670895e7; physical lines 3402–3402, row_sha256 f7d1581b4962994647e99120bdca4f6cf152b4ae9393fcf72969717c73267747; physical lines 3403–3403, row_sha256 85ae3b7d13f9008263b8eaa5a5756d739c445a12c52c9705c4e3ed17f04b552e; physical lines 3404–3404, row_sha256 a675146489fd8da933fdb3eefd846ede4962f6a46c2f3d14323d0f6ca38ca775; physical lines 3405–3405, row_sha256 d4e32c23e78cf6c8eb737bca2a7e1f104c9c22bc99f5d13760d45249cf9ad385; physical lines 3406–3406, row_sha256 7099822ac917ac35022ebdcb47dda5a2f6691606aa34b6ed1f0f26d0ec822645; physical lines 3407–3407, row_sha256 95a5af39ae07f3a86a47b7700cc0a1fa7e09de4201444298d33155068e50c285; physical lines 3408–3408, row_sha256 566422294c2282e2b959f44d4c3125ea28e9e491c8801605970cc8dda41d3332; physical lines 3409–3409, row_sha256 21e457a613f7ce6f69a3b88731200fd74a766a7a626be163a58bc876bc0ef1fd; physical lines 3410–3410, row_sha256 3c516ccb9ab97d4cd1576721f86438b9b1766c3f1e3f63ad5b1b5cc291386b7e; physical lines 3411–3411, row_sha256 99e9b351b0392ac5a4bbb8cd0b765620743456548b729dd4ebb5b29cf93a5f17; physical lines 3412–3412, row_sha256 bf071144c166ed8425b104d63e98ec364b4e125c6ab6d05171db6507d4bdf296; physical lines 3413–3413, row_sha256 02a068b81663e63db6789cc1f4185b5ecf2d3f4a70f3f35bb5167c2e6929d8d6; physical lines 3414–3414, row_sha256 1f890a991496e8905b030e038d4ac45cdafed7483aa3e6171300b6c4f3f518bb; physical lines 3415–3415, row_sha256 ecc92e79bf7a18729488c6376c06cdfb5120795582adadefd4b88b73a9de849c; physical lines 3416–3416, row_sha256 6d38a8437c1b1f607271dd42f890d80660dd59acbdf766d69af993f40d7d4632; physical lines 3417–3417, row_sha256 ce92ad966f3d83defd6be290bfd8fc658c74664a418d049601db6b79e50d5916; physical lines 3418–3418, row_sha256 9caf9d4eecbf52bd7469ef8979a78864b01732a08378b3b8f03054202f1df44f; physical lines 3419–3419, row_sha256 248c59284d20d9a59fd6f76dda150ca1c0f286a73ac6ccc80635f33454b0c13a; physical lines 3420–3420, row_sha256 f48204609c585a373b268b5bfa820380c67438be301fe905596458bc8edccffb; physical lines 3421–3421, row_sha256 157461c537f7ab0da7e9b4607668ee0ae13f1a5e1016f579093d6954499ca0bc; physical lines 3422–3422, row_sha256 2f597a7a73224b7d4f246a3e5810500c3ebcc453fd524b97e55f304e69db0f26; physical lines 3423–3423, row_sha256 779eec39f7b00feb8acabaa993b20f6784196620098e5de893c37fce4ee7d871; physical lines 3424–3424, row_sha256 bfabd1276aa3dcfef734119a8c7da4ba9eb2f9c0ffd920568614bd4218751315; physical lines 3425–3425, row_sha256 ab9e8cbb6ee1a05314c4710d462928a560decf314681ba2f8db1b8829820f889; physical lines 3426–3426, row_sha256 02c65c91a5769170c16facadcb501e97e83e389c554f69c71b9d77d03610969a; physical lines 3427–3427, row_sha256 d052d91d92526058cc3e69f52ea1344d1cd30595e1d0ebe7c533beacf3de2664; physical lines 3428–3428, row_sha256 a9ae78c91d53d7d5cd8d40f56b284e88cd4ee0bb7b0e1691be8d26c3172d8e3d; physical lines 3429–3429, row_sha256 01ce925e9fe51ba8393a352587ccac012437a9aa565f9c523a92c38d9f153e5f; physical lines 3430–3430, row_sha256 30f6aa62ec38509dadb35027f807133845faf3aa6a4b9cb9e55708675af566b8; physical lines 3431–3431, row_sha256 6909114cdaa1bc7e56c0ff9ecab414072d3928549b453f0e1633fc9061937c75; physical lines 3432–3432, row_sha256 40ca61bf73b706b01f9797afd0f3f0edc56a6d405cd69999d1d2e44ca265cbdd; physical lines 3433–3433, row_sha256 4aeddbf3e4f114f5a13100df1b77d4c17b3e35a5a2d17b9bbc0b1aee5dda684d; physical lines 3434–3434, row_sha256 628094eba90ad4db960756763055ea96b9da1e0fa041d59f393867034f130fd0; physical lines 3435–3435, row_sha256 cb57ed522a0ef4fda608802169abc5c0b1a1e7b133f4bbee2bd8e795ee75ab57; physical lines 3436–3436, row_sha256 16697d76b4a0dd3f6aa126c9de6f8601d74231ef6da9a8091e8128f79a13e866; physical lines 3437–3437, row_sha256 8ee7a4b00c045b2f2da9448f366f16a80d5172ad445346bee273faec07f95829; physical lines 3438–3438, row_sha256 aedfb016c3fc799bb52079a8ce9281c74b2006a43844379a67368d6438f4f4a6; physical lines 3439–3439, row_sha256 3daf3a2b747d942c3dd4e1c403b6fb30715bf4c90652b01bf4b3aedf7ef90d3f; physical lines 3440–3440, row_sha256 bdd70c803dc6ea84e1a782b3949fd50d70308c0180dacad7dc222e35b7353edb | supports | Complete retained physical row fields: [{"organism_name": "Coffea arabica", "organism_wikidata": "http://www.wikidata.org/entity/Q47685", "reference_doi": "10.1007/S002170100305", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:13443"}, {"organism_name": "Cortinarius herculeus", "organism_wikidata": "http://www.wikidata.org/entity/Q84325870", "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1586124"}, {"organism_name": "Cortinarius herculeus", "organism_wikidata": "http://www.wikidata.org/entity/Q84325870", "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1586124"}, {"organism_name": "Beta vulgaris", "organism_wikidata": "http://www.wikidata.org/entity/Q165191", "reference_doi": "10.1021/JF60204A059", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:161934"}, {"organism_name": "Oscillatoria brevis", "organism_wikidata": "http://www.wikidata.org/entity/Q39087436", "reference_doi": "10.1007/BF00416598", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:177969"}, {"organism_name": "Cystoderma amianthinum", "organism_wikidata": "http://www.wikidata.org/entity/Q470766", "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:182063"}, {"organism_name": "Cystoderma amianthinum", "organism_wikidata": "http://www.wikidata.org/entity/Q470766", "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:182063"}, {"organism_name": "Streptomyces", "organism_wikidata": "http://www.wikidata.org/entity/Q1144013", "reference_doi": "10.1016/J.YMBEN.2018.09.004", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1883"}, {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.1007/S10295-013-1383-2", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.1016/B978-0-12-404634-4.00014-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.1021/JA062669X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.1038/NCHEMBIO.2007.29", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.1371/JOURNAL.PONE.0060665", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833", "reference_doi": "10.7164/ANTIBIOTICS.47.434", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"}, {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919", "reference_doi": "10.1007/S10295-013-1383-2", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"}, {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919", "reference_doi": "10.1016/B978-0-12-404634-4.00014-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"}, {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919", "reference_doi": "10.1021/JA062669X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"}, {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919", "reference_doi": "10.1038/NCHEMBIO.2007.29", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"}, {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919", "reference_doi": "10.1371/JOURNAL.PONE.0060665", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"}, {"organism_name": "Streptomyces griseus", "organism_wikidata": "http://www.wikidata.org/entity/Q7623385", "reference_doi": "10.1111/J.1365-2672.1992.TB01818.X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1911"}, {"organism_name": "Streptomyces tendae", "organism_wikidata": "http://www.wikidata.org/entity/Q26292941", "reference_doi": "10.1021/JF00013A023", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1932"}, {"organism_name": "Streptomyces tendae", "organism_wikidata": "http://www.wikidata.org/entity/Q26292941", "reference_doi": "10.1128/AEM.57.12.3429-3432.1991", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1932"}, {"organism_name": "Streptomyces halstedii", "organism_wikidata": "http://www.wikidata.org/entity/Q22665882", "reference_doi": "10.1038/SJ.JIM.7000121", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1944"}, {"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562", "reference_doi": "10.1007/BF02932133", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:33903"}, {"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562", "reference_doi": "10.1038/JA.2006.66", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:33903"}, {"organism_name": "Basella alba", "organism_wikidata": "http://www.wikidata.org/entity/Q1130368", "reference_doi": "10.1016/0889-1575(91)90017-Z", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:3589"}, {"organism_name": "Chaetomium globosum", "organism_wikidata": "http://www.wikidata.org/entity/Q2947551", "reference_doi": "10.1248/CPB.29.1782", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:38033"}, {"organism_name": "Chaetomium globosum", "organism_wikidata": "http://www.wikidata.org/entity/Q2947551", "reference_doi": "10.1248/CPB.31.659", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:38033"}, {"organism_name": "Phaseolus vulgaris", "organism_wikidata": "http://www.wikidata.org/entity/Q42339", "reference_doi": "10.1021/JF60204A050", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:3885"}, {"organism_name": "Streptomyces nodosus", "organism_wikidata": "http://www.wikidata.org/entity/Q16759083", "reference_doi": "10.1007/S00253-015-7060-9", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:40318"}, {"organism_name": "Streptomyces nodosus", "organism_wikidata": "http://www.wikidata.org/entity/Q16759083", "reference_doi": "10.1016/S0031-9422(02)00282-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:40318"}, {"organism_name": "Streptomyces collinus", "organism_wikidata": "http://www.wikidata.org/entity/Q22287122", "reference_doi": "10.1007/S10295-015-1685-7", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:42684"}, {"organism_name": "Zea mays", "organism_wikidata": "http://www.wikidata.org/entity/Q11575", "reference_doi": "10.1021/JF60218A022", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:4577"}, {"organism_name": "Zea mays", "organism_wikidata": "http://www.wikidata.org/entity/Q11575", "reference_doi": "10.1021/JF60220A012", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:4577"}, {"organism_name": "Cystoderma carcharias", "organism_wikidata": "http://www.wikidata.org/entity/Q2640662", "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:511157"}, {"organism_name": "Cystoderma carcharias", "organism_wikidata": "http://www.wikidata.org/entity/Q2640662", "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:511157"}, {"organism_name": "Symphyogyna brongniartii", "organism_wikidata": "http://www.wikidata.org/entity/Q17268765", "reference_doi": "10.1515/ZNC-1991-3-404", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:53033"}, {"organism_name": "Physarum polycephalum", "organism_wikidata": "http://www.wikidata.org/entity/Q134950", "reference_doi": "10.1248/CPB.32.797", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:5791"}, {"organism_name": "Streptomyces thermocarboxydus", "organism_wikidata": "http://www.wikidata.org/entity/Q16992819", "reference_doi": "10.1007/S00253-019-10240-3", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:59299"}, {"organism_name": "Streptomyces alboflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286851", "reference_doi": "10.1111/1574-6968.12088", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:67267"}, {"organism_name": "Streptomyces violaceusniger", "organism_wikidata": "http://www.wikidata.org/entity/Q26293318", "reference_doi": "10.1039/C4CC00177J", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:68280"}] |
| support-2328-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/cyanometdb_occurrences": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}} |
| support-2328-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/npclassifier": {"matches": [{"last_physical_line": 1128, "physical_line": 1128, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tC[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C\tTerpenoids\tSesquiterpenoids\tEudesmane sesquiterpenoids&#124;Noreudesmane sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results": "Eudesmane sesquiterpenoids&#124;Noreudesmane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "superclass_results": "Sesquiterpenoids"}, "row_sha256": "d7a04a9b9d0fd8865254139891ef4e5a447c86bdb02c2c4e0bd65165ce344ebf"}], "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}} |
| support-2328-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 1128–1128, row_sha256 d7a04a9b9d0fd8865254139891ef4e5a447c86bdb02c2c4e0bd65165ce344ebf | supports | Complete retained physical row fields: [{"class_results": "Eudesmane sesquiterpenoids&#124;Noreudesmane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "superclass_results": "Sesquiterpenoids"}] |
| support-2328-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/pubchem_bioassay": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}} |
| support-2328-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/bindingdb_targets": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}} |
| support-2328-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/antibioticmech_inchikeys": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}} |
| support-2328-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/chebi_origins": {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows", "query": ["CHEBI:46702"]}} |
| support-2328-direct-contexts | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /records/7/direct_companion_paths; /records/7/direct_companion_predicates | supports | Exact direct companion scope; shared locus/key predicates do not transfer identity or evidence. Exact copied saved values: {"/records/7/direct_companion_paths": [], "/records/7/direct_companion_predicates": []} |
| support-2328-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /records/7/direct_companion_paths | supports | Complete source and raw/history context carries remain explicitly attributed in source notes. Distinct companion metadata: [] |
| support-2328-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 175–200; lines 368–435 | supports | Schema distinguishes retained structures, partial stereo and versioned computed classification from experimentally asserted identity. |
| support-2328-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 145–174 | supports | Source stereo_complete derives from unassigned tetrahedral centers in source SMILES; predicate inspection does not establish natural stereochemistry. |
| support-2328-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 296–307; lines 982–1020 | supports | Maintained seeder preserves source structure and versioned model arrays; no regeneration was run for scientific authoring. |
| support-2328-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | Twelve scientific dimensions, claim-specific evidence and partial completion reflect actual access limits. |
| support-2328-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill under absolute user no-outbound constraint | supports | Read-only review, source ownership and no native-status promotion apply; no external lookup was authorized. |
| support-2328-mechanism-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/7/owner_document/causal_graphs; /records/7/owner_document/biosynthetic_pathway; /records/7/owner_document/curation_history | supports | Complete retained graph/pathway/history, with historical primary-experiment labels and protein mapping distinct from fresh verification. Exact copied saved values: {"/records/7/owner_document/biosynthetic_pathway": [{"enzyme_id": "UniProtKB:Q9X839", "enzyme_label": "Cyc2 germacradienol/germacrene D synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "notes": "The N-terminal domain of bifunctional Cyc2 cyclizes (2E,6E)-farnesyl diphosphate to germacradienol, the sesquiterpene alcohol intermediate in geosmin biosynthesis.", "product": "CHEBI:46734", "reaction_id": "RHEA:22436", "step_number": 1, "substrate": "CHEBI:175763"}, {"enzyme_id": "UniProtKB:Q9X839", "enzyme_label": "Cyc2 geosmin synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "notes": "The C-terminal domain of bifunctional Cyc2 converts germacradienol to (−)-geosmin.", "product": "CHEBI:46702", "reaction_id": "RHEA:30371", "step_number": 2, "substrate": "CHEBI:46734"}], "/records/7/owner_document/causal_graphs": [{"description": "Partial Streptomyces coelicolor geosmin biosynthesis graph for bifunctional Cyc2 conversion of farnesyl diphosphate to (−)-geosmin through germacradienol.", "edges": [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "object": "cyc2", "predicate": "is cyclized by", "subject": "farnesyl_diphosphate"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "object": "germacradienol", "predicate": "forms", "subject": "cyc2"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "object": "cyc2", "predicate": "is converted by", "subject": "germacradienol"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "object": "geosmin", "predicate": "forms", "subject": "cyc2"}], "graph_id": "geosmin-cyc2-biosynthesis", "nodes": [{"grounding_status": "GROUNDED", "identifier": "CHEBI:175763", "label": "(2E,6E)-farnesyl diphosphate", "node_id": "farnesyl_diphosphate", "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED", "identifier": "UniProtKB:Q9X839", "label": "Cyc2", "node_id": "cyc2", "node_type": "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46734", "label": "germacradienol", "node_id": "germacradienol", "node_type": "COMPOUND"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46702", "label": "(−)-geosmin", "node_id": "geosmin", "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"}], "/records/7/owner_document/curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:08Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:02:26Z"}, {"action": "RECORD_CURATED", "changes": "Added a two-step BIOSYNTHESIS pathway and causal graph for geosmin biosynthesis; grounded the Streptomyces coelicolor bifunctional Cyc2 enzyme to UniProtKB:Q9X839 via SCO6073; and cited the experimentally characterized RHEA:22436 and RHEA:30371 reactions.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-26T22:48:26Z"}, {"action": "RECORD_CURATED", "changes": "Replaced the geosmin-forming Cyc2 step and edge evidence with the domain-resolved bifunctional geosmin synthase paper, DOI:10.1038/nchembio.2007.29.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-26T23:08:49Z"}]} |
| support-2328-reader | /private/tmp/npm-review-work/shared-next-batch233/native-current233-geosmin-maintained-reader-DATA-001.json; /status; /counts; /returned_view_equals_expected_complete_owner; /view_mismatches; /resolved_view/causal_graphs; /resolved_view/biosynthetic_pathway; /resolved_view/curation_history; /limitations | supports | Accepted maintained result preserves the complete owner and exact historical mechanism. No primary/sequence verification is added. Exact copied saved values: {"/counts": {"component_graphs": 0, "component_history_events": [], "component_refs": 0, "curation_history": 4, "edges": 4, "graphs": 1, "inline_graphs": 1, "molecular_targets": 0, "nodes": 4, "pathway_steps": 2}, "/limitations": ["Maintained topology and, where references exist, component schema/ownership/history validation are distinct from complete-owner preservation. They do not independently verify mechanism science, primary publications, sequences, constructs, groundings or the full owner schema.", "The expected-view object is a comparison oracle from the separately captured complete owner and complete ordered components; only causal_graphs is expanded. It is not a substitute for the one maintained call.", "Every owner field, target measurement/evidence item, pathway item and owner history is preserved; raw root presence is checked exactly, and only resolved causal_graphs may be added for a component-only owner. Referenced graphs append after inline graphs in exact reference order. Complete component documents and their histories remain separately preserved in component_captures. Owners without refs retain absent refs and empty components.", "Any known urllib3 socket-construction capability probe is denied before action and retained explicitly; any other denial fails this attempt.", "Critical dependency and resource pins are pre/post checked. Additional actually loaded local modules and file reads are recorded, not claimed statically exhaustively reviewed.", "Raw primary-experiment labels, database references, protein identifiers and historical source claims remain attributed annotations; the complete maintained view does not add primary, sequence, producer, natural-identity or stereochemical verification.", "No molecular parsing, canonical gate, Git command, campaign read or record mutation is invoked."], "/resolved_view/biosynthetic_pathway": [{"enzyme_id": "UniProtKB:Q9X839", "enzyme_label": "Cyc2 germacradienol/germacrene D synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "notes": "The N-terminal domain of bifunctional Cyc2 cyclizes (2E,6E)-farnesyl diphosphate to germacradienol, the sesquiterpene alcohol intermediate in geosmin biosynthesis.", "product": "CHEBI:46734", "reaction_id": "RHEA:22436", "step_number": 1, "substrate": "CHEBI:175763"}, {"enzyme_id": "UniProtKB:Q9X839", "enzyme_label": "Cyc2 geosmin synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "notes": "The C-terminal domain of bifunctional Cyc2 converts germacradienol to (−)-geosmin.", "product": "CHEBI:46702", "reaction_id": "RHEA:30371", "step_number": 2, "substrate": "CHEBI:46734"}], "/resolved_view/causal_graphs": [{"description": "Partial Streptomyces coelicolor geosmin biosynthesis graph for bifunctional Cyc2 conversion of farnesyl diphosphate to (−)-geosmin through germacradienol.", "edges": [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "object": "cyc2", "predicate": "is cyclized by", "subject": "farnesyl_diphosphate"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}], "object": "germacradienol", "predicate": "forms", "subject": "cyc2"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "object": "cyc2", "predicate": "is converted by", "subject": "germacradienol"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved study showed that the N-terminal domain forms germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase mechanism"}], "object": "geosmin", "predicate": "forms", "subject": "cyc2"}], "graph_id": "geosmin-cyc2-biosynthesis", "nodes": [{"grounding_status": "GROUNDED", "identifier": "CHEBI:175763", "label": "(2E,6E)-farnesyl diphosphate", "node_id": "farnesyl_diphosphate", "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED", "identifier": "UniProtKB:Q9X839", "label": "Cyc2", "node_id": "cyc2", "node_type": "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46734", "label": "germacradienol", "node_id": "germacradienol", "node_type": "COMPOUND"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46702", "label": "(−)-geosmin", "node_id": "geosmin", "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"}], "/resolved_view/curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:08Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:02:26Z"}, {"action": "RECORD_CURATED", "changes": "Added a two-step BIOSYNTHESIS pathway and causal graph for geosmin biosynthesis; grounded the Streptomyces coelicolor bifunctional Cyc2 enzyme to UniProtKB:Q9X839 via SCO6073; and cited the experimentally characterized RHEA:22436 and RHEA:30371 reactions.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-26T22:48:26Z"}, {"action": "RECORD_CURATED", "changes": "Replaced the geosmin-forming Cyc2 step and edge evidence with the domain-resolved bifunctional geosmin synthase paper, DOI:10.1038/nchembio.2007.29.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-26T23:08:49Z"}], "/returned_view_equals_expected_complete_owner": true, "/status": "maintained_reader_returned_and_verified_offline", "/view_mismatches": []} |
| support-2328-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-current233-geosmin-maintained-reader-acceptance-001.json; /status; /accepted; /DATA; /execution; /original_tools; /verification; /review_check_contract | supports | ROOT acceptance of the original reader, including exact check contract and before-action blocked capability probe. Exact copied saved values: {"/DATA": {"bytes": 704621, "path": "/private/tmp/npm-review-work/shared-next-batch233/native-current233-geosmin-maintained-reader-DATA-001.json", "sha256": "2f540243dbd7e0cfcf24a9befdfce649170186c6b06358c76c5a75302a6e4e65"}, "/accepted": true, "/execution": {"bytes": 5573, "path": "/private/tmp/npm-review-work/shared-next-batch233/native-current233-geosmin-reader-execution-001.json", "sha256": "97d220ea18aadb2b35a7f43a6e95f3d5a3fa38e2b6885e3e6113a0bae2d364da"}, "/original_tools": {"bytes": 1233, "path": "/private/tmp/npm-review-work/shared-next-batch233/native-current233-geosmin-reader-original-tools-001.json", "sha256": "30a284a3b0e9b9371459e442a4caf0afd6dc2e81a2e8562ffd5f3d94e0b1a4c5"}, "/review_check_contract": {"command": "/private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch233/read-selected-mechanism-guarded-001.py 2328 fd189cfeef53223564efc2e151e9ab13c9d4ff0eedbf2e9be9a97d35e2761db9 fee38fccf50dd95c8d1e025f3d6694a2bb81946e63438ab5f53f7e1bc7ed7152 c6a354765f2590d29898156c1d68bac79ab532abcad168d75c278a0a0e3df077 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927 c40437dc157b29c3b4bf647a7e232564fff639b957c0ac7b3a604fc9c490d85a", "exit_code": 0, "exit_source": "original tool terminal and process receipt", "name": "Complete offline maintained reader for geosmin", "required": true, "status": "passed", "target_order": 2328}, "/status": "accepted_original_offline_maintained_reader", "/verification": {"complete_owner_equality": true, "counts": {"component_graphs": 0, "component_history_events": [], "component_refs": 0, "curation_history": 4, "edges": 4, "graphs": 1, "inline_graphs": 1, "molecular_targets": 0, "nodes": 4, "pathway_steps": 2}, "current_paths": 1017, "current_pin_placements": 1944, "empty_stderr": true, "expected_before_action_denials": 1, "launch_environment_unchanged": true, "observed_runtime_only_environment": {"__CF_USER_TEXT_ENCODING": "0x1F5:0x0:0x0"}, "original_exit_code": 0, "positive_content_exact": true, "unexpected_denials": 0}} |
| support-2328-reader-execution | /private/tmp/npm-review-work/shared-next-batch233/native-current233-geosmin-reader-execution-001.json; Whole original execution receipt | supports | Native operated the one Geosmin maintained reader, original c0129f/session52080 to f62a02/exit0, with empty stderr and no retry. ROOT separately accepted it. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-233/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-233/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-233/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-233/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-233/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. No external publication, identifier, taxonomy, protein sequence or natural stereochemical assertion was refreshed under the absolute no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original gates, stored-form parsing and maintained-reader preservation establish only their stated scope.
- Exact empty joins are bounded by saved predicates/snapshots; shared loci, names, taxa or citations do not transfer identity, production, activity or mechanism.
- Two original omitted-undefined-stereo warnings remain global and unassigned. No additional molecular/YAML parse, source query or target invocation occurred during scientific authoring.
- No source record or native status/history is edited. Any correction belongs to the maintained owners admitted in the actual intake.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read all five complete raw owners/history, actual canonical intakes and its disjoint retained source partition; exact prior companion carries and BGC complementary readings remain explicitly attributed in the joint notes.
- Support personally read all ten saved forms: 292 atom and 320 bond rows, every scalar/ring/stereo/motif/map; terminals 75f742,41ef45,19e485,5b59bb. No alternate computation is substituted.
- ROOT operated activation/capture, inventory/composer, canonical intakes and molecular diagnostic. Native operated original local gates and maintained readers under ROOT authorization; ROOT separately accepted results. Scientific authoring invoked none of those targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T021206Z-geosmin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: (−)-geosmin'
started_at: '2026-11-04T01:29:01.338323Z'
finished_at: '2026-11-04T02:12:06.205399Z'
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
summary: (−)-Geosmin retains its exact local ChEBI grounding, consistent fully specified
  stored structure and a preserved partial two-domain Cyc2 mechanism. Historical experiment
  and protein claims remain qualified; scientific completion is partial.
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
  - path: data/natural_products/terpenoids/geosmin.yaml
    sha256: c026509c83990c5cda6a01008a0346bc2997fdc5b6d2fde3ba2ac5522a8f429a
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
  selection: Campaign path order 2328; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:46702
targets:
- target_id: CHEBI:46702
  path: data/natural_products/terpenoids/geosmin.yaml
  label: (−)-geosmin
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
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/terpenoids/geosmin.yaml
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
- name: Complete offline maintained reader for geosmin
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch233/read-selected-mechanism-guarded-001.py
    2328 fd189cfeef53223564efc2e151e9ab13c9d4ff0eedbf2e9be9a97d35e2761db9 fee38fccf50dd95c8d1e025f3d6694a2bb81946e63438ab5f53f7e1bc7ed7152
    c6a354765f2590d29898156c1d68bac79ab532abcad168d75c278a0a0e3df077 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
    c40437dc157b29c3b4bf647a7e232564fff639b957c0ac7b3a604fc9c490d85a
  exit_code: 0
  status: passed
  required: true
  check_id: maintained-mechanism-reader
  summary: One original offline maintained call preserves the complete Geosmin owner,
    one graph/four nodes/four edges, two pathway entries and four history events;
    historical science remains independently qualified.
  target_ids:
  - CHEBI:46702
  evidence_ids:
  - support-2328-mechanism-owner
  - support-2328-reader
  - support-2328-reader-acceptance
  - support-2328-reader-execution
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:46702
  command: just validate-strict data/natural_products/terpenoids/ent-quiannulatene.yaml
    data/natural_products/terpenoids/enterocin.yaml data/natural_products/terpenoids/eremophilene.yaml
    data/natural_products/terpenoids/euphol.yaml data/natural_products/terpenoids/eutypinic-acid.yaml
    data/natural_products/terpenoids/fumihopaside-a.yaml data/natural_products/terpenoids/fusarochromanone.yaml
    data/natural_products/terpenoids/geosmin.yaml data/natural_products/terpenoids/gibberellin.yaml
    data/natural_products/terpenoids/helvolic-acid.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-233/validate-strict-selected10-001.tsv
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
  - CHEBI:46702
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-233/validate-all-001.tsv
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
  - CHEBI:46702
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
  - CHEBI:46702
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
  - CHEBI:46702
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-233/review-queue-001.tsv
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
  - CHEBI:46702
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:46702
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:46702
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2328-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/geosmin.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Complete owner and all 4 history entries are covered by current exact whole-reading
    attribution. Native curation_status remains SEEDED.
  snapshot_sha256: c026509c83990c5cda6a01008a0346bc2997fdc5b6d2fde3ba2ac5522a8f429a
- evidence_id: support-2328-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/7
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete original captured owner and exact literal mechanism/component
    presence, distinct from maintained resolution. Exact copied saved values: {"/records/7":
    {"component_captures": [], "mechanism_capture_scope": "raw_owner_and_declared_components_only_not_maintained_resolution",
    "order": 2328, "owner_document": {"bgc_class": ["TERPENE"], "biosynthesis_origin":
    "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001181",
    "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "4", "evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001181 entry version
    4; citation taken from the compound bioactivity level", "reference": "DOI:10.1038/s41564-020-0697-x"}],
    "genome_accession": "genbank:AL645882.2", "link_evidence_basis": "CLUSTER_UNSTATED",
    "locus_from": 6666219, "locus_to": 6668399, "organism_label": "Streptomyces coelicolor
    A3(2)", "organism_taxon_id": "NCBITaxon:100226"}], "biosynthetic_pathway": [{"enzyme_id":
    "UniProtKB:Q9X839", "enzyme_label": "Cyc2 germacradienol/germacrene D synthase",
    "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "notes": "The N-terminal domain of bifunctional Cyc2 cyclizes (2E,6E)-farnesyl
    diphosphate to germacradienol, the sesquiterpene alcohol intermediate in geosmin
    biosynthesis.", "product": "CHEBI:46734", "reaction_id": "RHEA:22436", "step_number":
    1, "substrate": "CHEBI:175763"}, {"enzyme_id": "UniProtKB:Q9X839", "enzyme_label":
    "Cyc2 geosmin synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT",
    "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073
    gene product; the domain-resolved study showed that the N-terminal domain forms
    germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin
    reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional
    geosmin synthase mechanism"}], "notes": "The C-terminal domain of bifunctional
    Cyc2 converts germacradienol to (−)-geosmin.", "product": "CHEBI:46702", "reaction_id":
    "RHEA:30371", "step_number": 2, "substrate": "CHEBI:46734"}], "causal_graphs":
    [{"description": "Partial Streptomyces coelicolor geosmin biosynthesis graph for
    bifunctional Cyc2 conversion of farnesyl diphosphate to (−)-geosmin through germacradienol.",
    "edges": [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "object": "cyc2", "predicate": "is cyclized by", "subject": "farnesyl_diphosphate"},
    {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "object": "germacradienol", "predicate": "forms", "subject": "cyc2"}, {"evidence":
    [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to
    the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved
    study showed that the N-terminal domain forms germacradienol and that the C-terminal
    domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference":
    "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase
    mechanism"}], "object": "cyc2", "predicate": "is converted by", "subject": "germacradienol"},
    {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved
    study showed that the N-terminal domain forms germacradienol and that the C-terminal
    domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference":
    "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase
    mechanism"}], "object": "geosmin", "predicate": "forms", "subject": "cyc2"}],
    "graph_id": "geosmin-cyc2-biosynthesis", "nodes": [{"grounding_status": "GROUNDED",
    "identifier": "CHEBI:175763", "label": "(2E,6E)-farnesyl diphosphate", "node_id":
    "farnesyl_diphosphate", "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED",
    "identifier": "UniProtKB:Q9X839", "label": "Cyc2", "node_id": "cyc2", "node_type":
    "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46734", "label":
    "germacradienol", "node_id": "germacradienol", "node_type": "COMPOUND"}, {"grounding_status":
    "GROUNDED", "identifier": "CHEBI:46702", "label": "(−)-geosmin", "node_id": "geosmin",
    "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"}], "chemical_structure": {"smiles":
    "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1",
    "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001181"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:08Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:02:26Z"},
    {"action": "RECORD_CURATED", "changes": "Added a two-step BIOSYNTHESIS pathway
    and causal graph for geosmin biosynthesis; grounded the Streptomyces coelicolor
    bifunctional Cyc2 enzyme to UniProtKB:Q9X839 via SCO6073; and cited the experimentally
    characterized RHEA:22436 and RHEA:30371 reactions.", "curator": "codex", "llm_assisted":
    true, "timestamp": "2026-09-26T22:48:26Z"}, {"action": "RECORD_CURATED", "changes":
    "Replaced the geosmin-forming Cyc2 step and edge evidence with the domain-resolved
    bifunctional geosmin synthase paper, DOI:10.1038/nchembio.2007.29.", "curator":
    "codex", "llm_assisted": true, "timestamp": "2026-09-26T23:08:49Z"}], "curation_status":
    "SEEDED", "definition": "The (−)-stereoisomer of geosmin, having 4S,4aS,8aR configuration.",
    "definition_source": "CHEBI:46702", "grounding_status": "EXACT", "identifier":
    "CHEBI:46702", "label": "(−)-geosmin", "np_classification": {"class_results":
    ["Eudesmane sesquiterpenoids", "Noreudesmane sesquiterpenoids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Sesquiterpenoids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["ACTINOBACTERIAL", "CYANOBACTERIAL",
    "FUNGAL", "LAND_PLANT"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/S002170100305"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q47685",
    "source": "LOTUS", "taxon_id": "NCBITaxon:13443", "taxon_label": "Coffea arabica",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q84325870", "source": "LOTUS", "taxon_id": "NCBITaxon:1586124",
    "taxon_label": "Cortinarius herculeus", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q84325870", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1586124", "taxon_label": "Cortinarius herculeus",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1021/JF60204A059"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q165191",
    "source": "LOTUS", "taxon_id": "NCBITaxon:161934", "taxon_label": "Beta vulgaris",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/BF00416598"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q39087436",
    "source": "LOTUS", "taxon_id": "NCBITaxon:177969", "taxon_label": "Oscillatoria
    brevis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q470766", "source": "LOTUS", "taxon_id": "NCBITaxon:182063",
    "taxon_label": "Cystoderma amianthinum", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q470766", "source":
    "LOTUS", "taxon_id": "NCBITaxon:182063", "taxon_label": "Cystoderma amianthinum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1016/J.YMBEN.2018.09.004"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q1144013", "source": "LOTUS", "taxon_id": "NCBITaxon:1883",
    "taxon_label": "Streptomyces", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS",
    "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source":
    "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces
    albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1021/JA062669X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces
    albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces
    albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886",
    "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.47.434"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces
    coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902",
    "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1021/JA062669X"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces
    coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902",
    "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1111/J.1365-2672.1992.TB01818.X"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q7623385", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1911", "taxon_label": "Streptomyces griseus",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1021/JF00013A023"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292941",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1932", "taxon_label": "Streptomyces
    tendae", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1128/AEM.57.12.3429-3432.1991"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q26292941", "source": "LOTUS", "taxon_id": "NCBITaxon:1932",
    "taxon_label": "Streptomyces tendae", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1038/SJ.JIM.7000121"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q22665882", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1944", "taxon_label": "Streptomyces halstedii",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/BF02932133"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562",
    "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces
    avermitilis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/JA.2006.66"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562
    16 further cited occurrences are recorded in data/raw/lotus_occurrences.tsv and
    data/raw/chebi_origins.tsv but not written here: a record carrying hundreds of
    them cannot be reviewed. The inventories are the complete record.", "source":
    "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces avermitilis",
    "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster":
    "mibig:BGC0001181", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0001181 entry version 4; citation taken from the compound bioactivity
    level", "reference": "DOI:10.1038/s41564-020-0697-x"}], "evidence_basis": "SOURCE_ASSERTION",
    "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED;
    this field grades the taxon claim, which is a different question.", "source":
    "MIBIG", "source_version": "4", "taxon_id": "NCBITaxon:100226", "taxon_label":
    "Streptomyces coelicolor A3(2)"}], "producer_taxon_groups": ["ACTINOBACTERIAL"],
    "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-0349656c0d",
    "source": "MIBIG", "source_id": "BGC0001181", "source_label": "geosmin", "source_version":
    "4"}, {"minted_identifier": "naturalproductmech:chebi-cea96d6d0a", "source": "CHEBI",
    "source_id": "CHEBI:46702", "source_label": "(−)-geosmin", "source_version": "3-star"}],
    "synonyms": [{"source": "mibig:BGC0001181", "synonym_type": "RELATED_SYNONYM",
    "value": "geosmin"}]}, "owner_pin": {"bytes": 19003, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/geosmin.yaml",
    "sha256": "c026509c83990c5cda6a01008a0346bc2997fdc5b6d2fde3ba2ac5522a8f429a"},
    "path": "data/natural_products/terpenoids/geosmin.yaml", "read_finished_at": "2026-11-04T01:29:01.346830Z",
    "read_started_at": "2026-11-04T01:29:01.338323Z"}}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2328-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/7/owner_document/identifier; /records/7/owner_document/label;
    /records/7/owner_document/chemical_structure; /records/7/owner_document/definition;
    /records/7/owner_document/definition_source; /records/7/owner_document/synonyms;
    /records/7/owner_document/grounding_status; /records/7/owner_document/source_concepts
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Exact identity, source definition and grounding fields, including retained
    unresolved discussion where present. Exact copied saved values: {"/records/7/owner_document/chemical_structure":
    {"smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1",
    "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001181"}, "/records/7/owner_document/definition":
    "The (−)-stereoisomer of geosmin, having 4S,4aS,8aR configuration.", "/records/7/owner_document/definition_source":
    "CHEBI:46702", "/records/7/owner_document/grounding_status": "EXACT", "/records/7/owner_document/identifier":
    "CHEBI:46702", "/records/7/owner_document/label": "(−)-geosmin", "/records/7/owner_document/source_concepts":
    [{"minted_identifier": "naturalproductmech:mibig-0349656c0d", "source": "MIBIG",
    "source_id": "BGC0001181", "source_label": "geosmin", "source_version": "4"},
    {"minted_identifier": "naturalproductmech:chebi-cea96d6d0a", "source": "CHEBI",
    "source_id": "CHEBI:46702", "source_label": "(−)-geosmin", "source_version": "3-star"}],
    "/records/7/owner_document/synonyms": [{"source": "mibig:BGC0001181", "synonym_type":
    "RELATED_SYNONYM", "value": "geosmin"}]}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2328-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters;
    /records/7/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Separately graded producer and locus source assertions. Exact copied saved
    values: {"/records/7/owner_document/biosynthetic_gene_clusters": [{"accession":
    "mibig:BGC0001181", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version":
    "4", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001181
    entry version 4; citation taken from the compound bioactivity level", "reference":
    "DOI:10.1038/s41564-020-0697-x"}], "genome_accession": "genbank:AL645882.2", "link_evidence_basis":
    "CLUSTER_UNSTATED", "locus_from": 6666219, "locus_to": 6668399, "organism_label":
    "Streptomyces coelicolor A3(2)", "organism_taxon_id": "NCBITaxon:100226"}], "/records/7/owner_document/producer_organisms":
    [{"biosynthetic_gene_cluster": "mibig:BGC0001181", "evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "MIBiG BGC0001181 entry version 4; citation taken
    from the compound bioactivity level", "reference": "DOI:10.1038/s41564-020-0697-x"}],
    "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That
    evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim,
    which is a different question.", "source": "MIBIG", "source_version": "4", "taxon_id":
    "NCBITaxon:100226", "taxon_label": "Streptomyces coelicolor A3(2)"}], "/records/7/owner_document/producer_taxon_groups":
    ["ACTINOBACTERIAL"]}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2328-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/7/owner_document/occurrences; /records/7/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Written occurrence placements and retained further-row notes. Exact copied
    saved values: {"/records/7/owner_document/occurrence_taxon_groups": ["ACTINOBACTERIAL",
    "CYANOBACTERIAL", "FUNGAL", "LAND_PLANT"], "/records/7/owner_document/occurrences":
    [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1007/S002170100305"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q47685", "source":
    "LOTUS", "taxon_id": "NCBITaxon:13443", "taxon_label": "Coffea arabica", "taxon_source":
    "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q84325870",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1586124", "taxon_label": "Cortinarius
    herculeus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.2307/3761199"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q84325870",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1586124", "taxon_label": "Cortinarius
    herculeus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1021/JF60204A059"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q165191",
    "source": "LOTUS", "taxon_id": "NCBITaxon:161934", "taxon_label": "Beta vulgaris",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/BF00416598"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q39087436",
    "source": "LOTUS", "taxon_id": "NCBITaxon:177969", "taxon_label": "Oscillatoria
    brevis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q470766", "source": "LOTUS", "taxon_id": "NCBITaxon:182063",
    "taxon_label": "Cystoderma amianthinum", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q470766", "source":
    "LOTUS", "taxon_id": "NCBITaxon:182063", "taxon_label": "Cystoderma amianthinum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1016/J.YMBEN.2018.09.004"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q1144013", "source": "LOTUS", "taxon_id": "NCBITaxon:1883",
    "taxon_label": "Streptomyces", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS",
    "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source":
    "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces
    albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1021/JA062669X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces
    albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces
    albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886",
    "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.47.434"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces
    coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902",
    "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1021/JA062669X"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces
    coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902",
    "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1111/J.1365-2672.1992.TB01818.X"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q7623385", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1911", "taxon_label": "Streptomyces griseus",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1021/JF00013A023"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292941",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1932", "taxon_label": "Streptomyces
    tendae", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1128/AEM.57.12.3429-3432.1991"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q26292941", "source": "LOTUS", "taxon_id": "NCBITaxon:1932",
    "taxon_label": "Streptomyces tendae", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1038/SJ.JIM.7000121"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q22665882", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1944", "taxon_label": "Streptomyces halstedii",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/BF02932133"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562",
    "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces
    avermitilis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/JA.2006.66"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562
    16 further cited occurrences are recorded in data/raw/lotus_occurrences.tsv and
    data/raw/chebi_origins.tsv but not written here: a record carrying hundreds of
    them cannot be reviewed. The inventories are the complete record.", "source":
    "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces avermitilis",
    "taxon_source": "NCBITaxon"}]}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2328-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Written observations and coarse activity summary; whole owner selector
    proves absent optional roots without a global absence claim. Exact copied saved
    values: {"/records/7/owner_document": {"bgc_class": ["TERPENE"], "biosynthesis_origin":
    "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001181",
    "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "4", "evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001181 entry version
    4; citation taken from the compound bioactivity level", "reference": "DOI:10.1038/s41564-020-0697-x"}],
    "genome_accession": "genbank:AL645882.2", "link_evidence_basis": "CLUSTER_UNSTATED",
    "locus_from": 6666219, "locus_to": 6668399, "organism_label": "Streptomyces coelicolor
    A3(2)", "organism_taxon_id": "NCBITaxon:100226"}], "biosynthetic_pathway": [{"enzyme_id":
    "UniProtKB:Q9X839", "enzyme_label": "Cyc2 germacradienol/germacrene D synthase",
    "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "notes": "The N-terminal domain of bifunctional Cyc2 cyclizes (2E,6E)-farnesyl
    diphosphate to germacradienol, the sesquiterpene alcohol intermediate in geosmin
    biosynthesis.", "product": "CHEBI:46734", "reaction_id": "RHEA:22436", "step_number":
    1, "substrate": "CHEBI:175763"}, {"enzyme_id": "UniProtKB:Q9X839", "enzyme_label":
    "Cyc2 geosmin synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT",
    "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073
    gene product; the domain-resolved study showed that the N-terminal domain forms
    germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin
    reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional
    geosmin synthase mechanism"}], "notes": "The C-terminal domain of bifunctional
    Cyc2 converts germacradienol to (−)-geosmin.", "product": "CHEBI:46702", "reaction_id":
    "RHEA:30371", "step_number": 2, "substrate": "CHEBI:46734"}], "causal_graphs":
    [{"description": "Partial Streptomyces coelicolor geosmin biosynthesis graph for
    bifunctional Cyc2 conversion of farnesyl diphosphate to (−)-geosmin through germacradienol.",
    "edges": [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "object": "cyc2", "predicate": "is cyclized by", "subject": "farnesyl_diphosphate"},
    {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "object": "germacradienol", "predicate": "forms", "subject": "cyc2"}, {"evidence":
    [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to
    the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved
    study showed that the N-terminal domain forms germacradienol and that the C-terminal
    domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference":
    "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase
    mechanism"}], "object": "cyc2", "predicate": "is converted by", "subject": "germacradienol"},
    {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved
    study showed that the N-terminal domain forms germacradienol and that the C-terminal
    domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference":
    "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase
    mechanism"}], "object": "geosmin", "predicate": "forms", "subject": "cyc2"}],
    "graph_id": "geosmin-cyc2-biosynthesis", "nodes": [{"grounding_status": "GROUNDED",
    "identifier": "CHEBI:175763", "label": "(2E,6E)-farnesyl diphosphate", "node_id":
    "farnesyl_diphosphate", "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED",
    "identifier": "UniProtKB:Q9X839", "label": "Cyc2", "node_id": "cyc2", "node_type":
    "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46734", "label":
    "germacradienol", "node_id": "germacradienol", "node_type": "COMPOUND"}, {"grounding_status":
    "GROUNDED", "identifier": "CHEBI:46702", "label": "(−)-geosmin", "node_id": "geosmin",
    "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"}], "chemical_structure": {"smiles":
    "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1",
    "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001181"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:08Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:02:26Z"},
    {"action": "RECORD_CURATED", "changes": "Added a two-step BIOSYNTHESIS pathway
    and causal graph for geosmin biosynthesis; grounded the Streptomyces coelicolor
    bifunctional Cyc2 enzyme to UniProtKB:Q9X839 via SCO6073; and cited the experimentally
    characterized RHEA:22436 and RHEA:30371 reactions.", "curator": "codex", "llm_assisted":
    true, "timestamp": "2026-09-26T22:48:26Z"}, {"action": "RECORD_CURATED", "changes":
    "Replaced the geosmin-forming Cyc2 step and edge evidence with the domain-resolved
    bifunctional geosmin synthase paper, DOI:10.1038/nchembio.2007.29.", "curator":
    "codex", "llm_assisted": true, "timestamp": "2026-09-26T23:08:49Z"}], "curation_status":
    "SEEDED", "definition": "The (−)-stereoisomer of geosmin, having 4S,4aS,8aR configuration.",
    "definition_source": "CHEBI:46702", "grounding_status": "EXACT", "identifier":
    "CHEBI:46702", "label": "(−)-geosmin", "np_classification": {"class_results":
    ["Eudesmane sesquiterpenoids", "Noreudesmane sesquiterpenoids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Sesquiterpenoids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["ACTINOBACTERIAL", "CYANOBACTERIAL",
    "FUNGAL", "LAND_PLANT"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/S002170100305"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q47685",
    "source": "LOTUS", "taxon_id": "NCBITaxon:13443", "taxon_label": "Coffea arabica",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q84325870", "source": "LOTUS", "taxon_id": "NCBITaxon:1586124",
    "taxon_label": "Cortinarius herculeus", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q84325870", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1586124", "taxon_label": "Cortinarius herculeus",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1021/JF60204A059"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q165191",
    "source": "LOTUS", "taxon_id": "NCBITaxon:161934", "taxon_label": "Beta vulgaris",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/BF00416598"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q39087436",
    "source": "LOTUS", "taxon_id": "NCBITaxon:177969", "taxon_label": "Oscillatoria
    brevis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1080/00275514.1999.12060999"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q470766", "source": "LOTUS", "taxon_id": "NCBITaxon:182063",
    "taxon_label": "Cystoderma amianthinum", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.2307/3761199"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q470766", "source":
    "LOTUS", "taxon_id": "NCBITaxon:182063", "taxon_label": "Cystoderma amianthinum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1016/J.YMBEN.2018.09.004"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q1144013", "source": "LOTUS", "taxon_id": "NCBITaxon:1883",
    "taxon_label": "Streptomyces", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source": "LOTUS",
    "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "taxon_source":
    "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces
    albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1021/JA062669X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces
    albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces
    albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q22286833", "source": "LOTUS", "taxon_id": "NCBITaxon:1886",
    "taxon_label": "Streptomyces albidoflavus", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.47.434"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q22286833", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/S10295-013-1383-2"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces
    coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1016/B978-0-12-404634-4.00014-0"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902",
    "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1021/JA062669X"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/NCHEMBIO.2007.29"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q2355919",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces
    coelicolor", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1371/JOURNAL.PONE.0060665"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q2355919", "source": "LOTUS", "taxon_id": "NCBITaxon:1902",
    "taxon_label": "Streptomyces coelicolor", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1111/J.1365-2672.1992.TB01818.X"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q7623385", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1911", "taxon_label": "Streptomyces griseus",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1021/JF00013A023"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292941",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1932", "taxon_label": "Streptomyces
    tendae", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1128/AEM.57.12.3429-3432.1991"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q26292941", "source": "LOTUS", "taxon_id": "NCBITaxon:1932",
    "taxon_label": "Streptomyces tendae", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1038/SJ.JIM.7000121"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q22665882", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1944", "taxon_label": "Streptomyces halstedii",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1007/BF02932133"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562",
    "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces
    avermitilis", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/JA.2006.66"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562
    16 further cited occurrences are recorded in data/raw/lotus_occurrences.tsv and
    data/raw/chebi_origins.tsv but not written here: a record carrying hundreds of
    them cannot be reviewed. The inventories are the complete record.", "source":
    "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces avermitilis",
    "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster":
    "mibig:BGC0001181", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0001181 entry version 4; citation taken from the compound bioactivity
    level", "reference": "DOI:10.1038/s41564-020-0697-x"}], "evidence_basis": "SOURCE_ASSERTION",
    "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED;
    this field grades the taxon claim, which is a different question.", "source":
    "MIBIG", "source_version": "4", "taxon_id": "NCBITaxon:100226", "taxon_label":
    "Streptomyces coelicolor A3(2)"}], "producer_taxon_groups": ["ACTINOBACTERIAL"],
    "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-0349656c0d",
    "source": "MIBIG", "source_id": "BGC0001181", "source_label": "geosmin", "source_version":
    "4"}, {"minted_identifier": "naturalproductmech:chebi-cea96d6d0a", "source": "CHEBI",
    "source_id": "CHEBI:46702", "source_label": "(−)-geosmin", "source_version": "3-star"}],
    "synonyms": [{"source": "mibig:BGC0001181", "synonym_type": "RELATED_SYNONYM",
    "value": "geosmin"}]}}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2328-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification;
    /records/7/owner_document/bgc_class
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Versioned computed filing and separately asserted BGC/compound classes.
    Exact copied saved values: {"/records/7/owner_document/bgc_class": ["TERPENE"],
    "/records/7/owner_document/np_classification": {"class_results": ["Eudesmane sesquiterpenoids",
    "Noreudesmane sesquiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"],
    "superclass_results": ["Sesquiterpenoids"], "tool": "NPClassifier", "tool_version":
    "npclassifier.gnps2.org@2026-09-07"}, "/records/7/owner_document/np_pathway":
    "TERPENOIDS"}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2328-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/comparisons; /records/7/atom_correspondence
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete original declared forms/comparisons/map, unchanged. Exact copied
    saved values: {"/records/7/atom_correspondence": {"complete_atom_count_match":
    true, "full_graph_identity_established": false, "scope": "One chirality-aware
    substructure match; no independent full graph or natural identity claim.", "smiles_to_inchi_atom_indices":
    [0, 9, 5, 4, 7, 10, 11, 8, 3, 2, 6, 12, 1]}, "/records/7/comparisons": {"atom_count_equal":
    true, "bond_count_equal": true, "both_keys_equal_declared": true, "canonical_isomeric_smiles_equal":
    true, "canonical_nonisomeric_smiles_equal": true, "formal_charge_equal": true,
    "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer": true,
    "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "/records/7/declared_structure":
    {"smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1",
    "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001181"}}'
  snapshot_sha256: 98d9bae4e307da83403d9b3e783897999469aca3e863fd37b097f1688bf1d4ee
- evidence_id: support-2328-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed; /records/7/inchi/computed; /records/7/declared_structure;
    /records/7/comparisons; /records/7/atom_correspondence
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Both forms are neutral C12H22O with 13 atoms and 14 bonds. Two saturated
    six-membered carbocycles share one edge, with two methyl substituents and a tertiary
    bridgehead alcohol. Three tetrahedral centers are specified; no carbonyl or sugar-ring
    motif is present. All ten comparisons are true and the original atom correspondence
    is complete, while full_graph_identity_established remains false. Different local
    chiral tag orderings do not contradict the identical canonical stereochemical
    representation; neither local parsing nor the full key proves natural optical
    rotation or sample purity.
  snapshot_sha256: 98d9bae4e307da83403d9b3e783897999469aca3e863fd37b097f1688bf1d4ee
- evidence_id: support-2328-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/intakes/2328-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Actual canonical intake, all admitted input roles and maintained correction
    ownership. Exact copied saved values: {"/repository": "CultureBotAI/NaturalProductMech",
    "/source": {"git_revision": "ce6a5498df5be51116bd5e0c119023ee62bb5464", "inputs":
    [{"path": ".claude/skills/curate-yaml-record/references/review-checklist.md",
    "role": "context", "sha256": "13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9"},
    {"path": ".claude/skills/review-yaml-record/SKILL.md", "role": "context", "sha256":
    "493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae"}, {"path":
    "AGENTS.md", "role": "context", "sha256": "69e4037f8dc97d4b00bb7bb83b41ceca025f6ef578d5c0bf8086f3400becde0b"},
    {"path": "conf/id_label_targets.yaml", "role": "context", "sha256": "24235903e0e8df5793a30e92c551082c71c1c67739ea4e3b5fb0f68853a805e6"},
    {"path": "conf/producer_evidence.tsv", "role": "context", "sha256": "67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131"},
    {"path": "conf/record_review.yaml", "role": "context", "sha256": "e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8"},
    {"path": "curation/lotus_occurrence_exclusions.tsv", "role": "context", "sha256":
    "d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d"}, {"path":
    "curation/mibig_claim_references.tsv", "role": "context", "sha256": "bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029"},
    {"path": "curation/mibig_locus_evidence_overrides.tsv", "role": "context", "sha256":
    "7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e"}, {"path":
    "curation/mibig_producer_isolates.tsv", "role": "context", "sha256": "8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8"},
    {"path": "curation/mibig_producer_strains.tsv", "role": "context", "sha256": "bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae"},
    {"path": "curation/mibig_structure_corrections.tsv", "role": "context", "sha256":
    "c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0"}, {"path":
    "curation/mibig_xref_exclusions.tsv", "role": "context", "sha256": "cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c"},
    {"path": "data/natural_products/PATHS.tsv", "role": "context", "sha256": "2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3"},
    {"path": "data/natural_products/terpenoids/geosmin.yaml", "role": "target", "sha256":
    "c026509c83990c5cda6a01008a0346bc2997fdc5b6d2fde3ba2ac5522a8f429a"}, {"path":
    "data/raw/MANIFEST.yaml", "role": "context", "sha256": "b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3"},
    {"path": "data/raw/antibioticmech_inchikeys.tsv", "role": "context", "sha256":
    "ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6"}, {"path":
    "data/raw/bindingdb_targets.tsv", "role": "context", "sha256": "3cff45281c35a8b14d4d7784bc4b7af80e8e27779a5667a0292f0d9b022a22c1"},
    {"path": "data/raw/chebi_origins.tsv", "role": "context", "sha256": "fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8"},
    {"path": "data/raw/chebi_structures.tsv", "role": "context", "sha256": "62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2"},
    {"path": "data/raw/corpus_taxa.obo", "role": "context", "sha256": "8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9"},
    {"path": "data/raw/cyanometdb_occurrences.tsv", "role": "context", "sha256": "f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8"},
    {"path": "data/raw/lotus_occurrences.tsv", "role": "context", "sha256": "ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94"},
    {"path": "data/raw/mibig_compounds.tsv", "role": "context", "sha256": "e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6"},
    {"path": "data/raw/npclassifier.tsv", "role": "context", "sha256": "acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3"},
    {"path": "data/raw/pubchem_bioassay.tsv", "role": "context", "sha256": "6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b"},
    {"path": "docs/CURATION.md", "role": "context", "sha256": "c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa"},
    {"path": "docs/HARMONIZATION.md", "role": "context", "sha256": "c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79"},
    {"path": "docs/record-review-profile.md", "role": "context", "sha256": "1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a"},
    {"path": "docs/record-reviews.md", "role": "context", "sha256": "452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b"},
    {"path": "justfile", "role": "context", "sha256": "4f9057e3e54656dd46f2ded4d3a8f0804acad348d2605d436405e1fcfb6af550"},
    {"path": "schema/record_review.yaml", "role": "context", "sha256": "229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb"},
    {"path": "scripts/extract_chebi.py", "role": "context", "sha256": "46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f"},
    {"path": "scripts/extract_mibig.py", "role": "context", "sha256": "e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c"},
    {"path": "scripts/seed_from_sources.py", "role": "context", "sha256": "5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5"},
    {"path": "src/naturalproductmech/curate/claim_references.py", "role": "context",
    "sha256": "0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3"},
    {"path": "src/naturalproductmech/graph_components.py", "role": "context", "sha256":
    "10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17"}, {"path":
    "src/naturalproductmech/schema/naturalproductmech.yaml", "role": "context", "sha256":
    "9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d"}, {"path":
    "src/naturalproductmech/validation/write_validated.py", "role": "context", "sha256":
    "4b7648fc5d2e7a5d26ad8bb168dbcae609aaa2694434a8ed5cfcb33fb66ff80a"}], "state":
    "working_tree"}, "/status": "inspection_only", "/targets": [{"kind": "generated",
    "label": "(−)-geosmin", "owner_paths": [{"path": "scripts/seed_from_sources.py",
    "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained harmonization
    generator; seeded fields are corrected through maintained inputs and validated
    regeneration."}, {"path": "data/raw/mibig_compounds.tsv", "repository": "CultureBotAI/NaturalProductMech",
    "role": "Retained MIBiG structure, producer and compound-specific locus assertions."},
    {"path": "data/raw/npclassifier.tsv", "repository": "CultureBotAI/NaturalProductMech",
    "role": "Pinned computed classification and filing assertions."}, {"path": "scripts/extract_mibig.py",
    "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained extraction
    of MIBiG compound names, structures, stereochemistry flags and source provenance."},
    {"path": "data/raw/chebi_structures.tsv", "repository": "CultureBotAI/NaturalProductMech",
    "role": "Retained ChEBI identifiers, definitions and exact chemical forms."},
    {"path": "data/raw/lotus_occurrences.tsv", "repository": "CultureBotAI/NaturalProductMech",
    "role": "Retained cited occurrence assertions, distinct from demonstrated production."},
    {"path": "src/naturalproductmech/graph_components.py", "repository": "CultureBotAI/NaturalProductMech",
    "role": "Future maintained complete-owner reader implementation; not invoked in
    this plan."}, {"path": "src/naturalproductmech/validation/write_validated.py",
    "repository": "CultureBotAI/NaturalProductMech", "role": "Future maintained complete-owner
    reader implementation; not invoked in this plan."}, {"path": "data/natural_products/terpenoids/geosmin.yaml",
    "repository": "CultureBotAI/NaturalProductMech", "role": "Curator-owned declared
    graphs, graph references, pathway steps and history; imported molecular-target
    assertions and other seeded fields retain inventory ownership. Curated graph/pathway
    changes require the validated writer and a curation event."}], "ownership_note":
    "This review proposes no record edit. Source corrections belong in maintained
    inventories, implemented curation tables, extractors or the seeder; generated
    pages are not owners. This mechanism-bearing owner requires separately authorized
    complete maintained resolution before scientific assessment and draft assembly.
    Raw owner capture is not a maintained resolved view.", "path": "data/natural_products/terpenoids/geosmin.yaml",
    "record_class": "NaturalProductRecord", "target_id": "CHEBI:46702"}]}'
  snapshot_sha256: fee38fccf50dd95c8d1e025f3d6694a2bb81946e63438ab5f53f7e1bc7ed7152
- evidence_id: support-2328-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-intake-acceptance-001.json
  locator: /status; /accepted; /source_placements; /unique_source_paths
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: ROOT accepts all ten original canonical intakes, with 396 source placements
    and 68 distinct paths.
  snapshot_sha256: 3124e401a141d5fee52e3838ae8258cf2fc2b9c791050dfa2b6afd6ad1b308dd
- evidence_id: support-2328-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-source-inventory-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: ROOT accepts the original local inventory; source meanings are separately
    attributed.
  snapshot_sha256: 8e3a8821fa52e78220f01f692579f368a6adb58d85d3624d16eeb7fa4c86b5e1
- evidence_id: support-2328-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-input-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: ROOT accepts the original input plan, not a scientific verdict.
  snapshot_sha256: 4d76cf85f5594ce1d2b1990f9a8a3a1abbb6d2da1c9bc45456497364a4602999
- evidence_id: support-2328-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /verified; /records; /warnings; /warning_scope
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: ROOT accepts twenty original stored parses, all paired comparisons and
    declared keys. Two original undefined-stereo warnings remain global and unassigned.
  snapshot_sha256: aa8d2b7772b4907ebb043566a7016cd09fa16acee7cd80d449a7292b9f787125
- evidence_id: support-2328-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-native-gates-acceptance-001.json
  locator: /status; /accepted; /five_local_commands_passed; /all_native_gates_passed;
    /unavailable_required_gates
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Five original local commands passed; full QC and complete OAK authority
    coverage remain unavailable.
  snapshot_sha256: 7a2daeeecc690ede6862e80925055bb819c81ad72c293b2ab5f980a47ce0aa42
- evidence_id: support-2328-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: ROOT operated the one accepted diagnostic. No replay, alternate parse or
    owner-specific warning attribution is introduced by scientific authoring.
  snapshot_sha256: 589a14084b2981120032bfc10e40bb0105f2afda5e7300a7d5b296e1388951c4
- evidence_id: support-2328-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-target-input-plan-001.json
  locator: /records/7; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Complete accepted per-owner input plan; cohort totals 396 placements /
    68 paths, owner 39 placements.
  snapshot_sha256: bc361ca0270b857063f610d29fdc2c498e2ccf208d5f8ae3c0033c044923fe27
- evidence_id: support-2328-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Joint complete source reading and exact raw/history carry attribution,
    source-specific cautions and access limits; the notes precede scientific adjudication.
  snapshot_sha256: 98c23811517a583723d42fb365b4549d207753a27bd0e0c6654e836596cfad99
- evidence_id: support-2328-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: BGC performed one bounded 169-literal scan of eight directly opened implemented
    tables, including ignored files, with zero textual hits. Reserved decisions.tsv
    was unconsumed; no global absence claim follows.
  snapshot_sha256: 98c23811517a583723d42fb365b4549d207753a27bd0e0c6654e836596cfad99
- evidence_id: support-2328-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/matched_chebi_ids; /contexts/24/source_scope_inventory/source_taxa;
    /contexts/24/source_scope_inventory/forward_taxon_merge_matches; /contexts/24/source_scope_inventory/nonorganism_matches;
    /contexts/24/source_scope_inventory/actual_assay_rows; /contexts/24/source_scope_inventory/blank_AID_sentinels;
    /contexts/24/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained route metadata, including assay/sentinel distinctions
    and exact empty routes. Exact copied saved values: {"/contexts/24/source_scope_inventory/actual_assay_rows":
    [], "/contexts/24/source_scope_inventory/blank_AID_sentinels": [], "/contexts/24/source_scope_inventory/forward_taxon_merge_matches":
    [], "/contexts/24/source_scope_inventory/matched_chebi_ids": ["CHEBI:46702"],
    "/contexts/24/source_scope_inventory/nonorganism_matches": [], "/contexts/24/source_scope_inventory/related_corpus_rows":
    [], "/contexts/24/source_scope_inventory/source_taxa": ["NCBITaxon:100226", "NCBITaxon:13443",
    "NCBITaxon:1586124", "NCBITaxon:161934", "NCBITaxon:177969", "NCBITaxon:182063",
    "NCBITaxon:1883", "NCBITaxon:1886", "NCBITaxon:1902", "NCBITaxon:1911", "NCBITaxon:1932",
    "NCBITaxon:1944", "NCBITaxon:33903", "NCBITaxon:3589", "NCBITaxon:38033", "NCBITaxon:3885",
    "NCBITaxon:40318", "NCBITaxon:42684", "NCBITaxon:4577", "NCBITaxon:511157", "NCBITaxon:53033",
    "NCBITaxon:5791", "NCBITaxon:59299", "NCBITaxon:67267", "NCBITaxon:68280"]}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/4;
    /cached_taxonomy/whole_stanzas/5; /cached_taxonomy/whole_stanzas/6; /cached_taxonomy/whole_stanzas/7;
    /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/whole_stanzas/19; /cached_taxonomy/whole_stanzas/23;
    /cached_taxonomy/whole_stanzas/27; /cached_taxonomy/whole_stanzas/28; /cached_taxonomy/whole_stanzas/30;
    /cached_taxonomy/whole_stanzas/31; /cached_taxonomy/whole_stanzas/32; /cached_taxonomy/whole_stanzas/35;
    /cached_taxonomy/whole_stanzas/36; /cached_taxonomy/whole_stanzas/37; /cached_taxonomy/whole_stanzas/39;
    /cached_taxonomy/whole_stanzas/40; /cached_taxonomy/whole_stanzas/43; /cached_taxonomy/whole_stanzas/50;
    /cached_taxonomy/whole_stanzas/52; /cached_taxonomy/whole_stanzas/53; /cached_taxonomy/whole_stanzas/74;
    /cached_taxonomy/whole_stanzas/91
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'All applicable cached stanzas copied in full; names/synonyms remain local
    snapshots. Exact copied saved values: {"/cached_taxonomy/whole_stanzas/19": {"complete_stanza":
    "[Term]\nid: NCBITaxon:3885\nname: Phaseolus vulgaris\n\n", "id": "NCBITaxon:3885",
    "physical_line": 5800}, "/cached_taxonomy/whole_stanzas/2": {"complete_stanza":
    "[Term]\nid: NCBITaxon:1883\nname: Streptomyces\nsynonym: \"\\\"Microstreptospora\\\"
    Yan et al.\" EXACT []\nsynonym: \"Actinopycnidium Krasil''nikov 1962\" EXACT []\nsynonym:
    \"Actinosporangium Krasil''nikov and Yuan 1961\" EXACT []\nsynonym: \"Chainia\"
    EXACT []\nsynonym: \"Elytrosporangium Falcao de Morais et al. 1966\" EXACT []\nsynonym:
    \"Kitasatoa Matsumae and Hata 1968 (Approved Lists 1980)\" EXACT []\nsynonym:
    \"Microellobosporia\" EXACT []\nsynonym: \"Streptoverticillium Baldacci 1958\"
    EXACT []\n\n", "id": "NCBITaxon:1883", "physical_line": 2798}, "/cached_taxonomy/whole_stanzas/23":
    {"complete_stanza": "[Term]\nid: NCBITaxon:4577\nname: Zea mays\nsynonym: \"Zea
    mays var. japonica\" EXACT []\n\n", "id": "NCBITaxon:4577", "physical_line": 7255},
    "/cached_taxonomy/whole_stanzas/27": {"complete_stanza": "[Term]\nid: NCBITaxon:5791\nname:
    Badhamia polycephala\nsynonym: \"Physarum polycephalum\" EXACT []\n\n", "id":
    "NCBITaxon:5791", "physical_line": 8915}, "/cached_taxonomy/whole_stanzas/28":
    {"complete_stanza": "[Term]\nid: NCBITaxon:13443\nname: Coffea arabica\n\n", "id":
    "NCBITaxon:13443", "physical_line": 10977}, "/cached_taxonomy/whole_stanzas/3":
    {"complete_stanza": "[Term]\nid: NCBITaxon:1886\nname: Streptomyces albidoflavus\nsynonym:
    \"Actinomyces albidoflavus\" EXACT []\nsynonym: \"Actinomyces globisporus var.
    caucasicus\" EXACT []\nsynonym: \"Cladothrix albido-flava\" EXACT []\nsynonym:
    \"Streptomyces albidoflavus (Rossi Doria 1891) Waksman and Henrici 1948 (Approved
    Lists 1980)\" EXACT []\nsynonym: \"Streptomyces globisporus subsp. caucasicus\"
    EXACT []\n\n", "id": "NCBITaxon:1886", "physical_line": 2820}, "/cached_taxonomy/whole_stanzas/30":
    {"complete_stanza": "[Term]\nid: NCBITaxon:33903\nname: Streptomyces avermitilis\nsynonym:
    \"Streptomyces avermectinius\" EXACT []\n\n", "id": "NCBITaxon:33903", "physical_line":
    14687}, "/cached_taxonomy/whole_stanzas/31": {"complete_stanza": "[Term]\nid:
    NCBITaxon:38033\nname: Chaetomium globosum\nsynonym: \"Chaetomium rectum\" EXACT
    []\n\n", "id": "NCBITaxon:38033", "physical_line": 16592}, "/cached_taxonomy/whole_stanzas/32":
    {"complete_stanza": "[Term]\nid: NCBITaxon:40318\nname: Streptomyces nodosus\n\n",
    "id": "NCBITaxon:40318", "physical_line": 17770}, "/cached_taxonomy/whole_stanzas/35":
    {"complete_stanza": "[Term]\nid: NCBITaxon:42684\nname: Streptomyces collinus\n\n",
    "id": "NCBITaxon:42684", "physical_line": 19479}, "/cached_taxonomy/whole_stanzas/36":
    {"complete_stanza": "[Term]\nid: NCBITaxon:53033\nname: Symphyogyna brongniartii\n\n",
    "id": "NCBITaxon:53033", "physical_line": 24297}, "/cached_taxonomy/whole_stanzas/37":
    {"complete_stanza": "[Term]\nid: NCBITaxon:59299\nname: Streptomyces thermocarboxydus\n\n",
    "id": "NCBITaxon:59299", "physical_line": 27256}, "/cached_taxonomy/whole_stanzas/39":
    {"complete_stanza": "[Term]\nid: NCBITaxon:67267\nname: Streptomyces alboflavus\nsynonym:
    \"Actinomyces alboflavus\" EXACT []\nsynonym: \"Streptomyces albiflavus\" EXACT
    []\n\n", "id": "NCBITaxon:67267", "physical_line": 29939}, "/cached_taxonomy/whole_stanzas/4":
    {"complete_stanza": "[Term]\nid: NCBITaxon:1902\nname: Streptomyces coelicolor\nsynonym:
    \"Actinomyces coelicolor\" EXACT []\nsynonym: \"Cladothrix coelicolor\" EXACT
    []\nsynonym: \"Nocardia coelicolor\" EXACT []\nsynonym: \"Streptomyces coelicolor
    (Muller 1908) Waksman and Henrici 1948 (Approved Lists 1980)\" EXACT []\nsynonym:
    \"Streptomyces coelicolor subspecies coelicolor\" EXACT []\n\n", "id": "NCBITaxon:1902",
    "physical_line": 2915}, "/cached_taxonomy/whole_stanzas/40": {"complete_stanza":
    "[Term]\nid: NCBITaxon:68280\nname: Streptomyces violaceusniger\nsynonym: \"\\\"Streptomyces
    violaceo-niger\\\" (Waksman and Curtis 1916) Waksman and Henrici 1948\" EXACT
    []\nsynonym: \"Actinomyces violaceus-niger\" EXACT []\nsynonym: \"Streptomyces
    violaceiniger\" EXACT []\nsynonym: \"Streptomyces violaceoniger\" EXACT []\nsynonym:
    \"Streptomyces violaceus-niger\" EXACT []\n\n", "id": "NCBITaxon:68280", "physical_line":
    30810}, "/cached_taxonomy/whole_stanzas/43": {"complete_stanza": "[Term]\nid:
    NCBITaxon:100226\nname: Streptomyces coelicolor A3(2)\n\n", "id": "NCBITaxon:100226",
    "physical_line": 41549}, "/cached_taxonomy/whole_stanzas/5": {"complete_stanza":
    "[Term]\nid: NCBITaxon:1911\nname: Streptomyces griseus\nsynonym: \"Streptomyces
    cavourensis subsp. washingtonensis\" EXACT []\nsynonym: \"Streptomyces fimicarius\"
    EXACT []\nsynonym: \"Streptomyces fimicarius (Duche 1934) Waksman and Henrici
    1948 (Approved Lists 1980)\" EXACT []\nsynonym: \"Streptomyces griseus (Krainsky
    1914) Waksman and Henrici 1948 (Approved Lists 1980)\" EXACT []\nsynonym: \"Streptomyces
    setonii\" EXACT []\nsynonym: \"Streptomyces setonii (Millard and Burr 1926) Waksman
    1953 (Approved Lists 1980)\" EXACT []\n\n", "id": "NCBITaxon:1911", "physical_line":
    2971}, "/cached_taxonomy/whole_stanzas/50": {"complete_stanza": "[Term]\nid: NCBITaxon:161934\nname:
    Beta vulgaris\nsynonym: \"Beta altissima\" EXACT []\n\n", "id": "NCBITaxon:161934",
    "physical_line": 55335}, "/cached_taxonomy/whole_stanzas/52": {"complete_stanza":
    "[Term]\nid: NCBITaxon:177969\nname: Oscillatoria brevis\n\n", "id": "NCBITaxon:177969",
    "physical_line": 59083}, "/cached_taxonomy/whole_stanzas/53": {"complete_stanza":
    "[Term]\nid: NCBITaxon:182063\nname: Cystoderma amianthinum\nsynonym: \"Agaricus
    amianthinus\" EXACT []\n\n", "id": "NCBITaxon:182063", "physical_line": 60234},
    "/cached_taxonomy/whole_stanzas/6": {"complete_stanza": "[Term]\nid: NCBITaxon:1932\nname:
    Streptomyces tendae\n\n", "id": "NCBITaxon:1932", "physical_line": 3078}, "/cached_taxonomy/whole_stanzas/7":
    {"complete_stanza": "[Term]\nid: NCBITaxon:1944\nname: Streptomyces halstedii\nsynonym:
    \"Actinomyces halstedii\" EXACT []\n\n", "id": "NCBITaxon:1944", "physical_line":
    3136}, "/cached_taxonomy/whole_stanzas/74": {"complete_stanza": "[Term]\nid: NCBITaxon:511157\nname:
    Cystoderma carcharias\nsynonym: \"Agaricus carcharias\" EXACT []\nsynonym: \"Cystoderma
    carcharias var. carcharias\" EXACT []\n\n", "id": "NCBITaxon:511157", "physical_line":
    99997}, "/cached_taxonomy/whole_stanzas/9": {"complete_stanza": "[Term]\nid: NCBITaxon:3589\nname:
    Basella alba\n\n", "id": "NCBITaxon:3589", "physical_line": 4941}, "/cached_taxonomy/whole_stanzas/91":
    {"complete_stanza": "[Term]\nid: NCBITaxon:1586124\nname: Phlegmacium herculeum\nsynonym:
    \"Cortinarius herculeus\" EXACT []\n\n", "id": "NCBITaxon:1586124", "physical_line":
    133979}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/mibig_compounds":
    {"matches": [{"last_physical_line": 1404, "physical_line": 1404, "raw_tsv_record":
    "BGC0001181\t4\tactive\tquestionable\tunknown\tgeosmin\t1\tC[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C\tInChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1\tJLPUXFOGCDVKGO-TUAOUCFPSA-N\ttrue\t\t\tNCBITaxon:100226\tStreptomyces
    coelicolor A3(2)\tterpene\tSesquiterpene\tAL645882.2\t6666219\t6668399\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1038/s41564-020-0697-x\tCOMPOUND_BIOACTIVITY\n",
    "row": {"bgc_classes": "terpene", "bgc_subclasses": "Sesquiterpene", "cluster_link_evidence_basis":
    "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name":
    "geosmin", "database_ids": "", "entry_completeness": "unknown", "entry_quality":
    "questionable", "entry_status": "active", "entry_version": "4", "genome_accession":
    "AL645882.2", "locus_evidence_methods": "", "locus_from": "6666219", "locus_to":
    "6668399", "mibig_accession": "BGC0001181", "primary_reference": "DOI:10.1038/s41564-020-0697-x",
    "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "COMPOUND_BIOACTIVITY",
    "smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C", "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1",
    "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:100226", "taxon_label": "Streptomyces coelicolor A3(2)"},
    "row_sha256": "6704a99b28e0eb8375c36f67355e689d61466deffcb2f0a9ee54edf98d764ad6"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 1404–1404, row_sha256 6704a99b28e0eb8375c36f67355e689d61466deffcb2f0a9ee54edf98d764ad6
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"bgc_classes": "terpene", "bgc_subclasses":
    "Sesquiterpene", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes":
    "", "compound_index": "1", "compound_name": "geosmin", "database_ids": "", "entry_completeness":
    "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version":
    "4", "genome_accession": "AL645882.2", "locus_evidence_methods": "", "locus_from":
    "6666219", "locus_to": "6668399", "mibig_accession": "BGC0001181", "primary_reference":
    "DOI:10.1038/s41564-020-0697-x", "producer_evidence_basis": "SOURCE_ASSERTION",
    "reference_basis": "COMPOUND_BIOACTIVITY", "smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C",
    "standard_inchi": "InChI=1S/C12H22O/c1-10-6-5-8-11(2)7-3-4-9-12(10,11)13/h10,13H,3-9H2,1-2H3/t10-,11+,12-/m0/s1",
    "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:100226", "taxon_label": "Streptomyces coelicolor A3(2)"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2328-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/chebi_structures":
    {"matches": [{"last_physical_line": 12450, "physical_line": 12450, "raw_tsv_record":
    "CHEBI:46702\t(−)-geosmin\tThe (−)-stereoisomer of geosmin, having 4S,4aS,8aR
    configuration.\t3\tJLPUXFOGCDVKGO-TUAOUCFPSA-N\tC[C@H]1CCC[C@@]2(C)CCCC[C@]12O\n",
    "row": {"chebi_id": "CHEBI:46702", "definition": "The (−)-stereoisomer of geosmin,
    having 4S,4aS,8aR configuration.", "name": "(−)-geosmin", "smiles": "C[C@H]1CCC[C@@]2(C)CCCC[C@]12O",
    "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "stars": "3"}, "row_sha256":
    "76866239889b583a5ce6fdaa036a2a7ad89e6004a762f614e039bb206fd7e094"}], "predicate":
    "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-source-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line 1; physical lines 12450–12450, row_sha256 76866239889b583a5ce6fdaa036a2a7ad89e6004a762f614e039bb206fd7e094
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"chebi_id": "CHEBI:46702", "definition":
    "The (−)-stereoisomer of geosmin, having 4S,4aS,8aR configuration.", "name": "(−)-geosmin",
    "smiles": "C[C@H]1CCC[C@@]2(C)CCCC[C@]12O", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "stars": "3"}]'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: support-2328-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/lotus_occurrences":
    {"matches": [{"last_physical_line": 3400, "physical_line": 3400, "raw_tsv_record":
    "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCoffea arabica\tNCBITaxon:13443\thttp://www.wikidata.org/entity/Q47685\t10.1007/S002170100305\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Coffea arabica", "organism_wikidata": "http://www.wikidata.org/entity/Q47685",
    "reference_doi": "10.1007/S002170100305", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:13443"},
    "row_sha256": "f39c8894cd66b13bcf803bd3645fff0697a9ea6a90d6cd542b640c5e544e4851"},
    {"last_physical_line": 3401, "physical_line": 3401, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCortinarius
    herculeus\tNCBITaxon:1586124\thttp://www.wikidata.org/entity/Q84325870\t10.1080/00275514.1999.12060999\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Cortinarius herculeus", "organism_wikidata": "http://www.wikidata.org/entity/Q84325870",
    "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1586124"},
    "row_sha256": "853e818c627de61a1f130746bf13f1a431e19b8673f6a2f7e63e1786670895e7"},
    {"last_physical_line": 3402, "physical_line": 3402, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCortinarius
    herculeus\tNCBITaxon:1586124\thttp://www.wikidata.org/entity/Q84325870\t10.2307/3761199\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Cortinarius herculeus", "organism_wikidata": "http://www.wikidata.org/entity/Q84325870",
    "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1586124"},
    "row_sha256": "f7d1581b4962994647e99120bdca4f6cf152b4ae9393fcf72969717c73267747"},
    {"last_physical_line": 3403, "physical_line": 3403, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tBeta
    vulgaris\tNCBITaxon:161934\thttp://www.wikidata.org/entity/Q165191\t10.1021/JF60204A059\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Beta vulgaris", "organism_wikidata": "http://www.wikidata.org/entity/Q165191",
    "reference_doi": "10.1021/JF60204A059", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:161934"},
    "row_sha256": "85ae3b7d13f9008263b8eaa5a5756d739c445a12c52c9705c4e3ed17f04b552e"},
    {"last_physical_line": 3404, "physical_line": 3404, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tOscillatoria
    brevis\tNCBITaxon:177969\thttp://www.wikidata.org/entity/Q39087436\t10.1007/BF00416598\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Oscillatoria brevis", "organism_wikidata": "http://www.wikidata.org/entity/Q39087436",
    "reference_doi": "10.1007/BF00416598", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:177969"},
    "row_sha256": "a675146489fd8da933fdb3eefd846ede4962f6a46c2f3d14323d0f6ca38ca775"},
    {"last_physical_line": 3405, "physical_line": 3405, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCystoderma
    amianthinum\tNCBITaxon:182063\thttp://www.wikidata.org/entity/Q470766\t10.1080/00275514.1999.12060999\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Cystoderma amianthinum", "organism_wikidata": "http://www.wikidata.org/entity/Q470766",
    "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:182063"},
    "row_sha256": "d4e32c23e78cf6c8eb737bca2a7e1f104c9c22bc99f5d13760d45249cf9ad385"},
    {"last_physical_line": 3406, "physical_line": 3406, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCystoderma
    amianthinum\tNCBITaxon:182063\thttp://www.wikidata.org/entity/Q470766\t10.2307/3761199\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Cystoderma amianthinum", "organism_wikidata": "http://www.wikidata.org/entity/Q470766",
    "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:182063"},
    "row_sha256": "7099822ac917ac35022ebdcb47dda5a2f6691606aa34b6ed1f0f26d0ec822645"},
    {"last_physical_line": 3407, "physical_line": 3407, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces\tNCBITaxon:1883\thttp://www.wikidata.org/entity/Q1144013\t10.1016/J.YMBEN.2018.09.004\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces", "organism_wikidata": "http://www.wikidata.org/entity/Q1144013",
    "reference_doi": "10.1016/J.YMBEN.2018.09.004", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1883"},
    "row_sha256": "95a5af39ae07f3a86a47b7700cc0a1fa7e09de4201444298d33155068e50c285"},
    {"last_physical_line": 3408, "physical_line": 3408, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.1007/S10295-013-1383-2\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.1007/S10295-013-1383-2", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    "row_sha256": "566422294c2282e2b959f44d4c3125ea28e9e491c8801605970cc8dda41d3332"},
    {"last_physical_line": 3409, "physical_line": 3409, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.1016/B978-0-12-404634-4.00014-0\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.1016/B978-0-12-404634-4.00014-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    "row_sha256": "21e457a613f7ce6f69a3b88731200fd74a766a7a626be163a58bc876bc0ef1fd"},
    {"last_physical_line": 3410, "physical_line": 3410, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.1021/JA062669X\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.1021/JA062669X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    "row_sha256": "3c516ccb9ab97d4cd1576721f86438b9b1766c3f1e3f63ad5b1b5cc291386b7e"},
    {"last_physical_line": 3411, "physical_line": 3411, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.1038/NCHEMBIO.2007.29\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.1038/NCHEMBIO.2007.29", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    "row_sha256": "99e9b351b0392ac5a4bbb8cd0b765620743456548b729dd4ebb5b29cf93a5f17"},
    {"last_physical_line": 3412, "physical_line": 3412, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.1371/JOURNAL.PONE.0060665\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.1371/JOURNAL.PONE.0060665", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    "row_sha256": "bf071144c166ed8425b104d63e98ec364b4e125c6ab6d05171db6507d4bdf296"},
    {"last_physical_line": 3413, "physical_line": 3413, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    albidoflavus\tNCBITaxon:1886\thttp://www.wikidata.org/entity/Q22286833\t10.7164/ANTIBIOTICS.47.434\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.7164/ANTIBIOTICS.47.434", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    "row_sha256": "02a068b81663e63db6789cc1f4185b5ecf2d3f4a70f3f35bb5167c2e6929d8d6"},
    {"last_physical_line": 3414, "physical_line": 3414, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    coelicolor\tNCBITaxon:1902\thttp://www.wikidata.org/entity/Q2355919\t10.1007/S10295-013-1383-2\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919",
    "reference_doi": "10.1007/S10295-013-1383-2", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"},
    "row_sha256": "1f890a991496e8905b030e038d4ac45cdafed7483aa3e6171300b6c4f3f518bb"},
    {"last_physical_line": 3415, "physical_line": 3415, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    coelicolor\tNCBITaxon:1902\thttp://www.wikidata.org/entity/Q2355919\t10.1016/B978-0-12-404634-4.00014-0\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919",
    "reference_doi": "10.1016/B978-0-12-404634-4.00014-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"},
    "row_sha256": "ecc92e79bf7a18729488c6376c06cdfb5120795582adadefd4b88b73a9de849c"},
    {"last_physical_line": 3416, "physical_line": 3416, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    coelicolor\tNCBITaxon:1902\thttp://www.wikidata.org/entity/Q2355919\t10.1021/JA062669X\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919",
    "reference_doi": "10.1021/JA062669X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"},
    "row_sha256": "6d38a8437c1b1f607271dd42f890d80660dd59acbdf766d69af993f40d7d4632"},
    {"last_physical_line": 3417, "physical_line": 3417, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    coelicolor\tNCBITaxon:1902\thttp://www.wikidata.org/entity/Q2355919\t10.1038/NCHEMBIO.2007.29\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919",
    "reference_doi": "10.1038/NCHEMBIO.2007.29", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"},
    "row_sha256": "ce92ad966f3d83defd6be290bfd8fc658c74664a418d049601db6b79e50d5916"},
    {"last_physical_line": 3418, "physical_line": 3418, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    coelicolor\tNCBITaxon:1902\thttp://www.wikidata.org/entity/Q2355919\t10.1371/JOURNAL.PONE.0060665\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919",
    "reference_doi": "10.1371/JOURNAL.PONE.0060665", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"},
    "row_sha256": "9caf9d4eecbf52bd7469ef8979a78864b01732a08378b3b8f03054202f1df44f"},
    {"last_physical_line": 3419, "physical_line": 3419, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    griseus\tNCBITaxon:1911\thttp://www.wikidata.org/entity/Q7623385\t10.1111/J.1365-2672.1992.TB01818.X\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces griseus", "organism_wikidata": "http://www.wikidata.org/entity/Q7623385",
    "reference_doi": "10.1111/J.1365-2672.1992.TB01818.X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1911"},
    "row_sha256": "248c59284d20d9a59fd6f76dda150ca1c0f286a73ac6ccc80635f33454b0c13a"},
    {"last_physical_line": 3420, "physical_line": 3420, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    tendae\tNCBITaxon:1932\thttp://www.wikidata.org/entity/Q26292941\t10.1021/JF00013A023\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces tendae", "organism_wikidata": "http://www.wikidata.org/entity/Q26292941",
    "reference_doi": "10.1021/JF00013A023", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1932"},
    "row_sha256": "f48204609c585a373b268b5bfa820380c67438be301fe905596458bc8edccffb"},
    {"last_physical_line": 3421, "physical_line": 3421, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    tendae\tNCBITaxon:1932\thttp://www.wikidata.org/entity/Q26292941\t10.1128/AEM.57.12.3429-3432.1991\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces tendae", "organism_wikidata": "http://www.wikidata.org/entity/Q26292941",
    "reference_doi": "10.1128/AEM.57.12.3429-3432.1991", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1932"},
    "row_sha256": "157461c537f7ab0da7e9b4607668ee0ae13f1a5e1016f579093d6954499ca0bc"},
    {"last_physical_line": 3422, "physical_line": 3422, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    halstedii\tNCBITaxon:1944\thttp://www.wikidata.org/entity/Q22665882\t10.1038/SJ.JIM.7000121\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces halstedii", "organism_wikidata": "http://www.wikidata.org/entity/Q22665882",
    "reference_doi": "10.1038/SJ.JIM.7000121", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1944"},
    "row_sha256": "2f597a7a73224b7d4f246a3e5810500c3ebcc453fd524b97e55f304e69db0f26"},
    {"last_physical_line": 3423, "physical_line": 3423, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    avermitilis\tNCBITaxon:33903\thttp://www.wikidata.org/entity/Q1946562\t10.1007/BF02932133\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562",
    "reference_doi": "10.1007/BF02932133", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:33903"},
    "row_sha256": "779eec39f7b00feb8acabaa993b20f6784196620098e5de893c37fce4ee7d871"},
    {"last_physical_line": 3424, "physical_line": 3424, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    avermitilis\tNCBITaxon:33903\thttp://www.wikidata.org/entity/Q1946562\t10.1038/JA.2006.66\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562",
    "reference_doi": "10.1038/JA.2006.66", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:33903"},
    "row_sha256": "bfabd1276aa3dcfef734119a8c7da4ba9eb2f9c0ffd920568614bd4218751315"},
    {"last_physical_line": 3425, "physical_line": 3425, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tBasella
    alba\tNCBITaxon:3589\thttp://www.wikidata.org/entity/Q1130368\t10.1016/0889-1575(91)90017-Z\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Basella alba", "organism_wikidata": "http://www.wikidata.org/entity/Q1130368",
    "reference_doi": "10.1016/0889-1575(91)90017-Z", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:3589"},
    "row_sha256": "ab9e8cbb6ee1a05314c4710d462928a560decf314681ba2f8db1b8829820f889"},
    {"last_physical_line": 3426, "physical_line": 3426, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tChaetomium
    globosum\tNCBITaxon:38033\thttp://www.wikidata.org/entity/Q2947551\t10.1248/CPB.29.1782\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Chaetomium globosum", "organism_wikidata": "http://www.wikidata.org/entity/Q2947551",
    "reference_doi": "10.1248/CPB.29.1782", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:38033"},
    "row_sha256": "02c65c91a5769170c16facadcb501e97e83e389c554f69c71b9d77d03610969a"},
    {"last_physical_line": 3427, "physical_line": 3427, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tChaetomium
    globosum\tNCBITaxon:38033\thttp://www.wikidata.org/entity/Q2947551\t10.1248/CPB.31.659\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Chaetomium globosum", "organism_wikidata": "http://www.wikidata.org/entity/Q2947551",
    "reference_doi": "10.1248/CPB.31.659", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:38033"},
    "row_sha256": "d052d91d92526058cc3e69f52ea1344d1cd30595e1d0ebe7c533beacf3de2664"},
    {"last_physical_line": 3428, "physical_line": 3428, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tPhaseolus
    vulgaris\tNCBITaxon:3885\thttp://www.wikidata.org/entity/Q42339\t10.1021/JF60204A050\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Phaseolus vulgaris", "organism_wikidata": "http://www.wikidata.org/entity/Q42339",
    "reference_doi": "10.1021/JF60204A050", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:3885"},
    "row_sha256": "a9ae78c91d53d7d5cd8d40f56b284e88cd4ee0bb7b0e1691be8d26c3172d8e3d"},
    {"last_physical_line": 3429, "physical_line": 3429, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    nodosus\tNCBITaxon:40318\thttp://www.wikidata.org/entity/Q16759083\t10.1007/S00253-015-7060-9\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces nodosus", "organism_wikidata": "http://www.wikidata.org/entity/Q16759083",
    "reference_doi": "10.1007/S00253-015-7060-9", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:40318"},
    "row_sha256": "01ce925e9fe51ba8393a352587ccac012437a9aa565f9c523a92c38d9f153e5f"},
    {"last_physical_line": 3430, "physical_line": 3430, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    nodosus\tNCBITaxon:40318\thttp://www.wikidata.org/entity/Q16759083\t10.1016/S0031-9422(02)00282-0\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces nodosus", "organism_wikidata": "http://www.wikidata.org/entity/Q16759083",
    "reference_doi": "10.1016/S0031-9422(02)00282-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:40318"},
    "row_sha256": "30f6aa62ec38509dadb35027f807133845faf3aa6a4b9cb9e55708675af566b8"},
    {"last_physical_line": 3431, "physical_line": 3431, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    collinus\tNCBITaxon:42684\thttp://www.wikidata.org/entity/Q22287122\t10.1007/S10295-015-1685-7\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces collinus", "organism_wikidata": "http://www.wikidata.org/entity/Q22287122",
    "reference_doi": "10.1007/S10295-015-1685-7", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:42684"},
    "row_sha256": "6909114cdaa1bc7e56c0ff9ecab414072d3928549b453f0e1633fc9061937c75"},
    {"last_physical_line": 3432, "physical_line": 3432, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tZea
    mays\tNCBITaxon:4577\thttp://www.wikidata.org/entity/Q11575\t10.1021/JF60218A022\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Zea mays", "organism_wikidata": "http://www.wikidata.org/entity/Q11575",
    "reference_doi": "10.1021/JF60218A022", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:4577"},
    "row_sha256": "40ca61bf73b706b01f9797afd0f3f0edc56a6d405cd69999d1d2e44ca265cbdd"},
    {"last_physical_line": 3433, "physical_line": 3433, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tZea
    mays\tNCBITaxon:4577\thttp://www.wikidata.org/entity/Q11575\t10.1021/JF60220A012\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Zea mays", "organism_wikidata": "http://www.wikidata.org/entity/Q11575",
    "reference_doi": "10.1021/JF60220A012", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:4577"},
    "row_sha256": "4aeddbf3e4f114f5a13100df1b77d4c17b3e35a5a2d17b9bbc0b1aee5dda684d"},
    {"last_physical_line": 3434, "physical_line": 3434, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCystoderma
    carcharias\tNCBITaxon:511157\thttp://www.wikidata.org/entity/Q2640662\t10.1080/00275514.1999.12060999\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Cystoderma carcharias", "organism_wikidata": "http://www.wikidata.org/entity/Q2640662",
    "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:511157"},
    "row_sha256": "628094eba90ad4db960756763055ea96b9da1e0fa041d59f393867034f130fd0"},
    {"last_physical_line": 3435, "physical_line": 3435, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tCystoderma
    carcharias\tNCBITaxon:511157\thttp://www.wikidata.org/entity/Q2640662\t10.2307/3761199\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Cystoderma carcharias", "organism_wikidata": "http://www.wikidata.org/entity/Q2640662",
    "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:511157"},
    "row_sha256": "cb57ed522a0ef4fda608802169abc5c0b1a1e7b133f4bbee2bd8e795ee75ab57"},
    {"last_physical_line": 3436, "physical_line": 3436, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tSymphyogyna
    brongniartii\tNCBITaxon:53033\thttp://www.wikidata.org/entity/Q17268765\t10.1515/ZNC-1991-3-404\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Symphyogyna brongniartii", "organism_wikidata": "http://www.wikidata.org/entity/Q17268765",
    "reference_doi": "10.1515/ZNC-1991-3-404", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:53033"},
    "row_sha256": "16697d76b4a0dd3f6aa126c9de6f8601d74231ef6da9a8091e8128f79a13e866"},
    {"last_physical_line": 3437, "physical_line": 3437, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tPhysarum
    polycephalum\tNCBITaxon:5791\thttp://www.wikidata.org/entity/Q134950\t10.1248/CPB.32.797\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Physarum polycephalum", "organism_wikidata": "http://www.wikidata.org/entity/Q134950",
    "reference_doi": "10.1248/CPB.32.797", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:5791"},
    "row_sha256": "8ee7a4b00c045b2f2da9448f366f16a80d5172ad445346bee273faec07f95829"},
    {"last_physical_line": 3438, "physical_line": 3438, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    thermocarboxydus\tNCBITaxon:59299\thttp://www.wikidata.org/entity/Q16992819\t10.1007/S00253-019-10240-3\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces thermocarboxydus", "organism_wikidata":
    "http://www.wikidata.org/entity/Q16992819", "reference_doi": "10.1007/S00253-019-10240-3",
    "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q420233",
    "taxon_id": "NCBITaxon:59299"}, "row_sha256": "aedfb016c3fc799bb52079a8ce9281c74b2006a43844379a67368d6438f4f4a6"},
    {"last_physical_line": 3439, "physical_line": 3439, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    alboflavus\tNCBITaxon:67267\thttp://www.wikidata.org/entity/Q22286851\t10.1111/1574-6968.12088\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces alboflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286851",
    "reference_doi": "10.1111/1574-6968.12088", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:67267"},
    "row_sha256": "3daf3a2b747d942c3dd4e1c403b6fb30715bf4c90652b01bf4b3aedf7ef90d3f"},
    {"last_physical_line": 3440, "physical_line": 3440, "raw_tsv_record": "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tStreptomyces
    violaceusniger\tNCBITaxon:68280\thttp://www.wikidata.org/entity/Q26293318\t10.1039/C4CC00177J\thttp://www.wikidata.org/entity/Q420233\n",
    "row": {"organism_name": "Streptomyces violaceusniger", "organism_wikidata": "http://www.wikidata.org/entity/Q26293318",
    "reference_doi": "10.1039/C4CC00177J", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:68280"},
    "row_sha256": "bdd70c803dc6ea84e1a782b3949fd50d70308c0180dacad7dc222e35b7353edb"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 3400–3400, row_sha256 f39c8894cd66b13bcf803bd3645fff0697a9ea6a90d6cd542b640c5e544e4851;
    physical lines 3401–3401, row_sha256 853e818c627de61a1f130746bf13f1a431e19b8673f6a2f7e63e1786670895e7;
    physical lines 3402–3402, row_sha256 f7d1581b4962994647e99120bdca4f6cf152b4ae9393fcf72969717c73267747;
    physical lines 3403–3403, row_sha256 85ae3b7d13f9008263b8eaa5a5756d739c445a12c52c9705c4e3ed17f04b552e;
    physical lines 3404–3404, row_sha256 a675146489fd8da933fdb3eefd846ede4962f6a46c2f3d14323d0f6ca38ca775;
    physical lines 3405–3405, row_sha256 d4e32c23e78cf6c8eb737bca2a7e1f104c9c22bc99f5d13760d45249cf9ad385;
    physical lines 3406–3406, row_sha256 7099822ac917ac35022ebdcb47dda5a2f6691606aa34b6ed1f0f26d0ec822645;
    physical lines 3407–3407, row_sha256 95a5af39ae07f3a86a47b7700cc0a1fa7e09de4201444298d33155068e50c285;
    physical lines 3408–3408, row_sha256 566422294c2282e2b959f44d4c3125ea28e9e491c8801605970cc8dda41d3332;
    physical lines 3409–3409, row_sha256 21e457a613f7ce6f69a3b88731200fd74a766a7a626be163a58bc876bc0ef1fd;
    physical lines 3410–3410, row_sha256 3c516ccb9ab97d4cd1576721f86438b9b1766c3f1e3f63ad5b1b5cc291386b7e;
    physical lines 3411–3411, row_sha256 99e9b351b0392ac5a4bbb8cd0b765620743456548b729dd4ebb5b29cf93a5f17;
    physical lines 3412–3412, row_sha256 bf071144c166ed8425b104d63e98ec364b4e125c6ab6d05171db6507d4bdf296;
    physical lines 3413–3413, row_sha256 02a068b81663e63db6789cc1f4185b5ecf2d3f4a70f3f35bb5167c2e6929d8d6;
    physical lines 3414–3414, row_sha256 1f890a991496e8905b030e038d4ac45cdafed7483aa3e6171300b6c4f3f518bb;
    physical lines 3415–3415, row_sha256 ecc92e79bf7a18729488c6376c06cdfb5120795582adadefd4b88b73a9de849c;
    physical lines 3416–3416, row_sha256 6d38a8437c1b1f607271dd42f890d80660dd59acbdf766d69af993f40d7d4632;
    physical lines 3417–3417, row_sha256 ce92ad966f3d83defd6be290bfd8fc658c74664a418d049601db6b79e50d5916;
    physical lines 3418–3418, row_sha256 9caf9d4eecbf52bd7469ef8979a78864b01732a08378b3b8f03054202f1df44f;
    physical lines 3419–3419, row_sha256 248c59284d20d9a59fd6f76dda150ca1c0f286a73ac6ccc80635f33454b0c13a;
    physical lines 3420–3420, row_sha256 f48204609c585a373b268b5bfa820380c67438be301fe905596458bc8edccffb;
    physical lines 3421–3421, row_sha256 157461c537f7ab0da7e9b4607668ee0ae13f1a5e1016f579093d6954499ca0bc;
    physical lines 3422–3422, row_sha256 2f597a7a73224b7d4f246a3e5810500c3ebcc453fd524b97e55f304e69db0f26;
    physical lines 3423–3423, row_sha256 779eec39f7b00feb8acabaa993b20f6784196620098e5de893c37fce4ee7d871;
    physical lines 3424–3424, row_sha256 bfabd1276aa3dcfef734119a8c7da4ba9eb2f9c0ffd920568614bd4218751315;
    physical lines 3425–3425, row_sha256 ab9e8cbb6ee1a05314c4710d462928a560decf314681ba2f8db1b8829820f889;
    physical lines 3426–3426, row_sha256 02c65c91a5769170c16facadcb501e97e83e389c554f69c71b9d77d03610969a;
    physical lines 3427–3427, row_sha256 d052d91d92526058cc3e69f52ea1344d1cd30595e1d0ebe7c533beacf3de2664;
    physical lines 3428–3428, row_sha256 a9ae78c91d53d7d5cd8d40f56b284e88cd4ee0bb7b0e1691be8d26c3172d8e3d;
    physical lines 3429–3429, row_sha256 01ce925e9fe51ba8393a352587ccac012437a9aa565f9c523a92c38d9f153e5f;
    physical lines 3430–3430, row_sha256 30f6aa62ec38509dadb35027f807133845faf3aa6a4b9cb9e55708675af566b8;
    physical lines 3431–3431, row_sha256 6909114cdaa1bc7e56c0ff9ecab414072d3928549b453f0e1633fc9061937c75;
    physical lines 3432–3432, row_sha256 40ca61bf73b706b01f9797afd0f3f0edc56a6d405cd69999d1d2e44ca265cbdd;
    physical lines 3433–3433, row_sha256 4aeddbf3e4f114f5a13100df1b77d4c17b3e35a5a2d17b9bbc0b1aee5dda684d;
    physical lines 3434–3434, row_sha256 628094eba90ad4db960756763055ea96b9da1e0fa041d59f393867034f130fd0;
    physical lines 3435–3435, row_sha256 cb57ed522a0ef4fda608802169abc5c0b1a1e7b133f4bbee2bd8e795ee75ab57;
    physical lines 3436–3436, row_sha256 16697d76b4a0dd3f6aa126c9de6f8601d74231ef6da9a8091e8128f79a13e866;
    physical lines 3437–3437, row_sha256 8ee7a4b00c045b2f2da9448f366f16a80d5172ad445346bee273faec07f95829;
    physical lines 3438–3438, row_sha256 aedfb016c3fc799bb52079a8ce9281c74b2006a43844379a67368d6438f4f4a6;
    physical lines 3439–3439, row_sha256 3daf3a2b747d942c3dd4e1c403b6fb30715bf4c90652b01bf4b3aedf7ef90d3f;
    physical lines 3440–3440, row_sha256 bdd70c803dc6ea84e1a782b3949fd50d70308c0180dacad7dc222e35b7353edb
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"organism_name": "Coffea arabica",
    "organism_wikidata": "http://www.wikidata.org/entity/Q47685", "reference_doi":
    "10.1007/S002170100305", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:13443"},
    {"organism_name": "Cortinarius herculeus", "organism_wikidata": "http://www.wikidata.org/entity/Q84325870",
    "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1586124"},
    {"organism_name": "Cortinarius herculeus", "organism_wikidata": "http://www.wikidata.org/entity/Q84325870",
    "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1586124"},
    {"organism_name": "Beta vulgaris", "organism_wikidata": "http://www.wikidata.org/entity/Q165191",
    "reference_doi": "10.1021/JF60204A059", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:161934"},
    {"organism_name": "Oscillatoria brevis", "organism_wikidata": "http://www.wikidata.org/entity/Q39087436",
    "reference_doi": "10.1007/BF00416598", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:177969"},
    {"organism_name": "Cystoderma amianthinum", "organism_wikidata": "http://www.wikidata.org/entity/Q470766",
    "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:182063"},
    {"organism_name": "Cystoderma amianthinum", "organism_wikidata": "http://www.wikidata.org/entity/Q470766",
    "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:182063"},
    {"organism_name": "Streptomyces", "organism_wikidata": "http://www.wikidata.org/entity/Q1144013",
    "reference_doi": "10.1016/J.YMBEN.2018.09.004", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1883"},
    {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.1007/S10295-013-1383-2", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.1016/B978-0-12-404634-4.00014-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.1021/JA062669X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.1038/NCHEMBIO.2007.29", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.1371/JOURNAL.PONE.0060665", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    {"organism_name": "Streptomyces albidoflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286833",
    "reference_doi": "10.7164/ANTIBIOTICS.47.434", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1886"},
    {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919",
    "reference_doi": "10.1007/S10295-013-1383-2", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"},
    {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919",
    "reference_doi": "10.1016/B978-0-12-404634-4.00014-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"},
    {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919",
    "reference_doi": "10.1021/JA062669X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"},
    {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919",
    "reference_doi": "10.1038/NCHEMBIO.2007.29", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"},
    {"organism_name": "Streptomyces coelicolor", "organism_wikidata": "http://www.wikidata.org/entity/Q2355919",
    "reference_doi": "10.1371/JOURNAL.PONE.0060665", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1902"},
    {"organism_name": "Streptomyces griseus", "organism_wikidata": "http://www.wikidata.org/entity/Q7623385",
    "reference_doi": "10.1111/J.1365-2672.1992.TB01818.X", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1911"},
    {"organism_name": "Streptomyces tendae", "organism_wikidata": "http://www.wikidata.org/entity/Q26292941",
    "reference_doi": "10.1021/JF00013A023", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1932"},
    {"organism_name": "Streptomyces tendae", "organism_wikidata": "http://www.wikidata.org/entity/Q26292941",
    "reference_doi": "10.1128/AEM.57.12.3429-3432.1991", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1932"},
    {"organism_name": "Streptomyces halstedii", "organism_wikidata": "http://www.wikidata.org/entity/Q22665882",
    "reference_doi": "10.1038/SJ.JIM.7000121", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:1944"},
    {"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562",
    "reference_doi": "10.1007/BF02932133", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:33903"},
    {"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562",
    "reference_doi": "10.1038/JA.2006.66", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:33903"},
    {"organism_name": "Basella alba", "organism_wikidata": "http://www.wikidata.org/entity/Q1130368",
    "reference_doi": "10.1016/0889-1575(91)90017-Z", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:3589"},
    {"organism_name": "Chaetomium globosum", "organism_wikidata": "http://www.wikidata.org/entity/Q2947551",
    "reference_doi": "10.1248/CPB.29.1782", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:38033"},
    {"organism_name": "Chaetomium globosum", "organism_wikidata": "http://www.wikidata.org/entity/Q2947551",
    "reference_doi": "10.1248/CPB.31.659", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:38033"},
    {"organism_name": "Phaseolus vulgaris", "organism_wikidata": "http://www.wikidata.org/entity/Q42339",
    "reference_doi": "10.1021/JF60204A050", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:3885"},
    {"organism_name": "Streptomyces nodosus", "organism_wikidata": "http://www.wikidata.org/entity/Q16759083",
    "reference_doi": "10.1007/S00253-015-7060-9", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:40318"},
    {"organism_name": "Streptomyces nodosus", "organism_wikidata": "http://www.wikidata.org/entity/Q16759083",
    "reference_doi": "10.1016/S0031-9422(02)00282-0", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:40318"},
    {"organism_name": "Streptomyces collinus", "organism_wikidata": "http://www.wikidata.org/entity/Q22287122",
    "reference_doi": "10.1007/S10295-015-1685-7", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:42684"},
    {"organism_name": "Zea mays", "organism_wikidata": "http://www.wikidata.org/entity/Q11575",
    "reference_doi": "10.1021/JF60218A022", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:4577"},
    {"organism_name": "Zea mays", "organism_wikidata": "http://www.wikidata.org/entity/Q11575",
    "reference_doi": "10.1021/JF60220A012", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:4577"},
    {"organism_name": "Cystoderma carcharias", "organism_wikidata": "http://www.wikidata.org/entity/Q2640662",
    "reference_doi": "10.1080/00275514.1999.12060999", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:511157"},
    {"organism_name": "Cystoderma carcharias", "organism_wikidata": "http://www.wikidata.org/entity/Q2640662",
    "reference_doi": "10.2307/3761199", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:511157"},
    {"organism_name": "Symphyogyna brongniartii", "organism_wikidata": "http://www.wikidata.org/entity/Q17268765",
    "reference_doi": "10.1515/ZNC-1991-3-404", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:53033"},
    {"organism_name": "Physarum polycephalum", "organism_wikidata": "http://www.wikidata.org/entity/Q134950",
    "reference_doi": "10.1248/CPB.32.797", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:5791"},
    {"organism_name": "Streptomyces thermocarboxydus", "organism_wikidata": "http://www.wikidata.org/entity/Q16992819",
    "reference_doi": "10.1007/S00253-019-10240-3", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:59299"},
    {"organism_name": "Streptomyces alboflavus", "organism_wikidata": "http://www.wikidata.org/entity/Q22286851",
    "reference_doi": "10.1111/1574-6968.12088", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:67267"},
    {"organism_name": "Streptomyces violaceusniger", "organism_wikidata": "http://www.wikidata.org/entity/Q26293318",
    "reference_doi": "10.1039/C4CC00177J", "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q420233", "taxon_id": "NCBITaxon:68280"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2328-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/cyanometdb_occurrences":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/npclassifier":
    {"matches": [{"last_physical_line": 1128, "physical_line": 1128, "raw_tsv_record":
    "JLPUXFOGCDVKGO-TUAOUCFPSA-N\tC[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C\tTerpenoids\tSesquiterpenoids\tEudesmane
    sesquiterpenoids|Noreudesmane sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n",
    "row": {"class_results": "Eudesmane sesquiterpenoids|Noreudesmane sesquiterpenoids",
    "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C",
    "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "superclass_results": "Sesquiterpenoids"},
    "row_sha256": "d7a04a9b9d0fd8865254139891ef4e5a447c86bdb02c2c4e0bd65165ce344ebf"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 1128–1128, row_sha256 d7a04a9b9d0fd8865254139891ef4e5a447c86bdb02c2c4e0bd65165ce344ebf
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"class_results": "Eudesmane sesquiterpenoids|Noreudesmane
    sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "C[C@H]1CCC[C@@]2([C@@]1(CCCC2)O)C",
    "standard_inchi_key": "JLPUXFOGCDVKGO-TUAOUCFPSA-N", "superclass_results": "Sesquiterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2328-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/pubchem_bioassay":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/bindingdb_targets":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/antibioticmech_inchikeys":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "JLPUXFOGCDVKGO-TUAOUCFPSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/24/source_scope_inventory/joins/chebi_origins":
    {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows",
    "query": ["CHEBI:46702"]}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /records/7/direct_companion_paths; /records/7/direct_companion_predicates
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Exact direct companion scope; shared locus/key predicates do not transfer
    identity or evidence. Exact copied saved values: {"/records/7/direct_companion_paths":
    [], "/records/7/direct_companion_predicates": []}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /records/7/direct_companion_paths
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete source and raw/history context carries remain explicitly attributed
    in source notes. Distinct companion metadata: []'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2328-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 175–200; lines 368–435
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Schema distinguishes retained structures, partial stereo and versioned
    computed classification from experimentally asserted identity.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2328-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 145–174
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Source stereo_complete derives from unassigned tetrahedral centers in source
    SMILES; predicate inspection does not establish natural stereochemistry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2328-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 296–307; lines 982–1020
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Maintained seeder preserves source structure and versioned model arrays;
    no regeneration was run for scientific authoring.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2328-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Twelve scientific dimensions, claim-specific evidence and partial completion
    reflect actual access limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2328-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current skill under absolute user no-outbound constraint
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Read-only review, source ownership and no native-status promotion apply;
    no external lookup was authorized.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: support-2328-mechanism-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/7/owner_document/causal_graphs; /records/7/owner_document/biosynthetic_pathway;
    /records/7/owner_document/curation_history
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained graph/pathway/history, with historical primary-experiment
    labels and protein mapping distinct from fresh verification. Exact copied saved
    values: {"/records/7/owner_document/biosynthetic_pathway": [{"enzyme_id": "UniProtKB:Q9X839",
    "enzyme_label": "Cyc2 germacradienol/germacrene D synthase", "evidence": [{"evidence_type":
    "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to the Streptomyces
    coelicolor A3(2) cyc2/SCO6073 gene product, maps to EMBL AL939126 protein CAB41566.1,
    and annotates RHEA:22436 for formation of the germacradienol geosmin intermediate.",
    "reference": "DOI:10.1073/pnas.0337625100", "snippet": "Expression and mechanistic
    analysis of a germacradienol synthase"}], "notes": "The N-terminal domain of bifunctional
    Cyc2 cyclizes (2E,6E)-farnesyl diphosphate to germacradienol, the sesquiterpene
    alcohol intermediate in geosmin biosynthesis.", "product": "CHEBI:46734", "reaction_id":
    "RHEA:22436", "step_number": 1, "substrate": "CHEBI:175763"}, {"enzyme_id": "UniProtKB:Q9X839",
    "enzyme_label": "Cyc2 geosmin synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT",
    "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073
    gene product; the domain-resolved study showed that the N-terminal domain forms
    germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin
    reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional
    geosmin synthase mechanism"}], "notes": "The C-terminal domain of bifunctional
    Cyc2 converts germacradienol to (−)-geosmin.", "product": "CHEBI:46702", "reaction_id":
    "RHEA:30371", "step_number": 2, "substrate": "CHEBI:46734"}], "/records/7/owner_document/causal_graphs":
    [{"description": "Partial Streptomyces coelicolor geosmin biosynthesis graph for
    bifunctional Cyc2 conversion of farnesyl diphosphate to (−)-geosmin through germacradienol.",
    "edges": [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "object": "cyc2", "predicate": "is cyclized by", "subject": "farnesyl_diphosphate"},
    {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "object": "germacradienol", "predicate": "forms", "subject": "cyc2"}, {"evidence":
    [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to
    the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved
    study showed that the N-terminal domain forms germacradienol and that the C-terminal
    domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference":
    "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase
    mechanism"}], "object": "cyc2", "predicate": "is converted by", "subject": "germacradienol"},
    {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved
    study showed that the N-terminal domain forms germacradienol and that the C-terminal
    domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference":
    "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase
    mechanism"}], "object": "geosmin", "predicate": "forms", "subject": "cyc2"}],
    "graph_id": "geosmin-cyc2-biosynthesis", "nodes": [{"grounding_status": "GROUNDED",
    "identifier": "CHEBI:175763", "label": "(2E,6E)-farnesyl diphosphate", "node_id":
    "farnesyl_diphosphate", "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED",
    "identifier": "UniProtKB:Q9X839", "label": "Cyc2", "node_id": "cyc2", "node_type":
    "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46734", "label":
    "germacradienol", "node_id": "germacradienol", "node_type": "COMPOUND"}, {"grounding_status":
    "GROUNDED", "identifier": "CHEBI:46702", "label": "(−)-geosmin", "node_id": "geosmin",
    "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"}], "/records/7/owner_document/curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:08Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:02:26Z"},
    {"action": "RECORD_CURATED", "changes": "Added a two-step BIOSYNTHESIS pathway
    and causal graph for geosmin biosynthesis; grounded the Streptomyces coelicolor
    bifunctional Cyc2 enzyme to UniProtKB:Q9X839 via SCO6073; and cited the experimentally
    characterized RHEA:22436 and RHEA:30371 reactions.", "curator": "codex", "llm_assisted":
    true, "timestamp": "2026-09-26T22:48:26Z"}, {"action": "RECORD_CURATED", "changes":
    "Replaced the geosmin-forming Cyc2 step and edge evidence with the domain-resolved
    bifunctional geosmin synthase paper, DOI:10.1038/nchembio.2007.29.", "curator":
    "codex", "llm_assisted": true, "timestamp": "2026-09-26T23:08:49Z"}]}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2328-reader
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/native-current233-geosmin-maintained-reader-DATA-001.json
  locator: /status; /counts; /returned_view_equals_expected_complete_owner; /view_mismatches;
    /resolved_view/causal_graphs; /resolved_view/biosynthetic_pathway; /resolved_view/curation_history;
    /limitations
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Accepted maintained result preserves the complete owner and exact historical
    mechanism. No primary/sequence verification is added. Exact copied saved values:
    {"/counts": {"component_graphs": 0, "component_history_events": [], "component_refs":
    0, "curation_history": 4, "edges": 4, "graphs": 1, "inline_graphs": 1, "molecular_targets":
    0, "nodes": 4, "pathway_steps": 2}, "/limitations": ["Maintained topology and,
    where references exist, component schema/ownership/history validation are distinct
    from complete-owner preservation. They do not independently verify mechanism science,
    primary publications, sequences, constructs, groundings or the full owner schema.",
    "The expected-view object is a comparison oracle from the separately captured
    complete owner and complete ordered components; only causal_graphs is expanded.
    It is not a substitute for the one maintained call.", "Every owner field, target
    measurement/evidence item, pathway item and owner history is preserved; raw root
    presence is checked exactly, and only resolved causal_graphs may be added for
    a component-only owner. Referenced graphs append after inline graphs in exact
    reference order. Complete component documents and their histories remain separately
    preserved in component_captures. Owners without refs retain absent refs and empty
    components.", "Any known urllib3 socket-construction capability probe is denied
    before action and retained explicitly; any other denial fails this attempt.",
    "Critical dependency and resource pins are pre/post checked. Additional actually
    loaded local modules and file reads are recorded, not claimed statically exhaustively
    reviewed.", "Raw primary-experiment labels, database references, protein identifiers
    and historical source claims remain attributed annotations; the complete maintained
    view does not add primary, sequence, producer, natural-identity or stereochemical
    verification.", "No molecular parsing, canonical gate, Git command, campaign read
    or record mutation is invoked."], "/resolved_view/biosynthetic_pathway": [{"enzyme_id":
    "UniProtKB:Q9X839", "enzyme_label": "Cyc2 germacradienol/germacrene D synthase",
    "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "notes": "The N-terminal domain of bifunctional Cyc2 cyclizes (2E,6E)-farnesyl
    diphosphate to germacradienol, the sesquiterpene alcohol intermediate in geosmin
    biosynthesis.", "product": "CHEBI:46734", "reaction_id": "RHEA:22436", "step_number":
    1, "substrate": "CHEBI:175763"}, {"enzyme_id": "UniProtKB:Q9X839", "enzyme_label":
    "Cyc2 geosmin synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT",
    "notes": "UniProtKB:Q9X839 resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073
    gene product; the domain-resolved study showed that the N-terminal domain forms
    germacradienol and that the C-terminal domain catalyzes the RHEA:30371 germacradienol-to-geosmin
    reaction.", "reference": "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional
    geosmin synthase mechanism"}], "notes": "The C-terminal domain of bifunctional
    Cyc2 converts germacradienol to (−)-geosmin.", "product": "CHEBI:46702", "reaction_id":
    "RHEA:30371", "step_number": 2, "substrate": "CHEBI:46734"}], "/resolved_view/causal_graphs":
    [{"description": "Partial Streptomyces coelicolor geosmin biosynthesis graph for
    bifunctional Cyc2 conversion of farnesyl diphosphate to (−)-geosmin through germacradienol.",
    "edges": [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "object": "cyc2", "predicate": "is cyclized by", "subject": "farnesyl_diphosphate"},
    {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product, maps
    to EMBL AL939126 protein CAB41566.1, and annotates RHEA:22436 for formation of
    the germacradienol geosmin intermediate.", "reference": "DOI:10.1073/pnas.0337625100",
    "snippet": "Expression and mechanistic analysis of a germacradienol synthase"}],
    "object": "germacradienol", "predicate": "forms", "subject": "cyc2"}, {"evidence":
    [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839 resolves to
    the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved
    study showed that the N-terminal domain forms germacradienol and that the C-terminal
    domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference":
    "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase
    mechanism"}], "object": "cyc2", "predicate": "is converted by", "subject": "germacradienol"},
    {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "UniProtKB:Q9X839
    resolves to the Streptomyces coelicolor A3(2) cyc2/SCO6073 gene product; the domain-resolved
    study showed that the N-terminal domain forms germacradienol and that the C-terminal
    domain catalyzes the RHEA:30371 germacradienol-to-geosmin reaction.", "reference":
    "DOI:10.1038/nchembio.2007.29", "snippet": "the bifunctional geosmin synthase
    mechanism"}], "object": "geosmin", "predicate": "forms", "subject": "cyc2"}],
    "graph_id": "geosmin-cyc2-biosynthesis", "nodes": [{"grounding_status": "GROUNDED",
    "identifier": "CHEBI:175763", "label": "(2E,6E)-farnesyl diphosphate", "node_id":
    "farnesyl_diphosphate", "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED",
    "identifier": "UniProtKB:Q9X839", "label": "Cyc2", "node_id": "cyc2", "node_type":
    "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:46734", "label":
    "germacradienol", "node_id": "germacradienol", "node_type": "COMPOUND"}, {"grounding_status":
    "GROUNDED", "identifier": "CHEBI:46702", "label": "(−)-geosmin", "node_id": "geosmin",
    "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"}], "/resolved_view/curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:08Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:02:26Z"},
    {"action": "RECORD_CURATED", "changes": "Added a two-step BIOSYNTHESIS pathway
    and causal graph for geosmin biosynthesis; grounded the Streptomyces coelicolor
    bifunctional Cyc2 enzyme to UniProtKB:Q9X839 via SCO6073; and cited the experimentally
    characterized RHEA:22436 and RHEA:30371 reactions.", "curator": "codex", "llm_assisted":
    true, "timestamp": "2026-09-26T22:48:26Z"}, {"action": "RECORD_CURATED", "changes":
    "Replaced the geosmin-forming Cyc2 step and edge evidence with the domain-resolved
    bifunctional geosmin synthase paper, DOI:10.1038/nchembio.2007.29.", "curator":
    "codex", "llm_assisted": true, "timestamp": "2026-09-26T23:08:49Z"}], "/returned_view_equals_expected_complete_owner":
    true, "/status": "maintained_reader_returned_and_verified_offline", "/view_mismatches":
    []}'
  snapshot_sha256: 2f540243dbd7e0cfcf24a9befdfce649170186c6b06358c76c5a75302a6e4e65
- evidence_id: support-2328-reader-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-current233-geosmin-maintained-reader-acceptance-001.json
  locator: /status; /accepted; /DATA; /execution; /original_tools; /verification;
    /review_check_contract
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'ROOT acceptance of the original reader, including exact check contract
    and before-action blocked capability probe. Exact copied saved values: {"/DATA":
    {"bytes": 704621, "path": "/private/tmp/npm-review-work/shared-next-batch233/native-current233-geosmin-maintained-reader-DATA-001.json",
    "sha256": "2f540243dbd7e0cfcf24a9befdfce649170186c6b06358c76c5a75302a6e4e65"},
    "/accepted": true, "/execution": {"bytes": 5573, "path": "/private/tmp/npm-review-work/shared-next-batch233/native-current233-geosmin-reader-execution-001.json",
    "sha256": "97d220ea18aadb2b35a7f43a6e95f3d5a3fa38e2b6885e3e6113a0bae2d364da"},
    "/original_tools": {"bytes": 1233, "path": "/private/tmp/npm-review-work/shared-next-batch233/native-current233-geosmin-reader-original-tools-001.json",
    "sha256": "30a284a3b0e9b9371459e442a4caf0afd6dc2e81a2e8562ffd5f3d94e0b1a4c5"},
    "/review_check_contract": {"command": "/private/tmp/npm-record-reviews-20261021/.venv/bin/python
    -I -B /private/tmp/npm-review-work/shared-next-batch233/read-selected-mechanism-guarded-001.py
    2328 fd189cfeef53223564efc2e151e9ab13c9d4ff0eedbf2e9be9a97d35e2761db9 fee38fccf50dd95c8d1e025f3d6694a2bb81946e63438ab5f53f7e1bc7ed7152
    c6a354765f2590d29898156c1d68bac79ab532abcad168d75c278a0a0e3df077 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
    c40437dc157b29c3b4bf647a7e232564fff639b957c0ac7b3a604fc9c490d85a", "exit_code":
    0, "exit_source": "original tool terminal and process receipt", "name": "Complete
    offline maintained reader for geosmin", "required": true, "status": "passed",
    "target_order": 2328}, "/status": "accepted_original_offline_maintained_reader",
    "/verification": {"complete_owner_equality": true, "counts": {"component_graphs":
    0, "component_history_events": [], "component_refs": 0, "curation_history": 4,
    "edges": 4, "graphs": 1, "inline_graphs": 1, "molecular_targets": 0, "nodes":
    4, "pathway_steps": 2}, "current_paths": 1017, "current_pin_placements": 1944,
    "empty_stderr": true, "expected_before_action_denials": 1, "launch_environment_unchanged":
    true, "observed_runtime_only_environment": {"__CF_USER_TEXT_ENCODING": "0x1F5:0x0:0x0"},
    "original_exit_code": 0, "positive_content_exact": true, "unexpected_denials":
    0}}'
  snapshot_sha256: 7539e744ec2d81a1ac46beb8cfe082e8d6e11053ec6857342776af1a1c540d5f
- evidence_id: support-2328-reader-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/native-current233-geosmin-reader-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Native operated the one Geosmin maintained reader, original c0129f/session52080
    to f62a02/exit0, with empty stderr and no retry. ROOT separately accepted it.
  snapshot_sha256: 97d220ea18aadb2b35a7f43a6e95f3d5a3fa38e2b6885e3e6113a0bae2d364da
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-233/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json
  accessed_at: '2026-11-04T01:34:00.342391Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 2444131c9bbd175968f9d611c32bf3bbd12568e48a7b35408345deb11a289d74
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-233/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json
  accessed_at: '2026-11-04T01:34:25.871048Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 000c1c2d07219c9458f40443fecb23b8632036e95ae07b270a4f42ac7e26b30c
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-233/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json
  accessed_at: '2026-11-04T01:34:46.118004Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-233/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json
  accessed_at: '2026-11-04T01:35:21.245243Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-233/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json
  accessed_at: '2026-11-04T01:35:33.368121Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 23b82eee0ac99b361f8412dff6d8442ab42a37fb7d5a6453c6c277042174a02c
assessments:
- assessment_id: support-2328-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: 'CHEBI:46702 and the retained (−)-geosmin label are grounded by the complete
    key JLPUXFOGCDVKGO-TUAOUCFPSA-N and the exact three-star ChEBI structure row.
    The definition’s 4S,4aS,8aR configuration is compatible with the saved structure:
    SMILES atoms 1,6,5 respectively carry S,S,R. The optical sign is a retained source
    assertion and cannot be deduced from R/S labels. MIBiG BGC0001181 uses the related
    name geosmin; no broader isomer equivalence is inferred.'
  target_ids:
  - CHEBI:46702
  evidence_ids:
  - support-2328-grounding-owner
  - support-2328-source-mibig_compounds
  - support-2328-query-chebi_structures
  - support-2328-chemistry
  - support-2328-direct-contexts
  - support-2328-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: JLPUXFOGCDVKGO-TUAOUCFPSA-N; exact retained full key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - support-2328-grounding-owner
    - support-2328-source-mibig_compounds
    - support-2328-query-chebi_structures
    - support-2328-chemistry
    - support-2328-direct-contexts
    - support-2328-companion-boundaries
  - name: grounding_scope
    value: EXACT local CHEBI:46702 full-key match; source 4S,4aS,8aR and optical sign
      remain separately bounded.
    definition: Retained local grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2328-grounding-owner
    - support-2328-source-mibig_compounds
    - support-2328-query-chebi_structures
    - support-2328-chemistry
    - support-2328-direct-contexts
    - support-2328-companion-boundaries
- assessment_id: support-2328-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both forms are neutral C12H22O with 13 atoms and 14 bonds. Two saturated
    six-membered carbocycles share one edge, with two methyl substituents and a tertiary
    bridgehead alcohol. Three tetrahedral centers are specified; no carbonyl or sugar-ring
    motif is present. All ten comparisons are true and the original atom correspondence
    is complete, while full_graph_identity_established remains false. Different local
    chiral tag orderings do not contradict the identical canonical stereochemical
    representation; neither local parsing nor the full key proves natural optical
    rotation or sample purity.
  target_ids:
  - CHEBI:46702
  evidence_ids:
  - support-2328-grounding-owner
  - support-2328-chemistry
  - support-2328-topology
  - support-2328-diagnostic-acceptance
  - support-2328-structure-schema
  - support-2328-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Three specified centers; saved SMILES indices 1(S),6(S),5(R) align with
      source 4,4a,8a locants; no optical-sign inference.
    definition: Complete saved stereo/atom/bond interpretation; no new parse or experimental
      assignment.
    evidence_ids:
    - support-2328-grounding-owner
    - support-2328-chemistry
    - support-2328-topology
    - support-2328-diagnostic-acceptance
    - support-2328-structure-schema
    - support-2328-stereo-method
  - name: representation_correspondence
    value: All ten comparisons true and original map complete; full_graph_identity_established
      remains false.
    definition: Normalized identifier agreement does not establish fixed-graph or
      natural-form identity.
    evidence_ids:
    - support-2328-grounding-owner
    - support-2328-chemistry
    - support-2328-topology
    - support-2328-diagnostic-acceptance
    - support-2328-structure-schema
    - support-2328-stereo-method
- assessment_id: support-2328-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: Streptomyces coelicolor A3(2) NCBITaxon:100226 is SOURCE_ASSERTION from
    BGC0001181 version 4, whose source locus link remains CLUSTER_UNSTATED with no
    stated method. Its active/questionable/unknown metadata does not erase or upgrade
    the separately curated historical Cyc2 experiments. Forty-one LOTUS rows across
    broad taxa remain occurrence claims, not a reconstruction of production in every
    organism.
  target_ids:
  - CHEBI:46702
  evidence_ids:
  - support-2328-origin-owner
  - support-2328-source-mibig_compounds
  - support-2328-cached-taxonomy
  - support-2328-source-routes
  - support-2328-direct-contexts
  - support-2328-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: A3(2) 100226 producer assertion remains separate from the broad occurrence
      taxa and cached synonym relationships.
    definition: Producer, occurrence, species, strain and unresolved labels retain
      separate scope; cached labels are not fresh authority.
    evidence_ids:
    - support-2328-origin-owner
    - support-2328-source-mibig_compounds
    - support-2328-cached-taxonomy
    - support-2328-source-routes
    - support-2328-direct-contexts
    - support-2328-companion-boundaries
  - name: producer_evidence
    value: SOURCE_ASSERTION, BGC0001181 version 4; historical Cyc2 claims do not silently
      change this source grade.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - support-2328-origin-owner
    - support-2328-source-mibig_compounds
    - support-2328-cached-taxonomy
    - support-2328-source-routes
    - support-2328-direct-contexts
    - support-2328-companion-boundaries
  - name: locus_evidence
    value: CLUSTER_UNSTATED/no source method; partial historical Cyc2 pathway is separately
      evidenced.
    definition: Source version/status/method/grade is not a complete pathway or fresh
      primary verification.
    evidence_ids:
    - support-2328-origin-owner
    - support-2328-source-mibig_compounds
    - support-2328-cached-taxonomy
    - support-2328-source-routes
    - support-2328-direct-contexts
    - support-2328-companion-boundaries
- assessment_id: support-2328-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: The MIBiG producer/locus citation DOI:10.1038/s41564-020-0697-x is COMPOUND_BIOACTIVITY
    provenance. Historical mechanism DOI:10.1073/pnas.0337625100 supports the N-terminal
    germacradienol-forming role, while DOI:10.1038/nchembio.2007.29 supports the domain-resolved
    geosmin-forming role. The history records replacement of the latter evidence.
    Those retained PRIMARY_EXPERIMENT placements are distinct from database and LOTUS
    occurrence assertions; none was freshly accessed or sequence-verified.
  target_ids:
  - CHEBI:46702
  evidence_ids:
  - support-2328-origin-owner
  - support-2328-occurrence-owner
  - support-2328-source-mibig_compounds
  - support-2328-source-notes
  - support-2328-direct-contexts
  - support-2328-companion-boundaries
  - support-2328-source-chebi_structures
  - support-2328-source-lotus_occurrences
  - support-2328-mechanism-owner
  - support-2328-reader
  dimensions:
  - name: citation_scope
    value: Compound-bioactivity database provenance, two historical domain experiments
      and LOTUS occurrences retain distinct roles.
    definition: Database provenance, historical primary-experiment support and occurrence
      citations retain distinct roles; no publication independence or fresh access
      is assumed.
    evidence_ids:
    - support-2328-origin-owner
    - support-2328-occurrence-owner
    - support-2328-source-mibig_compounds
    - support-2328-source-notes
    - support-2328-direct-contexts
    - support-2328-companion-boundaries
    - support-2328-source-chebi_structures
    - support-2328-source-lotus_occurrences
    - support-2328-mechanism-owner
    - support-2328-reader
- assessment_id: support-2328-activity
  area: evidence
  topic: Activity
  outcome: supported
  summary: The complete retained LOTUS scope has 41 rows, represented by 25 written
    occurrences plus a sixteen-further note. Repeated taxon/publication placements
    are not independent experiments. Local cached Cortinarius/Phlegmacium and Physarum/Badhamia
    names retain synonym scope only. No written bioactivity or molecular target and
    no exact retained PubChem, BindingDB or sibling activity match is present. A COMPOUND_BIOACTIVITY
    citation on the MIBiG source is not itself a structured assay or proof of inactivity.
  target_ids:
  - CHEBI:46702
  evidence_ids:
  - support-2328-occurrence-owner
  - support-2328-assay-owner
  - support-2328-source-routes
  - support-2328-cached-taxonomy
  - support-2328-query-lotus_occurrences
  - support-2328-query-chebi_origins
  - support-2328-query-cyanometdb_occurrences
  - support-2328-query-pubchem_bioassay
  - support-2328-query-bindingdb_targets
  - support-2328-query-antibioticmech_inchikeys
  - support-2328-direct-contexts
  - support-2328-companion-boundaries
  dimensions:
  - name: occurrence_scope
    value: 41 retained rows =25 written +16 further; no claim of 41 independent experiments
      or producers.
    definition: Occurrence placements are not counts of independent experiments or
      demonstrated producers.
    evidence_ids:
    - support-2328-occurrence-owner
    - support-2328-assay-owner
    - support-2328-source-routes
    - support-2328-cached-taxonomy
    - support-2328-query-lotus_occurrences
    - support-2328-query-chebi_origins
    - support-2328-query-cyanometdb_occurrences
    - support-2328-query-pubchem_bioassay
    - support-2328-query-bindingdb_targets
    - support-2328-query-antibioticmech_inchikeys
    - support-2328-direct-contexts
    - support-2328-companion-boundaries
  - name: assay_target_scope
    value: No written activity/target or exact retained assay match; historical synthesis
      experiments are not target assays.
    definition: Exact retained assay/target assertions are bounded; phenotype titles
      are not direct mechanism proof.
    evidence_ids:
    - support-2328-occurrence-owner
    - support-2328-assay-owner
    - support-2328-source-routes
    - support-2328-cached-taxonomy
    - support-2328-query-lotus_occurrences
    - support-2328-query-chebi_origins
    - support-2328-query-cyanometdb_occurrences
    - support-2328-query-pubchem_bioassay
    - support-2328-query-bindingdb_targets
    - support-2328-query-antibioticmech_inchikeys
    - support-2328-direct-contexts
    - support-2328-companion-boundaries
- assessment_id: support-2328-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: NPClassifier retains Terpenoids / Sesquiterpenoids with both Eudesmane
    and Noreudesmane class strings and is_glycoside:false at its named version. The
    C12 bicyclic alcohol and retained C15-precursor conversion are compatible with
    a limited degraded-sesquiterpenoid discussion. Neither carbon count nor model
    labels alone establishes the natural pathway. Source TERPENE, historical Cyc2
    mechanism and computed filing remain separately attributed.
  target_ids:
  - CHEBI:46702
  evidence_ids:
  - support-2328-classification-owner
  - support-2328-source-mibig_compounds
  - support-2328-source-npclassifier
  - support-2328-chemistry
  - support-2328-topology
  - support-2328-structure-schema
  - support-2328-classification-seeder
  - support-2328-direct-contexts
  - support-2328-companion-boundaries
  dimensions:
  - name: classification_applicability
    value: Versioned Eudesmane/Noreudesmane predictions, C12 topology and C15-precursor
      historical mechanism retain distinct evidential scope.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct evidence types.
    evidence_ids:
    - support-2328-classification-owner
    - support-2328-source-mibig_compounds
    - support-2328-source-npclassifier
    - support-2328-chemistry
    - support-2328-topology
    - support-2328-structure-schema
    - support-2328-classification-seeder
    - support-2328-direct-contexts
    - support-2328-companion-boundaries
- assessment_id: support-2328-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: All twelve scientific dimensions were assessed against the complete owner/history,
    actual intake, complete retained source scope and both saved molecular forms.
    Five original local commands passed; full QC, complete OAK authority coverage
    and fresh primary/taxonomic verification remain unavailable. The selected Geosmin
    maintained reader returned once and preserved the complete owner and historical
    mechanism. No new supported maintained-source correction is established in this
    bounded evidence scope. Scientific completion remains partial; native status/history
    are unchanged.
  target_ids:
  - CHEBI:46702
  evidence_ids:
  - support-2328-owner
  - support-2328-capture
  - support-2328-intake
  - support-2328-intake-acceptance
  - support-2328-inventory-acceptance
  - support-2328-plan
  - support-2328-plan-acceptance
  - support-2328-source-notes
  - support-2328-curation-scope
  - support-2328-diagnostic-execution
  - support-2328-diagnostic-acceptance
  - support-2328-native-acceptance
  - support-2328-review-profile
  - support-2328-review-skill
  - support-2328-query-mibig_compounds
  - support-2328-query-chebi_structures
  - support-2328-query-lotus_occurrences
  - support-2328-query-cyanometdb_occurrences
  - support-2328-query-npclassifier
  - support-2328-query-pubchem_bioassay
  - support-2328-query-bindingdb_targets
  - support-2328-query-antibioticmech_inchikeys
  - support-2328-query-chebi_origins
  - support-2328-reader-acceptance
  - support-2328-reader-execution
  dimensions:
  - name: review_completion
    value: 'Partial: unavailable full QC/OAK and fresh source verification; no native-status
      promotion. No new supported maintained-source correction is established in this
      bounded evidence scope.'
    definition: Completion reflects actual evidence access and required-check coverage;
      parsing and gate success are not scientific proof.
    evidence_ids:
    - support-2328-owner
    - support-2328-capture
    - support-2328-intake
    - support-2328-intake-acceptance
    - support-2328-inventory-acceptance
    - support-2328-plan
    - support-2328-plan-acceptance
    - support-2328-source-notes
    - support-2328-curation-scope
    - support-2328-diagnostic-execution
    - support-2328-diagnostic-acceptance
    - support-2328-native-acceptance
    - support-2328-review-profile
    - support-2328-review-skill
    - support-2328-query-mibig_compounds
    - support-2328-query-chebi_structures
    - support-2328-query-lotus_occurrences
    - support-2328-query-cyanometdb_occurrences
    - support-2328-query-npclassifier
    - support-2328-query-pubchem_bioassay
    - support-2328-query-bindingdb_targets
    - support-2328-query-antibioticmech_inchikeys
    - support-2328-query-chebi_origins
    - support-2328-reader-acceptance
    - support-2328-reader-execution
- assessment_id: support-2328-pathway
  area: graph
  topic: Pathway
  outcome: supported
  summary: 'The two preserved steps use the same UniProtKB:Q9X839 Cyc2 protein: N-terminal
    conversion of CHEBI:175763 farnesyl diphosphate to CHEBI:46734 germacradienol
    with RHEA:22436, then C-terminal conversion to CHEBI:46702 with RHEA:30371. Two
    separate historical experiment citations are retained. This is an explicitly partial
    pathway, not complete upstream metabolism or newly verified reaction stoichiometry.
    SCO6073, AL939126/CAB41566.1 and domain mapping remain historical claims; no fresh
    protein sequence, construct, processing or strain-stock equality is established.'
  target_ids:
  - CHEBI:46702
  evidence_ids:
  - support-2328-mechanism-owner
  - support-2328-reader
  - support-2328-reader-acceptance
  - support-2328-reader-execution
- assessment_id: support-2328-graph
  area: graph
  topic: Graph
  outcome: supported
  summary: The accepted maintained reader preserves the complete owner, one inline
    BIOSYNTHESIS graph, four grounded nodes, four evidence-bearing edges, two pathway
    entries and all four history events. The graph separates substrate cyclization/germacradienol
    formation from conversion/geosmin formation through the same bifunctional Cyc2
    node. Four edge evidence placements reuse two citations and do not represent four
    independent experiments. No component or molecular-target root is declared. Reader
    preservation establishes representation fidelity, not fresh validation of the
    biological claims.
  target_ids:
  - CHEBI:46702
  evidence_ids:
  - support-2328-mechanism-owner
  - support-2328-reader
  - support-2328-reader-acceptance
  - support-2328-reader-execution
findings: []
actions: []
limitations:
- All evidence is retained locally. No external publication, identifier, taxonomy,
  protein sequence or natural stereochemical assertion was refreshed under the absolute
  no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original gates,
  stored-form parsing and maintained-reader preservation establish only their stated
  scope.
- Exact empty joins are bounded by saved predicates/snapshots; shared loci, names,
  taxa or citations do not transfer identity, production, activity or mechanism.
- Two original omitted-undefined-stereo warnings remain global and unassigned. No
  additional molecular/YAML parse, source query or target invocation occurred during
  scientific authoring.
- No source record or native status/history is edited. Any correction belongs to the
  maintained owners admitted in the actual intake.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support personally read all five complete raw owners/history, actual canonical intakes
  and its disjoint retained source partition; exact prior companion carries and BGC
  complementary readings remain explicitly attributed in the joint notes.
- 'Support personally read all ten saved forms: 292 atom and 320 bond rows, every
  scalar/ring/stereo/motif/map; terminals 75f742,41ef45,19e485,5b59bb. No alternate
  computation is substituted.'
- ROOT operated activation/capture, inventory/composer, canonical intakes and molecular
  diagnostic. Native operated original local gates and maintained readers under ROOT
  authorization; ROOT separately accepted results. Scientific authoring invoked none
  of those targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-233
```
