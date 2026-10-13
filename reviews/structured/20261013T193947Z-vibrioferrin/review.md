# Vibrioferrin exact-owner scientific review: CHEBI84585 citrate ester

- Review: 20261013T193947Z-vibrioferrin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T19:30:14.763790Z
- Finished UTC: 2026-10-13T19:39:47.006000Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Two confirmed major findings (nonexact PubChem identity and cross-claim citation selection), plus two minor provenance defects; NPAtlas and full primary attribution remain incomplete.

## Scope And Provenance

One exact owner, every nested claim and history, and complete resolved mechanism.

Selection: Next exact pending owner in the full3115-owner campaign; same-label sibling is context and receives its own separate review.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 39811a084202d1c1a47472622e3008bed7000083.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:84585 | data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml | generated | vibrioferrin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| vibrioferrin-inspect | passed | True | CHEBI:84585 | Canonical inspection ran before assessment, captured the current base and exact target/context inputs. |
| strict | passed | True | CHEBI:84585 | Fresh documented strict validation: two owners scanned, zero errors. |
| chemistry | failed | False | CHEBI:84585 | Initial diagnostic stopped at an assumed formula field absent from BGC0002527. No result was saved; corrected retry handles absent source properties explicitly. |
| chemistry-retry | passed | True | CHEBI:84585 | Pinned RDKit2026.03.5 verifies owner SMILES/InChI/key roundtrips, three versioned MIBiG structures, ChEBI neutral/anion distinction and PubChem mismatch. Formula/mass checked only where the source provides them. |
| source-read | passed | False | CHEBI:84585 | Structured NCBI taxonomy/GenBank parsing; all five2011 PDF pages read and rendered; relevant structure/NMR figures visually inspected. |
| html-read | passed | False | CHEBI:84585 | Official2007 publisher HTML parsed with stdlib after bs4 import was unavailable. Only abstract/references and subscription notice accessible; not a full-paper check. |
| corpus | passed | True | CHEBI:84585 | Fresh documented whole-corpus PATHS/filesystem integrity check. |
| labels | passed | True | CHEBI:84585 | Fresh configured ID-label gate, with all nonblocking warnings and no-adapter skips retained. Taxon names do not validate chemical equivalence. |
| queue | passed | False | CHEBI:84585 | Fresh native exhaustive pending-record queue written to a session-specific TSV; scientific status unchanged. |
| local-search | passed | False | CHEBI:84585 | Bounded ignored/hidden-inclusive identifier/label search; compressed archives not claimed text-exhaustive. |
| qc | passed | True | CHEBI:84585 | PRIOR executed native QC:758passed,3skipped,2dependency warnings; all3115 strict/reproduction, source provenance, graph/history, site and governance checks passed. Scientific input hashes match the current checkpoint. This run preceded two scoped successor bundles and an archive test, covered by later canonical/focused checks and full merge-group CI at current39811a084. Not a fresh QC run or scientific approval. |
| Full claim-specific primary attribution | unavailable | True | CHEBI:84585 | 2003 and2016 PMC pages challenged after API500 responses;1992 publisher PDF403;2007 subscription preview only.2013 regulation and2011 receptor studies inspected at abstract level only.1994 abstract was previously captured successfully, but its PubMed page now challenges. These limits prevent full sign-off. |
| Source Wikidata organism mappings | unavailable | True | CHEBI:84585 | Official organism entity endpoints returned403; no alternate retrieval. NCBI verifies scientific taxon identities independently, not these Wikidata mappings. |
| Structured expression-source applicability | not_applicable | False | CHEBI:84585 | The owner names no gene, protein, regulator, pathway step or transcriptomics dataset. Structured MIBiG, NCBI and chemistry sources were inspected first. Publication gene names are contextual, not owner mechanism claims; no iModulonDB coverage/absence claim. |
| NPAtlas exact equivalence | unavailable | True | CHEBI:84585 | Official NPA024673 endpoint returned403. Neither exactness nor mismatch established; no alternate retrieval. |

## Scientific And Domain Assessments

### Exact owner, chemical form and source grouping

identity: supported. Targets: CHEBI:84585.

The neutral ChEBI84585 graph, definition and two MIBiG compound structures agree. The2011 structural figures support its connectivity and epimeric resolution. ChEBI84630 is a distinct trianion, not an equivalent neutral form. Source-strain attribution remains separately limited.

### Encoded chemistry and stereochemical resolution

consistency: supported. Targets: CHEBI:84585.

SMILES, Standard InChI/key and stereo_complete:false roundtrip exactly. Calculated formula/mass are diagnostics, not measurements. Unspecified aminal configuration in IGQX accords with equilibrating epimers; no invented stereo completion. Representation consistency does not rescue the FPHR biological identity.

### Minted/ChEBI grounding and xrefs

grounding: concern. Targets: CHEBI:84585.

EXACT ChEBI84585 grounding is supported; PubChem197680 fails equivalence (F1), while NPA024673 remains unknown after403. No parent, congener or cross-corpus links are asserted.

### Filing, BGC class, organism taxonomy and origin

representation: supported. Targets: CHEBI:84585.

Pinned NPClassifier singleton Amino acids and Peptides correctly files AMINO_ACIDS_AND_PEPTIDES with its version; empty finer classes and nonglycoside flag match the inventory. OTHER is a separate MIBiG BGC assertion; OTHER_BACTERIAL is a taxonomic grouping, not chemical class. No facet is evidence for another.

### Natural origin versus heterologous expression

evidence: supported. Targets: CHEBI:84585.

Natural vibrioferrin provenance is consistent with the inspected isolation/biosynthesis abstracts and source assertions. The2011 heterologous expression makes a known natural molecule and does not by itself make this chemical structure ENGINEERED. Full exact-strain claims remain partial.

### Producer taxon, strain and evidence grade

scope: concern. Targets: CHEBI:84585.

NCBI labels/ranks match; CA is explicitly strain-scoped. WP1 is missing from the0946 producer (F4); AQ3354 belongs to another occurrence. SOURCE_ASSERTION is faithful; native knockout and CA genotype/metabolite evidence need full-text and claim-specific review before grade changes.

### Active versions, locus boundaries and link evidence

provenance: concern. Targets: CHEBI:84585.

0946v5 and2527v2 are active; AB082123.1 and CP005094.1/876779..886792 match the source.0946 zero bounds stay unstated. Empty methods accurately give CLUSTER_UNSTATED. F2 concerns citation routing, not proof that the CA locus is experimentally demonstrated.

### Every occurrence and nearest cited source

evidence: concern. Targets: CHEBI:84585.

All five rows reproduce.2016 abstract supports Azotobacter detection;1994 supports V.parahaemolyticus named-product identity;2003 abstract supports native biosynthesis context.1992 DOI resolves but AQ3354 is source-asserted only.2011 alginolyticus origin is indirect background (F3), not that study's detection experiment. Overlap notes correctly do not claim independent corroboration.

### Reference identity and claim-level placement

evidence: concern. Targets: CHEBI:84585.

References remain typed database assertions. The claim-level objects are present, but the generic bioactivity-first selector misroutes2527 evidence (F2); ChEBI2011 origin needs an indirect-provenance qualification (F3). Raw DOI whitespace is retained source provenance, not treated as a failed resolution.

### Assays, targets, quantities, clinical and sibling claims

completeness: not_applicable. Targets: CHEBI:84585.

No bioactivities, bioactivity_summary, molecular_targets, clinical status, datasets, parents/congeners or related_records are asserted. The PubChem inventory row is explicitly no assay data, not an experiment. Optional empty slots are not defects or global evidence-absence claims.

### Complete native mechanism and component ownership

graph: not_applicable. Targets: CHEBI:84585.

No biosynthetic_pathway, inline causal_graphs or causal_graph_refs on this owner. Complete native reader and243-component inventory agree. The2011 pathway figure is hypothetical and must not be imported as experimentally demonstrated edges. The whole-corpus graph objective remains active elsewhere.

### Discussions, status, history and maintained fix ownership

provenance: supported. Targets: CHEBI:84585.

Three seed events and the OPEN two-BGC shared-structure discussion are preserved. That discussion does not resolve the new xref/citation findings. Status stays SEEDED.

## Findings

### F1: PubChem197680 is not an exact chemical cross-reference

major / open / confirmed; issue key: chebi84585-nonexact-pubchem197680.

The official PubChem response encodes FPHRKFJYHKRDFJ-LWYCVJHGSA-N, whereas this owner and ChEBI84585 encode IGQXNKDXMPSELX-BIAKFKOBSA-N. RDKit and visual comparison confirm four free acids/no ester versus three free acids/one ester. Equal formula and exact mass do not establish equivalence. The incorrect xref originates in BGC0000946:1; BGC0002527:1 contributes a separate NPAtlas identifier whose equivalence remains unknown after403. Withhold only the proven nonexact PubChem assertion, not the NPAtlas identifier.

### F2: A compound-bioactivity citation displaces the entry-specific taxon/locus reference

major / open / confirmed; issue key: mibig-BGC0002527-bioactivity-reference-used-for-locus.

BGC0002527.2 attaches DOI10.1021/ic9016883 to siderophore bioactivity and retains PMID26452553 at entry level. The extractor chooses the former through its generic priority rule, and mibig_evidence reuses it for both the CA producer and CP005094.1 locus. The inspected2009 abstract concerns iron binding/photochemistry and marine bacteria; the2016 abstract explicitly concerns Azotobacter vibrioferrin and genome-based capacity. This confirms cross-claim citation selection, not a claim to have read either full paper or proved their every negative. Preserve the original database assertion and route claim-appropriate references separately. Full2016 evidence is still needed before assigning experimental grades or asserting those coordinates were tested.

### F3: The ChEBI alginolyticus origin citation is indirect, not that study's detection experiment

minor / open / confirmed; issue key: chebi84585-alginolyticus-indirect-origin-citation.

The full PMID22146715 paper does mention V.alginolyticus and V.parahaemolyticus as previously known sources. Its experiment, however, produces structurally characterized vibrioferrin in E.coli from sediment clone MG93-1; the donor taxon is not established by the protein homology comparisons. ChEBI84585 repeats the alginolyticus origin/PMID pair, so the import is faithful. Treat this as indirect prior-literature support and trace the actual isolation/biosynthesis source. Do not infer that alginolyticus cannot produce vibrioferrin, delete the occurrence merely because the paper is indirect, or turn the metagenomic clone into an identified native producer.

### F4: The deposited WP1 strain is missing from the producer claim

minor / open / confirmed; issue key: mibig-BGC0000946-vibrioferrin-source-strain.

AB082123.1 names V.parahaemolyticus strain WP1, but the corresponding BGC0000946 producer has only species-rank NCBITaxon670. The AQ3354 detection_context in a different ChEBI occurrence is not this accession's strain and must not be copied across. CA is already represented by strain-rank NCBITaxon1283330 and needs no inferred taxon replacement.

## Recommended Actions And Acceptance Checks

### A1

Withhold literal pubchem:197680 from BGC0000946:1 with complete-row digest2a6d88d4055ff04c4496c977d1bc1af425c5f12c860c7c85a591c681734cfe7c. Cite the official PubChem response and preserve the rejected assertion in the table-owned discussion. Do not select a replacement CID or exclude NPAtlas based on failed access.

- Reject stale/duplicate pins and xref reintroduction.
- ChEBI identity, NPAtlas assertion and other owner claims unchanged.
- Use maintained input/transform with regression tests; do not patch generated scientific fields.
- For authorized curation: validated writer and append-only event, seeder dry run/canary, exact diff, strict validation, verify-corpus, verify-reproduction and full qc.
- Retain raw source assertions, taxon IDs, source versions and independent producer/locus evidence grades.

### A2

Separate citation selection for compound structure/activity from producer/locus assertions. Preserve2527 bioactivity DOI in its correct source context, retain entry PMID26452553 for its appropriate claim, and inspect the full primary work before upgrading grades. Any extractor/schema change must account for other affected rows rather than silently reassigning the whole corpus.

- Regression fixture has differing compound-bioactivity and entry references and verifies claim-specific routing.
- Pin current2527:1 complete-row digest3be82cba240a164478055eac8f68fd1cceac0f615451f6b31133d121b58a73a1 for a bounded correction.
- Source citation provenance remains DATABASE_ASSERTION unless primary curation is separately justified.
- Use maintained input/transform with regression tests; do not patch generated scientific fields.
- For authorized curation: validated writer and append-only event, seeder dry run/canary, exact diff, strict validation, verify-corpus, verify-reproduction and full qc.
- Retain raw source assertions, taxon IDs, source versions and independent producer/locus evidence grades.

### A3

Qualify the ChEBI2011 alginolyticus occurrence as indirect literature context; trace the actual native detection/production source. Preserve the upstream origin pair and do not replace its taxon with E.coli or infer a metagenomic donor. A generated-row correction requires an implemented tested path; reserved decisions.tsv has no effect.

- Distinguish background organism mention, sequence homology, experimental host and natural producer.
- Any retained direct detection citation supports the exact product and taxon.
- Do not delete a biologically plausible occurrence merely because its current source is indirect.
- Use maintained input/transform with regression tests; do not patch generated scientific fields.
- For authorized curation: validated writer and append-only event, seeder dry run/canary, exact diff, strict validation, verify-corpus, verify-reproduction and full qc.
- Retain raw source assertions, taxon IDs, source versions and independent producer/locus evidence grades.

### A4

Add WP1 to the0946 producer through the existing row-pinned strain table, citing AB082123.1 and the0946:1 digest2a6d88d4055ff04c4496c977d1bc1af425c5f12c860c7c85a591c681734cfe7c. Leave AQ3354 occurrence context and CA strain-rank taxon unchanged.

- Only the correct0946 producer gains WP1 and separate qualifier evidence.
- No invented strain taxid or experimental grade upgrade.
- Use maintained input/transform with regression tests; do not patch generated scientific fields.
- For authorized curation: validated writer and append-only event, seeder dry run/canary, exact diff, strict validation, verify-corpus, verify-reproduction and full qc.
- Retain raw source assertions, taxon IDs, source versions and independent producer/locus evidence grades.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml; Entire raw YAML, all nested evidence, discussions and all three history events | supports | Exact ChEBI-grounded/SEEDED owner with two producers, five occurrences, two BGCs and an OPEN shared-structure task. |
| resolved | /private/tmp/npmech-vibrioferrin-resume-42VRr6/vibrioferrin-resolved.json; Complete read_natural_product view | supports | Resolved and raw views agree; no inline or attached graph components for this owner. |
| inventories | /private/tmp/npmech-vibrioferrin-resume-42VRr6/source-rows.json; Complete parsed source rows, TSV line numbers and full row_digest pins | supports | MIBiG0946:1 line1033,0947:1 line1034,2527:1 line3186; NPClassifier583/964; LOTUS1466-1472/2748-2750; ChEBI84585 line32253 and two origins10800-10801;84630 is a separate trianion. PubChem1608 is an empty assay placeholder. |
| chemistry | /private/tmp/npmech-vibrioferrin-resume-42VRr6/chemistry.json; Owner/MIBiG/ChEBI/PubChem roundtrips and functional-group counts | supports | Both neutral structures calculate C16H22N2O12 and434.117274144Da, charge0. FPHR has two assigned/two undefined centers, four free acids and no ester; IGQX has two assigned/one undefined center, three free acids and one ester. Stereo flags are internally correct; mass equality cannot select identity. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/197680/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; Official PUG REST properties: InChI, InChIKey, SMILES and formula; captured 2026-10-13T18:33:28.326859Z..2026-10-13T18:33:28.758788Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/pubchem197680.json; receipt SHA256 6798e11f45164c0b91d74083154b2591cf47638599ddd9cccbd2993ca0c3dbc2 | supports | CID197680 exactly matches FPHRKFJYHKRDFJ-LWYCVJHGSA-N, not IGQXNKDXMPSELX-BIAKFKOBSA-N. This validates registry representation, not the biological assignment. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/84585/; Default structure, three-star status, definition, chemical_data and both compound_origins; captured 2026-10-13T18:33:28.873693Z..2026-10-13T18:33:29.543360Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/CHEBI84585.json; receipt SHA256 7f8d4be564eecc439576597a8182658e8ea4ea8163f644d003505a5031e92e42 | supports | CHEBI84585 matches the neutral IGQX structure, definition and imported origins. The alginolyticus/PMID22146715 pairing is upstream, not invented by the seeder. AQ3354 is occurrence context only. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=354,663,670,1283330&amp;retmode=xml; TaxId354,663,670,1283330; ScientificName,Rank,Lineage; captured 2026-10-13T18:33:29.935562Z..2026-10-13T18:33:30.370373Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/taxonomy.xml; receipt SHA256 df47337057720cae8d2f28240e58987b198e980b8afb39c547bb33fca9f4de3c | supports | 354,663,670 are species nodes;1283330 is CA strain under354. All are bacterial Gammaproteobacteria, consistent with OTHER_BACTERIAL; taxonomy is independent of filing and natural-versus-engineered origin. |
| sequences | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=DQ201184.2,AB082123.1&amp;rettype=gbwithparts&amp;retmode=xml; DQ201184.2 and AB082123.1 source features, organism/strain/taxid and references; captured 2026-10-13T18:33:30.484659Z..2026-10-13T18:33:30.890466Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/sequences.xml; receipt SHA256 5c0014fba10c8bba3e915e2db8346b87fd29d2ed1ff9a286e03a6d24f30e45e7 | supports | DQ201184.2=V.alginolyticus/MVPO1 (letter O), citation PMID17593352; AB082123.1=V.parahaemolyticus/WP1, citation PMID14617658. Sequence annotation anchors the deposit, not the exact product structure. |
| sequence-ca | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=CP005094.1&amp;seq_start=876779&amp;seq_stop=886792&amp;rettype=gbwithparts&amp;retmode=xml; Explicit876779..886792 subregion, source qualifier and accession version; captured 2026-10-13T18:33:30.999989Z..2026-10-13T18:33:31.549838Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/CP005094-locus.xml; receipt SHA256 7637451f6a620cc98899ecb0c405bb3334ab23b23caaead8c61ded1d9769a367 | supports | The retrieved10014-base segment is from CA and taxon1283330. It is not a10014-base whole genome. Deposited genome metadata does not prove biosynthesis of the precise metabolite. |
| metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fj.1574-6968.1992.tb05311.x%22+OR+DOI%3A%2210.1007%2Fs00203-007-0261-6%22+OR+DOI%3A%2210.1021%2Fic9016883%22+OR+DOI%3A%2210.1021%2Fic9016883%22+OR+DOI%3A%2210.1093%2Foxfordjournals.jbchem.a124432%22+OR+DOI%3A%2210.1111%2Fj.1574-6968.2011.02389.x%22+OR+DOI%3A%2210.1128%2Faem.03160-15%22+OR+DOI%3A%2210.1128%2Fjb.00162-13%22+OR+DOI%3A%2210.1128%2Fjb.185.23.6938-6949.2003%22+OR+DOI%3A%2210.1271%2Fbbb.110379%22+OR+%28EXT_ID%3A14617658+AND+SRC%3AMED%29+OR+%28EXT_ID%3A17593352+AND+SRC%3AMED%29+OR+%28EXT_ID%3A22146715+AND+SRC%3AMED%29&amp;format=json&amp;resultType=core&amp;pageSize=100; Eight EuropePMC core records and full returned abstracts; DOI/PMID aliases resolved; captured 2026-10-13T18:33:25.693443Z..2026-10-13T18:33:26.796795Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/metadata.json; receipt SHA256 ab6411f5f6962beeb566a5547362070ee3641826d86380b97ea5f7573617009f | partial | 1994 identifies a citrate ester with equilibrating epimers;2003/2007 describe native siderophore disruption;2011 receptor work concerns uptake;2013 concerns RyhB/Hfq regulation;2009 concerns iron binding/photochemistry;2016 concerns Azotobacter chelome;2011 metagenomic expression is verified against full text. Abstract-only evidence does not settle all strain and product claims. |
| primary2011 | https://www.jstage.jst.go.jp/article/bbb/75/12/75_110379/_pdf; All five PDF pages; pp2284-2285 Figures1,3/Table1 visually inspected; pp2286-2287 methods/reference list; captured 2026-10-13T19:30:16.635878Z..2026-10-13T19:30:18.149789Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-resume-42VRr6/jstage2011.pdf; receipt SHA256 105381ec17c439d7bd021afe21c95c7871a7957b9cb9afd35ce9b61b5c4684ea | supports | Purified MG93-1 E.coli product has citrate-ethanolamine ester connectivity and interconverting aminal epimers. Native Vibrio species are prior-literature context; environmental donor remains unidentified. Figure4 is explicitly hypothetical, based on homology, and does not establish individual enzyme steps experimentally. |
| primary2007 | https://doi.org/10.1007/s00203-007-0261-6; Publisher abstract, source references and subscription preview notice; captured 2026-10-13T19:32:33.829658Z..2026-10-13T19:32:36.516188Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-resume-42VRr6/primary2007.html; receipt SHA256 195fce28fee626bbf37df8e1babf0d08f4cd67adfefcba0141475e40141d2c83 | partial | MVP01 (zero) is the publisher spelling. Abstract reports native pvsA/pvsD disruption and siderophore rescue. Full experiment/structure details require subscription and were not accessed; no alternate retrieval. |
| doi1992 | https://api.crossref.org/works/10.1111/j.1574-6968.1992.tb05311.x; DOI,title,bibliographic metadata and publisher PDF link; captured 2026-10-13T19:31:39.461660Z..2026-10-13T19:31:39.776050Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-resume-42VRr6/crossref1992.json; receipt SHA256 0dab6e5d80d7ba31dd9ba27b912fc8c10c2a9387d9c881f73242c3a1451ed62c | supports | The DOI resolves to the1992 V.parahaemolyticus isolation study. This does not verify AQ3354 against full text; the linked publisher PDF returned403. |
| access | /private/tmp/npmech-vibrioferrin-resume-42VRr6/web-observations.json; Recorded source-page challenge observations, separate from earlier structured metadata | unknown | PMC262695,PMC4702634 and PubMed7961600 displayed reCAPTCHA. EPMC XML500 is an endpoint failure, not article content. After explicit access challenges, no alternate retrieval was attempted. |
| wikidata-access | https://www.wikidata.org/wiki/Special:EntityData/Q134280.json; Official Q134280 denial payload; additional403 receipts forQ3556827 andQ2157875 preserved in capture.json; captured 2026-10-13T18:33:31.653729Z..2026-10-13T18:33:31.713504Z; HTTP403; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/wikidata-Q134280.json; receipt SHA256 fce6db281a4ffd53fdee829827fef899f288f12b8b4582854105aa4c3befc08e | unknown | 403 prevents current Wikidata mapping verification. NCBI identity verification does not recover these denied mappings. |
| citation-selector | scripts/extract_mibig.py; primary_reference, lines189-220 | supports | Generic selection prioritizes compound evidence, then compound bioactivity, then legacy entry references. The same single primary_reference/reference_basis pair becomes an inventory row. |
| citation-emitter | scripts/seed_from_sources.py; mibig_evidence and mibig_cluster, lines660-727; producer caller | supports | Producer and locus use the same selected row reference with DATABASE_ASSERTION and a source-level note. This preserves type but can misroute claim-specific evidence. |
| ownership | docs/CURATION.md; Implemented structure, xref, strain and locus-evidence correction paths | supports | decisions.tsv is reserved/unconsumed. Existing REPLACE_WITH_CHEBI rejects occupied destination keys, so FPHR-to-existing-IGQX is not an automatic replacement. Xref and strain tables are narrow row-pinned mechanisms. |
| rules | docs/HARMONIZATION.md; Exact structure identity, source claims, occurrence/production and computed filing rules | supports | Database assertion remains a database assertion. Locus and producer evidence grades are independent; neither taxonomy nor computed classification establishes origin. |
| local-search | /private/tmp/npmech-vibrioferrin-resume-42VRr6/local-search.log; Ignored/hidden-inclusive bounded rg search | supports | Matches are source rows, exact owners, derived queues and historical coverage archives. No matching implemented correction row or earlier canonical assessment found within this search. |
| capture | /private/tmp/npmech-vibrioferrin-resume-42VRr6/capture.json; All3115owners,243components,38prior immutable pairs and current inspection hashes | supports | Full checkpoint reverified. Only prior-context change is three unrelated myxochromide strain rows; no vibrioferrin input/owner changed. Science remains uncurated. |
| native-gates | /private/tmp/npmech-myxochromide-publish-MyX4Nq/qc.log; Prior executed full native QC; receipt and current hash attestation | supports | 758tests passed,3skipped; all3115strict/reproduction and native gates passed. Later merge-group CI at the current base passed; fresh local target/corpus/label/review checks are separate from this prior run. |
| mibig-BGC0000946.5 | https://mibig.secondarymetabolites.org/repository/BGC0000946.5/annotations.json; Exact accession/version/status, compounds[0], taxonomy,loci,classes and legacy_references; captured 2026-10-13T18:33:26.958447Z..2026-10-13T18:33:27.497463Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/BGC0000946.5.json; receipt SHA256 c6f0fb85cfc805d53848fbc09eb6d66084853c63d4b20935b087174d44c0e0e8 | supports | Active versioned source matches the imported graph/taxon/accession. Locus evidence methods are empty, correctly imported as SOURCE_ASSERTION/CLUSTER_UNSTATED; quality and review placeholders are not truth signals. No claim of latest version. |
| mibig-BGC0002527.2 | https://mibig.secondarymetabolites.org/repository/BGC0002527.2/annotations.json; Exact accession/version/status, compounds[0], taxonomy,loci,classes and legacy_references; captured 2026-10-13T18:33:27.611612Z..2026-10-13T18:33:28.223442Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/BGC0002527.2.json; receipt SHA256 b49582e3f48e34e9c117758e05143fdadb777215648bcf2836d61a83101f753b | supports | Active versioned source matches the imported graph/taxon/accession. Locus evidence methods are empty, correctly imported as SOURCE_ASSERTION/CLUSTER_UNSTATED; quality and review placeholders are not truth signals. No claim of latest version. |
| npatlas-access | https://www.npatlas.org/api/v1/compound/NPA024673?include=classifications; Official API denial payload; captured 2026-10-13T18:33:29.646890Z..2026-10-13T18:33:29.820673Z; HTTP403; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/NPA024673.json; receipt SHA256 1a32a5494e5b908c8e1c8ad127a3b8283a900a44d84f614ff92410a6ac4d8efc | unknown | HTTP403; exact equivalence unresolved, not evidence that the identifier is absent or wrong. |

## Limits And Additional Notes

- Required full-text attribution remains incomplete:1992 PDF403,2003/2016 PMC challenges after XML500,2007 subscription preview,1994 abstract only;2013 regulatory and2011 receptor sources read as abstracts only. No alternate retrieval after denial.
- Official Wikidata organism endpoints returned403. NCBI taxonomy verification does not validate those source mappings.
- Current calculations establish source graph consistency and differences, not experimental assignment in every source strain. The2011 pathway is hypothetical.
- Full native QC/reproduction is explicitly a verified prior run; current target strict, chemistry, corpus, label and later review-output checks are separate. Existing skips/warnings remain.
- Only new canonical review pairs are written to the repository; external payloads/receipts remain temporary, with stable source URLs and hashes recorded. No publisher PDF redistributed.
- No scientific record, source inventory, history, page or native status was changed. This does not complete the whole-corpus goal.
- NPA024673 exact equivalence remains unknown after403; no exclusion inferred from access failure.
- Base39811a084202d1c1a47472622e3008bed7000083 and43captured context/target inputs were verified against Git bytes.
- The old source scan omitted exact-ID ChEBI origins; this review uses the corrected complete structured join.
- The local checklist mentions decisions.tsv, but the current profile/CURATION implementation explicitly says it is reserved and unconsumed.
- Both records have three history events, not two; the source strain WP1 must not be confused with AQ3354.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T193947Z-vibrioferrin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Vibrioferrin exact-owner scientific review: CHEBI84585 citrate ester'
started_at: '2026-10-13T19:30:14.763790Z'
finished_at: '2026-10-13T19:39:47.006000Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant performing the ongoing audit; not an independent
    reviewer or human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: SEEDED retained; REVIEWED gate not met
scientific_review: true
summary: Two confirmed major findings (nonexact PubChem identity and cross-claim citation
  selection), plus two minor provenance defects; NPAtlas and full primary attribution
  remain incomplete.
source:
  git_revision: 39811a084202d1c1a47472622e3008bed7000083
  state: git_commit
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: CLAUDE.md
    sha256: 49e2ab03c7e82013e9d68356de2c9965c9f8517a3408a44124076f4ca1b529cd
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
  - path: curation/decisions.tsv
    sha256: 7214a74975fb2cb65521da18dd14ea1c65665f50060106976dc0db9caf887805
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: a1eb14fec4a7cee0c2fc25c43091e75af24ae62c44c4f7659ed7aedf0e6a0e6c
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 1688222f88ac4b89e831f95fed2bb7b2be04cd01eac0322ba9b0c8227b3c62a6
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: a4627732141b210992a2bac02fc4dc24eb7edb01b810873ce0f03cdcada7b5f7
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/amino_acids_and_peptides/vibrioferrin-2.yaml
    sha256: 3c28085e27066e5a22add10d008fe8a30e0b21f80d322dcc28f345b795f293d9
    role: context
  - path: data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
    sha256: 935bc847e79f24413d9b9d74a5eda47056a1fe1b29b6dc76cd2002b6c7d9e666
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 373f049029be3db137e062ff5f872a2400a9d5b423f3e108ea44ebde2f8dcc7d
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
  - path: data/raw/lotus_occurrences.tsv
    sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
    role: context
  - path: data/raw/mibig_compounds.tsv
    sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
    role: context
  - path: data/raw/npclassifier.tsv
    sha256: 7b9b9f78f5b14aea9fabb163bbaa9e842920a7e9b07deac8f98c97666e9e23fc
    role: context
  - path: data/raw/pubchem_bioassay.tsv
    sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
    role: context
  - path: docs/CURATION.md
    sha256: 245df036e09a00a2f92a5f78c70eadb210cef7d70046e8ee35377a9e636cd30b
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
  - path: scripts/extract_lotus.py
    sha256: 8a8c524f60f85d2bb54412ca055a6a45e0d37ec5f4584d8d70be454b8f664290
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/run_qc.py
    sha256: ff44ed3e40a9b3582eb84e38a81301745ae80d16445756d09a7efb2a480b1abb
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 8d82d7633e0492e9fe16011f6e5af6f8024f573e80c8a24176b65e2941478b71
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: 6026ddca19f0989d499b1681f7724fbab23918de8d3957750b49bbfe1a9c0bff
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: a8b8834788b4714cf1cb0d1cc410d5c2f88112a32ad8621c8e043f0a4bc38a9d
    role: context
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
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
  - path: uv.lock
    sha256: c62a5739e3ffeb12cc57b3bf12a31dcf9cdfbf00b417f4ba3a801d51ef9efbe3
    role: context
scope:
  description: One exact owner, every nested claim and history, and complete resolved
    mechanism.
  selection: Next exact pending owner in the full3115-owner campaign; same-label sibling
    is context and receives its own separate review.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CHEBI:84585
  exclusions:
  - target: Other3114 owners and their attached components
    reason: Not assessed by this single-owner observation; all3115owners/243components,
      previous partial reviews and unassessed remainder remain in scope.
targets:
- target_id: CHEBI:84585
  path: data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
  label: vibrioferrin
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported chemical, producer and cluster assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Imported structure-organism-reference triples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned ChEBI grounding inventory
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Pinned ChEBI occurrence inventory
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned computed classification
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned sibling exact-structure joins
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated harmonization and grading
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: LOTUS extraction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Implemented pinned structure corrections
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Implemented exact-context method corrections
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented pinned strain qualifications
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Implemented complete-row-pinned PubChem and NPAtlas exclusions
checks:
- check_id: vibrioferrin-inspect
  name: vibrioferrin-inspect
  status: passed
  required: true
  command: .venv/bin/python scripts/record_review.py inspect --targets /private/tmp/npmech-vibrioferrin-resume-42VRr6/vibrioferrin-targets.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/review-yaml-record/SKILL.md --input CLAUDE.md --input conf/id_label_targets.yaml
    --input conf/producer_evidence.tsv --input conf/record_review.yaml --input curation/decisions.tsv
    --input curation/mibig_locus_evidence_overrides.tsv --input curation/mibig_producer_strains.tsv
    --input curation/mibig_structure_corrections.tsv --input curation/mibig_xref_exclusions.tsv
    --input data/natural_products/PATHS.tsv --input data/natural_products/amino_acids_and_peptides/vibrioferrin-2.yaml
    --input data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml --input
    data/raw/MANIFEST.yaml --input data/raw/antibioticmech_inchikeys.tsv --input data/raw/chebi_origins.tsv
    --input data/raw/chebi_structures.tsv --input data/raw/corpus_taxa.obo --input
    data/raw/lotus_occurrences.tsv --input data/raw/mibig_compounds.tsv --input data/raw/npclassifier.tsv
    --input data/raw/pubchem_bioassay.tsv --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/record-review-profile.md --input docs/record-reviews.md --input justfile
    --input pyproject.toml --input schema/record_review.yaml --input scripts/extract_lotus.py
    --input scripts/extract_mibig.py --input scripts/record_review.py --input scripts/run_qc.py
    --input scripts/seed_from_sources.py --input src/naturalproductmech/curate/producer_strains.py
    --input src/naturalproductmech/curate/structure_corrections.py --input src/naturalproductmech/curate/xref_exclusions.py
    --input src/naturalproductmech/graph_components.py --input src/naturalproductmech/schema/history.yaml
    --input src/naturalproductmech/schema/mech_shared.yaml --input src/naturalproductmech/schema/naturalproductmech.yaml
    --input uv.lock
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Canonical inspection ran before assessment, captured the current base and
    exact target/context inputs.
  scope_note: Actual run 2026-10-13T19:30:23.318296Z..2026-10-13T19:30:29.594986Z;
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/vibrioferrin-inspect.json; SHA256
    50b6fc71cc1def81d176a584c14d35f3a4f8e585c46bd3c6f249cadd799f9722
- check_id: strict
  name: strict
  status: passed
  required: true
  command: just validate-strict data/natural_products/amino_acids_and_peptides/vibrioferrin-2.yaml
    data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml --out /private/tmp/npmech-vibrioferrin-resume-42VRr6/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: 'Fresh documented strict validation: two owners scanned, zero errors.'
  scope_note: Actual run 2026-10-13T19:32:25.976768Z..2026-10-13T19:32:31.473180Z;
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/strict.log; SHA256 bf77467c70fca28bc2f07583c587d0671d19bccc5616a76540da8ab6a4c69cb0
- check_id: chemistry
  name: chemistry
  status: failed
  required: false
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/src:/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-vibrioferrin-resume-42VRr6/chemistry.py
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Initial diagnostic stopped at an assumed formula field absent from BGC0002527.
    No result was saved; corrected retry handles absent source properties explicitly.
  scope_note: Actual run 2026-10-13T19:31:36.168652Z..2026-10-13T19:31:39.970282Z;
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/chemistry.log; SHA256 a03be05be67585cd0edc14cecfa542cbb4020090d07da79d2e86a5237d099f51
- check_id: chemistry-retry
  name: chemistry-retry
  status: passed
  required: true
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/src:/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-vibrioferrin-resume-42VRr6/chemistry.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Pinned RDKit2026.03.5 verifies owner SMILES/InChI/key roundtrips, three
    versioned MIBiG structures, ChEBI neutral/anion distinction and PubChem mismatch.
    Formula/mass checked only where the source provides them.
  scope_note: Actual run 2026-10-13T19:32:22.472629Z..2026-10-13T19:32:25.358091Z;
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/chemistry-retry.log; SHA256 e668f0f7400a6cf2cb04522585f8e1a7441a54acf4adc56437955e477f8d27af
- check_id: source-read
  name: source-read
  status: passed
  required: false
  command: env PYTHONPATH=/private/tmp/antibioticmech-pdf-tools-20261009 .venv/bin/python
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/read_sources.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Structured NCBI taxonomy/GenBank parsing; all five2011 PDF pages read and
    rendered; relevant structure/NMR figures visually inspected.
  scope_note: Actual run 2026-10-13T19:31:35.330300Z..2026-10-13T19:31:36.042621Z;
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/source-read.log; SHA256 638646023d9d40c9d931bdf95c6cd3a210928ae7530dd1906041cd745c2d14d6
- check_id: html-read
  name: html-read
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/npmech-vibrioferrin-resume-42VRr6/html_read.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Official2007 publisher HTML parsed with stdlib after bs4 import was unavailable.
    Only abstract/references and subscription notice accessible; not a full-paper
    check.
  scope_note: Actual run 2026-10-13T19:34:22.405303Z..2026-10-13T19:34:22.522026Z;
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/html-read.log; SHA256 342f2675a8c02b052b4910ddf229259dd8bb42c342953c2dd386fa7c3799dbfc
- check_id: corpus
  name: corpus
  status: passed
  required: true
  command: just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Fresh documented whole-corpus PATHS/filesystem integrity check.
  scope_note: Actual run 2026-10-13T19:34:24.894606Z..2026-10-13T19:36:35.434949Z;
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/corpus.log; SHA256 99919ecf8be13f6447470547d51601b47f57ec19836b0254cb62cbf94b505a1c
- check_id: labels
  name: labels
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Fresh configured ID-label gate, with all nonblocking warnings and no-adapter
    skips retained. Taxon names do not validate chemical equivalence.
  scope_note: Actual run 2026-10-13T19:34:58.847775Z..2026-10-13T19:37:52.611294Z;
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/labels.log; SHA256 19a4f6cca7894851de23ee2062f52d29b32def53c7b4f59edbc6c45ec4ce9828
- check_id: queue
  name: queue
  status: passed
  required: false
  command: just review-queue --tsv /private/tmp/npmech-vibrioferrin-resume-42VRr6/native-queue.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Fresh native exhaustive pending-record queue written to a session-specific
    TSV; scientific status unchanged.
  scope_note: Actual run 2026-10-13T19:32:30.312502Z..2026-10-13T19:33:33.182675Z;
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/queue.log; SHA256 ee040a45a0359b75de8aaf016da182b243fc67a481a1b3b9079285eb16724d8e
- check_id: local-search
  name: local-search
  status: passed
  required: false
  command: rg --no-ignore --hidden -l -i 'vibrioferrin|FPHRKFJYHKRDFJ|IGQXNKDXMPSELX|BGC0000946|BGC0000947|BGC0002527|NPA024673|22146715|197680|84585'
    curation data/raw data/natural_products data/causal_graphs reviews docs scripts
    src conf tests
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Bounded ignored/hidden-inclusive identifier/label search; compressed archives
    not claimed text-exhaustive.
  scope_note: Actual run 2026-10-13T19:32:49.109778Z..2026-10-13T19:32:49.260726Z;
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/local-search.log; SHA256 9cccc27fea367694d52a91370b9605c091d95d4a2dee9d2604447309964fcf11
- check_id: qc
  name: qc
  status: passed
  required: true
  command: env RECORD_REVIEW_BASE=606252dd3e23f7b3da0120a8cc7732bd01efecc8 .venv/bin/python
    scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: PRIOR executed native QC:758passed,3skipped,2dependency warnings; all3115
    strict/reproduction, source provenance, graph/history, site and governance checks
    passed. Scientific input hashes match the current checkpoint. This run preceded
    two scoped successor bundles and an archive test, covered by later canonical/focused
    checks and full merge-group CI at current39811a084. Not a fresh QC run or scientific
    approval.
  scope_note: Actual run 2026-10-13T18:42:37.393405Z..2026-10-13T18:56:46.781998Z;
    /private/tmp/npmech-myxochromide-publish-MyX4Nq/qc.log; SHA256 65b3d5000a0b19a843eb64aedd3e2716a3b2db5fea35ad59cfb85b317711b210
- check_id: primary-attribution
  name: Full claim-specific primary attribution
  status: unavailable
  required: true
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - metadata
  - access
  - primary2007
  summary: 2003 and2016 PMC pages challenged after API500 responses;1992 publisher
    PDF403;2007 subscription preview only.2013 regulation and2011 receptor studies
    inspected at abstract level only.1994 abstract was previously captured successfully,
    but its PubMed page now challenges. These limits prevent full sign-off.
- check_id: wikidata
  name: Source Wikidata organism mappings
  status: unavailable
  required: true
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - wikidata-access
  summary: Official organism entity endpoints returned403; no alternate retrieval.
    NCBI verifies scientific taxon identities independently, not these Wikidata mappings.
- check_id: imodulondb
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  target_ids:
  - CHEBI:84585
  summary: The owner names no gene, protein, regulator, pathway step or transcriptomics
    dataset. Structured MIBiG, NCBI and chemistry sources were inspected first. Publication
    gene names are contextual, not owner mechanism claims; no iModulonDB coverage/absence
    claim.
- check_id: npatlas-equivalence
  name: NPAtlas exact equivalence
  status: unavailable
  required: true
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - npatlas-access
  summary: Official NPA024673 endpoint returned403. Neither exactness nor mismatch
    established; no alternate retrieval.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
  locator: Entire raw YAML, all nested evidence, discussions and all three history
    events
  accessed_at: '2026-10-13T19:39:46.996684Z'
  support: supports
  summary: Exact ChEBI-grounded/SEEDED owner with two producers, five occurrences,
    two BGCs and an OPEN shared-structure task.
  snapshot_sha256: 935bc847e79f24413d9b9d74a5eda47056a1fe1b29b6dc76cd2002b6c7d9e666
- evidence_id: resolved
  kind: record_content
  reference: /private/tmp/npmech-vibrioferrin-resume-42VRr6/vibrioferrin-resolved.json
  locator: Complete read_natural_product view
  accessed_at: '2026-10-13T19:39:46.996830Z'
  support: supports
  summary: Resolved and raw views agree; no inline or attached graph components for
    this owner.
  snapshot_sha256: 77d9b99927295968eb5196448f5f8d1361f0bbf12fb986ac09d4d0d1ca0cd3ee
- evidence_id: inventories
  kind: database
  reference: /private/tmp/npmech-vibrioferrin-resume-42VRr6/source-rows.json
  locator: Complete parsed source rows, TSV line numbers and full row_digest pins
  accessed_at: '2026-10-13T19:39:46.996952Z'
  support: supports
  summary: MIBiG0946:1 line1033,0947:1 line1034,2527:1 line3186; NPClassifier583/964;
    LOTUS1466-1472/2748-2750; ChEBI84585 line32253 and two origins10800-10801;84630
    is a separate trianion. PubChem1608 is an empty assay placeholder.
  snapshot_sha256: d8a2ee338b5ea25b304709702431c55c701797b8428db90898fb9ef0b645bd7b
  search_scope: Full structured scans of seven TSVs by exact keys, name and exact
    ChEBI IDs. The old scan missed ChEBI origins by not joining IDs; its zero count
    was not absence evidence. No exact-key AntibioticMech row in this pinned inventory;
    not global absence.
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-vibrioferrin-resume-42VRr6/chemistry.json
  locator: Owner/MIBiG/ChEBI/PubChem roundtrips and functional-group counts
  accessed_at: '2026-10-13T19:39:46.997072Z'
  support: supports
  summary: Both neutral structures calculate C16H22N2O12 and434.117274144Da, charge0.
    FPHR has two assigned/two undefined centers, four free acids and no ester; IGQX
    has two assigned/one undefined center, three free acids and one ester. Stereo
    flags are internally correct; mass equality cannot select identity.
  snapshot_sha256: 331b305cb023d835a515a09e65b5d21e6e30dc40180c12cae9b6cdb15e147507
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/197680/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: 'Official PUG REST properties: InChI, InChIKey, SMILES and formula; captured
    2026-10-13T18:33:28.326859Z..2026-10-13T18:33:28.758788Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/pubchem197680.json;
    receipt SHA256 6798e11f45164c0b91d74083154b2591cf47638599ddd9cccbd2993ca0c3dbc2'
  accessed_at: '2026-10-13T19:39:46.997420Z'
  support: supports
  summary: CID197680 exactly matches FPHRKFJYHKRDFJ-LWYCVJHGSA-N, not IGQXNKDXMPSELX-BIAKFKOBSA-N.
    This validates registry representation, not the biological assignment.
  snapshot_sha256: 4edd74b20923622244a9f3f8485c619e4376b9898b42d2a0129b45fa47ab0ba5
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/84585/
  locator: Default structure, three-star status, definition, chemical_data and both
    compound_origins; captured 2026-10-13T18:33:28.873693Z..2026-10-13T18:33:29.543360Z;
    HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/CHEBI84585.json;
    receipt SHA256 7f8d4be564eecc439576597a8182658e8ea4ea8163f644d003505a5031e92e42
  accessed_at: '2026-10-13T19:39:46.997684Z'
  support: supports
  summary: CHEBI84585 matches the neutral IGQX structure, definition and imported
    origins. The alginolyticus/PMID22146715 pairing is upstream, not invented by the
    seeder. AQ3354 is occurrence context only.
  snapshot_sha256: e6fc9b11e3497b91083ab04d102260c96513548a22d0539172fbdd9a562d7b0b
- evidence_id: taxonomy
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=354,663,670,1283330&retmode=xml
  locator: TaxId354,663,670,1283330; ScientificName,Rank,Lineage; captured 2026-10-13T18:33:29.935562Z..2026-10-13T18:33:30.370373Z;
    HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/taxonomy.xml;
    receipt SHA256 df47337057720cae8d2f28240e58987b198e980b8afb39c547bb33fca9f4de3c
  accessed_at: '2026-10-13T19:39:46.997992Z'
  support: supports
  summary: 354,663,670 are species nodes;1283330 is CA strain under354. All are bacterial
    Gammaproteobacteria, consistent with OTHER_BACTERIAL; taxonomy is independent
    of filing and natural-versus-engineered origin.
  snapshot_sha256: 0a9ff030e6781fef4b7427f64d04a3582e25dc747aa9ba42042b8f707175b54f
- evidence_id: sequences
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=DQ201184.2,AB082123.1&rettype=gbwithparts&retmode=xml
  locator: DQ201184.2 and AB082123.1 source features, organism/strain/taxid and references;
    captured 2026-10-13T18:33:30.484659Z..2026-10-13T18:33:30.890466Z; HTTP200; payload
    /private/tmp/npmech-vibrioferrin-review-eZIUfP/sequences.xml; receipt SHA256 5c0014fba10c8bba3e915e2db8346b87fd29d2ed1ff9a286e03a6d24f30e45e7
  accessed_at: '2026-10-13T19:39:46.998448Z'
  support: supports
  summary: DQ201184.2=V.alginolyticus/MVPO1 (letter O), citation PMID17593352; AB082123.1=V.parahaemolyticus/WP1,
    citation PMID14617658. Sequence annotation anchors the deposit, not the exact
    product structure.
  snapshot_sha256: 44c416b5845230dc813b9dadc0df98e04391648993dfe4d96bed1b02eca13526
- evidence_id: sequence-ca
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=CP005094.1&seq_start=876779&seq_stop=886792&rettype=gbwithparts&retmode=xml
  locator: Explicit876779..886792 subregion, source qualifier and accession version;
    captured 2026-10-13T18:33:30.999989Z..2026-10-13T18:33:31.549838Z; HTTP200; payload
    /private/tmp/npmech-vibrioferrin-review-eZIUfP/CP005094-locus.xml; receipt SHA256
    7637451f6a620cc98899ecb0c405bb3334ab23b23caaead8c61ded1d9769a367
  accessed_at: '2026-10-13T19:39:46.998784Z'
  support: supports
  summary: The retrieved10014-base segment is from CA and taxon1283330. It is not
    a10014-base whole genome. Deposited genome metadata does not prove biosynthesis
    of the precise metabolite.
  snapshot_sha256: c91441f6317b10a1105c721bfc06564ca1dd47bb40b0e1dbb85635c908d175d6
- evidence_id: metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fj.1574-6968.1992.tb05311.x%22+OR+DOI%3A%2210.1007%2Fs00203-007-0261-6%22+OR+DOI%3A%2210.1021%2Fic9016883%22+OR+DOI%3A%2210.1021%2Fic9016883%22+OR+DOI%3A%2210.1093%2Foxfordjournals.jbchem.a124432%22+OR+DOI%3A%2210.1111%2Fj.1574-6968.2011.02389.x%22+OR+DOI%3A%2210.1128%2Faem.03160-15%22+OR+DOI%3A%2210.1128%2Fjb.00162-13%22+OR+DOI%3A%2210.1128%2Fjb.185.23.6938-6949.2003%22+OR+DOI%3A%2210.1271%2Fbbb.110379%22+OR+%28EXT_ID%3A14617658+AND+SRC%3AMED%29+OR+%28EXT_ID%3A17593352+AND+SRC%3AMED%29+OR+%28EXT_ID%3A22146715+AND+SRC%3AMED%29&format=json&resultType=core&pageSize=100
  locator: Eight EuropePMC core records and full returned abstracts; DOI/PMID aliases
    resolved; captured 2026-10-13T18:33:25.693443Z..2026-10-13T18:33:26.796795Z; HTTP200;
    payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/metadata.json; receipt
    SHA256 ab6411f5f6962beeb566a5547362070ee3641826d86380b97ea5f7573617009f
  accessed_at: '2026-10-13T19:39:46.999149Z'
  support: partial
  summary: 1994 identifies a citrate ester with equilibrating epimers;2003/2007 describe
    native siderophore disruption;2011 receptor work concerns uptake;2013 concerns
    RyhB/Hfq regulation;2009 concerns iron binding/photochemistry;2016 concerns Azotobacter
    chelome;2011 metagenomic expression is verified against full text. Abstract-only
    evidence does not settle all strain and product claims.
  snapshot_sha256: b069f711e5635e005035d88fdfcbe09a4931e5536f69aec123134f801680276d
- evidence_id: primary2011
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/bbb/75/12/75_110379/_pdf
  locator: All five PDF pages; pp2284-2285 Figures1,3/Table1 visually inspected; pp2286-2287
    methods/reference list; captured 2026-10-13T19:30:16.635878Z..2026-10-13T19:30:18.149789Z;
    HTTP200; payload /private/tmp/npmech-vibrioferrin-resume-42VRr6/jstage2011.pdf;
    receipt SHA256 105381ec17c439d7bd021afe21c95c7871a7957b9cb9afd35ce9b61b5c4684ea
  accessed_at: '2026-10-13T19:39:46.999992Z'
  support: supports
  summary: Purified MG93-1 E.coli product has citrate-ethanolamine ester connectivity
    and interconverting aminal epimers. Native Vibrio species are prior-literature
    context; environmental donor remains unidentified. Figure4 is explicitly hypothetical,
    based on homology, and does not establish individual enzyme steps experimentally.
  snapshot_sha256: 9c277977a917aaaa97e4585dc8e4422447cefd04c5966089c4c4820484d9c16a
- evidence_id: primary2007
  kind: primary_source
  reference: https://doi.org/10.1007/s00203-007-0261-6
  locator: Publisher abstract, source references and subscription preview notice;
    captured 2026-10-13T19:32:33.829658Z..2026-10-13T19:32:36.516188Z; HTTP200; payload
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/primary2007.html; receipt SHA256
    195fce28fee626bbf37df8e1babf0d08f4cd67adfefcba0141475e40141d2c83
  accessed_at: '2026-10-13T19:39:47.000912Z'
  support: partial
  summary: MVP01 (zero) is the publisher spelling. Abstract reports native pvsA/pvsD
    disruption and siderophore rescue. Full experiment/structure details require subscription
    and were not accessed; no alternate retrieval.
  snapshot_sha256: f24ea9624dc26e15ee7b98820c11683e9192def334a249cb804bf0be607ba38f
- evidence_id: doi1992
  kind: authority
  reference: https://api.crossref.org/works/10.1111/j.1574-6968.1992.tb05311.x
  locator: DOI,title,bibliographic metadata and publisher PDF link; captured 2026-10-13T19:31:39.461660Z..2026-10-13T19:31:39.776050Z;
    HTTP200; payload /private/tmp/npmech-vibrioferrin-resume-42VRr6/crossref1992.json;
    receipt SHA256 0dab6e5d80d7ba31dd9ba27b912fc8c10c2a9387d9c881f73242c3a1451ed62c
  accessed_at: '2026-10-13T19:39:47.001177Z'
  support: supports
  summary: The DOI resolves to the1992 V.parahaemolyticus isolation study. This does
    not verify AQ3354 against full text; the linked publisher PDF returned403.
  snapshot_sha256: 1642719f6c7b12f928b5cf61d4900acc6c41c2841798804c0aca0d62e4cda890
- evidence_id: access
  kind: search
  reference: /private/tmp/npmech-vibrioferrin-resume-42VRr6/web-observations.json
  locator: Recorded source-page challenge observations, separate from earlier structured
    metadata
  accessed_at: '2026-10-13T19:39:47.001201Z'
  support: unknown
  summary: PMC262695,PMC4702634 and PubMed7961600 displayed reCAPTCHA. EPMC XML500
    is an endpoint failure, not article content. After explicit access challenges,
    no alternate retrieval was attempted.
  snapshot_sha256: 358c1a4fc2edd290ba99f4fe36ab829af108b3f35df824342daf9643ef241233
  search_scope: Two recorded web queries, primary-source page opens only. Snippets
    and uninspected2026 computational-study lead do not support findings.
- evidence_id: wikidata-access
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q134280.json
  locator: Official Q134280 denial payload; additional403 receipts forQ3556827 andQ2157875
    preserved in capture.json; captured 2026-10-13T18:33:31.653729Z..2026-10-13T18:33:31.713504Z;
    HTTP403; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/wikidata-Q134280.json;
    receipt SHA256 fce6db281a4ffd53fdee829827fef899f288f12b8b4582854105aa4c3befc08e
  accessed_at: '2026-10-13T19:39:47.001540Z'
  support: unknown
  summary: 403 prevents current Wikidata mapping verification. NCBI identity verification
    does not recover these denied mappings.
  snapshot_sha256: 165da4d5af47d0a2008597750d184a3cef870aff9d0a5005b71d6bd17a75672e
- evidence_id: citation-selector
  kind: record_content
  reference: scripts/extract_mibig.py
  locator: primary_reference, lines189-220
  accessed_at: '2026-10-13T19:39:47.001564Z'
  support: supports
  summary: Generic selection prioritizes compound evidence, then compound bioactivity,
    then legacy entry references. The same single primary_reference/reference_basis
    pair becomes an inventory row.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: citation-emitter
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: mibig_evidence and mibig_cluster, lines660-727; producer caller
  accessed_at: '2026-10-13T19:39:47.001695Z'
  support: supports
  summary: Producer and locus use the same selected row reference with DATABASE_ASSERTION
    and a source-level note. This preserves type but can misroute claim-specific evidence.
  snapshot_sha256: 8d82d7633e0492e9fe16011f6e5af6f8024f573e80c8a24176b65e2941478b71
- evidence_id: ownership
  kind: record_content
  reference: docs/CURATION.md
  locator: Implemented structure, xref, strain and locus-evidence correction paths
  accessed_at: '2026-10-13T19:39:47.001979Z'
  support: supports
  summary: decisions.tsv is reserved/unconsumed. Existing REPLACE_WITH_CHEBI rejects
    occupied destination keys, so FPHR-to-existing-IGQX is not an automatic replacement.
    Xref and strain tables are narrow row-pinned mechanisms.
  snapshot_sha256: 245df036e09a00a2f92a5f78c70eadb210cef7d70046e8ee35377a9e636cd30b
- evidence_id: rules
  kind: record_content
  reference: docs/HARMONIZATION.md
  locator: Exact structure identity, source claims, occurrence/production and computed
    filing rules
  accessed_at: '2026-10-13T19:39:47.002117Z'
  support: supports
  summary: Database assertion remains a database assertion. Locus and producer evidence
    grades are independent; neither taxonomy nor computed classification establishes
    origin.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: local-search
  kind: search
  reference: /private/tmp/npmech-vibrioferrin-resume-42VRr6/local-search.log
  locator: Ignored/hidden-inclusive bounded rg search
  accessed_at: '2026-10-13T19:39:47.002256Z'
  support: supports
  summary: Matches are source rows, exact owners, derived queues and historical coverage
    archives. No matching implemented correction row or earlier canonical assessment
    found within this search.
  snapshot_sha256: 9cccc27fea367694d52a91370b9605c091d95d4a2dee9d2604447309964fcf11
  search_scope: curation data/raw data/natural_products data/causal_graphs reviews
    docs scripts src conf tests; vibrioferrin, both key prefixes, three BGCs, NPA024673,197680,84585,22146715.
    Hidden/ignored files included; compressed archives not claimed text-exhaustive.
- evidence_id: capture
  kind: validation
  reference: /private/tmp/npmech-vibrioferrin-resume-42VRr6/capture.json
  locator: All3115owners,243components,38prior immutable pairs and current inspection
    hashes
  accessed_at: '2026-10-13T19:39:47.002356Z'
  support: supports
  summary: Full checkpoint reverified. Only prior-context change is three unrelated
    myxochromide strain rows; no vibrioferrin input/owner changed. Science remains
    uncurated.
  snapshot_sha256: cb84df12c1097c075619c55ac1e0a8d3be2de088a05f3336e2f5ecac98386db4
- evidence_id: native-gates
  kind: validation
  reference: /private/tmp/npmech-myxochromide-publish-MyX4Nq/qc.log
  locator: Prior executed full native QC; receipt and current hash attestation
  accessed_at: '2026-10-13T19:39:47.002472Z'
  support: supports
  summary: 758tests passed,3skipped; all3115strict/reproduction and native gates passed.
    Later merge-group CI at the current base passed; fresh local target/corpus/label/review
    checks are separate from this prior run.
  snapshot_sha256: 65b3d5000a0b19a843eb64aedd3e2716a3b2db5fea35ad59cfb85b317711b210
- evidence_id: mibig-BGC0000946.5
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000946.5/annotations.json
  locator: Exact accession/version/status, compounds[0], taxonomy,loci,classes and
    legacy_references; captured 2026-10-13T18:33:26.958447Z..2026-10-13T18:33:27.497463Z;
    HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/BGC0000946.5.json;
    receipt SHA256 c6f0fb85cfc805d53848fbc09eb6d66084853c63d4b20935b087174d44c0e0e8
  accessed_at: '2026-10-13T19:39:47.003651Z'
  support: supports
  summary: Active versioned source matches the imported graph/taxon/accession. Locus
    evidence methods are empty, correctly imported as SOURCE_ASSERTION/CLUSTER_UNSTATED;
    quality and review placeholders are not truth signals. No claim of latest version.
  snapshot_sha256: 3da6f0e539ba8f1582f84d6efc6e5deb1db81c35abbf01276f62db4bafc47073
- evidence_id: mibig-BGC0002527.2
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002527.2/annotations.json
  locator: Exact accession/version/status, compounds[0], taxonomy,loci,classes and
    legacy_references; captured 2026-10-13T18:33:27.611612Z..2026-10-13T18:33:28.223442Z;
    HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/BGC0002527.2.json;
    receipt SHA256 b49582e3f48e34e9c117758e05143fdadb777215648bcf2836d61a83101f753b
  accessed_at: '2026-10-13T19:39:47.004683Z'
  support: supports
  summary: Active versioned source matches the imported graph/taxon/accession. Locus
    evidence methods are empty, correctly imported as SOURCE_ASSERTION/CLUSTER_UNSTATED;
    quality and review placeholders are not truth signals. No claim of latest version.
  snapshot_sha256: a2e65114d495800febb990ea92cf8f6c4dbd5126d85e817e12f48a0a5cf59494
- evidence_id: npatlas-access
  kind: authority
  reference: https://www.npatlas.org/api/v1/compound/NPA024673?include=classifications
  locator: Official API denial payload; captured 2026-10-13T18:33:29.646890Z..2026-10-13T18:33:29.820673Z;
    HTTP403; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/NPA024673.json;
    receipt SHA256 1a32a5494e5b908c8e1c8ad127a3b8283a900a44d84f614ff92410a6ac4d8efc
  accessed_at: '2026-10-13T19:39:47.005743Z'
  support: unknown
  summary: HTTP403; exact equivalence unresolved, not evidence that the identifier
    is absent or wrong.
  snapshot_sha256: 2938e9f1284180959e33ab1718d0793a72ff6e4cdb8108c34dcd14e69446de5c
assessments:
- assessment_id: identity
  area: identity
  topic: Exact owner, chemical form and source grouping
  outcome: supported
  summary: The neutral ChEBI84585 graph, definition and two MIBiG compound structures
    agree. The2011 structural figures support its connectivity and epimeric resolution.
    ChEBI84630 is a distinct trianion, not an equivalent neutral form. Source-strain
    attribution remains separately limited.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - chemistry
  - chebi
  - primary2011
  - metadata
  - inventories
- assessment_id: structure
  area: consistency
  topic: Encoded chemistry and stereochemical resolution
  outcome: supported
  summary: SMILES, Standard InChI/key and stereo_complete:false roundtrip exactly.
    Calculated formula/mass are diagnostics, not measurements. Unspecified aminal
    configuration in IGQX accords with equilibrating epimers; no invented stereo completion.
    Representation consistency does not rescue the FPHR biological identity.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - chemistry
  - primary2011
  - metadata
- assessment_id: equivalence
  area: grounding
  topic: Minted/ChEBI grounding and xrefs
  outcome: concern
  summary: EXACT ChEBI84585 grounding is supported; PubChem197680 fails equivalence
    (F1), while NPA024673 remains unknown after403. No parent, congener or cross-corpus
    links are asserted.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - inventories
  - pubchem
  - chebi
  - chemistry
  - npatlas-access
- assessment_id: facets
  area: representation
  topic: Filing, BGC class, organism taxonomy and origin
  outcome: supported
  summary: Pinned NPClassifier singleton Amino acids and Peptides correctly files
    AMINO_ACIDS_AND_PEPTIDES with its version; empty finer classes and nonglycoside
    flag match the inventory. OTHER is a separate MIBiG BGC assertion; OTHER_BACTERIAL
    is a taxonomic grouping, not chemical class. No facet is evidence for another.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - inventories
  - taxonomy
  - rules
  - mibig-BGC0000946.5
  - mibig-BGC0002527.2
  dimensions:
  - name: classification_model
    value: npclassifier.gnps2.org@2026-09-07
    definition: Pinned computational filing, not origin evidence
    evidence_ids:
    - owner
    - inventories
  - name: producer_taxonomy
    value: 'Vibrio parahaemolyticus: species670; Azotobacter vinelandii CA: strain1283330'
    definition: Taxon facet with explicit rank; not proof of production
    evidence_ids:
    - taxonomy
- assessment_id: origin
  area: evidence
  topic: Natural origin versus heterologous expression
  outcome: supported
  summary: Natural vibrioferrin provenance is consistent with the inspected isolation/biosynthesis
    abstracts and source assertions. The2011 heterologous expression makes a known
    natural molecule and does not by itself make this chemical structure ENGINEERED.
    Full exact-strain claims remain partial.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - metadata
  - primary2011
  - mibig-BGC0000946.5
  - mibig-BGC0002527.2
- assessment_id: producers
  area: scope
  topic: Producer taxon, strain and evidence grade
  outcome: concern
  summary: NCBI labels/ranks match; CA is explicitly strain-scoped. WP1 is missing
    from the0946 producer (F4); AQ3354 belongs to another occurrence. SOURCE_ASSERTION
    is faithful; native knockout and CA genotype/metabolite evidence need full-text
    and claim-specific review before grade changes.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - sequences
  - sequence-ca
  - taxonomy
  - metadata
  - primary2007
  - mibig-BGC0000946.5
  - mibig-BGC0002527.2
- assessment_id: bgcs
  area: provenance
  topic: Active versions, locus boundaries and link evidence
  outcome: concern
  summary: 0946v5 and2527v2 are active; AB082123.1 and CP005094.1/876779..886792 match
    the source.0946 zero bounds stay unstated. Empty methods accurately give CLUSTER_UNSTATED.
    F2 concerns citation routing, not proof that the CA locus is experimentally demonstrated.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - inventories
  - sequences
  - sequence-ca
  - mibig-BGC0000946.5
  - mibig-BGC0002527.2
- assessment_id: occurrences
  area: evidence
  topic: Every occurrence and nearest cited source
  outcome: concern
  summary: All five rows reproduce.2016 abstract supports Azotobacter detection;1994
    supports V.parahaemolyticus named-product identity;2003 abstract supports native
    biosynthesis context.1992 DOI resolves but AQ3354 is source-asserted only.2011
    alginolyticus origin is indirect background (F3), not that study's detection experiment.
    Overlap notes correctly do not claim independent corroboration.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - inventories
  - metadata
  - primary2011
  - doi1992
  - chebi
  - wikidata-access
- assessment_id: evidence
  area: evidence
  topic: Reference identity and claim-level placement
  outcome: concern
  summary: References remain typed database assertions. The claim-level objects are
    present, but the generic bioactivity-first selector misroutes2527 evidence (F2);
    ChEBI2011 origin needs an indirect-provenance qualification (F3). Raw DOI whitespace
    is retained source provenance, not treated as a failed resolution.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - metadata
  - doi1992
  - citation-selector
  - citation-emitter
- assessment_id: optional
  area: completeness
  topic: Assays, targets, quantities, clinical and sibling claims
  outcome: not_applicable
  summary: No bioactivities, bioactivity_summary, molecular_targets, clinical status,
    datasets, parents/congeners or related_records are asserted. The PubChem inventory
    row is explicitly no assay data, not an experiment. Optional empty slots are not
    defects or global evidence-absence claims.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - resolved
  - inventories
  - local-search
- assessment_id: mechanism
  area: graph
  topic: Complete native mechanism and component ownership
  outcome: not_applicable
  summary: No biosynthetic_pathway, inline causal_graphs or causal_graph_refs on this
    owner. Complete native reader and243-component inventory agree. The2011 pathway
    figure is hypothetical and must not be imported as experimentally demonstrated
    edges. The whole-corpus graph objective remains active elsewhere.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - resolved
  - capture
  - primary2011
- assessment_id: audit
  area: provenance
  topic: Discussions, status, history and maintained fix ownership
  outcome: supported
  summary: Three seed events and the OPEN two-BGC shared-structure discussion are
    preserved. That discussion does not resolve the new xref/citation findings. Status
    stays SEEDED.
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - ownership
  - capture
  - native-gates
findings:
- finding_id: F1
  issue_key: chebi84585-nonexact-pubchem197680
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: PubChem197680 is not an exact chemical cross-reference
  description: The official PubChem response encodes FPHRKFJYHKRDFJ-LWYCVJHGSA-N,
    whereas this owner and ChEBI84585 encode IGQXNKDXMPSELX-BIAKFKOBSA-N. RDKit and
    visual comparison confirm four free acids/no ester versus three free acids/one
    ester. Equal formula and exact mass do not establish equivalence. The incorrect
    xref originates in BGC0000946:1; BGC0002527:1 contributes a separate NPAtlas identifier
    whose equivalence remains unknown after403. Withhold only the proven nonexact
    PubChem assertion, not the NPAtlas identifier.
  target_ids:
  - CHEBI:84585
  field_paths:
  - xrefs[0]
  evidence_ids:
  - owner
  - chemistry
  - pubchem
  - chebi
  - inventories
  - mibig-BGC0000946.5
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Implemented literal xref exclusion with complete source-row pin
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Guarded xref exclusion loader
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Versioned source compound, taxon and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and citation-level selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Grouping and claim-specific evidence emission
  rule_id: review-checklist:Equivalence; docs/CURATION.md:MIBiG chemical xref exclusions
  native_severity: major
  normalization_reason: False external equivalence is material, while this owner retains
    internally consistent ChEBI-grounded identity.
- finding_id: F2
  issue_key: mibig-BGC0002527-bioactivity-reference-used-for-locus
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: A compound-bioactivity citation displaces the entry-specific taxon/locus
    reference
  description: BGC0002527.2 attaches DOI10.1021/ic9016883 to siderophore bioactivity
    and retains PMID26452553 at entry level. The extractor chooses the former through
    its generic priority rule, and mibig_evidence reuses it for both the CA producer
    and CP005094.1 locus. The inspected2009 abstract concerns iron binding/photochemistry
    and marine bacteria; the2016 abstract explicitly concerns Azotobacter vibrioferrin
    and genome-based capacity. This confirms cross-claim citation selection, not a
    claim to have read either full paper or proved their every negative. Preserve
    the original database assertion and route claim-appropriate references separately.
    Full2016 evidence is still needed before assigning experimental grades or asserting
    those coordinates were tested.
  target_ids:
  - CHEBI:84585
  field_paths:
  - producer_organisms[1].evidence
  - biosynthetic_gene_clusters[1].evidence
  evidence_ids:
  - owner
  - mibig-BGC0002527.2
  - metadata
  - inventories
  - citation-selector
  - citation-emitter
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Versioned source compound, taxon and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and citation-level selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Grouping and claim-specific evidence emission
  rule_id: review-checklist:Evidence standard/Producer organisms/Gene clusters; nearest
    source must support the same claim
  native_severity: major
  normalization_reason: Confirmed source-transform mismatch affects material taxon/locus
    attribution. The record discloses the bioactivity level and correctly remains
    DATABASE_ASSERTION, but disclosure does not supply the missing claim-specific
    reference.
- finding_id: F3
  issue_key: chebi84585-alginolyticus-indirect-origin-citation
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The ChEBI alginolyticus origin citation is indirect, not that study's detection
    experiment
  description: The full PMID22146715 paper does mention V.alginolyticus and V.parahaemolyticus
    as previously known sources. Its experiment, however, produces structurally characterized
    vibrioferrin in E.coli from sediment clone MG93-1; the donor taxon is not established
    by the protein homology comparisons. ChEBI84585 repeats the alginolyticus origin/PMID
    pair, so the import is faithful. Treat this as indirect prior-literature support
    and trace the actual isolation/biosynthesis source. Do not infer that alginolyticus
    cannot produce vibrioferrin, delete the occurrence merely because the paper is
    indirect, or turn the metagenomic clone into an identified native producer.
  target_ids:
  - CHEBI:84585
  field_paths:
  - occurrences[1].evidence
  evidence_ids:
  - owner
  - chebi
  - inventories
  - primary2011
  - primary2007
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Source origin assertions, not editable without maintained provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Occurrence evidence emission; a new correction path needs implementation
      and tests
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
    role: Only curator-owned cited qualification through validated writer/event; never
      hand-edit seeded fields
  rule_id: review-checklist:Occurrences and narrowest claim evidence; preserve database
    assertion versus experiment
  native_severity: minor
  normalization_reason: The named organism is explicitly discussed by the source and
    the record says DATABASE_ASSERTION. The defect is weak/indirect detection provenance,
    not a confirmed false biological occurrence.
- finding_id: F4
  issue_key: mibig-BGC0000946-vibrioferrin-source-strain
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The deposited WP1 strain is missing from the producer claim
  description: AB082123.1 names V.parahaemolyticus strain WP1, but the corresponding
    BGC0000946 producer has only species-rank NCBITaxon670. The AQ3354 detection_context
    in a different ChEBI occurrence is not this accession's strain and must not be
    copied across. CA is already represented by strain-rank NCBITaxon1283330 and needs
    no inferred taxon replacement.
  target_ids:
  - CHEBI:84585
  field_paths:
  - producer_organisms[0].strain
  evidence_ids:
  - owner
  - sequences
  - taxonomy
  - ownership
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented complete-source-row-pinned strain qualifier
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Guarded strain qualification loader
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Versioned source compound, taxon and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and citation-level selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Grouping and claim-specific evidence emission
  rule_id: review-checklist:Producer organisms; docs/CURATION.md:MIBiG producer strain
    context
  native_severity: minor
  normalization_reason: A bounded source-strain omission with exact accession traceability
    retained.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:84585
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Implemented literal xref exclusion with complete source-row pin
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Guarded xref exclusion loader
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Versioned source compound, taxon and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and citation-level selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Grouping and claim-specific evidence emission
  description: Withhold literal pubchem:197680 from BGC0000946:1 with complete-row
    digest2a6d88d4055ff04c4496c977d1bc1af425c5f12c860c7c85a591c681734cfe7c. Cite the
    official PubChem response and preserve the rejected assertion in the table-owned
    discussion. Do not select a replacement CID or exclude NPAtlas based on failed
    access.
  acceptance_checks:
  - Reject stale/duplicate pins and xref reintroduction.
  - ChEBI identity, NPAtlas assertion and other owner claims unchanged.
  - Use maintained input/transform with regression tests; do not patch generated scientific
    fields.
  - 'For authorized curation: validated writer and append-only event, seeder dry run/canary,
    exact diff, strict validation, verify-corpus, verify-reproduction and full qc.'
  - Retain raw source assertions, taxon IDs, source versions and independent producer/locus
    evidence grades.
  generator: scripts/seed_from_sources.py
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - CHEBI:84585
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Versioned source compound, taxon and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and citation-level selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Grouping and claim-specific evidence emission
  description: Separate citation selection for compound structure/activity from producer/locus
    assertions. Preserve2527 bioactivity DOI in its correct source context, retain
    entry PMID26452553 for its appropriate claim, and inspect the full primary work
    before upgrading grades. Any extractor/schema change must account for other affected
    rows rather than silently reassigning the whole corpus.
  acceptance_checks:
  - Regression fixture has differing compound-bioactivity and entry references and
    verifies claim-specific routing.
  - Pin current2527:1 complete-row digest3be82cba240a164478055eac8f68fd1cceac0f615451f6b31133d121b58a73a1
    for a bounded correction.
  - Source citation provenance remains DATABASE_ASSERTION unless primary curation
    is separately justified.
  - Use maintained input/transform with regression tests; do not patch generated scientific
    fields.
  - 'For authorized curation: validated writer and append-only event, seeder dry run/canary,
    exact diff, strict validation, verify-corpus, verify-reproduction and full qc.'
  - Retain raw source assertions, taxon IDs, source versions and independent producer/locus
    evidence grades.
  generator: scripts/extract_mibig.py and scripts/seed_from_sources.py after implemented
    correction
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - CHEBI:84585
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Source origin assertions, not editable without maintained provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Occurrence evidence emission; a new correction path needs implementation
      and tests
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
    role: Only curator-owned cited qualification through validated writer/event; never
      hand-edit seeded fields
  description: Qualify the ChEBI2011 alginolyticus occurrence as indirect literature
    context; trace the actual native detection/production source. Preserve the upstream
    origin pair and do not replace its taxon with E.coli or infer a metagenomic donor.
    A generated-row correction requires an implemented tested path; reserved decisions.tsv
    has no effect.
  acceptance_checks:
  - Distinguish background organism mention, sequence homology, experimental host
    and natural producer.
  - Any retained direct detection citation supports the exact product and taxon.
  - Do not delete a biologically plausible occurrence merely because its current source
    is indirect.
  - Use maintained input/transform with regression tests; do not patch generated scientific
    fields.
  - 'For authorized curation: validated writer and append-only event, seeder dry run/canary,
    exact diff, strict validation, verify-corpus, verify-reproduction and full qc.'
  - Retain raw source assertions, taxon IDs, source versions and independent producer/locus
    evidence grades.
- action_id: A4
  finding_ids:
  - F4
  target_ids:
  - CHEBI:84585
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented complete-source-row-pinned strain qualifier
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Guarded strain qualification loader
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Versioned source compound, taxon and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and citation-level selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Grouping and claim-specific evidence emission
  description: Add WP1 to the0946 producer through the existing row-pinned strain
    table, citing AB082123.1 and the0946:1 digest2a6d88d4055ff04c4496c977d1bc1af425c5f12c860c7c85a591c681734cfe7c.
    Leave AQ3354 occurrence context and CA strain-rank taxon unchanged.
  acceptance_checks:
  - Only the correct0946 producer gains WP1 and separate qualifier evidence.
  - No invented strain taxid or experimental grade upgrade.
  - Use maintained input/transform with regression tests; do not patch generated scientific
    fields.
  - 'For authorized curation: validated writer and append-only event, seeder dry run/canary,
    exact diff, strict validation, verify-corpus, verify-reproduction and full qc.'
  - Retain raw source assertions, taxon IDs, source versions and independent producer/locus
    evidence grades.
  generator: scripts/seed_from_sources.py
limitations:
- Required full-text attribution remains incomplete:1992 PDF403,2003/2016 PMC challenges
  after XML500,2007 subscription preview,1994 abstract only;2013 regulatory and2011
  receptor sources read as abstracts only. No alternate retrieval after denial.
- Official Wikidata organism endpoints returned403. NCBI taxonomy verification does
  not validate those source mappings.
- Current calculations establish source graph consistency and differences, not experimental
  assignment in every source strain. The2011 pathway is hypothetical.
- Full native QC/reproduction is explicitly a verified prior run; current target strict,
  chemistry, corpus, label and later review-output checks are separate. Existing skips/warnings
  remain.
- Only new canonical review pairs are written to the repository; external payloads/receipts
  remain temporary, with stable source URLs and hashes recorded. No publisher PDF
  redistributed.
- No scientific record, source inventory, history, page or native status was changed.
  This does not complete the whole-corpus goal.
- NPA024673 exact equivalence remains unknown after403; no exclusion inferred from
  access failure.
notes:
- Base39811a084202d1c1a47472622e3008bed7000083 and43captured context/target inputs
  were verified against Git bytes.
- The old source scan omitted exact-ID ChEBI origins; this review uses the corrected
  complete structured join.
- The local checklist mentions decisions.tsv, but the current profile/CURATION implementation
  explicitly says it is reserved and unconsumed.
- Both records have three history events, not two; the source strain WP1 must not
  be confused with AQ3354.
tags:
- record-review
- vibrioferrin
- partial
- read-only
```
