# Local evidence review: Venemycin

- Review: 20261103T133012Z-venemycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T13:02:50.375281Z
- Finished UTC: 2026-11-03T13:30:12.811289Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Venemycin: qualified partial review of retained identity, evidence grades, taxonomy and complete saved molecular tables.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2226; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-9ec6c64697 | data/natural_products/shikimates_and_phenylpropanoids/venemycin.yaml | generated | Venemycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-9ec6c64697 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-9ec6c64697 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-9ec6c64697 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-9ec6c64697 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-9ec6c64697 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-9ec6c64697 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-9ec6c64697 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-9ec6c64697 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding scope

identity: supported. Targets: naturalproductmech:mibig-9ec6c64697.

Venemycin retains the minted MIBiG structure concept BGC0001819 version 3, compound_index=1, and NPAtlas NPA028319. The exact full key HNPIAKGZUJZKED-UHFFFAOYSA-N is shared by the stored forms and the retained MIBiG, LOTUS and NPClassifier rows. The saved exact-key ChEBI query returns no row; this bounds the generated MINTED grounding note to the inspected snapshot and does not establish current global identifier absence. MIBiG marks the entry active, questionable quality and unknown completeness; an active deposit is not an independent identity verification.

### Paired representations and stereochemical limits

representation: supported. Targets: naturalproductmech:mibig-9ec6c64697.

Both saved forms give neutral C11H8O5 with 16 atoms and 17 bonds, matching full InChI/key and both canonical SMILES. The saved chirality-aware atom-count match is complete, while full_graph_identity_established remains false. Neither form identifies potential tetrahedral or double-bond stereochemistry; the literal stereo_complete:true is consistent with that saved scope. Equality of derived representations does not prove isolation identity or independent full-graph equivalence.

### Producer, occurrence and locus evidence grades

provenance: supported. Targets: naturalproductmech:mibig-9ec6c64697.

MIBiG BGC0001819 version 3 retains Streptomyces venezuelae NCBITaxon:54571 as SOURCE_ASSERTION. Its PKS locus on NZ_CP018074.1 spans 519875–549437 with no stated locus-evidence method and CLUSTER_UNSTATED. The LOTUS occurrence uses the same species, but occurrence and production remain different claims. The whole cached stanza supplies venezuelae/venezuelensis naming context, not live taxonomy validation. Five curation scan hits on this shared taxon belong to BGC0000094/BGC0000898, so their ATCC 15439 strain must not transfer to Venemycin.

### Citation placement and historical verification scope

evidence: supported. Targets: naturalproductmech:mibig-9ec6c64697.

The MIBiG citation DOI:10.1002/cbic.201600396 is explicitly COMPOUND_EVIDENCE and is retained as DATABASE_ASSERTION on the producer and locus. The LOTUS DOI differs only in case and may denote the same publication; the two retained routes do not demonstrate independent experimental replication. No article text, original sequence, identifier service or API response was inspected in this review.

### Occurrence, assay and companion boundaries

scope: supported. Targets: naturalproductmech:mibig-9ec6c64697.

One written LOTUS species occurrence is backed by one retained exact-key row. The saved PubChem, BindingDB, AntibioticMech and CyanoMetDB queries have no matching rows in their exact admitted predicates; the Chebi-origin query is empty because there is no matched structure identifier. This is not a claim that Venemycin lacks activity or wider occurrences. There are no selected direct companions or mechanism roots in the inspected owner.

### Computed classification and full-table topology limits

other: supported. Targets: naturalproductmech:mibig-9ec6c64697.

The saved graph contains a phenyl ring with two hydroxyls and an oxygen heterocycle bearing a third hydroxyl and C1=O0 in the SMILES indexing. Ring oxygen O15 uses aromaticized bonds to C1/C6, so the empty generic SINGLE-bond ester and C–O–C lists do not exclude the pyrone/lactone topology. There is no candidate C5O sugar ring or glycosidic substituent in these tables. NPClassifier version npclassifier.gnps2.org@2026-09-07 reports Shikimates and Phenylpropanoids with empty finer classes and is_glycoside:false; this prediction is separate from the retained PKS BGC assertion and does not determine biosynthetic origin.

### Partial completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-9ec6c64697.

The actual 37-input intake, admitted source plan and original two-form computation support a partial scientific review. The selected owner has no pathway, causal graph, component reference or molecular-target root, so a maintained mechanism reader is not applicable. Missing selected mechanism annotation is a completeness boundary, not proof of biological absence. Five local gates passed, while FullQC, complete OAK and external primary-source verification remain unavailable. Generated content remains owned by the source inventories/extractors/seeder; no scientific source record or history was edited.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2226-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/venemycin.yaml; lines 1–94 | supports | Whole current plaintext owner and all 3 curation-history events. Literal identifier naturalproductmech:mibig-9ec6c64697, label Venemycin, key HNPIAKGZUJZKED-UHFFFAOYSA-N; no new scientific verification is implied by historical events. |
| support-2226-capture | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/5/owner_document; /records/5/owner_pin | supports | Exact captured whole owner, including structure, producer/locus, occurrences, source concepts, computed classification and history. Root keys: ["identifier","label","chemical_structure","np_pathway","biosynthesis_origin","np_classification","occurrence_taxon_groups","occurrences","bgc_class","xrefs","producer_taxon_groups","producer_organisms","biosynthetic_gene_clusters","source_concepts","grounding_status","grounding_notes","curation_status","curation_history"]. No selected mechanism root or component reference is present. |
| support-2226-source-plan | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5 | supports | Complete admitted selected source context; 37 planned inputs; 0 direct companions. Nine query frames and their entire retained rows are available here; scoped matches do not establish current external completeness. |
| support-2226-intake | /private/tmp/npm-review-work/shared-next-batch223/intakes/2226-inspect-001.json; /status; /source; /targets | supports | Original canonical inspection output for the exact current selected owner, source ownership and input snapshots; no scientific verdict is supplied by inspection. |
| support-2226-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-input-plan-acceptance-001.json; /status; /plan; /notes; /inventory; /source_placements; /unique_source_paths; /per_order_counts; /selected_reader_orders | supports | ROOT accepts actual saved plan 415 placements/89 paths, exact inventory-derived maps and empty selected-reader applicability. |
| support-2226-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-intake-ready-001.json; /status; /intake_summary; /execution; /plan_acceptance; /source_placements; /unique_source_paths | supports | ROOT accepts the original ten canonical intakes and actual 415/89 input snapshots; this is execution authority, not independent scientific identity proof. |
| support-2226-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-local-diagnostics-acceptance-001.json; /status; /results; /unavailable; /all_native_gates_passed; /chemistry_DATA; /chemistry_execution | supports | ROOT accepts five local gate exits 0 and twenty parsed saved forms, with four global undefined-stereo warnings unassigned. Full QC/complete OAK/external verification remain unavailable; all_native_gates_passed is false because the complete native gate set is not available. |
| support-2226-chemistry | /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/literal_InChI_layers; /records/5/smiles; /records/5/inchi; /records/5/comparisons; /records/5/atom_correspondence | supports | Both saved forms give neutral C11H8O5 with 16 atoms and 17 bonds, matching full InChI/key and both canonical SMILES. The saved chirality-aware atom-count match is complete, while full_graph_identity_established remains false. Neither form identifies potential tetrahedral or double-bond stereochemistry; the literal stereo_complete:true is consistent with that saved scope. Equality of derived representations does not prove isolation identity or independent full-graph equivalence. |
| support-2226-topology | /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json; /records/5/smiles/computed; /records/5/inchi/computed; /records/5/atom_correspondence | supports | The saved graph contains a phenyl ring with two hydroxyls and an oxygen heterocycle bearing a third hydroxyl and C1=O0 in the SMILES indexing. Ring oxygen O15 uses aromaticized bonds to C1/C6, so the empty generic SINGLE-bond ester and C–O–C lists do not exclude the pyrone/lactone topology. There is no candidate C5O sugar ring or glycosidic substituent in these tables. |
| support-2226-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–173 | supports | structure_fields derives InChI/key and uses FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False), then sets stereo_complete from absence of ? atom-centre labels. It does not inspect potential double-bond stereo in this calculation. |
| support-2226-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 982–1019 | supports | The maintained seeder copies lead stereo_complete at line 995, keeps source structures/keys, and stores NPClassifier versioned outputs separately at lines 1011–1019. This is source-generation logic, not fresh molecular execution. |
| support-2226-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392–425 | supports | stereo_complete description addresses undefined stereocentres; ComputedClassification is explicitly a named/versioned computed result, never a source assertion or admission reason. |
| support-2226-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; lines 35–57 | supports | Native review separates exact structure/stereochemistry, source/producer/locus/occurrence grades and computed classification; generated source ownership belongs to inventories/extractors/seeder and implemented tables, with decisions.tsv reserved. |
| support-2226-source-notes | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-scope-notes-001.json; /reading; /curation; /cautions; /totals | supports | Complete team-attributed saved source/raw/history/cache reading and bounded curation scan. The 135 exact literal tokens produced five shared-taxonomy-only producer_strains hits outside cohort BGCs, no cohort override; these are bounded local results. |
| support-2226-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/source_scope_inventory/joins/mibig_compounds | supports | Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N"; 1 retained matching rows. A zero count applies only to this captured predicate and table, not global biological or source absence. |
| support-2226-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 2137–2137; row_sha256=4a0b23ac5a31a92a86d13ddbefde4ad275e612302a31fd7a3cfbd39b7ed15b86 | supports | Complete retained source row, current exact physical frame: {"mibig_accession":"BGC0001819","entry_version":"3","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"Venemycin","compound_index":"1","smiles":"O=C1C=C(O)C=C(C2=CC(O)=CC(O)=C2)O1","standard_inchi":"InChI=1S/C11H8O5/c12-7-1-6(2-8(13)3-7)10-4-9(14)5-11(15)16-10/h1-5,12-14H","standard_inchi_key":"HNPIAKGZUJZKED-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA028319","taxon_id":"NCBITaxon:54571","taxon_label":"Streptomyces venezuelae","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"NZ_CP018074.1","locus_from":"519875","locus_to":"549437","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"DOI:10.1002/cbic.201600396","reference_basis":"COMPOUND_EVIDENCE"} |
| support-2226-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/source_scope_inventory/joins/chebi_structures | supports | Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N"; 0 retained matching rows. A zero count applies only to this captured predicate and table, not global biological or source absence. |
| support-2226-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/source_scope_inventory/joins/lotus_occurrences | supports | Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N"; 1 retained matching rows. A zero count applies only to this captured predicate and table, not global biological or source absence. |
| support-2226-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 2527–2527; row_sha256=623b6f3b7d8cc3e4ce1266a85868d6e40b20415e3bcad571caae93aa286ecc60 | supports | Complete retained source row, current exact physical frame: {"standard_inchi_key":"HNPIAKGZUJZKED-UHFFFAOYSA-N","organism_name":"Streptomyces venezuelae","taxon_id":"NCBITaxon:54571","organism_wikidata":"http://www.wikidata.org/entity/Q7623398","reference_doi":"10.1002/CBIC.201600396","structure_wikidata":"http://www.wikidata.org/entity/Q105031005"} |
| support-2226-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/source_scope_inventory/joins/cyanometdb_occurrences | supports | Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N"; 0 retained matching rows. A zero count applies only to this captured predicate and table, not global biological or source absence. |
| support-2226-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/source_scope_inventory/joins/npclassifier | supports | Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N"; 1 retained matching rows. A zero count applies only to this captured predicate and table, not global biological or source absence. |
| support-2226-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 867–867; row_sha256=a157fbd149ce964af9e48f9697f47ffa5c13abd30b0ab44bc5d40f46b200bb21 | supports | Complete retained source row, current exact physical frame: {"standard_inchi_key":"HNPIAKGZUJZKED-UHFFFAOYSA-N","smiles":"O=C1C=C(O)C=C(C2=CC(O)=CC(O)=C2)O1","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"","class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"} |
| support-2226-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/source_scope_inventory/joins/pubchem_bioassay | supports | Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N"; 0 retained matching rows. A zero count applies only to this captured predicate and table, not global biological or source absence. |
| support-2226-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/source_scope_inventory/joins/bindingdb_targets | supports | Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N"; 0 retained matching rows. A zero count applies only to this captured predicate and table, not global biological or source absence. |
| support-2226-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N"; 0 retained matching rows. A zero count applies only to this captured predicate and table, not global biological or source absence. |
| support-2226-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/source_scope_inventory/joins/chebi_origins | supports | Exact saved predicate exact chebi_id from exact full-key structure rows; query=[]; 0 retained matching rows. A zero count applies only to this captured predicate and table, not global biological or source absence. |
| support-2226-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/source_scope_inventory/source_taxa; /records/5/source_scope_inventory/forward_taxon_merge_matches; /records/5/source_scope_inventory/nonorganism_matches | supports | Saved source taxa ["NCBITaxon:54571"]; forward-merge and non-organism matches are empty in this exact context. No live taxonomy request was made. |
| support-2226-cache-54571 | /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; physical lines 25180–25184 | supports | Whole cached stanza, preserving scope and literal synonym labels: [Term]<br>id: NCBITaxon:54571<br>name: Streptomyces venezuelae<br>synonym: "Streptomyces venezuelensis" EXACT [] |
| support-2226-mechanism-scope | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/5/declared_mechanism_roots_literal; /records/5/component_paths; /records/5/literal_mechanism_inventory; /records/5/proposed_companion_paths | supports | The selected owner has no four mechanism roots/components. Exact direct companions are separately admitted as context; positive unselected annotations do not create selected maintained-reader applicability. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-223/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-223/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-223/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-223/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-223/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- FullQC and complete ontology authority coverage/OAK were unavailable; the five successful local gates do not establish scientific completeness.
- No external retrieval, live taxonomy/identifier/protein query or direct publication verification was performed. These assessments use the original saved owner-form computations; no additional molecular parses occurred during fragment authoring.
- Database citations, cached taxonomy, source evidence grades and versioned predictions retain their own scopes. Stored representation agreement does not prove natural identity, independent publication support or complete natural stereochemistry.
- No scientific source record or curation history was edited. Canonical review persistence and campaign operations remain ROOT-owned.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Selected four-root/component scope is empty; no maintained reader applies. This is annotation applicability, not biological absence.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T133012Z-venemycin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: Venemycin'
started_at: '2026-11-03T13:02:50.375281Z'
finished_at: '2026-11-03T13:30:12.811289Z'
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
summary: 'Venemycin: qualified partial review of retained identity, evidence grades,
  taxonomy and complete saved molecular tables.'
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/venemycin.yaml
    sha256: 1194896fbb8ae1d0ad75e0b2f2f775dd89ff8b3fc39eada4d20e325171e11565
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
  selection: Campaign path order 2226; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-9ec6c64697
targets:
- target_id: naturalproductmech:mibig-9ec6c64697
  path: data/natural_products/shikimates_and_phenylpropanoids/venemycin.yaml
  label: Venemycin
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
  - naturalproductmech:mibig-9ec6c64697
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/s2507.yaml
    data/natural_products/shikimates_and_phenylpropanoids/semivioxanthin.yaml data/natural_products/shikimates_and_phenylpropanoids/stipitatic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/sungeidine-d.yaml data/natural_products/shikimates_and_phenylpropanoids/tropodithietic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/venemycin.yaml data/natural_products/shikimates_and_phenylpropanoids/xenocoumacin-1.yaml
    data/natural_products/shikimates_and_phenylpropanoids/xenocoumacin-ii.yaml data/natural_products/shikimates_and_phenylpropanoids/z-6-undecenyltyrazolone.yaml
    data/natural_products/terpenoids/1-epibotrydial.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-223/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-9ec6c64697
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-223/validate-all-001.tsv
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
  - naturalproductmech:mibig-9ec6c64697
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
  - naturalproductmech:mibig-9ec6c64697
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
  - naturalproductmech:mibig-9ec6c64697
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-223/review-queue-001.tsv
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
  - naturalproductmech:mibig-9ec6c64697
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-9ec6c64697
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-9ec6c64697
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2226-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/venemycin.yaml
  locator: lines 1–94
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Whole current plaintext owner and all 3 curation-history events. Literal
    identifier naturalproductmech:mibig-9ec6c64697, label Venemycin, key HNPIAKGZUJZKED-UHFFFAOYSA-N;
    no new scientific verification is implied by historical events.
  snapshot_sha256: 1194896fbb8ae1d0ad75e0b2f2f775dd89ff8b3fc39eada4d20e325171e11565
- evidence_id: support-2226-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/5/owner_document; /records/5/owner_pin
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: 'Exact captured whole owner, including structure, producer/locus, occurrences,
    source concepts, computed classification and history. Root keys: ["identifier","label","chemical_structure","np_pathway","biosynthesis_origin","np_classification","occurrence_taxon_groups","occurrences","bgc_class","xrefs","producer_taxon_groups","producer_organisms","biosynthetic_gene_clusters","source_concepts","grounding_status","grounding_notes","curation_status","curation_history"].
    No selected mechanism root or component reference is present.'
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: support-2226-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Complete admitted selected source context; 37 planned inputs; 0 direct
    companions. Nine query frames and their entire retained rows are available here;
    scoped matches do not establish current external completeness.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch223/intakes/2226-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Original canonical inspection output for the exact current selected owner,
    source ownership and input snapshots; no scientific verdict is supplied by inspection.
  snapshot_sha256: 5507923ef65d281a45363fcb8c51b09cfb0955fba94a6b00a9b658f402261c79
- evidence_id: support-2226-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-input-plan-acceptance-001.json
  locator: /status; /plan; /notes; /inventory; /source_placements; /unique_source_paths;
    /per_order_counts; /selected_reader_orders
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: ROOT accepts actual saved plan 415 placements/89 paths, exact inventory-derived
    maps and empty selected-reader applicability.
  snapshot_sha256: 4428e2ef161f4bb098750e9bbcdd4dd8841c2332e7bc64b01c75f1cc8aacdaf0
- evidence_id: support-2226-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-intake-ready-001.json
  locator: /status; /intake_summary; /execution; /plan_acceptance; /source_placements;
    /unique_source_paths
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: ROOT accepts the original ten canonical intakes and actual 415/89 input
    snapshots; this is execution authority, not independent scientific identity proof.
  snapshot_sha256: f4a1f4b715e664d404565e45fe7359127911e5c1349b6e9f0df7c7ce4a4519a7
- evidence_id: support-2226-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-local-diagnostics-acceptance-001.json
  locator: /status; /results; /unavailable; /all_native_gates_passed; /chemistry_DATA;
    /chemistry_execution
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: ROOT accepts five local gate exits 0 and twenty parsed saved forms, with
    four global undefined-stereo warnings unassigned. Full QC/complete OAK/external
    verification remain unavailable; all_native_gates_passed is false because the
    complete native gate set is not available.
  snapshot_sha256: 05cfab1ce4207e65f6e1a2f6f010bb822ee4db74b3c8277597c5b7707e04fb7a
- evidence_id: support-2226-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/literal_InChI_layers; /records/5/smiles;
    /records/5/inchi; /records/5/comparisons; /records/5/atom_correspondence
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Both saved forms give neutral C11H8O5 with 16 atoms and 17 bonds, matching
    full InChI/key and both canonical SMILES. The saved chirality-aware atom-count
    match is complete, while full_graph_identity_established remains false. Neither
    form identifies potential tetrahedral or double-bond stereochemistry; the literal
    stereo_complete:true is consistent with that saved scope. Equality of derived
    representations does not prove isolation identity or independent full-graph equivalence.
  snapshot_sha256: 1723f79377c00369ddbb345f4b472f98b3ef855db093e27f59998345d4779937
- evidence_id: support-2226-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/smiles/computed; /records/5/inchi/computed; /records/5/atom_correspondence
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: The saved graph contains a phenyl ring with two hydroxyls and an oxygen
    heterocycle bearing a third hydroxyl and C1=O0 in the SMILES indexing. Ring oxygen
    O15 uses aromaticized bonds to C1/C6, so the empty generic SINGLE-bond ester and
    C–O–C lists do not exclude the pyrone/lactone topology. There is no candidate
    C5O sugar ring or glycosidic substituent in these tables.
  snapshot_sha256: 1723f79377c00369ddbb345f4b472f98b3ef855db093e27f59998345d4779937
- evidence_id: support-2226-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–173
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: structure_fields derives InChI/key and uses FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False),
    then sets stereo_complete from absence of ? atom-centre labels. It does not inspect
    potential double-bond stereo in this calculation.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2226-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 982–1019
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: The maintained seeder copies lead stereo_complete at line 995, keeps source
    structures/keys, and stores NPClassifier versioned outputs separately at lines
    1011–1019. This is source-generation logic, not fresh molecular execution.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2226-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 392–425
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: stereo_complete description addresses undefined stereocentres; ComputedClassification
    is explicitly a named/versioned computed result, never a source assertion or admission
    reason.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2226-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: lines 35–57
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Native review separates exact structure/stereochemistry, source/producer/locus/occurrence
    grades and computed classification; generated source ownership belongs to inventories/extractors/seeder
    and implemented tables, with decisions.tsv reserved.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2226-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-scope-notes-001.json
  locator: /reading; /curation; /cautions; /totals
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Complete team-attributed saved source/raw/history/cache reading and bounded
    curation scan. The 135 exact literal tokens produced five shared-taxonomy-only
    producer_strains hits outside cohort BGCs, no cohort override; these are bounded
    local results.
  snapshot_sha256: 589a3b0bfdd9afec556e285580c4102a2e3fa8d9735e3364d7ea42d9827eee41
- evidence_id: support-2226-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N";
    1 retained matching rows. A zero count applies only to this captured predicate
    and table, not global biological or source absence.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 2137–2137; row_sha256=4a0b23ac5a31a92a86d13ddbefde4ad275e612302a31fd7a3cfbd39b7ed15b86
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: 'Complete retained source row, current exact physical frame: {"mibig_accession":"BGC0001819","entry_version":"3","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"Venemycin","compound_index":"1","smiles":"O=C1C=C(O)C=C(C2=CC(O)=CC(O)=C2)O1","standard_inchi":"InChI=1S/C11H8O5/c12-7-1-6(2-8(13)3-7)10-4-9(14)5-11(15)16-10/h1-5,12-14H","standard_inchi_key":"HNPIAKGZUJZKED-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"npatlas:NPA028319","taxon_id":"NCBITaxon:54571","taxon_label":"Streptomyces
    venezuelae","bgc_classes":"PKS","bgc_subclasses":"Unknown","genome_accession":"NZ_CP018074.1","locus_from":"519875","locus_to":"549437","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"DOI:10.1002/cbic.201600396","reference_basis":"COMPOUND_EVIDENCE"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2226-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N";
    0 retained matching rows. A zero count applies only to this captured predicate
    and table, not global biological or source absence.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N";
    1 retained matching rows. A zero count applies only to this captured predicate
    and table, not global biological or source absence.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 2527–2527; row_sha256=623b6f3b7d8cc3e4ce1266a85868d6e40b20415e3bcad571caae93aa286ecc60
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: 'Complete retained source row, current exact physical frame: {"standard_inchi_key":"HNPIAKGZUJZKED-UHFFFAOYSA-N","organism_name":"Streptomyces
    venezuelae","taxon_id":"NCBITaxon:54571","organism_wikidata":"http://www.wikidata.org/entity/Q7623398","reference_doi":"10.1002/CBIC.201600396","structure_wikidata":"http://www.wikidata.org/entity/Q105031005"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2226-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N";
    0 retained matching rows. A zero count applies only to this captured predicate
    and table, not global biological or source absence.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N";
    1 retained matching rows. A zero count applies only to this captured predicate
    and table, not global biological or source absence.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 867–867; row_sha256=a157fbd149ce964af9e48f9697f47ffa5c13abd30b0ab44bc5d40f46b200bb21
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: 'Complete retained source row, current exact physical frame: {"standard_inchi_key":"HNPIAKGZUJZKED-UHFFFAOYSA-N","smiles":"O=C1C=C(O)C=C(C2=CC(O)=CC(O)=C2)O1","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"","class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2226-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N";
    0 retained matching rows. A zero count applies only to this captured predicate
    and table, not global biological or source absence.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N";
    0 retained matching rows. A zero count applies only to this captured predicate
    and table, not global biological or source absence.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Exact saved predicate exact complete standard_inchi_key equality; query="HNPIAKGZUJZKED-UHFFFAOYSA-N";
    0 retained matching rows. A zero count applies only to this captured predicate
    and table, not global biological or source absence.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Exact saved predicate exact chebi_id from exact full-key structure rows;
    query=[]; 0 retained matching rows. A zero count applies only to this captured
    predicate and table, not global biological or source absence.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/source_taxa; /records/5/source_scope_inventory/forward_taxon_merge_matches;
    /records/5/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: Saved source taxa ["NCBITaxon:54571"]; forward-merge and non-organism matches
    are empty in this exact context. No live taxonomy request was made.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: support-2226-cache-54571
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: physical lines 25180–25184
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: 'Whole cached stanza, preserving scope and literal synonym labels: [Term]

    id: NCBITaxon:54571

    name: Streptomyces venezuelae

    synonym: "Streptomyces venezuelensis" EXACT []'
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: support-2226-mechanism-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/5/declared_mechanism_roots_literal; /records/5/component_paths;
    /records/5/literal_mechanism_inventory; /records/5/proposed_companion_paths
  accessed_at: '2026-11-03T13:23:57.266899Z'
  support: supports
  summary: The selected owner has no four mechanism roots/components. Exact direct
    companions are separately admitted as context; positive unselected annotations
    do not create selected maintained-reader applicability.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:04:37.883893Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 66324cb2f94b0ce47e3f280f083307555671c644c60bd8f537eca77bd779fb7e
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:05:07.558356Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 57dad69fca1e4915ddaa2cfc5cf058591111722e4e624616dadf9a79e2ddb244
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:05:29.643887Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:06:05.240084Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:06:18.573110Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: cfbaccb0dbd803cbeac03b9148b9355a7e6393913f208ea1a9c6d5c53927cf9b
assessments:
- assessment_id: support-2226-A1
  area: identity
  topic: Exact structure concept and grounding scope
  outcome: supported
  summary: Venemycin retains the minted MIBiG structure concept BGC0001819 version
    3, compound_index=1, and NPAtlas NPA028319. The exact full key HNPIAKGZUJZKED-UHFFFAOYSA-N
    is shared by the stored forms and the retained MIBiG, LOTUS and NPClassifier rows.
    The saved exact-key ChEBI query returns no row; this bounds the generated MINTED
    grounding note to the inspected snapshot and does not establish current global
    identifier absence. MIBiG marks the entry active, questionable quality and unknown
    completeness; an active deposit is not an independent identity verification.
  target_ids:
  - naturalproductmech:mibig-9ec6c64697
  evidence_ids:
  - support-2226-owner
  - support-2226-capture
  - support-2226-source-plan
  - support-2226-query-mibig_compounds
  - support-2226-query-chebi_structures
  - support-2226-row-mibig_compounds-0
  - support-2226-chemistry
  dimensions:
  - name: standard_inchi_key
    value: HNPIAKGZUJZKED-UHFFFAOYSA-N
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-owner
    - support-2226-capture
    - support-2226-source-plan
    - support-2226-query-mibig_compounds
    - support-2226-query-chebi_structures
    - support-2226-row-mibig_compounds-0
    - support-2226-chemistry
  - name: grounding_scope
    value: Minted MIBiG BGC0001819 version 3, source compound_index=1; exact-key ChEBI
      snapshot query empty; natural identity not independently established.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-owner
    - support-2226-capture
    - support-2226-source-plan
    - support-2226-query-mibig_compounds
    - support-2226-query-chebi_structures
    - support-2226-row-mibig_compounds-0
    - support-2226-chemistry
- assessment_id: support-2226-A2
  area: representation
  topic: Paired representations and stereochemical limits
  outcome: supported
  summary: Both saved forms give neutral C11H8O5 with 16 atoms and 17 bonds, matching
    full InChI/key and both canonical SMILES. The saved chirality-aware atom-count
    match is complete, while full_graph_identity_established remains false. Neither
    form identifies potential tetrahedral or double-bond stereochemistry; the literal
    stereo_complete:true is consistent with that saved scope. Equality of derived
    representations does not prove isolation identity or independent full-graph equivalence.
  target_ids:
  - naturalproductmech:mibig-9ec6c64697
  evidence_ids:
  - support-2226-capture
  - support-2226-chemistry
  - support-2226-stereo-method
  - support-2226-seeder
  - support-2226-structure-schema
  - support-2226-diagnostic-acceptance
  dimensions:
  - name: stereochemical_resolution
    value: No potential stereogenic unit detected in either saved form; literal true
      flag has this scope.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-capture
    - support-2226-chemistry
    - support-2226-stereo-method
    - support-2226-seeder
    - support-2226-structure-schema
    - support-2226-diagnostic-acceptance
  - name: representation_correspondence
    value: All ten comparisons true; complete atom-count map; independent full-graph
      identity false.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-capture
    - support-2226-chemistry
    - support-2226-stereo-method
    - support-2226-seeder
    - support-2226-structure-schema
    - support-2226-diagnostic-acceptance
- assessment_id: support-2226-A3
  area: provenance
  topic: Producer, occurrence and locus evidence grades
  outcome: supported
  summary: MIBiG BGC0001819 version 3 retains Streptomyces venezuelae NCBITaxon:54571
    as SOURCE_ASSERTION. Its PKS locus on NZ_CP018074.1 spans 519875–549437 with no
    stated locus-evidence method and CLUSTER_UNSTATED. The LOTUS occurrence uses the
    same species, but occurrence and production remain different claims. The whole
    cached stanza supplies venezuelae/venezuelensis naming context, not live taxonomy
    validation. Five curation scan hits on this shared taxon belong to BGC0000094/BGC0000898,
    so their ATCC 15439 strain must not transfer to Venemycin.
  target_ids:
  - naturalproductmech:mibig-9ec6c64697
  evidence_ids:
  - support-2226-capture
  - support-2226-taxonomy-routes
  - support-2226-source-notes
  - support-2226-row-mibig_compounds-0
  - support-2226-row-lotus_occurrences-0
  - support-2226-cache-54571
  dimensions:
  - name: taxon_and_strain_scope
    value: MIBiG BGC0001819 version 3 retains Streptomyces venezuelae NCBITaxon:54571
      as SOURCE_ASSERTION. Its PKS locus on NZ_CP018074.1 spans 519875–549437 with
      no stated locus-evidence method and CLUSTER_UNSTATED. The LOTUS occurrence uses
      the same species, but occurrence and production remain different claims. The
      whole cached stanza supplies venezuelae/venezuelensis naming context, not live
      taxonomy validation. Five curation scan hits on this shared taxon belong to
      BGC0000094/BGC0000898, so their ATCC 15439 strain must not transfer to Venemycin.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-capture
    - support-2226-taxonomy-routes
    - support-2226-source-notes
    - support-2226-row-mibig_compounds-0
    - support-2226-row-lotus_occurrences-0
    - support-2226-cache-54571
  - name: producer_evidence_tier
    value: SOURCE_ASSERTION
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-capture
    - support-2226-taxonomy-routes
    - support-2226-source-notes
    - support-2226-row-mibig_compounds-0
    - support-2226-row-lotus_occurrences-0
    - support-2226-cache-54571
  - name: locus_evidence_tier
    value: CLUSTER_UNSTATED
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-capture
    - support-2226-taxonomy-routes
    - support-2226-source-notes
    - support-2226-row-mibig_compounds-0
    - support-2226-row-lotus_occurrences-0
    - support-2226-cache-54571
- assessment_id: support-2226-A4
  area: evidence
  topic: Citation placement and historical verification scope
  outcome: supported
  summary: The MIBiG citation DOI:10.1002/cbic.201600396 is explicitly COMPOUND_EVIDENCE
    and is retained as DATABASE_ASSERTION on the producer and locus. The LOTUS DOI
    differs only in case and may denote the same publication; the two retained routes
    do not demonstrate independent experimental replication. No article text, original
    sequence, identifier service or API response was inspected in this review.
  target_ids:
  - naturalproductmech:mibig-9ec6c64697
  evidence_ids:
  - support-2226-capture
  - support-2226-source-notes
  - support-2226-row-mibig_compounds-0
  - support-2226-row-lotus_occurrences-0
  dimensions:
  - name: citation_scope
    value: The MIBiG citation DOI:10.1002/cbic.201600396 is explicitly COMPOUND_EVIDENCE
      and is retained as DATABASE_ASSERTION on the producer and locus. The LOTUS DOI
      differs only in case and may denote the same publication; the two retained routes
      do not demonstrate independent experimental replication. No article text, original
      sequence, identifier service or API response was inspected in this review.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-capture
    - support-2226-source-notes
    - support-2226-row-mibig_compounds-0
    - support-2226-row-lotus_occurrences-0
- assessment_id: support-2226-A5
  area: scope
  topic: Occurrence, assay and companion boundaries
  outcome: supported
  summary: One written LOTUS species occurrence is backed by one retained exact-key
    row. The saved PubChem, BindingDB, AntibioticMech and CyanoMetDB queries have
    no matching rows in their exact admitted predicates; the Chebi-origin query is
    empty because there is no matched structure identifier. This is not a claim that
    Venemycin lacks activity or wider occurrences. There are no selected direct companions
    or mechanism roots in the inspected owner.
  target_ids:
  - naturalproductmech:mibig-9ec6c64697
  evidence_ids:
  - support-2226-capture
  - support-2226-mechanism-scope
  - support-2226-query-mibig_compounds
  - support-2226-query-chebi_structures
  - support-2226-query-lotus_occurrences
  - support-2226-query-cyanometdb_occurrences
  - support-2226-query-npclassifier
  - support-2226-query-pubchem_bioassay
  - support-2226-query-bindingdb_targets
  - support-2226-query-antibioticmech_inchikeys
  - support-2226-query-chebi_origins
  - support-2226-row-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    value: One written LOTUS species occurrence is backed by one retained exact-key
      row. The saved PubChem, BindingDB, AntibioticMech and CyanoMetDB queries have
      no matching rows in their exact admitted predicates; the Chebi-origin query
      is empty because there is no matched structure identifier. This is not a claim
      that Venemycin lacks activity or wider occurrences. There are no selected direct
      companions or mechanism roots in the inspected owner.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-capture
    - support-2226-mechanism-scope
    - support-2226-query-mibig_compounds
    - support-2226-query-chebi_structures
    - support-2226-query-lotus_occurrences
    - support-2226-query-cyanometdb_occurrences
    - support-2226-query-npclassifier
    - support-2226-query-pubchem_bioassay
    - support-2226-query-bindingdb_targets
    - support-2226-query-antibioticmech_inchikeys
    - support-2226-query-chebi_origins
    - support-2226-row-lotus_occurrences-0
  - name: assay_scope
    value: No selected matching PubChem/BindingDB/AntibioticMech rows in admitted
      predicates; no biological inactivity claim.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-capture
    - support-2226-mechanism-scope
    - support-2226-query-mibig_compounds
    - support-2226-query-chebi_structures
    - support-2226-query-lotus_occurrences
    - support-2226-query-cyanometdb_occurrences
    - support-2226-query-npclassifier
    - support-2226-query-pubchem_bioassay
    - support-2226-query-bindingdb_targets
    - support-2226-query-antibioticmech_inchikeys
    - support-2226-query-chebi_origins
    - support-2226-row-lotus_occurrences-0
- assessment_id: support-2226-A6
  area: other
  topic: Computed classification and full-table topology limits
  outcome: supported
  summary: The saved graph contains a phenyl ring with two hydroxyls and an oxygen
    heterocycle bearing a third hydroxyl and C1=O0 in the SMILES indexing. Ring oxygen
    O15 uses aromaticized bonds to C1/C6, so the empty generic SINGLE-bond ester and
    C–O–C lists do not exclude the pyrone/lactone topology. There is no candidate
    C5O sugar ring or glycosidic substituent in these tables. NPClassifier version
    npclassifier.gnps2.org@2026-09-07 reports Shikimates and Phenylpropanoids with
    empty finer classes and is_glycoside:false; this prediction is separate from the
    retained PKS BGC assertion and does not determine biosynthetic origin.
  target_ids:
  - naturalproductmech:mibig-9ec6c64697
  evidence_ids:
  - support-2226-capture
  - support-2226-topology
  - support-2226-structure-schema
  - support-2226-seeder
  - support-2226-row-npclassifier-0
  - support-2226-row-mibig_compounds-0
  dimensions:
  - name: computed_classification
    value: The saved graph contains a phenyl ring with two hydroxyls and an oxygen
      heterocycle bearing a third hydroxyl and C1=O0 in the SMILES indexing. Ring
      oxygen O15 uses aromaticized bonds to C1/C6, so the empty generic SINGLE-bond
      ester and C–O–C lists do not exclude the pyrone/lactone topology. There is no
      candidate C5O sugar ring or glycosidic substituent in these tables. NPClassifier
      version npclassifier.gnps2.org@2026-09-07 reports Shikimates and Phenylpropanoids
      with empty finer classes and is_glycoside:false; this prediction is separate
      from the retained PKS BGC assertion and does not determine biosynthetic origin.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-capture
    - support-2226-topology
    - support-2226-structure-schema
    - support-2226-seeder
    - support-2226-row-npclassifier-0
    - support-2226-row-mibig_compounds-0
- assessment_id: support-2226-A7
  area: completeness
  topic: Partial completion and maintained ownership
  outcome: unknown
  summary: The actual 37-input intake, admitted source plan and original two-form
    computation support a partial scientific review. The selected owner has no pathway,
    causal graph, component reference or molecular-target root, so a maintained mechanism
    reader is not applicable. Missing selected mechanism annotation is a completeness
    boundary, not proof of biological absence. Five local gates passed, while FullQC,
    complete OAK and external primary-source verification remain unavailable. Generated
    content remains owned by the source inventories/extractors/seeder; no scientific
    source record or history was edited.
  target_ids:
  - naturalproductmech:mibig-9ec6c64697
  evidence_ids:
  - support-2226-intake
  - support-2226-intake-acceptance
  - support-2226-plan-acceptance
  - support-2226-diagnostic-acceptance
  - support-2226-review-profile
  - support-2226-mechanism-scope
  - support-2226-source-notes
  dimensions:
  - name: review_completion
    value: The actual 37-input intake, admitted source plan and original two-form
      computation support a partial scientific review. The selected owner has no pathway,
      causal graph, component reference or molecular-target root, so a maintained
      mechanism reader is not applicable. Missing selected mechanism annotation is
      a completeness boundary, not proof of biological absence. Five local gates passed,
      while FullQC, complete OAK and external primary-source verification remain unavailable.
      Generated content remains owned by the source inventories/extractors/seeder;
      no scientific source record or history was edited.
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2226-intake
    - support-2226-intake-acceptance
    - support-2226-plan-acceptance
    - support-2226-diagnostic-acceptance
    - support-2226-review-profile
    - support-2226-mechanism-scope
    - support-2226-source-notes
findings: []
actions: []
limitations:
- FullQC and complete ontology authority coverage/OAK were unavailable; the five successful
  local gates do not establish scientific completeness.
- No external retrieval, live taxonomy/identifier/protein query or direct publication
  verification was performed. These assessments use the original saved owner-form
  computations; no additional molecular parses occurred during fragment authoring.
- Database citations, cached taxonomy, source evidence grades and versioned predictions
  retain their own scopes. Stored representation agreement does not prove natural
  identity, independent publication support or complete natural stereochemistry.
- No scientific source record or curation history was edited. Canonical review persistence
  and campaign operations remain ROOT-owned.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Selected four-root/component scope is empty; no maintained reader applies. This
  is annotation applicability, not biological absence.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-223
```
