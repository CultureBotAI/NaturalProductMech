# Local evidence review: avermitilol

- Review: 20261103T185021Z-avermitilol
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T18:10:20.610495Z
- Finished UTC: 2026-11-03T18:50:21.979510Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Avermitilol is locally consistent with its full-key ChEBI/MIBiG structure and retained recombinant Tpc1 reaction annotations. The applied locus override supports the written locus grade while native producer and historical protein-identity claims remain separately limited. Scientific completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2274; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:63702 | data/natural_products/terpenoids/avermitilol.yaml | generated | avermitilol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for avermitilol | passed | True | CHEBI:63702 | One original offline maintained call preserved the complete owner and historical mechanism content; mechanical preservation is distinct from fresh scientific verification. |
| strict_ten | passed | True | CHEBI:63702 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:63702 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:63702 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:63702 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:63702 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:63702 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:63702 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:63702 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: CHEBI:63702.

CHEBI:63702 and MIBiG BGC0000683 version 3, compound index 1, share complete key BLGPPSRDEKNCLT-CDWXYHGHSA-N. The ChEBI definition describes the carbotricyclic tetramethyl alcohol and a specified diastereomer. Both saved forms reproduce neutral C15H26O and the saturated tricyclic alcohol topology. This establishes retained definition/structure compatibility without independently verifying the natural isolated product.

### Representation

representation: supported. Targets: CHEBI:63702.

Both forms contain 16 atoms, 18 bonds and one fragment, with six-, six- and three-membered rings. Six specified SMILES centres C0 R, C3 S, C5 S, C9 R, C11 S and C12 R correspond to InChI atoms 9, 14, 10, 8, 11 and 12. Ten comparison flags and the complete stored correspondence agree. No unspecified potential stereochemistry is reported within the diagnostic's supported scope, but independent full-graph and natural identity remain unestablished.

### Origin

provenance: supported. Targets: CHEBI:63702.

The raw BGC0000683 version 3 row is active, questionable and of unknown completeness, with no locus method. The maintained locus override at physical line 5 replaces that method with Enzymatic assays, explaining the written CLUSTER_DEMONSTRATED grade. Its rationale is recombinant SAV_76 incubation with farnesyl diphosphate; it expressly does not upgrade native production. Streptomyces avermitilis MA-4680 = NBRC 14893, taxon 227882, therefore remains SOURCE_ASSERTION, separately from the species-level LOTUS occurrence at 33903. The written interval is genbank:BA000030.3, 86073–87080.

### Citations

evidence: supported. Targets: CHEBI:63702.

The MIBiG producer/locus assertions use ENTRY PMID:20536237; the applied override explains its recombinant-assay scope. The historical graph and pathway retain a DOI:10.1021/ja103087w snippet, MIBiG version 3 database assertions and a 2026-09-30 UniProt annotation. Repetition of these same references on two edges and one step does not create independent experiments. The uppercase LOTUS DOI is another occurrence assertion, not a separate native-production demonstration. These complete retained annotations were read without fresh article, database or sequence access.

### Bioactivity

evidence: supported. Targets: CHEBI:63702.

One written LOTUS occurrence reports the species Streptomyces avermitilis, taxon 33903; it does not establish production by strain 227882. No bioactivities or molecular targets are written, and the exact retained PubChem, BindingDB and AntibioticMech joins are empty. The biosynthetic enzyme is not a pharmacological target. The accepted reader preserves the one graph and one pathway step but does not add an assay or producer observation.

### Classification

consistency: supported. Targets: CHEBI:63702.

The source TERPENE class and NPClassifier Terpenoids / Sesquiterpenoids / Cycloeudesmane sesquiterpenoids are distinct assertions. The named model's is_glycoside:false is compatible with the complete saturated tricyclic C15 alcohol and absence of a sugar residue or glycosidic linkage. That structural compatibility is separate from the historically attributed recombinant reaction and does not establish a complete natural pathway.

### Completion

completeness: unknown. Targets: CHEBI:63702.

All required scientific dimensions were assessed against the current owner, actual intake, retained source payloads and complete paired molecular tables. Five local gates passed, while full QC and complete OAK authority coverage remain unavailable. The accepted maintained reader preserved the complete mechanism owner; its success does not refresh primary, sequence or construct evidence. External facts remain unverified under the no-request instruction, so completion is partial and native curation status is unchanged.

### Mechanism

graph: supported. Targets: CHEBI:63702.

The accepted maintained reader returned the complete owner with one BIOSYNTHESIS graph, three nodes, two directed edges and one pathway step. The graph represents (2E,6E)-farnesyl diphosphate being cyclized by Tpc1 and Tpc1 forming avermitilol; the step retains CHEBI:175763 → CHEBI:63702 and RHEA:32023. Each edge and the step carries the same three reference placements. The primary-experiment snippet concerns recombinant SAV_76, while MIBiG and UniProt entries are historical database assertions. Direction and owner/product scope are coherent locally; neither topology validation nor repeated references demonstrate native production or a complete physiological pathway.

### Protein

grounding: unknown. Targets: CHEBI:63702.

The enzyme node and pathway retain UniProtKB:Q82RR7 for Streptomyces avermitilis MA-4680 Tpc1/SAV_76, with the historical note linking EMBL BA000030 protein BAC67785.1 and RHEA:32023. These are organism-specific native-reference annotations. The recombinant-assay snippet does not supply a complete construct, tag, residue boundary or sequence comparison, and no fresh accession or sequence was inspected. Preserve that unresolved construct-to-native identity boundary rather than treating the current local identifier as newly verified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2274-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/avermitilol.yaml; Whole owner plaintext and complete curation_history | supports | Complete current owner and all 4 ordered history entries personally read; native curation_status remains SEEDED. |
| bgc-2274-capture | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/3/owner_pin; /records/3/owner_document | supports | Exact complete captured owner, including all written fields and history. |
| bgc-2274-intake | /private/tmp/npm-review-work/shared-next-batch228/intakes/2274-inspect-001.json; /source; /targets | supports | Actual canonical one-record intake for CHEBI:63702 with 39 current source inputs and explicit field ownership. |
| bgc-2274-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-intake-ready-001.json; /accepted; /intake_summary; /verification | supports | ROOT accepts the ten original canonical intakes and their exact current ownership/source maps. |
| bgc-2274-grounding-owner | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/3/owner_document/identifier; /records/3/owner_document/label; /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status; /records/3/owner_document/definition; /records/3/owner_document/definition_source | supports | Complete written identity and definition/provenance fields: {"chemical_structure": {"smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C", "standard_inchi": "InChI=1S/C15H26O/c1-9-5-6-11(16)15(4)8-7-10-13(12(9)15)14(10,2)3/h9-13,16H,5-8H2,1-4H3/t9-,10-,11+,12+,13-,15-/m1/s1", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0000683"}, "definition": "A carbotricyclic compound that consists of decahydro-1H-1H-cyclopropa[a]naphthalene bearing four methyl substituents at position 1, 1, 3a and 7 as well as a hydroxy substituent at position 4 (the (1aR,3aS,4S,7R,7aS,7bR)-diastereomer).", "definition_source": "CHEBI:63702", "grounding_status": "EXACT", "identifier": "CHEBI:63702", "label": "avermitilol", "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-83a1fc1265", "source": "MIBIG", "source_id": "BGC0000683", "source_label": "avermitilol", "source_version": "3"}, {"minted_identifier": "naturalproductmech:chebi-65dfe9e019", "source": "CHEBI", "source_id": "CHEBI:63702", "source_label": "avermitilol", "source_version": "3-star"}]} |
| bgc-2274-origin-owner | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters; /records/3/owner_document/producer_taxon_groups | supports | Complete written producer and locus claims with their separate evidence grades: {"biosynthetic_gene_clusters": [{"accession": "mibig:BGC0000683", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0000683 entry version 3; citation taken from the entry level", "reference": "PMID:20536237"}], "genome_accession": "genbank:BA000030.3", "link_evidence_basis": "CLUSTER_DEMONSTRATED", "locus_evidence_methods": ["Enzymatic assays"], "locus_from": 86073, "locus_to": 87080, "organism_label": "Streptomyces avermitilis MA-4680 = NBRC 14893", "organism_taxon_id": "NCBITaxon:227882"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0000683", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0000683 entry version 3; citation taken from the entry level", "reference": "PMID:20536237"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: Enzymatic assays. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id": "NCBITaxon:227882", "taxon_label": "Streptomyces avermitilis MA-4680 = NBRC 14893"}], "producer_taxon_groups": ["ACTINOBACTERIAL"]} |
| bgc-2274-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/3/owner_document | supports | The complete owner establishes present or absent occurrences. Written occurrence fields and any omission notes: {"occurrence_taxon_groups": ["ACTINOBACTERIAL"], "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.", "reference": "DOI:10.1021/JA103087W"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562", "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces avermitilis", "taxon_source": "NCBITaxon"}]} |
| bgc-2274-assay-owner | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete owner establishes assay, target and mechanism-root presence without inferring biological absence: {} |
| bgc-2274-classification-owner | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/3/owner_document/np_pathway; /records/3/owner_document/np_classification; /records/3/owner_document/bgc_class | supports | Literal source BGC classification and named/versioned computed classification remain separate: {"bgc_class": ["TERPENE"], "np_classification": {"class_results": ["Cycloeudesmane sesquiterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Sesquiterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS"} |
| bgc-2274-chemistry | /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json; /records/3/declared_structure; /records/3/smiles/status; /records/3/inchi/status; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons; /records/3/atom_correspondence | supports | Both saved forms parsed. Their complete atom/bond/ring/stereo/motif tables and correspondence were personally read. Saved declared structure and comparison facts: {"comparisons": {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared": true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal": true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer": true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "declared_structure": {"smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C", "standard_inchi": "InChI=1S/C15H26O/c1-9-5-6-11(16)15(4)8-7-10-13(12(9)15)14(10,2)3/h9-13,16H,5-8H2,1-4H3/t9-,10-,11+,12+,13-,15-/m1/s1", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0000683"}, "inchi_formula": "C15H26O", "smiles_formula": "C15H26O"} |
| bgc-2274-topology | /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/atom_correspondence | supports | The complete SMILES table contains a saturated C15 carbon framework with six-, six- and three-membered rings and one alcohol at C5–O6H. All 18 bonds are single. Six tetrahedral centres are specified; there is no carbonyl, sugar residue or glycosidic linkage. |
| bgc-2274-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-execution-001.json; /command; /cwd; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr; /external_requests | supports | Original process receipt has exit 0 and retains exact stdout/stderr, clocks, command and source; no external request. |
| bgc-2274-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-local-diagnostics-acceptance-001.json; /accepted; /DATA; /execution; /verification; /unspecified_stereo; /limits | supports | ROOT accepts the original 20 stored-form parses and current dependency joins. The two original undefined-stereo warnings remain global and unassigned; full QC/OAK and scientific verification limits remain explicit. |
| bgc-2274-native-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-native-five-gates-acceptance-001.json; /five_exits; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows | supports | Five local gates passed. Full QC and complete OAK authority coverage remain unavailable; all_native_gates_passed is false. The selected queue is a local review aid, not proof of the scientific assertions. |
| bgc-2274-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch228-tentative/root-source-inventory-acceptance-001.json; /inventory; /verification; /reading_scope | supports | ROOT accepts the original retained inventory and exact current maps; scientific source-payload reading is separately attributed. |
| bgc-2274-plan | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/3; /source_placement_count; /unique_source_path_count | supports | Accepted source plan retains this exact owner and its input/context roles within 448 placements and 78 unique paths. |
| bgc-2274-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-input-plan-acceptance-001.json; /accepted; /plan; /source_notes; /source_placements; /unique_source_paths; /current_record_and_all_source_pins | supports | ROOT accepts the actual composed plan and current input/owner joins, separately from scientific judgments. |
| bgc-2274-source-notes | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-scope-notes-001.json; /reading; /curation; /cautions | supports | Complete personal and delegated source readings, exact bounded curation scan, source grades and limits are recorded. No external source refresh or congener transfer is implied. |
| bgc-2274-direct-contexts | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /records/3/direct_companion_paths; /records/3/direct_companion_predicates | supports | Exact direct-context paths and one-hop predicates: {"direct_companion_paths": [], "direct_companion_predicates": []} |
| bgc-2274-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/mibig_compounds | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [{"last_physical_line": 819, "physical_line": 819, "raw_tsv_record": "BGC0000683\t3\tactive\tquestionable\tunknown\tavermitilol\t1\t[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C\tInChI=1S/C15H26O/c1-9-5-6-11(16)15(4)8-7-10-13(12(9)15)14(10,2)3/h9-13,16H,5-8H2,1-4H3/t9-,10-,11+,12+,13-,15-/m1/s1\tBLGPPSRDEKNCLT-CDWXYHGHSA-N\ttrue\t\tnpatlas:NPA019411\tNCBITaxon:227882\tStreptomyces avermitilis MA-4680 = NBRC 14893\tterpene\tUnknown\tBA000030.3\t86073\t87080\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:20536237\tENTRY\n", "row": {"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "avermitilol", "database_ids": "npatlas:NPA019411", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "BA000030.3", "locus_evidence_methods": "", "locus_from": "86073", "locus_to": "87080", "mibig_accession": "BGC0000683", "primary_reference": "PMID:20536237", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C", "standard_inchi": "InChI=1S/C15H26O/c1-9-5-6-11(16)15(4)8-7-10-13(12(9)15)14(10,2)3/h9-13,16H,5-8H2,1-4H3/t9-,10-,11+,12+,13-,15-/m1/s1", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:227882", "taxon_label": "Streptomyces avermitilis MA-4680 = NBRC 14893"}, "row_sha256": "20ed5837f2130d80079011b55e1b719316cc975a06a53e30e77ed798bc56b618"}], "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"} |
| bgc-2274-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 819–819; row_sha256 20ed5837f2130d80079011b55e1b719316cc975a06a53e30e77ed798bc56b618 | supports | Complete physical source rows, all fields personally read and joined to the pinned table: [{"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "avermitilol", "database_ids": "npatlas:NPA019411", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "BA000030.3", "locus_evidence_methods": "", "locus_from": "86073", "locus_to": "87080", "mibig_accession": "BGC0000683", "primary_reference": "PMID:20536237", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C", "standard_inchi": "InChI=1S/C15H26O/c1-9-5-6-11(16)15(4)8-7-10-13(12(9)15)14(10,2)3/h9-13,16H,5-8H2,1-4H3/t9-,10-,11+,12+,13-,15-/m1/s1", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:227882", "taxon_label": "Streptomyces avermitilis MA-4680 = NBRC 14893"}] |
| bgc-2274-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/chebi_structures | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [{"last_physical_line": 20440, "physical_line": 20440, "raw_tsv_record": "CHEBI:63702\tavermitilol\tA carbotricyclic compound that consists of decahydro-1H-1H-cyclopropa[a]naphthalene bearing four methyl substituents at position 1, 1, 3a and 7 as well as a hydroxy substituent at position 4 (the (1aR,3aS,4S,7R,7aS,7bR)-diastereomer).\t3\tBLGPPSRDEKNCLT-CDWXYHGHSA-N\t[H][C@@]12[C@H](C)CC[C@H](O)[C@@]1(C)CC[C@@H]1[C@H]2C1(C)C\n", "row": {"chebi_id": "CHEBI:63702", "definition": "A carbotricyclic compound that consists of decahydro-1H-1H-cyclopropa[a]naphthalene bearing four methyl substituents at position 1, 1, 3a and 7 as well as a hydroxy substituent at position 4 (the (1aR,3aS,4S,7R,7aS,7bR)-diastereomer).", "name": "avermitilol", "smiles": "[H][C@@]12[C@H](C)CC[C@H](O)[C@@]1(C)CC[C@@H]1[C@H]2C1(C)C", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stars": "3"}, "row_sha256": "454c8be5e44b15a9c0b11463f860c6e7ecf090ebd8a1f15520795b03670b7013"}], "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"} |
| bgc-2274-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line 1; physical lines 20440–20440; row_sha256 454c8be5e44b15a9c0b11463f860c6e7ecf090ebd8a1f15520795b03670b7013 | supports | Complete physical source rows, all fields personally read and joined to the pinned table: [{"chebi_id": "CHEBI:63702", "definition": "A carbotricyclic compound that consists of decahydro-1H-1H-cyclopropa[a]naphthalene bearing four methyl substituents at position 1, 1, 3a and 7 as well as a hydroxy substituent at position 4 (the (1aR,3aS,4S,7R,7aS,7bR)-diastereomer).", "name": "avermitilol", "smiles": "[H][C@@]12[C@H](C)CC[C@H](O)[C@@]1(C)CC[C@@H]1[C@H]2C1(C)C", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stars": "3"}] |
| bgc-2274-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/lotus_occurrences | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [{"last_physical_line": 547, "physical_line": 547, "raw_tsv_record": "BLGPPSRDEKNCLT-CDWXYHGHSA-N\tStreptomyces avermitilis\tNCBITaxon:33903\thttp://www.wikidata.org/entity/Q1946562\t10.1021/JA103087W\thttp://www.wikidata.org/entity/Q27132738\n", "row": {"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562", "reference_doi": "10.1021/JA103087W", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27132738", "taxon_id": "NCBITaxon:33903"}, "row_sha256": "f2d11f6d25a7e6f29a5741bf4359fbe35128f7eaaa3dc9dc2a2ff05ef5be9f7c"}], "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"} |
| bgc-2274-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 547–547; row_sha256 f2d11f6d25a7e6f29a5741bf4359fbe35128f7eaaa3dc9dc2a2ff05ef5be9f7c | supports | Complete physical source rows, all fields personally read and joined to the pinned table: [{"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562", "reference_doi": "10.1021/JA103087W", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27132738", "taxon_id": "NCBITaxon:33903"}] |
| bgc-2274-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/cyanometdb_occurrences | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"} |
| bgc-2274-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/npclassifier | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [{"last_physical_line": 191, "physical_line": 191, "raw_tsv_record": "BLGPPSRDEKNCLT-CDWXYHGHSA-N\t[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C\tTerpenoids\tSesquiterpenoids\tCycloeudesmane sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results": "Cycloeudesmane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "superclass_results": "Sesquiterpenoids"}, "row_sha256": "1e56361dd43c5dfd758c03341c874f9222ed6739c489f34c93f0f44316325e4c"}], "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"} |
| bgc-2274-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 191–191; row_sha256 1e56361dd43c5dfd758c03341c874f9222ed6739c489f34c93f0f44316325e4c | supports | Complete physical source rows, all fields personally read and joined to the pinned table: [{"class_results": "Cycloeudesmane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "superclass_results": "Sesquiterpenoids"}] |
| bgc-2274-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/pubchem_bioassay | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"} |
| bgc-2274-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/bindingdb_targets | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"} |
| bgc-2274-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"} |
| bgc-2274-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/chebi_origins | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows", "query": ["CHEBI:63702"]} |
| bgc-2274-source-routes | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/source_taxa; /contexts/18/source_scope_inventory/forward_taxon_merge_matches; /contexts/18/source_scope_inventory/nonorganism_matches; /contexts/18/source_scope_inventory/actual_assay_rows; /contexts/18/source_scope_inventory/blank_AID_sentinels; /contexts/18/source_scope_inventory/related_corpus_rows | supports | Exact source taxa and route lists, distinguishing forward merges/nonorganism matches and blank sentinels from actual assays: {"actual_assay_rows": [], "blank_AID_sentinels": [], "forward_taxon_merge_matches": [], "nonorganism_matches": [], "related_corpus_rows": [], "source_taxa": ["NCBITaxon:227882", "NCBITaxon:33903"]} |
| bgc-2274-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/14; /cached_taxonomy/whole_stanzas/53; /cached_taxonomy/unmatched_ids | supports | Complete retained cache stanzas for this source-taxon scope, with cache misses retained globally and no fresh taxonomy or ancestry assertion: [{"complete_stanza": "[Term]\nid: NCBITaxon:33903\nname: Streptomyces avermitilis\nsynonym: \"Streptomyces avermectinius\" EXACT []\n\n", "id": "NCBITaxon:33903", "physical_line": 14687}, {"complete_stanza": "[Term]\nid: NCBITaxon:227882\nname: Streptomyces avermitilis MA-4680 = NBRC 14893\nsynonym: \"Streptomyces avermitilis MA-4680\" EXACT []\nsynonym: \"Streptomyces avermitilis NBRC 14893\" EXACT []\nsynonym: \"Streptomyces avermitilis NBRC 14893 = MA-4680\" EXACT []\n\n", "id": "NCBITaxon:227882", "physical_line": 69123}] |
| bgc-2274-curation-scope | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-scope-notes-001.json; /curation | supports | One bounded eight-table scan used 161 exact literals over 93 data rows, including ignored files by direct access. The only hit is the Avermitilol locus override at physical line 5; applicability is owner-specific. Reserved decisions.tsv was not consumed. PubChem exclusions were supplementary and are outside this batch input map. |
| bgc-2274-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure and ComputedClassification distinguish unspecified stereocentres, normalized keys and named/versioned model predictions; the latter are not source assertions or admission grounds. |
| bgc-2274-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–174 | supports | The maintained extractor computes stereo_complete from FindMolChiralCenters with unassigned centres included; it does not test every double-bond geometry. No extractor was invoked here. |
| bgc-2274-origin-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 1067–1196 | supports | Producer and locus evidence grades are separately copied, with explicit merge/qualification handling. ChEBI occurrence assertions are not promoted to production. |
| bgc-2274-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 968–1060 | supports | Full-key source grounding, model prediction projection and source-concept preservation have separate maintained roles. |
| bgc-2274-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole profile | supports | The current review profile requires claim-level identity, representation, evidence, provenance and completion coverage without promoting unavailable checks. |
| bgc-2274-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole skill | supports | The current one-record review procedure keeps source evidence and required verification limits explicit and does not authorize record edits or external requests here. |
| bgc-2274-locus-override | /private/tmp/npm-record-reviews-20261021/curation/mibig_locus_evidence_overrides.tsv; Header line 1; physical line 5 | supports | Complete applicable retained override: {"action": "REPLACE", "curator": "codex", "date": "2026-09-30", "expected_entry_version": "", "expected_genome_accession": "", "expected_locus_evidence_methods": "", "expected_locus_from": "", "expected_locus_to": "", "expected_standard_inchi_key": "", "expected_taxon_id": "", "locus_evidence_methods": "Enzymatic assays", "minted_identifier": "naturalproductmech:mibig-83a1fc1265", "rationale": "PMID:20536237 reports in vitro incubation of recombinant Streptomyces avermitilis SAV_76 with farnesyl diphosphate to form avermitilol; the evidence demonstrates the BGC0000683 locus without upgrading the native producer claim.", "reference": "", "source": "MIBIG", "source_id": "BGC0000683", "source_label": "avermitilol"} |
| bgc-2274-override-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 473–569 | supports | Maintained override loader and application replace the applicable locus method while keeping claim-specific producer handling separate. |
| bgc-2274-reader-DATA | /private/tmp/npm-review-work/shared-next-batch228/native-current228-avermitilol-maintained-reader-DATA-001.json; /status; /review_check_metadata; /raw_owner; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner; /counts; /denials; /unexpected_denials; /errors; /external_requests; /molecular_parses; /limitations | supports | One original maintained reader returned the complete owner exactly, with one graph, three nodes, two edges, one pathway step and four histories. One known socket capability probe was denied before action; no unexpected denial, request or molecular parse occurred. Historical scientific annotations remain unrefreshed. |
| bgc-2274-reader-execution | /private/tmp/npm-review-work/shared-next-batch228/native-current228-avermitilol-reader-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries; /external_requests | supports | Original command and process receipt: exit 0, empty stderr, zero retries and no external request. |
| bgc-2274-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-2274-maintained-reader-acceptance-001.json; /status; /DATA; /execution; /verification; /review_check_contract; /limits | supports | ROOT accepts the original complete-owner reader and exact check contract; its mechanical acceptance does not verify primary science, native sequence or construct identity. |
| bgc-2274-graph-0 | /private/tmp/npm-review-work/shared-next-batch228/native-current228-avermitilol-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/0 | supports | Complete graph, all nodes, directed edges and evidence placements: {"description": "Streptomyces avermitilis avermitilol biosynthesis graph for Tpc1-catalyzed cyclization of (2E,6E)-farnesyl diphosphate to avermitilol.", "edges": [{"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "Recombinant Streptomyces avermitilis SAV_76/Tpc1 cyclized farnesyl diphosphate to avermitilol.", "reference": "DOI:10.1021/ja103087w", "snippet": "Incubation of the recombinant protein, SAV_76, with farnesyl diphosphate"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG entry version 3 links BGC0000683 to avermitilol biosynthesis in Streptomyces avermitilis MA-4680.", "reference": "https://mibig.secondarymetabolites.org/repository/BGC0000683.3/", "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "UniProtKB:Q82RR7 is the reviewed Streptomyces avermitilis MA-4680 Tpc1/SAV_76 gene product, maps to EMBL BA000030 protein BAC67785.1, and annotates RHEA:32023 for cyclization of farnesyl diphosphate to avermitilol plus diphosphate.", "reference": "https://www.uniprot.org/uniprotkb/Q82RR7", "retrieved_on": "2026-09-30"}], "object": "tpc1", "predicate": "is cyclized by", "subject": "fpp"}, {"evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "Recombinant Streptomyces avermitilis SAV_76/Tpc1 cyclized farnesyl diphosphate to avermitilol.", "reference": "DOI:10.1021/ja103087w", "snippet": "Incubation of the recombinant protein, SAV_76, with farnesyl diphosphate"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG entry version 3 links BGC0000683 to avermitilol biosynthesis in Streptomyces avermitilis MA-4680.", "reference": "https://mibig.secondarymetabolites.org/repository/BGC0000683.3/", "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "UniProtKB:Q82RR7 is the reviewed Streptomyces avermitilis MA-4680 Tpc1/SAV_76 gene product, maps to EMBL BA000030 protein BAC67785.1, and annotates RHEA:32023 for cyclization of farnesyl diphosphate to avermitilol plus diphosphate.", "reference": "https://www.uniprot.org/uniprotkb/Q82RR7", "retrieved_on": "2026-09-30"}], "object": "avermitilol", "predicate": "forms", "subject": "tpc1"}], "graph_id": "avermitilol-tpc1-biosynthesis", "nodes": [{"grounding_status": "GROUNDED", "identifier": "CHEBI:175763", "label": "(2E,6E)-farnesyl diphosphate", "node_id": "fpp", "node_type": "PRECURSOR"}, {"grounding_status": "GROUNDED", "identifier": "UniProtKB:Q82RR7", "label": "Tpc1", "node_id": "tpc1", "node_type": "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:63702", "label": "avermitilol", "node_id": "avermitilol", "node_type": "COMPOUND"}], "scope": "BIOSYNTHESIS"} |
| bgc-2274-pathway-0 | /private/tmp/npm-review-work/shared-next-batch228/native-current228-avermitilol-maintained-reader-DATA-001.json; /resolved_view/biosynthetic_pathway/0 | supports | Complete pathway step and evidence placements: {"enzyme_id": "UniProtKB:Q82RR7", "enzyme_label": "Avermitilol synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT", "notes": "Recombinant Streptomyces avermitilis SAV_76/Tpc1 cyclized farnesyl diphosphate to avermitilol.", "reference": "DOI:10.1021/ja103087w", "snippet": "Incubation of the recombinant protein, SAV_76, with farnesyl diphosphate"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG entry version 3 links BGC0000683 to avermitilol biosynthesis in Streptomyces avermitilis MA-4680.", "reference": "https://mibig.secondarymetabolites.org/repository/BGC0000683.3/", "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes": "UniProtKB:Q82RR7 is the reviewed Streptomyces avermitilis MA-4680 Tpc1/SAV_76 gene product, maps to EMBL BA000030 protein BAC67785.1, and annotates RHEA:32023 for cyclization of farnesyl diphosphate to avermitilol plus diphosphate.", "reference": "https://www.uniprot.org/uniprotkb/Q82RR7", "retrieved_on": "2026-09-30"}], "notes": "Streptomyces avermitilis SAV_76/Tpc1 cyclizes (2E,6E)-farnesyl diphosphate to avermitilol.", "product": "CHEBI:63702", "reaction_id": "RHEA:32023", "step_number": 1, "substrate": "CHEBI:175763"} |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-228/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-228/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-228/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-228/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-228/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External identifiers, taxonomy, genome accessions and primary publications were not refreshed under the absolute no-request instruction. Historical and database assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and stored-form parsing establish only their declared mechanical scope.
- Empty joins refer only to retained exact predicates and snapshots; they do not establish biological absence. Shared loci, citations and congeners do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source records, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- The complete owner/history, actual intake, exact assigned source payloads and both complete saved molecular tables were personally read. Complementary source and companion reading is explicitly attributed in the pinned notes.
- The original batch diagnostic has two global undefined-stereo warnings, not attributed to individual records. All true comparison flags leave full_graph_identity_established:false unchanged.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T185021Z-avermitilol
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: avermitilol'
started_at: '2026-11-03T18:10:20.610495Z'
finished_at: '2026-11-03T18:50:21.979510Z'
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
summary: Avermitilol is locally consistent with its full-key ChEBI/MIBiG structure
  and retained recombinant Tpc1 reaction annotations. The applied locus override supports
  the written locus grade while native producer and historical protein-identity claims
  remain separately limited. Scientific completion is partial.
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
  - path: data/natural_products/terpenoids/avermitilol.yaml
    sha256: 0cb3158c5585c102db1439e961cbad475e3fd9a23429bbc1082e630f92ac7d89
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
  selection: Campaign path order 2274; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:63702
targets:
- target_id: CHEBI:63702
  path: data/natural_products/terpenoids/avermitilol.yaml
  label: avermitilol
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
    path: data/natural_products/terpenoids/avermitilol.yaml
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
  name: Complete offline maintained reader for avermitilol
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch228/read-selected-mechanism-guarded-001.py
    2274 87876d6c5ab3898854f3742e3c97ae5874f256a9be3a34ee3909e31da284dbe9 8b0fac707f5cd552d89b4d9b7e64bf5c1b135b0fb3adfc7819aefeeafcda4069
    2e4bc1b2f84679dd4ef1588ad68fc0c0a19ffeefc85bc91b9168ad4df0c0e601 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
    7abee563076618665c993a066381292cd48551ce0567a49954ad8017a3175d73
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CHEBI:63702
  evidence_ids:
  - bgc-2274-reader-DATA
  - bgc-2274-reader-execution
  - bgc-2274-reader-acceptance
  summary: One original offline maintained call preserved the complete owner and historical
    mechanism content; mechanical preservation is distinct from fresh scientific verification.
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:63702
  command: just validate-strict data/natural_products/terpenoids/aspterric-acid.yaml
    data/natural_products/terpenoids/astaxanthin.yaml data/natural_products/terpenoids/astellolide-a.yaml
    data/natural_products/terpenoids/avermitilol.yaml data/natural_products/terpenoids/betaestacin-i.yaml
    data/natural_products/terpenoids/betaestacin-ii.yaml data/natural_products/terpenoids/biscognienyne-b.yaml
    data/natural_products/terpenoids/botrydial.yaml data/natural_products/terpenoids/botrydienal.yaml
    data/natural_products/terpenoids/botryenalol.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-228/validate-strict-selected10-001.tsv
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
  - CHEBI:63702
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-228/validate-all-001.tsv
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
  - CHEBI:63702
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
  - CHEBI:63702
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
  - CHEBI:63702
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-228/review-queue-001.tsv
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
  - CHEBI:63702
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:63702
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:63702
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2274-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/avermitilol.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Complete current owner and all 4 ordered history entries personally read;
    native curation_status remains SEEDED.
  snapshot_sha256: 0cb3158c5585c102db1439e961cbad475e3fd9a23429bbc1082e630f92ac7d89
- evidence_id: bgc-2274-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/3/owner_pin; /records/3/owner_document
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Exact complete captured owner, including all written fields and history.
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2274-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/intakes/2274-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Actual canonical one-record intake for CHEBI:63702 with 39 current source
    inputs and explicit field ownership.
  snapshot_sha256: 8b0fac707f5cd552d89b4d9b7e64bf5c1b135b0fb3adfc7819aefeeafcda4069
- evidence_id: bgc-2274-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-intake-ready-001.json
  locator: /accepted; /intake_summary; /verification
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ROOT accepts the ten original canonical intakes and their exact current
    ownership/source maps.
  snapshot_sha256: c2c258d6da649f48e76d7d8994bfdef5dd2afa511e1762a008b8f65ef40f8501
- evidence_id: bgc-2274-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/3/owner_document/identifier; /records/3/owner_document/label;
    /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts;
    /records/3/owner_document/grounding_status; /records/3/owner_document/definition;
    /records/3/owner_document/definition_source
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete written identity and definition/provenance fields: {"chemical_structure":
    {"smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C",
    "standard_inchi": "InChI=1S/C15H26O/c1-9-5-6-11(16)15(4)8-7-10-13(12(9)15)14(10,2)3/h9-13,16H,5-8H2,1-4H3/t9-,10-,11+,12+,13-,15-/m1/s1",
    "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0000683"}, "definition":
    "A carbotricyclic compound that consists of decahydro-1H-1H-cyclopropa[a]naphthalene
    bearing four methyl substituents at position 1, 1, 3a and 7 as well as a hydroxy
    substituent at position 4 (the (1aR,3aS,4S,7R,7aS,7bR)-diastereomer).", "definition_source":
    "CHEBI:63702", "grounding_status": "EXACT", "identifier": "CHEBI:63702", "label":
    "avermitilol", "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-83a1fc1265",
    "source": "MIBIG", "source_id": "BGC0000683", "source_label": "avermitilol", "source_version":
    "3"}, {"minted_identifier": "naturalproductmech:chebi-65dfe9e019", "source": "CHEBI",
    "source_id": "CHEBI:63702", "source_label": "avermitilol", "source_version": "3-star"}]}'
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2274-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters;
    /records/3/owner_document/producer_taxon_groups
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete written producer and locus claims with their separate evidence
    grades: {"biosynthetic_gene_clusters": [{"accession": "mibig:BGC0000683", "bgc_class":
    ["TERPENE"], "entry_status": "active", "entry_version": "3", "evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "MIBiG BGC0000683 entry version 3; citation taken
    from the entry level", "reference": "PMID:20536237"}], "genome_accession": "genbank:BA000030.3",
    "link_evidence_basis": "CLUSTER_DEMONSTRATED", "locus_evidence_methods": ["Enzymatic
    assays"], "locus_from": 86073, "locus_to": 87080, "organism_label": "Streptomyces
    avermitilis MA-4680 = NBRC 14893", "organism_taxon_id": "NCBITaxon:227882"}],
    "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0000683", "evidence":
    [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0000683 entry version
    3; citation taken from the entry level", "reference": "PMID:20536237"}], "evidence_basis":
    "SOURCE_ASSERTION", "notes": "Locus evidence: Enzymatic assays. That evidence
    grades the LOCUS as CLUSTER_DEMONSTRATED; this field grades the taxon claim, which
    is a different question.", "source": "MIBIG", "source_version": "3", "taxon_id":
    "NCBITaxon:227882", "taxon_label": "Streptomyces avermitilis MA-4680 = NBRC 14893"}],
    "producer_taxon_groups": ["ACTINOBACTERIAL"]}'
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2274-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'The complete owner establishes present or absent occurrences. Written
    occurrence fields and any omission notes: {"occurrence_taxon_groups": ["ACTINOBACTERIAL"],
    "occurrences": [{"evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes":
    "LOTUS structure-organism-reference triple. LOTUS reports that the compound was
    found in the organism; it does not assert that the organism produces it.", "reference":
    "DOI:10.1021/JA103087W"}], "notes": "Wikidata organism http://www.wikidata.org/entity/Q1946562",
    "source": "LOTUS", "taxon_id": "NCBITaxon:33903", "taxon_label": "Streptomyces
    avermitilis", "taxon_source": "NCBITaxon"}]}'
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2274-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete owner establishes assay, target and mechanism-root presence without
    inferring biological absence: {}'
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2274-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_pathway; /records/3/owner_document/np_classification;
    /records/3/owner_document/bgc_class
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Literal source BGC classification and named/versioned computed classification
    remain separate: {"bgc_class": ["TERPENE"], "np_classification": {"class_results":
    ["Cycloeudesmane sesquiterpenoids"], "is_glycoside": false, "pathway_results":
    ["Terpenoids"], "superclass_results": ["Sesquiterpenoids"], "tool": "NPClassifier",
    "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS"}'
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2274-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/declared_structure; /records/3/smiles/status; /records/3/inchi/status;
    /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons;
    /records/3/atom_correspondence
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Both saved forms parsed. Their complete atom/bond/ring/stereo/motif tables
    and correspondence were personally read. Saved declared structure and comparison
    facts: {"comparisons": {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared":
    true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal":
    true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer":
    true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "declared_structure":
    {"smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C",
    "standard_inchi": "InChI=1S/C15H26O/c1-9-5-6-11(16)15(4)8-7-10-13(12(9)15)14(10,2)3/h9-13,16H,5-8H2,1-4H3/t9-,10-,11+,12+,13-,15-/m1/s1",
    "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0000683"}, "inchi_formula":
    "C15H26O", "smiles_formula": "C15H26O"}'
  snapshot_sha256: d4c6eb70f0eb830267ca6a459d5b3f2f1ed0903dbbd02a6ea6cea1104beb62f9
- evidence_id: bgc-2274-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed; /records/3/inchi/computed; /records/3/atom_correspondence
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: The complete SMILES table contains a saturated C15 carbon framework with
    six-, six- and three-membered rings and one alcohol at C5–O6H. All 18 bonds are
    single. Six tetrahedral centres are specified; there is no carbonyl, sugar residue
    or glycosidic linkage.
  snapshot_sha256: d4c6eb70f0eb830267ca6a459d5b3f2f1ed0903dbbd02a6ea6cea1104beb62f9
- evidence_id: bgc-2274-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-execution-001.json
  locator: /command; /cwd; /started_at; /finished_at; /exit_code; /source; /stdout;
    /stderr; /external_requests
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Original process receipt has exit 0 and retains exact stdout/stderr, clocks,
    command and source; no external request.
  snapshot_sha256: cec83a5bb171e1fb8a233f2b4d0f0421461c308bf28a3b13540cd0baeb3ab3cf
- evidence_id: bgc-2274-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-local-diagnostics-acceptance-001.json
  locator: /accepted; /DATA; /execution; /verification; /unspecified_stereo; /limits
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ROOT accepts the original 20 stored-form parses and current dependency
    joins. The two original undefined-stereo warnings remain global and unassigned;
    full QC/OAK and scientific verification limits remain explicit.
  snapshot_sha256: 538d4571fceb926adea82c64cc91c2cb0d058ceb5018e3d3261297b43223fcf8
- evidence_id: bgc-2274-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-native-five-gates-acceptance-001.json
  locator: /five_exits; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /selected_queue_rows
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Five local gates passed. Full QC and complete OAK authority coverage remain
    unavailable; all_native_gates_passed is false. The selected queue is a local review
    aid, not proof of the scientific assertions.
  snapshot_sha256: 46a484e5df5e5ff5b717dd9fbef5c00cc5bc1843abdf9cab2629b498187c780a
- evidence_id: bgc-2274-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/root-source-inventory-acceptance-001.json
  locator: /inventory; /verification; /reading_scope
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ROOT accepts the original retained inventory and exact current maps; scientific
    source-payload reading is separately attributed.
  snapshot_sha256: 2feaf455de349447001426cc4790a3fa85b20f1d257fef5061b48c27803f0f3d
- evidence_id: bgc-2274-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/3; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Accepted source plan retains this exact owner and its input/context roles
    within 448 placements and 78 unique paths.
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: bgc-2274-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-input-plan-acceptance-001.json
  locator: /accepted; /plan; /source_notes; /source_placements; /unique_source_paths;
    /current_record_and_all_source_pins
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ROOT accepts the actual composed plan and current input/owner joins, separately
    from scientific judgments.
  snapshot_sha256: 006b60c3550a7c223f1a10b5a127034d9429c714d72ff96363275b808fe1a2d6
- evidence_id: bgc-2274-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-scope-notes-001.json
  locator: /reading; /curation; /cautions
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Complete personal and delegated source readings, exact bounded curation
    scan, source grades and limits are recorded. No external source refresh or congener
    transfer is implied.
  snapshot_sha256: 63a4685a365402d997d4f20d1b80d7dce1b7f62d2d2264c93dae7fa581e52df5
- evidence_id: bgc-2274-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /records/3/direct_companion_paths; /records/3/direct_companion_predicates
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact direct-context paths and one-hop predicates: {"direct_companion_paths":
    [], "direct_companion_predicates": []}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [{"last_physical_line": 819, "physical_line": 819, "raw_tsv_record":
    "BGC0000683\t3\tactive\tquestionable\tunknown\tavermitilol\t1\t[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C\tInChI=1S/C15H26O/c1-9-5-6-11(16)15(4)8-7-10-13(12(9)15)14(10,2)3/h9-13,16H,5-8H2,1-4H3/t9-,10-,11+,12+,13-,15-/m1/s1\tBLGPPSRDEKNCLT-CDWXYHGHSA-N\ttrue\t\tnpatlas:NPA019411\tNCBITaxon:227882\tStreptomyces
    avermitilis MA-4680 = NBRC 14893\tterpene\tUnknown\tBA000030.3\t86073\t87080\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:20536237\tENTRY\n",
    "row": {"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis":
    "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name":
    "avermitilol", "database_ids": "npatlas:NPA019411", "entry_completeness": "unknown",
    "entry_quality": "questionable", "entry_status": "active", "entry_version": "3",
    "genome_accession": "BA000030.3", "locus_evidence_methods": "", "locus_from":
    "86073", "locus_to": "87080", "mibig_accession": "BGC0000683", "primary_reference":
    "PMID:20536237", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis":
    "ENTRY", "smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C",
    "standard_inchi": "InChI=1S/C15H26O/c1-9-5-6-11(16)15(4)8-7-10-13(12(9)15)14(10,2)3/h9-13,16H,5-8H2,1-4H3/t9-,10-,11+,12+,13-,15-/m1/s1",
    "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:227882", "taxon_label": "Streptomyces avermitilis MA-4680
    = NBRC 14893"}, "row_sha256": "20ed5837f2130d80079011b55e1b719316cc975a06a53e30e77ed798bc56b618"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 819–819; row_sha256 20ed5837f2130d80079011b55e1b719316cc975a06a53e30e77ed798bc56b618
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete physical source rows, all fields personally read and joined to
    the pinned table: [{"bgc_classes": "terpene", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis":
    "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name":
    "avermitilol", "database_ids": "npatlas:NPA019411", "entry_completeness": "unknown",
    "entry_quality": "questionable", "entry_status": "active", "entry_version": "3",
    "genome_accession": "BA000030.3", "locus_evidence_methods": "", "locus_from":
    "86073", "locus_to": "87080", "mibig_accession": "BGC0000683", "primary_reference":
    "PMID:20536237", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis":
    "ENTRY", "smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C",
    "standard_inchi": "InChI=1S/C15H26O/c1-9-5-6-11(16)15(4)8-7-10-13(12(9)15)14(10,2)3/h9-13,16H,5-8H2,1-4H3/t9-,10-,11+,12+,13-,15-/m1/s1",
    "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:227882", "taxon_label": "Streptomyces avermitilis MA-4680
    = NBRC 14893"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2274-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [{"last_physical_line": 20440, "physical_line": 20440, "raw_tsv_record":
    "CHEBI:63702\tavermitilol\tA carbotricyclic compound that consists of decahydro-1H-1H-cyclopropa[a]naphthalene
    bearing four methyl substituents at position 1, 1, 3a and 7 as well as a hydroxy
    substituent at position 4 (the (1aR,3aS,4S,7R,7aS,7bR)-diastereomer).\t3\tBLGPPSRDEKNCLT-CDWXYHGHSA-N\t[H][C@@]12[C@H](C)CC[C@H](O)[C@@]1(C)CC[C@@H]1[C@H]2C1(C)C\n",
    "row": {"chebi_id": "CHEBI:63702", "definition": "A carbotricyclic compound that
    consists of decahydro-1H-1H-cyclopropa[a]naphthalene bearing four methyl substituents
    at position 1, 1, 3a and 7 as well as a hydroxy substituent at position 4 (the
    (1aR,3aS,4S,7R,7aS,7bR)-diastereomer).", "name": "avermitilol", "smiles": "[H][C@@]12[C@H](C)CC[C@H](O)[C@@]1(C)CC[C@@H]1[C@H]2C1(C)C",
    "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stars": "3"}, "row_sha256":
    "454c8be5e44b15a9c0b11463f860c6e7ecf090ebd8a1f15520795b03670b7013"}], "predicate":
    "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-source-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line 1; physical lines 20440–20440; row_sha256 454c8be5e44b15a9c0b11463f860c6e7ecf090ebd8a1f15520795b03670b7013
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete physical source rows, all fields personally read and joined to
    the pinned table: [{"chebi_id": "CHEBI:63702", "definition": "A carbotricyclic
    compound that consists of decahydro-1H-1H-cyclopropa[a]naphthalene bearing four
    methyl substituents at position 1, 1, 3a and 7 as well as a hydroxy substituent
    at position 4 (the (1aR,3aS,4S,7R,7aS,7bR)-diastereomer).", "name": "avermitilol",
    "smiles": "[H][C@@]12[C@H](C)CC[C@H](O)[C@@]1(C)CC[C@@H]1[C@H]2C1(C)C", "standard_inchi_key":
    "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "stars": "3"}]'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2274-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [{"last_physical_line": 547, "physical_line": 547, "raw_tsv_record":
    "BLGPPSRDEKNCLT-CDWXYHGHSA-N\tStreptomyces avermitilis\tNCBITaxon:33903\thttp://www.wikidata.org/entity/Q1946562\t10.1021/JA103087W\thttp://www.wikidata.org/entity/Q27132738\n",
    "row": {"organism_name": "Streptomyces avermitilis", "organism_wikidata": "http://www.wikidata.org/entity/Q1946562",
    "reference_doi": "10.1021/JA103087W", "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27132738", "taxon_id":
    "NCBITaxon:33903"}, "row_sha256": "f2d11f6d25a7e6f29a5741bf4359fbe35128f7eaaa3dc9dc2a2ff05ef5be9f7c"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-source-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 547–547; row_sha256 f2d11f6d25a7e6f29a5741bf4359fbe35128f7eaaa3dc9dc2a2ff05ef5be9f7c
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete physical source rows, all fields personally read and joined to
    the pinned table: [{"organism_name": "Streptomyces avermitilis", "organism_wikidata":
    "http://www.wikidata.org/entity/Q1946562", "reference_doi": "10.1021/JA103087W",
    "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27132738",
    "taxon_id": "NCBITaxon:33903"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2274-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "BLGPPSRDEKNCLT-CDWXYHGHSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [{"last_physical_line": 191, "physical_line": 191, "raw_tsv_record":
    "BLGPPSRDEKNCLT-CDWXYHGHSA-N\t[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C\tTerpenoids\tSesquiterpenoids\tCycloeudesmane
    sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results":
    "Cycloeudesmane sesquiterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07",
    "pathway_results": "Terpenoids", "smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C",
    "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "superclass_results": "Sesquiterpenoids"},
    "row_sha256": "1e56361dd43c5dfd758c03341c874f9222ed6739c489f34c93f0f44316325e4c"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "BLGPPSRDEKNCLT-CDWXYHGHSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 191–191; row_sha256 1e56361dd43c5dfd758c03341c874f9222ed6739c489f34c93f0f44316325e4c
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete physical source rows, all fields personally read and joined to
    the pinned table: [{"class_results": "Cycloeudesmane sesquiterpenoids", "is_glycoside":
    "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results":
    "Terpenoids", "smiles": "[H][C@@]12CC[C@]3(C)[C@@H](O)CC[C@@H](C)[C@@]3([H])[C@]1([H])C2(C)C",
    "standard_inchi_key": "BLGPPSRDEKNCLT-CDWXYHGHSA-N", "superclass_results": "Sesquiterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2274-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "BLGPPSRDEKNCLT-CDWXYHGHSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "BLGPPSRDEKNCLT-CDWXYHGHSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "BLGPPSRDEKNCLT-CDWXYHGHSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows",
    "query": ["CHEBI:63702"]}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/source_taxa; /contexts/18/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/18/source_scope_inventory/nonorganism_matches; /contexts/18/source_scope_inventory/actual_assay_rows;
    /contexts/18/source_scope_inventory/blank_AID_sentinels; /contexts/18/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact source taxa and route lists, distinguishing forward merges/nonorganism
    matches and blank sentinels from actual assays: {"actual_assay_rows": [], "blank_AID_sentinels":
    [], "forward_taxon_merge_matches": [], "nonorganism_matches": [], "related_corpus_rows":
    [], "source_taxa": ["NCBITaxon:227882", "NCBITaxon:33903"]}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/14; /cached_taxonomy/whole_stanzas/53;
    /cached_taxonomy/unmatched_ids
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete retained cache stanzas for this source-taxon scope, with cache
    misses retained globally and no fresh taxonomy or ancestry assertion: [{"complete_stanza":
    "[Term]\nid: NCBITaxon:33903\nname: Streptomyces avermitilis\nsynonym: \"Streptomyces
    avermectinius\" EXACT []\n\n", "id": "NCBITaxon:33903", "physical_line": 14687},
    {"complete_stanza": "[Term]\nid: NCBITaxon:227882\nname: Streptomyces avermitilis
    MA-4680 = NBRC 14893\nsynonym: \"Streptomyces avermitilis MA-4680\" EXACT []\nsynonym:
    \"Streptomyces avermitilis NBRC 14893\" EXACT []\nsynonym: \"Streptomyces avermitilis
    NBRC 14893 = MA-4680\" EXACT []\n\n", "id": "NCBITaxon:227882", "physical_line":
    69123}]'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2274-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: One bounded eight-table scan used 161 exact literals over 93 data rows,
    including ignored files by direct access. The only hit is the Avermitilol locus
    override at physical line 5; applicability is owner-specific. Reserved decisions.tsv
    was not consumed. PubChem exclusions were supplementary and are outside this batch
    input map.
  snapshot_sha256: 63a4685a365402d997d4f20d1b80d7dce1b7f62d2d2264c93dae7fa581e52df5
- evidence_id: bgc-2274-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ChemicalStructure and ComputedClassification distinguish unspecified stereocentres,
    normalized keys and named/versioned model predictions; the latter are not source
    assertions or admission grounds.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2274-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–174
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: The maintained extractor computes stereo_complete from FindMolChiralCenters
    with unassigned centres included; it does not test every double-bond geometry.
    No extractor was invoked here.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2274-origin-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 1067–1196
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Producer and locus evidence grades are separately copied, with explicit
    merge/qualification handling. ChEBI occurrence assertions are not promoted to
    production.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2274-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 968–1060
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Full-key source grounding, model prediction projection and source-concept
    preservation have separate maintained roles.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2274-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole profile
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: The current review profile requires claim-level identity, representation,
    evidence, provenance and completion coverage without promoting unavailable checks.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2274-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole skill
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: The current one-record review procedure keeps source evidence and required
    verification limits explicit and does not authorize record edits or external requests
    here.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2274-locus-override
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/mibig_locus_evidence_overrides.tsv
  locator: Header line 1; physical line 5
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete applicable retained override: {"action": "REPLACE", "curator":
    "codex", "date": "2026-09-30", "expected_entry_version": "", "expected_genome_accession":
    "", "expected_locus_evidence_methods": "", "expected_locus_from": "", "expected_locus_to":
    "", "expected_standard_inchi_key": "", "expected_taxon_id": "", "locus_evidence_methods":
    "Enzymatic assays", "minted_identifier": "naturalproductmech:mibig-83a1fc1265",
    "rationale": "PMID:20536237 reports in vitro incubation of recombinant Streptomyces
    avermitilis SAV_76 with farnesyl diphosphate to form avermitilol; the evidence
    demonstrates the BGC0000683 locus without upgrading the native producer claim.",
    "reference": "", "source": "MIBIG", "source_id": "BGC0000683", "source_label":
    "avermitilol"}'
  snapshot_sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
- evidence_id: bgc-2274-override-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 473–569
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Maintained override loader and application replace the applicable locus
    method while keeping claim-specific producer handling separate.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2274-reader-DATA
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/native-current228-avermitilol-maintained-reader-DATA-001.json
  locator: /status; /review_check_metadata; /raw_owner; /resolved_view; /expected_view;
    /returned_view_equals_expected_complete_owner; /counts; /denials; /unexpected_denials;
    /errors; /external_requests; /molecular_parses; /limitations
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: One original maintained reader returned the complete owner exactly, with
    one graph, three nodes, two edges, one pathway step and four histories. One known
    socket capability probe was denied before action; no unexpected denial, request
    or molecular parse occurred. Historical scientific annotations remain unrefreshed.
  snapshot_sha256: 6d26128c1f068cb46521087bcd5f786fff89ba9591da44d03716cc37715c41b8
- evidence_id: bgc-2274-reader-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/native-current228-avermitilol-reader-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Original command and process receipt: exit 0, empty stderr, zero retries
    and no external request.'
  snapshot_sha256: dfeecc770228e143fc42923b3860ac9a8f5591d603d0eaf87028f4691859c138
- evidence_id: bgc-2274-reader-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-2274-maintained-reader-acceptance-001.json
  locator: /status; /DATA; /execution; /verification; /review_check_contract; /limits
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ROOT accepts the original complete-owner reader and exact check contract;
    its mechanical acceptance does not verify primary science, native sequence or
    construct identity.
  snapshot_sha256: ddd3bc961f781b15f033edf55705954214acda4952c0d38b2d45c4701818f1da
- evidence_id: bgc-2274-graph-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/native-current228-avermitilol-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/0
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete graph, all nodes, directed edges and evidence placements: {"description":
    "Streptomyces avermitilis avermitilol biosynthesis graph for Tpc1-catalyzed cyclization
    of (2E,6E)-farnesyl diphosphate to avermitilol.", "edges": [{"evidence": [{"evidence_type":
    "PRIMARY_EXPERIMENT", "notes": "Recombinant Streptomyces avermitilis SAV_76/Tpc1
    cyclized farnesyl diphosphate to avermitilol.", "reference": "DOI:10.1021/ja103087w",
    "snippet": "Incubation of the recombinant protein, SAV_76, with farnesyl diphosphate"},
    {"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG entry version 3 links
    BGC0000683 to avermitilol biosynthesis in Streptomyces avermitilis MA-4680.",
    "reference": "https://mibig.secondarymetabolites.org/repository/BGC0000683.3/",
    "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes":
    "UniProtKB:Q82RR7 is the reviewed Streptomyces avermitilis MA-4680 Tpc1/SAV_76
    gene product, maps to EMBL BA000030 protein BAC67785.1, and annotates RHEA:32023
    for cyclization of farnesyl diphosphate to avermitilol plus diphosphate.", "reference":
    "https://www.uniprot.org/uniprotkb/Q82RR7", "retrieved_on": "2026-09-30"}], "object":
    "tpc1", "predicate": "is cyclized by", "subject": "fpp"}, {"evidence": [{"evidence_type":
    "PRIMARY_EXPERIMENT", "notes": "Recombinant Streptomyces avermitilis SAV_76/Tpc1
    cyclized farnesyl diphosphate to avermitilol.", "reference": "DOI:10.1021/ja103087w",
    "snippet": "Incubation of the recombinant protein, SAV_76, with farnesyl diphosphate"},
    {"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG entry version 3 links
    BGC0000683 to avermitilol biosynthesis in Streptomyces avermitilis MA-4680.",
    "reference": "https://mibig.secondarymetabolites.org/repository/BGC0000683.3/",
    "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes":
    "UniProtKB:Q82RR7 is the reviewed Streptomyces avermitilis MA-4680 Tpc1/SAV_76
    gene product, maps to EMBL BA000030 protein BAC67785.1, and annotates RHEA:32023
    for cyclization of farnesyl diphosphate to avermitilol plus diphosphate.", "reference":
    "https://www.uniprot.org/uniprotkb/Q82RR7", "retrieved_on": "2026-09-30"}], "object":
    "avermitilol", "predicate": "forms", "subject": "tpc1"}], "graph_id": "avermitilol-tpc1-biosynthesis",
    "nodes": [{"grounding_status": "GROUNDED", "identifier": "CHEBI:175763", "label":
    "(2E,6E)-farnesyl diphosphate", "node_id": "fpp", "node_type": "PRECURSOR"}, {"grounding_status":
    "GROUNDED", "identifier": "UniProtKB:Q82RR7", "label": "Tpc1", "node_id": "tpc1",
    "node_type": "ENZYME"}, {"grounding_status": "GROUNDED", "identifier": "CHEBI:63702",
    "label": "avermitilol", "node_id": "avermitilol", "node_type": "COMPOUND"}], "scope":
    "BIOSYNTHESIS"}'
  snapshot_sha256: 6d26128c1f068cb46521087bcd5f786fff89ba9591da44d03716cc37715c41b8
- evidence_id: bgc-2274-pathway-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/native-current228-avermitilol-maintained-reader-DATA-001.json
  locator: /resolved_view/biosynthetic_pathway/0
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete pathway step and evidence placements: {"enzyme_id": "UniProtKB:Q82RR7",
    "enzyme_label": "Avermitilol synthase", "evidence": [{"evidence_type": "PRIMARY_EXPERIMENT",
    "notes": "Recombinant Streptomyces avermitilis SAV_76/Tpc1 cyclized farnesyl diphosphate
    to avermitilol.", "reference": "DOI:10.1021/ja103087w", "snippet": "Incubation
    of the recombinant protein, SAV_76, with farnesyl diphosphate"}, {"evidence_type":
    "DATABASE_ASSERTION", "notes": "MIBiG entry version 3 links BGC0000683 to avermitilol
    biosynthesis in Streptomyces avermitilis MA-4680.", "reference": "https://mibig.secondarymetabolites.org/repository/BGC0000683.3/",
    "retrieved_on": "2026-09-30"}, {"evidence_type": "DATABASE_ASSERTION", "notes":
    "UniProtKB:Q82RR7 is the reviewed Streptomyces avermitilis MA-4680 Tpc1/SAV_76
    gene product, maps to EMBL BA000030 protein BAC67785.1, and annotates RHEA:32023
    for cyclization of farnesyl diphosphate to avermitilol plus diphosphate.", "reference":
    "https://www.uniprot.org/uniprotkb/Q82RR7", "retrieved_on": "2026-09-30"}], "notes":
    "Streptomyces avermitilis SAV_76/Tpc1 cyclizes (2E,6E)-farnesyl diphosphate to
    avermitilol.", "product": "CHEBI:63702", "reaction_id": "RHEA:32023", "step_number":
    1, "substrate": "CHEBI:175763"}'
  snapshot_sha256: 6d26128c1f068cb46521087bcd5f786fff89ba9591da44d03716cc37715c41b8
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:12:47.775053Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: c21e163f3196cf186958794725f1b00a467ef5cca041142eb77868d0f57002a8
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:13:12.316523Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 87b8d13781a6e8b29a6548c0231420c70cfb7201c9942069049f0adfaa3a91dc
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:13:32.394271Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:14:07.640893Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:14:19.806834Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 8a9b4b2d4725b4513fcae189afd5e5e6f81b1ec228cdd2b2b100ff2dd2472a63
assessments:
- assessment_id: bgc-2274-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: CHEBI:63702 and MIBiG BGC0000683 version 3, compound index 1, share complete
    key BLGPPSRDEKNCLT-CDWXYHGHSA-N. The ChEBI definition describes the carbotricyclic
    tetramethyl alcohol and a specified diastereomer. Both saved forms reproduce neutral
    C15H26O and the saturated tricyclic alcohol topology. This establishes retained
    definition/structure compatibility without independently verifying the natural
    isolated product.
  target_ids:
  - CHEBI:63702
  evidence_ids:
  - bgc-2274-grounding-owner
  - bgc-2274-source-mibig_compounds
  - bgc-2274-source-chebi_structures
  - bgc-2274-query-chebi_structures
  - bgc-2274-chemistry
  - bgc-2274-topology
  - bgc-2274-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: BLGPPSRDEKNCLT-CDWXYHGHSA-N; exact complete ChEBI/MIBiG and saved-form
      key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2274-grounding-owner
    - bgc-2274-source-mibig_compounds
    - bgc-2274-source-chebi_structures
    - bgc-2274-query-chebi_structures
    - bgc-2274-chemistry
    - bgc-2274-topology
    - bgc-2274-direct-contexts
  - name: grounding_scope
    value: EXACT CHEBI:63702; local carbotricyclic alcohol definition/structure consistency.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2274-grounding-owner
    - bgc-2274-source-mibig_compounds
    - bgc-2274-source-chebi_structures
    - bgc-2274-query-chebi_structures
    - bgc-2274-chemistry
    - bgc-2274-topology
    - bgc-2274-direct-contexts
- assessment_id: bgc-2274-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both forms contain 16 atoms, 18 bonds and one fragment, with six-, six-
    and three-membered rings. Six specified SMILES centres C0 R, C3 S, C5 S, C9 R,
    C11 S and C12 R correspond to InChI atoms 9, 14, 10, 8, 11 and 12. Ten comparison
    flags and the complete stored correspondence agree. No unspecified potential stereochemistry
    is reported within the diagnostic's supported scope, but independent full-graph
    and natural identity remain unestablished.
  target_ids:
  - CHEBI:63702
  evidence_ids:
  - bgc-2274-grounding-owner
  - bgc-2274-chemistry
  - bgc-2274-topology
  - bgc-2274-diagnostic-acceptance
  - bgc-2274-structure-schema
  - bgc-2274-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Six specified tetrahedral centres; no unspecified potential stereo in the
      saved supported scope.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2274-grounding-owner
    - bgc-2274-chemistry
    - bgc-2274-topology
    - bgc-2274-diagnostic-acceptance
    - bgc-2274-structure-schema
    - bgc-2274-stereo-method
  - name: representation_correspondence
    value: Ten true comparisons and complete correspondence; no independent natural
      or full-graph identity.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2274-grounding-owner
    - bgc-2274-chemistry
    - bgc-2274-topology
    - bgc-2274-diagnostic-acceptance
    - bgc-2274-structure-schema
    - bgc-2274-stereo-method
- assessment_id: bgc-2274-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: The raw BGC0000683 version 3 row is active, questionable and of unknown
    completeness, with no locus method. The maintained locus override at physical
    line 5 replaces that method with Enzymatic assays, explaining the written CLUSTER_DEMONSTRATED
    grade. Its rationale is recombinant SAV_76 incubation with farnesyl diphosphate;
    it expressly does not upgrade native production. Streptomyces avermitilis MA-4680
    = NBRC 14893, taxon 227882, therefore remains SOURCE_ASSERTION, separately from
    the species-level LOTUS occurrence at 33903. The written interval is genbank:BA000030.3,
    86073–87080.
  target_ids:
  - CHEBI:63702
  evidence_ids:
  - bgc-2274-origin-owner
  - bgc-2274-source-mibig_compounds
  - bgc-2274-cached-taxonomy
  - bgc-2274-source-routes
  - bgc-2274-origin-seeder
  - bgc-2274-locus-override
  - bgc-2274-override-seeder
  dimensions:
  - name: taxon_scope
    value: Producer strain 227882 versus occurrence species 33903; cached labels remain
      attributed.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2274-origin-owner
    - bgc-2274-source-mibig_compounds
    - bgc-2274-cached-taxonomy
    - bgc-2274-source-routes
    - bgc-2274-origin-seeder
    - bgc-2274-locus-override
    - bgc-2274-override-seeder
  - name: producer_evidence
    value: SOURCE_ASSERTION for native strain production; recombinant assay does not
      upgrade it.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2274-origin-owner
    - bgc-2274-source-mibig_compounds
    - bgc-2274-cached-taxonomy
    - bgc-2274-source-routes
    - bgc-2274-origin-seeder
    - bgc-2274-locus-override
    - bgc-2274-override-seeder
  - name: locus_evidence
    value: BGC0000683 version 3; physical override 5 applies Enzymatic assays and
      CLUSTER_DEMONSTRATED.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2274-origin-owner
    - bgc-2274-source-mibig_compounds
    - bgc-2274-cached-taxonomy
    - bgc-2274-source-routes
    - bgc-2274-origin-seeder
    - bgc-2274-locus-override
    - bgc-2274-override-seeder
- assessment_id: bgc-2274-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: The MIBiG producer/locus assertions use ENTRY PMID:20536237; the applied
    override explains its recombinant-assay scope. The historical graph and pathway
    retain a DOI:10.1021/ja103087w snippet, MIBiG version 3 database assertions and
    a 2026-09-30 UniProt annotation. Repetition of these same references on two edges
    and one step does not create independent experiments. The uppercase LOTUS DOI
    is another occurrence assertion, not a separate native-production demonstration.
    These complete retained annotations were read without fresh article, database
    or sequence access.
  target_ids:
  - CHEBI:63702
  evidence_ids:
  - bgc-2274-origin-owner
  - bgc-2274-occurrence-owner
  - bgc-2274-source-mibig_compounds
  - bgc-2274-source-lotus_occurrences
  - bgc-2274-source-chebi_structures
  - bgc-2274-query-chebi_origins
  - bgc-2274-source-notes
  - bgc-2274-direct-contexts
  - bgc-2274-locus-override
  - bgc-2274-graph-0
  - bgc-2274-pathway-0
  - bgc-2274-reader-DATA
  dimensions:
  - name: citation_scope
    value: ENTRY PMID:20536237 plus historical DOI/MIBiG/UniProt annotations; repeated
      placements are not independent experiments.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2274-origin-owner
    - bgc-2274-occurrence-owner
    - bgc-2274-source-mibig_compounds
    - bgc-2274-source-lotus_occurrences
    - bgc-2274-source-chebi_structures
    - bgc-2274-query-chebi_origins
    - bgc-2274-source-notes
    - bgc-2274-direct-contexts
    - bgc-2274-locus-override
    - bgc-2274-graph-0
    - bgc-2274-pathway-0
    - bgc-2274-reader-DATA
- assessment_id: bgc-2274-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: One written LOTUS occurrence reports the species Streptomyces avermitilis,
    taxon 33903; it does not establish production by strain 227882. No bioactivities
    or molecular targets are written, and the exact retained PubChem, BindingDB and
    AntibioticMech joins are empty. The biosynthetic enzyme is not a pharmacological
    target. The accepted reader preserves the one graph and one pathway step but does
    not add an assay or producer observation.
  target_ids:
  - CHEBI:63702
  evidence_ids:
  - bgc-2274-occurrence-owner
  - bgc-2274-assay-owner
  - bgc-2274-source-routes
  - bgc-2274-cached-taxonomy
  - bgc-2274-query-lotus_occurrences
  - bgc-2274-query-chebi_origins
  - bgc-2274-query-cyanometdb_occurrences
  - bgc-2274-query-pubchem_bioassay
  - bgc-2274-query-bindingdb_targets
  - bgc-2274-query-antibioticmech_inchikeys
  - bgc-2274-source-lotus_occurrences
  - bgc-2274-reader-DATA
  dimensions:
  - name: occurrence_scope
    value: One species-level LOTUS occurrence, distinct from native-strain production.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2274-occurrence-owner
    - bgc-2274-assay-owner
    - bgc-2274-source-routes
    - bgc-2274-cached-taxonomy
    - bgc-2274-query-lotus_occurrences
    - bgc-2274-query-chebi_origins
    - bgc-2274-query-cyanometdb_occurrences
    - bgc-2274-query-pubchem_bioassay
    - bgc-2274-query-bindingdb_targets
    - bgc-2274-query-antibioticmech_inchikeys
    - bgc-2274-source-lotus_occurrences
    - bgc-2274-reader-DATA
  - name: assay_target_scope
    value: No written assays/targets and empty exact routes; biosynthetic Tpc1 is
      not a pharmacological target.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2274-occurrence-owner
    - bgc-2274-assay-owner
    - bgc-2274-source-routes
    - bgc-2274-cached-taxonomy
    - bgc-2274-query-lotus_occurrences
    - bgc-2274-query-chebi_origins
    - bgc-2274-query-cyanometdb_occurrences
    - bgc-2274-query-pubchem_bioassay
    - bgc-2274-query-bindingdb_targets
    - bgc-2274-query-antibioticmech_inchikeys
    - bgc-2274-source-lotus_occurrences
    - bgc-2274-reader-DATA
- assessment_id: bgc-2274-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The source TERPENE class and NPClassifier Terpenoids / Sesquiterpenoids
    / Cycloeudesmane sesquiterpenoids are distinct assertions. The named model's is_glycoside:false
    is compatible with the complete saturated tricyclic C15 alcohol and absence of
    a sugar residue or glycosidic linkage. That structural compatibility is separate
    from the historically attributed recombinant reaction and does not establish a
    complete natural pathway.
  target_ids:
  - CHEBI:63702
  evidence_ids:
  - bgc-2274-classification-owner
  - bgc-2274-source-mibig_compounds
  - bgc-2274-source-npclassifier
  - bgc-2274-chemistry
  - bgc-2274-topology
  - bgc-2274-structure-schema
  - bgc-2274-classification-seeder
  - bgc-2274-graph-0
  - bgc-2274-pathway-0
  dimensions:
  - name: classification_applicability
    value: Named Cycloeudesmane model; saturated tricyclic alcohol with no sugar linkage;
      reaction scope assessed separately.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2274-classification-owner
    - bgc-2274-source-mibig_compounds
    - bgc-2274-source-npclassifier
    - bgc-2274-chemistry
    - bgc-2274-topology
    - bgc-2274-structure-schema
    - bgc-2274-classification-seeder
    - bgc-2274-graph-0
    - bgc-2274-pathway-0
- assessment_id: bgc-2274-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: All required scientific dimensions were assessed against the current owner,
    actual intake, retained source payloads and complete paired molecular tables.
    Five local gates passed, while full QC and complete OAK authority coverage remain
    unavailable. The accepted maintained reader preserved the complete mechanism owner;
    its success does not refresh primary, sequence or construct evidence. External
    facts remain unverified under the no-request instruction, so completion is partial
    and native curation status is unchanged.
  target_ids:
  - CHEBI:63702
  evidence_ids:
  - bgc-2274-owner
  - bgc-2274-intake
  - bgc-2274-intake-acceptance
  - bgc-2274-inventory-acceptance
  - bgc-2274-plan
  - bgc-2274-plan-acceptance
  - bgc-2274-source-notes
  - bgc-2274-curation-scope
  - bgc-2274-diagnostic-execution
  - bgc-2274-diagnostic-acceptance
  - bgc-2274-native-acceptance
  - bgc-2274-review-profile
  - bgc-2274-review-skill
  - bgc-2274-reader-DATA
  - bgc-2274-reader-execution
  - bgc-2274-reader-acceptance
  dimensions:
  - name: review_completion
    value: Partial scientific review; actual intake and stored-form checks accepted,
      full QC/OAK and fresh external verification unavailable. Reader mechanical acceptance
      is separate from scientific verification.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2274-owner
    - bgc-2274-intake
    - bgc-2274-intake-acceptance
    - bgc-2274-inventory-acceptance
    - bgc-2274-plan
    - bgc-2274-plan-acceptance
    - bgc-2274-source-notes
    - bgc-2274-curation-scope
    - bgc-2274-diagnostic-execution
    - bgc-2274-diagnostic-acceptance
    - bgc-2274-native-acceptance
    - bgc-2274-review-profile
    - bgc-2274-review-skill
    - bgc-2274-reader-DATA
    - bgc-2274-reader-execution
    - bgc-2274-reader-acceptance
- assessment_id: bgc-2274-mechanism
  area: graph
  topic: Mechanism
  outcome: supported
  summary: The accepted maintained reader returned the complete owner with one BIOSYNTHESIS
    graph, three nodes, two directed edges and one pathway step. The graph represents
    (2E,6E)-farnesyl diphosphate being cyclized by Tpc1 and Tpc1 forming avermitilol;
    the step retains CHEBI:175763 → CHEBI:63702 and RHEA:32023. Each edge and the
    step carries the same three reference placements. The primary-experiment snippet
    concerns recombinant SAV_76, while MIBiG and UniProt entries are historical database
    assertions. Direction and owner/product scope are coherent locally; neither topology
    validation nor repeated references demonstrate native production or a complete
    physiological pathway.
  target_ids:
  - CHEBI:63702
  evidence_ids:
  - bgc-2274-reader-DATA
  - bgc-2274-reader-execution
  - bgc-2274-reader-acceptance
  - bgc-2274-graph-0
  - bgc-2274-pathway-0
  - bgc-2274-origin-owner
  - bgc-2274-locus-override
  - bgc-2274-source-mibig_compounds
  dimensions: []
- assessment_id: bgc-2274-protein
  area: grounding
  topic: Protein
  outcome: unknown
  summary: The enzyme node and pathway retain UniProtKB:Q82RR7 for Streptomyces avermitilis
    MA-4680 Tpc1/SAV_76, with the historical note linking EMBL BA000030 protein BAC67785.1
    and RHEA:32023. These are organism-specific native-reference annotations. The
    recombinant-assay snippet does not supply a complete construct, tag, residue boundary
    or sequence comparison, and no fresh accession or sequence was inspected. Preserve
    that unresolved construct-to-native identity boundary rather than treating the
    current local identifier as newly verified.
  target_ids:
  - CHEBI:63702
  evidence_ids:
  - bgc-2274-reader-DATA
  - bgc-2274-reader-execution
  - bgc-2274-reader-acceptance
  - bgc-2274-graph-0
  - bgc-2274-pathway-0
  - bgc-2274-origin-owner
  - bgc-2274-locus-override
  - bgc-2274-source-mibig_compounds
  dimensions: []
findings: []
actions: []
limitations:
- External identifiers, taxonomy, genome accessions and primary publications were
  not refreshed under the absolute no-request instruction. Historical and database
  assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and stored-form
  parsing establish only their declared mechanical scope.
- Empty joins refer only to retained exact predicates and snapshots; they do not establish
  biological absence. Shared loci, citations and congeners do not transfer compound-specific
  claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source
  records, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- The complete owner/history, actual intake, exact assigned source payloads and both
  complete saved molecular tables were personally read. Complementary source and companion
  reading is explicitly attributed in the pinned notes.
- The original batch diagnostic has two global undefined-stereo warnings, not attributed
  to individual records. All true comparison flags leave full_graph_identity_established:false
  unchanged.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-228
```
