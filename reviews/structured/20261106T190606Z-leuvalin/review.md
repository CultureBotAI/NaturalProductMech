# Local evidence review: leuvalin

- Review: 20261106T190606Z-leuvalin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T17:58:50.138760Z
- Finished UTC: 2026-11-06T19:06:06.876873Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Leuvalin needs a bounded synonym-source attribution correction: aureusimine C is tagged with BGC0002287 although the retained naming row is BGC0000308. Distinct producer/locus grades and both OPEN identity discussions remain preserved. The saved pyrazinone representations agree only within the limited diagnostic comparison.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2749; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:167321 | data/natural_products/unclassified/leuvalin.yaml | generated | leuvalin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | CHEBI:167321 | Both stored forms parsed in the original accepted diagnostic and regenerate their declared normalized identifiers and formula. |
| strict_ten | passed | True | CHEBI:167321 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:167321 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:167321 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:167321 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:167321 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:167321 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:167321 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:167321 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact source identity and grounding boundaries

identity: supported. Targets: CHEBI:167321.

CHEBI:167321 is the retained three-star leuvalin grounding, with full key WLZSJRZITZLEPW-UHFFFAOYSA-N and pubchem:121434429. MIBiG BGC0000308 v5 compound-3 names aureusimine C, while BGC0002287 v2 compound-2 names leuvalin at the same key and stored strings. The captured source_concepts keep those mappings distinct. Both name-disagreement and shared-structure discussions remain OPEN: normalized equality does not establish that the upstream biological entities are interchangeable, nor justify a merger or split.

### Stored molecular representations and stereochemistry

representation: supported. Targets: CHEBI:167321.

Both saved forms have 14 atoms, 14 bonds and neutral formula C11H18N2O, with a six-membered aromatic N2 ring and one carbonyl. Aromatic C–N bonds explain the strict amide match count of zero; this matcher boundary does not exclude the pyrazinone/lactam topology retained in the ChEBI definition. Both canonical comparisons and the limited 14-index map agree, but full graph identity remains false and no natural-sample identity is established. Neither saved form has a potential tetrahedral or double-bond stereo entry. This supports the limited atom-centred stereo_complete:true representation, without proving the source names or natural identity. Six stderr warnings belong to the shared original run and are not assigned to this record.

### Separate producer and locus source grades

provenance: supported. Targets: CHEBI:167321.

BGC0002287 v2 / genbank:MK144293.1:1–62987 names Streptococcus mutans / NCBITaxon:1309 with Heterologous expression and Knock-out studies, retaining BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED. BGC0000308 v5 / genbank:CP002120.1:176051–183901 separately names Staphylococcus aureus subsp. aureus str. JKD6008 /546342 with blank methods, retaining SOURCE_ASSERTION and CLUSTER_UNSTATED. Both source entries are active/questionable with unknown completeness. Their grades and experiments are not pooled.

### Citation grain and source attribution

evidence: concern. Targets: CHEBI:167321.

The entry-level MIBiG citations are PMID:31413323 for BGC0002287 and PMID:23302043 for BGC0000308. The ChEBI-origin occurrence cites PMID:20851341. Both history events are seeding events. A narrow provenance defect is present in synonyms[0]: aureusimine C points to mibig:BGC0002287 even though the retained row carrying that name is BGC0000308. The seeder collects names across source rows then stamps all synonyms with the evidence-ranked lead accession. Correct source_concepts and OPEN identity discussions do not repair this particular name-source pointer; the proposed correction concerns attribution only.

### Occurrence, assays and target boundaries

evidence: supported. Targets: CHEBI:167321.

The retained ChEBI-origin row reports Staphylococcus aureus / NCBITaxon:1280, with blank strain/component/comments. It is a broader occurrence claim, distinct from the JKD6008 producer and the Streptococcus mutans source context. The exact-key LOTUS frame is empty; no missing occurrence is inferred from that bounded negative. There is no retained exact-key PubChem AID row or blank sentinel, and BindingDB is empty. Source names, NRPS labels and a characterized cluster do not establish target-specific activity. No graph, pathway or molecular-target root is present.

### Filing and classifier applicability

consistency: supported. Targets: CHEBI:167321.

The six-membered aromatic pyrazinone supports a bounded comparison with Pyrazine and Piperazine alkaloids. It does not directly demonstrate a five-membered tetramate scaffold, so Tetramate alkaloids remains an unvalidated model superclass rather than a structural conclusion or automatic record error. Alkaloids and Amino acids and Peptides intentionally route to UNCLASSIFIED. Source NRPS classification does not close the two upstream identity discussions.

### Scope and unavailable required checks

completeness: supported. Targets: CHEBI:167321.

Whole current owner/history and assigned saved source/molecular payloads were personally read; input hashes and ownership were independently joined to accepted original intakes. No mechanism/pathway/target roots occur in this owner, so no maintained-reader invocation is assigned. Five local native commands passed. Full QC, OAK ontology consistency and external primary/authority verification remain unavailable under the no-request hold, so completion is partial. The minor synonym provenance finding requires a maintained-source correction; OPEN naming/shared-structure questions remain unresolved.

## Findings

### support-2749-synonym-origin-mismatch: Aureusimine C synonym points to the wrong retained naming row

minor / open / confirmed; issue key: leuvalin-aureusimine-c-synonym-source-attribution.

The current /synonyms/0 value aureusimine C cites mibig:BGC0002287. The complete retained MIBiG row417 (BGC0000308 v5, compound3) carries that name; row2766 (BGC0002287 v2, compound2) carries leuvalin. SourceConcept mappings are correct. Seeder605–624 separates naming from lead selection,953–957 aggregates names, and1006–1009 stamps every synonym with the evidence-ranked lead accession. This is a confirmed local per-name provenance mismatch, not schema invalidity, proof of a wrong upstream structure, or resolution of either OPEN identity discussion.

## Recommended Actions And Acceptance Checks

### support-2749-preserve-synonym-origin

Preserve the originating source accession alongside each collected name in the maintained seeder and emit aureusimine C with its retained BGC0000308 naming provenance. Retain both OPEN identity discussions and all separate producer/locus grades; do not infer a merger or split.

- A focused multi-source naming regression must retain a discarded alias with its originating accession when another row wins lead selection.
- Leuvalin retains CHEBI:167321, full key WLZSJRZITZLEPW-UHFFFAOYSA-N, both correct SourceConcept mappings, separate producer/locus grades and both OPEN identity discussions.
- Regenerate through the maintained workflow and run the required local validation/reproduction checks; source and record changes require their own review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2749-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/leuvalin.yaml; Complete current raw owner and all 2 history events | supports | Whole owner content and history personally read; exact current bytes match the accepted capture. |
| support-2749-capture | /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json; /records/8 | supports | Complete captured owner, mechanism-root presence and source claims; capture is distinct from a maintained-reader result. |
| support-2749-identity | /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json; /records/8/owner_document/identifier; /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts; /records/8/owner_document/xrefs; /records/8/owner_document/grounding_status; /records/8/owner_document/definition; /records/8/owner_document/synonyms; /records/8/owner_document/discussions | supports | Exact current identifier, source names and full structure key; source grounding is not natural-sample verification. |
| support-2749-producer-locus | /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json; /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters | supports | Separate source producer and locus claims with exact taxon, accession, methods and evidence grades. |
| support-2749-history-citations | /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json; /records/8/owner_document/curation_history; /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters | supports | Complete history and claim-level citation placements; no fresh primary paper or sequence verification. |
| support-2749-occurrence | /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json; /records/8/owner_document/occurrences; /records/8/owner_document/occurrence_taxon_groups | supports | Retained occurrence claims are separate from producers and experiments. |
| support-2749-classification | /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json; /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification; /records/8/owner_document/bgc_class; /records/8/owner_document/biosynthesis_origin | supports | Full model output, source BGC class and current UNCLASSIFIED filing remain separate. |
| support-2749-intake | /private/tmp/npm-review-work/shared-next-batch275/intakes-001/2749-inspect-001.json; /status; /source; /targets | supports | Actual canonical intake captures the current owner and each declared input; inspection alone is not science completion. |
| support-2749-intake-original | /private/tmp/npm-review-work/shared-next-batch275/intakes-001/intake-summary-001.json; /receipts/8 | supports | Original intake command, current input outcome and empty stderr, preserved without replay. |
| support-2749-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch275/root-current275-intake-acceptance-001.json; /accepted; /summary; /source_placements; /unique_source_paths; /first_nine_originals_unchanged; /aggregate_uses_actual_receipts | supports | Accepted ten actual intakes, preserving the first nine and the single corrected2750 completion. |
| support-2749-source-plan | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-current275-target-input-plan-corrected-002.json; /records/8 | supports | Current owner-specific source, companion and implementation inputs; companion claims do not transfer. |
| support-2749-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch275/root-current275-input-plan-acceptance-002.json; /accepted; /source_plan; /first_nine_full_records_and_inputs_preserved; /original_scoped_rows; /separate_supplemental_scoped_rows; /supplemental_scientific_review_order | supports | Corrected input authority retains the original158 source rows; separate PathwayMech supplement scientific scope belongs only to2750. |
| support-2749-source-reading | /private/tmp/npm-review-work/shared-next-batch275-tentative/support-prep/support-current275-assigned-source-reading-002.json; /contexts/7; /selected_counts; /primary_context_indices | supports | Personally read the complete selected source dictionaries, physical spans and exact negative frames; companion credit is separately attributed. |
| support-2749-notes | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-current275-source-scope-notes-002.json; /reading; /reading_reconciliation; /reading_boundaries; /cautions | supports | Disjoint original source-reading attribution and current Native cache/curation meanings; no additional primary credit. |
| support-2749-taxonomy | /private/tmp/npm-review-work/shared-next-batch275-tentative/native-prep/native-current275-cached-taxonomy-reading-001.json; /context_interpretations/12; /interpretation | supports | Cached exact taxon ID/label context only; no fresh lineage, rank or strain verification. |
| support-2749-curation | /private/tmp/npm-review-work/shared-next-batch275-tentative/native-prep/native-current275-implemented-curation-scan-001.json; /counts; /exact_applicability_resolution; /implementation_scope; /interpretation | supports | No exact applicable decision in nine retained substantive tables; lexical candidates do not establish applicability. |
| support-2749-molecular-DATA | /private/tmp/npm-review-work/shared-next-batch275/chemistry-local/diagnostic-DATA-001.json; /records/8 | supports | Complete saved two-form atom/bond/ring/stereo/motif tables, comparison flags and map limits; no new molecular parse. |
| support-2749-molecular-reading | /private/tmp/npm-review-work/shared-next-batch275-tentative/support-prep/support-current275-last-five-molecular-reading-001.json; /records/3; /counts; /warning_stream; /limits | supports | Personal complete saved-table reading with representation-aware interpretation and no natural-identity claim. |
| support-2749-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch275/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /false_comparisons_preserved; /unassigned_undefined_stereo_warning_lines | supports | Accepted original20-form computation; six stderr warnings remain global and unassigned. |
| support-2749-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch275/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr; /retries; /external_requests | supports | Actual original diagnostic command and streams, exit0/no retry/request. |
| support-2749-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165–172 | supports | stereo_complete is computed from atom-centred chiral centres; it does not assert every bond geometry or experimental assignment. |
| support-2749-grade-policy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; lines 18–40 | supports | Producer and locus grades use distinct supports; blank methods and heterologous versus knockout evidence are not interchangeable. |
| support-2749-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295–306 | supports | Zero or multiple pathway labels intentionally file UNCLASSIFIED; no arbitrary model label is chosen. |
| support-2749-local-gates | /private/tmp/npm-native-checks/batch-275/root-five-gates-acceptance-001.json; /accepted; /execution; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates | supports | Five local native commands passed; full QC/OAK completion remains unavailable. |
| support-2749-queue | /private/tmp/npm-native-checks/batch-275/root-selected-queue-snapshot-001.json; /selected_rows/8; /selected_rows/9; /selected_rows/10; /selected_rows/16 | supports | Current selected diagnostic queue items are review prompts, not established scientific defects. |
| support-2749-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/mibig_compounds | supports | Complete retained mibig_compounds frame: 2 positive placements with its exact predicate and full fields. |
| support-2749-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 417, 2766; full header and dictionaries in inventory /contexts/12/source_scope_inventory/joins/mibig_compounds/matches | supports | All physical row fields and blanks personally read; row placements are not independent experiments. |
| support-2749-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/chebi_structures | supports | Complete retained chebi_structures frame: 1 positive placements with its exact predicate and full fields. |
| support-2749-table-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Physical TSV lines 43369; full header and dictionaries in inventory /contexts/12/source_scope_inventory/joins/chebi_structures/matches | supports | All physical row fields and blanks personally read; row placements are not independent experiments. |
| support-2749-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained lotus_occurrences frame: 0 positive placements with its exact predicate and full fields. |
| support-2749-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained cyanometdb_occurrences frame: 0 positive placements with its exact predicate and full fields. |
| support-2749-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/npclassifier | supports | Complete retained npclassifier frame: 1 positive placements with its exact predicate and full fields. |
| support-2749-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 2656; full header and dictionaries in inventory /contexts/12/source_scope_inventory/joins/npclassifier/matches | supports | All physical row fields and blanks personally read; row placements are not independent experiments. |
| support-2749-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained pubchem_bioassay frame: 0 positive placements with its exact predicate and full fields. |
| support-2749-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained bindingdb_targets frame: 0 positive placements with its exact predicate and full fields. |
| support-2749-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained antibioticmech_inchikeys frame: 0 positive placements with its exact predicate and full fields. |
| support-2749-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/chebi_origins | supports | Complete retained chebi_origins frame: 1 positive placements with its exact predicate and full fields. |
| support-2749-table-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Physical TSV lines 17179; full header and dictionaries in inventory /contexts/12/source_scope_inventory/joins/chebi_origins/matches | supports | All physical row fields and blanks personally read; row placements are not independent experiments. |
| support-2749-taxon-predicates | /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/source_taxa; /contexts/12/source_scope_inventory/forward_taxon_merge_matches; /contexts/12/source_scope_inventory/nonorganism_matches | supports | Exact source-taxonomy forward merge and nonorganism frames; no reverse or live inference. |
| support-2749-synonym-provenance | /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json; /records/8/owner_document/synonyms/0; /records/8/owner_document/source_concepts; /records/8/owner_document/discussions | supports | The synonym source pointer differs from the exact row carrying the name; correct SourceConcept maps and OPEN identity discussions are preserved. |
| support-2749-synonym-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 605–624; 948–960; 1000–1009; 1031–1038 | supports | Naming is collected separately from producer-ranked lead selection, but all synonym sources receive the lead accession. |
| support-2749-synonym-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 434–464 | supports | CompoundSynonym.source is CURIE-typed; SourceConcept retains per-record labels. The finding is per-name attribution, not schema invalidity. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-275/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-275/native-current275-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-275/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-275/native-current275-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-275/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-275/native-current275-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-275/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-275/native-current275-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-275/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-275/native-current275-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Primary publications, live authorities, spectra, sequences, strain identities and complete natural-product identity were not independently verified; full QC/OAK/external checks remain unavailable.
- Canonical comparisons true; limited map14; aromatic amide matcher0; full identity false. Neither saved form has a potential tetrahedral or double-bond stereo entry. This supports the limited atom-centred stereo_complete:true representation, without proving the source names or natural identity. The shared diagnostic has six globally unassigned warnings.
- Retained exact-key/ID negatives are bounded by captured files and predicates, not universal absence or inactivity. Cached taxonomy and separate source grades are not upgraded.
- Both upstream identity discussions remain OPEN. The minor finding addresses a synonym source pointer only.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Current scientific judgments were authored from earned275 owner/source/intake/molecular evidence; prior batch artifacts supplied interface logic only.
- No source record or native curation status was changed. Proposed actions are unperformed.
- The PathwayMech correction applies only to2750; no supplemental positive or negative row credit is claimed for this owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T190606Z-leuvalin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: leuvalin'
started_at: '2026-11-06T17:58:50.138760Z'
finished_at: '2026-11-06T19:06:06.876873Z'
reviewer:
  identity: Codex root with native_checks, bgc_science and review_support peer agents
  kind: agent
  independence: independent
  independence_basis: This review team inspected existing owner and retained source
    bytes without editing them; scientific fragments were cross-checked separately
    from their author. Local validation is not treated as scientific proof.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Leuvalin needs a bounded synonym-source attribution correction: aureusimine
  C is tagged with BGC0002287 although the retained naming row is BGC0000308. Distinct
  producer/locus grades and both OPEN identity discussions remain preserved. The saved
  pyrazinone representations agree only within the limited diagnostic comparison.'
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
  - path: data/natural_products/unclassified/leuvalin.yaml
    sha256: 2ec49d8eae81fa63b5a093c18946529b367d054734c0f36711da27498af8196a
    role: target
  - path: data/natural_products/unclassified/mutanocyclin.yaml
    sha256: 68edcbaaf883fffbcba533420d42a3bbf8efd87350e6a1925046536bf751ee16
    role: context
  - path: data/natural_products/unclassified/phevalin.yaml
    sha256: 5f5e7ad28572dddca46301e4e97805a2257d86c62fac628eed359be4fccbf79f
    role: context
  - path: data/natural_products/unclassified/tyrvalin.yaml
    sha256: 3c409b3170f2d2aba0d52ffe40f2f128f85b179940db3445e738928e7db3ea7d
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
  selection: Campaign path order 2749; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:167321
targets:
- target_id: CHEBI:167321
  path: data/natural_products/unclassified/leuvalin.yaml
  label: leuvalin
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
    path: data/raw/chebi_origins.tsv
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch275/chemistry-local/diagnose275-001.py
    6a4b8bbb91d843e09dfae3f2952cb1b9a54ee99915dece9d71b404fd24def256 0f4b115434ae166215d8aeb3499ac0b23f78a4e4a08065f490b733d21867145a
    f9aafd24deee2407afc48c8ced300272a579856d381defe0941ee808ea378e4b
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed in the original accepted diagnostic and regenerate
    their declared normalized identifiers and formula.
  scope_note: Canonical comparisons true; limited map14; aromatic amide matcher0;
    full identity false. Neither saved form has a potential tetrahedral or double-bond
    stereo entry. This supports the limited atom-centred stereo_complete:true representation,
    without proving the source names or natural identity. Six shared warnings remain
    unassigned; no new parse or natural-identity proof.
  target_ids:
  - CHEBI:167321
  evidence_ids:
  - support-2749-molecular-DATA
  - support-2749-diagnostic-execution
  - support-2749-diagnostic-acceptance
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:167321
  command: just validate-strict data/natural_products/unclassified/lactocin-s.yaml
    data/natural_products/unclassified/lactonamycin-z.yaml data/natural_products/unclassified/lactonamycin.yaml
    data/natural_products/unclassified/largimycin-a1.yaml data/natural_products/unclassified/largimycin-a2.yaml
    data/natural_products/unclassified/largimycin-a3.yaml data/natural_products/unclassified/laterocidine.yaml
    data/natural_products/unclassified/legonoxamine-b.yaml data/natural_products/unclassified/leuvalin.yaml
    data/natural_products/unclassified/linearmycin-c.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-275/validate-strict-selected10-001.tsv
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
  - CHEBI:167321
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-275/validate-all-001.tsv
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
  - CHEBI:167321
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
  - CHEBI:167321
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
  - CHEBI:167321
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-275/review-queue-001.tsv
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
  - CHEBI:167321
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:167321
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:167321
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2749-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/leuvalin.yaml
  locator: Complete current raw owner and all 2 history events
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Whole owner content and history personally read; exact current bytes match
    the accepted capture.
  snapshot_sha256: 2ec49d8eae81fa63b5a093c18946529b367d054734c0f36711da27498af8196a
- evidence_id: support-2749-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json
  locator: /records/8
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Complete captured owner, mechanism-root presence and source claims; capture
    is distinct from a maintained-reader result.
  snapshot_sha256: 0f4b115434ae166215d8aeb3499ac0b23f78a4e4a08065f490b733d21867145a
- evidence_id: support-2749-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json
  locator: /records/8/owner_document/identifier; /records/8/owner_document/chemical_structure;
    /records/8/owner_document/source_concepts; /records/8/owner_document/xrefs; /records/8/owner_document/grounding_status;
    /records/8/owner_document/definition; /records/8/owner_document/synonyms; /records/8/owner_document/discussions
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Exact current identifier, source names and full structure key; source grounding
    is not natural-sample verification.
  snapshot_sha256: 0f4b115434ae166215d8aeb3499ac0b23f78a4e4a08065f490b733d21867145a
- evidence_id: support-2749-producer-locus
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json
  locator: /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Separate source producer and locus claims with exact taxon, accession,
    methods and evidence grades.
  snapshot_sha256: 0f4b115434ae166215d8aeb3499ac0b23f78a4e4a08065f490b733d21867145a
- evidence_id: support-2749-history-citations
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json
  locator: /records/8/owner_document/curation_history; /records/8/owner_document/producer_organisms;
    /records/8/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Complete history and claim-level citation placements; no fresh primary
    paper or sequence verification.
  snapshot_sha256: 0f4b115434ae166215d8aeb3499ac0b23f78a4e4a08065f490b733d21867145a
- evidence_id: support-2749-occurrence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json
  locator: /records/8/owner_document/occurrences; /records/8/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Retained occurrence claims are separate from producers and experiments.
  snapshot_sha256: 0f4b115434ae166215d8aeb3499ac0b23f78a4e4a08065f490b733d21867145a
- evidence_id: support-2749-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json
  locator: /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification;
    /records/8/owner_document/bgc_class; /records/8/owner_document/biosynthesis_origin
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Full model output, source BGC class and current UNCLASSIFIED filing remain
    separate.
  snapshot_sha256: 0f4b115434ae166215d8aeb3499ac0b23f78a4e4a08065f490b733d21867145a
- evidence_id: support-2749-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch275/intakes-001/2749-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Actual canonical intake captures the current owner and each declared input;
    inspection alone is not science completion.
  snapshot_sha256: fbcf2807d1d10fb040f6535ea45cad1416f1fc61dfde3f979c8edb569259a744
- evidence_id: support-2749-intake-original
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch275/intakes-001/intake-summary-001.json
  locator: /receipts/8
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Original intake command, current input outcome and empty stderr, preserved
    without replay.
  snapshot_sha256: f9aafd24deee2407afc48c8ced300272a579856d381defe0941ee808ea378e4b
- evidence_id: support-2749-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch275/root-current275-intake-acceptance-001.json
  locator: /accepted; /summary; /source_placements; /unique_source_paths; /first_nine_originals_unchanged;
    /aggregate_uses_actual_receipts
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Accepted ten actual intakes, preserving the first nine and the single corrected2750
    completion.
  snapshot_sha256: d8d67e4eea28cf4b3c1eaacb0a982a55af2c1a5ea4c0e70719299c513c26f9d5
- evidence_id: support-2749-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-current275-target-input-plan-corrected-002.json
  locator: /records/8
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Current owner-specific source, companion and implementation inputs; companion
    claims do not transfer.
  snapshot_sha256: 7c5d926d78121f75bcd4a35d9cf4a6a388a203beb8e0e44fce9b9c6f2f43f5df
- evidence_id: support-2749-source-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch275/root-current275-input-plan-acceptance-002.json
  locator: /accepted; /source_plan; /first_nine_full_records_and_inputs_preserved;
    /original_scoped_rows; /separate_supplemental_scoped_rows; /supplemental_scientific_review_order
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Corrected input authority retains the original158 source rows; separate
    PathwayMech supplement scientific scope belongs only to2750.
  snapshot_sha256: 0a0414c37e0b53637939ddaf1ee9739eb08ed0b9816eb53fb6ee3d5f2530a2fb
- evidence_id: support-2749-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/support-prep/support-current275-assigned-source-reading-002.json
  locator: /contexts/7; /selected_counts; /primary_context_indices
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Personally read the complete selected source dictionaries, physical spans
    and exact negative frames; companion credit is separately attributed.
  snapshot_sha256: e636b28dd28d91486d437d687cea166d2e8f74a258a593f2f28717d27eb97d66
- evidence_id: support-2749-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-current275-source-scope-notes-002.json
  locator: /reading; /reading_reconciliation; /reading_boundaries; /cautions
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Disjoint original source-reading attribution and current Native cache/curation
    meanings; no additional primary credit.
  snapshot_sha256: 450ce3ead89c6fd66e88de5b15c621f8cdb16092e432202ba7b6cea315e36162
- evidence_id: support-2749-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/native-prep/native-current275-cached-taxonomy-reading-001.json
  locator: /context_interpretations/12; /interpretation
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Cached exact taxon ID/label context only; no fresh lineage, rank or strain
    verification.
  snapshot_sha256: e0397f8a1873051f61ab786862e9bfedd3db1111d73988cc930ea8dce17dfb1b
- evidence_id: support-2749-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/native-prep/native-current275-implemented-curation-scan-001.json
  locator: /counts; /exact_applicability_resolution; /implementation_scope; /interpretation
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: No exact applicable decision in nine retained substantive tables; lexical
    candidates do not establish applicability.
  snapshot_sha256: aed9d93a5a3251d46b51267022e406b36ae64893e0674fb6f2d16745eaf01b5f
  search_scope: Ignored-inclusive eleven-table census, nine substantive correction/diagnostic
    tables and six exact identity predicates; decisions/source_queue extras are census-only,
    not correction evidence.
- evidence_id: support-2749-molecular-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch275/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Complete saved two-form atom/bond/ring/stereo/motif tables, comparison
    flags and map limits; no new molecular parse.
  snapshot_sha256: 2d47f8d0051bdb12c66a5c908b1eb6f23b9d8a26458b25571049861873a3cd85
- evidence_id: support-2749-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/support-prep/support-current275-last-five-molecular-reading-001.json
  locator: /records/3; /counts; /warning_stream; /limits
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Personal complete saved-table reading with representation-aware interpretation
    and no natural-identity claim.
  snapshot_sha256: 84d987c6c8ed78d9240658ac645e0e4b189718adad33d470fb7eeeb4ab2a8022
- evidence_id: support-2749-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch275/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /false_comparisons_preserved; /unassigned_undefined_stereo_warning_lines
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Accepted original20-form computation; six stderr warnings remain global
    and unassigned.
  snapshot_sha256: 5aa01b6cc7986ab68feacb505786b28a6f310a94b1c02b34865e57d9481c9046
- evidence_id: support-2749-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch275/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Actual original diagnostic command and streams, exit0/no retry/request.
  snapshot_sha256: efe3e8658269311c676eb6ad5983837836601e9d1680924ef0bb0690316af2a2
- evidence_id: support-2749-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 165–172
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: stereo_complete is computed from atom-centred chiral centres; it does not
    assert every bond geometry or experimental assignment.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2749-grade-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: lines 18–40
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Producer and locus grades use distinct supports; blank methods and heterologous
    versus knockout evidence are not interchangeable.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2749-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295–306
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Zero or multiple pathway labels intentionally file UNCLASSIFIED; no arbitrary
    model label is chosen.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2749-local-gates
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-275/root-five-gates-acceptance-001.json
  locator: /accepted; /execution; /five_local_commands_passed; /all_native_gates_passed;
    /unavailable_required_gates
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Five local native commands passed; full QC/OAK completion remains unavailable.
  snapshot_sha256: 40bf962b3e462b1c77b3e19245059444adbc56414036bb09e50a577699478224
- evidence_id: support-2749-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-275/root-selected-queue-snapshot-001.json
  locator: /selected_rows/8; /selected_rows/9; /selected_rows/10; /selected_rows/16
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Current selected diagnostic queue items are review prompts, not established
    scientific defects.
  snapshot_sha256: 542a31adc9e0288ad288f82fd4272b599cb536ffa7bffaa95acafef94d7c4dd6
- evidence_id: support-2749-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: 'Complete retained mibig_compounds frame: 2 positive placements with its
    exact predicate and full fields.'
  snapshot_sha256: 92dec1b37f9b659355112b143b8a681a8a9881fd7500633cfe333eade3b6dee9
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "WLZSJRZITZLEPW-UHFFFAOYSA-N", "scope": "Pinned retained table only; no replay,
    universal absence or biological inactivity inference.", "table": "mibig_compounds"}'
- evidence_id: support-2749-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 417, 2766; full header and dictionaries in inventory
    /contexts/12/source_scope_inventory/joins/mibig_compounds/matches
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: All physical row fields and blanks personally read; row placements are
    not independent experiments.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2749-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: 'Complete retained chebi_structures frame: 1 positive placements with its
    exact predicate and full fields.'
  snapshot_sha256: 92dec1b37f9b659355112b143b8a681a8a9881fd7500633cfe333eade3b6dee9
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "WLZSJRZITZLEPW-UHFFFAOYSA-N", "scope": "Pinned retained table only; no replay,
    universal absence or biological inactivity inference.", "table": "chebi_structures"}'
- evidence_id: support-2749-table-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Physical TSV lines 43369; full header and dictionaries in inventory /contexts/12/source_scope_inventory/joins/chebi_structures/matches
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: All physical row fields and blanks personally read; row placements are
    not independent experiments.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: support-2749-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: 'Complete retained lotus_occurrences frame: 0 positive placements with
    its exact predicate and full fields.'
  snapshot_sha256: 92dec1b37f9b659355112b143b8a681a8a9881fd7500633cfe333eade3b6dee9
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "WLZSJRZITZLEPW-UHFFFAOYSA-N", "scope": "Pinned retained table only; no replay,
    universal absence or biological inactivity inference.", "table": "lotus_occurrences"}'
- evidence_id: support-2749-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: 'Complete retained cyanometdb_occurrences frame: 0 positive placements
    with its exact predicate and full fields.'
  snapshot_sha256: 92dec1b37f9b659355112b143b8a681a8a9881fd7500633cfe333eade3b6dee9
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "WLZSJRZITZLEPW-UHFFFAOYSA-N", "scope": "Pinned retained table only; no replay,
    universal absence or biological inactivity inference.", "table": "cyanometdb_occurrences"}'
- evidence_id: support-2749-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: 'Complete retained npclassifier frame: 1 positive placements with its exact
    predicate and full fields.'
  snapshot_sha256: 92dec1b37f9b659355112b143b8a681a8a9881fd7500633cfe333eade3b6dee9
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "WLZSJRZITZLEPW-UHFFFAOYSA-N", "scope": "Pinned retained table only; no replay,
    universal absence or biological inactivity inference.", "table": "npclassifier"}'
- evidence_id: support-2749-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 2656; full header and dictionaries in inventory /contexts/12/source_scope_inventory/joins/npclassifier/matches
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: All physical row fields and blanks personally read; row placements are
    not independent experiments.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2749-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: 'Complete retained pubchem_bioassay frame: 0 positive placements with its
    exact predicate and full fields.'
  snapshot_sha256: 92dec1b37f9b659355112b143b8a681a8a9881fd7500633cfe333eade3b6dee9
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "WLZSJRZITZLEPW-UHFFFAOYSA-N", "scope": "Pinned retained table only; no replay,
    universal absence or biological inactivity inference.", "table": "pubchem_bioassay"}'
- evidence_id: support-2749-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: 'Complete retained bindingdb_targets frame: 0 positive placements with
    its exact predicate and full fields.'
  snapshot_sha256: 92dec1b37f9b659355112b143b8a681a8a9881fd7500633cfe333eade3b6dee9
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "WLZSJRZITZLEPW-UHFFFAOYSA-N", "scope": "Pinned retained table only; no replay,
    universal absence or biological inactivity inference.", "table": "bindingdb_targets"}'
- evidence_id: support-2749-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: 'Complete retained antibioticmech_inchikeys frame: 0 positive placements
    with its exact predicate and full fields.'
  snapshot_sha256: 92dec1b37f9b659355112b143b8a681a8a9881fd7500633cfe333eade3b6dee9
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "WLZSJRZITZLEPW-UHFFFAOYSA-N", "scope": "Pinned retained table only; no replay,
    universal absence or biological inactivity inference.", "table": "antibioticmech_inchikeys"}'
- evidence_id: support-2749-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: 'Complete retained chebi_origins frame: 1 positive placements with its
    exact predicate and full fields.'
  snapshot_sha256: 92dec1b37f9b659355112b143b8a681a8a9881fd7500633cfe333eade3b6dee9
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": ["CHEBI:167321"], "scope": "Pinned retained table only; no replay, universal
    absence or biological inactivity inference.", "table": "chebi_origins"}'
- evidence_id: support-2749-table-chebi_origins
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Physical TSV lines 17179; full header and dictionaries in inventory /contexts/12/source_scope_inventory/joins/chebi_origins/matches
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: All physical row fields and blanks personally read; row placements are
    not independent experiments.
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: support-2749-taxon-predicates
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch275-tentative/bgc-prep/bgc-conditional275-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/source_taxa; /contexts/12/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/12/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Exact source-taxonomy forward merge and nonorganism frames; no reverse
    or live inference.
  snapshot_sha256: 92dec1b37f9b659355112b143b8a681a8a9881fd7500633cfe333eade3b6dee9
  search_scope: Only this context literal source IDs against pinned retained tables.
- evidence_id: support-2749-synonym-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch275/owner-capture-DATA-001.json
  locator: /records/8/owner_document/synonyms/0; /records/8/owner_document/source_concepts;
    /records/8/owner_document/discussions
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: The synonym source pointer differs from the exact row carrying the name;
    correct SourceConcept maps and OPEN identity discussions are preserved.
  snapshot_sha256: 0f4b115434ae166215d8aeb3499ac0b23f78a4e4a08065f490b733d21867145a
- evidence_id: support-2749-synonym-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 605–624; 948–960; 1000–1009; 1031–1038
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: Naming is collected separately from producer-ranked lead selection, but
    all synonym sources receive the lead accession.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2749-synonym-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 434–464
  accessed_at: '2026-11-06T19:01:06.104923Z'
  support: supports
  summary: CompoundSynonym.source is CURIE-typed; SourceConcept retains per-record
    labels. The finding is per-name attribution, not schema invalidity.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-275/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-275/native-current275-five-gates-execution-001.json
  accessed_at: '2026-11-06T18:01:29.472438Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: e87dfa04362668174e7dfd9d26761c9e44dd24d00d6d3dbd232e543e2ec67664
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-275/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-275/native-current275-five-gates-execution-001.json
  accessed_at: '2026-11-06T18:01:53.428821Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 81a8b7ba673c98e3810ca452c891089a316eed59260f198e54552e5bdd39ef36
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-275/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-275/native-current275-five-gates-execution-001.json
  accessed_at: '2026-11-06T18:02:12.538085Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-275/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-275/native-current275-five-gates-execution-001.json
  accessed_at: '2026-11-06T18:02:45.736114Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-275/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-275/native-current275-five-gates-execution-001.json
  accessed_at: '2026-11-06T18:02:57.237152Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: dd54304610c38b1c53150d6e94d5a0c2bc017078a97e3985e2b42c36e4946008
assessments:
- assessment_id: support-2749-identity-assessment
  area: identity
  topic: Exact source identity and grounding boundaries
  summary: 'CHEBI:167321 is the retained three-star leuvalin grounding, with full
    key WLZSJRZITZLEPW-UHFFFAOYSA-N and pubchem:121434429. MIBiG BGC0000308 v5 compound-3
    names aureusimine C, while BGC0002287 v2 compound-2 names leuvalin at the same
    key and stored strings. The captured source_concepts keep those mappings distinct.
    Both name-disagreement and shared-structure discussions remain OPEN: normalized
    equality does not establish that the upstream biological entities are interchangeable,
    nor justify a merger or split.'
  outcome: supported
  target_ids:
  - CHEBI:167321
  evidence_ids:
  - support-2749-identity
  - support-2749-capture
  - support-2749-source-reading
  - support-2749-source-plan
  - support-2749-source-plan-acceptance
  - support-2749-notes
  - support-2749-curation
  - support-2749-query-mibig_compounds
  - support-2749-query-chebi_structures
  - support-2749-query-lotus_occurrences
  - support-2749-query-cyanometdb_occurrences
  - support-2749-query-npclassifier
  - support-2749-query-pubchem_bioassay
  - support-2749-query-bindingdb_targets
  - support-2749-query-antibioticmech_inchikeys
  - support-2749-query-chebi_origins
  - support-2749-table-mibig_compounds
  - support-2749-table-chebi_structures
  - support-2749-table-npclassifier
  - support-2749-table-chebi_origins
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete key without prefix or name substitution.
    value: WLZSJRZITZLEPW-UHFFFAOYSA-N
    evidence_ids:
    - support-2749-identity
    - support-2749-capture
    - support-2749-source-reading
    - support-2749-source-plan
    - support-2749-source-plan-acceptance
    - support-2749-notes
    - support-2749-curation
    - support-2749-query-mibig_compounds
    - support-2749-query-chebi_structures
    - support-2749-query-lotus_occurrences
    - support-2749-query-cyanometdb_occurrences
    - support-2749-query-npclassifier
    - support-2749-query-pubchem_bioassay
    - support-2749-query-bindingdb_targets
    - support-2749-query-antibioticmech_inchikeys
    - support-2749-query-chebi_origins
    - support-2749-table-mibig_compounds
    - support-2749-table-chebi_structures
    - support-2749-table-npclassifier
    - support-2749-table-chebi_origins
  - name: grounding_scope
    definition: Retained source grounding is distinct from natural identity.
    value: EXACT retained CHEBI167321 mapping; two source-identity discussions remain
      OPEN.
    evidence_ids:
    - support-2749-identity
    - support-2749-capture
    - support-2749-source-reading
    - support-2749-source-plan
    - support-2749-source-plan-acceptance
    - support-2749-notes
    - support-2749-curation
    - support-2749-query-mibig_compounds
    - support-2749-query-chebi_structures
    - support-2749-query-lotus_occurrences
    - support-2749-query-cyanometdb_occurrences
    - support-2749-query-npclassifier
    - support-2749-query-pubchem_bioassay
    - support-2749-query-bindingdb_targets
    - support-2749-query-antibioticmech_inchikeys
    - support-2749-query-chebi_origins
    - support-2749-table-mibig_compounds
    - support-2749-table-chebi_structures
    - support-2749-table-npclassifier
    - support-2749-table-chebi_origins
- assessment_id: support-2749-representation-assessment
  area: representation
  topic: Stored molecular representations and stereochemistry
  summary: Both saved forms have 14 atoms, 14 bonds and neutral formula C11H18N2O,
    with a six-membered aromatic N2 ring and one carbonyl. Aromatic C–N bonds explain
    the strict amide match count of zero; this matcher boundary does not exclude the
    pyrazinone/lactam topology retained in the ChEBI definition. Both canonical comparisons
    and the limited 14-index map agree, but full graph identity remains false and
    no natural-sample identity is established. Neither saved form has a potential
    tetrahedral or double-bond stereo entry. This supports the limited atom-centred
    stereo_complete:true representation, without proving the source names or natural
    identity. Six stderr warnings belong to the shared original run and are not assigned
    to this record.
  outcome: supported
  target_ids:
  - CHEBI:167321
  evidence_ids:
  - support-2749-molecular-DATA
  - support-2749-molecular-reading
  - support-2749-diagnostic-acceptance
  - support-2749-diagnostic-execution
  - support-2749-stereo-policy
  - support-2749-identity
  dimensions:
  - name: stereochemistry_scope
    definition: Saved stereochemical specifications are distinct from experimental
      assignment.
    value: Neither saved form has a potential tetrahedral or double-bond stereo entry.
      This supports the limited atom-centred stereo_complete:true representation,
      without proving the source names or natural identity.
    evidence_ids:
    - support-2749-molecular-DATA
    - support-2749-molecular-reading
    - support-2749-diagnostic-acceptance
    - support-2749-diagnostic-execution
    - support-2749-stereo-policy
    - support-2749-identity
  - name: representation_correspondence
    definition: Normalized equality and a limited map do not establish full identity.
    value: Canonical comparisons true; limited map14; aromatic amide matcher0; full
      identity false.
    evidence_ids:
    - support-2749-molecular-DATA
    - support-2749-molecular-reading
    - support-2749-diagnostic-acceptance
    - support-2749-diagnostic-execution
    - support-2749-stereo-policy
    - support-2749-identity
- assessment_id: support-2749-provenance-assessment
  area: provenance
  topic: Separate producer and locus source grades
  summary: BGC0002287 v2 / genbank:MK144293.1:1–62987 names Streptococcus mutans /
    NCBITaxon:1309 with Heterologous expression and Knock-out studies, retaining BGC_CHARACTERIZED
    and CLUSTER_DEMONSTRATED. BGC0000308 v5 / genbank:CP002120.1:176051–183901 separately
    names Staphylococcus aureus subsp. aureus str. JKD6008 /546342 with blank methods,
    retaining SOURCE_ASSERTION and CLUSTER_UNSTATED. Both source entries are active/questionable
    with unknown completeness. Their grades and experiments are not pooled.
  outcome: supported
  target_ids:
  - CHEBI:167321
  evidence_ids:
  - support-2749-producer-locus
  - support-2749-taxonomy
  - support-2749-grade-policy
  - support-2749-source-reading
  - support-2749-source-plan
  - support-2749-source-plan-acceptance
  - support-2749-notes
  - support-2749-curation
  - support-2749-query-mibig_compounds
  - support-2749-query-chebi_structures
  - support-2749-query-lotus_occurrences
  - support-2749-query-cyanometdb_occurrences
  - support-2749-query-npclassifier
  - support-2749-query-pubchem_bioassay
  - support-2749-query-bindingdb_targets
  - support-2749-query-antibioticmech_inchikeys
  - support-2749-query-chebi_origins
  - support-2749-table-mibig_compounds
  - support-2749-table-chebi_structures
  - support-2749-table-npclassifier
  - support-2749-table-chebi_origins
  dimensions:
  - name: taxon_scope
    definition: Exact retained ID/label routes, without new lineage or strain resolution.
    value: S. mutans /1309 and JKD6008 /546342 producer contexts remain separate from
      S. aureus /1280 occurrence.
    evidence_ids:
    - support-2749-producer-locus
    - support-2749-taxonomy
    - support-2749-grade-policy
    - support-2749-source-reading
    - support-2749-source-plan
    - support-2749-source-plan-acceptance
    - support-2749-notes
    - support-2749-curation
    - support-2749-query-mibig_compounds
    - support-2749-query-chebi_structures
    - support-2749-query-lotus_occurrences
    - support-2749-query-cyanometdb_occurrences
    - support-2749-query-npclassifier
    - support-2749-query-pubchem_bioassay
    - support-2749-query-bindingdb_targets
    - support-2749-query-antibioticmech_inchikeys
    - support-2749-query-chebi_origins
    - support-2749-table-mibig_compounds
    - support-2749-table-chebi_structures
    - support-2749-table-npclassifier
    - support-2749-table-chebi_origins
  - name: producer_evidence
    definition: Organism grade follows its own retained source methods.
    value: BGC2287 BGC_CHARACTERIZED; BGC0308 SOURCE_ASSERTION; grades not pooled.
    evidence_ids:
    - support-2749-producer-locus
    - support-2749-taxonomy
    - support-2749-grade-policy
    - support-2749-source-reading
    - support-2749-source-plan
    - support-2749-source-plan-acceptance
    - support-2749-notes
    - support-2749-curation
    - support-2749-query-mibig_compounds
    - support-2749-query-chebi_structures
    - support-2749-query-lotus_occurrences
    - support-2749-query-cyanometdb_occurrences
    - support-2749-query-npclassifier
    - support-2749-query-pubchem_bioassay
    - support-2749-query-bindingdb_targets
    - support-2749-query-antibioticmech_inchikeys
    - support-2749-query-chebi_origins
    - support-2749-table-mibig_compounds
    - support-2749-table-chebi_structures
    - support-2749-table-npclassifier
    - support-2749-table-chebi_origins
  - name: locus_evidence
    definition: Locus association remains separately graded.
    value: MK144293.1:1–62987 demonstrated; CP002120.1:176051–183901 unstated.
    evidence_ids:
    - support-2749-producer-locus
    - support-2749-taxonomy
    - support-2749-grade-policy
    - support-2749-source-reading
    - support-2749-source-plan
    - support-2749-source-plan-acceptance
    - support-2749-notes
    - support-2749-curation
    - support-2749-query-mibig_compounds
    - support-2749-query-chebi_structures
    - support-2749-query-lotus_occurrences
    - support-2749-query-cyanometdb_occurrences
    - support-2749-query-npclassifier
    - support-2749-query-pubchem_bioassay
    - support-2749-query-bindingdb_targets
    - support-2749-query-antibioticmech_inchikeys
    - support-2749-query-chebi_origins
    - support-2749-table-mibig_compounds
    - support-2749-table-chebi_structures
    - support-2749-table-npclassifier
    - support-2749-table-chebi_origins
- assessment_id: support-2749-citation-assessment
  area: evidence
  topic: Citation grain and source attribution
  summary: 'The entry-level MIBiG citations are PMID:31413323 for BGC0002287 and PMID:23302043
    for BGC0000308. The ChEBI-origin occurrence cites PMID:20851341. Both history
    events are seeding events. A narrow provenance defect is present in synonyms[0]:
    aureusimine C points to mibig:BGC0002287 even though the retained row carrying
    that name is BGC0000308. The seeder collects names across source rows then stamps
    all synonyms with the evidence-ranked lead accession. Correct source_concepts
    and OPEN identity discussions do not repair this particular name-source pointer;
    the proposed correction concerns attribution only.'
  outcome: concern
  target_ids:
  - CHEBI:167321
  evidence_ids:
  - support-2749-history-citations
  - support-2749-identity
  - support-2749-source-reading
  - support-2749-source-plan
  - support-2749-source-plan-acceptance
  - support-2749-notes
  - support-2749-curation
  - support-2749-query-mibig_compounds
  - support-2749-query-chebi_structures
  - support-2749-query-lotus_occurrences
  - support-2749-query-cyanometdb_occurrences
  - support-2749-query-npclassifier
  - support-2749-query-pubchem_bioassay
  - support-2749-query-bindingdb_targets
  - support-2749-query-antibioticmech_inchikeys
  - support-2749-query-chebi_origins
  - support-2749-table-mibig_compounds
  - support-2749-table-chebi_structures
  - support-2749-table-npclassifier
  - support-2749-table-chebi_origins
  - support-2749-synonym-provenance
  - support-2749-synonym-seeder
  - support-2749-synonym-schema
  dimensions:
  - name: citation_scope
    definition: Claim-level placements are distinct from new primary access or source
      independence.
    value: 'The entry-level MIBiG citations are PMID:31413323 for BGC0002287 and PMID:23302043
      for BGC0000308. The ChEBI-origin occurrence cites PMID:20851341. Both history
      events are seeding events. A narrow provenance defect is present in synonyms[0]:
      aureusimine C points to mibig:BGC0002287 even though the retained row carrying
      that name is BGC0000308. The seeder collects names across source rows then stamps
      all synonyms with the evidence-ranked lead accession. Correct source_concepts
      and OPEN identity discussions do not repair this particular name-source pointer;
      the proposed correction concerns attribution only.'
    evidence_ids:
    - support-2749-history-citations
    - support-2749-identity
    - support-2749-source-reading
    - support-2749-source-plan
    - support-2749-source-plan-acceptance
    - support-2749-notes
    - support-2749-curation
    - support-2749-query-mibig_compounds
    - support-2749-query-chebi_structures
    - support-2749-query-lotus_occurrences
    - support-2749-query-cyanometdb_occurrences
    - support-2749-query-npclassifier
    - support-2749-query-pubchem_bioassay
    - support-2749-query-bindingdb_targets
    - support-2749-query-antibioticmech_inchikeys
    - support-2749-query-chebi_origins
    - support-2749-table-mibig_compounds
    - support-2749-table-chebi_structures
    - support-2749-table-npclassifier
    - support-2749-table-chebi_origins
    - support-2749-synonym-provenance
    - support-2749-synonym-seeder
    - support-2749-synonym-schema
- assessment_id: support-2749-occurrence-assessment
  area: evidence
  topic: Occurrence, assays and target boundaries
  summary: The retained ChEBI-origin row reports Staphylococcus aureus / NCBITaxon:1280,
    with blank strain/component/comments. It is a broader occurrence claim, distinct
    from the JKD6008 producer and the Streptococcus mutans source context. The exact-key
    LOTUS frame is empty; no missing occurrence is inferred from that bounded negative.
    There is no retained exact-key PubChem AID row or blank sentinel, and BindingDB
    is empty. Source names, NRPS labels and a characterized cluster do not establish
    target-specific activity. No graph, pathway or molecular-target root is present.
  outcome: supported
  target_ids:
  - CHEBI:167321
  evidence_ids:
  - support-2749-occurrence
  - support-2749-taxonomy
  - support-2749-capture
  - support-2749-source-reading
  - support-2749-source-plan
  - support-2749-source-plan-acceptance
  - support-2749-notes
  - support-2749-curation
  - support-2749-query-mibig_compounds
  - support-2749-query-chebi_structures
  - support-2749-query-lotus_occurrences
  - support-2749-query-cyanometdb_occurrences
  - support-2749-query-npclassifier
  - support-2749-query-pubchem_bioassay
  - support-2749-query-bindingdb_targets
  - support-2749-query-antibioticmech_inchikeys
  - support-2749-query-chebi_origins
  - support-2749-table-mibig_compounds
  - support-2749-table-chebi_structures
  - support-2749-table-npclassifier
  - support-2749-table-chebi_origins
  dimensions:
  - name: occurrence_scope
    definition: Occurrence is not automatically production or an independent experiment.
    value: One ChEBI-origin placement at /1280; no strain equivalence.
    evidence_ids:
    - support-2749-occurrence
    - support-2749-taxonomy
    - support-2749-capture
    - support-2749-source-reading
    - support-2749-source-plan
    - support-2749-source-plan-acceptance
    - support-2749-notes
    - support-2749-curation
    - support-2749-query-mibig_compounds
    - support-2749-query-chebi_structures
    - support-2749-query-lotus_occurrences
    - support-2749-query-cyanometdb_occurrences
    - support-2749-query-npclassifier
    - support-2749-query-pubchem_bioassay
    - support-2749-query-bindingdb_targets
    - support-2749-query-antibioticmech_inchikeys
    - support-2749-query-chebi_origins
    - support-2749-table-mibig_compounds
    - support-2749-table-chebi_structures
    - support-2749-table-npclassifier
    - support-2749-table-chebi_origins
  - name: assay_target_scope
    definition: Actual AID rows, sentinels and bounded negatives remain distinct.
    value: No actual AID/sentinel or graph/target claim in retained scope.
    evidence_ids:
    - support-2749-occurrence
    - support-2749-taxonomy
    - support-2749-capture
    - support-2749-source-reading
    - support-2749-source-plan
    - support-2749-source-plan-acceptance
    - support-2749-notes
    - support-2749-curation
    - support-2749-query-mibig_compounds
    - support-2749-query-chebi_structures
    - support-2749-query-lotus_occurrences
    - support-2749-query-cyanometdb_occurrences
    - support-2749-query-npclassifier
    - support-2749-query-pubchem_bioassay
    - support-2749-query-bindingdb_targets
    - support-2749-query-antibioticmech_inchikeys
    - support-2749-query-chebi_origins
    - support-2749-table-mibig_compounds
    - support-2749-table-chebi_structures
    - support-2749-table-npclassifier
    - support-2749-table-chebi_origins
- assessment_id: support-2749-classification-assessment
  area: consistency
  topic: Filing and classifier applicability
  summary: The six-membered aromatic pyrazinone supports a bounded comparison with
    Pyrazine and Piperazine alkaloids. It does not directly demonstrate a five-membered
    tetramate scaffold, so Tetramate alkaloids remains an unvalidated model superclass
    rather than a structural conclusion or automatic record error. Alkaloids and Amino
    acids and Peptides intentionally route to UNCLASSIFIED. Source NRPS classification
    does not close the two upstream identity discussions.
  outcome: supported
  target_ids:
  - CHEBI:167321
  evidence_ids:
  - support-2749-classification
  - support-2749-filing-policy
  - support-2749-molecular-DATA
  - support-2749-queue
  - support-2749-source-reading
  - support-2749-source-plan
  - support-2749-source-plan-acceptance
  - support-2749-notes
  - support-2749-curation
  - support-2749-query-mibig_compounds
  - support-2749-query-chebi_structures
  - support-2749-query-lotus_occurrences
  - support-2749-query-cyanometdb_occurrences
  - support-2749-query-npclassifier
  - support-2749-query-pubchem_bioassay
  - support-2749-query-bindingdb_targets
  - support-2749-query-antibioticmech_inchikeys
  - support-2749-query-chebi_origins
  - support-2749-table-mibig_compounds
  - support-2749-table-chebi_structures
  - support-2749-table-npclassifier
  - support-2749-table-chebi_origins
  dimensions:
  - name: classification_applicability
    definition: Structural compatibility qualifies rather than validates a model output.
    value: Two labels → UNCLASSIFIED; six-membered pyrazinone does not verify tetramate
      superclass.
    evidence_ids:
    - support-2749-classification
    - support-2749-filing-policy
    - support-2749-molecular-DATA
    - support-2749-queue
    - support-2749-source-reading
    - support-2749-source-plan
    - support-2749-source-plan-acceptance
    - support-2749-notes
    - support-2749-curation
    - support-2749-query-mibig_compounds
    - support-2749-query-chebi_structures
    - support-2749-query-lotus_occurrences
    - support-2749-query-cyanometdb_occurrences
    - support-2749-query-npclassifier
    - support-2749-query-pubchem_bioassay
    - support-2749-query-bindingdb_targets
    - support-2749-query-antibioticmech_inchikeys
    - support-2749-query-chebi_origins
    - support-2749-table-mibig_compounds
    - support-2749-table-chebi_structures
    - support-2749-table-npclassifier
    - support-2749-table-chebi_origins
- assessment_id: support-2749-completion-assessment
  area: completeness
  topic: Scope and unavailable required checks
  summary: Whole current owner/history and assigned saved source/molecular payloads
    were personally read; input hashes and ownership were independently joined to
    accepted original intakes. No mechanism/pathway/target roots occur in this owner,
    so no maintained-reader invocation is assigned. Five local native commands passed.
    Full QC, OAK ontology consistency and external primary/authority verification
    remain unavailable under the no-request hold, so completion is partial. The minor
    synonym provenance finding requires a maintained-source correction; OPEN naming/shared-structure
    questions remain unresolved.
  outcome: supported
  target_ids:
  - CHEBI:167321
  evidence_ids:
  - support-2749-owner
  - support-2749-capture
  - support-2749-intake
  - support-2749-intake-original
  - support-2749-intake-acceptance
  - support-2749-source-reading
  - support-2749-molecular-reading
  - support-2749-local-gates
  - support-2749-queue
  dimensions:
  - name: review_completion
    definition: Complete assigned reading is distinct from completion of all required
      checks.
    value: partial; scientific_review true; full QC/OAK/external authority unavailable
    evidence_ids:
    - support-2749-owner
    - support-2749-capture
    - support-2749-intake
    - support-2749-intake-original
    - support-2749-intake-acceptance
    - support-2749-source-reading
    - support-2749-molecular-reading
    - support-2749-local-gates
    - support-2749-queue
findings:
- finding_id: support-2749-synonym-origin-mismatch
  issue_key: leuvalin-aureusimine-c-synonym-source-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Aureusimine C synonym points to the wrong retained naming row
  description: The current /synonyms/0 value aureusimine C cites mibig:BGC0002287.
    The complete retained MIBiG row417 (BGC0000308 v5, compound3) carries that name;
    row2766 (BGC0002287 v2, compound2) carries leuvalin. SourceConcept mappings are
    correct. Seeder605–624 separates naming from lead selection,953–957 aggregates
    names, and1006–1009 stamps every synonym with the evidence-ranked lead accession.
    This is a confirmed local per-name provenance mismatch, not schema invalidity,
    proof of a wrong upstream structure, or resolution of either OPEN identity discussion.
  target_ids:
  - CHEBI:167321
  field_paths:
  - /synonyms/0/source
  evidence_ids:
  - support-2749-synonym-provenance
  - support-2749-synonym-seeder
  - support-2749-synonym-schema
  - support-2749-query-mibig_compounds
  - support-2749-table-mibig_compounds
  ownership_note: The generated owner exposes the mismatch; the maintained naming/attribution
    logic is scripts/seed_from_sources.py, already captured by this intake. No record
    or source edit was performed.
actions:
- action_id: support-2749-preserve-synonym-origin
  description: Preserve the originating source accession alongside each collected
    name in the maintained seeder and emit aureusimine C with its retained BGC0000308
    naming provenance. Retain both OPEN identity discussions and all separate producer/locus
    grades; do not infer a merger or split.
  finding_ids:
  - support-2749-synonym-origin-mismatch
  target_ids:
  - CHEBI:167321
  ownership_note: Proposed maintained change to captured scripts/seed_from_sources.py,
    with regenerated record review afterward; no generated YAML-only edit or implementation
    is performed here.
  acceptance_checks:
  - A focused multi-source naming regression must retain a discarded alias with its
    originating accession when another row wins lead selection.
  - Leuvalin retains CHEBI:167321, full key WLZSJRZITZLEPW-UHFFFAOYSA-N, both correct
    SourceConcept mappings, separate producer/locus grades and both OPEN identity
    discussions.
  - Regenerate through the maintained workflow and run the required local validation/reproduction
    checks; source and record changes require their own review.
limitations:
- Primary publications, live authorities, spectra, sequences, strain identities and
  complete natural-product identity were not independently verified; full QC/OAK/external
  checks remain unavailable.
- Canonical comparisons true; limited map14; aromatic amide matcher0; full identity
  false. Neither saved form has a potential tetrahedral or double-bond stereo entry.
  This supports the limited atom-centred stereo_complete:true representation, without
  proving the source names or natural identity. The shared diagnostic has six globally
  unassigned warnings.
- Retained exact-key/ID negatives are bounded by captured files and predicates, not
  universal absence or inactivity. Cached taxonomy and separate source grades are
  not upgraded.
- Both upstream identity discussions remain OPEN. The minor finding addresses a synonym
  source pointer only.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Current scientific judgments were authored from earned275 owner/source/intake/molecular
  evidence; prior batch artifacts supplied interface logic only.
- No source record or native curation status was changed. Proposed actions are unperformed.
- The PathwayMech correction applies only to2750; no supplemental positive or negative
  row credit is claimed for this owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-275
```
