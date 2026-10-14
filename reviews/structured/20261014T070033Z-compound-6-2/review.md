# Compound 6 (BGC0002162.3): exact-owner partial review

- Review: 20261014T070033Z-compound-6-2
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-14T06:21:36.335659Z
- Finished UTC: 2026-10-14T07:00:33.430551Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Internally/source-consistent cation record with one provisional major exact-product evidence-scope finding; no corrected structure or exclusion inferred.

## Scope And Provenance

One complete owner including all declared scientific fields and history; no external graph references.

Selection: Next exact owner in the3115-record campaign checkpoint priority, not name-only lookup or representative sampling. The one-record denominator is distinct from the overall campaign denominator.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 22ced0a503edd1d04628f7cfbdbb14ee1d03047c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-fd2940acc4 | data/natural_products/terpenoids/compound-6-2.yaml | generated | compound 6 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| prepare | passed | True | naturalproductmech:mibig-fd2940acc4 | All3115 owner hashes,243 component hashes and87 prior bundles match the checkpoint; exact one-target inspect captured current inputs. |
| strict | passed | True | naturalproductmech:mibig-fd2940acc4 | Documented strict validator checked all four selected owners; zero errors. |
| sources-project-path | passed | True | naturalproductmech:mibig-fd2940acc4 | Pinned RDKit, structured inventory joins, source members, accession versions, taxon ranks and deposited loci checked. |
| local-search | passed | True | naturalproductmech:mibig-fd2940acc4 | Ignored/hidden-inclusive search recorded exact scope; no missing-input inference from default ignore behavior. |
| queue | passed | True | naturalproductmech:mibig-fd2940acc4 | Full documented pending-record queue regenerated into temporary workspace; no native status changes. |
| labels | passed | True | naturalproductmech:mibig-fd2940acc4 | Full-corpus label gate passed with499 non-blocking mismatches and4647 configured adapter skips; not a claim that every pair was independently verified. |
| qc | passed | True | naturalproductmech:mibig-fd2940acc4 | Authoritative full-corpus QC completed on unchanged scientific inputs; not proof of experimental correctness. |
| Primary exact-product closure | unavailable | True | naturalproductmech:mibig-fd2940acc4 | 2015 main text remains denied from prior403; previously retrieved public SI was inspected. Exact-numbered cation characterization and complete stereochemical mapping remain unverified. |
| Structured expression-module applicability | not_applicable | False | naturalproductmech:mibig-fd2940acc4 | No matching native fungal dataset among28 adapter entries; not negative biological evidence. |
| sources | failed | False | naturalproductmech:mibig-fd2940acc4 | Initial supplemental analysis could not import RDKit from project environment; superseded by sources-project-path. |
| sources-chemistry | failed | False | naturalproductmech:mibig-fd2940acc4 | Ephemeral pinned wheel resolution failed for x86_64 macOS; no dependency or lock change; superseded by existing isolated pinned runtime. |
| sources-verified | failed | False | naturalproductmech:mibig-fd2940acc4 | First isolated-runtime invocation omitted project src from PYTHONPATH; superseded by corrected explicit path. |

## Scientific And Domain Assessments

### Exact local owner and source-row identity

identity: supported. Targets: naturalproductmech:mibig-fd2940acc4.

Resolved by exact path, identifier, InChIKey and one-based MIBiG compound index, not the generic name. The internal structure and source member agree. No equivalence with the other compound6/8 owner is inferred.

### Experimental identity and numbered-material context

identity: concern. Targets: naturalproductmech:mibig-fd2940acc4.

The charged C25 species is consistent with a proposed mechanistic intermediate, while the source grades its locus as experimentally demonstrated and annotates NMR. Direct exact-cation characterization has not been established. Primary main-text numbering, strain and stereochemical mapping require adjudication.

### Stereochemical encoding, not experimental assignment

consistency: supported. Targets: naturalproductmech:mibig-fd2940acc4.

Stored stereo_complete=True is consistent with the 0 undefined atom centers. Neither completion nor absence of undefined centers establishes source-derived stereochemistry.

### Minted identity within the pinned corpus

grounding: supported. Targets: naturalproductmech:mibig-fd2940acc4.

No exact key exists in the complete pinned ChEBI structure inventory, supporting the local minted rationale. No global claim about current ChEBI or other registries is made; no replacement identifier was established.

### Separate filing, BGC and taxonomy axes

representation: supported. Targets: naturalproductmech:mibig-fd2940acc4.

Pinned NPClassifier output and PATHS filing agree and remain explicitly computed. The Diterpenoids superclass is not an experimentally asserted molecular class; carbon count is25. No reclassification or directory move follows from this review. The source BGC class and fungal lineage are retained on separate axes.

### Native taxon versus experimental host

scope: unknown. Targets: naturalproductmech:mibig-fd2940acc4.

SOURCE_ASSERTION remains a faithful database grade, not proof of native biosynthesis. NRRL181 resolves as a strain and the JCM catalogue equates it with JCM1740; treating the SI spelling JMC1740 as a transposition is an explicit inference, not a strain-mismatch finding. Heterologous expression does not prove native production of a modeled cation.

### Compound-specific scope of BGC evidence

evidence: concern. Targets: naturalproductmech:mibig-fd2940acc4.

Heterologous end-product synthesis and a proposed mechanistic cation must not be collapsed into direct demonstration of that cation. BGC coordinates and database provenance resolve, but the exact-product experiment does not.

### No optional claims inferred from neighboring products

completeness: not_applicable. Targets: naturalproductmech:mibig-fd2940acc4.

Owner has no occurrence, activity, molecular target, clinical assertion, cross-corpus link or pathway/graph. Complete local joins did not supply exact-key evidence for those surfaces. Activities or mechanisms of neutral sesterfisherol, biscognienyneB or similarly numbered compounds are not transferable. Empty optional fields are not evidence of biological absence.

### Scientific status, discussions and maintained ownership

provenance: supported. Targets: naturalproductmech:mibig-fd2940acc4.

Both seed history events and needs-a-name discussion are preserved. The label task is already explicit; do not invent a synonym. Native SEEDED status is appropriate because experimental identity and origin have not passed sign-off. No scientific input was changed.

## Findings

### cation-evidence-scope: Proposed cation versus demonstrated product remains unqualified

major / open / provisional; issue key: bgc0002162-compound6-cation-evidence-scope.

The owner encodes C25H41+ with 5/15 rings and an explicit carbon-centered positive charge. Its CLUSTER_DEMONSTRATED link is inherited from locus-level heterologous expression. Inspected primary material distinguishes proposed cationic mechanisms from isolated neutral products; the MIBiG NMR attribution has not been traced to a spectrum or experimental characterization of this exact charged structure. Qualify the exact-product evidence and adjudicate its record-versus-pathway-intermediate role. This is not a claim that carbocations cannot occur biologically or that all charged metabolites should be excluded. Main-text access and exact stereochemical/numbering closure remain missing, so no definitive deletion or replacement is asserted.

## Recommended Actions And Acceptance Checks

### primary-closure

Obtain legitimate access to the2015 main text; crosswalk each charged depiction and experimental claim. Retain proposed intermediates as explicitly proposed graph nodes where appropriate, and correct/qualify the exact-product locus grade only after primary adjudication. Do not silently substitute neutral sesterfisherol or bulk-exclude charged structures. A supported admission/exclusion change needs an implemented, tested source-owned mechanism; curation/decisions.tsv is reserved and ineffective.

- Map the exact structure, charge, stereochemistry and compound number to an inspected primary figure/table or spectrum.
- Separate native producer, donor-locus strain and experimental host; grade only the experiment on this exact form.
- Preserve upstream provenance, reviewed neighbors and all unrelated owner/component hashes.
- For authorized curation use validated writer plus event; run strict validation, reproduction, corpus, label and full QC gates.
- Save a new linked review with the same issue key before retiring any finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/terpenoids/compound-6-2.yaml; Entire owner and identical read_natural_product view at 22ced0a503edd1d04628f7cfbdbb14ee1d03047c | supports | Complete YAML read: exact structure, pinned computed filing, one MIBiG producer and locus, source concept, minted rationale, needs-a-name discussion and both history events. No graph refs, inline graph, pathway, occurrence, assay, target, xref or cross-corpus link is declared. |
| chemistry | reviews/evidence/20261014-numbered-products/source-analysis.json; compound-6-2; pinned RDKit 2026.03.5 | supports | SMILES reproduces the exact Standard InChI and key FAUJQEJMUWYQEX-PNWBJGBJSA-N; formula C25H41+, charge 1, exact mass 341.320277732 Da, ring sizes [5, 15]. Atom stereocenters [[3, 'R'], [6, 'R'], [8, 'S']] agree with stereo_complete=True. Internal consistency does not validate experimental identity. |
| inventory | data/raw/mibig_compounds.tsv; BGC0002162:3; full parsed-row SHA256 36baacd0d1cc26fc65bf1d6d2dba84d27f3cc96b583357ba0f3bbdfa0dc9392f | supports | One exact-key MIBiG row and one pinned NPClassifier row per owner. Full parsed inventories contain no exact-key ChEBI structure, LOTUS, assay, BindingDB or sibling-link match. ChEBI origins were joined through matching ChEBI structure IDs, not an absent InChIKey column. These bounded local joins are not claims of global registry absence. |
| local-search | reviews/evidence/20261014-numbered-products/local-search.log; Search command and output hash retained under local-search.receipt.json in the packet checks files | context_only | No earlier canonical review target or applicable curation decision found for these exact owners. Same generic labels denote different structures and must not be merged; neighboring compound5 reviews are context, not review coverage for these targets. |
| taxonomy | NCBITaxon:331117; Exact Taxon, ScientificName, Rank, OtherNames and Lineage elements | supports | NCBI confirms Aspergillus fischeri NRRL181 at strain rank (Neosartorya synonym) and Biscogniauxia sp. at species rank; both descend from Fungi. Taxonomic identity and fungal faceting are not proof of compound production. |
| adapter | reviews/evidence/20261014-numbered-products/imodulondb.log; All 28 returned dataset rows | context_only | Structured iModulonDB inventory contains no Aspergillus/Neosartorya or Biscogniauxia dataset. It is not applicable; E.coli expression hosts and unrelated taxa do not supply native-fungus evidence. |
| bounded-search | Web search, 2026-10-14 UTC; Exact quoted first InChIKey blocks for all four owners | context_only | Bounded exact-key searches did not resolve names or independent experimental identities; this is not a universal absence claim. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0002162.3/annotations.json; Version3 compounds index3, taxonomy and loci; committed response reread locally | partial | Active source repeats this exact charged encoding, assigns compound-level NMR with DOI10.1021/jacs.5b08319, and locus-level heterologous expression. The database assertion is not independent confirmation that this cation was isolated or directly characterized. |
| primary-abstract | DOI:10.1021/jacs.5b08319; PubmedArticle PMID26332841; public abstract and bibliographic identifiers only | partial | The study reports heterologous sesterfisherol production and oxidation to sesterfisheric acid; isotope experiments inform a proposed cyclization mechanism involving cationic intermediates. The abstract does not show isolation or NMR of this exact cation. |
| primary-si | https://ndownloader.figshare.com/files/3765199; DOI10.1021/jacs.5b08319 supporting information: complete pagesS1-S3 text, S12 SchemeS2 pixels, TOC and S5-S10 captions inspected; prior retrieval predates publisher denial | partial | SchemeS2 explicitly presents proposed carbocation mechanisms, including ent-6, not an isolation experiment. S2 names genomic-DNA donor JMC1740 (literal spelling), and S5-S10 describe neutral end-product spectroscopy or enzyme assays. Exact 2015 main-text numbering and complete stereochemical crosswalk remain unavailable; no NMR spectrum is reassigned to cation6 or8. |
| strain-catalogue | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_keyword?AN=Neosartorya&amp;BN=fischeri&amp;CN=fischeri&amp;DN=; JCM1740 entry, deposit history and equivalent culture numbers; not the distinct JCM22241 entry | supports | The collection explicitly equates JCM1740 with NRRL181 and CBS544.65. Interpreting the SI spelling JMC1740 as JCM1740 is a stated typographic inference; no evidence supports a different strain. Culture equivalence does not prove production of either charged compound. |
| later-primary | https://www.nature.com/articles/s41598-018-20916-x; Abstract; Results, Computed Mechanisms and Selectivity; Site-Directed Mutagenesis; Discussion; Methods. Earlier full text read; figure-page request and a later main-page recheck failed at inaccessible identity-provider redirects. No alternate retrieval. | partial | The 2018 study distinguishes calculated cations from isolated F191A-mutant products: the latter are neutral C25H40 hydrocarbons, not these C25H41+ records. It does not establish either stored cation as a directly demonstrated product. Numbered intermediates across publications must not be equated without an atom-level crosswalk. |
| locus | genbank:DS027698.1; Committed 2485363..2490827 slice,5465bp; source and two CDS annotations | supports | The slice is NRRL181/taxon331117 and contains NFIA_055490/EAW16200.1 and NFIA_055500/EAW16201.1. Coordinates resolve, but a genomic deposit cannot prove the charged product. Culture equivalence is separately supported by the JCM catalogue. No new protein grounding was asserted. |

## Limits And Additional Notes

- Partial scientific observation, not a completed review or native REVIEWED promotion. All three missing/failed supplemental setup attempts are retained; corrected analysis succeeded.
- Only this exact owner is assessed; sibling labels, neighboring compounds and the rest of3115-record corpus are not covered by this report.
- The portable evidence packet at reviews/evidence/20261014-numbered-products retains bounded source payloads and command receipts. Temporary paths in receipts describe original execution, not replay dependencies. Articles, SI and abstracts are reference-only, not redistributed.
- Search misses are bounded; local exhaustive inventory joins and ignored-inclusive file searches are distinct from global evidence absence.
- No direct reanalysis of raw experimental spectral data, no new graph/protein claim, no source refresh and no paid retrieval. Publication and issue tracking are separately user-authorized; native scientific inputs remain unchanged.
- 2015 main-text denial remains respected. The2018 main text was inspected as separate research; its figure page redirected to an inaccessible identity-provider endpoint, so pixels were not inspected and no alternate figure retrieval was attempted.
- S12 ent-6 is contextual evidence about a proposed scaffold; an exact stereochemical crosswalk to the stored cation is not asserted. The2018 mutant products and their numbering are not substituted for2015 compounds.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T070033Z-compound-6-2
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Compound 6 (BGC0002162.3): exact-owner partial review'
started_at: '2026-10-14T06:21:36.335659Z'
finished_at: '2026-10-14T07:00:33.430551Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same campaign assistant; not independent human or external review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: SEEDED retained; primary exact-product sign-off incomplete
scientific_review: true
summary: Internally/source-consistent cation record with one provisional major exact-product
  evidence-scope finding; no corrected structure or exclusion inferred.
source:
  git_revision: 22ced0a503edd1d04628f7cfbdbb14ee1d03047c
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
  - path: conf/sibling_pins.yaml
    sha256: 39a1d007ee65ba546567e8a34b7a309f75270b872809e1f783fe1fcee55866f2
    role: context
  - path: curation/decisions.tsv
    sha256: 7214a74975fb2cb65521da18dd14ea1c65665f50060106976dc0db9caf887805
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
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
    role: context
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/compound-8.yaml
    sha256: 996d80d8c8f8eb32b5ee5a074da9d5390601d56585fbacde28b84e3315a246c9
    role: context
  - path: data/natural_products/terpenoids/compound-6-2.yaml
    sha256: ff4b7f43512cb99d35e43bb8305b6615fa396a62bce5b4a88d29df4bc3ef5c94
    role: target
  - path: data/natural_products/terpenoids/compound-6.yaml
    sha256: 4db168bf9a510a55403f4087abc00f8eee30b59a886a13a49daa8322eaa3b5cd
    role: context
  - path: data/natural_products/terpenoids/compound-8-2.yaml
    sha256: 68403d95a9ea9be2728367fae51a04a8bccd310a91f1cf91c2fe25deca39ed99
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 373f049029be3db137e062ff5f872a2400a9d5b423f3e108ea44ebde2f8dcc7d
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
    sha256: 90420425c90529cc99b474cb38cfedc7209c0e825b851f105f418868575a0a61
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
  - path: reviews/evidence/20261014-compound5/inputs/BGC0002162.3.json
    sha256: 17f8488be3cf75c5a9fae986807e4992baba4a87de667e341511bac23b5e3836
    role: context
  - path: reviews/evidence/20261014-compound5/inputs/DS027698.1-region.xml
    sha256: 4af3eaffbe0d6236d308d3cea830a87e19d369a5fc6fd666513eac87a9abcf95
    role: context
  - path: reviews/evidence/20261014-compound5/inputs/taxonomy.xml
    sha256: 352215cbdbbfd5452d090254cd890ca7f181cb8fa47c0d476ec623140b5a82de
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
  - path: scripts/extract_pubchem_bioassay.py
    sha256: 24f9d794e7cf97c420351cb751f8767f7d81a5f22aed01669b2318d6755e7c00
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/run_qc.py
    sha256: ff44ed3e40a9b3582eb84e38a81301745ae80d16445756d09a7efb2a480b1abb
    role: context
  - path: scripts/seed_from_sources.py
    sha256: c7531c2ff57eb55174c1c358c8bdbd507b25f4446d20e163f9b60b1161e48415
    role: context
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
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
targets:
- target_id: naturalproductmech:mibig-fd2940acc4
  path: data/natural_products/terpenoids/compound-6-2.yaml
  label: compound 6
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned source identity and producer/locus assertion
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and compound-index mapping
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Admission, classification, evidence grading and generated emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Source-pinned exact-locus evidence withdrawal when justified
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Exact-source producer strain context only where supported
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Identity-to-path pin; no direct filename changes
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/terpenoids/compound-6-2.yaml
    role: Curator-owned discussions only through validated writer and appended event
scope:
  description: One complete owner including all declared scientific fields and history;
    no external graph references.
  selection: Next exact owner in the3115-record campaign checkpoint priority, not
    name-only lookup or representative sampling. The one-record denominator is distinct
    from the overall campaign denominator.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-fd2940acc4
  exclusions:
  - target: All other corpus owners
    reason: Separate immutable per-record assessments are required; no extrapolation.
checks:
- check_id: prepare
  name: prepare
  status: passed
  required: true
  command: uv run python /private/tmp/npmech-numbered-review-rKbZU4/prepare.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: All3115 owner hashes,243 component hashes and87 prior bundles match the
    checkpoint; exact one-target inspect captured current inputs.
  scope_note: 2026-10-14T06:21:31.560142Z..2026-10-14T06:21:50.133782Z; /private/tmp/npmech-numbered-review-rKbZU4/prepare.log;
    SHA256 b57929d1cb4be0400904f9e112e9e4b9b31d603e9ebdac820e1c503e4308e87e
- check_id: strict
  name: strict
  status: passed
  required: true
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/compound-8.yaml
    data/natural_products/terpenoids/compound-8-2.yaml data/natural_products/terpenoids/compound-6-2.yaml
    data/natural_products/terpenoids/compound-6.yaml --out /private/tmp/npmech-numbered-review-rKbZU4/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: Documented strict validator checked all four selected owners; zero errors.
  scope_note: 2026-10-14T06:23:43.851068Z..2026-10-14T06:23:51.445542Z; /private/tmp/npmech-numbered-review-rKbZU4/strict.log;
    SHA256 061a743ffc094120c86a777136629177524d9216ef756872e59926204174f70e
- check_id: sources-project-path
  name: sources-project-path
  status: passed
  required: true
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/src:/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-numbered-review-rKbZU4/inspect_sources.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: Pinned RDKit, structured inventory joins, source members, accession versions,
    taxon ranks and deposited loci checked.
  scope_note: 2026-10-14T06:25:43.556886Z..2026-10-14T06:25:49.020910Z; /private/tmp/npmech-numbered-review-rKbZU4/sources-project-path.log;
    SHA256 30b8246d511f4d0f1140f5e824d25b3f5963cb82cf7526cbe7ad83c2a1a0bca8
- check_id: local-search
  name: local-search
  status: passed
  required: true
  command: rg --no-ignore --hidden -l -g '!.git/**' -g '!.venv/**' -g '!pages/**'
    -g '!data/embeddings/**' 'BGC0002162|BGC0002290|naturalproductmech:mibig-007406ddf9|naturalproductmech:mibig-dd802af1dd|naturalproductmech:mibig-fd2940acc4|naturalproductmech:mibig-c9721b757b|HHJKLMAAAQXSLU|HNLYCKPDQJMNHD|FAUJQEJMUWYQEX|LMSXLLMHAAGBSJ'
    .
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: Ignored/hidden-inclusive search recorded exact scope; no missing-input
    inference from default ignore behavior.
  scope_note: 2026-10-14T06:22:30.350473Z..2026-10-14T06:22:30.594925Z; /private/tmp/npmech-numbered-review-rKbZU4/local-search.log;
    SHA256 788c1176197944fe3f3e2dceda119c1b022ebd11530886db5ad9ddb0e1343ae4
- check_id: queue
  name: queue
  status: passed
  required: true
  command: just review-queue --tsv /private/tmp/npmech-numbered-review-rKbZU4/review-queue.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: Full documented pending-record queue regenerated into temporary workspace;
    no native status changes.
  scope_note: 2026-10-14T06:26:23.499700Z..2026-10-14T06:28:03.667439Z; /private/tmp/npmech-numbered-review-rKbZU4/queue.log;
    SHA256 ca4d0e64fbe0fe991226f9fc89998d4931daccae98e094ffa3cfc196e1429130
- check_id: labels
  name: labels
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: Full-corpus label gate passed with499 non-blocking mismatches and4647 configured
    adapter skips; not a claim that every pair was independently verified.
  scope_note: 2026-10-14T06:24:39.112548Z..2026-10-14T06:28:34.079989Z; /private/tmp/npmech-numbered-review-rKbZU4/labels.log;
    SHA256 3a35478c0f50d04f173e629252d86cf81839ab6d9d291ca88a9631d93d0cca64
- check_id: qc
  name: qc
  status: passed
  required: true
  command: just qc
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: Authoritative full-corpus QC completed on unchanged scientific inputs;
    not proof of experimental correctness.
  scope_note: 2026-10-14T06:21:43.538432Z..2026-10-14T06:58:49.953099Z; /private/tmp/npmech-numbered-review-rKbZU4/qc.log;
    SHA256 1a1208d0f7253ac83660c1d662961f27fbab0dcedeb6ce347c6b5b2d27d7beb2
- check_id: primary-exact-product
  name: Primary exact-product closure
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: 2015 main text remains denied from prior403; previously retrieved public
    SI was inspected. Exact-numbered cation characterization and complete stereochemical
    mapping remain unverified.
- check_id: imodulondb-applicability
  name: Structured expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  evidence_ids:
  - adapter
  summary: No matching native fungal dataset among28 adapter entries; not negative
    biological evidence.
- check_id: sources
  name: sources
  status: failed
  required: false
  command: uv run python /private/tmp/npmech-numbered-review-rKbZU4/inspect_sources.py
  exit_code: 1
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: Initial supplemental analysis could not import RDKit from project environment;
    superseded by sources-project-path.
  scope_note: 2026-10-14T06:24:36.244600Z..2026-10-14T06:24:36.572050Z; /private/tmp/npmech-numbered-review-rKbZU4/sources.log;
    SHA256 a9c31b415f0af98c356683c3447166152178c52d3e9d08a4a22491aecb3f6802
- check_id: sources-chemistry
  name: sources-chemistry
  status: failed
  required: false
  command: uv run --with rdkit==2026.3.5 python /private/tmp/npmech-numbered-review-rKbZU4/inspect_sources.py
  exit_code: 1
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: Ephemeral pinned wheel resolution failed for x86_64 macOS; no dependency
    or lock change; superseded by existing isolated pinned runtime.
  scope_note: 2026-10-14T06:24:52.595986Z..2026-10-14T06:24:52.911856Z; /private/tmp/npmech-numbered-review-rKbZU4/sources-chemistry.log;
    SHA256 15dff4b81d3f7abb10c89061d96c2e0a8b3ed4e22b91430794d7d7d37f52deae
- check_id: sources-verified
  name: sources-verified
  status: failed
  required: false
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-numbered-review-rKbZU4/inspect_sources.py
  exit_code: 1
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  summary: First isolated-runtime invocation omitted project src from PYTHONPATH;
    superseded by corrected explicit path.
  scope_note: 2026-10-14T06:25:02.351230Z..2026-10-14T06:25:03.633766Z; /private/tmp/npmech-numbered-review-rKbZU4/sources-verified.log;
    SHA256 6cffc4489d8243866ae0c55927946d02d31899bf978f0ebfc9b01c8ae8fc5d22
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/terpenoids/compound-6-2.yaml
  locator: Entire owner and identical read_natural_product view at 22ced0a503edd1d04628f7cfbdbb14ee1d03047c
  accessed_at: '2026-10-14T07:00:33.354266Z'
  support: supports
  snapshot_sha256: ff4b7f43512cb99d35e43bb8305b6615fa396a62bce5b4a88d29df4bc3ef5c94
  summary: 'Complete YAML read: exact structure, pinned computed filing, one MIBiG
    producer and locus, source concept, minted rationale, needs-a-name discussion
    and both history events. No graph refs, inline graph, pathway, occurrence, assay,
    target, xref or cross-corpus link is declared.'
- evidence_id: chemistry
  kind: validation
  reference: reviews/evidence/20261014-numbered-products/source-analysis.json
  locator: compound-6-2; pinned RDKit 2026.03.5
  accessed_at: '2026-10-14T07:00:33.354705Z'
  support: supports
  snapshot_sha256: 1c7f521223d88c8039d8083a85309473291fd7bde59649fe1330ddaecb5cf0b3
  summary: SMILES reproduces the exact Standard InChI and key FAUJQEJMUWYQEX-PNWBJGBJSA-N;
    formula C25H41+, charge 1, exact mass 341.320277732 Da, ring sizes [5, 15]. Atom
    stereocenters [[3, 'R'], [6, 'R'], [8, 'S']] agree with stereo_complete=True.
    Internal consistency does not validate experimental identity.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: BGC0002162:3; full parsed-row SHA256 36baacd0d1cc26fc65bf1d6d2dba84d27f3cc96b583357ba0f3bbdfa0dc9392f
  accessed_at: '2026-10-14T07:00:33.355099Z'
  support: supports
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
  summary: One exact-key MIBiG row and one pinned NPClassifier row per owner. Full
    parsed inventories contain no exact-key ChEBI structure, LOTUS, assay, BindingDB
    or sibling-link match. ChEBI origins were joined through matching ChEBI structure
    IDs, not an absent InChIKey column. These bounded local joins are not claims of
    global registry absence.
- evidence_id: local-search
  kind: search
  reference: reviews/evidence/20261014-numbered-products/local-search.log
  locator: Search command and output hash retained under local-search.receipt.json
    in the packet checks files
  accessed_at: '2026-10-14T06:22:30.594925Z'
  support: context_only
  snapshot_sha256: 788c1176197944fe3f3e2dceda119c1b022ebd11530886db5ad9ddb0e1343ae4
  search_scope: Ignored/hidden-inclusive repository search by both BGCs, all four
    exact IDs and key prefixes; excluded .git, .venv, generated pages and embeddings.
    Separate ignored-inclusive structured-review/curation exact-ID scan had no match
    before saving.
  summary: No earlier canonical review target or applicable curation decision found
    for these exact owners. Same generic labels denote different structures and must
    not be merged; neighboring compound5 reviews are context, not review coverage
    for these targets.
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:331117
  locator: Exact Taxon, ScientificName, Rank, OtherNames and Lineage elements
  accessed_at: '2026-10-14T06:22:30.133225Z'
  summary: NCBI confirms Aspergillus fischeri NRRL181 at strain rank (Neosartorya
    synonym) and Biscogniauxia sp. at species rank; both descend from Fungi. Taxonomic
    identity and fungal faceting are not proof of compound production.
  support: supports
  snapshot_sha256: cfb7e58790784f123698cb131f22da8b6d00c517c50b00844ae45d3f4f53d8d2
- evidence_id: adapter
  kind: database
  reference: reviews/evidence/20261014-numbered-products/imodulondb.log
  locator: All 28 returned dataset rows
  accessed_at: '2026-10-14T06:22:57.245757Z'
  support: context_only
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  summary: Structured iModulonDB inventory contains no Aspergillus/Neosartorya or
    Biscogniauxia dataset. It is not applicable; E.coli expression hosts and unrelated
    taxa do not supply native-fungus evidence.
- evidence_id: bounded-search
  kind: search
  reference: Web search, 2026-10-14 UTC
  locator: Exact quoted first InChIKey blocks for all four owners
  accessed_at: '2026-10-14T07:00:33.367223Z'
  support: context_only
  search_scope: Queries "HHJKLMAAAQXSLU", "LMSXLLMHAAGBSJ", "HNLYCKPDQJMNHD", "FAUJQEJMUWYQEX"
    returned no results. BGC, DOI and producer searches were used separately. No search
    snippet is treated as exact-product evidence.
  summary: Bounded exact-key searches did not resolve names or independent experimental
    identities; this is not a universal absence claim.
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002162.3/annotations.json
  locator: Version3 compounds index3, taxonomy and loci; committed response reread
    locally
  accessed_at: '2026-10-14T07:00:33.367264Z'
  support: partial
  snapshot_sha256: 17f8488be3cf75c5a9fae986807e4992baba4a87de667e341511bac23b5e3836
  summary: Active source repeats this exact charged encoding, assigns compound-level
    NMR with DOI10.1021/jacs.5b08319, and locus-level heterologous expression. The
    database assertion is not independent confirmation that this cation was isolated
    or directly characterized.
- evidence_id: primary-abstract
  kind: primary_source
  reference: DOI:10.1021/jacs.5b08319
  locator: PubmedArticle PMID26332841; public abstract and bibliographic identifiers
    only
  accessed_at: '2026-10-14T06:22:44.631121Z'
  summary: The study reports heterologous sesterfisherol production and oxidation
    to sesterfisheric acid; isotope experiments inform a proposed cyclization mechanism
    involving cationic intermediates. The abstract does not show isolation or NMR
    of this exact cation.
  support: partial
  snapshot_sha256: 787ad110b9a47765710baf68a346985344332b4fbb9eed15870b6f04d864d817
- evidence_id: primary-si
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/3765199
  locator: 'DOI10.1021/jacs.5b08319 supporting information: complete pagesS1-S3 text,
    S12 SchemeS2 pixels, TOC and S5-S10 captions inspected; prior retrieval predates
    publisher denial'
  accessed_at: '2026-10-14T07:00:33.368052Z'
  support: partial
  snapshot_sha256: a516f771e00606c1437d2846f8f0b040a18ae73ee5c73809967cd619a71dce10
  summary: SchemeS2 explicitly presents proposed carbocation mechanisms, including
    ent-6, not an isolation experiment. S2 names genomic-DNA donor JMC1740 (literal
    spelling), and S5-S10 describe neutral end-product spectroscopy or enzyme assays.
    Exact 2015 main-text numbering and complete stereochemical crosswalk remain unavailable;
    no NMR spectrum is reassigned to cation6 or8.
- evidence_id: strain-catalogue
  kind: authority
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_keyword?AN=Neosartorya&BN=fischeri&CN=fischeri&DN=
  locator: JCM1740 entry, deposit history and equivalent culture numbers; not the
    distinct JCM22241 entry
  accessed_at: '2026-10-14T06:36:43.812726Z'
  summary: The collection explicitly equates JCM1740 with NRRL181 and CBS544.65. Interpreting
    the SI spelling JMC1740 as JCM1740 is a stated typographic inference; no evidence
    supports a different strain. Culture equivalence does not prove production of
    either charged compound.
  support: supports
  snapshot_sha256: 49a9483bf9cd9685368c5063560ba8344279146503b40b6116518a1682f77814
- evidence_id: later-primary
  kind: primary_source
  reference: https://www.nature.com/articles/s41598-018-20916-x
  locator: Abstract; Results, Computed Mechanisms and Selectivity; Site-Directed Mutagenesis;
    Discussion; Methods. Earlier full text read; figure-page request and a later main-page
    recheck failed at inaccessible identity-provider redirects. No alternate retrieval.
  accessed_at: '2026-10-14T07:00:33.421835Z'
  support: partial
  summary: 'The 2018 study distinguishes calculated cations from isolated F191A-mutant
    products: the latter are neutral C25H40 hydrocarbons, not these C25H41+ records.
    It does not establish either stored cation as a directly demonstrated product.
    Numbered intermediates across publications must not be equated without an atom-level
    crosswalk.'
- evidence_id: locus
  kind: database
  reference: genbank:DS027698.1
  locator: Committed 2485363..2490827 slice,5465bp; source and two CDS annotations
  accessed_at: '2026-10-14T07:00:33.421864Z'
  support: supports
  snapshot_sha256: 4af3eaffbe0d6236d308d3cea830a87e19d369a5fc6fd666513eac87a9abcf95
  summary: The slice is NRRL181/taxon331117 and contains NFIA_055490/EAW16200.1 and
    NFIA_055500/EAW16201.1. Coordinates resolve, but a genomic deposit cannot prove
    the charged product. Culture equivalence is separately supported by the JCM catalogue.
    No new protein grounding was asserted.
assessments:
- assessment_id: identity
  area: identity
  outcome: supported
  topic: Exact local owner and source-row identity
  summary: Resolved by exact path, identifier, InChIKey and one-based MIBiG compound
    index, not the generic name. The internal structure and source member agree. No
    equivalence with the other compound6/8 owner is inferred.
  evidence_ids:
  - owner
  - chemistry
  - inventory
  - mibig
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
- assessment_id: experimental-identity
  area: identity
  outcome: concern
  topic: Experimental identity and numbered-material context
  summary: The charged C25 species is consistent with a proposed mechanistic intermediate,
    while the source grades its locus as experimentally demonstrated and annotates
    NMR. Direct exact-cation characterization has not been established. Primary main-text
    numbering, strain and stereochemical mapping require adjudication.
  evidence_ids:
  - chemistry
  - mibig
  - primary-abstract
  - primary-si
  - later-primary
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
- assessment_id: stereo
  area: consistency
  outcome: supported
  topic: Stereochemical encoding, not experimental assignment
  summary: Stored stereo_complete=True is consistent with the 0 undefined atom centers.
    Neither completion nor absence of undefined centers establishes source-derived
    stereochemistry.
  evidence_ids:
  - chemistry
  - mibig
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
- assessment_id: grounding
  area: grounding
  outcome: supported
  topic: Minted identity within the pinned corpus
  summary: No exact key exists in the complete pinned ChEBI structure inventory, supporting
    the local minted rationale. No global claim about current ChEBI or other registries
    is made; no replacement identifier was established.
  evidence_ids:
  - inventory
  - bounded-search
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
- assessment_id: classification
  area: representation
  outcome: supported
  topic: Separate filing, BGC and taxonomy axes
  summary: Pinned NPClassifier output and PATHS filing agree and remain explicitly
    computed. The Diterpenoids superclass is not an experimentally asserted molecular
    class; carbon count is25. No reclassification or directory move follows from this
    review. The source BGC class and fungal lineage are retained on separate axes.
  evidence_ids:
  - inventory
  - chemistry
  - mibig
  - taxonomy
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
- assessment_id: producer
  area: scope
  outcome: unknown
  topic: Native taxon versus experimental host
  summary: SOURCE_ASSERTION remains a faithful database grade, not proof of native
    biosynthesis. NRRL181 resolves as a strain and the JCM catalogue equates it with
    JCM1740; treating the SI spelling JMC1740 as a transposition is an explicit inference,
    not a strain-mismatch finding. Heterologous expression does not prove native production
    of a modeled cation.
  evidence_ids:
  - owner
  - taxonomy
  - locus
  - primary-abstract
  - primary-si
  - strain-catalogue
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  dimensions:
  - name: evidence-tier
    value: SOURCE_ASSERTION
    definition: Native producer assertion; distinct from the locus grade
    evidence_ids:
    - owner
  - name: locus-evidence-tier
    value: CLUSTER_DEMONSTRATED
    definition: Database-derived exact-product claim requiring primary scope verification
    evidence_ids:
    - owner
    - mibig
- assessment_id: locus
  area: evidence
  outcome: concern
  topic: Compound-specific scope of BGC evidence
  summary: Heterologous end-product synthesis and a proposed mechanistic cation must
    not be collapsed into direct demonstration of that cation. BGC coordinates and
    database provenance resolve, but the exact-product experiment does not.
  evidence_ids:
  - mibig
  - locus
  - primary-abstract
  - primary-si
  - later-primary
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
- assessment_id: optional-claims
  area: completeness
  outcome: not_applicable
  topic: No optional claims inferred from neighboring products
  summary: Owner has no occurrence, activity, molecular target, clinical assertion,
    cross-corpus link or pathway/graph. Complete local joins did not supply exact-key
    evidence for those surfaces. Activities or mechanisms of neutral sesterfisherol,
    biscognienyneB or similarly numbered compounds are not transferable. Empty optional
    fields are not evidence of biological absence.
  evidence_ids:
  - owner
  - inventory
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
- assessment_id: history
  area: provenance
  outcome: supported
  topic: Scientific status, discussions and maintained ownership
  summary: Both seed history events and needs-a-name discussion are preserved. The
    label task is already explicit; do not invent a synonym. Native SEEDED status
    is appropriate because experimental identity and origin have not passed sign-off.
    No scientific input was changed.
  evidence_ids:
  - owner
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
findings:
- finding_id: cation-evidence-scope
  issue_key: bgc0002162-compound6-cation-evidence-scope
  category: scope
  severity: major
  status: open
  certainty: provisional
  title: Proposed cation versus demonstrated product remains unqualified
  description: The owner encodes C25H41+ with 5/15 rings and an explicit carbon-centered
    positive charge. Its CLUSTER_DEMONSTRATED link is inherited from locus-level heterologous
    expression. Inspected primary material distinguishes proposed cationic mechanisms
    from isolated neutral products; the MIBiG NMR attribution has not been traced
    to a spectrum or experimental characterization of this exact charged structure.
    Qualify the exact-product evidence and adjudicate its record-versus-pathway-intermediate
    role. This is not a claim that carbocations cannot occur biologically or that
    all charged metabolites should be excluded. Main-text access and exact stereochemical/numbering
    closure remain missing, so no definitive deletion or replacement is asserted.
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  field_paths:
  - biosynthesis_origin
  - biosynthetic_gene_clusters[0].link_evidence_basis
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - chemical_structure
  - discussions
  evidence_ids:
  - owner
  - chemistry
  - mibig
  - primary-abstract
  - primary-si
  - later-primary
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned source identity and producer/locus assertion
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and compound-index mapping
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Admission, classification, evidence grading and generated emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Source-pinned exact-locus evidence withdrawal when justified
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Exact-source producer strain context only where supported
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Identity-to-path pin; no direct filename changes
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/terpenoids/compound-6-2.yaml
    role: Curator-owned discussions only through validated writer and appended event
  rule_id: review-checklist:exact-compound-bgc-support
  native_severity: major
  normalization_reason: Material evidence-scope inflation is major; unavailable main-text
    identity closure prevents a confirmed wrong-identity blocker.
actions:
- action_id: primary-closure
  target_ids:
  - naturalproductmech:mibig-fd2940acc4
  finding_ids:
  - cation-evidence-scope
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned source identity and producer/locus assertion
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and compound-index mapping
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Admission, classification, evidence grading and generated emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Source-pinned exact-locus evidence withdrawal when justified
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Exact-source producer strain context only where supported
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Identity-to-path pin; no direct filename changes
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/terpenoids/compound-6-2.yaml
    role: Curator-owned discussions only through validated writer and appended event
  description: Obtain legitimate access to the2015 main text; crosswalk each charged
    depiction and experimental claim. Retain proposed intermediates as explicitly
    proposed graph nodes where appropriate, and correct/qualify the exact-product
    locus grade only after primary adjudication. Do not silently substitute neutral
    sesterfisherol or bulk-exclude charged structures. A supported admission/exclusion
    change needs an implemented, tested source-owned mechanism; curation/decisions.tsv
    is reserved and ineffective.
  generator: Guarded exact-record canary via scripts/seed_from_sources.py only after
    separately authorized maintained-input correction
  acceptance_checks:
  - Map the exact structure, charge, stereochemistry and compound number to an inspected
    primary figure/table or spectrum.
  - Separate native producer, donor-locus strain and experimental host; grade only
    the experiment on this exact form.
  - Preserve upstream provenance, reviewed neighbors and all unrelated owner/component
    hashes.
  - For authorized curation use validated writer plus event; run strict validation,
    reproduction, corpus, label and full QC gates.
  - Save a new linked review with the same issue key before retiring any finding.
limitations:
- Partial scientific observation, not a completed review or native REVIEWED promotion.
  All three missing/failed supplemental setup attempts are retained; corrected analysis
  succeeded.
- Only this exact owner is assessed; sibling labels, neighboring compounds and the
  rest of3115-record corpus are not covered by this report.
- The portable evidence packet at reviews/evidence/20261014-numbered-products retains
  bounded source payloads and command receipts. Temporary paths in receipts describe
  original execution, not replay dependencies. Articles, SI and abstracts are reference-only,
  not redistributed.
- Search misses are bounded; local exhaustive inventory joins and ignored-inclusive
  file searches are distinct from global evidence absence.
- No direct reanalysis of raw experimental spectral data, no new graph/protein claim,
  no source refresh and no paid retrieval. Publication and issue tracking are separately
  user-authorized; native scientific inputs remain unchanged.
- 2015 main-text denial remains respected. The2018 main text was inspected as separate
  research; its figure page redirected to an inaccessible identity-provider endpoint,
  so pixels were not inspected and no alternate figure retrieval was attempted.
- S12 ent-6 is contextual evidence about a proposed scaffold; an exact stereochemical
  crosswalk to the stored cation is not asserted. The2018 mutant products and their
  numbering are not substituted for2015 compounds.
```
