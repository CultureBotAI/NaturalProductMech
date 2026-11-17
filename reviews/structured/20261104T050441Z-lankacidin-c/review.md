# Local evidence review: lankacidin C

- Review: 20261104T050441Z-lankacidin-c
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T04:24:34.142593Z
- Finished UTC: 2026-11-04T05:04:41.492110Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Lankacidin C preserves matching, fully specified stored molecular forms and separately scoped Streptomyces rochei producer and occurrence assertions. The retained NRPS/PKS locus class and oxygenated nitrogen-bearing macrocycle make the computed Cembrane diterpenoid filing an applicability concern. No maintained-source defect is established by that prediction alone.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2346; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-441a8c4d3f | data/natural_products/terpenoids/lankacidin-c.yaml | generated | lankacidin C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-441a8c4d3f | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-441a8c4d3f | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-441a8c4d3f | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-441a8c4d3f | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-441a8c4d3f | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-441a8c4d3f | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-441a8c4d3f | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-441a8c4d3f | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: unknown. Targets: naturalproductmech:mibig-441a8c4d3f.

The minted identifier naturalproductmech:mibig-441a8c4d3f and complete key ATDILMLBOZKFGI-JUTMVFGESA-N preserve the compound labelled lankacidin C in MIBiG BGC0001100 version 5. NPAtlas NPA04098 remains an unrefreshed cross-reference. The exact retained ChEBI structure query has no match within its saved scope; it does not establish a new global absence. Matching stored identifiers and name provenance support local fidelity without independently re-establishing the natural isolate or its experimental structure assignment.

### Representation

representation: supported. Targets: naturalproductmech:mibig-441a8c4d3f.

Both complete saved forms are neutral C25H33NO7, with 33 heavy atoms, 34 bonds and one connected component. They retain a carbon macrocycle, an integrated six-membered lactone, two hydroxyls, a ring ketone and an acylamide side chain containing another ketone. The saved ring list includes alternate cycles and must not be interpreted as three independent rings. Six tetrahedral centres and four E alkenes are specified in both forms. The amide remains C19(=O20)-N18 in the SMILES table and C22(=O30)-N25 in the InChI-derived table; the mobile-H InChI layer has not produced a different fixed tautomer in this original diagnostic. All ten comparison flags are true. The recorded chirality-aware correspondence covers 33 atoms while full_graph_identity_established remains false; local Cis/Trans potential-stereo descriptors depend on atom ordering and do not contradict the aligned E bond labels. Stored completeness is not fresh experimental stereochemical proof.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-441a8c4d3f.

MIBiG BGC0001100 version 5 retains Streptomyces rochei (NCBITaxon:1928), GenBank AB088224.2 and locus coordinates 4922–35881. The active entry retains questionable quality and unknown completeness in its raw row. SOURCE_ASSERTION grades the producer, while CLUSTER_UNSTATED grades the locus because no method is stated. The NRPS and PKS source classes are separately asserted; no strain, complete pathway, enzyme activity or experimentally established producer is inferred from them.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-441a8c4d3f.

PMID:12791134 is retained at the MIBiG ENTRY level as a DATABASE_ASSERTION for producer/locus provenance. The twelve LOTUS DOI strings have occurrence scope, including publications expressed with different journal/year formats. Their presence is not proof of twelve independent isolations, and publication independence or equivalence to the entry-level PMID has not been established. No paper or identifier was freshly accessed.

### Activity

evidence: supported. Targets: naturalproductmech:mibig-441a8c4d3f.

All twelve written LOTUS occurrences name Streptomyces rochei and preserve twelve literal source references. The owner explicitly keeps occurrence separate from production and warns that citations can overlap. These rows do not upgrade SOURCE_ASSERTION or CLUSTER_UNSTATED. No bioactivity, pharmacological molecular target, graph or pathway is declared in the complete owner. Exact empty PubChem, BindingDB, sibling-corpus and other joins mean only no match in those retained query scopes, not universal absence of activity or biosynthesis.

### Classification

consistency: concern. Targets: naturalproductmech:mibig-441a8c4d3f.

NPClassifier npclassifier.gnps2.org@2026-09-07 faithfully supplies Terpenoids, Diterpenoids, Cembrane diterpenoids and is_glycoside:false. The C25 nitrogen-bearing macrocycle with acylamide/lactone functionality and the separate NRPS/PKS source classes make that model filing an applicability concern. Carbon count alone is not used to prove a biosynthetic class, and a faithful versioned prediction is not automatically a source-record error. The positive six-membered C5O motif is the integrated lactone, not an assigned sugar residue or glycosidic linkage; it does not contradict the retained false glycoside prediction.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-441a8c4d3f.

The complete current raw owner/history, actual canonical intake, assigned retained source rows and both complete saved forms have been read. No selected mechanism requires a maintained reader for this owner. Natural identity, source-only producer/locus grades and model applicability remain bounded; full QC, complete OAK coverage and fresh external verification are unavailable. No corrective finding is supported by the current evidence; final assembly will retain partial completion.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2346-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/lankacidin-c.yaml; Whole current owner plaintext and complete curation_history | supports | Complete owner and all 3 history events are covered by current exact whole-reading attribution. Native status remains SEEDED. |
| support-2346-capture | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/5 | supports | Complete original captured owner and exact mechanism/component presence, distinct from maintained resolution. Exact copied saved values: {"/records/5": {"component_captures": [], "mechanism_capture_scope": "raw_owner_and_declared_components_only_not_maintained_resolution", "order": 2346, "owner_document": {"bgc_class": ["NRPS", "PKS"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001100", "bgc_class": ["NRPS", "PKS"], "entry_status": "active", "entry_version": "5", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100 entry version 5; citation taken from the entry level", "reference": "PMID:12791134"}], "genome_accession": "genbank:AB088224.2", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 4922, "locus_to": 35881, "organism_label": "Streptomyces rochei", "organism_taxon_id": "NCBITaxon:1928"}], "chemical_structure": {"smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C", "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001100"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:03Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:01:28Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories and curation tables.", "curator": "seed_from_sources", "timestamp": "2026-10-13T10:42:36Z"}], "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "grounding_status": "MINTED", "identifier": "naturalproductmech:mibig-441a8c4d3f", "label": "lankacidin C", "np_classification": {"class_results": ["Cembrane diterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Diterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["ACTINOBACTERIAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1002/CBIC.201500393"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/J.JBIOSC.2018.03.006"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/J.TET.2011.05.047"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/S0378-1119(00)00060-3"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/JA.2010.146"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/S41598-019-47406-Y"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1046/J.1365-2958.2003.03523.X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1080/09168451.2014.882761"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1128/JB.01383-07"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1271/BBB.90591"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.26.647"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.47.1447"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001100", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100 entry version 5; citation taken from the entry level", "reference": "PMID:12791134"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "5", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei"}], "producer_taxon_groups": ["ACTINOBACTERIAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-441a8c4d3f", "source": "MIBIG", "source_id": "BGC0001100", "source_label": "lankacidin C", "source_version": "5"}], "xrefs": ["npatlas:NPA04098"]}, "owner_pin": {"bytes": 10540, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/lankacidin-c.yaml", "sha256": "efdee93632f199ca328314f66decb80dac20bee619b95f124158c22d299ee8a7"}, "path": "data/natural_products/terpenoids/lankacidin-c.yaml", "read_finished_at": "2026-11-04T04:24:34.146914Z", "read_started_at": "2026-11-04T04:24:34.142593Z"}} |
| support-2346-grounding-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/5/owner_document/identifier; /records/5/owner_document/label; /records/5/owner_document/chemical_structure; /records/5/owner_document/grounding_status; /records/5/owner_document/grounding_notes; /records/5/owner_document/source_concepts; /records/5/owner_document/xrefs | supports | Exact identity, source definition and grounding fields, including unresolved discussion where present. Exact copied saved values: {"/records/5/owner_document/chemical_structure": {"smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C", "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001100"}, "/records/5/owner_document/grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "/records/5/owner_document/grounding_status": "MINTED", "/records/5/owner_document/identifier": "naturalproductmech:mibig-441a8c4d3f", "/records/5/owner_document/label": "lankacidin C", "/records/5/owner_document/source_concepts": [{"minted_identifier": "naturalproductmech:mibig-441a8c4d3f", "source": "MIBIG", "source_id": "BGC0001100", "source_label": "lankacidin C", "source_version": "5"}], "/records/5/owner_document/xrefs": ["npatlas:NPA04098"]} |
| support-2346-origin-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/5/owner_document/producer_organisms; /records/5/owner_document/biosynthetic_gene_clusters; /records/5/owner_document/producer_taxon_groups | supports | Separately graded producer and locus source assertions. Exact copied saved values: {"/records/5/owner_document/biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001100", "bgc_class": ["NRPS", "PKS"], "entry_status": "active", "entry_version": "5", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100 entry version 5; citation taken from the entry level", "reference": "PMID:12791134"}], "genome_accession": "genbank:AB088224.2", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 4922, "locus_to": 35881, "organism_label": "Streptomyces rochei", "organism_taxon_id": "NCBITaxon:1928"}], "/records/5/owner_document/producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001100", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100 entry version 5; citation taken from the entry level", "reference": "PMID:12791134"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "5", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei"}], "/records/5/owner_document/producer_taxon_groups": ["ACTINOBACTERIAL"]} |
| support-2346-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/5/owner_document/occurrences; /records/5/owner_document/occurrence_taxon_groups | supports | Written occurrence placements and retained further-row notes. Exact copied saved values: {"/records/5/owner_document/occurrence_taxon_groups": ["ACTINOBACTERIAL"], "/records/5/owner_document/occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1002/CBIC.201500393"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/J.JBIOSC.2018.03.006"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/J.TET.2011.05.047"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/S0378-1119(00)00060-3"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/JA.2010.146"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/S41598-019-47406-Y"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1046/J.1365-2958.2003.03523.X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1080/09168451.2014.882761"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1128/JB.01383-07"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1271/BBB.90591"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.26.647"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.47.1447"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}]} |
| support-2346-assay-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/5/owner_document | supports | Written observations; whole-owner selector establishes optional-root absence within this owner only. Exact copied saved values: {"/records/5/owner_document": {"bgc_class": ["NRPS", "PKS"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001100", "bgc_class": ["NRPS", "PKS"], "entry_status": "active", "entry_version": "5", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100 entry version 5; citation taken from the entry level", "reference": "PMID:12791134"}], "genome_accession": "genbank:AB088224.2", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 4922, "locus_to": 35881, "organism_label": "Streptomyces rochei", "organism_taxon_id": "NCBITaxon:1928"}], "chemical_structure": {"smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C", "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001100"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:03Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:01:28Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories and curation tables.", "curator": "seed_from_sources", "timestamp": "2026-10-13T10:42:36Z"}], "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "grounding_status": "MINTED", "identifier": "naturalproductmech:mibig-441a8c4d3f", "label": "lankacidin C", "np_classification": {"class_results": ["Cembrane diterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Diterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["ACTINOBACTERIAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1002/CBIC.201500393"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/J.JBIOSC.2018.03.006"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/J.TET.2011.05.047"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1016/S0378-1119(00)00060-3"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/JA.2010.146"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1038/S41598-019-47406-Y"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1046/J.1365-2958.2003.03523.X"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1080/09168451.2014.882761"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1128/JB.01383-07"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1271/BBB.90591"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.26.647"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.47.1447"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001100", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100 entry version 5; citation taken from the entry level", "reference": "PMID:12791134"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "5", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei"}], "producer_taxon_groups": ["ACTINOBACTERIAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-441a8c4d3f", "source": "MIBIG", "source_id": "BGC0001100", "source_label": "lankacidin C", "source_version": "5"}], "xrefs": ["npatlas:NPA04098"]}} |
| support-2346-classification-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/5/owner_document/np_pathway; /records/5/owner_document/np_classification; /records/5/owner_document/bgc_class | supports | Versioned computed filing and separately asserted BGC/compound classes. Exact copied saved values: {"/records/5/owner_document/bgc_class": ["NRPS", "PKS"], "/records/5/owner_document/np_classification": {"class_results": ["Cembrane diterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Diterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "/records/5/owner_document/np_pathway": "TERPENOIDS"} |
| support-2346-chemistry | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/comparisons; /records/5/atom_correspondence | supports | Complete original declared forms/comparisons/map, unchanged. Exact copied saved values: {"/records/5/atom_correspondence": {"complete_atom_count_match": true, "full_graph_identity_established": false, "scope": "One chirality-aware substructure match; no independent full graph or natural identity claim.", "smiles_to_inchi_atom_indices": [19, 12, 18, 28, 10, 6, 13, 0, 5, 8, 17, 27, 9, 7, 14, 1, 11, 20, 25, 22, 30, 16, 3, 26, 24, 4, 23, 31, 32, 21, 29, 15, 2]}, "/records/5/comparisons": {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared": true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal": true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer": true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "/records/5/declared_structure": {"smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C", "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001100"}} |
| support-2346-topology | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json; /records/5/smiles/computed; /records/5/inchi/computed; /records/5/declared_structure; /records/5/comparisons; /records/5/atom_correspondence | supports | Both complete saved forms are neutral C25H33NO7, with 33 heavy atoms, 34 bonds and one connected component. They retain a carbon macrocycle, an integrated six-membered lactone, two hydroxyls, a ring ketone and an acylamide side chain containing another ketone. The saved ring list includes alternate cycles and must not be interpreted as three independent rings. Six tetrahedral centres and four E alkenes are specified in both forms. The amide remains C19(=O20)-N18 in the SMILES table and C22(=O30)-N25 in the InChI-derived table; the mobile-H InChI layer has not produced a different fixed tautomer in this original diagnostic. All ten comparison flags are true. The recorded chirality-aware correspondence covers 33 atoms while full_graph_identity_established remains false; local Cis/Trans potential-stereo descriptors depend on atom ordering and do not contradict the aligned E bond labels. Stored completeness is not fresh experimental stereochemical proof. |
| support-2346-intake | /private/tmp/npm-review-work/shared-next-batch235/intakes/2346-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake, all admitted input roles and maintained correction ownership. Exact copied saved values: {"/repository": "CultureBotAI/NaturalProductMech", "/source": {"git_revision": "ce6a5498df5be51116bd5e0c119023ee62bb5464", "inputs": [{"path": ".claude/skills/curate-yaml-record/references/review-checklist.md", "role": "context", "sha256": "13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9"}, {"path": ".claude/skills/review-yaml-record/SKILL.md", "role": "context", "sha256": "493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae"}, {"path": "AGENTS.md", "role": "context", "sha256": "69e4037f8dc97d4b00bb7bb83b41ceca025f6ef578d5c0bf8086f3400becde0b"}, {"path": "conf/id_label_targets.yaml", "role": "context", "sha256": "24235903e0e8df5793a30e92c551082c71c1c67739ea4e3b5fb0f68853a805e6"}, {"path": "conf/producer_evidence.tsv", "role": "context", "sha256": "67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131"}, {"path": "conf/record_review.yaml", "role": "context", "sha256": "e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8"}, {"path": "curation/lotus_occurrence_exclusions.tsv", "role": "context", "sha256": "d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d"}, {"path": "curation/mibig_claim_references.tsv", "role": "context", "sha256": "bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029"}, {"path": "curation/mibig_locus_evidence_overrides.tsv", "role": "context", "sha256": "7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e"}, {"path": "curation/mibig_producer_isolates.tsv", "role": "context", "sha256": "8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8"}, {"path": "curation/mibig_producer_strains.tsv", "role": "context", "sha256": "bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae"}, {"path": "curation/mibig_structure_corrections.tsv", "role": "context", "sha256": "c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0"}, {"path": "curation/mibig_xref_exclusions.tsv", "role": "context", "sha256": "cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c"}, {"path": "data/natural_products/PATHS.tsv", "role": "context", "sha256": "2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3"}, {"path": "data/natural_products/terpenoids/lankacidin-c.yaml", "role": "target", "sha256": "efdee93632f199ca328314f66decb80dac20bee619b95f124158c22d299ee8a7"}, {"path": "data/raw/MANIFEST.yaml", "role": "context", "sha256": "b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3"}, {"path": "data/raw/antibioticmech_inchikeys.tsv", "role": "context", "sha256": "ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6"}, {"path": "data/raw/bindingdb_targets.tsv", "role": "context", "sha256": "3cff45281c35a8b14d4d7784bc4b7af80e8e27779a5667a0292f0d9b022a22c1"}, {"path": "data/raw/chebi_origins.tsv", "role": "context", "sha256": "fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8"}, {"path": "data/raw/chebi_structures.tsv", "role": "context", "sha256": "62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2"}, {"path": "data/raw/corpus_taxa.obo", "role": "context", "sha256": "8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9"}, {"path": "data/raw/cyanometdb_occurrences.tsv", "role": "context", "sha256": "f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8"}, {"path": "data/raw/lotus_occurrences.tsv", "role": "context", "sha256": "ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94"}, {"path": "data/raw/mibig_compounds.tsv", "role": "context", "sha256": "e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6"}, {"path": "data/raw/npclassifier.tsv", "role": "context", "sha256": "acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3"}, {"path": "data/raw/pubchem_bioassay.tsv", "role": "context", "sha256": "6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b"}, {"path": "docs/CURATION.md", "role": "context", "sha256": "c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa"}, {"path": "docs/HARMONIZATION.md", "role": "context", "sha256": "c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79"}, {"path": "docs/record-review-profile.md", "role": "context", "sha256": "1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a"}, {"path": "docs/record-reviews.md", "role": "context", "sha256": "452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b"}, {"path": "justfile", "role": "context", "sha256": "4f9057e3e54656dd46f2ded4d3a8f0804acad348d2605d436405e1fcfb6af550"}, {"path": "schema/record_review.yaml", "role": "context", "sha256": "229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb"}, {"path": "scripts/extract_chebi.py", "role": "context", "sha256": "46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f"}, {"path": "scripts/extract_mibig.py", "role": "context", "sha256": "e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c"}, {"path": "scripts/seed_from_sources.py", "role": "context", "sha256": "5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5"}, {"path": "src/naturalproductmech/curate/claim_references.py", "role": "context", "sha256": "0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3"}, {"path": "src/naturalproductmech/schema/naturalproductmech.yaml", "role": "context", "sha256": "9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d"}], "state": "working_tree"}, "/status": "inspection_only", "/targets": [{"kind": "generated", "label": "lankacidin C", "owner_paths": [{"path": "scripts/seed_from_sources.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained harmonization generator; seeded fields are corrected through maintained inputs and validated regeneration."}, {"path": "data/raw/mibig_compounds.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Retained MIBiG structure, producer and compound-specific locus assertions."}, {"path": "data/raw/npclassifier.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Pinned computed classification and filing assertions."}, {"path": "scripts/extract_mibig.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained extraction of MIBiG compound names, structures, stereochemistry flags and source provenance."}, {"path": "data/raw/lotus_occurrences.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Retained cited occurrence assertions, distinct from demonstrated production."}], "ownership_note": "This review proposes no record edit. Source corrections belong in maintained inventories, implemented curation tables, extractors or the seeder; generated pages are not owners.", "path": "data/natural_products/terpenoids/lankacidin-c.yaml", "record_class": "NaturalProductRecord", "target_id": "naturalproductmech:mibig-441a8c4d3f"}]} |
| support-2346-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-intake-native-acceptance-001.json; /status; /accepted; /verification | supports | ROOT accepts ten original canonical intakes, 387 source placements and 58 distinct paths; historical pre-chemistry wording is not an assertion that later results remain pending. |
| support-2346-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-source-inventory-acceptance-001.json; /status; /totals | supports | ROOT accepts the original local inventory; source meanings remain separately attributed. |
| support-2346-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-source-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepts the original input plan, not a scientific verdict. |
| support-2346-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /verification; /warning_scope; /stderr | supports | ROOT accepts twenty original stored parses and all100 stored-form comparison flags are true. Two undefined-stereo and two charge-rearrangement warnings remain global and unassigned. |
| support-2346-native-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-native-five-gates-acceptance-001.json; Whole saved actual native-result authority | supports | Five original local commands passed within their saved result scope; full QC and complete OAK authority coverage remain unavailable. |
| support-2346-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-execution-001.json; Whole original execution receipt | supports | ROOT operated the one accepted diagnostic. No replay, alternate parse or owner-specific warning attribution is introduced. |
| support-2346-plan | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-target-input-plan-001.json; /records/5; /source_placement_count; /unique_source_path_count | supports | Complete accepted owner input plan; cohort 387 placements /58 paths, this owner 37 placements. |
| support-2346-source-notes | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Joint complete source reading, exact raw/history carries and source-specific cautions; these notes precede scientific adjudication. |
| support-2346-curation-scope | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json; /curation | supports | ROOT performed the bounded1233-literal scan of eight directly opened implemented tables, including ignored files. Its sole taxon1931 rationale hit concerns unrelated BGC1648/lasalocid and cannot transfer strain FXJ1.172 to Marinoterpins. Reserved decisions.tsv was unconsumed; no global absence claim follows. |
| support-2346-source-routes | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/matched_chebi_ids; /contexts/9/source_scope_inventory/source_taxa; /contexts/9/source_scope_inventory/forward_taxon_merge_matches; /contexts/9/source_scope_inventory/nonorganism_matches; /contexts/9/source_scope_inventory/actual_assay_rows; /contexts/9/source_scope_inventory/blank_AID_sentinels; /contexts/9/source_scope_inventory/related_corpus_rows | supports | Complete saved route metadata, including assay/sentinel distinctions and exact empty routes. Exact copied saved values: {"/contexts/9/source_scope_inventory/actual_assay_rows": [], "/contexts/9/source_scope_inventory/blank_AID_sentinels": [], "/contexts/9/source_scope_inventory/forward_taxon_merge_matches": [], "/contexts/9/source_scope_inventory/matched_chebi_ids": [], "/contexts/9/source_scope_inventory/nonorganism_matches": [], "/contexts/9/source_scope_inventory/related_corpus_rows": [], "/contexts/9/source_scope_inventory/source_taxa": ["NCBITaxon:1928"]} |
| support-2346-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/2 | supports | All relevant saved cached stanzas, including exact forward-merge destinations; names and synonyms remain retained local authority. Exact copied saved values: {"/cached_taxonomy/whole_stanzas/2": {"complete_stanza": "[Term]\nid: NCBITaxon:1928\nname: Streptomyces rochei\nsynonym: \"Actinomyces rochei\" EXACT []\n\n", "id": "NCBITaxon:1928", "physical_line": 3059}} |
| support-2346-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, all matches and exact no-match scope; no replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/mibig_compounds": {"matches": [{"last_physical_line": 1279, "physical_line": 1279, "raw_tsv_record": "BGC0001100\t5\tactive\tquestionable\tunknown\tlankacidin C\t1\t[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C\tInChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1\tATDILMLBOZKFGI-JUTMVFGESA-N\ttrue\t\tnpatlas:NPA04098\tNCBITaxon:1928\tStreptomyces rochei\tNRPS&#124;PKS\tType I&#124;Unknown\tAB088224.2\t4922\t35881\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:12791134\tENTRY\n", "row": {"bgc_classes": "NRPS&#124;PKS", "bgc_subclasses": "Type I&#124;Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "lankacidin C", "database_ids": "npatlas:NPA04098", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "5", "genome_accession": "AB088224.2", "locus_evidence_methods": "", "locus_from": "4922", "locus_to": "35881", "mibig_accession": "BGC0001100", "primary_reference": "PMID:12791134", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C", "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei"}, "row_sha256": "eb0b51dfc88f486d625d176c8ec13a99ffc97bc89f087c650bf2629d708541e6"}], "predicate": "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}} |
| support-2346-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 1279–1279, row_sha256 eb0b51dfc88f486d625d176c8ec13a99ffc97bc89f087c650bf2629d708541e6 | supports | Complete retained physical row fields: [{"bgc_classes": "NRPS&#124;PKS", "bgc_subclasses": "Type I&#124;Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "lankacidin C", "database_ids": "npatlas:NPA04098", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "5", "genome_accession": "AB088224.2", "locus_evidence_methods": "", "locus_from": "4922", "locus_to": "35881", "mibig_accession": "BGC0001100", "primary_reference": "PMID:12791134", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C", "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei"}] |
| support-2346-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, all matches and exact no-match scope; no replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/chebi_structures": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}} |
| support-2346-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, all matches and exact no-match scope; no replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/lotus_occurrences": {"matches": [{"last_physical_line": 334, "physical_line": 334, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1002/CBIC.201500393\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1002/CBIC.201500393", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "421ddcebcf641feed50c8b8e468cfc765c46aa5a9fd86732dd67d4e419781235"}, {"last_physical_line": 335, "physical_line": 335, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1016/J.JBIOSC.2018.03.006\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1016/J.JBIOSC.2018.03.006", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "f4ac8c36c460efad8cc99e186d4ef0d5703c2b38a0df02536b0e963ffac912af"}, {"last_physical_line": 336, "physical_line": 336, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1016/J.TET.2011.05.047\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1016/J.TET.2011.05.047", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "d539b92e9cedbae1975ed54fa957aa0e4a2b4ef66fd3c1631206350cd6b9e6e2"}, {"last_physical_line": 337, "physical_line": 337, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1016/S0378-1119(00)00060-3\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1016/S0378-1119(00)00060-3", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "c3908faf90e3409a400531614b4c432865c4fd32c17073137e2cf53d9fce121a"}, {"last_physical_line": 338, "physical_line": 338, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1038/JA.2010.146\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1038/JA.2010.146", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "30212f6da52512e9100109638280f1148f69a0b8f3cc3dfccd2e89c1cbae6bf4"}, {"last_physical_line": 339, "physical_line": 339, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1038/S41598-019-47406-Y\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1038/S41598-019-47406-Y", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "58df0e7bde807569d53228603db6a4bc94c0edc82c101f339b9540cce74cdab3"}, {"last_physical_line": 340, "physical_line": 340, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1046/J.1365-2958.2003.03523.X\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1046/J.1365-2958.2003.03523.X", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "291ce111c50cfcc970e4d47b9047671cb968498a97d626809325898713de0ef2"}, {"last_physical_line": 341, "physical_line": 341, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1080/09168451.2014.882761\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1080/09168451.2014.882761", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "181aad803ce0d2cce84e93cab53db7bd90bb72904f11e80d101c3db2f27cf46a"}, {"last_physical_line": 342, "physical_line": 342, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1128/JB.01383-07\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1128/JB.01383-07", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "ebb79e24785f90c99fb0c7aaedb1c271b1b5368ec2a2d6491e918f678cc147e9"}, {"last_physical_line": 343, "physical_line": 343, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1271/BBB.90591\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1271/BBB.90591", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "0edda1c8eac54e3e16a8bb53707b5afc595c64ec0f742d0a7a0c36c2790a88fe"}, {"last_physical_line": 344, "physical_line": 344, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.7164/ANTIBIOTICS.26.647\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.7164/ANTIBIOTICS.26.647", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "77c5e0b981712406ec60ffdc64ad53e8723bee3fedd6bc5b33f1b12f5be9fba2"}, {"last_physical_line": 345, "physical_line": 345, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.7164/ANTIBIOTICS.47.1447\thttp://www.wikidata.org/entity/Q27149238\n", "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.7164/ANTIBIOTICS.47.1447", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, "row_sha256": "a9d4a7ddc2482ea090b446e81d630300237ccd53cac7b9aee797677cdd6db396"}], "predicate": "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}} |
| support-2346-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 334–334, row_sha256 421ddcebcf641feed50c8b8e468cfc765c46aa5a9fd86732dd67d4e419781235; physical lines 335–335, row_sha256 f4ac8c36c460efad8cc99e186d4ef0d5703c2b38a0df02536b0e963ffac912af; physical lines 336–336, row_sha256 d539b92e9cedbae1975ed54fa957aa0e4a2b4ef66fd3c1631206350cd6b9e6e2; physical lines 337–337, row_sha256 c3908faf90e3409a400531614b4c432865c4fd32c17073137e2cf53d9fce121a; physical lines 338–338, row_sha256 30212f6da52512e9100109638280f1148f69a0b8f3cc3dfccd2e89c1cbae6bf4; physical lines 339–339, row_sha256 58df0e7bde807569d53228603db6a4bc94c0edc82c101f339b9540cce74cdab3; physical lines 340–340, row_sha256 291ce111c50cfcc970e4d47b9047671cb968498a97d626809325898713de0ef2; physical lines 341–341, row_sha256 181aad803ce0d2cce84e93cab53db7bd90bb72904f11e80d101c3db2f27cf46a; physical lines 342–342, row_sha256 ebb79e24785f90c99fb0c7aaedb1c271b1b5368ec2a2d6491e918f678cc147e9; physical lines 343–343, row_sha256 0edda1c8eac54e3e16a8bb53707b5afc595c64ec0f742d0a7a0c36c2790a88fe; physical lines 344–344, row_sha256 77c5e0b981712406ec60ffdc64ad53e8723bee3fedd6bc5b33f1b12f5be9fba2; physical lines 345–345, row_sha256 a9d4a7ddc2482ea090b446e81d630300237ccd53cac7b9aee797677cdd6db396 | supports | Complete retained physical row fields: [{"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1002/CBIC.201500393", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1016/J.JBIOSC.2018.03.006", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1016/J.TET.2011.05.047", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1016/S0378-1119(00)00060-3", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1038/JA.2010.146", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1038/S41598-019-47406-Y", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1046/J.1365-2958.2003.03523.X", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1080/09168451.2014.882761", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1128/JB.01383-07", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1271/BBB.90591", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.7164/ANTIBIOTICS.26.647", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.7164/ANTIBIOTICS.47.1447", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id": "NCBITaxon:1928"}] |
| support-2346-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, all matches and exact no-match scope; no replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/cyanometdb_occurrences": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}} |
| support-2346-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, all matches and exact no-match scope; no replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/npclassifier": {"matches": [{"last_physical_line": 98, "physical_line": 98, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\t[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C\tTerpenoids\tDiterpenoids\tCembrane diterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results": "Cembrane diterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "superclass_results": "Diterpenoids"}, "row_sha256": "d5a5f3e07b33c0e790c1eff9aab7b42cf54f0521ccd1caf00551ca2dad7e2a9f"}], "predicate": "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}} |
| support-2346-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 98–98, row_sha256 d5a5f3e07b33c0e790c1eff9aab7b42cf54f0521ccd1caf00551ca2dad7e2a9f | supports | Complete retained physical row fields: [{"class_results": "Cembrane diterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "superclass_results": "Diterpenoids"}] |
| support-2346-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, all matches and exact no-match scope; no replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/pubchem_bioassay": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}} |
| support-2346-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, all matches and exact no-match scope; no replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/bindingdb_targets": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}} |
| support-2346-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, all matches and exact no-match scope; no replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}} |
| support-2346-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, all matches and exact no-match scope; no replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/chebi_origins": {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows", "query": []}} |
| support-2346-direct-contexts | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /records/5/direct_companion_paths; /records/5/direct_companion_predicates | supports | Exact direct companion scope; a shared locus is not identity or transferred evidence. Exact copied saved values: {"/records/5/direct_companion_paths": [], "/records/5/direct_companion_predicates": []} |
| support-2346-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /records/5/direct_companion_paths | supports | Complete source and raw/history carries are explicitly attributed in source notes. Distinct companion metadata: [] |
| support-2346-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 175–200; lines 368–435 | supports | Schema separates stored structures, partial stereo and versioned computed classification from asserted identity. |
| support-2346-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 145–174 | supports | The source stereo_complete predicate uses unassigned tetrahedral centres in source SMILES, not every normalized tautomer or natural stereochemical proof. |
| support-2346-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 296–307; lines 982–1020 | supports | Maintained seeder retains source structure and all versioned model arrays; no regeneration was run. |
| support-2346-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | Twelve scientific dimensions and partial completion reflect actual access and check limits. |
| support-2346-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill under the absolute no-outbound instruction | supports | Read-only review, maintained ownership and no native-status promotion apply; no external lookup authorized. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-235/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-235/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-235/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-235/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-235/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. No external publication, identifier, taxonomy, protein sequence or natural stereochemical assertion was refreshed under the absolute no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original gates, stored-form parsing and maintained-reader preservation establish only their stated scope.
- Exact empty joins are bounded by saved predicates/snapshots; shared loci, names, taxa or citations do not transfer identity, production, activity or mechanism.
- Two original undefined-stereo and two charge-rearrangement warnings remain global and unassigned. No additional molecular/YAML parse, source query or target invocation occurred during scientific authoring.
- No source record or native status/history is edited. Computed model concerns do not automatically establish a maintained-source defect.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read all five complete raw owners/history, actual intakes and the disjoint source partition; exact prior companion carries and BGC/Native complementary readings remain attributed in the joint notes.
- Support personally read all ten saved forms: 312 atom and 338 bond rows, every scalar/ring/stereo/motif/map (a98425, da0f1d, d898a7, dc945f). The original correspondence limits are preserved; no new graph computation or molecular parse.
- ROOT operated activation/capture, inventory/composer, canonical intakes and the diagnostic. Native operated original gates and maintained reader under ROOT authorization; ROOT separately accepted results. Scientific authoring invoked none of these targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T050441Z-lankacidin-c
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: lankacidin C'
started_at: '2026-11-04T04:24:34.142593Z'
finished_at: '2026-11-04T05:04:41.492110Z'
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
summary: Lankacidin C preserves matching, fully specified stored molecular forms and
  separately scoped Streptomyces rochei producer and occurrence assertions. The retained
  NRPS/PKS locus class and oxygenated nitrogen-bearing macrocycle make the computed
  Cembrane diterpenoid filing an applicability concern. No maintained-source defect
  is established by that prediction alone.
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
  - path: data/natural_products/terpenoids/lankacidin-c.yaml
    sha256: efdee93632f199ca328314f66decb80dac20bee619b95f124158c22d299ee8a7
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
  selection: Campaign path order 2346; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-441a8c4d3f
targets:
- target_id: naturalproductmech:mibig-441a8c4d3f
  path: data/natural_products/terpenoids/lankacidin-c.yaml
  label: lankacidin C
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
  - naturalproductmech:mibig-441a8c4d3f
  command: just validate-strict data/natural_products/terpenoids/jerangolid-d.yaml
    data/natural_products/terpenoids/juniperol-longiborneol.yaml data/natural_products/terpenoids/kainic-acid-lactone.yaml
    data/natural_products/terpenoids/koraiol.yaml data/natural_products/terpenoids/ks-505a.yaml
    data/natural_products/terpenoids/lankacidin-c.yaml data/natural_products/terpenoids/lupeol.yaml
    data/natural_products/terpenoids/lycosantalonol.yaml data/natural_products/terpenoids/mangicol-a.yaml
    data/natural_products/terpenoids/marinoterpin-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-235/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-441a8c4d3f
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-235/validate-all-001.tsv
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
  - naturalproductmech:mibig-441a8c4d3f
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
  - naturalproductmech:mibig-441a8c4d3f
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
  - naturalproductmech:mibig-441a8c4d3f
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-235/review-queue-001.tsv
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
  - naturalproductmech:mibig-441a8c4d3f
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-441a8c4d3f
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-441a8c4d3f
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2346-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/lankacidin-c.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: Complete owner and all 3 history events are covered by current exact whole-reading
    attribution. Native status remains SEEDED.
  snapshot_sha256: efdee93632f199ca328314f66decb80dac20bee619b95f124158c22d299ee8a7
- evidence_id: support-2346-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/5
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete original captured owner and exact mechanism/component presence,
    distinct from maintained resolution. Exact copied saved values: {"/records/5":
    {"component_captures": [], "mechanism_capture_scope": "raw_owner_and_declared_components_only_not_maintained_resolution",
    "order": 2346, "owner_document": {"bgc_class": ["NRPS", "PKS"], "biosynthesis_origin":
    "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001100",
    "bgc_class": ["NRPS", "PKS"], "entry_status": "active", "entry_version": "5",
    "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100
    entry version 5; citation taken from the entry level", "reference": "PMID:12791134"}],
    "genome_accession": "genbank:AB088224.2", "link_evidence_basis": "CLUSTER_UNSTATED",
    "locus_from": 4922, "locus_to": 35881, "organism_label": "Streptomyces rochei",
    "organism_taxon_id": "NCBITaxon:1928"}], "chemical_structure": {"smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C",
    "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001100"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:03Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:01:28Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    and curation tables.", "curator": "seed_from_sources", "timestamp": "2026-10-13T10:42:36Z"}],
    "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares
    this structure, so the record keeps a content-hashed identifier.", "grounding_status":
    "MINTED", "identifier": "naturalproductmech:mibig-441a8c4d3f", "label": "lankacidin
    C", "np_classification": {"class_results": ["Cembrane diterpenoids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Diterpenoids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["ACTINOBACTERIAL"], "occurrences":
    [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1002/CBIC.201500393"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon
    is also recorded as a producer. Production and occurrence are distinct claims;
    their citations may refer to the same publication. Publication independence has
    not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1016/J.JBIOSC.2018.03.006"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1016/J.TET.2011.05.047"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1016/S0378-1119(00)00060-3"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/JA.2010.146"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1038/S41598-019-47406-Y"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1046/J.1365-2958.2003.03523.X"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer.
    Production and occurrence are distinct claims; their citations may refer to the
    same publication. Publication independence has not been established.", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source":
    "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1080/09168451.2014.882761"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1128/JB.01383-07"}], "notes": "Wikidata
    organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded
    as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1271/BBB.90591"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.26.647"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.7164/ANTIBIOTICS.47.1447"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer.
    Production and occurrence are distinct claims; their citations may refer to the
    same publication. Publication independence has not been established.", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source":
    "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001100",
    "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100
    entry version 5; citation taken from the entry level", "reference": "PMID:12791134"}],
    "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That
    evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim,
    which is a different question.", "source": "MIBIG", "source_version": "5", "taxon_id":
    "NCBITaxon:1928", "taxon_label": "Streptomyces rochei"}], "producer_taxon_groups":
    ["ACTINOBACTERIAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-441a8c4d3f",
    "source": "MIBIG", "source_id": "BGC0001100", "source_label": "lankacidin C",
    "source_version": "5"}], "xrefs": ["npatlas:NPA04098"]}, "owner_pin": {"bytes":
    10540, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/lankacidin-c.yaml",
    "sha256": "efdee93632f199ca328314f66decb80dac20bee619b95f124158c22d299ee8a7"},
    "path": "data/natural_products/terpenoids/lankacidin-c.yaml", "read_finished_at":
    "2026-11-04T04:24:34.146914Z", "read_started_at": "2026-11-04T04:24:34.142593Z"}}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: support-2346-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/5/owner_document/identifier; /records/5/owner_document/label;
    /records/5/owner_document/chemical_structure; /records/5/owner_document/grounding_status;
    /records/5/owner_document/grounding_notes; /records/5/owner_document/source_concepts;
    /records/5/owner_document/xrefs
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Exact identity, source definition and grounding fields, including unresolved
    discussion where present. Exact copied saved values: {"/records/5/owner_document/chemical_structure":
    {"smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C",
    "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001100"}, "/records/5/owner_document/grounding_notes":
    "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.", "/records/5/owner_document/grounding_status": "MINTED", "/records/5/owner_document/identifier":
    "naturalproductmech:mibig-441a8c4d3f", "/records/5/owner_document/label": "lankacidin
    C", "/records/5/owner_document/source_concepts": [{"minted_identifier": "naturalproductmech:mibig-441a8c4d3f",
    "source": "MIBIG", "source_id": "BGC0001100", "source_label": "lankacidin C",
    "source_version": "5"}], "/records/5/owner_document/xrefs": ["npatlas:NPA04098"]}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: support-2346-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/5/owner_document/producer_organisms; /records/5/owner_document/biosynthetic_gene_clusters;
    /records/5/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Separately graded producer and locus source assertions. Exact copied saved
    values: {"/records/5/owner_document/biosynthetic_gene_clusters": [{"accession":
    "mibig:BGC0001100", "bgc_class": ["NRPS", "PKS"], "entry_status": "active", "entry_version":
    "5", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100
    entry version 5; citation taken from the entry level", "reference": "PMID:12791134"}],
    "genome_accession": "genbank:AB088224.2", "link_evidence_basis": "CLUSTER_UNSTATED",
    "locus_from": 4922, "locus_to": 35881, "organism_label": "Streptomyces rochei",
    "organism_taxon_id": "NCBITaxon:1928"}], "/records/5/owner_document/producer_organisms":
    [{"biosynthetic_gene_cluster": "mibig:BGC0001100", "evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100 entry version 5; citation taken
    from the entry level", "reference": "PMID:12791134"}], "evidence_basis": "SOURCE_ASSERTION",
    "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED;
    this field grades the taxon claim, which is a different question.", "source":
    "MIBIG", "source_version": "5", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei"}], "/records/5/owner_document/producer_taxon_groups": ["ACTINOBACTERIAL"]}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: support-2346-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/5/owner_document/occurrences; /records/5/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Written occurrence placements and retained further-row notes. Exact copied
    saved values: {"/records/5/owner_document/occurrence_taxon_groups": ["ACTINOBACTERIAL"],
    "/records/5/owner_document/occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1002/CBIC.201500393"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1016/J.JBIOSC.2018.03.006"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1016/J.TET.2011.05.047"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1016/S0378-1119(00)00060-3"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/JA.2010.146"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1038/S41598-019-47406-Y"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1046/J.1365-2958.2003.03523.X"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer.
    Production and occurrence are distinct claims; their citations may refer to the
    same publication. Publication independence has not been established.", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source":
    "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1080/09168451.2014.882761"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1128/JB.01383-07"}], "notes": "Wikidata
    organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded
    as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1271/BBB.90591"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.26.647"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.7164/ANTIBIOTICS.47.1447"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer.
    Production and occurrence are distinct claims; their citations may refer to the
    same publication. Publication independence has not been established.", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source":
    "NCBITaxon"}]}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: support-2346-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/5/owner_document
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Written observations; whole-owner selector establishes optional-root absence
    within this owner only. Exact copied saved values: {"/records/5/owner_document":
    {"bgc_class": ["NRPS", "PKS"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters":
    [{"accession": "mibig:BGC0001100", "bgc_class": ["NRPS", "PKS"], "entry_status":
    "active", "entry_version": "5", "evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "MIBiG BGC0001100 entry version 5; citation taken from the entry level",
    "reference": "PMID:12791134"}], "genome_accession": "genbank:AB088224.2", "link_evidence_basis":
    "CLUSTER_UNSTATED", "locus_from": 4922, "locus_to": 35881, "organism_label": "Streptomyces
    rochei", "organism_taxon_id": "NCBITaxon:1928"}], "chemical_structure": {"smiles":
    "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C",
    "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001100"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:03Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:01:28Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    and curation tables.", "curator": "seed_from_sources", "timestamp": "2026-10-13T10:42:36Z"}],
    "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares
    this structure, so the record keeps a content-hashed identifier.", "grounding_status":
    "MINTED", "identifier": "naturalproductmech:mibig-441a8c4d3f", "label": "lankacidin
    C", "np_classification": {"class_results": ["Cembrane diterpenoids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Diterpenoids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["ACTINOBACTERIAL"], "occurrences":
    [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1002/CBIC.201500393"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon
    is also recorded as a producer. Production and occurrence are distinct claims;
    their citations may refer to the same publication. Publication independence has
    not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1016/J.JBIOSC.2018.03.006"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1016/J.TET.2011.05.047"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1016/S0378-1119(00)00060-3"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1038/JA.2010.146"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1038/S41598-019-47406-Y"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1046/J.1365-2958.2003.03523.X"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer.
    Production and occurrence are distinct claims; their citations may refer to the
    same publication. Publication independence has not been established.", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source":
    "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1080/09168451.2014.882761"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.1128/JB.01383-07"}], "notes": "Wikidata
    organism http://www.wikidata.org/entity/Q26292213 This taxon is also recorded
    as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1271/BBB.90591"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q26292213
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label":
    "Streptomyces rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS
    reports that the compound was found in the organism; it does not assert that the
    organism produces it.", "reference": "DOI:10.7164/ANTIBIOTICS.26.647"}], "notes":
    "Wikidata organism http://www.wikidata.org/entity/Q26292213 This taxon is also
    recorded as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.",
    "source": "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces
    rochei", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.7164/ANTIBIOTICS.47.1447"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q26292213 This taxon is also recorded as a producer.
    Production and occurrence are distinct claims; their citations may refer to the
    same publication. Publication independence has not been established.", "source":
    "LOTUS", "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei", "taxon_source":
    "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001100",
    "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001100
    entry version 5; citation taken from the entry level", "reference": "PMID:12791134"}],
    "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That
    evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim,
    which is a different question.", "source": "MIBIG", "source_version": "5", "taxon_id":
    "NCBITaxon:1928", "taxon_label": "Streptomyces rochei"}], "producer_taxon_groups":
    ["ACTINOBACTERIAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-441a8c4d3f",
    "source": "MIBIG", "source_id": "BGC0001100", "source_label": "lankacidin C",
    "source_version": "5"}], "xrefs": ["npatlas:NPA04098"]}}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: support-2346-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/5/owner_document/np_pathway; /records/5/owner_document/np_classification;
    /records/5/owner_document/bgc_class
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Versioned computed filing and separately asserted BGC/compound classes.
    Exact copied saved values: {"/records/5/owner_document/bgc_class": ["NRPS", "PKS"],
    "/records/5/owner_document/np_classification": {"class_results": ["Cembrane diterpenoids"],
    "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results":
    ["Diterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "/records/5/owner_document/np_pathway": "TERPENOIDS"}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: support-2346-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/comparisons; /records/5/atom_correspondence
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete original declared forms/comparisons/map, unchanged. Exact copied
    saved values: {"/records/5/atom_correspondence": {"complete_atom_count_match":
    true, "full_graph_identity_established": false, "scope": "One chirality-aware
    substructure match; no independent full graph or natural identity claim.", "smiles_to_inchi_atom_indices":
    [19, 12, 18, 28, 10, 6, 13, 0, 5, 8, 17, 27, 9, 7, 14, 1, 11, 20, 25, 22, 30,
    16, 3, 26, 24, 4, 23, 31, 32, 21, 29, 15, 2]}, "/records/5/comparisons": {"atom_count_equal":
    true, "bond_count_equal": true, "both_keys_equal_declared": true, "canonical_isomeric_smiles_equal":
    true, "canonical_nonisomeric_smiles_equal": true, "formal_charge_equal": true,
    "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer": true,
    "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "/records/5/declared_structure":
    {"smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C",
    "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001100"}}'
  snapshot_sha256: aeff6d2db3c52b75fa7cd85438a014925445302087c33263b7522f3f556e0d4c
- evidence_id: support-2346-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/smiles/computed; /records/5/inchi/computed; /records/5/declared_structure;
    /records/5/comparisons; /records/5/atom_correspondence
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: Both complete saved forms are neutral C25H33NO7, with 33 heavy atoms, 34
    bonds and one connected component. They retain a carbon macrocycle, an integrated
    six-membered lactone, two hydroxyls, a ring ketone and an acylamide side chain
    containing another ketone. The saved ring list includes alternate cycles and must
    not be interpreted as three independent rings. Six tetrahedral centres and four
    E alkenes are specified in both forms. The amide remains C19(=O20)-N18 in the
    SMILES table and C22(=O30)-N25 in the InChI-derived table; the mobile-H InChI
    layer has not produced a different fixed tautomer in this original diagnostic.
    All ten comparison flags are true. The recorded chirality-aware correspondence
    covers 33 atoms while full_graph_identity_established remains false; local Cis/Trans
    potential-stereo descriptors depend on atom ordering and do not contradict the
    aligned E bond labels. Stored completeness is not fresh experimental stereochemical
    proof.
  snapshot_sha256: aeff6d2db3c52b75fa7cd85438a014925445302087c33263b7522f3f556e0d4c
- evidence_id: support-2346-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/intakes/2346-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T04:54:20.560210Z'
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
    {"path": "data/natural_products/terpenoids/lankacidin-c.yaml", "role": "target",
    "sha256": "efdee93632f199ca328314f66decb80dac20bee619b95f124158c22d299ee8a7"},
    {"path": "data/raw/MANIFEST.yaml", "role": "context", "sha256": "b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3"},
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
    {"path": "src/naturalproductmech/schema/naturalproductmech.yaml", "role": "context",
    "sha256": "9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d"}],
    "state": "working_tree"}, "/status": "inspection_only", "/targets": [{"kind":
    "generated", "label": "lankacidin C", "owner_paths": [{"path": "scripts/seed_from_sources.py",
    "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained harmonization
    generator; seeded fields are corrected through maintained inputs and validated
    regeneration."}, {"path": "data/raw/mibig_compounds.tsv", "repository": "CultureBotAI/NaturalProductMech",
    "role": "Retained MIBiG structure, producer and compound-specific locus assertions."},
    {"path": "data/raw/npclassifier.tsv", "repository": "CultureBotAI/NaturalProductMech",
    "role": "Pinned computed classification and filing assertions."}, {"path": "scripts/extract_mibig.py",
    "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained extraction
    of MIBiG compound names, structures, stereochemistry flags and source provenance."},
    {"path": "data/raw/lotus_occurrences.tsv", "repository": "CultureBotAI/NaturalProductMech",
    "role": "Retained cited occurrence assertions, distinct from demonstrated production."}],
    "ownership_note": "This review proposes no record edit. Source corrections belong
    in maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners.", "path": "data/natural_products/terpenoids/lankacidin-c.yaml",
    "record_class": "NaturalProductRecord", "target_id": "naturalproductmech:mibig-441a8c4d3f"}]}'
  snapshot_sha256: 94eeabc1814e039cdbb40009931396be1eb22cc6ae417b3df2dd462d02c76f84
- evidence_id: support-2346-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-intake-native-acceptance-001.json
  locator: /status; /accepted; /verification
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: ROOT accepts ten original canonical intakes, 387 source placements and
    58 distinct paths; historical pre-chemistry wording is not an assertion that later
    results remain pending.
  snapshot_sha256: 97b8f40e4ce5c08c4508e916b5951f267a4aba333bf78abf8275d7c8c865e7f0
- evidence_id: support-2346-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-source-inventory-acceptance-001.json
  locator: /status; /totals
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: ROOT accepts the original local inventory; source meanings remain separately
    attributed.
  snapshot_sha256: efe55c8fc90acc75742e2e133be3d52885ba31a8027a7ef4736e7bc020950af9
- evidence_id: support-2346-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-source-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: ROOT accepts the original input plan, not a scientific verdict.
  snapshot_sha256: ebd812deb22f4b63b07c62f2cfb77b5ccaefd41fa85e5da34e9ad033ab96431c
- evidence_id: support-2346-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /verification; /warning_scope; /stderr
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: ROOT accepts twenty original stored parses and all100 stored-form comparison
    flags are true. Two undefined-stereo and two charge-rearrangement warnings remain
    global and unassigned.
  snapshot_sha256: 5c7d1831ae5c8d9ffdafa16a84aaf306a7641eec7b63ed29999a7182721156f6
- evidence_id: support-2346-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-native-five-gates-acceptance-001.json
  locator: Whole saved actual native-result authority
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: Five original local commands passed within their saved result scope; full
    QC and complete OAK authority coverage remain unavailable.
  snapshot_sha256: 713d96670fed493630776183217dec028aa27c64ca70142c925e14679e8064bc
- evidence_id: support-2346-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: ROOT operated the one accepted diagnostic. No replay, alternate parse or
    owner-specific warning attribution is introduced.
  snapshot_sha256: c6f0da32c1be702c997e92c5892ea02e38a069abc6c0b720fa4e1338b674661c
- evidence_id: support-2346-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-target-input-plan-001.json
  locator: /records/5; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: Complete accepted owner input plan; cohort 387 placements /58 paths, this
    owner 37 placements.
  snapshot_sha256: 4534eaf8666f0c106f388a2d17af4dc6b1edc20f665e7aef9a03813706c19ddb
- evidence_id: support-2346-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: Joint complete source reading, exact raw/history carries and source-specific
    cautions; these notes precede scientific adjudication.
  snapshot_sha256: 8c85f257f59a062eabc086ac4dd94acabd196bf072e6d66aa20f1215dd31aaa7
- evidence_id: support-2346-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: ROOT performed the bounded1233-literal scan of eight directly opened implemented
    tables, including ignored files. Its sole taxon1931 rationale hit concerns unrelated
    BGC1648/lasalocid and cannot transfer strain FXJ1.172 to Marinoterpins. Reserved
    decisions.tsv was unconsumed; no global absence claim follows.
  snapshot_sha256: 8c85f257f59a062eabc086ac4dd94acabd196bf072e6d66aa20f1215dd31aaa7
- evidence_id: support-2346-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/matched_chebi_ids; /contexts/9/source_scope_inventory/source_taxa;
    /contexts/9/source_scope_inventory/forward_taxon_merge_matches; /contexts/9/source_scope_inventory/nonorganism_matches;
    /contexts/9/source_scope_inventory/actual_assay_rows; /contexts/9/source_scope_inventory/blank_AID_sentinels;
    /contexts/9/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete saved route metadata, including assay/sentinel distinctions and
    exact empty routes. Exact copied saved values: {"/contexts/9/source_scope_inventory/actual_assay_rows":
    [], "/contexts/9/source_scope_inventory/blank_AID_sentinels": [], "/contexts/9/source_scope_inventory/forward_taxon_merge_matches":
    [], "/contexts/9/source_scope_inventory/matched_chebi_ids": [], "/contexts/9/source_scope_inventory/nonorganism_matches":
    [], "/contexts/9/source_scope_inventory/related_corpus_rows": [], "/contexts/9/source_scope_inventory/source_taxa":
    ["NCBITaxon:1928"]}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/2
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'All relevant saved cached stanzas, including exact forward-merge destinations;
    names and synonyms remain retained local authority. Exact copied saved values:
    {"/cached_taxonomy/whole_stanzas/2": {"complete_stanza": "[Term]\nid: NCBITaxon:1928\nname:
    Streptomyces rochei\nsynonym: \"Actinomyces rochei\" EXACT []\n\n", "id": "NCBITaxon:1928",
    "physical_line": 3059}}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match scope; no
    replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/mibig_compounds":
    {"matches": [{"last_physical_line": 1279, "physical_line": 1279, "raw_tsv_record":
    "BGC0001100\t5\tactive\tquestionable\tunknown\tlankacidin C\t1\t[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C\tInChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1\tATDILMLBOZKFGI-JUTMVFGESA-N\ttrue\t\tnpatlas:NPA04098\tNCBITaxon:1928\tStreptomyces
    rochei\tNRPS|PKS\tType I|Unknown\tAB088224.2\t4922\t35881\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:12791134\tENTRY\n",
    "row": {"bgc_classes": "NRPS|PKS", "bgc_subclasses": "Type I|Unknown", "cluster_link_evidence_basis":
    "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name":
    "lankacidin C", "database_ids": "npatlas:NPA04098", "entry_completeness": "unknown",
    "entry_quality": "questionable", "entry_status": "active", "entry_version": "5",
    "genome_accession": "AB088224.2", "locus_evidence_methods": "", "locus_from":
    "4922", "locus_to": "35881", "mibig_accession": "BGC0001100", "primary_reference":
    "PMID:12791134", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis":
    "ENTRY", "smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C",
    "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei"}, "row_sha256":
    "eb0b51dfc88f486d625d176c8ec13a99ffc97bc89f087c650bf2629d708541e6"}], "predicate":
    "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 1279–1279, row_sha256 eb0b51dfc88f486d625d176c8ec13a99ffc97bc89f087c650bf2629d708541e6
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"bgc_classes": "NRPS|PKS", "bgc_subclasses":
    "Type I|Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes":
    "", "compound_index": "1", "compound_name": "lankacidin C", "database_ids": "npatlas:NPA04098",
    "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status":
    "active", "entry_version": "5", "genome_accession": "AB088224.2", "locus_evidence_methods":
    "", "locus_from": "4922", "locus_to": "35881", "mibig_accession": "BGC0001100",
    "primary_reference": "PMID:12791134", "producer_evidence_basis": "SOURCE_ASSERTION",
    "reference_basis": "ENTRY", "smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C",
    "standard_inchi": "InChI=1S/C25H33NO7/c1-14-6-9-18(28)10-8-15(2)12-21(26-23(31)17(4)27)25(5)22(30)16(3)20(33-24(25)32)13-19(29)11-7-14/h6-8,10-12,16,18-21,28-29H,9,13H2,1-5H3,(H,26,31)/b10-8+,11-7+,14-6+,15-12+/t16-,18+,19-,20-,21-,25+/m1/s1",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:1928", "taxon_label": "Streptomyces rochei"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2346-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match scope; no
    replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/chebi_structures":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "ATDILMLBOZKFGI-JUTMVFGESA-N"}}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match scope; no
    replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/lotus_occurrences":
    {"matches": [{"last_physical_line": 334, "physical_line": 334, "raw_tsv_record":
    "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1002/CBIC.201500393\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.1002/CBIC.201500393", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "421ddcebcf641feed50c8b8e468cfc765c46aa5a9fd86732dd67d4e419781235"},
    {"last_physical_line": 335, "physical_line": 335, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1016/J.JBIOSC.2018.03.006\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.1016/J.JBIOSC.2018.03.006", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "f4ac8c36c460efad8cc99e186d4ef0d5703c2b38a0df02536b0e963ffac912af"},
    {"last_physical_line": 336, "physical_line": 336, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1016/J.TET.2011.05.047\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.1016/J.TET.2011.05.047", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "d539b92e9cedbae1975ed54fa957aa0e4a2b4ef66fd3c1631206350cd6b9e6e2"},
    {"last_physical_line": 337, "physical_line": 337, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1016/S0378-1119(00)00060-3\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.1016/S0378-1119(00)00060-3", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "c3908faf90e3409a400531614b4c432865c4fd32c17073137e2cf53d9fce121a"},
    {"last_physical_line": 338, "physical_line": 338, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1038/JA.2010.146\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.1038/JA.2010.146", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "30212f6da52512e9100109638280f1148f69a0b8f3cc3dfccd2e89c1cbae6bf4"},
    {"last_physical_line": 339, "physical_line": 339, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1038/S41598-019-47406-Y\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.1038/S41598-019-47406-Y", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "58df0e7bde807569d53228603db6a4bc94c0edc82c101f339b9540cce74cdab3"},
    {"last_physical_line": 340, "physical_line": 340, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1046/J.1365-2958.2003.03523.X\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.1046/J.1365-2958.2003.03523.X", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "291ce111c50cfcc970e4d47b9047671cb968498a97d626809325898713de0ef2"},
    {"last_physical_line": 341, "physical_line": 341, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1080/09168451.2014.882761\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.1080/09168451.2014.882761", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "181aad803ce0d2cce84e93cab53db7bd90bb72904f11e80d101c3db2f27cf46a"},
    {"last_physical_line": 342, "physical_line": 342, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1128/JB.01383-07\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.1128/JB.01383-07", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "ebb79e24785f90c99fb0c7aaedb1c271b1b5368ec2a2d6491e918f678cc147e9"},
    {"last_physical_line": 343, "physical_line": 343, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.1271/BBB.90591\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.1271/BBB.90591", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "0edda1c8eac54e3e16a8bb53707b5afc595c64ec0f742d0a7a0c36c2790a88fe"},
    {"last_physical_line": 344, "physical_line": 344, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.7164/ANTIBIOTICS.26.647\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.7164/ANTIBIOTICS.26.647", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "77c5e0b981712406ec60ffdc64ad53e8723bee3fedd6bc5b33f1b12f5be9fba2"},
    {"last_physical_line": 345, "physical_line": 345, "raw_tsv_record": "ATDILMLBOZKFGI-JUTMVFGESA-N\tStreptomyces
    rochei\tNCBITaxon:1928\thttp://www.wikidata.org/entity/Q26292213\t10.7164/ANTIBIOTICS.47.1447\thttp://www.wikidata.org/entity/Q27149238\n",
    "row": {"organism_name": "Streptomyces rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213",
    "reference_doi": "10.7164/ANTIBIOTICS.47.1447", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, "row_sha256": "a9d4a7ddc2482ea090b446e81d630300237ccd53cac7b9aee797677cdd6db396"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 334–334, row_sha256 421ddcebcf641feed50c8b8e468cfc765c46aa5a9fd86732dd67d4e419781235;
    physical lines 335–335, row_sha256 f4ac8c36c460efad8cc99e186d4ef0d5703c2b38a0df02536b0e963ffac912af;
    physical lines 336–336, row_sha256 d539b92e9cedbae1975ed54fa957aa0e4a2b4ef66fd3c1631206350cd6b9e6e2;
    physical lines 337–337, row_sha256 c3908faf90e3409a400531614b4c432865c4fd32c17073137e2cf53d9fce121a;
    physical lines 338–338, row_sha256 30212f6da52512e9100109638280f1148f69a0b8f3cc3dfccd2e89c1cbae6bf4;
    physical lines 339–339, row_sha256 58df0e7bde807569d53228603db6a4bc94c0edc82c101f339b9540cce74cdab3;
    physical lines 340–340, row_sha256 291ce111c50cfcc970e4d47b9047671cb968498a97d626809325898713de0ef2;
    physical lines 341–341, row_sha256 181aad803ce0d2cce84e93cab53db7bd90bb72904f11e80d101c3db2f27cf46a;
    physical lines 342–342, row_sha256 ebb79e24785f90c99fb0c7aaedb1c271b1b5368ec2a2d6491e918f678cc147e9;
    physical lines 343–343, row_sha256 0edda1c8eac54e3e16a8bb53707b5afc595c64ec0f742d0a7a0c36c2790a88fe;
    physical lines 344–344, row_sha256 77c5e0b981712406ec60ffdc64ad53e8723bee3fedd6bc5b33f1b12f5be9fba2;
    physical lines 345–345, row_sha256 a9d4a7ddc2482ea090b446e81d630300237ccd53cac7b9aee797677cdd6db396
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"organism_name": "Streptomyces
    rochei", "organism_wikidata": "http://www.wikidata.org/entity/Q26292213", "reference_doi":
    "10.1002/CBIC.201500393", "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27149238", "taxon_id":
    "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1016/J.JBIOSC.2018.03.006",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1016/J.TET.2011.05.047",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1016/S0378-1119(00)00060-3",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1038/JA.2010.146",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1038/S41598-019-47406-Y",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1046/J.1365-2958.2003.03523.X",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1080/09168451.2014.882761",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1128/JB.01383-07",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.1271/BBB.90591",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.7164/ANTIBIOTICS.26.647",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}, {"organism_name": "Streptomyces rochei", "organism_wikidata":
    "http://www.wikidata.org/entity/Q26292213", "reference_doi": "10.7164/ANTIBIOTICS.47.1447",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27149238",
    "taxon_id": "NCBITaxon:1928"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2346-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match scope; no
    replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/cyanometdb_occurrences":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "ATDILMLBOZKFGI-JUTMVFGESA-N"}}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match scope; no
    replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/npclassifier":
    {"matches": [{"last_physical_line": 98, "physical_line": 98, "raw_tsv_record":
    "ATDILMLBOZKFGI-JUTMVFGESA-N\t[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C\tTerpenoids\tDiterpenoids\tCembrane
    diterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results":
    "Cembrane diterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "superclass_results": "Diterpenoids"},
    "row_sha256": "d5a5f3e07b33c0e790c1eff9aab7b42cf54f0521ccd1caf00551ca2dad7e2a9f"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "ATDILMLBOZKFGI-JUTMVFGESA-N"}}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 98–98, row_sha256 d5a5f3e07b33c0e790c1eff9aab7b42cf54f0521ccd1caf00551ca2dad7e2a9f
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"class_results": "Cembrane diterpenoids",
    "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "[H][C@]12C[C@]([H])(O)\\C=C\\C(\\C)=C\\C[C@]([H])(O)\\C=C\\C(\\C)=C\\[C@@]([H])(NC(=O)C(C)=O)[C@](C)(C(=O)O1)C(=O)[C@@H]2C",
    "standard_inchi_key": "ATDILMLBOZKFGI-JUTMVFGESA-N", "superclass_results": "Diterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2346-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match scope; no
    replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/pubchem_bioassay":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "ATDILMLBOZKFGI-JUTMVFGESA-N"}}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match scope; no
    replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/bindingdb_targets":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "ATDILMLBOZKFGI-JUTMVFGESA-N"}}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match scope; no
    replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "ATDILMLBOZKFGI-JUTMVFGESA-N"}}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match scope; no
    replay. Exact copied saved values: {"/contexts/9/source_scope_inventory/joins/chebi_origins":
    {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows",
    "query": []}}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /records/5/direct_companion_paths; /records/5/direct_companion_predicates
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Exact direct companion scope; a shared locus is not identity or transferred
    evidence. Exact copied saved values: {"/records/5/direct_companion_paths": [],
    "/records/5/direct_companion_predicates": []}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /records/5/direct_companion_paths
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: 'Complete source and raw/history carries are explicitly attributed in source
    notes. Distinct companion metadata: []'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: support-2346-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 175–200; lines 368–435
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: Schema separates stored structures, partial stereo and versioned computed
    classification from asserted identity.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2346-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 145–174
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: The source stereo_complete predicate uses unassigned tetrahedral centres
    in source SMILES, not every normalized tautomer or natural stereochemical proof.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2346-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 296–307; lines 982–1020
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: Maintained seeder retains source structure and all versioned model arrays;
    no regeneration was run.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2346-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: Twelve scientific dimensions and partial completion reflect actual access
    and check limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2346-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current skill under the absolute no-outbound instruction
  accessed_at: '2026-11-04T04:54:20.560210Z'
  support: supports
  summary: Read-only review, maintained ownership and no native-status promotion apply;
    no external lookup authorized.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:28:50.246712Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 451bdae3fced338f9cab6a0065481c50af073167c8f08ea2278221cdc9bd3b9f
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:29:16.400882Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 855c8f91f20c1843d397c7f6cc176f7bc5b008882a65cac37c9d332069c3fa14
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:29:36.734590Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:30:13.718045Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:30:25.980598Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: f0f15dd29bebbfeaee4046ecb5069d24cf4a36fdd1c6d046bf9208c3c24d4d57
assessments:
- assessment_id: support-2346-identity
  area: identity
  topic: Identity
  outcome: unknown
  summary: The minted identifier naturalproductmech:mibig-441a8c4d3f and complete
    key ATDILMLBOZKFGI-JUTMVFGESA-N preserve the compound labelled lankacidin C in
    MIBiG BGC0001100 version 5. NPAtlas NPA04098 remains an unrefreshed cross-reference.
    The exact retained ChEBI structure query has no match within its saved scope;
    it does not establish a new global absence. Matching stored identifiers and name
    provenance support local fidelity without independently re-establishing the natural
    isolate or its experimental structure assignment.
  target_ids:
  - naturalproductmech:mibig-441a8c4d3f
  evidence_ids:
  - support-2346-grounding-owner
  - support-2346-source-mibig_compounds
  - support-2346-query-chebi_structures
  - support-2346-chemistry
  - support-2346-direct-contexts
  - support-2346-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: ATDILMLBOZKFGI-JUTMVFGESA-N; exact retained full key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - support-2346-grounding-owner
    - support-2346-source-mibig_compounds
    - support-2346-query-chebi_structures
    - support-2346-chemistry
    - support-2346-direct-contexts
    - support-2346-companion-boundaries
  - name: grounding_scope
    value: The minted identifier naturalproductmech:mibig-441a8c4d3f and complete
      key ATDILMLBOZKFGI-JUTMVFGESA-N preserve the compound labelled lankacidin C
      in MIBiG BGC0001100 version 5. NPAtlas NPA04098 remains an unrefreshed cross-reference.
      The exact retained ChEBI structure query has no match within its saved scope;
      it does not establish a new global absence. Matching stored identifiers and
      name provenance support local fidelity without independently re-establishing
      the natural isolate or its experimental structure assignment.
    definition: Retained local grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2346-grounding-owner
    - support-2346-source-mibig_compounds
    - support-2346-query-chebi_structures
    - support-2346-chemistry
    - support-2346-direct-contexts
    - support-2346-companion-boundaries
- assessment_id: support-2346-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both complete saved forms are neutral C25H33NO7, with 33 heavy atoms, 34
    bonds and one connected component. They retain a carbon macrocycle, an integrated
    six-membered lactone, two hydroxyls, a ring ketone and an acylamide side chain
    containing another ketone. The saved ring list includes alternate cycles and must
    not be interpreted as three independent rings. Six tetrahedral centres and four
    E alkenes are specified in both forms. The amide remains C19(=O20)-N18 in the
    SMILES table and C22(=O30)-N25 in the InChI-derived table; the mobile-H InChI
    layer has not produced a different fixed tautomer in this original diagnostic.
    All ten comparison flags are true. The recorded chirality-aware correspondence
    covers 33 atoms while full_graph_identity_established remains false; local Cis/Trans
    potential-stereo descriptors depend on atom ordering and do not contradict the
    aligned E bond labels. Stored completeness is not fresh experimental stereochemical
    proof.
  target_ids:
  - naturalproductmech:mibig-441a8c4d3f
  evidence_ids:
  - support-2346-grounding-owner
  - support-2346-chemistry
  - support-2346-topology
  - support-2346-diagnostic-acceptance
  - support-2346-structure-schema
  - support-2346-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both complete saved forms are neutral C25H33NO7, with 33 heavy atoms, 34
      bonds and one connected component. They retain a carbon macrocycle, an integrated
      six-membered lactone, two hydroxyls, a ring ketone and an acylamide side chain
      containing another ketone. The saved ring list includes alternate cycles and
      must not be interpreted as three independent rings. Six tetrahedral centres
      and four E alkenes are specified in both forms. The amide remains C19(=O20)-N18
      in the SMILES table and C22(=O30)-N25 in the InChI-derived table; the mobile-H
      InChI layer has not produced a different fixed tautomer in this original diagnostic.
      All ten comparison flags are true. The recorded chirality-aware correspondence
      covers 33 atoms while full_graph_identity_established remains false; local Cis/Trans
      potential-stereo descriptors depend on atom ordering and do not contradict the
      aligned E bond labels. Stored completeness is not fresh experimental stereochemical
      proof.
    definition: Complete saved stereo/atom/bond interpretation; no new parse or experimental
      assignment.
    evidence_ids:
    - support-2346-grounding-owner
    - support-2346-chemistry
    - support-2346-topology
    - support-2346-diagnostic-acceptance
    - support-2346-structure-schema
    - support-2346-stereo-method
  - name: representation_correspondence
    value: Both complete saved forms are neutral C25H33NO7, with 33 heavy atoms, 34
      bonds and one connected component. They retain a carbon macrocycle, an integrated
      six-membered lactone, two hydroxyls, a ring ketone and an acylamide side chain
      containing another ketone. The saved ring list includes alternate cycles and
      must not be interpreted as three independent rings. Six tetrahedral centres
      and four E alkenes are specified in both forms. The amide remains C19(=O20)-N18
      in the SMILES table and C22(=O30)-N25 in the InChI-derived table; the mobile-H
      InChI layer has not produced a different fixed tautomer in this original diagnostic.
      All ten comparison flags are true. The recorded chirality-aware correspondence
      covers 33 atoms while full_graph_identity_established remains false; local Cis/Trans
      potential-stereo descriptors depend on atom ordering and do not contradict the
      aligned E bond labels. Stored completeness is not fresh experimental stereochemical
      proof.
    definition: Normalized identifier agreement does not establish fixed-graph or
      natural-form identity.
    evidence_ids:
    - support-2346-grounding-owner
    - support-2346-chemistry
    - support-2346-topology
    - support-2346-diagnostic-acceptance
    - support-2346-structure-schema
    - support-2346-stereo-method
- assessment_id: support-2346-provenance
  area: provenance
  topic: Origin
  outcome: supported
  summary: MIBiG BGC0001100 version 5 retains Streptomyces rochei (NCBITaxon:1928),
    GenBank AB088224.2 and locus coordinates 4922–35881. The active entry retains
    questionable quality and unknown completeness in its raw row. SOURCE_ASSERTION
    grades the producer, while CLUSTER_UNSTATED grades the locus because no method
    is stated. The NRPS and PKS source classes are separately asserted; no strain,
    complete pathway, enzyme activity or experimentally established producer is inferred
    from them.
  target_ids:
  - naturalproductmech:mibig-441a8c4d3f
  evidence_ids:
  - support-2346-origin-owner
  - support-2346-source-mibig_compounds
  - support-2346-cached-taxonomy
  - support-2346-source-routes
  - support-2346-direct-contexts
  - support-2346-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0001100 version 5 retains Streptomyces rochei (NCBITaxon:1928),
      GenBank AB088224.2 and locus coordinates 4922–35881. The active entry retains
      questionable quality and unknown completeness in its raw row. SOURCE_ASSERTION
      grades the producer, while CLUSTER_UNSTATED grades the locus because no method
      is stated. The NRPS and PKS source classes are separately asserted; no strain,
      complete pathway, enzyme activity or experimentally established producer is
      inferred from them.
    definition: Producer, occurrence, species, strain and unresolved labels retain
      separate scope; cached labels are not fresh authority.
    evidence_ids:
    - support-2346-origin-owner
    - support-2346-source-mibig_compounds
    - support-2346-cached-taxonomy
    - support-2346-source-routes
    - support-2346-direct-contexts
    - support-2346-companion-boundaries
  - name: producer_evidence
    value: MIBiG BGC0001100 version 5 retains Streptomyces rochei (NCBITaxon:1928),
      GenBank AB088224.2 and locus coordinates 4922–35881. The active entry retains
      questionable quality and unknown completeness in its raw row. SOURCE_ASSERTION
      grades the producer, while CLUSTER_UNSTATED grades the locus because no method
      is stated. The NRPS and PKS source classes are separately asserted; no strain,
      complete pathway, enzyme activity or experimentally established producer is
      inferred from them.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - support-2346-origin-owner
    - support-2346-source-mibig_compounds
    - support-2346-cached-taxonomy
    - support-2346-source-routes
    - support-2346-direct-contexts
    - support-2346-companion-boundaries
  - name: locus_evidence
    value: MIBiG BGC0001100 version 5 retains Streptomyces rochei (NCBITaxon:1928),
      GenBank AB088224.2 and locus coordinates 4922–35881. The active entry retains
      questionable quality and unknown completeness in its raw row. SOURCE_ASSERTION
      grades the producer, while CLUSTER_UNSTATED grades the locus because no method
      is stated. The NRPS and PKS source classes are separately asserted; no strain,
      complete pathway, enzyme activity or experimentally established producer is
      inferred from them.
    definition: Source version/status/method/grade is not a complete pathway or fresh
      primary verification.
    evidence_ids:
    - support-2346-origin-owner
    - support-2346-source-mibig_compounds
    - support-2346-cached-taxonomy
    - support-2346-source-routes
    - support-2346-direct-contexts
    - support-2346-companion-boundaries
- assessment_id: support-2346-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: PMID:12791134 is retained at the MIBiG ENTRY level as a DATABASE_ASSERTION
    for producer/locus provenance. The twelve LOTUS DOI strings have occurrence scope,
    including publications expressed with different journal/year formats. Their presence
    is not proof of twelve independent isolations, and publication independence or
    equivalence to the entry-level PMID has not been established. No paper or identifier
    was freshly accessed.
  target_ids:
  - naturalproductmech:mibig-441a8c4d3f
  evidence_ids:
  - support-2346-origin-owner
  - support-2346-occurrence-owner
  - support-2346-source-mibig_compounds
  - support-2346-source-notes
  - support-2346-direct-contexts
  - support-2346-companion-boundaries
  - support-2346-source-lotus_occurrences
  dimensions:
  - name: citation_scope
    value: PMID:12791134 is retained at the MIBiG ENTRY level as a DATABASE_ASSERTION
      for producer/locus provenance. The twelve LOTUS DOI strings have occurrence
      scope, including publications expressed with different journal/year formats.
      Their presence is not proof of twelve independent isolations, and publication
      independence or equivalence to the entry-level PMID has not been established.
      No paper or identifier was freshly accessed.
    definition: Database provenance, historical primary-experiment support and occurrence
      citations retain distinct roles; no publication independence or fresh access
      is assumed.
    evidence_ids:
    - support-2346-origin-owner
    - support-2346-occurrence-owner
    - support-2346-source-mibig_compounds
    - support-2346-source-notes
    - support-2346-direct-contexts
    - support-2346-companion-boundaries
    - support-2346-source-lotus_occurrences
- assessment_id: support-2346-occurrence
  area: evidence
  topic: Activity
  outcome: supported
  summary: All twelve written LOTUS occurrences name Streptomyces rochei and preserve
    twelve literal source references. The owner explicitly keeps occurrence separate
    from production and warns that citations can overlap. These rows do not upgrade
    SOURCE_ASSERTION or CLUSTER_UNSTATED. No bioactivity, pharmacological molecular
    target, graph or pathway is declared in the complete owner. Exact empty PubChem,
    BindingDB, sibling-corpus and other joins mean only no match in those retained
    query scopes, not universal absence of activity or biosynthesis.
  target_ids:
  - naturalproductmech:mibig-441a8c4d3f
  evidence_ids:
  - support-2346-occurrence-owner
  - support-2346-assay-owner
  - support-2346-source-routes
  - support-2346-cached-taxonomy
  - support-2346-query-lotus_occurrences
  - support-2346-query-chebi_origins
  - support-2346-query-cyanometdb_occurrences
  - support-2346-query-pubchem_bioassay
  - support-2346-query-bindingdb_targets
  - support-2346-query-antibioticmech_inchikeys
  - support-2346-direct-contexts
  - support-2346-companion-boundaries
  dimensions:
  - name: occurrence_scope
    value: All twelve written LOTUS occurrences name Streptomyces rochei and preserve
      twelve literal source references. The owner explicitly keeps occurrence separate
      from production and warns that citations can overlap. These rows do not upgrade
      SOURCE_ASSERTION or CLUSTER_UNSTATED. No bioactivity, pharmacological molecular
      target, graph or pathway is declared in the complete owner. Exact empty PubChem,
      BindingDB, sibling-corpus and other joins mean only no match in those retained
      query scopes, not universal absence of activity or biosynthesis.
    definition: Occurrence placements are not counts of independent experiments or
      demonstrated producers.
    evidence_ids:
    - support-2346-occurrence-owner
    - support-2346-assay-owner
    - support-2346-source-routes
    - support-2346-cached-taxonomy
    - support-2346-query-lotus_occurrences
    - support-2346-query-chebi_origins
    - support-2346-query-cyanometdb_occurrences
    - support-2346-query-pubchem_bioassay
    - support-2346-query-bindingdb_targets
    - support-2346-query-antibioticmech_inchikeys
    - support-2346-direct-contexts
    - support-2346-companion-boundaries
  - name: assay_target_scope
    value: All twelve written LOTUS occurrences name Streptomyces rochei and preserve
      twelve literal source references. The owner explicitly keeps occurrence separate
      from production and warns that citations can overlap. These rows do not upgrade
      SOURCE_ASSERTION or CLUSTER_UNSTATED. No bioactivity, pharmacological molecular
      target, graph or pathway is declared in the complete owner. Exact empty PubChem,
      BindingDB, sibling-corpus and other joins mean only no match in those retained
      query scopes, not universal absence of activity or biosynthesis.
    definition: Exact retained assay/target assertions are bounded; biosynthetic proteins
      are not pharmacological target evidence.
    evidence_ids:
    - support-2346-occurrence-owner
    - support-2346-assay-owner
    - support-2346-source-routes
    - support-2346-cached-taxonomy
    - support-2346-query-lotus_occurrences
    - support-2346-query-chebi_origins
    - support-2346-query-cyanometdb_occurrences
    - support-2346-query-pubchem_bioassay
    - support-2346-query-bindingdb_targets
    - support-2346-query-antibioticmech_inchikeys
    - support-2346-direct-contexts
    - support-2346-companion-boundaries
- assessment_id: support-2346-classification
  area: consistency
  topic: Classification
  outcome: concern
  summary: NPClassifier npclassifier.gnps2.org@2026-09-07 faithfully supplies Terpenoids,
    Diterpenoids, Cembrane diterpenoids and is_glycoside:false. The C25 nitrogen-bearing
    macrocycle with acylamide/lactone functionality and the separate NRPS/PKS source
    classes make that model filing an applicability concern. Carbon count alone is
    not used to prove a biosynthetic class, and a faithful versioned prediction is
    not automatically a source-record error. The positive six-membered C5O motif is
    the integrated lactone, not an assigned sugar residue or glycosidic linkage; it
    does not contradict the retained false glycoside prediction.
  target_ids:
  - naturalproductmech:mibig-441a8c4d3f
  evidence_ids:
  - support-2346-classification-owner
  - support-2346-source-mibig_compounds
  - support-2346-source-npclassifier
  - support-2346-chemistry
  - support-2346-topology
  - support-2346-structure-schema
  - support-2346-classification-seeder
  - support-2346-direct-contexts
  - support-2346-companion-boundaries
  dimensions:
  - name: classification_applicability
    value: NPClassifier npclassifier.gnps2.org@2026-09-07 faithfully supplies Terpenoids,
      Diterpenoids, Cembrane diterpenoids and is_glycoside:false. The C25 nitrogen-bearing
      macrocycle with acylamide/lactone functionality and the separate NRPS/PKS source
      classes make that model filing an applicability concern. Carbon count alone
      is not used to prove a biosynthetic class, and a faithful versioned prediction
      is not automatically a source-record error. The positive six-membered C5O motif
      is the integrated lactone, not an assigned sugar residue or glycosidic linkage;
      it does not contradict the retained false glycoside prediction.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct evidence types.
    evidence_ids:
    - support-2346-classification-owner
    - support-2346-source-mibig_compounds
    - support-2346-source-npclassifier
    - support-2346-chemistry
    - support-2346-topology
    - support-2346-structure-schema
    - support-2346-classification-seeder
    - support-2346-direct-contexts
    - support-2346-companion-boundaries
- assessment_id: support-2346-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: The complete current raw owner/history, actual canonical intake, assigned
    retained source rows and both complete saved forms have been read. No selected
    mechanism requires a maintained reader for this owner. Natural identity, source-only
    producer/locus grades and model applicability remain bounded; full QC, complete
    OAK coverage and fresh external verification are unavailable. No corrective finding
    is supported by the current evidence; final assembly will retain partial completion.
  target_ids:
  - naturalproductmech:mibig-441a8c4d3f
  evidence_ids:
  - support-2346-owner
  - support-2346-capture
  - support-2346-intake
  - support-2346-intake-acceptance
  - support-2346-inventory-acceptance
  - support-2346-plan
  - support-2346-plan-acceptance
  - support-2346-source-notes
  - support-2346-curation-scope
  - support-2346-diagnostic-execution
  - support-2346-diagnostic-acceptance
  - support-2346-native-acceptance
  - support-2346-review-profile
  - support-2346-review-skill
  - support-2346-query-mibig_compounds
  - support-2346-query-chebi_structures
  - support-2346-query-lotus_occurrences
  - support-2346-query-cyanometdb_occurrences
  - support-2346-query-npclassifier
  - support-2346-query-pubchem_bioassay
  - support-2346-query-bindingdb_targets
  - support-2346-query-antibioticmech_inchikeys
  - support-2346-query-chebi_origins
  dimensions:
  - name: review_completion
    value: The complete current raw owner/history, actual canonical intake, assigned
      retained source rows and both complete saved forms have been read. No selected
      mechanism requires a maintained reader for this owner. Natural identity, source-only
      producer/locus grades and model applicability remain bounded; full QC, complete
      OAK coverage and fresh external verification are unavailable. No corrective
      finding is supported by the current evidence; final assembly will retain partial
      completion.
    definition: Completion reflects actual evidence access and required-check coverage;
      parsing and gate success are not scientific proof.
    evidence_ids:
    - support-2346-owner
    - support-2346-capture
    - support-2346-intake
    - support-2346-intake-acceptance
    - support-2346-inventory-acceptance
    - support-2346-plan
    - support-2346-plan-acceptance
    - support-2346-source-notes
    - support-2346-curation-scope
    - support-2346-diagnostic-execution
    - support-2346-diagnostic-acceptance
    - support-2346-native-acceptance
    - support-2346-review-profile
    - support-2346-review-skill
    - support-2346-query-mibig_compounds
    - support-2346-query-chebi_structures
    - support-2346-query-lotus_occurrences
    - support-2346-query-cyanometdb_occurrences
    - support-2346-query-npclassifier
    - support-2346-query-pubchem_bioassay
    - support-2346-query-bindingdb_targets
    - support-2346-query-antibioticmech_inchikeys
    - support-2346-query-chebi_origins
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
- Two original undefined-stereo and two charge-rearrangement warnings remain global
  and unassigned. No additional molecular/YAML parse, source query or target invocation
  occurred during scientific authoring.
- No source record or native status/history is edited. Computed model concerns do
  not automatically establish a maintained-source defect.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support personally read all five complete raw owners/history, actual intakes and
  the disjoint source partition; exact prior companion carries and BGC/Native complementary
  readings remain attributed in the joint notes.
- 'Support personally read all ten saved forms: 312 atom and 338 bond rows, every
  scalar/ring/stereo/motif/map (a98425, da0f1d, d898a7, dc945f). The original correspondence
  limits are preserved; no new graph computation or molecular parse.'
- ROOT operated activation/capture, inventory/composer, canonical intakes and the
  diagnostic. Native operated original gates and maintained reader under ROOT authorization;
  ROOT separately accepted results. Scientific authoring invoked none of these targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-235
```
