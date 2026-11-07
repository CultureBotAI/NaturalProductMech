# Local evidence review: phyllostictine B

- Review: 20261104T092726Z-phyllostictine-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T08:24:13.793006Z
- Finished UTC: 2026-11-04T09:27:26.505980Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Phyllostictine B has consistent retained molecular forms, four specified tetrahedral centers and one E alkene. Its integrated cyclic ether/acetal structure leaves a bounded applicability concern for the versioned glycoside:true prediction and separate Terpenoids filing versus source NRPS/PKS. These are qualified interpretation limits, not an identified ingestion defect or instruction to replace a model result.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2375; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-3ee41ca902 | data/natural_products/terpenoids/phyllostictine-b.yaml | generated | phyllostictine B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-3ee41ca902 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-3ee41ca902 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-3ee41ca902 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-3ee41ca902 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-3ee41ca902 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-3ee41ca902 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-3ee41ca902 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-3ee41ca902 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity/form consistency; natural identity unverified

identity: supported. Targets: naturalproductmech:mibig-3ee41ca902.

The minted identifier naturalproductmech:mibig-3ee41ca902 retains full key RQRYYNCRMSFECR-VKKPVAOGSA-N and BGC0001741 v3 compound_index 2. The source cross-reference is literally npatlas:NPA07656; this review neither normalizes that string nor verifies it externally. Phyllostictine A is a direct locus companion with a different full key and saved structure. Its name, source rows, occurrence citations and model output do not establish identity or chemical equivalence with B.

### Stored molecular representation and stereo scope

representation: supported. Targets: naturalproductmech:mibig-3ee41ca902.

Both original forms are neutral C15H23NO5 with 21 heavy atoms and 23 bonds; all ten comparison flags agree. They preserve four specified tetrahedral centers, one amide carbonyl, two hydroxyls, one methoxy acetal and an intraring ether. The double bond is STEREOE in both complete bond tables, despite the index-relative potential-stereo descriptor Bond_Cis; that descriptor is not an opposing Z assignment. The true source stereo flag is compatible with the specified tetrahedral scope. Complete atom-count correspondence is true but full_graph_identity_established remains false, and natural stereochemical identity is not freshly verified.

### Producer and locus evidence

provenance: supported. Targets: naturalproductmech:mibig-3ee41ca902.

MIBiG row 2061 retains Phyllosticta cirsii NCBITaxon:1986016 as SOURCE_ASSERTION and BGC0001741 v3 as CLUSTER_UNSTATED, with genome KY682688.1 and no listed locus method or coordinates. NRPS and PKS, with Type I and Unknown subclasses, are retained source-locus classifications. They are not silently replaced by the computed filing or upgraded because a related compound shares the locus.

### Citation authority and study scope

evidence: supported. Targets: naturalproductmech:mibig-3ee41ca902.

DOI:10.1016/j.taap.2011.03.027 has COMPOUND_BIOACTIVITY source basis. It is distinct from the occurrence DOI:10.1016/J.TET.2007.12.010. A bioactivity-level citation is not a structured assay result or direct biosynthetic-production proof. The source versions, literal DOI strings and claim levels are preserved without a new primary-paper lookup.

### Retained occurrence and assay scope

evidence: supported. Targets: naturalproductmech:mibig-3ee41ca902.

LOTUS rows 8208 and 8209 name Phyllosticta cirsii NCBITaxon:1986016 and Cirsium arvense NCBITaxon:41550 under the same DOI. The plant occurrence does not make the plant the demonstrated biosynthetic producer; the fungal occurrence does not independently upgrade the source producer assertion. These two placements do not establish independent experiments. No selected PubChem assay, BindingDB target or related-corpus match is returned by the recorded joins.

### Faithful versioned classification and bounded applicability

consistency: concern. Targets: naturalproductmech:mibig-3ee41ca902.

NPClassifier npclassifier.gnps2.org@2026-09-07 returns Terpenoids, empty superclass/class fields and is_glycoside:true, while the source locus carries NRPS/PKS. The complete C15 nitrogen-containing lactam/acetal graph has an integrated five-member oxygen-containing ring, rather than independently identified sugar and aglycone residues. Neither the acetal alone nor the empty C5O detector settles biochemical glycoside identity. Applicability of the named prediction therefore remains a concern, with source/model biosynthetic interpretation also unresolved. The output was faithfully ingested: preserve it with provenance rather than inventing a replacement result or declaring the source fields corrupt.

### Scientific review completion

completeness: unknown. Targets: naturalproductmech:mibig-3ee41ca902.

Complete owner/history, selected and Phyllostictine A source contexts, actual intake and both original stored molecular forms are read. No mechanism root or selected reader applies. Completion remains partial because model applicability, Full QC/OAK and fresh primary, taxonomy and natural-identity verification remain limited. No supported source-record correction or finding/action is inferred solely from the faithful prediction.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2375-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/phyllostictine-b.yaml; Whole current owner plaintext and complete curation_history | supports | Complete current phyllostictine B owner and 3 history events; native status remains SEEDED. No source record was edited. |
| bgc-2375-capture | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/4 | supports | Whole captured owner/history supports absence of all four mechanism roots, component references and selected reader applicability. |
| bgc-2375-intake | /private/tmp/npm-review-work/shared-next-batch238/intakes/2375-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake for naturalproductmech:mibig-3ee41ca902: 38 current input placements and complete source/curator ownership. Source and component corrections require their maintained owners, not generated pages. |
| bgc-2375-grounding-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/4/owner_document/identifier; /records/4/owner_document/label; /records/4/owner_document/chemical_structure; /records/4/owner_document/xrefs; /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status; /records/4/owner_document/grounding_notes | supports | Retained identity, full structure/key, concepts and any unresolved discussion; local agreement is not natural-identity authentication. |
| bgc-2375-origin-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/4/owner_document/producer_taxon_groups; /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters; /records/4/owner_document/source_concepts | supports | Retained source producer and locus grades, methods, genome scopes, entry versions and citation levels. |
| bgc-2375-classification-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/4/owner_document/np_pathway; /records/4/owner_document/np_classification; /records/4/owner_document/bgc_class; /records/4/owner_document/biosynthesis_origin | supports | Named/versioned model output and source biosynthetic classes retain separate authority. |
| bgc-2375-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/4/owner_document/occurrences; /records/4/owner_document/occurrence_taxon_groups; /records/4/owner_document/grounding_notes | supports | All written occurrence taxa/references and any cap note are retained. Occurrence is distinct from production and independent publication evidence. |
| bgc-2375-assay-owner | /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json; /records/4/owner_document | supports | Whole owner has no written bioactivities, bioactivity_summary or molecular_targets. The available source snapshot does not establish inactivity. |
| bgc-2375-chemistry | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/smiles; /records/4/inchi; /records/4/comparisons; /records/4/atom_correspondence | supports | Both original stored forms parsed; all ten comparisons and complete atom-count correspondence agree. The original full_graph_identity_established remains false. This is saved-form consistency, not natural identity or an independent full-graph proof. |
| bgc-2375-topology | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons; /records/4/atom_correspondence; /records/4/smiles/computed; /records/4/inchi/computed | supports | The complete saved basis contains a four-member lactam [N2,C19,C5,C3], a five-member C4O ring [C7,C6,C12,C9,O8] and a nine-member carbocycle. SMILES C9 is an acetal center bonded to ring O8 and methoxy O10–C11; hydroxyls are O13H on C12 and O15H on C14. The five-member oxygen-containing ring is integrated into the larger framework, with shared carbon connectivity. Its presence survives the empty six-member C5O detector but does not independently establish a carbohydrate residue or a biochemical glycosidic linkage. The actual C5=C6 bond is E in both forms. These full-graph observations support a bounded model-applicability concern, not a categorical assignment of glycoside status. |
| bgc-2375-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-execution-001.json; /observer; /command; /started_at; /finished_at; /exit_code; /stdout; /stderr; /retries; /external_requests | supports | ROOT operated the original stored-form diagnostic once, exit 0 and no retry. Exact stream pins and original timestamps are retained. |
| bgc-2375-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /status; /DATA; /execution; /original_tools; /warnings; /limits | supports | ROOT accepts original diagnostic integrity. Two omitted-undefined-stereo warnings remain global and unassigned; they are not per-record findings. |
| bgc-2375-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch238/root-intake-acceptance-001.json; /accepted; /status; /summary; /records; /verification | supports | ROOT accepts actual ten canonical intakes and exact source alignment. Intake ownership and hashes do not themselves certify science. |
| bgc-2375-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch238/root-source-inventory-acceptance-001.json; /accepted; /status; /inventory; /verification | supports | ROOT accepts the original local extraction; complete scientific source meanings are separately attributed. |
| bgc-2375-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch238/root-input-plan-acceptance-001.json; /accepted; /status; /plan; /verification | supports | ROOT accepts exact complete plan maps and source preservation; actual intake acceptance separately supplies completed outcomes. |
| bgc-2375-plan | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-target-input-plan-001.json; /records/4 | supports | Accepted per-record plan preserves exact current inputs, direct contexts and complete source payloads, without a later silent refresh. |
| bgc-2375-source-notes | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete source/raw/history attribution: BGC 127 rows, Support 344 Phellandrene rows, and Native 305 cached stanzas plus curation. Repeated shared source reading is not counted twice. |
| bgc-2375-curation-scope | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-scope-notes-001.json; /curation; /curation_scope; /curation_source_receipt | supports | Ignored-inclusive implemented-curation scan is attributed to Native. One applicable Pentalenolactone BGC0000653 REPLACE row is distinguished from two unrelated lexical hits; no matching LOTUS or assay exclusion was found. Reserved files are not consumed corrections. |
| bgc-2375-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line1; physical lines 2061–2061, row_sha256 a6280f249ccf2a5067ab66caf225c51053ca78517569f957cdff56c0db168024 | supports | Complete identity/key, source class, locus version/quality, producer/locus grades, and compound-versus-entry citation roles; implemented corrections are separate. All 1 complete row placements are retained. BGC complete source reading carries. |
| bgc-2375-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line1; physical lines 8208–8208, row_sha256 5266512b905985e5ca10892fda1f7b3ba5cc36c02b08c34f12ac5bc4a3f8a8d2; physical lines 8209–8209, row_sha256 7de46bfe2e43fbb24f33095743f6539fab9718f23fc00ae46f81f041afe07faf | supports | Complete literal organism, taxon, DOI and structure-organism fields; occurrence is not independent production or experiment evidence. All 2 complete row placements are retained. BGC complete source reading carries. |
| bgc-2375-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line1; physical lines 2156–2156, row_sha256 f7a99a3c2b271bef01ff1e8fe82bb7e1a5d673b2c42203fb5f92196368e1f2e4 | supports | Complete named/versioned computed prediction, including every blank class and glycoside value; faithful ingestion is distinct from chemical applicability. All 1 complete row placements are retained. BGC complete source reading carries. |
| bgc-2375-queries | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/joins/mibig_compounds; /contexts/17/source_scope_inventory/joins/chebi_structures; /contexts/17/source_scope_inventory/joins/lotus_occurrences; /contexts/17/source_scope_inventory/joins/cyanometdb_occurrences; /contexts/17/source_scope_inventory/joins/npclassifier; /contexts/17/source_scope_inventory/joins/pubchem_bioassay; /contexts/17/source_scope_inventory/joins/bindingdb_targets; /contexts/17/source_scope_inventory/joins/antibioticmech_inchikeys; /contexts/17/source_scope_inventory/joins/chebi_origins | supports | All nine complete saved query frames and negative predicates: mibig_compounds=1, chebi_structures=0, lotus_occurrences=2, cyanometdb_occurrences=0, npclassifier=1, pubchem_bioassay=0, bindingdb_targets=0, antibioticmech_inchikeys=0, chebi_origins=0. No source query was replayed. |
| bgc-2375-source-routes | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/source_taxa; /contexts/17/source_scope_inventory/forward_taxon_merge_matches; /contexts/17/source_scope_inventory/nonorganism_matches; /contexts/17/source_scope_inventory/actual_assay_rows; /contexts/17/source_scope_inventory/blank_AID_sentinels; /contexts/17/source_scope_inventory/related_corpus_rows | supports | Exact selected source taxa and all route/sentinel/related lists. No actual assay, nonorganism match or source-query replay is present. The selected forward-merge route is empty. |
| bgc-2375-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/46; /cached_taxonomy/whole_stanzas/271 | supports | Complete retained local stanzas for this context (2 placements), with Native's whole-cache reading attributed. Names and exact synonyms are not fresh taxonomy or producer-strain equivalence.  |
| bgc-2375-direct-contexts | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /records/4/direct_companion_paths; /records/4/direct_companion_predicates | supports | Exact bounded direct companion membership; shared loci or references do not transfer chemical identity, stereochemistry, production or assay claims. |
| bgc-2375-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json; /contexts/27 | supports | Complete saved direct-companion source/raw/history context is carried with the original whole-reading attribution. Distinct full keys and experimental scopes remain separate. |
| bgc-2375-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines392–433 | supports | The structure flag records undefined stereocentres; computed classification is a named/versioned prediction, not a source assertion. |
| bgc-2375-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines142–173 | supports | Maintained stereo_complete checks undefined tetrahedral chiral centers; it is not fresh natural stereochemistry or a universal guarantee of all bond geometry. |
| bgc-2375-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines972–1020 | supports | The maintained seeder preserves lead source structure and named/versioned prediction fields separately; filing is not experimental biosynthetic evidence. |
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
review_id: 20261104T092726Z-phyllostictine-b
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: phyllostictine B'
started_at: '2026-11-04T08:24:13.793006Z'
finished_at: '2026-11-04T09:27:26.505980Z'
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
summary: Phyllostictine B has consistent retained molecular forms, four specified
  tetrahedral centers and one E alkene. Its integrated cyclic ether/acetal structure
  leaves a bounded applicability concern for the versioned glycoside:true prediction
  and separate Terpenoids filing versus source NRPS/PKS. These are qualified interpretation
  limits, not an identified ingestion defect or instruction to replace a model result.
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
  - path: data/natural_products/terpenoids/phyllostictine-b.yaml
    sha256: 6e7d36ed9168ab4a72ebdb351d1824284fcf07730d25cbea2d314ee986b32d9c
    role: target
  - path: data/natural_products/unclassified/phyllostictine-a.yaml
    sha256: fc78eb6549850eeb8bae95e77ecf3b423422eeb7967ab3685c445d05dd8191b8
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
  selection: Campaign path order 2375; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-3ee41ca902
targets:
- target_id: naturalproductmech:mibig-3ee41ca902
  path: data/natural_products/terpenoids/phyllostictine-b.yaml
  label: phyllostictine B
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
  - naturalproductmech:mibig-3ee41ca902
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
  - naturalproductmech:mibig-3ee41ca902
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
  - naturalproductmech:mibig-3ee41ca902
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
  - naturalproductmech:mibig-3ee41ca902
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
  - naturalproductmech:mibig-3ee41ca902
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
  - naturalproductmech:mibig-3ee41ca902
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-3ee41ca902
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-3ee41ca902
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2375-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/phyllostictine-b.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Complete current phyllostictine B owner and 3 history events; native status
    remains SEEDED. No source record was edited.
  snapshot_sha256: 6e7d36ed9168ab4a72ebdb351d1824284fcf07730d25cbea2d314ee986b32d9c
- evidence_id: bgc-2375-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/4
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Whole captured owner/history supports absence of all four mechanism roots,
    component references and selected reader applicability.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2375-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/intakes/2375-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: 'Actual canonical intake for naturalproductmech:mibig-3ee41ca902: 38 current
    input placements and complete source/curator ownership. Source and component corrections
    require their maintained owners, not generated pages.'
  snapshot_sha256: a1099c17bc688c4ba132e9d3b820ea274f5c17264670885d21105b16527d02d9
- evidence_id: bgc-2375-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/4/owner_document/identifier; /records/4/owner_document/label;
    /records/4/owner_document/chemical_structure; /records/4/owner_document/xrefs;
    /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status;
    /records/4/owner_document/grounding_notes
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Retained identity, full structure/key, concepts and any unresolved discussion;
    local agreement is not natural-identity authentication.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2375-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/4/owner_document/producer_taxon_groups; /records/4/owner_document/producer_organisms;
    /records/4/owner_document/biosynthetic_gene_clusters; /records/4/owner_document/source_concepts
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Retained source producer and locus grades, methods, genome scopes, entry
    versions and citation levels.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2375-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/4/owner_document/np_pathway; /records/4/owner_document/np_classification;
    /records/4/owner_document/bgc_class; /records/4/owner_document/biosynthesis_origin
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Named/versioned model output and source biosynthetic classes retain separate
    authority.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2375-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/4/owner_document/occurrences; /records/4/owner_document/occurrence_taxon_groups;
    /records/4/owner_document/grounding_notes
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: All written occurrence taxa/references and any cap note are retained. Occurrence
    is distinct from production and independent publication evidence.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2375-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Whole owner has no written bioactivities, bioactivity_summary or molecular_targets.
    The available source snapshot does not establish inactivity.
  snapshot_sha256: b4284b4720d05297c08bdd27f7431a79dab9dbcbb6cfa501532c6a300a56fcb1
- evidence_id: bgc-2375-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/smiles;
    /records/4/inchi; /records/4/comparisons; /records/4/atom_correspondence
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Both original stored forms parsed; all ten comparisons and complete atom-count
    correspondence agree. The original full_graph_identity_established remains false.
    This is saved-form consistency, not natural identity or an independent full-graph
    proof.
  snapshot_sha256: 40f4a4d85e9c291635bcae75d173e7cb6ea4bcc74a1f9e248a1a9f8c6dc328d3
- evidence_id: bgc-2375-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons;
    /records/4/atom_correspondence; /records/4/smiles/computed; /records/4/inchi/computed
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: The complete saved basis contains a four-member lactam [N2,C19,C5,C3],
    a five-member C4O ring [C7,C6,C12,C9,O8] and a nine-member carbocycle. SMILES
    C9 is an acetal center bonded to ring O8 and methoxy O10–C11; hydroxyls are O13H
    on C12 and O15H on C14. The five-member oxygen-containing ring is integrated into
    the larger framework, with shared carbon connectivity. Its presence survives the
    empty six-member C5O detector but does not independently establish a carbohydrate
    residue or a biochemical glycosidic linkage. The actual C5=C6 bond is E in both
    forms. These full-graph observations support a bounded model-applicability concern,
    not a categorical assignment of glycoside status.
  snapshot_sha256: 40f4a4d85e9c291635bcae75d173e7cb6ea4bcc74a1f9e248a1a9f8c6dc328d3
- evidence_id: bgc-2375-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/diagnostic-execution-001.json
  locator: /observer; /command; /started_at; /finished_at; /exit_code; /stdout; /stderr;
    /retries; /external_requests
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: ROOT operated the original stored-form diagnostic once, exit 0 and no retry.
    Exact stream pins and original timestamps are retained.
  snapshot_sha256: c189304847deb6b5bcd363e93f191366348377f38746508ee229fd9fe75a9e8c
- evidence_id: bgc-2375-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /status; /DATA; /execution; /original_tools; /warnings; /limits
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: ROOT accepts original diagnostic integrity. Two omitted-undefined-stereo
    warnings remain global and unassigned; they are not per-record findings.
  snapshot_sha256: c58ec3eec001655cc705b5cb711fc96042b2dc765bacf31ef132ab3f8583f414
- evidence_id: bgc-2375-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/root-intake-acceptance-001.json
  locator: /accepted; /status; /summary; /records; /verification
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: ROOT accepts actual ten canonical intakes and exact source alignment. Intake
    ownership and hashes do not themselves certify science.
  snapshot_sha256: 3b660a99915d345d882a0d2bf5949015305d039e8bdd884b21e96240591549f4
- evidence_id: bgc-2375-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/root-source-inventory-acceptance-001.json
  locator: /accepted; /status; /inventory; /verification
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: ROOT accepts the original local extraction; complete scientific source
    meanings are separately attributed.
  snapshot_sha256: 8b502886402a2a78f2c2e47b1f1b14527b44355cc5396bd7088ac558ffd849d8
- evidence_id: bgc-2375-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238/root-input-plan-acceptance-001.json
  locator: /accepted; /status; /plan; /verification
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: ROOT accepts exact complete plan maps and source preservation; actual intake
    acceptance separately supplies completed outcomes.
  snapshot_sha256: c2eb7849664c6b9186115248a7edd7043745ff5ecd0664f37c5ec4bc0d9112e1
- evidence_id: bgc-2375-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-target-input-plan-001.json
  locator: /records/4
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Accepted per-record plan preserves exact current inputs, direct contexts
    and complete source payloads, without a later silent refresh.
  snapshot_sha256: d7f788858ab6b318cbd1ab1dbfdc3bd89de0f8b05206e546e3e109d858e8e77a
- evidence_id: bgc-2375-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: 'Complete source/raw/history attribution: BGC 127 rows, Support 344 Phellandrene
    rows, and Native 305 cached stanzas plus curation. Repeated shared source reading
    is not counted twice.'
  snapshot_sha256: 845e90961cd00a73cb97c0361f7f8a8c5dba5da7ec17d4b6c029dc816e44fbd7
- evidence_id: bgc-2375-curation-scope
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
- evidence_id: bgc-2375-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line1; physical lines 2061–2061, row_sha256 a6280f249ccf2a5067ab66caf225c51053ca78517569f957cdff56c0db168024
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Complete identity/key, source class, locus version/quality, producer/locus
    grades, and compound-versus-entry citation roles; implemented corrections are
    separate. All 1 complete row placements are retained. BGC complete source reading
    carries.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2375-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line1; physical lines 8208–8208, row_sha256 5266512b905985e5ca10892fda1f7b3ba5cc36c02b08c34f12ac5bc4a3f8a8d2;
    physical lines 8209–8209, row_sha256 7de46bfe2e43fbb24f33095743f6539fab9718f23fc00ae46f81f041afe07faf
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Complete literal organism, taxon, DOI and structure-organism fields; occurrence
    is not independent production or experiment evidence. All 2 complete row placements
    are retained. BGC complete source reading carries.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2375-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line1; physical lines 2156–2156, row_sha256 f7a99a3c2b271bef01ff1e8fe82bb7e1a5d673b2c42203fb5f92196368e1f2e4
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Complete named/versioned computed prediction, including every blank class
    and glycoside value; faithful ingestion is distinct from chemical applicability.
    All 1 complete row placements are retained. BGC complete source reading carries.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2375-queries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/joins/mibig_compounds; /contexts/17/source_scope_inventory/joins/chebi_structures;
    /contexts/17/source_scope_inventory/joins/lotus_occurrences; /contexts/17/source_scope_inventory/joins/cyanometdb_occurrences;
    /contexts/17/source_scope_inventory/joins/npclassifier; /contexts/17/source_scope_inventory/joins/pubchem_bioassay;
    /contexts/17/source_scope_inventory/joins/bindingdb_targets; /contexts/17/source_scope_inventory/joins/antibioticmech_inchikeys;
    /contexts/17/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: 'All nine complete saved query frames and negative predicates: mibig_compounds=1,
    chebi_structures=0, lotus_occurrences=2, cyanometdb_occurrences=0, npclassifier=1,
    pubchem_bioassay=0, bindingdb_targets=0, antibioticmech_inchikeys=0, chebi_origins=0.
    No source query was replayed.'
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
- evidence_id: bgc-2375-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/source_taxa; /contexts/17/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/17/source_scope_inventory/nonorganism_matches; /contexts/17/source_scope_inventory/actual_assay_rows;
    /contexts/17/source_scope_inventory/blank_AID_sentinels; /contexts/17/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Exact selected source taxa and all route/sentinel/related lists. No actual
    assay, nonorganism match or source-query replay is present. The selected forward-merge
    route is empty.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
- evidence_id: bgc-2375-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/46; /cached_taxonomy/whole_stanzas/271
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: 'Complete retained local stanzas for this context (2 placements), with
    Native''s whole-cache reading attributed. Names and exact synonyms are not fresh
    taxonomy or producer-strain equivalence. '
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
- evidence_id: bgc-2375-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /records/4/direct_companion_paths; /records/4/direct_companion_predicates
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Exact bounded direct companion membership; shared loci or references do
    not transfer chemical identity, stereochemistry, production or assay claims.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
- evidence_id: bgc-2375-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch238-tentative/bgc-prep/bgc-conditional238-source-inventory-DATA-001.json
  locator: /contexts/27
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Complete saved direct-companion source/raw/history context is carried with
    the original whole-reading attribution. Distinct full keys and experimental scopes
    remain separate.
  snapshot_sha256: 87339a105084ecf3ff4ffe58e38b8c4ad02b9d7048f8a9f72d17fddd7e80ed2c
- evidence_id: bgc-2375-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines392–433
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: The structure flag records undefined stereocentres; computed classification
    is a named/versioned prediction, not a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2375-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines142–173
  accessed_at: '2026-11-04T09:20:46.041756Z'
  support: supports
  summary: Maintained stereo_complete checks undefined tetrahedral chiral centers;
    it is not fresh natural stereochemistry or a universal guarantee of all bond geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2375-classification-seeder
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
- assessment_id: bgc-2375-identity
  area: identity
  topic: Retained identity/form consistency; natural identity unverified
  outcome: supported
  summary: The minted identifier naturalproductmech:mibig-3ee41ca902 retains full
    key RQRYYNCRMSFECR-VKKPVAOGSA-N and BGC0001741 v3 compound_index 2. The source
    cross-reference is literally npatlas:NPA07656; this review neither normalizes
    that string nor verifies it externally. Phyllostictine A is a direct locus companion
    with a different full key and saved structure. Its name, source rows, occurrence
    citations and model output do not establish identity or chemical equivalence with
    B.
  target_ids:
  - naturalproductmech:mibig-3ee41ca902
  evidence_ids:
  - bgc-2375-grounding-owner
  - bgc-2375-source-mibig_compounds
  - bgc-2375-queries
  - bgc-2375-chemistry
  - bgc-2375-direct-contexts
  - bgc-2375-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: RQRYYNCRMSFECR-VKKPVAOGSA-N; complete retained key, not a name-only identity
      substitute.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2375-grounding-owner
    - bgc-2375-source-mibig_compounds
    - bgc-2375-queries
    - bgc-2375-chemistry
    - bgc-2375-direct-contexts
    - bgc-2375-companion-boundaries
  - name: grounding_scope
    value: The minted identifier naturalproductmech:mibig-3ee41ca902 retains full
      key RQRYYNCRMSFECR-VKKPVAOGSA-N and BGC0001741 v3 compound_index 2. The source
      cross-reference is literally npatlas:NPA07656; this review neither normalizes
      that string nor verifies it externally. Phyllostictine A is a direct locus companion
      with a different full key and saved structure. Its name, source rows, occurrence
      citations and model output do not establish identity or chemical equivalence
      with B.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2375-grounding-owner
    - bgc-2375-source-mibig_compounds
    - bgc-2375-queries
    - bgc-2375-chemistry
    - bgc-2375-direct-contexts
    - bgc-2375-companion-boundaries
- assessment_id: bgc-2375-representation
  area: representation
  topic: Stored molecular representation and stereo scope
  outcome: supported
  summary: Both original forms are neutral C15H23NO5 with 21 heavy atoms and 23 bonds;
    all ten comparison flags agree. They preserve four specified tetrahedral centers,
    one amide carbonyl, two hydroxyls, one methoxy acetal and an intraring ether.
    The double bond is STEREOE in both complete bond tables, despite the index-relative
    potential-stereo descriptor Bond_Cis; that descriptor is not an opposing Z assignment.
    The true source stereo flag is compatible with the specified tetrahedral scope.
    Complete atom-count correspondence is true but full_graph_identity_established
    remains false, and natural stereochemical identity is not freshly verified.
  target_ids:
  - naturalproductmech:mibig-3ee41ca902
  evidence_ids:
  - bgc-2375-chemistry
  - bgc-2375-topology
  - bgc-2375-grounding-owner
  - bgc-2375-structure-schema
  - bgc-2375-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both original forms are neutral C15H23NO5 with 21 heavy atoms and 23 bonds;
      all ten comparison flags agree. They preserve four specified tetrahedral centers,
      one amide carbonyl, two hydroxyls, one methoxy acetal and an intraring ether.
      The double bond is STEREOE in both complete bond tables, despite the index-relative
      potential-stereo descriptor Bond_Cis; that descriptor is not an opposing Z assignment.
      The true source stereo flag is compatible with the specified tetrahedral scope.
      Complete atom-count correspondence is true but full_graph_identity_established
      remains false, and natural stereochemical identity is not freshly verified.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2375-chemistry
    - bgc-2375-topology
    - bgc-2375-grounding-owner
    - bgc-2375-structure-schema
    - bgc-2375-stereo-method
  - name: representation_correspondence
    value: All ten original comparison flags and complete atom-count correspondence
      are true; full_graph_identity_established remains false. Stored-form normalization
      does not authenticate natural identity.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2375-chemistry
    - bgc-2375-topology
    - bgc-2375-grounding-owner
    - bgc-2375-structure-schema
    - bgc-2375-stereo-method
- assessment_id: bgc-2375-provenance
  area: provenance
  topic: Producer and locus evidence
  outcome: supported
  summary: MIBiG row 2061 retains Phyllosticta cirsii NCBITaxon:1986016 as SOURCE_ASSERTION
    and BGC0001741 v3 as CLUSTER_UNSTATED, with genome KY682688.1 and no listed locus
    method or coordinates. NRPS and PKS, with Type I and Unknown subclasses, are retained
    source-locus classifications. They are not silently replaced by the computed filing
    or upgraded because a related compound shares the locus.
  target_ids:
  - naturalproductmech:mibig-3ee41ca902
  evidence_ids:
  - bgc-2375-origin-owner
  - bgc-2375-source-mibig_compounds
  - bgc-2375-cached-taxonomy
  - bgc-2375-source-routes
  dimensions:
  - name: taxon_scope
    value: MIBiG row 2061 retains Phyllosticta cirsii NCBITaxon:1986016 as SOURCE_ASSERTION
      and BGC0001741 v3 as CLUSTER_UNSTATED, with genome KY682688.1 and no listed
      locus method or coordinates. NRPS and PKS, with Type I and Unknown subclasses,
      are retained source-locus classifications. They are not silently replaced by
      the computed filing or upgraded because a related compound shares the locus.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2375-origin-owner
    - bgc-2375-source-mibig_compounds
    - bgc-2375-cached-taxonomy
    - bgc-2375-source-routes
  - name: producer_evidence
    value: MIBiG row 2061 retains Phyllosticta cirsii NCBITaxon:1986016 as SOURCE_ASSERTION
      and BGC0001741 v3 as CLUSTER_UNSTATED, with genome KY682688.1 and no listed
      locus method or coordinates. NRPS and PKS, with Type I and Unknown subclasses,
      are retained source-locus classifications. They are not silently replaced by
      the computed filing or upgraded because a related compound shares the locus.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2375-origin-owner
    - bgc-2375-source-mibig_compounds
    - bgc-2375-cached-taxonomy
    - bgc-2375-source-routes
  - name: locus_evidence
    value: MIBiG row 2061 retains Phyllosticta cirsii NCBITaxon:1986016 as SOURCE_ASSERTION
      and BGC0001741 v3 as CLUSTER_UNSTATED, with genome KY682688.1 and no listed
      locus method or coordinates. NRPS and PKS, with Type I and Unknown subclasses,
      are retained source-locus classifications. They are not silently replaced by
      the computed filing or upgraded because a related compound shares the locus.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2375-origin-owner
    - bgc-2375-source-mibig_compounds
    - bgc-2375-cached-taxonomy
    - bgc-2375-source-routes
- assessment_id: bgc-2375-citations
  area: evidence
  topic: Citation authority and study scope
  outcome: supported
  summary: DOI:10.1016/j.taap.2011.03.027 has COMPOUND_BIOACTIVITY source basis. It
    is distinct from the occurrence DOI:10.1016/J.TET.2007.12.010. A bioactivity-level
    citation is not a structured assay result or direct biosynthetic-production proof.
    The source versions, literal DOI strings and claim levels are preserved without
    a new primary-paper lookup.
  target_ids:
  - naturalproductmech:mibig-3ee41ca902
  evidence_ids:
  - bgc-2375-grounding-owner
  - bgc-2375-origin-owner
  - bgc-2375-source-mibig_compounds
  - bgc-2375-source-lotus_occurrences
  - bgc-2375-queries
  - bgc-2375-source-notes
  - bgc-2375-direct-contexts
  - bgc-2375-companion-boundaries
  dimensions:
  - name: citation_scope
    value: DOI:10.1016/j.taap.2011.03.027 has COMPOUND_BIOACTIVITY source basis. It
      is distinct from the occurrence DOI:10.1016/J.TET.2007.12.010. A bioactivity-level
      citation is not a structured assay result or direct biosynthetic-production
      proof. The source versions, literal DOI strings and claim levels are preserved
      without a new primary-paper lookup.
    definition: Distinguish retained database provenance, historical primary-experiment
      annotations and occurrence references; ENTRY and compound-specific citation
      bases remain separate. Repeated placements do not establish independent studies
      or fresh primary access.
    evidence_ids:
    - bgc-2375-grounding-owner
    - bgc-2375-origin-owner
    - bgc-2375-source-mibig_compounds
    - bgc-2375-source-lotus_occurrences
    - bgc-2375-queries
    - bgc-2375-source-notes
    - bgc-2375-direct-contexts
    - bgc-2375-companion-boundaries
- assessment_id: bgc-2375-occurrence
  area: evidence
  topic: Retained occurrence and assay scope
  outcome: supported
  summary: LOTUS rows 8208 and 8209 name Phyllosticta cirsii NCBITaxon:1986016 and
    Cirsium arvense NCBITaxon:41550 under the same DOI. The plant occurrence does
    not make the plant the demonstrated biosynthetic producer; the fungal occurrence
    does not independently upgrade the source producer assertion. These two placements
    do not establish independent experiments. No selected PubChem assay, BindingDB
    target or related-corpus match is returned by the recorded joins.
  target_ids:
  - naturalproductmech:mibig-3ee41ca902
  evidence_ids:
  - bgc-2375-occurrence-owner
  - bgc-2375-assay-owner
  - bgc-2375-source-lotus_occurrences
  - bgc-2375-queries
  - bgc-2375-source-routes
  - bgc-2375-cached-taxonomy
  - bgc-2375-source-notes
  - bgc-2375-curation-scope
  dimensions:
  - name: occurrence_scope
    value: LOTUS rows 8208 and 8209 name Phyllosticta cirsii NCBITaxon:1986016 and
      Cirsium arvense NCBITaxon:41550 under the same DOI. The plant occurrence does
      not make the plant the demonstrated biosynthetic producer; the fungal occurrence
      does not independently upgrade the source producer assertion. These two placements
      do not establish independent experiments. No selected PubChem assay, BindingDB
      target or related-corpus match is returned by the recorded joins.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2375-occurrence-owner
    - bgc-2375-assay-owner
    - bgc-2375-source-lotus_occurrences
    - bgc-2375-queries
    - bgc-2375-source-routes
    - bgc-2375-cached-taxonomy
    - bgc-2375-source-notes
    - bgc-2375-curation-scope
  - name: assay_target_scope
    value: No written assay or target. The retained PubChem, BindingDB and related-corpus
      joins are empty for this exact source scope; this does not establish inactivity.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2375-occurrence-owner
    - bgc-2375-assay-owner
    - bgc-2375-source-lotus_occurrences
    - bgc-2375-queries
    - bgc-2375-source-routes
    - bgc-2375-cached-taxonomy
    - bgc-2375-source-notes
    - bgc-2375-curation-scope
- assessment_id: bgc-2375-classification
  area: consistency
  topic: Faithful versioned classification and bounded applicability
  outcome: concern
  summary: 'NPClassifier npclassifier.gnps2.org@2026-09-07 returns Terpenoids, empty
    superclass/class fields and is_glycoside:true, while the source locus carries
    NRPS/PKS. The complete C15 nitrogen-containing lactam/acetal graph has an integrated
    five-member oxygen-containing ring, rather than independently identified sugar
    and aglycone residues. Neither the acetal alone nor the empty C5O detector settles
    biochemical glycoside identity. Applicability of the named prediction therefore
    remains a concern, with source/model biosynthetic interpretation also unresolved.
    The output was faithfully ingested: preserve it with provenance rather than inventing
    a replacement result or declaring the source fields corrupt.'
  target_ids:
  - naturalproductmech:mibig-3ee41ca902
  evidence_ids:
  - bgc-2375-classification-owner
  - bgc-2375-source-npclassifier
  - bgc-2375-source-mibig_compounds
  - bgc-2375-chemistry
  - bgc-2375-topology
  - bgc-2375-structure-schema
  - bgc-2375-classification-seeder
  dimensions:
  - name: classification_applicability
    value: 'NPClassifier npclassifier.gnps2.org@2026-09-07 returns Terpenoids, empty
      superclass/class fields and is_glycoside:true, while the source locus carries
      NRPS/PKS. The complete C15 nitrogen-containing lactam/acetal graph has an integrated
      five-member oxygen-containing ring, rather than independently identified sugar
      and aglycone residues. Neither the acetal alone nor the empty C5O detector settles
      biochemical glycoside identity. Applicability of the named prediction therefore
      remains a concern, with source/model biosynthetic interpretation also unresolved.
      The output was faithfully ingested: preserve it with provenance rather than
      inventing a replacement result or declaring the source fields corrupt.'
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2375-classification-owner
    - bgc-2375-source-npclassifier
    - bgc-2375-source-mibig_compounds
    - bgc-2375-chemistry
    - bgc-2375-topology
    - bgc-2375-structure-schema
    - bgc-2375-classification-seeder
- assessment_id: bgc-2375-completion
  area: completeness
  topic: Scientific review completion
  outcome: unknown
  summary: Complete owner/history, selected and Phyllostictine A source contexts,
    actual intake and both original stored molecular forms are read. No mechanism
    root or selected reader applies. Completion remains partial because model applicability,
    Full QC/OAK and fresh primary, taxonomy and natural-identity verification remain
    limited. No supported source-record correction or finding/action is inferred solely
    from the faithful prediction.
  target_ids:
  - naturalproductmech:mibig-3ee41ca902
  evidence_ids:
  - bgc-2375-owner
  - bgc-2375-capture
  - bgc-2375-intake
  - bgc-2375-plan
  - bgc-2375-intake-acceptance
  - bgc-2375-inventory-acceptance
  - bgc-2375-plan-acceptance
  - bgc-2375-source-notes
  - bgc-2375-curation-scope
  - bgc-2375-diagnostic-execution
  - bgc-2375-diagnostic-acceptance
  dimensions:
  - name: review_completion
    value: 'Partial: complete local source/intake/paired-form review; no applicable
      selected reader. Full QC/OAK and fresh primary/natural-identity verification
      remain unavailable; record-specific uncertainties remain explicit.'
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2375-owner
    - bgc-2375-capture
    - bgc-2375-intake
    - bgc-2375-plan
    - bgc-2375-intake-acceptance
    - bgc-2375-inventory-acceptance
    - bgc-2375-plan-acceptance
    - bgc-2375-source-notes
    - bgc-2375-curation-scope
    - bgc-2375-diagnostic-execution
    - bgc-2375-diagnostic-acceptance
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
