# Local evidence review: platencin

- Review: 20261104T092726Z-platencin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T08:24:13.799845Z
- Finished UTC: 2026-11-04T09:27:26.547529Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

CHEBI:68241 retains exact local full-key correspondence across ChEBI, MIBiG and AntibioticMech, four specified tetrahedral centers, and separately scoped producer, occurrence and antibacterial assertions. Canonical SMILES differ between the amide and regenerated imidic representation despite normalized identifier agreement. No supported source-edit finding follows; fresh natural identity and mechanism verification remain unavailable, so the review is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2379; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:68241 | data/natural_products/terpenoids/platencin.yaml | generated | platencin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:68241 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:68241 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:68241 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:68241 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:68241 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:68241 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:68241 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:68241 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained structure and identifier correspondence

identity: supported. Targets: CHEBI:68241.

The owner CHEBI:68241 carries DWUHGPPFFABTIY-RLWZQHMASA-N. The ChEBI three-star row, BGC0001140 version 5 compound 2 and pinned AntibioticMech row use this same key. The separate selected partial-key Platencin record shares a name and PubChem:44450228 but is not an exact full-key match. Its two assay calls remain attached to that separate record. Both accepted stored-form diagnostics reproduce the declared full key; normalized identifier agreement does not independently prove natural identity.

### Stored representation and stereochemical scope

representation: supported. Targets: CHEBI:68241.

The stored pair is neutral C24H27NO6 with 31 heavy atoms and 34 bonds. Formula, charge, normalized Standard InChI and declared full key agree, but both canonical-SMILES comparisons are false and the full atom-match array is empty. Source C17(=O18)–N19(H) becomes InChI-derived C18(–O27H)=N24; the canonical branches show the corresponding amide/imidic difference. Four specified tetrahedral centers remain present in both forms. The additional unspecified C=N belongs to the reconstructed representation and does not by itself refute the source stereo_complete true flag, whose extractor tests undefined tetrahedral centers. The complete tables preserve the ketone-bearing polycyclic carbon framework and aromatic amide/imidic-linked carboxylic acid with two phenolic hydroxyls. No independent whole-graph or natural-form identity is claimed.

### Producer and locus evidence

provenance: supported. Targets: CHEBI:68241.

Streptomyces platensis, NCBITaxon:58346, is recorded as BGC_CHARACTERIZED for the CLUSTER_DEMONSTRATED BGC0001140 locus, FJ655920.1:4531–45738, with knock-out and heterologous-expression methods. Shared-BGC Platensilin, Platensimycin and thio compounds provide direct context, each with a distinct structure key and compound-specific reference. Neither their identities nor activities transfer through cluster membership.

### Citation roles

evidence: supported. Targets: CHEBI:68241.

PMID:17456595 is the MIBiG compound-evidence reference. Three LOTUS DOIs and ChEBI origin PMID:21214253 have occurrence roles. The AntibioticMech correspondence is pinned to corpus commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976. These retain their database/corpus provenance; no new publication access, sequence grounding or experimental verification has occurred.

### Occurrence and activity scope

evidence: supported. Targets: CHEBI:68241.

Three LOTUS rows report Streptomyces platensis with distinct DOI strings. The ChEBI origin row adds the recorded strain context MA7327 and PMID:21214253; that strain detail is not generalized to all rows. The exact AntibioticMech key/identifier supports the retained ANTIBACTERIAL corpus summary. The ChEBI definition also mentions fatty-acid-synthase inhibition, but this is a retained definition claim rather than a newly established direct target mechanism. No PubChem assay rows matched this exact full key in the saved query.

### Versioned classification applicability

consistency: supported. Targets: CHEBI:68241.

The separately asserted Aromatic amino acid/simple benzoic acid and Diterpenoid classes fit the retained aromatic carboxylic-acid/amide and terpenoid-framework source context. NPClassifier’s versioned Terpenoids / Diterpenoids / Platensimycin and Platencins prediction remains a different evidence layer. Complete tables contain no identified sugar residue or glycosidic linkage, supporting is_glycoside false within the stored topology. Neither those observations nor the ANTIBACTERIAL corpus class establishes a complete biosynthetic or pharmacological mechanism.

### Review completion

completeness: unknown. Targets: CHEBI:68241.

The complete owner/history, accepted canonical intake, retained source rows and both saved molecular forms were personally read. All four mechanism-related owner roots are absent, so no maintained-reader invocation applies to this owner. Full QC, complete OAK authority coverage and fresh external verification remain unavailable. No supported source-edit finding or action is established; completion remains partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2379-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/platencin.yaml; Whole current plaintext and complete curation_history | supports | Complete current owner and 3 history events personally read; source record unchanged. |
| support-2379-capture | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete accepted owner; absence of causal_graphs, causal_graph_refs, biosynthetic_pathway and molecular_targets retained. No selected reader applies. |
| support-2379-grounding-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/8/owner_document/identifier; /records/8/owner_document/label; /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts; /records/8/owner_document/xrefs; /records/8/owner_document/grounding_status; /records/8/owner_document/definition; /records/8/owner_document/definition_source | supports | Exact retained identifier, complete key, source strings and grounding/definition provenance; no fresh natural identity claim. |
| support-2379-origin-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters; /records/8/owner_document/source_concepts | supports | Producer grades, locus methods/grades and source-specific citation roles remain distinct. |
| support-2379-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/8/owner_document | supports | The complete captured owner records three LOTUS occurrences of Streptomyces platensis with distinct DOI strings, one ChEBI occurrence with detection context MA7327 and PMID:21214253, and an ANTIBACTERIAL bioactivity summary. The strain context is not generalized to the other occurrences, and no molecular-target root is present. |
| support-2379-classification-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification; /records/8/owner_document/compound_classes; /records/8/owner_document/bgc_class | supports | Versioned computed classification is retained separately from asserted source classes. |
| support-2379-chemistry | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/comparisons; /records/8/atom_correspondence | supports | Exact declared strings, normalized identifiers and all comparison/map fields; false values remain explicit. |
| support-2379-topology | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json; /records/8/smiles; /records/8/inchi | supports | Complete paired atom/bond/stereo/ring/motif tables personally read. The source and regenerated representations retain the exact local features described in the representation assessment; no new parse or whole-graph equivalence assertion. |
| support-2379-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /DATA; /execution; /molecular_parse_attempts; /comparison_scope; /warnings; /limits | supports | ROOT accepted one original twenty-form diagnostic. Two omitted-undefined-stereo warnings are global; execution acceptance is not scientific certification. |
| support-2379-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /admission; /stderr; /retries; /external_requests | supports | Original diagnostic command/exit0 and immutable streams are retained; no retry or external request. |
| support-2379-diagnostic-warnings | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | context_only | Two omitted-undefined-stereo warnings; no owner-specific assignment. |
| support-2379-intake | /private/tmp/npm-review-work/shared-next-batch238/intakes/2379-inspect-001.json; /source; /targets | supports | Actual canonical intake identifies this owner and exact source-input snapshot. |
| support-2379-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch238/root-intake-acceptance-001.json; /status; /accepted; /summary; /source_placements; /unique_source_paths | supports | ROOT accepts all ten intakes with 400 placements/70 paths; no later source refresh. |
| support-2379-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch238/root-source-inventory-acceptance-001.json; /status; /inventory | supports | ROOT acceptance pins the original local source inventory. |
| support-2379-plan | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-target-input-plan-001.json; /records/8/proposed_input_paths; /records/8/additional_context_roles; /records/8/proposed_companion_paths | supports | Earned input and direct-companion maps align with actual intake. Companions remain bounded context. |
| support-2379-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch238/root-input-plan-acceptance-001.json; /status; /plan; /verification | supports | ROOT accepted the actual source plan and intake-map alignment. |
| support-2379-source-reading | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-scope-notes-001.json; /reading; /cautions; /scientific_limits; /curation_scope | context_only | Joint complete saved-source readings retain exact personal attribution and claim-specific limits; no fresh source lookup. |
| support-2379-direct-contexts | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-target-input-plan-001.json; /records/8/proposed_companion_paths; /records/8/direct_companion_predicates | context_only | Only exact owned-BGC/full-key direct contexts admitted by the source plan; no identity or evidence transfer. |
| support-2379-curation-scope | /private/tmp/npm-review-work/shared-next-batch238-tentative/native-prep/native-current238-implemented-curation-scan-001.json; /scope; /actual_assay_tuples; /exclusion_conclusion; /applicable_conclusion; /limitations | context_only | Native performed the ignored-inclusive implemented-table scan. No matching LOTUS or selected assay exclusion was identified; source-quality or same-locus metadata is not itself a correction. |
| support-2379-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2379-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2379-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2379-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2379-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds query predicate, command scope and 1 matching row placement(s); no rerun. Exact snapshot scope only. |
| support-2379-source-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical lines 1350–1350; exact header fields; row_sha256=6b49505ed0dc15a6fd3f6f3ca56989404044e82ac0f9abf7aabbdbf22b9f433f | supports | Exact retained mibig_compounds row with all 25 fields, including blank cells. BGC0001140 version 5, compound 2; BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED. |
| support-2379-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures query predicate, command scope and 1 matching row placement(s); no rerun. Exact snapshot scope only. |
| support-2379-source-chebi_structures-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Physical lines 23573–23573; exact header fields; row_sha256=74f0184b1180dd82d4193231c1c38615dd7446d9f73b2d1b97f2caeb1ee8f2bb | supports | Exact retained chebi_structures row with all 6 fields, including blank cells.  |
| support-2379-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences query predicate, command scope and 3 matching row placement(s); no rerun. Exact snapshot scope only. |
| support-2379-source-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 1191–1191; exact header fields; row_sha256=e181c0a2f639a0f19b0d26c1844cad38882898fa10617678da8d19276d95bda3 | supports | Exact retained lotus_occurrences row with all 6 fields, including blank cells. Occurrence only; not an independent producer or experiment count. |
| support-2379-source-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 1192–1192; exact header fields; row_sha256=daf162d5979d8a358a4ba9130fd3da999d3a5d8b9f5e63d9189eafbc3bcddbc3 | supports | Exact retained lotus_occurrences row with all 6 fields, including blank cells. Occurrence only; not an independent producer or experiment count. |
| support-2379-source-lotus_occurrences-2 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 1193–1193; exact header fields; row_sha256=685d44a7a34b6332133e6651b7ba59b08abfd28be31055eac48770b94dd92d2e | supports | Exact retained lotus_occurrences row with all 6 fields, including blank cells. Occurrence only; not an independent producer or experiment count. |
| support-2379-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences query predicate, command scope and 0 matching row placement(s); no rerun. Exact snapshot scope only. |
| support-2379-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier query predicate, command scope and 1 matching row placement(s); no rerun. Exact snapshot scope only. |
| support-2379-source-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical lines 486–486; exact header fields; row_sha256=e624e88750b961212e98c6f732c35b025801b91a44895520fe180992d18774e3 | supports | Exact retained npclassifier row with all 7 fields, including blank cells.  |
| support-2379-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay query predicate, command scope and 0 matching row placement(s); no rerun. Exact snapshot scope only. |
| support-2379-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets query predicate, command scope and 0 matching row placement(s); no rerun. Exact snapshot scope only. |
| support-2379-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys query predicate, command scope and 1 matching row placement(s); no rerun. Exact snapshot scope only. |
| support-2379-source-antibioticmech_inchikeys-0 | /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv; Physical lines 447–447; exact header fields; row_sha256=04f2d347f18ac525ee9736666eb1d2f486754a0dcdbeaa7442e4d81879034562 | supports | Exact retained antibioticmech_inchikeys row with all 6 fields, including blank cells. Exact full-key/identifier/corpus-commit correspondence, not imported target evidence. |
| support-2379-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins query predicate, command scope and 1 matching row placement(s); no rerun. Exact snapshot scope only. |
| support-2379-source-chebi_origins-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Physical lines 8568–8568; exact header fields; row_sha256=2f471a30b670db9775b7ba24203e612b5684e81f14645bc71e995f3dd1fc79c5 | supports | Exact retained chebi_origins row with all 7 fields, including blank cells.  |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-238/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-238/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-238/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-238/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-238/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. Natural identity, primary publications, current taxonomy and external identifiers were not freshly verified.
- Full QC, complete OAK authority coverage and fresh external verification remain unavailable; local parsing and gates do not replace them.
- Matching normalized identifiers do not prove complete fixed-graph identity. All false canonical comparisons and empty atom maps are preserved.
- Two original omitted-undefined-stereo warnings remain global and are not assigned to any owner.
- Occurrences, producer grades, locus support, model predictions, assay calls and sibling-corpus assertions retain separate scope. Shared names, loci or identifiers do not transfer claims.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five complete owners/history, all five actual intakes, 45 selected source query frames and 22 full positive rows/248 fields. Prior companion and complementary source readings remain explicitly attributed through accepted notes.
- Complete personal paired-table reading covers all ten forms: 272 atom rows and 298 bond rows plus every scalar, ring, stereo, motif and mapping field, using lossless constant-column factoring. No new molecular parse.
- ROOT operated the original diagnostic and intakes; Native prepared guarded methods. This scientific authoring invoked no target or external request.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T092726Z-platencin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: platencin'
started_at: '2026-11-04T08:24:13.799845Z'
finished_at: '2026-11-04T09:27:26.547529Z'
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
summary: CHEBI:68241 retains exact local full-key correspondence across ChEBI, MIBiG
  and AntibioticMech, four specified tetrahedral centers, and separately scoped producer,
  occurrence and antibacterial assertions. Canonical SMILES differ between the amide
  and regenerated imidic representation despite normalized identifier agreement. No
  supported source-edit finding follows; fresh natural identity and mechanism verification
  remain unavailable, so the review is partial.
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
  - path: data/natural_products/terpenoids/platencin.yaml
    sha256: 21a6987e6f7c8516683f2de21c7bbe08d7f947471dc769fc2fca99d24fc3e8d6
    role: target
  - path: data/natural_products/terpenoids/platensilin.yaml
    sha256: 104e0a4a067b7cf2c0ce5f0894426ea2e8e841825ebdc7143e19f25e9597dbd5
    role: context
  - path: data/natural_products/terpenoids/platensimycin.yaml
    sha256: 504b7ea4ad4e560784773e38067635c66b140fc9b1c75925ed6c6b30b0f565e4
    role: context
  - path: data/natural_products/terpenoids/thioplatencin.yaml
    sha256: 6e482578167d6e3a09955617ccd5aa3e0ae1a881be4e9c05c4154c9427384807
    role: context
  - path: data/natural_products/terpenoids/thioplatensilin.yaml
    sha256: 66ed0fa93f519082ea94b6b4f4527bb7da580fe995b1092b14611ca69511a4c1
    role: context
  - path: data/natural_products/terpenoids/thioplatensimycin.yaml
    sha256: 2f32e9aba7b153a8b062b52a0bffec41bf8b5ac608ee899d5ca4f5f973acfdbe
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2379; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:68241
targets:
- target_id: CHEBI:68241
  path: data/natural_products/terpenoids/platencin.yaml
  label: platencin
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
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned full-key AntibioticMech structure links and coarse activity summaries;
      no transfer of mechanism.
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
  - CHEBI:68241
  command: just validate-strict data/natural_products/terpenoids/pentalenolactone.yaml
    data/natural_products/terpenoids/pestalodiol-e.yaml data/natural_products/terpenoids/phellandrene.yaml
    data/natural_products/terpenoids/phyllocladan-16-ol.yaml data/natural_products/terpenoids/phyllostictine-b.yaml
    data/natural_products/terpenoids/phytocassane.yaml data/natural_products/terpenoids/pimara-8-14-15-diene.yaml
    data/natural_products/terpenoids/platencin-2.yaml data/natural_products/terpenoids/platencin.yaml
    data/natural_products/terpenoids/platensilin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-238/validate-strict-selected10-001.tsv
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
  - CHEBI:68241
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-238/validate-all-001.tsv
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
  - CHEBI:68241
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
  - CHEBI:68241
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
  - CHEBI:68241
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-238/review-queue-001.tsv
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
  - CHEBI:68241
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:68241
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:68241
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2379-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/platencin.yaml
  locator: Whole current plaintext and complete curation_history
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete current owner and 3 history events personally read; source record
    unchanged.
  snapshot_sha256: 21a6987e6f7c8516683f2de21c7bbe08d7f947471dc769fc2fca99d24fc3e8d6
- evidence_id: support-2379-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete accepted owner; absence of causal_graphs, causal_graph_refs, biosynthetic_pathway
    and molecular_targets retained. No selected reader applies.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: support-2379-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/8/owner_document/identifier; /records/8/owner_document/label;
    /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts;
    /records/8/owner_document/xrefs; /records/8/owner_document/grounding_status; /records/8/owner_document/definition;
    /records/8/owner_document/definition_source
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Exact retained identifier, complete key, source strings and grounding/definition
    provenance; no fresh natural identity claim.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: support-2379-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters;
    /records/8/owner_document/source_concepts
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Producer grades, locus methods/grades and source-specific citation roles
    remain distinct.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: support-2379-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: The complete captured owner records three LOTUS occurrences of Streptomyces
    platensis with distinct DOI strings, one ChEBI occurrence with detection context
    MA7327 and PMID:21214253, and an ANTIBACTERIAL bioactivity summary. The strain
    context is not generalized to the other occurrences, and no molecular-target root
    is present.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: support-2379-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification;
    /records/8/owner_document/compound_classes; /records/8/owner_document/bgc_class
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Versioned computed classification is retained separately from asserted
    source classes.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: support-2379-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/comparisons;
    /records/8/atom_correspondence
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Exact declared strings, normalized identifiers and all comparison/map fields;
    false values remain explicit.
  snapshot_sha256: 40f4a4d85e9c291635bcae75d173e7cb6ea4bcc74a1f9e248a1a9f8c6dc328d3
- evidence_id: support-2379-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/smiles; /records/8/inchi
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete paired atom/bond/stereo/ring/motif tables personally read. The
    source and regenerated representations retain the exact local features described
    in the representation assessment; no new parse or whole-graph equivalence assertion.
  snapshot_sha256: 40f4a4d85e9c291635bcae75d173e7cb6ea4bcc74a1f9e248a1a9f8c6dc328d3
- evidence_id: support-2379-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /DATA; /execution; /molecular_parse_attempts; /comparison_scope;
    /warnings; /limits
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: ROOT accepted one original twenty-form diagnostic. Two omitted-undefined-stereo
    warnings are global; execution acceptance is not scientific certification.
  snapshot_sha256: c58ec3eec001655cc705b5cb711fc96042b2dc765bacf31ef132ab3f8583f414
- evidence_id: support-2379-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /admission; /stderr; /retries; /external_requests
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Original diagnostic command/exit0 and immutable streams are retained; no
    retry or external request.
  snapshot_sha256: c189304847deb6b5bcd363e93f191366348377f38746508ee229fd9fe75a9e8c
- evidence_id: support-2379-diagnostic-warnings
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: context_only
  summary: Two omitted-undefined-stereo warnings; no owner-specific assignment.
  snapshot_sha256: e9b7d87b3202534a3ade2364214485c2749c0f16e7547c6a770de668e46f6259
- evidence_id: support-2379-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch238/intakes/2379-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Actual canonical intake identifies this owner and exact source-input snapshot.
  snapshot_sha256: b1aacde0f3a6104fa7af95fcca0add179424656b4dd547bb42089a27b3b62cc0
- evidence_id: support-2379-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch238/root-intake-acceptance-001.json
  locator: /status; /accepted; /summary; /source_placements; /unique_source_paths
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: ROOT accepts all ten intakes with 400 placements/70 paths; no later source
    refresh.
  snapshot_sha256: 3b660a99915d345d882a0d2bf5949015305d039e8bdd884b21e96240591549f4
- evidence_id: support-2379-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch238/root-source-inventory-acceptance-001.json
  locator: /status; /inventory
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: ROOT acceptance pins the original local source inventory.
  snapshot_sha256: 8b502886402a2a78f2c2e47b1f1b14527b44355cc5396bd7088ac558ffd849d8
- evidence_id: support-2379-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-target-input-plan-001.json
  locator: /records/8/proposed_input_paths; /records/8/additional_context_roles; /records/8/proposed_companion_paths
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Earned input and direct-companion maps align with actual intake. Companions
    remain bounded context.
  snapshot_sha256: d7f788858ab6b318cbd1ab1dbfdc3bd89de0f8b05206e546e3e109d858e8e77a
- evidence_id: support-2379-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch238/root-input-plan-acceptance-001.json
  locator: /status; /plan; /verification
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: ROOT accepted the actual source plan and intake-map alignment.
  snapshot_sha256: c2eb7849664c6b9186115248a7edd7043745ff5ecd0664f37c5ec4bc0d9112e1
- evidence_id: support-2379-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits; /curation_scope
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: context_only
  summary: Joint complete saved-source readings retain exact personal attribution
    and claim-specific limits; no fresh source lookup.
  snapshot_sha256: 845e90961cd00a73cb97c0361f7f8a8c5dba5da7ec17d4b6c029dc816e44fbd7
- evidence_id: support-2379-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-target-input-plan-001.json
  locator: /records/8/proposed_companion_paths; /records/8/direct_companion_predicates
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: context_only
  summary: Only exact owned-BGC/full-key direct contexts admitted by the source plan;
    no identity or evidence transfer.
  snapshot_sha256: d7f788858ab6b318cbd1ab1dbfdc3bd89de0f8b05206e546e3e109d858e8e77a
- evidence_id: support-2379-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/native-prep/native-current238-implemented-curation-scan-001.json
  locator: /scope; /actual_assay_tuples; /exclusion_conclusion; /applicable_conclusion;
    /limitations
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: context_only
  summary: Native performed the ignored-inclusive implemented-table scan. No matching
    LOTUS or selected assay exclusion was identified; source-quality or same-locus
    metadata is not itself a correction.
  snapshot_sha256: f0bd6d1faf8b286a7fc4718394872c3d80a754a9a094de95b693cf6a2da6bb00
  search_scope: All28 byte-current owner contexts and saved source identity fields,
    labels, slugs, full keys, owned BGC/source IDs, taxon/chemical CURIEs and both
    actual AIDs. Case-insensitive literal search of complete rows in all9 relevant
    local curation TSVs; ignored-inclusive Path.rglob enumerated all11 TSVs. This
    is the retained local implemented-table scan; no fresh request or decisions.tsv
    review.
- evidence_id: support-2379-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2379-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2379-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2379-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2379-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete saved mibig_compounds query predicate, command scope and 1 matching
    row placement(s); no rerun. Exact snapshot scope only.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
  search_scope: 'Saved mibig_compounds query only: exact complete standard_inchi_key
    equality; query="DWUHGPPFFABTIY-RLWZQHMASA-N". Complete matched or no-match result
    is retained at /contexts/21/source_scope_inventory/joins/mibig_compounds in the
    pinned local inventory; no fresh source request.'
- evidence_id: support-2379-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical lines 1350–1350; exact header fields; row_sha256=6b49505ed0dc15a6fd3f6f3ca56989404044e82ac0f9abf7aabbdbf22b9f433f
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Exact retained mibig_compounds row with all 25 fields, including blank
    cells. BGC0001140 version 5, compound 2; BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2379-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete saved chebi_structures query predicate, command scope and 1 matching
    row placement(s); no rerun. Exact snapshot scope only.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
  search_scope: 'Saved chebi_structures query only: exact complete standard_inchi_key
    equality; query="DWUHGPPFFABTIY-RLWZQHMASA-N". Complete matched or no-match result
    is retained at /contexts/21/source_scope_inventory/joins/chebi_structures in the
    pinned local inventory; no fresh source request.'
- evidence_id: support-2379-source-chebi_structures-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Physical lines 23573–23573; exact header fields; row_sha256=74f0184b1180dd82d4193231c1c38615dd7446d9f73b2d1b97f2caeb1ee8f2bb
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: 'Exact retained chebi_structures row with all 6 fields, including blank
    cells. '
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: support-2379-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete saved lotus_occurrences query predicate, command scope and 3 matching
    row placement(s); no rerun. Exact snapshot scope only.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
  search_scope: 'Saved lotus_occurrences query only: exact complete standard_inchi_key
    equality; query="DWUHGPPFFABTIY-RLWZQHMASA-N". Complete matched or no-match result
    is retained at /contexts/21/source_scope_inventory/joins/lotus_occurrences in
    the pinned local inventory; no fresh source request.'
- evidence_id: support-2379-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 1191–1191; exact header fields; row_sha256=e181c0a2f639a0f19b0d26c1844cad38882898fa10617678da8d19276d95bda3
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Exact retained lotus_occurrences row with all 6 fields, including blank
    cells. Occurrence only; not an independent producer or experiment count.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2379-source-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 1192–1192; exact header fields; row_sha256=daf162d5979d8a358a4ba9130fd3da999d3a5d8b9f5e63d9189eafbc3bcddbc3
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Exact retained lotus_occurrences row with all 6 fields, including blank
    cells. Occurrence only; not an independent producer or experiment count.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2379-source-lotus_occurrences-2
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 1193–1193; exact header fields; row_sha256=685d44a7a34b6332133e6651b7ba59b08abfd28be31055eac48770b94dd92d2e
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Exact retained lotus_occurrences row with all 6 fields, including blank
    cells. Occurrence only; not an independent producer or experiment count.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2379-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences query predicate, command scope and
    0 matching row placement(s); no rerun. Exact snapshot scope only.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
  search_scope: 'Saved cyanometdb_occurrences query only: exact complete standard_inchi_key
    equality; query="DWUHGPPFFABTIY-RLWZQHMASA-N". Complete matched or no-match result
    is retained at /contexts/21/source_scope_inventory/joins/cyanometdb_occurrences
    in the pinned local inventory; no fresh source request.'
- evidence_id: support-2379-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete saved npclassifier query predicate, command scope and 1 matching
    row placement(s); no rerun. Exact snapshot scope only.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
  search_scope: 'Saved npclassifier query only: exact complete standard_inchi_key
    equality; query="DWUHGPPFFABTIY-RLWZQHMASA-N". Complete matched or no-match result
    is retained at /contexts/21/source_scope_inventory/joins/npclassifier in the pinned
    local inventory; no fresh source request.'
- evidence_id: support-2379-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical lines 486–486; exact header fields; row_sha256=e624e88750b961212e98c6f732c35b025801b91a44895520fe180992d18774e3
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: 'Exact retained npclassifier row with all 7 fields, including blank cells. '
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2379-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete saved pubchem_bioassay query predicate, command scope and 0 matching
    row placement(s); no rerun. Exact snapshot scope only.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
  search_scope: 'Saved pubchem_bioassay query only: exact complete standard_inchi_key
    equality; query="DWUHGPPFFABTIY-RLWZQHMASA-N". Complete matched or no-match result
    is retained at /contexts/21/source_scope_inventory/joins/pubchem_bioassay in the
    pinned local inventory; no fresh source request.'
- evidence_id: support-2379-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete saved bindingdb_targets query predicate, command scope and 0 matching
    row placement(s); no rerun. Exact snapshot scope only.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
  search_scope: 'Saved bindingdb_targets query only: exact complete standard_inchi_key
    equality; query="DWUHGPPFFABTIY-RLWZQHMASA-N". Complete matched or no-match result
    is retained at /contexts/21/source_scope_inventory/joins/bindingdb_targets in
    the pinned local inventory; no fresh source request.'
- evidence_id: support-2379-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys query predicate, command scope
    and 1 matching row placement(s); no rerun. Exact snapshot scope only.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
  search_scope: 'Saved antibioticmech_inchikeys query only: exact complete standard_inchi_key
    equality; query="DWUHGPPFFABTIY-RLWZQHMASA-N". Complete matched or no-match result
    is retained at /contexts/21/source_scope_inventory/joins/antibioticmech_inchikeys
    in the pinned local inventory; no fresh source request.'
- evidence_id: support-2379-source-antibioticmech_inchikeys-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv
  locator: Physical lines 447–447; exact header fields; row_sha256=04f2d347f18ac525ee9736666eb1d2f486754a0dcdbeaa7442e4d81879034562
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Exact retained antibioticmech_inchikeys row with all 6 fields, including
    blank cells. Exact full-key/identifier/corpus-commit correspondence, not imported
    target evidence.
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
- evidence_id: support-2379-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: Complete saved chebi_origins query predicate, command scope and 1 matching
    row placement(s); no rerun. Exact snapshot scope only.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
  search_scope: 'Saved chebi_origins query only: exact chebi_id from exact full-key
    structure rows; query=["CHEBI:68241"]. Complete matched or no-match result is
    retained at /contexts/21/source_scope_inventory/joins/chebi_origins in the pinned
    local inventory; no fresh source request.'
- evidence_id: support-2379-source-chebi_origins-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Physical lines 8568–8568; exact header fields; row_sha256=2f471a30b670db9775b7ba24203e612b5684e81f14645bc71e995f3dd1fc79c5
  accessed_at: '2026-11-04T09:18:13.478278Z'
  support: supports
  summary: 'Exact retained chebi_origins row with all 7 fields, including blank cells. '
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-238/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json
  accessed_at: '2026-11-04T08:26:48.360818Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: ddb6129d9b295966cf13f1cd3dd2a7a77a2f233e19dfb56af98af964a8ed5cfc
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-238/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json
  accessed_at: '2026-11-04T08:27:14.590469Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 0c826a315a62b7ca5ace8d949bca7cafa3d6e3fc304c2051ce80758f76ac199f
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-238/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json
  accessed_at: '2026-11-04T08:27:35.132292Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-238/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json
  accessed_at: '2026-11-04T08:28:10.194681Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-238/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json
  accessed_at: '2026-11-04T08:28:22.125818Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 467d79611b8ccea3ff2d99b2028febe6f7e14eab069e304257148ed41e7e8201
assessments:
- area: identity
  topic: Retained structure and identifier correspondence
  outcome: supported
  assessment_id: support-2379-identity
  summary: The owner CHEBI:68241 carries DWUHGPPFFABTIY-RLWZQHMASA-N. The ChEBI three-star
    row, BGC0001140 version 5 compound 2 and pinned AntibioticMech row use this same
    key. The separate selected partial-key Platencin record shares a name and PubChem:44450228
    but is not an exact full-key match. Its two assay calls remain attached to that
    separate record. Both accepted stored-form diagnostics reproduce the declared
    full key; normalized identifier agreement does not independently prove natural
    identity.
  target_ids:
  - CHEBI:68241
  evidence_ids:
  - support-2379-grounding-owner
  - support-2379-chemistry
  - support-2379-query-chebi_structures
  - support-2379-direct-contexts
  - support-2379-source-mibig_compounds-0
  - support-2379-source-chebi_structures-0
  - support-2379-source-lotus_occurrences-0
  - support-2379-source-lotus_occurrences-1
  - support-2379-source-lotus_occurrences-2
  - support-2379-source-npclassifier-0
  - support-2379-source-antibioticmech_inchikeys-0
  - support-2379-source-chebi_origins-0
  dimensions:
  - name: standard_inchi_key
    value: DWUHGPPFFABTIY-RLWZQHMASA-N; exact retained full key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - support-2379-grounding-owner
    - support-2379-chemistry
    - support-2379-query-chebi_structures
    - support-2379-direct-contexts
    - support-2379-source-mibig_compounds-0
    - support-2379-source-chebi_structures-0
    - support-2379-source-lotus_occurrences-0
    - support-2379-source-lotus_occurrences-1
    - support-2379-source-lotus_occurrences-2
    - support-2379-source-npclassifier-0
    - support-2379-source-antibioticmech_inchikeys-0
    - support-2379-source-chebi_origins-0
  - name: grounding_scope
    value: The owner CHEBI:68241 carries DWUHGPPFFABTIY-RLWZQHMASA-N. The ChEBI three-star
      row, BGC0001140 version 5 compound 2 and pinned AntibioticMech row use this
      same key. The separate selected partial-key Platencin record shares a name and
      PubChem:44450228 but is not an exact full-key match. Its two assay calls remain
      attached to that separate record. Both accepted stored-form diagnostics reproduce
      the declared full key; normalized identifier agreement does not independently
      prove natural identity.
    definition: Retained local grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2379-grounding-owner
    - support-2379-chemistry
    - support-2379-query-chebi_structures
    - support-2379-direct-contexts
    - support-2379-source-mibig_compounds-0
    - support-2379-source-chebi_structures-0
    - support-2379-source-lotus_occurrences-0
    - support-2379-source-lotus_occurrences-1
    - support-2379-source-lotus_occurrences-2
    - support-2379-source-npclassifier-0
    - support-2379-source-antibioticmech_inchikeys-0
    - support-2379-source-chebi_origins-0
- area: representation
  topic: Stored representation and stereochemical scope
  outcome: supported
  assessment_id: support-2379-representation
  summary: The stored pair is neutral C24H27NO6 with 31 heavy atoms and 34 bonds.
    Formula, charge, normalized Standard InChI and declared full key agree, but both
    canonical-SMILES comparisons are false and the full atom-match array is empty.
    Source C17(=O18)–N19(H) becomes InChI-derived C18(–O27H)=N24; the canonical branches
    show the corresponding amide/imidic difference. Four specified tetrahedral centers
    remain present in both forms. The additional unspecified C=N belongs to the reconstructed
    representation and does not by itself refute the source stereo_complete true flag,
    whose extractor tests undefined tetrahedral centers. The complete tables preserve
    the ketone-bearing polycyclic carbon framework and aromatic amide/imidic-linked
    carboxylic acid with two phenolic hydroxyls. No independent whole-graph or natural-form
    identity is claimed.
  target_ids:
  - CHEBI:68241
  evidence_ids:
  - support-2379-grounding-owner
  - support-2379-chemistry
  - support-2379-topology
  - support-2379-diagnostic-acceptance
  - support-2379-structure-schema
  - support-2379-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: The stored pair is neutral C24H27NO6 with 31 heavy atoms and 34 bonds.
      Formula, charge, normalized Standard InChI and declared full key agree, but
      both canonical-SMILES comparisons are false and the full atom-match array is
      empty. Source C17(=O18)–N19(H) becomes InChI-derived C18(–O27H)=N24; the canonical
      branches show the corresponding amide/imidic difference. Four specified tetrahedral
      centers remain present in both forms. The additional unspecified C=N belongs
      to the reconstructed representation and does not by itself refute the source
      stereo_complete true flag, whose extractor tests undefined tetrahedral centers.
      The complete tables preserve the ketone-bearing polycyclic carbon framework
      and aromatic amide/imidic-linked carboxylic acid with two phenolic hydroxyls.
      No independent whole-graph or natural-form identity is claimed.
    definition: Complete saved stereo, atom and bond interpretation; no new parse
      or experimental assignment.
    evidence_ids:
    - support-2379-grounding-owner
    - support-2379-chemistry
    - support-2379-topology
    - support-2379-diagnostic-acceptance
    - support-2379-structure-schema
    - support-2379-stereo-method
  - name: representation_correspondence
    value: The stored pair is neutral C24H27NO6 with 31 heavy atoms and 34 bonds.
      Formula, charge, normalized Standard InChI and declared full key agree, but
      both canonical-SMILES comparisons are false and the full atom-match array is
      empty. Source C17(=O18)–N19(H) becomes InChI-derived C18(–O27H)=N24; the canonical
      branches show the corresponding amide/imidic difference. Four specified tetrahedral
      centers remain present in both forms. The additional unspecified C=N belongs
      to the reconstructed representation and does not by itself refute the source
      stereo_complete true flag, whose extractor tests undefined tetrahedral centers.
      The complete tables preserve the ketone-bearing polycyclic carbon framework
      and aromatic amide/imidic-linked carboxylic acid with two phenolic hydroxyls.
      No independent whole-graph or natural-form identity is claimed.
    definition: Normalized identifier agreement does not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2379-grounding-owner
    - support-2379-chemistry
    - support-2379-topology
    - support-2379-diagnostic-acceptance
    - support-2379-structure-schema
    - support-2379-stereo-method
- area: provenance
  topic: Producer and locus evidence
  outcome: supported
  assessment_id: support-2379-provenance
  summary: Streptomyces platensis, NCBITaxon:58346, is recorded as BGC_CHARACTERIZED
    for the CLUSTER_DEMONSTRATED BGC0001140 locus, FJ655920.1:4531–45738, with knock-out
    and heterologous-expression methods. Shared-BGC Platensilin, Platensimycin and
    thio compounds provide direct context, each with a distinct structure key and
    compound-specific reference. Neither their identities nor activities transfer
    through cluster membership.
  target_ids:
  - CHEBI:68241
  evidence_ids:
  - support-2379-origin-owner
  - support-2379-direct-contexts
  - support-2379-source-reading
  - support-2379-source-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    value: Streptomyces platensis, NCBITaxon:58346, is recorded as BGC_CHARACTERIZED
      for the CLUSTER_DEMONSTRATED BGC0001140 locus, FJ655920.1:4531–45738, with knock-out
      and heterologous-expression methods. Shared-BGC Platensilin, Platensimycin and
      thio compounds provide direct context, each with a distinct structure key and
      compound-specific reference. Neither their identities nor activities transfer
      through cluster membership.
    definition: Producer, occurrence, species, strain and unresolved labels retain
      separate scope; cached labels are not fresh authority.
    evidence_ids:
    - support-2379-origin-owner
    - support-2379-direct-contexts
    - support-2379-source-reading
    - support-2379-source-mibig_compounds-0
  - name: producer_evidence
    value: Streptomyces platensis, NCBITaxon:58346, is recorded as BGC_CHARACTERIZED
      for the CLUSTER_DEMONSTRATED BGC0001140 locus, FJ655920.1:4531–45738, with knock-out
      and heterologous-expression methods. Shared-BGC Platensilin, Platensimycin and
      thio compounds provide direct context, each with a distinct structure key and
      compound-specific reference. Neither their identities nor activities transfer
      through cluster membership.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - support-2379-origin-owner
    - support-2379-direct-contexts
    - support-2379-source-reading
    - support-2379-source-mibig_compounds-0
  - name: locus_evidence
    value: Streptomyces platensis, NCBITaxon:58346, is recorded as BGC_CHARACTERIZED
      for the CLUSTER_DEMONSTRATED BGC0001140 locus, FJ655920.1:4531–45738, with knock-out
      and heterologous-expression methods. Shared-BGC Platensilin, Platensimycin and
      thio compounds provide direct context, each with a distinct structure key and
      compound-specific reference. Neither their identities nor activities transfer
      through cluster membership.
    definition: Source version, status, method and grade are not a complete pathway
      or fresh primary verification.
    evidence_ids:
    - support-2379-origin-owner
    - support-2379-direct-contexts
    - support-2379-source-reading
    - support-2379-source-mibig_compounds-0
- area: evidence
  topic: Citation roles
  outcome: supported
  assessment_id: support-2379-citations
  summary: PMID:17456595 is the MIBiG compound-evidence reference. Three LOTUS DOIs
    and ChEBI origin PMID:21214253 have occurrence roles. The AntibioticMech correspondence
    is pinned to corpus commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976. These retain
    their database/corpus provenance; no new publication access, sequence grounding
    or experimental verification has occurred.
  target_ids:
  - CHEBI:68241
  evidence_ids:
  - support-2379-origin-owner
  - support-2379-occurrence-activity-owner
  - support-2379-source-reading
  - support-2379-source-mibig_compounds-0
  - support-2379-source-chebi_structures-0
  - support-2379-source-lotus_occurrences-0
  - support-2379-source-lotus_occurrences-1
  - support-2379-source-lotus_occurrences-2
  - support-2379-source-npclassifier-0
  - support-2379-source-antibioticmech_inchikeys-0
  - support-2379-source-chebi_origins-0
  dimensions:
  - name: citation_scope
    value: PMID:17456595 is the MIBiG compound-evidence reference. Three LOTUS DOIs
      and ChEBI origin PMID:21214253 have occurrence roles. The AntibioticMech correspondence
      is pinned to corpus commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976. These retain
      their database/corpus provenance; no new publication access, sequence grounding
      or experimental verification has occurred.
    definition: Database provenance and occurrence citations retain distinct roles;
      no publication independence or fresh source access is assumed.
    evidence_ids:
    - support-2379-origin-owner
    - support-2379-occurrence-activity-owner
    - support-2379-source-reading
    - support-2379-source-mibig_compounds-0
    - support-2379-source-chebi_structures-0
    - support-2379-source-lotus_occurrences-0
    - support-2379-source-lotus_occurrences-1
    - support-2379-source-lotus_occurrences-2
    - support-2379-source-npclassifier-0
    - support-2379-source-antibioticmech_inchikeys-0
    - support-2379-source-chebi_origins-0
- area: evidence
  topic: Occurrence and activity scope
  outcome: supported
  assessment_id: support-2379-occurrence
  summary: Three LOTUS rows report Streptomyces platensis with distinct DOI strings.
    The ChEBI origin row adds the recorded strain context MA7327 and PMID:21214253;
    that strain detail is not generalized to all rows. The exact AntibioticMech key/identifier
    supports the retained ANTIBACTERIAL corpus summary. The ChEBI definition also
    mentions fatty-acid-synthase inhibition, but this is a retained definition claim
    rather than a newly established direct target mechanism. No PubChem assay rows
    matched this exact full key in the saved query.
  target_ids:
  - CHEBI:68241
  evidence_ids:
  - support-2379-occurrence-activity-owner
  - support-2379-direct-contexts
  - support-2379-curation-scope
  - support-2379-query-lotus_occurrences
  - support-2379-query-chebi_origins
  - support-2379-query-cyanometdb_occurrences
  - support-2379-query-pubchem_bioassay
  - support-2379-query-bindingdb_targets
  - support-2379-query-antibioticmech_inchikeys
  - support-2379-source-mibig_compounds-0
  - support-2379-source-chebi_structures-0
  - support-2379-source-lotus_occurrences-0
  - support-2379-source-lotus_occurrences-1
  - support-2379-source-lotus_occurrences-2
  - support-2379-source-npclassifier-0
  - support-2379-source-antibioticmech_inchikeys-0
  - support-2379-source-chebi_origins-0
  dimensions:
  - name: occurrence_scope
    value: Three LOTUS rows report Streptomyces platensis with distinct DOI strings.
      The ChEBI origin row adds the recorded strain context MA7327 and PMID:21214253;
      that strain detail is not generalized to all rows. The exact AntibioticMech
      key/identifier supports the retained ANTIBACTERIAL corpus summary. The ChEBI
      definition also mentions fatty-acid-synthase inhibition, but this is a retained
      definition claim rather than a newly established direct target mechanism. No
      PubChem assay rows matched this exact full key in the saved query.
    definition: Occurrence placements are not counts of independent experiments or
      demonstrated producers.
    evidence_ids:
    - support-2379-occurrence-activity-owner
    - support-2379-direct-contexts
    - support-2379-curation-scope
    - support-2379-query-lotus_occurrences
    - support-2379-query-chebi_origins
    - support-2379-query-cyanometdb_occurrences
    - support-2379-query-pubchem_bioassay
    - support-2379-query-bindingdb_targets
    - support-2379-query-antibioticmech_inchikeys
    - support-2379-source-mibig_compounds-0
    - support-2379-source-chebi_structures-0
    - support-2379-source-lotus_occurrences-0
    - support-2379-source-lotus_occurrences-1
    - support-2379-source-lotus_occurrences-2
    - support-2379-source-npclassifier-0
    - support-2379-source-antibioticmech_inchikeys-0
    - support-2379-source-chebi_origins-0
  - name: assay_target_scope
    value: Three LOTUS rows report Streptomyces platensis with distinct DOI strings.
      The ChEBI origin row adds the recorded strain context MA7327 and PMID:21214253;
      that strain detail is not generalized to all rows. The exact AntibioticMech
      key/identifier supports the retained ANTIBACTERIAL corpus summary. The ChEBI
      definition also mentions fatty-acid-synthase inhibition, but this is a retained
      definition claim rather than a newly established direct target mechanism. No
      PubChem assay rows matched this exact full key in the saved query.
    definition: Retained assay and target assertions are bounded; biosynthetic proteins
      are not pharmacological target evidence.
    evidence_ids:
    - support-2379-occurrence-activity-owner
    - support-2379-direct-contexts
    - support-2379-curation-scope
    - support-2379-query-lotus_occurrences
    - support-2379-query-chebi_origins
    - support-2379-query-cyanometdb_occurrences
    - support-2379-query-pubchem_bioassay
    - support-2379-query-bindingdb_targets
    - support-2379-query-antibioticmech_inchikeys
    - support-2379-source-mibig_compounds-0
    - support-2379-source-chebi_structures-0
    - support-2379-source-lotus_occurrences-0
    - support-2379-source-lotus_occurrences-1
    - support-2379-source-lotus_occurrences-2
    - support-2379-source-npclassifier-0
    - support-2379-source-antibioticmech_inchikeys-0
    - support-2379-source-chebi_origins-0
- area: consistency
  topic: Versioned classification applicability
  outcome: supported
  assessment_id: support-2379-classification
  summary: The separately asserted Aromatic amino acid/simple benzoic acid and Diterpenoid
    classes fit the retained aromatic carboxylic-acid/amide and terpenoid-framework
    source context. NPClassifier’s versioned Terpenoids / Diterpenoids / Platensimycin
    and Platencins prediction remains a different evidence layer. Complete tables
    contain no identified sugar residue or glycosidic linkage, supporting is_glycoside
    false within the stored topology. Neither those observations nor the ANTIBACTERIAL
    corpus class establishes a complete biosynthetic or pharmacological mechanism.
  target_ids:
  - CHEBI:68241
  evidence_ids:
  - support-2379-classification-owner
  - support-2379-chemistry
  - support-2379-topology
  - support-2379-structure-schema
  - support-2379-classification-seeder
  - support-2379-source-mibig_compounds-0
  - support-2379-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: The separately asserted Aromatic amino acid/simple benzoic acid and Diterpenoid
      classes fit the retained aromatic carboxylic-acid/amide and terpenoid-framework
      source context. NPClassifier’s versioned Terpenoids / Diterpenoids / Platensimycin
      and Platencins prediction remains a different evidence layer. Complete tables
      contain no identified sugar residue or glycosidic linkage, supporting is_glycoside
      false within the stored topology. Neither those observations nor the ANTIBACTERIAL
      corpus class establishes a complete biosynthetic or pharmacological mechanism.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct evidence types.
    evidence_ids:
    - support-2379-classification-owner
    - support-2379-chemistry
    - support-2379-topology
    - support-2379-structure-schema
    - support-2379-classification-seeder
    - support-2379-source-mibig_compounds-0
    - support-2379-source-npclassifier-0
- area: completeness
  topic: Review completion
  outcome: unknown
  assessment_id: support-2379-completion
  summary: The complete owner/history, accepted canonical intake, retained source
    rows and both saved molecular forms were personally read. All four mechanism-related
    owner roots are absent, so no maintained-reader invocation applies to this owner.
    Full QC, complete OAK authority coverage and fresh external verification remain
    unavailable. No supported source-edit finding or action is established; completion
    remains partial.
  target_ids:
  - CHEBI:68241
  evidence_ids:
  - support-2379-owner
  - support-2379-capture
  - support-2379-intake
  - support-2379-intake-acceptance
  - support-2379-inventory-acceptance
  - support-2379-plan
  - support-2379-plan-acceptance
  - support-2379-source-reading
  - support-2379-diagnostic-acceptance
  - support-2379-diagnostic-execution
  - support-2379-diagnostic-warnings
  - support-2379-review-profile
  dimensions:
  - name: review_completion
    value: The complete owner/history, accepted canonical intake, retained source
      rows and both saved molecular forms were personally read. All four mechanism-related
      owner roots are absent, so no maintained-reader invocation applies to this owner.
      Full QC, complete OAK authority coverage and fresh external verification remain
      unavailable. No supported source-edit finding or action is established; completion
      remains partial.
    definition: Completion reflects actual access and required-check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - support-2379-owner
    - support-2379-capture
    - support-2379-intake
    - support-2379-intake-acceptance
    - support-2379-inventory-acceptance
    - support-2379-plan
    - support-2379-plan-acceptance
    - support-2379-source-reading
    - support-2379-diagnostic-acceptance
    - support-2379-diagnostic-execution
    - support-2379-diagnostic-warnings
    - support-2379-review-profile
findings: []
actions: []
limitations:
- All evidence is retained locally. Natural identity, primary publications, current
  taxonomy and external identifiers were not freshly verified.
- Full QC, complete OAK authority coverage and fresh external verification remain
  unavailable; local parsing and gates do not replace them.
- Matching normalized identifiers do not prove complete fixed-graph identity. All
  false canonical comparisons and empty atom maps are preserved.
- Two original omitted-undefined-stereo warnings remain global and are not assigned
  to any owner.
- Occurrences, producer grades, locus support, model predictions, assay calls and
  sibling-corpus assertions retain separate scope. Shared names, loci or identifiers
  do not transfer claims.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support personally read five complete owners/history, all five actual intakes, 45
  selected source query frames and 22 full positive rows/248 fields. Prior companion
  and complementary source readings remain explicitly attributed through accepted
  notes.
- 'Complete personal paired-table reading covers all ten forms: 272 atom rows and
  298 bond rows plus every scalar, ring, stereo, motif and mapping field, using lossless
  constant-column factoring. No new molecular parse.'
- ROOT operated the original diagnostic and intakes; Native prepared guarded methods.
  This scientific authoring invoked no target or external request.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-238
```
