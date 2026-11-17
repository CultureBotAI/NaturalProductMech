# Local evidence review: cyslabdan A

- Review: 20261103T222704Z-cyslabdan-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T21:43:37.806034Z
- Finished UTC: 2026-11-03T22:27:04.911273Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Cyslabdan A preserves its exact retained source key, distinct producer/locus/occurrence grades and a partial terminal Mca pathway. Stored-form canonical differences are explained by a bounded amide/imidic mobile-H witness without replacing the original failed graph mapping. The maintained reader preserves the complete historical mechanism; scientific completion remains partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2309; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-f3cb15d2b6 | data/natural_products/terpenoids/cyslabdan-a.yaml | generated | cyslabdan A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for cyslabdan-a | passed | True | naturalproductmech:mibig-f3cb15d2b6 | The original offline maintained reader returned the complete expected owner for order 2309: 1 graphs, 3 nodes, 2 edges, 1 pathway entries and 4 history events. Complete owner equality and original terminal exit 0 are ROOT-accepted; no unexpected denial or error occurred. This check establishes local preservation, not independent biological or primary-source verification. |
| strict_ten | passed | True | naturalproductmech:mibig-f3cb15d2b6 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-f3cb15d2b6 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-f3cb15d2b6 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-f3cb15d2b6 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-f3cb15d2b6 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-f3cb15d2b6 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-f3cb15d2b6 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-f3cb15d2b6 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-f3cb15d2b6.

The minted owner naturalproductmech:mibig-f3cb15d2b6 preserves complete key PSUMRJNLBIVEFF-RIVHMUOTSA-N from BGC0001910 version 4 compound index 1. Its exact retained ChEBI structure join is empty, and PubChem:24778014 is not freshly verified. Cyslabdan B and C share the locus but retain distinct complete keys; their structures, occurrences and activity claims do not transfer to this owner.

### Representation

representation: supported. Targets: naturalproductmech:mibig-f3cb15d2b6.

Both saved forms are neutral C25H41NO5S with 32 heavy atoms and 33 bonds, two six-carbon rings, a terminal alkene, an E side-chain alkene, two scaffold hydroxyls and a sulfur-linked N-acetylcysteine substituent. Six tetrahedral centres are specified. The stored SMILES amide N21–C22(=O23) corresponds locally to decoded imidic N25=C16–O26H: nitrogen loses one hydrogen, oxygen gains one, C–N becomes double and C=O becomes single. The decoded form adds an unspecified imidic C=N stereo possibility. Formula, charge, standard InChI and full key agree, but both canonical-SMILES equality flags are false, the original atom map is empty, complete_atom_count_match is false and full_graph_identity_established is false. A separately documented manual saved-table witness aligns all other adjacency/stereo properties without replacing those original results or proving natural fixed-graph identity. The retained true flag follows the documented tetrahedral-centre scope, not universal geometric completeness.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-f3cb15d2b6.

Streptomyces cyslabdanicus NCBITaxon:1470456 remains SOURCE_ASSERTION. BGC0001910 version 4 is active, questionable and of unknown completeness, with source locus methods unstated and CLUSTER_UNSTATED retained. The later curated terminal mechanism does not retroactively upgrade that source-derived locus grade. Streptomyces genus-level and S. thermocarboxydus occurrences remain distinct from this producer assertion.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-f3cb15d2b6.

The source COMPOUND_EVIDENCE reference DOI:10.1007/s10295-015-1694-6 differs from the occurrence references DOI:10.1038/JA.2008.102, DOI:10.1007/S00253-019-10240-3 and DOI:10.1038/JA.2016.103. The Mca graph separately retains historical primary deletion/heterologous evidence and MITE, UniProt, GenPept and MIBiG database mapping. Those roles are not pooled as independent exact-enzyme assays, and no source or identifier was freshly retrieved.

### Occurrence and activity

evidence: supported. Targets: naturalproductmech:mibig-f3cb15d2b6.

Three exact LOTUS rows preserve Streptomyces NCBITaxon:1883, S. thermocarboxydus NCBITaxon:59299 and S. cyslabdanicus NCBITaxon:1470456 occurrence assertions with their individual references. There are no written bioactivities or molecular targets and the exact saved assay/target joins are empty. The graph concerns biosynthetic maturation; it does not establish a therapeutic target or compound efficacy. Neither congeners nor a shared locus supply a missing assay.

### Classification

consistency: supported. Targets: naturalproductmech:mibig-f3cb15d2b6.

The retained NPClassifier prediction is Terpenoids / Diterpenoids / Labdane diterpenoids with glycoside:false, separate from MIBiG TERPENE and compound Diterpenoid/Diterpene labels. The complete saved topology supports a C20 scaffold plus a five-carbon nitrogen/sulfur-bearing substituent, so total C25 alone is not a contradiction of the broad diterpenoid class. No final-product sugar unit is represented; a glycosylated upstream mycothiol conjugate in the partial mechanism does not make the final owner a glycoside. The class and flag remain versioned predictions.

### Mechanism

graph: supported. Targets: naturalproductmech:mibig-f3cb15d2b6.

The accepted maintained reader preserves one graph with three nodes and two edges, one pathway entry and four history events, with no components or molecular targets. The mycothiol S-conjugate precursor remains UNGROUNDED, the Mca enzyme is grounded separately and the product is this exact owner. Historical deletion in the S. avermitilis SUKA22 heterologous setting carrying the S. cyslabdanicus cld cluster supports a downstream amidase requirement after nonenzymatic mycothiol addition; it does not by itself demonstrate purified exact-reference turnover. The MITE-annotated hydrolysis remains database-scoped. This single terminal step is explicitly partial: upstream CldA–D and the nonenzymatic addition are not a completed curated pathway.

### Proteins and constructs

grounding: supported. Targets: naturalproductmech:mibig-f3cb15d2b6.

Mca UniProt:A0A0H5B8U5 and GenPept:BAR97454.1 are retained as the 379-residue reference mapped to the complement of LC064028.1:10784..11923, with MITE:0000107 and BGC0001910 context. These accession/coordinate and historical functional mappings do not constitute a fresh translation, alignment, construct-junction, processing-boundary or purified-enzyme proof. The ungrounded precursor is not silently assigned a chemical identifier, and the heterologous deletion phenotype is not promoted to an organism-independent protein-family claim.

### Scientific completion

completeness: unknown. Targets: naturalproductmech:mibig-f3cb15d2b6.

The complete retained owner, actual canonical intake, saved source payloads/cache scope, both saved molecular forms and accepted maintained-reader result have been assessed within their local contracts. Full QC, complete OAK authority coverage, fresh primary-source/identifier verification and unresolved natural stereochemical or construct-specific claims remain unavailable. No source/native-status/history edit or new target execution is made; completion remains partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2309-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/cyslabdan-a.yaml; Whole current owner plaintext, including complete curation_history | supports | Complete current owner/history personally read with exact prior reading attribution; no YAML parse or native-status edit. The complete owner is preserved in the accepted capture and maintained result. |
| support-2309-capture | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/8 | supports | Complete actual captured owner and component scope; this owner has no declared component routes. |
| support-2309-intake | /private/tmp/npm-review-work/shared-next-batch231/intakes/2309-inspect-001.json; /status; /repository; /source; /targets | supports | Complete accepted canonical intake, including exact source ownership and maintained implementation dependencies. This is inspection scope, not a scientific verdict. |
| support-2309-grounding-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"chemical_structure":{"smiles":"C/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C","standard_inchi":"InChI=1S/C25H41NO5S/c1-7-16(2)9-10-19-24(6)12-8-11-23(4,5)20(24)13-21(28)25(19,31)15-32-14-18(22(29)30)26-17(3)27/h7,9,18-21,28,31H,1,8,10-15H2,2-6H3,(H,26,27)(H,29,30)/b16-9+/t18-,19+,20-,21-,24+,25-/m0/s1","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001910"},"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-f3cb15d2b6","label":"cyslabdan A","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-f3cb15d2b6","source":"MIBIG","source_id":"BGC0001910","source_label":"cyslabdan A","source_version":"4"}],"xrefs":["pubchem:24778014"]} |
| support-2309-origin-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0001910","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"4","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001910 entry version 4; citation taken from the compound evidence level","reference":"DOI:10.1007/s10295-015-1694-6"}],"genome_accession":"genbank:LC064028.1","link_evidence_basis":"CLUSTER_UNSTATED","organism_label":"Streptomyces cyslabdanicus","organism_taxon_id":"NCBITaxon:1470456"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0001910","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001910 entry version 4; citation taken from the compound evidence level","reference":"DOI:10.1007/s10295-015-1694-6"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"4","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces cyslabdanicus"}],"producer_taxon_groups":["ACTINOBACTERIAL"]} |
| support-2309-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"occurrence_taxon_groups":["ACTINOBACTERIAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1038/JA.2008.102"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1144013","source":"LOTUS","taxon_id":"NCBITaxon:1883","taxon_label":"Streptomyces","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1007/S00253-019-10240-3"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q16992819","source":"LOTUS","taxon_id":"NCBITaxon:59299","taxon_label":"Streptomyces thermocarboxydus","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1038/JA.2016.103"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q26290150 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.","source":"LOTUS","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces cyslabdanicus","taxon_source":"NCBITaxon"}]} |
| support-2309-assay-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {} |
| support-2309-classification-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","compound_classes":["Diterpenoid"],"np_classification":{"class_results":["Labdane diterpenoids"],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Diterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"} |
| support-2309-chemistry | /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/smiles/status; /records/8/inchi/status; /records/8/smiles/computed; /records/8/inchi/computed; /records/8/comparisons; /records/8/atom_correspondence | supports | Both stored forms parsed. Exact original comparison and correspondence values, preserved without a new parse: {"atom_correspondence":{"complete_atom_count_match":false,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim.","smiles_to_inchi_atom_indices":[]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":false,"canonical_nonisomeric_smiles_equal":false,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"inchi_stereo":{"Atom_Tetrahedral:Specified":6,"Bond_Double:Specified":1,"Bond_Double:Unspecified":1},"smiles_stereo":{"Atom_Tetrahedral:Specified":6,"Bond_Double:Specified":1}} |
| support-2309-topology | /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/smiles/status; /records/8/inchi/status; /records/8/smiles/computed; /records/8/inchi/computed; /records/8/comparisons; /records/8/atom_correspondence | supports | Both saved forms are neutral C25H41NO5S with 32 heavy atoms and 33 bonds, two six-carbon rings, a terminal alkene, an E side-chain alkene, two scaffold hydroxyls and a sulfur-linked N-acetylcysteine substituent. Six tetrahedral centres are specified. The stored SMILES amide N21–C22(=O23) corresponds locally to decoded imidic N25=C16–O26H: nitrogen loses one hydrogen, oxygen gains one, C–N becomes double and C=O becomes single. The decoded form adds an unspecified imidic C=N stereo possibility. Formula, charge, standard InChI and full key agree, but both canonical-SMILES equality flags are false, the original atom map is empty, complete_atom_count_match is false and full_graph_identity_established is false. |
| support-2309-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-execution-001.json; Whole original execution receipt | supports | Native operated one original stored-form diagnostic, exit 0, with preserved stdout/stderr and closed environment. The inherited DATA observer literal is not the operator attribution. |
| support-2309-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-chemistry-acceptance-001.json; Whole ROOT chemistry acceptance | supports | ROOT accepts the original 20 stored parses and retains 96 true/four false flags, two empty maps and four global unassigned warnings; it establishes no natural identity or fixed-graph equivalence. |
| support-2309-native-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-native-gates-acceptance-001.json; Whole ROOT gate acceptance and selected queue rows | supports | Five original local gates passed; all_native_gates_passed is false because full QC and complete OAK remain unavailable. Selected queues are follow-up context, not automatic scientific findings. |
| support-2309-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-intake-acceptance-001.json; Whole ROOT intake acceptance | supports | ROOT accepts ten actual one-record intakes, 411 source placements / 68 paths and exact ownership; no scientific verdict follows from intake success. |
| support-2309-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-source-inventory-acceptance-001.json; Whole ROOT source-inventory acceptance | supports | ROOT accepts the one original local inventory and its current input/capture/source joins; complete scientific reading is separately attributed in the notes. |
| support-2309-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-input-plan-acceptance-001.json; Whole ROOT input-plan acceptance | supports | ROOT accepts the exact current plan and preserved source contexts; no scientific verdict or future reader success is inferred. |
| support-2309-source-notes | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete disjoint source/raw-history reading attribution and bounded compound-specific cautions; no pre-intake verdict was asserted. |
| support-2309-curation-scope | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json; /curation | supports | Eight current pinned implemented curation tables were directly opened ignoring ignore rules; 101 exact case-sensitive cohort literals against 93 data rows yielded zero matches within that scope. Reserved decisions.tsv was not consumed. |
| support-2309-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure preserves source representation and standardized-key limitations. stereo_complete describes undefined centres; ComputedClassification is a named/versioned prediction, never a source assertion or admission criterion. |
| support-2309-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | Maintained stereo_complete derives from FindMolChiralCenters and the absence of question-mark centre tags; it is not a blanket all-bond-geometry proof. |
| support-2309-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 974–1065 | supports | Maintained seeding preserves the source structure and named/versioned classifier output while separately retaining BGC and source compound classes. |
| support-2309-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | One-record scientific review requires claim-level evidence and twelve dimensions with truthful partial-completion/unavailable-check limits. |
| support-2309-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill | supports | The review does not edit records; source access is bounded by the overriding no-request instruction. |
| support-2309-plan | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-target-input-plan-001.json; /records/8 | supports | Complete actual owner-specific input map and direct/additional roles. Historical planning language does not claim a reader result; actual reader evidence is linked separately. |
| support-2309-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[{"last_physical_line":2233,"physical_line":2233,"raw_tsv_record":"BGC0001910\t4\tactive\tquestionable\tunknown\tcyslabdan A\t1\tC/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C\tInChI=1S/C25H41NO5S/c1-7-16(2)9-10-19-24(6)12-8-11-23(4,5)20(24)13-21(28)25(19,31)15-32-14-18(22(29)30)26-17(3)27/h7,9,18-21,28,31H,1,8,10-15H2,2-6H3,(H,26,27)(H,29,30)/b16-9+/t18-,19+,20-,21-,24+,25-/m0/s1\tPSUMRJNLBIVEFF-RIVHMUOTSA-N\ttrue\tDiterpenoid\tpubchem:24778014\tNCBITaxon:1470456\tStreptomyces cyslabdanicus\tterpene\tDiterpene\tLC064028.1\t\t\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1007/s10295-015-1694-6\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Diterpene","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Diterpenoid","compound_index":"1","compound_name":"cyslabdan A","database_ids":"pubchem:24778014","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"LC064028.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001910","primary_reference":"DOI:10.1007/s10295-015-1694-6","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C","standard_inchi":"InChI=1S/C25H41NO5S/c1-7-16(2)9-10-19-24(6)12-8-11-23(4,5)20(24)13-21(28)25(19,31)15-32-14-18(22(29)30)26-17(3)27/h7,9,18-21,28,31H,1,8,10-15H2,2-6H3,(H,26,27)(H,29,30)/b16-9+/t18-,19+,20-,21-,24+,25-/m0/s1","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces cyslabdanicus"},"row_sha256":"168814408ed3c9891513598d71548db749ef58a07c57d2d21ff2780c221e195c"}],"predicate":"exact complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"} |
| support-2309-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2233–2233, row_sha256 168814408ed3c9891513598d71548db749ef58a07c57d2d21ff2780c221e195c | supports | Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Diterpene","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Diterpenoid","compound_index":"1","compound_name":"cyslabdan A","database_ids":"pubchem:24778014","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"LC064028.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001910","primary_reference":"DOI:10.1007/s10295-015-1694-6","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C","standard_inchi":"InChI=1S/C25H41NO5S/c1-7-16(2)9-10-19-24(6)12-8-11-23(4,5)20(24)13-21(28)25(19,31)15-32-14-18(22(29)30)26-17(3)27/h7,9,18-21,28,31H,1,8,10-15H2,2-6H3,(H,26,27)(H,29,30)/b16-9+/t18-,19+,20-,21-,24+,25-/m0/s1","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces cyslabdanicus"}] |
| support-2309-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"} |
| support-2309-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[{"last_physical_line":7116,"physical_line":7116,"raw_tsv_record":"PSUMRJNLBIVEFF-RIVHMUOTSA-N\tStreptomyces cyslabdanicus\tNCBITaxon:1470456\thttp://www.wikidata.org/entity/Q26290150\t10.1038/JA.2016.103\thttp://www.wikidata.org/entity/Q75069072\n","row":{"organism_name":"Streptomyces cyslabdanicus","organism_wikidata":"http://www.wikidata.org/entity/Q26290150","reference_doi":"10.1038/JA.2016.103","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:1470456"},"row_sha256":"216aff7694fc4af312e4a90368df4976e5fac83e6e9bef121223afa417e3a4f3"},{"last_physical_line":7117,"physical_line":7117,"raw_tsv_record":"PSUMRJNLBIVEFF-RIVHMUOTSA-N\tStreptomyces\tNCBITaxon:1883\thttp://www.wikidata.org/entity/Q1144013\t10.1038/JA.2008.102\thttp://www.wikidata.org/entity/Q75069072\n","row":{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1038/JA.2008.102","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:1883"},"row_sha256":"ff3c05e366d3345bcd9ce22327bbcbe37fa83f9a2ef714b3466602dca01ca54b"},{"last_physical_line":7118,"physical_line":7118,"raw_tsv_record":"PSUMRJNLBIVEFF-RIVHMUOTSA-N\tStreptomyces thermocarboxydus\tNCBITaxon:59299\thttp://www.wikidata.org/entity/Q16992819\t10.1007/S00253-019-10240-3\thttp://www.wikidata.org/entity/Q75069072\n","row":{"organism_name":"Streptomyces thermocarboxydus","organism_wikidata":"http://www.wikidata.org/entity/Q16992819","reference_doi":"10.1007/S00253-019-10240-3","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:59299"},"row_sha256":"059498b5595fbf54271b3bb9f10b1bd50ede5fe4bcfb98cf6990dc0936e6c297"}],"predicate":"exact complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"} |
| support-2309-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 7116–7116, row_sha256 216aff7694fc4af312e4a90368df4976e5fac83e6e9bef121223afa417e3a4f3; physical lines 7117–7117, row_sha256 ff3c05e366d3345bcd9ce22327bbcbe37fa83f9a2ef714b3466602dca01ca54b; physical lines 7118–7118, row_sha256 059498b5595fbf54271b3bb9f10b1bd50ede5fe4bcfb98cf6990dc0936e6c297 | supports | Complete retained physical row payloads, every field: [{"organism_name":"Streptomyces cyslabdanicus","organism_wikidata":"http://www.wikidata.org/entity/Q26290150","reference_doi":"10.1038/JA.2016.103","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:1470456"},{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1038/JA.2008.102","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:1883"},{"organism_name":"Streptomyces thermocarboxydus","organism_wikidata":"http://www.wikidata.org/entity/Q16992819","reference_doi":"10.1007/S00253-019-10240-3","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:59299"}] |
| support-2309-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"} |
| support-2309-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[{"last_physical_line":1926,"physical_line":1926,"raw_tsv_record":"PSUMRJNLBIVEFF-RIVHMUOTSA-N\tC/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C\tTerpenoids\tDiterpenoids\tLabdane diterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Labdane diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","superclass_results":"Diterpenoids"},"row_sha256":"738c1a63fdbd5ea790603a39d553bd8f17312724da8855d0ad2ca803e87eeb6f"}],"predicate":"exact complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"} |
| support-2309-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 1926–1926, row_sha256 738c1a63fdbd5ea790603a39d553bd8f17312724da8855d0ad2ca803e87eeb6f | supports | Complete retained physical row payloads, every field: [{"class_results":"Labdane diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","superclass_results":"Diterpenoids"}] |
| support-2309-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"} |
| support-2309-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"} |
| support-2309-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"} |
| support-2309-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[],"predicate":"exact chebi_id from exact full-key structure rows","query":[]} |
| support-2309-source-routes | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20/source_scope_inventory/source_taxa; /contexts/20/source_scope_inventory/forward_taxon_merge_matches; /contexts/20/source_scope_inventory/nonorganism_matches; /contexts/20/source_scope_inventory/actual_assay_rows; /contexts/20/source_scope_inventory/blank_AID_sentinels; /contexts/20/source_scope_inventory/related_corpus_rows | supports | Complete saved routing fields, without fresh taxonomy or source queries: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:1470456","NCBITaxon:1883","NCBITaxon:59299"]} |
| support-2309-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/0; /cached_taxonomy/whole_stanzas/12; /cached_taxonomy/whole_stanzas/30 | supports | Complete retained relevant stanzas; cached labels/synonyms are not fresh external authority: [{"complete_stanza":"[Term]\nid: NCBITaxon:1883\nname: Streptomyces\nsynonym: \"\\\"Microstreptospora\\\" Yan et al.\" EXACT []\nsynonym: \"Actinopycnidium Krasil'nikov 1962\" EXACT []\nsynonym: \"Actinosporangium Krasil'nikov and Yuan 1961\" EXACT []\nsynonym: \"Chainia\" EXACT []\nsynonym: \"Elytrosporangium Falcao de Morais et al. 1966\" EXACT []\nsynonym: \"Kitasatoa Matsumae and Hata 1968 (Approved Lists 1980)\" EXACT []\nsynonym: \"Microellobosporia\" EXACT []\nsynonym: \"Streptoverticillium Baldacci 1958\" EXACT []\n\n","id":"NCBITaxon:1883","physical_line":2798},{"complete_stanza":"[Term]\nid: NCBITaxon:59299\nname: Streptomyces thermocarboxydus\n\n","id":"NCBITaxon:59299","physical_line":27256},{"complete_stanza":"[Term]\nid: NCBITaxon:1470456\nname: Streptomyces cyslabdanicus\n\n","id":"NCBITaxon:1470456","physical_line":130135}] |
| support-2309-direct-contexts | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /records/8/direct_companion_paths; /records/8/direct_companion_predicates | supports | Exact direct companion scope and predicates, not transferred compound-specific evidence: {"direct_companion_paths":["data/natural_products/terpenoids/cyslabdan-b.yaml","data/natural_products/terpenoids/cyslabdan-c.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/terpenoids/cyslabdan-b.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001910"]},{"path":"data/natural_products/terpenoids/cyslabdan-c.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001910"]}]} |
| support-2309-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21; /contexts/22 | supports | Complete linked contexts are available at the selectors; identity and mechanism boundaries are [{"declared_mechanism_roots_literal":[],"identifier":"naturalproductmech:mibig-826d2ff0d3","owned_bgc_ids":["BGC0001910"],"path":"data/natural_products/terpenoids/cyslabdan-b.yaml","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N"},{"declared_mechanism_roots_literal":[],"identifier":"naturalproductmech:mibig-04c341bc33","owned_bgc_ids":["BGC0001910"],"path":"data/natural_products/terpenoids/cyslabdan-c.yaml","standard_inchi_key":"PTRRHQHGAOYEKT-KYXZTKSHSA-N"}]. Shared loci/citations do not transfer identity, activity or reader authority. |
| support-2309-reader-DATA | /private/tmp/npm-review-work/shared-next-batch231/native-current231-cyslabdan-a-maintained-reader-DATA-001.json; /order; /status; /counts; /raw_owner; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner; /reader_call_count; /denials; /unexpected_denials; /errors; /limitations | supports | Original accepted offline maintained reader. Complete owner equality and exact counts: {"component_graphs":0,"component_history_events":[],"component_refs":0,"curation_history":4,"edges":2,"graphs":1,"inline_graphs":1,"molecular_targets":0,"nodes":3,"pathway_steps":1}. The expected denied-before-action IPv6 capability probe is retained; it is not an outbound request. No unexpected denial or error. Preservation does not independently verify primary experiments or protein identity. |
| support-2309-reader-execution | /private/tmp/npm-review-work/shared-next-batch231/native-current231-cyslabdan-a-reader-execution-001.json; Whole original execution receipt | supports | Original single-reader execution, complete saved streams/tool-chain and terminal exit 0; no replay. The command, source/config hashes and process clocks bind the accepted result. |
| support-2309-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-2309-maintained-reader-acceptance-001.json; /status; /order; /DATA; /execution; /verification; /review_check_contract; /limits | supports | ROOT acceptance of this exact original complete-owner reader, with its precise check contract and bounded limits: {"command":"/private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch231/read-selected-mechanism-guarded-001.py 2309 d10634138cd57834c49ec3f0c4070d8bebdd489f1f50f123ab08cc389d2e85a9 5196c6065cb241fcd6d191e17555b752174aec8c28aa970774a1b474a31df89f d65dead86417d910f5158628f12930c526dbc5b81750f9197093bfcb644349d8 d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7 007a2056fbbf41f2bf14358fd9b1d850fb78421cc9b32ffb70ae8bc158f858c9","exit_code":0,"exit_source":"original tool terminal and process receipt","name":"Complete offline maintained reader for cyslabdan-a","required":true,"status":"passed","target_order":2309} |
| support-2309-graph-0 | /private/tmp/npm-review-work/shared-next-batch231/native-current231-cyslabdan-a-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/0 | supports | Complete retained graph, every node, edge, evidence placement and qualified note: {"description":"Terminal Streptomyces cyslabdanicus cyslabdan A biosynthesis graph for Mca-associated hydrolysis of a mycothiol S-conjugate.","edges":[{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Ikeda et al. number cyslabdan A as compound 1 and (7S,8S,12E)-8,17-epoxy-7-hydroxylabda-12,14-diene as compound 4. Their Streptomyces avermitilis SUKA22 mca-deletion experiment carrying the Streptomyces cyslabdanicus cld cluster showed that a mycothiol S-conjugate amidase is required downstream of nonenzymatic mycothiol addition to form cyslabdan A.","reference":"DOI:10.1007/s10295-015-1694-6","snippet":"failed to produce 1, but accumulated 4"},{"evidence_type":"DATABASE_ASSERTION","notes":"MITE0000107 is an active Mca amidase entry for the terminal hydrolysis of the glycosylated mycothiol S-conjugate in cyslabdan A biosynthesis. It links UniProtKB:A0A0H5B8U5, GenPept BAR97454.1, MIBiG BGC0001910 and the Ikeda et al. DOI.","reference":"https://mite.lisc.univie.ac.at/repository/MITE0000107","retrieved_on":"2026-10-01","snippet":"Hydrolysis"},{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001910.4 places BAR97454.1 inside the active Streptomyces cyslabdanicus cyslabdan A/B/C cluster as an amidase CDS and annotates the CDS with MITE0000107.","reference":"https://mibig.secondarymetabolites.org/repository/BGC0001910.4/index.html","retrieved_on":"2026-10-01","snippet":"MITE0000107"},{"evidence_type":"DATABASE_ASSERTION","notes":"Current unreviewed UniProtKB:A0A0H5B8U5 resolves as a Streptomyces cyslabdanicus 379 aa protein and cross-references EMBL LC064028 protein BAR97454.1.","reference":"https://www.uniprot.org/uniprotkb/A0A0H5B8U5","retrieved_on":"2026-10-01","snippet":"A0A0H5B8U5_STRCP"},{"evidence_type":"DATABASE_ASSERTION","notes":"GenPept BAR97454.1 is the 379 aa Streptomyces cyslabdanicus K04-0144 amidase encoded by complement(LC064028.1:10784..11923).","reference":"https://www.ncbi.nlm.nih.gov/protein/BAR97454.1","retrieved_on":"2026-10-01","snippet":"amidase [Streptomyces cyslabdanicus]"}],"notes":"Mca is associated with hydrolysis of the mycothiol S-conjugate amide upstream of cyslabdan A formation.","object":"mca","predicate":"is hydrolyzed by","subject":"cyslabdan_mycothiol_s_conjugate"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Ikeda et al. number cyslabdan A as compound 1 and (7S,8S,12E)-8,17-epoxy-7-hydroxylabda-12,14-diene as compound 4. Their Streptomyces avermitilis SUKA22 mca-deletion experiment carrying the Streptomyces cyslabdanicus cld cluster showed that a mycothiol S-conjugate amidase is required downstream of nonenzymatic mycothiol addition to form cyslabdan A.","reference":"DOI:10.1007/s10295-015-1694-6","snippet":"failed to produce 1, but accumulated 4"},{"evidence_type":"DATABASE_ASSERTION","notes":"MITE0000107 is an active Mca amidase entry for the terminal hydrolysis of the glycosylated mycothiol S-conjugate in cyslabdan A biosynthesis. It links UniProtKB:A0A0H5B8U5, GenPept BAR97454.1, MIBiG BGC0001910 and the Ikeda et al. DOI.","reference":"https://mite.lisc.univie.ac.at/repository/MITE0000107","retrieved_on":"2026-10-01","snippet":"Hydrolysis"},{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001910.4 places BAR97454.1 inside the active Streptomyces cyslabdanicus cyslabdan A/B/C cluster as an amidase CDS and annotates the CDS with MITE0000107.","reference":"https://mibig.secondarymetabolites.org/repository/BGC0001910.4/index.html","retrieved_on":"2026-10-01","snippet":"MITE0000107"},{"evidence_type":"DATABASE_ASSERTION","notes":"Current unreviewed UniProtKB:A0A0H5B8U5 resolves as a Streptomyces cyslabdanicus 379 aa protein and cross-references EMBL LC064028 protein BAR97454.1.","reference":"https://www.uniprot.org/uniprotkb/A0A0H5B8U5","retrieved_on":"2026-10-01","snippet":"A0A0H5B8U5_STRCP"},{"evidence_type":"DATABASE_ASSERTION","notes":"GenPept BAR97454.1 is the 379 aa Streptomyces cyslabdanicus K04-0144 amidase encoded by complement(LC064028.1:10784..11923).","reference":"https://www.ncbi.nlm.nih.gov/protein/BAR97454.1","retrieved_on":"2026-10-01","snippet":"amidase [Streptomyces cyslabdanicus]"}],"notes":"MITE records Mca hydrolysis as forming cyslabdan A.","object":"cyslabdan_a","predicate":"forms","subject":"mca"}],"graph_id":"cyslabdan-a-mca-hydrolysis","nodes":[{"grounding_status":"UNGROUNDED","label":"cyslabdan mycothiol S-conjugate","node_id":"cyslabdan_mycothiol_s_conjugate","node_type":"PRECURSOR"},{"grounding_status":"GROUNDED","identifier":"UniProtKB:A0A0H5B8U5","label":"Mca amidase","node_id":"mca","node_type":"ENZYME"},{"grounding_status":"GROUNDED","identifier":"naturalproductmech:mibig-f3cb15d2b6","label":"cyslabdan A","node_id":"cyslabdan_a","node_type":"COMPOUND"}],"scope":"BIOSYNTHESIS"} |
| support-2309-pathway-0 | /private/tmp/npm-review-work/shared-next-batch231/native-current231-cyslabdan-a-maintained-reader-DATA-001.json; /resolved_view/biosynthetic_pathway/0 | supports | Complete retained pathway entry, preserving optional fields and evidence: {"enzyme_id":"UniProtKB:A0A0H5B8U5","enzyme_label":"Mca amidase","evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Ikeda et al. number cyslabdan A as compound 1 and (7S,8S,12E)-8,17-epoxy-7-hydroxylabda-12,14-diene as compound 4. Their Streptomyces avermitilis SUKA22 mca-deletion experiment carrying the Streptomyces cyslabdanicus cld cluster showed that a mycothiol S-conjugate amidase is required downstream of nonenzymatic mycothiol addition to form cyslabdan A.","reference":"DOI:10.1007/s10295-015-1694-6","snippet":"failed to produce 1, but accumulated 4"},{"evidence_type":"DATABASE_ASSERTION","notes":"MITE0000107 is an active Mca amidase entry for the terminal hydrolysis of the glycosylated mycothiol S-conjugate in cyslabdan A biosynthesis. It links UniProtKB:A0A0H5B8U5, GenPept BAR97454.1, MIBiG BGC0001910 and the Ikeda et al. DOI.","reference":"https://mite.lisc.univie.ac.at/repository/MITE0000107","retrieved_on":"2026-10-01","snippet":"Hydrolysis"},{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001910.4 places BAR97454.1 inside the active Streptomyces cyslabdanicus cyslabdan A/B/C cluster as an amidase CDS and annotates the CDS with MITE0000107.","reference":"https://mibig.secondarymetabolites.org/repository/BGC0001910.4/index.html","retrieved_on":"2026-10-01","snippet":"MITE0000107"},{"evidence_type":"DATABASE_ASSERTION","notes":"Current unreviewed UniProtKB:A0A0H5B8U5 resolves as a Streptomyces cyslabdanicus 379 aa protein and cross-references EMBL LC064028 protein BAR97454.1.","reference":"https://www.uniprot.org/uniprotkb/A0A0H5B8U5","retrieved_on":"2026-10-01","snippet":"A0A0H5B8U5_STRCP"},{"evidence_type":"DATABASE_ASSERTION","notes":"GenPept BAR97454.1 is the 379 aa Streptomyces cyslabdanicus K04-0144 amidase encoded by complement(LC064028.1:10784..11923).","reference":"https://www.ncbi.nlm.nih.gov/protein/BAR97454.1","retrieved_on":"2026-10-01","snippet":"amidase [Streptomyces cyslabdanicus]"}],"notes":"Mca hydrolyzes the glycosylated mycothiol S-conjugate made from the CldC product in the terminal cyslabdan A step. This single-step partial pathway leaves the upstream CldA-CldD enzymatic steps and the nonenzymatic mycothiol addition uncurated.","product":"naturalproductmech:mibig-f3cb15d2b6","step_number":1} |
| support-2309-history | /private/tmp/npm-review-work/shared-next-batch231/native-current231-cyslabdan-a-maintained-reader-DATA-001.json; /resolved_view/curation_history | supports | Complete historical curation events; historical retrieval or sequence notes are not fresh verification: [{"action":"SEEDED_FROM_SOURCES","changes":"Seeded from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-10T05:54:11Z"},{"action":"SEEDED_FROM_SOURCES","changes":"Seeded from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-25T03:03:08Z"},{"action":"RECORD_CURATED","changes":"Added a terminal Mca/UniProtKB:A0A0H5B8U5 hydrolysis pathway step and BIOSYNTHESIS causal graph for cyslabdan A.","curator":"codex","llm_assisted":true,"timestamp":"2026-10-01T21:07:43Z"},{"action":"SEEDED_FROM_SOURCES","changes":"Seeded from the committed inventories and curation tables.","curator":"seed_from_sources","timestamp":"2026-10-13T10:44:44Z"}] |
| support-2309-manual-mobile-H-witness | /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json; /records/8/smiles/computed; /records/8/inchi/computed; /records/8/comparisons; /records/8/atom_correspondence | supports | Bounded independent interpretation of the saved tables: {"limits":"Original diagnostic empty map, false canonical flags, complete_atom_count_match:false and full_graph_identity_established:false are preserved. This witness neither replaces those results nor proves natural fixed-graph identity.","method":"Manual explicit saved-table correspondence, no molecule parse or graph search","observer_terminal":"a95c6e/0","only_atom_changes":"N21→25 total H 1→0; O23→26 total H 0→1","only_bond_changes":"SMILES bond21→InChI bond20 C–N SINGLE→DOUBLE; bond22→21 C=O DOUBLE→SINGLE","preserved":"All mapped adjacency, elements, formal charge, isotope, degree, aromatic/ring membership, CIP labels and neighbour-relative tetrahedral parity otherwise agree. Added imidic C=N potential is unassigned.","smiles_to_inchi_indices":[1,15,8,9,18,23,11,7,10,22,19,12,20,24,14,31,13,17,21,28,29,25,16,26,2,30,27,3,4,5,6,0]} |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-231/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-231/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-231/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-231/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-231/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. External identifiers, primary publications, taxonomy and natural stereochemical assignments were not refreshed under the absolute no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original local gates and successful stored parses establish only their stated mechanical scope.
- Empty joins concern only exact saved predicates and snapshots. Shared loci, taxa and citations do not transfer compound-specific production, activity, mechanism or independent-study status.
- Four original undefined-stereo warnings remain global and unassigned to records. No additional molecular/YAML parse, source query or target invocation occurred during scientific authoring.
- No source record, native curation status or history is edited. Any later correction belongs to the maintained owners listed in the accepted canonical intake.
- Accepted maintained-reader equality establishes complete local owner preservation only. Protein-family/reaction grounding, historical construct notes and proposed steps retain their explicit evidence limits.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete owner/history and actual canonical intake were read; matching source payloads, full cached stanzas and companion attribution are retained in the pinned source notes.
- Support personally read all six saved forms for these three owners: 154 atom rows and 166 bond rows plus every scalar, ring, stereo, motif and original mapping/comparison field. The Cyslabdan A manual witness is separate from the original failed map.
- ROOT operated original activation/capture and independently accepted the maintained results; Support operated original canonical intakes; Native operated original gates, chemistry and all three maintained readers; BGC operated original collector/composer. No new target was invoked during these assessments.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T222704Z-cyslabdan-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: cyslabdan A'
started_at: '2026-11-03T21:43:37.806034Z'
finished_at: '2026-11-03T22:27:04.911273Z'
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
summary: Cyslabdan A preserves its exact retained source key, distinct producer/locus/occurrence
  grades and a partial terminal Mca pathway. Stored-form canonical differences are
  explained by a bounded amide/imidic mobile-H witness without replacing the original
  failed graph mapping. The maintained reader preserves the complete historical mechanism;
  scientific completion remains partial.
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
  - path: data/natural_products/terpenoids/cyslabdan-a.yaml
    sha256: 49f630e192b2c029fccafb33e4506b0c4f6c2dc4786b2df278887c8cae21f5ae
    role: target
  - path: data/natural_products/terpenoids/cyslabdan-b.yaml
    sha256: d505c35b58d2eb17171996ca53704aedfbb0fd7a2db369f9e761ac3197ed12df
    role: context
  - path: data/natural_products/terpenoids/cyslabdan-c.yaml
    sha256: 6ab0f6ad6f58fd49b40cd8f0243a743d9d5f8e06d1f7f9c0adfd77c8e254a42a
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
  selection: Campaign path order 2309; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
targets:
- target_id: naturalproductmech:mibig-f3cb15d2b6
  path: data/natural_products/terpenoids/cyslabdan-a.yaml
  label: cyslabdan A
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
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/terpenoids/cyslabdan-a.yaml
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
- name: Complete offline maintained reader for cyslabdan-a
  status: passed
  required: true
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch231/read-selected-mechanism-guarded-001.py
    2309 d10634138cd57834c49ec3f0c4070d8bebdd489f1f50f123ab08cc389d2e85a9 5196c6065cb241fcd6d191e17555b752174aec8c28aa970774a1b474a31df89f
    d65dead86417d910f5158628f12930c526dbc5b81750f9197093bfcb644349d8 d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
    007a2056fbbf41f2bf14358fd9b1d850fb78421cc9b32ffb70ae8bc158f858c9
  exit_code: 0
  check_id: maintained-mechanism-reader
  summary: 'The original offline maintained reader returned the complete expected
    owner for order 2309: 1 graphs, 3 nodes, 2 edges, 1 pathway entries and 4 history
    events. Complete owner equality and original terminal exit 0 are ROOT-accepted;
    no unexpected denial or error occurred. This check establishes local preservation,
    not independent biological or primary-source verification.'
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  evidence_ids:
  - support-2309-reader-DATA
  - support-2309-reader-execution
  - support-2309-reader-acceptance
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  command: just validate-strict data/natural_products/terpenoids/compound-12.yaml
    data/natural_products/terpenoids/compound-15.yaml data/natural_products/terpenoids/compound-7a.yaml
    data/natural_products/terpenoids/conidiogenone.yaml data/natural_products/terpenoids/cucurbitacin-c.yaml
    data/natural_products/terpenoids/culmorin.yaml data/natural_products/terpenoids/cyatha-3-12-diene.yaml
    data/natural_products/terpenoids/cyclooctatin.yaml data/natural_products/terpenoids/cyslabdan-a.yaml
    data/natural_products/terpenoids/cyslabdan-b.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-231/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-f3cb15d2b6
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-231/validate-all-001.tsv
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
  - naturalproductmech:mibig-f3cb15d2b6
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
  - naturalproductmech:mibig-f3cb15d2b6
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
  - naturalproductmech:mibig-f3cb15d2b6
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-231/review-queue-001.tsv
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
  - naturalproductmech:mibig-f3cb15d2b6
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2309-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/cyslabdan-a.yaml
  locator: Whole current owner plaintext, including complete curation_history
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete current owner/history personally read with exact prior reading
    attribution; no YAML parse or native-status edit. The complete owner is preserved
    in the accepted capture and maintained result.
  snapshot_sha256: 49f630e192b2c029fccafb33e4506b0c4f6c2dc4786b2df278887c8cae21f5ae
- evidence_id: support-2309-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/8
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete actual captured owner and component scope; this owner has no declared
    component routes.
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2309-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/intakes/2309-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete accepted canonical intake, including exact source ownership and
    maintained implementation dependencies. This is inspection scope, not a scientific
    verdict.
  snapshot_sha256: 5196c6065cb241fcd6d191e17555b752174aec8c28aa970774a1b474a31df89f
- evidence_id: support-2309-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"chemical_structure":{"smiles":"C/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C","standard_inchi":"InChI=1S/C25H41NO5S/c1-7-16(2)9-10-19-24(6)12-8-11-23(4,5)20(24)13-21(28)25(19,31)15-32-14-18(22(29)30)26-17(3)27/h7,9,18-21,28,31H,1,8,10-15H2,2-6H3,(H,26,27)(H,29,30)/b16-9+/t18-,19+,20-,21-,24+,25-/m0/s1","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001910"},"grounding_notes":"No
    3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-f3cb15d2b6","label":"cyslabdan
    A","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-f3cb15d2b6","source":"MIBIG","source_id":"BGC0001910","source_label":"cyslabdan
    A","source_version":"4"}],"xrefs":["pubchem:24778014"]}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2309-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0001910","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"4","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001910 entry version 4; citation taken from the compound evidence level","reference":"DOI:10.1007/s10295-015-1694-6"}],"genome_accession":"genbank:LC064028.1","link_evidence_basis":"CLUSTER_UNSTATED","organism_label":"Streptomyces
    cyslabdanicus","organism_taxon_id":"NCBITaxon:1470456"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0001910","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001910 entry version 4; citation taken from the compound evidence level","reference":"DOI:10.1007/s10295-015-1694-6"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus
    evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this
    field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"4","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces
    cyslabdanicus"}],"producer_taxon_groups":["ACTINOBACTERIAL"]}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2309-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"occurrence_taxon_groups":["ACTINOBACTERIAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1038/JA.2008.102"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1144013","source":"LOTUS","taxon_id":"NCBITaxon:1883","taxon_label":"Streptomyces","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1007/S00253-019-10240-3"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q16992819","source":"LOTUS","taxon_id":"NCBITaxon:59299","taxon_label":"Streptomyces
    thermocarboxydus","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1038/JA.2016.103"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q26290150 This taxon is also recorded
    as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.","source":"LOTUS","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces
    cyslabdanicus","taxon_source":"NCBITaxon"}]}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2309-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2309-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","compound_classes":["Diterpenoid"],"np_classification":{"class_results":["Labdane
    diterpenoids"],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Diterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2309-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/smiles/status; /records/8/inchi/status;
    /records/8/smiles/computed; /records/8/inchi/computed; /records/8/comparisons;
    /records/8/atom_correspondence
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Both stored forms parsed. Exact original comparison and correspondence
    values, preserved without a new parse: {"atom_correspondence":{"complete_atom_count_match":false,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim.","smiles_to_inchi_atom_indices":[]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":false,"canonical_nonisomeric_smiles_equal":false,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"inchi_stereo":{"Atom_Tetrahedral:Specified":6,"Bond_Double:Specified":1,"Bond_Double:Unspecified":1},"smiles_stereo":{"Atom_Tetrahedral:Specified":6,"Bond_Double:Specified":1}}'
  snapshot_sha256: 5696325ae03369015ee813b99d1d51da767e934b2ac887dd9e29f2c27d0405bf
- evidence_id: support-2309-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/smiles/status; /records/8/inchi/status;
    /records/8/smiles/computed; /records/8/inchi/computed; /records/8/comparisons;
    /records/8/atom_correspondence
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Both saved forms are neutral C25H41NO5S with 32 heavy atoms and 33 bonds,
    two six-carbon rings, a terminal alkene, an E side-chain alkene, two scaffold
    hydroxyls and a sulfur-linked N-acetylcysteine substituent. Six tetrahedral centres
    are specified. The stored SMILES amide N21–C22(=O23) corresponds locally to decoded
    imidic N25=C16–O26H: nitrogen loses one hydrogen, oxygen gains one, C–N becomes
    double and C=O becomes single. The decoded form adds an unspecified imidic C=N
    stereo possibility. Formula, charge, standard InChI and full key agree, but both
    canonical-SMILES equality flags are false, the original atom map is empty, complete_atom_count_match
    is false and full_graph_identity_established is false.'
  snapshot_sha256: 5696325ae03369015ee813b99d1d51da767e934b2ac887dd9e29f2c27d0405bf
- evidence_id: support-2309-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Native operated one original stored-form diagnostic, exit 0, with preserved
    stdout/stderr and closed environment. The inherited DATA observer literal is not
    the operator attribution.
  snapshot_sha256: 65040543ad69a2d54b0cf784884a78bf49a7bf1c68cdec31272f1ada872be8db
- evidence_id: support-2309-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-chemistry-acceptance-001.json
  locator: Whole ROOT chemistry acceptance
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: ROOT accepts the original 20 stored parses and retains 96 true/four false
    flags, two empty maps and four global unassigned warnings; it establishes no natural
    identity or fixed-graph equivalence.
  snapshot_sha256: 129083683fbfc7528e17bfe7fcd04e7ceb7e44708a11682d024e10f384d5c740
- evidence_id: support-2309-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-native-gates-acceptance-001.json
  locator: Whole ROOT gate acceptance and selected queue rows
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Five original local gates passed; all_native_gates_passed is false because
    full QC and complete OAK remain unavailable. Selected queues are follow-up context,
    not automatic scientific findings.
  snapshot_sha256: b7921dc6afa5d8ce9587a5a097e427772c0b5b739481a22f8e61ce9bcb9e78cc
- evidence_id: support-2309-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-intake-acceptance-001.json
  locator: Whole ROOT intake acceptance
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: ROOT accepts ten actual one-record intakes, 411 source placements / 68
    paths and exact ownership; no scientific verdict follows from intake success.
  snapshot_sha256: af10db4855db731afb28ba6c9d972835e1c1689b3b6089b80d9ed7a76dd1118f
- evidence_id: support-2309-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-source-inventory-acceptance-001.json
  locator: Whole ROOT source-inventory acceptance
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: ROOT accepts the one original local inventory and its current input/capture/source
    joins; complete scientific reading is separately attributed in the notes.
  snapshot_sha256: a50f4decab71502d06fc10d04836ee324c2b09c0fdf118ea5826e7e7c4640d03
- evidence_id: support-2309-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-input-plan-acceptance-001.json
  locator: Whole ROOT input-plan acceptance
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: ROOT accepts the exact current plan and preserved source contexts; no scientific
    verdict or future reader success is inferred.
  snapshot_sha256: 2f7c566f713e12b9b357d9e9c870cb6c05ee90ca30a53c0879a5e5d6a547fa6f
- evidence_id: support-2309-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete disjoint source/raw-history reading attribution and bounded compound-specific
    cautions; no pre-intake verdict was asserted.
  snapshot_sha256: c178e2f5d22e7bf22457f90632cb8bd1b05ce4caf2a993684e4a357a81188afd
- evidence_id: support-2309-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Eight current pinned implemented curation tables were directly opened ignoring
    ignore rules; 101 exact case-sensitive cohort literals against 93 data rows yielded
    zero matches within that scope. Reserved decisions.tsv was not consumed.
  snapshot_sha256: c178e2f5d22e7bf22457f90632cb8bd1b05ce4caf2a993684e4a357a81188afd
- evidence_id: support-2309-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: ChemicalStructure preserves source representation and standardized-key
    limitations. stereo_complete describes undefined centres; ComputedClassification
    is a named/versioned prediction, never a source assertion or admission criterion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2309-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Maintained stereo_complete derives from FindMolChiralCenters and the absence
    of question-mark centre tags; it is not a blanket all-bond-geometry proof.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2309-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 974–1065
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Maintained seeding preserves the source structure and named/versioned classifier
    output while separately retaining BGC and source compound classes.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2309-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: One-record scientific review requires claim-level evidence and twelve dimensions
    with truthful partial-completion/unavailable-check limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2309-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current skill
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: The review does not edit records; source access is bounded by the overriding
    no-request instruction.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: support-2309-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-target-input-plan-001.json
  locator: /records/8
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete actual owner-specific input map and direct/additional roles. Historical
    planning language does not claim a reader result; actual reader evidence is linked
    separately.
  snapshot_sha256: 641feb36d59176354fbea2afb95ff2e5d7c1ea3253b71291ca442c15482dab14
- evidence_id: support-2309-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[{"last_physical_line":2233,"physical_line":2233,"raw_tsv_record":"BGC0001910\t4\tactive\tquestionable\tunknown\tcyslabdan
    A\t1\tC/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C\tInChI=1S/C25H41NO5S/c1-7-16(2)9-10-19-24(6)12-8-11-23(4,5)20(24)13-21(28)25(19,31)15-32-14-18(22(29)30)26-17(3)27/h7,9,18-21,28,31H,1,8,10-15H2,2-6H3,(H,26,27)(H,29,30)/b16-9+/t18-,19+,20-,21-,24+,25-/m0/s1\tPSUMRJNLBIVEFF-RIVHMUOTSA-N\ttrue\tDiterpenoid\tpubchem:24778014\tNCBITaxon:1470456\tStreptomyces
    cyslabdanicus\tterpene\tDiterpene\tLC064028.1\t\t\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1007/s10295-015-1694-6\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Diterpene","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Diterpenoid","compound_index":"1","compound_name":"cyslabdan
    A","database_ids":"pubchem:24778014","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"LC064028.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001910","primary_reference":"DOI:10.1007/s10295-015-1694-6","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C","standard_inchi":"InChI=1S/C25H41NO5S/c1-7-16(2)9-10-19-24(6)12-8-11-23(4,5)20(24)13-21(28)25(19,31)15-32-14-18(22(29)30)26-17(3)27/h7,9,18-21,28,31H,1,8,10-15H2,2-6H3,(H,26,27)(H,29,30)/b16-9+/t18-,19+,20-,21-,24+,25-/m0/s1","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces
    cyslabdanicus"},"row_sha256":"168814408ed3c9891513598d71548db749ef58a07c57d2d21ff2780c221e195c"}],"predicate":"exact
    complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2233–2233, row_sha256 168814408ed3c9891513598d71548db749ef58a07c57d2d21ff2780c221e195c
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Diterpene","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Diterpenoid","compound_index":"1","compound_name":"cyslabdan
    A","database_ids":"pubchem:24778014","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"LC064028.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001910","primary_reference":"DOI:10.1007/s10295-015-1694-6","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C","standard_inchi":"InChI=1S/C25H41NO5S/c1-7-16(2)9-10-19-24(6)12-8-11-23(4,5)20(24)13-21(28)25(19,31)15-32-14-18(22(29)30)26-17(3)27/h7,9,18-21,28,31H,1,8,10-15H2,2-6H3,(H,26,27)(H,29,30)/b16-9+/t18-,19+,20-,21-,24+,25-/m0/s1","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces
    cyslabdanicus"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2309-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[{"last_physical_line":7116,"physical_line":7116,"raw_tsv_record":"PSUMRJNLBIVEFF-RIVHMUOTSA-N\tStreptomyces
    cyslabdanicus\tNCBITaxon:1470456\thttp://www.wikidata.org/entity/Q26290150\t10.1038/JA.2016.103\thttp://www.wikidata.org/entity/Q75069072\n","row":{"organism_name":"Streptomyces
    cyslabdanicus","organism_wikidata":"http://www.wikidata.org/entity/Q26290150","reference_doi":"10.1038/JA.2016.103","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:1470456"},"row_sha256":"216aff7694fc4af312e4a90368df4976e5fac83e6e9bef121223afa417e3a4f3"},{"last_physical_line":7117,"physical_line":7117,"raw_tsv_record":"PSUMRJNLBIVEFF-RIVHMUOTSA-N\tStreptomyces\tNCBITaxon:1883\thttp://www.wikidata.org/entity/Q1144013\t10.1038/JA.2008.102\thttp://www.wikidata.org/entity/Q75069072\n","row":{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1038/JA.2008.102","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:1883"},"row_sha256":"ff3c05e366d3345bcd9ce22327bbcbe37fa83f9a2ef714b3466602dca01ca54b"},{"last_physical_line":7118,"physical_line":7118,"raw_tsv_record":"PSUMRJNLBIVEFF-RIVHMUOTSA-N\tStreptomyces
    thermocarboxydus\tNCBITaxon:59299\thttp://www.wikidata.org/entity/Q16992819\t10.1007/S00253-019-10240-3\thttp://www.wikidata.org/entity/Q75069072\n","row":{"organism_name":"Streptomyces
    thermocarboxydus","organism_wikidata":"http://www.wikidata.org/entity/Q16992819","reference_doi":"10.1007/S00253-019-10240-3","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:59299"},"row_sha256":"059498b5595fbf54271b3bb9f10b1bd50ede5fe4bcfb98cf6990dc0936e6c297"}],"predicate":"exact
    complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 7116–7116, row_sha256 216aff7694fc4af312e4a90368df4976e5fac83e6e9bef121223afa417e3a4f3;
    physical lines 7117–7117, row_sha256 ff3c05e366d3345bcd9ce22327bbcbe37fa83f9a2ef714b3466602dca01ca54b;
    physical lines 7118–7118, row_sha256 059498b5595fbf54271b3bb9f10b1bd50ede5fe4bcfb98cf6990dc0936e6c297
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"organism_name":"Streptomyces
    cyslabdanicus","organism_wikidata":"http://www.wikidata.org/entity/Q26290150","reference_doi":"10.1038/JA.2016.103","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:1470456"},{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1038/JA.2008.102","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:1883"},{"organism_name":"Streptomyces
    thermocarboxydus","organism_wikidata":"http://www.wikidata.org/entity/Q16992819","reference_doi":"10.1007/S00253-019-10240-3","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q75069072","taxon_id":"NCBITaxon:59299"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2309-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[{"last_physical_line":1926,"physical_line":1926,"raw_tsv_record":"PSUMRJNLBIVEFF-RIVHMUOTSA-N\tC/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C\tTerpenoids\tDiterpenoids\tLabdane
    diterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Labdane
    diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","superclass_results":"Diterpenoids"},"row_sha256":"738c1a63fdbd5ea790603a39d553bd8f17312724da8855d0ad2ca803e87eeb6f"}],"predicate":"exact
    complete standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 1926–1926, row_sha256 738c1a63fdbd5ea790603a39d553bd8f17312724da8855d0ad2ca803e87eeb6f
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"class_results":"Labdane
    diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C/C(=C\\C[C@@H]1[C@]2(CCCC([C@@H]2C[C@@H]([C@@]1(CSC[C@@H](C(=O)O)NC(=O)C)O)O)(C)C)C)/C=C","standard_inchi_key":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","superclass_results":"Diterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2309-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"PSUMRJNLBIVEFF-RIVHMUOTSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[],"predicate":"exact chebi_id
    from exact full-key structure rows","query":[]}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20/source_scope_inventory/source_taxa; /contexts/20/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/20/source_scope_inventory/nonorganism_matches; /contexts/20/source_scope_inventory/actual_assay_rows;
    /contexts/20/source_scope_inventory/blank_AID_sentinels; /contexts/20/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete saved routing fields, without fresh taxonomy or source queries:
    {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:1470456","NCBITaxon:1883","NCBITaxon:59299"]}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/0; /cached_taxonomy/whole_stanzas/12;
    /cached_taxonomy/whole_stanzas/30
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained relevant stanzas; cached labels/synonyms are not fresh
    external authority: [{"complete_stanza":"[Term]\nid: NCBITaxon:1883\nname: Streptomyces\nsynonym:
    \"\\\"Microstreptospora\\\" Yan et al.\" EXACT []\nsynonym: \"Actinopycnidium
    Krasil''nikov 1962\" EXACT []\nsynonym: \"Actinosporangium Krasil''nikov and Yuan
    1961\" EXACT []\nsynonym: \"Chainia\" EXACT []\nsynonym: \"Elytrosporangium Falcao
    de Morais et al. 1966\" EXACT []\nsynonym: \"Kitasatoa Matsumae and Hata 1968
    (Approved Lists 1980)\" EXACT []\nsynonym: \"Microellobosporia\" EXACT []\nsynonym:
    \"Streptoverticillium Baldacci 1958\" EXACT []\n\n","id":"NCBITaxon:1883","physical_line":2798},{"complete_stanza":"[Term]\nid:
    NCBITaxon:59299\nname: Streptomyces thermocarboxydus\n\n","id":"NCBITaxon:59299","physical_line":27256},{"complete_stanza":"[Term]\nid:
    NCBITaxon:1470456\nname: Streptomyces cyslabdanicus\n\n","id":"NCBITaxon:1470456","physical_line":130135}]'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /records/8/direct_companion_paths; /records/8/direct_companion_predicates
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Exact direct companion scope and predicates, not transferred compound-specific
    evidence: {"direct_companion_paths":["data/natural_products/terpenoids/cyslabdan-b.yaml","data/natural_products/terpenoids/cyslabdan-c.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/terpenoids/cyslabdan-b.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001910"]},{"path":"data/natural_products/terpenoids/cyslabdan-c.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001910"]}]}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21; /contexts/22
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete linked contexts are available at the selectors; identity and mechanism
    boundaries are [{"declared_mechanism_roots_literal":[],"identifier":"naturalproductmech:mibig-826d2ff0d3","owned_bgc_ids":["BGC0001910"],"path":"data/natural_products/terpenoids/cyslabdan-b.yaml","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N"},{"declared_mechanism_roots_literal":[],"identifier":"naturalproductmech:mibig-04c341bc33","owned_bgc_ids":["BGC0001910"],"path":"data/natural_products/terpenoids/cyslabdan-c.yaml","standard_inchi_key":"PTRRHQHGAOYEKT-KYXZTKSHSA-N"}].
    Shared loci/citations do not transfer identity, activity or reader authority.
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2309-reader-DATA
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-cyslabdan-a-maintained-reader-DATA-001.json
  locator: /order; /status; /counts; /raw_owner; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner;
    /reader_call_count; /denials; /unexpected_denials; /errors; /limitations
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Original accepted offline maintained reader. Complete owner equality and
    exact counts: {"component_graphs":0,"component_history_events":[],"component_refs":0,"curation_history":4,"edges":2,"graphs":1,"inline_graphs":1,"molecular_targets":0,"nodes":3,"pathway_steps":1}.
    The expected denied-before-action IPv6 capability probe is retained; it is not
    an outbound request. No unexpected denial or error. Preservation does not independently
    verify primary experiments or protein identity.'
  snapshot_sha256: 6a4902264b9223614ffdbac026bbd511263b74ca752483a0aaeca350b96eb1e2
- evidence_id: support-2309-reader-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-cyslabdan-a-reader-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Original single-reader execution, complete saved streams/tool-chain and
    terminal exit 0; no replay. The command, source/config hashes and process clocks
    bind the accepted result.
  snapshot_sha256: d1f3baaee7759158287f7b75f3db2ddba6c7f1f404191ba8f78dd2860bd930a5
- evidence_id: support-2309-reader-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-2309-maintained-reader-acceptance-001.json
  locator: /status; /order; /DATA; /execution; /verification; /review_check_contract;
    /limits
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'ROOT acceptance of this exact original complete-owner reader, with its
    precise check contract and bounded limits: {"command":"/private/tmp/npm-record-reviews-20261021/.venv/bin/python
    -I -B /private/tmp/npm-review-work/shared-next-batch231/read-selected-mechanism-guarded-001.py
    2309 d10634138cd57834c49ec3f0c4070d8bebdd489f1f50f123ab08cc389d2e85a9 5196c6065cb241fcd6d191e17555b752174aec8c28aa970774a1b474a31df89f
    d65dead86417d910f5158628f12930c526dbc5b81750f9197093bfcb644349d8 d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
    007a2056fbbf41f2bf14358fd9b1d850fb78421cc9b32ffb70ae8bc158f858c9","exit_code":0,"exit_source":"original
    tool terminal and process receipt","name":"Complete offline maintained reader
    for cyslabdan-a","required":true,"status":"passed","target_order":2309}'
  snapshot_sha256: 40c5b3280148fa50c70d4d68a1f39895a26a73b435df24662e2fce9e6d33c2e7
- evidence_id: support-2309-graph-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-cyslabdan-a-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/0
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained graph, every node, edge, evidence placement and qualified
    note: {"description":"Terminal Streptomyces cyslabdanicus cyslabdan A biosynthesis
    graph for Mca-associated hydrolysis of a mycothiol S-conjugate.","edges":[{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Ikeda
    et al. number cyslabdan A as compound 1 and (7S,8S,12E)-8,17-epoxy-7-hydroxylabda-12,14-diene
    as compound 4. Their Streptomyces avermitilis SUKA22 mca-deletion experiment carrying
    the Streptomyces cyslabdanicus cld cluster showed that a mycothiol S-conjugate
    amidase is required downstream of nonenzymatic mycothiol addition to form cyslabdan
    A.","reference":"DOI:10.1007/s10295-015-1694-6","snippet":"failed to produce 1,
    but accumulated 4"},{"evidence_type":"DATABASE_ASSERTION","notes":"MITE0000107
    is an active Mca amidase entry for the terminal hydrolysis of the glycosylated
    mycothiol S-conjugate in cyslabdan A biosynthesis. It links UniProtKB:A0A0H5B8U5,
    GenPept BAR97454.1, MIBiG BGC0001910 and the Ikeda et al. DOI.","reference":"https://mite.lisc.univie.ac.at/repository/MITE0000107","retrieved_on":"2026-10-01","snippet":"Hydrolysis"},{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001910.4 places BAR97454.1 inside the active Streptomyces cyslabdanicus cyslabdan
    A/B/C cluster as an amidase CDS and annotates the CDS with MITE0000107.","reference":"https://mibig.secondarymetabolites.org/repository/BGC0001910.4/index.html","retrieved_on":"2026-10-01","snippet":"MITE0000107"},{"evidence_type":"DATABASE_ASSERTION","notes":"Current
    unreviewed UniProtKB:A0A0H5B8U5 resolves as a Streptomyces cyslabdanicus 379 aa
    protein and cross-references EMBL LC064028 protein BAR97454.1.","reference":"https://www.uniprot.org/uniprotkb/A0A0H5B8U5","retrieved_on":"2026-10-01","snippet":"A0A0H5B8U5_STRCP"},{"evidence_type":"DATABASE_ASSERTION","notes":"GenPept
    BAR97454.1 is the 379 aa Streptomyces cyslabdanicus K04-0144 amidase encoded by
    complement(LC064028.1:10784..11923).","reference":"https://www.ncbi.nlm.nih.gov/protein/BAR97454.1","retrieved_on":"2026-10-01","snippet":"amidase
    [Streptomyces cyslabdanicus]"}],"notes":"Mca is associated with hydrolysis of
    the mycothiol S-conjugate amide upstream of cyslabdan A formation.","object":"mca","predicate":"is
    hydrolyzed by","subject":"cyslabdan_mycothiol_s_conjugate"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Ikeda
    et al. number cyslabdan A as compound 1 and (7S,8S,12E)-8,17-epoxy-7-hydroxylabda-12,14-diene
    as compound 4. Their Streptomyces avermitilis SUKA22 mca-deletion experiment carrying
    the Streptomyces cyslabdanicus cld cluster showed that a mycothiol S-conjugate
    amidase is required downstream of nonenzymatic mycothiol addition to form cyslabdan
    A.","reference":"DOI:10.1007/s10295-015-1694-6","snippet":"failed to produce 1,
    but accumulated 4"},{"evidence_type":"DATABASE_ASSERTION","notes":"MITE0000107
    is an active Mca amidase entry for the terminal hydrolysis of the glycosylated
    mycothiol S-conjugate in cyslabdan A biosynthesis. It links UniProtKB:A0A0H5B8U5,
    GenPept BAR97454.1, MIBiG BGC0001910 and the Ikeda et al. DOI.","reference":"https://mite.lisc.univie.ac.at/repository/MITE0000107","retrieved_on":"2026-10-01","snippet":"Hydrolysis"},{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001910.4 places BAR97454.1 inside the active Streptomyces cyslabdanicus cyslabdan
    A/B/C cluster as an amidase CDS and annotates the CDS with MITE0000107.","reference":"https://mibig.secondarymetabolites.org/repository/BGC0001910.4/index.html","retrieved_on":"2026-10-01","snippet":"MITE0000107"},{"evidence_type":"DATABASE_ASSERTION","notes":"Current
    unreviewed UniProtKB:A0A0H5B8U5 resolves as a Streptomyces cyslabdanicus 379 aa
    protein and cross-references EMBL LC064028 protein BAR97454.1.","reference":"https://www.uniprot.org/uniprotkb/A0A0H5B8U5","retrieved_on":"2026-10-01","snippet":"A0A0H5B8U5_STRCP"},{"evidence_type":"DATABASE_ASSERTION","notes":"GenPept
    BAR97454.1 is the 379 aa Streptomyces cyslabdanicus K04-0144 amidase encoded by
    complement(LC064028.1:10784..11923).","reference":"https://www.ncbi.nlm.nih.gov/protein/BAR97454.1","retrieved_on":"2026-10-01","snippet":"amidase
    [Streptomyces cyslabdanicus]"}],"notes":"MITE records Mca hydrolysis as forming
    cyslabdan A.","object":"cyslabdan_a","predicate":"forms","subject":"mca"}],"graph_id":"cyslabdan-a-mca-hydrolysis","nodes":[{"grounding_status":"UNGROUNDED","label":"cyslabdan
    mycothiol S-conjugate","node_id":"cyslabdan_mycothiol_s_conjugate","node_type":"PRECURSOR"},{"grounding_status":"GROUNDED","identifier":"UniProtKB:A0A0H5B8U5","label":"Mca
    amidase","node_id":"mca","node_type":"ENZYME"},{"grounding_status":"GROUNDED","identifier":"naturalproductmech:mibig-f3cb15d2b6","label":"cyslabdan
    A","node_id":"cyslabdan_a","node_type":"COMPOUND"}],"scope":"BIOSYNTHESIS"}'
  snapshot_sha256: 6a4902264b9223614ffdbac026bbd511263b74ca752483a0aaeca350b96eb1e2
- evidence_id: support-2309-pathway-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-cyslabdan-a-maintained-reader-DATA-001.json
  locator: /resolved_view/biosynthetic_pathway/0
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained pathway entry, preserving optional fields and evidence:
    {"enzyme_id":"UniProtKB:A0A0H5B8U5","enzyme_label":"Mca amidase","evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Ikeda
    et al. number cyslabdan A as compound 1 and (7S,8S,12E)-8,17-epoxy-7-hydroxylabda-12,14-diene
    as compound 4. Their Streptomyces avermitilis SUKA22 mca-deletion experiment carrying
    the Streptomyces cyslabdanicus cld cluster showed that a mycothiol S-conjugate
    amidase is required downstream of nonenzymatic mycothiol addition to form cyslabdan
    A.","reference":"DOI:10.1007/s10295-015-1694-6","snippet":"failed to produce 1,
    but accumulated 4"},{"evidence_type":"DATABASE_ASSERTION","notes":"MITE0000107
    is an active Mca amidase entry for the terminal hydrolysis of the glycosylated
    mycothiol S-conjugate in cyslabdan A biosynthesis. It links UniProtKB:A0A0H5B8U5,
    GenPept BAR97454.1, MIBiG BGC0001910 and the Ikeda et al. DOI.","reference":"https://mite.lisc.univie.ac.at/repository/MITE0000107","retrieved_on":"2026-10-01","snippet":"Hydrolysis"},{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001910.4 places BAR97454.1 inside the active Streptomyces cyslabdanicus cyslabdan
    A/B/C cluster as an amidase CDS and annotates the CDS with MITE0000107.","reference":"https://mibig.secondarymetabolites.org/repository/BGC0001910.4/index.html","retrieved_on":"2026-10-01","snippet":"MITE0000107"},{"evidence_type":"DATABASE_ASSERTION","notes":"Current
    unreviewed UniProtKB:A0A0H5B8U5 resolves as a Streptomyces cyslabdanicus 379 aa
    protein and cross-references EMBL LC064028 protein BAR97454.1.","reference":"https://www.uniprot.org/uniprotkb/A0A0H5B8U5","retrieved_on":"2026-10-01","snippet":"A0A0H5B8U5_STRCP"},{"evidence_type":"DATABASE_ASSERTION","notes":"GenPept
    BAR97454.1 is the 379 aa Streptomyces cyslabdanicus K04-0144 amidase encoded by
    complement(LC064028.1:10784..11923).","reference":"https://www.ncbi.nlm.nih.gov/protein/BAR97454.1","retrieved_on":"2026-10-01","snippet":"amidase
    [Streptomyces cyslabdanicus]"}],"notes":"Mca hydrolyzes the glycosylated mycothiol
    S-conjugate made from the CldC product in the terminal cyslabdan A step. This
    single-step partial pathway leaves the upstream CldA-CldD enzymatic steps and
    the nonenzymatic mycothiol addition uncurated.","product":"naturalproductmech:mibig-f3cb15d2b6","step_number":1}'
  snapshot_sha256: 6a4902264b9223614ffdbac026bbd511263b74ca752483a0aaeca350b96eb1e2
- evidence_id: support-2309-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-cyslabdan-a-maintained-reader-DATA-001.json
  locator: /resolved_view/curation_history
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete historical curation events; historical retrieval or sequence
    notes are not fresh verification: [{"action":"SEEDED_FROM_SOURCES","changes":"Seeded
    from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-10T05:54:11Z"},{"action":"SEEDED_FROM_SOURCES","changes":"Seeded
    from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-25T03:03:08Z"},{"action":"RECORD_CURATED","changes":"Added
    a terminal Mca/UniProtKB:A0A0H5B8U5 hydrolysis pathway step and BIOSYNTHESIS causal
    graph for cyslabdan A.","curator":"codex","llm_assisted":true,"timestamp":"2026-10-01T21:07:43Z"},{"action":"SEEDED_FROM_SOURCES","changes":"Seeded
    from the committed inventories and curation tables.","curator":"seed_from_sources","timestamp":"2026-10-13T10:44:44Z"}]'
  snapshot_sha256: 6a4902264b9223614ffdbac026bbd511263b74ca752483a0aaeca350b96eb1e2
- evidence_id: support-2309-manual-mobile-H-witness
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/smiles/computed; /records/8/inchi/computed; /records/8/comparisons;
    /records/8/atom_correspondence
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Bounded independent interpretation of the saved tables: {"limits":"Original
    diagnostic empty map, false canonical flags, complete_atom_count_match:false and
    full_graph_identity_established:false are preserved. This witness neither replaces
    those results nor proves natural fixed-graph identity.","method":"Manual explicit
    saved-table correspondence, no molecule parse or graph search","observer_terminal":"a95c6e/0","only_atom_changes":"N21→25
    total H 1→0; O23→26 total H 0→1","only_bond_changes":"SMILES bond21→InChI bond20
    C–N SINGLE→DOUBLE; bond22→21 C=O DOUBLE→SINGLE","preserved":"All mapped adjacency,
    elements, formal charge, isotope, degree, aromatic/ring membership, CIP labels
    and neighbour-relative tetrahedral parity otherwise agree. Added imidic C=N potential
    is unassigned.","smiles_to_inchi_indices":[1,15,8,9,18,23,11,7,10,22,19,12,20,24,14,31,13,17,21,28,29,25,16,26,2,30,27,3,4,5,6,0]}'
  snapshot_sha256: 5696325ae03369015ee813b99d1d51da767e934b2ac887dd9e29f2c27d0405bf
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-231/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json
  accessed_at: '2026-11-03T21:45:24.517787Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: b9cbdcc780498767fa6886409792cfedcdf872922813124081aff76c166efaab
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-231/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json
  accessed_at: '2026-11-03T21:45:49.043451Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 0fd8658ae562b1dfcb46dc521794fb6cd3f0991f7fb047b756120acde0412b7a
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-231/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json
  accessed_at: '2026-11-03T21:46:08.738233Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-231/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json
  accessed_at: '2026-11-03T21:46:42.527754Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-231/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json
  accessed_at: '2026-11-03T21:46:54.303959Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: e760c01e6aac640808752417dde3e98f774512d6edde19a22ad69372e87adaeb
assessments:
- assessment_id: support-2309-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The minted owner naturalproductmech:mibig-f3cb15d2b6 preserves complete
    key PSUMRJNLBIVEFF-RIVHMUOTSA-N from BGC0001910 version 4 compound index 1. Its
    exact retained ChEBI structure join is empty, and PubChem:24778014 is not freshly
    verified. Cyslabdan B and C share the locus but retain distinct complete keys;
    their structures, occurrences and activity claims do not transfer to this owner.
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  evidence_ids:
  - support-2309-grounding-owner
  - support-2309-source-mibig_compounds
  - support-2309-query-chebi_structures
  - support-2309-chemistry
  - support-2309-direct-contexts
  - support-2309-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: PSUMRJNLBIVEFF-RIVHMUOTSA-N; exact retained complete owner key, distinct
      from Cyslabdan B/C.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - support-2309-grounding-owner
    - support-2309-source-mibig_compounds
    - support-2309-query-chebi_structures
    - support-2309-chemistry
    - support-2309-direct-contexts
    - support-2309-companion-boundaries
  - name: grounding_scope
    value: Minted exact MIBiG identity with empty exact ChEBI structure join; natural
      identity/cross-references not freshly verified.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - support-2309-grounding-owner
    - support-2309-source-mibig_compounds
    - support-2309-query-chebi_structures
    - support-2309-chemistry
    - support-2309-direct-contexts
    - support-2309-companion-boundaries
- assessment_id: support-2309-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: 'Both saved forms are neutral C25H41NO5S with 32 heavy atoms and 33 bonds,
    two six-carbon rings, a terminal alkene, an E side-chain alkene, two scaffold
    hydroxyls and a sulfur-linked N-acetylcysteine substituent. Six tetrahedral centres
    are specified. The stored SMILES amide N21–C22(=O23) corresponds locally to decoded
    imidic N25=C16–O26H: nitrogen loses one hydrogen, oxygen gains one, C–N becomes
    double and C=O becomes single. The decoded form adds an unspecified imidic C=N
    stereo possibility. Formula, charge, standard InChI and full key agree, but both
    canonical-SMILES equality flags are false, the original atom map is empty, complete_atom_count_match
    is false and full_graph_identity_established is false. A separately documented
    manual saved-table witness aligns all other adjacency/stereo properties without
    replacing those original results or proving natural fixed-graph identity. The
    retained true flag follows the documented tetrahedral-centre scope, not universal
    geometric completeness.'
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  evidence_ids:
  - support-2309-grounding-owner
  - support-2309-chemistry
  - support-2309-topology
  - support-2309-manual-mobile-H-witness
  - support-2309-diagnostic-acceptance
  - support-2309-structure-schema
  - support-2309-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Six specified tetrahedral centres and an E side-chain alkene; decoded imidic
      form adds an unspecified C=N possibility.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - support-2309-grounding-owner
    - support-2309-chemistry
    - support-2309-topology
    - support-2309-manual-mobile-H-witness
    - support-2309-diagnostic-acceptance
    - support-2309-structure-schema
    - support-2309-stereo-method
  - name: representation_correspondence
    value: Both canonical equality flags false; original map empty and complete_atom_count_match/full_graph_identity_established
      false; separate bounded manual mobile-H witness retained.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - support-2309-grounding-owner
    - support-2309-chemistry
    - support-2309-topology
    - support-2309-manual-mobile-H-witness
    - support-2309-diagnostic-acceptance
    - support-2309-structure-schema
    - support-2309-stereo-method
- assessment_id: support-2309-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: Streptomyces cyslabdanicus NCBITaxon:1470456 remains SOURCE_ASSERTION.
    BGC0001910 version 4 is active, questionable and of unknown completeness, with
    source locus methods unstated and CLUSTER_UNSTATED retained. The later curated
    terminal mechanism does not retroactively upgrade that source-derived locus grade.
    Streptomyces genus-level and S. thermocarboxydus occurrences remain distinct from
    this producer assertion.
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  evidence_ids:
  - support-2309-origin-owner
  - support-2309-source-mibig_compounds
  - support-2309-cached-taxonomy
  - support-2309-source-routes
  - support-2309-direct-contexts
  - support-2309-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: S. cyslabdanicus producer remains separate from genus-level Streptomyces
      and S. thermocarboxydus occurrences.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - support-2309-origin-owner
    - support-2309-source-mibig_compounds
    - support-2309-cached-taxonomy
    - support-2309-source-routes
    - support-2309-direct-contexts
    - support-2309-companion-boundaries
  - name: producer_evidence
    value: SOURCE_ASSERTION for S. cyslabdanicus NCBITaxon:1470456.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - support-2309-origin-owner
    - support-2309-source-mibig_compounds
    - support-2309-cached-taxonomy
    - support-2309-source-routes
    - support-2309-direct-contexts
    - support-2309-companion-boundaries
  - name: locus_evidence
    value: BGC0001910 version 4 active/questionable/unknown; methods unstated and
      CLUSTER_UNSTATED despite a curated terminal mechanism.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - support-2309-origin-owner
    - support-2309-source-mibig_compounds
    - support-2309-cached-taxonomy
    - support-2309-source-routes
    - support-2309-direct-contexts
    - support-2309-companion-boundaries
- assessment_id: support-2309-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: The source COMPOUND_EVIDENCE reference DOI:10.1007/s10295-015-1694-6 differs
    from the occurrence references DOI:10.1038/JA.2008.102, DOI:10.1007/S00253-019-10240-3
    and DOI:10.1038/JA.2016.103. The Mca graph separately retains historical primary
    deletion/heterologous evidence and MITE, UniProt, GenPept and MIBiG database mapping.
    Those roles are not pooled as independent exact-enzyme assays, and no source or
    identifier was freshly retrieved.
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  evidence_ids:
  - support-2309-origin-owner
  - support-2309-occurrence-owner
  - support-2309-source-mibig_compounds
  - support-2309-source-lotus_occurrences
  - support-2309-source-notes
  - support-2309-graph-0
  - support-2309-pathway-0
  - support-2309-history
  dimensions:
  - name: citation_scope
    value: COMPOUND_EVIDENCE DOI differs from occurrence and curated Mca primary/database
      roles; no fresh verification.
    definition: Database provenance, historical primary-experiment support and occurrence
      citations retain distinct roles; no publication independence or fresh source
      access is assumed.
    evidence_ids:
    - support-2309-origin-owner
    - support-2309-occurrence-owner
    - support-2309-source-mibig_compounds
    - support-2309-source-lotus_occurrences
    - support-2309-source-notes
    - support-2309-graph-0
    - support-2309-pathway-0
    - support-2309-history
- assessment_id: support-2309-bioactivity
  area: evidence
  topic: Occurrence and activity
  outcome: supported
  summary: Three exact LOTUS rows preserve Streptomyces NCBITaxon:1883, S. thermocarboxydus
    NCBITaxon:59299 and S. cyslabdanicus NCBITaxon:1470456 occurrence assertions with
    their individual references. There are no written bioactivities or molecular targets
    and the exact saved assay/target joins are empty. The graph concerns biosynthetic
    maturation; it does not establish a therapeutic target or compound efficacy. Neither
    congeners nor a shared locus supply a missing assay.
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  evidence_ids:
  - support-2309-grounding-owner
  - support-2309-occurrence-owner
  - support-2309-assay-owner
  - support-2309-source-routes
  - support-2309-cached-taxonomy
  - support-2309-query-lotus_occurrences
  - support-2309-source-lotus_occurrences
  - support-2309-query-chebi_origins
  - support-2309-query-cyanometdb_occurrences
  - support-2309-query-pubchem_bioassay
  - support-2309-query-bindingdb_targets
  - support-2309-query-antibioticmech_inchikeys
  - support-2309-direct-contexts
  - support-2309-companion-boundaries
  dimensions:
  - name: occurrence_scope
    value: Three literal LOTUS taxon/reference assertions; shared BGC congeners remain
      distinct.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - support-2309-grounding-owner
    - support-2309-occurrence-owner
    - support-2309-assay-owner
    - support-2309-source-routes
    - support-2309-cached-taxonomy
    - support-2309-query-lotus_occurrences
    - support-2309-source-lotus_occurrences
    - support-2309-query-chebi_origins
    - support-2309-query-cyanometdb_occurrences
    - support-2309-query-pubchem_bioassay
    - support-2309-query-bindingdb_targets
    - support-2309-query-antibioticmech_inchikeys
    - support-2309-direct-contexts
    - support-2309-companion-boundaries
  - name: assay_target_scope
    value: No written bioactivity/target and bounded empty exact source joins; biosynthetic
      Mca is not a therapeutic target.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - support-2309-grounding-owner
    - support-2309-occurrence-owner
    - support-2309-assay-owner
    - support-2309-source-routes
    - support-2309-cached-taxonomy
    - support-2309-query-lotus_occurrences
    - support-2309-source-lotus_occurrences
    - support-2309-query-chebi_origins
    - support-2309-query-cyanometdb_occurrences
    - support-2309-query-pubchem_bioassay
    - support-2309-query-bindingdb_targets
    - support-2309-query-antibioticmech_inchikeys
    - support-2309-direct-contexts
    - support-2309-companion-boundaries
- assessment_id: support-2309-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The retained NPClassifier prediction is Terpenoids / Diterpenoids / Labdane
    diterpenoids with glycoside:false, separate from MIBiG TERPENE and compound Diterpenoid/Diterpene
    labels. The complete saved topology supports a C20 scaffold plus a five-carbon
    nitrogen/sulfur-bearing substituent, so total C25 alone is not a contradiction
    of the broad diterpenoid class. No final-product sugar unit is represented; a
    glycosylated upstream mycothiol conjugate in the partial mechanism does not make
    the final owner a glycoside. The class and flag remain versioned predictions.
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  evidence_ids:
  - support-2309-classification-owner
  - support-2309-source-npclassifier
  - support-2309-query-npclassifier
  - support-2309-source-mibig_compounds
  - support-2309-grounding-owner
  - support-2309-topology
  - support-2309-classification-seeder
  - support-2309-pathway-0
  dimensions:
  - name: classification_applicability
    value: Labdane diterpenoids/glycoside:false remain predictions; C20 scaffold plus
      C5 N/S substituent and upstream conjugate scopes are distinct.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - support-2309-classification-owner
    - support-2309-source-npclassifier
    - support-2309-query-npclassifier
    - support-2309-source-mibig_compounds
    - support-2309-grounding-owner
    - support-2309-topology
    - support-2309-classification-seeder
    - support-2309-pathway-0
- assessment_id: support-2309-mechanism
  area: graph
  topic: Mechanism
  outcome: supported
  summary: 'The accepted maintained reader preserves one graph with three nodes and
    two edges, one pathway entry and four history events, with no components or molecular
    targets. The mycothiol S-conjugate precursor remains UNGROUNDED, the Mca enzyme
    is grounded separately and the product is this exact owner. Historical deletion
    in the S. avermitilis SUKA22 heterologous setting carrying the S. cyslabdanicus
    cld cluster supports a downstream amidase requirement after nonenzymatic mycothiol
    addition; it does not by itself demonstrate purified exact-reference turnover.
    The MITE-annotated hydrolysis remains database-scoped. This single terminal step
    is explicitly partial: upstream CldA–D and the nonenzymatic addition are not a
    completed curated pathway.'
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  evidence_ids:
  - support-2309-reader-DATA
  - support-2309-reader-execution
  - support-2309-reader-acceptance
  - support-2309-graph-0
  - support-2309-pathway-0
  - support-2309-history
  - support-2309-grounding-owner
  dimensions: []
- assessment_id: support-2309-proteins
  area: grounding
  topic: Proteins and constructs
  outcome: supported
  summary: Mca UniProt:A0A0H5B8U5 and GenPept:BAR97454.1 are retained as the 379-residue
    reference mapped to the complement of LC064028.1:10784..11923, with MITE:0000107
    and BGC0001910 context. These accession/coordinate and historical functional mappings
    do not constitute a fresh translation, alignment, construct-junction, processing-boundary
    or purified-enzyme proof. The ungrounded precursor is not silently assigned a
    chemical identifier, and the heterologous deletion phenotype is not promoted to
    an organism-independent protein-family claim.
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  evidence_ids:
  - support-2309-reader-DATA
  - support-2309-reader-execution
  - support-2309-reader-acceptance
  - support-2309-graph-0
  - support-2309-pathway-0
  - support-2309-history
  - support-2309-grounding-owner
  dimensions: []
- assessment_id: support-2309-completion
  area: completeness
  topic: Scientific completion
  outcome: unknown
  summary: The complete retained owner, actual canonical intake, saved source payloads/cache
    scope, both saved molecular forms and accepted maintained-reader result have been
    assessed within their local contracts. Full QC, complete OAK authority coverage,
    fresh primary-source/identifier verification and unresolved natural stereochemical
    or construct-specific claims remain unavailable. No source/native-status/history
    edit or new target execution is made; completion remains partial.
  target_ids:
  - naturalproductmech:mibig-f3cb15d2b6
  evidence_ids:
  - support-2309-owner
  - support-2309-capture
  - support-2309-intake
  - support-2309-plan
  - support-2309-intake-acceptance
  - support-2309-inventory-acceptance
  - support-2309-plan-acceptance
  - support-2309-source-notes
  - support-2309-curation-scope
  - support-2309-diagnostic-execution
  - support-2309-diagnostic-acceptance
  - support-2309-native-acceptance
  - support-2309-review-profile
  - support-2309-review-skill
  - support-2309-reader-DATA
  - support-2309-reader-execution
  - support-2309-reader-acceptance
  - support-2309-graph-0
  - support-2309-pathway-0
  - support-2309-history
  - support-2309-grounding-owner
  dimensions:
  - name: review_completion
    value: 'Partial scientific completion: local evidence and accepted reader preservation
      assessed; Full QC/OAK/live primary/identity verification unavailable.'
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - support-2309-owner
    - support-2309-capture
    - support-2309-intake
    - support-2309-plan
    - support-2309-intake-acceptance
    - support-2309-inventory-acceptance
    - support-2309-plan-acceptance
    - support-2309-source-notes
    - support-2309-curation-scope
    - support-2309-diagnostic-execution
    - support-2309-diagnostic-acceptance
    - support-2309-native-acceptance
    - support-2309-review-profile
    - support-2309-review-skill
    - support-2309-reader-DATA
    - support-2309-reader-execution
    - support-2309-reader-acceptance
    - support-2309-graph-0
    - support-2309-pathway-0
    - support-2309-history
    - support-2309-grounding-owner
findings: []
actions: []
limitations:
- All evidence is retained locally. External identifiers, primary publications, taxonomy
  and natural stereochemical assignments were not refreshed under the absolute no-request
  instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original local gates
  and successful stored parses establish only their stated mechanical scope.
- Empty joins concern only exact saved predicates and snapshots. Shared loci, taxa
  and citations do not transfer compound-specific production, activity, mechanism
  or independent-study status.
- Four original undefined-stereo warnings remain global and unassigned to records.
  No additional molecular/YAML parse, source query or target invocation occurred during
  scientific authoring.
- No source record, native curation status or history is edited. Any later correction
  belongs to the maintained owners listed in the accepted canonical intake.
- Accepted maintained-reader equality establishes complete local owner preservation
  only. Protein-family/reaction grounding, historical construct notes and proposed
  steps retain their explicit evidence limits.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete owner/history and actual canonical intake were read; matching source payloads,
  full cached stanzas and companion attribution are retained in the pinned source
  notes.
- 'Support personally read all six saved forms for these three owners: 154 atom rows
  and 166 bond rows plus every scalar, ring, stereo, motif and original mapping/comparison
  field. The Cyslabdan A manual witness is separate from the original failed map.'
- ROOT operated original activation/capture and independently accepted the maintained
  results; Support operated original canonical intakes; Native operated original gates,
  chemistry and all three maintained readers; BGC operated original collector/composer.
  No new target was invoked during these assessments.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-231
```
