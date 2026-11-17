# Local evidence review: SNF4435D

- Review: 20261104T124233Z-snf4435d
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T11:41:40.736229Z
- Finished UTC: 2026-11-04T12:42:33.168031Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

SNF4435D has internally consistent retained structure and identifier correspondence while remaining distinct from SNF4435C. The versioned Terpenoids filing merits a bounded applicability concern alongside the preserved PKS source class. Producer, demonstrated locus and occurrence claims retain separate evidence grades. No supported source-edit finding is established; this is a qualified partial review.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2397; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-39f27be5a3 | data/natural_products/terpenoids/snf4435d.yaml | generated | SNF4435D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-39f27be5a3 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-39f27be5a3 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-39f27be5a3 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-39f27be5a3 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-39f27be5a3 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-39f27be5a3 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-39f27be5a3 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-39f27be5a3 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained structure and identifier correspondence

identity: supported. Targets: naturalproductmech:mibig-39f27be5a3.

SNF4435D retains the minted identifier naturalproductmech:mibig-39f27be5a3, full key DXCYJJKWPZZHNZ-KAKVGEDNSA-N and MIBiG BGC0000110 version 5 source concept. Both accepted stored-form diagnostics reproduce that full key. The retained no-3-star-ChEBI-match rationale is a bounded local-inventory result, not a new external absence claim. npatlas:NPA01579 remains an unrefreshed cross-reference. SNF4435C shares the connectivity block but has a different stereochemical key; the labels and complete forms are not interchangeable.

### Stored topology and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-39f27be5a3.

Both forms are neutral C28H31NO6 with 35 heavy atoms and 39 bonds. All ten comparison flags are true and the chirality-aware map spans all atoms; full_graph_identity_established remains false. Five tetrahedral centers are specified with no unspecified candidate tetrahedral center. Saved SMILES atom 22 is S, versus R in SNF4435C, while the remaining corresponding tetrahedral CIP labels agree. The tables retain a nitro group as charge-separated N/O with zero aggregate charge, five ring lists including a five-membered cyclic ether and a four-carbon ring, and one carbonyl. This supports internal representation consistency, not an independently verified natural stereoisomer. The four global charge warnings cannot be assigned to this owner.

### Producer and demonstrated locus remain distinct

provenance: supported. Targets: naturalproductmech:mibig-39f27be5a3.

MIBiG BGC0000110 version 5 retains Streptomyces orinoci, NCBITaxon:67339, as a SOURCE_ASSERTION producer. The separate AM778535.1 locus is CLUSTER_DEMONSTRATED through heterologous expression; no locus coordinates or strain are supplied in this retained row. That locus grade does not upgrade the native taxon claim or make the LOTUS Streptomyces spectabilis occurrences into producer evidence.

### Historical citation and companion scope

evidence: supported. Targets: naturalproductmech:mibig-39f27be5a3.

PMID:17763486 is retained as MIBiG entry-level DATABASE_ASSERTION provenance. Active status, questionable quality and complete source completeness are source-entry metadata, not independent proof for the precise stereoisomer. The distinct full-key same-BGC companions Orinocin and Spectinabilin supply locus context only; their labels, model classes, occurrence rows and activity claims are not transferred. No primary text or external identity record was retrieved for this review.

### Occurrence and activity boundaries

evidence: supported. Targets: naturalproductmech:mibig-39f27be5a3.

The selected full-key inventory contains one LOTUS row for Streptomyces spectabilis, NCBITaxon:68270, citing DOI:10.7164/ANTIBIOTICS.54.541. These are detection/isolation assertions, separately retained from the MIBiG producer; shared references do not establish publication independence or strain equivalence. No actual PubChem assay, BindingDB target, CyanometDB or AntibioticMech row is retained for this selected key, and the owner has no bioactivity or molecular-target root. These bounded negatives do not establish inactivity or absence of published activity.

### Versioned filing applicability

consistency: concern. Targets: naturalproductmech:mibig-39f27be5a3.

NPClassifier version npclassifier.gnps2.org@2026-09-07 supplies Terpenoids with empty subclass and superclass lists, whereas BGC0000110 separately asserts PKS. The nitroaryl/oxygenated heterocyclic structure and the source PKS context make the Terpenoids model filing an applicability question, not an established ingestion error or authority to overwrite the prediction. The complete topology has no separate sugar residue or saturated C5O candidate cycle, and its internal ether/methoxy bridges are compatible with the retained is_glycoside false. Neither a ring count nor a shared locus determines biosynthetic class by itself.

### Review completion

completeness: unknown. Targets: naturalproductmech:mibig-39f27be5a3.

The complete owner/history, actual canonical intake, all assigned source payloads and both accepted saved molecular forms were personally read. No causal_graphs, causal_graph_refs, biosynthetic_pathway or molecular_targets root is present, so no selected maintained-reader call applies. Full QC, complete OAK authority coverage and fresh external verification remain unavailable. No supported source-edit finding or action is established; this remains a qualified partial review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2397-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/snf4435d.yaml; Whole current plaintext and complete curation_history | supports | Complete owner and 2 history events personally read; unchanged source record. |
| support-2397-capture | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/6/owner_document | supports | Complete accepted captured owner establishes all present and absent roots. No causal graph, component, biosynthetic pathway or molecular target is declared; no selected reader applies. |
| support-2397-grounding-owner | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/6/owner_document/identifier; /records/6/owner_document/label; /records/6/owner_document/chemical_structure; /records/6/owner_document/source_concepts; /records/6/owner_document/xrefs; /records/6/owner_document/grounding_status; /records/6/owner_document/grounding_notes | supports | Retained identifier/key, stored structure, source concepts and grounding status; optional historical notes and definitions remain limited to the selected present fields. No fresh natural-identity proof. |
| support-2397-origin-owner | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters; /records/6/owner_document/producer_taxon_groups | supports | Complete producer and locus assertions with their independent grades and historical citation roles. Every retained version, coordinate and method is preserved without transferring support between claims. |
| support-2397-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/6/owner_document | supports | Whole owner establishes retained occurrence, related-corpus and activity annotations and the absence of a molecular target; no broader biological absence or activity transfer is inferred. |
| support-2397-classification-owner | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/6/owner_document/np_pathway; /records/6/owner_document/np_classification; /records/6/owner_document/bgc_class; /records/6/owner_document/biosynthesis_origin | supports | Versioned NPClassifier predictions, glycoside flag and retained source class are distinct assertions; no automatic reclassification. |
| support-2397-direct-contexts | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-target-input-plan-001.json; /records/6/proposed_companion_paths; /records/6/direct_companion_predicates; /records/6/additional_context_roles | context_only | Exact one-hop context predicates and input roles; companion identity, activity and producer claims do not transfer. |
| support-2397-intake | /private/tmp/npm-review-work/shared-next-batch240/intakes/2397-inspect-001.json; /targets; /source | supports | Original canonical intake: one target, exact maintained/generated ownership paths and immutable source-input map. |
| support-2397-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch240/root-intake-acceptance-001.json; /status; /accepted; /summary; /source_placements; /source_paths | supports | ROOT accepts all ten original intakes and exact source alignment. |
| support-2397-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch240/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /scope | supports | Original local extraction is accepted; source assertions remain retained evidence, not fresh verification. |
| support-2397-plan | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-target-input-plan-001.json; /records/6/proposed_input_paths; /records/6/proposed_input_count | supports | Actual immutable input plan reconciled to this canonical intake. |
| support-2397-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch240/root-source-plan-acceptance-001.json; /status; /accepted; /plan; /verification | supports | ROOT accepts the original complete local plan and exact input-map transformations. |
| support-2397-source-reading | /private/tmp/npm-review-work/shared-next-batch240-tentative/support-prep/support-current240-source-reading-001.json; /division; /reading; /contexts; /source_cautions | supports | Support personally read 11 assigned contexts, 99 query frames and 42 rows; selected last-five subset is 45 frames and 26 rows. BGC companion and Native cache/curation readings retain their named attribution. |
| support-2397-molecular-reading | /private/tmp/npm-review-work/shared-next-batch240-tentative/support-prep/support-current240-last-five-molecular-reading-001.json; /read_scope; /representation; /records; /totals; /read_caveats | supports | Support complete paired-form table reading is attributed by actual output chunks; no additional molecular parse. |
| support-2397-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch240-tentative/native-prep/native-current240-cached-taxonomy-reading-001.json; /scope; /counts; /requested_ids; /whole_stanza_locations; /readings; /cautions | context_only | Native personally read all 22 complete saved stanzas and their physical locations; no unmatched ID or forward route is retained. Cached labels do not constitute current external taxonomy verification. |
| support-2397-curation-scope | /private/tmp/npm-review-work/shared-next-batch240-tentative/native-prep/native-current240-implemented-curation-scan-001.json; /scope; /ignored_files_included; /table_pins; /scanned_tables; /scanned_rows; /applicable_curation; /unrelated_lexical_hits; /exclusion_conclusion; /limitations | context_only | Native complete bounded implemented-table scan: one identity-applicable Sodorifen/BGC0001361 override and 16 unrelated generic Streptomyces hits. No applicability is transferred to another owner or locus. |
| support-2397-chemistry | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json; /records/6/declared_structure; /records/6/literal_InChI_layers; /records/6/formula_comparison_scope; /records/6/comparisons; /records/6/atom_correspondence | supports | Both stored forms reproduce the retained normalized identifiers; all ten comparison flags are true and the saved chirality-aware map spans the atoms. full_graph_identity_established remains false. |
| support-2397-topology | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles; /records/6/inchi | supports | Complete personally read stored strings, atom/bond/ring/stereo/motif tables and scalar descriptors for both forms; no new parse or natural-identity inference. |
| support-2397-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /molecular_forms; /comparisons_true; /warning_count; /warning_record_attribution; /limits | supports | ROOT accepts the single original twenty-form diagnostic. Four charge-rearrangement warnings remain global and unassigned. |
| support-2397-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic exit 0 with preserved streams, no retry or external request. |
| support-2397-diagnostic-warnings | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | context_only | Four original Charges were rearranged warnings remain global and unassigned to owners. |
| support-2397-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2397-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2397-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2397-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2397-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame with 1 row placements; empty results are bounded by its retained local predicate. |
| support-2397-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Complete retained mibig_compounds row, physical lines 146–146, all 25 fields; source/citation roles are preserved. |
| support-2397-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 146 | context_only | Exact whole physical source rows and all fields joined to saved inventory; no source query replay. |
| support-2397-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame with 0 row placements; empty results are bounded by its retained local predicate. |
| support-2397-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame with 1 row placements; empty results are bounded by its retained local predicate. |
| support-2397-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Complete retained lotus_occurrences row, physical lines 1196–1196, all 6 fields; source/citation roles are preserved. |
| support-2397-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 1196 | context_only | Exact whole physical source rows and all fields joined to saved inventory; no source query replay. |
| support-2397-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame with 0 row placements; empty results are bounded by its retained local predicate. |
| support-2397-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame with 1 row placements; empty results are bounded by its retained local predicate. |
| support-2397-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/npclassifier/matches/0 | supports | Complete retained npclassifier row, physical lines 490–490, all 7 fields; source/citation roles are preserved. |
| support-2397-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 490 | context_only | Exact whole physical source rows and all fields joined to saved inventory; no source query replay. |
| support-2397-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame with 0 row placements; empty results are bounded by its retained local predicate. |
| support-2397-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame with 0 row placements; empty results are bounded by its retained local predicate. |
| support-2397-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame with 0 row placements; empty results are bounded by its retained local predicate. |
| support-2397-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/37/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame with 0 row placements; empty results are bounded by its retained local predicate. |
| support-2397-paired-owner-boundary | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/smiles; /records/5/inchi; /records/5/comparisons | context_only | The other individually reviewed chemical form retains its own complete saved structure/identifier tables. Local epimeric or oxidation/glycosylation distinctions do not transfer biological claims. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-240/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-240/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-240/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-240/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-240/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally; natural identity, primary papers, current taxonomy and external identifiers were not freshly verified.
- Full QC and complete OAK authority coverage remain unavailable; local gates/parsing do not replace them.
- Normalized identifiers and complete atom-count matches do not establish full fixed-graph or natural-form identity; explicit stereo limits remain.
- Four original charge-rearrangement warnings remain global and unassigned.
- Occurrence, producer, locus, model, companion and assay claims retain separate scopes.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five complete owners/history, the selected 45 saved query frames and 26 positive source rows (280 fields), within its complete 11-context/99-frame/42-row assignment. Complementary BGC source and Native cache/curation reading retain explicit attribution.
- All ten paired saved forms personally read: 292 atom rows and 324 bond rows plus complete strings, scalars, rings, stereo, motifs and correspondence, using exact lossless factoring. No new molecular parse.
- Actual last-five intakes contain 193 input placements over 45 paths. Support operated the authorized original intake controller; ROOT operated diagnostic and reader launch wrappers, with Native independent saved-result audits. This fragment authoring invoked no targets or requests.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T124233Z-snf4435d
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: SNF4435D'
started_at: '2026-11-04T11:41:40.736229Z'
finished_at: '2026-11-04T12:42:33.168031Z'
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
summary: SNF4435D has internally consistent retained structure and identifier correspondence
  while remaining distinct from SNF4435C. The versioned Terpenoids filing merits a
  bounded applicability concern alongside the preserved PKS source class. Producer,
  demonstrated locus and occurrence claims retain separate evidence grades. No supported
  source-edit finding is established; this is a qualified partial review.
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
  - path: data/natural_products/polyketides/orinocin.yaml
    sha256: 0a3215d2c430c465b161cf71a12a79174802a62c5b61bc596d4bdcc5a8bbfe13
    role: context
  - path: data/natural_products/polyketides/spectinabilin.yaml
    sha256: 8a7cdb81d9c952c26195bd758f819b17c34ad0e2014e464cb4759853a7b4b26d
    role: context
  - path: data/natural_products/terpenoids/snf4435c.yaml
    sha256: a392ac3870c210e80695a07d8efe7abdef8f66099d20d3defa83308ae2496058
    role: context
  - path: data/natural_products/terpenoids/snf4435d.yaml
    sha256: 6d40948f66ebbf501aa451b9e08b4f29ca01d68c14d9c4fdb5d27ec41e5ae3dc
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
  selection: Campaign path order 2397; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-39f27be5a3
targets:
- target_id: naturalproductmech:mibig-39f27be5a3
  path: data/natural_products/terpenoids/snf4435d.yaml
  label: SNF4435D
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
  - naturalproductmech:mibig-39f27be5a3
  command: just validate-strict data/natural_products/terpenoids/secobotrytriendiol.yaml
    data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml data/natural_products/terpenoids/sespenine.yaml
    data/natural_products/terpenoids/sesterfisheric-acid.yaml data/natural_products/terpenoids/sesterfisherol.yaml
    data/natural_products/terpenoids/snf4435c.yaml data/natural_products/terpenoids/snf4435d.yaml
    data/natural_products/terpenoids/sodorifen.yaml data/natural_products/terpenoids/sordaricin-b.yaml
    data/natural_products/terpenoids/sordarin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-240/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-39f27be5a3
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-240/validate-all-001.tsv
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
  - naturalproductmech:mibig-39f27be5a3
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
  - naturalproductmech:mibig-39f27be5a3
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
  - naturalproductmech:mibig-39f27be5a3
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-240/review-queue-001.tsv
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
  - naturalproductmech:mibig-39f27be5a3
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-39f27be5a3
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-39f27be5a3
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2397-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/snf4435d.yaml
  locator: Whole current plaintext and complete curation_history
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete owner and 2 history events personally read; unchanged source record.
  snapshot_sha256: 6d40948f66ebbf501aa451b9e08b4f29ca01d68c14d9c4fdb5d27ec41e5ae3dc
- evidence_id: support-2397-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete accepted captured owner establishes all present and absent roots.
    No causal graph, component, biosynthetic pathway or molecular target is declared;
    no selected reader applies.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: support-2397-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/6/owner_document/identifier; /records/6/owner_document/label;
    /records/6/owner_document/chemical_structure; /records/6/owner_document/source_concepts;
    /records/6/owner_document/xrefs; /records/6/owner_document/grounding_status; /records/6/owner_document/grounding_notes
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Retained identifier/key, stored structure, source concepts and grounding
    status; optional historical notes and definitions remain limited to the selected
    present fields. No fresh natural-identity proof.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: support-2397-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters;
    /records/6/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete producer and locus assertions with their independent grades and
    historical citation roles. Every retained version, coordinate and method is preserved
    without transferring support between claims.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: support-2397-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Whole owner establishes retained occurrence, related-corpus and activity
    annotations and the absence of a molecular target; no broader biological absence
    or activity transfer is inferred.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: support-2397-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/6/owner_document/np_pathway; /records/6/owner_document/np_classification;
    /records/6/owner_document/bgc_class; /records/6/owner_document/biosynthesis_origin
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Versioned NPClassifier predictions, glycoside flag and retained source
    class are distinct assertions; no automatic reclassification.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: support-2397-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-target-input-plan-001.json
  locator: /records/6/proposed_companion_paths; /records/6/direct_companion_predicates;
    /records/6/additional_context_roles
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: Exact one-hop context predicates and input roles; companion identity, activity
    and producer claims do not transfer.
  snapshot_sha256: e52fb36424e9a024531fd104d8039f91d4747645b78c4db4b0654db1e131da52
- evidence_id: support-2397-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240/intakes/2397-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: 'Original canonical intake: one target, exact maintained/generated ownership
    paths and immutable source-input map.'
  snapshot_sha256: 65c20d23ecb0dac945b083e2ddb3f6a2a4067606fee45ddada037c0fb8f7b067
- evidence_id: support-2397-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240/root-intake-acceptance-001.json
  locator: /status; /accepted; /summary; /source_placements; /source_paths
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: ROOT accepts all ten original intakes and exact source alignment.
  snapshot_sha256: 39665ad64e8c5ac43677a515dec2d8ff754b14f46840f107070fba7f9c20fe80
- evidence_id: support-2397-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /scope
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Original local extraction is accepted; source assertions remain retained
    evidence, not fresh verification.
  snapshot_sha256: 028f75b96abca331b845ddc08aadce4c383f232a598f5a508eed037d094dae26
- evidence_id: support-2397-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-target-input-plan-001.json
  locator: /records/6/proposed_input_paths; /records/6/proposed_input_count
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Actual immutable input plan reconciled to this canonical intake.
  snapshot_sha256: e52fb36424e9a024531fd104d8039f91d4747645b78c4db4b0654db1e131da52
- evidence_id: support-2397-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240/root-source-plan-acceptance-001.json
  locator: /status; /accepted; /plan; /verification
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: ROOT accepts the original complete local plan and exact input-map transformations.
  snapshot_sha256: d5bc2e6c4341bfd6ba23fb5fc9439fe40f227fe5848e1352f223d48871172734
- evidence_id: support-2397-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/support-prep/support-current240-source-reading-001.json
  locator: /division; /reading; /contexts; /source_cautions
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Support personally read 11 assigned contexts, 99 query frames and 42 rows;
    selected last-five subset is 45 frames and 26 rows. BGC companion and Native cache/curation
    readings retain their named attribution.
  snapshot_sha256: 4d0f937b395f6274618dd55e04ec2f3892672e756fb7f68ac5d0305de6af7a97
- evidence_id: support-2397-molecular-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/support-prep/support-current240-last-five-molecular-reading-001.json
  locator: /read_scope; /representation; /records; /totals; /read_caveats
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Support complete paired-form table reading is attributed by actual output
    chunks; no additional molecular parse.
  snapshot_sha256: 9a9b737ee495dd0cf9e35f4dcb39849446a6e795bb208df31857823ec4c2d7ef
- evidence_id: support-2397-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/native-prep/native-current240-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /requested_ids; /whole_stanza_locations; /readings; /cautions
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: Native personally read all 22 complete saved stanzas and their physical
    locations; no unmatched ID or forward route is retained. Cached labels do not
    constitute current external taxonomy verification.
  snapshot_sha256: 56fcae4e15e6d6042ddc77c6308f556c8e057c1fcd57af82c36c7f50eb28884c
- evidence_id: support-2397-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/native-prep/native-current240-implemented-curation-scan-001.json
  locator: /scope; /ignored_files_included; /table_pins; /scanned_tables; /scanned_rows;
    /applicable_curation; /unrelated_lexical_hits; /exclusion_conclusion; /limitations
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: 'Native complete bounded implemented-table scan: one identity-applicable
    Sodorifen/BGC0001361 override and 16 unrelated generic Streptomyces hits. No applicability
    is transferred to another owner or locus.'
  snapshot_sha256: e11b54bb43c56a6f60a0183df7479e707360d3ae3e984dba85792653fd27bab4
  search_scope: All41 current owner/source contexts, fullkeys, IDs, ownedBGCs, labels/slugs,
    taxa, chemical IDs,44 exact BGC:compound IDs and0 actual AID tuples. Case-insensitive
    literal token scan of complete rows in9 relevant curation TSVs; Path.rglob enumerates
    all11 TSVs including ignored files.
- evidence_id: support-2397-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/declared_structure; /records/6/literal_InChI_layers; /records/6/formula_comparison_scope;
    /records/6/comparisons; /records/6/atom_correspondence
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Both stored forms reproduce the retained normalized identifiers; all ten
    comparison flags are true and the saved chirality-aware map spans the atoms. full_graph_identity_established
    remains false.
  snapshot_sha256: df6a2b945015b15d512b8fe44d459381e89edf2ba59bc2c68e2f4c3af5c3e25c
- evidence_id: support-2397-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles; /records/6/inchi
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete personally read stored strings, atom/bond/ring/stereo/motif tables
    and scalar descriptors for both forms; no new parse or natural-identity inference.
  snapshot_sha256: df6a2b945015b15d512b8fe44d459381e89edf2ba59bc2c68e2f4c3af5c3e25c
- evidence_id: support-2397-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /molecular_forms; /comparisons_true; /warning_count;
    /warning_record_attribution; /limits
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: ROOT accepts the single original twenty-form diagnostic. Four charge-rearrangement
    warnings remain global and unassigned.
  snapshot_sha256: 7b2df2f605f5811f33a50b322bcb32924d833f122debedde4aade3f1cbb98593
- evidence_id: support-2397-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Original diagnostic exit 0 with preserved streams, no retry or external
    request.
  snapshot_sha256: e8eb39e2c4d3c778bd003e0f6124b4b8fe805c37edfecce886a63b7e6c9db494
- evidence_id: support-2397-diagnostic-warnings
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: Four original Charges were rearranged warnings remain global and unassigned
    to owners.
  snapshot_sha256: 99951a7dfd001f15be66cdf9a08ba90b41f25c0e20a58e3f09ea59003a415d47
- evidence_id: support-2397-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2397-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2397-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2397-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2397-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete saved mibig_compounds frame with 1 row placements; empty results
    are bounded by its retained local predicate.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "DXCYJJKWPZZHNZ-KAKVGEDNSA-N", "saved_frame": "/contexts/37/source_scope_inventory/joins/mibig_compounds",
    "scope": "Immutable local source inventory only; no live query, retry or broad
    absence claim."}'
- evidence_id: support-2397-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete retained mibig_compounds row, physical lines 146–146, all 25 fields;
    source/citation roles are preserved.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
- evidence_id: support-2397-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 146
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: Exact whole physical source rows and all fields joined to saved inventory;
    no source query replay.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2397-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete saved chebi_structures frame with 0 row placements; empty results
    are bounded by its retained local predicate.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "DXCYJJKWPZZHNZ-KAKVGEDNSA-N", "saved_frame": "/contexts/37/source_scope_inventory/joins/chebi_structures",
    "scope": "Immutable local source inventory only; no live query, retry or broad
    absence claim."}'
- evidence_id: support-2397-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete saved lotus_occurrences frame with 1 row placements; empty results
    are bounded by its retained local predicate.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "DXCYJJKWPZZHNZ-KAKVGEDNSA-N", "saved_frame": "/contexts/37/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Immutable local source inventory only; no live query, retry or broad
    absence claim."}'
- evidence_id: support-2397-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete retained lotus_occurrences row, physical lines 1196–1196, all
    6 fields; source/citation roles are preserved.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
- evidence_id: support-2397-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 1196
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: Exact whole physical source rows and all fields joined to saved inventory;
    no source query replay.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2397-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame with 0 row placements; empty
    results are bounded by its retained local predicate.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "DXCYJJKWPZZHNZ-KAKVGEDNSA-N", "saved_frame": "/contexts/37/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Immutable local source inventory only; no live query, retry or broad
    absence claim."}'
- evidence_id: support-2397-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete saved npclassifier frame with 1 row placements; empty results
    are bounded by its retained local predicate.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "DXCYJJKWPZZHNZ-KAKVGEDNSA-N", "saved_frame": "/contexts/37/source_scope_inventory/joins/npclassifier",
    "scope": "Immutable local source inventory only; no live query, retry or broad
    absence claim."}'
- evidence_id: support-2397-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete retained npclassifier row, physical lines 490–490, all 7 fields;
    source/citation roles are preserved.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
- evidence_id: support-2397-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 490
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: Exact whole physical source rows and all fields joined to saved inventory;
    no source query replay.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2397-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame with 0 row placements; empty results
    are bounded by its retained local predicate.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "DXCYJJKWPZZHNZ-KAKVGEDNSA-N", "saved_frame": "/contexts/37/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Immutable local source inventory only; no live query, retry or broad
    absence claim."}'
- evidence_id: support-2397-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete saved bindingdb_targets frame with 0 row placements; empty results
    are bounded by its retained local predicate.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "DXCYJJKWPZZHNZ-KAKVGEDNSA-N", "saved_frame": "/contexts/37/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Immutable local source inventory only; no live query, retry or broad
    absence claim."}'
- evidence_id: support-2397-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame with 0 row placements; empty
    results are bounded by its retained local predicate.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "DXCYJJKWPZZHNZ-KAKVGEDNSA-N", "saved_frame": "/contexts/37/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Immutable local source inventory only; no live query, retry or broad
    absence claim."}'
- evidence_id: support-2397-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/37/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: supports
  summary: Complete saved chebi_origins frame with 0 row placements; empty results
    are bounded by its retained local predicate.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/37/source_scope_inventory/joins/chebi_origins",
    "scope": "Immutable local source inventory only; no live query, retry or broad
    absence claim."}'
- evidence_id: support-2397-paired-owner-boundary
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/smiles; /records/5/inchi; /records/5/comparisons
  accessed_at: '2026-11-04T12:27:16.989635Z'
  support: context_only
  summary: The other individually reviewed chemical form retains its own complete
    saved structure/identifier tables. Local epimeric or oxidation/glycosylation distinctions
    do not transfer biological claims.
  snapshot_sha256: df6a2b945015b15d512b8fe44d459381e89edf2ba59bc2c68e2f4c3af5c3e25c
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-240/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json
  accessed_at: '2026-11-04T11:48:26.886706Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: a3ea4c1642d250ceb04a5ce0d0e63df092fc0b87afdabbbe0b2b7951b0ce3708
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-240/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json
  accessed_at: '2026-11-04T11:48:50.739192Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 0062770845553872da90b572db6992f46a2ed20f86a684fc1f4021b943a3f384
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-240/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json
  accessed_at: '2026-11-04T11:49:09.952157Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-240/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json
  accessed_at: '2026-11-04T11:49:43.151899Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-240/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json
  accessed_at: '2026-11-04T11:49:55.198103Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: ef0f483866268632a552451bc3d4ba0368facfa350b47970dd4e1d1f9e3727b9
assessments:
- area: identity
  topic: Retained structure and identifier correspondence
  outcome: supported
  summary: SNF4435D retains the minted identifier naturalproductmech:mibig-39f27be5a3,
    full key DXCYJJKWPZZHNZ-KAKVGEDNSA-N and MIBiG BGC0000110 version 5 source concept.
    Both accepted stored-form diagnostics reproduce that full key. The retained no-3-star-ChEBI-match
    rationale is a bounded local-inventory result, not a new external absence claim.
    npatlas:NPA01579 remains an unrefreshed cross-reference. SNF4435C shares the connectivity
    block but has a different stereochemical key; the labels and complete forms are
    not interchangeable.
  assessment_id: support-2397-identity
  target_ids:
  - naturalproductmech:mibig-39f27be5a3
  evidence_ids:
  - support-2397-grounding-owner
  - support-2397-chemistry
  - support-2397-direct-contexts
  - support-2397-query-chebi_structures
  - support-2397-source-mibig_compounds-0
  - support-2397-paired-owner-boundary
  dimensions:
  - name: standard_inchi_key
    value: DXCYJJKWPZZHNZ-KAKVGEDNSA-N; exact retained full key, not a first-block
      or name substitution.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2397-grounding-owner
    - support-2397-chemistry
    - support-2397-direct-contexts
    - support-2397-query-chebi_structures
    - support-2397-source-mibig_compounds-0
    - support-2397-paired-owner-boundary
  - name: grounding_scope
    value: MINTED at the retained local scope; natural identity and current external
      grounding remain unverified.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2397-grounding-owner
    - support-2397-chemistry
    - support-2397-direct-contexts
    - support-2397-query-chebi_structures
    - support-2397-source-mibig_compounds-0
    - support-2397-paired-owner-boundary
- area: representation
  topic: Stored topology and stereochemical scope
  outcome: supported
  summary: Both forms are neutral C28H31NO6 with 35 heavy atoms and 39 bonds. All
    ten comparison flags are true and the chirality-aware map spans all atoms; full_graph_identity_established
    remains false. Five tetrahedral centers are specified with no unspecified candidate
    tetrahedral center. Saved SMILES atom 22 is S, versus R in SNF4435C, while the
    remaining corresponding tetrahedral CIP labels agree. The tables retain a nitro
    group as charge-separated N/O with zero aggregate charge, five ring lists including
    a five-membered cyclic ether and a four-carbon ring, and one carbonyl. This supports
    internal representation consistency, not an independently verified natural stereoisomer.
    The four global charge warnings cannot be assigned to this owner.
  assessment_id: support-2397-representation
  target_ids:
  - naturalproductmech:mibig-39f27be5a3
  evidence_ids:
  - support-2397-grounding-owner
  - support-2397-chemistry
  - support-2397-topology
  - support-2397-molecular-reading
  - support-2397-diagnostic-acceptance
  - support-2397-structure-schema
  - support-2397-stereo-method
  - support-2397-paired-owner-boundary
  dimensions:
  - name: stereochemistry_scope
    value: Five specified tetrahedral centers; corresponding SNF4435C epimeric center
      differs (SMILES atom22 S here versus R there). Local stereo_complete true does
      not authenticate natural stereochemistry.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2397-grounding-owner
    - support-2397-chemistry
    - support-2397-topology
    - support-2397-molecular-reading
    - support-2397-diagnostic-acceptance
    - support-2397-structure-schema
    - support-2397-stereo-method
    - support-2397-paired-owner-boundary
  - name: representation_correspondence
    value: All ten saved comparison flags true; complete chirality-aware atom-count
      map. full_graph_identity_established remains false; no independent natural-form
      proof.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2397-grounding-owner
    - support-2397-chemistry
    - support-2397-topology
    - support-2397-molecular-reading
    - support-2397-diagnostic-acceptance
    - support-2397-structure-schema
    - support-2397-stereo-method
    - support-2397-paired-owner-boundary
- area: provenance
  topic: Producer and demonstrated locus remain distinct
  outcome: supported
  summary: MIBiG BGC0000110 version 5 retains Streptomyces orinoci, NCBITaxon:67339,
    as a SOURCE_ASSERTION producer. The separate AM778535.1 locus is CLUSTER_DEMONSTRATED
    through heterologous expression; no locus coordinates or strain are supplied in
    this retained row. That locus grade does not upgrade the native taxon claim or
    make the LOTUS Streptomyces spectabilis occurrences into producer evidence.
  assessment_id: support-2397-provenance
  target_ids:
  - naturalproductmech:mibig-39f27be5a3
  evidence_ids:
  - support-2397-origin-owner
  - support-2397-source-reading
  - support-2397-direct-contexts
  - support-2397-cached-taxonomy
  - support-2397-curation-scope
  - support-2397-source-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    value: Streptomyces orinoci (NCBITaxon:67339); 1 retained occurrence placements
      retain their separate taxon/reference scope.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2397-origin-owner
    - support-2397-source-reading
    - support-2397-direct-contexts
    - support-2397-cached-taxonomy
    - support-2397-curation-scope
    - support-2397-source-mibig_compounds-0
  - name: producer_evidence
    value: mibig:BGC0000110 SOURCE_ASSERTION (version 5); locus and occurrence support
      do not automatically upgrade producer claims.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2397-origin-owner
    - support-2397-source-reading
    - support-2397-direct-contexts
    - support-2397-cached-taxonomy
    - support-2397-curation-scope
    - support-2397-source-mibig_compounds-0
  - name: locus_evidence
    value: mibig:BGC0000110 version 5 CLUSTER_DEMONSTRATED; methods Heterologous expression
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2397-origin-owner
    - support-2397-source-reading
    - support-2397-direct-contexts
    - support-2397-cached-taxonomy
    - support-2397-curation-scope
    - support-2397-source-mibig_compounds-0
- area: evidence
  topic: Historical citation and companion scope
  outcome: supported
  summary: PMID:17763486 is retained as MIBiG entry-level DATABASE_ASSERTION provenance.
    Active status, questionable quality and complete source completeness are source-entry
    metadata, not independent proof for the precise stereoisomer. The distinct full-key
    same-BGC companions Orinocin and Spectinabilin supply locus context only; their
    labels, model classes, occurrence rows and activity claims are not transferred.
    No primary text or external identity record was retrieved for this review.
  assessment_id: support-2397-citations
  target_ids:
  - naturalproductmech:mibig-39f27be5a3
  evidence_ids:
  - support-2397-grounding-owner
  - support-2397-origin-owner
  - support-2397-occurrence-activity-owner
  - support-2397-source-reading
  - support-2397-direct-contexts
  - support-2397-source-mibig_compounds-0
  - support-2397-source-lotus_occurrences-0
  - support-2397-source-npclassifier-0
  dimensions:
  - name: citation_scope
    value: PMID:17763486 is retained as MIBiG entry-level DATABASE_ASSERTION provenance.
      Active status, questionable quality and complete source completeness are source-entry
      metadata, not independent proof for the precise stereoisomer. The distinct full-key
      same-BGC companions Orinocin and Spectinabilin supply locus context only; their
      labels, model classes, occurrence rows and activity claims are not transferred.
      No primary text or external identity record was retrieved for this review.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2397-grounding-owner
    - support-2397-origin-owner
    - support-2397-occurrence-activity-owner
    - support-2397-source-reading
    - support-2397-direct-contexts
    - support-2397-source-mibig_compounds-0
    - support-2397-source-lotus_occurrences-0
    - support-2397-source-npclassifier-0
- area: evidence
  topic: Occurrence and activity boundaries
  outcome: supported
  summary: The selected full-key inventory contains one LOTUS row for Streptomyces
    spectabilis, NCBITaxon:68270, citing DOI:10.7164/ANTIBIOTICS.54.541. These are
    detection/isolation assertions, separately retained from the MIBiG producer; shared
    references do not establish publication independence or strain equivalence. No
    actual PubChem assay, BindingDB target, CyanometDB or AntibioticMech row is retained
    for this selected key, and the owner has no bioactivity or molecular-target root.
    These bounded negatives do not establish inactivity or absence of published activity.
  assessment_id: support-2397-occurrence
  target_ids:
  - naturalproductmech:mibig-39f27be5a3
  evidence_ids:
  - support-2397-occurrence-activity-owner
  - support-2397-direct-contexts
  - support-2397-cached-taxonomy
  - support-2397-curation-scope
  - support-2397-query-lotus_occurrences
  - support-2397-query-chebi_origins
  - support-2397-query-cyanometdb_occurrences
  - support-2397-query-pubchem_bioassay
  - support-2397-query-bindingdb_targets
  - support-2397-query-antibioticmech_inchikeys
  - support-2397-source-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    value: 1 retained owner occurrences; raw matching placements are source assertions,
      not independent experiments or demonstrated native producers.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2397-occurrence-activity-owner
    - support-2397-direct-contexts
    - support-2397-cached-taxonomy
    - support-2397-curation-scope
    - support-2397-query-lotus_occurrences
    - support-2397-query-chebi_origins
    - support-2397-query-cyanometdb_occurrences
    - support-2397-query-pubchem_bioassay
    - support-2397-query-bindingdb_targets
    - support-2397-query-antibioticmech_inchikeys
    - support-2397-source-lotus_occurrences-0
  - name: assay_target_scope
    value: No retained actual assay or molecular target; empty bounded joins do not
      establish inactivity.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2397-occurrence-activity-owner
    - support-2397-direct-contexts
    - support-2397-cached-taxonomy
    - support-2397-curation-scope
    - support-2397-query-lotus_occurrences
    - support-2397-query-chebi_origins
    - support-2397-query-cyanometdb_occurrences
    - support-2397-query-pubchem_bioassay
    - support-2397-query-bindingdb_targets
    - support-2397-query-antibioticmech_inchikeys
    - support-2397-source-lotus_occurrences-0
- area: consistency
  topic: Versioned filing applicability
  outcome: concern
  summary: NPClassifier version npclassifier.gnps2.org@2026-09-07 supplies Terpenoids
    with empty subclass and superclass lists, whereas BGC0000110 separately asserts
    PKS. The nitroaryl/oxygenated heterocyclic structure and the source PKS context
    make the Terpenoids model filing an applicability question, not an established
    ingestion error or authority to overwrite the prediction. The complete topology
    has no separate sugar residue or saturated C5O candidate cycle, and its internal
    ether/methoxy bridges are compatible with the retained is_glycoside false. Neither
    a ring count nor a shared locus determines biosynthetic class by itself.
  assessment_id: support-2397-classification
  target_ids:
  - naturalproductmech:mibig-39f27be5a3
  evidence_ids:
  - support-2397-classification-owner
  - support-2397-chemistry
  - support-2397-topology
  - support-2397-structure-schema
  - support-2397-classification-seeder
  - support-2397-source-mibig_compounds-0
  - support-2397-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: NPClassifier version npclassifier.gnps2.org@2026-09-07 supplies Terpenoids
      with empty subclass and superclass lists, whereas BGC0000110 separately asserts
      PKS. The nitroaryl/oxygenated heterocyclic structure and the source PKS context
      make the Terpenoids model filing an applicability question, not an established
      ingestion error or authority to overwrite the prediction. The complete topology
      has no separate sugar residue or saturated C5O candidate cycle, and its internal
      ether/methoxy bridges are compatible with the retained is_glycoside false. Neither
      a ring count nor a shared locus determines biosynthetic class by itself.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2397-classification-owner
    - support-2397-chemistry
    - support-2397-topology
    - support-2397-structure-schema
    - support-2397-classification-seeder
    - support-2397-source-mibig_compounds-0
    - support-2397-source-npclassifier-0
- area: completeness
  topic: Review completion
  outcome: unknown
  summary: The complete owner/history, actual canonical intake, all assigned source
    payloads and both accepted saved molecular forms were personally read. No causal_graphs,
    causal_graph_refs, biosynthetic_pathway or molecular_targets root is present,
    so no selected maintained-reader call applies. Full QC, complete OAK authority
    coverage and fresh external verification remain unavailable. No supported source-edit
    finding or action is established; this remains a qualified partial review.
  assessment_id: support-2397-completion
  target_ids:
  - naturalproductmech:mibig-39f27be5a3
  evidence_ids:
  - support-2397-owner
  - support-2397-capture
  - support-2397-intake
  - support-2397-intake-acceptance
  - support-2397-inventory-acceptance
  - support-2397-plan
  - support-2397-plan-acceptance
  - support-2397-source-reading
  - support-2397-molecular-reading
  - support-2397-diagnostic-acceptance
  - support-2397-diagnostic-execution
  - support-2397-diagnostic-warnings
  - support-2397-review-profile
  dimensions:
  - name: review_completion
    value: Partial, pass_with_limitations. Complete assigned local source/intake/molecular
      reading and no applicable selected maintained reader; Full QC, complete OAK
      and fresh external verification unavailable.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2397-owner
    - support-2397-capture
    - support-2397-intake
    - support-2397-intake-acceptance
    - support-2397-inventory-acceptance
    - support-2397-plan
    - support-2397-plan-acceptance
    - support-2397-source-reading
    - support-2397-molecular-reading
    - support-2397-diagnostic-acceptance
    - support-2397-diagnostic-execution
    - support-2397-diagnostic-warnings
    - support-2397-review-profile
findings: []
actions: []
limitations:
- All evidence is retained locally; natural identity, primary papers, current taxonomy
  and external identifiers were not freshly verified.
- Full QC and complete OAK authority coverage remain unavailable; local gates/parsing
  do not replace them.
- Normalized identifiers and complete atom-count matches do not establish full fixed-graph
  or natural-form identity; explicit stereo limits remain.
- Four original charge-rearrangement warnings remain global and unassigned.
- Occurrence, producer, locus, model, companion and assay claims retain separate scopes.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support personally read five complete owners/history, the selected 45 saved query
  frames and 26 positive source rows (280 fields), within its complete 11-context/99-frame/42-row
  assignment. Complementary BGC source and Native cache/curation reading retain explicit
  attribution.
- 'All ten paired saved forms personally read: 292 atom rows and 324 bond rows plus
  complete strings, scalars, rings, stereo, motifs and correspondence, using exact
  lossless factoring. No new molecular parse.'
- Actual last-five intakes contain 193 input placements over 45 paths. Support operated
  the authorized original intake controller; ROOT operated diagnostic and reader launch
  wrappers, with Native independent saved-result audits. This fragment authoring invoked
  no targets or requests.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-240
```
