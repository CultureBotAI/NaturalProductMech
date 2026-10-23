# HHQ: exact tautomer, bounded PAO1 mechanism and occurrence provenance

- Review: 20261021T075346Z-2-heptylquinolin-4-1h-one
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T07:42:18.621186Z
- Finished UTC: 2026-10-21T07:53:46.213792Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact HHQ identity and five native PAO1 references are supported; both mechanism graphs preserve their evidence and construct limits. One major finding corrects PA14-to-PAO1 source-citation routing and omitted native methods. One minor finding identifies duplicate Ruta publication registrations. Historical 1945 occurrence is supported by a 1952 primary identity bridge; the 1965 citation and exact1999 Ruta assignment remain unverified.

## Scope And Provenance

One entire owner and resolved mechanism: seven LOTUS triples, one producer/locus, two sibling links and all 19 nodes / 17 edges across two inline graphs, including provenance and history.

Selection: Eleventh initially unreviewed path, first in batch 002 from fresh origin/main. The authoritative fresh-main list has 91 valid bundles covering 54 of 3,116 records; the ten separately validated reviews in pending PR 1000 bring campaign coverage to 64 paths before this review. All coverage inventories include ignored files. This bundle assesses exactly one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-182e475a70 | data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml | generated | 2-heptylquinolin-4(1H)-one |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and component validation | passed | True | naturalproductmech:mibig-182e475a70 | One complete owner and two inline graphs validated with zero ERROR rows. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-182e475a70 | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-182e475a70 | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-182e475a70 | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-182e475a70 | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate after environment repair | passed | True | naturalproductmech:mibig-182e475a70 | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Exact chemical and native protein reference audit | passed | True | naturalproductmech:mibig-182e475a70 | Owner SMILES/InChI/key agree; default ChEBI molfiles distinguish the tautomers. Five full native CDS translations equal independent GenPept and UniProt sequences. |
| Exact compound assignment in the1999 Ruta primary | unavailable | True | naturalproductmech:mibig-182e475a70 | Publisher abstract is readable but does not specify the heptyl member. The located public PDF did not provide readable body or image data through the attempted routes. |
| Complete bounded reaction and annotation graphs | passed | True | naturalproductmech:mibig-182e475a70 | All19 nodes and 17 edges were audited across PAO1 PqsBC primary assays, exact native references and explicitly database-level PqsA/D/E annotations. Construct, net-conversion and essentiality limits are preserved. |
| Historical P. aeruginosa HHQ occurrence identity bridge | passed | True | naturalproductmech:mibig-182e475a70 | Hays 1945 isolation plus Wells 1952 synthetic/authentic comparison establish the Pyo Ib–HHQ identity bridge. |
| Exact-compound support in Luckner and Ritter 1965 | unavailable | True | naturalproductmech:mibig-182e475a70 | Publisher access returned HTTP 403 and no readable primary experimental text was obtained. Exact homologue and methods remain unknown. |
| Bounded iModulonDB component and dataset context audit | passed | False | naturalproductmech:mibig-182e475a70 | Relevant component 85 membership and dataset species/strain context were inspected using the installed runner and the primary dataset publication. Coexpression was kept separate from biosynthetic causality. |
| precise411 searches through installed source runner | failed | False | naturalproductmech:mibig-182e475a70 | The optional search command ran and exited 2 on typed regulator=NoneType parsing; relevant dataset contents remained unavailable. No biological absence conclusion. |

## Scientific And Domain Assessments

### Exact achiral HHQ owner identity

identity: supported. Targets: naturalproductmech:mibig-182e475a70.

The valid owner graph, stored complete InChI/key, computed formula and current PubChem/NPAtlas records agree on neutral HHQ. The source label, actual quinolone depiction and stereo_complete flag are coherent. The hydroxy wording in older primary literature and NPAtlas original_name is reconciled through explicitly represented tautomerism rather than mistaken for PQS, HQNO or a longer side-chain congener.

### NPA026460 exactly matches the represented quinolone

identity: supported. Targets: naturalproductmech:mibig-182e475a70.

The current NPAtlas structure is exactly the owner keto tautomer, with the same full structure and no reassignment. Its origin reference and organism are retained as source metadata; the seven occurrence citations are reviewed separately.

### Conservative collision status is valid and exact candidate is now resolved

grounding: supported. Targets: naturalproductmech:mibig-182e475a70.

REVIEW_NEEDED is an accurate result of the present multi-three-star-key policy, so it is not a false exact-grounding claim. Official default molfiles now identify CHEBI:62219 as the owner graph and CHEBI:75306 as its hydroxy tautomer, despite both Standard InChIKeys being identical. This establishes the scientific candidate choice; implementing a durable grounding decision remains separate from this read-only review.

### Five exact native PAO1 reference sequences verified

grounding: supported. Targets: naturalproductmech:mibig-182e475a70.

Each selected accession has the correct PAO1 strain/taxon, gene, locus, protein length and genomic coordinates. Independent table 11 translation agrees with the deposited CDS translation, separately retrieved GenPept protein and UniProt at every residue. This validates native references and the historical version/length notes, without asserting tagged, mutated or historical plasmid-sequence equivalence.

### PqsA/PqsD/PqsE graph matches its stated annotation scope

graph: supported. Targets: naturalproductmech:mibig-182e475a70.

All ten database-only reaction/substrate/product edges agree with the current reviewed PqsA, PqsD and PqsE annotations. ATP/CoA use, AMP/diphosphate release, malonyl-CoA condensation to 2-ABA-CoA and hydrolysis to 2-ABA are represented at the correct evidence tier. The graph is explicitly unbalanced and omits some reaction species, so no stoichiometric completion is inferred. It avoids DHQ-to-HHQ substitution, PqsE essentiality, complete-route reconstitution and borrowed PA14 regulatory function. All three quoted snippets are literal matches. The separate final 2-ABA-to-HHQ net-assay link is documented in the primary-source assessments.

### PqsB/PqsC native reference labels preserve subunit and construct limits

graph: supported. Targets: naturalproductmech:mibig-182e475a70.

Current reviewed annotations support the selected protein labels and PqsBC association. The graph uses PROTEIN for PqsB and ENZYME for PqsC and expressly avoids assigning independent PqsB catalysis, enzyme-controlled ring closure or physiological complex stoichiometry. Native sequence agreement is separate from the PDB/experimental construct audit, documented in the primary-source assessments.

### Three exact natural-occurrence associations

evidence: supported. Targets: naturalproductmech:mibig-182e475a70.

Haplophyllum occurrence is supported under its accepted synonym; Streptomyces MBTG13 and Pseudoalteromonas M2 support the recorded genus-level associations. Primary isolate evidence does not automatically promote these LOTUS associations into biosynthesis-grade producers. All five provenance entities match their recorded taxon identifiers.

### Exact HHQ assignment in the cited Ruta paper

evidence: unknown. Targets: naturalproductmech:mibig-182e475a70.

The primary abstract identifies an unresolved homologue mixture but not the exact heptyl member. Exact occurrence is therefore not independently established in this review. The two DOI registrations refer to one paper; neither registration is a second isolation. Lack of readable primary compound-level evidence does not establish absence from Ruta.

### Pinned sibling links and broad antibacterial summary

evidence: supported. Targets: naturalproductmech:mibig-182e475a70.

Both pinned sibling records resolve and justify the summary at the repository-defined source-role tier. The inspected 2019 purified-compound bacterial assays independently support broad antibacterial activity. No MIC value, direct microbial target, clinical efficacy or antifungal-growth claim is imported into the owner. Shared Standard InChIKey linkage is distinct from exact fixed-H tautomer equality.

### Computed filing, asserted classifications and bounded curation history

provenance: supported. Targets: naturalproductmech:mibig-182e475a70.

NPClassifier outputs match the pinned exact-key result and remain computational. MIBiG source classes are separately asserted, with no inference that the tryptophan classification proves a precursor experiment. Two bounded graph-curation events do not claim whole-record review, and SEEDED remains appropriate. The earlier primary-access discussion is historical and is not contradicted by later successful retrieval.

### Entire owner and resolved mechanism coverage

scope: supported. Targets: naturalproductmech:mibig-182e475a70.

The complete owner, all 19 nodes and 17 edges in two inline graphs, source provenance, discussions and history were read. Separate assessments address each assertion group. There are no external components or quantitative/clinical claims to audit in this owner; optional mechanism expansion is outside the required completion criteria. Unavailable historical occurrence checks are explicit.

### Exact HHQ native PAO1 production and pqs locus

evidence: supported. Targets: naturalproductmech:mibig-182e475a70.

MIBiG compound 3, the recorded PAO1 reference interval, the PAO1-derived 2016 enzyme assay and the PAO1 Copenhagen native 2021 measurements converge on this exact product. The native pqsA deletion/restoration evidence supports BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED after maintained curation. Stock provenance and reference-locus mapping remain explicit; whole-region sufficiency and universal PhnAB necessity do not follow.

### Source compound evidence versus strain-specific producer and locus citations

evidence: concern. Targets: naturalproductmech:mibig-182e475a70.

The generated claim references route a PA14 study to PAO1 producer and locus claims without a strain qualifier. This does not refute PAO1 production; separately inspected PAO1 studies support it. One claim-specific citation and method correction resolves the scope mismatch and the inherited unstated methods.

### All seven nodes and six edges of pqsbc-pao1-net-hhq-formation

evidence: supported. Targets: naturalproductmech:mibig-182e475a70.

The two native references, association edges, two assay substrates, net process and detected HHQ product are supported at the explicitly bounded level. Exact short snippets match the primary text. The record correctly separates wild-type-derived assay preparation from the C129A crystal, sample sequence from native reference, net chemistry from unresolved ring closure, and association from independent subunit catalysis or physiological oligomerization. No graph correction is indicated.

### Final net assay connection in pqsade-pao1-annotated-hhq-precursors

evidence: supported. Targets: naturalproductmech:mibig-182e475a70.

The 2-ABA is_assay_precursor_of HHQ edge explicitly requires the separate PqsBC assay and octanoyl-CoA. It accurately avoids a one-step PqsE-to-HHQ reaction and a full-pathway reconstitution. Upstream PqsA/D/E catalytic statements are separately labelled database assertions; their full native reference/annotation audit is documented in the companion assessments.

### Reused PAO1 iModulon context

evidence: supported. Targets: naturalproductmech:mibig-182e475a70.

precise364 component 85 groups pqsABCDE and phnAB in a PAO1-lineage compendium. This is compatible transcriptional context for the HHQ pathway and is not used to establish exact chemistry, native necessity or complex assembly. The optional precise411 runner parsing failure is preserved as unavailable evidence, not absence.

### Retrospective Pyo Ib to HHQ primary identity bridge

evidence: supported. Targets: naturalproductmech:mibig-182e475a70.

The 1945 natural isolation and 1952 explicit structural assignment together support the recorded species-level occurrence. The older provisional name is not a demonstrated erroneous citation. Historical clinical strains remain distinct from PAO1, and mixture activity is not attributed to pure HHQ.

### Independent 1965 occurrence citation

evidence: unknown. Targets: naturalproductmech:mibig-182e475a70.

No readable experimental source was obtained for the 1965 assertion. A positive 1945/1952 identity bridge does not validate a separate publication. Full primary inspection must resolve the homologue and organism scope before this individual citation is signed off.

## Findings

### R-RUTA-REDUNDANCY: Two Ruta occurrences cite two registrations of the same paper

minor / open / confirmed; issue key: lotus-hhq-ruta-graveolens-duplicate-publication-dois.

The otherwise identical Ruta graveolens occurrences use PL00010251 and S007060050230. Publisher and Crossref metadata match the same four authors, German title, volume 130 issue 5 and page 703, including the original article identifier 91300703. Treating these as two displayed occurrence entries obscures that there is one publication. This bibliographic redundancy is established independently of the still-unverified exact HHQ assignment in the 1999 full text.

### hhq-pao1-claim-scope-and-methods: PA14 compound evidence is routed to PAO1 producer and locus claims

major / open / confirmed; issue key: mibig-bgc0000922-compound3-pao1-claim-reference-scope.

BGC0000922 compound 3 uses the 2013 Dulcey citation as compound-level MS evidence. The seeder attaches that reference to a specific PAO1 taxon and genomic interval, but the inspected study uses PA14 native strains and a PA14-derived PqsC construct. This is a claim-level strain mismatch, not evidence that PAO1 fails to produce HHQ. Direct PAO1-derived enzymology and PAO1 Copenhagen native pqsA loss/restoration data are available, so the citation can be corrected and the inherited SOURCE_ASSERTION/CLUSTER_UNSTATED methods completed reproducibly in the same curation action. The correctly bounded existing graph does not need a separate finding.

## Recommended Actions And Acceptance Checks

### R-CANONICALIZE-RUTA-PUBLICATION

Represent these verified DOI aliases as one Ruta occurrence/publication association through a maintained, tested DOI-alias normalization or source grouping step. Preserve both original DOI strings and raw source rows in provenance. Use the current publisher DOI PL00010251 as the display reference. Verify the original compound-level assignment separately before claiming full occurrence review; do not infer an exclusion of HHQ from lack of primary access.

- One generated Ruta occurrence represents this one publication, retaining both original DOI aliases in evidence or provenance. Independent Ruta publications must remain distinct.
- Pin and test the exact DOI pair, taxon 37565 and full owner key; do not globally collapse different articles on title resemblance alone. Preserve raw source assertions and MANIFEST/reproduction provenance.
- Run the documented extraction/seed canary as applicable, inspect the owner diff and preserved graphs, then strict target validation, verify-reproduction, verify-corpus --summary and qc.

### route-hhq-pao1-evidence-and-grade

Add a claim-reference decision for BGC0000922:3 pinned to full source-row SHA256 c3f5cdc523e4b0c2930fccdaeed45d3b942d4aab117341c543ceb06f941051cd. Use DOI:10.1371/journal.ppat.1009425 for both native PAO1 producer and locus claims, retaining the Copenhagen strain, pqsA deletion, tatA-intact restoration and LC-MS/MS scope in the rationale. Preserve the imported 2013 PA14 citation as original compound evidence in the raw row. Pair that decision with a REPLACE method override adding Knock-out studies, which yields BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED under the current rubric. Keep the independently supported 2016 PqsBC graph and its enzyme-assay evidence; any additional Enzymatic assays method must carry its own claim-local 2016 reference rather than borrowing the 2021 method citation.

- The REPLACE override is paired with the existing full-row-SHA claim-reference validation, or the method loader is extended to enforce equivalent context. Current expected_* fields alone protect WITHDRAW, not REPLACE. Demonstrate rejection on a changed compound index, taxon, locus, source citation or structure row.
- Only BGC0000922:3 (HHQ) changes; compound 1 PQS and compound 2 dihydroxyquinoline are not upgraded by inference. Pin source version 5, taxon 208964, AE004091.2:1073960..1087095 and UYRHHBXYXSYGHA-UHFFFAOYSA-N through the full row digest.
- Regenerated references distinguish the 2013 PA14 compound study, 2016 PAO1-derived purified-complex assay and 2021 PAO1 Copenhagen native genetics. Preserve original source provenance and distinguish citation routing from evidence grading.
- The regenerated native knockout method supports BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED but does not claim full bounded-locus sufficiency, sequence identity of historical stocks, universal PhnAB necessity, or a native P. putida producer.
- Both existing graphs retain their construct, net-reaction, annotation-only and stoichiometry limits; the PDB C129A model is not described as the active wild-type assay preparation.
- Run the documented seed canary for naturalproductmech:mibig-182e475a70, inspect generated differences, then documented regeneration, strict target validation, verify-reproduction, verify-corpus --summary and qc.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-IDENTITY-LOCAL | data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml; Complete owner and identical resolved record; chemical_structure, xrefs, source_concepts, grounding fields, both inline graphs and discussions | supports | The full owner represents achiral neutral HHQ as the quinolin-4(1H)-one graph, C16H21NO and key UYRHHBXYXSYGHA-UHFFFAOYSA-N. Its source concept is BGC0000922:3 and the stored minted identifier equals the seeder hash of that exact source key. The record explicitly retains REVIEW_NEEDED for two ChEBI candidates and distinguishes all five native PAO1 protein references from experimental constructs. |
| E-CHEMISTRY-IDENTITY | /private/tmp/npm-review-work/011/chemistry.json; Pinned RDKit result for complete owner SMILES | supports | The owner SMILES regenerates the stored complete InChI/key and neutral formula C16H21NO, exact mass 243.162314292; there are no stereocenters. Its stereo_complete=true is appropriate for this achiral graph. |
| E-NPATLAS | https://www.npatlas.org/api/v1/compound/NPA026460?include=classifications; Official current JSON: npaid, original_name, full smiles/inchi/inchikey, origin_reference, current mol_structures and reassignments | supports | NPA026460 is C16H21NO with the same complete InChI/key and quinolone SMILES CCCCCCCC1=CC(=O)C2=CC=CC=C2[NH]1. Its original name is 2-n-heptyl-4-hydroxyquinoline, but the displayed current graph is exactly the owner quinolone; reassignments is empty. Its origin reference is DOI:10.3390/md17020133, PMID:30813382, Streptomyces sp. MBTG13. The source was inspected through the official web API; direct file download returned HTTP 403, so no full-response checksum is claimed. |
| E-CHEBI-62219 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/62219/; Current default structure, full chemical identity and explicit tautomer relation; reused source preparation | supports | Current CHEBI:62219 is three-star 2-heptyl-4-quinolone, IUPAC 2-heptylquinolin-4(1H)-one; neutral C16H21NO. Its default full InChI gives UYRHHBXYXSYGHA-UHFFFAOYSA-N and a quinolin-4(1H)-one with a C7 heptyl substituent at C2. The default SMILES is not parseable by RDKit because it lacks the needed aromatic [nH]; the InChI parses and generates CCCCCCCc1cc(=O)c2ccccc2[nH]1. This is a database representation observation, not a target-record finding. |
| E-CHEBI-75306 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/75306/; Current default structure, full chemical identity and explicit tautomer relation; reused source preparation | supports | CHEBI:75306 is the separate three-star 2-heptyl-4-hydroxyquinoline entry. Both ChEBI records explicitly assert the tautomer relation and share the Standard InChI/key. Its aromatic hydroxyl SMILES parses. Standard InChIKey equality alone cannot select the represented tautomer; the separately inspected official default molfiles provide that distinction. |
| E-PUBCHEM | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/UYRHHBXYXSYGHA-UHFFFAOYSA-N/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; Complete full-key property JSON: PubChem CID, InChI, InChIKey, molecular formula and SMILES | supports | The full-key query resolves to PubChem CID164974, C16H21NO, with the same complete Standard InChI/key. PubChem SMILES CCCCCCCC1=CC(=O)C2=CC=CC=C2N1 independently yields that key and formula; there are no stereocenters. The nonaromatic ring carbon after seven side-chain carbons is part of the ring, not an eighth side-chain carbon. |
| E-CHEBI-MOL-62219 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/62219/; Official default-structure molfile, complete atom/bond representation | supports | The current official default molfile for CHEBI:62219 is parseable. It is the neutral quinolin-4(1H)-one graph represented by the owner. |
| E-CHEBI-MOL-75306 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/75306/; Official default-structure molfile, complete atom/bond representation | supports | The current official default molfile for CHEBI:75306 is parseable. It is the neutral 4-hydroxyquinoline tautomer, with a different fixed hydrogen position and bond graph from the owner. |
| E-CHEBI-TAUTOMER-COMPARISON | /private/tmp/npm-review-work/011/chebi-mol-comparison.json; Complete canonical graph and fixed-H InChI comparison of owner against both official default molfiles | supports | CHEBI:62219 default MOL canonicalizes to owner CCCCCCCc1cc(=O)c2ccccc2[nH]1 and fixed-H InChI ending /f/h17H. CHEBI:75306 gives CCCCCCCc1cc(O)c2ccccc2n1 and /f/h18H. Both retain the same Standard InChI/key; this is a tautomer collision, not a compound/zwitterion pair. The malformed ChEBI62219 SMILES does not prevent comparison of its valid official default MOL. |
| E-GROUNDING-INVENTORY | data/raw/chebi_structures.tsv; Exact-key rows CHEBI:62219 and CHEBI:75306 | supports | Both pinned three-star rows share key UYRHHBXYXSYGHA-UHFFFAOYSA-N. Their definitions distinguish the quinolone from 4-hydroxyquinoline; the former exported SMILES is malformed while the latter is valid. Current default molfiles resolve which represented tautomer matches the owner. |
| E-GROUNDING-IMPLEMENTATION | scripts/seed_from_sources.py; mint_identifier lines284-292; chebi_by_key construction and multi-match grounding branch lines881-889 and955-978 | supports | The implemented seeder uses full-key collision count: multiple three-star matches stay minted with REVIEW_NEEDED. The owner accurately reproduces this rule. The generated note uses a generic compound/zwitterion example, whereas this exact pair are neutral tautomers. No candidate-level molfile decision is made in this branch. |
| E-GROUNDING-OWNERSHIP | docs/CURATION.md; The decision file, especially lines17-21; supported MIBiG structure-correction actions | supports | The documentation explicitly says curation/decisions.tsv is reserved and not consumed. Existing structure corrections require an unambiguous destination and do not supply a same-key candidate-choice mechanism. A future exact-tautomer grounding change requires an implemented, tested consumer and guarded migration rather than merely adding a reserved decision row or hand-editing generated YAML. |
| E-GROUNDING-CONSUMER-SEARCH | scripts/seed_from_sources.py; src; tests; conf; curation; .claude; docs; rg --no-ignore --hidden grounding/override/load-decisions/decisions.tsv queries | context_only | The bounded maintained-source search found the documented reserved decisions format and references, but no implemented grounding-decision loader in the searched code. Direct seeder and ownership documentation reads establish the current effective behavior. |
| E-HHQ-PRIMARY-IDENTITY | https://pmc.ncbi.nlm.nih.gov/articles/PMC337054/; DOI:10.1073/pnas.0307694100; Fig2 SeriesA C7H15/HHQ, Fig4 and methods; complete HTML and figure read | supports | The primary chemical figure explicitly labels the C7H15 member of SeriesA as HHQ, [M+H]+244, while PQS and HQNO are separately labelled compounds. The drawing uses the hydroxy tautomer. Native PA14 culture data establish HHQ identity and natural occurrence; they do not independently establish any one of the seven owner LOTUS citations or native PAO1 locus evidence. |
| E-PQSA-UNIPROT | https://rest.uniprot.org/uniprotkb/Q9I4X3.json; entryAudit, organism, genes, sequence, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT and EMBL reference | supports | Reviewed Q9I4X3, version 115, is PAO1 taxon 208964 pqsa/PA0996, 517 aa, linked to AAG04385.1. Current FUNCTION/CATALYTIC ACTIVITY support anthranilate + ATP + CoA yielding anthraniloyl-CoA, AMP and diphosphate (RHEA:10828). |
| E-PQSA-GENPEPT | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AAG04385.1&amp;db=protein&amp;report=genpept&amp;retmode=text; LOCUS, organism/source taxon, gene/locus_tag, coded_by, translation table and complete ORIGIN | supports | AAG04385.1 is native PAO1 pqsa/PA0996, taxon 208964, 517 aa, coded by AE004091.2:1078462..1080015 on the plus strand, translation table 11. Its full sequence agrees exactly with independently translated genomic DNA and UniProt. |
| E-PQSB-UNIPROT | https://rest.uniprot.org/uniprotkb/Q9I4X2.json; entryAudit, organism, genes, sequence, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT and EMBL reference | supports | Reviewed Q9I4X2, version 108, is PAO1 taxon 208964 pqsb/PA0997, 283 aa, linked to AAG04386.1. Current FUNCTION/SUBUNIT describe association with PqsC and probably a folding role rather than independent PqsB catalysis. The owner does not adopt broader ring-closure language as an elementary reaction assignment. |
| E-PQSB-GENPEPT | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AAG04386.1&amp;db=protein&amp;report=genpept&amp;retmode=text; LOCUS, organism/source taxon, gene/locus_tag, coded_by, translation table and complete ORIGIN | supports | AAG04386.1 is native PAO1 pqsb/PA0997, taxon 208964, 283 aa, coded by AE004091.2:1080009..1080860 on the plus strand, translation table 11. Its full sequence agrees exactly with independently translated genomic DNA and UniProt. |
| E-PQSC-UNIPROT | https://rest.uniprot.org/uniprotkb/Q9I4X1.json; entryAudit, organism, genes, sequence, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT and EMBL reference | supports | Reviewed Q9I4X1, version 132, is PAO1 taxon 208964 pqsc/PA0998, 348 aa, linked to AAG04387.1. Current FUNCTION/SUBUNIT and RHEA:50396 describe the PqsBC complex and net HHQ production. The accession is the wild-type native reference, not the C129A crystal or tagged assay construct. |
| E-PQSC-GENPEPT | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AAG04387.1&amp;db=protein&amp;report=genpept&amp;retmode=text; LOCUS, organism/source taxon, gene/locus_tag, coded_by, translation table and complete ORIGIN | supports | AAG04387.1 is native PAO1 pqsc/PA0998, taxon 208964, 348 aa, coded by AE004091.2:1080853..1081899 on the plus strand, translation table 11. Its full sequence agrees exactly with independently translated genomic DNA and UniProt. |
| E-PQSD-UNIPROT | https://rest.uniprot.org/uniprotkb/P20582.json; entryAudit, organism, genes, sequence, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT and EMBL reference | supports | Reviewed P20582, version 147, is PAO1 taxon 208964 pqsd/PA0999, 337 aa, linked to AAG04388.1. Current FUNCTION/CATALYTIC ACTIVITY support anthraniloyl-CoA plus malonyl-CoA yielding 2-ABA-CoA with CoA and carbon dioxide (RHEA:50472). DHQ is a separate spontaneous product discussed in the source and is not asserted as HHQ in the owner. |
| E-PQSD-GENPEPT | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AAG04388.1&amp;db=protein&amp;report=genpept&amp;retmode=text; LOCUS, organism/source taxon, gene/locus_tag, coded_by, translation table and complete ORIGIN | supports | AAG04388.1 is native PAO1 pqsd/PA0999, taxon 208964, 337 aa, coded by AE004091.2:1081942..1082955 on the plus strand, translation table 11. Its full sequence agrees exactly with independently translated genomic DNA and UniProt. |
| E-PQSE-UNIPROT | https://rest.uniprot.org/uniprotkb/P20581.json; entryAudit, organism, genes, sequence, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT and EMBL reference | supports | Reviewed P20581, version 129, is PAO1 taxon 208964 pqse/PA1000, 301 aa, linked to AAG04389.1. Current FUNCTION/CATALYTIC ACTIVITY support 2-ABA-CoA hydrolysis to 2-ABA and CoA (RHEA:49444). The owner does not import the broader PA14 RhlR regulatory annotations or claim PqsE is physiologically indispensable. |
| E-PQSE-GENPEPT | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AAG04389.1&amp;db=protein&amp;report=genpept&amp;retmode=text; LOCUS, organism/source taxon, gene/locus_tag, coded_by, translation table and complete ORIGIN | supports | AAG04389.1 is native PAO1 pqse/PA1000, taxon 208964, 301 aa, coded by AE004091.2:1082949..1083854 on the plus strand, translation table 11. Its full sequence agrees exactly with independently translated genomic DNA and UniProt. |
| E-PAO1-GENOME | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AE004091.2&amp;db=nuccore&amp;report=genbank&amp;retmode=text&amp;from=1073960&amp;to=1087095; AE004091.2 slice 1073960..1087095; five complete CDS features, deposited translations and ORIGIN | supports | Reused the previously fetched official PAO1 interval, 13,136 nt. Complete pqsA-E CDS features encode AAG04385.1 through AAG04389.1, each with codon_start 1 and translation table 11. Absolute coordinates were reconstructed from slice offset and independently agree with GenPept coded_by. |
| E-PROTEIN-EQUIVALENCE | /private/tmp/npm-review-work/011/protein-equivalence.json; Independent table 11 translation of each complete genomic CDS and comparisons to deposited CDS, GenPept and UniProt | supports | All five comparisons are exact at every residue: PqsA 517 aa (1554nt, ATG/TGA); PqsB 283 aa (852nt, ATG/TAA); PqsC 348 aa (1047nt, ATG/TGA); PqsD 337 aa (1014nt, ATG/TGA); PqsE 301 aa (906nt, ATG/TGA). All five have taxon 208964, the expected PA0996-PA1000 loci and no internal stop codons. The result records nucleotide/protein SHA256 values and confirms all three owner UniProt snippets literally occur in the cited current records. |
| R-LOCAL | data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml; Entire owner and read_natural_product resolved view; exact-key inventories, source concepts, classifications, all 19 nodes and 17 edges, discussions and history | supports | Seven LOTUS structure/taxon/reference triples remain occurrence assertions, distinct from one PAO1 producer and locus. The two inline graphs contain 19 nodes and 17 edges. NPClassifier values match the exact-key inventory; MIBiG classes remain separately asserted. Two seed and two bounded mechanism curation events coexist with SEEDED status. No external components, separate pathway steps, molecular-target entries or quantitative activity assertions occur in the complete resolved owner. |
| R-HAPLOPHYLLUM-PRIMARY | https://www.researchgate.net/profile/Luc-Angenot/publication/244500675_Alkaloids_from_Haplophyllum_leptomerum/links/581471ed08ae90acb23bfdaa/Alkaloids-from-Haplophyllum-leptomerum.pdf; DOI:10.1007/s10600-010-9661-y, pp 502-503; full author-uploaded article text inspected through its publication page and extracted PDF text | supports | Compound 6 is 2-heptylquinolin-4-one, isolated as 13 mg from the aerial parts of Haplophyllum leptomerum collected in the Babataga Mountains in May 2008. Proton NMR and comparison with a synthetic sample support its identity. This establishes plant occurrence; the separate root isolates and dictamnine anticancer results do not apply to HHQ. |
| R-HAPLOPHYLLUM-TAXON | https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:771290-1; Kew POWO accepted name and complete synonym list | supports | POWO accepts Haplophyllum griffithianum and explicitly lists H. leptomerum as a heterotypic synonym. Thus the primary paper name and recorded occurrence name are compatible; this is not a species-scope mismatch. |
| R-STREPTOMYCES | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=6410270&amp;retmode=xml; DOI:10.3390/md17020133; PMID:30813382; Results 2.1-2.3, Methods 4.2-4.3, Table 1 | supports | The primary article isolates compound 1, explicitly 2-n-heptyl-4-hydroxyquinoline, from a six-week rice culture of Streptomyces sp. MBTG13. Its NMR/UV identity is separated from the N-oxide, octyl and dione congeners. The organism is retained at genus level despite 99% 16S identity to a named species. Purified compound 1 has bacterial MIC measurements, independently supporting the broad ANTIBACTERIAL summary. No Candida growth-inhibition or direct Efg1-binding claim follows from the separate hyphal-response results. |
| R-PSEUDANE | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=5706026&amp;retmode=xml; DOI:10.3390/md15110336; PMID:29104209; Results 2.1-2.2, Table 1, Methods 4.2-4.4 | supports | Pseudane-VII is isolated from Pseudoalteromonas sp. M2 culture supernatant. The main compound is checked against a standard, purified (11.37 mg), and analyzed by proton/carbon NMR. Its [M+H]+244.1695, six side-chain methylenes and terminal methyl distinguish the heptyl congener from adjacent pseudanes. The source calls the family 4-hydroxy-2-alkylquinolines; ChEBI independently supplies the pseudan VII synonym for the matching HHQ tautomer. This supports the conservative genus-level occurrence. Adjacent peaks described as tentative are not substituted for the isolated principal compound. |
| R-TAXON-PROVENANCE | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q18080097%7CQ1144013%7CQ31856%7CQ25062%7CQ842207&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Official entity labels and complete P685 claims for all five unique provenance URIs | supports | Q18080097 maps to Haplophyllum griffithianum/1006075; Q1144013 to Streptomyces/1883; Q31856 to Pseudomonas aeruginosa/287; Q25062 to Ruta graveolens/37565; Q842207 to Pseudoalteromonas/53246. These match the recorded taxonomy identifiers and preserve genus versus species scope. |
| R-RUTA-DOI1 | https://api.crossref.org/works/10.1007%2FPL00010251; Crossref complete metadata for DOI:10.1007/PL00010251 | supports | The deposited article has English and German titles, four authors Kostova/Ivanova/Mikhova/Klaiber, volume 130 issue 5, pages 703-707 and May 1999 date. Its alternative identifier is91300703. Metadata establish the publication, not its individual compound inventory. |
| R-RUTA-DOI2 | https://api.crossref.org/works/10.1007%2FS007060050230; Crossref complete metadata for DOI:10.1007/S007060050230 | supports | The older DOI has the same German title, four authors, volume 130 issue 5 and page 703 in 1999; its original publisher URL ends91300703.htm. Together with the newer record this identifies duplicate DOI registrations for the same article, not independent occurrence experiments. |
| R-RUTA-ACCESS | https://link.springer.com/article/10.1007/PL00010251; Complete publisher abstract and metadata; author-uploaded PDF acquisition also attempted | partial | The primary abstract reports four new quinolone homologues and thirteen known components from Bulgarian-grown Ruta graveolens, but does not name individual homologues. The author-uploaded five-page PDF is discoverable; direct retrieval returned HTTP 403, extracted text was empty, and screenshot tools returned placeholders without inspectable image data. The publisher PDF URL returned HTML rather than PDF. Exact HHQ attribution in this 1999 article remains unverified. Search-result snippets from later papers were not treated as its primary body. |
| R-RUTA-SEARCH | https://www.researchgate.net/publication/225245803_Alkaloids_and_Coumarins_from_Ruta_graveolens; Bounded public-source retrieval and web queries | unknown | The publisher preview and author-uploaded file were located; no readable compound-level 1999 text was obtained in these attempts. Later primary and secondary references are useful leads but do not resolve what was actually assigned in the cited paper. |
| R-SIBLING-QUINOLONE | https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml; Entire exact pinned AntibioticMech YAML at commit74f6cc8362498900f2fe2c13d0b6fdb66dd30976 | supports | The pinned sibling identifier, label, full Standard InChIKey and ANTIBACTERIAL class agree with the generated link and activity summary. The quinolone and hydroxyquinoline siblings preserve separate ChEBI concepts with a shared tautomer-normalized key. These are seeded activity-role assertions without quantitative mechanism claims; SAME_INCHIKEY does not establish fixed-H graph identity. |
| R-SIBLING-HYDROXY | https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml; Entire exact pinned AntibioticMech YAML at commit74f6cc8362498900f2fe2c13d0b6fdb66dd30976 | supports | The pinned sibling identifier, label, full Standard InChIKey and ANTIBACTERIAL class agree with the generated link and activity summary. The quinolone and hydroxyquinoline siblings preserve separate ChEBI concepts with a shared tautomer-normalized key. These are seeded activity-role assertions without quantitative mechanism claims; SAME_INCHIKEY does not establish fixed-H graph identity. |
| R-SIBLING-INVENTORY | data/raw/antibioticmech_inchikeys.tsv; Complete TSV parsed; exact full-key rows and MANIFEST pin; seeder full-key join | supports | Both matching sibling rows carry the exact inspected commit and identifiers. The seeder faithfully emits SAME_STRUCTURE with basis SAME_INCHIKEY and derives ANTIBACTERIAL from the pinned sibling class. This is the repository-defined Standard InChIKey relation, not a claim that the two fixed-H tautomer drawings are identical. |
| R-RUTA-TRANSFORM | scripts/extract_lotus.py; extract_rows exact (key, organism, DOI) signature; seeder LOTUS loop emits one occurrence for each retained triple | supports | The existing extractor deduplicates identical DOI strings, so the two bibliographic aliases survive as distinct triples and the seeder emits two otherwise identical Ruta occurrences. No source-row deletion is needed to document that these refer to one publication. |
| R-ISSUE822 | https://github.com/CultureBotAI/NaturalProductMech/issues/822; Read-only gh issue view822; full title, body and OPEN state | supports | The explicitly linked historical issue concerns the unparsable CHEBI62219 exported SMILES, while affirming the valid MIBiG owner and preserving the tautomer ambiguity. Current source inspection confirms the same exported-string defect and provides a valid default molfile. This review neither closes that issue nor treats it as a validated structured predecessor. |
| hhq-source922-compound3 | https://mibig.secondarymetabolites.org/repository/BGC0000922.5/annotations.json; Version 5 complete entry: compounds[2] (one-based compound_index 3), taxonomy, loci and biosynthesis; original /010/mibig922.json reused | supports | Exact HHQ is compound 3, distinct from compound 1 PQS and compound 2 dihydroxyquinoline. Its structure is C16H21NO with the owner StandardInChIKey UYRHHBXYXSYGHA-UHFFFAOYSA-N. The source records PAO1 taxon 208964, AE004091.2:1073960..1087095 and PKS/Type III, with no locus methods. Its mass-spectrometry compound-identification citation is DOI:10.1016/j.chembiol.2013.09.021. Source quality is questionable and completeness unknown. The original external access time is retained; applicability to the full 011 owner and exact source row was checked on 2026-10-21 at 07:43:16Z. |
| hhq-pao1-locus-reference | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AE004091.2&amp;db=nuccore&amp;report=genbank&amp;retmode=text&amp;from=1073960&amp;to=1087095; Complete source and CDS annotations in /010/ae004091-bgc.gb; same accession and bounds as 011 | supports | This PAO1 reference interval includes pqsABCDE (PA0996-PA1000), phnAB (PA1001/PA1002) and mvfR (PA1003), together with upstream genes. It bridges the named pqsA and PqsBC experiments to the represented locus. Unlinked pqsH is not within these bounds and consumes HHQ in PQS formation. Reference annotation does not sequence-verify the historical Copenhagen stock or prove sufficiency of every base in the bounded interval. Original external access retained; record applicability checked afresh. |
| hhq-primary2013-strain-scope | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=3877684&amp;retmode=xml; DOI:10.1016/j.chembiol.2013.09.021 / PMID:24239007; full primary XML, Table 1 and Methods P44/P51/P57; Figure 3 and Figure 5b | partial | The native Pseudomonas strains in Table 1 are PA14 and its derivatives. Native genetics, isotope incorporation and product measurements concern that lineage. The tagged PqsC construct is explicitly amplified from PA14; PqsB comes through a supplied pMSR1 construct whose original template is not independently sequenced here. The paper establishes exact HHQ formation, including copurified PqsBC plus 2-ABA and octanoyl-CoA, but is not direct PAO1 native experimentation. Figure 3 totals HAQs rather than providing an isolated HHQ endpoint. This is legitimate compound evidence whose unqualified routing to a PAO1 strain/locus claim exceeds its inspected experimental scope. |
| hhq-primary2016-pqsbc-assay | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=4807248&amp;retmode=xml; DOI:10.1074/jbc.M115.708453 / PMID:26811339; Experimental Procedures, Expression and Purification, Enzyme Activity Assays; Results and Figure 7 caption | supports | The study explicitly clones PAO1 pqsB/pqsC into a sequence-verified expression plasmid. PqsC has a His8/TEV/SAG N-terminal fusion and purification includes tag cleavage. Wild-type-derived PqsBC converts supplied 2-ABA plus octanoyl-CoA into HPLC-quantified HHQ at 25 C in 50 mM HEPES pH 8.2, 50 mM NaCl and 100 micromolar DTT; spectroscopy independently follows the net reaction. The owner snippet "quantification of HHQ by HPLC" is exact. This supports the four substrate/process/product edges and the separate 2-ABA assay-precursor edge, without proving a complete PqsA/D/E/BC reconstitution. |
| hhq-primary2016-association-and-boundaries | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=4807248&amp;retmode=xml; Same full manuscript: purification, PqsBC C129A crystal structure results, Table 1 and final Discussion paragraph | supports | Copurification, gel filtration and a large PqsB/PqsC interface support association. The owner snippet "form a tight complex" is exact in the Results and Introduction. The crystal is the C129A variant, whereas the net activity assay uses the wild-type-derived preparation. The paper proposes a scaffolding role for PqsB and leaves elementary cyclization unresolved; the owner quote "ring closure could also occur non-enzymatically" is exact. Thus the graph correctly avoids independent PqsB catalysis, enzyme-catalyzed ring closure and physiological stoichiometry claims. Figure 8 instead uses engineered P. putida KT2440, not a native producer. |
| hhq-primary2021-native-genetics | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=8432897&amp;retmode=xml; DOI:10.1371/journal.ppat.1009425 / PMID:34460871; Results on constitutive pqsABCD, Figure 8 and Methods AQ quantification; full XML | supports | The study separately measures HHQ, PQS and HQNO by LC-MS/MS. In the tatA-intact PAO1 pqsA deletion background, plasmid pqsABCD restores HHQ relative to the empty-vector control; the tatA/pqsA double mutant does not show that restoration. These data establish native pqsA-linked HHQ loss and genetic restoration under the reported conditions. They do not establish unconditional pathway sufficiency, require every bounded-locus gene, or show that PhnAB is universally necessary. |
| hhq-primary2021-strain-table | https://journals.plos.org/plospathogens/article/file?id=10.1371/journal.ppat.1009425.s011&amp;type=supplementary; Official Table S1 DOCX, complete strain and plasmid table; primary-2021-tat-tableS1.docx in HHQ source preparation | supports | The relevant native wild type is PAO1 from the Copenhagen collection, and the pqsA mutant is an in-frame PAO1 deletion. PA14 strains are separately listed for the petA/cytochrome experiments. The pBBR1MCS-5::pqsABCD construct is attributed to the 2011 Niewerth study. This verifies PAO1 lineage, while the exact historical stock and plasmid sequence remain distinct from the current reference genome. |
| hhq-primary2021-fig8-visual | https://journals.plos.org/plospathogens/article/figure/image?size=large&amp;id=10.1371/journal.ppat.1009425.g008; Official Figure 8, visually inspected HHQ panel B at 07:46:48Z; receipt tat2021-fig8-access.json | supports | The HHQ-labelled panel B shows baseline signal for the pqsA deletion with empty vector, a clear signal after pqsABCD complementation, and baseline signal in the tatA/pqsA double mutant with either vector. The adjacent PQS and HQNO panels were kept distinct. The axis is LC-MS/MS peak area, not absolute concentration; no new quantitative yield is inferred. |
| hhq-primary2021-native-wildtype-visual | https://journals.plos.org/plospathogens/article/file?id=10.1371/journal.ppat.1009425.s004&amp;type=supplementary; Official Figure S4 TIFF, plotted HHQ panel A, visually inspected at 07:47:24Z; tat2021-figS4-access.json | supports | Whole-culture extracts of the PAO1 wild type show HHQ at 8 and 16 h, while the tatA/pqsA double mutant remains near baseline with or without pqsABCD. This independently supports native HHQ production rather than only a complemented-mutant observation. The source caption reverses the panel labels (it calls PQS A and HHQ B); the actual plotted axis labels are HHQ A and PQS B. The review follows the explicit plotted chemical labels and preserves the caption discrepancy. |
| hhq-pdb5dwz-construct | https://files.rcsb.org/download/5DWZ.cif; _entity_poly, _struct_ref, _struct_ref_seq and _struct_ref_seq_dif; full deposited sequence comparison in pdb-construct-comparison.json | supports | PqsB entity 2 has the complete 283-residue native Q9I4X2 sequence. PqsC entity 1 has SAG followed by native Q9I4X1 residues 2-348; the sole aligned difference is native C129A (construct position 131), for a 350-residue deposited sample. The current mmCIF still records older A0A072ZZD2 and A0A0C6EZ24 mappings. Independent current UniProt/GenPept/native-CDS comparisons supplied by the identity reviewer establish the chosen PAO1 references. The owner distinguishes both engineered sequence and historical mappings correctly. |
| hhq-pdb5dwz-coverage-assemblies | https://files.rcsb.org/download/5DWZ.cif; _pdbx_struct_assembly, _pdbx_struct_assembly_gen, _pdbx_unobs_or_zero_occ_residues; current RCSB entry and entity JSON cross-checks | supports | The asymmetric unit contains four PqsB and four PqsC chains. Across 2532 sample residues, 2474 are modeled and 58 are unmodeled. Unmodeled counts by author chain are A5/B5/C10/D10/E4/F10/G5/H9. Both deposited assemblies are PISA/author-and-software-defined tetramers of four chains. Current RCSB entity mapping uses Q9I4X1 for PqsC and Q9I4X2 for PqsB, while the mmCIF retains older accessions. This agrees with the owner caveats; deposited assemblies are not independent proof of physiological stoichiometry. |
| hhq-native-reference-for-construct | https://rest.uniprot.org/uniprotkb/Q9I4X1.json; Complete current Q9I4X1 and Q9I4X2 sequence fields; /011/identity-access.json and protein-equivalence.json | supports | The current PAO1 native references contain 348 residues for PqsC and 283 for PqsB. The identity reviewer independently translated the complete native CDSs and matched the corresponding GenPept sequences. This review separately aligned the complete PDB sample sequences: PqsB is exact and PqsC differs only by the N-terminal construct change and C129A described above. Sequence agreement does not independently verify the historical experimental plasmid. |
| hhq-local-claim-routing-and-ownership | data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml; data/raw/mibig_compounds.tsv; curation/mibig_claim_references.tsv; curation/mibig_locus_evidence_overrides.tsv; scripts/seed_from_sources.py; Complete owner and resolved view, exact BGC0000922:3 source row; claim-reference loader and method override implementation | partial | The source compound citation is copied into both PAO1 producer and locus evidence. Full-row canonical SHA256 is c3f5cdc523e4b0c2930fccdaeed45d3b942d4aab117341c543ceb06f941051cd. The separate existing PqsBC graph already correctly uses the PAO1 2016 primary assay. Current claim-reference decisions enforce a complete source-row SHA, whereas expected_* context fields are enforced only for WITHDRAW in the method loader. A future REPLACE must be paired with a SHA-pinned claim-reference row or the loader must be extended; expected_* fields alone do not protect REPLACE. |
| hhq-maintained-override-search | curation/; conf/; rg --no-ignore --hidden for BGC0000922, minted identifier, exact label variants and slug; exit 1 with no matches | context_only | No matching maintained decision row was found in these bounded curation and configuration trees. This supports the local completion task, not a claim that no scientific evidence exists. |
| hhq-imodulon-component85-context | https://imodulondb.org/api/imodulons/p_aeruginosa/precise364/85/genes; Exact component-membership JSON endpoint used by installed runner get_imodulon_genes; verified HTTP200 and matching seven-gene payload; imodulon-component85-source.json plus source-access receipt. Original runner summary and context receipts retained. | context_only | The complete returned membership has seven genes: pqsA/PA0996, pqsB/PA0997, pqsC/PA0998, pqsD/PA0999, pqsE/PA1000, phnA/PA1001 and phnB/PA1002. All seven have positive weights above the reported threshold 0.115881 and member rows name MvfR. PhnA/P09785 and PhnB/P09786 are annotation context for this HHQ locus. STRING identifiers use taxon 208964. PqsH is not among these seven component members; no biological absence or lack of regulation follows. Component weights represent a transcriptomic decomposition, not reaction rates or causal necessity. Reused source inspection with its original timestamp; applicability here is only PAO1 pathway transcriptional context. |
| hhq-imodulon-dataset-strain-context | https://academic.oup.com/nar/article/50/7/3658/6561658; DOI:10.1093/nar/gkac187; Methods, RNA extraction and Data acquisition; Results, iModulon structure of the transcriptome; dataset link | context_only | The dataset's primary publication explicitly links aeruPRECISE364 to the inspected database dataset. It reports PAO1 and PAO1 delta-mexB expression profiles, comprising 364 quality-filtered samples (83 new and 281 public), mapped to PAO1 genome NC_002516.2. Thus this is relevant PAO1 lineage regulatory context, not a PA14 assay. The runner's dataset catalogue independently labels p_aeruginosa/precise364 as Pseudomonas aeruginosa but supplies no strain field; the strain attribution comes from the primary methods. Reused source inspection with its original timestamp; applicability here is only PAO1 pathway transcriptional context. |
| hhq-imodulon-precise411-unavailable | https://imodulondb.org/dataset.html?organism=p_aeruginosa&amp;dataset=precise411; Original root search receipts and .err files for pqs, phn and mvfR | unknown | All three precise411 searches exited 2 with the typed error: imodulons[0].regulator must be a JSON list, got NoneType. The outputs were empty because parsing failed. The dataset is listed by the runner, but relevant components could not be assessed through this runner. This is unavailable evidence, not a negative search result. Reused source inspection with its original timestamp; applicability here is only PAO1 pathway transcriptional context. |
| H-HAYS1945 | https://www.researchgate.net/publication/232301559_Antibiotic_substances_produced_by_Pseudomonas_aeruginosa; DOI:10.1016/S0021-9258(17)41580-8; pp.727–729, cultures and provisional Pyo naming; pp.730–732, assays and fractionation; pp.735–741, purification and physical characterization; pp.745–746, bacteriological scope | supports | Clinical cultures are designated P-SLU and P-CC; these are not identified as PAO1. P-SLU lost activity, and P-CC variants differed in pigment and Pyo production. Broth growth, solvent extraction, permutit fractionation and recrystallization yielded Pyo fractions. Chemical constitutions were not assigned in this paper. Much bacteriological work used crude extracts or Pyo II, so it cannot all be attributed to purified HHQ. Primary article text inspected through web extraction; original PDF and figure pixels not inspected. Direct free HTTP PDF and HTML requests returned 403. |
| H-WELLS1952 | https://www.researchgate.net/publication/10560858_Antibiotic_substances_produced_by_Pseudomonas_aeruginosa_syntheses_of_Pyo_Ib_Pyo_Ic_and_Pyo_III; DOI:10.1016/S0021-9258(18)55737-9; pp.331–332, direct relationship to Hays 1945 and structural conclusions; p.335, synthesis and comparison with authentic Pyo Ib | supports | Wells explicitly assigns Pyo Ib to 2-heptyl-4-quinolinol. Synthetic material melted at 146–147°C, did not depress the melting point of authentic Pyo Ib, and depressed that of Pyo Ic. The paper compares UV absorption of synthetic and authentic material and directly connects its natural Pyo samples to Hays 1945. 2-Heptyl-4-quinolinol is the lactim tautomer of the reviewed 2-heptylquinolin-4(1H)-one (HHQ); this name reconciliation is chemical interpretation of the explicit structure assignment. Primary article text inspected through web extraction; original PDF and figure pixels not inspected. |
| H-LUCKNER1965 | https://pubmed.ncbi.nlm.nih.gov/14291872/; DOI:10.1016/S0040-4039(01)83977-0; Bibliographic metadata only; exact primary content unavailable | unknown | Metadata identify the 1965 article, but the exact heptyl homologue, experimental strain and structure-identification methods could not be inspected. Publisher access returned HTTP 403. This is an incomplete citation check, not refutation of the LOTUS association. Metadata only. Publisher HTTP 403; DOI web open failed; PubMed open yielded browser challenge. No experimental full text inspected. |
| hhq-imodulon-search-scope | https://imodulondb.org/dataset.html?organism=p_aeruginosa&amp;dataset=precise364; Installed kg-microbe-sources read-only searches for pqs, phn and mvfR; imodulon-search-receipts.json and captured outputs | context_only | Bounded precise364 searches return component 85 MvfR/PQS signalling and the corresponding pqs and phnA/phnB genes. The mvfR query also returns component 15 LasR, annotated for pyochelin biosynthesis and secretion, which was not treated as exact-HHQ biosynthetic evidence. The phn query's component 70 PhnR-2 concerns phosphate/phosphonate transport context; it is not evidence for the similarly named anthranilate synthase genes. Original root search receipts, not a fresh search, were reused. |

## Limits And Additional Notes

- CHEBI:62219 exported SMILES fails RDKit, but its separately retrieved official default molfile parses and exactly matches the owner. Both ChEBI candidates share a tautomer-normalized Standard InChI/key; the fixed-H comparison resolves the represented form.
- The owner accurately retains the seeder collision flag. No current grounding override consumer is assumed: docs explicitly mark decisions.tsv as reserved. A future identifier migration requires implemented guarded ownership and reproduction support.
- NPAtlas official API was fully inspected through the web tool; direct download returned HTTP 403, so no full API-response hash is claimed.
- Protein sequence equivalence establishes native-reference identity only. PDB5DWZ variants, retained linkers, unmodeled residues and assembly interpretation are covered by the independent BGC reviewer.
- PqsA/PqsD/PqsE statements are audited as database annotations. Historical bibliography entries and the graph discussion of earlier access failures are not treated as newly inspected primary assays.
- The 1999 Ruta exact HHQ assignment remains unavailable at compound level despite a readable abstract and located public PDF; direct retrieval failed and screenshots did not expose image data to this session. This is not negative occurrence evidence.
- The 2017 and 2019 primary bodies, methods and structure-identification tables were inspected as full XML. Their chemical figure images were not obtained after bounded publisher/PMC attempts; no independent visual structure reconstruction is claimed.
- Broad antibacterial support is kept at its actual source tier. This review does not add quantitative assays, antimicrobial mechanisms or new producer claims.
- The two sibling links share a Standard InChIKey while their fixed-H tautomer graphs differ. Current SAME_INCHIKEY basis remains explicit.
- The already-open source-SMILES issue 822 was read, not changed. Fresh default-molfile evidence does not repair the malformed exported source string or implement a grounding migration.
- Primary source-preparation accesses are reused with original timestamps. Their full XML and relevant strain tables were rechecked for this owner; these are not claimed as fresh external downloads. New PDB and figure accesses have separate timestamped receipts.
- The 2021 PAO1 Copenhagen stock is identified by its primary strain table, not by an independently available genome sequence of that historical stock. The reference-locus bridge rests on PAO1 named genes and independently verified reference CDSs.
- The 2011 original pBBR-pqsABCD construction paper was identified but not inspected. No historical donor/plasmid sequence identity or complete-locus sufficiency is inferred from the 2016 engineered P. putida or 2021 complementation experiments.
- PqsBC main text, methods, tables and captions were inspected; its figure pixels and supplementary movie were not independently rendered. No new kinetic, cavity-geometry or stereochemical conclusion depends on those unviewed assets. The 2021 Figure 8 and Figure S4 images were independently rendered.
- Figure S4 has a primary-source caption/panel-order conflict: plotted HHQ is A although the caption calls it B. This is preserved in evidence and is not an error attributed to the owner record.
- PDB deposited sample sequences and modeled coverage were audited, not diffraction data, density maps or re-refinement. Deposited PISA tetramers and the paper's heterodimer interpretation do not settle physiological stoichiometry.
- The owner's October 11 primary-access limitations are dated historical curation notes. This review obtained the 2013 manuscript by an alternate public route; it does not rewrite the earlier retrieval history or treat that history as a current absence claim.
- precise411 remained unavailable through the previously used typed runner because regulator=NoneType failed parsing. Reused precise364 membership is coexpression context only, not independent biological proof.
- The 1965 citation remains individually unverified. A positive 1945/1952 bridge does not substitute for auditing that separate assertion.
- Accessible 1945/1952 material was extracted text. Garbled OCR formulas and tables were not used to derive precise quantitative activity, formula, or molecular-weight claims.
- No transfer of historical cultures to PAO1, Pyo II results to HHQ, or extract activity to purified HHQ is justified by this scoped review.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- No scientific owner, source inventory, graph, native status or curation history was edited. A saved partial scientific review does not promote SEEDED to REVIEWED.
- Native quality checks are reused from the identical tracked source revision, with their original timestamps and receipts. New strict validation was run for this exact target; saved-bundle checks follow persistence.
- The source-SMILES issue 822 and current multi-ChEBI collision flag remain open context. Valid official molfiles resolve the represented tautomer scientifically; a maintained guarded grounding consumer would be needed for a durable identifier migration.
- Optional historical documentation improvement: cite Wells 1952 alongside Hays 1945 to make the exact Pyo Ib/HHQ identity bridge visible. No occurrence correction is established for that historical association.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075346Z-2-heptylquinolin-4-1h-one
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'HHQ: exact tautomer, bounded PAO1 mechanism and occurrence provenance'
started_at: '2026-10-21T07:42:18.621186Z'
finished_at: '2026-10-21T07:53:46.213792Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Exact HHQ identity and five native PAO1 references are supported; both mechanism
  graphs preserve their evidence and construct limits. One major finding corrects
  PA14-to-PAO1 source-citation routing and omitted native methods. One minor finding
  identifies duplicate Ruta publication registrations. Historical 1945 occurrence
  is supported by a 1952 primary identity bridge; the 1965 citation and exact1999
  Ruta assignment remain unverified.
source:
  git_revision: 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: CLAUDE.md
    sha256: c783814c18591ea92aaa628fde98e6b0dbf1f59d45d240fe349682eec753e63f
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
    sha256: 4bc422b93002508b0abb86e0fa0afa49aff88745b5b0dd3bcbf351a68725d766
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: f87a4fa580dede966366bece28ccfb6542bdec4a0f810e40cdfc719811407a05
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: b27c2e61e696a285c38bc88c852dbbdc6c06fec8c4584343f2b9146462eea6cf
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml
    sha256: d5154364fae7512b92f31f1542e6ece4a85d07f99ffe7aefae65a5b3cc906288
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
    role: context
  - path: data/raw/antibioticmech_inchikeys.tsv
    sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
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
    sha256: 6873daace2f9e2225ef3d6830e993ac8cf8d01cec66b779fa5829309d77b3eaf
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
  - path: scripts/extract_lotus.py
    sha256: 8a8c524f60f85d2bb54412ca055a6a45e0d37ec5f4584d8d70be454b8f664290
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/lotus_exclusions.py
    sha256: 6352cac7c587eab5a56d907c523cc899d02d197009081624bf8649c675ee30f7
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: 'One entire owner and resolved mechanism: seven LOTUS triples, one
    producer/locus, two sibling links and all 19 nodes / 17 edges across two inline
    graphs, including provenance and history.'
  selection: Eleventh initially unreviewed path, first in batch 002 from fresh origin/main.
    The authoritative fresh-main list has 91 valid bundles covering 54 of 3,116 records;
    the ten separately validated reviews in pending PR 1000 bring campaign coverage
    to 64 paths before this review. All coverage inventories include ignored files.
    This bundle assesses exactly one target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-182e475a70
targets:
- target_id: naturalproductmech:mibig-182e475a70
  path: data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml
  label: 2-heptylquinolin-4(1H)-one
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: MIBiG source identity, producer and locus
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: LOTUS occurrence triples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: CyanoMetDB exact-structure occurrence source
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated owner transform
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned sibling linkage and activity-class inventory
checks:
- check_id: C-STRICT
  name: Closed-schema and component validation
  status: passed
  required: true
  summary: One complete owner and two inline graphs validated with zero ERROR rows.
  command: just validate-strict data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml
    --out /private/tmp/npm-review-work/011/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-182e475a70
  scope_note: Actual target check finished 2026-10-21T07:42:23.897784Z
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned
    filing pathways.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016808Z; finished 2026-10-21T06:37:52.997020Z. Exact
    session transcript: /private/tmp/npm-native-checks/verify-corpus.log. Reused for
    batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-182e475a70
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3,116 records are byte-identical to the seeder output from committed
    inventories and maintained curation inputs.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-reproduction
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016703Z; finished 2026-10-21T06:38:35.570687Z. Exact
    session transcript: /private/tmp/npm-native-checks/verify-reproduction.log. Reused
    for batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-182e475a70
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The documented exhaustive queue command produced 8,928 diagnostic rows
    in 12 queues; deterministic queue output does not establish scientific review.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just review-queue
    --tsv /private/tmp/npm-review-queue-initial.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016598Z; finished 2026-10-21T06:37:11.018366Z. Exact
    session transcript: /private/tmp/npm-native-checks/review-queue.log. Reused for
    batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-182e475a70
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'Full configured gate passed using existing CHEBI and GO caches plus the
    committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35
    documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because
    their prefixes have no adapter.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.498212Z; finished 2026-10-21T06:38:54.776253Z. Exact
    session transcript: /private/tmp/npm-native-checks/validate-products.log. Reused
    for batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-182e475a70
- check_id: shared-qc
  name: Full repository quality gate after environment repair
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed after installing the pinned
    linter, allowing the read-only governance fetch, and restoring the required provenance
    tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116
    records and zero errors. Documentation, provenance, source queue, governed artifacts,
    generated pages, reproduction, filing integrity and corpus reporting all passed.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:02.058886Z; finished 2026-10-21T06:54:53.950582Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt4.log. Reused for
    batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-182e475a70
- check_id: C-IDENTITY-PROTEIN
  name: Exact chemical and native protein reference audit
  status: passed
  required: true
  summary: Owner SMILES/InChI/key agree; default ChEBI molfiles distinguish the tautomers.
    Five full native CDS translations equal independent GenPept and UniProt sequences.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - E-CHEMISTRY-IDENTITY
  - E-CHEBI-TAUTOMER-COMPARISON
  - E-PROTEIN-EQUIVALENCE
- check_id: C-RUTA-PRIMARY
  name: Exact compound assignment in the1999 Ruta primary
  status: unavailable
  required: true
  summary: Publisher abstract is readable but does not specify the heptyl member.
    The located public PDF did not provide readable body or image data through the
    attempted routes.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - R-RUTA-ACCESS
  - R-RUTA-SEARCH
- check_id: C-GRAPHS
  name: Complete bounded reaction and annotation graphs
  status: passed
  required: true
  summary: All19 nodes and 17 edges were audited across PAO1 PqsBC primary assays,
    exact native references and explicitly database-level PqsA/D/E annotations. Construct,
    net-conversion and essentiality limits are preserved.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - hhq-primary2016-pqsbc-assay
  - hhq-pdb5dwz-construct
  - E-PQSA-UNIPROT
  - E-PQSD-UNIPROT
  - E-PQSE-UNIPROT
- check_id: historical-hhQ-hays-wells-primary-bridge
  name: Historical P. aeruginosa HHQ occurrence identity bridge
  status: passed
  required: true
  summary: Hays 1945 isolation plus Wells 1952 synthetic/authentic comparison establish
    the Pyo Ib–HHQ identity bridge.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  scope_note: Primary extracted text inspected; OCR numerical tables and figure pixels
    were not used for new quantitative conclusions.
  evidence_ids:
  - H-HAYS1945
  - H-WELLS1952
- check_id: historical-hhQ-luckner1965-primary
  name: Exact-compound support in Luckner and Ritter 1965
  status: unavailable
  required: true
  summary: Publisher access returned HTTP 403 and no readable primary experimental
    text was obtained. Exact homologue and methods remain unknown.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  scope_note: Required citation-level review is incomplete. This is an access limitation,
    not a negative scientific finding.
  evidence_ids:
  - H-LUCKNER1965
- check_id: imodulondb-precise364-context
  name: Bounded iModulonDB component and dataset context audit
  status: passed
  required: false
  summary: Relevant component 85 membership and dataset species/strain context were
    inspected using the installed runner and the primary dataset publication. Coexpression
    was kept separate from biosynthetic causality.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  command: PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 25 summarize --organism p_aeruginosa --dataset precise364
    --k 85 --limit 100
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - hhq-imodulon-component85-context
  - hhq-imodulon-dataset-strain-context
  scope_note: Read-only runner; working directory was the isolated review checkout.
    No code edits, dependency synchronization or corpus mutation. Reused actual execution
    for the same PAO1 pqs genes and unchanged runner/source; no new run is claimed.
- check_id: imodulondb-precise411-context
  name: precise411 searches through installed source runner
  status: failed
  required: false
  summary: The optional search command ran and exited 2 on typed regulator=NoneType
    parsing; relevant dataset contents remained unavailable. No biological absence
    conclusion.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 25 search --organism p_aeruginosa --dataset precise411 --query
    pqs
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - hhq-imodulon-precise411-unavailable
  scope_note: Original root command receipt reused; phn and mvfR queries failed with
    the same typed error. No runner changes were attempted. Reused actual execution
    for the same PAO1 pqs genes and unchanged runner/source; no new run is claimed.
evidence:
- evidence_id: E-IDENTITY-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml
  locator: Complete owner and identical resolved record; chemical_structure, xrefs,
    source_concepts, grounding fields, both inline graphs and discussions
  accessed_at: '2026-10-21T07:47:37.057434Z'
  support: supports
  summary: The full owner represents achiral neutral HHQ as the quinolin-4(1H)-one
    graph, C16H21NO and key UYRHHBXYXSYGHA-UHFFFAOYSA-N. Its source concept is BGC0000922:3
    and the stored minted identifier equals the seeder hash of that exact source key.
    The record explicitly retains REVIEW_NEEDED for two ChEBI candidates and distinguishes
    all five native PAO1 protein references from experimental constructs.
  snapshot_sha256: d5154364fae7512b92f31f1542e6ece4a85d07f99ffe7aefae65a5b3cc906288
- evidence_id: E-CHEMISTRY-IDENTITY
  kind: validation
  reference: /private/tmp/npm-review-work/011/chemistry.json
  locator: Pinned RDKit result for complete owner SMILES
  accessed_at: '2026-10-21T07:42:20.674341Z'
  support: supports
  summary: The owner SMILES regenerates the stored complete InChI/key and neutral
    formula C16H21NO, exact mass 243.162314292; there are no stereocenters. Its stereo_complete=true
    is appropriate for this achiral graph.
  snapshot_sha256: 649328991794f00bf60baca2eeb399a3537210f1e5fef86e4a5df75fb3b9116f
- evidence_id: E-NPATLAS
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA026460?include=classifications
  locator: 'Official current JSON: npaid, original_name, full smiles/inchi/inchikey,
    origin_reference, current mol_structures and reassignments'
  accessed_at: '2026-10-21T07:43:37Z'
  support: supports
  summary: NPA026460 is C16H21NO with the same complete InChI/key and quinolone SMILES
    CCCCCCCC1=CC(=O)C2=CC=CC=C2[NH]1. Its original name is 2-n-heptyl-4-hydroxyquinoline,
    but the displayed current graph is exactly the owner quinolone; reassignments
    is empty. Its origin reference is DOI:10.3390/md17020133, PMID:30813382, Streptomyces
    sp. MBTG13. The source was inspected through the official web API; direct file
    download returned HTTP 403, so no full-response checksum is claimed.
- evidence_id: E-CHEBI-62219
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/62219/
  locator: Current default structure, full chemical identity and explicit tautomer
    relation; reused source preparation
  accessed_at: '2026-10-21T07:27:37.833867Z'
  support: supports
  summary: Current CHEBI:62219 is three-star 2-heptyl-4-quinolone, IUPAC 2-heptylquinolin-4(1H)-one;
    neutral C16H21NO. Its default full InChI gives UYRHHBXYXSYGHA-UHFFFAOYSA-N and
    a quinolin-4(1H)-one with a C7 heptyl substituent at C2. The default SMILES is
    not parseable by RDKit because it lacks the needed aromatic [nH]; the InChI parses
    and generates CCCCCCCc1cc(=O)c2ccccc2[nH]1. This is a database representation
    observation, not a target-record finding.
  snapshot_sha256: bbc81625aee04b914c61fab49426dd38d4949c4b721af57c277149cad1431bcd
- evidence_id: E-CHEBI-75306
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/75306/
  locator: Current default structure, full chemical identity and explicit tautomer
    relation; reused source preparation
  accessed_at: '2026-10-21T07:28:25.933145Z'
  support: supports
  summary: CHEBI:75306 is the separate three-star 2-heptyl-4-hydroxyquinoline entry.
    Both ChEBI records explicitly assert the tautomer relation and share the Standard
    InChI/key. Its aromatic hydroxyl SMILES parses. Standard InChIKey equality alone
    cannot select the represented tautomer; the separately inspected official default
    molfiles provide that distinction.
  snapshot_sha256: 906fb63bde8c983bc5f57a404fae6d8e1081f3c08c050a308d93619bae27ccd0
- evidence_id: E-PUBCHEM
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/UYRHHBXYXSYGHA-UHFFFAOYSA-N/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: 'Complete full-key property JSON: PubChem CID, InChI, InChIKey, molecular
    formula and SMILES'
  accessed_at: '2026-10-21T07:28:25.630653Z'
  support: supports
  summary: The full-key query resolves to PubChem CID164974, C16H21NO, with the same
    complete Standard InChI/key. PubChem SMILES CCCCCCCC1=CC(=O)C2=CC=CC=C2N1 independently
    yields that key and formula; there are no stereocenters. The nonaromatic ring
    carbon after seven side-chain carbons is part of the ring, not an eighth side-chain
    carbon.
  snapshot_sha256: 181c5b199ce8d495a1787406020ee47c1ac7a53226c10e0d934900470291792c
- evidence_id: E-CHEBI-MOL-62219
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/62219/
  locator: Official default-structure molfile, complete atom/bond representation
  accessed_at: '2026-10-21T07:45:06.324988Z'
  support: supports
  summary: The current official default molfile for CHEBI:62219 is parseable. It is
    the neutral quinolin-4(1H)-one graph represented by the owner.
  snapshot_sha256: fa658c74e71e3f1b1ef96eba294ac60f1bbfea5e405031d3a90957c00aa3455c
- evidence_id: E-CHEBI-MOL-75306
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/75306/
  locator: Official default-structure molfile, complete atom/bond representation
  accessed_at: '2026-10-21T07:45:06.325307Z'
  support: supports
  summary: The current official default molfile for CHEBI:75306 is parseable. It is
    the neutral 4-hydroxyquinoline tautomer, with a different fixed hydrogen position
    and bond graph from the owner.
  snapshot_sha256: f328e1840cace96b3eb23ff275bf70e5fda628f4f1932784fcd0b0e5c8832fb5
- evidence_id: E-CHEBI-TAUTOMER-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/011/chebi-mol-comparison.json
  locator: Complete canonical graph and fixed-H InChI comparison of owner against
    both official default molfiles
  accessed_at: '2026-10-21T07:45:18.188389Z'
  support: supports
  summary: CHEBI:62219 default MOL canonicalizes to owner CCCCCCCc1cc(=O)c2ccccc2[nH]1
    and fixed-H InChI ending /f/h17H. CHEBI:75306 gives CCCCCCCc1cc(O)c2ccccc2n1 and
    /f/h18H. Both retain the same Standard InChI/key; this is a tautomer collision,
    not a compound/zwitterion pair. The malformed ChEBI62219 SMILES does not prevent
    comparison of its valid official default MOL.
  snapshot_sha256: aa4aa66f06970be917f4fda6327d8da152bbdb4753734042698a70c662aa50ba
- evidence_id: E-GROUNDING-INVENTORY
  kind: record_content
  reference: data/raw/chebi_structures.tsv
  locator: Exact-key rows CHEBI:62219 and CHEBI:75306
  accessed_at: '2026-10-21T07:47:37.057434Z'
  support: supports
  summary: Both pinned three-star rows share key UYRHHBXYXSYGHA-UHFFFAOYSA-N. Their
    definitions distinguish the quinolone from 4-hydroxyquinoline; the former exported
    SMILES is malformed while the latter is valid. Current default molfiles resolve
    which represented tautomer matches the owner.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: E-GROUNDING-IMPLEMENTATION
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: mint_identifier lines284-292; chebi_by_key construction and multi-match
    grounding branch lines881-889 and955-978
  accessed_at: '2026-10-21T07:47:37.057434Z'
  support: supports
  summary: 'The implemented seeder uses full-key collision count: multiple three-star
    matches stay minted with REVIEW_NEEDED. The owner accurately reproduces this rule.
    The generated note uses a generic compound/zwitterion example, whereas this exact
    pair are neutral tautomers. No candidate-level molfile decision is made in this
    branch.'
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: E-GROUNDING-OWNERSHIP
  kind: record_content
  reference: docs/CURATION.md
  locator: The decision file, especially lines17-21; supported MIBiG structure-correction
    actions
  accessed_at: '2026-10-21T07:47:37.057434Z'
  support: supports
  summary: The documentation explicitly says curation/decisions.tsv is reserved and
    not consumed. Existing structure corrections require an unambiguous destination
    and do not supply a same-key candidate-choice mechanism. A future exact-tautomer
    grounding change requires an implemented, tested consumer and guarded migration
    rather than merely adding a reserved decision row or hand-editing generated YAML.
  snapshot_sha256: 6873daace2f9e2225ef3d6830e993ac8cf8d01cec66b779fa5829309d77b3eaf
- evidence_id: E-GROUNDING-CONSUMER-SEARCH
  kind: search
  reference: scripts/seed_from_sources.py; src; tests; conf; curation; .claude; docs
  locator: rg --no-ignore --hidden grounding/override/load-decisions/decisions.tsv
    queries
  accessed_at: '2026-10-21T07:45:49Z'
  support: context_only
  summary: The bounded maintained-source search found the documented reserved decisions
    format and references, but no implemented grounding-decision loader in the searched
    code. Direct seeder and ownership documentation reads establish the current effective
    behavior.
  search_scope: Searched scripts, src, tests, conf, curation, .claude and docs with
    rg --no-ignore --hidden, including ignored files in those directories, for grounding.*overrid,
    overrid.*grounding, load.*decisions and decisions.tsv. This is a bounded repository-code
    search, not an exhaustive claim about external tools or all Git objects.
- evidence_id: E-HHQ-PRIMARY-IDENTITY
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC337054/
  locator: DOI:10.1073/pnas.0307694100; Fig2 SeriesA C7H15/HHQ, Fig4 and methods;
    complete HTML and figure read
  accessed_at: '2026-10-21T07:28:25.555296Z'
  support: supports
  summary: The primary chemical figure explicitly labels the C7H15 member of SeriesA
    as HHQ, [M+H]+244, while PQS and HQNO are separately labelled compounds. The drawing
    uses the hydroxy tautomer. Native PA14 culture data establish HHQ identity and
    natural occurrence; they do not independently establish any one of the seven owner
    LOTUS citations or native PAO1 locus evidence.
  snapshot_sha256: e48d0601463a084c3dbe6f809159053369cdb712e0b6b7ee93dc366a0430f7c2
- evidence_id: E-PQSA-UNIPROT
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9I4X3.json
  locator: entryAudit, organism, genes, sequence, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT
    and EMBL reference
  accessed_at: '2026-10-21T07:43:36.063920Z'
  support: supports
  summary: Reviewed Q9I4X3, version 115, is PAO1 taxon 208964 pqsa/PA0996, 517 aa,
    linked to AAG04385.1. Current FUNCTION/CATALYTIC ACTIVITY support anthranilate
    + ATP + CoA yielding anthraniloyl-CoA, AMP and diphosphate (RHEA:10828).
  snapshot_sha256: 1ebb2455a36a95facf51c5b0cb407d258376a360accea76c6a73ce5185f704eb
- evidence_id: E-PQSA-GENPEPT
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AAG04385.1&db=protein&report=genpept&retmode=text
  locator: LOCUS, organism/source taxon, gene/locus_tag, coded_by, translation table
    and complete ORIGIN
  accessed_at: '2026-10-21T07:43:36.905020Z'
  support: supports
  summary: AAG04385.1 is native PAO1 pqsa/PA0996, taxon 208964, 517 aa, coded by AE004091.2:1078462..1080015
    on the plus strand, translation table 11. Its full sequence agrees exactly with
    independently translated genomic DNA and UniProt.
  snapshot_sha256: ea2660efe3f06266daf81a39574ff977e6139185e3eb97fa94182c3854d1da26
- evidence_id: E-PQSB-UNIPROT
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9I4X2.json
  locator: entryAudit, organism, genes, sequence, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT
    and EMBL reference
  accessed_at: '2026-10-21T07:43:36.061743Z'
  support: supports
  summary: Reviewed Q9I4X2, version 108, is PAO1 taxon 208964 pqsb/PA0997, 283 aa,
    linked to AAG04386.1. Current FUNCTION/SUBUNIT describe association with PqsC
    and probably a folding role rather than independent PqsB catalysis. The owner
    does not adopt broader ring-closure language as an elementary reaction assignment.
  snapshot_sha256: 5c22bd87148d57249370c71018cb73416a362f76b60a76a6951116cf958f0649
- evidence_id: E-PQSB-GENPEPT
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AAG04386.1&db=protein&report=genpept&retmode=text
  locator: LOCUS, organism/source taxon, gene/locus_tag, coded_by, translation table
    and complete ORIGIN
  accessed_at: '2026-10-21T07:43:36.951592Z'
  support: supports
  summary: AAG04386.1 is native PAO1 pqsb/PA0997, taxon 208964, 283 aa, coded by AE004091.2:1080009..1080860
    on the plus strand, translation table 11. Its full sequence agrees exactly with
    independently translated genomic DNA and UniProt.
  snapshot_sha256: e7e6cb9f471dd6386da8e768129b17a4dc90a7cfc078e24522f62fc376562bbc
- evidence_id: E-PQSC-UNIPROT
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9I4X1.json
  locator: entryAudit, organism, genes, sequence, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT
    and EMBL reference
  accessed_at: '2026-10-21T07:43:36.063721Z'
  support: supports
  summary: Reviewed Q9I4X1, version 132, is PAO1 taxon 208964 pqsc/PA0998, 348 aa,
    linked to AAG04387.1. Current FUNCTION/SUBUNIT and RHEA:50396 describe the PqsBC
    complex and net HHQ production. The accession is the wild-type native reference,
    not the C129A crystal or tagged assay construct.
  snapshot_sha256: 813928f4837dc1a6d7cff3cf341f8476422a9621b1ad86ad46852ed2132ef7f6
- evidence_id: E-PQSC-GENPEPT
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AAG04387.1&db=protein&report=genpept&retmode=text
  locator: LOCUS, organism/source taxon, gene/locus_tag, coded_by, translation table
    and complete ORIGIN
  accessed_at: '2026-10-21T07:43:36.952034Z'
  support: supports
  summary: AAG04387.1 is native PAO1 pqsc/PA0998, taxon 208964, 348 aa, coded by AE004091.2:1080853..1081899
    on the plus strand, translation table 11. Its full sequence agrees exactly with
    independently translated genomic DNA and UniProt.
  snapshot_sha256: 90088c3c9ab2f5f2ce5a0b8fb226f32adc8ecc0fb6ce1eb4f108b62cc5ebb48c
- evidence_id: E-PQSD-UNIPROT
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P20582.json
  locator: entryAudit, organism, genes, sequence, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT
    and EMBL reference
  accessed_at: '2026-10-21T07:43:36.064045Z'
  support: supports
  summary: Reviewed P20582, version 147, is PAO1 taxon 208964 pqsd/PA0999, 337 aa,
    linked to AAG04388.1. Current FUNCTION/CATALYTIC ACTIVITY support anthraniloyl-CoA
    plus malonyl-CoA yielding 2-ABA-CoA with CoA and carbon dioxide (RHEA:50472).
    DHQ is a separate spontaneous product discussed in the source and is not asserted
    as HHQ in the owner.
  snapshot_sha256: c2e406c8c1ca5b03aa16d0f0a6090e2a69d7b03c6fb2cc55c8bfcc0f1dc4840c
- evidence_id: E-PQSD-GENPEPT
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AAG04388.1&db=protein&report=genpept&retmode=text
  locator: LOCUS, organism/source taxon, gene/locus_tag, coded_by, translation table
    and complete ORIGIN
  accessed_at: '2026-10-21T07:43:37.824133Z'
  support: supports
  summary: AAG04388.1 is native PAO1 pqsd/PA0999, taxon 208964, 337 aa, coded by AE004091.2:1081942..1082955
    on the plus strand, translation table 11. Its full sequence agrees exactly with
    independently translated genomic DNA and UniProt.
  snapshot_sha256: 3aedb126c61de93c027cafa269db4bb0c5150756f04533ae7e1a741a8e904f4f
- evidence_id: E-PQSE-UNIPROT
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P20581.json
  locator: entryAudit, organism, genes, sequence, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT
    and EMBL reference
  accessed_at: '2026-10-21T07:43:36.817031Z'
  support: supports
  summary: Reviewed P20581, version 129, is PAO1 taxon 208964 pqse/PA1000, 301 aa,
    linked to AAG04389.1. Current FUNCTION/CATALYTIC ACTIVITY support 2-ABA-CoA hydrolysis
    to 2-ABA and CoA (RHEA:49444). The owner does not import the broader PA14 RhlR
    regulatory annotations or claim PqsE is physiologically indispensable.
  snapshot_sha256: ae733337c1170cfa8ebfc69f58a961ac21529189a4beaa97fe5a1d099689aed7
- evidence_id: E-PQSE-GENPEPT
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AAG04389.1&db=protein&report=genpept&retmode=text
  locator: LOCUS, organism/source taxon, gene/locus_tag, coded_by, translation table
    and complete ORIGIN
  accessed_at: '2026-10-21T07:43:37.888776Z'
  support: supports
  summary: AAG04389.1 is native PAO1 pqse/PA1000, taxon 208964, 301 aa, coded by AE004091.2:1082949..1083854
    on the plus strand, translation table 11. Its full sequence agrees exactly with
    independently translated genomic DNA and UniProt.
  snapshot_sha256: d296109da195d41b0c5d385865feda831578f11d66c710dde2bc320791b0a461
- evidence_id: E-PAO1-GENOME
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AE004091.2&db=nuccore&report=genbank&retmode=text&from=1073960&to=1087095
  locator: AE004091.2 slice 1073960..1087095; five complete CDS features, deposited
    translations and ORIGIN
  accessed_at: '2026-10-21T07:17:15.132327Z'
  support: supports
  summary: Reused the previously fetched official PAO1 interval, 13,136 nt. Complete
    pqsA-E CDS features encode AAG04385.1 through AAG04389.1, each with codon_start
    1 and translation table 11. Absolute coordinates were reconstructed from slice
    offset and independently agree with GenPept coded_by.
  snapshot_sha256: 330511e0ab7b1880d773dcf8f12963ad08388969aac89c63854fdd87c7fe012f
- evidence_id: E-PROTEIN-EQUIVALENCE
  kind: validation
  reference: /private/tmp/npm-review-work/011/protein-equivalence.json
  locator: Independent table 11 translation of each complete genomic CDS and comparisons
    to deposited CDS, GenPept and UniProt
  accessed_at: '2026-10-21T07:44:24.758548Z'
  support: supports
  summary: 'All five comparisons are exact at every residue: PqsA 517 aa (1554nt,
    ATG/TGA); PqsB 283 aa (852nt, ATG/TAA); PqsC 348 aa (1047nt, ATG/TGA); PqsD 337
    aa (1014nt, ATG/TGA); PqsE 301 aa (906nt, ATG/TGA). All five have taxon 208964,
    the expected PA0996-PA1000 loci and no internal stop codons. The result records
    nucleotide/protein SHA256 values and confirms all three owner UniProt snippets
    literally occur in the cited current records.'
  snapshot_sha256: 4ce13d9add95a93390e8b4bd69394688a119c021e1609d909e9d40c31453ac16
- evidence_id: R-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml
  locator: Entire owner and read_natural_product resolved view; exact-key inventories,
    source concepts, classifications, all 19 nodes and 17 edges, discussions and history
  accessed_at: '2026-10-21T07:52:19.541932Z'
  support: supports
  summary: Seven LOTUS structure/taxon/reference triples remain occurrence assertions,
    distinct from one PAO1 producer and locus. The two inline graphs contain 19 nodes
    and 17 edges. NPClassifier values match the exact-key inventory; MIBiG classes
    remain separately asserted. Two seed and two bounded mechanism curation events
    coexist with SEEDED status. No external components, separate pathway steps, molecular-target
    entries or quantitative activity assertions occur in the complete resolved owner.
  snapshot_sha256: d5154364fae7512b92f31f1542e6ece4a85d07f99ffe7aefae65a5b3cc906288
- evidence_id: R-HAPLOPHYLLUM-PRIMARY
  kind: primary_source
  reference: https://www.researchgate.net/profile/Luc-Angenot/publication/244500675_Alkaloids_from_Haplophyllum_leptomerum/links/581471ed08ae90acb23bfdaa/Alkaloids-from-Haplophyllum-leptomerum.pdf
  locator: DOI:10.1007/s10600-010-9661-y, pp 502-503; full author-uploaded article
    text inspected through its publication page and extracted PDF text
  accessed_at: '2026-10-21T07:48:42Z'
  support: supports
  summary: Compound 6 is 2-heptylquinolin-4-one, isolated as 13 mg from the aerial
    parts of Haplophyllum leptomerum collected in the Babataga Mountains in May 2008.
    Proton NMR and comparison with a synthetic sample support its identity. This establishes
    plant occurrence; the separate root isolates and dictamnine anticancer results
    do not apply to HHQ.
- evidence_id: R-HAPLOPHYLLUM-TAXON
  kind: authority
  reference: https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:771290-1
  locator: Kew POWO accepted name and complete synonym list
  accessed_at: '2026-10-21T07:48:42Z'
  support: supports
  summary: POWO accepts Haplophyllum griffithianum and explicitly lists H. leptomerum
    as a heterotypic synonym. Thus the primary paper name and recorded occurrence
    name are compatible; this is not a species-scope mismatch.
- evidence_id: R-STREPTOMYCES
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=6410270&retmode=xml
  locator: DOI:10.3390/md17020133; PMID:30813382; Results 2.1-2.3, Methods 4.2-4.3,
    Table 1
  accessed_at: '2026-10-21T07:47:53.629959Z'
  support: supports
  summary: The primary article isolates compound 1, explicitly 2-n-heptyl-4-hydroxyquinoline,
    from a six-week rice culture of Streptomyces sp. MBTG13. Its NMR/UV identity is
    separated from the N-oxide, octyl and dione congeners. The organism is retained
    at genus level despite 99% 16S identity to a named species. Purified compound
    1 has bacterial MIC measurements, independently supporting the broad ANTIBACTERIAL
    summary. No Candida growth-inhibition or direct Efg1-binding claim follows from
    the separate hyphal-response results.
  snapshot_sha256: a3542466411e071b82f79cd62c2188f62a8182ec8d3e286b6e383fd607243c00
- evidence_id: R-PSEUDANE
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5706026&retmode=xml
  locator: DOI:10.3390/md15110336; PMID:29104209; Results 2.1-2.2, Table 1, Methods
    4.2-4.4
  accessed_at: '2026-10-21T07:47:52.626040Z'
  support: supports
  summary: Pseudane-VII is isolated from Pseudoalteromonas sp. M2 culture supernatant.
    The main compound is checked against a standard, purified (11.37 mg), and analyzed
    by proton/carbon NMR. Its [M+H]+244.1695, six side-chain methylenes and terminal
    methyl distinguish the heptyl congener from adjacent pseudanes. The source calls
    the family 4-hydroxy-2-alkylquinolines; ChEBI independently supplies the pseudan
    VII synonym for the matching HHQ tautomer. This supports the conservative genus-level
    occurrence. Adjacent peaks described as tentative are not substituted for the
    isolated principal compound.
  snapshot_sha256: 58860745947d6e77c2007d85dd8da7126f2c367529fb6285d2a38aa1ca24d1d1
- evidence_id: R-TAXON-PROVENANCE
  kind: authority
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q18080097%7CQ1144013%7CQ31856%7CQ25062%7CQ842207&props=labels%7Cclaims&languages=en&format=json
  locator: Official entity labels and complete P685 claims for all five unique provenance
    URIs
  accessed_at: '2026-10-21T07:47:52.990128Z'
  support: supports
  summary: Q18080097 maps to Haplophyllum griffithianum/1006075; Q1144013 to Streptomyces/1883;
    Q31856 to Pseudomonas aeruginosa/287; Q25062 to Ruta graveolens/37565; Q842207
    to Pseudoalteromonas/53246. These match the recorded taxonomy identifiers and
    preserve genus versus species scope.
  snapshot_sha256: 8818f278f571c18dba07593c67001147637d9151414215714e8932a465faba6e
- evidence_id: R-RUTA-DOI1
  kind: authority
  reference: https://api.crossref.org/works/10.1007%2FPL00010251
  locator: Crossref complete metadata for DOI:10.1007/PL00010251
  accessed_at: '2026-10-21T07:47:53.080992Z'
  support: supports
  summary: The deposited article has English and German titles, four authors Kostova/Ivanova/Mikhova/Klaiber,
    volume 130 issue 5, pages 703-707 and May 1999 date. Its alternative identifier
    is91300703. Metadata establish the publication, not its individual compound inventory.
  snapshot_sha256: 81ee280fbfc03c9ccb85161697c6d45444eedb8ce6d6d68533cbefc7bd3639f8
- evidence_id: R-RUTA-DOI2
  kind: authority
  reference: https://api.crossref.org/works/10.1007%2FS007060050230
  locator: Crossref complete metadata for DOI:10.1007/S007060050230
  accessed_at: '2026-10-21T07:47:53.381988Z'
  support: supports
  summary: The older DOI has the same German title, four authors, volume 130 issue
    5 and page 703 in 1999; its original publisher URL ends91300703.htm. Together
    with the newer record this identifies duplicate DOI registrations for the same
    article, not independent occurrence experiments.
  snapshot_sha256: 93b61da9d7187f5b7bc5d4ab4cb2f102ae4478a4ebbecfd19f841d45a61a2730
- evidence_id: R-RUTA-ACCESS
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/PL00010251
  locator: Complete publisher abstract and metadata; author-uploaded PDF acquisition
    also attempted
  accessed_at: '2026-10-21T07:49:18.057909Z'
  support: partial
  summary: The primary abstract reports four new quinolone homologues and thirteen
    known components from Bulgarian-grown Ruta graveolens, but does not name individual
    homologues. The author-uploaded five-page PDF is discoverable; direct retrieval
    returned HTTP 403, extracted text was empty, and screenshot tools returned placeholders
    without inspectable image data. The publisher PDF URL returned HTML rather than
    PDF. Exact HHQ attribution in this 1999 article remains unverified. Search-result
    snippets from later papers were not treated as its primary body.
- evidence_id: R-RUTA-SEARCH
  kind: search
  reference: https://www.researchgate.net/publication/225245803_Alkaloids_and_Coumarins_from_Ruta_graveolens
  locator: Bounded public-source retrieval and web queries
  accessed_at: '2026-10-21T07:49:18.057909Z'
  support: unknown
  summary: The publisher preview and author-uploaded file were located; no readable
    compound-level 1999 text was obtained in these attempts. Later primary and secondary
    references are useful leads but do not resolve what was actually assigned in the
    cited paper.
  search_scope: 'Queries: exact title plus heptyl, exact DOI plus pdf; Springer article/PDF,
    ResearchGate author-uploaded PDF and five-page screenshot attempts. Scope is these
    public endpoints, not an assertion of global unavailability.'
- evidence_id: R-SIBLING-QUINOLONE
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml
  locator: Entire exact pinned AntibioticMech YAML at commit74f6cc8362498900f2fe2c13d0b6fdb66dd30976
  accessed_at: '2026-10-21T07:49:18.097412Z'
  support: supports
  summary: The pinned sibling identifier, label, full Standard InChIKey and ANTIBACTERIAL
    class agree with the generated link and activity summary. The quinolone and hydroxyquinoline
    siblings preserve separate ChEBI concepts with a shared tautomer-normalized key.
    These are seeded activity-role assertions without quantitative mechanism claims;
    SAME_INCHIKEY does not establish fixed-H graph identity.
  snapshot_sha256: 821a5ddb81a01d413df4f447de50280acef38aa07bc9104b37c68ef4caff881f
- evidence_id: R-SIBLING-HYDROXY
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml
  locator: Entire exact pinned AntibioticMech YAML at commit74f6cc8362498900f2fe2c13d0b6fdb66dd30976
  accessed_at: '2026-10-21T07:49:18.092121Z'
  support: supports
  summary: The pinned sibling identifier, label, full Standard InChIKey and ANTIBACTERIAL
    class agree with the generated link and activity summary. The quinolone and hydroxyquinoline
    siblings preserve separate ChEBI concepts with a shared tautomer-normalized key.
    These are seeded activity-role assertions without quantitative mechanism claims;
    SAME_INCHIKEY does not establish fixed-H graph identity.
  snapshot_sha256: 3a1ee029ce91ccbd693c5359a2b949894199e9cc3103ed3f8f1edeea96ca2eda
- evidence_id: R-SIBLING-INVENTORY
  kind: record_content
  reference: data/raw/antibioticmech_inchikeys.tsv
  locator: Complete TSV parsed; exact full-key rows and MANIFEST pin; seeder full-key
    join
  accessed_at: '2026-10-21T07:52:19.541932Z'
  support: supports
  summary: Both matching sibling rows carry the exact inspected commit and identifiers.
    The seeder faithfully emits SAME_STRUCTURE with basis SAME_INCHIKEY and derives
    ANTIBACTERIAL from the pinned sibling class. This is the repository-defined Standard
    InChIKey relation, not a claim that the two fixed-H tautomer drawings are identical.
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
- evidence_id: R-RUTA-TRANSFORM
  kind: record_content
  reference: scripts/extract_lotus.py
  locator: extract_rows exact (key, organism, DOI) signature; seeder LOTUS loop emits
    one occurrence for each retained triple
  accessed_at: '2026-10-21T07:52:19.541932Z'
  support: supports
  summary: The existing extractor deduplicates identical DOI strings, so the two bibliographic
    aliases survive as distinct triples and the seeder emits two otherwise identical
    Ruta occurrences. No source-row deletion is needed to document that these refer
    to one publication.
  snapshot_sha256: 8a8c524f60f85d2bb54412ca055a6a45e0d37ec5f4584d8d70be454b8f664290
- evidence_id: R-ISSUE822
  kind: prior_review
  reference: https://github.com/CultureBotAI/NaturalProductMech/issues/822
  locator: Read-only gh issue view822; full title, body and OPEN state
  accessed_at: '2026-10-21T07:50:13Z'
  support: supports
  summary: The explicitly linked historical issue concerns the unparsable CHEBI62219
    exported SMILES, while affirming the valid MIBiG owner and preserving the tautomer
    ambiguity. Current source inspection confirms the same exported-string defect
    and provides a valid default molfile. This review neither closes that issue nor
    treats it as a validated structured predecessor.
- evidence_id: hhq-source922-compound3
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000922.5/annotations.json
  locator: 'Version 5 complete entry: compounds[2] (one-based compound_index 3), taxonomy,
    loci and biosynthesis; original /010/mibig922.json reused'
  accessed_at: '2026-10-21T07:17:15Z'
  support: supports
  summary: Exact HHQ is compound 3, distinct from compound 1 PQS and compound 2 dihydroxyquinoline.
    Its structure is C16H21NO with the owner StandardInChIKey UYRHHBXYXSYGHA-UHFFFAOYSA-N.
    The source records PAO1 taxon 208964, AE004091.2:1073960..1087095 and PKS/Type
    III, with no locus methods. Its mass-spectrometry compound-identification citation
    is DOI:10.1016/j.chembiol.2013.09.021. Source quality is questionable and completeness
    unknown. The original external access time is retained; applicability to the full
    011 owner and exact source row was checked on 2026-10-21 at 07:43:16Z.
- evidence_id: hhq-pao1-locus-reference
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AE004091.2&db=nuccore&report=genbank&retmode=text&from=1073960&to=1087095
  locator: Complete source and CDS annotations in /010/ae004091-bgc.gb; same accession
    and bounds as 011
  accessed_at: '2026-10-21T07:17:15Z'
  support: supports
  summary: This PAO1 reference interval includes pqsABCDE (PA0996-PA1000), phnAB (PA1001/PA1002)
    and mvfR (PA1003), together with upstream genes. It bridges the named pqsA and
    PqsBC experiments to the represented locus. Unlinked pqsH is not within these
    bounds and consumes HHQ in PQS formation. Reference annotation does not sequence-verify
    the historical Copenhagen stock or prove sufficiency of every base in the bounded
    interval. Original external access retained; record applicability checked afresh.
- evidence_id: hhq-primary2013-strain-scope
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3877684&retmode=xml
  locator: DOI:10.1016/j.chembiol.2013.09.021 / PMID:24239007; full primary XML, Table
    1 and Methods P44/P51/P57; Figure 3 and Figure 5b
  accessed_at: '2026-10-21T07:26:38Z'
  support: partial
  summary: The native Pseudomonas strains in Table 1 are PA14 and its derivatives.
    Native genetics, isotope incorporation and product measurements concern that lineage.
    The tagged PqsC construct is explicitly amplified from PA14; PqsB comes through
    a supplied pMSR1 construct whose original template is not independently sequenced
    here. The paper establishes exact HHQ formation, including copurified PqsBC plus
    2-ABA and octanoyl-CoA, but is not direct PAO1 native experimentation. Figure
    3 totals HAQs rather than providing an isolated HHQ endpoint. This is legitimate
    compound evidence whose unqualified routing to a PAO1 strain/locus claim exceeds
    its inspected experimental scope.
- evidence_id: hhq-primary2016-pqsbc-assay
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=4807248&retmode=xml
  locator: DOI:10.1074/jbc.M115.708453 / PMID:26811339; Experimental Procedures, Expression
    and Purification, Enzyme Activity Assays; Results and Figure 7 caption
  accessed_at: '2026-10-21T07:26:38Z'
  support: supports
  summary: The study explicitly clones PAO1 pqsB/pqsC into a sequence-verified expression
    plasmid. PqsC has a His8/TEV/SAG N-terminal fusion and purification includes tag
    cleavage. Wild-type-derived PqsBC converts supplied 2-ABA plus octanoyl-CoA into
    HPLC-quantified HHQ at 25 C in 50 mM HEPES pH 8.2, 50 mM NaCl and 100 micromolar
    DTT; spectroscopy independently follows the net reaction. The owner snippet "quantification
    of HHQ by HPLC" is exact. This supports the four substrate/process/product edges
    and the separate 2-ABA assay-precursor edge, without proving a complete PqsA/D/E/BC
    reconstitution.
- evidence_id: hhq-primary2016-association-and-boundaries
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=4807248&retmode=xml
  locator: 'Same full manuscript: purification, PqsBC C129A crystal structure results,
    Table 1 and final Discussion paragraph'
  accessed_at: '2026-10-21T07:26:38Z'
  support: supports
  summary: Copurification, gel filtration and a large PqsB/PqsC interface support
    association. The owner snippet "form a tight complex" is exact in the Results
    and Introduction. The crystal is the C129A variant, whereas the net activity assay
    uses the wild-type-derived preparation. The paper proposes a scaffolding role
    for PqsB and leaves elementary cyclization unresolved; the owner quote "ring closure
    could also occur non-enzymatically" is exact. Thus the graph correctly avoids
    independent PqsB catalysis, enzyme-catalyzed ring closure and physiological stoichiometry
    claims. Figure 8 instead uses engineered P. putida KT2440, not a native producer.
- evidence_id: hhq-primary2021-native-genetics
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=8432897&retmode=xml
  locator: DOI:10.1371/journal.ppat.1009425 / PMID:34460871; Results on constitutive
    pqsABCD, Figure 8 and Methods AQ quantification; full XML
  accessed_at: '2026-10-21T07:27:23Z'
  support: supports
  summary: The study separately measures HHQ, PQS and HQNO by LC-MS/MS. In the tatA-intact
    PAO1 pqsA deletion background, plasmid pqsABCD restores HHQ relative to the empty-vector
    control; the tatA/pqsA double mutant does not show that restoration. These data
    establish native pqsA-linked HHQ loss and genetic restoration under the reported
    conditions. They do not establish unconditional pathway sufficiency, require every
    bounded-locus gene, or show that PhnAB is universally necessary.
- evidence_id: hhq-primary2021-strain-table
  kind: primary_source
  reference: https://journals.plos.org/plospathogens/article/file?id=10.1371/journal.ppat.1009425.s011&type=supplementary
  locator: Official Table S1 DOCX, complete strain and plasmid table; primary-2021-tat-tableS1.docx
    in HHQ source preparation
  accessed_at: '2026-10-21T07:28:04Z'
  support: supports
  summary: The relevant native wild type is PAO1 from the Copenhagen collection, and
    the pqsA mutant is an in-frame PAO1 deletion. PA14 strains are separately listed
    for the petA/cytochrome experiments. The pBBR1MCS-5::pqsABCD construct is attributed
    to the 2011 Niewerth study. This verifies PAO1 lineage, while the exact historical
    stock and plasmid sequence remain distinct from the current reference genome.
- evidence_id: hhq-primary2021-fig8-visual
  kind: primary_source
  reference: https://journals.plos.org/plospathogens/article/figure/image?size=large&id=10.1371/journal.ppat.1009425.g008
  locator: Official Figure 8, visually inspected HHQ panel B at 07:46:48Z; receipt
    tat2021-fig8-access.json
  accessed_at: '2026-10-21T07:46:45Z'
  support: supports
  summary: The HHQ-labelled panel B shows baseline signal for the pqsA deletion with
    empty vector, a clear signal after pqsABCD complementation, and baseline signal
    in the tatA/pqsA double mutant with either vector. The adjacent PQS and HQNO panels
    were kept distinct. The axis is LC-MS/MS peak area, not absolute concentration;
    no new quantitative yield is inferred.
- evidence_id: hhq-primary2021-native-wildtype-visual
  kind: primary_source
  reference: https://journals.plos.org/plospathogens/article/file?id=10.1371/journal.ppat.1009425.s004&type=supplementary
  locator: Official Figure S4 TIFF, plotted HHQ panel A, visually inspected at 07:47:24Z;
    tat2021-figS4-access.json
  accessed_at: '2026-10-21T07:47:21Z'
  support: supports
  summary: Whole-culture extracts of the PAO1 wild type show HHQ at 8 and 16 h, while
    the tatA/pqsA double mutant remains near baseline with or without pqsABCD. This
    independently supports native HHQ production rather than only a complemented-mutant
    observation. The source caption reverses the panel labels (it calls PQS A and
    HHQ B); the actual plotted axis labels are HHQ A and PQS B. The review follows
    the explicit plotted chemical labels and preserves the caption discrepancy.
- evidence_id: hhq-pdb5dwz-construct
  kind: database
  reference: https://files.rcsb.org/download/5DWZ.cif
  locator: _entity_poly, _struct_ref, _struct_ref_seq and _struct_ref_seq_dif; full
    deposited sequence comparison in pdb-construct-comparison.json
  accessed_at: '2026-10-21T07:43:41Z'
  support: supports
  summary: PqsB entity 2 has the complete 283-residue native Q9I4X2 sequence. PqsC
    entity 1 has SAG followed by native Q9I4X1 residues 2-348; the sole aligned difference
    is native C129A (construct position 131), for a 350-residue deposited sample.
    The current mmCIF still records older A0A072ZZD2 and A0A0C6EZ24 mappings. Independent
    current UniProt/GenPept/native-CDS comparisons supplied by the identity reviewer
    establish the chosen PAO1 references. The owner distinguishes both engineered
    sequence and historical mappings correctly.
- evidence_id: hhq-pdb5dwz-coverage-assemblies
  kind: database
  reference: https://files.rcsb.org/download/5DWZ.cif
  locator: _pdbx_struct_assembly, _pdbx_struct_assembly_gen, _pdbx_unobs_or_zero_occ_residues;
    current RCSB entry and entity JSON cross-checks
  accessed_at: '2026-10-21T07:43:41Z'
  support: supports
  summary: The asymmetric unit contains four PqsB and four PqsC chains. Across 2532
    sample residues, 2474 are modeled and 58 are unmodeled. Unmodeled counts by author
    chain are A5/B5/C10/D10/E4/F10/G5/H9. Both deposited assemblies are PISA/author-and-software-defined
    tetramers of four chains. Current RCSB entity mapping uses Q9I4X1 for PqsC and
    Q9I4X2 for PqsB, while the mmCIF retains older accessions. This agrees with the
    owner caveats; deposited assemblies are not independent proof of physiological
    stoichiometry.
- evidence_id: hhq-native-reference-for-construct
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9I4X1.json
  locator: Complete current Q9I4X1 and Q9I4X2 sequence fields; /011/identity-access.json
    and protein-equivalence.json
  accessed_at: '2026-10-21T07:43:36Z'
  support: supports
  summary: 'The current PAO1 native references contain 348 residues for PqsC and 283
    for PqsB. The identity reviewer independently translated the complete native CDSs
    and matched the corresponding GenPept sequences. This review separately aligned
    the complete PDB sample sequences: PqsB is exact and PqsC differs only by the
    N-terminal construct change and C129A described above. Sequence agreement does
    not independently verify the historical experimental plasmid.'
- evidence_id: hhq-local-claim-routing-and-ownership
  kind: record_content
  reference: data/natural_products/alkaloids/2-heptylquinolin-4-1h-one.yaml; data/raw/mibig_compounds.tsv;
    curation/mibig_claim_references.tsv; curation/mibig_locus_evidence_overrides.tsv;
    scripts/seed_from_sources.py
  locator: Complete owner and resolved view, exact BGC0000922:3 source row; claim-reference
    loader and method override implementation
  accessed_at: '2026-10-21T07:47:41Z'
  support: partial
  summary: The source compound citation is copied into both PAO1 producer and locus
    evidence. Full-row canonical SHA256 is c3f5cdc523e4b0c2930fccdaeed45d3b942d4aab117341c543ceb06f941051cd.
    The separate existing PqsBC graph already correctly uses the PAO1 2016 primary
    assay. Current claim-reference decisions enforce a complete source-row SHA, whereas
    expected_* context fields are enforced only for WITHDRAW in the method loader.
    A future REPLACE must be paired with a SHA-pinned claim-reference row or the loader
    must be extended; expected_* fields alone do not protect REPLACE.
- evidence_id: hhq-maintained-override-search
  kind: search
  reference: curation/; conf/
  locator: rg --no-ignore --hidden for BGC0000922, minted identifier, exact label
    variants and slug; exit 1 with no matches
  accessed_at: '2026-10-21T07:47:53Z'
  support: context_only
  summary: No matching maintained decision row was found in these bounded curation
    and configuration trees. This supports the local completion task, not a claim
    that no scientific evidence exists.
  search_scope: Ignored and hidden files included. Scope limited to the current isolated
    checkout curation/ and conf/, searching BGC0000922, mibig-182e475a70, 2-heptylquinolin-4,
    2-heptyl-4.*quinolone and 2-heptylquinolin-4-1h-one.
- evidence_id: hhq-imodulon-component85-context
  kind: database
  reference: https://imodulondb.org/api/imodulons/p_aeruginosa/precise364/85/genes
  locator: Exact component-membership JSON endpoint used by installed runner get_imodulon_genes;
    verified HTTP200 and matching seven-gene payload; imodulon-component85-source.json
    plus source-access receipt. Original runner summary and context receipts retained.
  accessed_at: '2026-10-21T07:25:32Z'
  support: context_only
  summary: 'The complete returned membership has seven genes: pqsA/PA0996, pqsB/PA0997,
    pqsC/PA0998, pqsD/PA0999, pqsE/PA1000, phnA/PA1001 and phnB/PA1002. All seven
    have positive weights above the reported threshold 0.115881 and member rows name
    MvfR. PhnA/P09785 and PhnB/P09786 are annotation context for this HHQ locus. STRING
    identifiers use taxon 208964. PqsH is not among these seven component members;
    no biological absence or lack of regulation follows. Component weights represent
    a transcriptomic decomposition, not reaction rates or causal necessity. Reused
    source inspection with its original timestamp; applicability here is only PAO1
    pathway transcriptional context.'
- evidence_id: hhq-imodulon-dataset-strain-context
  kind: primary_source
  reference: https://academic.oup.com/nar/article/50/7/3658/6561658
  locator: DOI:10.1093/nar/gkac187; Methods, RNA extraction and Data acquisition;
    Results, iModulon structure of the transcriptome; dataset link
  accessed_at: '2026-10-21T07:21:25Z'
  support: context_only
  summary: The dataset's primary publication explicitly links aeruPRECISE364 to the
    inspected database dataset. It reports PAO1 and PAO1 delta-mexB expression profiles,
    comprising 364 quality-filtered samples (83 new and 281 public), mapped to PAO1
    genome NC_002516.2. Thus this is relevant PAO1 lineage regulatory context, not
    a PA14 assay. The runner's dataset catalogue independently labels p_aeruginosa/precise364
    as Pseudomonas aeruginosa but supplies no strain field; the strain attribution
    comes from the primary methods. Reused source inspection with its original timestamp;
    applicability here is only PAO1 pathway transcriptional context.
- evidence_id: hhq-imodulon-precise411-unavailable
  kind: search
  reference: https://imodulondb.org/dataset.html?organism=p_aeruginosa&dataset=precise411
  locator: Original root search receipts and .err files for pqs, phn and mvfR
  accessed_at: '2026-10-21T07:18:22Z'
  support: unknown
  summary: 'All three precise411 searches exited 2 with the typed error: imodulons[0].regulator
    must be a JSON list, got NoneType. The outputs were empty because parsing failed.
    The dataset is listed by the runner, but relevant components could not be assessed
    through this runner. This is unavailable evidence, not a negative search result.
    Reused source inspection with its original timestamp; applicability here is only
    PAO1 pathway transcriptional context.'
  search_scope: Three bounded installed-runner searches in p_aeruginosa/precise411
    for pqs, phn and mvfR. Each failed during typed response parsing; results were
    unavailable, not negative.
- evidence_id: H-HAYS1945
  kind: primary_source
  reference: https://www.researchgate.net/publication/232301559_Antibiotic_substances_produced_by_Pseudomonas_aeruginosa
  locator: DOI:10.1016/S0021-9258(17)41580-8; pp.727–729, cultures and provisional
    Pyo naming; pp.730–732, assays and fractionation; pp.735–741, purification and
    physical characterization; pp.745–746, bacteriological scope
  accessed_at: '2026-10-21T07:49:13Z'
  support: supports
  summary: Clinical cultures are designated P-SLU and P-CC; these are not identified
    as PAO1. P-SLU lost activity, and P-CC variants differed in pigment and Pyo production.
    Broth growth, solvent extraction, permutit fractionation and recrystallization
    yielded Pyo fractions. Chemical constitutions were not assigned in this paper.
    Much bacteriological work used crude extracts or Pyo II, so it cannot all be attributed
    to purified HHQ. Primary article text inspected through web extraction; original
    PDF and figure pixels not inspected. Direct free HTTP PDF and HTML requests returned
    403.
- evidence_id: H-WELLS1952
  kind: primary_source
  reference: https://www.researchgate.net/publication/10560858_Antibiotic_substances_produced_by_Pseudomonas_aeruginosa_syntheses_of_Pyo_Ib_Pyo_Ic_and_Pyo_III
  locator: DOI:10.1016/S0021-9258(18)55737-9; pp.331–332, direct relationship to Hays
    1945 and structural conclusions; p.335, synthesis and comparison with authentic
    Pyo Ib
  accessed_at: '2026-10-21T07:51:28Z'
  support: supports
  summary: Wells explicitly assigns Pyo Ib to 2-heptyl-4-quinolinol. Synthetic material
    melted at 146–147°C, did not depress the melting point of authentic Pyo Ib, and
    depressed that of Pyo Ic. The paper compares UV absorption of synthetic and authentic
    material and directly connects its natural Pyo samples to Hays 1945. 2-Heptyl-4-quinolinol
    is the lactim tautomer of the reviewed 2-heptylquinolin-4(1H)-one (HHQ); this
    name reconciliation is chemical interpretation of the explicit structure assignment.
    Primary article text inspected through web extraction; original PDF and figure
    pixels not inspected.
- evidence_id: H-LUCKNER1965
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/14291872/
  locator: DOI:10.1016/S0040-4039(01)83977-0; Bibliographic metadata only; exact primary
    content unavailable
  accessed_at: '2026-10-21T07:48:37.681611Z'
  support: unknown
  summary: Metadata identify the 1965 article, but the exact heptyl homologue, experimental
    strain and structure-identification methods could not be inspected. Publisher
    access returned HTTP 403. This is an incomplete citation check, not refutation
    of the LOTUS association. Metadata only. Publisher HTTP 403; DOI web open failed;
    PubMed open yielded browser challenge. No experimental full text inspected.
- evidence_id: hhq-imodulon-search-scope
  kind: search
  reference: https://imodulondb.org/dataset.html?organism=p_aeruginosa&dataset=precise364
  locator: Installed kg-microbe-sources read-only searches for pqs, phn and mvfR;
    imodulon-search-receipts.json and captured outputs
  accessed_at: '2026-10-21T07:18:21Z'
  support: context_only
  summary: Bounded precise364 searches return component 85 MvfR/PQS signalling and
    the corresponding pqs and phnA/phnB genes. The mvfR query also returns component
    15 LasR, annotated for pyochelin biosynthesis and secretion, which was not treated
    as exact-HHQ biosynthetic evidence. The phn query's component 70 PhnR-2 concerns
    phosphate/phosphonate transport context; it is not evidence for the similarly
    named anthranilate synthase genes. Original root search receipts, not a fresh
    search, were reused.
  search_scope: Organism p_aeruginosa, dataset precise364; queries pqs, phn and mvfR.
    Dataset-local search only, with separate gene and component matches.
assessments:
- assessment_id: A-IDENTITY-EXACT
  area: identity
  topic: Exact achiral HHQ owner identity
  outcome: supported
  summary: The valid owner graph, stored complete InChI/key, computed formula and
    current PubChem/NPAtlas records agree on neutral HHQ. The source label, actual
    quinolone depiction and stereo_complete flag are coherent. The hydroxy wording
    in older primary literature and NPAtlas original_name is reconciled through explicitly
    represented tautomerism rather than mistaken for PQS, HQNO or a longer side-chain
    congener.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-CHEMISTRY-IDENTITY
  - E-NPATLAS
  - E-PUBCHEM
  - E-HHQ-PRIMARY-IDENTITY
- assessment_id: A-XREF-EQUIVALENCE
  area: identity
  topic: NPA026460 exactly matches the represented quinolone
  outcome: supported
  summary: The current NPAtlas structure is exactly the owner keto tautomer, with
    the same full structure and no reassignment. Its origin reference and organism
    are retained as source metadata; the seven occurrence citations are reviewed separately.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - E-NPATLAS
  - E-IDENTITY-LOCAL
  - E-CHEMISTRY-IDENTITY
- assessment_id: A-GROUNDING-COLLISION
  area: grounding
  topic: Conservative collision status is valid and exact candidate is now resolved
  outcome: supported
  summary: REVIEW_NEEDED is an accurate result of the present multi-three-star-key
    policy, so it is not a false exact-grounding claim. Official default molfiles
    now identify CHEBI:62219 as the owner graph and CHEBI:75306 as its hydroxy tautomer,
    despite both Standard InChIKeys being identical. This establishes the scientific
    candidate choice; implementing a durable grounding decision remains separate from
    this read-only review.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - E-CHEBI-62219
  - E-CHEBI-75306
  - E-CHEBI-MOL-62219
  - E-CHEBI-MOL-75306
  - E-CHEBI-TAUTOMER-COMPARISON
  - E-GROUNDING-INVENTORY
  - E-GROUNDING-IMPLEMENTATION
  - E-GROUNDING-OWNERSHIP
- assessment_id: A-NATIVE-PROTEIN-REFERENCES
  area: grounding
  topic: Five exact native PAO1 reference sequences verified
  outcome: supported
  summary: Each selected accession has the correct PAO1 strain/taxon, gene, locus,
    protein length and genomic coordinates. Independent table 11 translation agrees
    with the deposited CDS translation, separately retrieved GenPept protein and UniProt
    at every residue. This validates native references and the historical version/length
    notes, without asserting tagged, mutated or historical plasmid-sequence equivalence.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - E-PAO1-GENOME
  - E-PROTEIN-EQUIVALENCE
  - E-PQSA-UNIPROT
  - E-PQSA-GENPEPT
  - E-PQSB-UNIPROT
  - E-PQSB-GENPEPT
  - E-PQSC-UNIPROT
  - E-PQSC-GENPEPT
  - E-PQSD-UNIPROT
  - E-PQSD-GENPEPT
  - E-PQSE-UNIPROT
  - E-PQSE-GENPEPT
- assessment_id: A-PQSADE-ANNOTATION
  area: graph
  topic: PqsA/PqsD/PqsE graph matches its stated annotation scope
  outcome: supported
  summary: All ten database-only reaction/substrate/product edges agree with the current
    reviewed PqsA, PqsD and PqsE annotations. ATP/CoA use, AMP/diphosphate release,
    malonyl-CoA condensation to 2-ABA-CoA and hydrolysis to 2-ABA are represented
    at the correct evidence tier. The graph is explicitly unbalanced and omits some
    reaction species, so no stoichiometric completion is inferred. It avoids DHQ-to-HHQ
    substitution, PqsE essentiality, complete-route reconstitution and borrowed PA14
    regulatory function. All three quoted snippets are literal matches. The separate
    final 2-ABA-to-HHQ net-assay link is documented in the primary-source assessments.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-PQSA-UNIPROT
  - E-PQSD-UNIPROT
  - E-PQSE-UNIPROT
  - E-PROTEIN-EQUIVALENCE
- assessment_id: A-PQSBC-NATIVE-BOUNDARIES
  area: graph
  topic: PqsB/PqsC native reference labels preserve subunit and construct limits
  outcome: supported
  summary: Current reviewed annotations support the selected protein labels and PqsBC
    association. The graph uses PROTEIN for PqsB and ENZYME for PqsC and expressly
    avoids assigning independent PqsB catalysis, enzyme-controlled ring closure or
    physiological complex stoichiometry. Native sequence agreement is separate from
    the PDB/experimental construct audit, documented in the primary-source assessments.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-PQSB-UNIPROT
  - E-PQSC-UNIPROT
  - E-PROTEIN-EQUIVALENCE
- assessment_id: R-OCCURRENCE-POSITIVE
  area: evidence
  topic: Three exact natural-occurrence associations
  outcome: supported
  summary: Haplophyllum occurrence is supported under its accepted synonym; Streptomyces
    MBTG13 and Pseudoalteromonas M2 support the recorded genus-level associations.
    Primary isolate evidence does not automatically promote these LOTUS associations
    into biosynthesis-grade producers. All five provenance entities match their recorded
    taxon identifiers.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - R-HAPLOPHYLLUM-PRIMARY
  - R-HAPLOPHYLLUM-TAXON
  - R-STREPTOMYCES
  - R-PSEUDANE
  - R-TAXON-PROVENANCE
  - E-CHEBI-75306
- assessment_id: R-RUTA-UNRESOLVED
  area: evidence
  topic: Exact HHQ assignment in the cited Ruta paper
  outcome: unknown
  summary: The primary abstract identifies an unresolved homologue mixture but not
    the exact heptyl member. Exact occurrence is therefore not independently established
    in this review. The two DOI registrations refer to one paper; neither registration
    is a second isolation. Lack of readable primary compound-level evidence does not
    establish absence from Ruta.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - R-RUTA-DOI1
  - R-RUTA-DOI2
  - R-RUTA-ACCESS
  - R-RUTA-SEARCH
- assessment_id: R-SIBLING-ACTIVITY
  area: evidence
  topic: Pinned sibling links and broad antibacterial summary
  outcome: supported
  summary: Both pinned sibling records resolve and justify the summary at the repository-defined
    source-role tier. The inspected 2019 purified-compound bacterial assays independently
    support broad antibacterial activity. No MIC value, direct microbial target, clinical
    efficacy or antifungal-growth claim is imported into the owner. Shared Standard
    InChIKey linkage is distinct from exact fixed-H tautomer equality.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - R-SIBLING-QUINOLONE
  - R-SIBLING-HYDROXY
  - R-SIBLING-INVENTORY
  - R-STREPTOMYCES
  - E-CHEBI-TAUTOMER-COMPARISON
- assessment_id: R-CLASSIFICATION-HISTORY
  area: provenance
  topic: Computed filing, asserted classifications and bounded curation history
  outcome: supported
  summary: NPClassifier outputs match the pinned exact-key result and remain computational.
    MIBiG source classes are separately asserted, with no inference that the tryptophan
    classification proves a precursor experiment. Two bounded graph-curation events
    do not claim whole-record review, and SEEDED remains appropriate. The earlier
    primary-access discussion is historical and is not contradicted by later successful
    retrieval.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - R-LOCAL
  - R-ISSUE822
- assessment_id: R-COMPLETE-OWNER
  area: scope
  topic: Entire owner and resolved mechanism coverage
  outcome: supported
  summary: The complete owner, all 19 nodes and 17 edges in two inline graphs, source
    provenance, discussions and history were read. Separate assessments address each
    assertion group. There are no external components or quantitative/clinical claims
    to audit in this owner; optional mechanism expansion is outside the required completion
    criteria. Unavailable historical occurrence checks are explicit.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - R-LOCAL
- assessment_id: hhq-native-locus-supported
  area: evidence
  topic: Exact HHQ native PAO1 production and pqs locus
  outcome: supported
  summary: MIBiG compound 3, the recorded PAO1 reference interval, the PAO1-derived
    2016 enzyme assay and the PAO1 Copenhagen native 2021 measurements converge on
    this exact product. The native pqsA deletion/restoration evidence supports BGC_CHARACTERIZED
    and CLUSTER_DEMONSTRATED after maintained curation. Stock provenance and reference-locus
    mapping remain explicit; whole-region sufficiency and universal PhnAB necessity
    do not follow.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - hhq-source922-compound3
  - hhq-pao1-locus-reference
  - hhq-primary2016-pqsbc-assay
  - hhq-primary2021-native-genetics
  - hhq-primary2021-strain-table
  - hhq-primary2021-fig8-visual
  - hhq-primary2021-native-wildtype-visual
- assessment_id: hhq-citation-routing-concern
  area: evidence
  topic: Source compound evidence versus strain-specific producer and locus citations
  outcome: concern
  summary: The generated claim references route a PA14 study to PAO1 producer and
    locus claims without a strain qualifier. This does not refute PAO1 production;
    separately inspected PAO1 studies support it. One claim-specific citation and
    method correction resolves the scope mismatch and the inherited unstated methods.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - hhq-primary2013-strain-scope
  - hhq-local-claim-routing-and-ownership
  - hhq-maintained-override-search
  - hhq-primary2021-native-genetics
- assessment_id: hhq-pqsbc-complete-graph
  area: evidence
  topic: All seven nodes and six edges of pqsbc-pao1-net-hhq-formation
  outcome: supported
  summary: The two native references, association edges, two assay substrates, net
    process and detected HHQ product are supported at the explicitly bounded level.
    Exact short snippets match the primary text. The record correctly separates wild-type-derived
    assay preparation from the C129A crystal, sample sequence from native reference,
    net chemistry from unresolved ring closure, and association from independent subunit
    catalysis or physiological oligomerization. No graph correction is indicated.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - hhq-primary2016-pqsbc-assay
  - hhq-primary2016-association-and-boundaries
  - hhq-pdb5dwz-construct
  - hhq-pdb5dwz-coverage-assemblies
  - hhq-native-reference-for-construct
- assessment_id: hhq-second-graph-net-connection
  area: evidence
  topic: Final net assay connection in pqsade-pao1-annotated-hhq-precursors
  outcome: supported
  summary: The 2-ABA is_assay_precursor_of HHQ edge explicitly requires the separate
    PqsBC assay and octanoyl-CoA. It accurately avoids a one-step PqsE-to-HHQ reaction
    and a full-pathway reconstitution. Upstream PqsA/D/E catalytic statements are
    separately labelled database assertions; their full native reference/annotation
    audit is documented in the companion assessments.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - hhq-primary2016-pqsbc-assay
  - hhq-local-claim-routing-and-ownership
- assessment_id: hhq-imodulon-context-only
  area: evidence
  topic: Reused PAO1 iModulon context
  outcome: supported
  summary: precise364 component 85 groups pqsABCDE and phnAB in a PAO1-lineage compendium.
    This is compatible transcriptional context for the HHQ pathway and is not used
    to establish exact chemistry, native necessity or complex assembly. The optional
    precise411 runner parsing failure is preserved as unavailable evidence, not absence.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - hhq-imodulon-component85-context
  - hhq-imodulon-dataset-strain-context
  - hhq-imodulon-precise411-unavailable
- assessment_id: H-HISTORICAL-BRIDGE
  area: evidence
  topic: Retrospective Pyo Ib to HHQ primary identity bridge
  outcome: supported
  summary: The 1945 natural isolation and 1952 explicit structural assignment together
    support the recorded species-level occurrence. The older provisional name is not
    a demonstrated erroneous citation. Historical clinical strains remain distinct
    from PAO1, and mixture activity is not attributed to pure HHQ.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - H-HAYS1945
  - H-WELLS1952
  - E-CHEBI-75306
- assessment_id: H-1965-UNKNOWN
  area: evidence
  topic: Independent 1965 occurrence citation
  outcome: unknown
  summary: No readable experimental source was obtained for the 1965 assertion. A
    positive 1945/1952 identity bridge does not validate a separate publication. Full
    primary inspection must resolve the homologue and organism scope before this individual
    citation is signed off.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  evidence_ids:
  - H-LUCKNER1965
findings:
- finding_id: R-RUTA-REDUNDANCY
  issue_key: lotus-hhq-ruta-graveolens-duplicate-publication-dois
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Two Ruta occurrences cite two registrations of the same paper
  description: The otherwise identical Ruta graveolens occurrences use PL00010251
    and S007060050230. Publisher and Crossref metadata match the same four authors,
    German title, volume 130 issue 5 and page 703, including the original article
    identifier 91300703. Treating these as two displayed occurrence entries obscures
    that there is one publication. This bibliographic redundancy is established independently
    of the still-unverified exact HHQ assignment in the 1999 full text.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  field_paths:
  - occurrences[4]
  - occurrences[5]
  evidence_ids:
  - R-RUTA-DOI1
  - R-RUTA-DOI2
  - R-RUTA-ACCESS
  - R-RUTA-TRANSFORM
  rule_id: 'review-yaml-record: minor redundant evidence and claim-specific provenance'
  native_severity: 'minor: one publication represented twice through DOI aliases'
  normalization_reason: This is bounded bibliographic duplication, not evidence that
    the plant occurrence is false or a source-grade upgrade is justified.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: Occurrence source normalization and exact DOI signature
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated occurrence grouping while retaining original provenance
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Preserved original DOI-bearing source triples
- finding_id: hhq-pao1-claim-scope-and-methods
  issue_key: mibig-bgc0000922-compound3-pao1-claim-reference-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: PA14 compound evidence is routed to PAO1 producer and locus claims
  description: BGC0000922 compound 3 uses the 2013 Dulcey citation as compound-level
    MS evidence. The seeder attaches that reference to a specific PAO1 taxon and genomic
    interval, but the inspected study uses PA14 native strains and a PA14-derived
    PqsC construct. This is a claim-level strain mismatch, not evidence that PAO1
    fails to produce HHQ. Direct PAO1-derived enzymology and PAO1 Copenhagen native
    pqsA loss/restoration data are available, so the citation can be corrected and
    the inherited SOURCE_ASSERTION/CLUSTER_UNSTATED methods completed reproducibly
    in the same curation action. The correctly bounded existing graph does not need
    a separate finding.
  target_ids:
  - naturalproductmech:mibig-182e475a70
  field_paths:
  - producer_organisms[0].evidence
  - producer_organisms[0].evidence_basis
  - producer_organisms[0].notes
  - biosynthetic_gene_clusters[0].evidence
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - biosynthetic_gene_clusters[0].link_evidence_basis
  evidence_ids:
  - hhq-source922-compound3
  - hhq-primary2013-strain-scope
  - hhq-primary2016-pqsbc-assay
  - hhq-primary2021-native-genetics
  - hhq-primary2021-strain-table
  - hhq-primary2021-fig8-visual
  - hhq-primary2021-native-wildtype-visual
  - hhq-local-claim-routing-and-ownership
  rule_id: 'review-yaml-record Evidence Rules: narrowest claim, strain scope and inspected
    primary support'
  native_severity: 'major: compound-identification citation is promoted to a strain-specific
    claim beyond its experimental scope'
  normalization_reason: One finding covers the related citation routing and missing
    methods because one maintained exact-row correction resolves both. The underlying
    producer/locus is positively supported by independent PAO1 evidence, and no false-reaction
    or wrong-producer finding is asserted.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: SHA-pinned claim-specific reference routing for BGC0000922:3
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: exact-target native method adjudication, paired with the source pin
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: unchanged original compound evidence and source row provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: reproducible methods and grades; REPLACE context enforcement if extended
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: existing fail-closed full-row SHA validation and reference emission
actions:
- action_id: R-CANONICALIZE-RUTA-PUBLICATION
  description: Represent these verified DOI aliases as one Ruta occurrence/publication
    association through a maintained, tested DOI-alias normalization or source grouping
    step. Preserve both original DOI strings and raw source rows in provenance. Use
    the current publisher DOI PL00010251 as the display reference. Verify the original
    compound-level assignment separately before claiming full occurrence review; do
    not infer an exclusion of HHQ from lack of primary access.
  finding_ids:
  - R-RUTA-REDUNDANCY
  target_ids:
  - naturalproductmech:mibig-182e475a70
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: Occurrence source normalization and exact DOI signature
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated occurrence grouping while retaining original provenance
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Preserved original DOI-bearing source triples
  generator: scripts/extract_lotus.py and scripts/seed_from_sources.py, with an explicitly
    maintained alias mapping if introduced
  acceptance_checks:
  - One generated Ruta occurrence represents this one publication, retaining both
    original DOI aliases in evidence or provenance. Independent Ruta publications
    must remain distinct.
  - Pin and test the exact DOI pair, taxon 37565 and full owner key; do not globally
    collapse different articles on title resemblance alone. Preserve raw source assertions
    and MANIFEST/reproduction provenance.
  - Run the documented extraction/seed canary as applicable, inspect the owner diff
    and preserved graphs, then strict target validation, verify-reproduction, verify-corpus
    --summary and qc.
- action_id: route-hhq-pao1-evidence-and-grade
  description: Add a claim-reference decision for BGC0000922:3 pinned to full source-row
    SHA256 c3f5cdc523e4b0c2930fccdaeed45d3b942d4aab117341c543ceb06f941051cd. Use DOI:10.1371/journal.ppat.1009425
    for both native PAO1 producer and locus claims, retaining the Copenhagen strain,
    pqsA deletion, tatA-intact restoration and LC-MS/MS scope in the rationale. Preserve
    the imported 2013 PA14 citation as original compound evidence in the raw row.
    Pair that decision with a REPLACE method override adding Knock-out studies, which
    yields BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED under the current rubric. Keep
    the independently supported 2016 PqsBC graph and its enzyme-assay evidence; any
    additional Enzymatic assays method must carry its own claim-local 2016 reference
    rather than borrowing the 2021 method citation.
  finding_ids:
  - hhq-pao1-claim-scope-and-methods
  target_ids:
  - naturalproductmech:mibig-182e475a70
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: SHA-pinned claim-specific reference routing for BGC0000922:3
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: exact-target native method adjudication, paired with the source pin
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: unchanged original compound evidence and source row provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: reproducible methods and grades; REPLACE context enforcement if extended
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: existing fail-closed full-row SHA validation and reference emission
  generator: scripts/seed_from_sources.py using curation/mibig_claim_references.tsv
    and curation/mibig_locus_evidence_overrides.tsv
  acceptance_checks:
  - The REPLACE override is paired with the existing full-row-SHA claim-reference
    validation, or the method loader is extended to enforce equivalent context. Current
    expected_* fields alone protect WITHDRAW, not REPLACE. Demonstrate rejection on
    a changed compound index, taxon, locus, source citation or structure row.
  - Only BGC0000922:3 (HHQ) changes; compound 1 PQS and compound 2 dihydroxyquinoline
    are not upgraded by inference. Pin source version 5, taxon 208964, AE004091.2:1073960..1087095
    and UYRHHBXYXSYGHA-UHFFFAOYSA-N through the full row digest.
  - Regenerated references distinguish the 2013 PA14 compound study, 2016 PAO1-derived
    purified-complex assay and 2021 PAO1 Copenhagen native genetics. Preserve original
    source provenance and distinguish citation routing from evidence grading.
  - The regenerated native knockout method supports BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED
    but does not claim full bounded-locus sufficiency, sequence identity of historical
    stocks, universal PhnAB necessity, or a native P. putida producer.
  - Both existing graphs retain their construct, net-reaction, annotation-only and
    stoichiometry limits; the PDB C129A model is not described as the active wild-type
    assay preparation.
  - Run the documented seed canary for naturalproductmech:mibig-182e475a70, inspect
    generated differences, then documented regeneration, strict target validation,
    verify-reproduction, verify-corpus --summary and qc.
limitations:
- CHEBI:62219 exported SMILES fails RDKit, but its separately retrieved official default
  molfile parses and exactly matches the owner. Both ChEBI candidates share a tautomer-normalized
  Standard InChI/key; the fixed-H comparison resolves the represented form.
- 'The owner accurately retains the seeder collision flag. No current grounding override
  consumer is assumed: docs explicitly mark decisions.tsv as reserved. A future identifier
  migration requires implemented guarded ownership and reproduction support.'
- NPAtlas official API was fully inspected through the web tool; direct download returned
  HTTP 403, so no full API-response hash is claimed.
- Protein sequence equivalence establishes native-reference identity only. PDB5DWZ
  variants, retained linkers, unmodeled residues and assembly interpretation are covered
  by the independent BGC reviewer.
- PqsA/PqsD/PqsE statements are audited as database annotations. Historical bibliography
  entries and the graph discussion of earlier access failures are not treated as newly
  inspected primary assays.
- The 1999 Ruta exact HHQ assignment remains unavailable at compound level despite
  a readable abstract and located public PDF; direct retrieval failed and screenshots
  did not expose image data to this session. This is not negative occurrence evidence.
- The 2017 and 2019 primary bodies, methods and structure-identification tables were
  inspected as full XML. Their chemical figure images were not obtained after bounded
  publisher/PMC attempts; no independent visual structure reconstruction is claimed.
- Broad antibacterial support is kept at its actual source tier. This review does
  not add quantitative assays, antimicrobial mechanisms or new producer claims.
- The two sibling links share a Standard InChIKey while their fixed-H tautomer graphs
  differ. Current SAME_INCHIKEY basis remains explicit.
- The already-open source-SMILES issue 822 was read, not changed. Fresh default-molfile
  evidence does not repair the malformed exported source string or implement a grounding
  migration.
- Primary source-preparation accesses are reused with original timestamps. Their full
  XML and relevant strain tables were rechecked for this owner; these are not claimed
  as fresh external downloads. New PDB and figure accesses have separate timestamped
  receipts.
- The 2021 PAO1 Copenhagen stock is identified by its primary strain table, not by
  an independently available genome sequence of that historical stock. The reference-locus
  bridge rests on PAO1 named genes and independently verified reference CDSs.
- The 2011 original pBBR-pqsABCD construction paper was identified but not inspected.
  No historical donor/plasmid sequence identity or complete-locus sufficiency is inferred
  from the 2016 engineered P. putida or 2021 complementation experiments.
- PqsBC main text, methods, tables and captions were inspected; its figure pixels
  and supplementary movie were not independently rendered. No new kinetic, cavity-geometry
  or stereochemical conclusion depends on those unviewed assets. The 2021 Figure 8
  and Figure S4 images were independently rendered.
- 'Figure S4 has a primary-source caption/panel-order conflict: plotted HHQ is A although
  the caption calls it B. This is preserved in evidence and is not an error attributed
  to the owner record.'
- PDB deposited sample sequences and modeled coverage were audited, not diffraction
  data, density maps or re-refinement. Deposited PISA tetramers and the paper's heterodimer
  interpretation do not settle physiological stoichiometry.
- The owner's October 11 primary-access limitations are dated historical curation
  notes. This review obtained the 2013 manuscript by an alternate public route; it
  does not rewrite the earlier retrieval history or treat that history as a current
  absence claim.
- precise411 remained unavailable through the previously used typed runner because
  regulator=NoneType failed parsing. Reused precise364 membership is coexpression
  context only, not independent biological proof.
- The 1965 citation remains individually unverified. A positive 1945/1952 bridge does
  not substitute for auditing that separate assertion.
- Accessible 1945/1952 material was extracted text. Garbled OCR formulas and tables
  were not used to derive precise quantitative activity, formula, or molecular-weight
  claims.
- No transfer of historical cultures to PAO1, Pyo II results to HHQ, or extract activity
  to purified HHQ is justified by this scoped review.
- The configured full identifier-label gate accepts 499 warning-level taxon-label
  mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus;
  its exit 0 is not independent verification of every identifier or of this record's
  scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison
  because the isolated clone has no sibling checkout, and skips three command-frontmatter
  cases because their parameter sets are empty. Pinned-hash and network governance
  checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants.
  They do not establish biological production, stereochemical specificity, evidence
  adequacy or literature-level claim support.
notes:
- No scientific owner, source inventory, graph, native status or curation history
  was edited. A saved partial scientific review does not promote SEEDED to REVIEWED.
- Native quality checks are reused from the identical tracked source revision, with
  their original timestamps and receipts. New strict validation was run for this exact
  target; saved-bundle checks follow persistence.
- The source-SMILES issue 822 and current multi-ChEBI collision flag remain open context.
  Valid official molfiles resolve the represented tautomer scientifically; a maintained
  guarded grounding consumer would be needed for a durable identifier migration.
- 'Optional historical documentation improvement: cite Wells 1952 alongside Hays 1945
  to make the exact Pyo Ib/HHQ identity bridge visible. No occurrence correction is
  established for that historical association.'
tags:
- path-order-campaign
- batch-002
- hhq-quinolone
- tautomer-boundaries
links:
- https://github.com/CultureBotAI/NaturalProductMech/issues/822
```
