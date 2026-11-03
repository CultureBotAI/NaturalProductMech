# Local evidence review: aspulvinone E

- Review: 20261103T080908Z-aspulvinone-e
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T07:43:36.036226Z
- Finished UTC: 2026-11-03T08:09:08.527319Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

aspulvinone E: qualified partial review preserving exact identity, source grades and bounded representation/activity claims.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2180; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:17704 | data/natural_products/shikimates_and_phenylpropanoids/aspulvinone-e.yaml | generated | aspulvinone E |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:17704 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:17704 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:17704 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:17704 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:17704 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:17704 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:17704 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:17704 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact identity and grounding scope

identity: supported. Targets: CHEBI:17704.

CHEBI:17704 and MIBiG BGC0002348 version 2 compound 1 retain BNNVVTQUWNGKPH-ZROIWOOFSA-N/C17H12O5. The three-star ChEBI Z-benzylidenefuranone definition agrees with the saved STEREOZ bond assignment. The AntibioticMech row shares the full key and CHEBI:17704 and supports the recorded SAME_STRUCTURE/SAME_INCHIKEY link within its pinned version. No broader record or congener identity is inferred.

### Paired representations and stereochemistry limits

representation: supported. Targets: CHEBI:17704.

Both saved forms parse as neutral C17H12O5 (22 atoms/24 bonds), agree on all ten saved comparisons and retain a complete atom map with full_graph_identity_established:false. Both forms encode one specified Z exocyclic alkene: SMILES bond 6 C6=C7 has STEREOZ with stereo atoms 5/12; InChI bond 13 C8=C13 has STEREOZ with atoms 9/21. At the ring end O12 (O21) outranks carbon, and the aryl carbon outranks H at the other end. The potential-stereo descriptor Bond_Trans uses neighbor ordering and is not an E assignment or a contradiction of ChEBI Z. No tetrahedral stereo is detected; literal stereo_complete:true remains an encoded-source flag, not new experimental proof. Two original global warnings remain unassigned.

### Producer, occurrence and locus grades

provenance: supported. Targets: CHEBI:17704.

Aspergillus terreus NIH2624 (NCBITaxon:341663) is retained as BGC_CHARACTERIZED with CLUSTER_DEMONSTRATED BGC0002348 and Knock-out studies. The source lists NRPS Type I, CH476597.1 coordinates 2146060–2164193, active version 2 with questionable quality and unknown completeness. Species33178, species 41900 and genus 5052 occurrence scopes do not establish production by the NIH2624 strain.

### Claim-level citation support

evidence: supported. Targets: CHEBI:17704.

DOI:10.1039/d2ra08133d is explicitly MIBiG COMPOUND_BIOACTIVITY citation scope, while the source locus-method field supplies the retained knockout grade; this review did not independently establish what that paper demonstrates. Six LOTUS citations and two ChEBI-origin assertions (DOI:10.1007/s00044-014-1164-0 and PMID:23411074) remain occurrence-scoped. Shared identifiers or database routes do not establish independent experiments.

### Occurrence and assay boundaries

scope: supported. Targets: CHEBI:17704.

Eight written occurrences match six LOTUS rows plus two ChEBI-origin rows. The origins retain Aspergillus terreus RCC1 cell-suspension-culture context and Gwq-48, distinct from producer NIH2624; LOTUS includes species A.terreus33178, A.flavipes41900 and genusAspergillus5052. There are no written bioactivity objects, PubChem assay rows or BindingDB target rows for this retained exact key. ANTIVIRAL is supported only at coarse annotation scope by the exact AntibioticMech row and retained ChEBI definition. The sibling pin74f6cc8362498900f2fe2c13d0b6fdb66dd30976 matches the record source-version prefix; no assay, quantitative antiviral endpoint, virus, target or mechanism is transferred.

### Computed classification and topology applicability

other: supported. Targets: CHEBI:17704.

NPClassifier reports Shikimates and Phenylpropanoids / Diazotetronic acids and derivatives / Pulvinones, is_glycoside=false (npclassifier.gnps2.org@2026-09-07). The Pulvinones model label is consistent with the hydroxybenzylidene/hydroxyphenyl furanone topology. Its Diazotetronic acids and derivatives superclass is a model label, not a literal claim of nitrogen atoms (the saved formula has none), and model filing remains separate from the retained NRPS source class. The SMILES tables show a five-membered unsaturated lactone ring [8,7,12,10,9], carbonyl C10=O11, ring oxygen O12, two hydroxyphenyl rings, and hydroxyl O20 at C8. Its exocyclic alkene is distinct from the in-ring C8=C9 bond. The carbonyl ester motif C10–O12–C7 is present, with no saturated C5O candidate sugar ring; the ring oxygen is not a glycosidic linkage.

### Partial completion and maintained ownership

completeness: supported. Targets: CHEBI:17704.

All seven core areas and twelve dimensions were assessed against the actual intake, complete raw/history, retained source rows/cache and both saved chemical forms. Five local commands passed; full QC/OAK and external verification remain unavailable. This owner declares no mechanism roots/components and needs no maintained reader. The pinned source assertions and local structure are positively supported within that scope; no concrete contradiction requiring a finding was established. SEEDED status/history and all source records remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2180-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/aspulvinone-e.yaml; Complete raw owner, lines 1-176. | supports | Whole selected raw owner and 2 complete history events personally read; exact bytes retained. |
| support-2180-capture | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/9/owner_document; /records/9/owner_pin; /records/9/read_started_at; /records/9/read_finished_at | supports | Actual captured complete owner, current raw pin and original access clocks. |
| support-2180-intake | /private/tmp/npm-review-work/shared-next-batch218/intakes/2180-inspect-001.json; /status; /source; /targets/0 | supports | Original inspection-only intake with 37 current admitted inputs and explicit maintained owner paths. |
| support-2180-source-plan | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/9; /source_placement_count; /unique_source_path_count | supports | Exact selected raw/history/source frames and input map match accepted inventory and actual intake. Whole cohort 392placements67 paths; no future scientific authority inferred. |
| support-2180-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch218-tentative/root-conditional218-input-plan-acceptance-001.json; /accepted; /plan; /inventory; /per_order_counts | supports | ROOT accepts the exact saved plan and joins all actual intake maps; no scientific verdict is conferred. |
| support-2180-history | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/complete_raw_history; /contexts/16/history_count | supports | All 2 complete history events retained unchanged. |
| support-2180-direct-contexts | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/9/proposed_companion_paths; /records/9/direct_companion_predicates; /records/9/declared_mechanism_roots_literal; /records/9/component_paths | supports | No direct companions, four mechanism roots or components are admitted for this selected owner; no maintained reader applies. |
| support-2180-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/mibig_compounds | supports | Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N"; 1 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2180-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical TSV line 2871. | supports | Retained row only, row SHA256 b70ec6c52c3efd280a306bf17e6fb76ab87509dc98d508f77a21ffb1afac9668: {"bgc_classes": "NRPS", "bgc_subclasses": "Type I", "cluster_link_evidence_basis": "CLUSTER_DEMONSTRATED", "compound_classes": "", "compound_index": "1", "compound_name": "aspulvinone E", "database_ids": "npatlas:NPA001618", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "2", "genome_accession": "CH476597.1", "locus_evidence_methods": "Knock-out studies", "locus_from": "2146060", "locus_to": "2164193", "mibig_accession": "BGC0002348", "primary_reference": "DOI:10.1039/d2ra08133d", "producer_evidence_basis": "BGC_CHARACTERIZED", "reference_basis": "COMPOUND_BIOACTIVITY", "smiles": "C1=CC(=CC=C1/C=C\\2/C(=C(C(=O)O2)C3=CC=C(C=C3)O)O)O", "standard_inchi": "InChI=1S/C17H12O5/c18-12-5-1-10(2-6-12)9-14-16(20)15(17(21)22-14)11-3-7-13(19)8-4-11/h1-9,18-20H/b14-9-", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:341663", "taxon_label": "Aspergillus terreus NIH2624"} |
| support-2180-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/chebi_structures | supports | Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N"; 1 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2180-row-chebi_structures-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line 1; physical TSV line 4104. | supports | Retained row only, row SHA256 047de634a329e9f91ea45e4193cad23dee901d46509fe52f6fd7fac9ffe2976e: {"chebi_id": "CHEBI:17704", "definition": "A 4-hydroxy-5-(4-hydroxybenzylidene)-3-(4-hydroxyphenyl)furan-2(5H)-one in which the double bond adopts a Z-configuration. It is a marine metabolite isolated from the fungus Aspergillus terreus and exhibits antiviral activity.", "name": "aspulvinone E", "smiles": "O=C1O/C(=C\\c2ccc(O)cc2)C(O)=C1c1ccc(O)cc1", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "stars": "3"} |
| support-2180-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/lotus_occurrences | supports | Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N"; 6 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2180-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical TSV line 559. | supports | Retained row only, row SHA256 a1442858c5f592fa72577f149e19be8a1c95309177f3b745ecdefa1c2f2c8797: {"organism_name": "Aspergillus terreus", "organism_wikidata": "http://www.wikidata.org/entity/Q3798237", "reference_doi": "10.1016/0031-9422(73)80469-8", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id": "NCBITaxon:33178"} |
| support-2180-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical TSV line 560. | supports | Retained row only, row SHA256 78afb924e53857a297da5a30d87e5aae7bd943aa45764e6a556fff0907a97e9d: {"organism_name": "Aspergillus terreus", "organism_wikidata": "http://www.wikidata.org/entity/Q3798237", "reference_doi": "10.1016/J.BMCL.2013.01.051", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id": "NCBITaxon:33178"} |
| support-2180-row-lotus_occurrences-2 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical TSV line 561. | supports | Retained row only, row SHA256 6d8385e66de810749899429f70a792dc47bb3640bac6bafcd4f331ebbabb2fb2: {"organism_name": "Aspergillus terreus", "organism_wikidata": "http://www.wikidata.org/entity/Q3798237", "reference_doi": "10.1016/J.CHEMBIOL.2016.03.014", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id": "NCBITaxon:33178"} |
| support-2180-row-lotus_occurrences-3 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical TSV line 562. | supports | Retained row only, row SHA256 374918b6f38bbca4abf951288d95e5ad0e8cdbd352c8ac361c591c0526937cbd: {"organism_name": "Aspergillus terreus", "organism_wikidata": "http://www.wikidata.org/entity/Q3798237", "reference_doi": "10.1016/J.PHYTOL.2015.02.009", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id": "NCBITaxon:33178"} |
| support-2180-row-lotus_occurrences-4 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical TSV line 563. | supports | Retained row only, row SHA256 aee21b1566f11ab01b571ac037c4cf517a1e42e2e341f1e8624e48756e6b323d: {"organism_name": "Aspergillus flavipes", "organism_wikidata": "http://www.wikidata.org/entity/Q6650998", "reference_doi": "10.1186/2191-2858-2-9", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id": "NCBITaxon:41900"} |
| support-2180-row-lotus_occurrences-5 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical TSV line 564. | supports | Retained row only, row SHA256 681a992e43633d88b932c8b00b8bdbd0f0ccb3d70f963cea8ac410051ba41ed8: {"organism_name": "Aspergillus", "organism_wikidata": "http://www.wikidata.org/entity/Q335130", "reference_doi": "10.1021/ACS.JNATPROD.6B00878", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id": "NCBITaxon:5052"} |
| support-2180-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N"; 0 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2180-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/npclassifier | supports | Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N"; 1 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2180-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical TSV line 202. | supports | Retained row only, row SHA256 3a458b33be69c1a1253b1a61dba74c6440ab6925548265c6545344beedd03d63: {"class_results": "Pulvinones", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Shikimates and Phenylpropanoids", "smiles": "C1=CC(=CC=C1/C=C\\2/C(=C(C(=O)O2)C3=CC=C(C=C3)O)O)O", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "superclass_results": "Diazotetronic acids and derivatives"} |
| support-2180-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/pubchem_bioassay | supports | Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N"; 0 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2180-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/bindingdb_targets | supports | Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N"; 0 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2180-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N"; 1 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2180-row-antibioticmech_inchikeys-0 | /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv; Header line 1; physical TSV line 163. | supports | Retained row only, row SHA256 f0104f76ee0b705ffda091acdc51491cb2cb2b0fcf4efa61623c8eb53d4b2a39: {"antimicrobial_class": "ANTIVIRAL", "corpus_commit": "74f6cc8362498900f2fe2c13d0b6fdb66dd30976", "identifier": "CHEBI:17704", "label": "aspulvinone E", "slug": "aspulvinone-e", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N"} |
| support-2180-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/chebi_origins | supports | Saved predicate exact chebi_id from exact full-key structure rows; query ["CHEBI:17704"]; 2 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2180-row-chebi_origins-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Header line 1; physical TSV line 2820. | supports | Retained row only, row SHA256 eef84deb8a0dc519c1dd4f5f034315f41fa62f1470b66f330aab390ea5d143ce: {"chebi_id": "CHEBI:17704", "comments": "", "component_text": "cell suspension culture", "source_accession": "10.1007/s00044-014-1164-0", "species_accession": "33178", "species_text": "Aspergillus terreus", "strain_text": "RCC1"} |
| support-2180-row-chebi_origins-1 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Header line 1; physical TSV line 2821. | supports | Retained row only, row SHA256 598beae388c1c5370b3c977ae444878e0d0a717e1309243b89c0374c43cdf1f4: {"chebi_id": "CHEBI:17704", "comments": "", "component_text": "", "source_accession": "23411074", "species_accession": "33178", "species_text": "Aspergillus terreus", "strain_text": "Gwq-48"} |
| support-2180-taxon-routes | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/source_taxa; /contexts/16/source_scope_inventory/forward_taxon_merge_matches; /contexts/16/source_scope_inventory/nonorganism_matches | supports | Exact source taxa NCBITaxon:33178, NCBITaxon:341663, NCBITaxon:41900, NCBITaxon:5052; no retained forward merge or nonorganism matches. Cached labels do not establish production or fresh taxonomic authority. |
| support-2180-taxon-33178 | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/16; /cached_taxonomy/input | supports | Whole cached stanza for NCBITaxon:33178 names Aspergillus terreus at OBO line 14562. Source/historical labels and any synonyms remain scoped; no live taxonomy or production proof. |
| support-2180-taxon-341663 | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/49; /cached_taxonomy/input | supports | Whole cached stanza for NCBITaxon:341663 names Aspergillus terreus NIH2624 at OBO line 84583. Source/historical labels and any synonyms remain scoped; no live taxonomy or production proof. |
| support-2180-taxon-41900 | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/19; /cached_taxonomy/input | supports | Whole cached stanza for NCBITaxon:41900 names Aspergillus flavipes at OBO line 19140. Source/historical labels and any synonyms remain scoped; no live taxonomy or production proof. |
| support-2180-taxon-5052 | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/input | supports | Whole cached stanza for NCBITaxon:5052 names Aspergillus at OBO line 7840. Source/historical labels and any synonyms remain scoped; no live taxonomy or production proof. |
| support-2180-chemistry | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json; /records/9/declared_structure; /records/9/smiles/computed; /records/9/inchi/computed; /records/9/comparisons; /records/9/atom_correspondence; /records/9/literal_InChI_layers | supports | Both saved forms parse as neutral C17H12O5 with 22 atoms/24 bonds; all ten comparisons true and complete chirality-aware atom map. full_graph_identity_established:false; no fresh parse or proof of natural identity. |
| support-2180-topology | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles/computed; /records/9/inchi/computed | supports | The SMILES tables show a five-membered unsaturated lactone ring [8,7,12,10,9], carbonyl C10=O11, ring oxygen O12, two hydroxyphenyl rings, and hydroxyl O20 at C8. Its exocyclic alkene is distinct from the in-ring C8=C9 bond. The carbonyl ester motif C10–O12–C7 is present, with no saturated C5O candidate sugar ring; the ring oxygen is not a glycosidic linkage. |
| support-2180-stereo | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json; /records/9/declared_structure; /records/9/smiles/computed/potential_stereo; /records/9/inchi/computed/potential_stereo; /records/9/smiles/computed/stereo_counts; /records/9/inchi/computed/stereo_counts; /records/9/smiles/computed/atoms; /records/9/inchi/computed/atoms; /records/9/smiles/computed/bonds; /records/9/inchi/computed/bonds | supports | Both forms encode one specified Z exocyclic alkene: SMILES bond 6 C6=C7 has STEREOZ with stereo atoms 5/12; InChI bond 13 C8=C13 has STEREOZ with atoms 9/21. At the ring end O12 (O21) outranks carbon, and the aryl carbon outranks H at the other end. The potential-stereo descriptor Bond_Trans uses neighbor ordering and is not an E assignment. No tetrahedral stereo is detected; literal stereo_complete:true remains an encoded-source flag, not new experimental proof. |
| support-2180-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165-172. | supports | Maintained stereo_complete derives from unassigned atom-centered FindMolChiralCenters results; no independent axial/all-natural-stereo claim. |
| support-2180-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-execution-001.json; /exit_code; /target_invocations; /retries; /DATA; /stderr | supports | Original ROOT diagnostic exit0, one target invocation/no retries; exact DATA and stderr pins. |
| support-2180-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch218/root-diagnostic-acceptance-001.json; /accepted; /verification; /limits; /DATA | supports | ROOT accepts 20 parsed forms/all 100 comparisons true. Two original global stereo warnings remain unassigned; natural identity and complete stereochemistry are not established. |
| support-2180-warnings | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-stderr-001.log; Complete original stderr, lines 1-4. | supports | Two original global omitted-undefined-stereo warnings with blank separators; not assigned to any one owner. |
| support-2180-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch218/root-intake-ready-001.json; /status; /input_placements; /unique_input_paths; /input_counts; /reader_orders | supports | ROOT accepts all 10 original inspection-only intakes 392placements67 paths with no selected readers. |
| support-2180-native-acceptance | /private/tmp/npm-review-work/shared-next-batch218/root-native-gates-acceptance-001.json; /results; /unavailable_required_gates; /all_native_gates_passed; /selected_queue_rows | supports | Five actual local commands passed; strict selected 10/full 3116 zero errors and 3116 byte-identical reproduction. Only 14 selected queue rows and 12 group counts are read here; full QC/OAK unavailable and all_native_gates_passed:false. |
| support-2180-source-ownership | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 950-1005; lines 1252-1308; lines 1310-1381; lines 1438-1468. | supports | Maintained exact-key grounding, literal stereo-source carry, occurrence deduplication/cap, written ACTIVE assay summary and coarse same-key sibling summary derivation; generator read as text only. |
| support-2180-activity-method | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 128-178; lines 1310-1381; lines 1438-1468. | supports | Assay names supply coarse classes only for ACTIVE written calls; sibling mappings support coarse summary without target, MIC or mechanism transfer. |
| support-2180-activity-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 273-286; lines 920-949. | supports | The schema requires a backed coarse activity summary and distinguishes measurements from bare observations; no potency is invented. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-218/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-218/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-218/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-218/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-218/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- No external requests, original-paper reading or live ontology/taxonomy/accession/sibling verification. Imported identifiers and quotations retain their source scope.
- All ten saved comparisons agree, but full_graph_identity_established remains false. The two original global stereo warnings are unassigned; natural identity and unmeasured stereochemistry are not proved.
- Full QC/OAK remain unavailable. Local gate success and selected queue rows do not establish scientific completeness.
- Empty retained query frames apply only to the exact pinned key/query; no inactivity, literature absence or congener-transfer inference. Curation reading is limited to the admitted seven baseline tables; the eighth assay table was supplemental preparation only.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Whole selected raw/history and both complete saved molecular tables personally read. BGC owns collector/composer and other source partitions; Support owns this target's retained payloads and relevant cached stanzas.
- No source, status or history edits, additional molecular/YAML parses, maintained-reader/gate/assembly/canonical invocation or outbound activity.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T080908Z-aspulvinone-e
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: aspulvinone E'
started_at: '2026-11-03T07:43:36.036226Z'
finished_at: '2026-11-03T08:09:08.527319Z'
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
summary: 'aspulvinone E: qualified partial review preserving exact identity, source
  grades and bounded representation/activity claims.'
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/aspulvinone-e.yaml
    sha256: 934404beb11d0e7f803d6b0022530a50dfc9a5b71277943b58a8c14619996766
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
  selection: Campaign path order 2180; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:17704
targets:
- target_id: CHEBI:17704
  path: data/natural_products/shikimates_and_phenylpropanoids/aspulvinone-e.yaml
  label: aspulvinone E
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
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned full-key AntibioticMech structure links and coarse activity summaries;
      no transfer of mechanism.
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
  - CHEBI:17704
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/3-5-dibromo-p-anisic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/3-p-hydroxyphenyl-1-2-propanediol.yaml
    data/natural_products/shikimates_and_phenylpropanoids/4-hydroxy-3-prenylbenzoic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/6-hydroxymellein.yaml data/natural_products/shikimates_and_phenylpropanoids/6-methylsalicylic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/8-methyldiaporthin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/aflavarin.yaml data/natural_products/shikimates_and_phenylpropanoids/ajudazol-a.yaml
    data/natural_products/shikimates_and_phenylpropanoids/alternariol.yaml data/natural_products/shikimates_and_phenylpropanoids/aspulvinone-e.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-218/validate-strict-selected10-001.tsv
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
  - CHEBI:17704
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-218/validate-all-001.tsv
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
  - CHEBI:17704
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
  - CHEBI:17704
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
  - CHEBI:17704
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-218/review-queue-001.tsv
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
  - CHEBI:17704
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:17704
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:17704
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2180-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/aspulvinone-e.yaml
  locator: Complete raw owner, lines 1-176.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Whole selected raw owner and 2 complete history events personally read;
    exact bytes retained.
  snapshot_sha256: 934404beb11d0e7f803d6b0022530a50dfc9a5b71277943b58a8c14619996766
- evidence_id: support-2180-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/9/owner_document; /records/9/owner_pin; /records/9/read_started_at;
    /records/9/read_finished_at
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Actual captured complete owner, current raw pin and original access clocks.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: support-2180-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/intakes/2180-inspect-001.json
  locator: /status; /source; /targets/0
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Original inspection-only intake with 37 current admitted inputs and explicit
    maintained owner paths.
  snapshot_sha256: d17f0014c50d02b8b07e193e7a3b28948bbc95efd35ce2cd94f4cc134aae3aa7
- evidence_id: support-2180-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/9; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Exact selected raw/history/source frames and input map match accepted inventory
    and actual intake. Whole cohort 392placements67 paths; no future scientific authority
    inferred.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
- evidence_id: support-2180-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/root-conditional218-input-plan-acceptance-001.json
  locator: /accepted; /plan; /inventory; /per_order_counts
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: ROOT accepts the exact saved plan and joins all actual intake maps; no
    scientific verdict is conferred.
  snapshot_sha256: 938383f6b986f11823252b0a936784870aac1edd32b51ca4eea8c01b059af7ed
- evidence_id: support-2180-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/complete_raw_history; /contexts/16/history_count
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: All 2 complete history events retained unchanged.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/9/proposed_companion_paths; /records/9/direct_companion_predicates;
    /records/9/declared_mechanism_roots_literal; /records/9/component_paths
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: No direct companions, four mechanism roots or components are admitted for
    this selected owner; no maintained reader applies.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
- evidence_id: support-2180-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N";
    1 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical TSV line 2871.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 b70ec6c52c3efd280a306bf17e6fb76ab87509dc98d508f77a21ffb1afac9668:
    {"bgc_classes": "NRPS", "bgc_subclasses": "Type I", "cluster_link_evidence_basis":
    "CLUSTER_DEMONSTRATED", "compound_classes": "", "compound_index": "1", "compound_name":
    "aspulvinone E", "database_ids": "npatlas:NPA001618", "entry_completeness": "unknown",
    "entry_quality": "questionable", "entry_status": "active", "entry_version": "2",
    "genome_accession": "CH476597.1", "locus_evidence_methods": "Knock-out studies",
    "locus_from": "2146060", "locus_to": "2164193", "mibig_accession": "BGC0002348",
    "primary_reference": "DOI:10.1039/d2ra08133d", "producer_evidence_basis": "BGC_CHARACTERIZED",
    "reference_basis": "COMPOUND_BIOACTIVITY", "smiles": "C1=CC(=CC=C1/C=C\\2/C(=C(C(=O)O2)C3=CC=C(C=C3)O)O)O",
    "standard_inchi": "InChI=1S/C17H12O5/c18-12-5-1-10(2-6-12)9-14-16(20)15(17(21)22-14)11-3-7-13(19)8-4-11/h1-9,18-20H/b14-9-",
    "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:341663", "taxon_label": "Aspergillus terreus NIH2624"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2180-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N";
    1 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-row-chebi_structures-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line 1; physical TSV line 4104.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 047de634a329e9f91ea45e4193cad23dee901d46509fe52f6fd7fac9ffe2976e:
    {"chebi_id": "CHEBI:17704", "definition": "A 4-hydroxy-5-(4-hydroxybenzylidene)-3-(4-hydroxyphenyl)furan-2(5H)-one
    in which the double bond adopts a Z-configuration. It is a marine metabolite isolated
    from the fungus Aspergillus terreus and exhibits antiviral activity.", "name":
    "aspulvinone E", "smiles": "O=C1O/C(=C\\c2ccc(O)cc2)C(O)=C1c1ccc(O)cc1", "standard_inchi_key":
    "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "stars": "3"}'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: support-2180-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N";
    6 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical TSV line 559.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 a1442858c5f592fa72577f149e19be8a1c95309177f3b745ecdefa1c2f2c8797:
    {"organism_name": "Aspergillus terreus", "organism_wikidata": "http://www.wikidata.org/entity/Q3798237",
    "reference_doi": "10.1016/0031-9422(73)80469-8", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id":
    "NCBITaxon:33178"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2180-row-lotus_occurrences-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical TSV line 560.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 78afb924e53857a297da5a30d87e5aae7bd943aa45764e6a556fff0907a97e9d:
    {"organism_name": "Aspergillus terreus", "organism_wikidata": "http://www.wikidata.org/entity/Q3798237",
    "reference_doi": "10.1016/J.BMCL.2013.01.051", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id":
    "NCBITaxon:33178"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2180-row-lotus_occurrences-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical TSV line 561.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 6d8385e66de810749899429f70a792dc47bb3640bac6bafcd4f331ebbabb2fb2:
    {"organism_name": "Aspergillus terreus", "organism_wikidata": "http://www.wikidata.org/entity/Q3798237",
    "reference_doi": "10.1016/J.CHEMBIOL.2016.03.014", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id":
    "NCBITaxon:33178"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2180-row-lotus_occurrences-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical TSV line 562.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 374918b6f38bbca4abf951288d95e5ad0e8cdbd352c8ac361c591c0526937cbd:
    {"organism_name": "Aspergillus terreus", "organism_wikidata": "http://www.wikidata.org/entity/Q3798237",
    "reference_doi": "10.1016/J.PHYTOL.2015.02.009", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id":
    "NCBITaxon:33178"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2180-row-lotus_occurrences-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical TSV line 563.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 aee21b1566f11ab01b571ac037c4cf517a1e42e2e341f1e8624e48756e6b323d:
    {"organism_name": "Aspergillus flavipes", "organism_wikidata": "http://www.wikidata.org/entity/Q6650998",
    "reference_doi": "10.1186/2191-2858-2-9", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id":
    "NCBITaxon:41900"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2180-row-lotus_occurrences-5
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical TSV line 564.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 681a992e43633d88b932c8b00b8bdbd0f0ccb3d70f963cea8ac410051ba41ed8:
    {"organism_name": "Aspergillus", "organism_wikidata": "http://www.wikidata.org/entity/Q335130",
    "reference_doi": "10.1021/ACS.JNATPROD.6B00878", "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27102544", "taxon_id":
    "NCBITaxon:5052"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2180-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N";
    0 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N";
    1 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical TSV line 202.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 3a458b33be69c1a1253b1a61dba74c6440ab6925548265c6545344beedd03d63:
    {"class_results": "Pulvinones", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Shikimates and Phenylpropanoids", "smiles": "C1=CC(=CC=C1/C=C\\2/C(=C(C(=O)O2)C3=CC=C(C=C3)O)O)O",
    "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N", "superclass_results": "Diazotetronic
    acids and derivatives"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2180-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N";
    0 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N";
    0 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "BNNVVTQUWNGKPH-ZROIWOOFSA-N";
    1 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-row-antibioticmech_inchikeys-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv
  locator: Header line 1; physical TSV line 163.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 f0104f76ee0b705ffda091acdc51491cb2cb2b0fcf4efa61623c8eb53d4b2a39:
    {"antimicrobial_class": "ANTIVIRAL", "corpus_commit": "74f6cc8362498900f2fe2c13d0b6fdb66dd30976",
    "identifier": "CHEBI:17704", "label": "aspulvinone E", "slug": "aspulvinone-e",
    "standard_inchi_key": "BNNVVTQUWNGKPH-ZROIWOOFSA-N"}'
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
- evidence_id: support-2180-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact chebi_id from exact full-key structure rows; query
    ["CHEBI:17704"]; 2 retained rows. Empty results describe only this pinned scope,
    not inactivity or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-row-chebi_origins-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Header line 1; physical TSV line 2820.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 eef84deb8a0dc519c1dd4f5f034315f41fa62f1470b66f330aab390ea5d143ce:
    {"chebi_id": "CHEBI:17704", "comments": "", "component_text": "cell suspension
    culture", "source_accession": "10.1007/s00044-014-1164-0", "species_accession":
    "33178", "species_text": "Aspergillus terreus", "strain_text": "RCC1"}'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: support-2180-row-chebi_origins-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Header line 1; physical TSV line 2821.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 598beae388c1c5370b3c977ae444878e0d0a717e1309243b89c0374c43cdf1f4:
    {"chebi_id": "CHEBI:17704", "comments": "", "component_text": "", "source_accession":
    "23411074", "species_accession": "33178", "species_text": "Aspergillus terreus",
    "strain_text": "Gwq-48"}'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: support-2180-taxon-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/source_taxa; /contexts/16/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/16/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Exact source taxa NCBITaxon:33178, NCBITaxon:341663, NCBITaxon:41900, NCBITaxon:5052;
    no retained forward merge or nonorganism matches. Cached labels do not establish
    production or fresh taxonomic authority.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-taxon-33178
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/16; /cached_taxonomy/input
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Whole cached stanza for NCBITaxon:33178 names Aspergillus terreus at OBO
    line 14562. Source/historical labels and any synonyms remain scoped; no live taxonomy
    or production proof.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-taxon-341663
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/49; /cached_taxonomy/input
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Whole cached stanza for NCBITaxon:341663 names Aspergillus terreus NIH2624
    at OBO line 84583. Source/historical labels and any synonyms remain scoped; no
    live taxonomy or production proof.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-taxon-41900
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/19; /cached_taxonomy/input
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Whole cached stanza for NCBITaxon:41900 names Aspergillus flavipes at OBO
    line 19140. Source/historical labels and any synonyms remain scoped; no live taxonomy
    or production proof.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-taxon-5052
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/input
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Whole cached stanza for NCBITaxon:5052 names Aspergillus at OBO line 7840.
    Source/historical labels and any synonyms remain scoped; no live taxonomy or production
    proof.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2180-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/declared_structure; /records/9/smiles/computed; /records/9/inchi/computed;
    /records/9/comparisons; /records/9/atom_correspondence; /records/9/literal_InChI_layers
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Both saved forms parse as neutral C17H12O5 with 22 atoms/24 bonds; all
    ten comparisons true and complete chirality-aware atom map. full_graph_identity_established:false;
    no fresh parse or proof of natural identity.
  snapshot_sha256: 4e71336f0142da26d4b24905132c2acb742b3252da930bfd5b6bc483129f1330
- evidence_id: support-2180-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles/computed; /records/9/inchi/computed
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: The SMILES tables show a five-membered unsaturated lactone ring [8,7,12,10,9],
    carbonyl C10=O11, ring oxygen O12, two hydroxyphenyl rings, and hydroxyl O20 at
    C8. Its exocyclic alkene is distinct from the in-ring C8=C9 bond. The carbonyl
    ester motif C10–O12–C7 is present, with no saturated C5O candidate sugar ring;
    the ring oxygen is not a glycosidic linkage.
  snapshot_sha256: 4e71336f0142da26d4b24905132c2acb742b3252da930bfd5b6bc483129f1330
- evidence_id: support-2180-stereo
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/declared_structure; /records/9/smiles/computed/potential_stereo;
    /records/9/inchi/computed/potential_stereo; /records/9/smiles/computed/stereo_counts;
    /records/9/inchi/computed/stereo_counts; /records/9/smiles/computed/atoms; /records/9/inchi/computed/atoms;
    /records/9/smiles/computed/bonds; /records/9/inchi/computed/bonds
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Both forms encode one specified Z exocyclic alkene: SMILES bond 6 C6=C7
    has STEREOZ with stereo atoms 5/12; InChI bond 13 C8=C13 has STEREOZ with atoms
    9/21. At the ring end O12 (O21) outranks carbon, and the aryl carbon outranks
    H at the other end. The potential-stereo descriptor Bond_Trans uses neighbor ordering
    and is not an E assignment. No tetrahedral stereo is detected; literal stereo_complete:true
    remains an encoded-source flag, not new experimental proof.'
  snapshot_sha256: 4e71336f0142da26d4b24905132c2acb742b3252da930bfd5b6bc483129f1330
- evidence_id: support-2180-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165-172.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Maintained stereo_complete derives from unassigned atom-centered FindMolChiralCenters
    results; no independent axial/all-natural-stereo claim.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2180-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /target_invocations; /retries; /DATA; /stderr
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Original ROOT diagnostic exit0, one target invocation/no retries; exact
    DATA and stderr pins.
  snapshot_sha256: 2ef21bfab2aa20e8c198737cd65814fabc3cf91a51eb09cb617abb548c80cc06
- evidence_id: support-2180-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-diagnostic-acceptance-001.json
  locator: /accepted; /verification; /limits; /DATA
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: ROOT accepts 20 parsed forms/all 100 comparisons true. Two original global
    stereo warnings remain unassigned; natural identity and complete stereochemistry
    are not established.
  snapshot_sha256: 0f1c218ef2948f88c16e3ae0c830644e13e2d397ea05a9e4604a715e8da98443
- evidence_id: support-2180-warnings
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-stderr-001.log
  locator: Complete original stderr, lines 1-4.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Two original global omitted-undefined-stereo warnings with blank separators;
    not assigned to any one owner.
  snapshot_sha256: 836c9e40af7d808b240d363bb89b8b73c826451b24292cbfa9509297a4b6c480
- evidence_id: support-2180-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-intake-ready-001.json
  locator: /status; /input_placements; /unique_input_paths; /input_counts; /reader_orders
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: ROOT accepts all 10 original inspection-only intakes 392placements67 paths
    with no selected readers.
  snapshot_sha256: 4d19c500387ec2c243eb986a2e00c596a04a9fa2e4f1879d15165d0fcd2ac0cd
- evidence_id: support-2180-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-native-gates-acceptance-001.json
  locator: /results; /unavailable_required_gates; /all_native_gates_passed; /selected_queue_rows
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Five actual local commands passed; strict selected 10/full 3116 zero errors
    and 3116 byte-identical reproduction. Only 14 selected queue rows and 12 group
    counts are read here; full QC/OAK unavailable and all_native_gates_passed:false.
  snapshot_sha256: 57138741c14dfd03efcb91097dad031f0dc2209cb36d90f08c3b8796ae6f17b5
- evidence_id: support-2180-source-ownership
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 950-1005; lines 1252-1308; lines 1310-1381; lines 1438-1468.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Maintained exact-key grounding, literal stereo-source carry, occurrence
    deduplication/cap, written ACTIVE assay summary and coarse same-key sibling summary
    derivation; generator read as text only.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2180-activity-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 128-178; lines 1310-1381; lines 1438-1468.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Assay names supply coarse classes only for ACTIVE written calls; sibling
    mappings support coarse summary without target, MIC or mechanism transfer.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2180-activity-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 273-286; lines 920-949.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: The schema requires a backed coarse activity summary and distinguishes
    measurements from bare observations; no potency is invented.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-218/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json
  accessed_at: '2026-11-03T07:45:15.668585Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 35b181876d50c61aae3d6d9f47dda6fb34ee6cde4034660f8fc4f331a26db38d
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-218/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json
  accessed_at: '2026-11-03T07:45:43.691892Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 9a21ff2483495ee3c3d0e1631a10c4dd5cf399ea7f3f5838778bf6c4104dd10d
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-218/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json
  accessed_at: '2026-11-03T07:46:05.559629Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-218/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json
  accessed_at: '2026-11-03T07:46:42.649455Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-218/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json
  accessed_at: '2026-11-03T07:46:55.530300Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: cf9808fb82c82233d73dbf69f7483bb393c3341686b96881f6fc8137b53cdbaa
assessments:
- assessment_id: support-2180-A1
  area: identity
  topic: Exact identity and grounding scope
  outcome: supported
  summary: CHEBI:17704 and MIBiG BGC0002348 version 2 compound 1 retain BNNVVTQUWNGKPH-ZROIWOOFSA-N/C17H12O5.
    The three-star ChEBI Z-benzylidenefuranone definition agrees with the saved STEREOZ
    bond assignment. The AntibioticMech row shares the full key and CHEBI:17704 and
    supports the recorded SAME_STRUCTURE/SAME_INCHIKEY link within its pinned version.
    No broader record or congener identity is inferred.
  target_ids:
  - CHEBI:17704
  evidence_ids:
  - support-2180-owner
  - support-2180-capture
  - support-2180-intake
  - support-2180-source-plan
  - support-2180-plan-acceptance
  - support-2180-direct-contexts
  - support-2180-query-chebi_structures
  - support-2180-row-mibig_compounds-0
  - support-2180-row-chebi_structures-0
  - support-2180-row-antibioticmech_inchikeys-0
  - support-2180-chemistry
  - support-2180-stereo
  dimensions:
  - name: standard_inchi_key
    value: BNNVVTQUWNGKPH-ZROIWOOFSA-N
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-direct-contexts
    - support-2180-query-chebi_structures
    - support-2180-row-mibig_compounds-0
    - support-2180-row-chebi_structures-0
    - support-2180-row-antibioticmech_inchikeys-0
    - support-2180-chemistry
    - support-2180-stereo
  - name: grounding_scope
    value: EXACT; one retained three-star CHEBI:17704 match and full-key sibling link
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-direct-contexts
    - support-2180-query-chebi_structures
    - support-2180-row-mibig_compounds-0
    - support-2180-row-chebi_structures-0
    - support-2180-row-antibioticmech_inchikeys-0
    - support-2180-chemistry
    - support-2180-stereo
- assessment_id: support-2180-A2
  area: representation
  topic: Paired representations and stereochemistry limits
  outcome: supported
  summary: 'Both saved forms parse as neutral C17H12O5 (22 atoms/24 bonds), agree
    on all ten saved comparisons and retain a complete atom map with full_graph_identity_established:false.
    Both forms encode one specified Z exocyclic alkene: SMILES bond 6 C6=C7 has STEREOZ
    with stereo atoms 5/12; InChI bond 13 C8=C13 has STEREOZ with atoms 9/21. At the
    ring end O12 (O21) outranks carbon, and the aryl carbon outranks H at the other
    end. The potential-stereo descriptor Bond_Trans uses neighbor ordering and is
    not an E assignment or a contradiction of ChEBI Z. No tetrahedral stereo is detected;
    literal stereo_complete:true remains an encoded-source flag, not new experimental
    proof. Two original global warnings remain unassigned.'
  target_ids:
  - CHEBI:17704
  evidence_ids:
  - support-2180-owner
  - support-2180-capture
  - support-2180-intake
  - support-2180-source-plan
  - support-2180-plan-acceptance
  - support-2180-chemistry
  - support-2180-stereo
  - support-2180-stereo-method
  - support-2180-diagnostic-execution
  - support-2180-diagnostic-acceptance
  - support-2180-warnings
  dimensions:
  - name: stereochemical_resolution
    value: 'Both forms encode one specified Z exocyclic alkene: SMILES bond 6 C6=C7
      has STEREOZ with stereo atoms 5/12; InChI bond 13 C8=C13 has STEREOZ with atoms
      9/21. At the ring end O12 (O21) outranks carbon, and the aryl carbon outranks
      H at the other end. The potential-stereo descriptor Bond_Trans uses neighbor
      ordering and is not an E assignment or a contradiction of ChEBI Z. No tetrahedral
      stereo is detected; literal stereo_complete:true remains an encoded-source flag,
      not new experimental proof.'
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-chemistry
    - support-2180-stereo
    - support-2180-stereo-method
    - support-2180-diagnostic-execution
    - support-2180-diagnostic-acceptance
    - support-2180-warnings
  - name: representation_correspondence
    value: Ten comparisons true; complete chirality-aware map; full_graph_identity_established:false
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-chemistry
    - support-2180-stereo
    - support-2180-stereo-method
    - support-2180-diagnostic-execution
    - support-2180-diagnostic-acceptance
    - support-2180-warnings
- assessment_id: support-2180-A3
  area: provenance
  topic: Producer, occurrence and locus grades
  outcome: supported
  summary: Aspergillus terreus NIH2624 (NCBITaxon:341663) is retained as BGC_CHARACTERIZED
    with CLUSTER_DEMONSTRATED BGC0002348 and Knock-out studies. The source lists NRPS
    Type I, CH476597.1 coordinates 2146060–2164193, active version 2 with questionable
    quality and unknown completeness. Species33178, species 41900 and genus 5052 occurrence
    scopes do not establish production by the NIH2624 strain.
  target_ids:
  - CHEBI:17704
  evidence_ids:
  - support-2180-owner
  - support-2180-capture
  - support-2180-intake
  - support-2180-source-plan
  - support-2180-plan-acceptance
  - support-2180-row-mibig_compounds-0
  - support-2180-row-lotus_occurrences-0
  - support-2180-row-lotus_occurrences-1
  - support-2180-row-lotus_occurrences-2
  - support-2180-row-lotus_occurrences-3
  - support-2180-row-lotus_occurrences-4
  - support-2180-row-lotus_occurrences-5
  - support-2180-row-chebi_origins-0
  - support-2180-row-chebi_origins-1
  - support-2180-taxon-routes
  - support-2180-taxon-33178
  - support-2180-taxon-341663
  - support-2180-taxon-41900
  - support-2180-taxon-5052
  dimensions:
  - name: taxon_and_strain_scope
    value: NCBITaxon:33178; NCBITaxon:341663; NCBITaxon:41900; NCBITaxon:5052; source/cached
      labels only
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-row-mibig_compounds-0
    - support-2180-row-lotus_occurrences-0
    - support-2180-row-lotus_occurrences-1
    - support-2180-row-lotus_occurrences-2
    - support-2180-row-lotus_occurrences-3
    - support-2180-row-lotus_occurrences-4
    - support-2180-row-lotus_occurrences-5
    - support-2180-row-chebi_origins-0
    - support-2180-row-chebi_origins-1
    - support-2180-taxon-routes
    - support-2180-taxon-33178
    - support-2180-taxon-341663
    - support-2180-taxon-41900
    - support-2180-taxon-5052
  - name: producer_evidence_tier
    value: BGC_CHARACTERIZED; retained source assertion
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-row-mibig_compounds-0
    - support-2180-row-lotus_occurrences-0
    - support-2180-row-lotus_occurrences-1
    - support-2180-row-lotus_occurrences-2
    - support-2180-row-lotus_occurrences-3
    - support-2180-row-lotus_occurrences-4
    - support-2180-row-lotus_occurrences-5
    - support-2180-row-chebi_origins-0
    - support-2180-row-chebi_origins-1
    - support-2180-taxon-routes
    - support-2180-taxon-33178
    - support-2180-taxon-341663
    - support-2180-taxon-41900
    - support-2180-taxon-5052
  - name: locus_evidence_tier
    value: CLUSTER_DEMONSTRATED; Knock-out studies
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-row-mibig_compounds-0
    - support-2180-row-lotus_occurrences-0
    - support-2180-row-lotus_occurrences-1
    - support-2180-row-lotus_occurrences-2
    - support-2180-row-lotus_occurrences-3
    - support-2180-row-lotus_occurrences-4
    - support-2180-row-lotus_occurrences-5
    - support-2180-row-chebi_origins-0
    - support-2180-row-chebi_origins-1
    - support-2180-taxon-routes
    - support-2180-taxon-33178
    - support-2180-taxon-341663
    - support-2180-taxon-41900
    - support-2180-taxon-5052
- assessment_id: support-2180-A4
  area: evidence
  topic: Claim-level citation support
  outcome: supported
  summary: DOI:10.1039/d2ra08133d is explicitly MIBiG COMPOUND_BIOACTIVITY citation
    scope, while the source locus-method field supplies the retained knockout grade;
    this review did not independently establish what that paper demonstrates. Six
    LOTUS citations and two ChEBI-origin assertions (DOI:10.1007/s00044-014-1164-0
    and PMID:23411074) remain occurrence-scoped. Shared identifiers or database routes
    do not establish independent experiments.
  target_ids:
  - CHEBI:17704
  evidence_ids:
  - support-2180-owner
  - support-2180-capture
  - support-2180-intake
  - support-2180-source-plan
  - support-2180-plan-acceptance
  - support-2180-history
  - support-2180-row-mibig_compounds-0
  - support-2180-row-chebi_structures-0
  - support-2180-row-lotus_occurrences-0
  - support-2180-row-lotus_occurrences-1
  - support-2180-row-lotus_occurrences-2
  - support-2180-row-lotus_occurrences-3
  - support-2180-row-lotus_occurrences-4
  - support-2180-row-lotus_occurrences-5
  - support-2180-row-chebi_origins-0
  - support-2180-row-chebi_origins-1
  - support-2180-row-antibioticmech_inchikeys-0
  dimensions:
  - name: citation_scope
    value: MIBiG COMPOUND_BIOACTIVITY DOI10.1039/d2ra08133d; six LOTUS and two ChEBI-origin
      rows
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-history
    - support-2180-row-mibig_compounds-0
    - support-2180-row-chebi_structures-0
    - support-2180-row-lotus_occurrences-0
    - support-2180-row-lotus_occurrences-1
    - support-2180-row-lotus_occurrences-2
    - support-2180-row-lotus_occurrences-3
    - support-2180-row-lotus_occurrences-4
    - support-2180-row-lotus_occurrences-5
    - support-2180-row-chebi_origins-0
    - support-2180-row-chebi_origins-1
    - support-2180-row-antibioticmech_inchikeys-0
- assessment_id: support-2180-A5
  area: scope
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: Eight written occurrences match six LOTUS rows plus two ChEBI-origin rows.
    The origins retain Aspergillus terreus RCC1 cell-suspension-culture context and
    Gwq-48, distinct from producer NIH2624; LOTUS includes species A.terreus33178,
    A.flavipes41900 and genusAspergillus5052. There are no written bioactivity objects,
    PubChem assay rows or BindingDB target rows for this retained exact key. ANTIVIRAL
    is supported only at coarse annotation scope by the exact AntibioticMech row and
    retained ChEBI definition. The sibling pin74f6cc8362498900f2fe2c13d0b6fdb66dd30976
    matches the record source-version prefix; no assay, quantitative antiviral endpoint,
    virus, target or mechanism is transferred.
  target_ids:
  - CHEBI:17704
  evidence_ids:
  - support-2180-owner
  - support-2180-capture
  - support-2180-intake
  - support-2180-source-plan
  - support-2180-plan-acceptance
  - support-2180-query-lotus_occurrences
  - support-2180-query-cyanometdb_occurrences
  - support-2180-query-pubchem_bioassay
  - support-2180-query-bindingdb_targets
  - support-2180-query-antibioticmech_inchikeys
  - support-2180-query-chebi_origins
  - support-2180-row-lotus_occurrences-0
  - support-2180-row-lotus_occurrences-1
  - support-2180-row-lotus_occurrences-2
  - support-2180-row-lotus_occurrences-3
  - support-2180-row-lotus_occurrences-4
  - support-2180-row-lotus_occurrences-5
  - support-2180-row-chebi_origins-0
  - support-2180-row-chebi_origins-1
  - support-2180-row-antibioticmech_inchikeys-0
  - support-2180-activity-method
  - support-2180-activity-schema
  - support-2180-row-chebi_structures-0
  dimensions:
  - name: occurrence_scope
    value: Eight written occurrences match six LOTUS rows plus two ChEBI-origin rows.
      The origins retain Aspergillus terreus RCC1 cell-suspension-culture context
      and Gwq-48, distinct from producer NIH2624; LOTUS includes species A.terreus33178,
      A.flavipes41900 and genusAspergillus5052.
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-query-lotus_occurrences
    - support-2180-query-cyanometdb_occurrences
    - support-2180-query-pubchem_bioassay
    - support-2180-query-bindingdb_targets
    - support-2180-query-antibioticmech_inchikeys
    - support-2180-query-chebi_origins
    - support-2180-row-lotus_occurrences-0
    - support-2180-row-lotus_occurrences-1
    - support-2180-row-lotus_occurrences-2
    - support-2180-row-lotus_occurrences-3
    - support-2180-row-lotus_occurrences-4
    - support-2180-row-lotus_occurrences-5
    - support-2180-row-chebi_origins-0
    - support-2180-row-chebi_origins-1
    - support-2180-row-antibioticmech_inchikeys-0
    - support-2180-activity-method
    - support-2180-activity-schema
    - support-2180-row-chebi_structures-0
  - name: assay_scope
    value: Coarse sibling-backed ANTIVIRAL; no PubChem/BindingDB observations or potency
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-query-lotus_occurrences
    - support-2180-query-cyanometdb_occurrences
    - support-2180-query-pubchem_bioassay
    - support-2180-query-bindingdb_targets
    - support-2180-query-antibioticmech_inchikeys
    - support-2180-query-chebi_origins
    - support-2180-row-lotus_occurrences-0
    - support-2180-row-lotus_occurrences-1
    - support-2180-row-lotus_occurrences-2
    - support-2180-row-lotus_occurrences-3
    - support-2180-row-lotus_occurrences-4
    - support-2180-row-lotus_occurrences-5
    - support-2180-row-chebi_origins-0
    - support-2180-row-chebi_origins-1
    - support-2180-row-antibioticmech_inchikeys-0
    - support-2180-activity-method
    - support-2180-activity-schema
    - support-2180-row-chebi_structures-0
- assessment_id: support-2180-A6
  area: other
  topic: Computed classification and topology applicability
  outcome: supported
  summary: NPClassifier reports Shikimates and Phenylpropanoids / Diazotetronic acids
    and derivatives / Pulvinones, is_glycoside=false (npclassifier.gnps2.org@2026-09-07).
    The Pulvinones model label is consistent with the hydroxybenzylidene/hydroxyphenyl
    furanone topology. Its Diazotetronic acids and derivatives superclass is a model
    label, not a literal claim of nitrogen atoms (the saved formula has none), and
    model filing remains separate from the retained NRPS source class. The SMILES
    tables show a five-membered unsaturated lactone ring [8,7,12,10,9], carbonyl C10=O11,
    ring oxygen O12, two hydroxyphenyl rings, and hydroxyl O20 at C8. Its exocyclic
    alkene is distinct from the in-ring C8=C9 bond. The carbonyl ester motif C10–O12–C7
    is present, with no saturated C5O candidate sugar ring; the ring oxygen is not
    a glycosidic linkage.
  target_ids:
  - CHEBI:17704
  evidence_ids:
  - support-2180-owner
  - support-2180-capture
  - support-2180-intake
  - support-2180-source-plan
  - support-2180-plan-acceptance
  - support-2180-topology
  - support-2180-chemistry
  - support-2180-row-npclassifier-0
  - support-2180-row-mibig_compounds-0
  dimensions:
  - name: computed_classification
    value: Shikimates and Phenylpropanoids / Diazotetronic acids and derivatives /
      Pulvinones; glycoside=false; npclassifier.gnps2.org@2026-09-07
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-topology
    - support-2180-chemistry
    - support-2180-row-npclassifier-0
    - support-2180-row-mibig_compounds-0
- assessment_id: support-2180-A7
  area: completeness
  topic: Partial completion and maintained ownership
  outcome: supported
  summary: All seven core areas and twelve dimensions were assessed against the actual
    intake, complete raw/history, retained source rows/cache and both saved chemical
    forms. Five local commands passed; full QC/OAK and external verification remain
    unavailable. This owner declares no mechanism roots/components and needs no maintained
    reader. The pinned source assertions and local structure are positively supported
    within that scope; no concrete contradiction requiring a finding was established.
    SEEDED status/history and all source records remain unchanged.
  target_ids:
  - CHEBI:17704
  evidence_ids:
  - support-2180-owner
  - support-2180-capture
  - support-2180-intake
  - support-2180-source-plan
  - support-2180-plan-acceptance
  - support-2180-history
  - support-2180-direct-contexts
  - support-2180-intake-acceptance
  - support-2180-native-acceptance
  - support-2180-diagnostic-acceptance
  - support-2180-source-ownership
  dimensions:
  - name: review_completion
    value: partial; QC/OAK/external unavailable; native source/status/history unchanged
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2180-owner
    - support-2180-capture
    - support-2180-intake
    - support-2180-source-plan
    - support-2180-plan-acceptance
    - support-2180-history
    - support-2180-direct-contexts
    - support-2180-intake-acceptance
    - support-2180-native-acceptance
    - support-2180-diagnostic-acceptance
    - support-2180-source-ownership
findings: []
actions: []
limitations:
- No external requests, original-paper reading or live ontology/taxonomy/accession/sibling
  verification. Imported identifiers and quotations retain their source scope.
- All ten saved comparisons agree, but full_graph_identity_established remains false.
  The two original global stereo warnings are unassigned; natural identity and unmeasured
  stereochemistry are not proved.
- Full QC/OAK remain unavailable. Local gate success and selected queue rows do not
  establish scientific completeness.
- Empty retained query frames apply only to the exact pinned key/query; no inactivity,
  literature absence or congener-transfer inference. Curation reading is limited to
  the admitted seven baseline tables; the eighth assay table was supplemental preparation
  only.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Whole selected raw/history and both complete saved molecular tables personally read.
  BGC owns collector/composer and other source partitions; Support owns this target's
  retained payloads and relevant cached stanzas.
- No source, status or history edits, additional molecular/YAML parses, maintained-reader/gate/assembly/canonical
  invocation or outbound activity.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-218
```
