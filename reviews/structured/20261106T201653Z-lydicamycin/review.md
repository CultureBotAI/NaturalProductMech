# Local evidence review: lydicamycin

- Review: 20261106T201653Z-lydicamycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T19:49:35.594612Z
- Finished UTC: 2026-11-06T20:16:53.788358Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Lydicamycin retains fourteen unspecified atom centres and a representation-dependent lactam/imidic-acid difference. All normalized identifiers agree, while canonical comparisons and correspondence remain false. Source entry completeness, occurrence taxa and the blank-assay sentinel do not strengthen molecular or producer certainty.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2758; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-a0453972fa | data/natural_products/unclassified/lydicamycin.yaml | generated | lydicamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-a0453972fa | Both stored forms parsed in the accepted original run and regenerate the declared normalized identifiers and formula; explicit graph equivalence is not established. |
| strict_ten | passed | True | naturalproductmech:mibig-a0453972fa | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-a0453972fa | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-a0453972fa | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-a0453972fa | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-a0453972fa | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-a0453972fa | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-a0453972fa | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-a0453972fa | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact source identity and grounding boundaries

identity: supported. Targets: naturalproductmech:mibig-a0453972fa.

Lydicamycin retains the exact MIBiG BGC0001477 compound 1 route and full structure key. Entry completeness metadata is separate from atom stereochemical completeness and from experimental confirmation of this stored representation.

### Stored molecular representations and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-a0453972fa.

Both saved forms are neutral C47H74N4O10 with 61 atoms, 64 bonds and one fragment. Their four saved rings include two fused six-membered carbon rings, a five-membered nitrogen ring bearing a guanidino group, and a separate five-membered carbonyl-containing nitrogen ring. The source has two carbonyls and one strict amide; the InChI-derived form has one carbonyl, no strict amide and one terminal C(OH)=N site in the latter ring. No ester or saturated C5O candidate ring is detected. These are explicit representation differences, not a full-graph equivalence proof. All fourteen potential tetrahedral centres remain unspecified in both forms. The source saved bond enums show five STEREOE double bonds; the InChI-derived graph shows four STEREOE and one STEREOZ at the exocyclic enol linkage, alongside the changed lactam/imidic representation and substituent priorities. This descriptor difference is retained without inferring experimental isomerization or a verified atom map. Both forms also have one unspecified guanidino C=N potential-stereo entry. The source stereo_complete false remains appropriate. Two shared original-run warnings remain globally unassigned.

### Separate producer and locus source grades

provenance: supported. Targets: naturalproductmech:mibig-a0453972fa.

BGC0001477 version 5 supplies Streptomyces sp. ID38640 NCBITaxon:1265399 and MG459168.1 with blank coordinates and method. SOURCE_ASSERTION and CLUSTER_UNSTATED remain the supported grades. The row's active/questionable/complete status describes the source entry, not a demonstrated producer or a complete stereochemical assignment.

### Citation grain and source attribution

evidence: supported. Targets: naturalproductmech:mibig-a0453972fa.

Both seeding-history events were read. DOI:10.1016/j.chembiol.2018.02.008 is entry-level MIBiG provenance; its uppercase LOTUS rendering is a citation-case duplicate, not a second independent publication. DOI:10.3389/FMICB.2019.02077 is a separate occurrence placement. Primary text and experiments were not newly verified.

### Occurrence, assays and target boundaries

evidence: supported. Targets: naturalproductmech:mibig-a0453972fa.

The two LOTUS rows concern Streptomyces NCBITaxon:1883 and Streptomyces lydicus NCBITaxon:47763, with their separate DOI placements. Neither establishes the exact ID38640 producer or its locus association. The PubChem CID:90469739 row is a blank-AID sentinel with no assay measurement or target. ChemSpider:4943765 is an identifier cross-reference, not assay evidence. Empty BindingDB and other frames remain local bounded negatives.

### Filing and classifier applicability

consistency: supported. Targets: naturalproductmech:mibig-a0453972fa.

NPClassifier reports two pathway labels with Cyclic polyketides and 3-Decalinoyltetramic acids, is_glycoside false. UNCLASSIFIED is the intended multi-label filing. The source fused carbon-ring system and five-membered nitrogen/dicarbonyl motif are compatible with broad cyclic-polyketide/tetramic-acid model language. The exact unsaturation, unassigned centres and tautomer-sensitive carbonyl/amide counts limit residue, positional and biosynthetic claims; no independent model validation is claimed.

### Scope and unavailable required checks

completeness: supported. Targets: naturalproductmech:mibig-a0453972fa.

Whole current owner/history and complete assigned saved source/molecular tables were personally read and joined to original canonical intakes. No graph, pathway, target or component root requires a maintained reader. Five local native commands passed; full QC, OAK consistency and external primary/authority verification remain unavailable, so completion is partial. No actionable defect was established within the retained scope; incomplete or representation-dependent chemistry remains explicit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2758-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/lydicamycin.yaml; Complete current raw owner and all 2 history events | supports | Whole current owner and history personally read; exact bytes join the accepted capture. |
| support-2758-capture | /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json; /records/7 | supports | Complete current captured owner and negative literal mechanism/component roots; no maintained-reader result is assigned. |
| support-2758-identity | /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json; /records/7/owner_document/identifier; /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts; /records/7/owner_document/xrefs; /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes | supports | Exact current identifier, source names, concepts and full key; source grouping is not natural-identity verification. |
| support-2758-producer-locus | /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json; /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters | supports | Separate source producer and locus claims retain exact taxon/accession/method/grade scope. |
| support-2758-history-citations | /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json; /records/7/owner_document/curation_history; /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters | supports | All history and claim citation placements, without fresh primary text or sequence verification. |
| support-2758-occurrence | /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json; /records/7/owner_document/occurrences; /records/7/owner_document/occurrence_taxon_groups | supports | Retained occurrences remain distinct from demonstrated production and causal locus evidence. |
| support-2758-classification | /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json; /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification; /records/7/owner_document/bgc_class; /records/7/owner_document/biosynthesis_origin | supports | Computed classification, source BGC labels and current filing are separate claims. |
| support-2758-intake | /private/tmp/npm-review-work/shared-next-batch276/intakes-001/2758-inspect-001.json; /status; /source; /targets | supports | Actual canonical intake captures owner, source hashes and maintained ownership; inspection alone is not scientific completion. |
| support-2758-intake-original | /private/tmp/npm-review-work/shared-next-batch276/intakes-001/intake-summary-001.json; /receipts/7 | supports | Actual original intake command, exit 0 and empty stderr, preserved without replay. |
| support-2758-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch276/root-current276-intake-acceptance-001.json; /accepted; /intake_summary; /source_placements; /unique_source_paths; /all_stderr_empty; /maintained_reader_invocations | supports | ROOT accepted all ten original canonical intakes, 452 input placements/53 paths and zero maintained readers. |
| support-2758-source-plan | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-target-input-plan-001.json; /records/7 | supports | Exact owner-specific source and maintained implementation inputs; companions do not transfer scientific claims. |
| support-2758-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch276/root-current276-input-plan-acceptance-001.json; /accepted; /source_plan; /source_scope_notes; /all_selected_related_corpora_routes_complete; /original_scoped_rows; /maintained_reader_orders | supports | Accepted current input routes preserve 39 original source rows and the explicit Lysocin E AntibioticMech route; no reader assigned. |
| support-2758-source-reading | /private/tmp/npm-review-work/shared-next-batch276-tentative/support-prep/support-current276-assigned-source-reading-001.json; /contexts/2; /counts; /primary_context_indices | supports | Personally read complete saved row dictionaries, physical spans and negative predicates for this owner. |
| support-2758-notes | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-scope-notes-001.json; /reading; /reading_reconciliation; /reading_boundaries; /cautions/support_context_interpretations/2 | supports | Disjoint BGC 15 / Support 24 source attribution and exact current copied interpretations; no extra primary credit. |
| support-2758-taxonomy | /private/tmp/npm-review-work/shared-next-batch276-tentative/native-prep/native-current276-cached-taxonomy-reading-001.json; /context_interpretations/7; /interpretation | supports | Native attributed complete cached ID/label stanzas; no new rank, lineage, strain or external-taxonomy verification. |
| support-2758-curation | /private/tmp/npm-review-work/shared-next-batch276-tentative/native-prep/native-current276-implemented-curation-scan-001.json; /counts; /exact_applicability_resolution; /implementation_scope; /interpretation | supports | Native bounded substantive-table scan found no exact applicable existing correction; lexical overlaps do not establish applicability. |
| support-2758-molecular-DATA | /private/tmp/npm-review-work/shared-next-batch276/chemistry-local/diagnostic-DATA-001.json; /records/7 | supports | Original saved two-form atom/bond/ring/stereo/motif data, false canonical comparisons and empty map; no new parse. |
| support-2758-molecular-reading | /private/tmp/npm-review-work/shared-next-batch276-tentative/support-prep/support-current276-last-five-molecular-intake-reading-001.json; /records/2; /counts; /warning_stream; /limits | supports | Personal complete saved-table reading and actual intake joins; secondary source strings were not additional parsed molecules. |
| support-2758-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch276/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /false_comparisons_preserved; /unassigned_undefined_stereo_warning_lines | supports | Accepted original 20-form diagnostic; two warnings remain global and unassigned. |
| support-2758-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch276/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr; /retries; /external_requests | supports | Exact original command and stored streams, exit 0 with no retries or requests. |
| support-2758-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165–172 | supports | Source stereo_complete uses atom-centred chiral-centre assignment; it is not a blanket bond-geometry or experimental-completeness claim. |
| support-2758-grade-policy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; lines 18–40 | supports | Organism and locus grades are separately derived; knockout support does not transfer to a separate assertion-only source route. |
| support-2758-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295–306 | supports | The maintained seeder intentionally files zero/multiple model pathway labels UNCLASSIFIED. |
| support-2758-local-gates | /private/tmp/npm-review-work/shared-next-batch276/root-current276-five-gates-acceptance-001.json; /accepted; /ledger; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates | supports | Five actual local commands passed; full QC and OAK remain unavailable, so all native gates have not passed. |
| support-2758-queue | /private/tmp/npm-native-checks/batch-276/review-queue-001.tsv; Physical TSV lines 1451, 4135, 8458 | supports | Current source-evidence, filing, stereochemistry and identity queue prompts were assessed; queue presence alone is not a defect. |
| support-2758-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/mibig_compounds | supports | Complete retained mibig_compounds frame: 1 positive placements, all fields and exact negative predicates read. |
| support-2758-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 1793; complete header/fields in inventory /contexts/7/source_scope_inventory/joins/mibig_compounds/matches | supports | All source fields/blanks personally read; row placements and citation case variants are not automatically independent experiments. |
| support-2758-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_structures | supports | Complete retained chebi_structures frame: 0 positive placements, all fields and exact negative predicates read. |
| support-2758-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained lotus_occurrences frame: 2 positive placements, all fields and exact negative predicates read. |
| support-2758-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 2528, 2529; complete header/fields in inventory /contexts/7/source_scope_inventory/joins/lotus_occurrences/matches | supports | All source fields/blanks personally read; row placements and citation case variants are not automatically independent experiments. |
| support-2758-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained cyanometdb_occurrences frame: 0 positive placements, all fields and exact negative predicates read. |
| support-2758-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/npclassifier | supports | Complete retained npclassifier frame: 1 positive placements, all fields and exact negative predicates read. |
| support-2758-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 868; complete header/fields in inventory /contexts/7/source_scope_inventory/joins/npclassifier/matches | supports | All source fields/blanks personally read; row placements and citation case variants are not automatically independent experiments. |
| support-2758-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained pubchem_bioassay frame: 1 positive placements, all fields and exact negative predicates read. |
| support-2758-table-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 2567; complete header/fields in inventory /contexts/7/source_scope_inventory/joins/pubchem_bioassay/matches | supports | All source fields/blanks personally read; row placements and citation case variants are not automatically independent experiments. |
| support-2758-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained bindingdb_targets frame: 0 positive placements, all fields and exact negative predicates read. |
| support-2758-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained antibioticmech_inchikeys frame: 0 positive placements, all fields and exact negative predicates read. |
| support-2758-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_origins | supports | Complete retained chebi_origins frame: 0 positive placements, all fields and exact negative predicates read. |
| support-2758-taxon-predicates | /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/source_taxa; /contexts/7/source_scope_inventory/forward_taxon_merge_matches; /contexts/7/source_scope_inventory/nonorganism_matches | supports | Exact source-ID merge and nonorganism frames retain their negative scope. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-276/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-276/native-current276-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-276/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-276/native-current276-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-276/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-276/native-current276-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-276/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-276/native-current276-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-276/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-276/native-current276-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Primary publications, spectra, sequences, live taxonomy and natural-product identity were not independently verified; full QC/OAK/external checks remain unavailable.
- Both canonical flags are false and the limited correspondence is empty/incomplete, with full_graph_identity_established false despite normalized StandardInChI/key/formula equality. The five specified bond descriptors do not repair fourteen unresolved atom centres. All fourteen potential tetrahedral centres remain unspecified in both forms. The source saved bond enums show five STEREOE double bonds; the InChI-derived graph shows four STEREOE and one STEREOZ at the exocyclic enol linkage, alongside the changed lactam/imidic representation and substituent priorities. This descriptor difference is retained without inferring experimental isomerization or a verified atom map. Both forms also have one unspecified guanidino C=N potential-stereo entry. The source stereo_complete false remains appropriate. The two diagnostic warnings remain globally unassigned.
- Exact-key/ID negatives and cached taxonomy are bounded by captured files and predicates, not universal absence, inactivity or a producer-grade upgrade.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh current batch 276 judgments use earned owner/source/intake/diagnostic evidence; prior batches supplied interface logic only.
- No source record or native curation status was changed. Proposed action remains unperformed.
- Five actual native checks and three required unavailable checks are appended by the ROOT assembler; no reader check is assigned to this owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T201653Z-lydicamycin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: lydicamycin'
started_at: '2026-11-06T19:49:35.594612Z'
finished_at: '2026-11-06T20:16:53.788358Z'
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
summary: Lydicamycin retains fourteen unspecified atom centres and a representation-dependent
  lactam/imidic-acid difference. All normalized identifiers agree, while canonical
  comparisons and correspondence remain false. Source entry completeness, occurrence
  taxa and the blank-assay sentinel do not strengthen molecular or producer certainty.
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
  - path: data/natural_products/unclassified/lydicamycin.yaml
    sha256: d475a147dba20ffcaae1fb1b0f9bdaaf2a4f2a800e2391ddda3b6312cee91691
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
  selection: Campaign path order 2758; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-a0453972fa
targets:
- target_id: naturalproductmech:mibig-a0453972fa
  path: data/natural_products/unclassified/lydicamycin.yaml
  label: lydicamycin
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch276/chemistry-local/diagnose276-001.py
    9f107dc593c36d82d7418f2cb93440e9a67b8d2239318d8e0df28704720d0a15 dee9540e42ebdae658c9b534bddd419d26d544ecc44ab7f658de9b98672572d2
    1ae68a3c10d22aace9149a742eb4f4d6ae1fc3aaa028e3e70e583b9f2189cba5
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed in the accepted original run and regenerate the
    declared normalized identifiers and formula; explicit graph equivalence is not
    established.
  scope_note: Both canonical flags are false and the limited correspondence is empty/incomplete,
    with full_graph_identity_established false despite normalized StandardInChI/key/formula
    equality. The five specified bond descriptors do not repair fourteen unresolved
    atom centres. All fourteen potential tetrahedral centres remain unspecified in
    both forms. The source saved bond enums show five STEREOE double bonds; the InChI-derived
    graph shows four STEREOE and one STEREOZ at the exocyclic enol linkage, alongside
    the changed lactam/imidic representation and substituent priorities. This descriptor
    difference is retained without inferring experimental isomerization or a verified
    atom map. Both forms also have one unspecified guanidino C=N potential-stereo
    entry. The source stereo_complete false remains appropriate. Two warnings remain
    globally unassigned; no molecular replay.
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  evidence_ids:
  - support-2758-molecular-DATA
  - support-2758-diagnostic-execution
  - support-2758-diagnostic-acceptance
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  command: just validate-strict data/natural_products/unclassified/lobosamide-a.yaml
    data/natural_products/unclassified/lobosamide-b.yaml data/natural_products/unclassified/lobosamide-c.yaml
    data/natural_products/unclassified/locillomycin-b.yaml data/natural_products/unclassified/locillomycin-c.yaml
    data/natural_products/unclassified/locillomycin.yaml data/natural_products/unclassified/lokisin.yaml
    data/natural_products/unclassified/lydicamycin.yaml data/natural_products/unclassified/lysobactin.yaml
    data/natural_products/unclassified/lysocin-e.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-276/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-a0453972fa
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-276/validate-all-001.tsv
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
  - naturalproductmech:mibig-a0453972fa
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
  - naturalproductmech:mibig-a0453972fa
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
  - naturalproductmech:mibig-a0453972fa
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-276/review-queue-001.tsv
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
  - naturalproductmech:mibig-a0453972fa
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2758-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/lydicamycin.yaml
  locator: Complete current raw owner and all 2 history events
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Whole current owner and history personally read; exact bytes join the accepted
    capture.
  snapshot_sha256: d475a147dba20ffcaae1fb1b0f9bdaaf2a4f2a800e2391ddda3b6312cee91691
- evidence_id: support-2758-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json
  locator: /records/7
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Complete current captured owner and negative literal mechanism/component
    roots; no maintained-reader result is assigned.
  snapshot_sha256: dee9540e42ebdae658c9b534bddd419d26d544ecc44ab7f658de9b98672572d2
- evidence_id: support-2758-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json
  locator: /records/7/owner_document/identifier; /records/7/owner_document/chemical_structure;
    /records/7/owner_document/source_concepts; /records/7/owner_document/xrefs; /records/7/owner_document/grounding_status;
    /records/7/owner_document/grounding_notes
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Exact current identifier, source names, concepts and full key; source grouping
    is not natural-identity verification.
  snapshot_sha256: dee9540e42ebdae658c9b534bddd419d26d544ecc44ab7f658de9b98672572d2
- evidence_id: support-2758-producer-locus
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json
  locator: /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Separate source producer and locus claims retain exact taxon/accession/method/grade
    scope.
  snapshot_sha256: dee9540e42ebdae658c9b534bddd419d26d544ecc44ab7f658de9b98672572d2
- evidence_id: support-2758-history-citations
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json
  locator: /records/7/owner_document/curation_history; /records/7/owner_document/producer_organisms;
    /records/7/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: All history and claim citation placements, without fresh primary text or
    sequence verification.
  snapshot_sha256: dee9540e42ebdae658c9b534bddd419d26d544ecc44ab7f658de9b98672572d2
- evidence_id: support-2758-occurrence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json
  locator: /records/7/owner_document/occurrences; /records/7/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Retained occurrences remain distinct from demonstrated production and causal
    locus evidence.
  snapshot_sha256: dee9540e42ebdae658c9b534bddd419d26d544ecc44ab7f658de9b98672572d2
- evidence_id: support-2758-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch276/owner-capture-DATA-001.json
  locator: /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification;
    /records/7/owner_document/bgc_class; /records/7/owner_document/biosynthesis_origin
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Computed classification, source BGC labels and current filing are separate
    claims.
  snapshot_sha256: dee9540e42ebdae658c9b534bddd419d26d544ecc44ab7f658de9b98672572d2
- evidence_id: support-2758-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch276/intakes-001/2758-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Actual canonical intake captures owner, source hashes and maintained ownership;
    inspection alone is not scientific completion.
  snapshot_sha256: 2daeb0727d503d8928b70bde5bf72e04d2c8dcf883b188803b1eba80504e6a80
- evidence_id: support-2758-intake-original
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch276/intakes-001/intake-summary-001.json
  locator: /receipts/7
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Actual original intake command, exit 0 and empty stderr, preserved without
    replay.
  snapshot_sha256: 1ae68a3c10d22aace9149a742eb4f4d6ae1fc3aaa028e3e70e583b9f2189cba5
- evidence_id: support-2758-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch276/root-current276-intake-acceptance-001.json
  locator: /accepted; /intake_summary; /source_placements; /unique_source_paths; /all_stderr_empty;
    /maintained_reader_invocations
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: ROOT accepted all ten original canonical intakes, 452 input placements/53
    paths and zero maintained readers.
  snapshot_sha256: 4c7fdfaef49a3b91a738015f44ec8f6f95708cd7753455b0e6bcaa06ea367459
- evidence_id: support-2758-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-target-input-plan-001.json
  locator: /records/7
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Exact owner-specific source and maintained implementation inputs; companions
    do not transfer scientific claims.
  snapshot_sha256: fd1afd31a07e870089e795aa2d07db538b56f5b47612c373091de15dc0ad957a
- evidence_id: support-2758-source-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch276/root-current276-input-plan-acceptance-001.json
  locator: /accepted; /source_plan; /source_scope_notes; /all_selected_related_corpora_routes_complete;
    /original_scoped_rows; /maintained_reader_orders
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Accepted current input routes preserve 39 original source rows and the
    explicit Lysocin E AntibioticMech route; no reader assigned.
  snapshot_sha256: 875f26b852611f8671ed5e922ec7f3717c4eb5f011c5c0386c2c053b0244185c
- evidence_id: support-2758-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/support-prep/support-current276-assigned-source-reading-001.json
  locator: /contexts/2; /counts; /primary_context_indices
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Personally read complete saved row dictionaries, physical spans and negative
    predicates for this owner.
  snapshot_sha256: 1b6ee6fbfaacda3c5675eb343bd9d9e7b402c5db8a78211e792fa3fbbdf8614f
- evidence_id: support-2758-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /reading_boundaries; /cautions/support_context_interpretations/2
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Disjoint BGC 15 / Support 24 source attribution and exact current copied
    interpretations; no extra primary credit.
  snapshot_sha256: 9bc332e7eedff1d2c17f3809f559d6c3eedbcafca7c40c429ce400ceb228f9c2
- evidence_id: support-2758-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/native-prep/native-current276-cached-taxonomy-reading-001.json
  locator: /context_interpretations/7; /interpretation
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Native attributed complete cached ID/label stanzas; no new rank, lineage,
    strain or external-taxonomy verification.
  snapshot_sha256: f573223f237b4cac4edccb9b9b5f728126a4b916e911013cdce56e315cd10dd6
- evidence_id: support-2758-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/native-prep/native-current276-implemented-curation-scan-001.json
  locator: /counts; /exact_applicability_resolution; /implementation_scope; /interpretation
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Native bounded substantive-table scan found no exact applicable existing
    correction; lexical overlaps do not establish applicability.
  snapshot_sha256: 3e8d3852a6576c163dc3f665de4a3743c94ccbcc96dda64a9b63e6ee7c63811d
  search_scope: Nine retained substantive tables and six exact identity predicates.
    Two census-only extras are excluded; no biological absence or universal curation-completeness
    inference.
- evidence_id: support-2758-molecular-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch276/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Original saved two-form atom/bond/ring/stereo/motif data, false canonical
    comparisons and empty map; no new parse.
  snapshot_sha256: 1815de0e011d32c221528a9601d4ac7b07df3bce40162650435d75a5ab859a14
- evidence_id: support-2758-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/support-prep/support-current276-last-five-molecular-intake-reading-001.json
  locator: /records/2; /counts; /warning_stream; /limits
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Personal complete saved-table reading and actual intake joins; secondary
    source strings were not additional parsed molecules.
  snapshot_sha256: 3048b9ab16f024c1a9896509f73ea08fa3cec79859c8f9c48a09de158aa96c4b
- evidence_id: support-2758-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch276/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /false_comparisons_preserved; /unassigned_undefined_stereo_warning_lines
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Accepted original 20-form diagnostic; two warnings remain global and unassigned.
  snapshot_sha256: 8faf6dde0eed6148cb627761388db478cd2ade4c5620dc1ca3ee299484880533
- evidence_id: support-2758-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch276/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Exact original command and stored streams, exit 0 with no retries or requests.
  snapshot_sha256: ff211e52436f32be0c3ef7c16cb85bb43ece38a2aea0bd73734caf6d84e1547b
- evidence_id: support-2758-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 165–172
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Source stereo_complete uses atom-centred chiral-centre assignment; it is
    not a blanket bond-geometry or experimental-completeness claim.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2758-grade-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: lines 18–40
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Organism and locus grades are separately derived; knockout support does
    not transfer to a separate assertion-only source route.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2758-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295–306
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: The maintained seeder intentionally files zero/multiple model pathway labels
    UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2758-local-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch276/root-current276-five-gates-acceptance-001.json
  locator: /accepted; /ledger; /five_local_commands_passed; /all_native_gates_passed;
    /unavailable_required_gates
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Five actual local commands passed; full QC and OAK remain unavailable,
    so all native gates have not passed.
  snapshot_sha256: 53706d877239372b99e55a3f09028e216bd34eb279a2fa962b510bd581f5f2c6
- evidence_id: support-2758-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-276/review-queue-001.tsv
  locator: Physical TSV lines 1451, 4135, 8458
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Current source-evidence, filing, stereochemistry and identity queue prompts
    were assessed; queue presence alone is not a defect.
  snapshot_sha256: 0a4d4e609fb4c229bcc04a3e4112dcf3fbfd77a6a362d0f0872fb89b9f35a7cf
- evidence_id: support-2758-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: 'Complete retained mibig_compounds frame: 1 positive placements, all fields
    and exact negative predicates read.'
  snapshot_sha256: 4da6bdc09238fd05d79910ef11efcb8f76d6948fc4bf9f844c9bbc4b574ab91c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HNSRCWWMQWCNGW-YCUXMAJDSA-N", "scope": "Only the pinned retained table and this
    exact key/derived-ID predicate; no replay, universal absence or inactivity inference.",
    "table": "mibig_compounds"}'
- evidence_id: support-2758-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 1793; complete header/fields in inventory /contexts/7/source_scope_inventory/joins/mibig_compounds/matches
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: All source fields/blanks personally read; row placements and citation case
    variants are not automatically independent experiments.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2758-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: 'Complete retained chebi_structures frame: 0 positive placements, all fields
    and exact negative predicates read.'
  snapshot_sha256: 4da6bdc09238fd05d79910ef11efcb8f76d6948fc4bf9f844c9bbc4b574ab91c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HNSRCWWMQWCNGW-YCUXMAJDSA-N", "scope": "Only the pinned retained table and this
    exact key/derived-ID predicate; no replay, universal absence or inactivity inference.",
    "table": "chebi_structures"}'
- evidence_id: support-2758-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: 'Complete retained lotus_occurrences frame: 2 positive placements, all
    fields and exact negative predicates read.'
  snapshot_sha256: 4da6bdc09238fd05d79910ef11efcb8f76d6948fc4bf9f844c9bbc4b574ab91c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HNSRCWWMQWCNGW-YCUXMAJDSA-N", "scope": "Only the pinned retained table and this
    exact key/derived-ID predicate; no replay, universal absence or inactivity inference.",
    "table": "lotus_occurrences"}'
- evidence_id: support-2758-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 2528, 2529; complete header/fields in inventory /contexts/7/source_scope_inventory/joins/lotus_occurrences/matches
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: All source fields/blanks personally read; row placements and citation case
    variants are not automatically independent experiments.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2758-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: 'Complete retained cyanometdb_occurrences frame: 0 positive placements,
    all fields and exact negative predicates read.'
  snapshot_sha256: 4da6bdc09238fd05d79910ef11efcb8f76d6948fc4bf9f844c9bbc4b574ab91c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HNSRCWWMQWCNGW-YCUXMAJDSA-N", "scope": "Only the pinned retained table and this
    exact key/derived-ID predicate; no replay, universal absence or inactivity inference.",
    "table": "cyanometdb_occurrences"}'
- evidence_id: support-2758-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: 'Complete retained npclassifier frame: 1 positive placements, all fields
    and exact negative predicates read.'
  snapshot_sha256: 4da6bdc09238fd05d79910ef11efcb8f76d6948fc4bf9f844c9bbc4b574ab91c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HNSRCWWMQWCNGW-YCUXMAJDSA-N", "scope": "Only the pinned retained table and this
    exact key/derived-ID predicate; no replay, universal absence or inactivity inference.",
    "table": "npclassifier"}'
- evidence_id: support-2758-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 868; complete header/fields in inventory /contexts/7/source_scope_inventory/joins/npclassifier/matches
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: All source fields/blanks personally read; row placements and citation case
    variants are not automatically independent experiments.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2758-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: 'Complete retained pubchem_bioassay frame: 1 positive placements, all fields
    and exact negative predicates read.'
  snapshot_sha256: 4da6bdc09238fd05d79910ef11efcb8f76d6948fc4bf9f844c9bbc4b574ab91c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HNSRCWWMQWCNGW-YCUXMAJDSA-N", "scope": "Only the pinned retained table and this
    exact key/derived-ID predicate; no replay, universal absence or inactivity inference.",
    "table": "pubchem_bioassay"}'
- evidence_id: support-2758-table-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 2567; complete header/fields in inventory /contexts/7/source_scope_inventory/joins/pubchem_bioassay/matches
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: All source fields/blanks personally read; row placements and citation case
    variants are not automatically independent experiments.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2758-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: 'Complete retained bindingdb_targets frame: 0 positive placements, all
    fields and exact negative predicates read.'
  snapshot_sha256: 4da6bdc09238fd05d79910ef11efcb8f76d6948fc4bf9f844c9bbc4b574ab91c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HNSRCWWMQWCNGW-YCUXMAJDSA-N", "scope": "Only the pinned retained table and this
    exact key/derived-ID predicate; no replay, universal absence or inactivity inference.",
    "table": "bindingdb_targets"}'
- evidence_id: support-2758-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: 'Complete retained antibioticmech_inchikeys frame: 0 positive placements,
    all fields and exact negative predicates read.'
  snapshot_sha256: 4da6bdc09238fd05d79910ef11efcb8f76d6948fc4bf9f844c9bbc4b574ab91c
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HNSRCWWMQWCNGW-YCUXMAJDSA-N", "scope": "Only the pinned retained table and this
    exact key/derived-ID predicate; no replay, universal absence or inactivity inference.",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: support-2758-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: 'Complete retained chebi_origins frame: 0 positive placements, all fields
    and exact negative predicates read.'
  snapshot_sha256: 4da6bdc09238fd05d79910ef11efcb8f76d6948fc4bf9f844c9bbc4b574ab91c
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "scope": "Only the pinned retained table and this exact key/derived-ID
    predicate; no replay, universal absence or inactivity inference.", "table": "chebi_origins"}'
- evidence_id: support-2758-taxon-predicates
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch276-tentative/bgc-prep/bgc-conditional276-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/source_taxa; /contexts/7/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/7/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-06T20:08:43.198360Z'
  support: supports
  summary: Exact source-ID merge and nonorganism frames retain their negative scope.
  snapshot_sha256: 4da6bdc09238fd05d79910ef11efcb8f76d6948fc4bf9f844c9bbc4b574ab91c
  search_scope: This context source IDs against pinned local tables only; no reverse
    inference or live taxonomy.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-276/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-276/native-current276-five-gates-execution-001.json
  accessed_at: '2026-11-06T19:50:19.560693Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 422da94bca9606ad2cfca4c1acf62a06b9fecd756221a3caefa700a058ccc098
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-276/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-276/native-current276-five-gates-execution-001.json
  accessed_at: '2026-11-06T19:50:44.844266Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: b1102434243b0570ac0eac3f9efd2300adc63fb360ca450689d3315ca74703c1
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-276/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-276/native-current276-five-gates-execution-001.json
  accessed_at: '2026-11-06T19:51:04.516355Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-276/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-276/native-current276-five-gates-execution-001.json
  accessed_at: '2026-11-06T19:51:38.246028Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-276/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-276/native-current276-five-gates-execution-001.json
  accessed_at: '2026-11-06T19:51:49.910656Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: b3588ca2411afc8ef52486c8f2134681c077f3b2fa8061a2624addc12b3802ed
assessments:
- assessment_id: support-2758-identity-assessment
  area: identity
  topic: Exact source identity and grounding boundaries
  summary: Lydicamycin retains the exact MIBiG BGC0001477 compound 1 route and full
    structure key. Entry completeness metadata is separate from atom stereochemical
    completeness and from experimental confirmation of this stored representation.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  evidence_ids:
  - support-2758-identity
  - support-2758-capture
  - support-2758-source-reading
  - support-2758-source-plan
  - support-2758-source-plan-acceptance
  - support-2758-notes
  - support-2758-curation
  - support-2758-query-mibig_compounds
  - support-2758-query-chebi_structures
  - support-2758-query-lotus_occurrences
  - support-2758-query-cyanometdb_occurrences
  - support-2758-query-npclassifier
  - support-2758-query-pubchem_bioassay
  - support-2758-query-bindingdb_targets
  - support-2758-query-antibioticmech_inchikeys
  - support-2758-query-chebi_origins
  - support-2758-table-mibig_compounds
  - support-2758-table-lotus_occurrences
  - support-2758-table-npclassifier
  - support-2758-table-pubchem_bioassay
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete key without prefix or name substitution.
    value: HNSRCWWMQWCNGW-YCUXMAJDSA-N
    evidence_ids:
    - support-2758-identity
    - support-2758-capture
    - support-2758-source-reading
    - support-2758-source-plan
    - support-2758-source-plan-acceptance
    - support-2758-notes
    - support-2758-curation
    - support-2758-query-mibig_compounds
    - support-2758-query-chebi_structures
    - support-2758-query-lotus_occurrences
    - support-2758-query-cyanometdb_occurrences
    - support-2758-query-npclassifier
    - support-2758-query-pubchem_bioassay
    - support-2758-query-bindingdb_targets
    - support-2758-query-antibioticmech_inchikeys
    - support-2758-query-chebi_origins
    - support-2758-table-mibig_compounds
    - support-2758-table-lotus_occurrences
    - support-2758-table-npclassifier
    - support-2758-table-pubchem_bioassay
  - name: grounding_scope
    definition: Retained grounding is distinct from natural-sample identity.
    value: Exact retained MIBiG compound/full-key grounding; neither entry 'complete'
      metadata nor source citation proves complete stereochemistry or natural identity.
    evidence_ids:
    - support-2758-identity
    - support-2758-capture
    - support-2758-source-reading
    - support-2758-source-plan
    - support-2758-source-plan-acceptance
    - support-2758-notes
    - support-2758-curation
    - support-2758-query-mibig_compounds
    - support-2758-query-chebi_structures
    - support-2758-query-lotus_occurrences
    - support-2758-query-cyanometdb_occurrences
    - support-2758-query-npclassifier
    - support-2758-query-pubchem_bioassay
    - support-2758-query-bindingdb_targets
    - support-2758-query-antibioticmech_inchikeys
    - support-2758-query-chebi_origins
    - support-2758-table-mibig_compounds
    - support-2758-table-lotus_occurrences
    - support-2758-table-npclassifier
    - support-2758-table-pubchem_bioassay
- assessment_id: support-2758-representation-assessment
  area: representation
  topic: Stored molecular representations and stereochemistry
  summary: Both saved forms are neutral C47H74N4O10 with 61 atoms, 64 bonds and one
    fragment. Their four saved rings include two fused six-membered carbon rings,
    a five-membered nitrogen ring bearing a guanidino group, and a separate five-membered
    carbonyl-containing nitrogen ring. The source has two carbonyls and one strict
    amide; the InChI-derived form has one carbonyl, no strict amide and one terminal
    C(OH)=N site in the latter ring. No ester or saturated C5O candidate ring is detected.
    These are explicit representation differences, not a full-graph equivalence proof.
    All fourteen potential tetrahedral centres remain unspecified in both forms. The
    source saved bond enums show five STEREOE double bonds; the InChI-derived graph
    shows four STEREOE and one STEREOZ at the exocyclic enol linkage, alongside the
    changed lactam/imidic representation and substituent priorities. This descriptor
    difference is retained without inferring experimental isomerization or a verified
    atom map. Both forms also have one unspecified guanidino C=N potential-stereo
    entry. The source stereo_complete false remains appropriate. Two shared original-run
    warnings remain globally unassigned.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  evidence_ids:
  - support-2758-molecular-DATA
  - support-2758-molecular-reading
  - support-2758-diagnostic-acceptance
  - support-2758-diagnostic-execution
  - support-2758-stereo-policy
  - support-2758-identity
  dimensions:
  - name: stereochemistry_scope
    definition: Stored specifications are distinct from experimental assignment.
    value: All fourteen potential tetrahedral centres remain unspecified in both forms.
      The source saved bond enums show five STEREOE double bonds; the InChI-derived
      graph shows four STEREOE and one STEREOZ at the exocyclic enol linkage, alongside
      the changed lactam/imidic representation and substituent priorities. This descriptor
      difference is retained without inferring experimental isomerization or a verified
      atom map. Both forms also have one unspecified guanidino C=N potential-stereo
      entry. The source stereo_complete false remains appropriate.
    evidence_ids:
    - support-2758-molecular-DATA
    - support-2758-molecular-reading
    - support-2758-diagnostic-acceptance
    - support-2758-diagnostic-execution
    - support-2758-stereo-policy
    - support-2758-identity
  - name: representation_correspondence
    definition: Normalized equality does not establish explicit graph or natural identity.
    value: Both canonical flags are false and the limited correspondence is empty/incomplete,
      with full_graph_identity_established false despite normalized StandardInChI/key/formula
      equality. The five specified bond descriptors do not repair fourteen unresolved
      atom centres.
    evidence_ids:
    - support-2758-molecular-DATA
    - support-2758-molecular-reading
    - support-2758-diagnostic-acceptance
    - support-2758-diagnostic-execution
    - support-2758-stereo-policy
    - support-2758-identity
- assessment_id: support-2758-provenance-assessment
  area: provenance
  topic: Separate producer and locus source grades
  summary: BGC0001477 version 5 supplies Streptomyces sp. ID38640 NCBITaxon:1265399
    and MG459168.1 with blank coordinates and method. SOURCE_ASSERTION and CLUSTER_UNSTATED
    remain the supported grades. The row's active/questionable/complete status describes
    the source entry, not a demonstrated producer or a complete stereochemical assignment.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  evidence_ids:
  - support-2758-producer-locus
  - support-2758-taxonomy
  - support-2758-grade-policy
  - support-2758-source-reading
  - support-2758-source-plan
  - support-2758-source-plan-acceptance
  - support-2758-notes
  - support-2758-curation
  - support-2758-query-mibig_compounds
  - support-2758-query-chebi_structures
  - support-2758-query-lotus_occurrences
  - support-2758-query-cyanometdb_occurrences
  - support-2758-query-npclassifier
  - support-2758-query-pubchem_bioassay
  - support-2758-query-bindingdb_targets
  - support-2758-query-antibioticmech_inchikeys
  - support-2758-query-chebi_origins
  - support-2758-table-mibig_compounds
  - support-2758-table-lotus_occurrences
  - support-2758-table-npclassifier
  - support-2758-table-pubchem_bioassay
  dimensions:
  - name: taxon_scope
    definition: Exact retained labels and IDs without new lineage or strain resolution.
    value: The exact producer route is Streptomyces sp. ID38640 NCBITaxon:1265399.
      LOTUS Streptomyces NCBITaxon:1883 and Streptomyces lydicus NCBITaxon:47763 remain
      separate occurrence routes; cached labels cannot merge them or transfer strain
      evidence.
    evidence_ids:
    - support-2758-producer-locus
    - support-2758-taxonomy
    - support-2758-grade-policy
    - support-2758-source-reading
    - support-2758-source-plan
    - support-2758-source-plan-acceptance
    - support-2758-notes
    - support-2758-curation
    - support-2758-query-mibig_compounds
    - support-2758-query-chebi_structures
    - support-2758-query-lotus_occurrences
    - support-2758-query-cyanometdb_occurrences
    - support-2758-query-npclassifier
    - support-2758-query-pubchem_bioassay
    - support-2758-query-bindingdb_targets
    - support-2758-query-antibioticmech_inchikeys
    - support-2758-query-chebi_origins
    - support-2758-table-mibig_compounds
    - support-2758-table-lotus_occurrences
    - support-2758-table-npclassifier
    - support-2758-table-pubchem_bioassay
  - name: producer_evidence
    definition: Organism grade follows its own source methods.
    value: SOURCE_ASSERTION for the source ID38640 label; no grade transfer from genus-
      or species-labelled occurrences.
    evidence_ids:
    - support-2758-producer-locus
    - support-2758-taxonomy
    - support-2758-grade-policy
    - support-2758-source-reading
    - support-2758-source-plan
    - support-2758-source-plan-acceptance
    - support-2758-notes
    - support-2758-curation
    - support-2758-query-mibig_compounds
    - support-2758-query-chebi_structures
    - support-2758-query-lotus_occurrences
    - support-2758-query-cyanometdb_occurrences
    - support-2758-query-npclassifier
    - support-2758-query-pubchem_bioassay
    - support-2758-query-bindingdb_targets
    - support-2758-query-antibioticmech_inchikeys
    - support-2758-query-chebi_origins
    - support-2758-table-mibig_compounds
    - support-2758-table-lotus_occurrences
    - support-2758-table-npclassifier
    - support-2758-table-pubchem_bioassay
  - name: locus_evidence
    definition: Locus claims remain separately graded.
    value: BGC0001477 / MG459168.1 without a retained method or coordinates; CLUSTER_UNSTATED.
    evidence_ids:
    - support-2758-producer-locus
    - support-2758-taxonomy
    - support-2758-grade-policy
    - support-2758-source-reading
    - support-2758-source-plan
    - support-2758-source-plan-acceptance
    - support-2758-notes
    - support-2758-curation
    - support-2758-query-mibig_compounds
    - support-2758-query-chebi_structures
    - support-2758-query-lotus_occurrences
    - support-2758-query-cyanometdb_occurrences
    - support-2758-query-npclassifier
    - support-2758-query-pubchem_bioassay
    - support-2758-query-bindingdb_targets
    - support-2758-query-antibioticmech_inchikeys
    - support-2758-query-chebi_origins
    - support-2758-table-mibig_compounds
    - support-2758-table-lotus_occurrences
    - support-2758-table-npclassifier
    - support-2758-table-pubchem_bioassay
- assessment_id: support-2758-citation-assessment
  area: evidence
  topic: Citation grain and source attribution
  summary: Both seeding-history events were read. DOI:10.1016/j.chembiol.2018.02.008
    is entry-level MIBiG provenance; its uppercase LOTUS rendering is a citation-case
    duplicate, not a second independent publication. DOI:10.3389/FMICB.2019.02077
    is a separate occurrence placement. Primary text and experiments were not newly
    verified.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  evidence_ids:
  - support-2758-history-citations
  - support-2758-identity
  - support-2758-source-reading
  - support-2758-source-plan
  - support-2758-source-plan-acceptance
  - support-2758-notes
  - support-2758-curation
  - support-2758-query-mibig_compounds
  - support-2758-query-chebi_structures
  - support-2758-query-lotus_occurrences
  - support-2758-query-cyanometdb_occurrences
  - support-2758-query-npclassifier
  - support-2758-query-pubchem_bioassay
  - support-2758-query-bindingdb_targets
  - support-2758-query-antibioticmech_inchikeys
  - support-2758-query-chebi_origins
  - support-2758-table-mibig_compounds
  - support-2758-table-lotus_occurrences
  - support-2758-table-npclassifier
  - support-2758-table-pubchem_bioassay
  dimensions:
  - name: citation_scope
    definition: Claim placements are distinct from fresh primary access and independent
      evidence.
    value: Both seeding-history events were read. DOI:10.1016/j.chembiol.2018.02.008
      is entry-level MIBiG provenance; its uppercase LOTUS rendering is a citation-case
      duplicate, not a second independent publication. DOI:10.3389/FMICB.2019.02077
      is a separate occurrence placement. Primary text and experiments were not newly
      verified.
    evidence_ids:
    - support-2758-history-citations
    - support-2758-identity
    - support-2758-source-reading
    - support-2758-source-plan
    - support-2758-source-plan-acceptance
    - support-2758-notes
    - support-2758-curation
    - support-2758-query-mibig_compounds
    - support-2758-query-chebi_structures
    - support-2758-query-lotus_occurrences
    - support-2758-query-cyanometdb_occurrences
    - support-2758-query-npclassifier
    - support-2758-query-pubchem_bioassay
    - support-2758-query-bindingdb_targets
    - support-2758-query-antibioticmech_inchikeys
    - support-2758-query-chebi_origins
    - support-2758-table-mibig_compounds
    - support-2758-table-lotus_occurrences
    - support-2758-table-npclassifier
    - support-2758-table-pubchem_bioassay
- assessment_id: support-2758-occurrence-assessment
  area: evidence
  topic: Occurrence, assays and target boundaries
  summary: The two LOTUS rows concern Streptomyces NCBITaxon:1883 and Streptomyces
    lydicus NCBITaxon:47763, with their separate DOI placements. Neither establishes
    the exact ID38640 producer or its locus association. The PubChem CID:90469739
    row is a blank-AID sentinel with no assay measurement or target. ChemSpider:4943765
    is an identifier cross-reference, not assay evidence. Empty BindingDB and other
    frames remain local bounded negatives.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  evidence_ids:
  - support-2758-occurrence
  - support-2758-taxonomy
  - support-2758-capture
  - support-2758-source-reading
  - support-2758-source-plan
  - support-2758-source-plan-acceptance
  - support-2758-notes
  - support-2758-curation
  - support-2758-query-mibig_compounds
  - support-2758-query-chebi_structures
  - support-2758-query-lotus_occurrences
  - support-2758-query-cyanometdb_occurrences
  - support-2758-query-npclassifier
  - support-2758-query-pubchem_bioassay
  - support-2758-query-bindingdb_targets
  - support-2758-query-antibioticmech_inchikeys
  - support-2758-query-chebi_origins
  - support-2758-table-mibig_compounds
  - support-2758-table-lotus_occurrences
  - support-2758-table-npclassifier
  - support-2758-table-pubchem_bioassay
  dimensions:
  - name: occurrence_scope
    definition: Occurrence does not automatically demonstrate production.
    value: Two distinct LOTUS organism/reference placements; citation case duplication
      is preserved without extra source credit.
    evidence_ids:
    - support-2758-occurrence
    - support-2758-taxonomy
    - support-2758-capture
    - support-2758-source-reading
    - support-2758-source-plan
    - support-2758-source-plan-acceptance
    - support-2758-notes
    - support-2758-curation
    - support-2758-query-mibig_compounds
    - support-2758-query-chebi_structures
    - support-2758-query-lotus_occurrences
    - support-2758-query-cyanometdb_occurrences
    - support-2758-query-npclassifier
    - support-2758-query-pubchem_bioassay
    - support-2758-query-bindingdb_targets
    - support-2758-query-antibioticmech_inchikeys
    - support-2758-query-chebi_origins
    - support-2758-table-mibig_compounds
    - support-2758-table-lotus_occurrences
    - support-2758-table-npclassifier
    - support-2758-table-pubchem_bioassay
  - name: assay_target_scope
    definition: AID rows, sentinels and coarse summaries are distinct evidence grains.
    value: Zero actual AIDs; one blank-AID sentinel. Cross-references and missing
      retained target rows do not establish activity, inactivity or mechanism.
    evidence_ids:
    - support-2758-occurrence
    - support-2758-taxonomy
    - support-2758-capture
    - support-2758-source-reading
    - support-2758-source-plan
    - support-2758-source-plan-acceptance
    - support-2758-notes
    - support-2758-curation
    - support-2758-query-mibig_compounds
    - support-2758-query-chebi_structures
    - support-2758-query-lotus_occurrences
    - support-2758-query-cyanometdb_occurrences
    - support-2758-query-npclassifier
    - support-2758-query-pubchem_bioassay
    - support-2758-query-bindingdb_targets
    - support-2758-query-antibioticmech_inchikeys
    - support-2758-query-chebi_origins
    - support-2758-table-mibig_compounds
    - support-2758-table-lotus_occurrences
    - support-2758-table-npclassifier
    - support-2758-table-pubchem_bioassay
- assessment_id: support-2758-classification-assessment
  area: consistency
  topic: Filing and classifier applicability
  summary: NPClassifier reports two pathway labels with Cyclic polyketides and 3-Decalinoyltetramic
    acids, is_glycoside false. UNCLASSIFIED is the intended multi-label filing. The
    source fused carbon-ring system and five-membered nitrogen/dicarbonyl motif are
    compatible with broad cyclic-polyketide/tetramic-acid model language. The exact
    unsaturation, unassigned centres and tautomer-sensitive carbonyl/amide counts
    limit residue, positional and biosynthetic claims; no independent model validation
    is claimed.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  evidence_ids:
  - support-2758-classification
  - support-2758-filing-policy
  - support-2758-molecular-DATA
  - support-2758-queue
  - support-2758-source-reading
  - support-2758-source-plan
  - support-2758-source-plan-acceptance
  - support-2758-notes
  - support-2758-curation
  - support-2758-query-mibig_compounds
  - support-2758-query-chebi_structures
  - support-2758-query-lotus_occurrences
  - support-2758-query-cyanometdb_occurrences
  - support-2758-query-npclassifier
  - support-2758-query-pubchem_bioassay
  - support-2758-query-bindingdb_targets
  - support-2758-query-antibioticmech_inchikeys
  - support-2758-query-chebi_origins
  - support-2758-table-mibig_compounds
  - support-2758-table-lotus_occurrences
  - support-2758-table-npclassifier
  - support-2758-table-pubchem_bioassay
  dimensions:
  - name: classification_applicability
    definition: Structural compatibility qualifies rather than independently validates
      model output.
    value: The source fused carbon-ring system and five-membered nitrogen/dicarbonyl
      motif are compatible with broad cyclic-polyketide/tetramic-acid model language.
      The exact unsaturation, unassigned centres and tautomer-sensitive carbonyl/amide
      counts limit residue, positional and biosynthetic claims; no independent model
      validation is claimed.
    evidence_ids:
    - support-2758-classification
    - support-2758-filing-policy
    - support-2758-molecular-DATA
    - support-2758-queue
    - support-2758-source-reading
    - support-2758-source-plan
    - support-2758-source-plan-acceptance
    - support-2758-notes
    - support-2758-curation
    - support-2758-query-mibig_compounds
    - support-2758-query-chebi_structures
    - support-2758-query-lotus_occurrences
    - support-2758-query-cyanometdb_occurrences
    - support-2758-query-npclassifier
    - support-2758-query-pubchem_bioassay
    - support-2758-query-bindingdb_targets
    - support-2758-query-antibioticmech_inchikeys
    - support-2758-query-chebi_origins
    - support-2758-table-mibig_compounds
    - support-2758-table-lotus_occurrences
    - support-2758-table-npclassifier
    - support-2758-table-pubchem_bioassay
- assessment_id: support-2758-completion-assessment
  area: completeness
  topic: Scope and unavailable required checks
  summary: Whole current owner/history and complete assigned saved source/molecular
    tables were personally read and joined to original canonical intakes. No graph,
    pathway, target or component root requires a maintained reader. Five local native
    commands passed; full QC, OAK consistency and external primary/authority verification
    remain unavailable, so completion is partial. No actionable defect was established
    within the retained scope; incomplete or representation-dependent chemistry remains
    explicit.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-a0453972fa
  evidence_ids:
  - support-2758-owner
  - support-2758-capture
  - support-2758-intake
  - support-2758-intake-original
  - support-2758-intake-acceptance
  - support-2758-source-reading
  - support-2758-molecular-reading
  - support-2758-local-gates
  - support-2758-queue
  dimensions:
  - name: review_completion
    definition: Complete assigned reading does not mean all required checks are complete.
    value: partial; scientific_review true; full QC/OAK/external authority unavailable
    evidence_ids:
    - support-2758-owner
    - support-2758-capture
    - support-2758-intake
    - support-2758-intake-original
    - support-2758-intake-acceptance
    - support-2758-source-reading
    - support-2758-molecular-reading
    - support-2758-local-gates
    - support-2758-queue
findings: []
actions: []
limitations:
- Primary publications, spectra, sequences, live taxonomy and natural-product identity
  were not independently verified; full QC/OAK/external checks remain unavailable.
- Both canonical flags are false and the limited correspondence is empty/incomplete,
  with full_graph_identity_established false despite normalized StandardInChI/key/formula
  equality. The five specified bond descriptors do not repair fourteen unresolved
  atom centres. All fourteen potential tetrahedral centres remain unspecified in both
  forms. The source saved bond enums show five STEREOE double bonds; the InChI-derived
  graph shows four STEREOE and one STEREOZ at the exocyclic enol linkage, alongside
  the changed lactam/imidic representation and substituent priorities. This descriptor
  difference is retained without inferring experimental isomerization or a verified
  atom map. Both forms also have one unspecified guanidino C=N potential-stereo entry.
  The source stereo_complete false remains appropriate. The two diagnostic warnings
  remain globally unassigned.
- Exact-key/ID negatives and cached taxonomy are bounded by captured files and predicates,
  not universal absence, inactivity or a producer-grade upgrade.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh current batch 276 judgments use earned owner/source/intake/diagnostic evidence;
  prior batches supplied interface logic only.
- No source record or native curation status was changed. Proposed action remains
  unperformed.
- Five actual native checks and three required unavailable checks are appended by
  the ROOT assembler; no reader check is assigned to this owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-276
```
