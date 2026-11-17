# Local evidence review: nodulisporic acid F

- Review: 20261107T044643Z-nodulisporic-acid-f
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T04:12:19.967847Z
- Finished UTC: 2026-11-07T04:46:43.575213Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Nodulisporic acid F has matching saved canonical forms, a coherent indole-containing fused scaffold, six specified atom centres and one E alkene. The stated source producer and separate occurrence remain distinct. No material local defect is established; the review is a qualified partial pass.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2830; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-094f8c95c8 | data/natural_products/unclassified/nodulisporic-acid-f.yaml | generated | nodulisporic acid F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-094f8c95c8 | Both stored forms parsed with declared normalized keys and formula agreement. Both canonical SMILES comparisons agree and the limited 32-atom map is complete; full_graph_identity_established nevertheless remains false. |
| strict_ten | passed | True | naturalproductmech:mibig-094f8c95c8 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-094f8c95c8 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-094f8c95c8 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-094f8c95c8 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-094f8c95c8 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-094f8c95c8 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-094f8c95c8 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-094f8c95c8 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained compound grounding

identity: supported. Targets: naturalproductmech:mibig-094f8c95c8.

The selected owner naturalproductmech:mibig-094f8c95c8 is active MIBiG BGC0001706 version 3 compound index 1 with full key FYZYVTHTMPXJHJ-UOOBVZAFSA-N and retained NPAtlas NPA09237. Its explicit-H source spelling and normalized local comparison identify the retained representation without independently proving the natural isolated compound.

### Saved molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-094f8c95c8.

Both neutral single-component forms have 32 atoms and 36 bonds, formula C28H37NO3, matching canonical isomeric/nonisomeric strings and the declared normalized InChI/key. Five reported ring rows have sizes 5,5,6,6,6, including the fused aromatic indole and adjoining carbocyclic scaffold. A neutral carboxylic acid and an alcohol are retained; no ester or amide motif is reported by the strict predicates. SMILES acid carbon 26 has double-bond oxygen 28 and single-bond OH 27; alcohol oxygen 18 is attached to stereocentre 17. The E alkene is bond 23 between atoms 23 and 24. InChI counterparts are acid carbon 24/O30/O31, alcohol O29 on carbon 22, and E bond 9 (7=16). The five-ring indole includes [nH] and the six-ring aromatic system; the remaining rings are carbocyclic. Ring/motif predicates do not assign natural biosynthetic steps. Both canonical SMILES comparisons agree and the limited 32-atom map is complete; full_graph_identity_established nevertheless remains false. Normalized identifiers, formula agreement and local parsing do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry or primary biological validation.

### Compound-specific producer, locus and taxon

provenance: supported. Targets: naturalproductmech:mibig-094f8c95c8.

Hypoxylon pulicicidum, NCBITaxon:1243767, is the MIBiG SOURCE_ASSERTION producer; this remains distinct from a LOTUS Nodulisporium occurrence. MG182145.1:42700–71644 remains CLUSTER_UNSTATED with blank locus methods. BGC0001706 version 3 has questionable quality and unknown completeness. The lowercase terpene BGC class and Unknown subclass are separate retained fields.

### Citation grain and retained history

evidence: supported. Targets: naturalproductmech:mibig-094f8c95c8.

PMID:29283570 is ENTRY-level MIBiG evidence; DOI:10.1021/NP0498455 is a separate occurrence pointer. Distinct pointers do not establish publication independence without reading their contents. The two import-history events document processing, not new experiments.

### Occurrence and assay limits

evidence: supported. Targets: naturalproductmech:mibig-094f8c95c8.

LOTUS reports Nodulisporium/NCBITaxon:96453. Cached labels give no lineage or synonym assertion equating it with Hypoxylon pulicicidum; no producer/occurrence identity repair follows. This owner has no direct companion under the current exact predicate. Saved ChEBI, CyanoMetDB, PubChem, BindingDB, AntibioticMech and origins frames are negative; no actual AID, blank assay sentinel or measured target is established. Negative saved queries are not universal biological absence.

### Source classes, model labels and filing

consistency: supported. Targets: naturalproductmech:mibig-094f8c95c8.

NPClassifier predicts Alkaloids plus Terpenoids, Tryptophan alkaloids and Indole-Diterpenoid alkaloids (Penitrems), with is_glycoside:false. The saved indole-containing fused scaffold is compatible with descriptive alkaloid/terpenoid language, not proof of a biosynthetic route. Two pathway results correctly leave filing UNCLASSIFIED; compound_classes is blank and NPAtlas is not identity validation.

### Earned work and unavailable authority

completeness: supported. Targets: naturalproductmech:mibig-094f8c95c8.

Complete selected owner, actual source/intake and both saved molecular forms were read. The complete selected owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary, related_records or component root. No maintained reader is applicable. This bounded record absence does not assert absent biology or missing upstream experimental mechanisms. No material local defect was established within this bounded evidence. Five local gates pass; full QC, complete OAK and fresh primary/external verification remain unavailable. Completion is partial and native SEEDED status is unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2830-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/nodulisporic-acid-f.yaml; complete file: identifier, label, chemical_structure, source_concepts, producer_organisms, biosynthetic_gene_clusters, classification and curation_history | supports | Complete current selected owner; generated source facts and field absence remain attributed. |
| support-2830-capture | /private/tmp/npm-review-work/shared-next-batch283/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete accepted owner capture of the current stored record. |
| support-2830-source | /private/tmp/npm-review-work/shared-next-batch283-tentative/support-prep/support-current283-assigned-source-reading-002.json; /contexts/5; /selected_counts; /companion_counts; /global_cautions | supports | Own complete current selected source credit is 17 rows/208 fields/45 frames/28 negatives. The sole unselected nocobactin NA adds four companion rows/49 fields, not an additional selected target. |
| support-2830-plan | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-target-input-plan-001.json; /records/9; /source_placement_count; /unique_source_path_count | supports | Accepted 459-placement/54-path plan; this owner has 44 actual captured inputs. |
| support-2830-planaccept | /private/tmp/npm-review-work/shared-next-batch283/root-current283-source-plan-acceptance-001.json; /status; /accepted; /plan | supports | ROOT accepted the original source plan. |
| support-2830-notes | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /curation | supports | Current disjoint BGC16 plus Support21 named source rows; Native and overlapping ROOT readings add zero primary-row credit. |
| support-2830-intake | /private/tmp/npm-review-work/shared-next-batch283/intakes-001/2830-inspect-001.json; /status; /source; /targets | supports | Actual canonical intake fixes current input hashes, generated target and maintained ownership. |
| support-2830-intakeaccept | /private/tmp/npm-review-work/shared-next-batch283/root-current283-intakes-acceptance-001.json; /status; /accepted; /summary | supports | All ten original intakes exited zero with empty stderr; no reruns. |
| support-2830-data | /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles; /records/9/inchi; /records/9/comparisons; /records/9/atom_correspondence; /records/9/literal_InChI_layers; /records/9/formula_comparison_scope | supports | Both neutral single-component forms have 32 atoms and 36 bonds, formula C28H37NO3, matching canonical isomeric/nonisomeric strings and the declared normalized InChI/key. Five reported ring rows have sizes 5,5,6,6,6, including the fused aromatic indole and adjoining carbocyclic scaffold. A neutral carboxylic acid and an alcohol are retained; no ester or amide motif is reported by the strict predicates. Both canonical SMILES comparisons agree and the limited 32-atom map is complete; full_graph_identity_established nevertheless remains false. |
| support-2830-stereo | /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles/computed/atoms; /records/9/smiles/computed/bonds; /records/9/smiles/computed/potential_stereo; /records/9/inchi/computed/atoms; /records/9/inchi/computed/bonds; /records/9/inchi/computed/potential_stereo | supports | Both forms retain six specified tetrahedral centres and one specified alkene. The saved bond enums are STEREOE even though the potential-stereo descriptor is Bond_Cis, a different local-control frame. Neither descriptor is substituted for the other; no new experimental absolute configuration is claimed. |
| support-2830-motifs | /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles/computed/atoms; /records/9/smiles/computed/bonds; /records/9/smiles/computed/rings; /records/9/smiles/computed/motifs; /records/9/inchi/computed/atoms; /records/9/inchi/computed/bonds; /records/9/inchi/computed/rings; /records/9/inchi/computed/motifs | supports | SMILES acid carbon 26 has double-bond oxygen 28 and single-bond OH 27; alcohol oxygen 18 is attached to stereocentre 17. The E alkene is bond 23 between atoms 23 and 24. InChI counterparts are acid carbon 24/O30/O31, alcohol O29 on carbon 22, and E bond 9 (7=16). The five-ring indole includes [nH] and the six-ring aromatic system; the remaining rings are carbocyclic. Ring/motif predicates do not assign natural biosynthetic steps. |
| support-2830-molecularreading | /private/tmp/npm-review-work/shared-next-batch283-tentative/support-prep/support-current283-last-five-molecular-intake-reading-001.json; /records/4; /counts; /interpretations/2830; /warnings | supports | Personally read complete ten saved forms:410 atoms/422 bonds/22 ring rows/44 potential-stereo entries. No new parse. |
| support-2830-execution | /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /retries; /stderr | supports | One original diagnostic execution exited zero with no retry. |
| support-2830-diagaccept | /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /scientific_limits | supports | ROOT accepted the original stored-form diagnostic; scientific interpretation remains bounded. |
| support-2830-stderr | /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnostic-original-001.stderr; complete two original warning lines | supports | Two original Omitted undefined stereo warning lines remain globally unassigned; neither is attributed to an individual owner. |
| support-2830-taxonomy | /private/tmp/npm-review-work/shared-next-batch283-tentative/native-prep/native-current283-cached-taxonomy-reading-001.json; /context_interpretations/10; /physical_negative_query_scopes/10; /whole_stanzas | supports | Keep Hypoxylon pulicicidum (1243767), BGC0001706:1 and MG182145.1:42700–71644 source producer/locus separate from LOTUS genus Nodulisporium (96453) occurrence at DOI:10.1021/NP0498455. Preserve SOURCE_ASSERTION/CLUSTER_UNSTATED and entry-level PMID:29283570. The cache supplies no lineage or synonym assertion connecting these two labels; no producer/occurrence identity repair follows. All saved source taxon IDs have complete local cache stanzas; no forward merge or nonorganism match is retained for this context. Cached labels/synonyms do not establish rank, lineage, freshness, production or strain equivalence. |
| support-2830-curation | /private/tmp/npm-review-work/shared-next-batch283-tentative/native-prep/native-current283-implemented-curation-scan-001.json; /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows; /interpretation | supports | Nine substantive tables retain no exact applicable maintained correction; lexical matches and unrelated assay exclusions do not transfer. |
| support-2830-producerpolicy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; complete method grading table | supports | SOURCE_ASSERTION producer and CLUSTER_UNSTATED locus grades answer distinct questions. |
| support-2830-stereopolicy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142-173 structure_fields; atom-centre predicate lines 165-172 | supports | stereo_complete derives from FindMolChiralCenters and unknown atom tags; it does not assert complete E/Z or natural identity. |
| support-2830-filingpolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306 choose_pathway | supports | One supported normalized pathway chooses filing; multiple, none or unsupported results retain UNCLASSIFIED. |
| support-2830-gates | /private/tmp/npm-review-work/shared-next-batch283/root-current283-five-gates-acceptance-001.json; /five_exit_codes; /selected_queue_rows; /unavailable_required_gates; /all_native_gates_passed | supports | All five local gates pass; full QC/OAK remain unavailable and all_native_gates_passed is false. Queue leads do not independently establish defects. |
| support-2830-history | /private/tmp/npm-review-work/shared-next-batch283/owner-capture-DATA-001.json; /records/9/owner_document/curation_history; /records/9/owner_document/source_concepts | supports | PMID:29283570 is ENTRY-level MIBiG evidence; DOI:10.1021/NP0498455 is a separate occurrence pointer. Distinct pointers do not establish publication independence without reading their contents. The two import-history events document processing, not new experiments. |
| support-2830-scope | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-target-input-plan-001.json; /records/9/complete_root_keys; /records/9/declared_mechanism_roots_literal; /records/9/component_paths; /records/9/complete_raw_mechanism_sections | supports | The complete selected owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary, related_records or component root. No maintained reader is applicable. This bounded record absence does not assert absent biology or missing upstream experimental mechanisms. |
| support-2830-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds query frame with 1 matched placements. |
| support-2830-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical line 2027, raw UTF-8 row SHA-256 f4d97b8e43404f45ab05b2844e4cad3e8aca605d9026f1818d690a7ab2a0747c | supports | The selected owner naturalproductmech:mibig-094f8c95c8 is active MIBiG BGC0001706 version 3 compound index 1 with full key FYZYVTHTMPXJHJ-UOOBVZAFSA-N and retained NPAtlas NPA09237. Its explicit-H source spelling and normalized local comparison identify the retained representation without independently proving the natural isolated compound. Hypoxylon pulicicidum, NCBITaxon:1243767, is the MIBiG SOURCE_ASSERTION producer; this remains distinct from a LOTUS Nodulisporium occurrence. MG182145.1:42700–71644 remains CLUSTER_UNSTATED with blank locus methods. BGC0001706 version 3 has questionable quality and unknown completeness. The lowercase terpene BGC class and Unknown subclass are separate retained fields. |
| support-2830-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures query frame with 0 matched placements. |
| support-2830-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences query frame with 1 matched placements. |
| support-2830-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical line 2059, raw UTF-8 row SHA-256 d5babaa768f0dc3cd808a3aabb5b3e15bedef26a5f0590fa2fa6f4a2b038ca5e | supports | LOTUS reports Nodulisporium/NCBITaxon:96453. Cached labels give no lineage or synonym assertion equating it with Hypoxylon pulicicidum; no producer/occurrence identity repair follows. This owner has no direct companion under the current exact predicate. |
| support-2830-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences query frame with 0 matched placements. |
| support-2830-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier query frame with 1 matched placements. |
| support-2830-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical line 633, raw UTF-8 row SHA-256 c44da786d5ce4430ed2c45d708d979b32491130a3f5422c0718f3a5f9bf4f321 | supports | NPClassifier predicts Alkaloids plus Terpenoids, Tryptophan alkaloids and Indole-Diterpenoid alkaloids (Penitrems), with is_glycoside:false. The saved indole-containing fused scaffold is compatible with descriptive alkaloid/terpenoid language, not proof of a biosynthetic route. Two pathway results correctly leave filing UNCLASSIFIED; compound_classes is blank and NPAtlas is not identity validation. |
| support-2830-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay query frame with 0 matched placements. |
| support-2830-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets query frame with 0 matched placements. |
| support-2830-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys query frame with 0 matched placements. |
| support-2830-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins query frame with 0 matched placements. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-283/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-283/native-current283-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-283/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-283/native-current283-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-283/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-283/native-current283-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-283/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-283/native-current283-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-283/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-283/native-current283-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Normalized identifiers, formula agreement and local parsing do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry or primary biological validation.
- Both canonical SMILES comparisons agree and the limited 32-atom map is complete; full_graph_identity_established nevertheless remains false. Both forms retain six specified tetrahedral centres and one specified alkene. The saved bond enums are STEREOE even though the potential-stereo descriptor is Bond_Cis, a different local-control frame. Neither descriptor is substituted for the other; no new experimental absolute configuration is claimed.
- Two original Omitted undefined stereo warning lines remain globally unassigned; neither is attributed to an individual owner.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK remain unavailable; source/database claims retain their exact grain and authority.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh current 283 evidence and judgments; prior batches provide interface logic only.
- No source record, native status or history was changed; no query, molecular parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual local gate checks and three required unavailable checks. No maintained-reader check is applicable; unselected companions remain context only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T044643Z-nodulisporic-acid-f
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: nodulisporic acid F'
started_at: '2026-11-07T04:12:19.967847Z'
finished_at: '2026-11-07T04:46:43.575213Z'
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
summary: Nodulisporic acid F has matching saved canonical forms, a coherent indole-containing
  fused scaffold, six specified atom centres and one E alkene. The stated source producer
  and separate occurrence remain distinct. No material local defect is established;
  the review is a qualified partial pass.
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
  - path: data/natural_products/unclassified/nodulisporic-acid-f.yaml
    sha256: 8bee780b69e6bc01999b18f8844c492ccb8ab15fa7c8144c5f811a9fd024f584
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
  selection: Campaign path order 2830; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-094f8c95c8
targets:
- target_id: naturalproductmech:mibig-094f8c95c8
  path: data/natural_products/unclassified/nodulisporic-acid-f.yaml
  label: nodulisporic acid F
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnose283-001.py
    f7eed9da8b50003026558b703482191fdca29c9a922e7f43191aa9ad8b838627 ccb2947ae508c4adfbae4d738ad2378acad9430c4244387b20f044274f1f2f32
    28658a75e6bdfa0ef1853bd53a964a606a283173211532e32abc7b02ff9d8639
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed with declared normalized keys and formula agreement.
    Both canonical SMILES comparisons agree and the limited 32-atom map is complete;
    full_graph_identity_established nevertheless remains false.
  scope_note: Both neutral single-component forms have 32 atoms and 36 bonds, formula
    C28H37NO3, matching canonical isomeric/nonisomeric strings and the declared normalized
    InChI/key. Five reported ring rows have sizes 5,5,6,6,6, including the fused aromatic
    indole and adjoining carbocyclic scaffold. A neutral carboxylic acid and an alcohol
    are retained; no ester or amide motif is reported by the strict predicates. Both
    forms retain six specified tetrahedral centres and one specified alkene. The saved
    bond enums are STEREOE even though the potential-stereo descriptor is Bond_Cis,
    a different local-control frame. Neither descriptor is substituted for the other;
    no new experimental absolute configuration is claimed. Two original Omitted undefined
    stereo warning lines remain globally unassigned; neither is attributed to an individual
    owner.
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  evidence_ids:
  - support-2830-data
  - support-2830-execution
  - support-2830-diagaccept
  - support-2830-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  command: just validate-strict data/natural_products/unclassified/niizalactam-c.yaml
    data/natural_products/unclassified/nocardiopsin-a.yaml data/natural_products/unclassified/nocardiopsin-b.yaml
    data/natural_products/unclassified/nocardiopsin-c.yaml data/natural_products/unclassified/nocardiopsin-d.yaml
    data/natural_products/unclassified/nocobactin-na-10152b.yaml data/natural_products/unclassified/nocuolactylate-a.yaml
    data/natural_products/unclassified/nocuolactylate-b.yaml data/natural_products/unclassified/nocuolactylate-c.yaml
    data/natural_products/unclassified/nodulisporic-acid-f.yaml --workers 1 --out
    /private/tmp/npm-native-checks/batch-283/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-094f8c95c8
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-283/validate-all-001.tsv
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
  - naturalproductmech:mibig-094f8c95c8
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
  - naturalproductmech:mibig-094f8c95c8
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
  - naturalproductmech:mibig-094f8c95c8
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-283/review-queue-001.tsv
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
  - naturalproductmech:mibig-094f8c95c8
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2830-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/nodulisporic-acid-f.yaml
  locator: 'complete file: identifier, label, chemical_structure, source_concepts,
    producer_organisms, biosynthetic_gene_clusters, classification and curation_history'
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete current selected owner; generated source facts and field absence
    remain attributed.
  snapshot_sha256: 8bee780b69e6bc01999b18f8844c492ccb8ab15fa7c8144c5f811a9fd024f584
- evidence_id: support-2830-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch283/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete accepted owner capture of the current stored record.
  snapshot_sha256: ccb2947ae508c4adfbae4d738ad2378acad9430c4244387b20f044274f1f2f32
- evidence_id: support-2830-source
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/support-prep/support-current283-assigned-source-reading-002.json
  locator: /contexts/5; /selected_counts; /companion_counts; /global_cautions
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Own complete current selected source credit is 17 rows/208 fields/45 frames/28
    negatives. The sole unselected nocobactin NA adds four companion rows/49 fields,
    not an additional selected target.
  snapshot_sha256: e54bca095c7afe77356b58cd19caa713350474bafd04f350dfa71a6d25f1e607
- evidence_id: support-2830-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-target-input-plan-001.json
  locator: /records/9; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Accepted 459-placement/54-path plan; this owner has 44 actual captured
    inputs.
  snapshot_sha256: 3aed42cc3b6e67821797e83390bcc2ebfb1edaa180175e1241638e06f20d40b8
- evidence_id: support-2830-planaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283/root-current283-source-plan-acceptance-001.json
  locator: /status; /accepted; /plan
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: ROOT accepted the original source plan.
  snapshot_sha256: 69d4faf5b6fca585ddc91342e8a5fd1aaaa5da756822ae0f934156d8457ea1e7
- evidence_id: support-2830-notes
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /curation
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Current disjoint BGC16 plus Support21 named source rows; Native and overlapping
    ROOT readings add zero primary-row credit.
  snapshot_sha256: 52c35704f15d7aaa17553f434fa27e18f0334cd745f0d963fc8fd8b5b937eafb
- evidence_id: support-2830-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283/intakes-001/2830-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Actual canonical intake fixes current input hashes, generated target and
    maintained ownership.
  snapshot_sha256: 05ee6f4bb22d2105595b7caf049b15176b88cf86091d4101f77a5cf5f735d5db
- evidence_id: support-2830-intakeaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283/root-current283-intakes-acceptance-001.json
  locator: /status; /accepted; /summary
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: All ten original intakes exited zero with empty stderr; no reruns.
  snapshot_sha256: 4015a5a5e7ef8c1991cf05d677cea3ce3445b046da29c3b61e410cc6718f592b
- evidence_id: support-2830-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles; /records/9/inchi; /records/9/comparisons; /records/9/atom_correspondence;
    /records/9/literal_InChI_layers; /records/9/formula_comparison_scope
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Both neutral single-component forms have 32 atoms and 36 bonds, formula
    C28H37NO3, matching canonical isomeric/nonisomeric strings and the declared normalized
    InChI/key. Five reported ring rows have sizes 5,5,6,6,6, including the fused aromatic
    indole and adjoining carbocyclic scaffold. A neutral carboxylic acid and an alcohol
    are retained; no ester or amide motif is reported by the strict predicates. Both
    canonical SMILES comparisons agree and the limited 32-atom map is complete; full_graph_identity_established
    nevertheless remains false.
  snapshot_sha256: 7ed86891cefb3aaf5d481b53685d9add53080894be61adf37776456c6fd8717a
- evidence_id: support-2830-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles/computed/atoms; /records/9/smiles/computed/bonds; /records/9/smiles/computed/potential_stereo;
    /records/9/inchi/computed/atoms; /records/9/inchi/computed/bonds; /records/9/inchi/computed/potential_stereo
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Both forms retain six specified tetrahedral centres and one specified alkene.
    The saved bond enums are STEREOE even though the potential-stereo descriptor is
    Bond_Cis, a different local-control frame. Neither descriptor is substituted for
    the other; no new experimental absolute configuration is claimed.
  snapshot_sha256: 7ed86891cefb3aaf5d481b53685d9add53080894be61adf37776456c6fd8717a
- evidence_id: support-2830-motifs
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles/computed/atoms; /records/9/smiles/computed/bonds; /records/9/smiles/computed/rings;
    /records/9/smiles/computed/motifs; /records/9/inchi/computed/atoms; /records/9/inchi/computed/bonds;
    /records/9/inchi/computed/rings; /records/9/inchi/computed/motifs
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: SMILES acid carbon 26 has double-bond oxygen 28 and single-bond OH 27;
    alcohol oxygen 18 is attached to stereocentre 17. The E alkene is bond 23 between
    atoms 23 and 24. InChI counterparts are acid carbon 24/O30/O31, alcohol O29 on
    carbon 22, and E bond 9 (7=16). The five-ring indole includes [nH] and the six-ring
    aromatic system; the remaining rings are carbocyclic. Ring/motif predicates do
    not assign natural biosynthetic steps.
  snapshot_sha256: 7ed86891cefb3aaf5d481b53685d9add53080894be61adf37776456c6fd8717a
- evidence_id: support-2830-molecularreading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/support-prep/support-current283-last-five-molecular-intake-reading-001.json
  locator: /records/4; /counts; /interpretations/2830; /warnings
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Personally read complete ten saved forms:410 atoms/422 bonds/22 ring rows/44
    potential-stereo entries. No new parse.
  snapshot_sha256: 7040591aaa6a77348a62b325ec740a242b3198cd349ccb0a6bdde32e8ff7b788
- evidence_id: support-2830-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /retries; /stderr
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: One original diagnostic execution exited zero with no retry.
  snapshot_sha256: e26bc1063548409d289427344212b21df85a38517d856490012ce5ba1943a8e6
- evidence_id: support-2830-diagaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /scientific_limits
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: ROOT accepted the original stored-form diagnostic; scientific interpretation
    remains bounded.
  snapshot_sha256: 95ebe92297007daee981790f68c1da647d148ec840bda2f42ef42255260c397b
- evidence_id: support-2830-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283/chemistry-local/diagnostic-original-001.stderr
  locator: complete two original warning lines
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Two original Omitted undefined stereo warning lines remain globally unassigned;
    neither is attributed to an individual owner.
  snapshot_sha256: 7919e4bc3330c7493db648e7b21f0edec2119e76bb68020d03a35053e86e1826
- evidence_id: support-2830-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/native-prep/native-current283-cached-taxonomy-reading-001.json
  locator: /context_interpretations/10; /physical_negative_query_scopes/10; /whole_stanzas
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Keep Hypoxylon pulicicidum (1243767), BGC0001706:1 and MG182145.1:42700–71644
    source producer/locus separate from LOTUS genus Nodulisporium (96453) occurrence
    at DOI:10.1021/NP0498455. Preserve SOURCE_ASSERTION/CLUSTER_UNSTATED and entry-level
    PMID:29283570. The cache supplies no lineage or synonym assertion connecting these
    two labels; no producer/occurrence identity repair follows. All saved source taxon
    IDs have complete local cache stanzas; no forward merge or nonorganism match is
    retained for this context. Cached labels/synonyms do not establish rank, lineage,
    freshness, production or strain equivalence.
  snapshot_sha256: f4d935b240d6bca39c28c5a89623f402833d1b1444528486fcb2e7091098b7da
- evidence_id: support-2830-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/native-prep/native-current283-implemented-curation-scan-001.json
  locator: /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows;
    /interpretation
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Nine substantive tables retain no exact applicable maintained correction;
    lexical matches and unrelated assay exclusions do not transfer.
  snapshot_sha256: f88a39131d43dda2d9aade5bb787ca1efc7b6e43803fb92077082a2711ccbe5b
  search_scope: Native attributed complete nine-table/3422-row scan with exact owner/source
    compound/BGC/full-key/occurrence/assay predicates; no new query or universal absence.
- evidence_id: support-2830-producerpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: complete method grading table
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: SOURCE_ASSERTION producer and CLUSTER_UNSTATED locus grades answer distinct
    questions.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2830-stereopolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142-173 structure_fields; atom-centre predicate lines 165-172
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: stereo_complete derives from FindMolChiralCenters and unknown atom tags;
    it does not assert complete E/Z or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2830-filingpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295-306 choose_pathway
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: One supported normalized pathway chooses filing; multiple, none or unsupported
    results retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2830-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch283/root-current283-five-gates-acceptance-001.json
  locator: /five_exit_codes; /selected_queue_rows; /unavailable_required_gates; /all_native_gates_passed
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: All five local gates pass; full QC/OAK remain unavailable and all_native_gates_passed
    is false. Queue leads do not independently establish defects.
  snapshot_sha256: 0a6d1f5fcc92f78a80056efc171208bdb6bb18e15143bbc29d352933d0ef2fe4
- evidence_id: support-2830-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch283/owner-capture-DATA-001.json
  locator: /records/9/owner_document/curation_history; /records/9/owner_document/source_concepts
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: PMID:29283570 is ENTRY-level MIBiG evidence; DOI:10.1021/NP0498455 is a
    separate occurrence pointer. Distinct pointers do not establish publication independence
    without reading their contents. The two import-history events document processing,
    not new experiments.
  snapshot_sha256: ccb2947ae508c4adfbae4d738ad2378acad9430c4244387b20f044274f1f2f32
- evidence_id: support-2830-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-target-input-plan-001.json
  locator: /records/9/complete_root_keys; /records/9/declared_mechanism_roots_literal;
    /records/9/component_paths; /records/9/complete_raw_mechanism_sections
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: The complete selected owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway,
    molecular_targets, bioactivities, bioactivity_summary, related_records or component
    root. No maintained reader is applicable. This bounded record absence does not
    assert absent biology or missing upstream experimental mechanisms.
  snapshot_sha256: 3aed42cc3b6e67821797e83390bcc2ebfb1edaa180175e1241638e06f20d40b8
- evidence_id: support-2830-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete saved mibig_compounds query frame with 1 matched placements.
  snapshot_sha256: 1d18b3e2264cb5fb227a3d05799d525013d9a51bf14ab0a9989a97da516149d0
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and exact query "FYZYVTHTMPXJHJ-UOOBVZAFSA-N" only; no replay or universal absence.
- evidence_id: support-2830-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical line 2027, raw UTF-8 row SHA-256 f4d97b8e43404f45ab05b2844e4cad3e8aca605d9026f1818d690a7ab2a0747c
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: The selected owner naturalproductmech:mibig-094f8c95c8 is active MIBiG
    BGC0001706 version 3 compound index 1 with full key FYZYVTHTMPXJHJ-UOOBVZAFSA-N
    and retained NPAtlas NPA09237. Its explicit-H source spelling and normalized local
    comparison identify the retained representation without independently proving
    the natural isolated compound. Hypoxylon pulicicidum, NCBITaxon:1243767, is the
    MIBiG SOURCE_ASSERTION producer; this remains distinct from a LOTUS Nodulisporium
    occurrence. MG182145.1:42700–71644 remains CLUSTER_UNSTATED with blank locus methods.
    BGC0001706 version 3 has questionable quality and unknown completeness. The lowercase
    terpene BGC class and Unknown subclass are separate retained fields.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2830-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete saved chebi_structures query frame with 0 matched placements.
  snapshot_sha256: 1d18b3e2264cb5fb227a3d05799d525013d9a51bf14ab0a9989a97da516149d0
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and exact query "FYZYVTHTMPXJHJ-UOOBVZAFSA-N" only; no replay or universal absence.
- evidence_id: support-2830-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete saved lotus_occurrences query frame with 1 matched placements.
  snapshot_sha256: 1d18b3e2264cb5fb227a3d05799d525013d9a51bf14ab0a9989a97da516149d0
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and exact query "FYZYVTHTMPXJHJ-UOOBVZAFSA-N" only; no replay or universal absence.
- evidence_id: support-2830-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical line 2059, raw UTF-8 row SHA-256 d5babaa768f0dc3cd808a3aabb5b3e15bedef26a5f0590fa2fa6f4a2b038ca5e
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: LOTUS reports Nodulisporium/NCBITaxon:96453. Cached labels give no lineage
    or synonym assertion equating it with Hypoxylon pulicicidum; no producer/occurrence
    identity repair follows. This owner has no direct companion under the current
    exact predicate.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2830-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences query frame with 0 matched placements.
  snapshot_sha256: 1d18b3e2264cb5fb227a3d05799d525013d9a51bf14ab0a9989a97da516149d0
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and exact query "FYZYVTHTMPXJHJ-UOOBVZAFSA-N" only; no replay or universal absence.
- evidence_id: support-2830-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete saved npclassifier query frame with 1 matched placements.
  snapshot_sha256: 1d18b3e2264cb5fb227a3d05799d525013d9a51bf14ab0a9989a97da516149d0
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and exact query "FYZYVTHTMPXJHJ-UOOBVZAFSA-N" only; no replay or universal absence.
- evidence_id: support-2830-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical line 633, raw UTF-8 row SHA-256 c44da786d5ce4430ed2c45d708d979b32491130a3f5422c0718f3a5f9bf4f321
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: NPClassifier predicts Alkaloids plus Terpenoids, Tryptophan alkaloids and
    Indole-Diterpenoid alkaloids (Penitrems), with is_glycoside:false. The saved indole-containing
    fused scaffold is compatible with descriptive alkaloid/terpenoid language, not
    proof of a biosynthetic route. Two pathway results correctly leave filing UNCLASSIFIED;
    compound_classes is blank and NPAtlas is not identity validation.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2830-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete saved pubchem_bioassay query frame with 0 matched placements.
  snapshot_sha256: 1d18b3e2264cb5fb227a3d05799d525013d9a51bf14ab0a9989a97da516149d0
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and exact query "FYZYVTHTMPXJHJ-UOOBVZAFSA-N" only; no replay or universal absence.
- evidence_id: support-2830-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete saved bindingdb_targets query frame with 0 matched placements.
  snapshot_sha256: 1d18b3e2264cb5fb227a3d05799d525013d9a51bf14ab0a9989a97da516149d0
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and exact query "FYZYVTHTMPXJHJ-UOOBVZAFSA-N" only; no replay or universal absence.
- evidence_id: support-2830-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys query frame with 0 matched placements.
  snapshot_sha256: 1d18b3e2264cb5fb227a3d05799d525013d9a51bf14ab0a9989a97da516149d0
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and exact query "FYZYVTHTMPXJHJ-UOOBVZAFSA-N" only; no replay or universal absence.
- evidence_id: support-2830-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch283-tentative/bgc-prep/bgc-conditional283-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T04:42:03.315542Z'
  support: supports
  summary: Complete saved chebi_origins query frame with 0 matched placements.
  snapshot_sha256: 1d18b3e2264cb5fb227a3d05799d525013d9a51bf14ab0a9989a97da516149d0
  search_scope: Retained uncapped predicate exact chebi_id from exact full-key structure
    rows and exact query [] only; no replay or universal absence.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-283/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-283/native-current283-five-gates-execution-001.json
  accessed_at: '2026-11-07T04:14:42.395581Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 0d5e7e0aec5d12f7fe9a5da98b4ac41e85b98e6f65494213eb95ae5024b91c53
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-283/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-283/native-current283-five-gates-execution-001.json
  accessed_at: '2026-11-07T04:15:08.182267Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: ccf5b47a6b735c1f7f452ef0b2b19cb58ddf8b8cba753cf35420ea9720fab51e
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-283/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-283/native-current283-five-gates-execution-001.json
  accessed_at: '2026-11-07T04:15:28.643670Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-283/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-283/native-current283-five-gates-execution-001.json
  accessed_at: '2026-11-07T04:16:03.827826Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-283/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-283/native-current283-five-gates-execution-001.json
  accessed_at: '2026-11-07T04:16:16.631042Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 5b6cc7afce02e3857066e6a6bb8a886f7db89ee387d7e8f4643513222e411663
assessments:
- assessment_id: support-2830-identity-assessment
  area: identity
  topic: Exact retained compound grounding
  summary: The selected owner naturalproductmech:mibig-094f8c95c8 is active MIBiG
    BGC0001706 version 3 compound index 1 with full key FYZYVTHTMPXJHJ-UOOBVZAFSA-N
    and retained NPAtlas NPA09237. Its explicit-H source spelling and normalized local
    comparison identify the retained representation without independently proving
    the natural isolated compound.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  evidence_ids:
  - support-2830-owner
  - support-2830-capture
  - support-2830-source
  - support-2830-intake
  - support-2830-curation
  - support-2830-plan
  - support-2830-table-mibig_compounds
  - support-2830-table-lotus_occurrences
  - support-2830-table-npclassifier
  dimensions:
  - name: standard_inchi_key
    definition: Complete source key, not label-only identity.
    value: FYZYVTHTMPXJHJ-UOOBVZAFSA-N
    evidence_ids:
    - support-2830-owner
    - support-2830-capture
    - support-2830-source
    - support-2830-intake
    - support-2830-curation
    - support-2830-plan
    - support-2830-table-mibig_compounds
    - support-2830-table-lotus_occurrences
    - support-2830-table-npclassifier
  - name: grounding_scope
    definition: Retained identity versus independently established natural identity.
    value: The selected owner naturalproductmech:mibig-094f8c95c8 is active MIBiG
      BGC0001706 version 3 compound index 1 with full key FYZYVTHTMPXJHJ-UOOBVZAFSA-N
      and retained NPAtlas NPA09237. Its explicit-H source spelling and normalized
      local comparison identify the retained representation without independently
      proving the natural isolated compound.
    evidence_ids:
    - support-2830-owner
    - support-2830-capture
    - support-2830-source
    - support-2830-intake
    - support-2830-curation
    - support-2830-plan
    - support-2830-table-mibig_compounds
    - support-2830-table-lotus_occurrences
    - support-2830-table-npclassifier
- assessment_id: support-2830-representation-assessment
  area: representation
  topic: Saved molecular forms and stereochemical scope
  summary: Both neutral single-component forms have 32 atoms and 36 bonds, formula
    C28H37NO3, matching canonical isomeric/nonisomeric strings and the declared normalized
    InChI/key. Five reported ring rows have sizes 5,5,6,6,6, including the fused aromatic
    indole and adjoining carbocyclic scaffold. A neutral carboxylic acid and an alcohol
    are retained; no ester or amide motif is reported by the strict predicates. SMILES
    acid carbon 26 has double-bond oxygen 28 and single-bond OH 27; alcohol oxygen
    18 is attached to stereocentre 17. The E alkene is bond 23 between atoms 23 and
    24. InChI counterparts are acid carbon 24/O30/O31, alcohol O29 on carbon 22, and
    E bond 9 (7=16). The five-ring indole includes [nH] and the six-ring aromatic
    system; the remaining rings are carbocyclic. Ring/motif predicates do not assign
    natural biosynthetic steps. Both canonical SMILES comparisons agree and the limited
    32-atom map is complete; full_graph_identity_established nevertheless remains
    false. Normalized identifiers, formula agreement and local parsing do not establish
    independent full graph identity, natural-sample identity, experimental absolute
    stereochemistry or primary biological validation.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  evidence_ids:
  - support-2830-data
  - support-2830-stereo
  - support-2830-motifs
  - support-2830-molecularreading
  - support-2830-execution
  - support-2830-diagaccept
  - support-2830-stereopolicy
  dimensions:
  - name: stereochemistry_scope
    definition: Saved specified centres and representation-dependent bond candidates.
    value: Both forms retain six specified tetrahedral centres and one specified alkene.
      The saved bond enums are STEREOE even though the potential-stereo descriptor
      is Bond_Cis, a different local-control frame. Neither descriptor is substituted
      for the other; no new experimental absolute configuration is claimed.
    evidence_ids:
    - support-2830-data
    - support-2830-stereo
    - support-2830-motifs
    - support-2830-molecularreading
    - support-2830-execution
    - support-2830-diagaccept
    - support-2830-stereopolicy
  - name: representation_correspondence
    definition: Bounded saved comparison, not full identity.
    value: Both canonical SMILES comparisons agree and the limited 32-atom map is
      complete; full_graph_identity_established nevertheless remains false. Normalized
      identifiers, formula agreement and local parsing do not establish independent
      full graph identity, natural-sample identity, experimental absolute stereochemistry
      or primary biological validation.
    evidence_ids:
    - support-2830-data
    - support-2830-stereo
    - support-2830-motifs
    - support-2830-molecularreading
    - support-2830-execution
    - support-2830-diagaccept
    - support-2830-stereopolicy
- assessment_id: support-2830-provenance-assessment
  area: provenance
  topic: Compound-specific producer, locus and taxon
  summary: Hypoxylon pulicicidum, NCBITaxon:1243767, is the MIBiG SOURCE_ASSERTION
    producer; this remains distinct from a LOTUS Nodulisporium occurrence. MG182145.1:42700–71644
    remains CLUSTER_UNSTATED with blank locus methods. BGC0001706 version 3 has questionable
    quality and unknown completeness. The lowercase terpene BGC class and Unknown
    subclass are separate retained fields.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  evidence_ids:
  - support-2830-source
  - support-2830-capture
  - support-2830-taxonomy
  - support-2830-curation
  - support-2830-producerpolicy
  - support-2830-plan
  - support-2830-table-mibig_compounds
  - support-2830-table-lotus_occurrences
  - support-2830-table-npclassifier
  dimensions:
  - name: taxon_scope
    definition: Cached names do not resolve current rank/lineage or strain equivalence.
    value: Keep Hypoxylon pulicicidum (1243767), BGC0001706:1 and MG182145.1:42700–71644
      source producer/locus separate from LOTUS genus Nodulisporium (96453) occurrence
      at DOI:10.1021/NP0498455. Preserve SOURCE_ASSERTION/CLUSTER_UNSTATED and entry-level
      PMID:29283570. The cache supplies no lineage or synonym assertion connecting
      these two labels; no producer/occurrence identity repair follows. All saved
      source taxon IDs have complete local cache stanzas; no forward merge or nonorganism
      match is retained for this context. Cached labels/synonyms do not establish
      rank, lineage, freshness, production or strain equivalence.
    evidence_ids:
    - support-2830-source
    - support-2830-capture
    - support-2830-taxonomy
    - support-2830-curation
    - support-2830-producerpolicy
    - support-2830-plan
    - support-2830-table-mibig_compounds
    - support-2830-table-lotus_occurrences
    - support-2830-table-npclassifier
  - name: producer_evidence
    definition: Producer grade remains separate from locus evidence.
    value: Hypoxylon pulicicidum, NCBITaxon:1243767, is the MIBiG SOURCE_ASSERTION
      producer; this remains distinct from a LOTUS Nodulisporium occurrence.
    evidence_ids:
    - support-2830-source
    - support-2830-capture
    - support-2830-taxonomy
    - support-2830-curation
    - support-2830-producerpolicy
    - support-2830-plan
    - support-2830-table-mibig_compounds
    - support-2830-table-lotus_occurrences
    - support-2830-table-npclassifier
  - name: locus_evidence
    definition: Exact source version, endpoints and methods delimit evidence.
    value: MG182145.1:42700–71644 remains CLUSTER_UNSTATED with blank locus methods.
      BGC0001706 version 3 has questionable quality and unknown completeness. The
      lowercase terpene BGC class and Unknown subclass are separate retained fields.
    evidence_ids:
    - support-2830-source
    - support-2830-capture
    - support-2830-taxonomy
    - support-2830-curation
    - support-2830-producerpolicy
    - support-2830-plan
    - support-2830-table-mibig_compounds
    - support-2830-table-lotus_occurrences
    - support-2830-table-npclassifier
- assessment_id: support-2830-citations-assessment
  area: evidence
  topic: Citation grain and retained history
  summary: PMID:29283570 is ENTRY-level MIBiG evidence; DOI:10.1021/NP0498455 is a
    separate occurrence pointer. Distinct pointers do not establish publication independence
    without reading their contents. The two import-history events document processing,
    not new experiments.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  evidence_ids:
  - support-2830-owner
  - support-2830-source
  - support-2830-capture
  - support-2830-history
  - support-2830-table-mibig_compounds
  - support-2830-table-lotus_occurrences
  - support-2830-table-npclassifier
  dimensions:
  - name: citation_scope
    definition: Source pointers and imports do not supply independent primary proof.
    value: PMID:29283570 is ENTRY-level MIBiG evidence; DOI:10.1021/NP0498455 is a
      separate occurrence pointer. Distinct pointers do not establish publication
      independence without reading their contents. The two import-history events document
      processing, not new experiments.
    evidence_ids:
    - support-2830-owner
    - support-2830-source
    - support-2830-capture
    - support-2830-history
    - support-2830-table-mibig_compounds
    - support-2830-table-lotus_occurrences
    - support-2830-table-npclassifier
- assessment_id: support-2830-occurrence-assay-assessment
  area: evidence
  topic: Occurrence and assay limits
  summary: LOTUS reports Nodulisporium/NCBITaxon:96453. Cached labels give no lineage
    or synonym assertion equating it with Hypoxylon pulicicidum; no producer/occurrence
    identity repair follows. This owner has no direct companion under the current
    exact predicate. Saved ChEBI, CyanoMetDB, PubChem, BindingDB, AntibioticMech and
    origins frames are negative; no actual AID, blank assay sentinel or measured target
    is established. Negative saved queries are not universal biological absence.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  evidence_ids:
  - support-2830-source
  - support-2830-taxonomy
  - support-2830-curation
  - support-2830-plan
  - support-2830-query-mibig_compounds
  - support-2830-query-chebi_structures
  - support-2830-query-lotus_occurrences
  - support-2830-query-cyanometdb_occurrences
  - support-2830-query-npclassifier
  - support-2830-query-pubchem_bioassay
  - support-2830-query-bindingdb_targets
  - support-2830-query-antibioticmech_inchikeys
  - support-2830-query-chebi_origins
  - support-2830-table-mibig_compounds
  - support-2830-table-lotus_occurrences
  - support-2830-table-npclassifier
  dimensions:
  - name: occurrence_scope
    definition: Occurrence and literal source fields do not establish causal production.
    value: LOTUS reports Nodulisporium/NCBITaxon:96453. Cached labels give no lineage
      or synonym assertion equating it with Hypoxylon pulicicidum; no producer/occurrence
      identity repair follows. This owner has no direct companion under the current
      exact predicate.
    evidence_ids:
    - support-2830-source
    - support-2830-taxonomy
    - support-2830-curation
    - support-2830-plan
    - support-2830-query-mibig_compounds
    - support-2830-query-chebi_structures
    - support-2830-query-lotus_occurrences
    - support-2830-query-cyanometdb_occurrences
    - support-2830-query-npclassifier
    - support-2830-query-pubchem_bioassay
    - support-2830-query-bindingdb_targets
    - support-2830-query-antibioticmech_inchikeys
    - support-2830-query-chebi_origins
    - support-2830-table-mibig_compounds
    - support-2830-table-lotus_occurrences
    - support-2830-table-npclassifier
  - name: assay_target_scope
    definition: Retained negative queries are not inactivity experiments.
    value: Saved ChEBI, CyanoMetDB, PubChem, BindingDB, AntibioticMech and origins
      frames are negative; no actual AID, blank assay sentinel or measured target
      is established. Negative saved queries are not universal biological absence.
    evidence_ids:
    - support-2830-source
    - support-2830-taxonomy
    - support-2830-curation
    - support-2830-plan
    - support-2830-query-mibig_compounds
    - support-2830-query-chebi_structures
    - support-2830-query-lotus_occurrences
    - support-2830-query-cyanometdb_occurrences
    - support-2830-query-npclassifier
    - support-2830-query-pubchem_bioassay
    - support-2830-query-bindingdb_targets
    - support-2830-query-antibioticmech_inchikeys
    - support-2830-query-chebi_origins
    - support-2830-table-mibig_compounds
    - support-2830-table-lotus_occurrences
    - support-2830-table-npclassifier
- assessment_id: support-2830-classification-assessment
  area: consistency
  topic: Source classes, model labels and filing
  summary: NPClassifier predicts Alkaloids plus Terpenoids, Tryptophan alkaloids and
    Indole-Diterpenoid alkaloids (Penitrems), with is_glycoside:false. The saved indole-containing
    fused scaffold is compatible with descriptive alkaloid/terpenoid language, not
    proof of a biosynthetic route. Two pathway results correctly leave filing UNCLASSIFIED;
    compound_classes is blank and NPAtlas is not identity validation.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  evidence_ids:
  - support-2830-source
  - support-2830-owner
  - support-2830-motifs
  - support-2830-filingpolicy
  - support-2830-gates
  - support-2830-table-mibig_compounds
  - support-2830-table-lotus_occurrences
  - support-2830-table-npclassifier
  dimensions:
  - name: classification_applicability
    definition: Source/model/topology/biochemical evidence remain distinct.
    value: NPClassifier predicts Alkaloids plus Terpenoids, Tryptophan alkaloids and
      Indole-Diterpenoid alkaloids (Penitrems), with is_glycoside:false. The saved
      indole-containing fused scaffold is compatible with descriptive alkaloid/terpenoid
      language, not proof of a biosynthetic route. Two pathway results correctly leave
      filing UNCLASSIFIED; compound_classes is blank and NPAtlas is not identity validation.
    evidence_ids:
    - support-2830-source
    - support-2830-owner
    - support-2830-motifs
    - support-2830-filingpolicy
    - support-2830-gates
    - support-2830-table-mibig_compounds
    - support-2830-table-lotus_occurrences
    - support-2830-table-npclassifier
- assessment_id: support-2830-completion-assessment
  area: completeness
  topic: Earned work and unavailable authority
  summary: Complete selected owner, actual source/intake and both saved molecular
    forms were read. The complete selected owner has no causal_graphs, causal_graph_refs,
    biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary, related_records
    or component root. No maintained reader is applicable. This bounded record absence
    does not assert absent biology or missing upstream experimental mechanisms. No
    material local defect was established within this bounded evidence. Five local
    gates pass; full QC, complete OAK and fresh primary/external verification remain
    unavailable. Completion is partial and native SEEDED status is unchanged.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-094f8c95c8
  evidence_ids:
  - support-2830-intake
  - support-2830-intakeaccept
  - support-2830-plan
  - support-2830-planaccept
  - support-2830-notes
  - support-2830-gates
  - support-2830-data
  - support-2830-diagaccept
  - support-2830-scope
  dimensions:
  - name: review_completion
    definition: Local review does not substitute for unavailable authority or promote
      native status.
    value: Complete selected owner, actual source/intake and both saved molecular
      forms were read. The complete selected owner has no causal_graphs, causal_graph_refs,
      biosynthetic_pathway, molecular_targets, bioactivities, bioactivity_summary,
      related_records or component root. No maintained reader is applicable. This
      bounded record absence does not assert absent biology or missing upstream experimental
      mechanisms. No material local defect was established within this bounded evidence.
      Five local gates pass; full QC, complete OAK and fresh primary/external verification
      remain unavailable. Completion is partial and native SEEDED status is unchanged.
    evidence_ids:
    - support-2830-intake
    - support-2830-intakeaccept
    - support-2830-plan
    - support-2830-planaccept
    - support-2830-notes
    - support-2830-gates
    - support-2830-data
    - support-2830-diagaccept
    - support-2830-scope
findings: []
actions: []
limitations:
- Normalized identifiers, formula agreement and local parsing do not establish independent
  full graph identity, natural-sample identity, experimental absolute stereochemistry
  or primary biological validation.
- Both canonical SMILES comparisons agree and the limited 32-atom map is complete;
  full_graph_identity_established nevertheless remains false. Both forms retain six
  specified tetrahedral centres and one specified alkene. The saved bond enums are
  STEREOE even though the potential-stereo descriptor is Bond_Cis, a different local-control
  frame. Neither descriptor is substituted for the other; no new experimental absolute
  configuration is claimed.
- Two original Omitted undefined stereo warning lines remain globally unassigned;
  neither is attributed to an individual owner.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK
  remain unavailable; source/database claims retain their exact grain and authority.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh current 283 evidence and judgments; prior batches provide interface logic
  only.
- No source record, native status or history was changed; no query, molecular parse,
  target invocation or outbound request occurred in this lane.
- ROOT appends five actual local gate checks and three required unavailable checks.
  No maintained-reader check is applicable; unselected companions remain context only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-283
```
