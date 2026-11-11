# Review of 5aTHQ-9n

- Review: 20261021T091137Z-5athq-9n
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T09:00:27.907946Z
- Finished UTC: 2026-10-21T09:11:37.434169Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact primary congener and natural isolation are supported. The producer assertion omits HEK616 and its material combined-culture condition. The 2019 main body and SI remain unavailable for exact genetic-method grading.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 28, batch 003, selected in path order from the fresh-main authoritative validated catalogue and the separately validated pending-PR targets. At selection, 74 of 3116 current records had campaign coverage and 3042 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-099cf744f9 | data/natural_products/alkaloids/5athq-9n.yaml | generated | 5aTHQ-9n |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-099cf744f9 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-099cf744f9 | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-099cf744f9 | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-099cf744f9 | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-099cf744f9 | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate after environment repair | passed | True | naturalproductmech:mibig-099cf744f9 | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Primary exact normal-chain graph comparison | passed | True | naturalproductmech:mibig-099cf744f9 | Primary compound 5 and the achiral owner graph agree. |
| Cited exact-compound occurrence verification | passed | True | naturalproductmech:mibig-099cf744f9 | The 2015 source names and isolates exact 9n from the specified combined culture. |
| Producer cultivation-context audit | failed | True | naturalproductmech:mibig-099cf744f9 | The producer assertion omits the source strain and material combined-culture condition. |
| Exact-congener biosynthetic experiment verification | unavailable | True | naturalproductmech:mibig-099cf744f9 | Original 2019 methods/SI remain inaccessible; abstract-only claims are insufficient to select an exact experimental grade. |
| Pure-compound response and congener-specific endpoint scope | passed | True | naturalproductmech:mibig-099cf744f9 | The exact 9n dose-response was inspected without borrowing an MIC or direct target from another compound. |
| Independent chemical equivalence audit | passed | True | naturalproductmech:mibig-099cf744f9 | Owner, NPAtlas and official ChEBI graphs have identical complete Standard and fixed-H InChIs, full key ZIASNLTUSWPFPK-UHFFFAOYSA-N and no stereocentre. The straight nonyl chain is constitutionally distinct from the branched congener. |
| Current authority mapping | passed | True | naturalproductmech:mibig-099cf744f9 | Current NCBI and Wikidata identifiers agree with the source organism. |
| Direct iModulonDB dataset applicability | not_applicable | False | naturalproductmech:mibig-099cf744f9 | The complete structured catalogue has no exact producer dataset; no proxy expression assay was used. |

## Scientific And Domain Assessments

### Exact normal-chain congener and stereochemical completeness

identity: supported. Targets: naturalproductmech:mibig-099cf744f9.

The owner is primary compound 5, N–H 5-nonyl-1,2,3,4-tetrahydroquinoline. The normal chain and primary formula agree with the graph. No absolute configuration is required because the molecule is achiral; the S assignment of 10a is irrelevant. Companion identifier sections verify current NPA002245 and ChEBI eligibility.

### Exact cited 9n isolation and organism context

evidence: supported. Targets: naturalproductmech:mibig-099cf744f9.

The actual cited 2015 source isolates 9n from S. nigrescens HEK616 combined with T. pulmonis TP-B0596, supporting the exact occurrence with this experimental boundary. Authors assign production to HEK616, but the Figure S3 partner-switch LC-MS panel directly traces 9i; it is not an independent 9n-specific partner comparison.

### Material strain and cultivation boundary

provenance: concern. Targets: naturalproductmech:mibig-099cf744f9.

The MIBiG producer lacks HEK616 and the combined-culture condition even though the original source reports non-detection in the tested pure cultures. Preserving that condition improves provenance without contradicting the source species claim or declaring the partner a co-producer.

### Exact 2019 genetic experiment applicability

evidence: unknown. Targets: naturalproductmech:mibig-099cf744f9.

The current active source supports exact compound membership and the source-faithful empty-method grade. The 2019 abstract reports family-level genetics and acetate feeding, but unavailable main body/SI leave exact 9n products, host/strain, construct and assay mapping unresolved. SOURCE_ASSERTION and CLUSTER_UNSTATED should not be upgraded on the abstract alone.

### 9n pure-compound response with bounded mechanism

evidence: supported. Targets: naturalproductmech:mibig-099cf744f9.

The exact 9n panel shows dose-dependent partial wild-type S. pombe growth inhibition and much weaker effects in the erg mutants over the shown range. Figure 4 gives 24 h and three independent experiments; Figure S5 retains mean/SD. No numerical MIC or fitted IC50 is reported for 9n. Neither the 7n MIC nor a direct membrane-binding target can be transferred. The owner makes no such claim, and the empty optional activity slots are not findings.

### Remaining sparse scientific and audit fields

completeness: not_applicable. Targets: naturalproductmech:mibig-099cf744f9.

No named gene, enzyme, graph, target or clinical claim appears in the complete owner, so no corresponding mechanism or expression-module enrichment is required. Source-versioned classification and three SEEDED events remain; this review does not promote status. Identifier/classification reconciliation is in the companion root packet.

### Exact owner graph and stereochemical resolution

identity: supported. Targets: naturalproductmech:mibig-099cf744f9.

The owner representations are mutually consistent and agree with the official ChEBI graph. The achiral structure justifies stereo_complete:true; branch topology, rather than stereochemistry, separates 9i and 9n.

### Current exact NPAtlas equivalence

identity: supported. Targets: naturalproductmech:mibig-099cf744f9.

Owner, NPAtlas and official ChEBI graphs have identical complete Standard and fixed-H InChIs, full key ZIASNLTUSWPFPK-UHFFFAOYSA-N and no stereocentre. The straight nonyl chain is constitutionally distinct from the branched congener.

### Content-hashed identity and ChEBI eligibility

provenance: supported. Targets: naturalproductmech:mibig-099cf744f9.

The exact live ChEBI match is two-star and the complete committed eligible inventory has no exact full-key row. The minted identifier remains appropriate; current two-star availability is not a grounding defect.

### Producer and occurrence taxon mapping

provenance: supported. Targets: naturalproductmech:mibig-099cf744f9.

Taxon 1920 and Wikidata Q26291447 identify S. nigrescens. Strain and combined-culture qualifications are assessed separately against the primary evidence. No database metadata is promoted to a second independent publication.

### Predicted scaffold class versus experimental biosynthetic origin

evidence: supported. Targets: naturalproductmech:mibig-099cf744f9.

The model-versioned ALKALOIDS filing is reproducible and compatible with the nitrogen heterocycle. Its precursor-named superclass predictions remain tool outputs. PKS is the separate source class, and the unavailable full 2019 experiments limit detailed reaction assignments.

### Applicability of expression context

evidence: not_applicable. Targets: naturalproductmech:mibig-099cf744f9.

No exact producer dataset is available in the inspected structured catalogue. Other Streptomyces species or a co-culture partner are not substitutes for a direct S. nigrescens dataset.

## Findings

### S028-CULTURE-CONTEXT: Preserve the HEK616 combined-culture context for 9n

minor / open / confirmed; issue key: bgc0001917-hek616-combined-culture-provenance.

The exact 9n producer assertion omits HEK616 and the combined-culture condition under which natural compound 5 was isolated. Because the original source reports non-detection in each tested pure culture, this is a material but non-blocking provenance qualification. It does not refute S. nigrescens attribution or prove TP-B0596 is a second producer.

## Recommended Actions And Acceptance Checks

### S028-QUALIFY-PRODUCER

Add an exact BGC0001917:2 producer-strain qualifier pinned to complete raw-row SHA256 b9928d74b58869be705142f70016446955ad311d7a26537c5324c940a960cca8, with strain HEK616 and DOI:10.1021/acs.orglett.5b00607. Preserve the exact compound 5 isolation from HEK616/TP-B0596 combined culture, source-bounded pure-culture non-detection and authors’ producer attribution in the emitted evidence rationale. Do not make the co-culture partner a biosynthetic producer or upgrade taxon/locus evidence grades.

- The existing qualification loader accepts exactly the pinned source row and rejects stale digest, duplicate decision and missing source row.
- Canary generation retains the HEK616 qualifier and full co-culture rationale with the 2015 citation; taxon 1920, LC349994.1, version 4, SOURCE_ASSERTION and CLUSTER_UNSTATED remain unchanged.
- The exact 9n full key, NPA002245 and source-faithful LOTUS occurrence are preserved; no 9i-specific LC-MS control is rewritten as a 9n experiment.
- Run focused producer-qualification tests, target strict validation, reproduction and required repository QC; do not edit generated YAML directly.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| S028-OWNER | data/natural_products/alkaloids/5athq-9n.yaml; Entire owner, resolved local source view and three SEEDED history entries | supports | The neutral achiral 9n owner has one exact LOTUS occurrence, a MIBiG producer/locus assertion and NPA002245. No separate bioactivity, summary, molecular target, pathway, causal graph, related-record or clinical assertion is present. |
| S028-RAW | data/raw/mibig_compounds.tsv; Complete exact BGC0001917:2 row and local extraction | supports | The source preserves the straight-chain 9n graph, version 4, species taxon 1920, LC349994.1, DOI:10.1039/c8ob02846j and no locus methods. Complete raw-row SHA256 b9928d74b58869be705142f70016446955ad311d7a26537c5324c940a960cca8. |
| S028-LOTUS | data/raw/lotus_occurrences.tsv; Exact owner full-key occurrence row | supports | The raw LOTUS row links ZIASNLTUSWPFPK-UHFFFAOYSA-N with S. nigrescens, taxon 1920, Wikidata Q26291447 and the 2015 discovery DOI. The emitted occurrence remains distinct from the MIBiG biosynthetic producer claim. |
| S028-PRIMARY2015 | https://www.lookchem.com/FreePDFArticle_128740-70-5_65987467.htm; Verified original article, Org. Lett. 2015, 17, 1918–1921; Figure 1 compound 5, congener naming, isolation and Figure 4b | supports | The article identifies exact compound 5 as 5aTHQ-9n, with an unbranched nine-carbon chain at THQ C5. It reports compounds 1–8 from combined culture and attributes production to HEK616 under the tested conditions. The pure-compound activity series separately includes 9n. |
| S028-SI2015 | https://ndownloader.figshare.com/files/3809767; Official DOI:10.1021/acs.orglett.5b00607.s001; S2–S4 isolation and compound 5, S12 NMR table, S17 pure-compound curves | supports | Combined-culture fractionation gives 6.4 mg of 9n. Compound 5 is N–H 5-nonyl THQ, C18H29N, with [M+H]+ observed 260.2373 and calculated 260.2374. Table S1 gives the normal terminal methyl at 0.89 ppm as a triplet. Its Figure S5 dose-response is distinct from 9i and the C10 congeners. |
| S028-PRIMARY-MAPPING | /private/tmp/npm-review-work/028/primary-structure-comparison.json; Independent complete owner versus manually transcribed exact primary compound 5 drawing | supports | The straight nine-carbon side chain and THQ ring reproduce ZIASNLTUSWPFPK-UHFFFAOYSA-N and the owner fixed-H InChI. No stereogenic centre exists; 9n is distinct from iso-branched 9i despite their equal formula. |
| S028-ABSTRACT2019 | https://pubmed.ncbi.nlm.nih.gov/30629078/; Complete primary abstract and DOI metadata only; no main body or SI | partial | DOI:10.1039/c8ob02846j again names HEK616/TP-B0596 combined culture and describes acetate feeding, nine cluster genes, heterologous expression and gene inactivation at family level. Exact congener chromatograms, hosts, constructs, individual deletion outcomes and analytical criteria remain uninspected. |
| S028-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0001917.4/annotations.json; Complete current version 4 entry; exact compound 2 and locus evidence arrays | supports | The active version-4 source contains exact 9n with NMR evidence citing 2019. Its locus evidence array is empty, and 0..0 bounds are sentinel values. This supports faithful import and omission of a meaningless interval, without proving an individual gene assay. |
| S028-GENBANK | https://www.ncbi.nlm.nih.gov/nuccore/LC349994.1; Definition, source feature, taxon 1920 and deposited cluster annotation | supports | The LC349994.1 source explicitly identifies S. nigrescens HEK616 and taxon 1920 for the 17,000 bp deposited cluster. This resolves strain provenance; annotated stm genes do not establish a 9n-specific formation experiment. |
| S028-STRAIN-LOADER | src/naturalproductmech/curate/producer_strains.py; Complete source-pinned qualification loader and emitted evidence rationale | context_only | The implemented producer strain table accepts an exact source-row digest and appends the full rationale to producer evidence while preserving taxon and grades. A HEK616 qualifier can therefore preserve the combined-culture condition and authors’ bounded attribution without a new schema or direct generated edit. |
| S028-ACCESS2019 | /private/tmp/npm-review-work/shared-next/5athq2019/access.json; Bounded original primary-body/SI access attempts retained from preparation | unknown | The original publisher body/PDF/author-version routes returned 403; the official SI route returned 404 and alternate publisher SI 403. Crossref/OpenAlex/PubMed supplied metadata or abstract. These are access failures, not evidence against the reported experiments. |
| S028-SEARCH | /private/tmp/npm-review-work/028/science-search-receipts.json; Three target-specific ignored-inclusive repository searches | supports | No existing BGC0001917 qualification or structured review was found in the searched curation/review surfaces. The corpus/source search returns this owner and linked source congeners, without making the congeners review targets. |
| R028-OWNER | data/natural_products/alkaloids/5athq-9n.yaml; Complete generated owner, resolved source views and audit history | supports | The exact 5aTHQ-9n owner has one species-level MIBiG producer and locus, one NPAtlas xref, and one LOTUS occurrence assertion distinct from production. There are no inline or referenced mechanisms, molecular targets or clinical claims. |
| R028-COMPARISON | /private/tmp/npm-review-work/028/identity-comparison.json; Independent RDKit parsing of owner and NPAtlas SMILES plus official ChEBI SMILES and default MOL | supports | Owner, NPAtlas and official ChEBI graphs have identical complete Standard and fixed-H InChIs, full key ZIASNLTUSWPFPK-UHFFFAOYSA-N and no stereocentre. The straight nonyl chain is constitutionally distinct from the branched congener. |
| R028-NPATLAS | https://www.npatlas.org/api/v1/compound/NPA002245?include=classifications; Complete current response independently inspected | supports | NPA002245 retains the 2015 original DOI:10.1021/acs.orglett.5b00607, S. nigrescens HEK616 origin and structure version 1. Its full structure matches the exact owner. This is database metadata, not a new independent isolation experiment. |
| R028-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/199481/; Complete current response independently inspected | supports | CHEBI:199481 is a two-star entry whose complete graph matches the owner. Its genus-level Streptomyces origin cites PMID:25826296. It is not eligible for the repository three-star grounding rule. |
| R028-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/199481/; Complete current response independently inspected | supports | The complete official default MOL independently reconstructs the owner graph and exact stereochemical resolution. |
| R028-CHEBI-QUERY | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=ZIASNLTUSWPFPK-UHFFFAOYSA-N&amp;size=100; Complete current response independently inspected | supports | The complete exact full-key query returns one hit, CHEBI:199481, with two stars. The committed eligible structure inventory also has no full-key row. No eligible three-star grounding was found within these explicit routes. |
| R028-TAXON | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1920&amp;retmode=xml; Complete current response independently inspected | supports | The current NCBI response confirms taxon 1920 as species Streptomyces nigrescens. The deposited accession and source producer use that taxon; the co-culture partner is a separate organism. |
| R028-WIKIDATA | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q26291447&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Complete current response independently inspected | supports | Q26291447 has label Streptomyces nigrescens and NCBI taxon claim 1920. It agrees with the exact imported LOTUS organism mapping. |
| R028-CLASS | data/raw/npclassifier.tsv; Complete exact full-key prediction row and emitted classification | context_only | The pinned model predicts Alkaloids, Tryptophan alkaloids, Anthranilic acid alkaloids and Quinoline alkaloids; the generated owner faithfully preserves these tool-qualified predictions. The separate MIBiG PKS class and primary polyketide proposal are not evidence for tryptophan or anthranilate incorporation. |
| R028-SEARCH | /private/tmp/npm-review-work/028/identity-search.txt; Complete matching output from exact owner ID, full key, xref and label search | supports | The matches identify the owner and expected raw/classification/PATHS surfaces. No exact correction or earlier structured review was found within the searched surfaces, including ignored and hidden files. |
| R028-IMODULON | https://imodulondb.org/; Complete 28-dataset structured catalogue previously retrieved at the stated time | context_only | The catalogue has no S. nigrescens dataset. Its C. glutamicum dataset is not a direct dataset for the producer merely because that species was an alternative co-culture partner. No expression result or absent-gene conclusion is inferred. |

## Limits And Additional Notes

- 2019 body/SI remained unavailable through the previously recorded bounded free-access routes. Exact congener/strain genetic and isotope evidence cannot be graded from its abstract.
- 2015 original article text and figures were inspected on a verified mirror; official ACS SI is directly available. No primary article PDF was obtained.
- The source provides a separate 9n structure, isolation yield and dose-response. Figure S3 tracks 9i, so the C. glutamicum-switch experiment is not upgraded to an exact 9n measurement. No raw NMR reprocessing or assay-curve fitting was performed.
- The current authority comparison is bounded to the exact-key query, returned ChEBI entry/default MOL and current NPAtlas entry. Database origin metadata is not an additional primary isolation experiment.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- Baseline reuse concerns the identical committed inputs and original executed checks; it does not claim a fresh network/governance or ontology-cache refresh.
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
review_id: 20261021T091137Z-5athq-9n
title: Review of 5aTHQ-9n
started_at: '2026-10-21T09:00:27.907946Z'
finished_at: '2026-10-21T09:11:37.434169Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact primary congener and natural isolation are supported. The producer
  assertion omits HEK616 and its material combined-culture condition. The 2019 main
  body and SI remain unavailable for exact genetic-method grading.
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
  - path: data/natural_products/alkaloids/5athq-9n.yaml
    sha256: 06369a7998c8ed56da46a53fee8bb05ec01607807f8b00b6ebad082c3cfaa436
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
  selection: Campaign record 28, batch 003, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated pending-PR targets.
    At selection, 74 of 3116 current records had campaign coverage and 3042 remained.
    The population search included ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-099cf744f9
targets:
- target_id: naturalproductmech:mibig-099cf744f9
  path: data/natural_products/alkaloids/5athq-9n.yaml
  label: 5aTHQ-9n
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
  - naturalproductmech:mibig-099cf744f9
  command: just validate-strict data/natural_products/alkaloids/5athq-9n.yaml --out
    /private/tmp/npm-review-work/028/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T09:00:31.029581Z
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
    Started 2026-10-21T06:36:36.016808+00:00; finished 2026-10-21T06:37:52.997020+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/verify-corpus.log. Reused
    for batch 003 after verifying exact HEAD/base/tree equality and all tracked worktree
    bytes against the original baseline. This command was not rerun for batch 003;
    original times and receipts are retained.'
  target_ids:
  - naturalproductmech:mibig-099cf744f9
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
    Started 2026-10-21T06:36:36.016703+00:00; finished 2026-10-21T06:38:35.570687+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/verify-reproduction.log.
    Reused for batch 003 after verifying exact HEAD/base/tree equality and all tracked
    worktree bytes against the original baseline. This command was not rerun for batch
    003; original times and receipts are retained.'
  target_ids:
  - naturalproductmech:mibig-099cf744f9
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
    Started 2026-10-21T06:36:36.016598+00:00; finished 2026-10-21T06:37:11.018366+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/review-queue.log. Reused
    for batch 003 after verifying exact HEAD/base/tree equality and all tracked worktree
    bytes against the original baseline. This command was not rerun for batch 003;
    original times and receipts are retained.'
  target_ids:
  - naturalproductmech:mibig-099cf744f9
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
    Started 2026-10-21T06:36:56.498212+00:00; finished 2026-10-21T06:38:54.776253+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/validate-products.log.
    Reused for batch 003 after verifying exact HEAD/base/tree equality and all tracked
    worktree bytes against the original baseline. This command was not rerun for batch
    003; original times and receipts are retained.'
  target_ids:
  - naturalproductmech:mibig-099cf744f9
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
    Started 2026-10-21T06:46:02.058886+00:00; finished 2026-10-21T06:54:53.950582+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/qc-attempt4.log. Reused
    for batch 003 after verifying exact HEAD/base/tree equality and all tracked worktree
    bytes against the original baseline. This command was not rerun for batch 003;
    original times and receipts are retained.'
  target_ids:
  - naturalproductmech:mibig-099cf744f9
- check_id: S028-C-IDENTITY
  name: Primary exact normal-chain graph comparison
  status: passed
  required: true
  summary: Primary compound 5 and the achiral owner graph agree.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-PRIMARY-MAPPING
  - S028-SI2015
- check_id: S028-C-OCCURRENCE
  name: Cited exact-compound occurrence verification
  status: passed
  required: true
  summary: The 2015 source names and isolates exact 9n from the specified combined
    culture.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-LOTUS
  - S028-PRIMARY2015
  - S028-SI2015
- check_id: S028-C-CULTURE
  name: Producer cultivation-context audit
  status: failed
  required: true
  summary: The producer assertion omits the source strain and material combined-culture
    condition.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-OWNER
  - S028-PRIMARY2015
  - S028-SI2015
- check_id: S028-C-2019
  name: Exact-congener biosynthetic experiment verification
  status: unavailable
  required: true
  summary: Original 2019 methods/SI remain inaccessible; abstract-only claims are
    insufficient to select an exact experimental grade.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-ABSTRACT2019
  - S028-ACCESS2019
- check_id: S028-C-ACTIVITY
  name: Pure-compound response and congener-specific endpoint scope
  status: passed
  required: true
  summary: The exact 9n dose-response was inspected without borrowing an MIC or direct
    target from another compound.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-PRIMARY2015
  - S028-SI2015
- check_id: R028-C-XREF
  name: Independent chemical equivalence audit
  status: passed
  required: true
  summary: Owner, NPAtlas and official ChEBI graphs have identical complete Standard
    and fixed-H InChIs, full key ZIASNLTUSWPFPK-UHFFFAOYSA-N and no stereocentre.
    The straight nonyl chain is constitutionally distinct from the branched congener.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - R028-COMPARISON
  - R028-NPATLAS
  - R028-MOL
- check_id: R028-C-TAXON
  name: Current authority mapping
  status: passed
  required: true
  summary: Current NCBI and Wikidata identifiers agree with the source organism.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - R028-TAXON
  - R028-WIKIDATA
- check_id: R028-C-IMODULON
  name: Direct iModulonDB dataset applicability
  status: not_applicable
  required: false
  summary: The complete structured catalogue has no exact producer dataset; no proxy
    expression assay was used.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - R028-IMODULON
evidence:
- evidence_id: S028-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/5athq-9n.yaml
  locator: Entire owner, resolved local source view and three SEEDED history entries
  accessed_at: '2026-10-21T09:08:54.672868Z'
  support: supports
  summary: The neutral achiral 9n owner has one exact LOTUS occurrence, a MIBiG producer/locus
    assertion and NPA002245. No separate bioactivity, summary, molecular target, pathway,
    causal graph, related-record or clinical assertion is present.
  snapshot_sha256: 06369a7998c8ed56da46a53fee8bb05ec01607807f8b00b6ebad082c3cfaa436
- evidence_id: S028-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: Complete exact BGC0001917:2 row and local extraction
  accessed_at: '2026-10-21T09:08:54.672868Z'
  support: supports
  summary: The source preserves the straight-chain 9n graph, version 4, species taxon
    1920, LC349994.1, DOI:10.1039/c8ob02846j and no locus methods. Complete raw-row
    SHA256 b9928d74b58869be705142f70016446955ad311d7a26537c5324c940a960cca8.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: S028-LOTUS
  kind: record_content
  reference: data/raw/lotus_occurrences.tsv
  locator: Exact owner full-key occurrence row
  accessed_at: '2026-10-21T09:08:54.672868Z'
  support: supports
  summary: The raw LOTUS row links ZIASNLTUSWPFPK-UHFFFAOYSA-N with S. nigrescens,
    taxon 1920, Wikidata Q26291447 and the 2015 discovery DOI. The emitted occurrence
    remains distinct from the MIBiG biosynthetic producer claim.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: S028-PRIMARY2015
  kind: primary_source
  reference: https://www.lookchem.com/FreePDFArticle_128740-70-5_65987467.htm
  locator: Verified original article, Org. Lett. 2015, 17, 1918–1921; Figure 1 compound
    5, congener naming, isolation and Figure 4b
  accessed_at: '2026-10-21T08:42:29Z'
  support: supports
  summary: The article identifies exact compound 5 as 5aTHQ-9n, with an unbranched
    nine-carbon chain at THQ C5. It reports compounds 1–8 from combined culture and
    attributes production to HEK616 under the tested conditions. The pure-compound
    activity series separately includes 9n.
  snapshot_sha256: cfe3fb8c82d2ffd09c405193ebabe7ce4e4d9649ad4dffa9bb1e6d53e011ae07
- evidence_id: S028-SI2015
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/3809767
  locator: Official DOI:10.1021/acs.orglett.5b00607.s001; S2–S4 isolation and compound
    5, S12 NMR table, S17 pure-compound curves
  accessed_at: '2026-10-21T08:41:12.945270Z'
  support: supports
  summary: Combined-culture fractionation gives 6.4 mg of 9n. Compound 5 is N–H 5-nonyl
    THQ, C18H29N, with [M+H]+ observed 260.2373 and calculated 260.2374. Table S1
    gives the normal terminal methyl at 0.89 ppm as a triplet. Its Figure S5 dose-response
    is distinct from 9i and the C10 congeners.
  snapshot_sha256: 8dc377e262f34a86c4bbaaa695dd451793ea827327c883f86a2d0ae61402cf8f
- evidence_id: S028-PRIMARY-MAPPING
  kind: validation
  reference: /private/tmp/npm-review-work/028/primary-structure-comparison.json
  locator: Independent complete owner versus manually transcribed exact primary compound
    5 drawing
  accessed_at: '2026-10-21T09:08:54.672868Z'
  support: supports
  summary: The straight nine-carbon side chain and THQ ring reproduce ZIASNLTUSWPFPK-UHFFFAOYSA-N
    and the owner fixed-H InChI. No stereogenic centre exists; 9n is distinct from
    iso-branched 9i despite their equal formula.
  snapshot_sha256: 55f5c66f3ebe147ebdb891b8e9c736b52de2d72f5d1f12a46a5a14988bf03e00
- evidence_id: S028-ABSTRACT2019
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/30629078/
  locator: Complete primary abstract and DOI metadata only; no main body or SI
  accessed_at: '2026-10-21T08:30:29.079775Z'
  support: partial
  summary: DOI:10.1039/c8ob02846j again names HEK616/TP-B0596 combined culture and
    describes acetate feeding, nine cluster genes, heterologous expression and gene
    inactivation at family level. Exact congener chromatograms, hosts, constructs,
    individual deletion outcomes and analytical criteria remain uninspected.
  snapshot_sha256: 66d22d6956c8012814aaf79b9687d63700efec06b32d1d5d27485c09adbe721d
- evidence_id: S028-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0001917.4/annotations.json
  locator: Complete current version 4 entry; exact compound 2 and locus evidence arrays
  accessed_at: '2026-10-21T09:01:10.183957Z'
  support: supports
  summary: The active version-4 source contains exact 9n with NMR evidence citing
    2019. Its locus evidence array is empty, and 0..0 bounds are sentinel values.
    This supports faithful import and omission of a meaningless interval, without
    proving an individual gene assay.
  snapshot_sha256: bef63588d404c3c8a800cc0c4c2a2c956d28e3d12e4a748b6724fce7e7c05aff
- evidence_id: S028-GENBANK
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/LC349994.1
  locator: Definition, source feature, taxon 1920 and deposited cluster annotation
  accessed_at: '2026-10-21T09:01:10.650896Z'
  support: supports
  summary: The LC349994.1 source explicitly identifies S. nigrescens HEK616 and taxon
    1920 for the 17,000 bp deposited cluster. This resolves strain provenance; annotated
    stm genes do not establish a 9n-specific formation experiment.
  snapshot_sha256: 303964fbee92f641d2299022f235ecc5f211051a03d601a921d59e1bf48cda7e
- evidence_id: S028-STRAIN-LOADER
  kind: record_content
  reference: src/naturalproductmech/curate/producer_strains.py
  locator: Complete source-pinned qualification loader and emitted evidence rationale
  accessed_at: '2026-10-21T09:05:39.511050Z'
  support: context_only
  summary: The implemented producer strain table accepts an exact source-row digest
    and appends the full rationale to producer evidence while preserving taxon and
    grades. A HEK616 qualifier can therefore preserve the combined-culture condition
    and authors’ bounded attribution without a new schema or direct generated edit.
  snapshot_sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
- evidence_id: S028-ACCESS2019
  kind: search
  reference: /private/tmp/npm-review-work/shared-next/5athq2019/access.json
  locator: Bounded original primary-body/SI access attempts retained from preparation
  accessed_at: '2026-10-21T08:32:04.929079Z'
  support: unknown
  summary: The original publisher body/PDF/author-version routes returned 403; the
    official SI route returned 404 and alternate publisher SI 403. Crossref/OpenAlex/PubMed
    supplied metadata or abstract. These are access failures, not evidence against
    the reported experiments.
  snapshot_sha256: 02a10dbbbdbc4cf1f55a2c49d733f7afb23f144276fc18bedb2c905f3f1b822f
  search_scope: Previously attempted official RSC article HTML/PDF/current platform/author-version
    and both official SI hosts, plus Crossref/OpenAlex/PubMed discovery; no renewed
    failed route or paid access.
- evidence_id: S028-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/028/science-search-receipts.json
  locator: Three target-specific ignored-inclusive repository searches
  accessed_at: '2026-10-21T09:08:54.672868Z'
  support: supports
  summary: No existing BGC0001917 qualification or structured review was found in
    the searched curation/review surfaces. The corpus/source search returns this owner
    and linked source congeners, without making the congeners review targets.
  snapshot_sha256: 15f22096715397a046e5b870f5a07276baa8d315863c1e3e9f75b972f8d56d0a
  search_scope: rg -l --no-ignore --hidden for 5aTHQ-9n, 5athq-9n, mibig-099cf744f9,
    ZIASNLTUSWPFPK and BGC0001917 across curation, reviews/structured, data/natural_products,
    data/causal_graphs and data/raw; ignored and hidden files included.
- evidence_id: R028-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/5athq-9n.yaml
  locator: Complete generated owner, resolved source views and audit history
  accessed_at: '2026-10-21T09:10:08.549027Z'
  support: supports
  summary: The exact 5aTHQ-9n owner has one species-level MIBiG producer and locus,
    one NPAtlas xref, and one LOTUS occurrence assertion distinct from production.
    There are no inline or referenced mechanisms, molecular targets or clinical claims.
  snapshot_sha256: 06369a7998c8ed56da46a53fee8bb05ec01607807f8b00b6ebad082c3cfaa436
- evidence_id: R028-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/028/identity-comparison.json
  locator: Independent RDKit parsing of owner and NPAtlas SMILES plus official ChEBI
    SMILES and default MOL
  accessed_at: '2026-10-21T09:05:14.510554Z'
  support: supports
  summary: Owner, NPAtlas and official ChEBI graphs have identical complete Standard
    and fixed-H InChIs, full key ZIASNLTUSWPFPK-UHFFFAOYSA-N and no stereocentre.
    The straight nonyl chain is constitutionally distinct from the branched congener.
  snapshot_sha256: d2ada10983dc0b63de88164ed658515de93ebf9d55dc2cbcd1e8d470890b0a97
- evidence_id: R028-NPATLAS
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA002245?include=classifications
  locator: Complete current response independently inspected
  accessed_at: '2026-10-21T09:01:09.978513Z'
  support: supports
  summary: NPA002245 retains the 2015 original DOI:10.1021/acs.orglett.5b00607, S.
    nigrescens HEK616 origin and structure version 1. Its full structure matches the
    exact owner. This is database metadata, not a new independent isolation experiment.
  snapshot_sha256: b13ff90987e0945257b495c70a8594bb12d695c2bc0a659182f07facb232849a
- evidence_id: R028-CHEBI
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/199481/
  locator: Complete current response independently inspected
  accessed_at: '2026-10-21T09:04:25.700354Z'
  support: supports
  summary: CHEBI:199481 is a two-star entry whose complete graph matches the owner.
    Its genus-level Streptomyces origin cites PMID:25826296. It is not eligible for
    the repository three-star grounding rule.
  snapshot_sha256: e5051f07fdcc6bada92b9eef3c4ffb9cb6153d60b754f1b28ca4b19f6d22c845
- evidence_id: R028-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/199481/
  locator: Complete current response independently inspected
  accessed_at: '2026-10-21T09:04:25.723292Z'
  support: supports
  summary: The complete official default MOL independently reconstructs the owner
    graph and exact stereochemical resolution.
  snapshot_sha256: 0beefdde10cd0e918ce8a4d04a997b04aec8d417643eede45de5a6ef8333e14c
- evidence_id: R028-CHEBI-QUERY
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=ZIASNLTUSWPFPK-UHFFFAOYSA-N&size=100
  locator: Complete current response independently inspected
  accessed_at: '2026-10-21T09:01:10.178132Z'
  support: supports
  summary: The complete exact full-key query returns one hit, CHEBI:199481, with two
    stars. The committed eligible structure inventory also has no full-key row. No
    eligible three-star grounding was found within these explicit routes.
  snapshot_sha256: 1d4bed4f9dd4115a1b6f143aaa234a857d18d4a94650313db87e1f0e62931e6f
- evidence_id: R028-TAXON
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1920&retmode=xml
  locator: Complete current response independently inspected
  accessed_at: '2026-10-21T09:01:10.747814Z'
  support: supports
  summary: The current NCBI response confirms taxon 1920 as species Streptomyces nigrescens.
    The deposited accession and source producer use that taxon; the co-culture partner
    is a separate organism.
  snapshot_sha256: ff4827e0deaf9d60551fabfb3052e7fc2f645e2597cfdaf47ce23ba5ad5650a6
- evidence_id: R028-WIKIDATA
  kind: database
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q26291447&props=labels%7Cclaims&languages=en&format=json
  locator: Complete current response independently inspected
  accessed_at: '2026-10-21T09:01:10.848517Z'
  support: supports
  summary: Q26291447 has label Streptomyces nigrescens and NCBI taxon claim 1920.
    It agrees with the exact imported LOTUS organism mapping.
  snapshot_sha256: 2464655f0f8a26a215b586943f506e3fd242f99310e7cc0985f093e2de470aee
- evidence_id: R028-CLASS
  kind: record_content
  reference: data/raw/npclassifier.tsv
  locator: Complete exact full-key prediction row and emitted classification
  accessed_at: '2026-10-21T09:10:08.549027Z'
  support: context_only
  summary: The pinned model predicts Alkaloids, Tryptophan alkaloids, Anthranilic
    acid alkaloids and Quinoline alkaloids; the generated owner faithfully preserves
    these tool-qualified predictions. The separate MIBiG PKS class and primary polyketide
    proposal are not evidence for tryptophan or anthranilate incorporation.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: R028-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/028/identity-search.txt
  locator: Complete matching output from exact owner ID, full key, xref and label
    search
  accessed_at: '2026-10-21T09:05:15.587978Z'
  support: supports
  summary: The matches identify the owner and expected raw/classification/PATHS surfaces.
    No exact correction or earlier structured review was found within the searched
    surfaces, including ignored and hidden files.
  snapshot_sha256: f61f7a848b7993e13d7af0efd6360870fa7492eebbed8f01c1a43496e518f8b7
  search_scope: rg -n --no-ignore --hidden -F -e naturalproductmech:mibig-099cf744f9
    -e ZIASNLTUSWPFPK-UHFFFAOYSA-N -e NPA002245 -e 5aTHQ-9n curation reviews/structured
    data/natural_products data/raw src scripts conf
- evidence_id: R028-IMODULON
  kind: database
  reference: https://imodulondb.org/
  locator: Complete 28-dataset structured catalogue previously retrieved at the stated
    time
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: The catalogue has no S. nigrescens dataset. Its C. glutamicum dataset is
    not a direct dataset for the producer merely because that species was an alternative
    co-culture partner. No expression result or absent-gene conclusion is inferred.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
assessments:
- assessment_id: S028-IDENTITY
  area: identity
  topic: Exact normal-chain congener and stereochemical completeness
  outcome: supported
  summary: The owner is primary compound 5, N–H 5-nonyl-1,2,3,4-tetrahydroquinoline.
    The normal chain and primary formula agree with the graph. No absolute configuration
    is required because the molecule is achiral; the S assignment of 10a is irrelevant.
    Companion identifier sections verify current NPA002245 and ChEBI eligibility.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-OWNER
  - S028-PRIMARY2015
  - S028-SI2015
  - S028-PRIMARY-MAPPING
- assessment_id: S028-OCCURRENCE
  area: evidence
  topic: Exact cited 9n isolation and organism context
  outcome: supported
  summary: The actual cited 2015 source isolates 9n from S. nigrescens HEK616 combined
    with T. pulmonis TP-B0596, supporting the exact occurrence with this experimental
    boundary. Authors assign production to HEK616, but the Figure S3 partner-switch
    LC-MS panel directly traces 9i; it is not an independent 9n-specific partner comparison.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-LOTUS
  - S028-PRIMARY2015
  - S028-SI2015
- assessment_id: S028-CONTEXT
  area: provenance
  topic: Material strain and cultivation boundary
  outcome: concern
  summary: The MIBiG producer lacks HEK616 and the combined-culture condition even
    though the original source reports non-detection in the tested pure cultures.
    Preserving that condition improves provenance without contradicting the source
    species claim or declaring the partner a co-producer.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-OWNER
  - S028-PRIMARY2015
  - S028-SI2015
  - S028-GENBANK
- assessment_id: S028-BGC
  area: evidence
  topic: Exact 2019 genetic experiment applicability
  outcome: unknown
  summary: The current active source supports exact compound membership and the source-faithful
    empty-method grade. The 2019 abstract reports family-level genetics and acetate
    feeding, but unavailable main body/SI leave exact 9n products, host/strain, construct
    and assay mapping unresolved. SOURCE_ASSERTION and CLUSTER_UNSTATED should not
    be upgraded on the abstract alone.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-RAW
  - S028-MIBIG
  - S028-ABSTRACT2019
  - S028-ACCESS2019
- assessment_id: S028-ACTIVITY
  area: evidence
  topic: 9n pure-compound response with bounded mechanism
  outcome: supported
  summary: The exact 9n panel shows dose-dependent partial wild-type S. pombe growth
    inhibition and much weaker effects in the erg mutants over the shown range. Figure
    4 gives 24 h and three independent experiments; Figure S5 retains mean/SD. No
    numerical MIC or fitted IC50 is reported for 9n. Neither the 7n MIC nor a direct
    membrane-binding target can be transferred. The owner makes no such claim, and
    the empty optional activity slots are not findings.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-OWNER
  - S028-PRIMARY2015
  - S028-SI2015
- assessment_id: S028-OPTIONAL
  area: completeness
  topic: Remaining sparse scientific and audit fields
  outcome: not_applicable
  summary: No named gene, enzyme, graph, target or clinical claim appears in the complete
    owner, so no corresponding mechanism or expression-module enrichment is required.
    Source-versioned classification and three SEEDED events remain; this review does
    not promote status. Identifier/classification reconciliation is in the companion
    root packet.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - S028-OWNER
  - S028-RAW
- assessment_id: R028-IDENTITY
  area: identity
  topic: Exact owner graph and stereochemical resolution
  outcome: supported
  summary: The owner representations are mutually consistent and agree with the official
    ChEBI graph. The achiral structure justifies stereo_complete:true; branch topology,
    rather than stereochemistry, separates 9i and 9n.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - R028-OWNER
  - R028-COMPARISON
  - R028-MOL
- assessment_id: R028-XREF
  area: identity
  topic: Current exact NPAtlas equivalence
  outcome: supported
  summary: Owner, NPAtlas and official ChEBI graphs have identical complete Standard
    and fixed-H InChIs, full key ZIASNLTUSWPFPK-UHFFFAOYSA-N and no stereocentre.
    The straight nonyl chain is constitutionally distinct from the branched congener.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - R028-COMPARISON
  - R028-NPATLAS
  - R028-MOL
- assessment_id: R028-GROUNDING
  area: provenance
  topic: Content-hashed identity and ChEBI eligibility
  outcome: supported
  summary: The exact live ChEBI match is two-star and the complete committed eligible
    inventory has no exact full-key row. The minted identifier remains appropriate;
    current two-star availability is not a grounding defect.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - R028-CHEBI
  - R028-CHEBI-QUERY
  - R028-COMPARISON
- assessment_id: R028-TAXON
  area: provenance
  topic: Producer and occurrence taxon mapping
  outcome: supported
  summary: Taxon 1920 and Wikidata Q26291447 identify S. nigrescens. Strain and combined-culture
    qualifications are assessed separately against the primary evidence. No database
    metadata is promoted to a second independent publication.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - R028-TAXON
  - R028-WIKIDATA
  - R028-NPATLAS
  - R028-OWNER
- assessment_id: R028-CLASSIFICATION
  area: evidence
  topic: Predicted scaffold class versus experimental biosynthetic origin
  outcome: supported
  summary: The model-versioned ALKALOIDS filing is reproducible and compatible with
    the nitrogen heterocycle. Its precursor-named superclass predictions remain tool
    outputs. PKS is the separate source class, and the unavailable full 2019 experiments
    limit detailed reaction assignments.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - R028-CLASS
  - R028-OWNER
- assessment_id: R028-IMODULON
  area: evidence
  topic: Applicability of expression context
  outcome: not_applicable
  summary: No exact producer dataset is available in the inspected structured catalogue.
    Other Streptomyces species or a co-culture partner are not substitutes for a direct
    S. nigrescens dataset.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  evidence_ids:
  - R028-IMODULON
findings:
- finding_id: S028-CULTURE-CONTEXT
  issue_key: bgc0001917-hek616-combined-culture-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve the HEK616 combined-culture context for 9n
  description: The exact 9n producer assertion omits HEK616 and the combined-culture
    condition under which natural compound 5 was isolated. Because the original source
    reports non-detection in each tested pure culture, this is a material but non-blocking
    provenance qualification. It does not refute S. nigrescens attribution or prove
    TP-B0596 is a second producer.
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  field_paths:
  - producer_organisms[0].strain
  - producer_organisms[0].evidence
  evidence_ids:
  - S028-OWNER
  - S028-PRIMARY2015
  - S028-SI2015
  - S028-GENBANK
  - S028-STRAIN-LOADER
  - S028-SEARCH
  rule_id: 'review-checklist: producer organisms retain source strain and experimental
    context'
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned HEK616 qualification and combined-culture rationale
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Existing producer qualification and provenance emitter
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Regenerate the qualified producer claim
actions:
- action_id: S028-QUALIFY-PRODUCER
  description: Add an exact BGC0001917:2 producer-strain qualifier pinned to complete
    raw-row SHA256 b9928d74b58869be705142f70016446955ad311d7a26537c5324c940a960cca8,
    with strain HEK616 and DOI:10.1021/acs.orglett.5b00607. Preserve the exact compound
    5 isolation from HEK616/TP-B0596 combined culture, source-bounded pure-culture
    non-detection and authors’ producer attribution in the emitted evidence rationale.
    Do not make the co-culture partner a biosynthetic producer or upgrade taxon/locus
    evidence grades.
  finding_ids:
  - S028-CULTURE-CONTEXT
  target_ids:
  - naturalproductmech:mibig-099cf744f9
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned HEK616 qualification and combined-culture rationale
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Existing producer qualification and provenance emitter
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Regenerate the qualified producer claim
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - The existing qualification loader accepts exactly the pinned source row and rejects
    stale digest, duplicate decision and missing source row.
  - Canary generation retains the HEK616 qualifier and full co-culture rationale with
    the 2015 citation; taxon 1920, LC349994.1, version 4, SOURCE_ASSERTION and CLUSTER_UNSTATED
    remain unchanged.
  - The exact 9n full key, NPA002245 and source-faithful LOTUS occurrence are preserved;
    no 9i-specific LC-MS control is rewritten as a 9n experiment.
  - Run focused producer-qualification tests, target strict validation, reproduction
    and required repository QC; do not edit generated YAML directly.
limitations:
- 2019 body/SI remained unavailable through the previously recorded bounded free-access
  routes. Exact congener/strain genetic and isotope evidence cannot be graded from
  its abstract.
- 2015 original article text and figures were inspected on a verified mirror; official
  ACS SI is directly available. No primary article PDF was obtained.
- The source provides a separate 9n structure, isolation yield and dose-response.
  Figure S3 tracks 9i, so the C. glutamicum-switch experiment is not upgraded to an
  exact 9n measurement. No raw NMR reprocessing or assay-curve fitting was performed.
- The current authority comparison is bounded to the exact-key query, returned ChEBI
  entry/default MOL and current NPAtlas entry. Database origin metadata is not an
  additional primary isolation experiment.
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
- Baseline reuse concerns the identical committed inputs and original executed checks;
  it does not claim a fresh network/governance or ontology-cache refresh.
notes:
- No scientific owner, inventory, curation table, native status or history was edited.
  Actions are proposed work.
- Baseline gates retain their actual original receipts after byte-for-byte input verification;
  target strict validation ran afresh. Scientific failed or unavailable checks are
  distinct from bundle validation.
tags:
- path-order-campaign
- batch-003
- combined-culture-provenance
- primary-access-limited
```
