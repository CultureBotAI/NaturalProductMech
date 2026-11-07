# Local evidence review: coumermycin A1

- Review: 20261103T103427Z-coumermycin-a1
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T09:59:30.241054Z
- Finished UTC: 2026-11-03T10:34:27.894429Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

coumermycin A1: qualified partial review of exact structure, retained evidence grades, source boundaries and saved computation; complete accepted maintained mechanism retained with historical experiment/protein limits.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2197; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3907 | data/natural_products/shikimates_and_phenylpropanoids/coumermycin-a1.yaml | generated | coumermycin A1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for coumermycin A1 | passed | True | CHEBI:3907 | Original complete offline maintained resolution preserved the whole owner and exact 23 components; 24 graphs, 335 nodes, 407 edges and 590 references. This is not fresh primary, protein-sequence, natural-identity or mechanism verification. |
| strict_ten | passed | True | CHEBI:3907 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:3907 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:3907 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:3907 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:3907 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:3907 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:3907 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:3907 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding scope

identity: supported. Targets: CHEBI:3907.

Coumermycin A1 retains CHEBI:3907 and full key WTIJXIZOODAMJT-DHFGXMAYSA-N across the exact-key MIBiG, ChEBI and AntibioticMech rows, with neutral C55H59N5O20 in both saved owner-form calculations. BGC0000833 version 4 names this compound at index 1. ChEBI's hydroxycoumarin, antibacterial and anticancer definition is an attributed database assertion, not a newly measured potency result. The retained ChEBI SMILES has aromatic n spellings differing from the owner representation; that third string was not reparsed, and source-key agreement is not proof of equivalence of every source drawing or natural sample.

### Paired molecular representations and stereochemical limits

representation: supported. Targets: CHEBI:3907.

Both owner forms parse with equal standardized InChI/full key, formula, charge and 80-atom/88-bond counts, but both canonical SMILES equality flags are false and the chirality-aware atom correspondence is empty. Saved SMILES contains C32(=O33)–N31 and C40(=O41)–N42 amides; the InChI-derived form contains C45(OH64)=N58 and C46(OH65)=N59. This supports a bounded amide/imidic-acid representation interpretation without proving full graph equivalence, natural tautomer population or a wrong identity. Eight specified tetrahedral centers persist in both forms; two unspecified double-bond entries appear only at the InChI-derived C=N bonds. The maintained atom-centered stereo_complete derivation is narrower than universal geometric or natural stereochemical completeness.

### Producer, occurrence and locus evidence grades

provenance: supported. Targets: CHEBI:3907.

MIBiG assigns Streptomyces rishiriensis NCBITaxon:68264 a BGC_CHARACTERIZED producer grade and BGC0000833 a CLUSTER_DEMONSTRATED link, retaining knockout, enzymatic and heterologous-expression methods. AF235050.4 coordinates 2307–40140 are the deposited locus scope. The 21 LOTUS rows represent three taxa—1886 S. albidoflavus, 1902 S. coelicolor and 68264 S. rishiriensis—crossed with seven citations; they are occurrence assertions, not 21 independent producer experiments. The additional ChEBI-origin row also names S. rishiriensis. Cached names and historical host labels do not transfer native production to a recombinant host.

### Citation placement and historical verification scope

evidence: supported. Targets: CHEBI:3907.

PMID:14285468 is the MIBiG ENTRY-level citation; PMID:24079980 is the ChEBI-origin citation; the seven retained LOTUS DOI strings retain their individual occurrence placements. Publication independence across those claims has not been established. The whole inline graph, 23 components and their histories preserve primary-experiment labels, quotations, source conflicts and prior inspection annotations, but no original article, API response or protein sequence was newly inspected in this review. Their historical annotations are not promoted to fresh external verification.

### Occurrence, assay and companion boundaries

scope: supported. Targets: CHEBI:3907.

The exact-key AntibioticMech row supports the coarse ANTIBACTERIAL summary and SAME_STRUCTURE link at pinned sibling commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976; it supplies no new molecular target or quantitative assay. The PubChem row for CID 54720057 has blank AID and assay fields, so it is an empty-assay sentinel, not an inactive result. The owner has no written bioactivity observations or molecular targets. ChEBI's anticancer wording and the enzyme-component substrate assays remain separate evidence scopes; neither becomes a compound dose-response or a clinical claim. The 22 written occurrence assertions remain distinct from production.

### Computed classification and full-table topology limits

other: supported. Targets: CHEBI:3907.

The pinned NPClassifier model reports Coumarins, Simple coumarins and is_glycoside true; MIBiG SACCHARIDE/OTHER and aminocoumarin annotations remain source cluster descriptions. Both saved molecular forms contain two saturated C5O candidate rings, two terminal methylpyrrole ester linkages, two aromaticized coumarin systems and a central substituted pyrrole. SMILES ester sites C6(=O7)–O8–C9 and C63(=O64)–O62–C54 are distinct from the aromatic ring oxygens that the generic SINGLE-bond ester scan omits. Two amide sites disappear from that motif class in the imidic representation. These topological observations do not independently assign biochemical sugar positions, natural configuration, reaction order or in-vivo mechanism.

### Partial scientific completion and maintained ownership

completeness: supported. Targets: CHEBI:3907.

The complete owner with 13 history events and all 23 components with 30 component-history events were personally read. The accepted original maintained reader preserves the entire owner and appends those 23 graphs exactly once: 24 graphs, 335 nodes, 407 edges and 590 graph-reference placements; no pathway steps or molecular targets are added. This is structural preservation and maintained resolution, not independent verification of the historical biochemical claims. Original local gates passed, while full QC, ontology authority coverage and external source verification remain unavailable. The review stays partial and does not alter native status, scientific records or curation histories.

### Complete maintained mechanism and biochemical experiment boundaries

graph: supported. Targets: CHEBI:3907.

The accepted maintained view preserves the inline CouL graph and all 23 ordered components. CouL's unglycosylated monoamide/diamide experiments retain unresolved monoamide position, substrate scope, ATP/enzyme-loading source conflicts, conditional apparent Km/Vmax and censored relative endpoints; they do not reconstruct mature A1 or establish native flux. CouO lysate endpoints and SAH/docking models, CouN1/N7 carrier-shuttling experiments, CouR heterologous genetics/isotope/ATPase evidence, CouN2–6 native mutants and CouM/P tandem reactions remain distinct. Genetic complementation is not chemical rescue; small product peaks or bounded nondetection are not numerical zero. Surrogate compounds, congener enzymes, engineered analogues and heterologous hosts are not silently replaced with the native complete pathway. Conflicts are retained explicitly in the corresponding components rather than resolved by the successful reader.

### Native references, engineered constructs and protein-claim limits

grounding: supported. Targets: CHEBI:3907.

Native protein references are kept separate from tagged/engineered preparations and historical versioned constructs. CouL Q9F8U8/AAG29784.2/AF235050.4 is a 529 aa reference, not proof of the exact His6 assay construct; historical 384–385 RA versus current EG and unverified full plasmid sequence remain scoped. CouO's native 230 aa reference does not establish equal active fractions in its lysate mutant panel. CouR2/CouR6 and CouN2–6 sequence revisions, the CouN3/CloN3 accession conflict, CouN4 allele/probe conflicts and native versus congener oxidation assays remain explicit. CouM 402 aa/CouP 276 aa references and an added novobiocin NovN experiment do not establish native coumermycin terminal tailoring. No primary article/API response or protein sequence was newly inspected here; UniProt/GenBank/PDB names, sequence strings and historical inspection notes remain retained source claims, not fresh grounding verification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2197-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/coumermycin-a1.yaml; Complete raw owner, lines 1-932. | supports | Complete owner and all 13 history events personally read; exact current bytes preserved. |
| support-2197-capture | /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json; /records/6/owner_document; /records/6/owner_pin; /records/6/read_started_at; /records/6/read_finished_at | supports | Actual complete captured owner, source pin and original read clocks; component resolution is separate. |
| support-2197-intake | /private/tmp/npm-review-work/shared-next-batch220/intakes/2197-inspect-001.json; /status; /source; /targets/0 | supports | Original inspection-only intake, 62 current inputs, exact target and maintained ownership. |
| support-2197-intake-ready | /private/tmp/npm-review-work/shared-next-batch220/root-intake-ready-001.json; /status; /records/6; /source_placements; /unique_source_paths; /external_requests | supports | ROOT acceptance of the original ten intakes and exact 455/123 source maps. |
| support-2197-source-plan | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6 | supports | Complete owner source plan: raw/history, all nine query frames, positive payloads, route sets, direct companions and input paths. |
| support-2197-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch220/root-source-plan-acceptance-001.json; /status; /plan; /source_notes; /actual_intake_ready; /verified | supports | ROOT joins the earned source plan to the accepted inventory and actual intake maps. |
| support-2197-source-notes | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-scope-notes-001.json; /reading; /cautions; /totals | supports | Complete-source-reading attribution and retained source cautions; no new primary verification is asserted. |
| support-2197-curation-scope | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-scope-notes-001.json; /curation | supports | Completed 142-literal-token scan over eight explicitly opened tables including ignored files: 101 physical lines/93 data rows, zero matches within that exact scope. |
| support-2197-chemistry | /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json; /records/6/declared_structure; /records/6/literal_InChI_layers; /records/6/smiles; /records/6/inchi; /records/6/comparisons; /records/6/atom_correspondence | supports | Complete saved paired molecular computations, literal source stereo flag, exact comparisons and atom-map limits. No additional molecule was parsed. |
| support-2197-topology | /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed; /records/6/inchi/computed | supports | Both complete atom/bond/ring/stereo/motif tables personally read: 80 atoms and 88 bonds per form. Topology motifs are not natural-identity proof. |
| support-2197-chemistry-execution | /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /stdout; /stderr; /output; /external_requests | supports | Original twenty-form diagnostic exited 0 with empty original stderr; no new parse, retry or owner-specific warning assignment. |
| support-2197-chemistry-acceptance | /private/tmp/npm-review-work/shared-next-batch220/root-chemistry-acceptance-001.json; /status; /data; /execution; /records/6; /scope | supports | ROOT accepts the saved original diagnostic while preserving false comparisons and scientific limits. |
| support-2197-native-acceptance | /private/tmp/npm-review-work/shared-next-batch220/root-native-gates-acceptance-001.json; /status; /ledger; /outcomes; /reading | supports | Five original local gates passed; full QC and ontology consistency/OAK remain unavailable. Selected queue rows are diagnostic leads. |
| support-2197-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165-172. | supports | Maintained stereo_complete derives from unassigned atom-centered FindMolChiralCenters output; it is not universal geometric, axial or natural stereochemical completeness. |
| support-2197-source-ownership | /private/tmp/npm-review-work/shared-next-batch220/intakes/2197-inspect-001.json; /targets/0/owner_paths; /targets/0/ownership_note | supports | Generated fields belong to retained inventories/extractors/seeder; curated mechanism owner/components and their histories have separately stated validated-writer ownership. |
| support-2197-taxon-1886 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /cached_taxonomy/whole_stanzas/2 | supports | Complete cached stanza for NCBITaxon:1886; literal labels/synonyms, not fresh taxonomy authority. |
| support-2197-taxon-1902 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /cached_taxonomy/whole_stanzas/3 | supports | Complete cached stanza for NCBITaxon:1902; literal labels/synonyms, not fresh taxonomy authority. |
| support-2197-taxon-68264 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /cached_taxonomy/whole_stanzas/19 | supports | Complete cached stanza for NCBITaxon:68264; literal labels/synonyms, not fresh taxonomy authority. |
| support-2197-taxon-routes | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6/source_scope_inventory/source_taxa; /records/6/source_scope_inventory/forward_taxon_merge_matches; /records/6/source_scope_inventory/nonorganism_matches | supports | Exact saved taxon route sets; no forward merge/non-organism hit for this selected owner. |
| support-2197-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6/source_scope_inventory/joins/mibig_compounds | supports | Complete retained mibig_compounds predicate/query and all 1 matches; empty results refer only to this frozen query. |
| support-2197-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical lines 906-906; exact complete TSV record SHA256 cb9e5d76e06fbd39c3ec56a879a3e390ee507c3d90eb5273e498a8774be30577. | supports | Retained row fields: {"mibig_accession":"BGC0000833","entry_version":"4","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"coumermycin A1","compound_index":"1","smiles":"CC1=CC=C(N1)C(=O)O[C@H]2[C@H]([C@@H](OC([C@@H]2OC)(C)C)OC3=C(C4=C(C=C3)C(=C(C(=O)O4)NC(=O)C5=CNC(=C5C)C(=O)NC6=C(C7=C(C(=C(C=C7)O[C@H]8[C@@H]([C@@H]([C@H](C(O8)(C)C)OC)OC(=O)C9=CC=C(N9)C)O)C)OC6=O)O)O)C)O","standard_inchi":"InChI=1S/C55H59N5O20/c1-21-12-16-29(57-21)48(67)77-42-38(63)52(79-54(6,7)44(42)71-10)73-31-18-14-26-36(61)34(50(69)75-40(26)24(31)4)59-46(65)28-20-56-33(23(28)3)47(66)60-35-37(62)27-15-19-32(25(5)41(27)76-51(35)70)74-53-39(64)43(45(72-11)55(8,9)80-53)78-49(68)30-17-13-22(2)58-30/h12-20,38-39,42-45,52-53,56-58,61-64H,1-11H3,(H,59,65)(H,60,66)/t38-,39-,42+,43+,44-,45-,52-,53-/m1/s1","standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:54675768&#124;pubchem:54720057","taxon_id":"NCBITaxon:68264","taxon_label":"Streptomyces rishiriensis","bgc_classes":"saccharide&#124;other","bgc_subclasses":"hybrid/tailoring&#124;aminocoumarin","genome_accession":"AF235050.4","locus_from":"2307","locus_to":"40140","locus_evidence_methods":"Knock-out studies&#124;Enzymatic assays&#124;Heterologous expression","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:14285468","reference_basis":"ENTRY"} |
| support-2197-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6/source_scope_inventory/joins/chebi_structures | supports | Complete retained chebi_structures predicate/query and all 1 matches; empty results refer only to this frozen query. |
| support-2197-row-chebi_structures-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Physical lines 754-754; exact complete TSV record SHA256 cce8438bd10c6450ef7fd7c60c91c122514c891c5d6acf6d7bcb8b8b2057a25f. | supports | Retained row fields: {"chebi_id":"CHEBI:3907","name":"coumermycin A1","definition":"A hydroxycoumarin antibiotic that is obtained from Streptomyces rishiriensis and exhibits potent antibacterial and anticancer activity.","stars":"3","standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","smiles":"CO[C@@H]1[C@@H](OC(=O)c2ccc(C)n2)[C@@H](O)[C@H](Oc2ccc3c(O)c(NC(=O)c4cnc(C(=O)Nc5c(O)c6ccc(O[C@@H]7OC(C)(C)[C@H](OC)[C@@H](OC(=O)c8ccc(C)n8)[C@H]7O)c(C)c6oc5=O)c4C)c(=O)oc3c2C)OC1(C)C"} |
| support-2197-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained lotus_occurrences predicate/query and all 21 matches; empty results refer only to this frozen query. |
| support-2197-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9377-9377; exact complete TSV record SHA256 442f427691834f8e450a81acd327a3c6bb8740931a1e0de3b0bad458bdc47b16. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1002/BIP.21493","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9378-9378; exact complete TSV record SHA256 c1b367ffd57b6b2a39af81fd5656415ebe04e410e0bb2c099cf87d59d57c5cd3. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1007/S10295-013-1348-5","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-2 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9379-9379; exact complete TSV record SHA256 21a1365b1ec5fc17087e3d1dc89fd2e59b9c46efd06784b9eb50bee37996d51f. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1046/J.1432-1033.2003.03830.X","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-3 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9380-9380; exact complete TSV record SHA256 06cad44e0d8e4ec04893dc340217baccfe7e2d42893ee340d222293dec2449c8. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1099/00221287-148-10-3317","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-4 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9381-9381; exact complete TSV record SHA256 9c977861666ab24e0211bd5f9ffa0436fc47a6c6724bc358e0c438fbf8d3c783. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1099/MIC.0.26867-0","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-5 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9382-9382; exact complete TSV record SHA256 627e1d3ba977f39b0f4a5cc79cd48d0b54579488914c94b7884db4316ffe0612. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1128/AAC.44.11.3040-3048.2000","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-6 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9383-9383; exact complete TSV record SHA256 7be8cd3949f566e40f6926bb723289d101eee102f502839bb23e3743e3eb9924. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1371/JOURNAL.PONE.0171056","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-7 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9384-9384; exact complete TSV record SHA256 b21728538de08b1ae2ef58bf2ab3319d1ef9bf74908ab86adefcff508a08e72e. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1002/BIP.21493","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-8 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9385-9385; exact complete TSV record SHA256 6002f578facf937b27160c9926bf3b3e5cc344ef83964752f641ce233bf7a190. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1007/S10295-013-1348-5","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-9 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9386-9386; exact complete TSV record SHA256 0baedbc8b8c3876e57ebf507ca843445df5731dbaf1556cec7e6000ce0b2551f. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1046/J.1432-1033.2003.03830.X","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-10 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9387-9387; exact complete TSV record SHA256 67c9b3a97b13b4199a1a876909b3ea710ac7fad49ab999f4eb33ddf84b720b45. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1099/00221287-148-10-3317","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-11 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9388-9388; exact complete TSV record SHA256 04e5972baa5a832f86e55f256278021e9086cd7ba1e763dcee7b77d5303cd1ed. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1099/MIC.0.26867-0","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-12 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9389-9389; exact complete TSV record SHA256 4406b3485ef19892f4260c225d1ef544abe51397b42b18eb2cddf7c1892b5d7e. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1128/AAC.44.11.3040-3048.2000","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-13 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9390-9390; exact complete TSV record SHA256 c21daf0e50b5303e4ce389443eb85c01231e99a754fe13396d79384d0ddad040. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1371/JOURNAL.PONE.0171056","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-14 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9391-9391; exact complete TSV record SHA256 e1edad48b1bc55013da1e68f53d38169ea39d02f5ccf0cd826b16e7ab81734cb. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1002/BIP.21493","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-15 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9392-9392; exact complete TSV record SHA256 4f31128e419d0b71ab692f8b60b100a5979c611bfc6725aecf9f4f49d01271a0. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1007/S10295-013-1348-5","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-16 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9393-9393; exact complete TSV record SHA256 b7003d6d8320fe7351df8565d76f2b16893d72eead8e15151a4a46dcc7e0a748. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1046/J.1432-1033.2003.03830.X","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-17 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9394-9394; exact complete TSV record SHA256 43dc85bcedb1c67977fef9d6ef19c323d599834119f8e7850547b7b9ac0a7b40. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1099/00221287-148-10-3317","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-18 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9395-9395; exact complete TSV record SHA256 f7e91dd450e045cdc539acbd5fe37c165d3c1295445d3828e108944d861242d0. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1099/MIC.0.26867-0","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-19 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9396-9396; exact complete TSV record SHA256 cafd17f021d5e120314faad7564dffdd751caf820895ad2081874fdf0dbf0f84. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1128/AAC.44.11.3040-3048.2000","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-row-lotus_occurrences-20 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical lines 9397-9397; exact complete TSV record SHA256 16af19ed4cad9c553ed0c52e1cdc52cf5fdb8f1b37c6e855e552f9ea203a3dea. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1371/JOURNAL.PONE.0171056","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"} |
| support-2197-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained cyanometdb_occurrences predicate/query and all 0 matches; empty results refer only to this frozen query. |
| support-2197-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6/source_scope_inventory/joins/npclassifier | supports | Complete retained npclassifier predicate/query and all 1 matches; empty results refer only to this frozen query. |
| support-2197-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical lines 2691-2691; exact complete TSV record SHA256 d22f3bf32145b570a21039a37325d7b58fbef18681d32b1875c05047e04068fd. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","smiles":"CC1=CC=C(N1)C(=O)O[C@H]2[C@H]([C@@H](OC([C@@H]2OC)(C)C)OC3=C(C4=C(C=C3)C(=C(C(=O)O4)NC(=O)C5=CNC(=C5C)C(=O)NC6=C(C7=C(C(=C(C=C7)O[C@H]8[C@@H]([C@@H]([C@H](C(O8)(C)C)OC)OC(=O)C9=CC=C(N9)C)O)C)OC6=O)O)O)C)O","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Coumarins","class_results":"Simple coumarins","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07"} |
| support-2197-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained pubchem_bioassay predicate/query and all 1 matches; empty results refer only to this frozen query. |
| support-2197-row-pubchem_bioassay-0 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical lines 8773-8773; exact complete TSV record SHA256 e6768903aef6e6d089c7eef672fa41e5385e2742be3002f1cf0f04518e65f7c3. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","cid":"54720057","aid":"","assay_name":"(no assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""} |
| support-2197-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained bindingdb_targets predicate/query and all 0 matches; empty results refer only to this frozen query. |
| support-2197-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained antibioticmech_inchikeys predicate/query and all 1 matches; empty results refer only to this frozen query. |
| support-2197-row-antibioticmech_inchikeys-0 | /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv; Physical lines 2491-2491; exact complete TSV record SHA256 8104484e41b9ee5bb858fe9a821ea49e3353aa0d14e62bbbe1af31fc04da98c7. | supports | Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","identifier":"CHEBI:3907","label":"coumermycin A1","antimicrobial_class":"ANTIBACTERIAL","slug":"coumermycin-a1","corpus_commit":"74f6cc8362498900f2fe2c13d0b6fdb66dd30976"} |
| support-2197-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/6/source_scope_inventory/joins/chebi_origins | supports | Complete retained chebi_origins predicate/query and all 1 matches; empty results refer only to this frozen query. |
| support-2197-row-chebi_origins-0 | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Physical lines 351-351; exact complete TSV record SHA256 035e8e79f07141761980b34c669191d3b447a02acfb60bc50f76043bb0fae715. | supports | Retained row fields: {"chebi_id":"CHEBI:3907","species_text":"Streptomyces rishiriensis","species_accession":"68264","component_text":"","strain_text":"","source_accession":"24079980","comments":""} |
| support-2197-component-0 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-native-identity-and-precursor-evidence.yaml; Complete component and history, lines 1-168. | supports | Native CouO reference and precursor identity remain separate from engineered assay constructs and surrogate substrates. |
| support-2197-component-1 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-constructs-and-soluble-protein-preparations.yaml; Complete component and history, lines 1-696. | supports | WT and ten mutant preparations retain literal construct/primer/protein claims; full plasmids and assay constructs were not freshly sequence-verified. |
| support-2197-component-2 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-lysate-normalization-and-mutant-endpoint-limits.yaml; Complete component and history, lines 1-575. | supports | Cleared-lysate 24 h surrogate endpoints use normalized CouO content, not equal active enzyme. Variable soluble content, H120A solubility, relative triplicate ranges and near-background mutants do not establish kcat or numerical zero. |
| support-2197-component-3 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-sah-structure-dimer-and-model-limits.yaml; Complete component and history, lines 1-254. | supports | 5M58 is an SAH-bound structure; SAM/coumarin docking and NovO analogy are models. Missing chain terminal density, Glu4/Glu6 conflict and condition-specific dimer evidence remain explicit. |
| support-2197-component-4 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-native-identities-and-annotation-limits.yaml; Complete component and history, lines 1-165. | supports | CouN1/7 native references are 95/281 aa; submitted hydrolase/lipase annotations are not measured native reaction specificity. |
| support-2197-component-5 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-carrier-loading-and-terminal-transfer.yaml; Complete component and history, lines 1-224. | supports | Sfp/synthetic acyl-CoA carrier loading and terminal transfer retain exact substrate/cofactor scope. Novobiocin surrogate use is not native mature-coumermycin reconstitution. |
| support-2197-component-6 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-reversible-shuttling-and-covalent-intermediate.yaml; Complete component and history, lines 1-188. | supports | S101A radiolabeled-acetyl trapping supports the reported covalent-intermediate experiment without establishing atomic structure, folding controls or all native transfer rates. |
| support-2197-component-7 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-engineered-substrate-panel-and-supporting-material-limits.yaml; Complete component and history, lines 1-218. | supports | The 21-variant aggregate and 23-donor headings remain distinct; chemical synthesis SI is not a full enzyme-activity matrix and nomenclature conflicts are not silently resolved. |
| support-2197-component-8 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-native-identities-and-sequence-revisions.yaml; Complete component and history, lines 1-421. | supports | CouR2 old 377 aa versus revised 172/205 aa proteins and CouR6 old 290/current 291 aa retain version and coordinate uncertainty; revisions are not proven assay-construct sequences. |
| support-2197-component-9 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-individual-deletion-constructs-and-pcr-limits.yaml; Complete component and history, lines 1-458. | supports | Individual CouR deletions in heterologous M1146 retain PCR/genotype and polar-effect limits; historical restriction coordinates are not complete current allele sequences. |
| support-2197-component-10 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-genetic-titers-cpm-feeding-and-partial-rescue.yaml; Complete component and history, lines 1-372. | supports | Reported intact 10.20 mg/L and deletion/CPM-feed titers are conditional endpoints. Censored less-than 0.01 values are not zero; chemical rescue is not genetic complementation; only stated R1/R4 genetic rescues carry. |
| support-2197-component-11 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-phosphothreonine-feeding-and-strain-label-conflict.yaml; Complete component and history, lines 1-149. | supports | Phosphothreonine feeding retains 44 percent average increase and conflicting AK08/AK09 strain labels; this does not demonstrate the kinase reaction. |
| support-2197-component-12 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-isotope-precursor-evidence-and-historical-pathway-model.yaml; Complete component and history, lines 1-265. | supports | Threonine isotope incorporation supports four carbons plus nitrogen of the central pyrrole, while remaining carbon origin and historical pathway models remain unresolved. |
| support-2197-component-13 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-minimal-expression-constructs-and-coordinate-limits.yaml; Complete component and history, lines 1-325. | supports | Minimal heterologous constructs and coordinate/primer models do not constitute a purified full pathway or native essentiality experiment. |
| support-2197-component-14 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-heterologous-cpm-production-and-unit-limits.yaml; Complete component and history, lines 1-223. | supports | Heterologous CPM production retains the indexed mg/mL unit conflict and strain/context limits; no silent unit conversion or mature-antibiotic yield inference. |
| support-2197-component-15 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-cour3-preparation-atpase-and-unconfirmed-kinase.yaml; Complete component and history, lines 1-228. | supports | His8 CouR3 ATPase activity and no observed threonine dependence are not threonine phosphorylation or proof that no substrate can exist. |
| support-2197-component-16 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-native-identities-and-version-conflicts.yaml; Complete component and history, lines 1-319. | supports | CouN2–6 native accessions/version changes and the historical CouN3/CloN3 accession error remain separated; old/new protein lengths are not natural polymorphism proof. |
| support-2197-component-17 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-coun3-deletion-and-historical-allele-limits.yaml; Complete component and history, lines 1-178. | supports | Native CouN3 historical 480 bp deletion/restriction model and Southern controls retain allele-version limits; current protein length is not substituted into the old construct. |
| support-2197-component-18 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-coun4-insertion-and-source-conflicts.yaml; Complete component and history, lines 1-174. | supports | CouN4 aphII insertion retains couN3 naming and 870 bp/1350 bp probe conflicts; genotype uncertainty is preserved rather than repaired by prose. |
| support-2197-component-19 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-native-genetic-phenotypes-and-product-boundaries.yaml; Complete component and history, lines 1-284. | supports | Native mutant losses are bounded detection results; CoumerD activity values and N4 HPLC versus N3 LCMS evidence do not establish improved coumermycin A1 yield or equal analytical coverage. |
| support-2197-component-20 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-proline-loading-and-oxidation-assay-boundaries.yaml; Complete component and history, lines 1-214. | supports | CouN4 prolyl-AMP/loading evidence remains distinct from rapid-quench oxidation attributed to CloN3 rather than CouN3; congener enzymes are not merged. |
| support-2197-component-21 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coump-native-references-and-bounded-tandem-reactions.yaml; Complete component and history, lines 1-307. | supports | CouM 402 aa/CouP 276 aa native references and staged tandem reactions remain bounded. Added NovN is a novobiocin enzyme and an engineered biscarbamoylated analogue is not mature terminal-pyrrole A1. |
| support-2197-component-22 | /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coump-coup-deletion-and-demethyl-product-boundaries.yaml; Complete component and history, lines 1-148. | supports | CouP-deletion demethyl-product abundance compares different molecules, not increased A1 yield; abstract-level observations do not add missing calibration or replication. |
| support-2197-reader-data | /private/tmp/npm-review-work/shared-next-batch220/native-current220-coumermycin-a1-maintained-reader-DATA-001.json; /status; /reader_call_count; /review_check_metadata; /raw_owner; /component_captures; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner; /counts; /denials; /unexpected_denials; /errors; /limitations | supports | One accepted maintained call preserved the complete owner and ordered 23 appends: 24 graphs, 335 nodes, 407 edges; all raw/history fields carry. Known socket capability probe denied before action; no request or fresh scientific authority. |
| support-2197-reader-execution | /private/tmp/npm-review-work/shared-next-batch220/native-current220-coumermycin-a1-reader-execution-001.json; /command; /source; /configuration; /started_at; /finished_at; /exit_code; /original_tool; /stdout; /stderr; /DATA; /external_requests | supports | Original Coumermycin reader process exited 0 with empty stderr and preserved original tool/process/streams; no replay. |
| support-2197-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch220/root-current220-coumermycin-a1-reader-acceptance-001.json; /status; /order; /DATA; /execution; /verification; /review_check_contract; /scientific_scope | supports | ROOT accepts complete-owner equality, exact positive content and original 0; 590 graph references remain historical source annotations. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-220/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-220/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-220/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-220/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-220/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Full QC and complete ontology authority coverage/OAK were unavailable; passing local gates do not establish scientific completeness.
- No external requests, primary-article retrieval or live taxonomy/identifier/protein queries were performed. These assessments use the original saved owner-form computations, with no additional molecular parses during fragment authoring.
- Source citations, database labels, model predictions and historical annotations retain their stated evidence types; no publication independence or natural-identity proof is inferred from matching keys.
- No source record, component or curation history was edited by this review. Canonical review persistence and campaign publication are separate ROOT-owned operations.
- The original reader resolves/preserves complete content; it does not verify historical primary claims, protein sequences, constructs, natural mechanism or stereochemistry.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Raw/source/cache/curation and molecular reading attribution is preserved in the fragment metadata and source-scope notes.
- No finding in this bounded review closes an existing issue or proves absence of uncertainty outside the inspected scope.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T103427Z-coumermycin-a1
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: coumermycin A1'
started_at: '2026-11-03T09:59:30.241054Z'
finished_at: '2026-11-03T10:34:27.894429Z'
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
summary: 'coumermycin A1: qualified partial review of exact structure, retained evidence
  grades, source boundaries and saved computation; complete accepted maintained mechanism
  retained with historical experiment/protein limits.'
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
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coump-coup-deletion-and-demethyl-product-boundaries.yaml
    sha256: 3393544c720602178971fbca625864d0c000b59c4b6fe81e0643ed8d4028bb57
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coump-native-references-and-bounded-tandem-reactions.yaml
    sha256: c4794c900fa7f9f618d8d55107b882a9c03e96aff010f3167fd3900606c544cc
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-carrier-loading-and-terminal-transfer.yaml
    sha256: 300b8f85cf756435114a90f5358937e4cac0ffdeb4ea230436cabc39d61a5a18
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-engineered-substrate-panel-and-supporting-material-limits.yaml
    sha256: 845b497d571bccdb1d1305434c9c165f649091af14802692ea9d647de63fe3c0
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-native-identities-and-annotation-limits.yaml
    sha256: f9a7461ea3af618f627311d2d6b663162fb41a690301be3e7c15cb5d19dd6111
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-reversible-shuttling-and-covalent-intermediate.yaml
    sha256: 50e4f0be584a3c74664fe468cf6b0a252af60dffec6871e52f1d53fb4a81f035
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-coun3-deletion-and-historical-allele-limits.yaml
    sha256: 74f7ccce61cf77409be077d68b23526707dc3552ebeb71e28f2d7276bcadcada
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-coun4-insertion-and-source-conflicts.yaml
    sha256: 53a911bcec5316c802c019d51c619e80367dacf30a92af9396608a20d8004957
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-native-genetic-phenotypes-and-product-boundaries.yaml
    sha256: a80e4f86bf97d1282bee63ef3c9865075a05ba395b6420a6b6d5a3e9c5e0e151
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-native-identities-and-version-conflicts.yaml
    sha256: fdbef28a3f445efa3b3555c0d25d3e83420af65ff2ff21e5aa19cc2b46203129
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-proline-loading-and-oxidation-assay-boundaries.yaml
    sha256: 1d0ab86d450ed025fc32e9f45e39dbc2710283ca6228d61b41146347948fc9e9
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-constructs-and-soluble-protein-preparations.yaml
    sha256: c0e04abf16d7ab6e64b1ce07e13a9497413502093d90576ade44a31f318a189e
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-lysate-normalization-and-mutant-endpoint-limits.yaml
    sha256: 1b3e54226e40adb0e88b7649b1f5d024a1f32434baeb436ce5a3a2ca9680b3fe
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-native-identity-and-precursor-evidence.yaml
    sha256: f13039b270d6fc042ac03927b5055da74d7dc29fe8e2357a27cef0f3f8227f7c
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-sah-structure-dimer-and-model-limits.yaml
    sha256: c73eb5e39d86145b997a2da9d27dda6711db749981d81c2bdc80d30159ec2308
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-cour3-preparation-atpase-and-unconfirmed-kinase.yaml
    sha256: 76bd74ba4b3a42390cd419c137b9cf7aef8d1ef352f0cae7913657c2c22146b7
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-genetic-titers-cpm-feeding-and-partial-rescue.yaml
    sha256: 5492b6b7b32c41acec058a6de22da326625fb4e6286c0a379cb9882d8cc5ae2c
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-heterologous-cpm-production-and-unit-limits.yaml
    sha256: ff89076526e22bcd73e47f38f077c3762c667fa423116c60f724027656b7562e
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-individual-deletion-constructs-and-pcr-limits.yaml
    sha256: d75abb21881f1f5907b3969443a7b432f25831b11f894689b67942dd5b904ccb
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-isotope-precursor-evidence-and-historical-pathway-model.yaml
    sha256: 97cb886fbfb5a5c5f03bfdff643b33c9fa3048e874992ca59aa5b51e154ff292
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-minimal-expression-constructs-and-coordinate-limits.yaml
    sha256: 3b0477348a58babe5ea904b31c96c94ed91aaa261c70c6ca1b6ab8b8f9df1d3e
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-native-identities-and-sequence-revisions.yaml
    sha256: 85ad3fce986966bcdf8522e75815e2a9e2cfeb39bf5e666cc0de71ba90e86c47
    role: context
  - path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-phosphothreonine-feeding-and-strain-label-conflict.yaml
    sha256: 02d9625f953fa9fe9b2d7dd43f648946fb9c59a0712a32f9fb543062996ff0fc
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/coumermycin-a1.yaml
    sha256: d6403ffb0f4d4c4d6bea614c6efdc77cd73c07f1807505f8a6ea732cb7356e85
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
  selection: Campaign path order 2197; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3907
targets:
- target_id: CHEBI:3907
  path: data/natural_products/shikimates_and_phenylpropanoids/coumermycin-a1.yaml
  label: coumermycin A1
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
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned full-key AntibioticMech structure links and coarse activity summaries;
      no transfer of mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/shikimates_and_phenylpropanoids/coumermycin-a1.yaml
    role: Curator-owned declared graphs, graph references, pathway steps and history;
      imported molecular-target assertions and other seeded fields retain inventory
      ownership. Curated graph/pathway changes require the validated writer and a
      curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-native-identity-and-precursor-evidence.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-constructs-and-soluble-protein-preparations.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-lysate-normalization-and-mutant-endpoint-limits.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-sah-structure-dimer-and-model-limits.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-native-identities-and-annotation-limits.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-carrier-loading-and-terminal-transfer.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-reversible-shuttling-and-covalent-intermediate.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-engineered-substrate-panel-and-supporting-material-limits.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-native-identities-and-sequence-revisions.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-individual-deletion-constructs-and-pcr-limits.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-genetic-titers-cpm-feeding-and-partial-rescue.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-phosphothreonine-feeding-and-strain-label-conflict.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-isotope-precursor-evidence-and-historical-pathway-model.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-minimal-expression-constructs-and-coordinate-limits.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-heterologous-cpm-production-and-unit-limits.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-cour3-preparation-atpase-and-unconfirmed-kinase.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-native-identities-and-version-conflicts.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-coun3-deletion-and-historical-allele-limits.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-coun4-insertion-and-source-conflicts.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-native-genetic-phenotypes-and-product-boundaries.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-proline-loading-and-oxidation-assay-boundaries.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coump-native-references-and-bounded-tandem-reactions.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coump-coup-deletion-and-demethyl-product-boundaries.yaml
    role: Exact-owner curated graph component and its history; component changes require
      write_validated_graph_bundle and an artifact-specific curation event.
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners. This mechanism-bearing owner requires separately
    authorized complete maintained resolution before scientific assessment and draft
    assembly. Raw owner capture is not a maintained resolved view.
checks:
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for coumermycin A1
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch220/read-selected-mechanism-guarded-001.py
    2197 69d08ec74c6977d72d2a3e3d009b85f55694f702ede69996831b3fb69d5d9a8c af59aa75171e0fe7a2a05e93fab191f0dcbddca593a08142df29efab0c113b75
    4cb727bc012b60f38c4c7ab4e836df44ab3e6de564f5a3f049b5f4b909a92c86 90236bcdb9064859a691606fd163f92576040ab44a954a6323cc0b39871e571d
    12ce40bf4d89ad17c0e207a877f813db30acdf3ccb71a015cc99e907d1a5a9d5
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CHEBI:3907
  evidence_ids:
  - support-2197-reader-data
  - support-2197-reader-execution
  - support-2197-reader-acceptance
  summary: Original complete offline maintained resolution preserved the whole owner
    and exact 23 components; 24 graphs, 335 nodes, 407 edges and 590 references. This
    is not fresh primary, protein-sequence, natural-identity or mechanism verification.
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:3907
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/chartreusin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/chlorflavonin.yaml data/natural_products/shikimates_and_phenylpropanoids/clorobiocin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/colletorin-d-acid.yaml data/natural_products/shikimates_and_phenylpropanoids/collinomycin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml data/natural_products/shikimates_and_phenylpropanoids/coumermycin-a1.yaml
    data/natural_products/shikimates_and_phenylpropanoids/dichlorodiaporthin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/e-n-2-hydroxy-5-oxocyclopent-1-en-1-yl-5-o-tolyl-pent-4-enamide.yaml
    data/natural_products/shikimates_and_phenylpropanoids/echoside-a.yaml --workers
    1 --out /private/tmp/npm-native-checks/batch-220/validate-strict-selected10-001.tsv
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
  - CHEBI:3907
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-220/validate-all-001.tsv
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
  - CHEBI:3907
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
  - CHEBI:3907
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
  - CHEBI:3907
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-220/review-queue-001.tsv
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
  - CHEBI:3907
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:3907
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:3907
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2197-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/coumermycin-a1.yaml
  locator: Complete raw owner, lines 1-932.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete owner and all 13 history events personally read; exact current
    bytes preserved.
  snapshot_sha256: d6403ffb0f4d4c4d6bea614c6efdc77cd73c07f1807505f8a6ea732cb7356e85
- evidence_id: support-2197-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json
  locator: /records/6/owner_document; /records/6/owner_pin; /records/6/read_started_at;
    /records/6/read_finished_at
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Actual complete captured owner, source pin and original read clocks; component
    resolution is separate.
  snapshot_sha256: 90236bcdb9064859a691606fd163f92576040ab44a954a6323cc0b39871e571d
- evidence_id: support-2197-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/intakes/2197-inspect-001.json
  locator: /status; /source; /targets/0
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Original inspection-only intake, 62 current inputs, exact target and maintained
    ownership.
  snapshot_sha256: af59aa75171e0fe7a2a05e93fab191f0dcbddca593a08142df29efab0c113b75
- evidence_id: support-2197-intake-ready
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-intake-ready-001.json
  locator: /status; /records/6; /source_placements; /unique_source_paths; /external_requests
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: ROOT acceptance of the original ten intakes and exact 455/123 source maps.
  snapshot_sha256: 0d2b19cf4c0cd15f0c85c8325c71569238160f93ba1db1f2d0f347ca4b659b60
- evidence_id: support-2197-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Complete owner source plan: raw/history, all nine query frames, positive
    payloads, route sets, direct companions and input paths.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-source-plan-acceptance-001.json
  locator: /status; /plan; /source_notes; /actual_intake_ready; /verified
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: ROOT joins the earned source plan to the accepted inventory and actual
    intake maps.
  snapshot_sha256: 8a51c9303cf8dd7483b2fc282491f294f43ae3adc3a419819b31fe9531b98f6b
- evidence_id: support-2197-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-scope-notes-001.json
  locator: /reading; /cautions; /totals
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete-source-reading attribution and retained source cautions; no new
    primary verification is asserted.
  snapshot_sha256: aabfc3a0d18af5bd7d41acb95f1f89848cfbd06a962b174ef64b76218295ec7d
- evidence_id: support-2197-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Completed 142-literal-token scan over eight explicitly opened tables including
    ignored files: 101 physical lines/93 data rows, zero matches within that exact
    scope.'
  snapshot_sha256: aabfc3a0d18af5bd7d41acb95f1f89848cfbd06a962b174ef64b76218295ec7d
- evidence_id: support-2197-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/declared_structure; /records/6/literal_InChI_layers; /records/6/smiles;
    /records/6/inchi; /records/6/comparisons; /records/6/atom_correspondence
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete saved paired molecular computations, literal source stereo flag,
    exact comparisons and atom-map limits. No additional molecule was parsed.
  snapshot_sha256: 7bfd670e8944734f1da87a78ecd6d4cee7c6a8dd8bbb225b260809c176bb3de7
- evidence_id: support-2197-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed; /records/6/inchi/computed
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Both complete atom/bond/ring/stereo/motif tables personally read: 80 atoms
    and 88 bonds per form. Topology motifs are not natural-identity proof.'
  snapshot_sha256: 7bfd670e8944734f1da87a78ecd6d4cee7c6a8dd8bbb225b260809c176bb3de7
- evidence_id: support-2197-chemistry-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /stdout; /stderr; /output;
    /external_requests
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Original twenty-form diagnostic exited 0 with empty original stderr; no
    new parse, retry or owner-specific warning assignment.
  snapshot_sha256: 84a2689e8e405cf60782b070279cad53dbf96aadc5499ce50c17bd97650dd6ca
- evidence_id: support-2197-chemistry-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-chemistry-acceptance-001.json
  locator: /status; /data; /execution; /records/6; /scope
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: ROOT accepts the saved original diagnostic while preserving false comparisons
    and scientific limits.
  snapshot_sha256: c7b9547299a849c14093f64f88df2ec128f3806a864554cb39d89a2236dae984
- evidence_id: support-2197-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-native-gates-acceptance-001.json
  locator: /status; /ledger; /outcomes; /reading
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Five original local gates passed; full QC and ontology consistency/OAK
    remain unavailable. Selected queue rows are diagnostic leads.
  snapshot_sha256: 8ec4e48edaf25db9df0c202f6b8595e07cc7118c8fd24193c839e9c875f2c5c7
- evidence_id: support-2197-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165-172.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Maintained stereo_complete derives from unassigned atom-centered FindMolChiralCenters
    output; it is not universal geometric, axial or natural stereochemical completeness.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2197-source-ownership
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220/intakes/2197-inspect-001.json
  locator: /targets/0/owner_paths; /targets/0/ownership_note
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Generated fields belong to retained inventories/extractors/seeder; curated
    mechanism owner/components and their histories have separately stated validated-writer
    ownership.
  snapshot_sha256: af59aa75171e0fe7a2a05e93fab191f0dcbddca593a08142df29efab0c113b75
- evidence_id: support-2197-taxon-1886
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /cached_taxonomy/whole_stanzas/2
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete cached stanza for NCBITaxon:1886; literal labels/synonyms, not
    fresh taxonomy authority.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2197-taxon-1902
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /cached_taxonomy/whole_stanzas/3
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete cached stanza for NCBITaxon:1902; literal labels/synonyms, not
    fresh taxonomy authority.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2197-taxon-68264
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /cached_taxonomy/whole_stanzas/19
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete cached stanza for NCBITaxon:68264; literal labels/synonyms, not
    fresh taxonomy authority.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2197-taxon-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/source_taxa; /records/6/source_scope_inventory/forward_taxon_merge_matches;
    /records/6/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Exact saved taxon route sets; no forward merge/non-organism hit for this
    selected owner.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained mibig_compounds predicate/query and all 1 matches; empty
    results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical lines 906-906; exact complete TSV record SHA256 cb9e5d76e06fbd39c3ec56a879a3e390ee507c3d90eb5273e498a8774be30577.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"mibig_accession":"BGC0000833","entry_version":"4","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"coumermycin
    A1","compound_index":"1","smiles":"CC1=CC=C(N1)C(=O)O[C@H]2[C@H]([C@@H](OC([C@@H]2OC)(C)C)OC3=C(C4=C(C=C3)C(=C(C(=O)O4)NC(=O)C5=CNC(=C5C)C(=O)NC6=C(C7=C(C(=C(C=C7)O[C@H]8[C@@H]([C@@H]([C@H](C(O8)(C)C)OC)OC(=O)C9=CC=C(N9)C)O)C)OC6=O)O)O)C)O","standard_inchi":"InChI=1S/C55H59N5O20/c1-21-12-16-29(57-21)48(67)77-42-38(63)52(79-54(6,7)44(42)71-10)73-31-18-14-26-36(61)34(50(69)75-40(26)24(31)4)59-46(65)28-20-56-33(23(28)3)47(66)60-35-37(62)27-15-19-32(25(5)41(27)76-51(35)70)74-53-39(64)43(45(72-11)55(8,9)80-53)78-49(68)30-17-13-22(2)58-30/h12-20,38-39,42-45,52-53,56-58,61-64H,1-11H3,(H,59,65)(H,60,66)/t38-,39-,42+,43+,44-,45-,52-,53-/m1/s1","standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:54675768|pubchem:54720057","taxon_id":"NCBITaxon:68264","taxon_label":"Streptomyces
    rishiriensis","bgc_classes":"saccharide|other","bgc_subclasses":"hybrid/tailoring|aminocoumarin","genome_accession":"AF235050.4","locus_from":"2307","locus_to":"40140","locus_evidence_methods":"Knock-out
    studies|Enzymatic assays|Heterologous expression","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:14285468","reference_basis":"ENTRY"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2197-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained chebi_structures predicate/query and all 1 matches; empty
    results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-row-chebi_structures-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Physical lines 754-754; exact complete TSV record SHA256 cce8438bd10c6450ef7fd7c60c91c122514c891c5d6acf6d7bcb8b8b2057a25f.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"chebi_id":"CHEBI:3907","name":"coumermycin A1","definition":"A
    hydroxycoumarin antibiotic that is obtained from Streptomyces rishiriensis and
    exhibits potent antibacterial and anticancer activity.","stars":"3","standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","smiles":"CO[C@@H]1[C@@H](OC(=O)c2ccc(C)n2)[C@@H](O)[C@H](Oc2ccc3c(O)c(NC(=O)c4cnc(C(=O)Nc5c(O)c6ccc(O[C@@H]7OC(C)(C)[C@H](OC)[C@@H](OC(=O)c8ccc(C)n8)[C@H]7O)c(C)c6oc5=O)c4C)c(=O)oc3c2C)OC1(C)C"}'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: support-2197-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained lotus_occurrences predicate/query and all 21 matches;
    empty results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9377-9377; exact complete TSV record SHA256 442f427691834f8e450a81acd327a3c6bb8740931a1e0de3b0bad458bdc47b16.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1002/BIP.21493","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9378-9378; exact complete TSV record SHA256 c1b367ffd57b6b2a39af81fd5656415ebe04e410e0bb2c099cf87d59d57c5cd3.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1007/S10295-013-1348-5","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9379-9379; exact complete TSV record SHA256 21a1365b1ec5fc17087e3d1dc89fd2e59b9c46efd06784b9eb50bee37996d51f.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1046/J.1432-1033.2003.03830.X","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9380-9380; exact complete TSV record SHA256 06cad44e0d8e4ec04893dc340217baccfe7e2d42893ee340d222293dec2449c8.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1099/00221287-148-10-3317","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9381-9381; exact complete TSV record SHA256 9c977861666ab24e0211bd5f9ffa0436fc47a6c6724bc358e0c438fbf8d3c783.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1099/MIC.0.26867-0","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-5
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9382-9382; exact complete TSV record SHA256 627e1d3ba977f39b0f4a5cc79cd48d0b54579488914c94b7884db4316ffe0612.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1128/AAC.44.11.3040-3048.2000","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-6
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9383-9383; exact complete TSV record SHA256 7be8cd3949f566e40f6926bb723289d101eee102f502839bb23e3743e3eb9924.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    albidoflavus","taxon_id":"NCBITaxon:1886","organism_wikidata":"http://www.wikidata.org/entity/Q22286833","reference_doi":"10.1371/JOURNAL.PONE.0171056","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-7
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9384-9384; exact complete TSV record SHA256 b21728538de08b1ae2ef58bf2ab3319d1ef9bf74908ab86adefcff508a08e72e.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1002/BIP.21493","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-8
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9385-9385; exact complete TSV record SHA256 6002f578facf937b27160c9926bf3b3e5cc344ef83964752f641ce233bf7a190.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1007/S10295-013-1348-5","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-9
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9386-9386; exact complete TSV record SHA256 0baedbc8b8c3876e57ebf507ca843445df5731dbaf1556cec7e6000ce0b2551f.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1046/J.1432-1033.2003.03830.X","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-10
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9387-9387; exact complete TSV record SHA256 67c9b3a97b13b4199a1a876909b3ea710ac7fad49ab999f4eb33ddf84b720b45.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1099/00221287-148-10-3317","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-11
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9388-9388; exact complete TSV record SHA256 04e5972baa5a832f86e55f256278021e9086cd7ba1e763dcee7b77d5303cd1ed.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1099/MIC.0.26867-0","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-12
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9389-9389; exact complete TSV record SHA256 4406b3485ef19892f4260c225d1ef544abe51397b42b18eb2cddf7c1892b5d7e.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1128/AAC.44.11.3040-3048.2000","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-13
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9390-9390; exact complete TSV record SHA256 c21daf0e50b5303e4ce389443eb85c01231e99a754fe13396d79384d0ddad040.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    coelicolor","taxon_id":"NCBITaxon:1902","organism_wikidata":"http://www.wikidata.org/entity/Q2355919","reference_doi":"10.1371/JOURNAL.PONE.0171056","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-14
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9391-9391; exact complete TSV record SHA256 e1edad48b1bc55013da1e68f53d38169ea39d02f5ccf0cd826b16e7ab81734cb.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1002/BIP.21493","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-15
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9392-9392; exact complete TSV record SHA256 4f31128e419d0b71ab692f8b60b100a5979c611bfc6725aecf9f4f49d01271a0.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1007/S10295-013-1348-5","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-16
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9393-9393; exact complete TSV record SHA256 b7003d6d8320fe7351df8565d76f2b16893d72eead8e15151a4a46dcc7e0a748.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1046/J.1432-1033.2003.03830.X","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-17
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9394-9394; exact complete TSV record SHA256 43dc85bcedb1c67977fef9d6ef19c323d599834119f8e7850547b7b9ac0a7b40.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1099/00221287-148-10-3317","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-18
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9395-9395; exact complete TSV record SHA256 f7e91dd450e045cdc539acbd5fe37c165d3c1295445d3828e108944d861242d0.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1099/MIC.0.26867-0","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-19
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9396-9396; exact complete TSV record SHA256 cafd17f021d5e120314faad7564dffdd751caf820895ad2081874fdf0dbf0f84.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1128/AAC.44.11.3040-3048.2000","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-row-lotus_occurrences-20
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical lines 9397-9397; exact complete TSV record SHA256 16af19ed4cad9c553ed0c52e1cdc52cf5fdb8f1b37c6e855e552f9ea203a3dea.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","organism_name":"Streptomyces
    rishiriensis","taxon_id":"NCBITaxon:68264","organism_wikidata":"http://www.wikidata.org/entity/Q26292202","reference_doi":"10.1371/JOURNAL.PONE.0171056","structure_wikidata":"http://www.wikidata.org/entity/Q15408415"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2197-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained cyanometdb_occurrences predicate/query and all 0 matches;
    empty results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained npclassifier predicate/query and all 1 matches; empty
    results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical lines 2691-2691; exact complete TSV record SHA256 d22f3bf32145b570a21039a37325d7b58fbef18681d32b1875c05047e04068fd.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","smiles":"CC1=CC=C(N1)C(=O)O[C@H]2[C@H]([C@@H](OC([C@@H]2OC)(C)C)OC3=C(C4=C(C=C3)C(=C(C(=O)O4)NC(=O)C5=CNC(=C5C)C(=O)NC6=C(C7=C(C(=C(C=C7)O[C@H]8[C@@H]([C@@H]([C@H](C(O8)(C)C)OC)OC(=O)C9=CC=C(N9)C)O)C)OC6=O)O)O)C)O","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Coumarins","class_results":"Simple
    coumarins","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2197-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained pubchem_bioassay predicate/query and all 1 matches; empty
    results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-row-pubchem_bioassay-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical lines 8773-8773; exact complete TSV record SHA256 e6768903aef6e6d089c7eef672fa41e5385e2742be3002f1cf0f04518e65f7c3.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","cid":"54720057","aid":"","assay_name":"(no
    assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""}'
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2197-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained bindingdb_targets predicate/query and all 0 matches;
    empty results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained antibioticmech_inchikeys predicate/query and all 1 matches;
    empty results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-row-antibioticmech_inchikeys-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv
  locator: Physical lines 2491-2491; exact complete TSV record SHA256 8104484e41b9ee5bb858fe9a821ea49e3353aa0d14e62bbbe1af31fc04da98c7.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"WTIJXIZOODAMJT-DHFGXMAYSA-N","identifier":"CHEBI:3907","label":"coumermycin
    A1","antimicrobial_class":"ANTIBACTERIAL","slug":"coumermycin-a1","corpus_commit":"74f6cc8362498900f2fe2c13d0b6fdb66dd30976"}'
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
- evidence_id: support-2197-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained chebi_origins predicate/query and all 1 matches; empty
    results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2197-row-chebi_origins-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Physical lines 351-351; exact complete TSV record SHA256 035e8e79f07141761980b34c669191d3b447a02acfb60bc50f76043bb0fae715.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"chebi_id":"CHEBI:3907","species_text":"Streptomyces
    rishiriensis","species_accession":"68264","component_text":"","strain_text":"","source_accession":"24079980","comments":""}'
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: support-2197-component-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-native-identity-and-precursor-evidence.yaml
  locator: Complete component and history, lines 1-168.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Native CouO reference and precursor identity remain separate from engineered
    assay constructs and surrogate substrates.
  snapshot_sha256: f13039b270d6fc042ac03927b5055da74d7dc29fe8e2357a27cef0f3f8227f7c
- evidence_id: support-2197-component-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-constructs-and-soluble-protein-preparations.yaml
  locator: Complete component and history, lines 1-696.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: WT and ten mutant preparations retain literal construct/primer/protein
    claims; full plasmids and assay constructs were not freshly sequence-verified.
  snapshot_sha256: c0e04abf16d7ab6e64b1ce07e13a9497413502093d90576ade44a31f318a189e
- evidence_id: support-2197-component-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-lysate-normalization-and-mutant-endpoint-limits.yaml
  locator: Complete component and history, lines 1-575.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Cleared-lysate 24 h surrogate endpoints use normalized CouO content, not
    equal active enzyme. Variable soluble content, H120A solubility, relative triplicate
    ranges and near-background mutants do not establish kcat or numerical zero.
  snapshot_sha256: 1b3e54226e40adb0e88b7649b1f5d024a1f32434baeb436ce5a3a2ca9680b3fe
- evidence_id: support-2197-component-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-couo-sah-structure-dimer-and-model-limits.yaml
  locator: Complete component and history, lines 1-254.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 5M58 is an SAH-bound structure; SAM/coumarin docking and NovO analogy are
    models. Missing chain terminal density, Glu4/Glu6 conflict and condition-specific
    dimer evidence remain explicit.
  snapshot_sha256: c73eb5e39d86145b997a2da9d27dda6711db749981d81c2bdc80d30159ec2308
- evidence_id: support-2197-component-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-native-identities-and-annotation-limits.yaml
  locator: Complete component and history, lines 1-165.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: CouN1/7 native references are 95/281 aa; submitted hydrolase/lipase annotations
    are not measured native reaction specificity.
  snapshot_sha256: f9a7461ea3af618f627311d2d6b663162fb41a690301be3e7c15cb5d19dd6111
- evidence_id: support-2197-component-5
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-carrier-loading-and-terminal-transfer.yaml
  locator: Complete component and history, lines 1-224.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Sfp/synthetic acyl-CoA carrier loading and terminal transfer retain exact
    substrate/cofactor scope. Novobiocin surrogate use is not native mature-coumermycin
    reconstitution.
  snapshot_sha256: 300b8f85cf756435114a90f5358937e4cac0ffdeb4ea230436cabc39d61a5a18
- evidence_id: support-2197-component-6
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-reversible-shuttling-and-covalent-intermediate.yaml
  locator: Complete component and history, lines 1-188.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: S101A radiolabeled-acetyl trapping supports the reported covalent-intermediate
    experiment without establishing atomic structure, folding controls or all native
    transfer rates.
  snapshot_sha256: 50e4f0be584a3c74664fe468cf6b0a252af60dffec6871e52f1d53fb4a81f035
- evidence_id: support-2197-component-7
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun17-engineered-substrate-panel-and-supporting-material-limits.yaml
  locator: Complete component and history, lines 1-218.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: The 21-variant aggregate and 23-donor headings remain distinct; chemical
    synthesis SI is not a full enzyme-activity matrix and nomenclature conflicts are
    not silently resolved.
  snapshot_sha256: 845b497d571bccdb1d1305434c9c165f649091af14802692ea9d647de63fe3c0
- evidence_id: support-2197-component-8
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-native-identities-and-sequence-revisions.yaml
  locator: Complete component and history, lines 1-421.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: CouR2 old 377 aa versus revised 172/205 aa proteins and CouR6 old 290/current
    291 aa retain version and coordinate uncertainty; revisions are not proven assay-construct
    sequences.
  snapshot_sha256: 85ad3fce986966bcdf8522e75815e2a9e2cfeb39bf5e666cc0de71ba90e86c47
- evidence_id: support-2197-component-9
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-individual-deletion-constructs-and-pcr-limits.yaml
  locator: Complete component and history, lines 1-458.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Individual CouR deletions in heterologous M1146 retain PCR/genotype and
    polar-effect limits; historical restriction coordinates are not complete current
    allele sequences.
  snapshot_sha256: d75abb21881f1f5907b3969443a7b432f25831b11f894689b67942dd5b904ccb
- evidence_id: support-2197-component-10
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-genetic-titers-cpm-feeding-and-partial-rescue.yaml
  locator: Complete component and history, lines 1-372.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Reported intact 10.20 mg/L and deletion/CPM-feed titers are conditional
    endpoints. Censored less-than 0.01 values are not zero; chemical rescue is not
    genetic complementation; only stated R1/R4 genetic rescues carry.
  snapshot_sha256: 5492b6b7b32c41acec058a6de22da326625fb4e6286c0a379cb9882d8cc5ae2c
- evidence_id: support-2197-component-11
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-phosphothreonine-feeding-and-strain-label-conflict.yaml
  locator: Complete component and history, lines 1-149.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Phosphothreonine feeding retains 44 percent average increase and conflicting
    AK08/AK09 strain labels; this does not demonstrate the kinase reaction.
  snapshot_sha256: 02d9625f953fa9fe9b2d7dd43f648946fb9c59a0712a32f9fb543062996ff0fc
- evidence_id: support-2197-component-12
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-isotope-precursor-evidence-and-historical-pathway-model.yaml
  locator: Complete component and history, lines 1-265.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Threonine isotope incorporation supports four carbons plus nitrogen of
    the central pyrrole, while remaining carbon origin and historical pathway models
    remain unresolved.
  snapshot_sha256: 97cb886fbfb5a5c5f03bfdff643b33c9fa3048e874992ca59aa5b51e154ff292
- evidence_id: support-2197-component-13
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-minimal-expression-constructs-and-coordinate-limits.yaml
  locator: Complete component and history, lines 1-325.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Minimal heterologous constructs and coordinate/primer models do not constitute
    a purified full pathway or native essentiality experiment.
  snapshot_sha256: 3b0477348a58babe5ea904b31c96c94ed91aaa261c70c6ca1b6ab8b8f9df1d3e
- evidence_id: support-2197-component-14
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-heterologous-cpm-production-and-unit-limits.yaml
  locator: Complete component and history, lines 1-223.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Heterologous CPM production retains the indexed mg/mL unit conflict and
    strain/context limits; no silent unit conversion or mature-antibiotic yield inference.
  snapshot_sha256: ff89076526e22bcd73e47f38f077c3762c667fa423116c60f724027656b7562e
- evidence_id: support-2197-component-15
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-cour-cour3-preparation-atpase-and-unconfirmed-kinase.yaml
  locator: Complete component and history, lines 1-228.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: His8 CouR3 ATPase activity and no observed threonine dependence are not
    threonine phosphorylation or proof that no substrate can exist.
  snapshot_sha256: 76bd74ba4b3a42390cd419c137b9cf7aef8d1ef352f0cae7913657c2c22146b7
- evidence_id: support-2197-component-16
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-native-identities-and-version-conflicts.yaml
  locator: Complete component and history, lines 1-319.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: CouN2–6 native accessions/version changes and the historical CouN3/CloN3
    accession error remain separated; old/new protein lengths are not natural polymorphism
    proof.
  snapshot_sha256: fdbef28a3f445efa3b3555c0d25d3e83420af65ff2ff21e5aa19cc2b46203129
- evidence_id: support-2197-component-17
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-coun3-deletion-and-historical-allele-limits.yaml
  locator: Complete component and history, lines 1-178.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Native CouN3 historical 480 bp deletion/restriction model and Southern
    controls retain allele-version limits; current protein length is not substituted
    into the old construct.
  snapshot_sha256: 74f7ccce61cf77409be077d68b23526707dc3552ebeb71e28f2d7276bcadcada
- evidence_id: support-2197-component-18
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-coun4-insertion-and-source-conflicts.yaml
  locator: Complete component and history, lines 1-174.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: CouN4 aphII insertion retains couN3 naming and 870 bp/1350 bp probe conflicts;
    genotype uncertainty is preserved rather than repaired by prose.
  snapshot_sha256: 53a911bcec5316c802c019d51c619e80367dacf30a92af9396608a20d8004957
- evidence_id: support-2197-component-19
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-native-genetic-phenotypes-and-product-boundaries.yaml
  locator: Complete component and history, lines 1-284.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Native mutant losses are bounded detection results; CoumerD activity values
    and N4 HPLC versus N3 LCMS evidence do not establish improved coumermycin A1 yield
    or equal analytical coverage.
  snapshot_sha256: a80e4f86bf97d1282bee63ef3c9865075a05ba395b6420a6b6d5a3e9c5e0e151
- evidence_id: support-2197-component-20
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coun23456-proline-loading-and-oxidation-assay-boundaries.yaml
  locator: Complete component and history, lines 1-214.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: CouN4 prolyl-AMP/loading evidence remains distinct from rapid-quench oxidation
    attributed to CloN3 rather than CouN3; congener enzymes are not merged.
  snapshot_sha256: 1d0ab86d450ed025fc32e9f45e39dbc2710283ca6228d61b41146347948fc9e9
- evidence_id: support-2197-component-21
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coump-native-references-and-bounded-tandem-reactions.yaml
  locator: Complete component and history, lines 1-307.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: CouM 402 aa/CouP 276 aa native references and staged tandem reactions remain
    bounded. Added NovN is a novobiocin enzyme and an engineered biscarbamoylated
    analogue is not mature terminal-pyrrole A1.
  snapshot_sha256: c4794c900fa7f9f618d8d55107b882a9c03e96aff010f3167fd3900606c544cc
- evidence_id: support-2197-component-22
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/causal_graphs/WTIJXIZOODAMJT-DHFGXMAYSA-N/coumermycin-a1-coump-coup-deletion-and-demethyl-product-boundaries.yaml
  locator: Complete component and history, lines 1-148.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: CouP-deletion demethyl-product abundance compares different molecules,
    not increased A1 yield; abstract-level observations do not add missing calibration
    or replication.
  snapshot_sha256: 3393544c720602178971fbca625864d0c000b59c4b6fe81e0643ed8d4028bb57
- evidence_id: support-2197-reader-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/native-current220-coumermycin-a1-maintained-reader-DATA-001.json
  locator: /status; /reader_call_count; /review_check_metadata; /raw_owner; /component_captures;
    /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner;
    /counts; /denials; /unexpected_denials; /errors; /limitations
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'One accepted maintained call preserved the complete owner and ordered
    23 appends: 24 graphs, 335 nodes, 407 edges; all raw/history fields carry. Known
    socket capability probe denied before action; no request or fresh scientific authority.'
  snapshot_sha256: 17fe7c1937be11737eb598da87e48c41654b29219d7951533b844344cb99b532
- evidence_id: support-2197-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/native-current220-coumermycin-a1-reader-execution-001.json
  locator: /command; /source; /configuration; /started_at; /finished_at; /exit_code;
    /original_tool; /stdout; /stderr; /DATA; /external_requests
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Original Coumermycin reader process exited 0 with empty stderr and preserved
    original tool/process/streams; no replay.
  snapshot_sha256: 7fad1d7d156e06c09ada498d9df9a4efb0a7f39611ad8d1902ad082e3251c5ba
- evidence_id: support-2197-reader-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-current220-coumermycin-a1-reader-acceptance-001.json
  locator: /status; /order; /DATA; /execution; /verification; /review_check_contract;
    /scientific_scope
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: ROOT accepts complete-owner equality, exact positive content and original
    0; 590 graph references remain historical source annotations.
  snapshot_sha256: a7c34283eb2255a358cd991ae683d9e471c2df82f83502ae76b47a2d12070b2d
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:05:35.934949Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 3eb7a41f227bc3766da4ddb5affcab339127e3eec377a38a928d989861e7bca3
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:06:00.493115Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: b0fee61c050e78f367a4ad7e88aa28c2e04159e5fc41cb9fdd8c3cc0c524bbf8
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:06:19.575968Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:06:54.142706Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:07:06.355777Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 6b8a6b8cb74ddc70b591fb67b612031f05b241b0a0c649cdb0317a6bdeabfb46
assessments:
- assessment_id: support-2197-A1
  area: identity
  topic: Exact structure concept and grounding scope
  outcome: supported
  summary: Coumermycin A1 retains CHEBI:3907 and full key WTIJXIZOODAMJT-DHFGXMAYSA-N
    across the exact-key MIBiG, ChEBI and AntibioticMech rows, with neutral C55H59N5O20
    in both saved owner-form calculations. BGC0000833 version 4 names this compound
    at index 1. ChEBI's hydroxycoumarin, antibacterial and anticancer definition is
    an attributed database assertion, not a newly measured potency result. The retained
    ChEBI SMILES has aromatic n spellings differing from the owner representation;
    that third string was not reparsed, and source-key agreement is not proof of equivalence
    of every source drawing or natural sample.
  target_ids:
  - CHEBI:3907
  evidence_ids:
  - support-2197-owner
  - support-2197-capture
  - support-2197-intake
  - support-2197-source-plan
  - support-2197-plan-acceptance
  - support-2197-chemistry
  - support-2197-query-mibig_compounds
  - support-2197-row-mibig_compounds-0
  - support-2197-query-chebi_structures
  - support-2197-row-chebi_structures-0
  dimensions:
  - name: standard_inchi_key
    value: WTIJXIZOODAMJT-DHFGXMAYSA-N
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-capture
    - support-2197-intake
    - support-2197-source-plan
    - support-2197-plan-acceptance
    - support-2197-chemistry
    - support-2197-query-mibig_compounds
    - support-2197-row-mibig_compounds-0
    - support-2197-query-chebi_structures
    - support-2197-row-chebi_structures-0
  - name: grounding_scope
    value: CHEBI3907 exact-key source join;third ChEBI string not reparsed
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-capture
    - support-2197-intake
    - support-2197-source-plan
    - support-2197-plan-acceptance
    - support-2197-chemistry
    - support-2197-query-mibig_compounds
    - support-2197-row-mibig_compounds-0
    - support-2197-query-chebi_structures
    - support-2197-row-chebi_structures-0
- assessment_id: support-2197-A2
  area: representation
  topic: Paired molecular representations and stereochemical limits
  outcome: supported
  summary: Both owner forms parse with equal standardized InChI/full key, formula,
    charge and 80-atom/88-bond counts, but both canonical SMILES equality flags are
    false and the chirality-aware atom correspondence is empty. Saved SMILES contains
    C32(=O33)–N31 and C40(=O41)–N42 amides; the InChI-derived form contains C45(OH64)=N58
    and C46(OH65)=N59. This supports a bounded amide/imidic-acid representation interpretation
    without proving full graph equivalence, natural tautomer population or a wrong
    identity. Eight specified tetrahedral centers persist in both forms; two unspecified
    double-bond entries appear only at the InChI-derived C=N bonds. The maintained
    atom-centered stereo_complete derivation is narrower than universal geometric
    or natural stereochemical completeness.
  target_ids:
  - CHEBI:3907
  evidence_ids:
  - support-2197-owner
  - support-2197-chemistry
  - support-2197-topology
  - support-2197-stereo-method
  - support-2197-chemistry-execution
  - support-2197-chemistry-acceptance
  dimensions:
  - name: stereochemical_resolution
    value: 8 specified tetra each;2 unspecified C=N only InChI;literal flag true
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-chemistry
    - support-2197-topology
    - support-2197-stereo-method
    - support-2197-chemistry-execution
    - support-2197-chemistry-acceptance
  - name: representation_correspondence
    value: Both canonical comparisons false;empty map;equal standardized key
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-chemistry
    - support-2197-topology
    - support-2197-stereo-method
    - support-2197-chemistry-execution
    - support-2197-chemistry-acceptance
- assessment_id: support-2197-A3
  area: provenance
  topic: Producer, occurrence and locus evidence grades
  outcome: supported
  summary: MIBiG assigns Streptomyces rishiriensis NCBITaxon:68264 a BGC_CHARACTERIZED
    producer grade and BGC0000833 a CLUSTER_DEMONSTRATED link, retaining knockout,
    enzymatic and heterologous-expression methods. AF235050.4 coordinates 2307–40140
    are the deposited locus scope. The 21 LOTUS rows represent three taxa—1886 S.
    albidoflavus, 1902 S. coelicolor and 68264 S. rishiriensis—crossed with seven
    citations; they are occurrence assertions, not 21 independent producer experiments.
    The additional ChEBI-origin row also names S. rishiriensis. Cached names and historical
    host labels do not transfer native production to a recombinant host.
  target_ids:
  - CHEBI:3907
  evidence_ids:
  - support-2197-owner
  - support-2197-capture
  - support-2197-taxon-routes
  - support-2197-query-mibig_compounds
  - support-2197-row-mibig_compounds-0
  - support-2197-query-lotus_occurrences
  - support-2197-row-lotus_occurrences-0
  - support-2197-row-lotus_occurrences-1
  - support-2197-row-lotus_occurrences-2
  - support-2197-row-lotus_occurrences-3
  - support-2197-row-lotus_occurrences-4
  - support-2197-row-lotus_occurrences-5
  - support-2197-row-lotus_occurrences-6
  - support-2197-row-lotus_occurrences-7
  - support-2197-row-lotus_occurrences-8
  - support-2197-row-lotus_occurrences-9
  - support-2197-row-lotus_occurrences-10
  - support-2197-row-lotus_occurrences-11
  - support-2197-row-lotus_occurrences-12
  - support-2197-row-lotus_occurrences-13
  - support-2197-row-lotus_occurrences-14
  - support-2197-row-lotus_occurrences-15
  - support-2197-row-lotus_occurrences-16
  - support-2197-row-lotus_occurrences-17
  - support-2197-row-lotus_occurrences-18
  - support-2197-row-lotus_occurrences-19
  - support-2197-row-lotus_occurrences-20
  - support-2197-query-chebi_origins
  - support-2197-row-chebi_origins-0
  - support-2197-taxon-1886
  - support-2197-taxon-1902
  - support-2197-taxon-68264
  dimensions:
  - name: taxon_and_strain_scope
    value: S.rishiriensis68264 producer;1886/1902/68264 occurrences
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-capture
    - support-2197-taxon-routes
    - support-2197-query-mibig_compounds
    - support-2197-row-mibig_compounds-0
    - support-2197-query-lotus_occurrences
    - support-2197-row-lotus_occurrences-0
    - support-2197-row-lotus_occurrences-1
    - support-2197-row-lotus_occurrences-2
    - support-2197-row-lotus_occurrences-3
    - support-2197-row-lotus_occurrences-4
    - support-2197-row-lotus_occurrences-5
    - support-2197-row-lotus_occurrences-6
    - support-2197-row-lotus_occurrences-7
    - support-2197-row-lotus_occurrences-8
    - support-2197-row-lotus_occurrences-9
    - support-2197-row-lotus_occurrences-10
    - support-2197-row-lotus_occurrences-11
    - support-2197-row-lotus_occurrences-12
    - support-2197-row-lotus_occurrences-13
    - support-2197-row-lotus_occurrences-14
    - support-2197-row-lotus_occurrences-15
    - support-2197-row-lotus_occurrences-16
    - support-2197-row-lotus_occurrences-17
    - support-2197-row-lotus_occurrences-18
    - support-2197-row-lotus_occurrences-19
    - support-2197-row-lotus_occurrences-20
    - support-2197-query-chebi_origins
    - support-2197-row-chebi_origins-0
    - support-2197-taxon-1886
    - support-2197-taxon-1902
    - support-2197-taxon-68264
  - name: producer_evidence_tier
    value: BGC_CHARACTERIZED, MIBiG833v4
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-capture
    - support-2197-taxon-routes
    - support-2197-query-mibig_compounds
    - support-2197-row-mibig_compounds-0
    - support-2197-query-lotus_occurrences
    - support-2197-row-lotus_occurrences-0
    - support-2197-row-lotus_occurrences-1
    - support-2197-row-lotus_occurrences-2
    - support-2197-row-lotus_occurrences-3
    - support-2197-row-lotus_occurrences-4
    - support-2197-row-lotus_occurrences-5
    - support-2197-row-lotus_occurrences-6
    - support-2197-row-lotus_occurrences-7
    - support-2197-row-lotus_occurrences-8
    - support-2197-row-lotus_occurrences-9
    - support-2197-row-lotus_occurrences-10
    - support-2197-row-lotus_occurrences-11
    - support-2197-row-lotus_occurrences-12
    - support-2197-row-lotus_occurrences-13
    - support-2197-row-lotus_occurrences-14
    - support-2197-row-lotus_occurrences-15
    - support-2197-row-lotus_occurrences-16
    - support-2197-row-lotus_occurrences-17
    - support-2197-row-lotus_occurrences-18
    - support-2197-row-lotus_occurrences-19
    - support-2197-row-lotus_occurrences-20
    - support-2197-query-chebi_origins
    - support-2197-row-chebi_origins-0
    - support-2197-taxon-1886
    - support-2197-taxon-1902
    - support-2197-taxon-68264
  - name: locus_evidence_tier
    value: CLUSTER_DEMONSTRATED;knockout/enzymatic/heterologous
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-capture
    - support-2197-taxon-routes
    - support-2197-query-mibig_compounds
    - support-2197-row-mibig_compounds-0
    - support-2197-query-lotus_occurrences
    - support-2197-row-lotus_occurrences-0
    - support-2197-row-lotus_occurrences-1
    - support-2197-row-lotus_occurrences-2
    - support-2197-row-lotus_occurrences-3
    - support-2197-row-lotus_occurrences-4
    - support-2197-row-lotus_occurrences-5
    - support-2197-row-lotus_occurrences-6
    - support-2197-row-lotus_occurrences-7
    - support-2197-row-lotus_occurrences-8
    - support-2197-row-lotus_occurrences-9
    - support-2197-row-lotus_occurrences-10
    - support-2197-row-lotus_occurrences-11
    - support-2197-row-lotus_occurrences-12
    - support-2197-row-lotus_occurrences-13
    - support-2197-row-lotus_occurrences-14
    - support-2197-row-lotus_occurrences-15
    - support-2197-row-lotus_occurrences-16
    - support-2197-row-lotus_occurrences-17
    - support-2197-row-lotus_occurrences-18
    - support-2197-row-lotus_occurrences-19
    - support-2197-row-lotus_occurrences-20
    - support-2197-query-chebi_origins
    - support-2197-row-chebi_origins-0
    - support-2197-taxon-1886
    - support-2197-taxon-1902
    - support-2197-taxon-68264
- assessment_id: support-2197-A4
  area: evidence
  topic: Citation placement and historical verification scope
  outcome: supported
  summary: PMID:14285468 is the MIBiG ENTRY-level citation; PMID:24079980 is the ChEBI-origin
    citation; the seven retained LOTUS DOI strings retain their individual occurrence
    placements. Publication independence across those claims has not been established.
    The whole inline graph, 23 components and their histories preserve primary-experiment
    labels, quotations, source conflicts and prior inspection annotations, but no
    original article, API response or protein sequence was newly inspected in this
    review. Their historical annotations are not promoted to fresh external verification.
  target_ids:
  - CHEBI:3907
  evidence_ids:
  - support-2197-owner
  - support-2197-capture
  - support-2197-taxon-routes
  - support-2197-query-mibig_compounds
  - support-2197-row-mibig_compounds-0
  - support-2197-query-lotus_occurrences
  - support-2197-row-lotus_occurrences-0
  - support-2197-row-lotus_occurrences-1
  - support-2197-row-lotus_occurrences-2
  - support-2197-row-lotus_occurrences-3
  - support-2197-row-lotus_occurrences-4
  - support-2197-row-lotus_occurrences-5
  - support-2197-row-lotus_occurrences-6
  - support-2197-row-lotus_occurrences-7
  - support-2197-row-lotus_occurrences-8
  - support-2197-row-lotus_occurrences-9
  - support-2197-row-lotus_occurrences-10
  - support-2197-row-lotus_occurrences-11
  - support-2197-row-lotus_occurrences-12
  - support-2197-row-lotus_occurrences-13
  - support-2197-row-lotus_occurrences-14
  - support-2197-row-lotus_occurrences-15
  - support-2197-row-lotus_occurrences-16
  - support-2197-row-lotus_occurrences-17
  - support-2197-row-lotus_occurrences-18
  - support-2197-row-lotus_occurrences-19
  - support-2197-row-lotus_occurrences-20
  - support-2197-query-chebi_origins
  - support-2197-row-chebi_origins-0
  - support-2197-taxon-1886
  - support-2197-taxon-1902
  - support-2197-taxon-68264
  - support-2197-source-notes
  - support-2197-reader-data
  - support-2197-reader-execution
  - support-2197-reader-acceptance
  - support-2197-component-0
  - support-2197-component-1
  - support-2197-component-2
  - support-2197-component-3
  - support-2197-component-4
  - support-2197-component-5
  - support-2197-component-6
  - support-2197-component-7
  - support-2197-component-8
  - support-2197-component-9
  - support-2197-component-10
  - support-2197-component-11
  - support-2197-component-12
  - support-2197-component-13
  - support-2197-component-14
  - support-2197-component-15
  - support-2197-component-16
  - support-2197-component-17
  - support-2197-component-18
  - support-2197-component-19
  - support-2197-component-20
  - support-2197-component-21
  - support-2197-component-22
  dimensions:
  - name: citation_scope
    value: ENTRY14285468;LOTUS DOIs;ChEBI-origin24079980;historical graph citations
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-capture
    - support-2197-taxon-routes
    - support-2197-query-mibig_compounds
    - support-2197-row-mibig_compounds-0
    - support-2197-query-lotus_occurrences
    - support-2197-row-lotus_occurrences-0
    - support-2197-row-lotus_occurrences-1
    - support-2197-row-lotus_occurrences-2
    - support-2197-row-lotus_occurrences-3
    - support-2197-row-lotus_occurrences-4
    - support-2197-row-lotus_occurrences-5
    - support-2197-row-lotus_occurrences-6
    - support-2197-row-lotus_occurrences-7
    - support-2197-row-lotus_occurrences-8
    - support-2197-row-lotus_occurrences-9
    - support-2197-row-lotus_occurrences-10
    - support-2197-row-lotus_occurrences-11
    - support-2197-row-lotus_occurrences-12
    - support-2197-row-lotus_occurrences-13
    - support-2197-row-lotus_occurrences-14
    - support-2197-row-lotus_occurrences-15
    - support-2197-row-lotus_occurrences-16
    - support-2197-row-lotus_occurrences-17
    - support-2197-row-lotus_occurrences-18
    - support-2197-row-lotus_occurrences-19
    - support-2197-row-lotus_occurrences-20
    - support-2197-query-chebi_origins
    - support-2197-row-chebi_origins-0
    - support-2197-taxon-1886
    - support-2197-taxon-1902
    - support-2197-taxon-68264
    - support-2197-source-notes
- assessment_id: support-2197-A5
  area: scope
  topic: Occurrence, assay and companion boundaries
  outcome: supported
  summary: The exact-key AntibioticMech row supports the coarse ANTIBACTERIAL summary
    and SAME_STRUCTURE link at pinned sibling commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976;
    it supplies no new molecular target or quantitative assay. The PubChem row for
    CID 54720057 has blank AID and assay fields, so it is an empty-assay sentinel,
    not an inactive result. The owner has no written bioactivity observations or molecular
    targets. ChEBI's anticancer wording and the enzyme-component substrate assays
    remain separate evidence scopes; neither becomes a compound dose-response or a
    clinical claim. The 22 written occurrence assertions remain distinct from production.
  target_ids:
  - CHEBI:3907
  evidence_ids:
  - support-2197-owner
  - support-2197-curation-scope
  - support-2197-query-lotus_occurrences
  - support-2197-row-lotus_occurrences-0
  - support-2197-row-lotus_occurrences-1
  - support-2197-row-lotus_occurrences-2
  - support-2197-row-lotus_occurrences-3
  - support-2197-row-lotus_occurrences-4
  - support-2197-row-lotus_occurrences-5
  - support-2197-row-lotus_occurrences-6
  - support-2197-row-lotus_occurrences-7
  - support-2197-row-lotus_occurrences-8
  - support-2197-row-lotus_occurrences-9
  - support-2197-row-lotus_occurrences-10
  - support-2197-row-lotus_occurrences-11
  - support-2197-row-lotus_occurrences-12
  - support-2197-row-lotus_occurrences-13
  - support-2197-row-lotus_occurrences-14
  - support-2197-row-lotus_occurrences-15
  - support-2197-row-lotus_occurrences-16
  - support-2197-row-lotus_occurrences-17
  - support-2197-row-lotus_occurrences-18
  - support-2197-row-lotus_occurrences-19
  - support-2197-row-lotus_occurrences-20
  - support-2197-query-pubchem_bioassay
  - support-2197-row-pubchem_bioassay-0
  - support-2197-query-bindingdb_targets
  - support-2197-query-antibioticmech_inchikeys
  - support-2197-row-antibioticmech_inchikeys-0
  - support-2197-query-chebi_structures
  - support-2197-row-chebi_structures-0
  dimensions:
  - name: occurrence_scope
    value: 21 LOTUS triples plus1 ChEBI origin;independence unverified
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-curation-scope
    - support-2197-query-lotus_occurrences
    - support-2197-row-lotus_occurrences-0
    - support-2197-row-lotus_occurrences-1
    - support-2197-row-lotus_occurrences-2
    - support-2197-row-lotus_occurrences-3
    - support-2197-row-lotus_occurrences-4
    - support-2197-row-lotus_occurrences-5
    - support-2197-row-lotus_occurrences-6
    - support-2197-row-lotus_occurrences-7
    - support-2197-row-lotus_occurrences-8
    - support-2197-row-lotus_occurrences-9
    - support-2197-row-lotus_occurrences-10
    - support-2197-row-lotus_occurrences-11
    - support-2197-row-lotus_occurrences-12
    - support-2197-row-lotus_occurrences-13
    - support-2197-row-lotus_occurrences-14
    - support-2197-row-lotus_occurrences-15
    - support-2197-row-lotus_occurrences-16
    - support-2197-row-lotus_occurrences-17
    - support-2197-row-lotus_occurrences-18
    - support-2197-row-lotus_occurrences-19
    - support-2197-row-lotus_occurrences-20
    - support-2197-query-pubchem_bioassay
    - support-2197-row-pubchem_bioassay-0
    - support-2197-query-bindingdb_targets
    - support-2197-query-antibioticmech_inchikeys
    - support-2197-row-antibioticmech_inchikeys-0
    - support-2197-query-chebi_structures
    - support-2197-row-chebi_structures-0
  - name: assay_scope
    value: Blank AID sentinel;coarse sibling ANTIBACTERIAL;no new potency/target
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-curation-scope
    - support-2197-query-lotus_occurrences
    - support-2197-row-lotus_occurrences-0
    - support-2197-row-lotus_occurrences-1
    - support-2197-row-lotus_occurrences-2
    - support-2197-row-lotus_occurrences-3
    - support-2197-row-lotus_occurrences-4
    - support-2197-row-lotus_occurrences-5
    - support-2197-row-lotus_occurrences-6
    - support-2197-row-lotus_occurrences-7
    - support-2197-row-lotus_occurrences-8
    - support-2197-row-lotus_occurrences-9
    - support-2197-row-lotus_occurrences-10
    - support-2197-row-lotus_occurrences-11
    - support-2197-row-lotus_occurrences-12
    - support-2197-row-lotus_occurrences-13
    - support-2197-row-lotus_occurrences-14
    - support-2197-row-lotus_occurrences-15
    - support-2197-row-lotus_occurrences-16
    - support-2197-row-lotus_occurrences-17
    - support-2197-row-lotus_occurrences-18
    - support-2197-row-lotus_occurrences-19
    - support-2197-row-lotus_occurrences-20
    - support-2197-query-pubchem_bioassay
    - support-2197-row-pubchem_bioassay-0
    - support-2197-query-bindingdb_targets
    - support-2197-query-antibioticmech_inchikeys
    - support-2197-row-antibioticmech_inchikeys-0
    - support-2197-query-chebi_structures
    - support-2197-row-chebi_structures-0
- assessment_id: support-2197-A6
  area: other
  topic: Computed classification and full-table topology limits
  outcome: supported
  summary: The pinned NPClassifier model reports Coumarins, Simple coumarins and is_glycoside
    true; MIBiG SACCHARIDE/OTHER and aminocoumarin annotations remain source cluster
    descriptions. Both saved molecular forms contain two saturated C5O candidate rings,
    two terminal methylpyrrole ester linkages, two aromaticized coumarin systems and
    a central substituted pyrrole. SMILES ester sites C6(=O7)–O8–C9 and C63(=O64)–O62–C54
    are distinct from the aromatic ring oxygens that the generic SINGLE-bond ester
    scan omits. Two amide sites disappear from that motif class in the imidic representation.
    These topological observations do not independently assign biochemical sugar positions,
    natural configuration, reaction order or in-vivo mechanism.
  target_ids:
  - CHEBI:3907
  evidence_ids:
  - support-2197-owner
  - support-2197-topology
  - support-2197-chemistry
  - support-2197-query-npclassifier
  - support-2197-row-npclassifier-0
  - support-2197-query-mibig_compounds
  - support-2197-row-mibig_compounds-0
  dimensions:
  - name: computed_classification
    value: Pinned Coumarins/Simple coumarins/glycoside;two candidate C5O rings
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-topology
    - support-2197-chemistry
    - support-2197-query-npclassifier
    - support-2197-row-npclassifier-0
    - support-2197-query-mibig_compounds
    - support-2197-row-mibig_compounds-0
- assessment_id: support-2197-A7
  area: completeness
  topic: Partial scientific completion and maintained ownership
  outcome: supported
  summary: 'The complete owner with 13 history events and all 23 components with 30
    component-history events were personally read. The accepted original maintained
    reader preserves the entire owner and appends those 23 graphs exactly once: 24
    graphs, 335 nodes, 407 edges and 590 graph-reference placements; no pathway steps
    or molecular targets are added. This is structural preservation and maintained
    resolution, not independent verification of the historical biochemical claims.
    Original local gates passed, while full QC, ontology authority coverage and external
    source verification remain unavailable. The review stays partial and does not
    alter native status, scientific records or curation histories.'
  target_ids:
  - CHEBI:3907
  evidence_ids:
  - support-2197-owner
  - support-2197-intake
  - support-2197-intake-ready
  - support-2197-native-acceptance
  - support-2197-source-ownership
  - support-2197-source-notes
  - support-2197-reader-data
  - support-2197-reader-execution
  - support-2197-reader-acceptance
  - support-2197-component-0
  - support-2197-component-1
  - support-2197-component-2
  - support-2197-component-3
  - support-2197-component-4
  - support-2197-component-5
  - support-2197-component-6
  - support-2197-component-7
  - support-2197-component-8
  - support-2197-component-9
  - support-2197-component-10
  - support-2197-component-11
  - support-2197-component-12
  - support-2197-component-13
  - support-2197-component-14
  - support-2197-component-15
  - support-2197-component-16
  - support-2197-component-17
  - support-2197-component-18
  - support-2197-component-19
  - support-2197-component-20
  - support-2197-component-21
  - support-2197-component-22
  dimensions:
  - name: review_completion
    value: partial;accepted maintained view;QC/OAK/primary verification unavailable
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2197-owner
    - support-2197-intake
    - support-2197-intake-ready
    - support-2197-native-acceptance
    - support-2197-source-ownership
    - support-2197-source-notes
    - support-2197-reader-acceptance
- assessment_id: support-2197-A8
  area: graph
  topic: Complete maintained mechanism and biochemical experiment boundaries
  outcome: supported
  target_ids:
  - CHEBI:3907
  evidence_ids:
  - support-2197-owner
  - support-2197-capture
  - support-2197-reader-data
  - support-2197-reader-execution
  - support-2197-reader-acceptance
  - support-2197-component-0
  - support-2197-component-1
  - support-2197-component-2
  - support-2197-component-3
  - support-2197-component-4
  - support-2197-component-5
  - support-2197-component-6
  - support-2197-component-7
  - support-2197-component-8
  - support-2197-component-9
  - support-2197-component-10
  - support-2197-component-11
  - support-2197-component-12
  - support-2197-component-13
  - support-2197-component-14
  - support-2197-component-15
  - support-2197-component-16
  - support-2197-component-17
  - support-2197-component-18
  - support-2197-component-19
  - support-2197-component-20
  - support-2197-component-21
  - support-2197-component-22
  summary: The accepted maintained view preserves the inline CouL graph and all 23
    ordered components. CouL's unglycosylated monoamide/diamide experiments retain
    unresolved monoamide position, substrate scope, ATP/enzyme-loading source conflicts,
    conditional apparent Km/Vmax and censored relative endpoints; they do not reconstruct
    mature A1 or establish native flux. CouO lysate endpoints and SAH/docking models,
    CouN1/N7 carrier-shuttling experiments, CouR heterologous genetics/isotope/ATPase
    evidence, CouN2–6 native mutants and CouM/P tandem reactions remain distinct.
    Genetic complementation is not chemical rescue; small product peaks or bounded
    nondetection are not numerical zero. Surrogate compounds, congener enzymes, engineered
    analogues and heterologous hosts are not silently replaced with the native complete
    pathway. Conflicts are retained explicitly in the corresponding components rather
    than resolved by the successful reader.
- assessment_id: support-2197-A9
  area: grounding
  topic: Native references, engineered constructs and protein-claim limits
  outcome: supported
  target_ids:
  - CHEBI:3907
  evidence_ids:
  - support-2197-owner
  - support-2197-capture
  - support-2197-reader-data
  - support-2197-reader-execution
  - support-2197-reader-acceptance
  - support-2197-component-0
  - support-2197-component-1
  - support-2197-component-2
  - support-2197-component-3
  - support-2197-component-4
  - support-2197-component-5
  - support-2197-component-6
  - support-2197-component-7
  - support-2197-component-8
  - support-2197-component-9
  - support-2197-component-10
  - support-2197-component-11
  - support-2197-component-12
  - support-2197-component-13
  - support-2197-component-14
  - support-2197-component-15
  - support-2197-component-16
  - support-2197-component-17
  - support-2197-component-18
  - support-2197-component-19
  - support-2197-component-20
  - support-2197-component-21
  - support-2197-component-22
  summary: Native protein references are kept separate from tagged/engineered preparations
    and historical versioned constructs. CouL Q9F8U8/AAG29784.2/AF235050.4 is a 529
    aa reference, not proof of the exact His6 assay construct; historical 384–385
    RA versus current EG and unverified full plasmid sequence remain scoped. CouO's
    native 230 aa reference does not establish equal active fractions in its lysate
    mutant panel. CouR2/CouR6 and CouN2–6 sequence revisions, the CouN3/CloN3 accession
    conflict, CouN4 allele/probe conflicts and native versus congener oxidation assays
    remain explicit. CouM 402 aa/CouP 276 aa references and an added novobiocin NovN
    experiment do not establish native coumermycin terminal tailoring. No primary
    article/API response or protein sequence was newly inspected here; UniProt/GenBank/PDB
    names, sequence strings and historical inspection notes remain retained source
    claims, not fresh grounding verification.
findings: []
actions: []
limitations:
- Full QC and complete ontology authority coverage/OAK were unavailable; passing local
  gates do not establish scientific completeness.
- No external requests, primary-article retrieval or live taxonomy/identifier/protein
  queries were performed. These assessments use the original saved owner-form computations,
  with no additional molecular parses during fragment authoring.
- Source citations, database labels, model predictions and historical annotations
  retain their stated evidence types; no publication independence or natural-identity
  proof is inferred from matching keys.
- No source record, component or curation history was edited by this review. Canonical
  review persistence and campaign publication are separate ROOT-owned operations.
- The original reader resolves/preserves complete content; it does not verify historical
  primary claims, protein sequences, constructs, natural mechanism or stereochemistry.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Raw/source/cache/curation and molecular reading attribution is preserved in the
  fragment metadata and source-scope notes.
- No finding in this bounded review closes an existing issue or proves absence of
  uncertainty outside the inspected scope.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-220
```
