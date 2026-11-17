# 17-hydroxy-8-desmethoxy-isomigrastatin: exact identity and native causal evidence

- Review: 20261021T071318Z-17-hydroxy-8-desmethoxy-isomigrastatin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T07:07:34.732534Z
- Finished UTC: 2026-10-21T07:13:18.739665Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact structure, five stereocentres, three alkene geometries, NPAtlas xref, minted grounding and both occurrences are supported. The exact target is compound 13 in the cited native knockout/complementation study, so BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED are justified. No actionable defect was found within the complete record scope; the original stereochemical assignment and source-access limits remain explicit.

## Scope And Provenance

One complete generated owner and resolved mechanism, with every asserted field group assessed against local provenance and accessible primary evidence.

Selection: Eighth unreviewed path in deterministic order from the initial validated list: 91 bundles covered 54 of 3,116 records and 3,062 remained. Ignored bundles were included in coverage counting. This bundle assesses one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-c995bb8923 | data/natural_products/alkaloids/17-hydroxy-8-desmethoxy-isomigrastatin.yaml | generated | 17-hydroxy-8-desmethoxy-isomigrastatin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and component validation | passed | True | naturalproductmech:mibig-c995bb8923 | One complete owner validated with zero ERROR rows. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-c995bb8923 | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-c995bb8923 | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-c995bb8923 | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-c995bb8923 | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Initial QC attempt before installing the pinned linter | failed | False | naturalproductmech:mibig-c995bb8923 | The first full QC invocation stopped at lint because the isolated copied Python environment lacked Ruff. Exact uv.lock version Ruff 0.16.6 was subsequently installed and lint passed on later invocations. |
| QC attempt without network access | failed | False | naturalproductmech:mibig-c995bb8923 | After Ruff installation, QC passed lint and stopped at vendored-sync because sandbox DNS could not reach the pinned public CLAW governance source. Approved network access allowed the next invocation to verify all 22 governed artifacts. |
| QC attempt before restoring the required provenance tag | failed | False | naturalproductmech:mibig-c995bb8923 | QC passed lint, vendored sync, documentation, provenance and source queue, then stopped at tests: 998 passed, 1 failed, 4 skipped. The sole failure was the isolated clone lacking refs/tags/review-base/gentamicin-20261013; it was not a failed archive-content assertion. The tag was subsequently fetched from origin. |
| Targeted verification after restoring the provenance tag | passed | False | naturalproductmech:mibig-c995bb8923 | After restoring the required tag, the exact previously failed gentamicin archive test passed (1 passed). No repository content was edited for this remediation. |
| Diagnosis of the suite skip conditions | passed | False | naturalproductmech:mibig-c995bb8923 | The four observed skip cases were reproduced with pytest skip reasons enabled: the optional sibling AntibioticMech comparison has no sibling checkout in the isolated clone, and three command-frontmatter tests have empty parameter sets. This diagnostic invocation executed no passing tests; it reported four skips. |
| Full repository quality gate after environment repair | passed | True | naturalproductmech:mibig-c995bb8923 | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Exact structure, both occurrences and native causal evidence | passed | True | naturalproductmech:mibig-c995bb8923 | Both original official occurrence supplements, independent configuration mapping and complete primary knockout/complementation manuscript support the exact desmethoxy target. The distinct desmethyl comparator is excluded. |
| Both occurrence organism provenance identifiers | passed | True | naturalproductmech:mibig-c995bb8923 | Official API identifiers resolve to the recorded species and NCBI taxa. |
| Expression-module source applicability | not_applicable | False | naturalproductmech:mibig-c995bb8923 | No expression-module or regulatory assertion is used; direct chemical and genetic experiments support the owner. |

## Scientific And Domain Assessments

### Exact C8-desmethoxy and C17-hydroxy congener

identity: supported. Targets: naturalproductmech:mibig-c995bb8923.

The owner encodes the named C26H37NO7 congener, with five assigned centres and three E alkenes. The complete encoding agrees with NPAtlas and current ChEBI. It is distinct from the C8-desmethyl congener, which retains an additional hydroxyl.

### NPAtlas exact full-structure equivalence

identity: supported. Targets: naturalproductmech:mibig-c995bb8923.

NPA013831 matches the full stereochemical InChI/key. No chemical-equivalence defect was found.

### Minted identity follows the eligible ChEBI rule

grounding: supported. Targets: naturalproductmech:mibig-c995bb8923.

The current exact candidate CHEBI:208682 is two-star and the pinned eligible inventory contains no matching connectivity row. Retaining MINTED follows repository policy.

### Published configuration maps to the complete stored graph

evidence: supported. Targets: naturalproductmech:mibig-c995bb8923.

The original structure drawing and stereochemical discussion map to C9R/C10S/C11R/C14S/C17R, with three E alkenes, reproducing the exact owner key. The assignment rests on the authors' comparative NMR and biosynthetic correlation, including C17 comparison to streptimidone; it is not presented as a direct absolute-configuration experiment on this isolated compound.

### Both exact compound–organism occurrence pairs

evidence: supported. Targets: naturalproductmech:mibig-c995bb8923.

Both original official supplements directly report isolation and identification of the exact compound from the listed species and specified strains. The 2005 compound 19 and 2007 compound 3 are explicitly bridged by spectroscopic and rotation comparison. Neither occurrence depends solely on a paper title or a family-level statement.

### Isolated macrocyclic congener versus rearranged products

evidence: supported. Targets: naturalproductmech:mibig-c995bb8923.

The exact macrocyclic target is among the isolated fermentation congeners and is distinguished from later water-mediated laboratory rearrangement products. These primary observations support its culture-derived natural-product origin. Whether the specific recorded locus and producer evidence grades are justified is assessed separately against the causal experiments.

### Computed chemical filing and generated history

provenance: supported. Targets: naturalproductmech:mibig-c995bb8923.

The exact-key NPClassifier inventory agrees with the recorded Alkaloids/Lysine alkaloids/Piperidine alkaloids classes and pinned model version. The separate source PKS class addresses biosynthetic categorization. SEEDED and its three seed events do not claim scientific review.

### Complete resolved optional assertions

scope: not_applicable. Targets: naturalproductmech:mibig-c995bb8923.

The complete owner and resolved view have no optional mechanisms, targets, assays, clinical or cross-record assertions to audit. Their absence alone is not a defect.

### Exact desmethoxy congener and strain/locus mapping

grounding: supported. Targets: naturalproductmech:mibig-c995bb8923.

The owner graph and source row correspond to primary compound 13, not the distinct desmethyl comparator 18. S. amphibiosporus taxon 221586, the experimentally used ATCC 53964 culture and GQ274954.1 map consistently. PKS class and omitted unspecified numerical bounds are faithful.

### Compound-specific native knockout and complementation evidence

evidence: supported. Targets: naturalproductmech:mibig-c995bb8923.

The exact target 13 is lost after native ltmE/ltmH disruption and after ltmK deletion, then restored by ltmK complementation. Retain BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED with the existing PMID:25405956 citation. These grades are supported by the recorded native locus, independently of the separate occurrence assertions.

### Biological formation and alternative producer context

evidence: supported. Targets: naturalproductmech:mibig-c995bb8923.

The exact target is a native ltm-dependent minor metabolite and also a nascent mgs-pathway product reported from S. platensis. It is distinct from the prior record’s nonenzymatic shunt compound. NATURAL_PRODUCT is consistent with the inspected biological evidence; occurrence in a second producer does not relocate the recorded ltm locus.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-IDENTITY-LOCAL | data/natural_products/alkaloids/17-hydroxy-8-desmethoxy-isomigrastatin.yaml; Complete owner; label, chemical_structure, xrefs and grounding_notes | supports | The owner represents the 17-hydroxy, C8-desmethoxy iso-migrastatin congener, with full key IVFXTQLBVDABOI-DVYWRAFASA-N, five assigned centres and three specified alkenes. It has NPA013831 as its sole chemical xref and retains a minted identifier. |
| E-NPATLAS | https://www.npatlas.org/api/v1/compound/NPA013831?include=classifications; original_name, smiles, inchi, inchikey, origin_reference and reassignments | supports | NPA013831 names 17-hydroxy-8-desmethoxy-isomigrastatin and exactly matches the record full InChI and key. Its origin reference is DOI 10.1021/ja053118u, PMID 16117518, and reassignments is empty. |
| E-CHEBI-IDENTITY | https://www.ebi.ac.uk/chebi/backend/api/public/compound/208682/; name, stars and default_structure id3381225 | supports | CHEBI:208682 names the exact target and its default structure matches the complete InChI/key. It has two stars, so it does not meet the automatic three-star grounding threshold. |
| E-CHEMISTRY-IDENTITY | /private/tmp/npm-review-work/008/chemistry.json; RDKit 2026.03.5 result generated 2026-10-21T07:07:35.735270Z; complete result inspected | supports | The SMILES regenerates the exact stored InChI/key, neutral formula C26H37NO7 and exact mass 475.257002524. Assigned centres are zero-based atoms 1:S, 5:R, 16:R, 18:S and 23:R; none is unassigned. |
| E-GROUNDING-SEARCH | data/raw/chebi_structures.tsv; Complete pinned eligible inventory; connectivity prefix and exact chemical-name stem | supports | No row matching IVFXTQLBVDABOI or 17-hydroxy-8-desmethoxy was found in the pinned eligible ChEBI inventory. The current exact candidate is two-star. |
| E-GROUNDING-POLICY | docs/HARMONIZATION.md; Unambiguous three-star ChEBI default-structure rule | supports | Automatic ChEBI grounding requires an unambiguous matching three-star default structure. |
| E-PRIMARY-IDENTITY | https://api.figshare.com/v2/file/download/5108431; DOI 10.1021/ja053118u supporting information S3–S5, STables 2/3, SFigure 2 compound 19 on S21 | supports | The original SI explicitly names compound 19 as 17-hydroxy-8-desmethoxy-isomigrastatin and gives its MS, optical rotation and NMR assignments. SFigure 2 shows the C8 methylene and C17 hydroxyl, distinguishing it from C8-desmethyl congeners that retain a C8 oxygen. S4–S5 assign shared stereochemistry by biosynthetic origin and comparative NMR; C17R is assigned by NMR comparison with previously established streptimidone. These are the authors' stated grounds, not a new direct crystal determination of compound 19. |
| E-PRIMARY-EQUIVALENCE | https://api.figshare.com/v2/file/download/4669732; DOI 10.1021/ol702249g supporting information S4, paragraph immediately before Physicochemical properties | supports | The authors identify their isolated compound 3 by identical MS, proton/carbon NMR and optical rotation to 17-hydroxy-8-desmethoxy-isomigrastatin from the earlier study. The explicit name and comparative-data statement establish the exact compound bridge despite an inconsistent subsequent property heading. |
| E-STEREO-MAPPING | /private/tmp/npm-review-work/008/stereo-mapping.json; Original SI SFigure 2 compound 19 independently transcribed; C11 from explicit S4 assignment | supports | All five owner tetrahedral tags were removed. Primary wedges map natural C9, C10, C14 and C17 to atoms 16:R, 18:S, 1:S and 23:R, while explicit C11R maps to atom 5. The regenerated complete InChI/key matches the owner. C2=C3, C6=C7 and C12=C13 are E. The C9 CIP label is R because loss of C8 oxygen changes priorities; it is spatially consistent with the authors' shared-configuration assignment. |
| R-LOCAL | data/natural_products/alkaloids/17-hydroxy-8-desmethoxy-isomigrastatin.yaml; Entire owner, read_natural_product resolved view and exact-key inventory rows | supports | The complete owner has one MIBiG source, two LOTUS occurrences, one NPAtlas xref, producer and locus claims and explicitly computed NPClassifier classes. It retains SEEDED and three seed events. No optional pathway, molecular target, bioactivity, clinical, related-record or causal graph assertions occur in the complete resolved view. |
| R-SI-2005 | https://api.figshare.com/v2/file/download/5108431; S1 strain and fermentation; S2–S3 isolation and exact compound 19 identification; DOI:10.1021/ja053118u.s001 | supports | The original supplement identifies this exact congener as compound 19, isolated in 45 mg from Streptomyces platensis NRRL 18993 fermentation. Its named structure has reported MS, NMR and optical rotation data. Resin-assisted isolation preserves the macrocycle; later laboratory rearrangements are separately described and concern other numbered products. This directly supports the listed exact occurrence. |
| R-SI-2007 | https://api.figshare.com/v2/file/download/4669732; S3–S4 wild-type resin fermentation, isolation of compound 3 and exact identification; DOI:10.1021/ol702249g.s002 | supports | The original supplement reports 103 mg of compound 3 isolated from wild-type Streptomyces amphibiosporus ATCC 53964. It explicitly matches compound 3 to 17-hydroxy-8-desmethoxy-isomigrastatin by mass spectra, proton/carbon NMR and optical rotation. The exact occurrence is supported; the nearby laboratory rearrangement methods are separate experiments. |
| R-WIKIDATA-PLATENSIS | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q26291839&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Q26291839 English label, P225 scientific name and P685 NCBI taxonomy identifier | supports | Previously inspected official API identifies Q26291839 as Streptomyces platensis, NCBI Taxonomy 58346. Exact reuse applicability was checked against the first occurrence of this owner; organism identity does not establish compound evidence. |
| R-WIKIDATA-AMPHIBIOSPORUS | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q104096108&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Q104096108 English label and P225/P685 claims | supports | The official public API identifies Streptomyces amphibiosporus and NCBI Taxonomy 221586, matching the second occurrence taxon and provenance URI. |
| bgc-v5-source | https://mibig.secondarymetabolites.org/repository/BGC0000083.5/annotations.json; compounds[3], loci[0], taxonomy, biosynthesis and legacy_references | supports | The complete version-5 entry lists the matching exact 17-hydroxy-8-desmethoxy-isomigrastatin structure as compound index 4, source locus GQ274954.1, S. amphibiosporus taxon 221586, PKS/Type I and Knock-out studies. Source references include PMID:25405956 and PMID:17997563. Empty numeric bounds correctly preserve the source’s unspecified 0/0 bounds; status is active, quality questionable, completeness complete. |
| bgc-gq274954 | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=GQ274954.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text; LOCUS, DEFINITION, VERSION, source feature and CDS features | supports | The 50,543 bp complete lactimidomycin cluster is explicitly from S. amphibiosporus strain ATCC 53964, culture collection ATCC:53964, taxon 221586. It encodes LtmE, LtmH and LtmK among the ltm genes. The primary manuscript independently names GQ274954 as its deposited ltm sequence, supplying the exact accession/strain bridge. |
| bgc-primary-exact-congener | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=4270375&amp;retmode=xml; PMID:25405956 / DOI:10.1021/bi501396v, Introduction paragraph on the three LTM congeners; Figure 1; structural discussion of compounds 16 and 18 | supports | The full primary manuscript explicitly identifies 8,9-dihydro-9R-hydroxy-LTM (13) as identical to 17R-hydroxy-8-desmethoxy-iso-MGS (13). It reports isolation from both named producer cultures. The target graph lacks C8 oxygen and has C9/C17 hydroxyls, consistent with 13. The cytotoxicity comparator 18 is the distinct 8-desmethyl congener with an additional C8 hydroxyl; its assay-only role must not be transferred to this target. |
| bgc-primary-knockout-exact13 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=4270375&amp;retmode=xml; Materials and Methods: wild-type/recombinant fermentation and HPLC; Results: ltmE/ltmH inactivation and ltmK inactivation/complementation; Figure 2B; GenBank accession statement | supports | Authentic standards identify metabolites 13-15 by HPLC. Native ltmE and ltmH disruptions abolish 13 as well as LTM and the other minor congeners. ltmK deletion also loses 13, while ltmK complementation restores it. The paper connects the experiments to ATCC 53964 and GQ274954. This is exact-target native causal evidence, supporting both the producer and locus grades rather than merely a family or comparator association. |
| bgc-local-supported-grades | data/raw/mibig_compounds.tsv; data/natural_products/alkaloids/17-hydroxy-8-desmethoxy-isomigrastatin.yaml; conf/producer_evidence.tsv; MIBiG source row 113 / BGC0000083:4; full target; Knock-out studies grading rule | supports | The exact source row inherits Knock-out studies and ENTRY citation PMID:25405956, which generate BGC_CHARACTERIZED producer and CLUSTER_DEMONSTRATED locus. For this exact congener the inspected primary experiments justify both grades. No exact-target override was found in the inspected evidence, reference and strain tables. |

## Limits And Additional Notes

- This identity review verifies the published assignment and graph equivalence. It does not independently reinterpret raw NMR spectra or claim that the isolated target itself underwent X-ray absolute-configuration determination.
- The primary S4 phrase same configuration describes spatial configuration. Removing the C8 oxygen changes the target C9 CIP label to R, so copying the parent compound's C9S text literally would create an incorrect epimer.
- The ChEBI check covers the complete pinned eligible inventory and the identified current exact candidate, not every current ontology entry.
- Direct ACS main-article endpoints returned 403. Both original official supporting-information PDFs were available and their full isolation methods and exact-compound passages were read. This occurrence review does not independently reanalyse raw spectra.
- Direct PMC browser access returned a challenge, but the complete official primary XML was retrieved and inspected.
- The primary article contains inconsistent mutant strain numbering between its abstract and main text and occasional ATCC 53694 spellings. Conclusions here are keyed to the named disrupted genes; the Genome Scanning and Sequence Analysis methods, accession statement and GenBank deposit explicitly establish ATCC 53964. No cross-strain claim is inferred from typographical variants.
- Exact drawing/stereochemistry and original occurrence supplements are independently assessed by the identity/root reviewers; the BGC conclusion additionally uses the primary paper’s explicit equivalence between its two names for compound 13.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- No scientific owner, source inventory, component, native status or seed history was edited. A positive saved review does not itself promote native status to REVIEWED.
- The desmethoxy target is distinguished from the desmethyl comparator despite similar names. No optional activity or mechanism field is required merely because the source paper reports additional experiments.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T071318Z-17-hydroxy-8-desmethoxy-isomigrastatin
kind: record
repository: CultureBotAI/NaturalProductMech
title: '17-hydroxy-8-desmethoxy-isomigrastatin: exact identity and native causal evidence'
started_at: '2026-10-21T07:07:34.732534Z'
finished_at: '2026-10-21T07:13:18.739665Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Exact structure, five stereocentres, three alkene geometries, NPAtlas xref,
  minted grounding and both occurrences are supported. The exact target is compound
  13 in the cited native knockout/complementation study, so BGC_CHARACTERIZED and
  CLUSTER_DEMONSTRATED are justified. No actionable defect was found within the complete
  record scope; the original stereochemical assignment and source-access limits remain
  explicit.
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
  - path: data/natural_products/alkaloids/17-hydroxy-8-desmethoxy-isomigrastatin.yaml
    sha256: 9b4110a46af0c08dc3a0721fdbcccf54a12bc2d1550a2f37b9ad99bb5b6cfab3
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
  description: One complete generated owner and resolved mechanism, with every asserted
    field group assessed against local provenance and accessible primary evidence.
  selection: 'Eighth unreviewed path in deterministic order from the initial validated
    list: 91 bundles covered 54 of 3,116 records and 3,062 remained. Ignored bundles
    were included in coverage counting. This bundle assesses one target.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-c995bb8923
targets:
- target_id: naturalproductmech:mibig-c995bb8923
  path: data/natural_products/alkaloids/17-hydroxy-8-desmethoxy-isomigrastatin.yaml
  label: 17-hydroxy-8-desmethoxy-isomigrastatin
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
    role: CyanoMetDB exact structure occurrence source
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated owner transform
checks:
- check_id: C-STRICT
  name: Closed-schema and component validation
  status: passed
  required: true
  summary: One complete owner validated with zero ERROR rows.
  command: just validate-strict data/natural_products/alkaloids/17-hydroxy-8-desmethoxy-isomigrastatin.yaml
    --out /private/tmp/npm-review-work/008/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-c995bb8923
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned
    filing pathways.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016808Z; finished 2026-10-21T06:37:52.997020Z. Exact
    session transcript: /private/tmp/npm-native-checks/verify-corpus.log.'
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3,116 records are byte-identical to the seeder output from committed
    inventories and maintained curation inputs.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-reproduction
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016703Z; finished 2026-10-21T06:38:35.570687Z. Exact
    session transcript: /private/tmp/npm-native-checks/verify-reproduction.log.'
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The documented exhaustive queue command produced 8,928 diagnostic rows
    in 12 queues; deterministic queue output does not establish scientific review.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just review-queue
    --tsv /private/tmp/npm-review-queue-initial.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016598Z; finished 2026-10-21T06:37:11.018366Z. Exact
    session transcript: /private/tmp/npm-native-checks/review-queue.log.'
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'Full configured gate passed using existing CHEBI and GO caches plus the
    committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35
    documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because
    their prefixes have no adapter.'
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.498212Z; finished 2026-10-21T06:38:54.776253Z. Exact
    session transcript: /private/tmp/npm-native-checks/validate-products.log.'
- check_id: qc-environment-attempt1
  name: Initial QC attempt before installing the pinned linter
  status: failed
  required: false
  summary: The first full QC invocation stopped at lint because the isolated copied
    Python environment lacked Ruff. Exact uv.lock version Ruff 0.16.6 was subsequently
    installed and lint passed on later invocations.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.497107Z; finished 2026-10-21T06:36:56.918133Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc.log.'
- check_id: qc-network-attempt2
  name: QC attempt without network access
  status: failed
  required: false
  summary: After Ruff installation, QC passed lint and stopped at vendored-sync because
    sandbox DNS could not reach the pinned public CLAW governance source. Approved
    network access allowed the next invocation to verify all 22 governed artifacts.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:37:57.661447Z; finished 2026-10-21T06:37:59.874785Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt2.log.'
- check_id: qc-tag-attempt3
  name: QC attempt before restoring the required provenance tag
  status: failed
  required: false
  summary: 'QC passed lint, vendored sync, documentation, provenance and source queue,
    then stopped at tests: 998 passed, 1 failed, 4 skipped. The sole failure was the
    isolated clone lacking refs/tags/review-base/gentamicin-20261013; it was not a
    failed archive-content assertion. The tag was subsequently fetched from origin.'
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:38:17.713062Z; finished 2026-10-21T06:45:43.079802Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt3.log.'
- check_id: qc-tag-remediation
  name: Targeted verification after restoring the provenance tag
  status: passed
  required: false
  summary: After restoring the required tag, the exact previously failed gentamicin
    archive test passed (1 passed). No repository content was edited for this remediation.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just test -q
    tests/test_gentamicin_review_archive.py::test_gentamicin_archive_and_scoped_dispositions
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:45:52.383490Z; finished 2026-10-21T06:45:54.030116Z. Exact
    session transcript: /private/tmp/npm-native-checks/gentamicin-tag-check.log.'
- check_id: qc-skip-diagnosis
  name: Diagnosis of the suite skip conditions
  status: passed
  required: false
  summary: 'The four observed skip cases were reproduced with pytest skip reasons
    enabled: the optional sibling AntibioticMech comparison has no sibling checkout
    in the isolated clone, and three command-frontmatter tests have empty parameter
    sets. This diagnostic invocation executed no passing tests; it reported four skips.'
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just test -q
    -rs tests/test_schema.py::test_shared_mech_modules_are_byte_identical_to_the_fleet
    tests/test_skill_frontmatter.py::test_command_frontmatter_has_no_duplicate_keys
    tests/test_skill_frontmatter.py::test_command_frontmatter_is_valid_yaml tests/test_skill_frontmatter.py::test_command_declares_a_usable_description
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:30.259937Z; finished 2026-10-21T06:46:31.251048Z. Exact
    session transcript: /private/tmp/npm-native-checks/skipped-tests-diagnosis.log.'
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
  - naturalproductmech:mibig-c995bb8923
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:02.058886Z; finished 2026-10-21T06:54:53.950582Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt4.log.'
- check_id: C-PRIMARY-EXACT
  name: Exact structure, both occurrences and native causal evidence
  status: passed
  required: true
  summary: Both original official occurrence supplements, independent configuration
    mapping and complete primary knockout/complementation manuscript support the exact
    desmethoxy target. The distinct desmethyl comparator is excluded.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - R-SI-2005
  - R-SI-2007
  - E-STEREO-MAPPING
  - bgc-primary-knockout-exact13
- check_id: C-PROVENANCE-URI
  name: Both occurrence organism provenance identifiers
  status: passed
  required: true
  summary: Official API identifiers resolve to the recorded species and NCBI taxa.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - R-WIKIDATA-PLATENSIS
  - R-WIKIDATA-AMPHIBIOSPORUS
- check_id: C-IMODULON
  name: Expression-module source applicability
  status: not_applicable
  required: false
  summary: No expression-module or regulatory assertion is used; direct chemical and
    genetic experiments support the owner.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
evidence:
- evidence_id: E-IDENTITY-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/17-hydroxy-8-desmethoxy-isomigrastatin.yaml
  locator: Complete owner; label, chemical_structure, xrefs and grounding_notes
  accessed_at: '2026-10-21T07:10:27Z'
  support: supports
  summary: The owner represents the 17-hydroxy, C8-desmethoxy iso-migrastatin congener,
    with full key IVFXTQLBVDABOI-DVYWRAFASA-N, five assigned centres and three specified
    alkenes. It has NPA013831 as its sole chemical xref and retains a minted identifier.
  snapshot_sha256: 9b4110a46af0c08dc3a0721fdbcccf54a12bc2d1550a2f37b9ad99bb5b6cfab3
- evidence_id: E-NPATLAS
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA013831?include=classifications
  locator: original_name, smiles, inchi, inchikey, origin_reference and reassignments
  accessed_at: '2026-10-21T07:10:41Z'
  support: supports
  summary: NPA013831 names 17-hydroxy-8-desmethoxy-isomigrastatin and exactly matches
    the record full InChI and key. Its origin reference is DOI 10.1021/ja053118u,
    PMID 16117518, and reassignments is empty.
  snapshot_sha256: 326fe5c713e7116cc9809086f46afbe4d7f296efeb07647fcf5300a2dd05cb66
- evidence_id: E-CHEBI-IDENTITY
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/208682/
  locator: name, stars and default_structure id3381225
  accessed_at: '2026-10-21T07:10:41Z'
  support: supports
  summary: CHEBI:208682 names the exact target and its default structure matches the
    complete InChI/key. It has two stars, so it does not meet the automatic three-star
    grounding threshold.
  snapshot_sha256: e707c508e1744c8c3dff32dd6fa58efc9051d2949084683d9e66a1c92696bf60
- evidence_id: E-CHEMISTRY-IDENTITY
  kind: validation
  reference: /private/tmp/npm-review-work/008/chemistry.json
  locator: RDKit 2026.03.5 result generated 2026-10-21T07:07:35.735270Z; complete
    result inspected
  accessed_at: '2026-10-21T07:10:27Z'
  support: supports
  summary: The SMILES regenerates the exact stored InChI/key, neutral formula C26H37NO7
    and exact mass 475.257002524. Assigned centres are zero-based atoms 1:S, 5:R,
    16:R, 18:S and 23:R; none is unassigned.
  snapshot_sha256: b2e2b6ca410b4b15033bc554a78b6b555878e963eff1f6ed8a051fe963a332b9
- evidence_id: E-GROUNDING-SEARCH
  kind: search
  reference: data/raw/chebi_structures.tsv
  locator: Complete pinned eligible inventory; connectivity prefix and exact chemical-name
    stem
  accessed_at: '2026-10-21T07:10:41Z'
  support: supports
  summary: No row matching IVFXTQLBVDABOI or 17-hydroxy-8-desmethoxy was found in
    the pinned eligible ChEBI inventory. The current exact candidate is two-star.
  search_scope: Searched the entire explicitly named inventory with rg --no-ignore
    --hidden for IVFXTQLBVDABOI and 17-hydroxy-8-desmethoxy. Ignored files were included;
    no matching row was returned.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: E-GROUNDING-POLICY
  kind: authority
  reference: docs/HARMONIZATION.md
  locator: Unambiguous three-star ChEBI default-structure rule
  accessed_at: '2026-10-21T06:45:28Z'
  support: supports
  summary: Automatic ChEBI grounding requires an unambiguous matching three-star default
    structure.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: E-PRIMARY-IDENTITY
  kind: primary_source
  reference: https://api.figshare.com/v2/file/download/5108431
  locator: DOI 10.1021/ja053118u supporting information S3–S5, STables 2/3, SFigure
    2 compound 19 on S21
  accessed_at: '2026-10-21T07:08:48.840392Z'
  support: supports
  summary: The original SI explicitly names compound 19 as 17-hydroxy-8-desmethoxy-isomigrastatin
    and gives its MS, optical rotation and NMR assignments. SFigure 2 shows the C8
    methylene and C17 hydroxyl, distinguishing it from C8-desmethyl congeners that
    retain a C8 oxygen. S4–S5 assign shared stereochemistry by biosynthetic origin
    and comparative NMR; C17R is assigned by NMR comparison with previously established
    streptimidone. These are the authors' stated grounds, not a new direct crystal
    determination of compound 19.
  snapshot_sha256: 603ed1d6b03418ff4a1f4d01cd4fc96a6a846585f04ef756825dd9a553f804be
- evidence_id: E-PRIMARY-EQUIVALENCE
  kind: primary_source
  reference: https://api.figshare.com/v2/file/download/4669732
  locator: DOI 10.1021/ol702249g supporting information S4, paragraph immediately
    before Physicochemical properties
  accessed_at: '2026-10-21T07:08:48.840277Z'
  support: supports
  summary: The authors identify their isolated compound 3 by identical MS, proton/carbon
    NMR and optical rotation to 17-hydroxy-8-desmethoxy-isomigrastatin from the earlier
    study. The explicit name and comparative-data statement establish the exact compound
    bridge despite an inconsistent subsequent property heading.
  snapshot_sha256: 85759ea4f1c8fdbe81b4b9d8777236164e34aa0a2302abcfa4596773fb2d4d46
- evidence_id: E-STEREO-MAPPING
  kind: validation
  reference: /private/tmp/npm-review-work/008/stereo-mapping.json
  locator: Original SI SFigure 2 compound 19 independently transcribed; C11 from explicit
    S4 assignment
  accessed_at: '2026-10-21T07:11:36.863480Z'
  support: supports
  summary: All five owner tetrahedral tags were removed. Primary wedges map natural
    C9, C10, C14 and C17 to atoms 16:R, 18:S, 1:S and 23:R, while explicit C11R maps
    to atom 5. The regenerated complete InChI/key matches the owner. C2=C3, C6=C7
    and C12=C13 are E. The C9 CIP label is R because loss of C8 oxygen changes priorities;
    it is spatially consistent with the authors' shared-configuration assignment.
  snapshot_sha256: 6e04d5281cca87e65bfd445e4847809225a865297e40131b3ce1bf480a175b3c
- evidence_id: R-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/17-hydroxy-8-desmethoxy-isomigrastatin.yaml
  locator: Entire owner, read_natural_product resolved view and exact-key inventory
    rows
  accessed_at: '2026-10-21T07:09:54.590463Z'
  support: supports
  summary: The complete owner has one MIBiG source, two LOTUS occurrences, one NPAtlas
    xref, producer and locus claims and explicitly computed NPClassifier classes.
    It retains SEEDED and three seed events. No optional pathway, molecular target,
    bioactivity, clinical, related-record or causal graph assertions occur in the
    complete resolved view.
  snapshot_sha256: 9b4110a46af0c08dc3a0721fdbcccf54a12bc2d1550a2f37b9ad99bb5b6cfab3
- evidence_id: R-SI-2005
  kind: primary_source
  reference: https://api.figshare.com/v2/file/download/5108431
  locator: S1 strain and fermentation; S2–S3 isolation and exact compound 19 identification;
    DOI:10.1021/ja053118u.s001
  accessed_at: '2026-10-21T07:08:48.840392Z'
  support: supports
  summary: The original supplement identifies this exact congener as compound 19,
    isolated in 45 mg from Streptomyces platensis NRRL 18993 fermentation. Its named
    structure has reported MS, NMR and optical rotation data. Resin-assisted isolation
    preserves the macrocycle; later laboratory rearrangements are separately described
    and concern other numbered products. This directly supports the listed exact occurrence.
  snapshot_sha256: 603ed1d6b03418ff4a1f4d01cd4fc96a6a846585f04ef756825dd9a553f804be
- evidence_id: R-SI-2007
  kind: primary_source
  reference: https://api.figshare.com/v2/file/download/4669732
  locator: S3–S4 wild-type resin fermentation, isolation of compound 3 and exact identification;
    DOI:10.1021/ol702249g.s002
  accessed_at: '2026-10-21T07:08:48.840277Z'
  support: supports
  summary: The original supplement reports 103 mg of compound 3 isolated from wild-type
    Streptomyces amphibiosporus ATCC 53964. It explicitly matches compound 3 to 17-hydroxy-8-desmethoxy-isomigrastatin
    by mass spectra, proton/carbon NMR and optical rotation. The exact occurrence
    is supported; the nearby laboratory rearrangement methods are separate experiments.
  snapshot_sha256: 85759ea4f1c8fdbe81b4b9d8777236164e34aa0a2302abcfa4596773fb2d4d46
- evidence_id: R-WIKIDATA-PLATENSIS
  kind: database
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q26291839&props=labels%7Cclaims&languages=en&format=json
  locator: Q26291839 English label, P225 scientific name and P685 NCBI taxonomy identifier
  accessed_at: '2026-10-21T07:06:23.339657Z'
  support: supports
  summary: Previously inspected official API identifies Q26291839 as Streptomyces
    platensis, NCBI Taxonomy 58346. Exact reuse applicability was checked against
    the first occurrence of this owner; organism identity does not establish compound
    evidence.
  snapshot_sha256: 6540a304eb8b2aa1c20bc3241ff2636b6971aae7cacfb21442fe250c681c705f
- evidence_id: R-WIKIDATA-AMPHIBIOSPORUS
  kind: database
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q104096108&props=labels%7Cclaims&languages=en&format=json
  locator: Q104096108 English label and P225/P685 claims
  accessed_at: '2026-10-21T07:07:51.920428Z'
  support: supports
  summary: The official public API identifies Streptomyces amphibiosporus and NCBI
    Taxonomy 221586, matching the second occurrence taxon and provenance URI.
  snapshot_sha256: ccb5ec59dd7548ac88c1ad0b63af9c348e692098325264735079a69dbe16a855
- evidence_id: bgc-v5-source
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000083.5/annotations.json
  locator: compounds[3], loci[0], taxonomy, biosynthesis and legacy_references
  accessed_at: '2026-10-21T07:09:55Z'
  support: supports
  summary: The complete version-5 entry lists the matching exact 17-hydroxy-8-desmethoxy-isomigrastatin
    structure as compound index 4, source locus GQ274954.1, S. amphibiosporus taxon
    221586, PKS/Type I and Knock-out studies. Source references include PMID:25405956
    and PMID:17997563. Empty numeric bounds correctly preserve the source’s unspecified
    0/0 bounds; status is active, quality questionable, completeness complete.
- evidence_id: bgc-gq274954
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=GQ274954.1&db=nuccore&report=genbank&retmode=text
  locator: LOCUS, DEFINITION, VERSION, source feature and CDS features
  accessed_at: '2026-10-21T07:10:18Z'
  support: supports
  summary: The 50,543 bp complete lactimidomycin cluster is explicitly from S. amphibiosporus
    strain ATCC 53964, culture collection ATCC:53964, taxon 221586. It encodes LtmE,
    LtmH and LtmK among the ltm genes. The primary manuscript independently names
    GQ274954 as its deposited ltm sequence, supplying the exact accession/strain bridge.
- evidence_id: bgc-primary-exact-congener
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=4270375&retmode=xml
  locator: PMID:25405956 / DOI:10.1021/bi501396v, Introduction paragraph on the three
    LTM congeners; Figure 1; structural discussion of compounds 16 and 18
  accessed_at: '2026-10-21T07:10:17Z'
  support: supports
  summary: The full primary manuscript explicitly identifies 8,9-dihydro-9R-hydroxy-LTM
    (13) as identical to 17R-hydroxy-8-desmethoxy-iso-MGS (13). It reports isolation
    from both named producer cultures. The target graph lacks C8 oxygen and has C9/C17
    hydroxyls, consistent with 13. The cytotoxicity comparator 18 is the distinct
    8-desmethyl congener with an additional C8 hydroxyl; its assay-only role must
    not be transferred to this target.
- evidence_id: bgc-primary-knockout-exact13
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=4270375&retmode=xml
  locator: 'Materials and Methods: wild-type/recombinant fermentation and HPLC; Results:
    ltmE/ltmH inactivation and ltmK inactivation/complementation; Figure 2B; GenBank
    accession statement'
  accessed_at: '2026-10-21T07:10:17Z'
  support: supports
  summary: Authentic standards identify metabolites 13-15 by HPLC. Native ltmE and
    ltmH disruptions abolish 13 as well as LTM and the other minor congeners. ltmK
    deletion also loses 13, while ltmK complementation restores it. The paper connects
    the experiments to ATCC 53964 and GQ274954. This is exact-target native causal
    evidence, supporting both the producer and locus grades rather than merely a family
    or comparator association.
- evidence_id: bgc-local-supported-grades
  kind: record_content
  reference: data/raw/mibig_compounds.tsv; data/natural_products/alkaloids/17-hydroxy-8-desmethoxy-isomigrastatin.yaml;
    conf/producer_evidence.tsv
  locator: MIBiG source row 113 / BGC0000083:4; full target; Knock-out studies grading
    rule
  accessed_at: '2026-10-21T07:10:56Z'
  support: supports
  summary: The exact source row inherits Knock-out studies and ENTRY citation PMID:25405956,
    which generate BGC_CHARACTERIZED producer and CLUSTER_DEMONSTRATED locus. For
    this exact congener the inspected primary experiments justify both grades. No
    exact-target override was found in the inspected evidence, reference and strain
    tables.
  search_scope: Full current record and exact-key raw source row read. Searches for
    the exact key, minted identifier and BGC compound key included ignored files in
    the scoped correction tables; no wider absence conclusion is made.
assessments:
- assessment_id: A-IDENTITY-REPRESENTATION
  area: identity
  topic: Exact C8-desmethoxy and C17-hydroxy congener
  outcome: supported
  summary: The owner encodes the named C26H37NO7 congener, with five assigned centres
    and three E alkenes. The complete encoding agrees with NPAtlas and current ChEBI.
    It is distinct from the C8-desmethyl congener, which retains an additional hydroxyl.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-NPATLAS
  - E-CHEBI-IDENTITY
  - E-CHEMISTRY-IDENTITY
  - E-PRIMARY-IDENTITY
- assessment_id: A-XREF-EQUIVALENCE
  area: identity
  topic: NPAtlas exact full-structure equivalence
  outcome: supported
  summary: NPA013831 matches the full stereochemical InChI/key. No chemical-equivalence
    defect was found.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-NPATLAS
- assessment_id: A-GROUNDING
  area: grounding
  topic: Minted identity follows the eligible ChEBI rule
  outcome: supported
  summary: The current exact candidate CHEBI:208682 is two-star and the pinned eligible
    inventory contains no matching connectivity row. Retaining MINTED follows repository
    policy.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-CHEBI-IDENTITY
  - E-GROUNDING-SEARCH
  - E-GROUNDING-POLICY
- assessment_id: A-PRIMARY-STEREOCHEMISTRY
  area: evidence
  topic: Published configuration maps to the complete stored graph
  outcome: supported
  summary: The original structure drawing and stereochemical discussion map to C9R/C10S/C11R/C14S/C17R,
    with three E alkenes, reproducing the exact owner key. The assignment rests on
    the authors' comparative NMR and biosynthetic correlation, including C17 comparison
    to streptimidone; it is not presented as a direct absolute-configuration experiment
    on this isolated compound.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - E-PRIMARY-IDENTITY
  - E-PRIMARY-EQUIVALENCE
  - E-STEREO-MAPPING
- assessment_id: R-OCCURRENCES
  area: evidence
  topic: Both exact compound–organism occurrence pairs
  outcome: supported
  summary: Both original official supplements directly report isolation and identification
    of the exact compound from the listed species and specified strains. The 2005
    compound 19 and 2007 compound 3 are explicitly bridged by spectroscopic and rotation
    comparison. Neither occurrence depends solely on a paper title or a family-level
    statement.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - R-LOCAL
  - R-SI-2005
  - R-SI-2007
  - R-WIKIDATA-PLATENSIS
  - R-WIKIDATA-AMPHIBIOSPORUS
  dimensions:
  - name: isolation_contexts
    value: 'S. platensis NRRL 18993: 2005 compound 19; S. amphibiosporus ATCC 53964:
      2007 compound 3'
    definition: Strain and original article numbering support the species-level occurrences,
      without asserting these strains are taxonomically interchangeable.
    evidence_ids:
    - R-SI-2005
    - R-SI-2007
- assessment_id: R-ORIGIN
  area: evidence
  topic: Isolated macrocyclic congener versus rearranged products
  outcome: supported
  summary: The exact macrocyclic target is among the isolated fermentation congeners
    and is distinguished from later water-mediated laboratory rearrangement products.
    These primary observations support its culture-derived natural-product origin.
    Whether the specific recorded locus and producer evidence grades are justified
    is assessed separately against the causal experiments.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - R-SI-2005
  - R-SI-2007
  - R-LOCAL
- assessment_id: R-CLASSIFICATION
  area: provenance
  topic: Computed chemical filing and generated history
  outcome: supported
  summary: The exact-key NPClassifier inventory agrees with the recorded Alkaloids/Lysine
    alkaloids/Piperidine alkaloids classes and pinned model version. The separate
    source PKS class addresses biosynthetic categorization. SEEDED and its three seed
    events do not claim scientific review.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - R-LOCAL
- assessment_id: R-OPTIONAL
  area: scope
  topic: Complete resolved optional assertions
  outcome: not_applicable
  summary: The complete owner and resolved view have no optional mechanisms, targets,
    assays, clinical or cross-record assertions to audit. Their absence alone is not
    a defect.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - R-LOCAL
- assessment_id: bgc-target-and-strain-supported
  area: grounding
  topic: Exact desmethoxy congener and strain/locus mapping
  outcome: supported
  summary: The owner graph and source row correspond to primary compound 13, not the
    distinct desmethyl comparator 18. S. amphibiosporus taxon 221586, the experimentally
    used ATCC 53964 culture and GQ274954.1 map consistently. PKS class and omitted
    unspecified numerical bounds are faithful.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - bgc-v5-source
  - bgc-gq274954
  - bgc-primary-exact-congener
- assessment_id: bgc-native-causal-grades-supported
  area: evidence
  topic: Compound-specific native knockout and complementation evidence
  outcome: supported
  summary: The exact target 13 is lost after native ltmE/ltmH disruption and after
    ltmK deletion, then restored by ltmK complementation. Retain BGC_CHARACTERIZED
    and CLUSTER_DEMONSTRATED with the existing PMID:25405956 citation. These grades
    are supported by the recorded native locus, independently of the separate occurrence
    assertions.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - bgc-primary-knockout-exact13
  - bgc-gq274954
  - bgc-local-supported-grades
- assessment_id: bgc-natural-formation-supported
  area: evidence
  topic: Biological formation and alternative producer context
  outcome: supported
  summary: The exact target is a native ltm-dependent minor metabolite and also a
    nascent mgs-pathway product reported from S. platensis. It is distinct from the
    prior record’s nonenzymatic shunt compound. NATURAL_PRODUCT is consistent with
    the inspected biological evidence; occurrence in a second producer does not relocate
    the recorded ltm locus.
  target_ids:
  - naturalproductmech:mibig-c995bb8923
  evidence_ids:
  - bgc-primary-exact-congener
  - bgc-primary-knockout-exact13
findings: []
actions: []
limitations:
- This identity review verifies the published assignment and graph equivalence. It
  does not independently reinterpret raw NMR spectra or claim that the isolated target
  itself underwent X-ray absolute-configuration determination.
- The primary S4 phrase same configuration describes spatial configuration. Removing
  the C8 oxygen changes the target C9 CIP label to R, so copying the parent compound's
  C9S text literally would create an incorrect epimer.
- The ChEBI check covers the complete pinned eligible inventory and the identified
  current exact candidate, not every current ontology entry.
- Direct ACS main-article endpoints returned 403. Both original official supporting-information
  PDFs were available and their full isolation methods and exact-compound passages
  were read. This occurrence review does not independently reanalyse raw spectra.
- Direct PMC browser access returned a challenge, but the complete official primary
  XML was retrieved and inspected.
- The primary article contains inconsistent mutant strain numbering between its abstract
  and main text and occasional ATCC 53694 spellings. Conclusions here are keyed to
  the named disrupted genes; the Genome Scanning and Sequence Analysis methods, accession
  statement and GenBank deposit explicitly establish ATCC 53964. No cross-strain claim
  is inferred from typographical variants.
- Exact drawing/stereochemistry and original occurrence supplements are independently
  assessed by the identity/root reviewers; the BGC conclusion additionally uses the
  primary paper’s explicit equivalence between its two names for compound 13.
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
- No scientific owner, source inventory, component, native status or seed history
  was edited. A positive saved review does not itself promote native status to REVIEWED.
- The desmethoxy target is distinguished from the desmethyl comparator despite similar
  names. No optional activity or mechanism field is required merely because the source
  paper reports additional experiments.
tags:
- path-order-campaign
- batch-001
- isomigrastatin
```
