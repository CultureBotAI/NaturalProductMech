# Local evidence review: pestalodiol E

- Review: 20261104T092726Z-pestalodiol-e
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T08:24:13.784090Z
- Finished UTC: 2026-11-04T09:27:26.474580Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Pestalodiol E has consistent retained molecular forms and a distinct full key within the multi-compound BGC0002290 entry. The saved aromatic/prenyl/alkynyl structure has no potential stereogenic elements. Locus demonstration, producer assertion and sibling compounds remain separate; completion is qualified and partial, without a source correction or transfer of companion claims.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2372; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-2b8aee01b5 | data/natural_products/terpenoids/pestalodiol-e.yaml | generated | pestalodiol E |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-2b8aee01b5 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-2b8aee01b5 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-2b8aee01b5 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-2b8aee01b5 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-2b8aee01b5 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-2b8aee01b5 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-2b8aee01b5 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-2b8aee01b5 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity/form consistency; natural identity unverified

identity: supported. Targets: naturalproductmech:mibig-2b8aee01b5.

The minted identifier naturalproductmech:mibig-2b8aee01b5 retains full key XLJZQTJROGTDLX-UHFFFAOYSA-N and MIBiG row 2782, compound_index 12 in BGC0002290 v2. That index is the inventory position, not a newly inferred paper label. The eleven direct companions have distinct full keys and remain context records, including compounds with different names, source citation bases and classifications. No compound identity, occurrence, bioactivity or structure is transferred from a companion. No ChEBI structure or additional exact-key identity authority is returned by the recorded joins.

### Stored molecular representation and stereo scope

representation: supported. Targets: naturalproductmech:mibig-2b8aee01b5.

Both saved forms are neutral C16H18O2 with 18 heavy atoms and 18 bonds; all ten original comparisons agree. The tables show one aromatic six-carbon ring, two phenolic hydroxyls, one C≡C and two nonaromatic C=C bonds. Potential-stereo lists are empty in both forms: one alkene terminates in CH2 and the other has two methyl substituents on one end, so the source slash notation does not establish an independent E/Z assignment. The true tetrahedral-completeness flag is consistent at its maintained scope. Complete atom-count correspondence is true, but full_graph_identity_established remains false and natural identity is not experimentally authenticated.

### Producer and locus evidence

provenance: supported. Targets: naturalproductmech:mibig-2b8aee01b5.

The retained producer is the literal unresolved label Biscogniauxia sp., NCBITaxon:1896107, with SOURCE_ASSERTION evidence. BGC0002290 v2 spans MT109335.1:1–37984 and is CLUSTER_DEMONSTRATED through Heterologous expression. The source class OTHER and subclass other are separate from that experimental method. A demonstrated locus does not identify an unresolved species more precisely or automatically upgrade the producer evidence basis.

### Citation authority and study scope

evidence: supported. Targets: naturalproductmech:mibig-2b8aee01b5.

MIBiG row 2782 cites PMID:32364293 at ENTRY level. The shared entry citation does not establish a compound-specific experiment for every companion. In particular, the different COMPOUND_BIOACTIVITY citation retained for compound 15 is not silently copied to Pestalodiol E. The current source entry version and each literal citation role are preserved; no primary paper has been freshly read.

### Retained occurrence and assay scope

evidence: supported. Targets: naturalproductmech:mibig-2b8aee01b5.

Neither occurrences nor occurrence_taxon_groups is written in the owner, and the three saved occurrence-source joins return no match for this context. Those bounded absences do not establish absence in nature. The recorded PubChem, BindingDB and related-corpus joins are also empty; they do not imply inactivity. Occurrences written on other BGC0002290 products remain specific to those products.

### Faithful versioned classification and bounded applicability

consistency: supported. Targets: naturalproductmech:mibig-2b8aee01b5.

The record faithfully retains NPClassifier npclassifier.gnps2.org@2026-09-07 outputs Terpenoids, Meroterpenoids, Miscellaneous meroterpenoids and is_glycoside:false. The aromatic scaffold with prenyl/alkynyl side chains supplies bounded chemical context, and the complete graph does not contain a sugar residue or glycosidic linkage. MIBiG OTHER and Heterologous expression retain their separate class and method meanings. Local structural compatibility does not independently establish biosynthetic provenance or validate every model class.

### Scientific review completion

completeness: unknown. Targets: naturalproductmech:mibig-2b8aee01b5.

Complete local owner/history, retained selected and eleven direct-companion contexts, actual intake and both original saved form tables have been reviewed. No mechanism root or maintained-reader route applies. Completion remains partial because Full QC/OAK and fresh primary, taxonomy and natural-identity verification are unavailable. No supported maintained-input correction is established.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2372-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/pestalodiol-e.yaml; Whole current owner plaintext and complete curation_history | supports | Complete current pestalodiol E owner and 2 history events; native status remains SEEDED. No source record was edited. |
| bgc-2372-capture | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/1 | supports | Whole captured owner/history supports absence of all four mechanism roots, component references and selected reader applicability. |
| bgc-2372-intake | /private/tmp/npm-review-work/shared-next-batch238/intakes/2372-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake for naturalproductmech:mibig-2b8aee01b5: 48 current input placements and complete source/curator ownership. Source and component corrections require their maintained owners, not generated pages. |
| bgc-2372-grounding-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/1/owner_document/identifier; /records/1/owner_document/label; /records/1/owner_document/chemical_structure; /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status; /records/1/owner_document/grounding_notes | supports | Retained identity, full structure/key, concepts and any unresolved discussion; local agreement is not natural-identity authentication. |
| bgc-2372-origin-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/1/owner_document/producer_taxon_groups; /records/1/owner_document/producer_organisms; /records/1/owner_document/biosynthetic_gene_clusters; /records/1/owner_document/source_concepts | supports | Retained source producer and locus grades, methods, genome scopes, entry versions and citation levels. |
| bgc-2372-classification-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/1/owner_document/np_pathway; /records/1/owner_document/np_classification; /records/1/owner_document/bgc_class; /records/1/owner_document/biosynthesis_origin | supports | Named/versioned model output and source biosynthetic classes retain separate authority. |
| bgc-2372-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/1/owner_document | supports | Whole owner supports absence of occurrences and occurrence_taxon_groups, while retaining its provenance/grounding notes. This is a snapshot absence, not absence in nature. |
| bgc-2372-assay-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/1/owner_document | supports | Whole owner has no written bioactivities, bioactivity_summary or molecular_targets. The available source snapshot does not establish inactivity. |
| bgc-2372-chemistry | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/smiles; /records/1/inchi; /records/1/comparisons; /records/1/atom_correspondence | supports | Both original stored forms parsed; all ten comparisons and complete atom-count correspondence agree. The original full_graph_identity_established remains false. This is saved-form consistency, not natural identity or an independent full-graph proof. |
| bgc-2372-topology | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence; /records/1/smiles/computed; /records/1/inchi/computed | supports | The aromatic ring bears hydroxyl oxygens SMILES O6 and O15 and two distinct side chains: aryl–C≡C–C(CH3)=CH2 and aryl–CH2–CH=C(CH3)2. All ring atoms are carbon; no cyclic ether, ester, amide, carbonyl or sugar residue is present in the saved graph. Both forms have empty potential-stereo lists. This is complete saved-representation interpretation, not reconstruction of a biosynthetic experiment. |
| bgc-2372-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-execution-001.json; /observer; /command; /started_at; /finished_at; /exit_code; /stdout; /stderr; /retries; /external_requests | supports | ROOT operated the original stored-form diagnostic once, exit 0 and no retry. Exact stream pins and original timestamps are retained. |
| bgc-2372-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /status; /DATA; /execution; /original_tools; /warnings; /limits | supports | ROOT accepts original diagnostic integrity. Two omitted-undefined-stereo warnings remain global and unassigned; they are not per-record findings. |
| bgc-2372-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch238/root-intake-acceptance-001.json; /accepted; /status; /summary; /records; /verification | supports | ROOT accepts actual ten canonical intakes and exact source alignment. Intake ownership and hashes do not themselves certify science. |
| bgc-2372-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch238/root-source-inventory-acceptance-001.json; /accepted; /status; /inventory; /verification | supports | ROOT accepts the original local extraction; complete scientific source meanings are separately attributed. |
| bgc-2372-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch238/root-input-plan-acceptance-001.json; /accepted; /status; /plan; /verification | supports | ROOT accepts exact complete plan maps and source preservation; actual intake acceptance separately supplies completed outcomes. |
| bgc-2372-plan | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-target-input-plan-001.json; /records/1 | supports | Accepted per-record plan preserves exact current inputs, direct contexts and complete source payloads, without a later silent refresh. |
| bgc-2372-source-notes | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete source/raw/history attribution: BGC 127 rows, Support 344 Phellandrene rows, and Native 305 cached stanzas plus curation. Repeated shared source reading is not counted twice. |
| bgc-2372-curation-scope | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-scope-notes-001.json; /curation; /curation_scope; /curation_source_receipt | supports | Ignored-inclusive implemented-curation scan is attributed to Native. One applicable Pentalenolactone BGC0000653 REPLACE row is distinguished from two unrelated lexical hits; no matching LOTUS or assay exclusion was found. Reserved files are not consumed corrections. |
| bgc-2372-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line1; physical lines 2782–2782, row_sha256 6ec11c326cc37a015f72b9151eb3485817537350ce694f1f05c439d8f7d5908c | supports | Complete identity/key, source class, locus version/quality, producer/locus grades, and compound-versus-entry citation roles; implemented corrections are separate. All 1 complete row placements are retained. BGC complete source reading carries. |
| bgc-2372-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line1; physical lines 2795–2795, row_sha256 822916888dedafca3e3b92e9f2ae401a7384bb35e889979544919e828213575a | supports | Complete named/versioned computed prediction, including every blank class and glycoside value; faithful ingestion is distinct from chemical applicability. All 1 complete row placements are retained. BGC complete source reading carries. |
| bgc-2372-queries | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/mibig_compounds; /contexts/14/source_scope_inventory/joins/chebi_structures; /contexts/14/source_scope_inventory/joins/lotus_occurrences; /contexts/14/source_scope_inventory/joins/cyanometdb_occurrences; /contexts/14/source_scope_inventory/joins/npclassifier; /contexts/14/source_scope_inventory/joins/pubchem_bioassay; /contexts/14/source_scope_inventory/joins/bindingdb_targets; /contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys; /contexts/14/source_scope_inventory/joins/chebi_origins | supports | All nine complete saved query frames and negative predicates: mibig_compounds=1, chebi_structures=0, lotus_occurrences=0, cyanometdb_occurrences=0, npclassifier=1, pubchem_bioassay=0, bindingdb_targets=0, antibioticmech_inchikeys=0, chebi_origins=0. No source query was replayed. |
| bgc-2372-source-routes | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/source_taxa; /contexts/14/source_scope_inventory/forward_taxon_merge_matches; /contexts/14/source_scope_inventory/nonorganism_matches; /contexts/14/source_scope_inventory/actual_assay_rows; /contexts/14/source_scope_inventory/blank_AID_sentinels; /contexts/14/source_scope_inventory/related_corpus_rows | supports | Exact selected source taxa and all route/sentinel/related lists. No actual assay, nonorganism match or source-query replay is present. The selected forward-merge route is empty. |
| bgc-2372-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/268 | supports | Complete retained local stanzas for this context (1 placements), with Native's whole-cache reading attributed. Names and exact synonyms are not fresh taxonomy or producer-strain equivalence.  |
| bgc-2372-direct-contexts | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /records/1/direct_companion_paths; /records/1/direct_companion_predicates | supports | Exact bounded direct companion membership; shared loci or references do not transfer chemical identity, stereochemistry, production or assay claims. |
| bgc-2372-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/0; /contexts/1; /contexts/2; /contexts/3; /contexts/4; /contexts/5; /contexts/6; /contexts/7; /contexts/8; /contexts/9; /contexts/10 | supports | Complete saved direct-companion source/raw/history context is carried with the original whole-reading attribution. Distinct full keys and experimental scopes remain separate. |
| bgc-2372-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines392–433 | supports | The structure flag records undefined stereocentres; computed classification is a named/versioned prediction, not a source assertion. |
| bgc-2372-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines142–173 | supports | Maintained stereo_complete checks undefined tetrahedral chiral centers; it is not fresh natural stereochemistry or a universal guarantee of all bond geometry. |
| bgc-2372-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines972–1020 | supports | The maintained seeder preserves lead source structure and named/versioned prediction fields separately; filing is not experimental biosynthetic evidence. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-238/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-238/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-238/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-238/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-238/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-238/native-current238-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. No external publication, identifier, taxonomy, assay, protein sequence or natural stereochemical assignment was refreshed.
- Full QC and complete OAK coverage remain unavailable. Local diagnostics, source joins and maintained preservation have only their stated scope.
- Shared loci, names, taxa, source references or companion records do not transfer identity, stereochemistry, production, activity or independent-study status.
- Two original undefined-stereo warnings remain global and unassigned. No molecular/YAML reparse, source query or target ran during scientific authoring.
- No source status, record or history is edited. Any later supported correction belongs to the maintained owners in the actual intake.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete first-five raw/history, actual intakes and all ten original stored forms were personally read; the forms comprise 180 atom rows and 196 bond rows plus all scalar/ring/stereo/motif/map fields. Diagnostic indices are zero-based, not biochemical locants.
- Source meanings retain exact attribution: BGC 127 non-Phellandrene rows, Support 344 Phellandrene rows, Native all305 cached stanzas and implemented curation. Complete current prior raw/history carries are in accepted notes.
- ROOT operated original activation/capture, collector/composer, intakes and molecular diagnostic. Native operated gates and the sole Pentalenolactone maintained reader. BGC authored source planning and these scientific assessments without target invocation.
- No finding/action is inferred solely from an unresolved source identity, partial stereochemistry or faithful model-applicability concern.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T092726Z-pestalodiol-e
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: pestalodiol E'
started_at: '2026-11-04T08:24:13.784090Z'
finished_at: '2026-11-04T09:27:26.474580Z'
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
summary: Pestalodiol E has consistent retained molecular forms and a distinct full
  key within the multi-compound BGC0002290 entry. The saved aromatic/prenyl/alkynyl
  structure has no potential stereogenic elements. Locus demonstration, producer assertion
  and sibling compounds remain separate; completion is qualified and partial, without
  a source correction or transfer of companion claims.
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/3-4-dihydroxy-5-polyprenylbenzoic-acid.yaml
    sha256: 81e523462ebb0540e1de3b9eb19f88bc87266f0c7a4dcabbacae3556ccbdb91d
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/4-hydroxy-3-prenylbenzoic-acid.yaml
    sha256: 7ea7276c7e9cd0e4510ea28aa8076911d173a70ec9b80bd3ae7803749a5b53de
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml
    sha256: 5b2493967d1774d28d023edd8500fbf16a14cfbe5139e0ff65abb0d471302e56
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/compound-8.yaml
    sha256: 996d80d8c8f8eb32b5ee5a074da9d5390601d56585fbacde28b84e3315a246c9
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/prenylhydroquinone.yaml
    sha256: 9e180def1be87dc17c2f604712ad8ce85162e4fb8ef3af415887e619dc1dd6ac
    role: context
  - path: data/natural_products/terpenoids/biscognienyne-b.yaml
    sha256: ed9704a4411299b7c325c3ed9017a2aeabe6cfcb5600f5a13d923adc8361e3df
    role: context
  - path: data/natural_products/terpenoids/compound-11.yaml
    sha256: c6b1144ed2ccd49b3eb15d81e70c396bee614094e11074ed50076687ec64a29a
    role: context
  - path: data/natural_products/terpenoids/compound-12.yaml
    sha256: 68523e625132f3a958ba5ad4f2bad5984bfbc7d33f8a0f73e46e9ec109b21fd9
    role: context
  - path: data/natural_products/terpenoids/compound-15.yaml
    sha256: 86ed50b1cb3aeb1170f1e40e4c1d365b90cf94937cb27d36376882cda4b327ce
    role: context
  - path: data/natural_products/terpenoids/compound-6.yaml
    sha256: 4db168bf9a510a55403f4087abc00f8eee30b59a886a13a49daa8322eaa3b5cd
    role: context
  - path: data/natural_products/terpenoids/eutypinic-acid.yaml
    sha256: a2fbde14564e24a58cdf68e5c5b12fca09bb50874a8708eaf2904e684cfc6158
    role: context
  - path: data/natural_products/terpenoids/pestalodiol-e.yaml
    sha256: 6ee7a6ba26b1c13ea95adc492d1e200f9aefc45e3f700b3c53608e5960fc4e0b
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
  selection: Campaign path order 2372; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-2b8aee01b5
targets:
- target_id: naturalproductmech:mibig-2b8aee01b5
  path: data/natural_products/terpenoids/pestalodiol-e.yaml
  label: pestalodiol E
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
  - naturalproductmech:mibig-2b8aee01b5
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
  - naturalproductmech:mibig-2b8aee01b5
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
  - naturalproductmech:mibig-2b8aee01b5
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
  - naturalproductmech:mibig-2b8aee01b5
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
  - naturalproductmech:mibig-2b8aee01b5
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
  - naturalproductmech:mibig-2b8aee01b5
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-2b8aee01b5
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-2b8aee01b5
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2372-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/pestalodiol-e.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Complete current pestalodiol E owner and 2 history events; native status
    remains SEEDED. No source record was edited.
  snapshot_sha256: 6ee7a6ba26b1c13ea95adc492d1e200f9aefc45e3f700b3c53608e5960fc4e0b
- evidence_id: bgc-2372-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/1
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Whole captured owner/history supports absence of all four mechanism roots,
    component references and selected reader applicability.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2372-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/intakes/2372-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: 'Actual canonical intake for naturalproductmech:mibig-2b8aee01b5: 48 current
    input placements and complete source/curator ownership. Source and component corrections
    require their maintained owners, not generated pages.'
  snapshot_sha256: 2561da5c57d96c318a74fb68669bdf425605eb6cb8a0d5ce4bf62c53a004bcb0
- evidence_id: bgc-2372-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/1/owner_document/identifier; /records/1/owner_document/label;
    /records/1/owner_document/chemical_structure; /records/1/owner_document/source_concepts;
    /records/1/owner_document/grounding_status; /records/1/owner_document/grounding_notes
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Retained identity, full structure/key, concepts and any unresolved discussion;
    local agreement is not natural-identity authentication.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2372-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/1/owner_document/producer_taxon_groups; /records/1/owner_document/producer_organisms;
    /records/1/owner_document/biosynthetic_gene_clusters; /records/1/owner_document/source_concepts
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Retained source producer and locus grades, methods, genome scopes, entry
    versions and citation levels.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2372-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/1/owner_document/np_pathway; /records/1/owner_document/np_classification;
    /records/1/owner_document/bgc_class; /records/1/owner_document/biosynthesis_origin
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Named/versioned model output and source biosynthetic classes retain separate
    authority.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2372-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Whole owner supports absence of occurrences and occurrence_taxon_groups,
    while retaining its provenance/grounding notes. This is a snapshot absence, not
    absence in nature.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2372-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Whole owner has no written bioactivities, bioactivity_summary or molecular_targets.
    The available source snapshot does not establish inactivity.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2372-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/smiles;
    /records/1/inchi; /records/1/comparisons; /records/1/atom_correspondence
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Both original stored forms parsed; all ten comparisons and complete atom-count
    correspondence agree. The original full_graph_identity_established remains false.
    This is saved-form consistency, not natural identity or an independent full-graph
    proof.
  snapshot_sha256: 40f4a4d85e9c291635bcae75d173e7cb6ea4bcc74a1f9e248a1a9f8c6dc328d3
- evidence_id: bgc-2372-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons;
    /records/1/atom_correspondence; /records/1/smiles/computed; /records/1/inchi/computed
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: 'The aromatic ring bears hydroxyl oxygens SMILES O6 and O15 and two distinct
    side chains: aryl–C≡C–C(CH3)=CH2 and aryl–CH2–CH=C(CH3)2. All ring atoms are carbon;
    no cyclic ether, ester, amide, carbonyl or sugar residue is present in the saved
    graph. Both forms have empty potential-stereo lists. This is complete saved-representation
    interpretation, not reconstruction of a biosynthetic experiment.'
  snapshot_sha256: 40f4a4d85e9c291635bcae75d173e7cb6ea4bcc74a1f9e248a1a9f8c6dc328d3
- evidence_id: bgc-2372-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-execution-001.json
  locator: /observer; /command; /started_at; /finished_at; /exit_code; /stdout; /stderr;
    /retries; /external_requests
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: ROOT operated the original stored-form diagnostic once, exit 0 and no retry.
    Exact stream pins and original timestamps are retained.
  snapshot_sha256: c189304847deb6b5bcd363e93f191366348377f38746508ee229fd9fe75a9e8c
- evidence_id: bgc-2372-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /status; /DATA; /execution; /original_tools; /warnings; /limits
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: ROOT accepts original diagnostic integrity. Two omitted-undefined-stereo
    warnings remain global and unassigned; they are not per-record findings.
  snapshot_sha256: c58ec3eec001655cc705b5cb711fc96042b2dc765bacf31ef132ab3f8583f414
- evidence_id: bgc-2372-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/root-intake-acceptance-001.json
  locator: /accepted; /status; /summary; /records; /verification
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: ROOT accepts actual ten canonical intakes and exact source alignment. Intake
    ownership and hashes do not themselves certify science.
  snapshot_sha256: 3b660a99915d345d882a0d2bf5949015305d039e8bdd884b21e96240591549f4
- evidence_id: bgc-2372-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/root-source-inventory-acceptance-001.json
  locator: /accepted; /status; /inventory; /verification
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: ROOT accepts the original local extraction; complete scientific source
    meanings are separately attributed.
  snapshot_sha256: 8b502886402a2a78f2c2e47b1f1b14527b44355cc5396bd7088ac558ffd849d8
- evidence_id: bgc-2372-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/root-input-plan-acceptance-001.json
  locator: /accepted; /status; /plan; /verification
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: ROOT accepts exact complete plan maps and source preservation; actual intake
    acceptance separately supplies completed outcomes.
  snapshot_sha256: c2eb7849664c6b9186115248a7edd7043745ff5ecd0664f37c5ec4bc0d9112e1
- evidence_id: bgc-2372-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-target-input-plan-001.json
  locator: /records/1
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Accepted per-record plan preserves exact current inputs, direct contexts
    and complete source payloads, without a later silent refresh.
  snapshot_sha256: d7f788858ab6b318cbd1ab1dbfdc3bd89de0f8b05206e546e3e109d858e8e77a
- evidence_id: bgc-2372-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: 'Complete source/raw/history attribution: BGC 127 rows, Support 344 Phellandrene
    rows, and Native 305 cached stanzas plus curation. Repeated shared source reading
    is not counted twice.'
  snapshot_sha256: 845e90961cd00a73cb97c0361f7f8a8c5dba5da7ec17d4b6c029dc816e44fbd7
- evidence_id: bgc-2372-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-scope-notes-001.json
  locator: /curation; /curation_scope; /curation_source_receipt
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Ignored-inclusive implemented-curation scan is attributed to Native. One
    applicable Pentalenolactone BGC0000653 REPLACE row is distinguished from two unrelated
    lexical hits; no matching LOTUS or assay exclusion was found. Reserved files are
    not consumed corrections.
  snapshot_sha256: 845e90961cd00a73cb97c0361f7f8a8c5dba5da7ec17d4b6c029dc816e44fbd7
- evidence_id: bgc-2372-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line1; physical lines 2782–2782, row_sha256 6ec11c326cc37a015f72b9151eb3485817537350ce694f1f05c439d8f7d5908c
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Complete identity/key, source class, locus version/quality, producer/locus
    grades, and compound-versus-entry citation roles; implemented corrections are
    separate. All 1 complete row placements are retained. BGC complete source reading
    carries.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2372-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line1; physical lines 2795–2795, row_sha256 822916888dedafca3e3b92e9f2ae401a7384bb35e889979544919e828213575a
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Complete named/versioned computed prediction, including every blank class
    and glycoside value; faithful ingestion is distinct from chemical applicability.
    All 1 complete row placements are retained. BGC complete source reading carries.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2372-queries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/mibig_compounds; /contexts/14/source_scope_inventory/joins/chebi_structures;
    /contexts/14/source_scope_inventory/joins/lotus_occurrences; /contexts/14/source_scope_inventory/joins/cyanometdb_occurrences;
    /contexts/14/source_scope_inventory/joins/npclassifier; /contexts/14/source_scope_inventory/joins/pubchem_bioassay;
    /contexts/14/source_scope_inventory/joins/bindingdb_targets; /contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys;
    /contexts/14/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: 'All nine complete saved query frames and negative predicates: mibig_compounds=1,
    chebi_structures=0, lotus_occurrences=0, cyanometdb_occurrences=0, npclassifier=1,
    pubchem_bioassay=0, bindingdb_targets=0, antibioticmech_inchikeys=0, chebi_origins=0.
    No source query was replayed.'
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
- evidence_id: bgc-2372-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/source_taxa; /contexts/14/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/14/source_scope_inventory/nonorganism_matches; /contexts/14/source_scope_inventory/actual_assay_rows;
    /contexts/14/source_scope_inventory/blank_AID_sentinels; /contexts/14/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Exact selected source taxa and all route/sentinel/related lists. No actual
    assay, nonorganism match or source-query replay is present. The selected forward-merge
    route is empty.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
- evidence_id: bgc-2372-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/268
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: 'Complete retained local stanzas for this context (1 placements), with
    Native''s whole-cache reading attributed. Names and exact synonyms are not fresh
    taxonomy or producer-strain equivalence. '
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
- evidence_id: bgc-2372-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /records/1/direct_companion_paths; /records/1/direct_companion_predicates
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Exact bounded direct companion membership; shared loci or references do
    not transfer chemical identity, stereochemistry, production or assay claims.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
- evidence_id: bgc-2372-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/0; /contexts/1; /contexts/2; /contexts/3; /contexts/4; /contexts/5;
    /contexts/6; /contexts/7; /contexts/8; /contexts/9; /contexts/10
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Complete saved direct-companion source/raw/history context is carried with
    the original whole-reading attribution. Distinct full keys and experimental scopes
    remain separate.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
- evidence_id: bgc-2372-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines392–433
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: The structure flag records undefined stereocentres; computed classification
    is a named/versioned prediction, not a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2372-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines142–173
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Maintained stereo_complete checks undefined tetrahedral chiral centers;
    it is not fresh natural stereochemistry or a universal guarantee of all bond geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2372-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines972–1020
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: The maintained seeder preserves lead source structure and named/versioned
    prediction fields separately; filing is not experimental biosynthetic evidence.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
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
- assessment_id: bgc-2372-identity
  area: identity
  topic: Retained identity/form consistency; natural identity unverified
  outcome: supported
  summary: The minted identifier naturalproductmech:mibig-2b8aee01b5 retains full
    key XLJZQTJROGTDLX-UHFFFAOYSA-N and MIBiG row 2782, compound_index 12 in BGC0002290
    v2. That index is the inventory position, not a newly inferred paper label. The
    eleven direct companions have distinct full keys and remain context records, including
    compounds with different names, source citation bases and classifications. No
    compound identity, occurrence, bioactivity or structure is transferred from a
    companion. No ChEBI structure or additional exact-key identity authority is returned
    by the recorded joins.
  target_ids:
  - naturalproductmech:mibig-2b8aee01b5
  evidence_ids:
  - bgc-2372-grounding-owner
  - bgc-2372-source-mibig_compounds
  - bgc-2372-queries
  - bgc-2372-chemistry
  - bgc-2372-direct-contexts
  - bgc-2372-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: XLJZQTJROGTDLX-UHFFFAOYSA-N; complete retained key, not a name-only identity
      substitute.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2372-grounding-owner
    - bgc-2372-source-mibig_compounds
    - bgc-2372-queries
    - bgc-2372-chemistry
    - bgc-2372-direct-contexts
    - bgc-2372-companion-boundaries
  - name: grounding_scope
    value: The minted identifier naturalproductmech:mibig-2b8aee01b5 retains full
      key XLJZQTJROGTDLX-UHFFFAOYSA-N and MIBiG row 2782, compound_index 12 in BGC0002290
      v2. That index is the inventory position, not a newly inferred paper label.
      The eleven direct companions have distinct full keys and remain context records,
      including compounds with different names, source citation bases and classifications.
      No compound identity, occurrence, bioactivity or structure is transferred from
      a companion. No ChEBI structure or additional exact-key identity authority is
      returned by the recorded joins.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2372-grounding-owner
    - bgc-2372-source-mibig_compounds
    - bgc-2372-queries
    - bgc-2372-chemistry
    - bgc-2372-direct-contexts
    - bgc-2372-companion-boundaries
- assessment_id: bgc-2372-representation
  area: representation
  topic: Stored molecular representation and stereo scope
  outcome: supported
  summary: 'Both saved forms are neutral C16H18O2 with 18 heavy atoms and 18 bonds;
    all ten original comparisons agree. The tables show one aromatic six-carbon ring,
    two phenolic hydroxyls, one C≡C and two nonaromatic C=C bonds. Potential-stereo
    lists are empty in both forms: one alkene terminates in CH2 and the other has
    two methyl substituents on one end, so the source slash notation does not establish
    an independent E/Z assignment. The true tetrahedral-completeness flag is consistent
    at its maintained scope. Complete atom-count correspondence is true, but full_graph_identity_established
    remains false and natural identity is not experimentally authenticated.'
  target_ids:
  - naturalproductmech:mibig-2b8aee01b5
  evidence_ids:
  - bgc-2372-chemistry
  - bgc-2372-topology
  - bgc-2372-grounding-owner
  - bgc-2372-structure-schema
  - bgc-2372-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: 'Both saved forms are neutral C16H18O2 with 18 heavy atoms and 18 bonds;
      all ten original comparisons agree. The tables show one aromatic six-carbon
      ring, two phenolic hydroxyls, one C≡C and two nonaromatic C=C bonds. Potential-stereo
      lists are empty in both forms: one alkene terminates in CH2 and the other has
      two methyl substituents on one end, so the source slash notation does not establish
      an independent E/Z assignment. The true tetrahedral-completeness flag is consistent
      at its maintained scope. Complete atom-count correspondence is true, but full_graph_identity_established
      remains false and natural identity is not experimentally authenticated.'
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2372-chemistry
    - bgc-2372-topology
    - bgc-2372-grounding-owner
    - bgc-2372-structure-schema
    - bgc-2372-stereo-method
  - name: representation_correspondence
    value: All ten original comparison flags and complete atom-count correspondence
      are true; full_graph_identity_established remains false. Stored-form normalization
      does not authenticate natural identity.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2372-chemistry
    - bgc-2372-topology
    - bgc-2372-grounding-owner
    - bgc-2372-structure-schema
    - bgc-2372-stereo-method
- assessment_id: bgc-2372-provenance
  area: provenance
  topic: Producer and locus evidence
  outcome: supported
  summary: The retained producer is the literal unresolved label Biscogniauxia sp.,
    NCBITaxon:1896107, with SOURCE_ASSERTION evidence. BGC0002290 v2 spans MT109335.1:1–37984
    and is CLUSTER_DEMONSTRATED through Heterologous expression. The source class
    OTHER and subclass other are separate from that experimental method. A demonstrated
    locus does not identify an unresolved species more precisely or automatically
    upgrade the producer evidence basis.
  target_ids:
  - naturalproductmech:mibig-2b8aee01b5
  evidence_ids:
  - bgc-2372-origin-owner
  - bgc-2372-source-mibig_compounds
  - bgc-2372-cached-taxonomy
  - bgc-2372-source-routes
  dimensions:
  - name: taxon_scope
    value: The retained producer is the literal unresolved label Biscogniauxia sp.,
      NCBITaxon:1896107, with SOURCE_ASSERTION evidence. BGC0002290 v2 spans MT109335.1:1–37984
      and is CLUSTER_DEMONSTRATED through Heterologous expression. The source class
      OTHER and subclass other are separate from that experimental method. A demonstrated
      locus does not identify an unresolved species more precisely or automatically
      upgrade the producer evidence basis.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2372-origin-owner
    - bgc-2372-source-mibig_compounds
    - bgc-2372-cached-taxonomy
    - bgc-2372-source-routes
  - name: producer_evidence
    value: The retained producer is the literal unresolved label Biscogniauxia sp.,
      NCBITaxon:1896107, with SOURCE_ASSERTION evidence. BGC0002290 v2 spans MT109335.1:1–37984
      and is CLUSTER_DEMONSTRATED through Heterologous expression. The source class
      OTHER and subclass other are separate from that experimental method. A demonstrated
      locus does not identify an unresolved species more precisely or automatically
      upgrade the producer evidence basis.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2372-origin-owner
    - bgc-2372-source-mibig_compounds
    - bgc-2372-cached-taxonomy
    - bgc-2372-source-routes
  - name: locus_evidence
    value: The retained producer is the literal unresolved label Biscogniauxia sp.,
      NCBITaxon:1896107, with SOURCE_ASSERTION evidence. BGC0002290 v2 spans MT109335.1:1–37984
      and is CLUSTER_DEMONSTRATED through Heterologous expression. The source class
      OTHER and subclass other are separate from that experimental method. A demonstrated
      locus does not identify an unresolved species more precisely or automatically
      upgrade the producer evidence basis.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2372-origin-owner
    - bgc-2372-source-mibig_compounds
    - bgc-2372-cached-taxonomy
    - bgc-2372-source-routes
- assessment_id: bgc-2372-citations
  area: evidence
  topic: Citation authority and study scope
  outcome: supported
  summary: MIBiG row 2782 cites PMID:32364293 at ENTRY level. The shared entry citation
    does not establish a compound-specific experiment for every companion. In particular,
    the different COMPOUND_BIOACTIVITY citation retained for compound 15 is not silently
    copied to Pestalodiol E. The current source entry version and each literal citation
    role are preserved; no primary paper has been freshly read.
  target_ids:
  - naturalproductmech:mibig-2b8aee01b5
  evidence_ids:
  - bgc-2372-grounding-owner
  - bgc-2372-origin-owner
  - bgc-2372-source-mibig_compounds
  - bgc-2372-queries
  - bgc-2372-source-notes
  - bgc-2372-direct-contexts
  - bgc-2372-companion-boundaries
  dimensions:
  - name: citation_scope
    value: MIBiG row 2782 cites PMID:32364293 at ENTRY level. The shared entry citation
      does not establish a compound-specific experiment for every companion. In particular,
      the different COMPOUND_BIOACTIVITY citation retained for compound 15 is not
      silently copied to Pestalodiol E. The current source entry version and each
      literal citation role are preserved; no primary paper has been freshly read.
    definition: Distinguish retained database provenance, historical primary-experiment
      annotations and occurrence references; ENTRY and compound-specific citation
      bases remain separate. Repeated placements do not establish independent studies
      or fresh primary access.
    evidence_ids:
    - bgc-2372-grounding-owner
    - bgc-2372-origin-owner
    - bgc-2372-source-mibig_compounds
    - bgc-2372-queries
    - bgc-2372-source-notes
    - bgc-2372-direct-contexts
    - bgc-2372-companion-boundaries
- assessment_id: bgc-2372-occurrence
  area: evidence
  topic: Retained occurrence and assay scope
  outcome: supported
  summary: Neither occurrences nor occurrence_taxon_groups is written in the owner,
    and the three saved occurrence-source joins return no match for this context.
    Those bounded absences do not establish absence in nature. The recorded PubChem,
    BindingDB and related-corpus joins are also empty; they do not imply inactivity.
    Occurrences written on other BGC0002290 products remain specific to those products.
  target_ids:
  - naturalproductmech:mibig-2b8aee01b5
  evidence_ids:
  - bgc-2372-occurrence-owner
  - bgc-2372-assay-owner
  - bgc-2372-queries
  - bgc-2372-source-routes
  - bgc-2372-cached-taxonomy
  - bgc-2372-source-notes
  - bgc-2372-curation-scope
  dimensions:
  - name: occurrence_scope
    value: Neither occurrences nor occurrence_taxon_groups is written in the owner,
      and the three saved occurrence-source joins return no match for this context.
      Those bounded absences do not establish absence in nature. The recorded PubChem,
      BindingDB and related-corpus joins are also empty; they do not imply inactivity.
      Occurrences written on other BGC0002290 products remain specific to those products.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2372-occurrence-owner
    - bgc-2372-assay-owner
    - bgc-2372-queries
    - bgc-2372-source-routes
    - bgc-2372-cached-taxonomy
    - bgc-2372-source-notes
    - bgc-2372-curation-scope
  - name: assay_target_scope
    value: No written assay or target. The retained PubChem, BindingDB and related-corpus
      joins are empty for this exact source scope; this does not establish inactivity.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2372-occurrence-owner
    - bgc-2372-assay-owner
    - bgc-2372-queries
    - bgc-2372-source-routes
    - bgc-2372-cached-taxonomy
    - bgc-2372-source-notes
    - bgc-2372-curation-scope
- assessment_id: bgc-2372-classification
  area: consistency
  topic: Faithful versioned classification and bounded applicability
  outcome: supported
  summary: The record faithfully retains NPClassifier npclassifier.gnps2.org@2026-09-07
    outputs Terpenoids, Meroterpenoids, Miscellaneous meroterpenoids and is_glycoside:false.
    The aromatic scaffold with prenyl/alkynyl side chains supplies bounded chemical
    context, and the complete graph does not contain a sugar residue or glycosidic
    linkage. MIBiG OTHER and Heterologous expression retain their separate class and
    method meanings. Local structural compatibility does not independently establish
    biosynthetic provenance or validate every model class.
  target_ids:
  - naturalproductmech:mibig-2b8aee01b5
  evidence_ids:
  - bgc-2372-classification-owner
  - bgc-2372-source-npclassifier
  - bgc-2372-source-mibig_compounds
  - bgc-2372-chemistry
  - bgc-2372-topology
  - bgc-2372-structure-schema
  - bgc-2372-classification-seeder
  dimensions:
  - name: classification_applicability
    value: The record faithfully retains NPClassifier npclassifier.gnps2.org@2026-09-07
      outputs Terpenoids, Meroterpenoids, Miscellaneous meroterpenoids and is_glycoside:false.
      The aromatic scaffold with prenyl/alkynyl side chains supplies bounded chemical
      context, and the complete graph does not contain a sugar residue or glycosidic
      linkage. MIBiG OTHER and Heterologous expression retain their separate class
      and method meanings. Local structural compatibility does not independently establish
      biosynthetic provenance or validate every model class.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2372-classification-owner
    - bgc-2372-source-npclassifier
    - bgc-2372-source-mibig_compounds
    - bgc-2372-chemistry
    - bgc-2372-topology
    - bgc-2372-structure-schema
    - bgc-2372-classification-seeder
- assessment_id: bgc-2372-completion
  area: completeness
  topic: Scientific review completion
  outcome: unknown
  summary: Complete local owner/history, retained selected and eleven direct-companion
    contexts, actual intake and both original saved form tables have been reviewed.
    No mechanism root or maintained-reader route applies. Completion remains partial
    because Full QC/OAK and fresh primary, taxonomy and natural-identity verification
    are unavailable. No supported maintained-input correction is established.
  target_ids:
  - naturalproductmech:mibig-2b8aee01b5
  evidence_ids:
  - bgc-2372-owner
  - bgc-2372-capture
  - bgc-2372-intake
  - bgc-2372-plan
  - bgc-2372-intake-acceptance
  - bgc-2372-inventory-acceptance
  - bgc-2372-plan-acceptance
  - bgc-2372-source-notes
  - bgc-2372-curation-scope
  - bgc-2372-diagnostic-execution
  - bgc-2372-diagnostic-acceptance
  dimensions:
  - name: review_completion
    value: 'Partial: complete local source/intake/paired-form review; no applicable
      selected reader. Full QC/OAK and fresh primary/natural-identity verification
      remain unavailable; record-specific uncertainties remain explicit.'
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2372-owner
    - bgc-2372-capture
    - bgc-2372-intake
    - bgc-2372-plan
    - bgc-2372-intake-acceptance
    - bgc-2372-inventory-acceptance
    - bgc-2372-plan-acceptance
    - bgc-2372-source-notes
    - bgc-2372-curation-scope
    - bgc-2372-diagnostic-execution
    - bgc-2372-diagnostic-acceptance
findings: []
actions: []
limitations:
- All evidence is retained locally. No external publication, identifier, taxonomy,
  assay, protein sequence or natural stereochemical assignment was refreshed.
- Full QC and complete OAK coverage remain unavailable. Local diagnostics, source
  joins and maintained preservation have only their stated scope.
- Shared loci, names, taxa, source references or companion records do not transfer
  identity, stereochemistry, production, activity or independent-study status.
- Two original undefined-stereo warnings remain global and unassigned. No molecular/YAML
  reparse, source query or target ran during scientific authoring.
- No source status, record or history is edited. Any later supported correction belongs
  to the maintained owners in the actual intake.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete first-five raw/history, actual intakes and all ten original stored forms
  were personally read; the forms comprise 180 atom rows and 196 bond rows plus all
  scalar/ring/stereo/motif/map fields. Diagnostic indices are zero-based, not biochemical
  locants.
- 'Source meanings retain exact attribution: BGC 127 non-Phellandrene rows, Support
  344 Phellandrene rows, Native all305 cached stanzas and implemented curation. Complete
  current prior raw/history carries are in accepted notes.'
- ROOT operated original activation/capture, collector/composer, intakes and molecular
  diagnostic. Native operated gates and the sole Pentalenolactone maintained reader.
  BGC authored source planning and these scientific assessments without target invocation.
- No finding/action is inferred solely from an unresolved source identity, partial
  stereochemistry or faithful model-applicability concern.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-238
```
