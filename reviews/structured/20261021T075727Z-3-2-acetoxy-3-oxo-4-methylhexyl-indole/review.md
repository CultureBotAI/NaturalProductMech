# Acetoxy-methylhexyl indole: exact source identity and unresolved primary assay scope

- Review: 20261021T075727Z-3-2-acetoxy-3-oxo-4-methylhexyl-indole
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T07:48:12.877756Z
- Finished UTC: 2026-10-21T07:57:27.367423Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact stereo-incomplete acetoxyhexyl indole, NPAtlas cross-reference, minted grounding, species/strain separation and generated source grades are coherent. A primary patent independently supports natural occurrence. No confirmed corrective finding was established. Exact content of the cited 1995 isolation paper and 2014 congener-specific biosynthesis experiments remains unverified.

## Scope And Provenance

One full generated owner, all source concepts, chemical identity and declared stereochemical resolution, occurrence and producer/locus evidence, classification, grounding and history.

Selection: Twelfth initially unreviewed path, second in batch 002 from fresh origin/main; earlier review starts and saves follow path order. The fresh-main authoritative list has 91 valid bundles covering 54 of 3,116 records; the ten reviews in pending PR 1000 are separate campaign coverage. Ignored files were included. This bundle has one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-1effb406fc | data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylhexyl-indole.yaml | generated | 3-(2'-acetoxy-3'-oxo-4'-methylhexyl)-indole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-1effb406fc | The entire owner validates with zero ERROR rows. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-1effb406fc | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-1effb406fc | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-1effb406fc | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-1effb406fc | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate after environment repair | passed | True | naturalproductmech:mibig-1effb406fc | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Exact connectivity and declared stereo resolution | passed | True | naturalproductmech:mibig-1effb406fc | Owner, NPAtlas, PubChem and official ChEBI default MOL agree on the exact connectivity and two unspecified centres. The only current ChEBI hit has two stars; the minted rationale is consistent. |
| Exact compound in the cited1995 journal paper | unavailable | True | naturalproductmech:mibig-1effb406fc | The primary abstract identifies indole isolation from X. bovienii A2 but does not name this target. Database mapping and independent patent occurrence are positive; the original journal compound-level content remains uninspected. |
| Exact congener assays and stereochemistry in the2014 primary | unavailable | True | naturalproductmech:mibig-1effb406fc | Complete primary abstract supports SS-2004 xenocyloin experiments at family scope. Full body and SI were unavailable; exact target panels and stereochemical assignments cannot be adjudicated. |
| Structured expression-source applicability | not_applicable | False | naturalproductmech:mibig-1effb406fc | The returned complete dataset catalogue has no Xenorhabdus coverage. No biological absence is inferred. |

## Scientific And Domain Assessments

### Exact represented connectivity, congener boundary and honest stereo flag

identity: supported. Targets: naturalproductmech:mibig-1effb406fc.

The label, owner graph, complete InChI/key, C17H21NO3, NPA016203 and current external structures agree on acetoxyhexyl indole. The hydroxy and shorter pentyl siblings are distinguishable. stereo_complete:false accurately flags both C2-prime and C4-prime as unassigned. Neither a racemate nor a fully determined absolute configuration is asserted.

### Minted identity remains justified by the eligible-source rule

grounding: supported. Targets: naturalproductmech:mibig-1effb406fc.

The minted key recomputes from the exact MIBiG compound 4 source concept. Current CHEBI:221219 is an exact chemical match but has only two stars, so it does not contradict the stored no-three-star grounding rationale. Its valid default MOL confirms the match despite a malformed database SMILES export.

### NPAtlas cross-reference is the same chemical representation

identity: supported. Targets: naturalproductmech:mibig-1effb406fc.

NPA016203 has the exact full structure and no reassignment, exclusion or stereoisomer specification beyond the owner. The sole xref is supported.

### Species occurrence corroborated by independent primary patent

evidence: supported. Targets: naturalproductmech:mibig-1effb406fc.

The owner faithfully retains the exact LOTUS species triple as a database assertion. Independent primary patent Examples 10–11 report isolation and identification of exact ID1 from X. bovienii culture broth. This supports the species occurrence itself, while the original journal citation remains separately unverified at the exact-compound level. A2 isolation is not attributed to SS-2004 or converted into a producer experiment.

### Species, strain and Wikidata mapping

grounding: supported. Targets: naturalproductmech:mibig-1effb406fc.

Occurrence taxon 40576 is X. bovienii species; producer and locus taxon 406818 are its SS-2004 strain. Wikidata Q26307560 resolves to the stated species. Both OTHER_BACTERIAL facets are coherent, and the two source strains are not collapsed.

### Computed filing and asserted locus class remain distinct

consistency: supported. Targets: naturalproductmech:mibig-1effb406fc.

ALKALOIDS and the versioned NPClassifier results reproduce the committed exact-key row and match the indole scaffold. PKS is independently preserved from the MIBiG locus, whose Type III/acylating-ketosynthase context is compatible with the 2014 abstract. No computed class is used as evidence of natural origin.

### Biological occurrence supports natural-product origin

evidence: supported. Targets: naturalproductmech:mibig-1effb406fc.

The exact compound is reported from bacterial culture broth in primary isolation evidence. NATURAL_PRODUCT is therefore supported independently of computed filing. No synthesis, degradation-product or semisynthetic identity is substituted.

### Source version, generated status and historical events

provenance: supported. Targets: naturalproductmech:mibig-1effb406fc.

The source concept and structure-source accession identify MIBiG version 4 compound 4, and the owner exactly reproduces the pinned source claims. SEEDED and its two historical seed events make no claim of completed scientific curation. This review does not change record status or history.

### No unsupported demand to populate optional mechanisms or activity

completeness: not_applicable. Targets: naturalproductmech:mibig-1effb406fc.

The complete owner contains no mechanism graph, pathway, activity observation or summary, molecular target, clinical status, dataset or sibling-record assertion. Optional absence alone is not a defect. The full returned iModulonDB catalogue contains no covered Xenorhabdus dataset, so a strain-matched expression query is not applicable.

### Original1995 DOI exact-compound citation verification

evidence: unknown. Targets: naturalproductmech:mibig-1effb406fc.

DOI 10.1021/np50121a016 and PMID 7561900 identify the same original isolation article. Its inspected abstract reports indoles from X. bovienii A2 but does not explicitly name this target. NPAtlas maps this exact structure to that DOI, supporting the imported database citation; it does not substitute for direct inspection of the cited paper. The independent patent supports actual occurrence, but neither its authorship nor matching compound name proves the journal body contains the exact ID1 structure. Citation-specific verification remains incomplete.

### BGC0000189 compound 4 source, strain and locus mapping

evidence: supported. Targets: naturalproductmech:mibig-1effb406fc.

The exact connectivity, SS-2004 taxon, deposited interval, source method vocabulary and generated two-claim grading agree with the inspected databases. The primary abstract independently corroborates SS-2004 and the reported experimental method categories. Neither heterologous expression nor enzymology alone is used to upgrade native production.

### Exact acetoxyhexyl congener in XclA/B/C experiments

evidence: unknown. Targets: naturalproductmech:mibig-1effb406fc.

The source database assigns demonstrated locus methods to exact compound 4, but the accessible primary abstract summarizes the family. Without the full body/SI, the exact XclA/B/C preparation, target-product experiment, native chromatogram, controls and strain-specific construct details could not be independently adjudicated. No contrary experimental result or confirmed owner defect was found; this remains a primary-access limitation.

### S-selectivity versus two-centre exact target stereochemistry

identity: unknown. Targets: naturalproductmech:mibig-1effb406fc.

The owner explicitly says stereo_complete:false. XclA S-selectivity in the primary abstract does not establish both absolute configurations of this exact acetoxyhexyl product, nor independently establish which exact congeners were stereochemically measured. The 4-prime centre remains unassigned in the owner; no R/S repair or stereo_complete:true promotion is warranted from the inspected abstract alone.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-LOCAL | data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylhexyl-indole.yaml; Complete owner and resolved view, including all nested evidence and two seed events | supports | The owner is a seeded MIBiG compound 4 record with one LOTUS species occurrence, one source-asserted SS-2004 producer and one demonstrated-locus database assertion. It contains no referenced components, pathway, causal graph, pure-compound activity, target, clinical claim, dataset or sibling-corpus link. Optional absent slots are observed only in this complete owner; they are not findings. |
| E-CHEMISTRY | /private/tmp/npm-review-work/012/chemistry.json; RDKit 2026.03.5 parse and complete Standard InChI/key calculation | supports | The owner graph yields exactly the stored InChI and QIUGSZAEYGGUPJ-UHFFFAOYSA-N, C17H21NO3, charge 0 and exact mass 287.152143532. The two tetrahedral stereocentres, side-chain C2-prime and C4-prime, are both unspecified. No resolved stereoisomer is asserted. |
| E-STRUCTURE-COMPARISON | /private/tmp/npm-review-work/012/identity-comparison.json; Owner versus official ChEBI default MOL and PubChem graph; source-concept hash calculation | supports | Both official external representations canonicalize to CCC(C)C(=O)C(Cc1c[nH]c2ccccc12)OC(C)=O, exactly the owner graph. The implemented SHA256 of MIBIG, a null separator and BGC0000189:4 yields the stored minted identifier. This confirms represented connectivity and unresolved stereochemistry, not absolute configuration. |
| E-NPATLAS | https://www.npatlas.org/api/v1/compound/NPA016203?include=classifications; Complete official API text, current structure version 1, origin reference and organism, external identifiers and NPClassifier | supports | NPA016203 has the exact owner name, full InChI/key, C17H21NO3 and stereo-unspecified graph. It lists no reassignments or exclusions. Origin is Li et al. 1995, DOI 10.1021/np50121a016, Xenorhabdus bovienii A2; external IDs include BGC0000189. NPClassifier gives Alkaloids / Tryptophan alkaloids / Simple indole alkaloids, glycoside false. API text was inspected via the web tool; no downloaded-response hash is claimed. |
| E-PUBCHEM | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/QIUGSZAEYGGUPJ-UHFFFAOYSA-N/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; Full-key PUG identity response, CID 15285576 | supports | PubChem CID 15285576 has the same complete InChI/key, C17H21NO3 and unassigned-stereochemistry graph. This independent representation supports identity without adding an unrequested xref. |
| E-CHEBI-SEARCH | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=QIUGSZAEYGGUPJ-UHFFFAOYSA-N&amp;size=100; Exact complete InChIKey query; total1 result, one page | supports | The official search returns only CHEBI:221219, rated two stars. This is not an eligible three-star grounding candidate under the repository rule. |
| E-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/221219/; Current record star rating, chemical identity and default_structure3431320 | supports | CHEBI:221219 is the exact named stereo-unspecified compound, two stars, C17H21NO3 and full owner InChI/key. Its genus-level origin is linked to DOI 10.1021/np50121a016. Its exported aromatic SMILES omits the necessary [nH], so identity was checked independently against the valid official default MOL. |
| E-CHEBI-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/221219/; Complete official default molfile | supports | The valid default molfile parses and matches the complete owner graph and key, with two unassigned centres. This resolves the malformed SMILES export without changing the target record. |
| E-SOURCE-ROWS | data/raw/mibig_compounds.tsv; BGC0000189 version 4 compound_index 4; corresponding complete rows in local-sources.json | supports | The pinned row has the exact owner structure and NPA016203 xref, SS-2004 taxon 406818, active BGC0000189, FN667741.1:3771005..3779127, PKS/Type III and entry-level PMID 24488732. Its two method-derived grades reproduce the owner. Entry quality questionable is retained as source metadata, not used as a truth judgement. |
| E-LOTUS | data/raw/lotus_occurrences.tsv; Only full-key row for QIUGSZAEYGGUPJ-UHFFFAOYSA-N, captured in local-sources.json | supports | The exact row gives Xenorhabdus bovienii, taxon 40576, Wikidata Q26307560 and DOI 10.1021/NP50121A016. The owner preserves its occurrence-only DATABASE_ASSERTION scope. |
| E-PUBMED-1995 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=24488732,7561900&amp;retmode=xml; PubmedArticle PMID 7561900; ArticleId DOI and full AbstractText | partial | PMID 7561900 maps to DOI 10.1021/np50121a016, Li et al., Journal of Natural Products 58(7):1081-1086,1995. The abstract reports isolation of indoles and dithiolopyrrolones from X. bovienii A2 but does not name the individual indole structures. Exact structure-to-reference mapping therefore also uses NPAtlas and the separate primary patent, not this abstract alone. |
| E-PRIMARY-PATENT | https://patents.google.com/patent/WO1995003695A1/en; WO1995003695A1, Examples 10–11 and exact ID1; Google Patents text lines617–637 | supports | The investigators report extraction of cell-free X. bovienii culture broth, naming SFU strain A2 or ATCC 35271, and chromatographic isolation of ID1. Example 11 identifies ID1 as the exact acetoxy-methyl-oxohexyl indole, molecular ion 287, and lists its proton NMR. ID2 is the shorter pentyl congener; ID3 is hydroxyhexyl. No absolute stereochemical assignment for ID1 is provided in these sections. This is primary patent evidence, not a substitute labelled as the 1995 journal full text. |
| E-TAXA | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=40576,406818&amp;retmode=xml; TaxaSet entries 40576 and 406818, scientific names, ranks, parent and lineage | supports | NCBITaxon:40576 is species Xenorhabdus bovienii. NCBITaxon:406818 is strain Xenorhabdus bovienii SS-2004, directly parented to 40576. Both belong to Bacteria, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Morganellaceae. OTHER_BACTERIAL is consistent for both; A2 and SS-2004 remain distinct contexts. |
| E-WIKIDATA | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q26307560&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Entity Q26307560 English label and P685 taxon mapping | supports | Q26307560 resolves to Xenorhabdus bovienii and its P685 statement is 40576, agreeing with the occurrence note and NCBI species identity. The later successful API retrieval supersedes the initial403 attempt. |
| E-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0000189.4/annotations.json; Version 4 complete JSON: four compounds, locus, taxon, evidence methods, legacy reference | supports | BGC0000189 version 4 is active and explicitly lists the exact acetoxyhexyl target as compound 4/NPA016203, distinct from the three related congeners. Taxon406818, coordinates3771005..3779127 on FN667741.1, PKS Type III, enzymatic assays and heterologous expression agree with the owner. PMID 24488732 is entry-level; individual compound evidence arrays are empty. |
| E-LOCUS | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=FN667741.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text&amp;from=3771005&amp;to=3779127; Official FN667741.1 genomic region 3771005..3779127, LOCUS and source feature | supports | The requested interval contains 8,123 nt on accession FN667741.1 and explicitly identifies X. bovienii SS-2004, taxon 406818. This verifies accession, coordinates and organism, independently of whether a particular experiment proves exact congener formation. No protein accession is asserted in the owner. |
| E-PUBMED-2014 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=24488732,7561900&amp;retmode=xml; PubmedArticle PMID 24488732; ArticleId DOI and complete AbstractText | partial | PMID 24488732 is Proschak et al. 2014, DOI 10.1002/cbic.201300694. The abstract reports SS-2004 xenocyloin biosynthesis studied by heterologous expression and enzyme assays, an S-selective XclA condensation and XclB/C acylation. The abstract does not map the exact acetoxyhexyl target to an individual assay or assign both target stereocentres. |
| E-NPCLASSIFIER | data/raw/npclassifier.tsv; Exact full-key row, model npclassifier.gnps2.org@2026-09-07 | supports | The committed row has precisely the owner Alkaloids/Tryptophan alkaloids/Simple indole alkaloids results, is_glycoside=false and model version. The represented graph has an indole and no glycoside. The PKS locus label is a separate source-derived axis. |
| E-GROUNDING-RULE | scripts/seed_from_sources.py; mint_identifier lines284–292 and MIBiG source-concept/grounding branch lines950–981 | supports | The seeder hashes MIBIG plus accession:compound_index, selects only eligible three-star ChEBI rows and keeps MINTED when no such row matches. No matching row is present in the pinned three-star inventory for this complete key; the current two-star match does not change that policy result. |
| E-GRADE-RULE | docs/HARMONIZATION.md; Producer versus occurrence section and method-to-producer/locus grading table | supports | Heterologous expression and enzymatic assays map to SOURCE_ASSERTION for the native producer and CLUSTER_DEMONSTRATED for the locus. The owner preserves that separation and cites both imported claims as DATABASE_ASSERTION. This rule explains extraction; it does not establish compound-specific experiments. |
| xcl-native-locus-bridge | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=FN667741.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text&amp;from=3771005&amp;to=3779127; VERSION, source strain/taxon, full interval CDS annotation; locus.gb | supports | The 8123-bp interval belongs to X. bovienii SS-2004 with taxon 406818. CBJ83019.1/XBJ1_3901 (MIBiG xclA) lies at 3777430..3779127 on the reverse strand, and CBJ83018.1/XBJ1_3900 (MIBiG xclB) lies at 3776409..3777440 on the reverse strand. The interval also includes CBJ83016.1/XBJ1_3898, annotated as a synthase III, but the inspected GenBank annotation alone does not identify it experimentally as XclC. These records establish the strain/accession bridge, not full-locus sufficiency or historical construct sequences. |
| xcl-fulltext-si-unavailable | https://chemistry-europe.onlinelibrary.wiley.com/doi/abs/10.1002/cbic.201300694; Public publisher page identifies SI cbic_201300694_sm_miscellaneous_information.pdf; attempted full, PDF, suppl/supinfo and normal downloadSupplement routes; bgc-access.json | unknown | The publisher abstract and SI filename were visible in indexed primary content. Both Wiley domains returned HTTP 403 for the exact supplement and full text, as did the normal PDF and downloadSupplement routes. The Crossref-listed TDM endpoint returned HTTP 400 requiring a TDM client token; no credentials or paid service were used. The body and SI were therefore not obtained or inspected. Access failure is not evidence that the paper lacks the exact product experiment. |
| xcl-institutional-copy-unavailable | https://pure.mpg.de/rest/items/item_3369009; Public author-linked institutional record, complete JSON; bgc-pure-item.json and bgc-access.json | unknown | The author publication list resolves to MPG.PuRe item 3369009. Its complete public REST record contains the matching article metadata and abstract, without a file/component entry providing the manuscript or supplement. OpenAlex separately listed only closed publisher and PubMed locations. This bounded repository check supplied no additional experimental text; it does not show that no author copy exists elsewhere. |
| R-PATENT-PDF | https://patentimages.storage.googleapis.com/88/ee/a5/deee26bcd7e0de/WO1995003695A1.pdf; Original patent printed pp 32-33, Examples 10-11; PDF pages 34-35 rendered and visually inspected at 2026-10-21T07:56:13Z | supports | The original page image confirms cell-free Xenorhabdus bovienii culture extraction, chromatographic separation and the exact ID1 acetoxyhexyl name, molecular ion 287 and reported proton NMR. No absolute stereochemical assignment is made in these inspected sections. This independently checks the HTML transcription without substituting the patent for the cited journal article. |
| R-IMODULON-CATALOGUE | /private/tmp/npm-review-work/010/imodulon-datasets.txt; Complete installed kg-microbe-sources datasets response; actual command receipt in010/imodulon-context-receipts.json | context_only | The complete returned catalogue has 28 dataset keys; none covers Xenorhabdus. No strain-matched structured expression-module query is applicable to this record. This is catalogue coverage only and not evidence against xenocyloin production or gene activity. |

## Limits And Additional Notes

- The owner deliberately represents two unassigned stereocentres. Primary patent structure data, current databases and local calculations verify that resolution; they do not establish an absolute configuration. The 2014 abstract’s XclA S-selectivity is not transferred to both centres of this exact congener.
- The 1995 journal full text was not accessible from the publisher during this review. Its PubMed abstract was read; exact structure-to-reference mapping uses the official NPAtlas record, and independent primary patent Examples 10–11 corroborate exact occurrence. The patent is not represented as a journal full-text inspection.
- NPAtlas official API text was fully inspected via the web tool. Direct download returned HTTP 403, so no full-response hash is claimed.
- Current ChEBI search is bounded to the complete InChIKey and returned one two-star hit. The official default MOL confirms identity; the malformed exported ChEBI SMILES is an external representation issue, not an owner error.
- No raw NMR spectrum was independently reinterpreted and no missing optional mechanism or bioactivity has been fabricated. Native deterministic checks are documented separately from scientific evidence.
- The requested 2014 main body and named SI were not accessible through the bounded free public routes. Only the complete primary abstract, bibliographic metadata and database/locus records were inspected. No full-text or SI experiment is represented as read.
- Exact target compound numbering within the 2014 paper, native and heterologous metabolite panels, individual XclA/B/C products and controls, expression constructs, assay conditions and stereochemical derivatization or comparison methods remain unverified.
- The exact structure is MIBiG compound 4, not one of the hydroxy congeners or the shorter pentyl congener. No congener transfer is used to infer target stereochemistry or a false experimental claim.
- The source PKS/Type III classification is faithfully generated. The abstract describes unusual acylating ketosynthases but is insufficient to adjudicate a classification repair; no reclassification finding is made.
- Native SS-2004 production is reported at family level in the abstract. The record retains SOURCE_ASSERTION; no native knockout, locus necessity or whole-region sufficiency is inferred.
- The independent primary patent corroborates actual occurrence but does not establish the exact content of the cited 1995 journal paper. Its DOI-specific compound verification remains unknown pending an accessible primary body or figures.
- The scientific review is partial for exact 1995 citation content and 2014 target-specific experimental/stereochemical detail. No confirmed contradictory record assertion was established, so no corrective finding or unsupported maintained-input change is proposed.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- No scientific owner, source inventory or native curation status/history was changed. Partial scientific review does not promote SEEDED to REVIEWED.
- Native corpus checks reuse actual successful commands from the identical tracked base with original receipts. Exact target strict validation was run afresh.
- If further primary access resolves the remaining citation or stereochemical questions, record a new immutable review observation before proposing a maintained-source correction. No corrective input change is supported solely by unavailable text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075727Z-3-2-acetoxy-3-oxo-4-methylhexyl-indole
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Acetoxy-methylhexyl indole: exact source identity and unresolved primary assay
  scope'
started_at: '2026-10-21T07:48:12.877756Z'
finished_at: '2026-10-21T07:57:27.367423Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: The exact stereo-incomplete acetoxyhexyl indole, NPAtlas cross-reference,
  minted grounding, species/strain separation and generated source grades are coherent.
  A primary patent independently supports natural occurrence. No confirmed corrective
  finding was established. Exact content of the cited 1995 isolation paper and 2014
  congener-specific biosynthesis experiments remains unverified.
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
  - path: data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylhexyl-indole.yaml
    sha256: bd0c877ab7dd9a932d93749b0ef6b6f6709c20324616fbe0a1ca95d251e561d2
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
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
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One full generated owner, all source concepts, chemical identity and
    declared stereochemical resolution, occurrence and producer/locus evidence, classification,
    grounding and history.
  selection: Twelfth initially unreviewed path, second in batch 002 from fresh origin/main;
    earlier review starts and saves follow path order. The fresh-main authoritative
    list has 91 valid bundles covering 54 of 3,116 records; the ten reviews in pending
    PR 1000 are separate campaign coverage. Ignored files were included. This bundle
    has one target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-1effb406fc
targets:
- target_id: naturalproductmech:mibig-1effb406fc
  path: data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylhexyl-indole.yaml
  label: 3-(2'-acetoxy-3'-oxo-4'-methylhexyl)-indole
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
checks:
- check_id: C-STRICT
  name: Closed-schema target validation
  status: passed
  required: true
  summary: The entire owner validates with zero ERROR rows.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  command: just validate-strict data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylhexyl-indole.yaml
    --out /private/tmp/npm-review-work/012/strict.tsv
  exit_code: 0
  scope_note: Actual target command finished 2026-10-21T07:48:16.467657Z
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
  - naturalproductmech:mibig-1effb406fc
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
  - naturalproductmech:mibig-1effb406fc
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
  - naturalproductmech:mibig-1effb406fc
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
  - naturalproductmech:mibig-1effb406fc
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
  - naturalproductmech:mibig-1effb406fc
- check_id: C-IDENTITY
  name: Exact connectivity and declared stereo resolution
  status: passed
  required: true
  summary: Owner, NPAtlas, PubChem and official ChEBI default MOL agree on the exact
    connectivity and two unspecified centres. The only current ChEBI hit has two stars;
    the minted rationale is consistent.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-CHEMISTRY
  - E-STRUCTURE-COMPARISON
  - E-NPATLAS
  - E-CHEBI-SEARCH
  - E-CHEBI-MOL
- check_id: C-CITED-1995
  name: Exact compound in the cited1995 journal paper
  status: unavailable
  required: true
  summary: The primary abstract identifies indole isolation from X. bovienii A2 but
    does not name this target. Database mapping and independent patent occurrence
    are positive; the original journal compound-level content remains uninspected.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-PUBMED-1995
  - E-NPATLAS
  - E-PRIMARY-PATENT
  - R-PATENT-PDF
- check_id: C-CITED-2014
  name: Exact congener assays and stereochemistry in the2014 primary
  status: unavailable
  required: true
  summary: Complete primary abstract supports SS-2004 xenocyloin experiments at family
    scope. Full body and SI were unavailable; exact target panels and stereochemical
    assignments cannot be adjudicated.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-PUBMED-2014
  - xcl-fulltext-si-unavailable
  - xcl-institutional-copy-unavailable
- check_id: C-IMODULON
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: The returned complete dataset catalogue has no Xenorhabdus coverage. No
    biological absence is inferred.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - R-IMODULON-CATALOGUE
evidence:
- evidence_id: E-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylhexyl-indole.yaml
  locator: Complete owner and resolved view, including all nested evidence and two
    seed events
  accessed_at: '2026-10-21T07:54:32.791480Z'
  support: supports
  summary: The owner is a seeded MIBiG compound 4 record with one LOTUS species occurrence,
    one source-asserted SS-2004 producer and one demonstrated-locus database assertion.
    It contains no referenced components, pathway, causal graph, pure-compound activity,
    target, clinical claim, dataset or sibling-corpus link. Optional absent slots
    are observed only in this complete owner; they are not findings.
  snapshot_sha256: bd0c877ab7dd9a932d93749b0ef6b6f6709c20324616fbe0a1ca95d251e561d2
- evidence_id: E-CHEMISTRY
  kind: validation
  reference: /private/tmp/npm-review-work/012/chemistry.json
  locator: RDKit 2026.03.5 parse and complete Standard InChI/key calculation
  accessed_at: '2026-10-21T07:48:14.273238Z'
  support: supports
  summary: The owner graph yields exactly the stored InChI and QIUGSZAEYGGUPJ-UHFFFAOYSA-N,
    C17H21NO3, charge 0 and exact mass 287.152143532. The two tetrahedral stereocentres,
    side-chain C2-prime and C4-prime, are both unspecified. No resolved stereoisomer
    is asserted.
  snapshot_sha256: 6738c7b0ec908722ba0abfd722280438eea1e3973a6b3d6929cac8f76eb41430
- evidence_id: E-STRUCTURE-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/012/identity-comparison.json
  locator: Owner versus official ChEBI default MOL and PubChem graph; source-concept
    hash calculation
  accessed_at: '2026-10-21T07:52:44.198087Z'
  support: supports
  summary: Both official external representations canonicalize to CCC(C)C(=O)C(Cc1c[nH]c2ccccc12)OC(C)=O,
    exactly the owner graph. The implemented SHA256 of MIBIG, a null separator and
    BGC0000189:4 yields the stored minted identifier. This confirms represented connectivity
    and unresolved stereochemistry, not absolute configuration.
  snapshot_sha256: 5f8cf12d88b12feaf405803fb93b9805a506cdd03c88cb46fed1339fb2f16b56
- evidence_id: E-NPATLAS
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA016203?include=classifications
  locator: Complete official API text, current structure version 1, origin reference
    and organism, external identifiers and NPClassifier
  accessed_at: '2026-10-21T07:52:10Z'
  support: supports
  summary: NPA016203 has the exact owner name, full InChI/key, C17H21NO3 and stereo-unspecified
    graph. It lists no reassignments or exclusions. Origin is Li et al. 1995, DOI
    10.1021/np50121a016, Xenorhabdus bovienii A2; external IDs include BGC0000189.
    NPClassifier gives Alkaloids / Tryptophan alkaloids / Simple indole alkaloids,
    glycoside false. API text was inspected via the web tool; no downloaded-response
    hash is claimed.
- evidence_id: E-PUBCHEM
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/QIUGSZAEYGGUPJ-UHFFFAOYSA-N/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: Full-key PUG identity response, CID 15285576
  accessed_at: '2026-10-21T07:50:13.738911Z'
  support: supports
  summary: PubChem CID 15285576 has the same complete InChI/key, C17H21NO3 and unassigned-stereochemistry
    graph. This independent representation supports identity without adding an unrequested
    xref.
  snapshot_sha256: b6568b87f2546f27a3d79ee5055548783d22394b187eea53b5dbe6d1506737dd
- evidence_id: E-CHEBI-SEARCH
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=QIUGSZAEYGGUPJ-UHFFFAOYSA-N&size=100
  locator: Exact complete InChIKey query; total1 result, one page
  accessed_at: '2026-10-21T07:49:07.758014Z'
  support: supports
  summary: The official search returns only CHEBI:221219, rated two stars. This is
    not an eligible three-star grounding candidate under the repository rule.
  snapshot_sha256: dce0481b578f581d2bf516f744c5c4b7daf9b5579966edaa46ada71e8df51687
  search_scope: Official ChEBI public es_search API; term=QIUGSZAEYGGUPJ-UHFFFAOYSA-N,
    size=100; returned total1 and number_pages1. This is a bounded current exact-key
    search, not an exhaustive search of unindexed alternate structures.
- evidence_id: E-CHEBI
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/221219/
  locator: Current record star rating, chemical identity and default_structure3431320
  accessed_at: '2026-10-21T07:50:13.402335Z'
  support: supports
  summary: CHEBI:221219 is the exact named stereo-unspecified compound, two stars,
    C17H21NO3 and full owner InChI/key. Its genus-level origin is linked to DOI 10.1021/np50121a016.
    Its exported aromatic SMILES omits the necessary [nH], so identity was checked
    independently against the valid official default MOL.
  snapshot_sha256: 36532d36f4e3d8b1c1bb9ab60725ee79c349bedb084c8de817543e2cc5de7b23
- evidence_id: E-CHEBI-MOL
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/221219/
  locator: Complete official default molfile
  accessed_at: '2026-10-21T07:50:13.402853Z'
  support: supports
  summary: The valid default molfile parses and matches the complete owner graph and
    key, with two unassigned centres. This resolves the malformed SMILES export without
    changing the target record.
  snapshot_sha256: 7e14822a0f752389960977e649959fd40125697ee8c31b19026c6b03933e05a8
- evidence_id: E-SOURCE-ROWS
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: BGC0000189 version 4 compound_index 4; corresponding complete rows in local-sources.json
  accessed_at: '2026-10-21T07:54:32.791480Z'
  support: supports
  summary: The pinned row has the exact owner structure and NPA016203 xref, SS-2004
    taxon 406818, active BGC0000189, FN667741.1:3771005..3779127, PKS/Type III and
    entry-level PMID 24488732. Its two method-derived grades reproduce the owner.
    Entry quality questionable is retained as source metadata, not used as a truth
    judgement.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: E-LOTUS
  kind: record_content
  reference: data/raw/lotus_occurrences.tsv
  locator: Only full-key row for QIUGSZAEYGGUPJ-UHFFFAOYSA-N, captured in local-sources.json
  accessed_at: '2026-10-21T07:54:32.791480Z'
  support: supports
  summary: The exact row gives Xenorhabdus bovienii, taxon 40576, Wikidata Q26307560
    and DOI 10.1021/NP50121A016. The owner preserves its occurrence-only DATABASE_ASSERTION
    scope.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: E-PUBMED-1995
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=24488732,7561900&retmode=xml
  locator: PubmedArticle PMID 7561900; ArticleId DOI and full AbstractText
  accessed_at: '2026-10-21T07:49:07.390045Z'
  support: partial
  summary: PMID 7561900 maps to DOI 10.1021/np50121a016, Li et al., Journal of Natural
    Products 58(7):1081-1086,1995. The abstract reports isolation of indoles and dithiolopyrrolones
    from X. bovienii A2 but does not name the individual indole structures. Exact
    structure-to-reference mapping therefore also uses NPAtlas and the separate primary
    patent, not this abstract alone.
  snapshot_sha256: a3ac05ea8d63ac020ceaaa5fd45a1ed0ce1bee13948e096900dc59d63d3eca99
- evidence_id: E-PRIMARY-PATENT
  kind: primary_source
  reference: https://patents.google.com/patent/WO1995003695A1/en
  locator: WO1995003695A1, Examples 10–11 and exact ID1; Google Patents text lines617–637
  accessed_at: '2026-10-21T07:50:13.542964Z'
  support: supports
  summary: The investigators report extraction of cell-free X. bovienii culture broth,
    naming SFU strain A2 or ATCC 35271, and chromatographic isolation of ID1. Example
    11 identifies ID1 as the exact acetoxy-methyl-oxohexyl indole, molecular ion 287,
    and lists its proton NMR. ID2 is the shorter pentyl congener; ID3 is hydroxyhexyl.
    No absolute stereochemical assignment for ID1 is provided in these sections. This
    is primary patent evidence, not a substitute labelled as the 1995 journal full
    text.
  snapshot_sha256: 5e747601869f7f089c1e9c2b90e0de7af24cf07b8f5a3d6eb7e3239fa1f64e4c
- evidence_id: E-TAXA
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=40576,406818&retmode=xml
  locator: TaxaSet entries 40576 and 406818, scientific names, ranks, parent and lineage
  accessed_at: '2026-10-21T07:49:07.390300Z'
  support: supports
  summary: NCBITaxon:40576 is species Xenorhabdus bovienii. NCBITaxon:406818 is strain
    Xenorhabdus bovienii SS-2004, directly parented to 40576. Both belong to Bacteria,
    Pseudomonadota, Gammaproteobacteria, Enterobacterales, Morganellaceae. OTHER_BACTERIAL
    is consistent for both; A2 and SS-2004 remain distinct contexts.
  snapshot_sha256: e30e7f63a8a598c81d5de79fe275304036a4144e701d74fb74d1bf9ac4ca249b
- evidence_id: E-WIKIDATA
  kind: authority
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q26307560&props=labels%7Cclaims&languages=en&format=json
  locator: Entity Q26307560 English label and P685 taxon mapping
  accessed_at: '2026-10-21T07:50:13.547545Z'
  support: supports
  summary: Q26307560 resolves to Xenorhabdus bovienii and its P685 statement is 40576,
    agreeing with the occurrence note and NCBI species identity. The later successful
    API retrieval supersedes the initial403 attempt.
  snapshot_sha256: 717159983c1676ff6cb57d6b11425bcf6d58074c6a1cc6b732eb85273fa7af29
- evidence_id: E-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000189.4/annotations.json
  locator: 'Version 4 complete JSON: four compounds, locus, taxon, evidence methods,
    legacy reference'
  accessed_at: '2026-10-21T07:49:07.389720Z'
  support: supports
  summary: BGC0000189 version 4 is active and explicitly lists the exact acetoxyhexyl
    target as compound 4/NPA016203, distinct from the three related congeners. Taxon406818,
    coordinates3771005..3779127 on FN667741.1, PKS Type III, enzymatic assays and
    heterologous expression agree with the owner. PMID 24488732 is entry-level; individual
    compound evidence arrays are empty.
  snapshot_sha256: 19dc9b2968df6671963e288b5a18c06322ff4d9b85078fcf930cd7ad43bfee14
- evidence_id: E-LOCUS
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=FN667741.1&db=nuccore&report=genbank&retmode=text&from=3771005&to=3779127
  locator: Official FN667741.1 genomic region 3771005..3779127, LOCUS and source feature
  accessed_at: '2026-10-21T07:49:07.390142Z'
  support: supports
  summary: The requested interval contains 8,123 nt on accession FN667741.1 and explicitly
    identifies X. bovienii SS-2004, taxon 406818. This verifies accession, coordinates
    and organism, independently of whether a particular experiment proves exact congener
    formation. No protein accession is asserted in the owner.
  snapshot_sha256: eca1cf9eaaf3166c42cd8d3437c1d41c88cdc2fddfc3393776a8a29a76bd8122
- evidence_id: E-PUBMED-2014
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=24488732,7561900&retmode=xml
  locator: PubmedArticle PMID 24488732; ArticleId DOI and complete AbstractText
  accessed_at: '2026-10-21T07:49:07.390045Z'
  support: partial
  summary: PMID 24488732 is Proschak et al. 2014, DOI 10.1002/cbic.201300694. The
    abstract reports SS-2004 xenocyloin biosynthesis studied by heterologous expression
    and enzyme assays, an S-selective XclA condensation and XclB/C acylation. The
    abstract does not map the exact acetoxyhexyl target to an individual assay or
    assign both target stereocentres.
  snapshot_sha256: a3ac05ea8d63ac020ceaaa5fd45a1ed0ce1bee13948e096900dc59d63d3eca99
- evidence_id: E-NPCLASSIFIER
  kind: record_content
  reference: data/raw/npclassifier.tsv
  locator: Exact full-key row, model npclassifier.gnps2.org@2026-09-07
  accessed_at: '2026-10-21T07:54:32.791480Z'
  support: supports
  summary: The committed row has precisely the owner Alkaloids/Tryptophan alkaloids/Simple
    indole alkaloids results, is_glycoside=false and model version. The represented
    graph has an indole and no glycoside. The PKS locus label is a separate source-derived
    axis.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: E-GROUNDING-RULE
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: mint_identifier lines284–292 and MIBiG source-concept/grounding branch
    lines950–981
  accessed_at: '2026-10-21T07:54:32.791480Z'
  support: supports
  summary: The seeder hashes MIBIG plus accession:compound_index, selects only eligible
    three-star ChEBI rows and keeps MINTED when no such row matches. No matching row
    is present in the pinned three-star inventory for this complete key; the current
    two-star match does not change that policy result.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: E-GRADE-RULE
  kind: record_content
  reference: docs/HARMONIZATION.md
  locator: Producer versus occurrence section and method-to-producer/locus grading
    table
  accessed_at: '2026-10-21T07:54:32.791480Z'
  support: supports
  summary: Heterologous expression and enzymatic assays map to SOURCE_ASSERTION for
    the native producer and CLUSTER_DEMONSTRATED for the locus. The owner preserves
    that separation and cites both imported claims as DATABASE_ASSERTION. This rule
    explains extraction; it does not establish compound-specific experiments.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: xcl-native-locus-bridge
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=FN667741.1&db=nuccore&report=genbank&retmode=text&from=3771005&to=3779127
  locator: VERSION, source strain/taxon, full interval CDS annotation; locus.gb
  accessed_at: '2026-10-21T07:49:07Z'
  support: supports
  summary: The 8123-bp interval belongs to X. bovienii SS-2004 with taxon 406818.
    CBJ83019.1/XBJ1_3901 (MIBiG xclA) lies at 3777430..3779127 on the reverse strand,
    and CBJ83018.1/XBJ1_3900 (MIBiG xclB) lies at 3776409..3777440 on the reverse
    strand. The interval also includes CBJ83016.1/XBJ1_3898, annotated as a synthase
    III, but the inspected GenBank annotation alone does not identify it experimentally
    as XclC. These records establish the strain/accession bridge, not full-locus sufficiency
    or historical construct sequences.
- evidence_id: xcl-fulltext-si-unavailable
  kind: search
  reference: https://chemistry-europe.onlinelibrary.wiley.com/doi/abs/10.1002/cbic.201300694
  locator: Public publisher page identifies SI cbic_201300694_sm_miscellaneous_information.pdf;
    attempted full, PDF, suppl/supinfo and normal downloadSupplement routes; bgc-access.json
  accessed_at: '2026-10-21T07:52:30Z'
  support: unknown
  summary: The publisher abstract and SI filename were visible in indexed primary
    content. Both Wiley domains returned HTTP 403 for the exact supplement and full
    text, as did the normal PDF and downloadSupplement routes. The Crossref-listed
    TDM endpoint returned HTTP 400 requiring a TDM client token; no credentials or
    paid service were used. The body and SI were therefore not obtained or inspected.
    Access failure is not evidence that the paper lacks the exact product experiment.
  search_scope: Free public sources only. DOI/title/author and exact SI-filename searches,
    publisher chemistry-europe/onlinelibrary routes, Crossref-provided TDM endpoint,
    OpenAlex article locations and the author-linked MPG.PuRe item were checked. No
    broad claim of literature absence. Search snippets were used as leads, not experimental
    proof.
- evidence_id: xcl-institutional-copy-unavailable
  kind: search
  reference: https://pure.mpg.de/rest/items/item_3369009
  locator: Public author-linked institutional record, complete JSON; bgc-pure-item.json
    and bgc-access.json
  accessed_at: '2026-10-21T07:51:28Z'
  support: unknown
  summary: The author publication list resolves to MPG.PuRe item 3369009. Its complete
    public REST record contains the matching article metadata and abstract, without
    a file/component entry providing the manuscript or supplement. OpenAlex separately
    listed only closed publisher and PubMed locations. This bounded repository check
    supplied no additional experimental text; it does not show that no author copy
    exists elsewhere.
  search_scope: Exact author-linked item3369009 and DOI-matched OpenAlex work; no
    recursive institutional-repository absence claim.
- evidence_id: R-PATENT-PDF
  kind: primary_source
  reference: https://patentimages.storage.googleapis.com/88/ee/a5/deee26bcd7e0de/WO1995003695A1.pdf
  locator: Original patent printed pp 32-33, Examples 10-11; PDF pages 34-35 rendered
    and visually inspected at 2026-10-21T07:56:13Z
  accessed_at: '2026-10-21T07:55:42.903242Z'
  support: supports
  summary: The original page image confirms cell-free Xenorhabdus bovienii culture
    extraction, chromatographic separation and the exact ID1 acetoxyhexyl name, molecular
    ion 287 and reported proton NMR. No absolute stereochemical assignment is made
    in these inspected sections. This independently checks the HTML transcription
    without substituting the patent for the cited journal article.
  snapshot_sha256: 80a64cb6cbbd141f11962790dc81c37ac9b7a3e52b5320f67c2d5ea78ee44803
- evidence_id: R-IMODULON-CATALOGUE
  kind: search
  reference: /private/tmp/npm-review-work/010/imodulon-datasets.txt
  locator: Complete installed kg-microbe-sources datasets response; actual command
    receipt in010/imodulon-context-receipts.json
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: The complete returned catalogue has 28 dataset keys; none covers Xenorhabdus.
    No strain-matched structured expression-module query is applicable to this record.
    This is catalogue coverage only and not evidence against xenocyloin production
    or gene activity.
  search_scope: All28 dataset rows returned by the installed read-only runner. Original
    command/result reused; no new network query or independent global database export
    is claimed.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
assessments:
- assessment_id: A-IDENTITY
  area: identity
  topic: Exact represented connectivity, congener boundary and honest stereo flag
  outcome: supported
  summary: The label, owner graph, complete InChI/key, C17H21NO3, NPA016203 and current
    external structures agree on acetoxyhexyl indole. The hydroxy and shorter pentyl
    siblings are distinguishable. stereo_complete:false accurately flags both C2-prime
    and C4-prime as unassigned. Neither a racemate nor a fully determined absolute
    configuration is asserted.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-LOCAL
  - E-CHEMISTRY
  - E-STRUCTURE-COMPARISON
  - E-NPATLAS
  - E-PUBCHEM
  - E-PRIMARY-PATENT
- assessment_id: A-GROUNDING
  area: grounding
  topic: Minted identity remains justified by the eligible-source rule
  outcome: supported
  summary: The minted key recomputes from the exact MIBiG compound 4 source concept.
    Current CHEBI:221219 is an exact chemical match but has only two stars, so it
    does not contradict the stored no-three-star grounding rationale. Its valid default
    MOL confirms the match despite a malformed database SMILES export.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-GROUNDING-RULE
  - E-STRUCTURE-COMPARISON
  - E-CHEBI-SEARCH
  - E-CHEBI
  - E-CHEBI-MOL
- assessment_id: A-XREF
  area: identity
  topic: NPAtlas cross-reference is the same chemical representation
  outcome: supported
  summary: NPA016203 has the exact full structure and no reassignment, exclusion or
    stereoisomer specification beyond the owner. The sole xref is supported.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-NPATLAS
  - E-CHEMISTRY
  - E-LOCAL
- assessment_id: A-OCCURRENCE
  area: evidence
  topic: Species occurrence corroborated by independent primary patent
  outcome: supported
  summary: The owner faithfully retains the exact LOTUS species triple as a database
    assertion. Independent primary patent Examples 10–11 report isolation and identification
    of exact ID1 from X. bovienii culture broth. This supports the species occurrence
    itself, while the original journal citation remains separately unverified at the
    exact-compound level. A2 isolation is not attributed to SS-2004 or converted into
    a producer experiment.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-LOTUS
  - E-PRIMARY-PATENT
  - E-TAXA
  - R-PATENT-PDF
- assessment_id: A-TAXONOMY
  area: grounding
  topic: Species, strain and Wikidata mapping
  outcome: supported
  summary: Occurrence taxon 40576 is X. bovienii species; producer and locus taxon
    406818 are its SS-2004 strain. Wikidata Q26307560 resolves to the stated species.
    Both OTHER_BACTERIAL facets are coherent, and the two source strains are not collapsed.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-TAXA
  - E-WIKIDATA
  - E-LOCUS
  - E-LOCAL
- assessment_id: A-CLASSIFICATION
  area: consistency
  topic: Computed filing and asserted locus class remain distinct
  outcome: supported
  summary: ALKALOIDS and the versioned NPClassifier results reproduce the committed
    exact-key row and match the indole scaffold. PKS is independently preserved from
    the MIBiG locus, whose Type III/acylating-ketosynthase context is compatible with
    the 2014 abstract. No computed class is used as evidence of natural origin.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-NPCLASSIFIER
  - E-MIBIG
  - E-PUBMED-2014
  - E-LOCAL
- assessment_id: A-NATURAL-ORIGIN
  area: evidence
  topic: Biological occurrence supports natural-product origin
  outcome: supported
  summary: The exact compound is reported from bacterial culture broth in primary
    isolation evidence. NATURAL_PRODUCT is therefore supported independently of computed
    filing. No synthesis, degradation-product or semisynthetic identity is substituted.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-PRIMARY-PATENT
  - E-NPATLAS
  - E-PUBMED-1995
  - R-PATENT-PDF
- assessment_id: A-PROVENANCE
  area: provenance
  topic: Source version, generated status and historical events
  outcome: supported
  summary: The source concept and structure-source accession identify MIBiG version
    4 compound 4, and the owner exactly reproduces the pinned source claims. SEEDED
    and its two historical seed events make no claim of completed scientific curation.
    This review does not change record status or history.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-LOCAL
  - E-SOURCE-ROWS
  - E-MIBIG
  - E-GROUNDING-RULE
- assessment_id: A-OPTIONAL-CONTENT
  area: completeness
  topic: No unsupported demand to populate optional mechanisms or activity
  outcome: not_applicable
  summary: The complete owner contains no mechanism graph, pathway, activity observation
    or summary, molecular target, clinical status, dataset or sibling-record assertion.
    Optional absence alone is not a defect. The full returned iModulonDB catalogue
    contains no covered Xenorhabdus dataset, so a strain-matched expression query
    is not applicable.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-LOCAL
  - E-LOCUS
  - R-IMODULON-CATALOGUE
- assessment_id: A-CITED-ISOLATION
  area: evidence
  topic: Original1995 DOI exact-compound citation verification
  outcome: unknown
  summary: DOI 10.1021/np50121a016 and PMID 7561900 identify the same original isolation
    article. Its inspected abstract reports indoles from X. bovienii A2 but does not
    explicitly name this target. NPAtlas maps this exact structure to that DOI, supporting
    the imported database citation; it does not substitute for direct inspection of
    the cited paper. The independent patent supports actual occurrence, but neither
    its authorship nor matching compound name proves the journal body contains the
    exact ID1 structure. Citation-specific verification remains incomplete.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-PUBMED-1995
  - E-NPATLAS
  - E-LOTUS
  - E-PRIMARY-PATENT
- assessment_id: xcl-source-and-locus-metadata
  area: evidence
  topic: BGC0000189 compound 4 source, strain and locus mapping
  outcome: supported
  summary: The exact connectivity, SS-2004 taxon, deposited interval, source method
    vocabulary and generated two-claim grading agree with the inspected databases.
    The primary abstract independently corroborates SS-2004 and the reported experimental
    method categories. Neither heterologous expression nor enzymology alone is used
    to upgrade native production.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-MIBIG
  - xcl-native-locus-bridge
  - E-GRADE-RULE
  - E-PUBMED-2014
- assessment_id: xcl-exact-product-assay-scope
  area: evidence
  topic: Exact acetoxyhexyl congener in XclA/B/C experiments
  outcome: unknown
  summary: The source database assigns demonstrated locus methods to exact compound
    4, but the accessible primary abstract summarizes the family. Without the full
    body/SI, the exact XclA/B/C preparation, target-product experiment, native chromatogram,
    controls and strain-specific construct details could not be independently adjudicated.
    No contrary experimental result or confirmed owner defect was found; this remains
    a primary-access limitation.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-MIBIG
  - E-PUBMED-2014
  - xcl-fulltext-si-unavailable
  - xcl-institutional-copy-unavailable
- assessment_id: xcl-stereochemical-scope
  area: identity
  topic: S-selectivity versus two-centre exact target stereochemistry
  outcome: unknown
  summary: The owner explicitly says stereo_complete:false. XclA S-selectivity in
    the primary abstract does not establish both absolute configurations of this exact
    acetoxyhexyl product, nor independently establish which exact congeners were stereochemically
    measured. The 4-prime centre remains unassigned in the owner; no R/S repair or
    stereo_complete:true promotion is warranted from the inspected abstract alone.
  target_ids:
  - naturalproductmech:mibig-1effb406fc
  evidence_ids:
  - E-GRADE-RULE
  - E-PUBMED-2014
  - xcl-fulltext-si-unavailable
findings: []
actions: []
limitations:
- The owner deliberately represents two unassigned stereocentres. Primary patent structure
  data, current databases and local calculations verify that resolution; they do not
  establish an absolute configuration. The 2014 abstract’s XclA S-selectivity is not
  transferred to both centres of this exact congener.
- The 1995 journal full text was not accessible from the publisher during this review.
  Its PubMed abstract was read; exact structure-to-reference mapping uses the official
  NPAtlas record, and independent primary patent Examples 10–11 corroborate exact
  occurrence. The patent is not represented as a journal full-text inspection.
- NPAtlas official API text was fully inspected via the web tool. Direct download
  returned HTTP 403, so no full-response hash is claimed.
- Current ChEBI search is bounded to the complete InChIKey and returned one two-star
  hit. The official default MOL confirms identity; the malformed exported ChEBI SMILES
  is an external representation issue, not an owner error.
- No raw NMR spectrum was independently reinterpreted and no missing optional mechanism
  or bioactivity has been fabricated. Native deterministic checks are documented separately
  from scientific evidence.
- The requested 2014 main body and named SI were not accessible through the bounded
  free public routes. Only the complete primary abstract, bibliographic metadata and
  database/locus records were inspected. No full-text or SI experiment is represented
  as read.
- Exact target compound numbering within the 2014 paper, native and heterologous metabolite
  panels, individual XclA/B/C products and controls, expression constructs, assay
  conditions and stereochemical derivatization or comparison methods remain unverified.
- The exact structure is MIBiG compound 4, not one of the hydroxy congeners or the
  shorter pentyl congener. No congener transfer is used to infer target stereochemistry
  or a false experimental claim.
- The source PKS/Type III classification is faithfully generated. The abstract describes
  unusual acylating ketosynthases but is insufficient to adjudicate a classification
  repair; no reclassification finding is made.
- Native SS-2004 production is reported at family level in the abstract. The record
  retains SOURCE_ASSERTION; no native knockout, locus necessity or whole-region sufficiency
  is inferred.
- The independent primary patent corroborates actual occurrence but does not establish
  the exact content of the cited 1995 journal paper. Its DOI-specific compound verification
  remains unknown pending an accessible primary body or figures.
- The scientific review is partial for exact 1995 citation content and 2014 target-specific
  experimental/stereochemical detail. No confirmed contradictory record assertion
  was established, so no corrective finding or unsupported maintained-input change
  is proposed.
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
- No scientific owner, source inventory or native curation status/history was changed.
  Partial scientific review does not promote SEEDED to REVIEWED.
- Native corpus checks reuse actual successful commands from the identical tracked
  base with original receipts. Exact target strict validation was run afresh.
- If further primary access resolves the remaining citation or stereochemical questions,
  record a new immutable review observation before proposing a maintained-source correction.
  No corrective input change is supported solely by unavailable text.
tags:
- path-order-campaign
- batch-002
- xenocyloin
- stereo-incomplete
```
