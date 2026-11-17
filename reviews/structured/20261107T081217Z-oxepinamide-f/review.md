# Local evidence review: oxepinamide F

- Review: 20261107T081217Z-oxepinamide-f
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T07:42:09.792193Z
- Finished UTC: 2026-11-07T08:12:17.096727Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Oxepinamide F retains three specified atom centres and one secondary-amide/imidic representation difference, with the existing ring-ether O–C=N motif distinguished. Its OpaA/B/C/E/F graph preserves database-asserted transformations and explicitly ungrounded intermediates; historical sequence/product claims do not establish primary experiments. No material defect is established, and completion remains partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2852; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-97178951c1 | data/natural_products/unclassified/oxepinamide-f.yaml | generated | oxepinamide F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-97178951c1 | Both exact stored forms parsed in the sole original twenty-attempt diagnostic and agree in formula, charge, Standard InChI and declared complete key. |
| Complete offline maintained reader for oxepinamide-f | passed | True | naturalproductmech:mibig-97178951c1 | One original maintained reader preserves the complete owner, 1 graph, all graph evidence and 4 histories. |
| strict_ten | passed | True | naturalproductmech:mibig-97178951c1 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-97178951c1 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-97178951c1 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-97178951c1 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-97178951c1 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-97178951c1 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-97178951c1 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-97178951c1 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: naturalproductmech:mibig-97178951c1.

oxepinamide F retains exact identifier naturalproductmech:mibig-97178951c1, complete key HFZOLZVOTSSKSM-WSZRMNBISA-N, and BGC0002208 v3 compound index 1. Retained cross-references npatlas:NPA010066, pubchem:51003508 remain source-attributed identifiers, not fresh authority verification. Both saved forms normalize to C23H25N3O4 and the declared full key, while their canonical SMILES and limited atom map differ. Exact natural or tautomer identity is not established.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-97178951c1.

Both saved neutral C23H25N3O4 forms retain 30 heavy atoms and 33 bonds, with two six-membered heterocyclic rings, a seven-membered oxygen-containing ring and a separate benzene ring. The source form has two amides, including one tertiary nitrogen, a methoxy substituent and a sec-butyl side chain. Its pre-existing O–C=N motif contains a ring ether oxygen rather than an OH; it is distinct from the new imidic OH in the InChI-derived form. No source reaction, residue identity or exact natural conformation follows from these motifs. Both forms retain three specified tetrahedral centres, including the sec-butyl substituent centre, and no saved unspecified potential stereo entries. The source stereo_complete:true is compatible with the maintained atom-centre test. It does not validate upstream named intermediates, the historical product comparison or every possible natural conformer. The secondary amide at SMILES C27/N29 becomes InChI-derived C19(OH26)=N23; the tertiary amide carbonyl remains. The pre-existing ring-ether O–C=N site remains a separate motif, so two reported O–C=N motifs do not mean two amide-to-imidic shifts. Formula, charge, Standard InChI and complete key agree, but both canonical SMILES comparisons are false and the limited map is empty. No exact tautomer or full natural identity is established.

### Producer assertion versus locus evidence

provenance: supported. Targets: naturalproductmech:mibig-97178951c1.

BGC0002208 version 3 compound 1 attributes Aspergillus ustus NCBITaxon:40382 with SOURCE_ASSERTION. Questionable quality and unknown entry completeness remain explicit. Neither the historical graph strain reference nor the separate A. puniceus occurrence upgrades the retained producer evidence. The separate CLUSTER_UNSTATED locus is JOMC01000153.1:1113..31365, with no populated locus evidence method and ENTRY-level PMID:33004788. The retained OpaA/B/C/E/F annotations describe a database-asserted route; they do not convert the source locus into demonstrated experimental linkage.

### Citation grain and attributed history

evidence: supported. Targets: naturalproductmech:mibig-97178951c1.

BGC0002208: PMID:33004788 at ENTRY grain. These are retained database citations, not newly inspected primary bodies. Repeated placements do not establish independent experiments. All 4 complete histories were read, including 2 source-seeding events. The additional graph curation history records historical functional attribution, sequence comparison and product checking; those actions are not repeated or upgraded by the current reader.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: naturalproductmech:mibig-97178951c1.

One retained LOTUS claim names Aspergillus puniceus/41744 at DOI:10.1002/EJOC.201000812. It does not transfer the A. ustus genomic reference, source producer grade or enzymatic route to that occurrence organism. No actual AID or blank assay marker matches this owner in the saved PubChem frame. Exact-key BindingDB, AntibioticMech and CyanoMetDB frames and dependent ChEBI-origin scope are also negative. These bounded results do not prove inactivity or universal database absence.

### Computed filing and asserted class applicability

consistency: supported. Targets: naturalproductmech:mibig-97178951c1.

The retained NPClassifier model predicts Alkaloids&#124;Amino acids and Peptides, Peptide alkaloids and Other indole diketopiperazine alkaloids, with is_glycoside:false. These are model assertions, distinct from the source locus classes and actual encoded oxepin topology. Two pathway labels retain UNCLASSIFIED under choose_pathway; no curated reaction pathway is inferred.

### Local completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-97178951c1.

Complete current owner/history reading carries by exact raw/capture equality. All 4 histories, nine source frames (3 row placements/38 fields and 6 negatives), and both entire saved molecular forms were personally read. All 46 actual input hashes and maintained ownership paths join the accepted plan. Five original local gates passed; queue rows remain leads. The complete selected owner has one inline BIOSYNTHESIS graph and no pathway steps, component references, molecular targets, activity or related-corpus root. Its accepted original maintained reader preserves the entire owner; technical preservation is separate from scientific functional validation. Full QC/OAK and fresh source-authority or independent primary verification remain unavailable; completion is partial.

### Retained biosynthetic attribution and historical sequence/product verification limits

graph: supported. Targets: naturalproductmech:mibig-97178951c1.

The complete retained BIOSYNTHESIS graph has fifteen nodes and fourteen database-reported edges. OpaA is attributed assembly of protuboxepin K; OpaB oxepin-ring formation; OpaC hydroxylation with double-bond migration; OpaE conversion of the named 15-epi intermediate; and OpaF C-12 hydroxyl methylation to F. OpaF A0A0C1E5J2/KIA75453.1 remains distinct from OpaC A0A0C1BV72/KIA75456.1. The four upstream compound nodes remain ungrounded. The retained MITE OpaB example has an unspecified side-chain centre, and the OpaC example lacks stereochemical encoding; example flags do not establish exact intermediate identity or pathway finality. The five historical native-protein sequence comparisons and product-match claims are attributed to their dated curation notes, not independently reverified here; database evidence codes do not become inspected experiments. No kinetic, knockout, predicted-residue, physical-complex, transcript, construct or assay-stock claim is adopted. The complete current reader preserves the annotated route without validating its experimental function. No current external request or sequence comparison was performed; the separate stored-form diagnostic remains independently scoped.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2852-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/oxepinamide-f.yaml; Complete retained plaintext, all roots and history | supports | Complete owner reading carries from the pinned preview and exact current raw/capture equality. |
| bgc-2852-whole-owner-attribution | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-ten-owner-root-history-preview-001.json; /selected_records/1 | context_only | BGC Science personally read this whole owner and history; current equality carries that credit. |
| bgc-2852-identity | /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json; /records/1/owner_document/identifier; /records/1/owner_document/chemical_structure; /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status | supports | oxepinamide F retains exact identifier naturalproductmech:mibig-97178951c1, complete key HFZOLZVOTSSKSM-WSZRMNBISA-N, and BGC0002208 v3 compound index 1. Retained cross-references npatlas:NPA010066, pubchem:51003508 remain source-attributed identifiers, not fresh authority verification. Both saved forms normalize to C23H25N3O4 and the declared full key, while their canonical SMILES and limited atom map differ. Exact natural or tautomer identity is not established. |
| bgc-2852-history | /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json; /records/1/owner_document/curation_history | supports | BGC0002208: PMID:33004788 at ENTRY grain. These are retained database citations, not newly inspected primary bodies. Repeated placements do not establish independent experiments. All 4 complete histories were read, including 2 source-seeding events. The additional graph curation history records historical functional attribution, sequence comparison and product checking; those actions are not repeated or upgraded by the current reader. |
| bgc-2852-provenance | /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json; /records/1/owner_document/producer_organisms; /records/1/owner_document/biosynthetic_gene_clusters | supports | BGC0002208 version 3 compound 1 attributes Aspergillus ustus NCBITaxon:40382 with SOURCE_ASSERTION. Questionable quality and unknown entry completeness remain explicit. Neither the historical graph strain reference nor the separate A. puniceus occurrence upgrades the retained producer evidence. The separate CLUSTER_UNSTATED locus is JOMC01000153.1:1113..31365, with no populated locus evidence method and ENTRY-level PMID:33004788. The retained OpaA/B/C/E/F annotations describe a database-asserted route; they do not convert the source locus into demonstrated experimental linkage. |
| bgc-2852-classification | /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json; /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway; /records/1/owner_document/bgc_class | supports | The retained NPClassifier model predicts Alkaloids&#124;Amino acids and Peptides, Peptide alkaloids and Other indole diketopiperazine alkaloids, with is_glycoside:false. These are model assertions, distinct from the source locus classes and actual encoded oxepin topology. Two pathway labels retain UNCLASSIFIED under choose_pathway; no curated reaction pathway is inferred. |
| bgc-2852-roots | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/1/complete_root_keys; /contexts/1/declared_mechanism_roots_literal; /contexts/1/literal_bioactivities_root | context_only | The complete selected owner has one inline BIOSYNTHESIS graph and no pathway steps, component references, molecular targets, activity or related-corpus root. Its accepted original maintained reader preserves the entire owner; technical preservation is separate from scientific functional validation. |
| bgc-2852-chemistry | /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-DATA-001.json; /records/1/smiles/computed; /records/1/inchi/computed; /records/1/comparisons; /records/1/atom_correspondence | supports | Both saved neutral C23H25N3O4 forms retain 30 heavy atoms and 33 bonds, with two six-membered heterocyclic rings, a seven-membered oxygen-containing ring and a separate benzene ring. The source form has two amides, including one tertiary nitrogen, a methoxy substituent and a sec-butyl side chain. Its pre-existing O–C=N motif contains a ring ether oxygen rather than an OH; it is distinct from the new imidic OH in the InChI-derived form. No source reaction, residue identity or exact natural conformation follows from these motifs. Both forms retain three specified tetrahedral centres, including the sec-butyl substituent centre, and no saved unspecified potential stereo entries. The source stereo_complete:true is compatible with the maintained atom-centre test. It does not validate upstream named intermediates, the historical product comparison or every possible natural conformer. The secondary amide at SMILES C27/N29 becomes InChI-derived C19(OH26)=N23; the tertiary amide carbonyl remains. The pre-existing ring-ether O–C=N site remains a separate motif, so two reported O–C=N motifs do not mean two amide-to-imidic shifts. Formula, charge, Standard InChI and complete key agree, but both canonical SMILES comparisons are false and the limited map is empty. No exact tautomer or full natural identity is established. |
| bgc-2852-molecular-reading | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-current286-first-five-molecular-intake-reading-001.json; /records/1; /personal_reading_scope; /global_cautions | supports | All saved per-form tables and current intake meanings personally read without a new parse. |
| bgc-2852-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch286/root-current286-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /molecular_parse_attempts; /stderr_bytes; /scope | supports | ROOT accepted the sole twenty stored-form attempts with exact false comparisons preserved. |
| bgc-2852-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stderr | supports | Original diagnostic command, zero exit and empty stderr; no replay. |
| bgc-2852-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-original-001.stderr; Complete zero-byte original stderr | context_only | The complete original diagnostic stderr is empty. No record-specific or global warning is invented. |
| bgc-2852-intake | /private/tmp/npm-review-work/shared-next-batch286/intakes-001/2852-inspect-001.json; /targets; /source/inputs | supports | One exact target, 46 current input hashes and maintained ownership roles. |
| bgc-2852-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch286/root-current286-intake-acceptance-001.json; /accepted; /intake_summary; /records; /source_placements; /unique_source_paths | supports | Ten original inspections accepted with 474 placements across 55 paths. |
| bgc-2852-plan | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-target-input-plan-001.json; /records/1 | supports | Exact current map and 0 direct selected companions. |
| bgc-2852-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch286/root-current286-source-plan-acceptance-001.json; /accepted; /plan; /source_placements; /unique_source_paths | supports | ROOT accepted the actual current source input plan. |
| bgc-2852-gates | /private/tmp/npm-review-work/shared-next-batch286/root-current286-five-gates-acceptance-001.json; /five_local_commands_passed; /ledger; /denominators; /all_native_gates_passed; /unavailable_required_gates | context_only | Five original local gates passed; full QC/OAK remain unavailable and queue rows are leads. |
| bgc-2852-source-reading | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-current286-assigned-source-reading-001.json; /contexts/1; /counts; /reading_attribution | supports | All 3 complete row placements/38 fields, 6 negative frames and full histories personally read. |
| bgc-2852-source-notes | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-scope-notes-001.json; /totals; /reading_reconciliation; /reading_boundaries | context_only | Disjoint primary attribution is BGC 19 rows/229 fields plus Support 33/318, totaling 52/547. Native adds no named-source credit. |
| bgc-2852-taxonomy | /private/tmp/npm-review-work/shared-next-batch286-tentative/native-prep/native-current286-cached-taxonomy-reading-001.json; /scope; /context_interpretations/1; /interpretation | context_only | BGC0002208 version 3 compound 1 attributes Aspergillus ustus NCBITaxon:40382 with SOURCE_ASSERTION. Questionable quality and unknown entry completeness remain explicit. Neither the historical graph strain reference nor the separate A. puniceus occurrence upgrades the retained producer evidence. Exact cached names/synonyms remain separately attributed; no new rank, lineage or strain equivalence. |
| bgc-2852-curation | /private/tmp/npm-review-work/shared-next-batch286-tentative/native-prep/native-current286-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation | context_only | Native read nine substantive tables/3,422 rows and twenty current lexical candidates, with zero exact applicable decisions. Ninety-three unchanged decision rows carry by exact prior attribution; two reserved tables remain census-only. |
| bgc-2852-assay-curation | /private/tmp/npm-review-work/shared-next-batch286-tentative/native-prep/native-current286-implemented-curation-scan-001.json; /assay_scope | context_only | No actual AID or blank assay marker matches this owner in the saved PubChem frame. Exact-key BindingDB, AntibioticMech and CyanoMetDB frames and dependent ChEBI-origin scope are also negative. These bounded results do not prove inactivity or universal database absence. |
| bgc-2852-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters and the question-mark atom tag | context_only | The true flag tests unassigned atom-centred chirality; it does not promise all bond geometry or natural identity. |
| bgc-2852-stereo-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392-397: chemical_structure.stereo_complete | context_only | Undefined stereocentres remain recorded; no natural configuration is invented. |
| bgc-2852-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306: choose_pathway | context_only | One supported mapped pathway files the record; multiple, absent or unsupported results retain UNCLASSIFIED. |
| bgc-2852-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame with 1 row placements; all fields and bounded meanings read. |
| bgc-2852-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 2637-2637; raw record sha256 e4a0531b317ed1cd44a7110bdf37a44192d74fb51800a0fadcb61f984a81364a | supports | All 25 fields personally read, retaining blanks, source identity, grades and citation grain. |
| bgc-2852-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures frame with 0 row placements; all fields and bounded meanings read. |
| bgc-2852-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame with 1 row placements; all fields and bounded meanings read. |
| bgc-2852-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 2411-2411; raw record sha256 08334b92cf6aa67ca1653ff8d3c6665a961aa5dc57f6cf69492b9ebad2598101 | supports | All 6 fields personally read, retaining blanks, source identity, grades and citation grain. |
| bgc-2852-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences frame with 0 row placements; all fields and bounded meanings read. |
| bgc-2852-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame with 1 row placements; all fields and bounded meanings read. |
| bgc-2852-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 817-817; raw record sha256 5b84cb66237dd2d84ba62b8e52b63488fe9434b674e8e67fd79979f184bc57f0 | supports | All 7 fields personally read, retaining blanks, source identity, grades and citation grain. |
| bgc-2852-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/pubchem_bioassay | context_only | Complete saved pubchem_bioassay frame with 0 row placements; all fields and bounded meanings read. |
| bgc-2852-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets frame with 0 row placements; all fields and bounded meanings read. |
| bgc-2852-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys frame with 0 row placements; all fields and bounded meanings read. |
| bgc-2852-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins frame with 0 row placements; all fields and bounded meanings read. |
| bgc-2852-graph | /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json; /records/1/owner_document/causal_graphs; /records/1/owner_document/curation_history | supports | The complete retained BIOSYNTHESIS graph has fifteen nodes and fourteen database-reported edges. OpaA is attributed assembly of protuboxepin K; OpaB oxepin-ring formation; OpaC hydroxylation with double-bond migration; OpaE conversion of the named 15-epi intermediate; and OpaF C-12 hydroxyl methylation to F. OpaF A0A0C1E5J2/KIA75453.1 remains distinct from OpaC A0A0C1BV72/KIA75456.1. The four upstream compound nodes remain ungrounded. The retained MITE OpaB example has an unspecified side-chain centre, and the OpaC example lacks stereochemical encoding; example flags do not establish exact intermediate identity or pathway finality. The five historical native-protein sequence comparisons and product-match claims are attributed to their dated curation notes, not independently reverified here; database evidence codes do not become inspected experiments. No kinetic, knockout, predicted-residue, physical-complex, transcript, construct or assay-stock claim is adopted. The complete current reader preserves the annotated route without validating its experimental function. No current external request or sequence comparison was performed; the separate stored-form diagnostic remains independently scoped. |
| bgc-2852-reader-DATA | /private/tmp/npm-review-work/shared-next-batch286/native-current286-oxepinamide-f-maintained-reader-DATA-001.json; /resolved_view | supports | Complete original maintained view equals the entire personally read owner, with every graph, reference and history preserved. |
| bgc-2852-reader-execution | /private/tmp/npm-review-work/shared-next-batch286/native-current286-oxepinamide-f-reader-execution-001.json; /command; /exit_code | supports | Original reader command and zero exit; this author made no invocation. |
| bgc-2852-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch286/root-current286-oxepinamide-f-reader-acceptance-001.json; /accepted; /DATA; /execution; /review_check_contract | supports | ROOT accepted the original complete-owner maintained reader and exact check contract. |
| bgc-2852-reader-reading | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-current286-two-complete-maintained-reader-reading-001.json; /records/1; /scope | supports | Complete returned owner reading carries through exact equality to the personally read captured owner; functional validation remains separate. |
| bgc-2852-reference-availability | /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-current286-prior-authority-local-reference-preparation-001.json; /bounded_local_reference_search | context_only | Bounded local retained-reference availability only; no URLs fetched or universal absence claim. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-286/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-286/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-286/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-286/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-286/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Full QC/OAK and fresh primary, sequence, source-authority and strain verification remain unavailable. SOURCE_ASSERTION and CLUSTER_UNSTATED are not upgraded.
- The secondary amide at SMILES C27/N29 becomes InChI-derived C19(OH26)=N23; the tertiary amide carbonyl remains. The pre-existing ring-ether O–C=N site remains a separate motif, so two reported O–C=N motifs do not mean two amide-to-imidic shifts. Formula, charge, Standard InChI and complete key agree, but both canonical SMILES comparisons are false and the limited map is empty. No exact tautomer or full natural identity is established.
- Both forms retain three specified tetrahedral centres, including the sec-butyl substituent centre, and no saved unspecified potential stereo entries. The source stereo_complete:true is compatible with the maintained atom-centre test. It does not validate upstream named intermediates, the historical product comparison or every possible natural conformer.
- Local motifs and source classifications do not independently establish natural identity, complete biosynthetic reactions or pharmacological activity.
- The complete retained BIOSYNTHESIS graph has fifteen nodes and fourteen database-reported edges. OpaA is attributed assembly of protuboxepin K; OpaB oxepin-ring formation; OpaC hydroxylation with double-bond migration; OpaE conversion of the named 15-epi intermediate; and OpaF C-12 hydroxyl methylation to F. OpaF A0A0C1E5J2/KIA75453.1 remains distinct from OpaC A0A0C1BV72/KIA75456.1. The four upstream compound nodes remain ungrounded. The retained MITE OpaB example has an unspecified side-chain centre, and the OpaC example lacks stereochemical encoding; example flags do not establish exact intermediate identity or pathway finality. The five historical native-protein sequence comparisons and product-match claims are attributed to their dated curation notes, not independently reverified here; database evidence codes do not become inspected experiments. No kinetic, knockout, predicted-residue, physical-complex, transcript, construct or assay-stock claim is adopted. The complete current reader preserves the annotated route without validating its experimental function. No current external request or sequence comparison was performed; the separate stored-form diagnostic remains independently scoped.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- No record or source table is edited. Generated-field corrections, if justified later, belong in maintained inventory, implemented curation, extractor or seeder ownership; curated graph changes require the validated writer and attributed history.
- This author read retained original outputs only: no new molecular parse, sequence comparison, source query, maintained-reader invocation or external request.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T081217Z-oxepinamide-f
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: oxepinamide F'
started_at: '2026-11-07T07:42:09.792193Z'
finished_at: '2026-11-07T08:12:17.096727Z'
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
summary: Oxepinamide F retains three specified atom centres and one secondary-amide/imidic
  representation difference, with the existing ring-ether O–C=N motif distinguished.
  Its OpaA/B/C/E/F graph preserves database-asserted transformations and explicitly
  ungrounded intermediates; historical sequence/product claims do not establish primary
  experiments. No material defect is established, and completion remains partial.
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
  - path: data/natural_products/unclassified/oxepinamide-f.yaml
    sha256: 0d5b9f61e786586973d3e943ece51332ab00b9b5435a790f6c5d59f97ced1512
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
  selection: Campaign path order 2852; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-97178951c1
targets:
- target_id: naturalproductmech:mibig-97178951c1
  path: data/natural_products/unclassified/oxepinamide-f.yaml
  label: oxepinamide F
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
    path: data/natural_products/unclassified/oxepinamide-f.yaml
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnose286-001.py
    900fe8c8d280fbdd52892c2adbd241fe97c4163dd4dfba325ff9ce52a0f39abd deda858259c8e3df482e115d881fc4ab92d28aa7ff577fb2172fe55afb74327f
    584f3d16c0cf2e17d787e79e5575c82f88dfb3794618a63ae7b880ab965e66a2
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both exact stored forms parsed in the sole original twenty-attempt diagnostic
    and agree in formula, charge, Standard InChI and declared complete key.
  scope_note: The secondary amide at SMILES C27/N29 becomes InChI-derived C19(OH26)=N23;
    the tertiary amide carbonyl remains. The pre-existing ring-ether O–C=N site remains
    a separate motif, so two reported O–C=N motifs do not mean two amide-to-imidic
    shifts. Formula, charge, Standard InChI and complete key agree, but both canonical
    SMILES comparisons are false and the limited map is empty. No exact tautomer or
    full natural identity is established. The complete original diagnostic stderr
    is empty. No record-specific or global warning is invented.
  target_ids:
  - naturalproductmech:mibig-97178951c1
  evidence_ids:
  - bgc-2852-chemistry
  - bgc-2852-diagnostic-acceptance
  - bgc-2852-diagnostic-execution
  - bgc-2852-diagnostic-stderr
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for oxepinamide-f
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch286/read-selected-mechanism-guarded-001.py
    2852 584f3d16c0cf2e17d787e79e5575c82f88dfb3794618a63ae7b880ab965e66a2 861031c8f527aece2c028ce6f8f04a2550865caf2807333d4dd1b5900cb56619
    8b93627a36ff66bc2b4dfbee0215a08469fcdfd2f5effc3ce8bb52c837f57d4a deda858259c8e3df482e115d881fc4ab92d28aa7ff577fb2172fe55afb74327f
    900fe8c8d280fbdd52892c2adbd241fe97c4163dd4dfba325ff9ce52a0f39abd
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: One original maintained reader preserves the complete owner, 1 graph, all
    graph evidence and 4 histories.
  scope_note: Technical complete-owner preservation only. Historical sequence, database
    function and product assertions remain attributed; no primary experiment or natural
    identity is independently verified by the reader.
  target_ids:
  - naturalproductmech:mibig-97178951c1
  evidence_ids:
  - bgc-2852-reader-DATA
  - bgc-2852-reader-execution
  - bgc-2852-reader-acceptance
  - bgc-2852-graph
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-97178951c1
  command: just validate-strict data/natural_products/unclassified/oxepinamide-d.yaml
    data/natural_products/unclassified/oxepinamide-f.yaml data/natural_products/unclassified/pactamide-a.yaml
    data/natural_products/unclassified/pactamide-b.yaml data/natural_products/unclassified/pactamide-c.yaml
    data/natural_products/unclassified/pactamide-d.yaml data/natural_products/unclassified/pactamide-e.yaml
    data/natural_products/unclassified/pactamide-f.yaml data/natural_products/unclassified/paenibacterin.yaml
    data/natural_products/unclassified/paraherquamide.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-286/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-97178951c1
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-286/validate-all-001.tsv
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
  - naturalproductmech:mibig-97178951c1
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
  - naturalproductmech:mibig-97178951c1
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
  - naturalproductmech:mibig-97178951c1
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-286/review-queue-001.tsv
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
  - naturalproductmech:mibig-97178951c1
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-97178951c1
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-97178951c1
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2852-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/oxepinamide-f.yaml
  locator: Complete retained plaintext, all roots and history
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Complete owner reading carries from the pinned preview and exact current
    raw/capture equality.
  snapshot_sha256: 0d5b9f61e786586973d3e943ece51332ab00b9b5435a790f6c5d59f97ced1512
- evidence_id: bgc-2852-whole-owner-attribution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-ten-owner-root-history-preview-001.json
  locator: /selected_records/1
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: BGC Science personally read this whole owner and history; current equality
    carries that credit.
  snapshot_sha256: f723b47c8c53d41c3e2e8ced1412562baf30197e7ad896c50a3ffd086cbc9b71
- evidence_id: bgc-2852-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json
  locator: /records/1/owner_document/identifier; /records/1/owner_document/chemical_structure;
    /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: oxepinamide F retains exact identifier naturalproductmech:mibig-97178951c1,
    complete key HFZOLZVOTSSKSM-WSZRMNBISA-N, and BGC0002208 v3 compound index 1.
    Retained cross-references npatlas:NPA010066, pubchem:51003508 remain source-attributed
    identifiers, not fresh authority verification. Both saved forms normalize to C23H25N3O4
    and the declared full key, while their canonical SMILES and limited atom map differ.
    Exact natural or tautomer identity is not established.
  snapshot_sha256: deda858259c8e3df482e115d881fc4ab92d28aa7ff577fb2172fe55afb74327f
- evidence_id: bgc-2852-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json
  locator: /records/1/owner_document/curation_history
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: 'BGC0002208: PMID:33004788 at ENTRY grain. These are retained database
    citations, not newly inspected primary bodies. Repeated placements do not establish
    independent experiments. All 4 complete histories were read, including 2 source-seeding
    events. The additional graph curation history records historical functional attribution,
    sequence comparison and product checking; those actions are not repeated or upgraded
    by the current reader.'
  snapshot_sha256: deda858259c8e3df482e115d881fc4ab92d28aa7ff577fb2172fe55afb74327f
- evidence_id: bgc-2852-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json
  locator: /records/1/owner_document/producer_organisms; /records/1/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: BGC0002208 version 3 compound 1 attributes Aspergillus ustus NCBITaxon:40382
    with SOURCE_ASSERTION. Questionable quality and unknown entry completeness remain
    explicit. Neither the historical graph strain reference nor the separate A. puniceus
    occurrence upgrades the retained producer evidence. The separate CLUSTER_UNSTATED
    locus is JOMC01000153.1:1113..31365, with no populated locus evidence method and
    ENTRY-level PMID:33004788. The retained OpaA/B/C/E/F annotations describe a database-asserted
    route; they do not convert the source locus into demonstrated experimental linkage.
  snapshot_sha256: deda858259c8e3df482e115d881fc4ab92d28aa7ff577fb2172fe55afb74327f
- evidence_id: bgc-2852-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json
  locator: /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway;
    /records/1/owner_document/bgc_class
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: The retained NPClassifier model predicts Alkaloids|Amino acids and Peptides,
    Peptide alkaloids and Other indole diketopiperazine alkaloids, with is_glycoside:false.
    These are model assertions, distinct from the source locus classes and actual
    encoded oxepin topology. Two pathway labels retain UNCLASSIFIED under choose_pathway;
    no curated reaction pathway is inferred.
  snapshot_sha256: deda858259c8e3df482e115d881fc4ab92d28aa7ff577fb2172fe55afb74327f
- evidence_id: bgc-2852-roots
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/1/complete_root_keys; /contexts/1/declared_mechanism_roots_literal;
    /contexts/1/literal_bioactivities_root
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: The complete selected owner has one inline BIOSYNTHESIS graph and no pathway
    steps, component references, molecular targets, activity or related-corpus root.
    Its accepted original maintained reader preserves the entire owner; technical
    preservation is separate from scientific functional validation.
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: Complete exact selected owner root set; not a biological absence claim.
- evidence_id: bgc-2852-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/smiles/computed; /records/1/inchi/computed; /records/1/comparisons;
    /records/1/atom_correspondence
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Both saved neutral C23H25N3O4 forms retain 30 heavy atoms and 33 bonds,
    with two six-membered heterocyclic rings, a seven-membered oxygen-containing ring
    and a separate benzene ring. The source form has two amides, including one tertiary
    nitrogen, a methoxy substituent and a sec-butyl side chain. Its pre-existing O–C=N
    motif contains a ring ether oxygen rather than an OH; it is distinct from the
    new imidic OH in the InChI-derived form. No source reaction, residue identity
    or exact natural conformation follows from these motifs. Both forms retain three
    specified tetrahedral centres, including the sec-butyl substituent centre, and
    no saved unspecified potential stereo entries. The source stereo_complete:true
    is compatible with the maintained atom-centre test. It does not validate upstream
    named intermediates, the historical product comparison or every possible natural
    conformer. The secondary amide at SMILES C27/N29 becomes InChI-derived C19(OH26)=N23;
    the tertiary amide carbonyl remains. The pre-existing ring-ether O–C=N site remains
    a separate motif, so two reported O–C=N motifs do not mean two amide-to-imidic
    shifts. Formula, charge, Standard InChI and complete key agree, but both canonical
    SMILES comparisons are false and the limited map is empty. No exact tautomer or
    full natural identity is established.
  snapshot_sha256: 5c3cc60a877b9d858bd1076d34f37b57a5f0bc27c896aa121e3a58c370638a0a
- evidence_id: bgc-2852-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-current286-first-five-molecular-intake-reading-001.json
  locator: /records/1; /personal_reading_scope; /global_cautions
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: All saved per-form tables and current intake meanings personally read without
    a new parse.
  snapshot_sha256: 1690cc0a0abd016e8a9c9a455bba57dfe33ae4672959907e4ad620ab1a0977c4
- evidence_id: bgc-2852-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/root-current286-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /molecular_parse_attempts; /stderr_bytes;
    /scope
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: ROOT accepted the sole twenty stored-form attempts with exact false comparisons
    preserved.
  snapshot_sha256: 11c878f68a85192b33f7cfbb37505ae1e304a5c03ecf3d5284e3b60aa7834b85
- evidence_id: bgc-2852-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stderr
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Original diagnostic command, zero exit and empty stderr; no replay.
  snapshot_sha256: b7a36417331f165b8e9bf404bf5704cce0af5adf89a0aec75bc5d2018627680e
- evidence_id: bgc-2852-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/chemistry-local/diagnostic-original-001.stderr
  locator: Complete zero-byte original stderr
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: The complete original diagnostic stderr is empty. No record-specific or
    global warning is invented.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: bgc-2852-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/intakes-001/2852-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: One exact target, 46 current input hashes and maintained ownership roles.
  snapshot_sha256: 861031c8f527aece2c028ce6f8f04a2550865caf2807333d4dd1b5900cb56619
- evidence_id: bgc-2852-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/root-current286-intake-acceptance-001.json
  locator: /accepted; /intake_summary; /records; /source_placements; /unique_source_paths
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Ten original inspections accepted with 474 placements across 55 paths.
  snapshot_sha256: b8614bce387a2efc0cdf39025553707d4faf85909e5c68d7de84fb060f0038e5
- evidence_id: bgc-2852-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-target-input-plan-001.json
  locator: /records/1
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Exact current map and 0 direct selected companions.
  snapshot_sha256: 13a0a31f319999f8fa6e1fa57c7c927f238ea2df8c6035d3c04d440d5bf3e979
- evidence_id: bgc-2852-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/root-current286-source-plan-acceptance-001.json
  locator: /accepted; /plan; /source_placements; /unique_source_paths
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: ROOT accepted the actual current source input plan.
  snapshot_sha256: 9cb4d60ee03a72a21248d27eff29749732a31d3f88eb616c44eb0d83f0a72b4a
- evidence_id: bgc-2852-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/root-current286-five-gates-acceptance-001.json
  locator: /five_local_commands_passed; /ledger; /denominators; /all_native_gates_passed;
    /unavailable_required_gates
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Five original local gates passed; full QC/OAK remain unavailable and queue
    rows are leads.
  snapshot_sha256: be979d3983ecafe3575f15b24dd3837a9f87d8144daea3d73777c7911faab017
- evidence_id: bgc-2852-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-current286-assigned-source-reading-001.json
  locator: /contexts/1; /counts; /reading_attribution
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: All 3 complete row placements/38 fields, 6 negative frames and full histories
    personally read.
  snapshot_sha256: 8339fda9de3621f1fafeee85e3c8fb4edb78e6fc165a093b6eefd2c38bda67e0
- evidence_id: bgc-2852-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Disjoint primary attribution is BGC 19 rows/229 fields plus Support 33/318,
    totaling 52/547. Native adds no named-source credit.
  snapshot_sha256: d8c2be163249152840683342fb18d3cb0e7514aac521fc79f649070b797b05cd
- evidence_id: bgc-2852-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/native-prep/native-current286-cached-taxonomy-reading-001.json
  locator: /scope; /context_interpretations/1; /interpretation
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: BGC0002208 version 3 compound 1 attributes Aspergillus ustus NCBITaxon:40382
    with SOURCE_ASSERTION. Questionable quality and unknown entry completeness remain
    explicit. Neither the historical graph strain reference nor the separate A. puniceus
    occurrence upgrades the retained producer evidence. Exact cached names/synonyms
    remain separately attributed; no new rank, lineage or strain equivalence.
  snapshot_sha256: 75dda850603caeab4a4fd4e53fe37307d25b41d552eebe645019fffc3d25c098
  search_scope: Current retained taxon IDs, complete stanzas and exact saved forward/nonorganism
    scopes only.
- evidence_id: bgc-2852-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/native-prep/native-current286-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Native read nine substantive tables/3,422 rows and twenty current lexical
    candidates, with zero exact applicable decisions. Ninety-three unchanged decision
    rows carry by exact prior attribution; two reserved tables remain census-only.
  snapshot_sha256: 3d2309e330b55bfef215e5a0350a7f06ae8df548cf6c7bdd22ce675cb770b4e0
  search_scope: Exact owner/source-compound/BGC/full-key/occurrence/assay predicates;
    lexical similarity is not applicability.
- evidence_id: bgc-2852-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/native-prep/native-current286-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: No actual AID or blank assay marker matches this owner in the saved PubChem
    frame. Exact-key BindingDB, AntibioticMech and CyanoMetDB frames and dependent
    ChEBI-origin scope are also negative. These bounded results do not prove inactivity
    or universal database absence.
  snapshot_sha256: 3d2309e330b55bfef215e5a0350a7f06ae8df548cf6c7bdd22ce675cb770b4e0
  search_scope: Current exact full-key/CID scope, empty AIDs distinct from actual
    assays; no other-owner activity transfer.
- evidence_id: bgc-2852-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters and the question-mark atom tag'
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: The true flag tests unassigned atom-centred chirality; it does not promise
    all bond geometry or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2852-stereo-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: 'lines 392-397: chemical_structure.stereo_complete'
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Undefined stereocentres remain recorded; no natural configuration is invented.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2852-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines 295-306: choose_pathway'
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: One supported mapped pathway files the record; multiple, absent or unsupported
    results retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2852-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Complete saved mibig_compounds frame with 1 row placements; all fields
    and bounded meanings read.
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
- evidence_id: bgc-2852-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 2637-2637; raw record sha256 e4a0531b317ed1cd44a7110bdf37a44192d74fb51800a0fadcb61f984a81364a
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: All 25 fields personally read, retaining blanks, source identity, grades
    and citation grain.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2852-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Complete saved chebi_structures frame with 0 row placements; all fields
    and bounded meanings read.
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/oxepinamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "HFZOLZVOTSSKSM-WSZRMNBISA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2852-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Complete saved lotus_occurrences frame with 1 row placements; all fields
    and bounded meanings read.
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
- evidence_id: bgc-2852-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 2411-2411; raw record sha256 08334b92cf6aa67ca1653ff8d3c6665a961aa5dc57f6cf69492b9ebad2598101
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: All 6 fields personally read, retaining blanks, source identity, grades
    and citation grain.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2852-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Complete saved cyanometdb_occurrences frame with 0 row placements; all
    fields and bounded meanings read.
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/oxepinamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "HFZOLZVOTSSKSM-WSZRMNBISA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2852-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Complete saved npclassifier frame with 1 row placements; all fields and
    bounded meanings read.
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
- evidence_id: bgc-2852-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 817-817; raw record sha256 5b84cb66237dd2d84ba62b8e52b63488fe9434b674e8e67fd79979f184bc57f0
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: All 7 fields personally read, retaining blanks, source identity, grades
    and citation grain.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2852-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Complete saved pubchem_bioassay frame with 0 row placements; all fields
    and bounded meanings read.
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/oxepinamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "HFZOLZVOTSSKSM-WSZRMNBISA-N",
    "table": "pubchem_bioassay"}'
- evidence_id: bgc-2852-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Complete saved bindingdb_targets frame with 0 row placements; all fields
    and bounded meanings read.
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/oxepinamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "HFZOLZVOTSSKSM-WSZRMNBISA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2852-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Complete saved antibioticmech_inchikeys frame with 0 row placements; all
    fields and bounded meanings read.
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/oxepinamide-f.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "HFZOLZVOTSSKSM-WSZRMNBISA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2852-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-conditional286-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Complete saved chebi_origins frame with 0 row placements; all fields and
    bounded meanings read.
  snapshot_sha256: f2452165cd65efd00d84239e9699bb71e98528e9fa580133f8a39b9a61365b87
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/oxepinamide-f.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: bgc-2852-graph
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch286/owner-capture-DATA-001.json
  locator: /records/1/owner_document/causal_graphs; /records/1/owner_document/curation_history
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: The complete retained BIOSYNTHESIS graph has fifteen nodes and fourteen
    database-reported edges. OpaA is attributed assembly of protuboxepin K; OpaB oxepin-ring
    formation; OpaC hydroxylation with double-bond migration; OpaE conversion of the
    named 15-epi intermediate; and OpaF C-12 hydroxyl methylation to F. OpaF A0A0C1E5J2/KIA75453.1
    remains distinct from OpaC A0A0C1BV72/KIA75456.1. The four upstream compound nodes
    remain ungrounded. The retained MITE OpaB example has an unspecified side-chain
    centre, and the OpaC example lacks stereochemical encoding; example flags do not
    establish exact intermediate identity or pathway finality. The five historical
    native-protein sequence comparisons and product-match claims are attributed to
    their dated curation notes, not independently reverified here; database evidence
    codes do not become inspected experiments. No kinetic, knockout, predicted-residue,
    physical-complex, transcript, construct or assay-stock claim is adopted. The complete
    current reader preserves the annotated route without validating its experimental
    function. No current external request or sequence comparison was performed; the
    separate stored-form diagnostic remains independently scoped.
  snapshot_sha256: deda858259c8e3df482e115d881fc4ab92d28aa7ff577fb2172fe55afb74327f
- evidence_id: bgc-2852-reader-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/native-current286-oxepinamide-f-maintained-reader-DATA-001.json
  locator: /resolved_view
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Complete original maintained view equals the entire personally read owner,
    with every graph, reference and history preserved.
  snapshot_sha256: 4c1601d90ace30e44980f633229e8279440a54e86858b4f121285901a114766a
- evidence_id: bgc-2852-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/native-current286-oxepinamide-f-reader-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Original reader command and zero exit; this author made no invocation.
  snapshot_sha256: 1936fb7bfdc76ea63cafb26ea3f561c329574d7f6f617c5ce1dd1d4ff257bae9
- evidence_id: bgc-2852-reader-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286/root-current286-oxepinamide-f-reader-acceptance-001.json
  locator: /accepted; /DATA; /execution; /review_check_contract
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: ROOT accepted the original complete-owner maintained reader and exact check
    contract.
  snapshot_sha256: 50a232ae5d471e5f895846a0fdba1da33574461fe13d955e3e337abf849e23a3
- evidence_id: bgc-2852-reader-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-current286-two-complete-maintained-reader-reading-001.json
  locator: /records/1; /scope
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: supports
  summary: Complete returned owner reading carries through exact equality to the personally
    read captured owner; functional validation remains separate.
  snapshot_sha256: faac6846ce579747874e8fdfd1e126aab8570f1df75d8cfb7bc00df37645ab7f
- evidence_id: bgc-2852-reference-availability
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch286-tentative/bgc-prep/bgc-current286-prior-authority-local-reference-preparation-001.json
  locator: /bounded_local_reference_search
  accessed_at: '2026-11-07T08:06:31.234687Z'
  support: context_only
  summary: Bounded local retained-reference availability only; no URLs fetched or
    universal absence claim.
  snapshot_sha256: c33941f928d8856f4d7a8125431d93fde5f615fd21dca3c1f1009d8aec620f76
  search_scope: The referenced receipt records the precise ignored-inclusive filename
    roots and bounded content directories; its scope is not the entirety of workspace
    content.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-286/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json
  accessed_at: '2026-11-07T07:42:42.597912Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: f17e0cf2f7ffae5324b426cf095d627a5d9b16d8a6900938a2d86d33f01a8383
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-286/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json
  accessed_at: '2026-11-07T07:43:08.970157Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 809ff62f379495190e829e91f1ef111d41207c3b04672317dbaab7695f20763d
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-286/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json
  accessed_at: '2026-11-07T07:43:29.315088Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-286/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json
  accessed_at: '2026-11-07T07:44:05.084768Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-286/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-286/native-current286-five-gates-execution-001.json
  accessed_at: '2026-11-07T07:44:17.484589Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 3c72058344dc65e7aacd353aa6cbe966526faf56687259146ea8a0bdb7b36f86
assessments:
- assessment_id: bgc-2852-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: oxepinamide F retains exact identifier naturalproductmech:mibig-97178951c1,
    complete key HFZOLZVOTSSKSM-WSZRMNBISA-N, and BGC0002208 v3 compound index 1.
    Retained cross-references npatlas:NPA010066, pubchem:51003508 remain source-attributed
    identifiers, not fresh authority verification. Both saved forms normalize to C23H25N3O4
    and the declared full key, while their canonical SMILES and limited atom map differ.
    Exact natural or tautomer identity is not established.
  target_ids:
  - naturalproductmech:mibig-97178951c1
  evidence_ids:
  - bgc-2852-identity
  - bgc-2852-whole-owner-attribution
  - bgc-2852-chemistry
  - bgc-2852-query-mibig_compounds
  - bgc-2852-query-chebi_structures
  - bgc-2852-plan
  - bgc-2852-row-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    value: HFZOLZVOTSSKSM-WSZRMNBISA-N
    evidence_ids:
    - bgc-2852-identity
    - bgc-2852-whole-owner-attribution
    - bgc-2852-chemistry
    - bgc-2852-query-mibig_compounds
    - bgc-2852-query-chebi_structures
    - bgc-2852-plan
    - bgc-2852-row-mibig_compounds-0
  - name: grounding_scope
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    value: oxepinamide F retains exact identifier naturalproductmech:mibig-97178951c1,
      complete key HFZOLZVOTSSKSM-WSZRMNBISA-N, and BGC0002208 v3 compound index 1.
      Retained cross-references npatlas:NPA010066, pubchem:51003508 remain source-attributed
      identifiers, not fresh authority verification. Both saved forms normalize to
      C23H25N3O4 and the declared full key, while their canonical SMILES and limited
      atom map differ. Exact natural or tautomer identity is not established.
    evidence_ids:
    - bgc-2852-identity
    - bgc-2852-whole-owner-attribution
    - bgc-2852-chemistry
    - bgc-2852-query-mibig_compounds
    - bgc-2852-query-chebi_structures
    - bgc-2852-plan
    - bgc-2852-row-mibig_compounds-0
- assessment_id: bgc-2852-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: Both saved neutral C23H25N3O4 forms retain 30 heavy atoms and 33 bonds,
    with two six-membered heterocyclic rings, a seven-membered oxygen-containing ring
    and a separate benzene ring. The source form has two amides, including one tertiary
    nitrogen, a methoxy substituent and a sec-butyl side chain. Its pre-existing O–C=N
    motif contains a ring ether oxygen rather than an OH; it is distinct from the
    new imidic OH in the InChI-derived form. No source reaction, residue identity
    or exact natural conformation follows from these motifs. Both forms retain three
    specified tetrahedral centres, including the sec-butyl substituent centre, and
    no saved unspecified potential stereo entries. The source stereo_complete:true
    is compatible with the maintained atom-centre test. It does not validate upstream
    named intermediates, the historical product comparison or every possible natural
    conformer. The secondary amide at SMILES C27/N29 becomes InChI-derived C19(OH26)=N23;
    the tertiary amide carbonyl remains. The pre-existing ring-ether O–C=N site remains
    a separate motif, so two reported O–C=N motifs do not mean two amide-to-imidic
    shifts. Formula, charge, Standard InChI and complete key agree, but both canonical
    SMILES comparisons are false and the limited map is empty. No exact tautomer or
    full natural identity is established.
  target_ids:
  - naturalproductmech:mibig-97178951c1
  evidence_ids:
  - bgc-2852-identity
  - bgc-2852-chemistry
  - bgc-2852-molecular-reading
  - bgc-2852-diagnostic-acceptance
  - bgc-2852-diagnostic-stderr
  - bgc-2852-stereo-policy
  - bgc-2852-stereo-schema
  dimensions:
  - name: stereochemistry_scope
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    value: Both forms retain three specified tetrahedral centres, including the sec-butyl
      substituent centre, and no saved unspecified potential stereo entries. The source
      stereo_complete:true is compatible with the maintained atom-centre test. It
      does not validate upstream named intermediates, the historical product comparison
      or every possible natural conformer.
    evidence_ids:
    - bgc-2852-identity
    - bgc-2852-chemistry
    - bgc-2852-molecular-reading
    - bgc-2852-diagnostic-acceptance
    - bgc-2852-diagnostic-stderr
    - bgc-2852-stereo-policy
    - bgc-2852-stereo-schema
  - name: representation_correspondence
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    value: The secondary amide at SMILES C27/N29 becomes InChI-derived C19(OH26)=N23;
      the tertiary amide carbonyl remains. The pre-existing ring-ether O–C=N site
      remains a separate motif, so two reported O–C=N motifs do not mean two amide-to-imidic
      shifts. Formula, charge, Standard InChI and complete key agree, but both canonical
      SMILES comparisons are false and the limited map is empty. No exact tautomer
      or full natural identity is established.
    evidence_ids:
    - bgc-2852-identity
    - bgc-2852-chemistry
    - bgc-2852-molecular-reading
    - bgc-2852-diagnostic-acceptance
    - bgc-2852-diagnostic-stderr
    - bgc-2852-stereo-policy
    - bgc-2852-stereo-schema
- assessment_id: bgc-2852-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: BGC0002208 version 3 compound 1 attributes Aspergillus ustus NCBITaxon:40382
    with SOURCE_ASSERTION. Questionable quality and unknown entry completeness remain
    explicit. Neither the historical graph strain reference nor the separate A. puniceus
    occurrence upgrades the retained producer evidence. The separate CLUSTER_UNSTATED
    locus is JOMC01000153.1:1113..31365, with no populated locus evidence method and
    ENTRY-level PMID:33004788. The retained OpaA/B/C/E/F annotations describe a database-asserted
    route; they do not convert the source locus into demonstrated experimental linkage.
  target_ids:
  - naturalproductmech:mibig-97178951c1
  evidence_ids:
  - bgc-2852-provenance
  - bgc-2852-query-mibig_compounds
  - bgc-2852-taxonomy
  - bgc-2852-curation
  - bgc-2852-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    value: BGC0002208 version 3 compound 1 attributes Aspergillus ustus NCBITaxon:40382
      with SOURCE_ASSERTION. Questionable quality and unknown entry completeness remain
      explicit. Neither the historical graph strain reference nor the separate A.
      puniceus occurrence upgrades the retained producer evidence.
    evidence_ids:
    - bgc-2852-provenance
    - bgc-2852-query-mibig_compounds
    - bgc-2852-taxonomy
    - bgc-2852-curation
    - bgc-2852-row-mibig_compounds-0
  - name: producer_evidence
    definition: Producer evidence grade and its demonstrated or asserted scope.
    value: BGC0002208 version 3 compound 1 attributes Aspergillus ustus NCBITaxon:40382
      with SOURCE_ASSERTION. Questionable quality and unknown entry completeness remain
      explicit. Neither the historical graph strain reference nor the separate A.
      puniceus occurrence upgrades the retained producer evidence.
    evidence_ids:
    - bgc-2852-provenance
    - bgc-2852-query-mibig_compounds
    - bgc-2852-taxonomy
    - bgc-2852-curation
    - bgc-2852-row-mibig_compounds-0
  - name: locus_evidence
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    value: The separate CLUSTER_UNSTATED locus is JOMC01000153.1:1113..31365, with
      no populated locus evidence method and ENTRY-level PMID:33004788. The retained
      OpaA/B/C/E/F annotations describe a database-asserted route; they do not convert
      the source locus into demonstrated experimental linkage.
    evidence_ids:
    - bgc-2852-provenance
    - bgc-2852-query-mibig_compounds
    - bgc-2852-taxonomy
    - bgc-2852-curation
    - bgc-2852-row-mibig_compounds-0
- assessment_id: bgc-2852-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: 'BGC0002208: PMID:33004788 at ENTRY grain. These are retained database
    citations, not newly inspected primary bodies. Repeated placements do not establish
    independent experiments. All 4 complete histories were read, including 2 source-seeding
    events. The additional graph curation history records historical functional attribution,
    sequence comparison and product checking; those actions are not repeated or upgraded
    by the current reader.'
  target_ids:
  - naturalproductmech:mibig-97178951c1
  evidence_ids:
  - bgc-2852-history
  - bgc-2852-source-reading
  - bgc-2852-query-mibig_compounds
  - bgc-2852-row-mibig_compounds-0
  - bgc-2852-row-lotus_occurrences-0
  dimensions:
  - name: citation_scope
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    value: 'BGC0002208: PMID:33004788 at ENTRY grain. These are retained database
      citations, not newly inspected primary bodies. Repeated placements do not establish
      independent experiments. All 4 complete histories were read, including 2 source-seeding
      events. The additional graph curation history records historical functional
      attribution, sequence comparison and product checking; those actions are not
      repeated or upgraded by the current reader.'
    evidence_ids:
    - bgc-2852-history
    - bgc-2852-source-reading
    - bgc-2852-query-mibig_compounds
    - bgc-2852-row-mibig_compounds-0
    - bgc-2852-row-lotus_occurrences-0
- assessment_id: bgc-2852-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: One retained LOTUS claim names Aspergillus puniceus/41744 at DOI:10.1002/EJOC.201000812.
    It does not transfer the A. ustus genomic reference, source producer grade or
    enzymatic route to that occurrence organism. No actual AID or blank assay marker
    matches this owner in the saved PubChem frame. Exact-key BindingDB, AntibioticMech
    and CyanoMetDB frames and dependent ChEBI-origin scope are also negative. These
    bounded results do not prove inactivity or universal database absence.
  target_ids:
  - naturalproductmech:mibig-97178951c1
  evidence_ids:
  - bgc-2852-roots
  - bgc-2852-query-lotus_occurrences
  - bgc-2852-query-chebi_origins
  - bgc-2852-query-cyanometdb_occurrences
  - bgc-2852-query-pubchem_bioassay
  - bgc-2852-query-bindingdb_targets
  - bgc-2852-query-antibioticmech_inchikeys
  - bgc-2852-assay-curation
  - bgc-2852-row-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    definition: Exact retained occurrence tuples and limits on production/independence.
    value: One retained LOTUS claim names Aspergillus puniceus/41744 at DOI:10.1002/EJOC.201000812.
      It does not transfer the A. ustus genomic reference, source producer grade or
      enzymatic route to that occurrence organism.
    evidence_ids:
    - bgc-2852-roots
    - bgc-2852-query-lotus_occurrences
    - bgc-2852-query-chebi_origins
    - bgc-2852-query-cyanometdb_occurrences
    - bgc-2852-query-pubchem_bioassay
    - bgc-2852-query-bindingdb_targets
    - bgc-2852-query-antibioticmech_inchikeys
    - bgc-2852-assay-curation
    - bgc-2852-row-lotus_occurrences-0
  - name: assay_target_scope
    definition: Retained activity/assay/target positives and bounded negative queries.
    value: No actual AID or blank assay marker matches this owner in the saved PubChem
      frame. Exact-key BindingDB, AntibioticMech and CyanoMetDB frames and dependent
      ChEBI-origin scope are also negative. These bounded results do not prove inactivity
      or universal database absence.
    evidence_ids:
    - bgc-2852-roots
    - bgc-2852-query-lotus_occurrences
    - bgc-2852-query-chebi_origins
    - bgc-2852-query-cyanometdb_occurrences
    - bgc-2852-query-pubchem_bioassay
    - bgc-2852-query-bindingdb_targets
    - bgc-2852-query-antibioticmech_inchikeys
    - bgc-2852-assay-curation
    - bgc-2852-row-lotus_occurrences-0
- assessment_id: bgc-2852-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: The retained NPClassifier model predicts Alkaloids|Amino acids and Peptides,
    Peptide alkaloids and Other indole diketopiperazine alkaloids, with is_glycoside:false.
    These are model assertions, distinct from the source locus classes and actual
    encoded oxepin topology. Two pathway labels retain UNCLASSIFIED under choose_pathway;
    no curated reaction pathway is inferred.
  target_ids:
  - naturalproductmech:mibig-97178951c1
  evidence_ids:
  - bgc-2852-classification
  - bgc-2852-chemistry
  - bgc-2852-query-npclassifier
  - bgc-2852-query-mibig_compounds
  - bgc-2852-filing-policy
  - bgc-2852-row-npclassifier-0
  - bgc-2852-row-mibig_compounds-0
  dimensions:
  - name: classification_applicability
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    value: The retained NPClassifier model predicts Alkaloids|Amino acids and Peptides,
      Peptide alkaloids and Other indole diketopiperazine alkaloids, with is_glycoside:false.
      These are model assertions, distinct from the source locus classes and actual
      encoded oxepin topology. Two pathway labels retain UNCLASSIFIED under choose_pathway;
      no curated reaction pathway is inferred.
    evidence_ids:
    - bgc-2852-classification
    - bgc-2852-chemistry
    - bgc-2852-query-npclassifier
    - bgc-2852-query-mibig_compounds
    - bgc-2852-filing-policy
    - bgc-2852-row-npclassifier-0
    - bgc-2852-row-mibig_compounds-0
- assessment_id: bgc-2852-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: unknown
  summary: Complete current owner/history reading carries by exact raw/capture equality.
    All 4 histories, nine source frames (3 row placements/38 fields and 6 negatives),
    and both entire saved molecular forms were personally read. All 46 actual input
    hashes and maintained ownership paths join the accepted plan. Five original local
    gates passed; queue rows remain leads. The complete selected owner has one inline
    BIOSYNTHESIS graph and no pathway steps, component references, molecular targets,
    activity or related-corpus root. Its accepted original maintained reader preserves
    the entire owner; technical preservation is separate from scientific functional
    validation. Full QC/OAK and fresh source-authority or independent primary verification
    remain unavailable; completion is partial.
  target_ids:
  - naturalproductmech:mibig-97178951c1
  evidence_ids:
  - bgc-2852-owner
  - bgc-2852-whole-owner-attribution
  - bgc-2852-history
  - bgc-2852-intake
  - bgc-2852-intake-acceptance
  - bgc-2852-plan
  - bgc-2852-plan-acceptance
  - bgc-2852-gates
  - bgc-2852-source-reading
  - bgc-2852-source-notes
  - bgc-2852-molecular-reading
  - bgc-2852-roots
  - bgc-2852-graph
  - bgc-2852-reader-DATA
  - bgc-2852-reader-execution
  - bgc-2852-reader-acceptance
  - bgc-2852-reader-reading
  - bgc-2852-reference-availability
  dimensions:
  - name: review_completion
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    value: Complete current owner/history reading carries by exact raw/capture equality.
      All 4 histories, nine source frames (3 row placements/38 fields and 6 negatives),
      and both entire saved molecular forms were personally read. All 46 actual input
      hashes and maintained ownership paths join the accepted plan. Five original
      local gates passed; queue rows remain leads. The complete selected owner has
      one inline BIOSYNTHESIS graph and no pathway steps, component references, molecular
      targets, activity or related-corpus root. Its accepted original maintained reader
      preserves the entire owner; technical preservation is separate from scientific
      functional validation. Full QC/OAK and fresh source-authority or independent
      primary verification remain unavailable; completion is partial.
    evidence_ids:
    - bgc-2852-owner
    - bgc-2852-whole-owner-attribution
    - bgc-2852-history
    - bgc-2852-intake
    - bgc-2852-intake-acceptance
    - bgc-2852-plan
    - bgc-2852-plan-acceptance
    - bgc-2852-gates
    - bgc-2852-source-reading
    - bgc-2852-source-notes
    - bgc-2852-molecular-reading
    - bgc-2852-roots
    - bgc-2852-graph
    - bgc-2852-reader-DATA
    - bgc-2852-reader-execution
    - bgc-2852-reader-acceptance
    - bgc-2852-reader-reading
    - bgc-2852-reference-availability
- assessment_id: bgc-2852-graph
  area: graph
  topic: Retained biosynthetic attribution and historical sequence/product verification
    limits
  outcome: supported
  summary: The complete retained BIOSYNTHESIS graph has fifteen nodes and fourteen
    database-reported edges. OpaA is attributed assembly of protuboxepin K; OpaB oxepin-ring
    formation; OpaC hydroxylation with double-bond migration; OpaE conversion of the
    named 15-epi intermediate; and OpaF C-12 hydroxyl methylation to F. OpaF A0A0C1E5J2/KIA75453.1
    remains distinct from OpaC A0A0C1BV72/KIA75456.1. The four upstream compound nodes
    remain ungrounded. The retained MITE OpaB example has an unspecified side-chain
    centre, and the OpaC example lacks stereochemical encoding; example flags do not
    establish exact intermediate identity or pathway finality. The five historical
    native-protein sequence comparisons and product-match claims are attributed to
    their dated curation notes, not independently reverified here; database evidence
    codes do not become inspected experiments. No kinetic, knockout, predicted-residue,
    physical-complex, transcript, construct or assay-stock claim is adopted. The complete
    current reader preserves the annotated route without validating its experimental
    function. No current external request or sequence comparison was performed; the
    separate stored-form diagnostic remains independently scoped.
  target_ids:
  - naturalproductmech:mibig-97178951c1
  evidence_ids:
  - bgc-2852-graph
  - bgc-2852-reader-DATA
  - bgc-2852-reader-execution
  - bgc-2852-reader-acceptance
  - bgc-2852-reader-reading
  - bgc-2852-reference-availability
  - bgc-2852-source-reading
  - bgc-2852-history
  dimensions: []
findings: []
actions: []
limitations:
- Full QC/OAK and fresh primary, sequence, source-authority and strain verification
  remain unavailable. SOURCE_ASSERTION and CLUSTER_UNSTATED are not upgraded.
- The secondary amide at SMILES C27/N29 becomes InChI-derived C19(OH26)=N23; the tertiary
  amide carbonyl remains. The pre-existing ring-ether O–C=N site remains a separate
  motif, so two reported O–C=N motifs do not mean two amide-to-imidic shifts. Formula,
  charge, Standard InChI and complete key agree, but both canonical SMILES comparisons
  are false and the limited map is empty. No exact tautomer or full natural identity
  is established.
- Both forms retain three specified tetrahedral centres, including the sec-butyl substituent
  centre, and no saved unspecified potential stereo entries. The source stereo_complete:true
  is compatible with the maintained atom-centre test. It does not validate upstream
  named intermediates, the historical product comparison or every possible natural
  conformer.
- Local motifs and source classifications do not independently establish natural identity,
  complete biosynthetic reactions or pharmacological activity.
- The complete retained BIOSYNTHESIS graph has fifteen nodes and fourteen database-reported
  edges. OpaA is attributed assembly of protuboxepin K; OpaB oxepin-ring formation;
  OpaC hydroxylation with double-bond migration; OpaE conversion of the named 15-epi
  intermediate; and OpaF C-12 hydroxyl methylation to F. OpaF A0A0C1E5J2/KIA75453.1
  remains distinct from OpaC A0A0C1BV72/KIA75456.1. The four upstream compound nodes
  remain ungrounded. The retained MITE OpaB example has an unspecified side-chain
  centre, and the OpaC example lacks stereochemical encoding; example flags do not
  establish exact intermediate identity or pathway finality. The five historical native-protein
  sequence comparisons and product-match claims are attributed to their dated curation
  notes, not independently reverified here; database evidence codes do not become
  inspected experiments. No kinetic, knockout, predicted-residue, physical-complex,
  transcript, construct or assay-stock claim is adopted. The complete current reader
  preserves the annotated route without validating its experimental function. No current
  external request or sequence comparison was performed; the separate stored-form
  diagnostic remains independently scoped.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- No record or source table is edited. Generated-field corrections, if justified later,
  belong in maintained inventory, implemented curation, extractor or seeder ownership;
  curated graph changes require the validated writer and attributed history.
- 'This author read retained original outputs only: no new molecular parse, sequence
  comparison, source query, maintained-reader invocation or external request.'
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-286
```
