# Local evidence review: Myxarylin

- Review: 20261107T004933Z-myxarylin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T23:53:39.614399Z
- Finished UTC: 2026-11-07T00:49:33.522991Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Myxarylin retains exact compound-specific source grounding and a qualified proposed BytZ methylation graph. The complete reader preserves the graph-only owner; saved molecular normalization agrees but both canonical forms differ. No new specific local defect is established, and primary mechanism/sequence claims remain unverified, so completion is partial with limitations.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2798; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-489bd6e2d9 | data/natural_products/unclassified/myxarylin.yaml | generated | Myxarylin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-489bd6e2d9 | Both stored forms parsed and retain declared normalized keys; Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. |
| Complete offline maintained reader for myxarylin | passed | True | naturalproductmech:mibig-489bd6e2d9 | One original complete offline maintained reader returned the exact captured owner. |
| strict_ten | passed | True | naturalproductmech:mibig-489bd6e2d9 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-489bd6e2d9 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-489bd6e2d9 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-489bd6e2d9 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-489bd6e2d9 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-489bd6e2d9 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-489bd6e2d9 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-489bd6e2d9 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained compound grounding

identity: supported. Targets: naturalproductmech:mibig-489bd6e2d9.

The exact YNCKCZXUTZJZTQ-ULQDDVLXSA-N grouping is BGC0002631 version 2, compound index 1, with NPAtlas NPA033347. The stored macrocyclic label and full key do not independently establish a natural sample or database example product match.

### Saved molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-489bd6e2d9.

Both forms contain 32 atoms, 34 bonds and neutral C22H29N5O5. Standard InChI, key, formula, charge and counts agree, but both canonical SMILES comparisons are false and the limited atom map is empty. Each form retains three rings: a 14-membered macrocycle, an aromatic six-ring and an aromatic five-membered imidazole ring. The macrocycle contains the aryl-carbon to imidazole-nitrogen linkage S9-N11 and two peptide amides S22-N21 and S30-N29. In the InChI-derived form those become two C-single-O/double-N sites I19-N24-O28 and I20-N25-O29, with zero strict carbonyl amides. A free carboxyl, phenolic oxygen and N-methyl secondary amine remain; the latter is not a nonamide primary amine. No ester, C-O-C bridge or saturated C5O sugar ring is detected by the defined motifs. Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. Normalized key/formula agreement and a successful local process do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry, primary mechanism validation or a native status promotion.

### Compound-specific producer, locus and taxon

provenance: supported. Targets: naturalproductmech:mibig-489bd6e2d9.

Pyxidicoccus fallax (394095) remains SOURCE_ASSERTION. The cached Pyxicoccus spelling synonym and historical An d48/MCy8396 notes do not supply a new strain, sequence or experimental identity check. BGC0002631 version 2, OL539738.1:1-3091, retains active/questionable/unknown metadata and CLUSTER_UNSTATED with no method. Source RIBOSOMAL/RiPP classification is separate from the proposed BytZ activity.

### Citation grain and retained history

evidence: supported. Targets: naturalproductmech:mibig-489bd6e2d9.

All four history events are retained: three seeding events and one 2026-10-07 curation event. The graph has five reference placements, including repeated MITE0000420 version 1 plus GenPept UID85537.1 and OL539738.1 historical claims. The prior 795-nt/table-11/264-residue and product-key comparisons are not newly reproduced primary or sequence proof. Inaccessible historical papers and bounded historical UniProt searches remain qualified attribution, not fresh absence or verification.

### Occurrence and assay limits

evidence: supported. Targets: naturalproductmech:mibig-489bd6e2d9.

The LOTUS Pyxidicoccus fallax occurrence cites DOI:10.3390/MOLECULES26247483. MIBiG cites DOI:10.3390/molecules26247483 at COMPOUND_EVIDENCE grain. Case variants of this DOI do not establish two independent publications or turn occurrence into production. No retained PubChem AID, BindingDB target or AntibioticMech full-key row is present in the saved frames. The proposed methyltransferase context is not an assay magnitude, target-binding result, knockout phenotype or physiological cofactor assignment.

### Source classes, model labels and filing

consistency: supported. Targets: naturalproductmech:mibig-489bd6e2d9.

The source Macrocyclic and RIBOSOMAL labels are separate from model Alkaloids plus Amino acids and Peptides, Oligopeptides/Histidine alkaloids and Cyclic peptides/Imidazole alkaloids. The saved macrocycle and imidazole support the limited structural description, while the two-pathway result correctly retains UNCLASSIFIED. False glycoside is a model value; motif negatives are bounded.

### Complete retained mechanism and owner scope

consistency: supported. Targets: naturalproductmech:mibig-489bd6e2d9.

The accepted complete owner has one four-node, three-edge graph, four histories and no biosynthetic_pathway, components or molecular targets. NCBIProtein:UID85537.1 is a grounded native reference; the cyclized substrate example and methylation process remain ungrounded. All edges explicitly qualify BytZ as database-proposed. The reader does not validate catalysis, historical CDS identity, leader cleavage, BytA/BytO function, full pathway order or physiological finality. No unsupported stronger claim is adopted.

### Earned work and unavailable authority

completeness: supported. Targets: naturalproductmech:mibig-489bd6e2d9.

Complete assigned raw/source/intake and both saved molecular forms were read. The required original maintained reader returned the complete owner; preservation does not verify mechanism science. Five local native commands pass; full QC, complete OAK and fresh primary verification remain unavailable. Completion is partial, native SEEDED status unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2798-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/myxarylin.yaml; complete file: chemical_structure, source_concepts, producer_organisms, biosynthetic_gene_clusters, classification, mechanisms and curation_history | supports | Complete current owner retained; generated facts and curator-owned mechanisms remain distinct. |
| support-2798-capture | /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json; /records/7/owner_document; /records/7/component_captures | supports | Whole accepted owner capture; no component or target transfer. |
| support-2798-source | /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-assigned-source-reading-001.json; /contexts/5; /selected_counts; /counts; /global_cautions | supports | Complete assigned saved source context. Own selected credit totals 18 rows/239 fields/45 frames/31 negatives; five companions have separate context-only credit. |
| support-2798-plan | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-target-input-plan-001.json; /records/7; /source_placement_count; /unique_source_path_count | supports | Actual 463-placement/72-path plan; this owner has 46 captured inputs. |
| support-2798-planaccept | /private/tmp/npm-review-work/shared-next-batch280/root-current280-input-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepted this original current source plan. |
| support-2798-notes | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /curation | supports | Current notes retain the disjoint source and Native taxonomy/curation interpretations; no added primary credit. |
| support-2798-intake | /private/tmp/npm-review-work/shared-next-batch280/intakes-001/2798-inspect-001.json; /status; /source; /targets | supports | Actual intake fixes generated target, maintained owners and current relative input hashes. |
| support-2798-intakeaccept | /private/tmp/npm-review-work/shared-next-batch280/root-current280-intake-acceptance-001.json; /status; /accepted; /intake_summary | supports | ROOT accepted all ten original intakes, all exit zero with empty stderr. |
| support-2798-data | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles; /records/7/inchi; /records/7/comparisons; /records/7/atom_correspondence; /records/7/literal_InChI_layers; /records/7/formula_comparison_scope | supports | Both forms contain 32 atoms, 34 bonds and neutral C22H29N5O5. Standard InChI, key, formula, charge and counts agree, but both canonical SMILES comparisons are false and the limited atom map is empty. Each form retains three rings: a 14-membered macrocycle, an aromatic six-ring and an aromatic five-membered imidazole ring. Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. |
| support-2798-stereo | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed/atoms; /records/7/smiles/computed/potential_stereo; /records/7/smiles/computed/bonds; /records/7/inchi/computed/atoms; /records/7/inchi/computed/potential_stereo; /records/7/inchi/computed/bonds | supports | Each form retains three specified S tetrahedral centres (S2, S17, S24; I14, I15, I16). Two unspecified potential C=N candidates occur in the InChI-derived representation. The source atom-stereo flag does not establish a complete natural configuration or prove the proposed enzyme's activity. |
| support-2798-motifs | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed/motifs; /records/7/smiles/computed/rings; /records/7/smiles/computed/bonds; /records/7/smiles/computed/atoms; /records/7/inchi/computed/motifs; /records/7/inchi/computed/rings; /records/7/inchi/computed/bonds; /records/7/inchi/computed/atoms | supports | The macrocycle contains the aryl-carbon to imidazole-nitrogen linkage S9-N11 and two peptide amides S22-N21 and S30-N29. In the InChI-derived form those become two C-single-O/double-N sites I19-N24-O28 and I20-N25-O29, with zero strict carbonyl amides. A free carboxyl, phenolic oxygen and N-methyl secondary amine remain; the latter is not a nonamide primary amine. No ester, C-O-C bridge or saturated C5O sugar ring is detected by the defined motifs. |
| support-2798-molecularreading | /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-last-five-molecular-intake-reading-001.json; /records/2; /counts; /warnings | supports | Complete ten saved forms personally read; no molecular replay. Four original undefined-stereo warning lines and two proton-addition/removal warning lines remain globally unassigned; none is assigned to an individual owner. |
| support-2798-execution | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries | supports | Single original diagnostic command and retained streams; no replay. |
| support-2798-diagaccept | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/root-current280-diagnostic-acceptance-001.json; /status; /accepted; /diagnostic; /execution | supports | ROOT accepted the original stored-form diagnostic. |
| support-2798-stderr | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-original-001.stderr; complete six original warning lines | supports | Four original undefined-stereo warning lines and two proton-addition/removal warning lines remain globally unassigned; none is assigned to an individual owner. |
| support-2798-taxonomy | /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-cached-taxonomy-reading-001.json; /context_interpretations/14; /physical_negative_query_scopes/14; /whole_stanzas | supports | Retain Pyxidicoccus fallax (394095), cached spelling synonym Pyxicoccus fallax, and BGC0002631:1/OL539738.1 COMPOUND_EVIDENCE citation. LOTUS occurrence has the same taxon and DOI spelling variant but does not establish independent publication or production evidence. Historical An d48/MCy8396 sequence claims remain attributed. |
| support-2798-curation | /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-implemented-curation-scan-002.json; /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows; /interpretation | supports | No current exact applicable maintained correction; lexical names and unrelated BGC rows do not transfer decisions. |
| support-2798-producerpolicy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; complete method grading table | supports | Producer evidence and locus methods answer different questions; unstated methods retain their grade. |
| support-2798-stereopolicy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172, atom-centre completeness predicate | supports | Retained stereo_complete checks unassigned atom centres, not all geometry or natural identity. |
| support-2798-filingpolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306, choose_pathway | supports | One supported normalized pathway selects filing; multiple, none or unsupported values retain UNCLASSIFIED. |
| support-2798-gates | /private/tmp/npm-review-work/shared-next-batch280/root-current280-five-gates-acceptance-001.json; /five_local_commands_passed; /all_native_gates_passed; /selected_queue_rows; /selected_queue_counts/2798; /unavailable_required_gates | supports | Five local gates pass, with required QC/OAK unavailable. Actual queue entries are diagnostic leads, not automatic scientific findings. |
| support-2798-history | /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json; /records/7/owner_document/curation_history; /records/7/owner_document/source_concepts | supports | All four history events are retained: three seeding events and one 2026-10-07 curation event. The graph has five reference placements, including repeated MITE0000420 version 1 plus GenPept UID85537.1 and OL539738.1 historical claims. The prior 795-nt/table-11/264-residue and product-key comparisons are not newly reproduced primary or sequence proof. Inaccessible historical papers and bounded historical UniProt searches remain qualified attribution, not fresh absence or verification. |
| support-2798-scope | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-target-input-plan-001.json; /records/7/complete_root_keys; /records/7/declared_mechanism_roots_literal; /records/7/component_paths; /records/7/complete_raw_mechanism_sections | supports | The accepted complete owner has one four-node, three-edge graph, four histories and no biosynthetic_pathway, components or molecular targets. NCBIProtein:UID85537.1 is a grounded native reference; the cyclized substrate example and methylation process remain ungrounded. All edges explicitly qualify BytZ as database-proposed. The reader does not validate catalysis, historical CDS identity, leader cleavage, BytA/BytO function, full pathway order or physiological finality. No unsupported stronger claim is adopted. |
| support-2798-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame with 1 positive placements read. |
| support-2798-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical line 3358, raw UTF-8 row SHA-256 632a6521f6d4ee23b6cc11d13d8d9e66b2f20abb1c38cc82a51cdb71d0037f61 | supports | The exact YNCKCZXUTZJZTQ-ULQDDVLXSA-N grouping is BGC0002631 version 2, compound index 1, with NPAtlas NPA033347. The stored macrocyclic label and full key do not independently establish a natural sample or database example product match. Pyxidicoccus fallax (394095) remains SOURCE_ASSERTION. The cached Pyxicoccus spelling synonym and historical An d48/MCy8396 notes do not supply a new strain, sequence or experimental identity check. BGC0002631 version 2, OL539738.1:1-3091, retains active/questionable/unknown metadata and CLUSTER_UNSTATED with no method. Source RIBOSOMAL/RiPP classification is separate from the proposed BytZ activity. |
| support-2798-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame with 0 positive placements read. |
| support-2798-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame with 1 positive placements read. |
| support-2798-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical line 9873, raw UTF-8 row SHA-256 69bc9abe3b04b533bb78fa3c2f0046b52c7c1c82e09778ae527c1cf164a57711 | supports | The LOTUS Pyxidicoccus fallax occurrence cites DOI:10.3390/MOLECULES26247483. MIBiG cites DOI:10.3390/molecules26247483 at COMPOUND_EVIDENCE grain. Case variants of this DOI do not establish two independent publications or turn occurrence into production. |
| support-2798-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame with 0 positive placements read. |
| support-2798-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame with 1 positive placements read. |
| support-2798-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical line 2946, raw UTF-8 row SHA-256 81e7c93386542e906c3dcfc2f2ca03cc1a81cb9a23972b01a7af47ab95f72d2f | supports | The source Macrocyclic and RIBOSOMAL labels are separate from model Alkaloids plus Amino acids and Peptides, Oligopeptides/Histidine alkaloids and Cyclic peptides/Imidazole alkaloids. The saved macrocycle and imidazole support the limited structural description, while the two-pathway result correctly retains UNCLASSIFIED. False glycoside is a model value; motif negatives are bounded. |
| support-2798-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame with 0 positive placements read. |
| support-2798-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame with 0 positive placements read. |
| support-2798-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame with 0 positive placements read. |
| support-2798-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame with 0 positive placements read. |
| support-2798-reader-data | /private/tmp/npm-review-work/shared-next-batch280/native-current280-myxarylin-maintained-reader-DATA-001.json; /raw_owner; /resolved_view; /expected_view; /counts; /reader_call_count; /denials; /unexpected_denials; /errors | supports | The accepted complete owner has one four-node, three-edge graph, four histories and no biosynthetic_pathway, components or molecular targets. NCBIProtein:UID85537.1 is a grounded native reference; the cyclized substrate example and methylation process remain ungrounded. All edges explicitly qualify BytZ as database-proposed. The reader does not validate catalysis, historical CDS identity, leader cleavage, BytA/BytO function, full pathway order or physiological finality. No unsupported stronger claim is adopted. Whole returned owner equals accepted capture; no primary or scientific validation follows. |
| support-2798-reader-execution | /private/tmp/npm-review-work/shared-next-batch280/native-current280-myxarylin-reader-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries | supports | One original offline maintained call, zero exit and stderr; known socket construction denied before action, no requests. |
| support-2798-reader-accept | /private/tmp/npm-review-work/shared-next-batch280/root-current280-myxarylin-reader-acceptance-001.json; /status; /accepted; /DATA; /execution; /review_check_contract; /limits | supports | ROOT accepted the complete returned owner and exact check contract; interpretation remains separate. |
| support-2798-reader-reading | /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-last-five-maintained-reader-reading-001.json; /records/1 | supports | review_support read every returned owner, graph, node, edge, evidence, pathway and history value. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-280/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-280/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-280/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-280/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-280/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Normalized key/formula agreement and a successful local process do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry, primary mechanism validation or a native status promotion.
- Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. Each form retains three specified S tetrahedral centres (S2, S17, S24; I14, I15, I16). Two unspecified potential C=N candidates occur in the InChI-derived representation. The source atom-stereo flag does not establish a complete natural configuration or prove the proposed enzyme's activity.
- Four original undefined-stereo warning lines and two proton-addition/removal warning lines remain globally unassigned; none is assigned to an individual owner.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK remain unavailable; source/database claims retain their exact authority.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh current 280 evidence and judgments; prior batches provide interface logic only.
- No source row, record, campaign or native status was changed; no query, molecular parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual native checks and three required unavailable checks; only orders 2797 and 2798 in this fragment receive actual maintained-reader checks.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T004933Z-myxarylin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: Myxarylin'
started_at: '2026-11-06T23:53:39.614399Z'
finished_at: '2026-11-07T00:49:33.522991Z'
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
summary: Myxarylin retains exact compound-specific source grounding and a qualified
  proposed BytZ methylation graph. The complete reader preserves the graph-only owner;
  saved molecular normalization agrees but both canonical forms differ. No new specific
  local defect is established, and primary mechanism/sequence claims remain unverified,
  so completion is partial with limitations.
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
  - path: data/natural_products/unclassified/myxarylin.yaml
    sha256: 2cc557ac6faea5363f32139df58dbe1fb7c4fb5a24c93f4651e66b269e894e44
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
  selection: Campaign path order 2798; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-489bd6e2d9
targets:
- target_id: naturalproductmech:mibig-489bd6e2d9
  path: data/natural_products/unclassified/myxarylin.yaml
  label: Myxarylin
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
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/myxarylin.yaml
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
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnose280-001.py
    2ba99053ef31c5bdddb405acb0108a92720b8a4af71d98f5b032ccd0adfb11b7 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
    df0120607515dc9243bfa92b39622a3bb842fd0bd3d1eb18d29677b785fd591b
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed and retain declared normalized keys; Both canonical
    SMILES comparisons are false; the saved map is empty, complete_atom_count_match
    is false and full_graph_identity_established is false.
  scope_note: 'Both forms contain 32 atoms, 34 bonds and neutral C22H29N5O5. Standard
    InChI, key, formula, charge and counts agree, but both canonical SMILES comparisons
    are false and the limited atom map is empty. Each form retains three rings: a
    14-membered macrocycle, an aromatic six-ring and an aromatic five-membered imidazole
    ring. Each form retains three specified S tetrahedral centres (S2, S17, S24; I14,
    I15, I16). Two unspecified potential C=N candidates occur in the InChI-derived
    representation. The source atom-stereo flag does not establish a complete natural
    configuration or prove the proposed enzyme''s activity. Four original undefined-stereo
    warning lines and two proton-addition/removal warning lines remain globally unassigned;
    none is assigned to an individual owner.'
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  evidence_ids:
  - support-2798-data
  - support-2798-execution
  - support-2798-diagaccept
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for myxarylin
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch280/read-selected-mechanism-guarded-001.py
    2798 df0120607515dc9243bfa92b39622a3bb842fd0bd3d1eb18d29677b785fd591b aac3680442ab340c9f6ffbd27d9253d1078b370126a0be0da132eb3d863e03a8
    a44b8239212154b11705bb659af9577a9ea6c7a94ca560b4a804f10dc48b84aa 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
    2ba99053ef31c5bdddb405acb0108a92720b8a4af71d98f5b032ccd0adfb11b7
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: One original complete offline maintained reader returned the exact captured
    owner.
  scope_note: The accepted complete owner has one four-node, three-edge graph, four
    histories and no biosynthetic_pathway, components or molecular targets. NCBIProtein:UID85537.1
    is a grounded native reference; the cyclized substrate example and methylation
    process remain ungrounded. All edges explicitly qualify BytZ as database-proposed.
    The reader does not validate catalysis, historical CDS identity, leader cleavage,
    BytA/BytO function, full pathway order or physiological finality. No unsupported
    stronger claim is adopted. Reader success is preservation and topology evidence,
    not scientific field-placement or primary-source validation.
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  evidence_ids:
  - support-2798-reader-data
  - support-2798-reader-execution
  - support-2798-reader-accept
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  command: just validate-strict data/natural_products/unclassified/ml-449.yaml data/natural_products/unclassified/montamide-a.yaml
    data/natural_products/unclassified/montanastatin.yaml data/natural_products/unclassified/muscoride-b.yaml
    data/natural_products/unclassified/mutanocyclin.yaml data/natural_products/unclassified/mycobactin.yaml
    data/natural_products/unclassified/mycosporine-glycine.yaml data/natural_products/unclassified/myxarylin.yaml
    data/natural_products/unclassified/myxochromide-b.yaml data/natural_products/unclassified/myxochromide-c.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-280/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-489bd6e2d9
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-280/validate-all-001.tsv
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
  - naturalproductmech:mibig-489bd6e2d9
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
  - naturalproductmech:mibig-489bd6e2d9
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
  - naturalproductmech:mibig-489bd6e2d9
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-280/review-queue-001.tsv
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
  - naturalproductmech:mibig-489bd6e2d9
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2798-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/myxarylin.yaml
  locator: 'complete file: chemical_structure, source_concepts, producer_organisms,
    biosynthetic_gene_clusters, classification, mechanisms and curation_history'
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete current owner retained; generated facts and curator-owned mechanisms
    remain distinct.
  snapshot_sha256: 2cc557ac6faea5363f32139df58dbe1fb7c4fb5a24c93f4651e66b269e894e44
- evidence_id: support-2798-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json
  locator: /records/7/owner_document; /records/7/component_captures
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Whole accepted owner capture; no component or target transfer.
  snapshot_sha256: 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
- evidence_id: support-2798-source
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-assigned-source-reading-001.json
  locator: /contexts/5; /selected_counts; /counts; /global_cautions
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete assigned saved source context. Own selected credit totals 18 rows/239
    fields/45 frames/31 negatives; five companions have separate context-only credit.
  snapshot_sha256: 585a5127b5ae32d25e5558b6d6299bb5da1cdf7584de93d3f093bd410ea4b5b0
- evidence_id: support-2798-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-target-input-plan-001.json
  locator: /records/7; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Actual 463-placement/72-path plan; this owner has 46 captured inputs.
  snapshot_sha256: d6777f8dea91c7542347ffaf26f8bc8cc03d93b08032d32861abac52335c3fa3
- evidence_id: support-2798-planaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-input-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: ROOT accepted this original current source plan.
  snapshot_sha256: 0e8c34013ec3794cfaa30bcb060b8a8717b99a038f5ba349a893ae7fbc47c2ce
- evidence_id: support-2798-notes
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /curation
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Current notes retain the disjoint source and Native taxonomy/curation interpretations;
    no added primary credit.
  snapshot_sha256: e5b80095d288105ec28103716a87da06b65c083b79bf0fbbac86dc83773a08d4
- evidence_id: support-2798-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/intakes-001/2798-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Actual intake fixes generated target, maintained owners and current relative
    input hashes.
  snapshot_sha256: aac3680442ab340c9f6ffbd27d9253d1078b370126a0be0da132eb3d863e03a8
- evidence_id: support-2798-intakeaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-intake-acceptance-001.json
  locator: /status; /accepted; /intake_summary
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: ROOT accepted all ten original intakes, all exit zero with empty stderr.
  snapshot_sha256: e11e8f952eeb308c816112881974c56ec907ec0a5ee8935ee308347ab2e2d871
- evidence_id: support-2798-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles; /records/7/inchi; /records/7/comparisons; /records/7/atom_correspondence;
    /records/7/literal_InChI_layers; /records/7/formula_comparison_scope
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: 'Both forms contain 32 atoms, 34 bonds and neutral C22H29N5O5. Standard
    InChI, key, formula, charge and counts agree, but both canonical SMILES comparisons
    are false and the limited atom map is empty. Each form retains three rings: a
    14-membered macrocycle, an aromatic six-ring and an aromatic five-membered imidazole
    ring. Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match
    is false and full_graph_identity_established is false.'
  snapshot_sha256: c1725a2a201004679fb5a6b60a3124217de57850698749040b40e46d316502d8
- evidence_id: support-2798-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed/atoms; /records/7/smiles/computed/potential_stereo;
    /records/7/smiles/computed/bonds; /records/7/inchi/computed/atoms; /records/7/inchi/computed/potential_stereo;
    /records/7/inchi/computed/bonds
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Each form retains three specified S tetrahedral centres (S2, S17, S24;
    I14, I15, I16). Two unspecified potential C=N candidates occur in the InChI-derived
    representation. The source atom-stereo flag does not establish a complete natural
    configuration or prove the proposed enzyme's activity.
  snapshot_sha256: c1725a2a201004679fb5a6b60a3124217de57850698749040b40e46d316502d8
- evidence_id: support-2798-motifs
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed/motifs; /records/7/smiles/computed/rings; /records/7/smiles/computed/bonds;
    /records/7/smiles/computed/atoms; /records/7/inchi/computed/motifs; /records/7/inchi/computed/rings;
    /records/7/inchi/computed/bonds; /records/7/inchi/computed/atoms
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The macrocycle contains the aryl-carbon to imidazole-nitrogen linkage S9-N11
    and two peptide amides S22-N21 and S30-N29. In the InChI-derived form those become
    two C-single-O/double-N sites I19-N24-O28 and I20-N25-O29, with zero strict carbonyl
    amides. A free carboxyl, phenolic oxygen and N-methyl secondary amine remain;
    the latter is not a nonamide primary amine. No ester, C-O-C bridge or saturated
    C5O sugar ring is detected by the defined motifs.
  snapshot_sha256: c1725a2a201004679fb5a6b60a3124217de57850698749040b40e46d316502d8
- evidence_id: support-2798-molecularreading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-last-five-molecular-intake-reading-001.json
  locator: /records/2; /counts; /warnings
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete ten saved forms personally read; no molecular replay. Four original
    undefined-stereo warning lines and two proton-addition/removal warning lines remain
    globally unassigned; none is assigned to an individual owner.
  snapshot_sha256: f5ca966135e76b0744ac3f920329e18329eb3fa3c4b384b3606068946a6ac3aa
- evidence_id: support-2798-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Single original diagnostic command and retained streams; no replay.
  snapshot_sha256: fe6b12cc17cb942787983efb14216babe8b2ee52b81adaca8ffaed0d29142fd6
- evidence_id: support-2798-diagaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/root-current280-diagnostic-acceptance-001.json
  locator: /status; /accepted; /diagnostic; /execution
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: ROOT accepted the original stored-form diagnostic.
  snapshot_sha256: 409fc03abfaba0325bf25149704a554a7c7d5fc80f2dd056cca027cd008797c5
- evidence_id: support-2798-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-original-001.stderr
  locator: complete six original warning lines
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Four original undefined-stereo warning lines and two proton-addition/removal
    warning lines remain globally unassigned; none is assigned to an individual owner.
  snapshot_sha256: f6a74ef31a1d327a6a483c87de5d2671dedd256b334e08156260de25ee0a95be
- evidence_id: support-2798-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-cached-taxonomy-reading-001.json
  locator: /context_interpretations/14; /physical_negative_query_scopes/14; /whole_stanzas
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Retain Pyxidicoccus fallax (394095), cached spelling synonym Pyxicoccus
    fallax, and BGC0002631:1/OL539738.1 COMPOUND_EVIDENCE citation. LOTUS occurrence
    has the same taxon and DOI spelling variant but does not establish independent
    publication or production evidence. Historical An d48/MCy8396 sequence claims
    remain attributed.
  snapshot_sha256: 7b3133d38f9f774b7be03c70880701cccf97fa8b6968bb2278462c34f3c47fe0
- evidence_id: support-2798-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-implemented-curation-scan-002.json
  locator: /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows;
    /interpretation
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: No current exact applicable maintained correction; lexical names and unrelated
    BGC rows do not transfer decisions.
  snapshot_sha256: 6ad28a5dd301fac51ee52e70ca0789cd040a1906660932acedd202703d786e11
  search_scope: Native complete nine-table/3422-row bounded scan, exact owner/full-key/BGC/occurrence/assay
    predicates; no new query or universal absence.
- evidence_id: support-2798-producerpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: complete method grading table
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Producer evidence and locus methods answer different questions; unstated
    methods retain their grade.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2798-stereopolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 165-172, atom-centre completeness predicate
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Retained stereo_complete checks unassigned atom centres, not all geometry
    or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2798-filingpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295-306, choose_pathway
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: One supported normalized pathway selects filing; multiple, none or unsupported
    values retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2798-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-five-gates-acceptance-001.json
  locator: /five_local_commands_passed; /all_native_gates_passed; /selected_queue_rows;
    /selected_queue_counts/2798; /unavailable_required_gates
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Five local gates pass, with required QC/OAK unavailable. Actual queue entries
    are diagnostic leads, not automatic scientific findings.
  snapshot_sha256: 7e6f44be6a38a56ec60db94569abcb6d4b76d33133e329930db626e8bbb3f0b8
- evidence_id: support-2798-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json
  locator: /records/7/owner_document/curation_history; /records/7/owner_document/source_concepts
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: 'All four history events are retained: three seeding events and one 2026-10-07
    curation event. The graph has five reference placements, including repeated MITE0000420
    version 1 plus GenPept UID85537.1 and OL539738.1 historical claims. The prior
    795-nt/table-11/264-residue and product-key comparisons are not newly reproduced
    primary or sequence proof. Inaccessible historical papers and bounded historical
    UniProt searches remain qualified attribution, not fresh absence or verification.'
  snapshot_sha256: 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
- evidence_id: support-2798-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-target-input-plan-001.json
  locator: /records/7/complete_root_keys; /records/7/declared_mechanism_roots_literal;
    /records/7/component_paths; /records/7/complete_raw_mechanism_sections
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The accepted complete owner has one four-node, three-edge graph, four histories
    and no biosynthetic_pathway, components or molecular targets. NCBIProtein:UID85537.1
    is a grounded native reference; the cyclized substrate example and methylation
    process remain ungrounded. All edges explicitly qualify BytZ as database-proposed.
    The reader does not validate catalysis, historical CDS identity, leader cleavage,
    BytA/BytO function, full pathway order or physiological finality. No unsupported
    stronger claim is adopted.
  snapshot_sha256: d6777f8dea91c7542347ffaf26f8bc8cc03d93b08032d32861abac52335c3fa3
- evidence_id: support-2798-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved mibig_compounds frame with 1 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "YNCKCZXUTZJZTQ-ULQDDVLXSA-N" only; no source replay or universal absence.
- evidence_id: support-2798-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical line 3358, raw UTF-8 row SHA-256 632a6521f6d4ee23b6cc11d13d8d9e66b2f20abb1c38cc82a51cdb71d0037f61
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The exact YNCKCZXUTZJZTQ-ULQDDVLXSA-N grouping is BGC0002631 version 2,
    compound index 1, with NPAtlas NPA033347. The stored macrocyclic label and full
    key do not independently establish a natural sample or database example product
    match. Pyxidicoccus fallax (394095) remains SOURCE_ASSERTION. The cached Pyxicoccus
    spelling synonym and historical An d48/MCy8396 notes do not supply a new strain,
    sequence or experimental identity check. BGC0002631 version 2, OL539738.1:1-3091,
    retains active/questionable/unknown metadata and CLUSTER_UNSTATED with no method.
    Source RIBOSOMAL/RiPP classification is separate from the proposed BytZ activity.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2798-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved chebi_structures frame with 0 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "YNCKCZXUTZJZTQ-ULQDDVLXSA-N" only; no source replay or universal absence.
- evidence_id: support-2798-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved lotus_occurrences frame with 1 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "YNCKCZXUTZJZTQ-ULQDDVLXSA-N" only; no source replay or universal absence.
- evidence_id: support-2798-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical line 9873, raw UTF-8 row SHA-256 69bc9abe3b04b533bb78fa3c2f0046b52c7c1c82e09778ae527c1cf164a57711
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The LOTUS Pyxidicoccus fallax occurrence cites DOI:10.3390/MOLECULES26247483.
    MIBiG cites DOI:10.3390/molecules26247483 at COMPOUND_EVIDENCE grain. Case variants
    of this DOI do not establish two independent publications or turn occurrence into
    production.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2798-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame with 0 positive placements
    read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "YNCKCZXUTZJZTQ-ULQDDVLXSA-N" only; no source replay or universal absence.
- evidence_id: support-2798-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved npclassifier frame with 1 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "YNCKCZXUTZJZTQ-ULQDDVLXSA-N" only; no source replay or universal absence.
- evidence_id: support-2798-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical line 2946, raw UTF-8 row SHA-256 81e7c93386542e906c3dcfc2f2ca03cc1a81cb9a23972b01a7af47ab95f72d2f
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The source Macrocyclic and RIBOSOMAL labels are separate from model Alkaloids
    plus Amino acids and Peptides, Oligopeptides/Histidine alkaloids and Cyclic peptides/Imidazole
    alkaloids. The saved macrocycle and imidazole support the limited structural description,
    while the two-pathway result correctly retains UNCLASSIFIED. False glycoside is
    a model value; motif negatives are bounded.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2798-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame with 0 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "YNCKCZXUTZJZTQ-ULQDDVLXSA-N" only; no source replay or universal absence.
- evidence_id: support-2798-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved bindingdb_targets frame with 0 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "YNCKCZXUTZJZTQ-ULQDDVLXSA-N" only; no source replay or universal absence.
- evidence_id: support-2798-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame with 0 positive placements
    read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "YNCKCZXUTZJZTQ-ULQDDVLXSA-N" only; no source replay or universal absence.
- evidence_id: support-2798-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved chebi_origins frame with 0 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact chebi_id from exact full-key structure
    rows and query [] only; no source replay or universal absence.
- evidence_id: support-2798-reader-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/native-current280-myxarylin-maintained-reader-DATA-001.json
  locator: /raw_owner; /resolved_view; /expected_view; /counts; /reader_call_count;
    /denials; /unexpected_denials; /errors
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The accepted complete owner has one four-node, three-edge graph, four histories
    and no biosynthetic_pathway, components or molecular targets. NCBIProtein:UID85537.1
    is a grounded native reference; the cyclized substrate example and methylation
    process remain ungrounded. All edges explicitly qualify BytZ as database-proposed.
    The reader does not validate catalysis, historical CDS identity, leader cleavage,
    BytA/BytO function, full pathway order or physiological finality. No unsupported
    stronger claim is adopted. Whole returned owner equals accepted capture; no primary
    or scientific validation follows.
  snapshot_sha256: 0c4da43ed1cbaa0ebf4301f36ebb8aedf8d032b3c8f955ff024533ba993e942d
- evidence_id: support-2798-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/native-current280-myxarylin-reader-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: One original offline maintained call, zero exit and stderr; known socket
    construction denied before action, no requests.
  snapshot_sha256: d3a47e503be3f736e56dc73be99347c5dc149c0476007d8baaee87e764a9dc04
- evidence_id: support-2798-reader-accept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-myxarylin-reader-acceptance-001.json
  locator: /status; /accepted; /DATA; /execution; /review_check_contract; /limits
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: ROOT accepted the complete returned owner and exact check contract; interpretation
    remains separate.
  snapshot_sha256: 3ec5d7dd8be065b4ad806df6e2b8815bbb3f95f3188b097ef4f6af90c8e99119
- evidence_id: support-2798-reader-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-last-five-maintained-reader-reading-001.json
  locator: /records/1
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: review_support read every returned owner, graph, node, edge, evidence,
    pathway and history value.
  snapshot_sha256: 3fa3bc413bd887941dbb4e55bd97ee4600bee153f430a46fb015b886843cf832
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:58:35.720629Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 11c07976d94801b8044a911f854cef59d220d80dafabd86673396f6a1ee54ae4
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:58:59.871180Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 54b4e29921ed94b48337f9938b95ac8c403d840bd704ec9c7c3c6fe215016937
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:59:19.061941Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:59:52.340365Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-07T00:00:03.873381Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: b0c41dbce9d0cef868a144aadc058261eb329ecea06a3affb0e50465adf478e0
assessments:
- assessment_id: support-2798-identity-assessment
  area: identity
  topic: Exact retained compound grounding
  summary: The exact YNCKCZXUTZJZTQ-ULQDDVLXSA-N grouping is BGC0002631 version 2,
    compound index 1, with NPAtlas NPA033347. The stored macrocyclic label and full
    key do not independently establish a natural sample or database example product
    match.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  evidence_ids:
  - support-2798-owner
  - support-2798-capture
  - support-2798-source
  - support-2798-intake
  - support-2798-curation
  - support-2798-table-mibig_compounds
  - support-2798-table-lotus_occurrences
  - support-2798-table-npclassifier
  dimensions:
  - name: standard_inchi_key
    definition: Full key rather than label matching.
    value: YNCKCZXUTZJZTQ-ULQDDVLXSA-N
    evidence_ids:
    - support-2798-owner
    - support-2798-capture
    - support-2798-source
    - support-2798-intake
    - support-2798-curation
    - support-2798-table-mibig_compounds
    - support-2798-table-lotus_occurrences
    - support-2798-table-npclassifier
  - name: grounding_scope
    definition: Retained source identity is distinct from natural identity.
    value: The exact YNCKCZXUTZJZTQ-ULQDDVLXSA-N grouping is BGC0002631 version 2,
      compound index 1, with NPAtlas NPA033347. The stored macrocyclic label and full
      key do not independently establish a natural sample or database example product
      match.
    evidence_ids:
    - support-2798-owner
    - support-2798-capture
    - support-2798-source
    - support-2798-intake
    - support-2798-curation
    - support-2798-table-mibig_compounds
    - support-2798-table-lotus_occurrences
    - support-2798-table-npclassifier
- assessment_id: support-2798-representation-assessment
  area: representation
  topic: Saved molecular forms and stereochemical scope
  summary: 'Both forms contain 32 atoms, 34 bonds and neutral C22H29N5O5. Standard
    InChI, key, formula, charge and counts agree, but both canonical SMILES comparisons
    are false and the limited atom map is empty. Each form retains three rings: a
    14-membered macrocycle, an aromatic six-ring and an aromatic five-membered imidazole
    ring. The macrocycle contains the aryl-carbon to imidazole-nitrogen linkage S9-N11
    and two peptide amides S22-N21 and S30-N29. In the InChI-derived form those become
    two C-single-O/double-N sites I19-N24-O28 and I20-N25-O29, with zero strict carbonyl
    amides. A free carboxyl, phenolic oxygen and N-methyl secondary amine remain;
    the latter is not a nonamide primary amine. No ester, C-O-C bridge or saturated
    C5O sugar ring is detected by the defined motifs. Both canonical SMILES comparisons
    are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established
    is false. Normalized key/formula agreement and a successful local process do not
    establish independent full graph identity, natural-sample identity, experimental
    absolute stereochemistry, primary mechanism validation or a native status promotion.'
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  evidence_ids:
  - support-2798-data
  - support-2798-stereo
  - support-2798-motifs
  - support-2798-molecularreading
  - support-2798-execution
  - support-2798-diagaccept
  - support-2798-stereopolicy
  dimensions:
  - name: stereochemistry_scope
    definition: Specified atom centres and representation-dependent candidates remain
      distinct.
    value: Each form retains three specified S tetrahedral centres (S2, S17, S24;
      I14, I15, I16). Two unspecified potential C=N candidates occur in the InChI-derived
      representation. The source atom-stereo flag does not establish a complete natural
      configuration or prove the proposed enzyme's activity.
    evidence_ids:
    - support-2798-data
    - support-2798-stereo
    - support-2798-motifs
    - support-2798-molecularreading
    - support-2798-execution
    - support-2798-diagaccept
    - support-2798-stereopolicy
  - name: representation_correspondence
    definition: Saved limited comparison, not full identity.
    value: Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match
      is false and full_graph_identity_established is false. Normalized key/formula
      agreement and a successful local process do not establish independent full graph
      identity, natural-sample identity, experimental absolute stereochemistry, primary
      mechanism validation or a native status promotion.
    evidence_ids:
    - support-2798-data
    - support-2798-stereo
    - support-2798-motifs
    - support-2798-molecularreading
    - support-2798-execution
    - support-2798-diagaccept
    - support-2798-stereopolicy
- assessment_id: support-2798-provenance-assessment
  area: provenance
  topic: Compound-specific producer, locus and taxon
  summary: Pyxidicoccus fallax (394095) remains SOURCE_ASSERTION. The cached Pyxicoccus
    spelling synonym and historical An d48/MCy8396 notes do not supply a new strain,
    sequence or experimental identity check. BGC0002631 version 2, OL539738.1:1-3091,
    retains active/questionable/unknown metadata and CLUSTER_UNSTATED with no method.
    Source RIBOSOMAL/RiPP classification is separate from the proposed BytZ activity.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  evidence_ids:
  - support-2798-source
  - support-2798-capture
  - support-2798-taxonomy
  - support-2798-curation
  - support-2798-producerpolicy
  - support-2798-table-mibig_compounds
  - support-2798-table-lotus_occurrences
  - support-2798-table-npclassifier
  dimensions:
  - name: taxon_scope
    definition: Cached names do not establish current lineage or strain equivalence.
    value: Retain Pyxidicoccus fallax (394095), cached spelling synonym Pyxicoccus
      fallax, and BGC0002631:1/OL539738.1 COMPOUND_EVIDENCE citation. LOTUS occurrence
      has the same taxon and DOI spelling variant but does not establish independent
      publication or production evidence. Historical An d48/MCy8396 sequence claims
      remain attributed.
    evidence_ids:
    - support-2798-source
    - support-2798-capture
    - support-2798-taxonomy
    - support-2798-curation
    - support-2798-producerpolicy
    - support-2798-table-mibig_compounds
    - support-2798-table-lotus_occurrences
    - support-2798-table-npclassifier
  - name: producer_evidence
    definition: Producer and locus evidence remain separate.
    value: Pyxidicoccus fallax (394095) remains SOURCE_ASSERTION. The cached Pyxicoccus
      spelling synonym and historical An d48/MCy8396 notes do not supply a new strain,
      sequence or experimental identity check.
    evidence_ids:
    - support-2798-source
    - support-2798-capture
    - support-2798-taxonomy
    - support-2798-curation
    - support-2798-producerpolicy
    - support-2798-table-mibig_compounds
    - support-2798-table-lotus_occurrences
    - support-2798-table-npclassifier
  - name: locus_evidence
    definition: Exact source version, endpoints and methods delimit the claim.
    value: BGC0002631 version 2, OL539738.1:1-3091, retains active/questionable/unknown
      metadata and CLUSTER_UNSTATED with no method. Source RIBOSOMAL/RiPP classification
      is separate from the proposed BytZ activity.
    evidence_ids:
    - support-2798-source
    - support-2798-capture
    - support-2798-taxonomy
    - support-2798-curation
    - support-2798-producerpolicy
    - support-2798-table-mibig_compounds
    - support-2798-table-lotus_occurrences
    - support-2798-table-npclassifier
- assessment_id: support-2798-citations-assessment
  area: evidence
  topic: Citation grain and retained history
  summary: 'All four history events are retained: three seeding events and one 2026-10-07
    curation event. The graph has five reference placements, including repeated MITE0000420
    version 1 plus GenPept UID85537.1 and OL539738.1 historical claims. The prior
    795-nt/table-11/264-residue and product-key comparisons are not newly reproduced
    primary or sequence proof. Inaccessible historical papers and bounded historical
    UniProt searches remain qualified attribution, not fresh absence or verification.'
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  evidence_ids:
  - support-2798-owner
  - support-2798-source
  - support-2798-capture
  - support-2798-history
  - support-2798-table-mibig_compounds
  - support-2798-table-lotus_occurrences
  - support-2798-table-npclassifier
  dimensions:
  - name: citation_scope
    definition: Repeated annotations are not independent primary proof.
    value: 'All four history events are retained: three seeding events and one 2026-10-07
      curation event. The graph has five reference placements, including repeated
      MITE0000420 version 1 plus GenPept UID85537.1 and OL539738.1 historical claims.
      The prior 795-nt/table-11/264-residue and product-key comparisons are not newly
      reproduced primary or sequence proof. Inaccessible historical papers and bounded
      historical UniProt searches remain qualified attribution, not fresh absence
      or verification.'
    evidence_ids:
    - support-2798-owner
    - support-2798-source
    - support-2798-capture
    - support-2798-history
    - support-2798-table-mibig_compounds
    - support-2798-table-lotus_occurrences
    - support-2798-table-npclassifier
- assessment_id: support-2798-occurrence-assay-assessment
  area: evidence
  topic: Occurrence and assay limits
  summary: The LOTUS Pyxidicoccus fallax occurrence cites DOI:10.3390/MOLECULES26247483.
    MIBiG cites DOI:10.3390/molecules26247483 at COMPOUND_EVIDENCE grain. Case variants
    of this DOI do not establish two independent publications or turn occurrence into
    production. No retained PubChem AID, BindingDB target or AntibioticMech full-key
    row is present in the saved frames. The proposed methyltransferase context is
    not an assay magnitude, target-binding result, knockout phenotype or physiological
    cofactor assignment.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  evidence_ids:
  - support-2798-source
  - support-2798-taxonomy
  - support-2798-curation
  - support-2798-query-mibig_compounds
  - support-2798-query-chebi_structures
  - support-2798-query-lotus_occurrences
  - support-2798-query-cyanometdb_occurrences
  - support-2798-query-npclassifier
  - support-2798-query-pubchem_bioassay
  - support-2798-query-bindingdb_targets
  - support-2798-query-antibioticmech_inchikeys
  - support-2798-query-chebi_origins
  dimensions:
  - name: occurrence_scope
    definition: Occurrence does not establish production.
    value: The LOTUS Pyxidicoccus fallax occurrence cites DOI:10.3390/MOLECULES26247483.
      MIBiG cites DOI:10.3390/molecules26247483 at COMPOUND_EVIDENCE grain. Case variants
      of this DOI do not establish two independent publications or turn occurrence
      into production.
    evidence_ids:
    - support-2798-source
    - support-2798-taxonomy
    - support-2798-curation
    - support-2798-query-mibig_compounds
    - support-2798-query-chebi_structures
    - support-2798-query-lotus_occurrences
    - support-2798-query-cyanometdb_occurrences
    - support-2798-query-npclassifier
    - support-2798-query-pubchem_bioassay
    - support-2798-query-bindingdb_targets
    - support-2798-query-antibioticmech_inchikeys
    - support-2798-query-chebi_origins
  - name: assay_target_scope
    definition: Blank sentinels and bounded negatives are not inactivity.
    value: No retained PubChem AID, BindingDB target or AntibioticMech full-key row
      is present in the saved frames. The proposed methyltransferase context is not
      an assay magnitude, target-binding result, knockout phenotype or physiological
      cofactor assignment.
    evidence_ids:
    - support-2798-source
    - support-2798-taxonomy
    - support-2798-curation
    - support-2798-query-mibig_compounds
    - support-2798-query-chebi_structures
    - support-2798-query-lotus_occurrences
    - support-2798-query-cyanometdb_occurrences
    - support-2798-query-npclassifier
    - support-2798-query-pubchem_bioassay
    - support-2798-query-bindingdb_targets
    - support-2798-query-antibioticmech_inchikeys
    - support-2798-query-chebi_origins
- assessment_id: support-2798-classification-assessment
  area: consistency
  topic: Source classes, model labels and filing
  summary: The source Macrocyclic and RIBOSOMAL labels are separate from model Alkaloids
    plus Amino acids and Peptides, Oligopeptides/Histidine alkaloids and Cyclic peptides/Imidazole
    alkaloids. The saved macrocycle and imidazole support the limited structural description,
    while the two-pathway result correctly retains UNCLASSIFIED. False glycoside is
    a model value; motif negatives are bounded.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  evidence_ids:
  - support-2798-source
  - support-2798-owner
  - support-2798-motifs
  - support-2798-filingpolicy
  - support-2798-gates
  - support-2798-table-mibig_compounds
  - support-2798-table-lotus_occurrences
  - support-2798-table-npclassifier
  dimensions:
  - name: classification_applicability
    definition: Model, source and saved topology are separate evidence.
    value: The source Macrocyclic and RIBOSOMAL labels are separate from model Alkaloids
      plus Amino acids and Peptides, Oligopeptides/Histidine alkaloids and Cyclic
      peptides/Imidazole alkaloids. The saved macrocycle and imidazole support the
      limited structural description, while the two-pathway result correctly retains
      UNCLASSIFIED. False glycoside is a model value; motif negatives are bounded.
    evidence_ids:
    - support-2798-source
    - support-2798-owner
    - support-2798-motifs
    - support-2798-filingpolicy
    - support-2798-gates
    - support-2798-table-mibig_compounds
    - support-2798-table-lotus_occurrences
    - support-2798-table-npclassifier
- assessment_id: support-2798-mechanism-assessment
  area: consistency
  topic: Complete retained mechanism and owner scope
  summary: The accepted complete owner has one four-node, three-edge graph, four histories
    and no biosynthetic_pathway, components or molecular targets. NCBIProtein:UID85537.1
    is a grounded native reference; the cyclized substrate example and methylation
    process remain ungrounded. All edges explicitly qualify BytZ as database-proposed.
    The reader does not validate catalysis, historical CDS identity, leader cleavage,
    BytA/BytO function, full pathway order or physiological finality. No unsupported
    stronger claim is adopted.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  evidence_ids:
  - support-2798-scope
  - support-2798-reader-data
  - support-2798-reader-execution
  - support-2798-reader-accept
  - support-2798-reader-reading
  dimensions: []
- assessment_id: support-2798-completion-assessment
  area: completeness
  topic: Earned work and unavailable authority
  summary: Complete assigned raw/source/intake and both saved molecular forms were
    read. The required original maintained reader returned the complete owner; preservation
    does not verify mechanism science. Five local native commands pass; full QC, complete
    OAK and fresh primary verification remain unavailable. Completion is partial,
    native SEEDED status unchanged.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-489bd6e2d9
  evidence_ids:
  - support-2798-intake
  - support-2798-intakeaccept
  - support-2798-plan
  - support-2798-planaccept
  - support-2798-notes
  - support-2798-gates
  - support-2798-data
  - support-2798-diagaccept
  - support-2798-scope
  dimensions:
  - name: review_completion
    definition: Local review does not promote native status or substitute for unavailable
      checks.
    value: Complete assigned raw/source/intake and both saved molecular forms were
      read. The required original maintained reader returned the complete owner; preservation
      does not verify mechanism science. Five local native commands pass; full QC,
      complete OAK and fresh primary verification remain unavailable. Completion is
      partial, native SEEDED status unchanged.
    evidence_ids:
    - support-2798-intake
    - support-2798-intakeaccept
    - support-2798-plan
    - support-2798-planaccept
    - support-2798-notes
    - support-2798-gates
    - support-2798-data
    - support-2798-diagaccept
    - support-2798-scope
findings: []
actions: []
limitations:
- Normalized key/formula agreement and a successful local process do not establish
  independent full graph identity, natural-sample identity, experimental absolute
  stereochemistry, primary mechanism validation or a native status promotion.
- Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match
  is false and full_graph_identity_established is false. Each form retains three specified
  S tetrahedral centres (S2, S17, S24; I14, I15, I16). Two unspecified potential C=N
  candidates occur in the InChI-derived representation. The source atom-stereo flag
  does not establish a complete natural configuration or prove the proposed enzyme's
  activity.
- Four original undefined-stereo warning lines and two proton-addition/removal warning
  lines remain globally unassigned; none is assigned to an individual owner.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK
  remain unavailable; source/database claims retain their exact authority.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh current 280 evidence and judgments; prior batches provide interface logic
  only.
- No source row, record, campaign or native status was changed; no query, molecular
  parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual native checks and three required unavailable checks; only
  orders 2797 and 2798 in this fragment receive actual maintained-reader checks.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-280
```
