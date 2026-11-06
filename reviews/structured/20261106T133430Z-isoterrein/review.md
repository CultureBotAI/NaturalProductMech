# Local evidence review: isoterrein

- Review: 20261106T133430Z-isoterrein
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T12:38:14.171092Z
- Finished UTC: 2026-11-06T13:34:30.973038Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass for isoterrein's retained source identity, two specified stereocentres, E alkene and consistent stored forms. Species-level occurrence and strain-level production remain distinct, and the empty classifier output correctly leaves filing unresolved. Completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2717; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-ef6e0053ae | data/natural_products/unclassified/isoterrein.yaml | generated | isoterrein |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-ef6e0053ae | The original execution parsed both stored forms; formula, formal charge, StandardInChI and declared full key agree. |
| strict_ten | passed | True | naturalproductmech:mibig-ef6e0053ae | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-ef6e0053ae | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-ef6e0053ae | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-ef6e0053ae | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-ef6e0053ae | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-ef6e0053ae | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-ef6e0053ae | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-ef6e0053ae | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and grounding

identity: supported. Targets: naturalproductmech:mibig-ef6e0053ae.

MIBiG BGC0000161 v4 and full key MHOOPNKRBMHHEC-RIAPOHOLSA-N support the minted isoterrein mapping. The literal NPAtlas cross-reference NPA019504 is retained without fresh resolution. No exact retained ChEBI structure or distinct same-BGC companion was returned by the bounded scope; no name-only or partial-key substitution is made.

### Stored forms and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-ef6e0053ae.

The two saved forms agree on neutral C8H10O3, 11 atoms, 11 bonds, both canonical SMILES strings, StandardInChI and full key. The existing complete one-way 11-index correspondence supports this limited comparison, while full_graph_identity_established explicitly remains false. Both forms contain one five-carbon ring, one ketone, two hydroxyl groups, two specified tetrahedral centres with saved S labels and one specified E side-chain alkene. The ring double bond has no potential-double-stereo entry. No ester, amide, C(OH)=N or candidate C5O sugar ring is present. These saved results do not independently establish natural configuration. Four charge-rearrangement and four undefined-stereo warnings in shared stderr remain globally unassigned.

### Producer, taxonomy and locus grades

provenance: supported. Targets: naturalproductmech:mibig-ef6e0053ae.

Aspergillus terreus NIH2624 / NCBITaxon:341663 retains BGC_CHARACTERIZED, separately from the BGC0000161 v4 CLUSTER_DEMONSTRATED link. The saved methods are knock-out studies, heterologous expression and expression correlated with production; the maintained grading table supports keeping the organism and cluster questions separate. The locus is CH476594.1:399827–432585. Species-level A. terreus33178 and A. fischeri36630 occurrence routes do not replace the NIH2624 strain or prove production by every occurrence taxon.

### Citation and history scope

evidence: supported. Targets: naturalproductmech:mibig-ef6e0053ae.

PMID:24816227 is the MIBiG ENTRY citation. LOTUS retains DOI:10.1016/J.CHEMBIOL.2014.03.010 for A. terreus and DOI:10.2520/MYCO.56.3 for two source rows naming Aspergillus fischeri and Neosartorya fischeri at the same taxon36630. Their publication independence is not established. Both seeding events remain unchanged; no paper was reopened.

### Occurrence, assay and target boundaries

evidence: supported. Targets: naturalproductmech:mibig-ef6e0053ae.

The three physical LOTUS placements reduce to two written taxon/reference occurrences: A. terreus33178 and A. fischeri36630. The two source labels sharing36630 and the same DOI are not separate production experiments; the retained seeder deduplicates exact taxon/reference pairs. All saved assay, BindingDB and related-corpus frames are empty for this owner. That is a finite data boundary, not proof of inactivity or no biological role.

### Classification and saved topology

consistency: supported. Targets: naturalproductmech:mibig-ef6e0053ae.

NPClassifier pathway, superclass and class arrays are all empty and is_glycoside:false. The maintained zero-label branch intentionally returns UNCLASSIFIED. A hydroxylated cyclopentenone with an E side-chain alkene is supported by the saved topology, but assigning a model pathway or natural biosynthetic family would exceed these rows. The MIBiG PKS class remains a locus-level annotation.

### Scientific completion and ownership

completeness: unknown. Targets: naturalproductmech:mibig-ef6e0053ae.

Whole owner/history, every assigned saved source frame/positive dictionary, both complete molecular tables and actual intake claims were read. Current input hashes and ownership match the accepted plan; that is distinct from whole-corpus scientific reading. Five local commands passed. Full QC, OAK grounding and live primary-source verification remain unavailable under the request hold. No graph/pathway reader applies to this owner. Completion is partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2717-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/isoterrein.yaml; Whole current plaintext including complete history | supports | Whole current owner/history personally read; source bytes remain exact. |
| support-2717-capture | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/6/owner_document | supports | Complete original captured owner; no live-source verification is inferred. |
| support-2717-identity | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/6/owner_document/identifier; /records/6/owner_document/chemical_structure; /records/6/owner_document/source_concepts; /records/6/owner_document/xrefs; /records/6/owner_document/grounding_status; /records/6/owner_document/grounding_notes | supports | Exact full-key/source mapping and literal xrefs; no name or prefix substitution. |
| support-2717-producer-locus | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters; /records/6/owner_document/producer_taxon_groups; /records/6/owner_document/bgc_class | supports | Separate producer and locus grades, source methods and exact citation placement. |
| support-2717-history-citations | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/6/owner_document/source_concepts; /records/6/owner_document/biosynthetic_gene_clusters; /records/6/owner_document/curation_history | supports | Complete source citation grain and every current history event; historical notes are attributed. |
| support-2717-occurrence | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/6/owner_document/occurrences; /records/6/owner_document/occurrence_taxon_groups; /records/6/owner_document/xrefs | supports | Owner-local occurrence/xref placements, distinct from producer or assay claims. |
| support-2717-classification | /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json; /records/6/owner_document/np_pathway; /records/6/owner_document/np_classification; /records/6/owner_document/biosynthesis_origin; /records/6/owner_document/bgc_class | supports | Literal filing, model classification and source BGC class retain different evidential roles. |
| support-2717-intake | /private/tmp/npm-review-work/shared-next-batch272/intakes-001/2717-inspect-001.json; /status; /source; /targets | supports | Original inspection target, ownership and input hashes; hash checking is not whole-corpus reading. |
| support-2717-intake-original | /private/tmp/npm-review-work/shared-next-batch272/intakes-001/intake-summary-001.json; /receipts/6 | supports | Original owner intake argv/environment/exit0/stdout and empty stderr, no replay. |
| support-2717-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch272/root-intake-acceptance-001.json; /accepted; /summary; /all_expected_maps_exact; /all_stderr_empty | supports | ROOT accepted original exact458 placements/61 paths. |
| support-2717-source-plan | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-target-input-plan-001.json; /records/6 | supports | Exact owner-local companion and diagnostic/reader roles; no claim transfer from another owner. |
| support-2717-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch272/root-current272-source-plan-acceptance-001.json; /accepted; /plan | supports | Accepted original source plan, not an invented future input set. |
| support-2717-source-reading | /private/tmp/npm-review-work/shared-next-batch272-tentative/support-prep/support-current272-assigned-source-reading-001.json; /contexts/1; /counts; /primary_context_indices | supports | Complete assigned saved query/row reading; this owner selected from the disjoint27-row Support partition. |
| support-2717-notes | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | supports | Actual33+27 primary rows, Native0; source-query and literature boundaries remain explicit. |
| support-2717-taxonomy | /private/tmp/npm-review-work/shared-next-batch272-tentative/native-prep/native-current272-cached-taxonomy-reading-001.json; /context_interpretations/10; /interpretation | supports | Owner-local retained cached taxon routes; no fresh rank, lineage or strain verification. |
| support-2717-curation | /private/tmp/npm-review-work/shared-next-batch272-tentative/native-prep/native-current272-implemented-curation-scan-001.json; /counts; /exact_applicability_resolution; /implementation_scope; /interpretation | supports | Nine substantive retained tables and exact identity predicates give no applicable correction for this owner; census-only extra tables are excluded. |
| support-2717-molecular-DATA | /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnostic-DATA-001.json; /records/6 | supports | All saved atom/bond/stereo/motif fields and existing map; normalized agreement is distinct from fixed-form or natural identity. |
| support-2717-molecular-reading | /private/tmp/npm-review-work/shared-next-batch272-tentative/support-prep/support-current272-last-five-molecular-intake-reading-001.json; /records/1 | supports | Personal complete saved-table reading and representation-aware interpretation, with no new parse. |
| support-2717-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /warning_lines; /warnings_assigned_to_records | supports | Accepted original20-form diagnostic; four charge and four undefined-stereo warnings are globally unassigned. |
| support-2717-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr; /retries; /external_requests | supports | One original successful diagnostic; no repeated parse or target invocation in this review lane. |
| support-2717-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–172 | supports | Source stereo_complete uses atom-centred FindMolChiralCenters; it does not certify all double-bond geometry. |
| support-2717-grade-policy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; lines 1–40 | supports | Producer evidence and locus evidence are graded separately; source occurrence cannot upgrade either. |
| support-2717-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295–306 | supports | choose_pathway preserves zero/multiple predictions as UNCLASSIFIED. |
| support-2717-local-gates | /private/tmp/npm-review-work/shared-next-batch272/root-native-five-gates-acceptance-001.json; /accepted; /all_five_commands_exit_zero; /selected_queue_rows | supports | Five original local commands passed; queue entries are leads, not automatic scientific defects or complete QC. |
| support-2717-reader-scope | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-selected-mechanism-profile-001.json; /mechanisms; /selected_reader_orders | supports | Only2719/2720 require maintained graph/pathway resolution; Jamaicamide C stays unselected context. |
| support-2717-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds predicate and all 1 positive placements or bounded negative result. |
| support-2717-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Whole physical TSV rows and parsed dictionaries at /contexts/10/source_scope_inventory/joins/mibig_compounds/matches in the pinned inventory | supports | All positive fields, physical line bounds/raw spans and row digests personally read and joined in the attributed source receipt. |
| support-2717-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures predicate and all 0 positive placements or bounded negative result. |
| support-2717-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences predicate and all 3 positive placements or bounded negative result. |
| support-2717-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Whole physical TSV rows and parsed dictionaries at /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches in the pinned inventory | supports | All positive fields, physical line bounds/raw spans and row digests personally read and joined in the attributed source receipt. |
| support-2717-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences predicate and all 0 positive placements or bounded negative result. |
| support-2717-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier predicate and all 1 positive placements or bounded negative result. |
| support-2717-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Whole physical TSV rows and parsed dictionaries at /contexts/10/source_scope_inventory/joins/npclassifier/matches in the pinned inventory | supports | All positive fields, physical line bounds/raw spans and row digests personally read and joined in the attributed source receipt. |
| support-2717-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay predicate and all 0 positive placements or bounded negative result. |
| support-2717-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets predicate and all 0 positive placements or bounded negative result. |
| support-2717-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys predicate and all 0 positive placements or bounded negative result. |
| support-2717-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins predicate and all 0 positive placements or bounded negative result. |
| support-2717-taxon-predicates | /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/source_taxa; /contexts/10/source_scope_inventory/forward_taxon_merge_matches; /contexts/10/source_scope_inventory/nonorganism_matches | supports | Exact owner-local taxon route and negative merge/nonorganism frames; no companion-route substitution. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-272/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-272/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-272/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-272/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-272/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained owner/source rows and accepted original local outputs only; no fresh primary publication, taxonomy, sequence or external-identifier resolution.
- The eleven-atom one-way match and canonical agreement are limited stored-form checks; they do not establish natural identity, experimental stereochemical assignment or production by the species-level occurrence taxa.
- Four charge-rearrangement and four undefined-stereo warnings are global and unassigned. Full QC/OAK and live primary verification remain unavailable; source grades and citation grain are not upgraded.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete selected owner/history, saved source frames and both molecular tables personally read; positive row placements are not independent experiments and hash verification is not whole-corpus reading.
- No source, record, curation-status or history edit is proposed. No outbound request, new parse or target execution occurred in this authoring lane.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T133430Z-isoterrein
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: isoterrein'
started_at: '2026-11-06T12:38:14.171092Z'
finished_at: '2026-11-06T13:34:30.973038Z'
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
summary: Qualified pass for isoterrein's retained source identity, two specified stereocentres,
  E alkene and consistent stored forms. Species-level occurrence and strain-level
  production remain distinct, and the empty classifier output correctly leaves filing
  unresolved. Completion is partial.
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
  - path: data/natural_products/unclassified/isoterrein.yaml
    sha256: c9d1fc01b7883b48de5aeca1778b1d088d21dec317dfe854de8e86b105b34f61
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
  selection: Campaign path order 2717; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-ef6e0053ae
targets:
- target_id: naturalproductmech:mibig-ef6e0053ae
  path: data/natural_products/unclassified/isoterrein.yaml
  label: isoterrein
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnose272-001.py
    0cb2578b19e493e9249755546918ab75743c353b19d38062e893ebab5314f402 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
    511c5c899beeb5cde2fdff1e9d7148a34c04f2076e2e2e674b19adbcf1da5db7
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The original execution parsed both stored forms; formula, formal charge,
    StandardInChI and declared full key agree.
  scope_note: Both canonical comparisons are true with the existing complete11-atom
    one-way map. Full graph identity remains explicitly false. Eight warnings are
    globally unassigned. A passed execution does not establish natural identity or
    experimental stereochemistry.
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  evidence_ids:
  - support-2717-molecular-DATA
  - support-2717-diagnostic-acceptance
  - support-2717-diagnostic-execution
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  command: just validate-strict data/natural_products/unclassified/ilamycin-c1.yaml
    data/natural_products/unclassified/ilamycin-c2.yaml data/natural_products/unclassified/ilicicolin-b.yaml
    data/natural_products/unclassified/incarnatapeptin-b.yaml data/natural_products/unclassified/incednine.yaml
    data/natural_products/unclassified/irciniastatin-b.yaml data/natural_products/unclassified/isoterrein.yaml
    data/natural_products/unclassified/jagaricin.yaml data/natural_products/unclassified/jamaicamide-a.yaml
    data/natural_products/unclassified/jamaicamide-b.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-272/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-ef6e0053ae
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-272/validate-all-001.tsv
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
  - naturalproductmech:mibig-ef6e0053ae
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
  - naturalproductmech:mibig-ef6e0053ae
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
  - naturalproductmech:mibig-ef6e0053ae
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-272/review-queue-001.tsv
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
  - naturalproductmech:mibig-ef6e0053ae
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2717-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/isoterrein.yaml
  locator: Whole current plaintext including complete history
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Whole current owner/history personally read; source bytes remain exact.
  snapshot_sha256: c9d1fc01b7883b48de5aeca1778b1d088d21dec317dfe854de8e86b105b34f61
- evidence_id: support-2717-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete original captured owner; no live-source verification is inferred.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: support-2717-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/6/owner_document/identifier; /records/6/owner_document/chemical_structure;
    /records/6/owner_document/source_concepts; /records/6/owner_document/xrefs; /records/6/owner_document/grounding_status;
    /records/6/owner_document/grounding_notes
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Exact full-key/source mapping and literal xrefs; no name or prefix substitution.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: support-2717-producer-locus
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters;
    /records/6/owner_document/producer_taxon_groups; /records/6/owner_document/bgc_class
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Separate producer and locus grades, source methods and exact citation placement.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: support-2717-history-citations
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/6/owner_document/source_concepts; /records/6/owner_document/biosynthetic_gene_clusters;
    /records/6/owner_document/curation_history
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete source citation grain and every current history event; historical
    notes are attributed.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: support-2717-occurrence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/6/owner_document/occurrences; /records/6/owner_document/occurrence_taxon_groups;
    /records/6/owner_document/xrefs
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Owner-local occurrence/xref placements, distinct from producer or assay
    claims.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: support-2717-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272/owner-capture-DATA-001.json
  locator: /records/6/owner_document/np_pathway; /records/6/owner_document/np_classification;
    /records/6/owner_document/biosynthesis_origin; /records/6/owner_document/bgc_class
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Literal filing, model classification and source BGC class retain different
    evidential roles.
  snapshot_sha256: 4c1f720d95432490e9e37b885f20aaa25a80ae533fdb2b97a7c74abf026ae647
- evidence_id: support-2717-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/intakes-001/2717-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Original inspection target, ownership and input hashes; hash checking is
    not whole-corpus reading.
  snapshot_sha256: 5b1eacd95a2ab591574bf1466c17feeb88a1e5379132680f3a571e77676ba4cf
- evidence_id: support-2717-intake-original
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/intakes-001/intake-summary-001.json
  locator: /receipts/6
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Original owner intake argv/environment/exit0/stdout and empty stderr, no
    replay.
  snapshot_sha256: 511c5c899beeb5cde2fdff1e9d7148a34c04f2076e2e2e674b19adbcf1da5db7
- evidence_id: support-2717-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/root-intake-acceptance-001.json
  locator: /accepted; /summary; /all_expected_maps_exact; /all_stderr_empty
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: ROOT accepted original exact458 placements/61 paths.
  snapshot_sha256: 801e9a99db5b2826fd4355b9527ff19648873390bf43fa1224336bfb8a0ffabe
- evidence_id: support-2717-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-target-input-plan-001.json
  locator: /records/6
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Exact owner-local companion and diagnostic/reader roles; no claim transfer
    from another owner.
  snapshot_sha256: 88b8e4da369b51ff7ba70fbd6c6f9e584601e9c106daee1c3e8eba2406851cb3
- evidence_id: support-2717-source-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/root-current272-source-plan-acceptance-001.json
  locator: /accepted; /plan
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Accepted original source plan, not an invented future input set.
  snapshot_sha256: d81d9507e202fa0c3eac7c74f2bb61aad22a3d42a95091cf47d4da887823aa33
- evidence_id: support-2717-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/support-prep/support-current272-assigned-source-reading-001.json
  locator: /contexts/1; /counts; /primary_context_indices
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete assigned saved query/row reading; this owner selected from the
    disjoint27-row Support partition.
  snapshot_sha256: 9e25c4c73b08fc9e79a753b274bed2915ba2ddc838b6dab2939e28879ece72e4
- evidence_id: support-2717-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Actual33+27 primary rows, Native0; source-query and literature boundaries
    remain explicit.
  snapshot_sha256: 3fbbc507013f5e09915ebbab660ac6757a56b402499ab2187ec384c9aa010b4e
- evidence_id: support-2717-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/native-prep/native-current272-cached-taxonomy-reading-001.json
  locator: /context_interpretations/10; /interpretation
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Owner-local retained cached taxon routes; no fresh rank, lineage or strain
    verification.
  snapshot_sha256: a8b0ac542d9758a6e7205450e57e04968f18e69dd61358f5b16716c06e410435
- evidence_id: support-2717-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/native-prep/native-current272-implemented-curation-scan-001.json
  locator: /counts; /exact_applicability_resolution; /implementation_scope; /interpretation
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Nine substantive retained tables and exact identity predicates give no
    applicable correction for this owner; census-only extra tables are excluded.
  snapshot_sha256: b9aaad338ba894d766d71c50336f9cf0056fdf4a6bb5f26a2b2ca188cf906bfe
  search_scope: Exact current owner/source compound/full-key/digest predicates in
    the receipt, not a genus/name substring verdict; no new source query.
- evidence_id: support-2717-molecular-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: All saved atom/bond/stereo/motif fields and existing map; normalized agreement
    is distinct from fixed-form or natural identity.
  snapshot_sha256: bb91cc8d0e213bdc89d27c74eeb34cebef9d7b2b0d18bfe8a1f48e201f497c8e
- evidence_id: support-2717-molecular-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/support-prep/support-current272-last-five-molecular-intake-reading-001.json
  locator: /records/1
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Personal complete saved-table reading and representation-aware interpretation,
    with no new parse.
  snapshot_sha256: 32720c3d7f691f0f74b7b781c912b9755a4ba78b54e4728c26ab19e797233a60
- evidence_id: support-2717-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /warning_lines; /warnings_assigned_to_records
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Accepted original20-form diagnostic; four charge and four undefined-stereo
    warnings are globally unassigned.
  snapshot_sha256: 1aa9f9ca7b5c5f3293ef344dc9e2ebf8987395ceebf7c1142c413afedf44f380
- evidence_id: support-2717-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: One original successful diagnostic; no repeated parse or target invocation
    in this review lane.
  snapshot_sha256: 335d822411906e6b33c46d5a94157b9e76fbfd92034a04ac911ac138e38cfc69
- evidence_id: support-2717-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–172
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Source stereo_complete uses atom-centred FindMolChiralCenters; it does
    not certify all double-bond geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2717-grade-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: lines 1–40
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Producer evidence and locus evidence are graded separately; source occurrence
    cannot upgrade either.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2717-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295–306
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: choose_pathway preserves zero/multiple predictions as UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2717-local-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch272/root-native-five-gates-acceptance-001.json
  locator: /accepted; /all_five_commands_exit_zero; /selected_queue_rows
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Five original local commands passed; queue entries are leads, not automatic
    scientific defects or complete QC.
  snapshot_sha256: 7f601817efeea14be333affd31eb25acaf490f1f4449a89d71c78d6bd018cfa0
- evidence_id: support-2717-reader-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-selected-mechanism-profile-001.json
  locator: /mechanisms; /selected_reader_orders
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Only2719/2720 require maintained graph/pathway resolution; Jamaicamide
    C stays unselected context.
  snapshot_sha256: c6142f398d28e745fd5cca30e6ae76655b62a77d43154ff65767d7d14e22b383
- evidence_id: support-2717-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete saved mibig_compounds predicate and all 1 positive placements
    or bounded negative result.
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"positive_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "MHOOPNKRBMHHEC-RIAPOHOLSA-N"}'
- evidence_id: support-2717-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Whole physical TSV rows and parsed dictionaries at /contexts/10/source_scope_inventory/joins/mibig_compounds/matches
    in the pinned inventory
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: All positive fields, physical line bounds/raw spans and row digests personally
    read and joined in the attributed source receipt.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2717-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete saved chebi_structures predicate and all 0 positive placements
    or bounded negative result.
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"positive_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "MHOOPNKRBMHHEC-RIAPOHOLSA-N"}'
- evidence_id: support-2717-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete saved lotus_occurrences predicate and all 3 positive placements
    or bounded negative result.
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"positive_placements": 3, "predicate": "exact complete standard_inchi_key
    equality", "query": "MHOOPNKRBMHHEC-RIAPOHOLSA-N"}'
- evidence_id: support-2717-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Whole physical TSV rows and parsed dictionaries at /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches
    in the pinned inventory
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: All positive fields, physical line bounds/raw spans and row digests personally
    read and joined in the attributed source receipt.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2717-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences predicate and all 0 positive placements
    or bounded negative result.
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"positive_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "MHOOPNKRBMHHEC-RIAPOHOLSA-N"}'
- evidence_id: support-2717-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete saved npclassifier predicate and all 1 positive placements or
    bounded negative result.
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"positive_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "MHOOPNKRBMHHEC-RIAPOHOLSA-N"}'
- evidence_id: support-2717-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Whole physical TSV rows and parsed dictionaries at /contexts/10/source_scope_inventory/joins/npclassifier/matches
    in the pinned inventory
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: All positive fields, physical line bounds/raw spans and row digests personally
    read and joined in the attributed source receipt.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2717-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete saved pubchem_bioassay predicate and all 0 positive placements
    or bounded negative result.
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"positive_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "MHOOPNKRBMHHEC-RIAPOHOLSA-N"}'
- evidence_id: support-2717-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete saved bindingdb_targets predicate and all 0 positive placements
    or bounded negative result.
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"positive_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "MHOOPNKRBMHHEC-RIAPOHOLSA-N"}'
- evidence_id: support-2717-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys predicate and all 0 positive placements
    or bounded negative result.
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"positive_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "MHOOPNKRBMHHEC-RIAPOHOLSA-N"}'
- evidence_id: support-2717-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Complete saved chebi_origins predicate and all 0 positive placements or
    bounded negative result.
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: '{"positive_placements": 0, "predicate": "exact chebi_id from exact
    full-key structure rows", "query": []}'
- evidence_id: support-2717-taxon-predicates
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch272-tentative/bgc-prep/bgc-conditional272-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/source_taxa; /contexts/10/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/10/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-06T13:24:15.016679Z'
  support: supports
  summary: Exact owner-local taxon route and negative merge/nonorganism frames; no
    companion-route substitution.
  snapshot_sha256: 9076082ebb296dcca1064715a0e840feaaa4c1c0005da100cb0ae9db78b9bb40
  search_scope: Captured taxon IDs only; complete retained merge/nonorganism predicates,
    no live taxonomy.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-272/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json
  accessed_at: '2026-11-06T12:48:19.529888Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: fd0cb34130c3476f25db169b5325777ebb89e90a074ab9e1f366e3f2457ccedd
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-272/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json
  accessed_at: '2026-11-06T12:48:43.420906Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: c1d32476a8c22a015b77eee75bb463a26856281054e90ab736ad3a6daa2ddb31
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-272/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json
  accessed_at: '2026-11-06T12:49:02.369675Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-272/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json
  accessed_at: '2026-11-06T12:49:35.366970Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-272/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-272/native-current272-five-gates-execution-001.json
  accessed_at: '2026-11-06T12:49:46.753813Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: bbd68fc20f1f48e4ea8a6a703a235b662c04e17f7a9e47c3fcef4bc064c02e09
assessments:
- area: identity
  topic: Retained identity and grounding
  dimensions:
  - name: standard_inchi_key
    definition: Exact full key; no prefix or name substitution.
    value: MHOOPNKRBMHHEC-RIAPOHOLSA-N
    evidence_ids:
    - support-2717-identity
    - support-2717-molecular-DATA
    - support-2717-query-mibig_compounds
    - support-2717-query-chebi_structures
    - support-2717-source-plan
    - support-2717-source-reading
  - name: grounding_scope
    definition: Stored grounding fidelity is distinct from fresh natural-identity
      verification.
    value: MINTED retained full-key mapping; no independent natural-identity proof
    evidence_ids:
    - support-2717-identity
    - support-2717-molecular-DATA
    - support-2717-query-mibig_compounds
    - support-2717-query-chebi_structures
    - support-2717-source-plan
    - support-2717-source-reading
  assessment_id: support-2717-identity
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  evidence_ids:
  - support-2717-identity
  - support-2717-molecular-DATA
  - support-2717-query-mibig_compounds
  - support-2717-query-chebi_structures
  - support-2717-source-plan
  - support-2717-source-reading
  outcome: supported
  summary: MIBiG BGC0000161 v4 and full key MHOOPNKRBMHHEC-RIAPOHOLSA-N support the
    minted isoterrein mapping. The literal NPAtlas cross-reference NPA019504 is retained
    without fresh resolution. No exact retained ChEBI structure or distinct same-BGC
    companion was returned by the bounded scope; no name-only or partial-key substitution
    is made.
- area: representation
  topic: Stored forms and stereochemistry
  dimensions:
  - name: stereochemistry_scope
    definition: Saved original atom-center and double-bond scope; no natural stereochemistry
      proof.
    value: Two specified S atom centres and one E side-chain alkene in both forms;
      no potential ring-double geometry entry.
    evidence_ids:
    - support-2717-identity
    - support-2717-molecular-DATA
    - support-2717-molecular-reading
    - support-2717-diagnostic-acceptance
    - support-2717-diagnostic-execution
    - support-2717-stereo-policy
  - name: representation_correspondence
    definition: Normalized InChI/key agreement does not prove full fixed-form graph
      equivalence.
    value: Both canonical comparisons true; existing complete11-index one-way map;
      full-identity flag remains false.
    evidence_ids:
    - support-2717-identity
    - support-2717-molecular-DATA
    - support-2717-molecular-reading
    - support-2717-diagnostic-acceptance
    - support-2717-diagnostic-execution
    - support-2717-stereo-policy
  assessment_id: support-2717-representation
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  evidence_ids:
  - support-2717-identity
  - support-2717-molecular-DATA
  - support-2717-molecular-reading
  - support-2717-diagnostic-acceptance
  - support-2717-diagnostic-execution
  - support-2717-stereo-policy
  outcome: supported
  summary: The two saved forms agree on neutral C8H10O3, 11 atoms, 11 bonds, both
    canonical SMILES strings, StandardInChI and full key. The existing complete one-way
    11-index correspondence supports this limited comparison, while full_graph_identity_established
    explicitly remains false. Both forms contain one five-carbon ring, one ketone,
    two hydroxyl groups, two specified tetrahedral centres with saved S labels and
    one specified E side-chain alkene. The ring double bond has no potential-double-stereo
    entry. No ester, amide, C(OH)=N or candidate C5O sugar ring is present. These
    saved results do not independently establish natural configuration. Four charge-rearrangement
    and four undefined-stereo warnings in shared stderr remain globally unassigned.
- area: provenance
  topic: Producer, taxonomy and locus grades
  dimensions:
  - name: taxon_scope
    definition: Cached IDs/names/synonyms are distinct from verified rank, lineage
      or strain identity.
    value: NIH2624 / NCBITaxon:341663 producer;33178 and36630 occurrence routes stay
      separate.
    evidence_ids:
    - support-2717-producer-locus
    - support-2717-taxonomy
    - support-2717-taxon-predicates
    - support-2717-curation
    - support-2717-grade-policy
    - support-2717-query-mibig_compounds
  - name: producer_evidence
    definition: Retained producer grade, not inferred from occurrence or locus association.
    value: BGC_CHARACTERIZED for NIH2624, retained at source grain.
    evidence_ids:
    - support-2717-producer-locus
    - support-2717-taxonomy
    - support-2717-taxon-predicates
    - support-2717-curation
    - support-2717-grade-policy
    - support-2717-query-mibig_compounds
  - name: locus_evidence
    definition: Retained compound-specific cluster-link grade and source methods.
    value: CLUSTER_DEMONSTRATED; CH476594.1:399827–432585; knock-out, heterologous
      and correlation methods.
    evidence_ids:
    - support-2717-producer-locus
    - support-2717-taxonomy
    - support-2717-taxon-predicates
    - support-2717-curation
    - support-2717-grade-policy
    - support-2717-query-mibig_compounds
  assessment_id: support-2717-provenance
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  evidence_ids:
  - support-2717-producer-locus
  - support-2717-taxonomy
  - support-2717-taxon-predicates
  - support-2717-curation
  - support-2717-grade-policy
  - support-2717-query-mibig_compounds
  outcome: supported
  summary: Aspergillus terreus NIH2624 / NCBITaxon:341663 retains BGC_CHARACTERIZED,
    separately from the BGC0000161 v4 CLUSTER_DEMONSTRATED link. The saved methods
    are knock-out studies, heterologous expression and expression correlated with
    production; the maintained grading table supports keeping the organism and cluster
    questions separate. The locus is CH476594.1:399827–432585. Species-level A. terreus33178
    and A. fischeri36630 occurrence routes do not replace the NIH2624 strain or prove
    production by every occurrence taxon.
- area: evidence
  topic: Citation and history scope
  dimensions:
  - name: citation_scope
    definition: Exact retained citation basis; no implied new primary-source access.
    value: ENTRY PMID:24816227; two LOTUS DOI routes, source aliases at36630; two
      seeding events.
    evidence_ids:
    - support-2717-history-citations
    - support-2717-source-reading
    - support-2717-notes
    - support-2717-table-mibig_compounds
    - support-2717-table-lotus_occurrences
    - support-2717-table-npclassifier
    - support-2717-query-mibig_compounds
    - support-2717-query-chebi_structures
    - support-2717-query-lotus_occurrences
    - support-2717-query-cyanometdb_occurrences
    - support-2717-query-npclassifier
    - support-2717-query-pubchem_bioassay
    - support-2717-query-bindingdb_targets
    - support-2717-query-antibioticmech_inchikeys
    - support-2717-query-chebi_origins
  assessment_id: support-2717-citations
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  evidence_ids:
  - support-2717-history-citations
  - support-2717-source-reading
  - support-2717-notes
  - support-2717-table-mibig_compounds
  - support-2717-table-lotus_occurrences
  - support-2717-table-npclassifier
  - support-2717-query-mibig_compounds
  - support-2717-query-chebi_structures
  - support-2717-query-lotus_occurrences
  - support-2717-query-cyanometdb_occurrences
  - support-2717-query-npclassifier
  - support-2717-query-pubchem_bioassay
  - support-2717-query-bindingdb_targets
  - support-2717-query-antibioticmech_inchikeys
  - support-2717-query-chebi_origins
  outcome: supported
  summary: PMID:24816227 is the MIBiG ENTRY citation. LOTUS retains DOI:10.1016/J.CHEMBIOL.2014.03.010
    for A. terreus and DOI:10.2520/MYCO.56.3 for two source rows naming Aspergillus
    fischeri and Neosartorya fischeri at the same taxon36630. Their publication independence
    is not established. Both seeding events remain unchanged; no paper was reopened.
- area: evidence
  topic: Occurrence, assay and target boundaries
  dimensions:
  - name: occurrence_scope
    definition: Source placements and shared citations are not independent production
      experiments.
    value: Three physical LOTUS rows yield two taxon/reference occurrences; aliases
      do not add independent experiments.
    evidence_ids:
    - support-2717-occurrence
    - support-2717-source-reading
    - support-2717-curation
    - support-2717-taxon-predicates
    - support-2717-table-mibig_compounds
    - support-2717-table-lotus_occurrences
    - support-2717-table-npclassifier
    - support-2717-query-mibig_compounds
    - support-2717-query-chebi_structures
    - support-2717-query-lotus_occurrences
    - support-2717-query-cyanometdb_occurrences
    - support-2717-query-npclassifier
    - support-2717-query-pubchem_bioassay
    - support-2717-query-bindingdb_targets
    - support-2717-query-antibioticmech_inchikeys
    - support-2717-query-chebi_origins
  - name: assay_target_scope
    definition: Actual AIDs, blank sentinels and bounded negative target queries remain
      distinct.
    value: No retained assay rows, sentinel, BindingDB target or related-corpus match;
      bounded negatives only.
    evidence_ids:
    - support-2717-occurrence
    - support-2717-source-reading
    - support-2717-curation
    - support-2717-taxon-predicates
    - support-2717-table-mibig_compounds
    - support-2717-table-lotus_occurrences
    - support-2717-table-npclassifier
    - support-2717-query-mibig_compounds
    - support-2717-query-chebi_structures
    - support-2717-query-lotus_occurrences
    - support-2717-query-cyanometdb_occurrences
    - support-2717-query-npclassifier
    - support-2717-query-pubchem_bioassay
    - support-2717-query-bindingdb_targets
    - support-2717-query-antibioticmech_inchikeys
    - support-2717-query-chebi_origins
  assessment_id: support-2717-occurrence-activity
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  evidence_ids:
  - support-2717-occurrence
  - support-2717-source-reading
  - support-2717-curation
  - support-2717-taxon-predicates
  - support-2717-table-mibig_compounds
  - support-2717-table-lotus_occurrences
  - support-2717-table-npclassifier
  - support-2717-query-mibig_compounds
  - support-2717-query-chebi_structures
  - support-2717-query-lotus_occurrences
  - support-2717-query-cyanometdb_occurrences
  - support-2717-query-npclassifier
  - support-2717-query-pubchem_bioassay
  - support-2717-query-bindingdb_targets
  - support-2717-query-antibioticmech_inchikeys
  - support-2717-query-chebi_origins
  outcome: supported
  summary: 'The three physical LOTUS placements reduce to two written taxon/reference
    occurrences: A. terreus33178 and A. fischeri36630. The two source labels sharing36630
    and the same DOI are not separate production experiments; the retained seeder
    deduplicates exact taxon/reference pairs. All saved assay, BindingDB and related-corpus
    frames are empty for this owner. That is a finite data boundary, not proof of
    inactivity or no biological role.'
- area: consistency
  topic: Classification and saved topology
  dimensions:
  - name: classification_applicability
    definition: Local encoded topology can support a broad description without validating
      a model-derived pathway or natural identity.
    value: Zero model pathway labels yield UNCLASSIFIED; all family arrays empty;
      hydroxylated cyclopentenone topology only.
    evidence_ids:
    - support-2717-classification
    - support-2717-molecular-DATA
    - support-2717-molecular-reading
    - support-2717-filing-policy
    - support-2717-query-npclassifier
    - support-2717-query-mibig_compounds
  assessment_id: support-2717-classification
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  evidence_ids:
  - support-2717-classification
  - support-2717-molecular-DATA
  - support-2717-molecular-reading
  - support-2717-filing-policy
  - support-2717-query-npclassifier
  - support-2717-query-mibig_compounds
  outcome: supported
  summary: NPClassifier pathway, superclass and class arrays are all empty and is_glycoside:false.
    The maintained zero-label branch intentionally returns UNCLASSIFIED. A hydroxylated
    cyclopentenone with an E side-chain alkene is supported by the saved topology,
    but assigning a model pathway or natural biosynthetic family would exceed these
    rows. The MIBiG PKS class remains a locus-level annotation.
- area: completeness
  topic: Scientific completion and ownership
  dimensions:
  - name: review_completion
    definition: Coverage of a whole record is distinct from all required checks and
      independent external verification.
    value: partial; scientific_review:true;5 local commands passed; full QC/OAK/live
      primary unavailable
    evidence_ids:
    - support-2717-owner
    - support-2717-capture
    - support-2717-intake
    - support-2717-intake-original
    - support-2717-intake-acceptance
    - support-2717-source-plan
    - support-2717-source-plan-acceptance
    - support-2717-source-reading
    - support-2717-notes
    - support-2717-diagnostic-acceptance
    - support-2717-molecular-reading
    - support-2717-local-gates
    - support-2717-reader-scope
  assessment_id: support-2717-completion
  target_ids:
  - naturalproductmech:mibig-ef6e0053ae
  evidence_ids:
  - support-2717-owner
  - support-2717-capture
  - support-2717-intake
  - support-2717-intake-original
  - support-2717-intake-acceptance
  - support-2717-source-plan
  - support-2717-source-plan-acceptance
  - support-2717-source-reading
  - support-2717-notes
  - support-2717-diagnostic-acceptance
  - support-2717-molecular-reading
  - support-2717-local-gates
  - support-2717-reader-scope
  outcome: unknown
  summary: Whole owner/history, every assigned saved source frame/positive dictionary,
    both complete molecular tables and actual intake claims were read. Current input
    hashes and ownership match the accepted plan; that is distinct from whole-corpus
    scientific reading. Five local commands passed. Full QC, OAK grounding and live
    primary-source verification remain unavailable under the request hold. No graph/pathway
    reader applies to this owner. Completion is partial.
findings: []
actions: []
limitations:
- Retained owner/source rows and accepted original local outputs only; no fresh primary
  publication, taxonomy, sequence or external-identifier resolution.
- The eleven-atom one-way match and canonical agreement are limited stored-form checks;
  they do not establish natural identity, experimental stereochemical assignment or
  production by the species-level occurrence taxa.
- Four charge-rearrangement and four undefined-stereo warnings are global and unassigned.
  Full QC/OAK and live primary verification remain unavailable; source grades and
  citation grain are not upgraded.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete selected owner/history, saved source frames and both molecular tables personally
  read; positive row placements are not independent experiments and hash verification
  is not whole-corpus reading.
- No source, record, curation-status or history edit is proposed. No outbound request,
  new parse or target execution occurred in this authoring lane.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-272
```
