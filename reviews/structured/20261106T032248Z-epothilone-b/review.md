# Local evidence review: epothilone B

- Review: 20261106T032248Z-epothilone-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T02:22:01.261994Z
- Finished UTC: 2026-11-06T03:22:48.015991Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Epothilone B has consistent retained ChEBI grounding and stereospecified molecular encodings. Its complete mechanism preserves a terminal EpoK step, qualified strain-specific assembly annotations and deposited tubulin-model contacts. One written assay has an unsupported enzyme-specific class: AID 504832 describes delayed parasite death without identifying an enzyme. This bounded class finding requires curation; the assay measurement and the separately scoped NSD2 observations remain intact.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2641; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:31550 | data/natural_products/unclassified/epothilone-b.yaml | generated | epothilone B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for epothilone-b | passed | True | CHEBI:31550 | The accepted original reader preserves the complete owner and six ordered components, eight graphs, 52 nodes, 44 edges, one terminal step, 149 graph evidence placements, four step references and all histories. |
| strict_ten | passed | True | CHEBI:31550 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:31550 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:31550 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:31550 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:31550 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:31550 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:31550 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:31550 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### identity

identity: supported. Targets: CHEBI:31550.

CHEBI:31550 is retained EXACT grounding. Both saved forms regenerate QXRSDHAAWVKZLJ-PVYNADRNSA-N, C27H41NO6S and net charge 0, with identical canonical strings. The retained ChEBI definition describes the epoxide derived from epothilone D, and four MIBiG compound rows agree with the encoded structure. These support local encoded and database consistency. The OPEN four-entry shared-structure discussion remains unresolved; normalized agreement does not independently characterize natural or engineered products.

### representation

representation: supported. Targets: CHEBI:31550.

Both complete forms have 35 atoms, 37 bonds and three returned rings: a 16-member lactone, a three-member epoxide and a five-member aromatic thiazole. One ester, one ketone and two hydroxyl groups accompany seven specified tetrahedral centers and one specified E alkene. No original tetrahedral center is unspecified. Local stereo-atom conventions differ in one descriptor, while both bond tables and canonical strings preserve the E geometry. The complete 35-index one-way match is limited correspondence, not full graph or natural-identity proof.

### provenance

provenance: unknown. Targets: CHEBI:31550.

The four active MIBiG entries BGC0000988.5, BGC0000989.3, BGC0000990.3 and BGC0000991.4 retain questionable quality, unknown completeness, SOURCE_ASSERTION producers and CLUSTER_UNSTATED loci. They distinguish Sorangium cellulosum NCBITaxon:56 from So0157-2 NCBITaxon:1254432 and the four genome accessions. Literal classes NRPS&#124;PKS remain separate from subclasses Type I&#124;Unknown. Later curated protein graphs do not silently upgrade these source-owned grades or make strains interchangeable.

### citations

evidence: unknown. Targets: CHEBI:31550.

The source rows cite PMID:10662695, PMID:23549746 and PMID:10649995 at ENTRY grain; the repeated first PMID is not independent replication. The retained EpoK annotation cites a primary-experiment snippet plus database and curator evidence. SMP44 assembly includes an abstract-only whole-cluster production claim; other strain components preserve proposed participation and inaccessible-paper limits. PDB contact graphs preserve database and historical coordinate annotations. No cited paper, sequence or structure deposition was newly accessed.

### occurrence_activity

evidence: concern. Targets: CHEBI:31550.

Eleven LOTUS placements support occurrence assertions across the exact retained taxa and citations, without production or publication-independence inference. The uncapped assay query contains 117 rows representing 111 full-key/CID/AID tuples; six paired rows differ in target-accession content. The owner retains 25 sorted observations and explicitly omits 92. AID 504832 is ACTIVE with source Potency 0.0013 uM, represented as OTHER, but its delayed-death 48-hour title and blank target do not support ENZYME_INHIBITOR. The 96-hour AID 504834 result is separately inconclusive. NSD2 cellular assays and O96028 annotations remain distinct; they do not establish direct enzyme inhibition or affinity, and their presence does not make the overall summary globally verified. No existing exact exclusion applies.

### classification

consistency: unknown. Targets: CHEBI:31550.

The stored 16-member lactone, epoxide and thiazole support a broad epothilone/macrolide structural interpretation. NPClassifier reports Amino acids and Peptides, Polyketides, Macrolides and Epothilones, with is_glycoside false. The retained topology is compatible with that family, but exact model applicability and biological assembly are separate claims. Strain-specific biosynthesis graphs and deposited tubulin contacts are assessed at their own evidence grain rather than inferred from classification.

### completion

completeness: unknown. Targets: CHEBI:31550.

The complete owner and history, scoped retained source payloads, both full saved molecular forms, and 52 actual input hashes and ownership declarations were reviewed. The accepted plan and intakes contain 458 input placements across 69 paths. Five local gates passed; full QC, OAK and fresh external authority remain unavailable. The accepted complete Epothilone maintained view includes all six components; preservation does not independently validate their historical scientific claims. Completion remains partial.

### qualified_epothilone_biosynthesis_and_model_contacts

graph: supported. Targets: CHEBI:31550.

The accepted maintained view preserves eight complete graphs, 52 nodes, 44 edges, six component references and one numbered pathway step. EpoK Q9KIZ4/RHEA:47808 records terminal D-to-B epoxidation; the step has no literal proposed field. SMP44 and the three other strain graphs separately retain source-annotated or proposed participation, without a complete reaction order or transferred individual enzyme assays. So0157-2 EpoF remains a generic P450, while KYC3013 uses versioned protein references instead of deleted UniProt entries. The 9PND, 6S8M and 7DAE graphs restrict drug contact to deposited beta-tubulin models and distinguish construct membership, ligand-quality limitations and missing coordinates. Complete reader equality supports faithful retained representation, not fresh protein/sequence/coordinate validation, binding affinity or downstream effect.

## Findings

### bgc-2641-unsupported-delayed-death-enzyme-class: Delayed parasite-death screening is promoted to enzyme inhibition

major / open / confirmed; issue key: epothilone-b-aid504832-unsupported-delayed-death-enzyme-class.

The exact QXRSDHAAWVKZLJ-PVYNADRNSA-N/CID448013/AID504832 source row describes delayed death of the malarial parasite plastid after 48 hours, with Active, Potency 0.0013 uM and a blank target accession. The written observation faithfully retains ACTIVE, OTHER and 0.0013 uM, but the generic inhibitors-of title fallback adds ENZYME_INHIBITOR without an enzyme-specific endpoint or identified enzyme. This is a confirmed retained-evidence class-scope defect, not a measurement, identity or source-row error. NSD2 cellular assays remain separate evidence and do not make the whole summary scientifically verified; automatic summary deletion is not justified by this single finding.

Disposition: Proposed local maintained-classifier correction and focused validation only; no record/source edit, external lookup or completed fix is claimed.

## Recommended Actions And Acceptance Checks

### bgc-2641-bound-delayed-death-classification

Revise the maintained classifier so generic inhibitors-of wording in a phenotypic delayed-death title does not alone establish ENZYME_INHIBITOR. Determine the appropriately supported class from retained evidence without prescribing an unverified replacement. Preserve ACTIVE, OTHER, 0.0013 uM, pubchem.aid:504832, original source bytes and all other observations. Reassess any derived summary against its remaining independent backing rather than deleting it automatically. This is proposed local work, with no outbound request authorized.

- The exact AID504832 row no longer receives enzyme specificity solely from the generic title, while its call, measurement, unit, evidence and original input row remain exact.
- Keep distinct AID504834 96-hour inconclusive behavior and all six target-accession variant pairs; do not collapse positive-row attribution or apply a different-key/CID exclusion.
- Retain and separately scope NSD2-named cellular observations and O96028 annotations; do not infer direct inhibition/affinity or automatically erase the overall enzyme-class summary.
- If a generator change is separately authorized, add focused local supported/unsupported-title regression coverage, regenerate through maintained validated paths and verify strict, corpus and reproduction checks without observation loss or changes to the established 25-observation ordering/cap.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2641-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/epothilone-b.yaml; Complete plaintext including every curation_history entry | supports | Complete current owner and all 12 history entries were personally read. Historical curator assertions do not confer fresh source-access credit. |
| bgc-2641-capture | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/0 | supports | Actual complete owner capture preserves current local content; it is not an independent scientific validation. |
| bgc-2641-identity | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/label; /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status | supports | Exact stored identity, source concepts, grounding and chemical encodings; natural identity is assessed separately. |
| bgc-2641-history | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/0/owner_document/curation_history | supports | All 12 current history entries retain their original source and curation scope; no inherited paper access is claimed. |
| bgc-2641-provenance | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts | supports | Owner-specific producer, locus and source-concept assertions preserve their distinct grades and references. |
| bgc-2641-activity-owner | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/0/owner_document/occurrences; /records/0/owner_document/bioactivities; /records/0/owner_document/xrefs | supports | The selected occurrence, activity (when present) and cross-reference fields retain their distinct claim scopes. Occurrence or a cross-reference does not establish production, activity or mechanism. |
| bgc-2641-classification-owner | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/0/owner_document/np_pathway; /records/0/owner_document/biosynthesis_origin; /records/0/owner_document/np_classification; /records/0/owner_document/bgc_class | supports | Recorded classification/model labels and BGC class content; exact source subclasses remain separately visible in the retained MIBiG row. |
| bgc-2641-mechanism-scope | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/0/owner_document/causal_graphs; /records/0/owner_document/biosynthetic_pathway; /records/0/owner_document/discussions; /records/0/owner_document/causal_graph_refs | supports | The complete captured raw owner retains two inline graphs, six declared component references, one numbered terminal step whose proposed field is absent, and the OPEN shared-structure discussion. The separately linked maintained-reader evidence contains all eight resolved graphs; no complete experimental pathway is inferred. |
| bgc-2641-reader-DATA | /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json; /resolved_view; /counts; /returned_view_equals_expected_complete_owner; /denials; /limitations | supports | The actual maintained view was personally read in full, including every graph, step, reference and history field. Exact preservation is distinct from biological or sequence verification. |
| bgc-2641-reader-execution | /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-reader-execution-001.json; /command; /exit_code; /stdout; /stderr; /original_tools; /process_receipt | supports | The original maintained-reader execution closed once with exit 0 and preserved genuine stdout/stderr and terminal objects. |
| bgc-2641-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch265/root-native-reader-2641-acceptance-001.json; /accepted; /DATA; /execution; /verification; /review_check_contract; /scientific_limits | supports | ROOT accepted this exact positive reader result. One expected IPv6 socket-construction probe was denied before action; no request was sent. |
| bgc-2641-reader-reading | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-current265-Epothilone-B-maintained-view-reading-001.json; /complete_owner_read; /counts; /interpretations; /limits | supports | Independent scientific reading of the complete maintained owner preserves the qualified biosynthesis/model graphs, component histories and citation limits. |
| bgc-2641-intake | /private/tmp/npm-review-work/shared-next-batch265/intakes-001/2641-inspect-001.json; /targets; /source | supports | Actual canonical inspection captures 52 current input hashes and complete target ownership declarations. Hash capture does not imply whole scientific reading of each input table. |
| bgc-2641-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch265/root-intakes-acceptance-001.json; /accepted; /status; /summary | supports | ROOT accepted the ten actual canonical inspections and their exact 458-input/69-path scope. |
| bgc-2641-plan | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-target-input-plan-001.json; /records/0; /source_placement_count; /unique_source_path_count | supports | This owner has 52 exact planned inputs, now matched to its accepted actual canonical inspection; the full plan has 458 placements/69 paths. |
| bgc-2641-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch265/root-source-plan-acceptance-001.json; /accepted; /status; /plan | supports | ROOT accepted the original local composed input plan; all current input paths and roles are preserved. |
| bgc-2641-chemistry | /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-DATA-001.json; /records/0 | supports | Both complete saved forms, all atom/bond/ring/motif/stereo fields, comparisons and limited atom correspondence were personally read. No alternative parse was performed. |
| bgc-2641-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /status; /DATA; /execution | supports | ROOT accepted the once-only offline diagnostic execution and saved outputs; this does not establish natural identity or full graph equivalence. |
| bgc-2641-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-execution-001.json; /exit_code; /stdout; /stderr | supports | Actual diagnostic execution closed with exit 0 and preserved original stdout/stderr; no diagnostic replay was made. |
| bgc-2641-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-original-001.stderr; Complete original stderr | context_only | The original diagnostic stderr contains four undefined-stereo warning blocks. They remain global and are not attributed to a particular owner or stored form. |
| bgc-2641-molecular-reading | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-current265-first-five-molecular-intake-reading-001.json; /records/0; /reading_attribution; /limitations | supports | Owner-specific complete saved-table reading and interpretation, with normalized identifiers distinguished from canonical correspondence and natural identity. |
| bgc-2641-gates | /private/tmp/npm-review-work/shared-next-batch265/root-native-gates-acceptance-001.json; /checks_passed; /all_native_gates_passed; /unavailable_required_gates; /complete_selected_queue_rows | supports | Five local checks passed. Full QC and OAK remain unavailable, so native completion and scientific completion are not promoted. |
| bgc-2641-source-reading | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-current265-assigned-source-reading-001.json; /records/1; /full_meaning_scope; /boundaries | supports | Assigned retained-row meanings and all query metadata for this owner were read. References remain retained database assertions rather than newly inspected primary papers. |
| bgc-2641-source-notes | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /reading_boundaries | supports | Original 458-input/69-path source notes preserve disjoint positive-row reading credit 187 BGC + 38 Support + 0 Native. Actual intake acceptance is supported separately. |
| bgc-2641-taxonomy | /private/tmp/npm-review-work/shared-next-batch265-tentative/native-prep/native-current265-cached-taxonomy-reading-001.json; /context_interpretations/2; /interpretation | partial | Owner-local retained taxonomy routes, names and synonyms, with no current rank, lineage or freshness verification. |
| bgc-2641-curation | /private/tmp/npm-review-work/shared-next-batch265-tentative/native-prep/native-current265-implemented-curation-scan-001.json; /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope; /interpretation | context_only | Ignored-inclusive retained curation scope found no exact applicable correction. The producer-strain and row-digest implementation readings retain their bounded scope. |
| bgc-2641-assay-curation | /private/tmp/npm-review-work/shared-next-batch265-tentative/native-prep/native-current265-implemented-curation-scan-001.json; /assay_scope | context_only | The receipt-wide scan retains 118 actual assay rows, 112 exact tuples and five blank sentinels. Six tuple pairs differ in target-accession content; all row placements remain. The 117 Epothilone rows and one Equisetin row have no exact applicable exclusion. Same-AID decisions with other full keys or CIDs are not transferred. |
| bgc-2641-stereo-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392-396: stereo_complete description | context_only | The maintained flag describes undefined stereocentres; it does not by itself establish full double-bond geometric resolution. |
| bgc-2641-stereo-extractor | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters and undefined-tag predicate | context_only | The maintained extractor computes stereo_complete from unassigned tetrahedral chiral-centre tags. No extractor or molecule was rerun for this reading. |
| bgc-2641-stereo-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; line 995: direct stereo_complete copy | context_only | The maintained seeder copies the retained atom-centred boolean without independently resolving geometric stereochemistry. |
| bgc-2641-stereo-policy | /private/tmp/npm-record-reviews-20261021/docs/HARMONIZATION.md; lines 99-104: stereochemical completeness | context_only | The documented retained stereocentre scope is separated from unknown original bond geometry and reconstruction-derived imine descriptors. |
| bgc-2641-delegated-context-reading | /private/tmp/npm-review-work/shared-next-batch265-tentative/support-prep/support-current265-assigned-source-reading-001.json; /contexts | context_only | Support personally read the six complementary contexts, including the five last-half owners and Griseoviridin. This preserves attribution without adding BGC primary source-row credit or transferring activity between owners. |
| bgc-2641-direct-contexts | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-target-input-plan-001.json; /records/0/proposed_companion_paths; /records/0/direct_companion_predicates | context_only | This owner has 0 immediate shared-BGC context input(s); the exact predicates do not establish equivalent identity, independent experimental evidence or source transfer. |
| bgc-2641-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds query frame: 4 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2641-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 1114-1114; raw record sha256 5f918ca917d1b1e361f89faf27c9dcc21d1f4988535f2593f27e4e9ca81ec7f2 | supports | Assigned retained-row reading of all 25 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-mibig_compounds-1 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 1115-1115; raw record sha256 7e7b43c0b8914455e974332099b35c3640609b54f9ad8c90c1cec26702372fd5 | supports | Assigned retained-row reading of all 25 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-mibig_compounds-2 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 1116-1116; raw record sha256 0c82d326ca60fdf3ce8c36b2382c76a8ddab32c792185e0b2e04b6302a97f493 | supports | Assigned retained-row reading of all 25 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-mibig_compounds-3 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 1117-1117; raw record sha256 7de8b344995475f6d692bde3b56df7cbcfb0aba30b81aef39cbd383b2856fc79 | supports | Assigned retained-row reading of all 25 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2641-row-chebi_structures-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; physical lines 8008-8008; raw record sha256 b3b8ee23db09f5ac06106098539e6a24b357eb7cb1176cabac06d02d05a0e45c | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences query frame: 11 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2641-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7586-7586; raw record sha256 129259be5c1dd8295a76f70fa04ab72ffe2206cd513ed7cad9ffa69b25b0ea65 | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7587-7587; raw record sha256 92e2ae70ea42f1ae24c09da73433021c30eb6e9d69150a4c8631a853080b4fb2 | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-lotus_occurrences-2 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7588-7588; raw record sha256 a923ea114bbd131474b7120313b9363a75a754150836a382b67184437b9dd41d | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-lotus_occurrences-3 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7589-7589; raw record sha256 92436adc654ec3f1116fd3cb08e5a0748599c39043a905e265fbbc89b1b12d1a | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-lotus_occurrences-4 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7590-7590; raw record sha256 7f4454de52a3a0d51a7e18860878f68577d1e33ba469bb1c7f19f5270f58a9f6 | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-lotus_occurrences-5 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7591-7591; raw record sha256 73d02d760963fcf8985261a12881e8b00b173453241c946a45035c0aa74bdbb1 | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-lotus_occurrences-6 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7592-7592; raw record sha256 7fcf3ff6693b66604e5a7c818d45399eb5fbd6c7fd09dae18b93fc3826220ce3 | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-lotus_occurrences-7 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7593-7593; raw record sha256 af7f2c33e8d6a25485d83116b8ec37ab959a6e83e1351cac406d8f26e55410ee | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-lotus_occurrences-8 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7594-7594; raw record sha256 27af5fe26b59ccb3bc1eb138d7109cbaf8aea6286d7eb7bc6cdef9f281014a87 | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-lotus_occurrences-9 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7595-7595; raw record sha256 4ce178a7eda29c64f046f1801eeff946adf27003aefcf0141a6fe8c4b928815b | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-lotus_occurrences-10 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7596-7596; raw record sha256 7b2ed19ddeb2a1e4296ce1eb8ecbe1651bbfb1574ea3f944ef078d040c8bee4f | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2641-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2641-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2060-2060; raw record sha256 93b8c7ba42986bbf869c29d415571f4ef2799e16f49475c9d23cab967e4e3064 | supports | Assigned retained-row reading of all 7 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay query frame: 117 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2641-row-pubchem_bioassay-0 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5898-5898; raw record sha256 450ecf3be3a719425ec7cd41cc2633a6f3e4d6de6daf20fcc8ebf46bae696ebd | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-1 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5899-5899; raw record sha256 e3a9109fd6a1fd3260162e2b348dd2d464d1e1898ab91903aac2d97dc7283e2b | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-2 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5900-5900; raw record sha256 26158ac31134080466fd9aa57f919c5f0e2c3cae589dc678f3a7957d8c59d89d | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-3 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5901-5901; raw record sha256 a04e4e4a2319a36224dfef54c9fa3b85f4e81453eeac437cfb0579077808cf64 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-4 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5902-5902; raw record sha256 c07f51e239293d6f708b43571f79a9d3ef1db62672d1dcd73fe9029f64a1ddb9 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-5 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5903-5903; raw record sha256 16fdcece1d51af880490a32c3d5138e031a555e394a7710c6a73773b9b252ec1 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-6 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5904-5904; raw record sha256 4e5cabfb0843aa52c2130d70959ac597374a21e034c8c67ba7b8b91bd751ad28 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-7 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5905-5905; raw record sha256 90fab1d53a32dfa74d6394957fe679080673d109f874fcfbe94c58c2c4a779fe | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-8 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5906-5906; raw record sha256 6a86bc520c5b80079bdd884c081efe5ad5dc4d57e4538deb13ae5ab2035fde6f | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-9 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5907-5907; raw record sha256 8fa2beec5ef5eb06c4c6d04c89659a2648d2c2fcaf72848dda685ff11c72b86d | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-10 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5908-5908; raw record sha256 a5f150f2851e091314936bb4872a608b308e5ddd2ba9a8ccb35ab07855f9db96 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-11 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5909-5909; raw record sha256 73a99ce9b92c743e43005888e37354f0e831d701005814318d3c7984363567dd | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-12 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5910-5910; raw record sha256 bde5c0020f1a20782682d88c1722935adf16c31fbae5669d14176c2e47fc0d15 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-13 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5911-5911; raw record sha256 973670b9c05beb9eebdc50e2e4ebe761e52cf9b664f59e4a8e6da04631ce4bc9 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-14 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5912-5912; raw record sha256 2b5fc3146f42ad9d29431c30cc13a313c1460a8dc9e9a8f1fa90f4605e092473 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-15 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5913-5913; raw record sha256 c3610138460ccd946cf471e78100741e72e33ade3d0c7b64b47f3c345dcbd6ff | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-16 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5914-5914; raw record sha256 b1ef0f78848b40e8681df4609d7c7daf340b905e69fd1f082803ddfb06850023 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-17 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5915-5915; raw record sha256 72a5e4943a05cb645a74ba9b9feca1c8a8d4772fa4bde2a303e0a8172c9ad448 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-18 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5916-5916; raw record sha256 29a5c664db570b56fa28c33c41bb28dd20ca35eed3762a033ede9cba955c3e8d | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-19 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5917-5917; raw record sha256 47744a81fb785bdf1d787f264ea116ec57c931552004a91045a0360f3ea9285f | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-20 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5918-5918; raw record sha256 18d46a121c6925c8440c93d3c357ba2bd73b43bcb397ec272642c3b263b4c85a | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-21 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5919-5919; raw record sha256 f8e8074df8923730f67a14ac1a8cca57e25ff406fe82be2e89f28701cefc8219 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-22 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5920-5920; raw record sha256 8825a6ac52ba00bc33ae08abdbebda24e2493e3e8bafb0b24956f6103f3a58fe | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-23 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5921-5921; raw record sha256 0e757e82bd32b1ba720748310c675702c29188dcbf76f16f41055395de9bc601 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-24 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5922-5922; raw record sha256 34356c1f31da7a4ffc1d51d0e8df1e20af17a7c409158f573d81a4758920a36b | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-25 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5923-5923; raw record sha256 bfb293d68eef33e896a0b660974a26d2324dec3f77be48cc97889ba090213972 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-26 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5924-5924; raw record sha256 4ee90a0b437d2822f2b64814d99ceb4046f75d0d5bb76321c46be3f5307498b7 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-27 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5925-5925; raw record sha256 c141d95dd952a21eb0d080d0093bf031eba48b521fa162ae73b09eb531348820 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-28 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5926-5926; raw record sha256 1df1ce662597d3c5e4aaa5db257b073f5f524848eb7cdc79ed3b125e8a7e649a | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-29 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5927-5927; raw record sha256 2876b3905671fcbecc3a4ea7dd3d7e134d2c27091bc0c865c2afd8c58083b216 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-30 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5928-5928; raw record sha256 7fbcfcff7e69c87ecbc37cc5844b0acb8ec8ddef955965c247c44d6ce35d8211 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-31 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5929-5929; raw record sha256 be2954579c1a2b6ed49ce868cdd9a971c0c4468e7fe2879bad3506af8da639d8 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-32 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5930-5930; raw record sha256 6cd6dd1470ab572c4f26aa1e3ecc7763ea52cc6578fc47935fe5d3f27dd1055f | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-33 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5931-5931; raw record sha256 4ec9b60be4e827f8423e85c45065414dd0253b3de351a13f649cfe804cfa13dc | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-34 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5932-5932; raw record sha256 99f52756f1ca54a01559776b86333aa3cecf9807337c6047cd932222d1d7e6ef | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-35 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5933-5933; raw record sha256 9d79932da845c710890b46ff0930ab1164dfb23d6f4ada361bd57c602430dd64 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-36 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5934-5934; raw record sha256 b661eadba99725c90c16d72f7d3777fbf60b78cd6a8bc77b8763cad917b3fab0 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-37 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5935-5935; raw record sha256 fdb36296e593c125eeb8ead3afd0fbf4a74e8e205d6baa4ed6fa41c54fc1a8f8 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-38 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5936-5936; raw record sha256 c52f1ab123ce2f7ba23bc40ea811ed3f6f565b5c8ab679bf059d31662d200f1e | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-39 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5937-5937; raw record sha256 bcf46c68e453eefbd668f1205567e7defa198d4dca2135e6f103190dce6d0674 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-40 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5938-5938; raw record sha256 88071946066701a2b0bb2976b2f2cd4ef23d83992c99bb42564203ba0c055fca | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-41 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5939-5939; raw record sha256 feb0bb85be85e67007c1cfb41f995de4d9bc67eebf28cfd1e363124cde4abb84 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-42 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5940-5940; raw record sha256 02b21767b26635409972f3cf5a1fd5e40a588aa2d56f8fff2336eee8f68372ac | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-43 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5941-5941; raw record sha256 1ad99ab95ade85f7e5dcbfbb078a8e294c9915e6e442dc0e5c72b0b74b5a8a36 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-44 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5942-5942; raw record sha256 be14060565b3cb24206357849c607b600f52abd22e5a94f39cecb88889551f97 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-45 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5943-5943; raw record sha256 73ef51ccadf15fad3d97cff32c59a26a947248354ca786e771425c41c0351a7d | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-46 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5944-5944; raw record sha256 9623a5d3d02cb7c2a5b999bc7aae29131fe4f2e3224ee86092126a744273c2f7 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-47 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5945-5945; raw record sha256 0acb22b97c405c2899e892b17b8aeb5806f120846379d3566ef6f2bf84dd135b | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-48 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5946-5946; raw record sha256 c483ed4d6635362a6df11e10876915ca59722cac0580f8f03eb91f622e765b4e | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-49 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5947-5947; raw record sha256 096f7426350dd072921dc0e21aab6b5e694957c8b0817a29ec400b2db70bdcd4 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-50 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5948-5948; raw record sha256 6ae29e20088d5dfec11461fe3909d9941457072a36b25d7fa5643a767fafd71a | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-51 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5949-5949; raw record sha256 f01a893f0d9c5f8e335fb1f3810f44ab67cbe25901f31b1e54050e477c240bb7 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-52 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5950-5950; raw record sha256 64936c16fee91021ca7b685aa003dc7b45c0850c0dfafa7962b4ed07e34708b9 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-53 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5951-5951; raw record sha256 4b4351dadd21025ae7aacdae204c6151247512b171c4a2286faeade5606c4525 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-54 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5952-5952; raw record sha256 d7480821160ad4a9bf6c06af25584e8135f235466a87251cd59a30941aa6a29d | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-55 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5953-5953; raw record sha256 333a5a94fd03d4e62740d0466591112562b878d3c75f18f26eee82ac703e4488 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-56 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5954-5954; raw record sha256 14283ebfa2743ef5901884bfd7a5aec186b417d8f6ebdf7b140ef362d426d176 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-57 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5955-5955; raw record sha256 0c845aa1d7bca96159ad7df2d41e6cd4e015fdfd14e8670f57a00c56541cbd05 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-58 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5956-5956; raw record sha256 0e2c8dfb2a3ffb513f7319e5370d7a7c4a6f995a349575b049687028d8b607af | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-59 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5957-5957; raw record sha256 2d29b53158300d24b7327c0789370e061f92d5f84244d5084ec88c5be3341f93 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-60 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5958-5958; raw record sha256 640812cdb0dc94c0900567e7c908062bfcbf8d4d5871e02bbebc031b4de6e3f3 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-61 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5959-5959; raw record sha256 b00b4aee47800ef3f8ffffb2a5011c9b45740cb2342da150de938d80dc7b330a | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-62 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5960-5960; raw record sha256 7a181456a2e4cc451b3a451b19c079096986275b3a38bda551350a59b495fde4 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-63 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5961-5961; raw record sha256 078dff037ca246668cd5261ed606b671b6441c2526514bb4ac020144e3746032 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-64 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5962-5962; raw record sha256 2547d02404ec28fd2a8d88cffd45714d1737680a73bcaa953cfcf53a7748c188 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-65 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5963-5963; raw record sha256 38282118db2c6386d00bf8b157390d20dc20cca623c10b08c1d4452bc04b37ce | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-66 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5964-5964; raw record sha256 14b4423b5efc6a4b68aed0abb27f76ac9ff95f6813be8afe3197d21054b79bd6 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-67 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5965-5965; raw record sha256 cab0559fc129bdc699a8390ba2d19f1223b7c7fc8b17fa08dd7e53d5aea8f9b9 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-68 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5966-5966; raw record sha256 554f1c56339f29bac26f9ddd0dd5d9ada3e0037b09b9e897390ddbc164584b40 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-69 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5967-5967; raw record sha256 349d0634b8e2f1ab336fa542765402d0337bad14b19693363aecca3491e58da7 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-70 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5968-5968; raw record sha256 b19b3b3f35bfe5b4a77771f9eb701602d112adf75a997d8de08342066bb87f33 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-71 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5969-5969; raw record sha256 847dd0ae31db8067201f57acffb24ee9e451b77ec80540a12d9956e1c3c0524e | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-72 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5970-5970; raw record sha256 0aa78c6ff49554eb0012a9a4ff5e4fe06948c19200b22949e183026ef1085b1e | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-73 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5971-5971; raw record sha256 74470905babd22b96200ee63cdb40d8d9d31793a200692e7f519969f4fa03f25 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-74 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5972-5972; raw record sha256 0ca55b31a0359308b8330eb933d9260f78bd25e81f8b221bab775e3fb5d3e58c | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-75 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5973-5973; raw record sha256 d3d5aa9b86320ac2068f6e6fb152054bc80543aac5f4338d6d72c293787556f3 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-76 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5974-5974; raw record sha256 02544239e71e3cd574c9e6f9d5ece54c6f1ebf1554fdd1d0a56d08e5eb7467e9 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-77 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5975-5975; raw record sha256 ba2b784ef45831a670506f72a22f07c5eb7cc72f6d4d9c15954c6697cbf455f7 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-78 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5976-5976; raw record sha256 943a76331ad0e5da8b346ede6c4ae44a4546e25c5fd0aff6e0ab6854b3b2a4d0 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-79 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5977-5977; raw record sha256 6eaa00e6d4521540e8daa448a536ae31fc44c016b764d4a7574d4cbc568d65b6 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-80 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5978-5978; raw record sha256 a3ff8f1f57138445c20ee3c76783aa7b4de77ac20d6ae05964fa66d9a301e7f0 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-81 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5979-5979; raw record sha256 0de403d212c9e60a6c96f1ce730b794444da01b8d28f3df13862eff57170c788 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-82 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5980-5980; raw record sha256 cd7338c00cb2e2d21f450c0f1a8544b0c20ebb1928cf3a69692944f1ae0ec64c | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-83 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5981-5981; raw record sha256 0f3d9a9143cebb4ce0307c38116902bb1e040a6d9d10456dcb437c2ad2e54d69 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-84 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5982-5982; raw record sha256 128568060ff228c14a45180f0e22b99c5d7e4070fe47dc34f65b5bebd0432964 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-85 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5983-5983; raw record sha256 27734e8e0623a7d890aea527ff26cd6f8f353db04142aa870a3a86223f3e88f4 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-86 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5984-5984; raw record sha256 9344602355f839e54a1b058b399eafc4a71948e7274afc12abd163acab7fa03c | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-87 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5985-5985; raw record sha256 eb8b18ab0b6a9c1870dd6e06e7cf90134e2ca183d67fd8a9d8456682a903e5c4 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-88 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5986-5986; raw record sha256 e5ae7cdc683be5daef55d748d7bed55b5e71c817d240f09104468192e9e30f1c | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-89 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5987-5987; raw record sha256 6f00eca47565d880402b24d428681669e6dd995de121e916839d68aea0510c10 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-90 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5988-5988; raw record sha256 de2108c18b02fa07c956fc85c89ac749fcfbb2080a1a05d9a2110bf51d3316da | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-91 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5989-5989; raw record sha256 d98bd1fdcb93bfdd539c8d5d48e63c40cfddcdbf0f1effc77196c36255cead30 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-92 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5990-5990; raw record sha256 32fb23b18fc7d436c971b2a931ebb1ba5cfc3dd5f5ff5222d1384cb14bca6d26 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-93 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5991-5991; raw record sha256 d16afae1786795fb6baf26e51cd6be4a9091216b0b041a5e0155153501b9b9cf | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-94 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5992-5992; raw record sha256 5bf3ce701c349a375b6c7b2341fa80a57414f72fd5f69a897a72075f83b93ff5 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-95 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5993-5993; raw record sha256 a2adccf6374eb33354a5a455e729a8be9ff6b0a2e19eee41d1eff20552010bb3 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-96 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5994-5994; raw record sha256 597e217902e2cae485c6bf35a6188e17a88071deb97576c8bc2d004bc70e4aa3 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-97 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5995-5995; raw record sha256 6f3be4eea1dafb8aa3c5da82911493df42ca26a729ee6fc6e8bb607680d35dc2 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-98 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5996-5996; raw record sha256 220e4d9d57ff3b30e22f871d8efb84a2be94641e315493358a4b6c8771de50d5 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-99 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5997-5997; raw record sha256 35de9acdecd7a7ca86fc5451b24114319fda5aa2c2b2c51b25f31c94aa1ae1f6 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-100 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5998-5998; raw record sha256 aa4dc9f8dc8104909042990c9c473290f2c83e013e5f9c752da1c01e3158925f | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-101 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 5999-5999; raw record sha256 91c95e3f907508aa7599a4b75a1d8df474c48aa949443830a03c5bebac947c16 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-102 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6000-6000; raw record sha256 1f3815fe3304a4c882ca29bbaebad262b9bf371823ac55bbf02894dfffa7635d | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-103 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6001-6001; raw record sha256 df593e76124d749f32ead6fd40eb7d75cf74ca801f833a6e664e715b9128a206 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-104 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6002-6002; raw record sha256 04a1f973910c19eccebaf757c977d24805741f5ab4eb6579ccd4c475a913ca5f | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-105 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6003-6003; raw record sha256 4a752783f5ec1e6c5031f148710a7b34e23a5f4fdbb76913a22ed7808d496b17 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-106 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6004-6004; raw record sha256 6e88d0eea37c53461edca96a6cca2306327d8973547193cc3c07274205b5dd3f | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-107 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6005-6005; raw record sha256 f92c28f54e6aa51daa86b60079dd0ff4ef51233c0638ed977da32334ea0124f0 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-108 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6006-6006; raw record sha256 0a9546716d88aaff5f5ef88550a3e004cfc4fb76f256ed1478f80b7dcd387c20 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-109 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6007-6007; raw record sha256 163c3a36586a8fd7eeb5898ed242e995d730edaa4087945a5223cdf98478efa6 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-110 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6008-6008; raw record sha256 ae87c595d66db84c60fecef96f101dbea9c313d8b3a726dd42537606f07dcf24 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-111 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6009-6009; raw record sha256 8e15744b06810c8439f602de7e41efed45ba38fffe87cd0bc2e11fd95feec440 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-112 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6010-6010; raw record sha256 1c17df55f883cec73d8149e6463b591490d175c71250a379ea8a9faaeef24e08 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-113 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6011-6011; raw record sha256 02cb11d3982f5a83a420b960566ee9e1e277167ae4ffc07cd02cc0740a054ae3 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-114 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6012-6012; raw record sha256 6bff2fbff524825b0573f37be306dd5cdd7549e6ae21620d1cdc3ffa48f94e87 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-115 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6013-6013; raw record sha256 4578c4c72d3b65e96f55904e094b6aacc260b399d117e77a00a99ec0953206b9 | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-row-pubchem_bioassay-116 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6014-6014; raw record sha256 ccee7a003ee2164e7c4510dcd5841343dc99c5000b2a7306f14514417b8b103d | supports | Assigned retained-row reading of all 11 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2641-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2641-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2641-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2641-additional-0 | /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Exact assay identity exclusion decisions for selected/direct/comparison source context.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-1 | /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained unresolved-taxon diagnostic context used by the bounded curation scan; no fresh taxonomy, forward-merge decision or producer confirmation.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-2 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-6s8m-deposited-motor-tubulin-model.yaml; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Exact-owner referenced graph component, full raw/history; no flattening or transitive ownership transfer.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-3 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-7dae-deposited-tubulin-partner-model.yaml; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Exact-owner referenced graph component, full raw/history; no flattening or transitive ownership transfer.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-4 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-9pnd-deposited-tubulin-model.yaml; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Exact-owner referenced graph component, full raw/history; no flattening or transitive ownership transfer.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-5 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-kyc3013-proposed-biosynthetic-participants.yaml; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Exact-owner referenced graph component, full raw/history; no flattening or transitive ownership transfer.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-6 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-so0157-2-proposed-biosynthetic-participants.yaml; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Exact-owner referenced graph component, full raw/history; no flattening or transitive ownership transfer.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-7 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-soce90-proposed-biosynthetic-participants.yaml; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Exact-owner referenced graph component, full raw/history; no flattening or transitive ownership transfer.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-8 | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained explicit forward-merge table used by positive and negative taxon queries for each owner; historical route evidence only, no fresh taxonomy.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-9 | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_non_organism.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained non-organism table used by positive and negative taxon queries for each owner; diagnostic scope only, not a taxon verdict from file presence.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-10 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Maintained source-row identity/digest guard; text-only dependency.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-11 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/producer_strains.py; load_producer_strains lines 12-17; _load_qualifications lines 28-62; qualify_producer lines 65-68; _append_evidence lines 78-89 | context_only | Captured additional input role: Maintained producer-strain qualification implementation: source-row and digest predicate, strain-only CURATOR_INFERENCE scope; plaintext dependency, no execution or grade/taxon upgrade.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-12 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py; row_digest lines 19-23 only | context_only | Captured additional input role: Maintained row_digest implementation used by qualification guards: sorted ensure_ascii JSON digest only; input presence does not claim an audit or application of other structure-correction behavior.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-13 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/graph_components.py; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Future maintained complete-owner reader implementation; not invoked in this plan.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-additional-14 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/validation/write_validated.py; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Future maintained complete-owner reader implementation; not invoked in this plan.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2641-focal-assay-owner | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/0/owner_document/bioactivities/16; /records/0/owner_document/bioactivity_summary | supports | The exact delayed-death AID 504832 observation retains ACTIVE, OTHER, 0.0013 uM and ENZYME_INHIBITOR. The summary is retained but is not globally verified by this reading. |
| bgc-2641-other-enzyme-named-assays | /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json; /records/0/owner_document/bioactivities/18; /records/0/owner_document/bioactivities/19; /records/0/owner_document/bioactivities/20; /records/0/owner_document/bioactivities/21 | supports | NSD2 cellular-assay titles and two O96028 annotations are separate retained context. They do not establish direct inhibition/affinity, and the focal finding does not automatically delete the overall summary. |
| bgc-2641-assay-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 128-178: activity title patterns/classify_activity; lines 1310-1381: observations, numeric ordering, 25-cap and summary | supports | The generic inhibitors-of pattern supplies enzyme specificity to this delayed-death title. The maintained code separately preserves endpoint values, source provenance, written-observation order/cap and summary derivation. |
| bgc-2641-activity-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; BioactivityObservation; BioactivityClassEnum.ENZYME_INHIBITOR | supports | The observation class denotes enzyme inhibition; a general phenotypic inhibition title does not identify an enzyme or enzyme-specific endpoint. |
| bgc-2641-severity-rubric | /private/tmp/npm-record-reviews-20261021/docs/record-reviews.md; Verdict And Severity: major unsupported claims and scope inflation | supports | A materially unsupported enzyme-specific activity class is major evidence-scope inflation; measurement and identity are not challenged. |
| bgc-2641-component-0 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-soce90-proposed-biosynthetic-participants.yaml; Complete current component plaintext and curation_history; actual resolved graph 2 | supports | Exact-owner component content is wholly represented in the personally read accepted maintained view. Protein references, proposed roles, model geometry, histories and limitations are retained without fresh external verification. |
| bgc-2641-component-1 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-so0157-2-proposed-biosynthetic-participants.yaml; Complete current component plaintext and curation_history; actual resolved graph 3 | supports | Exact-owner component content is wholly represented in the personally read accepted maintained view. Protein references, proposed roles, model geometry, histories and limitations are retained without fresh external verification. |
| bgc-2641-component-2 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-kyc3013-proposed-biosynthetic-participants.yaml; Complete current component plaintext and curation_history; actual resolved graph 4 | supports | Exact-owner component content is wholly represented in the personally read accepted maintained view. Protein references, proposed roles, model geometry, histories and limitations are retained without fresh external verification. |
| bgc-2641-component-3 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-9pnd-deposited-tubulin-model.yaml; Complete current component plaintext and curation_history; actual resolved graph 5 | supports | Exact-owner component content is wholly represented in the personally read accepted maintained view. Protein references, proposed roles, model geometry, histories and limitations are retained without fresh external verification. |
| bgc-2641-component-4 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-6s8m-deposited-motor-tubulin-model.yaml; Complete current component plaintext and curation_history; actual resolved graph 6 | supports | Exact-owner component content is wholly represented in the personally read accepted maintained view. Protein references, proposed roles, model geometry, histories and limitations are retained without fresh external verification. |
| bgc-2641-component-5 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-7dae-deposited-tubulin-partner-model.yaml; Complete current component plaintext and curation_history; actual resolved graph 7 | supports | Exact-owner component content is wholly represented in the personally read accepted maintained view. Protein references, proposed roles, model geometry, histories and limitations are retained without fresh external verification. |
| bgc-2641-graph-0 | /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/0 | supports | Complete graph epothilone-b-epok-epoxidation: every description, node, edge, reference and qualifier was read. The local semantic scope is preserved, without transferring model membership to drug engagement or strain participation to experimentally established reaction order. |
| bgc-2641-graph-1 | /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/1 | supports | Complete graph epothilone-smp44-source-annotated-assembly: every description, node, edge, reference and qualifier was read. The local semantic scope is preserved, without transferring model membership to drug engagement or strain participation to experimentally established reaction order. |
| bgc-2641-graph-2 | /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/2 | supports | Complete graph epothilone-soce90-proposed-biosynthetic-participants: every description, node, edge, reference and qualifier was read. The local semantic scope is preserved, without transferring model membership to drug engagement or strain participation to experimentally established reaction order. |
| bgc-2641-graph-3 | /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/3 | supports | Complete graph epothilone-so0157-2-proposed-biosynthetic-participants: every description, node, edge, reference and qualifier was read. The local semantic scope is preserved, without transferring model membership to drug engagement or strain participation to experimentally established reaction order. |
| bgc-2641-graph-4 | /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/4 | supports | Complete graph epothilone-kyc3013-proposed-biosynthetic-participants: every description, node, edge, reference and qualifier was read. The local semantic scope is preserved, without transferring model membership to drug engagement or strain participation to experimentally established reaction order. |
| bgc-2641-graph-5 | /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/5 | supports | Complete graph epothilone-b-9pnd-deposited-tubulin-model: every description, node, edge, reference and qualifier was read. The local semantic scope is preserved, without transferring model membership to drug engagement or strain participation to experimentally established reaction order. |
| bgc-2641-graph-6 | /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/6 | supports | Complete graph epothilone-b-6s8m-deposited-motor-tubulin-model: every description, node, edge, reference and qualifier was read. The local semantic scope is preserved, without transferring model membership to drug engagement or strain participation to experimentally established reaction order. |
| bgc-2641-graph-7 | /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/7 | supports | Complete graph epothilone-b-7dae-deposited-tubulin-partner-model: every description, node, edge, reference and qualifier was read. The local semantic scope is preserved, without transferring model membership to drug engagement or strain participation to experimentally established reaction order. |
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
- AID 504832 class is the sole new finding; the source observation, value, activity call and other assay observations are not corrected or deleted by this review.
- The overall ENZYME_INHIBITOR summary has other retained enzyme-named assay context. Its complete scientific validity is not established, and automatic deletion is not prescribed.
- Historical model-partner wording is read with the later clarification: absence of an asserted target edge is not proof of biological non-target status.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T032248Z-epothilone-b
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: epothilone B'
started_at: '2026-11-06T02:22:01.261994Z'
finished_at: '2026-11-06T03:22:48.015991Z'
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
summary: 'Epothilone B has consistent retained ChEBI grounding and stereospecified
  molecular encodings. Its complete mechanism preserves a terminal EpoK step, qualified
  strain-specific assembly annotations and deposited tubulin-model contacts. One written
  assay has an unsupported enzyme-specific class: AID 504832 describes delayed parasite
  death without identifying an enzyme. This bounded class finding requires curation;
  the assay measurement and the separately scoped NSD2 observations remain intact.'
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
  - path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-6s8m-deposited-motor-tubulin-model.yaml
    sha256: 50e069de76894be19a1afe453f1cb19bb2531567f42274579a9ef17da83c62d7
    role: context
  - path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-7dae-deposited-tubulin-partner-model.yaml
    sha256: ad1bd45add3808a75f55bdbfa01115ecfebf69c9be2d9ce241346f8c688fcedd
    role: context
  - path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-9pnd-deposited-tubulin-model.yaml
    sha256: 77144f274ec203dcbf6674cb8c4871c311753c937848361661a21c019c281bf6
    role: context
  - path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-kyc3013-proposed-biosynthetic-participants.yaml
    sha256: c8b3acfbd6457b887c0ac0048b8e02f1166cbea5ab2ba13aad7b8ab7617db53e
    role: context
  - path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-so0157-2-proposed-biosynthetic-participants.yaml
    sha256: 8f5c1b7dd4675c24821fad86257a7aa4f741bd1594cf688b1c5cef37c24306ea
    role: context
  - path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-soce90-proposed-biosynthetic-participants.yaml
    sha256: 812d2a6d2845f1168293e039d0aa733a534d17906c9916741366a2f72d0d5315
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/unclassified/epothilone-b.yaml
    sha256: a1215767f42b2dac9bc371bf5a4046d2875b05dbf310eab9676d099c1fcb68b1
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
  - path: src/naturalproductmech/graph_components.py
    sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: src/naturalproductmech/validation/write_validated.py
    sha256: 4b7648fc5d2e7a5d26ad8bb168dbcae609aaa2694434a8ed5cfcb33fb66ff80a
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2641; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:31550
targets:
- target_id: CHEBI:31550
  path: data/natural_products/unclassified/epothilone-b.yaml
  label: epothilone B
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
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Exact assay identity exclusion decisions for selected/direct/comparison
      source context.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/unresolved_taxa.tsv
    role: Retained unresolved-taxon diagnostic context used by the bounded curation
      scan; no fresh taxonomy, forward-merge decision or producer confirmation.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-6s8m-deposited-motor-tubulin-model.yaml
    role: Exact-owner referenced graph component, full raw/history; no flattening
      or transitive ownership transfer.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-7dae-deposited-tubulin-partner-model.yaml
    role: Exact-owner referenced graph component, full raw/history; no flattening
      or transitive ownership transfer.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-9pnd-deposited-tubulin-model.yaml
    role: Exact-owner referenced graph component, full raw/history; no flattening
      or transitive ownership transfer.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-kyc3013-proposed-biosynthetic-participants.yaml
    role: Exact-owner referenced graph component, full raw/history; no flattening
      or transitive ownership transfer.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-so0157-2-proposed-biosynthetic-participants.yaml
    role: Exact-owner referenced graph component, full raw/history; no flattening
      or transitive ownership transfer.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-soce90-proposed-biosynthetic-participants.yaml
    role: Exact-owner referenced graph component, full raw/history; no flattening
      or transitive ownership transfer.
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
    role: Maintained source-row identity/digest guard; text-only dependency.
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
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/epothilone-b.yaml
    role: Curator-owned declared graphs, graph references, pathway steps and history;
      imported molecular-target assertions and other seeded fields retain inventory
      ownership. Curated graph/pathway changes require the validated writer and a
      curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-soce90-proposed-biosynthetic-participants.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-so0157-2-proposed-biosynthetic-participants.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-kyc3013-proposed-biosynthetic-participants.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-9pnd-deposited-tubulin-model.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-6s8m-deposited-motor-tubulin-model.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-7dae-deposited-tubulin-partner-model.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners. This mechanism-bearing owner requires separately
    authorized complete maintained resolution before scientific assessment and draft
    assembly. Raw owner capture is not a maintained resolved view.
checks:
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for epothilone-b
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch265/read-selected-mechanism-guarded-001.py
    2641 4993320737f70ad5b23965aab6f96a1047dee674c3a68d7794cae04976ffe7b1 945dfb7385f6abee91a084e0a47a62525860a1d7e4e67d5b4bcc3beb07687c8f
    1ac15b0876c39cb1ad596ebc8a6e5070e2c9a150a242dce750ba89e644c4cfcc e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
    d1603d86514a293c5635c5e7d1f781da78730105c54eb32526e72583a2065e01
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The accepted original reader preserves the complete owner and six ordered
    components, eight graphs, 52 nodes, 44 edges, one terminal step, 149 graph evidence
    placements, four step references and all histories.
  scope_note: One expected IPv6 socket-construction probe was denied before action;
    no request was sent. Complete preservation does not independently validate protein
    grounding, publications, natural identity or a full biosynthetic sequence.
  target_ids:
  - CHEBI:31550
  evidence_ids:
  - bgc-2641-reader-DATA
  - bgc-2641-reader-execution
  - bgc-2641-reader-acceptance
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:31550
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
  - CHEBI:31550
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
  - CHEBI:31550
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
  - CHEBI:31550
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
  - CHEBI:31550
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
  - CHEBI:31550
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:31550
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:31550
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2641-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/epothilone-b.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Complete current owner and all 12 history entries were personally read.
    Historical curator assertions do not confer fresh source-access credit.
  snapshot_sha256: a1215767f42b2dac9bc371bf5a4046d2875b05dbf310eab9676d099c1fcb68b1
- evidence_id: bgc-2641-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/0
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Actual complete owner capture preserves current local content; it is not
    an independent scientific validation.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2641-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/label;
    /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts;
    /records/0/owner_document/grounding_status
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Exact stored identity, source concepts, grounding and chemical encodings;
    natural identity is assessed separately.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2641-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/0/owner_document/curation_history
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: All 12 current history entries retain their original source and curation
    scope; no inherited paper access is claimed.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2641-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters;
    /records/0/owner_document/source_concepts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Owner-specific producer, locus and source-concept assertions preserve their
    distinct grades and references.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2641-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/0/owner_document/occurrences; /records/0/owner_document/bioactivities;
    /records/0/owner_document/xrefs
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: The selected occurrence, activity (when present) and cross-reference fields
    retain their distinct claim scopes. Occurrence or a cross-reference does not establish
    production, activity or mechanism.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2641-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_pathway; /records/0/owner_document/biosynthesis_origin;
    /records/0/owner_document/np_classification; /records/0/owner_document/bgc_class
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Recorded classification/model labels and BGC class content; exact source
    subclasses remain separately visible in the retained MIBiG row.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2641-mechanism-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/0/owner_document/causal_graphs; /records/0/owner_document/biosynthetic_pathway;
    /records/0/owner_document/discussions; /records/0/owner_document/causal_graph_refs
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: The complete captured raw owner retains two inline graphs, six declared
    component references, one numbered terminal step whose proposed field is absent,
    and the OPEN shared-structure discussion. The separately linked maintained-reader
    evidence contains all eight resolved graphs; no complete experimental pathway
    is inferred.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2641-reader-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json
  locator: /resolved_view; /counts; /returned_view_equals_expected_complete_owner;
    /denials; /limitations
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: The actual maintained view was personally read in full, including every
    graph, step, reference and history field. Exact preservation is distinct from
    biological or sequence verification.
  snapshot_sha256: bec91c77e5b6b3aadf1e79a36d84c8050b5b59af473100c7769534a62b097d93
- evidence_id: bgc-2641-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-reader-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /original_tools; /process_receipt
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: The original maintained-reader execution closed once with exit 0 and preserved
    genuine stdout/stderr and terminal objects.
  snapshot_sha256: f8b52a6cab1f11210e67fa8902b86b0ca9322c4df4e9bf7f5b628683b7faaeab
- evidence_id: bgc-2641-reader-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/root-native-reader-2641-acceptance-001.json
  locator: /accepted; /DATA; /execution; /verification; /review_check_contract; /scientific_limits
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: ROOT accepted this exact positive reader result. One expected IPv6 socket-construction
    probe was denied before action; no request was sent.
  snapshot_sha256: c96eee9871f33bcb8fa92b801e0a145e84bff49e80af3218e1df0556c0b8727e
- evidence_id: bgc-2641-reader-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-current265-Epothilone-B-maintained-view-reading-001.json
  locator: /complete_owner_read; /counts; /interpretations; /limits
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Independent scientific reading of the complete maintained owner preserves
    the qualified biosynthesis/model graphs, component histories and citation limits.
  snapshot_sha256: 0464d324fbe8c82f8d2d8ddc8085bc34f3c4569a4cca05adb8b6dd2d1a4ff9ba
- evidence_id: bgc-2641-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/intakes-001/2641-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Actual canonical inspection captures 52 current input hashes and complete
    target ownership declarations. Hash capture does not imply whole scientific reading
    of each input table.
  snapshot_sha256: 945dfb7385f6abee91a084e0a47a62525860a1d7e4e67d5b4bcc3beb07687c8f
- evidence_id: bgc-2641-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/root-intakes-acceptance-001.json
  locator: /accepted; /status; /summary
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: ROOT accepted the ten actual canonical inspections and their exact 458-input/69-path
    scope.
  snapshot_sha256: d9bfdc9fd488493604bd3b14e5b1ba99ce90cbb7c036b512cd67adb816b15a94
- evidence_id: bgc-2641-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-target-input-plan-001.json
  locator: /records/0; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: This owner has 52 exact planned inputs, now matched to its accepted actual
    canonical inspection; the full plan has 458 placements/69 paths.
  snapshot_sha256: 6c1c8151bfe6e5429970a5172b60f081cd00e0db37b52fe2f03baf22da2e3301
- evidence_id: bgc-2641-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/root-source-plan-acceptance-001.json
  locator: /accepted; /status; /plan
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: ROOT accepted the original local composed input plan; all current input
    paths and roles are preserved.
  snapshot_sha256: 8cba825369eb66a55a9be750e7a84ac29007c062f18d9631c4dc4a54094e2814
- evidence_id: bgc-2641-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Both complete saved forms, all atom/bond/ring/motif/stereo fields, comparisons
    and limited atom correspondence were personally read. No alternative parse was
    performed.
  snapshot_sha256: 58e6b7a2976ba940a3ac602a014f525360bc5c513c295bbfda1a597362dfb49c
- evidence_id: bgc-2641-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /status; /DATA; /execution
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: ROOT accepted the once-only offline diagnostic execution and saved outputs;
    this does not establish natural identity or full graph equivalence.
  snapshot_sha256: 2e9621e8613270d0e133b65ff7159a7d1d60517492cfc0a265e0e97a5a584fac
- evidence_id: bgc-2641-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /stdout; /stderr
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Actual diagnostic execution closed with exit 0 and preserved original stdout/stderr;
    no diagnostic replay was made.
  snapshot_sha256: a0a4b065cd2af9f176555009b9c7b42efdbf6e4234ee2fe8dade850db004f357
- evidence_id: bgc-2641-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The original diagnostic stderr contains four undefined-stereo warning blocks.
    They remain global and are not attributed to a particular owner or stored form.
  snapshot_sha256: 3571c04aece6b5ad4d3aa0f3c1cfa07ce5f070eec712da8b3ab4fac64d8601d2
- evidence_id: bgc-2641-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-current265-first-five-molecular-intake-reading-001.json
  locator: /records/0; /reading_attribution; /limitations
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Owner-specific complete saved-table reading and interpretation, with normalized
    identifiers distinguished from canonical correspondence and natural identity.
  snapshot_sha256: f17c7cc533377e3d9d05b2d791ce756dccdf85f090958e62f13550a1532221dd
- evidence_id: bgc-2641-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265/root-native-gates-acceptance-001.json
  locator: /checks_passed; /all_native_gates_passed; /unavailable_required_gates;
    /complete_selected_queue_rows
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Five local checks passed. Full QC and OAK remain unavailable, so native
    completion and scientific completion are not promoted.
  snapshot_sha256: 3785657c1cb4e0bb8f1fe2ba13ff7118fe0b0f937fd885ed29b3d5a128fcee55
- evidence_id: bgc-2641-source-reading
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-current265-assigned-source-reading-001.json
  locator: /records/1; /full_meaning_scope; /boundaries
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row meanings and all query metadata for this owner were
    read. References remain retained database assertions rather than newly inspected
    primary papers.
  snapshot_sha256: d93b851280e712f4f1f573637ddcfa386e6c915231bc3c1c221cc5c7c8fb04c5
- evidence_id: bgc-2641-source-notes
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Original 458-input/69-path source notes preserve disjoint positive-row
    reading credit 187 BGC + 38 Support + 0 Native. Actual intake acceptance is supported
    separately.
  snapshot_sha256: abb84f059d8a7c96b5c8ac546f5e0bffd8c82d929289b3adde72920d05cbc167
- evidence_id: bgc-2641-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/native-prep/native-current265-cached-taxonomy-reading-001.json
  locator: /context_interpretations/2; /interpretation
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: partial
  summary: Owner-local retained taxonomy routes, names and synonyms, with no current
    rank, lineage or freshness verification.
  snapshot_sha256: 84cfb0811e71455d15f59a8da5f322fdbc71fae1acf9cbec50d6741d6177efa1
- evidence_id: bgc-2641-curation
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
- evidence_id: bgc-2641-assay-curation
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
- evidence_id: bgc-2641-stereo-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: 'lines 392-396: stereo_complete description'
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The maintained flag describes undefined stereocentres; it does not by itself
    establish full double-bond geometric resolution.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2641-stereo-extractor
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters and undefined-tag predicate'
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The maintained extractor computes stereo_complete from unassigned tetrahedral
    chiral-centre tags. No extractor or molecule was rerun for this reading.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2641-stereo-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'line 995: direct stereo_complete copy'
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The maintained seeder copies the retained atom-centred boolean without
    independently resolving geometric stereochemistry.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2641-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/HARMONIZATION.md
  locator: 'lines 99-104: stereochemical completeness'
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: The documented retained stereocentre scope is separated from unknown original
    bond geometry and reconstruction-derived imine descriptors.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: bgc-2641-delegated-context-reading
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/support-prep/support-current265-assigned-source-reading-001.json
  locator: /contexts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: Support personally read the six complementary contexts, including the five
    last-half owners and Griseoviridin. This preserves attribution without adding
    BGC primary source-row credit or transferring activity between owners.
  snapshot_sha256: 29e3c5318905a2800b1953120011a91a94fbd48e8fdc594900a114697d6a75ba
- evidence_id: bgc-2641-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-target-input-plan-001.json
  locator: /records/0/proposed_companion_paths; /records/0/direct_companion_predicates
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: This owner has 0 immediate shared-BGC context input(s); the exact predicates
    do not establish equivalent identity, independent experimental evidence or source
    transfer.
  snapshot_sha256: 6c1c8151bfe6e5429970a5172b60f081cd00e0db37b52fe2f03baf22da2e3301
- evidence_id: bgc-2641-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete saved mibig_compounds query frame: 4 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
- evidence_id: bgc-2641-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 1114-1114; raw record sha256 5f918ca917d1b1e361f89faf27c9dcc21d1f4988535f2593f27e4e9ca81ec7f2
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 25 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2641-row-mibig_compounds-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 1115-1115; raw record sha256 7e7b43c0b8914455e974332099b35c3640609b54f9ad8c90c1cec26702372fd5
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 25 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2641-row-mibig_compounds-2
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 1116-1116; raw record sha256 0c82d326ca60fdf3ce8c36b2382c76a8ddab32c792185e0b2e04b6302a97f493
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 25 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2641-row-mibig_compounds-3
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 1117-1117; raw record sha256 7de8b344995475f6d692bde3b56df7cbcfb0aba30b81aef39cbd383b2856fc79
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 25 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2641-query-chebi_structures
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete saved chebi_structures query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
- evidence_id: bgc-2641-row-chebi_structures-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: physical lines 8008-8008; raw record sha256 b3b8ee23db09f5ac06106098539e6a24b357eb7cb1176cabac06d02d05a0e45c
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2641-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete saved lotus_occurrences query frame: 11 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
- evidence_id: bgc-2641-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7586-7586; raw record sha256 129259be5c1dd8295a76f70fa04ab72ffe2206cd513ed7cad9ffa69b25b0ea65
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-row-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7587-7587; raw record sha256 92e2ae70ea42f1ae24c09da73433021c30eb6e9d69150a4c8631a853080b4fb2
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-row-lotus_occurrences-2
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7588-7588; raw record sha256 a923ea114bbd131474b7120313b9363a75a754150836a382b67184437b9dd41d
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-row-lotus_occurrences-3
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7589-7589; raw record sha256 92436adc654ec3f1116fd3cb08e5a0748599c39043a905e265fbbc89b1b12d1a
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-row-lotus_occurrences-4
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7590-7590; raw record sha256 7f4454de52a3a0d51a7e18860878f68577d1e33ba469bb1c7f19f5270f58a9f6
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-row-lotus_occurrences-5
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7591-7591; raw record sha256 73d02d760963fcf8985261a12881e8b00b173453241c946a45035c0aa74bdbb1
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-row-lotus_occurrences-6
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7592-7592; raw record sha256 7fcf3ff6693b66604e5a7c818d45399eb5fbd6c7fd09dae18b93fc3826220ce3
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-row-lotus_occurrences-7
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7593-7593; raw record sha256 af7f2c33e8d6a25485d83116b8ec37ab959a6e83e1351cac406d8f26e55410ee
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-row-lotus_occurrences-8
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7594-7594; raw record sha256 27af5fe26b59ccb3bc1eb138d7109cbaf8aea6286d7eb7bc6cdef9f281014a87
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-row-lotus_occurrences-9
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7595-7595; raw record sha256 4ce178a7eda29c64f046f1801eeff946adf27003aefcf0141a6fe8c4b928815b
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-row-lotus_occurrences-10
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7596-7596; raw record sha256 7b2ed19ddeb2a1e4296ce1eb8ecbe1651bbfb1574ea3f944ef078d040c8bee4f
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2641-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
  search_scope: '{"context_path": "data/natural_products/unclassified/epothilone-b.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "QXRSDHAAWVKZLJ-PVYNADRNSA-N", "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2641-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete saved npclassifier query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
- evidence_id: bgc-2641-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2060-2060; raw record sha256 93b8c7ba42986bbf869c29d415571f4ef2799e16f49475c9d23cab967e4e3064
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 7 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2641-query-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay query frame: 117 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
- evidence_id: bgc-2641-row-pubchem_bioassay-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5898-5898; raw record sha256 450ecf3be3a719425ec7cd41cc2633a6f3e4d6de6daf20fcc8ebf46bae696ebd
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5899-5899; raw record sha256 e3a9109fd6a1fd3260162e2b348dd2d464d1e1898ab91903aac2d97dc7283e2b
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-2
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5900-5900; raw record sha256 26158ac31134080466fd9aa57f919c5f0e2c3cae589dc678f3a7957d8c59d89d
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-3
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5901-5901; raw record sha256 a04e4e4a2319a36224dfef54c9fa3b85f4e81453eeac437cfb0579077808cf64
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-4
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5902-5902; raw record sha256 c07f51e239293d6f708b43571f79a9d3ef1db62672d1dcd73fe9029f64a1ddb9
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-5
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5903-5903; raw record sha256 16fdcece1d51af880490a32c3d5138e031a555e394a7710c6a73773b9b252ec1
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-6
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5904-5904; raw record sha256 4e5cabfb0843aa52c2130d70959ac597374a21e034c8c67ba7b8b91bd751ad28
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-7
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5905-5905; raw record sha256 90fab1d53a32dfa74d6394957fe679080673d109f874fcfbe94c58c2c4a779fe
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-8
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5906-5906; raw record sha256 6a86bc520c5b80079bdd884c081efe5ad5dc4d57e4538deb13ae5ab2035fde6f
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-9
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5907-5907; raw record sha256 8fa2beec5ef5eb06c4c6d04c89659a2648d2c2fcaf72848dda685ff11c72b86d
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-10
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5908-5908; raw record sha256 a5f150f2851e091314936bb4872a608b308e5ddd2ba9a8ccb35ab07855f9db96
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-11
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5909-5909; raw record sha256 73a99ce9b92c743e43005888e37354f0e831d701005814318d3c7984363567dd
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-12
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5910-5910; raw record sha256 bde5c0020f1a20782682d88c1722935adf16c31fbae5669d14176c2e47fc0d15
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-13
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5911-5911; raw record sha256 973670b9c05beb9eebdc50e2e4ebe761e52cf9b664f59e4a8e6da04631ce4bc9
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-14
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5912-5912; raw record sha256 2b5fc3146f42ad9d29431c30cc13a313c1460a8dc9e9a8f1fa90f4605e092473
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-15
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5913-5913; raw record sha256 c3610138460ccd946cf471e78100741e72e33ade3d0c7b64b47f3c345dcbd6ff
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-16
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5914-5914; raw record sha256 b1ef0f78848b40e8681df4609d7c7daf340b905e69fd1f082803ddfb06850023
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-17
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5915-5915; raw record sha256 72a5e4943a05cb645a74ba9b9feca1c8a8d4772fa4bde2a303e0a8172c9ad448
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-18
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5916-5916; raw record sha256 29a5c664db570b56fa28c33c41bb28dd20ca35eed3762a033ede9cba955c3e8d
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-19
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5917-5917; raw record sha256 47744a81fb785bdf1d787f264ea116ec57c931552004a91045a0360f3ea9285f
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-20
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5918-5918; raw record sha256 18d46a121c6925c8440c93d3c357ba2bd73b43bcb397ec272642c3b263b4c85a
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-21
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5919-5919; raw record sha256 f8e8074df8923730f67a14ac1a8cca57e25ff406fe82be2e89f28701cefc8219
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-22
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5920-5920; raw record sha256 8825a6ac52ba00bc33ae08abdbebda24e2493e3e8bafb0b24956f6103f3a58fe
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-23
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5921-5921; raw record sha256 0e757e82bd32b1ba720748310c675702c29188dcbf76f16f41055395de9bc601
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-24
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5922-5922; raw record sha256 34356c1f31da7a4ffc1d51d0e8df1e20af17a7c409158f573d81a4758920a36b
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-25
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5923-5923; raw record sha256 bfb293d68eef33e896a0b660974a26d2324dec3f77be48cc97889ba090213972
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-26
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5924-5924; raw record sha256 4ee90a0b437d2822f2b64814d99ceb4046f75d0d5bb76321c46be3f5307498b7
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-27
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5925-5925; raw record sha256 c141d95dd952a21eb0d080d0093bf031eba48b521fa162ae73b09eb531348820
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-28
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5926-5926; raw record sha256 1df1ce662597d3c5e4aaa5db257b073f5f524848eb7cdc79ed3b125e8a7e649a
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-29
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5927-5927; raw record sha256 2876b3905671fcbecc3a4ea7dd3d7e134d2c27091bc0c865c2afd8c58083b216
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-30
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5928-5928; raw record sha256 7fbcfcff7e69c87ecbc37cc5844b0acb8ec8ddef955965c247c44d6ce35d8211
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-31
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5929-5929; raw record sha256 be2954579c1a2b6ed49ce868cdd9a971c0c4468e7fe2879bad3506af8da639d8
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-32
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5930-5930; raw record sha256 6cd6dd1470ab572c4f26aa1e3ecc7763ea52cc6578fc47935fe5d3f27dd1055f
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-33
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5931-5931; raw record sha256 4ec9b60be4e827f8423e85c45065414dd0253b3de351a13f649cfe804cfa13dc
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-34
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5932-5932; raw record sha256 99f52756f1ca54a01559776b86333aa3cecf9807337c6047cd932222d1d7e6ef
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-35
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5933-5933; raw record sha256 9d79932da845c710890b46ff0930ab1164dfb23d6f4ada361bd57c602430dd64
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-36
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5934-5934; raw record sha256 b661eadba99725c90c16d72f7d3777fbf60b78cd6a8bc77b8763cad917b3fab0
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-37
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5935-5935; raw record sha256 fdb36296e593c125eeb8ead3afd0fbf4a74e8e205d6baa4ed6fa41c54fc1a8f8
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-38
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5936-5936; raw record sha256 c52f1ab123ce2f7ba23bc40ea811ed3f6f565b5c8ab679bf059d31662d200f1e
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-39
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5937-5937; raw record sha256 bcf46c68e453eefbd668f1205567e7defa198d4dca2135e6f103190dce6d0674
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-40
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5938-5938; raw record sha256 88071946066701a2b0bb2976b2f2cd4ef23d83992c99bb42564203ba0c055fca
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-41
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5939-5939; raw record sha256 feb0bb85be85e67007c1cfb41f995de4d9bc67eebf28cfd1e363124cde4abb84
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-42
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5940-5940; raw record sha256 02b21767b26635409972f3cf5a1fd5e40a588aa2d56f8fff2336eee8f68372ac
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-43
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5941-5941; raw record sha256 1ad99ab95ade85f7e5dcbfbb078a8e294c9915e6e442dc0e5c72b0b74b5a8a36
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-44
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5942-5942; raw record sha256 be14060565b3cb24206357849c607b600f52abd22e5a94f39cecb88889551f97
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-45
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5943-5943; raw record sha256 73ef51ccadf15fad3d97cff32c59a26a947248354ca786e771425c41c0351a7d
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-46
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5944-5944; raw record sha256 9623a5d3d02cb7c2a5b999bc7aae29131fe4f2e3224ee86092126a744273c2f7
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-47
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5945-5945; raw record sha256 0acb22b97c405c2899e892b17b8aeb5806f120846379d3566ef6f2bf84dd135b
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-48
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5946-5946; raw record sha256 c483ed4d6635362a6df11e10876915ca59722cac0580f8f03eb91f622e765b4e
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-49
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5947-5947; raw record sha256 096f7426350dd072921dc0e21aab6b5e694957c8b0817a29ec400b2db70bdcd4
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-50
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5948-5948; raw record sha256 6ae29e20088d5dfec11461fe3909d9941457072a36b25d7fa5643a767fafd71a
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-51
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5949-5949; raw record sha256 f01a893f0d9c5f8e335fb1f3810f44ab67cbe25901f31b1e54050e477c240bb7
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-52
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5950-5950; raw record sha256 64936c16fee91021ca7b685aa003dc7b45c0850c0dfafa7962b4ed07e34708b9
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-53
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5951-5951; raw record sha256 4b4351dadd21025ae7aacdae204c6151247512b171c4a2286faeade5606c4525
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-54
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5952-5952; raw record sha256 d7480821160ad4a9bf6c06af25584e8135f235466a87251cd59a30941aa6a29d
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-55
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5953-5953; raw record sha256 333a5a94fd03d4e62740d0466591112562b878d3c75f18f26eee82ac703e4488
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-56
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5954-5954; raw record sha256 14283ebfa2743ef5901884bfd7a5aec186b417d8f6ebdf7b140ef362d426d176
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-57
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5955-5955; raw record sha256 0c845aa1d7bca96159ad7df2d41e6cd4e015fdfd14e8670f57a00c56541cbd05
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-58
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5956-5956; raw record sha256 0e2c8dfb2a3ffb513f7319e5370d7a7c4a6f995a349575b049687028d8b607af
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-59
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5957-5957; raw record sha256 2d29b53158300d24b7327c0789370e061f92d5f84244d5084ec88c5be3341f93
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-60
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5958-5958; raw record sha256 640812cdb0dc94c0900567e7c908062bfcbf8d4d5871e02bbebc031b4de6e3f3
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-61
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5959-5959; raw record sha256 b00b4aee47800ef3f8ffffb2a5011c9b45740cb2342da150de938d80dc7b330a
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-62
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5960-5960; raw record sha256 7a181456a2e4cc451b3a451b19c079096986275b3a38bda551350a59b495fde4
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-63
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5961-5961; raw record sha256 078dff037ca246668cd5261ed606b671b6441c2526514bb4ac020144e3746032
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-64
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5962-5962; raw record sha256 2547d02404ec28fd2a8d88cffd45714d1737680a73bcaa953cfcf53a7748c188
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-65
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5963-5963; raw record sha256 38282118db2c6386d00bf8b157390d20dc20cca623c10b08c1d4452bc04b37ce
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-66
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5964-5964; raw record sha256 14b4423b5efc6a4b68aed0abb27f76ac9ff95f6813be8afe3197d21054b79bd6
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-67
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5965-5965; raw record sha256 cab0559fc129bdc699a8390ba2d19f1223b7c7fc8b17fa08dd7e53d5aea8f9b9
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-68
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5966-5966; raw record sha256 554f1c56339f29bac26f9ddd0dd5d9ada3e0037b09b9e897390ddbc164584b40
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-69
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5967-5967; raw record sha256 349d0634b8e2f1ab336fa542765402d0337bad14b19693363aecca3491e58da7
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-70
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5968-5968; raw record sha256 b19b3b3f35bfe5b4a77771f9eb701602d112adf75a997d8de08342066bb87f33
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-71
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5969-5969; raw record sha256 847dd0ae31db8067201f57acffb24ee9e451b77ec80540a12d9956e1c3c0524e
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-72
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5970-5970; raw record sha256 0aa78c6ff49554eb0012a9a4ff5e4fe06948c19200b22949e183026ef1085b1e
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-73
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5971-5971; raw record sha256 74470905babd22b96200ee63cdb40d8d9d31793a200692e7f519969f4fa03f25
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-74
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5972-5972; raw record sha256 0ca55b31a0359308b8330eb933d9260f78bd25e81f8b221bab775e3fb5d3e58c
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-75
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5973-5973; raw record sha256 d3d5aa9b86320ac2068f6e6fb152054bc80543aac5f4338d6d72c293787556f3
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-76
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5974-5974; raw record sha256 02544239e71e3cd574c9e6f9d5ece54c6f1ebf1554fdd1d0a56d08e5eb7467e9
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-77
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5975-5975; raw record sha256 ba2b784ef45831a670506f72a22f07c5eb7cc72f6d4d9c15954c6697cbf455f7
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-78
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5976-5976; raw record sha256 943a76331ad0e5da8b346ede6c4ae44a4546e25c5fd0aff6e0ab6854b3b2a4d0
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-79
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5977-5977; raw record sha256 6eaa00e6d4521540e8daa448a536ae31fc44c016b764d4a7574d4cbc568d65b6
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-80
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5978-5978; raw record sha256 a3ff8f1f57138445c20ee3c76783aa7b4de77ac20d6ae05964fa66d9a301e7f0
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-81
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5979-5979; raw record sha256 0de403d212c9e60a6c96f1ce730b794444da01b8d28f3df13862eff57170c788
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-82
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5980-5980; raw record sha256 cd7338c00cb2e2d21f450c0f1a8544b0c20ebb1928cf3a69692944f1ae0ec64c
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-83
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5981-5981; raw record sha256 0f3d9a9143cebb4ce0307c38116902bb1e040a6d9d10456dcb437c2ad2e54d69
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-84
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5982-5982; raw record sha256 128568060ff228c14a45180f0e22b99c5d7e4070fe47dc34f65b5bebd0432964
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-85
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5983-5983; raw record sha256 27734e8e0623a7d890aea527ff26cd6f8f353db04142aa870a3a86223f3e88f4
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-86
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5984-5984; raw record sha256 9344602355f839e54a1b058b399eafc4a71948e7274afc12abd163acab7fa03c
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-87
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5985-5985; raw record sha256 eb8b18ab0b6a9c1870dd6e06e7cf90134e2ca183d67fd8a9d8456682a903e5c4
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-88
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5986-5986; raw record sha256 e5ae7cdc683be5daef55d748d7bed55b5e71c817d240f09104468192e9e30f1c
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-89
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5987-5987; raw record sha256 6f00eca47565d880402b24d428681669e6dd995de121e916839d68aea0510c10
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-90
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5988-5988; raw record sha256 de2108c18b02fa07c956fc85c89ac749fcfbb2080a1a05d9a2110bf51d3316da
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-91
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5989-5989; raw record sha256 d98bd1fdcb93bfdd539c8d5d48e63c40cfddcdbf0f1effc77196c36255cead30
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-92
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5990-5990; raw record sha256 32fb23b18fc7d436c971b2a931ebb1ba5cfc3dd5f5ff5222d1384cb14bca6d26
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-93
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5991-5991; raw record sha256 d16afae1786795fb6baf26e51cd6be4a9091216b0b041a5e0155153501b9b9cf
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-94
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5992-5992; raw record sha256 5bf3ce701c349a375b6c7b2341fa80a57414f72fd5f69a897a72075f83b93ff5
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-95
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5993-5993; raw record sha256 a2adccf6374eb33354a5a455e729a8be9ff6b0a2e19eee41d1eff20552010bb3
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-96
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5994-5994; raw record sha256 597e217902e2cae485c6bf35a6188e17a88071deb97576c8bc2d004bc70e4aa3
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-97
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5995-5995; raw record sha256 6f3be4eea1dafb8aa3c5da82911493df42ca26a729ee6fc6e8bb607680d35dc2
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-98
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5996-5996; raw record sha256 220e4d9d57ff3b30e22f871d8efb84a2be94641e315493358a4b6c8771de50d5
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-99
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5997-5997; raw record sha256 35de9acdecd7a7ca86fc5451b24114319fda5aa2c2b2c51b25f31c94aa1ae1f6
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-100
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5998-5998; raw record sha256 aa4dc9f8dc8104909042990c9c473290f2c83e013e5f9c752da1c01e3158925f
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-101
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 5999-5999; raw record sha256 91c95e3f907508aa7599a4b75a1d8df474c48aa949443830a03c5bebac947c16
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-102
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6000-6000; raw record sha256 1f3815fe3304a4c882ca29bbaebad262b9bf371823ac55bbf02894dfffa7635d
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-103
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6001-6001; raw record sha256 df593e76124d749f32ead6fd40eb7d75cf74ca801f833a6e664e715b9128a206
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-104
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6002-6002; raw record sha256 04a1f973910c19eccebaf757c977d24805741f5ab4eb6579ccd4c475a913ca5f
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-105
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6003-6003; raw record sha256 4a752783f5ec1e6c5031f148710a7b34e23a5f4fdbb76913a22ed7808d496b17
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-106
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6004-6004; raw record sha256 6e88d0eea37c53461edca96a6cca2306327d8973547193cc3c07274205b5dd3f
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-107
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6005-6005; raw record sha256 f92c28f54e6aa51daa86b60079dd0ff4ef51233c0638ed977da32334ea0124f0
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-108
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6006-6006; raw record sha256 0a9546716d88aaff5f5ef88550a3e004cfc4fb76f256ed1478f80b7dcd387c20
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-109
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6007-6007; raw record sha256 163c3a36586a8fd7eeb5898ed242e995d730edaa4087945a5223cdf98478efa6
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-110
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6008-6008; raw record sha256 ae87c595d66db84c60fecef96f101dbea9c313d8b3a726dd42537606f07dcf24
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-111
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6009-6009; raw record sha256 8e15744b06810c8439f602de7e41efed45ba38fffe87cd0bc2e11fd95feec440
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-112
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6010-6010; raw record sha256 1c17df55f883cec73d8149e6463b591490d175c71250a379ea8a9faaeef24e08
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-113
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6011-6011; raw record sha256 02cb11d3982f5a83a420b960566ee9e1e277167ae4ffc07cd02cc0740a054ae3
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-114
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6012-6012; raw record sha256 6bff2fbff524825b0573f37be306dd5cdd7549e6ae21620d1cdc3ffa48f94e87
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-115
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6013-6013; raw record sha256 4578c4c72d3b65e96f55904e094b6aacc260b399d117e77a00a99ec0953206b9
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-row-pubchem_bioassay-116
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6014-6014; raw record sha256 ccee7a003ee2164e7c4510dcd5841343dc99c5000b2a7306f14514417b8b103d
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Assigned retained-row reading of all 11 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2641-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
  search_scope: '{"context_path": "data/natural_products/unclassified/epothilone-b.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "QXRSDHAAWVKZLJ-PVYNADRNSA-N", "table": "bindingdb_targets"}'
- evidence_id: bgc-2641-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
  search_scope: '{"context_path": "data/natural_products/unclassified/epothilone-b.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "QXRSDHAAWVKZLJ-PVYNADRNSA-N", "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2641-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch265-tentative/bgc-prep/bgc-conditional265-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Complete saved chebi_origins query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: 06a153005b0b83be8e74f277a0ea887401e5c05945eabd70522d38e19ab91174
  search_scope: '{"context_path": "data/natural_products/unclassified/epothilone-b.yaml",
    "matches": 0, "predicate": "exact chebi_id from exact full-key structure rows",
    "query": ["CHEBI:31550"], "table": "chebi_origins"}'
- evidence_id: bgc-2641-additional-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Exact assay identity exclusion decisions
    for selected/direct/comparison source context.. File presence itself confers no
    positive source-row, AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
- evidence_id: bgc-2641-additional-1
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
- evidence_id: bgc-2641-additional-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-6s8m-deposited-motor-tubulin-model.yaml
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Exact-owner referenced graph component,
    full raw/history; no flattening or transitive ownership transfer.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: 50e069de76894be19a1afe453f1cb19bb2531567f42274579a9ef17da83c62d7
- evidence_id: bgc-2641-additional-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-7dae-deposited-tubulin-partner-model.yaml
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Exact-owner referenced graph component,
    full raw/history; no flattening or transitive ownership transfer.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: ad1bd45add3808a75f55bdbfa01115ecfebf69c9be2d9ce241346f8c688fcedd
- evidence_id: bgc-2641-additional-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-9pnd-deposited-tubulin-model.yaml
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Exact-owner referenced graph component,
    full raw/history; no flattening or transitive ownership transfer.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: 77144f274ec203dcbf6674cb8c4871c311753c937848361661a21c019c281bf6
- evidence_id: bgc-2641-additional-5
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-kyc3013-proposed-biosynthetic-participants.yaml
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Exact-owner referenced graph component,
    full raw/history; no flattening or transitive ownership transfer.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: c8b3acfbd6457b887c0ac0048b8e02f1166cbea5ab2ba13aad7b8ab7617db53e
- evidence_id: bgc-2641-additional-6
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-so0157-2-proposed-biosynthetic-participants.yaml
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Exact-owner referenced graph component,
    full raw/history; no flattening or transitive ownership transfer.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: 8f5c1b7dd4675c24821fad86257a7aa4f741bd1594cf688b1c5cef37c24306ea
- evidence_id: bgc-2641-additional-7
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-soce90-proposed-biosynthetic-participants.yaml
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Exact-owner referenced graph component,
    full raw/history; no flattening or transitive ownership transfer.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: 812d2a6d2845f1168293e039d0aa733a534d17906c9916741366a2f72d0d5315
- evidence_id: bgc-2641-additional-8
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
- evidence_id: bgc-2641-additional-9
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
- evidence_id: bgc-2641-additional-10
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Maintained source-row identity/digest
    guard; text-only dependency.. File presence itself confers no positive source-row,
    AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
- evidence_id: bgc-2641-additional-11
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
- evidence_id: bgc-2641-additional-12
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
- evidence_id: bgc-2641-additional-13
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/graph_components.py
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Future maintained complete-owner reader
    implementation; not invoked in this plan.. File presence itself confers no positive
    source-row, AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
- evidence_id: bgc-2641-additional-14
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/validation/write_validated.py
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: context_only
  summary: 'Captured additional input role: Future maintained complete-owner reader
    implementation; not invoked in this plan.. File presence itself confers no positive
    source-row, AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: 4b7648fc5d2e7a5d26ad8bb168dbcae609aaa2694434a8ed5cfcb33fb66ff80a
- evidence_id: bgc-2641-focal-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/0/owner_document/bioactivities/16; /records/0/owner_document/bioactivity_summary
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: The exact delayed-death AID 504832 observation retains ACTIVE, OTHER, 0.0013
    uM and ENZYME_INHIBITOR. The summary is retained but is not globally verified
    by this reading.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2641-other-enzyme-named-assays
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/owner-capture-DATA-001.json
  locator: /records/0/owner_document/bioactivities/18; /records/0/owner_document/bioactivities/19;
    /records/0/owner_document/bioactivities/20; /records/0/owner_document/bioactivities/21
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: NSD2 cellular-assay titles and two O96028 annotations are separate retained
    context. They do not establish direct inhibition/affinity, and the focal finding
    does not automatically delete the overall summary.
  snapshot_sha256: e2712308ebe6492456f1f40313345d3067eae61ba4dfa09034c66d55a50b64de
- evidence_id: bgc-2641-assay-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines 128-178: activity title patterns/classify_activity; lines 1310-1381:
    observations, numeric ordering, 25-cap and summary'
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: The generic inhibitors-of pattern supplies enzyme specificity to this delayed-death
    title. The maintained code separately preserves endpoint values, source provenance,
    written-observation order/cap and summary derivation.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2641-activity-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: BioactivityObservation; BioactivityClassEnum.ENZYME_INHIBITOR
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: The observation class denotes enzyme inhibition; a general phenotypic inhibition
    title does not identify an enzyme or enzyme-specific endpoint.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2641-severity-rubric
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-reviews.md
  locator: 'Verdict And Severity: major unsupported claims and scope inflation'
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: A materially unsupported enzyme-specific activity class is major evidence-scope
    inflation; measurement and identity are not challenged.
  snapshot_sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
- evidence_id: bgc-2641-component-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-soce90-proposed-biosynthetic-participants.yaml
  locator: Complete current component plaintext and curation_history; actual resolved
    graph 2
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Exact-owner component content is wholly represented in the personally read
    accepted maintained view. Protein references, proposed roles, model geometry,
    histories and limitations are retained without fresh external verification.
  snapshot_sha256: 812d2a6d2845f1168293e039d0aa733a534d17906c9916741366a2f72d0d5315
- evidence_id: bgc-2641-component-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-so0157-2-proposed-biosynthetic-participants.yaml
  locator: Complete current component plaintext and curation_history; actual resolved
    graph 3
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Exact-owner component content is wholly represented in the personally read
    accepted maintained view. Protein references, proposed roles, model geometry,
    histories and limitations are retained without fresh external verification.
  snapshot_sha256: 8f5c1b7dd4675c24821fad86257a7aa4f741bd1594cf688b1c5cef37c24306ea
- evidence_id: bgc-2641-component-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-kyc3013-proposed-biosynthetic-participants.yaml
  locator: Complete current component plaintext and curation_history; actual resolved
    graph 4
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Exact-owner component content is wholly represented in the personally read
    accepted maintained view. Protein references, proposed roles, model geometry,
    histories and limitations are retained without fresh external verification.
  snapshot_sha256: c8b3acfbd6457b887c0ac0048b8e02f1166cbea5ab2ba13aad7b8ab7617db53e
- evidence_id: bgc-2641-component-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-9pnd-deposited-tubulin-model.yaml
  locator: Complete current component plaintext and curation_history; actual resolved
    graph 5
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Exact-owner component content is wholly represented in the personally read
    accepted maintained view. Protein references, proposed roles, model geometry,
    histories and limitations are retained without fresh external verification.
  snapshot_sha256: 77144f274ec203dcbf6674cb8c4871c311753c937848361661a21c019c281bf6
- evidence_id: bgc-2641-component-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-6s8m-deposited-motor-tubulin-model.yaml
  locator: Complete current component plaintext and curation_history; actual resolved
    graph 6
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Exact-owner component content is wholly represented in the personally read
    accepted maintained view. Protein references, proposed roles, model geometry,
    histories and limitations are retained without fresh external verification.
  snapshot_sha256: 50e069de76894be19a1afe453f1cb19bb2531567f42274579a9ef17da83c62d7
- evidence_id: bgc-2641-component-5
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/QXRSDHAAWVKZLJ-PVYNADRNSA-N/epothilone-b-7dae-deposited-tubulin-partner-model.yaml
  locator: Complete current component plaintext and curation_history; actual resolved
    graph 7
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: Exact-owner component content is wholly represented in the personally read
    accepted maintained view. Protein references, proposed roles, model geometry,
    histories and limitations are retained without fresh external verification.
  snapshot_sha256: ad1bd45add3808a75f55bdbfa01115ecfebf69c9be2d9ce241346f8c688fcedd
- evidence_id: bgc-2641-graph-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/0
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete graph epothilone-b-epok-epoxidation: every description, node,
    edge, reference and qualifier was read. The local semantic scope is preserved,
    without transferring model membership to drug engagement or strain participation
    to experimentally established reaction order.'
  snapshot_sha256: bec91c77e5b6b3aadf1e79a36d84c8050b5b59af473100c7769534a62b097d93
- evidence_id: bgc-2641-graph-1
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/1
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete graph epothilone-smp44-source-annotated-assembly: every description,
    node, edge, reference and qualifier was read. The local semantic scope is preserved,
    without transferring model membership to drug engagement or strain participation
    to experimentally established reaction order.'
  snapshot_sha256: bec91c77e5b6b3aadf1e79a36d84c8050b5b59af473100c7769534a62b097d93
- evidence_id: bgc-2641-graph-2
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/2
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete graph epothilone-soce90-proposed-biosynthetic-participants: every
    description, node, edge, reference and qualifier was read. The local semantic
    scope is preserved, without transferring model membership to drug engagement or
    strain participation to experimentally established reaction order.'
  snapshot_sha256: bec91c77e5b6b3aadf1e79a36d84c8050b5b59af473100c7769534a62b097d93
- evidence_id: bgc-2641-graph-3
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/3
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete graph epothilone-so0157-2-proposed-biosynthetic-participants:
    every description, node, edge, reference and qualifier was read. The local semantic
    scope is preserved, without transferring model membership to drug engagement or
    strain participation to experimentally established reaction order.'
  snapshot_sha256: bec91c77e5b6b3aadf1e79a36d84c8050b5b59af473100c7769534a62b097d93
- evidence_id: bgc-2641-graph-4
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/4
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete graph epothilone-kyc3013-proposed-biosynthetic-participants:
    every description, node, edge, reference and qualifier was read. The local semantic
    scope is preserved, without transferring model membership to drug engagement or
    strain participation to experimentally established reaction order.'
  snapshot_sha256: bec91c77e5b6b3aadf1e79a36d84c8050b5b59af473100c7769534a62b097d93
- evidence_id: bgc-2641-graph-5
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/5
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete graph epothilone-b-9pnd-deposited-tubulin-model: every description,
    node, edge, reference and qualifier was read. The local semantic scope is preserved,
    without transferring model membership to drug engagement or strain participation
    to experimentally established reaction order.'
  snapshot_sha256: bec91c77e5b6b3aadf1e79a36d84c8050b5b59af473100c7769534a62b097d93
- evidence_id: bgc-2641-graph-6
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/6
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete graph epothilone-b-6s8m-deposited-motor-tubulin-model: every
    description, node, edge, reference and qualifier was read. The local semantic
    scope is preserved, without transferring model membership to drug engagement or
    strain participation to experimentally established reaction order.'
  snapshot_sha256: bec91c77e5b6b3aadf1e79a36d84c8050b5b59af473100c7769534a62b097d93
- evidence_id: bgc-2641-graph-7
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch265/native-current265-epothilone-b-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/7
  accessed_at: '2026-11-06T03:15:30.257607Z'
  support: supports
  summary: 'Complete graph epothilone-b-7dae-deposited-tubulin-partner-model: every
    description, node, edge, reference and qualifier was read. The local semantic
    scope is preserved, without transferring model membership to drug engagement or
    strain participation to experimentally established reaction order.'
  snapshot_sha256: bec91c77e5b6b3aadf1e79a36d84c8050b5b59af473100c7769534a62b097d93
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
- assessment_id: bgc-2641-identity
  area: identity
  topic: identity
  outcome: supported
  summary: CHEBI:31550 is retained EXACT grounding. Both saved forms regenerate QXRSDHAAWVKZLJ-PVYNADRNSA-N,
    C27H41NO6S and net charge 0, with identical canonical strings. The retained ChEBI
    definition describes the epoxide derived from epothilone D, and four MIBiG compound
    rows agree with the encoded structure. These support local encoded and database
    consistency. The OPEN four-entry shared-structure discussion remains unresolved;
    normalized agreement does not independently characterize natural or engineered
    products.
  target_ids:
  - CHEBI:31550
  evidence_ids:
  - bgc-2641-identity
  - bgc-2641-chemistry
  - bgc-2641-diagnostic-acceptance
  - bgc-2641-query-mibig_compounds
  - bgc-2641-query-chebi_structures
  - bgc-2641-query-antibioticmech_inchikeys
  - bgc-2641-direct-contexts
  - bgc-2641-row-mibig_compounds-0
  - bgc-2641-row-mibig_compounds-1
  - bgc-2641-row-mibig_compounds-2
  - bgc-2641-row-mibig_compounds-3
  - bgc-2641-row-chebi_structures-0
  - bgc-2641-reader-DATA
  - bgc-2641-reader-execution
  - bgc-2641-reader-acceptance
  - bgc-2641-reader-reading
  - bgc-2641-delegated-context-reading
  dimensions:
  - name: standard_inchi_key
    value: QXRSDHAAWVKZLJ-PVYNADRNSA-N; both normalized regenerations agree
    definition: Literal retained full key and accepted saved regeneration scope.
    evidence_ids:
    - bgc-2641-identity
    - bgc-2641-chemistry
    - bgc-2641-diagnostic-acceptance
    - bgc-2641-query-mibig_compounds
    - bgc-2641-query-chebi_structures
    - bgc-2641-query-antibioticmech_inchikeys
    - bgc-2641-direct-contexts
    - bgc-2641-row-mibig_compounds-0
    - bgc-2641-row-mibig_compounds-1
    - bgc-2641-row-mibig_compounds-2
    - bgc-2641-row-mibig_compounds-3
    - bgc-2641-row-chebi_structures-0
    - bgc-2641-reader-DATA
    - bgc-2641-reader-execution
    - bgc-2641-reader-acceptance
    - bgc-2641-reader-reading
    - bgc-2641-delegated-context-reading
  - name: grounding_scope
    value: EXACT CHEBI:31550; natural identity not independently established
    definition: Recorded grounding category, separated from independent natural identity.
    evidence_ids:
    - bgc-2641-identity
    - bgc-2641-chemistry
    - bgc-2641-diagnostic-acceptance
    - bgc-2641-query-mibig_compounds
    - bgc-2641-query-chebi_structures
    - bgc-2641-query-antibioticmech_inchikeys
    - bgc-2641-direct-contexts
    - bgc-2641-row-mibig_compounds-0
    - bgc-2641-row-mibig_compounds-1
    - bgc-2641-row-mibig_compounds-2
    - bgc-2641-row-mibig_compounds-3
    - bgc-2641-row-chebi_structures-0
    - bgc-2641-reader-DATA
    - bgc-2641-reader-execution
    - bgc-2641-reader-acceptance
    - bgc-2641-reader-reading
    - bgc-2641-delegated-context-reading
- assessment_id: bgc-2641-representation
  area: representation
  topic: representation
  outcome: supported
  summary: 'Both complete forms have 35 atoms, 37 bonds and three returned rings:
    a 16-member lactone, a three-member epoxide and a five-member aromatic thiazole.
    One ester, one ketone and two hydroxyl groups accompany seven specified tetrahedral
    centers and one specified E alkene. No original tetrahedral center is unspecified.
    Local stereo-atom conventions differ in one descriptor, while both bond tables
    and canonical strings preserve the E geometry. The complete 35-index one-way match
    is limited correspondence, not full graph or natural-identity proof.'
  target_ids:
  - CHEBI:31550
  evidence_ids:
  - bgc-2641-identity
  - bgc-2641-chemistry
  - bgc-2641-molecular-reading
  - bgc-2641-diagnostic-acceptance
  - bgc-2641-diagnostic-stderr
  - bgc-2641-row-mibig_compounds-0
  - bgc-2641-row-mibig_compounds-1
  - bgc-2641-row-mibig_compounds-2
  - bgc-2641-row-mibig_compounds-3
  - bgc-2641-stereo-schema
  - bgc-2641-stereo-extractor
  - bgc-2641-stereo-seeder
  - bgc-2641-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    value: 7 specified tetrahedra; 0 unspecified; one E alkene
    definition: Specified original centers and bond geometry, separated from reconstructed
      imine descriptors.
    evidence_ids:
    - bgc-2641-identity
    - bgc-2641-chemistry
    - bgc-2641-molecular-reading
    - bgc-2641-diagnostic-acceptance
    - bgc-2641-diagnostic-stderr
    - bgc-2641-row-mibig_compounds-0
    - bgc-2641-row-mibig_compounds-1
    - bgc-2641-row-mibig_compounds-2
    - bgc-2641-row-mibig_compounds-3
    - bgc-2641-stereo-schema
    - bgc-2641-stereo-extractor
    - bgc-2641-stereo-seeder
    - bgc-2641-stereo-policy
  - name: representation_correspondence
    value: Both canonical comparisons true; complete 35-index one-way match
    definition: Saved canonical comparisons and limited atom-match result; normalized
      identifiers are not full graph proof.
    evidence_ids:
    - bgc-2641-identity
    - bgc-2641-chemistry
    - bgc-2641-molecular-reading
    - bgc-2641-diagnostic-acceptance
    - bgc-2641-diagnostic-stderr
    - bgc-2641-row-mibig_compounds-0
    - bgc-2641-row-mibig_compounds-1
    - bgc-2641-row-mibig_compounds-2
    - bgc-2641-row-mibig_compounds-3
    - bgc-2641-stereo-schema
    - bgc-2641-stereo-extractor
    - bgc-2641-stereo-seeder
    - bgc-2641-stereo-policy
- assessment_id: bgc-2641-provenance
  area: provenance
  topic: provenance
  outcome: unknown
  summary: The four active MIBiG entries BGC0000988.5, BGC0000989.3, BGC0000990.3
    and BGC0000991.4 retain questionable quality, unknown completeness, SOURCE_ASSERTION
    producers and CLUSTER_UNSTATED loci. They distinguish Sorangium cellulosum NCBITaxon:56
    from So0157-2 NCBITaxon:1254432 and the four genome accessions. Literal classes
    NRPS|PKS remain separate from subclasses Type I|Unknown. Later curated protein
    graphs do not silently upgrade these source-owned grades or make strains interchangeable.
  target_ids:
  - CHEBI:31550
  evidence_ids:
  - bgc-2641-owner
  - bgc-2641-provenance
  - bgc-2641-query-mibig_compounds
  - bgc-2641-query-lotus_occurrences
  - bgc-2641-taxonomy
  - bgc-2641-curation
  - bgc-2641-direct-contexts
  - bgc-2641-row-mibig_compounds-0
  - bgc-2641-row-mibig_compounds-1
  - bgc-2641-row-mibig_compounds-2
  - bgc-2641-row-mibig_compounds-3
  - bgc-2641-row-lotus_occurrences-0
  - bgc-2641-row-lotus_occurrences-1
  - bgc-2641-row-lotus_occurrences-2
  - bgc-2641-row-lotus_occurrences-3
  - bgc-2641-row-lotus_occurrences-4
  - bgc-2641-row-lotus_occurrences-5
  - bgc-2641-row-lotus_occurrences-6
  - bgc-2641-row-lotus_occurrences-7
  - bgc-2641-row-lotus_occurrences-8
  - bgc-2641-row-lotus_occurrences-9
  - bgc-2641-row-lotus_occurrences-10
  - bgc-2641-component-0
  - bgc-2641-component-1
  - bgc-2641-component-2
  - bgc-2641-component-3
  - bgc-2641-component-4
  - bgc-2641-component-5
  - bgc-2641-graph-0
  - bgc-2641-graph-1
  - bgc-2641-graph-2
  - bgc-2641-graph-3
  - bgc-2641-graph-4
  - bgc-2641-graph-5
  - bgc-2641-graph-6
  - bgc-2641-graph-7
  - bgc-2641-reader-DATA
  - bgc-2641-reader-execution
  - bgc-2641-reader-acceptance
  - bgc-2641-reader-reading
  - bgc-2641-delegated-context-reading
  dimensions:
  - name: taxon_scope
    value: Producer taxa 56 and 1254432; occurrence taxa remain separately scoped
    definition: Retained names, IDs and synonyms; current rank and ancestry are not
      independently established.
    evidence_ids:
    - bgc-2641-owner
    - bgc-2641-provenance
    - bgc-2641-query-mibig_compounds
    - bgc-2641-query-lotus_occurrences
    - bgc-2641-taxonomy
    - bgc-2641-curation
    - bgc-2641-direct-contexts
    - bgc-2641-row-mibig_compounds-0
    - bgc-2641-row-mibig_compounds-1
    - bgc-2641-row-mibig_compounds-2
    - bgc-2641-row-mibig_compounds-3
    - bgc-2641-row-lotus_occurrences-0
    - bgc-2641-row-lotus_occurrences-1
    - bgc-2641-row-lotus_occurrences-2
    - bgc-2641-row-lotus_occurrences-3
    - bgc-2641-row-lotus_occurrences-4
    - bgc-2641-row-lotus_occurrences-5
    - bgc-2641-row-lotus_occurrences-6
    - bgc-2641-row-lotus_occurrences-7
    - bgc-2641-row-lotus_occurrences-8
    - bgc-2641-row-lotus_occurrences-9
    - bgc-2641-row-lotus_occurrences-10
    - bgc-2641-component-0
    - bgc-2641-component-1
    - bgc-2641-component-2
    - bgc-2641-component-3
    - bgc-2641-component-4
    - bgc-2641-component-5
    - bgc-2641-graph-0
    - bgc-2641-graph-1
    - bgc-2641-graph-2
    - bgc-2641-graph-3
    - bgc-2641-graph-4
    - bgc-2641-graph-5
    - bgc-2641-graph-6
    - bgc-2641-graph-7
    - bgc-2641-reader-DATA
    - bgc-2641-reader-execution
    - bgc-2641-reader-acceptance
    - bgc-2641-reader-reading
    - bgc-2641-delegated-context-reading
  - name: producer_evidence
    value: Four SOURCE_ASSERTION producer assertions
    definition: Literal source grade for the compound producer assertion.
    evidence_ids:
    - bgc-2641-owner
    - bgc-2641-provenance
    - bgc-2641-query-mibig_compounds
    - bgc-2641-query-lotus_occurrences
    - bgc-2641-taxonomy
    - bgc-2641-curation
    - bgc-2641-direct-contexts
    - bgc-2641-row-mibig_compounds-0
    - bgc-2641-row-mibig_compounds-1
    - bgc-2641-row-mibig_compounds-2
    - bgc-2641-row-mibig_compounds-3
    - bgc-2641-row-lotus_occurrences-0
    - bgc-2641-row-lotus_occurrences-1
    - bgc-2641-row-lotus_occurrences-2
    - bgc-2641-row-lotus_occurrences-3
    - bgc-2641-row-lotus_occurrences-4
    - bgc-2641-row-lotus_occurrences-5
    - bgc-2641-row-lotus_occurrences-6
    - bgc-2641-row-lotus_occurrences-7
    - bgc-2641-row-lotus_occurrences-8
    - bgc-2641-row-lotus_occurrences-9
    - bgc-2641-row-lotus_occurrences-10
    - bgc-2641-component-0
    - bgc-2641-component-1
    - bgc-2641-component-2
    - bgc-2641-component-3
    - bgc-2641-component-4
    - bgc-2641-component-5
    - bgc-2641-graph-0
    - bgc-2641-graph-1
    - bgc-2641-graph-2
    - bgc-2641-graph-3
    - bgc-2641-graph-4
    - bgc-2641-graph-5
    - bgc-2641-graph-6
    - bgc-2641-graph-7
    - bgc-2641-reader-DATA
    - bgc-2641-reader-execution
    - bgc-2641-reader-acceptance
    - bgc-2641-reader-reading
    - bgc-2641-delegated-context-reading
  - name: locus_evidence
    value: 'BGC0000988–BGC0000991: CLUSTER_UNSTATED'
    definition: Literal source grade for the locus-to-compound assertion.
    evidence_ids:
    - bgc-2641-owner
    - bgc-2641-provenance
    - bgc-2641-query-mibig_compounds
    - bgc-2641-query-lotus_occurrences
    - bgc-2641-taxonomy
    - bgc-2641-curation
    - bgc-2641-direct-contexts
    - bgc-2641-row-mibig_compounds-0
    - bgc-2641-row-mibig_compounds-1
    - bgc-2641-row-mibig_compounds-2
    - bgc-2641-row-mibig_compounds-3
    - bgc-2641-row-lotus_occurrences-0
    - bgc-2641-row-lotus_occurrences-1
    - bgc-2641-row-lotus_occurrences-2
    - bgc-2641-row-lotus_occurrences-3
    - bgc-2641-row-lotus_occurrences-4
    - bgc-2641-row-lotus_occurrences-5
    - bgc-2641-row-lotus_occurrences-6
    - bgc-2641-row-lotus_occurrences-7
    - bgc-2641-row-lotus_occurrences-8
    - bgc-2641-row-lotus_occurrences-9
    - bgc-2641-row-lotus_occurrences-10
    - bgc-2641-component-0
    - bgc-2641-component-1
    - bgc-2641-component-2
    - bgc-2641-component-3
    - bgc-2641-component-4
    - bgc-2641-component-5
    - bgc-2641-graph-0
    - bgc-2641-graph-1
    - bgc-2641-graph-2
    - bgc-2641-graph-3
    - bgc-2641-graph-4
    - bgc-2641-graph-5
    - bgc-2641-graph-6
    - bgc-2641-graph-7
    - bgc-2641-reader-DATA
    - bgc-2641-reader-execution
    - bgc-2641-reader-acceptance
    - bgc-2641-reader-reading
    - bgc-2641-delegated-context-reading
- assessment_id: bgc-2641-citations
  area: evidence
  topic: citations
  outcome: unknown
  summary: The source rows cite PMID:10662695, PMID:23549746 and PMID:10649995 at
    ENTRY grain; the repeated first PMID is not independent replication. The retained
    EpoK annotation cites a primary-experiment snippet plus database and curator evidence.
    SMP44 assembly includes an abstract-only whole-cluster production claim; other
    strain components preserve proposed participation and inaccessible-paper limits.
    PDB contact graphs preserve database and historical coordinate annotations. No
    cited paper, sequence or structure deposition was newly accessed.
  target_ids:
  - CHEBI:31550
  evidence_ids:
  - bgc-2641-provenance
  - bgc-2641-query-mibig_compounds
  - bgc-2641-query-lotus_occurrences
  - bgc-2641-query-chebi_origins
  - bgc-2641-source-reading
  - bgc-2641-history
  - bgc-2641-row-mibig_compounds-0
  - bgc-2641-row-mibig_compounds-1
  - bgc-2641-row-mibig_compounds-2
  - bgc-2641-row-mibig_compounds-3
  - bgc-2641-row-lotus_occurrences-0
  - bgc-2641-row-lotus_occurrences-1
  - bgc-2641-row-lotus_occurrences-2
  - bgc-2641-row-lotus_occurrences-3
  - bgc-2641-row-lotus_occurrences-4
  - bgc-2641-row-lotus_occurrences-5
  - bgc-2641-row-lotus_occurrences-6
  - bgc-2641-row-lotus_occurrences-7
  - bgc-2641-row-lotus_occurrences-8
  - bgc-2641-row-lotus_occurrences-9
  - bgc-2641-row-lotus_occurrences-10
  - bgc-2641-focal-assay-owner
  - bgc-2641-other-enzyme-named-assays
  - bgc-2641-assay-seeder
  - bgc-2641-activity-schema
  - bgc-2641-severity-rubric
  - bgc-2641-component-0
  - bgc-2641-component-1
  - bgc-2641-component-2
  - bgc-2641-component-3
  - bgc-2641-component-4
  - bgc-2641-component-5
  - bgc-2641-graph-0
  - bgc-2641-graph-1
  - bgc-2641-graph-2
  - bgc-2641-graph-3
  - bgc-2641-graph-4
  - bgc-2641-graph-5
  - bgc-2641-graph-6
  - bgc-2641-graph-7
  - bgc-2641-reader-DATA
  - bgc-2641-reader-execution
  - bgc-2641-reader-acceptance
  - bgc-2641-reader-reading
  - bgc-2641-delegated-context-reading
  dimensions:
  - name: citation_scope
    value: ENTRY papers; qualified historical graph and model evidence
    definition: Reference grain in the retained source rows; no inherited primary-paper
      access.
    evidence_ids:
    - bgc-2641-provenance
    - bgc-2641-query-mibig_compounds
    - bgc-2641-query-lotus_occurrences
    - bgc-2641-query-chebi_origins
    - bgc-2641-source-reading
    - bgc-2641-history
    - bgc-2641-row-mibig_compounds-0
    - bgc-2641-row-mibig_compounds-1
    - bgc-2641-row-mibig_compounds-2
    - bgc-2641-row-mibig_compounds-3
    - bgc-2641-row-lotus_occurrences-0
    - bgc-2641-row-lotus_occurrences-1
    - bgc-2641-row-lotus_occurrences-2
    - bgc-2641-row-lotus_occurrences-3
    - bgc-2641-row-lotus_occurrences-4
    - bgc-2641-row-lotus_occurrences-5
    - bgc-2641-row-lotus_occurrences-6
    - bgc-2641-row-lotus_occurrences-7
    - bgc-2641-row-lotus_occurrences-8
    - bgc-2641-row-lotus_occurrences-9
    - bgc-2641-row-lotus_occurrences-10
    - bgc-2641-focal-assay-owner
    - bgc-2641-other-enzyme-named-assays
    - bgc-2641-assay-seeder
    - bgc-2641-activity-schema
    - bgc-2641-severity-rubric
    - bgc-2641-component-0
    - bgc-2641-component-1
    - bgc-2641-component-2
    - bgc-2641-component-3
    - bgc-2641-component-4
    - bgc-2641-component-5
    - bgc-2641-graph-0
    - bgc-2641-graph-1
    - bgc-2641-graph-2
    - bgc-2641-graph-3
    - bgc-2641-graph-4
    - bgc-2641-graph-5
    - bgc-2641-graph-6
    - bgc-2641-graph-7
    - bgc-2641-reader-DATA
    - bgc-2641-reader-execution
    - bgc-2641-reader-acceptance
    - bgc-2641-reader-reading
    - bgc-2641-delegated-context-reading
- assessment_id: bgc-2641-occurrence_activity
  area: evidence
  topic: occurrence_activity
  outcome: concern
  summary: Eleven LOTUS placements support occurrence assertions across the exact
    retained taxa and citations, without production or publication-independence inference.
    The uncapped assay query contains 117 rows representing 111 full-key/CID/AID tuples;
    six paired rows differ in target-accession content. The owner retains 25 sorted
    observations and explicitly omits 92. AID 504832 is ACTIVE with source Potency
    0.0013 uM, represented as OTHER, but its delayed-death 48-hour title and blank
    target do not support ENZYME_INHIBITOR. The 96-hour AID 504834 result is separately
    inconclusive. NSD2 cellular assays and O96028 annotations remain distinct; they
    do not establish direct enzyme inhibition or affinity, and their presence does
    not make the overall summary globally verified. No existing exact exclusion applies.
  target_ids:
  - CHEBI:31550
  evidence_ids:
  - bgc-2641-activity-owner
  - bgc-2641-query-lotus_occurrences
  - bgc-2641-query-chebi_origins
  - bgc-2641-query-cyanometdb_occurrences
  - bgc-2641-query-pubchem_bioassay
  - bgc-2641-query-bindingdb_targets
  - bgc-2641-query-antibioticmech_inchikeys
  - bgc-2641-assay-curation
  - bgc-2641-direct-contexts
  - bgc-2641-row-lotus_occurrences-0
  - bgc-2641-row-lotus_occurrences-1
  - bgc-2641-row-lotus_occurrences-2
  - bgc-2641-row-lotus_occurrences-3
  - bgc-2641-row-lotus_occurrences-4
  - bgc-2641-row-lotus_occurrences-5
  - bgc-2641-row-lotus_occurrences-6
  - bgc-2641-row-lotus_occurrences-7
  - bgc-2641-row-lotus_occurrences-8
  - bgc-2641-row-lotus_occurrences-9
  - bgc-2641-row-lotus_occurrences-10
  - bgc-2641-row-pubchem_bioassay-0
  - bgc-2641-row-pubchem_bioassay-1
  - bgc-2641-row-pubchem_bioassay-2
  - bgc-2641-row-pubchem_bioassay-3
  - bgc-2641-row-pubchem_bioassay-4
  - bgc-2641-row-pubchem_bioassay-5
  - bgc-2641-row-pubchem_bioassay-6
  - bgc-2641-row-pubchem_bioassay-7
  - bgc-2641-row-pubchem_bioassay-8
  - bgc-2641-row-pubchem_bioassay-9
  - bgc-2641-row-pubchem_bioassay-10
  - bgc-2641-row-pubchem_bioassay-11
  - bgc-2641-row-pubchem_bioassay-12
  - bgc-2641-row-pubchem_bioassay-13
  - bgc-2641-row-pubchem_bioassay-14
  - bgc-2641-row-pubchem_bioassay-15
  - bgc-2641-row-pubchem_bioassay-16
  - bgc-2641-row-pubchem_bioassay-17
  - bgc-2641-row-pubchem_bioassay-18
  - bgc-2641-row-pubchem_bioassay-19
  - bgc-2641-row-pubchem_bioassay-20
  - bgc-2641-row-pubchem_bioassay-21
  - bgc-2641-row-pubchem_bioassay-22
  - bgc-2641-row-pubchem_bioassay-23
  - bgc-2641-row-pubchem_bioassay-24
  - bgc-2641-row-pubchem_bioassay-25
  - bgc-2641-row-pubchem_bioassay-26
  - bgc-2641-row-pubchem_bioassay-27
  - bgc-2641-row-pubchem_bioassay-28
  - bgc-2641-row-pubchem_bioassay-29
  - bgc-2641-row-pubchem_bioassay-30
  - bgc-2641-row-pubchem_bioassay-31
  - bgc-2641-row-pubchem_bioassay-32
  - bgc-2641-row-pubchem_bioassay-33
  - bgc-2641-row-pubchem_bioassay-34
  - bgc-2641-row-pubchem_bioassay-35
  - bgc-2641-row-pubchem_bioassay-36
  - bgc-2641-row-pubchem_bioassay-37
  - bgc-2641-row-pubchem_bioassay-38
  - bgc-2641-row-pubchem_bioassay-39
  - bgc-2641-row-pubchem_bioassay-40
  - bgc-2641-row-pubchem_bioassay-41
  - bgc-2641-row-pubchem_bioassay-42
  - bgc-2641-row-pubchem_bioassay-43
  - bgc-2641-row-pubchem_bioassay-44
  - bgc-2641-row-pubchem_bioassay-45
  - bgc-2641-row-pubchem_bioassay-46
  - bgc-2641-row-pubchem_bioassay-47
  - bgc-2641-row-pubchem_bioassay-48
  - bgc-2641-row-pubchem_bioassay-49
  - bgc-2641-row-pubchem_bioassay-50
  - bgc-2641-row-pubchem_bioassay-51
  - bgc-2641-row-pubchem_bioassay-52
  - bgc-2641-row-pubchem_bioassay-53
  - bgc-2641-row-pubchem_bioassay-54
  - bgc-2641-row-pubchem_bioassay-55
  - bgc-2641-row-pubchem_bioassay-56
  - bgc-2641-row-pubchem_bioassay-57
  - bgc-2641-row-pubchem_bioassay-58
  - bgc-2641-row-pubchem_bioassay-59
  - bgc-2641-row-pubchem_bioassay-60
  - bgc-2641-row-pubchem_bioassay-61
  - bgc-2641-row-pubchem_bioassay-62
  - bgc-2641-row-pubchem_bioassay-63
  - bgc-2641-row-pubchem_bioassay-64
  - bgc-2641-row-pubchem_bioassay-65
  - bgc-2641-row-pubchem_bioassay-66
  - bgc-2641-row-pubchem_bioassay-67
  - bgc-2641-row-pubchem_bioassay-68
  - bgc-2641-row-pubchem_bioassay-69
  - bgc-2641-row-pubchem_bioassay-70
  - bgc-2641-row-pubchem_bioassay-71
  - bgc-2641-row-pubchem_bioassay-72
  - bgc-2641-row-pubchem_bioassay-73
  - bgc-2641-row-pubchem_bioassay-74
  - bgc-2641-row-pubchem_bioassay-75
  - bgc-2641-row-pubchem_bioassay-76
  - bgc-2641-row-pubchem_bioassay-77
  - bgc-2641-row-pubchem_bioassay-78
  - bgc-2641-row-pubchem_bioassay-79
  - bgc-2641-row-pubchem_bioassay-80
  - bgc-2641-row-pubchem_bioassay-81
  - bgc-2641-row-pubchem_bioassay-82
  - bgc-2641-row-pubchem_bioassay-83
  - bgc-2641-row-pubchem_bioassay-84
  - bgc-2641-row-pubchem_bioassay-85
  - bgc-2641-row-pubchem_bioassay-86
  - bgc-2641-row-pubchem_bioassay-87
  - bgc-2641-row-pubchem_bioassay-88
  - bgc-2641-row-pubchem_bioassay-89
  - bgc-2641-row-pubchem_bioassay-90
  - bgc-2641-row-pubchem_bioassay-91
  - bgc-2641-row-pubchem_bioassay-92
  - bgc-2641-row-pubchem_bioassay-93
  - bgc-2641-row-pubchem_bioassay-94
  - bgc-2641-row-pubchem_bioassay-95
  - bgc-2641-row-pubchem_bioassay-96
  - bgc-2641-row-pubchem_bioassay-97
  - bgc-2641-row-pubchem_bioassay-98
  - bgc-2641-row-pubchem_bioassay-99
  - bgc-2641-row-pubchem_bioassay-100
  - bgc-2641-row-pubchem_bioassay-101
  - bgc-2641-row-pubchem_bioassay-102
  - bgc-2641-row-pubchem_bioassay-103
  - bgc-2641-row-pubchem_bioassay-104
  - bgc-2641-row-pubchem_bioassay-105
  - bgc-2641-row-pubchem_bioassay-106
  - bgc-2641-row-pubchem_bioassay-107
  - bgc-2641-row-pubchem_bioassay-108
  - bgc-2641-row-pubchem_bioassay-109
  - bgc-2641-row-pubchem_bioassay-110
  - bgc-2641-row-pubchem_bioassay-111
  - bgc-2641-row-pubchem_bioassay-112
  - bgc-2641-row-pubchem_bioassay-113
  - bgc-2641-row-pubchem_bioassay-114
  - bgc-2641-row-pubchem_bioassay-115
  - bgc-2641-row-pubchem_bioassay-116
  - bgc-2641-focal-assay-owner
  - bgc-2641-other-enzyme-named-assays
  - bgc-2641-assay-seeder
  - bgc-2641-activity-schema
  - bgc-2641-severity-rubric
  - bgc-2641-delegated-context-reading
  dimensions:
  - name: occurrence_scope
    value: 11 LOTUS placements; no production or independence transfer
    definition: Exact retained occurrence query scope, without production or independence
      transfer.
    evidence_ids:
    - bgc-2641-activity-owner
    - bgc-2641-query-lotus_occurrences
    - bgc-2641-query-chebi_origins
    - bgc-2641-query-cyanometdb_occurrences
    - bgc-2641-query-pubchem_bioassay
    - bgc-2641-query-bindingdb_targets
    - bgc-2641-query-antibioticmech_inchikeys
    - bgc-2641-assay-curation
    - bgc-2641-direct-contexts
    - bgc-2641-row-lotus_occurrences-0
    - bgc-2641-row-lotus_occurrences-1
    - bgc-2641-row-lotus_occurrences-2
    - bgc-2641-row-lotus_occurrences-3
    - bgc-2641-row-lotus_occurrences-4
    - bgc-2641-row-lotus_occurrences-5
    - bgc-2641-row-lotus_occurrences-6
    - bgc-2641-row-lotus_occurrences-7
    - bgc-2641-row-lotus_occurrences-8
    - bgc-2641-row-lotus_occurrences-9
    - bgc-2641-row-lotus_occurrences-10
    - bgc-2641-row-pubchem_bioassay-0
    - bgc-2641-row-pubchem_bioassay-1
    - bgc-2641-row-pubchem_bioassay-2
    - bgc-2641-row-pubchem_bioassay-3
    - bgc-2641-row-pubchem_bioassay-4
    - bgc-2641-row-pubchem_bioassay-5
    - bgc-2641-row-pubchem_bioassay-6
    - bgc-2641-row-pubchem_bioassay-7
    - bgc-2641-row-pubchem_bioassay-8
    - bgc-2641-row-pubchem_bioassay-9
    - bgc-2641-row-pubchem_bioassay-10
    - bgc-2641-row-pubchem_bioassay-11
    - bgc-2641-row-pubchem_bioassay-12
    - bgc-2641-row-pubchem_bioassay-13
    - bgc-2641-row-pubchem_bioassay-14
    - bgc-2641-row-pubchem_bioassay-15
    - bgc-2641-row-pubchem_bioassay-16
    - bgc-2641-row-pubchem_bioassay-17
    - bgc-2641-row-pubchem_bioassay-18
    - bgc-2641-row-pubchem_bioassay-19
    - bgc-2641-row-pubchem_bioassay-20
    - bgc-2641-row-pubchem_bioassay-21
    - bgc-2641-row-pubchem_bioassay-22
    - bgc-2641-row-pubchem_bioassay-23
    - bgc-2641-row-pubchem_bioassay-24
    - bgc-2641-row-pubchem_bioassay-25
    - bgc-2641-row-pubchem_bioassay-26
    - bgc-2641-row-pubchem_bioassay-27
    - bgc-2641-row-pubchem_bioassay-28
    - bgc-2641-row-pubchem_bioassay-29
    - bgc-2641-row-pubchem_bioassay-30
    - bgc-2641-row-pubchem_bioassay-31
    - bgc-2641-row-pubchem_bioassay-32
    - bgc-2641-row-pubchem_bioassay-33
    - bgc-2641-row-pubchem_bioassay-34
    - bgc-2641-row-pubchem_bioassay-35
    - bgc-2641-row-pubchem_bioassay-36
    - bgc-2641-row-pubchem_bioassay-37
    - bgc-2641-row-pubchem_bioassay-38
    - bgc-2641-row-pubchem_bioassay-39
    - bgc-2641-row-pubchem_bioassay-40
    - bgc-2641-row-pubchem_bioassay-41
    - bgc-2641-row-pubchem_bioassay-42
    - bgc-2641-row-pubchem_bioassay-43
    - bgc-2641-row-pubchem_bioassay-44
    - bgc-2641-row-pubchem_bioassay-45
    - bgc-2641-row-pubchem_bioassay-46
    - bgc-2641-row-pubchem_bioassay-47
    - bgc-2641-row-pubchem_bioassay-48
    - bgc-2641-row-pubchem_bioassay-49
    - bgc-2641-row-pubchem_bioassay-50
    - bgc-2641-row-pubchem_bioassay-51
    - bgc-2641-row-pubchem_bioassay-52
    - bgc-2641-row-pubchem_bioassay-53
    - bgc-2641-row-pubchem_bioassay-54
    - bgc-2641-row-pubchem_bioassay-55
    - bgc-2641-row-pubchem_bioassay-56
    - bgc-2641-row-pubchem_bioassay-57
    - bgc-2641-row-pubchem_bioassay-58
    - bgc-2641-row-pubchem_bioassay-59
    - bgc-2641-row-pubchem_bioassay-60
    - bgc-2641-row-pubchem_bioassay-61
    - bgc-2641-row-pubchem_bioassay-62
    - bgc-2641-row-pubchem_bioassay-63
    - bgc-2641-row-pubchem_bioassay-64
    - bgc-2641-row-pubchem_bioassay-65
    - bgc-2641-row-pubchem_bioassay-66
    - bgc-2641-row-pubchem_bioassay-67
    - bgc-2641-row-pubchem_bioassay-68
    - bgc-2641-row-pubchem_bioassay-69
    - bgc-2641-row-pubchem_bioassay-70
    - bgc-2641-row-pubchem_bioassay-71
    - bgc-2641-row-pubchem_bioassay-72
    - bgc-2641-row-pubchem_bioassay-73
    - bgc-2641-row-pubchem_bioassay-74
    - bgc-2641-row-pubchem_bioassay-75
    - bgc-2641-row-pubchem_bioassay-76
    - bgc-2641-row-pubchem_bioassay-77
    - bgc-2641-row-pubchem_bioassay-78
    - bgc-2641-row-pubchem_bioassay-79
    - bgc-2641-row-pubchem_bioassay-80
    - bgc-2641-row-pubchem_bioassay-81
    - bgc-2641-row-pubchem_bioassay-82
    - bgc-2641-row-pubchem_bioassay-83
    - bgc-2641-row-pubchem_bioassay-84
    - bgc-2641-row-pubchem_bioassay-85
    - bgc-2641-row-pubchem_bioassay-86
    - bgc-2641-row-pubchem_bioassay-87
    - bgc-2641-row-pubchem_bioassay-88
    - bgc-2641-row-pubchem_bioassay-89
    - bgc-2641-row-pubchem_bioassay-90
    - bgc-2641-row-pubchem_bioassay-91
    - bgc-2641-row-pubchem_bioassay-92
    - bgc-2641-row-pubchem_bioassay-93
    - bgc-2641-row-pubchem_bioassay-94
    - bgc-2641-row-pubchem_bioassay-95
    - bgc-2641-row-pubchem_bioassay-96
    - bgc-2641-row-pubchem_bioassay-97
    - bgc-2641-row-pubchem_bioassay-98
    - bgc-2641-row-pubchem_bioassay-99
    - bgc-2641-row-pubchem_bioassay-100
    - bgc-2641-row-pubchem_bioassay-101
    - bgc-2641-row-pubchem_bioassay-102
    - bgc-2641-row-pubchem_bioassay-103
    - bgc-2641-row-pubchem_bioassay-104
    - bgc-2641-row-pubchem_bioassay-105
    - bgc-2641-row-pubchem_bioassay-106
    - bgc-2641-row-pubchem_bioassay-107
    - bgc-2641-row-pubchem_bioassay-108
    - bgc-2641-row-pubchem_bioassay-109
    - bgc-2641-row-pubchem_bioassay-110
    - bgc-2641-row-pubchem_bioassay-111
    - bgc-2641-row-pubchem_bioassay-112
    - bgc-2641-row-pubchem_bioassay-113
    - bgc-2641-row-pubchem_bioassay-114
    - bgc-2641-row-pubchem_bioassay-115
    - bgc-2641-row-pubchem_bioassay-116
    - bgc-2641-focal-assay-owner
    - bgc-2641-other-enzyme-named-assays
    - bgc-2641-assay-seeder
    - bgc-2641-activity-schema
    - bgc-2641-severity-rubric
    - bgc-2641-delegated-context-reading
  - name: assay_target_scope
    value: 117 rows/111 tuples; AID 504832 class unsupported; 25 written observations
    definition: Actual AID, endpoint and direct-target scope, including sentinels
      and exclusions.
    evidence_ids:
    - bgc-2641-activity-owner
    - bgc-2641-query-lotus_occurrences
    - bgc-2641-query-chebi_origins
    - bgc-2641-query-cyanometdb_occurrences
    - bgc-2641-query-pubchem_bioassay
    - bgc-2641-query-bindingdb_targets
    - bgc-2641-query-antibioticmech_inchikeys
    - bgc-2641-assay-curation
    - bgc-2641-direct-contexts
    - bgc-2641-row-lotus_occurrences-0
    - bgc-2641-row-lotus_occurrences-1
    - bgc-2641-row-lotus_occurrences-2
    - bgc-2641-row-lotus_occurrences-3
    - bgc-2641-row-lotus_occurrences-4
    - bgc-2641-row-lotus_occurrences-5
    - bgc-2641-row-lotus_occurrences-6
    - bgc-2641-row-lotus_occurrences-7
    - bgc-2641-row-lotus_occurrences-8
    - bgc-2641-row-lotus_occurrences-9
    - bgc-2641-row-lotus_occurrences-10
    - bgc-2641-row-pubchem_bioassay-0
    - bgc-2641-row-pubchem_bioassay-1
    - bgc-2641-row-pubchem_bioassay-2
    - bgc-2641-row-pubchem_bioassay-3
    - bgc-2641-row-pubchem_bioassay-4
    - bgc-2641-row-pubchem_bioassay-5
    - bgc-2641-row-pubchem_bioassay-6
    - bgc-2641-row-pubchem_bioassay-7
    - bgc-2641-row-pubchem_bioassay-8
    - bgc-2641-row-pubchem_bioassay-9
    - bgc-2641-row-pubchem_bioassay-10
    - bgc-2641-row-pubchem_bioassay-11
    - bgc-2641-row-pubchem_bioassay-12
    - bgc-2641-row-pubchem_bioassay-13
    - bgc-2641-row-pubchem_bioassay-14
    - bgc-2641-row-pubchem_bioassay-15
    - bgc-2641-row-pubchem_bioassay-16
    - bgc-2641-row-pubchem_bioassay-17
    - bgc-2641-row-pubchem_bioassay-18
    - bgc-2641-row-pubchem_bioassay-19
    - bgc-2641-row-pubchem_bioassay-20
    - bgc-2641-row-pubchem_bioassay-21
    - bgc-2641-row-pubchem_bioassay-22
    - bgc-2641-row-pubchem_bioassay-23
    - bgc-2641-row-pubchem_bioassay-24
    - bgc-2641-row-pubchem_bioassay-25
    - bgc-2641-row-pubchem_bioassay-26
    - bgc-2641-row-pubchem_bioassay-27
    - bgc-2641-row-pubchem_bioassay-28
    - bgc-2641-row-pubchem_bioassay-29
    - bgc-2641-row-pubchem_bioassay-30
    - bgc-2641-row-pubchem_bioassay-31
    - bgc-2641-row-pubchem_bioassay-32
    - bgc-2641-row-pubchem_bioassay-33
    - bgc-2641-row-pubchem_bioassay-34
    - bgc-2641-row-pubchem_bioassay-35
    - bgc-2641-row-pubchem_bioassay-36
    - bgc-2641-row-pubchem_bioassay-37
    - bgc-2641-row-pubchem_bioassay-38
    - bgc-2641-row-pubchem_bioassay-39
    - bgc-2641-row-pubchem_bioassay-40
    - bgc-2641-row-pubchem_bioassay-41
    - bgc-2641-row-pubchem_bioassay-42
    - bgc-2641-row-pubchem_bioassay-43
    - bgc-2641-row-pubchem_bioassay-44
    - bgc-2641-row-pubchem_bioassay-45
    - bgc-2641-row-pubchem_bioassay-46
    - bgc-2641-row-pubchem_bioassay-47
    - bgc-2641-row-pubchem_bioassay-48
    - bgc-2641-row-pubchem_bioassay-49
    - bgc-2641-row-pubchem_bioassay-50
    - bgc-2641-row-pubchem_bioassay-51
    - bgc-2641-row-pubchem_bioassay-52
    - bgc-2641-row-pubchem_bioassay-53
    - bgc-2641-row-pubchem_bioassay-54
    - bgc-2641-row-pubchem_bioassay-55
    - bgc-2641-row-pubchem_bioassay-56
    - bgc-2641-row-pubchem_bioassay-57
    - bgc-2641-row-pubchem_bioassay-58
    - bgc-2641-row-pubchem_bioassay-59
    - bgc-2641-row-pubchem_bioassay-60
    - bgc-2641-row-pubchem_bioassay-61
    - bgc-2641-row-pubchem_bioassay-62
    - bgc-2641-row-pubchem_bioassay-63
    - bgc-2641-row-pubchem_bioassay-64
    - bgc-2641-row-pubchem_bioassay-65
    - bgc-2641-row-pubchem_bioassay-66
    - bgc-2641-row-pubchem_bioassay-67
    - bgc-2641-row-pubchem_bioassay-68
    - bgc-2641-row-pubchem_bioassay-69
    - bgc-2641-row-pubchem_bioassay-70
    - bgc-2641-row-pubchem_bioassay-71
    - bgc-2641-row-pubchem_bioassay-72
    - bgc-2641-row-pubchem_bioassay-73
    - bgc-2641-row-pubchem_bioassay-74
    - bgc-2641-row-pubchem_bioassay-75
    - bgc-2641-row-pubchem_bioassay-76
    - bgc-2641-row-pubchem_bioassay-77
    - bgc-2641-row-pubchem_bioassay-78
    - bgc-2641-row-pubchem_bioassay-79
    - bgc-2641-row-pubchem_bioassay-80
    - bgc-2641-row-pubchem_bioassay-81
    - bgc-2641-row-pubchem_bioassay-82
    - bgc-2641-row-pubchem_bioassay-83
    - bgc-2641-row-pubchem_bioassay-84
    - bgc-2641-row-pubchem_bioassay-85
    - bgc-2641-row-pubchem_bioassay-86
    - bgc-2641-row-pubchem_bioassay-87
    - bgc-2641-row-pubchem_bioassay-88
    - bgc-2641-row-pubchem_bioassay-89
    - bgc-2641-row-pubchem_bioassay-90
    - bgc-2641-row-pubchem_bioassay-91
    - bgc-2641-row-pubchem_bioassay-92
    - bgc-2641-row-pubchem_bioassay-93
    - bgc-2641-row-pubchem_bioassay-94
    - bgc-2641-row-pubchem_bioassay-95
    - bgc-2641-row-pubchem_bioassay-96
    - bgc-2641-row-pubchem_bioassay-97
    - bgc-2641-row-pubchem_bioassay-98
    - bgc-2641-row-pubchem_bioassay-99
    - bgc-2641-row-pubchem_bioassay-100
    - bgc-2641-row-pubchem_bioassay-101
    - bgc-2641-row-pubchem_bioassay-102
    - bgc-2641-row-pubchem_bioassay-103
    - bgc-2641-row-pubchem_bioassay-104
    - bgc-2641-row-pubchem_bioassay-105
    - bgc-2641-row-pubchem_bioassay-106
    - bgc-2641-row-pubchem_bioassay-107
    - bgc-2641-row-pubchem_bioassay-108
    - bgc-2641-row-pubchem_bioassay-109
    - bgc-2641-row-pubchem_bioassay-110
    - bgc-2641-row-pubchem_bioassay-111
    - bgc-2641-row-pubchem_bioassay-112
    - bgc-2641-row-pubchem_bioassay-113
    - bgc-2641-row-pubchem_bioassay-114
    - bgc-2641-row-pubchem_bioassay-115
    - bgc-2641-row-pubchem_bioassay-116
    - bgc-2641-focal-assay-owner
    - bgc-2641-other-enzyme-named-assays
    - bgc-2641-assay-seeder
    - bgc-2641-activity-schema
    - bgc-2641-severity-rubric
    - bgc-2641-delegated-context-reading
- assessment_id: bgc-2641-classification
  area: consistency
  topic: classification
  outcome: unknown
  summary: The stored 16-member lactone, epoxide and thiazole support a broad epothilone/macrolide
    structural interpretation. NPClassifier reports Amino acids and Peptides, Polyketides,
    Macrolides and Epothilones, with is_glycoside false. The retained topology is
    compatible with that family, but exact model applicability and biological assembly
    are separate claims. Strain-specific biosynthesis graphs and deposited tubulin
    contacts are assessed at their own evidence grain rather than inferred from classification.
  target_ids:
  - CHEBI:31550
  evidence_ids:
  - bgc-2641-classification-owner
  - bgc-2641-query-npclassifier
  - bgc-2641-query-mibig_compounds
  - bgc-2641-chemistry
  - bgc-2641-molecular-reading
  - bgc-2641-row-npclassifier-0
  - bgc-2641-row-mibig_compounds-0
  - bgc-2641-row-mibig_compounds-1
  - bgc-2641-row-mibig_compounds-2
  - bgc-2641-row-mibig_compounds-3
  dimensions:
  - name: classification_applicability
    value: Macrolide/epoxide/thiazole topology supported; model and biological scope
      bounded
    definition: Encoded motif support separated from exact computed model-family or
      biosynthesis claims.
    evidence_ids:
    - bgc-2641-classification-owner
    - bgc-2641-query-npclassifier
    - bgc-2641-query-mibig_compounds
    - bgc-2641-chemistry
    - bgc-2641-molecular-reading
    - bgc-2641-row-npclassifier-0
    - bgc-2641-row-mibig_compounds-0
    - bgc-2641-row-mibig_compounds-1
    - bgc-2641-row-mibig_compounds-2
    - bgc-2641-row-mibig_compounds-3
- assessment_id: bgc-2641-completion
  area: completeness
  topic: completion
  outcome: unknown
  summary: The complete owner and history, scoped retained source payloads, both full
    saved molecular forms, and 52 actual input hashes and ownership declarations were
    reviewed. The accepted plan and intakes contain 458 input placements across 69
    paths. Five local gates passed; full QC, OAK and fresh external authority remain
    unavailable. The accepted complete Epothilone maintained view includes all six
    components; preservation does not independently validate their historical scientific
    claims. Completion remains partial.
  target_ids:
  - CHEBI:31550
  evidence_ids:
  - bgc-2641-intake
  - bgc-2641-intake-acceptance
  - bgc-2641-plan
  - bgc-2641-plan-acceptance
  - bgc-2641-gates
  - bgc-2641-source-reading
  - bgc-2641-source-notes
  - bgc-2641-molecular-reading
  - bgc-2641-diagnostic-acceptance
  - bgc-2641-mechanism-scope
  - bgc-2641-focal-assay-owner
  - bgc-2641-other-enzyme-named-assays
  - bgc-2641-assay-seeder
  - bgc-2641-activity-schema
  - bgc-2641-severity-rubric
  - bgc-2641-component-0
  - bgc-2641-component-1
  - bgc-2641-component-2
  - bgc-2641-component-3
  - bgc-2641-component-4
  - bgc-2641-component-5
  - bgc-2641-graph-0
  - bgc-2641-graph-1
  - bgc-2641-graph-2
  - bgc-2641-graph-3
  - bgc-2641-graph-4
  - bgc-2641-graph-5
  - bgc-2641-graph-6
  - bgc-2641-graph-7
  - bgc-2641-reader-DATA
  - bgc-2641-reader-execution
  - bgc-2641-reader-acceptance
  - bgc-2641-reader-reading
  dimensions:
  - name: review_completion
    value: Partial; 52 actual inputs and complete paired forms
    definition: Actual local review scope and unavailable required gates.
    evidence_ids:
    - bgc-2641-intake
    - bgc-2641-intake-acceptance
    - bgc-2641-plan
    - bgc-2641-plan-acceptance
    - bgc-2641-gates
    - bgc-2641-source-reading
    - bgc-2641-source-notes
    - bgc-2641-molecular-reading
    - bgc-2641-diagnostic-acceptance
    - bgc-2641-mechanism-scope
    - bgc-2641-focal-assay-owner
    - bgc-2641-other-enzyme-named-assays
    - bgc-2641-assay-seeder
    - bgc-2641-activity-schema
    - bgc-2641-severity-rubric
    - bgc-2641-component-0
    - bgc-2641-component-1
    - bgc-2641-component-2
    - bgc-2641-component-3
    - bgc-2641-component-4
    - bgc-2641-component-5
    - bgc-2641-graph-0
    - bgc-2641-graph-1
    - bgc-2641-graph-2
    - bgc-2641-graph-3
    - bgc-2641-graph-4
    - bgc-2641-graph-5
    - bgc-2641-graph-6
    - bgc-2641-graph-7
    - bgc-2641-reader-DATA
    - bgc-2641-reader-execution
    - bgc-2641-reader-acceptance
    - bgc-2641-reader-reading
- assessment_id: bgc-2641-graph
  area: graph
  topic: qualified_epothilone_biosynthesis_and_model_contacts
  outcome: supported
  summary: The accepted maintained view preserves eight complete graphs, 52 nodes,
    44 edges, six component references and one numbered pathway step. EpoK Q9KIZ4/RHEA:47808
    records terminal D-to-B epoxidation; the step has no literal proposed field. SMP44
    and the three other strain graphs separately retain source-annotated or proposed
    participation, without a complete reaction order or transferred individual enzyme
    assays. So0157-2 EpoF remains a generic P450, while KYC3013 uses versioned protein
    references instead of deleted UniProt entries. The 9PND, 6S8M and 7DAE graphs
    restrict drug contact to deposited beta-tubulin models and distinguish construct
    membership, ligand-quality limitations and missing coordinates. Complete reader
    equality supports faithful retained representation, not fresh protein/sequence/coordinate
    validation, binding affinity or downstream effect.
  target_ids:
  - CHEBI:31550
  evidence_ids:
  - bgc-2641-reader-DATA
  - bgc-2641-reader-execution
  - bgc-2641-reader-acceptance
  - bgc-2641-reader-reading
  - bgc-2641-mechanism-scope
  - bgc-2641-provenance
  - bgc-2641-source-reading
  - bgc-2641-component-0
  - bgc-2641-component-1
  - bgc-2641-component-2
  - bgc-2641-component-3
  - bgc-2641-component-4
  - bgc-2641-component-5
  - bgc-2641-graph-0
  - bgc-2641-graph-1
  - bgc-2641-graph-2
  - bgc-2641-graph-3
  - bgc-2641-graph-4
  - bgc-2641-graph-5
  - bgc-2641-graph-6
  - bgc-2641-graph-7
  dimensions: []
findings:
- finding_id: bgc-2641-unsupported-delayed-death-enzyme-class
  issue_key: epothilone-b-aid504832-unsupported-delayed-death-enzyme-class
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Delayed parasite-death screening is promoted to enzyme inhibition
  description: The exact QXRSDHAAWVKZLJ-PVYNADRNSA-N/CID448013/AID504832 source row
    describes delayed death of the malarial parasite plastid after 48 hours, with
    Active, Potency 0.0013 uM and a blank target accession. The written observation
    faithfully retains ACTIVE, OTHER and 0.0013 uM, but the generic inhibitors-of
    title fallback adds ENZYME_INHIBITOR without an enzyme-specific endpoint or identified
    enzyme. This is a confirmed retained-evidence class-scope defect, not a measurement,
    identity or source-row error. NSD2 cellular assays remain separate evidence and
    do not make the whole summary scientifically verified; automatic summary deletion
    is not justified by this single finding.
  field_paths:
  - bioactivities[16].activity_class
  rule_id: review-yaml-record:major-unsupported-evidence-scope
  native_severity: major
  normalization_reason: Unsupported enzyme specificity materially inflates the biological
    scope of this assay and is graded major. The retained result, value, compound
    identity and other assay classes are not challenged.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained title-to-activity classification; preserve observations, source
      measurements, provenance and independently supported classes.
  disposition_reason: Proposed local maintained-classifier correction and focused
    validation only; no record/source edit, external lookup or completed fix is claimed.
  target_ids:
  - CHEBI:31550
  evidence_ids:
  - bgc-2641-focal-assay-owner
  - bgc-2641-other-enzyme-named-assays
  - bgc-2641-assay-seeder
  - bgc-2641-activity-schema
  - bgc-2641-severity-rubric
  - bgc-2641-query-pubchem_bioassay
  - bgc-2641-assay-curation
  - bgc-2641-row-pubchem_bioassay-72
  - bgc-2641-row-pubchem_bioassay-73
actions:
- action_id: bgc-2641-bound-delayed-death-classification
  description: Revise the maintained classifier so generic inhibitors-of wording in
    a phenotypic delayed-death title does not alone establish ENZYME_INHIBITOR. Determine
    the appropriately supported class from retained evidence without prescribing an
    unverified replacement. Preserve ACTIVE, OTHER, 0.0013 uM, pubchem.aid:504832,
    original source bytes and all other observations. Reassess any derived summary
    against its remaining independent backing rather than deleting it automatically.
    This is proposed local work, with no outbound request authorized.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained title-to-activity classification; preserve observations, source
      measurements, provenance and independently supported classes.
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - The exact AID504832 row no longer receives enzyme specificity solely from the
    generic title, while its call, measurement, unit, evidence and original input
    row remain exact.
  - Keep distinct AID504834 96-hour inconclusive behavior and all six target-accession
    variant pairs; do not collapse positive-row attribution or apply a different-key/CID
    exclusion.
  - Retain and separately scope NSD2-named cellular observations and O96028 annotations;
    do not infer direct inhibition/affinity or automatically erase the overall enzyme-class
    summary.
  - If a generator change is separately authorized, add focused local supported/unsupported-title
    regression coverage, regenerate through maintained validated paths and verify
    strict, corpus and reproduction checks without observation loss or changes to
    the established 25-observation ordering/cap.
  target_ids:
  - CHEBI:31550
  finding_ids:
  - bgc-2641-unsupported-delayed-death-enzyme-class
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
- AID 504832 class is the sole new finding; the source observation, value, activity
  call and other assay observations are not corrected or deleted by this review.
- The overall ENZYME_INHIBITOR summary has other retained enzyme-named assay context.
  Its complete scientific validity is not established, and automatic deletion is not
  prescribed.
- 'Historical model-partner wording is read with the later clarification: absence
  of an asserted target edge is not proof of biological non-target status.'
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-265
```
