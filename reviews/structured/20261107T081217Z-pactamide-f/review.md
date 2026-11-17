# Local evidence review: pactamide F

- Review: 20261107T081217Z-pactamide-f
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T07:42:09.812244Z
- Finished UTC: 2026-11-07T08:12:17.163914Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Pactamide F retains a chloromethyl substituent, nine specified atom stereocentres and its distinct full source key. Two amide/imidic changes explain the saved canonical difference, with unresolved bond geometry preserved. The local evidence supports a qualified partial pass without a new material finding.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2858; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-59b7206fd7 | data/natural_products/unclassified/pactamide-f.yaml | generated | pactamide F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-59b7206fd7 | Both stored forms parsed and retained declared key/formula agreement. Both canonical SMILES comparisons are false; the chirality-aware map is empty and complete_atom_count_match/full_graph_identity_established remain false. |
| strict_ten | passed | True | naturalproductmech:mibig-59b7206fd7 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-59b7206fd7 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-59b7206fd7 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-59b7206fd7 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-59b7206fd7 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-59b7206fd7 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-59b7206fd7 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-59b7206fd7 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained compound grounding

identity: supported. Targets: naturalproductmech:mibig-59b7206fd7.

BGC0001726 version 4 compound index 6 grounds pactamide F, full key BRNQMLSKMSMSQY-QLIRVBKLSA-N, PubChem CID 146684580 and NPAtlas NPA028480. Its chlorine-containing formula and distinct complete key remain separate from the other selected Pactamides.

### Saved forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-59b7206fd7.

Both saved forms are neutral C29H39ClN2O5 with 37 atoms and 41 bonds. Five saved ring rows have sizes 5, 5, 6, 16 and 5 and cycle rank five. Two strict amides and three carbonyls in SMILES become two C(OH)=N motifs and one carbonyl in the InChI form. The chloromethyl and hydroxylated quaternary centre persist; no intercongener biosynthetic transformation is inferred. SMILES C9 bears OH12 and chloromethyl C10-Cl11; the InChI form retains C28-O36H and C14-Cl29. Amides C20(=O21)-N22 and C34(=O35)-N36 shift to InChI C23(OH33)=N30 and C27(OH35)=N31. The ketone remains. No ester, acid, free primary amine, saturated C5O candidate sugar, phosphorus or metal is present; functional-pattern comparison is not a full atom correspondence. Both canonical SMILES comparisons are false; the chirality-aware map is empty and complete_atom_count_match/full_graph_identity_established remain false. Normalized identifiers, formula agreement and local parsing do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry or primary biological validation.

### Producer, locus and taxon claim grain

provenance: supported. Targets: naturalproductmech:mibig-59b7206fd7.

Streptomyces pactum NCBITaxon:68249 remains the source-asserted producer, distinct in evidentiary role from the LOTUS occurrence. BGC0001726 version 4 is active with questionable quality and unknown completeness. The KU569222.1 NRPS&#124;PKS/Type I&#124;Unknown locus retains blank methods and coordinates and CLUSTER_UNSTATED; no experimental or complete-route upgrade is supported.

### Citation grain and retained history

evidence: supported. Targets: naturalproductmech:mibig-59b7206fd7.

PMID:28451290 is COMPOUND_EVIDENCE. LOTUS DOI:10.1039/C6SC03875A and the three seed events do not add independently verified experiments.

### Occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-59b7206fd7.

LOTUS row 577 retains Streptomyces pactum 68249 and organism Q26291629 with DOI:10.1039/C6SC03875A. Publication independence and causal production remain unestablished. PubChem row 862 has CID 146684580 and a blank AID/no-assay marker. Empty endpoints and other negative frames provide no activity, inactivity or target measurement.

### Source classes, model labels and filing

consistency: supported. Targets: naturalproductmech:mibig-59b7206fd7.

MIBiG supplies Ornithine-derived, Tetramate alkaloid, Cyclic polyketide and Macrocyclic polyketide. NPClassifier gives Amino acids and Peptides plus Polyketides, Macrolides, Macrocyclic tetramic acids and is_glycoside:false. These retained predictions and source classes describe different evidence scopes; multiple model pathways retain UNCLASSIFIED.

### Earned work and unavailable authority

completeness: supported. Targets: naturalproductmech:mibig-59b7206fd7.

The complete owner, assigned source payloads, current canonical intake and both saved forms were read. The complete owner lacks causal_graphs, causal_graph_refs, biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary, related_records and components. No maintained reader applies to this owner. This scoped absence does not assert absent biology; the two Oxepinamide reader routes elsewhere in batch 286 confer no authority on this record. No additional material local defect was established in this earned scope. Five local gates pass; full QC, complete OAK and fresh primary/external verification are unavailable. Completion is partial and native SEEDED status is unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2858-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-f.yaml; complete file: identity, chemical_structure, producer/locus/occurrence, source_concepts, discussion and history | supports | Complete current generated owner; source scopes and open discussions retained. |
| support-2858-capture | /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json; /records/7/owner_document | supports | Original whole owner capture with all source concepts and history. |
| support-2858-source | /private/tmp/npm-review-work/shared-next-batch286-tentative/support-prep/support-current286-assigned-source-reading-001.json; /contexts/2; /counts; /global_cautions | supports | Own disjoint last-five reading: 33 rows, 318 fields, 45 frames, 26 negatives, 13 histories; four blank AID markers and no actual assay row. |
| support-2858-plan | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-target-input-plan-001.json; /records/7; /source_placement_count; /unique_source_path_count | supports | Accepted 474-placement/55-path plan; 49 actual inputs for this owner. |
| support-2858-planaccept | /private/tmp/npm-review-work/shared-next-batch286/root-current286-source-plan-acceptance-001.json; /accepted; /plan; /status | supports | ROOT accepted the original current plan. |
| support-2858-notes | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /curation | supports | Disjoint BGC 19 plus Support 33 rows total 52 rows and 547 fields. Native taxonomy/curation adds no primary-row credit. |
| support-2858-intake | /private/tmp/npm-review-work/shared-next-batch286/intakes-001/2858-inspect-001.json; /status; /source; /targets | supports | Original canonical intake fixes the current hashes and maintained owner roles. |
| support-2858-intakeaccept | /private/tmp/npm-review-work/shared-next-batch286/root-current286-intake-acceptance-001.json; /accepted; /status; /intake_summary; /records | supports | Ten original intakes passed with the actual current input maps. |
| support-2858-data | /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles; /records/7/inchi; /records/7/comparisons; /records/7/atom_correspondence; /records/7/literal_InChI_layers; /records/7/formula_comparison_scope | supports | Both saved forms are neutral C29H39ClN2O5 with 37 atoms and 41 bonds. Five saved ring rows have sizes 5, 5, 6, 16 and 5 and cycle rank five. Two strict amides and three carbonyls in SMILES become two C(OH)=N motifs and one carbonyl in the InChI form. The chloromethyl and hydroxylated quaternary centre persist; no intercongener biosynthetic transformation is inferred. Both canonical SMILES comparisons are false; the chirality-aware map is empty and complete_atom_count_match/full_graph_identity_established remain false. |
| support-2858-stereo | /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed/atoms; /records/7/smiles/computed/bonds; /records/7/smiles/computed/potential_stereo; /records/7/smiles/computed/stereo_counts; /records/7/inchi/computed/atoms; /records/7/inchi/computed/bonds; /records/7/inchi/computed/potential_stereo; /records/7/inchi/computed/stereo_counts | supports | Both encodings retain nine specified tetrahedral candidates and one actual STEREOZ plus one STEREOE bond. The source enol/tetramate double remains geometrically unspecified; the InChI form records it as unknown and adds one unspecified imidic candidate. The true source stereo_complete flag applies to atom centres, not all double-bond geometries or natural absolute configuration. |
| support-2858-motifs | /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed/atoms; /records/7/smiles/computed/bonds; /records/7/smiles/computed/rings; /records/7/smiles/computed/motifs; /records/7/inchi/computed/atoms; /records/7/inchi/computed/bonds; /records/7/inchi/computed/rings; /records/7/inchi/computed/motifs | supports | SMILES C9 bears OH12 and chloromethyl C10-Cl11; the InChI form retains C28-O36H and C14-Cl29. Amides C20(=O21)-N22 and C34(=O35)-N36 shift to InChI C23(OH33)=N30 and C27(OH35)=N31. The ketone remains. No ester, acid, free primary amine, saturated C5O candidate sugar, phosphorus or metal is present; functional-pattern comparison is not a full atom correspondence. |
| support-2858-molecularreading | /private/tmp/npm-review-work/shared-next-batch286-tentative/support-prep/support-current286-last-five-molecular-intake-reading-001.json; /records/2; /counts; /interpretations/2858; /warnings | supports | All ten saved forms personally read: 514 atoms, 548 bonds, 46 ring rows and 127 potential-stereo entries; no reparse. |
| support-2858-execution | /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /retries; /stderr | supports | One original diagnostic exited zero, with no retry. |
| support-2858-diagaccept | /private/tmp/npm-review-work/shared-next-batch286/root-current286-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /scope | supports | ROOT accepted the original technical outputs without a scientific identity claim. |
| support-2858-stderr | /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-original-001.stderr; complete original empty stderr stream | supports | The original diagnostic stderr is empty. No warning is invented or assigned to an owner. |
| support-2858-taxonomy | /private/tmp/npm-review-work/shared-next-batch286-tentative/native-prep/native-current286-cached-taxonomy-reading-001.json; /context_interpretations/7; /physical_negative_query_scopes/7; /whole_stanzas | supports | Attributed Native cached-name reading: NCBITaxon:68249 = Streptomyces pactum. These complete retained stanzas contain names and synonyms, not fresh rank/lineage, strain equivalence or experimental production. Exact merge and nonorganism predicates are negative. |
| support-2858-curation | /private/tmp/npm-review-work/shared-next-batch286-tentative/native-prep/native-current286-implemented-curation-scan-001.json; /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows; /interpretation | supports | Nine substantive curation tables have no exact applicable decision for these current owners. Generic lexical matches do not apply a correction. |
| support-2858-producerpolicy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; complete retained source-method grading table | supports | Source assertion and CLUSTER_UNSTATED remain separate from causal producer or demonstrated locus evidence. |
| support-2858-stereopolicy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142-173 structure_fields, specifically 165-172 atom-centre predicate | supports | FindMolChiralCenters unknown atom tags determine stereo_complete; full E/Z and natural identity are not certified. |
| support-2858-filingpolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306 choose_pathway | supports | One supported model pathway files a record; multiple, absent or unsupported results retain UNCLASSIFIED. |
| support-2858-gates | /private/tmp/npm-review-work/shared-next-batch286/root-current286-five-gates-acceptance-001.json; /accepted; /five_local_commands_passed; /denominators; /unavailable_required_gates; /all_native_gates_passed | supports | Five local gates pass; full QC and complete OAK remain unavailable. Queue leads are not scientific findings. |
| support-2858-history | /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json; /records/7/owner_document/curation_history; /records/7/owner_document/source_concepts | supports | PMID:28451290 is COMPOUND_EVIDENCE. LOTUS DOI:10.1039/C6SC03875A and the three seed events do not add independently verified experiments. |
| support-2858-scope | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-target-input-plan-001.json; /records/7/complete_root_keys; /records/7/declared_mechanism_roots_literal; /records/7/component_paths | supports | The complete owner lacks causal_graphs, causal_graph_refs, biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary, related_records and components. No maintained reader applies to this owner. This scoped absence does not assert absent biology; the two Oxepinamide reader routes elsewhere in batch 286 confer no authority on this record. |
| support-2858-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/mibig_compounds | supports | Whole saved mibig_compounds frame: 1 positive placements. |
| support-2858-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical line 2048, raw UTF-8 row SHA-256 271cadb14b0efa5ad1ab537b966c190b2f97700a4a9cc750513bf316acc7fe5d | supports | BGC0001726 version 4 compound index 6 grounds pactamide F, full key BRNQMLSKMSMSQY-QLIRVBKLSA-N, PubChem CID 146684580 and NPAtlas NPA028480. Its chlorine-containing formula and distinct complete key remain separate from the other selected Pactamides. Streptomyces pactum NCBITaxon:68249 remains the source-asserted producer, distinct in evidentiary role from the LOTUS occurrence. BGC0001726 version 4 is active with questionable quality and unknown completeness. The KU569222.1 NRPS&#124;PKS/Type I&#124;Unknown locus retains blank methods and coordinates and CLUSTER_UNSTATED; no experimental or complete-route upgrade is supported. |
| support-2858-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_structures | supports | Whole saved chebi_structures frame: 0 positive placements. |
| support-2858-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/lotus_occurrences | supports | Whole saved lotus_occurrences frame: 1 positive placements. |
| support-2858-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical line 577, raw UTF-8 row SHA-256 57c2e20c299518738cd645754bb44f60c0bffab33ffeae53a8adfe120e1a617d | supports | LOTUS row 577 retains Streptomyces pactum 68249 and organism Q26291629 with DOI:10.1039/C6SC03875A. Publication independence and causal production remain unestablished. |
| support-2858-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences | supports | Whole saved cyanometdb_occurrences frame: 0 positive placements. |
| support-2858-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/npclassifier | supports | Whole saved npclassifier frame: 1 positive placements. |
| support-2858-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical line 216, raw UTF-8 row SHA-256 d3fd5c38b9149f89615074d8218f95a789fdca64637ef1c5cdb5ce8c14157fc5 | supports | MIBiG supplies Ornithine-derived, Tetramate alkaloid, Cyclic polyketide and Macrocyclic polyketide. NPClassifier gives Amino acids and Peptides plus Polyketides, Macrolides, Macrocyclic tetramic acids and is_glycoside:false. These retained predictions and source classes describe different evidence scopes; multiple model pathways retain UNCLASSIFIED. |
| support-2858-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/pubchem_bioassay | supports | Whole saved pubchem_bioassay frame: 1 positive placements. |
| support-2858-table-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical line 862, raw UTF-8 row SHA-256 278e9942e85dbc42e027352cbb5c758aaa33c58dd7d77ddebab018c43edd6c4e | supports | PubChem row 862 has CID 146684580 and a blank AID/no-assay marker. Empty endpoints and other negative frames provide no activity, inactivity or target measurement. |
| support-2858-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/bindingdb_targets | supports | Whole saved bindingdb_targets frame: 0 positive placements. |
| support-2858-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Whole saved antibioticmech_inchikeys frame: 0 positive placements. |
| support-2858-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_origins | supports | Whole saved chebi_origins frame: 0 positive placements. |
| support-2858-companion-0 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-a.yaml; complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters; whole raw reading attributed in current source scope | supports | Direct selected Pactamide shared-BGC context with distinct full key; no identity, stereo, assay, producer grade or pathway transfer. Primary source reading is assigned once per owner. |
| support-2858-companion-1 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-b.yaml; complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters; whole raw reading attributed in current source scope | supports | Direct selected Pactamide shared-BGC context with distinct full key; no identity, stereo, assay, producer grade or pathway transfer. Primary source reading is assigned once per owner. |
| support-2858-companion-2 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-c.yaml; complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters; whole raw reading attributed in current source scope | supports | Direct selected Pactamide shared-BGC context with distinct full key; no identity, stereo, assay, producer grade or pathway transfer. Primary source reading is assigned once per owner. |
| support-2858-companion-3 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-d.yaml; complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters; whole raw reading attributed in current source scope | supports | Direct selected Pactamide shared-BGC context with distinct full key; no identity, stereo, assay, producer grade or pathway transfer. Primary source reading is assigned once per owner. |
| support-2858-companion-4 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-e.yaml; complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters; whole raw reading attributed in current source scope | supports | Direct selected Pactamide shared-BGC context with distinct full key; no identity, stereo, assay, producer grade or pathway transfer. Primary source reading is assigned once per owner. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-286/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-286/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-286/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-286/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-286/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Normalized identifiers, formula agreement and local parsing do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry or primary biological validation.
- Both canonical SMILES comparisons are false; the chirality-aware map is empty and complete_atom_count_match/full_graph_identity_established remain false. Both encodings retain nine specified tetrahedral candidates and one actual STEREOZ plus one STEREOE bond. The source enol/tetramate double remains geometrically unspecified; the InChI form records it as unknown and adds one unspecified imidic candidate. The true source stereo_complete flag applies to atom centres, not all double-bond geometries or natural absolute configuration.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK remain unavailable. Source assertions retain their original grades and unresolved questions.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh batch 286 evidence and judgments; batch 285 supplies schema interface only.
- No record, native status or history was edited and no source query, molecular parse, target invocation or external request occurred in this lane.
- ROOT appends five actual local gate checks and three required unavailable checks. No maintained-reader check applies to these five owners.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T081217Z-pactamide-f
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: pactamide F'
started_at: '2026-11-07T07:42:09.812244Z'
finished_at: '2026-11-07T08:12:17.163914Z'
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
summary: Pactamide F retains a chloromethyl substituent, nine specified atom stereocentres
  and its distinct full source key. Two amide/imidic changes explain the saved canonical
  difference, with unresolved bond geometry preserved. The local evidence supports
  a qualified partial pass without a new material finding.
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
  - path: data/natural_products/unclassified/pactamide-a.yaml
    sha256: a8418e6c5c3f77863f237b6eb29235b859474f8740b4cf4bde541d258d6edaee
    role: context
  - path: data/natural_products/unclassified/pactamide-b.yaml
    sha256: 063e98ee16c19bc8a78df5ebac39150bfb9a51394a691a579e17c95e1ee5f443
    role: context
  - path: data/natural_products/unclassified/pactamide-c.yaml
    sha256: f16e70c83d939186646e73c741504996a32822774d3ec77639c0785824b39091
    role: context
  - path: data/natural_products/unclassified/pactamide-d.yaml
    sha256: 6631bd4a1e85637fa7b3719a5bcc831f92781909ec93adbb1705c665c20de24b
    role: context
  - path: data/natural_products/unclassified/pactamide-e.yaml
    sha256: 5be823189b24d168545dd55165c20d2f76b89542bf79450d07825acd66bccb29
    role: context
  - path: data/natural_products/unclassified/pactamide-f.yaml
    sha256: 36c2649a8b27959345b32152c709513e2b047b127de3e25090c41b0636b4c3e8
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
  selection: Campaign path order 2858; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-59b7206fd7
targets:
- target_id: naturalproductmech:mibig-59b7206fd7
  path: data/natural_products/unclassified/pactamide-f.yaml
  label: pactamide F
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnose286-001.py
    900fe8c8d280fbdd52892c2adbd241fe97c4163dd4dfba325ff9ce52a0f39abd deda858259c8e3df482e115d881fc4ab92d28aa7ff577fb2172fe55afb74327f
    584f3d16c0cf2e17d787e79e5575c82f88dfb3794618a63ae7b880ab965e66a2
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed and retained declared key/formula agreement. Both
    canonical SMILES comparisons are false; the chirality-aware map is empty and complete_atom_count_match/full_graph_identity_established
    remain false.
  scope_note: Both saved forms are neutral C29H39ClN2O5 with 37 atoms and 41 bonds.
    Five saved ring rows have sizes 5, 5, 6, 16 and 5 and cycle rank five. Two strict
    amides and three carbonyls in SMILES become two C(OH)=N motifs and one carbonyl
    in the InChI form. The chloromethyl and hydroxylated quaternary centre persist;
    no intercongener biosynthetic transformation is inferred. Both encodings retain
    nine specified tetrahedral candidates and one actual STEREOZ plus one STEREOE
    bond. The source enol/tetramate double remains geometrically unspecified; the
    InChI form records it as unknown and adds one unspecified imidic candidate. The
    true source stereo_complete flag applies to atom centres, not all double-bond
    geometries or natural absolute configuration. The original diagnostic stderr is
    empty. No warning is invented or assigned to an owner.
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  evidence_ids:
  - support-2858-data
  - support-2858-execution
  - support-2858-diagaccept
  - support-2858-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  command: just validate-strict data/natural_products/unclassified/oxepinamide-d.yaml
    data/natural_products/unclassified/oxepinamide-f.yaml data/natural_products/unclassified/pactamide-a.yaml
    data/natural_products/unclassified/pactamide-b.yaml data/natural_products/unclassified/pactamide-c.yaml
    data/natural_products/unclassified/pactamide-d.yaml data/natural_products/unclassified/pactamide-e.yaml
    data/natural_products/unclassified/pactamide-f.yaml data/natural_products/unclassified/paenibacterin.yaml
    data/natural_products/unclassified/paraherquamide.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-286/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-59b7206fd7
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-286/validate-all-001.tsv
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
  - naturalproductmech:mibig-59b7206fd7
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
  - naturalproductmech:mibig-59b7206fd7
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
  - naturalproductmech:mibig-59b7206fd7
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-286/review-queue-001.tsv
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
  - naturalproductmech:mibig-59b7206fd7
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2858-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-f.yaml
  locator: 'complete file: identity, chemical_structure, producer/locus/occurrence,
    source_concepts, discussion and history'
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Complete current generated owner; source scopes and open discussions retained.
  snapshot_sha256: 36c2649a8b27959345b32152c709513e2b047b127de3e25090c41b0636b4c3e8
- evidence_id: support-2858-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Original whole owner capture with all source concepts and history.
  snapshot_sha256: deda858259c8e3df482e115d881fc4ab92d28aa7ff577fb2172fe55afb74327f
- evidence_id: support-2858-source
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/support-prep/support-current286-assigned-source-reading-001.json
  locator: /contexts/2; /counts; /global_cautions
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Own disjoint last-five reading: 33 rows, 318 fields, 45 frames, 26 negatives,
    13 histories; four blank AID markers and no actual assay row.'
  snapshot_sha256: eb078dda4d5a188c17e962d58598975dab3644fa357146d795414355aba293ee
- evidence_id: support-2858-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-target-input-plan-001.json
  locator: /records/7; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Accepted 474-placement/55-path plan; 49 actual inputs for this owner.
  snapshot_sha256: 13a0a31f319999f8fa6e1fa57c7c927f238ea2df8c6035d3c04d440d5bf3e979
- evidence_id: support-2858-planaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/root-current286-source-plan-acceptance-001.json
  locator: /accepted; /plan; /status
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: ROOT accepted the original current plan.
  snapshot_sha256: 9cb4d60ee03a72a21248d27eff29749732a31d3f88eb616c44eb0d83f0a72b4a
- evidence_id: support-2858-notes
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /curation
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Disjoint BGC 19 plus Support 33 rows total 52 rows and 547 fields. Native
    taxonomy/curation adds no primary-row credit.
  snapshot_sha256: d8c2be163249152840683342fb18d3cb0e7514aac521fc79f649070b797b05cd
- evidence_id: support-2858-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/intakes-001/2858-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Original canonical intake fixes the current hashes and maintained owner
    roles.
  snapshot_sha256: 47707f6b1418a6901fa84f1ddb0df92d007066a191093591c10c580f46dbca22
- evidence_id: support-2858-intakeaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/root-current286-intake-acceptance-001.json
  locator: /accepted; /status; /intake_summary; /records
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Ten original intakes passed with the actual current input maps.
  snapshot_sha256: b8614bce387a2efc0cdf39025553707d4faf85909e5c68d7de84fb060f0038e5
- evidence_id: support-2858-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles; /records/7/inchi; /records/7/comparisons; /records/7/atom_correspondence;
    /records/7/literal_InChI_layers; /records/7/formula_comparison_scope
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Both saved forms are neutral C29H39ClN2O5 with 37 atoms and 41 bonds. Five
    saved ring rows have sizes 5, 5, 6, 16 and 5 and cycle rank five. Two strict amides
    and three carbonyls in SMILES become two C(OH)=N motifs and one carbonyl in the
    InChI form. The chloromethyl and hydroxylated quaternary centre persist; no intercongener
    biosynthetic transformation is inferred. Both canonical SMILES comparisons are
    false; the chirality-aware map is empty and complete_atom_count_match/full_graph_identity_established
    remain false.
  snapshot_sha256: 5c3cc60a877b9d858bd1076d34f37b57a5f0bc27c896aa121e3a58c370638a0a
- evidence_id: support-2858-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed/atoms; /records/7/smiles/computed/bonds; /records/7/smiles/computed/potential_stereo;
    /records/7/smiles/computed/stereo_counts; /records/7/inchi/computed/atoms; /records/7/inchi/computed/bonds;
    /records/7/inchi/computed/potential_stereo; /records/7/inchi/computed/stereo_counts
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Both encodings retain nine specified tetrahedral candidates and one actual
    STEREOZ plus one STEREOE bond. The source enol/tetramate double remains geometrically
    unspecified; the InChI form records it as unknown and adds one unspecified imidic
    candidate. The true source stereo_complete flag applies to atom centres, not all
    double-bond geometries or natural absolute configuration.
  snapshot_sha256: 5c3cc60a877b9d858bd1076d34f37b57a5f0bc27c896aa121e3a58c370638a0a
- evidence_id: support-2858-motifs
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed/atoms; /records/7/smiles/computed/bonds; /records/7/smiles/computed/rings;
    /records/7/smiles/computed/motifs; /records/7/inchi/computed/atoms; /records/7/inchi/computed/bonds;
    /records/7/inchi/computed/rings; /records/7/inchi/computed/motifs
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: SMILES C9 bears OH12 and chloromethyl C10-Cl11; the InChI form retains
    C28-O36H and C14-Cl29. Amides C20(=O21)-N22 and C34(=O35)-N36 shift to InChI C23(OH33)=N30
    and C27(OH35)=N31. The ketone remains. No ester, acid, free primary amine, saturated
    C5O candidate sugar, phosphorus or metal is present; functional-pattern comparison
    is not a full atom correspondence.
  snapshot_sha256: 5c3cc60a877b9d858bd1076d34f37b57a5f0bc27c896aa121e3a58c370638a0a
- evidence_id: support-2858-molecularreading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/support-prep/support-current286-last-five-molecular-intake-reading-001.json
  locator: /records/2; /counts; /interpretations/2858; /warnings
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'All ten saved forms personally read: 514 atoms, 548 bonds, 46 ring rows
    and 127 potential-stereo entries; no reparse.'
  snapshot_sha256: 3040216f3c1ad6503f50dece059f2fbe456c799dee77dc51526c302d4cfd635a
- evidence_id: support-2858-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /retries; /stderr
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: One original diagnostic exited zero, with no retry.
  snapshot_sha256: b7a36417331f165b8e9bf404bf5704cce0af5adf89a0aec75bc5d2018627680e
- evidence_id: support-2858-diagaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/root-current286-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /scope
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: ROOT accepted the original technical outputs without a scientific identity
    claim.
  snapshot_sha256: 11c878f68a85192b33f7cfbb37505ae1e304a5c03ecf3d5284e3b60aa7834b85
- evidence_id: support-2858-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-original-001.stderr
  locator: complete original empty stderr stream
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: The original diagnostic stderr is empty. No warning is invented or assigned
    to an owner.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: support-2858-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/native-prep/native-current286-cached-taxonomy-reading-001.json
  locator: /context_interpretations/7; /physical_negative_query_scopes/7; /whole_stanzas
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Attributed Native cached-name reading: NCBITaxon:68249 = Streptomyces
    pactum. These complete retained stanzas contain names and synonyms, not fresh
    rank/lineage, strain equivalence or experimental production. Exact merge and nonorganism
    predicates are negative.'
  snapshot_sha256: 75dda850603caeab4a4fd4e53fe37307d25b41d552eebe645019fffc3d25c098
- evidence_id: support-2858-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/native-prep/native-current286-implemented-curation-scan-001.json
  locator: /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows;
    /interpretation
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Nine substantive curation tables have no exact applicable decision for
    these current owners. Generic lexical matches do not apply a correction.
  snapshot_sha256: 3d2309e330b55bfef215e5a0350a7f06ae8df548cf6c7bdd22ce675cb770b4e0
  search_scope: Attributed ignored-inclusive nine-table/3422-row current scan using
    exact owner/source/BGC/key/occurrence/assay predicates; no replay or universal
    absence.
- evidence_id: support-2858-producerpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: complete retained source-method grading table
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Source assertion and CLUSTER_UNSTATED remain separate from causal producer
    or demonstrated locus evidence.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2858-stereopolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142-173 structure_fields, specifically 165-172 atom-centre predicate
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: FindMolChiralCenters unknown atom tags determine stereo_complete; full
    E/Z and natural identity are not certified.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2858-filingpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295-306 choose_pathway
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: One supported model pathway files a record; multiple, absent or unsupported
    results retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2858-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/root-current286-five-gates-acceptance-001.json
  locator: /accepted; /five_local_commands_passed; /denominators; /unavailable_required_gates;
    /all_native_gates_passed
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Five local gates pass; full QC and complete OAK remain unavailable. Queue
    leads are not scientific findings.
  snapshot_sha256: be979d3983ecafe3575f15b24dd3837a9f87d8144daea3d73777c7911faab017
- evidence_id: support-2858-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json
  locator: /records/7/owner_document/curation_history; /records/7/owner_document/source_concepts
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: PMID:28451290 is COMPOUND_EVIDENCE. LOTUS DOI:10.1039/C6SC03875A and the
    three seed events do not add independently verified experiments.
  snapshot_sha256: deda858259c8e3df482e115d881fc4ab92d28aa7ff577fb2172fe55afb74327f
- evidence_id: support-2858-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-target-input-plan-001.json
  locator: /records/7/complete_root_keys; /records/7/declared_mechanism_roots_literal;
    /records/7/component_paths
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: The complete owner lacks causal_graphs, causal_graph_refs, biosynthetic_pathway,
    molecular_targets, bioactivities, bioactivity_summary, related_records and components.
    No maintained reader applies to this owner. This scoped absence does not assert
    absent biology; the two Oxepinamide reader routes elsewhere in batch 286 confer
    no authority on this record.
  snapshot_sha256: 13a0a31f319999f8fa6e1fa57c7c927f238ea2df8c6035d3c04d440d5bf3e979
- evidence_id: support-2858-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Whole saved mibig_compounds frame: 1 positive placements.'
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "BRNQMLSKMSMSQY-QLIRVBKLSA-N". No replay or wider absence claim.
- evidence_id: support-2858-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical line 2048, raw UTF-8 row SHA-256 271cadb14b0efa5ad1ab537b966c190b2f97700a4a9cc750513bf316acc7fe5d
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: BGC0001726 version 4 compound index 6 grounds pactamide F, full key BRNQMLSKMSMSQY-QLIRVBKLSA-N,
    PubChem CID 146684580 and NPAtlas NPA028480. Its chlorine-containing formula and
    distinct complete key remain separate from the other selected Pactamides. Streptomyces
    pactum NCBITaxon:68249 remains the source-asserted producer, distinct in evidentiary
    role from the LOTUS occurrence. BGC0001726 version 4 is active with questionable
    quality and unknown completeness. The KU569222.1 NRPS|PKS/Type I|Unknown locus
    retains blank methods and coordinates and CLUSTER_UNSTATED; no experimental or
    complete-route upgrade is supported.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2858-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Whole saved chebi_structures frame: 0 positive placements.'
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "BRNQMLSKMSMSQY-QLIRVBKLSA-N". No replay or wider absence claim.
- evidence_id: support-2858-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Whole saved lotus_occurrences frame: 1 positive placements.'
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "BRNQMLSKMSMSQY-QLIRVBKLSA-N". No replay or wider absence claim.
- evidence_id: support-2858-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical line 577, raw UTF-8 row SHA-256 57c2e20c299518738cd645754bb44f60c0bffab33ffeae53a8adfe120e1a617d
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: LOTUS row 577 retains Streptomyces pactum 68249 and organism Q26291629
    with DOI:10.1039/C6SC03875A. Publication independence and causal production remain
    unestablished.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2858-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Whole saved cyanometdb_occurrences frame: 0 positive placements.'
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "BRNQMLSKMSMSQY-QLIRVBKLSA-N". No replay or wider absence claim.
- evidence_id: support-2858-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Whole saved npclassifier frame: 1 positive placements.'
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "BRNQMLSKMSMSQY-QLIRVBKLSA-N". No replay or wider absence claim.
- evidence_id: support-2858-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical line 216, raw UTF-8 row SHA-256 d3fd5c38b9149f89615074d8218f95a789fdca64637ef1c5cdb5ce8c14157fc5
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: MIBiG supplies Ornithine-derived, Tetramate alkaloid, Cyclic polyketide
    and Macrocyclic polyketide. NPClassifier gives Amino acids and Peptides plus Polyketides,
    Macrolides, Macrocyclic tetramic acids and is_glycoside:false. These retained
    predictions and source classes describe different evidence scopes; multiple model
    pathways retain UNCLASSIFIED.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2858-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Whole saved pubchem_bioassay frame: 1 positive placements.'
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "BRNQMLSKMSMSQY-QLIRVBKLSA-N". No replay or wider absence claim.
- evidence_id: support-2858-table-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical line 862, raw UTF-8 row SHA-256 278e9942e85dbc42e027352cbb5c758aaa33c58dd7d77ddebab018c43edd6c4e
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: PubChem row 862 has CID 146684580 and a blank AID/no-assay marker. Empty
    endpoints and other negative frames provide no activity, inactivity or target
    measurement.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2858-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Whole saved bindingdb_targets frame: 0 positive placements.'
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "BRNQMLSKMSMSQY-QLIRVBKLSA-N". No replay or wider absence claim.
- evidence_id: support-2858-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Whole saved antibioticmech_inchikeys frame: 0 positive placements.'
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "BRNQMLSKMSMSQY-QLIRVBKLSA-N". No replay or wider absence claim.
- evidence_id: support-2858-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: 'Whole saved chebi_origins frame: 0 positive placements.'
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: Saved predicate exact chebi_id from exact full-key structure rows;
    query []. No replay or wider absence claim.
- evidence_id: support-2858-companion-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-a.yaml
  locator: complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters;
    whole raw reading attributed in current source scope
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Direct selected Pactamide shared-BGC context with distinct full key; no
    identity, stereo, assay, producer grade or pathway transfer. Primary source reading
    is assigned once per owner.
  snapshot_sha256: a8418e6c5c3f77863f237b6eb29235b859474f8740b4cf4bde541d258d6edaee
- evidence_id: support-2858-companion-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-b.yaml
  locator: complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters;
    whole raw reading attributed in current source scope
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Direct selected Pactamide shared-BGC context with distinct full key; no
    identity, stereo, assay, producer grade or pathway transfer. Primary source reading
    is assigned once per owner.
  snapshot_sha256: 063e98ee16c19bc8a78df5ebac39150bfb9a51394a691a579e17c95e1ee5f443
- evidence_id: support-2858-companion-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-c.yaml
  locator: complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters;
    whole raw reading attributed in current source scope
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Direct selected Pactamide shared-BGC context with distinct full key; no
    identity, stereo, assay, producer grade or pathway transfer. Primary source reading
    is assigned once per owner.
  snapshot_sha256: f16e70c83d939186646e73c741504996a32822774d3ec77639c0785824b39091
- evidence_id: support-2858-companion-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-d.yaml
  locator: complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters;
    whole raw reading attributed in current source scope
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Direct selected Pactamide shared-BGC context with distinct full key; no
    identity, stereo, assay, producer grade or pathway transfer. Primary source reading
    is assigned once per owner.
  snapshot_sha256: 6631bd4a1e85637fa7b3719a5bcc831f92781909ec93adbb1705c665c20de24b
- evidence_id: support-2858-companion-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/pactamide-e.yaml
  locator: complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters;
    whole raw reading attributed in current source scope
  accessed_at: '2026-11-07T08:02:30.922345Z'
  support: supports
  summary: Direct selected Pactamide shared-BGC context with distinct full key; no
    identity, stereo, assay, producer grade or pathway transfer. Primary source reading
    is assigned once per owner.
  snapshot_sha256: 5be823189b24d168545dd55165c20d2f76b89542bf79450d07825acd66bccb29
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-286/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json
  accessed_at: '2026-11-07T07:42:42.597912Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: f17e0cf2f7ffae5324b426cf095d627a5d9b16d8a6900938a2d86d33f01a8383
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-286/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json
  accessed_at: '2026-11-07T07:43:08.970157Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 809ff62f379495190e829e91f1ef111d41207c3b04672317dbaab7695f20763d
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-286/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json
  accessed_at: '2026-11-07T07:43:29.315088Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-286/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json
  accessed_at: '2026-11-07T07:44:05.084768Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-286/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json
  accessed_at: '2026-11-07T07:44:17.484589Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 3c72058344dc65e7aacd353aa6cbe966526faf56687259146ea8a0bdb7b36f86
assessments:
- assessment_id: support-2858-identity-assessment
  area: identity
  topic: Exact retained compound grounding
  summary: BGC0001726 version 4 compound index 6 grounds pactamide F, full key BRNQMLSKMSMSQY-QLIRVBKLSA-N,
    PubChem CID 146684580 and NPAtlas NPA028480. Its chlorine-containing formula and
    distinct complete key remain separate from the other selected Pactamides.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  evidence_ids:
  - support-2858-owner
  - support-2858-capture
  - support-2858-source
  - support-2858-intake
  - support-2858-curation
  - support-2858-plan
  - support-2858-table-mibig_compounds
  - support-2858-table-lotus_occurrences
  - support-2858-table-npclassifier
  - support-2858-table-pubchem_bioassay
  - support-2858-companion-0
  - support-2858-companion-1
  - support-2858-companion-2
  - support-2858-companion-3
  - support-2858-companion-4
  dimensions:
  - name: standard_inchi_key
    definition: Complete source key, not label-only identity.
    value: BRNQMLSKMSMSQY-QLIRVBKLSA-N
    evidence_ids:
    - support-2858-owner
    - support-2858-capture
    - support-2858-source
    - support-2858-intake
    - support-2858-curation
    - support-2858-plan
    - support-2858-table-mibig_compounds
    - support-2858-table-lotus_occurrences
    - support-2858-table-npclassifier
    - support-2858-table-pubchem_bioassay
    - support-2858-companion-0
    - support-2858-companion-1
    - support-2858-companion-2
    - support-2858-companion-3
    - support-2858-companion-4
  - name: grounding_scope
    definition: Retained source identity versus independent natural identity.
    value: BGC0001726 version 4 compound index 6 grounds pactamide F, full key BRNQMLSKMSMSQY-QLIRVBKLSA-N,
      PubChem CID 146684580 and NPAtlas NPA028480. Its chlorine-containing formula
      and distinct complete key remain separate from the other selected Pactamides.
    evidence_ids:
    - support-2858-owner
    - support-2858-capture
    - support-2858-source
    - support-2858-intake
    - support-2858-curation
    - support-2858-plan
    - support-2858-table-mibig_compounds
    - support-2858-table-lotus_occurrences
    - support-2858-table-npclassifier
    - support-2858-table-pubchem_bioassay
    - support-2858-companion-0
    - support-2858-companion-1
    - support-2858-companion-2
    - support-2858-companion-3
    - support-2858-companion-4
- assessment_id: support-2858-representation-assessment
  area: representation
  topic: Saved forms and stereochemical scope
  summary: Both saved forms are neutral C29H39ClN2O5 with 37 atoms and 41 bonds. Five
    saved ring rows have sizes 5, 5, 6, 16 and 5 and cycle rank five. Two strict amides
    and three carbonyls in SMILES become two C(OH)=N motifs and one carbonyl in the
    InChI form. The chloromethyl and hydroxylated quaternary centre persist; no intercongener
    biosynthetic transformation is inferred. SMILES C9 bears OH12 and chloromethyl
    C10-Cl11; the InChI form retains C28-O36H and C14-Cl29. Amides C20(=O21)-N22 and
    C34(=O35)-N36 shift to InChI C23(OH33)=N30 and C27(OH35)=N31. The ketone remains.
    No ester, acid, free primary amine, saturated C5O candidate sugar, phosphorus
    or metal is present; functional-pattern comparison is not a full atom correspondence.
    Both canonical SMILES comparisons are false; the chirality-aware map is empty
    and complete_atom_count_match/full_graph_identity_established remain false. Normalized
    identifiers, formula agreement and local parsing do not establish independent
    full graph identity, natural-sample identity, experimental absolute stereochemistry
    or primary biological validation.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  evidence_ids:
  - support-2858-data
  - support-2858-stereo
  - support-2858-motifs
  - support-2858-molecularreading
  - support-2858-execution
  - support-2858-diagaccept
  - support-2858-stereopolicy
  dimensions:
  - name: stereochemistry_scope
    definition: Saved atom/bond assignments and representation-dependent candidates.
    value: Both encodings retain nine specified tetrahedral candidates and one actual
      STEREOZ plus one STEREOE bond. The source enol/tetramate double remains geometrically
      unspecified; the InChI form records it as unknown and adds one unspecified imidic
      candidate. The true source stereo_complete flag applies to atom centres, not
      all double-bond geometries or natural absolute configuration.
    evidence_ids:
    - support-2858-data
    - support-2858-stereo
    - support-2858-motifs
    - support-2858-molecularreading
    - support-2858-execution
    - support-2858-diagaccept
    - support-2858-stereopolicy
  - name: representation_correspondence
    definition: Limited matching is distinct from full identity.
    value: Both canonical SMILES comparisons are false; the chirality-aware map is
      empty and complete_atom_count_match/full_graph_identity_established remain false.
      Normalized identifiers, formula agreement and local parsing do not establish
      independent full graph identity, natural-sample identity, experimental absolute
      stereochemistry or primary biological validation.
    evidence_ids:
    - support-2858-data
    - support-2858-stereo
    - support-2858-motifs
    - support-2858-molecularreading
    - support-2858-execution
    - support-2858-diagaccept
    - support-2858-stereopolicy
- assessment_id: support-2858-provenance-assessment
  area: provenance
  topic: Producer, locus and taxon claim grain
  summary: Streptomyces pactum NCBITaxon:68249 remains the source-asserted producer,
    distinct in evidentiary role from the LOTUS occurrence. BGC0001726 version 4 is
    active with questionable quality and unknown completeness. The KU569222.1 NRPS|PKS/Type
    I|Unknown locus retains blank methods and coordinates and CLUSTER_UNSTATED; no
    experimental or complete-route upgrade is supported.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  evidence_ids:
  - support-2858-source
  - support-2858-capture
  - support-2858-taxonomy
  - support-2858-curation
  - support-2858-producerpolicy
  - support-2858-table-mibig_compounds
  - support-2858-table-lotus_occurrences
  - support-2858-table-npclassifier
  - support-2858-table-pubchem_bioassay
  dimensions:
  - name: taxon_scope
    definition: Cached names do not establish live taxonomy or strain equivalence.
    value: 'Attributed Native cached-name reading: NCBITaxon:68249 = Streptomyces
      pactum. These complete retained stanzas contain names and synonyms, not fresh
      rank/lineage, strain equivalence or experimental production. Exact merge and
      nonorganism predicates are negative.'
    evidence_ids:
    - support-2858-source
    - support-2858-capture
    - support-2858-taxonomy
    - support-2858-curation
    - support-2858-producerpolicy
    - support-2858-table-mibig_compounds
    - support-2858-table-lotus_occurrences
    - support-2858-table-npclassifier
    - support-2858-table-pubchem_bioassay
  - name: producer_evidence
    definition: Producer grade remains separate from locus and occurrence evidence.
    value: Streptomyces pactum NCBITaxon:68249 remains the source-asserted producer,
      distinct in evidentiary role from the LOTUS occurrence.
    evidence_ids:
    - support-2858-source
    - support-2858-capture
    - support-2858-taxonomy
    - support-2858-curation
    - support-2858-producerpolicy
    - support-2858-table-mibig_compounds
    - support-2858-table-lotus_occurrences
    - support-2858-table-npclassifier
    - support-2858-table-pubchem_bioassay
  - name: locus_evidence
    definition: Entry quality, completeness and methods delimit evidence.
    value: BGC0001726 version 4 is active with questionable quality and unknown completeness.
      The KU569222.1 NRPS|PKS/Type I|Unknown locus retains blank methods and coordinates
      and CLUSTER_UNSTATED; no experimental or complete-route upgrade is supported.
    evidence_ids:
    - support-2858-source
    - support-2858-capture
    - support-2858-taxonomy
    - support-2858-curation
    - support-2858-producerpolicy
    - support-2858-table-mibig_compounds
    - support-2858-table-lotus_occurrences
    - support-2858-table-npclassifier
    - support-2858-table-pubchem_bioassay
- assessment_id: support-2858-citations-assessment
  area: evidence
  topic: Citation grain and retained history
  summary: PMID:28451290 is COMPOUND_EVIDENCE. LOTUS DOI:10.1039/C6SC03875A and the
    three seed events do not add independently verified experiments.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  evidence_ids:
  - support-2858-owner
  - support-2858-source
  - support-2858-capture
  - support-2858-history
  - support-2858-table-mibig_compounds
  - support-2858-table-lotus_occurrences
  - support-2858-table-npclassifier
  - support-2858-table-pubchem_bioassay
  dimensions:
  - name: citation_scope
    definition: Pointers and seed events are not independent experimental proof.
    value: PMID:28451290 is COMPOUND_EVIDENCE. LOTUS DOI:10.1039/C6SC03875A and the
      three seed events do not add independently verified experiments.
    evidence_ids:
    - support-2858-owner
    - support-2858-source
    - support-2858-capture
    - support-2858-history
    - support-2858-table-mibig_compounds
    - support-2858-table-lotus_occurrences
    - support-2858-table-npclassifier
    - support-2858-table-pubchem_bioassay
- assessment_id: support-2858-occurrence-assay-assessment
  area: evidence
  topic: Occurrence and assay boundaries
  summary: LOTUS row 577 retains Streptomyces pactum 68249 and organism Q26291629
    with DOI:10.1039/C6SC03875A. Publication independence and causal production remain
    unestablished. PubChem row 862 has CID 146684580 and a blank AID/no-assay marker.
    Empty endpoints and other negative frames provide no activity, inactivity or target
    measurement.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  evidence_ids:
  - support-2858-source
  - support-2858-taxonomy
  - support-2858-curation
  - support-2858-plan
  - support-2858-query-mibig_compounds
  - support-2858-query-chebi_structures
  - support-2858-query-lotus_occurrences
  - support-2858-query-cyanometdb_occurrences
  - support-2858-query-npclassifier
  - support-2858-query-pubchem_bioassay
  - support-2858-query-bindingdb_targets
  - support-2858-query-antibioticmech_inchikeys
  - support-2858-query-chebi_origins
  - support-2858-table-mibig_compounds
  - support-2858-table-lotus_occurrences
  - support-2858-table-npclassifier
  - support-2858-table-pubchem_bioassay
  dimensions:
  - name: occurrence_scope
    definition: Occurrence is distinct from causal production.
    value: LOTUS row 577 retains Streptomyces pactum 68249 and organism Q26291629
      with DOI:10.1039/C6SC03875A. Publication independence and causal production
      remain unestablished.
    evidence_ids:
    - support-2858-source
    - support-2858-taxonomy
    - support-2858-curation
    - support-2858-plan
    - support-2858-query-mibig_compounds
    - support-2858-query-chebi_structures
    - support-2858-query-lotus_occurrences
    - support-2858-query-cyanometdb_occurrences
    - support-2858-query-npclassifier
    - support-2858-query-pubchem_bioassay
    - support-2858-query-bindingdb_targets
    - support-2858-query-antibioticmech_inchikeys
    - support-2858-query-chebi_origins
    - support-2858-table-mibig_compounds
    - support-2858-table-lotus_occurrences
    - support-2858-table-npclassifier
    - support-2858-table-pubchem_bioassay
  - name: assay_target_scope
    definition: Blank markers and bounded negatives are not measurements.
    value: PubChem row 862 has CID 146684580 and a blank AID/no-assay marker. Empty
      endpoints and other negative frames provide no activity, inactivity or target
      measurement.
    evidence_ids:
    - support-2858-source
    - support-2858-taxonomy
    - support-2858-curation
    - support-2858-plan
    - support-2858-query-mibig_compounds
    - support-2858-query-chebi_structures
    - support-2858-query-lotus_occurrences
    - support-2858-query-cyanometdb_occurrences
    - support-2858-query-npclassifier
    - support-2858-query-pubchem_bioassay
    - support-2858-query-bindingdb_targets
    - support-2858-query-antibioticmech_inchikeys
    - support-2858-query-chebi_origins
    - support-2858-table-mibig_compounds
    - support-2858-table-lotus_occurrences
    - support-2858-table-npclassifier
    - support-2858-table-pubchem_bioassay
- assessment_id: support-2858-classification-assessment
  area: consistency
  topic: Source classes, model labels and filing
  summary: MIBiG supplies Ornithine-derived, Tetramate alkaloid, Cyclic polyketide
    and Macrocyclic polyketide. NPClassifier gives Amino acids and Peptides plus Polyketides,
    Macrolides, Macrocyclic tetramic acids and is_glycoside:false. These retained
    predictions and source classes describe different evidence scopes; multiple model
    pathways retain UNCLASSIFIED.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  evidence_ids:
  - support-2858-source
  - support-2858-owner
  - support-2858-motifs
  - support-2858-filingpolicy
  - support-2858-gates
  - support-2858-table-mibig_compounds
  - support-2858-table-lotus_occurrences
  - support-2858-table-npclassifier
  - support-2858-table-pubchem_bioassay
  dimensions:
  - name: classification_applicability
    definition: Source/model/topology and biochemical proof remain distinct.
    value: MIBiG supplies Ornithine-derived, Tetramate alkaloid, Cyclic polyketide
      and Macrocyclic polyketide. NPClassifier gives Amino acids and Peptides plus
      Polyketides, Macrolides, Macrocyclic tetramic acids and is_glycoside:false.
      These retained predictions and source classes describe different evidence scopes;
      multiple model pathways retain UNCLASSIFIED.
    evidence_ids:
    - support-2858-source
    - support-2858-owner
    - support-2858-motifs
    - support-2858-filingpolicy
    - support-2858-gates
    - support-2858-table-mibig_compounds
    - support-2858-table-lotus_occurrences
    - support-2858-table-npclassifier
    - support-2858-table-pubchem_bioassay
- assessment_id: support-2858-completion-assessment
  area: completeness
  topic: Earned work and unavailable authority
  summary: The complete owner, assigned source payloads, current canonical intake
    and both saved forms were read. The complete owner lacks causal_graphs, causal_graph_refs,
    biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary, related_records
    and components. No maintained reader applies to this owner. This scoped absence
    does not assert absent biology; the two Oxepinamide reader routes elsewhere in
    batch 286 confer no authority on this record. No additional material local defect
    was established in this earned scope. Five local gates pass; full QC, complete
    OAK and fresh primary/external verification are unavailable. Completion is partial
    and native SEEDED status is unchanged.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-59b7206fd7
  evidence_ids:
  - support-2858-intake
  - support-2858-intakeaccept
  - support-2858-plan
  - support-2858-planaccept
  - support-2858-notes
  - support-2858-gates
  - support-2858-data
  - support-2858-diagaccept
  - support-2858-scope
  dimensions:
  - name: review_completion
    definition: Earned local work does not replace unavailable authority or promote
      native status.
    value: The complete owner, assigned source payloads, current canonical intake
      and both saved forms were read. The complete owner lacks causal_graphs, causal_graph_refs,
      biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary,
      related_records and components. No maintained reader applies to this owner.
      This scoped absence does not assert absent biology; the two Oxepinamide reader
      routes elsewhere in batch 286 confer no authority on this record. No additional
      material local defect was established in this earned scope. Five local gates
      pass; full QC, complete OAK and fresh primary/external verification are unavailable.
      Completion is partial and native SEEDED status is unchanged.
    evidence_ids:
    - support-2858-intake
    - support-2858-intakeaccept
    - support-2858-plan
    - support-2858-planaccept
    - support-2858-notes
    - support-2858-gates
    - support-2858-data
    - support-2858-diagaccept
    - support-2858-scope
findings: []
actions: []
limitations:
- Normalized identifiers, formula agreement and local parsing do not establish independent
  full graph identity, natural-sample identity, experimental absolute stereochemistry
  or primary biological validation.
- Both canonical SMILES comparisons are false; the chirality-aware map is empty and
  complete_atom_count_match/full_graph_identity_established remain false. Both encodings
  retain nine specified tetrahedral candidates and one actual STEREOZ plus one STEREOE
  bond. The source enol/tetramate double remains geometrically unspecified; the InChI
  form records it as unknown and adds one unspecified imidic candidate. The true source
  stereo_complete flag applies to atom centres, not all double-bond geometries or
  natural absolute configuration.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK
  remain unavailable. Source assertions retain their original grades and unresolved
  questions.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh batch 286 evidence and judgments; batch 285 supplies schema interface only.
- No record, native status or history was edited and no source query, molecular parse,
  target invocation or external request occurred in this lane.
- ROOT appends five actual local gate checks and three required unavailable checks.
  No maintained-reader check applies to these five owners.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-286
```
