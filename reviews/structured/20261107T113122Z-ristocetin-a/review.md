# Review Ristocetin A against retained local evidence

- Review: 20261107T113122Z-ristocetin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T11:21:22.782398Z
- Finished UTC: 2026-11-07T11:31:22.525768Z
- Reviewer: Codex ROOT with Bgc/Support scientific reviewers and Native local checks (unknown)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Ristocetin A: the retained identity, chemical topology and explicitly graded source assertions are locally coherent. The review is partial; source-limited producer/occurrence evidence, representation differences and unperformed external checks remain explicit.

## Scope And Provenance

Complete local reading of this one selected owner, its history and any declared mechanism components; scientific verification remains partial. The current campaign corpus contains 3136 records.

Selection: Batch289, order 2889: one of the first ten sorted currently unreviewed paths in the reconciled catalogue (1768 covered,1368 remaining before this batch). This bundle assesses only this target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 18ca5dd6b9023670f10355084b45a8757a7a4e9e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:85129 | data/natural_products/amino_acids_and_peptides/ristocetin-a.yaml | generated | Ristocetin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical target and source capture | passed | True | CHEBI:85129 | Captured this exact generated target and its regular-file source inputs at the selected fresh main commit; current input hashes remain unchanged. |
| Maintained local gate: strict_ten | passed | True | CHEBI:85129 | All ten selected whole owners passed closed validation; zero error rows. |
| Maintained local gate: strict_full | passed | True | CHEBI:85129 | All 3136 current owners passed full closed validation with component-inventory audit; zero error rows. |
| Maintained local gate: lockfile | passed | True | CHEBI:85129 | All 3136 owner paths agree with PATHS.tsv and filing pins, including component inventory checks. |
| Maintained local gate: reproduction | passed | True | CHEBI:85129 | All 3136 records are byte-identical to the current seeder output. Carried curator mechanism claims are preserved, not independently proven. |
| Maintained local gate: queue | passed | True | CHEBI:85129 | The complete current review queue was generated locally: 8919 rows across 12 queues. Queue membership does not establish scientific review. |
| Local stored-form molecular diagnostic | passed | True | CHEBI:85129 | Exactly two stored encodings were parsed for this record (20 across the batch). Their normalized Standard InChI, key, computed formula and net charge agree; graph/canonical-SMILES equivalence and natural sample identity are not inferred. Record-specific differences remain in the scientific assessments. |
| Complete maintained mechanism read | not_applicable | False | CHEBI:85129 | The fully read owner has no graph, component-reference, pathway or molecular-target roots. No maintained mechanism-reader call was made for this target. The absence of these optional roots is not itself a scientific defect. |
| Full repository QC | unavailable | True | CHEBI:85129 | Not run: maintained full QC reaches the vendored-sync fetch. The five local gates do not substitute for full QC. |
| Complete OAK identifier-label correspondence | unavailable | True | CHEBI:85129 | Not run: a complete pinned offline CHEBI/GO adapter boundary was not established. No ontology download or remote resolver was permitted. |
| Fresh source, literature, taxonomy and structured database verification | unavailable | True | CHEBI:85129 | Not run under the source-request hold. Database assertions, gene/pathway annotations, citations, exact forms and strain claims are assessed only against retained local evidence; no fresh resolution or primary-paper authentication is claimed. |

## Scientific And Domain Assessments

### Exact source identity and direct-congener boundary

identity: supported. Targets: CHEBI:85129.

CHEBI:85129, the complete VUOPFFVAZTUEGW-FBMDODLCSA-N key and MIBiG BGC0000418 compound 1 join the selected Ristocetin A owner. The retained ChEBI label is the generic ristocetin; conf/id_label_targets.yaml explicitly allows the exact CHEBI:85129/Ristocetin A name variant with curator confirmation still noted. This known local exception is not treated as fresh resolution of the generic-name ambiguity. Ristocetin B and both desmethyl owners retain different full keys/formulas.

### Complete saved chemical forms and stereochemistry

representation: supported. Targets: CHEBI:85129.

Both saved neutral C95H110N8O44 forms contain 147 atoms and 163 bonds. The crosslinked glycopeptide scaffold contains seven aromatic six-member rings and six saturated C5O ring motifs connected through oxygen bridges. Nineteen saved symmetric-SSSR ring rows are not nineteen independent cycles; the connected graph has cycle rank 17. Six secondary amides become six C(OH)=N sites in the saved InChI form. The methyl ester remains: SMILES C141(=O142)–O143–C144 and InChI C89(=O130)–O131–C3; it is not a free terminal acid. Both forms retain 36 specified and one unspecified tetrahedral centre. The unknown centre is an acetal-like C–H with two oxygen neighbours in a C5O ring (SMILES C56; InChI C90). This agrees with stereo_complete:false and does not supply a natural anomer assignment. Six extra unspecified InChI C=N candidates belong to the imidic representations. Candidate C5O motifs and bridge topology alone do not assign sugar names, linkage positions or natural configuration. Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized Standard InChI/key, declared key, formula, charge and atom/bond counts agree. The saved chirality-aware atom map is empty and full_graph_identity_established is false. The explicit motif changes explain a representation difference but do not establish full graph or natural-sample identity.

### Producer grade, locus method and occurrence grain

provenance: supported. Targets: CHEBI:85129.

BGC0000418 v5 records SOURCE_ASSERTION Amycolatopsis lurida, NCBITaxon:31959, and CLUSTER_UNSTATED linkage with no locus methods or coordinates. Separate ChEBI occurrences retain NCBITaxon:1460371 at NRRL 2430 strain scope (cached name Amycolatopsis lurida NRRL 2430; PMID:25323720) and Amycolatopsis sp. NCBITaxon:37632, strain MJM2582 (PMID:25359910). LOTUS's Nocardia occurrence, DOI:10.1039/C39790000906, is another occurrence assertion. None is automatically a causal producer upgrade.

### Mechanism applicability and activity evidence scope

graph: not_applicable. Targets: CHEBI:85129.

The owner has no local graph, graph reference, pathway, target or assay items, so a maintained mechanism-reader call is not applicable. Its ANTIBACTERIAL summary is instead backed by the exact SAME_STRUCTURE/SAME_INCHIKEY AntibioticMech link at pinned corpus commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976. The maintained seeder permits that class/link route while withholding transferred targets, MICs and mechanism detail. The blank-AID PubChem marker is not a measurement.

### Claim-specific references and complete history

evidence: supported. Targets: CHEBI:85129.

DOI:10.1128/aac.03512-14 is recorded at MIBiG COMPOUND_EVIDENCE level; the ChEBI and LOTUS occurrence references retain their own scope. BGC0000418 also contains the B and desmethyl compound rows, but shared entry/citation is not independent experiment or identity evidence. Two seed histories are preserved. The sibling inventory is inspected; its underlying mechanism and primary papers are not newly verified.

### Chemical classification, source semantics and queue limits

consistency: supported. Targets: CHEBI:85129.

The NPClassifier Vancomycins and Teicoplanins/Oligopeptides classification and glycoside:true are explicit computed outputs. Asserted Glycopeptide compound class and NRPS/Type I BGC classification remain separate. The antibacterial summary is sourced through the permitted sibling-link rule rather than inferred from the computed glycopeptide class.

### Earned local work and held verification

completeness: unknown. Targets: CHEBI:85129.

The seven review areas were assessed against complete current owners/histories, exact retained source rows, cached taxon stanzas, actual canonical intakes and both complete saved molecular forms. No evidenced record defect was identified in this bounded review. Full QC, complete OAK and fresh external primary-source/taxonomic verification remain unavailable or held. Local stored-form parsing, database metadata and cached taxonomy do not replace those checks. One exact ANTIBACTERIAL sibling-summary row; PubChem CID16131418 marker has blank AID and no assay data. No local measurement or copied target.

### Bounded positive local validation and normalized chemical representation

consistency: supported. Targets: CHEBI:85129.

The selected record is well-formed under the current closed schema and reproduces from maintained inputs. The two stored molecular encodings generate the declared Standard InChIKey and agree in parsed formula and net charge. These positive local results do not establish natural identity, exact graph equivalence, strain-specific production or primary-paper support.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| S289-2889-owner | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/ristocetin-a.yaml; complete current UTF-8 owner; every root and both curation-history events | supports | CHEBI:85129, the complete VUOPFFVAZTUEGW-FBMDODLCSA-N key and MIBiG BGC0000418 compound 1 join the selected Ristocetin A owner. The retained ChEBI label is the generic ristocetin; conf/id_label_targets.yaml explicitly allows the exact CHEBI:85129/Ristocetin A name variant with curator confirmation still noted. This known local exception is not treated as fresh resolution of the generic-name ambiguity. Ristocetin B and both desmethyl owners retain different full keys/formulas. |
| S289-2889-source-reading | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch289-conditional-preflight/support-prep/support-conditional289-last-five-source-reading-001.json; /contexts/3/frames and /unique_physical_rows; all fields and physical spans; exact current owner/table hashes rechecked | partial | BGC0000418 v5 records SOURCE_ASSERTION Amycolatopsis lurida, NCBITaxon:31959, and CLUSTER_UNSTATED linkage with no locus methods or coordinates. Separate ChEBI occurrences retain NCBITaxon:1460371 at NRRL 2430 strain scope (cached name Amycolatopsis lurida NRRL 2430; PMID:25323720) and Amycolatopsis sp. NCBITaxon:37632, strain MJM2582 (PMID:25359910). LOTUS's Nocardia occurrence, DOI:10.1039/C39790000906, is another occurrence assertion. None is automatically a causal producer upgrade. Compound-level DOI:10.1128/aac.03512-14; separate occurrence PMID:25323720/25359910 and LOTUS DOI; pinned sibling class/link is not a freshly read mechanism. |
| S289-2889-intake | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/intakes-001/intake-summary-001.json; /records/8: exact 70 current input paths and selected target | supports | Actual canonical inspection binds the current source snapshot and target; it is not independent verification of the asserted biology. |
| S289-2889-intake-execution | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/inspect-2889-001/receipt.json; complete original canonical-inspect process receipt; exit status and exact invocation | supports | Original canonical inspection completed; no target was replayed for this fragment. |
| S289-2889-capture | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/current-owner-capture-001.json; /records/8/owner | supports | Complete actual owner capture equals the current selected raw bytes and the earlier complete raw/history reading. |
| S289-2889-chemistry | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/chemistry-local/diagnostic-DATA-001.json; /records/8: comparisons, atom_correspondence and complete smiles/inchi computed atoms, bonds, rings, potential_stereo, motifs | partial | Both saved neutral C95H110N8O44 forms contain 147 atoms and 163 bonds. The crosslinked glycopeptide scaffold contains seven aromatic six-member rings and six saturated C5O ring motifs connected through oxygen bridges. Nineteen saved symmetric-SSSR ring rows are not nineteen independent cycles; the connected graph has cycle rank 17. Six secondary amides become six C(OH)=N sites in the saved InChI form. The methyl ester remains: SMILES C141(=O142)–O143–C144 and InChI C89(=O130)–O131–C3; it is not a free terminal acid. Both forms retain 36 specified and one unspecified tetrahedral centre. The unknown centre is an acetal-like C–H with two oxygen neighbours in a C5O ring (SMILES C56; InChI C90). This agrees with stereo_complete:false and does not supply a natural anomer assignment. Six extra unspecified InChI C=N candidates belong to the imidic representations. Candidate C5O motifs and bridge topology alone do not assign sugar names, linkage positions or natural configuration. Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized Standard InChI/key, declared key, formula, charge and atom/bond counts agree. The saved chirality-aware atom map is empty and full_graph_identity_established is false. The explicit motif changes explain a representation difference but do not establish full graph or natural-sample identity. |
| S289-2889-chemistry-execution | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/diagnostic-original-001/receipt.json; complete original process receipt; stdout/stderr pins and denied-event boundary | supports | Exactly twenty literal stored-form parses were performed once for the batch; this fragment reads saved outputs and performs no molecule parsing. |
| S289-2889-seeder | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/scripts/seed_from_sources.py; MIBiG reference emission 695–717; blank-AID filtering 939–941; exact-key sibling class/link route 1453–1483 | supports | ENTRY and COMPOUND_EVIDENCE scope, empty AID markers, producer/locus evidence axes and permitted sibling class/link emission are distinct. No target, MIC or mechanism is transferred solely from a sibling class. |
| S289-2889-stereo-policy | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/scripts/extract_mibig.py; structure_fields; lines 142–173, especially 165–172 | supports | stereo_complete uses FindMolChiralCenters with includeUnassigned and tests atom-centre question marks. It is not a universal bond-geometry or natural-configuration guarantee. |
| S289-2889-taxonomy-cache | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/corpus_taxa.obo; complete relevant NCBITaxon stanzas: Species-level producer NCBITaxon:31959; separate NRRL2430 strain occurrence1460371, Amycolatopsis sp.37632/MJM2582 and genus Nocardia1817 occurrences. | partial | Species-level producer NCBITaxon:31959; separate NRRL2430 strain occurrence1460371, Amycolatopsis sp.37632/MJM2582 and genus Nocardia1817 occurrences. These cached labels/synonyms support only local label/strain interpretation; no fresh OAK or taxonomy request occurred. |
| S289-2889-schema | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; chemical structure stereocentre meaning, ProducerOrganism, BiosyntheticGeneCluster, occurrences, related_records and bioactivity_summary | supports | Optional mechanisms, source provenance grades, occurrence granularity and class summaries are assessed separately; presence/absence does not imply biological truth. |
| S289-2889-native-scope | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/native-current289-local-execution-handoff-001.json; /five_gates and /maintained_reader_applicability; this selected owner and queue rows | supports | Five local native gates passed, including complete 3136-record strict/reproduction scope. Full QC/OAK were not earned. Selected queue rows are leads, not automatic scientific findings. No maintained mechanism-reader route applies. |
| S289-2889-table-00 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical TSV lines 566, 567, 568, 569 | context_only | Complete matching payload columns were read; identity and same-BGC context matches remain distinguished. |
| S289-2889-table-01 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; physical TSV lines 32664 | context_only | Complete matching payload columns were read; identity and same-BGC context matches remain distinguished. |
| S289-2889-table-02 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; physical TSV lines 10985, 10986 | context_only | Complete matching payload columns were read; identity and same-BGC context matches remain distinguished. |
| S289-2889-table-03 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical TSV lines 2591 | context_only | Complete matching payload columns were read; identity and same-BGC context matches remain distinguished. |
| S289-2889-table-04 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical TSV lines 9131 | context_only | Complete matching payload columns were read; identity and same-BGC context matches remain distinguished. |
| S289-2889-table-05 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/cyanometdb_occurrences.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-06 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical TSV lines 8531 | context_only | Complete matching payload columns were read; identity and same-BGC context matches remain distinguished. |
| S289-2889-table-07 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/bindingdb_targets.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-08 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv; physical TSV lines 2365 | context_only | Complete matching payload columns were read; identity and same-BGC context matches remain distinguished. |
| S289-2889-table-09 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/pathwaymech_products.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-10 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/curated_compounds.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-11 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/lotus_occurrence_exclusions.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-12 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_claim_references.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-13 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_locus_evidence_overrides.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-14 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_producer_isolates.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-15 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_producer_strains.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-16 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_structure_corrections.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-17 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_xref_exclusions.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-18 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-table-19 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/unresolved_taxa.tsv; complete retained table; exact predicates recorded in source-reading context frame | context_only | No row matched the bounded identity/BGC predicates in this retained table; no wider absence claim. |
| S289-2889-bounded-search | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch289-conditional-preflight/support-prep/support-conditional289-last-five-source-reading-001.json; /contexts/3/frames filtered to the twenty actual intake table paths; /search_scope | partial | One exact ANTIBACTERIAL sibling-summary row; PubChem CID16131418 marker has blank AID and no assay data. No local measurement or copied target. |
| S289-2889-companion-0 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/ristocetin-b.yaml; complete direct same-BGC owner, full key/formula, source/occurrence/related roots and complete history | context_only | Direct BGC context is included to maintain distinct compound identities and evidence ownership; no activity, stereochemistry, producer causation or independent-publication credit is transferred. |
| S289-2889-companion-1 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/desmethyl-ristocetin-a.yaml; complete direct same-BGC owner, full key/formula, source/occurrence/related roots and complete history | context_only | Direct BGC context is included to maintain distinct compound identities and evidence ownership; no activity, stereochemistry, producer causation or independent-publication credit is transferred. |
| S289-2889-companion-2 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/desmethyl-ristocetin-b.yaml; complete direct same-BGC owner, full key/formula, source/occurrence/related roots and complete history | context_only | Direct BGC context is included to maintain distinct compound identities and evidence ownership; no activity, stereochemistry, producer causation or independent-publication credit is transferred. |
| S289-2889-label-exception | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/conf/id_label_targets.yaml; exact CHEBI:85129 / Ristocetin A exception | partial | The existing generic ristocetin name variant is permitted locally while curator confirmation remains noted; this is not fresh independent disambiguation. |
| EV289-intake | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/inspect-2889-001/stdout; Retained original execution output; exact SHA256 below. | supports | Captured this exact generated target and its regular-file source inputs at the selected fresh main commit; current input hashes remain unchanged. |
| EV289-strict_ten | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-strict-ten-001/stderr; Retained original execution output; exact SHA256 below. | supports | All ten selected whole owners passed closed validation; zero error rows. |
| EV289-strict_full | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-strict-full-001/stderr; Retained original execution output; exact SHA256 below. | supports | All 3136 current owners passed full closed validation with component-inventory audit; zero error rows. |
| EV289-lockfile | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-lockfile-001/stdout; Retained original execution output; exact SHA256 below. | supports | All 3136 owner paths agree with PATHS.tsv and filing pins, including component inventory checks. |
| EV289-reproduction | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-reproduction-001/stdout; Retained original execution output; exact SHA256 below. | supports | All 3136 records are byte-identical to the current seeder output. Carried curator mechanism claims are preserved, not independently proven. |
| EV289-queue | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-queue-001/stdout; Retained original execution output; exact SHA256 below. | supports | The complete current review queue was generated locally: 8919 rows across 12 queues. Queue membership does not establish scientific review. |
| EV289-molecular | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/chemistry-local/diagnostic-DATA-001.json; Retained original execution output; exact SHA256 below. | supports | Exactly two stored encodings were parsed for this record (20 across the batch). Their normalized Standard InChI, key, computed formula and net charge agree; graph/canonical-SMILES equivalence and natural sample identity are not inferred. Record-specific differences remain in the scientific assessments. |

## Limits And Additional Notes

- Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized Standard InChI/key, declared key, formula, charge and atom/bond counts agree. The saved chirality-aware atom map is empty and full_graph_identity_established is false. The explicit motif changes explain a representation difference but do not establish full graph or natural-sample identity.
- SOURCE_ASSERTION producer and CLUSTER_UNSTATED locus; three occurrence assertions preserve citation and taxon/strain grain. Compound-level DOI:10.1128/aac.03512-14; separate occurrence PMID:25323720/25359910 and LOTUS DOI; pinned sibling class/link is not a freshly read mechanism.
- One exact ANTIBACTERIAL sibling-summary row; PubChem CID16131418 marker has blank AID and no assay data. No local measurement or copied target.
- Full QC, complete OAK and fresh external primary-source/taxonomic verification remain unavailable or held. Local stored-form parsing, database metadata and cached taxonomy do not replace those checks.
- One unspecified tetrahedral centre remains in both stored forms; no natural stereochemical assignment was supplied.
- The existing CHEBI:85129 generic-label exception still notes curator confirmation; the ANTIBACTERIAL sibling summary is not a direct assay or newly inspected mechanism.
- Full QC, complete OAK label checks and fresh external-source verification are unavailable. Completion remains partial despite successful local gates.
- The review source is a working-tree input attestation at the captured Git base. Saved validation does not promote native record status or close unrelated historical findings.
- Source revision: 18ca5dd6b9023670f10355084b45a8757a7a4e9e; current canonical working-tree inputs rehashed exactly.
- No new source request, mechanism-reader call, molecular parse, record edit or saved-review operation was performed by this author.
- ROOT supplies original common check templates and final admission; this fragment does not claim full QC, OAK or fresh primary verification.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T113122Z-ristocetin-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: Review Ristocetin A against retained local evidence
started_at: '2026-11-07T11:21:22.782398Z'
finished_at: '2026-11-07T11:31:22.525768Z'
reviewer:
  identity: Codex ROOT with Bgc/Support scientific reviewers and Native local checks
  kind: agent
  independence: unknown
  independence_basis: Read-only review in an isolated owned checkout. Authorship independence
    from historical record curation is not established; local technical checks and
    domain assessments were assigned separately.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: 'Ristocetin A: the retained identity, chemical topology and explicitly graded
  source assertions are locally coherent. The review is partial; source-limited producer/occurrence
  evidence, representation differences and unperformed external checks remain explicit.'
source:
  git_revision: 18ca5dd6b9023670f10355084b45a8757a7a4e9e
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
    sha256: c3a6935589e9db0fdff25c518a31e2d5b02b99d9110a33f6ff6335455e03601c
    role: context
  - path: conf/np_roles.tsv
    sha256: 0660a4067b6b9b23c0929ddbe2a42b470c41bf77575ea7f83008c450bbf91dd3
    role: context
  - path: conf/producer_evidence.tsv
    sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
    role: context
  - path: conf/record_review.yaml
    sha256: e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8
    role: context
  - path: conf/sources.yaml
    sha256: d5e8ab63eeebb376589a0c9bf6f7eb92f45913b84243de20d820442ec88d5a98
    role: context
  - path: curation/curated_compounds.tsv
    sha256: 371b3a8b453dc9706e6a8f7f615bf6604809b1c42f4a38b7e9e921ffcbbad064
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
    sha256: 2917836665e5117aebf1947cb148711bc0df7f1475bd2fdbfad0cd6d411e6cc7
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
    sha256: 364ec7b1bbd49467cde7fe69f66964e4640020638ba80fccfc62e2162ede7f42
    role: context
  - path: data/natural_products/amino_acids_and_peptides/desmethyl-ristocetin-a.yaml
    sha256: b7465fc3dc1b1ef85c81e5f739c465e1ff8e2d25bf7e5a02338b7ef50c77437b
    role: context
  - path: data/natural_products/amino_acids_and_peptides/desmethyl-ristocetin-b.yaml
    sha256: 579cbd8bf43b2863d4f57ae421a02fa02ff98a718b8c115467b413b15485c83b
    role: context
  - path: data/natural_products/amino_acids_and_peptides/ristocetin-a.yaml
    sha256: 706627ed07c9b008a534211a2ecfe539767a2545904699d46d87bb924ff79fee
    role: target
  - path: data/natural_products/amino_acids_and_peptides/ristocetin-b.yaml
    sha256: 9cdc63b960370ec4ede731b894c1a6be4bb4895c746e40d3c851953e03e42a25
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 3370e0835cefa2f4d08fe496e81f7dc3ad8783ee76fd9b2a222465e1f5e31937
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
    sha256: f62f89df12bd373e0663a7e11e56e46733ca174f8495ec116ec57679c2279f35
    role: context
  - path: data/raw/pathwaymech_products.tsv
    sha256: 28ff699b83648614928f7ea5d8e8f5aee49a34ebbc9b6e9dbfece255383b7e04
    role: context
  - path: data/raw/pubchem_bioassay.tsv
    sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
    role: context
  - path: data/raw/taxon_groups.tsv
    sha256: f73f228d57d79a1d85a1441efa6829917b1ffecac08cb7bdd4fc855046255f8f
    role: context
  - path: data/raw/taxon_merged.tsv
    sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
    role: context
  - path: data/raw/taxon_names.tsv
    sha256: 9058b9a99260eb483ea21ce7cc9713fd336177031d883f0b5fb50325c7b2c371
    role: context
  - path: data/raw/taxon_non_organism.tsv
    sha256: f2c1ee257bbbcb0854528196ab1f809d658c27f1c7b2036f7f71f088b52935bb
    role: context
  - path: docs/CURATION.md
    sha256: 397dc32b7978f9115229f13232f3d9e9c5fac4ce5265e2f9e9cef13b6a9842f9
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
  - path: pyproject.toml
    sha256: 02505a46585e870eac7333f31a6773df51465ef13969d4d490fbc0247931d85c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/check_reproduction.py
    sha256: b00efb72ebf81c84760ccb4a0a491a596d1198d1e21613df6cb417e68caff868
    role: context
  - path: scripts/curation_worklist.py
    sha256: 913508ca8df2eb5c037cd9e4769b14b027869ab78c7306f33b59e1c7e383a1c3
    role: context
  - path: scripts/extract_chebi.py
    sha256: 46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/seed_from_sources.py
    sha256: d6650a80685b7f778050f79cc72de1fc3bbf281c57336401a5c773755de56324
    role: context
  - path: scripts/validate_strict.py
    sha256: e9b844d10fb7d2889521677716098da5883c7fd7d3c887a5cb600b87bbca0c21
    role: context
  - path: scripts/verify_corpus.py
    sha256: 3e79d6e18e43010a84e2ef7857625655185796d447ee12979a94cd836d756b60
    role: context
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: c57128ce7815cd3e336e427e9699e374836fa263905da875055ca9defea55f01
    role: context
  - path: src/naturalproductmech/curate/curated_compounds.py
    sha256: fdafad9ed1d94c78c996083632c75f3bafc1620a31da5aa7b9a37e558a187915
    role: context
  - path: src/naturalproductmech/curate/lotus_exclusions.py
    sha256: 6352cac7c587eab5a56d907c523cc899d02d197009081624bf8649c675ee30f7
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
    role: context
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
    role: context
  - path: src/naturalproductmech/grading.py
    sha256: ece54c4a2c0803f034ac59de51b1006cf79ea8d6b6256d75757d4adb88ea9630
    role: context
  - path: src/naturalproductmech/graph_components.py
    sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
    role: context
  - path: src/naturalproductmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/naturalproductmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: src/naturalproductmech/validation/write_validated.py
    sha256: 4728cfb7d3406b971c02f2bc81e1dfb97679ea0914d27563282ce4c5185f474a
    role: context
  - path: tests/test_curated_compounds.py
    sha256: 01af0ae1e13811d6238227f5c82ac627f4e9effa870ecc50b922cb7de2d144cc
    role: context
  - path: tests/test_record_review_contract.py
    sha256: 7be08e684dcd235ddeae8f3c6a5d45b0ee74a60d1c1818cc81467e38901e5d56
    role: context
  - path: uv.lock
    sha256: c62a5739e3ffeb12cc57b3bf12a31dcf9cdfbf00b417f4ba3a801d51ef9efbe3
    role: context
scope:
  description: Complete local reading of this one selected owner, its history and
    any declared mechanism components; scientific verification remains partial. The
    current campaign corpus contains 3136 records.
  selection: 'Batch289, order 2889: one of the first ten sorted currently unreviewed
    paths in the reconciled catalogue (1768 covered,1368 remaining before this batch).
    This bundle assesses only this target.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:85129
targets:
- target_id: CHEBI:85129
  path: data/natural_products/amino_acids_and_peptides/ristocetin-a.yaml
  label: Ristocetin A
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained source harmonization and guarded emission of generated records.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Maintained MIBiG structure, producer and locus evidence extraction.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned imported structure and compound-specific BGC assertions; correct
      through the maintained extractor or implemented supported curation inputs.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_chebi.py
    role: Maintained extraction of the retained ChEBI definition and source concept.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned ChEBI source row for the retained definition and same-key concept.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned sibling-corpus structure-key join and activity-class summary; not
      primary assay evidence.
  ownership_note: Review only. Mechanism roots are absent in the complete selected
    owner. Source-specific correction actions must name the applicable implemented
    input; reserved curation/decisions.tsv is not consumed.
checks:
- check_id: CK289-intake
  name: Canonical target and source capture
  status: passed
  required: true
  summary: Captured this exact generated target and its regular-file source inputs
    at the selected fresh main commit; current input hashes remain unchanged.
  target_ids:
  - CHEBI:85129
  command: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/.venv/bin/python
    scripts/record_review.py inspect --targets /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/intakes-001/2889-targets-002.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/review-yaml-record/SKILL.md --input AGENTS.md --input conf/id_label_targets.yaml
    --input conf/np_roles.tsv --input conf/producer_evidence.tsv --input conf/record_review.yaml
    --input conf/sources.yaml --input curation/curated_compounds.tsv --input curation/lotus_occurrence_exclusions.tsv
    --input curation/mibig_claim_references.tsv --input curation/mibig_locus_evidence_overrides.tsv
    --input curation/mibig_producer_isolates.tsv --input curation/mibig_producer_strains.tsv
    --input curation/mibig_structure_corrections.tsv --input curation/mibig_xref_exclusions.tsv
    --input curation/pubchem_bioassay_exclusions.tsv --input curation/unresolved_taxa.tsv
    --input data/natural_products/PATHS.tsv --input data/natural_products/amino_acids_and_peptides/desmethyl-ristocetin-a.yaml
    --input data/natural_products/amino_acids_and_peptides/desmethyl-ristocetin-b.yaml
    --input data/natural_products/amino_acids_and_peptides/ristocetin-b.yaml --input
    data/raw/MANIFEST.yaml --input data/raw/antibioticmech_inchikeys.tsv --input data/raw/bindingdb_targets.tsv
    --input data/raw/chebi_origins.tsv --input data/raw/chebi_structures.tsv --input
    data/raw/corpus_taxa.obo --input data/raw/cyanometdb_occurrences.tsv --input data/raw/lotus_occurrences.tsv
    --input data/raw/mibig_compounds.tsv --input data/raw/npclassifier.tsv --input
    data/raw/pathwaymech_products.tsv --input data/raw/pubchem_bioassay.tsv --input
    data/raw/taxon_groups.tsv --input data/raw/taxon_merged.tsv --input data/raw/taxon_names.tsv
    --input data/raw/taxon_non_organism.tsv --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/record-review-profile.md --input docs/record-reviews.md --input justfile
    --input pyproject.toml --input schema/record_review.yaml --input scripts/check_reproduction.py
    --input scripts/curation_worklist.py --input scripts/extract_chebi.py --input
    scripts/extract_mibig.py --input scripts/record_review.py --input scripts/seed_from_sources.py
    --input scripts/validate_strict.py --input scripts/verify_corpus.py --input src/naturalproductmech/curate/bioassay_exclusions.py
    --input src/naturalproductmech/curate/claim_references.py --input src/naturalproductmech/curate/curated_compounds.py
    --input src/naturalproductmech/curate/lotus_exclusions.py --input src/naturalproductmech/curate/producer_strains.py
    --input src/naturalproductmech/curate/structure_corrections.py --input src/naturalproductmech/curate/xref_exclusions.py
    --input src/naturalproductmech/grading.py --input src/naturalproductmech/graph_components.py
    --input src/naturalproductmech/schema/history.yaml --input src/naturalproductmech/schema/mech_shared.yaml
    --input src/naturalproductmech/schema/naturalproductmech.yaml --input src/naturalproductmech/validation/write_validated.py
    --input tests/test_curated_compounds.py --input tests/test_record_review_contract.py
    --input uv.lock
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-intake
- check_id: CK289-strict_ten
  name: 'Maintained local gate: strict_ten'
  status: passed
  required: true
  summary: All ten selected whole owners passed closed validation; zero error rows.
  target_ids:
  - CHEBI:85129
  command: /opt/homebrew/bin/just validate-strict data/natural_products/amino_acids_and_peptides/rc-aip1.yaml
    data/natural_products/amino_acids_and_peptides/rhabdopeptide-1.yaml data/natural_products/amino_acids_and_peptides/rhabdopeptide-2.yaml
    data/natural_products/amino_acids_and_peptides/rhabdopeptide-3.yaml data/natural_products/amino_acids_and_peptides/rhabdopeptide-4.yaml
    data/natural_products/amino_acids_and_peptides/rhizocticin-a.yaml data/natural_products/amino_acids_and_peptides/ririwpeptide-a.yaml
    data/natural_products/amino_acids_and_peptides/ririwpeptide-b.yaml data/natural_products/amino_acids_and_peptides/ristocetin-a.yaml
    data/natural_products/amino_acids_and_peptides/ristocetin-b.yaml --workers 2 --quiet
    --out /Users/marcin/agent-work/NaturalProductMech/npm-native-checks/batch-289/selected-strict-001.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-strict_ten
- check_id: CK289-strict_full
  name: 'Maintained local gate: strict_full'
  status: passed
  required: true
  summary: All 3136 current owners passed full closed validation with component-inventory
    audit; zero error rows.
  target_ids:
  - CHEBI:85129
  command: /opt/homebrew/bin/just validate-strict --workers 2 --quiet --out /Users/marcin/agent-work/NaturalProductMech/npm-native-checks/batch-289/full-strict-001.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-strict_full
- check_id: CK289-lockfile
  name: 'Maintained local gate: lockfile'
  status: passed
  required: true
  summary: All 3136 owner paths agree with PATHS.tsv and filing pins, including component
    inventory checks.
  target_ids:
  - CHEBI:85129
  command: /opt/homebrew/bin/just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-lockfile
- check_id: CK289-reproduction
  name: 'Maintained local gate: reproduction'
  status: passed
  required: true
  summary: All 3136 records are byte-identical to the current seeder output. Carried
    curator mechanism claims are preserved, not independently proven.
  target_ids:
  - CHEBI:85129
  command: /opt/homebrew/bin/just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-reproduction
- check_id: CK289-queue
  name: 'Maintained local gate: queue'
  status: passed
  required: true
  summary: 'The complete current review queue was generated locally: 8919 rows across
    12 queues. Queue membership does not establish scientific review.'
  target_ids:
  - CHEBI:85129
  command: /opt/homebrew/bin/just review-queue --tsv /Users/marcin/agent-work/NaturalProductMech/npm-native-checks/batch-289/review-queue-001.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-queue
- check_id: CK289-molecular
  name: Local stored-form molecular diagnostic
  status: passed
  required: true
  summary: Exactly two stored encodings were parsed for this record (20 across the
    batch). Their normalized Standard InChI, key, computed formula and net charge
    agree; graph/canonical-SMILES equivalence and natural sample identity are not
    inferred. Record-specific differences remain in the scientific assessments.
  target_ids:
  - CHEBI:85129
  command: /usr/bin/sandbox-exec -p '(version 1)(allow default)(deny network*)' /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/.venv/bin/python
    -I -S -B /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/diagnose289-001.py
    diagnostic
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-molecular
- check_id: CK289-reader
  name: Complete maintained mechanism read
  status: not_applicable
  required: false
  summary: The fully read owner has no graph, component-reference, pathway or molecular-target
    roots. No maintained mechanism-reader call was made for this target. The absence
    of these optional roots is not itself a scientific defect.
  target_ids:
  - CHEBI:85129
- check_id: CK289-full-qc
  name: Full repository QC
  status: unavailable
  required: true
  summary: 'Not run: maintained full QC reaches the vendored-sync fetch. The five
    local gates do not substitute for full QC.'
  target_ids:
  - CHEBI:85129
- check_id: CK289-ontology
  name: Complete OAK identifier-label correspondence
  status: unavailable
  required: true
  summary: 'Not run: a complete pinned offline CHEBI/GO adapter boundary was not established.
    No ontology download or remote resolver was permitted.'
  target_ids:
  - CHEBI:85129
- check_id: CK289-fresh-authorities
  name: Fresh source, literature, taxonomy and structured database verification
  status: unavailable
  required: true
  summary: Not run under the source-request hold. Database assertions, gene/pathway
    annotations, citations, exact forms and strain claims are assessed only against
    retained local evidence; no fresh resolution or primary-paper authentication is
    claimed.
  target_ids:
  - CHEBI:85129
evidence:
- evidence_id: S289-2889-owner
  kind: record_content
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/ristocetin-a.yaml
  locator: complete current UTF-8 owner; every root and both curation-history events
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: supports
  summary: CHEBI:85129, the complete VUOPFFVAZTUEGW-FBMDODLCSA-N key and MIBiG BGC0000418
    compound 1 join the selected Ristocetin A owner. The retained ChEBI label is the
    generic ristocetin; conf/id_label_targets.yaml explicitly allows the exact CHEBI:85129/Ristocetin
    A name variant with curator confirmation still noted. This known local exception
    is not treated as fresh resolution of the generic-name ambiguity. Ristocetin B
    and both desmethyl owners retain different full keys/formulas.
  snapshot_sha256: 706627ed07c9b008a534211a2ecfe539767a2545904699d46d87bb924ff79fee
- evidence_id: S289-2889-source-reading
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch289-conditional-preflight/support-prep/support-conditional289-last-five-source-reading-001.json
  locator: /contexts/3/frames and /unique_physical_rows; all fields and physical spans;
    exact current owner/table hashes rechecked
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: partial
  summary: BGC0000418 v5 records SOURCE_ASSERTION Amycolatopsis lurida, NCBITaxon:31959,
    and CLUSTER_UNSTATED linkage with no locus methods or coordinates. Separate ChEBI
    occurrences retain NCBITaxon:1460371 at NRRL 2430 strain scope (cached name Amycolatopsis
    lurida NRRL 2430; PMID:25323720) and Amycolatopsis sp. NCBITaxon:37632, strain
    MJM2582 (PMID:25359910). LOTUS's Nocardia occurrence, DOI:10.1039/C39790000906,
    is another occurrence assertion. None is automatically a causal producer upgrade.
    Compound-level DOI:10.1128/aac.03512-14; separate occurrence PMID:25323720/25359910
    and LOTUS DOI; pinned sibling class/link is not a freshly read mechanism.
  snapshot_sha256: 0ff69d7fdb76f3bf4abb25bf1151e99ae473b6052b8dbab1af33da7b28f9ede6
- evidence_id: S289-2889-intake
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/intakes-001/intake-summary-001.json
  locator: '/records/8: exact 70 current input paths and selected target'
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: supports
  summary: Actual canonical inspection binds the current source snapshot and target;
    it is not independent verification of the asserted biology.
  snapshot_sha256: c28d956d44f73b8f96f2b72c9db4f22ab58f7c05fa5fafd1a8a98969c79a8620
- evidence_id: S289-2889-intake-execution
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/inspect-2889-001/receipt.json
  locator: complete original canonical-inspect process receipt; exit status and exact
    invocation
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: supports
  summary: Original canonical inspection completed; no target was replayed for this
    fragment.
  snapshot_sha256: 18e61fbc7b0f3318a5c20ca50a6b1e853782b3125fe0c1766042e460be844fc6
- evidence_id: S289-2889-capture
  kind: record_content
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/current-owner-capture-001.json
  locator: /records/8/owner
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: supports
  summary: Complete actual owner capture equals the current selected raw bytes and
    the earlier complete raw/history reading.
  snapshot_sha256: 2761213c0119b7eb309908183611aaa5a27df5afe094e13b69a7003276fce4ef
- evidence_id: S289-2889-chemistry
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/chemistry-local/diagnostic-DATA-001.json
  locator: '/records/8: comparisons, atom_correspondence and complete smiles/inchi
    computed atoms, bonds, rings, potential_stereo, motifs'
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: partial
  summary: 'Both saved neutral C95H110N8O44 forms contain 147 atoms and 163 bonds.
    The crosslinked glycopeptide scaffold contains seven aromatic six-member rings
    and six saturated C5O ring motifs connected through oxygen bridges. Nineteen saved
    symmetric-SSSR ring rows are not nineteen independent cycles; the connected graph
    has cycle rank 17. Six secondary amides become six C(OH)=N sites in the saved
    InChI form. The methyl ester remains: SMILES C141(=O142)–O143–C144 and InChI C89(=O130)–O131–C3;
    it is not a free terminal acid. Both forms retain 36 specified and one unspecified
    tetrahedral centre. The unknown centre is an acetal-like C–H with two oxygen neighbours
    in a C5O ring (SMILES C56; InChI C90). This agrees with stereo_complete:false
    and does not supply a natural anomer assignment. Six extra unspecified InChI C=N
    candidates belong to the imidic representations. Candidate C5O motifs and bridge
    topology alone do not assign sugar names, linkage positions or natural configuration.
    Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized
    Standard InChI/key, declared key, formula, charge and atom/bond counts agree.
    The saved chirality-aware atom map is empty and full_graph_identity_established
    is false. The explicit motif changes explain a representation difference but do
    not establish full graph or natural-sample identity.'
  snapshot_sha256: 4c5fc29dbe122c1cf52903fa7f8c29ee51d8bc5ed33fec85a221d4b65b591ba2
- evidence_id: S289-2889-chemistry-execution
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/diagnostic-original-001/receipt.json
  locator: complete original process receipt; stdout/stderr pins and denied-event
    boundary
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: supports
  summary: Exactly twenty literal stored-form parses were performed once for the batch;
    this fragment reads saved outputs and performs no molecule parsing.
  snapshot_sha256: 5054842eb7c370445ff3c5bdc872ae0e8fd8b5e0d37166f609d7cd623bc75a5a
- evidence_id: S289-2889-seeder
  kind: record_content
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: MIBiG reference emission 695–717; blank-AID filtering 939–941; exact-key
    sibling class/link route 1453–1483
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: supports
  summary: ENTRY and COMPOUND_EVIDENCE scope, empty AID markers, producer/locus evidence
    axes and permitted sibling class/link emission are distinct. No target, MIC or
    mechanism is transferred solely from a sibling class.
  snapshot_sha256: d6650a80685b7f778050f79cc72de1fc3bbf281c57336401a5c773755de56324
- evidence_id: S289-2889-stereo-policy
  kind: record_content
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: structure_fields; lines 142–173, especially 165–172
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: supports
  summary: stereo_complete uses FindMolChiralCenters with includeUnassigned and tests
    atom-centre question marks. It is not a universal bond-geometry or natural-configuration
    guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: S289-2889-taxonomy-cache
  kind: authority
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/corpus_taxa.obo
  locator: 'complete relevant NCBITaxon stanzas: Species-level producer NCBITaxon:31959;
    separate NRRL2430 strain occurrence1460371, Amycolatopsis sp.37632/MJM2582 and
    genus Nocardia1817 occurrences.'
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: partial
  summary: Species-level producer NCBITaxon:31959; separate NRRL2430 strain occurrence1460371,
    Amycolatopsis sp.37632/MJM2582 and genus Nocardia1817 occurrences. These cached
    labels/synonyms support only local label/strain interpretation; no fresh OAK or
    taxonomy request occurred.
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: S289-2889-schema
  kind: record_content
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: chemical structure stereocentre meaning, ProducerOrganism, BiosyntheticGeneCluster,
    occurrences, related_records and bioactivity_summary
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: supports
  summary: Optional mechanisms, source provenance grades, occurrence granularity and
    class summaries are assessed separately; presence/absence does not imply biological
    truth.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: S289-2889-native-scope
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/native-current289-local-execution-handoff-001.json
  locator: /five_gates and /maintained_reader_applicability; this selected owner and
    queue rows
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: supports
  summary: Five local native gates passed, including complete 3136-record strict/reproduction
    scope. Full QC/OAK were not earned. Selected queue rows are leads, not automatic
    scientific findings. No maintained mechanism-reader route applies.
  snapshot_sha256: 556c67fe36355e4a6a1ecd13584f377333f438b252a4bef5e1942a3084b94bb2
- evidence_id: S289-2889-table-00
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical TSV lines 566, 567, 568, 569
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: Complete matching payload columns were read; identity and same-BGC context
    matches remain distinguished.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: S289-2889-table-01
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: physical TSV lines 32664
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: Complete matching payload columns were read; identity and same-BGC context
    matches remain distinguished.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: S289-2889-table-02
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: physical TSV lines 10985, 10986
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: Complete matching payload columns were read; identity and same-BGC context
    matches remain distinguished.
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: S289-2889-table-03
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical TSV lines 2591
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: Complete matching payload columns were read; identity and same-BGC context
    matches remain distinguished.
  snapshot_sha256: f62f89df12bd373e0663a7e11e56e46733ca174f8495ec116ec57679c2279f35
- evidence_id: S289-2889-table-04
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical TSV lines 9131
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: Complete matching payload columns were read; identity and same-BGC context
    matches remain distinguished.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: S289-2889-table-05
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/cyanometdb_occurrences.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8
- evidence_id: S289-2889-table-06
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical TSV lines 8531
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: Complete matching payload columns were read; identity and same-BGC context
    matches remain distinguished.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: S289-2889-table-07
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/bindingdb_targets.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: 3cff45281c35a8b14d4d7784bc4b7af80e8e27779a5667a0292f0d9b022a22c1
- evidence_id: S289-2889-table-08
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv
  locator: physical TSV lines 2365
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: Complete matching payload columns were read; identity and same-BGC context
    matches remain distinguished.
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
- evidence_id: S289-2889-table-09
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/pathwaymech_products.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: 28ff699b83648614928f7ea5d8e8f5aee49a34ebbc9b6e9dbfece255383b7e04
- evidence_id: S289-2889-table-10
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/curated_compounds.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: 371b3a8b453dc9706e6a8f7f615bf6604809b1c42f4a38b7e9e921ffcbbad064
- evidence_id: S289-2889-table-11
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/lotus_occurrence_exclusions.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d
- evidence_id: S289-2889-table-12
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_claim_references.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029
- evidence_id: S289-2889-table-13
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_locus_evidence_overrides.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
- evidence_id: S289-2889-table-14
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_producer_isolates.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
- evidence_id: S289-2889-table-15
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_producer_strains.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: 2917836665e5117aebf1947cb148711bc0df7f1475bd2fdbfad0cd6d411e6cc7
- evidence_id: S289-2889-table-16
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_structure_corrections.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0
- evidence_id: S289-2889-table-17
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/mibig_xref_exclusions.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
- evidence_id: S289-2889-table-18
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
- evidence_id: S289-2889-table-19
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/unresolved_taxa.tsv
  locator: complete retained table; exact predicates recorded in source-reading context
    frame
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: No row matched the bounded identity/BGC predicates in this retained table;
    no wider absence claim.
  snapshot_sha256: 86efbda9c09388723a4f24da35e18404032f1549a9088192fbd2020cb846fa43
- evidence_id: S289-2889-bounded-search
  kind: search
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch289-conditional-preflight/support-prep/support-conditional289-last-five-source-reading-001.json
  locator: /contexts/3/frames filtered to the twenty actual intake table paths; /search_scope
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: partial
  summary: One exact ANTIBACTERIAL sibling-summary row; PubChem CID16131418 marker
    has blank AID and no assay data. No local measurement or copied target.
  snapshot_sha256: 0ff69d7fdb76f3bf4abb25bf1151e99ae473b6052b8dbab1af33da7b28f9ede6
  search_scope: Twenty actual-input raw/curation TSVs with literal boundary predicates
    from /contexts/3/frames in the pinned source reading; tokens are full InChIKey,
    exact owner/CHEBI identifiers and direct BGC accessions. Source discovery and
    owner-context search included ignored/hidden files (rg --files -uu; rg --no-ignore
    --hidden). Reserved decisions.tsv and source_queue.tsv census frames are excluded
    from this actual-input assessment. No name expansion, transitive congeners, external
    query or global literature/cache absence claim.
- evidence_id: S289-2889-companion-0
  kind: record_content
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/ristocetin-b.yaml
  locator: complete direct same-BGC owner, full key/formula, source/occurrence/related
    roots and complete history
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: Direct BGC context is included to maintain distinct compound identities
    and evidence ownership; no activity, stereochemistry, producer causation or independent-publication
    credit is transferred.
  snapshot_sha256: 9cdc63b960370ec4ede731b894c1a6be4bb4895c746e40d3c851953e03e42a25
- evidence_id: S289-2889-companion-1
  kind: record_content
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/desmethyl-ristocetin-a.yaml
  locator: complete direct same-BGC owner, full key/formula, source/occurrence/related
    roots and complete history
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: Direct BGC context is included to maintain distinct compound identities
    and evidence ownership; no activity, stereochemistry, producer causation or independent-publication
    credit is transferred.
  snapshot_sha256: b7465fc3dc1b1ef85c81e5f739c465e1ff8e2d25bf7e5a02338b7ef50c77437b
- evidence_id: S289-2889-companion-2
  kind: record_content
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/desmethyl-ristocetin-b.yaml
  locator: complete direct same-BGC owner, full key/formula, source/occurrence/related
    roots and complete history
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: context_only
  summary: Direct BGC context is included to maintain distinct compound identities
    and evidence ownership; no activity, stereochemistry, producer causation or independent-publication
    credit is transferred.
  snapshot_sha256: 579cbd8bf43b2863d4f57ae421a02fa02ff98a718b8c115467b413b15485c83b
- evidence_id: S289-2889-label-exception
  kind: authority
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/conf/id_label_targets.yaml
  locator: exact CHEBI:85129 / Ristocetin A exception
  accessed_at: '2026-11-07T11:30:40.854263Z'
  support: partial
  summary: The existing generic ristocetin name variant is permitted locally while
    curator confirmation remains noted; this is not fresh independent disambiguation.
  snapshot_sha256: c3a6935589e9db0fdff25c518a31e2d5b02b99d9110a33f6ff6335455e03601c
- evidence_id: EV289-intake
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/inspect-2889-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:21:24.023609Z'
  support: supports
  summary: Captured this exact generated target and its regular-file source inputs
    at the selected fresh main commit; current input hashes remain unchanged.
  snapshot_sha256: 87d9c65292506d8273ce7b1de28ac852dba013c0978d2e3c8c422303c54c0158
- evidence_id: EV289-strict_ten
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-strict-ten-001/stderr
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:22:30.692246Z'
  support: supports
  summary: All ten selected whole owners passed closed validation; zero error rows.
  snapshot_sha256: 64fa4be75844498991904765d1286900d9908e3a3d6a6cc5e74e4479178ee54b
- evidence_id: EV289-strict_full
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-strict-full-001/stderr
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:22:52.233216Z'
  support: supports
  summary: All 3136 current owners passed full closed validation with component-inventory
    audit; zero error rows.
  snapshot_sha256: d957eed8e15bb928f2ae3c3f22989ac01713bea2f869c39f80fa858c596a2311
- evidence_id: EV289-lockfile
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-lockfile-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:23:14.056358Z'
  support: supports
  summary: All 3136 owner paths agree with PATHS.tsv and filing pins, including component
    inventory checks.
  snapshot_sha256: 06b20cd71ef4e0ce9f998515c0dbd4076f81b0f420e22e4949fc19494217de24
- evidence_id: EV289-reproduction
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-reproduction-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:23:51.297984Z'
  support: supports
  summary: All 3136 records are byte-identical to the current seeder output. Carried
    curator mechanism claims are preserved, not independently proven.
  snapshot_sha256: 6375bbedfde712e0de5fd1fd6c8f939e45bd2cab4fecb4be7f8fc5b11ab7337d
- evidence_id: EV289-queue
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-queue-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:24:04.393915Z'
  support: supports
  summary: 'The complete current review queue was generated locally: 8919 rows across
    12 queues. Queue membership does not establish scientific review.'
  snapshot_sha256: 386216f171f1a0c3aac15fbc6e76ee6eedda8235755ec8abb80a2c173f297369
- evidence_id: EV289-molecular
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/chemistry-local/diagnostic-DATA-001.json
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:25:50.467442Z'
  support: supports
  summary: Exactly two stored encodings were parsed for this record (20 across the
    batch). Their normalized Standard InChI, key, computed formula and net charge
    agree; graph/canonical-SMILES equivalence and natural sample identity are not
    inferred. Record-specific differences remain in the scientific assessments.
  snapshot_sha256: 4c5fc29dbe122c1cf52903fa7f8c29ee51d8bc5ed33fec85a221d4b65b591ba2
assessments:
- assessment_id: S289-2889-identity
  area: identity
  topic: Exact source identity and direct-congener boundary
  summary: CHEBI:85129, the complete VUOPFFVAZTUEGW-FBMDODLCSA-N key and MIBiG BGC0000418
    compound 1 join the selected Ristocetin A owner. The retained ChEBI label is the
    generic ristocetin; conf/id_label_targets.yaml explicitly allows the exact CHEBI:85129/Ristocetin
    A name variant with curator confirmation still noted. This known local exception
    is not treated as fresh resolution of the generic-name ambiguity. Ristocetin B
    and both desmethyl owners retain different full keys/formulas.
  outcome: supported
  target_ids:
  - CHEBI:85129
  evidence_ids:
  - S289-2889-owner
  - S289-2889-source-reading
  - S289-2889-intake
  - S289-2889-bounded-search
  - S289-2889-companion-0
  - S289-2889-companion-1
  - S289-2889-companion-2
  - S289-2889-label-exception
  dimensions:
  - name: full_key
    definition: Complete selected compound key.
    value: VUOPFFVAZTUEGW-FBMDODLCSA-N
    evidence_ids:
    - S289-2889-owner
    - S289-2889-source-reading
    - S289-2889-intake
    - S289-2889-bounded-search
    - S289-2889-companion-0
    - S289-2889-companion-1
    - S289-2889-companion-2
    - S289-2889-label-exception
  - name: identity_scope
    definition: Grounding and distinct-context limits.
    value: CHEBI:85129, the complete VUOPFFVAZTUEGW-FBMDODLCSA-N key and MIBiG BGC0000418
      compound 1 join the selected Ristocetin A owner. The retained ChEBI label is
      the generic ristocetin; conf/id_label_targets.yaml explicitly allows the exact
      CHEBI:85129/Ristocetin A name variant with curator confirmation still noted.
      This known local exception is not treated as fresh resolution of the generic-name
      ambiguity. Ristocetin B and both desmethyl owners retain different full keys/formulas.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-source-reading
    - S289-2889-intake
    - S289-2889-bounded-search
    - S289-2889-companion-0
    - S289-2889-companion-1
    - S289-2889-companion-2
    - S289-2889-label-exception
- assessment_id: S289-2889-representation
  area: representation
  topic: Complete saved chemical forms and stereochemistry
  summary: 'Both saved neutral C95H110N8O44 forms contain 147 atoms and 163 bonds.
    The crosslinked glycopeptide scaffold contains seven aromatic six-member rings
    and six saturated C5O ring motifs connected through oxygen bridges. Nineteen saved
    symmetric-SSSR ring rows are not nineteen independent cycles; the connected graph
    has cycle rank 17. Six secondary amides become six C(OH)=N sites in the saved
    InChI form. The methyl ester remains: SMILES C141(=O142)–O143–C144 and InChI C89(=O130)–O131–C3;
    it is not a free terminal acid. Both forms retain 36 specified and one unspecified
    tetrahedral centre. The unknown centre is an acetal-like C–H with two oxygen neighbours
    in a C5O ring (SMILES C56; InChI C90). This agrees with stereo_complete:false
    and does not supply a natural anomer assignment. Six extra unspecified InChI C=N
    candidates belong to the imidic representations. Candidate C5O motifs and bridge
    topology alone do not assign sugar names, linkage positions or natural configuration.
    Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized
    Standard InChI/key, declared key, formula, charge and atom/bond counts agree.
    The saved chirality-aware atom map is empty and full_graph_identity_established
    is false. The explicit motif changes explain a representation difference but do
    not establish full graph or natural-sample identity.'
  outcome: supported
  target_ids:
  - CHEBI:85129
  evidence_ids:
  - S289-2889-owner
  - S289-2889-chemistry
  - S289-2889-chemistry-execution
  - S289-2889-stereo-policy
  - S289-2889-intake
  dimensions:
  - name: saved_topology
    definition: Interpretation of all saved atom/bond/ring/stereo/motif rows.
    value: 'Both saved neutral C95H110N8O44 forms contain 147 atoms and 163 bonds.
      The crosslinked glycopeptide scaffold contains seven aromatic six-member rings
      and six saturated C5O ring motifs connected through oxygen bridges. Nineteen
      saved symmetric-SSSR ring rows are not nineteen independent cycles; the connected
      graph has cycle rank 17. Six secondary amides become six C(OH)=N sites in the
      saved InChI form. The methyl ester remains: SMILES C141(=O142)–O143–C144 and
      InChI C89(=O130)–O131–C3; it is not a free terminal acid. Both forms retain
      36 specified and one unspecified tetrahedral centre. The unknown centre is an
      acetal-like C–H with two oxygen neighbours in a C5O ring (SMILES C56; InChI
      C90). This agrees with stereo_complete:false and does not supply a natural anomer
      assignment. Six extra unspecified InChI C=N candidates belong to the imidic
      representations. Candidate C5O motifs and bridge topology alone do not assign
      sugar names, linkage positions or natural configuration.'
    evidence_ids:
    - S289-2889-owner
    - S289-2889-chemistry
    - S289-2889-chemistry-execution
    - S289-2889-stereo-policy
    - S289-2889-intake
  - name: comparison_limit
    definition: Exact limits of the original diagnostic comparison.
    value: Both canonical isomeric and nonisomeric SMILES comparisons are false while
      normalized Standard InChI/key, declared key, formula, charge and atom/bond counts
      agree. The saved chirality-aware atom map is empty and full_graph_identity_established
      is false. The explicit motif changes explain a representation difference but
      do not establish full graph or natural-sample identity.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-chemistry
    - S289-2889-chemistry-execution
    - S289-2889-stereo-policy
    - S289-2889-intake
- assessment_id: S289-2889-provenance
  area: provenance
  topic: Producer grade, locus method and occurrence grain
  summary: BGC0000418 v5 records SOURCE_ASSERTION Amycolatopsis lurida, NCBITaxon:31959,
    and CLUSTER_UNSTATED linkage with no locus methods or coordinates. Separate ChEBI
    occurrences retain NCBITaxon:1460371 at NRRL 2430 strain scope (cached name Amycolatopsis
    lurida NRRL 2430; PMID:25323720) and Amycolatopsis sp. NCBITaxon:37632, strain
    MJM2582 (PMID:25359910). LOTUS's Nocardia occurrence, DOI:10.1039/C39790000906,
    is another occurrence assertion. None is automatically a causal producer upgrade.
  outcome: supported
  target_ids:
  - CHEBI:85129
  evidence_ids:
  - S289-2889-owner
  - S289-2889-source-reading
  - S289-2889-intake
  - S289-2889-intake-execution
  - S289-2889-seeder
  - S289-2889-bounded-search
  - S289-2889-table-00
  - S289-2889-table-01
  - S289-2889-table-02
  - S289-2889-table-03
  - S289-2889-table-04
  - S289-2889-table-05
  - S289-2889-table-06
  - S289-2889-table-07
  - S289-2889-table-08
  - S289-2889-table-09
  - S289-2889-table-10
  - S289-2889-table-11
  - S289-2889-table-12
  - S289-2889-table-13
  - S289-2889-table-14
  - S289-2889-table-15
  - S289-2889-table-16
  - S289-2889-table-17
  - S289-2889-table-18
  - S289-2889-table-19
  - S289-2889-companion-0
  - S289-2889-companion-1
  - S289-2889-companion-2
  - S289-2889-taxonomy-cache
  - S289-2889-schema
  dimensions:
  - name: evidence_axes
    definition: Separate source producer/locus grades.
    value: SOURCE_ASSERTION producer and CLUSTER_UNSTATED locus; three occurrence
      assertions preserve citation and taxon/strain grain.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-source-reading
    - S289-2889-intake
    - S289-2889-intake-execution
    - S289-2889-seeder
    - S289-2889-bounded-search
    - S289-2889-table-00
    - S289-2889-table-01
    - S289-2889-table-02
    - S289-2889-table-03
    - S289-2889-table-04
    - S289-2889-table-05
    - S289-2889-table-06
    - S289-2889-table-07
    - S289-2889-table-08
    - S289-2889-table-09
    - S289-2889-table-10
    - S289-2889-table-11
    - S289-2889-table-12
    - S289-2889-table-13
    - S289-2889-table-14
    - S289-2889-table-15
    - S289-2889-table-16
    - S289-2889-table-17
    - S289-2889-table-18
    - S289-2889-table-19
    - S289-2889-companion-0
    - S289-2889-companion-1
    - S289-2889-companion-2
    - S289-2889-taxonomy-cache
    - S289-2889-schema
  - name: taxon_and_strain
    definition: Source name, taxon identifier and occurrence granularity.
    value: Species-level producer NCBITaxon:31959; separate NRRL2430 strain occurrence1460371,
      Amycolatopsis sp.37632/MJM2582 and genus Nocardia1817 occurrences.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-taxonomy-cache
    - S289-2889-source-reading
    - S289-2889-table-00
    - S289-2889-table-01
    - S289-2889-table-02
    - S289-2889-table-03
    - S289-2889-table-04
    - S289-2889-table-05
    - S289-2889-table-06
    - S289-2889-table-07
    - S289-2889-table-08
    - S289-2889-table-09
    - S289-2889-table-10
    - S289-2889-table-11
    - S289-2889-table-12
    - S289-2889-table-13
    - S289-2889-table-14
    - S289-2889-table-15
    - S289-2889-table-16
    - S289-2889-table-17
    - S289-2889-table-18
    - S289-2889-table-19
- assessment_id: S289-2889-graph
  area: graph
  topic: Mechanism applicability and activity evidence scope
  summary: The owner has no local graph, graph reference, pathway, target or assay
    items, so a maintained mechanism-reader call is not applicable. Its ANTIBACTERIAL
    summary is instead backed by the exact SAME_STRUCTURE/SAME_INCHIKEY AntibioticMech
    link at pinned corpus commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976. The maintained
    seeder permits that class/link route while withholding transferred targets, MICs
    and mechanism detail. The blank-AID PubChem marker is not a measurement.
  outcome: not_applicable
  target_ids:
  - CHEBI:85129
  evidence_ids:
  - S289-2889-owner
  - S289-2889-capture
  - S289-2889-source-reading
  - S289-2889-bounded-search
  - S289-2889-seeder
  - S289-2889-schema
  - S289-2889-native-scope
  - S289-2889-table-00
  - S289-2889-table-01
  - S289-2889-table-02
  - S289-2889-table-03
  - S289-2889-table-04
  - S289-2889-table-05
  - S289-2889-table-06
  - S289-2889-table-07
  - S289-2889-table-08
  - S289-2889-table-09
  - S289-2889-table-10
  - S289-2889-table-11
  - S289-2889-table-12
  - S289-2889-table-13
  - S289-2889-table-14
  - S289-2889-table-15
  - S289-2889-table-16
  - S289-2889-table-17
  - S289-2889-table-18
  - S289-2889-table-19
  dimensions:
  - name: mechanistic_scope
    definition: Literal whole-owner mechanism applicability.
    value: The owner has no local graph, graph reference, pathway, target or assay
      items, so a maintained mechanism-reader call is not applicable. Its ANTIBACTERIAL
      summary is instead backed by the exact SAME_STRUCTURE/SAME_INCHIKEY AntibioticMech
      link at pinned corpus commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976. The maintained
      seeder permits that class/link route while withholding transferred targets,
      MICs and mechanism detail. The blank-AID PubChem marker is not a measurement.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-capture
    - S289-2889-source-reading
    - S289-2889-bounded-search
    - S289-2889-seeder
    - S289-2889-schema
    - S289-2889-native-scope
    - S289-2889-table-00
    - S289-2889-table-01
    - S289-2889-table-02
    - S289-2889-table-03
    - S289-2889-table-04
    - S289-2889-table-05
    - S289-2889-table-06
    - S289-2889-table-07
    - S289-2889-table-08
    - S289-2889-table-09
    - S289-2889-table-10
    - S289-2889-table-11
    - S289-2889-table-12
    - S289-2889-table-13
    - S289-2889-table-14
    - S289-2889-table-15
    - S289-2889-table-16
    - S289-2889-table-17
    - S289-2889-table-18
    - S289-2889-table-19
  - name: activity_scope
    definition: Class summary versus assay/target/mechanism evidence.
    value: One exact ANTIBACTERIAL sibling-summary row; PubChem CID16131418 marker
      has blank AID and no assay data. No local measurement or copied target.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-capture
    - S289-2889-source-reading
    - S289-2889-bounded-search
    - S289-2889-seeder
    - S289-2889-schema
    - S289-2889-native-scope
    - S289-2889-table-00
    - S289-2889-table-01
    - S289-2889-table-02
    - S289-2889-table-03
    - S289-2889-table-04
    - S289-2889-table-05
    - S289-2889-table-06
    - S289-2889-table-07
    - S289-2889-table-08
    - S289-2889-table-09
    - S289-2889-table-10
    - S289-2889-table-11
    - S289-2889-table-12
    - S289-2889-table-13
    - S289-2889-table-14
    - S289-2889-table-15
    - S289-2889-table-16
    - S289-2889-table-17
    - S289-2889-table-18
    - S289-2889-table-19
- assessment_id: S289-2889-evidence
  area: evidence
  topic: Claim-specific references and complete history
  summary: DOI:10.1128/aac.03512-14 is recorded at MIBiG COMPOUND_EVIDENCE level;
    the ChEBI and LOTUS occurrence references retain their own scope. BGC0000418 also
    contains the B and desmethyl compound rows, but shared entry/citation is not independent
    experiment or identity evidence. Two seed histories are preserved. The sibling
    inventory is inspected; its underlying mechanism and primary papers are not newly
    verified.
  outcome: supported
  target_ids:
  - CHEBI:85129
  evidence_ids:
  - S289-2889-owner
  - S289-2889-source-reading
  - S289-2889-intake
  - S289-2889-intake-execution
  - S289-2889-seeder
  - S289-2889-bounded-search
  - S289-2889-table-00
  - S289-2889-table-01
  - S289-2889-table-02
  - S289-2889-table-03
  - S289-2889-table-04
  - S289-2889-table-05
  - S289-2889-table-06
  - S289-2889-table-07
  - S289-2889-table-08
  - S289-2889-table-09
  - S289-2889-table-10
  - S289-2889-table-11
  - S289-2889-table-12
  - S289-2889-table-13
  - S289-2889-table-14
  - S289-2889-table-15
  - S289-2889-table-16
  - S289-2889-table-17
  - S289-2889-table-18
  - S289-2889-table-19
  - S289-2889-companion-0
  - S289-2889-companion-1
  - S289-2889-companion-2
  - S289-2889-capture
  dimensions:
  - name: citation_scope
    definition: Reference basis and publication independence.
    value: Compound-level DOI:10.1128/aac.03512-14; separate occurrence PMID:25323720/25359910
      and LOTUS DOI; pinned sibling class/link is not a freshly read mechanism.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-source-reading
    - S289-2889-intake
    - S289-2889-intake-execution
    - S289-2889-seeder
    - S289-2889-bounded-search
    - S289-2889-table-00
    - S289-2889-table-01
    - S289-2889-table-02
    - S289-2889-table-03
    - S289-2889-table-04
    - S289-2889-table-05
    - S289-2889-table-06
    - S289-2889-table-07
    - S289-2889-table-08
    - S289-2889-table-09
    - S289-2889-table-10
    - S289-2889-table-11
    - S289-2889-table-12
    - S289-2889-table-13
    - S289-2889-table-14
    - S289-2889-table-15
    - S289-2889-table-16
    - S289-2889-table-17
    - S289-2889-table-18
    - S289-2889-table-19
    - S289-2889-companion-0
    - S289-2889-companion-1
    - S289-2889-companion-2
    - S289-2889-capture
  - name: history_scope
    definition: Complete retained history without inferred state promotion.
    value: Both seed-history events are retained; no current REVIEWED promotion or
      additional curation event is inferred.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-capture
- assessment_id: S289-2889-consistency
  area: consistency
  topic: Chemical classification, source semantics and queue limits
  summary: The NPClassifier Vancomycins and Teicoplanins/Oligopeptides classification
    and glycoside:true are explicit computed outputs. Asserted Glycopeptide compound
    class and NRPS/Type I BGC classification remain separate. The antibacterial summary
    is sourced through the permitted sibling-link rule rather than inferred from the
    computed glycopeptide class.
  outcome: supported
  target_ids:
  - CHEBI:85129
  evidence_ids:
  - S289-2889-owner
  - S289-2889-source-reading
  - S289-2889-intake
  - S289-2889-intake-execution
  - S289-2889-seeder
  - S289-2889-bounded-search
  - S289-2889-table-00
  - S289-2889-table-01
  - S289-2889-table-02
  - S289-2889-table-03
  - S289-2889-table-04
  - S289-2889-table-05
  - S289-2889-table-06
  - S289-2889-table-07
  - S289-2889-table-08
  - S289-2889-table-09
  - S289-2889-table-10
  - S289-2889-table-11
  - S289-2889-table-12
  - S289-2889-table-13
  - S289-2889-table-14
  - S289-2889-table-15
  - S289-2889-table-16
  - S289-2889-table-17
  - S289-2889-table-18
  - S289-2889-table-19
  - S289-2889-companion-0
  - S289-2889-companion-1
  - S289-2889-companion-2
  - S289-2889-schema
  - S289-2889-chemistry
  - S289-2889-native-scope
  - S289-2889-label-exception
  dimensions:
  - name: classification_axes
    definition: Computed classification versus asserted source biology.
    value: The NPClassifier Vancomycins and Teicoplanins/Oligopeptides classification
      and glycoside:true are explicit computed outputs. Asserted Glycopeptide compound
      class and NRPS/Type I BGC classification remain separate. The antibacterial
      summary is sourced through the permitted sibling-link rule rather than inferred
      from the computed glycopeptide class.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-source-reading
    - S289-2889-intake
    - S289-2889-intake-execution
    - S289-2889-seeder
    - S289-2889-bounded-search
    - S289-2889-table-00
    - S289-2889-table-01
    - S289-2889-table-02
    - S289-2889-table-03
    - S289-2889-table-04
    - S289-2889-table-05
    - S289-2889-table-06
    - S289-2889-table-07
    - S289-2889-table-08
    - S289-2889-table-09
    - S289-2889-table-10
    - S289-2889-table-11
    - S289-2889-table-12
    - S289-2889-table-13
    - S289-2889-table-14
    - S289-2889-table-15
    - S289-2889-table-16
    - S289-2889-table-17
    - S289-2889-table-18
    - S289-2889-table-19
    - S289-2889-companion-0
    - S289-2889-companion-1
    - S289-2889-companion-2
    - S289-2889-schema
    - S289-2889-chemistry
    - S289-2889-native-scope
    - S289-2889-label-exception
  - name: queue_scope
    definition: Native diagnostics are leads requiring source interpretation.
    value: Producer, demonstrated-locus and stereo queue entries are interpreted using
      the actual source grades and complete saved forms; they are not automatic findings.
    evidence_ids:
    - S289-2889-native-scope
    - S289-2889-source-reading
    - S289-2889-owner
    - S289-2889-chemistry
- assessment_id: S289-2889-completeness
  area: completeness
  topic: Earned local work and held verification
  summary: The seven review areas were assessed against complete current owners/histories,
    exact retained source rows, cached taxon stanzas, actual canonical intakes and
    both complete saved molecular forms. No evidenced record defect was identified
    in this bounded review. Full QC, complete OAK and fresh external primary-source/taxonomic
    verification remain unavailable or held. Local stored-form parsing, database metadata
    and cached taxonomy do not replace those checks. One exact ANTIBACTERIAL sibling-summary
    row; PubChem CID16131418 marker has blank AID and no assay data. No local measurement
    or copied target.
  outcome: unknown
  target_ids:
  - CHEBI:85129
  evidence_ids:
  - S289-2889-owner
  - S289-2889-intake
  - S289-2889-intake-execution
  - S289-2889-chemistry
  - S289-2889-chemistry-execution
  - S289-2889-native-scope
  - S289-2889-source-reading
  - S289-2889-bounded-search
  dimensions:
  - name: completed_scope
    definition: Work actually read for this owner.
    value: Whole owner and two histories; twenty bounded table frames; 70 actual input
      paths; both complete saved molecular forms; applicable native results.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-intake
    - S289-2889-intake-execution
    - S289-2889-chemistry
    - S289-2889-chemistry-execution
    - S289-2889-native-scope
    - S289-2889-source-reading
    - S289-2889-bounded-search
  - name: unavailable_scope
    definition: Unperformed checks and remaining epistemic limits.
    value: Full QC, complete OAK and fresh external primary-source/taxonomic verification
      remain unavailable or held. Local stored-form parsing, database metadata and
      cached taxonomy do not replace those checks.
    evidence_ids:
    - S289-2889-owner
    - S289-2889-intake
    - S289-2889-intake-execution
    - S289-2889-chemistry
    - S289-2889-chemistry-execution
    - S289-2889-native-scope
    - S289-2889-source-reading
    - S289-2889-bounded-search
- assessment_id: AS289-local-consistency
  area: consistency
  topic: Bounded positive local validation and normalized chemical representation
  outcome: supported
  summary: The selected record is well-formed under the current closed schema and
    reproduces from maintained inputs. The two stored molecular encodings generate
    the declared Standard InChIKey and agree in parsed formula and net charge. These
    positive local results do not establish natural identity, exact graph equivalence,
    strain-specific production or primary-paper support.
  target_ids:
  - CHEBI:85129
  evidence_ids:
  - EV289-strict_ten
  - EV289-reproduction
  - EV289-molecular
findings: []
actions: []
limitations:
- Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized
  Standard InChI/key, declared key, formula, charge and atom/bond counts agree. The
  saved chirality-aware atom map is empty and full_graph_identity_established is false.
  The explicit motif changes explain a representation difference but do not establish
  full graph or natural-sample identity.
- SOURCE_ASSERTION producer and CLUSTER_UNSTATED locus; three occurrence assertions
  preserve citation and taxon/strain grain. Compound-level DOI:10.1128/aac.03512-14;
  separate occurrence PMID:25323720/25359910 and LOTUS DOI; pinned sibling class/link
  is not a freshly read mechanism.
- One exact ANTIBACTERIAL sibling-summary row; PubChem CID16131418 marker has blank
  AID and no assay data. No local measurement or copied target.
- Full QC, complete OAK and fresh external primary-source/taxonomic verification remain
  unavailable or held. Local stored-form parsing, database metadata and cached taxonomy
  do not replace those checks.
- One unspecified tetrahedral centre remains in both stored forms; no natural stereochemical
  assignment was supplied.
- The existing CHEBI:85129 generic-label exception still notes curator confirmation;
  the ANTIBACTERIAL sibling summary is not a direct assay or newly inspected mechanism.
- Full QC, complete OAK label checks and fresh external-source verification are unavailable.
  Completion remains partial despite successful local gates.
- The review source is a working-tree input attestation at the captured Git base.
  Saved validation does not promote native record status or close unrelated historical
  findings.
notes:
- 'Source revision: 18ca5dd6b9023670f10355084b45a8757a7a4e9e; current canonical working-tree
  inputs rehashed exactly.'
- No new source request, mechanism-reader call, molecular parse, record edit or saved-review
  operation was performed by this author.
- ROOT supplies original common check templates and final admission; this fragment
  does not claim full QC, OAK or fresh primary verification.
tags:
- batch-289
- local-evidence
- partial-review
```
