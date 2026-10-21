# 12-epi-fischerindole I isonitrile: identity and claim-specific source review

- Review: 20261021T065538Z-12-epi-fischerindole-i-isonitrile
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T06:42:58.663376Z
- Finished UTC: 2026-10-21T06:55:38.396895Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact encoded structure and both chemical xrefs agree across inspected sources. The BGC claim reuses an isolation reference and inherits experiments whose exact-congener scope needs adjudication. A second LOTUS citation resolves to a different chemical-family paper; its support remains unverified because full text was unavailable. This is a partial scientific review with actionable evidence findings, not native REVIEWED status.

## Scope And Provenance

One full generated owner and its complete resolved mechanism; source support is partial where primary text could not be accessed.

Selection: Second unreviewed path after the initial validated list: 91 bundles covered 54 of 3,116 corpus records; 3,062 remained. Selected deterministically in path order, one target per bundle. The helper includes ignored review bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-bc49771bdc | data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml | generated | 12-epi-fischerindole I isonitrile |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and component validation | passed | True | naturalproductmech:mibig-bc49771bdc | One full record validated with zero ERROR rows. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-bc49771bdc | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-bc49771bdc | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-bc49771bdc | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-bc49771bdc | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Initial QC attempt before installing the pinned linter | failed | False | naturalproductmech:mibig-bc49771bdc | The first full QC invocation stopped at lint because the isolated copied Python environment lacked Ruff. Exact uv.lock version Ruff 0.16.6 was subsequently installed and lint passed on later invocations. |
| QC attempt without network access | failed | False | naturalproductmech:mibig-bc49771bdc | After Ruff installation, QC passed lint and stopped at vendored-sync because sandbox DNS could not reach the pinned public CLAW governance source. Approved network access allowed the next invocation to verify all 22 governed artifacts. |
| QC attempt before restoring the required provenance tag | failed | False | naturalproductmech:mibig-bc49771bdc | QC passed lint, vendored sync, documentation, provenance and source queue, then stopped at tests: 998 passed, 1 failed, 4 skipped. The sole failure was the isolated clone lacking refs/tags/review-base/gentamicin-20261013; it was not a failed archive-content assertion. The tag was subsequently fetched from origin. |
| Targeted verification after restoring the provenance tag | passed | False | naturalproductmech:mibig-bc49771bdc | After restoring the required tag, the exact previously failed gentamicin archive test passed (1 passed). No repository content was edited for this remediation. |
| Diagnosis of the suite skip conditions | passed | False | naturalproductmech:mibig-bc49771bdc | The four observed skip cases were reproduced with pytest skip reasons enabled: the optional sibling AntibioticMech comparison has no sibling checkout in the isolated clone, and three command-frontmatter tests have empty parameter sets. This diagnostic invocation executed no passing tests; it reported four skips. |
| Full repository quality gate after environment repair | passed | True | naturalproductmech:mibig-bc49771bdc | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Full source support for 1990 occurrence citation | unavailable | True | naturalproductmech:mibig-bc49771bdc | DOI metadata resolves; full cited article could not be accessed via attempted free routes, leaving exact target/taxon support unresolved. |
| Expression-module source applicability | not_applicable | False | naturalproductmech:mibig-bc49771bdc | No expression-module/regulatory claim is used to substantiate this record; primary biochemical evidence is assessed directly. No database-coverage absence claim is made. |

## Scientific And Domain Assessments

### Exact isonitrile structure and internal stereochemical consistency

identity: supported. Targets: naturalproductmech:mibig-bc49771bdc.

The record represents the named chlorinated isonitrile with a chemically consistent SMILES/InChI/InChIKey set and three assigned stereocentres. Official NPAtlas, CyanoMetDB, ChEBI and PubChem agree on the full stereochemical key.

### NPAtlas and CyanoMetDB chemical equivalence

identity: supported. Targets: naturalproductmech:mibig-bc49771bdc.

Both asserted chemical xrefs resolve to the exact named full-key structure. NPAtlas accepts NPA04901 and identifies canonical NPA004901; the short form is a working alias, so no broken-reference finding is inferred from its padding.

### Primary absolute configuration and explicit atom mapping

evidence: supported. Targets: naturalproductmech:mibig-bc49771bdc.

The later enantiospecific synthesis explicitly uses the correct natural enantiomer and labels the exact isonitrile as 12-epi-fischerindole I(21). Transcription of all three stereochemical bonds in Scheme13 reproduces the owner full InChIKey; the published drawing and encoded configuration agree.

Mapped natural-product C12, C13 and C15 to record RDKit atoms7,5,3 respectively. Observed methyl toward viewer, chlorine away and hydrogen toward viewer recover S,R,S. The record connectivity was reused only after every existing stereo tag was removed. The later primary source supplies the absolute-enantiomer correlation beyond the 1994 relative-configuration abstract.

### Minted identity under the current repository rule

grounding: supported. Targets: naturalproductmech:mibig-bc49771bdc.

The pinned eligible ChEBI inventory has no matching structure and the directly inspected current CHEBI:202147 entry has two stars. Retaining MINTED is consistent with the repository three-star grounding rule.

### Three occurrence objects, two unique source publications

evidence: concern. Targets: naturalproductmech:mibig-bc49771bdc.

The 1994 isolation reference is relevant and shared by LOTUS and CyanoMetDB; those are two database routes to one publication. The 1990 LOTUS citation resolves but exact-compound support was not established. All occurrences remain distinct from the strain-level producer claim.

### Active compound-specific MIBiG entry, sequence and strain identity

grounding: supported. Targets: naturalproductmech:mibig-bc49771bdc.

The exact compound is listed in the active version 5 source, the sequence accession resolves, and source taxonomy matches the strain in the record. Terpene/other are the source’s asserted cluster classes; the omitted numeric bounds accurately reflect unspecified MIBiG bounds.

### Exact-congener scope and citation routing of demonstrated locus evidence

evidence: concern. Targets: naturalproductmech:mibig-bc49771bdc.

The sole cluster citation is the target’s chemical-isolation/NMR reference, while inspected pathway experiments concern precursors, a related welwitindolinone, or other fischerindole/hapalindole congeners. Exact-product CLUSTER_DEMONSTRATED is not substantiated by the evidence inspected. Retain native producer SOURCE_ASSERTION; the 2014 strain work was xenic and is not an axenic production demonstration.

### Computed filing versus asserted BGC class

provenance: supported. Targets: naturalproductmech:mibig-bc49771bdc.

Pinned NPClassifier output is explicitly marked computed and matches the exact-key inventory; ALKALOIDS agrees with the filing pin. TERPENE/OTHER separately retain MIBiG biosynthetic class assertions and are not replaced by computed chemical classes.

### Optional claims, complete mechanism and scientific status

scope: not_applicable. Targets: naturalproductmech:mibig-bc49771bdc.

The complete owner has no declared graph components or optional mechanism, target, activity, clinical or cross-corpus assertions to audit. Their absence alone is not a defect. The two seed events and SEEDED status do not claim scientific sign-off and remain unchanged.

## Findings

### O-SUSPICIOUS-CITATION: One LOTUS occurrence points to a different chemical-family paper

major / open / provisional; issue key: lotus-zvbczygmkqojfw-ja00166a066-occurrence-citation.

The second LOTUS occurrence cites DOI:10.1021/JA00166A066, whose authoritative metadata identifies a paracyclophane paper. Inspected sources did not establish this exact fischerindole occurrence in that paper. Because full text was unavailable, this is a provisional citation mismatch requiring inspection before withdrawal, not a confirmed assertion that the compound is absent from the species.

### bgc-claim-scope: Cluster demonstration reuses an isolation citation and lacks exact-congener experimental support

major / open / confirmed; issue key: mibig-bgc0000668-compound5-link-evidence.

BGC0000668:5 inherits entry-level enzymatic/heterologous methods but cites only the compound’s 1994 NMR/isolation DOI. The source’s actual pathway references are omitted. The inspected 2014 cluster study demonstrates common precursor formation and a different welwitindolinone methylation; its fischerindole oxidative steps remain proposed. The halogenase paper’s accessible abstract concerns other congeners. Thus the current claim-specific citation is misrouted, and the strong exact-product grade needs adjudication rather than automatic inheritance. This finding does not deny the plausible wel-pathway association or assert that no later exact-product study exists.

## Recommended Actions And Acceptance Checks

### O-VERIFY-CITATION

Inspect the complete 1990 article and any relevant supplementary material for this exact compound and taxon. If the triple is unsupported, add a full-row-pinned exclusion for the literal imported DOI, retain the supported 1994 assertions, and regenerate through the guarded seeder. Do not substitute a plausible DOI without exact source evidence.

- A cited full-text passage establishes exact compound/taxon support, or a reviewed exclusion removes only key ZVBCZYGMKQOJFW-QDUSTFBWSA-N / taxon NCBITaxon:162986 / DOI:10.1021/JA00166A066.
- The 1994 LOTUS and CyanoMetDB provenance and native producer claim remain separately scoped; run just seed-canary naturalproductmech:mibig-bc49771bdc, just validate-strict data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml, just verify-reproduction, just verify-corpus --summary, and just qc.

### reconcile-wel-target-evidence

Review BGC0000668:5 with the primary pathway and isolation literature. Use the implemented source-pinned claim-reference table to route the locus claim to actual biosynthetic sources, preserving the isolation citation where appropriate. Separately adjudicate whether entry-wide methods apply to this exact congener and qualify or withdraw inapplicable methods through the implemented locus-evidence override; a reference-only correction must not silently certify CLUSTER_DEMONSTRATED. Preserve SOURCE_ASSERTION and document xenic culture limitations. Do not infer a new strain ID or use unimplemented decisions.tsv.

- A reviewer can identify the exact experimental product, enzyme/locus and strain for every retained demonstration claim; precursor or related-congener results remain explicitly scoped.
- Producer and locus references are individually justified; the isolation DOI is not the sole support for a modern locus experiment.
- Use just seed-canary naturalproductmech:mibig-bc49771bdc, inspect output, then documented seeding and just validate-strict data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml, just verify-reproduction, just verify-corpus --summary and just qc.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-IDENTITY-LOCAL | data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml; Complete owner; chemical_structure, xrefs, source_concepts and grounding_status | supports | Read the entire exact owner. It encodes the isonitrile, three assigned stereocentres and Standard InChIKey ZVBCZYGMKQOJFW-QDUSTFBWSA-N, with MIBiG provenance and two chemical database xrefs. |
| E-NPATLAS | https://www.npatlas.org/api/v1/compound/NPA004901?include=classifications; npaid, original_name, inchikey, inchi, smiles, origin_reference, mol_structures and reassignments; official JSON linked from https://www.npatlas.org/explore/compounds/NPA04901 | supports | The literal stored short accession NPA04901 resolves on the official site to canonical NPA004901, named 12-epi-Fischerindole I isonitrile. The complete InChI and key match the record, including stereochemical layers. Current structure cites DOI:10.1021/ja00101a015; reassignments is empty. The page reports database version 2024_09. |
| E-CYANOMETDB-SOURCE | https://zenodo.org/records/13854577/files/CyanoMetDB_V03_2024.csv?download=1; Exact row CyanoMetDB_Identifier=CyanoMetDB_1565; columns CompoundName, NPAtlas_ID, SMILES_isomeric, InChI, InChlKey, DOI_No1 and NMR_used | supports | Official v03 source row names the exact compound, has full key ZVBCZYGMKQOJFW-QDUSTFBWSA-N, canonical NPAtlas_ID=NPA004901 and original-isolation DOI:10.1021/ja00101a015. The downloaded source SHA256 matches the committed MANIFEST.yaml source pin. Its NMR_used=yes flag is a database annotation, not independent spectral verification. |
| E-CHEBI-IDENTITY | https://www.ebi.ac.uk/chebi/backend/api/public/compound/202147/; chebi_accession, name, stars, default_structure and chemical_data | supports | CHEBI:202147 names the exact compound and supplies the same Standard InChI and full stereochemical key, formula C21H21ClN2 and neutral charge. The entry has two stars and therefore does not qualify for the repository three-star grounding rule. |
| E-PUBCHEM-CONTEXT | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/11624200/property/InChIKey,InChI,CanonicalSMILES/JSON; PropertyTable.Properties[0]; CID 11624200 discovered from CyanoMetDB_1565 | supports | The official PubChem response gives the identical full InChI and key. This is an additional identity cross-check; CID 11624200 is not an xref currently asserted by the owner. |
| E-SYNTHESIS-2008 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2634302/; Richter et al., DOI:10.1021/ja806981k; section discussing compound 21 and Scheme 13; footnotes 61 and 63; directly retrieved complete PMC HTML | supports | The primary synthesis explicitly identifies compound 21 as 12-epi-fischerindole I. It distinguishes earlier ent-G experiments using (R)-carvone oxide from the later sequence using (S)-carvone oxide to obtain the natural-product enantiomer. Thus the 1994 relative-configuration abstract is not the entire stereochemical evidence base. |
| E-SYNTHESIS-FIGURE | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3f16/2634302/6aaddef7b850/nihms-86646-f0020.jpg; Scheme 13, bottom product 21; visual inspection of published structure and isonitrile linkage | supports | The published scheme explicitly labels product 21 as 12-epi-fischerindole I and draws its isonitrile connectivity and stereochemistry. This is the named isonitrile, not the later nitrile congener. |
| E-CHEMISTRY-IDENTITY | /private/tmp/npm-review-work/002/chemistry.json; Root-agent RDKit 2026.03.5 calculation, generated 2026-10-21T06:43:33.402246Z; inspected result | supports | Calculated Standard InChI and full key match the record. Formula C21H21ClN2, charge 0 and exact mass 336.139326352 agree with database values. Three chiral centres are assigned and none is reported unassigned. This establishes representation consistency, not an experimental absolute assignment. |
| E-GROUNDING-SEARCH | data/raw/chebi_structures.tsv; Entire eligible pinned inventory searched for exact key, label and slug | context_only | No exact-key, label or slug hit in the committed eligible inventory. This agrees with the minted identity rationale and the directly checked current two-star entry; it does not establish absence from every current ChEBI entry. |
| E-GROUNDING-POLICY | docs/HARMONIZATION.md; Identity resolution: unambiguous three-star default-structure rule | supports | Only an unambiguous matching three-star ChEBI default structure grounds automatically; a lower-tier exact entry does not require replacing the minted identifier. |
| E-STEREO-MAPPING | /private/tmp/npm-review-work/002/stereo-mapping.json; Manual transcription of Scheme13 compound21, cross-checked with native RDKit labelled depiction | supports | All existing stereo tags were removed before transcribing the published bond directions. Natural-product C12 maps to zero-based RDKit atom7 and its methyl bond is a solid wedge; C13 maps to atom5 and its chlorine bond is hashed; C15 maps to atom3 and its hydrogen bond is solid. RDKit assigns S,R,S respectively and regenerates the exact owner InChI and key ZVBCZYGMKQOJFW-QDUSTFBWSA-N. The computation compares the published drawing with the encoded structure; it is not a new experimental stereochemical determination. |
| O-LOTUS | data/raw/lotus_occurrences.tsv; Rows with key ZVBCZYGMKQOJFW-QDUSTFBWSA-N, taxon NCBITaxon:162986, DOI:10.1021/JA00101A015 and 10.1021/JA00166A066 | context_only | Both exact-key structure–taxon–DOI triples are in the source inventory and emitted unchanged as database assertions. The second reference needs the separate source-scope assessment below. |
| O-PRIMARY-1994 | https://pure.psu.edu/en/publications/welwitindolinones-unusual-alkaloids-from-the-blue-green-algae-hap/; Authors institutional abstract, DOI:10.1021/ja00101a015, lines 23–26 | partial | The authors report fischerindoles among minor compounds from Hapalosiphon welwitschii UHIC-52-3 and assign their relative structures spectroscopically. The abstract does not enumerate every fischerindole name; exact I-congener linkage is additionally checked against compound-specific source entries. The X-ray absolute assignment in this abstract concerns compound 7, not every co-isolated compound. |
| O-CROSSREF-1990 | https://api.crossref.org/works/10.1021/ja00166a066; message.DOI,title,published,page | context_only | The cited DOI resolves to Moore et al., [7.7]Paracyclophanes from blue-green algae, JACS 112:4061–4063(1990). This title is a different chemical family from the target. Metadata alone does not prove the complete absence of a supporting statement; the full article could not be inspected. |
| O-CROSSREF-1994 | https://api.crossref.org/works/10.1021/ja00101a015; message.DOI,title,published,page | supports | DOI resolves to Stratmann et al., Welwitindolinones, Unusual Alkaloids from the Blue-Green Algae Hapalosiphon welwitschii and Westiella intricata. Relationship to Fischerindoles and Hapalinodoles, JACS 116:9935–9942(1994). DOI case differences in imported observations identify this same publication. |
| O-WIKIDATA | https://www.wikidata.org/wiki/Special:EntityData/Q67340456.json; entity Q67340456 revision 2543823250, label/en and claims P225/P685 | supports | The provenance URI resolves to Hapalosiphon welwitschii and NCBI Taxonomy 162986, matching both imported occurrence taxa. |
| O-SEARCH-LIMIT | Public web search and official ACS URLs; DOI/title searches and article/PDF access attempts on 2026-10-21 | unknown | The 1990 full text remained unavailable after publisher article/abstract/PDF requests and an indexed PDF mirror failed. No paid access was attempted. Search snippets were not treated as occurrence proof. |
| O-CORRECTION-OWNER | docs/CURATION.md; LOTUS occurrence exclusions; curation/lotus_occurrence_exclusions.tsv header and implemented pinned-row semantics | supports | A verified unsupported triple can be withheld through the exact-key/taxon/literal-DOI exclusion table with a full source-row digest and inspected reference. Current ignored-file-independent searches found no existing correction for this exact key, identifier or label. |
| bgc-v5-source | https://mibig.secondarymetabolites.org/repository/BGC0000668.5/annotations.json; compounds[4]; loci[0]; taxonomy; biosynthesis.classes; legacy_references | supports | Inspected complete JSON. BGC0000668 version 5 is active, questionable quality, complete, with twelve listed compounds. The exact target is compound index 5 with matching structure and an NMR reference DOI:10.1021/ja00101a015. The KF811479.1 locus has Enzymatic assays and Heterologous expression methods without method-level citations and zero/zero unspecified bounds. Taxonomy is 1433842, Hapalosiphon welwitschii UTEX B 1830. Classes are terpene/Monoterpene and other (converted from Alkaloid). Separate entry references are PMID:24677572 and PMID:25218740. |
| bgc-kf811479 | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KF811479.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text; LOCUS/DEFINITION/ACCESSION/VERSION; source feature; REFERENCE1 | supports | GenBank resolves KF811479.1 to a 36,570 bp partial indolinone biosynthetic cluster sequence from Hapalosiphon welwitschii UTEX B 1830, taxon 1433842. The source feature explicitly states strain UTEX B 1830. Reference 1 is Hillwig et al., ChemBioChem 15:665–669 (2014), PMID:24677572. The raw 0/0 MIBiG bounds are not real genomic coordinates and are appropriately omitted by the record. |
| bgc-taxon-1433842 | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&amp;id=1433842&amp;lvl=&amp;mode=node; Current name, Taxonomy ID, equivalent name, rank and lineage | supports | Direct NCBI taxonomy text resolves 1433842 to Hapalosiphon welwitschii UTEX B 1830, with equivalent name Hapalosiphon welwitschii UTEX 1830 and no-rank status below species Hapalosiphon welwitschii. This is the record’s strain-level source taxon. |
| bgc-primary24677572 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4382313/; Full article main text, strain selection and cluster assembly paragraphs; Figures 3–5 and associated results; Experimental Section; DOI:10.1002/cbic.201300794 / PMID:24677572 | partial | The authors studied xenic UTEX B 1830, profiled metabolites by HPLC/UV/HRMS and assembled the 36 kb wel locus. WelI1–3 expressed in E. coli generated the common indole-isonitrile precursor; WelP2 supplied GPP, and WelM methylated welwitindolinone C isothiocyanate. Oxidative transformations involving fischerindoles and WelO1–4 remained proposals. These experiments support pathway association but do not report heterologous production or enzymatic formation of this exact fischerindole I congener. |
| bgc-primary25218740 | https://www.nature.com/articles/nchembio.1625; Public primary-paper abstract; Hillwig and Liu, Nature Chemical Biology 10:921–923 (2014), DOI:10.1038/nchembio.1625 / PMID:25218740 | partial | The inspected abstract specifies WelO5 monochlorination of free 12-epi-fischerindole U and 12-epi-hapalindole C. It does not describe direct formation of 12-epi-fischerindole I isonitrile. This is congener/step evidence, not an exact-product demonstration for the reviewed structure. |
| bgc-local-routing | scripts/extract_mibig.py; scripts/seed_from_sources.py; data/raw/mibig_compounds.tsv; docs/CURATION.md; extract_mibig.py primary_reference() and extract loop; seed_from_sources.py claim evidence emission; mibig_compounds.tsv row 793/BGC0000668 compound_index 5; CURATION claim-specific references and locus overrides | supports | The extractor prioritizes the compound’s structure reference and stores one primary_reference while copying entry-level locus methods to each compound. The exact raw row therefore pairs COMPOUND_EVIDENCE DOI:10.1021/ja00101a015 with CLUSTER_DEMONSTRATED. The generated producer and cluster both reuse that citation. Implemented claim-reference correction and locus-evidence override tables provide separate maintained correction paths. |
| R-LOCAL | data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml; Complete generated owner and read_natural_product resolved representation; exact-key committed source rows | supports | The full owner has one MIBiG compound concept, three occurrence objects, two exact chemical xrefs and one active source cluster. It remains SEEDED with two seed events. NPClassifier row yields Alkaloids/Tryptophan alkaloids/Hapalindole alkaloids with model version npclassifier.gnps2.org@2026-09-07. No pathways, targets, bioactivities, bioactivity_summary, causal_graphs, causal_graph_refs, related-record or clinical assertions are present. |

## Limits And Additional Notes

- Published drawing-to-structure stereochemistry was checked by explicit atom mapping and a stereo-stripped reconstruction. The synthesis enantiomer correlation is source evidence; no optical rotations were remeasured and no spectra or crystallographic data were independently reinterpreted.
- Primary synthesis access was recovered through a normal direct retrieval of complete PMC HTML after the web renderer returned a challenge and the Europe PMC full-text service returned an error. No challenge bypass or paid access was used. The 2005 institutional PDF lead failed TLS verification; no conclusions rely on its uninspected content.
- The ChEBI absence search covers the complete pinned eligible inventory with ignored-file exclusions disabled, plus direct inspection of CHEBI:202147. It does not claim an exhaustive current-ontology search.
- The 1990 LOTUS citation was resolved bibliographically but its complete article could not be inspected; exact occurrence support remains unresolved. The 1994 institutional abstract was read, but the original full isolation methods were not accessible.
- The main text of PMID:24677572 was fully inspected, but supplementary PDFs and figure images remained inaccessible through attempted free readers. Exact chromatogram assignments were not independently re-read.
- PMID:25218740 was inspected at primary abstract level; full text was paywalled and no paid access was used.
- A bounded web search used exact target name with biosynthesis/enzyme and WelO/WelO1 terms. It did not establish exhaustive absence of later exact-target experiments.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- The configured ontology check skips unsupported adapters and allows taxon-label warnings; its success is not universal external identifier verification.
- No scientific owner, source inventory, graph, status or history was edited. All corrective actions are proposed work only.
- LOTUS and CyanoMetDB cite the same 1994 paper through distinct database routes; this does not establish independent experimental corroboration.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T065538Z-12-epi-fischerindole-i-isonitrile
kind: record
repository: CultureBotAI/NaturalProductMech
title: '12-epi-fischerindole I isonitrile: identity and claim-specific source review'
started_at: '2026-10-21T06:42:58.663376Z'
finished_at: '2026-10-21T06:55:38.396895Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This review team did not author or modify the selected owner
    or maintained source tables. Parallel source inspections were reconciled by the
    parent reviewer; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact encoded structure and both chemical xrefs agree across inspected
  sources. The BGC claim reuses an isolation reference and inherits experiments whose
  exact-congener scope needs adjudication. A second LOTUS citation resolves to a different
  chemical-family paper; its support remains unverified because full text was unavailable.
  This is a partial scientific review with actionable evidence findings, not native
  REVIEWED status.
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
  - path: data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml
    sha256: e1d9ccc2cb88dcf9aeabcfd71160abb187f9231a55172ad681805ed77f8fbd2b
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
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
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One full generated owner and its complete resolved mechanism; source
    support is partial where primary text could not be accessed.
  selection: 'Second unreviewed path after the initial validated list: 91 bundles
    covered 54 of 3,116 corpus records; 3,062 remained. Selected deterministically
    in path order, one target per bundle. The helper includes ignored review bundles.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-bc49771bdc
targets:
- target_id: naturalproductmech:mibig-bc49771bdc
  path: data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml
  label: 12-epi-fischerindole I isonitrile
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: MIBiG seed identity, producer and cluster source
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Occurrence source
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated record transform
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: CyanoMetDB occurrence source
checks:
- check_id: C-STRICT
  name: Closed-schema and component validation
  status: passed
  required: true
  summary: One full record validated with zero ERROR rows.
  command: just validate-strict data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml
    --out /private/tmp/npm-review-work/002/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned
    filing pathways.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016808+00:00; finished 2026-10-21T06:37:52.997020+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/verify-corpus.log.'
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3,116 records are byte-identical to the seeder output from committed
    inventories and maintained curation inputs.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-reproduction
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016703+00:00; finished 2026-10-21T06:38:35.570687+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/verify-reproduction.log.'
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The documented exhaustive queue command produced 8,928 diagnostic rows
    in 12 queues; deterministic queue output does not establish scientific review.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just review-queue
    --tsv /private/tmp/npm-review-queue-initial.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016598+00:00; finished 2026-10-21T06:37:11.018366+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/review-queue.log.'
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'Full configured gate passed using existing CHEBI and GO caches plus the
    committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35
    documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because
    their prefixes have no adapter.'
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.498212+00:00; finished 2026-10-21T06:38:54.776253+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/validate-products.log.'
- check_id: qc-environment-attempt1
  name: Initial QC attempt before installing the pinned linter
  status: failed
  required: false
  summary: The first full QC invocation stopped at lint because the isolated copied
    Python environment lacked Ruff. Exact uv.lock version Ruff 0.16.6 was subsequently
    installed and lint passed on later invocations.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.497107+00:00; finished 2026-10-21T06:36:56.918133+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/qc.log.'
- check_id: qc-network-attempt2
  name: QC attempt without network access
  status: failed
  required: false
  summary: After Ruff installation, QC passed lint and stopped at vendored-sync because
    sandbox DNS could not reach the pinned public CLAW governance source. Approved
    network access allowed the next invocation to verify all 22 governed artifacts.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:37:57.661447+00:00; finished 2026-10-21T06:37:59.874785+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/qc-attempt2.log.'
- check_id: qc-tag-attempt3
  name: QC attempt before restoring the required provenance tag
  status: failed
  required: false
  summary: 'QC passed lint, vendored sync, documentation, provenance and source queue,
    then stopped at tests: 998 passed, 1 failed, 4 skipped. The sole failure was the
    isolated clone lacking refs/tags/review-base/gentamicin-20261013; it was not a
    failed archive-content assertion. The tag was subsequently fetched from origin.'
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:38:17.713062+00:00; finished 2026-10-21T06:45:43.079802+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/qc-attempt3.log.'
- check_id: qc-tag-remediation
  name: Targeted verification after restoring the provenance tag
  status: passed
  required: false
  summary: After restoring the required tag, the exact previously failed gentamicin
    archive test passed (1 passed). No repository content was edited for this remediation.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just test -q
    tests/test_gentamicin_review_archive.py::test_gentamicin_archive_and_scoped_dispositions
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:45:52.383490+00:00; finished 2026-10-21T06:45:54.030116+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/gentamicin-tag-check.log.'
- check_id: qc-skip-diagnosis
  name: Diagnosis of the suite skip conditions
  status: passed
  required: false
  summary: 'The four observed skip cases were reproduced with pytest skip reasons
    enabled: the optional sibling AntibioticMech comparison has no sibling checkout
    in the isolated clone, and three command-frontmatter tests have empty parameter
    sets. This diagnostic invocation executed no passing tests; it reported four skips.'
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just test -q
    -rs tests/test_schema.py::test_shared_mech_modules_are_byte_identical_to_the_fleet
    tests/test_skill_frontmatter.py::test_command_frontmatter_has_no_duplicate_keys
    tests/test_skill_frontmatter.py::test_command_frontmatter_is_valid_yaml tests/test_skill_frontmatter.py::test_command_declares_a_usable_description
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:30.259937+00:00; finished 2026-10-21T06:46:31.251048+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/skipped-tests-diagnosis.log.'
- check_id: shared-qc
  name: Full repository quality gate after environment repair
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed after installing the pinned
    linter, allowing the read-only governance fetch, and restoring the required provenance
    tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116
    records and zero errors. Documentation, provenance, source queue, governed artifacts,
    generated pages, reproduction, filing integrity and corpus reporting all passed.'
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:02.058886+00:00; finished 2026-10-21T06:54:53.950582+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/qc-attempt4.log.'
- check_id: C-OCCURRENCE-PRIMARY
  name: Full source support for 1990 occurrence citation
  status: unavailable
  required: true
  summary: DOI metadata resolves; full cited article could not be accessed via attempted
    free routes, leaving exact target/taxon support unresolved.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  evidence_ids:
  - O-CROSSREF-1990
  - O-SEARCH-LIMIT
- check_id: C-IMODULON
  name: Expression-module source applicability
  status: not_applicable
  required: false
  summary: No expression-module/regulatory claim is used to substantiate this record;
    primary biochemical evidence is assessed directly. No database-coverage absence
    claim is made.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
evidence:
- evidence_id: E-IDENTITY-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml
  locator: Complete owner; chemical_structure, xrefs, source_concepts and grounding_status
  accessed_at: '2026-10-21T06:43:12Z'
  support: supports
  summary: Read the entire exact owner. It encodes the isonitrile, three assigned
    stereocentres and Standard InChIKey ZVBCZYGMKQOJFW-QDUSTFBWSA-N, with MIBiG provenance
    and two chemical database xrefs.
  snapshot_sha256: e1d9ccc2cb88dcf9aeabcfd71160abb187f9231a55172ad681805ed77f8fbd2b
- evidence_id: E-NPATLAS
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA004901?include=classifications
  locator: npaid, original_name, inchikey, inchi, smiles, origin_reference, mol_structures
    and reassignments; official JSON linked from https://www.npatlas.org/explore/compounds/NPA04901
  accessed_at: '2026-10-21T06:43:53Z'
  support: supports
  summary: The literal stored short accession NPA04901 resolves on the official site
    to canonical NPA004901, named 12-epi-Fischerindole I isonitrile. The complete
    InChI and key match the record, including stereochemical layers. Current structure
    cites DOI:10.1021/ja00101a015; reassignments is empty. The page reports database
    version 2024_09.
- evidence_id: E-CYANOMETDB-SOURCE
  kind: database
  reference: https://zenodo.org/records/13854577/files/CyanoMetDB_V03_2024.csv?download=1
  locator: Exact row CyanoMetDB_Identifier=CyanoMetDB_1565; columns CompoundName,
    NPAtlas_ID, SMILES_isomeric, InChI, InChlKey, DOI_No1 and NMR_used
  accessed_at: '2026-10-21T06:43:53Z'
  support: supports
  summary: Official v03 source row names the exact compound, has full key ZVBCZYGMKQOJFW-QDUSTFBWSA-N,
    canonical NPAtlas_ID=NPA004901 and original-isolation DOI:10.1021/ja00101a015.
    The downloaded source SHA256 matches the committed MANIFEST.yaml source pin. Its
    NMR_used=yes flag is a database annotation, not independent spectral verification.
  snapshot_sha256: 91aa57146c9e803d5eeef656fc0e5cfc8f804531b1b83718757e96aa848a4121
- evidence_id: E-CHEBI-IDENTITY
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/202147/
  locator: chebi_accession, name, stars, default_structure and chemical_data
  accessed_at: '2026-10-21T06:43:53Z'
  support: supports
  summary: CHEBI:202147 names the exact compound and supplies the same Standard InChI
    and full stereochemical key, formula C21H21ClN2 and neutral charge. The entry
    has two stars and therefore does not qualify for the repository three-star grounding
    rule.
- evidence_id: E-PUBCHEM-CONTEXT
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/11624200/property/InChIKey,InChI,CanonicalSMILES/JSON
  locator: PropertyTable.Properties[0]; CID 11624200 discovered from CyanoMetDB_1565
  accessed_at: '2026-10-21T06:44:02Z'
  support: supports
  summary: The official PubChem response gives the identical full InChI and key. This
    is an additional identity cross-check; CID 11624200 is not an xref currently asserted
    by the owner.
- evidence_id: E-SYNTHESIS-2008
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2634302/
  locator: Richter et al., DOI:10.1021/ja806981k; section discussing compound 21 and
    Scheme 13; footnotes 61 and 63; directly retrieved complete PMC HTML
  accessed_at: '2026-10-21T06:44:46Z'
  support: supports
  summary: The primary synthesis explicitly identifies compound 21 as 12-epi-fischerindole
    I. It distinguishes earlier ent-G experiments using (R)-carvone oxide from the
    later sequence using (S)-carvone oxide to obtain the natural-product enantiomer.
    Thus the 1994 relative-configuration abstract is not the entire stereochemical
    evidence base.
  snapshot_sha256: 34db36ed0e8abad24d65270507186f601a45e0ae8fc7576c633a075c08f2a83b
- evidence_id: E-SYNTHESIS-FIGURE
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3f16/2634302/6aaddef7b850/nihms-86646-f0020.jpg
  locator: Scheme 13, bottom product 21; visual inspection of published structure
    and isonitrile linkage
  accessed_at: '2026-10-21T06:44:50Z'
  support: supports
  summary: The published scheme explicitly labels product 21 as 12-epi-fischerindole
    I and draws its isonitrile connectivity and stereochemistry. This is the named
    isonitrile, not the later nitrile congener.
  snapshot_sha256: 3b5fa59b195b2bce35f889ac86c87da705ef877011dab7016365bf1881650c86
- evidence_id: E-CHEMISTRY-IDENTITY
  kind: validation
  reference: /private/tmp/npm-review-work/002/chemistry.json
  locator: Root-agent RDKit 2026.03.5 calculation, generated 2026-10-21T06:43:33.402246Z;
    inspected result
  accessed_at: '2026-10-21T06:45:28Z'
  support: supports
  summary: Calculated Standard InChI and full key match the record. Formula C21H21ClN2,
    charge 0 and exact mass 336.139326352 agree with database values. Three chiral
    centres are assigned and none is reported unassigned. This establishes representation
    consistency, not an experimental absolute assignment.
  snapshot_sha256: d0f5bf57df3927f9935a05a4b6163b58df08409e0e75e9ab457f1dc4d4a8b7cf
- evidence_id: E-GROUNDING-SEARCH
  kind: search
  reference: data/raw/chebi_structures.tsv
  locator: Entire eligible pinned inventory searched for exact key, label and slug
  accessed_at: '2026-10-21T06:45:28Z'
  support: context_only
  summary: No exact-key, label or slug hit in the committed eligible inventory. This
    agrees with the minted identity rationale and the directly checked current two-star
    entry; it does not establish absence from every current ChEBI entry.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
  search_scope: On 2026-10-21 ran rg --no-ignore --hidden -n -F -e ZVBCZYGMKQOJFW-QDUSTFBWSA-N
    -e 12-epi-Fischerindole I isonitrile -e 12-epi-fischerindole-i-isonitrile data/raw/chebi_structures.tsv.
    Entire explicit file searched with ignored-file exclusions disabled; exit 1 signifies
    no matches.
- evidence_id: E-GROUNDING-POLICY
  kind: authority
  reference: docs/HARMONIZATION.md
  locator: 'Identity resolution: unambiguous three-star default-structure rule'
  accessed_at: '2026-10-21T06:45:28Z'
  support: supports
  summary: Only an unambiguous matching three-star ChEBI default structure grounds
    automatically; a lower-tier exact entry does not require replacing the minted
    identifier.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: E-STEREO-MAPPING
  kind: validation
  reference: /private/tmp/npm-review-work/002/stereo-mapping.json
  locator: Manual transcription of Scheme13 compound21, cross-checked with native
    RDKit labelled depiction
  accessed_at: '2026-10-21T06:48:43.559432Z'
  support: supports
  summary: All existing stereo tags were removed before transcribing the published
    bond directions. Natural-product C12 maps to zero-based RDKit atom7 and its methyl
    bond is a solid wedge; C13 maps to atom5 and its chlorine bond is hashed; C15
    maps to atom3 and its hydrogen bond is solid. RDKit assigns S,R,S respectively
    and regenerates the exact owner InChI and key ZVBCZYGMKQOJFW-QDUSTFBWSA-N. The
    computation compares the published drawing with the encoded structure; it is not
    a new experimental stereochemical determination.
  snapshot_sha256: 9ab7a340a26892fe3c5dd071dff958dfab660af5dead9a9de92cac2fd3e31939
- evidence_id: O-LOTUS
  kind: database
  reference: data/raw/lotus_occurrences.tsv
  locator: Rows with key ZVBCZYGMKQOJFW-QDUSTFBWSA-N, taxon NCBITaxon:162986, DOI:10.1021/JA00101A015
    and 10.1021/JA00166A066
  accessed_at: '2026-10-21T06:43:33Z'
  support: context_only
  summary: Both exact-key structure–taxon–DOI triples are in the source inventory
    and emitted unchanged as database assertions. The second reference needs the separate
    source-scope assessment below.
- evidence_id: O-PRIMARY-1994
  kind: primary_source
  reference: https://pure.psu.edu/en/publications/welwitindolinones-unusual-alkaloids-from-the-blue-green-algae-hap/
  locator: Authors institutional abstract, DOI:10.1021/ja00101a015, lines 23–26
  accessed_at: '2026-10-21T06:43:40Z'
  support: partial
  summary: The authors report fischerindoles among minor compounds from Hapalosiphon
    welwitschii UHIC-52-3 and assign their relative structures spectroscopically.
    The abstract does not enumerate every fischerindole name; exact I-congener linkage
    is additionally checked against compound-specific source entries. The X-ray absolute
    assignment in this abstract concerns compound 7, not every co-isolated compound.
- evidence_id: O-CROSSREF-1990
  kind: authority
  reference: https://api.crossref.org/works/10.1021/ja00166a066
  locator: message.DOI,title,published,page
  accessed_at: '2026-10-21T06:44:51.286176Z'
  support: context_only
  summary: The cited DOI resolves to Moore et al., [7.7]Paracyclophanes from blue-green
    algae, JACS 112:4061–4063(1990). This title is a different chemical family from
    the target. Metadata alone does not prove the complete absence of a supporting
    statement; the full article could not be inspected.
- evidence_id: O-CROSSREF-1994
  kind: authority
  reference: https://api.crossref.org/works/10.1021/ja00101a015
  locator: message.DOI,title,published,page
  accessed_at: '2026-10-21T06:44:51.538552Z'
  support: supports
  summary: DOI resolves to Stratmann et al., Welwitindolinones, Unusual Alkaloids
    from the Blue-Green Algae Hapalosiphon welwitschii and Westiella intricata. Relationship
    to Fischerindoles and Hapalinodoles, JACS 116:9935–9942(1994). DOI case differences
    in imported observations identify this same publication.
- evidence_id: O-WIKIDATA
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q67340456.json
  locator: entity Q67340456 revision 2543823250, label/en and claims P225/P685
  accessed_at: '2026-10-21T06:44:23.635771Z'
  support: supports
  summary: The provenance URI resolves to Hapalosiphon welwitschii and NCBI Taxonomy
    162986, matching both imported occurrence taxa.
  snapshot_sha256: 53fdaac9788b1ac4ea420b9173248f248da507f8d3a1ab73fa39607f8c6cd4fb
- evidence_id: O-SEARCH-LIMIT
  kind: search
  reference: Public web search and official ACS URLs
  locator: DOI/title searches and article/PDF access attempts on 2026-10-21
  accessed_at: '2026-10-21T06:44:51Z'
  support: unknown
  summary: The 1990 full text remained unavailable after publisher article/abstract/PDF
    requests and an indexed PDF mirror failed. No paid access was attempted. Search
    snippets were not treated as occurrence proof.
  search_scope: 'Queries: exact DOI:10.1021/ja00166a066; exact paper title plus pdf;
    paracyclophanes 4061 pdf Moore. Official ACS endpoints returned 403 or inaccessible;
    electronicsandbooks PDF open timed out and direct request failed network reachability.
    This is a bounded access limitation, not a global absence claim.'
- evidence_id: O-CORRECTION-OWNER
  kind: authority
  reference: docs/CURATION.md
  locator: LOTUS occurrence exclusions; curation/lotus_occurrence_exclusions.tsv header
    and implemented pinned-row semantics
  accessed_at: '2026-10-21T06:45:03Z'
  support: supports
  summary: A verified unsupported triple can be withheld through the exact-key/taxon/literal-DOI
    exclusion table with a full source-row digest and inspected reference. Current
    ignored-file-independent searches found no existing correction for this exact
    key, identifier or label.
- evidence_id: bgc-v5-source
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000668.5/annotations.json
  locator: compounds[4]; loci[0]; taxonomy; biosynthesis.classes; legacy_references
  accessed_at: '2026-10-21T06:43:48Z'
  support: supports
  summary: Inspected complete JSON. BGC0000668 version 5 is active, questionable quality,
    complete, with twelve listed compounds. The exact target is compound index 5 with
    matching structure and an NMR reference DOI:10.1021/ja00101a015. The KF811479.1
    locus has Enzymatic assays and Heterologous expression methods without method-level
    citations and zero/zero unspecified bounds. Taxonomy is 1433842, Hapalosiphon
    welwitschii UTEX B 1830. Classes are terpene/Monoterpene and other (converted
    from Alkaloid). Separate entry references are PMID:24677572 and PMID:25218740.
- evidence_id: bgc-kf811479
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KF811479.1&db=nuccore&report=genbank&retmode=text
  locator: LOCUS/DEFINITION/ACCESSION/VERSION; source feature; REFERENCE1
  accessed_at: '2026-10-21T06:43:48Z'
  support: supports
  summary: GenBank resolves KF811479.1 to a 36,570 bp partial indolinone biosynthetic
    cluster sequence from Hapalosiphon welwitschii UTEX B 1830, taxon 1433842. The
    source feature explicitly states strain UTEX B 1830. Reference 1 is Hillwig et
    al., ChemBioChem 15:665–669 (2014), PMID:24677572. The raw 0/0 MIBiG bounds are
    not real genomic coordinates and are appropriately omitted by the record.
- evidence_id: bgc-taxon-1433842
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1433842&lvl=&mode=node
  locator: Current name, Taxonomy ID, equivalent name, rank and lineage
  accessed_at: '2026-10-21T06:45:11Z'
  support: supports
  summary: Direct NCBI taxonomy text resolves 1433842 to Hapalosiphon welwitschii
    UTEX B 1830, with equivalent name Hapalosiphon welwitschii UTEX 1830 and no-rank
    status below species Hapalosiphon welwitschii. This is the record’s strain-level
    source taxon.
- evidence_id: bgc-primary24677572
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4382313/
  locator: Full article main text, strain selection and cluster assembly paragraphs;
    Figures 3–5 and associated results; Experimental Section; DOI:10.1002/cbic.201300794
    / PMID:24677572
  accessed_at: '2026-10-21T06:45:11Z'
  support: partial
  summary: The authors studied xenic UTEX B 1830, profiled metabolites by HPLC/UV/HRMS
    and assembled the 36 kb wel locus. WelI1–3 expressed in E. coli generated the
    common indole-isonitrile precursor; WelP2 supplied GPP, and WelM methylated welwitindolinone
    C isothiocyanate. Oxidative transformations involving fischerindoles and WelO1–4
    remained proposals. These experiments support pathway association but do not report
    heterologous production or enzymatic formation of this exact fischerindole I congener.
  search_scope: Complete main article text and figure captions inspected. Supplementary
    PDF and figure images returned browser checks; exact supplementary chromatogram
    assignments were not independently inspected.
- evidence_id: bgc-primary25218740
  kind: primary_source
  reference: https://www.nature.com/articles/nchembio.1625
  locator: Public primary-paper abstract; Hillwig and Liu, Nature Chemical Biology
    10:921–923 (2014), DOI:10.1038/nchembio.1625 / PMID:25218740
  accessed_at: '2026-10-21T06:45:11Z'
  support: partial
  summary: The inspected abstract specifies WelO5 monochlorination of free 12-epi-fischerindole
    U and 12-epi-hapalindole C. It does not describe direct formation of 12-epi-fischerindole
    I isonitrile. This is congener/step evidence, not an exact-product demonstration
    for the reviewed structure.
  search_scope: Publisher abstract retrieved directly; full article is subscription
    content and was not purchased. EuropePMC PMID metadata confirms this reference
    and lack of an open full-text copy there.
- evidence_id: bgc-local-routing
  kind: record_content
  reference: scripts/extract_mibig.py; scripts/seed_from_sources.py; data/raw/mibig_compounds.tsv;
    docs/CURATION.md
  locator: extract_mibig.py primary_reference() and extract loop; seed_from_sources.py
    claim evidence emission; mibig_compounds.tsv row 793/BGC0000668 compound_index
    5; CURATION claim-specific references and locus overrides
  accessed_at: '2026-10-21T06:45:46Z'
  support: supports
  summary: The extractor prioritizes the compound’s structure reference and stores
    one primary_reference while copying entry-level locus methods to each compound.
    The exact raw row therefore pairs COMPOUND_EVIDENCE DOI:10.1021/ja00101a015 with
    CLUSTER_DEMONSTRATED. The generated producer and cluster both reuse that citation.
    Implemented claim-reference correction and locus-evidence override tables provide
    separate maintained correction paths.
  search_scope: Read code and table row; rg --no-ignore --hidden searched the exact
    identifier, compound label and BGC0000668:5 in curation, extractor, seeder and
    MIBiG inventory, including ignored files in these scoped paths.
- evidence_id: R-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml
  locator: Complete generated owner and read_natural_product resolved representation;
    exact-key committed source rows
  accessed_at: '2026-10-21T06:43:33Z'
  support: supports
  summary: The full owner has one MIBiG compound concept, three occurrence objects,
    two exact chemical xrefs and one active source cluster. It remains SEEDED with
    two seed events. NPClassifier row yields Alkaloids/Tryptophan alkaloids/Hapalindole
    alkaloids with model version npclassifier.gnps2.org@2026-09-07. No pathways, targets,
    bioactivities, bioactivity_summary, causal_graphs, causal_graph_refs, related-record
    or clinical assertions are present.
  snapshot_sha256: e1d9ccc2cb88dcf9aeabcfd71160abb187f9231a55172ad681805ed77f8fbd2b
assessments:
- assessment_id: A-IDENTITY-REPRESENTATION
  area: identity
  topic: Exact isonitrile structure and internal stereochemical consistency
  outcome: supported
  summary: The record represents the named chlorinated isonitrile with a chemically
    consistent SMILES/InChI/InChIKey set and three assigned stereocentres. Official
    NPAtlas, CyanoMetDB, ChEBI and PubChem agree on the full stereochemical key.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-NPATLAS
  - E-CYANOMETDB-SOURCE
  - E-CHEBI-IDENTITY
  - E-PUBCHEM-CONTEXT
  - E-CHEMISTRY-IDENTITY
  dimensions:
  - name: stereochemical_representation
    value: Three assigned centres; no unassigned centres in calculation
    definition: Completeness of the encoded representation, distinguished from experimental
      provenance for absolute configuration
    evidence_ids:
    - E-IDENTITY-LOCAL
    - E-CHEMISTRY-IDENTITY
  - name: standard_inchi_key
    value: ZVBCZYGMKQOJFW-QDUSTFBWSA-N
    definition: Full stereochemical structure key, not connectivity-block-only comparison
    evidence_ids:
    - E-IDENTITY-LOCAL
    - E-NPATLAS
    - E-CYANOMETDB-SOURCE
- assessment_id: A-XREF-EQUIVALENCE
  area: identity
  topic: NPAtlas and CyanoMetDB chemical equivalence
  outcome: supported
  summary: Both asserted chemical xrefs resolve to the exact named full-key structure.
    NPAtlas accepts NPA04901 and identifies canonical NPA004901; the short form is
    a working alias, so no broken-reference finding is inferred from its padding.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-NPATLAS
  - E-CYANOMETDB-SOURCE
  dimensions:
  - name: npatlas_version
    value: '2024_09'
    definition: Database version displayed on the inspected NPAtlas page
    evidence_ids:
    - E-NPATLAS
  - name: cyanometdb_version
    value: V03_2024; Zenodo 13854577
    definition: Exact source export, whose SHA256 matches the committed raw-source
      manifest
    evidence_ids:
    - E-CYANOMETDB-SOURCE
- assessment_id: A-PRIMARY-STEREOCHEMISTRY
  area: evidence
  topic: Primary absolute configuration and explicit atom mapping
  outcome: supported
  summary: The later enantiospecific synthesis explicitly uses the correct natural
    enantiomer and labels the exact isonitrile as 12-epi-fischerindole I(21). Transcription
    of all three stereochemical bonds in Scheme13 reproduces the owner full InChIKey;
    the published drawing and encoded configuration agree.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  evidence_ids:
  - E-SYNTHESIS-2008
  - E-SYNTHESIS-FIGURE
  - E-IDENTITY-LOCAL
  - E-STEREO-MAPPING
  details: Mapped natural-product C12, C13 and C15 to record RDKit atoms7,5,3 respectively.
    Observed methyl toward viewer, chlorine away and hydrogen toward viewer recover
    S,R,S. The record connectivity was reused only after every existing stereo tag
    was removed. The later primary source supplies the absolute-enantiomer correlation
    beyond the 1994 relative-configuration abstract.
  dimensions:
  - name: primary_stereo_mapping
    value: C12=atom7:S; C13=atom5:R; C15=atom3:S
    definition: Natural-product ring positions mapped to zero-based record RDKit indices
      by connectivity and published directed bonds
    evidence_ids:
    - E-SYNTHESIS-FIGURE
    - E-STEREO-MAPPING
- assessment_id: A-GROUNDING
  area: grounding
  topic: Minted identity under the current repository rule
  outcome: supported
  summary: The pinned eligible ChEBI inventory has no matching structure and the directly
    inspected current CHEBI:202147 entry has two stars. Retaining MINTED is consistent
    with the repository three-star grounding rule.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-CHEBI-IDENTITY
  - E-GROUNDING-SEARCH
  - E-GROUNDING-POLICY
- assessment_id: O-OCCURRENCES
  area: evidence
  topic: Three occurrence objects, two unique source publications
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  evidence_ids:
  - O-LOTUS
  - O-PRIMARY-1994
  - O-CROSSREF-1994
  - O-CROSSREF-1990
  - O-WIKIDATA
  summary: The 1994 isolation reference is relevant and shared by LOTUS and CyanoMetDB;
    those are two database routes to one publication. The 1990 LOTUS citation resolves
    but exact-compound support was not established. All occurrences remain distinct
    from the strain-level producer claim.
  dimensions:
  - name: occurrence_taxon
    value: Hapalosiphon welwitschii; NCBITaxon:162986
    definition: Species-level occurrence assertion rather than a strain-specific biosynthetic
      demonstration
    evidence_ids:
    - O-WIKIDATA
    - O-LOTUS
  - name: primary_isolation_context
    value: UHIC-52-3 in 1994 abstract; strain n.a. in CyanoMetDB imported observation
    definition: Preserve the distinction between published culture context and source
      missing-value text
    evidence_ids:
    - O-PRIMARY-1994
- assessment_id: bgc-identifiers-supported
  area: grounding
  topic: Active compound-specific MIBiG entry, sequence and strain identity
  outcome: supported
  summary: The exact compound is listed in the active version 5 source, the sequence
    accession resolves, and source taxonomy matches the strain in the record. Terpene/other
    are the source’s asserted cluster classes; the omitted numeric bounds accurately
    reflect unspecified MIBiG bounds.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  evidence_ids:
  - bgc-v5-source
  - bgc-kf811479
  - bgc-taxon-1433842
- assessment_id: bgc-claim-evidence-concern
  area: evidence
  topic: Exact-congener scope and citation routing of demonstrated locus evidence
  outcome: concern
  summary: The sole cluster citation is the target’s chemical-isolation/NMR reference,
    while inspected pathway experiments concern precursors, a related welwitindolinone,
    or other fischerindole/hapalindole congeners. Exact-product CLUSTER_DEMONSTRATED
    is not substantiated by the evidence inspected. Retain native producer SOURCE_ASSERTION;
    the 2014 strain work was xenic and is not an axenic production demonstration.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  evidence_ids:
  - bgc-v5-source
  - bgc-primary24677572
  - bgc-primary25218740
  - bgc-local-routing
  dimensions:
  - name: strain
    value: Hapalosiphon welwitschii UTEX B 1830; xenic culture
    definition: Strain and culture status used for the cluster-identification study
    evidence_ids:
    - bgc-primary24677572
    - bgc-kf811479
  - name: evidence_scope
    value: Precursor and related-congener enzyme experiments; exact target link unresolved
    definition: Experiment scope must match the reviewed individual structure before
      assigning demonstration
    evidence_ids:
    - bgc-primary24677572
    - bgc-primary25218740
- assessment_id: R-CLASSIFICATION
  area: provenance
  topic: Computed filing versus asserted BGC class
  outcome: supported
  summary: Pinned NPClassifier output is explicitly marked computed and matches the
    exact-key inventory; ALKALOIDS agrees with the filing pin. TERPENE/OTHER separately
    retain MIBiG biosynthetic class assertions and are not replaced by computed chemical
    classes.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  evidence_ids:
  - R-LOCAL
  - bgc-v5-source
- assessment_id: R-OPTIONAL-MECHANISM
  area: scope
  topic: Optional claims, complete mechanism and scientific status
  outcome: not_applicable
  summary: The complete owner has no declared graph components or optional mechanism,
    target, activity, clinical or cross-corpus assertions to audit. Their absence
    alone is not a defect. The two seed events and SEEDED status do not claim scientific
    sign-off and remain unchanged.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  evidence_ids:
  - R-LOCAL
findings:
- finding_id: O-SUSPICIOUS-CITATION
  issue_key: lotus-zvbczygmkqojfw-ja00166a066-occurrence-citation
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: One LOTUS occurrence points to a different chemical-family paper
  description: The second LOTUS occurrence cites DOI:10.1021/JA00166A066, whose authoritative
    metadata identifies a paracyclophane paper. Inspected sources did not establish
    this exact fischerindole occurrence in that paper. Because full text was unavailable,
    this is a provisional citation mismatch requiring inspection before withdrawal,
    not a confirmed assertion that the compound is absent from the species.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  field_paths:
  - occurrences[1].evidence[0].reference
  evidence_ids:
  - O-LOTUS
  - O-CROSSREF-1990
  - O-SEARCH-LIMIT
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Exact imported occurrence triple
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Implemented source-pinned occurrence withdrawal
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Occurrence emission
  rule_id: '.claude/skills/curate-yaml-record/references/review-checklist.md: Occurrences'
  native_severity: 'major: potentially unsupported compound-specific occurrence citation'
  normalization_reason: A material occurrence claim needs exact-compound support;
    certainty remains provisional because only bibliographic scope could be verified.
- finding_id: bgc-claim-scope
  issue_key: mibig-bgc0000668-compound5-link-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Cluster demonstration reuses an isolation citation and lacks exact-congener
    experimental support
  description: BGC0000668:5 inherits entry-level enzymatic/heterologous methods but
    cites only the compound’s 1994 NMR/isolation DOI. The source’s actual pathway
    references are omitted. The inspected 2014 cluster study demonstrates common precursor
    formation and a different welwitindolinone methylation; its fischerindole oxidative
    steps remain proposed. The halogenase paper’s accessible abstract concerns other
    congeners. Thus the current claim-specific citation is misrouted, and the strong
    exact-product grade needs adjudication rather than automatic inheritance. This
    finding does not deny the plausible wel-pathway association or assert that no
    later exact-product study exists.
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  field_paths:
  - biosynthetic_gene_clusters[0].evidence
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - biosynthetic_gene_clusters[0].link_evidence_basis
  - producer_organisms[0].evidence
  evidence_ids:
  - bgc-v5-source
  - bgc-primary24677572
  - bgc-primary25218740
  - bgc-local-routing
  rule_id: 'review-yaml-record Evidence Rules: narrowest claim support and congener
    specificity; docs/record-review-profile.md: compound-specific BGC evidence'
  native_severity: 'major: materially unsupported claim-level evidence and scope inflation
    risk'
  normalization_reason: Citation routing and inherited exact-product grade are one
    underlying evidence-scope problem; recorded once. Citation mismatch is confirmed;
    absence of direct proof is limited to the inspected sources.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: source-pinned producer versus locus citation correction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: compound-specific locus-method applicability correction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: generic reference selection and locus evidence propagation
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: source row BGC0000668:5
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: generated claim evidence and grades
actions:
- action_id: O-VERIFY-CITATION
  description: Inspect the complete 1990 article and any relevant supplementary material
    for this exact compound and taxon. If the triple is unsupported, add a full-row-pinned
    exclusion for the literal imported DOI, retain the supported 1994 assertions,
    and regenerate through the guarded seeder. Do not substitute a plausible DOI without
    exact source evidence.
  finding_ids:
  - O-SUSPICIOUS-CITATION
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Exact imported occurrence triple
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Implemented source-pinned occurrence withdrawal
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Occurrence emission
  generator: scripts/seed_from_sources.py through documented seed canary and guarded
    seeding
  acceptance_checks:
  - A cited full-text passage establishes exact compound/taxon support, or a reviewed
    exclusion removes only key ZVBCZYGMKQOJFW-QDUSTFBWSA-N / taxon NCBITaxon:162986
    / DOI:10.1021/JA00166A066.
  - The 1994 LOTUS and CyanoMetDB provenance and native producer claim remain separately
    scoped; run just seed-canary naturalproductmech:mibig-bc49771bdc, just validate-strict
    data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml, just verify-reproduction,
    just verify-corpus --summary, and just qc.
- action_id: reconcile-wel-target-evidence
  description: Review BGC0000668:5 with the primary pathway and isolation literature.
    Use the implemented source-pinned claim-reference table to route the locus claim
    to actual biosynthetic sources, preserving the isolation citation where appropriate.
    Separately adjudicate whether entry-wide methods apply to this exact congener
    and qualify or withdraw inapplicable methods through the implemented locus-evidence
    override; a reference-only correction must not silently certify CLUSTER_DEMONSTRATED.
    Preserve SOURCE_ASSERTION and document xenic culture limitations. Do not infer
    a new strain ID or use unimplemented decisions.tsv.
  finding_ids:
  - bgc-claim-scope
  target_ids:
  - naturalproductmech:mibig-bc49771bdc
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: source-pinned producer versus locus citation correction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: compound-specific locus-method applicability correction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: generic reference selection and locus evidence propagation
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: source row BGC0000668:5
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: generated claim evidence and grades
  generator: scripts/seed_from_sources.py via documented seed canary and guarded regeneration
  acceptance_checks:
  - A reviewer can identify the exact experimental product, enzyme/locus and strain
    for every retained demonstration claim; precursor or related-congener results
    remain explicitly scoped.
  - Producer and locus references are individually justified; the isolation DOI is
    not the sole support for a modern locus experiment.
  - Use just seed-canary naturalproductmech:mibig-bc49771bdc, inspect output, then
    documented seeding and just validate-strict data/natural_products/alkaloids/12-epi-fischerindole-i-isonitrile.yaml,
    just verify-reproduction, just verify-corpus --summary and just qc.
limitations:
- Published drawing-to-structure stereochemistry was checked by explicit atom mapping
  and a stereo-stripped reconstruction. The synthesis enantiomer correlation is source
  evidence; no optical rotations were remeasured and no spectra or crystallographic
  data were independently reinterpreted.
- Primary synthesis access was recovered through a normal direct retrieval of complete
  PMC HTML after the web renderer returned a challenge and the Europe PMC full-text
  service returned an error. No challenge bypass or paid access was used. The 2005
  institutional PDF lead failed TLS verification; no conclusions rely on its uninspected
  content.
- The ChEBI absence search covers the complete pinned eligible inventory with ignored-file
  exclusions disabled, plus direct inspection of CHEBI:202147. It does not claim an
  exhaustive current-ontology search.
- The 1990 LOTUS citation was resolved bibliographically but its complete article
  could not be inspected; exact occurrence support remains unresolved. The 1994 institutional
  abstract was read, but the original full isolation methods were not accessible.
- The main text of PMID:24677572 was fully inspected, but supplementary PDFs and figure
  images remained inaccessible through attempted free readers. Exact chromatogram
  assignments were not independently re-read.
- PMID:25218740 was inspected at primary abstract level; full text was paywalled and
  no paid access was used.
- A bounded web search used exact target name with biosynthesis/enzyme and WelO/WelO1
  terms. It did not establish exhaustive absence of later exact-target experiments.
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
- The configured ontology check skips unsupported adapters and allows taxon-label
  warnings; its success is not universal external identifier verification.
notes:
- No scientific owner, source inventory, graph, status or history was edited. All
  corrective actions are proposed work only.
- LOTUS and CyanoMetDB cite the same 1994 paper through distinct database routes;
  this does not establish independent experimental corroboration.
tags:
- path-order-campaign
- batch-001
- fischerindole
```
