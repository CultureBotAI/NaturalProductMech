# Local evidence review: myxofacycline D

- Review: 20261107T021905Z-myxofacycline-d
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T01:29:28.070468Z
- Finished UTC: 2026-11-07T02:19:05.206392Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Myxofacycline D retains its own C15H25NO4 full key, a saved aromatic N–O five-ring, a branched hydroxyalkyl substituent and a carboxylic acid. Both stored forms give equal canonical strings and a complete limited 20-atom map, but the hydroxy-bearing stereocentre remains unspecified and full graph/natural identity is not certified. BGC0002342 carries characterized producer and demonstrated locus grades for Myxococcus xanthus; the Streptomyces prunicolor occurrence is a separate claim. Empty classifier arrays and unknown source-entry completeness remain explicit. No congener identity or experimental support is transferred from the six direct companions.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2804; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-75d7a33032 | data/natural_products/unclassified/myxofacycline-d.yaml | generated | myxofacycline D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-75d7a33032 | Both exact stored forms parsed in the original twenty-attempt diagnostic and agree in formula, charge, normalized Standard InChI and complete key. |
| strict_ten | passed | True | naturalproductmech:mibig-75d7a33032 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-75d7a33032 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-75d7a33032 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-75d7a33032 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-75d7a33032 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-75d7a33032 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-75d7a33032 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-75d7a33032 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: naturalproductmech:mibig-75d7a33032.

myxofacycline D retains exact identifier naturalproductmech:mibig-75d7a33032, complete key AYZBMLHVFCLOSX-UHFFFAOYSA-N, and source rows BGC0002342 v3 compound index 2. Cross-references npatlas:NPA033231 remain attributed identifiers, not fresh authority confirmation. Both saved forms normalize to C15H25NO4 and the declared full key. Distinct source compounds and direct companions retain their own full keys; no identity, experimental grade or stereochemistry is transferred.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-75d7a33032.

The saved neutral connected C15H25NO4 graph has 20 atoms and 20 bonds. One aromatic five-ring contains adjacent N18/O19 and three carbons, supporting an isoxazole-like structural description; the retained computation represents the literal Kekule input aromatically. A branched alkyl chain bears OH at C7–O8, and C15(=O16)–O17H is a carboxylic acid. The motif table has no strict amide or ester, and this N–O ring is not a C5O sugar ring. Aromatic normalization is not by itself a record defect or proof of biosynthetic origin. The OH-bearing atom is an unspecified tetrahedral centre (SMILES C7, corresponding InChI C12), consistent with the source stereo_complete:false flag and the key without an assigned stereo layer. Canonical agreement and complete limited atom mapping preserve this unknown; they cannot assign a natural enantiomer or resolve stereochemistry by comparison with another myxofacycline. Both stored forms parsed; all ten recorded comparisons, including both canonical SMILES comparisons, are true, and the limited 20-atom correspondence is complete. The diagnostic still reports full_graph_identity_established:false. This bounded agreement supports consistent local representation while leaving the unspecified centre and experimental natural identity unresolved; no additional cleanup or parse was performed.

### Producer assertion versus locus evidence

provenance: supported. Targets: naturalproductmech:mibig-75d7a33032.

The BGC0002342 producer is Myxococcus xanthus (NCBITaxon:34), with source BGC_CHARACTERIZED grade and knockout/heterologous-expression methods. Streptomyces prunicolor (NCBITaxon:67348) belongs to the separate LOTUS occurrence route. Neither cached naming nor that occurrence is used to replace or strengthen the retained producer assertion. BGC0002342 v3 retains MT513750.1:8235–29793, NRPS&#124;PKS with Type I&#124;Unknown subclass, CLUSTER_DEMONSTRATED and knockout/heterologous-expression methods. It is active and quality questionable, but completeness is explicitly unknown. Its blank compound-class field and ENTRY-grain PMID:34617331 are preserved; the six other myxofacyclines sharing this entry keep distinct full keys and source stereo flags.

### Citation grain and attributed history

evidence: supported. Targets: naturalproductmech:mibig-75d7a33032.

BGC0002342: PMID:34617331 at ENTRY grain. These are attributed database citations, not newly examined primary bodies. DOI case variants and repeated placements do not create independent evidence. All 2 histories were read: 2 are seeder-attributed SEEDED_FROM_SOURCES events.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: naturalproductmech:mibig-75d7a33032.

The LOTUS occurrence is Streptomyces prunicolor (NCBITaxon:67348), DOI:10.1002/CHEM.202103095. It remains separate from the Myxococcus xanthus producer claim and from all other myxofacycline keys, even though the companions share the same retained occurrence citation. The saved PubChem BioAssay frame has no row or blank sentinel for this owner. No actual AID or molecular target is captured. ChEBI structure/origin, CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not global absence, inactivity, potency or target-mechanism proof.

### Computed filing and asserted class applicability

consistency: supported. Targets: naturalproductmech:mibig-75d7a33032.

All three NPClassifier result arrays are empty, with is_glycoside:false; the maintained zero-result rule leaves UNCLASSIFIED. The saved graph has no sugar-like C5O ring, but the false model flag is not an independent natural glycosylation experiment. Source NRPS&#124;PKS is retained separately and does not fill an absent classifier result or imply a peptide ring.

### Local completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-75d7a33032.

The complete current owner is carried from ROOT’s attributed whole-owner reading and exact current raw/capture equality. All 2 histories, nine saved source frames (3 positive placements/38 fields and 6 negatives), and both complete saved molecular forms were personally read. All 50 actual input hashes and maintained ownership paths join the accepted plan. Input pinning is not a claim to have substantively read every entire corpus. Five original local gates passed. The complete owner root set has no positive graph, pathway, component or molecular-target root, so no maintained reader applies. Full QC/OAK, fresh source-authority checks and independent primary confirmation remain unavailable; completion is partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2804-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/myxofacycline-d.yaml; Complete plaintext, every root and all curation_history entries | supports | Complete current owner carried from ROOT’s attributed whole reading and joined exactly to capture; current source/history meanings were personally read. |
| bgc-2804-whole-owner-attribution | /private/tmp/npm-review-work/shared-next-batch281-tentative/root-conditional281-whole-owner-reading-001.json; /records | context_only | ROOT’s complete selected-owner reading is carried through exact current raw/capture equality; it is not additional BGC personal whole-owner credit. |
| bgc-2804-identity | /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json; /records/3/owner_document/identifier; /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status | supports | myxofacycline D retains exact identifier naturalproductmech:mibig-75d7a33032, complete key AYZBMLHVFCLOSX-UHFFFAOYSA-N, and source rows BGC0002342 v3 compound index 2. Cross-references npatlas:NPA033231 remain attributed identifiers, not fresh authority confirmation. Both saved forms normalize to C15H25NO4 and the declared full key. Distinct source compounds and direct companions retain their own full keys; no identity, experimental grade or stereochemistry is transferred. |
| bgc-2804-history | /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json; /records/3/owner_document/curation_history | supports | BGC0002342: PMID:34617331 at ENTRY grain. These are attributed database citations, not newly examined primary bodies. DOI case variants and repeated placements do not create independent evidence. All 2 histories were read: 2 are seeder-attributed SEEDED_FROM_SOURCES events. |
| bgc-2804-provenance | /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters | supports | The BGC0002342 producer is Myxococcus xanthus (NCBITaxon:34), with source BGC_CHARACTERIZED grade and knockout/heterologous-expression methods. Streptomyces prunicolor (NCBITaxon:67348) belongs to the separate LOTUS occurrence route. Neither cached naming nor that occurrence is used to replace or strengthen the retained producer assertion. BGC0002342 v3 retains MT513750.1:8235–29793, NRPS&#124;PKS with Type I&#124;Unknown subclass, CLUSTER_DEMONSTRATED and knockout/heterologous-expression methods. It is active and quality questionable, but completeness is explicitly unknown. Its blank compound-class field and ENTRY-grain PMID:34617331 are preserved; the six other myxofacyclines sharing this entry keep distinct full keys and source stereo flags. |
| bgc-2804-classification | /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json; /records/3/owner_document/np_classification; /records/3/owner_document/np_pathway; /records/3/owner_document/bgc_class | supports | All three NPClassifier result arrays are empty, with is_glycoside:false; the maintained zero-result rule leaves UNCLASSIFIED. The saved graph has no sugar-like C5O ring, but the false model flag is not an independent natural glycosylation experiment. Source NRPS&#124;PKS is retained separately and does not fill an absent classifier result or imply a peptide ring. |
| bgc-2804-roots | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/19/complete_root_keys; /contexts/19/declared_mechanism_roots_literal; /contexts/19/literal_bioactivities_root | context_only | The complete owner root set has no positive graph, pathway, component or molecular-target root, so no maintained reader applies. |
| bgc-2804-chemistry | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons; /records/3/atom_correspondence | supports | The saved neutral connected C15H25NO4 graph has 20 atoms and 20 bonds. One aromatic five-ring contains adjacent N18/O19 and three carbons, supporting an isoxazole-like structural description; the retained computation represents the literal Kekule input aromatically. A branched alkyl chain bears OH at C7–O8, and C15(=O16)–O17H is a carboxylic acid. The motif table has no strict amide or ester, and this N–O ring is not a C5O sugar ring. Aromatic normalization is not by itself a record defect or proof of biosynthetic origin. The OH-bearing atom is an unspecified tetrahedral centre (SMILES C7, corresponding InChI C12), consistent with the source stereo_complete:false flag and the key without an assigned stereo layer. Canonical agreement and complete limited atom mapping preserve this unknown; they cannot assign a natural enantiomer or resolve stereochemistry by comparison with another myxofacycline. Both stored forms parsed; all ten recorded comparisons, including both canonical SMILES comparisons, are true, and the limited 20-atom correspondence is complete. The diagnostic still reports full_graph_identity_established:false. This bounded agreement supports consistent local representation while leaving the unspecified centre and experimental natural identity unresolved; no additional cleanup or parse was performed. |
| bgc-2804-molecular-reading | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-current281-first-five-molecular-intake-reading-001.json; /records/3; /personal_reading_scope; /global_cautions | supports | Complete saved tables personally read and interpreted without a new parse. |
| bgc-2804-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/root-current281-diagnostic-acceptance-001.json; /status; /accepted; /diagnostic; /molecular_parse_attempts; /limits | supports | ROOT accepted the original twenty stored-form attempts; exact representation and identity limits remain. |
| bgc-2804-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-execution-001.json; /command; /exit_code | supports | Original ROOT diagnostic command and exit zero; no replay. |
| bgc-2804-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-original-001.stderr; Complete original stderr including blank separators | context_only | Four undefined-stereo warnings remain globally unassigned; no message is attributed to this owner. |
| bgc-2804-intake | /private/tmp/npm-review-work/shared-next-batch281/intakes-001/2804-inspect-001.json; /targets; /source/inputs | supports | One exact target, 50 current inputs and explicit maintained ownership paths. |
| bgc-2804-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch281/root-current281-intake-acceptance-001.json; /accepted; /intake_summary; /records; /source_placements; /unique_source_paths | supports | All ten original inspections exited zero with empty stderr and 470 placements/71 paths. |
| bgc-2804-plan | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-target-input-plan-001.json; /records/3 | supports | Exact current input map, 6 direct companions and the literal reader applicability. |
| bgc-2804-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch281/root-current281-input-plan-acceptance-001.json; /accepted; /input_plan; /source_placements; /unique_source_paths | supports | ROOT accepted the current source input plan. |
| bgc-2804-gates | /private/tmp/npm-review-work/shared-next-batch281/root-current281-five-gates-acceptance-001.json; /records; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows | context_only | Five local gates passed; queue rows are review leads, not findings. Full QC/OAK remain unavailable. |
| bgc-2804-source-reading | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-current281-assigned-source-reading-001.json; /contexts/9; /counts; /reading_attribution | supports | All 3 complete positive dictionaries/38 fields and 6 bounded negative frames were personally read in the attributed source pass. |
| bgc-2804-source-notes | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-scope-notes-001.json; /totals; /reading_reconciliation; /reading_boundaries | context_only | The original 113 source placements/1,389 fields retain BGC 38 and Support 75 primary-row attribution; Native and ROOT have zero primary-row credit. |
| bgc-2804-taxonomy | /private/tmp/npm-review-work/shared-next-batch281-tentative/native-prep/native-current281-cached-taxonomy-reading-001.json; /scope; /context_interpretations/19; /interpretation | context_only | The BGC0002342 producer is Myxococcus xanthus (NCBITaxon:34), with source BGC_CHARACTERIZED grade and knockout/heterologous-expression methods. Streptomyces prunicolor (NCBITaxon:67348) belongs to the separate LOTUS occurrence route. Neither cached naming nor that occurrence is used to replace or strengthen the retained producer assertion. Cached names do not independently supply rank, lineage or strain-level evidence. |
| bgc-2804-curation | /private/tmp/npm-review-work/shared-next-batch281-tentative/native-prep/native-current281-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation | context_only | Nine substantive tables/3,422 rows were scanned by Native; 10 lexical candidates yield zero exact applicable decisions. Two reserved census-only tables are excluded. |
| bgc-2804-assay-curation | /private/tmp/npm-review-work/shared-next-batch281-tentative/native-prep/native-current281-implemented-curation-scan-001.json; /assay_scope | context_only | The saved PubChem BioAssay frame has no row or blank sentinel for this owner. No actual AID or molecular target is captured. ChEBI structure/origin, CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not global absence, inactivity, potency or target-mechanism proof. |
| bgc-2804-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters(includeUnassigned=True) | context_only | The source stereo_complete flag tests unassigned atom-centred chirality, not all double-bond geometry or natural identity. |
| bgc-2804-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306: choose_pathway | context_only | Exactly one supported mapped pathway selects filing; zero, unsupported single or multiple labels retain UNCLASSIFIED. |
| bgc-2804-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 positive placements, with all fields and bounded query meanings read. |
| bgc-2804-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 2854-2854; raw record sha256 41ca0947d1d176097f6cc150a29e06bec69cd5a16a9b8cdfcd994d4e44e9faae | supports | All 25 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2804-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2804-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 1 positive placements, with all fields and bounded query meanings read. |
| bgc-2804-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 419-419; raw record sha256 1589c1855c0ef80be754b1d399b6a699e59c7f5cd2c906e924ef0aadb7184220 | supports | All 6 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2804-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2804-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 positive placements, with all fields and bounded query meanings read. |
| bgc-2804-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 128-128; raw record sha256 fd817e40b719b0681fc5184bc19edbbe821674aac38ff4f4c12579edbbc78ffa | supports | All 7 fields read, preserving blanks, evidence grades, source identity and citation grain. |
| bgc-2804-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/pubchem_bioassay | context_only | Complete saved pubchem_bioassay frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2804-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2804-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2804-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins frame: 0 positive placements, with all fields and bounded query meanings read. |
| bgc-2804-congener-0 | /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/myxofacycline-e.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2804-congener-1 | /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/myxofacycline-f.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2804-congener-2 | /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/myxofacycline-g.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2804-congener-3 | /private/tmp/npm-record-reviews-20261021/data/natural_products/fatty_acids/myxofacycline-a.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2804-congener-4 | /private/tmp/npm-record-reviews-20261021/data/natural_products/fatty_acids/myxofacycline-b.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| bgc-2804-congener-5 | /private/tmp/npm-record-reviews-20261021/data/natural_products/fatty_acids/myxofacycline-c.yaml; Complete current owner identity/source concepts and attributed history | context_only | Direct shared-BGC context retains a distinct complete key. No molecular, stereochemical, activity or experimental-grade transfer follows. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-281/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-281/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-281/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-281/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-281/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Fresh source-authority, primary publication, sequence and strain verification remain unavailable. Full QC/OAK were not run; retained experimental grades stay source-attributed.
- Both stored forms parsed; all ten recorded comparisons, including both canonical SMILES comparisons, are true, and the limited 20-atom correspondence is complete. The diagnostic still reports full_graph_identity_established:false. This bounded agreement supports consistent local representation while leaving the unspecified centre and experimental natural identity unresolved; no additional cleanup or parse was performed. Four undefined-stereo warnings remain globally unassigned; no message is attributed to this owner.
- The OH-bearing atom is an unspecified tetrahedral centre (SMILES C7, corresponding InChI C12), consistent with the source stereo_complete:false flag and the key without an assigned stereo layer. Canonical agreement and complete limited atom mapping preserve this unknown; they cannot assign a natural enantiomer or resolve stereochemistry by comparison with another myxofacycline.
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
review_id: 20261107T021905Z-myxofacycline-d
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: myxofacycline D'
started_at: '2026-11-07T01:29:28.070468Z'
finished_at: '2026-11-07T02:19:05.206392Z'
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
summary: Myxofacycline D retains its own C15H25NO4 full key, a saved aromatic N–O
  five-ring, a branched hydroxyalkyl substituent and a carboxylic acid. Both stored
  forms give equal canonical strings and a complete limited 20-atom map, but the hydroxy-bearing
  stereocentre remains unspecified and full graph/natural identity is not certified.
  BGC0002342 carries characterized producer and demonstrated locus grades for Myxococcus
  xanthus; the Streptomyces prunicolor occurrence is a separate claim. Empty classifier
  arrays and unknown source-entry completeness remain explicit. No congener identity
  or experimental support is transferred from the six direct companions.
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
  - path: data/natural_products/alkaloids/myxofacycline-e.yaml
    sha256: 217af40d7f6cdd5fce6c715f301ea53722f984d736a3d07aab4fb03e3b6ad965
    role: context
  - path: data/natural_products/alkaloids/myxofacycline-f.yaml
    sha256: b883a268156852475a3290c9e411c02ea61f0b350edf5dfb703b82caa28fb689
    role: context
  - path: data/natural_products/alkaloids/myxofacycline-g.yaml
    sha256: 97805dfcd098cd821ed1a5ef68861472311ebcebc8967e60f1482c4dd6b9ee9a
    role: context
  - path: data/natural_products/fatty_acids/myxofacycline-a.yaml
    sha256: e542894641f17bad9dda44700cefd66dc1e479bc26e1d558097826029c304bee
    role: context
  - path: data/natural_products/fatty_acids/myxofacycline-b.yaml
    sha256: 7c66ef4af142c17f99f47978976f000019c51928c06a22b743ec60fa29f466ed
    role: context
  - path: data/natural_products/fatty_acids/myxofacycline-c.yaml
    sha256: 8c2342b1bf3f0e282ae3d41d197b800dce7834fa5287be4cf536406ba12c865a
    role: context
  - path: data/natural_products/unclassified/myxofacycline-d.yaml
    sha256: ae6d457479ba91d286dd6bf4ebaad1dec0a1ec4b04959da8f0f5236b73ddfaea
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
  selection: Campaign path order 2804; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-75d7a33032
targets:
- target_id: naturalproductmech:mibig-75d7a33032
  path: data/natural_products/unclassified/myxofacycline-d.yaml
  label: myxofacycline D
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnose281-001.py
    39d094b3fb91806d9fc15040748c5adfccb89cfc7a705122dc84ceec8346e971 dd20c76fb6a393cb3ddb8385f086f3cceb91cd099a75233730ca46241a9d680e
    f2b54906126f773c478253bc0fb9feb17399b2f2da565d486a024c578dbd71a1
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both exact stored forms parsed in the original twenty-attempt diagnostic
    and agree in formula, charge, normalized Standard InChI and complete key.
  scope_note: Both stored forms parsed; all ten recorded comparisons, including both
    canonical SMILES comparisons, are true, and the limited 20-atom correspondence
    is complete. The diagnostic still reports full_graph_identity_established:false.
    This bounded agreement supports consistent local representation while leaving
    the unspecified centre and experimental natural identity unresolved; no additional
    cleanup or parse was performed. Four undefined-stereo warnings remain globally
    unassigned; no message is attributed to this owner.
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  evidence_ids:
  - bgc-2804-chemistry
  - bgc-2804-diagnostic-acceptance
  - bgc-2804-diagnostic-execution
  - bgc-2804-diagnostic-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  command: just validate-strict data/natural_products/unclassified/myxochromide-d-2.yaml
    data/natural_products/unclassified/myxochromide-d.yaml data/natural_products/unclassified/myxochromide-s.yaml
    data/natural_products/unclassified/myxofacycline-d.yaml data/natural_products/unclassified/myxothiazol.yaml
    data/natural_products/unclassified/myxovirescin-a1.yaml data/natural_products/unclassified/n-coronafacoyl-l-isoleucine.yaml
    data/natural_products/unclassified/n-methylwelwitindolinone-c-isothiocyanate.yaml
    data/natural_products/unclassified/n-methylwelwitinsolinone-c-isonitrile.yaml
    data/natural_products/unclassified/n-tetradecanoyl-tyrosine.yaml --workers 1 --out
    /private/tmp/npm-native-checks/batch-281/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-75d7a33032
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-281/validate-all-001.tsv
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
  - naturalproductmech:mibig-75d7a33032
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
  - naturalproductmech:mibig-75d7a33032
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
  - naturalproductmech:mibig-75d7a33032
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-281/review-queue-001.tsv
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
  - naturalproductmech:mibig-75d7a33032
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2804-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/myxofacycline-d.yaml
  locator: Complete plaintext, every root and all curation_history entries
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: Complete current owner carried from ROOT’s attributed whole reading and
    joined exactly to capture; current source/history meanings were personally read.
  snapshot_sha256: ae6d457479ba91d286dd6bf4ebaad1dec0a1ec4b04959da8f0f5236b73ddfaea
- evidence_id: bgc-2804-whole-owner-attribution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/root-conditional281-whole-owner-reading-001.json
  locator: /records
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: ROOT’s complete selected-owner reading is carried through exact current
    raw/capture equality; it is not additional BGC personal whole-owner credit.
  snapshot_sha256: 609334358b44459307d2a0fcd143429feb04a2319014e6d3cb90f10b8cc2ede5
- evidence_id: bgc-2804-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json
  locator: /records/3/owner_document/identifier; /records/3/owner_document/chemical_structure;
    /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: myxofacycline D retains exact identifier naturalproductmech:mibig-75d7a33032,
    complete key AYZBMLHVFCLOSX-UHFFFAOYSA-N, and source rows BGC0002342 v3 compound
    index 2. Cross-references npatlas:NPA033231 remain attributed identifiers, not
    fresh authority confirmation. Both saved forms normalize to C15H25NO4 and the
    declared full key. Distinct source compounds and direct companions retain their
    own full keys; no identity, experimental grade or stereochemistry is transferred.
  snapshot_sha256: dd20c76fb6a393cb3ddb8385f086f3cceb91cd099a75233730ca46241a9d680e
- evidence_id: bgc-2804-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json
  locator: /records/3/owner_document/curation_history
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: 'BGC0002342: PMID:34617331 at ENTRY grain. These are attributed database
    citations, not newly examined primary bodies. DOI case variants and repeated placements
    do not create independent evidence. All 2 histories were read: 2 are seeder-attributed
    SEEDED_FROM_SOURCES events.'
  snapshot_sha256: dd20c76fb6a393cb3ddb8385f086f3cceb91cd099a75233730ca46241a9d680e
- evidence_id: bgc-2804-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: The BGC0002342 producer is Myxococcus xanthus (NCBITaxon:34), with source
    BGC_CHARACTERIZED grade and knockout/heterologous-expression methods. Streptomyces
    prunicolor (NCBITaxon:67348) belongs to the separate LOTUS occurrence route. Neither
    cached naming nor that occurrence is used to replace or strengthen the retained
    producer assertion. BGC0002342 v3 retains MT513750.1:8235–29793, NRPS|PKS with
    Type I|Unknown subclass, CLUSTER_DEMONSTRATED and knockout/heterologous-expression
    methods. It is active and quality questionable, but completeness is explicitly
    unknown. Its blank compound-class field and ENTRY-grain PMID:34617331 are preserved;
    the six other myxofacyclines sharing this entry keep distinct full keys and source
    stereo flags.
  snapshot_sha256: dd20c76fb6a393cb3ddb8385f086f3cceb91cd099a75233730ca46241a9d680e
- evidence_id: bgc-2804-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_classification; /records/3/owner_document/np_pathway;
    /records/3/owner_document/bgc_class
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: All three NPClassifier result arrays are empty, with is_glycoside:false;
    the maintained zero-result rule leaves UNCLASSIFIED. The saved graph has no sugar-like
    C5O ring, but the false model flag is not an independent natural glycosylation
    experiment. Source NRPS|PKS is retained separately and does not fill an absent
    classifier result or imply a peptide ring.
  snapshot_sha256: dd20c76fb6a393cb3ddb8385f086f3cceb91cd099a75233730ca46241a9d680e
- evidence_id: bgc-2804-roots
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/19/complete_root_keys; /contexts/19/declared_mechanism_roots_literal;
    /contexts/19/literal_bioactivities_root
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: The complete owner root set has no positive graph, pathway, component or
    molecular-target root, so no maintained reader applies.
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: Complete captured owner root set, not a biological absence claim.
- evidence_id: bgc-2804-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons;
    /records/3/atom_correspondence
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: The saved neutral connected C15H25NO4 graph has 20 atoms and 20 bonds.
    One aromatic five-ring contains adjacent N18/O19 and three carbons, supporting
    an isoxazole-like structural description; the retained computation represents
    the literal Kekule input aromatically. A branched alkyl chain bears OH at C7–O8,
    and C15(=O16)–O17H is a carboxylic acid. The motif table has no strict amide or
    ester, and this N–O ring is not a C5O sugar ring. Aromatic normalization is not
    by itself a record defect or proof of biosynthetic origin. The OH-bearing atom
    is an unspecified tetrahedral centre (SMILES C7, corresponding InChI C12), consistent
    with the source stereo_complete:false flag and the key without an assigned stereo
    layer. Canonical agreement and complete limited atom mapping preserve this unknown;
    they cannot assign a natural enantiomer or resolve stereochemistry by comparison
    with another myxofacycline. Both stored forms parsed; all ten recorded comparisons,
    including both canonical SMILES comparisons, are true, and the limited 20-atom
    correspondence is complete. The diagnostic still reports full_graph_identity_established:false.
    This bounded agreement supports consistent local representation while leaving
    the unspecified centre and experimental natural identity unresolved; no additional
    cleanup or parse was performed.
  snapshot_sha256: f9503e14398594b03f4d7d0fefbbc595cb6cfd4d81dc07b456a97f975be3f769
- evidence_id: bgc-2804-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-current281-first-five-molecular-intake-reading-001.json
  locator: /records/3; /personal_reading_scope; /global_cautions
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: Complete saved tables personally read and interpreted without a new parse.
  snapshot_sha256: f21989ba844fa5a9ab40ca2674b87a5fae6286f5001713ac78c2fb795b94f2ed
- evidence_id: bgc-2804-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/root-current281-diagnostic-acceptance-001.json
  locator: /status; /accepted; /diagnostic; /molecular_parse_attempts; /limits
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form attempts; exact representation
    and identity limits remain.
  snapshot_sha256: 59aa0376922e13348c35507038d8316ea84cec456b334ca658b5ef604695f996
- evidence_id: bgc-2804-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: Original ROOT diagnostic command and exit zero; no replay.
  snapshot_sha256: 71bbb4159caead14c60c52f68bc5fba6c7c01c202065c7d884060845dcc8dfbb
- evidence_id: bgc-2804-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr including blank separators
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: Four undefined-stereo warnings remain globally unassigned; no message is
    attributed to this owner.
  snapshot_sha256: 5d01f97b54087f4a5b02d5bfa8256e2c3dd0ef1eedd4f53b44b3f15175e371eb
- evidence_id: bgc-2804-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/intakes-001/2804-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: One exact target, 50 current inputs and explicit maintained ownership paths.
  snapshot_sha256: 523b8f7e4d6079a7407a6309396a5390d4257d60628516d95469471b463d287c
- evidence_id: bgc-2804-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/root-current281-intake-acceptance-001.json
  locator: /accepted; /intake_summary; /records; /source_placements; /unique_source_paths
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: All ten original inspections exited zero with empty stderr and 470 placements/71
    paths.
  snapshot_sha256: c3101664e021d9412d0a28e7dbbc23673a92eaac35271fbc0400a2dc358e9ad1
- evidence_id: bgc-2804-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-target-input-plan-001.json
  locator: /records/3
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: Exact current input map, 6 direct companions and the literal reader applicability.
  snapshot_sha256: 1768138ada2bdcae10e503fb5367f29803b483a4a1b9292857d128b2806dd3b2
- evidence_id: bgc-2804-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/root-current281-input-plan-acceptance-001.json
  locator: /accepted; /input_plan; /source_placements; /unique_source_paths
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: ROOT accepted the current source input plan.
  snapshot_sha256: a0999f7c6f038c5a7a25face71298a63adf5773b69ae6b5c5f5f513bf697e117
- evidence_id: bgc-2804-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/root-current281-five-gates-acceptance-001.json
  locator: /records; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: Five local gates passed; queue rows are review leads, not findings. Full
    QC/OAK remain unavailable.
  snapshot_sha256: bee633ce4ef4b1ffa11a1442e4684d04cd28725d99a824e742150ba78847f993
- evidence_id: bgc-2804-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-current281-assigned-source-reading-001.json
  locator: /contexts/9; /counts; /reading_attribution
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: All 3 complete positive dictionaries/38 fields and 6 bounded negative frames
    were personally read in the attributed source pass.
  snapshot_sha256: 5d32ddd463223a0a84898654015ae7d14e5c57604017b2876616712ae485e9e9
- evidence_id: bgc-2804-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: The original 113 source placements/1,389 fields retain BGC 38 and Support
    75 primary-row attribution; Native and ROOT have zero primary-row credit.
  snapshot_sha256: d1ca69f6f2602123f4e78b56ad442002a36a9d9fe9500a36c7efbce2163569ec
- evidence_id: bgc-2804-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/native-prep/native-current281-cached-taxonomy-reading-001.json
  locator: /scope; /context_interpretations/19; /interpretation
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: The BGC0002342 producer is Myxococcus xanthus (NCBITaxon:34), with source
    BGC_CHARACTERIZED grade and knockout/heterologous-expression methods. Streptomyces
    prunicolor (NCBITaxon:67348) belongs to the separate LOTUS occurrence route. Neither
    cached naming nor that occurrence is used to replace or strengthen the retained
    producer assertion. Cached names do not independently supply rank, lineage or
    strain-level evidence.
  snapshot_sha256: 5c1f8bf064a6a33157f3bd0a91780fee3194a6e3f6a0bf388ebfa8a4a1039672
  search_scope: Exact current taxon route and retained cached names/synonyms; no fresh
    external taxonomy or inferred hierarchy.
- evidence_id: bgc-2804-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/native-prep/native-current281-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: Nine substantive tables/3,422 rows were scanned by Native; 10 lexical candidates
    yield zero exact applicable decisions. Two reserved census-only tables are excluded.
  snapshot_sha256: a3ef3db1fbabc749d3da41afdf67beb422a7534fb4a5ea302d922bd0ffb166f3
  search_scope: Actual captured table inputs and exact identity/source/occurrence/assay
    predicates; no decision from lexical similarity.
- evidence_id: bgc-2804-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/native-prep/native-current281-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: The saved PubChem BioAssay frame has no row or blank sentinel for this
    owner. No actual AID or molecular target is captured. ChEBI structure/origin,
    CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not
    global absence, inactivity, potency or target-mechanism proof.
  snapshot_sha256: a3ef3db1fbabc749d3da41afdf67beb422a7534fb4a5ea302d922bd0ffb166f3
  search_scope: Exact owner full-key/CID scope; blank-AID rows are sentinels. No other-owner
    assay is transferred.
- evidence_id: bgc-2804-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters(includeUnassigned=True)'
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: The source stereo_complete flag tests unassigned atom-centred chirality,
    not all double-bond geometry or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2804-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines 295-306: choose_pathway'
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: Exactly one supported mapped pathway selects filing; zero, unsupported
    single or multiple labels retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2804-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
- evidence_id: bgc-2804-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 2854-2854; raw record sha256 41ca0947d1d176097f6cc150a29e06bec69cd5a16a9b8cdfcd994d4e44e9faae
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: All 25 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2804-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: 'Complete saved chebi_structures frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/myxofacycline-d.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "AYZBMLHVFCLOSX-UHFFFAOYSA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2804-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 1 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
- evidence_id: bgc-2804-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 419-419; raw record sha256 1589c1855c0ef80be754b1d399b6a699e59c7f5cd2c906e924ef0aadb7184220
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: All 6 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2804-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences frame: 0 positive placements, with
    all fields and bounded query meanings read.'
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/myxofacycline-d.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "AYZBMLHVFCLOSX-UHFFFAOYSA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2804-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 positive placements, with all fields
    and bounded query meanings read.'
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
- evidence_id: bgc-2804-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 128-128; raw record sha256 fd817e40b719b0681fc5184bc19edbbe821674aac38ff4f4c12579edbbc78ffa
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: supports
  summary: All 7 fields read, preserving blanks, evidence grades, source identity
    and citation grain.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2804-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: 'Complete saved pubchem_bioassay frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/myxofacycline-d.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "AYZBMLHVFCLOSX-UHFFFAOYSA-N",
    "table": "pubchem_bioassay"}'
- evidence_id: bgc-2804-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets frame: 0 positive placements, with all
    fields and bounded query meanings read.'
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/myxofacycline-d.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "AYZBMLHVFCLOSX-UHFFFAOYSA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2804-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 positive placements,
    with all fields and bounded query meanings read.'
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/myxofacycline-d.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "AYZBMLHVFCLOSX-UHFFFAOYSA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2804-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: 'Complete saved chebi_origins frame: 0 positive placements, with all fields
    and bounded query meanings read.'
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/myxofacycline-d.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: bgc-2804-congener-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/myxofacycline-e.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 217af40d7f6cdd5fce6c715f301ea53722f984d736a3d07aab4fb03e3b6ad965
- evidence_id: bgc-2804-congener-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/myxofacycline-f.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: b883a268156852475a3290c9e411c02ea61f0b350edf5dfb703b82caa28fb689
- evidence_id: bgc-2804-congener-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/myxofacycline-g.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 97805dfcd098cd821ed1a5ef68861472311ebcebc8967e60f1482c4dd6b9ee9a
- evidence_id: bgc-2804-congener-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/fatty_acids/myxofacycline-a.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: e542894641f17bad9dda44700cefd66dc1e479bc26e1d558097826029c304bee
- evidence_id: bgc-2804-congener-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/fatty_acids/myxofacycline-b.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 7c66ef4af142c17f99f47978976f000019c51928c06a22b743ec60fa29f466ed
- evidence_id: bgc-2804-congener-5
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/fatty_acids/myxofacycline-c.yaml
  locator: Complete current owner identity/source concepts and attributed history
  accessed_at: '2026-11-07T02:12:20.759782Z'
  support: context_only
  summary: Direct shared-BGC context retains a distinct complete key. No molecular,
    stereochemical, activity or experimental-grade transfer follows.
  snapshot_sha256: 8c2342b1bf3f0e282ae3d41d197b800dce7834fa5287be4cf536406ba12c865a
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-281/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json
  accessed_at: '2026-11-07T01:30:24.330865Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 03a80e1e85942727ce16ef18e7738a8f6e4f475ae16c33bafdff14983e11c92b
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-281/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json
  accessed_at: '2026-11-07T01:30:50.002163Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 82e9b13ab7c0c7d66e1b379908bd1f6d1808dfa47a52bbffbf993f138e0338e5
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-281/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json
  accessed_at: '2026-11-07T01:31:10.249345Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-281/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json
  accessed_at: '2026-11-07T01:31:44.888349Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-281/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json
  accessed_at: '2026-11-07T01:31:56.831286Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: d0c62425db906e0c8a82e0acf6b68378fb634710f508f7e411fc343e525870de
assessments:
- assessment_id: bgc-2804-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: myxofacycline D retains exact identifier naturalproductmech:mibig-75d7a33032,
    complete key AYZBMLHVFCLOSX-UHFFFAOYSA-N, and source rows BGC0002342 v3 compound
    index 2. Cross-references npatlas:NPA033231 remain attributed identifiers, not
    fresh authority confirmation. Both saved forms normalize to C15H25NO4 and the
    declared full key. Distinct source compounds and direct companions retain their
    own full keys; no identity, experimental grade or stereochemistry is transferred.
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  evidence_ids:
  - bgc-2804-identity
  - bgc-2804-whole-owner-attribution
  - bgc-2804-chemistry
  - bgc-2804-query-mibig_compounds
  - bgc-2804-plan
  - bgc-2804-row-mibig_compounds-0
  - bgc-2804-congener-0
  - bgc-2804-congener-1
  - bgc-2804-congener-2
  - bgc-2804-congener-3
  - bgc-2804-congener-4
  - bgc-2804-congener-5
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    value: AYZBMLHVFCLOSX-UHFFFAOYSA-N
    evidence_ids:
    - bgc-2804-identity
    - bgc-2804-whole-owner-attribution
    - bgc-2804-chemistry
    - bgc-2804-query-mibig_compounds
    - bgc-2804-plan
    - bgc-2804-row-mibig_compounds-0
    - bgc-2804-congener-0
    - bgc-2804-congener-1
    - bgc-2804-congener-2
    - bgc-2804-congener-3
    - bgc-2804-congener-4
    - bgc-2804-congener-5
  - name: grounding_scope
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    value: myxofacycline D retains exact identifier naturalproductmech:mibig-75d7a33032,
      complete key AYZBMLHVFCLOSX-UHFFFAOYSA-N, and source rows BGC0002342 v3 compound
      index 2. Cross-references npatlas:NPA033231 remain attributed identifiers, not
      fresh authority confirmation. Both saved forms normalize to C15H25NO4 and the
      declared full key. Distinct source compounds and direct companions retain their
      own full keys; no identity, experimental grade or stereochemistry is transferred.
    evidence_ids:
    - bgc-2804-identity
    - bgc-2804-whole-owner-attribution
    - bgc-2804-chemistry
    - bgc-2804-query-mibig_compounds
    - bgc-2804-plan
    - bgc-2804-row-mibig_compounds-0
    - bgc-2804-congener-0
    - bgc-2804-congener-1
    - bgc-2804-congener-2
    - bgc-2804-congener-3
    - bgc-2804-congener-4
    - bgc-2804-congener-5
- assessment_id: bgc-2804-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: The saved neutral connected C15H25NO4 graph has 20 atoms and 20 bonds.
    One aromatic five-ring contains adjacent N18/O19 and three carbons, supporting
    an isoxazole-like structural description; the retained computation represents
    the literal Kekule input aromatically. A branched alkyl chain bears OH at C7–O8,
    and C15(=O16)–O17H is a carboxylic acid. The motif table has no strict amide or
    ester, and this N–O ring is not a C5O sugar ring. Aromatic normalization is not
    by itself a record defect or proof of biosynthetic origin. The OH-bearing atom
    is an unspecified tetrahedral centre (SMILES C7, corresponding InChI C12), consistent
    with the source stereo_complete:false flag and the key without an assigned stereo
    layer. Canonical agreement and complete limited atom mapping preserve this unknown;
    they cannot assign a natural enantiomer or resolve stereochemistry by comparison
    with another myxofacycline. Both stored forms parsed; all ten recorded comparisons,
    including both canonical SMILES comparisons, are true, and the limited 20-atom
    correspondence is complete. The diagnostic still reports full_graph_identity_established:false.
    This bounded agreement supports consistent local representation while leaving
    the unspecified centre and experimental natural identity unresolved; no additional
    cleanup or parse was performed.
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  evidence_ids:
  - bgc-2804-identity
  - bgc-2804-chemistry
  - bgc-2804-molecular-reading
  - bgc-2804-diagnostic-acceptance
  - bgc-2804-diagnostic-stderr
  - bgc-2804-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    value: The OH-bearing atom is an unspecified tetrahedral centre (SMILES C7, corresponding
      InChI C12), consistent with the source stereo_complete:false flag and the key
      without an assigned stereo layer. Canonical agreement and complete limited atom
      mapping preserve this unknown; they cannot assign a natural enantiomer or resolve
      stereochemistry by comparison with another myxofacycline.
    evidence_ids:
    - bgc-2804-identity
    - bgc-2804-chemistry
    - bgc-2804-molecular-reading
    - bgc-2804-diagnostic-acceptance
    - bgc-2804-diagnostic-stderr
    - bgc-2804-stereo-policy
  - name: representation_correspondence
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    value: Both stored forms parsed; all ten recorded comparisons, including both
      canonical SMILES comparisons, are true, and the limited 20-atom correspondence
      is complete. The diagnostic still reports full_graph_identity_established:false.
      This bounded agreement supports consistent local representation while leaving
      the unspecified centre and experimental natural identity unresolved; no additional
      cleanup or parse was performed.
    evidence_ids:
    - bgc-2804-identity
    - bgc-2804-chemistry
    - bgc-2804-molecular-reading
    - bgc-2804-diagnostic-acceptance
    - bgc-2804-diagnostic-stderr
    - bgc-2804-stereo-policy
- assessment_id: bgc-2804-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: The BGC0002342 producer is Myxococcus xanthus (NCBITaxon:34), with source
    BGC_CHARACTERIZED grade and knockout/heterologous-expression methods. Streptomyces
    prunicolor (NCBITaxon:67348) belongs to the separate LOTUS occurrence route. Neither
    cached naming nor that occurrence is used to replace or strengthen the retained
    producer assertion. BGC0002342 v3 retains MT513750.1:8235–29793, NRPS|PKS with
    Type I|Unknown subclass, CLUSTER_DEMONSTRATED and knockout/heterologous-expression
    methods. It is active and quality questionable, but completeness is explicitly
    unknown. Its blank compound-class field and ENTRY-grain PMID:34617331 are preserved;
    the six other myxofacyclines sharing this entry keep distinct full keys and source
    stereo flags.
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  evidence_ids:
  - bgc-2804-provenance
  - bgc-2804-query-mibig_compounds
  - bgc-2804-taxonomy
  - bgc-2804-curation
  - bgc-2804-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    value: The BGC0002342 producer is Myxococcus xanthus (NCBITaxon:34), with source
      BGC_CHARACTERIZED grade and knockout/heterologous-expression methods. Streptomyces
      prunicolor (NCBITaxon:67348) belongs to the separate LOTUS occurrence route.
      Neither cached naming nor that occurrence is used to replace or strengthen the
      retained producer assertion.
    evidence_ids:
    - bgc-2804-provenance
    - bgc-2804-query-mibig_compounds
    - bgc-2804-taxonomy
    - bgc-2804-curation
    - bgc-2804-row-mibig_compounds-0
  - name: producer_evidence
    definition: Producer evidence grade and its demonstrated or asserted scope.
    value: The BGC0002342 producer is Myxococcus xanthus (NCBITaxon:34), with source
      BGC_CHARACTERIZED grade and knockout/heterologous-expression methods. Streptomyces
      prunicolor (NCBITaxon:67348) belongs to the separate LOTUS occurrence route.
      Neither cached naming nor that occurrence is used to replace or strengthen the
      retained producer assertion.
    evidence_ids:
    - bgc-2804-provenance
    - bgc-2804-query-mibig_compounds
    - bgc-2804-taxonomy
    - bgc-2804-curation
    - bgc-2804-row-mibig_compounds-0
  - name: locus_evidence
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    value: BGC0002342 v3 retains MT513750.1:8235–29793, NRPS|PKS with Type I|Unknown
      subclass, CLUSTER_DEMONSTRATED and knockout/heterologous-expression methods.
      It is active and quality questionable, but completeness is explicitly unknown.
      Its blank compound-class field and ENTRY-grain PMID:34617331 are preserved;
      the six other myxofacyclines sharing this entry keep distinct full keys and
      source stereo flags.
    evidence_ids:
    - bgc-2804-provenance
    - bgc-2804-query-mibig_compounds
    - bgc-2804-taxonomy
    - bgc-2804-curation
    - bgc-2804-row-mibig_compounds-0
- assessment_id: bgc-2804-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: 'BGC0002342: PMID:34617331 at ENTRY grain. These are attributed database
    citations, not newly examined primary bodies. DOI case variants and repeated placements
    do not create independent evidence. All 2 histories were read: 2 are seeder-attributed
    SEEDED_FROM_SOURCES events.'
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  evidence_ids:
  - bgc-2804-history
  - bgc-2804-source-reading
  - bgc-2804-query-mibig_compounds
  - bgc-2804-row-mibig_compounds-0
  - bgc-2804-row-lotus_occurrences-0
  dimensions:
  - name: citation_scope
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    value: 'BGC0002342: PMID:34617331 at ENTRY grain. These are attributed database
      citations, not newly examined primary bodies. DOI case variants and repeated
      placements do not create independent evidence. All 2 histories were read: 2
      are seeder-attributed SEEDED_FROM_SOURCES events.'
    evidence_ids:
    - bgc-2804-history
    - bgc-2804-source-reading
    - bgc-2804-query-mibig_compounds
    - bgc-2804-row-mibig_compounds-0
    - bgc-2804-row-lotus_occurrences-0
- assessment_id: bgc-2804-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: The LOTUS occurrence is Streptomyces prunicolor (NCBITaxon:67348), DOI:10.1002/CHEM.202103095.
    It remains separate from the Myxococcus xanthus producer claim and from all other
    myxofacycline keys, even though the companions share the same retained occurrence
    citation. The saved PubChem BioAssay frame has no row or blank sentinel for this
    owner. No actual AID or molecular target is captured. ChEBI structure/origin,
    CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives, not
    global absence, inactivity, potency or target-mechanism proof.
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  evidence_ids:
  - bgc-2804-roots
  - bgc-2804-query-lotus_occurrences
  - bgc-2804-query-chebi_origins
  - bgc-2804-query-cyanometdb_occurrences
  - bgc-2804-query-pubchem_bioassay
  - bgc-2804-query-bindingdb_targets
  - bgc-2804-query-antibioticmech_inchikeys
  - bgc-2804-assay-curation
  - bgc-2804-row-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    definition: Exact retained occurrence tuples and limits on production/independence.
    value: The LOTUS occurrence is Streptomyces prunicolor (NCBITaxon:67348), DOI:10.1002/CHEM.202103095.
      It remains separate from the Myxococcus xanthus producer claim and from all
      other myxofacycline keys, even though the companions share the same retained
      occurrence citation.
    evidence_ids:
    - bgc-2804-roots
    - bgc-2804-query-lotus_occurrences
    - bgc-2804-query-chebi_origins
    - bgc-2804-query-cyanometdb_occurrences
    - bgc-2804-query-pubchem_bioassay
    - bgc-2804-query-bindingdb_targets
    - bgc-2804-query-antibioticmech_inchikeys
    - bgc-2804-assay-curation
    - bgc-2804-row-lotus_occurrences-0
  - name: assay_target_scope
    definition: Retained activity/assay/target positives and bounded negative queries.
    value: The saved PubChem BioAssay frame has no row or blank sentinel for this
      owner. No actual AID or molecular target is captured. ChEBI structure/origin,
      CyanoMetDB, BindingDB and AntibioticMech frames are bounded local negatives,
      not global absence, inactivity, potency or target-mechanism proof.
    evidence_ids:
    - bgc-2804-roots
    - bgc-2804-query-lotus_occurrences
    - bgc-2804-query-chebi_origins
    - bgc-2804-query-cyanometdb_occurrences
    - bgc-2804-query-pubchem_bioassay
    - bgc-2804-query-bindingdb_targets
    - bgc-2804-query-antibioticmech_inchikeys
    - bgc-2804-assay-curation
    - bgc-2804-row-lotus_occurrences-0
- assessment_id: bgc-2804-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: All three NPClassifier result arrays are empty, with is_glycoside:false;
    the maintained zero-result rule leaves UNCLASSIFIED. The saved graph has no sugar-like
    C5O ring, but the false model flag is not an independent natural glycosylation
    experiment. Source NRPS|PKS is retained separately and does not fill an absent
    classifier result or imply a peptide ring.
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  evidence_ids:
  - bgc-2804-classification
  - bgc-2804-chemistry
  - bgc-2804-query-npclassifier
  - bgc-2804-query-mibig_compounds
  - bgc-2804-filing-policy
  - bgc-2804-row-npclassifier-0
  - bgc-2804-row-mibig_compounds-0
  dimensions:
  - name: classification_applicability
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    value: All three NPClassifier result arrays are empty, with is_glycoside:false;
      the maintained zero-result rule leaves UNCLASSIFIED. The saved graph has no
      sugar-like C5O ring, but the false model flag is not an independent natural
      glycosylation experiment. Source NRPS|PKS is retained separately and does not
      fill an absent classifier result or imply a peptide ring.
    evidence_ids:
    - bgc-2804-classification
    - bgc-2804-chemistry
    - bgc-2804-query-npclassifier
    - bgc-2804-query-mibig_compounds
    - bgc-2804-filing-policy
    - bgc-2804-row-npclassifier-0
    - bgc-2804-row-mibig_compounds-0
- assessment_id: bgc-2804-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: unknown
  summary: The complete current owner is carried from ROOT’s attributed whole-owner
    reading and exact current raw/capture equality. All 2 histories, nine saved source
    frames (3 positive placements/38 fields and 6 negatives), and both complete saved
    molecular forms were personally read. All 50 actual input hashes and maintained
    ownership paths join the accepted plan. Input pinning is not a claim to have substantively
    read every entire corpus. Five original local gates passed. The complete owner
    root set has no positive graph, pathway, component or molecular-target root, so
    no maintained reader applies. Full QC/OAK, fresh source-authority checks and independent
    primary confirmation remain unavailable; completion is partial.
  target_ids:
  - naturalproductmech:mibig-75d7a33032
  evidence_ids:
  - bgc-2804-owner
  - bgc-2804-whole-owner-attribution
  - bgc-2804-history
  - bgc-2804-intake
  - bgc-2804-intake-acceptance
  - bgc-2804-plan
  - bgc-2804-plan-acceptance
  - bgc-2804-gates
  - bgc-2804-source-reading
  - bgc-2804-source-notes
  - bgc-2804-molecular-reading
  - bgc-2804-roots
  dimensions:
  - name: review_completion
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    value: The complete current owner is carried from ROOT’s attributed whole-owner
      reading and exact current raw/capture equality. All 2 histories, nine saved
      source frames (3 positive placements/38 fields and 6 negatives), and both complete
      saved molecular forms were personally read. All 50 actual input hashes and maintained
      ownership paths join the accepted plan. Input pinning is not a claim to have
      substantively read every entire corpus. Five original local gates passed. The
      complete owner root set has no positive graph, pathway, component or molecular-target
      root, so no maintained reader applies. Full QC/OAK, fresh source-authority checks
      and independent primary confirmation remain unavailable; completion is partial.
    evidence_ids:
    - bgc-2804-owner
    - bgc-2804-whole-owner-attribution
    - bgc-2804-history
    - bgc-2804-intake
    - bgc-2804-intake-acceptance
    - bgc-2804-plan
    - bgc-2804-plan-acceptance
    - bgc-2804-gates
    - bgc-2804-source-reading
    - bgc-2804-source-notes
    - bgc-2804-molecular-reading
    - bgc-2804-roots
findings: []
actions: []
limitations:
- Fresh source-authority, primary publication, sequence and strain verification remain
  unavailable. Full QC/OAK were not run; retained experimental grades stay source-attributed.
- Both stored forms parsed; all ten recorded comparisons, including both canonical
  SMILES comparisons, are true, and the limited 20-atom correspondence is complete.
  The diagnostic still reports full_graph_identity_established:false. This bounded
  agreement supports consistent local representation while leaving the unspecified
  centre and experimental natural identity unresolved; no additional cleanup or parse
  was performed. Four undefined-stereo warnings remain globally unassigned; no message
  is attributed to this owner.
- The OH-bearing atom is an unspecified tetrahedral centre (SMILES C7, corresponding
  InChI C12), consistent with the source stereo_complete:false flag and the key without
  an assigned stereo layer. Canonical agreement and complete limited atom mapping
  preserve this unknown; they cannot assign a natural enantiomer or resolve stereochemistry
  by comparison with another myxofacycline.
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
- batch-281
```
