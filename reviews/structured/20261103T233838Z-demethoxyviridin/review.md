# Local evidence review: demethoxyviridin

- Review: 20261103T233838Z-demethoxyviridin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T23:01:25.981463Z
- Finished UTC: 2026-11-03T23:38:38.959008Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Demethoxyviridin preserves the retained C19 structure and distinct unresolved producer versus species-level occurrence scope. Eight LOTUS rows reduce to four taxon–reference pairs; they are not eight independent experiments. Scientific completion remains partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2313; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-f81c240204 | data/natural_products/terpenoids/demethoxyviridin.yaml | generated | demethoxyviridin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-f81c240204 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-f81c240204 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-f81c240204 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-f81c240204 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-f81c240204 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-f81c240204 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-f81c240204 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-f81c240204 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-f81c240204.

The minted identifier preserves SWJBYJJNDIXFSA-KUHUBIRLSA-N and the literal demethoxyviridin label from BGC0001571 version 3, compound index 1. The exact saved ChEBI structure join is empty. No direct full-key or owned-BGC companion is selected for this owner; source identity is not inferred from a similar name or a normalized key alone.

### Representation

representation: supported. Targets: naturalproductmech:mibig-f81c240204.

Both saved forms are neutral C19H14O5 with 24 atoms and 28 bonds, a five-ring polycyclic framework including an aromatic carbocycle and five-membered oxygen heterocycle, three ketones and one hydroxyl. Two R tetrahedral centers are specified. All ten comparison flags are true and the original chirality-aware map is complete, while full_graph_identity_established is false. The source true stereo flag is consistent with these stored centers; this is local representation agreement, not a fresh experimental stereochemical assignment.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-f81c240204.

Nodulisporium sp. NCBITaxon:1897413 is an unresolved source producer assertion, recorded as SOURCE_ASSERTION with CLUSTER_UNSTATED and no locus method. BGC0001571 version 3 is active, questionable and of unknown completeness. LOTUS occurrences at NCBITaxon:455034 do not resolve the producer to that species. The whole local 455034 cache stanza names Hypoxylon hinnuleum and lists Nodulisporium hinnuleum as a synonym; the separate 1897413 cached label remains Nodulisporium sp.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-f81c240204.

PMID:29743477 is ENTRY-level MIBiG provenance. Four distinct LOTUS DOI strings—10.1039/P19830000867, 10.1039/P19830000871, 10.1039/P19840000567 and 10.1039/P19850001311—support occurrence placements only. Repeated names and rows do not create independent experimental replication, and none of those occurrence citations is silently promoted to the producer/locus citation.

### Activity

evidence: supported. Targets: naturalproductmech:mibig-f81c240204.

Eight exact LOTUS rows contain two name placements for each of four identical taxon 455034/literal-DOI pairs. The owner correctly writes four occurrences. This identity-based collapse preserves the four citation scopes without claiming eight experiments or equating 455034 to unresolved producer 1897413. There is no written assay or target, and all exact saved activity/target, ChEBI-origin and CyanometDB joins are empty; no inactivity inference follows.

### Classification

consistency: supported. Targets: naturalproductmech:mibig-f81c240204.

NPClassifier retains Terpenoids / Steroids / Androstane steroids and is_glycoside:false at version npclassifier.gnps2.org@2026-09-07. Source TERPENE and subclass Unknown are distinct from this model label. The saved C19 polycyclic, oxygen-heterocyclic topology and lack of a sugar residue support a bounded applicability discussion, not an experimentally demonstrated steroid pathway or a change to source identity.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-f81c240204.

All twelve scientific dimensions were assessed against the complete current owner/history, actual canonical intake, complete retained source scope and both saved molecular forms. Five original local gates passed; full QC, complete OAK authority coverage and fresh primary/taxonomic verification remain unavailable. This owner has no declared mechanism root, component or selected maintained reader. The bounded eight-table curation scan found no exact cohort-token hit; no supported new maintained-source correction is established. Scientific completion remains partial and native curation status/history remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2313-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/demethoxyviridin.yaml; Whole current owner plaintext and complete curation_history | supports | Complete current owner, including all 2 history entries; native curation_status remains SEEDED. Full raw reading/carry attribution is preserved in source notes. |
| support-2313-capture | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/2 | supports | Complete captured owner and strict mechanism-absence scope; no selected reader applies. Exact copied saved values: {"/records/2": {"component_captures": [], "mechanism_capture_scope": "raw_owner_and_declared_components_only_not_maintained_resolution", "order": 2313, "owner_document": {"bgc_class": ["TERPENE"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001571", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001571 entry version 3; citation taken from the entry level", "reference": "PMID:29743477"}], "genome_accession": "genbank:MG886384.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 66332, "organism_label": "Nodulisporium sp.", "organism_taxon_id": "NCBITaxon:1897413"}], "chemical_structure": {"smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi": "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001571"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:13Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:25Z"}], "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "grounding_status": "MINTED", "identifier": "naturalproductmech:mibig-f81c240204", "label": "demethoxyviridin", "np_classification": {"class_results": ["Androstane steroids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Steroids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["FUNGAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19830000867"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19830000871"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19840000567"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19850001311"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001571", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001571 entry version 3; citation taken from the entry level", "reference": "PMID:29743477"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:1897413", "taxon_label": "Nodulisporium sp."}], "producer_taxon_groups": ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-f81c240204", "source": "MIBIG", "source_id": "BGC0001571", "source_label": "demethoxyviridin", "source_version": "3"}]}, "owner_pin": {"bytes": 4238, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/demethoxyviridin.yaml", "sha256": "2227239b32a368e652c7e5fff066173f8b55c69314f101c2fc819175142472ab"}, "path": "data/natural_products/terpenoids/demethoxyviridin.yaml", "read_finished_at": "2026-11-03T23:01:25.983431Z", "read_started_at": "2026-11-03T23:01:25.981463Z"}} |
| support-2313-grounding-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/2/owner_document/identifier; /records/2/owner_document/label; /records/2/owner_document/chemical_structure; /records/2/owner_document/grounding_status; /records/2/owner_document/grounding_notes; /records/2/owner_document/source_concepts | supports | Exact written identity/grounding fields; absent optional fields are not invented. Exact copied saved values: {"/records/2/owner_document/chemical_structure": {"smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi": "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001571"}, "/records/2/owner_document/grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "/records/2/owner_document/grounding_status": "MINTED", "/records/2/owner_document/identifier": "naturalproductmech:mibig-f81c240204", "/records/2/owner_document/label": "demethoxyviridin", "/records/2/owner_document/source_concepts": [{"minted_identifier": "naturalproductmech:mibig-f81c240204", "source": "MIBIG", "source_id": "BGC0001571", "source_label": "demethoxyviridin", "source_version": "3"}]} |
| support-2313-origin-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/producer_taxon_groups | supports | Exact separately graded source producer and locus fields. Exact copied saved values: {"/records/2/owner_document/biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001571", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001571 entry version 3; citation taken from the entry level", "reference": "PMID:29743477"}], "genome_accession": "genbank:MG886384.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 66332, "organism_label": "Nodulisporium sp.", "organism_taxon_id": "NCBITaxon:1897413"}], "/records/2/owner_document/producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001571", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001571 entry version 3; citation taken from the entry level", "reference": "PMID:29743477"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:1897413", "taxon_label": "Nodulisporium sp."}], "/records/2/owner_document/producer_taxon_groups": ["FUNGAL"]} |
| support-2313-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/2/owner_document/occurrences; /records/2/owner_document/occurrence_taxon_groups | supports | Written occurrence scope, distinct from production. Whole owner selector also proves absence when no occurrence field exists. Exact copied saved values: {"/records/2/owner_document/occurrence_taxon_groups": ["FUNGAL"], "/records/2/owner_document/occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19830000867"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19830000871"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19840000567"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19850001311"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}]} |
| support-2313-assay-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/2/owner_document | supports | Written activity/target scope; whole owner selector proves absent optional roots without a global absence claim. Exact copied saved values: {"/records/2/owner_document": {"bgc_class": ["TERPENE"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001571", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001571 entry version 3; citation taken from the entry level", "reference": "PMID:29743477"}], "genome_accession": "genbank:MG886384.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 66332, "organism_label": "Nodulisporium sp.", "organism_taxon_id": "NCBITaxon:1897413"}], "chemical_structure": {"smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi": "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001571"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:13Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:25Z"}], "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "grounding_status": "MINTED", "identifier": "naturalproductmech:mibig-f81c240204", "label": "demethoxyviridin", "np_classification": {"class_results": ["Androstane steroids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Steroids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["FUNGAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19830000867"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19830000871"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19840000567"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1039/P19850001311"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum", "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001571", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001571 entry version 3; citation taken from the entry level", "reference": "PMID:29743477"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:1897413", "taxon_label": "Nodulisporium sp."}], "producer_taxon_groups": ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-f81c240204", "source": "MIBIG", "source_id": "BGC0001571", "source_label": "demethoxyviridin", "source_version": "3"}]}} |
| support-2313-classification-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/2/owner_document/np_pathway; /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class | supports | Exact versioned computed filing and separately asserted BGC/compound classes. Exact copied saved values: {"/records/2/owner_document/bgc_class": ["TERPENE"], "/records/2/owner_document/np_classification": {"class_results": ["Androstane steroids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Steroids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "/records/2/owner_document/np_pathway": "TERPENOIDS"} |
| support-2313-chemistry | /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/comparisons; /records/2/atom_correspondence | supports | Complete declared representation and original comparisons/map, unchanged. Exact copied saved values: {"/records/2/atom_correspondence": {"complete_atom_count_match": true, "full_graph_identity_established": false, "scope": "One chirality-aware substructure match; no independent full graph or natural identity claim.", "smiles_to_inchi_atom_indices": [0, 18, 13, 5, 12, 20, 9, 6, 23, 17, 15, 16, 22, 14, 10, 3, 1, 7, 8, 2, 4, 11, 19, 21]}, "/records/2/comparisons": {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared": true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal": true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer": true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "/records/2/declared_structure": {"smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi": "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001571"}} |
| support-2313-topology | /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json; /records/2/smiles/computed; /records/2/inchi/computed; /records/2/declared_structure; /records/2/comparisons; /records/2/atom_correspondence | supports | Demethoxyviridin: neutral C19H14O5, 24 atoms/28 bonds, five-ring polycyclic framework, aromatic carbocycle and five-membered oxygen heterocycle, three ketones and one hydroxyl; two specified R tetrahedral centers, all ten comparisons true. |
| support-2313-intake | /private/tmp/npm-review-work/shared-next-batch232/intakes/2313-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake including all input roles, maintained owners and proposed-correction ownership. Exact copied saved values: {"/repository": "CultureBotAI/NaturalProductMech", "/source": {"git_revision": "ce6a5498df5be51116bd5e0c119023ee62bb5464", "inputs": [{"path": ".claude/skills/curate-yaml-record/references/review-checklist.md", "role": "context", "sha256": "13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9"}, {"path": ".claude/skills/review-yaml-record/SKILL.md", "role": "context", "sha256": "493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae"}, {"path": "AGENTS.md", "role": "context", "sha256": "69e4037f8dc97d4b00bb7bb83b41ceca025f6ef578d5c0bf8086f3400becde0b"}, {"path": "conf/id_label_targets.yaml", "role": "context", "sha256": "24235903e0e8df5793a30e92c551082c71c1c67739ea4e3b5fb0f68853a805e6"}, {"path": "conf/producer_evidence.tsv", "role": "context", "sha256": "67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131"}, {"path": "conf/record_review.yaml", "role": "context", "sha256": "e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8"}, {"path": "curation/lotus_occurrence_exclusions.tsv", "role": "context", "sha256": "d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d"}, {"path": "curation/mibig_claim_references.tsv", "role": "context", "sha256": "bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029"}, {"path": "curation/mibig_locus_evidence_overrides.tsv", "role": "context", "sha256": "7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e"}, {"path": "curation/mibig_producer_isolates.tsv", "role": "context", "sha256": "8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8"}, {"path": "curation/mibig_producer_strains.tsv", "role": "context", "sha256": "bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae"}, {"path": "curation/mibig_structure_corrections.tsv", "role": "context", "sha256": "c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0"}, {"path": "curation/mibig_xref_exclusions.tsv", "role": "context", "sha256": "cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c"}, {"path": "data/natural_products/PATHS.tsv", "role": "context", "sha256": "2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3"}, {"path": "data/natural_products/terpenoids/demethoxyviridin.yaml", "role": "target", "sha256": "2227239b32a368e652c7e5fff066173f8b55c69314f101c2fc819175142472ab"}, {"path": "data/raw/MANIFEST.yaml", "role": "context", "sha256": "b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3"}, {"path": "data/raw/antibioticmech_inchikeys.tsv", "role": "context", "sha256": "ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6"}, {"path": "data/raw/bindingdb_targets.tsv", "role": "context", "sha256": "3cff45281c35a8b14d4d7784bc4b7af80e8e27779a5667a0292f0d9b022a22c1"}, {"path": "data/raw/chebi_origins.tsv", "role": "context", "sha256": "fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8"}, {"path": "data/raw/chebi_structures.tsv", "role": "context", "sha256": "62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2"}, {"path": "data/raw/corpus_taxa.obo", "role": "context", "sha256": "8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9"}, {"path": "data/raw/cyanometdb_occurrences.tsv", "role": "context", "sha256": "f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8"}, {"path": "data/raw/lotus_occurrences.tsv", "role": "context", "sha256": "ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94"}, {"path": "data/raw/mibig_compounds.tsv", "role": "context", "sha256": "e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6"}, {"path": "data/raw/npclassifier.tsv", "role": "context", "sha256": "acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3"}, {"path": "data/raw/pubchem_bioassay.tsv", "role": "context", "sha256": "6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b"}, {"path": "docs/CURATION.md", "role": "context", "sha256": "c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa"}, {"path": "docs/HARMONIZATION.md", "role": "context", "sha256": "c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79"}, {"path": "docs/record-review-profile.md", "role": "context", "sha256": "1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a"}, {"path": "docs/record-reviews.md", "role": "context", "sha256": "452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b"}, {"path": "justfile", "role": "context", "sha256": "4f9057e3e54656dd46f2ded4d3a8f0804acad348d2605d436405e1fcfb6af550"}, {"path": "schema/record_review.yaml", "role": "context", "sha256": "229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb"}, {"path": "scripts/extract_chebi.py", "role": "context", "sha256": "46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f"}, {"path": "scripts/extract_mibig.py", "role": "context", "sha256": "e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c"}, {"path": "scripts/seed_from_sources.py", "role": "context", "sha256": "5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5"}, {"path": "src/naturalproductmech/curate/claim_references.py", "role": "context", "sha256": "0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3"}, {"path": "src/naturalproductmech/schema/naturalproductmech.yaml", "role": "context", "sha256": "9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d"}], "state": "working_tree"}, "/status": "inspection_only", "/targets": [{"kind": "generated", "label": "demethoxyviridin", "owner_paths": [{"path": "scripts/seed_from_sources.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained harmonization generator; seeded fields are corrected through maintained inputs and validated regeneration."}, {"path": "data/raw/mibig_compounds.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Retained MIBiG structure, producer and compound-specific locus assertions."}, {"path": "data/raw/npclassifier.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Pinned computed classification and filing assertions."}, {"path": "scripts/extract_mibig.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained extraction of MIBiG compound names, structures, stereochemistry flags and source provenance."}, {"path": "data/raw/lotus_occurrences.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Retained cited occurrence assertions, distinct from demonstrated production."}], "ownership_note": "This review proposes no record edit. Source corrections belong in maintained inventories, implemented curation tables, extractors or the seeder; generated pages are not owners.", "path": "data/natural_products/terpenoids/demethoxyviridin.yaml", "record_class": "NaturalProductRecord", "target_id": "naturalproductmech:mibig-f81c240204"}]} |
| support-2313-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-intake-acceptance-001.json; /status; /accepted | supports | ROOT accepts the ten original canonical intakes; exact per-owner input sets are independently joined. |
| support-2313-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-source-inventory-acceptance-001.json; /status; /accepted | supports | ROOT acceptance of the sole original local inventory; source meanings are separately attributed. |
| support-2313-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-input-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepts the actual input plan; this receipt does not itself establish scientific truth. |
| support-2313-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-diagnostic-acceptance-001.json; /status; /accepted; /comparison_flags_true; /comparison_flags_false; /warning_scope; /scientific_scope; /global_stereo_warnings | supports | ROOT accepts original diagnostics for complete scientific reading: 98 true flags and two Cyslabdan C false flags; six global warnings unassigned. |
| support-2313-native-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-native-gates-acceptance-001.json; /status; /local_checks_passed; /unavailable_required_gates; /all_native_gates_passed | supports | Five original local gates passed. Full QC and complete ontology/OAK gate coverage remain unavailable; all-native-gates-passed is false. |
| support-2313-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-execution-001.json; Whole original diagnostic execution receipt | supports | Native operated the one original diagnostic under ROOT authorization, despite the inherited DATA observer literal. No replay, alternate parse or owner-specific warning attribution is introduced. |
| support-2313-plan | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-target-input-plan-001.json; /records/2; /source_placement_count; /unique_source_path_count | supports | Complete accepted per-owner plan with 37 actual source placements; cohort totals 436 placements / 75 paths. |
| support-2313-source-notes | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json; /reading; /cautions; /scientific_limits | supports | Joint complete source reading/carry attribution and source-specific cautions; source observations precede scientific adjudication. |
| support-2313-curation-scope | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json; /curation | supports | BGC performed one bounded 101-literal scan across eight directly opened implemented curation tables including ignored files, finding zero textual hits. This is not a global absence claim; reserved decisions.tsv was unconsumed. |
| support-2313-source-routes | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/matched_chebi_ids; /contexts/21/source_scope_inventory/source_taxa; /contexts/21/source_scope_inventory/forward_taxon_merge_matches; /contexts/21/source_scope_inventory/nonorganism_matches; /contexts/21/source_scope_inventory/actual_assay_rows; /contexts/21/source_scope_inventory/blank_AID_sentinels; /contexts/21/source_scope_inventory/related_corpus_rows | supports | Exact saved route metadata; no query replay or transfer from companion mechanisms. Exact copied saved values: {"/contexts/21/source_scope_inventory/actual_assay_rows": [], "/contexts/21/source_scope_inventory/blank_AID_sentinels": [], "/contexts/21/source_scope_inventory/forward_taxon_merge_matches": [], "/contexts/21/source_scope_inventory/matched_chebi_ids": [], "/contexts/21/source_scope_inventory/nonorganism_matches": [], "/contexts/21/source_scope_inventory/related_corpus_rows": [], "/contexts/21/source_scope_inventory/source_taxa": ["NCBITaxon:1897413", "NCBITaxon:455034"]} |
| support-2313-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/10; /cached_taxonomy/whole_stanzas/15 | supports | All applicable cached stanzas copied in full. These local labels/synonyms are not fresh taxonomic verification. Exact copied saved values: {"/cached_taxonomy/whole_stanzas/10": {"complete_stanza": "[Term]\nid: NCBITaxon:455034\nname: Hypoxylon hinnuleum\nsynonym: \"Nodulisporium hinnuleum\" EXACT []\n\n", "id": "NCBITaxon:455034", "physical_line": 95223}, "/cached_taxonomy/whole_stanzas/15": {"complete_stanza": "[Term]\nid: NCBITaxon:1897413\nname: Nodulisporium sp.\n\n", "id": "NCBITaxon:1897413", "physical_line": 140473}} |
| support-2313-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/mibig_compounds | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/mibig_compounds": {"matches": [{"last_physical_line": 1874, "physical_line": 1874, "raw_tsv_record": "BGC0001571\t3\tactive\tquestionable\tunknown\tdemethoxyviridin\t1\tC[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O\tInChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1\tSWJBYJJNDIXFSA-KUHUBIRLSA-N\ttrue\t\t\tNCBITaxon:1897413\tNodulisporium sp.\tterpene\tUnknown\tMG886384.1\t1\t66332\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:29743477\tENTRY\n", "row": {"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "demethoxyviridin", "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "MG886384.1", "locus_evidence_methods": "", "locus_from": "1", "locus_to": "66332", "mibig_accession": "BGC0001571", "primary_reference": "PMID:29743477", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi": "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:1897413", "taxon_label": "Nodulisporium sp."}, "row_sha256": "8144985c72b96df87468eaa7bc0de02bf57373f9064c75d66c7dc28c4d7849f3"}], "predicate": "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}} |
| support-2313-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 1874–1874, row_sha256 8144985c72b96df87468eaa7bc0de02bf57373f9064c75d66c7dc28c4d7849f3 | supports | Complete retained physical row fields: [{"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "demethoxyviridin", "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "MG886384.1", "locus_evidence_methods": "", "locus_from": "1", "locus_to": "66332", "mibig_accession": "BGC0001571", "primary_reference": "PMID:29743477", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi": "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:1897413", "taxon_label": "Nodulisporium sp."}] |
| support-2313-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/chebi_structures | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/chebi_structures": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}} |
| support-2313-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/lotus_occurrences": {"matches": [{"last_physical_line": 8526, "physical_line": 8526, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tHypoxylon hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q104865594\t10.1039/P19830000867\thttp://www.wikidata.org/entity/Q82955817\n", "row": {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594", "reference_doi": "10.1039/P19830000867", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, "row_sha256": "dcfa05b7c308cd60ba7d3eca750cab7f3c1962e11cb89f7d994d950cb50d2167"}, {"last_physical_line": 8527, "physical_line": 8527, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tNodulisporium hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q10601705\t10.1039/P19830000867\thttp://www.wikidata.org/entity/Q82955817\n", "row": {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705", "reference_doi": "10.1039/P19830000867", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, "row_sha256": "bce877edcc7a59858e4c0c3749d7c8f5b87b912bfc7d4221482f062226334cfc"}, {"last_physical_line": 8528, "physical_line": 8528, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tHypoxylon hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q104865594\t10.1039/P19830000871\thttp://www.wikidata.org/entity/Q82955817\n", "row": {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594", "reference_doi": "10.1039/P19830000871", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, "row_sha256": "82a47e8533c10ee0586c4799cd1805536223d857f2e2c9da0026a5be272e8177"}, {"last_physical_line": 8529, "physical_line": 8529, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tNodulisporium hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q10601705\t10.1039/P19830000871\thttp://www.wikidata.org/entity/Q82955817\n", "row": {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705", "reference_doi": "10.1039/P19830000871", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, "row_sha256": "bfdb25ba095db278e81d5ce02dc733cb3090cd6fe25ad1d4a91251a40f59510e"}, {"last_physical_line": 8530, "physical_line": 8530, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tHypoxylon hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q104865594\t10.1039/P19840000567\thttp://www.wikidata.org/entity/Q82955817\n", "row": {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594", "reference_doi": "10.1039/P19840000567", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, "row_sha256": "de9dce9c7d43b524c48d2683f6ef188798a80d762ac0e26e2ffa2bcfa3b54283"}, {"last_physical_line": 8531, "physical_line": 8531, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tNodulisporium hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q10601705\t10.1039/P19840000567\thttp://www.wikidata.org/entity/Q82955817\n", "row": {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705", "reference_doi": "10.1039/P19840000567", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, "row_sha256": "b4f78db194b2d514a1b57899cb9c371b044695bc36f984fc96545e5d981b5149"}, {"last_physical_line": 8532, "physical_line": 8532, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tHypoxylon hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q104865594\t10.1039/P19850001311\thttp://www.wikidata.org/entity/Q82955817\n", "row": {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594", "reference_doi": "10.1039/P19850001311", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, "row_sha256": "124898b7254b6b1b367be7602f80bd23a13fc3a48f067f27892db3c02859c471"}, {"last_physical_line": 8533, "physical_line": 8533, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tNodulisporium hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q10601705\t10.1039/P19850001311\thttp://www.wikidata.org/entity/Q82955817\n", "row": {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705", "reference_doi": "10.1039/P19850001311", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, "row_sha256": "40ed5966e23b3f3704fdf1db48601c18bc263bce68eb50e04d35e07ba2f02440"}], "predicate": "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}} |
| support-2313-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 8526–8526, row_sha256 dcfa05b7c308cd60ba7d3eca750cab7f3c1962e11cb89f7d994d950cb50d2167; physical lines 8527–8527, row_sha256 bce877edcc7a59858e4c0c3749d7c8f5b87b912bfc7d4221482f062226334cfc; physical lines 8528–8528, row_sha256 82a47e8533c10ee0586c4799cd1805536223d857f2e2c9da0026a5be272e8177; physical lines 8529–8529, row_sha256 bfdb25ba095db278e81d5ce02dc733cb3090cd6fe25ad1d4a91251a40f59510e; physical lines 8530–8530, row_sha256 de9dce9c7d43b524c48d2683f6ef188798a80d762ac0e26e2ffa2bcfa3b54283; physical lines 8531–8531, row_sha256 b4f78db194b2d514a1b57899cb9c371b044695bc36f984fc96545e5d981b5149; physical lines 8532–8532, row_sha256 124898b7254b6b1b367be7602f80bd23a13fc3a48f067f27892db3c02859c471; physical lines 8533–8533, row_sha256 40ed5966e23b3f3704fdf1db48601c18bc263bce68eb50e04d35e07ba2f02440 | supports | Complete retained physical row fields: [{"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594", "reference_doi": "10.1039/P19830000867", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705", "reference_doi": "10.1039/P19830000867", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594", "reference_doi": "10.1039/P19830000871", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705", "reference_doi": "10.1039/P19830000871", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594", "reference_doi": "10.1039/P19840000567", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705", "reference_doi": "10.1039/P19840000567", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594", "reference_doi": "10.1039/P19850001311", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705", "reference_doi": "10.1039/P19850001311", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}] |
| support-2313-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/cyanometdb_occurrences": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}} |
| support-2313-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/npclassifier | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/npclassifier": {"matches": [{"last_physical_line": 2307, "physical_line": 2307, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tC[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O\tTerpenoids\tSteroids\tAndrostane steroids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results": "Androstane steroids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "superclass_results": "Steroids"}, "row_sha256": "1597d3246dd7938bbf2dadeb3cc425291b5f5b273437cf19e3a103f7140393bd"}], "predicate": "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}} |
| support-2313-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 2307–2307, row_sha256 1597d3246dd7938bbf2dadeb3cc425291b5f5b273437cf19e3a103f7140393bd | supports | Complete retained physical row fields: [{"class_results": "Androstane steroids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "superclass_results": "Steroids"}] |
| support-2313-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/pubchem_bioassay": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}} |
| support-2313-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/bindingdb_targets": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}} |
| support-2313-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/antibioticmech_inchikeys": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}} |
| support-2313-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/chebi_origins | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/chebi_origins": {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows", "query": []}} |
| support-2313-direct-contexts | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /records/2/direct_companion_paths; /records/2/direct_companion_predicates | supports | Exact direct context planning; shared key/locus scope does not transfer identity, experiment or mechanism. Exact copied saved values: {"/records/2/direct_companion_paths": [], "/records/2/direct_companion_predicates": []} |
| support-2313-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /records/2/direct_companion_paths | supports | Complete raw/history and source scope for declared direct companions remains context only; exact whole-reading carry is in source notes. Metadata: [] |
| support-2313-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 175–200; lines 368–435 | supports | Schema distinguishes source SMILES, normalized-key limitations, undefined stereocenters, versioned computed classification and source BGC class. |
| support-2313-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 145–174 | supports | Maintained source extractor derives stereo_complete from unassigned tetrahedral chiral centers of source SMILES. This read-only predicate inspection does not execute it or establish natural stereochemistry. |
| support-2313-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 296–307; lines 982–1020 | supports | Maintained seeder preserves source structure fields and all versioned NPClassifier arrays; filing follows the returned pathway array. No seeder run occurred for scientific authoring. |
| support-2313-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | Scientific dimensions, independent claims and partial completion remain required; local gates are not scientific proof. |
| support-2313-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current review skill under the absolute user no-outbound constraint | supports | Read-only review and evidence ownership are preserved; no source records or native status/history are edited. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-232/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-232/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-232/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-232/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-232/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. No external identifier, publication, taxonomy or natural stereochemical assignment was refreshed under the absolute no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original local gates and successful stored parses establish only their stated mechanical scope.
- Empty joins concern exact saved predicates and snapshots. Shared loci, taxa or citations do not transfer compound-specific identity, production, activity or mechanism.
- Six original omitted-undefined-stereo warnings remain global and unassigned. No additional molecular/YAML parse, source query or target invocation occurred during scientific authoring.
- No source record, native curation status or history is edited. Any later correction belongs to maintained owners listed in the actual canonical intake.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Whole first-five raw/history and actual capture were personally read. Assigned saved-source scope and exact prior companion carries are attributed in the pinned Support reading receipt and joint source notes.
- Support personally read all ten saved forms: 246 atom and 266 bond rows plus every scalar, stereo, ring, motif and original comparison/map. Cyslabdan C has a separately documented explicit manual table witness; it does not replace the diagnostic map.
- ROOT operated original activation/capture, inventory/composer and canonical intakes; Native operated original local gates and molecular diagnostic. Scientific authoring invoked none of these targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T233838Z-demethoxyviridin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: demethoxyviridin'
started_at: '2026-11-03T23:01:25.981463Z'
finished_at: '2026-11-03T23:38:38.959008Z'
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
summary: Demethoxyviridin preserves the retained C19 structure and distinct unresolved
  producer versus species-level occurrence scope. Eight LOTUS rows reduce to four
  taxon–reference pairs; they are not eight independent experiments. Scientific completion
  remains partial.
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
  - path: data/natural_products/terpenoids/demethoxyviridin.yaml
    sha256: 2227239b32a368e652c7e5fff066173f8b55c69314f101c2fc819175142472ab
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
  selection: Campaign path order 2313; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-f81c240204
targets:
- target_id: naturalproductmech:mibig-f81c240204
  path: data/natural_products/terpenoids/demethoxyviridin.yaml
  label: demethoxyviridin
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
  - naturalproductmech:mibig-f81c240204
  command: just validate-strict data/natural_products/terpenoids/cyslabdan-c.yaml
    data/natural_products/terpenoids/dehydrobotrydienol.yaml data/natural_products/terpenoids/demethoxyviridin.yaml
    data/natural_products/terpenoids/desacetylfusarochromene.yaml data/natural_products/terpenoids/deschloro-merochlorin-a.yaml
    data/natural_products/terpenoids/deschloro-merochlorin-b.yaml data/natural_products/terpenoids/dichloro-merochlorin-b.yaml
    data/natural_products/terpenoids/dihydrobotrydial.yaml data/natural_products/terpenoids/ent-kauren-16alpha-ol-2.yaml
    data/natural_products/terpenoids/ent-kauren-16alpha-ol.yaml --workers 1 --out
    /private/tmp/npm-native-checks/batch-232/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-f81c240204
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-232/validate-all-001.tsv
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
  - naturalproductmech:mibig-f81c240204
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
  - naturalproductmech:mibig-f81c240204
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
  - naturalproductmech:mibig-f81c240204
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-232/review-queue-001.tsv
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
  - naturalproductmech:mibig-f81c240204
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-f81c240204
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-f81c240204
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2313-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/demethoxyviridin.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Complete current owner, including all 2 history entries; native curation_status
    remains SEEDED. Full raw reading/carry attribution is preserved in source notes.
  snapshot_sha256: 2227239b32a368e652c7e5fff066173f8b55c69314f101c2fc819175142472ab
- evidence_id: support-2313-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/2
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete captured owner and strict mechanism-absence scope; no selected
    reader applies. Exact copied saved values: {"/records/2": {"component_captures":
    [], "mechanism_capture_scope": "raw_owner_and_declared_components_only_not_maintained_resolution",
    "order": 2313, "owner_document": {"bgc_class": ["TERPENE"], "biosynthesis_origin":
    "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001571",
    "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "3", "evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001571 entry version
    3; citation taken from the entry level", "reference": "PMID:29743477"}], "genome_accession":
    "genbank:MG886384.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from":
    1, "locus_to": 66332, "organism_label": "Nodulisporium sp.", "organism_taxon_id":
    "NCBITaxon:1897413"}], "chemical_structure": {"smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O",
    "standard_inchi": "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001571"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:13Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:25Z"}],
    "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares
    this structure, so the record keeps a content-hashed identifier.", "grounding_status":
    "MINTED", "identifier": "naturalproductmech:mibig-f81c240204", "label": "demethoxyviridin",
    "np_classification": {"class_results": ["Androstane steroids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Steroids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["FUNGAL"], "occurrences":
    [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1039/P19830000867"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source":
    "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1039/P19830000871"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594",
    "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1039/P19840000567"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594",
    "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1039/P19850001311"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594",
    "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster":
    "mibig:BGC0001571", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0001571 entry version 3; citation taken from the entry level", "reference":
    "PMID:29743477"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence:
    none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades
    the taxon claim, which is a different question.", "source": "MIBIG", "source_version":
    "3", "taxon_id": "NCBITaxon:1897413", "taxon_label": "Nodulisporium sp."}], "producer_taxon_groups":
    ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-f81c240204",
    "source": "MIBIG", "source_id": "BGC0001571", "source_label": "demethoxyviridin",
    "source_version": "3"}]}, "owner_pin": {"bytes": 4238, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/demethoxyviridin.yaml",
    "sha256": "2227239b32a368e652c7e5fff066173f8b55c69314f101c2fc819175142472ab"},
    "path": "data/natural_products/terpenoids/demethoxyviridin.yaml", "read_finished_at":
    "2026-11-03T23:01:25.983431Z", "read_started_at": "2026-11-03T23:01:25.981463Z"}}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2313-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/2/owner_document/identifier; /records/2/owner_document/label;
    /records/2/owner_document/chemical_structure; /records/2/owner_document/grounding_status;
    /records/2/owner_document/grounding_notes; /records/2/owner_document/source_concepts
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Exact written identity/grounding fields; absent optional fields are not
    invented. Exact copied saved values: {"/records/2/owner_document/chemical_structure":
    {"smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi":
    "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001571"}, "/records/2/owner_document/grounding_notes":
    "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.", "/records/2/owner_document/grounding_status": "MINTED", "/records/2/owner_document/identifier":
    "naturalproductmech:mibig-f81c240204", "/records/2/owner_document/label": "demethoxyviridin",
    "/records/2/owner_document/source_concepts": [{"minted_identifier": "naturalproductmech:mibig-f81c240204",
    "source": "MIBIG", "source_id": "BGC0001571", "source_label": "demethoxyviridin",
    "source_version": "3"}]}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2313-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters;
    /records/2/owner_document/producer_taxon_groups
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Exact separately graded source producer and locus fields. Exact copied
    saved values: {"/records/2/owner_document/biosynthetic_gene_clusters": [{"accession":
    "mibig:BGC0001571", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version":
    "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001571
    entry version 3; citation taken from the entry level", "reference": "PMID:29743477"}],
    "genome_accession": "genbank:MG886384.1", "link_evidence_basis": "CLUSTER_UNSTATED",
    "locus_from": 1, "locus_to": 66332, "organism_label": "Nodulisporium sp.", "organism_taxon_id":
    "NCBITaxon:1897413"}], "/records/2/owner_document/producer_organisms": [{"biosynthetic_gene_cluster":
    "mibig:BGC0001571", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0001571 entry version 3; citation taken from the entry level", "reference":
    "PMID:29743477"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence:
    none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades
    the taxon claim, which is a different question.", "source": "MIBIG", "source_version":
    "3", "taxon_id": "NCBITaxon:1897413", "taxon_label": "Nodulisporium sp."}], "/records/2/owner_document/producer_taxon_groups":
    ["FUNGAL"]}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2313-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/2/owner_document/occurrences; /records/2/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Written occurrence scope, distinct from production. Whole owner selector
    also proves absence when no occurrence field exists. Exact copied saved values:
    {"/records/2/owner_document/occurrence_taxon_groups": ["FUNGAL"], "/records/2/owner_document/occurrences":
    [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1039/P19830000867"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source":
    "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1039/P19830000871"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594",
    "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1039/P19840000567"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594",
    "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1039/P19850001311"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594",
    "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}]}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2313-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Written activity/target scope; whole owner selector proves absent optional
    roots without a global absence claim. Exact copied saved values: {"/records/2/owner_document":
    {"bgc_class": ["TERPENE"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters":
    [{"accession": "mibig:BGC0001571", "bgc_class": ["TERPENE"], "entry_status": "active",
    "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0001571 entry version 3; citation taken from the entry level", "reference":
    "PMID:29743477"}], "genome_accession": "genbank:MG886384.1", "link_evidence_basis":
    "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 66332, "organism_label": "Nodulisporium
    sp.", "organism_taxon_id": "NCBITaxon:1897413"}], "chemical_structure": {"smiles":
    "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi":
    "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001571"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:13Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:25Z"}],
    "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares
    this structure, so the record keeps a content-hashed identifier.", "grounding_status":
    "MINTED", "identifier": "naturalproductmech:mibig-f81c240204", "label": "demethoxyviridin",
    "np_classification": {"class_results": ["Androstane steroids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Steroids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "occurrence_taxon_groups": ["FUNGAL"], "occurrences":
    [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference
    triple. LOTUS reports that the compound was found in the organism; it does not
    assert that the organism produces it.", "reference": "DOI:10.1039/P19830000867"}],
    "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594", "source":
    "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1039/P19830000871"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594",
    "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1039/P19840000567"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594",
    "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}, {"evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound
    was found in the organism; it does not assert that the organism produces it.",
    "reference": "DOI:10.1039/P19850001311"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q104865594",
    "source": "LOTUS", "taxon_id": "NCBITaxon:455034", "taxon_label": "Hypoxylon hinnuleum",
    "taxon_source": "NCBITaxon"}], "producer_organisms": [{"biosynthetic_gene_cluster":
    "mibig:BGC0001571", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0001571 entry version 3; citation taken from the entry level", "reference":
    "PMID:29743477"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence:
    none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades
    the taxon claim, which is a different question.", "source": "MIBIG", "source_version":
    "3", "taxon_id": "NCBITaxon:1897413", "taxon_label": "Nodulisporium sp."}], "producer_taxon_groups":
    ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-f81c240204",
    "source": "MIBIG", "source_id": "BGC0001571", "source_label": "demethoxyviridin",
    "source_version": "3"}]}}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2313-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_pathway; /records/2/owner_document/np_classification;
    /records/2/owner_document/bgc_class
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Exact versioned computed filing and separately asserted BGC/compound classes.
    Exact copied saved values: {"/records/2/owner_document/bgc_class": ["TERPENE"],
    "/records/2/owner_document/np_classification": {"class_results": ["Androstane
    steroids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results":
    ["Steroids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "/records/2/owner_document/np_pathway": "TERPENOIDS"}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2313-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/comparisons; /records/2/atom_correspondence
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete declared representation and original comparisons/map, unchanged.
    Exact copied saved values: {"/records/2/atom_correspondence": {"complete_atom_count_match":
    true, "full_graph_identity_established": false, "scope": "One chirality-aware
    substructure match; no independent full graph or natural identity claim.", "smiles_to_inchi_atom_indices":
    [0, 18, 13, 5, 12, 20, 9, 6, 23, 17, 15, 16, 22, 14, 10, 3, 1, 7, 8, 2, 4, 11,
    19, 21]}, "/records/2/comparisons": {"atom_count_equal": true, "bond_count_equal":
    true, "both_keys_equal_declared": true, "canonical_isomeric_smiles_equal": true,
    "canonical_nonisomeric_smiles_equal": true, "formal_charge_equal": true, "formula_equal":
    true, "smiles_formula_equals_literal_InChI_main_layer": true, "standard_inchi_equal":
    true, "standard_inchi_key_equal": true}, "/records/2/declared_structure": {"smiles":
    "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O", "standard_inchi":
    "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001571"}}'
  snapshot_sha256: 24e1f67161d916573d35a6640775a2330ce09969f6fc115611f39275865549b9
- evidence_id: support-2313-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/smiles/computed; /records/2/inchi/computed; /records/2/declared_structure;
    /records/2/comparisons; /records/2/atom_correspondence
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Demethoxyviridin: neutral C19H14O5, 24 atoms/28 bonds, five-ring polycyclic
    framework, aromatic carbocycle and five-membered oxygen heterocycle, three ketones
    and one hydroxyl; two specified R tetrahedral centers, all ten comparisons true.'
  snapshot_sha256: 24e1f67161d916573d35a6640775a2330ce09969f6fc115611f39275865549b9
- evidence_id: support-2313-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/intakes/2313-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Actual canonical intake including all input roles, maintained owners and
    proposed-correction ownership. Exact copied saved values: {"/repository": "CultureBotAI/NaturalProductMech",
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
    {"path": "data/natural_products/terpenoids/demethoxyviridin.yaml", "role": "target",
    "sha256": "2227239b32a368e652c7e5fff066173f8b55c69314f101c2fc819175142472ab"},
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
    "generated", "label": "demethoxyviridin", "owner_paths": [{"path": "scripts/seed_from_sources.py",
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
    generated pages are not owners.", "path": "data/natural_products/terpenoids/demethoxyviridin.yaml",
    "record_class": "NaturalProductRecord", "target_id": "naturalproductmech:mibig-f81c240204"}]}'
  snapshot_sha256: 562bb60d51f6db3ec1739d3f7054e771af427c30151ab0511cf37a7d91ed97dd
- evidence_id: support-2313-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-intake-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: ROOT accepts the ten original canonical intakes; exact per-owner input
    sets are independently joined.
  snapshot_sha256: 8fcc103949fe722e55e277ca6ebd8c7e6a91535ced87dcc906209bd397b5a926
- evidence_id: support-2313-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-source-inventory-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: ROOT acceptance of the sole original local inventory; source meanings are
    separately attributed.
  snapshot_sha256: 1be82b2a714236a0bf38785ec588e0dbc35d6d0c52e614aa4dc66faf9e19742f
- evidence_id: support-2313-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-input-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: ROOT accepts the actual input plan; this receipt does not itself establish
    scientific truth.
  snapshot_sha256: ac91e6edf46b06471c00f82f4e414d90618c1520b4a4634518c4b2ac43f43630
- evidence_id: support-2313-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /comparison_flags_true; /comparison_flags_false; /warning_scope;
    /scientific_scope; /global_stereo_warnings
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'ROOT accepts original diagnostics for complete scientific reading: 98
    true flags and two Cyslabdan C false flags; six global warnings unassigned.'
  snapshot_sha256: 7b2881f00f40f445f7f8a07b77560f80516976679c6c7ab7bdc5a0d6bbbf42c1
- evidence_id: support-2313-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-native-gates-acceptance-001.json
  locator: /status; /local_checks_passed; /unavailable_required_gates; /all_native_gates_passed
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Five original local gates passed. Full QC and complete ontology/OAK gate
    coverage remain unavailable; all-native-gates-passed is false.
  snapshot_sha256: a95313b79d0a1105500acbfbd4cd8633d3878a9fd0176bdb2130446ee881a049
- evidence_id: support-2313-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-execution-001.json
  locator: Whole original diagnostic execution receipt
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Native operated the one original diagnostic under ROOT authorization, despite
    the inherited DATA observer literal. No replay, alternate parse or owner-specific
    warning attribution is introduced.
  snapshot_sha256: 15c8254e0158f96b799ce154e0da4573fcbab5d68a0220d3ae7d9e58b1363a58
- evidence_id: support-2313-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-target-input-plan-001.json
  locator: /records/2; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Complete accepted per-owner plan with 37 actual source placements; cohort
    totals 436 placements / 75 paths.
  snapshot_sha256: 94f01db8f3a55101c987af4aa40300302ac195827d11910711925264210ed158
- evidence_id: support-2313-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Joint complete source reading/carry attribution and source-specific cautions;
    source observations precede scientific adjudication.
  snapshot_sha256: 725071a2a2a8f19fa72422d9eefda4482682b9ae2ccc4471cbc38618a7f38a25
- evidence_id: support-2313-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json
  locator: /curation
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: BGC performed one bounded 101-literal scan across eight directly opened
    implemented curation tables including ignored files, finding zero textual hits.
    This is not a global absence claim; reserved decisions.tsv was unconsumed.
  snapshot_sha256: 725071a2a2a8f19fa72422d9eefda4482682b9ae2ccc4471cbc38618a7f38a25
- evidence_id: support-2313-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/matched_chebi_ids; /contexts/21/source_scope_inventory/source_taxa;
    /contexts/21/source_scope_inventory/forward_taxon_merge_matches; /contexts/21/source_scope_inventory/nonorganism_matches;
    /contexts/21/source_scope_inventory/actual_assay_rows; /contexts/21/source_scope_inventory/blank_AID_sentinels;
    /contexts/21/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Exact saved route metadata; no query replay or transfer from companion
    mechanisms. Exact copied saved values: {"/contexts/21/source_scope_inventory/actual_assay_rows":
    [], "/contexts/21/source_scope_inventory/blank_AID_sentinels": [], "/contexts/21/source_scope_inventory/forward_taxon_merge_matches":
    [], "/contexts/21/source_scope_inventory/matched_chebi_ids": [], "/contexts/21/source_scope_inventory/nonorganism_matches":
    [], "/contexts/21/source_scope_inventory/related_corpus_rows": [], "/contexts/21/source_scope_inventory/source_taxa":
    ["NCBITaxon:1897413", "NCBITaxon:455034"]}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/10; /cached_taxonomy/whole_stanzas/15
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'All applicable cached stanzas copied in full. These local labels/synonyms
    are not fresh taxonomic verification. Exact copied saved values: {"/cached_taxonomy/whole_stanzas/10":
    {"complete_stanza": "[Term]\nid: NCBITaxon:455034\nname: Hypoxylon hinnuleum\nsynonym:
    \"Nodulisporium hinnuleum\" EXACT []\n\n", "id": "NCBITaxon:455034", "physical_line":
    95223}, "/cached_taxonomy/whole_stanzas/15": {"complete_stanza": "[Term]\nid:
    NCBITaxon:1897413\nname: Nodulisporium sp.\n\n", "id": "NCBITaxon:1897413", "physical_line":
    140473}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/mibig_compounds":
    {"matches": [{"last_physical_line": 1874, "physical_line": 1874, "raw_tsv_record":
    "BGC0001571\t3\tactive\tquestionable\tunknown\tdemethoxyviridin\t1\tC[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O\tInChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1\tSWJBYJJNDIXFSA-KUHUBIRLSA-N\ttrue\t\t\tNCBITaxon:1897413\tNodulisporium
    sp.\tterpene\tUnknown\tMG886384.1\t1\t66332\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:29743477\tENTRY\n",
    "row": {"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis":
    "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name":
    "demethoxyviridin", "database_ids": "", "entry_completeness": "unknown", "entry_quality":
    "questionable", "entry_status": "active", "entry_version": "3", "genome_accession":
    "MG886384.1", "locus_evidence_methods": "", "locus_from": "1", "locus_to": "66332",
    "mibig_accession": "BGC0001571", "primary_reference": "PMID:29743477", "producer_evidence_basis":
    "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O",
    "standard_inchi": "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:1897413", "taxon_label": "Nodulisporium sp."}, "row_sha256":
    "8144985c72b96df87468eaa7bc0de02bf57373f9064c75d66c7dc28c4d7849f3"}], "predicate":
    "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 1874–1874, row_sha256 8144985c72b96df87468eaa7bc0de02bf57373f9064c75d66c7dc28c4d7849f3
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"bgc_classes": "terpene", "bgc_subclasses":
    "Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes":
    "", "compound_index": "1", "compound_name": "demethoxyviridin", "database_ids":
    "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status":
    "active", "entry_version": "3", "genome_accession": "MG886384.1", "locus_evidence_methods":
    "", "locus_from": "1", "locus_to": "66332", "mibig_accession": "BGC0001571", "primary_reference":
    "PMID:29743477", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis":
    "ENTRY", "smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O",
    "standard_inchi": "InChI=1S/C19H14O5/c1-19-11-4-2-8-9(3-5-12(8)20)15(11)17(23)18-16(19)10(7-24-18)13(21)6-14(19)22/h2,4,7,14,22H,3,5-6H2,1H3/t14-,19+/m1/s1",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:1897413", "taxon_label": "Nodulisporium sp."}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2313-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/chebi_structures":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/lotus_occurrences":
    {"matches": [{"last_physical_line": 8526, "physical_line": 8526, "raw_tsv_record":
    "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tHypoxylon hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q104865594\t10.1039/P19830000867\thttp://www.wikidata.org/entity/Q82955817\n",
    "row": {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594",
    "reference_doi": "10.1039/P19830000867", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id":
    "NCBITaxon:455034"}, "row_sha256": "dcfa05b7c308cd60ba7d3eca750cab7f3c1962e11cb89f7d994d950cb50d2167"},
    {"last_physical_line": 8527, "physical_line": 8527, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tNodulisporium
    hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q10601705\t10.1039/P19830000867\thttp://www.wikidata.org/entity/Q82955817\n",
    "row": {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705",
    "reference_doi": "10.1039/P19830000867", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id":
    "NCBITaxon:455034"}, "row_sha256": "bce877edcc7a59858e4c0c3749d7c8f5b87b912bfc7d4221482f062226334cfc"},
    {"last_physical_line": 8528, "physical_line": 8528, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tHypoxylon
    hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q104865594\t10.1039/P19830000871\thttp://www.wikidata.org/entity/Q82955817\n",
    "row": {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594",
    "reference_doi": "10.1039/P19830000871", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id":
    "NCBITaxon:455034"}, "row_sha256": "82a47e8533c10ee0586c4799cd1805536223d857f2e2c9da0026a5be272e8177"},
    {"last_physical_line": 8529, "physical_line": 8529, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tNodulisporium
    hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q10601705\t10.1039/P19830000871\thttp://www.wikidata.org/entity/Q82955817\n",
    "row": {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705",
    "reference_doi": "10.1039/P19830000871", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id":
    "NCBITaxon:455034"}, "row_sha256": "bfdb25ba095db278e81d5ce02dc733cb3090cd6fe25ad1d4a91251a40f59510e"},
    {"last_physical_line": 8530, "physical_line": 8530, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tHypoxylon
    hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q104865594\t10.1039/P19840000567\thttp://www.wikidata.org/entity/Q82955817\n",
    "row": {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594",
    "reference_doi": "10.1039/P19840000567", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id":
    "NCBITaxon:455034"}, "row_sha256": "de9dce9c7d43b524c48d2683f6ef188798a80d762ac0e26e2ffa2bcfa3b54283"},
    {"last_physical_line": 8531, "physical_line": 8531, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tNodulisporium
    hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q10601705\t10.1039/P19840000567\thttp://www.wikidata.org/entity/Q82955817\n",
    "row": {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705",
    "reference_doi": "10.1039/P19840000567", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id":
    "NCBITaxon:455034"}, "row_sha256": "b4f78db194b2d514a1b57899cb9c371b044695bc36f984fc96545e5d981b5149"},
    {"last_physical_line": 8532, "physical_line": 8532, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tHypoxylon
    hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q104865594\t10.1039/P19850001311\thttp://www.wikidata.org/entity/Q82955817\n",
    "row": {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594",
    "reference_doi": "10.1039/P19850001311", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id":
    "NCBITaxon:455034"}, "row_sha256": "124898b7254b6b1b367be7602f80bd23a13fc3a48f067f27892db3c02859c471"},
    {"last_physical_line": 8533, "physical_line": 8533, "raw_tsv_record": "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tNodulisporium
    hinnuleum\tNCBITaxon:455034\thttp://www.wikidata.org/entity/Q10601705\t10.1039/P19850001311\thttp://www.wikidata.org/entity/Q82955817\n",
    "row": {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705",
    "reference_doi": "10.1039/P19850001311", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id":
    "NCBITaxon:455034"}, "row_sha256": "40ed5966e23b3f3704fdf1db48601c18bc263bce68eb50e04d35e07ba2f02440"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 8526–8526, row_sha256 dcfa05b7c308cd60ba7d3eca750cab7f3c1962e11cb89f7d994d950cb50d2167;
    physical lines 8527–8527, row_sha256 bce877edcc7a59858e4c0c3749d7c8f5b87b912bfc7d4221482f062226334cfc;
    physical lines 8528–8528, row_sha256 82a47e8533c10ee0586c4799cd1805536223d857f2e2c9da0026a5be272e8177;
    physical lines 8529–8529, row_sha256 bfdb25ba095db278e81d5ce02dc733cb3090cd6fe25ad1d4a91251a40f59510e;
    physical lines 8530–8530, row_sha256 de9dce9c7d43b524c48d2683f6ef188798a80d762ac0e26e2ffa2bcfa3b54283;
    physical lines 8531–8531, row_sha256 b4f78db194b2d514a1b57899cb9c371b044695bc36f984fc96545e5d981b5149;
    physical lines 8532–8532, row_sha256 124898b7254b6b1b367be7602f80bd23a13fc3a48f067f27892db3c02859c471;
    physical lines 8533–8533, row_sha256 40ed5966e23b3f3704fdf1db48601c18bc263bce68eb50e04d35e07ba2f02440
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"organism_name": "Hypoxylon hinnuleum",
    "organism_wikidata": "http://www.wikidata.org/entity/Q104865594", "reference_doi":
    "10.1039/P19830000867", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata":
    "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, {"organism_name":
    "Nodulisporium hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q10601705",
    "reference_doi": "10.1039/P19830000867", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id":
    "NCBITaxon:455034"}, {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata":
    "http://www.wikidata.org/entity/Q104865594", "reference_doi": "10.1039/P19830000871",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817",
    "taxon_id": "NCBITaxon:455034"}, {"organism_name": "Nodulisporium hinnuleum",
    "organism_wikidata": "http://www.wikidata.org/entity/Q10601705", "reference_doi":
    "10.1039/P19830000871", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata":
    "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}, {"organism_name":
    "Hypoxylon hinnuleum", "organism_wikidata": "http://www.wikidata.org/entity/Q104865594",
    "reference_doi": "10.1039/P19840000567", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q82955817", "taxon_id":
    "NCBITaxon:455034"}, {"organism_name": "Nodulisporium hinnuleum", "organism_wikidata":
    "http://www.wikidata.org/entity/Q10601705", "reference_doi": "10.1039/P19840000567",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817",
    "taxon_id": "NCBITaxon:455034"}, {"organism_name": "Hypoxylon hinnuleum", "organism_wikidata":
    "http://www.wikidata.org/entity/Q104865594", "reference_doi": "10.1039/P19850001311",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q82955817",
    "taxon_id": "NCBITaxon:455034"}, {"organism_name": "Nodulisporium hinnuleum",
    "organism_wikidata": "http://www.wikidata.org/entity/Q10601705", "reference_doi":
    "10.1039/P19850001311", "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "structure_wikidata":
    "http://www.wikidata.org/entity/Q82955817", "taxon_id": "NCBITaxon:455034"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2313-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/cyanometdb_occurrences":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/npclassifier":
    {"matches": [{"last_physical_line": 2307, "physical_line": 2307, "raw_tsv_record":
    "SWJBYJJNDIXFSA-KUHUBIRLSA-N\tC[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O\tTerpenoids\tSteroids\tAndrostane
    steroids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results":
    "Androstane steroids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "superclass_results": "Steroids"},
    "row_sha256": "1597d3246dd7938bbf2dadeb3cc425291b5f5b273437cf19e3a103f7140393bd"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 2307–2307, row_sha256 1597d3246dd7938bbf2dadeb3cc425291b5f5b273437cf19e3a103f7140393bd
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"class_results": "Androstane
    steroids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "C[C@]12[C@@H](CC(=O)C3=COC(=C31)C(=O)C4=C2C=CC5=C4CCC5=O)O",
    "standard_inchi_key": "SWJBYJJNDIXFSA-KUHUBIRLSA-N", "superclass_results": "Steroids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2313-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/pubchem_bioassay":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/bindingdb_targets":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/antibioticmech_inchikeys":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "SWJBYJJNDIXFSA-KUHUBIRLSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/21/source_scope_inventory/joins/chebi_origins":
    {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows",
    "query": []}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /records/2/direct_companion_paths; /records/2/direct_companion_predicates
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Exact direct context planning; shared key/locus scope does not transfer
    identity, experiment or mechanism. Exact copied saved values: {"/records/2/direct_companion_paths":
    [], "/records/2/direct_companion_predicates": []}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /records/2/direct_companion_paths
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete raw/history and source scope for declared direct companions remains
    context only; exact whole-reading carry is in source notes. Metadata: []'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2313-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 175–200; lines 368–435
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Schema distinguishes source SMILES, normalized-key limitations, undefined
    stereocenters, versioned computed classification and source BGC class.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2313-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 145–174
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Maintained source extractor derives stereo_complete from unassigned tetrahedral
    chiral centers of source SMILES. This read-only predicate inspection does not
    execute it or establish natural stereochemistry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2313-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 296–307; lines 982–1020
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Maintained seeder preserves source structure fields and all versioned NPClassifier
    arrays; filing follows the returned pathway array. No seeder run occurred for
    scientific authoring.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2313-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Scientific dimensions, independent claims and partial completion remain
    required; local gates are not scientific proof.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2313-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current review skill under the absolute user no-outbound constraint
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Read-only review and evidence ownership are preserved; no source records
    or native status/history are edited.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-232/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json
  accessed_at: '2026-11-03T23:06:58.212721Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 8f5917ea73bc1cfaff0acd36b896a8bf563a39d9fa0c06095a640ade8a7f0eb5
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-232/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json
  accessed_at: '2026-11-03T23:07:23.062519Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 905f0c596112665df821aae49a7d58f13c781433d2bbd42c17b090f83c29ba07
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-232/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json
  accessed_at: '2026-11-03T23:07:42.545614Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-232/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json
  accessed_at: '2026-11-03T23:08:16.218635Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-232/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json
  accessed_at: '2026-11-03T23:08:27.888600Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 135ad5a077a12b8b149dc037f520fc077338ad6bf40df6dfb82dc6c51e9e139b
assessments:
- assessment_id: support-2313-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The minted identifier preserves SWJBYJJNDIXFSA-KUHUBIRLSA-N and the literal
    demethoxyviridin label from BGC0001571 version 3, compound index 1. The exact
    saved ChEBI structure join is empty. No direct full-key or owned-BGC companion
    is selected for this owner; source identity is not inferred from a similar name
    or a normalized key alone.
  target_ids:
  - naturalproductmech:mibig-f81c240204
  evidence_ids:
  - support-2313-grounding-owner
  - support-2313-source-mibig_compounds
  - support-2313-query-chebi_structures
  - support-2313-chemistry
  - support-2313-direct-contexts
  - support-2313-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: SWJBYJJNDIXFSA-KUHUBIRLSA-N; exact retained full key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - support-2313-grounding-owner
    - support-2313-source-mibig_compounds
    - support-2313-query-chebi_structures
    - support-2313-chemistry
    - support-2313-direct-contexts
    - support-2313-companion-boundaries
  - name: grounding_scope
    value: MINTED, complete retained key and empty exact ChEBI join; no external identity
      verification.
    definition: Local retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2313-grounding-owner
    - support-2313-source-mibig_compounds
    - support-2313-query-chebi_structures
    - support-2313-chemistry
    - support-2313-direct-contexts
    - support-2313-companion-boundaries
- assessment_id: support-2313-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both saved forms are neutral C19H14O5 with 24 atoms and 28 bonds, a five-ring
    polycyclic framework including an aromatic carbocycle and five-membered oxygen
    heterocycle, three ketones and one hydroxyl. Two R tetrahedral centers are specified.
    All ten comparison flags are true and the original chirality-aware map is complete,
    while full_graph_identity_established is false. The source true stereo flag is
    consistent with these stored centers; this is local representation agreement,
    not a fresh experimental stereochemical assignment.
  target_ids:
  - naturalproductmech:mibig-f81c240204
  evidence_ids:
  - support-2313-grounding-owner
  - support-2313-chemistry
  - support-2313-topology
  - support-2313-diagnostic-acceptance
  - support-2313-structure-schema
  - support-2313-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Two specified R tetrahedra; source true flag is consistent with saved representation,
      not natural stereochemical proof.
    definition: Complete saved stereo/atom/bond interpretation; no new parse or experimental
      assignment.
    evidence_ids:
    - support-2313-grounding-owner
    - support-2313-chemistry
    - support-2313-topology
    - support-2313-diagnostic-acceptance
    - support-2313-structure-schema
    - support-2313-stereo-method
  - name: representation_correspondence
    value: All ten comparisons true and complete original correspondence; full_graph_identity_established
      false.
    definition: Normalized identifier agreement does not establish fixed-graph or
      natural-form identity.
    evidence_ids:
    - support-2313-grounding-owner
    - support-2313-chemistry
    - support-2313-topology
    - support-2313-diagnostic-acceptance
    - support-2313-structure-schema
    - support-2313-stereo-method
- assessment_id: support-2313-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: Nodulisporium sp. NCBITaxon:1897413 is an unresolved source producer assertion,
    recorded as SOURCE_ASSERTION with CLUSTER_UNSTATED and no locus method. BGC0001571
    version 3 is active, questionable and of unknown completeness. LOTUS occurrences
    at NCBITaxon:455034 do not resolve the producer to that species. The whole local
    455034 cache stanza names Hypoxylon hinnuleum and lists Nodulisporium hinnuleum
    as a synonym; the separate 1897413 cached label remains Nodulisporium sp.
  target_ids:
  - naturalproductmech:mibig-f81c240204
  evidence_ids:
  - support-2313-origin-owner
  - support-2313-source-mibig_compounds
  - support-2313-cached-taxonomy
  - support-2313-source-routes
  - support-2313-direct-contexts
  - support-2313-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: Unresolved producer 1897413 remains distinct from occurrence species 455034
      and its two retained synonymous names.
    definition: Producer, occurrence, species, strain and unresolved labels retain
      their separate scope; cached labels are not fresh authority.
    evidence_ids:
    - support-2313-origin-owner
    - support-2313-source-mibig_compounds
    - support-2313-cached-taxonomy
    - support-2313-source-routes
    - support-2313-direct-contexts
    - support-2313-companion-boundaries
  - name: producer_evidence
    value: SOURCE_ASSERTION, Nodulisporium sp.; no independent species/strain identification.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - support-2313-origin-owner
    - support-2313-source-mibig_compounds
    - support-2313-cached-taxonomy
    - support-2313-source-routes
    - support-2313-direct-contexts
    - support-2313-companion-boundaries
  - name: locus_evidence
    value: BGC0001571 version 3, CLUSTER_UNSTATED, no method; active/questionable/unknown
      metadata.
    definition: Source version/status/method/grade is not a complete pathway or fresh
      primary verification.
    evidence_ids:
    - support-2313-origin-owner
    - support-2313-source-mibig_compounds
    - support-2313-cached-taxonomy
    - support-2313-source-routes
    - support-2313-direct-contexts
    - support-2313-companion-boundaries
- assessment_id: support-2313-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: PMID:29743477 is ENTRY-level MIBiG provenance. Four distinct LOTUS DOI
    strings—10.1039/P19830000867, 10.1039/P19830000871, 10.1039/P19840000567 and 10.1039/P19850001311—support
    occurrence placements only. Repeated names and rows do not create independent
    experimental replication, and none of those occurrence citations is silently promoted
    to the producer/locus citation.
  target_ids:
  - naturalproductmech:mibig-f81c240204
  evidence_ids:
  - support-2313-origin-owner
  - support-2313-occurrence-owner
  - support-2313-source-mibig_compounds
  - support-2313-source-notes
  - support-2313-direct-contexts
  - support-2313-companion-boundaries
  - support-2313-source-lotus_occurrences
  dimensions:
  - name: citation_scope
    value: ENTRY PMID:29743477; four separate LOTUS DOI strings retain occurrence-only
      roles.
    definition: Database provenance and occurrence citations retain distinct roles;
      no publication independence or fresh source access is assumed.
    evidence_ids:
    - support-2313-origin-owner
    - support-2313-occurrence-owner
    - support-2313-source-mibig_compounds
    - support-2313-source-notes
    - support-2313-direct-contexts
    - support-2313-companion-boundaries
    - support-2313-source-lotus_occurrences
- assessment_id: support-2313-activity
  area: evidence
  topic: Activity
  outcome: supported
  summary: Eight exact LOTUS rows contain two name placements for each of four identical
    taxon 455034/literal-DOI pairs. The owner correctly writes four occurrences. This
    identity-based collapse preserves the four citation scopes without claiming eight
    experiments or equating 455034 to unresolved producer 1897413. There is no written
    assay or target, and all exact saved activity/target, ChEBI-origin and CyanometDB
    joins are empty; no inactivity inference follows.
  target_ids:
  - naturalproductmech:mibig-f81c240204
  evidence_ids:
  - support-2313-occurrence-owner
  - support-2313-assay-owner
  - support-2313-source-routes
  - support-2313-cached-taxonomy
  - support-2313-query-lotus_occurrences
  - support-2313-query-chebi_origins
  - support-2313-query-cyanometdb_occurrences
  - support-2313-query-pubchem_bioassay
  - support-2313-query-bindingdb_targets
  - support-2313-query-antibioticmech_inchikeys
  - support-2313-direct-contexts
  - support-2313-companion-boundaries
  dimensions:
  - name: occurrence_scope
    value: Eight saved rows collapse to four exact taxon–literal-reference pairs and
      four written occurrences, not eight independent studies.
    definition: Occurrence placements are not counts of independent experiments or
      demonstrated producers.
    evidence_ids:
    - support-2313-occurrence-owner
    - support-2313-assay-owner
    - support-2313-source-routes
    - support-2313-cached-taxonomy
    - support-2313-query-lotus_occurrences
    - support-2313-query-chebi_origins
    - support-2313-query-cyanometdb_occurrences
    - support-2313-query-pubchem_bioassay
    - support-2313-query-bindingdb_targets
    - support-2313-query-antibioticmech_inchikeys
    - support-2313-direct-contexts
    - support-2313-companion-boundaries
  - name: assay_target_scope
    value: No written bioactivity/target and exact retained assay/target joins empty;
      no inactivity or global absence inference.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - support-2313-occurrence-owner
    - support-2313-assay-owner
    - support-2313-source-routes
    - support-2313-cached-taxonomy
    - support-2313-query-lotus_occurrences
    - support-2313-query-chebi_origins
    - support-2313-query-cyanometdb_occurrences
    - support-2313-query-pubchem_bioassay
    - support-2313-query-bindingdb_targets
    - support-2313-query-antibioticmech_inchikeys
    - support-2313-direct-contexts
    - support-2313-companion-boundaries
- assessment_id: support-2313-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: NPClassifier retains Terpenoids / Steroids / Androstane steroids and is_glycoside:false
    at version npclassifier.gnps2.org@2026-09-07. Source TERPENE and subclass Unknown
    are distinct from this model label. The saved C19 polycyclic, oxygen-heterocyclic
    topology and lack of a sugar residue support a bounded applicability discussion,
    not an experimentally demonstrated steroid pathway or a change to source identity.
  target_ids:
  - naturalproductmech:mibig-f81c240204
  evidence_ids:
  - support-2313-classification-owner
  - support-2313-source-mibig_compounds
  - support-2313-source-npclassifier
  - support-2313-chemistry
  - support-2313-topology
  - support-2313-structure-schema
  - support-2313-classification-seeder
  - support-2313-direct-contexts
  - support-2313-companion-boundaries
  dimensions:
  - name: classification_applicability
    value: Versioned Androstane steroids/false glycoside is a computed filing assertion,
      distinct from source TERPENE/Unknown.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct evidence types.
    evidence_ids:
    - support-2313-classification-owner
    - support-2313-source-mibig_compounds
    - support-2313-source-npclassifier
    - support-2313-chemistry
    - support-2313-topology
    - support-2313-structure-schema
    - support-2313-classification-seeder
    - support-2313-direct-contexts
    - support-2313-companion-boundaries
- assessment_id: support-2313-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: All twelve scientific dimensions were assessed against the complete current
    owner/history, actual canonical intake, complete retained source scope and both
    saved molecular forms. Five original local gates passed; full QC, complete OAK
    authority coverage and fresh primary/taxonomic verification remain unavailable.
    This owner has no declared mechanism root, component or selected maintained reader.
    The bounded eight-table curation scan found no exact cohort-token hit; no supported
    new maintained-source correction is established. Scientific completion remains
    partial and native curation status/history remain unchanged.
  target_ids:
  - naturalproductmech:mibig-f81c240204
  evidence_ids:
  - support-2313-owner
  - support-2313-capture
  - support-2313-intake
  - support-2313-intake-acceptance
  - support-2313-inventory-acceptance
  - support-2313-plan
  - support-2313-plan-acceptance
  - support-2313-source-notes
  - support-2313-curation-scope
  - support-2313-diagnostic-execution
  - support-2313-diagnostic-acceptance
  - support-2313-native-acceptance
  - support-2313-review-profile
  - support-2313-review-skill
  - support-2313-query-mibig_compounds
  - support-2313-query-chebi_structures
  - support-2313-query-lotus_occurrences
  - support-2313-query-cyanometdb_occurrences
  - support-2313-query-npclassifier
  - support-2313-query-pubchem_bioassay
  - support-2313-query-bindingdb_targets
  - support-2313-query-antibioticmech_inchikeys
  - support-2313-query-chebi_origins
  dimensions:
  - name: review_completion
    value: 'Partial: retained evidence only, unavailable full QC/OAK and unresolved
      fresh primary/taxonomic/natural stereochemical verification. No native status
      promotion.'
    definition: Completion reflects actual evidence access and required-check coverage;
      parsing and gate success are not scientific proof.
    evidence_ids:
    - support-2313-owner
    - support-2313-capture
    - support-2313-intake
    - support-2313-intake-acceptance
    - support-2313-inventory-acceptance
    - support-2313-plan
    - support-2313-plan-acceptance
    - support-2313-source-notes
    - support-2313-curation-scope
    - support-2313-diagnostic-execution
    - support-2313-diagnostic-acceptance
    - support-2313-native-acceptance
    - support-2313-review-profile
    - support-2313-review-skill
    - support-2313-query-mibig_compounds
    - support-2313-query-chebi_structures
    - support-2313-query-lotus_occurrences
    - support-2313-query-cyanometdb_occurrences
    - support-2313-query-npclassifier
    - support-2313-query-pubchem_bioassay
    - support-2313-query-bindingdb_targets
    - support-2313-query-antibioticmech_inchikeys
    - support-2313-query-chebi_origins
findings: []
actions: []
limitations:
- All evidence is retained locally. No external identifier, publication, taxonomy
  or natural stereochemical assignment was refreshed under the absolute no-request
  instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original local gates
  and successful stored parses establish only their stated mechanical scope.
- Empty joins concern exact saved predicates and snapshots. Shared loci, taxa or citations
  do not transfer compound-specific identity, production, activity or mechanism.
- Six original omitted-undefined-stereo warnings remain global and unassigned. No
  additional molecular/YAML parse, source query or target invocation occurred during
  scientific authoring.
- No source record, native curation status or history is edited. Any later correction
  belongs to maintained owners listed in the actual canonical intake.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Whole first-five raw/history and actual capture were personally read. Assigned saved-source
  scope and exact prior companion carries are attributed in the pinned Support reading
  receipt and joint source notes.
- 'Support personally read all ten saved forms: 246 atom and 266 bond rows plus every
  scalar, stereo, ring, motif and original comparison/map. Cyslabdan C has a separately
  documented explicit manual table witness; it does not replace the diagnostic map.'
- ROOT operated original activation/capture, inventory/composer and canonical intakes;
  Native operated original local gates and molecular diagnostic. Scientific authoring
  invoked none of these targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-232
```
