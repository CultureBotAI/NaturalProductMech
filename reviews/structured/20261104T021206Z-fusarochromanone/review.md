# Local evidence review: fusarochromanone

- Review: 20261104T021206Z-fusarochromanone
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T01:29:01.336284Z
- Finished UTC: 2026-11-04T02:12:06.192155Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Fusarochromanone preserves matching partially specified structures, distinct source NRPS/OTHER and model Merohemiterpenoid classifications, and separate producer versus occurrence claims. Scientific completion remains partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2327; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-95c375019f | data/natural_products/terpenoids/fusarochromanone.yaml | generated | fusarochromanone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-95c375019f | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-95c375019f | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-95c375019f | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-95c375019f | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-95c375019f | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-95c375019f | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-95c375019f | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-95c375019f | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-95c375019f.

The minted identifier and literal Fusarochromanone label retain full key COSICWYFCAPPJB-UHFFFAOYSA-N from BGC0002256 version 3. Exact retained ChEBI structure matching is empty; NPAtlas NPA017097 and PubChem 107777 are retained cross-references. Fusarochromene, desacetylfusarochromene and 4-hydroxykynurenine remain distinct full-key companions despite shared locus ownership.

### Representation

representation: supported. Targets: naturalproductmech:mibig-95c375019f.

Both forms are neutral C15H20N2O4 with 21 atoms and 22 bonds. The complete tables show a benzene ring sharing an edge with a six-membered oxygen heterocycle, two ketones, an aromatic amino substituent and an amino-alcohol side chain. The side-chain tetrahedron is unspecified in both forms, consistent with stereo_complete:false. All ten comparison flags are true and the original correspondence is complete, while full_graph_identity_established remains false. The cyclic ether alone does not identify a sugar or glycosidic linkage, and matching partially specified forms do not identify the natural stereoisomer.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-95c375019f.

Fusarium equiseti NCBITaxon:61235 is SOURCE_ASSERTION from BGC0002256 version 3. The locus has no stated method and remains CLUSTER_UNSTATED; active/questionable/unknown are source metadata. Separate F. equiseti and historical F. roseum occurrences do not upgrade that production claim. The local taxon 5128 stanza names F. sambucinum and retains F. roseum as a synonym; this cached relationship is not fresh taxonomy verification.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-95c375019f.

PMID:33107888 is ENTRY-level MIBiG provenance shared across the BGC compounds. The three LOTUS DOI strings 10.1139/V86-217, 10.1097/CAD.0B013E3280D94298 and 10.1128/AEM.55.4.794-797.1989 remain occurrence citations. They are not automatically pure-compound activity evidence, independent replications or proof of producer equivalence.

### Activity

evidence: supported. Targets: naturalproductmech:mibig-95c375019f.

Three written LOTUS occurrences retain two taxon scopes and three literal DOI strings. There is no written bioactivity or molecular target, and exact retained PubChem, BindingDB, sibling activity, ChEBI-origin and CyanometDB joins are empty. Publication titles or companion activity are not substituted for an owner-specific assay; bounded empty joins do not mean inactivity.

### Classification

consistency: supported. Targets: naturalproductmech:mibig-95c375019f.

NPClassifier retains Terpenoids / Meroterpenoids / Merohemiterpenoids and is_glycoside:false at its named 2026-09-07 version. Source NRPS and OTHER, with Type I and other subclasses, describe the BGC and are separate from this computed filing. The gem-dimethyl oxygen heterocycle and amino-ketone side chain permit a bounded topology discussion; their presence does not experimentally establish a meroterpenoid pathway or require a source-identity correction.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-95c375019f.

All twelve scientific dimensions were assessed against the complete owner/history, actual intake, complete retained source scope and both saved molecular forms. Five original local commands passed; full QC, complete OAK authority coverage and fresh primary/taxonomic verification remain unavailable. This owner has no declared mechanism root/component and no selected maintained reader. No new supported maintained-source correction is established in this bounded evidence scope. Scientific completion remains partial; native status/history are unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2327-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/fusarochromanone.yaml; Whole current owner plaintext and complete curation_history | supports | Complete owner and all 3 history entries are covered by current exact whole-reading attribution. Native curation_status remains SEEDED. |
| support-2327-capture | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/6 | supports | Complete original captured owner and exact literal mechanism/component presence, distinct from maintained resolution. Exact copied saved values: {"/records/6": {"component_captures": [], "mechanism_capture_scope": "raw_owner_and_declared_components_only_not_maintained_resolution", "order": 2327, "owner_document": {"bgc_class": ["NRPS", "OTHER"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256", "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id": "NCBITaxon:61235"}], "chemical_structure": {"smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi": "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": false, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:04Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:01:42Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories and curation tables.", "curator": "seed_from_sources", "timestamp": "2026-10-13T10:42:50Z"}], "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "grounding_status": "MINTED", "identifier": "naturalproductmech:mibig-95c375019f", "label": "fusarochromanone", "np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["FUNGAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1139/V86-217"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q54356794", "source": "LOTUS", "taxon_id": "NCBITaxon:5128", "taxon_label": "Fusarium roseum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1097/CAD.0B013E3280D94298"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1128/AEM.55.4.794-797.1989"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti", "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "producer_taxon_groups": ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-95c375019f", "source": "MIBIG", "source_id": "BGC0002256", "source_label": "fusarochromanone", "source_version": "3"}], "xrefs": ["npatlas:NPA017097", "pubchem:107777"]}, "owner_pin": {"bytes": 4391, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/fusarochromanone.yaml", "sha256": "5d8adf4a61d8d941b042d0efb089a113fdab1f54296b6cbc5b915490669f9a2b"}, "path": "data/natural_products/terpenoids/fusarochromanone.yaml", "read_finished_at": "2026-11-04T01:29:01.338305Z", "read_started_at": "2026-11-04T01:29:01.336284Z"}} |
| support-2327-grounding-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/6/owner_document/identifier; /records/6/owner_document/label; /records/6/owner_document/chemical_structure; /records/6/owner_document/grounding_status; /records/6/owner_document/grounding_notes; /records/6/owner_document/source_concepts; /records/6/owner_document/xrefs | supports | Exact identity, source definition and grounding fields, including retained unresolved discussion where present. Exact copied saved values: {"/records/6/owner_document/chemical_structure": {"smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi": "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": false, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "/records/6/owner_document/grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "/records/6/owner_document/grounding_status": "MINTED", "/records/6/owner_document/identifier": "naturalproductmech:mibig-95c375019f", "/records/6/owner_document/label": "fusarochromanone", "/records/6/owner_document/source_concepts": [{"minted_identifier": "naturalproductmech:mibig-95c375019f", "source": "MIBIG", "source_id": "BGC0002256", "source_label": "fusarochromanone", "source_version": "3"}], "/records/6/owner_document/xrefs": ["npatlas:NPA017097", "pubchem:107777"]} |
| support-2327-origin-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters; /records/6/owner_document/producer_taxon_groups | supports | Separately graded producer and locus source assertions. Exact copied saved values: {"/records/6/owner_document/biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256", "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id": "NCBITaxon:61235"}], "/records/6/owner_document/producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "/records/6/owner_document/producer_taxon_groups": ["FUNGAL"]} |
| support-2327-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/6/owner_document/occurrences; /records/6/owner_document/occurrence_taxon_groups | supports | Written occurrence placements and retained further-row notes. Exact copied saved values: {"/records/6/owner_document/occurrence_taxon_groups": ["FUNGAL"], "/records/6/owner_document/occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1139/V86-217"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q54356794", "source": "LOTUS", "taxon_id": "NCBITaxon:5128", "taxon_label": "Fusarium roseum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1097/CAD.0B013E3280D94298"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1128/AEM.55.4.794-797.1989"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti", "taxon_source": "NCBITaxon"}]} |
| support-2327-assay-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/6/owner_document | supports | Written observations and coarse activity summary; whole owner selector proves absent optional roots without a global absence claim. Exact copied saved values: {"/records/6/owner_document": {"bgc_class": ["NRPS", "OTHER"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256", "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id": "NCBITaxon:61235"}], "chemical_structure": {"smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi": "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": false, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:04Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:01:42Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories and curation tables.", "curator": "seed_from_sources", "timestamp": "2026-10-13T10:42:50Z"}], "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "grounding_status": "MINTED", "identifier": "naturalproductmech:mibig-95c375019f", "label": "fusarochromanone", "np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["FUNGAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1139/V86-217"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q54356794", "source": "LOTUS", "taxon_id": "NCBITaxon:5128", "taxon_label": "Fusarium roseum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1097/CAD.0B013E3280D94298"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1128/AEM.55.4.794-797.1989"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti", "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "producer_taxon_groups": ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-95c375019f", "source": "MIBIG", "source_id": "BGC0002256", "source_label": "fusarochromanone", "source_version": "3"}], "xrefs": ["npatlas:NPA017097", "pubchem:107777"]}} |
| support-2327-classification-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/6/owner_document/np_pathway; /records/6/owner_document/np_classification; /records/6/owner_document/bgc_class | supports | Versioned computed filing and separately asserted BGC/compound classes. Exact copied saved values: {"/records/6/owner_document/bgc_class": ["NRPS", "OTHER"], "/records/6/owner_document/np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "/records/6/owner_document/np_pathway": "TERPENOIDS"} |
| support-2327-chemistry | /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json; /records/6/declared_structure; /records/6/comparisons; /records/6/atom_correspondence | supports | Complete original declared forms/comparisons/map, unchanged. Exact copied saved values: {"/records/6/atom_correspondence": {"complete_atom_count_match": true, "full_graph_identity_established": false, "scope": "One chirality-aware substructure match; no independent full graph or natural identity claim.", "smiles_to_inchi_atom_indices": [0, 14, 5, 10, 19, 12, 11, 20, 3, 2, 8, 13, 16, 9, 18, 4, 7, 6, 17, 15, 1]}, "/records/6/comparisons": {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared": true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal": true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer": true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "/records/6/declared_structure": {"smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi": "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": false, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}} |
| support-2327-topology | /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed; /records/6/inchi/computed; /records/6/declared_structure; /records/6/comparisons; /records/6/atom_correspondence | supports | Both forms are neutral C15H20N2O4 with 21 atoms and 22 bonds. The complete tables show a benzene ring sharing an edge with a six-membered oxygen heterocycle, two ketones, an aromatic amino substituent and an amino-alcohol side chain. The side-chain tetrahedron is unspecified in both forms, consistent with stereo_complete:false. All ten comparison flags are true and the original correspondence is complete, while full_graph_identity_established remains false. The cyclic ether alone does not identify a sugar or glycosidic linkage, and matching partially specified forms do not identify the natural stereoisomer. |
| support-2327-intake | /private/tmp/npm-review-work/shared-next-batch233/intakes/2327-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake, all admitted input roles and maintained correction ownership. Exact copied saved values: {"/repository": "CultureBotAI/NaturalProductMech", "/source": {"git_revision": "ce6a5498df5be51116bd5e0c119023ee62bb5464", "inputs": [{"path": ".claude/skills/curate-yaml-record/references/review-checklist.md", "role": "context", "sha256": "13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9"}, {"path": ".claude/skills/review-yaml-record/SKILL.md", "role": "context", "sha256": "493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae"}, {"path": "AGENTS.md", "role": "context", "sha256": "69e4037f8dc97d4b00bb7bb83b41ceca025f6ef578d5c0bf8086f3400becde0b"}, {"path": "conf/id_label_targets.yaml", "role": "context", "sha256": "24235903e0e8df5793a30e92c551082c71c1c67739ea4e3b5fb0f68853a805e6"}, {"path": "conf/producer_evidence.tsv", "role": "context", "sha256": "67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131"}, {"path": "conf/record_review.yaml", "role": "context", "sha256": "e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8"}, {"path": "curation/lotus_occurrence_exclusions.tsv", "role": "context", "sha256": "d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d"}, {"path": "curation/mibig_claim_references.tsv", "role": "context", "sha256": "bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029"}, {"path": "curation/mibig_locus_evidence_overrides.tsv", "role": "context", "sha256": "7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e"}, {"path": "curation/mibig_producer_isolates.tsv", "role": "context", "sha256": "8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8"}, {"path": "curation/mibig_producer_strains.tsv", "role": "context", "sha256": "bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae"}, {"path": "curation/mibig_structure_corrections.tsv", "role": "context", "sha256": "c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0"}, {"path": "curation/mibig_xref_exclusions.tsv", "role": "context", "sha256": "cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c"}, {"path": "data/natural_products/PATHS.tsv", "role": "context", "sha256": "2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3"}, {"path": "data/natural_products/alkaloids/fusarochromene.yaml", "role": "context", "sha256": "f653a81c04f30502862e365013fef6947eb101c9b2d3594bf2ac1db978709812"}, {"path": "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "role": "context", "sha256": "e76125d04ba9f83d969ab51a0fa4d4886ba3d4ff92e9a2860274a2f74e98cd86"}, {"path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml", "role": "context", "sha256": "0ce3c89b56843eacfcf535c67a34a84b798ecf99a5d4c70da5824b334997a021"}, {"path": "data/natural_products/terpenoids/fusarochromanone.yaml", "role": "target", "sha256": "5d8adf4a61d8d941b042d0efb089a113fdab1f54296b6cbc5b915490669f9a2b"}, {"path": "data/raw/MANIFEST.yaml", "role": "context", "sha256": "b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3"}, {"path": "data/raw/antibioticmech_inchikeys.tsv", "role": "context", "sha256": "ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6"}, {"path": "data/raw/bindingdb_targets.tsv", "role": "context", "sha256": "3cff45281c35a8b14d4d7784bc4b7af80e8e27779a5667a0292f0d9b022a22c1"}, {"path": "data/raw/chebi_origins.tsv", "role": "context", "sha256": "fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8"}, {"path": "data/raw/chebi_structures.tsv", "role": "context", "sha256": "62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2"}, {"path": "data/raw/corpus_taxa.obo", "role": "context", "sha256": "8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9"}, {"path": "data/raw/cyanometdb_occurrences.tsv", "role": "context", "sha256": "f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8"}, {"path": "data/raw/lotus_occurrences.tsv", "role": "context", "sha256": "ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94"}, {"path": "data/raw/mibig_compounds.tsv", "role": "context", "sha256": "e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6"}, {"path": "data/raw/npclassifier.tsv", "role": "context", "sha256": "acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3"}, {"path": "data/raw/pubchem_bioassay.tsv", "role": "context", "sha256": "6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b"}, {"path": "docs/CURATION.md", "role": "context", "sha256": "c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa"}, {"path": "docs/HARMONIZATION.md", "role": "context", "sha256": "c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79"}, {"path": "docs/record-review-profile.md", "role": "context", "sha256": "1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a"}, {"path": "docs/record-reviews.md", "role": "context", "sha256": "452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b"}, {"path": "justfile", "role": "context", "sha256": "4f9057e3e54656dd46f2ded4d3a8f0804acad348d2605d436405e1fcfb6af550"}, {"path": "schema/record_review.yaml", "role": "context", "sha256": "229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb"}, {"path": "scripts/extract_chebi.py", "role": "context", "sha256": "46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f"}, {"path": "scripts/extract_mibig.py", "role": "context", "sha256": "e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c"}, {"path": "scripts/seed_from_sources.py", "role": "context", "sha256": "5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5"}, {"path": "src/naturalproductmech/curate/claim_references.py", "role": "context", "sha256": "0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3"}, {"path": "src/naturalproductmech/schema/naturalproductmech.yaml", "role": "context", "sha256": "9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d"}], "state": "working_tree"}, "/status": "inspection_only", "/targets": [{"kind": "generated", "label": "fusarochromanone", "owner_paths": [{"path": "scripts/seed_from_sources.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained harmonization generator; seeded fields are corrected through maintained inputs and validated regeneration."}, {"path": "data/raw/mibig_compounds.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Retained MIBiG structure, producer and compound-specific locus assertions."}, {"path": "data/raw/npclassifier.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Pinned computed classification and filing assertions."}, {"path": "scripts/extract_mibig.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained extraction of MIBiG compound names, structures, stereochemistry flags and source provenance."}, {"path": "data/raw/lotus_occurrences.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Retained cited occurrence assertions, distinct from demonstrated production."}], "ownership_note": "This review proposes no record edit. Source corrections belong in maintained inventories, implemented curation tables, extractors or the seeder; generated pages are not owners.", "path": "data/natural_products/terpenoids/fusarochromanone.yaml", "record_class": "NaturalProductRecord", "target_id": "naturalproductmech:mibig-95c375019f"}]} |
| support-2327-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-intake-acceptance-001.json; /status; /accepted; /source_placements; /unique_source_paths | supports | ROOT accepts all ten original canonical intakes, with 396 source placements and 68 distinct paths. |
| support-2327-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-source-inventory-acceptance-001.json; /status; /accepted | supports | ROOT accepts the original local inventory; source meanings are separately attributed. |
| support-2327-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-input-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepts the original input plan, not a scientific verdict. |
| support-2327-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-diagnostic-acceptance-001.json; /status; /accepted; /verified; /records; /warnings; /warning_scope | supports | ROOT accepts twenty original stored parses, all paired comparisons and declared keys. Two original undefined-stereo warnings remain global and unassigned. |
| support-2327-native-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-native-gates-acceptance-001.json; /status; /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates | supports | Five original local commands passed; full QC and complete OAK authority coverage remain unavailable. |
| support-2327-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-execution-001.json; Whole original execution receipt | supports | ROOT operated the one accepted diagnostic. No replay, alternate parse or owner-specific warning attribution is introduced by scientific authoring. |
| support-2327-plan | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-target-input-plan-001.json; /records/6; /source_placement_count; /unique_source_path_count | supports | Complete accepted per-owner input plan; cohort totals 396 placements / 68 paths, owner 40 placements. |
| support-2327-source-notes | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Joint complete source reading and exact raw/history carry attribution, source-specific cautions and access limits; the notes precede scientific adjudication. |
| support-2327-curation-scope | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json; /curation | supports | BGC performed one bounded 169-literal scan of eight directly opened implemented tables, including ignored files, with zero textual hits. Reserved decisions.tsv was unconsumed; no global absence claim follows. |
| support-2327-source-routes | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/23/source_scope_inventory/matched_chebi_ids; /contexts/23/source_scope_inventory/source_taxa; /contexts/23/source_scope_inventory/forward_taxon_merge_matches; /contexts/23/source_scope_inventory/nonorganism_matches; /contexts/23/source_scope_inventory/actual_assay_rows; /contexts/23/source_scope_inventory/blank_AID_sentinels; /contexts/23/source_scope_inventory/related_corpus_rows | supports | Complete retained route metadata, including assay/sentinel distinctions and exact empty routes. Exact copied saved values: {"/contexts/23/source_scope_inventory/actual_assay_rows": [], "/contexts/23/source_scope_inventory/blank_AID_sentinels": [], "/contexts/23/source_scope_inventory/forward_taxon_merge_matches": [], "/contexts/23/source_scope_inventory/matched_chebi_ids": [], "/contexts/23/source_scope_inventory/nonorganism_matches": [], "/contexts/23/source_scope_inventory/related_corpus_rows": [], "/contexts/23/source_scope_inventory/source_taxa": ["NCBITaxon:5128", "NCBITaxon:61235"]} |
| support-2327-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/26; /cached_taxonomy/whole_stanzas/38 | supports | All applicable cached stanzas copied in full; names/synonyms remain local snapshots. Exact copied saved values: {"/cached_taxonomy/whole_stanzas/26": {"complete_stanza": "[Term]\nid: NCBITaxon:5128\nname: Fusarium sambucinum\nsynonym: \"Fusarium roseum\" EXACT []\nsynonym: \"Fusarium sambucinum var. sambucinum\" EXACT []\nsynonym: \"Gibberella pulicaris\" EXACT []\nsynonym: \"Sphaeria pulicaris\" EXACT []\n\n", "id": "NCBITaxon:5128", "physical_line": 8045}, "/cached_taxonomy/whole_stanzas/38": {"complete_stanza": "[Term]\nid: NCBITaxon:61235\nname: Fusarium equiseti\nsynonym: \"Gibberella intricans\" EXACT []\nsynonym: \"Selenosporium equiseti\" EXACT []\n\n", "id": "NCBITaxon:61235", "physical_line": 27935}} |
| support-2327-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/23/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/mibig_compounds": {"matches": [{"last_physical_line": 2707, "physical_line": 2707, "raw_tsv_record": "BGC0002256\t3\tactive\tquestionable\tunknown\tfusarochromanone\t1\tCC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C\tInChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3\tCOSICWYFCAPPJB-UHFFFAOYSA-N\tfalse\t\tnpatlas:NPA017097&#124;pubchem:107777\tNCBITaxon:61235\tFusarium equiseti\tNRPS&#124;other\tType I&#124;other\tBK013344.1\t1\t23896\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:33107888\tENTRY\n", "row": {"bgc_classes": "NRPS&#124;other", "bgc_subclasses": "Type I&#124;other", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "fusarochromanone", "database_ids": "npatlas:NPA017097&#124;pubchem:107777", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "BK013344.1", "locus_evidence_methods": "", "locus_from": "1", "locus_to": "23896", "mibig_accession": "BGC0002256", "primary_reference": "PMID:33107888", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi": "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": "false", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}, "row_sha256": "44d2d987ec1322d4ee6d802780e9535419b987744ff102119c17e62f63dfaedd"}], "predicate": "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}} |
| support-2327-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2707–2707, row_sha256 44d2d987ec1322d4ee6d802780e9535419b987744ff102119c17e62f63dfaedd | supports | Complete retained physical row fields: [{"bgc_classes": "NRPS&#124;other", "bgc_subclasses": "Type I&#124;other", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "fusarochromanone", "database_ids": "npatlas:NPA017097&#124;pubchem:107777", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "BK013344.1", "locus_evidence_methods": "", "locus_from": "1", "locus_to": "23896", "mibig_accession": "BGC0002256", "primary_reference": "PMID:33107888", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi": "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": "false", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}] |
| support-2327-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/23/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/chebi_structures": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}} |
| support-2327-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/23/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/lotus_occurrences": {"matches": [{"last_physical_line": 839, "physical_line": 839, "raw_tsv_record": "COSICWYFCAPPJB-UHFFFAOYSA-N\tFusarium roseum\tNCBITaxon:5128\thttp://www.wikidata.org/entity/Q54356794\t10.1139/V86-217\thttp://www.wikidata.org/entity/Q27278066\n", "row": {"organism_name": "Fusarium roseum", "organism_wikidata": "http://www.wikidata.org/entity/Q54356794", "reference_doi": "10.1139/V86-217", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27278066", "taxon_id": "NCBITaxon:5128"}, "row_sha256": "55c27de607cabf3bded965835b11e971eb41e7b1289e67f3a1485337c5413c46"}, {"last_physical_line": 840, "physical_line": 840, "raw_tsv_record": "COSICWYFCAPPJB-UHFFFAOYSA-N\tFusarium equiseti\tNCBITaxon:61235\thttp://www.wikidata.org/entity/Q103817240\t10.1097/CAD.0B013E3280D94298\thttp://www.wikidata.org/entity/Q27278066\n", "row": {"organism_name": "Fusarium equiseti", "organism_wikidata": "http://www.wikidata.org/entity/Q103817240", "reference_doi": "10.1097/CAD.0B013E3280D94298", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27278066", "taxon_id": "NCBITaxon:61235"}, "row_sha256": "fb1c564bd006a8596330dc6ef0900d6edec7595cf2a9be5d8cd4ede1a1fc91a9"}, {"last_physical_line": 841, "physical_line": 841, "raw_tsv_record": "COSICWYFCAPPJB-UHFFFAOYSA-N\tFusarium equiseti\tNCBITaxon:61235\thttp://www.wikidata.org/entity/Q103817240\t10.1128/AEM.55.4.794-797.1989\thttp://www.wikidata.org/entity/Q27278066\n", "row": {"organism_name": "Fusarium equiseti", "organism_wikidata": "http://www.wikidata.org/entity/Q103817240", "reference_doi": "10.1128/AEM.55.4.794-797.1989", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27278066", "taxon_id": "NCBITaxon:61235"}, "row_sha256": "5d02b5df53d2be1246d7467ed73fc52abed4b9c8c8e49f788b2c1370aea24d57"}], "predicate": "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}} |
| support-2327-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 839–839, row_sha256 55c27de607cabf3bded965835b11e971eb41e7b1289e67f3a1485337c5413c46; physical lines 840–840, row_sha256 fb1c564bd006a8596330dc6ef0900d6edec7595cf2a9be5d8cd4ede1a1fc91a9; physical lines 841–841, row_sha256 5d02b5df53d2be1246d7467ed73fc52abed4b9c8c8e49f788b2c1370aea24d57 | supports | Complete retained physical row fields: [{"organism_name": "Fusarium roseum", "organism_wikidata": "http://www.wikidata.org/entity/Q54356794", "reference_doi": "10.1139/V86-217", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27278066", "taxon_id": "NCBITaxon:5128"}, {"organism_name": "Fusarium equiseti", "organism_wikidata": "http://www.wikidata.org/entity/Q103817240", "reference_doi": "10.1097/CAD.0B013E3280D94298", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27278066", "taxon_id": "NCBITaxon:61235"}, {"organism_name": "Fusarium equiseti", "organism_wikidata": "http://www.wikidata.org/entity/Q103817240", "reference_doi": "10.1128/AEM.55.4.794-797.1989", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27278066", "taxon_id": "NCBITaxon:61235"}] |
| support-2327-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/23/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/cyanometdb_occurrences": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}} |
| support-2327-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/23/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/npclassifier": {"matches": [{"last_physical_line": 321, "physical_line": 321, "raw_tsv_record": "COSICWYFCAPPJB-UHFFFAOYSA-N\tCC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C\tTerpenoids\tMeroterpenoids\tMerohemiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results": "Merohemiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "superclass_results": "Meroterpenoids"}, "row_sha256": "34931960f55a5b942c98c3ca8c9d23e27bd99fb184dd7dcc8543bdf08344d7ae"}], "predicate": "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}} |
| support-2327-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 321–321, row_sha256 34931960f55a5b942c98c3ca8c9d23e27bd99fb184dd7dcc8543bdf08344d7ae | supports | Complete retained physical row fields: [{"class_results": "Merohemiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "superclass_results": "Meroterpenoids"}] |
| support-2327-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/23/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/pubchem_bioassay": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}} |
| support-2327-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/23/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/bindingdb_targets": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}} |
| support-2327-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/23/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/antibioticmech_inchikeys": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}} |
| support-2327-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/23/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, all matches and exact no-match predicate scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/chebi_origins": {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows", "query": []}} |
| support-2327-direct-contexts | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /records/6/direct_companion_paths; /records/6/direct_companion_predicates | supports | Exact direct companion scope; shared locus/key predicates do not transfer identity or evidence. Exact copied saved values: {"/records/6/direct_companion_paths": ["data/natural_products/alkaloids/fusarochromene.yaml", "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "data/natural_products/terpenoids/desacetylfusarochromene.yaml"], "/records/6/direct_companion_predicates": [{"path": "data/natural_products/alkaloids/fusarochromene.yaml", "same_complete_InChIKey": false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}, {"path": "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "same_complete_InChIKey": false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}, {"path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml", "same_complete_InChIKey": false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}]} |
| support-2327-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/0; /contexts/1; /contexts/16 | supports | Complete source and raw/history context carries remain explicitly attributed in source notes. Distinct companion metadata: [{"declared_mechanism_roots_literal": [], "history_count": 2, "identifier": "naturalproductmech:mibig-ea1711783a", "input": {"bytes": 2962, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/fusarochromene.yaml", "sha256": "f653a81c04f30502862e365013fef6947eb101c9b2d3594bf2ac1db978709812"}, "label": "fusarochromene", "owned_bgc_ids": ["BGC0002256"], "path": "data/natural_products/alkaloids/fusarochromene.yaml", "standard_inchi_key": "JWWKBOBMBFAOAR-LLVKDONJSA-N"}, {"declared_mechanism_roots_literal": [], "history_count": 2, "identifier": "naturalproductmech:mibig-a896068bf1", "input": {"bytes": 2434, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "sha256": "e76125d04ba9f83d969ab51a0fa4d4886ba3d4ff92e9a2860274a2f74e98cd86"}, "label": "4-hydroxykynurenine", "owned_bgc_ids": ["BGC0002256"], "path": "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "standard_inchi_key": "GNUVAWTWZCFAJG-UHFFFAOYSA-N"}, {"declared_mechanism_roots_literal": [], "history_count": 2, "identifier": "naturalproductmech:mibig-da909f5425", "input": {"bytes": 2434, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/desacetylfusarochromene.yaml", "sha256": "0ce3c89b56843eacfcf535c67a34a84b798ecf99a5d4c70da5824b334997a021"}, "label": "desacetylfusarochromene", "owned_bgc_ids": ["BGC0002256"], "path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}] |
| support-2327-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 175–200; lines 368–435 | supports | Schema distinguishes retained structures, partial stereo and versioned computed classification from experimentally asserted identity. |
| support-2327-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 145–174 | supports | Source stereo_complete derives from unassigned tetrahedral centers in source SMILES; predicate inspection does not establish natural stereochemistry. |
| support-2327-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 296–307; lines 982–1020 | supports | Maintained seeder preserves source structure and versioned model arrays; no regeneration was run for scientific authoring. |
| support-2327-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | Twelve scientific dimensions, claim-specific evidence and partial completion reflect actual access limits. |
| support-2327-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill under absolute user no-outbound constraint | supports | Read-only review, source ownership and no native-status promotion apply; no external lookup was authorized. |
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
review_id: 20261104T021206Z-fusarochromanone
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: fusarochromanone'
started_at: '2026-11-04T01:29:01.336284Z'
finished_at: '2026-11-04T02:12:06.192155Z'
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
summary: Fusarochromanone preserves matching partially specified structures, distinct
  source NRPS/OTHER and model Merohemiterpenoid classifications, and separate producer
  versus occurrence claims. Scientific completion remains partial.
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
  - path: data/natural_products/alkaloids/fusarochromene.yaml
    sha256: f653a81c04f30502862e365013fef6947eb101c9b2d3594bf2ac1db978709812
    role: context
  - path: data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml
    sha256: e76125d04ba9f83d969ab51a0fa4d4886ba3d4ff92e9a2860274a2f74e98cd86
    role: context
  - path: data/natural_products/terpenoids/desacetylfusarochromene.yaml
    sha256: 0ce3c89b56843eacfcf535c67a34a84b798ecf99a5d4c70da5824b334997a021
    role: context
  - path: data/natural_products/terpenoids/fusarochromanone.yaml
    sha256: 5d8adf4a61d8d941b042d0efb089a113fdab1f54296b6cbc5b915490669f9a2b
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
  selection: Campaign path order 2327; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-95c375019f
targets:
- target_id: naturalproductmech:mibig-95c375019f
  path: data/natural_products/terpenoids/fusarochromanone.yaml
  label: fusarochromanone
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
  - naturalproductmech:mibig-95c375019f
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
  - naturalproductmech:mibig-95c375019f
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
  - naturalproductmech:mibig-95c375019f
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
  - naturalproductmech:mibig-95c375019f
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
  - naturalproductmech:mibig-95c375019f
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
  - naturalproductmech:mibig-95c375019f
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-95c375019f
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-95c375019f
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2327-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/fusarochromanone.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Complete owner and all 3 history entries are covered by current exact whole-reading
    attribution. Native curation_status remains SEEDED.
  snapshot_sha256: 5d8adf4a61d8d941b042d0efb089a113fdab1f54296b6cbc5b915490669f9a2b
- evidence_id: support-2327-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/6
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete original captured owner and exact literal mechanism/component
    presence, distinct from maintained resolution. Exact copied saved values: {"/records/6":
    {"component_captures": [], "mechanism_capture_scope": "raw_owner_and_declared_components_only_not_maintained_resolution",
    "order": 2327, "owner_document": {"bgc_class": ["NRPS", "OTHER"], "biosynthesis_origin":
    "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256",
    "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3",
    "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256
    entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}],
    "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED",
    "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id":
    "NCBITaxon:61235"}], "chemical_structure": {"smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C",
    "standard_inchi": "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3",
    "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": false,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:04Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:01:42Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    and curation tables.", "curator": "seed_from_sources", "timestamp": "2026-10-13T10:42:50Z"}],
    "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares
    this structure, so the record keeps a content-hashed identifier.", "grounding_status":
    "MINTED", "identifier": "naturalproductmech:mibig-95c375019f", "label": "fusarochromanone",
    "np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["FUNGAL"], "occurrences":
    [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1139/V86-217"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q54356794", "source":
    "LOTUS", "taxon_id": "NCBITaxon:5128", "taxon_label": "Fusarium roseum", "taxon_source":
    "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1097/CAD.0B013E3280D94298"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235",
    "taxon_label": "Fusarium equiseti", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1128/AEM.55.4.794-797.1989"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240 This taxon
    is also recorded as a producer. Production and occurrence are distinct claims;
    their citations may refer to the same publication. Publication independence has
    not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235", "taxon_label":
    "Fusarium equiseti", "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster":
    "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference":
    "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence:
    none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades
    the taxon claim, which is a different question.", "source": "MIBIG", "source_version":
    "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "producer_taxon_groups":
    ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-95c375019f",
    "source": "MIBIG", "source_id": "BGC0002256", "source_label": "fusarochromanone",
    "source_version": "3"}], "xrefs": ["npatlas:NPA017097", "pubchem:107777"]}, "owner_pin":
    {"bytes": 4391, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/fusarochromanone.yaml",
    "sha256": "5d8adf4a61d8d941b042d0efb089a113fdab1f54296b6cbc5b915490669f9a2b"},
    "path": "data/natural_products/terpenoids/fusarochromanone.yaml", "read_finished_at":
    "2026-11-04T01:29:01.338305Z", "read_started_at": "2026-11-04T01:29:01.336284Z"}}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2327-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/6/owner_document/identifier; /records/6/owner_document/label;
    /records/6/owner_document/chemical_structure; /records/6/owner_document/grounding_status;
    /records/6/owner_document/grounding_notes; /records/6/owner_document/source_concepts;
    /records/6/owner_document/xrefs
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Exact identity, source definition and grounding fields, including retained
    unresolved discussion where present. Exact copied saved values: {"/records/6/owner_document/chemical_structure":
    {"smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi": "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3",
    "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": false,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "/records/6/owner_document/grounding_notes":
    "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.", "/records/6/owner_document/grounding_status": "MINTED", "/records/6/owner_document/identifier":
    "naturalproductmech:mibig-95c375019f", "/records/6/owner_document/label": "fusarochromanone",
    "/records/6/owner_document/source_concepts": [{"minted_identifier": "naturalproductmech:mibig-95c375019f",
    "source": "MIBIG", "source_id": "BGC0002256", "source_label": "fusarochromanone",
    "source_version": "3"}], "/records/6/owner_document/xrefs": ["npatlas:NPA017097",
    "pubchem:107777"]}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2327-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters;
    /records/6/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Separately graded producer and locus source assertions. Exact copied saved
    values: {"/records/6/owner_document/biosynthetic_gene_clusters": [{"accession":
    "mibig:BGC0002256", "bgc_class": ["NRPS", "OTHER"], "entry_status": "active",
    "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference":
    "PMID:33107888"}], "genome_accession": "genbank:BK013344.1", "link_evidence_basis":
    "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium
    equiseti", "organism_taxon_id": "NCBITaxon:61235"}], "/records/6/owner_document/producer_organisms":
    [{"biosynthetic_gene_cluster": "mibig:BGC0002256", "evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken
    from the entry level", "reference": "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION",
    "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED;
    this field grades the taxon claim, which is a different question.", "source":
    "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:61235", "taxon_label":
    "Fusarium equiseti"}], "/records/6/owner_document/producer_taxon_groups": ["FUNGAL"]}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2327-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/6/owner_document/occurrences; /records/6/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Written occurrence placements and retained further-row notes. Exact copied
    saved values: {"/records/6/owner_document/occurrence_taxon_groups": ["FUNGAL"],
    "/records/6/owner_document/occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1139/V86-217"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q54356794",
    "source": "LOTUS", "taxon_id": "NCBITaxon:5128", "taxon_label": "Fusarium roseum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1097/CAD.0B013E3280D94298"}], "notes": "Wikidata organism
    http://www.wikidata.org/entity/Q103817240 This taxon is also recorded as a producer.
    Production and occurrence are distinct claims; their citations may refer to the
    same publication. Publication independence has not been established.", "source":
    "LOTUS", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti", "taxon_source":
    "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1128/AEM.55.4.794-797.1989"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235",
    "taxon_label": "Fusarium equiseti", "taxon_source": "NCBITaxon"}]}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2327-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Written observations and coarse activity summary; whole owner selector
    proves absent optional roots without a global absence claim. Exact copied saved
    values: {"/records/6/owner_document": {"bgc_class": ["NRPS", "OTHER"], "biosynthesis_origin":
    "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256",
    "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3",
    "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256
    entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}],
    "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED",
    "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id":
    "NCBITaxon:61235"}], "chemical_structure": {"smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C",
    "standard_inchi": "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3",
    "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": false,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:04Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:01:42Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    and curation tables.", "curator": "seed_from_sources", "timestamp": "2026-10-13T10:42:50Z"}],
    "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares
    this structure, so the record keeps a content-hashed identifier.", "grounding_status":
    "MINTED", "identifier": "naturalproductmech:mibig-95c375019f", "label": "fusarochromanone",
    "np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["FUNGAL"], "occurrences":
    [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1139/V86-217"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q54356794", "source":
    "LOTUS", "taxon_id": "NCBITaxon:5128", "taxon_label": "Fusarium roseum", "taxon_source":
    "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1097/CAD.0B013E3280D94298"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240
    This taxon is also recorded as a producer. Production and occurrence are distinct
    claims; their citations may refer to the same publication. Publication independence
    has not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235",
    "taxon_label": "Fusarium equiseti", "taxon_source": "NCBITaxon"}, {"evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1128/AEM.55.4.794-797.1989"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q103817240 This taxon
    is also recorded as a producer. Production and occurrence are distinct claims;
    their citations may refer to the same publication. Publication independence has
    not been established.", "source": "LOTUS", "taxon_id": "NCBITaxon:61235", "taxon_label":
    "Fusarium equiseti", "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster":
    "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference":
    "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence:
    none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades
    the taxon claim, which is a different question.", "source": "MIBIG", "source_version":
    "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "producer_taxon_groups":
    ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-95c375019f",
    "source": "MIBIG", "source_id": "BGC0002256", "source_label": "fusarochromanone",
    "source_version": "3"}], "xrefs": ["npatlas:NPA017097", "pubchem:107777"]}}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2327-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/6/owner_document/np_pathway; /records/6/owner_document/np_classification;
    /records/6/owner_document/bgc_class
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Versioned computed filing and separately asserted BGC/compound classes.
    Exact copied saved values: {"/records/6/owner_document/bgc_class": ["NRPS", "OTHER"],
    "/records/6/owner_document/np_classification": {"class_results": ["Merohemiterpenoids"],
    "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results":
    ["Meroterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "/records/6/owner_document/np_pathway": "TERPENOIDS"}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: support-2327-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/declared_structure; /records/6/comparisons; /records/6/atom_correspondence
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete original declared forms/comparisons/map, unchanged. Exact copied
    saved values: {"/records/6/atom_correspondence": {"complete_atom_count_match":
    true, "full_graph_identity_established": false, "scope": "One chirality-aware
    substructure match; no independent full graph or natural identity claim.", "smiles_to_inchi_atom_indices":
    [0, 14, 5, 10, 19, 12, 11, 20, 3, 2, 8, 13, 16, 9, 18, 4, 7, 6, 17, 15, 1]}, "/records/6/comparisons":
    {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared":
    true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal":
    true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer":
    true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "/records/6/declared_structure":
    {"smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi": "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3",
    "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": false,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}}'
  snapshot_sha256: 98d9bae4e307da83403d9b3e783897999469aca3e863fd37b097f1688bf1d4ee
- evidence_id: support-2327-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed; /records/6/inchi/computed; /records/6/declared_structure;
    /records/6/comparisons; /records/6/atom_correspondence
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Both forms are neutral C15H20N2O4 with 21 atoms and 22 bonds. The complete
    tables show a benzene ring sharing an edge with a six-membered oxygen heterocycle,
    two ketones, an aromatic amino substituent and an amino-alcohol side chain. The
    side-chain tetrahedron is unspecified in both forms, consistent with stereo_complete:false.
    All ten comparison flags are true and the original correspondence is complete,
    while full_graph_identity_established remains false. The cyclic ether alone does
    not identify a sugar or glycosidic linkage, and matching partially specified forms
    do not identify the natural stereoisomer.
  snapshot_sha256: 98d9bae4e307da83403d9b3e783897999469aca3e863fd37b097f1688bf1d4ee
- evidence_id: support-2327-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/intakes/2327-inspect-001.json
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
    {"path": "data/natural_products/alkaloids/fusarochromene.yaml", "role": "context",
    "sha256": "f653a81c04f30502862e365013fef6947eb101c9b2d3594bf2ac1db978709812"},
    {"path": "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml",
    "role": "context", "sha256": "e76125d04ba9f83d969ab51a0fa4d4886ba3d4ff92e9a2860274a2f74e98cd86"},
    {"path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml", "role":
    "context", "sha256": "0ce3c89b56843eacfcf535c67a34a84b798ecf99a5d4c70da5824b334997a021"},
    {"path": "data/natural_products/terpenoids/fusarochromanone.yaml", "role": "target",
    "sha256": "5d8adf4a61d8d941b042d0efb089a113fdab1f54296b6cbc5b915490669f9a2b"},
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
    "generated", "label": "fusarochromanone", "owner_paths": [{"path": "scripts/seed_from_sources.py",
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
    generated pages are not owners.", "path": "data/natural_products/terpenoids/fusarochromanone.yaml",
    "record_class": "NaturalProductRecord", "target_id": "naturalproductmech:mibig-95c375019f"}]}'
  snapshot_sha256: 7ff93af9dde5764b92852c03417550a39f412e3321ec16f7d8ccddf4271820a9
- evidence_id: support-2327-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-intake-acceptance-001.json
  locator: /status; /accepted; /source_placements; /unique_source_paths
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: ROOT accepts all ten original canonical intakes, with 396 source placements
    and 68 distinct paths.
  snapshot_sha256: 3124e401a141d5fee52e3838ae8258cf2fc2b9c791050dfa2b6afd6ad1b308dd
- evidence_id: support-2327-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-source-inventory-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: ROOT accepts the original local inventory; source meanings are separately
    attributed.
  snapshot_sha256: 8e3a8821fa52e78220f01f692579f368a6adb58d85d3624d16eeb7fa4c86b5e1
- evidence_id: support-2327-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-input-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: ROOT accepts the original input plan, not a scientific verdict.
  snapshot_sha256: 4d76cf85f5594ce1d2b1990f9a8a3a1abbb6d2da1c9bc45456497364a4602999
- evidence_id: support-2327-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /verified; /records; /warnings; /warning_scope
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: ROOT accepts twenty original stored parses, all paired comparisons and
    declared keys. Two original undefined-stereo warnings remain global and unassigned.
  snapshot_sha256: aa8d2b7772b4907ebb043566a7016cd09fa16acee7cd80d449a7292b9f787125
- evidence_id: support-2327-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-native-gates-acceptance-001.json
  locator: /status; /accepted; /five_local_commands_passed; /all_native_gates_passed;
    /unavailable_required_gates
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Five original local commands passed; full QC and complete OAK authority
    coverage remain unavailable.
  snapshot_sha256: 7a2daeeecc690ede6862e80925055bb819c81ad72c293b2ab5f980a47ce0aa42
- evidence_id: support-2327-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: ROOT operated the one accepted diagnostic. No replay, alternate parse or
    owner-specific warning attribution is introduced by scientific authoring.
  snapshot_sha256: 589a14084b2981120032bfc10e40bb0105f2afda5e7300a7d5b296e1388951c4
- evidence_id: support-2327-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-target-input-plan-001.json
  locator: /records/6; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Complete accepted per-owner input plan; cohort totals 396 placements /
    68 paths, owner 40 placements.
  snapshot_sha256: bc361ca0270b857063f610d29fdc2c498e2ccf208d5f8ae3c0033c044923fe27
- evidence_id: support-2327-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Joint complete source reading and exact raw/history carry attribution,
    source-specific cautions and access limits; the notes precede scientific adjudication.
  snapshot_sha256: 98c23811517a583723d42fb365b4549d207753a27bd0e0c6654e836596cfad99
- evidence_id: support-2327-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: BGC performed one bounded 169-literal scan of eight directly opened implemented
    tables, including ignored files, with zero textual hits. Reserved decisions.tsv
    was unconsumed; no global absence claim follows.
  snapshot_sha256: 98c23811517a583723d42fb365b4549d207753a27bd0e0c6654e836596cfad99
- evidence_id: support-2327-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/23/source_scope_inventory/matched_chebi_ids; /contexts/23/source_scope_inventory/source_taxa;
    /contexts/23/source_scope_inventory/forward_taxon_merge_matches; /contexts/23/source_scope_inventory/nonorganism_matches;
    /contexts/23/source_scope_inventory/actual_assay_rows; /contexts/23/source_scope_inventory/blank_AID_sentinels;
    /contexts/23/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained route metadata, including assay/sentinel distinctions
    and exact empty routes. Exact copied saved values: {"/contexts/23/source_scope_inventory/actual_assay_rows":
    [], "/contexts/23/source_scope_inventory/blank_AID_sentinels": [], "/contexts/23/source_scope_inventory/forward_taxon_merge_matches":
    [], "/contexts/23/source_scope_inventory/matched_chebi_ids": [], "/contexts/23/source_scope_inventory/nonorganism_matches":
    [], "/contexts/23/source_scope_inventory/related_corpus_rows": [], "/contexts/23/source_scope_inventory/source_taxa":
    ["NCBITaxon:5128", "NCBITaxon:61235"]}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/26; /cached_taxonomy/whole_stanzas/38
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'All applicable cached stanzas copied in full; names/synonyms remain local
    snapshots. Exact copied saved values: {"/cached_taxonomy/whole_stanzas/26": {"complete_stanza":
    "[Term]\nid: NCBITaxon:5128\nname: Fusarium sambucinum\nsynonym: \"Fusarium roseum\"
    EXACT []\nsynonym: \"Fusarium sambucinum var. sambucinum\" EXACT []\nsynonym:
    \"Gibberella pulicaris\" EXACT []\nsynonym: \"Sphaeria pulicaris\" EXACT []\n\n",
    "id": "NCBITaxon:5128", "physical_line": 8045}, "/cached_taxonomy/whole_stanzas/38":
    {"complete_stanza": "[Term]\nid: NCBITaxon:61235\nname: Fusarium equiseti\nsynonym:
    \"Gibberella intricans\" EXACT []\nsynonym: \"Selenosporium equiseti\" EXACT []\n\n",
    "id": "NCBITaxon:61235", "physical_line": 27935}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/23/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/mibig_compounds":
    {"matches": [{"last_physical_line": 2707, "physical_line": 2707, "raw_tsv_record":
    "BGC0002256\t3\tactive\tquestionable\tunknown\tfusarochromanone\t1\tCC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C\tInChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3\tCOSICWYFCAPPJB-UHFFFAOYSA-N\tfalse\t\tnpatlas:NPA017097|pubchem:107777\tNCBITaxon:61235\tFusarium
    equiseti\tNRPS|other\tType I|other\tBK013344.1\t1\t23896\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:33107888\tENTRY\n",
    "row": {"bgc_classes": "NRPS|other", "bgc_subclasses": "Type I|other", "cluster_link_evidence_basis":
    "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name":
    "fusarochromanone", "database_ids": "npatlas:NPA017097|pubchem:107777", "entry_completeness":
    "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version":
    "3", "genome_accession": "BK013344.1", "locus_evidence_methods": "", "locus_from":
    "1", "locus_to": "23896", "mibig_accession": "BGC0002256", "primary_reference":
    "PMID:33107888", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis":
    "ENTRY", "smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi":
    "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3",
    "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": "false",
    "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}, "row_sha256":
    "44d2d987ec1322d4ee6d802780e9535419b987744ff102119c17e62f63dfaedd"}], "predicate":
    "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2707–2707, row_sha256 44d2d987ec1322d4ee6d802780e9535419b987744ff102119c17e62f63dfaedd
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"bgc_classes": "NRPS|other",
    "bgc_subclasses": "Type I|other", "cluster_link_evidence_basis": "CLUSTER_UNSTATED",
    "compound_classes": "", "compound_index": "1", "compound_name": "fusarochromanone",
    "database_ids": "npatlas:NPA017097|pubchem:107777", "entry_completeness": "unknown",
    "entry_quality": "questionable", "entry_status": "active", "entry_version": "3",
    "genome_accession": "BK013344.1", "locus_evidence_methods": "", "locus_from":
    "1", "locus_to": "23896", "mibig_accession": "BGC0002256", "primary_reference":
    "PMID:33107888", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis":
    "ENTRY", "smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi":
    "InChI=1S/C15H20N2O4/c1-15(2)6-11(20)13-12(21-15)4-3-9(14(13)17)10(19)5-8(16)7-18/h3-4,8,18H,5-7,16-17H2,1-2H3",
    "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "stereo_complete": "false",
    "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2327-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/23/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/chebi_structures":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "COSICWYFCAPPJB-UHFFFAOYSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/23/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/lotus_occurrences":
    {"matches": [{"last_physical_line": 839, "physical_line": 839, "raw_tsv_record":
    "COSICWYFCAPPJB-UHFFFAOYSA-N\tFusarium roseum\tNCBITaxon:5128\thttp://www.wikidata.org/entity/Q54356794\t10.1139/V86-217\thttp://www.wikidata.org/entity/Q27278066\n",
    "row": {"organism_name": "Fusarium roseum", "organism_wikidata": "http://www.wikidata.org/entity/Q54356794",
    "reference_doi": "10.1139/V86-217", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27278066", "taxon_id":
    "NCBITaxon:5128"}, "row_sha256": "55c27de607cabf3bded965835b11e971eb41e7b1289e67f3a1485337c5413c46"},
    {"last_physical_line": 840, "physical_line": 840, "raw_tsv_record": "COSICWYFCAPPJB-UHFFFAOYSA-N\tFusarium
    equiseti\tNCBITaxon:61235\thttp://www.wikidata.org/entity/Q103817240\t10.1097/CAD.0B013E3280D94298\thttp://www.wikidata.org/entity/Q27278066\n",
    "row": {"organism_name": "Fusarium equiseti", "organism_wikidata": "http://www.wikidata.org/entity/Q103817240",
    "reference_doi": "10.1097/CAD.0B013E3280D94298", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27278066", "taxon_id":
    "NCBITaxon:61235"}, "row_sha256": "fb1c564bd006a8596330dc6ef0900d6edec7595cf2a9be5d8cd4ede1a1fc91a9"},
    {"last_physical_line": 841, "physical_line": 841, "raw_tsv_record": "COSICWYFCAPPJB-UHFFFAOYSA-N\tFusarium
    equiseti\tNCBITaxon:61235\thttp://www.wikidata.org/entity/Q103817240\t10.1128/AEM.55.4.794-797.1989\thttp://www.wikidata.org/entity/Q27278066\n",
    "row": {"organism_name": "Fusarium equiseti", "organism_wikidata": "http://www.wikidata.org/entity/Q103817240",
    "reference_doi": "10.1128/AEM.55.4.794-797.1989", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27278066", "taxon_id":
    "NCBITaxon:61235"}, "row_sha256": "5d02b5df53d2be1246d7467ed73fc52abed4b9c8c8e49f788b2c1370aea24d57"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 839–839, row_sha256 55c27de607cabf3bded965835b11e971eb41e7b1289e67f3a1485337c5413c46;
    physical lines 840–840, row_sha256 fb1c564bd006a8596330dc6ef0900d6edec7595cf2a9be5d8cd4ede1a1fc91a9;
    physical lines 841–841, row_sha256 5d02b5df53d2be1246d7467ed73fc52abed4b9c8c8e49f788b2c1370aea24d57
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"organism_name": "Fusarium roseum",
    "organism_wikidata": "http://www.wikidata.org/entity/Q54356794", "reference_doi":
    "10.1139/V86-217", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "structure_wikidata":
    "http://www.wikidata.org/entity/Q27278066", "taxon_id": "NCBITaxon:5128"}, {"organism_name":
    "Fusarium equiseti", "organism_wikidata": "http://www.wikidata.org/entity/Q103817240",
    "reference_doi": "10.1097/CAD.0B013E3280D94298", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27278066", "taxon_id":
    "NCBITaxon:61235"}, {"organism_name": "Fusarium equiseti", "organism_wikidata":
    "http://www.wikidata.org/entity/Q103817240", "reference_doi": "10.1128/AEM.55.4.794-797.1989",
    "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27278066",
    "taxon_id": "NCBITaxon:61235"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2327-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/23/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/cyanometdb_occurrences":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "COSICWYFCAPPJB-UHFFFAOYSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/23/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/npclassifier":
    {"matches": [{"last_physical_line": 321, "physical_line": 321, "raw_tsv_record":
    "COSICWYFCAPPJB-UHFFFAOYSA-N\tCC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C\tTerpenoids\tMeroterpenoids\tMerohemiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n",
    "row": {"class_results": "Merohemiterpenoids", "is_glycoside": "false", "model_version":
    "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles":
    "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N",
    "superclass_results": "Meroterpenoids"}, "row_sha256": "34931960f55a5b942c98c3ca8c9d23e27bd99fb184dd7dcc8543bdf08344d7ae"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "COSICWYFCAPPJB-UHFFFAOYSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 321–321, row_sha256 34931960f55a5b942c98c3ca8c9d23e27bd99fb184dd7dcc8543bdf08344d7ae
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"class_results": "Merohemiterpenoids",
    "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "CC1(CC(=O)C2=C(O1)C=CC(=C2N)C(=O)CC(CO)N)C",
    "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N", "superclass_results": "Meroterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2327-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/23/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/pubchem_bioassay":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "COSICWYFCAPPJB-UHFFFAOYSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/23/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/bindingdb_targets":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "COSICWYFCAPPJB-UHFFFAOYSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/23/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/antibioticmech_inchikeys":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "COSICWYFCAPPJB-UHFFFAOYSA-N"}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/23/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete retained query frame, all matches and exact no-match predicate
    scope; no replay. Exact copied saved values: {"/contexts/23/source_scope_inventory/joins/chebi_origins":
    {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows",
    "query": []}}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /records/6/direct_companion_paths; /records/6/direct_companion_predicates
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Exact direct companion scope; shared locus/key predicates do not transfer
    identity or evidence. Exact copied saved values: {"/records/6/direct_companion_paths":
    ["data/natural_products/alkaloids/fusarochromene.yaml", "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml",
    "data/natural_products/terpenoids/desacetylfusarochromene.yaml"], "/records/6/direct_companion_predicates":
    [{"path": "data/natural_products/alkaloids/fusarochromene.yaml", "same_complete_InChIKey":
    false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}, {"path":
    "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "same_complete_InChIKey":
    false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}, {"path":
    "data/natural_products/terpenoids/desacetylfusarochromene.yaml", "same_complete_InChIKey":
    false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}]}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/0; /contexts/1; /contexts/16
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: 'Complete source and raw/history context carries remain explicitly attributed
    in source notes. Distinct companion metadata: [{"declared_mechanism_roots_literal":
    [], "history_count": 2, "identifier": "naturalproductmech:mibig-ea1711783a", "input":
    {"bytes": 2962, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/fusarochromene.yaml",
    "sha256": "f653a81c04f30502862e365013fef6947eb101c9b2d3594bf2ac1db978709812"},
    "label": "fusarochromene", "owned_bgc_ids": ["BGC0002256"], "path": "data/natural_products/alkaloids/fusarochromene.yaml",
    "standard_inchi_key": "JWWKBOBMBFAOAR-LLVKDONJSA-N"}, {"declared_mechanism_roots_literal":
    [], "history_count": 2, "identifier": "naturalproductmech:mibig-a896068bf1", "input":
    {"bytes": 2434, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml",
    "sha256": "e76125d04ba9f83d969ab51a0fa4d4886ba3d4ff92e9a2860274a2f74e98cd86"},
    "label": "4-hydroxykynurenine", "owned_bgc_ids": ["BGC0002256"], "path": "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml",
    "standard_inchi_key": "GNUVAWTWZCFAJG-UHFFFAOYSA-N"}, {"declared_mechanism_roots_literal":
    [], "history_count": 2, "identifier": "naturalproductmech:mibig-da909f5425", "input":
    {"bytes": 2434, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/desacetylfusarochromene.yaml",
    "sha256": "0ce3c89b56843eacfcf535c67a34a84b798ecf99a5d4c70da5824b334997a021"},
    "label": "desacetylfusarochromene", "owned_bgc_ids": ["BGC0002256"], "path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml",
    "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}]'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: support-2327-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 175–200; lines 368–435
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Schema distinguishes retained structures, partial stereo and versioned
    computed classification from experimentally asserted identity.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2327-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 145–174
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Source stereo_complete derives from unassigned tetrahedral centers in source
    SMILES; predicate inspection does not establish natural stereochemistry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2327-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 296–307; lines 982–1020
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Maintained seeder preserves source structure and versioned model arrays;
    no regeneration was run for scientific authoring.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2327-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Twelve scientific dimensions, claim-specific evidence and partial completion
    reflect actual access limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2327-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current skill under absolute user no-outbound constraint
  accessed_at: '2026-11-04T02:01:48.988187Z'
  support: supports
  summary: Read-only review, source ownership and no native-status promotion apply;
    no external lookup was authorized.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
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
- assessment_id: support-2327-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The minted identifier and literal Fusarochromanone label retain full key
    COSICWYFCAPPJB-UHFFFAOYSA-N from BGC0002256 version 3. Exact retained ChEBI structure
    matching is empty; NPAtlas NPA017097 and PubChem 107777 are retained cross-references.
    Fusarochromene, desacetylfusarochromene and 4-hydroxykynurenine remain distinct
    full-key companions despite shared locus ownership.
  target_ids:
  - naturalproductmech:mibig-95c375019f
  evidence_ids:
  - support-2327-grounding-owner
  - support-2327-source-mibig_compounds
  - support-2327-query-chebi_structures
  - support-2327-chemistry
  - support-2327-direct-contexts
  - support-2327-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: COSICWYFCAPPJB-UHFFFAOYSA-N; exact retained full key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - support-2327-grounding-owner
    - support-2327-source-mibig_compounds
    - support-2327-query-chebi_structures
    - support-2327-chemistry
    - support-2327-direct-contexts
    - support-2327-companion-boundaries
  - name: grounding_scope
    value: MINTED; full key retained, ChEBI join empty; three distinct shared-locus
      companions are context only.
    definition: Retained local grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2327-grounding-owner
    - support-2327-source-mibig_compounds
    - support-2327-query-chebi_structures
    - support-2327-chemistry
    - support-2327-direct-contexts
    - support-2327-companion-boundaries
- assessment_id: support-2327-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both forms are neutral C15H20N2O4 with 21 atoms and 22 bonds. The complete
    tables show a benzene ring sharing an edge with a six-membered oxygen heterocycle,
    two ketones, an aromatic amino substituent and an amino-alcohol side chain. The
    side-chain tetrahedron is unspecified in both forms, consistent with stereo_complete:false.
    All ten comparison flags are true and the original correspondence is complete,
    while full_graph_identity_established remains false. The cyclic ether alone does
    not identify a sugar or glycosidic linkage, and matching partially specified forms
    do not identify the natural stereoisomer.
  target_ids:
  - naturalproductmech:mibig-95c375019f
  evidence_ids:
  - support-2327-grounding-owner
  - support-2327-chemistry
  - support-2327-topology
  - support-2327-diagnostic-acceptance
  - support-2327-structure-schema
  - support-2327-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: One unspecified amino-alcohol side-chain center in both forms; source stereo_complete:false
      retained.
    definition: Complete saved stereo/atom/bond interpretation; no new parse or experimental
      assignment.
    evidence_ids:
    - support-2327-grounding-owner
    - support-2327-chemistry
    - support-2327-topology
    - support-2327-diagnostic-acceptance
    - support-2327-structure-schema
    - support-2327-stereo-method
  - name: representation_correspondence
    value: All ten comparisons true with complete original map; partially specified
      natural identity remains unresolved.
    definition: Normalized identifier agreement does not establish fixed-graph or
      natural-form identity.
    evidence_ids:
    - support-2327-grounding-owner
    - support-2327-chemistry
    - support-2327-topology
    - support-2327-diagnostic-acceptance
    - support-2327-structure-schema
    - support-2327-stereo-method
- assessment_id: support-2327-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: Fusarium equiseti NCBITaxon:61235 is SOURCE_ASSERTION from BGC0002256 version
    3. The locus has no stated method and remains CLUSTER_UNSTATED; active/questionable/unknown
    are source metadata. Separate F. equiseti and historical F. roseum occurrences
    do not upgrade that production claim. The local taxon 5128 stanza names F. sambucinum
    and retains F. roseum as a synonym; this cached relationship is not fresh taxonomy
    verification.
  target_ids:
  - naturalproductmech:mibig-95c375019f
  evidence_ids:
  - support-2327-origin-owner
  - support-2327-source-mibig_compounds
  - support-2327-cached-taxonomy
  - support-2327-source-routes
  - support-2327-direct-contexts
  - support-2327-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: Producer 61235 remains separate from occurrences 61235 and 5128; cached
      F. roseum synonym is not refreshed authority.
    definition: Producer, occurrence, species, strain and unresolved labels retain
      separate scope; cached labels are not fresh authority.
    evidence_ids:
    - support-2327-origin-owner
    - support-2327-source-mibig_compounds
    - support-2327-cached-taxonomy
    - support-2327-source-routes
    - support-2327-direct-contexts
    - support-2327-companion-boundaries
  - name: producer_evidence
    value: F. equiseti SOURCE_ASSERTION, BGC0002256 version 3.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - support-2327-origin-owner
    - support-2327-source-mibig_compounds
    - support-2327-cached-taxonomy
    - support-2327-source-routes
    - support-2327-direct-contexts
    - support-2327-companion-boundaries
  - name: locus_evidence
    value: CLUSTER_UNSTATED with no method; source active/questionable/unknown.
    definition: Source version/status/method/grade is not a complete pathway or fresh
      primary verification.
    evidence_ids:
    - support-2327-origin-owner
    - support-2327-source-mibig_compounds
    - support-2327-cached-taxonomy
    - support-2327-source-routes
    - support-2327-direct-contexts
    - support-2327-companion-boundaries
- assessment_id: support-2327-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: PMID:33107888 is ENTRY-level MIBiG provenance shared across the BGC compounds.
    The three LOTUS DOI strings 10.1139/V86-217, 10.1097/CAD.0B013E3280D94298 and
    10.1128/AEM.55.4.794-797.1989 remain occurrence citations. They are not automatically
    pure-compound activity evidence, independent replications or proof of producer
    equivalence.
  target_ids:
  - naturalproductmech:mibig-95c375019f
  evidence_ids:
  - support-2327-origin-owner
  - support-2327-occurrence-owner
  - support-2327-source-mibig_compounds
  - support-2327-source-notes
  - support-2327-direct-contexts
  - support-2327-companion-boundaries
  - support-2327-source-lotus_occurrences
  dimensions:
  - name: citation_scope
    value: ENTRY PMID:33107888 differs in role from three occurrence DOI placements.
    definition: Database provenance, historical primary-experiment support and occurrence
      citations retain distinct roles; no publication independence or fresh access
      is assumed.
    evidence_ids:
    - support-2327-origin-owner
    - support-2327-occurrence-owner
    - support-2327-source-mibig_compounds
    - support-2327-source-notes
    - support-2327-direct-contexts
    - support-2327-companion-boundaries
    - support-2327-source-lotus_occurrences
- assessment_id: support-2327-activity
  area: evidence
  topic: Activity
  outcome: supported
  summary: Three written LOTUS occurrences retain two taxon scopes and three literal
    DOI strings. There is no written bioactivity or molecular target, and exact retained
    PubChem, BindingDB, sibling activity, ChEBI-origin and CyanometDB joins are empty.
    Publication titles or companion activity are not substituted for an owner-specific
    assay; bounded empty joins do not mean inactivity.
  target_ids:
  - naturalproductmech:mibig-95c375019f
  evidence_ids:
  - support-2327-occurrence-owner
  - support-2327-assay-owner
  - support-2327-source-routes
  - support-2327-cached-taxonomy
  - support-2327-query-lotus_occurrences
  - support-2327-query-chebi_origins
  - support-2327-query-cyanometdb_occurrences
  - support-2327-query-pubchem_bioassay
  - support-2327-query-bindingdb_targets
  - support-2327-query-antibioticmech_inchikeys
  - support-2327-direct-contexts
  - support-2327-companion-boundaries
  dimensions:
  - name: occurrence_scope
    value: Three written LOTUS occurrences across two taxon IDs; counts are not independent
      experiments.
    definition: Occurrence placements are not counts of independent experiments or
      demonstrated producers.
    evidence_ids:
    - support-2327-occurrence-owner
    - support-2327-assay-owner
    - support-2327-source-routes
    - support-2327-cached-taxonomy
    - support-2327-query-lotus_occurrences
    - support-2327-query-chebi_origins
    - support-2327-query-cyanometdb_occurrences
    - support-2327-query-pubchem_bioassay
    - support-2327-query-bindingdb_targets
    - support-2327-query-antibioticmech_inchikeys
    - support-2327-direct-contexts
    - support-2327-companion-boundaries
  - name: assay_target_scope
    value: No written assay/target and exact retained activity joins empty; no inference
      from companion claims.
    definition: Exact retained assay/target assertions are bounded; phenotype titles
      are not direct mechanism proof.
    evidence_ids:
    - support-2327-occurrence-owner
    - support-2327-assay-owner
    - support-2327-source-routes
    - support-2327-cached-taxonomy
    - support-2327-query-lotus_occurrences
    - support-2327-query-chebi_origins
    - support-2327-query-cyanometdb_occurrences
    - support-2327-query-pubchem_bioassay
    - support-2327-query-bindingdb_targets
    - support-2327-query-antibioticmech_inchikeys
    - support-2327-direct-contexts
    - support-2327-companion-boundaries
- assessment_id: support-2327-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: NPClassifier retains Terpenoids / Meroterpenoids / Merohemiterpenoids and
    is_glycoside:false at its named 2026-09-07 version. Source NRPS and OTHER, with
    Type I and other subclasses, describe the BGC and are separate from this computed
    filing. The gem-dimethyl oxygen heterocycle and amino-ketone side chain permit
    a bounded topology discussion; their presence does not experimentally establish
    a meroterpenoid pathway or require a source-identity correction.
  target_ids:
  - naturalproductmech:mibig-95c375019f
  evidence_ids:
  - support-2327-classification-owner
  - support-2327-source-mibig_compounds
  - support-2327-source-npclassifier
  - support-2327-chemistry
  - support-2327-topology
  - support-2327-structure-schema
  - support-2327-classification-seeder
  - support-2327-direct-contexts
  - support-2327-companion-boundaries
  dimensions:
  - name: classification_applicability
    value: Versioned Merohemiterpenoids/false glycoside, source NRPS/OTHER and observed
      oxygen heterocycle remain separate scopes.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct evidence types.
    evidence_ids:
    - support-2327-classification-owner
    - support-2327-source-mibig_compounds
    - support-2327-source-npclassifier
    - support-2327-chemistry
    - support-2327-topology
    - support-2327-structure-schema
    - support-2327-classification-seeder
    - support-2327-direct-contexts
    - support-2327-companion-boundaries
- assessment_id: support-2327-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: All twelve scientific dimensions were assessed against the complete owner/history,
    actual intake, complete retained source scope and both saved molecular forms.
    Five original local commands passed; full QC, complete OAK authority coverage
    and fresh primary/taxonomic verification remain unavailable. This owner has no
    declared mechanism root/component and no selected maintained reader. No new supported
    maintained-source correction is established in this bounded evidence scope. Scientific
    completion remains partial; native status/history are unchanged.
  target_ids:
  - naturalproductmech:mibig-95c375019f
  evidence_ids:
  - support-2327-owner
  - support-2327-capture
  - support-2327-intake
  - support-2327-intake-acceptance
  - support-2327-inventory-acceptance
  - support-2327-plan
  - support-2327-plan-acceptance
  - support-2327-source-notes
  - support-2327-curation-scope
  - support-2327-diagnostic-execution
  - support-2327-diagnostic-acceptance
  - support-2327-native-acceptance
  - support-2327-review-profile
  - support-2327-review-skill
  - support-2327-query-mibig_compounds
  - support-2327-query-chebi_structures
  - support-2327-query-lotus_occurrences
  - support-2327-query-cyanometdb_occurrences
  - support-2327-query-npclassifier
  - support-2327-query-pubchem_bioassay
  - support-2327-query-bindingdb_targets
  - support-2327-query-antibioticmech_inchikeys
  - support-2327-query-chebi_origins
  dimensions:
  - name: review_completion
    value: 'Partial: unavailable full QC/OAK and fresh source verification; no native-status
      promotion. No new supported maintained-source correction is established in this
      bounded evidence scope.'
    definition: Completion reflects actual evidence access and required-check coverage;
      parsing and gate success are not scientific proof.
    evidence_ids:
    - support-2327-owner
    - support-2327-capture
    - support-2327-intake
    - support-2327-intake-acceptance
    - support-2327-inventory-acceptance
    - support-2327-plan
    - support-2327-plan-acceptance
    - support-2327-source-notes
    - support-2327-curation-scope
    - support-2327-diagnostic-execution
    - support-2327-diagnostic-acceptance
    - support-2327-native-acceptance
    - support-2327-review-profile
    - support-2327-review-skill
    - support-2327-query-mibig_compounds
    - support-2327-query-chebi_structures
    - support-2327-query-lotus_occurrences
    - support-2327-query-cyanometdb_occurrences
    - support-2327-query-npclassifier
    - support-2327-query-pubchem_bioassay
    - support-2327-query-bindingdb_targets
    - support-2327-query-antibioticmech_inchikeys
    - support-2327-query-chebi_origins
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
