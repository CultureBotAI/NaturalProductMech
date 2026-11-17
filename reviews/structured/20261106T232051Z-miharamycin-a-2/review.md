# Local evidence review: miharamycin A

- Review: 20261106T232051Z-miharamycin-a-2
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T22:48:57.544803Z
- Finished UTC: 2026-11-06T23:20:51.517517Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The owner at miharamycin-a-2.yaml is labelled miharamycin A; the filename suffix is not a distinct source compound name. Its BGC0001956 full key and wholly unspecified tetrahedral layer are kept separate from the other selected Miharamycin A owner. The source locus remains unstated. Saved representation differences and the explicit comparison input support a qualified partial pass without merging or filling missing stereochemistry.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2788; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-ace24a1c40 | data/natural_products/unclassified/miharamycin-a-2.yaml | generated | miharamycin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-ace24a1c40 | Both stored forms parsed and match the declared normalized key/formula and normalized identifiers; both canonical SMILES comparisons are false and the saved atom map is empty. |
| strict_ten | passed | True | naturalproductmech:mibig-ace24a1c40 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-ace24a1c40 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-ace24a1c40 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-ace24a1c40 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-ace24a1c40 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-ace24a1c40 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-ace24a1c40 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-ace24a1c40 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained compound grounding

identity: supported. Targets: naturalproductmech:mibig-ace24a1c40.

BGC0001956:1, version 3, active, questionable quality and unknown completeness, grounds the label miharamycin A and pubchem:202591. The full key is QSPCQKVMQODSDN-UHFFFAOYSA-N. The reciprocal captured owner has the same label and first key block but full key QSPCQKVMQODSDN-TVGXWQJGSA-N and a different BGC. These explicit comparison inputs are not direct shared-BGC edges. Equal nonisomeric strings within each corresponding saved form support a limited connectivity comparison; they do not authorize an identity merge, source-grade transfer or stereochemical completion.

### Saved molecular forms, stereochemistry and motif scope

representation: supported. Targets: naturalproductmech:mibig-ace24a1c40.

Each saved form has C20H30N10O9, 39 atoms, 42 bonds, one component and charge zero. The source has two carbonyls, one acid and one amide; the InChI-derived form retains the acid carbonyl and represents the amide as C(OH)=N. An exocyclic amino group on the aromatic aza-ring becomes an imino group while a ring nitrogen gains hydrogen. The original guanidine C=N persists. These saved tautomer-sensitive representations agree in normalized InChI/key but not canonical SMILES; the correspondence map remains empty. The source saturated six-ring [2,3,4,5,6,7] has five carbons and one oxygen; the adjacent five-ring [0,1,2,7,8] has four carbons and one oxygen and shares edge 2–7. They are a fused bicyclic oxygenated system, not two disjoint glycosides. Two further rings form a fused aromatic nitrogen heterocycle. Source acid C20 and amide C24/N23 are separate; InChI amide-derived C14(OH32)=N26 and aza-ring C18=N23 illustrate the changed bond/proton placement. The N–OH group remains on the guanidine. No ester, N-acetyl or phosphorus motif is present. Eight saved comparison flags agree, including standard InChI, complete key, formula, charge and atom/bond counts. Both canonical isomeric and nonisomeric SMILES comparisons are false. The saved chirality-aware correspondence list is empty, complete_atom_count_match is false and full_graph_identity_established is false. Equal normalized identifiers do not establish a returned graph map, complete tautomer equivalence, natural-sample identity or experimental stereochemistry.

### Producer, taxon and compound-specific locus

provenance: supported. Targets: naturalproductmech:mibig-ace24a1c40.

Streptomyces miharaensis, NCBITaxon:285483, is a SOURCE_ASSERTION from BGC0001956. The matching LOTUS taxon is a separately attributed occurrence, not independent causal production evidence. The stronger locus evidence attached to BGC0002479 cannot be transferred to this source compound merely through its identical label or connectivity-prefix key. BGC0001956:1 retains MH534948.1 with no locus bounds or experimental methods stated, so CLUSTER_UNSTATED remains appropriate. The entry retains questionable quality and unknown completeness. Its PKS/Unknown source class does not prove a complete mechanism or sequence assignment, and the BGC0002479 coordinates and heterologous-expression claim belong to the other owner.

### Reference grain and historical provenance

evidence: supported. Targets: naturalproductmech:mibig-ace24a1c40.

DOI:10.1021/jacs.9b03021 is ENTRY-level MIBiG attribution. The LOTUS DOI:10.1021/JACS.9B03021 differs only in case and is not independent publication evidence. The owner explicitly leaves publication independence unestablished. All three seeding events, 2026-09-10, 2026-09-25 and 2026-10-13, are provenance for generation, not scientific verification. No paper or sequence was fetched.

### Occurrence and retained assay limits

evidence: supported. Targets: naturalproductmech:mibig-ace24a1c40.

The single LOTUS row attributes this full-key structure to Streptomyces miharaensis, NCBITaxon:285483, with organism Q104853211 and structure Q82899820. Its occurrence status is preserved beside the producer assertion, with the shared-publication caveat. No production, activity or BGC-completeness upgrade follows from that match. All nine saved query frames were read. PubChem CID 202591 has one blank-AID sentinel, with no actual assay or biological measurement. Exact-key ChEBI, CyanoMetDB, BindingDB and AntibioticMech negatives are limited to the retained predicates. No inactivity, missing universal target or natural-product identity conclusion is drawn.

### Classification, filing and literal mechanism scope

consistency: supported. Targets: naturalproductmech:mibig-ace24a1c40.

The retained NPClassifier version npclassifier.gnps2.org@2026-09-07 has empty pathway, superclass and class lists and is_glycoside false. Empty pathway results correctly retain UNCLASSIFIED; source PKS remains separate. The saved fused oxygenated rings are structural observations and do not automatically replace the model's glycoside flag or establish a particular sugar identity. No mechanism, pathway, component, activity, target or related-record root is present.

### Earned review and unavailable authority

completeness: supported. Targets: naturalproductmech:mibig-ace24a1c40.

The complete current owner and exact source rows were read, actual canonical intake fixed current ownership and input hashes, and the one original saved molecular computation was assessed without replay. Literal mechanism, pathway, component, target, activity and related-record roots are absent; no maintained reader is assigned. Five local native commands passed, but full QC, complete OAK checks and external primary verification remain unavailable. Completion is partial; native SEEDED status and generated records remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2788-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/miharamycin-a-2.yaml; complete file: chemical_structure, source_concepts, producer_organisms, biosynthetic_gene_clusters, classification and history | supports | Complete current generated owner read; no record or native status edit. |
| support-2788-capture | /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json; /records/7/owner_document; /records/7/component_captures | supports | Accepted complete owner/history capture and empty selected component scope; raw capture is not a maintained-reader invocation. |
| support-2788-source | /private/tmp/npm-review-work/shared-next-batch279-tentative/support-prep/support-current279-assigned-source-reading-002.json; /contexts/2; /totals; /global_cautions | supports | Complete nine-frame assigned source context, all physical positive rows, fields and negative predicates personally read. Own primary credit is 21 rows/241 fields across these five selected contexts; no BGC or Native row duplication. |
| support-2788-plan | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-target-input-plan-001.json; /records/7; /source_placement_count; /unique_source_path_count | supports | Actual original plan retains owner and direct-context inputs; global scope is 469 placements/70 paths, with no additional reviewed-target credit. |
| support-2788-planaccept | /private/tmp/npm-review-work/shared-next-batch279/root-current279-input-plan-acceptance-001.json; /status; /accepted; /input_plan; /source_placements; /unique_source_paths | supports | ROOT accepted the original current source plan. |
| support-2788-notes | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /curation | supports | Current source notes preserve disjoint BGC/Support source readings and Native taxonomy/curation attribution without new primary proof. |
| support-2788-intake | /private/tmp/npm-review-work/shared-next-batch279/intakes-001/2788-inspect-001.json; /status; /source; /targets | supports | Actual canonical intake preserves this generated target, maintained owners and complete current input hash map. |
| support-2788-intakeaccept | /private/tmp/npm-review-work/shared-next-batch279/root-current279-intake-acceptance-001.json; /status; /accepted; /intake_summary; /records; /source_placements; /unique_source_paths | supports | ROOT accepted all ten original canonical intakes; this scientific review uses only its assigned target. |
| support-2788-data | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles; /records/7/inchi; /records/7/comparisons; /records/7/atom_correspondence | supports | Each saved form has C20H30N10O9, 39 atoms, 42 bonds, one component and charge zero. The source has two carbonyls, one acid and one amide; the InChI-derived form retains the acid carbonyl and represents the amide as C(OH)=N. An exocyclic amino group on the aromatic aza-ring becomes an imino group while a ring nitrogen gains hydrogen. The original guanidine C=N persists. These saved tautomer-sensitive representations agree in normalized InChI/key but not canonical SMILES; the correspondence map remains empty. Eight saved comparison flags agree, including standard InChI, complete key, formula, charge and atom/bond counts. Both canonical isomeric and nonisomeric SMILES comparisons are false. The saved chirality-aware correspondence list is empty, complete_atom_count_match is false and full_graph_identity_established is false. Equal normalized identifiers do not establish a returned graph map, complete tautomer equivalence, natural-sample identity or experimental stereochemistry. |
| support-2788-stereo | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/smiles/computed/potential_stereo; /records/7/inchi/computed/potential_stereo; /records/7/smiles/computed/atoms; /records/7/inchi/computed/atoms | supports | All eight saved tetrahedral candidates are unspecified in both forms, with no specified atom configuration. The false stereo_complete flag is therefore retained. The source has one unspecified guanidine double-bond candidate; the InChI-derived form has three, including the imidic amide and relocated exocyclic aza-ring imine. The other Miharamycin A owner's six specified centres cannot fill these unknowns. No cross-owner or natural stereochemical identity is established. |
| support-2788-motifs | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed/motifs; /records/7/smiles/computed/rings; /records/7/smiles/computed/bonds; /records/7/inchi/computed/motifs; /records/7/inchi/computed/rings; /records/7/inchi/computed/bonds | supports | The source saturated six-ring [2,3,4,5,6,7] has five carbons and one oxygen; the adjacent five-ring [0,1,2,7,8] has four carbons and one oxygen and shares edge 2–7. They are a fused bicyclic oxygenated system, not two disjoint glycosides. Two further rings form a fused aromatic nitrogen heterocycle. Source acid C20 and amide C24/N23 are separate; InChI amide-derived C14(OH32)=N26 and aza-ring C18=N23 illustrate the changed bond/proton placement. The N–OH group remains on the guanidine. No ester, N-acetyl or phosphorus motif is present. |
| support-2788-molecularreading | /private/tmp/npm-review-work/shared-next-batch279-tentative/support-prep/support-current279-last-five-molecular-intake-reading-001.json; /records/2; /counts; /warnings | supports | Complete ten assigned saved forms and actual intakes retained; no molecular replay. Six undefined-stereo warnings remain globally unassigned. |
| support-2788-execution | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries | supports | Single original diagnostic exited zero, with exact command/streams and no retry. Process success is not a natural-identity result. |
| support-2788-diagaccept | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /DATA; /execution | supports | ROOT accepted the original saved diagnostic; no additional parse was performed for this review. |
| support-2788-stderr | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-original-001.stderr; complete original stderr, six warning lines | supports | Six undefined-stereo warning lines are globally unassigned to records. They are not used as six record-specific defects. |
| support-2788-taxonomy | /private/tmp/npm-review-work/shared-next-batch279-tentative/native-prep/native-current279-cached-taxonomy-reading-001.json; /context_interpretations/24; /whole_stanzas; /physical_negative_query_scopes/24 | supports | Retain Streptomyces miharaensis (285483) as attributed, but keep the BGC0001956/MH534948.1/DOI10.1021/jacs.9b03021 and BGC0002479/MN850873.1/PMID32167762 source compounds, locus bounds and ENTRY citations separate. The two selected Miharamycin A owners have distinct full InChIKeys QSPCQKVMQODSDN-UHFFFAOYSA-N and QSPCQKVMQODSDN-TVGXWQJGSA-N. Shared label, producer or first key block does not authorize identity merging or stereochemical transfer. Reciprocal selected-owner comparison inputs are separately declared, not additional BGC companion evidence; Miharamycin B remains a distinct compound. |
| support-2788-curation | /private/tmp/npm-review-work/shared-next-batch279-tentative/native-prep/native-current279-implemented-curation-scan-001.json; /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows; /implementation_scope; /input_ownership | supports | Native found no exact applicable implemented curation decision; lexical numerical/name hits do not establish applicability. |
| support-2788-producerpolicy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; complete retained method grading table | supports | The method table distinguishes organism+cluster knockout support from cluster-only enzymatic or heterologous evidence, and preserves the unstated-method grade. |
| support-2788-stereopolicy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172, FindMolChiralCenters(includeUnassigned=True, useLegacyImplementation=False) | supports | The source stereo_complete predicate checks unassigned atom centres. It does not establish complete natural-product geometry. |
| support-2788-filingpolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306, choose_pathway | supports | Exactly one supported normalized pathway label selects a directory; multiple, empty or unsupported labels retain UNCLASSIFIED. All model labels are preserved separately. |
| support-2788-gates | /private/tmp/npm-review-work/shared-next-batch279/root-current279-five-gates-acceptance-001.json; /records; /selected_queue_rows; /full_native_checks_passed; /unavailable_checks; /scope | supports | Five local command results passed; full QC/OAK remain unavailable. Current producer, pathway, biosynthesis and stereo queue rows are scoped diagnostic leads, not automatic findings. |
| support-2788-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame has 1 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2788-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2788-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame has 1 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2788-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2788-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame has 1 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2788-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame has 1 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2788-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2788-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2788-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/24/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame has 0 positive placements; complete rows or the complete empty predicate frame were read. |
| support-2788-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical line 2266, raw UTF-8 row SHA-256 6b47f2ad9899aa77495bf2637c79d16e212372ef6cefb4c61b4f5e15014c0440 | supports | BGC0001956:1, version 3, active, questionable quality and unknown completeness, grounds the label miharamycin A and pubchem:202591. The full key is QSPCQKVMQODSDN-UHFFFAOYSA-N. The reciprocal captured owner has the same label and first key block but full key QSPCQKVMQODSDN-TVGXWQJGSA-N and a different BGC. These explicit comparison inputs are not direct shared-BGC edges. Equal nonisomeric strings within each corresponding saved form support a limited connectivity comparison; they do not authorize an identity merge, source-grade transfer or stereochemical completion. |
| support-2788-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical line 7400, raw UTF-8 row SHA-256 09e35e90487e416fe469075ad554ef9733d846b986f31e73bb5b883a9efbcbd3 | supports | The single LOTUS row attributes this full-key structure to Streptomyces miharaensis, NCBITaxon:285483, with organism Q104853211 and structure Q82899820. Its occurrence status is preserved beside the producer assertion, with the shared-publication caveat. No production, activity or BGC-completeness upgrade follows from that match. |
| support-2788-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical line 2032, raw UTF-8 row SHA-256 729f2d11fa3a49c27f0ef59f785b187ddc693c01c5878bd221ca3839554cc491 | supports | The retained NPClassifier version npclassifier.gnps2.org@2026-09-07 has empty pathway, superclass and class lists and is_glycoside false. Empty pathway results correctly retain UNCLASSIFIED; source PKS remains separate. The saved fused oxygenated rings are structural observations and do not automatically replace the model's glycoside flag or establish a particular sugar identity. No mechanism, pathway, component, activity, target or related-record root is present. |
| support-2788-table-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical line 5732, raw UTF-8 row SHA-256 2993461b945d3493bcab1c07beedd8b89790d77b4ec3d2f42e112dde5bc4d6cc | supports | All nine saved query frames were read. PubChem CID 202591 has one blank-AID sentinel, with no actual assay or biological measurement. Exact-key ChEBI, CyanoMetDB, BindingDB and AntibioticMech negatives are limited to the retained predicates. No inactivity, missing universal target or natural-product identity conclusion is drawn. |
| support-2788-history | /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json; /records/7/owner_document/curation_history; /records/7/owner_document/source_concepts | supports | DOI:10.1021/jacs.9b03021 is ENTRY-level MIBiG attribution. The LOTUS DOI:10.1021/JACS.9B03021 differs only in case and is not independent publication evidence. The owner explicitly leaves publication independence unestablished. All three seeding events, 2026-09-10, 2026-09-25 and 2026-10-13, are provenance for generation, not scientific verification. No paper or sequence was fetched. |
| support-2788-scope | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-target-input-plan-001.json; /records/7/complete_root_keys; /records/7/declared_mechanism_roots_literal; /records/7/component_paths; /records/7/literal_related_record_corpora | supports | Literal selected mechanism/pathway/component/target/activity/related roots are absent. This is not evidence of biological absence and assigns no maintained reader. |
| support-2788-counterpart-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/miharamycin-a.yaml; complete file: chemical_structure, source_concepts, producer_organisms and biosynthetic_gene_clusters | supports | Explicit captured comparison owner only: identical label and first key block, distinct full key/stereochemistry and BGC authority; no merge, grade transfer or new reviewed-target credit. |
| support-2788-counterpart-molecular | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/smiles; /records/7/inchi; /records/7/comparisons; /records/7/atom_correspondence; /records/8/declared_structure; /records/8/smiles; /records/8/inchi; /records/8/comparisons; /records/8/atom_correspondence | supports | Both complete saved Miharamycin pairs were read. Corresponding per-form nonisomeric strings agree across owners, but full keys and 0 versus 6 specified tetrahedral centres differ. Within each owner the two canonical representations differ; no full graph identity or stereochemical transfer is established. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-279/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-279/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-279/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-279/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-279/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Primary papers, spectra, sequences, live taxonomy and natural-product identity were not independently verified. Full QC, complete OAK and external primary checks remain unavailable.
- Eight saved comparison flags agree, including standard InChI, complete key, formula, charge and atom/bond counts. Both canonical isomeric and nonisomeric SMILES comparisons are false. The saved chirality-aware correspondence list is empty, complete_atom_count_match is false and full_graph_identity_established is false. Equal normalized identifiers do not establish a returned graph map, complete tautomer equivalence, natural-sample identity or experimental stereochemistry. All eight saved tetrahedral candidates are unspecified in both forms, with no specified atom configuration. The false stereo_complete flag is therefore retained. The source has one unspecified guanidine double-bond candidate; the InChI-derived form has three, including the imidic amide and relocated exocyclic aza-ring imine. The other Miharamycin A owner's six specified centres cannot fill these unknowns. No cross-owner or natural stereochemical identity is established.
- Six undefined-stereo warning lines are globally unassigned. Exact-key negatives and literal root absence do not establish inactivity or universal absence.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh current 279 scientific judgments use current retained owner/source/intake/diagnostic evidence; earlier batches supply interface logic only.
- No generated record, source inventory, native status or campaign artifact was edited. No query, molecular parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual local native checks and three required unavailable checks. No maintained-reader check belongs to these zero-reader targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T232051Z-miharamycin-a-2
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: miharamycin A'
started_at: '2026-11-06T22:48:57.544803Z'
finished_at: '2026-11-06T23:20:51.517517Z'
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
summary: The owner at miharamycin-a-2.yaml is labelled miharamycin A; the filename
  suffix is not a distinct source compound name. Its BGC0001956 full key and wholly
  unspecified tetrahedral layer are kept separate from the other selected Miharamycin
  A owner. The source locus remains unstated. Saved representation differences and
  the explicit comparison input support a qualified partial pass without merging or
  filling missing stereochemistry.
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
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: curation/unresolved_taxa.tsv
    sha256: 86efbda9c09388723a4f24da35e18404032f1549a9088192fbd2020cb846fa43
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/carbohydrates/miharamycin-b.yaml
    sha256: db0853cb5b961b3aa830564d6567f300295cebaad4a510f8afc73b5616617fcf
    role: context
  - path: data/natural_products/unclassified/miharamycin-a-2.yaml
    sha256: d9f19da8b0dc2f398d24156ebe873296fa42553e65a9de4d4e613733f4bd2233
    role: target
  - path: data/natural_products/unclassified/miharamycin-a.yaml
    sha256: 2c745d7fc5ceaa4769f9277e1502726c6c15804f60290b3bb4e03ee75ab2596f
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
  - path: data/raw/taxon_merged.tsv
    sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
    role: context
  - path: data/raw/taxon_non_organism.tsv
    sha256: f2c1ee257bbbcb0854528196ab1f809d658c27f1c7b2036f7f71f088b52935bb
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
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2788; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-ace24a1c40
targets:
- target_id: naturalproductmech:mibig-ace24a1c40
  path: data/natural_products/unclassified/miharamycin-a-2.yaml
  label: miharamycin A
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
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Retained exclusion-table diagnostic context captured for every review; applicable
      exact assay exclusions and biological rows must be derived from actual retained
      inventory, not file presence.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/unresolved_taxa.tsv
    role: Retained unresolved-taxon diagnostic context used by the bounded curation
      scan; no fresh taxonomy, forward-merge decision or producer confirmation.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/miharamycin-a.yaml
    role: 'Explicit retained counterpart for bounded identity comparison: same first
      InChIKey block and label, distinct complete keys/stereochemical layers and owned
      BGCs. This input is not a direct BGC/full-key identity edge and does not authorize
      a merge or evidence-grade transfer.'
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_merged.tsv
    role: Retained explicit forward-merge table used by positive and negative taxon
      queries for each owner; historical route evidence only, no fresh taxonomy.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_non_organism.tsv
    role: Retained non-organism table used by positive and negative taxon queries
      for each owner; diagnostic scope only, not a taxon verdict from file presence.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Maintained exclusion identity, source-row digest and attributed-rationale
      implementation context; no execution or new assay evidence.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: 'Maintained producer-strain qualification implementation: source-row and
      digest predicate, strain-only CURATOR_INFERENCE scope; plaintext dependency,
      no execution or grade/taxon upgrade.'
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: 'Maintained row_digest implementation used by qualification guards: sorted
      ensure_ascii JSON digest only; input presence does not claim an audit or application
      of other structure-correction behavior.'
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners.
checks:
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnose279-001.py
    a7294b88d0cf543a0d838418f9f884f502b2a2fab9e2fe6292739731ec63e673 7d587c755373d7148002108737073753112d72744cddfc3b885327d4320222ed
    9e4bcf4327dbebf8f8b5387771e02cdcb2590d4507e185f6170391192bc3f389
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed and match the declared normalized key/formula
    and normalized identifiers; both canonical SMILES comparisons are false and the
    saved atom map is empty.
  scope_note: Eight saved comparison flags agree, including standard InChI, complete
    key, formula, charge and atom/bond counts. Both canonical isomeric and nonisomeric
    SMILES comparisons are false. The saved chirality-aware correspondence list is
    empty, complete_atom_count_match is false and full_graph_identity_established
    is false. Equal normalized identifiers do not establish a returned graph map,
    complete tautomer equivalence, natural-sample identity or experimental stereochemistry.
    All eight saved tetrahedral candidates are unspecified in both forms, with no
    specified atom configuration. The false stereo_complete flag is therefore retained.
    The source has one unspecified guanidine double-bond candidate; the InChI-derived
    form has three, including the imidic amide and relocated exocyclic aza-ring imine.
    The other Miharamycin A owner's six specified centres cannot fill these unknowns.
    No cross-owner or natural stereochemical identity is established. Six original
    warning lines remain globally unassigned; no replay.
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  evidence_ids:
  - support-2788-data
  - support-2788-execution
  - support-2788-diagaccept
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  command: just validate-strict data/natural_products/unclassified/microansamycin-g.yaml
    data/natural_products/unclassified/microansamycin-h.yaml data/natural_products/unclassified/micropeptin-k139.yaml
    data/natural_products/unclassified/microtermolide-a.yaml data/natural_products/unclassified/microviridin-1748.yaml
    data/natural_products/unclassified/microviridin-j.yaml data/natural_products/unclassified/microviridin-n5.yaml
    data/natural_products/unclassified/miharamycin-a-2.yaml data/natural_products/unclassified/miharamycin-a.yaml
    data/natural_products/unclassified/minimycin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-279/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-ace24a1c40
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-279/validate-all-001.tsv
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
  - naturalproductmech:mibig-ace24a1c40
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
  - naturalproductmech:mibig-ace24a1c40
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
  - naturalproductmech:mibig-ace24a1c40
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-279/review-queue-001.tsv
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
  - naturalproductmech:mibig-ace24a1c40
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2788-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/miharamycin-a-2.yaml
  locator: 'complete file: chemical_structure, source_concepts, producer_organisms,
    biosynthetic_gene_clusters, classification and history'
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Complete current generated owner read; no record or native status edit.
  snapshot_sha256: d9f19da8b0dc2f398d24156ebe873296fa42553e65a9de4d4e613733f4bd2233
- evidence_id: support-2788-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json
  locator: /records/7/owner_document; /records/7/component_captures
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Accepted complete owner/history capture and empty selected component scope;
    raw capture is not a maintained-reader invocation.
  snapshot_sha256: 7d587c755373d7148002108737073753112d72744cddfc3b885327d4320222ed
- evidence_id: support-2788-source
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/support-prep/support-current279-assigned-source-reading-002.json
  locator: /contexts/2; /totals; /global_cautions
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Complete nine-frame assigned source context, all physical positive rows,
    fields and negative predicates personally read. Own primary credit is 21 rows/241
    fields across these five selected contexts; no BGC or Native row duplication.
  snapshot_sha256: 0b58c2ef1024c7af805abf237ee22c01a6ceb7548268fb73e57c600c02f2c6f4
- evidence_id: support-2788-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-target-input-plan-001.json
  locator: /records/7; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Actual original plan retains owner and direct-context inputs; global scope
    is 469 placements/70 paths, with no additional reviewed-target credit.
  snapshot_sha256: 9af820a19ec2457a4d2fb49a1d43086ac34ee266f4b058abf99f012d19473ddf
- evidence_id: support-2788-planaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/root-current279-input-plan-acceptance-001.json
  locator: /status; /accepted; /input_plan; /source_placements; /unique_source_paths
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: ROOT accepted the original current source plan.
  snapshot_sha256: 418448d2207f4547fb83474f27fee432e10648b65e6c48729524a9d120aa6ef4
- evidence_id: support-2788-notes
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /curation
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Current source notes preserve disjoint BGC/Support source readings and
    Native taxonomy/curation attribution without new primary proof.
  snapshot_sha256: 2e1145cabe812c1418e0c6d14b17caf32fe0e6a57c3b2683f2337d28f8f4d686
- evidence_id: support-2788-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/intakes-001/2788-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Actual canonical intake preserves this generated target, maintained owners
    and complete current input hash map.
  snapshot_sha256: 46a5a6a1664a9715c605aa6ea6f28c8b4e07a7fd6ce43a5934b4ad16c7e668c3
- evidence_id: support-2788-intakeaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/root-current279-intake-acceptance-001.json
  locator: /status; /accepted; /intake_summary; /records; /source_placements; /unique_source_paths
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: ROOT accepted all ten original canonical intakes; this scientific review
    uses only its assigned target.
  snapshot_sha256: 9347c539f301f7d6e9bf7cb6449143f33930afed1aec9fd05b960d1fb399af87
- evidence_id: support-2788-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles; /records/7/inchi; /records/7/comparisons; /records/7/atom_correspondence
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Each saved form has C20H30N10O9, 39 atoms, 42 bonds, one component and
    charge zero. The source has two carbonyls, one acid and one amide; the InChI-derived
    form retains the acid carbonyl and represents the amide as C(OH)=N. An exocyclic
    amino group on the aromatic aza-ring becomes an imino group while a ring nitrogen
    gains hydrogen. The original guanidine C=N persists. These saved tautomer-sensitive
    representations agree in normalized InChI/key but not canonical SMILES; the correspondence
    map remains empty. Eight saved comparison flags agree, including standard InChI,
    complete key, formula, charge and atom/bond counts. Both canonical isomeric and
    nonisomeric SMILES comparisons are false. The saved chirality-aware correspondence
    list is empty, complete_atom_count_match is false and full_graph_identity_established
    is false. Equal normalized identifiers do not establish a returned graph map,
    complete tautomer equivalence, natural-sample identity or experimental stereochemistry.
  snapshot_sha256: 3e1f6e3796bb1c289edf7dea5f0660e9f5917cfc6b690a115be7b583a9efe671
- evidence_id: support-2788-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/smiles/computed/potential_stereo;
    /records/7/inchi/computed/potential_stereo; /records/7/smiles/computed/atoms;
    /records/7/inchi/computed/atoms
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: All eight saved tetrahedral candidates are unspecified in both forms, with
    no specified atom configuration. The false stereo_complete flag is therefore retained.
    The source has one unspecified guanidine double-bond candidate; the InChI-derived
    form has three, including the imidic amide and relocated exocyclic aza-ring imine.
    The other Miharamycin A owner's six specified centres cannot fill these unknowns.
    No cross-owner or natural stereochemical identity is established.
  snapshot_sha256: 3e1f6e3796bb1c289edf7dea5f0660e9f5917cfc6b690a115be7b583a9efe671
- evidence_id: support-2788-motifs
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed/motifs; /records/7/smiles/computed/rings; /records/7/smiles/computed/bonds;
    /records/7/inchi/computed/motifs; /records/7/inchi/computed/rings; /records/7/inchi/computed/bonds
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: The source saturated six-ring [2,3,4,5,6,7] has five carbons and one oxygen;
    the adjacent five-ring [0,1,2,7,8] has four carbons and one oxygen and shares
    edge 2–7. They are a fused bicyclic oxygenated system, not two disjoint glycosides.
    Two further rings form a fused aromatic nitrogen heterocycle. Source acid C20
    and amide C24/N23 are separate; InChI amide-derived C14(OH32)=N26 and aza-ring
    C18=N23 illustrate the changed bond/proton placement. The N–OH group remains on
    the guanidine. No ester, N-acetyl or phosphorus motif is present.
  snapshot_sha256: 3e1f6e3796bb1c289edf7dea5f0660e9f5917cfc6b690a115be7b583a9efe671
- evidence_id: support-2788-molecularreading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/support-prep/support-current279-last-five-molecular-intake-reading-001.json
  locator: /records/2; /counts; /warnings
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Complete ten assigned saved forms and actual intakes retained; no molecular
    replay. Six undefined-stereo warnings remain globally unassigned.
  snapshot_sha256: 6a4d554686d146d01b4d071e5efe287492a6c7648cb2530c158701e1d3422f68
- evidence_id: support-2788-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Single original diagnostic exited zero, with exact command/streams and
    no retry. Process success is not a natural-identity result.
  snapshot_sha256: fbcf86328e60d26eac7a770199fc2054f192983e22eab011c0de17d494281984
- evidence_id: support-2788-diagaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /DATA; /execution
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: ROOT accepted the original saved diagnostic; no additional parse was performed
    for this review.
  snapshot_sha256: faeda5d6678e25fea4f2481b52d4fab578df595a6ff7b6b5d065d7824f582230
- evidence_id: support-2788-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-original-001.stderr
  locator: complete original stderr, six warning lines
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Six undefined-stereo warning lines are globally unassigned to records.
    They are not used as six record-specific defects.
  snapshot_sha256: 02c7027b4a2f575eff692bc02e20727a6cd814b2a504cc117a96b08f7c28703f
- evidence_id: support-2788-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/native-prep/native-current279-cached-taxonomy-reading-001.json
  locator: /context_interpretations/24; /whole_stanzas; /physical_negative_query_scopes/24
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Retain Streptomyces miharaensis (285483) as attributed, but keep the BGC0001956/MH534948.1/DOI10.1021/jacs.9b03021
    and BGC0002479/MN850873.1/PMID32167762 source compounds, locus bounds and ENTRY
    citations separate. The two selected Miharamycin A owners have distinct full InChIKeys
    QSPCQKVMQODSDN-UHFFFAOYSA-N and QSPCQKVMQODSDN-TVGXWQJGSA-N. Shared label, producer
    or first key block does not authorize identity merging or stereochemical transfer.
    Reciprocal selected-owner comparison inputs are separately declared, not additional
    BGC companion evidence; Miharamycin B remains a distinct compound.
  snapshot_sha256: 83a8fd84a6a63860446b23105de7dc89570492acd671888d45dcb815934e78dd
- evidence_id: support-2788-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/native-prep/native-current279-implemented-curation-scan-001.json
  locator: /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows;
    /implementation_scope; /input_ownership
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Native found no exact applicable implemented curation decision; lexical
    numerical/name hits do not establish applicability.
  snapshot_sha256: 9bfe54d89a2923e73dfaead325e3d8422a7960e4a418c37d6330d94744fcca59
  search_scope: Nine retained substantive tables, exact owner/source compound/BGC/full-key/occurrence/assay
    predicates; two reserved census-only tables excluded. No new source query or universal
    absence claim.
- evidence_id: support-2788-producerpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: complete retained method grading table
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: The method table distinguishes organism+cluster knockout support from cluster-only
    enzymatic or heterologous evidence, and preserves the unstated-method grade.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2788-stereopolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 165-172, FindMolChiralCenters(includeUnassigned=True, useLegacyImplementation=False)
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: The source stereo_complete predicate checks unassigned atom centres. It
    does not establish complete natural-product geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2788-filingpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295-306, choose_pathway
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Exactly one supported normalized pathway label selects a directory; multiple,
    empty or unsupported labels retain UNCLASSIFIED. All model labels are preserved
    separately.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2788-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/root-current279-five-gates-acceptance-001.json
  locator: /records; /selected_queue_rows; /full_native_checks_passed; /unavailable_checks;
    /scope
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Five local command results passed; full QC/OAK remain unavailable. Current
    producer, pathway, biosynthesis and stereo queue rows are scoped diagnostic leads,
    not automatic findings.
  snapshot_sha256: b9027a83706e568c056855b68f4afbf896601b0fbd78abe415472276b68401f4
- evidence_id: support-2788-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Saved mibig_compounds frame has 1 positive placements; complete rows or
    the complete empty predicate frame were read.
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "QSPCQKVMQODSDN-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2788-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Saved chebi_structures frame has 0 positive placements; complete rows or
    the complete empty predicate frame were read.
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "QSPCQKVMQODSDN-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2788-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Saved lotus_occurrences frame has 1 positive placements; complete rows
    or the complete empty predicate frame were read.
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "QSPCQKVMQODSDN-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2788-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame has 0 positive placements; complete
    rows or the complete empty predicate frame were read.
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "QSPCQKVMQODSDN-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2788-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Saved npclassifier frame has 1 positive placements; complete rows or the
    complete empty predicate frame were read.
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "QSPCQKVMQODSDN-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2788-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Saved pubchem_bioassay frame has 1 positive placements; complete rows or
    the complete empty predicate frame were read.
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "QSPCQKVMQODSDN-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2788-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Saved bindingdb_targets frame has 0 positive placements; complete rows
    or the complete empty predicate frame were read.
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "QSPCQKVMQODSDN-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2788-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame has 0 positive placements; complete
    rows or the complete empty predicate frame were read.
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: Explicit retained input only; predicate exact complete standard_inchi_key
    equality; query "QSPCQKVMQODSDN-UHFFFAOYSA-N". No cap, query replay or universal
    literature/biological absence claim.
- evidence_id: support-2788-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/24/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Saved chebi_origins frame has 0 positive placements; complete rows or the
    complete empty predicate frame were read.
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: Explicit retained input only; predicate exact chebi_id from exact
    full-key structure rows; query []. No cap, query replay or universal literature/biological
    absence claim.
- evidence_id: support-2788-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical line 2266, raw UTF-8 row SHA-256 6b47f2ad9899aa77495bf2637c79d16e212372ef6cefb4c61b4f5e15014c0440
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: BGC0001956:1, version 3, active, questionable quality and unknown completeness,
    grounds the label miharamycin A and pubchem:202591. The full key is QSPCQKVMQODSDN-UHFFFAOYSA-N.
    The reciprocal captured owner has the same label and first key block but full
    key QSPCQKVMQODSDN-TVGXWQJGSA-N and a different BGC. These explicit comparison
    inputs are not direct shared-BGC edges. Equal nonisomeric strings within each
    corresponding saved form support a limited connectivity comparison; they do not
    authorize an identity merge, source-grade transfer or stereochemical completion.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2788-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical line 7400, raw UTF-8 row SHA-256 09e35e90487e416fe469075ad554ef9733d846b986f31e73bb5b883a9efbcbd3
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: The single LOTUS row attributes this full-key structure to Streptomyces
    miharaensis, NCBITaxon:285483, with organism Q104853211 and structure Q82899820.
    Its occurrence status is preserved beside the producer assertion, with the shared-publication
    caveat. No production, activity or BGC-completeness upgrade follows from that
    match.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2788-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical line 2032, raw UTF-8 row SHA-256 729f2d11fa3a49c27f0ef59f785b187ddc693c01c5878bd221ca3839554cc491
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: The retained NPClassifier version npclassifier.gnps2.org@2026-09-07 has
    empty pathway, superclass and class lists and is_glycoside false. Empty pathway
    results correctly retain UNCLASSIFIED; source PKS remains separate. The saved
    fused oxygenated rings are structural observations and do not automatically replace
    the model's glycoside flag or establish a particular sugar identity. No mechanism,
    pathway, component, activity, target or related-record root is present.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2788-table-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical line 5732, raw UTF-8 row SHA-256 2993461b945d3493bcab1c07beedd8b89790d77b4ec3d2f42e112dde5bc4d6cc
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: All nine saved query frames were read. PubChem CID 202591 has one blank-AID
    sentinel, with no actual assay or biological measurement. Exact-key ChEBI, CyanoMetDB,
    BindingDB and AntibioticMech negatives are limited to the retained predicates.
    No inactivity, missing universal target or natural-product identity conclusion
    is drawn.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2788-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json
  locator: /records/7/owner_document/curation_history; /records/7/owner_document/source_concepts
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: DOI:10.1021/jacs.9b03021 is ENTRY-level MIBiG attribution. The LOTUS DOI:10.1021/JACS.9B03021
    differs only in case and is not independent publication evidence. The owner explicitly
    leaves publication independence unestablished. All three seeding events, 2026-09-10,
    2026-09-25 and 2026-10-13, are provenance for generation, not scientific verification.
    No paper or sequence was fetched.
  snapshot_sha256: 7d587c755373d7148002108737073753112d72744cddfc3b885327d4320222ed
- evidence_id: support-2788-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-target-input-plan-001.json
  locator: /records/7/complete_root_keys; /records/7/declared_mechanism_roots_literal;
    /records/7/component_paths; /records/7/literal_related_record_corpora
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Literal selected mechanism/pathway/component/target/activity/related roots
    are absent. This is not evidence of biological absence and assigns no maintained
    reader.
  snapshot_sha256: 9af820a19ec2457a4d2fb49a1d43086ac34ee266f4b058abf99f012d19473ddf
- evidence_id: support-2788-counterpart-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/miharamycin-a.yaml
  locator: 'complete file: chemical_structure, source_concepts, producer_organisms
    and biosynthetic_gene_clusters'
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: 'Explicit captured comparison owner only: identical label and first key
    block, distinct full key/stereochemistry and BGC authority; no merge, grade transfer
    or new reviewed-target credit.'
  snapshot_sha256: 2c745d7fc5ceaa4769f9277e1502726c6c15804f60290b3bb4e03ee75ab2596f
- evidence_id: support-2788-counterpart-molecular
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/smiles; /records/7/inchi; /records/7/comparisons;
    /records/7/atom_correspondence; /records/8/declared_structure; /records/8/smiles;
    /records/8/inchi; /records/8/comparisons; /records/8/atom_correspondence
  accessed_at: '2026-11-06T23:14:18.054965Z'
  support: supports
  summary: Both complete saved Miharamycin pairs were read. Corresponding per-form
    nonisomeric strings agree across owners, but full keys and 0 versus 6 specified
    tetrahedral centres differ. Within each owner the two canonical representations
    differ; no full graph identity or stereochemical transfer is established.
  snapshot_sha256: 3e1f6e3796bb1c289edf7dea5f0660e9f5917cfc6b690a115be7b583a9efe671
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-279/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json
  accessed_at: '2026-11-06T22:49:33.617178Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 8308433a377991dfadc0d4d7c27597f30359e4eebfeb69905f656033a6cd5d24
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-279/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json
  accessed_at: '2026-11-06T22:49:58.336243Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 548e62d3df6bcd986c517cf5074a61bb6587897d5b6010cb0b88967001e11659
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-279/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json
  accessed_at: '2026-11-06T22:50:17.857028Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-279/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json
  accessed_at: '2026-11-06T22:50:51.594218Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-279/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json
  accessed_at: '2026-11-06T22:51:03.290430Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 946aa09f038631dc68e741aa6b4fefa1d4f52995677f8f38e6078889449090fc
assessments:
- assessment_id: support-2788-identity-assessment
  area: identity
  topic: Exact retained compound grounding
  summary: BGC0001956:1, version 3, active, questionable quality and unknown completeness,
    grounds the label miharamycin A and pubchem:202591. The full key is QSPCQKVMQODSDN-UHFFFAOYSA-N.
    The reciprocal captured owner has the same label and first key block but full
    key QSPCQKVMQODSDN-TVGXWQJGSA-N and a different BGC. These explicit comparison
    inputs are not direct shared-BGC edges. Equal nonisomeric strings within each
    corresponding saved form support a limited connectivity comparison; they do not
    authorize an identity merge, source-grade transfer or stereochemical completion.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  evidence_ids:
  - support-2788-owner
  - support-2788-capture
  - support-2788-source
  - support-2788-plan
  - support-2788-intake
  - support-2788-curation
  - support-2788-table-mibig_compounds
  - support-2788-table-lotus_occurrences
  - support-2788-table-npclassifier
  - support-2788-table-pubchem_bioassay
  - support-2788-counterpart-owner
  - support-2788-counterpart-molecular
  dimensions:
  - name: standard_inchi_key
    definition: Complete key, not name or connectivity-prefix matching.
    value: QSPCQKVMQODSDN-UHFFFAOYSA-N
    evidence_ids:
    - support-2788-owner
    - support-2788-capture
    - support-2788-source
    - support-2788-plan
    - support-2788-intake
    - support-2788-curation
    - support-2788-table-mibig_compounds
    - support-2788-table-lotus_occurrences
    - support-2788-table-npclassifier
    - support-2788-table-pubchem_bioassay
    - support-2788-counterpart-owner
    - support-2788-counterpart-molecular
  - name: grounding_scope
    definition: Database grounding is distinct from natural-sample identity.
    value: BGC0001956:1, version 3, active, questionable quality and unknown completeness,
      grounds the label miharamycin A and pubchem:202591. The full key is QSPCQKVMQODSDN-UHFFFAOYSA-N.
      The reciprocal captured owner has the same label and first key block but full
      key QSPCQKVMQODSDN-TVGXWQJGSA-N and a different BGC. These explicit comparison
      inputs are not direct shared-BGC edges. Equal nonisomeric strings within each
      corresponding saved form support a limited connectivity comparison; they do
      not authorize an identity merge, source-grade transfer or stereochemical completion.
    evidence_ids:
    - support-2788-owner
    - support-2788-capture
    - support-2788-source
    - support-2788-plan
    - support-2788-intake
    - support-2788-curation
    - support-2788-table-mibig_compounds
    - support-2788-table-lotus_occurrences
    - support-2788-table-npclassifier
    - support-2788-table-pubchem_bioassay
    - support-2788-counterpart-owner
    - support-2788-counterpart-molecular
- assessment_id: support-2788-representation-assessment
  area: representation
  topic: Saved molecular forms, stereochemistry and motif scope
  summary: Each saved form has C20H30N10O9, 39 atoms, 42 bonds, one component and
    charge zero. The source has two carbonyls, one acid and one amide; the InChI-derived
    form retains the acid carbonyl and represents the amide as C(OH)=N. An exocyclic
    amino group on the aromatic aza-ring becomes an imino group while a ring nitrogen
    gains hydrogen. The original guanidine C=N persists. These saved tautomer-sensitive
    representations agree in normalized InChI/key but not canonical SMILES; the correspondence
    map remains empty. The source saturated six-ring [2,3,4,5,6,7] has five carbons
    and one oxygen; the adjacent five-ring [0,1,2,7,8] has four carbons and one oxygen
    and shares edge 2–7. They are a fused bicyclic oxygenated system, not two disjoint
    glycosides. Two further rings form a fused aromatic nitrogen heterocycle. Source
    acid C20 and amide C24/N23 are separate; InChI amide-derived C14(OH32)=N26 and
    aza-ring C18=N23 illustrate the changed bond/proton placement. The N–OH group
    remains on the guanidine. No ester, N-acetyl or phosphorus motif is present. Eight
    saved comparison flags agree, including standard InChI, complete key, formula,
    charge and atom/bond counts. Both canonical isomeric and nonisomeric SMILES comparisons
    are false. The saved chirality-aware correspondence list is empty, complete_atom_count_match
    is false and full_graph_identity_established is false. Equal normalized identifiers
    do not establish a returned graph map, complete tautomer equivalence, natural-sample
    identity or experimental stereochemistry.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  evidence_ids:
  - support-2788-data
  - support-2788-stereo
  - support-2788-motifs
  - support-2788-molecularreading
  - support-2788-execution
  - support-2788-diagaccept
  - support-2788-stereopolicy
  - support-2788-counterpart-owner
  - support-2788-counterpart-molecular
  dimensions:
  - name: stereochemistry_scope
    definition: Saved configurations and unspecified candidates remain distinct.
    value: All eight saved tetrahedral candidates are unspecified in both forms, with
      no specified atom configuration. The false stereo_complete flag is therefore
      retained. The source has one unspecified guanidine double-bond candidate; the
      InChI-derived form has three, including the imidic amide and relocated exocyclic
      aza-ring imine. The other Miharamycin A owner's six specified centres cannot
      fill these unknowns. No cross-owner or natural stereochemical identity is established.
    evidence_ids:
    - support-2788-data
    - support-2788-stereo
    - support-2788-motifs
    - support-2788-molecularreading
    - support-2788-execution
    - support-2788-diagaccept
    - support-2788-stereopolicy
    - support-2788-counterpart-owner
    - support-2788-counterpart-molecular
  - name: representation_correspondence
    definition: Limited saved calculation, without independent full/natural identity.
    value: Eight saved comparison flags agree, including standard InChI, complete
      key, formula, charge and atom/bond counts. Both canonical isomeric and nonisomeric
      SMILES comparisons are false. The saved chirality-aware correspondence list
      is empty, complete_atom_count_match is false and full_graph_identity_established
      is false. Equal normalized identifiers do not establish a returned graph map,
      complete tautomer equivalence, natural-sample identity or experimental stereochemistry.
    evidence_ids:
    - support-2788-data
    - support-2788-stereo
    - support-2788-motifs
    - support-2788-molecularreading
    - support-2788-execution
    - support-2788-diagaccept
    - support-2788-stereopolicy
    - support-2788-counterpart-owner
    - support-2788-counterpart-molecular
- assessment_id: support-2788-provenance-assessment
  area: provenance
  topic: Producer, taxon and compound-specific locus
  summary: Streptomyces miharaensis, NCBITaxon:285483, is a SOURCE_ASSERTION from
    BGC0001956. The matching LOTUS taxon is a separately attributed occurrence, not
    independent causal production evidence. The stronger locus evidence attached to
    BGC0002479 cannot be transferred to this source compound merely through its identical
    label or connectivity-prefix key. BGC0001956:1 retains MH534948.1 with no locus
    bounds or experimental methods stated, so CLUSTER_UNSTATED remains appropriate.
    The entry retains questionable quality and unknown completeness. Its PKS/Unknown
    source class does not prove a complete mechanism or sequence assignment, and the
    BGC0002479 coordinates and heterologous-expression claim belong to the other owner.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  evidence_ids:
  - support-2788-owner
  - support-2788-capture
  - support-2788-source
  - support-2788-taxonomy
  - support-2788-curation
  - support-2788-producerpolicy
  - support-2788-table-mibig_compounds
  dimensions:
  - name: taxon_scope
    definition: Cached naming does not establish current taxonomy or role transfer.
    value: Retain Streptomyces miharaensis (285483) as attributed, but keep the BGC0001956/MH534948.1/DOI10.1021/jacs.9b03021
      and BGC0002479/MN850873.1/PMID32167762 source compounds, locus bounds and ENTRY
      citations separate. The two selected Miharamycin A owners have distinct full
      InChIKeys QSPCQKVMQODSDN-UHFFFAOYSA-N and QSPCQKVMQODSDN-TVGXWQJGSA-N. Shared
      label, producer or first key block does not authorize identity merging or stereochemical
      transfer. Reciprocal selected-owner comparison inputs are separately declared,
      not additional BGC companion evidence; Miharamycin B remains a distinct compound.
    evidence_ids:
    - support-2788-owner
    - support-2788-capture
    - support-2788-source
    - support-2788-taxonomy
    - support-2788-curation
    - support-2788-producerpolicy
    - support-2788-table-mibig_compounds
  - name: producer_evidence
    definition: Source-organism evidence is separate from locus evidence.
    value: Streptomyces miharaensis, NCBITaxon:285483, is a SOURCE_ASSERTION from
      BGC0001956. The matching LOTUS taxon is a separately attributed occurrence,
      not independent causal production evidence. The stronger locus evidence attached
      to BGC0002479 cannot be transferred to this source compound merely through its
      identical label or connectivity-prefix key.
    evidence_ids:
    - support-2788-owner
    - support-2788-capture
    - support-2788-source
    - support-2788-taxonomy
    - support-2788-curation
    - support-2788-producerpolicy
    - support-2788-table-mibig_compounds
  - name: locus_evidence
    definition: Exact compound version, locus and methods delimit the claim.
    value: BGC0001956:1 retains MH534948.1 with no locus bounds or experimental methods
      stated, so CLUSTER_UNSTATED remains appropriate. The entry retains questionable
      quality and unknown completeness. Its PKS/Unknown source class does not prove
      a complete mechanism or sequence assignment, and the BGC0002479 coordinates
      and heterologous-expression claim belong to the other owner.
    evidence_ids:
    - support-2788-owner
    - support-2788-capture
    - support-2788-source
    - support-2788-taxonomy
    - support-2788-curation
    - support-2788-producerpolicy
    - support-2788-table-mibig_compounds
- assessment_id: support-2788-citations-assessment
  area: evidence
  topic: Reference grain and historical provenance
  summary: DOI:10.1021/jacs.9b03021 is ENTRY-level MIBiG attribution. The LOTUS DOI:10.1021/JACS.9B03021
    differs only in case and is not independent publication evidence. The owner explicitly
    leaves publication independence unestablished. All three seeding events, 2026-09-10,
    2026-09-25 and 2026-10-13, are provenance for generation, not scientific verification.
    No paper or sequence was fetched.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  evidence_ids:
  - support-2788-owner
  - support-2788-capture
  - support-2788-source
  - support-2788-history
  - support-2788-table-mibig_compounds
  - support-2788-table-lotus_occurrences
  - support-2788-table-npclassifier
  - support-2788-table-pubchem_bioassay
  dimensions:
  - name: citation_scope
    definition: Repeated attribution does not equal independent primary proof.
    value: DOI:10.1021/jacs.9b03021 is ENTRY-level MIBiG attribution. The LOTUS DOI:10.1021/JACS.9B03021
      differs only in case and is not independent publication evidence. The owner
      explicitly leaves publication independence unestablished. All three seeding
      events, 2026-09-10, 2026-09-25 and 2026-10-13, are provenance for generation,
      not scientific verification. No paper or sequence was fetched.
    evidence_ids:
    - support-2788-owner
    - support-2788-capture
    - support-2788-source
    - support-2788-history
    - support-2788-table-mibig_compounds
    - support-2788-table-lotus_occurrences
    - support-2788-table-npclassifier
    - support-2788-table-pubchem_bioassay
- assessment_id: support-2788-occurrence-assay-assessment
  area: evidence
  topic: Occurrence and retained assay limits
  summary: The single LOTUS row attributes this full-key structure to Streptomyces
    miharaensis, NCBITaxon:285483, with organism Q104853211 and structure Q82899820.
    Its occurrence status is preserved beside the producer assertion, with the shared-publication
    caveat. No production, activity or BGC-completeness upgrade follows from that
    match. All nine saved query frames were read. PubChem CID 202591 has one blank-AID
    sentinel, with no actual assay or biological measurement. Exact-key ChEBI, CyanoMetDB,
    BindingDB and AntibioticMech negatives are limited to the retained predicates.
    No inactivity, missing universal target or natural-product identity conclusion
    is drawn.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  evidence_ids:
  - support-2788-source
  - support-2788-taxonomy
  - support-2788-curation
  - support-2788-scope
  - support-2788-query-mibig_compounds
  - support-2788-query-chebi_structures
  - support-2788-query-lotus_occurrences
  - support-2788-query-cyanometdb_occurrences
  - support-2788-query-npclassifier
  - support-2788-query-pubchem_bioassay
  - support-2788-query-bindingdb_targets
  - support-2788-query-antibioticmech_inchikeys
  - support-2788-query-chebi_origins
  dimensions:
  - name: occurrence_scope
    definition: Occurrence alone does not establish biosynthesis.
    value: The single LOTUS row attributes this full-key structure to Streptomyces
      miharaensis, NCBITaxon:285483, with organism Q104853211 and structure Q82899820.
      Its occurrence status is preserved beside the producer assertion, with the shared-publication
      caveat. No production, activity or BGC-completeness upgrade follows from that
      match.
    evidence_ids:
    - support-2788-source
    - support-2788-taxonomy
    - support-2788-curation
    - support-2788-scope
    - support-2788-query-mibig_compounds
    - support-2788-query-chebi_structures
    - support-2788-query-lotus_occurrences
    - support-2788-query-cyanometdb_occurrences
    - support-2788-query-npclassifier
    - support-2788-query-pubchem_bioassay
    - support-2788-query-bindingdb_targets
    - support-2788-query-antibioticmech_inchikeys
    - support-2788-query-chebi_origins
  - name: assay_target_scope
    definition: Retained negatives are bounded predicates, not biological negatives.
    value: All nine saved query frames were read. PubChem CID 202591 has one blank-AID
      sentinel, with no actual assay or biological measurement. Exact-key ChEBI, CyanoMetDB,
      BindingDB and AntibioticMech negatives are limited to the retained predicates.
      No inactivity, missing universal target or natural-product identity conclusion
      is drawn.
    evidence_ids:
    - support-2788-source
    - support-2788-taxonomy
    - support-2788-curation
    - support-2788-scope
    - support-2788-query-mibig_compounds
    - support-2788-query-chebi_structures
    - support-2788-query-lotus_occurrences
    - support-2788-query-cyanometdb_occurrences
    - support-2788-query-npclassifier
    - support-2788-query-pubchem_bioassay
    - support-2788-query-bindingdb_targets
    - support-2788-query-antibioticmech_inchikeys
    - support-2788-query-chebi_origins
- assessment_id: support-2788-classification-assessment
  area: consistency
  topic: Classification, filing and literal mechanism scope
  summary: The retained NPClassifier version npclassifier.gnps2.org@2026-09-07 has
    empty pathway, superclass and class lists and is_glycoside false. Empty pathway
    results correctly retain UNCLASSIFIED; source PKS remains separate. The saved
    fused oxygenated rings are structural observations and do not automatically replace
    the model's glycoside flag or establish a particular sugar identity. No mechanism,
    pathway, component, activity, target or related-record root is present.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  evidence_ids:
  - support-2788-owner
  - support-2788-source
  - support-2788-filingpolicy
  - support-2788-motifs
  - support-2788-gates
  - support-2788-scope
  - support-2788-table-npclassifier
  dimensions:
  - name: classification_applicability
    definition: Source classes, model labels and graph observations remain distinct.
    value: The retained NPClassifier version npclassifier.gnps2.org@2026-09-07 has
      empty pathway, superclass and class lists and is_glycoside false. Empty pathway
      results correctly retain UNCLASSIFIED; source PKS remains separate. The saved
      fused oxygenated rings are structural observations and do not automatically
      replace the model's glycoside flag or establish a particular sugar identity.
      No mechanism, pathway, component, activity, target or related-record root is
      present.
    evidence_ids:
    - support-2788-owner
    - support-2788-source
    - support-2788-filingpolicy
    - support-2788-motifs
    - support-2788-gates
    - support-2788-scope
    - support-2788-table-npclassifier
- assessment_id: support-2788-completion-assessment
  area: completeness
  topic: Earned review and unavailable authority
  summary: The complete current owner and exact source rows were read, actual canonical
    intake fixed current ownership and input hashes, and the one original saved molecular
    computation was assessed without replay. Literal mechanism, pathway, component,
    target, activity and related-record roots are absent; no maintained reader is
    assigned. Five local native commands passed, but full QC, complete OAK checks
    and external primary verification remain unavailable. Completion is partial; native
    SEEDED status and generated records remain unchanged.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-ace24a1c40
  evidence_ids:
  - support-2788-intake
  - support-2788-intakeaccept
  - support-2788-plan
  - support-2788-planaccept
  - support-2788-notes
  - support-2788-gates
  - support-2788-data
  - support-2788-execution
  - support-2788-diagaccept
  - support-2788-scope
  dimensions:
  - name: review_completion
    definition: Scientific review does not promote native status or claim full external
      QC.
    value: The complete current owner and exact source rows were read, actual canonical
      intake fixed current ownership and input hashes, and the one original saved
      molecular computation was assessed without replay. Literal mechanism, pathway,
      component, target, activity and related-record roots are absent; no maintained
      reader is assigned. Five local native commands passed, but full QC, complete
      OAK checks and external primary verification remain unavailable. Completion
      is partial; native SEEDED status and generated records remain unchanged.
    evidence_ids:
    - support-2788-intake
    - support-2788-intakeaccept
    - support-2788-plan
    - support-2788-planaccept
    - support-2788-notes
    - support-2788-gates
    - support-2788-data
    - support-2788-execution
    - support-2788-diagaccept
    - support-2788-scope
findings: []
actions: []
limitations:
- Primary papers, spectra, sequences, live taxonomy and natural-product identity were
  not independently verified. Full QC, complete OAK and external primary checks remain
  unavailable.
- Eight saved comparison flags agree, including standard InChI, complete key, formula,
  charge and atom/bond counts. Both canonical isomeric and nonisomeric SMILES comparisons
  are false. The saved chirality-aware correspondence list is empty, complete_atom_count_match
  is false and full_graph_identity_established is false. Equal normalized identifiers
  do not establish a returned graph map, complete tautomer equivalence, natural-sample
  identity or experimental stereochemistry. All eight saved tetrahedral candidates
  are unspecified in both forms, with no specified atom configuration. The false stereo_complete
  flag is therefore retained. The source has one unspecified guanidine double-bond
  candidate; the InChI-derived form has three, including the imidic amide and relocated
  exocyclic aza-ring imine. The other Miharamycin A owner's six specified centres
  cannot fill these unknowns. No cross-owner or natural stereochemical identity is
  established.
- Six undefined-stereo warning lines are globally unassigned. Exact-key negatives
  and literal root absence do not establish inactivity or universal absence.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh current 279 scientific judgments use current retained owner/source/intake/diagnostic
  evidence; earlier batches supply interface logic only.
- No generated record, source inventory, native status or campaign artifact was edited.
  No query, molecular parse, target invocation or outbound request occurred in this
  lane.
- ROOT appends five actual local native checks and three required unavailable checks.
  No maintained-reader check belongs to these zero-reader targets.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-279
```
