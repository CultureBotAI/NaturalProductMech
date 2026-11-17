# Local evidence review: muscoride B

- Review: 20261107T004933Z-muscoride-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T23:53:39.598583Z
- Finished UTC: 2026-11-07T00:49:33.475422Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Muscoride B has three oxazole-like rings, a saturated nitrogen-containing five-ring and separate N-linked and ester-O-linked prenyl groups. Its saved forms agree computationally, while the maintained reader preserves a partial, proposed UHCC-0398 MusE/MusF1/MusF2 route. Primary and sequence claims remain historical and attributed; completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2794; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-f4bf230570 | data/natural_products/unclassified/muscoride-b.yaml | generated | muscoride B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-f4bf230570 | Both exact stored forms parsed in the original twenty-attempt diagnostic and agree in formula, charge, normalized Standard InChI and complete key. |
| Complete offline maintained reader for muscoride-b | passed | True | naturalproductmech:mibig-f4bf230570 | One original maintained reader preserved the complete Muscoride B owner, one six-node/six-edge graph, two proposed pathway steps and four histories; zero components. |
| strict_ten | passed | True | naturalproductmech:mibig-f4bf230570 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-f4bf230570 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-f4bf230570 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-f4bf230570 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-f4bf230570 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-f4bf230570 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-f4bf230570 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-f4bf230570 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: naturalproductmech:mibig-f4bf230570.

muscoride B retains exact identifier naturalproductmech:mibig-f4bf230570, complete key RYLVRVUEEVJKJO-OPXMRZJTSA-N, and source rows BGC0002485 v2 compound index 2; BGC0002551 v2 compound index 2. Cross-references (npatlas:NPA025875) remain attributed identifiers, not fresh authority confirmation. Both saved forms normalize to C31H41N5O6 and the declared full key. The OPEN shared-structure discussion remains unresolved; multiple source concepts and computational agreement do not independently adjudicate the source identity.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-f4bf230570.

The saved Muscoride B forms each contain 42 atoms and 45 bonds. Four five-membered rings comprise one saturated nitrogen-containing ring and three aromatic N/O oxazole-like rings. The SMILES graph contains tertiary amide C11(=O12)-N13 and ester C27(=O28)-O29-C30. Separate N-linked and ester-O-linked isoprenyl substituents are explicit at N5-C6-C7=C8 and O29-C30-C31=C32. This is compatible with the recorded bis-prenylated product, but the molecule alone does not demonstrate MusF1 or MusF2 catalysis. All three potential tetrahedral centres are specified S in the saved SMILES graph (C2, C4 and C17), with corresponding S centres in the InChI-derived graph. Each isoprenyl alkene has two methyl substituents on one end, so neither is an E/Z stereogenic double bond; absence of an E/Z potential is not missing geometry. The retained true stereo flag and this saved agreement do not independently certify natural absolute stereochemistry. Both canonical SMILES comparisons are true and the saved chirality-aware match contains all 42 atoms. The tertiary amide and ester are retained without secondary-amide/imidic relocation. Formula, aggregate charge, atom/bond counts, normalized Standard InChI and full key also agree. The diagnostic explicitly leaves full_graph_identity_established false: the one-way match and canonical agreement are limited computational consistency evidence, not independent natural identity or primary experimental certification.

### Producer assertion versus locus evidence

provenance: supported. Targets: naturalproductmech:mibig-f4bf230570.

Desmonostoc sp. PCC 7906 (NCBITaxon:1181) and Nostoc sp. UHCC-0398 (2665154) remain two separate SOURCE_ASSERTION producer claims. The Nostoc occurrence label (1177) supplies neither strain equivalence nor a causal producer experiment. The partial MusE/MusF1/MusF2 mechanism is explicitly scoped to the UHCC-0398 route and is not transferred to PCC 7906. Both MIBiG entries are v2, active, questionable in quality and unknown in completeness. BGC0002485 uses MK806443.1:1-14448 with heterologous expression; BGC0002551 uses MK806444.1:1-13360 with enzymatic assays. Both retain CLUSTER_DEMONSTRATED locus support and ENTRY PMID:31674754. Shared citation and full key do not collapse the two locus/producer routes or independently resolve their OPEN identity discussion.

### Citation grain and attributed history

evidence: supported. Targets: naturalproductmech:mibig-f4bf230570.

BGC0002485: PMID:31674754 at ENTRY grain; BGC0002551: PMID:31674754 at ENTRY grain. These are attributed database citations, not newly examined primary bodies. DOI case variants and repeated placements do not create independent evidence. All 4 histories were read: 3 are seeder-attributed SEEDED_FROM_SOURCES events. The remaining 2026-09-28 codex event adds the explicitly partial terminal-prenylation graph/pathway; its historical primary and sequence claims are retained without fresh verification.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: naturalproductmech:mibig-f4bf230570.

One exact-key LOTUS tuple names Nostoc (1177) with DOI:10.1021/ACSCHEMBIO.9B00620. The case variant of the mechanism DOI is the same citation, not independent primary corroboration. The occurrence is not a third experimentally established producer route. The saved PubChem BioAssay frame has no row or blank sentinel for this owner. No actual AID or molecular target is captured. ChEBI structure/origin, CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not global absence, inactivity, potency or target-mechanism proof.

### Computed filing and asserted class applicability

consistency: supported. Targets: naturalproductmech:mibig-f4bf230570.

The model returns Alkaloids and Amino acids and Peptides, with empty superclass/class arrays and is_glycoside:false; UNCLASSIFIED follows the maintained multi-label rule. Source RIBOSOMAL/OTHER/TERPENE labels remain attributed. Structural prenyl groups and the partial curated pathway add qualified context without converting model labels into a fully demonstrated assembly pathway.

### Local completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-f4bf230570.

Whole current owner and all 4 histories, nine saved source frames (4 positive placements/63 fields and 6 negatives), and both complete saved molecular forms were personally read. All 47 actual input hashes and maintained ownership paths join the accepted plan. Input pinning is not a claim to have substantively read every entire corpus. Five original local gates passed. One inline graph and two proposed pathway steps require the separately accepted maintained reader; no component or molecular-target root is present. Full QC/OAK, fresh source-authority checks and independent primary confirmation remain unavailable; completion is partial.

### Partial UHCC-0398 terminal prenylation and historical evidence boundaries

graph: supported. Targets: naturalproductmech:mibig-f4bf230570.

The accepted single Muscoride B reader preserves the entire owner, one six-node/six-edge inline BIOSYNTHESIS graph, two proposed numbered steps and all four histories, with no components or molecular targets. MusE (A0A5Q0TX65) supplies precursor context for C-terminal and N-terminal prenylation; MusF1 (A0A5Q0TWZ6) and MusF2 (A0A5Q0TX00) are linked to those respective processes. The two process nodes and exact intermediates remain ungrounded; the product edges say contributes to the downstream bis-prenylated Muscoride B, not a directly specified one-step substrate-product transformation. Steps 1 and 2 retain proposed:true and do not establish a complete assembly route, the kinetic order of independent terminal modifications, proteolysis or oxazole formation. The annotations attribute enzymatic findings to DOI:10.1021/acschembio.9b00620 and historical 2026-09-28 GenBank/UniProt/GenPept checks of MK806444.1, QGA72599.1 (67 aa), QGA72595.1 and QGA72594.1 (300 aa each). Their 28 graph and eight pathway reference placements are repeated evidence attributions, not 36 independent experiments or fresh sequence verification. The saved product topology is compatible with two prenyl groups, but does not prove enzyme activity, protein-grounding accuracy or producer identity. The qualified partial representation is internally coherent with the UHCC-0398 scope; the PCC 7906 route, exact natural identity and underlying primary evidence remain separately unresolved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2794-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/muscoride-b.yaml; Complete plaintext, every root and all curation_history entries | supports | Complete current owner personally read and joined exactly to the accepted raw capture. |
| bgc-2794-identity | /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json; /records/3/owner_document/identifier; /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status; /records/3/owner_document/discussions | supports | muscoride B retains exact identifier naturalproductmech:mibig-f4bf230570, complete key RYLVRVUEEVJKJO-OPXMRZJTSA-N, and source rows BGC0002485 v2 compound index 2; BGC0002551 v2 compound index 2. Cross-references (npatlas:NPA025875) remain attributed identifiers, not fresh authority confirmation. Both saved forms normalize to C31H41N5O6 and the declared full key. The OPEN shared-structure discussion remains unresolved; multiple source concepts and computational agreement do not independently adjudicate the source identity. |
| bgc-2794-history | /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json; /records/3/owner_document/curation_history | supports | BGC0002485: PMID:31674754 at ENTRY grain; BGC0002551: PMID:31674754 at ENTRY grain. These are attributed database citations, not newly examined primary bodies. DOI case variants and repeated placements do not create independent evidence. All 4 histories were read: 3 are seeder-attributed SEEDED_FROM_SOURCES events. The remaining 2026-09-28 codex event adds the explicitly partial terminal-prenylation graph/pathway; its historical primary and sequence claims are retained without fresh verification. |
| bgc-2794-provenance | /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters | supports | Desmonostoc sp. PCC 7906 (NCBITaxon:1181) and Nostoc sp. UHCC-0398 (2665154) remain two separate SOURCE_ASSERTION producer claims. The Nostoc occurrence label (1177) supplies neither strain equivalence nor a causal producer experiment. The partial MusE/MusF1/MusF2 mechanism is explicitly scoped to the UHCC-0398 route and is not transferred to PCC 7906. Both MIBiG entries are v2, active, questionable in quality and unknown in completeness. BGC0002485 uses MK806443.1:1-14448 with heterologous expression; BGC0002551 uses MK806444.1:1-13360 with enzymatic assays. Both retain CLUSTER_DEMONSTRATED locus support and ENTRY PMID:31674754. Shared citation and full key do not collapse the two locus/producer routes or independently resolve their OPEN identity discussion. |
| bgc-2794-classification | /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json; /records/3/owner_document/np_classification; /records/3/owner_document/np_pathway; /records/3/owner_document/bgc_class | supports | The model returns Alkaloids and Amino acids and Peptides, with empty superclass/class arrays and is_glycoside:false; UNCLASSIFIED follows the maintained multi-label rule. Source RIBOSOMAL/OTHER/TERPENE labels remain attributed. Structural prenyl groups and the partial curated pathway add qualified context without converting model labels into a fully demonstrated assembly pathway. |
| bgc-2794-roots | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/10/complete_root_keys; /contexts/10/declared_mechanism_roots_literal; /contexts/10/literal_bioactivities_root | context_only | One inline graph and two proposed pathway steps require the separately accepted maintained reader; no component or molecular-target root is present. |
| bgc-2794-chemistry | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons; /records/3/atom_correspondence | supports | The saved Muscoride B forms each contain 42 atoms and 45 bonds. Four five-membered rings comprise one saturated nitrogen-containing ring and three aromatic N/O oxazole-like rings. The SMILES graph contains tertiary amide C11(=O12)-N13 and ester C27(=O28)-O29-C30. Separate N-linked and ester-O-linked isoprenyl substituents are explicit at N5-C6-C7=C8 and O29-C30-C31=C32. This is compatible with the recorded bis-prenylated product, but the molecule alone does not demonstrate MusF1 or MusF2 catalysis. All three potential tetrahedral centres are specified S in the saved SMILES graph (C2, C4 and C17), with corresponding S centres in the InChI-derived graph. Each isoprenyl alkene has two methyl substituents on one end, so neither is an E/Z stereogenic double bond; absence of an E/Z potential is not missing geometry. The retained true stereo flag and this saved agreement do not independently certify natural absolute stereochemistry. Both canonical SMILES comparisons are true and the saved chirality-aware match contains all 42 atoms. The tertiary amide and ester are retained without secondary-amide/imidic relocation. Formula, aggregate charge, atom/bond counts, normalized Standard InChI and full key also agree. The diagnostic explicitly leaves full_graph_identity_established false: the one-way match and canonical agreement are limited computational consistency evidence, not independent natural identity or primary experimental certification. |
| bgc-2794-molecular-reading | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-current280-first-five-molecular-reading-001.json; /records/3; /scope_orders; /method_limits | supports | Complete saved tables personally read and interpreted without a new parse. |
| bgc-2794-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/root-current280-diagnostic-acceptance-001.json; /status; /accepted; /diagnostic; /molecular_parse_attempts; /limits | supports | ROOT accepted the original twenty stored-form attempts; exact representation and identity limits remain. |
| bgc-2794-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-execution-001.json; /command; /exit_code | supports | Original ROOT diagnostic command and exit zero; no replay. |
| bgc-2794-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-original-001.stderr; Complete original stderr including blank separators | context_only | Four undefined-stereo and two proton-added/removed warnings remain globally unassigned; no message is attributed to this owner. |
| bgc-2794-intake | /private/tmp/npm-review-work/shared-next-batch280/intakes-001/2794-inspect-001.json; /targets; /source/inputs | supports | One exact target, 47 current inputs and explicit maintained ownership paths. |
| bgc-2794-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch280/root-current280-intake-acceptance-001.json; /accepted; /intake_summary; /records; /source_placements; /unique_source_paths | supports | All ten original inspections exited zero with empty stderr and 463 placements/72 paths. |
| bgc-2794-plan | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-target-input-plan-001.json; /records/3 | supports | Exact current input map, 1 direct companions and the literal reader applicability. |
| bgc-2794-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch280/root-current280-input-plan-acceptance-001.json; /accepted; /input_plan; /source_placements; /unique_source_paths | supports | ROOT accepted the current source input plan. |
| bgc-2794-gates | /private/tmp/npm-review-work/shared-next-batch280/root-current280-five-gates-acceptance-001.json; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows; /selected_queue_counts/2794 | context_only | Five local gates passed; queue rows are review leads, not findings. Full QC/OAK remain unavailable. |
| bgc-2794-source-reading | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-current280-assigned-source-reading-001.json; /contexts/7; /counts; /reading_attribution | supports | All 4 complete positive dictionaries/63 fields and 6 bounded negative frames were personally read in the attributed source pass. |
| bgc-2794-source-notes | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-scope-notes-001.json; /totals; /reading_reconciliation; /reading_boundaries | context_only | The original 83 source placements/1,081 fields retain BGC 38 and Support 45 primary-row attribution; Native and ROOT have zero primary-row credit. |
| bgc-2794-taxonomy | /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-cached-taxonomy-reading-001.json; /scope; /context_interpretations/10; /interpretation | context_only | Desmonostoc sp. PCC 7906 (NCBITaxon:1181) and Nostoc sp. UHCC-0398 (2665154) remain two separate SOURCE_ASSERTION producer claims. The Nostoc occurrence label (1177) supplies neither strain equivalence nor a causal producer experiment. The partial MusE/MusF1/MusF2 mechanism is explicitly scoped to the UHCC-0398 route and is not transferred to PCC 7906. Cached names do not independently supply rank, lineage or strain-level evidence. |
| bgc-2794-curation | /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-implemented-curation-scan-002.json; /scope; /counts; /applied_rows; /interpretation | context_only | Nine substantive tables/3,422 rows were scanned by Native; 119 lexical candidates yield zero exact applicable decisions. Two reserved census-only tables are excluded. |
| bgc-2794-assay-curation | /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-implemented-curation-scan-002.json; /assay_scope | context_only | The saved PubChem BioAssay frame has no row or blank sentinel for this owner. No actual AID or molecular target is captured. ChEBI structure/origin, CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not global absence, inactivity, potency or target-mechanism proof. |
| bgc-2794-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters(includeUnassigned=True) | context_only | The source stereo_complete flag tests unassigned atom-centred chirality, not all double-bond geometry or natural identity. |
| bgc-2794-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306: choose_pathway | context_only | Exactly one supported mapped pathway selects filing; zero, unsupported single or multiple labels retain UNCLASSIFIED. |
| bgc-2794-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 2 positive placements, with all fields and bounded query meanings read. |
| bgc-2794-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 3109-3109; raw record sha256 b87ce801a6c0d741031e8be1bb785bb2a52640d8dfd990af04d72abf58147f6f | supports | All 25 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2794-row-mibig_compounds-1 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 3227-3227; raw record sha256 0a92f9cde3a65eaa9adc69ebc5a930f0ee8c42bfd81438e4d47405fd0264a856 | supports | All 25 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2794-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2794-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 1 positive placements, with all fields and bounded query meanings read. |
| bgc-2794-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 8286-8286; raw record sha256 3412c3e25f0b9fc8e3986c8184a2aa297d61bc15ffc10cf64ff123df3a1c6d2b | supports | All 6 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2794-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2794-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 positive placements, with all fields and bounded query meanings read. |
| bgc-2794-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2196-2196; raw record sha256 efdda7e299f5f74ebccf7f803fbc8736f6c2d0d668d2a373cb67aad7e2164195 | supports | All 7 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2794-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/pubchem_bioassay | context_only | Complete saved pubchem_bioassay frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2794-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2794-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2794-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2794-congener-0 | /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/muscoride-a.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2794-reader-DATA | /private/tmp/npm-review-work/shared-next-batch280/native-current280-muscoride-b-maintained-reader-DATA-001.json; /resolved_view; /raw_owner; /expected_view; /counts; /reader_call_count; /denials; /unexpected_denials; /external_requests | supports | One original maintained call preserves the entire captured owner and all declared graph/pathway/history content. |
| bgc-2794-reader-execution | /private/tmp/npm-review-work/shared-next-batch280/native-current280-muscoride-b-reader-execution-001.json; /command; /exit_code | supports | Original ROOT maintained-reader execution and exit zero. |
| bgc-2794-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch280/root-current280-muscoride-b-reader-acceptance-001.json; /accepted; /review_check_contract; /verification; /limits | supports | ROOT accepted complete-owner equality and the exact original check contract; scientific interpretation remains separate. |
| bgc-2794-reader-reading | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-current280-muscoride-b-complete-reader-view-reading-001.json; /whole_returned_view; /interpretation; /counts | supports | Complete actual returned view and every evidence/history meaning personally read, with no fresh sequence or primary verification. |
| bgc-2794-graph | /private/tmp/npm-review-work/shared-next-batch280/native-current280-muscoride-b-maintained-reader-DATA-001.json; /resolved_view/causal_graphs; /resolved_view/biosynthetic_pathway; /resolved_view/curation_history | supports | The accepted single Muscoride B reader preserves the entire owner, one six-node/six-edge inline BIOSYNTHESIS graph, two proposed numbered steps and all four histories, with no components or molecular targets. MusE (A0A5Q0TX65) supplies precursor context for C-terminal and N-terminal prenylation; MusF1 (A0A5Q0TWZ6) and MusF2 (A0A5Q0TX00) are linked to those respective processes. The two process nodes and exact intermediates remain ungrounded; the product edges say contributes to the downstream bis-prenylated Muscoride B, not a directly specified one-step substrate-product transformation. Steps 1 and 2 retain proposed:true and do not establish a complete assembly route, the kinetic order of independent terminal modifications, proteolysis or oxazole formation. The annotations attribute enzymatic findings to DOI:10.1021/acschembio.9b00620 and historical 2026-09-28 GenBank/UniProt/GenPept checks of MK806444.1, QGA72599.1 (67 aa), QGA72595.1 and QGA72594.1 (300 aa each). Their 28 graph and eight pathway reference placements are repeated evidence attributions, not 36 independent experiments or fresh sequence verification. The saved product topology is compatible with two prenyl groups, but does not prove enzyme activity, protein-grounding accuracy or producer identity. The qualified partial representation is internally coherent with the UHCC-0398 scope; the PCC 7906 route, exact natural identity and underlying primary evidence remain separately unresolved. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-280/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-280/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-280/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-280/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-280/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Fresh source-authority, primary publication, sequence and strain verification remain unavailable. Full QC/OAK were not run; retained experimental grades stay source-attributed.
- Both canonical SMILES comparisons are true and the saved chirality-aware match contains all 42 atoms. The tertiary amide and ester are retained without secondary-amide/imidic relocation. Formula, aggregate charge, atom/bond counts, normalized Standard InChI and full key also agree. The diagnostic explicitly leaves full_graph_identity_established false: the one-way match and canonical agreement are limited computational consistency evidence, not independent natural identity or primary experimental certification. Four undefined-stereo and two proton-added/removed warnings remain globally unassigned; no message is attributed to this owner.
- All three potential tetrahedral centres are specified S in the saved SMILES graph (C2, C4 and C17), with corresponding S centres in the InChI-derived graph. Each isoprenyl alkene has two methyl substituents on one end, so neither is an E/Z stereogenic double bond; absence of an E/Z potential is not missing geometry. The retained true stereo flag and this saved agreement do not independently certify natural absolute stereochemistry.
- Saved topology supports the encoded molecule without independently establishing every natural residue, biosynthetic reaction or pharmacological mechanism.
- The accepted reader proves complete preservation and maintained structural consistency, not scientific validity of every grounding or primary claim. The MusF route is partial, both steps remain proposed, exact intermediates are ungrounded and the OPEN two-source identity discussion remains unresolved.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- No record, source table, native scientific status or curation history is modified. Corrections, if later justified, belong in maintained source/curation/extractor ownership; curated mechanism changes require validated writing and attributed history.
- This author interpreted retained original outputs only, with zero molecular parses, source-query replays, target runs or outbound requests.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T004933Z-muscoride-b
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: muscoride B'
started_at: '2026-11-06T23:53:39.598583Z'
finished_at: '2026-11-07T00:49:33.475422Z'
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
summary: Muscoride B has three oxazole-like rings, a saturated nitrogen-containing
  five-ring and separate N-linked and ester-O-linked prenyl groups. Its saved forms
  agree computationally, while the maintained reader preserves a partial, proposed
  UHCC-0398 MusE/MusF1/MusF2 route. Primary and sequence claims remain historical
  and attributed; completion is partial.
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
  - path: data/natural_products/amino_acids_and_peptides/muscoride-a.yaml
    sha256: 419669ca87f7b1933f451c660e564b06b5f3350607b94a9cc1b95d244ce46c77
    role: context
  - path: data/natural_products/unclassified/muscoride-b.yaml
    sha256: 66164d381187a9abe0fac6a20d0a0a3d9fff0942086308fcbc62657a20e7e51b
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
  selection: Campaign path order 2794; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-f4bf230570
targets:
- target_id: naturalproductmech:mibig-f4bf230570
  path: data/natural_products/unclassified/muscoride-b.yaml
  label: muscoride B
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
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/muscoride-b.yaml
    role: Curator-owned declared graphs, graph references, pathway steps and history;
      imported molecular-target assertions and other seeded fields retain inventory
      ownership. Curated graph/pathway changes require the validated writer and a
      curation event.
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners. This mechanism-bearing owner requires separately
    authorized complete maintained resolution before scientific assessment and draft
    assembly. Raw owner capture is not a maintained resolved view.
checks:
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnose280-001.py
    2ba99053ef31c5bdddb405acb0108a92720b8a4af71d98f5b032ccd0adfb11b7 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
    df0120607515dc9243bfa92b39622a3bb842fd0bd3d1eb18d29677b785fd591b
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both exact stored forms parsed in the original twenty-attempt diagnostic
    and agree in formula, charge, normalized Standard InChI and complete key.
  scope_note: 'Both canonical SMILES comparisons are true and the saved chirality-aware
    match contains all 42 atoms. The tertiary amide and ester are retained without
    secondary-amide/imidic relocation. Formula, aggregate charge, atom/bond counts,
    normalized Standard InChI and full key also agree. The diagnostic explicitly leaves
    full_graph_identity_established false: the one-way match and canonical agreement
    are limited computational consistency evidence, not independent natural identity
    or primary experimental certification. Four undefined-stereo and two proton-added/removed
    warnings remain globally unassigned; no message is attributed to this owner.'
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  evidence_ids:
  - bgc-2794-chemistry
  - bgc-2794-diagnostic-acceptance
  - bgc-2794-diagnostic-execution
  - bgc-2794-diagnostic-stderr
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for muscoride-b
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch280/read-selected-mechanism-guarded-001.py
    2794 df0120607515dc9243bfa92b39622a3bb842fd0bd3d1eb18d29677b785fd591b bebd2de74e497589776d27306ddba461995df5857a3b46d20c13c734ab428e20
    a44b8239212154b11705bb659af9577a9ea6c7a94ca560b4a804f10dc48b84aa 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
    2ba99053ef31c5bdddb405acb0108a92720b8a4af71d98f5b032ccd0adfb11b7
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: One original maintained reader preserved the complete Muscoride B owner,
    one six-node/six-edge graph, two proposed pathway steps and four histories; zero
    components.
  scope_note: Complete preservation and maintained structural consistency only. Historical
    source/protein claims, proposed intermediates and incomplete assembly remain qualified.
    One socket capability probe was denied before action; no request was sent.
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  evidence_ids:
  - bgc-2794-reader-DATA
  - bgc-2794-reader-execution
  - bgc-2794-reader-acceptance
  - bgc-2794-graph
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  command: just validate-strict data/natural_products/unclassified/ml-449.yaml data/natural_products/unclassified/montamide-a.yaml
    data/natural_products/unclassified/montanastatin.yaml data/natural_products/unclassified/muscoride-b.yaml
    data/natural_products/unclassified/mutanocyclin.yaml data/natural_products/unclassified/mycobactin.yaml
    data/natural_products/unclassified/mycosporine-glycine.yaml data/natural_products/unclassified/myxarylin.yaml
    data/natural_products/unclassified/myxochromide-b.yaml data/natural_products/unclassified/myxochromide-c.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-280/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-f4bf230570
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-280/validate-all-001.tsv
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
  - naturalproductmech:mibig-f4bf230570
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
  - naturalproductmech:mibig-f4bf230570
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
  - naturalproductmech:mibig-f4bf230570
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-280/review-queue-001.tsv
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
  - naturalproductmech:mibig-f4bf230570
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2794-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/muscoride-b.yaml
  locator: Complete plaintext, every root and all curation_history entries
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: Complete current owner personally read and joined exactly to the accepted
    raw capture.
  snapshot_sha256: 66164d381187a9abe0fac6a20d0a0a3d9fff0942086308fcbc62657a20e7e51b
- evidence_id: bgc-2794-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json
  locator: /records/3/owner_document/identifier; /records/3/owner_document/chemical_structure;
    /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status;
    /records/3/owner_document/discussions
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: muscoride B retains exact identifier naturalproductmech:mibig-f4bf230570,
    complete key RYLVRVUEEVJKJO-OPXMRZJTSA-N, and source rows BGC0002485 v2 compound
    index 2; BGC0002551 v2 compound index 2. Cross-references (npatlas:NPA025875)
    remain attributed identifiers, not fresh authority confirmation. Both saved forms
    normalize to C31H41N5O6 and the declared full key. The OPEN shared-structure discussion
    remains unresolved; multiple source concepts and computational agreement do not
    independently adjudicate the source identity.
  snapshot_sha256: 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
- evidence_id: bgc-2794-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json
  locator: /records/3/owner_document/curation_history
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: 'BGC0002485: PMID:31674754 at ENTRY grain; BGC0002551: PMID:31674754 at
    ENTRY grain. These are attributed database citations, not newly examined primary
    bodies. DOI case variants and repeated placements do not create independent evidence.
    All 4 histories were read: 3 are seeder-attributed SEEDED_FROM_SOURCES events.
    The remaining 2026-09-28 codex event adds the explicitly partial terminal-prenylation
    graph/pathway; its historical primary and sequence claims are retained without
    fresh verification.'
  snapshot_sha256: 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
- evidence_id: bgc-2794-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: Desmonostoc sp. PCC 7906 (NCBITaxon:1181) and Nostoc sp. UHCC-0398 (2665154)
    remain two separate SOURCE_ASSERTION producer claims. The Nostoc occurrence label
    (1177) supplies neither strain equivalence nor a causal producer experiment. The
    partial MusE/MusF1/MusF2 mechanism is explicitly scoped to the UHCC-0398 route
    and is not transferred to PCC 7906. Both MIBiG entries are v2, active, questionable
    in quality and unknown in completeness. BGC0002485 uses MK806443.1:1-14448 with
    heterologous expression; BGC0002551 uses MK806444.1:1-13360 with enzymatic assays.
    Both retain CLUSTER_DEMONSTRATED locus support and ENTRY PMID:31674754. Shared
    citation and full key do not collapse the two locus/producer routes or independently
    resolve their OPEN identity discussion.
  snapshot_sha256: 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
- evidence_id: bgc-2794-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_classification; /records/3/owner_document/np_pathway;
    /records/3/owner_document/bgc_class
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: The model returns Alkaloids and Amino acids and Peptides, with empty superclass/class
    arrays and is_glycoside:false; UNCLASSIFIED follows the maintained multi-label
    rule. Source RIBOSOMAL/OTHER/TERPENE labels remain attributed. Structural prenyl
    groups and the partial curated pathway add qualified context without converting
    model labels into a fully demonstrated assembly pathway.
  snapshot_sha256: 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
- evidence_id: bgc-2794-roots
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/10/complete_root_keys; /contexts/10/declared_mechanism_roots_literal;
    /contexts/10/literal_bioactivities_root
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: One inline graph and two proposed pathway steps require the separately
    accepted maintained reader; no component or molecular-target root is present.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Complete captured owner root set, not a biological absence claim.
- evidence_id: bgc-2794-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons;
    /records/3/atom_correspondence
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: 'The saved Muscoride B forms each contain 42 atoms and 45 bonds. Four five-membered
    rings comprise one saturated nitrogen-containing ring and three aromatic N/O oxazole-like
    rings. The SMILES graph contains tertiary amide C11(=O12)-N13 and ester C27(=O28)-O29-C30.
    Separate N-linked and ester-O-linked isoprenyl substituents are explicit at N5-C6-C7=C8
    and O29-C30-C31=C32. This is compatible with the recorded bis-prenylated product,
    but the molecule alone does not demonstrate MusF1 or MusF2 catalysis. All three
    potential tetrahedral centres are specified S in the saved SMILES graph (C2, C4
    and C17), with corresponding S centres in the InChI-derived graph. Each isoprenyl
    alkene has two methyl substituents on one end, so neither is an E/Z stereogenic
    double bond; absence of an E/Z potential is not missing geometry. The retained
    true stereo flag and this saved agreement do not independently certify natural
    absolute stereochemistry. Both canonical SMILES comparisons are true and the saved
    chirality-aware match contains all 42 atoms. The tertiary amide and ester are
    retained without secondary-amide/imidic relocation. Formula, aggregate charge,
    atom/bond counts, normalized Standard InChI and full key also agree. The diagnostic
    explicitly leaves full_graph_identity_established false: the one-way match and
    canonical agreement are limited computational consistency evidence, not independent
    natural identity or primary experimental certification.'
  snapshot_sha256: c1725a2a201004679fb5a6b60a3124217de57850698749040b40e46d316502d8
- evidence_id: bgc-2794-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-current280-first-five-molecular-reading-001.json
  locator: /records/3; /scope_orders; /method_limits
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: Complete saved tables personally read and interpreted without a new parse.
  snapshot_sha256: a72e37fd5a290d52d7bcbb3b7c0ff490d7e830b0687aa039c0b8e82dc493a6c7
- evidence_id: bgc-2794-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/root-current280-diagnostic-acceptance-001.json
  locator: /status; /accepted; /diagnostic; /molecular_parse_attempts; /limits
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form attempts; exact representation
    and identity limits remain.
  snapshot_sha256: 409fc03abfaba0325bf25149704a554a7c7d5fc80f2dd056cca027cd008797c5
- evidence_id: bgc-2794-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: Original ROOT diagnostic command and exit zero; no replay.
  snapshot_sha256: fe6b12cc17cb942787983efb14216babe8b2ee52b81adaca8ffaed0d29142fd6
- evidence_id: bgc-2794-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr including blank separators
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: Four undefined-stereo and two proton-added/removed warnings remain globally
    unassigned; no message is attributed to this owner.
  snapshot_sha256: f6a74ef31a1d327a6a483c87de5d2671dedd256b334e08156260de25ee0a95be
- evidence_id: bgc-2794-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/intakes-001/2794-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: One exact target, 47 current inputs and explicit maintained ownership paths.
  snapshot_sha256: bebd2de74e497589776d27306ddba461995df5857a3b46d20c13c734ab428e20
- evidence_id: bgc-2794-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-intake-acceptance-001.json
  locator: /accepted; /intake_summary; /records; /source_placements; /unique_source_paths
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: All ten original inspections exited zero with empty stderr and 463 placements/72
    paths.
  snapshot_sha256: e11e8f952eeb308c816112881974c56ec907ec0a5ee8935ee308347ab2e2d871
- evidence_id: bgc-2794-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-target-input-plan-001.json
  locator: /records/3
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: Exact current input map, 1 direct companions and the literal reader applicability.
  snapshot_sha256: d6777f8dea91c7542347ffaf26f8bc8cc03d93b08032d32861abac52335c3fa3
- evidence_id: bgc-2794-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-input-plan-acceptance-001.json
  locator: /accepted; /input_plan; /source_placements; /unique_source_paths
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: ROOT accepted the current source input plan.
  snapshot_sha256: 0e8c34013ec3794cfaa30bcb060b8a8717b99a038f5ba349a893ae7fbc47c2ce
- evidence_id: bgc-2794-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-five-gates-acceptance-001.json
  locator: /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /selected_queue_rows; /selected_queue_counts/2794
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: Five local gates passed; queue rows are review leads, not findings. Full
    QC/OAK remain unavailable.
  snapshot_sha256: 7e6f44be6a38a56ec60db94569abcb6d4b76d33133e329930db626e8bbb3f0b8
- evidence_id: bgc-2794-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-current280-assigned-source-reading-001.json
  locator: /contexts/7; /counts; /reading_attribution
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: All 4 complete positive dictionaries/63 fields and 6 bounded negative frames
    were personally read in the attributed source pass.
  snapshot_sha256: cec71b1551d3ff3e07fe61b1b5a324d56537dc2484cc52174b3258a61b84420c
- evidence_id: bgc-2794-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: The original 83 source placements/1,081 fields retain BGC 38 and Support
    45 primary-row attribution; Native and ROOT have zero primary-row credit.
  snapshot_sha256: e5b80095d288105ec28103716a87da06b65c083b79bf0fbbac86dc83773a08d4
- evidence_id: bgc-2794-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-cached-taxonomy-reading-001.json
  locator: /scope; /context_interpretations/10; /interpretation
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: Desmonostoc sp. PCC 7906 (NCBITaxon:1181) and Nostoc sp. UHCC-0398 (2665154)
    remain two separate SOURCE_ASSERTION producer claims. The Nostoc occurrence label
    (1177) supplies neither strain equivalence nor a causal producer experiment. The
    partial MusE/MusF1/MusF2 mechanism is explicitly scoped to the UHCC-0398 route
    and is not transferred to PCC 7906. Cached names do not independently supply rank,
    lineage or strain-level evidence.
  snapshot_sha256: 7b3133d38f9f774b7be03c70880701cccf97fa8b6968bb2278462c34f3c47fe0
  search_scope: Exact current taxon route and retained cached names/synonyms; no fresh
    external taxonomy or inferred hierarchy.
- evidence_id: bgc-2794-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-implemented-curation-scan-002.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: Nine substantive tables/3,422 rows were scanned by Native; 119 lexical
    candidates yield zero exact applicable decisions. Two reserved census-only tables
    are excluded.
  snapshot_sha256: 6ad28a5dd301fac51ee52e70ca0789cd040a1906660932acedd202703d786e11
  search_scope: Actual captured table inputs and exact identity/source/occurrence/assay
    predicates; no decision from lexical similarity.
- evidence_id: bgc-2794-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-implemented-curation-scan-002.json
  locator: /assay_scope
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: The saved PubChem BioAssay frame has no row or blank sentinel for this
    owner. No actual AID or molecular target is captured. ChEBI structure/origin,
    CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not
    global absence, inactivity, potency or target-mechanism proof.
  snapshot_sha256: 6ad28a5dd301fac51ee52e70ca0789cd040a1906660932acedd202703d786e11
  search_scope: Exact owner full-key/CID scope; blank-AID rows are sentinels. No other-owner
    assay is transferred.
- evidence_id: bgc-2794-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters(includeUnassigned=True)'
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: The source stereo_complete flag tests unassigned atom-centred chirality,
    not all double-bond geometry or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2794-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines 295-306: choose_pathway'
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: Exactly one supported mapped pathway selects filing; zero, unsupported
    single or multiple labels retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2794-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 2 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
- evidence_id: bgc-2794-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 3109-3109; raw record sha256 b87ce801a6c0d741031e8be1bb785bb2a52640d8dfd990af04d72abf58147f6f
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: All 25 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2794-row-mibig_compounds-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 3227-3227; raw record sha256 0a92f9cde3a65eaa9adc69ebc5a930f0ee8c42bfd81438e4d47405fd0264a856
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: All 25 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2794-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: 'Complete saved chebi_structures frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/muscoride-b.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RYLVRVUEEVJKJO-OPXMRZJTSA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2794-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 1 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
- evidence_id: bgc-2794-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 8286-8286; raw record sha256 3412c3e25f0b9fc8e3986c8184a2aa297d61bc15ffc10cf64ff123df3a1c6d2b
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: All 6 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2794-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences frame: 0 positive placements, with
    all fields and bounded query meanings read.'
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/muscoride-b.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RYLVRVUEEVJKJO-OPXMRZJTSA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2794-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 positive placements, with all fields
    and bounded query meanings read.'
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
- evidence_id: bgc-2794-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2196-2196; raw record sha256 efdda7e299f5f74ebccf7f803fbc8736f6c2d0d668d2a373cb67aad7e2164195
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: All 7 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2794-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: 'Complete saved pubchem_bioassay frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/muscoride-b.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RYLVRVUEEVJKJO-OPXMRZJTSA-N",
    "table": "pubchem_bioassay"}'
- evidence_id: bgc-2794-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/muscoride-b.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RYLVRVUEEVJKJO-OPXMRZJTSA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2794-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 positive placements,
    with all fields and bounded query meanings read.'
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/muscoride-b.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RYLVRVUEEVJKJO-OPXMRZJTSA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2794-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: 'Complete saved chebi_origins frame: 0 positive placements, with all fields
    and bounded query meanings read.'
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/muscoride-b.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: bgc-2794-congener-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/muscoride-a.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 419669ca87f7b1933f451c660e564b06b5f3350607b94a9cc1b95d244ce46c77
- evidence_id: bgc-2794-reader-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/native-current280-muscoride-b-maintained-reader-DATA-001.json
  locator: /resolved_view; /raw_owner; /expected_view; /counts; /reader_call_count;
    /denials; /unexpected_denials; /external_requests
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: One original maintained call preserves the entire captured owner and all
    declared graph/pathway/history content.
  snapshot_sha256: e6258c72c6c3d9c371c0d8af991303a18ba3f33e0995774351a50ab5192e6f73
- evidence_id: bgc-2794-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/native-current280-muscoride-b-reader-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: Original ROOT maintained-reader execution and exit zero.
  snapshot_sha256: d05319c909d080b0c1baaf8d31c6ad7d8a7810e65708fa17e1013ff2b11323d7
- evidence_id: bgc-2794-reader-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-muscoride-b-reader-acceptance-001.json
  locator: /accepted; /review_check_contract; /verification; /limits
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: ROOT accepted complete-owner equality and the exact original check contract;
    scientific interpretation remains separate.
  snapshot_sha256: be778787c7eb24c34b8cffa6f8fa90164d008d59fec9d39b5854df418bf81695
- evidence_id: bgc-2794-reader-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-current280-muscoride-b-complete-reader-view-reading-001.json
  locator: /whole_returned_view; /interpretation; /counts
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: Complete actual returned view and every evidence/history meaning personally
    read, with no fresh sequence or primary verification.
  snapshot_sha256: 939711761e855693fce75850e893773ad15b1655108e03cac57b17cf0f8970df
- evidence_id: bgc-2794-graph
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280/native-current280-muscoride-b-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs; /resolved_view/biosynthetic_pathway; /resolved_view/curation_history
  accessed_at: '2026-11-07T00:37:37.683374Z'
  support: supports
  summary: The accepted single Muscoride B reader preserves the entire owner, one
    six-node/six-edge inline BIOSYNTHESIS graph, two proposed numbered steps and all
    four histories, with no components or molecular targets. MusE (A0A5Q0TX65) supplies
    precursor context for C-terminal and N-terminal prenylation; MusF1 (A0A5Q0TWZ6)
    and MusF2 (A0A5Q0TX00) are linked to those respective processes. The two process
    nodes and exact intermediates remain ungrounded; the product edges say contributes
    to the downstream bis-prenylated Muscoride B, not a directly specified one-step
    substrate-product transformation. Steps 1 and 2 retain proposed:true and do not
    establish a complete assembly route, the kinetic order of independent terminal
    modifications, proteolysis or oxazole formation. The annotations attribute enzymatic
    findings to DOI:10.1021/acschembio.9b00620 and historical 2026-09-28 GenBank/UniProt/GenPept
    checks of MK806444.1, QGA72599.1 (67 aa), QGA72595.1 and QGA72594.1 (300 aa each).
    Their 28 graph and eight pathway reference placements are repeated evidence attributions,
    not 36 independent experiments or fresh sequence verification. The saved product
    topology is compatible with two prenyl groups, but does not prove enzyme activity,
    protein-grounding accuracy or producer identity. The qualified partial representation
    is internally coherent with the UHCC-0398 scope; the PCC 7906 route, exact natural
    identity and underlying primary evidence remain separately unresolved.
  snapshot_sha256: e6258c72c6c3d9c371c0d8af991303a18ba3f33e0995774351a50ab5192e6f73
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:58:35.720629Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 11c07976d94801b8044a911f854cef59d220d80dafabd86673396f6a1ee54ae4
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:58:59.871180Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 54b4e29921ed94b48337f9938b95ac8c403d840bd704ec9c7c3c6fe215016937
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:59:19.061941Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:59:52.340365Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-07T00:00:03.873381Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: b0c41dbce9d0cef868a144aadc058261eb329ecea06a3affb0e50465adf478e0
assessments:
- assessment_id: bgc-2794-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: muscoride B retains exact identifier naturalproductmech:mibig-f4bf230570,
    complete key RYLVRVUEEVJKJO-OPXMRZJTSA-N, and source rows BGC0002485 v2 compound
    index 2; BGC0002551 v2 compound index 2. Cross-references (npatlas:NPA025875)
    remain attributed identifiers, not fresh authority confirmation. Both saved forms
    normalize to C31H41N5O6 and the declared full key. The OPEN shared-structure discussion
    remains unresolved; multiple source concepts and computational agreement do not
    independently adjudicate the source identity.
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  evidence_ids:
  - bgc-2794-identity
  - bgc-2794-chemistry
  - bgc-2794-query-mibig_compounds
  - bgc-2794-plan
  - bgc-2794-row-mibig_compounds-0
  - bgc-2794-row-mibig_compounds-1
  - bgc-2794-congener-0
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    value: RYLVRVUEEVJKJO-OPXMRZJTSA-N
    evidence_ids:
    - bgc-2794-identity
    - bgc-2794-chemistry
    - bgc-2794-query-mibig_compounds
    - bgc-2794-plan
    - bgc-2794-row-mibig_compounds-0
    - bgc-2794-row-mibig_compounds-1
    - bgc-2794-congener-0
  - name: grounding_scope
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    value: muscoride B retains exact identifier naturalproductmech:mibig-f4bf230570,
      complete key RYLVRVUEEVJKJO-OPXMRZJTSA-N, and source rows BGC0002485 v2 compound
      index 2; BGC0002551 v2 compound index 2. Cross-references (npatlas:NPA025875)
      remain attributed identifiers, not fresh authority confirmation. Both saved
      forms normalize to C31H41N5O6 and the declared full key. The OPEN shared-structure
      discussion remains unresolved; multiple source concepts and computational agreement
      do not independently adjudicate the source identity.
    evidence_ids:
    - bgc-2794-identity
    - bgc-2794-chemistry
    - bgc-2794-query-mibig_compounds
    - bgc-2794-plan
    - bgc-2794-row-mibig_compounds-0
    - bgc-2794-row-mibig_compounds-1
    - bgc-2794-congener-0
- assessment_id: bgc-2794-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: 'The saved Muscoride B forms each contain 42 atoms and 45 bonds. Four five-membered
    rings comprise one saturated nitrogen-containing ring and three aromatic N/O oxazole-like
    rings. The SMILES graph contains tertiary amide C11(=O12)-N13 and ester C27(=O28)-O29-C30.
    Separate N-linked and ester-O-linked isoprenyl substituents are explicit at N5-C6-C7=C8
    and O29-C30-C31=C32. This is compatible with the recorded bis-prenylated product,
    but the molecule alone does not demonstrate MusF1 or MusF2 catalysis. All three
    potential tetrahedral centres are specified S in the saved SMILES graph (C2, C4
    and C17), with corresponding S centres in the InChI-derived graph. Each isoprenyl
    alkene has two methyl substituents on one end, so neither is an E/Z stereogenic
    double bond; absence of an E/Z potential is not missing geometry. The retained
    true stereo flag and this saved agreement do not independently certify natural
    absolute stereochemistry. Both canonical SMILES comparisons are true and the saved
    chirality-aware match contains all 42 atoms. The tertiary amide and ester are
    retained without secondary-amide/imidic relocation. Formula, aggregate charge,
    atom/bond counts, normalized Standard InChI and full key also agree. The diagnostic
    explicitly leaves full_graph_identity_established false: the one-way match and
    canonical agreement are limited computational consistency evidence, not independent
    natural identity or primary experimental certification.'
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  evidence_ids:
  - bgc-2794-identity
  - bgc-2794-chemistry
  - bgc-2794-molecular-reading
  - bgc-2794-diagnostic-acceptance
  - bgc-2794-diagnostic-stderr
  - bgc-2794-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    value: All three potential tetrahedral centres are specified S in the saved SMILES
      graph (C2, C4 and C17), with corresponding S centres in the InChI-derived graph.
      Each isoprenyl alkene has two methyl substituents on one end, so neither is
      an E/Z stereogenic double bond; absence of an E/Z potential is not missing geometry.
      The retained true stereo flag and this saved agreement do not independently
      certify natural absolute stereochemistry.
    evidence_ids:
    - bgc-2794-identity
    - bgc-2794-chemistry
    - bgc-2794-molecular-reading
    - bgc-2794-diagnostic-acceptance
    - bgc-2794-diagnostic-stderr
    - bgc-2794-stereo-policy
  - name: representation_correspondence
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    value: 'Both canonical SMILES comparisons are true and the saved chirality-aware
      match contains all 42 atoms. The tertiary amide and ester are retained without
      secondary-amide/imidic relocation. Formula, aggregate charge, atom/bond counts,
      normalized Standard InChI and full key also agree. The diagnostic explicitly
      leaves full_graph_identity_established false: the one-way match and canonical
      agreement are limited computational consistency evidence, not independent natural
      identity or primary experimental certification.'
    evidence_ids:
    - bgc-2794-identity
    - bgc-2794-chemistry
    - bgc-2794-molecular-reading
    - bgc-2794-diagnostic-acceptance
    - bgc-2794-diagnostic-stderr
    - bgc-2794-stereo-policy
- assessment_id: bgc-2794-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: Desmonostoc sp. PCC 7906 (NCBITaxon:1181) and Nostoc sp. UHCC-0398 (2665154)
    remain two separate SOURCE_ASSERTION producer claims. The Nostoc occurrence label
    (1177) supplies neither strain equivalence nor a causal producer experiment. The
    partial MusE/MusF1/MusF2 mechanism is explicitly scoped to the UHCC-0398 route
    and is not transferred to PCC 7906. Both MIBiG entries are v2, active, questionable
    in quality and unknown in completeness. BGC0002485 uses MK806443.1:1-14448 with
    heterologous expression; BGC0002551 uses MK806444.1:1-13360 with enzymatic assays.
    Both retain CLUSTER_DEMONSTRATED locus support and ENTRY PMID:31674754. Shared
    citation and full key do not collapse the two locus/producer routes or independently
    resolve their OPEN identity discussion.
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  evidence_ids:
  - bgc-2794-provenance
  - bgc-2794-query-mibig_compounds
  - bgc-2794-taxonomy
  - bgc-2794-curation
  - bgc-2794-row-mibig_compounds-0
  - bgc-2794-row-mibig_compounds-1
  - bgc-2794-reader-DATA
  - bgc-2794-graph
  dimensions:
  - name: taxon_scope
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    value: Desmonostoc sp. PCC 7906 (NCBITaxon:1181) and Nostoc sp. UHCC-0398 (2665154)
      remain two separate SOURCE_ASSERTION producer claims. The Nostoc occurrence
      label (1177) supplies neither strain equivalence nor a causal producer experiment.
      The partial MusE/MusF1/MusF2 mechanism is explicitly scoped to the UHCC-0398
      route and is not transferred to PCC 7906.
    evidence_ids:
    - bgc-2794-provenance
    - bgc-2794-query-mibig_compounds
    - bgc-2794-taxonomy
    - bgc-2794-curation
    - bgc-2794-row-mibig_compounds-0
    - bgc-2794-row-mibig_compounds-1
    - bgc-2794-reader-DATA
    - bgc-2794-graph
  - name: producer_evidence
    definition: Producer evidence grade and its demonstrated or asserted scope.
    value: Desmonostoc sp. PCC 7906 (NCBITaxon:1181) and Nostoc sp. UHCC-0398 (2665154)
      remain two separate SOURCE_ASSERTION producer claims. The Nostoc occurrence
      label (1177) supplies neither strain equivalence nor a causal producer experiment.
      The partial MusE/MusF1/MusF2 mechanism is explicitly scoped to the UHCC-0398
      route and is not transferred to PCC 7906.
    evidence_ids:
    - bgc-2794-provenance
    - bgc-2794-query-mibig_compounds
    - bgc-2794-taxonomy
    - bgc-2794-curation
    - bgc-2794-row-mibig_compounds-0
    - bgc-2794-row-mibig_compounds-1
    - bgc-2794-reader-DATA
    - bgc-2794-graph
  - name: locus_evidence
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    value: Both MIBiG entries are v2, active, questionable in quality and unknown
      in completeness. BGC0002485 uses MK806443.1:1-14448 with heterologous expression;
      BGC0002551 uses MK806444.1:1-13360 with enzymatic assays. Both retain CLUSTER_DEMONSTRATED
      locus support and ENTRY PMID:31674754. Shared citation and full key do not collapse
      the two locus/producer routes or independently resolve their OPEN identity discussion.
    evidence_ids:
    - bgc-2794-provenance
    - bgc-2794-query-mibig_compounds
    - bgc-2794-taxonomy
    - bgc-2794-curation
    - bgc-2794-row-mibig_compounds-0
    - bgc-2794-row-mibig_compounds-1
    - bgc-2794-reader-DATA
    - bgc-2794-graph
- assessment_id: bgc-2794-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: 'BGC0002485: PMID:31674754 at ENTRY grain; BGC0002551: PMID:31674754 at
    ENTRY grain. These are attributed database citations, not newly examined primary
    bodies. DOI case variants and repeated placements do not create independent evidence.
    All 4 histories were read: 3 are seeder-attributed SEEDED_FROM_SOURCES events.
    The remaining 2026-09-28 codex event adds the explicitly partial terminal-prenylation
    graph/pathway; its historical primary and sequence claims are retained without
    fresh verification.'
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  evidence_ids:
  - bgc-2794-history
  - bgc-2794-source-reading
  - bgc-2794-query-mibig_compounds
  - bgc-2794-row-mibig_compounds-0
  - bgc-2794-row-mibig_compounds-1
  - bgc-2794-row-lotus_occurrences-0
  dimensions:
  - name: citation_scope
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    value: 'BGC0002485: PMID:31674754 at ENTRY grain; BGC0002551: PMID:31674754 at
      ENTRY grain. These are attributed database citations, not newly examined primary
      bodies. DOI case variants and repeated placements do not create independent
      evidence. All 4 histories were read: 3 are seeder-attributed SEEDED_FROM_SOURCES
      events. The remaining 2026-09-28 codex event adds the explicitly partial terminal-prenylation
      graph/pathway; its historical primary and sequence claims are retained without
      fresh verification.'
    evidence_ids:
    - bgc-2794-history
    - bgc-2794-source-reading
    - bgc-2794-query-mibig_compounds
    - bgc-2794-row-mibig_compounds-0
    - bgc-2794-row-mibig_compounds-1
    - bgc-2794-row-lotus_occurrences-0
- assessment_id: bgc-2794-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: One exact-key LOTUS tuple names Nostoc (1177) with DOI:10.1021/ACSCHEMBIO.9B00620.
    The case variant of the mechanism DOI is the same citation, not independent primary
    corroboration. The occurrence is not a third experimentally established producer
    route. The saved PubChem BioAssay frame has no row or blank sentinel for this
    owner. No actual AID or molecular target is captured. ChEBI structure/origin,
    CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not
    global absence, inactivity, potency or target-mechanism proof.
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  evidence_ids:
  - bgc-2794-roots
  - bgc-2794-query-lotus_occurrences
  - bgc-2794-query-chebi_origins
  - bgc-2794-query-cyanometdb_occurrences
  - bgc-2794-query-pubchem_bioassay
  - bgc-2794-query-bindingdb_targets
  - bgc-2794-query-antibioticmech_inchikeys
  - bgc-2794-assay-curation
  - bgc-2794-row-lotus_occurrences-0
  - bgc-2794-reader-DATA
  - bgc-2794-graph
  dimensions:
  - name: occurrence_scope
    definition: Exact retained occurrence tuples and limits on production/independence.
    value: One exact-key LOTUS tuple names Nostoc (1177) with DOI:10.1021/ACSCHEMBIO.9B00620.
      The case variant of the mechanism DOI is the same citation, not independent
      primary corroboration. The occurrence is not a third experimentally established
      producer route.
    evidence_ids:
    - bgc-2794-roots
    - bgc-2794-query-lotus_occurrences
    - bgc-2794-query-chebi_origins
    - bgc-2794-query-cyanometdb_occurrences
    - bgc-2794-query-pubchem_bioassay
    - bgc-2794-query-bindingdb_targets
    - bgc-2794-query-antibioticmech_inchikeys
    - bgc-2794-assay-curation
    - bgc-2794-row-lotus_occurrences-0
    - bgc-2794-reader-DATA
    - bgc-2794-graph
  - name: assay_target_scope
    definition: Retained activity/assay/target positives and bounded negative queries.
    value: The saved PubChem BioAssay frame has no row or blank sentinel for this
      owner. No actual AID or molecular target is captured. ChEBI structure/origin,
      CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives,
      not global absence, inactivity, potency or target-mechanism proof.
    evidence_ids:
    - bgc-2794-roots
    - bgc-2794-query-lotus_occurrences
    - bgc-2794-query-chebi_origins
    - bgc-2794-query-cyanometdb_occurrences
    - bgc-2794-query-pubchem_bioassay
    - bgc-2794-query-bindingdb_targets
    - bgc-2794-query-antibioticmech_inchikeys
    - bgc-2794-assay-curation
    - bgc-2794-row-lotus_occurrences-0
    - bgc-2794-reader-DATA
    - bgc-2794-graph
- assessment_id: bgc-2794-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: The model returns Alkaloids and Amino acids and Peptides, with empty superclass/class
    arrays and is_glycoside:false; UNCLASSIFIED follows the maintained multi-label
    rule. Source RIBOSOMAL/OTHER/TERPENE labels remain attributed. Structural prenyl
    groups and the partial curated pathway add qualified context without converting
    model labels into a fully demonstrated assembly pathway.
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  evidence_ids:
  - bgc-2794-classification
  - bgc-2794-chemistry
  - bgc-2794-query-npclassifier
  - bgc-2794-query-mibig_compounds
  - bgc-2794-filing-policy
  - bgc-2794-row-npclassifier-0
  - bgc-2794-reader-DATA
  - bgc-2794-graph
  dimensions:
  - name: classification_applicability
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    value: The model returns Alkaloids and Amino acids and Peptides, with empty superclass/class
      arrays and is_glycoside:false; UNCLASSIFIED follows the maintained multi-label
      rule. Source RIBOSOMAL/OTHER/TERPENE labels remain attributed. Structural prenyl
      groups and the partial curated pathway add qualified context without converting
      model labels into a fully demonstrated assembly pathway.
    evidence_ids:
    - bgc-2794-classification
    - bgc-2794-chemistry
    - bgc-2794-query-npclassifier
    - bgc-2794-query-mibig_compounds
    - bgc-2794-filing-policy
    - bgc-2794-row-npclassifier-0
    - bgc-2794-reader-DATA
    - bgc-2794-graph
- assessment_id: bgc-2794-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: unknown
  summary: Whole current owner and all 4 histories, nine saved source frames (4 positive
    placements/63 fields and 6 negatives), and both complete saved molecular forms
    were personally read. All 47 actual input hashes and maintained ownership paths
    join the accepted plan. Input pinning is not a claim to have substantively read
    every entire corpus. Five original local gates passed. One inline graph and two
    proposed pathway steps require the separately accepted maintained reader; no component
    or molecular-target root is present. Full QC/OAK, fresh source-authority checks
    and independent primary confirmation remain unavailable; completion is partial.
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  evidence_ids:
  - bgc-2794-owner
  - bgc-2794-history
  - bgc-2794-intake
  - bgc-2794-intake-acceptance
  - bgc-2794-plan
  - bgc-2794-plan-acceptance
  - bgc-2794-gates
  - bgc-2794-source-reading
  - bgc-2794-source-notes
  - bgc-2794-molecular-reading
  - bgc-2794-roots
  - bgc-2794-reader-DATA
  - bgc-2794-reader-acceptance
  - bgc-2794-reader-reading
  dimensions:
  - name: review_completion
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    value: Whole current owner and all 4 histories, nine saved source frames (4 positive
      placements/63 fields and 6 negatives), and both complete saved molecular forms
      were personally read. All 47 actual input hashes and maintained ownership paths
      join the accepted plan. Input pinning is not a claim to have substantively read
      every entire corpus. Five original local gates passed. One inline graph and
      two proposed pathway steps require the separately accepted maintained reader;
      no component or molecular-target root is present. Full QC/OAK, fresh source-authority
      checks and independent primary confirmation remain unavailable; completion is
      partial.
    evidence_ids:
    - bgc-2794-owner
    - bgc-2794-history
    - bgc-2794-intake
    - bgc-2794-intake-acceptance
    - bgc-2794-plan
    - bgc-2794-plan-acceptance
    - bgc-2794-gates
    - bgc-2794-source-reading
    - bgc-2794-source-notes
    - bgc-2794-molecular-reading
    - bgc-2794-roots
    - bgc-2794-reader-DATA
    - bgc-2794-reader-acceptance
    - bgc-2794-reader-reading
- assessment_id: bgc-2794-graph
  area: graph
  topic: Partial UHCC-0398 terminal prenylation and historical evidence boundaries
  outcome: supported
  summary: The accepted single Muscoride B reader preserves the entire owner, one
    six-node/six-edge inline BIOSYNTHESIS graph, two proposed numbered steps and all
    four histories, with no components or molecular targets. MusE (A0A5Q0TX65) supplies
    precursor context for C-terminal and N-terminal prenylation; MusF1 (A0A5Q0TWZ6)
    and MusF2 (A0A5Q0TX00) are linked to those respective processes. The two process
    nodes and exact intermediates remain ungrounded; the product edges say contributes
    to the downstream bis-prenylated Muscoride B, not a directly specified one-step
    substrate-product transformation. Steps 1 and 2 retain proposed:true and do not
    establish a complete assembly route, the kinetic order of independent terminal
    modifications, proteolysis or oxazole formation. The annotations attribute enzymatic
    findings to DOI:10.1021/acschembio.9b00620 and historical 2026-09-28 GenBank/UniProt/GenPept
    checks of MK806444.1, QGA72599.1 (67 aa), QGA72595.1 and QGA72594.1 (300 aa each).
    Their 28 graph and eight pathway reference placements are repeated evidence attributions,
    not 36 independent experiments or fresh sequence verification. The saved product
    topology is compatible with two prenyl groups, but does not prove enzyme activity,
    protein-grounding accuracy or producer identity. The qualified partial representation
    is internally coherent with the UHCC-0398 scope; the PCC 7906 route, exact natural
    identity and underlying primary evidence remain separately unresolved.
  target_ids:
  - naturalproductmech:mibig-f4bf230570
  evidence_ids:
  - bgc-2794-reader-DATA
  - bgc-2794-reader-execution
  - bgc-2794-reader-acceptance
  - bgc-2794-reader-reading
  - bgc-2794-graph
  - bgc-2794-chemistry
  - bgc-2794-provenance
  dimensions: []
findings: []
actions: []
limitations:
- Fresh source-authority, primary publication, sequence and strain verification remain
  unavailable. Full QC/OAK were not run; retained experimental grades stay source-attributed.
- 'Both canonical SMILES comparisons are true and the saved chirality-aware match
  contains all 42 atoms. The tertiary amide and ester are retained without secondary-amide/imidic
  relocation. Formula, aggregate charge, atom/bond counts, normalized Standard InChI
  and full key also agree. The diagnostic explicitly leaves full_graph_identity_established
  false: the one-way match and canonical agreement are limited computational consistency
  evidence, not independent natural identity or primary experimental certification.
  Four undefined-stereo and two proton-added/removed warnings remain globally unassigned;
  no message is attributed to this owner.'
- All three potential tetrahedral centres are specified S in the saved SMILES graph
  (C2, C4 and C17), with corresponding S centres in the InChI-derived graph. Each
  isoprenyl alkene has two methyl substituents on one end, so neither is an E/Z stereogenic
  double bond; absence of an E/Z potential is not missing geometry. The retained true
  stereo flag and this saved agreement do not independently certify natural absolute
  stereochemistry.
- Saved topology supports the encoded molecule without independently establishing
  every natural residue, biosynthetic reaction or pharmacological mechanism.
- The accepted reader proves complete preservation and maintained structural consistency,
  not scientific validity of every grounding or primary claim. The MusF route is partial,
  both steps remain proposed, exact intermediates are ungrounded and the OPEN two-source
  identity discussion remains unresolved.
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
- batch-280
```
