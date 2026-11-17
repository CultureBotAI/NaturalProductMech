# Local evidence review: legioliulin

- Review: 20261103T113308Z-legioliulin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T11:08:47.848002Z
- Finished UTC: 2026-11-03T11:33:08.348727Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

legioliulin: qualified partial review of exact retained structure, source grades, taxonomy and saved molecular topology.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2207; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156300 | data/natural_products/shikimates_and_phenylpropanoids/legioliulin.yaml | generated | legioliulin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:156300 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:156300 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:156300 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:156300 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:156300 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:156300 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:156300 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:156300 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding scope

identity: supported. Targets: CHEBI:156300.

Legioliulin has exact retained MIBiG and three-star ChEBI grounding to CHEBI:156300 through IFFMOWIJJAFQJN-HINBXAKRSA-N. The paired computations give neutral C19H14O3. The ChEBI isocoumarin and (1E,3E)-phenylbutadienyl definition is structurally compatible with the stored molecule; the blue-white autofluorescence statement remains a retained database definition, not a newly reproduced observation.

### Paired molecular representations and stereochemical limits

representation: supported. Targets: CHEBI:156300.

Both forms have 22 atoms and 24 bonds, all ten comparisons true and a complete 22-atom correspondence; independent full graph and natural identity remain unproved. The two side-chain double bonds are explicitly STEREOE in the saved bond tables (SMILES bonds 7 and 9), with two specified potential-double entries and no unspecified tetrahedral centre. This supports the stored E,E representation rather than assigning geometry solely from the potential-stereo word Trans. The literal stereo_complete:true has the narrower maintained atom-centre derivation.

### Producer, occurrence and locus evidence grades

provenance: supported. Targets: CHEBI:156300.

MIBiG BGC0000180 version 5 retains Legionella parisiensis NCBITaxon:45071 at BGC_CHARACTERIZED and the locus at CLUSTER_DEMONSTRATED, based on knockout studies and expression correlated with production. The source entry is questionable/complete; KM222819.1 coordinates 4550–31415 preserve its locus scope without elevating it to a complete pathway. Four written occurrence assertions represent two taxa and two source types. Cache NCBITaxon:463 names Fluoribacter dumoffii and explicitly lists Legionella dumoffii as an exact synonym, so the historical definition and current occurrence label are compatible within this cache. L. parisiensis is a distinct taxon, not a synonym of dumoffii.

### Citation placement and historical verification scope

evidence: supported. Targets: CHEBI:156300.

PMID:23821465 is the MIBiG ENTRY citation and also appears in the ChEBI L. parisiensis origin; its related LOTUS DOI is 10.1002/CBIC.201300373. The dumoffii occurrence sources retain DOI:10.1016/J.BBRC.2004.08.180 and PMID:15381093. Their preservation does not establish publication independence or fresh primary verification. The current owner already separates occurrence and producer claims and explicitly cautions about shared publications.

### Occurrence, assay and companion boundaries

scope: supported. Targets: CHEBI:156300.

Two LOTUS and two ChEBI-origin rows support occurrence claims for Fluoribacter dumoffii and Legionella parisiensis; they do not turn all occurring organisms into experimentally demonstrated producers. Exact selected PubChem, BindingDB, AntibioticMech and CyanometDB joins are empty, and no direct companions are admitted. The retained fluorophore definition is not substituted for a quantitative pharmacology or target assay, and the empty assay scope does not establish inactivity.

### Computed classification and full-table topology limits

other: supported. Targets: CHEBI:156300.

The complete graph contains a benzene-fused six-member oxygen heterocycle bearing C3=O4 and aromatic ring oxygen O5, plus a terminal phenyl ring joined by an E,E conjugated diene. The generic SINGLE-bond ester scan does not report the aromaticized isocoumarin ring; this is a motif-helper limitation, not absence of the ring carbonyl/oxygen topology. No sugar residue is present. NPClassifier Coumarins/Isocoumarins and false glycoside status describe the retained prediction; the MIBiG PKS class is a separate biosynthetic classification.

### Partial scientific completion and maintained ownership

completeness: supported. Targets: CHEBI:156300.

This is a qualified partial review with stronger imported locus/producer evidence than a source assertion, but no complete biosynthetic pathway, molecular targets, causal graphs or components are stored. The biosynthesis queue remains a completeness lead, not proof that a pathway was reconstructed here. No maintained reader applies. Five local gates passed; full QC, OAK coverage and fresh publication verification remain unavailable. Maintained owner paths in the intake define any future correction route.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2207-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/legioliulin.yaml; Complete raw owner, lines 1-135. | supports | Complete selected owner and all 3 history events personally read; exact current bytes retained. |
| support-2207-capture | /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json; /records/6 | supports | Complete captured owner and literal mechanism-root absence; capture is the authoritative saved owner reading, not scientific verification. |
| support-2207-intake | /private/tmp/npm-review-work/shared-next-batch221/intakes/2207-inspect-001.json; /targets; /source | supports | Complete current intake and all source input placements personally read; maintained ownership and exact target scope retained. |
| support-2207-intake-ready | /private/tmp/npm-review-work/shared-next-batch221/root-intake-ready-001.json; /status; /records; /source_placements; /unique_source_paths; /mechanism_owner_orders | supports | ROOT accepted the ten original intakes with 396 placements across 57 unique paths and no selected mechanism readers. |
| support-2207-source-plan | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6 | supports | Complete retained selected source frames, direct predicates and exact intake input map; source collection is local and does not verify publications. |
| support-2207-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch221/root-target-input-plan-acceptance-001.json; /status; /plan; /source_placements; /unique_source_paths; /per_order_counts | supports | ROOT accepted the exact target-input plan and 396/57 maps. |
| support-2207-source-notes | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-source-scope-notes-001.json; /reading; /cautions | supports | Explicit author/team reading attribution and bounded scientific source cautions; no fresh source retrieval. |
| support-2207-curation-scope | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-source-scope-notes-001.json; /curation | supports | BGC performed the admitted eight-table 79-token scan with zero hits; this is attributed bounded curation scope, not universal absence. |
| support-2207-chemistry | /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-DATA-001.json; /records/6/declared_structure; /records/6/smiles; /records/6/inchi; /records/6/comparisons; /records/6/atom_correspondence | supports | Both complete saved forms and all atom/bond/stereo/motif fields personally read. All ten comparisons true; complete atom map; full_graph_identity_established:false retained. |
| support-2207-topology | /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed; /records/6/inchi/computed | supports | Complete paired atom/bond/neighborhood, charge/isotope/aromatic, ring, stereo and motif tables support the bounded topology interpretation in assessment A6; the stored graph is not a natural-identity proof. |
| support-2207-chemistry-execution | /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-execution-001.json; /argv; /exit_code; /stdout; /stderr; /external_requests; /retries | supports | The single original diagnostic exited 0 with saved streams, no external requests and no retries. |
| support-2207-chemistry-acceptance | /private/tmp/npm-review-work/shared-next-batch221/root-chemistry-acceptance-001.json; /status; /data; /execution; /records; /molecular_parse_attempts; /parse_errors; /denied_events; /false_comparisons | supports | ROOT accepted 20 original parsed forms with no parse errors/denials. Acceptance does not substitute for full molecular interpretation. |
| support-2207-warnings | /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-stderr-001.txt; Complete original stderr, lines 1-8. | supports | Two proton-added/removed warnings and two omitted-undefined-stereo warnings are global unassigned messages. They are not assigned to any selected owner. |
| support-2207-native-acceptance | /private/tmp/npm-review-work/shared-next-batch221/root-native-gates-acceptance-001.json; /results; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates | supports | Five local gates passed; full QC and ontology_consistency_OAK unavailable. Scientific completion remains partial. |
| support-2207-source-ownership | /private/tmp/npm-review-work/shared-next-batch221/intakes/2207-inspect-001.json; /targets/0/owner_paths; /targets/0/ownership_note | supports | Generated owner corrections belong to maintained source tables/extractor/seeder as named by this intake. |
| support-2207-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165-173. | supports | Maintained stereo_complete derives from FindMolChiralCenters and absence of unassigned atom-centre tags; it is not blanket natural stereochemistry verification. |
| support-2207-classification-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 406-432. | supports | ComputedClassification explicitly means a named/versioned structure prediction, never a source assertion or admission reason. |
| support-2207-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 1011-1019. | supports | The seeder copies model labels and converts the retained is_glycoside string into its Boolean prediction, preserving the model version. |
| support-2207-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds scope: predicate=exact complete standard_inchi_key equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=1. Empty scope is bounded to this retained query. |
| support-2207-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 233-233; exact row SHA256 2352ffb7240bb9c5b324a21fa77f05a0eff3af2259f7056fa2fd773b7fa41e8e. | supports | Complete retained row: {"mibig_accession":"BGC0000180","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"legioliulin","compound_index":"1","smiles":"OC1=C2C(=O)OC(\\C=C\\C=C\\C3=CC=CC=C3)=CC2=CC=C1","standard_inchi":"InChI=1S/C19H14O3/c20-17-12-6-10-15-13-16(22-19(21)18(15)17)11-5-4-9-14-7-2-1-3-8-14/h1-13,20H/b9-4+,11-5+","standard_inchi_key":"IFFMOWIJJAFQJN-HINBXAKRSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA0480","taxon_id":"NCBITaxon:45071","taxon_label":"Legionella parisiensis","bgc_classes":"PKS","bgc_subclasses":"Trans-AT type I","genome_accession":"KM222819.1","locus_from":"4550","locus_to":"31415","locus_evidence_methods":"Knock-out studies&#124;Gene expression correlated with compound production","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:23821465","reference_basis":"ENTRY"}. This is retained source payload, not freshly verified primary evidence. |
| support-2207-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures scope: predicate=exact complete standard_inchi_key equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=1. Empty scope is bounded to this retained query. |
| support-2207-row-chebi_structures-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Physical TSV lines 43064-43064; exact row SHA256 f423cd2724f336b6b4cef2de938e21e010ad198dd6909c2b62f3a2f14a96c3e3. | supports | Complete retained row: {"chebi_id":"CHEBI:156300","name":"legioliulin","definition":"A member of the class of isocoumarins that is 8-hydroxy-1H-isochromen-1-one substituted by a (1E,3E)-4-phenylbuta-1,3-dien-1-yl group at position 3. It is a fluorophore responsible for the blue-white autofluorescence in Legionella dumoffii.","stars":"3","standard_inchi_key":"IFFMOWIJJAFQJN-HINBXAKRSA-N","smiles":"O=c1oc(/C=C/C=C/c2ccccc2)cc2cccc(O)c12"}. This is retained source payload, not freshly verified primary evidence. |
| support-2207-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences scope: predicate=exact complete standard_inchi_key equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=2. Empty scope is bounded to this retained query. |
| support-2207-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 2743-2743; exact row SHA256 f3036579672c0395e13a54a96334575a3dda87f175820de719c8ea068a197f11. | supports | Complete retained row: {"standard_inchi_key":"IFFMOWIJJAFQJN-HINBXAKRSA-N","organism_name":"Legionella parisiensis","taxon_id":"NCBITaxon:45071","organism_wikidata":"http://www.wikidata.org/entity/Q15261673","reference_doi":"10.1002/CBIC.201300373","structure_wikidata":"http://www.wikidata.org/entity/Q75057232"}. This is retained source payload, not freshly verified primary evidence. |
| support-2207-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 2744-2744; exact row SHA256 68a0653681bcbe19a34fdae0fe0152ecc8e17e9c98a49aae5cc369b7ffca6843. | supports | Complete retained row: {"standard_inchi_key":"IFFMOWIJJAFQJN-HINBXAKRSA-N","organism_name":"Fluoribacter dumoffii","taxon_id":"NCBITaxon:463","organism_wikidata":"http://www.wikidata.org/entity/Q25858957","reference_doi":"10.1016/J.BBRC.2004.08.180","structure_wikidata":"http://www.wikidata.org/entity/Q75057232"}. This is retained source payload, not freshly verified primary evidence. |
| support-2207-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences scope: predicate=exact complete standard_inchi_key equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=0. Empty scope is bounded to this retained query. |
| support-2207-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier scope: predicate=exact complete standard_inchi_key equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=1. Empty scope is bounded to this retained query. |
| support-2207-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 960-960; exact row SHA256 dac935386a1688649303161bbdf0810f8aa533ac17c94c1d0760e74d0dadaf7b. | supports | Complete retained row: {"standard_inchi_key":"IFFMOWIJJAFQJN-HINBXAKRSA-N","smiles":"OC1=C2C(=O)OC(\\C=C\\C=C\\C3=CC=CC=C3)=CC2=CC=C1","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Coumarins","class_results":"Isocoumarins","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}. This is retained source payload, not freshly verified primary evidence. |
| support-2207-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay scope: predicate=exact complete standard_inchi_key equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=0. Empty scope is bounded to this retained query. |
| support-2207-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets scope: predicate=exact complete standard_inchi_key equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=0. Empty scope is bounded to this retained query. |
| support-2207-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys scope: predicate=exact complete standard_inchi_key equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=0. Empty scope is bounded to this retained query. |
| support-2207-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins scope: predicate=exact chebi_id from exact full-key structure rows; query=['CHEBI:156300']; matches=2. Empty scope is bounded to this retained query. |
| support-2207-row-chebi_origins-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Physical TSV lines 16995-16995; exact row SHA256 14b55270d73ede593794175f6c5cb68402500587dfb4499cb50966906f416d9f. | supports | Complete retained row: {"chebi_id":"CHEBI:156300","species_text":"Fluoribacter dumoffii","species_accession":"463","component_text":"","strain_text":"","source_accession":"15381093","comments":""}. This is retained source payload, not freshly verified primary evidence. |
| support-2207-row-chebi_origins-1 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Physical TSV lines 16996-16996; exact row SHA256 b016216bc870a37c26e81689940970101050d7befeef14dfe158321f43ae7dbe. | supports | Complete retained row: {"chebi_id":"CHEBI:156300","species_text":"Legionella parisiensis","species_accession":"45071","component_text":"","strain_text":"","source_accession":"23821465","comments":""}. This is retained source payload, not freshly verified primary evidence. |
| support-2207-taxon-45071 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; Complete OBO stanza, physical lines 20307-20311. | supports | [Term]<br>id: NCBITaxon:45071<br>name: Legionella parisiensis<br>synonym: "Legionella parisensis" EXACT [] This is the retained local taxonomy cache, not live authority. |
| support-2207-taxon-463 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; Complete OBO stanza, physical lines 687-691. | supports | [Term]<br>id: NCBITaxon:463<br>name: Fluoribacter dumoffii<br>synonym: "Legionella dumoffii" EXACT [] This is the retained local taxonomy cache, not live authority. |
| support-2207-taxon-routes | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/6/source_scope_inventory/source_taxa; /records/6/source_scope_inventory/forward_taxon_merge_matches; /records/6/source_scope_inventory/nonorganism_matches | supports | All selected source-taxon route sets read; no forward-merge or nonorganism match appears in this saved owner scope. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-221/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-221/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-221/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-221/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-221/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Full QC and complete ontology authority coverage/OAK were unavailable; passing local gates do not establish scientific completeness.
- No external retrieval, live taxonomy/identifier/protein queries or publication verification were performed. These assessments use the original saved owner-form computations; no additional molecular parses were performed during fragment authoring.
- Database citations and labels, versioned model predictions and source grades retain their stated evidence types. No publication independence, natural stereochemistry or full graph identity is inferred from matching keys.
- No source record or curation history was edited by this review. Canonical review persistence and campaign operations are separately ROOT-owned.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Selected mechanism roots and component references are absent; no maintained reader is applicable. This is artifact scope, not biological absence.
- No current source identity/producer/activity defect was established within this bounded evidence. Unresolved external verification and model/stereochemical limits remain explicit.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T113308Z-legioliulin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: legioliulin'
started_at: '2026-11-03T11:08:47.848002Z'
finished_at: '2026-11-03T11:33:08.348727Z'
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
summary: 'legioliulin: qualified partial review of exact retained structure, source
  grades, taxonomy and saved molecular topology.'
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/legioliulin.yaml
    sha256: 5b7d041aff170067c515d60d348de0988bf96cc15adca60401054e1c3c32a52f
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
  selection: Campaign path order 2207; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156300
targets:
- target_id: CHEBI:156300
  path: data/natural_products/shikimates_and_phenylpropanoids/legioliulin.yaml
  label: legioliulin
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
  - CHEBI:156300
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/echoside-b.yaml
    data/natural_products/shikimates_and_phenylpropanoids/echoside-c.yaml data/natural_products/shikimates_and_phenylpropanoids/echoside-d.yaml
    data/natural_products/shikimates_and_phenylpropanoids/echoside-e.yaml data/natural_products/shikimates_and_phenylpropanoids/ferroverdin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/hydroxytropodithietic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/legioliulin.yaml data/natural_products/shikimates_and_phenylpropanoids/mellein.yaml
    data/natural_products/shikimates_and_phenylpropanoids/microperfuranone.yaml data/natural_products/shikimates_and_phenylpropanoids/morpholine-containing-hemiacetal-piperazine-compound.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-221/validate-strict-selected10-001.tsv
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
  - CHEBI:156300
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-221/validate-all-001.tsv
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
  - CHEBI:156300
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
  - CHEBI:156300
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
  - CHEBI:156300
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-221/review-queue-001.tsv
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
  - CHEBI:156300
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:156300
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:156300
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2207-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/legioliulin.yaml
  locator: Complete raw owner, lines 1-135.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Complete selected owner and all 3 history events personally read; exact
    current bytes retained.
  snapshot_sha256: 5b7d041aff170067c515d60d348de0988bf96cc15adca60401054e1c3c32a52f
- evidence_id: support-2207-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json
  locator: /records/6
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Complete captured owner and literal mechanism-root absence; capture is
    the authoritative saved owner reading, not scientific verification.
  snapshot_sha256: 2210415fa28b6922444699bb73205eb3fe195a9daa94f96d193aae706d0b1b55
- evidence_id: support-2207-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/intakes/2207-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Complete current intake and all source input placements personally read;
    maintained ownership and exact target scope retained.
  snapshot_sha256: 14fd7a180d86b509f1205b00c73b4dbf43f352e4b8c66984dd493a1ace5bfbc6
- evidence_id: support-2207-intake-ready
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/root-intake-ready-001.json
  locator: /status; /records; /source_placements; /unique_source_paths; /mechanism_owner_orders
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: ROOT accepted the ten original intakes with 396 placements across 57 unique
    paths and no selected mechanism readers.
  snapshot_sha256: ae4b2499763d2da63172d43fcbfd00f53c29684c7ef10c59f0fd030d2a877925
- evidence_id: support-2207-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Complete retained selected source frames, direct predicates and exact intake
    input map; source collection is local and does not verify publications.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: support-2207-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/root-target-input-plan-acceptance-001.json
  locator: /status; /plan; /source_placements; /unique_source_paths; /per_order_counts
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: ROOT accepted the exact target-input plan and 396/57 maps.
  snapshot_sha256: 9156574ffb4dba0fb5d018bf09b5a93625abd4d184b8b5305f5ad79eb6090180
- evidence_id: support-2207-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-source-scope-notes-001.json
  locator: /reading; /cautions
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Explicit author/team reading attribution and bounded scientific source
    cautions; no fresh source retrieval.
  snapshot_sha256: 1590fe4aff9489e2d4bfba3444f56a607f01c0029f46288d01cecfbbaf9eaf72
- evidence_id: support-2207-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: BGC performed the admitted eight-table 79-token scan with zero hits; this
    is attributed bounded curation scope, not universal absence.
  snapshot_sha256: 1590fe4aff9489e2d4bfba3444f56a607f01c0029f46288d01cecfbbaf9eaf72
- evidence_id: support-2207-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/declared_structure; /records/6/smiles; /records/6/inchi; /records/6/comparisons;
    /records/6/atom_correspondence
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Both complete saved forms and all atom/bond/stereo/motif fields personally
    read. All ten comparisons true; complete atom map; full_graph_identity_established:false
    retained.
  snapshot_sha256: 3442ee764bfa4a6dc5c45524b05d448402c881cdae0b10bca2a6200d162d984f
- evidence_id: support-2207-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed; /records/6/inchi/computed
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Complete paired atom/bond/neighborhood, charge/isotope/aromatic, ring,
    stereo and motif tables support the bounded topology interpretation in assessment
    A6; the stored graph is not a natural-identity proof.
  snapshot_sha256: 3442ee764bfa4a6dc5c45524b05d448402c881cdae0b10bca2a6200d162d984f
- evidence_id: support-2207-chemistry-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-execution-001.json
  locator: /argv; /exit_code; /stdout; /stderr; /external_requests; /retries
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: The single original diagnostic exited 0 with saved streams, no external
    requests and no retries.
  snapshot_sha256: ed85a59dd5a7abcb3394c579c42e2cf0cc46c01781e962dba3025bd8d6444ad9
- evidence_id: support-2207-chemistry-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/root-chemistry-acceptance-001.json
  locator: /status; /data; /execution; /records; /molecular_parse_attempts; /parse_errors;
    /denied_events; /false_comparisons
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: ROOT accepted 20 original parsed forms with no parse errors/denials. Acceptance
    does not substitute for full molecular interpretation.
  snapshot_sha256: b8f9ad5a7e5ab5f998d1d2b594f633c6f8f75b20171c4385a57c8585cc135741
- evidence_id: support-2207-warnings
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-stderr-001.txt
  locator: Complete original stderr, lines 1-8.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Two proton-added/removed warnings and two omitted-undefined-stereo warnings
    are global unassigned messages. They are not assigned to any selected owner.
  snapshot_sha256: 4940b20f88d0b2a4d936fcfeee7ec4000e90e66213fc482d8b00ede5ebea6aa9
- evidence_id: support-2207-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/root-native-gates-acceptance-001.json
  locator: /results; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Five local gates passed; full QC and ontology_consistency_OAK unavailable.
    Scientific completion remains partial.
  snapshot_sha256: dd0cd192791e7954204141637854406302975cd1e4a2d56012ccbfc2dd05206d
- evidence_id: support-2207-source-ownership
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/intakes/2207-inspect-001.json
  locator: /targets/0/owner_paths; /targets/0/ownership_note
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Generated owner corrections belong to maintained source tables/extractor/seeder
    as named by this intake.
  snapshot_sha256: 14fd7a180d86b509f1205b00c73b4dbf43f352e4b8c66984dd493a1ace5bfbc6
- evidence_id: support-2207-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165-173.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: Maintained stereo_complete derives from FindMolChiralCenters and absence
    of unassigned atom-centre tags; it is not blanket natural stereochemistry verification.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2207-classification-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 406-432.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: ComputedClassification explicitly means a named/versioned structure prediction,
    never a source assertion or admission reason.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2207-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 1011-1019.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: The seeder copies model labels and converts the retained is_glycoside string
    into its Boolean prediction, preserving the model version.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2207-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Saved mibig_compounds scope: predicate=exact complete standard_inchi_key
    equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=1. Empty scope is bounded
    to this retained query.'
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: support-2207-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 233-233; exact row SHA256 2352ffb7240bb9c5b324a21fa77f05a0eff3af2259f7056fa2fd773b7fa41e8e.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Complete retained row: {"mibig_accession":"BGC0000180","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"legioliulin","compound_index":"1","smiles":"OC1=C2C(=O)OC(\\C=C\\C=C\\C3=CC=CC=C3)=CC2=CC=C1","standard_inchi":"InChI=1S/C19H14O3/c20-17-12-6-10-15-13-16(22-19(21)18(15)17)11-5-4-9-14-7-2-1-3-8-14/h1-13,20H/b9-4+,11-5+","standard_inchi_key":"IFFMOWIJJAFQJN-HINBXAKRSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA0480","taxon_id":"NCBITaxon:45071","taxon_label":"Legionella
    parisiensis","bgc_classes":"PKS","bgc_subclasses":"Trans-AT type I","genome_accession":"KM222819.1","locus_from":"4550","locus_to":"31415","locus_evidence_methods":"Knock-out
    studies|Gene expression correlated with compound production","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:23821465","reference_basis":"ENTRY"}.
    This is retained source payload, not freshly verified primary evidence.'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2207-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Saved chebi_structures scope: predicate=exact complete standard_inchi_key
    equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=1. Empty scope is bounded
    to this retained query.'
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: support-2207-row-chebi_structures-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Physical TSV lines 43064-43064; exact row SHA256 f423cd2724f336b6b4cef2de938e21e010ad198dd6909c2b62f3a2f14a96c3e3.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Complete retained row: {"chebi_id":"CHEBI:156300","name":"legioliulin","definition":"A
    member of the class of isocoumarins that is 8-hydroxy-1H-isochromen-1-one substituted
    by a (1E,3E)-4-phenylbuta-1,3-dien-1-yl group at position 3. It is a fluorophore
    responsible for the blue-white autofluorescence in Legionella dumoffii.","stars":"3","standard_inchi_key":"IFFMOWIJJAFQJN-HINBXAKRSA-N","smiles":"O=c1oc(/C=C/C=C/c2ccccc2)cc2cccc(O)c12"}.
    This is retained source payload, not freshly verified primary evidence.'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: support-2207-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Saved lotus_occurrences scope: predicate=exact complete standard_inchi_key
    equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=2. Empty scope is bounded
    to this retained query.'
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: support-2207-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 2743-2743; exact row SHA256 f3036579672c0395e13a54a96334575a3dda87f175820de719c8ea068a197f11.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Complete retained row: {"standard_inchi_key":"IFFMOWIJJAFQJN-HINBXAKRSA-N","organism_name":"Legionella
    parisiensis","taxon_id":"NCBITaxon:45071","organism_wikidata":"http://www.wikidata.org/entity/Q15261673","reference_doi":"10.1002/CBIC.201300373","structure_wikidata":"http://www.wikidata.org/entity/Q75057232"}.
    This is retained source payload, not freshly verified primary evidence.'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2207-row-lotus_occurrences-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 2744-2744; exact row SHA256 68a0653681bcbe19a34fdae0fe0152ecc8e17e9c98a49aae5cc369b7ffca6843.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Complete retained row: {"standard_inchi_key":"IFFMOWIJJAFQJN-HINBXAKRSA-N","organism_name":"Fluoribacter
    dumoffii","taxon_id":"NCBITaxon:463","organism_wikidata":"http://www.wikidata.org/entity/Q25858957","reference_doi":"10.1016/J.BBRC.2004.08.180","structure_wikidata":"http://www.wikidata.org/entity/Q75057232"}.
    This is retained source payload, not freshly verified primary evidence.'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2207-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Saved cyanometdb_occurrences scope: predicate=exact complete standard_inchi_key
    equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=0. Empty scope is bounded
    to this retained query.'
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: support-2207-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Saved npclassifier scope: predicate=exact complete standard_inchi_key
    equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=1. Empty scope is bounded
    to this retained query.'
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: support-2207-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 960-960; exact row SHA256 dac935386a1688649303161bbdf0810f8aa533ac17c94c1d0760e74d0dadaf7b.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Complete retained row: {"standard_inchi_key":"IFFMOWIJJAFQJN-HINBXAKRSA-N","smiles":"OC1=C2C(=O)OC(\\C=C\\C=C\\C3=CC=CC=C3)=CC2=CC=C1","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Coumarins","class_results":"Isocoumarins","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}.
    This is retained source payload, not freshly verified primary evidence.'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2207-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Saved pubchem_bioassay scope: predicate=exact complete standard_inchi_key
    equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=0. Empty scope is bounded
    to this retained query.'
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: support-2207-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Saved bindingdb_targets scope: predicate=exact complete standard_inchi_key
    equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=0. Empty scope is bounded
    to this retained query.'
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: support-2207-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Saved antibioticmech_inchikeys scope: predicate=exact complete standard_inchi_key
    equality; query=IFFMOWIJJAFQJN-HINBXAKRSA-N; matches=0. Empty scope is bounded
    to this retained query.'
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: support-2207-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Saved chebi_origins scope: predicate=exact chebi_id from exact full-key
    structure rows; query=[''CHEBI:156300'']; matches=2. Empty scope is bounded to
    this retained query.'
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: support-2207-row-chebi_origins-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Physical TSV lines 16995-16995; exact row SHA256 14b55270d73ede593794175f6c5cb68402500587dfb4499cb50966906f416d9f.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Complete retained row: {"chebi_id":"CHEBI:156300","species_text":"Fluoribacter
    dumoffii","species_accession":"463","component_text":"","strain_text":"","source_accession":"15381093","comments":""}.
    This is retained source payload, not freshly verified primary evidence.'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: support-2207-row-chebi_origins-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Physical TSV lines 16996-16996; exact row SHA256 b016216bc870a37c26e81689940970101050d7befeef14dfe158321f43ae7dbe.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: 'Complete retained row: {"chebi_id":"CHEBI:156300","species_text":"Legionella
    parisiensis","species_accession":"45071","component_text":"","strain_text":"","source_accession":"23821465","comments":""}.
    This is retained source payload, not freshly verified primary evidence.'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: support-2207-taxon-45071
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: Complete OBO stanza, physical lines 20307-20311.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: '[Term]

    id: NCBITaxon:45071

    name: Legionella parisiensis

    synonym: "Legionella parisensis" EXACT [] This is the retained local taxonomy
    cache, not live authority.'
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2207-taxon-463
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: Complete OBO stanza, physical lines 687-691.
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: '[Term]

    id: NCBITaxon:463

    name: Fluoribacter dumoffii

    synonym: "Legionella dumoffii" EXACT [] This is the retained local taxonomy cache,
    not live authority.'
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2207-taxon-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/source_taxa; /records/6/source_scope_inventory/forward_taxon_merge_matches;
    /records/6/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T11:24:55.163541Z'
  support: supports
  summary: All selected source-taxon route sets read; no forward-merge or nonorganism
    match appears in this saved owner scope.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-221/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json
  accessed_at: '2026-11-03T11:10:13.322718Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: e7bac32597510403baf82edb26400e7ff5ec8175e48b494bb1e3d649da975c3b
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-221/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json
  accessed_at: '2026-11-03T11:10:39.416135Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: d102de9a8e126b63c7ebecc65f3b0b96b8ce2117ac0ae0835ba385125e89b02b
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-221/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json
  accessed_at: '2026-11-03T11:10:59.558620Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-221/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json
  accessed_at: '2026-11-03T11:11:34.402203Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-221/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json
  accessed_at: '2026-11-03T11:11:46.456820Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: afe3bd09534d479f44cbec647a35fd4d3f395466bd25a250ca36dad1434726c4
assessments:
- assessment_id: support-2207-A1
  area: identity
  topic: Exact structure concept and grounding scope
  outcome: supported
  summary: Legioliulin has exact retained MIBiG and three-star ChEBI grounding to
    CHEBI:156300 through IFFMOWIJJAFQJN-HINBXAKRSA-N. The paired computations give
    neutral C19H14O3. The ChEBI isocoumarin and (1E,3E)-phenylbutadienyl definition
    is structurally compatible with the stored molecule; the blue-white autofluorescence
    statement remains a retained database definition, not a newly reproduced observation.
  target_ids:
  - CHEBI:156300
  evidence_ids:
  - support-2207-owner
  - support-2207-capture
  - support-2207-intake
  - support-2207-source-plan
  - support-2207-plan-acceptance
  - support-2207-chemistry
  - support-2207-query-mibig_compounds
  - support-2207-row-mibig_compounds-0
  - support-2207-query-chebi_structures
  - support-2207-row-chebi_structures-0
  dimensions:
  - name: standard_inchi_key
    value: IFFMOWIJJAFQJN-HINBXAKRSA-N
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-capture
    - support-2207-intake
    - support-2207-source-plan
    - support-2207-plan-acceptance
    - support-2207-chemistry
    - support-2207-query-mibig_compounds
    - support-2207-row-mibig_compounds-0
    - support-2207-query-chebi_structures
    - support-2207-row-chebi_structures-0
  - name: grounding_scope
    value: EXACT CHEBI:156300;MIBiG+ChEBI retained match
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-capture
    - support-2207-intake
    - support-2207-source-plan
    - support-2207-plan-acceptance
    - support-2207-chemistry
    - support-2207-query-mibig_compounds
    - support-2207-row-mibig_compounds-0
    - support-2207-query-chebi_structures
    - support-2207-row-chebi_structures-0
- assessment_id: support-2207-A2
  area: representation
  topic: Paired molecular representations and stereochemical limits
  outcome: supported
  summary: Both forms have 22 atoms and 24 bonds, all ten comparisons true and a complete
    22-atom correspondence; independent full graph and natural identity remain unproved.
    The two side-chain double bonds are explicitly STEREOE in the saved bond tables
    (SMILES bonds 7 and 9), with two specified potential-double entries and no unspecified
    tetrahedral centre. This supports the stored E,E representation rather than assigning
    geometry solely from the potential-stereo word Trans. The literal stereo_complete:true
    has the narrower maintained atom-centre derivation.
  target_ids:
  - CHEBI:156300
  evidence_ids:
  - support-2207-owner
  - support-2207-chemistry
  - support-2207-topology
  - support-2207-stereo-method
  - support-2207-chemistry-execution
  - support-2207-chemistry-acceptance
  - support-2207-warnings
  dimensions:
  - name: stereochemical_resolution
    value: Two specified E double bonds;literal true atom-centre flag
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-chemistry
    - support-2207-topology
    - support-2207-stereo-method
    - support-2207-chemistry-execution
    - support-2207-chemistry-acceptance
    - support-2207-warnings
  - name: representation_correspondence
    value: All comparisons true;22-atom map;full identity unproved
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-chemistry
    - support-2207-topology
    - support-2207-stereo-method
    - support-2207-chemistry-execution
    - support-2207-chemistry-acceptance
    - support-2207-warnings
- assessment_id: support-2207-A3
  area: provenance
  topic: Producer, occurrence and locus evidence grades
  outcome: supported
  summary: MIBiG BGC0000180 version 5 retains Legionella parisiensis NCBITaxon:45071
    at BGC_CHARACTERIZED and the locus at CLUSTER_DEMONSTRATED, based on knockout
    studies and expression correlated with production. The source entry is questionable/complete;
    KM222819.1 coordinates 4550–31415 preserve its locus scope without elevating it
    to a complete pathway. Four written occurrence assertions represent two taxa and
    two source types. Cache NCBITaxon:463 names Fluoribacter dumoffii and explicitly
    lists Legionella dumoffii as an exact synonym, so the historical definition and
    current occurrence label are compatible within this cache. L. parisiensis is a
    distinct taxon, not a synonym of dumoffii.
  target_ids:
  - CHEBI:156300
  evidence_ids:
  - support-2207-owner
  - support-2207-capture
  - support-2207-taxon-routes
  - support-2207-query-mibig_compounds
  - support-2207-row-mibig_compounds-0
  - support-2207-query-lotus_occurrences
  - support-2207-row-lotus_occurrences-0
  - support-2207-row-lotus_occurrences-1
  - support-2207-query-chebi_origins
  - support-2207-row-chebi_origins-0
  - support-2207-row-chebi_origins-1
  - support-2207-taxon-45071
  - support-2207-taxon-463
  dimensions:
  - name: taxon_and_strain_scope
    value: L.parisiensis45071;F.dumoffii463 occurrence synonym preserved
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-capture
    - support-2207-taxon-routes
    - support-2207-query-mibig_compounds
    - support-2207-row-mibig_compounds-0
    - support-2207-query-lotus_occurrences
    - support-2207-row-lotus_occurrences-0
    - support-2207-row-lotus_occurrences-1
    - support-2207-query-chebi_origins
    - support-2207-row-chebi_origins-0
    - support-2207-row-chebi_origins-1
    - support-2207-taxon-45071
    - support-2207-taxon-463
  - name: producer_evidence_tier
    value: BGC_CHARACTERIZED;BGC180v5
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-capture
    - support-2207-taxon-routes
    - support-2207-query-mibig_compounds
    - support-2207-row-mibig_compounds-0
    - support-2207-query-lotus_occurrences
    - support-2207-row-lotus_occurrences-0
    - support-2207-row-lotus_occurrences-1
    - support-2207-query-chebi_origins
    - support-2207-row-chebi_origins-0
    - support-2207-row-chebi_origins-1
    - support-2207-taxon-45071
    - support-2207-taxon-463
  - name: locus_evidence_tier
    value: CLUSTER_DEMONSTRATED;knockout/expression
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-capture
    - support-2207-taxon-routes
    - support-2207-query-mibig_compounds
    - support-2207-row-mibig_compounds-0
    - support-2207-query-lotus_occurrences
    - support-2207-row-lotus_occurrences-0
    - support-2207-row-lotus_occurrences-1
    - support-2207-query-chebi_origins
    - support-2207-row-chebi_origins-0
    - support-2207-row-chebi_origins-1
    - support-2207-taxon-45071
    - support-2207-taxon-463
- assessment_id: support-2207-A4
  area: evidence
  topic: Citation placement and historical verification scope
  outcome: supported
  summary: PMID:23821465 is the MIBiG ENTRY citation and also appears in the ChEBI
    L. parisiensis origin; its related LOTUS DOI is 10.1002/CBIC.201300373. The dumoffii
    occurrence sources retain DOI:10.1016/J.BBRC.2004.08.180 and PMID:15381093. Their
    preservation does not establish publication independence or fresh primary verification.
    The current owner already separates occurrence and producer claims and explicitly
    cautions about shared publications.
  target_ids:
  - CHEBI:156300
  evidence_ids:
  - support-2207-owner
  - support-2207-capture
  - support-2207-taxon-routes
  - support-2207-query-mibig_compounds
  - support-2207-row-mibig_compounds-0
  - support-2207-query-lotus_occurrences
  - support-2207-row-lotus_occurrences-0
  - support-2207-row-lotus_occurrences-1
  - support-2207-query-chebi_origins
  - support-2207-row-chebi_origins-0
  - support-2207-row-chebi_origins-1
  - support-2207-taxon-45071
  - support-2207-taxon-463
  - support-2207-source-notes
  - support-2207-query-chebi_structures
  - support-2207-row-chebi_structures-0
  dimensions:
  - name: citation_scope
    value: PMID23821465 and occurrence citations;independence unproved
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-capture
    - support-2207-taxon-routes
    - support-2207-query-mibig_compounds
    - support-2207-row-mibig_compounds-0
    - support-2207-query-lotus_occurrences
    - support-2207-row-lotus_occurrences-0
    - support-2207-row-lotus_occurrences-1
    - support-2207-query-chebi_origins
    - support-2207-row-chebi_origins-0
    - support-2207-row-chebi_origins-1
    - support-2207-taxon-45071
    - support-2207-taxon-463
    - support-2207-source-notes
    - support-2207-query-chebi_structures
    - support-2207-row-chebi_structures-0
- assessment_id: support-2207-A5
  area: scope
  topic: Occurrence, assay and companion boundaries
  outcome: supported
  summary: Two LOTUS and two ChEBI-origin rows support occurrence claims for Fluoribacter
    dumoffii and Legionella parisiensis; they do not turn all occurring organisms
    into experimentally demonstrated producers. Exact selected PubChem, BindingDB,
    AntibioticMech and CyanometDB joins are empty, and no direct companions are admitted.
    The retained fluorophore definition is not substituted for a quantitative pharmacology
    or target assay, and the empty assay scope does not establish inactivity.
  target_ids:
  - CHEBI:156300
  evidence_ids:
  - support-2207-owner
  - support-2207-curation-scope
  - support-2207-source-notes
  - support-2207-query-lotus_occurrences
  - support-2207-row-lotus_occurrences-0
  - support-2207-row-lotus_occurrences-1
  - support-2207-query-chebi_origins
  - support-2207-row-chebi_origins-0
  - support-2207-row-chebi_origins-1
  - support-2207-query-cyanometdb_occurrences
  - support-2207-query-pubchem_bioassay
  - support-2207-query-bindingdb_targets
  - support-2207-query-antibioticmech_inchikeys
  dimensions:
  - name: occurrence_scope
    value: Four assertions across two taxa/two sources
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-curation-scope
    - support-2207-source-notes
    - support-2207-query-lotus_occurrences
    - support-2207-row-lotus_occurrences-0
    - support-2207-row-lotus_occurrences-1
    - support-2207-query-chebi_origins
    - support-2207-row-chebi_origins-0
    - support-2207-row-chebi_origins-1
    - support-2207-query-cyanometdb_occurrences
    - support-2207-query-pubchem_bioassay
    - support-2207-query-bindingdb_targets
    - support-2207-query-antibioticmech_inchikeys
  - name: assay_scope
    value: No exact selected assay/target rows;not inactivity
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-curation-scope
    - support-2207-source-notes
    - support-2207-query-lotus_occurrences
    - support-2207-row-lotus_occurrences-0
    - support-2207-row-lotus_occurrences-1
    - support-2207-query-chebi_origins
    - support-2207-row-chebi_origins-0
    - support-2207-row-chebi_origins-1
    - support-2207-query-cyanometdb_occurrences
    - support-2207-query-pubchem_bioassay
    - support-2207-query-bindingdb_targets
    - support-2207-query-antibioticmech_inchikeys
- assessment_id: support-2207-A6
  area: other
  topic: Computed classification and full-table topology limits
  outcome: supported
  summary: The complete graph contains a benzene-fused six-member oxygen heterocycle
    bearing C3=O4 and aromatic ring oxygen O5, plus a terminal phenyl ring joined
    by an E,E conjugated diene. The generic SINGLE-bond ester scan does not report
    the aromaticized isocoumarin ring; this is a motif-helper limitation, not absence
    of the ring carbonyl/oxygen topology. No sugar residue is present. NPClassifier
    Coumarins/Isocoumarins and false glycoside status describe the retained prediction;
    the MIBiG PKS class is a separate biosynthetic classification.
  target_ids:
  - CHEBI:156300
  evidence_ids:
  - support-2207-owner
  - support-2207-chemistry
  - support-2207-topology
  - support-2207-classification-schema
  - support-2207-classification-seeder
  - support-2207-query-npclassifier
  - support-2207-row-npclassifier-0
  - support-2207-query-mibig_compounds
  - support-2207-row-mibig_compounds-0
  dimensions:
  - name: computed_classification
    value: Aromaticized isocoumarin/diene topology;motif helper limitation
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-chemistry
    - support-2207-topology
    - support-2207-classification-schema
    - support-2207-classification-seeder
    - support-2207-query-npclassifier
    - support-2207-row-npclassifier-0
    - support-2207-query-mibig_compounds
    - support-2207-row-mibig_compounds-0
- assessment_id: support-2207-A7
  area: completeness
  topic: Partial scientific completion and maintained ownership
  outcome: supported
  summary: This is a qualified partial review with stronger imported locus/producer
    evidence than a source assertion, but no complete biosynthetic pathway, molecular
    targets, causal graphs or components are stored. The biosynthesis queue remains
    a completeness lead, not proof that a pathway was reconstructed here. No maintained
    reader applies. Five local gates passed; full QC, OAK coverage and fresh publication
    verification remain unavailable. Maintained owner paths in the intake define any
    future correction route.
  target_ids:
  - CHEBI:156300
  evidence_ids:
  - support-2207-owner
  - support-2207-capture
  - support-2207-intake
  - support-2207-intake-ready
  - support-2207-native-acceptance
  - support-2207-chemistry-acceptance
  - support-2207-source-ownership
  - support-2207-source-notes
  dimensions:
  - name: review_completion
    value: partial;no complete pathway;QC/OAK/primary verification unavailable
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2207-owner
    - support-2207-capture
    - support-2207-intake
    - support-2207-intake-ready
    - support-2207-native-acceptance
    - support-2207-chemistry-acceptance
    - support-2207-source-ownership
    - support-2207-source-notes
findings: []
actions: []
limitations:
- Full QC and complete ontology authority coverage/OAK were unavailable; passing local
  gates do not establish scientific completeness.
- No external retrieval, live taxonomy/identifier/protein queries or publication verification
  were performed. These assessments use the original saved owner-form computations;
  no additional molecular parses were performed during fragment authoring.
- Database citations and labels, versioned model predictions and source grades retain
  their stated evidence types. No publication independence, natural stereochemistry
  or full graph identity is inferred from matching keys.
- No source record or curation history was edited by this review. Canonical review
  persistence and campaign operations are separately ROOT-owned.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Selected mechanism roots and component references are absent; no maintained reader
  is applicable. This is artifact scope, not biological absence.
- No current source identity/producer/activity defect was established within this
  bounded evidence. Unresolved external verification and model/stereochemical limits
  remain explicit.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-221
```
