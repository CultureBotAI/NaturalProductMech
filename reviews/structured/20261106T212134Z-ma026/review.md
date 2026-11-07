# Local evidence review: MA026

- Review: 20261106T212134Z-ma026
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T20:51:57.270672Z
- Finished UTC: 2026-11-06T21:21:34.858643Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

MA026 retains a lipid-bearing cyclic depsipeptide scaffold with a 25-membered ester-containing ring, six specified and ten unspecified atom centres. Its source assertion, unstated locus evidence and amide–imidic representation limits keep this review partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2761; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-41bdd645a6 | data/natural_products/unclassified/ma026.yaml | generated | MA026 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-41bdd645a6 | Both exact stored forms parsed in the original 20-attempt diagnostic and agree in formula, aggregate charge, normalized Standard InChI and full key. |
| strict_ten | passed | True | naturalproductmech:mibig-41bdd645a6 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-41bdd645a6 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-41bdd645a6 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-41bdd645a6 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-41bdd645a6 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-41bdd645a6 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-41bdd645a6 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-41bdd645a6 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: naturalproductmech:mibig-41bdd645a6.

MA026 retains exact owner naturalproductmech:mibig-41bdd645a6, complete key UUNSGSIHFUBGCM-XVRKXJHRSA-N, and MIBiG BGC0002379 v3 compound index 1. Its retained cross-references (npatlas:NPA033064) are source-attributed, not remotely adjudicated. Both original forms normalize to C84H146N18O23 and the full declared key. The exact captured owner is resolved for this review; no broader family or similarly named target is substituted.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-41bdd645a6.

Both saved forms contain 125 atoms and 125 bonds in one component. The SMILES graph has one 25-membered ester-containing peptide ring (saved ring 0), an acyclic hydroxyalkyl acyl chain, 18 amide sites and one free carboxyl group. The ring ester is C63(=O64)-O62-C61; the free acid is C24(=O25)-O26H. Four of the amides are terminal carboxamides at C33/C54/C76/C93, so the total amide count is not a residue count. This encoded topology supports a lipid-bearing cyclic depsipeptide scaffold without assigning every natural residue or its biosynthetic assembly. No C5O sugar-ring candidate is encoded. Both forms preserve six specified tetrahedral centres and ten unspecified tetrahedral centres. The six specified SMILES centres are C13/C21/C30/C39/C43/C51, all assigned S in the saved table. The partial /t layer and stereo_complete:false are consistent with the ten unassigned centres. The InChI reconstruction adds 18 unspecified C=N stereo potentials at its imidic sites; these are representation-dependent, not 18 unresolved carbon-carbon alkenes in the source SMILES. No natural stereochemistry is newly certified. Eighteen SMILES C(=O)-N sites become terminal C(OH)=N sites in the InChI reconstruction; each saved imidic oxygen has one hydrogen, and four terminal imidic nitrogens retain one hydrogen. Carbonyl/amide counts change from 20/18 to 2/0, while the ester and free acid remain. Formula, total charge, normalized Standard InChI and the full declared key agree. Both canonical SMILES comparisons are false and the limited map is empty, so exact graph identity is not established. This retained mobile-H representation difference alone is not a demonstrated source defect.

### Producer assertion versus locus evidence

provenance: supported. Targets: naturalproductmech:mibig-41bdd645a6.

Pseudomonas sp. RtIB026/NCBITaxon:2749999 remains a SOURCE_ASSERTION. The separate Pseudomonas/NCBITaxon:286 LOTUS label establishes neither the same strain nor demonstrated production. BGC0002379 v3 is active, questionable in quality and of unknown completeness. AP023348.1:3642436-3761997 remains CLUSTER_UNSTATED with no stated method; coordinates do not prove a demonstrated locus. Source NRPS/Type I is a cluster classification, not a complete MA026 pathway.

### Citation grain and attributed history

evidence: supported. Targets: naturalproductmech:mibig-41bdd645a6.

PMID:33533101 retains MIBiG ENTRY citation grain. LOTUS DOI strings remain attached to their individual occurrence tuples; publication independence and underlying primary claims are not newly verified. All 2 history events are SEEDED_FROM_SOURCES and seeder-attributed.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: naturalproductmech:mibig-41bdd645a6.

The one retained LOTUS tuple reports Pseudomonas/NCBITaxon:286 with DOI:10.1002/ANGE.202015193. This remains evidence of a reported occurrence, separate from the strain-labelled MIBiG source assertion. No actual PubChem AID or blank-AID sentinel belongs to this owner. ChEBI structures/origins, CyanoMetDB, BindingDB and AntibioticMech are bounded negative saved frames for this key. These local negatives establish neither global absence nor biological inactivity, potency or a molecular target.

### Computed filing and asserted class applicability

consistency: supported. Targets: naturalproductmech:mibig-41bdd645a6.

NPClassifier npclassifier.gnps2.org@2026-09-07 predicts Amino acids and Peptides&#124;Polyketides, Oligopeptides and Cyclic peptides&#124;Depsipeptides&#124;Lipopeptides; is_glycoside is false. The stored peptide bonds, cyclic ester and hydroxyalkyl acyl segment are compatible with those broad scaffold labels. Two pathway predictions correctly retain UNCLASSIFIED filing; the source compound_classes field is blank. Neither predictions nor topology identify a complete biological pathway.

### Local completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-41bdd645a6.

Whole current owner and its 2 seeder histories, all nine saved source frames (3 positive placements/38 fields and 6 negatives), and both complete original molecular tables were read. All 44 actual input hashes and maintained ownership declarations were joined; this is not a claim to have substantively read every entire input corpus. Five original local gates passed. Full QC/OAK, live source-authority checks and independent primary confirmation remain unavailable, so completion is partial. No literal graph/pathway/component/target root requires a maintained reader. Any later correction belongs in maintained inputs, applicable curation, extractors or the seeder.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2761-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/ma026.yaml; Whole retained plaintext including all curation_history entries | supports | Whole owner and history previously read; current bytes equal accepted capture. |
| bgc-2761-identity | /private/tmp/npm-review-work/shared-next-batch277/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status | supports | MA026 retains exact owner naturalproductmech:mibig-41bdd645a6, complete key UUNSGSIHFUBGCM-XVRKXJHRSA-N, and MIBiG BGC0002379 v3 compound index 1. Its retained cross-references (npatlas:NPA033064) are source-attributed, not remotely adjudicated. Both original forms normalize to C84H146N18O23 and the full declared key. The exact captured owner is resolved for this review; no broader family or similarly named target is substituted. |
| bgc-2761-history | /private/tmp/npm-review-work/shared-next-batch277/owner-capture-DATA-001.json; /records/0/owner_document/curation_history | supports | PMID:33533101 retains MIBiG ENTRY citation grain. LOTUS DOI strings remain attached to their individual occurrence tuples; publication independence and underlying primary claims are not newly verified. All 2 history events are SEEDED_FROM_SOURCES and seeder-attributed. |
| bgc-2761-provenance | /private/tmp/npm-review-work/shared-next-batch277/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters | supports | Pseudomonas sp. RtIB026/NCBITaxon:2749999 remains a SOURCE_ASSERTION. The separate Pseudomonas/NCBITaxon:286 LOTUS label establishes neither the same strain nor demonstrated production. BGC0002379 v3 is active, questionable in quality and of unknown completeness. AP023348.1:3642436-3761997 remains CLUSTER_UNSTATED with no stated method; coordinates do not prove a demonstrated locus. Source NRPS/Type I is a cluster classification, not a complete MA026 pathway. |
| bgc-2761-classification | /private/tmp/npm-review-work/shared-next-batch277/owner-capture-DATA-001.json; /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway; /records/0/owner_document/bgc_class | supports | NPClassifier npclassifier.gnps2.org@2026-09-07 predicts Amino acids and Peptides&#124;Polyketides, Oligopeptides and Cyclic peptides&#124;Depsipeptides&#124;Lipopeptides; is_glycoside is false. The stored peptide bonds, cyclic ester and hydroxyalkyl acyl segment are compatible with those broad scaffold labels. Two pathway predictions correctly retain UNCLASSIFIED filing; the source compound_classes field is blank. Neither predictions nor topology identify a complete biological pathway. |
| bgc-2761-roots | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json; /contexts/4/complete_root_keys; /contexts/4/declared_mechanism_roots_literal; /contexts/4/literal_bioactivities_root | context_only | Complete saved root declarations have no positive mechanism, component, target or measured activity root; no maintained reader applies. |
| bgc-2761-chemistry | /private/tmp/npm-review-work/shared-next-batch277/chemistry-local/diagnostic-DATA-001.json; /records/0/smiles/computed; /records/0/inchi/computed; /records/0/comparisons; /records/0/atom_correspondence | supports | Both saved forms contain 125 atoms and 125 bonds in one component. The SMILES graph has one 25-membered ester-containing peptide ring (saved ring 0), an acyclic hydroxyalkyl acyl chain, 18 amide sites and one free carboxyl group. The ring ester is C63(=O64)-O62-C61; the free acid is C24(=O25)-O26H. Four of the amides are terminal carboxamides at C33/C54/C76/C93, so the total amide count is not a residue count. This encoded topology supports a lipid-bearing cyclic depsipeptide scaffold without assigning every natural residue or its biosynthetic assembly. No C5O sugar-ring candidate is encoded. Both forms preserve six specified tetrahedral centres and ten unspecified tetrahedral centres. The six specified SMILES centres are C13/C21/C30/C39/C43/C51, all assigned S in the saved table. The partial /t layer and stereo_complete:false are consistent with the ten unassigned centres. The InChI reconstruction adds 18 unspecified C=N stereo potentials at its imidic sites; these are representation-dependent, not 18 unresolved carbon-carbon alkenes in the source SMILES. No natural stereochemistry is newly certified. Eighteen SMILES C(=O)-N sites become terminal C(OH)=N sites in the InChI reconstruction; each saved imidic oxygen has one hydrogen, and four terminal imidic nitrogens retain one hydrogen. Carbonyl/amide counts change from 20/18 to 2/0, while the ester and free acid remain. Formula, total charge, normalized Standard InChI and the full declared key agree. Both canonical SMILES comparisons are false and the limited map is empty, so exact graph identity is not established. This retained mobile-H representation difference alone is not a demonstrated source defect. |
| bgc-2761-molecular-reading | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-current277-first-five-molecular-reading-001.json; /records/0; /scope_orders; /method_limits | supports | Complete saved tables personally read; representation-aware interpretation retained without a new parse. |
| bgc-2761-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch277/chemistry-local/root-current277-diagnostic-acceptance-001.json; /status; /accepted; /data; /molecular_parse_attempts; /warning_attribution | supports | ROOT accepted 20 original stored-form parses; canonical and full-identity limits are preserved. |
| bgc-2761-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch277/chemistry-local/diagnostic-execution-001.json; /command; /exit_code | supports | Original ROOT diagnostic argv and exit zero, without replay. |
| bgc-2761-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch277/chemistry-local/diagnostic-original-001.stderr; Complete original stderr including blank separators | context_only | Two charge-rearrangement and two undefined-stereo warnings remain globally unassigned. |
| bgc-2761-intake | /private/tmp/npm-review-work/shared-next-batch277/intakes-001/2761-inspect-001.json; /targets; /source/inputs | supports | One exact target, 44 current inputs and explicit maintained owner paths. |
| bgc-2761-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch277/root-current277-intake-acceptance-001.json; /accepted; /records/0; /source_placements; /unique_source_paths | supports | ROOT accepted ten original inspections with 468 input placements/59 paths and empty stderr. |
| bgc-2761-plan | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-target-input-plan-001.json; /records/0 | supports | Exact current input map with 0 direct companion paths and no reader requirement. |
| bgc-2761-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch277/root-current277-input-plan-acceptance-001.json; /accepted; /plan; /source_placements; /unique_source_paths | supports | ROOT accepted the actual current source input plan. |
| bgc-2761-gates | /private/tmp/npm-review-work/shared-next-batch277/root-current277-five-gates-acceptance-001.json; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows | context_only | Five local gates passed. Queue entries are bounded leads; full QC/OAK remain unavailable and gate passes do not establish biology. |
| bgc-2761-source-reading | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-current277-assigned-source-reading-001.json; /contexts/4; /counts; /reading_attribution | supports | All 3 positive source dictionaries/38 fields and 6 negative frames were read in the separately attributed source pass. |
| bgc-2761-source-notes | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-scope-notes-001.json; /totals; /reading_reconciliation; /reading_boundaries | context_only | Current 59 rows/679 fields retain BGC 32 and Support 27 primary-row attribution; Native/ROOT have zero primary-row credit. |
| bgc-2761-taxonomy | /private/tmp/npm-review-work/shared-next-batch277-tentative/native-prep/native-current277-cached-taxonomy-reading-002.json; /scope; /context_interpretations/4; /interpretation | context_only | Pseudomonas sp. RtIB026/NCBITaxon:2749999 remains a SOURCE_ASSERTION. The separate Pseudomonas/NCBITaxon:286 LOTUS label establishes neither the same strain nor demonstrated production. Cached stanzas contain no rank or lineage; no external taxonomy upgrade follows. |
| bgc-2761-curation | /private/tmp/npm-review-work/shared-next-batch277-tentative/native-prep/native-current277-implemented-curation-scan-002.json; /scope; /counts; /applied_rows; /interpretation | context_only | Native scanned nine substantive tables/3,422 rows. All 95 lexical candidates fail exact predicates, including 94 coordinate-token-only hits and one unresolved Macrophoma diagnostic. No applicable correction. |
| bgc-2761-assay-curation | /private/tmp/npm-review-work/shared-next-batch277-tentative/native-prep/native-current277-implemented-curation-scan-002.json; /assay_scope | context_only | No actual PubChem AID or blank-AID sentinel belongs to this owner. ChEBI structures/origins, CyanoMetDB, BindingDB and AntibioticMech are bounded negative saved frames for this key. These local negatives establish neither global absence nor biological inactivity, potency or a molecular target. |
| bgc-2761-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters(includeUnassigned=True) | context_only | stereo_complete tests unassigned atom-centred chirality; it does not certify every bond configuration or natural identity. |
| bgc-2761-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306: choose_pathway | context_only | One mapped pathway selects filing; zero or multiple labels retain UNCLASSIFIED while keeping all predictions. |
| bgc-2761-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 positive placements with every retained field and negative predicate read. |
| bgc-2761-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 2932-2932; raw record sha256 6ca97ff947628e194b073504b6b8dbab30f95ba06315e2fbb3588370a7e41be5 | supports | All 25 fields read, preserving literal blanks, source qualifiers and citation grain. |
| bgc-2761-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures frame: 0 positive placements with every retained field and negative predicate read. |
| bgc-2761-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 1 positive placements with every retained field and negative predicate read. |
| bgc-2761-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 8916-8916; raw record sha256 2f7eaf0e7c2fc6b2bf688e6f61c753dad61c39288753e47375d67f1a53bb298d | supports | All 6 fields read, preserving literal blanks, source qualifiers and citation grain. |
| bgc-2761-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences frame: 0 positive placements with every retained field and negative predicate read. |
| bgc-2761-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 positive placements with every retained field and negative predicate read. |
| bgc-2761-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2465-2465; raw record sha256 0b6b811334ba302c2a50d4e78a70abc93324f9e96d8ca977250b955a14bc6210 | supports | All 7 fields read, preserving literal blanks, source qualifiers and citation grain. |
| bgc-2761-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/pubchem_bioassay | context_only | Complete saved pubchem_bioassay frame: 0 positive placements with every retained field and negative predicate read. |
| bgc-2761-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets frame: 0 positive placements with every retained field and negative predicate read. |
| bgc-2761-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys frame: 0 positive placements with every retained field and negative predicate read. |
| bgc-2761-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins frame: 0 positive placements with every retained field and negative predicate read. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-277/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-277/native-current277-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-277/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-277/native-current277-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-277/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-277/native-current277-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-277/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-277/native-current277-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-277/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-277/native-current277-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External authority, primary publications, sequence-level and strain-level confirmation were not newly obtained. Full QC/OAK are unavailable; source assertions and source-level experimental grades remain attributed.
- Eighteen SMILES C(=O)-N sites become terminal C(OH)=N sites in the InChI reconstruction; each saved imidic oxygen has one hydrogen, and four terminal imidic nitrogens retain one hydrogen. Carbonyl/amide counts change from 20/18 to 2/0, while the ester and free acid remain. Formula, total charge, normalized Standard InChI and the full declared key agree. Both canonical SMILES comparisons are false and the limited map is empty, so exact graph identity is not established. This retained mobile-H representation difference alone is not a demonstrated source defect. The original two charge-rearrangement and two undefined-stereo warnings remain globally unassigned.
- Both forms preserve six specified tetrahedral centres and ten unspecified tetrahedral centres. The six specified SMILES centres are C13/C21/C30/C39/C43/C51, all assigned S in the saved table. The partial /t layer and stereo_complete:false are consistent with the ten unassigned centres. The InChI reconstruction adds 18 unspecified C=N stereo potentials at its imidic sites; these are representation-dependent, not 18 unresolved carbon-carbon alkenes in the source SMILES. No natural stereochemistry is newly certified.
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
review_id: 20261106T212134Z-ma026
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: MA026'
started_at: '2026-11-06T20:51:57.270672Z'
finished_at: '2026-11-06T21:21:34.858643Z'
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
summary: MA026 retains a lipid-bearing cyclic depsipeptide scaffold with a 25-membered
  ester-containing ring, six specified and ten unspecified atom centres. Its source
  assertion, unstated locus evidence and amide–imidic representation limits keep this
  review partial.
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
  - path: data/natural_products/unclassified/ma026.yaml
    sha256: b32b164cf66049a4c5a4b3c5e5ffb719b96123c23b5166d57f1b0dd53cf1cb60
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
  selection: Campaign path order 2761; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-41bdd645a6
targets:
- target_id: naturalproductmech:mibig-41bdd645a6
  path: data/natural_products/unclassified/ma026.yaml
  label: MA026
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch277/chemistry-local/diagnose277-001.py
    086a06a7e4078a643eacde5903b8b39fe98e02cb31395033d7d422bddc4914e1 5c1a8b6859b771749b77a3f67ee38989250fa3cef2202c25ff402100ecc43899
    5f0ca4a8b4a8160550b06294f5051c882c97c5329bc7d7f9019998b3f1b91dcf
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both exact stored forms parsed in the original 20-attempt diagnostic and
    agree in formula, aggregate charge, normalized Standard InChI and full key.
  scope_note: Eighteen SMILES C(=O)-N sites become terminal C(OH)=N sites in the InChI
    reconstruction; each saved imidic oxygen has one hydrogen, and four terminal imidic
    nitrogens retain one hydrogen. Carbonyl/amide counts change from 20/18 to 2/0,
    while the ester and free acid remain. Formula, total charge, normalized Standard
    InChI and the full declared key agree. Both canonical SMILES comparisons are false
    and the limited map is empty, so exact graph identity is not established. This
    retained mobile-H representation difference alone is not a demonstrated source
    defect. Four original warnings remain globally unassigned; no independent natural
    or primary biological certification.
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  evidence_ids:
  - bgc-2761-chemistry
  - bgc-2761-diagnostic-acceptance
  - bgc-2761-diagnostic-execution
  - bgc-2761-diagnostic-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  command: just validate-strict data/natural_products/unclassified/ma026.yaml data/natural_products/unclassified/macrophorin-a.yaml
    data/natural_products/unclassified/maklamicin.yaml data/natural_products/unclassified/malleobactin-a.yaml
    data/natural_products/unclassified/malleobactin-c.yaml data/natural_products/unclassified/malleobactin-x.yaml
    data/natural_products/unclassified/marformycin-a.yaml data/natural_products/unclassified/marformycin-b.yaml
    data/natural_products/unclassified/marformycin-c.yaml data/natural_products/unclassified/marformycin-d.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-277/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-41bdd645a6
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-277/validate-all-001.tsv
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
  - naturalproductmech:mibig-41bdd645a6
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
  - naturalproductmech:mibig-41bdd645a6
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
  - naturalproductmech:mibig-41bdd645a6
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-277/review-queue-001.tsv
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
  - naturalproductmech:mibig-41bdd645a6
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2761-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/ma026.yaml
  locator: Whole retained plaintext including all curation_history entries
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: Whole owner and history previously read; current bytes equal accepted capture.
  snapshot_sha256: b32b164cf66049a4c5a4b3c5e5ffb719b96123c23b5166d57f1b0dd53cf1cb60
- evidence_id: bgc-2761-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch277/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/chemical_structure;
    /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: MA026 retains exact owner naturalproductmech:mibig-41bdd645a6, complete
    key UUNSGSIHFUBGCM-XVRKXJHRSA-N, and MIBiG BGC0002379 v3 compound index 1. Its
    retained cross-references (npatlas:NPA033064) are source-attributed, not remotely
    adjudicated. Both original forms normalize to C84H146N18O23 and the full declared
    key. The exact captured owner is resolved for this review; no broader family or
    similarly named target is substituted.
  snapshot_sha256: 5c1a8b6859b771749b77a3f67ee38989250fa3cef2202c25ff402100ecc43899
- evidence_id: bgc-2761-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch277/owner-capture-DATA-001.json
  locator: /records/0/owner_document/curation_history
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: PMID:33533101 retains MIBiG ENTRY citation grain. LOTUS DOI strings remain
    attached to their individual occurrence tuples; publication independence and underlying
    primary claims are not newly verified. All 2 history events are SEEDED_FROM_SOURCES
    and seeder-attributed.
  snapshot_sha256: 5c1a8b6859b771749b77a3f67ee38989250fa3cef2202c25ff402100ecc43899
- evidence_id: bgc-2761-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch277/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: Pseudomonas sp. RtIB026/NCBITaxon:2749999 remains a SOURCE_ASSERTION. The
    separate Pseudomonas/NCBITaxon:286 LOTUS label establishes neither the same strain
    nor demonstrated production. BGC0002379 v3 is active, questionable in quality
    and of unknown completeness. AP023348.1:3642436-3761997 remains CLUSTER_UNSTATED
    with no stated method; coordinates do not prove a demonstrated locus. Source NRPS/Type
    I is a cluster classification, not a complete MA026 pathway.
  snapshot_sha256: 5c1a8b6859b771749b77a3f67ee38989250fa3cef2202c25ff402100ecc43899
- evidence_id: bgc-2761-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch277/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway;
    /records/0/owner_document/bgc_class
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: NPClassifier npclassifier.gnps2.org@2026-09-07 predicts Amino acids and
    Peptides|Polyketides, Oligopeptides and Cyclic peptides|Depsipeptides|Lipopeptides;
    is_glycoside is false. The stored peptide bonds, cyclic ester and hydroxyalkyl
    acyl segment are compatible with those broad scaffold labels. Two pathway predictions
    correctly retain UNCLASSIFIED filing; the source compound_classes field is blank.
    Neither predictions nor topology identify a complete biological pathway.
  snapshot_sha256: 5c1a8b6859b771749b77a3f67ee38989250fa3cef2202c25ff402100ecc43899
- evidence_id: bgc-2761-roots
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json
  locator: /contexts/4/complete_root_keys; /contexts/4/declared_mechanism_roots_literal;
    /contexts/4/literal_bioactivities_root
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: Complete saved root declarations have no positive mechanism, component,
    target or measured activity root; no maintained reader applies.
  snapshot_sha256: 267b6fbbc5f7dc45be0500268071fac46ea2827523921ecece609fb9b2d02006
  search_scope: Complete exact owner root set, not an inference of biological absence.
- evidence_id: bgc-2761-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch277/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/smiles/computed; /records/0/inchi/computed; /records/0/comparisons;
    /records/0/atom_correspondence
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: Both saved forms contain 125 atoms and 125 bonds in one component. The
    SMILES graph has one 25-membered ester-containing peptide ring (saved ring 0),
    an acyclic hydroxyalkyl acyl chain, 18 amide sites and one free carboxyl group.
    The ring ester is C63(=O64)-O62-C61; the free acid is C24(=O25)-O26H. Four of
    the amides are terminal carboxamides at C33/C54/C76/C93, so the total amide count
    is not a residue count. This encoded topology supports a lipid-bearing cyclic
    depsipeptide scaffold without assigning every natural residue or its biosynthetic
    assembly. No C5O sugar-ring candidate is encoded. Both forms preserve six specified
    tetrahedral centres and ten unspecified tetrahedral centres. The six specified
    SMILES centres are C13/C21/C30/C39/C43/C51, all assigned S in the saved table.
    The partial /t layer and stereo_complete:false are consistent with the ten unassigned
    centres. The InChI reconstruction adds 18 unspecified C=N stereo potentials at
    its imidic sites; these are representation-dependent, not 18 unresolved carbon-carbon
    alkenes in the source SMILES. No natural stereochemistry is newly certified. Eighteen
    SMILES C(=O)-N sites become terminal C(OH)=N sites in the InChI reconstruction;
    each saved imidic oxygen has one hydrogen, and four terminal imidic nitrogens
    retain one hydrogen. Carbonyl/amide counts change from 20/18 to 2/0, while the
    ester and free acid remain. Formula, total charge, normalized Standard InChI and
    the full declared key agree. Both canonical SMILES comparisons are false and the
    limited map is empty, so exact graph identity is not established. This retained
    mobile-H representation difference alone is not a demonstrated source defect.
  snapshot_sha256: 39034e243afa6fa0bccc091a8297d2e2ab64704ba3d5683bd3e6e28ca0d4d49a
- evidence_id: bgc-2761-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-current277-first-five-molecular-reading-001.json
  locator: /records/0; /scope_orders; /method_limits
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: Complete saved tables personally read; representation-aware interpretation
    retained without a new parse.
  snapshot_sha256: c723b272952e21f1a2dad058574417c6ef3434205bdbfdca9661c65ac7d75a81
- evidence_id: bgc-2761-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch277/chemistry-local/root-current277-diagnostic-acceptance-001.json
  locator: /status; /accepted; /data; /molecular_parse_attempts; /warning_attribution
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: ROOT accepted 20 original stored-form parses; canonical and full-identity
    limits are preserved.
  snapshot_sha256: 3ca9e985c9e95571f2d2fda7e7ec82ceda5a7a51a44c3c60d132e4e542726059
- evidence_id: bgc-2761-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch277/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: Original ROOT diagnostic argv and exit zero, without replay.
  snapshot_sha256: 716e9ab0a7909165b65ca662b4c0d17309696a0f35a0397e804d011554d49610
- evidence_id: bgc-2761-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch277/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr including blank separators
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: Two charge-rearrangement and two undefined-stereo warnings remain globally
    unassigned.
  snapshot_sha256: f59c20af9c5fa7ada11c2b49ca94043277c1a3e32b7a7982d638728c7c80c0b7
- evidence_id: bgc-2761-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch277/intakes-001/2761-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: One exact target, 44 current inputs and explicit maintained owner paths.
  snapshot_sha256: 77480f81bf1a18129ff32868d45251ec383a3a8dd8490afde5a77703d4ac2c89
- evidence_id: bgc-2761-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch277/root-current277-intake-acceptance-001.json
  locator: /accepted; /records/0; /source_placements; /unique_source_paths
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: ROOT accepted ten original inspections with 468 input placements/59 paths
    and empty stderr.
  snapshot_sha256: 3750202d7854c59f356f5457d2cd575fe90ad7b917d8a68b8830066c265ed6c2
- evidence_id: bgc-2761-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-target-input-plan-001.json
  locator: /records/0
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: Exact current input map with 0 direct companion paths and no reader requirement.
  snapshot_sha256: ac8ae699cd97a213089fe498a36b8be8628d507589a745a8812951d4d3b7c875
- evidence_id: bgc-2761-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch277/root-current277-input-plan-acceptance-001.json
  locator: /accepted; /plan; /source_placements; /unique_source_paths
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: ROOT accepted the actual current source input plan.
  snapshot_sha256: bad8b01739530276f7950a6678f2d16779bccde1f889aa76d00c64bc68fbf2c4
- evidence_id: bgc-2761-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch277/root-current277-five-gates-acceptance-001.json
  locator: /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /selected_queue_rows
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: Five local gates passed. Queue entries are bounded leads; full QC/OAK remain
    unavailable and gate passes do not establish biology.
  snapshot_sha256: 9901feaafa2853b49491c30af6bd92089777f81ce97d0de2637559ae9b93fadf
- evidence_id: bgc-2761-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-current277-assigned-source-reading-001.json
  locator: /contexts/4; /counts; /reading_attribution
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: All 3 positive source dictionaries/38 fields and 6 negative frames were
    read in the separately attributed source pass.
  snapshot_sha256: 45cf7141b5d2bbff977e6c26183b39740cb597c2618153c29e30bb22bd7fb546
- evidence_id: bgc-2761-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: Current 59 rows/679 fields retain BGC 32 and Support 27 primary-row attribution;
    Native/ROOT have zero primary-row credit.
  snapshot_sha256: ef54f2e0f2983f4946cb7dad5860dbab926d44ae52670018c6ddb0ba7667927b
- evidence_id: bgc-2761-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/native-prep/native-current277-cached-taxonomy-reading-002.json
  locator: /scope; /context_interpretations/4; /interpretation
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: Pseudomonas sp. RtIB026/NCBITaxon:2749999 remains a SOURCE_ASSERTION. The
    separate Pseudomonas/NCBITaxon:286 LOTUS label establishes neither the same strain
    nor demonstrated production. Cached stanzas contain no rank or lineage; no external
    taxonomy upgrade follows.
  snapshot_sha256: 61179ea49d70109a537134575a0a13b7e96006c52f579d2f5c9e3eee57ccc623
  search_scope: Exact current source-taxon route and retained cached names/synonyms;
    no inferred strain equivalence or hierarchy.
- evidence_id: bgc-2761-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/native-prep/native-current277-implemented-curation-scan-002.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: Native scanned nine substantive tables/3,422 rows. All 95 lexical candidates
    fail exact predicates, including 94 coordinate-token-only hits and one unresolved
    Macrophoma diagnostic. No applicable correction.
  snapshot_sha256: 4742551f0a1df52bb42f9cb950a44dc769caf7ecd18f9a211b4087a12403fa29
  search_scope: Current exact owner/source/occurrence/assay predicates over captured
    tables; two census-only inputs excluded.
- evidence_id: bgc-2761-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/native-prep/native-current277-implemented-curation-scan-002.json
  locator: /assay_scope
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: No actual PubChem AID or blank-AID sentinel belongs to this owner. ChEBI
    structures/origins, CyanoMetDB, BindingDB and AntibioticMech are bounded negative
    saved frames for this key. These local negatives establish neither global absence
    nor biological inactivity, potency or a molecular target.
  snapshot_sha256: 4742551f0a1df52bb42f9cb950a44dc769caf7ecd18f9a211b4087a12403fa29
  search_scope: No actual AIDs; only maklamicin has the retained blank sentinel. No
    other-owner evidence is transferred.
- evidence_id: bgc-2761-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters(includeUnassigned=True)'
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: stereo_complete tests unassigned atom-centred chirality; it does not certify
    every bond configuration or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2761-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines 295-306: choose_pathway'
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: One mapped pathway selects filing; zero or multiple labels retain UNCLASSIFIED
    while keeping all predictions.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2761-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 positive placements with every
    retained field and negative predicate read.'
  snapshot_sha256: 267b6fbbc5f7dc45be0500268071fac46ea2827523921ecece609fb9b2d02006
- evidence_id: bgc-2761-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 2932-2932; raw record sha256 6ca97ff947628e194b073504b6b8dbab30f95ba06315e2fbb3588370a7e41be5
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: All 25 fields read, preserving literal blanks, source qualifiers and citation
    grain.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2761-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: 'Complete saved chebi_structures frame: 0 positive placements with every
    retained field and negative predicate read.'
  snapshot_sha256: 267b6fbbc5f7dc45be0500268071fac46ea2827523921ecece609fb9b2d02006
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/ma026.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "UUNSGSIHFUBGCM-XVRKXJHRSA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2761-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 1 positive placements with every
    retained field and negative predicate read.'
  snapshot_sha256: 267b6fbbc5f7dc45be0500268071fac46ea2827523921ecece609fb9b2d02006
- evidence_id: bgc-2761-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 8916-8916; raw record sha256 2f7eaf0e7c2fc6b2bf688e6f61c753dad61c39288753e47375d67f1a53bb298d
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: All 6 fields read, preserving literal blanks, source qualifiers and citation
    grain.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2761-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences frame: 0 positive placements with
    every retained field and negative predicate read.'
  snapshot_sha256: 267b6fbbc5f7dc45be0500268071fac46ea2827523921ecece609fb9b2d02006
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/ma026.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "UUNSGSIHFUBGCM-XVRKXJHRSA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2761-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 positive placements with every retained
    field and negative predicate read.'
  snapshot_sha256: 267b6fbbc5f7dc45be0500268071fac46ea2827523921ecece609fb9b2d02006
- evidence_id: bgc-2761-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2465-2465; raw record sha256 0b6b811334ba302c2a50d4e78a70abc93324f9e96d8ca977250b955a14bc6210
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: supports
  summary: All 7 fields read, preserving literal blanks, source qualifiers and citation
    grain.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2761-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: 'Complete saved pubchem_bioassay frame: 0 positive placements with every
    retained field and negative predicate read.'
  snapshot_sha256: 267b6fbbc5f7dc45be0500268071fac46ea2827523921ecece609fb9b2d02006
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/ma026.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "UUNSGSIHFUBGCM-XVRKXJHRSA-N",
    "table": "pubchem_bioassay"}'
- evidence_id: bgc-2761-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets frame: 0 positive placements with every
    retained field and negative predicate read.'
  snapshot_sha256: 267b6fbbc5f7dc45be0500268071fac46ea2827523921ecece609fb9b2d02006
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/ma026.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "UUNSGSIHFUBGCM-XVRKXJHRSA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2761-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 positive placements with
    every retained field and negative predicate read.'
  snapshot_sha256: 267b6fbbc5f7dc45be0500268071fac46ea2827523921ecece609fb9b2d02006
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/ma026.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "UUNSGSIHFUBGCM-XVRKXJHRSA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2761-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch277-tentative/bgc-prep/bgc-conditional277-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T21:13:30.654133Z'
  support: context_only
  summary: 'Complete saved chebi_origins frame: 0 positive placements with every retained
    field and negative predicate read.'
  snapshot_sha256: 267b6fbbc5f7dc45be0500268071fac46ea2827523921ecece609fb9b2d02006
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/ma026.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-277/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-277/native-current277-five-gates-execution-001.json
  accessed_at: '2026-11-06T20:53:54.179777Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: e27bebda4f9fb1d03f5dff65a9461dc5d1a126013af8386b6a847ec1ac380873
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-277/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-277/native-current277-five-gates-execution-001.json
  accessed_at: '2026-11-06T20:54:18.416346Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: cec19f819c097cbc8a2117a28bf5ec0b812317ed0443aadfbf72d00b7d53a8af
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-277/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-277/native-current277-five-gates-execution-001.json
  accessed_at: '2026-11-06T20:54:37.558109Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-277/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-277/native-current277-five-gates-execution-001.json
  accessed_at: '2026-11-06T20:55:11.048142Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-277/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-277/native-current277-five-gates-execution-001.json
  accessed_at: '2026-11-06T20:55:22.530427Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: e14c50af5317dbe938a00f9a3e382149df9c7615ddb441f07512f7504488025e
assessments:
- assessment_id: bgc-2761-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: MA026 retains exact owner naturalproductmech:mibig-41bdd645a6, complete
    key UUNSGSIHFUBGCM-XVRKXJHRSA-N, and MIBiG BGC0002379 v3 compound index 1. Its
    retained cross-references (npatlas:NPA033064) are source-attributed, not remotely
    adjudicated. Both original forms normalize to C84H146N18O23 and the full declared
    key. The exact captured owner is resolved for this review; no broader family or
    similarly named target is substituted.
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  evidence_ids:
  - bgc-2761-identity
  - bgc-2761-chemistry
  - bgc-2761-query-mibig_compounds
  - bgc-2761-plan
  - bgc-2761-row-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    value: UUNSGSIHFUBGCM-XVRKXJHRSA-N
    evidence_ids:
    - bgc-2761-identity
    - bgc-2761-chemistry
    - bgc-2761-query-mibig_compounds
    - bgc-2761-plan
    - bgc-2761-row-mibig_compounds-0
  - name: grounding_scope
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    value: MA026 retains exact owner naturalproductmech:mibig-41bdd645a6, complete
      key UUNSGSIHFUBGCM-XVRKXJHRSA-N, and MIBiG BGC0002379 v3 compound index 1. Its
      retained cross-references (npatlas:NPA033064) are source-attributed, not remotely
      adjudicated. Both original forms normalize to C84H146N18O23 and the full declared
      key. The exact captured owner is resolved for this review; no broader family
      or similarly named target is substituted.
    evidence_ids:
    - bgc-2761-identity
    - bgc-2761-chemistry
    - bgc-2761-query-mibig_compounds
    - bgc-2761-plan
    - bgc-2761-row-mibig_compounds-0
- assessment_id: bgc-2761-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: Both saved forms contain 125 atoms and 125 bonds in one component. The
    SMILES graph has one 25-membered ester-containing peptide ring (saved ring 0),
    an acyclic hydroxyalkyl acyl chain, 18 amide sites and one free carboxyl group.
    The ring ester is C63(=O64)-O62-C61; the free acid is C24(=O25)-O26H. Four of
    the amides are terminal carboxamides at C33/C54/C76/C93, so the total amide count
    is not a residue count. This encoded topology supports a lipid-bearing cyclic
    depsipeptide scaffold without assigning every natural residue or its biosynthetic
    assembly. No C5O sugar-ring candidate is encoded. Both forms preserve six specified
    tetrahedral centres and ten unspecified tetrahedral centres. The six specified
    SMILES centres are C13/C21/C30/C39/C43/C51, all assigned S in the saved table.
    The partial /t layer and stereo_complete:false are consistent with the ten unassigned
    centres. The InChI reconstruction adds 18 unspecified C=N stereo potentials at
    its imidic sites; these are representation-dependent, not 18 unresolved carbon-carbon
    alkenes in the source SMILES. No natural stereochemistry is newly certified. Eighteen
    SMILES C(=O)-N sites become terminal C(OH)=N sites in the InChI reconstruction;
    each saved imidic oxygen has one hydrogen, and four terminal imidic nitrogens
    retain one hydrogen. Carbonyl/amide counts change from 20/18 to 2/0, while the
    ester and free acid remain. Formula, total charge, normalized Standard InChI and
    the full declared key agree. Both canonical SMILES comparisons are false and the
    limited map is empty, so exact graph identity is not established. This retained
    mobile-H representation difference alone is not a demonstrated source defect.
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  evidence_ids:
  - bgc-2761-identity
  - bgc-2761-chemistry
  - bgc-2761-molecular-reading
  - bgc-2761-diagnostic-acceptance
  - bgc-2761-diagnostic-stderr
  - bgc-2761-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    value: Both forms preserve six specified tetrahedral centres and ten unspecified
      tetrahedral centres. The six specified SMILES centres are C13/C21/C30/C39/C43/C51,
      all assigned S in the saved table. The partial /t layer and stereo_complete:false
      are consistent with the ten unassigned centres. The InChI reconstruction adds
      18 unspecified C=N stereo potentials at its imidic sites; these are representation-dependent,
      not 18 unresolved carbon-carbon alkenes in the source SMILES. No natural stereochemistry
      is newly certified.
    evidence_ids:
    - bgc-2761-identity
    - bgc-2761-chemistry
    - bgc-2761-molecular-reading
    - bgc-2761-diagnostic-acceptance
    - bgc-2761-diagnostic-stderr
    - bgc-2761-stereo-policy
  - name: representation_correspondence
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    value: Eighteen SMILES C(=O)-N sites become terminal C(OH)=N sites in the InChI
      reconstruction; each saved imidic oxygen has one hydrogen, and four terminal
      imidic nitrogens retain one hydrogen. Carbonyl/amide counts change from 20/18
      to 2/0, while the ester and free acid remain. Formula, total charge, normalized
      Standard InChI and the full declared key agree. Both canonical SMILES comparisons
      are false and the limited map is empty, so exact graph identity is not established.
      This retained mobile-H representation difference alone is not a demonstrated
      source defect.
    evidence_ids:
    - bgc-2761-identity
    - bgc-2761-chemistry
    - bgc-2761-molecular-reading
    - bgc-2761-diagnostic-acceptance
    - bgc-2761-diagnostic-stderr
    - bgc-2761-stereo-policy
- assessment_id: bgc-2761-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: Pseudomonas sp. RtIB026/NCBITaxon:2749999 remains a SOURCE_ASSERTION. The
    separate Pseudomonas/NCBITaxon:286 LOTUS label establishes neither the same strain
    nor demonstrated production. BGC0002379 v3 is active, questionable in quality
    and of unknown completeness. AP023348.1:3642436-3761997 remains CLUSTER_UNSTATED
    with no stated method; coordinates do not prove a demonstrated locus. Source NRPS/Type
    I is a cluster classification, not a complete MA026 pathway.
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  evidence_ids:
  - bgc-2761-provenance
  - bgc-2761-query-mibig_compounds
  - bgc-2761-taxonomy
  - bgc-2761-curation
  - bgc-2761-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    value: Pseudomonas sp. RtIB026/NCBITaxon:2749999 remains a SOURCE_ASSERTION. The
      separate Pseudomonas/NCBITaxon:286 LOTUS label establishes neither the same
      strain nor demonstrated production.
    evidence_ids:
    - bgc-2761-provenance
    - bgc-2761-query-mibig_compounds
    - bgc-2761-taxonomy
    - bgc-2761-curation
    - bgc-2761-row-mibig_compounds-0
  - name: producer_evidence
    definition: Producer evidence grade and its demonstrated or asserted scope.
    value: Pseudomonas sp. RtIB026/NCBITaxon:2749999 remains a SOURCE_ASSERTION. The
      separate Pseudomonas/NCBITaxon:286 LOTUS label establishes neither the same
      strain nor demonstrated production.
    evidence_ids:
    - bgc-2761-provenance
    - bgc-2761-query-mibig_compounds
    - bgc-2761-taxonomy
    - bgc-2761-curation
    - bgc-2761-row-mibig_compounds-0
  - name: locus_evidence
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    value: BGC0002379 v3 is active, questionable in quality and of unknown completeness.
      AP023348.1:3642436-3761997 remains CLUSTER_UNSTATED with no stated method; coordinates
      do not prove a demonstrated locus. Source NRPS/Type I is a cluster classification,
      not a complete MA026 pathway.
    evidence_ids:
    - bgc-2761-provenance
    - bgc-2761-query-mibig_compounds
    - bgc-2761-taxonomy
    - bgc-2761-curation
    - bgc-2761-row-mibig_compounds-0
- assessment_id: bgc-2761-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: PMID:33533101 retains MIBiG ENTRY citation grain. LOTUS DOI strings remain
    attached to their individual occurrence tuples; publication independence and underlying
    primary claims are not newly verified. All 2 history events are SEEDED_FROM_SOURCES
    and seeder-attributed.
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  evidence_ids:
  - bgc-2761-history
  - bgc-2761-source-reading
  - bgc-2761-query-mibig_compounds
  - bgc-2761-row-mibig_compounds-0
  - bgc-2761-row-lotus_occurrences-0
  dimensions:
  - name: citation_scope
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    value: PMID:33533101 retains MIBiG ENTRY citation grain. LOTUS DOI strings remain
      attached to their individual occurrence tuples; publication independence and
      underlying primary claims are not newly verified. All 2 history events are SEEDED_FROM_SOURCES
      and seeder-attributed.
    evidence_ids:
    - bgc-2761-history
    - bgc-2761-source-reading
    - bgc-2761-query-mibig_compounds
    - bgc-2761-row-mibig_compounds-0
    - bgc-2761-row-lotus_occurrences-0
- assessment_id: bgc-2761-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: The one retained LOTUS tuple reports Pseudomonas/NCBITaxon:286 with DOI:10.1002/ANGE.202015193.
    This remains evidence of a reported occurrence, separate from the strain-labelled
    MIBiG source assertion. No actual PubChem AID or blank-AID sentinel belongs to
    this owner. ChEBI structures/origins, CyanoMetDB, BindingDB and AntibioticMech
    are bounded negative saved frames for this key. These local negatives establish
    neither global absence nor biological inactivity, potency or a molecular target.
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  evidence_ids:
  - bgc-2761-roots
  - bgc-2761-query-lotus_occurrences
  - bgc-2761-query-chebi_origins
  - bgc-2761-query-cyanometdb_occurrences
  - bgc-2761-query-pubchem_bioassay
  - bgc-2761-query-bindingdb_targets
  - bgc-2761-query-antibioticmech_inchikeys
  - bgc-2761-assay-curation
  - bgc-2761-row-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    definition: Exact retained occurrence tuples and limits on production/independence.
    value: The one retained LOTUS tuple reports Pseudomonas/NCBITaxon:286 with DOI:10.1002/ANGE.202015193.
      This remains evidence of a reported occurrence, separate from the strain-labelled
      MIBiG source assertion.
    evidence_ids:
    - bgc-2761-roots
    - bgc-2761-query-lotus_occurrences
    - bgc-2761-query-chebi_origins
    - bgc-2761-query-cyanometdb_occurrences
    - bgc-2761-query-pubchem_bioassay
    - bgc-2761-query-bindingdb_targets
    - bgc-2761-query-antibioticmech_inchikeys
    - bgc-2761-assay-curation
    - bgc-2761-row-lotus_occurrences-0
  - name: assay_target_scope
    definition: Retained activity/assay/target positives and bounded negative queries.
    value: No actual PubChem AID or blank-AID sentinel belongs to this owner. ChEBI
      structures/origins, CyanoMetDB, BindingDB and AntibioticMech are bounded negative
      saved frames for this key. These local negatives establish neither global absence
      nor biological inactivity, potency or a molecular target.
    evidence_ids:
    - bgc-2761-roots
    - bgc-2761-query-lotus_occurrences
    - bgc-2761-query-chebi_origins
    - bgc-2761-query-cyanometdb_occurrences
    - bgc-2761-query-pubchem_bioassay
    - bgc-2761-query-bindingdb_targets
    - bgc-2761-query-antibioticmech_inchikeys
    - bgc-2761-assay-curation
    - bgc-2761-row-lotus_occurrences-0
- assessment_id: bgc-2761-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: NPClassifier npclassifier.gnps2.org@2026-09-07 predicts Amino acids and
    Peptides|Polyketides, Oligopeptides and Cyclic peptides|Depsipeptides|Lipopeptides;
    is_glycoside is false. The stored peptide bonds, cyclic ester and hydroxyalkyl
    acyl segment are compatible with those broad scaffold labels. Two pathway predictions
    correctly retain UNCLASSIFIED filing; the source compound_classes field is blank.
    Neither predictions nor topology identify a complete biological pathway.
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  evidence_ids:
  - bgc-2761-classification
  - bgc-2761-chemistry
  - bgc-2761-query-npclassifier
  - bgc-2761-query-mibig_compounds
  - bgc-2761-filing-policy
  - bgc-2761-row-npclassifier-0
  dimensions:
  - name: classification_applicability
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    value: NPClassifier npclassifier.gnps2.org@2026-09-07 predicts Amino acids and
      Peptides|Polyketides, Oligopeptides and Cyclic peptides|Depsipeptides|Lipopeptides;
      is_glycoside is false. The stored peptide bonds, cyclic ester and hydroxyalkyl
      acyl segment are compatible with those broad scaffold labels. Two pathway predictions
      correctly retain UNCLASSIFIED filing; the source compound_classes field is blank.
      Neither predictions nor topology identify a complete biological pathway.
    evidence_ids:
    - bgc-2761-classification
    - bgc-2761-chemistry
    - bgc-2761-query-npclassifier
    - bgc-2761-query-mibig_compounds
    - bgc-2761-filing-policy
    - bgc-2761-row-npclassifier-0
- assessment_id: bgc-2761-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: unknown
  summary: Whole current owner and its 2 seeder histories, all nine saved source frames
    (3 positive placements/38 fields and 6 negatives), and both complete original
    molecular tables were read. All 44 actual input hashes and maintained ownership
    declarations were joined; this is not a claim to have substantively read every
    entire input corpus. Five original local gates passed. Full QC/OAK, live source-authority
    checks and independent primary confirmation remain unavailable, so completion
    is partial. No literal graph/pathway/component/target root requires a maintained
    reader. Any later correction belongs in maintained inputs, applicable curation,
    extractors or the seeder.
  target_ids:
  - naturalproductmech:mibig-41bdd645a6
  evidence_ids:
  - bgc-2761-owner
  - bgc-2761-history
  - bgc-2761-intake
  - bgc-2761-intake-acceptance
  - bgc-2761-plan
  - bgc-2761-plan-acceptance
  - bgc-2761-gates
  - bgc-2761-source-reading
  - bgc-2761-source-notes
  - bgc-2761-molecular-reading
  - bgc-2761-roots
  dimensions:
  - name: review_completion
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    value: Whole current owner and its 2 seeder histories, all nine saved source frames
      (3 positive placements/38 fields and 6 negatives), and both complete original
      molecular tables were read. All 44 actual input hashes and maintained ownership
      declarations were joined; this is not a claim to have substantively read every
      entire input corpus. Five original local gates passed. Full QC/OAK, live source-authority
      checks and independent primary confirmation remain unavailable, so completion
      is partial. No literal graph/pathway/component/target root requires a maintained
      reader. Any later correction belongs in maintained inputs, applicable curation,
      extractors or the seeder.
    evidence_ids:
    - bgc-2761-owner
    - bgc-2761-history
    - bgc-2761-intake
    - bgc-2761-intake-acceptance
    - bgc-2761-plan
    - bgc-2761-plan-acceptance
    - bgc-2761-gates
    - bgc-2761-source-reading
    - bgc-2761-source-notes
    - bgc-2761-molecular-reading
    - bgc-2761-roots
findings: []
actions: []
limitations:
- External authority, primary publications, sequence-level and strain-level confirmation
  were not newly obtained. Full QC/OAK are unavailable; source assertions and source-level
  experimental grades remain attributed.
- Eighteen SMILES C(=O)-N sites become terminal C(OH)=N sites in the InChI reconstruction;
  each saved imidic oxygen has one hydrogen, and four terminal imidic nitrogens retain
  one hydrogen. Carbonyl/amide counts change from 20/18 to 2/0, while the ester and
  free acid remain. Formula, total charge, normalized Standard InChI and the full
  declared key agree. Both canonical SMILES comparisons are false and the limited
  map is empty, so exact graph identity is not established. This retained mobile-H
  representation difference alone is not a demonstrated source defect. The original
  two charge-rearrangement and two undefined-stereo warnings remain globally unassigned.
- Both forms preserve six specified tetrahedral centres and ten unspecified tetrahedral
  centres. The six specified SMILES centres are C13/C21/C30/C39/C43/C51, all assigned
  S in the saved table. The partial /t layer and stereo_complete:false are consistent
  with the ten unassigned centres. The InChI reconstruction adds 18 unspecified C=N
  stereo potentials at its imidic sites; these are representation-dependent, not 18
  unresolved carbon-carbon alkenes in the source SMILES. No natural stereochemistry
  is newly certified.
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
- batch-277
```
