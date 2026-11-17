# Local evidence review: notoamide F

- Review: 20261107T060415Z-notoamide-f
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T05:22:53.386311Z
- Finished UTC: 2026-11-07T06:04:15.628915Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Notoamide F retains its own aromatic indole/methoxy topology, full key and source-asserted FM242 context. Four specified tetrahedral centres and one amide/imidic representation difference remain bounded; shared BGC context does not transfer notoamide A's mechanism or producer grades. Review is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2834; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-b68e89ca68 | data/natural_products/unclassified/notoamide-f.yaml | generated | notoamide F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-b68e89ca68 | Both exact stored forms parsed in the original twenty-attempt diagnostic and agree in formula, charge, normalized Standard InChI and complete key. |
| strict_ten | passed | True | naturalproductmech:mibig-b68e89ca68 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-b68e89ca68 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-b68e89ca68 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-b68e89ca68 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-b68e89ca68 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-b68e89ca68 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-b68e89ca68 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-b68e89ca68 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: naturalproductmech:mibig-b68e89ca68.

notoamide F retains exact identifier naturalproductmech:mibig-b68e89ca68, complete key RWPUAUNPEMCSNR-CZQHCSHRSA-N, and source rows BGC0002254 v3 compound index 1. Cross-references npatlas:NPA009414, pubchem:25180710 remain attributed identifiers, not fresh authority confirmation. Both saved forms normalize to C27H31N3O4 and the declared full key. Distinct source compounds and direct companions retain their own full keys; no identity, experimental grade or stereochemistry is transferred.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-b68e89ca68.

The saved notoamide F graph has eight overlapping ring rows in a connected 34-heavy-atom polycyclic structure. It retains an aromatic indole N–H system, a methoxy-bearing saturated centre, an N-containing five-membered ring, a bridged amide-containing system and an unsaturated oxygen-containing six-membered ring. Two strict amide sites and no strict ester are present in the source-SMILES form. Its C27H31N3O4 formula and full key remain distinct from notoamide A's C26H29N3O5/N-hydroxy oxindole topology. Both saved notoamide F forms contain four specified tetrahedral centres and no unspecified potential-stereo entry in the retained tables. The true source stereo_complete flag retains its atom-centred extraction scope; it is not proof of natural absolute configuration or a basis for transferring notoamide A's graph assertions. Both stored notoamide F forms normalize to the same Standard InChI, declared full key and neutral C27H31N3O4 formula. One secondary amide appears as C(OH)=N in the InChI-derived form, leaving one strict tertiary amide. Both canonical comparisons are false and the saved match is empty; full graph identity is not established. Formula and key agreement do not collapse its identity into notoamide A.

### Producer assertion versus locus evidence

provenance: supported. Targets: naturalproductmech:mibig-b68e89ca68.

BGC0002254 v3 assigns Aspergillus sp. FM242 (NCBITaxon:2741095) at SOURCE_ASSERTION. This source claim does not inherit the correlated MF297-2 producer grade attached to notoamide A through a different MIBiG entry. MT457561.1:1–46989 remains CLUSTER_UNSTATED, with questionable entry quality and unknown completeness. PMID:32433885 is ENTRY-scoped. Shared BGC0002254 context does not transfer notoamide A's other loci, native protein annotations, NotG inference or experimental grades.

### Citation grain and attributed history

evidence: supported. Targets: naturalproductmech:mibig-b68e89ca68.

BGC0002254: PMID:32433885 at ENTRY grain. These are attributed database citations, not newly examined primary bodies. DOI case variants and repeated placements do not create independent evidence. All 2 histories were read: 2 are seeder-attributed SEEDED_FROM_SOURCES events.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: naturalproductmech:mibig-b68e89ca68.

Three LOTUS Aspergillus 5052 occurrences retain DOI 10.1002/CHIN.200728180, 10.1021/ACS.ORGLETT.0C01411 and 10.1021/NP800471Y. They are attributed occurrence references, not independent experimental confirmations or activity evidence. The saved PubChem BioAssay frame has no row or blank sentinel for this owner. No actual AID or molecular target is captured. ChEBI structure/origin, CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not global absence, inactivity, potency or target-mechanism proof.

### Computed filing and asserted class applicability

consistency: supported. Targets: naturalproductmech:mibig-b68e89ca68.

NPClassifier retains Alkaloids plus Amino acids and Peptides, Peptide alkaloids and Indole diketopiperazine alkaloids (L-Trp, L-Pro), while BGC0002254 supplies a PKS source class. These are distinct annotation systems, not evidence of a resolved biosynthetic disagreement. The aromatic indole and amide-containing topology supports bounded structural classification; two model pathways retain UNCLASSIFIED.

### Local completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-b68e89ca68.

The complete current owner is carried from BGC Science’s attributed complete owner reading and exact current raw/capture equality. All 2 histories, nine saved source frames (5 positive placements/50 fields and 6 negatives), and both complete saved molecular forms were personally read. All 49 actual input hashes and maintained ownership paths join the accepted plan. Input pinning is not a claim to have substantively read every entire corpus. Five original local gates passed. The complete owner root set has no positive graph, pathway, component or molecular-target root, so no maintained reader applies. Full QC/OAK, fresh source-authority checks and independent primary confirmation remain unavailable; completion is partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2834-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/notoamide-f.yaml; Complete plaintext, every root and all curation_history entries | supports | Complete current owner carried from BGC Science’s attributed complete owner reading and joined exactly to capture; current source/history meanings were personally read. |
| bgc-2834-whole-owner-attribution | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-ten-owner-root-history-preview-001.json; /records | context_only | BGC Science personally read these complete selected owners and histories in the pinned preview; exact raw/capture equality carries that reading without duplicate credit. |
| bgc-2834-identity | /private/tmp/npm-review-work/shared-next-batch284/owner-capture-DATA-001.json; /records/3/owner_document/identifier; /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status | supports | notoamide F retains exact identifier naturalproductmech:mibig-b68e89ca68, complete key RWPUAUNPEMCSNR-CZQHCSHRSA-N, and source rows BGC0002254 v3 compound index 1. Cross-references npatlas:NPA009414, pubchem:25180710 remain attributed identifiers, not fresh authority confirmation. Both saved forms normalize to C27H31N3O4 and the declared full key. Distinct source compounds and direct companions retain their own full keys; no identity, experimental grade or stereochemistry is transferred. |
| bgc-2834-history | /private/tmp/npm-review-work/shared-next-batch284/owner-capture-DATA-001.json; /records/3/owner_document/curation_history | supports | BGC0002254: PMID:32433885 at ENTRY grain. These are attributed database citations, not newly examined primary bodies. DOI case variants and repeated placements do not create independent evidence. All 2 histories were read: 2 are seeder-attributed SEEDED_FROM_SOURCES events. |
| bgc-2834-provenance | /private/tmp/npm-review-work/shared-next-batch284/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters | supports | BGC0002254 v3 assigns Aspergillus sp. FM242 (NCBITaxon:2741095) at SOURCE_ASSERTION. This source claim does not inherit the correlated MF297-2 producer grade attached to notoamide A through a different MIBiG entry. MT457561.1:1–46989 remains CLUSTER_UNSTATED, with questionable entry quality and unknown completeness. PMID:32433885 is ENTRY-scoped. Shared BGC0002254 context does not transfer notoamide A's other loci, native protein annotations, NotG inference or experimental grades. |
| bgc-2834-classification | /private/tmp/npm-review-work/shared-next-batch284/owner-capture-DATA-001.json; /records/3/owner_document/np_classification; /records/3/owner_document/np_pathway; /records/3/owner_document/bgc_class | supports | NPClassifier retains Alkaloids plus Amino acids and Peptides, Peptide alkaloids and Indole diketopiperazine alkaloids (L-Trp, L-Pro), while BGC0002254 supplies a PKS source class. These are distinct annotation systems, not evidence of a resolved biosynthetic disagreement. The aromatic indole and amide-containing topology supports bounded structural classification; two model pathways retain UNCLASSIFIED. |
| bgc-2834-roots | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json; /contexts/8/complete_root_keys; /contexts/8/declared_mechanism_roots_literal; /contexts/8/literal_bioactivities_root | context_only | The complete owner root set has no positive graph, pathway, component or molecular-target root, so no maintained reader applies. |
| bgc-2834-chemistry | /private/tmp/npm-review-work/shared-next-batch284/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons; /records/3/atom_correspondence; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/declared_structure | supports | The saved notoamide F graph has eight overlapping ring rows in a connected 34-heavy-atom polycyclic structure. It retains an aromatic indole N–H system, a methoxy-bearing saturated centre, an N-containing five-membered ring, a bridged amide-containing system and an unsaturated oxygen-containing six-membered ring. Two strict amide sites and no strict ester are present in the source-SMILES form. Its C27H31N3O4 formula and full key remain distinct from notoamide A's C26H29N3O5/N-hydroxy oxindole topology. Both saved notoamide F forms contain four specified tetrahedral centres and no unspecified potential-stereo entry in the retained tables. The true source stereo_complete flag retains its atom-centred extraction scope; it is not proof of natural absolute configuration or a basis for transferring notoamide A's graph assertions. Both stored notoamide F forms normalize to the same Standard InChI, declared full key and neutral C27H31N3O4 formula. One secondary amide appears as C(OH)=N in the InChI-derived form, leaving one strict tertiary amide. Both canonical comparisons are false and the saved match is empty; full graph identity is not established. Formula and key agreement do not collapse its identity into notoamide A. |
| bgc-2834-molecular-reading | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-current284-first-five-molecular-intake-reading-001.json; /records/3; /personal_reading_scope; /global_cautions | supports | Complete saved tables personally read and interpreted without a new parse. |
| bgc-2834-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch284/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /DATA; /molecular_parse_attempts; /scientific_limits | supports | ROOT accepted the original twenty stored-form attempts; exact representation and identity limits remain. |
| bgc-2834-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch284/chemistry-local/diagnostic-execution-001.json; /command; /exit_code | supports | Original ROOT diagnostic command and exit zero; no replay. |
| bgc-2834-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch284/chemistry-local/diagnostic-original-001.stderr; Complete original stderr including blank separators | context_only | The original diagnostic stderr is empty; no warning or unreported stereochemical assignment is inferred. |
| bgc-2834-intake | /private/tmp/npm-review-work/shared-next-batch284/intakes-001/2834-inspect-001.json; /targets; /source/inputs | supports | One exact target, 49 current inputs and explicit maintained ownership paths. |
| bgc-2834-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch284/root-current284-intakes-acceptance-001.json; /accepted; /summary; /records; /source_placements; /unique_source_paths | supports | All ten original inspections exited zero with empty stderr and 458 placements/63 paths. |
| bgc-2834-plan | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-target-input-plan-001.json; /records/3 | supports | Exact current input map, 5 direct companions and the literal reader applicability. |
| bgc-2834-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch284/root-current284-source-plan-acceptance-001.json; /accepted; /source_plan; /source_placements; /unique_source_paths | supports | ROOT accepted the current source input plan. |
| bgc-2834-gates | /private/tmp/npm-review-work/shared-next-batch284/root-current284-five-gates-acceptance-001.json; /five_local_commands_passed; /commands; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows | context_only | Five local gates passed; queue rows are review leads, not findings. Full QC/OAK remain unavailable. |
| bgc-2834-source-reading | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-current284-assigned-source-reading-001.json; /contexts/8; /counts; /reading_attribution | supports | All 5 complete positive dictionaries/50 fields and 6 bounded negative frames were personally read in the attributed source pass. |
| bgc-2834-source-notes | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-scope-notes-001.json; /totals; /reading_reconciliation; /reading_boundaries | context_only | The original 77 source placements/994 fields retain BGC 55 and Support 22 primary-row attribution; Native and ROOT have zero primary-row credit. |
| bgc-2834-taxonomy | /private/tmp/npm-review-work/shared-next-batch284-tentative/native-prep/native-current284-cached-taxonomy-reading-002.json; /scope; /context_interpretations/8; /interpretation | context_only | BGC0002254 v3 assigns Aspergillus sp. FM242 (NCBITaxon:2741095) at SOURCE_ASSERTION. This source claim does not inherit the correlated MF297-2 producer grade attached to notoamide A through a different MIBiG entry. Cached names do not independently supply rank, lineage or strain-level evidence. |
| bgc-2834-curation | /private/tmp/npm-review-work/shared-next-batch284-tentative/native-prep/native-current284-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation | context_only | Native reports nine substantive tables/3,422 rows and 119 lexical candidates with zero exact applicable decisions. Ninety-three complete unchanged candidate rows/rationales carry by exact prior attribution; 26 current diagnostics were freshly read. Two reserved census-only tables are excluded. |
| bgc-2834-assay-curation | /private/tmp/npm-review-work/shared-next-batch284-tentative/native-prep/native-current284-implemented-curation-scan-001.json; /assay_scope | context_only | The saved PubChem BioAssay frame has no row or blank sentinel for this owner. No actual AID or molecular target is captured. ChEBI structure/origin, CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not global absence, inactivity, potency or target-mechanism proof. |
| bgc-2834-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters(includeUnassigned=True) | context_only | The source stereo_complete flag tests unassigned atom-centred chirality, not all double-bond geometry or natural identity. |
| bgc-2834-stereo-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392-397: chemical_structure.stereo_complete | context_only | Schema preserves undefined stereocentres rather than inventing them; the maintained source extractor defines the actual atom-centre test. |
| bgc-2834-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306: choose_pathway | context_only | Exactly one supported mapped pathway selects filing; zero, unsupported single or multiple labels retain UNCLASSIFIED. |
| bgc-2834-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 positive placements, with all fields and bounded query meanings read. |
| bgc-2834-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 2700-2700; raw record sha256 e23acce827c39908cf0269d624f7a46d39d93f8af00b40c05d7d0a8e3f344f7e | supports | All 25 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2834-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2834-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 3 positive placements, with all fields and bounded query meanings read. |
| bgc-2834-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 8253-8253; raw record sha256 66789b299761b5fd5cad996a18da2f136e3a8557180bb2c8a40580e439ec0f7b | supports | All 6 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2834-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 8254-8254; raw record sha256 39fe5457b79c823b6f767ecf03f803430f9b5d279c4761769b9e1cd63d7b52fb | supports | All 6 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2834-row-lotus_occurrences-2 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 8255-8255; raw record sha256 dfd15db0acf84ea64a910934d15bcccab50488845624bd5d00cfe150a237b253 | supports | All 6 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2834-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2834-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 positive placements, with all fields and bounded query meanings read. |
| bgc-2834-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2187-2187; raw record sha256 bc4a4ae983604139912599e18a54dc9e900b8dd52272e468022be9717526dd88 | supports | All 7 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2834-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/pubchem_bioassay | context_only | Complete saved pubchem_bioassay frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2834-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2834-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2834-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2834-congener-0 | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/semivioxanthin.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2834-congener-1 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/notoamide-a.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2834-congener-2 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/waikikiamide-a.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2834-congener-3 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/waikikiamide-b.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2834-congener-4 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/waikikiamide-c.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-284/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-284/native-current284-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-284/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-284/native-current284-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-284/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-284/native-current284-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-284/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-284/native-current284-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-284/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-284/native-current284-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Fresh source-authority, primary publication, sequence and strain verification remain unavailable. Full QC/OAK were not run; retained experimental grades stay source-attributed.
- Both stored notoamide F forms normalize to the same Standard InChI, declared full key and neutral C27H31N3O4 formula. One secondary amide appears as C(OH)=N in the InChI-derived form, leaving one strict tertiary amide. Both canonical comparisons are false and the saved match is empty; full graph identity is not established. Formula and key agreement do not collapse its identity into notoamide A. The original diagnostic stderr is empty; no warning or unreported stereochemical assignment is inferred.
- Both saved notoamide F forms contain four specified tetrahedral centres and no unspecified potential-stereo entry in the retained tables. The true source stereo_complete flag retains its atom-centred extraction scope; it is not proof of natural absolute configuration or a basis for transferring notoamide A's graph assertions.
- Saved topology supports the encoded molecule without independently establishing every natural residue, biosynthetic reaction or pharmacological mechanism.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- No record, source table, native scientific status or curation history is modified. Corrections, if later justified, belong in maintained source/curation/extractor ownership; curated mechanism changes require validated writing and attributed history.
- This author interpreted retained original outputs only, with zero molecular parses, source-query replays, target runs or outbound requests.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T060415Z-notoamide-f
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: notoamide F'
started_at: '2026-11-07T05:22:53.386311Z'
finished_at: '2026-11-07T06:04:15.628915Z'
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
summary: Notoamide F retains its own aromatic indole/methoxy topology, full key and
  source-asserted FM242 context. Four specified tetrahedral centres and one amide/imidic
  representation difference remain bounded; shared BGC context does not transfer notoamide
  A's mechanism or producer grades. Review is partial.
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/semivioxanthin.yaml
    sha256: 831a3278dcb075d1d2ec4d35beb91cfe13ede3eec9ab67ff9f7cd4adbf7635fd
    role: context
  - path: data/natural_products/unclassified/notoamide-a.yaml
    sha256: 7549b9dca8f87ef4def6f8859de7a9a7aef387b9573bce863b42a2bca9daee28
    role: context
  - path: data/natural_products/unclassified/notoamide-f.yaml
    sha256: d8379848d5196a34b9ef86ad6e56c3bbd8c7105d6ad045b4cd05ee75a55e8091
    role: target
  - path: data/natural_products/unclassified/waikikiamide-a.yaml
    sha256: 20db88c6f052686619eb1aa4aec4903eea52bdf4dec508181d8f3344f15042fa
    role: context
  - path: data/natural_products/unclassified/waikikiamide-b.yaml
    sha256: 9f551202f245f1ffa04cece0258a1bc1b72f54ae46ef53c164ce1f95e783d667
    role: context
  - path: data/natural_products/unclassified/waikikiamide-c.yaml
    sha256: 4efb10942ebef081df90f74dcb43d6ea8bbc87bb5b4efb032ca198a48c681c93
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
  selection: Campaign path order 2834; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-b68e89ca68
targets:
- target_id: naturalproductmech:mibig-b68e89ca68
  path: data/natural_products/unclassified/notoamide-f.yaml
  label: notoamide F
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch284/chemistry-local/diagnose284-001.py
    fee2df0fa3229718cc54bd2e3ceb6a8eec00840ac6433f51fcd525d7d72f1e55 d19813831e56b948759cf98208273ce2955cc726475fcb17c1f38949216e4e16
    15eca5f442de3d257c360ea99912a73c615dbf8996c8a6d167a1f89f1fe1aa1a
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both exact stored forms parsed in the original twenty-attempt diagnostic
    and agree in formula, charge, normalized Standard InChI and complete key.
  scope_note: Both stored notoamide F forms normalize to the same Standard InChI,
    declared full key and neutral C27H31N3O4 formula. One secondary amide appears
    as C(OH)=N in the InChI-derived form, leaving one strict tertiary amide. Both
    canonical comparisons are false and the saved match is empty; full graph identity
    is not established. Formula and key agreement do not collapse its identity into
    notoamide A. The original diagnostic stderr is empty; no warning or unreported
    stereochemical assignment is inferred.
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  evidence_ids:
  - bgc-2834-chemistry
  - bgc-2834-diagnostic-acceptance
  - bgc-2834-diagnostic-execution
  - bgc-2834-diagnostic-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  command: just validate-strict data/natural_products/unclassified/nordidemnin-b.yaml
    data/natural_products/unclassified/nostopeptolide-a2.yaml data/natural_products/unclassified/notoamide-a.yaml
    data/natural_products/unclassified/notoamide-f.yaml data/natural_products/unclassified/novofumigatonin.yaml
    data/natural_products/unclassified/ohmyungsamycin-a.yaml data/natural_products/unclassified/ohmyungsamycin-b.yaml
    data/natural_products/unclassified/okaramine-b.yaml data/natural_products/unclassified/okaramine-d.yaml
    data/natural_products/unclassified/omnipeptin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-284/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-b68e89ca68
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-284/validate-all-001.tsv
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
  - naturalproductmech:mibig-b68e89ca68
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
  - naturalproductmech:mibig-b68e89ca68
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
  - naturalproductmech:mibig-b68e89ca68
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-284/review-queue-001.tsv
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
  - naturalproductmech:mibig-b68e89ca68
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2834-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/notoamide-f.yaml
  locator: Complete plaintext, every root and all curation_history entries
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: Complete current owner carried from BGC Science’s attributed complete owner
    reading and joined exactly to capture; current source/history meanings were personally
    read.
  snapshot_sha256: d8379848d5196a34b9ef86ad6e56c3bbd8c7105d6ad045b4cd05ee75a55e8091
- evidence_id: bgc-2834-whole-owner-attribution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-ten-owner-root-history-preview-001.json
  locator: /records
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: BGC Science personally read these complete selected owners and histories
    in the pinned preview; exact raw/capture equality carries that reading without
    duplicate credit.
  snapshot_sha256: 94b03b1f31eab632d7cd6257f96a7589ad79b17c15249eee24493b2fbe8a3b98
- evidence_id: bgc-2834-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch284/owner-capture-DATA-001.json
  locator: /records/3/owner_document/identifier; /records/3/owner_document/chemical_structure;
    /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: notoamide F retains exact identifier naturalproductmech:mibig-b68e89ca68,
    complete key RWPUAUNPEMCSNR-CZQHCSHRSA-N, and source rows BGC0002254 v3 compound
    index 1. Cross-references npatlas:NPA009414, pubchem:25180710 remain attributed
    identifiers, not fresh authority confirmation. Both saved forms normalize to C27H31N3O4
    and the declared full key. Distinct source compounds and direct companions retain
    their own full keys; no identity, experimental grade or stereochemistry is transferred.
  snapshot_sha256: d19813831e56b948759cf98208273ce2955cc726475fcb17c1f38949216e4e16
- evidence_id: bgc-2834-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch284/owner-capture-DATA-001.json
  locator: /records/3/owner_document/curation_history
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: 'BGC0002254: PMID:32433885 at ENTRY grain. These are attributed database
    citations, not newly examined primary bodies. DOI case variants and repeated placements
    do not create independent evidence. All 2 histories were read: 2 are seeder-attributed
    SEEDED_FROM_SOURCES events.'
  snapshot_sha256: d19813831e56b948759cf98208273ce2955cc726475fcb17c1f38949216e4e16
- evidence_id: bgc-2834-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch284/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: BGC0002254 v3 assigns Aspergillus sp. FM242 (NCBITaxon:2741095) at SOURCE_ASSERTION.
    This source claim does not inherit the correlated MF297-2 producer grade attached
    to notoamide A through a different MIBiG entry. MT457561.1:1–46989 remains CLUSTER_UNSTATED,
    with questionable entry quality and unknown completeness. PMID:32433885 is ENTRY-scoped.
    Shared BGC0002254 context does not transfer notoamide A's other loci, native protein
    annotations, NotG inference or experimental grades.
  snapshot_sha256: d19813831e56b948759cf98208273ce2955cc726475fcb17c1f38949216e4e16
- evidence_id: bgc-2834-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch284/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_classification; /records/3/owner_document/np_pathway;
    /records/3/owner_document/bgc_class
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: NPClassifier retains Alkaloids plus Amino acids and Peptides, Peptide alkaloids
    and Indole diketopiperazine alkaloids (L-Trp, L-Pro), while BGC0002254 supplies
    a PKS source class. These are distinct annotation systems, not evidence of a resolved
    biosynthetic disagreement. The aromatic indole and amide-containing topology supports
    bounded structural classification; two model pathways retain UNCLASSIFIED.
  snapshot_sha256: d19813831e56b948759cf98208273ce2955cc726475fcb17c1f38949216e4e16
- evidence_id: bgc-2834-roots
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json
  locator: /contexts/8/complete_root_keys; /contexts/8/declared_mechanism_roots_literal;
    /contexts/8/literal_bioactivities_root
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: The complete owner root set has no positive graph, pathway, component or
    molecular-target root, so no maintained reader applies.
  snapshot_sha256: 2a868582e28cbf5248d0c804cabc0ee8e64fdbe4852902e7f1525bbe36b4e118
  search_scope: Complete captured owner root set, not a biological absence claim.
- evidence_id: bgc-2834-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch284/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons;
    /records/3/atom_correspondence; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds;
    /records/2/declared_structure
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: The saved notoamide F graph has eight overlapping ring rows in a connected
    34-heavy-atom polycyclic structure. It retains an aromatic indole N–H system,
    a methoxy-bearing saturated centre, an N-containing five-membered ring, a bridged
    amide-containing system and an unsaturated oxygen-containing six-membered ring.
    Two strict amide sites and no strict ester are present in the source-SMILES form.
    Its C27H31N3O4 formula and full key remain distinct from notoamide A's C26H29N3O5/N-hydroxy
    oxindole topology. Both saved notoamide F forms contain four specified tetrahedral
    centres and no unspecified potential-stereo entry in the retained tables. The
    true source stereo_complete flag retains its atom-centred extraction scope; it
    is not proof of natural absolute configuration or a basis for transferring notoamide
    A's graph assertions. Both stored notoamide F forms normalize to the same Standard
    InChI, declared full key and neutral C27H31N3O4 formula. One secondary amide appears
    as C(OH)=N in the InChI-derived form, leaving one strict tertiary amide. Both
    canonical comparisons are false and the saved match is empty; full graph identity
    is not established. Formula and key agreement do not collapse its identity into
    notoamide A.
  snapshot_sha256: 4d515cf6af4916a87211ec7d797e172e062a8d2b42ce6804c4e7dbd72d07d1e4
- evidence_id: bgc-2834-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-current284-first-five-molecular-intake-reading-001.json
  locator: /records/3; /personal_reading_scope; /global_cautions
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: Complete saved tables personally read and interpreted without a new parse.
  snapshot_sha256: 98f17c2201f1d11e41cee85acee2401ed7b9b1ef8e985c00f4c097f390db4459
- evidence_id: bgc-2834-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch284/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /DATA; /molecular_parse_attempts; /scientific_limits
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form attempts; exact representation
    and identity limits remain.
  snapshot_sha256: e1cf5638534b0341ff6e9e94b874341c0390f20e7b3cd873eb8caafee620fba1
- evidence_id: bgc-2834-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch284/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: Original ROOT diagnostic command and exit zero; no replay.
  snapshot_sha256: aa364bcaa8f24ac8141f02937b8a996ca0d2a8a1a79854f5a32f9cf041549f62
- evidence_id: bgc-2834-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch284/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr including blank separators
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: The original diagnostic stderr is empty; no warning or unreported stereochemical
    assignment is inferred.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: bgc-2834-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch284/intakes-001/2834-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: One exact target, 49 current inputs and explicit maintained ownership paths.
  snapshot_sha256: 8adb50195164e4960eddcde813144d713b3e3067420dac7cf81c50d32fef35bb
- evidence_id: bgc-2834-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch284/root-current284-intakes-acceptance-001.json
  locator: /accepted; /summary; /records; /source_placements; /unique_source_paths
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: All ten original inspections exited zero with empty stderr and 458 placements/63
    paths.
  snapshot_sha256: ee87b9cbdc66d2b8070bb7f1492c8ce7c4576d9ececbaa66ce1c376d2fbb48fa
- evidence_id: bgc-2834-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-target-input-plan-001.json
  locator: /records/3
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: Exact current input map, 5 direct companions and the literal reader applicability.
  snapshot_sha256: 3b58af03b49be800848e62c42c2d67413ac10c0102f30f38aa2f07c1124f6057
- evidence_id: bgc-2834-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch284/root-current284-source-plan-acceptance-001.json
  locator: /accepted; /source_plan; /source_placements; /unique_source_paths
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: ROOT accepted the current source input plan.
  snapshot_sha256: d873d295f85383f303be7815b63658fdde0b1f25fdc23e2e1c6aaef5377b0879
- evidence_id: bgc-2834-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch284/root-current284-five-gates-acceptance-001.json
  locator: /five_local_commands_passed; /commands; /all_native_gates_passed; /unavailable_required_gates;
    /selected_queue_rows
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: Five local gates passed; queue rows are review leads, not findings. Full
    QC/OAK remain unavailable.
  snapshot_sha256: fbcd5b4d249a50b2b5d34106be33f0f99989d0ead081bc0138cc68d1897fe1d6
- evidence_id: bgc-2834-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-current284-assigned-source-reading-001.json
  locator: /contexts/8; /counts; /reading_attribution
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: All 5 complete positive dictionaries/50 fields and 6 bounded negative frames
    were personally read in the attributed source pass.
  snapshot_sha256: 68eac1bc1a034a97bfe07959ace606c3f2733fa441704d62c111b9216e9d468d
- evidence_id: bgc-2834-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: The original 77 source placements/994 fields retain BGC 55 and Support
    22 primary-row attribution; Native and ROOT have zero primary-row credit.
  snapshot_sha256: a22b999b10a22c88033cd8cd3000064ae4aa501d373c81f98b700b70ad198b76
- evidence_id: bgc-2834-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/native-prep/native-current284-cached-taxonomy-reading-002.json
  locator: /scope; /context_interpretations/8; /interpretation
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: BGC0002254 v3 assigns Aspergillus sp. FM242 (NCBITaxon:2741095) at SOURCE_ASSERTION.
    This source claim does not inherit the correlated MF297-2 producer grade attached
    to notoamide A through a different MIBiG entry. Cached names do not independently
    supply rank, lineage or strain-level evidence.
  snapshot_sha256: 6c86b733e64c674636503384d948010ec43e2abbb4314f4699052ac9d4fb314a
  search_scope: Exact current taxon route and retained cached names/synonyms; no fresh
    external taxonomy or inferred hierarchy.
- evidence_id: bgc-2834-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/native-prep/native-current284-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: Native reports nine substantive tables/3,422 rows and 119 lexical candidates
    with zero exact applicable decisions. Ninety-three complete unchanged candidate
    rows/rationales carry by exact prior attribution; 26 current diagnostics were
    freshly read. Two reserved census-only tables are excluded.
  snapshot_sha256: 76cf06304d1cc03019cced74e6d4a8e60d8e481915c0a35677107bd89afbade5
  search_scope: Actual captured table inputs and exact identity/source/occurrence/assay
    predicates; no decision from lexical similarity.
- evidence_id: bgc-2834-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/native-prep/native-current284-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: The saved PubChem BioAssay frame has no row or blank sentinel for this
    owner. No actual AID or molecular target is captured. ChEBI structure/origin,
    CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not
    global absence, inactivity, potency or target-mechanism proof.
  snapshot_sha256: 76cf06304d1cc03019cced74e6d4a8e60d8e481915c0a35677107bd89afbade5
  search_scope: Exact owner full-key/CID scope; blank-AID rows are sentinels. No other-owner
    assay is transferred.
- evidence_id: bgc-2834-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters(includeUnassigned=True)'
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: The source stereo_complete flag tests unassigned atom-centred chirality,
    not all double-bond geometry or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2834-stereo-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: 'lines 392-397: chemical_structure.stereo_complete'
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: Schema preserves undefined stereocentres rather than inventing them; the
    maintained source extractor defines the actual atom-centre test.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2834-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines 295-306: choose_pathway'
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: Exactly one supported mapped pathway selects filing; zero, unsupported
    single or multiple labels retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2834-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 2a868582e28cbf5248d0c804cabc0ee8e64fdbe4852902e7f1525bbe36b4e118
- evidence_id: bgc-2834-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 2700-2700; raw record sha256 e23acce827c39908cf0269d624f7a46d39d93f8af00b40c05d7d0a8e3f344f7e
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: All 25 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2834-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: 'Complete saved chebi_structures frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 2a868582e28cbf5248d0c804cabc0ee8e64fdbe4852902e7f1525bbe36b4e118
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/notoamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RWPUAUNPEMCSNR-CZQHCSHRSA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2834-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 3 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 2a868582e28cbf5248d0c804cabc0ee8e64fdbe4852902e7f1525bbe36b4e118
- evidence_id: bgc-2834-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 8253-8253; raw record sha256 66789b299761b5fd5cad996a18da2f136e3a8557180bb2c8a40580e439ec0f7b
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: All 6 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2834-row-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 8254-8254; raw record sha256 39fe5457b79c823b6f767ecf03f803430f9b5d279c4761769b9e1cd63d7b52fb
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: All 6 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2834-row-lotus_occurrences-2
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 8255-8255; raw record sha256 dfd15db0acf84ea64a910934d15bcccab50488845624bd5d00cfe150a237b253
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: All 6 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2834-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences frame: 0 positive placements, with
    all fields and bounded query meanings read.'
  snapshot_sha256: 2a868582e28cbf5248d0c804cabc0ee8e64fdbe4852902e7f1525bbe36b4e118
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/notoamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RWPUAUNPEMCSNR-CZQHCSHRSA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2834-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 positive placements, with all fields
    and bounded query meanings read.'
  snapshot_sha256: 2a868582e28cbf5248d0c804cabc0ee8e64fdbe4852902e7f1525bbe36b4e118
- evidence_id: bgc-2834-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2187-2187; raw record sha256 bc4a4ae983604139912599e18a54dc9e900b8dd52272e468022be9717526dd88
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: supports
  summary: All 7 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2834-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: 'Complete saved pubchem_bioassay frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 2a868582e28cbf5248d0c804cabc0ee8e64fdbe4852902e7f1525bbe36b4e118
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/notoamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RWPUAUNPEMCSNR-CZQHCSHRSA-N",
    "table": "pubchem_bioassay"}'
- evidence_id: bgc-2834-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 2a868582e28cbf5248d0c804cabc0ee8e64fdbe4852902e7f1525bbe36b4e118
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/notoamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RWPUAUNPEMCSNR-CZQHCSHRSA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2834-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 positive placements,
    with all fields and bounded query meanings read.'
  snapshot_sha256: 2a868582e28cbf5248d0c804cabc0ee8e64fdbe4852902e7f1525bbe36b4e118
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/notoamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RWPUAUNPEMCSNR-CZQHCSHRSA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2834-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch284-tentative/bgc-prep/bgc-conditional284-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: 'Complete saved chebi_origins frame: 0 positive placements, with all fields
    and bounded query meanings read.'
  snapshot_sha256: 2a868582e28cbf5248d0c804cabc0ee8e64fdbe4852902e7f1525bbe36b4e118
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/notoamide-f.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: bgc-2834-congener-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/semivioxanthin.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 831a3278dcb075d1d2ec4d35beb91cfe13ede3eec9ab67ff9f7cd4adbf7635fd
- evidence_id: bgc-2834-congener-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/notoamide-a.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 7549b9dca8f87ef4def6f8859de7a9a7aef387b9573bce863b42a2bca9daee28
- evidence_id: bgc-2834-congener-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/waikikiamide-a.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 20db88c6f052686619eb1aa4aec4903eea52bdf4dec508181d8f3344f15042fa
- evidence_id: bgc-2834-congener-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/waikikiamide-b.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 9f551202f245f1ffa04cece0258a1bc1b72f54ae46ef53c164ce1f95e783d667
- evidence_id: bgc-2834-congener-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/waikikiamide-c.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T05:54:08.616004Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 4efb10942ebef081df90f74dcb43d6ea8bbc87bb5b4efb032ca198a48c681c93
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-284/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-284/native-current284-five-gates-execution-001.json
  accessed_at: '2026-11-07T05:25:04.360988Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 46d507058c4ad052e82dc7932d9a8d1dc76106d8d334124d166cd7077a1c1dcb
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-284/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-284/native-current284-five-gates-execution-001.json
  accessed_at: '2026-11-07T05:25:30.149947Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 89a98dac1c1d60b5cb0326ab82136381ab76e2e5f32ddc2d71d8068468f59ea2
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-284/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-284/native-current284-five-gates-execution-001.json
  accessed_at: '2026-11-07T05:25:50.191692Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-284/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-284/native-current284-five-gates-execution-001.json
  accessed_at: '2026-11-07T05:26:25.152760Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-284/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-284/native-current284-five-gates-execution-001.json
  accessed_at: '2026-11-07T05:26:37.318331Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: a66384e031da0128485e4c4f2acd7352ef34e0d86ac6f013495d1669763be2e6
assessments:
- assessment_id: bgc-2834-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: notoamide F retains exact identifier naturalproductmech:mibig-b68e89ca68,
    complete key RWPUAUNPEMCSNR-CZQHCSHRSA-N, and source rows BGC0002254 v3 compound
    index 1. Cross-references npatlas:NPA009414, pubchem:25180710 remain attributed
    identifiers, not fresh authority confirmation. Both saved forms normalize to C27H31N3O4
    and the declared full key. Distinct source compounds and direct companions retain
    their own full keys; no identity, experimental grade or stereochemistry is transferred.
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  evidence_ids:
  - bgc-2834-identity
  - bgc-2834-whole-owner-attribution
  - bgc-2834-chemistry
  - bgc-2834-query-mibig_compounds
  - bgc-2834-plan
  - bgc-2834-row-mibig_compounds-0
  - bgc-2834-congener-0
  - bgc-2834-congener-1
  - bgc-2834-congener-2
  - bgc-2834-congener-3
  - bgc-2834-congener-4
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    value: RWPUAUNPEMCSNR-CZQHCSHRSA-N
    evidence_ids:
    - bgc-2834-identity
    - bgc-2834-whole-owner-attribution
    - bgc-2834-chemistry
    - bgc-2834-query-mibig_compounds
    - bgc-2834-plan
    - bgc-2834-row-mibig_compounds-0
    - bgc-2834-congener-0
    - bgc-2834-congener-1
    - bgc-2834-congener-2
    - bgc-2834-congener-3
    - bgc-2834-congener-4
  - name: grounding_scope
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    value: notoamide F retains exact identifier naturalproductmech:mibig-b68e89ca68,
      complete key RWPUAUNPEMCSNR-CZQHCSHRSA-N, and source rows BGC0002254 v3 compound
      index 1. Cross-references npatlas:NPA009414, pubchem:25180710 remain attributed
      identifiers, not fresh authority confirmation. Both saved forms normalize to
      C27H31N3O4 and the declared full key. Distinct source compounds and direct companions
      retain their own full keys; no identity, experimental grade or stereochemistry
      is transferred.
    evidence_ids:
    - bgc-2834-identity
    - bgc-2834-whole-owner-attribution
    - bgc-2834-chemistry
    - bgc-2834-query-mibig_compounds
    - bgc-2834-plan
    - bgc-2834-row-mibig_compounds-0
    - bgc-2834-congener-0
    - bgc-2834-congener-1
    - bgc-2834-congener-2
    - bgc-2834-congener-3
    - bgc-2834-congener-4
- assessment_id: bgc-2834-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: The saved notoamide F graph has eight overlapping ring rows in a connected
    34-heavy-atom polycyclic structure. It retains an aromatic indole N–H system,
    a methoxy-bearing saturated centre, an N-containing five-membered ring, a bridged
    amide-containing system and an unsaturated oxygen-containing six-membered ring.
    Two strict amide sites and no strict ester are present in the source-SMILES form.
    Its C27H31N3O4 formula and full key remain distinct from notoamide A's C26H29N3O5/N-hydroxy
    oxindole topology. Both saved notoamide F forms contain four specified tetrahedral
    centres and no unspecified potential-stereo entry in the retained tables. The
    true source stereo_complete flag retains its atom-centred extraction scope; it
    is not proof of natural absolute configuration or a basis for transferring notoamide
    A's graph assertions. Both stored notoamide F forms normalize to the same Standard
    InChI, declared full key and neutral C27H31N3O4 formula. One secondary amide appears
    as C(OH)=N in the InChI-derived form, leaving one strict tertiary amide. Both
    canonical comparisons are false and the saved match is empty; full graph identity
    is not established. Formula and key agreement do not collapse its identity into
    notoamide A.
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  evidence_ids:
  - bgc-2834-identity
  - bgc-2834-chemistry
  - bgc-2834-molecular-reading
  - bgc-2834-diagnostic-acceptance
  - bgc-2834-diagnostic-stderr
  - bgc-2834-stereo-policy
  - bgc-2834-stereo-schema
  dimensions:
  - name: stereochemistry_scope
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    value: Both saved notoamide F forms contain four specified tetrahedral centres
      and no unspecified potential-stereo entry in the retained tables. The true source
      stereo_complete flag retains its atom-centred extraction scope; it is not proof
      of natural absolute configuration or a basis for transferring notoamide A's
      graph assertions.
    evidence_ids:
    - bgc-2834-identity
    - bgc-2834-chemistry
    - bgc-2834-molecular-reading
    - bgc-2834-diagnostic-acceptance
    - bgc-2834-diagnostic-stderr
    - bgc-2834-stereo-policy
    - bgc-2834-stereo-schema
  - name: representation_correspondence
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    value: Both stored notoamide F forms normalize to the same Standard InChI, declared
      full key and neutral C27H31N3O4 formula. One secondary amide appears as C(OH)=N
      in the InChI-derived form, leaving one strict tertiary amide. Both canonical
      comparisons are false and the saved match is empty; full graph identity is not
      established. Formula and key agreement do not collapse its identity into notoamide
      A.
    evidence_ids:
    - bgc-2834-identity
    - bgc-2834-chemistry
    - bgc-2834-molecular-reading
    - bgc-2834-diagnostic-acceptance
    - bgc-2834-diagnostic-stderr
    - bgc-2834-stereo-policy
    - bgc-2834-stereo-schema
- assessment_id: bgc-2834-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: BGC0002254 v3 assigns Aspergillus sp. FM242 (NCBITaxon:2741095) at SOURCE_ASSERTION.
    This source claim does not inherit the correlated MF297-2 producer grade attached
    to notoamide A through a different MIBiG entry. MT457561.1:1–46989 remains CLUSTER_UNSTATED,
    with questionable entry quality and unknown completeness. PMID:32433885 is ENTRY-scoped.
    Shared BGC0002254 context does not transfer notoamide A's other loci, native protein
    annotations, NotG inference or experimental grades.
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  evidence_ids:
  - bgc-2834-provenance
  - bgc-2834-query-mibig_compounds
  - bgc-2834-taxonomy
  - bgc-2834-curation
  - bgc-2834-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    value: BGC0002254 v3 assigns Aspergillus sp. FM242 (NCBITaxon:2741095) at SOURCE_ASSERTION.
      This source claim does not inherit the correlated MF297-2 producer grade attached
      to notoamide A through a different MIBiG entry.
    evidence_ids:
    - bgc-2834-provenance
    - bgc-2834-query-mibig_compounds
    - bgc-2834-taxonomy
    - bgc-2834-curation
    - bgc-2834-row-mibig_compounds-0
  - name: producer_evidence
    definition: Producer evidence grade and its demonstrated or asserted scope.
    value: BGC0002254 v3 assigns Aspergillus sp. FM242 (NCBITaxon:2741095) at SOURCE_ASSERTION.
      This source claim does not inherit the correlated MF297-2 producer grade attached
      to notoamide A through a different MIBiG entry.
    evidence_ids:
    - bgc-2834-provenance
    - bgc-2834-query-mibig_compounds
    - bgc-2834-taxonomy
    - bgc-2834-curation
    - bgc-2834-row-mibig_compounds-0
  - name: locus_evidence
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    value: MT457561.1:1–46989 remains CLUSTER_UNSTATED, with questionable entry quality
      and unknown completeness. PMID:32433885 is ENTRY-scoped. Shared BGC0002254 context
      does not transfer notoamide A's other loci, native protein annotations, NotG
      inference or experimental grades.
    evidence_ids:
    - bgc-2834-provenance
    - bgc-2834-query-mibig_compounds
    - bgc-2834-taxonomy
    - bgc-2834-curation
    - bgc-2834-row-mibig_compounds-0
- assessment_id: bgc-2834-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: 'BGC0002254: PMID:32433885 at ENTRY grain. These are attributed database
    citations, not newly examined primary bodies. DOI case variants and repeated placements
    do not create independent evidence. All 2 histories were read: 2 are seeder-attributed
    SEEDED_FROM_SOURCES events.'
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  evidence_ids:
  - bgc-2834-history
  - bgc-2834-source-reading
  - bgc-2834-query-mibig_compounds
  - bgc-2834-row-mibig_compounds-0
  - bgc-2834-row-lotus_occurrences-0
  - bgc-2834-row-lotus_occurrences-1
  - bgc-2834-row-lotus_occurrences-2
  dimensions:
  - name: citation_scope
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    value: 'BGC0002254: PMID:32433885 at ENTRY grain. These are attributed database
      citations, not newly examined primary bodies. DOI case variants and repeated
      placements do not create independent evidence. All 2 histories were read: 2
      are seeder-attributed SEEDED_FROM_SOURCES events.'
    evidence_ids:
    - bgc-2834-history
    - bgc-2834-source-reading
    - bgc-2834-query-mibig_compounds
    - bgc-2834-row-mibig_compounds-0
    - bgc-2834-row-lotus_occurrences-0
    - bgc-2834-row-lotus_occurrences-1
    - bgc-2834-row-lotus_occurrences-2
- assessment_id: bgc-2834-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: Three LOTUS Aspergillus 5052 occurrences retain DOI 10.1002/CHIN.200728180,
    10.1021/ACS.ORGLETT.0C01411 and 10.1021/NP800471Y. They are attributed occurrence
    references, not independent experimental confirmations or activity evidence. The
    saved PubChem BioAssay frame has no row or blank sentinel for this owner. No actual
    AID or molecular target is captured. ChEBI structure/origin, CyanoMetDB, BindingDB
    and AntibioticMech frames are bounded local negatives, not global absence, inactivity,
    potency or target-mechanism proof.
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  evidence_ids:
  - bgc-2834-roots
  - bgc-2834-query-lotus_occurrences
  - bgc-2834-query-chebi_origins
  - bgc-2834-query-cyanometdb_occurrences
  - bgc-2834-query-pubchem_bioassay
  - bgc-2834-query-bindingdb_targets
  - bgc-2834-query-antibioticmech_inchikeys
  - bgc-2834-assay-curation
  - bgc-2834-row-lotus_occurrences-0
  - bgc-2834-row-lotus_occurrences-1
  - bgc-2834-row-lotus_occurrences-2
  dimensions:
  - name: occurrence_scope
    definition: Exact retained occurrence tuples and limits on production/independence.
    value: Three LOTUS Aspergillus 5052 occurrences retain DOI 10.1002/CHIN.200728180,
      10.1021/ACS.ORGLETT.0C01411 and 10.1021/NP800471Y. They are attributed occurrence
      references, not independent experimental confirmations or activity evidence.
    evidence_ids:
    - bgc-2834-roots
    - bgc-2834-query-lotus_occurrences
    - bgc-2834-query-chebi_origins
    - bgc-2834-query-cyanometdb_occurrences
    - bgc-2834-query-pubchem_bioassay
    - bgc-2834-query-bindingdb_targets
    - bgc-2834-query-antibioticmech_inchikeys
    - bgc-2834-assay-curation
    - bgc-2834-row-lotus_occurrences-0
    - bgc-2834-row-lotus_occurrences-1
    - bgc-2834-row-lotus_occurrences-2
  - name: assay_target_scope
    definition: Retained activity/assay/target positives and bounded negative queries.
    value: The saved PubChem BioAssay frame has no row or blank sentinel for this
      owner. No actual AID or molecular target is captured. ChEBI structure/origin,
      CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives,
      not global absence, inactivity, potency or target-mechanism proof.
    evidence_ids:
    - bgc-2834-roots
    - bgc-2834-query-lotus_occurrences
    - bgc-2834-query-chebi_origins
    - bgc-2834-query-cyanometdb_occurrences
    - bgc-2834-query-pubchem_bioassay
    - bgc-2834-query-bindingdb_targets
    - bgc-2834-query-antibioticmech_inchikeys
    - bgc-2834-assay-curation
    - bgc-2834-row-lotus_occurrences-0
    - bgc-2834-row-lotus_occurrences-1
    - bgc-2834-row-lotus_occurrences-2
- assessment_id: bgc-2834-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: NPClassifier retains Alkaloids plus Amino acids and Peptides, Peptide alkaloids
    and Indole diketopiperazine alkaloids (L-Trp, L-Pro), while BGC0002254 supplies
    a PKS source class. These are distinct annotation systems, not evidence of a resolved
    biosynthetic disagreement. The aromatic indole and amide-containing topology supports
    bounded structural classification; two model pathways retain UNCLASSIFIED.
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  evidence_ids:
  - bgc-2834-classification
  - bgc-2834-chemistry
  - bgc-2834-query-npclassifier
  - bgc-2834-query-mibig_compounds
  - bgc-2834-filing-policy
  - bgc-2834-row-npclassifier-0
  - bgc-2834-row-mibig_compounds-0
  dimensions:
  - name: classification_applicability
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    value: NPClassifier retains Alkaloids plus Amino acids and Peptides, Peptide alkaloids
      and Indole diketopiperazine alkaloids (L-Trp, L-Pro), while BGC0002254 supplies
      a PKS source class. These are distinct annotation systems, not evidence of a
      resolved biosynthetic disagreement. The aromatic indole and amide-containing
      topology supports bounded structural classification; two model pathways retain
      UNCLASSIFIED.
    evidence_ids:
    - bgc-2834-classification
    - bgc-2834-chemistry
    - bgc-2834-query-npclassifier
    - bgc-2834-query-mibig_compounds
    - bgc-2834-filing-policy
    - bgc-2834-row-npclassifier-0
    - bgc-2834-row-mibig_compounds-0
- assessment_id: bgc-2834-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: unknown
  summary: The complete current owner is carried from BGC Science’s attributed complete
    owner reading and exact current raw/capture equality. All 2 histories, nine saved
    source frames (5 positive placements/50 fields and 6 negatives), and both complete
    saved molecular forms were personally read. All 49 actual input hashes and maintained
    ownership paths join the accepted plan. Input pinning is not a claim to have substantively
    read every entire corpus. Five original local gates passed. The complete owner
    root set has no positive graph, pathway, component or molecular-target root, so
    no maintained reader applies. Full QC/OAK, fresh source-authority checks and independent
    primary confirmation remain unavailable; completion is partial.
  target_ids:
  - naturalproductmech:mibig-b68e89ca68
  evidence_ids:
  - bgc-2834-owner
  - bgc-2834-whole-owner-attribution
  - bgc-2834-history
  - bgc-2834-intake
  - bgc-2834-intake-acceptance
  - bgc-2834-plan
  - bgc-2834-plan-acceptance
  - bgc-2834-gates
  - bgc-2834-source-reading
  - bgc-2834-source-notes
  - bgc-2834-molecular-reading
  - bgc-2834-roots
  dimensions:
  - name: review_completion
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    value: The complete current owner is carried from BGC Science’s attributed complete
      owner reading and exact current raw/capture equality. All 2 histories, nine
      saved source frames (5 positive placements/50 fields and 6 negatives), and both
      complete saved molecular forms were personally read. All 49 actual input hashes
      and maintained ownership paths join the accepted plan. Input pinning is not
      a claim to have substantively read every entire corpus. Five original local
      gates passed. The complete owner root set has no positive graph, pathway, component
      or molecular-target root, so no maintained reader applies. Full QC/OAK, fresh
      source-authority checks and independent primary confirmation remain unavailable;
      completion is partial.
    evidence_ids:
    - bgc-2834-owner
    - bgc-2834-whole-owner-attribution
    - bgc-2834-history
    - bgc-2834-intake
    - bgc-2834-intake-acceptance
    - bgc-2834-plan
    - bgc-2834-plan-acceptance
    - bgc-2834-gates
    - bgc-2834-source-reading
    - bgc-2834-source-notes
    - bgc-2834-molecular-reading
    - bgc-2834-roots
findings: []
actions: []
limitations:
- Fresh source-authority, primary publication, sequence and strain verification remain
  unavailable. Full QC/OAK were not run; retained experimental grades stay source-attributed.
- Both stored notoamide F forms normalize to the same Standard InChI, declared full
  key and neutral C27H31N3O4 formula. One secondary amide appears as C(OH)=N in the
  InChI-derived form, leaving one strict tertiary amide. Both canonical comparisons
  are false and the saved match is empty; full graph identity is not established.
  Formula and key agreement do not collapse its identity into notoamide A. The original
  diagnostic stderr is empty; no warning or unreported stereochemical assignment is
  inferred.
- Both saved notoamide F forms contain four specified tetrahedral centres and no unspecified
  potential-stereo entry in the retained tables. The true source stereo_complete flag
  retains its atom-centred extraction scope; it is not proof of natural absolute configuration
  or a basis for transferring notoamide A's graph assertions.
- Saved topology supports the encoded molecule without independently establishing
  every natural residue, biosynthetic reaction or pharmacological mechanism.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- No record, source table, native scientific status or curation history is modified.
  Corrections, if later justified, belong in maintained source/curation/extractor
  ownership; curated mechanism changes require validated writing and attributed history.
- This author interpreted retained original outputs only, with zero molecular parses,
  source-query replays, target runs or outbound requests.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-284
```
