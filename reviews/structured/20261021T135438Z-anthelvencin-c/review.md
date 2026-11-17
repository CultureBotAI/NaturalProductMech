# Anthelvencin C: exact congener supported, strain and species context incomplete

- Review: 20261021T135438Z-anthelvencin-c
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T13:48:19.321658Z
- Finished UTC: 2026-10-21T13:54:38.151383Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The dimethyl 2020 C graph, NPAtlas identity and native genetic evidence agree at the reported HRMS/MS resolution. The same constitution is called B in2021 and current Wikidata; the owner correctly leaves its stereocentre unspecified. One major finding requires strain and disputed-species qualifications on the producer, BGC and positive same-paper occurrence.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 72, batch 008, selected in path order from the fresh-main authoritative validated catalogue and the separately validated targets in earlier batch commits (publication tracked separately). At selection, 124 of 3116 current records had campaign coverage and 2992 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-bc87d77ef8 | data/natural_products/alkaloids/anthelvencin-c.yaml | generated | anthelvencin C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-bc87d77ef8 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-bc87d77ef8 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-bc87d77ef8 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-bc87d77ef8 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-bc87d77ef8 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-bc87d77ef8 | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Complete owner and component scope | passed | True | naturalproductmech:mibig-bc87d77ef8 | The complete owner and every matching local source row were read. The empty referenced-component set was confirmed by the native resolved reader; all captured input hashes still agree. |
| Exact graph and literal chemical identifiers | passed | True | naturalproductmech:mibig-bc87d77ef8 | Independent Standard/fixed-H calculations resolve NPA033489 and Q82881638. More-specific ChEBI/PubChem candidates and the SDF-only imine geometry are explicitly distinguished. |
| Exact-congener primary support and native genetic scope | passed | True | naturalproductmech:mibig-bc87d77ef8 | The cited complete accepted primary manuscript and official SI were inspected; exact product peaks and native loss experiments support the imported method, with congener-specific rescue limits retained. |
| Experimental stock and contested species qualification | failed | True | naturalproductmech:mibig-bc87d77ef8 | The exact culture is demonstrated, but its strain and disputed biological species placement are absent from the producer/BGC representation. |

## Scientific And Domain Assessments

### Native status and retained seed history

provenance: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

The 3 dated SEEDED_FROM_SOURCES entries and SEEDED status describe generated provenance. No curation event or native status promotion is inferred from this review. The 2026-10-13 table-based reseeding entry, where present, is another seed event.

### Optional mechanism, activity and application fields

completeness: not_applicable. Targets: naturalproductmech:mibig-bc87d77ef8.

The owner has no structured pathway, causal graph, molecular target, bioactivity, summary, clinical status or engineering application claim. Optional enrichment is separate from correcting present assertions; no activity or enzyme function is inferred from the name or class.

### Computed filing and source-asserted classes

representation: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

The owner reproduces its exact-key NPClassifier row, with model version npclassifier.gnps2.org@2026-09-07, Alkaloids filing, all returned superclass/class labels, and false glycoside flag. These are explicitly computed classifications; they do not establish precursor use or natural origin. The separate BGC and compound-class assertions retain their MIBiG source and receive biological assessment in the science packet.

### Structured transcriptomic context

completeness: not_applicable. Targets: naturalproductmech:mibig-bc87d77ef8.

The native producer and exact biosynthetic locus lack a matching dataset in the inspected catalogue. Recombinant E. coli or A. oryzae expression experiments do not become native-producer transcriptomic context; database noncoverage is not negative biological evidence.

### Literal LOTUS organism-identifier routing

provenance: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

Every organism Wikidata identifier in these exact source rows resolves to the stated species and NCBI taxon. Experimental occurrence, strain scope and taxonomy conflicts are assessed against the cited primary sources separately.

### Exact C graph, literal NPAtlas xref and undefined stereocentre

identity: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

The owner, current MIBiG, NPA033489, PubChem property record and original C drawing agree at the asserted unspecified tetrahedral resolution. Neutral formula C20H27N9O3 and full key QLVFNFMPVONXSG-UHFFFAOYSA-N reproduce. No A-specific NMR or assigned-S authority is transferred.

### Exact source concept and eligible ChEBI boundary

grounding: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

BGC0002042:3 reproducibly mints naturalproductmech:mibig-bc87d77ef8. The pinned eligible inventory is empty; current CHEBI:223046 is two-star and S-assigned. It cannot replace the exact unspecified owner simply by sharing its name.

### LOTUS chemical identifier and representation boundary

provenance: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

Q82881638 retains the exact chemical key despite the current B label. Its direct graph, rather than its name, grounds the stored LOTUS triple. PubChem SDF geometry differs only at the terminal amidine under fixed-H encoding; the Standard-key match does not conceal that representational distinction.

### Computed alkaloid filing and separate NRPS source class

representation: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

Versioned NPClassifier peptide/simple-amide outputs are preserved as predictions. The source NRPS class remains distinct; unadopted two-star ChEBI relations are not promoted into asserted owner classes.

### Exact C natural origin and locus support

evidence: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

C is the doubly pyrrole-N-methylated peak IV, measured [M+H]+ 442.2311 versus calculated 442.2310. It disappears in native ant8/ant23/ant24 replacement cultures. Isolation/identification used ATCC 14583-derived ANT012 with a second ant23-ant24 copy. C is restored in the displayed dual ant23-ant24 genetic complementation and racemic precursor-feeding experiments. The authors explicitly report instability prevented NMR confirmation of C.

### Experimental strain and species circumscription

identity: concern. Targets: naturalproductmech:mibig-bc87d77ef8.

The source’s native stock is supported, but the current strongest producer claim and BGC organism label omit ATCC 14583 and the primary-versus-current-database species conflict.

### Imported methods versus later precursor evidence

evidence: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

Knock-out studies and CLUSTER_DEMONSTRATED are supported for this exact congener at the stated 2020 identification resolution. Do not add Enzymatic assays from the later ADPC experiment or misroute the 2021 B label.

### Computed filing and asserted biosynthetic class

representation: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

The pinned NPClassifier peptide/simple-amide alkaloid output is explicitly computed. NRPS is consistent with the primary stand-alone-domain type II NRPS system. The raw Type I subclass is not emitted as a claim in this owner.

### LOTUS exact occurrence and source independence

evidence: supported. Targets: naturalproductmech:mibig-bc87d77ef8.

The sole DOI resolves to the same 2020 study and supports C occurrence in the native stock and its ANT012 derivative at HRMS/MS resolution. The shared species-label caveat applies. It is not independent of the BGC citation.

## Findings

### S072-F-STRAIN: The producer omits the exact stock and disputed species assignment

major / open / confirmed; issue key: mibig-bgc0002042-atcc14583-producer-context.

The 2020 native experiment supports ATCC 14583, but the owner emits an unqualified strongest S. venezuelae producer claim and BGC organism label. The 2021 primary genome analysis disputes this species placement; the current assembly still maps the strain to 54571 with an inconclusive taxonomy check. Qualify both claims without inventing a replacement taxon or discarding valid native production. This repeats the same source-context cause on a distinct congener; it does not supersede another target’s review. The same disputed species label is used by the positive LOTUS occurrence and also requires an explicit strain/taxonomy qualification.

## Recommended Actions And Acceptance Checks

### S072-ACT-STRAIN

Add a consumed strain qualification with source_id=BGC0002042:3, expected_source_row_sha256=4a296bcd7c8128ba970099ebda6117cb3636b3493d054cbce8edfb86cbcfbd44, strain=ATCC 14583, reference=PMID:32129986 and dated curator/rationale. Cite PMID:34877485 in the rationale for the disputed biological species assignment, retaining 54571 as the historical/current deposit mapping with an inconclusive taxonomy check. The existing consumer only qualifies producer context: implement and test guarded propagation of the same context to the existing BGC notes field. Preserve native loss evidence and distinguish ANT012 from WT, dual ant23-ant24 rescue from single-gene rescue, ATCC 14585 from 14583, and 2021 B from 2020 B. Do not relabel the stock as S. gardneri or add a complete-product enzyme method. Retain the HRMS/MS identification and unsuccessful NMR confirmation; qualify the same historical species label in the LOTUS occurrence notes using a separately implemented full-occurrence-row-guarded context path, not deletion of a positive occurrence. LOTUS context guard: exact full row SHA c359f5ccb78462c46e152917fc88516b36098d6282c4793ae6336dce386ddc9b; key QLVFNFMPVONXSG-UHFFFAOYSA-N, taxon NCBITaxon:54571, DOI 10.1021/ACSCHEMBIO.9B00960, organism Wikidata http://www.wikidata.org/entity/Q7623398. No such occurrence-context consumer is claimed to exist.

- Require exactly one matching complete raw compound row and its SHA; altered source data or duplicate qualifiers must fail.
- Test current producer-only strain emission separately from the new BGC-note propagation; preserve exact structure, existing methods, grades and source references.
- Verify both producer and BGC notes name ATCC 14583, cite the 2021 conflict and retain current 54571 mapping without an unsupported replacement species.
- The exact-target canary must preserve congener-specific assay limits and leave unrelated rows unchanged. Run documented strict validation, verify-reproduction, verify-corpus and QC after authorized curation.
- For the new occurrence-context consumer, require the exact complete LOTUS row and its stated SHA; changing any source field or duplicating the qualification must fail. Preserve the positive occurrence and its original reference, adding the qualified ATCC 14583 context without a taxon replacement or grade promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R072-OWNER | data/natural_products/alkaloids/anthelvencin-c.yaml; Complete owner YAML, every source claim and history entry | supports | Root read the complete anthelvencin C owner following its individual intake. It contains 1 occurrences, one producer and one cluster. Its component-reference set and optional mechanism, activity, target, application, cross-corpus and discussion fields are empty. This is based on complete parsed contents, not a filtered text-search miss. |
| R072-LOCAL-SOURCES | /private/tmp/npm-review-work/072/local-sources.json; Every matching MIBiG, LOTUS, ChEBI, CyanoMetDB and NPClassifier row plus complete resolved view | context_only | Root read all matching rows and the complete owner. These retained database assertions and deterministic joins are distinguished from the exact primary experiments assessed separately. |
| R072-IMODULON-DATASETS | /private/tmp/npm-review-work/010/imodulon-datasets.txt; Full 28-row dataset catalogue; actual retrieval receipt retained in 010/imodulon-context-receipts.json | context_only | The full same-session catalogue retrieved at 07:21:15 UTC contains S. albidoflavus and S. coelicolor datasets, but no S. venezuelae, S. argillaceus, S. refuineus or A. candidus dataset. No fresh retrieval is claimed. Matching a species label alone does not establish an exact experimental strain, locus or product. |
| R072-Q7623398 | https://www.wikidata.org/wiki/Special:EntityData/Q7623398.json; Exact entity ID, English/scientific name and P685 NCBI Taxonomy identifier | context_only | The literal organism entity Q7623398 resolves as Streptomyces venezuelae, with P685 54571, matching the local LOTUS organism identifier. This verifies identifier routing only; it does not independently support the compound-occurrence claim or resolve strain-level taxonomy. |
| C072-OWNER | data/natural_products/alkaloids/anthelvencin-c.yaml; Complete owner and resolved mechanism | supports | The exact owner anthelvencin C and all locally resolved contents were read; it identifies QLVFNFMPVONXSG-UHFFFAOYSA-N. |
| C072-RAW | data/raw/mibig_compounds.tsv; Complete relevant source rows | supports | Canonical sorted-JSON full-row SHA256 pins: [{"selector": "BGC0002042:3", "version": "3", "sha256": "4a296bcd7c8128ba970099ebda6117cb3636b3493d054cbce8edfb86cbcfbd44"}]. Source-concept mints: {"BGC0002042:3": "naturalproductmech:mibig-bc87d77ef8"}. Exact eligible ChEBI projection has 0 row(s). |
| C072-SEARCH | /private/tmp/npm-review-work/072/chemistry-local-search.txt; Ignored-inclusive exact key, identifier and slug search | supports | Current owner, curation, configuration and source-code matching paths inspected; this is a bounded local inventory search, not universal absence. |
| C072-CLASS | data/raw/npclassifier.tsv; Exact-key classification row and PATHS filing | context_only | The exact-key classifier row, source model version and owner classification were compared. Computed filing is kept separate from source-asserted BGC and molecular classes. |
| C072-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0002042.3/annotations.json; Complete retained response for the exact identifier/query | supports | Current BGC0002042 version 3 is active, quality questionable, completeness complete. The selected exact compound graph independently agrees with the owner; complete versioned source metadata and changelog were read. |
| C072-NPA | https://www.npatlas.org/api/v1/compound/NPA033489; Complete retained response for the exact identifier/query | supports | Literal NPA033489 resolves canonically, retaining the exact unspecified C20H27N9O3 graph and a single current structure history. Its origin reference is the 2020 paper and its source culture text is ATCC 14583; this database field is not independent isolation evidence. |
| C072-PUBCHEM | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/QLVFNFMPVONXSG-UHFFFAOYSA-N/property/InChIKey,InChI,IsomericSMILES,MolecularFormula,Charge/JSON; Complete retained response for the exact identifier/query | supports | Exact-key PubChem Compound query yields CID 14039041, matching the owner unspecified tetrahedral centre and full Standard/fixed-H graph. This is a CID, not a Substance identifier. |
| C072-PUBCHEM-SDF | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/14039041/SDF; Complete retained response for the exact identifier/query | supports | Official CID 14039041 SDF has the same Standard key but additionally encodes terminal amidine C=N geometry with an explicit H. The differing fixed-H key is retained; no constitutional defect is inferred. |
| C072-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/223046/; Complete retained response for the exact identifier/query | supports | Name hit CHEBI:223046 has two stars and assigns the cyclic centre S, giving QLVFNFMPVONXSG-ZDUSSCGKSA-N. It is neither an exact full-key match nor eligible under the three-star rule. |
| C072-CHEBI-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/223046/; Complete retained response for the exact identifier/query | supports | The official MOL independently confirms the two-star entry's S-assigned graph. It does not justify silently completing the owner stereochemistry. |
| C072-PUBCHEM-ASSIGNED | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/QLVFNFMPVONXSG-ZDUSSCGKSA-N/property/InChIKey,InChI,IsomericSMILES,MolecularFormula,Charge/JSON; Complete retained response for the exact identifier/query | supports | CID 14039043 is the S-assigned sibling representation corresponding to CHEBI:223046, distinct from unspecified CID 14039041. |
| C072-CHEBI-KEY | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=QLVFNFMPVONXSG-UHFFFAOYSA-N&amp;size=100; Complete retained response for the exact identifier/query | supports | The current exact full-key query returns explicit no match. The name query's S-assigned two-star sibling is separately inspected; no global absence is inferred. |
| C072-CHEBI-NAME | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=anthelvencin+C&amp;size=100; Complete retained response for the exact identifier/query | supports | Complete bounded literal-name candidate list read; it supplies CHEBI:223046, not an eligible exact-key identity. |
| C072-WD-Q82881638 | https://www.wikidata.org/wiki/Special:EntityData/Q82881638.json; Literal LOTUS chemical entity; full identity properties | supports | The literal LOTUS chemical entity is currently labelled Anthelvencin B, but its P235/P234 and neutral SMILES encode the owner C20H27N9O3 full key, and it links NPA033489/CID 14039041. The naming crosswalk must remain publication-specific: a label alone must not transfer evidence from the unmethylated 2020 B graph. |
| C072-PRIMARY | DOI:10.1021/acschembio.9b00960; Main chemical-identification paragraph; original Figure 1A and SI S7 | supports | Both pyrroles are N-methylated and the cyclic amidine centre is unspecified. The observed parent [M+H]+ 442.2311 and calculated 442.2310 agree with neutral C20H27N9O3. The SI caption's 428.2151 is inconsistent with its actual C panel and main text; it is not evidence for an owner formula defect. The authors report instability prevented C NMR confirmation. |
| C072-TAX | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=54571&amp;retmode=xml; Complete retained response for the exact identifier/query | supports | Current NCBI 54571 is S. venezuelae at species rank; it does not denote a strain. The source culture and 2021 circumscription conflict remain separately qualified. |
| C072-ASSEMBLY | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&amp;id=4693161&amp;retmode=json; Complete retained response for the exact identifier/query | supports | Current assembly metadata maps exact ATCC 14583 to 54571 but marks the taxonomy check Inconclusive; this does not override the 2021 phylogenomic study. |
| C072-CALC | /private/tmp/npm-review-work/072/chemistry-authority-comparison.json; Full Standard/fixed-H chemistry, formula, charge and all tetrahedral centres | supports | Fresh read-only molecular calculations retain every compared source representation and do not silently add stereochemistry. |
| S072-E-LOCAL | data/natural_products/alkaloids/anthelvencin-c.yaml; Complete owner, resolved local sources and exact BGC0002042:3 raw row | supports | The full owner has no mechanism components. Its exact congener is linked to BGC0002042 version 3 and PMID:32129986 with native knockout methods and strong producer/locus grades. The sole LOTUS occurrence cites the same 2020 paper; it is not an independent study. |
| S072-E-MAIN | https://doi.org/10.1021/acschembio.9b00960; Results: ant8 loss, chemical nature of II–IV, ant23/ant24 tests; Figures 2–4; complete Methods | supports | C is the doubly pyrrole-N-methylated peak IV, measured [M+H]+ 442.2311 versus calculated 442.2310. It disappears in native ant8/ant23/ant24 replacement cultures. Isolation/identification used ATCC 14583-derived ANT012 with a second ant23-ant24 copy. C is restored in the displayed dual ant23-ant24 genetic complementation and racemic precursor-feeding experiments. The authors explicitly report instability prevented NMR confirmation of C. The 2020 study establishes native genetic dependence, not purified final-product enzymology. The proposed Ant15 methylation sequence and individual assembly reactions are not all directly assayed. |
| S072-E-SI | https://acs.figshare.com/doi/suppl/10.1021/acschembio.9b00960; Complete official SI; Tables S1–S3; Figure S7 physical page 21; S8/S9 physical pages 22–24 | supports | The exact product HRMS/MS parent and fragments were inspected. Both pyrrole N-methyl groups are drawn for C; its S7 caption incorrectly repeats 428.2151, whereas the actual parent spectrum and main text give 442.2311. ANT007, ANT008 and ANT009 are native ant8, ant23 and ant24 replacements; ANT013/014 complementation expresses both ant23 and ant24. S8 labels A (1), C (3) and precursor 5; no exact B rescue is shown. The natural ADPC-derived centre is not assigned by racemic feeding. |
| S072-E-2021 | https://doi.org/10.1016/j.isci.2021.103410; Phylogenomic Results; pyrrolamide Results; Figure 4; Methods disruption/expression/assays | supports | The genome analysis separates ATCC 14583/14584/14585 from the authors’ true S. venezuelae group, without naming an accepted replacement species. Main Figure 4 calls the dimethyl compound B, constitutionally the 2020 C; it does not establish the unmethylated 2020 B. New CRISPR deletions were made in ATCC 14585. Purified tagged/TEV-cleaved Athv28 proteins from three stocks make ADPC from glutamine, not complete anthelvencins. |
| S072-E-2021-SI | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8627960/supplementaryFiles; Official mmc1.pdf: Data S1 physical page 15; pathway/PCR physical page 23; Table S1 physical page 26 | context_only | The supplement retains obsolete A regioisomer drawings in both Data S1 and the pathway, unlike the revised main Figure 4. Its observed-mass labels also disagree with calculated masses and the main dataset. The dimethyl B depiction still crosswalks to 2020 C. The exact ATCC 14583 Athv28 core-to-Ant24 bridge is recorded separately; neither sequence equality nor precursor assays establish final-product enzymology. |
| S072-E-LOCUS | https://www.ncbi.nlm.nih.gov/nuccore/MK483114.1; Header, source qualifiers and boundary genes ant22/ant24 | supports | The 30,551 bp accession identifies ATCC 14583, culture_collection ATCC:14583 and taxon 54571. The curated 1540..27652 region is within this accession. The unpublished reference title says 14593, unlike the explicit source/strain fields and primary paper; it is not grounds to replace the experimental stock. No protein functional inference is made from metadata. |
| S072-E-ASSEMBLY | https://www.ncbi.nlm.nih.gov/assembly/GCF_008642355.1; Current assembly UID 4693161; strain, taxid and taxonomy-check-status | supports | Current assembly metadata maps exact ATCC 14583 to S. venezuelae taxid/speciestaxid 54571 and reports an Inconclusive taxonomy check. This is a current deposit mapping, distinct from settled biological species circumscription. |
| S072-E-CONSUMERS | src/naturalproductmech/curate/producer_strains.py; Complete loader; seeder producer/cluster emission lines 1094–1150 | supports | The implemented strain table requires unique exact BGC:compound ID, full raw-row SHA, strain, reference, curator, date and rationale. It qualifies only the producer. BGC-context propagation is not currently implemented and must be explicitly added/tested; reserved decisions.tsv is not a consumed repair. |
| S072-E-QUALIFIER-SEARCH | /private/tmp/npm-review-work/072/science-qualification-search.json; Exact consumed table and loader/seeder search | context_only | No existing BGC0002042 row-specific strain qualification appears in the consumed table or its loader/seeder. The current producer-only versus BGC behavior was separately read from code. |

## Limits And Additional Notes

- The review assesses current record assertions and concrete source questions. It does not claim exhaustive discovery of every subsequent study or require optional mechanistic enrichment as a precondition for review coverage.
- C was assigned by HRMS/MS; the source explicitly reports unsuccessful NMR confirmation because of instability. No absolute hand is added.
- The current Wikidata B label uses different nomenclature from 2020 C; primary references must be crosswalked by graph, not by name.
- The source species/strain context and 2021 phylogenomic conflict are covered by the independent science action; current authority resolution is not experimental proof.
- The 2020 accepted manuscript is retained from a public mirror; its scientific text and official SI were inspected. The original 1965 body was not obtained, but no current claim depends solely on that historical citation.
- No new absolute stereochemistry is established. The owner leaves the ADPC-derived centre unspecified; racemic feeding and A-only NMR do not resolve B/C configuration.
- The 2021 SI has obsolete A drawings and discrepant observed-mass labels; its 14585 genetics and precursor-only assays are not transferred by a congener letter alone. No raw instrument data were reprocessed.
- The configured identifier-label gate accepts 499 warning-level mismatches and 35 explicit exceptions and skips 4,744 no-adapter pairs; exit 0 does not independently verify every identifier or scientific claim.
- The quality suite reports 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). Skipped tests are not counted as passing tests. Existing ontology caches were used; no multi-gigabyte cache download was required.
- Native gates assess deterministic consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy, or literature-level claim support.
- The five reused gates retain their batch004 execution times and cached ontology results. Reuse establishes unchanged repository inputs; it is not a new remote authority query or new assertion of ontology freshness.
- The ignored-inclusive check enumerates record and saved-review YAML paths, and all tracked files are hashed. Generated Python bytecode and external tool caches are not claimed to have been independently byte-pinned at the prior execution.
- No scientific owner, inventory, curation table, native status or history was edited. Actions are proposed work.
- Baseline gates retain their actual original receipts after byte-for-byte input verification; target strict validation ran afresh. Scientific failed or unavailable checks are distinct from bundle validation.

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
review_id: 20261021T135438Z-anthelvencin-c
title: 'Anthelvencin C: exact congener supported, strain and species context incomplete'
started_at: '2026-10-21T13:48:19.321658Z'
finished_at: '2026-10-21T13:54:38.151383Z'
completion: completed
verdict: needs_curation
scientific_review: true
summary: The dimethyl 2020 C graph, NPAtlas identity and native genetic evidence agree
  at the reported HRMS/MS resolution. The same constitution is called B in2021 and
  current Wikidata; the owner correctly leaves its stereocentre unspecified. One major
  finding requires strain and disputed-species qualifications on the producer, BGC
  and positive same-paper occurrence.
source:
  git_revision: 1c2402097718c138b081e00943de8f04de0541cd
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
  - path: conf/sources.yaml
    sha256: d5e8ab63eeebb376589a0c9bf6f7eb92f45913b84243de20d820442ec88d5a98
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
  - path: data/natural_products/alkaloids/anthelvencin-c.yaml
    sha256: 44fe441d3af3d5737356407d0aa70db974e2f0297a3cd948ca23561574880af9
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
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 72, batch 008, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated targets in earlier
    batch commits (publication tracked separately). At selection, 124 of 3116 current
    records had campaign coverage and 2992 remained. The population search included
    ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-bc87d77ef8
targets:
- target_id: naturalproductmech:mibig-bc87d77ef8
  path: data/natural_products/alkaloids/anthelvencin-c.yaml
  label: anthelvencin C
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
  summary: The documented target strict validator completed; scientific support is
    assessed separately.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  command: just validate-strict data/natural_products/alkaloids/anthelvencin-c.yaml
    --out /private/tmp/npm-review-work/072/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T13:48:21.505098Z
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 current record files agree with PATHS.tsv and their pinned filing
    pathways.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055340+00:00;
    finished 2026-10-21T09:55:22.727768+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/verify-corpus.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-corpus.log. Reused
    for batch008 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch008. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3,116 current records passed the documented byte-reproduction gate
    against committed inventories and maintained curation inputs.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055361+00:00;
    finished 2026-10-21T09:56:44.050706+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/verify-reproduction.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-reproduction.log.
    Reused for batch008 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch008. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The exhaustive review queue produced 8,928 diagnostic rows across 12 queues;
    this deterministic output does not establish scientific review.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just review-queue --tsv /private/tmp/npm-review-queue-batch-004.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.057401+00:00;
    finished 2026-10-21T09:54:38.468783+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/review-queue.json;
    transcript: /private/tmp/npm-native-checks/batch-004/review-queue.log. Reused
    for batch008 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch008. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'The configured identifier-label gate passed using the existing ontology
    caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions,
    499 warning-only mismatches and 4,744 pairs skipped because their prefixes have
    no adapter.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.061733+00:00;
    finished 2026-10-21T09:56:36.296159+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/validate-products.json;
    transcript: /private/tmp/npm-native-checks/batch-004/validate-products.log. Reused
    for batch008 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch008. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
- check_id: shared-qc
  name: Full repository quality gate on the current main baseline
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed on the unchanged main baseline
    during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21).
    All configured lint, governance, documentation, provenance, source-queue, schema,
    rendering, reproduction, filing-integrity and reporting stages completed successfully.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:30.560925+00:00;
    finished 2026-10-21T10:04:44.806799+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/qc.json;
    transcript: /private/tmp/npm-native-checks/batch-004/qc.log. Reused for batch008
    only after a fresh fetch/clean branch, equal commit/tree and two reads of all
    9,182 tracked byte streams and modes (208,070,649 bytes), including a recheck
    after the fresh authoritative catalogue. This gate was not rerun for batch008.
    Original execution times, scope, warnings, exceptions and skips are retained.'
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
- check_id: R072-FULL-OWNER
  name: Complete owner and component scope
  status: passed
  required: true
  summary: The complete owner and every matching local source row were read. The empty
    referenced-component set was confirmed by the native resolved reader; all captured
    input hashes still agree.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - R072-OWNER
  - R072-LOCAL-SOURCES
- check_id: C072-IDENTITY-CHECK
  name: Exact graph and literal chemical identifiers
  status: passed
  required: true
  summary: Independent Standard/fixed-H calculations resolve NPA033489 and Q82881638.
    More-specific ChEBI/PubChem candidates and the SDF-only imine geometry are explicitly
    distinguished.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - C072-CALC
  - C072-NPA
  - C072-PUBCHEM
  - C072-CHEBI-MOL
  - C072-WD-Q82881638
- check_id: S072-C-SOURCE
  name: Exact-congener primary support and native genetic scope
  status: passed
  required: true
  summary: The cited complete accepted primary manuscript and official SI were inspected;
    exact product peaks and native loss experiments support the imported method, with
    congener-specific rescue limits retained.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - S072-E-MAIN
  - S072-E-SI
  - S072-E-LOCUS
- check_id: S072-C-TAXON
  name: Experimental stock and contested species qualification
  status: failed
  required: true
  summary: The exact culture is demonstrated, but its strain and disputed biological
    species placement are absent from the producer/BGC representation.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - S072-E-LOCAL
  - S072-E-2021
  - S072-E-ASSEMBLY
evidence:
- evidence_id: R072-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/anthelvencin-c.yaml
  locator: Complete owner YAML, every source claim and history entry
  accessed_at: '2026-10-21T13:49:21.619544Z'
  support: supports
  summary: Root read the complete anthelvencin C owner following its individual intake.
    It contains 1 occurrences, one producer and one cluster. Its component-reference
    set and optional mechanism, activity, target, application, cross-corpus and discussion
    fields are empty. This is based on complete parsed contents, not a filtered text-search
    miss.
  snapshot_sha256: 44fe441d3af3d5737356407d0aa70db974e2f0297a3cd948ca23561574880af9
- evidence_id: R072-LOCAL-SOURCES
  kind: record_content
  reference: /private/tmp/npm-review-work/072/local-sources.json
  locator: Every matching MIBiG, LOTUS, ChEBI, CyanoMetDB and NPClassifier row plus
    complete resolved view
  accessed_at: '2026-10-21T13:49:21.619544Z'
  support: context_only
  summary: Root read all matching rows and the complete owner. These retained database
    assertions and deterministic joins are distinguished from the exact primary experiments
    assessed separately.
  snapshot_sha256: 91dc397233e38af2557fa325fae685bcf2c610256742b060dfe1902eab392893
- evidence_id: R072-IMODULON-DATASETS
  kind: database
  reference: /private/tmp/npm-review-work/010/imodulon-datasets.txt
  locator: Full 28-row dataset catalogue; actual retrieval receipt retained in 010/imodulon-context-receipts.json
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: The full same-session catalogue retrieved at 07:21:15 UTC contains S. albidoflavus
    and S. coelicolor datasets, but no S. venezuelae, S. argillaceus, S. refuineus
    or A. candidus dataset. No fresh retrieval is claimed. Matching a species label
    alone does not establish an exact experimental strain, locus or product.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: R072-Q7623398
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q7623398.json
  locator: Exact entity ID, English/scientific name and P685 NCBI Taxonomy identifier
  accessed_at: '2026-10-21T13:49:50.521993Z'
  support: context_only
  summary: The literal organism entity Q7623398 resolves as Streptomyces venezuelae,
    with P685 54571, matching the local LOTUS organism identifier. This verifies identifier
    routing only; it does not independently support the compound-occurrence claim
    or resolve strain-level taxonomy.
  snapshot_sha256: 4237c4cb9e8b7d14817b3db612f7651549eb3bbb2bb592fc8ab91767ac6b9cdc
- evidence_id: C072-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/anthelvencin-c.yaml
  locator: Complete owner and resolved mechanism
  accessed_at: '2026-10-21T13:53:34.608776Z'
  support: supports
  summary: The exact owner anthelvencin C and all locally resolved contents were read;
    it identifies QLVFNFMPVONXSG-UHFFFAOYSA-N.
  snapshot_sha256: 44fe441d3af3d5737356407d0aa70db974e2f0297a3cd948ca23561574880af9
- evidence_id: C072-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: Complete relevant source rows
  accessed_at: '2026-10-21T13:53:34.608776Z'
  support: supports
  summary: 'Canonical sorted-JSON full-row SHA256 pins: [{"selector": "BGC0002042:3",
    "version": "3", "sha256": "4a296bcd7c8128ba970099ebda6117cb3636b3493d054cbce8edfb86cbcfbd44"}].
    Source-concept mints: {"BGC0002042:3": "naturalproductmech:mibig-bc87d77ef8"}.
    Exact eligible ChEBI projection has 0 row(s).'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: C072-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/072/chemistry-local-search.txt
  locator: Ignored-inclusive exact key, identifier and slug search
  accessed_at: '2026-10-21T13:53:34.768040Z'
  support: supports
  summary: Current owner, curation, configuration and source-code matching paths inspected;
    this is a bounded local inventory search, not universal absence.
  snapshot_sha256: b3104acff8ac74ab14442b7c14a1648387258fa023c021ee796d4f16a81cc287
  search_scope: rg --no-ignore --hidden -l -F -e QLVFNFMPVONXSG-UHFFFAOYSA-N -e naturalproductmech:mibig-bc87d77ef8
    -e anthelvencin-c data/natural_products curation conf src scripts
- evidence_id: C072-CLASS
  kind: record_content
  reference: data/raw/npclassifier.tsv
  locator: Exact-key classification row and PATHS filing
  accessed_at: '2026-10-21T13:53:34.608776Z'
  support: context_only
  summary: The exact-key classifier row, source model version and owner classification
    were compared. Computed filing is kept separate from source-asserted BGC and molecular
    classes.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: C072-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002042.3/annotations.json
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T12:55:37.462606Z'
  support: supports
  summary: Current BGC0002042 version 3 is active, quality questionable, completeness
    complete. The selected exact compound graph independently agrees with the owner;
    complete versioned source metadata and changelog were read.
  snapshot_sha256: 7f848be6a931fccb35fb081abfe16d93320822475b346e13ffa97be2c2c06020
- evidence_id: C072-NPA
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA033489
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T13:03:16.861134Z'
  support: supports
  summary: Literal NPA033489 resolves canonically, retaining the exact unspecified
    C20H27N9O3 graph and a single current structure history. Its origin reference
    is the 2020 paper and its source culture text is ATCC 14583; this database field
    is not independent isolation evidence.
  snapshot_sha256: 39d65cdcae0137a59fec7b70585fe70d7280ab04ceb8a3166c7bd9ffc53d6f46
- evidence_id: C072-PUBCHEM
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/QLVFNFMPVONXSG-UHFFFAOYSA-N/property/InChIKey,InChI,IsomericSMILES,MolecularFormula,Charge/JSON
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T13:03:16.439697Z'
  support: supports
  summary: Exact-key PubChem Compound query yields CID 14039041, matching the owner
    unspecified tetrahedral centre and full Standard/fixed-H graph. This is a CID,
    not a Substance identifier.
  snapshot_sha256: a00a4144826ccf974d0bd4862bfdd8155600dd40c846fc5b08e9f2ad8e361af3
- evidence_id: C072-PUBCHEM-SDF
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/14039041/SDF
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T13:03:43.841083Z'
  support: supports
  summary: Official CID 14039041 SDF has the same Standard key but additionally encodes
    terminal amidine C=N geometry with an explicit H. The differing fixed-H key is
    retained; no constitutional defect is inferred.
  snapshot_sha256: 8ff1ef7798d4f780abeaa5b099eb9d6b71d97503b96a968667afb4ab6f4c8ce7
- evidence_id: C072-CHEBI
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/223046/
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T13:04:19.290534Z'
  support: supports
  summary: Name hit CHEBI:223046 has two stars and assigns the cyclic centre S, giving
    QLVFNFMPVONXSG-ZDUSSCGKSA-N. It is neither an exact full-key match nor eligible
    under the three-star rule.
  snapshot_sha256: 3d6c787ea5105f43e9090b846763b6da69faf5e2d55769cce9eb805fbd97155a
- evidence_id: C072-CHEBI-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/223046/
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T13:04:19.291314Z'
  support: supports
  summary: The official MOL independently confirms the two-star entry's S-assigned
    graph. It does not justify silently completing the owner stereochemistry.
  snapshot_sha256: f4dd54f843cd4ef932355b0b9e136945e6a024954308095873dba4c169a4c741
- evidence_id: C072-PUBCHEM-ASSIGNED
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/QLVFNFMPVONXSG-ZDUSSCGKSA-N/property/InChIKey,InChI,IsomericSMILES,MolecularFormula,Charge/JSON
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T13:04:19.291720Z'
  support: supports
  summary: CID 14039043 is the S-assigned sibling representation corresponding to
    CHEBI:223046, distinct from unspecified CID 14039041.
  snapshot_sha256: b0fa7b83e7a35b5e84561104881878e4abbf508985f9237378af5b39da10e8a5
- evidence_id: C072-CHEBI-KEY
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=QLVFNFMPVONXSG-UHFFFAOYSA-N&size=100
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T13:03:16.152953Z'
  support: supports
  summary: The current exact full-key query returns explicit no match. The name query's
    S-assigned two-star sibling is separately inspected; no global absence is inferred.
  snapshot_sha256: 4813188210d36286a5b176726b7f03e1f5867cbc4cea17168f791068aa40e4be
- evidence_id: C072-CHEBI-NAME
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=anthelvencin+C&size=100
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T13:03:42.281390Z'
  support: supports
  summary: Complete bounded literal-name candidate list read; it supplies CHEBI:223046,
    not an eligible exact-key identity.
  snapshot_sha256: 8b8f7703d0a3cf2e92e664413f63636f6afb75313f29029e8d2fee39a19e1108
- evidence_id: C072-WD-Q82881638
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q82881638.json
  locator: Literal LOTUS chemical entity; full identity properties
  accessed_at: '2026-10-21T13:52:12.269337Z'
  support: supports
  summary: 'The literal LOTUS chemical entity is currently labelled Anthelvencin B,
    but its P235/P234 and neutral SMILES encode the owner C20H27N9O3 full key, and
    it links NPA033489/CID 14039041. The naming crosswalk must remain publication-specific:
    a label alone must not transfer evidence from the unmethylated 2020 B graph.'
  snapshot_sha256: df84bc0794fdc2b1b59818e0af88968b726f4b4966798501c95431b859c7a117
- evidence_id: C072-PRIMARY
  kind: primary_source
  reference: DOI:10.1021/acschembio.9b00960
  locator: Main chemical-identification paragraph; original Figure 1A and SI S7
  accessed_at: '2026-10-21T12:13:40.791747Z'
  support: supports
  summary: Both pyrroles are N-methylated and the cyclic amidine centre is unspecified.
    The observed parent [M+H]+ 442.2311 and calculated 442.2310 agree with neutral
    C20H27N9O3. The SI caption's 428.2151 is inconsistent with its actual C panel
    and main text; it is not evidence for an owner formula defect. The authors report
    instability prevented C NMR confirmation.
  snapshot_sha256: 9ae1b0c6f18276fce63e48ca27d25f9bf1c3c6c6fbf3cb3d52f66cf5a3a5a464
- evidence_id: C072-TAX
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=54571&retmode=xml
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T13:08:56.752265Z'
  support: supports
  summary: Current NCBI 54571 is S. venezuelae at species rank; it does not denote
    a strain. The source culture and 2021 circumscription conflict remain separately
    qualified.
  snapshot_sha256: 402ba95337d317272822f819ce23f97a2999d183713a817066676219fece93c5
- evidence_id: C072-ASSEMBLY
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&id=4693161&retmode=json
  locator: Complete retained response for the exact identifier/query
  accessed_at: '2026-10-21T13:09:09.248060Z'
  support: supports
  summary: Current assembly metadata maps exact ATCC 14583 to 54571 but marks the
    taxonomy check Inconclusive; this does not override the 2021 phylogenomic study.
  snapshot_sha256: f252ab15c2f3efed51486b076625fdb8d1fc1ae7095aef0fda516cbe4d4421e2
- evidence_id: C072-CALC
  kind: validation
  reference: /private/tmp/npm-review-work/072/chemistry-authority-comparison.json
  locator: Full Standard/fixed-H chemistry, formula, charge and all tetrahedral centres
  accessed_at: '2026-10-21T13:53:34.769929Z'
  support: supports
  summary: Fresh read-only molecular calculations retain every compared source representation
    and do not silently add stereochemistry.
  snapshot_sha256: 503777318c651c37ee2c0996e8596411bfe0f7572be48ac16a53809816933d3d
- evidence_id: S072-E-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/anthelvencin-c.yaml
  locator: Complete owner, resolved local sources and exact BGC0002042:3 raw row
  accessed_at: '2026-10-21T13:50:53.894843Z'
  support: supports
  summary: The full owner has no mechanism components. Its exact congener is linked
    to BGC0002042 version 3 and PMID:32129986 with native knockout methods and strong
    producer/locus grades. The sole LOTUS occurrence cites the same 2020 paper; it
    is not an independent study.
  snapshot_sha256: 44fe441d3af3d5737356407d0aa70db974e2f0297a3cd948ca23561574880af9
- evidence_id: S072-E-MAIN
  kind: primary_source
  reference: https://doi.org/10.1021/acschembio.9b00960
  locator: 'Results: ant8 loss, chemical nature of II–IV, ant23/ant24 tests; Figures
    2–4; complete Methods'
  accessed_at: '2026-10-21T12:20:51Z'
  support: supports
  summary: C is the doubly pyrrole-N-methylated peak IV, measured [M+H]+ 442.2311
    versus calculated 442.2310. It disappears in native ant8/ant23/ant24 replacement
    cultures. Isolation/identification used ATCC 14583-derived ANT012 with a second
    ant23-ant24 copy. C is restored in the displayed dual ant23-ant24 genetic complementation
    and racemic precursor-feeding experiments. The authors explicitly report instability
    prevented NMR confirmation of C. The 2020 study establishes native genetic dependence,
    not purified final-product enzymology. The proposed Ant15 methylation sequence
    and individual assembly reactions are not all directly assayed.
  snapshot_sha256: 3479ef8f0b6eba70888f5e72d056efe599fbe91ed60856bded9768ceeeb64663
- evidence_id: S072-E-SI
  kind: primary_source
  reference: https://acs.figshare.com/doi/suppl/10.1021/acschembio.9b00960
  locator: Complete official SI; Tables S1–S3; Figure S7 physical page 21; S8/S9 physical
    pages 22–24
  accessed_at: '2026-10-21T12:13:40.791747Z'
  support: supports
  summary: The exact product HRMS/MS parent and fragments were inspected. Both pyrrole
    N-methyl groups are drawn for C; its S7 caption incorrectly repeats 428.2151,
    whereas the actual parent spectrum and main text give 442.2311. ANT007, ANT008
    and ANT009 are native ant8, ant23 and ant24 replacements; ANT013/014 complementation
    expresses both ant23 and ant24. S8 labels A (1), C (3) and precursor 5; no exact
    B rescue is shown. The natural ADPC-derived centre is not assigned by racemic
    feeding.
  snapshot_sha256: c10501cfc37d06872de9eda36178f20a233429f4085eff5d3070cc341b4a679a
- evidence_id: S072-E-2021
  kind: primary_source
  reference: https://doi.org/10.1016/j.isci.2021.103410
  locator: Phylogenomic Results; pyrrolamide Results; Figure 4; Methods disruption/expression/assays
  accessed_at: '2026-10-21T13:08:06.467062Z'
  support: supports
  summary: The genome analysis separates ATCC 14583/14584/14585 from the authors’
    true S. venezuelae group, without naming an accepted replacement species. Main
    Figure 4 calls the dimethyl compound B, constitutionally the 2020 C; it does not
    establish the unmethylated 2020 B. New CRISPR deletions were made in ATCC 14585.
    Purified tagged/TEV-cleaved Athv28 proteins from three stocks make ADPC from glutamine,
    not complete anthelvencins.
  snapshot_sha256: 3d535ebe79ee79a78715f19c7ae5fd763861004f59e294517299dd505976fc01
- evidence_id: S072-E-2021-SI
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8627960/supplementaryFiles
  locator: 'Official mmc1.pdf: Data S1 physical page 15; pathway/PCR physical page
    23; Table S1 physical page 26'
  accessed_at: '2026-10-21T13:21:04.900081Z'
  support: context_only
  summary: The supplement retains obsolete A regioisomer drawings in both Data S1
    and the pathway, unlike the revised main Figure 4. Its observed-mass labels also
    disagree with calculated masses and the main dataset. The dimethyl B depiction
    still crosswalks to 2020 C. The exact ATCC 14583 Athv28 core-to-Ant24 bridge is
    recorded separately; neither sequence equality nor precursor assays establish
    final-product enzymology.
  snapshot_sha256: a2efc1d0c91d65d84f4aa654dd5a768112504c7ac34b534cec7c3b5ae63fec4a
- evidence_id: S072-E-LOCUS
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/MK483114.1
  locator: Header, source qualifiers and boundary genes ant22/ant24
  accessed_at: '2026-10-21T12:30:53.672999Z'
  support: supports
  summary: The 30,551 bp accession identifies ATCC 14583, culture_collection ATCC:14583
    and taxon 54571. The curated 1540..27652 region is within this accession. The
    unpublished reference title says 14593, unlike the explicit source/strain fields
    and primary paper; it is not grounds to replace the experimental stock. No protein
    functional inference is made from metadata.
  snapshot_sha256: 783b97587fef65bd1b18ff4394a72cae323faf6cffc2c6ebfda60dfd6bf29c51
- evidence_id: S072-E-ASSEMBLY
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/assembly/GCF_008642355.1
  locator: Current assembly UID 4693161; strain, taxid and taxonomy-check-status
  accessed_at: '2026-10-21T13:09:09.541390Z'
  support: supports
  summary: Current assembly metadata maps exact ATCC 14583 to S. venezuelae taxid/speciestaxid
    54571 and reports an Inconclusive taxonomy check. This is a current deposit mapping,
    distinct from settled biological species circumscription.
  snapshot_sha256: f252ab15c2f3efed51486b076625fdb8d1fc1ae7095aef0fda516cbe4d4421e2
- evidence_id: S072-E-CONSUMERS
  kind: record_content
  reference: src/naturalproductmech/curate/producer_strains.py
  locator: Complete loader; seeder producer/cluster emission lines 1094–1150
  accessed_at: '2026-10-21T13:50:53.894843Z'
  support: supports
  summary: The implemented strain table requires unique exact BGC:compound ID, full
    raw-row SHA, strain, reference, curator, date and rationale. It qualifies only
    the producer. BGC-context propagation is not currently implemented and must be
    explicitly added/tested; reserved decisions.tsv is not a consumed repair.
  snapshot_sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
- evidence_id: S072-E-QUALIFIER-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/072/science-qualification-search.json
  locator: Exact consumed table and loader/seeder search
  accessed_at: '2026-10-21T13:51:46.427404Z'
  support: context_only
  summary: No existing BGC0002042 row-specific strain qualification appears in the
    consumed table or its loader/seeder. The current producer-only versus BGC behavior
    was separately read from code.
  snapshot_sha256: d37db80d9e6dd20d7c19ac523e774f132dbb477ae8cc2d724fe2400e93c133e4
  search_scope: Ignored-inclusive exact BGC selector search of the consumed strain
    table and its loader/seeder; no claim of repository-wide absence. Query BGC0002042(:[23])?
    returned exit 1/no match. This does not establish absence of historical reviews
    or unconsumed files.
assessments:
- assessment_id: R072-HISTORY
  area: provenance
  topic: Native status and retained seed history
  outcome: supported
  summary: The 3 dated SEEDED_FROM_SOURCES entries and SEEDED status describe generated
    provenance. No curation event or native status promotion is inferred from this
    review. The 2026-10-13 table-based reseeding entry, where present, is another
    seed event.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - R072-OWNER
- assessment_id: R072-OPTIONAL
  area: completeness
  topic: Optional mechanism, activity and application fields
  outcome: not_applicable
  summary: The owner has no structured pathway, causal graph, molecular target, bioactivity,
    summary, clinical status or engineering application claim. Optional enrichment
    is separate from correcting present assertions; no activity or enzyme function
    is inferred from the name or class.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - R072-OWNER
  - R072-LOCAL-SOURCES
- assessment_id: R072-FILING
  area: representation
  topic: Computed filing and source-asserted classes
  outcome: supported
  summary: The owner reproduces its exact-key NPClassifier row, with model version
    npclassifier.gnps2.org@2026-09-07, Alkaloids filing, all returned superclass/class
    labels, and false glycoside flag. These are explicitly computed classifications;
    they do not establish precursor use or natural origin. The separate BGC and compound-class
    assertions retain their MIBiG source and receive biological assessment in the
    science packet.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - R072-OWNER
  - R072-LOCAL-SOURCES
- assessment_id: R072-IMODULON
  area: completeness
  topic: Structured transcriptomic context
  outcome: not_applicable
  summary: The native producer and exact biosynthetic locus lack a matching dataset
    in the inspected catalogue. Recombinant E. coli or A. oryzae expression experiments
    do not become native-producer transcriptomic context; database noncoverage is
    not negative biological evidence.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - R072-OWNER
  - R072-IMODULON-DATASETS
- assessment_id: R072-ORGANISM-IDS
  area: provenance
  topic: Literal LOTUS organism-identifier routing
  outcome: supported
  summary: Every organism Wikidata identifier in these exact source rows resolves
    to the stated species and NCBI taxon. Experimental occurrence, strain scope and
    taxonomy conflicts are assessed against the cited primary sources separately.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - R072-LOCAL-SOURCES
  - R072-Q7623398
- assessment_id: C072-IDENTITY
  area: identity
  topic: Exact C graph, literal NPAtlas xref and undefined stereocentre
  outcome: supported
  summary: The owner, current MIBiG, NPA033489, PubChem property record and original
    C drawing agree at the asserted unspecified tetrahedral resolution. Neutral formula
    C20H27N9O3 and full key QLVFNFMPVONXSG-UHFFFAOYSA-N reproduce. No A-specific NMR
    or assigned-S authority is transferred.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - C072-OWNER
  - C072-CALC
  - C072-MIBIG
  - C072-NPA
  - C072-PUBCHEM
  - C072-PRIMARY
- assessment_id: C072-GROUNDING
  area: grounding
  topic: Exact source concept and eligible ChEBI boundary
  outcome: supported
  summary: BGC0002042:3 reproducibly mints naturalproductmech:mibig-bc87d77ef8. The
    pinned eligible inventory is empty; current CHEBI:223046 is two-star and S-assigned.
    It cannot replace the exact unspecified owner simply by sharing its name.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - C072-RAW
  - C072-SEARCH
  - C072-CHEBI-KEY
  - C072-CHEBI-NAME
  - C072-CHEBI
  - C072-CHEBI-MOL
- assessment_id: C072-SOURCE-IDENTITY
  area: provenance
  topic: LOTUS chemical identifier and representation boundary
  outcome: supported
  summary: Q82881638 retains the exact chemical key despite the current B label. Its
    direct graph, rather than its name, grounds the stored LOTUS triple. PubChem SDF
    geometry differs only at the terminal amidine under fixed-H encoding; the Standard-key
    match does not conceal that representational distinction.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - C072-WD-Q82881638
  - C072-CALC
  - C072-PUBCHEM-SDF
  - C072-NPA
- assessment_id: C072-CLASSIFICATION
  area: representation
  topic: Computed alkaloid filing and separate NRPS source class
  outcome: supported
  summary: Versioned NPClassifier peptide/simple-amide outputs are preserved as predictions.
    The source NRPS class remains distinct; unadopted two-star ChEBI relations are
    not promoted into asserted owner classes.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - C072-CLASS
  - C072-RAW
  - C072-OWNER
- assessment_id: S072-A-ORIGIN
  area: evidence
  topic: Exact C natural origin and locus support
  outcome: supported
  summary: C is the doubly pyrrole-N-methylated peak IV, measured [M+H]+ 442.2311
    versus calculated 442.2310. It disappears in native ant8/ant23/ant24 replacement
    cultures. Isolation/identification used ATCC 14583-derived ANT012 with a second
    ant23-ant24 copy. C is restored in the displayed dual ant23-ant24 genetic complementation
    and racemic precursor-feeding experiments. The authors explicitly report instability
    prevented NMR confirmation of C.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - S072-E-MAIN
  - S072-E-SI
  - S072-E-LOCUS
  dimensions:
  - name: experimental_strain
    value: ATCC 14583; native replacement mutants; ANT012 identification material
    definition: The stock tested in the cited 2020 native study, distinguished from
      the later ATCC 14585 CRISPR host.
    evidence_ids:
    - S072-E-MAIN
    - S072-E-SI
    - S072-E-2021
  - name: evidence_tier
    value: Native knockout support; no complete-product purified-enzyme assay
    definition: A final-product loss result supports the existing cluster grade without
      transferring precursor enzymology or another congener’s rescue.
    evidence_ids:
    - S072-E-MAIN
    - S072-E-SI
  - name: taxonomic_context
    value: Historical/current deposit 54571; 2021 biological species assignment disputed
    definition: The exact strain remains supported while its species placement requires
      qualification.
    evidence_ids:
    - S072-E-2021
    - S072-E-ASSEMBLY
- assessment_id: S072-A-TAXON
  area: identity
  topic: Experimental strain and species circumscription
  outcome: concern
  summary: The source’s native stock is supported, but the current strongest producer
    claim and BGC organism label omit ATCC 14583 and the primary-versus-current-database
    species conflict.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - S072-E-LOCAL
  - S072-E-2021
  - S072-E-ASSEMBLY
  dimensions:
  - name: taxonomic_context
    value: Historical/current deposit 54571; 2021 biological species assignment disputed
    definition: The exact strain remains supported while its species placement requires
      qualification.
    evidence_ids:
    - S072-E-2021
    - S072-E-ASSEMBLY
- assessment_id: S072-A-METHOD
  area: evidence
  topic: Imported methods versus later precursor evidence
  outcome: supported
  summary: Knock-out studies and CLUSTER_DEMONSTRATED are supported for this exact
    congener at the stated 2020 identification resolution. Do not add Enzymatic assays
    from the later ADPC experiment or misroute the 2021 B label.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - S072-E-MAIN
  - S072-E-SI
  - S072-E-2021
  - S072-E-2021-SI
- assessment_id: S072-A-CLASS
  area: representation
  topic: Computed filing and asserted biosynthetic class
  outcome: supported
  summary: The pinned NPClassifier peptide/simple-amide alkaloid output is explicitly
    computed. NRPS is consistent with the primary stand-alone-domain type II NRPS
    system. The raw Type I subclass is not emitted as a claim in this owner.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - S072-E-LOCAL
  - S072-E-MAIN
- assessment_id: S072-A-OCC
  area: evidence
  topic: LOTUS exact occurrence and source independence
  outcome: supported
  summary: The sole DOI resolves to the same 2020 study and supports C occurrence
    in the native stock and its ANT012 derivative at HRMS/MS resolution. The shared
    species-label caveat applies. It is not independent of the BGC citation.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  evidence_ids:
  - S072-E-LOCAL
  - S072-E-MAIN
  - S072-E-SI
  - S072-E-2021
findings:
- finding_id: S072-F-STRAIN
  issue_key: mibig-bgc0002042-atcc14583-producer-context
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: The producer omits the exact stock and disputed species assignment
  description: The 2020 native experiment supports ATCC 14583, but the owner emits
    an unqualified strongest S. venezuelae producer claim and BGC organism label.
    The 2021 primary genome analysis disputes this species placement; the current
    assembly still maps the strain to 54571 with an inconclusive taxonomy check. Qualify
    both claims without inventing a replacement taxon or discarding valid native production.
    This repeats the same source-context cause on a distinct congener; it does not
    supersede another target’s review. The same disputed species label is used by
    the positive LOTUS occurrence and also requires an explicit strain/taxonomy qualification.
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  field_paths:
  - producer_organisms[0]
  - biosynthetic_gene_clusters[0].organism_taxon_id
  - biosynthetic_gene_clusters[0].organism_label
  - occurrences[0].taxon_id
  - occurrences[0].taxon_label
  - occurrences[0].notes
  evidence_ids:
  - S072-E-LOCAL
  - S072-E-MAIN
  - S072-E-SI
  - S072-E-2021
  - S072-E-ASSEMBLY
  - S072-E-CONSUMERS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Exact-row-pinned strain qualification
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Consumed producer qualification and tested context extension
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Producer and BGC context emission
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Preserved full source row
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/schema/naturalproductmech.yaml
    role: Existing notes fields for source context
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Preserved occurrence row; new tested qualification path required
  rule_id: 'review-yaml-record: preserve experimental strain and source conflicts'
  native_severity: 'major: unsupported unqualified species scope'
  normalization_reason: The strain-level native locus is supported; the strongest
    species claim requires a material qualification.
actions:
- action_id: S072-ACT-STRAIN
  description: 'Add a consumed strain qualification with source_id=BGC0002042:3, expected_source_row_sha256=4a296bcd7c8128ba970099ebda6117cb3636b3493d054cbce8edfb86cbcfbd44,
    strain=ATCC 14583, reference=PMID:32129986 and dated curator/rationale. Cite PMID:34877485
    in the rationale for the disputed biological species assignment, retaining 54571
    as the historical/current deposit mapping with an inconclusive taxonomy check.
    The existing consumer only qualifies producer context: implement and test guarded
    propagation of the same context to the existing BGC notes field. Preserve native
    loss evidence and distinguish ANT012 from WT, dual ant23-ant24 rescue from single-gene
    rescue, ATCC 14585 from 14583, and 2021 B from 2020 B. Do not relabel the stock
    as S. gardneri or add a complete-product enzyme method. Retain the HRMS/MS identification
    and unsuccessful NMR confirmation; qualify the same historical species label in
    the LOTUS occurrence notes using a separately implemented full-occurrence-row-guarded
    context path, not deletion of a positive occurrence. LOTUS context guard: exact
    full row SHA c359f5ccb78462c46e152917fc88516b36098d6282c4793ae6336dce386ddc9b;
    key QLVFNFMPVONXSG-UHFFFAOYSA-N, taxon NCBITaxon:54571, DOI 10.1021/ACSCHEMBIO.9B00960,
    organism Wikidata http://www.wikidata.org/entity/Q7623398. No such occurrence-context
    consumer is claimed to exist.'
  finding_ids:
  - S072-F-STRAIN
  target_ids:
  - naturalproductmech:mibig-bc87d77ef8
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Exact-row-pinned strain qualification
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Consumed producer qualification and tested context extension
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Producer and BGC context emission
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Preserved full source row
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/schema/naturalproductmech.yaml
    role: Existing notes fields for source context
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Preserved occurrence row; new tested qualification path required
  generator: scripts/seed_from_sources.py with the consumed strain table and explicitly
    tested context propagation
  acceptance_checks:
  - Require exactly one matching complete raw compound row and its SHA; altered source
    data or duplicate qualifiers must fail.
  - Test current producer-only strain emission separately from the new BGC-note propagation;
    preserve exact structure, existing methods, grades and source references.
  - Verify both producer and BGC notes name ATCC 14583, cite the 2021 conflict and
    retain current 54571 mapping without an unsupported replacement species.
  - The exact-target canary must preserve congener-specific assay limits and leave
    unrelated rows unchanged. Run documented strict validation, verify-reproduction,
    verify-corpus and QC after authorized curation.
  - For the new occurrence-context consumer, require the exact complete LOTUS row
    and its stated SHA; changing any source field or duplicating the qualification
    must fail. Preserve the positive occurrence and its original reference, adding
    the qualified ATCC 14583 context without a taxon replacement or grade promotion.
limitations:
- The review assesses current record assertions and concrete source questions. It
  does not claim exhaustive discovery of every subsequent study or require optional
  mechanistic enrichment as a precondition for review coverage.
- C was assigned by HRMS/MS; the source explicitly reports unsuccessful NMR confirmation
  because of instability. No absolute hand is added.
- The current Wikidata B label uses different nomenclature from 2020 C; primary references
  must be crosswalked by graph, not by name.
- The source species/strain context and 2021 phylogenomic conflict are covered by
  the independent science action; current authority resolution is not experimental
  proof.
- The 2020 accepted manuscript is retained from a public mirror; its scientific text
  and official SI were inspected. The original 1965 body was not obtained, but no
  current claim depends solely on that historical citation.
- No new absolute stereochemistry is established. The owner leaves the ADPC-derived
  centre unspecified; racemic feeding and A-only NMR do not resolve B/C configuration.
- The 2021 SI has obsolete A drawings and discrepant observed-mass labels; its 14585
  genetics and precursor-only assays are not transferred by a congener letter alone.
  No raw instrument data were reprocessed.
- The configured identifier-label gate accepts 499 warning-level mismatches and 35
  explicit exceptions and skips 4,744 no-adapter pairs; exit 0 does not independently
  verify every identifier or scientific claim.
- The quality suite reports 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21).
  Skipped tests are not counted as passing tests. Existing ontology caches were used;
  no multi-gigabyte cache download was required.
- Native gates assess deterministic consistency and configured invariants. They do
  not establish biological production, stereochemical specificity, evidence adequacy,
  or literature-level claim support.
- The five reused gates retain their batch004 execution times and cached ontology
  results. Reuse establishes unchanged repository inputs; it is not a new remote authority
  query or new assertion of ontology freshness.
- The ignored-inclusive check enumerates record and saved-review YAML paths, and all
  tracked files are hashed. Generated Python bytecode and external tool caches are
  not claimed to have been independently byte-pinned at the prior execution.
notes:
- No scientific owner, inventory, curation table, native status or history was edited.
  Actions are proposed work.
- Baseline gates retain their actual original receipts after byte-for-byte input verification;
  target strict validation ran afresh. Scientific failed or unavailable checks are
  distinct from bundle validation.
tags:
- path-order-campaign
- batch-008
```
