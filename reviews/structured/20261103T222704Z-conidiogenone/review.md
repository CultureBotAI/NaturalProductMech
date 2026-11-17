# Local evidence review: conidiogenone

- Review: 20261103T222704Z-conidiogenone
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T21:43:37.776761Z
- Finished UTC: 2026-11-03T22:27:04.855426Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Conidiogenone preserves its exact retained structure, separately graded producer/locus assertions and the complete local PchDS/PchP450 mechanism. PchP450 remains a proposed homolog inference; natural identity, exact protein/construct claims and primary support are not freshly verified. Scientific completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2304; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:189095 | data/natural_products/terpenoids/conidiogenone.yaml | generated | conidiogenone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for conidiogenone | passed | True | CHEBI:189095 | The original offline maintained reader returned the complete expected owner for order 2304: 1 graphs, 6 nodes, 6 edges, 3 pathway entries and 3 history events. Complete owner equality and original terminal exit 0 are ROOT-accepted; no unexpected denial or error occurred. This check establishes local preservation, not independent biological or primary-source verification. |
| strict_ten | passed | True | CHEBI:189095 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:189095 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:189095 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:189095 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:189095 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:189095 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:189095 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:189095 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: CHEBI:189095.

The retained CHEBI:189095 grounding and complete key VXPSMCORCRBNAO-TYVLEIALSA-N agree with the exact MIBiG BGC0002320 version 3 compound-index-1 and three-star ChEBI structure rows. The owner preserves both source concepts rather than substituting a name-only match. NPA017609 and other external cross-references remain retained identifiers, not fresh verification of the natural isolate or every stereochemical assignment.

### Representation

representation: supported. Targets: CHEBI:189095.

Both saved forms are neutral C20H32O2 with 22 heavy atoms, 25 bonds, a 6/5/5/5 ring basis, a ketone and a hydroxyl. All seven potential tetrahedral centres are specified. All ten stored comparisons are true and the original chirality-aware atom correspondence is complete; full_graph_identity_established nevertheless remains false. These tables support local representation agreement and the retained centre-completeness flag, not experimental natural-identity proof. The four global diagnostic warnings are not assigned to this record.

### Origin

provenance: supported. Targets: CHEBI:189095.

Penicillium rubens Wisconsin 54-1255, NCBITaxon:500485, is retained as SOURCE_ASSERTION. BGC0002320 version 3 is active, questionable and of unknown completeness; Heterologous expression supports its separate CLUSTER_DEMONSTRATED locus grade. The occurrences in P. cyclopium and P. aurantiogriseum do not upgrade the Wisconsin producer assertion or establish equivalent strains.

### Citations

evidence: supported. Targets: CHEBI:189095.

PMID:30343633 is ENTRY-level MIBiG database provenance. The curated mechanism separately retains DOI:10.1080/09168451.2018.1536518 as historical primary-experiment support together with UniProt/GenPept database mapping. Occurrence references have their own roles, including a ChEBI reference without an inferred new DOI prefix. Repeated evidence placements are not independent experiments, and none of these publications or accessions was freshly retrieved.

### Occurrence and activity

evidence: supported. Targets: CHEBI:189095.

Four exact LOTUS rows and one ChEBI-origin row account for the five written occurrence assertions: two P. aurantiogriseum placements and three P. cyclopium placements across the two sources. The retained ChEBI definition calls conidiogenone conidiation-inducing; that database wording is not a newly measured assay, dose, target or condition. PubChem, BindingDB and AntibioticMech exact saved joins are empty. No biological inactivity or global lack of activity is inferred.

### Classification

consistency: supported. Targets: CHEBI:189095.

The retained NPClassifier prediction is Terpenoids / Diterpenoids / Cyclopiane diterpenoids with glycoside:false. The full saved C20 polycyclic topology has no sugar unit and is compatible with the broad diterpenoid filing, while the precise model class remains a versioned prediction. MIBiG TERPENE and the ChEBI definition are distinct source assertions; neither computed filing nor carbon count alone establishes biosynthetic provenance.

### Mechanism

graph: supported. Targets: CHEBI:189095.

The accepted maintained reader preserves the complete owner, one inline graph with six nodes and six edges, three pathway entries and three history events, with no component or molecular-target routes. PchDS is represented in the FPP-plus-IPP to GGPP step and the subsequent deoxyconidiogenol step. PchP450 remains proposed:true, and the two putative predicates preserve inference from an assayed PrP450 homolog rather than direct demonstration of this exact PchP450 protein. The three retained pathway products/substrates and their evidence are preserved; the local reader does not establish complete reaction stoichiometry, natural flux or direct activity for every edge.

### Proteins and constructs

grounding: supported. Targets: CHEBI:189095.

The owner distinguishes PchDS B6HFX8 / Pc20g10860 / CAP86415.1 from PchP450 B6HFX9 / Pc20g10870 / CAP86416.1 on AM920435.1. The PchDS C-terminal prenyltransferase and N-terminal cyclase descriptions remain historical domain-function assignments. PchP450 grounding does not turn its homolog-based functional proposal into an exact-protein experiment. No fresh genomic translation, sequence alignment, processing-boundary, construct-junction or purified-enzyme verification occurred.

### Scientific completion

completeness: unknown. Targets: CHEBI:189095.

The complete retained owner, actual canonical intake, saved source payloads/cache scope, both saved molecular forms and accepted maintained-reader result have been assessed within their local contracts. Full QC, complete OAK authority coverage, fresh primary-source/identifier verification and unresolved natural stereochemical or construct-specific claims remain unavailable. No source/native-status/history edit or new target execution is made; completion remains partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2304-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/conidiogenone.yaml; Whole current owner plaintext, including complete curation_history | supports | Complete current owner/history personally read with exact prior reading attribution; no YAML parse or native-status edit. The complete owner is preserved in the accepted capture and maintained result. |
| support-2304-capture | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/3 | supports | Complete actual captured owner and component scope; this owner has no declared component routes. |
| support-2304-intake | /private/tmp/npm-review-work/shared-next-batch231/intakes/2304-inspect-001.json; /status; /repository; /source; /targets | supports | Complete accepted canonical intake, including exact source ownership and maintained implementation dependencies. This is inspection scope, not a scientific verdict. |
| support-2304-grounding-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"chemical_structure":{"smiles":"C[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O","standard_inchi":"InChI=1S/C20H32O2/c1-12-14(21)10-15(22)19(5)7-6-13-16-17(2,3)8-9-18(16,4)11-20(12,13)19/h12-14,16,21H,6-11H2,1-5H3/t12-,13-,14+,16+,18+,19-,20-/m0/s1","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0002320"},"definition":"A diterpenoid with formula C20H32O2. It is isolated from Penicillium cyclopium and exhibits potent conidiation inducing activity.","definition_source":"CHEBI:189095","grounding_status":"EXACT","identifier":"CHEBI:189095","label":"conidiogenone","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-15ed0bd790","source":"MIBIG","source_id":"BGC0002320","source_label":"conidiogenone","source_version":"3"},{"minted_identifier":"naturalproductmech:chebi-3d5ca63698","source":"CHEBI","source_id":"CHEBI:189095","source_label":"conidiogenone","source_version":"3-star"}],"xrefs":["npatlas:NPA017609"]} |
| support-2304-origin-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0002320","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"3","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0002320 entry version 3; citation taken from the entry level","reference":"PMID:30343633"}],"genome_accession":"genbank:AM920435.1","link_evidence_basis":"CLUSTER_DEMONSTRATED","locus_evidence_methods":["Heterologous expression"],"locus_from":2509978,"locus_to":2517120,"organism_label":"Penicillium rubens Wisconsin 54-1255","organism_taxon_id":"NCBITaxon:500485"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0002320","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0002320 entry version 3; citation taken from the entry level","reference":"PMID:30343633"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus evidence: Heterologous expression. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"3","taxon_id":"NCBITaxon:500485","taxon_label":"Penicillium rubens Wisconsin 54-1255"}],"producer_taxon_groups":["FUNGAL"]} |
| support-2304-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"occurrence_taxon_groups":["FUNGAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/S0040-4039(02)01493-4"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q7162856","source":"LOTUS","taxon_id":"NCBITaxon:36655","taxon_label":"Penicillium aurantiogriseum","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1128/EC.1.5.823-829.2002"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q7162856","source":"LOTUS","taxon_id":"NCBITaxon:36655","taxon_label":"Penicillium aurantiogriseum","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"ChEBI compound origin for CHEBI:189095","reference":"10.1016/S0040-4039(02)01493-4"}],"source":"CHEBI","taxon_id":"NCBITaxon:60167","taxon_label":"Penicillium cyclopium","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/S0040-4039(02)01493-4"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q104083838","source":"LOTUS","taxon_id":"NCBITaxon:60167","taxon_label":"Penicillium cyclopium","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1128/EC.1.5.823-829.2002"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q104083838","source":"LOTUS","taxon_id":"NCBITaxon:60167","taxon_label":"Penicillium cyclopium","taxon_source":"NCBITaxon"}]} |
| support-2304-assay-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {} |
| support-2304-classification-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","np_classification":{"class_results":["Cyclopiane diterpenoids"],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Diterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"} |
| support-2304-chemistry | /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json; /records/3/declared_structure; /records/3/smiles/status; /records/3/inchi/status; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons; /records/3/atom_correspondence | supports | Both stored forms parsed. Exact original comparison and correspondence values, preserved without a new parse: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim.","smiles_to_inchi_atom_indices":[0,11,13,9,14,21,18,19,10,17,8,7,16,15,12,5,6,1,2,3,4,20]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"inchi_stereo":{"Atom_Tetrahedral:Specified":7},"smiles_stereo":{"Atom_Tetrahedral:Specified":7}} |
| support-2304-topology | /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json; /records/3/declared_structure; /records/3/smiles/status; /records/3/inchi/status; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons; /records/3/atom_correspondence | supports | Both saved forms are neutral C20H32O2 with 22 heavy atoms, 25 bonds, a 6/5/5/5 ring basis, a ketone and a hydroxyl. All seven potential tetrahedral centres are specified. All ten stored comparisons are true and the original chirality-aware atom correspondence is complete; full_graph_identity_established nevertheless remains false. These tables support local representation agreement and the retained centre-completeness flag, not experimental natural-identity proof. |
| support-2304-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-execution-001.json; Whole original execution receipt | supports | Native operated one original stored-form diagnostic, exit 0, with preserved stdout/stderr and closed environment. The inherited DATA observer literal is not the operator attribution. |
| support-2304-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-chemistry-acceptance-001.json; Whole ROOT chemistry acceptance | supports | ROOT accepts the original 20 stored parses and retains 96 true/four false flags, two empty maps and four global unassigned warnings; it establishes no natural identity or fixed-graph equivalence. |
| support-2304-native-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-native-gates-acceptance-001.json; Whole ROOT gate acceptance and selected queue rows | supports | Five original local gates passed; all_native_gates_passed is false because full QC and complete OAK remain unavailable. Selected queues are follow-up context, not automatic scientific findings. |
| support-2304-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-intake-acceptance-001.json; Whole ROOT intake acceptance | supports | ROOT accepts ten actual one-record intakes, 411 source placements / 68 paths and exact ownership; no scientific verdict follows from intake success. |
| support-2304-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-source-inventory-acceptance-001.json; Whole ROOT source-inventory acceptance | supports | ROOT accepts the one original local inventory and its current input/capture/source joins; complete scientific reading is separately attributed in the notes. |
| support-2304-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-input-plan-acceptance-001.json; Whole ROOT input-plan acceptance | supports | ROOT accepts the exact current plan and preserved source contexts; no scientific verdict or future reader success is inferred. |
| support-2304-source-notes | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete disjoint source/raw-history reading attribution and bounded compound-specific cautions; no pre-intake verdict was asserted. |
| support-2304-curation-scope | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json; /curation | supports | Eight current pinned implemented curation tables were directly opened ignoring ignore rules; 101 exact case-sensitive cohort literals against 93 data rows yielded zero matches within that scope. Reserved decisions.tsv was not consumed. |
| support-2304-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure preserves source representation and standardized-key limitations. stereo_complete describes undefined centres; ComputedClassification is a named/versioned prediction, never a source assertion or admission criterion. |
| support-2304-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | Maintained stereo_complete derives from FindMolChiralCenters and the absence of question-mark centre tags; it is not a blanket all-bond-geometry proof. |
| support-2304-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 974–1065 | supports | Maintained seeding preserves the source structure and named/versioned classifier output while separately retaining BGC and source compound classes. |
| support-2304-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | One-record scientific review requires claim-level evidence and twelve dimensions with truthful partial-completion/unavailable-check limits. |
| support-2304-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill | supports | The review does not edit records; source access is bounded by the overriding no-request instruction. |
| support-2304-plan | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-target-input-plan-001.json; /records/3 | supports | Complete actual owner-specific input map and direct/additional roles. Historical planning language does not claim a reader result; actual reader evidence is linked separately. |
| support-2304-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[{"last_physical_line":2818,"physical_line":2818,"raw_tsv_record":"BGC0002320\t3\tactive\tquestionable\tunknown\tconidiogenone\t1\tC[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O\tInChI=1S/C20H32O2/c1-12-14(21)10-15(22)19(5)7-6-13-16-17(2,3)8-9-18(16,4)11-20(12,13)19/h12-14,16,21H,6-11H2,1-5H3/t12-,13-,14+,16+,18+,19-,20-/m0/s1\tVXPSMCORCRBNAO-TYVLEIALSA-N\ttrue\t\tnpatlas:NPA017609\tNCBITaxon:500485\tPenicillium rubens Wisconsin 54-1255\tterpene\tUnknown\tAM920435.1\t2509978\t2517120\tHeterologous expression\tSOURCE_ASSERTION\tCLUSTER_DEMONSTRATED\tPMID:30343633\tENTRY\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"conidiogenone","database_ids":"npatlas:NPA017609","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"AM920435.1","locus_evidence_methods":"Heterologous expression","locus_from":"2509978","locus_to":"2517120","mibig_accession":"BGC0002320","primary_reference":"PMID:30343633","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"C[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O","standard_inchi":"InChI=1S/C20H32O2/c1-12-14(21)10-15(22)19(5)7-6-13-16-17(2,3)8-9-18(16,4)11-20(12,13)19/h12-14,16,21H,6-11H2,1-5H3/t12-,13-,14+,16+,18+,19-,20-/m0/s1","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:500485","taxon_label":"Penicillium rubens Wisconsin 54-1255"},"row_sha256":"f804fa13dc179660c1c01d46940144af218f65ef25773c413944cecb1e4bce9e"}],"predicate":"exact complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"} |
| support-2304-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2818–2818, row_sha256 f804fa13dc179660c1c01d46940144af218f65ef25773c413944cecb1e4bce9e | supports | Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"conidiogenone","database_ids":"npatlas:NPA017609","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"AM920435.1","locus_evidence_methods":"Heterologous expression","locus_from":"2509978","locus_to":"2517120","mibig_accession":"BGC0002320","primary_reference":"PMID:30343633","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"C[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O","standard_inchi":"InChI=1S/C20H32O2/c1-12-14(21)10-15(22)19(5)7-6-13-16-17(2,3)8-9-18(16,4)11-20(12,13)19/h12-14,16,21H,6-11H2,1-5H3/t12-,13-,14+,16+,18+,19-,20-/m0/s1","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:500485","taxon_label":"Penicillium rubens Wisconsin 54-1255"}] |
| support-2304-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[{"last_physical_line":44099,"physical_line":44099,"raw_tsv_record":"CHEBI:189095\tconidiogenone\tA diterpenoid with formula C20H32O2. It is isolated from Penicillium cyclopium and exhibits potent conidiation inducing activity.\t3\tVXPSMCORCRBNAO-TYVLEIALSA-N\t[H][C@]12[C@@H]3CC[C@@]4(C)C(=O)C[C@@H](O)[C@H](C)[C@@]34C[C@@]1(C)CCC2(C)C\n","row":{"chebi_id":"CHEBI:189095","definition":"A diterpenoid with formula C20H32O2. It is isolated from Penicillium cyclopium and exhibits potent conidiation inducing activity.","name":"conidiogenone","smiles":"[H][C@]12[C@@H]3CC[C@@]4(C)C(=O)C[C@@H](O)[C@H](C)[C@@]34C[C@@]1(C)CCC2(C)C","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","stars":"3"},"row_sha256":"241f6a46d26e084cecabe1aa5ecee6ab2d83517354d47efc51fe0a7410f1ee00"}],"predicate":"exact complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"} |
| support-2304-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line 1; physical lines 44099–44099, row_sha256 241f6a46d26e084cecabe1aa5ecee6ab2d83517354d47efc51fe0a7410f1ee00 | supports | Complete retained physical row payloads, every field: [{"chebi_id":"CHEBI:189095","definition":"A diterpenoid with formula C20H32O2. It is isolated from Penicillium cyclopium and exhibits potent conidiation inducing activity.","name":"conidiogenone","smiles":"[H][C@]12[C@@H]3CC[C@@]4(C)C(=O)C[C@@H](O)[C@H](C)[C@@]34C[C@@]1(C)CCC2(C)C","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","stars":"3"}] |
| support-2304-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[{"last_physical_line":9164,"physical_line":9164,"raw_tsv_record":"VXPSMCORCRBNAO-TYVLEIALSA-N\tPenicillium aurantiogriseum\tNCBITaxon:36655\thttp://www.wikidata.org/entity/Q7162856\t10.1016/S0040-4039(02)01493-4\thttp://www.wikidata.org/entity/Q105298671\n","row":{"organism_name":"Penicillium aurantiogriseum","organism_wikidata":"http://www.wikidata.org/entity/Q7162856","reference_doi":"10.1016/S0040-4039(02)01493-4","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:36655"},"row_sha256":"4b1c52ce899b7dd6693ccb0df390e4071688ec38de4f1ad263c0506d0fe97358"},{"last_physical_line":9165,"physical_line":9165,"raw_tsv_record":"VXPSMCORCRBNAO-TYVLEIALSA-N\tPenicillium aurantiogriseum\tNCBITaxon:36655\thttp://www.wikidata.org/entity/Q7162856\t10.1128/EC.1.5.823-829.2002\thttp://www.wikidata.org/entity/Q105298671\n","row":{"organism_name":"Penicillium aurantiogriseum","organism_wikidata":"http://www.wikidata.org/entity/Q7162856","reference_doi":"10.1128/EC.1.5.823-829.2002","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:36655"},"row_sha256":"f22347354cb4da84e8c0a2e66c7d3f743aa004173d2fd7a245677a38881fd3bf"},{"last_physical_line":9166,"physical_line":9166,"raw_tsv_record":"VXPSMCORCRBNAO-TYVLEIALSA-N\tPenicillium cyclopium\tNCBITaxon:60167\thttp://www.wikidata.org/entity/Q104083838\t10.1016/S0040-4039(02)01493-4\thttp://www.wikidata.org/entity/Q105298671\n","row":{"organism_name":"Penicillium cyclopium","organism_wikidata":"http://www.wikidata.org/entity/Q104083838","reference_doi":"10.1016/S0040-4039(02)01493-4","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:60167"},"row_sha256":"14e510f79269a72f78430be2054327606db6bdcadd764fbe13946d921c816951"},{"last_physical_line":9167,"physical_line":9167,"raw_tsv_record":"VXPSMCORCRBNAO-TYVLEIALSA-N\tPenicillium cyclopium\tNCBITaxon:60167\thttp://www.wikidata.org/entity/Q104083838\t10.1128/EC.1.5.823-829.2002\thttp://www.wikidata.org/entity/Q105298671\n","row":{"organism_name":"Penicillium cyclopium","organism_wikidata":"http://www.wikidata.org/entity/Q104083838","reference_doi":"10.1128/EC.1.5.823-829.2002","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:60167"},"row_sha256":"b12239cb7c0da362d81c614aac77de40040e1d6ba3c3d24f23a61e5dbea046fc"}],"predicate":"exact complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"} |
| support-2304-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 9164–9164, row_sha256 4b1c52ce899b7dd6693ccb0df390e4071688ec38de4f1ad263c0506d0fe97358; physical lines 9165–9165, row_sha256 f22347354cb4da84e8c0a2e66c7d3f743aa004173d2fd7a245677a38881fd3bf; physical lines 9166–9166, row_sha256 14e510f79269a72f78430be2054327606db6bdcadd764fbe13946d921c816951; physical lines 9167–9167, row_sha256 b12239cb7c0da362d81c614aac77de40040e1d6ba3c3d24f23a61e5dbea046fc | supports | Complete retained physical row payloads, every field: [{"organism_name":"Penicillium aurantiogriseum","organism_wikidata":"http://www.wikidata.org/entity/Q7162856","reference_doi":"10.1016/S0040-4039(02)01493-4","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:36655"},{"organism_name":"Penicillium aurantiogriseum","organism_wikidata":"http://www.wikidata.org/entity/Q7162856","reference_doi":"10.1128/EC.1.5.823-829.2002","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:36655"},{"organism_name":"Penicillium cyclopium","organism_wikidata":"http://www.wikidata.org/entity/Q104083838","reference_doi":"10.1016/S0040-4039(02)01493-4","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:60167"},{"organism_name":"Penicillium cyclopium","organism_wikidata":"http://www.wikidata.org/entity/Q104083838","reference_doi":"10.1128/EC.1.5.823-829.2002","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:60167"}] |
| support-2304-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"} |
| support-2304-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[{"last_physical_line":2594,"physical_line":2594,"raw_tsv_record":"VXPSMCORCRBNAO-TYVLEIALSA-N\tC[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O\tTerpenoids\tDiterpenoids\tCyclopiane diterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Cyclopiane diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","superclass_results":"Diterpenoids"},"row_sha256":"6847745fb731f13c328a7a7d376072ed0ae923601700f82a065df43e672bf0aa"}],"predicate":"exact complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"} |
| support-2304-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 2594–2594, row_sha256 6847745fb731f13c328a7a7d376072ed0ae923601700f82a065df43e672bf0aa | supports | Complete retained physical row payloads, every field: [{"class_results":"Cyclopiane diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","superclass_results":"Diterpenoids"}] |
| support-2304-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"} |
| support-2304-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"} |
| support-2304-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"} |
| support-2304-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, including exact predicate, counts, every positive payload or no-match result: {"matches":[{"last_physical_line":17573,"physical_line":17573,"raw_tsv_record":"CHEBI:189095\tPenicillium cyclopium\t60167\t\t\t10.1016/S0040-4039(02)01493-4\t\n","row":{"chebi_id":"CHEBI:189095","comments":"","component_text":"","source_accession":"10.1016/S0040-4039(02)01493-4","species_accession":"60167","species_text":"Penicillium cyclopium","strain_text":""},"row_sha256":"8896c9d5a7ce360d54cc0e7b0139a750f55eb0d0d03e1d590d59af948024d472"}],"predicate":"exact chebi_id from exact full-key structure rows","query":["CHEBI:189095"]} |
| support-2304-source-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Header line 1; physical lines 17573–17573, row_sha256 8896c9d5a7ce360d54cc0e7b0139a750f55eb0d0d03e1d590d59af948024d472 | supports | Complete retained physical row payloads, every field: [{"chebi_id":"CHEBI:189095","comments":"","component_text":"","source_accession":"10.1016/S0040-4039(02)01493-4","species_accession":"60167","species_text":"Penicillium cyclopium","strain_text":""}] |
| support-2304-source-routes | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/source_taxa; /contexts/15/source_scope_inventory/forward_taxon_merge_matches; /contexts/15/source_scope_inventory/nonorganism_matches; /contexts/15/source_scope_inventory/actual_assay_rows; /contexts/15/source_scope_inventory/blank_AID_sentinels; /contexts/15/source_scope_inventory/related_corpus_rows | supports | Complete saved routing fields, without fresh taxonomy or source queries: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:36655","NCBITaxon:500485","NCBITaxon:60167"]} |
| support-2304-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/10; /cached_taxonomy/whole_stanzas/13; /cached_taxonomy/whole_stanzas/26 | supports | Complete retained relevant stanzas; cached labels/synonyms are not fresh external authority: [{"complete_stanza":"[Term]\nid: NCBITaxon:36655\nname: Penicillium aurantiogriseum\n\n","id":"NCBITaxon:36655","physical_line":15999},{"complete_stanza":"[Term]\nid: NCBITaxon:60167\nname: Penicillium cyclopium\nsynonym: \"Penicillium verrucosum var. cyclopium\" EXACT []\n\n","id":"NCBITaxon:60167","physical_line":27608},{"complete_stanza":"[Term]\nid: NCBITaxon:500485\nname: Penicillium rubens Wisconsin 54-1255\n\n","id":"NCBITaxon:500485","physical_line":99323}] |
| support-2304-direct-contexts | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /records/3/direct_companion_paths; /records/3/direct_companion_predicates | supports | Exact direct companion scope and predicates, not transferred compound-specific evidence: {"direct_companion_paths":[],"direct_companion_predicates":[]} |
| support-2304-reader-DATA | /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json; /order; /status; /counts; /raw_owner; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner; /reader_call_count; /denials; /unexpected_denials; /errors; /limitations | supports | Original accepted offline maintained reader. Complete owner equality and exact counts: {"component_graphs":0,"component_history_events":[],"component_refs":0,"curation_history":3,"edges":6,"graphs":1,"inline_graphs":1,"molecular_targets":0,"nodes":6,"pathway_steps":3}. The expected denied-before-action IPv6 capability probe is retained; it is not an outbound request. No unexpected denial or error. Preservation does not independently verify primary experiments or protein identity. |
| support-2304-reader-execution | /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-reader-execution-001.json; Whole original execution receipt | supports | Original single-reader execution, complete saved streams/tool-chain and terminal exit 0; no replay. The command, source/config hashes and process clocks bind the accepted result. |
| support-2304-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-2304-maintained-reader-acceptance-001.json; /status; /order; /DATA; /execution; /verification; /review_check_contract; /limits | supports | ROOT acceptance of this exact original complete-owner reader, with its precise check contract and bounded limits: {"command":"/private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch231/read-selected-mechanism-guarded-001.py 2304 d10634138cd57834c49ec3f0c4070d8bebdd489f1f50f123ab08cc389d2e85a9 66699d97f8ce77d31e74f8685a05c4ad2ce4f4653465502d5dec131dcb22e170 d65dead86417d910f5158628f12930c526dbc5b81750f9197093bfcb644349d8 d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7 007a2056fbbf41f2bf14358fd9b1d850fb78421cc9b32ffb70ae8bc158f858c9","exit_code":0,"exit_source":"original tool terminal and process receipt","name":"Complete offline maintained reader for conidiogenone","required":true,"status":"passed","target_order":2304} |
| support-2304-graph-0 | /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/0 | supports | Complete retained graph, every node, edge, evidence placement and qualified note: {"description":"Penicillium rubens conidiogenone biosynthesis graph for PchDS formation and cyclization of GGPP, followed by the inferred PchP450 oxidation of deoxyconidiogenol to conidiogenone.","edges":[{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8 resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"object":"pchds","predicate":"is prenylated by","subject":"farnesyl_diphosphate"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8 resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"object":"ggpp","predicate":"forms","subject":"pchds"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8 resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"object":"pchds","predicate":"is cyclized by","subject":"ggpp"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8 resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"object":"deoxyconidiogenol","predicate":"forms","subject":"pchds"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina et al. identified PchP450/Pc20g10870 in the Penicillium rubens Wisconsin 54-1255 locus as the P450 homolog corresponding to the experimentally assayed PrP450 conidiogenone synthase.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX9 resolves PchP450 to the reviewed Penicillium rubens Pc20g10870 protein, maps it to EMBL AM920435 protein CAP86416.1, and infers the conidiogenone oxidation function from the assayed Penicillium roqueforti PrP450 homolog.","reference":"https://www.uniprot.org/uniprotkb/B6HFX9","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept CAP86416.1 is the AM920435.1 Pc20g10870 coding sequence cross-referenced from UniProtKB:B6HFX9.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86416.1","retrieved_on":"2026-09-27"}],"notes":"The P. rubens PchP450 function is inferred from the assayed P. roqueforti PrP450 homolog.","object":"pchp450","predicate":"is putatively oxidized by","subject":"deoxyconidiogenol"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina et al. identified PchP450/Pc20g10870 in the Penicillium rubens Wisconsin 54-1255 locus as the P450 homolog corresponding to the experimentally assayed PrP450 conidiogenone synthase.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX9 resolves PchP450 to the reviewed Penicillium rubens Pc20g10870 protein, maps it to EMBL AM920435 protein CAP86416.1, and infers the conidiogenone oxidation function from the assayed Penicillium roqueforti PrP450 homolog.","reference":"https://www.uniprot.org/uniprotkb/B6HFX9","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept CAP86416.1 is the AM920435.1 Pc20g10870 coding sequence cross-referenced from UniProtKB:B6HFX9.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86416.1","retrieved_on":"2026-09-27"}],"notes":"The P. rubens PchP450 function is inferred from the assayed P. roqueforti PrP450 homolog.","object":"conidiogenone","predicate":"putatively forms","subject":"pchp450"}],"graph_id":"conidiogenone-biosynthesis","nodes":[{"grounding_status":"GROUNDED","identifier":"CHEBI:175763","label":"(2E,6E)-farnesyl diphosphate","node_id":"farnesyl_diphosphate","node_type":"PRECURSOR"},{"grounding_status":"GROUNDED","identifier":"UniProtKB:B6HFX8","label":"PchDS","node_id":"pchds","node_type":"ENZYME"},{"grounding_status":"GROUNDED","identifier":"CHEBI:58756","label":"(2E,6E,10E)-geranylgeranyl diphosphate","node_id":"ggpp","node_type":"PRECURSOR"},{"grounding_status":"GROUNDED","identifier":"CHEBI:177897","label":"deoxyconidiogenol","node_id":"deoxyconidiogenol","node_type":"COMPOUND"},{"grounding_status":"GROUNDED","identifier":"UniProtKB:B6HFX9","label":"PchP450","node_id":"pchp450","node_type":"ENZYME"},{"grounding_status":"GROUNDED","identifier":"CHEBI:189095","label":"conidiogenone","node_id":"conidiogenone","node_type":"COMPOUND"}],"scope":"BIOSYNTHESIS"} |
| support-2304-pathway-0 | /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json; /resolved_view/biosynthetic_pathway/0 | supports | Complete retained pathway entry, preserving optional fields and evidence: {"enzyme_id":"UniProtKB:B6HFX8","enzyme_label":"PchDS","evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8 resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"notes":"The C-terminal prenyltransferase domain of PchDS condenses isopentenyl diphosphate with (2E,6E)-farnesyl diphosphate to form (2E,6E,10E)-geranylgeranyl diphosphate in the conidiogenone pathway.","product":"CHEBI:58756","reaction_id":"RHEA:17653","step_number":1,"substrate":"CHEBI:175763"} |
| support-2304-pathway-1 | /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json; /resolved_view/biosynthetic_pathway/1 | supports | Complete retained pathway entry, preserving optional fields and evidence: {"enzyme_id":"UniProtKB:B6HFX8","enzyme_label":"PchDS","evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8 resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"notes":"The N-terminal terpene cyclase domain of PchDS cyclizes (2E,6E,10E)-geranylgeranyl diphosphate to deoxyconidiogenol.","product":"CHEBI:177897","step_number":2,"substrate":"CHEBI:58756"} |
| support-2304-pathway-2 | /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json; /resolved_view/biosynthetic_pathway/2 | supports | Complete retained pathway entry, preserving optional fields and evidence: {"enzyme_id":"UniProtKB:B6HFX9","enzyme_label":"PchP450","evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina et al. identified PchP450/Pc20g10870 in the Penicillium rubens Wisconsin 54-1255 locus as the P450 homolog corresponding to the experimentally assayed PrP450 conidiogenone synthase.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX9 resolves PchP450 to the reviewed Penicillium rubens Pc20g10870 protein, maps it to EMBL AM920435 protein CAP86416.1, and infers the conidiogenone oxidation function from the assayed Penicillium roqueforti PrP450 homolog.","reference":"https://www.uniprot.org/uniprotkb/B6HFX9","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept CAP86416.1 is the AM920435.1 Pc20g10870 coding sequence cross-referenced from UniProtKB:B6HFX9.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86416.1","retrieved_on":"2026-09-27"}],"notes":"PchP450 is the Pc20g10870 P450 homolog proposed to catalyze the deoxyconidiogenol-to-conidiogenone oxidation in the Penicillium rubens AM920435.1 locus; the exact two-round oxidation was assayed with the Penicillium roqueforti PrP450 homolog, not directly with PchP450.","product":"CHEBI:189095","proposed":true,"step_number":3,"substrate":"CHEBI:177897"} |
| support-2304-history | /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json; /resolved_view/curation_history | supports | Complete historical curation events; historical retrieval or sequence notes are not fresh verification: [{"action":"SEEDED_FROM_SOURCES","changes":"Seeded from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-10T05:54:15Z"},{"action":"SEEDED_FROM_SOURCES","changes":"Seeded from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-25T03:03:36Z"},{"action":"RECORD_CURATED","changes":"Added the PchDS/PchP450 conidiogenone biosynthetic pathway and a BIOSYNTHESIS causal graph grounded to UniProtKB accessions B6HFX8 and B6HFX9, with the PchP450 oxidation marked as proposed from the experimentally assayed PrP450 homolog.","curator":"codex","llm_assisted":true,"timestamp":"2026-09-27T03:02:37Z"}] |
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
review_id: 20261103T222704Z-conidiogenone
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: conidiogenone'
started_at: '2026-11-03T21:43:37.776761Z'
finished_at: '2026-11-03T22:27:04.855426Z'
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
summary: Conidiogenone preserves its exact retained structure, separately graded producer/locus
  assertions and the complete local PchDS/PchP450 mechanism. PchP450 remains a proposed
  homolog inference; natural identity, exact protein/construct claims and primary
  support are not freshly verified. Scientific completion is partial.
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
  - path: data/natural_products/terpenoids/conidiogenone.yaml
    sha256: c2bc865dda751821c499599e505d7b948ab4a0dc3531c42c9f2eca5ca0c1e8b1
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
  selection: Campaign path order 2304; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:189095
targets:
- target_id: CHEBI:189095
  path: data/natural_products/terpenoids/conidiogenone.yaml
  label: conidiogenone
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
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/terpenoids/conidiogenone.yaml
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
- name: Complete offline maintained reader for conidiogenone
  status: passed
  required: true
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch231/read-selected-mechanism-guarded-001.py
    2304 d10634138cd57834c49ec3f0c4070d8bebdd489f1f50f123ab08cc389d2e85a9 66699d97f8ce77d31e74f8685a05c4ad2ce4f4653465502d5dec131dcb22e170
    d65dead86417d910f5158628f12930c526dbc5b81750f9197093bfcb644349d8 d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
    007a2056fbbf41f2bf14358fd9b1d850fb78421cc9b32ffb70ae8bc158f858c9
  exit_code: 0
  check_id: maintained-mechanism-reader
  summary: 'The original offline maintained reader returned the complete expected
    owner for order 2304: 1 graphs, 6 nodes, 6 edges, 3 pathway entries and 3 history
    events. Complete owner equality and original terminal exit 0 are ROOT-accepted;
    no unexpected denial or error occurred. This check establishes local preservation,
    not independent biological or primary-source verification.'
  target_ids:
  - CHEBI:189095
  evidence_ids:
  - support-2304-reader-DATA
  - support-2304-reader-execution
  - support-2304-reader-acceptance
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:189095
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
  - CHEBI:189095
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
  - CHEBI:189095
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
  - CHEBI:189095
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
  - CHEBI:189095
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
  - CHEBI:189095
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:189095
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:189095
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2304-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/conidiogenone.yaml
  locator: Whole current owner plaintext, including complete curation_history
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete current owner/history personally read with exact prior reading
    attribution; no YAML parse or native-status edit. The complete owner is preserved
    in the accepted capture and maintained result.
  snapshot_sha256: c2bc865dda751821c499599e505d7b948ab4a0dc3531c42c9f2eca5ca0c1e8b1
- evidence_id: support-2304-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/3
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete actual captured owner and component scope; this owner has no declared
    component routes.
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2304-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/intakes/2304-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete accepted canonical intake, including exact source ownership and
    maintained implementation dependencies. This is inspection scope, not a scientific
    verdict.
  snapshot_sha256: 66699d97f8ce77d31e74f8685a05c4ad2ce4f4653465502d5dec131dcb22e170
- evidence_id: support-2304-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"chemical_structure":{"smiles":"C[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O","standard_inchi":"InChI=1S/C20H32O2/c1-12-14(21)10-15(22)19(5)7-6-13-16-17(2,3)8-9-18(16,4)11-20(12,13)19/h12-14,16,21H,6-11H2,1-5H3/t12-,13-,14+,16+,18+,19-,20-/m0/s1","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0002320"},"definition":"A
    diterpenoid with formula C20H32O2. It is isolated from Penicillium cyclopium and
    exhibits potent conidiation inducing activity.","definition_source":"CHEBI:189095","grounding_status":"EXACT","identifier":"CHEBI:189095","label":"conidiogenone","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-15ed0bd790","source":"MIBIG","source_id":"BGC0002320","source_label":"conidiogenone","source_version":"3"},{"minted_identifier":"naturalproductmech:chebi-3d5ca63698","source":"CHEBI","source_id":"CHEBI:189095","source_label":"conidiogenone","source_version":"3-star"}],"xrefs":["npatlas:NPA017609"]}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2304-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0002320","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"3","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0002320 entry version 3; citation taken from the entry level","reference":"PMID:30343633"}],"genome_accession":"genbank:AM920435.1","link_evidence_basis":"CLUSTER_DEMONSTRATED","locus_evidence_methods":["Heterologous
    expression"],"locus_from":2509978,"locus_to":2517120,"organism_label":"Penicillium
    rubens Wisconsin 54-1255","organism_taxon_id":"NCBITaxon:500485"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0002320","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0002320 entry version 3; citation taken from the entry level","reference":"PMID:30343633"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus
    evidence: Heterologous expression. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED;
    this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"3","taxon_id":"NCBITaxon:500485","taxon_label":"Penicillium
    rubens Wisconsin 54-1255"}],"producer_taxon_groups":["FUNGAL"]}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2304-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"occurrence_taxon_groups":["FUNGAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/S0040-4039(02)01493-4"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q7162856","source":"LOTUS","taxon_id":"NCBITaxon:36655","taxon_label":"Penicillium
    aurantiogriseum","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1128/EC.1.5.823-829.2002"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q7162856","source":"LOTUS","taxon_id":"NCBITaxon:36655","taxon_label":"Penicillium
    aurantiogriseum","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"ChEBI
    compound origin for CHEBI:189095","reference":"10.1016/S0040-4039(02)01493-4"}],"source":"CHEBI","taxon_id":"NCBITaxon:60167","taxon_label":"Penicillium
    cyclopium","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/S0040-4039(02)01493-4"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q104083838","source":"LOTUS","taxon_id":"NCBITaxon:60167","taxon_label":"Penicillium
    cyclopium","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1128/EC.1.5.823-829.2002"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q104083838","source":"LOTUS","taxon_id":"NCBITaxon:60167","taxon_label":"Penicillium
    cyclopium","taxon_source":"NCBITaxon"}]}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2304-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2304-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","np_classification":{"class_results":["Cyclopiane
    diterpenoids"],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Diterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: support-2304-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/declared_structure; /records/3/smiles/status; /records/3/inchi/status;
    /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons;
    /records/3/atom_correspondence
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Both stored forms parsed. Exact original comparison and correspondence
    values, preserved without a new parse: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim.","smiles_to_inchi_atom_indices":[0,11,13,9,14,21,18,19,10,17,8,7,16,15,12,5,6,1,2,3,4,20]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"inchi_stereo":{"Atom_Tetrahedral:Specified":7},"smiles_stereo":{"Atom_Tetrahedral:Specified":7}}'
  snapshot_sha256: 5696325ae03369015ee813b99d1d51da767e934b2ac887dd9e29f2c27d0405bf
- evidence_id: support-2304-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/declared_structure; /records/3/smiles/status; /records/3/inchi/status;
    /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons;
    /records/3/atom_correspondence
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Both saved forms are neutral C20H32O2 with 22 heavy atoms, 25 bonds, a
    6/5/5/5 ring basis, a ketone and a hydroxyl. All seven potential tetrahedral centres
    are specified. All ten stored comparisons are true and the original chirality-aware
    atom correspondence is complete; full_graph_identity_established nevertheless
    remains false. These tables support local representation agreement and the retained
    centre-completeness flag, not experimental natural-identity proof.
  snapshot_sha256: 5696325ae03369015ee813b99d1d51da767e934b2ac887dd9e29f2c27d0405bf
- evidence_id: support-2304-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Native operated one original stored-form diagnostic, exit 0, with preserved
    stdout/stderr and closed environment. The inherited DATA observer literal is not
    the operator attribution.
  snapshot_sha256: 65040543ad69a2d54b0cf784884a78bf49a7bf1c68cdec31272f1ada872be8db
- evidence_id: support-2304-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-chemistry-acceptance-001.json
  locator: Whole ROOT chemistry acceptance
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: ROOT accepts the original 20 stored parses and retains 96 true/four false
    flags, two empty maps and four global unassigned warnings; it establishes no natural
    identity or fixed-graph equivalence.
  snapshot_sha256: 129083683fbfc7528e17bfe7fcd04e7ceb7e44708a11682d024e10f384d5c740
- evidence_id: support-2304-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-native-gates-acceptance-001.json
  locator: Whole ROOT gate acceptance and selected queue rows
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Five original local gates passed; all_native_gates_passed is false because
    full QC and complete OAK remain unavailable. Selected queues are follow-up context,
    not automatic scientific findings.
  snapshot_sha256: b7921dc6afa5d8ce9587a5a097e427772c0b5b739481a22f8e61ce9bcb9e78cc
- evidence_id: support-2304-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-intake-acceptance-001.json
  locator: Whole ROOT intake acceptance
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: ROOT accepts ten actual one-record intakes, 411 source placements / 68
    paths and exact ownership; no scientific verdict follows from intake success.
  snapshot_sha256: af10db4855db731afb28ba6c9d972835e1c1689b3b6089b80d9ed7a76dd1118f
- evidence_id: support-2304-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-source-inventory-acceptance-001.json
  locator: Whole ROOT source-inventory acceptance
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: ROOT accepts the one original local inventory and its current input/capture/source
    joins; complete scientific reading is separately attributed in the notes.
  snapshot_sha256: a50f4decab71502d06fc10d04836ee324c2b09c0fdf118ea5826e7e7c4640d03
- evidence_id: support-2304-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-input-plan-acceptance-001.json
  locator: Whole ROOT input-plan acceptance
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: ROOT accepts the exact current plan and preserved source contexts; no scientific
    verdict or future reader success is inferred.
  snapshot_sha256: 2f7c566f713e12b9b357d9e9c870cb6c05ee90ca30a53c0879a5e5d6a547fa6f
- evidence_id: support-2304-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete disjoint source/raw-history reading attribution and bounded compound-specific
    cautions; no pre-intake verdict was asserted.
  snapshot_sha256: c178e2f5d22e7bf22457f90632cb8bd1b05ce4caf2a993684e4a357a81188afd
- evidence_id: support-2304-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Eight current pinned implemented curation tables were directly opened ignoring
    ignore rules; 101 exact case-sensitive cohort literals against 93 data rows yielded
    zero matches within that scope. Reserved decisions.tsv was not consumed.
  snapshot_sha256: c178e2f5d22e7bf22457f90632cb8bd1b05ce4caf2a993684e4a357a81188afd
- evidence_id: support-2304-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: ChemicalStructure preserves source representation and standardized-key
    limitations. stereo_complete describes undefined centres; ComputedClassification
    is a named/versioned prediction, never a source assertion or admission criterion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2304-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Maintained stereo_complete derives from FindMolChiralCenters and the absence
    of question-mark centre tags; it is not a blanket all-bond-geometry proof.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2304-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 974–1065
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Maintained seeding preserves the source structure and named/versioned classifier
    output while separately retaining BGC and source compound classes.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2304-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: One-record scientific review requires claim-level evidence and twelve dimensions
    with truthful partial-completion/unavailable-check limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2304-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current skill
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: The review does not edit records; source access is bounded by the overriding
    no-request instruction.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: support-2304-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-target-input-plan-001.json
  locator: /records/3
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Complete actual owner-specific input map and direct/additional roles. Historical
    planning language does not claim a reader result; actual reader evidence is linked
    separately.
  snapshot_sha256: 641feb36d59176354fbea2afb95ff2e5d7c1ea3253b71291ca442c15482dab14
- evidence_id: support-2304-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[{"last_physical_line":2818,"physical_line":2818,"raw_tsv_record":"BGC0002320\t3\tactive\tquestionable\tunknown\tconidiogenone\t1\tC[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O\tInChI=1S/C20H32O2/c1-12-14(21)10-15(22)19(5)7-6-13-16-17(2,3)8-9-18(16,4)11-20(12,13)19/h12-14,16,21H,6-11H2,1-5H3/t12-,13-,14+,16+,18+,19-,20-/m0/s1\tVXPSMCORCRBNAO-TYVLEIALSA-N\ttrue\t\tnpatlas:NPA017609\tNCBITaxon:500485\tPenicillium
    rubens Wisconsin 54-1255\tterpene\tUnknown\tAM920435.1\t2509978\t2517120\tHeterologous
    expression\tSOURCE_ASSERTION\tCLUSTER_DEMONSTRATED\tPMID:30343633\tENTRY\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"conidiogenone","database_ids":"npatlas:NPA017609","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"AM920435.1","locus_evidence_methods":"Heterologous
    expression","locus_from":"2509978","locus_to":"2517120","mibig_accession":"BGC0002320","primary_reference":"PMID:30343633","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"C[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O","standard_inchi":"InChI=1S/C20H32O2/c1-12-14(21)10-15(22)19(5)7-6-13-16-17(2,3)8-9-18(16,4)11-20(12,13)19/h12-14,16,21H,6-11H2,1-5H3/t12-,13-,14+,16+,18+,19-,20-/m0/s1","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:500485","taxon_label":"Penicillium
    rubens Wisconsin 54-1255"},"row_sha256":"f804fa13dc179660c1c01d46940144af218f65ef25773c413944cecb1e4bce9e"}],"predicate":"exact
    complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2818–2818, row_sha256 f804fa13dc179660c1c01d46940144af218f65ef25773c413944cecb1e4bce9e
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"conidiogenone","database_ids":"npatlas:NPA017609","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"AM920435.1","locus_evidence_methods":"Heterologous
    expression","locus_from":"2509978","locus_to":"2517120","mibig_accession":"BGC0002320","primary_reference":"PMID:30343633","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"C[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O","standard_inchi":"InChI=1S/C20H32O2/c1-12-14(21)10-15(22)19(5)7-6-13-16-17(2,3)8-9-18(16,4)11-20(12,13)19/h12-14,16,21H,6-11H2,1-5H3/t12-,13-,14+,16+,18+,19-,20-/m0/s1","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:500485","taxon_label":"Penicillium
    rubens Wisconsin 54-1255"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2304-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[{"last_physical_line":44099,"physical_line":44099,"raw_tsv_record":"CHEBI:189095\tconidiogenone\tA
    diterpenoid with formula C20H32O2. It is isolated from Penicillium cyclopium and
    exhibits potent conidiation inducing activity.\t3\tVXPSMCORCRBNAO-TYVLEIALSA-N\t[H][C@]12[C@@H]3CC[C@@]4(C)C(=O)C[C@@H](O)[C@H](C)[C@@]34C[C@@]1(C)CCC2(C)C\n","row":{"chebi_id":"CHEBI:189095","definition":"A
    diterpenoid with formula C20H32O2. It is isolated from Penicillium cyclopium and
    exhibits potent conidiation inducing activity.","name":"conidiogenone","smiles":"[H][C@]12[C@@H]3CC[C@@]4(C)C(=O)C[C@@H](O)[C@H](C)[C@@]34C[C@@]1(C)CCC2(C)C","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","stars":"3"},"row_sha256":"241f6a46d26e084cecabe1aa5ecee6ab2d83517354d47efc51fe0a7410f1ee00"}],"predicate":"exact
    complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-source-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line 1; physical lines 44099–44099, row_sha256 241f6a46d26e084cecabe1aa5ecee6ab2d83517354d47efc51fe0a7410f1ee00
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"chebi_id":"CHEBI:189095","definition":"A
    diterpenoid with formula C20H32O2. It is isolated from Penicillium cyclopium and
    exhibits potent conidiation inducing activity.","name":"conidiogenone","smiles":"[H][C@]12[C@@H]3CC[C@@]4(C)C(=O)C[C@@H](O)[C@H](C)[C@@]34C[C@@]1(C)CCC2(C)C","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","stars":"3"}]'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: support-2304-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[{"last_physical_line":9164,"physical_line":9164,"raw_tsv_record":"VXPSMCORCRBNAO-TYVLEIALSA-N\tPenicillium
    aurantiogriseum\tNCBITaxon:36655\thttp://www.wikidata.org/entity/Q7162856\t10.1016/S0040-4039(02)01493-4\thttp://www.wikidata.org/entity/Q105298671\n","row":{"organism_name":"Penicillium
    aurantiogriseum","organism_wikidata":"http://www.wikidata.org/entity/Q7162856","reference_doi":"10.1016/S0040-4039(02)01493-4","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:36655"},"row_sha256":"4b1c52ce899b7dd6693ccb0df390e4071688ec38de4f1ad263c0506d0fe97358"},{"last_physical_line":9165,"physical_line":9165,"raw_tsv_record":"VXPSMCORCRBNAO-TYVLEIALSA-N\tPenicillium
    aurantiogriseum\tNCBITaxon:36655\thttp://www.wikidata.org/entity/Q7162856\t10.1128/EC.1.5.823-829.2002\thttp://www.wikidata.org/entity/Q105298671\n","row":{"organism_name":"Penicillium
    aurantiogriseum","organism_wikidata":"http://www.wikidata.org/entity/Q7162856","reference_doi":"10.1128/EC.1.5.823-829.2002","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:36655"},"row_sha256":"f22347354cb4da84e8c0a2e66c7d3f743aa004173d2fd7a245677a38881fd3bf"},{"last_physical_line":9166,"physical_line":9166,"raw_tsv_record":"VXPSMCORCRBNAO-TYVLEIALSA-N\tPenicillium
    cyclopium\tNCBITaxon:60167\thttp://www.wikidata.org/entity/Q104083838\t10.1016/S0040-4039(02)01493-4\thttp://www.wikidata.org/entity/Q105298671\n","row":{"organism_name":"Penicillium
    cyclopium","organism_wikidata":"http://www.wikidata.org/entity/Q104083838","reference_doi":"10.1016/S0040-4039(02)01493-4","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:60167"},"row_sha256":"14e510f79269a72f78430be2054327606db6bdcadd764fbe13946d921c816951"},{"last_physical_line":9167,"physical_line":9167,"raw_tsv_record":"VXPSMCORCRBNAO-TYVLEIALSA-N\tPenicillium
    cyclopium\tNCBITaxon:60167\thttp://www.wikidata.org/entity/Q104083838\t10.1128/EC.1.5.823-829.2002\thttp://www.wikidata.org/entity/Q105298671\n","row":{"organism_name":"Penicillium
    cyclopium","organism_wikidata":"http://www.wikidata.org/entity/Q104083838","reference_doi":"10.1128/EC.1.5.823-829.2002","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:60167"},"row_sha256":"b12239cb7c0da362d81c614aac77de40040e1d6ba3c3d24f23a61e5dbea046fc"}],"predicate":"exact
    complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 9164–9164, row_sha256 4b1c52ce899b7dd6693ccb0df390e4071688ec38de4f1ad263c0506d0fe97358;
    physical lines 9165–9165, row_sha256 f22347354cb4da84e8c0a2e66c7d3f743aa004173d2fd7a245677a38881fd3bf;
    physical lines 9166–9166, row_sha256 14e510f79269a72f78430be2054327606db6bdcadd764fbe13946d921c816951;
    physical lines 9167–9167, row_sha256 b12239cb7c0da362d81c614aac77de40040e1d6ba3c3d24f23a61e5dbea046fc
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"organism_name":"Penicillium
    aurantiogriseum","organism_wikidata":"http://www.wikidata.org/entity/Q7162856","reference_doi":"10.1016/S0040-4039(02)01493-4","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:36655"},{"organism_name":"Penicillium
    aurantiogriseum","organism_wikidata":"http://www.wikidata.org/entity/Q7162856","reference_doi":"10.1128/EC.1.5.823-829.2002","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:36655"},{"organism_name":"Penicillium
    cyclopium","organism_wikidata":"http://www.wikidata.org/entity/Q104083838","reference_doi":"10.1016/S0040-4039(02)01493-4","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:60167"},{"organism_name":"Penicillium
    cyclopium","organism_wikidata":"http://www.wikidata.org/entity/Q104083838","reference_doi":"10.1128/EC.1.5.823-829.2002","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q105298671","taxon_id":"NCBITaxon:60167"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2304-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[{"last_physical_line":2594,"physical_line":2594,"raw_tsv_record":"VXPSMCORCRBNAO-TYVLEIALSA-N\tC[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O\tTerpenoids\tDiterpenoids\tCyclopiane
    diterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Cyclopiane
    diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","superclass_results":"Diterpenoids"},"row_sha256":"6847745fb731f13c328a7a7d376072ed0ae923601700f82a065df43e672bf0aa"}],"predicate":"exact
    complete standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 2594–2594, row_sha256 6847745fb731f13c328a7a7d376072ed0ae923601700f82a065df43e672bf0aa
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"class_results":"Cyclopiane
    diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@H]1[C@@H](CC(=O)[C@]2([C@@]13C[C@]4(CCC([C@H]4[C@@H]3CC2)(C)C)C)C)O","standard_inchi_key":"VXPSMCORCRBNAO-TYVLEIALSA-N","superclass_results":"Diterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2304-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"VXPSMCORCRBNAO-TYVLEIALSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained query frame, including exact predicate, counts, every
    positive payload or no-match result: {"matches":[{"last_physical_line":17573,"physical_line":17573,"raw_tsv_record":"CHEBI:189095\tPenicillium
    cyclopium\t60167\t\t\t10.1016/S0040-4039(02)01493-4\t\n","row":{"chebi_id":"CHEBI:189095","comments":"","component_text":"","source_accession":"10.1016/S0040-4039(02)01493-4","species_accession":"60167","species_text":"Penicillium
    cyclopium","strain_text":""},"row_sha256":"8896c9d5a7ce360d54cc0e7b0139a750f55eb0d0d03e1d590d59af948024d472"}],"predicate":"exact
    chebi_id from exact full-key structure rows","query":["CHEBI:189095"]}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-source-chebi_origins
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Header line 1; physical lines 17573–17573, row_sha256 8896c9d5a7ce360d54cc0e7b0139a750f55eb0d0d03e1d590d59af948024d472
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"chebi_id":"CHEBI:189095","comments":"","component_text":"","source_accession":"10.1016/S0040-4039(02)01493-4","species_accession":"60167","species_text":"Penicillium
    cyclopium","strain_text":""}]'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: support-2304-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/source_taxa; /contexts/15/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/15/source_scope_inventory/nonorganism_matches; /contexts/15/source_scope_inventory/actual_assay_rows;
    /contexts/15/source_scope_inventory/blank_AID_sentinels; /contexts/15/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete saved routing fields, without fresh taxonomy or source queries:
    {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:36655","NCBITaxon:500485","NCBITaxon:60167"]}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/10; /cached_taxonomy/whole_stanzas/13;
    /cached_taxonomy/whole_stanzas/26
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained relevant stanzas; cached labels/synonyms are not fresh
    external authority: [{"complete_stanza":"[Term]\nid: NCBITaxon:36655\nname: Penicillium
    aurantiogriseum\n\n","id":"NCBITaxon:36655","physical_line":15999},{"complete_stanza":"[Term]\nid:
    NCBITaxon:60167\nname: Penicillium cyclopium\nsynonym: \"Penicillium verrucosum
    var. cyclopium\" EXACT []\n\n","id":"NCBITaxon:60167","physical_line":27608},{"complete_stanza":"[Term]\nid:
    NCBITaxon:500485\nname: Penicillium rubens Wisconsin 54-1255\n\n","id":"NCBITaxon:500485","physical_line":99323}]'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /records/3/direct_companion_paths; /records/3/direct_companion_predicates
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Exact direct companion scope and predicates, not transferred compound-specific
    evidence: {"direct_companion_paths":[],"direct_companion_predicates":[]}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: support-2304-reader-DATA
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json
  locator: /order; /status; /counts; /raw_owner; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner;
    /reader_call_count; /denials; /unexpected_denials; /errors; /limitations
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Original accepted offline maintained reader. Complete owner equality and
    exact counts: {"component_graphs":0,"component_history_events":[],"component_refs":0,"curation_history":3,"edges":6,"graphs":1,"inline_graphs":1,"molecular_targets":0,"nodes":6,"pathway_steps":3}.
    The expected denied-before-action IPv6 capability probe is retained; it is not
    an outbound request. No unexpected denial or error. Preservation does not independently
    verify primary experiments or protein identity.'
  snapshot_sha256: 881b376c6bbde41484af9f8f942b8185cf368e79443a4be313c381a4e7bc52bb
- evidence_id: support-2304-reader-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-reader-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: Original single-reader execution, complete saved streams/tool-chain and
    terminal exit 0; no replay. The command, source/config hashes and process clocks
    bind the accepted result.
  snapshot_sha256: 9b69abf87444fed8a75356de3eec65a2450d45ff94b63d4b955eff40e139c396
- evidence_id: support-2304-reader-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-2304-maintained-reader-acceptance-001.json
  locator: /status; /order; /DATA; /execution; /verification; /review_check_contract;
    /limits
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'ROOT acceptance of this exact original complete-owner reader, with its
    precise check contract and bounded limits: {"command":"/private/tmp/npm-record-reviews-20261021/.venv/bin/python
    -I -B /private/tmp/npm-review-work/shared-next-batch231/read-selected-mechanism-guarded-001.py
    2304 d10634138cd57834c49ec3f0c4070d8bebdd489f1f50f123ab08cc389d2e85a9 66699d97f8ce77d31e74f8685a05c4ad2ce4f4653465502d5dec131dcb22e170
    d65dead86417d910f5158628f12930c526dbc5b81750f9197093bfcb644349d8 d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
    007a2056fbbf41f2bf14358fd9b1d850fb78421cc9b32ffb70ae8bc158f858c9","exit_code":0,"exit_source":"original
    tool terminal and process receipt","name":"Complete offline maintained reader
    for conidiogenone","required":true,"status":"passed","target_order":2304}'
  snapshot_sha256: 4c71a4e1a87c861fe29892d571518109ae0928a7f1f4d64f7ca27e9d91a1e0b3
- evidence_id: support-2304-graph-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/0
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained graph, every node, edge, evidence placement and qualified
    note: {"description":"Penicillium rubens conidiogenone biosynthesis graph for
    PchDS formation and cyclization of GGPP, followed by the inferred PchP450 oxidation
    of deoxyconidiogenol to conidiogenone.","edges":[{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina
    et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional
    diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor
    deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8
    resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps
    it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced
    from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"object":"pchds","predicate":"is
    prenylated by","subject":"farnesyl_diphosphate"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina
    et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional
    diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor
    deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8
    resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps
    it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced
    from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"object":"ggpp","predicate":"forms","subject":"pchds"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina
    et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional
    diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor
    deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8
    resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps
    it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced
    from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"object":"pchds","predicate":"is
    cyclized by","subject":"ggpp"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina
    et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional
    diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor
    deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8
    resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps
    it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced
    from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"object":"deoxyconidiogenol","predicate":"forms","subject":"pchds"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina
    et al. identified PchP450/Pc20g10870 in the Penicillium rubens Wisconsin 54-1255
    locus as the P450 homolog corresponding to the experimentally assayed PrP450 conidiogenone
    synthase.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX9
    resolves PchP450 to the reviewed Penicillium rubens Pc20g10870 protein, maps it
    to EMBL AM920435 protein CAP86416.1, and infers the conidiogenone oxidation function
    from the assayed Penicillium roqueforti PrP450 homolog.","reference":"https://www.uniprot.org/uniprotkb/B6HFX9","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept CAP86416.1 is the AM920435.1 Pc20g10870 coding sequence cross-referenced
    from UniProtKB:B6HFX9.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86416.1","retrieved_on":"2026-09-27"}],"notes":"The
    P. rubens PchP450 function is inferred from the assayed P. roqueforti PrP450 homolog.","object":"pchp450","predicate":"is
    putatively oxidized by","subject":"deoxyconidiogenol"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina
    et al. identified PchP450/Pc20g10870 in the Penicillium rubens Wisconsin 54-1255
    locus as the P450 homolog corresponding to the experimentally assayed PrP450 conidiogenone
    synthase.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX9
    resolves PchP450 to the reviewed Penicillium rubens Pc20g10870 protein, maps it
    to EMBL AM920435 protein CAP86416.1, and infers the conidiogenone oxidation function
    from the assayed Penicillium roqueforti PrP450 homolog.","reference":"https://www.uniprot.org/uniprotkb/B6HFX9","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept CAP86416.1 is the AM920435.1 Pc20g10870 coding sequence cross-referenced
    from UniProtKB:B6HFX9.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86416.1","retrieved_on":"2026-09-27"}],"notes":"The
    P. rubens PchP450 function is inferred from the assayed P. roqueforti PrP450 homolog.","object":"conidiogenone","predicate":"putatively
    forms","subject":"pchp450"}],"graph_id":"conidiogenone-biosynthesis","nodes":[{"grounding_status":"GROUNDED","identifier":"CHEBI:175763","label":"(2E,6E)-farnesyl
    diphosphate","node_id":"farnesyl_diphosphate","node_type":"PRECURSOR"},{"grounding_status":"GROUNDED","identifier":"UniProtKB:B6HFX8","label":"PchDS","node_id":"pchds","node_type":"ENZYME"},{"grounding_status":"GROUNDED","identifier":"CHEBI:58756","label":"(2E,6E,10E)-geranylgeranyl
    diphosphate","node_id":"ggpp","node_type":"PRECURSOR"},{"grounding_status":"GROUNDED","identifier":"CHEBI:177897","label":"deoxyconidiogenol","node_id":"deoxyconidiogenol","node_type":"COMPOUND"},{"grounding_status":"GROUNDED","identifier":"UniProtKB:B6HFX9","label":"PchP450","node_id":"pchp450","node_type":"ENZYME"},{"grounding_status":"GROUNDED","identifier":"CHEBI:189095","label":"conidiogenone","node_id":"conidiogenone","node_type":"COMPOUND"}],"scope":"BIOSYNTHESIS"}'
  snapshot_sha256: 881b376c6bbde41484af9f8f942b8185cf368e79443a4be313c381a4e7bc52bb
- evidence_id: support-2304-pathway-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json
  locator: /resolved_view/biosynthetic_pathway/0
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained pathway entry, preserving optional fields and evidence:
    {"enzyme_id":"UniProtKB:B6HFX8","enzyme_label":"PchDS","evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina
    et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional
    diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor
    deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8
    resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps
    it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced
    from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"notes":"The
    C-terminal prenyltransferase domain of PchDS condenses isopentenyl diphosphate
    with (2E,6E)-farnesyl diphosphate to form (2E,6E,10E)-geranylgeranyl diphosphate
    in the conidiogenone pathway.","product":"CHEBI:58756","reaction_id":"RHEA:17653","step_number":1,"substrate":"CHEBI:175763"}'
  snapshot_sha256: 881b376c6bbde41484af9f8f942b8185cf368e79443a4be313c381a4e7bc52bb
- evidence_id: support-2304-pathway-1
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json
  locator: /resolved_view/biosynthetic_pathway/1
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained pathway entry, preserving optional fields and evidence:
    {"enzyme_id":"UniProtKB:B6HFX8","enzyme_label":"PchDS","evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina
    et al. experimentally characterized the Penicillium rubens Wisconsin 54-1255 bifunctional
    diterpene synthase PchDS/Pc20g10860 that produces the conidiogenone precursor
    deoxyconidiogenol.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX8
    resolves PchDS to the reviewed Penicillium rubens Pc20g10860 protein and maps
    it to EMBL AM920435 protein CAP86415.1.","reference":"https://www.uniprot.org/uniprotkb/B6HFX8","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept CAP86415.1 is the AM920435.1 Pc20g10860 coding sequence cross-referenced
    from UniProtKB:B6HFX8.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86415.1","retrieved_on":"2026-09-27"}],"notes":"The
    N-terminal terpene cyclase domain of PchDS cyclizes (2E,6E,10E)-geranylgeranyl
    diphosphate to deoxyconidiogenol.","product":"CHEBI:177897","step_number":2,"substrate":"CHEBI:58756"}'
  snapshot_sha256: 881b376c6bbde41484af9f8f942b8185cf368e79443a4be313c381a4e7bc52bb
- evidence_id: support-2304-pathway-2
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json
  locator: /resolved_view/biosynthetic_pathway/2
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete retained pathway entry, preserving optional fields and evidence:
    {"enzyme_id":"UniProtKB:B6HFX9","enzyme_label":"PchP450","evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Shiina
    et al. identified PchP450/Pc20g10870 in the Penicillium rubens Wisconsin 54-1255
    locus as the P450 homolog corresponding to the experimentally assayed PrP450 conidiogenone
    synthase.","reference":"DOI:10.1080/09168451.2018.1536518"},{"evidence_type":"DATABASE_ASSERTION","notes":"UniProtKB:B6HFX9
    resolves PchP450 to the reviewed Penicillium rubens Pc20g10870 protein, maps it
    to EMBL AM920435 protein CAP86416.1, and infers the conidiogenone oxidation function
    from the assayed Penicillium roqueforti PrP450 homolog.","reference":"https://www.uniprot.org/uniprotkb/B6HFX9","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept CAP86416.1 is the AM920435.1 Pc20g10870 coding sequence cross-referenced
    from UniProtKB:B6HFX9.","reference":"https://www.ncbi.nlm.nih.gov/protein/CAP86416.1","retrieved_on":"2026-09-27"}],"notes":"PchP450
    is the Pc20g10870 P450 homolog proposed to catalyze the deoxyconidiogenol-to-conidiogenone
    oxidation in the Penicillium rubens AM920435.1 locus; the exact two-round oxidation
    was assayed with the Penicillium roqueforti PrP450 homolog, not directly with
    PchP450.","product":"CHEBI:189095","proposed":true,"step_number":3,"substrate":"CHEBI:177897"}'
  snapshot_sha256: 881b376c6bbde41484af9f8f942b8185cf368e79443a4be313c381a4e7bc52bb
- evidence_id: support-2304-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/native-current231-conidiogenone-maintained-reader-DATA-001.json
  locator: /resolved_view/curation_history
  accessed_at: '2026-11-03T22:23:00.023197Z'
  support: supports
  summary: 'Complete historical curation events; historical retrieval or sequence
    notes are not fresh verification: [{"action":"SEEDED_FROM_SOURCES","changes":"Seeded
    from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-10T05:54:15Z"},{"action":"SEEDED_FROM_SOURCES","changes":"Seeded
    from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-25T03:03:36Z"},{"action":"RECORD_CURATED","changes":"Added
    the PchDS/PchP450 conidiogenone biosynthetic pathway and a BIOSYNTHESIS causal
    graph grounded to UniProtKB accessions B6HFX8 and B6HFX9, with the PchP450 oxidation
    marked as proposed from the experimentally assayed PrP450 homolog.","curator":"codex","llm_assisted":true,"timestamp":"2026-09-27T03:02:37Z"}]'
  snapshot_sha256: 881b376c6bbde41484af9f8f942b8185cf368e79443a4be313c381a4e7bc52bb
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
- assessment_id: support-2304-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The retained CHEBI:189095 grounding and complete key VXPSMCORCRBNAO-TYVLEIALSA-N
    agree with the exact MIBiG BGC0002320 version 3 compound-index-1 and three-star
    ChEBI structure rows. The owner preserves both source concepts rather than substituting
    a name-only match. NPA017609 and other external cross-references remain retained
    identifiers, not fresh verification of the natural isolate or every stereochemical
    assignment.
  target_ids:
  - CHEBI:189095
  evidence_ids:
  - support-2304-grounding-owner
  - support-2304-source-mibig_compounds
  - support-2304-query-chebi_structures
  - support-2304-source-chebi_structures
  - support-2304-chemistry
  - support-2304-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: VXPSMCORCRBNAO-TYVLEIALSA-N; exact full retained MIBiG/ChEBI structure
      key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - support-2304-grounding-owner
    - support-2304-source-mibig_compounds
    - support-2304-query-chebi_structures
    - support-2304-source-chebi_structures
    - support-2304-chemistry
    - support-2304-direct-contexts
  - name: grounding_scope
    value: CHEBI:189095 exact retained structure join; natural isolate and external
      accessions are not freshly verified.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - support-2304-grounding-owner
    - support-2304-source-mibig_compounds
    - support-2304-query-chebi_structures
    - support-2304-source-chebi_structures
    - support-2304-chemistry
    - support-2304-direct-contexts
- assessment_id: support-2304-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both saved forms are neutral C20H32O2 with 22 heavy atoms, 25 bonds, a
    6/5/5/5 ring basis, a ketone and a hydroxyl. All seven potential tetrahedral centres
    are specified. All ten stored comparisons are true and the original chirality-aware
    atom correspondence is complete; full_graph_identity_established nevertheless
    remains false. These tables support local representation agreement and the retained
    centre-completeness flag, not experimental natural-identity proof. The four global
    diagnostic warnings are not assigned to this record.
  target_ids:
  - CHEBI:189095
  evidence_ids:
  - support-2304-grounding-owner
  - support-2304-chemistry
  - support-2304-topology
  - support-2304-diagnostic-acceptance
  - support-2304-structure-schema
  - support-2304-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Seven specified tetrahedral centres in both saved forms; no experimental
      stereochemical reassignment.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - support-2304-grounding-owner
    - support-2304-chemistry
    - support-2304-topology
    - support-2304-diagnostic-acceptance
    - support-2304-structure-schema
    - support-2304-stereo-method
  - name: representation_correspondence
    value: All ten comparisons true and complete original atom correspondence; full_graph_identity_established
      remains false.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - support-2304-grounding-owner
    - support-2304-chemistry
    - support-2304-topology
    - support-2304-diagnostic-acceptance
    - support-2304-structure-schema
    - support-2304-stereo-method
- assessment_id: support-2304-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: Penicillium rubens Wisconsin 54-1255, NCBITaxon:500485, is retained as
    SOURCE_ASSERTION. BGC0002320 version 3 is active, questionable and of unknown
    completeness; Heterologous expression supports its separate CLUSTER_DEMONSTRATED
    locus grade. The occurrences in P. cyclopium and P. aurantiogriseum do not upgrade
    the Wisconsin producer assertion or establish equivalent strains.
  target_ids:
  - CHEBI:189095
  evidence_ids:
  - support-2304-origin-owner
  - support-2304-source-mibig_compounds
  - support-2304-cached-taxonomy
  - support-2304-source-routes
  - support-2304-direct-contexts
  dimensions:
  - name: taxon_scope
    value: Wisconsin 54-1255 producer assertion remains distinct from P. cyclopium
      and P. aurantiogriseum occurrences.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - support-2304-origin-owner
    - support-2304-source-mibig_compounds
    - support-2304-cached-taxonomy
    - support-2304-source-routes
    - support-2304-direct-contexts
  - name: producer_evidence
    value: SOURCE_ASSERTION for Penicillium rubens Wisconsin 54-1255, NCBITaxon:500485.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - support-2304-origin-owner
    - support-2304-source-mibig_compounds
    - support-2304-cached-taxonomy
    - support-2304-source-routes
    - support-2304-direct-contexts
  - name: locus_evidence
    value: BGC0002320 version 3, active/questionable/unknown; Heterologous expression;
      CLUSTER_DEMONSTRATED.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - support-2304-origin-owner
    - support-2304-source-mibig_compounds
    - support-2304-cached-taxonomy
    - support-2304-source-routes
    - support-2304-direct-contexts
- assessment_id: support-2304-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: PMID:30343633 is ENTRY-level MIBiG database provenance. The curated mechanism
    separately retains DOI:10.1080/09168451.2018.1536518 as historical primary-experiment
    support together with UniProt/GenPept database mapping. Occurrence references
    have their own roles, including a ChEBI reference without an inferred new DOI
    prefix. Repeated evidence placements are not independent experiments, and none
    of these publications or accessions was freshly retrieved.
  target_ids:
  - CHEBI:189095
  evidence_ids:
  - support-2304-origin-owner
  - support-2304-occurrence-owner
  - support-2304-source-mibig_compounds
  - support-2304-source-lotus_occurrences
  - support-2304-source-chebi_origins
  - support-2304-source-notes
  - support-2304-graph-0
  - support-2304-pathway-0
  - support-2304-pathway-1
  - support-2304-pathway-2
  - support-2304-history
  dimensions:
  - name: citation_scope
    value: ENTRY PMID:30343633, separate curated primary/database mechanism references
      and occurrence references; no fresh retrieval.
    definition: Database provenance, historical primary-experiment support and occurrence
      citations retain distinct roles; no publication independence or fresh source
      access is assumed.
    evidence_ids:
    - support-2304-origin-owner
    - support-2304-occurrence-owner
    - support-2304-source-mibig_compounds
    - support-2304-source-lotus_occurrences
    - support-2304-source-chebi_origins
    - support-2304-source-notes
    - support-2304-graph-0
    - support-2304-pathway-0
    - support-2304-pathway-1
    - support-2304-pathway-2
    - support-2304-history
- assessment_id: support-2304-bioactivity
  area: evidence
  topic: Occurrence and activity
  outcome: supported
  summary: 'Four exact LOTUS rows and one ChEBI-origin row account for the five written
    occurrence assertions: two P. aurantiogriseum placements and three P. cyclopium
    placements across the two sources. The retained ChEBI definition calls conidiogenone
    conidiation-inducing; that database wording is not a newly measured assay, dose,
    target or condition. PubChem, BindingDB and AntibioticMech exact saved joins are
    empty. No biological inactivity or global lack of activity is inferred.'
  target_ids:
  - CHEBI:189095
  evidence_ids:
  - support-2304-grounding-owner
  - support-2304-occurrence-owner
  - support-2304-assay-owner
  - support-2304-source-routes
  - support-2304-cached-taxonomy
  - support-2304-query-lotus_occurrences
  - support-2304-source-lotus_occurrences
  - support-2304-query-chebi_origins
  - support-2304-source-chebi_origins
  - support-2304-query-cyanometdb_occurrences
  - support-2304-query-pubchem_bioassay
  - support-2304-query-bindingdb_targets
  - support-2304-query-antibioticmech_inchikeys
  - support-2304-direct-contexts
  dimensions:
  - name: occurrence_scope
    value: Four LOTUS plus one ChEBI-origin placement, five written assertions; not
      five independent experiments.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - support-2304-grounding-owner
    - support-2304-occurrence-owner
    - support-2304-assay-owner
    - support-2304-source-routes
    - support-2304-cached-taxonomy
    - support-2304-query-lotus_occurrences
    - support-2304-source-lotus_occurrences
    - support-2304-query-chebi_origins
    - support-2304-source-chebi_origins
    - support-2304-query-cyanometdb_occurrences
    - support-2304-query-pubchem_bioassay
    - support-2304-query-bindingdb_targets
    - support-2304-query-antibioticmech_inchikeys
    - support-2304-direct-contexts
  - name: assay_target_scope
    value: Definition-level conidiation wording only; exact saved assay/target joins
      empty, no inactivity inference.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - support-2304-grounding-owner
    - support-2304-occurrence-owner
    - support-2304-assay-owner
    - support-2304-source-routes
    - support-2304-cached-taxonomy
    - support-2304-query-lotus_occurrences
    - support-2304-source-lotus_occurrences
    - support-2304-query-chebi_origins
    - support-2304-source-chebi_origins
    - support-2304-query-cyanometdb_occurrences
    - support-2304-query-pubchem_bioassay
    - support-2304-query-bindingdb_targets
    - support-2304-query-antibioticmech_inchikeys
    - support-2304-direct-contexts
- assessment_id: support-2304-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The retained NPClassifier prediction is Terpenoids / Diterpenoids / Cyclopiane
    diterpenoids with glycoside:false. The full saved C20 polycyclic topology has
    no sugar unit and is compatible with the broad diterpenoid filing, while the precise
    model class remains a versioned prediction. MIBiG TERPENE and the ChEBI definition
    are distinct source assertions; neither computed filing nor carbon count alone
    establishes biosynthetic provenance.
  target_ids:
  - CHEBI:189095
  evidence_ids:
  - support-2304-classification-owner
  - support-2304-source-npclassifier
  - support-2304-query-npclassifier
  - support-2304-source-mibig_compounds
  - support-2304-grounding-owner
  - support-2304-topology
  - support-2304-classification-seeder
  dimensions:
  - name: classification_applicability
    value: Cyclopiane diterpenoids and glycoside:false remain versioned predictions
      compatible with the saved broad topology.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - support-2304-classification-owner
    - support-2304-source-npclassifier
    - support-2304-query-npclassifier
    - support-2304-source-mibig_compounds
    - support-2304-grounding-owner
    - support-2304-topology
    - support-2304-classification-seeder
- assessment_id: support-2304-mechanism
  area: graph
  topic: Mechanism
  outcome: supported
  summary: The accepted maintained reader preserves the complete owner, one inline
    graph with six nodes and six edges, three pathway entries and three history events,
    with no component or molecular-target routes. PchDS is represented in the FPP-plus-IPP
    to GGPP step and the subsequent deoxyconidiogenol step. PchP450 remains proposed:true,
    and the two putative predicates preserve inference from an assayed PrP450 homolog
    rather than direct demonstration of this exact PchP450 protein. The three retained
    pathway products/substrates and their evidence are preserved; the local reader
    does not establish complete reaction stoichiometry, natural flux or direct activity
    for every edge.
  target_ids:
  - CHEBI:189095
  evidence_ids:
  - support-2304-reader-DATA
  - support-2304-reader-execution
  - support-2304-reader-acceptance
  - support-2304-graph-0
  - support-2304-pathway-0
  - support-2304-pathway-1
  - support-2304-pathway-2
  - support-2304-history
  - support-2304-grounding-owner
  dimensions: []
- assessment_id: support-2304-proteins
  area: grounding
  topic: Proteins and constructs
  outcome: supported
  summary: The owner distinguishes PchDS B6HFX8 / Pc20g10860 / CAP86415.1 from PchP450
    B6HFX9 / Pc20g10870 / CAP86416.1 on AM920435.1. The PchDS C-terminal prenyltransferase
    and N-terminal cyclase descriptions remain historical domain-function assignments.
    PchP450 grounding does not turn its homolog-based functional proposal into an
    exact-protein experiment. No fresh genomic translation, sequence alignment, processing-boundary,
    construct-junction or purified-enzyme verification occurred.
  target_ids:
  - CHEBI:189095
  evidence_ids:
  - support-2304-reader-DATA
  - support-2304-reader-execution
  - support-2304-reader-acceptance
  - support-2304-graph-0
  - support-2304-pathway-0
  - support-2304-pathway-1
  - support-2304-pathway-2
  - support-2304-history
  - support-2304-grounding-owner
  dimensions: []
- assessment_id: support-2304-completion
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
  - CHEBI:189095
  evidence_ids:
  - support-2304-owner
  - support-2304-capture
  - support-2304-intake
  - support-2304-plan
  - support-2304-intake-acceptance
  - support-2304-inventory-acceptance
  - support-2304-plan-acceptance
  - support-2304-source-notes
  - support-2304-curation-scope
  - support-2304-diagnostic-execution
  - support-2304-diagnostic-acceptance
  - support-2304-native-acceptance
  - support-2304-review-profile
  - support-2304-review-skill
  - support-2304-reader-DATA
  - support-2304-reader-execution
  - support-2304-reader-acceptance
  - support-2304-graph-0
  - support-2304-pathway-0
  - support-2304-pathway-1
  - support-2304-pathway-2
  - support-2304-history
  - support-2304-grounding-owner
  dimensions:
  - name: review_completion
    value: 'Partial scientific completion: local evidence and accepted reader preservation
      assessed; Full QC/OAK/live primary/identity verification unavailable.'
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - support-2304-owner
    - support-2304-capture
    - support-2304-intake
    - support-2304-plan
    - support-2304-intake-acceptance
    - support-2304-inventory-acceptance
    - support-2304-plan-acceptance
    - support-2304-source-notes
    - support-2304-curation-scope
    - support-2304-diagnostic-execution
    - support-2304-diagnostic-acceptance
    - support-2304-native-acceptance
    - support-2304-review-profile
    - support-2304-review-skill
    - support-2304-reader-DATA
    - support-2304-reader-execution
    - support-2304-reader-acceptance
    - support-2304-graph-0
    - support-2304-pathway-0
    - support-2304-pathway-1
    - support-2304-pathway-2
    - support-2304-history
    - support-2304-grounding-owner
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
