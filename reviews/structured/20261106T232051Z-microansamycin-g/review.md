# Local evidence review: microansamycin G

- Review: 20261106T232051Z-microansamycin-g
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T22:48:57.534036Z
- Finished UTC: 2026-11-06T23:20:51.443669Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Microansamycin G retains its exact full-key source identity and an oxygenated fused-ring scaffold with a ketone and glycolamide. One amide/imidic representation change and an unspecified alkene limit exact structural certification. Producer and locus remain source assertions; the local review passes with limitations and partial completion.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2781; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-216120fec9 | data/natural_products/unclassified/microansamycin-g.yaml | generated | microansamycin G |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-216120fec9 | Both exact stored forms parsed in the original 20-attempt diagnostic and agree in formula, aggregate charge, normalized Standard InChI and full key. |
| strict_ten | passed | True | naturalproductmech:mibig-216120fec9 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-216120fec9 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-216120fec9 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-216120fec9 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-216120fec9 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-216120fec9 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-216120fec9 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-216120fec9 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: naturalproductmech:mibig-216120fec9.

microansamycin G retains exact owner naturalproductmech:mibig-216120fec9, complete key CYYOWCJHSDSDCW-JKSUJKDBSA-N, and MIBiG BGC0001666 v3 compound index 7. Its retained cross-references (npatlas:NPA023915, pubchem:139591130) are source-attributed, not remotely adjudicated. Both original forms normalize to C18H23NO6 and the full declared key. Distinct shared-BGC companions remain separate by their complete keys and source compound indices; no identity or experimental transfer follows.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-216120fec9.

The two saved forms each contain 25 atoms and 26 bonds. A seven-membered oxygen heterocycle is fused to an aromatic six-ring. In the stored SMILES graph, ketone C2=O3 and glycolamide N18-C19(=O20)-C21-O22H are separate; phenolic O17H, ring alcohol O23H and the C6-O12-C11 ether are explicit. No strict ester motif is present. This supports the encoded oxygenated cyclic scaffold without inferring a macrolactam or congener-specific biosynthesis. The SMILES table specifies C6 R and C7 S, while C4=C5 has unspecified geometry. The InChI form retains two specified tetrahedral centres plus that unspecified alkene and an additional unspecified imidic C=N potential. The stored stereo_complete:true flag follows the extractor atom-centred rule; it does not certify all double-bond geometry or natural absolute stereochemistry. The glycolamide C19(=O20)-N18 is represented as a terminal C(OH)=N site in the InChI-derived graph; the separate ketone remains. Strict amide counts change from one to zero and carbonyl counts from two to one. The original forms agree in formula, aggregate charge, atom/bond counts, normalized Standard InChI and full key, but both canonical SMILES comparisons are false and the one-way atom map is empty. All full-graph identity flags are false. Mobile-hydrogen normalization explains a bounded representation difference; it does not certify exact tautomeric or natural identity and is not by itself a record defect.

### Producer assertion versus locus evidence

provenance: supported. Targets: naturalproductmech:mibig-216120fec9.

Micromonospora sp. HK160111 (NCBITaxon:1245497) remains the MIBiG SOURCE_ASSERTION producer. The separate genus-labelled Micromonospora occurrence (1873) does not demonstrate strain production. Cached names supply no independent rank, lineage or strain confirmation. BGC0001666 v3 is retained as active with questionable quality and unknown completeness. MG018799.1 has no retained coordinates or locus method, so CLUSTER_UNSTATED is preserved. COMPOUND_EVIDENCE citation grain improves attribution to this source compound but is not new primary verification or a knockout demonstration.

### Citation grain and attributed history

evidence: supported. Targets: naturalproductmech:mibig-216120fec9.

PMID:29412682 retains MIBiG COMPOUND_EVIDENCE citation grain. LOTUS DOI strings stay attached to their occurrence tuples; distinct databases or citation placements do not establish independent experiments. Underlying primary claims were not newly verified. Both of the 2 history events are SEEDED_FROM_SOURCES and seeder-attributed.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: naturalproductmech:mibig-216120fec9.

The one LOTUS tuple attributes this full key to Micromonospora (1873) with DOI:10.1021/ACS.ORGLETT.7B04018. It remains an occurrence assertion, separate from the HK160111 producer and not an independent primary experiment. One retained PubChem BioAssay row has an empty AID and no assay result; it is a blank sentinel, not a measured activity or target. No actual AID or measured target is captured. ChEBI structures/origins, CyanoMetDB, BindingDB and AntibioticMech queries are bounded negatives. These do not establish global absence, inactivity, potency or mechanism.

### Computed filing and asserted class applicability

consistency: supported. Targets: naturalproductmech:mibig-216120fec9.

UNCLASSIFIED follows the empty NPClassifier pathway array; its superclass/class arrays are also empty and is_glycoside is false. Source Cyclic polyketide/Polycyclic polyketide and PKS labels remain source assertions rather than classifier outputs. The saved two-ring topology is structurally compatible, but does not verify a biosynthetic pathway.

### Local completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-216120fec9.

Whole current owner and its 2 seeder histories, all nine saved source frames (4 positive placements/49 fields and 5 negatives), and both complete original molecular tables were read. All 52 actual input hashes and maintained ownership declarations were joined; this is not a claim to have substantively read every entire input corpus. Five original local gates passed. Full QC/OAK, live source-authority checks and independent primary confirmation remain unavailable, so completion is partial. No literal graph/pathway/component/target root requires a maintained reader. Any later correction belongs in maintained inputs, applicable curation, extractors or the seeder.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2781-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/microansamycin-g.yaml; Whole retained plaintext including all curation_history entries | supports | Complete current owner and every history entry personally read in the attributed source pass and current captured-owner readback; bytes equal accepted capture. |
| bgc-2781-identity | /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status | supports | microansamycin G retains exact owner naturalproductmech:mibig-216120fec9, complete key CYYOWCJHSDSDCW-JKSUJKDBSA-N, and MIBiG BGC0001666 v3 compound index 7. Its retained cross-references (npatlas:NPA023915, pubchem:139591130) are source-attributed, not remotely adjudicated. Both original forms normalize to C18H23NO6 and the full declared key. Distinct shared-BGC companions remain separate by their complete keys and source compound indices; no identity or experimental transfer follows. |
| bgc-2781-history | /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json; /records/0/owner_document/curation_history | supports | PMID:29412682 retains MIBiG COMPOUND_EVIDENCE citation grain. LOTUS DOI strings stay attached to their occurrence tuples; distinct databases or citation placements do not establish independent experiments. Underlying primary claims were not newly verified. Both of the 2 history events are SEEDED_FROM_SOURCES and seeder-attributed. |
| bgc-2781-provenance | /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters | supports | Micromonospora sp. HK160111 (NCBITaxon:1245497) remains the MIBiG SOURCE_ASSERTION producer. The separate genus-labelled Micromonospora occurrence (1873) does not demonstrate strain production. Cached names supply no independent rank, lineage or strain confirmation. BGC0001666 v3 is retained as active with questionable quality and unknown completeness. MG018799.1 has no retained coordinates or locus method, so CLUSTER_UNSTATED is preserved. COMPOUND_EVIDENCE citation grain improves attribution to this source compound but is not new primary verification or a knockout demonstration. |
| bgc-2781-classification | /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json; /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway; /records/0/owner_document/bgc_class | supports | UNCLASSIFIED follows the empty NPClassifier pathway array; its superclass/class arrays are also empty and is_glycoside is false. Source Cyclic polyketide/Polycyclic polyketide and PKS labels remain source assertions rather than classifier outputs. The saved two-ring topology is structurally compatible, but does not verify a biosynthetic pathway. |
| bgc-2781-roots | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/17/complete_root_keys; /contexts/17/declared_mechanism_roots_literal; /contexts/17/literal_bioactivities_root | context_only | Complete saved root declarations have no positive mechanism, component, target or measured activity root; no maintained reader applies. |
| bgc-2781-chemistry | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-DATA-001.json; /records/0/smiles/computed; /records/0/inchi/computed; /records/0/comparisons; /records/0/atom_correspondence | supports | The two saved forms each contain 25 atoms and 26 bonds. A seven-membered oxygen heterocycle is fused to an aromatic six-ring. In the stored SMILES graph, ketone C2=O3 and glycolamide N18-C19(=O20)-C21-O22H are separate; phenolic O17H, ring alcohol O23H and the C6-O12-C11 ether are explicit. No strict ester motif is present. This supports the encoded oxygenated cyclic scaffold without inferring a macrolactam or congener-specific biosynthesis. The SMILES table specifies C6 R and C7 S, while C4=C5 has unspecified geometry. The InChI form retains two specified tetrahedral centres plus that unspecified alkene and an additional unspecified imidic C=N potential. The stored stereo_complete:true flag follows the extractor atom-centred rule; it does not certify all double-bond geometry or natural absolute stereochemistry. The glycolamide C19(=O20)-N18 is represented as a terminal C(OH)=N site in the InChI-derived graph; the separate ketone remains. Strict amide counts change from one to zero and carbonyl counts from two to one. The original forms agree in formula, aggregate charge, atom/bond counts, normalized Standard InChI and full key, but both canonical SMILES comparisons are false and the one-way atom map is empty. All full-graph identity flags are false. Mobile-hydrogen normalization explains a bounded representation difference; it does not certify exact tautomeric or natural identity and is not by itself a record defect. |
| bgc-2781-molecular-reading | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-current279-first-five-molecular-reading-002.json; /records/0; /scope_orders; /method_limits | supports | Complete saved tables personally read; representation-aware interpretation retained without a new parse. |
| bgc-2781-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /DATA; /parse_attempts; /scope | supports | ROOT accepted 20 original stored-form parses; canonical and full-identity limits are preserved. |
| bgc-2781-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-execution-001.json; /command; /exit_code | supports | Original ROOT diagnostic argv and exit zero, without replay. |
| bgc-2781-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-original-001.stderr; Complete original stderr including blank separators | context_only | Six undefined-stereo warnings remain globally unassigned. |
| bgc-2781-intake | /private/tmp/npm-review-work/shared-next-batch279/intakes-001/2781-inspect-001.json; /targets; /source/inputs | supports | One exact target, 52 current inputs and explicit maintained owner paths. |
| bgc-2781-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch279/root-current279-intake-acceptance-001.json; /accepted; /intake_summary; /records; /source_placements; /unique_source_paths | supports | ROOT accepted ten original inspections with 469 input placements/70 paths and empty stderr. |
| bgc-2781-plan | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-target-input-plan-001.json; /records/0 | supports | Exact current input map with 8 direct companion paths and no reader requirement. |
| bgc-2781-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch279/root-current279-input-plan-acceptance-001.json; /accepted; /input_plan; /source_placements; /unique_source_paths | supports | ROOT accepted the actual current source input plan. |
| bgc-2781-gates | /private/tmp/npm-review-work/shared-next-batch279/root-current279-five-gates-acceptance-001.json; /records; /full_native_checks_passed; /unavailable_checks; /selected_queue_rows | context_only | Five local gates passed. Queue entries are bounded leads; full QC/OAK remain unavailable and gate passes do not establish biology. |
| bgc-2781-source-reading | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-current279-assigned-source-reading-002.json; /contexts/17; /counts; /reading_attribution | supports | All 4 positive source dictionaries/49 fields and 5 negative frames were read in the separately attributed source pass. |
| bgc-2781-source-notes | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-scope-notes-001.json; /totals; /reading_reconciliation; /reading_boundaries | context_only | Current 111 rows/1,335 fields retain BGC 90 and Support 21 primary-row attribution; Native/ROOT have zero primary-row credit. |
| bgc-2781-taxonomy | /private/tmp/npm-review-work/shared-next-batch279-tentative/native-prep/native-current279-cached-taxonomy-reading-001.json; /scope; /context_interpretations/17; /interpretation | context_only | Micromonospora sp. HK160111 (NCBITaxon:1245497) remains the MIBiG SOURCE_ASSERTION producer. The separate genus-labelled Micromonospora occurrence (1873) does not demonstrate strain production. Cached names supply no independent rank, lineage or strain confirmation. Cached stanzas contain no rank or lineage; no external taxonomy upgrade follows. |
| bgc-2781-curation | /private/tmp/npm-review-work/shared-next-batch279-tentative/native-prep/native-current279-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation | context_only | Native scanned nine substantive tables/3,422 rows. All 98 lexical candidates fail the current exact predicates. No applicable correction; reserved census-only tables remain excluded. |
| bgc-2781-assay-curation | /private/tmp/npm-review-work/shared-next-batch279-tentative/native-prep/native-current279-implemented-curation-scan-001.json; /assay_scope | context_only | One retained PubChem BioAssay row has an empty AID and no assay result; it is a blank sentinel, not a measured activity or target. No actual AID or measured target is captured. ChEBI structures/origins, CyanoMetDB, BindingDB and AntibioticMech queries are bounded negatives. These do not establish global absence, inactivity, potency or mechanism. |
| bgc-2781-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters(includeUnassigned=True) | context_only | stereo_complete tests unassigned atom-centred chirality; it does not certify every bond configuration or natural identity. |
| bgc-2781-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306: choose_pathway | context_only | Exactly one supported mapped pathway selects filing; unsupported single, zero or multiple labels retain UNCLASSIFIED while keeping all predictions. |
| bgc-2781-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 positive placements with every retained field and negative predicate read. |
| bgc-2781-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 1991-1991; raw record sha256 b4606cd143c4793e496378b85da25fea30ef2907aadc3cf922d1ed08f232eb2d | supports | All 25 fields read, preserving literal blanks, source qualifiers and citation grain. |
| bgc-2781-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures frame: 0 positive placements with every retained field and negative predicate read. |
| bgc-2781-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 1 positive placements with every retained field and negative predicate read. |
| bgc-2781-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 962-962; raw record sha256 88ee40ef3e431a870d14c4ede9de73c1aadb1f70cfe6a61ab04858049de5ced3 | supports | All 6 fields read, preserving literal blanks, source qualifiers and citation grain. |
| bgc-2781-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences frame: 0 positive placements with every retained field and negative predicate read. |
| bgc-2781-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 positive placements with every retained field and negative predicate read. |
| bgc-2781-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 367-367; raw record sha256 bbdfac729b31aa29c300be53a084b58271efa209e5dfdc98a6ef7cb19e6e0d8b | supports | All 7 fields read, preserving literal blanks, source qualifiers and citation grain. |
| bgc-2781-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame: 1 positive placements with every retained field and negative predicate read. |
| bgc-2781-row-pubchem_bioassay-0 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 947-947; raw record sha256 85e98f2ffa1ac5bb6f55fa19619cd5922c446ee27cb2ba25434960bcb157e311 | supports | All 11 fields read, preserving literal blanks, source qualifiers and citation grain. |
| bgc-2781-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets frame: 0 positive placements with every retained field and negative predicate read. |
| bgc-2781-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys frame: 0 positive placements with every retained field and negative predicate read. |
| bgc-2781-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json; /contexts/17/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins frame: 0 positive placements with every retained field and negative predicate read. |
| bgc-2781-congener-0 | /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/microansamycin-i.yaml; Complete current owner identity/source concepts and attributed history | context_only | Shared-BGC context has a separate full key and source compound index. No molecular identity, biological grade, activity or congener-specific experiment transfers. |
| bgc-2781-congener-1 | /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-a.yaml; Complete current owner identity/source concepts and attributed history | context_only | Shared-BGC context has a separate full key and source compound index. No molecular identity, biological grade, activity or congener-specific experiment transfers. |
| bgc-2781-congener-2 | /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-b.yaml; Complete current owner identity/source concepts and attributed history | context_only | Shared-BGC context has a separate full key and source compound index. No molecular identity, biological grade, activity or congener-specific experiment transfers. |
| bgc-2781-congener-3 | /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-c.yaml; Complete current owner identity/source concepts and attributed history | context_only | Shared-BGC context has a separate full key and source compound index. No molecular identity, biological grade, activity or congener-specific experiment transfers. |
| bgc-2781-congener-4 | /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-d.yaml; Complete current owner identity/source concepts and attributed history | context_only | Shared-BGC context has a separate full key and source compound index. No molecular identity, biological grade, activity or congener-specific experiment transfers. |
| bgc-2781-congener-5 | /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-e.yaml; Complete current owner identity/source concepts and attributed history | context_only | Shared-BGC context has a separate full key and source compound index. No molecular identity, biological grade, activity or congener-specific experiment transfers. |
| bgc-2781-congener-6 | /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-f.yaml; Complete current owner identity/source concepts and attributed history | context_only | Shared-BGC context has a separate full key and source compound index. No molecular identity, biological grade, activity or congener-specific experiment transfers. |
| bgc-2781-congener-7 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/microansamycin-h.yaml; Complete current owner identity/source concepts and attributed history | context_only | Shared-BGC context has a separate full key and source compound index. No molecular identity, biological grade, activity or congener-specific experiment transfers. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-279/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-279/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-279/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-279/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-279/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External authority, primary publications, sequence-level and strain-level confirmation were not newly obtained. Full QC/OAK are unavailable; source assertions and source-level experimental grades remain attributed.
- The glycolamide C19(=O20)-N18 is represented as a terminal C(OH)=N site in the InChI-derived graph; the separate ketone remains. Strict amide counts change from one to zero and carbonyl counts from two to one. The original forms agree in formula, aggregate charge, atom/bond counts, normalized Standard InChI and full key, but both canonical SMILES comparisons are false and the one-way atom map is empty. All full-graph identity flags are false. Mobile-hydrogen normalization explains a bounded representation difference; it does not certify exact tautomeric or natural identity and is not by itself a record defect. The six original undefined-stereo warnings remain globally unassigned.
- The SMILES table specifies C6 R and C7 S, while C4=C5 has unspecified geometry. The InChI form retains two specified tetrahedral centres plus that unspecified alkene and an additional unspecified imidic C=N potential. The stored stereo_complete:true flag follows the extractor atom-centred rule; it does not certify all double-bond geometry or natural absolute stereochemistry.
- Saved topology supports the encoded scaffold only; it does not independently establish every natural residue, reaction, pharmacological mechanism or biosynthetic pathway.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- This review concerns one exact captured target and its declared input scope. No record, native scientific status, source table or curation history is edited.
- Only retained original evidence was interpreted. This author performed no molecular parse, target execution, source-query replay or outbound request.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T232051Z-microansamycin-g
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: microansamycin G'
started_at: '2026-11-06T22:48:57.534036Z'
finished_at: '2026-11-06T23:20:51.443669Z'
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
summary: Microansamycin G retains its exact full-key source identity and an oxygenated
  fused-ring scaffold with a ketone and glycolamide. One amide/imidic representation
  change and an unspecified alkene limit exact structural certification. Producer
  and locus remain source assertions; the local review passes with limitations and
  partial completion.
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
  - path: data/natural_products/alkaloids/microansamycin-i.yaml
    sha256: 2e29826a0be2421992edc189a02ffe18d70350e9cae84e44601d56f1c85ce144
    role: context
  - path: data/natural_products/polyketides/microansamycin-a.yaml
    sha256: d77f6424cfeffb9620f21ea630c35f432f2cce704070018b88b96d76507b747e
    role: context
  - path: data/natural_products/polyketides/microansamycin-b.yaml
    sha256: c228f90ea6413d575c30814edab2ab40525854cfbe9c772aad50e2a7e3d40b2e
    role: context
  - path: data/natural_products/polyketides/microansamycin-c.yaml
    sha256: a6ddda6a8d68e5495e9c60af8b923d90c9fc9529a2bb6ff6b3475de0df25f5f7
    role: context
  - path: data/natural_products/polyketides/microansamycin-d.yaml
    sha256: e85fd46b9d396a7623f818b10c6b12247a20cdda780fb7a9376a73ce1c894b87
    role: context
  - path: data/natural_products/polyketides/microansamycin-e.yaml
    sha256: 0b6989c4a5928ac95285003840eaf23299a23fbb34bbad029e66f9f57d551d3e
    role: context
  - path: data/natural_products/polyketides/microansamycin-f.yaml
    sha256: e04fe8d1cc66a2d4b77f191a69d740d99b8639b50f9f0772a28263dec45d3c23
    role: context
  - path: data/natural_products/unclassified/microansamycin-g.yaml
    sha256: f0a82a19dab5ad613825725019ed12d327aba41a144deb1d15d10c4dbea2d7b2
    role: target
  - path: data/natural_products/unclassified/microansamycin-h.yaml
    sha256: c1e318e58620b9c3a8b5b2cd228dc32186e6a48822e23d57033a9009406ccedd
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
  selection: Campaign path order 2781; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-216120fec9
targets:
- target_id: naturalproductmech:mibig-216120fec9
  path: data/natural_products/unclassified/microansamycin-g.yaml
  label: microansamycin G
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnose279-001.py
    a7294b88d0cf543a0d838418f9f884f502b2a2fab9e2fe6292739731ec63e673 7d587c755373d7148002108737073753112d72744cddfc3b885327d4320222ed
    9e4bcf4327dbebf8f8b5387771e02cdcb2590d4507e185f6170391192bc3f389
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both exact stored forms parsed in the original 20-attempt diagnostic and
    agree in formula, aggregate charge, normalized Standard InChI and full key.
  scope_note: The glycolamide C19(=O20)-N18 is represented as a terminal C(OH)=N site
    in the InChI-derived graph; the separate ketone remains. Strict amide counts change
    from one to zero and carbonyl counts from two to one. The original forms agree
    in formula, aggregate charge, atom/bond counts, normalized Standard InChI and
    full key, but both canonical SMILES comparisons are false and the one-way atom
    map is empty. All full-graph identity flags are false. Mobile-hydrogen normalization
    explains a bounded representation difference; it does not certify exact tautomeric
    or natural identity and is not by itself a record defect. Six original warnings
    remain globally unassigned; no independent natural or primary biological certification.
  target_ids:
  - naturalproductmech:mibig-216120fec9
  evidence_ids:
  - bgc-2781-chemistry
  - bgc-2781-diagnostic-acceptance
  - bgc-2781-diagnostic-execution
  - bgc-2781-diagnostic-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-216120fec9
  command: just validate-strict data/natural_products/unclassified/microansamycin-g.yaml
    data/natural_products/unclassified/microansamycin-h.yaml data/natural_products/unclassified/micropeptin-k139.yaml
    data/natural_products/unclassified/microtermolide-a.yaml data/natural_products/unclassified/microviridin-1748.yaml
    data/natural_products/unclassified/microviridin-j.yaml data/natural_products/unclassified/microviridin-n5.yaml
    data/natural_products/unclassified/miharamycin-a-2.yaml data/natural_products/unclassified/miharamycin-a.yaml
    data/natural_products/unclassified/minimycin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-279/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-216120fec9
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-279/validate-all-001.tsv
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
  - naturalproductmech:mibig-216120fec9
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
  - naturalproductmech:mibig-216120fec9
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
  - naturalproductmech:mibig-216120fec9
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-279/review-queue-001.tsv
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
  - naturalproductmech:mibig-216120fec9
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-216120fec9
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-216120fec9
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2781-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/microansamycin-g.yaml
  locator: Whole retained plaintext including all curation_history entries
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: Complete current owner and every history entry personally read in the attributed
    source pass and current captured-owner readback; bytes equal accepted capture.
  snapshot_sha256: f0a82a19dab5ad613825725019ed12d327aba41a144deb1d15d10c4dbea2d7b2
- evidence_id: bgc-2781-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/chemical_structure;
    /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: microansamycin G retains exact owner naturalproductmech:mibig-216120fec9,
    complete key CYYOWCJHSDSDCW-JKSUJKDBSA-N, and MIBiG BGC0001666 v3 compound index
    7. Its retained cross-references (npatlas:NPA023915, pubchem:139591130) are source-attributed,
    not remotely adjudicated. Both original forms normalize to C18H23NO6 and the full
    declared key. Distinct shared-BGC companions remain separate by their complete
    keys and source compound indices; no identity or experimental transfer follows.
  snapshot_sha256: 7d587c755373d7148002108737073753112d72744cddfc3b885327d4320222ed
- evidence_id: bgc-2781-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json
  locator: /records/0/owner_document/curation_history
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: PMID:29412682 retains MIBiG COMPOUND_EVIDENCE citation grain. LOTUS DOI
    strings stay attached to their occurrence tuples; distinct databases or citation
    placements do not establish independent experiments. Underlying primary claims
    were not newly verified. Both of the 2 history events are SEEDED_FROM_SOURCES
    and seeder-attributed.
  snapshot_sha256: 7d587c755373d7148002108737073753112d72744cddfc3b885327d4320222ed
- evidence_id: bgc-2781-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: Micromonospora sp. HK160111 (NCBITaxon:1245497) remains the MIBiG SOURCE_ASSERTION
    producer. The separate genus-labelled Micromonospora occurrence (1873) does not
    demonstrate strain production. Cached names supply no independent rank, lineage
    or strain confirmation. BGC0001666 v3 is retained as active with questionable
    quality and unknown completeness. MG018799.1 has no retained coordinates or locus
    method, so CLUSTER_UNSTATED is preserved. COMPOUND_EVIDENCE citation grain improves
    attribution to this source compound but is not new primary verification or a knockout
    demonstration.
  snapshot_sha256: 7d587c755373d7148002108737073753112d72744cddfc3b885327d4320222ed
- evidence_id: bgc-2781-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch279/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway;
    /records/0/owner_document/bgc_class
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: UNCLASSIFIED follows the empty NPClassifier pathway array; its superclass/class
    arrays are also empty and is_glycoside is false. Source Cyclic polyketide/Polycyclic
    polyketide and PKS labels remain source assertions rather than classifier outputs.
    The saved two-ring topology is structurally compatible, but does not verify a
    biosynthetic pathway.
  snapshot_sha256: 7d587c755373d7148002108737073753112d72744cddfc3b885327d4320222ed
- evidence_id: bgc-2781-roots
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/17/complete_root_keys; /contexts/17/declared_mechanism_roots_literal;
    /contexts/17/literal_bioactivities_root
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Complete saved root declarations have no positive mechanism, component,
    target or measured activity root; no maintained reader applies.
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: Complete exact owner root set, not an inference of biological absence.
- evidence_id: bgc-2781-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/smiles/computed; /records/0/inchi/computed; /records/0/comparisons;
    /records/0/atom_correspondence
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: The two saved forms each contain 25 atoms and 26 bonds. A seven-membered
    oxygen heterocycle is fused to an aromatic six-ring. In the stored SMILES graph,
    ketone C2=O3 and glycolamide N18-C19(=O20)-C21-O22H are separate; phenolic O17H,
    ring alcohol O23H and the C6-O12-C11 ether are explicit. No strict ester motif
    is present. This supports the encoded oxygenated cyclic scaffold without inferring
    a macrolactam or congener-specific biosynthesis. The SMILES table specifies C6
    R and C7 S, while C4=C5 has unspecified geometry. The InChI form retains two specified
    tetrahedral centres plus that unspecified alkene and an additional unspecified
    imidic C=N potential. The stored stereo_complete:true flag follows the extractor
    atom-centred rule; it does not certify all double-bond geometry or natural absolute
    stereochemistry. The glycolamide C19(=O20)-N18 is represented as a terminal C(OH)=N
    site in the InChI-derived graph; the separate ketone remains. Strict amide counts
    change from one to zero and carbonyl counts from two to one. The original forms
    agree in formula, aggregate charge, atom/bond counts, normalized Standard InChI
    and full key, but both canonical SMILES comparisons are false and the one-way
    atom map is empty. All full-graph identity flags are false. Mobile-hydrogen normalization
    explains a bounded representation difference; it does not certify exact tautomeric
    or natural identity and is not by itself a record defect.
  snapshot_sha256: 3e1f6e3796bb1c289edf7dea5f0660e9f5917cfc6b690a115be7b583a9efe671
- evidence_id: bgc-2781-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-current279-first-five-molecular-reading-002.json
  locator: /records/0; /scope_orders; /method_limits
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: Complete saved tables personally read; representation-aware interpretation
    retained without a new parse.
  snapshot_sha256: c742df8bcfbb57808dfe1c860daede6182cb39e47619aab89c77b7c5212e50bd
- evidence_id: bgc-2781-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /DATA; /parse_attempts; /scope
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: ROOT accepted 20 original stored-form parses; canonical and full-identity
    limits are preserved.
  snapshot_sha256: faeda5d6678e25fea4f2481b52d4fab578df595a6ff7b6b5d065d7824f582230
- evidence_id: bgc-2781-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: Original ROOT diagnostic argv and exit zero, without replay.
  snapshot_sha256: fbcf86328e60d26eac7a770199fc2054f192983e22eab011c0de17d494281984
- evidence_id: bgc-2781-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr including blank separators
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Six undefined-stereo warnings remain globally unassigned.
  snapshot_sha256: 02c7027b4a2f575eff692bc02e20727a6cd814b2a504cc117a96b08f7c28703f
- evidence_id: bgc-2781-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/intakes-001/2781-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: One exact target, 52 current inputs and explicit maintained owner paths.
  snapshot_sha256: a829248b2219d47d40f650ba61632c365013830cf3b5578592185c4d1e669809
- evidence_id: bgc-2781-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/root-current279-intake-acceptance-001.json
  locator: /accepted; /intake_summary; /records; /source_placements; /unique_source_paths
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: ROOT accepted ten original inspections with 469 input placements/70 paths
    and empty stderr.
  snapshot_sha256: 9347c539f301f7d6e9bf7cb6449143f33930afed1aec9fd05b960d1fb399af87
- evidence_id: bgc-2781-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-target-input-plan-001.json
  locator: /records/0
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: Exact current input map with 8 direct companion paths and no reader requirement.
  snapshot_sha256: 9af820a19ec2457a4d2fb49a1d43086ac34ee266f4b058abf99f012d19473ddf
- evidence_id: bgc-2781-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/root-current279-input-plan-acceptance-001.json
  locator: /accepted; /input_plan; /source_placements; /unique_source_paths
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: ROOT accepted the actual current source input plan.
  snapshot_sha256: 418448d2207f4547fb83474f27fee432e10648b65e6c48729524a9d120aa6ef4
- evidence_id: bgc-2781-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch279/root-current279-five-gates-acceptance-001.json
  locator: /records; /full_native_checks_passed; /unavailable_checks; /selected_queue_rows
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Five local gates passed. Queue entries are bounded leads; full QC/OAK remain
    unavailable and gate passes do not establish biology.
  snapshot_sha256: b9027a83706e568c056855b68f4afbf896601b0fbd78abe415472276b68401f4
- evidence_id: bgc-2781-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-current279-assigned-source-reading-002.json
  locator: /contexts/17; /counts; /reading_attribution
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: All 4 positive source dictionaries/49 fields and 5 negative frames were
    read in the separately attributed source pass.
  snapshot_sha256: a47706e2c162e1c99e62a50ddec2d37b9dfc1992531b7dd4f2c3de35672bb6c8
- evidence_id: bgc-2781-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Current 111 rows/1,335 fields retain BGC 90 and Support 21 primary-row
    attribution; Native/ROOT have zero primary-row credit.
  snapshot_sha256: 2e1145cabe812c1418e0c6d14b17caf32fe0e6a57c3b2683f2337d28f8f4d686
- evidence_id: bgc-2781-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/native-prep/native-current279-cached-taxonomy-reading-001.json
  locator: /scope; /context_interpretations/17; /interpretation
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Micromonospora sp. HK160111 (NCBITaxon:1245497) remains the MIBiG SOURCE_ASSERTION
    producer. The separate genus-labelled Micromonospora occurrence (1873) does not
    demonstrate strain production. Cached names supply no independent rank, lineage
    or strain confirmation. Cached stanzas contain no rank or lineage; no external
    taxonomy upgrade follows.
  snapshot_sha256: 83a8fd84a6a63860446b23105de7dc89570492acd671888d45dcb815934e78dd
  search_scope: Exact current source-taxon route and retained cached names/synonyms;
    no inferred strain equivalence or hierarchy.
- evidence_id: bgc-2781-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/native-prep/native-current279-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Native scanned nine substantive tables/3,422 rows. All 98 lexical candidates
    fail the current exact predicates. No applicable correction; reserved census-only
    tables remain excluded.
  snapshot_sha256: 9bfe54d89a2923e73dfaead325e3d8422a7960e4a418c37d6330d94744fcca59
  search_scope: Current exact owner/source/occurrence/assay predicates over captured
    tables; two census-only inputs excluded.
- evidence_id: bgc-2781-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/native-prep/native-current279-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: One retained PubChem BioAssay row has an empty AID and no assay result;
    it is a blank sentinel, not a measured activity or target. No actual AID or measured
    target is captured. ChEBI structures/origins, CyanoMetDB, BindingDB and AntibioticMech
    queries are bounded negatives. These do not establish global absence, inactivity,
    potency or mechanism.
  snapshot_sha256: 9bfe54d89a2923e73dfaead325e3d8422a7960e4a418c37d6330d94744fcca59
  search_scope: Exact owner full-key/CID query; an empty-AID sentinel is not an assay.
    No other-owner evidence is transferred.
- evidence_id: bgc-2781-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters(includeUnassigned=True)'
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: stereo_complete tests unassigned atom-centred chirality; it does not certify
    every bond configuration or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2781-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines 295-306: choose_pathway'
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Exactly one supported mapped pathway selects filing; unsupported single,
    zero or multiple labels retain UNCLASSIFIED while keeping all predictions.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2781-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 positive placements with every
    retained field and negative predicate read.'
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
- evidence_id: bgc-2781-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 1991-1991; raw record sha256 b4606cd143c4793e496378b85da25fea30ef2907aadc3cf922d1ed08f232eb2d
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: All 25 fields read, preserving literal blanks, source qualifiers and citation
    grain.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2781-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: 'Complete saved chebi_structures frame: 0 positive placements with every
    retained field and negative predicate read.'
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/microansamycin-g.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "CYYOWCJHSDSDCW-JKSUJKDBSA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2781-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 1 positive placements with every
    retained field and negative predicate read.'
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
- evidence_id: bgc-2781-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 962-962; raw record sha256 88ee40ef3e431a870d14c4ede9de73c1aadb1f70cfe6a61ab04858049de5ced3
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: All 6 fields read, preserving literal blanks, source qualifiers and citation
    grain.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2781-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences frame: 0 positive placements with
    every retained field and negative predicate read.'
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/microansamycin-g.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "CYYOWCJHSDSDCW-JKSUJKDBSA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2781-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 positive placements with every retained
    field and negative predicate read.'
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
- evidence_id: bgc-2781-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 367-367; raw record sha256 bbdfac729b31aa29c300be53a084b58271efa209e5dfdc98a6ef7cb19e6e0d8b
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: All 7 fields read, preserving literal blanks, source qualifiers and citation
    grain.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2781-query-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay frame: 1 positive placements with every
    retained field and negative predicate read.'
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
- evidence_id: bgc-2781-row-pubchem_bioassay-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 947-947; raw record sha256 85e98f2ffa1ac5bb6f55fa19619cd5922c446ee27cb2ba25434960bcb157e311
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: supports
  summary: All 11 fields read, preserving literal blanks, source qualifiers and citation
    grain.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2781-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets frame: 0 positive placements with every
    retained field and negative predicate read.'
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/microansamycin-g.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "CYYOWCJHSDSDCW-JKSUJKDBSA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2781-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 positive placements with
    every retained field and negative predicate read.'
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/microansamycin-g.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "CYYOWCJHSDSDCW-JKSUJKDBSA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2781-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch279-tentative/bgc-prep/bgc-conditional279-source-inventory-DATA-001.json
  locator: /contexts/17/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: 'Complete saved chebi_origins frame: 0 positive placements with every retained
    field and negative predicate read.'
  snapshot_sha256: 6dcad711b5d9a8d5a5702657473afe19bf6d228a4a76cac4a533b20af2f3a6cf
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/microansamycin-g.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: bgc-2781-congener-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/microansamycin-i.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Shared-BGC context has a separate full key and source compound index. No
    molecular identity, biological grade, activity or congener-specific experiment
    transfers.
  snapshot_sha256: 2e29826a0be2421992edc189a02ffe18d70350e9cae84e44601d56f1c85ce144
- evidence_id: bgc-2781-congener-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-a.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Shared-BGC context has a separate full key and source compound index. No
    molecular identity, biological grade, activity or congener-specific experiment
    transfers.
  snapshot_sha256: d77f6424cfeffb9620f21ea630c35f432f2cce704070018b88b96d76507b747e
- evidence_id: bgc-2781-congener-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-b.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Shared-BGC context has a separate full key and source compound index. No
    molecular identity, biological grade, activity or congener-specific experiment
    transfers.
  snapshot_sha256: c228f90ea6413d575c30814edab2ab40525854cfbe9c772aad50e2a7e3d40b2e
- evidence_id: bgc-2781-congener-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-c.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Shared-BGC context has a separate full key and source compound index. No
    molecular identity, biological grade, activity or congener-specific experiment
    transfers.
  snapshot_sha256: a6ddda6a8d68e5495e9c60af8b923d90c9fc9529a2bb6ff6b3475de0df25f5f7
- evidence_id: bgc-2781-congener-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-d.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Shared-BGC context has a separate full key and source compound index. No
    molecular identity, biological grade, activity or congener-specific experiment
    transfers.
  snapshot_sha256: e85fd46b9d396a7623f818b10c6b12247a20cdda780fb7a9376a73ce1c894b87
- evidence_id: bgc-2781-congener-5
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-e.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Shared-BGC context has a separate full key and source compound index. No
    molecular identity, biological grade, activity or congener-specific experiment
    transfers.
  snapshot_sha256: 0b6989c4a5928ac95285003840eaf23299a23fbb34bbad029e66f9f57d551d3e
- evidence_id: bgc-2781-congener-6
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/polyketides/microansamycin-f.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Shared-BGC context has a separate full key and source compound index. No
    molecular identity, biological grade, activity or congener-specific experiment
    transfers.
  snapshot_sha256: e04fe8d1cc66a2d4b77f191a69d740d99b8639b50f9f0772a28263dec45d3c23
- evidence_id: bgc-2781-congener-7
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/microansamycin-h.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-06T23:12:47.918504Z'
  support: context_only
  summary: Shared-BGC context has a separate full key and source compound index. No
    molecular identity, biological grade, activity or congener-specific experiment
    transfers.
  snapshot_sha256: c1e318e58620b9c3a8b5b2cd228dc32186e6a48822e23d57033a9009406ccedd
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-279/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json
  accessed_at: '2026-11-06T22:49:33.617178Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 8308433a377991dfadc0d4d7c27597f30359e4eebfeb69905f656033a6cd5d24
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-279/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json
  accessed_at: '2026-11-06T22:49:58.336243Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 548e62d3df6bcd986c517cf5074a61bb6587897d5b6010cb0b88967001e11659
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-279/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json
  accessed_at: '2026-11-06T22:50:17.857028Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-279/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json
  accessed_at: '2026-11-06T22:50:51.594218Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-279/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-279/native-current279-five-gates-execution-001.json
  accessed_at: '2026-11-06T22:51:03.290430Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 946aa09f038631dc68e741aa6b4fefa1d4f52995677f8f38e6078889449090fc
assessments:
- assessment_id: bgc-2781-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: microansamycin G retains exact owner naturalproductmech:mibig-216120fec9,
    complete key CYYOWCJHSDSDCW-JKSUJKDBSA-N, and MIBiG BGC0001666 v3 compound index
    7. Its retained cross-references (npatlas:NPA023915, pubchem:139591130) are source-attributed,
    not remotely adjudicated. Both original forms normalize to C18H23NO6 and the full
    declared key. Distinct shared-BGC companions remain separate by their complete
    keys and source compound indices; no identity or experimental transfer follows.
  target_ids:
  - naturalproductmech:mibig-216120fec9
  evidence_ids:
  - bgc-2781-identity
  - bgc-2781-chemistry
  - bgc-2781-query-mibig_compounds
  - bgc-2781-plan
  - bgc-2781-row-mibig_compounds-0
  - bgc-2781-congener-0
  - bgc-2781-congener-1
  - bgc-2781-congener-2
  - bgc-2781-congener-3
  - bgc-2781-congener-4
  - bgc-2781-congener-5
  - bgc-2781-congener-6
  - bgc-2781-congener-7
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    value: CYYOWCJHSDSDCW-JKSUJKDBSA-N
    evidence_ids:
    - bgc-2781-identity
    - bgc-2781-chemistry
    - bgc-2781-query-mibig_compounds
    - bgc-2781-plan
    - bgc-2781-row-mibig_compounds-0
    - bgc-2781-congener-0
    - bgc-2781-congener-1
    - bgc-2781-congener-2
    - bgc-2781-congener-3
    - bgc-2781-congener-4
    - bgc-2781-congener-5
    - bgc-2781-congener-6
    - bgc-2781-congener-7
  - name: grounding_scope
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    value: microansamycin G retains exact owner naturalproductmech:mibig-216120fec9,
      complete key CYYOWCJHSDSDCW-JKSUJKDBSA-N, and MIBiG BGC0001666 v3 compound index
      7. Its retained cross-references (npatlas:NPA023915, pubchem:139591130) are
      source-attributed, not remotely adjudicated. Both original forms normalize to
      C18H23NO6 and the full declared key. Distinct shared-BGC companions remain separate
      by their complete keys and source compound indices; no identity or experimental
      transfer follows.
    evidence_ids:
    - bgc-2781-identity
    - bgc-2781-chemistry
    - bgc-2781-query-mibig_compounds
    - bgc-2781-plan
    - bgc-2781-row-mibig_compounds-0
    - bgc-2781-congener-0
    - bgc-2781-congener-1
    - bgc-2781-congener-2
    - bgc-2781-congener-3
    - bgc-2781-congener-4
    - bgc-2781-congener-5
    - bgc-2781-congener-6
    - bgc-2781-congener-7
- assessment_id: bgc-2781-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: The two saved forms each contain 25 atoms and 26 bonds. A seven-membered
    oxygen heterocycle is fused to an aromatic six-ring. In the stored SMILES graph,
    ketone C2=O3 and glycolamide N18-C19(=O20)-C21-O22H are separate; phenolic O17H,
    ring alcohol O23H and the C6-O12-C11 ether are explicit. No strict ester motif
    is present. This supports the encoded oxygenated cyclic scaffold without inferring
    a macrolactam or congener-specific biosynthesis. The SMILES table specifies C6
    R and C7 S, while C4=C5 has unspecified geometry. The InChI form retains two specified
    tetrahedral centres plus that unspecified alkene and an additional unspecified
    imidic C=N potential. The stored stereo_complete:true flag follows the extractor
    atom-centred rule; it does not certify all double-bond geometry or natural absolute
    stereochemistry. The glycolamide C19(=O20)-N18 is represented as a terminal C(OH)=N
    site in the InChI-derived graph; the separate ketone remains. Strict amide counts
    change from one to zero and carbonyl counts from two to one. The original forms
    agree in formula, aggregate charge, atom/bond counts, normalized Standard InChI
    and full key, but both canonical SMILES comparisons are false and the one-way
    atom map is empty. All full-graph identity flags are false. Mobile-hydrogen normalization
    explains a bounded representation difference; it does not certify exact tautomeric
    or natural identity and is not by itself a record defect.
  target_ids:
  - naturalproductmech:mibig-216120fec9
  evidence_ids:
  - bgc-2781-identity
  - bgc-2781-chemistry
  - bgc-2781-molecular-reading
  - bgc-2781-diagnostic-acceptance
  - bgc-2781-diagnostic-stderr
  - bgc-2781-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    value: The SMILES table specifies C6 R and C7 S, while C4=C5 has unspecified geometry.
      The InChI form retains two specified tetrahedral centres plus that unspecified
      alkene and an additional unspecified imidic C=N potential. The stored stereo_complete:true
      flag follows the extractor atom-centred rule; it does not certify all double-bond
      geometry or natural absolute stereochemistry.
    evidence_ids:
    - bgc-2781-identity
    - bgc-2781-chemistry
    - bgc-2781-molecular-reading
    - bgc-2781-diagnostic-acceptance
    - bgc-2781-diagnostic-stderr
    - bgc-2781-stereo-policy
  - name: representation_correspondence
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    value: The glycolamide C19(=O20)-N18 is represented as a terminal C(OH)=N site
      in the InChI-derived graph; the separate ketone remains. Strict amide counts
      change from one to zero and carbonyl counts from two to one. The original forms
      agree in formula, aggregate charge, atom/bond counts, normalized Standard InChI
      and full key, but both canonical SMILES comparisons are false and the one-way
      atom map is empty. All full-graph identity flags are false. Mobile-hydrogen
      normalization explains a bounded representation difference; it does not certify
      exact tautomeric or natural identity and is not by itself a record defect.
    evidence_ids:
    - bgc-2781-identity
    - bgc-2781-chemistry
    - bgc-2781-molecular-reading
    - bgc-2781-diagnostic-acceptance
    - bgc-2781-diagnostic-stderr
    - bgc-2781-stereo-policy
- assessment_id: bgc-2781-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: Micromonospora sp. HK160111 (NCBITaxon:1245497) remains the MIBiG SOURCE_ASSERTION
    producer. The separate genus-labelled Micromonospora occurrence (1873) does not
    demonstrate strain production. Cached names supply no independent rank, lineage
    or strain confirmation. BGC0001666 v3 is retained as active with questionable
    quality and unknown completeness. MG018799.1 has no retained coordinates or locus
    method, so CLUSTER_UNSTATED is preserved. COMPOUND_EVIDENCE citation grain improves
    attribution to this source compound but is not new primary verification or a knockout
    demonstration.
  target_ids:
  - naturalproductmech:mibig-216120fec9
  evidence_ids:
  - bgc-2781-provenance
  - bgc-2781-query-mibig_compounds
  - bgc-2781-taxonomy
  - bgc-2781-curation
  - bgc-2781-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    value: Micromonospora sp. HK160111 (NCBITaxon:1245497) remains the MIBiG SOURCE_ASSERTION
      producer. The separate genus-labelled Micromonospora occurrence (1873) does
      not demonstrate strain production. Cached names supply no independent rank,
      lineage or strain confirmation.
    evidence_ids:
    - bgc-2781-provenance
    - bgc-2781-query-mibig_compounds
    - bgc-2781-taxonomy
    - bgc-2781-curation
    - bgc-2781-row-mibig_compounds-0
  - name: producer_evidence
    definition: Producer evidence grade and its demonstrated or asserted scope.
    value: Micromonospora sp. HK160111 (NCBITaxon:1245497) remains the MIBiG SOURCE_ASSERTION
      producer. The separate genus-labelled Micromonospora occurrence (1873) does
      not demonstrate strain production. Cached names supply no independent rank,
      lineage or strain confirmation.
    evidence_ids:
    - bgc-2781-provenance
    - bgc-2781-query-mibig_compounds
    - bgc-2781-taxonomy
    - bgc-2781-curation
    - bgc-2781-row-mibig_compounds-0
  - name: locus_evidence
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    value: BGC0001666 v3 is retained as active with questionable quality and unknown
      completeness. MG018799.1 has no retained coordinates or locus method, so CLUSTER_UNSTATED
      is preserved. COMPOUND_EVIDENCE citation grain improves attribution to this
      source compound but is not new primary verification or a knockout demonstration.
    evidence_ids:
    - bgc-2781-provenance
    - bgc-2781-query-mibig_compounds
    - bgc-2781-taxonomy
    - bgc-2781-curation
    - bgc-2781-row-mibig_compounds-0
- assessment_id: bgc-2781-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: PMID:29412682 retains MIBiG COMPOUND_EVIDENCE citation grain. LOTUS DOI
    strings stay attached to their occurrence tuples; distinct databases or citation
    placements do not establish independent experiments. Underlying primary claims
    were not newly verified. Both of the 2 history events are SEEDED_FROM_SOURCES
    and seeder-attributed.
  target_ids:
  - naturalproductmech:mibig-216120fec9
  evidence_ids:
  - bgc-2781-history
  - bgc-2781-source-reading
  - bgc-2781-query-mibig_compounds
  - bgc-2781-row-mibig_compounds-0
  - bgc-2781-row-lotus_occurrences-0
  dimensions:
  - name: citation_scope
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    value: PMID:29412682 retains MIBiG COMPOUND_EVIDENCE citation grain. LOTUS DOI
      strings stay attached to their occurrence tuples; distinct databases or citation
      placements do not establish independent experiments. Underlying primary claims
      were not newly verified. Both of the 2 history events are SEEDED_FROM_SOURCES
      and seeder-attributed.
    evidence_ids:
    - bgc-2781-history
    - bgc-2781-source-reading
    - bgc-2781-query-mibig_compounds
    - bgc-2781-row-mibig_compounds-0
    - bgc-2781-row-lotus_occurrences-0
- assessment_id: bgc-2781-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: The one LOTUS tuple attributes this full key to Micromonospora (1873) with
    DOI:10.1021/ACS.ORGLETT.7B04018. It remains an occurrence assertion, separate
    from the HK160111 producer and not an independent primary experiment. One retained
    PubChem BioAssay row has an empty AID and no assay result; it is a blank sentinel,
    not a measured activity or target. No actual AID or measured target is captured.
    ChEBI structures/origins, CyanoMetDB, BindingDB and AntibioticMech queries are
    bounded negatives. These do not establish global absence, inactivity, potency
    or mechanism.
  target_ids:
  - naturalproductmech:mibig-216120fec9
  evidence_ids:
  - bgc-2781-roots
  - bgc-2781-query-lotus_occurrences
  - bgc-2781-query-chebi_origins
  - bgc-2781-query-cyanometdb_occurrences
  - bgc-2781-query-pubchem_bioassay
  - bgc-2781-query-bindingdb_targets
  - bgc-2781-query-antibioticmech_inchikeys
  - bgc-2781-assay-curation
  - bgc-2781-row-lotus_occurrences-0
  - bgc-2781-row-pubchem_bioassay-0
  dimensions:
  - name: occurrence_scope
    definition: Exact retained occurrence tuples and limits on production/independence.
    value: The one LOTUS tuple attributes this full key to Micromonospora (1873) with
      DOI:10.1021/ACS.ORGLETT.7B04018. It remains an occurrence assertion, separate
      from the HK160111 producer and not an independent primary experiment.
    evidence_ids:
    - bgc-2781-roots
    - bgc-2781-query-lotus_occurrences
    - bgc-2781-query-chebi_origins
    - bgc-2781-query-cyanometdb_occurrences
    - bgc-2781-query-pubchem_bioassay
    - bgc-2781-query-bindingdb_targets
    - bgc-2781-query-antibioticmech_inchikeys
    - bgc-2781-assay-curation
    - bgc-2781-row-lotus_occurrences-0
    - bgc-2781-row-pubchem_bioassay-0
  - name: assay_target_scope
    definition: Retained activity/assay/target positives and bounded negative queries.
    value: One retained PubChem BioAssay row has an empty AID and no assay result;
      it is a blank sentinel, not a measured activity or target. No actual AID or
      measured target is captured. ChEBI structures/origins, CyanoMetDB, BindingDB
      and AntibioticMech queries are bounded negatives. These do not establish global
      absence, inactivity, potency or mechanism.
    evidence_ids:
    - bgc-2781-roots
    - bgc-2781-query-lotus_occurrences
    - bgc-2781-query-chebi_origins
    - bgc-2781-query-cyanometdb_occurrences
    - bgc-2781-query-pubchem_bioassay
    - bgc-2781-query-bindingdb_targets
    - bgc-2781-query-antibioticmech_inchikeys
    - bgc-2781-assay-curation
    - bgc-2781-row-lotus_occurrences-0
    - bgc-2781-row-pubchem_bioassay-0
- assessment_id: bgc-2781-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: UNCLASSIFIED follows the empty NPClassifier pathway array; its superclass/class
    arrays are also empty and is_glycoside is false. Source Cyclic polyketide/Polycyclic
    polyketide and PKS labels remain source assertions rather than classifier outputs.
    The saved two-ring topology is structurally compatible, but does not verify a
    biosynthetic pathway.
  target_ids:
  - naturalproductmech:mibig-216120fec9
  evidence_ids:
  - bgc-2781-classification
  - bgc-2781-chemistry
  - bgc-2781-query-npclassifier
  - bgc-2781-query-mibig_compounds
  - bgc-2781-filing-policy
  - bgc-2781-row-npclassifier-0
  dimensions:
  - name: classification_applicability
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    value: UNCLASSIFIED follows the empty NPClassifier pathway array; its superclass/class
      arrays are also empty and is_glycoside is false. Source Cyclic polyketide/Polycyclic
      polyketide and PKS labels remain source assertions rather than classifier outputs.
      The saved two-ring topology is structurally compatible, but does not verify
      a biosynthetic pathway.
    evidence_ids:
    - bgc-2781-classification
    - bgc-2781-chemistry
    - bgc-2781-query-npclassifier
    - bgc-2781-query-mibig_compounds
    - bgc-2781-filing-policy
    - bgc-2781-row-npclassifier-0
- assessment_id: bgc-2781-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: unknown
  summary: Whole current owner and its 2 seeder histories, all nine saved source frames
    (4 positive placements/49 fields and 5 negatives), and both complete original
    molecular tables were read. All 52 actual input hashes and maintained ownership
    declarations were joined; this is not a claim to have substantively read every
    entire input corpus. Five original local gates passed. Full QC/OAK, live source-authority
    checks and independent primary confirmation remain unavailable, so completion
    is partial. No literal graph/pathway/component/target root requires a maintained
    reader. Any later correction belongs in maintained inputs, applicable curation,
    extractors or the seeder.
  target_ids:
  - naturalproductmech:mibig-216120fec9
  evidence_ids:
  - bgc-2781-owner
  - bgc-2781-history
  - bgc-2781-intake
  - bgc-2781-intake-acceptance
  - bgc-2781-plan
  - bgc-2781-plan-acceptance
  - bgc-2781-gates
  - bgc-2781-source-reading
  - bgc-2781-source-notes
  - bgc-2781-molecular-reading
  - bgc-2781-roots
  dimensions:
  - name: review_completion
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    value: Whole current owner and its 2 seeder histories, all nine saved source frames
      (4 positive placements/49 fields and 5 negatives), and both complete original
      molecular tables were read. All 52 actual input hashes and maintained ownership
      declarations were joined; this is not a claim to have substantively read every
      entire input corpus. Five original local gates passed. Full QC/OAK, live source-authority
      checks and independent primary confirmation remain unavailable, so completion
      is partial. No literal graph/pathway/component/target root requires a maintained
      reader. Any later correction belongs in maintained inputs, applicable curation,
      extractors or the seeder.
    evidence_ids:
    - bgc-2781-owner
    - bgc-2781-history
    - bgc-2781-intake
    - bgc-2781-intake-acceptance
    - bgc-2781-plan
    - bgc-2781-plan-acceptance
    - bgc-2781-gates
    - bgc-2781-source-reading
    - bgc-2781-source-notes
    - bgc-2781-molecular-reading
    - bgc-2781-roots
findings: []
actions: []
limitations:
- External authority, primary publications, sequence-level and strain-level confirmation
  were not newly obtained. Full QC/OAK are unavailable; source assertions and source-level
  experimental grades remain attributed.
- The glycolamide C19(=O20)-N18 is represented as a terminal C(OH)=N site in the InChI-derived
  graph; the separate ketone remains. Strict amide counts change from one to zero
  and carbonyl counts from two to one. The original forms agree in formula, aggregate
  charge, atom/bond counts, normalized Standard InChI and full key, but both canonical
  SMILES comparisons are false and the one-way atom map is empty. All full-graph identity
  flags are false. Mobile-hydrogen normalization explains a bounded representation
  difference; it does not certify exact tautomeric or natural identity and is not
  by itself a record defect. The six original undefined-stereo warnings remain globally
  unassigned.
- The SMILES table specifies C6 R and C7 S, while C4=C5 has unspecified geometry.
  The InChI form retains two specified tetrahedral centres plus that unspecified alkene
  and an additional unspecified imidic C=N potential. The stored stereo_complete:true
  flag follows the extractor atom-centred rule; it does not certify all double-bond
  geometry or natural absolute stereochemistry.
- Saved topology supports the encoded scaffold only; it does not independently establish
  every natural residue, reaction, pharmacological mechanism or biosynthetic pathway.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- This review concerns one exact captured target and its declared input scope. No
  record, native scientific status, source table or curation history is edited.
- Only retained original evidence was interpreted. This author performed no molecular
  parse, target execution, source-query replay or outbound request.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-279
```
