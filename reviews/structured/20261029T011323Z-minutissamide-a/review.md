# Scientific review of minutissamide A

- Review: 20261029T011323Z-minutissamide-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-29T01:00:53.898722Z
- Finished UTC: 2026-10-29T01:13:23.385770Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Minutissamide A retains internally reproducible normalized InChI/key diagnostics, with the saved canonical representation differences and stereochemical limits preserved. MIBiG BGC0001952/version3 and BGC0001953/version4 both name minutissamide A; the exact-key CyanoMetDB row names Minutissamide C. Exact natural-congener correspondence remains unresolved. The 2011 isolation abstract and 2019 family biosynthesis abstract are own-identified, but the latter PMC response supplies no substantive body. Producer/locus grades remain SOURCE_ASSERTION and CLUSTER_UNSTATED; no activity or replacement is transferred. The six-DOI metadata result is accepted within its bibliographic scope and reconciled with the current official intake. The separate NP200236C occurrence citation raises a title-limited applicability question; no replacement or wrong-graph conclusion follows.

## Scope And Provenance

Read-only scientific review of this exact minutissamide owner, complete retained source rows, saved dual-encoding diagnostics and inspected isolation/biosynthesis abstracts and bibliographic metadata. Source-specific congener names, strain/locus assignments and assay applicability remain explicitly unresolved.

Selection: One current unreviewed record selected in canonical path order; official batch89 selection and intake exactly reconcile the frozen owner and source evidence.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-9fd577c5ae | data/natural_products/amino_acids_and_peptides/minutissamide-a.yaml | generated | minutissamide A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-9fd577c5ae | Fresh corpus gate passed:3116 PATHS.tsv rows and3116 files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-9fd577c5ae | Fresh reproduction gate passed:all3116 records are byte-identical to seeding from maintained inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-9fd577c5ae | Fresh deterministic review queue produced8922 rows across12 queues; this is not scientific review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-9fd577c5ae | Fresh configured identifier-label gate passed:13472 canonical,657 synonym and35 exception matches;499 nonblocking mismatches and4898 no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-9fd577c5ae | Fresh full quality gate passed:1024 tests passed,4 skipped,2 dependency warnings;3116 closed-schema records have zero errors; site freshness, reproduction and lockfile checks passed, alongside22 governed artifacts and15 raw inventories. |
| Native strict target validation | passed | True | naturalproductmech:mibig-9fd577c5ae | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Saved structure representations and stereochemical resolution | passed | True | naturalproductmech:mibig-9fd577c5ae | Saved SMILES and InChI parses agree on formula C55H89N13O16, Standard InChI and key HZHLPFLQTJCCHS-HFAMINCGSA-N. The SMILES parse has 11 specified tetrahedral sites and two specified double-bond sites, with zero unspecified SMILES sites; stereo_complete=true. Both saved representations have a 31-member C21N10 ring and a five-member C4N ring. Both canonical-SMILES comparisons and the complete atom correspondence are false. InChI adds 11 unspecified C(O)=N representation sites; these are separate from the retained tetrahedral-resolution flag and do not prove missing natural stereochemistry. These saved diagnostic results do not identify the natural congener. |
| Source-specific congener names and exact full-key correspondence | unavailable | True | naturalproductmech:mibig-9fd577c5ae | Which source-specific A/B/C/D structure and supported stereochemical resolution corresponds to full key HZHLPFLQTJCCHS-HFAMINCGSA-N? MIBiG BGC0001952/version3 and BGC0001953/version4 both name minutissamide A; the exact-key CyanoMetDB row names Minutissamide C. The inspected abstracts do not supply a full graph-to-label map. Preserve these literal discrepancies and the existing shared-structure discussion; neither a correct replacement name nor a chemically wrong record is established here. |
| Producer assertions versus source strain scope | unavailable | True | naturalproductmech:mibig-9fd577c5ae | The two retained MIBiG producer claims name Anabaena minutissima UTEX B1613 and Anabaena sp. UHCC-0399. PMID21699148 reports isolation of its A–D compounds from cultured UTEX1613; PMID30504214 names UTEX B1613 specifically in the putative D chlorination explanation. Neither inspected abstract resolves each retained full key to both producer strains, validates taxon IDs or equates the strain literals. Preserve SOURCE_ASSERTION and distinguish isolation/occurrence from compound-specific biosynthesis. |
| Occurrence citations and exact-congener applicability | unavailable | True | naturalproductmech:mibig-9fd577c5ae | LOTUS and CyanoMetDB occurrences remain database assertions for Anabaena minutissima. Own PMID21699148/DOI10.1021/np2002226 identifies the A–D isolation work, but exact full-key correspondence remains unresolved because the retained source labels differ. The second exact-key LOTUS row and owner occurrence use literal DOI10.1021/NP200236C. Its own Crossref title instead names ethyl tumonoate A from cf. Oscillatoria margaritifera, which creates a bounded citation-applicability concern for this retained occurrence. The metadata lacks an abstract and article body; the title does not prove the unread article excludes minutissamides, establish a wrong isomer or justify replacing the citation. UTEX1613 occurrence must not be promoted to either retained producer solely from isolation. |
| Family biosynthesis versus exact locus and congener experiments | unavailable | True | naturalproductmech:mibig-9fd577c5ae | The retained active BGC0001952/version3 and BGC0001953/version4 rows report questionable quality, unknown completeness and no locus-method entries, with MH325199.1 and MH325200.1. The locus grade remains CLUSTER_UNSTATED. The 2019 abstract supplies PUW/MIN family context and a putative D halogenase explanation, not an independently checked experiment assigning these exact retained structures to both loci. Neither database quality labels nor abstract language certify a current version, precise locus, enzyme identity or causal edge. |
| Paper compound assays and nontransfer to unresolved owner | unavailable | True | naturalproductmech:mibig-9fd577c5ae | The 2011 abstract reports ordered HT29 IC50 results for its four A–D/1–4 compounds; no value is transferred to this record without an exact structure-to-compound map. The 2019 major-variant antibacterial statement and PUW F yeast activity are not this owner’s assay. Local bioactivity/target fields and assay/target rows are empty; emptiness is neither a biological negative result nor an automatic major defect. |
| Mechanism fields and causal specificity | unavailable | True | naturalproductmech:mibig-9fd577c5ae | No inline graph, referenced component, biosynthetic pathway or molecular target is retained in this owner. The inspected family-level starter-module and putative chlorination statements do not justify fabricating exact-owner enzyme steps, a complex, substrate edges or direct targets. Completing a graph is separate from resolving the congener correspondence. |
| Computed filing versus asserted classification | passed | True | naturalproductmech:mibig-9fd577c5ae | The current path is amino_acids_and_peptides and np_pathway is AMINO_ACIDS_AND_PEPTIDES. The exact-key NPClassifier row, model npclassifier.gnps2.org@2026-09-07, reports Amino acids and Peptides / Oligopeptides / Cyclic peptides and is_glycoside=false. The retained MIBiG bgc_class NRPS is a separate source assertion. The computed filing is preserved and does not establish biological origin or resolve the A/B/C/D label conflict. |
| Source versions, evidence placement and current conditional context | passed | True | naturalproductmech:mibig-9fd577c5ae | The retained MIBiG versions3/4 and entry-level PMID30504214 are distinct from the CyanoMetDB PMID21699148 and LOTUS DOI citations. Two seed events and the open shared-structure discussion remain. The 37 current official source inputs use the regular AGENTS.md context and agree with the captured owner and raw rows. Original machine/retrieval clocks are retained separately from later source interpretation. |
| Minted record identity and unverified authority equivalence | unavailable | True | naturalproductmech:mibig-9fd577c5ae | The owner retains minted identifier naturalproductmech:mibig-9fd577c5ae with a content-hash rationale and PubChem cross-reference pubchem:53467644. Its exact joined ChEBI sets are empty. These local facts do not freshly verify the PubChem structure, a live ChEBI absence claim or every taxon authority. The pending label question does not justify an invented replacement identifier. |
| Inspected source extent and completed metadata boundary | unavailable | True | naturalproductmech:mibig-9fd577c5ae | Own PubMed fields and the complete returned PMC frontmatter/abstracts were inspected; original retrieval clocks remain separate from later scientific reading. The full PMC6365827 XML route is held because substantive body/back were not returned. PMC3142320 was unattempted at the accepted failed-canary boundary. No figure pixels, supplementary files, spectra or full structural depictions were inspected. The six-DOI metadata group is complete and accepted within its bibliographic scope after independent response review; the current official intake is reconciled. Own NP200236C metadata adds only a title-limited occurrence-citation question, not full article coverage. |

## Scientific And Domain Assessments

### Saved structure representations and stereochemical resolution

consistency: supported. Targets: naturalproductmech:mibig-9fd577c5ae.

Saved SMILES and InChI parses agree on formula C55H89N13O16, Standard InChI and key HZHLPFLQTJCCHS-HFAMINCGSA-N. The SMILES parse has 11 specified tetrahedral sites and two specified double-bond sites, with zero unspecified SMILES sites; stereo_complete=true. Both saved representations have a 31-member C21N10 ring and a five-member C4N ring. Both canonical-SMILES comparisons and the complete atom correspondence are false. InChI adds 11 unspecified C(O)=N representation sites; these are separate from the retained tetrahedral-resolution flag and do not prove missing natural stereochemistry. These saved diagnostic results do not identify the natural congener.

### Source-specific congener names and exact full-key correspondence

identity: unknown. Targets: naturalproductmech:mibig-9fd577c5ae.

Which source-specific A/B/C/D structure and supported stereochemical resolution corresponds to full key HZHLPFLQTJCCHS-HFAMINCGSA-N? MIBiG BGC0001952/version3 and BGC0001953/version4 both name minutissamide A; the exact-key CyanoMetDB row names Minutissamide C. The inspected abstracts do not supply a full graph-to-label map. Preserve these literal discrepancies and the existing shared-structure discussion; neither a correct replacement name nor a chemically wrong record is established here.

### Producer assertions versus source strain scope

provenance: unknown. Targets: naturalproductmech:mibig-9fd577c5ae.

The two retained MIBiG producer claims name Anabaena minutissima UTEX B1613 and Anabaena sp. UHCC-0399. PMID21699148 reports isolation of its A–D compounds from cultured UTEX1613; PMID30504214 names UTEX B1613 specifically in the putative D chlorination explanation. Neither inspected abstract resolves each retained full key to both producer strains, validates taxon IDs or equates the strain literals. Preserve SOURCE_ASSERTION and distinguish isolation/occurrence from compound-specific biosynthesis.

### Occurrence citations and exact-congener applicability

evidence: unknown. Targets: naturalproductmech:mibig-9fd577c5ae.

LOTUS and CyanoMetDB occurrences remain database assertions for Anabaena minutissima. Own PMID21699148/DOI10.1021/np2002226 identifies the A–D isolation work, but exact full-key correspondence remains unresolved because the retained source labels differ. The second exact-key LOTUS row and owner occurrence use literal DOI10.1021/NP200236C. Its own Crossref title instead names ethyl tumonoate A from cf. Oscillatoria margaritifera, which creates a bounded citation-applicability concern for this retained occurrence. The metadata lacks an abstract and article body; the title does not prove the unread article excludes minutissamides, establish a wrong isomer or justify replacing the citation. UTEX1613 occurrence must not be promoted to either retained producer solely from isolation.

### Family biosynthesis versus exact locus and congener experiments

evidence: unknown. Targets: naturalproductmech:mibig-9fd577c5ae.

The retained active BGC0001952/version3 and BGC0001953/version4 rows report questionable quality, unknown completeness and no locus-method entries, with MH325199.1 and MH325200.1. The locus grade remains CLUSTER_UNSTATED. The 2019 abstract supplies PUW/MIN family context and a putative D halogenase explanation, not an independently checked experiment assigning these exact retained structures to both loci. Neither database quality labels nor abstract language certify a current version, precise locus, enzyme identity or causal edge.

### Paper compound assays and nontransfer to unresolved owner

evidence: unknown. Targets: naturalproductmech:mibig-9fd577c5ae.

The 2011 abstract reports ordered HT29 IC50 results for its four A–D/1–4 compounds; no value is transferred to this record without an exact structure-to-compound map. The 2019 major-variant antibacterial statement and PUW F yeast activity are not this owner’s assay. Local bioactivity/target fields and assay/target rows are empty; emptiness is neither a biological negative result nor an automatic major defect.

### Mechanism fields and causal specificity

completeness: unknown. Targets: naturalproductmech:mibig-9fd577c5ae.

No inline graph, referenced component, biosynthetic pathway or molecular target is retained in this owner. The inspected family-level starter-module and putative chlorination statements do not justify fabricating exact-owner enzyme steps, a complex, substrate edges or direct targets. Completing a graph is separate from resolving the congener correspondence.

### Computed filing versus asserted classification

representation: supported. Targets: naturalproductmech:mibig-9fd577c5ae.

The current path is amino_acids_and_peptides and np_pathway is AMINO_ACIDS_AND_PEPTIDES. The exact-key NPClassifier row, model npclassifier.gnps2.org@2026-09-07, reports Amino acids and Peptides / Oligopeptides / Cyclic peptides and is_glycoside=false. The retained MIBiG bgc_class NRPS is a separate source assertion. The computed filing is preserved and does not establish biological origin or resolve the A/B/C/D label conflict.

### Source versions, evidence placement and current conditional context

provenance: supported. Targets: naturalproductmech:mibig-9fd577c5ae.

The retained MIBiG versions3/4 and entry-level PMID30504214 are distinct from the CyanoMetDB PMID21699148 and LOTUS DOI citations. Two seed events and the open shared-structure discussion remain. The 37 current official source inputs use the regular AGENTS.md context and agree with the captured owner and raw rows. Original machine/retrieval clocks are retained separately from later source interpretation.

### Minted record identity and unverified authority equivalence

grounding: unknown. Targets: naturalproductmech:mibig-9fd577c5ae.

The owner retains minted identifier naturalproductmech:mibig-9fd577c5ae with a content-hash rationale and PubChem cross-reference pubchem:53467644. Its exact joined ChEBI sets are empty. These local facts do not freshly verify the PubChem structure, a live ChEBI absence claim or every taxon authority. The pending label question does not justify an invented replacement identifier.

### Inspected source extent and completed metadata boundary

scope: unknown. Targets: naturalproductmech:mibig-9fd577c5ae.

Own PubMed fields and the complete returned PMC frontmatter/abstracts were inspected; original retrieval clocks remain separate from later scientific reading. The full PMC6365827 XML route is held because substantive body/back were not returned. PMC3142320 was unattempted at the accepted failed-canary boundary. No figure pixels, supplementary files, spectra or full structural depictions were inspected. The six-DOI metadata group is complete and accepted within its bibliographic scope after independent response review; the current official intake is reconciled. Own NP200236C metadata adds only a title-limited occurrence-citation question, not full article coverage.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI887-LOCAL | /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/minutissamide-a.yaml; whole owner; chemical_structure; occurrences; producer_organisms; biosynthetic_gene_clusters; source_concepts; discussions; curation_history | context_only | The whole owner is labeled minutissamide A, key HZHLPFLQTJCCHS-HFAMINCGSA-N, NATURAL_PRODUCT and SEEDED. It retains two MIBiG producer/BGC assertions, SOURCE_ASSERTION and CLUSTER_UNSTATED, two seed-history entries, and an open shared-structure discussion. The owner contains no bioactivities, molecular targets, biosynthetic pathway, inline causal graph or referenced component; these are local-field observations only. |
| SCI887-ROWS | /private/tmp/npm-review-work/shared-next-batch089-tentative/bgc-tentative89-owner-source-reconnaissance-DATA-001.json; /records/6/retained_rows; /records/6/supplemental_rows; /records/6/row_guards | context_only | MIBiG BGC0001952/version3 and BGC0001953/version4 both name minutissamide A; the exact-key CyanoMetDB row names Minutissamide C. The exact-key joins contain two MIBiG, 2 LOTUS, one NPClassifier and one CyanoMetDB row. Both ChEBI sets and all PubChem BioAssay/BindingDB/AntibioticMech joins are empty. The raw producer/BGC reference is literal PMID:30504214 at ENTRY scope; the CyanoMetDB isolation citation is literal PMID:21699148. These are retained database rows, not verified structure assignments. |
| SCI887-ENCODINGS | /private/tmp/npm-review-work/shared-next-batch089-tentative/source-science-preparation/native-tentative89-ten-owner-dual-encoding-results-001.json; /records/6/smiles; /records/6/inchi; /records/6/stereo_counts; /records/6/comparisons; /records/6/atom_correspondence | supports | Saved SMILES and InChI parses agree on formula C55H89N13O16, Standard InChI and key HZHLPFLQTJCCHS-HFAMINCGSA-N. The SMILES parse has 11 specified tetrahedral sites and two specified double-bond sites, with zero unspecified SMILES sites; stereo_complete=true. Both saved representations have a 31-member C21N10 ring and a five-member C4N ring. Both canonical-SMILES comparisons and the complete atom correspondence are false. InChI adds 11 unspecified C(O)=N representation sites; these are separate from the retained tetrahedral-resolution flag and do not prove missing natural stereochemistry. These saved diagnostic results do not identify the natural congener. |
| SCI887-PUBMED2011 | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-three-unattempted-PubMed-001/pmid-21699148.xml; ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract; ./PubmedArticle/PubmedData/ArticleIdList | partial | Own PMID21699148 identifies the A–D isolation paper, DOI10.1021/np2002226 and PMC3142320. Its abstract reports four cyclic decapeptides from cultured Anabaena minutissima UTEX1613, planar and stereochemical characterization, and ordered A–D/1–4 HT29 antiproliferative results. The source describes four named paper compounds; it does not give a full InChIKey mapping in these inspected fields. |
| SCI887-PUBMED2019 | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-three-unattempted-PubMed-001/pmid-30504214.xml; ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract; ./PubmedArticle/PubmedData/ArticleIdList | partial | Own PMID30504214 identifies DOI10.1128/AEM.02675-18 and PMC6365827. Its abstract reports PUW/MIN clusters and variants from six strains, alternative starter modules, and a putative halogenase explanation for minutissamide D chlorination in UTEX B1613. The reported major-variant antibacterial limitation and PUW F yeast activity retain their stated scope. |
| SCI887-PMC-FRONT | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-primary-two-own-PMC-001/pmc6365827.xml; ./article/front/article-meta/article-id; ./article/front/article-meta/abstract[1]; ./article/front/article-meta/abstract[2] | partial | The complete returned PMC6365827 XML confirms the own article identifiers and supplies a precis plus the abstract/importance text. It retains the six-strain PUW/MIN framing, putative MIN D chlorination explanation and PUW F-specific yeast statement. The two abstract elements overlap; they are not independent experimental confirmations. |
| SCI887-SOURCE-HOLD | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/root-tentative89-PMC6365827-frontmatter-only-hold-observation-001.json; whole original execution/access/index/body joins; selectors; unattempted_identifiers | context_only | The one initial PMC6365827 XML route returned complete HTTP200 frontmatter with an explicit publisher restriction comment, zero article body and zero back. The collector held that route. PMC3142320 remained unattempted in this phase. A returned full-text restriction is not evidence that the article, figures or supplementary material do not exist. |
| SCI887-CONTEXT-PEER | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/review-support-tentative89-PMC6365827-actual-response-context-independent-peer-001.json; /owner_context; /literal_citation_placements; /scientific_claim_scope; /unattempted_boundary | context_only | The accepted bounded response/context peer preserves both whole minutissamide owners and exact raw rows, separates the source-specific name discrepancies from chemical identity, and retains the lack of a verified full-key mapping or congener-specific assay transfer. Its reading clock is later than the original retrieval clocks. |
| SCI887-PENDING-CITATIONS | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/native-tentative89-six-unresolved-DOI-cache-route-DATA-001.json; /lead_adjudications; /proposed_initial_Crossref_jobs; /resolved_DOI_exclusions | context_only | At its original recorded clock, this accepted route DATA excluded verified own metadata aliases and identified six unresolved DOI works for a separate metadata group. NP200236C was a distinct record887 occurrence-citation lead, not NP2002226. This preserved pre-request assessment is not the later retrieval or its applicability result. |
| SCI887-CROSSREF-NP200236C | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-six-unresolved-crossref-001/doi-04.json; /message/DOI; /message/title; /message/published-online; /message/published-print; /message/reference-count | context_only | Own Crossref DOI10.1021/np200236c has the title Phylogeny-Guided Isolation of Ethyl Tumonoate A from the Marine Cyanobacterium cf. Oscillatoria margaritifera, with 2011 publication dates. The returned metadata has no abstract or article body and contains 34 foreign reference entries. Publisher/PDF links are uninspected leads; title and references alone do not establish the complete contents of the article. |
| SCI887-CROSSREF-COMPLETION | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/root-tentative89-six-crossref-complete-reading-001.json; /records; /index; /all_complete_body_bytes_read; /all_own_DOIs_verified; /scientific_scope; /source_failures_added; /canonical_failures_added | context_only | ROOT reports complete own-DOI reads for all six selected Crossref metadata responses, no added source or canonical failures, and no article abstracts or bodies. ROOT distinguishes NP200236C from the minutissamides A–D DOI and limits its title to a citation-applicability question. This is a later reading receipt; original retrieval clocks are separately retained. |

## Limits And Additional Notes

- Which source-specific A/B/C/D structure and supported stereochemical resolution corresponds to full key HZHLPFLQTJCCHS-HFAMINCGSA-N? MIBiG BGC0001952/version3 and BGC0001953/version4 both name minutissamide A; the exact-key CyanoMetDB row names Minutissamide C. The inspected abstracts do not supply a full graph-to-label map. Preserve these literal discrepancies and the existing shared-structure discussion; neither a correct replacement name nor a chemically wrong record is established here.
- The two retained MIBiG producer claims name Anabaena minutissima UTEX B1613 and Anabaena sp. UHCC-0399. PMID21699148 reports isolation of its A–D compounds from cultured UTEX1613; PMID30504214 names UTEX B1613 specifically in the putative D chlorination explanation. Neither inspected abstract resolves each retained full key to both producer strains, validates taxon IDs or equates the strain literals. Preserve SOURCE_ASSERTION and distinguish isolation/occurrence from compound-specific biosynthesis.
- The retained active BGC0001952/version3 and BGC0001953/version4 rows report questionable quality, unknown completeness and no locus-method entries, with MH325199.1 and MH325200.1. The locus grade remains CLUSTER_UNSTATED. The 2019 abstract supplies PUW/MIN family context and a putative D halogenase explanation, not an independently checked experiment assigning these exact retained structures to both loci. Neither database quality labels nor abstract language certify a current version, precise locus, enzyme identity or causal edge.
- The 2011 abstract reports ordered HT29 IC50 results for its four A–D/1–4 compounds; no value is transferred to this record without an exact structure-to-compound map. The 2019 major-variant antibacterial statement and PUW F yeast activity are not this owner’s assay. Local bioactivity/target fields and assay/target rows are empty; emptiness is neither a biological negative result nor an automatic major defect.
- Own PubMed fields and the complete returned PMC frontmatter/abstracts were inspected; original retrieval clocks remain separate from later scientific reading. The full PMC6365827 XML route is held because substantive body/back were not returned. PMC3142320 was unattempted at the accepted failed-canary boundary. No figure pixels, supplementary files, spectra or full structural depictions were inspected. The six-DOI metadata group is complete and accepted within its bibliographic scope after independent response review; the current official intake is reconciled. Own NP200236C metadata adds only a title-limited occurrence-citation question, not full article coverage.
- The review does not establish a replacement name, graph or stereochemical assignment. The current owner is unchanged, and actual baseline, selection, intake and strict receipts are retained separately from the scientific evidence.
- Record887 retains a LOTUS occurrence for Anabaena minutissima under full key HZHLPFLQTJCCHS-HFAMINCGSA-N with literal DOI10.1021/NP200236C. Own Crossref metadata identifies that DOI as the 2011 ethyl tumonoate A / cf. Oscillatoria margaritifera paper, distinct from the own-verified minutissamides A–D work DOI10.1021/np2002226. This difference warrants checking the exact structure–organism–citation applicability. The response contains no abstract or article body; its title and 34 foreign reference entries cannot establish that the unread paper lacks minutissamide content, prove an incorrect chemical graph, or select a replacement citation.
- Source seeding retains five unresolved assay-organism targets (one distinct Human label),42 withheld nonspecific producer claims and161 merged-taxonomy rewrites.
- Queue diagnostics rank deterministic curation questions and do not prove literature support or review completion.
- 499 configured nonblocking mismatches remain warnings;4898 pairs lacked an adapter.35 exception and657 synonym matches retain their configured scope; no fresh ontology authority retrieval is asserted.
- Four tests were skipped; two dependency deprecations concern LinkML dataclass and Pandas copy-on-write behavior. Source seeding warnings and configured gate boundaries are retained in the full log.
- Native baseline gates establish configured consistency, not independent biological production, exact stereochemistry or primary-source adequacy.
- Configured ontology caches and scientific/test skips retain their original scope; a new command execution is not a fresh retrieval of every authority.
- All tracked link objects are hashed as link-target bytes without dereferencing; canonical record source intake remains regular-file-only and uses the separately reviewed AGENTS.md context projection.
- The whole local owner and retained source rows were read. Full-owner scientific verification remains false; scientific_review denotes the bounded scientific interpretation in this report.
- Original owner/source reading, two-encoding computation, primary-text reading, HTTP retrieval and later metadata reading retain separate clocks. Official intake separately computed SMILES facts.
- No scientific record, maintained input or native curation status was changed. Any findings and actions record ROOT-adopted proposed work; exact-source limitations and unavailable checks remain explicit.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
kind: record
repository: CultureBotAI/NaturalProductMech
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
review_id: 20261029T011323Z-minutissamide-a
title: Scientific review of minutissamide A
started_at: '2026-10-29T01:00:53.898722Z'
finished_at: '2026-10-29T01:13:23.385770Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Minutissamide A retains internally reproducible normalized InChI/key diagnostics,
  with the saved canonical representation differences and stereochemical limits preserved.
  MIBiG BGC0001952/version3 and BGC0001953/version4 both name minutissamide A; the
  exact-key CyanoMetDB row names Minutissamide C. Exact natural-congener correspondence
  remains unresolved. The 2011 isolation abstract and 2019 family biosynthesis abstract
  are own-identified, but the latter PMC response supplies no substantive body. Producer/locus
  grades remain SOURCE_ASSERTION and CLUSTER_UNSTATED; no activity or replacement
  is transferred. The six-DOI metadata result is accepted within its bibliographic
  scope and reconciled with the current official intake. The separate NP200236C occurrence
  citation raises a title-limited applicability question; no replacement or wrong-graph
  conclusion follows.
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
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/amino_acids_and_peptides/minutissamide-a.yaml
    sha256: a04d20aa1ea89955cf918438dd1075ffd82b3520bef55ba0bfda21ef261b11b5
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
targets:
- target_id: naturalproductmech:mibig-9fd577c5ae
  path: data/natural_products/amino_acids_and_peptides/minutissamide-a.yaml
  label: minutissamide A
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
    path: data/natural_products/amino_acids_and_peptides/minutissamide-a.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
scope:
  description: Read-only scientific review of this exact minutissamide owner, complete
    retained source rows, saved dual-encoding diagnostics and inspected isolation/biosynthesis
    abstracts and bibliographic metadata. Source-specific congener names, strain/locus
    assignments and assay applicability remain explicitly unresolved.
  selection: One current unreviewed record selected in canonical path order; official
    batch89 selection and intake exactly reconcile the frozen owner and source evidence.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  exclusions:
  - target: Complete natural structure and stereochemistry
    reason: Full primary bodies, structure figure pixels, supplementary data and complete
      atom-level correspondence were not inspected; normalized InChI agreement is
      bounded representation evidence.
  - target: Natural A/B/C/D name and assay correspondence
    reason: Source databases assign conflicting congener labels to the retained full
      keys. Inspected abstracts do not establish the graph-to-paper-compound map required
      for names, pure-compound assay values or producer assignment.
  - target: Fresh external authority resolution
    reason: Retained chemical and taxon identifiers were checked in local rows; complete
      live authority equivalence was not established.
checks:
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: Fresh corpus gate passed:3116 PATHS.tsv rows and3116 files, each at its
    pinned path.
  command: env -u PYTEST_ADDOPTS UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache
    RECORD_REVIEW_BASE=ce6a5498df5be51116bd5e0c119023ee62bb5464 PYTHONDONTWRITEBYTECODE=1
    just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: Fresh batch087 command on ce6a5498df5be51116bd5e0c119023ee62bb5464 in
    /private/tmp/npm-record-reviews-20261021. Started 2026-10-28T21:33:09.338684Z;
    finished 2026-10-28T21:33:29.829334Z; ROOT observed at 2026-10-28T21:38:57.679080Z.
    Original receipt /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/verify-corpus.json;
    transcript /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/verify-corpus.log.
    PYTEST_ADDOPTS was explicitly unset. Full tracked byte/mode capture and recheck
    occurred separately after these gates; no pre-gate capture is inferred. Warnings,
    configured exceptions and skips remain in the original transcript.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: Fresh reproduction gate passed:all3116 records are byte-identical to seeding
    from maintained inputs.
  command: env -u PYTEST_ADDOPTS UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache
    RECORD_REVIEW_BASE=ce6a5498df5be51116bd5e0c119023ee62bb5464 PYTHONDONTWRITEBYTECODE=1
    just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: Fresh batch087 command on ce6a5498df5be51116bd5e0c119023ee62bb5464 in
    /private/tmp/npm-record-reviews-20261021. Started 2026-10-28T21:33:09.338638Z;
    finished 2026-10-28T21:33:44.898261Z; ROOT observed at 2026-10-28T21:38:57.679080Z.
    Original receipt /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/verify-reproduction.json;
    transcript /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/verify-reproduction.log.
    PYTEST_ADDOPTS was explicitly unset. Full tracked byte/mode capture and recheck
    occurred separately after these gates; no pre-gate capture is inferred. Warnings,
    configured exceptions and skips remain in the original transcript.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: Fresh deterministic review queue produced8922 rows across12 queues; this
    is not scientific review coverage.
  command: env -u PYTEST_ADDOPTS UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache
    RECORD_REVIEW_BASE=ce6a5498df5be51116bd5e0c119023ee62bb5464 PYTHONDONTWRITEBYTECODE=1
    just review-queue --tsv /private/tmp/npm-review-queue-batch-087-freshce6a5498-001.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: Fresh batch087 command on ce6a5498df5be51116bd5e0c119023ee62bb5464 in
    /private/tmp/npm-record-reviews-20261021. Started 2026-10-28T21:33:09.340163Z;
    finished 2026-10-28T21:33:21.471992Z; ROOT observed at 2026-10-28T21:38:57.679080Z.
    Original receipt /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/review-queue.json;
    transcript /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/review-queue.log.
    PYTEST_ADDOPTS was explicitly unset. Full tracked byte/mode capture and recheck
    occurred separately after these gates; no pre-gate capture is inferred. Warnings,
    configured exceptions and skips remain in the original transcript.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: Fresh configured identifier-label gate passed:13472 canonical,657 synonym
    and35 exception matches;499 nonblocking mismatches and4898 no-adapter skips remain
    explicit.
  command: env -u PYTEST_ADDOPTS UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache
    RECORD_REVIEW_BASE=ce6a5498df5be51116bd5e0c119023ee62bb5464 PYTHONDONTWRITEBYTECODE=1
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: Fresh batch087 command on ce6a5498df5be51116bd5e0c119023ee62bb5464 in
    /private/tmp/npm-record-reviews-20261021. Started 2026-10-28T21:33:09.340947Z;
    finished 2026-10-28T21:33:45.063118Z; ROOT observed at 2026-10-28T21:38:57.679080Z.
    Original receipt /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/validate-products.json;
    transcript /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/validate-products.log.
    PYTEST_ADDOPTS was explicitly unset. Full tracked byte/mode capture and recheck
    occurred separately after these gates; no pre-gate capture is inferred. Warnings,
    configured exceptions and skips remain in the original transcript.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
- check_id: shared-qc
  name: Full repository quality gate on the fresh main baseline
  status: passed
  required: true
  summary: Fresh full quality gate passed:1024 tests passed,4 skipped,2 dependency
    warnings;3116 closed-schema records have zero errors; site freshness, reproduction
    and lockfile checks passed, alongside22 governed artifacts and15 raw inventories.
  command: env -u PYTEST_ADDOPTS UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache
    RECORD_REVIEW_BASE=ce6a5498df5be51116bd5e0c119023ee62bb5464 PYTHONDONTWRITEBYTECODE=1
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Fresh batch087 command on ce6a5498df5be51116bd5e0c119023ee62bb5464 in
    /private/tmp/npm-record-reviews-20261021. Started 2026-10-28T21:33:14.328372Z;
    finished 2026-10-28T21:38:03.336464Z; ROOT observed at 2026-10-28T21:38:57.679080Z.
    Original receipt /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/qc.json;
    transcript /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/qc.log.
    PYTEST_ADDOPTS was explicitly unset. Full tracked byte/mode capture and recheck
    occurred separately after these gates; no pre-gate capture is inferred. Warnings,
    configured exceptions and skips remain in the original transcript.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/minutissamide-a.yaml
    --out /private/tmp/npm-review-work/887/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-29T01:00:55.250647Z. Original
    receipt: /private/tmp/npm-review-work/887/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
- check_id: SCI887-ENCODINGS
  name: Saved structure representations and stereochemical resolution
  status: passed
  required: true
  summary: Saved SMILES and InChI parses agree on formula C55H89N13O16, Standard InChI
    and key HZHLPFLQTJCCHS-HFAMINCGSA-N. The SMILES parse has 11 specified tetrahedral
    sites and two specified double-bond sites, with zero unspecified SMILES sites;
    stereo_complete=true. Both saved representations have a 31-member C21N10 ring
    and a five-member C4N ring. Both canonical-SMILES comparisons and the complete
    atom correspondence are false. InChI adds 11 unspecified C(O)=N representation
    sites; these are separate from the retained tetrahedral-resolution flag and do
    not prove missing natural stereochemistry. These saved diagnostic results do not
    identify the natural congener.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ENCODINGS
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI887-IDENTITY
  name: Source-specific congener names and exact full-key correspondence
  status: unavailable
  required: true
  summary: Which source-specific A/B/C/D structure and supported stereochemical resolution
    corresponds to full key HZHLPFLQTJCCHS-HFAMINCGSA-N? MIBiG BGC0001952/version3
    and BGC0001953/version4 both name minutissamide A; the exact-key CyanoMetDB row
    names Minutissamide C. The inspected abstracts do not supply a full graph-to-label
    map. Preserve these literal discrepancies and the existing shared-structure discussion;
    neither a correct replacement name nor a chemically wrong record is established
    here.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-ENCODINGS
  - SCI887-PUBMED2011
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
  - SCI887-CONTEXT-PEER
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI887-PRODUCER
  name: Producer assertions versus source strain scope
  status: unavailable
  required: true
  summary: The two retained MIBiG producer claims name Anabaena minutissima UTEX B1613
    and Anabaena sp. UHCC-0399. PMID21699148 reports isolation of its A–D compounds
    from cultured UTEX1613; PMID30504214 names UTEX B1613 specifically in the putative
    D chlorination explanation. Neither inspected abstract resolves each retained
    full key to both producer strains, validates taxon IDs or equates the strain literals.
    Preserve SOURCE_ASSERTION and distinguish isolation/occurrence from compound-specific
    biosynthesis.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2011
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI887-OCCURRENCE
  name: Occurrence citations and exact-congener applicability
  status: unavailable
  required: true
  summary: LOTUS and CyanoMetDB occurrences remain database assertions for Anabaena
    minutissima. Own PMID21699148/DOI10.1021/np2002226 identifies the A–D isolation
    work, but exact full-key correspondence remains unresolved because the retained
    source labels differ. The second exact-key LOTUS row and owner occurrence use
    literal DOI10.1021/NP200236C. Its own Crossref title instead names ethyl tumonoate
    A from cf. Oscillatoria margaritifera, which creates a bounded citation-applicability
    concern for this retained occurrence. The metadata lacks an abstract and article
    body; the title does not prove the unread article excludes minutissamides, establish
    a wrong isomer or justify replacing the citation. UTEX1613 occurrence must not
    be promoted to either retained producer solely from isolation.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2011
  - SCI887-PENDING-CITATIONS
  - SCI887-CONTEXT-PEER
  - SCI887-CROSSREF-NP200236C
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI887-BIOSYNTHESIS
  name: Family biosynthesis versus exact locus and congener experiments
  status: unavailable
  required: true
  summary: The retained active BGC0001952/version3 and BGC0001953/version4 rows report
    questionable quality, unknown completeness and no locus-method entries, with MH325199.1
    and MH325200.1. The locus grade remains CLUSTER_UNSTATED. The 2019 abstract supplies
    PUW/MIN family context and a putative D halogenase explanation, not an independently
    checked experiment assigning these exact retained structures to both loci. Neither
    database quality labels nor abstract language certify a current version, precise
    locus, enzyme identity or causal edge.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI887-BIOACTIVITY
  name: Paper compound assays and nontransfer to unresolved owner
  status: unavailable
  required: true
  summary: The 2011 abstract reports ordered HT29 IC50 results for its four A–D/1–4
    compounds; no value is transferred to this record without an exact structure-to-compound
    map. The 2019 major-variant antibacterial statement and PUW F yeast activity are
    not this owner’s assay. Local bioactivity/target fields and assay/target rows
    are empty; emptiness is neither a biological negative result nor an automatic
    major defect.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2011
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI887-GRAPH
  name: Mechanism fields and causal specificity
  status: unavailable
  required: true
  summary: No inline graph, referenced component, biosynthetic pathway or molecular
    target is retained in this owner. The inspected family-level starter-module and
    putative chlorination statements do not justify fabricating exact-owner enzyme
    steps, a complex, substrate edges or direct targets. Completing a graph is separate
    from resolving the congener correspondence.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI887-CLASSIFICATION
  name: Computed filing versus asserted classification
  status: passed
  required: true
  summary: The current path is amino_acids_and_peptides and np_pathway is AMINO_ACIDS_AND_PEPTIDES.
    The exact-key NPClassifier row, model npclassifier.gnps2.org@2026-09-07, reports
    Amino acids and Peptides / Oligopeptides / Cyclic peptides and is_glycoside=false.
    The retained MIBiG bgc_class NRPS is a separate source assertion. The computed
    filing is preserved and does not establish biological origin or resolve the A/B/C/D
    label conflict.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-ENCODINGS
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI887-PROVENANCE
  name: Source versions, evidence placement and current conditional context
  status: passed
  required: true
  summary: The retained MIBiG versions3/4 and entry-level PMID30504214 are distinct
    from the CyanoMetDB PMID21699148 and LOTUS DOI citations. Two seed events and
    the open shared-structure discussion remain. The 37 current official source inputs
    use the regular AGENTS.md context and agree with the captured owner and raw rows.
    Original machine/retrieval clocks are retained separately from later source interpretation.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2011
  - SCI887-PUBMED2019
  - SCI887-CONTEXT-PEER
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI887-GROUNDING
  name: Minted record identity and unverified authority equivalence
  status: unavailable
  required: true
  summary: The owner retains minted identifier naturalproductmech:mibig-9fd577c5ae
    with a content-hash rationale and PubChem cross-reference pubchem:53467644. Its
    exact joined ChEBI sets are empty. These local facts do not freshly verify the
    PubChem structure, a live ChEBI absence claim or every taxon authority. The pending
    label question does not justify an invented replacement identifier.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI887-AVAILABILITY
  name: Inspected source extent and completed metadata boundary
  status: unavailable
  required: true
  summary: Own PubMed fields and the complete returned PMC frontmatter/abstracts were
    inspected; original retrieval clocks remain separate from later scientific reading.
    The full PMC6365827 XML route is held because substantive body/back were not returned.
    PMC3142320 was unattempted at the accepted failed-canary boundary. No figure pixels,
    supplementary files, spectra or full structural depictions were inspected. The
    six-DOI metadata group is complete and accepted within its bibliographic scope
    after independent response review; the current official intake is reconciled.
    Own NP200236C metadata adds only a title-limited occurrence-citation question,
    not full article coverage.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-PUBMED2011
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
  - SCI887-SOURCE-HOLD
  - SCI887-CONTEXT-PEER
  - SCI887-PENDING-CITATIONS
  - SCI887-CROSSREF-COMPLETION
  - SCI887-CROSSREF-NP200236C
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
evidence:
- evidence_id: SCI887-LOCAL
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/minutissamide-a.yaml
  locator: whole owner; chemical_structure; occurrences; producer_organisms; biosynthetic_gene_clusters;
    source_concepts; discussions; curation_history
  accessed_at: '2026-10-28T23:47:10.346565Z'
  snapshot_sha256: a04d20aa1ea89955cf918438dd1075ffd82b3520bef55ba0bfda21ef261b11b5
  support: context_only
  summary: The whole owner is labeled minutissamide A, key HZHLPFLQTJCCHS-HFAMINCGSA-N,
    NATURAL_PRODUCT and SEEDED. It retains two MIBiG producer/BGC assertions, SOURCE_ASSERTION
    and CLUSTER_UNSTATED, two seed-history entries, and an open shared-structure discussion.
    The owner contains no bioactivities, molecular targets, biosynthetic pathway,
    inline causal graph or referenced component; these are local-field observations
    only.
- evidence_id: SCI887-ROWS
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/bgc-tentative89-owner-source-reconnaissance-DATA-001.json
  locator: /records/6/retained_rows; /records/6/supplemental_rows; /records/6/row_guards
  accessed_at: '2026-10-28T23:47:10.346565Z'
  snapshot_sha256: 1fb4869ecc967e2a94b073ff4b524f8b9d084f2e15f3b7e8aa9429d9734ea6e2
  support: context_only
  summary: MIBiG BGC0001952/version3 and BGC0001953/version4 both name minutissamide
    A; the exact-key CyanoMetDB row names Minutissamide C. The exact-key joins contain
    two MIBiG, 2 LOTUS, one NPClassifier and one CyanoMetDB row. Both ChEBI sets and
    all PubChem BioAssay/BindingDB/AntibioticMech joins are empty. The raw producer/BGC
    reference is literal PMID:30504214 at ENTRY scope; the CyanoMetDB isolation citation
    is literal PMID:21699148. These are retained database rows, not verified structure
    assignments.
- evidence_id: SCI887-ENCODINGS
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/source-science-preparation/native-tentative89-ten-owner-dual-encoding-results-001.json
  locator: /records/6/smiles; /records/6/inchi; /records/6/stereo_counts; /records/6/comparisons;
    /records/6/atom_correspondence
  accessed_at: '2026-10-28T23:59:21.473794Z'
  snapshot_sha256: 356c8827be928050a8b7082816ba6ea6f707f5a5881cf0f1ceecf15e16e37570
  support: supports
  summary: Saved SMILES and InChI parses agree on formula C55H89N13O16, Standard InChI
    and key HZHLPFLQTJCCHS-HFAMINCGSA-N. The SMILES parse has 11 specified tetrahedral
    sites and two specified double-bond sites, with zero unspecified SMILES sites;
    stereo_complete=true. Both saved representations have a 31-member C21N10 ring
    and a five-member C4N ring. Both canonical-SMILES comparisons and the complete
    atom correspondence are false. InChI adds 11 unspecified C(O)=N representation
    sites; these are separate from the retained tetrahedral-resolution flag and do
    not prove missing natural stereochemistry. These saved diagnostic results do not
    identify the natural congener.
- evidence_id: SCI887-PUBMED2011
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-three-unattempted-PubMed-001/pmid-21699148.xml
  locator: ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract;
    ./PubmedArticle/PubmedData/ArticleIdList
  accessed_at: '2026-10-29T00:31:36.551249Z'
  snapshot_sha256: b5634811aea3a358bedf758d59ebf855db6e9a180b892360421b7af5822d53aa
  support: partial
  summary: Own PMID21699148 identifies the A–D isolation paper, DOI10.1021/np2002226
    and PMC3142320. Its abstract reports four cyclic decapeptides from cultured Anabaena
    minutissima UTEX1613, planar and stereochemical characterization, and ordered
    A–D/1–4 HT29 antiproliferative results. The source describes four named paper
    compounds; it does not give a full InChIKey mapping in these inspected fields.
- evidence_id: SCI887-PUBMED2019
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-three-unattempted-PubMed-001/pmid-30504214.xml
  locator: ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract;
    ./PubmedArticle/PubmedData/ArticleIdList
  accessed_at: '2026-10-29T00:31:09.133224Z'
  snapshot_sha256: 2a5587a48520b5d78135002cba5a5d914f0f82083a8aba24d128c06fca5b909f
  support: partial
  summary: Own PMID30504214 identifies DOI10.1128/AEM.02675-18 and PMC6365827. Its
    abstract reports PUW/MIN clusters and variants from six strains, alternative starter
    modules, and a putative halogenase explanation for minutissamide D chlorination
    in UTEX B1613. The reported major-variant antibacterial limitation and PUW F yeast
    activity retain their stated scope.
- evidence_id: SCI887-PMC-FRONT
  kind: primary_source
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-primary-two-own-PMC-001/pmc6365827.xml
  locator: ./article/front/article-meta/article-id; ./article/front/article-meta/abstract[1];
    ./article/front/article-meta/abstract[2]
  accessed_at: '2026-10-29T00:48:47.756620Z'
  snapshot_sha256: fba0d825c8f33e32e914e794406e16e9652864ce644cc27e924d3c63124f4354
  support: partial
  summary: The complete returned PMC6365827 XML confirms the own article identifiers
    and supplies a precis plus the abstract/importance text. It retains the six-strain
    PUW/MIN framing, putative MIN D chlorination explanation and PUW F-specific yeast
    statement. The two abstract elements overlap; they are not independent experimental
    confirmations.
- evidence_id: SCI887-SOURCE-HOLD
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/root-tentative89-PMC6365827-frontmatter-only-hold-observation-001.json
  locator: whole original execution/access/index/body joins; selectors; unattempted_identifiers
  accessed_at: '2026-10-29T00:51:11.112172Z'
  snapshot_sha256: 19204a638e5b227b0363bf204f6ced7ba1389981632378d442ee3dce1a49053e
  support: context_only
  summary: The one initial PMC6365827 XML route returned complete HTTP200 frontmatter
    with an explicit publisher restriction comment, zero article body and zero back.
    The collector held that route. PMC3142320 remained unattempted in this phase.
    A returned full-text restriction is not evidence that the article, figures or
    supplementary material do not exist.
  search_scope: One exact initial URL https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=6365827&retmode=xml
    at original access 2026-10-29T00:48:47.449780Z through 2026-10-29T00:48:47.756620Z;
    no redirects, retries, alternate or remaining invocation. Exact isolated output
    filenames, including ignored names, were checked in the accepted peer. No global
    literature absence claim.
- evidence_id: SCI887-CONTEXT-PEER
  kind: prior_review
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/review-support-tentative89-PMC6365827-actual-response-context-independent-peer-001.json
  locator: /owner_context; /literal_citation_placements; /scientific_claim_scope;
    /unattempted_boundary
  accessed_at: '2026-10-29T00:53:37.327057Z'
  snapshot_sha256: 93f3c01b9d3080edda218bf1cce0f6ceb189b67fa7763a85e12a293fb587f6be
  support: context_only
  summary: The accepted bounded response/context peer preserves both whole minutissamide
    owners and exact raw rows, separates the source-specific name discrepancies from
    chemical identity, and retains the lack of a verified full-key mapping or congener-specific
    assay transfer. Its reading clock is later than the original retrieval clocks.
- evidence_id: SCI887-PENDING-CITATIONS
  kind: prior_review
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/native-tentative89-six-unresolved-DOI-cache-route-DATA-001.json
  locator: /lead_adjudications; /proposed_initial_Crossref_jobs; /resolved_DOI_exclusions
  accessed_at: '2026-10-29T00:45:03.584765Z'
  snapshot_sha256: bb9febe093624c768fb7ca5080dcf4dd446891f754c4d5e3237f42c0a4154e54
  support: context_only
  summary: At its original recorded clock, this accepted route DATA excluded verified
    own metadata aliases and identified six unresolved DOI works for a separate metadata
    group. NP200236C was a distinct record887 occurrence-citation lead, not NP2002226.
    This preserved pre-request assessment is not the later retrieval or its applicability
    result.
- evidence_id: SCI887-CROSSREF-NP200236C
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-six-unresolved-crossref-001/doi-04.json
  locator: /message/DOI; /message/title; /message/published-online; /message/published-print;
    /message/reference-count
  accessed_at: '2026-10-29T00:57:20.576642Z'
  snapshot_sha256: 8fa17103e6d0fb124b61efcd7b2869bf7dde79e4ce1d3b9749ab0b31fce504c2
  support: context_only
  summary: Own Crossref DOI10.1021/np200236c has the title Phylogeny-Guided Isolation
    of Ethyl Tumonoate A from the Marine Cyanobacterium cf. Oscillatoria margaritifera,
    with 2011 publication dates. The returned metadata has no abstract or article
    body and contains 34 foreign reference entries. Publisher/PDF links are uninspected
    leads; title and references alone do not establish the complete contents of the
    article.
- evidence_id: SCI887-CROSSREF-COMPLETION
  kind: prior_review
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/root-tentative89-six-crossref-complete-reading-001.json
  locator: /records; /index; /all_complete_body_bytes_read; /all_own_DOIs_verified;
    /scientific_scope; /source_failures_added; /canonical_failures_added
  accessed_at: '2026-10-29T00:58:38.268422Z'
  snapshot_sha256: 25be192812d13bdcbf548e5c49e3bdc304bed90f10b1031f0bbf7f68d08eb055
  support: context_only
  summary: ROOT reports complete own-DOI reads for all six selected Crossref metadata
    responses, no added source or canonical failures, and no article abstracts or
    bodies. ROOT distinguishes NP200236C from the minutissamides A–D DOI and limits
    its title to a citation-applicability question. This is a later reading receipt;
    original retrieval clocks are separately retained.
assessments:
- assessment_id: SCI887-ENCODINGS
  area: consistency
  topic: Saved structure representations and stereochemical resolution
  outcome: supported
  summary: Saved SMILES and InChI parses agree on formula C55H89N13O16, Standard InChI
    and key HZHLPFLQTJCCHS-HFAMINCGSA-N. The SMILES parse has 11 specified tetrahedral
    sites and two specified double-bond sites, with zero unspecified SMILES sites;
    stereo_complete=true. Both saved representations have a 31-member C21N10 ring
    and a five-member C4N ring. Both canonical-SMILES comparisons and the complete
    atom correspondence are false. InChI adds 11 unspecified C(O)=N representation
    sites; these are separate from the retained tetrahedral-resolution flag and do
    not prove missing natural stereochemistry. These saved diagnostic results do not
    identify the natural congener.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ENCODINGS
  dimensions:
  - name: stereochemical_resolution
    value: 11 specified tetrahedral sites and two specified double-bond sites, with
      zero unspecified SMILES sites; stereo_complete=true
    definition: Literal owner flag and saved local stereochemical diagnostics. Normalized
      InChI agreement is distinct from canonical graph/string equality or natural
      stereochemical proof.
    evidence_ids:
    - SCI887-LOCAL
    - SCI887-ENCODINGS
- assessment_id: SCI887-IDENTITY
  area: identity
  topic: Source-specific congener names and exact full-key correspondence
  outcome: unknown
  summary: Which source-specific A/B/C/D structure and supported stereochemical resolution
    corresponds to full key HZHLPFLQTJCCHS-HFAMINCGSA-N? MIBiG BGC0001952/version3
    and BGC0001953/version4 both name minutissamide A; the exact-key CyanoMetDB row
    names Minutissamide C. The inspected abstracts do not supply a full graph-to-label
    map. Preserve these literal discrepancies and the existing shared-structure discussion;
    neither a correct replacement name nor a chemically wrong record is established
    here.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-ENCODINGS
  - SCI887-PUBMED2011
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
  - SCI887-CONTEXT-PEER
- assessment_id: SCI887-PRODUCER
  area: provenance
  topic: Producer assertions versus source strain scope
  outcome: unknown
  summary: The two retained MIBiG producer claims name Anabaena minutissima UTEX B1613
    and Anabaena sp. UHCC-0399. PMID21699148 reports isolation of its A–D compounds
    from cultured UTEX1613; PMID30504214 names UTEX B1613 specifically in the putative
    D chlorination explanation. Neither inspected abstract resolves each retained
    full key to both producer strains, validates taxon IDs or equates the strain literals.
    Preserve SOURCE_ASSERTION and distinguish isolation/occurrence from compound-specific
    biosynthesis.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2011
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
  dimensions:
  - name: taxon_strain
    value: Retained UTEX B1613 / NCBITaxon:2303153 and UHCC-0399 / NCBITaxon:2303154;
      occurrence Anabaena minutissima / NCBITaxon:2303152
    definition: Literal database taxa and strains; source-specific congener correspondence
      and taxonomic authority resolution remain unverified.
    evidence_ids:
    - SCI887-LOCAL
    - SCI887-ROWS
    - SCI887-PUBMED2011
    - SCI887-PUBMED2019
- assessment_id: SCI887-OCCURRENCE
  area: evidence
  topic: Occurrence citations and exact-congener applicability
  outcome: unknown
  summary: LOTUS and CyanoMetDB occurrences remain database assertions for Anabaena
    minutissima. Own PMID21699148/DOI10.1021/np2002226 identifies the A–D isolation
    work, but exact full-key correspondence remains unresolved because the retained
    source labels differ. The second exact-key LOTUS row and owner occurrence use
    literal DOI10.1021/NP200236C. Its own Crossref title instead names ethyl tumonoate
    A from cf. Oscillatoria margaritifera, which creates a bounded citation-applicability
    concern for this retained occurrence. The metadata lacks an abstract and article
    body; the title does not prove the unread article excludes minutissamides, establish
    a wrong isomer or justify replacing the citation. UTEX1613 occurrence must not
    be promoted to either retained producer solely from isolation.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2011
  - SCI887-PENDING-CITATIONS
  - SCI887-CONTEXT-PEER
  - SCI887-CROSSREF-NP200236C
- assessment_id: SCI887-BIOSYNTHESIS
  area: evidence
  topic: Family biosynthesis versus exact locus and congener experiments
  outcome: unknown
  summary: The retained active BGC0001952/version3 and BGC0001953/version4 rows report
    questionable quality, unknown completeness and no locus-method entries, with MH325199.1
    and MH325200.1. The locus grade remains CLUSTER_UNSTATED. The 2019 abstract supplies
    PUW/MIN family context and a putative D halogenase explanation, not an independently
    checked experiment assigning these exact retained structures to both loci. Neither
    database quality labels nor abstract language certify a current version, precise
    locus, enzyme identity or causal edge.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
- assessment_id: SCI887-BIOACTIVITY
  area: evidence
  topic: Paper compound assays and nontransfer to unresolved owner
  outcome: unknown
  summary: The 2011 abstract reports ordered HT29 IC50 results for its four A–D/1–4
    compounds; no value is transferred to this record without an exact structure-to-compound
    map. The 2019 major-variant antibacterial statement and PUW F yeast activity are
    not this owner’s assay. Local bioactivity/target fields and assay/target rows
    are empty; emptiness is neither a biological negative result nor an automatic
    major defect.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2011
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
- assessment_id: SCI887-GRAPH
  area: completeness
  topic: Mechanism fields and causal specificity
  outcome: unknown
  summary: No inline graph, referenced component, biosynthetic pathway or molecular
    target is retained in this owner. The inspected family-level starter-module and
    putative chlorination statements do not justify fabricating exact-owner enzyme
    steps, a complex, substrate edges or direct targets. Completing a graph is separate
    from resolving the congener correspondence.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
- assessment_id: SCI887-CLASSIFICATION
  area: representation
  topic: Computed filing versus asserted classification
  outcome: supported
  summary: The current path is amino_acids_and_peptides and np_pathway is AMINO_ACIDS_AND_PEPTIDES.
    The exact-key NPClassifier row, model npclassifier.gnps2.org@2026-09-07, reports
    Amino acids and Peptides / Oligopeptides / Cyclic peptides and is_glycoside=false.
    The retained MIBiG bgc_class NRPS is a separate source assertion. The computed
    filing is preserved and does not establish biological origin or resolve the A/B/C/D
    label conflict.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-ENCODINGS
- assessment_id: SCI887-PROVENANCE
  area: provenance
  topic: Source versions, evidence placement and current conditional context
  outcome: supported
  summary: The retained MIBiG versions3/4 and entry-level PMID30504214 are distinct
    from the CyanoMetDB PMID21699148 and LOTUS DOI citations. Two seed events and
    the open shared-structure discussion remain. The 37 current official source inputs
    use the regular AGENTS.md context and agree with the captured owner and raw rows.
    Original machine/retrieval clocks are retained separately from later source interpretation.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
  - SCI887-PUBMED2011
  - SCI887-PUBMED2019
  - SCI887-CONTEXT-PEER
  dimensions:
  - name: source_version
    value: MIBiG BGC0001952/version3 and BGC0001953/version4; NPClassifier npclassifier.gnps2.org@2026-09-07
    definition: Retained database/model versions; publication dates and live authority
      validation are separate.
    evidence_ids:
    - SCI887-LOCAL
    - SCI887-ROWS
  - name: evidence_tier
    value: DATABASE_ASSERTION; SOURCE_ASSERTION; CLUSTER_UNSTATED; own PubMed abstracts
      and restricted PMC frontmatter
    definition: Different grades apply to taxon, locus, source identity and chemical
      correspondence. Neither a matching citation nor local diagnostic consistency
      upgrades biological proof.
    evidence_ids:
    - SCI887-LOCAL
    - SCI887-ROWS
    - SCI887-PUBMED2011
    - SCI887-PUBMED2019
    - SCI887-PMC-FRONT
- assessment_id: SCI887-GROUNDING
  area: grounding
  topic: Minted record identity and unverified authority equivalence
  outcome: unknown
  summary: The owner retains minted identifier naturalproductmech:mibig-9fd577c5ae
    with a content-hash rationale and PubChem cross-reference pubchem:53467644. Its
    exact joined ChEBI sets are empty. These local facts do not freshly verify the
    PubChem structure, a live ChEBI absence claim or every taxon authority. The pending
    label question does not justify an invented replacement identifier.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-LOCAL
  - SCI887-ROWS
- assessment_id: SCI887-AVAILABILITY
  area: scope
  topic: Inspected source extent and completed metadata boundary
  outcome: unknown
  summary: Own PubMed fields and the complete returned PMC frontmatter/abstracts were
    inspected; original retrieval clocks remain separate from later scientific reading.
    The full PMC6365827 XML route is held because substantive body/back were not returned.
    PMC3142320 was unattempted at the accepted failed-canary boundary. No figure pixels,
    supplementary files, spectra or full structural depictions were inspected. The
    six-DOI metadata group is complete and accepted within its bibliographic scope
    after independent response review; the current official intake is reconciled.
    Own NP200236C metadata adds only a title-limited occurrence-citation question,
    not full article coverage.
  target_ids:
  - naturalproductmech:mibig-9fd577c5ae
  evidence_ids:
  - SCI887-PUBMED2011
  - SCI887-PUBMED2019
  - SCI887-PMC-FRONT
  - SCI887-SOURCE-HOLD
  - SCI887-CONTEXT-PEER
  - SCI887-PENDING-CITATIONS
  - SCI887-CROSSREF-COMPLETION
  - SCI887-CROSSREF-NP200236C
findings: []
actions: []
limitations:
- Which source-specific A/B/C/D structure and supported stereochemical resolution
  corresponds to full key HZHLPFLQTJCCHS-HFAMINCGSA-N? MIBiG BGC0001952/version3 and
  BGC0001953/version4 both name minutissamide A; the exact-key CyanoMetDB row names
  Minutissamide C. The inspected abstracts do not supply a full graph-to-label map.
  Preserve these literal discrepancies and the existing shared-structure discussion;
  neither a correct replacement name nor a chemically wrong record is established
  here.
- The two retained MIBiG producer claims name Anabaena minutissima UTEX B1613 and
  Anabaena sp. UHCC-0399. PMID21699148 reports isolation of its A–D compounds from
  cultured UTEX1613; PMID30504214 names UTEX B1613 specifically in the putative D
  chlorination explanation. Neither inspected abstract resolves each retained full
  key to both producer strains, validates taxon IDs or equates the strain literals.
  Preserve SOURCE_ASSERTION and distinguish isolation/occurrence from compound-specific
  biosynthesis.
- The retained active BGC0001952/version3 and BGC0001953/version4 rows report questionable
  quality, unknown completeness and no locus-method entries, with MH325199.1 and MH325200.1.
  The locus grade remains CLUSTER_UNSTATED. The 2019 abstract supplies PUW/MIN family
  context and a putative D halogenase explanation, not an independently checked experiment
  assigning these exact retained structures to both loci. Neither database quality
  labels nor abstract language certify a current version, precise locus, enzyme identity
  or causal edge.
- The 2011 abstract reports ordered HT29 IC50 results for its four A–D/1–4 compounds;
  no value is transferred to this record without an exact structure-to-compound map.
  The 2019 major-variant antibacterial statement and PUW F yeast activity are not
  this owner’s assay. Local bioactivity/target fields and assay/target rows are empty;
  emptiness is neither a biological negative result nor an automatic major defect.
- Own PubMed fields and the complete returned PMC frontmatter/abstracts were inspected;
  original retrieval clocks remain separate from later scientific reading. The full
  PMC6365827 XML route is held because substantive body/back were not returned. PMC3142320
  was unattempted at the accepted failed-canary boundary. No figure pixels, supplementary
  files, spectra or full structural depictions were inspected. The six-DOI metadata
  group is complete and accepted within its bibliographic scope after independent
  response review; the current official intake is reconciled. Own NP200236C metadata
  adds only a title-limited occurrence-citation question, not full article coverage.
- The review does not establish a replacement name, graph or stereochemical assignment.
  The current owner is unchanged, and actual baseline, selection, intake and strict
  receipts are retained separately from the scientific evidence.
- Record887 retains a LOTUS occurrence for Anabaena minutissima under full key HZHLPFLQTJCCHS-HFAMINCGSA-N
  with literal DOI10.1021/NP200236C. Own Crossref metadata identifies that DOI as
  the 2011 ethyl tumonoate A / cf. Oscillatoria margaritifera paper, distinct from
  the own-verified minutissamides A–D work DOI10.1021/np2002226. This difference warrants
  checking the exact structure–organism–citation applicability. The response contains
  no abstract or article body; its title and 34 foreign reference entries cannot establish
  that the unread paper lacks minutissamide content, prove an incorrect chemical graph,
  or select a replacement citation.
- Source seeding retains five unresolved assay-organism targets (one distinct Human
  label),42 withheld nonspecific producer claims and161 merged-taxonomy rewrites.
- Queue diagnostics rank deterministic curation questions and do not prove literature
  support or review completion.
- 499 configured nonblocking mismatches remain warnings;4898 pairs lacked an adapter.35
  exception and657 synonym matches retain their configured scope; no fresh ontology
  authority retrieval is asserted.
- Four tests were skipped; two dependency deprecations concern LinkML dataclass and
  Pandas copy-on-write behavior. Source seeding warnings and configured gate boundaries
  are retained in the full log.
- Native baseline gates establish configured consistency, not independent biological
  production, exact stereochemistry or primary-source adequacy.
- Configured ontology caches and scientific/test skips retain their original scope;
  a new command execution is not a fresh retrieval of every authority.
- All tracked link objects are hashed as link-target bytes without dereferencing;
  canonical record source intake remains regular-file-only and uses the separately
  reviewed AGENTS.md context projection.
notes:
- The whole local owner and retained source rows were read. Full-owner scientific
  verification remains false; scientific_review denotes the bounded scientific interpretation
  in this report.
- Original owner/source reading, two-encoding computation, primary-text reading, HTTP
  retrieval and later metadata reading retain separate clocks. Official intake separately
  computed SMILES facts.
- No scientific record, maintained input or native curation status was changed. Any
  findings and actions record ROOT-adopted proposed work; exact-source limitations
  and unavailable checks remain explicit.
```
