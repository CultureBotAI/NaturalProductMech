# Local evidence review: stellatic acid

- Review: 20261104T142158Z-stellatic-acid
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T13:28:08.548322Z
- Finished UTC: 2026-11-04T14:21:58.797459Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Stellatic acid retains an exact local ChEBI/MIBiG structure join and internally consistent stored forms. The ChEBI sesterterpenoid definition and versioned Diterpenoids/Valparane prediction remain distinct assertions with unresolved model applicability; no source correction is established.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2401; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:169999 | data/natural_products/terpenoids/stellatic-acid.yaml | generated | stellatic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:169999 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:169999 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:169999 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:169999 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:169999 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:169999 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:169999 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:169999 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity/form consistency; natural identity unverified

identity: supported. Targets: CHEBI:169999.

The retained CHEBI:169999 identifier is grounded by the complete key FSKFLBQJBSQQKA-DMZCBJAKSA-N shared by the saved MIBiG and three-star ChEBI rows. MIBiG supplies the structure; ChEBI supplies the definition and exact concept join, while NPA032764 is a cross-reference. Both original forms normalize to this key and C25H38O2. This supports retained identity/form consistency, not independently verified natural identity or the truth of every database definition.

### Original stored-form and stereochemical scope

representation: supported. Targets: CHEBI:169999.

Both forms are neutral C25H38O2 with 27 heavy atoms and 29 bonds, five specified tetrahedral centers, and two specified double bonds. Saved SMILES bond 14 is Z and bond 21 is E; those are diagnostic indices, not chemical locants. All ten comparison flags are true and the original atom match covers 27 atoms, while full_graph_identity_established remains false. The retained true stereo flag is a source encoding assertion, not fresh stereochemical proof.

### Separate source producer, locus and taxonomic scopes

provenance: supported. Targets: CHEBI:169999.

BGC0002610 v3 compound 1 names Aspergillus stellatus NCBITaxon:1549217 as SOURCE_ASSERTION; its LC073704.1:101–6568 locus remains CLUSTER_UNSTATED with no evidence methods supplied. The ChEBI definition says Emericella variecolor, and the saved ChEBI origin note says it is another name for the recorded species. This is retained source attribution, not a fresh nomenclatural reconciliation or strain identity proof. The ignored-inclusive implemented-curation scan found no applicable correction.

### Citation roles and retained source attribution

evidence: supported. Targets: CHEBI:169999.

PMID:26351860 is the MIBiG entry-level reference repeated on producer and locus. The two LOTUS DOI placements and ChEBI origin PMID:15612624 have occurrence roles; ChEBI:169999 is the definition source. Repetition and co-occurrence of these citations do not demonstrate independent experiments. No primary article was freshly read or verified.

### Bounded occurrence and assay/target evidence

evidence: supported. Targets: CHEBI:169999.

The owner has three occurrence placements: two LOTUS assertions and one ChEBI origin, all under NCBITaxon:1549217. The two LOTUS DOIs remain separate source assertions, while the ChEBI origin includes the Emericella variecolor naming note. Neither matching the producer taxon nor repeated citation placement upgrades occurrence to experimentally established production. Saved occurrence queries are bounded to the retained exact-key/source joins.

### Versioned model fidelity and bounded applicability

consistency: concern. Targets: CHEBI:169999.

NPClassifier npclassifier.gnps2.org@2026-09-07 is faithfully retained as Terpenoids/Diterpenoids/Valparane diterpenoids with is_glycoside:false. The retained ChEBI definition instead calls the C25 compound a sesterterpenoid. This is a bounded model-applicability concern, not evidence that the prediction was ingested incorrectly. C25 and the local ring pattern alone do not adjudicate the model class; its fine applicability remains unresolved. No separate sugar is shown by the saved topology.

### Actual evidence coverage and remaining scientific limits

completeness: unknown. Targets: CHEBI:169999.

Complete owner/history, actual canonical intake, retained source rows and negative query frames, and both original molecular forms have been read. All four mechanism roots are absent in this owner, so no maintained-mechanism reader applies. Full QC/OAK, fresh primary and taxonomic/assay verification, and independent natural identity or stereochemical authentication remain unavailable. This is a partial review with no supported record-edit finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2401-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/stellatic-acid.yaml; Complete current plaintext, including all curation_history entries | supports | Whole stellatic acid owner and 3 retained history events; EXACT grounding and SEEDED status remain unchanged. Personal full plaintext/history reading carries. |
| bgc-2401-capture | /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json; /records/0 | supports | Complete actual captured owner, metadata, root presence and history; count equality is not scientific authentication. |
| bgc-2401-intake | /private/tmp/npm-review-work/shared-next-batch241/intakes/2401-inspect-001.json; /status; /repository; /source; /targets | supports | Actual target, complete ownership map and all 37 current input placements, exactly matching the accepted source plan. |
| bgc-2401-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch241/root-intake-acceptance-001.json; /status | supports | ROOT acceptance of the actual ten canonical intakes; this owner’s complete inputs are linked separately. |
| bgc-2401-grounding-owner | /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/label; /records/0/owner_document/chemical_structure; /records/0/owner_document/definition; /records/0/owner_document/definition_source; /records/0/owner_document/xrefs; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status | supports | Exact retained identifier, full structure, grounding/source concepts and present definition/cross-reference or grounding-note fields. This is owner content, not a new external identity check. |
| bgc-2401-origin-owner | /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups; /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts | supports | Complete producer/locus/source assertions, grades, citations and present genome/coordinate fields. Evidence grades do not become fresh experimental verification. |
| bgc-2401-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json; /records/0/owner_document | supports | The owner retains 3 occurrence placements; bioactivities and bioactivity_summary are absent. |
| bgc-2401-classification-owner | /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json; /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway; /records/0/owner_document/bgc_class | supports | Exact named/versioned classifier arrays and glycoside flag, separate filing pathway and source class fields; model applicability remains an assessment question. |
| bgc-2401-history-owner | /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json; /records/0/owner_document/curation_status; /records/0/owner_document/curation_history | supports | Complete original status/history; review authoring does not promote or rewrite the native record. |
| bgc-2401-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json; /records/0/owner_document | supports | The complete owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs and molecular_targets. This exact owner-scoped absence makes a maintained-mechanism call inapplicable here. |
| bgc-2401-chemistry | /private/tmp/npm-review-work/shared-next-batch241/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/formula; /records/0/smiles/computed/formal_charge; /records/0/smiles/computed/standard_inchi; /records/0/smiles/computed/standard_inchi_key; /records/0/smiles/computed/canonical_isomeric_smiles; /records/0/smiles/computed/canonical_nonisomeric_smiles; /records/0/smiles/computed/atom_count; /records/0/smiles/computed/heavy_atom_count; /records/0/smiles/computed/bond_count; /records/0/smiles/computed/element_counts; /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/formula; /records/0/inchi/computed/formal_charge; /records/0/inchi/computed/standard_inchi; /records/0/inchi/computed/standard_inchi_key; /records/0/inchi/computed/canonical_isomeric_smiles; /records/0/inchi/computed/canonical_nonisomeric_smiles; /records/0/inchi/computed/atom_count; /records/0/inchi/computed/heavy_atom_count; /records/0/inchi/computed/bond_count; /records/0/inchi/computed/element_counts; /records/0/inchi/computed/stereo_counts | supports | Both saved forms have all ten comparison flags true, a complete supplied atom match, and full_graph_identity_established:false. Exact structure strings and normalized scalars are retained; natural identity is not established. |
| bgc-2401-topology | /private/tmp/npm-review-work/shared-next-batch241/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds; /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo; /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices; /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings; /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs; /records/0/inchi/computed/fragment_atom_indices | supports | The complete saved tables show one connected structure, carbocyclic rings of lengths 5, 6 and 11, a terminal exomethylene, and one carboxylic acid (SMILES C16=O17 with O18H). No ester, amide, ether bridge or C5O candidate is reported. These are observations of the stored encoding; they do not independently assign a named natural scaffold. |
| bgc-2401-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-current241-first-five-diagnostic-reading-001.json; /records/0; /coverage; /lossless_reading_method; /limits | supports | BGC personally read all ten first-five forms:258 atom rows,278 bond rows, all strings/scalars/rings/stereo/motifs/maps and complete intake roles. Exact lossless table factoring and limits are disclosed. |
| bgc-2401-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch241/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /warning_count; /warning_record_attribution; /limits; /records/0; /stderr | supports | ROOT accepted one original twenty-form diagnostic. This owner has all ten comparisons true; stderr is empty. The recorded full-graph-identity flag remains false, and natural identity is not established by these checks. |
| bgc-2401-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch241/chemistry-local/diagnostic-execution-001.json; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original execution and saved stdout/stderr pins; no new molecular parse is performed by this review. |
| bgc-2401-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines381–435 | supports | The schema separates retained stereochemical completeness and versioned computed classifications; it does not make model output a source assertion. |
| bgc-2401-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines155–173 | supports | The extractor derives the flag from unassigned chiral centers in its original input; this does not experimentally validate stereochemistry. |
| bgc-2401-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines295–306;988–1022 | supports | The seeder preserves source structure/flag and exact versioned classifier arrays, with filing determined by the pathway array. Fidelity is separate from scientific applicability. |
| bgc-2401-source-reading | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-current241-source-reading-001.json; /scope; /division; /reading; /verification; /cautions | supports | BGC personally read all eight assigned contexts:72 frames,41 positive rows and414 fields, including these five selected contexts and three preterpestacins. Complete raw/history carry and source meanings are separately attributed. |
| bgc-2401-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /limitations; /source_stage_contract | supports | Complete17-context scope combines BGC41 rows and Support48 rows, plus Native14 cached stanzas and the bounded implemented-curation scan. Author-time pending fields are historical source-stage metadata; later runtime authority is separately linked. |
| bgc-2401-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch241/root-source-plan-acceptance-001.json; /status | supports | ROOT accepted the actual source plan and its reconciliation with current canonical input maps; source-stage conditional prose is not used as missing runtime evidence. |
| bgc-2401-curation-scope | /private/tmp/npm-review-work/shared-next-batch241-tentative/native-prep/native-current241-implemented-curation-scan-001.json; /scope; /ignored_files_included; /table_pins; /scanned_tables; /lexical_positive_rows; /applicable_rows; /conclusion; /assay_exclusion_scope; /reserved_files; /limitations | supports | Ignored-inclusive bounded scan of nine relevant tables from eleven enumerated TSVs found zero lexical/applicable hits. The exact T-2 assay tuple has no exclusion; this does not verify its identity or protocol. Reserved files do not become effective corrections. |
| bgc-2401-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/12 | supports | Complete retained stanzas for this owner’s source taxon IDs contain names and exact synonyms only. These do not freshly establish ancestry, production or strain equivalence. |
| bgc-2401-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch241-tentative/native-prep/native-current241-cached-taxonomy-reading-001.json; /scope; /counts; /readings; /cautions | supports | Native personally read all14 inventory stanzas; BGC additionally read the eleven unique first-five stanzas at68f0ab. The source Fusarium incarnatum versus cached Fusarium cf. incarnatum distinction is preserved, without a new taxonomy lookup. |
| bgc-2401-direct-contexts | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-target-input-plan-001.json; /records/0/proposed_companion_paths; /records/0/direct_companion_predicates | supports | Exact one-hop same-locus context membership, including any empty list. There is no transitive expansion or automatic identity/activity/mechanism transfer. |
| bgc-2401-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 positive placements, exact predicate/query and all fields. A blank AID would be a sentinel, not an assay; none occurs in these selected contexts. |
| bgc-2401-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line1; physical lines3317–3317; row_sha256 131e6d7f67755caaae7c710128398405504b3bf4d57cf09ea0c52c420bf61928 | supports | Exact full-key compound/version/index, producer/locus grades, genome and citation-level fields. BGC complete selected source-row reading carries. |
| bgc-2401-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame: 1 positive placements, exact predicate/query and all fields. A blank AID would be a sentinel, not an assay; none occurs in these selected contexts. |
| bgc-2401-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line1; physical lines43564–43564; row_sha256 4f8b9c2668aa98113814bd45b76f5577edcc69c1eb6205ce45293e79a8f4966e | supports | Exact full-key ChEBI concept, retained definition and source grounding fields. BGC complete selected source-row reading carries. |
| bgc-2401-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 2 positive placements, exact predicate/query and all fields. A blank AID would be a sentinel, not an assay; none occurs in these selected contexts. |
| bgc-2401-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line1; physical lines1550–1550; row_sha256 4f712b61b924499f6858bd54c449cc8321ceb7e62b66565041b846ed09f77a2e; physical lines1551–1551; row_sha256 d7bdd8c060aad5a3decbfba45d8e3d76031d9df0c898ff36120ad78e2af2bb76 | supports | All organism/reference strings preserve occurrence scope; duplicate references do not establish independent studies or production. BGC complete selected source-row reading carries. |
| bgc-2401-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame: 0 positive placements, exact predicate/query and all fields. A blank AID would be a sentinel, not an assay; none occurs in these selected contexts. |
| bgc-2401-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 positive placements, exact predicate/query and all fields. A blank AID would be a sentinel, not an assay; none occurs in these selected contexts. |
| bgc-2401-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line1; physical lines603–603; row_sha256 6ca95045111453905473de32667e2e75a9ef9946470232cda10635fb51c98671 | supports | Exact named/versioned model arrays and glycoside prediction; scientific applicability is not inferred from ingestion fidelity. BGC complete selected source-row reading carries. |
| bgc-2401-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame: 0 positive placements, exact predicate/query and all fields. A blank AID would be a sentinel, not an assay; none occurs in these selected contexts. |
| bgc-2401-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame: 0 positive placements, exact predicate/query and all fields. A blank AID would be a sentinel, not an assay; none occurs in these selected contexts. |
| bgc-2401-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame: 0 positive placements, exact predicate/query and all fields. A blank AID would be a sentinel, not an assay; none occurs in these selected contexts. |
| bgc-2401-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame: 1 positive placements, exact predicate/query and all fields. A blank AID would be a sentinel, not an assay; none occurs in these selected contexts. |
| bgc-2401-source-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Header line1; physical lines17249–17249; row_sha256 4611f7dc3eedb266a35bbb3595295a0ffb902e8f227b363a08fe0ae3d8625869 | supports | Complete ChEBI source taxon, strain/detection-context, comment and citation fields; no automatic producer assignment. BGC complete selected source-row reading carries. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-241/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-241/native-current241-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-241/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-241/native-current241-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-241/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-241/native-current241-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-241/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-241/native-current241-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-241/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-241/native-current241-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only: no fresh primary literature, taxonomy, assay protocol, natural-identity or experimental-stereochemistry verification.
- Full QC and complete OAK coverage remain unavailable. Local normalization, motifs and one atom match do not establish independent full-graph or natural-form identity.
- Producer, locus, occurrence, strain/detection context and citation roles remain distinct; congeners and repeated references do not transfer product claims or experimental independence.
- Model values are retained with provenance. Fine applicability concerns do not establish a source-ingestion error or justify a replacement.
- The complete owner has no graph/pathway/component/target roots. No maintained-mechanism check is claimed for this record; no source status/history edit is proposed.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all ten first-five forms: 258 atom rows and 278 bond rows, all scalar/ring/stereo/motif/map fields. Diagnostic atom/bond indices are zero-based, not biochemical locants. Original stderr is empty.
- Source meanings remain disjoint: BGC eight contexts/41 rows/414 fields/72 frames; Support nine contexts/48 rows/485 fields/81 frames. Native owns all 14 cached stanzas and the bounded ignored-inclusive curation scan; BGC additionally read the eleven first-five unique cached stanzas. Prior complete companion raw/history carries remain attributed.
- BGC operated the admitted source collector and composer. ROOT operated the actual canonical intakes and original diagnostic. These five owners have no maintained-reader call; no runtime is launched by authoring.
- All scientific outcomes are partial, with no supported finding or action. Missing fresh verification, model concern or diagnostic success alone is not a record-edit finding.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T142158Z-stellatic-acid
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: stellatic acid'
started_at: '2026-11-04T13:28:08.548322Z'
finished_at: '2026-11-04T14:21:58.797459Z'
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
summary: Stellatic acid retains an exact local ChEBI/MIBiG structure join and internally
  consistent stored forms. The ChEBI sesterterpenoid definition and versioned Diterpenoids/Valparane
  prediction remain distinct assertions with unresolved model applicability; no source
  correction is established.
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
  - path: data/natural_products/terpenoids/stellatic-acid.yaml
    sha256: a1f705c1351288a127c4d03a3fc8ccfb67f133a6d203f67a1deb2434162b2b46
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
  selection: Campaign path order 2401; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:169999
targets:
- target_id: CHEBI:169999
  path: data/natural_products/terpenoids/stellatic-acid.yaml
  label: stellatic acid
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
  - CHEBI:169999
  command: just validate-strict data/natural_products/terpenoids/stellatic-acid.yaml
    data/natural_products/terpenoids/t-2-toxin.yaml data/natural_products/terpenoids/taxa-4-20-11-12-diene.yaml
    data/natural_products/terpenoids/taxa-4-5-11-12-diene.yaml data/natural_products/terpenoids/terpestacin.yaml
    data/natural_products/terpenoids/thaliandiol.yaml data/natural_products/terpenoids/thalianin.yaml
    data/natural_products/terpenoids/thalianol.yaml data/natural_products/terpenoids/thioplatencin.yaml
    data/natural_products/terpenoids/thioplatensilin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-241/validate-strict-selected10-001.tsv
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
  - CHEBI:169999
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-241/validate-all-001.tsv
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
  - CHEBI:169999
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
  - CHEBI:169999
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
  - CHEBI:169999
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-241/review-queue-001.tsv
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
  - CHEBI:169999
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:169999
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:169999
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2401-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/stellatic-acid.yaml
  locator: Complete current plaintext, including all curation_history entries
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Whole stellatic acid owner and 3 retained history events; EXACT grounding
    and SEEDED status remain unchanged. Personal full plaintext/history reading carries.
  snapshot_sha256: a1f705c1351288a127c4d03a3fc8ccfb67f133a6d203f67a1deb2434162b2b46
- evidence_id: bgc-2401-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json
  locator: /records/0
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Complete actual captured owner, metadata, root presence and history; count
    equality is not scientific authentication.
  snapshot_sha256: f239673f23d4e88e28b54da9528cd596d60dbaf00d7821efe59e65919d79d10d
- evidence_id: bgc-2401-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/intakes/2401-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Actual target, complete ownership map and all 37 current input placements,
    exactly matching the accepted source plan.
  snapshot_sha256: 61861c90ea033a24c654cea97c26196fb6cc8aa852c11131370f13d95f57e155
- evidence_id: bgc-2401-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/root-intake-acceptance-001.json
  locator: /status
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: ROOT acceptance of the actual ten canonical intakes; this owner’s complete
    inputs are linked separately.
  snapshot_sha256: 6eed59a29a57474207d5458200dcc6c0435b2ee1d2911f33e4ce783f9d70a5b2
- evidence_id: bgc-2401-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/label;
    /records/0/owner_document/chemical_structure; /records/0/owner_document/definition;
    /records/0/owner_document/definition_source; /records/0/owner_document/xrefs;
    /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Exact retained identifier, full structure, grounding/source concepts and
    present definition/cross-reference or grounding-note fields. This is owner content,
    not a new external identity check.
  snapshot_sha256: f239673f23d4e88e28b54da9528cd596d60dbaf00d7821efe59e65919d79d10d
- evidence_id: bgc-2401-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups;
    /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Complete producer/locus/source assertions, grades, citations and present
    genome/coordinate fields. Evidence grades do not become fresh experimental verification.
  snapshot_sha256: f239673f23d4e88e28b54da9528cd596d60dbaf00d7821efe59e65919d79d10d
- evidence_id: bgc-2401-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: The owner retains 3 occurrence placements; bioactivities and bioactivity_summary
    are absent.
  snapshot_sha256: f239673f23d4e88e28b54da9528cd596d60dbaf00d7821efe59e65919d79d10d
- evidence_id: bgc-2401-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway;
    /records/0/owner_document/bgc_class
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Exact named/versioned classifier arrays and glycoside flag, separate filing
    pathway and source class fields; model applicability remains an assessment question.
  snapshot_sha256: f239673f23d4e88e28b54da9528cd596d60dbaf00d7821efe59e65919d79d10d
- evidence_id: bgc-2401-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json
  locator: /records/0/owner_document/curation_status; /records/0/owner_document/curation_history
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Complete original status/history; review authoring does not promote or
    rewrite the native record.
  snapshot_sha256: f239673f23d4e88e28b54da9528cd596d60dbaf00d7821efe59e65919d79d10d
- evidence_id: bgc-2401-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: The complete owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs
    and molecular_targets. This exact owner-scoped absence makes a maintained-mechanism
    call inapplicable here.
  snapshot_sha256: f239673f23d4e88e28b54da9528cd596d60dbaf00d7821efe59e65919d79d10d
- evidence_id: bgc-2401-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons;
    /records/0/atom_correspondence; /records/0/smiles/computed/formula; /records/0/smiles/computed/formal_charge;
    /records/0/smiles/computed/standard_inchi; /records/0/smiles/computed/standard_inchi_key;
    /records/0/smiles/computed/canonical_isomeric_smiles; /records/0/smiles/computed/canonical_nonisomeric_smiles;
    /records/0/smiles/computed/atom_count; /records/0/smiles/computed/heavy_atom_count;
    /records/0/smiles/computed/bond_count; /records/0/smiles/computed/element_counts;
    /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/formula; /records/0/inchi/computed/formal_charge;
    /records/0/inchi/computed/standard_inchi; /records/0/inchi/computed/standard_inchi_key;
    /records/0/inchi/computed/canonical_isomeric_smiles; /records/0/inchi/computed/canonical_nonisomeric_smiles;
    /records/0/inchi/computed/atom_count; /records/0/inchi/computed/heavy_atom_count;
    /records/0/inchi/computed/bond_count; /records/0/inchi/computed/element_counts;
    /records/0/inchi/computed/stereo_counts
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Both saved forms have all ten comparison flags true, a complete supplied
    atom match, and full_graph_identity_established:false. Exact structure strings
    and normalized scalars are retained; natural identity is not established.
  snapshot_sha256: 2f54f5781336e79e428ed10ad729dd8ff0b7c4fae50d162fd117d1dc82f1a04e
- evidence_id: bgc-2401-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons;
    /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds;
    /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo;
    /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices;
    /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings;
    /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs;
    /records/0/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: The complete saved tables show one connected structure, carbocyclic rings
    of lengths 5, 6 and 11, a terminal exomethylene, and one carboxylic acid (SMILES
    C16=O17 with O18H). No ester, amide, ether bridge or C5O candidate is reported.
    These are observations of the stored encoding; they do not independently assign
    a named natural scaffold.
  snapshot_sha256: 2f54f5781336e79e428ed10ad729dd8ff0b7c4fae50d162fd117d1dc82f1a04e
- evidence_id: bgc-2401-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-current241-first-five-diagnostic-reading-001.json
  locator: /records/0; /coverage; /lossless_reading_method; /limits
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: BGC personally read all ten first-five forms:258 atom rows,278 bond rows,
    all strings/scalars/rings/stereo/motifs/maps and complete intake roles. Exact
    lossless table factoring and limits are disclosed.
  snapshot_sha256: 4247df3c2287df2a783988ab53a7929c02bae1dddb9c4481dcbd8e7ceee92d25
- evidence_id: bgc-2401-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /warning_count; /warning_record_attribution;
    /limits; /records/0; /stderr
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: ROOT accepted one original twenty-form diagnostic. This owner has all ten
    comparisons true; stderr is empty. The recorded full-graph-identity flag remains
    false, and natural identity is not established by these checks.
  snapshot_sha256: 7bdbb8221f58663ffadf5fa8519563ea76adaa19a8ecd47b368decb5201e296d
- evidence_id: bgc-2401-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/chemistry-local/diagnostic-execution-001.json
  locator: /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Exact original execution and saved stdout/stderr pins; no new molecular
    parse is performed by this review.
  snapshot_sha256: 3c59a70379ecc64abc7d86c0361093d19ce87795fdc9561c3fc7b7bd4035f23f
- evidence_id: bgc-2401-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines381–435
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: The schema separates retained stereochemical completeness and versioned
    computed classifications; it does not make model output a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2401-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines155–173
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: The extractor derives the flag from unassigned chiral centers in its original
    input; this does not experimentally validate stereochemistry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2401-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines295–306;988–1022
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: The seeder preserves source structure/flag and exact versioned classifier
    arrays, with filing determined by the pathway array. Fidelity is separate from
    scientific applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2401-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-current241-source-reading-001.json
  locator: /scope; /division; /reading; /verification; /cautions
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: BGC personally read all eight assigned contexts:72 frames,41 positive rows
    and414 fields, including these five selected contexts and three preterpestacins.
    Complete raw/history carry and source meanings are separately attributed.
  snapshot_sha256: abe53f5b4d87e97e398bf2f1860dfc115ddbe6b970431a2c58ceda09f7b53c51
- evidence_id: bgc-2401-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /limitations;
    /source_stage_contract
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Complete17-context scope combines BGC41 rows and Support48 rows, plus Native14
    cached stanzas and the bounded implemented-curation scan. Author-time pending
    fields are historical source-stage metadata; later runtime authority is separately
    linked.
  snapshot_sha256: 59bd6d012105acf2b6eb7048fecb2a74d393d5493a2e50e332a38635fdf3d923
- evidence_id: bgc-2401-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241/root-source-plan-acceptance-001.json
  locator: /status
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: ROOT accepted the actual source plan and its reconciliation with current
    canonical input maps; source-stage conditional prose is not used as missing runtime
    evidence.
  snapshot_sha256: a056cd753c436e9cae909b69f4c7d920ccf86492447a43191695c6cbec53cd5f
- evidence_id: bgc-2401-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/native-prep/native-current241-implemented-curation-scan-001.json
  locator: /scope; /ignored_files_included; /table_pins; /scanned_tables; /lexical_positive_rows;
    /applicable_rows; /conclusion; /assay_exclusion_scope; /reserved_files; /limitations
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Ignored-inclusive bounded scan of nine relevant tables from eleven enumerated
    TSVs found zero lexical/applicable hits. The exact T-2 assay tuple has no exclusion;
    this does not verify its identity or protocol. Reserved files do not become effective
    corrections.
  snapshot_sha256: 30e07c0cd9f7e67b61cbe87c194e0f98e2517854df6476f8eb7cb22da53f4c5c
  search_scope: 'All17 current context metadata: owner/source identifiers, full keys,
    ownedBGCs, labels/slugs, taxa/chemical IDs,17 exact BGC:compound IDs and1 actual
    AID tuple;146 case-insensitive literal tokens. Raw mechanism full keys and explicit
    taxon81972/A.lyrata strings included as literal scan tokens without adding cache
    authority. Complete rows scanned in9 current curation TSVs via ignored-inclusive
    Path.rglob enumeration of all11 TSVs.'
- evidence_id: bgc-2401-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/12
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Complete retained stanzas for this owner’s source taxon IDs contain names
    and exact synonyms only. These do not freshly establish ancestry, production or
    strain equivalence.
  snapshot_sha256: d1262a817775335b95bf149194a3c460b22c0b5d4f19de6e9134275eea5e7333
- evidence_id: bgc-2401-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/native-prep/native-current241-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /readings; /cautions
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Native personally read all14 inventory stanzas; BGC additionally read the
    eleven unique first-five stanzas at68f0ab. The source Fusarium incarnatum versus
    cached Fusarium cf. incarnatum distinction is preserved, without a new taxonomy
    lookup.
  snapshot_sha256: bc70c42f78523d260bd309bab9acbd0cd63ab009bcaae71948181ab0ecd92ddc
- evidence_id: bgc-2401-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-target-input-plan-001.json
  locator: /records/0/proposed_companion_paths; /records/0/direct_companion_predicates
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Exact one-hop same-locus context membership, including any empty list.
    There is no transitive expansion or automatic identity/activity/mechanism transfer.
  snapshot_sha256: 47b6f5a95bdd600cdc811c39f40ab509291e1ca62b07401cd07e1f34b82c3dfc
- evidence_id: bgc-2401-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 positive placements, exact predicate/query
    and all fields. A blank AID would be a sentinel, not an assay; none occurs in
    these selected contexts.'
  snapshot_sha256: d1262a817775335b95bf149194a3c460b22c0b5d4f19de6e9134275eea5e7333
  search_scope: Saved original local inventory only; exact mibig_compounds predicate
    exact complete standard_inchi_key equality; query value "FSKFLBQJBSQQKA-DMZCBJAKSA-N".
    All matched rows or the complete empty result are retained. No replay or external
    search.
- evidence_id: bgc-2401-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line1; physical lines3317–3317; row_sha256 131e6d7f67755caaae7c710128398405504b3bf4d57cf09ea0c52c420bf61928
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Exact full-key compound/version/index, producer/locus grades, genome and
    citation-level fields. BGC complete selected source-row reading carries.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2401-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: 'Complete saved chebi_structures frame: 1 positive placements, exact predicate/query
    and all fields. A blank AID would be a sentinel, not an assay; none occurs in
    these selected contexts.'
  snapshot_sha256: d1262a817775335b95bf149194a3c460b22c0b5d4f19de6e9134275eea5e7333
  search_scope: Saved original local inventory only; exact chebi_structures predicate
    exact complete standard_inchi_key equality; query value "FSKFLBQJBSQQKA-DMZCBJAKSA-N".
    All matched rows or the complete empty result are retained. No replay or external
    search.
- evidence_id: bgc-2401-source-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line1; physical lines43564–43564; row_sha256 4f8b9c2668aa98113814bd45b76f5577edcc69c1eb6205ce45293e79a8f4966e
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Exact full-key ChEBI concept, retained definition and source grounding
    fields. BGC complete selected source-row reading carries.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2401-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 2 positive placements, exact predicate/query
    and all fields. A blank AID would be a sentinel, not an assay; none occurs in
    these selected contexts.'
  snapshot_sha256: d1262a817775335b95bf149194a3c460b22c0b5d4f19de6e9134275eea5e7333
  search_scope: Saved original local inventory only; exact lotus_occurrences predicate
    exact complete standard_inchi_key equality; query value "FSKFLBQJBSQQKA-DMZCBJAKSA-N".
    All matched rows or the complete empty result are retained. No replay or external
    search.
- evidence_id: bgc-2401-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line1; physical lines1550–1550; row_sha256 4f712b61b924499f6858bd54c449cc8321ceb7e62b66565041b846ed09f77a2e;
    physical lines1551–1551; row_sha256 d7bdd8c060aad5a3decbfba45d8e3d76031d9df0c898ff36120ad78e2af2bb76
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: All organism/reference strings preserve occurrence scope; duplicate references
    do not establish independent studies or production. BGC complete selected source-row
    reading carries.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2401-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: 'Complete saved cyanometdb_occurrences frame: 0 positive placements, exact
    predicate/query and all fields. A blank AID would be a sentinel, not an assay;
    none occurs in these selected contexts.'
  snapshot_sha256: d1262a817775335b95bf149194a3c460b22c0b5d4f19de6e9134275eea5e7333
  search_scope: Saved original local inventory only; exact cyanometdb_occurrences
    predicate exact complete standard_inchi_key equality; query value "FSKFLBQJBSQQKA-DMZCBJAKSA-N".
    All matched rows or the complete empty result are retained. No replay or external
    search.
- evidence_id: bgc-2401-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 positive placements, exact predicate/query
    and all fields. A blank AID would be a sentinel, not an assay; none occurs in
    these selected contexts.'
  snapshot_sha256: d1262a817775335b95bf149194a3c460b22c0b5d4f19de6e9134275eea5e7333
  search_scope: Saved original local inventory only; exact npclassifier predicate
    exact complete standard_inchi_key equality; query value "FSKFLBQJBSQQKA-DMZCBJAKSA-N".
    All matched rows or the complete empty result are retained. No replay or external
    search.
- evidence_id: bgc-2401-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line1; physical lines603–603; row_sha256 6ca95045111453905473de32667e2e75a9ef9946470232cda10635fb51c98671
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside prediction; scientific
    applicability is not inferred from ingestion fidelity. BGC complete selected source-row
    reading carries.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2401-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay frame: 0 positive placements, exact predicate/query
    and all fields. A blank AID would be a sentinel, not an assay; none occurs in
    these selected contexts.'
  snapshot_sha256: d1262a817775335b95bf149194a3c460b22c0b5d4f19de6e9134275eea5e7333
  search_scope: Saved original local inventory only; exact pubchem_bioassay predicate
    exact complete standard_inchi_key equality; query value "FSKFLBQJBSQQKA-DMZCBJAKSA-N".
    All matched rows or the complete empty result are retained. No replay or external
    search.
- evidence_id: bgc-2401-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: 'Complete saved bindingdb_targets frame: 0 positive placements, exact predicate/query
    and all fields. A blank AID would be a sentinel, not an assay; none occurs in
    these selected contexts.'
  snapshot_sha256: d1262a817775335b95bf149194a3c460b22c0b5d4f19de6e9134275eea5e7333
  search_scope: Saved original local inventory only; exact bindingdb_targets predicate
    exact complete standard_inchi_key equality; query value "FSKFLBQJBSQQKA-DMZCBJAKSA-N".
    All matched rows or the complete empty result are retained. No replay or external
    search.
- evidence_id: bgc-2401-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 positive placements,
    exact predicate/query and all fields. A blank AID would be a sentinel, not an
    assay; none occurs in these selected contexts.'
  snapshot_sha256: d1262a817775335b95bf149194a3c460b22c0b5d4f19de6e9134275eea5e7333
  search_scope: Saved original local inventory only; exact antibioticmech_inchikeys
    predicate exact complete standard_inchi_key equality; query value "FSKFLBQJBSQQKA-DMZCBJAKSA-N".
    All matched rows or the complete empty result are retained. No replay or external
    search.
- evidence_id: bgc-2401-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch241-tentative/bgc-prep/bgc-conditional241-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: 'Complete saved chebi_origins frame: 1 positive placements, exact predicate/query
    and all fields. A blank AID would be a sentinel, not an assay; none occurs in
    these selected contexts.'
  snapshot_sha256: d1262a817775335b95bf149194a3c460b22c0b5d4f19de6e9134275eea5e7333
  search_scope: Saved original local inventory only; exact chebi_origins predicate
    exact chebi_id from exact full-key structure rows; query value ["CHEBI:169999"].
    All matched rows or the complete empty result are retained. No replay or external
    search.
- evidence_id: bgc-2401-source-chebi_origins
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Header line1; physical lines17249–17249; row_sha256 4611f7dc3eedb266a35bbb3595295a0ffb902e8f227b363a08fe0ae3d8625869
  accessed_at: '2026-11-04T14:03:16.862789Z'
  support: supports
  summary: Complete ChEBI source taxon, strain/detection-context, comment and citation
    fields; no automatic producer assignment. BGC complete selected source-row reading
    carries.
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-241/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-241/native-current241-five-gates-execution-001.json
  accessed_at: '2026-11-04T13:32:58.346537Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: ea95a2cf0dd388820427ff3be1b6c830609ded88a41b10ec14b90419ace4af5b
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-241/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-241/native-current241-five-gates-execution-001.json
  accessed_at: '2026-11-04T13:33:23.041545Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: eb9c86f5848e609ae12e4c38e7c9cf87600ca731a97f491c88e93b1a489ef103
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-241/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-241/native-current241-five-gates-execution-001.json
  accessed_at: '2026-11-04T13:33:42.433969Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-241/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-241/native-current241-five-gates-execution-001.json
  accessed_at: '2026-11-04T13:34:16.496577Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-241/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-241/native-current241-five-gates-execution-001.json
  accessed_at: '2026-11-04T13:34:28.193393Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 2dd2f2bb2b57a0f3ce268c7c2c96ec9a3150f75c0b4c3a3d4c8c5f4ba7569da8
assessments:
- assessment_id: bgc-2401-identity
  area: identity
  topic: Retained identity/form consistency; natural identity unverified
  outcome: supported
  summary: The retained CHEBI:169999 identifier is grounded by the complete key FSKFLBQJBSQQKA-DMZCBJAKSA-N
    shared by the saved MIBiG and three-star ChEBI rows. MIBiG supplies the structure;
    ChEBI supplies the definition and exact concept join, while NPA032764 is a cross-reference.
    Both original forms normalize to this key and C25H38O2. This supports retained
    identity/form consistency, not independently verified natural identity or the
    truth of every database definition.
  target_ids:
  - CHEBI:169999
  evidence_ids:
  - bgc-2401-grounding-owner
  - bgc-2401-chemistry
  - bgc-2401-source-mibig_compounds
  - bgc-2401-source-chebi_structures
  - bgc-2401-query-chebi_structures
  - bgc-2401-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: FSKFLBQJBSQQKA-DMZCBJAKSA-N; exact retained complete key, not independent
      natural identity.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2401-grounding-owner
    - bgc-2401-chemistry
    - bgc-2401-source-mibig_compounds
    - bgc-2401-source-chebi_structures
    - bgc-2401-query-chebi_structures
    - bgc-2401-direct-contexts
  - name: grounding_scope
    value: The retained CHEBI:169999 identifier is grounded by the complete key FSKFLBQJBSQQKA-DMZCBJAKSA-N
      shared by the saved MIBiG and three-star ChEBI rows. MIBiG supplies the structure;
      ChEBI supplies the definition and exact concept join, while NPA032764 is a cross-reference.
      Both original forms normalize to this key and C25H38O2. This supports retained
      identity/form consistency, not independently verified natural identity or the
      truth of every database definition.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2401-grounding-owner
    - bgc-2401-chemistry
    - bgc-2401-source-mibig_compounds
    - bgc-2401-source-chebi_structures
    - bgc-2401-query-chebi_structures
    - bgc-2401-direct-contexts
- assessment_id: bgc-2401-representation
  area: representation
  topic: Original stored-form and stereochemical scope
  outcome: supported
  summary: Both forms are neutral C25H38O2 with 27 heavy atoms and 29 bonds, five
    specified tetrahedral centers, and two specified double bonds. Saved SMILES bond
    14 is Z and bond 21 is E; those are diagnostic indices, not chemical locants.
    All ten comparison flags are true and the original atom match covers 27 atoms,
    while full_graph_identity_established remains false. The retained true stereo
    flag is a source encoding assertion, not fresh stereochemical proof.
  target_ids:
  - CHEBI:169999
  evidence_ids:
  - bgc-2401-grounding-owner
  - bgc-2401-chemistry
  - bgc-2401-topology
  - bgc-2401-diagnostic-reading
  - bgc-2401-diagnostic-acceptance
  - bgc-2401-structure-schema
  - bgc-2401-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both forms are neutral C25H38O2 with 27 heavy atoms and 29 bonds, five
      specified tetrahedral centers, and two specified double bonds. Saved SMILES
      bond 14 is Z and bond 21 is E; those are diagnostic indices, not chemical locants.
      All ten comparison flags are true and the original atom match covers 27 atoms,
      while full_graph_identity_established remains false. The retained true stereo
      flag is a source encoding assertion, not fresh stereochemical proof.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2401-grounding-owner
    - bgc-2401-chemistry
    - bgc-2401-topology
    - bgc-2401-diagnostic-reading
    - bgc-2401-diagnostic-acceptance
    - bgc-2401-structure-schema
    - bgc-2401-stereo-method
  - name: representation_correspondence
    value: All ten original flags are true and the supplied chirality-aware match
      covers the atom count. full_graph_identity_established remains false; no natural-form
      identity or new full-graph proof is claimed.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2401-grounding-owner
    - bgc-2401-chemistry
    - bgc-2401-topology
    - bgc-2401-diagnostic-reading
    - bgc-2401-diagnostic-acceptance
    - bgc-2401-structure-schema
    - bgc-2401-stereo-method
- assessment_id: bgc-2401-provenance
  area: provenance
  topic: Separate source producer, locus and taxonomic scopes
  outcome: supported
  summary: BGC0002610 v3 compound 1 names Aspergillus stellatus NCBITaxon:1549217
    as SOURCE_ASSERTION; its LC073704.1:101–6568 locus remains CLUSTER_UNSTATED with
    no evidence methods supplied. The ChEBI definition says Emericella variecolor,
    and the saved ChEBI origin note says it is another name for the recorded species.
    This is retained source attribution, not a fresh nomenclatural reconciliation
    or strain identity proof. The ignored-inclusive implemented-curation scan found
    no applicable correction.
  target_ids:
  - CHEBI:169999
  evidence_ids:
  - bgc-2401-origin-owner
  - bgc-2401-grounding-owner
  - bgc-2401-occurrence-owner
  - bgc-2401-source-mibig_compounds
  - bgc-2401-source-chebi_origins
  - bgc-2401-cached-taxonomy
  - bgc-2401-curation-scope
  - bgc-2401-direct-contexts
  dimensions:
  - name: taxon_scope
    value: BGC0002610 v3 compound 1 names Aspergillus stellatus NCBITaxon:1549217
      as SOURCE_ASSERTION; its LC073704.1:101–6568 locus remains CLUSTER_UNSTATED
      with no evidence methods supplied. The ChEBI definition says Emericella variecolor,
      and the saved ChEBI origin note says it is another name for the recorded species.
      This is retained source attribution, not a fresh nomenclatural reconciliation
      or strain identity proof. The ignored-inclusive implemented-curation scan found
      no applicable correction.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2401-origin-owner
    - bgc-2401-grounding-owner
    - bgc-2401-occurrence-owner
    - bgc-2401-source-mibig_compounds
    - bgc-2401-source-chebi_origins
    - bgc-2401-cached-taxonomy
    - bgc-2401-curation-scope
    - bgc-2401-direct-contexts
  - name: producer_evidence
    value: BGC0002610 v3 compound 1 names Aspergillus stellatus NCBITaxon:1549217
      as SOURCE_ASSERTION; its LC073704.1:101–6568 locus remains CLUSTER_UNSTATED
      with no evidence methods supplied. The ChEBI definition says Emericella variecolor,
      and the saved ChEBI origin note says it is another name for the recorded species.
      This is retained source attribution, not a fresh nomenclatural reconciliation
      or strain identity proof. The ignored-inclusive implemented-curation scan found
      no applicable correction.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2401-origin-owner
    - bgc-2401-grounding-owner
    - bgc-2401-occurrence-owner
    - bgc-2401-source-mibig_compounds
    - bgc-2401-source-chebi_origins
    - bgc-2401-cached-taxonomy
    - bgc-2401-curation-scope
    - bgc-2401-direct-contexts
  - name: locus_evidence
    value: BGC0002610 v3 compound 1 names Aspergillus stellatus NCBITaxon:1549217
      as SOURCE_ASSERTION; its LC073704.1:101–6568 locus remains CLUSTER_UNSTATED
      with no evidence methods supplied. The ChEBI definition says Emericella variecolor,
      and the saved ChEBI origin note says it is another name for the recorded species.
      This is retained source attribution, not a fresh nomenclatural reconciliation
      or strain identity proof. The ignored-inclusive implemented-curation scan found
      no applicable correction.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2401-origin-owner
    - bgc-2401-grounding-owner
    - bgc-2401-occurrence-owner
    - bgc-2401-source-mibig_compounds
    - bgc-2401-source-chebi_origins
    - bgc-2401-cached-taxonomy
    - bgc-2401-curation-scope
    - bgc-2401-direct-contexts
- assessment_id: bgc-2401-citations
  area: evidence
  topic: Citation roles and retained source attribution
  outcome: supported
  summary: PMID:26351860 is the MIBiG entry-level reference repeated on producer and
    locus. The two LOTUS DOI placements and ChEBI origin PMID:15612624 have occurrence
    roles; ChEBI:169999 is the definition source. Repetition and co-occurrence of
    these citations do not demonstrate independent experiments. No primary article
    was freshly read or verified.
  target_ids:
  - CHEBI:169999
  evidence_ids:
  - bgc-2401-origin-owner
  - bgc-2401-grounding-owner
  - bgc-2401-occurrence-owner
  - bgc-2401-source-mibig_compounds
  - bgc-2401-source-chebi_structures
  - bgc-2401-source-lotus_occurrences
  - bgc-2401-source-chebi_origins
  - bgc-2401-source-reading
  dimensions:
  - name: citation_scope
    value: PMID:26351860 is the MIBiG entry-level reference repeated on producer and
      locus. The two LOTUS DOI placements and ChEBI origin PMID:15612624 have occurrence
      roles; ChEBI:169999 is the definition source. Repetition and co-occurrence of
      these citations do not demonstrate independent experiments. No primary article
      was freshly read or verified.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2401-origin-owner
    - bgc-2401-grounding-owner
    - bgc-2401-occurrence-owner
    - bgc-2401-source-mibig_compounds
    - bgc-2401-source-chebi_structures
    - bgc-2401-source-lotus_occurrences
    - bgc-2401-source-chebi_origins
    - bgc-2401-source-reading
- assessment_id: bgc-2401-occurrence
  area: evidence
  topic: Bounded occurrence and assay/target evidence
  outcome: supported
  summary: 'The owner has three occurrence placements: two LOTUS assertions and one
    ChEBI origin, all under NCBITaxon:1549217. The two LOTUS DOIs remain separate
    source assertions, while the ChEBI origin includes the Emericella variecolor naming
    note. Neither matching the producer taxon nor repeated citation placement upgrades
    occurrence to experimentally established production. Saved occurrence queries
    are bounded to the retained exact-key/source joins.'
  target_ids:
  - CHEBI:169999
  evidence_ids:
  - bgc-2401-occurrence-owner
  - bgc-2401-source-lotus_occurrences
  - bgc-2401-source-chebi_origins
  - bgc-2401-query-lotus_occurrences
  - bgc-2401-query-chebi_origins
  - bgc-2401-query-cyanometdb_occurrences
  - bgc-2401-query-pubchem_bioassay
  - bgc-2401-query-bindingdb_targets
  - bgc-2401-cached-taxonomy
  - bgc-2401-taxonomy-reading
  - bgc-2401-curation-scope
  - bgc-2401-mechanism-absence
  dimensions:
  - name: occurrence_scope
    value: 'The owner has three occurrence placements: two LOTUS assertions and one
      ChEBI origin, all under NCBITaxon:1549217. The two LOTUS DOIs remain separate
      source assertions, while the ChEBI origin includes the Emericella variecolor
      naming note. Neither matching the producer taxon nor repeated citation placement
      upgrades occurrence to experimentally established production. Saved occurrence
      queries are bounded to the retained exact-key/source joins.'
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2401-occurrence-owner
    - bgc-2401-source-lotus_occurrences
    - bgc-2401-source-chebi_origins
    - bgc-2401-query-lotus_occurrences
    - bgc-2401-query-chebi_origins
    - bgc-2401-query-cyanometdb_occurrences
    - bgc-2401-query-pubchem_bioassay
    - bgc-2401-query-bindingdb_targets
    - bgc-2401-cached-taxonomy
    - bgc-2401-taxonomy-reading
    - bgc-2401-curation-scope
    - bgc-2401-mechanism-absence
  - name: assay_target_scope
    value: Bioactivities, bioactivity_summary and molecular_targets are absent in
      the complete owner; the saved PubChem and BindingDB joins are empty. This bounded
      absence does not establish inactivity or absence of all published assays.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2401-occurrence-owner
    - bgc-2401-source-lotus_occurrences
    - bgc-2401-source-chebi_origins
    - bgc-2401-query-lotus_occurrences
    - bgc-2401-query-chebi_origins
    - bgc-2401-query-cyanometdb_occurrences
    - bgc-2401-query-pubchem_bioassay
    - bgc-2401-query-bindingdb_targets
    - bgc-2401-cached-taxonomy
    - bgc-2401-taxonomy-reading
    - bgc-2401-curation-scope
    - bgc-2401-mechanism-absence
- assessment_id: bgc-2401-classification
  area: consistency
  topic: Versioned model fidelity and bounded applicability
  outcome: concern
  summary: NPClassifier npclassifier.gnps2.org@2026-09-07 is faithfully retained as
    Terpenoids/Diterpenoids/Valparane diterpenoids with is_glycoside:false. The retained
    ChEBI definition instead calls the C25 compound a sesterterpenoid. This is a bounded
    model-applicability concern, not evidence that the prediction was ingested incorrectly.
    C25 and the local ring pattern alone do not adjudicate the model class; its fine
    applicability remains unresolved. No separate sugar is shown by the saved topology.
  target_ids:
  - CHEBI:169999
  evidence_ids:
  - bgc-2401-classification-owner
  - bgc-2401-grounding-owner
  - bgc-2401-source-npclassifier
  - bgc-2401-chemistry
  - bgc-2401-topology
  - bgc-2401-structure-schema
  - bgc-2401-classification-seeder
  dimensions:
  - name: classification_applicability
    value: NPClassifier npclassifier.gnps2.org@2026-09-07 is faithfully retained as
      Terpenoids/Diterpenoids/Valparane diterpenoids with is_glycoside:false. The
      retained ChEBI definition instead calls the C25 compound a sesterterpenoid.
      This is a bounded model-applicability concern, not evidence that the prediction
      was ingested incorrectly. C25 and the local ring pattern alone do not adjudicate
      the model class; its fine applicability remains unresolved. No separate sugar
      is shown by the saved topology.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2401-classification-owner
    - bgc-2401-grounding-owner
    - bgc-2401-source-npclassifier
    - bgc-2401-chemistry
    - bgc-2401-topology
    - bgc-2401-structure-schema
    - bgc-2401-classification-seeder
- assessment_id: bgc-2401-completion
  area: completeness
  topic: Actual evidence coverage and remaining scientific limits
  outcome: unknown
  summary: Complete owner/history, actual canonical intake, retained source rows and
    negative query frames, and both original molecular forms have been read. All four
    mechanism roots are absent in this owner, so no maintained-mechanism reader applies.
    Full QC/OAK, fresh primary and taxonomic/assay verification, and independent natural
    identity or stereochemical authentication remain unavailable. This is a partial
    review with no supported record-edit finding.
  target_ids:
  - CHEBI:169999
  evidence_ids:
  - bgc-2401-owner
  - bgc-2401-capture
  - bgc-2401-intake
  - bgc-2401-intake-acceptance
  - bgc-2401-diagnostic-reading
  - bgc-2401-diagnostic-acceptance
  - bgc-2401-diagnostic-execution
  - bgc-2401-source-reading
  - bgc-2401-joint-source-notes
  - bgc-2401-source-plan-acceptance
  - bgc-2401-curation-scope
  - bgc-2401-mechanism-absence
  dimensions:
  - name: review_completion
    value: Complete owner/history, actual canonical intake, retained source rows and
      negative query frames, and both original molecular forms have been read. All
      four mechanism roots are absent in this owner, so no maintained-mechanism reader
      applies. Full QC/OAK, fresh primary and taxonomic/assay verification, and independent
      natural identity or stereochemical authentication remain unavailable. This is
      a partial review with no supported record-edit finding.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2401-owner
    - bgc-2401-capture
    - bgc-2401-intake
    - bgc-2401-intake-acceptance
    - bgc-2401-diagnostic-reading
    - bgc-2401-diagnostic-acceptance
    - bgc-2401-diagnostic-execution
    - bgc-2401-source-reading
    - bgc-2401-joint-source-notes
    - bgc-2401-source-plan-acceptance
    - bgc-2401-curation-scope
    - bgc-2401-mechanism-absence
findings: []
actions: []
limitations:
- 'Retained local evidence only: no fresh primary literature, taxonomy, assay protocol,
  natural-identity or experimental-stereochemistry verification.'
- Full QC and complete OAK coverage remain unavailable. Local normalization, motifs
  and one atom match do not establish independent full-graph or natural-form identity.
- Producer, locus, occurrence, strain/detection context and citation roles remain
  distinct; congeners and repeated references do not transfer product claims or experimental
  independence.
- Model values are retained with provenance. Fine applicability concerns do not establish
  a source-ingestion error or justify a replacement.
- The complete owner has no graph/pathway/component/target roots. No maintained-mechanism
  check is claimed for this record; no source status/history edit is proposed.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'BGC personally read all ten first-five forms: 258 atom rows and 278 bond rows,
  all scalar/ring/stereo/motif/map fields. Diagnostic atom/bond indices are zero-based,
  not biochemical locants. Original stderr is empty.'
- 'Source meanings remain disjoint: BGC eight contexts/41 rows/414 fields/72 frames;
  Support nine contexts/48 rows/485 fields/81 frames. Native owns all 14 cached stanzas
  and the bounded ignored-inclusive curation scan; BGC additionally read the eleven
  first-five unique cached stanzas. Prior complete companion raw/history carries remain
  attributed.'
- BGC operated the admitted source collector and composer. ROOT operated the actual
  canonical intakes and original diagnostic. These five owners have no maintained-reader
  call; no runtime is launched by authoring.
- All scientific outcomes are partial, with no supported finding or action. Missing
  fresh verification, model concern or diagnostic success alone is not a record-edit
  finding.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-241
```
