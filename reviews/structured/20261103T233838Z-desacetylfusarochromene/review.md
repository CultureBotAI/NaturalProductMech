# Local evidence review: desacetylfusarochromene

- Review: 20261103T233838Z-desacetylfusarochromene
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T23:01:25.983456Z
- Finished UTC: 2026-11-03T23:38:38.969514Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Desacetylfusarochromene retains a partial-stereochemistry structure and separately declared NRPS/OTHER source versus Merohemiterpenoids prediction. Current evidence supports no source correction; scientific completion remains partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2314; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-da909f5425 | data/natural_products/terpenoids/desacetylfusarochromene.yaml | generated | desacetylfusarochromene |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-da909f5425 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-da909f5425 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-da909f5425 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-da909f5425 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-da909f5425 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-da909f5425 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-da909f5425 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-da909f5425 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-da909f5425.

The literal label desacetylfusarochromene and full key PCIHXARFCRKZMV-UHFFFAOYSA-N match BGC0002256 version 3, compound index 2. The record is MINTED and the exact saved ChEBI join is empty. Fusarochromene, 4-hydroxykynurenine and Fusarochromanone are direct locus context with distinct complete keys and source assertions; their folder locations, names or occurrence evidence are not identity substitutes.

### Representation

representation: supported. Targets: naturalproductmech:mibig-da909f5425.

Both forms are neutral C15H20N2O3 with 20 atoms and 21 bonds. Complete tables show an aromatic ring joined to an unsaturated oxygen heterocycle, a ketone-bearing side chain, two primary amino groups and terminal alcohol. The amino-alcohol side-chain tetrahedron is unspecified in both forms, consistent with stereo_complete:false and the unassigned stereo block of the key. All ten comparisons are true and the original substructure correspondence is complete, but full_graph_identity_established is false. The single cyclic C–O–C bridge does not establish a sugar or glycosidic linkage, and matching partially specified forms do not identify the natural stereoisomer.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-da909f5425.

Fusarium equiseti NCBITaxon:61235 is SOURCE_ASSERTION from BGC0002256 version 3. The locus has no stated method and remains CLUSTER_UNSTATED; active/questionable/unknown are retained source metadata. Companion occurrences in F. sacchari, F. roseum or F. equiseti do not create an occurrence or production experiment for this exact full key.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-da909f5425.

PMID:33107888 is ENTRY-level source provenance shared across the BGC0002256 compounds. It is not converted into a purified-enzyme experiment or a compound-specific activity assertion. Separate companion LOTUS citations remain attached to their own full keys; no citation transfer is warranted.

### Activity

evidence: supported. Targets: naturalproductmech:mibig-da909f5425.

No occurrence, bioactivity or molecular target is written for this owner. Its exact saved LOTUS, ChEBI-origin, CyanometDB, PubChem, BindingDB and sibling-corpus activity joins are empty. This is a bounded retained-source absence, not evidence of inactivity or universal biological absence.

### Classification

consistency: supported. Targets: naturalproductmech:mibig-da909f5425.

The retained model is Terpenoids / Meroterpenoids / Merohemiterpenoids with is_glycoside:false at npclassifier.gnps2.org@2026-09-07. The source BGC classes NRPS and OTHER and subclasses Type I and other concern locus classification, not a competing experimental molecular-class assignment. The gem-dimethyl oxygen heterocycle and amino-ketone side chain permit a limited topology discussion; the model filing is neither a newly demonstrated pathway nor grounds to edit the source record.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-da909f5425.

All twelve scientific dimensions were assessed against the complete current owner/history, actual canonical intake, complete retained source scope and both saved molecular forms. Five original local gates passed; full QC, complete OAK authority coverage and fresh primary/taxonomic verification remain unavailable. This owner has no declared mechanism root, component or selected maintained reader. The bounded eight-table curation scan found no exact cohort-token hit; no supported new maintained-source correction is established. Scientific completion remains partial and native curation status/history remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2314-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/desacetylfusarochromene.yaml; Whole current owner plaintext and complete curation_history | supports | Complete current owner, including all 2 history entries; native curation_status remains SEEDED. Full raw reading/carry attribution is preserved in source notes. |
| support-2314-capture | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/3 | supports | Complete captured owner and strict mechanism-absence scope; no selected reader applies. Exact copied saved values: {"/records/3": {"component_captures": [], "mechanism_capture_scope": "raw_owner_and_declared_components_only_not_maintained_resolution", "order": 2314, "owner_document": {"bgc_class": ["NRPS", "OTHER"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256", "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id": "NCBITaxon:61235"}], "chemical_structure": {"smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": false, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:11Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:03Z"}], "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "grounding_status": "MINTED", "identifier": "naturalproductmech:mibig-da909f5425", "label": "desacetylfusarochromene", "np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "producer_taxon_groups": ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-da909f5425", "source": "MIBIG", "source_id": "BGC0002256", "source_label": "desacetylfusarochromene", "source_version": "3"}]}, "owner_pin": {"bytes": 2434, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/desacetylfusarochromene.yaml", "sha256": "0ce3c89b56843eacfcf535c67a34a84b798ecf99a5d4c70da5824b334997a021"}, "path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml", "read_finished_at": "2026-11-03T23:01:25.984675Z", "read_started_at": "2026-11-03T23:01:25.983456Z"}} |
| support-2314-grounding-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/3/owner_document/identifier; /records/3/owner_document/label; /records/3/owner_document/chemical_structure; /records/3/owner_document/grounding_status; /records/3/owner_document/grounding_notes; /records/3/owner_document/source_concepts | supports | Exact written identity/grounding fields; absent optional fields are not invented. Exact copied saved values: {"/records/3/owner_document/chemical_structure": {"smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": false, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "/records/3/owner_document/grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "/records/3/owner_document/grounding_status": "MINTED", "/records/3/owner_document/identifier": "naturalproductmech:mibig-da909f5425", "/records/3/owner_document/label": "desacetylfusarochromene", "/records/3/owner_document/source_concepts": [{"minted_identifier": "naturalproductmech:mibig-da909f5425", "source": "MIBIG", "source_id": "BGC0002256", "source_label": "desacetylfusarochromene", "source_version": "3"}]} |
| support-2314-origin-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters; /records/3/owner_document/producer_taxon_groups | supports | Exact separately graded source producer and locus fields. Exact copied saved values: {"/records/3/owner_document/biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256", "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id": "NCBITaxon:61235"}], "/records/3/owner_document/producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "/records/3/owner_document/producer_taxon_groups": ["FUNGAL"]} |
| support-2314-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/3/owner_document | supports | Written occurrence scope, distinct from production. Whole owner selector also proves absence when no occurrence field exists. Exact copied saved values: {"/records/3/owner_document": {"bgc_class": ["NRPS", "OTHER"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256", "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id": "NCBITaxon:61235"}], "chemical_structure": {"smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": false, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:11Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:03Z"}], "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "grounding_status": "MINTED", "identifier": "naturalproductmech:mibig-da909f5425", "label": "desacetylfusarochromene", "np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "producer_taxon_groups": ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-da909f5425", "source": "MIBIG", "source_id": "BGC0002256", "source_label": "desacetylfusarochromene", "source_version": "3"}]}} |
| support-2314-assay-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/3/owner_document | supports | Written activity/target scope; whole owner selector proves absent optional roots without a global absence claim. Exact copied saved values: {"/records/3/owner_document": {"bgc_class": ["NRPS", "OTHER"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256", "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id": "NCBITaxon:61235"}], "chemical_structure": {"smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": false, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:11Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:03Z"}], "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.", "grounding_status": "MINTED", "identifier": "naturalproductmech:mibig-da909f5425", "label": "desacetylfusarochromene", "np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS", "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "producer_taxon_groups": ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-da909f5425", "source": "MIBIG", "source_id": "BGC0002256", "source_label": "desacetylfusarochromene", "source_version": "3"}]}} |
| support-2314-classification-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/3/owner_document/np_pathway; /records/3/owner_document/np_classification; /records/3/owner_document/bgc_class | supports | Exact versioned computed filing and separately asserted BGC/compound classes. Exact copied saved values: {"/records/3/owner_document/bgc_class": ["NRPS", "OTHER"], "/records/3/owner_document/np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "/records/3/owner_document/np_pathway": "TERPENOIDS"} |
| support-2314-chemistry | /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json; /records/3/declared_structure; /records/3/comparisons; /records/3/atom_correspondence | supports | Complete declared representation and original comparisons/map, unchanged. Exact copied saved values: {"/records/3/atom_correspondence": {"complete_atom_count_match": true, "full_graph_identity_established": false, "scope": "One chirality-aware substructure match; no independent full graph or natural identity claim.", "smiles_to_inchi_atom_indices": [0, 14, 1, 5, 4, 10, 12, 3, 2, 9, 11, 6, 8, 15, 7, 17, 18, 13, 16, 19]}, "/records/3/comparisons": {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared": true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal": true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer": true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "/records/3/declared_structure": {"smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": false, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}} |
| support-2314-topology | /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/declared_structure; /records/3/comparisons; /records/3/atom_correspondence | supports | Desacetylfusarochromene: neutral C15H20N2O3, 20 atoms/21 bonds, aromatic ring/unsaturated oxygen heterocycle, ketone side chain, two primary amines and terminal alcohol. One unspecified tetrahedral center matches retained stereo_complete:false; all ten comparisons true. An oxygen bridge does not itself identify a sugar. |
| support-2314-intake | /private/tmp/npm-review-work/shared-next-batch232/intakes/2314-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake including all input roles, maintained owners and proposed-correction ownership. Exact copied saved values: {"/repository": "CultureBotAI/NaturalProductMech", "/source": {"git_revision": "ce6a5498df5be51116bd5e0c119023ee62bb5464", "inputs": [{"path": ".claude/skills/curate-yaml-record/references/review-checklist.md", "role": "context", "sha256": "13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9"}, {"path": ".claude/skills/review-yaml-record/SKILL.md", "role": "context", "sha256": "493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae"}, {"path": "AGENTS.md", "role": "context", "sha256": "69e4037f8dc97d4b00bb7bb83b41ceca025f6ef578d5c0bf8086f3400becde0b"}, {"path": "conf/id_label_targets.yaml", "role": "context", "sha256": "24235903e0e8df5793a30e92c551082c71c1c67739ea4e3b5fb0f68853a805e6"}, {"path": "conf/producer_evidence.tsv", "role": "context", "sha256": "67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131"}, {"path": "conf/record_review.yaml", "role": "context", "sha256": "e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8"}, {"path": "curation/lotus_occurrence_exclusions.tsv", "role": "context", "sha256": "d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d"}, {"path": "curation/mibig_claim_references.tsv", "role": "context", "sha256": "bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029"}, {"path": "curation/mibig_locus_evidence_overrides.tsv", "role": "context", "sha256": "7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e"}, {"path": "curation/mibig_producer_isolates.tsv", "role": "context", "sha256": "8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8"}, {"path": "curation/mibig_producer_strains.tsv", "role": "context", "sha256": "bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae"}, {"path": "curation/mibig_structure_corrections.tsv", "role": "context", "sha256": "c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0"}, {"path": "curation/mibig_xref_exclusions.tsv", "role": "context", "sha256": "cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c"}, {"path": "data/natural_products/PATHS.tsv", "role": "context", "sha256": "2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3"}, {"path": "data/natural_products/alkaloids/fusarochromene.yaml", "role": "context", "sha256": "f653a81c04f30502862e365013fef6947eb101c9b2d3594bf2ac1db978709812"}, {"path": "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "role": "context", "sha256": "e76125d04ba9f83d969ab51a0fa4d4886ba3d4ff92e9a2860274a2f74e98cd86"}, {"path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml", "role": "target", "sha256": "0ce3c89b56843eacfcf535c67a34a84b798ecf99a5d4c70da5824b334997a021"}, {"path": "data/natural_products/terpenoids/fusarochromanone.yaml", "role": "context", "sha256": "5d8adf4a61d8d941b042d0efb089a113fdab1f54296b6cbc5b915490669f9a2b"}, {"path": "data/raw/MANIFEST.yaml", "role": "context", "sha256": "b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3"}, {"path": "data/raw/antibioticmech_inchikeys.tsv", "role": "context", "sha256": "ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6"}, {"path": "data/raw/bindingdb_targets.tsv", "role": "context", "sha256": "3cff45281c35a8b14d4d7784bc4b7af80e8e27779a5667a0292f0d9b022a22c1"}, {"path": "data/raw/chebi_origins.tsv", "role": "context", "sha256": "fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8"}, {"path": "data/raw/chebi_structures.tsv", "role": "context", "sha256": "62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2"}, {"path": "data/raw/corpus_taxa.obo", "role": "context", "sha256": "8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9"}, {"path": "data/raw/cyanometdb_occurrences.tsv", "role": "context", "sha256": "f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8"}, {"path": "data/raw/lotus_occurrences.tsv", "role": "context", "sha256": "ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94"}, {"path": "data/raw/mibig_compounds.tsv", "role": "context", "sha256": "e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6"}, {"path": "data/raw/npclassifier.tsv", "role": "context", "sha256": "acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3"}, {"path": "data/raw/pubchem_bioassay.tsv", "role": "context", "sha256": "6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b"}, {"path": "docs/CURATION.md", "role": "context", "sha256": "c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa"}, {"path": "docs/HARMONIZATION.md", "role": "context", "sha256": "c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79"}, {"path": "docs/record-review-profile.md", "role": "context", "sha256": "1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a"}, {"path": "docs/record-reviews.md", "role": "context", "sha256": "452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b"}, {"path": "justfile", "role": "context", "sha256": "4f9057e3e54656dd46f2ded4d3a8f0804acad348d2605d436405e1fcfb6af550"}, {"path": "schema/record_review.yaml", "role": "context", "sha256": "229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb"}, {"path": "scripts/extract_chebi.py", "role": "context", "sha256": "46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f"}, {"path": "scripts/extract_mibig.py", "role": "context", "sha256": "e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c"}, {"path": "scripts/seed_from_sources.py", "role": "context", "sha256": "5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5"}, {"path": "src/naturalproductmech/curate/claim_references.py", "role": "context", "sha256": "0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3"}, {"path": "src/naturalproductmech/schema/naturalproductmech.yaml", "role": "context", "sha256": "9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d"}], "state": "working_tree"}, "/status": "inspection_only", "/targets": [{"kind": "generated", "label": "desacetylfusarochromene", "owner_paths": [{"path": "scripts/seed_from_sources.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained harmonization generator; seeded fields are corrected through maintained inputs and validated regeneration."}, {"path": "data/raw/mibig_compounds.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Retained MIBiG structure, producer and compound-specific locus assertions."}, {"path": "data/raw/npclassifier.tsv", "repository": "CultureBotAI/NaturalProductMech", "role": "Pinned computed classification and filing assertions."}, {"path": "scripts/extract_mibig.py", "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained extraction of MIBiG compound names, structures, stereochemistry flags and source provenance."}], "ownership_note": "This review proposes no record edit. Source corrections belong in maintained inventories, implemented curation tables, extractors or the seeder; generated pages are not owners.", "path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml", "record_class": "NaturalProductRecord", "target_id": "naturalproductmech:mibig-da909f5425"}]} |
| support-2314-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-intake-acceptance-001.json; /status; /accepted | supports | ROOT accepts the ten original canonical intakes; exact per-owner input sets are independently joined. |
| support-2314-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-source-inventory-acceptance-001.json; /status; /accepted | supports | ROOT acceptance of the sole original local inventory; source meanings are separately attributed. |
| support-2314-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-input-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepts the actual input plan; this receipt does not itself establish scientific truth. |
| support-2314-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-diagnostic-acceptance-001.json; /status; /accepted; /comparison_flags_true; /comparison_flags_false; /warning_scope; /scientific_scope; /global_stereo_warnings | supports | ROOT accepts original diagnostics for complete scientific reading: 98 true flags and two Cyslabdan C false flags; six global warnings unassigned. |
| support-2314-native-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-native-gates-acceptance-001.json; /status; /local_checks_passed; /unavailable_required_gates; /all_native_gates_passed | supports | Five original local gates passed. Full QC and complete ontology/OAK gate coverage remain unavailable; all-native-gates-passed is false. |
| support-2314-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-execution-001.json; Whole original diagnostic execution receipt | supports | Native operated the one original diagnostic under ROOT authorization, despite the inherited DATA observer literal. No replay, alternate parse or owner-specific warning attribution is introduced. |
| support-2314-plan | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-target-input-plan-001.json; /records/3; /source_placement_count; /unique_source_path_count | supports | Complete accepted per-owner plan with 40 actual source placements; cohort totals 436 placements / 75 paths. |
| support-2314-source-notes | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json; /reading; /cautions; /scientific_limits | supports | Joint complete source reading/carry attribution and source-specific cautions; source observations precede scientific adjudication. |
| support-2314-curation-scope | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json; /curation | supports | BGC performed one bounded 101-literal scan across eight directly opened implemented curation tables including ignored files, finding zero textual hits. This is not a global absence claim; reserved decisions.tsv was unconsumed. |
| support-2314-source-routes | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/22/source_scope_inventory/matched_chebi_ids; /contexts/22/source_scope_inventory/source_taxa; /contexts/22/source_scope_inventory/forward_taxon_merge_matches; /contexts/22/source_scope_inventory/nonorganism_matches; /contexts/22/source_scope_inventory/actual_assay_rows; /contexts/22/source_scope_inventory/blank_AID_sentinels; /contexts/22/source_scope_inventory/related_corpus_rows | supports | Exact saved route metadata; no query replay or transfer from companion mechanisms. Exact copied saved values: {"/contexts/22/source_scope_inventory/actual_assay_rows": [], "/contexts/22/source_scope_inventory/blank_AID_sentinels": [], "/contexts/22/source_scope_inventory/forward_taxon_merge_matches": [], "/contexts/22/source_scope_inventory/matched_chebi_ids": [], "/contexts/22/source_scope_inventory/nonorganism_matches": [], "/contexts/22/source_scope_inventory/related_corpus_rows": [], "/contexts/22/source_scope_inventory/source_taxa": ["NCBITaxon:61235"]} |
| support-2314-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/6 | supports | All applicable cached stanzas copied in full. These local labels/synonyms are not fresh taxonomic verification. Exact copied saved values: {"/cached_taxonomy/whole_stanzas/6": {"complete_stanza": "[Term]\nid: NCBITaxon:61235\nname: Fusarium equiseti\nsynonym: \"Gibberella intricans\" EXACT []\nsynonym: \"Selenosporium equiseti\" EXACT []\n\n", "id": "NCBITaxon:61235", "physical_line": 27935}} |
| support-2314-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/22/source_scope_inventory/joins/mibig_compounds | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/mibig_compounds": {"matches": [{"last_physical_line": 2708, "physical_line": 2708, "raw_tsv_record": "BGC0002256\t3\tactive\tquestionable\tunknown\tdesacetylfusarochromene\t2\tCC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1\tInChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3\tPCIHXARFCRKZMV-UHFFFAOYSA-N\tfalse\t\t\tNCBITaxon:61235\tFusarium equiseti\tNRPS&#124;other\tType I&#124;other\tBK013344.1\t1\t23896\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:33107888\tENTRY\n", "row": {"bgc_classes": "NRPS&#124;other", "bgc_subclasses": "Type I&#124;other", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "2", "compound_name": "desacetylfusarochromene", "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "BK013344.1", "locus_evidence_methods": "", "locus_from": "1", "locus_to": "23896", "mibig_accession": "BGC0002256", "primary_reference": "PMID:33107888", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": "false", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}, "row_sha256": "41a54411f2d12cb7b6dcf10a3225d23f97ae065665ce588c352be32f81292ed8"}], "predicate": "exact complete standard_inchi_key equality", "query": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}} |
| support-2314-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2708–2708, row_sha256 41a54411f2d12cb7b6dcf10a3225d23f97ae065665ce588c352be32f81292ed8 | supports | Complete retained physical row fields: [{"bgc_classes": "NRPS&#124;other", "bgc_subclasses": "Type I&#124;other", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "2", "compound_name": "desacetylfusarochromene", "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "BK013344.1", "locus_evidence_methods": "", "locus_from": "1", "locus_to": "23896", "mibig_accession": "BGC0002256", "primary_reference": "PMID:33107888", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": "false", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}] |
| support-2314-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/22/source_scope_inventory/joins/chebi_structures | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/chebi_structures": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}} |
| support-2314-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/22/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/lotus_occurrences": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}} |
| support-2314-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/22/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/cyanometdb_occurrences": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}} |
| support-2314-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/22/source_scope_inventory/joins/npclassifier | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/npclassifier": {"matches": [{"last_physical_line": 1843, "physical_line": 1843, "raw_tsv_record": "PCIHXARFCRKZMV-UHFFFAOYSA-N\tCC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1\tTerpenoids\tMeroterpenoids\tMerohemiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results": "Merohemiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "superclass_results": "Meroterpenoids"}, "row_sha256": "e4df2475c17542602cf70db5505a0f7f14f7a2295c88ed7e5ca1726a884829a6"}], "predicate": "exact complete standard_inchi_key equality", "query": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}} |
| support-2314-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 1843–1843, row_sha256 e4df2475c17542602cf70db5505a0f7f14f7a2295c88ed7e5ca1726a884829a6 | supports | Complete retained physical row fields: [{"class_results": "Merohemiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "superclass_results": "Meroterpenoids"}] |
| support-2314-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/22/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/pubchem_bioassay": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}} |
| support-2314-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/22/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/bindingdb_targets": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}} |
| support-2314-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/22/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/antibioticmech_inchikeys": {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}} |
| support-2314-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/22/source_scope_inventory/joins/chebi_origins | supports | Complete retained exact query frame, including all matches and no-match scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/chebi_origins": {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows", "query": []}} |
| support-2314-direct-contexts | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /records/3/direct_companion_paths; /records/3/direct_companion_predicates | supports | Exact direct context planning; shared key/locus scope does not transfer identity, experiment or mechanism. Exact copied saved values: {"/records/3/direct_companion_paths": ["data/natural_products/alkaloids/fusarochromene.yaml", "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "data/natural_products/terpenoids/fusarochromanone.yaml"], "/records/3/direct_companion_predicates": [{"path": "data/natural_products/alkaloids/fusarochromene.yaml", "same_complete_InChIKey": false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}, {"path": "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "same_complete_InChIKey": false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}, {"path": "data/natural_products/terpenoids/fusarochromanone.yaml", "same_complete_InChIKey": false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}]} |
| support-2314-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/0; /contexts/1; /contexts/29 | supports | Complete raw/history and source scope for declared direct companions remains context only; exact whole-reading carry is in source notes. Metadata: [{"declared_mechanism_roots_literal": [], "history_count": 2, "identifier": "naturalproductmech:mibig-ea1711783a", "input": {"bytes": 2962, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/fusarochromene.yaml", "sha256": "f653a81c04f30502862e365013fef6947eb101c9b2d3594bf2ac1db978709812"}, "label": "fusarochromene", "owned_bgc_ids": ["BGC0002256"], "path": "data/natural_products/alkaloids/fusarochromene.yaml", "standard_inchi_key": "JWWKBOBMBFAOAR-LLVKDONJSA-N"}, {"declared_mechanism_roots_literal": [], "history_count": 2, "identifier": "naturalproductmech:mibig-a896068bf1", "input": {"bytes": 2434, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "sha256": "e76125d04ba9f83d969ab51a0fa4d4886ba3d4ff92e9a2860274a2f74e98cd86"}, "label": "4-hydroxykynurenine", "owned_bgc_ids": ["BGC0002256"], "path": "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "standard_inchi_key": "GNUVAWTWZCFAJG-UHFFFAOYSA-N"}, {"declared_mechanism_roots_literal": [], "history_count": 3, "identifier": "naturalproductmech:mibig-95c375019f", "input": {"bytes": 4391, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/fusarochromanone.yaml", "sha256": "5d8adf4a61d8d941b042d0efb089a113fdab1f54296b6cbc5b915490669f9a2b"}, "label": "fusarochromanone", "owned_bgc_ids": ["BGC0002256"], "path": "data/natural_products/terpenoids/fusarochromanone.yaml", "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N"}] |
| support-2314-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 175–200; lines 368–435 | supports | Schema distinguishes source SMILES, normalized-key limitations, undefined stereocenters, versioned computed classification and source BGC class. |
| support-2314-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 145–174 | supports | Maintained source extractor derives stereo_complete from unassigned tetrahedral chiral centers of source SMILES. This read-only predicate inspection does not execute it or establish natural stereochemistry. |
| support-2314-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 296–307; lines 982–1020 | supports | Maintained seeder preserves source structure fields and all versioned NPClassifier arrays; filing follows the returned pathway array. No seeder run occurred for scientific authoring. |
| support-2314-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | Scientific dimensions, independent claims and partial completion remain required; local gates are not scientific proof. |
| support-2314-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current review skill under the absolute user no-outbound constraint | supports | Read-only review and evidence ownership are preserved; no source records or native status/history are edited. |
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
review_id: 20261103T233838Z-desacetylfusarochromene
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: desacetylfusarochromene'
started_at: '2026-11-03T23:01:25.983456Z'
finished_at: '2026-11-03T23:38:38.969514Z'
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
summary: Desacetylfusarochromene retains a partial-stereochemistry structure and separately
  declared NRPS/OTHER source versus Merohemiterpenoids prediction. Current evidence
  supports no source correction; scientific completion remains partial.
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
    role: target
  - path: data/natural_products/terpenoids/fusarochromanone.yaml
    sha256: 5d8adf4a61d8d941b042d0efb089a113fdab1f54296b6cbc5b915490669f9a2b
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
  selection: Campaign path order 2314; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-da909f5425
targets:
- target_id: naturalproductmech:mibig-da909f5425
  path: data/natural_products/terpenoids/desacetylfusarochromene.yaml
  label: desacetylfusarochromene
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
  - naturalproductmech:mibig-da909f5425
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
  - naturalproductmech:mibig-da909f5425
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
  - naturalproductmech:mibig-da909f5425
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
  - naturalproductmech:mibig-da909f5425
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
  - naturalproductmech:mibig-da909f5425
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
  - naturalproductmech:mibig-da909f5425
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-da909f5425
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-da909f5425
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2314-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/desacetylfusarochromene.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Complete current owner, including all 2 history entries; native curation_status
    remains SEEDED. Full raw reading/carry attribution is preserved in source notes.
  snapshot_sha256: 0ce3c89b56843eacfcf535c67a34a84b798ecf99a5d4c70da5824b334997a021
- evidence_id: support-2314-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/3
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete captured owner and strict mechanism-absence scope; no selected
    reader applies. Exact copied saved values: {"/records/3": {"component_captures":
    [], "mechanism_capture_scope": "raw_owner_and_declared_components_only_not_maintained_resolution",
    "order": 2314, "owner_document": {"bgc_class": ["NRPS", "OTHER"], "biosynthesis_origin":
    "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256",
    "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3",
    "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256
    entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}],
    "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED",
    "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id":
    "NCBITaxon:61235"}], "chemical_structure": {"smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1",
    "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3",
    "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": false,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:11Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:03Z"}],
    "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares
    this structure, so the record keeps a content-hashed identifier.", "grounding_status":
    "MINTED", "identifier": "naturalproductmech:mibig-da909f5425", "label": "desacetylfusarochromene",
    "np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "producer_organisms": [{"biosynthetic_gene_cluster":
    "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference":
    "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence:
    none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades
    the taxon claim, which is a different question.", "source": "MIBIG", "source_version":
    "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "producer_taxon_groups":
    ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-da909f5425",
    "source": "MIBIG", "source_id": "BGC0002256", "source_label": "desacetylfusarochromene",
    "source_version": "3"}]}, "owner_pin": {"bytes": 2434, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/desacetylfusarochromene.yaml",
    "sha256": "0ce3c89b56843eacfcf535c67a34a84b798ecf99a5d4c70da5824b334997a021"},
    "path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml", "read_finished_at":
    "2026-11-03T23:01:25.984675Z", "read_started_at": "2026-11-03T23:01:25.983456Z"}}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2314-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/3/owner_document/identifier; /records/3/owner_document/label;
    /records/3/owner_document/chemical_structure; /records/3/owner_document/grounding_status;
    /records/3/owner_document/grounding_notes; /records/3/owner_document/source_concepts
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Exact written identity/grounding fields; absent optional fields are not
    invented. Exact copied saved values: {"/records/3/owner_document/chemical_structure":
    {"smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3",
    "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": false,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "/records/3/owner_document/grounding_notes":
    "No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.", "/records/3/owner_document/grounding_status": "MINTED", "/records/3/owner_document/identifier":
    "naturalproductmech:mibig-da909f5425", "/records/3/owner_document/label": "desacetylfusarochromene",
    "/records/3/owner_document/source_concepts": [{"minted_identifier": "naturalproductmech:mibig-da909f5425",
    "source": "MIBIG", "source_id": "BGC0002256", "source_label": "desacetylfusarochromene",
    "source_version": "3"}]}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2314-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters;
    /records/3/owner_document/producer_taxon_groups
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Exact separately graded source producer and locus fields. Exact copied
    saved values: {"/records/3/owner_document/biosynthetic_gene_clusters": [{"accession":
    "mibig:BGC0002256", "bgc_class": ["NRPS", "OTHER"], "entry_status": "active",
    "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference":
    "PMID:33107888"}], "genome_accession": "genbank:BK013344.1", "link_evidence_basis":
    "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium
    equiseti", "organism_taxon_id": "NCBITaxon:61235"}], "/records/3/owner_document/producer_organisms":
    [{"biosynthetic_gene_cluster": "mibig:BGC0002256", "evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256 entry version 3; citation taken
    from the entry level", "reference": "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION",
    "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED;
    this field grades the taxon claim, which is a different question.", "source":
    "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:61235", "taxon_label":
    "Fusarium equiseti"}], "/records/3/owner_document/producer_taxon_groups": ["FUNGAL"]}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2314-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Written occurrence scope, distinct from production. Whole owner selector
    also proves absence when no occurrence field exists. Exact copied saved values:
    {"/records/3/owner_document": {"bgc_class": ["NRPS", "OTHER"], "biosynthesis_origin":
    "NATURAL_PRODUCT", "biosynthetic_gene_clusters": [{"accession": "mibig:BGC0002256",
    "bgc_class": ["NRPS", "OTHER"], "entry_status": "active", "entry_version": "3",
    "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0002256
    entry version 3; citation taken from the entry level", "reference": "PMID:33107888"}],
    "genome_accession": "genbank:BK013344.1", "link_evidence_basis": "CLUSTER_UNSTATED",
    "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium equiseti", "organism_taxon_id":
    "NCBITaxon:61235"}], "chemical_structure": {"smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1",
    "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3",
    "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": false,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:11Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:03Z"}],
    "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares
    this structure, so the record keeps a content-hashed identifier.", "grounding_status":
    "MINTED", "identifier": "naturalproductmech:mibig-da909f5425", "label": "desacetylfusarochromene",
    "np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "producer_organisms": [{"biosynthetic_gene_cluster":
    "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference":
    "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence:
    none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades
    the taxon claim, which is a different question.", "source": "MIBIG", "source_version":
    "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "producer_taxon_groups":
    ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-da909f5425",
    "source": "MIBIG", "source_id": "BGC0002256", "source_label": "desacetylfusarochromene",
    "source_version": "3"}]}}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2314-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Written activity/target scope; whole owner selector proves absent optional
    roots without a global absence claim. Exact copied saved values: {"/records/3/owner_document":
    {"bgc_class": ["NRPS", "OTHER"], "biosynthesis_origin": "NATURAL_PRODUCT", "biosynthetic_gene_clusters":
    [{"accession": "mibig:BGC0002256", "bgc_class": ["NRPS", "OTHER"], "entry_status":
    "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION",
    "notes": "MIBiG BGC0002256 entry version 3; citation taken from the entry level",
    "reference": "PMID:33107888"}], "genome_accession": "genbank:BK013344.1", "link_evidence_basis":
    "CLUSTER_UNSTATED", "locus_from": 1, "locus_to": 23896, "organism_label": "Fusarium
    equiseti", "organism_taxon_id": "NCBITaxon:61235"}], "chemical_structure": {"smiles":
    "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3",
    "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": false,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}, "curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-10T05:54:11Z"},
    {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from the committed inventories
    in data/raw/.", "curator": "seed_from_sources", "timestamp": "2026-09-25T03:03:03Z"}],
    "curation_status": "SEEDED", "grounding_notes": "No 3-star ChEBI entry shares
    this structure, so the record keeps a content-hashed identifier.", "grounding_status":
    "MINTED", "identifier": "naturalproductmech:mibig-da909f5425", "label": "desacetylfusarochromene",
    "np_classification": {"class_results": ["Merohemiterpenoids"], "is_glycoside":
    false, "pathway_results": ["Terpenoids"], "superclass_results": ["Meroterpenoids"],
    "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS", "producer_organisms": [{"biosynthetic_gene_cluster":
    "mibig:BGC0002256", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "MIBiG BGC0002256 entry version 3; citation taken from the entry level", "reference":
    "PMID:33107888"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence:
    none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades
    the taxon claim, which is a different question.", "source": "MIBIG", "source_version":
    "3", "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}], "producer_taxon_groups":
    ["FUNGAL"], "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-da909f5425",
    "source": "MIBIG", "source_id": "BGC0002256", "source_label": "desacetylfusarochromene",
    "source_version": "3"}]}}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2314-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_pathway; /records/3/owner_document/np_classification;
    /records/3/owner_document/bgc_class
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Exact versioned computed filing and separately asserted BGC/compound classes.
    Exact copied saved values: {"/records/3/owner_document/bgc_class": ["NRPS", "OTHER"],
    "/records/3/owner_document/np_classification": {"class_results": ["Merohemiterpenoids"],
    "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results":
    ["Meroterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "/records/3/owner_document/np_pathway": "TERPENOIDS"}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: support-2314-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/declared_structure; /records/3/comparisons; /records/3/atom_correspondence
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete declared representation and original comparisons/map, unchanged.
    Exact copied saved values: {"/records/3/atom_correspondence": {"complete_atom_count_match":
    true, "full_graph_identity_established": false, "scope": "One chirality-aware
    substructure match; no independent full graph or natural identity claim.", "smiles_to_inchi_atom_indices":
    [0, 14, 1, 5, 4, 10, 12, 3, 2, 9, 11, 6, 8, 15, 7, 17, 18, 13, 16, 19]}, "/records/3/comparisons":
    {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared":
    true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal":
    true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer":
    true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "/records/3/declared_structure":
    {"smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3",
    "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": false,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0002256"}}'
  snapshot_sha256: 24e1f67161d916573d35a6640775a2330ce09969f6fc115611f39275865549b9
- evidence_id: support-2314-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed; /records/3/inchi/computed; /records/3/declared_structure;
    /records/3/comparisons; /records/3/atom_correspondence
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Desacetylfusarochromene: neutral C15H20N2O3, 20 atoms/21 bonds, aromatic
    ring/unsaturated oxygen heterocycle, ketone side chain, two primary amines and
    terminal alcohol. One unspecified tetrahedral center matches retained stereo_complete:false;
    all ten comparisons true. An oxygen bridge does not itself identify a sugar.'
  snapshot_sha256: 24e1f67161d916573d35a6640775a2330ce09969f6fc115611f39275865549b9
- evidence_id: support-2314-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/intakes/2314-inspect-001.json
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
    {"path": "data/natural_products/alkaloids/fusarochromene.yaml", "role": "context",
    "sha256": "f653a81c04f30502862e365013fef6947eb101c9b2d3594bf2ac1db978709812"},
    {"path": "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml",
    "role": "context", "sha256": "e76125d04ba9f83d969ab51a0fa4d4886ba3d4ff92e9a2860274a2f74e98cd86"},
    {"path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml", "role":
    "target", "sha256": "0ce3c89b56843eacfcf535c67a34a84b798ecf99a5d4c70da5824b334997a021"},
    {"path": "data/natural_products/terpenoids/fusarochromanone.yaml", "role": "context",
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
    "generated", "label": "desacetylfusarochromene", "owner_paths": [{"path": "scripts/seed_from_sources.py",
    "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained harmonization
    generator; seeded fields are corrected through maintained inputs and validated
    regeneration."}, {"path": "data/raw/mibig_compounds.tsv", "repository": "CultureBotAI/NaturalProductMech",
    "role": "Retained MIBiG structure, producer and compound-specific locus assertions."},
    {"path": "data/raw/npclassifier.tsv", "repository": "CultureBotAI/NaturalProductMech",
    "role": "Pinned computed classification and filing assertions."}, {"path": "scripts/extract_mibig.py",
    "repository": "CultureBotAI/NaturalProductMech", "role": "Maintained extraction
    of MIBiG compound names, structures, stereochemistry flags and source provenance."}],
    "ownership_note": "This review proposes no record edit. Source corrections belong
    in maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners.", "path": "data/natural_products/terpenoids/desacetylfusarochromene.yaml",
    "record_class": "NaturalProductRecord", "target_id": "naturalproductmech:mibig-da909f5425"}]}'
  snapshot_sha256: 553c1f1c5ca5cba77ae7641da0f957ee3ae9db700856f06618740e794c147699
- evidence_id: support-2314-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-intake-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: ROOT accepts the ten original canonical intakes; exact per-owner input
    sets are independently joined.
  snapshot_sha256: 8fcc103949fe722e55e277ca6ebd8c7e6a91535ced87dcc906209bd397b5a926
- evidence_id: support-2314-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-source-inventory-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: ROOT acceptance of the sole original local inventory; source meanings are
    separately attributed.
  snapshot_sha256: 1be82b2a714236a0bf38785ec588e0dbc35d6d0c52e614aa4dc66faf9e19742f
- evidence_id: support-2314-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-input-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: ROOT accepts the actual input plan; this receipt does not itself establish
    scientific truth.
  snapshot_sha256: ac91e6edf46b06471c00f82f4e414d90618c1520b4a4634518c4b2ac43f43630
- evidence_id: support-2314-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /comparison_flags_true; /comparison_flags_false; /warning_scope;
    /scientific_scope; /global_stereo_warnings
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'ROOT accepts original diagnostics for complete scientific reading: 98
    true flags and two Cyslabdan C false flags; six global warnings unassigned.'
  snapshot_sha256: 7b2881f00f40f445f7f8a07b77560f80516976679c6c7ab7bdc5a0d6bbbf42c1
- evidence_id: support-2314-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-native-gates-acceptance-001.json
  locator: /status; /local_checks_passed; /unavailable_required_gates; /all_native_gates_passed
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Five original local gates passed. Full QC and complete ontology/OAK gate
    coverage remain unavailable; all-native-gates-passed is false.
  snapshot_sha256: a95313b79d0a1105500acbfbd4cd8633d3878a9fd0176bdb2130446ee881a049
- evidence_id: support-2314-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-execution-001.json
  locator: Whole original diagnostic execution receipt
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Native operated the one original diagnostic under ROOT authorization, despite
    the inherited DATA observer literal. No replay, alternate parse or owner-specific
    warning attribution is introduced.
  snapshot_sha256: 15c8254e0158f96b799ce154e0da4573fcbab5d68a0220d3ae7d9e58b1363a58
- evidence_id: support-2314-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-target-input-plan-001.json
  locator: /records/3; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Complete accepted per-owner plan with 40 actual source placements; cohort
    totals 436 placements / 75 paths.
  snapshot_sha256: 94f01db8f3a55101c987af4aa40300302ac195827d11910711925264210ed158
- evidence_id: support-2314-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Joint complete source reading/carry attribution and source-specific cautions;
    source observations precede scientific adjudication.
  snapshot_sha256: 725071a2a2a8f19fa72422d9eefda4482682b9ae2ccc4471cbc38618a7f38a25
- evidence_id: support-2314-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json
  locator: /curation
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: BGC performed one bounded 101-literal scan across eight directly opened
    implemented curation tables including ignored files, finding zero textual hits.
    This is not a global absence claim; reserved decisions.tsv was unconsumed.
  snapshot_sha256: 725071a2a2a8f19fa72422d9eefda4482682b9ae2ccc4471cbc38618a7f38a25
- evidence_id: support-2314-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/22/source_scope_inventory/matched_chebi_ids; /contexts/22/source_scope_inventory/source_taxa;
    /contexts/22/source_scope_inventory/forward_taxon_merge_matches; /contexts/22/source_scope_inventory/nonorganism_matches;
    /contexts/22/source_scope_inventory/actual_assay_rows; /contexts/22/source_scope_inventory/blank_AID_sentinels;
    /contexts/22/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Exact saved route metadata; no query replay or transfer from companion
    mechanisms. Exact copied saved values: {"/contexts/22/source_scope_inventory/actual_assay_rows":
    [], "/contexts/22/source_scope_inventory/blank_AID_sentinels": [], "/contexts/22/source_scope_inventory/forward_taxon_merge_matches":
    [], "/contexts/22/source_scope_inventory/matched_chebi_ids": [], "/contexts/22/source_scope_inventory/nonorganism_matches":
    [], "/contexts/22/source_scope_inventory/related_corpus_rows": [], "/contexts/22/source_scope_inventory/source_taxa":
    ["NCBITaxon:61235"]}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/6
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'All applicable cached stanzas copied in full. These local labels/synonyms
    are not fresh taxonomic verification. Exact copied saved values: {"/cached_taxonomy/whole_stanzas/6":
    {"complete_stanza": "[Term]\nid: NCBITaxon:61235\nname: Fusarium equiseti\nsynonym:
    \"Gibberella intricans\" EXACT []\nsynonym: \"Selenosporium equiseti\" EXACT []\n\n",
    "id": "NCBITaxon:61235", "physical_line": 27935}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/22/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/mibig_compounds":
    {"matches": [{"last_physical_line": 2708, "physical_line": 2708, "raw_tsv_record":
    "BGC0002256\t3\tactive\tquestionable\tunknown\tdesacetylfusarochromene\t2\tCC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1\tInChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3\tPCIHXARFCRKZMV-UHFFFAOYSA-N\tfalse\t\t\tNCBITaxon:61235\tFusarium
    equiseti\tNRPS|other\tType I|other\tBK013344.1\t1\t23896\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:33107888\tENTRY\n",
    "row": {"bgc_classes": "NRPS|other", "bgc_subclasses": "Type I|other", "cluster_link_evidence_basis":
    "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "2", "compound_name":
    "desacetylfusarochromene", "database_ids": "", "entry_completeness": "unknown",
    "entry_quality": "questionable", "entry_status": "active", "entry_version": "3",
    "genome_accession": "BK013344.1", "locus_evidence_methods": "", "locus_from":
    "1", "locus_to": "23896", "mibig_accession": "BGC0002256", "primary_reference":
    "PMID:33107888", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis":
    "ENTRY", "smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi":
    "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3",
    "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": "false",
    "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}, "row_sha256":
    "41a54411f2d12cb7b6dcf10a3225d23f97ae065665ce588c352be32f81292ed8"}], "predicate":
    "exact complete standard_inchi_key equality", "query": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2708–2708, row_sha256 41a54411f2d12cb7b6dcf10a3225d23f97ae065665ce588c352be32f81292ed8
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"bgc_classes": "NRPS|other",
    "bgc_subclasses": "Type I|other", "cluster_link_evidence_basis": "CLUSTER_UNSTATED",
    "compound_classes": "", "compound_index": "2", "compound_name": "desacetylfusarochromene",
    "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable",
    "entry_status": "active", "entry_version": "3", "genome_accession": "BK013344.1",
    "locus_evidence_methods": "", "locus_from": "1", "locus_to": "23896", "mibig_accession":
    "BGC0002256", "primary_reference": "PMID:33107888", "producer_evidence_basis":
    "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1",
    "standard_inchi": "InChI=1S/C15H20N2O3/c1-15(2)6-5-11-13(20-15)4-3-10(14(11)17)12(19)7-9(16)8-18/h3-6,9,18H,7-8,16-17H2,1-2H3",
    "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "stereo_complete": "false",
    "taxon_id": "NCBITaxon:61235", "taxon_label": "Fusarium equiseti"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2314-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/22/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/chebi_structures":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "PCIHXARFCRKZMV-UHFFFAOYSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/22/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/lotus_occurrences":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "PCIHXARFCRKZMV-UHFFFAOYSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/22/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/cyanometdb_occurrences":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "PCIHXARFCRKZMV-UHFFFAOYSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/22/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/npclassifier":
    {"matches": [{"last_physical_line": 1843, "physical_line": 1843, "raw_tsv_record":
    "PCIHXARFCRKZMV-UHFFFAOYSA-N\tCC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1\tTerpenoids\tMeroterpenoids\tMerohemiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n",
    "row": {"class_results": "Merohemiterpenoids", "is_glycoside": "false", "model_version":
    "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles":
    "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1", "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N",
    "superclass_results": "Meroterpenoids"}, "row_sha256": "e4df2475c17542602cf70db5505a0f7f14f7a2295c88ed7e5ca1726a884829a6"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "PCIHXARFCRKZMV-UHFFFAOYSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 1843–1843, row_sha256 e4df2475c17542602cf70db5505a0f7f14f7a2295c88ed7e5ca1726a884829a6
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained physical row fields: [{"class_results": "Merohemiterpenoids",
    "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "CC1(C)C=CC2=C(C=CC(C(CC(N)CO)=O)=C2N)O1",
    "standard_inchi_key": "PCIHXARFCRKZMV-UHFFFAOYSA-N", "superclass_results": "Meroterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2314-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/22/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/pubchem_bioassay":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "PCIHXARFCRKZMV-UHFFFAOYSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/22/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/bindingdb_targets":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "PCIHXARFCRKZMV-UHFFFAOYSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/22/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/antibioticmech_inchikeys":
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "PCIHXARFCRKZMV-UHFFFAOYSA-N"}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/22/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete retained exact query frame, including all matches and no-match
    scope. Exact copied saved values: {"/contexts/22/source_scope_inventory/joins/chebi_origins":
    {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows",
    "query": []}}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /records/3/direct_companion_paths; /records/3/direct_companion_predicates
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Exact direct context planning; shared key/locus scope does not transfer
    identity, experiment or mechanism. Exact copied saved values: {"/records/3/direct_companion_paths":
    ["data/natural_products/alkaloids/fusarochromene.yaml", "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml",
    "data/natural_products/terpenoids/fusarochromanone.yaml"], "/records/3/direct_companion_predicates":
    [{"path": "data/natural_products/alkaloids/fusarochromene.yaml", "same_complete_InChIKey":
    false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}, {"path":
    "data/natural_products/amino_acids_and_peptides/4-hydroxykynurenine.yaml", "same_complete_InChIKey":
    false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}, {"path":
    "data/natural_products/terpenoids/fusarochromanone.yaml", "same_complete_InChIKey":
    false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0002256"]}]}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/0; /contexts/1; /contexts/29
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: 'Complete raw/history and source scope for declared direct companions remains
    context only; exact whole-reading carry is in source notes. Metadata: [{"declared_mechanism_roots_literal":
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
    [], "history_count": 3, "identifier": "naturalproductmech:mibig-95c375019f", "input":
    {"bytes": 4391, "path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/fusarochromanone.yaml",
    "sha256": "5d8adf4a61d8d941b042d0efb089a113fdab1f54296b6cbc5b915490669f9a2b"},
    "label": "fusarochromanone", "owned_bgc_ids": ["BGC0002256"], "path": "data/natural_products/terpenoids/fusarochromanone.yaml",
    "standard_inchi_key": "COSICWYFCAPPJB-UHFFFAOYSA-N"}]'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: support-2314-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 175–200; lines 368–435
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Schema distinguishes source SMILES, normalized-key limitations, undefined
    stereocenters, versioned computed classification and source BGC class.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2314-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 145–174
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Maintained source extractor derives stereo_complete from unassigned tetrahedral
    chiral centers of source SMILES. This read-only predicate inspection does not
    execute it or establish natural stereochemistry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2314-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 296–307; lines 982–1020
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Maintained seeder preserves source structure fields and all versioned NPClassifier
    arrays; filing follows the returned pathway array. No seeder run occurred for
    scientific authoring.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2314-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-03T23:28:58.494624Z'
  support: supports
  summary: Scientific dimensions, independent claims and partial completion remain
    required; local gates are not scientific proof.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2314-review-skill
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
- assessment_id: support-2314-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The literal label desacetylfusarochromene and full key PCIHXARFCRKZMV-UHFFFAOYSA-N
    match BGC0002256 version 3, compound index 2. The record is MINTED and the exact
    saved ChEBI join is empty. Fusarochromene, 4-hydroxykynurenine and Fusarochromanone
    are direct locus context with distinct complete keys and source assertions; their
    folder locations, names or occurrence evidence are not identity substitutes.
  target_ids:
  - naturalproductmech:mibig-da909f5425
  evidence_ids:
  - support-2314-grounding-owner
  - support-2314-source-mibig_compounds
  - support-2314-query-chebi_structures
  - support-2314-chemistry
  - support-2314-direct-contexts
  - support-2314-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: PCIHXARFCRKZMV-UHFFFAOYSA-N; exact retained full key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - support-2314-grounding-owner
    - support-2314-source-mibig_compounds
    - support-2314-query-chebi_structures
    - support-2314-chemistry
    - support-2314-direct-contexts
    - support-2314-companion-boundaries
  - name: grounding_scope
    value: MINTED, exact ChEBI join empty; distinct companion full keys and naming
      scopes retained.
    definition: Local retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2314-grounding-owner
    - support-2314-source-mibig_compounds
    - support-2314-query-chebi_structures
    - support-2314-chemistry
    - support-2314-direct-contexts
    - support-2314-companion-boundaries
- assessment_id: support-2314-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both forms are neutral C15H20N2O3 with 20 atoms and 21 bonds. Complete
    tables show an aromatic ring joined to an unsaturated oxygen heterocycle, a ketone-bearing
    side chain, two primary amino groups and terminal alcohol. The amino-alcohol side-chain
    tetrahedron is unspecified in both forms, consistent with stereo_complete:false
    and the unassigned stereo block of the key. All ten comparisons are true and the
    original substructure correspondence is complete, but full_graph_identity_established
    is false. The single cyclic C–O–C bridge does not establish a sugar or glycosidic
    linkage, and matching partially specified forms do not identify the natural stereoisomer.
  target_ids:
  - naturalproductmech:mibig-da909f5425
  evidence_ids:
  - support-2314-grounding-owner
  - support-2314-chemistry
  - support-2314-topology
  - support-2314-diagnostic-acceptance
  - support-2314-structure-schema
  - support-2314-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: One unspecified side-chain tetrahedron in both forms; source stereo_complete:false
      preserved.
    definition: Complete saved stereo/atom/bond interpretation; no new parse or experimental
      assignment.
    evidence_ids:
    - support-2314-grounding-owner
    - support-2314-chemistry
    - support-2314-topology
    - support-2314-diagnostic-acceptance
    - support-2314-structure-schema
    - support-2314-stereo-method
  - name: representation_correspondence
    value: All ten comparisons true and complete stored correspondence, but partially
      specified natural identity is unresolved.
    definition: Normalized identifier agreement does not establish fixed-graph or
      natural-form identity.
    evidence_ids:
    - support-2314-grounding-owner
    - support-2314-chemistry
    - support-2314-topology
    - support-2314-diagnostic-acceptance
    - support-2314-structure-schema
    - support-2314-stereo-method
- assessment_id: support-2314-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: Fusarium equiseti NCBITaxon:61235 is SOURCE_ASSERTION from BGC0002256 version
    3. The locus has no stated method and remains CLUSTER_UNSTATED; active/questionable/unknown
    are retained source metadata. Companion occurrences in F. sacchari, F. roseum
    or F. equiseti do not create an occurrence or production experiment for this exact
    full key.
  target_ids:
  - naturalproductmech:mibig-da909f5425
  evidence_ids:
  - support-2314-origin-owner
  - support-2314-source-mibig_compounds
  - support-2314-cached-taxonomy
  - support-2314-source-routes
  - support-2314-direct-contexts
  - support-2314-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: F. equiseti 61235 producer only; no written occurrence and no transfer
      from companion taxa.
    definition: Producer, occurrence, species, strain and unresolved labels retain
      their separate scope; cached labels are not fresh authority.
    evidence_ids:
    - support-2314-origin-owner
    - support-2314-source-mibig_compounds
    - support-2314-cached-taxonomy
    - support-2314-source-routes
    - support-2314-direct-contexts
    - support-2314-companion-boundaries
  - name: producer_evidence
    value: SOURCE_ASSERTION, BGC0002256 version 3.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - support-2314-origin-owner
    - support-2314-source-mibig_compounds
    - support-2314-cached-taxonomy
    - support-2314-source-routes
    - support-2314-direct-contexts
    - support-2314-companion-boundaries
  - name: locus_evidence
    value: CLUSTER_UNSTATED with no method; active/questionable/unknown source metadata.
    definition: Source version/status/method/grade is not a complete pathway or fresh
      primary verification.
    evidence_ids:
    - support-2314-origin-owner
    - support-2314-source-mibig_compounds
    - support-2314-cached-taxonomy
    - support-2314-source-routes
    - support-2314-direct-contexts
    - support-2314-companion-boundaries
- assessment_id: support-2314-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: PMID:33107888 is ENTRY-level source provenance shared across the BGC0002256
    compounds. It is not converted into a purified-enzyme experiment or a compound-specific
    activity assertion. Separate companion LOTUS citations remain attached to their
    own full keys; no citation transfer is warranted.
  target_ids:
  - naturalproductmech:mibig-da909f5425
  evidence_ids:
  - support-2314-origin-owner
  - support-2314-occurrence-owner
  - support-2314-source-mibig_compounds
  - support-2314-source-notes
  - support-2314-direct-contexts
  - support-2314-companion-boundaries
  dimensions:
  - name: citation_scope
    value: ENTRY PMID:33107888; companion occurrence citations remain scoped to their
      respective full keys.
    definition: Database provenance and occurrence citations retain distinct roles;
      no publication independence or fresh source access is assumed.
    evidence_ids:
    - support-2314-origin-owner
    - support-2314-occurrence-owner
    - support-2314-source-mibig_compounds
    - support-2314-source-notes
    - support-2314-direct-contexts
    - support-2314-companion-boundaries
- assessment_id: support-2314-activity
  area: evidence
  topic: Activity
  outcome: supported
  summary: No occurrence, bioactivity or molecular target is written for this owner.
    Its exact saved LOTUS, ChEBI-origin, CyanometDB, PubChem, BindingDB and sibling-corpus
    activity joins are empty. This is a bounded retained-source absence, not evidence
    of inactivity or universal biological absence.
  target_ids:
  - naturalproductmech:mibig-da909f5425
  evidence_ids:
  - support-2314-occurrence-owner
  - support-2314-assay-owner
  - support-2314-source-routes
  - support-2314-cached-taxonomy
  - support-2314-query-lotus_occurrences
  - support-2314-query-chebi_origins
  - support-2314-query-cyanometdb_occurrences
  - support-2314-query-pubchem_bioassay
  - support-2314-query-bindingdb_targets
  - support-2314-query-antibioticmech_inchikeys
  - support-2314-direct-contexts
  - support-2314-companion-boundaries
  dimensions:
  - name: occurrence_scope
    value: No written occurrence, assay or target; all relevant exact retained joins
      empty.
    definition: Occurrence placements are not counts of independent experiments or
      demonstrated producers.
    evidence_ids:
    - support-2314-occurrence-owner
    - support-2314-assay-owner
    - support-2314-source-routes
    - support-2314-cached-taxonomy
    - support-2314-query-lotus_occurrences
    - support-2314-query-chebi_origins
    - support-2314-query-cyanometdb_occurrences
    - support-2314-query-pubchem_bioassay
    - support-2314-query-bindingdb_targets
    - support-2314-query-antibioticmech_inchikeys
    - support-2314-direct-contexts
    - support-2314-companion-boundaries
  - name: assay_target_scope
    value: No written bioactivity/target and exact retained assay/target joins empty;
      no inactivity or global absence inference.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - support-2314-occurrence-owner
    - support-2314-assay-owner
    - support-2314-source-routes
    - support-2314-cached-taxonomy
    - support-2314-query-lotus_occurrences
    - support-2314-query-chebi_origins
    - support-2314-query-cyanometdb_occurrences
    - support-2314-query-pubchem_bioassay
    - support-2314-query-bindingdb_targets
    - support-2314-query-antibioticmech_inchikeys
    - support-2314-direct-contexts
    - support-2314-companion-boundaries
- assessment_id: support-2314-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The retained model is Terpenoids / Meroterpenoids / Merohemiterpenoids
    with is_glycoside:false at npclassifier.gnps2.org@2026-09-07. The source BGC classes
    NRPS and OTHER and subclasses Type I and other concern locus classification, not
    a competing experimental molecular-class assignment. The gem-dimethyl oxygen heterocycle
    and amino-ketone side chain permit a limited topology discussion; the model filing
    is neither a newly demonstrated pathway nor grounds to edit the source record.
  target_ids:
  - naturalproductmech:mibig-da909f5425
  evidence_ids:
  - support-2314-classification-owner
  - support-2314-source-mibig_compounds
  - support-2314-source-npclassifier
  - support-2314-chemistry
  - support-2314-topology
  - support-2314-structure-schema
  - support-2314-classification-seeder
  - support-2314-direct-contexts
  - support-2314-companion-boundaries
  dimensions:
  - name: classification_applicability
    value: Merohemiterpenoids/false glycoside is a versioned prediction; NRPS/OTHER
      source classes describe the locus.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct evidence types.
    evidence_ids:
    - support-2314-classification-owner
    - support-2314-source-mibig_compounds
    - support-2314-source-npclassifier
    - support-2314-chemistry
    - support-2314-topology
    - support-2314-structure-schema
    - support-2314-classification-seeder
    - support-2314-direct-contexts
    - support-2314-companion-boundaries
- assessment_id: support-2314-completion
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
  - naturalproductmech:mibig-da909f5425
  evidence_ids:
  - support-2314-owner
  - support-2314-capture
  - support-2314-intake
  - support-2314-intake-acceptance
  - support-2314-inventory-acceptance
  - support-2314-plan
  - support-2314-plan-acceptance
  - support-2314-source-notes
  - support-2314-curation-scope
  - support-2314-diagnostic-execution
  - support-2314-diagnostic-acceptance
  - support-2314-native-acceptance
  - support-2314-review-profile
  - support-2314-review-skill
  - support-2314-query-mibig_compounds
  - support-2314-query-chebi_structures
  - support-2314-query-lotus_occurrences
  - support-2314-query-cyanometdb_occurrences
  - support-2314-query-npclassifier
  - support-2314-query-pubchem_bioassay
  - support-2314-query-bindingdb_targets
  - support-2314-query-antibioticmech_inchikeys
  - support-2314-query-chebi_origins
  dimensions:
  - name: review_completion
    value: 'Partial: retained evidence only, unavailable full QC/OAK and unresolved
      fresh primary/taxonomic/natural stereochemical verification. No native status
      promotion.'
    definition: Completion reflects actual evidence access and required-check coverage;
      parsing and gate success are not scientific proof.
    evidence_ids:
    - support-2314-owner
    - support-2314-capture
    - support-2314-intake
    - support-2314-intake-acceptance
    - support-2314-inventory-acceptance
    - support-2314-plan
    - support-2314-plan-acceptance
    - support-2314-source-notes
    - support-2314-curation-scope
    - support-2314-diagnostic-execution
    - support-2314-diagnostic-acceptance
    - support-2314-native-acceptance
    - support-2314-review-profile
    - support-2314-review-skill
    - support-2314-query-mibig_compounds
    - support-2314-query-chebi_structures
    - support-2314-query-lotus_occurrences
    - support-2314-query-cyanometdb_occurrences
    - support-2314-query-npclassifier
    - support-2314-query-pubchem_bioassay
    - support-2314-query-bindingdb_targets
    - support-2314-query-antibioticmech_inchikeys
    - support-2314-query-chebi_origins
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
