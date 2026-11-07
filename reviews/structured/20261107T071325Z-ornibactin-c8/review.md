# Local evidence review: ornibactin C8

- Review: 20261107T071325Z-ornibactin-c8
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T06:39:53.601267Z
- Finished UTC: 2026-11-07T07:13:25.899608Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Ornibactin C8 retains its distinct exact-key source identity, with six unresolved atom stereocentres and four amide/imidic representation changes. Source-characterized producer and demonstrated locus claims remain attributed. No material local defect was established; the review is a qualified partial pass.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2847; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-92a1e3d468 | data/natural_products/unclassified/ornibactin-c8.yaml | generated | ornibactin C8 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-92a1e3d468 | Both stored forms parsed with declared normalized key and formula agreement. Both canonical SMILES comparisons are false; the chirality-aware map is empty and complete_atom_count_match/full_graph_identity_established remain false. |
| strict_ten | passed | True | naturalproductmech:mibig-92a1e3d468 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-92a1e3d468 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-92a1e3d468 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-92a1e3d468 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-92a1e3d468 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-92a1e3d468 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-92a1e3d468 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-92a1e3d468 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained compound grounding

identity: supported. Targets: naturalproductmech:mibig-92a1e3d468.

The owner is BGC0002569 version 3 compound index 1, NPAtlas NPA015051, full key NJIOFEXYZOVVKA-UHFFFAOYSA-N and formula C30H56N8O13. Direct C4/C6/C8 shared-BGC contexts have separate full keys. The label and common cluster do not merge identities or transfer natural stereochemistry.

### Saved molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-92a1e3d468.

Both saved forms are neutral C30H56N8O13 with 51 atoms, 50 bonds, one acyclic component and no aromatic atoms or metal. SMILES has seven carbonyls and six strict amides; the InChI-derived form has three carbonyls and two strict amides plus four C(OH)=N sites. The two N-hydroxy acyl carbonyls remain, while four secondary amides change representation. This explains the canonical-SMILES disagreement without independently proving natural identity or choosing a preferred biological tautomer. In SMILES the hydroxyacyl chain is C0–C7 including carbonyl C7, with OH at C5/O50. N-hydroxy acyl groups are C7(=O8)–N9–O49 and formyl C37(=O38)–N36–O39. The neutral acid is C19(=O20)–O21H, and N47/N48 are free primary amines. The InChI form retains the acid C29/O47/O48 and four imidic motif sites; no complete atom mapping is asserted. Neither form has an ester, N-acetyl motif, saturated C5O candidate sugar or phosphorus. N-hydroxy groups alone establish no metal affinity, complex or assay result. The two actually parsed C6/C8 owners differ by two methylene units in their hydroxyacyl chains: six versus eight carbons including the carbonyl, with a C2H4 formula increment. Both have the same counted amide/imidic pattern and six unknown atom centres. Their distinct full keys and unknown stereo remain separate; no biosynthetic conversion, metal binding or unparsed C4 equivalence is inferred. Both canonical SMILES comparisons are false; the chirality-aware map is empty and complete_atom_count_match/full_graph_identity_established remain false. Normalized identifiers, formula agreement and local parsing do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry or primary biological validation.

### Compound-specific producer, locus and taxon

provenance: supported. Targets: naturalproductmech:mibig-92a1e3d468.

Burkholderia cenocepacia J2315, NCBITaxon:216591, remains the BGC_CHARACTERIZED producer. This strain-qualified source claim is separate from the genus/species LOTUS occurrences and is not newly verified experimentally. AM747720.1:1846454–1876827 remains CLUSTER_DEMONSTRATED from retained Knock-out studies and Gene expression correlated with compound production. BGC0002569 version 3 is active, questionable quality and unknown completeness. These source methods support the recorded grade without establishing a complete enzyme-by-enzyme pathway.

### Citation grain and retained history

evidence: supported. Targets: naturalproductmech:mibig-92a1e3d468.

PMID:16672617 has ENTRY scope. The LOTUS DOI pointers remain occurrence citations, not newly read primary bodies; shared entry and congener citations do not add independent experiments. Two seed-history events document processing and retain unresolved source questions.

### Occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-92a1e3d468.

LOTUS rows 6008/6009 retain Pseudomonas, NCBITaxon:286, DOI:10.1002/JLAC.199319930108 and Burkholderia cenocepacia, NCBITaxon:95486, DOI:10.1128/JB.188.10.3631-3644.2006, both structure Q77562412. Species occurrence remains distinct from strain J2315; publication independence was not established. All six other saved named frames are bounded negatives: ChEBI structures and their conditional origins, CyanoMetDB, PubChem, BindingDB and AntibioticMech. No actual AID or blank AID marker exists in this owner scope. No activity, target, inactivity or metal binding follows from those negatives or the compound name.

### Source classes, model labels and filing

consistency: supported. Targets: naturalproductmech:mibig-92a1e3d468.

MIBiG NRPS and Type I are source BGC class and subclass. The exact NPClassifier row has empty pathway, superclass and class labels, and is_glycoside:false, model npclassifier.gnps2.org@2026-09-07. Empty model results retain UNCLASSIFIED under choose_pathway; they do not erase source NRPS provenance or constitute a structure defect.

### Earned work and unavailable authority

completeness: supported. Targets: naturalproductmech:mibig-92a1e3d468.

The complete selected owner, current source/intake and both saved molecular forms were read. The complete selected owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary, related_records or component root. No maintained reader is applicable to this owner. This bounded record absence is not a claim of absent biology; no selected owner in batch 285 requires a maintained reader. The positive unselected o-orsellinic-acid context does not transfer into these owners. No additional material local defect was established in this bounded scope. Existing OPEN discussions are not closed. Five local gates pass; full QC, complete OAK and fresh primary/external verification remain unavailable. Completion is partial and native SEEDED status remains unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2847-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/ornibactin-c8.yaml; complete file: identifier, label, chemical_structure, source_concepts, producer/locus/occurrence fields, discussions, classification and curation_history | supports | Complete selected generated owner; source assertions and absence remain attributed. |
| support-2847-capture | /private/tmp/npm-review-work/shared-next-batch285/owner-capture-DATA-001.json; /records/6/owner_document | supports | Complete accepted current owner capture, including discussions and source concepts. |
| support-2847-source | /private/tmp/npm-review-work/shared-next-batch285-tentative/support-prep/support-current285-assigned-source-reading-001.json; /contexts/1; /selected_counts; /companion_counts; /global_cautions | supports | Own disjoint selected reading covers 20 named row placements, 230 fields, 45 frames, 28 negative frames and 11 histories. The two Outovirin blank AID sentinels are not assay observations. |
| support-2847-plan | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-target-input-plan-001.json; /records/6; /source_placement_count; /unique_source_path_count | supports | Accepted 463-placement/60-path plan; this owner has 46 actual inputs. Direct companions are exact scoped inputs. |
| support-2847-planaccept | /private/tmp/npm-review-work/shared-next-batch285/root-current285-source-plan-acceptance-001.json; /status; /accepted; /plan | supports | ROOT accepted the original current source plan. |
| support-2847-notes | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /curation | supports | Current disjoint BGC 95 plus Support 20 named rows total 115 rows and 1,145 fields; Native secondary readings add no primary-row credit. |
| support-2847-intake | /private/tmp/npm-review-work/shared-next-batch285/intakes-001/2847-inspect-001.json; /status; /source; /targets | supports | Actual canonical intake fixes the current source hashes, generated target and maintained owners. |
| support-2847-intakeaccept | /private/tmp/npm-review-work/shared-next-batch285/root-current285-intake-acceptance-001.json; /status; /accepted; /summary | supports | All ten original intakes passed with empty stderr; no reruns. |
| support-2847-data | /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles; /records/6/inchi; /records/6/comparisons; /records/6/atom_correspondence; /records/6/literal_InChI_layers; /records/6/formula_comparison_scope | supports | Both saved forms are neutral C30H56N8O13 with 51 atoms, 50 bonds, one acyclic component and no aromatic atoms or metal. SMILES has seven carbonyls and six strict amides; the InChI-derived form has three carbonyls and two strict amides plus four C(OH)=N sites. The two N-hydroxy acyl carbonyls remain, while four secondary amides change representation. This explains the canonical-SMILES disagreement without independently proving natural identity or choosing a preferred biological tautomer. Both canonical SMILES comparisons are false; the chirality-aware map is empty and complete_atom_count_match/full_graph_identity_established remain false. |
| support-2847-stereo | /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed/atoms; /records/6/smiles/computed/bonds; /records/6/smiles/computed/potential_stereo; /records/6/inchi/computed/atoms; /records/6/inchi/computed/bonds; /records/6/inchi/computed/potential_stereo | supports | Both encodings have six unspecified tetrahedral candidates and no assigned tetrahedral centres. The InChI-derived form adds four unspecified potential C=N sites at its imidic bonds. The source false stereo_complete flag is consistent with unresolved atom centres; these added candidate doubles do not supply natural geometries or four new experimental ambiguities. |
| support-2847-motifs | /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed/atoms; /records/6/smiles/computed/bonds; /records/6/smiles/computed/rings; /records/6/smiles/computed/motifs; /records/6/inchi/computed/atoms; /records/6/inchi/computed/bonds; /records/6/inchi/computed/rings; /records/6/inchi/computed/motifs | supports | In SMILES the hydroxyacyl chain is C0–C7 including carbonyl C7, with OH at C5/O50. N-hydroxy acyl groups are C7(=O8)–N9–O49 and formyl C37(=O38)–N36–O39. The neutral acid is C19(=O20)–O21H, and N47/N48 are free primary amines. The InChI form retains the acid C29/O47/O48 and four imidic motif sites; no complete atom mapping is asserted. Neither form has an ester, N-acetyl motif, saturated C5O candidate sugar or phosphorus. N-hydroxy groups alone establish no metal affinity, complex or assay result. |
| support-2847-molecularreading | /private/tmp/npm-review-work/shared-next-batch285-tentative/support-prep/support-current285-last-five-molecular-intake-reading-001.json; /records/1; /counts; /interpretations/2847; /warnings | supports | Personally read all ten saved forms: 430 atoms, 446 bonds, 30 ring rows and 85 potential-stereo entries. No new parse. |
| support-2847-execution | /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /retries; /stderr | supports | One original stored-form diagnostic exited zero without retry. |
| support-2847-diagaccept | /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /warnings_scope | supports | ROOT accepted the original diagnostic; scientific identity remains bounded. |
| support-2847-stderr | /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-original-001.stderr; complete original stderr stream; twelve warning lines and their exact ordering | supports | The original diagnostic has twelve omitted-undefined-stereo warning lines. They remain global and unassigned to any owner or form; no warning-to-record attribution is inferred. |
| support-2847-taxonomy | /private/tmp/npm-review-work/shared-next-batch285-tentative/native-prep/native-current285-cached-taxonomy-reading-003.json; /context_interpretations/9; /physical_negative_query_scopes/9; /whole_stanzas | supports | Attributed Native cached-name reading: NCBITaxon:216591 = Burkholderia cenocepacia J2315, NCBITaxon:286 = Pseudomonas, NCBITaxon:95486 = Burkholderia cenocepacia. These retained labels establish no fresh rank, lineage, strain equivalence or experimental producer validation. Source producer and occurrence roles remain distinct; no exact merge or nonorganism decision applies to this context. |
| support-2847-curation | /private/tmp/npm-review-work/shared-next-batch285-tentative/native-prep/native-current285-implemented-curation-scan-001.json; /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows; /interpretation | supports | Nine substantive curation tables have no exact applicable correction. All exact predicates are negative for these five owners; lexical matches are not applied corrections. |
| support-2847-producerpolicy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; complete method grading table | supports | Knockout supports organism and locus; heterologous expression and enzymatic assays support locus only. Source method labels remain attributed rather than newly inspected experiments. |
| support-2847-stereopolicy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142-173 structure_fields; atom-centre predicate lines 165-172 | supports | stereo_complete derives from FindMolChiralCenters and unknown atom tags; it does not certify full E/Z or natural identity. |
| support-2847-filingpolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306 choose_pathway | supports | One supported normalized model pathway chooses filing; multiple, none or unsupported results retain UNCLASSIFIED. |
| support-2847-gates | /private/tmp/npm-review-work/shared-next-batch285/root-current285-five-gates-acceptance-001.json; /commands; /selected_queue_rows; /unavailable_required_gates; /all_native_gates_passed | supports | All five local gates pass; complete QC/OAK remain unavailable and all_native_gates_passed is false. Queue leads are not automatic scientific findings. |
| support-2847-history | /private/tmp/npm-review-work/shared-next-batch285/owner-capture-DATA-001.json; /records/6/owner_document/curation_history; /records/6/owner_document/source_concepts | supports | PMID:16672617 has ENTRY scope. The LOTUS DOI pointers remain occurrence citations, not newly read primary bodies; shared entry and congener citations do not add independent experiments. Two seed-history events document processing and retain unresolved source questions. |
| support-2847-scope | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-target-input-plan-001.json; /records/6/complete_root_keys; /records/6/declared_mechanism_roots_literal; /records/6/component_paths; /records/6/complete_raw_mechanism_sections | supports | The complete selected owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary, related_records or component root. No maintained reader is applicable to this owner. This bounded record absence is not a claim of absent biology; no selected owner in batch 285 requires a maintained reader. The positive unselected o-orsellinic-acid context does not transfer into these owners. |
| support-2847-comparison | /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-DATA-001.json; /records/5/smiles/computed/formula; /records/5/smiles/computed/atoms; /records/5/smiles/computed/bonds; /records/5/smiles/computed/canonical_isomeric_smiles; /records/5/inchi/computed/formula; /records/5/inchi/computed/atoms; /records/5/inchi/computed/bonds; /records/5/inchi/computed/canonical_isomeric_smiles; /records/6/smiles/computed/formula; /records/6/smiles/computed/atoms; /records/6/smiles/computed/bonds; /records/6/smiles/computed/canonical_isomeric_smiles; /records/6/inchi/computed/formula; /records/6/inchi/computed/atoms; /records/6/inchi/computed/bonds; /records/6/inchi/computed/canonical_isomeric_smiles | supports | The two actually parsed C6/C8 owners differ by two methylene units in their hydroxyacyl chains: six versus eight carbons including the carbonyl, with a C2H4 formula increment. Both have the same counted amide/imidic pattern and six unknown atom centres. Their distinct full keys and unknown stereo remain separate; no biosynthetic conversion, metal binding or unparsed C4 equivalence is inferred. |
| support-2847-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame with 1 positive placements. |
| support-2847-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical line 3264, raw UTF-8 row SHA-256 49f90f0a92bb90d0012d177fbcda28a23c26706746e7d452bea2ad905ae83dd3 | supports | The owner is BGC0002569 version 3 compound index 1, NPAtlas NPA015051, full key NJIOFEXYZOVVKA-UHFFFAOYSA-N and formula C30H56N8O13. Direct C4/C6/C8 shared-BGC contexts have separate full keys. The label and common cluster do not merge identities or transfer natural stereochemistry. Burkholderia cenocepacia J2315, NCBITaxon:216591, remains the BGC_CHARACTERIZED producer. This strain-qualified source claim is separate from the genus/species LOTUS occurrences and is not newly verified experimentally. AM747720.1:1846454–1876827 remains CLUSTER_DEMONSTRATED from retained Knock-out studies and Gene expression correlated with compound production. BGC0002569 version 3 is active, questionable quality and unknown completeness. These source methods support the recorded grade without establishing a complete enzyme-by-enzyme pathway. |
| support-2847-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame with 0 positive placements. |
| support-2847-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame with 2 positive placements. |
| support-2847-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical line 6008, raw UTF-8 row SHA-256 6c72884959835d573c396bc0db51ff1aa417a62c9dade41c0c9e6cea291492f8; physical line 6009, raw UTF-8 row SHA-256 3f55de23c52144e327f6072ab6ce71baad8240c92f6e95e91504a15a8bc30c2a | supports | LOTUS rows 6008/6009 retain Pseudomonas, NCBITaxon:286, DOI:10.1002/JLAC.199319930108 and Burkholderia cenocepacia, NCBITaxon:95486, DOI:10.1128/JB.188.10.3631-3644.2006, both structure Q77562412. Species occurrence remains distinct from strain J2315; publication independence was not established. |
| support-2847-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame with 0 positive placements. |
| support-2847-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame with 1 positive placements. |
| support-2847-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical line 1612, raw UTF-8 row SHA-256 178a4b6e4f3fd6943f032e76ced7bcb65bacdece6806637669a4543e18c35f15 | supports | MIBiG NRPS and Type I are source BGC class and subclass. The exact NPClassifier row has empty pathway, superclass and class labels, and is_glycoside:false, model npclassifier.gnps2.org@2026-09-07. Empty model results retain UNCLASSIFIED under choose_pathway; they do not erase source NRPS provenance or constitute a structure defect. |
| support-2847-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame with 0 positive placements. |
| support-2847-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame with 0 positive placements. |
| support-2847-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame with 0 positive placements. |
| support-2847-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame with 0 positive placements. |
| support-2847-companion-0 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/ornibactin-c4.yaml; complete file: identifier, chemical_structure, source_concepts, biosynthetic_gene_clusters and curation_history | supports | Exact captured direct owned-BGC companion, with distinct full key and context-only attribution. No congener identity, stereochemistry, producer grade or activity is transferred; only the explicitly linked saved-form comparison is used. |
| support-2847-companion-1 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/ornibactin-c6.yaml; complete file: identifier, chemical_structure, source_concepts, biosynthetic_gene_clusters and curation_history | supports | Exact captured direct owned-BGC companion, with distinct full key and context-only attribution. No congener identity, stereochemistry, producer grade or activity is transferred; only the explicitly linked saved-form comparison is used. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-285/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-285/native-current285-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-285/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-285/native-current285-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-285/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-285/native-current285-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-285/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-285/native-current285-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-285/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-285/native-current285-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Normalized identifiers, formula agreement and local parsing do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry or primary biological validation.
- Both canonical SMILES comparisons are false; the chirality-aware map is empty and complete_atom_count_match/full_graph_identity_established remain false. Both encodings have six unspecified tetrahedral candidates and no assigned tetrahedral centres. The InChI-derived form adds four unspecified potential C=N sites at its imidic bonds. The source false stereo_complete flag is consistent with unresolved atom centres; these added candidate doubles do not supply natural geometries or four new experimental ambiguities.
- The original diagnostic has twelve omitted-undefined-stereo warning lines. They remain global and unassigned to any owner or form; no warning-to-record attribution is inferred.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK remain unavailable. All database assertions retain their original grain, grades and unresolved questions.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh current 285 evidence and judgments; prior batches supply interface logic only.
- No source record, native status or history was changed; no source query, molecular parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual local gate checks and three required unavailable checks. No maintained-reader check applies to these five negative-root owners.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T071325Z-ornibactin-c8
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: ornibactin C8'
started_at: '2026-11-07T06:39:53.601267Z'
finished_at: '2026-11-07T07:13:25.899608Z'
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
summary: Ornibactin C8 retains its distinct exact-key source identity, with six unresolved
  atom stereocentres and four amide/imidic representation changes. Source-characterized
  producer and demonstrated locus claims remain attributed. No material local defect
  was established; the review is a qualified partial pass.
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
  - path: data/natural_products/unclassified/ornibactin-c4.yaml
    sha256: d406d92134aa25a7d4e2ba01de8ccc6087ff64256a1ba0b9c2d018e7e01b7c1f
    role: context
  - path: data/natural_products/unclassified/ornibactin-c6.yaml
    sha256: 9092e63aa57f62359c78ff40b2523c14ddfa45c8e4d64e9193673df9a32cdd3c
    role: context
  - path: data/natural_products/unclassified/ornibactin-c8.yaml
    sha256: 9a4b403096e77b131305e0d142e8b79795f1e3c92c21a6a3205eb3c3a53eb142
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
  selection: Campaign path order 2847; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-92a1e3d468
targets:
- target_id: naturalproductmech:mibig-92a1e3d468
  path: data/natural_products/unclassified/ornibactin-c8.yaml
  label: ornibactin C8
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
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Retained exclusion-table diagnostic context captured for every review; applicable
      exact assay exclusions and biological rows must be derived from actual retained
      inventory, not file presence.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/unresolved_taxa.tsv
    role: Retained unresolved-taxon diagnostic context used by the bounded curation
      scan; no fresh taxonomy, forward-merge decision or producer confirmation.
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnose285-001.py
    2b8d1be7aac3c9455b693b03752576a9cd91d7db058478af6e59e500f14a9e15 9042e782394e35188f0a4053f6cb76565baa3a45c799b52949b8d6d21a1ea9ad
    7002393dc6a8ac9d1948f6d779aba71034a25557bc6f2c05bc53f6a1e637375f
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed with declared normalized key and formula agreement.
    Both canonical SMILES comparisons are false; the chirality-aware map is empty
    and complete_atom_count_match/full_graph_identity_established remain false.
  scope_note: Both saved forms are neutral C30H56N8O13 with 51 atoms, 50 bonds, one
    acyclic component and no aromatic atoms or metal. SMILES has seven carbonyls and
    six strict amides; the InChI-derived form has three carbonyls and two strict amides
    plus four C(OH)=N sites. The two N-hydroxy acyl carbonyls remain, while four secondary
    amides change representation. This explains the canonical-SMILES disagreement
    without independently proving natural identity or choosing a preferred biological
    tautomer. Both encodings have six unspecified tetrahedral candidates and no assigned
    tetrahedral centres. The InChI-derived form adds four unspecified potential C=N
    sites at its imidic bonds. The source false stereo_complete flag is consistent
    with unresolved atom centres; these added candidate doubles do not supply natural
    geometries or four new experimental ambiguities. The original diagnostic has twelve
    omitted-undefined-stereo warning lines. They remain global and unassigned to any
    owner or form; no warning-to-record attribution is inferred.
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  evidence_ids:
  - support-2847-data
  - support-2847-execution
  - support-2847-diagaccept
  - support-2847-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  command: just validate-strict data/natural_products/unclassified/orcinol.yaml data/natural_products/unclassified/orfamide-a.yaml
    data/natural_products/unclassified/orfamide-b.yaml data/natural_products/unclassified/orfamide-c.yaml
    data/natural_products/unclassified/ornibactin-c4.yaml data/natural_products/unclassified/ornibactin-c6.yaml
    data/natural_products/unclassified/ornibactin-c8.yaml data/natural_products/unclassified/outovirin-a.yaml
    data/natural_products/unclassified/outovirin-c.yaml data/natural_products/unclassified/oxazolomycin.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-285/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-92a1e3d468
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-285/validate-all-001.tsv
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
  - naturalproductmech:mibig-92a1e3d468
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
  - naturalproductmech:mibig-92a1e3d468
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
  - naturalproductmech:mibig-92a1e3d468
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-285/review-queue-001.tsv
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
  - naturalproductmech:mibig-92a1e3d468
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2847-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/ornibactin-c8.yaml
  locator: 'complete file: identifier, label, chemical_structure, source_concepts,
    producer/locus/occurrence fields, discussions, classification and curation_history'
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete selected generated owner; source assertions and absence remain
    attributed.
  snapshot_sha256: 9a4b403096e77b131305e0d142e8b79795f1e3c92c21a6a3205eb3c3a53eb142
- evidence_id: support-2847-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch285/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete accepted current owner capture, including discussions and source
    concepts.
  snapshot_sha256: 9042e782394e35188f0a4053f6cb76565baa3a45c799b52949b8d6d21a1ea9ad
- evidence_id: support-2847-source
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/support-prep/support-current285-assigned-source-reading-001.json
  locator: /contexts/1; /selected_counts; /companion_counts; /global_cautions
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Own disjoint selected reading covers 20 named row placements, 230 fields,
    45 frames, 28 negative frames and 11 histories. The two Outovirin blank AID sentinels
    are not assay observations.
  snapshot_sha256: 483f353cb66f9afacd7679eeb3bc283ba54f13b692f26087afb30321aad25275
- evidence_id: support-2847-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-target-input-plan-001.json
  locator: /records/6; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Accepted 463-placement/60-path plan; this owner has 46 actual inputs. Direct
    companions are exact scoped inputs.
  snapshot_sha256: 8e6577535a621797ed5bb16973a653730dc5a2ca3fccfe1e0d486e4799d749b4
- evidence_id: support-2847-planaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/root-current285-source-plan-acceptance-001.json
  locator: /status; /accepted; /plan
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: ROOT accepted the original current source plan.
  snapshot_sha256: af32e4aaaefd19568801675917fe35bfcda99608f2117b1b5825e7ba25a95cef
- evidence_id: support-2847-notes
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /curation
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Current disjoint BGC 95 plus Support 20 named rows total 115 rows and 1,145
    fields; Native secondary readings add no primary-row credit.
  snapshot_sha256: 3f27e9e59b4511f94e4ba492b5218c564c727e02bbcccc13c29544a22c1b4b94
- evidence_id: support-2847-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/intakes-001/2847-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Actual canonical intake fixes the current source hashes, generated target
    and maintained owners.
  snapshot_sha256: 1bb4deb478f4cc142ea393ba0c1b2b3ab8c43cc2188a07e99e0544950693f9e2
- evidence_id: support-2847-intakeaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/root-current285-intake-acceptance-001.json
  locator: /status; /accepted; /summary
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: All ten original intakes passed with empty stderr; no reruns.
  snapshot_sha256: 0961a623db89338e99a2cf362f885b15e0e3a64a1370993faef05503ad3d1d10
- evidence_id: support-2847-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles; /records/6/inchi; /records/6/comparisons; /records/6/atom_correspondence;
    /records/6/literal_InChI_layers; /records/6/formula_comparison_scope
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Both saved forms are neutral C30H56N8O13 with 51 atoms, 50 bonds, one acyclic
    component and no aromatic atoms or metal. SMILES has seven carbonyls and six strict
    amides; the InChI-derived form has three carbonyls and two strict amides plus
    four C(OH)=N sites. The two N-hydroxy acyl carbonyls remain, while four secondary
    amides change representation. This explains the canonical-SMILES disagreement
    without independently proving natural identity or choosing a preferred biological
    tautomer. Both canonical SMILES comparisons are false; the chirality-aware map
    is empty and complete_atom_count_match/full_graph_identity_established remain
    false.
  snapshot_sha256: 381563a9a0778e2c0ec460c24ebc54f65bf72366d3285e62d8dd0778e05f9cab
- evidence_id: support-2847-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed/atoms; /records/6/smiles/computed/bonds; /records/6/smiles/computed/potential_stereo;
    /records/6/inchi/computed/atoms; /records/6/inchi/computed/bonds; /records/6/inchi/computed/potential_stereo
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Both encodings have six unspecified tetrahedral candidates and no assigned
    tetrahedral centres. The InChI-derived form adds four unspecified potential C=N
    sites at its imidic bonds. The source false stereo_complete flag is consistent
    with unresolved atom centres; these added candidate doubles do not supply natural
    geometries or four new experimental ambiguities.
  snapshot_sha256: 381563a9a0778e2c0ec460c24ebc54f65bf72366d3285e62d8dd0778e05f9cab
- evidence_id: support-2847-motifs
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed/atoms; /records/6/smiles/computed/bonds; /records/6/smiles/computed/rings;
    /records/6/smiles/computed/motifs; /records/6/inchi/computed/atoms; /records/6/inchi/computed/bonds;
    /records/6/inchi/computed/rings; /records/6/inchi/computed/motifs
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: In SMILES the hydroxyacyl chain is C0–C7 including carbonyl C7, with OH
    at C5/O50. N-hydroxy acyl groups are C7(=O8)–N9–O49 and formyl C37(=O38)–N36–O39.
    The neutral acid is C19(=O20)–O21H, and N47/N48 are free primary amines. The InChI
    form retains the acid C29/O47/O48 and four imidic motif sites; no complete atom
    mapping is asserted. Neither form has an ester, N-acetyl motif, saturated C5O
    candidate sugar or phosphorus. N-hydroxy groups alone establish no metal affinity,
    complex or assay result.
  snapshot_sha256: 381563a9a0778e2c0ec460c24ebc54f65bf72366d3285e62d8dd0778e05f9cab
- evidence_id: support-2847-molecularreading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/support-prep/support-current285-last-five-molecular-intake-reading-001.json
  locator: /records/1; /counts; /interpretations/2847; /warnings
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: 'Personally read all ten saved forms: 430 atoms, 446 bonds, 30 ring rows
    and 85 potential-stereo entries. No new parse.'
  snapshot_sha256: 42619405bd79fdec906718eef3b57a9fdcdc53bfa5a0009dd01045aa473663b9
- evidence_id: support-2847-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /retries; /stderr
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: One original stored-form diagnostic exited zero without retry.
  snapshot_sha256: a283410764019d05a4cf85a4c19e63604743b740015f54569d58fabde7960ed1
- evidence_id: support-2847-diagaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /warnings_scope
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: ROOT accepted the original diagnostic; scientific identity remains bounded.
  snapshot_sha256: 4cc99c911f71330ac321493b6a3ba6279d933fbbc38ce530b7a08496d5f5f0bb
- evidence_id: support-2847-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-original-001.stderr
  locator: complete original stderr stream; twelve warning lines and their exact ordering
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: The original diagnostic has twelve omitted-undefined-stereo warning lines.
    They remain global and unassigned to any owner or form; no warning-to-record attribution
    is inferred.
  snapshot_sha256: 51097dc3e1fd0bf15e9992b2242e46b190b2ad046d6d3360f4eb1c8be17c3a15
- evidence_id: support-2847-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/native-prep/native-current285-cached-taxonomy-reading-003.json
  locator: /context_interpretations/9; /physical_negative_query_scopes/9; /whole_stanzas
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: 'Attributed Native cached-name reading: NCBITaxon:216591 = Burkholderia
    cenocepacia J2315, NCBITaxon:286 = Pseudomonas, NCBITaxon:95486 = Burkholderia
    cenocepacia. These retained labels establish no fresh rank, lineage, strain equivalence
    or experimental producer validation. Source producer and occurrence roles remain
    distinct; no exact merge or nonorganism decision applies to this context.'
  snapshot_sha256: 2d1c204d18dd79035d1d96a27e7424f42efd48af7b2b33c89ad5f8a78f87533b
- evidence_id: support-2847-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/native-prep/native-current285-implemented-curation-scan-001.json
  locator: /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows;
    /interpretation
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Nine substantive curation tables have no exact applicable correction. All
    exact predicates are negative for these five owners; lexical matches are not applied
    corrections.
  snapshot_sha256: 9b0b181bf96326cb154a70093b1deec0ad3a7ff0cf4e80871fd27ea981ebb716
  search_scope: Attributed ignored-inclusive nine-table/3422-row scan with exact owner/source-compound/BGC/full-key/occurrence/assay
    predicates. No new query or universal absence claim.
- evidence_id: support-2847-producerpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: complete method grading table
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Knockout supports organism and locus; heterologous expression and enzymatic
    assays support locus only. Source method labels remain attributed rather than
    newly inspected experiments.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2847-stereopolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142-173 structure_fields; atom-centre predicate lines 165-172
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: stereo_complete derives from FindMolChiralCenters and unknown atom tags;
    it does not certify full E/Z or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2847-filingpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295-306 choose_pathway
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: One supported normalized model pathway chooses filing; multiple, none or
    unsupported results retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2847-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/root-current285-five-gates-acceptance-001.json
  locator: /commands; /selected_queue_rows; /unavailable_required_gates; /all_native_gates_passed
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: All five local gates pass; complete QC/OAK remain unavailable and all_native_gates_passed
    is false. Queue leads are not automatic scientific findings.
  snapshot_sha256: da1beac543291886af6aa8c11c26adf093b28a78b794b6d79c656cfdc307360f
- evidence_id: support-2847-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch285/owner-capture-DATA-001.json
  locator: /records/6/owner_document/curation_history; /records/6/owner_document/source_concepts
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: PMID:16672617 has ENTRY scope. The LOTUS DOI pointers remain occurrence
    citations, not newly read primary bodies; shared entry and congener citations
    do not add independent experiments. Two seed-history events document processing
    and retain unresolved source questions.
  snapshot_sha256: 9042e782394e35188f0a4053f6cb76565baa3a45c799b52949b8d6d21a1ea9ad
- evidence_id: support-2847-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-target-input-plan-001.json
  locator: /records/6/complete_root_keys; /records/6/declared_mechanism_roots_literal;
    /records/6/component_paths; /records/6/complete_raw_mechanism_sections
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: The complete selected owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway,
    molecular_targets, bioactivities, bioactivity_summary, related_records or component
    root. No maintained reader is applicable to this owner. This bounded record absence
    is not a claim of absent biology; no selected owner in batch 285 requires a maintained
    reader. The positive unselected o-orsellinic-acid context does not transfer into
    these owners.
  snapshot_sha256: 8e6577535a621797ed5bb16973a653730dc5a2ca3fccfe1e0d486e4799d749b4
- evidence_id: support-2847-comparison
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch285/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/smiles/computed/formula; /records/5/smiles/computed/atoms; /records/5/smiles/computed/bonds;
    /records/5/smiles/computed/canonical_isomeric_smiles; /records/5/inchi/computed/formula;
    /records/5/inchi/computed/atoms; /records/5/inchi/computed/bonds; /records/5/inchi/computed/canonical_isomeric_smiles;
    /records/6/smiles/computed/formula; /records/6/smiles/computed/atoms; /records/6/smiles/computed/bonds;
    /records/6/smiles/computed/canonical_isomeric_smiles; /records/6/inchi/computed/formula;
    /records/6/inchi/computed/atoms; /records/6/inchi/computed/bonds; /records/6/inchi/computed/canonical_isomeric_smiles
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: 'The two actually parsed C6/C8 owners differ by two methylene units in
    their hydroxyacyl chains: six versus eight carbons including the carbonyl, with
    a C2H4 formula increment. Both have the same counted amide/imidic pattern and
    six unknown atom centres. Their distinct full keys and unknown stereo remain separate;
    no biosynthetic conversion, metal binding or unparsed C4 equivalence is inferred.'
  snapshot_sha256: 381563a9a0778e2c0ec460c24ebc54f65bf72366d3285e62d8dd0778e05f9cab
- evidence_id: support-2847-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete saved mibig_compounds frame with 1 positive placements.
  snapshot_sha256: 67aeb7d272d84232606fa30f5146793937cd9afbdb91a5dc1be071ea92634385
  search_scope: Uncapped retained predicate exact complete standard_inchi_key equality
    and exact query "NJIOFEXYZOVVKA-UHFFFAOYSA-N" only; no replay or universal absence.
- evidence_id: support-2847-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical line 3264, raw UTF-8 row SHA-256 49f90f0a92bb90d0012d177fbcda28a23c26706746e7d452bea2ad905ae83dd3
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: The owner is BGC0002569 version 3 compound index 1, NPAtlas NPA015051,
    full key NJIOFEXYZOVVKA-UHFFFAOYSA-N and formula C30H56N8O13. Direct C4/C6/C8
    shared-BGC contexts have separate full keys. The label and common cluster do not
    merge identities or transfer natural stereochemistry. Burkholderia cenocepacia
    J2315, NCBITaxon:216591, remains the BGC_CHARACTERIZED producer. This strain-qualified
    source claim is separate from the genus/species LOTUS occurrences and is not newly
    verified experimentally. AM747720.1:1846454–1876827 remains CLUSTER_DEMONSTRATED
    from retained Knock-out studies and Gene expression correlated with compound production.
    BGC0002569 version 3 is active, questionable quality and unknown completeness.
    These source methods support the recorded grade without establishing a complete
    enzyme-by-enzyme pathway.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2847-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete saved chebi_structures frame with 0 positive placements.
  snapshot_sha256: 67aeb7d272d84232606fa30f5146793937cd9afbdb91a5dc1be071ea92634385
  search_scope: Uncapped retained predicate exact complete standard_inchi_key equality
    and exact query "NJIOFEXYZOVVKA-UHFFFAOYSA-N" only; no replay or universal absence.
- evidence_id: support-2847-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete saved lotus_occurrences frame with 2 positive placements.
  snapshot_sha256: 67aeb7d272d84232606fa30f5146793937cd9afbdb91a5dc1be071ea92634385
  search_scope: Uncapped retained predicate exact complete standard_inchi_key equality
    and exact query "NJIOFEXYZOVVKA-UHFFFAOYSA-N" only; no replay or universal absence.
- evidence_id: support-2847-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical line 6008, raw UTF-8 row SHA-256 6c72884959835d573c396bc0db51ff1aa417a62c9dade41c0c9e6cea291492f8;
    physical line 6009, raw UTF-8 row SHA-256 3f55de23c52144e327f6072ab6ce71baad8240c92f6e95e91504a15a8bc30c2a
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: LOTUS rows 6008/6009 retain Pseudomonas, NCBITaxon:286, DOI:10.1002/JLAC.199319930108
    and Burkholderia cenocepacia, NCBITaxon:95486, DOI:10.1128/JB.188.10.3631-3644.2006,
    both structure Q77562412. Species occurrence remains distinct from strain J2315;
    publication independence was not established.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2847-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame with 0 positive placements.
  snapshot_sha256: 67aeb7d272d84232606fa30f5146793937cd9afbdb91a5dc1be071ea92634385
  search_scope: Uncapped retained predicate exact complete standard_inchi_key equality
    and exact query "NJIOFEXYZOVVKA-UHFFFAOYSA-N" only; no replay or universal absence.
- evidence_id: support-2847-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete saved npclassifier frame with 1 positive placements.
  snapshot_sha256: 67aeb7d272d84232606fa30f5146793937cd9afbdb91a5dc1be071ea92634385
  search_scope: Uncapped retained predicate exact complete standard_inchi_key equality
    and exact query "NJIOFEXYZOVVKA-UHFFFAOYSA-N" only; no replay or universal absence.
- evidence_id: support-2847-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical line 1612, raw UTF-8 row SHA-256 178a4b6e4f3fd6943f032e76ced7bcb65bacdece6806637669a4543e18c35f15
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: MIBiG NRPS and Type I are source BGC class and subclass. The exact NPClassifier
    row has empty pathway, superclass and class labels, and is_glycoside:false, model
    npclassifier.gnps2.org@2026-09-07. Empty model results retain UNCLASSIFIED under
    choose_pathway; they do not erase source NRPS provenance or constitute a structure
    defect.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2847-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame with 0 positive placements.
  snapshot_sha256: 67aeb7d272d84232606fa30f5146793937cd9afbdb91a5dc1be071ea92634385
  search_scope: Uncapped retained predicate exact complete standard_inchi_key equality
    and exact query "NJIOFEXYZOVVKA-UHFFFAOYSA-N" only; no replay or universal absence.
- evidence_id: support-2847-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete saved bindingdb_targets frame with 0 positive placements.
  snapshot_sha256: 67aeb7d272d84232606fa30f5146793937cd9afbdb91a5dc1be071ea92634385
  search_scope: Uncapped retained predicate exact complete standard_inchi_key equality
    and exact query "NJIOFEXYZOVVKA-UHFFFAOYSA-N" only; no replay or universal absence.
- evidence_id: support-2847-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame with 0 positive placements.
  snapshot_sha256: 67aeb7d272d84232606fa30f5146793937cd9afbdb91a5dc1be071ea92634385
  search_scope: Uncapped retained predicate exact complete standard_inchi_key equality
    and exact query "NJIOFEXYZOVVKA-UHFFFAOYSA-N" only; no replay or universal absence.
- evidence_id: support-2847-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch285-tentative/bgc-prep/bgc-conditional285-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Complete saved chebi_origins frame with 0 positive placements.
  snapshot_sha256: 67aeb7d272d84232606fa30f5146793937cd9afbdb91a5dc1be071ea92634385
  search_scope: Uncapped retained predicate exact chebi_id from exact full-key structure
    rows and exact query [] only; no replay or universal absence.
- evidence_id: support-2847-companion-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/ornibactin-c4.yaml
  locator: 'complete file: identifier, chemical_structure, source_concepts, biosynthetic_gene_clusters
    and curation_history'
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Exact captured direct owned-BGC companion, with distinct full key and context-only
    attribution. No congener identity, stereochemistry, producer grade or activity
    is transferred; only the explicitly linked saved-form comparison is used.
  snapshot_sha256: d406d92134aa25a7d4e2ba01de8ccc6087ff64256a1ba0b9c2d018e7e01b7c1f
- evidence_id: support-2847-companion-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/ornibactin-c6.yaml
  locator: 'complete file: identifier, chemical_structure, source_concepts, biosynthetic_gene_clusters
    and curation_history'
  accessed_at: '2026-11-07T07:09:01.470125Z'
  support: supports
  summary: Exact captured direct owned-BGC companion, with distinct full key and context-only
    attribution. No congener identity, stereochemistry, producer grade or activity
    is transferred; only the explicitly linked saved-form comparison is used.
  snapshot_sha256: 9092e63aa57f62359c78ff40b2523c14ddfa45c8e4d64e9193673df9a32cdd3c
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-285/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-285/native-current285-five-gates-execution-001.json
  accessed_at: '2026-11-07T06:41:05.132932Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: fbe2cdff4587f125eb6732814ea44c3c28e60ed55c5c8fab1852c1e9bf279b93
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-285/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-285/native-current285-five-gates-execution-001.json
  accessed_at: '2026-11-07T06:41:31.079423Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: b6a260b4f76c02eca90a7d90c5cb0d35a2eddff1101ffd75796f8bdfe064f535
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-285/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-285/native-current285-five-gates-execution-001.json
  accessed_at: '2026-11-07T06:41:51.246036Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-285/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-285/native-current285-five-gates-execution-001.json
  accessed_at: '2026-11-07T06:42:25.824908Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-285/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-285/native-current285-five-gates-execution-001.json
  accessed_at: '2026-11-07T06:42:37.728016Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 9d2078db8c4708e2d558f25e910fab78d6d942f315d31ac277807b65a97972b3
assessments:
- assessment_id: support-2847-identity-assessment
  area: identity
  topic: Exact retained compound grounding
  summary: The owner is BGC0002569 version 3 compound index 1, NPAtlas NPA015051,
    full key NJIOFEXYZOVVKA-UHFFFAOYSA-N and formula C30H56N8O13. Direct C4/C6/C8
    shared-BGC contexts have separate full keys. The label and common cluster do not
    merge identities or transfer natural stereochemistry.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  evidence_ids:
  - support-2847-owner
  - support-2847-capture
  - support-2847-source
  - support-2847-intake
  - support-2847-curation
  - support-2847-plan
  - support-2847-table-mibig_compounds
  - support-2847-table-lotus_occurrences
  - support-2847-table-npclassifier
  - support-2847-companion-0
  - support-2847-companion-1
  dimensions:
  - name: standard_inchi_key
    definition: Complete source key, not label-only identity.
    value: NJIOFEXYZOVVKA-UHFFFAOYSA-N
    evidence_ids:
    - support-2847-owner
    - support-2847-capture
    - support-2847-source
    - support-2847-intake
    - support-2847-curation
    - support-2847-plan
    - support-2847-table-mibig_compounds
    - support-2847-table-lotus_occurrences
    - support-2847-table-npclassifier
    - support-2847-companion-0
    - support-2847-companion-1
  - name: grounding_scope
    definition: Retained source identity versus independently established natural
      identity.
    value: The owner is BGC0002569 version 3 compound index 1, NPAtlas NPA015051,
      full key NJIOFEXYZOVVKA-UHFFFAOYSA-N and formula C30H56N8O13. Direct C4/C6/C8
      shared-BGC contexts have separate full keys. The label and common cluster do
      not merge identities or transfer natural stereochemistry.
    evidence_ids:
    - support-2847-owner
    - support-2847-capture
    - support-2847-source
    - support-2847-intake
    - support-2847-curation
    - support-2847-plan
    - support-2847-table-mibig_compounds
    - support-2847-table-lotus_occurrences
    - support-2847-table-npclassifier
    - support-2847-companion-0
    - support-2847-companion-1
- assessment_id: support-2847-representation-assessment
  area: representation
  topic: Saved molecular forms and stereochemical scope
  summary: 'Both saved forms are neutral C30H56N8O13 with 51 atoms, 50 bonds, one
    acyclic component and no aromatic atoms or metal. SMILES has seven carbonyls and
    six strict amides; the InChI-derived form has three carbonyls and two strict amides
    plus four C(OH)=N sites. The two N-hydroxy acyl carbonyls remain, while four secondary
    amides change representation. This explains the canonical-SMILES disagreement
    without independently proving natural identity or choosing a preferred biological
    tautomer. In SMILES the hydroxyacyl chain is C0–C7 including carbonyl C7, with
    OH at C5/O50. N-hydroxy acyl groups are C7(=O8)–N9–O49 and formyl C37(=O38)–N36–O39.
    The neutral acid is C19(=O20)–O21H, and N47/N48 are free primary amines. The InChI
    form retains the acid C29/O47/O48 and four imidic motif sites; no complete atom
    mapping is asserted. Neither form has an ester, N-acetyl motif, saturated C5O
    candidate sugar or phosphorus. N-hydroxy groups alone establish no metal affinity,
    complex or assay result. The two actually parsed C6/C8 owners differ by two methylene
    units in their hydroxyacyl chains: six versus eight carbons including the carbonyl,
    with a C2H4 formula increment. Both have the same counted amide/imidic pattern
    and six unknown atom centres. Their distinct full keys and unknown stereo remain
    separate; no biosynthetic conversion, metal binding or unparsed C4 equivalence
    is inferred. Both canonical SMILES comparisons are false; the chirality-aware
    map is empty and complete_atom_count_match/full_graph_identity_established remain
    false. Normalized identifiers, formula agreement and local parsing do not establish
    independent full graph identity, natural-sample identity, experimental absolute
    stereochemistry or primary biological validation.'
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  evidence_ids:
  - support-2847-data
  - support-2847-stereo
  - support-2847-motifs
  - support-2847-molecularreading
  - support-2847-execution
  - support-2847-diagaccept
  - support-2847-stereopolicy
  - support-2847-plan
  - support-2847-comparison
  - support-2847-companion-0
  - support-2847-companion-1
  dimensions:
  - name: stereochemistry_scope
    definition: Saved atom/bond assignments and representation-dependent candidates.
    value: Both encodings have six unspecified tetrahedral candidates and no assigned
      tetrahedral centres. The InChI-derived form adds four unspecified potential
      C=N sites at its imidic bonds. The source false stereo_complete flag is consistent
      with unresolved atom centres; these added candidate doubles do not supply natural
      geometries or four new experimental ambiguities.
    evidence_ids:
    - support-2847-data
    - support-2847-stereo
    - support-2847-motifs
    - support-2847-molecularreading
    - support-2847-execution
    - support-2847-diagaccept
    - support-2847-stereopolicy
    - support-2847-plan
    - support-2847-comparison
    - support-2847-companion-0
    - support-2847-companion-1
  - name: representation_correspondence
    definition: Saved match remains distinct from full identity.
    value: Both canonical SMILES comparisons are false; the chirality-aware map is
      empty and complete_atom_count_match/full_graph_identity_established remain false.
      Normalized identifiers, formula agreement and local parsing do not establish
      independent full graph identity, natural-sample identity, experimental absolute
      stereochemistry or primary biological validation.
    evidence_ids:
    - support-2847-data
    - support-2847-stereo
    - support-2847-motifs
    - support-2847-molecularreading
    - support-2847-execution
    - support-2847-diagaccept
    - support-2847-stereopolicy
    - support-2847-plan
    - support-2847-comparison
    - support-2847-companion-0
    - support-2847-companion-1
- assessment_id: support-2847-provenance-assessment
  area: provenance
  topic: Compound-specific producer, locus and taxon
  summary: Burkholderia cenocepacia J2315, NCBITaxon:216591, remains the BGC_CHARACTERIZED
    producer. This strain-qualified source claim is separate from the genus/species
    LOTUS occurrences and is not newly verified experimentally. AM747720.1:1846454–1876827
    remains CLUSTER_DEMONSTRATED from retained Knock-out studies and Gene expression
    correlated with compound production. BGC0002569 version 3 is active, questionable
    quality and unknown completeness. These source methods support the recorded grade
    without establishing a complete enzyme-by-enzyme pathway.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  evidence_ids:
  - support-2847-source
  - support-2847-capture
  - support-2847-taxonomy
  - support-2847-curation
  - support-2847-producerpolicy
  - support-2847-plan
  - support-2847-table-mibig_compounds
  - support-2847-table-lotus_occurrences
  - support-2847-table-npclassifier
  dimensions:
  - name: taxon_scope
    definition: Cached names do not resolve current rank/lineage or strain equivalence.
    value: 'Attributed Native cached-name reading: NCBITaxon:216591 = Burkholderia
      cenocepacia J2315, NCBITaxon:286 = Pseudomonas, NCBITaxon:95486 = Burkholderia
      cenocepacia. These retained labels establish no fresh rank, lineage, strain
      equivalence or experimental producer validation. Source producer and occurrence
      roles remain distinct; no exact merge or nonorganism decision applies to this
      context.'
    evidence_ids:
    - support-2847-source
    - support-2847-capture
    - support-2847-taxonomy
    - support-2847-curation
    - support-2847-producerpolicy
    - support-2847-plan
    - support-2847-table-mibig_compounds
    - support-2847-table-lotus_occurrences
    - support-2847-table-npclassifier
  - name: producer_evidence
    definition: Producer grade remains distinct from locus evidence.
    value: Burkholderia cenocepacia J2315, NCBITaxon:216591, remains the BGC_CHARACTERIZED
      producer. This strain-qualified source claim is separate from the genus/species
      LOTUS occurrences and is not newly verified experimentally.
    evidence_ids:
    - support-2847-source
    - support-2847-capture
    - support-2847-taxonomy
    - support-2847-curation
    - support-2847-producerpolicy
    - support-2847-plan
    - support-2847-table-mibig_compounds
    - support-2847-table-lotus_occurrences
    - support-2847-table-npclassifier
  - name: locus_evidence
    definition: Exact entry version, endpoints and methods delimit evidence.
    value: AM747720.1:1846454–1876827 remains CLUSTER_DEMONSTRATED from retained Knock-out
      studies and Gene expression correlated with compound production. BGC0002569
      version 3 is active, questionable quality and unknown completeness. These source
      methods support the recorded grade without establishing a complete enzyme-by-enzyme
      pathway.
    evidence_ids:
    - support-2847-source
    - support-2847-capture
    - support-2847-taxonomy
    - support-2847-curation
    - support-2847-producerpolicy
    - support-2847-plan
    - support-2847-table-mibig_compounds
    - support-2847-table-lotus_occurrences
    - support-2847-table-npclassifier
- assessment_id: support-2847-citations-assessment
  area: evidence
  topic: Citation grain and retained history
  summary: PMID:16672617 has ENTRY scope. The LOTUS DOI pointers remain occurrence
    citations, not newly read primary bodies; shared entry and congener citations
    do not add independent experiments. Two seed-history events document processing
    and retain unresolved source questions.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  evidence_ids:
  - support-2847-owner
  - support-2847-source
  - support-2847-capture
  - support-2847-history
  - support-2847-table-mibig_compounds
  - support-2847-table-lotus_occurrences
  - support-2847-table-npclassifier
  dimensions:
  - name: citation_scope
    definition: Database pointers/imports do not supply independent primary proof.
    value: PMID:16672617 has ENTRY scope. The LOTUS DOI pointers remain occurrence
      citations, not newly read primary bodies; shared entry and congener citations
      do not add independent experiments. Two seed-history events document processing
      and retain unresolved source questions.
    evidence_ids:
    - support-2847-owner
    - support-2847-source
    - support-2847-capture
    - support-2847-history
    - support-2847-table-mibig_compounds
    - support-2847-table-lotus_occurrences
    - support-2847-table-npclassifier
- assessment_id: support-2847-occurrence-assay-assessment
  area: evidence
  topic: Occurrence and assay boundaries
  summary: 'LOTUS rows 6008/6009 retain Pseudomonas, NCBITaxon:286, DOI:10.1002/JLAC.199319930108
    and Burkholderia cenocepacia, NCBITaxon:95486, DOI:10.1128/JB.188.10.3631-3644.2006,
    both structure Q77562412. Species occurrence remains distinct from strain J2315;
    publication independence was not established. All six other saved named frames
    are bounded negatives: ChEBI structures and their conditional origins, CyanoMetDB,
    PubChem, BindingDB and AntibioticMech. No actual AID or blank AID marker exists
    in this owner scope. No activity, target, inactivity or metal binding follows
    from those negatives or the compound name.'
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  evidence_ids:
  - support-2847-source
  - support-2847-taxonomy
  - support-2847-curation
  - support-2847-plan
  - support-2847-query-mibig_compounds
  - support-2847-query-chebi_structures
  - support-2847-query-lotus_occurrences
  - support-2847-query-cyanometdb_occurrences
  - support-2847-query-npclassifier
  - support-2847-query-pubchem_bioassay
  - support-2847-query-bindingdb_targets
  - support-2847-query-antibioticmech_inchikeys
  - support-2847-query-chebi_origins
  - support-2847-table-mibig_compounds
  - support-2847-table-lotus_occurrences
  - support-2847-table-npclassifier
  dimensions:
  - name: occurrence_scope
    definition: Occurrence does not establish a causal producer.
    value: LOTUS rows 6008/6009 retain Pseudomonas, NCBITaxon:286, DOI:10.1002/JLAC.199319930108
      and Burkholderia cenocepacia, NCBITaxon:95486, DOI:10.1128/JB.188.10.3631-3644.2006,
      both structure Q77562412. Species occurrence remains distinct from strain J2315;
      publication independence was not established.
    evidence_ids:
    - support-2847-source
    - support-2847-taxonomy
    - support-2847-curation
    - support-2847-plan
    - support-2847-query-mibig_compounds
    - support-2847-query-chebi_structures
    - support-2847-query-lotus_occurrences
    - support-2847-query-cyanometdb_occurrences
    - support-2847-query-npclassifier
    - support-2847-query-pubchem_bioassay
    - support-2847-query-bindingdb_targets
    - support-2847-query-antibioticmech_inchikeys
    - support-2847-query-chebi_origins
    - support-2847-table-mibig_compounds
    - support-2847-table-lotus_occurrences
    - support-2847-table-npclassifier
  - name: assay_target_scope
    definition: Negative saved predicates are not inactivity experiments.
    value: 'All six other saved named frames are bounded negatives: ChEBI structures
      and their conditional origins, CyanoMetDB, PubChem, BindingDB and AntibioticMech.
      No actual AID or blank AID marker exists in this owner scope. No activity, target,
      inactivity or metal binding follows from those negatives or the compound name.'
    evidence_ids:
    - support-2847-source
    - support-2847-taxonomy
    - support-2847-curation
    - support-2847-plan
    - support-2847-query-mibig_compounds
    - support-2847-query-chebi_structures
    - support-2847-query-lotus_occurrences
    - support-2847-query-cyanometdb_occurrences
    - support-2847-query-npclassifier
    - support-2847-query-pubchem_bioassay
    - support-2847-query-bindingdb_targets
    - support-2847-query-antibioticmech_inchikeys
    - support-2847-query-chebi_origins
    - support-2847-table-mibig_compounds
    - support-2847-table-lotus_occurrences
    - support-2847-table-npclassifier
- assessment_id: support-2847-classification-assessment
  area: consistency
  topic: Source classes, model labels and filing
  summary: MIBiG NRPS and Type I are source BGC class and subclass. The exact NPClassifier
    row has empty pathway, superclass and class labels, and is_glycoside:false, model
    npclassifier.gnps2.org@2026-09-07. Empty model results retain UNCLASSIFIED under
    choose_pathway; they do not erase source NRPS provenance or constitute a structure
    defect.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  evidence_ids:
  - support-2847-source
  - support-2847-owner
  - support-2847-motifs
  - support-2847-filingpolicy
  - support-2847-gates
  - support-2847-table-mibig_compounds
  - support-2847-table-lotus_occurrences
  - support-2847-table-npclassifier
  dimensions:
  - name: classification_applicability
    definition: Source/model/topology/biochemical evidence remain distinct.
    value: MIBiG NRPS and Type I are source BGC class and subclass. The exact NPClassifier
      row has empty pathway, superclass and class labels, and is_glycoside:false,
      model npclassifier.gnps2.org@2026-09-07. Empty model results retain UNCLASSIFIED
      under choose_pathway; they do not erase source NRPS provenance or constitute
      a structure defect.
    evidence_ids:
    - support-2847-source
    - support-2847-owner
    - support-2847-motifs
    - support-2847-filingpolicy
    - support-2847-gates
    - support-2847-table-mibig_compounds
    - support-2847-table-lotus_occurrences
    - support-2847-table-npclassifier
- assessment_id: support-2847-completion-assessment
  area: completeness
  topic: Earned work and unavailable authority
  summary: The complete selected owner, current source/intake and both saved molecular
    forms were read. The complete selected owner has no causal_graphs, causal_graph_refs,
    biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary, related_records
    or component root. No maintained reader is applicable to this owner. This bounded
    record absence is not a claim of absent biology; no selected owner in batch 285
    requires a maintained reader. The positive unselected o-orsellinic-acid context
    does not transfer into these owners. No additional material local defect was established
    in this bounded scope. Existing OPEN discussions are not closed. Five local gates
    pass; full QC, complete OAK and fresh primary/external verification remain unavailable.
    Completion is partial and native SEEDED status remains unchanged.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-92a1e3d468
  evidence_ids:
  - support-2847-intake
  - support-2847-intakeaccept
  - support-2847-plan
  - support-2847-planaccept
  - support-2847-notes
  - support-2847-gates
  - support-2847-data
  - support-2847-diagaccept
  - support-2847-scope
  dimensions:
  - name: review_completion
    definition: Local review does not substitute for unavailable authority or promote
      native status.
    value: The complete selected owner, current source/intake and both saved molecular
      forms were read. The complete selected owner has no causal_graphs, causal_graph_refs,
      biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary,
      related_records or component root. No maintained reader is applicable to this
      owner. This bounded record absence is not a claim of absent biology; no selected
      owner in batch 285 requires a maintained reader. The positive unselected o-orsellinic-acid
      context does not transfer into these owners. No additional material local defect
      was established in this bounded scope. Existing OPEN discussions are not closed.
      Five local gates pass; full QC, complete OAK and fresh primary/external verification
      remain unavailable. Completion is partial and native SEEDED status remains unchanged.
    evidence_ids:
    - support-2847-intake
    - support-2847-intakeaccept
    - support-2847-plan
    - support-2847-planaccept
    - support-2847-notes
    - support-2847-gates
    - support-2847-data
    - support-2847-diagaccept
    - support-2847-scope
findings: []
actions: []
limitations:
- Normalized identifiers, formula agreement and local parsing do not establish independent
  full graph identity, natural-sample identity, experimental absolute stereochemistry
  or primary biological validation.
- Both canonical SMILES comparisons are false; the chirality-aware map is empty and
  complete_atom_count_match/full_graph_identity_established remain false. Both encodings
  have six unspecified tetrahedral candidates and no assigned tetrahedral centres.
  The InChI-derived form adds four unspecified potential C=N sites at its imidic bonds.
  The source false stereo_complete flag is consistent with unresolved atom centres;
  these added candidate doubles do not supply natural geometries or four new experimental
  ambiguities.
- The original diagnostic has twelve omitted-undefined-stereo warning lines. They
  remain global and unassigned to any owner or form; no warning-to-record attribution
  is inferred.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK
  remain unavailable. All database assertions retain their original grain, grades
  and unresolved questions.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh current 285 evidence and judgments; prior batches supply interface logic only.
- No source record, native status or history was changed; no source query, molecular
  parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual local gate checks and three required unavailable checks.
  No maintained-reader check applies to these five negative-root owners.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-285
```
