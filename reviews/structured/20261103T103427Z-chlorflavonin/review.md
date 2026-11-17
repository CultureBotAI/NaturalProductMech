# Local evidence review: chlorflavonin

- Review: 20261103T103427Z-chlorflavonin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T09:59:30.053925Z
- Finished UTC: 2026-11-03T10:34:27.813928Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified local review: retained identity, source grades, chemistry and applicable mechanism boundaries are coherent within offline limits.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2192; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3613 | data/natural_products/shikimates_and_phenylpropanoids/chlorflavonin.yaml | generated | chlorflavonin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:3613 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:3613 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:3613 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:3613 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:3613 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:3613 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:3613 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:3613 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: CHEBI:3613.

The exact full key JLSQXYITDXJTKL-UHFFFAOYSA-N joins the retained three-star CHEBI:3613 structure and the BGC0001544 source concept, supporting the written EXACT grounding locally. The source definition and its literal wording remain a database assertion rather than newly verified chemical nomenclature. No name-only or congener substitution was made.

### Representation

representation: supported. Targets: CHEBI:3613.

Both stored forms parse as neutral C18H15ClO7 with 26 atoms and 28 bonds and all ten comparison flags true. The saved tables contain no potential tetrahedral or double-bond stereoelements. Three aromatic rings, one carbonyl, three methoxy groups, two hydroxyls and one chlorine are retained. This local stereo result and the true source flag do not establish every possible axial or natural stereochemical claim; full_graph_identity_established remains false.

### Origin

provenance: supported. Targets: CHEBI:3613.

BGC0001544 v3 records Aspergillus campestris IBT28561 (1392248) as SOURCE_ASSERTION and the locus as CLUSTER_UNSTATED. Its cited DOI is a compound-bioactivity reference, not fresh producer evidence. Five written occurrence assertions comprise four LOTUS rows plus one ChEBI-origin row on species taxa41067/41068, separate from the producer strain. Their cached labels preserve that distinction.

### Citations

evidence: unknown. Targets: CHEBI:3613.

DOI:10.1021/acsinfecdis.7b00055 is explicitly COMPOUND_BIOACTIVITY in the MIBiG row; carrying it on producer/locus fields does not prove those experiments were inspected. Four LOTUS DOIs and ChEBI-origin PMID:5391291 retain their original roles. The identical-key AntibioticMech relation has a pinned source commit, not fresh article access or demonstrated publication independence.

### Bioactivity

evidence: supported. Targets: CHEBI:3613.

No bioactivities or molecular_targets are written and the retained PubChem/BindingDB joins are empty. The ANTIFUNGAL summary nevertheless has an explicit backing route: the same-full-key AntibioticMech row1004 names CHEBI:3613 and ANTIFUNGAL. This supports the coarse retained summary as a sibling-corpus assertion, not an assay endpoint or mechanism. The five occurrence claims remain separate from that activity assertion.

### Classification

consistency: unknown. Targets: CHEBI:3613.

NPClassifier Flavonols and glycoside=false are predictions. The full saved graph supports a flavone-like oxygen heterocycle with a carbonyl, substituted phenyl ring, chlorine and methoxy/hydroxyl groups; no C5O sugar cycle is present. A methoxylated flavonol-related model label is a bounded classification, not proof of a biosynthetic route. MIBiG NRPS/PKS source axes remain distinct from the model filing path.

### Completion

completeness: unknown. Targets: CHEBI:3613.

Complete local source, owner/history and paired molecular tables were reviewed after inspect. No curation defect is established from the retained evidence; the source definition typo is not inflated into an identity finding. External primary/xref verification, full QC and OAK remain unavailable, so this is a qualified partial scientific review with no native-status promotion.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2192-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/chlorflavonin.yaml; Whole owner plaintext and complete curation_history | supports | BGC complete plaintext/history reading, carried by exact current bytes; no new YAML parse or record edit. |
| bgc-2192-capture | /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json; /records/1/owner_document | supports | Complete actual captured owner, including source-owned fields and full history. |
| bgc-2192-intake | /private/tmp/npm-review-work/shared-next-batch220/intakes/2192-inspect-001.json; /source; /targets | supports | Original canonical inspect captures exact target and 37 source inputs; inspection alone does not certify scientific accuracy. |
| bgc-2192-source-plan | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1 | supports | Exact owner/direct/additional input map and complete retained owner/source context for this record; future runtime slots in the plan remain historical nulls. |
| bgc-2192-source-notes | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-scope-notes-001.json; /observer; /recorded_at; /status; /inventory; /inventory_ROOT_acceptance; /inventory_ROOT_acceptance_inventory_key; /original_inventory; /original_collector_execution; /inventory_metadata_correction; /prior_final_acceptance; /accepted_prior_remaining; /frozen_remaining; /collector_source; /totals; /per_order_counts; /reading; /cautions; /curation; /future_result_authorities; /scientific_verdicts; /external_requests; /outbound_active_queued_scheduled_child | supports | Local source-reading attribution is supplied by the complete notes artifact; individual claims below cite their exact owner/source evidence. |
| bgc-2192-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch220/root-source-plan-acceptance-001.json; /status; /plan; /inventory; /source_notes; /actual_intake_ready; /verified | supports | ROOT acceptance of current saved plan and exact actual intake maps. |
| bgc-2192-grounding-owner | /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json; /records/1/owner_document/identifier; /records/1/owner_document/chemical_structure; /records/1/owner_document/grounding_status; /records/1/owner_document/source_concepts | supports | Written identity, full structure, source concepts and grounding scope; xrefs are retained when present. |
| bgc-2192-origin-owner | /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json; /records/1/owner_document/producer_organisms; /records/1/owner_document/biosynthetic_gene_clusters | supports | Written producer/locus claims retain grades, source versions, method categories and exact citations. |
| bgc-2192-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json; /records/1/owner_document/occurrences; /records/1/owner_document/occurrence_taxon_groups | supports | Written occurrence assertions, source labels, references and group labels; no fresh taxon verification. |
| bgc-2192-classification-owner | /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json; /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway; /records/1/owner_document/bgc_class | supports | Written model classifications/filing path and separate source BGC classes. |
| bgc-2192-assay-owner | /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json; /records/1/owner_document/bioactivity_summary; /records/1/owner_document/related_records | supports | Written activity/target/related-record fields only; their presence or absence is bounded to the complete captured owner. |
| bgc-2192-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1/source_scope_inventory/joins/mibig_compounds | supports | Retained complete query frame: Exact saved predicate exact complete standard_inchi_key equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned mibig_compounds table; no new query or external lookup.; 1 matched rows. |
| bgc-2192-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 1856 | supports | Complete retained row fields, including blanks, with physical-frame hashes: [{"physical_line":1856,"row_sha256":"3ccb624478f1f5093fff5a7b54d342582f1808505fcf6b904e140d37e9010c2b","row":{"mibig_accession":"BGC0001544","entry_version":"3","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"chlorflavonin","compound_index":"1","smiles":"COC1=C(C2=C(C(=C1)O)C(=O)C(=C(O2)C3=C(C(=CC=C3)Cl)O)OC)OC","standard_inchi":"InChI=1S/C18H15ClO7/c1-23-11-7-10(20)12-14(22)18(25-3)15(26-17(12)16(11)24-2)8-5-4-6-9(19)13(8)21/h4-7,20-21H,1-3H3","standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"","taxon_id":"NCBITaxon:1392248","taxon_label":"Aspergillus campestris IBT 28561","bgc_classes":"NRPS&#124;PKS","bgc_subclasses":"Type I&#124;Unknown","genome_accession":"MSFM01000001.1","locus_from":"576138","locus_to":"603864","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"DOI:10.1021/acsinfecdis.7b00055","reference_basis":"COMPOUND_BIOACTIVITY"}}] |
| bgc-2192-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1/source_scope_inventory/joins/chebi_structures | supports | Retained complete query frame: Exact saved predicate exact complete standard_inchi_key equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned chebi_structures table; no new query or external lookup.; 1 matched rows. |
| bgc-2192-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Physical TSV lines 671 | supports | Complete retained row fields, including blanks, with physical-frame hashes: [{"physical_line":671,"row_sha256":"4acb869530d56d42f2df36e77bd3a733a46c922848e40efd802658815229b61b","row":{"chebi_id":"CHEBI:3613","name":"chlorflavonin","definition":"A dihydroxyflavone that is flavone substituted by a chloro group at position 3', hydroxy groups at positions 5 and 2' and methoxy groups at positions 3, 7 band 8 respectively.","stars":"3","standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","smiles":"COc1cc(O)c2c(=O)c(OC)c(-c3cccc(Cl)c3O)oc2c1OC"}}] |
| bgc-2192-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1/source_scope_inventory/joins/lotus_occurrences | supports | Retained complete query frame: Exact saved predicate exact complete standard_inchi_key equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned lotus_occurrences table; no new query or external lookup.; 4 matched rows. |
| bgc-2192-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 3441, 3442, 3443, 3444 | supports | Complete retained row fields, including blanks, with physical-frame hashes: [{"physical_line":3441,"row_sha256":"ecad1df17f0be1f4fed5ebf252dd7f9ec16ef03a80c2bd8851e7b598aafbd6cf","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","organism_name":"Aspergillus candidus","taxon_id":"NCBITaxon:41067","organism_wikidata":"http://www.wikidata.org/entity/Q6855122","reference_doi":"10.1271/BBB1961.49.867","structure_wikidata":"http://www.wikidata.org/entity/Q27106149"}},{"physical_line":3442,"row_sha256":"d42d5ec277ffcbe87b148e282b7730e20619c822c5c71f89d04e50e39ba49bb5","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","organism_name":"Aspergillus candidus","taxon_id":"NCBITaxon:41067","organism_wikidata":"http://www.wikidata.org/entity/Q6855122","reference_doi":"10.7164/ANTIBIOTICS.22.388","structure_wikidata":"http://www.wikidata.org/entity/Q27106149"}},{"physical_line":3443,"row_sha256":"31f90d5099635c1631dff21015ed14b42c59ef71c6e6c91c5be1851318aeaaf7","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","organism_name":"Aspergillus campestris","taxon_id":"NCBITaxon:41068","organism_wikidata":"http://www.wikidata.org/entity/Q10419951","reference_doi":"10.1016/S0031-9422(99)00596-8","structure_wikidata":"http://www.wikidata.org/entity/Q27106149"}},{"physical_line":3444,"row_sha256":"c2e8f44735af92c0aa0f36a29fe5acc4a4d2d14cbcc886faec4368c020d6f397","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","organism_name":"Aspergillus campestris","taxon_id":"NCBITaxon:41068","organism_wikidata":"http://www.wikidata.org/entity/Q10419951","reference_doi":"10.1073/PNAS.1715954115","structure_wikidata":"http://www.wikidata.org/entity/Q27106149"}}] |
| bgc-2192-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1/source_scope_inventory/joins/cyanometdb_occurrences | supports | Retained complete query frame: Exact saved predicate exact complete standard_inchi_key equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned cyanometdb_occurrences table; no new query or external lookup.; 0 matched rows. |
| bgc-2192-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1/source_scope_inventory/joins/npclassifier | supports | Retained complete query frame: Exact saved predicate exact complete standard_inchi_key equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned npclassifier table; no new query or external lookup.; 1 matched rows. |
| bgc-2192-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 1129 | supports | Complete retained row fields, including blanks, with physical-frame hashes: [{"physical_line":1129,"row_sha256":"a40d85087aded706eb055ac4d938c886821b67bb6c40fe9616b52c1d85f0fcbe","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","smiles":"COC1=C(C2=C(C(=C1)O)C(=O)C(=C(O2)C3=C(C(=CC=C3)Cl)O)OC)OC","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Flavonoids","class_results":"Flavonols","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}] |
| bgc-2192-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1/source_scope_inventory/joins/pubchem_bioassay | supports | Retained complete query frame: Exact saved predicate exact complete standard_inchi_key equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned pubchem_bioassay table; no new query or external lookup.; 0 matched rows. |
| bgc-2192-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1/source_scope_inventory/joins/bindingdb_targets | supports | Retained complete query frame: Exact saved predicate exact complete standard_inchi_key equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned bindingdb_targets table; no new query or external lookup.; 0 matched rows. |
| bgc-2192-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Retained complete query frame: Exact saved predicate exact complete standard_inchi_key equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned antibioticmech_inchikeys table; no new query or external lookup.; 1 matched rows. |
| bgc-2192-source-antibioticmech_inchikeys | /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv; Physical TSV lines 1004 | supports | Complete retained row fields, including blanks, with physical-frame hashes: [{"physical_line":1004,"row_sha256":"8e77ef5e733b8780613403a0a956d013b9d566f849b1947c2e34652573845efc","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","identifier":"CHEBI:3613","label":"chlorflavonin","antimicrobial_class":"ANTIFUNGAL","slug":"chlorflavonin","corpus_commit":"74f6cc8362498900f2fe2c13d0b6fdb66dd30976"}}] |
| bgc-2192-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1/source_scope_inventory/joins/chebi_origins | supports | Retained complete query frame: Exact saved predicate exact chebi_id from exact full-key structure rows with query ["CHEBI:3613"] over the pinned chebi_origins table; no new query or external lookup.; 1 matched rows. |
| bgc-2192-source-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Physical TSV lines 325 | supports | Complete retained row fields, including blanks, with physical-frame hashes: [{"physical_line":325,"row_sha256":"1628719e94a9689be710af8e9ae4c13c802cf23a3d4d359fb818f4c9df5dcd65","row":{"chebi_id":"CHEBI:3613","species_text":"Aspergillus candidus","species_accession":"41067","component_text":"","strain_text":"","source_accession":"5391291","comments":""}}] |
| bgc-2192-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /cached_taxonomy/whole_stanzas/12; /cached_taxonomy/whole_stanzas/13; /cached_taxonomy/whole_stanzas/53 | supports | Complete saved requested taxon stanzas, locally current and personally read, retain labels/synonyms only: [{"id":"NCBITaxon:41067","physical_line":18441,"complete_stanza":"[Term]\nid: NCBITaxon:41067\nname: Aspergillus candidus\n\n"},{"id":"NCBITaxon:41068","physical_line":18445,"complete_stanza":"[Term]\nid: NCBITaxon:41068\nname: Aspergillus campestris\n\n"},{"id":"NCBITaxon:1392248","physical_line":128218,"complete_stanza":"[Term]\nid: NCBITaxon:1392248\nname: Aspergillus campestris IBT 28561\n\n"}] |
| bgc-2192-source-routes | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/1/source_scope_inventory/source_taxa; /records/1/source_scope_inventory/forward_taxon_merge_matches; /records/1/source_scope_inventory/nonorganism_matches | supports | Exact selected-source taxon and route frames; companion routes remain separate within their own direct context. |
| bgc-2192-chemistry | /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/smiles; /records/1/inchi; /records/1/comparisons; /records/1/atom_correspondence | supports | Original saved paired profiles and full tables: {"comparisons":{"formula_equal":true,"formal_charge_equal":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"smiles_formula_equals_literal_InChI_main_layer":true},"smiles_stereo":{},"inchi_stereo":{}} |
| bgc-2192-topology | /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json; /records/1/smiles/computed/atoms; /records/1/smiles/computed/bonds; /records/1/smiles/computed/rings; /records/1/smiles/computed/motifs; /records/1/smiles/computed/potential_stereo; /records/1/inchi/computed/atoms; /records/1/inchi/computed/bonds; /records/1/inchi/computed/rings; /records/1/inchi/computed/motifs; /records/1/inchi/computed/potential_stereo; /records/1/atom_correspondence; /records/1/declared_structure | supports | Both complete atom/bond/ring/motif/stereo tables personally read. Diagnostic motif matches are graph candidates with bounded applicability, and explicit full-graph identity remains unestablished. |
| bgc-2192-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch220/root-chemistry-acceptance-001.json; /status; /data; /execution; /original_terminal; /scope | supports | ROOT acceptance of the original offline computation, preserved inputs and scope; no scientific verdict. |
| bgc-2192-native-acceptance | /private/tmp/npm-review-work/shared-next-batch220/root-native-gates-acceptance-001.json; /status; /ledger; /outcomes | supports | Accepted five original native checks, with full QC/OAK unavailable; these do not certify scientific accuracy. |
| bgc-2192-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Workflow; Output | supports | Claim-level evidence, scope preservation, major unsupported-claim severity and immutable partial review requirements. |
| bgc-2192-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Native questions and ownership; Native checks and queue | supports | Producer/occurrence/locus/model distinctions, maintained fix ownership and limitations of native gates; reserved decisions.tsv is not an implemented correction route. |
| bgc-2192-stereo-extraction | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 144–173 | supports | The retained stereo_complete flag is derived from FindMolChiralCenters on the source SMILES; it does not independently verify natural stereochemistry or every double-bond geometry. |
| bgc-2192-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 376–402 | supports | Standard InChIKey limits and source stereochemistry requirements; matching keys do not prove all explicit graph or natural-form identity. |
| bgc-2192-activity-classifier | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 128-178; lines 1310-1381 | supports | Maintained classifier promises an unambiguous assay-name class, uses a generic inhibition/binding fallback, adds classes only to ACTIVE observations and derives the activity summary from classified written observations. |
| bgc-2192-activity-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 631-664; lines 920-949 | supports | activity_class is optional; the enum describes backed coarse buckets and has no dedicated ENZYME_INHIBITOR definition. Claim support must still follow the retained observation. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-220/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-220/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-220/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-220/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-220/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- No outbound request was made. Primary papers, DOI/PMID services, database accessions, sequences and external xrefs were not freshly resolved; their factual claims remain attributed to retained local sources.
- Full QC and OAK ontology consistency were unavailable. Accepted native checks, stored-form chemistry and maintained-reader success do not establish scientific accuracy or complete source verification.
- The molecular evidence is the original saved computation on the two stored forms. Normalized identifiers, motif candidates and one substructure correspondence do not independently establish full-graph identity, natural absolute stereochemistry, named sugar residues or biochemical pathway order.
- Cached taxon names and bounded retained source joins do not establish organism identity, publication independence, strain-wide production or global absence. No source record, classification, graph, history or native curation status was edited in this review.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Source inventory/composer and first-five scientific authorship overlap is disclosed; independent scientific peer is separate.
- All current scientific judgments use exact accepted local evidence after canonical inspect. No record/native-status mutation or fresh external verification occurred.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T103427Z-chlorflavonin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: chlorflavonin'
started_at: '2026-11-03T09:59:30.053925Z'
finished_at: '2026-11-03T10:34:27.813928Z'
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
summary: 'Qualified local review: retained identity, source grades, chemistry and
  applicable mechanism boundaries are coherent within offline limits.'
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/chlorflavonin.yaml
    sha256: cd28803db3ffbe954458fddfe2888a276a49f0d2ea460c433d64795df0c90dc9
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
  selection: Campaign path order 2192; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3613
targets:
- target_id: CHEBI:3613
  path: data/natural_products/shikimates_and_phenylpropanoids/chlorflavonin.yaml
  label: chlorflavonin
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
  - CHEBI:3613
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/chartreusin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/chlorflavonin.yaml data/natural_products/shikimates_and_phenylpropanoids/clorobiocin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/colletorin-d-acid.yaml data/natural_products/shikimates_and_phenylpropanoids/collinomycin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml data/natural_products/shikimates_and_phenylpropanoids/coumermycin-a1.yaml
    data/natural_products/shikimates_and_phenylpropanoids/dichlorodiaporthin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/e-n-2-hydroxy-5-oxocyclopent-1-en-1-yl-5-o-tolyl-pent-4-enamide.yaml
    data/natural_products/shikimates_and_phenylpropanoids/echoside-a.yaml --workers
    1 --out /private/tmp/npm-native-checks/batch-220/validate-strict-selected10-001.tsv
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
  - CHEBI:3613
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-220/validate-all-001.tsv
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
  - CHEBI:3613
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
  - CHEBI:3613
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
  - CHEBI:3613
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-220/review-queue-001.tsv
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
  - CHEBI:3613
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:3613
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:3613
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2192-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/chlorflavonin.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: BGC complete plaintext/history reading, carried by exact current bytes;
    no new YAML parse or record edit.
  snapshot_sha256: cd28803db3ffbe954458fddfe2888a276a49f0d2ea460c433d64795df0c90dc9
- evidence_id: bgc-2192-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Complete actual captured owner, including source-owned fields and full
    history.
  snapshot_sha256: 90236bcdb9064859a691606fd163f92576040ab44a954a6323cc0b39871e571d
- evidence_id: bgc-2192-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/intakes/2192-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Original canonical inspect captures exact target and 37 source inputs;
    inspection alone does not certify scientific accuracy.
  snapshot_sha256: a768cb07f2610b2e1c27852dc3d3e04f15b7981a84d2e0bda59532600f330e2c
- evidence_id: bgc-2192-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Exact owner/direct/additional input map and complete retained owner/source
    context for this record; future runtime slots in the plan remain historical nulls.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: bgc-2192-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-scope-notes-001.json
  locator: /observer; /recorded_at; /status; /inventory; /inventory_ROOT_acceptance;
    /inventory_ROOT_acceptance_inventory_key; /original_inventory; /original_collector_execution;
    /inventory_metadata_correction; /prior_final_acceptance; /accepted_prior_remaining;
    /frozen_remaining; /collector_source; /totals; /per_order_counts; /reading; /cautions;
    /curation; /future_result_authorities; /scientific_verdicts; /external_requests;
    /outbound_active_queued_scheduled_child
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Local source-reading attribution is supplied by the complete notes artifact;
    individual claims below cite their exact owner/source evidence.
  snapshot_sha256: aabfc3a0d18af5bd7d41acb95f1f89848cfbd06a962b174ef64b76218295ec7d
- evidence_id: bgc-2192-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-source-plan-acceptance-001.json
  locator: /status; /plan; /inventory; /source_notes; /actual_intake_ready; /verified
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: ROOT acceptance of current saved plan and exact actual intake maps.
  snapshot_sha256: 8a51c9303cf8dd7483b2fc282491f294f43ae3adc3a419819b31fe9531b98f6b
- evidence_id: bgc-2192-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json
  locator: /records/1/owner_document/identifier; /records/1/owner_document/chemical_structure;
    /records/1/owner_document/grounding_status; /records/1/owner_document/source_concepts
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Written identity, full structure, source concepts and grounding scope;
    xrefs are retained when present.
  snapshot_sha256: 90236bcdb9064859a691606fd163f92576040ab44a954a6323cc0b39871e571d
- evidence_id: bgc-2192-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json
  locator: /records/1/owner_document/producer_organisms; /records/1/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Written producer/locus claims retain grades, source versions, method categories
    and exact citations.
  snapshot_sha256: 90236bcdb9064859a691606fd163f92576040ab44a954a6323cc0b39871e571d
- evidence_id: bgc-2192-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json
  locator: /records/1/owner_document/occurrences; /records/1/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Written occurrence assertions, source labels, references and group labels;
    no fresh taxon verification.
  snapshot_sha256: 90236bcdb9064859a691606fd163f92576040ab44a954a6323cc0b39871e571d
- evidence_id: bgc-2192-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json
  locator: /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway;
    /records/1/owner_document/bgc_class
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Written model classifications/filing path and separate source BGC classes.
  snapshot_sha256: 90236bcdb9064859a691606fd163f92576040ab44a954a6323cc0b39871e571d
- evidence_id: bgc-2192-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json
  locator: /records/1/owner_document/bioactivity_summary; /records/1/owner_document/related_records
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Written activity/target/related-record fields only; their presence or absence
    is bounded to the complete captured owner.
  snapshot_sha256: 90236bcdb9064859a691606fd163f92576040ab44a954a6323cc0b39871e571d
- evidence_id: bgc-2192-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Retained complete query frame: Exact saved predicate exact complete standard_inchi_key
    equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned mibig_compounds
    table; no new query or external lookup.; 1 matched rows.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned mibig_compounds table; no
    new query or external lookup.
- evidence_id: bgc-2192-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 1856
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Complete retained row fields, including blanks, with physical-frame hashes:
    [{"physical_line":1856,"row_sha256":"3ccb624478f1f5093fff5a7b54d342582f1808505fcf6b904e140d37e9010c2b","row":{"mibig_accession":"BGC0001544","entry_version":"3","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"chlorflavonin","compound_index":"1","smiles":"COC1=C(C2=C(C(=C1)O)C(=O)C(=C(O2)C3=C(C(=CC=C3)Cl)O)OC)OC","standard_inchi":"InChI=1S/C18H15ClO7/c1-23-11-7-10(20)12-14(22)18(25-3)15(26-17(12)16(11)24-2)8-5-4-6-9(19)13(8)21/h4-7,20-21H,1-3H3","standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"","taxon_id":"NCBITaxon:1392248","taxon_label":"Aspergillus
    campestris IBT 28561","bgc_classes":"NRPS|PKS","bgc_subclasses":"Type I|Unknown","genome_accession":"MSFM01000001.1","locus_from":"576138","locus_to":"603864","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"DOI:10.1021/acsinfecdis.7b00055","reference_basis":"COMPOUND_BIOACTIVITY"}}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2192-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Retained complete query frame: Exact saved predicate exact complete standard_inchi_key
    equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned chebi_structures
    table; no new query or external lookup.; 1 matched rows.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned chebi_structures table; no
    new query or external lookup.
- evidence_id: bgc-2192-source-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Physical TSV lines 671
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Complete retained row fields, including blanks, with physical-frame hashes:
    [{"physical_line":671,"row_sha256":"4acb869530d56d42f2df36e77bd3a733a46c922848e40efd802658815229b61b","row":{"chebi_id":"CHEBI:3613","name":"chlorflavonin","definition":"A
    dihydroxyflavone that is flavone substituted by a chloro group at position 3'',
    hydroxy groups at positions 5 and 2'' and methoxy groups at positions 3, 7 band
    8 respectively.","stars":"3","standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","smiles":"COc1cc(O)c2c(=O)c(OC)c(-c3cccc(Cl)c3O)oc2c1OC"}}]'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2192-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Retained complete query frame: Exact saved predicate exact complete standard_inchi_key
    equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned lotus_occurrences
    table; no new query or external lookup.; 4 matched rows.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned lotus_occurrences table; no
    new query or external lookup.
- evidence_id: bgc-2192-source-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 3441, 3442, 3443, 3444
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Complete retained row fields, including blanks, with physical-frame hashes:
    [{"physical_line":3441,"row_sha256":"ecad1df17f0be1f4fed5ebf252dd7f9ec16ef03a80c2bd8851e7b598aafbd6cf","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","organism_name":"Aspergillus
    candidus","taxon_id":"NCBITaxon:41067","organism_wikidata":"http://www.wikidata.org/entity/Q6855122","reference_doi":"10.1271/BBB1961.49.867","structure_wikidata":"http://www.wikidata.org/entity/Q27106149"}},{"physical_line":3442,"row_sha256":"d42d5ec277ffcbe87b148e282b7730e20619c822c5c71f89d04e50e39ba49bb5","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","organism_name":"Aspergillus
    candidus","taxon_id":"NCBITaxon:41067","organism_wikidata":"http://www.wikidata.org/entity/Q6855122","reference_doi":"10.7164/ANTIBIOTICS.22.388","structure_wikidata":"http://www.wikidata.org/entity/Q27106149"}},{"physical_line":3443,"row_sha256":"31f90d5099635c1631dff21015ed14b42c59ef71c6e6c91c5be1851318aeaaf7","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","organism_name":"Aspergillus
    campestris","taxon_id":"NCBITaxon:41068","organism_wikidata":"http://www.wikidata.org/entity/Q10419951","reference_doi":"10.1016/S0031-9422(99)00596-8","structure_wikidata":"http://www.wikidata.org/entity/Q27106149"}},{"physical_line":3444,"row_sha256":"c2e8f44735af92c0aa0f36a29fe5acc4a4d2d14cbcc886faec4368c020d6f397","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","organism_name":"Aspergillus
    campestris","taxon_id":"NCBITaxon:41068","organism_wikidata":"http://www.wikidata.org/entity/Q10419951","reference_doi":"10.1073/PNAS.1715954115","structure_wikidata":"http://www.wikidata.org/entity/Q27106149"}}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2192-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Retained complete query frame: Exact saved predicate exact complete standard_inchi_key
    equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned cyanometdb_occurrences
    table; no new query or external lookup.; 0 matched rows.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned cyanometdb_occurrences table;
    no new query or external lookup.
- evidence_id: bgc-2192-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Retained complete query frame: Exact saved predicate exact complete standard_inchi_key
    equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned npclassifier
    table; no new query or external lookup.; 1 matched rows.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned npclassifier table; no new
    query or external lookup.
- evidence_id: bgc-2192-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 1129
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Complete retained row fields, including blanks, with physical-frame hashes:
    [{"physical_line":1129,"row_sha256":"a40d85087aded706eb055ac4d938c886821b67bb6c40fe9616b52c1d85f0fcbe","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","smiles":"COC1=C(C2=C(C(=C1)O)C(=O)C(=C(O2)C3=C(C(=CC=C3)Cl)O)OC)OC","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Flavonoids","class_results":"Flavonols","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2192-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Retained complete query frame: Exact saved predicate exact complete standard_inchi_key
    equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned pubchem_bioassay
    table; no new query or external lookup.; 0 matched rows.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned pubchem_bioassay table; no
    new query or external lookup.
- evidence_id: bgc-2192-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Retained complete query frame: Exact saved predicate exact complete standard_inchi_key
    equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned bindingdb_targets
    table; no new query or external lookup.; 0 matched rows.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned bindingdb_targets table; no
    new query or external lookup.
- evidence_id: bgc-2192-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Retained complete query frame: Exact saved predicate exact complete standard_inchi_key
    equality with query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned antibioticmech_inchikeys
    table; no new query or external lookup.; 1 matched rows.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "JLSQXYITDXJTKL-UHFFFAOYSA-N" over the pinned antibioticmech_inchikeys table;
    no new query or external lookup.
- evidence_id: bgc-2192-source-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv
  locator: Physical TSV lines 1004
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Complete retained row fields, including blanks, with physical-frame hashes:
    [{"physical_line":1004,"row_sha256":"8e77ef5e733b8780613403a0a956d013b9d566f849b1947c2e34652573845efc","row":{"standard_inchi_key":"JLSQXYITDXJTKL-UHFFFAOYSA-N","identifier":"CHEBI:3613","label":"chlorflavonin","antimicrobial_class":"ANTIFUNGAL","slug":"chlorflavonin","corpus_commit":"74f6cc8362498900f2fe2c13d0b6fdb66dd30976"}}]'
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
- evidence_id: bgc-2192-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Retained complete query frame: Exact saved predicate exact chebi_id from
    exact full-key structure rows with query ["CHEBI:3613"] over the pinned chebi_origins
    table; no new query or external lookup.; 1 matched rows.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
  search_scope: Exact saved predicate exact chebi_id from exact full-key structure
    rows with query ["CHEBI:3613"] over the pinned chebi_origins table; no new query
    or external lookup.
- evidence_id: bgc-2192-source-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Physical TSV lines 325
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Complete retained row fields, including blanks, with physical-frame hashes:
    [{"physical_line":325,"row_sha256":"1628719e94a9689be710af8e9ae4c13c802cf23a3d4d359fb818f4c9df5dcd65","row":{"chebi_id":"CHEBI:3613","species_text":"Aspergillus
    candidus","species_accession":"41067","component_text":"","strain_text":"","source_accession":"5391291","comments":""}}]'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: bgc-2192-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /cached_taxonomy/whole_stanzas/12; /cached_taxonomy/whole_stanzas/13; /cached_taxonomy/whole_stanzas/53
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Complete saved requested taxon stanzas, locally current and personally
    read, retain labels/synonyms only: [{"id":"NCBITaxon:41067","physical_line":18441,"complete_stanza":"[Term]\nid:
    NCBITaxon:41067\nname: Aspergillus candidus\n\n"},{"id":"NCBITaxon:41068","physical_line":18445,"complete_stanza":"[Term]\nid:
    NCBITaxon:41068\nname: Aspergillus campestris\n\n"},{"id":"NCBITaxon:1392248","physical_line":128218,"complete_stanza":"[Term]\nid:
    NCBITaxon:1392248\nname: Aspergillus campestris IBT 28561\n\n"}]'
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: bgc-2192-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/1/source_scope_inventory/source_taxa; /records/1/source_scope_inventory/forward_taxon_merge_matches;
    /records/1/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Exact selected-source taxon and route frames; companion routes remain separate
    within their own direct context.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: bgc-2192-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/declared_structure; /records/1/smiles; /records/1/inchi; /records/1/comparisons;
    /records/1/atom_correspondence
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: 'Original saved paired profiles and full tables: {"comparisons":{"formula_equal":true,"formal_charge_equal":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"smiles_formula_equals_literal_InChI_main_layer":true},"smiles_stereo":{},"inchi_stereo":{}}'
  snapshot_sha256: 7bfd670e8944734f1da87a78ecd6d4cee7c6a8dd8bbb225b260809c176bb3de7
- evidence_id: bgc-2192-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/smiles/computed/atoms; /records/1/smiles/computed/bonds; /records/1/smiles/computed/rings;
    /records/1/smiles/computed/motifs; /records/1/smiles/computed/potential_stereo;
    /records/1/inchi/computed/atoms; /records/1/inchi/computed/bonds; /records/1/inchi/computed/rings;
    /records/1/inchi/computed/motifs; /records/1/inchi/computed/potential_stereo;
    /records/1/atom_correspondence; /records/1/declared_structure
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Both complete atom/bond/ring/motif/stereo tables personally read. Diagnostic
    motif matches are graph candidates with bounded applicability, and explicit full-graph
    identity remains unestablished.
  snapshot_sha256: 7bfd670e8944734f1da87a78ecd6d4cee7c6a8dd8bbb225b260809c176bb3de7
- evidence_id: bgc-2192-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-chemistry-acceptance-001.json
  locator: /status; /data; /execution; /original_terminal; /scope
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: ROOT acceptance of the original offline computation, preserved inputs and
    scope; no scientific verdict.
  snapshot_sha256: c7b9547299a849c14093f64f88df2ec128f3806a864554cb39d89a2236dae984
- evidence_id: bgc-2192-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-native-gates-acceptance-001.json
  locator: /status; /ledger; /outcomes
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Accepted five original native checks, with full QC/OAK unavailable; these
    do not certify scientific accuracy.
  snapshot_sha256: 8ec4e48edaf25db9df0c202f6b8595e07cc7118c8fd24193c839e9c875f2c5c7
- evidence_id: bgc-2192-review-skill
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Workflow; Output
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Claim-level evidence, scope preservation, major unsupported-claim severity
    and immutable partial review requirements.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2192-review-profile
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Native questions and ownership; Native checks and queue
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Producer/occurrence/locus/model distinctions, maintained fix ownership
    and limitations of native gates; reserved decisions.tsv is not an implemented
    correction route.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2192-stereo-extraction
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 144–173
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: The retained stereo_complete flag is derived from FindMolChiralCenters
    on the source SMILES; it does not independently verify natural stereochemistry
    or every double-bond geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2192-structure-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 376–402
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Standard InChIKey limits and source stereochemistry requirements; matching
    keys do not prove all explicit graph or natural-form identity.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2192-activity-classifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 128-178; lines 1310-1381
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: Maintained classifier promises an unambiguous assay-name class, uses a
    generic inhibition/binding fallback, adds classes only to ACTIVE observations
    and derives the activity summary from classified written observations.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2192-activity-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 631-664; lines 920-949
  accessed_at: '2026-11-03T10:23:23.978779Z'
  support: supports
  summary: activity_class is optional; the enum describes backed coarse buckets and
    has no dedicated ENZYME_INHIBITOR definition. Claim support must still follow
    the retained observation.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:05:35.934949Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 3eb7a41f227bc3766da4ddb5affcab339127e3eec377a38a928d989861e7bca3
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:06:00.493115Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: b0fee61c050e78f367a4ad7e88aa28c2e04159e5fc41cb9fdd8c3cc0c524bbf8
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:06:19.575968Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:06:54.142706Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:07:06.355777Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 6b8a6b8cb74ddc70b591fb67b612031f05b241b0a0c649cdb0317a6bdeabfb46
assessments:
- assessment_id: bgc-2192-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The exact full key JLSQXYITDXJTKL-UHFFFAOYSA-N joins the retained three-star
    CHEBI:3613 structure and the BGC0001544 source concept, supporting the written
    EXACT grounding locally. The source definition and its literal wording remain
    a database assertion rather than newly verified chemical nomenclature. No name-only
    or congener substitution was made.
  target_ids:
  - CHEBI:3613
  evidence_ids:
  - bgc-2192-owner
  - bgc-2192-capture
  - bgc-2192-intake
  - bgc-2192-grounding-owner
  - bgc-2192-source-plan
  - bgc-2192-query-chebi_structures
  - bgc-2192-source-mibig_compounds
  - bgc-2192-chemistry
  - bgc-2192-source-chebi_structures
  - bgc-2192-source-chebi_origins
  dimensions:
  - name: standard_inchi_key
    value: JLSQXYITDXJTKL-UHFFFAOYSA-N
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2192-owner
    - bgc-2192-capture
    - bgc-2192-intake
    - bgc-2192-grounding-owner
    - bgc-2192-source-plan
    - bgc-2192-query-chebi_structures
    - bgc-2192-source-mibig_compounds
    - bgc-2192-chemistry
    - bgc-2192-source-chebi_structures
    - bgc-2192-source-chebi_origins
  - name: grounding_scope
    value: EXACT retained CHEBI3613 full-key join with MIBiG BGC0001544 v3.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2192-owner
    - bgc-2192-capture
    - bgc-2192-intake
    - bgc-2192-grounding-owner
    - bgc-2192-source-plan
    - bgc-2192-query-chebi_structures
    - bgc-2192-source-mibig_compounds
    - bgc-2192-chemistry
    - bgc-2192-source-chebi_structures
    - bgc-2192-source-chebi_origins
- assessment_id: bgc-2192-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both stored forms parse as neutral C18H15ClO7 with 26 atoms and 28 bonds
    and all ten comparison flags true. The saved tables contain no potential tetrahedral
    or double-bond stereoelements. Three aromatic rings, one carbonyl, three methoxy
    groups, two hydroxyls and one chlorine are retained. This local stereo result
    and the true source flag do not establish every possible axial or natural stereochemical
    claim; full_graph_identity_established remains false.
  target_ids:
  - CHEBI:3613
  evidence_ids:
  - bgc-2192-chemistry
  - bgc-2192-topology
  - bgc-2192-diagnostic-acceptance
  - bgc-2192-stereo-extraction
  - bgc-2192-structure-schema
  dimensions:
  - name: stereochemistry_scope
    value: No potential tetrahedral/double-bond elements in either form; no independent
      axial/natural claim.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2192-chemistry
    - bgc-2192-topology
    - bgc-2192-diagnostic-acceptance
    - bgc-2192-stereo-extraction
    - bgc-2192-structure-schema
  - name: representation_correspondence
    value: 10/10 comparisons true;26 atoms/28 bonds; full-graph identity not established.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2192-chemistry
    - bgc-2192-topology
    - bgc-2192-diagnostic-acceptance
    - bgc-2192-stereo-extraction
    - bgc-2192-structure-schema
- assessment_id: bgc-2192-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: BGC0001544 v3 records Aspergillus campestris IBT28561 (1392248) as SOURCE_ASSERTION
    and the locus as CLUSTER_UNSTATED. Its cited DOI is a compound-bioactivity reference,
    not fresh producer evidence. Five written occurrence assertions comprise four
    LOTUS rows plus one ChEBI-origin row on species taxa41067/41068, separate from
    the producer strain. Their cached labels preserve that distinction.
  target_ids:
  - CHEBI:3613
  evidence_ids:
  - bgc-2192-origin-owner
  - bgc-2192-occurrence-owner
  - bgc-2192-source-mibig_compounds
  - bgc-2192-source-lotus_occurrences
  - bgc-2192-cached-taxonomy
  - bgc-2192-source-routes
  - bgc-2192-review-profile
  - bgc-2192-source-chebi_structures
  - bgc-2192-source-chebi_origins
  dimensions:
  - name: taxon_scope
    value: Species41067/41068 occurrences separate from strain1392248 producer.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2192-origin-owner
    - bgc-2192-occurrence-owner
    - bgc-2192-source-mibig_compounds
    - bgc-2192-source-lotus_occurrences
    - bgc-2192-cached-taxonomy
    - bgc-2192-source-routes
    - bgc-2192-review-profile
    - bgc-2192-source-chebi_structures
    - bgc-2192-source-chebi_origins
  - name: producer_evidence
    value: SOURCE_ASSERTION for Aspergillus campestris IBT28561.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2192-origin-owner
    - bgc-2192-occurrence-owner
    - bgc-2192-source-mibig_compounds
    - bgc-2192-source-lotus_occurrences
    - bgc-2192-cached-taxonomy
    - bgc-2192-source-routes
    - bgc-2192-review-profile
    - bgc-2192-source-chebi_structures
    - bgc-2192-source-chebi_origins
  - name: locus_evidence
    value: BGC0001544 v3 CLUSTER_UNSTATED; MSFM01000001.1:576138..603864.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2192-origin-owner
    - bgc-2192-occurrence-owner
    - bgc-2192-source-mibig_compounds
    - bgc-2192-source-lotus_occurrences
    - bgc-2192-cached-taxonomy
    - bgc-2192-source-routes
    - bgc-2192-review-profile
    - bgc-2192-source-chebi_structures
    - bgc-2192-source-chebi_origins
- assessment_id: bgc-2192-citations
  area: evidence
  topic: Citations
  outcome: unknown
  summary: DOI:10.1021/acsinfecdis.7b00055 is explicitly COMPOUND_BIOACTIVITY in the
    MIBiG row; carrying it on producer/locus fields does not prove those experiments
    were inspected. Four LOTUS DOIs and ChEBI-origin PMID:5391291 retain their original
    roles. The identical-key AntibioticMech relation has a pinned source commit, not
    fresh article access or demonstrated publication independence.
  target_ids:
  - CHEBI:3613
  evidence_ids:
  - bgc-2192-origin-owner
  - bgc-2192-occurrence-owner
  - bgc-2192-source-mibig_compounds
  - bgc-2192-source-lotus_occurrences
  - bgc-2192-assay-owner
  - bgc-2192-source-chebi_structures
  - bgc-2192-source-chebi_origins
  - bgc-2192-source-antibioticmech_inchikeys
  dimensions:
  - name: citation_scope
    value: MIBiG COMPOUND_BIOACTIVITY DOI versus four LOTUS and one ChEBI-origin citation;
      no fresh primary access.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2192-origin-owner
    - bgc-2192-occurrence-owner
    - bgc-2192-source-mibig_compounds
    - bgc-2192-source-lotus_occurrences
    - bgc-2192-assay-owner
    - bgc-2192-source-chebi_structures
    - bgc-2192-source-chebi_origins
    - bgc-2192-source-antibioticmech_inchikeys
- assessment_id: bgc-2192-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: 'No bioactivities or molecular_targets are written and the retained PubChem/BindingDB
    joins are empty. The ANTIFUNGAL summary nevertheless has an explicit backing route:
    the same-full-key AntibioticMech row1004 names CHEBI:3613 and ANTIFUNGAL. This
    supports the coarse retained summary as a sibling-corpus assertion, not an assay
    endpoint or mechanism. The five occurrence claims remain separate from that activity
    assertion.'
  target_ids:
  - CHEBI:3613
  evidence_ids:
  - bgc-2192-assay-owner
  - bgc-2192-occurrence-owner
  - bgc-2192-query-pubchem_bioassay
  - bgc-2192-query-bindingdb_targets
  - bgc-2192-query-antibioticmech_inchikeys
  - bgc-2192-source-plan
  - bgc-2192-source-antibioticmech_inchikeys
  dimensions:
  - name: occurrence_scope
    value: Five written occurrence assertions, two species, from four LOTUS and one
      ChEBI-origin row.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2192-assay-owner
    - bgc-2192-occurrence-owner
    - bgc-2192-query-pubchem_bioassay
    - bgc-2192-query-bindingdb_targets
    - bgc-2192-query-antibioticmech_inchikeys
    - bgc-2192-source-plan
    - bgc-2192-source-antibioticmech_inchikeys
  - name: assay_target_scope
    value: No written assays/targets; explicit same-key sibling ANTIFUNGAL backing,
      not assay evidence.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2192-assay-owner
    - bgc-2192-occurrence-owner
    - bgc-2192-query-pubchem_bioassay
    - bgc-2192-query-bindingdb_targets
    - bgc-2192-query-antibioticmech_inchikeys
    - bgc-2192-source-plan
    - bgc-2192-source-antibioticmech_inchikeys
- assessment_id: bgc-2192-classification
  area: consistency
  topic: Classification
  outcome: unknown
  summary: NPClassifier Flavonols and glycoside=false are predictions. The full saved
    graph supports a flavone-like oxygen heterocycle with a carbonyl, substituted
    phenyl ring, chlorine and methoxy/hydroxyl groups; no C5O sugar cycle is present.
    A methoxylated flavonol-related model label is a bounded classification, not proof
    of a biosynthetic route. MIBiG NRPS/PKS source axes remain distinct from the model
    filing path.
  target_ids:
  - CHEBI:3613
  evidence_ids:
  - bgc-2192-classification-owner
  - bgc-2192-source-npclassifier
  - bgc-2192-source-mibig_compounds
  - bgc-2192-chemistry
  - bgc-2192-topology
  - bgc-2192-review-profile
  dimensions:
  - name: classification_applicability
    value: Predicted Flavonols; flavone-like methoxylated/chlorinated graph without
      C5O sugar; NRPS/PKS source separate.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2192-classification-owner
    - bgc-2192-source-npclassifier
    - bgc-2192-source-mibig_compounds
    - bgc-2192-chemistry
    - bgc-2192-topology
    - bgc-2192-review-profile
- assessment_id: bgc-2192-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: Complete local source, owner/history and paired molecular tables were reviewed
    after inspect. No curation defect is established from the retained evidence; the
    source definition typo is not inflated into an identity finding. External primary/xref
    verification, full QC and OAK remain unavailable, so this is a qualified partial
    scientific review with no native-status promotion.
  target_ids:
  - CHEBI:3613
  evidence_ids:
  - bgc-2192-owner
  - bgc-2192-intake
  - bgc-2192-source-notes
  - bgc-2192-native-acceptance
  - bgc-2192-diagnostic-acceptance
  - bgc-2192-review-skill
  - bgc-2192-review-profile
  - bgc-2192-source-plan
  dimensions:
  - name: review_completion
    value: Qualified partial; no supported defect; external/full QC/OAK unavailable.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2192-owner
    - bgc-2192-intake
    - bgc-2192-source-notes
    - bgc-2192-native-acceptance
    - bgc-2192-diagnostic-acceptance
    - bgc-2192-review-skill
    - bgc-2192-review-profile
    - bgc-2192-source-plan
findings: []
actions: []
limitations:
- No outbound request was made. Primary papers, DOI/PMID services, database accessions,
  sequences and external xrefs were not freshly resolved; their factual claims remain
  attributed to retained local sources.
- Full QC and OAK ontology consistency were unavailable. Accepted native checks, stored-form
  chemistry and maintained-reader success do not establish scientific accuracy or
  complete source verification.
- The molecular evidence is the original saved computation on the two stored forms.
  Normalized identifiers, motif candidates and one substructure correspondence do
  not independently establish full-graph identity, natural absolute stereochemistry,
  named sugar residues or biochemical pathway order.
- Cached taxon names and bounded retained source joins do not establish organism identity,
  publication independence, strain-wide production or global absence. No source record,
  classification, graph, history or native curation status was edited in this review.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Source inventory/composer and first-five scientific authorship overlap is disclosed;
  independent scientific peer is separate.
- All current scientific judgments use exact accepted local evidence after canonical
  inspect. No record/native-status mutation or fresh external verification occurred.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-220
```
