# Local evidence review: eupenifeldin

- Review: 20261106T032248Z-eupenifeldin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T02:22:01.325156Z
- Finished UTC: 2026-11-06T03:22:48.039985Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Eupenifeldin retains a consistent normalized formula and full key while its two stored-form reconstructions differ in carbonyl/hydroxyl placement across oxygenated rings. Five unresolved tetrahedral centers remain explicit. Its MIBiG producer and locus, LOTUS occurrence and computed meroterpenoid family are kept at their recorded evidence grades; no actual assay result is present in the retained join.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2643; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-d7152699ce | data/natural_products/unclassified/eupenifeldin.yaml | generated | eupenifeldin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-d7152699ce | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-d7152699ce | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-d7152699ce | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-d7152699ce | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-d7152699ce | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-d7152699ce | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-d7152699ce | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-d7152699ce | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### identity

identity: supported. Targets: naturalproductmech:mibig-d7152699ce.

Both saved forms regenerate BWTQHPFSWXJOGP-BQYQJAHWSA-N, C33H40O7 and net charge 0, agreeing with the MINTED BGC0001976 compound record. Both canonical comparisons are false and the atom match is empty. Normalized consistency therefore supports the retained encoded identity only within that resolution; it does not prove complete graph correspondence or natural-material identity.

### representation

representation: supported. Targets: naturalproductmech:mibig-d7152699ce.

Each form contains 40 atoms, 44 bonds and five returned rings of sizes 7, 6, 11, 6 and 7. The two conjugated oxygenated seven-member rings, two cyclic ether connections, two carbonyls and three hydroxyls are retained. Canonical strings move adjacent carbonyl/hydroxyl assignments within both oxygenated rings, consistent with the two literal mobile-H groups in the stored InChI. This is a bounded carbonyl/enol representation difference, not amide normalization: the structure contains no nitrogen or amide. Five unspecified tetrahedral centers and one E alkene persist in both forms; the false atom-centered completeness flag is preserved.

### provenance

provenance: unknown. Targets: naturalproductmech:mibig-d7152699ce.

Active BGC0001976 version 3 retains questionable quality and unknown completeness. Phoma sp. NCBITaxon:1707701 is SOURCE_ASSERTION and MK400120.1 is CLUSTER_UNSTATED without a retained method or bounded locus. The raw class terpene and subclass Unknown remain separate. A genus-level Phoma occurrence is not strain-specific biosynthetic support.

### citations

evidence: unknown. Targets: naturalproductmech:mibig-d7152699ce.

PMID:30980906 is retained at ENTRY grain. The LOTUS occurrence cites DOI:10.1016/J.FGB.2019.04.004. Neither reference was newly opened, and their overlap in subject matter is not independent experimental confirmation. Database IDs remain recorded source links without new identity validation.

### occurrence_activity

evidence: unknown. Targets: naturalproductmech:mibig-d7152699ce.

One LOTUS row records Phoma NCBITaxon:37463, distinct from the producer identifier 1707701. The PubChem join returns a blank-AID sentinel rather than an experimental result. No actual AID, quantified activity or molecular target is established in this retained scope; the negative frames do not establish inactivity.

### classification

consistency: unknown. Targets: naturalproductmech:mibig-d7152699ce.

The conjugated oxygenated rings and mixed polycyclic framework are compatible with the broad Meroterpenoids interpretation. NPClassifier reports Polyketides, Terpenoids and Tetraketide meroterpenoids, with is_glycoside false. Exact tetraketide origin and model-family applicability are not established by the local topology or the ungraded source locus alone.

### completion

completeness: unknown. Targets: naturalproductmech:mibig-d7152699ce.

The complete owner and history, scoped retained source payloads, both full saved molecular forms, and 44 actual input hashes and ownership declarations were reviewed. The accepted plan and intakes contain 458 input placements across 69 paths. Five local gates passed; full QC, OAK and fresh external authority remain unavailable. No mechanism or declared-component root is present in this owner, so no maintained reader applies. Completion remains partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2643-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/eupenifeldin.yaml; Complete plaintext including every curation_history entry | supports | Complete current owner and all 2 history entries were personally read. Historical curator assertions do not confer fresh source-access credit. |
| bgc-2643-capture | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/2 | supports | Actual complete owner capture preserves current local content; it is not an independent scientific validation. |
| bgc-2643-identity | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/2/owner_document/identifier; /records/2/owner_document/label; /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status | supports | Exact stored identity, source concepts, grounding and chemical encodings; natural identity is assessed separately. |
| bgc-2643-history | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/2/owner_document/curation_history | supports | All 2 current history entries retain their original source and curation scope; no inherited paper access is claimed. |
| bgc-2643-provenance | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/source_concepts | supports | Owner-specific producer, locus and source-concept assertions preserve their distinct grades and references. |
| bgc-2643-activity-owner | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/2/owner_document/occurrences; /records/2/owner_document/xrefs | supports | The selected occurrence, activity (when present) and cross-reference fields retain their distinct claim scopes. Occurrence or a cross-reference does not establish production, activity or mechanism. |
| bgc-2643-classification-owner | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/2/owner_document/np_pathway; /records/2/owner_document/biosynthesis_origin; /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class | supports | Recorded classification/model labels and BGC class content; exact source subclasses remain separately visible in the retained MIBiG row. |
| bgc-2643-mechanism-scope | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/2/owner_document | context_only | This complete captured owner has no causal_graphs, biosynthetic_pathway or declared-component root; there is no applicable maintained-reader result. |
| bgc-2643-intake | /private/tmp/npm-review-work/shared-next-batch265/intakes-001/2643-inspect-001.json; /targets; /source | supports | Actual canonical inspection captures 44 current input hashes and complete target ownership declarations. Hash capture does not imply whole scientific reading of each input table. |
| bgc-2643-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch265/root-intakes-acceptance-001.json; /accepted; /status; /summary | supports | ROOT accepted the ten actual canonical inspections and their exact 458-input/69-path scope. |
| bgc-2643-plan | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-target-input-plan-001.json; /records/2; /source_placement_count; /unique_source_path_count | supports | This owner has 44 exact planned inputs, now matched to its accepted actual canonical inspection; the full plan has 458 placements/69 paths. |
| bgc-2643-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch265/root-source-plan-acceptance-001.json; /accepted; /status; /plan | supports | ROOT accepted the original local composed input plan; all current input paths and roles are preserved. |
| bgc-2643-chemistry | /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-DATA-001.json; /records/2 | supports | Both complete saved forms, all atom/bond/ring/motif/stereo fields, comparisons and limited atom correspondence were personally read. No alternative parse was performed. |
| bgc-2643-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /status; /DATA; /execution | supports | ROOT accepted the once-only offline diagnostic execution and saved outputs; this does not establish natural identity or full graph equivalence. |
| bgc-2643-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-execution-001.json; /exit_code; /stdout; /stderr | supports | Actual diagnostic execution closed with exit 0 and preserved original stdout/stderr; no diagnostic replay was made. |
| bgc-2643-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-original-001.stderr; Complete original stderr | context_only | The original diagnostic stderr contains four undefined-stereo warning blocks. They remain global and are not attributed to a particular owner or stored form. |
| bgc-2643-molecular-reading | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-current265-first-five-molecular-intake-reading-001.json; /records/2; /reading_attribution; /limitations | supports | Owner-specific complete saved-table reading and interpretation, with normalized identifiers distinguished from canonical correspondence and natural identity. |
| bgc-2643-gates | /private/tmp/npm-review-work/shared-next-batch265/root-native-gates-acceptance-001.json; /checks_passed; /all_native_gates_passed; /unavailable_required_gates; /complete_selected_queue_rows | supports | Five local checks passed. Full QC and OAK remain unavailable, so native completion and scientific completion are not promoted. |
| bgc-2643-source-reading | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-current265-assigned-source-reading-001.json; /records/3; /full_meaning_scope; /boundaries | supports | Assigned retained-row meanings and all query metadata for this owner were read. References remain retained database assertions rather than newly inspected primary papers. |
| bgc-2643-source-notes | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /reading_boundaries | supports | Original 458-input/69-path source notes preserve disjoint positive-row reading credit 187 BGC + 38 Support + 0 Native. Actual intake acceptance is supported separately. |
| bgc-2643-taxonomy | /private/tmp/npm-review-work/shared-next-batch265-tentative/native-prep/native-current265-cached-taxonomy-reading-001.json; /context_interpretations/4; /interpretation | partial | Owner-local retained taxonomy routes, names and synonyms, with no current rank, lineage or freshness verification. |
| bgc-2643-curation | /private/tmp/npm-review-work/shared-next-batch265-tentative/native-prep/native-current265-implemented-curation-scan-001.json; /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope; /interpretation | context_only | Ignored-inclusive retained curation scope found no exact applicable correction. The producer-strain and row-digest implementation readings retain their bounded scope. |
| bgc-2643-assay-curation | /private/tmp/npm-review-work/shared-next-batch265-tentative/native-prep/native-current265-implemented-curation-scan-001.json; /assay_scope | context_only | The receipt-wide scan retains 118 actual assay rows, 112 exact tuples and five blank sentinels. Six tuple pairs differ in target-accession content; all row placements remain. The 117 Epothilone rows and one Equisetin row have no exact applicable exclusion. Same-AID decisions with other full keys or CIDs are not transferred. |
| bgc-2643-stereo-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392-396: stereo_complete description | context_only | The maintained flag describes undefined stereocentres; it does not by itself establish full double-bond geometric resolution. |
| bgc-2643-stereo-extractor | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters and undefined-tag predicate | context_only | The maintained extractor computes stereo_complete from unassigned tetrahedral chiral-centre tags. No extractor or molecule was rerun for this reading. |
| bgc-2643-stereo-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; line 995: direct stereo_complete copy | context_only | The maintained seeder copies the retained atom-centred boolean without independently resolving geometric stereochemistry. |
| bgc-2643-stereo-policy | /private/tmp/npm-record-reviews-20261021/docs/HARMONIZATION.md; lines 99-104: stereochemical completeness | context_only | The documented retained stereocentre scope is separated from unknown original bond geometry and reconstruction-derived imine descriptors. |
| bgc-2643-delegated-context-reading | /private/tmp/npm-review-work/shared-next-batch265-tentative/support-prep/support-current265-assigned-source-reading-001.json; /contexts | context_only | Support personally read the six complementary contexts, including the five last-half owners and Griseoviridin. This preserves attribution without adding BGC primary source-row credit or transferring activity between owners. |
| bgc-2643-direct-contexts | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-target-input-plan-001.json; /records/2/proposed_companion_paths; /records/2/direct_companion_predicates | context_only | This owner has 0 immediate shared-BGC context input(s); the exact predicates do not establish equivalent identity, independent experimental evidence or source transfer. |
| bgc-2643-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2643-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 2282-2282; raw record sha256 6b68952184669ca825c36d6cb59ae7aff7b3ca01018e343e3bbdbbd45c86d6b6 | supports | Assigned retained-row reading of all 25 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2643-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2643-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2643-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 605-605; raw record sha256 4e7853ee374a48a1cc65bb1c1fcd698dec9f0250c2fb285694081174066c7194 | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2643-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2643-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2643-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 237-237; raw record sha256 d388361350cef22e4994af7925c6becf17460c38ba996f4cea8a71b9194bbdad | supports | Assigned retained-row reading of all 7 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2643-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2643-row-pubchem_bioassay-0 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 867-867; raw record sha256 4dd773351d53226649917a2697fd14fdfa0fdf792afa04da9c9c24dde1ca8ec5 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2643-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2643-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2643-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2643-additional-0 | /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained exclusion-table diagnostic context captured for every review; applicable exact assay exclusions and biological rows must be derived from actual retained inventory, not file presence.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2643-additional-1 | /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained unresolved-taxon diagnostic context used by the bounded curation scan; no fresh taxonomy, forward-merge decision or producer confirmation.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2643-additional-2 | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained explicit forward-merge table used by positive and negative taxon queries for each owner; historical route evidence only, no fresh taxonomy.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2643-additional-3 | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_non_organism.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained non-organism table used by positive and negative taxon queries for each owner; diagnostic scope only, not a taxon verdict from file presence.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2643-additional-4 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Maintained exclusion identity, source-row digest and attributed-rationale implementation context; no execution or new assay evidence.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2643-additional-5 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/producer_strains.py; load_producer_strains lines 12-17; _load_qualifications lines 28-62; qualify_producer lines 65-68; _append_evidence lines 78-89 | context_only | Captured additional input role: Maintained producer-strain qualification implementation: source-row and digest predicate, strain-only CURATOR_INFERENCE scope; plaintext dependency, no execution or grade/taxon upgrade.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2643-additional-6 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py; row_digest lines 19-23 only | context_only | Captured additional input role: Maintained row_digest implementation used by qualification guards: sorted ensure_ascii JSON digest only; input presence does not claim an audit or application of other structure-correction behavior.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-265/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-265/native-current265-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-265/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-265/native-current265-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-265/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-265/native-current265-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-265/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-265/native-current265-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-265/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-265/native-current265-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Both stored forms were read completely from the accepted saved diagnostic without reparsing. Normalized identifier, formula and charge agreement does not establish complete graph correspondence or natural identity.
- The diagnostic attempts a limited chirality-aware substructure match. Its full_graph_identity_established flag remains false, including when a complete one-way atom match is present.
- Four undefined-stereo warning blocks belong to the original global stderr and are not attributed to a particular owner or form.
- Retained source dictionaries, database references and historical curator annotations were read locally. No primary publication, sequence, coordinate model, live taxonomy authority or external database was newly accessed.
- Cached taxonomy supplies IDs, retained names and synonyms without independently verified rank, lineage or freshness. Occurrence does not establish production.
- All captured input hashes and ownership declarations were verified; source payloads were read within the recorded query scope. This is not a claim to have scientifically read every row of every input table.
- Five local gates passed, but full QC and OAK remain unavailable. Scientific and overall completion remain partial.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- No amide/imidic interpretation is applied to this nitrogen-free structure.
- The positional representation difference is retained without prescribing an unsupported replacement structure.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T032248Z-eupenifeldin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: eupenifeldin'
started_at: '2026-11-06T02:22:01.325156Z'
finished_at: '2026-11-06T03:22:48.039985Z'
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
summary: Eupenifeldin retains a consistent normalized formula and full key while its
  two stored-form reconstructions differ in carbonyl/hydroxyl placement across oxygenated
  rings. Five unresolved tetrahedral centers remain explicit. Its MIBiG producer and
  locus, LOTUS occurrence and computed meroterpenoid family are kept at their recorded
  evidence grades; no actual assay result is present in the retained join.
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
  - path: data/natural_products/unclassified/eupenifeldin.yaml
    sha256: 71064197f8884e2a2320fcc12edb8c174ac3ec013d776a0a1bd9724a55a5b2a3
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
  selection: Campaign path order 2643; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-d7152699ce
targets:
- target_id: naturalproductmech:mibig-d7152699ce
  path: data/natural_products/unclassified/eupenifeldin.yaml
  label: eupenifeldin
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
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-d7152699ce
  command: just validate-strict data/natural_products/unclassified/epothilone-b.yaml
    data/natural_products/unclassified/equisetin.yaml data/natural_products/unclassified/eupenifeldin.yaml
    data/natural_products/unclassified/fa2097.yaml data/natural_products/unclassified/fengycin.yaml
    data/natural_products/unclassified/fijimycin-a.yaml data/natural_products/unclassified/flavunoidine.yaml
    data/natural_products/unclassified/fluvirucin-b2.yaml data/natural_products/unclassified/fosfomycin.yaml
    data/natural_products/unclassified/fr-900098.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-265/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-d7152699ce
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-265/validate-all-001.tsv
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
  - naturalproductmech:mibig-d7152699ce
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
  - naturalproductmech:mibig-d7152699ce
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
  - naturalproductmech:mibig-d7152699ce
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-265/review-queue-001.tsv
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
  - naturalproductmech:mibig-d7152699ce
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-d7152699ce
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-d7152699ce
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2643-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/eupenifeldin.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Complete current owner and all 2 history entries were personally read.
    Historical curator assertions do not confer fresh source-access credit.
  snapshot_sha256: 71064197f8884e2a2320fcc12edb8c174ac3ec013d776a0a1bd9724a55a5b2a3
- evidence_id: bgc-2643-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/2
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Actual complete owner capture preserves current local content; it is not
    an independent scientific validation.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2643-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/2/owner_document/identifier; /records/2/owner_document/label;
    /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts;
    /records/2/owner_document/grounding_status
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Exact stored identity, source concepts, grounding and chemical encodings;
    natural identity is assessed separately.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2643-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/2/owner_document/curation_history
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: All 2 current history entries retain their original source and curation
    scope; no inherited paper access is claimed.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2643-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters;
    /records/2/owner_document/source_concepts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Owner-specific producer, locus and source-concept assertions preserve their
    distinct grades and references.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2643-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/2/owner_document/occurrences; /records/2/owner_document/xrefs
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: The selected occurrence, activity (when present) and cross-reference fields
    retain their distinct claim scopes. Occurrence or a cross-reference does not establish
    production, activity or mechanism.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2643-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_pathway; /records/2/owner_document/biosynthesis_origin;
    /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Recorded classification/model labels and BGC class content; exact source
    subclasses remain separately visible in the retained MIBiG row.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2643-mechanism-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: This complete captured owner has no causal_graphs, biosynthetic_pathway
    or declared-component root; there is no applicable maintained-reader result.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
  search_scope: Exact literal root-presence inspection of this complete captured owner
    only; no molecular mechanism or biological absence inference.
- evidence_id: bgc-2643-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/intakes-001/2643-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Actual canonical inspection captures 44 current input hashes and complete
    target ownership declarations. Hash capture does not imply whole scientific reading
    of each input table.
  snapshot_sha256: 7aec826116b8ae29ea78f66bce602763010af7f49674d19b5687f82d2f8b422b
- evidence_id: bgc-2643-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/root-intakes-acceptance-001.json
  locator: /accepted; /status; /summary
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: ROOT accepted the ten actual canonical inspections and their exact 458-input/69-path
    scope.
  snapshot_sha256: d9bfdc9fd488493604bd3b14e5b1ba99ce90cbb7c036b512cd67adb816b15a94
- evidence_id: bgc-2643-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-target-input-plan-001.json
  locator: /records/2; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: This owner has 44 exact planned inputs, now matched to its accepted actual
    canonical inspection; the full plan has 458 placements/69 paths.
  snapshot_sha256: 6c1c8151bfe6e5429970a5172b60f081cd00e0db37b52fe2f03baf22da2e3301
- evidence_id: bgc-2643-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/root-source-plan-acceptance-001.json
  locator: /accepted; /status; /plan
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: ROOT accepted the original local composed input plan; all current input
    paths and roles are preserved.
  snapshot_sha256: 8cba825369eb66a55a9be750e7a84ac29007c062f18d9631c4dc4a54094e2814
- evidence_id: bgc-2643-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Both complete saved forms, all atom/bond/ring/motif/stereo fields, comparisons
    and limited atom correspondence were personally read. No alternative parse was
    performed.
  snapshot_sha256: 58e6b7a2976ba940a3ac602a014f525360bc5c513c295bbfda1a597362dfb49c
- evidence_id: bgc-2643-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /status; /DATA; /execution
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: ROOT accepted the once-only offline diagnostic execution and saved outputs;
    this does not establish natural identity or full graph equivalence.
  snapshot_sha256: 2e9621e8613270d0e133b65ff7159a7d1d60517492cfc0a265e0e97a5a584fac
- evidence_id: bgc-2643-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /stdout; /stderr
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Actual diagnostic execution closed with exit 0 and preserved original stdout/stderr;
    no diagnostic replay was made.
  snapshot_sha256: a0a4b065cd2af9f176555009b9c7b42efdbf6e4234ee2fe8dade850db004f357
- evidence_id: bgc-2643-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The original diagnostic stderr contains four undefined-stereo warning blocks.
    They remain global and are not attributed to a particular owner or stored form.
  snapshot_sha256: 3571c04aece6b5ad4d3aa0f3c1cfa07ce5f070eec712da8b3ab4fac64d8601d2
- evidence_id: bgc-2643-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-current265-first-five-molecular-intake-reading-001.json
  locator: /records/2; /reading_attribution; /limitations
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Owner-specific complete saved-table reading and interpretation, with normalized
    identifiers distinguished from canonical correspondence and natural identity.
  snapshot_sha256: f17c7cc533377e3d9d05b2d791ce756dccdf85f090958e62f13550a1532221dd
- evidence_id: bgc-2643-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/root-native-gates-acceptance-001.json
  locator: /checks_passed; /all_native_gates_passed; /unavailable_required_gates;
    /complete_selected_queue_rows
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Five local checks passed. Full QC and OAK remain unavailable, so native
    completion and scientific completion are not promoted.
  snapshot_sha256: 3785657c1cb4e0bb8f1fe2ba13ff7118fe0b0f937fd885ed29b3d5a128fcee55
- evidence_id: bgc-2643-source-reading
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-current265-assigned-source-reading-001.json
  locator: /records/3; /full_meaning_scope; /boundaries
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row meanings and all query metadata for this owner were
    read. References remain retained database assertions rather than newly inspected
    primary papers.
  snapshot_sha256: d93b851280e712f4f1f573637ddcfa386e6c915231bc3c1c221cc5c7c8fb04c5
- evidence_id: bgc-2643-source-notes
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Original 458-input/69-path source notes preserve disjoint positive-row
    reading credit 187 BGC + 38 Support + 0 Native. Actual intake acceptance is supported
    separately.
  snapshot_sha256: abb84f059d8a7c96b5c8ac546f5e0bffd8c82d929289b3adde72920d05cbc167
- evidence_id: bgc-2643-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/native-prep/native-current265-cached-taxonomy-reading-001.json
  locator: /context_interpretations/4; /interpretation
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: partial
  summary: Owner-local retained taxonomy routes, names and synonyms, with no current
    rank, lineage or freshness verification.
  snapshot_sha256: 84cfb0811e71455d15f59a8da5f322fdbc71fae1acf9cbec50d6741d6177efa1
- evidence_id: bgc-2643-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/native-prep/native-current265-implemented-curation-scan-001.json
  locator: /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope;
    /interpretation
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: Ignored-inclusive retained curation scope found no exact applicable correction.
    The producer-strain and row-digest implementation readings retain their bounded
    scope.
  snapshot_sha256: 979d6b01f1d716831d82199ed03d20b19e5c5aa8cb095436f3cc8e6a3eebf72b
  search_scope: Nine implemented curation/diagnostic tables among eleven enumerated;
    decisions/source_queue excluded. Exact current context predicates applied after
    broad lexical screening; no general absence claim.
- evidence_id: bgc-2643-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/native-prep/native-current265-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The receipt-wide scan retains 118 actual assay rows, 112 exact tuples and
    five blank sentinels. Six tuple pairs differ in target-accession content; all
    row placements remain. The 117 Epothilone rows and one Equisetin row have no exact
    applicable exclusion. Same-AID decisions with other full keys or CIDs are not
    transferred.
  snapshot_sha256: 979d6b01f1d716831d82199ed03d20b19e5c5aa8cb095436f3cc8e6a3eebf72b
  search_scope: All fifteen retained exclusion decisions under the implemented exact
    full-key/CID/AID/source-provenance guards; owner assay counts are recorded in
    its own saved query frame.
- evidence_id: bgc-2643-stereo-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: 'lines 392-396: stereo_complete description'
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The maintained flag describes undefined stereocentres; it does not by itself
    establish full double-bond geometric resolution.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2643-stereo-extractor
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters and undefined-tag predicate'
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The maintained extractor computes stereo_complete from unassigned tetrahedral
    chiral-centre tags. No extractor or molecule was rerun for this reading.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2643-stereo-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'line 995: direct stereo_complete copy'
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The maintained seeder copies the retained atom-centred boolean without
    independently resolving geometric stereochemistry.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2643-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/HARMONIZATION.md
  locator: 'lines 99-104: stereochemical completeness'
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The documented retained stereocentre scope is separated from unknown original
    bond geometry and reconstruction-derived imine descriptors.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: bgc-2643-delegated-context-reading
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/support-prep/support-current265-assigned-source-reading-001.json
  locator: /contexts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: Support personally read the six complementary contexts, including the five
    last-half owners and Griseoviridin. This preserves attribution without adding
    BGC primary source-row credit or transferring activity between owners.
  snapshot_sha256: 29e3c5318905a2800b1953120011a91a94fbd48e8fdc594900a114697d6a75ba
- evidence_id: bgc-2643-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-target-input-plan-001.json
  locator: /records/2/proposed_companion_paths; /records/2/direct_companion_predicates
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: This owner has 0 immediate shared-BGC context input(s); the exact predicates
    do not establish equivalent identity, independent experimental evidence or source
    transfer.
  snapshot_sha256: 6c1c8151bfe6e5429970a5172b60f081cd00e0db37b52fe2f03baf22da2e3301
- evidence_id: bgc-2643-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete saved mibig_compounds query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
- evidence_id: bgc-2643-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 2282-2282; raw record sha256 6b68952184669ca825c36d6cb59ae7aff7b3ca01018e343e3bbdbbd45c86d6b6
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 25 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2643-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Complete saved chebi_structures query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
  search_scope: '{"context_path": "data/natural_products/unclassified/eupenifeldin.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "BWTQHPFSWXJOGP-BQYQJAHWSA-N", "table": "chebi_structures"}'
- evidence_id: bgc-2643-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete saved lotus_occurrences query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
- evidence_id: bgc-2643-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 605-605; raw record sha256 4e7853ee374a48a1cc65bb1c1fcd698dec9f0250c2fb285694081174066c7194
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2643-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
  search_scope: '{"context_path": "data/natural_products/unclassified/eupenifeldin.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "BWTQHPFSWXJOGP-BQYQJAHWSA-N", "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2643-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete saved npclassifier query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
- evidence_id: bgc-2643-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 237-237; raw record sha256 d388361350cef22e4994af7925c6becf17460c38ba996f4cea8a71b9194bbdad
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 7 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2643-query-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
- evidence_id: bgc-2643-row-pubchem_bioassay-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 867-867; raw record sha256 4dd773351d53226649917a2697fd14fdfa0fdf792afa04da9c9c24dde1ca8ec5
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2643-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
  search_scope: '{"context_path": "data/natural_products/unclassified/eupenifeldin.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "BWTQHPFSWXJOGP-BQYQJAHWSA-N", "table": "bindingdb_targets"}'
- evidence_id: bgc-2643-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
  search_scope: '{"context_path": "data/natural_products/unclassified/eupenifeldin.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "BWTQHPFSWXJOGP-BQYQJAHWSA-N", "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2643-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Complete saved chebi_origins query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
  search_scope: '{"context_path": "data/natural_products/unclassified/eupenifeldin.yaml",
    "matches": 0, "predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "table": "chebi_origins"}'
- evidence_id: bgc-2643-additional-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Retained exclusion-table diagnostic context
    captured for every review; applicable exact assay exclusions and biological rows
    must be derived from actual retained inventory, not file presence.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
- evidence_id: bgc-2643-additional-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Retained unresolved-taxon diagnostic context
    used by the bounded curation scan; no fresh taxonomy, forward-merge decision or
    producer confirmation.. File presence itself confers no positive source-row, AID,
    taxon-rank or correction applicability credit.'
  snapshot_sha256: 86efbda9c09388723a4f24da35e18404032f1549a9088192fbd2020cb846fa43
- evidence_id: bgc-2643-additional-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Retained explicit forward-merge table
    used by positive and negative taxon queries for each owner; historical route evidence
    only, no fresh taxonomy.. File presence itself confers no positive source-row,
    AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
- evidence_id: bgc-2643-additional-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_non_organism.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Retained non-organism table used by positive
    and negative taxon queries for each owner; diagnostic scope only, not a taxon
    verdict from file presence.. File presence itself confers no positive source-row,
    AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: f2c1ee257bbbcb0854528196ab1f809d658c27f1c7b2036f7f71f088b52935bb
- evidence_id: bgc-2643-additional-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Maintained exclusion identity, source-row
    digest and attributed-rationale implementation context; no execution or new assay
    evidence.. File presence itself confers no positive source-row, AID, taxon-rank
    or correction applicability credit.'
  snapshot_sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
- evidence_id: bgc-2643-additional-5
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/producer_strains.py
  locator: load_producer_strains lines 12-17; _load_qualifications lines 28-62; qualify_producer
    lines 65-68; _append_evidence lines 78-89
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Maintained producer-strain qualification
    implementation: source-row and digest predicate, strain-only CURATOR_INFERENCE
    scope; plaintext dependency, no execution or grade/taxon upgrade.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
- evidence_id: bgc-2643-additional-6
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py
  locator: row_digest lines 19-23 only
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Maintained row_digest implementation used
    by qualification guards: sorted ensure_ascii JSON digest only; input presence
    does not claim an audit or application of other structure-correction behavior..
    File presence itself confers no positive source-row, AID, taxon-rank or correction
    applicability credit.'
  snapshot_sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-265/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-265/native-current265-five-gates-execution-001.json
  accessed_at: '2026-11-06T02:31:53.901344Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 626894a13ef4bada88df8165354e76053e4348115e1452b1654b4c430d9bbd38
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-265/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-265/native-current265-five-gates-execution-001.json
  accessed_at: '2026-11-06T02:32:18.460654Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: efa56307c799e5a00e7a757ca2b1ab74ce6adc13aa3990ccd8f3e5bf3bd1a5e0
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-265/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-265/native-current265-five-gates-execution-001.json
  accessed_at: '2026-11-06T02:32:37.874925Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-265/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-265/native-current265-five-gates-execution-001.json
  accessed_at: '2026-11-06T02:33:12.259720Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-265/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-265/native-current265-five-gates-execution-001.json
  accessed_at: '2026-11-06T02:33:23.989187Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: bf42fdb15fdcae3114178e0ce77d83728e4a2b81ddbdd4a4dd5fba8c47c8b0ef
assessments:
- assessment_id: bgc-2643-identity
  area: identity
  topic: identity
  outcome: supported
  summary: Both saved forms regenerate BWTQHPFSWXJOGP-BQYQJAHWSA-N, C33H40O7 and net
    charge 0, agreeing with the MINTED BGC0001976 compound record. Both canonical
    comparisons are false and the atom match is empty. Normalized consistency therefore
    supports the retained encoded identity only within that resolution; it does not
    prove complete graph correspondence or natural-material identity.
  target_ids:
  - naturalproductmech:mibig-d7152699ce
  evidence_ids:
  - bgc-2643-identity
  - bgc-2643-chemistry
  - bgc-2643-diagnostic-acceptance
  - bgc-2643-query-mibig_compounds
  - bgc-2643-query-chebi_structures
  - bgc-2643-query-antibioticmech_inchikeys
  - bgc-2643-direct-contexts
  - bgc-2643-row-mibig_compounds-0
  - bgc-2643-delegated-context-reading
  dimensions:
  - name: standard_inchi_key
    value: BWTQHPFSWXJOGP-BQYQJAHWSA-N; both normalized regenerations agree
    definition: Literal retained full key and accepted saved regeneration scope.
    evidence_ids:
    - bgc-2643-identity
    - bgc-2643-chemistry
    - bgc-2643-diagnostic-acceptance
    - bgc-2643-query-mibig_compounds
    - bgc-2643-query-chebi_structures
    - bgc-2643-query-antibioticmech_inchikeys
    - bgc-2643-direct-contexts
    - bgc-2643-row-mibig_compounds-0
    - bgc-2643-delegated-context-reading
  - name: grounding_scope
    value: MINTED naturalproductmech:mibig-d7152699ce; natural identity not independently
      established
    definition: Recorded grounding category, separated from independent natural identity.
    evidence_ids:
    - bgc-2643-identity
    - bgc-2643-chemistry
    - bgc-2643-diagnostic-acceptance
    - bgc-2643-query-mibig_compounds
    - bgc-2643-query-chebi_structures
    - bgc-2643-query-antibioticmech_inchikeys
    - bgc-2643-direct-contexts
    - bgc-2643-row-mibig_compounds-0
    - bgc-2643-delegated-context-reading
- assessment_id: bgc-2643-representation
  area: representation
  topic: representation
  outcome: supported
  summary: 'Each form contains 40 atoms, 44 bonds and five returned rings of sizes
    7, 6, 11, 6 and 7. The two conjugated oxygenated seven-member rings, two cyclic
    ether connections, two carbonyls and three hydroxyls are retained. Canonical strings
    move adjacent carbonyl/hydroxyl assignments within both oxygenated rings, consistent
    with the two literal mobile-H groups in the stored InChI. This is a bounded carbonyl/enol
    representation difference, not amide normalization: the structure contains no
    nitrogen or amide. Five unspecified tetrahedral centers and one E alkene persist
    in both forms; the false atom-centered completeness flag is preserved.'
  target_ids:
  - naturalproductmech:mibig-d7152699ce
  evidence_ids:
  - bgc-2643-identity
  - bgc-2643-chemistry
  - bgc-2643-molecular-reading
  - bgc-2643-diagnostic-acceptance
  - bgc-2643-diagnostic-stderr
  - bgc-2643-row-mibig_compounds-0
  - bgc-2643-stereo-schema
  - bgc-2643-stereo-extractor
  - bgc-2643-stereo-seeder
  - bgc-2643-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    value: 5 unspecified tetrahedra; one E alkene; stereo_complete false
    definition: Specified original centers and bond geometry, separated from reconstructed
      imine descriptors.
    evidence_ids:
    - bgc-2643-identity
    - bgc-2643-chemistry
    - bgc-2643-molecular-reading
    - bgc-2643-diagnostic-acceptance
    - bgc-2643-diagnostic-stderr
    - bgc-2643-row-mibig_compounds-0
    - bgc-2643-stereo-schema
    - bgc-2643-stereo-extractor
    - bgc-2643-stereo-seeder
    - bgc-2643-stereo-policy
  - name: representation_correspondence
    value: Both canonical comparisons false; empty match; carbonyl/enol placement
      differences
    definition: Saved canonical comparisons and limited atom-match result; normalized
      identifiers are not full graph proof.
    evidence_ids:
    - bgc-2643-identity
    - bgc-2643-chemistry
    - bgc-2643-molecular-reading
    - bgc-2643-diagnostic-acceptance
    - bgc-2643-diagnostic-stderr
    - bgc-2643-row-mibig_compounds-0
    - bgc-2643-stereo-schema
    - bgc-2643-stereo-extractor
    - bgc-2643-stereo-seeder
    - bgc-2643-stereo-policy
- assessment_id: bgc-2643-provenance
  area: provenance
  topic: provenance
  outcome: unknown
  summary: Active BGC0001976 version 3 retains questionable quality and unknown completeness.
    Phoma sp. NCBITaxon:1707701 is SOURCE_ASSERTION and MK400120.1 is CLUSTER_UNSTATED
    without a retained method or bounded locus. The raw class terpene and subclass
    Unknown remain separate. A genus-level Phoma occurrence is not strain-specific
    biosynthetic support.
  target_ids:
  - naturalproductmech:mibig-d7152699ce
  evidence_ids:
  - bgc-2643-owner
  - bgc-2643-provenance
  - bgc-2643-query-mibig_compounds
  - bgc-2643-query-lotus_occurrences
  - bgc-2643-taxonomy
  - bgc-2643-curation
  - bgc-2643-direct-contexts
  - bgc-2643-row-mibig_compounds-0
  - bgc-2643-row-lotus_occurrences-0
  - bgc-2643-delegated-context-reading
  dimensions:
  - name: taxon_scope
    value: Producer Phoma sp. 1707701 versus occurrence Phoma 37463
    definition: Retained names, IDs and synonyms; current rank and ancestry are not
      independently established.
    evidence_ids:
    - bgc-2643-owner
    - bgc-2643-provenance
    - bgc-2643-query-mibig_compounds
    - bgc-2643-query-lotus_occurrences
    - bgc-2643-taxonomy
    - bgc-2643-curation
    - bgc-2643-direct-contexts
    - bgc-2643-row-mibig_compounds-0
    - bgc-2643-row-lotus_occurrences-0
    - bgc-2643-delegated-context-reading
  - name: producer_evidence
    value: SOURCE_ASSERTION
    definition: Literal source grade for the compound producer assertion.
    evidence_ids:
    - bgc-2643-owner
    - bgc-2643-provenance
    - bgc-2643-query-mibig_compounds
    - bgc-2643-query-lotus_occurrences
    - bgc-2643-taxonomy
    - bgc-2643-curation
    - bgc-2643-direct-contexts
    - bgc-2643-row-mibig_compounds-0
    - bgc-2643-row-lotus_occurrences-0
    - bgc-2643-delegated-context-reading
  - name: locus_evidence
    value: 'BGC0001976: CLUSTER_UNSTATED'
    definition: Literal source grade for the locus-to-compound assertion.
    evidence_ids:
    - bgc-2643-owner
    - bgc-2643-provenance
    - bgc-2643-query-mibig_compounds
    - bgc-2643-query-lotus_occurrences
    - bgc-2643-taxonomy
    - bgc-2643-curation
    - bgc-2643-direct-contexts
    - bgc-2643-row-mibig_compounds-0
    - bgc-2643-row-lotus_occurrences-0
    - bgc-2643-delegated-context-reading
- assessment_id: bgc-2643-citations
  area: evidence
  topic: citations
  outcome: unknown
  summary: PMID:30980906 is retained at ENTRY grain. The LOTUS occurrence cites DOI:10.1016/J.FGB.2019.04.004.
    Neither reference was newly opened, and their overlap in subject matter is not
    independent experimental confirmation. Database IDs remain recorded source links
    without new identity validation.
  target_ids:
  - naturalproductmech:mibig-d7152699ce
  evidence_ids:
  - bgc-2643-provenance
  - bgc-2643-query-mibig_compounds
  - bgc-2643-query-lotus_occurrences
  - bgc-2643-query-chebi_origins
  - bgc-2643-source-reading
  - bgc-2643-history
  - bgc-2643-row-mibig_compounds-0
  - bgc-2643-row-lotus_occurrences-0
  - bgc-2643-delegated-context-reading
  dimensions:
  - name: citation_scope
    value: ENTRY PMID:30980906 and retained LOTUS DOI
    definition: Reference grain in the retained source rows; no inherited primary-paper
      access.
    evidence_ids:
    - bgc-2643-provenance
    - bgc-2643-query-mibig_compounds
    - bgc-2643-query-lotus_occurrences
    - bgc-2643-query-chebi_origins
    - bgc-2643-source-reading
    - bgc-2643-history
    - bgc-2643-row-mibig_compounds-0
    - bgc-2643-row-lotus_occurrences-0
    - bgc-2643-delegated-context-reading
- assessment_id: bgc-2643-occurrence_activity
  area: evidence
  topic: occurrence_activity
  outcome: unknown
  summary: One LOTUS row records Phoma NCBITaxon:37463, distinct from the producer
    identifier 1707701. The PubChem join returns a blank-AID sentinel rather than
    an experimental result. No actual AID, quantified activity or molecular target
    is established in this retained scope; the negative frames do not establish inactivity.
  target_ids:
  - naturalproductmech:mibig-d7152699ce
  evidence_ids:
  - bgc-2643-activity-owner
  - bgc-2643-query-lotus_occurrences
  - bgc-2643-query-chebi_origins
  - bgc-2643-query-cyanometdb_occurrences
  - bgc-2643-query-pubchem_bioassay
  - bgc-2643-query-bindingdb_targets
  - bgc-2643-query-antibioticmech_inchikeys
  - bgc-2643-assay-curation
  - bgc-2643-direct-contexts
  - bgc-2643-row-lotus_occurrences-0
  - bgc-2643-row-pubchem_bioassay-0
  - bgc-2643-delegated-context-reading
  dimensions:
  - name: occurrence_scope
    value: One genus-level LOTUS placement; no strain transfer
    definition: Exact retained occurrence query scope, without production or independence
      transfer.
    evidence_ids:
    - bgc-2643-activity-owner
    - bgc-2643-query-lotus_occurrences
    - bgc-2643-query-chebi_origins
    - bgc-2643-query-cyanometdb_occurrences
    - bgc-2643-query-pubchem_bioassay
    - bgc-2643-query-bindingdb_targets
    - bgc-2643-query-antibioticmech_inchikeys
    - bgc-2643-assay-curation
    - bgc-2643-direct-contexts
    - bgc-2643-row-lotus_occurrences-0
    - bgc-2643-row-pubchem_bioassay-0
    - bgc-2643-delegated-context-reading
  - name: assay_target_scope
    value: 0 actual AIDs; one blank sentinel; no target
    definition: Actual AID, endpoint and direct-target scope, including sentinels
      and exclusions.
    evidence_ids:
    - bgc-2643-activity-owner
    - bgc-2643-query-lotus_occurrences
    - bgc-2643-query-chebi_origins
    - bgc-2643-query-cyanometdb_occurrences
    - bgc-2643-query-pubchem_bioassay
    - bgc-2643-query-bindingdb_targets
    - bgc-2643-query-antibioticmech_inchikeys
    - bgc-2643-assay-curation
    - bgc-2643-direct-contexts
    - bgc-2643-row-lotus_occurrences-0
    - bgc-2643-row-pubchem_bioassay-0
    - bgc-2643-delegated-context-reading
- assessment_id: bgc-2643-classification
  area: consistency
  topic: classification
  outcome: unknown
  summary: The conjugated oxygenated rings and mixed polycyclic framework are compatible
    with the broad Meroterpenoids interpretation. NPClassifier reports Polyketides,
    Terpenoids and Tetraketide meroterpenoids, with is_glycoside false. Exact tetraketide
    origin and model-family applicability are not established by the local topology
    or the ungraded source locus alone.
  target_ids:
  - naturalproductmech:mibig-d7152699ce
  evidence_ids:
  - bgc-2643-classification-owner
  - bgc-2643-query-npclassifier
  - bgc-2643-query-mibig_compounds
  - bgc-2643-chemistry
  - bgc-2643-molecular-reading
  - bgc-2643-row-npclassifier-0
  - bgc-2643-row-mibig_compounds-0
  dimensions:
  - name: classification_applicability
    value: Broad meroterpenoid compatibility; exact tetraketide origin unresolved
    definition: Encoded motif support separated from exact computed model-family or
      biosynthesis claims.
    evidence_ids:
    - bgc-2643-classification-owner
    - bgc-2643-query-npclassifier
    - bgc-2643-query-mibig_compounds
    - bgc-2643-chemistry
    - bgc-2643-molecular-reading
    - bgc-2643-row-npclassifier-0
    - bgc-2643-row-mibig_compounds-0
- assessment_id: bgc-2643-completion
  area: completeness
  topic: completion
  outcome: unknown
  summary: The complete owner and history, scoped retained source payloads, both full
    saved molecular forms, and 44 actual input hashes and ownership declarations were
    reviewed. The accepted plan and intakes contain 458 input placements across 69
    paths. Five local gates passed; full QC, OAK and fresh external authority remain
    unavailable. No mechanism or declared-component root is present in this owner,
    so no maintained reader applies. Completion remains partial.
  target_ids:
  - naturalproductmech:mibig-d7152699ce
  evidence_ids:
  - bgc-2643-intake
  - bgc-2643-intake-acceptance
  - bgc-2643-plan
  - bgc-2643-plan-acceptance
  - bgc-2643-gates
  - bgc-2643-source-reading
  - bgc-2643-source-notes
  - bgc-2643-molecular-reading
  - bgc-2643-diagnostic-acceptance
  - bgc-2643-mechanism-scope
  dimensions:
  - name: review_completion
    value: Partial; 44 actual inputs and complete paired forms
    definition: Actual local review scope and unavailable required gates.
    evidence_ids:
    - bgc-2643-intake
    - bgc-2643-intake-acceptance
    - bgc-2643-plan
    - bgc-2643-plan-acceptance
    - bgc-2643-gates
    - bgc-2643-source-reading
    - bgc-2643-source-notes
    - bgc-2643-molecular-reading
    - bgc-2643-diagnostic-acceptance
    - bgc-2643-mechanism-scope
findings: []
actions: []
limitations:
- Both stored forms were read completely from the accepted saved diagnostic without
  reparsing. Normalized identifier, formula and charge agreement does not establish
  complete graph correspondence or natural identity.
- The diagnostic attempts a limited chirality-aware substructure match. Its full_graph_identity_established
  flag remains false, including when a complete one-way atom match is present.
- Four undefined-stereo warning blocks belong to the original global stderr and are
  not attributed to a particular owner or form.
- Retained source dictionaries, database references and historical curator annotations
  were read locally. No primary publication, sequence, coordinate model, live taxonomy
  authority or external database was newly accessed.
- Cached taxonomy supplies IDs, retained names and synonyms without independently
  verified rank, lineage or freshness. Occurrence does not establish production.
- All captured input hashes and ownership declarations were verified; source payloads
  were read within the recorded query scope. This is not a claim to have scientifically
  read every row of every input table.
- Five local gates passed, but full QC and OAK remain unavailable. Scientific and
  overall completion remain partial.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- No amide/imidic interpretation is applied to this nitrogen-free structure.
- The positional representation difference is retained without prescribing an unsupported
  replacement structure.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-265
```
