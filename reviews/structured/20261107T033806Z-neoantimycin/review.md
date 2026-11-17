# Local evidence review: neoantimycin

- Review: 20261107T033806Z-neoantimycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T02:55:59.698315Z
- Finished UTC: 2026-11-07T03:38:06.855047Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Neoantimycin retains seven specified atom centres, a separate source producer and a differently attributed occurrence. Both stored forms normalize to the declared key despite two amide/imidic representation changes. Local review is partial; the retained evidence does not support an identity merger or a corrective finding.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2817; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-3f35f559e8 | data/natural_products/unclassified/neoantimycin.yaml | generated | neoantimycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-3f35f559e8 | Both stored forms parsed and retain declared normalized keys; Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. |
| strict_ten | passed | True | naturalproductmech:mibig-3f35f559e8 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-3f35f559e8 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-3f35f559e8 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-3f35f559e8 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-3f35f559e8 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-3f35f559e8 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-3f35f559e8 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-3f35f559e8 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained compound grounding

identity: supported. Targets: naturalproductmech:mibig-3f35f559e8.

The complete key JIJATTFJYJZEBT-MDDNAQDNSA-N and BGC0001695:1 distinguish this source form under the literal neoantimycin label. A same-label record does not establish equivalent stereochemistry or production. The current owner has no direct-companion or explicit comparison inputs, so no additional counterpart chemical assessment is claimed.

### Saved molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-3f35f559e8.

Both stored forms parse to one neutral C36H46N2O12 fragment with 50 atoms and 52 bonds and the same declared normalized InChI/key. Both canonical SMILES comparisons are false and the limited correspondence is empty. Two SMILES amides become two C(OH)=N sites in the InChI-derived form while four ester carbonyls persist. The specific saved change is compatible with representation normalization; full graph and natural identity are not established by key agreement. The 15-membered macrocycle, two aromatic six-membered rings and four C(=O)-O-C links are retained in both tables. SMILES amides 26/25 and 33/32 become InChI-derived C(OH)=N sites 30/37/41 and 17/36/38. The hydroxy/gem-dimethyl, benzyl, isopropyl and sec-butyl substituent topology remains explicit. No candidate saturated C5O sugar ring is reported. Only the two stored owner strings were parsed; no source alternate or congener was reparsed. Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. Normalized key/formula agreement and a successful local process do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry, primary mechanism validation or a native status promotion.

### Compound-specific producer, locus and taxon

provenance: supported. Targets: naturalproductmech:mibig-3f35f559e8.

BGC0001695 version 5, compound index 1, attributes Streptomyces conglobatus (NCBITaxon:1653203) as SOURCE_ASSERTION producer. The entry remains active with questionable quality and unknown completeness. It is not interchangeable with the separately cited Streptomyces orinoci occurrence. MH128122.1 has blank coordinate bounds and no stated locus method, retaining CLUSTER_UNSTATED. Source NRPS/Type I and npatlas:NPA010703 are literal assertions; PMID:29979567 is entry-level evidence, not fresh pathway validation.

### Citation grain and retained history

evidence: supported. Targets: naturalproductmech:mibig-3f35f559e8.

MIBiG PMID:29979567 and LOTUS DOI:10.1016/S0040-4020(01)82768-X have different assertion scopes. The two seeding histories retain their provenance without adding independent experimental confirmation. Primary papers, spectra and sequence evidence were not newly checked.

### Occurrence and assay limits

evidence: supported. Targets: naturalproductmech:mibig-3f35f559e8.

LOTUS physical line 3028 retains Streptomyces orinoci (NCBITaxon:67339), structure Q77498040 and DOI:10.1016/S0040-4020(01)82768-X. This occurrence differs from the source producer taxon and remains a separate cited assertion. Cached taxonomy does not establish strain equivalence or publication independence. No actual PubChem assay, BindingDB target or AntibioticMech exact-key row occurs in this saved context. The bounded negative frames are not evidence of inactivity and do not transfer activity from another neoantimycin form.

### Source classes, model labels and filing

consistency: supported. Targets: naturalproductmech:mibig-3f35f559e8.

NPClassifier retains Amino acids and Peptides&#124;Polyketides, Macrolides, Antimycins and is_glycoside false at the retained 2026-09-07 model version. Multiple pathways explain UNCLASSIFIED filing; source NRPS and topology remain distinct evidence from model predictions.

### Earned work and unavailable authority

completeness: supported. Targets: naturalproductmech:mibig-3f35f559e8.

Complete assigned raw/source/intake and both saved molecular forms were read. The complete captured owner has no graph, graph reference, pathway, target, activity or component root and requires no maintained reader. Source locus and classification assertions do not supply missing mechanistic steps. Five local native commands pass; full QC, complete OAK and fresh primary verification remain unavailable. Completion is partial, native SEEDED status unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2817-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/neoantimycin.yaml; complete file: identifier, label, chemical_structure, source_concepts, producer_organisms, biosynthetic_gene_clusters, classification, curation_history and present mechanism/activity roots | supports | Complete current owner retained; generated source facts and curator-owned annotations remain distinct. |
| support-2817-capture | /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json; /records/6/owner_document; /records/6/component_captures | supports | Whole accepted owner capture; no protein, companion or component identity transfer. |
| support-2817-source | /private/tmp/npm-review-work/shared-next-batch282-tentative/support-prep/support-current282-assigned-source-reading-001.json; /contexts/7; /selected_counts; /counts; /global_cautions | supports | Complete assigned saved source context. Own selected credit is 20 rows/235 fields/45 frames/28 negatives; six Argimycin companion contexts are separate. ROOT reread two assay rows with zero additional primary credit. |
| support-2817-plan | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-target-input-plan-001.json; /records/6; /source_placement_count; /unique_source_path_count | supports | Actual 460-placement/65-path plan; this owner has 44 captured inputs. |
| support-2817-planaccept | /private/tmp/npm-review-work/shared-next-batch282/root-current282-input-plan-acceptance-001.json; /status; /accepted; /input_plan | supports | ROOT accepted the original current source plan. |
| support-2817-notes | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /curation | supports | Current notes retain BGC 26 plus Support 37 positive placements; Native and overlapping ROOT readings add zero primary rows. Attribution and exact source grain are preserved. |
| support-2817-intake | /private/tmp/npm-review-work/shared-next-batch282/intakes-001/2817-inspect-001.json; /status; /source; /targets | supports | Actual intake fixes generated target, maintained owners and current relative input hashes. |
| support-2817-intakeaccept | /private/tmp/npm-review-work/shared-next-batch282/root-current282-intake-acceptance-001.json; /status; /accepted; /intake_summary | supports | ROOT accepted all ten original intakes, all exit zero with empty stderr. |
| support-2817-data | /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles; /records/6/inchi; /records/6/comparisons; /records/6/atom_correspondence; /records/6/literal_InChI_layers; /records/6/formula_comparison_scope | supports | Both stored forms parse to one neutral C36H46N2O12 fragment with 50 atoms and 52 bonds and the same declared normalized InChI/key. Both canonical SMILES comparisons are false and the limited correspondence is empty. Two SMILES amides become two C(OH)=N sites in the InChI-derived form while four ester carbonyls persist. The specific saved change is compatible with representation normalization; full graph and natural identity are not established by key agreement. Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. |
| support-2817-stereo | /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed/atoms; /records/6/smiles/computed/potential_stereo; /records/6/smiles/computed/bonds; /records/6/inchi/computed/atoms; /records/6/inchi/computed/potential_stereo; /records/6/inchi/computed/bonds | supports | Seven tetrahedral centres are specified in each form. Saved SMILES atom CIP values are S at indices 0, 20, 24, 38 and 46 and R at 7 and 9; corresponding InChI-derived centres retain the same configured scaffold. Two unspecified double-bond candidates appear only in the imidic InChI-derived representation. The true source stereo_complete flag measures atom-centre completeness and does not assign every possible representation-dependent double geometry or establish natural-sample configuration. |
| support-2817-motifs | /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed/motifs; /records/6/smiles/computed/rings; /records/6/smiles/computed/bonds; /records/6/smiles/computed/atoms; /records/6/inchi/computed/motifs; /records/6/inchi/computed/rings; /records/6/inchi/computed/bonds; /records/6/inchi/computed/atoms | supports | The 15-membered macrocycle, two aromatic six-membered rings and four C(=O)-O-C links are retained in both tables. SMILES amides 26/25 and 33/32 become InChI-derived C(OH)=N sites 30/37/41 and 17/36/38. The hydroxy/gem-dimethyl, benzyl, isopropyl and sec-butyl substituent topology remains explicit. No candidate saturated C5O sugar ring is reported. Only the two stored owner strings were parsed; no source alternate or congener was reparsed. |
| support-2817-molecularreading | /private/tmp/npm-review-work/shared-next-batch282-tentative/support-prep/support-current282-last-five-molecular-intake-reading-001.json; /records/1; /counts; /warnings | supports | Complete ten saved forms personally read, 492 atoms/510 bonds/28 ring rows/120 potential-stereo rows; no molecular replay. Six original undefined-stereo warning lines remain globally unassigned; none is assigned to an individual owner. |
| support-2817-execution | /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries | supports | Single original diagnostic command and retained streams; no replay. |
| support-2817-diagaccept | /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/root-current282-diagnostic-acceptance-001.json; /status; /accepted; /diagnostic; /execution | supports | ROOT accepted the original stored-form diagnostic. |
| support-2817-stderr | /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-original-001.stderr; complete six original warning lines | supports | Six original undefined-stereo warning lines remain globally unassigned; none is assigned to an individual owner. |
| support-2817-taxonomy | /private/tmp/npm-review-work/shared-next-batch282-tentative/native-prep/native-current282-cached-taxonomy-reading-001.json; /context_interpretations/16; /physical_negative_query_scopes/16; /whole_stanzas | supports | Keep BGC0001695 producer Streptomyces conglobatus (1653203), MH128122.1 and PMID:29979567 distinct from LOTUS Streptomyces orinoci (67339) at DOI:10.1016/S0040-4020(01)82768-X. SOURCE_ASSERTION/CLUSTER_UNSTATED and unknown source completeness remain bounded; the shared neoantimycin name does not merge producer, occurrence, congener or experiment. All saved source taxon IDs have complete cache stanzas; no forward merge or nonorganism match is retained for this context. Cached labels and synonyms do not establish current remote taxonomy, lineage, production or strain identity. |
| support-2817-curation | /private/tmp/npm-review-work/shared-next-batch282-tentative/native-prep/native-current282-implemented-curation-scan-001.json; /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows; /interpretation | supports | No exact applicable maintained correction; lexical names, related BGC rows and an assay exclusion for another complete chemical identity do not transfer decisions. |
| support-2817-producerpolicy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; complete method grading table | supports | Producer evidence and locus methods answer different questions; missing methods retain their stated grade. |
| support-2817-stereopolicy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142-173, complete structure_fields; specifically lines 167-168 FindMolChiralCenters and unassigned atom-centre predicate | supports | Source stereo_complete covers atom centres, not E/Z completeness or natural identity. |
| support-2817-filingpolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306, choose_pathway | supports | One supported normalized pathway selects filing; multiple, none or unsupported values retain UNCLASSIFIED. |
| support-2817-gates | /private/tmp/npm-review-work/shared-next-batch282/root-current282-five-gates-acceptance-001.json; /records; /all_native_gates_passed; /selected_queue_rows; /unavailable_required_gates | supports | Five local gates pass, with required QC/OAK unavailable. Queue entries remain diagnostic leads, not scientific findings. |
| support-2817-history | /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json; /records/6/owner_document/curation_history; /records/6/owner_document/source_concepts | supports | MIBiG PMID:29979567 and LOTUS DOI:10.1016/S0040-4020(01)82768-X have different assertion scopes. The two seeding histories retain their provenance without adding independent experimental confirmation. Primary papers, spectra and sequence evidence were not newly checked. |
| support-2817-scope | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-target-input-plan-001.json; /records/6/complete_root_keys; /records/6/declared_mechanism_roots_literal; /records/6/component_paths; /records/6/complete_raw_mechanism_sections | supports | The complete captured owner has no graph, graph reference, pathway, target, activity or component root and requires no maintained reader. Source locus and classification assertions do not supply missing mechanistic steps. |
| support-2817-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame with 1 positive placements read. |
| support-2817-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical line 2016, raw UTF-8 row SHA-256 681a95db254b110fff286e10c12b5bacf6622c4d0cf7bf97e52a604b801925ae | supports | The complete key JIJATTFJYJZEBT-MDDNAQDNSA-N and BGC0001695:1 distinguish this source form under the literal neoantimycin label. A same-label record does not establish equivalent stereochemistry or production. The current owner has no direct-companion or explicit comparison inputs, so no additional counterpart chemical assessment is claimed. BGC0001695 version 5, compound index 1, attributes Streptomyces conglobatus (NCBITaxon:1653203) as SOURCE_ASSERTION producer. The entry remains active with questionable quality and unknown completeness. It is not interchangeable with the separately cited Streptomyces orinoci occurrence. MH128122.1 has blank coordinate bounds and no stated locus method, retaining CLUSTER_UNSTATED. Source NRPS/Type I and npatlas:NPA010703 are literal assertions; PMID:29979567 is entry-level evidence, not fresh pathway validation. |
| support-2817-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame with 0 positive placements read. |
| support-2817-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame with 1 positive placements read. |
| support-2817-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical line 3028, raw UTF-8 row SHA-256 96400dfaf42a6abcdff7a28b13f9b9acd5fe6ddfadee610f905c2660ac299c80 | supports | LOTUS physical line 3028 retains Streptomyces orinoci (NCBITaxon:67339), structure Q77498040 and DOI:10.1016/S0040-4020(01)82768-X. This occurrence differs from the source producer taxon and remains a separate cited assertion. Cached taxonomy does not establish strain equivalence or publication independence. |
| support-2817-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame with 0 positive placements read. |
| support-2817-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame with 1 positive placements read. |
| support-2817-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical line 1115, raw UTF-8 row SHA-256 3230b89a70cbde05f5cbb1ff97f33f7554ae881c7297b3a3705f2830f2b4a9eb | supports | NPClassifier retains Amino acids and Peptides&#124;Polyketides, Macrolides, Antimycins and is_glycoside false at the retained 2026-09-07 model version. Multiple pathways explain UNCLASSIFIED filing; source NRPS and topology remain distinct evidence from model predictions. |
| support-2817-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame with 0 positive placements read. |
| support-2817-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame with 0 positive placements read. |
| support-2817-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame with 0 positive placements read. |
| support-2817-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json; /contexts/16/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame with 0 positive placements read. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-282/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-282/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-282/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-282/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-282/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Normalized key/formula agreement and a successful local process do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry, primary mechanism validation or a native status promotion.
- Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. Seven tetrahedral centres are specified in each form. Saved SMILES atom CIP values are S at indices 0, 20, 24, 38 and 46 and R at 7 and 9; corresponding InChI-derived centres retain the same configured scaffold. Two unspecified double-bond candidates appear only in the imidic InChI-derived representation. The true source stereo_complete flag measures atom-centre completeness and does not assign every possible representation-dependent double geometry or establish natural-sample configuration.
- Six original undefined-stereo warning lines remain globally unassigned; none is assigned to an individual owner.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK remain unavailable; source/database claims retain their exact authority.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh current 282 evidence and judgments; prior batches provide interface logic only.
- No source row, record, campaign or native status was changed; no query, molecular parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual native checks and three required unavailable checks. Only selected order 2818 requires a maintained-reader check; unselected companions remain context only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T033806Z-neoantimycin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: neoantimycin'
started_at: '2026-11-07T02:55:59.698315Z'
finished_at: '2026-11-07T03:38:06.855047Z'
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
summary: Neoantimycin retains seven specified atom centres, a separate source producer
  and a differently attributed occurrence. Both stored forms normalize to the declared
  key despite two amide/imidic representation changes. Local review is partial; the
  retained evidence does not support an identity merger or a corrective finding.
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
  - path: data/natural_products/unclassified/neoantimycin.yaml
    sha256: b5606e8636fe6a914d14b8bdbf54ed2a2156be487c6453d5e99199f639565e82
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
  selection: Campaign path order 2817; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-3f35f559e8
targets:
- target_id: naturalproductmech:mibig-3f35f559e8
  path: data/natural_products/unclassified/neoantimycin.yaml
  label: neoantimycin
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnose282-001.py
    ddb26c5b49b323471e1246a18352bf9cf19325f959be014bba541e3c5a780d10 2a94e2ad0338b4b959ef7a27e176ebdb67a903ecd83f041068dac2a3e1f8cd35
    9f93ed9b2ebbecda2375829542ce823524b14b89071b27fd29f512838c8c18fb
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed and retain declared normalized keys; Both canonical
    SMILES comparisons are false; the saved map is empty, complete_atom_count_match
    is false and full_graph_identity_established is false.
  scope_note: Both stored forms parse to one neutral C36H46N2O12 fragment with 50
    atoms and 52 bonds and the same declared normalized InChI/key. Both canonical
    SMILES comparisons are false and the limited correspondence is empty. Two SMILES
    amides become two C(OH)=N sites in the InChI-derived form while four ester carbonyls
    persist. The specific saved change is compatible with representation normalization;
    full graph and natural identity are not established by key agreement. Seven tetrahedral
    centres are specified in each form. Saved SMILES atom CIP values are S at indices
    0, 20, 24, 38 and 46 and R at 7 and 9; corresponding InChI-derived centres retain
    the same configured scaffold. Two unspecified double-bond candidates appear only
    in the imidic InChI-derived representation. The true source stereo_complete flag
    measures atom-centre completeness and does not assign every possible representation-dependent
    double geometry or establish natural-sample configuration. Six original undefined-stereo
    warning lines remain globally unassigned; none is assigned to an individual owner.
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  evidence_ids:
  - support-2817-data
  - support-2817-execution
  - support-2817-diagaccept
  - support-2817-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  command: just validate-strict data/natural_products/unclassified/nannocystin-a.yaml
    data/natural_products/unclassified/napyradiomycin-2.yaml data/natural_products/unclassified/napyradiomycin-3.yaml
    data/natural_products/unclassified/napyradiomycin-4.yaml data/natural_products/unclassified/necroxime-b.yaml
    data/natural_products/unclassified/neoantimycin-2.yaml data/natural_products/unclassified/neoantimycin.yaml
    data/natural_products/unclassified/neocarzinostatin-chromophore.yaml data/natural_products/unclassified/neomediomycin-b.yaml
    data/natural_products/unclassified/nigrifactin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-282/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-3f35f559e8
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-282/validate-all-001.tsv
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
  - naturalproductmech:mibig-3f35f559e8
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
  - naturalproductmech:mibig-3f35f559e8
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
  - naturalproductmech:mibig-3f35f559e8
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-282/review-queue-001.tsv
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
  - naturalproductmech:mibig-3f35f559e8
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2817-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/neoantimycin.yaml
  locator: 'complete file: identifier, label, chemical_structure, source_concepts,
    producer_organisms, biosynthetic_gene_clusters, classification, curation_history
    and present mechanism/activity roots'
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete current owner retained; generated source facts and curator-owned
    annotations remain distinct.
  snapshot_sha256: b5606e8636fe6a914d14b8bdbf54ed2a2156be487c6453d5e99199f639565e82
- evidence_id: support-2817-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json
  locator: /records/6/owner_document; /records/6/component_captures
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Whole accepted owner capture; no protein, companion or component identity
    transfer.
  snapshot_sha256: 2a94e2ad0338b4b959ef7a27e176ebdb67a903ecd83f041068dac2a3e1f8cd35
- evidence_id: support-2817-source
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/support-prep/support-current282-assigned-source-reading-001.json
  locator: /contexts/7; /selected_counts; /counts; /global_cautions
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete assigned saved source context. Own selected credit is 20 rows/235
    fields/45 frames/28 negatives; six Argimycin companion contexts are separate.
    ROOT reread two assay rows with zero additional primary credit.
  snapshot_sha256: 804fbc005d55b5ba152421dbd9b555a8711279b69eb88b069bcbd7465d482c85
- evidence_id: support-2817-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-target-input-plan-001.json
  locator: /records/6; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Actual 460-placement/65-path plan; this owner has 44 captured inputs.
  snapshot_sha256: 92b2c735b1716c07a2fea1c7c34caf4ad63fa45e2b2be7236ccf7ad97beaa06b
- evidence_id: support-2817-planaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/root-current282-input-plan-acceptance-001.json
  locator: /status; /accepted; /input_plan
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: ROOT accepted the original current source plan.
  snapshot_sha256: 8b8a6476268a7af1cc5b9cae8af2eb5909613b261055a9801dad3be298d4a294
- evidence_id: support-2817-notes
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /curation
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Current notes retain BGC 26 plus Support 37 positive placements; Native
    and overlapping ROOT readings add zero primary rows. Attribution and exact source
    grain are preserved.
  snapshot_sha256: 6a37d82b406b849e574c64989542ecd594b7ba449e5b64126cc88856c975164d
- evidence_id: support-2817-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/intakes-001/2817-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Actual intake fixes generated target, maintained owners and current relative
    input hashes.
  snapshot_sha256: 1ff459e1c17450bc09ca3c6261f899b75d9fd787b49d80da43872e2d0eb113ac
- evidence_id: support-2817-intakeaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/root-current282-intake-acceptance-001.json
  locator: /status; /accepted; /intake_summary
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: ROOT accepted all ten original intakes, all exit zero with empty stderr.
  snapshot_sha256: bcc44a28603093d5698cc3314edd9fcd4d00da9d335f3d01c0fd69bb09375907
- evidence_id: support-2817-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles; /records/6/inchi; /records/6/comparisons; /records/6/atom_correspondence;
    /records/6/literal_InChI_layers; /records/6/formula_comparison_scope
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Both stored forms parse to one neutral C36H46N2O12 fragment with 50 atoms
    and 52 bonds and the same declared normalized InChI/key. Both canonical SMILES
    comparisons are false and the limited correspondence is empty. Two SMILES amides
    become two C(OH)=N sites in the InChI-derived form while four ester carbonyls
    persist. The specific saved change is compatible with representation normalization;
    full graph and natural identity are not established by key agreement. Both canonical
    SMILES comparisons are false; the saved map is empty, complete_atom_count_match
    is false and full_graph_identity_established is false.
  snapshot_sha256: b8723a2c2f820f7bded66a674a1aa9228bf11d19c25f92fb816090125edecfc9
- evidence_id: support-2817-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed/atoms; /records/6/smiles/computed/potential_stereo;
    /records/6/smiles/computed/bonds; /records/6/inchi/computed/atoms; /records/6/inchi/computed/potential_stereo;
    /records/6/inchi/computed/bonds
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Seven tetrahedral centres are specified in each form. Saved SMILES atom
    CIP values are S at indices 0, 20, 24, 38 and 46 and R at 7 and 9; corresponding
    InChI-derived centres retain the same configured scaffold. Two unspecified double-bond
    candidates appear only in the imidic InChI-derived representation. The true source
    stereo_complete flag measures atom-centre completeness and does not assign every
    possible representation-dependent double geometry or establish natural-sample
    configuration.
  snapshot_sha256: b8723a2c2f820f7bded66a674a1aa9228bf11d19c25f92fb816090125edecfc9
- evidence_id: support-2817-motifs
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed/motifs; /records/6/smiles/computed/rings; /records/6/smiles/computed/bonds;
    /records/6/smiles/computed/atoms; /records/6/inchi/computed/motifs; /records/6/inchi/computed/rings;
    /records/6/inchi/computed/bonds; /records/6/inchi/computed/atoms
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: The 15-membered macrocycle, two aromatic six-membered rings and four C(=O)-O-C
    links are retained in both tables. SMILES amides 26/25 and 33/32 become InChI-derived
    C(OH)=N sites 30/37/41 and 17/36/38. The hydroxy/gem-dimethyl, benzyl, isopropyl
    and sec-butyl substituent topology remains explicit. No candidate saturated C5O
    sugar ring is reported. Only the two stored owner strings were parsed; no source
    alternate or congener was reparsed.
  snapshot_sha256: b8723a2c2f820f7bded66a674a1aa9228bf11d19c25f92fb816090125edecfc9
- evidence_id: support-2817-molecularreading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/support-prep/support-current282-last-five-molecular-intake-reading-001.json
  locator: /records/1; /counts; /warnings
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete ten saved forms personally read, 492 atoms/510 bonds/28 ring rows/120
    potential-stereo rows; no molecular replay. Six original undefined-stereo warning
    lines remain globally unassigned; none is assigned to an individual owner.
  snapshot_sha256: e4ad9a6b3627859a47aaf7335070c481f37fc27f761531c369b0431e70053d7d
- evidence_id: support-2817-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Single original diagnostic command and retained streams; no replay.
  snapshot_sha256: edbe8e835223207019e1654a83719f8f5a4356c9c4ce4bf65b3416defeeced22
- evidence_id: support-2817-diagaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/root-current282-diagnostic-acceptance-001.json
  locator: /status; /accepted; /diagnostic; /execution
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: ROOT accepted the original stored-form diagnostic.
  snapshot_sha256: aa0cfe84870e49a819a87cbbc8094e2522a8e8b0143bd6bb21bcb29d1211679b
- evidence_id: support-2817-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/chemistry-local/diagnostic-original-001.stderr
  locator: complete six original warning lines
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Six original undefined-stereo warning lines remain globally unassigned;
    none is assigned to an individual owner.
  snapshot_sha256: da9c0e81ec69521d5ee373f4100f63c8d2d23091a4f6562a0e39bfafc12e03f6
- evidence_id: support-2817-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/native-prep/native-current282-cached-taxonomy-reading-001.json
  locator: /context_interpretations/16; /physical_negative_query_scopes/16; /whole_stanzas
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Keep BGC0001695 producer Streptomyces conglobatus (1653203), MH128122.1
    and PMID:29979567 distinct from LOTUS Streptomyces orinoci (67339) at DOI:10.1016/S0040-4020(01)82768-X.
    SOURCE_ASSERTION/CLUSTER_UNSTATED and unknown source completeness remain bounded;
    the shared neoantimycin name does not merge producer, occurrence, congener or
    experiment. All saved source taxon IDs have complete cache stanzas; no forward
    merge or nonorganism match is retained for this context. Cached labels and synonyms
    do not establish current remote taxonomy, lineage, production or strain identity.
  snapshot_sha256: 1af1cb0b6cd2ad65ea34a03d0f9c8a746e250c6b9e51cd28c7bc15238b82c98a
- evidence_id: support-2817-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/native-prep/native-current282-implemented-curation-scan-001.json
  locator: /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows;
    /interpretation
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: No exact applicable maintained correction; lexical names, related BGC rows
    and an assay exclusion for another complete chemical identity do not transfer
    decisions.
  snapshot_sha256: f6c068d113e15f780e75e277a2f18431aca40b12e9343964db87f8043c2c7fd5
  search_scope: Native complete nine-table/3422-row scan, exact owner/full-key/BGC/occurrence/assay
    predicates; no new query or universal absence.
- evidence_id: support-2817-producerpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: complete method grading table
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Producer evidence and locus methods answer different questions; missing
    methods retain their stated grade.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2817-stereopolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142-173, complete structure_fields; specifically lines 167-168 FindMolChiralCenters
    and unassigned atom-centre predicate
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Source stereo_complete covers atom centres, not E/Z completeness or natural
    identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2817-filingpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295-306, choose_pathway
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: One supported normalized pathway selects filing; multiple, none or unsupported
    values retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2817-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch282/root-current282-five-gates-acceptance-001.json
  locator: /records; /all_native_gates_passed; /selected_queue_rows; /unavailable_required_gates
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Five local gates pass, with required QC/OAK unavailable. Queue entries
    remain diagnostic leads, not scientific findings.
  snapshot_sha256: c371d0597706c9c881bd2f515a1314108d3eaa162d3ff8d18acd48b74db9239e
- evidence_id: support-2817-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch282/owner-capture-DATA-001.json
  locator: /records/6/owner_document/curation_history; /records/6/owner_document/source_concepts
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: MIBiG PMID:29979567 and LOTUS DOI:10.1016/S0040-4020(01)82768-X have different
    assertion scopes. The two seeding histories retain their provenance without adding
    independent experimental confirmation. Primary papers, spectra and sequence evidence
    were not newly checked.
  snapshot_sha256: 2a94e2ad0338b4b959ef7a27e176ebdb67a903ecd83f041068dac2a3e1f8cd35
- evidence_id: support-2817-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-target-input-plan-001.json
  locator: /records/6/complete_root_keys; /records/6/declared_mechanism_roots_literal;
    /records/6/component_paths; /records/6/complete_raw_mechanism_sections
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: The complete captured owner has no graph, graph reference, pathway, target,
    activity or component root and requires no maintained reader. Source locus and
    classification assertions do not supply missing mechanistic steps.
  snapshot_sha256: 92b2c735b1716c07a2fea1c7c34caf4ad63fa45e2b2be7236ccf7ad97beaa06b
- evidence_id: support-2817-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete saved mibig_compounds frame with 1 positive placements read.
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JIJATTFJYJZEBT-MDDNAQDNSA-N" only; no source replay or universal absence.
- evidence_id: support-2817-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical line 2016, raw UTF-8 row SHA-256 681a95db254b110fff286e10c12b5bacf6622c4d0cf7bf97e52a604b801925ae
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: The complete key JIJATTFJYJZEBT-MDDNAQDNSA-N and BGC0001695:1 distinguish
    this source form under the literal neoantimycin label. A same-label record does
    not establish equivalent stereochemistry or production. The current owner has
    no direct-companion or explicit comparison inputs, so no additional counterpart
    chemical assessment is claimed. BGC0001695 version 5, compound index 1, attributes
    Streptomyces conglobatus (NCBITaxon:1653203) as SOURCE_ASSERTION producer. The
    entry remains active with questionable quality and unknown completeness. It is
    not interchangeable with the separately cited Streptomyces orinoci occurrence.
    MH128122.1 has blank coordinate bounds and no stated locus method, retaining CLUSTER_UNSTATED.
    Source NRPS/Type I and npatlas:NPA010703 are literal assertions; PMID:29979567
    is entry-level evidence, not fresh pathway validation.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2817-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete saved chebi_structures frame with 0 positive placements read.
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JIJATTFJYJZEBT-MDDNAQDNSA-N" only; no source replay or universal absence.
- evidence_id: support-2817-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete saved lotus_occurrences frame with 1 positive placements read.
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JIJATTFJYJZEBT-MDDNAQDNSA-N" only; no source replay or universal absence.
- evidence_id: support-2817-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical line 3028, raw UTF-8 row SHA-256 96400dfaf42a6abcdff7a28b13f9b9acd5fe6ddfadee610f905c2660ac299c80
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: LOTUS physical line 3028 retains Streptomyces orinoci (NCBITaxon:67339),
    structure Q77498040 and DOI:10.1016/S0040-4020(01)82768-X. This occurrence differs
    from the source producer taxon and remains a separate cited assertion. Cached
    taxonomy does not establish strain equivalence or publication independence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2817-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame with 0 positive placements
    read.
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JIJATTFJYJZEBT-MDDNAQDNSA-N" only; no source replay or universal absence.
- evidence_id: support-2817-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete saved npclassifier frame with 1 positive placements read.
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JIJATTFJYJZEBT-MDDNAQDNSA-N" only; no source replay or universal absence.
- evidence_id: support-2817-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical line 1115, raw UTF-8 row SHA-256 3230b89a70cbde05f5cbb1ff97f33f7554ae881c7297b3a3705f2830f2b4a9eb
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: NPClassifier retains Amino acids and Peptides|Polyketides, Macrolides,
    Antimycins and is_glycoside false at the retained 2026-09-07 model version. Multiple
    pathways explain UNCLASSIFIED filing; source NRPS and topology remain distinct
    evidence from model predictions.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2817-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame with 0 positive placements read.
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JIJATTFJYJZEBT-MDDNAQDNSA-N" only; no source replay or universal absence.
- evidence_id: support-2817-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete saved bindingdb_targets frame with 0 positive placements read.
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JIJATTFJYJZEBT-MDDNAQDNSA-N" only; no source replay or universal absence.
- evidence_id: support-2817-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame with 0 positive placements
    read.
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JIJATTFJYJZEBT-MDDNAQDNSA-N" only; no source replay or universal absence.
- evidence_id: support-2817-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch282-tentative/bgc-prep/bgc-conditional282-source-inventory-DATA-001.json
  locator: /contexts/16/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T03:34:22.869459Z'
  support: supports
  summary: Complete saved chebi_origins frame with 0 positive placements read.
  snapshot_sha256: cab9ddfed1920f3e3be3dbc29c5ec8cfb2b2e9ed4bbdecd7af1472a805f26387
  search_scope: Retained uncapped predicate exact chebi_id from exact full-key structure
    rows and query [] only; no source replay or universal absence.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-282/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json
  accessed_at: '2026-11-07T02:57:33.203784Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 64d3574e79778146d92ca263450b21c2b1069ed2e3c619de74334e87646ea9bb
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-282/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json
  accessed_at: '2026-11-07T02:57:58.096578Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: fe9b4651b4ba89812db89378bcc5bd759f45f66d8d27a8bae471ff3e72ef0180
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-282/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json
  accessed_at: '2026-11-07T02:58:17.725128Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-282/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json
  accessed_at: '2026-11-07T02:58:51.640951Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-282/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-282/native-current282-five-gates-execution-001.json
  accessed_at: '2026-11-07T02:59:03.312006Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 242feea98ad824bbb95284fc6ee693a3464fd1917a299d276b43d18e23f24d2a
assessments:
- assessment_id: support-2817-identity-assessment
  area: identity
  topic: Exact retained compound grounding
  summary: The complete key JIJATTFJYJZEBT-MDDNAQDNSA-N and BGC0001695:1 distinguish
    this source form under the literal neoantimycin label. A same-label record does
    not establish equivalent stereochemistry or production. The current owner has
    no direct-companion or explicit comparison inputs, so no additional counterpart
    chemical assessment is claimed.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  evidence_ids:
  - support-2817-owner
  - support-2817-capture
  - support-2817-source
  - support-2817-intake
  - support-2817-curation
  - support-2817-plan
  - support-2817-table-mibig_compounds
  - support-2817-table-lotus_occurrences
  - support-2817-table-npclassifier
  dimensions:
  - name: standard_inchi_key
    definition: Full key rather than label matching.
    value: JIJATTFJYJZEBT-MDDNAQDNSA-N
    evidence_ids:
    - support-2817-owner
    - support-2817-capture
    - support-2817-source
    - support-2817-intake
    - support-2817-curation
    - support-2817-plan
    - support-2817-table-mibig_compounds
    - support-2817-table-lotus_occurrences
    - support-2817-table-npclassifier
  - name: grounding_scope
    definition: Retained source identity is distinct from natural identity.
    value: The complete key JIJATTFJYJZEBT-MDDNAQDNSA-N and BGC0001695:1 distinguish
      this source form under the literal neoantimycin label. A same-label record does
      not establish equivalent stereochemistry or production. The current owner has
      no direct-companion or explicit comparison inputs, so no additional counterpart
      chemical assessment is claimed.
    evidence_ids:
    - support-2817-owner
    - support-2817-capture
    - support-2817-source
    - support-2817-intake
    - support-2817-curation
    - support-2817-plan
    - support-2817-table-mibig_compounds
    - support-2817-table-lotus_occurrences
    - support-2817-table-npclassifier
- assessment_id: support-2817-representation-assessment
  area: representation
  topic: Saved molecular forms and stereochemical scope
  summary: Both stored forms parse to one neutral C36H46N2O12 fragment with 50 atoms
    and 52 bonds and the same declared normalized InChI/key. Both canonical SMILES
    comparisons are false and the limited correspondence is empty. Two SMILES amides
    become two C(OH)=N sites in the InChI-derived form while four ester carbonyls
    persist. The specific saved change is compatible with representation normalization;
    full graph and natural identity are not established by key agreement. The 15-membered
    macrocycle, two aromatic six-membered rings and four C(=O)-O-C links are retained
    in both tables. SMILES amides 26/25 and 33/32 become InChI-derived C(OH)=N sites
    30/37/41 and 17/36/38. The hydroxy/gem-dimethyl, benzyl, isopropyl and sec-butyl
    substituent topology remains explicit. No candidate saturated C5O sugar ring is
    reported. Only the two stored owner strings were parsed; no source alternate or
    congener was reparsed. Both canonical SMILES comparisons are false; the saved
    map is empty, complete_atom_count_match is false and full_graph_identity_established
    is false. Normalized key/formula agreement and a successful local process do not
    establish independent full graph identity, natural-sample identity, experimental
    absolute stereochemistry, primary mechanism validation or a native status promotion.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  evidence_ids:
  - support-2817-data
  - support-2817-stereo
  - support-2817-motifs
  - support-2817-molecularreading
  - support-2817-execution
  - support-2817-diagaccept
  - support-2817-stereopolicy
  - support-2817-plan
  dimensions:
  - name: stereochemistry_scope
    definition: Specified atom centres and representation-dependent candidates remain
      distinct.
    value: Seven tetrahedral centres are specified in each form. Saved SMILES atom
      CIP values are S at indices 0, 20, 24, 38 and 46 and R at 7 and 9; corresponding
      InChI-derived centres retain the same configured scaffold. Two unspecified double-bond
      candidates appear only in the imidic InChI-derived representation. The true
      source stereo_complete flag measures atom-centre completeness and does not assign
      every possible representation-dependent double geometry or establish natural-sample
      configuration.
    evidence_ids:
    - support-2817-data
    - support-2817-stereo
    - support-2817-motifs
    - support-2817-molecularreading
    - support-2817-execution
    - support-2817-diagaccept
    - support-2817-stereopolicy
    - support-2817-plan
  - name: representation_correspondence
    definition: Saved limited comparison, not full identity.
    value: Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match
      is false and full_graph_identity_established is false. Normalized key/formula
      agreement and a successful local process do not establish independent full graph
      identity, natural-sample identity, experimental absolute stereochemistry, primary
      mechanism validation or a native status promotion.
    evidence_ids:
    - support-2817-data
    - support-2817-stereo
    - support-2817-motifs
    - support-2817-molecularreading
    - support-2817-execution
    - support-2817-diagaccept
    - support-2817-stereopolicy
    - support-2817-plan
- assessment_id: support-2817-provenance-assessment
  area: provenance
  topic: Compound-specific producer, locus and taxon
  summary: BGC0001695 version 5, compound index 1, attributes Streptomyces conglobatus
    (NCBITaxon:1653203) as SOURCE_ASSERTION producer. The entry remains active with
    questionable quality and unknown completeness. It is not interchangeable with
    the separately cited Streptomyces orinoci occurrence. MH128122.1 has blank coordinate
    bounds and no stated locus method, retaining CLUSTER_UNSTATED. Source NRPS/Type
    I and npatlas:NPA010703 are literal assertions; PMID:29979567 is entry-level evidence,
    not fresh pathway validation.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  evidence_ids:
  - support-2817-source
  - support-2817-capture
  - support-2817-taxonomy
  - support-2817-curation
  - support-2817-producerpolicy
  - support-2817-table-mibig_compounds
  - support-2817-table-lotus_occurrences
  - support-2817-table-npclassifier
  dimensions:
  - name: taxon_scope
    definition: Cached names do not establish current lineage or strain equivalence.
    value: Keep BGC0001695 producer Streptomyces conglobatus (1653203), MH128122.1
      and PMID:29979567 distinct from LOTUS Streptomyces orinoci (67339) at DOI:10.1016/S0040-4020(01)82768-X.
      SOURCE_ASSERTION/CLUSTER_UNSTATED and unknown source completeness remain bounded;
      the shared neoantimycin name does not merge producer, occurrence, congener or
      experiment. All saved source taxon IDs have complete cache stanzas; no forward
      merge or nonorganism match is retained for this context. Cached labels and synonyms
      do not establish current remote taxonomy, lineage, production or strain identity.
    evidence_ids:
    - support-2817-source
    - support-2817-capture
    - support-2817-taxonomy
    - support-2817-curation
    - support-2817-producerpolicy
    - support-2817-table-mibig_compounds
    - support-2817-table-lotus_occurrences
    - support-2817-table-npclassifier
  - name: producer_evidence
    definition: Producer and locus evidence remain separate.
    value: BGC0001695 version 5, compound index 1, attributes Streptomyces conglobatus
      (NCBITaxon:1653203) as SOURCE_ASSERTION producer. The entry remains active with
      questionable quality and unknown completeness. It is not interchangeable with
      the separately cited Streptomyces orinoci occurrence.
    evidence_ids:
    - support-2817-source
    - support-2817-capture
    - support-2817-taxonomy
    - support-2817-curation
    - support-2817-producerpolicy
    - support-2817-table-mibig_compounds
    - support-2817-table-lotus_occurrences
    - support-2817-table-npclassifier
  - name: locus_evidence
    definition: Exact source version, endpoints and methods delimit the claim.
    value: MH128122.1 has blank coordinate bounds and no stated locus method, retaining
      CLUSTER_UNSTATED. Source NRPS/Type I and npatlas:NPA010703 are literal assertions;
      PMID:29979567 is entry-level evidence, not fresh pathway validation.
    evidence_ids:
    - support-2817-source
    - support-2817-capture
    - support-2817-taxonomy
    - support-2817-curation
    - support-2817-producerpolicy
    - support-2817-table-mibig_compounds
    - support-2817-table-lotus_occurrences
    - support-2817-table-npclassifier
- assessment_id: support-2817-citations-assessment
  area: evidence
  topic: Citation grain and retained history
  summary: MIBiG PMID:29979567 and LOTUS DOI:10.1016/S0040-4020(01)82768-X have different
    assertion scopes. The two seeding histories retain their provenance without adding
    independent experimental confirmation. Primary papers, spectra and sequence evidence
    were not newly checked.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  evidence_ids:
  - support-2817-owner
  - support-2817-source
  - support-2817-capture
  - support-2817-history
  - support-2817-table-mibig_compounds
  - support-2817-table-lotus_occurrences
  - support-2817-table-npclassifier
  dimensions:
  - name: citation_scope
    definition: Repeated annotations are not independent primary proof.
    value: MIBiG PMID:29979567 and LOTUS DOI:10.1016/S0040-4020(01)82768-X have different
      assertion scopes. The two seeding histories retain their provenance without
      adding independent experimental confirmation. Primary papers, spectra and sequence
      evidence were not newly checked.
    evidence_ids:
    - support-2817-owner
    - support-2817-source
    - support-2817-capture
    - support-2817-history
    - support-2817-table-mibig_compounds
    - support-2817-table-lotus_occurrences
    - support-2817-table-npclassifier
- assessment_id: support-2817-occurrence-assay-assessment
  area: evidence
  topic: Occurrence and assay limits
  summary: LOTUS physical line 3028 retains Streptomyces orinoci (NCBITaxon:67339),
    structure Q77498040 and DOI:10.1016/S0040-4020(01)82768-X. This occurrence differs
    from the source producer taxon and remains a separate cited assertion. Cached
    taxonomy does not establish strain equivalence or publication independence. No
    actual PubChem assay, BindingDB target or AntibioticMech exact-key row occurs
    in this saved context. The bounded negative frames are not evidence of inactivity
    and do not transfer activity from another neoantimycin form.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  evidence_ids:
  - support-2817-source
  - support-2817-taxonomy
  - support-2817-curation
  - support-2817-plan
  - support-2817-query-mibig_compounds
  - support-2817-query-chebi_structures
  - support-2817-query-lotus_occurrences
  - support-2817-query-cyanometdb_occurrences
  - support-2817-query-npclassifier
  - support-2817-query-pubchem_bioassay
  - support-2817-query-bindingdb_targets
  - support-2817-query-antibioticmech_inchikeys
  - support-2817-query-chebi_origins
  - support-2817-table-mibig_compounds
  - support-2817-table-lotus_occurrences
  - support-2817-table-npclassifier
  dimensions:
  - name: occurrence_scope
    definition: Occurrence does not establish production.
    value: LOTUS physical line 3028 retains Streptomyces orinoci (NCBITaxon:67339),
      structure Q77498040 and DOI:10.1016/S0040-4020(01)82768-X. This occurrence differs
      from the source producer taxon and remains a separate cited assertion. Cached
      taxonomy does not establish strain equivalence or publication independence.
    evidence_ids:
    - support-2817-source
    - support-2817-taxonomy
    - support-2817-curation
    - support-2817-plan
    - support-2817-query-mibig_compounds
    - support-2817-query-chebi_structures
    - support-2817-query-lotus_occurrences
    - support-2817-query-cyanometdb_occurrences
    - support-2817-query-npclassifier
    - support-2817-query-pubchem_bioassay
    - support-2817-query-bindingdb_targets
    - support-2817-query-antibioticmech_inchikeys
    - support-2817-query-chebi_origins
    - support-2817-table-mibig_compounds
    - support-2817-table-lotus_occurrences
    - support-2817-table-npclassifier
  - name: assay_target_scope
    definition: Binding observations and classification are distinct; negative frames
      are not inactivity.
    value: No actual PubChem assay, BindingDB target or AntibioticMech exact-key row
      occurs in this saved context. The bounded negative frames are not evidence of
      inactivity and do not transfer activity from another neoantimycin form.
    evidence_ids:
    - support-2817-source
    - support-2817-taxonomy
    - support-2817-curation
    - support-2817-plan
    - support-2817-query-mibig_compounds
    - support-2817-query-chebi_structures
    - support-2817-query-lotus_occurrences
    - support-2817-query-cyanometdb_occurrences
    - support-2817-query-npclassifier
    - support-2817-query-pubchem_bioassay
    - support-2817-query-bindingdb_targets
    - support-2817-query-antibioticmech_inchikeys
    - support-2817-query-chebi_origins
    - support-2817-table-mibig_compounds
    - support-2817-table-lotus_occurrences
    - support-2817-table-npclassifier
- assessment_id: support-2817-classification-assessment
  area: consistency
  topic: Source classes, model labels and filing
  summary: NPClassifier retains Amino acids and Peptides|Polyketides, Macrolides,
    Antimycins and is_glycoside false at the retained 2026-09-07 model version. Multiple
    pathways explain UNCLASSIFIED filing; source NRPS and topology remain distinct
    evidence from model predictions.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  evidence_ids:
  - support-2817-source
  - support-2817-owner
  - support-2817-motifs
  - support-2817-filingpolicy
  - support-2817-gates
  - support-2817-table-mibig_compounds
  - support-2817-table-lotus_occurrences
  - support-2817-table-npclassifier
  dimensions:
  - name: classification_applicability
    definition: Model, source, saved topology and biological class are separate evidence.
    value: NPClassifier retains Amino acids and Peptides|Polyketides, Macrolides,
      Antimycins and is_glycoside false at the retained 2026-09-07 model version.
      Multiple pathways explain UNCLASSIFIED filing; source NRPS and topology remain
      distinct evidence from model predictions.
    evidence_ids:
    - support-2817-source
    - support-2817-owner
    - support-2817-motifs
    - support-2817-filingpolicy
    - support-2817-gates
    - support-2817-table-mibig_compounds
    - support-2817-table-lotus_occurrences
    - support-2817-table-npclassifier
- assessment_id: support-2817-completion-assessment
  area: completeness
  topic: Earned work and unavailable authority
  summary: Complete assigned raw/source/intake and both saved molecular forms were
    read. The complete captured owner has no graph, graph reference, pathway, target,
    activity or component root and requires no maintained reader. Source locus and
    classification assertions do not supply missing mechanistic steps. Five local
    native commands pass; full QC, complete OAK and fresh primary verification remain
    unavailable. Completion is partial, native SEEDED status unchanged.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-3f35f559e8
  evidence_ids:
  - support-2817-intake
  - support-2817-intakeaccept
  - support-2817-plan
  - support-2817-planaccept
  - support-2817-notes
  - support-2817-gates
  - support-2817-data
  - support-2817-diagaccept
  - support-2817-scope
  dimensions:
  - name: review_completion
    definition: Local review does not promote native status or substitute for unavailable
      checks.
    value: Complete assigned raw/source/intake and both saved molecular forms were
      read. The complete captured owner has no graph, graph reference, pathway, target,
      activity or component root and requires no maintained reader. Source locus and
      classification assertions do not supply missing mechanistic steps. Five local
      native commands pass; full QC, complete OAK and fresh primary verification remain
      unavailable. Completion is partial, native SEEDED status unchanged.
    evidence_ids:
    - support-2817-intake
    - support-2817-intakeaccept
    - support-2817-plan
    - support-2817-planaccept
    - support-2817-notes
    - support-2817-gates
    - support-2817-data
    - support-2817-diagaccept
    - support-2817-scope
findings: []
actions: []
limitations:
- Normalized key/formula agreement and a successful local process do not establish
  independent full graph identity, natural-sample identity, experimental absolute
  stereochemistry, primary mechanism validation or a native status promotion.
- Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match
  is false and full_graph_identity_established is false. Seven tetrahedral centres
  are specified in each form. Saved SMILES atom CIP values are S at indices 0, 20,
  24, 38 and 46 and R at 7 and 9; corresponding InChI-derived centres retain the same
  configured scaffold. Two unspecified double-bond candidates appear only in the imidic
  InChI-derived representation. The true source stereo_complete flag measures atom-centre
  completeness and does not assign every possible representation-dependent double
  geometry or establish natural-sample configuration.
- Six original undefined-stereo warning lines remain globally unassigned; none is
  assigned to an individual owner.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK
  remain unavailable; source/database claims retain their exact authority.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh current 282 evidence and judgments; prior batches provide interface logic
  only.
- No source row, record, campaign or native status was changed; no query, molecular
  parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual native checks and three required unavailable checks. Only
  selected order 2818 requires a maintained-reader check; unselected companions remain
  context only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-282
```
