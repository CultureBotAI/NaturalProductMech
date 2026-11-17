# 12-epi-fischerindole U isonitrile: exact identity, occurrence and WelU1 locus evidence

- Review: 20261021T070042Z-12-epi-fischerindole-u-isonitrile
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T06:48:23.743260Z
- Finished UTC: 2026-10-21T07:00:42.800405Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact ChEBI grounding, both chemical xrefs and all four stereocentres are supported. WelU1 from the listed UTEX B1830 locus demonstrably forms this exact U congener, so CLUSTER_DEMONSTRATED can remain with corrected claim-level references. The ChEBI occurrence citation is supported by its full methods. A separate 1987 LOTUS attribution remains unresolved, and the sourced definition mislabels Stigonematales as a genus.

## Scope And Provenance

One complete generated owner and resolved mechanism, with full field coverage and partial source access for one occurrence citation.

Selection: Third unreviewed path in deterministic path order after the initial validated list: 91 bundles covered 54 of 3,116 corpus records; 3,062 remained. This one-target bundle uses the helper’s ignored-file-inclusive coverage accounting.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:140442 | data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml | generated | 12-epi-fischerindole U isonitrile |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and component validation | passed | True | CHEBI:140442 | One complete owner validated with zero ERROR rows. |
| Corpus path and filing integrity | passed | True | CHEBI:140442 | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | CHEBI:140442 | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | CHEBI:140442 | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:140442 | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Initial QC attempt before installing the pinned linter | failed | False | CHEBI:140442 | The first full QC invocation stopped at lint because the isolated copied Python environment lacked Ruff. Exact uv.lock version Ruff 0.16.6 was subsequently installed and lint passed on later invocations. |
| QC attempt without network access | failed | False | CHEBI:140442 | After Ruff installation, QC passed lint and stopped at vendored-sync because sandbox DNS could not reach the pinned public CLAW governance source. Approved network access allowed the next invocation to verify all 22 governed artifacts. |
| QC attempt before restoring the required provenance tag | failed | False | CHEBI:140442 | QC passed lint, vendored sync, documentation, provenance and source queue, then stopped at tests: 998 passed, 1 failed, 4 skipped. The sole failure was the isolated clone lacking refs/tags/review-base/gentamicin-20261013; it was not a failed archive-content assertion. The tag was subsequently fetched from origin. |
| Targeted verification after restoring the provenance tag | passed | False | CHEBI:140442 | After restoring the required tag, the exact previously failed gentamicin archive test passed (1 passed). No repository content was edited for this remediation. |
| Diagnosis of the suite skip conditions | passed | False | CHEBI:140442 | The four observed skip cases were reproduced with pytest skip reasons enabled: the optional sibling AntibioticMech comparison has no sibling checkout in the isolated clone, and three command-frontmatter tests have empty parameter sets. This diagnostic invocation executed no passing tests; it reported four skips. |
| Full repository quality gate after environment repair | passed | True | CHEBI:140442 | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Full-text support for the 1987 occurrence citation | unavailable | True | CHEBI:140442 | Official bibliographic metadata resolves, but exact target and organism support cannot be adjudicated without the inaccessible full source. |
| Expression-module source applicability | not_applicable | False | CHEBI:140442 | No expression-module or regulatory claim is used to support this owner. Direct biochemical studies were inspected; no source-coverage absence is inferred. |

## Scientific And Domain Assessments

### Exact congener and internally consistent stereochemical encoding

identity: supported. Targets: CHEBI:140442.

The record consistently represents the unchlorinated U isonitrile with four assigned stereocentres. Official ChEBI, NPAtlas and CyanoMetDB agree on the full key NEYJIGPAQAKWSI-QBGRRASTSA-N.

### Exact chemical equivalence of both asserted xrefs

identity: supported. Targets: CHEBI:140442.

Both xrefs resolve to the exact full stereochemical structure. NPAtlas accepts its shorter NPA08787 accession and displays canonical NPA008787; its padding does not constitute a broken reference. Chemical equivalence does not validate unrelated provenance fields.

### Short related synonym denotes the same structure

identity: supported. Targets: CHEBI:140442.

ChEBI uses 12-epi-fischerindole U for the identical default structure containing the isonitrile. This directly supports the shorter related synonym at the level of chemical equivalence.

### Three-star exact ChEBI grounding

grounding: supported. Targets: CHEBI:140442.

CHEBI:140442 is the unique exact full-key match in the pinned eligible inventory and its current official entry remains three-star with the same default structure. EXACT grounding follows the repository rule.

### Independent exact-target primary configuration support

evidence: supported. Targets: CHEBI:140442.

The 2026 synthesis supports the encoded four-centre configuration. Systematic position mapping independently recovers the exact full key. Natural-enantiomer evidence is the authors’ synthesis correlation and enzyme acceptance; it is not a new crystallographic determination.

### Four occurrence objects and their claim-specific support

evidence: concern. Targets: CHEBI:140442.

The ChEBI PMID 27348090 occurrence is directly supported by the inspected methods. The 1994 source is relevant and shared by LOTUS and CyanoMetDB, so those routes are not independent experiments. The additional 1987 LOTUS citation names another species and its exact-compound support remains unresolved. Preserve species-level and strain-level observations separately.

### Taxonomic rank in sourced definition

identity: concern. Targets: CHEBI:140442.

The chemical description as a tetracyclic indole alkaloid is consistent with the structure; calling Stigonematales a genus is a bounded source-derived wording error.

### Computed classification and optional assertion scope

provenance: supported. Targets: CHEBI:140442.

The exact-key NPClassifier row matches Alkaloids/Tryptophan alkaloids/Hapalindole alkaloids and is explicitly marked computed. It is separate from source BGC TERPENE/OTHER. SEEDED and the three seed events do not claim scientific sign-off. No absent optional field is treated as a defect.

### Resolved mechanism, assays and additional assertions

scope: not_applicable. Targets: CHEBI:140442.

The full resolved owner has no optional mechanism graphs, activity records, targets, clinical claims or cross-corpus assertions. There are no declared components to resolve; this is bounded to the inspected owner.

### Exact compound, strain, sequence and source classification

grounding: supported. Targets: CHEBI:140442.

The versioned MIBiG source lists this exact unhalogenated U congener, and the strain taxon and deposited sequence resolve consistently. The TERPENE / OTHER classes reproduce the source’s terpene and alkaloid-derived classification. Omitted numerical locus bounds appropriately represent unspecified source bounds.

### Exact U formation versus halogenase substrate evidence

evidence: supported. Targets: CHEBI:140442.

The 2017 WelU1 experiment supplies an exact U formation result linked to the recorded UTEX B1830 accession, supporting retained CLUSTER_DEMONSTRATED with appropriate experimental citations. This is stronger exact-congener support than precursor assays or U consumption by WelO5. Preserve producer SOURCE_ASSERTION because heterologous protein expression and xenic-culture observations do not independently prove axenic native production.

### Claim-specific publication attribution

evidence: concern. Targets: CHEBI:140442.

The current producer and locus evidence both cite a compound-level 1987 reference. The exact modern locus demonstration is recoverable, but its publication is absent from the generated claim. Reference routing should be corrected independently of evidence-grade retention.

## Findings

### R-OCCURRENCE-CITATION: One LOTUS occurrence has unresolved exact-compound and species support

major / open / provisional; issue key: lotus-neyjigpaqakwsi-jo00226a009-occurrence-citation.

The second LOTUS observation cites a 1987 paper whose metadata names fontonamide, anhydrohapaloxindole A and H. fontinalis. The record instead asserts exact U occurrence in H. welwitschii. This is a provisional citation mismatch: full text is needed before concluding that no supporting passage exists. Independent support for U occurrence from other publications does not repair this source attribution.

### R-DEFINITION-RANK: Definition incorrectly calls Stigonematales a genus

minor / open / confirmed; issue key: chebi-140442-definition-stigonematales-rank.

The imported definition says Stigonematales genus. Primary taxonomic literature describes Stigonematales as a historical order. This bounded rank error is separate from the supported exact chemical identity and producer taxon.

### bgc-u-claim-reference: Producer and demonstrated locus reuse a compound reference instead of the exact WelU1 experiment

major / open / confirmed; issue key: mibig-bgc0000668-compound3-claim-reference.

BGC0000668:3 imports DOI:10.1021/jo00226a009 from compound-level evidence and repeats it as the sole support for both producer and demonstrated locus. The DOI metadata describes a 1987 H. fontinalis isolation paper; no inspected content connects it to KF811479.1. Exact U biosynthesis is experimentally supported by the 2017 WelU1 study, with the tested accession traceable to this same locus and strain. Correct claim-level citation routing while retaining the now-supported locus grade. Whether the 1987 paper independently reports this compound is a separate unresolved occurrence question; this finding does not assert article-wide absence from title alone.

## Recommended Actions And Acceptance Checks

### R-VERIFY-OCCURRENCE

Inspect the full 1987 article for exact U and the asserted H. welwitschii organism. If unsupported, use the exact-row-pinned LOTUS exclusion table; retain independently supported occurrence objects and do not substitute another DOI without evidence.

- An exact primary passage supports the imported triple, or a pinned exclusion removes only NEYJIGPAQAKWSI-QBGRRASTSA-N / NCBITaxon:162986 / literal DOI:10.1021/JO00226A009.
- Run just seed-canary CHEBI:140442; inspect the generated owner, then documented seeding, just validate-strict data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml, just verify-reproduction, just verify-corpus --summary and just qc.

### R-CORRECT-DEFINITION

Correct the sourced definition through a reproducible maintained source or supported qualification route. Use an evidence-backed cyanobacterial origin statement that avoids calling Stigonematales a genus, and retain transparent attribution for any local qualification. Do not hand-edit only the generated YAML.

- A regenerated owner has a scientifically accurate rank or precise organism wording, with source attribution preserved and exact structure unchanged.
- Run the documented seed canary, guarded regeneration, strict validation and reproduction/corpus gates; verify that the wording survives regeneration.

### route-u-claim-references

Use curation/mibig_claim_references.tsv with source key BGC0000668:3 and the exact source-row hash to route the locus to PMID:28225144 / DOI:10.1039/c7cc00782e, documenting its WelU1 accession bridge. Select a separately justified producer reference from the strain-specific primary studies or versioned source. Preserve source provenance, SOURCE_ASSERTION for native production, and CLUSTER_DEMONSTRATED for this exact U congener. Document that the heterologous expression produced the enzyme for in vitro assays, not a demonstrated native axenic culture. Do not substitute PMID:27348090 as proof of U formation.

- The generated locus citation identifies an experiment forming exact U, with AHI58823.1 mapped to KF811479.1 and UTEX B1830.
- Producer and locus citations are justified separately; native SOURCE_ASSERTION and supported CLUSTER_DEMONSTRATED remain distinct.
- Use just seed-canary CHEBI:140442, inspect output, then documented seeding and just validate-strict data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml, just verify-reproduction, just verify-corpus --summary and just qc.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-IDENTITY-LOCAL | data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml; Entire owner; chemical_structure, synonyms, xrefs, source_concepts and grounding_status | supports | The full owner encodes an unchlorinated tetracyclic isonitrile, four assigned centres and full key NEYJIGPAQAKWSI-QBGRRASTSA-N. The shorter name 12-epi-fischerindole U is a related synonym. |
| E-CHEBI-IDENTITY | https://www.ebi.ac.uk/chebi/backend/api/public/compound/140442/; chebi_accession, name, stars, default_structure id3104647, names and chemical_data; refreshed official response | supports | CHEBI:140442 has three stars and its default structure matches the entire record InChI and full key. Name 12-epi-fischerindole U denotes this exact isonitrile; the systematic synonym specifies (6aS,9S,10R,10aS). Formula C21H24N2 and neutral charge agree. |
| E-NPATLAS | https://www.npatlas.org/api/v1/compound/NPA008787?include=classifications; npaid, original_name, inchikey, inchi, smiles, mol_structures and reassignments; linked official page https://www.npatlas.org/explore/compounds/NPA08787 | supports | The literal legacy accession NPA08787 resolves to canonical NPA008787, named 12-epi-fischerindole U isonitrile. Its entire InChI and key match the owner, including all stereochemical layers. No structural reassignments are listed. This supports chemical equivalence; the separate origin-reference claim is not validated by the match. |
| E-CYANOMETDB-SOURCE | https://zenodo.org/records/13854577/files/CyanoMetDB_V03_2024.csv?download=1; Exact row CyanoMetDB_Identifier=CyanoMetDB_1549; CompoundName, NPAtlas_ID, SMILES_isomeric, InChI, InChlKey and IUPAC_name | supports | Official v03 row names 12-epi-fischerindole U isonitrile and provides matching full stereochemical key NEYJIGPAQAKWSI-QBGRRASTSA-N, NPAtlas_ID NPA008787 and formula C21H24N2. Its systematic name agrees with all four assigned centres. Full downloaded CSV checksum matches the committed source manifest. |
| E-CHEMISTRY-IDENTITY | /private/tmp/npm-review-work/003/chemistry.json; RDKit 2026.03.5 calculation generated 2026-10-21T06:49:35.950871Z; inspected result | supports | The SMILES recomputes to the exact owner InChI/key, C21H24N2, charge 0 and exact mass 304.193948768. Four centres are assigned: zero-based atoms 3:S,6:S,10:R,13:S; none is unassigned. This is internal consistency, distinguished from experimental configuration evidence. |
| E-GROUNDING-INVENTORY | data/raw/chebi_structures.tsv; Complete explicit pinned TSV parsed with csv.DictReader, all rows checked for full Standard InChIKey | supports | The full pinned eligible inventory contains exactly one hit for NEYJIGPAQAKWSI-QBGRRASTSA-N: CHEBI:140442, three stars, name 12-epi-fischerindole U. Thus the source-specific minted concepts collapse to one exact eligible structure. |
| E-GROUNDING-POLICY | docs/HARMONIZATION.md; Identity resolution: unambiguous three-star default-structure rule | supports | An unambiguous three-star ChEBI default-structure match is eligible for exact grounding. |
| E-SYNTHESIS-2026 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=13528852&amp;retmode=xml; Narva et al. DOI:10.1021/acs.joc.6c00185; PMC13528852; Results paragraphs P8-P12,P14-P15; Experimental subsections for 5, 10 and 1a | supports | The exact-target synthesis starts with (S)-carvone. Precursors 5 and 10 are explicitly (6aS,9S,10R,10aS); conversion to 1a retains axial isonitrile configuration and its NMR agrees with the natural-isolate report. Authors correlate the natural enantiomer through synthesis and WelO5 acceptance. They acknowledge that the original isolation lacked a specific rotation for comparison. They distinguish this target from earlier U isothiocyanate and 11-epi syntheses. |
| E-STEREO-MAPPING | /private/tmp/npm-review-work/003/stereo-mapping.json; Systematic ring positions mapped by connectivity; every original stereo tag stripped before assigning the four primary-text configurations | supports | Systematic positions 6a,9,10,10a map to zero-based record atoms 3,6,10,13. Assigning S,S,R,S independently gives the exact owner full InChI and key NEYJIGPAQAKWSI-QBGRRASTSA-N. This is a reproducible comparison with published assignments, not a new experiment. |
| R-LOCAL | data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml; Full generated owner, complete read_natural_product view and exact-key committed source rows | supports | The full owner merges the exact MIBiG and three-star ChEBI structure. Four occurrences comprise two LOTUS references, one CyanoMetDB reference shared with LOTUS, and one strain-specific ChEBI origin. The definition is copied from CHEBI:140442; three seed events retain SEEDED status. There are no declared causal_graph_refs or optional pathways, targets, activities, clinical or related-record claims. |
| R-1994 | https://pure.psu.edu/en/publications/welwitindolinones-unusual-alkaloids-from-the-blue-green-algae-hap/; Authors institutional abstract; DOI:10.1021/ja00101a015; source inspection reconciled at recorded timestamp | partial | The authors report fischerindoles and hapalindoles among minor constituents from H. welwitschii UHIC-52-3. Their relative structures were assigned spectroscopically. The abstract does not enumerate every fischerindole name; exact target linkage is supplied by the inspected compound-specific sources. The abstract’s absolute X-ray determination concerns welwitindolinone compound 7, not all co-isolated compounds. |
| R-WIKIDATA | https://www.wikidata.org/wiki/Special:EntityData/Q67340456.json; entity Q67340456 revision 2543823250, label/en and claims P225/P685 | supports | Previously inspected Q67340456 entity identifies Hapalosiphon welwitschii and NCBI Taxonomy 162986. Applicability was checked against this target’s three species-level occurrence objects; the ChEBI object instead uses a strain taxon. |
| R-WELO5-METHODS | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=5391150&amp;retmode=xml; ONLINE METHODS, WelO5-G166D, WelO5-S189A and WelO5-G166D-S189A in vitro activity assays; PMID:27348090 | supports | Official full article XML explicitly states that the exact 12-epi-fischerindole U substrate was isolated from H. welwitschii B1830 and purified to homogeneity, referring to the earlier isolation procedure. This supports the ChEBI strain occurrence citation. The enzyme consumes and chlorinates U; that reaction alone does not demonstrate formation of unhalogenated U. |
| R-TAXON-RANK | https://pubmed.ncbi.nlm.nih.gov/15023942/; Gugger and Hoffmann 2004, abstract; DOI:10.1099/ijs.0.02744-0; source inspection reconciled at recorded timestamp | refutes | The primary phylogenetic study describes true-branching cyanobacteria as Subsection V, formerly order Stigonematales. This contradicts calling Stigonematales a genus. Its polyphyly result also cautions against treating that historical grouping as a single producer genus; no modern rank reassignment is inferred here. |
| R-DEFINITION-TRANSFORM | scripts/extract_chebi.py; scripts/seed_from_sources.py; data/raw/chebi_structures.tsv; extract_chebi load_compounds/extract_structures; seed_from_sources lines 1003-1005; CHEBI:140442 exact-key source row; source inspection reconciled at recorded timestamp | supports | The extractor removes ChEBI HTML markup and retains definition text; the seeder directly emits the sole exact-match definition and its ChEBI source. The erroneous genus wording is therefore a source-derived definition, not an independent local taxonomic judgment. |
| R-1987-ACCESS | https://pubs.acs.org/doi/10.1021/jo00226a009; Bounded free primary article and PDF search; source inspection reconciled at recorded timestamp | unknown | The publisher metadata and Crossref record identify the 1987 H. fontinalis paper, but the full text could not be inspected. Exact U occurrence in H. welwitschii remains unresolved for this one citation. |
| bgc-v5-source | https://mibig.secondarymetabolites.org/repository/BGC0000668.5/annotations.json; compounds[2]; loci[0]; taxonomy; biosynthesis.classes; legacy_references | supports | Reused previously inspected full version-5 JSON, with applicability checked against this record: compound index 3 is 12-epi-fischerindole U isonitrile, C21H24N2, with the exact stored unhalogenated stereochemical SMILES and NMR reference DOI:10.1021/jo00226a009. The active, questionable-quality, complete entry lists KF811479.1, taxon 1433842, terpene/Monoterpene and other classes, and entry-wide Enzymatic assays / Heterologous expression methods without method-level references. Bounds 0/0 are unspecified, not genomic coordinates. Legacy references are PMID:24677572 and PMID:25218740. |
| bgc-kf811479 | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KF811479.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text; LOCUS, DEFINITION, VERSION, source feature and REFERENCE 1 | supports | Reused the already inspected accession source, applicable because this exact record lists KF811479.1 and taxon 1433842. The deposit is a 36,570 bp partial indolinone biosynthetic cluster from Hapalosiphon welwitschii UTEX B 1830, explicitly strain UTEX B 1830; its linked primary publication is PMID:24677572. |
| bgc-taxon-1433842 | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&amp;id=1433842&amp;lvl=&amp;mode=node; Taxonomy ID, current/equivalent names, rank and lineage | supports | Reused direct NCBI taxonomy inspection: 1433842 is the strain-level Hapalosiphon welwitschii UTEX B 1830 taxon, with equivalent UTEX 1830 spelling. Applies directly to the producer and cluster organism identifiers in this record. |
| bgc-primary24677572 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4382313/; Strain selection, metabolite profiling, cluster discovery and Experimental Section; PMID:24677572 / DOI:10.1002/cbic.201300794 | partial | Reused inspected full main text for the same UTEX B 1830 wel locus: the culture was xenic, metabolite profiling used HPLC/UV/HRMS, and the study assembled the approximately 36 kb cluster. Its experiments primarily demonstrated common precursor synthesis and methylation of another welwitindolinone. This provides strain/locus context but does not independently establish axenic native production of U. |
| bgc-primary28225144 | https://pubs.rsc.org/en/content/articlehtml/2017/cc/c7cc00782e; Primary abstract; Zhu and Liu, Chemical Communications 53:2826-2829 (2017); PMID:28225144 / DOI:10.1039/c7cc00782e | supports | The primary abstract explicitly reports that heterologously expressed and purified WelU1 selectively forms exact 12-epi-fischerindole U from 3-geranyl 3-isocyanovinyl indolenine. The study examines the UTEX B1830 and IC-52-3 pathways; the supplement resolves which tested enzyme came from which strain. Main article body did not load, so only the abstract and separately accessible complete supplement were inspected. |
| bgc-welu1-supplement | https://www.rsc.org/suppdata/c7/cc/c7cc00782e/c7cc00782e1.pdf; PDF pages 2-4 Methods; page 7 Figure S2; page 11 Figure S6; DOI:10.1039/c7cc00782e supporting information | supports | Free primary supplement identifies WelU1 as AHI58823, amplified from UTEX B1830 genomic DNA and expressed in E. coli C43(DE3). Methods specify purified-enzyme formation of U and preparative isolation. Figure S2 compares the enzymatic product by 1H NMR with natural U. Figure S6 separately reports U in UTEX B1830 crude-metabolite HPLC, with 20.7% relative abundance, and distinguishes IC-52-3 isolation data. This directly supports the exact U enzyme-locus link; it does not make the native culture axenic. |
| bgc-welu1-accession | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AHI58823.1&amp;db=protein&amp;report=genpept&amp;retmode=text; DEFINITION, DBSOURCE, source feature and coded_by qualifier | supports | Direct GenPept text identifies AHI58823.1 as 228-residue WelU1 from H. welwitschii UTEX B 1830, taxon 1433842; DBSOURCE is KF811479.1 and coded_by is complement(KF811479.1:8668..9354). This bridges the experimentally tested protein in the 2017 supplement to this record’s exact strain and listed locus accession. |
| bgc-primary27348090 | https://pubmed.ncbi.nlm.nih.gov/27348090/; Abstract and Figures 1-4 captions; DOI:10.1038/nchembio.2112 | partial | The primary abstract and figure captions describe WelO5 binding and chlorinating 12-epi-fischerindole U as a substrate. This demonstrates enzymatic consumption and halogenation of U rather than formation of the unhalogenated U target. It cannot replace the exact-product formation study as locus synthesis evidence. Primary full text was not retrieved in the attempted PMC/EuropePMC readers. The full methods were subsequently retrieved by the parent reviewer; see R-WELO5-METHODS for occurrence support. |
| bgc-cited-doi-metadata | https://api.crossref.org/works/10.1021/jo00226a009; title, published date, container-title, volume/issue/pages; independently matched indexed ACS publisher metadata | partial | Official DOI metadata identifies the cited publication as the 1987 Journal of Organic Chemistry paper Fontonamide and anhydrohapaloxindole A, two new alkaloids from the blue-green alga Hapalosiphon fontinalis, 52(17):3773-3777. This is not the modern WelU1 experiment or the 2014 KF811479.1 cluster paper. Full primary text was inaccessible; the title alone does not prove U absent from the article. |
| bgc-local-routing | scripts/extract_mibig.py; scripts/seed_from_sources.py; data/raw/mibig_compounds.tsv; curation/mibig_claim_references.tsv; primary_reference() lines 189-221; mibig_compounds.tsv row 791, source key BGC0000668:3; current record producer and cluster evidence | supports | The exact raw row stores COMPOUND_EVIDENCE DOI:10.1021/jo00226a009 alongside the locus methods and CLUSTER_DEMONSTRATED grade. The extractor prioritizes chemical-structure references over entry references; the generated producer and locus both inherit that reference. The implemented claim-reference table permits separate source-pinned producer_reference and locus_reference corrections. |

## Limits And Additional Notes

- Primary full text was inspected through the public NCBI efetch XML endpoint. PMC web and figure routes returned a challenge and EuropePMC returned an error; no unavailable figure is claimed as visually checked.
- The published systematic assignments and product-retention discussion were compared with the encoded structure. Spectra, rotations and enzyme experiments were not independently remeasured or reinterpreted; published assignment and natural-enantiomer correlation remain source-level evidence.
- The inventory uniqueness statement covers the entire pinned eligible ChEBI file and direct official inspection of CHEBI:140442; it is not an exhaustive search across every current ChEBI entity.
- The complete 1987 cited article remains inaccessible, so the LOTUS citation concern is provisional. The 1994 institutional abstract was inspected; its complete original isolation methods were not obtained.
- The PMID 27348090 full article methods were recovered via official NCBI XML after browser access failures, resolving its occurrence support; raw spectra and crystallographic coordinates were not independently reanalysed.
- The 2017 primary main article body did not load; its primary abstract and complete public supplement provided the inspected exact enzyme, strain, assay and NMR evidence.
- DOI:10.1021/jo00226a009 full text was not obtained. Official metadata supports citation-scope concern but not a claim that U is absent from every passage.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- No owner, source inventory, component, curation status or seed history was edited; all follow-up actions are proposals.
- The native producer SOURCE_ASSERTION remains distinct from supported occurrence and enzyme-locus evidence. A validated partial review does not confer native REVIEWED status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070042Z-12-epi-fischerindole-u-isonitrile
kind: record
repository: CultureBotAI/NaturalProductMech
title: '12-epi-fischerindole U isonitrile: exact identity, occurrence and WelU1 locus
  evidence'
started_at: '2026-10-21T06:48:23.743260Z'
finished_at: '2026-10-21T07:00:42.800405Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its source inputs. Parallel source inspections were reconciled into this single
    observation; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Exact ChEBI grounding, both chemical xrefs and all four stereocentres are
  supported. WelU1 from the listed UTEX B1830 locus demonstrably forms this exact
  U congener, so CLUSTER_DEMONSTRATED can remain with corrected claim-level references.
  The ChEBI occurrence citation is supported by its full methods. A separate 1987
  LOTUS attribution remains unresolved, and the sourced definition mislabels Stigonematales
  as a genus.
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
  - path: data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml
    sha256: e90aba11e104f2f7087ba3875f3e09fb66722ae4a5aa432fa9ef860b38cac689
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete generated owner and resolved mechanism, with full field
    coverage and partial source access for one occurrence citation.
  selection: 'Third unreviewed path in deterministic path order after the initial
    validated list: 91 bundles covered 54 of 3,116 corpus records; 3,062 remained.
    This one-target bundle uses the helper’s ignored-file-inclusive coverage accounting.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:140442
targets:
- target_id: CHEBI:140442
  path: data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml
  label: 12-epi-fischerindole U isonitrile
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
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: ChEBI organism origin source
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: ChEBI grounding and definition source
checks:
- check_id: C-STRICT
  name: Closed-schema and component validation
  status: passed
  required: true
  summary: One complete owner validated with zero ERROR rows.
  command: just validate-strict data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml
    --out /private/tmp/npm-review-work/003/strict.tsv
  exit_code: 0
  target_ids:
  - CHEBI:140442
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned
    filing pathways.
  target_ids:
  - CHEBI:140442
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
  - CHEBI:140442
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
  - CHEBI:140442
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
  - CHEBI:140442
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
  - CHEBI:140442
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
  - CHEBI:140442
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
  - CHEBI:140442
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
  - CHEBI:140442
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
  - CHEBI:140442
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
  - CHEBI:140442
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:02.058886+00:00; finished 2026-10-21T06:54:53.950582+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/qc-attempt4.log.'
- check_id: C-1987-OCCURRENCE
  name: Full-text support for the 1987 occurrence citation
  status: unavailable
  required: true
  summary: Official bibliographic metadata resolves, but exact target and organism
    support cannot be adjudicated without the inaccessible full source.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - bgc-cited-doi-metadata
  - R-1987-ACCESS
- check_id: C-IMODULON
  name: Expression-module source applicability
  status: not_applicable
  required: false
  summary: No expression-module or regulatory claim is used to support this owner.
    Direct biochemical studies were inspected; no source-coverage absence is inferred.
  target_ids:
  - CHEBI:140442
evidence:
- evidence_id: E-IDENTITY-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml
  locator: Entire owner; chemical_structure, synonyms, xrefs, source_concepts and
    grounding_status
  accessed_at: '2026-10-21T06:52:25Z'
  support: supports
  summary: The full owner encodes an unchlorinated tetracyclic isonitrile, four assigned
    centres and full key NEYJIGPAQAKWSI-QBGRRASTSA-N. The shorter name 12-epi-fischerindole
    U is a related synonym.
  snapshot_sha256: e90aba11e104f2f7087ba3875f3e09fb66722ae4a5aa432fa9ef860b38cac689
- evidence_id: E-CHEBI-IDENTITY
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/140442/
  locator: chebi_accession, name, stars, default_structure id3104647, names and chemical_data;
    refreshed official response
  accessed_at: '2026-10-21T06:52:44Z'
  support: supports
  summary: CHEBI:140442 has three stars and its default structure matches the entire
    record InChI and full key. Name 12-epi-fischerindole U denotes this exact isonitrile;
    the systematic synonym specifies (6aS,9S,10R,10aS). Formula C21H24N2 and neutral
    charge agree.
  snapshot_sha256: 79207e6fc4f1f384e3572d81e122bf8efc8007e1a2be33e12b5d4a760a839a94
- evidence_id: E-NPATLAS
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA008787?include=classifications
  locator: npaid, original_name, inchikey, inchi, smiles, mol_structures and reassignments;
    linked official page https://www.npatlas.org/explore/compounds/NPA08787
  accessed_at: '2026-10-21T06:52:44Z'
  support: supports
  summary: The literal legacy accession NPA08787 resolves to canonical NPA008787,
    named 12-epi-fischerindole U isonitrile. Its entire InChI and key match the owner,
    including all stereochemical layers. No structural reassignments are listed. This
    supports chemical equivalence; the separate origin-reference claim is not validated
    by the match.
  snapshot_sha256: 8b2fc773333ef91363359404994f8bb2b14147ccb2e724c88dfbae329de74b8e
- evidence_id: E-CYANOMETDB-SOURCE
  kind: database
  reference: https://zenodo.org/records/13854577/files/CyanoMetDB_V03_2024.csv?download=1
  locator: Exact row CyanoMetDB_Identifier=CyanoMetDB_1549; CompoundName, NPAtlas_ID,
    SMILES_isomeric, InChI, InChlKey and IUPAC_name
  accessed_at: '2026-10-21T06:50:07Z'
  support: supports
  summary: Official v03 row names 12-epi-fischerindole U isonitrile and provides matching
    full stereochemical key NEYJIGPAQAKWSI-QBGRRASTSA-N, NPAtlas_ID NPA008787 and
    formula C21H24N2. Its systematic name agrees with all four assigned centres. Full
    downloaded CSV checksum matches the committed source manifest.
  snapshot_sha256: 91aa57146c9e803d5eeef656fc0e5cfc8f804531b1b83718757e96aa848a4121
- evidence_id: E-CHEMISTRY-IDENTITY
  kind: validation
  reference: /private/tmp/npm-review-work/003/chemistry.json
  locator: RDKit 2026.03.5 calculation generated 2026-10-21T06:49:35.950871Z; inspected
    result
  accessed_at: '2026-10-21T06:52:07Z'
  support: supports
  summary: 'The SMILES recomputes to the exact owner InChI/key, C21H24N2, charge 0
    and exact mass 304.193948768. Four centres are assigned: zero-based atoms 3:S,6:S,10:R,13:S;
    none is unassigned. This is internal consistency, distinguished from experimental
    configuration evidence.'
  snapshot_sha256: 24b9c03bc3fdd9aea21939ca26e8ad109d7b9a30a5438bbce12df1e8e6356d6f
- evidence_id: E-GROUNDING-INVENTORY
  kind: search
  reference: data/raw/chebi_structures.tsv
  locator: Complete explicit pinned TSV parsed with csv.DictReader, all rows checked
    for full Standard InChIKey
  accessed_at: '2026-10-21T06:53:03Z'
  support: supports
  summary: 'The full pinned eligible inventory contains exactly one hit for NEYJIGPAQAKWSI-QBGRRASTSA-N:
    CHEBI:140442, three stars, name 12-epi-fischerindole U. Thus the source-specific
    minted concepts collapse to one exact eligible structure.'
  search_scope: Read the complete explicitly named inventory file, including all its
    rows without gitignore-based exclusions; compared the full standard_inchi_key
    column, not only its connectivity block.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: E-GROUNDING-POLICY
  kind: authority
  reference: docs/HARMONIZATION.md
  locator: 'Identity resolution: unambiguous three-star default-structure rule'
  accessed_at: '2026-10-21T06:45:28Z'
  support: supports
  summary: An unambiguous three-star ChEBI default-structure match is eligible for
    exact grounding.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: E-SYNTHESIS-2026
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=13528852&retmode=xml
  locator: Narva et al. DOI:10.1021/acs.joc.6c00185; PMC13528852; Results paragraphs
    P8-P12,P14-P15; Experimental subsections for 5, 10 and 1a
  accessed_at: '2026-10-21T06:51:35Z'
  support: supports
  summary: The exact-target synthesis starts with (S)-carvone. Precursors 5 and 10
    are explicitly (6aS,9S,10R,10aS); conversion to 1a retains axial isonitrile configuration
    and its NMR agrees with the natural-isolate report. Authors correlate the natural
    enantiomer through synthesis and WelO5 acceptance. They acknowledge that the original
    isolation lacked a specific rotation for comparison. They distinguish this target
    from earlier U isothiocyanate and 11-epi syntheses.
  snapshot_sha256: 8e242392b291945551a944e4a20aa398b179ba4576b23741274067966cdfcd83
- evidence_id: E-STEREO-MAPPING
  kind: validation
  reference: /private/tmp/npm-review-work/003/stereo-mapping.json
  locator: Systematic ring positions mapped by connectivity; every original stereo
    tag stripped before assigning the four primary-text configurations
  accessed_at: '2026-10-21T06:53:03.389146Z'
  support: supports
  summary: Systematic positions 6a,9,10,10a map to zero-based record atoms 3,6,10,13.
    Assigning S,S,R,S independently gives the exact owner full InChI and key NEYJIGPAQAKWSI-QBGRRASTSA-N.
    This is a reproducible comparison with published assignments, not a new experiment.
  snapshot_sha256: 8c495d73aec4afd3d6ac7a949f4d1e85c8c493e5691addd275f50a8cdbef709b
- evidence_id: R-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml
  locator: Full generated owner, complete read_natural_product view and exact-key
    committed source rows
  accessed_at: '2026-10-21T06:49:35.950871Z'
  support: supports
  summary: The full owner merges the exact MIBiG and three-star ChEBI structure. Four
    occurrences comprise two LOTUS references, one CyanoMetDB reference shared with
    LOTUS, and one strain-specific ChEBI origin. The definition is copied from CHEBI:140442;
    three seed events retain SEEDED status. There are no declared causal_graph_refs
    or optional pathways, targets, activities, clinical or related-record claims.
  snapshot_sha256: e90aba11e104f2f7087ba3875f3e09fb66722ae4a5aa432fa9ef860b38cac689
- evidence_id: R-1994
  kind: primary_source
  reference: https://pure.psu.edu/en/publications/welwitindolinones-unusual-alkaloids-from-the-blue-green-algae-hap/
  locator: Authors institutional abstract; DOI:10.1021/ja00101a015; source inspection
    reconciled at recorded timestamp
  accessed_at: '2026-10-21T06:58:59.989041Z'
  support: partial
  summary: The authors report fischerindoles and hapalindoles among minor constituents
    from H. welwitschii UHIC-52-3. Their relative structures were assigned spectroscopically.
    The abstract does not enumerate every fischerindole name; exact target linkage
    is supplied by the inspected compound-specific sources. The abstract’s absolute
    X-ray determination concerns welwitindolinone compound 7, not all co-isolated
    compounds.
- evidence_id: R-WIKIDATA
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q67340456.json
  locator: entity Q67340456 revision 2543823250, label/en and claims P225/P685
  accessed_at: '2026-10-21T06:44:23.635771Z'
  support: supports
  summary: Previously inspected Q67340456 entity identifies Hapalosiphon welwitschii
    and NCBI Taxonomy 162986. Applicability was checked against this target’s three
    species-level occurrence objects; the ChEBI object instead uses a strain taxon.
  snapshot_sha256: 53fdaac9788b1ac4ea420b9173248f248da507f8d3a1ab73fa39607f8c6cd4fb
- evidence_id: R-WELO5-METHODS
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5391150&retmode=xml
  locator: ONLINE METHODS, WelO5-G166D, WelO5-S189A and WelO5-G166D-S189A in vitro
    activity assays; PMID:27348090
  accessed_at: '2026-10-21T06:53:20.206452Z'
  support: supports
  summary: Official full article XML explicitly states that the exact 12-epi-fischerindole
    U substrate was isolated from H. welwitschii B1830 and purified to homogeneity,
    referring to the earlier isolation procedure. This supports the ChEBI strain occurrence
    citation. The enzyme consumes and chlorinates U; that reaction alone does not
    demonstrate formation of unhalogenated U.
  snapshot_sha256: 7529fd58d4361761dcb082a1b55bc733db89827842151a2008fc555fa20e7e1d
- evidence_id: R-TAXON-RANK
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15023942/
  locator: Gugger and Hoffmann 2004, abstract; DOI:10.1099/ijs.0.02744-0; source inspection
    reconciled at recorded timestamp
  accessed_at: '2026-10-21T06:58:59.989041Z'
  support: refutes
  summary: The primary phylogenetic study describes true-branching cyanobacteria as
    Subsection V, formerly order Stigonematales. This contradicts calling Stigonematales
    a genus. Its polyphyly result also cautions against treating that historical grouping
    as a single producer genus; no modern rank reassignment is inferred here.
- evidence_id: R-DEFINITION-TRANSFORM
  kind: record_content
  reference: scripts/extract_chebi.py; scripts/seed_from_sources.py; data/raw/chebi_structures.tsv
  locator: extract_chebi load_compounds/extract_structures; seed_from_sources lines
    1003-1005; CHEBI:140442 exact-key source row; source inspection reconciled at
    recorded timestamp
  accessed_at: '2026-10-21T06:58:59.989041Z'
  support: supports
  summary: The extractor removes ChEBI HTML markup and retains definition text; the
    seeder directly emits the sole exact-match definition and its ChEBI source. The
    erroneous genus wording is therefore a source-derived definition, not an independent
    local taxonomic judgment.
- evidence_id: R-1987-ACCESS
  kind: search
  reference: https://pubs.acs.org/doi/10.1021/jo00226a009
  locator: Bounded free primary article and PDF search; source inspection reconciled
    at recorded timestamp
  accessed_at: '2026-10-21T06:58:59.989041Z'
  support: unknown
  summary: The publisher metadata and Crossref record identify the 1987 H. fontinalis
    paper, but the full text could not be inspected. Exact U occurrence in H. welwitschii
    remains unresolved for this one citation.
  search_scope: Searched exact DOI and exact title plus pdf. Tried official ACS article,
    PDF and ePDF endpoints; these were inaccessible or returned 403. Indexed results
    were metadata, later reviews or other databases, not inspected primary full text.
    No paid access or author contact. This is an access limitation, not article-wide
    or literature-wide absence.
- evidence_id: bgc-v5-source
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000668.5/annotations.json
  locator: compounds[2]; loci[0]; taxonomy; biosynthesis.classes; legacy_references
  accessed_at: '2026-10-21T06:43:48Z'
  support: supports
  summary: 'Reused previously inspected full version-5 JSON, with applicability checked
    against this record: compound index 3 is 12-epi-fischerindole U isonitrile, C21H24N2,
    with the exact stored unhalogenated stereochemical SMILES and NMR reference DOI:10.1021/jo00226a009.
    The active, questionable-quality, complete entry lists KF811479.1, taxon 1433842,
    terpene/Monoterpene and other classes, and entry-wide Enzymatic assays / Heterologous
    expression methods without method-level references. Bounds 0/0 are unspecified,
    not genomic coordinates. Legacy references are PMID:24677572 and PMID:25218740.'
- evidence_id: bgc-kf811479
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KF811479.1&db=nuccore&report=genbank&retmode=text
  locator: LOCUS, DEFINITION, VERSION, source feature and REFERENCE 1
  accessed_at: '2026-10-21T06:43:48Z'
  support: supports
  summary: Reused the already inspected accession source, applicable because this
    exact record lists KF811479.1 and taxon 1433842. The deposit is a 36,570 bp partial
    indolinone biosynthetic cluster from Hapalosiphon welwitschii UTEX B 1830, explicitly
    strain UTEX B 1830; its linked primary publication is PMID:24677572.
- evidence_id: bgc-taxon-1433842
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1433842&lvl=&mode=node
  locator: Taxonomy ID, current/equivalent names, rank and lineage
  accessed_at: '2026-10-21T06:45:11Z'
  support: supports
  summary: 'Reused direct NCBI taxonomy inspection: 1433842 is the strain-level Hapalosiphon
    welwitschii UTEX B 1830 taxon, with equivalent UTEX 1830 spelling. Applies directly
    to the producer and cluster organism identifiers in this record.'
- evidence_id: bgc-primary24677572
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4382313/
  locator: Strain selection, metabolite profiling, cluster discovery and Experimental
    Section; PMID:24677572 / DOI:10.1002/cbic.201300794
  accessed_at: '2026-10-21T06:45:11Z'
  support: partial
  summary: 'Reused inspected full main text for the same UTEX B 1830 wel locus: the
    culture was xenic, metabolite profiling used HPLC/UV/HRMS, and the study assembled
    the approximately 36 kb cluster. Its experiments primarily demonstrated common
    precursor synthesis and methylation of another welwitindolinone. This provides
    strain/locus context but does not independently establish axenic native production
    of U.'
- evidence_id: bgc-primary28225144
  kind: primary_source
  reference: https://pubs.rsc.org/en/content/articlehtml/2017/cc/c7cc00782e
  locator: Primary abstract; Zhu and Liu, Chemical Communications 53:2826-2829 (2017);
    PMID:28225144 / DOI:10.1039/c7cc00782e
  accessed_at: '2026-10-21T06:50:18Z'
  support: supports
  summary: The primary abstract explicitly reports that heterologously expressed and
    purified WelU1 selectively forms exact 12-epi-fischerindole U from 3-geranyl 3-isocyanovinyl
    indolenine. The study examines the UTEX B1830 and IC-52-3 pathways; the supplement
    resolves which tested enzyme came from which strain. Main article body did not
    load, so only the abstract and separately accessible complete supplement were
    inspected.
- evidence_id: bgc-welu1-supplement
  kind: primary_source
  reference: https://www.rsc.org/suppdata/c7/cc/c7cc00782e/c7cc00782e1.pdf
  locator: PDF pages 2-4 Methods; page 7 Figure S2; page 11 Figure S6; DOI:10.1039/c7cc00782e
    supporting information
  accessed_at: '2026-10-21T06:50:18Z'
  support: supports
  summary: Free primary supplement identifies WelU1 as AHI58823, amplified from UTEX
    B1830 genomic DNA and expressed in E. coli C43(DE3). Methods specify purified-enzyme
    formation of U and preparative isolation. Figure S2 compares the enzymatic product
    by 1H NMR with natural U. Figure S6 separately reports U in UTEX B1830 crude-metabolite
    HPLC, with 20.7% relative abundance, and distinguishes IC-52-3 isolation data.
    This directly supports the exact U enzyme-locus link; it does not make the native
    culture axenic.
  search_scope: Complete searchable 14-page primary PDF inspected. Screenshot retrieval
    failed with HTTP 404, so visual stereochemical comparison of embedded structure
    drawings was not independently performed.
- evidence_id: bgc-welu1-accession
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AHI58823.1&db=protein&report=genpept&retmode=text
  locator: DEFINITION, DBSOURCE, source feature and coded_by qualifier
  accessed_at: '2026-10-21T06:50:50Z'
  support: supports
  summary: Direct GenPept text identifies AHI58823.1 as 228-residue WelU1 from H.
    welwitschii UTEX B 1830, taxon 1433842; DBSOURCE is KF811479.1 and coded_by is
    complement(KF811479.1:8668..9354). This bridges the experimentally tested protein
    in the 2017 supplement to this record’s exact strain and listed locus accession.
- evidence_id: bgc-primary27348090
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/27348090/
  locator: Abstract and Figures 1-4 captions; DOI:10.1038/nchembio.2112
  accessed_at: '2026-10-21T06:50:00Z'
  support: partial
  summary: The primary abstract and figure captions describe WelO5 binding and chlorinating
    12-epi-fischerindole U as a substrate. This demonstrates enzymatic consumption
    and halogenation of U rather than formation of the unhalogenated U target. It
    cannot replace the exact-product formation study as locus synthesis evidence.
    Primary full text was not retrieved in the attempted PMC/EuropePMC readers. The
    full methods were subsequently retrieved by the parent reviewer; see R-WELO5-METHODS
    for occurrence support.
- evidence_id: bgc-cited-doi-metadata
  kind: authority
  reference: https://api.crossref.org/works/10.1021/jo00226a009
  locator: title, published date, container-title, volume/issue/pages; independently
    matched indexed ACS publisher metadata
  accessed_at: '2026-10-21T06:50:50Z'
  support: partial
  summary: Official DOI metadata identifies the cited publication as the 1987 Journal
    of Organic Chemistry paper Fontonamide and anhydrohapaloxindole A, two new alkaloids
    from the blue-green alga Hapalosiphon fontinalis, 52(17):3773-3777. This is not
    the modern WelU1 experiment or the 2014 KF811479.1 cluster paper. Full primary
    text was inaccessible; the title alone does not prove U absent from the article.
- evidence_id: bgc-local-routing
  kind: record_content
  reference: scripts/extract_mibig.py; scripts/seed_from_sources.py; data/raw/mibig_compounds.tsv;
    curation/mibig_claim_references.tsv
  locator: primary_reference() lines 189-221; mibig_compounds.tsv row 791, source
    key BGC0000668:3; current record producer and cluster evidence
  accessed_at: '2026-10-21T06:51:14Z'
  support: supports
  summary: The exact raw row stores COMPOUND_EVIDENCE DOI:10.1021/jo00226a009 alongside
    the locus methods and CLUSTER_DEMONSTRATED grade. The extractor prioritizes chemical-structure
    references over entry references; the generated producer and locus both inherit
    that reference. The implemented claim-reference table permits separate source-pinned
    producer_reference and locus_reference corrections.
  search_scope: Read exact target and source row; rg --no-ignore --hidden searched
    the exact label, minted source identifier and BGC0000668:3 across the raw MIBiG
    inventory and relevant correction tables, including ignored files in those scoped
    paths.
assessments:
- assessment_id: A-IDENTITY-REPRESENTATION
  area: identity
  topic: Exact congener and internally consistent stereochemical encoding
  outcome: supported
  summary: The record consistently represents the unchlorinated U isonitrile with
    four assigned stereocentres. Official ChEBI, NPAtlas and CyanoMetDB agree on the
    full key NEYJIGPAQAKWSI-QBGRRASTSA-N.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-CHEBI-IDENTITY
  - E-NPATLAS
  - E-CYANOMETDB-SOURCE
  - E-CHEMISTRY-IDENTITY
- assessment_id: A-XREF-EQUIVALENCE
  area: identity
  topic: Exact chemical equivalence of both asserted xrefs
  outcome: supported
  summary: Both xrefs resolve to the exact full stereochemical structure. NPAtlas
    accepts its shorter NPA08787 accession and displays canonical NPA008787; its padding
    does not constitute a broken reference. Chemical equivalence does not validate
    unrelated provenance fields.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-NPATLAS
  - E-CYANOMETDB-SOURCE
- assessment_id: A-SYNONYM
  area: identity
  topic: Short related synonym denotes the same structure
  outcome: supported
  summary: ChEBI uses 12-epi-fischerindole U for the identical default structure containing
    the isonitrile. This directly supports the shorter related synonym at the level
    of chemical equivalence.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-CHEBI-IDENTITY
- assessment_id: A-GROUNDING
  area: grounding
  topic: Three-star exact ChEBI grounding
  outcome: supported
  summary: CHEBI:140442 is the unique exact full-key match in the pinned eligible
    inventory and its current official entry remains three-star with the same default
    structure. EXACT grounding follows the repository rule.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-CHEBI-IDENTITY
  - E-GROUNDING-INVENTORY
  - E-GROUNDING-POLICY
- assessment_id: A-PRIMARY-STEREOCHEMISTRY
  area: evidence
  topic: Independent exact-target primary configuration support
  outcome: supported
  summary: The 2026 synthesis supports the encoded four-centre configuration. Systematic
    position mapping independently recovers the exact full key. Natural-enantiomer
    evidence is the authors’ synthesis correlation and enzyme acceptance; it is not
    a new crystallographic determination.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - E-SYNTHESIS-2026
  - E-STEREO-MAPPING
  - E-CHEMISTRY-IDENTITY
  dimensions:
  - name: primary_configuration_mapping
    value: 6a=atom3:S; 9=atom6:S; 10=atom10:R; 10a=atom13:S
    definition: Systematic indeno[2,1-b]indole positions mapped to zero-based RDKit
      atom indices by connectivity
    evidence_ids:
    - E-SYNTHESIS-2026
    - E-STEREO-MAPPING
- assessment_id: R-OCCURRENCE
  area: evidence
  topic: Four occurrence objects and their claim-specific support
  outcome: concern
  summary: The ChEBI PMID 27348090 occurrence is directly supported by the inspected
    methods. The 1994 source is relevant and shared by LOTUS and CyanoMetDB, so those
    routes are not independent experiments. The additional 1987 LOTUS citation names
    another species and its exact-compound support remains unresolved. Preserve species-level
    and strain-level observations separately.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - R-LOCAL
  - R-1994
  - R-WIKIDATA
  - R-WELO5-METHODS
  - bgc-cited-doi-metadata
  - bgc-welu1-supplement
  dimensions:
  - name: occurrence_taxon_resolution
    value: NCBITaxon:162986 species; NCBITaxon:1433842 UTEX B1830 strain
    definition: Distinct source occurrence scopes; neither alone upgrades the native
      producer evidence tier
    evidence_ids:
    - R-LOCAL
    - R-WIKIDATA
    - bgc-taxon-1433842
  - name: ChEBI_source_label_scope
    value: Species text Hapalosiphon welwitschii plus strain context UTEX B1830, linked
      to strain taxon 1433842
    definition: The preserved source label is less specific than its taxon identifier;
      the explicit strain context resolves the intended organism
    evidence_ids:
    - R-LOCAL
    - bgc-taxon-1433842
    - R-WELO5-METHODS
- assessment_id: R-DEFINITION
  area: identity
  topic: Taxonomic rank in sourced definition
  outcome: concern
  summary: The chemical description as a tetracyclic indole alkaloid is consistent
    with the structure; calling Stigonematales a genus is a bounded source-derived
    wording error.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - R-LOCAL
  - R-TAXON-RANK
  - R-DEFINITION-TRANSFORM
- assessment_id: R-CLASSIFICATION
  area: provenance
  topic: Computed classification and optional assertion scope
  outcome: supported
  summary: The exact-key NPClassifier row matches Alkaloids/Tryptophan alkaloids/Hapalindole
    alkaloids and is explicitly marked computed. It is separate from source BGC TERPENE/OTHER.
    SEEDED and the three seed events do not claim scientific sign-off. No absent optional
    field is treated as a defect.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - R-LOCAL
  - bgc-v5-source
- assessment_id: R-OPTIONAL
  area: scope
  topic: Resolved mechanism, assays and additional assertions
  outcome: not_applicable
  summary: The full resolved owner has no optional mechanism graphs, activity records,
    targets, clinical claims or cross-corpus assertions. There are no declared components
    to resolve; this is bounded to the inspected owner.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - R-LOCAL
- assessment_id: bgc-identifiers-supported
  area: grounding
  topic: Exact compound, strain, sequence and source classification
  outcome: supported
  summary: The versioned MIBiG source lists this exact unhalogenated U congener, and
    the strain taxon and deposited sequence resolve consistently. The TERPENE / OTHER
    classes reproduce the source’s terpene and alkaloid-derived classification. Omitted
    numerical locus bounds appropriately represent unspecified source bounds.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - bgc-v5-source
  - bgc-kf811479
  - bgc-taxon-1433842
- assessment_id: bgc-u-demonstration-supported
  area: evidence
  topic: Exact U formation versus halogenase substrate evidence
  outcome: supported
  summary: The 2017 WelU1 experiment supplies an exact U formation result linked to
    the recorded UTEX B1830 accession, supporting retained CLUSTER_DEMONSTRATED with
    appropriate experimental citations. This is stronger exact-congener support than
    precursor assays or U consumption by WelO5. Preserve producer SOURCE_ASSERTION
    because heterologous protein expression and xenic-culture observations do not
    independently prove axenic native production.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - bgc-primary28225144
  - bgc-welu1-supplement
  - bgc-welu1-accession
  - bgc-primary24677572
  - bgc-primary27348090
- assessment_id: bgc-claim-reference-concern
  area: evidence
  topic: Claim-specific publication attribution
  outcome: concern
  summary: The current producer and locus evidence both cite a compound-level 1987
    reference. The exact modern locus demonstration is recoverable, but its publication
    is absent from the generated claim. Reference routing should be corrected independently
    of evidence-grade retention.
  target_ids:
  - CHEBI:140442
  evidence_ids:
  - bgc-local-routing
  - bgc-cited-doi-metadata
  - bgc-primary28225144
  - bgc-welu1-accession
findings:
- finding_id: R-OCCURRENCE-CITATION
  issue_key: lotus-neyjigpaqakwsi-jo00226a009-occurrence-citation
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: One LOTUS occurrence has unresolved exact-compound and species support
  description: 'The second LOTUS observation cites a 1987 paper whose metadata names
    fontonamide, anhydrohapaloxindole A and H. fontinalis. The record instead asserts
    exact U occurrence in H. welwitschii. This is a provisional citation mismatch:
    full text is needed before concluding that no supporting passage exists. Independent
    support for U occurrence from other publications does not repair this source attribution.'
  target_ids:
  - CHEBI:140442
  field_paths:
  - occurrences[1].evidence[0].reference
  evidence_ids:
  - R-LOCAL
  - bgc-cited-doi-metadata
  - R-1987-ACCESS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Exact structure-taxon-DOI source triple
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Implemented source-row-pinned occurrence exclusion
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated occurrence emission
  rule_id: '.claude/skills/curate-yaml-record/references/review-checklist.md: Occurrences'
  native_severity: 'major: potentially unsupported exact-compound occurrence attribution'
  normalization_reason: A claim-specific source gap is material; certainty stays provisional
    because the full cited article was unavailable.
- finding_id: R-DEFINITION-RANK
  issue_key: chebi-140442-definition-stigonematales-rank
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Definition incorrectly calls Stigonematales a genus
  description: The imported definition says Stigonematales genus. Primary taxonomic
    literature describes Stigonematales as a historical order. This bounded rank error
    is separate from the supported exact chemical identity and producer taxon.
  target_ids:
  - CHEBI:140442
  field_paths:
  - definition
  evidence_ids:
  - R-LOCAL
  - R-TAXON-RANK
  - R-DEFINITION-TRANSFORM
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: CHEBI:140442 sourced definition
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_chebi.py
    role: Definition import
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Definition emission
  rule_id: '.claude/skills/curate-yaml-record/references/review-checklist.md: Identity
    and source fidelity'
  native_severity: 'minor: incorrect taxonomic rank in sourced prose'
  normalization_reason: The definition wording is inaccurate but does not change the
    exact structure or organism identifiers.
- finding_id: bgc-u-claim-reference
  issue_key: mibig-bgc0000668-compound3-claim-reference
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Producer and demonstrated locus reuse a compound reference instead of the
    exact WelU1 experiment
  description: BGC0000668:3 imports DOI:10.1021/jo00226a009 from compound-level evidence
    and repeats it as the sole support for both producer and demonstrated locus. The
    DOI metadata describes a 1987 H. fontinalis isolation paper; no inspected content
    connects it to KF811479.1. Exact U biosynthesis is experimentally supported by
    the 2017 WelU1 study, with the tested accession traceable to this same locus and
    strain. Correct claim-level citation routing while retaining the now-supported
    locus grade. Whether the 1987 paper independently reports this compound is a separate
    unresolved occurrence question; this finding does not assert article-wide absence
    from title alone.
  target_ids:
  - CHEBI:140442
  field_paths:
  - producer_organisms[0].evidence
  - biosynthetic_gene_clusters[0].evidence
  evidence_ids:
  - bgc-local-routing
  - bgc-cited-doi-metadata
  - bgc-primary28225144
  - bgc-welu1-supplement
  - bgc-welu1-accession
  rule_id: 'review-yaml-record Evidence Rules: claim-specific support; docs/record-review-profile.md:
    compound-specific BGC evidence'
  native_severity: 'major: sole producer/locus references do not identify the supporting
    experimental work'
  normalization_reason: One combined citation-routing finding; exact U locus evidence
    is supported by recovered primary experiments, so no separate unsupported-grade
    finding is counted.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: source-pinned producer and locus citation correction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: reference selection and source-level attribution
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: source row BGC0000668:3
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: generated claim evidence
actions:
- action_id: R-VERIFY-OCCURRENCE
  description: Inspect the full 1987 article for exact U and the asserted H. welwitschii
    organism. If unsupported, use the exact-row-pinned LOTUS exclusion table; retain
    independently supported occurrence objects and do not substitute another DOI without
    evidence.
  finding_ids:
  - R-OCCURRENCE-CITATION
  target_ids:
  - CHEBI:140442
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Exact structure-taxon-DOI source triple
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Implemented source-row-pinned occurrence exclusion
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated occurrence emission
  generator: scripts/seed_from_sources.py through documented source-pinned correction
    and guarded seeding
  acceptance_checks:
  - An exact primary passage supports the imported triple, or a pinned exclusion removes
    only NEYJIGPAQAKWSI-QBGRRASTSA-N / NCBITaxon:162986 / literal DOI:10.1021/JO00226A009.
  - Run just seed-canary CHEBI:140442; inspect the generated owner, then documented
    seeding, just validate-strict data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml,
    just verify-reproduction, just verify-corpus --summary and just qc.
- action_id: R-CORRECT-DEFINITION
  description: Correct the sourced definition through a reproducible maintained source
    or supported qualification route. Use an evidence-backed cyanobacterial origin
    statement that avoids calling Stigonematales a genus, and retain transparent attribution
    for any local qualification. Do not hand-edit only the generated YAML.
  finding_ids:
  - R-DEFINITION-RANK
  target_ids:
  - CHEBI:140442
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: CHEBI:140442 sourced definition
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_chebi.py
    role: Definition import
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Definition emission
  generator: scripts/extract_chebi.py and scripts/seed_from_sources.py through documented
    regeneration
  acceptance_checks:
  - A regenerated owner has a scientifically accurate rank or precise organism wording,
    with source attribution preserved and exact structure unchanged.
  - Run the documented seed canary, guarded regeneration, strict validation and reproduction/corpus
    gates; verify that the wording survives regeneration.
- action_id: route-u-claim-references
  description: Use curation/mibig_claim_references.tsv with source key BGC0000668:3
    and the exact source-row hash to route the locus to PMID:28225144 / DOI:10.1039/c7cc00782e,
    documenting its WelU1 accession bridge. Select a separately justified producer
    reference from the strain-specific primary studies or versioned source. Preserve
    source provenance, SOURCE_ASSERTION for native production, and CLUSTER_DEMONSTRATED
    for this exact U congener. Document that the heterologous expression produced
    the enzyme for in vitro assays, not a demonstrated native axenic culture. Do not
    substitute PMID:27348090 as proof of U formation.
  finding_ids:
  - bgc-u-claim-reference
  target_ids:
  - CHEBI:140442
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: source-pinned producer and locus citation correction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: reference selection and source-level attribution
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: source row BGC0000668:3
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: generated claim evidence
  generator: scripts/seed_from_sources.py via documented source-pinned correction
    and guarded regeneration
  acceptance_checks:
  - The generated locus citation identifies an experiment forming exact U, with AHI58823.1
    mapped to KF811479.1 and UTEX B1830.
  - Producer and locus citations are justified separately; native SOURCE_ASSERTION
    and supported CLUSTER_DEMONSTRATED remain distinct.
  - Use just seed-canary CHEBI:140442, inspect output, then documented seeding and
    just validate-strict data/natural_products/alkaloids/12-epi-fischerindole-u-isonitrile.yaml,
    just verify-reproduction, just verify-corpus --summary and just qc.
limitations:
- Primary full text was inspected through the public NCBI efetch XML endpoint. PMC
  web and figure routes returned a challenge and EuropePMC returned an error; no unavailable
  figure is claimed as visually checked.
- The published systematic assignments and product-retention discussion were compared
  with the encoded structure. Spectra, rotations and enzyme experiments were not independently
  remeasured or reinterpreted; published assignment and natural-enantiomer correlation
  remain source-level evidence.
- The inventory uniqueness statement covers the entire pinned eligible ChEBI file
  and direct official inspection of CHEBI:140442; it is not an exhaustive search across
  every current ChEBI entity.
- The complete 1987 cited article remains inaccessible, so the LOTUS citation concern
  is provisional. The 1994 institutional abstract was inspected; its complete original
  isolation methods were not obtained.
- The PMID 27348090 full article methods were recovered via official NCBI XML after
  browser access failures, resolving its occurrence support; raw spectra and crystallographic
  coordinates were not independently reanalysed.
- The 2017 primary main article body did not load; its primary abstract and complete
  public supplement provided the inspected exact enzyme, strain, assay and NMR evidence.
- DOI:10.1021/jo00226a009 full text was not obtained. Official metadata supports citation-scope
  concern but not a claim that U is absent from every passage.
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
- No owner, source inventory, component, curation status or seed history was edited;
  all follow-up actions are proposals.
- The native producer SOURCE_ASSERTION remains distinct from supported occurrence
  and enzyme-locus evidence. A validated partial review does not confer native REVIEWED
  status.
tags:
- path-order-campaign
- batch-001
- fischerindole
```
