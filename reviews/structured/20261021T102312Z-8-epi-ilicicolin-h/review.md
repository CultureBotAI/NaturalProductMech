# 8-epi-ilicicolin H: incomplete stereochemistry and unsupported source association

- Review: 20261021T102312Z-8-epi-ilicicolin-h
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T10:08:27.255647Z
- Finished UTC: 2026-10-21T10:23:12.693481Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The named epimer is encoded with one unresolved propenyl-bearing stereocentre, while the primary Icc study specifies that centre. The cited Neonectria DH2 work establishes ilicicolin H and J; exact 8-epi-ilicicolin H is demonstrated in a different donor-locus/heterologous-host system. Correcting chemistry and source claims therefore requires coordinated, guarded implementation. Existing method withdrawal and citation replacement cannot suppress the unsupported association. No scientific data was edited.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 33, batch 004, selected in path order from the fresh-main authoritative validated catalogue and the separately validated pending-PR targets. At selection, 84 of 3116 current records had campaign coverage and 3032 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-1cc1aa7754 | data/natural_products/alkaloids/8-epi-ilicicolin-h.yaml | generated | 8-epi-ilicicolin H |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-1cc1aa7754 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-1cc1aa7754 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-1cc1aa7754 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-1cc1aa7754 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-1cc1aa7754 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-1cc1aa7754 | The full documented just qc recipe passed against the new main revision. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Exact supported stereochemical resolution | failed | True | naturalproductmech:mibig-1cc1aa7754 | One stereocentre of the named fully specified product is absent from the source graph. |
| Exact-product producer and locus applicability | failed | True | naturalproductmech:mibig-1cc1aa7754 | The cited DH2/ili experiments demonstrate H/J, not this named epimer; the exact product is supported by another donor/host/locus experiment. |
| Applicable fungal expression dataset | not_applicable | False | naturalproductmech:mibig-1cc1aa7754 | No applicable fungal dataset appears in the complete retained catalogue. |

## Scientific And Domain Assessments

### Published exact epimer versus incomplete source graph

identity: concern. Targets: naturalproductmech:mibig-1cc1aa7754.

The current graph has one unresolved centre, explicitly flagged false, whereas the exact primary product is fully specified. The missing centre is the propenyl-bearing C9/C17, not epimer-defining C8. The full candidate graph requires a guarded identity migration and cannot be made an xref-equivalent of the broader key.

### Native donor, heterologous host and congener identity

scope: concern. Targets: naturalproductmech:mibig-1cc1aa7754.

DH2/ili evidence concerns H/J, while the exact epimer is demonstrated in A1145 expressing HXQ-H-1 icc genes. Correcting the citation alone would transfer evidence across donor taxa and loci. The current sole producer/locus association needs explicit suppression or replacement through an implemented source route.

### Biological formation of the fully specified candidate

evidence: supported. Targets: naturalproductmech:mibig-1cc1aa7754.

The JACS study supplies exact-product heterologous production and purified-enzyme conversion. This supports a biological route for the fully assigned candidate, while current source admission must be repaired without presenting donor-gene provenance as native occurrence.

### Source fidelity, taxonomy, filing and audit

provenance: supported. Targets: naturalproductmech:mibig-1cc1aa7754.

The current YAML faithfully reproduces its active source and partial stereo flag. Taxon and deposited-contig metadata resolve, computed filing is attributed and both seed events retain SEEDED. These deterministic and provenance positives coexist with the scientific identity/source defects.

### Unasserted optional activity and mechanisms

completeness: not_applicable. Targets: naturalproductmech:mibig-1cc1aa7754.

The owner makes no assay, enzyme or graph assertion. Optional content need not be added to fix the record. If later expanded, exact epimer assays and icc experiments must remain separate from parent H/J activity and proposed IliD chemistry.

## Findings

### R033-F-STEREO: The named epimer remains unresolved at one published stereocentre

blocker / open / confirmed; issue key: mibig-bgc0002035-compound3-incomplete-exact-stereochemistry.

The owner truthfully declares incomplete stereo, but its unspecified propenyl-bearing centre allows two different full structures. The primary JACS compound2 and official ChEBI MOL specify the exact 8-epi product. This is a resolution mismatch, not a false stereo_complete:true flag or a missing C8 assignment.

### R033-F-SOURCE: The cited DH2 study does not demonstrate this epimer

major / open / confirmed; issue key: mibig-bgc0002035-compound3-wrong-product-producer-locus.

PMID31216742 reports native and transferred DH2 ili production of ilicicolin H/J and cites the distinct HXQ-H-1 icc study for 8-epi-H. The imported native producer/locus pair therefore lacks exact-product support. Empty locus methods and SOURCE_ASSERTION accurately describe the database import but do not cure the misassociation. A simple citation replacement would conflate different loci and production hosts.

## Recommended Actions And Acceptance Checks

### R033-A-IDENTITY

Implement and test an explicit primary-source-backed exact-structure correction route for BGC0002035:3, pinning complete raw row fb39874b95050f740b756b4a04de6a25fa9b4b93c7116d9b2d04d57d53c796c0 and the inspected primary structure evidence. Independently confirm the five-centre candidate BYVVOONSAAQMKI-NMEWZTTESA-N and collision/migration scope. Existing REPLACE_WITH_CHEBI cannot accept two-star155888; do not promote its status or silently repair its API SMILES. Use the verified official MOL and primary drawing to inform a guarded source route. Coordinate this structural change with the source-claim action so that the corrected key does not inherit an unsupported DH2 producer/locus. Preserve original assertions as explicitly superseded provenance.

- The exact five-centre structure is independently confirmed against the original compound2 drawing, with C9/C17 distinguished from C8; SMILES/InChI/full key/stereo flag agree.
- A gitignore-independent full-key search and complete source-table comparison establish all collisions and affected owners before any migration; old and new keys are not asserted equivalent.
- The complete original source row and replacement chemistry/evidence are pinned; source or replacement drift fails closed. No unconsumed decisions.tsv entry or ineligible two-star ChEBI grounding is used.
- The structural and producer/locus corrections compose under explicit tested guards; no existing guard is bypassed by refreshing hashes.
- Canary output, migration/PATHS checks, strict validation, exact byte reproduction and repository QC pass before the correction is accepted.

### R033-A-SOURCE

Implement a source-pinned claim suppression/replacement path that prevents BGC0002035:3 from emitting unsupported DH2 production or ili-locus attribution for this epimer. Retain the original MIBiG row as historical source provenance. Re-establish the corrected exact product through an effective reproducible admission route anchored to PMID30905148: distinguish HXQ-H-1 donor genes, the deposited icc locus and FGSC A1145 heterologous production, with Enzymatic assays/Heterologous expression only where directly supported. Merely changing the source PMID or applying WITHDRAW is insufficient: WITHDRAW leaves the assertions present and existing methods are already empty. Treat any native-donor occurrence as unresolved unless separately evidenced.

- No DH2 producer or RQWH01000002.1 ili association remains asserted for the corrected epimer solely on PMID31216742; original source provenance remains inspectable.
- The exact corrected product has a valid reproducible biological-origin admission route and source evidence; do not leave an orphan record or infer membership from chemical resemblance.
- The donor organism, production host, native versus heterologous context and actual source locus are independently grounded and separately qualified; do not reuse BGC0002035 for the icc experiment.
- Keep H/J parent activities and proposed unassayed IliD chemistry off the epimer. Do not introduce native DH2 or native HXQ-H-1 production without exact-compound evidence.
- Composition tests cover source drift, structure correction, suppression, replacement, source provenance and corpus reproduction; run canary, strict, filing-integrity and full repository gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R033-OWNER | data/natural_products/alkaloids/8-epi-ilicicolin-h.yaml; Complete owner and resolved view, source concept and both seed events | supports | The named epimer has four assigned centres and one unspecified centre, correctly flagged stereo_complete:false. Its only imported producer/locus is Neonectria sp. DH2/BGC0002035, with SOURCE_ASSERTION and CLUSTER_UNSTATED; no occurrence, chemical xref, pathway, graph or activity claim is asserted. |
| R033-RAW | data/raw/mibig_compounds.tsv; Complete BGC0002035:3 version3 row | supports | The source contains the same incomplete stereochemical graph, Neonectria taxon1735992, RQWH01000002.1:1095186..1116947 and PMID31216742, with no locus methods. Canonical full-row SHA256 fb39874b95050f740b756b4a04de6a25fa9b4b93c7116d9b2d04d57d53c796c0. |
| R033-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0002035.3/annotations.json; Complete exact response inspected | supports | Version3 is active and lists parent H, J and 8-epi-H, with an empty locus method list. The owner copies compound3 faithfully. The sole source citation is PMID31216742; active database status does not establish exact-product support. |
| R033-CITED-MAIN | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6631495/fullTextXML; DOI10.3390/molecules24122267, PMID31216742; full main Introduction, Results, Methods, Conclusions and figure captions | supports | The full cited Molecules paper identifies native Neonectria DH2 parent ilicicolin H and heterologous A. nidulans production of H/J. It explicitly contrasts its results with the separate Penicillium variabile icc study that produced 8-epi-H. It reports no exact 8-epi-H production by DH2 or its transferred ili locus. Purified IliD was expressed but the absence of substrate prevented its enzymatic assay. |
| R033-CITED-SI | https://mdpi-res.com/d_attachment/molecules/molecules-24-02267/article_deploy/molecules-24-02267-s001.pdf; Complete 18-page publisher SI text, tables, captions and protein sequence text; no raw spectral reprocessing | supports | The complete supplement text, tables and captions concern H/J, recombinant plasmids, IliD expression, negative H↔J host-feeding tests and H/J spectra/assays. No exact 8-epi-H experimental product appears in this inspected supplement. Plasmid/gene labels differ among body, Figure3 and SI tables; these cannot be converted into verified exact recombinant genotype claims without reconciliation. |
| R033-CITED-FIG1 | https://mdpi-res.com/molecules/molecules-24-02267/article_deploy/html/images/molecules-24-02267-g001.png; Original full-resolution Figure1A pixels; Molecules atom numbering | supports | The original Figure1A depicts the named epimer as contextual third structure, without a product number. Its propenyl-bearing centre is left without a wedge, whereas its carbonyl-bearing C8 is shown opposite to parent H. This source drawing is consistent with the incomplete database encoding, but it is not a complete exact-epimer assignment. |
| R033-CITED-FIG3 | https://mdpi-res.com/molecules/molecules-24-02267/article_deploy/html/images/molecules-24-02267-g003.png; Original full-resolution Figure3A/B pixels | supports | The original chromatograms label products1 and2 as H and J, and show native DH2 and recombinant-host profiles. They do not label or authenticate target 8-epi-H. The gene labels are inconsistent with some prose/table labels and are not used to infer exact unsequenced constructs. |
| R033-JACS-MAIN | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=6585442&amp;retmode=xml; DOI10.1021/jacs.9b02204, PMID30905148; complete main Results and Discussion | supports | The independent icc study expresses genes from P. variabile HXQ-H-1 in A. nidulans A1145. IccA/B/C/D produce exact 8-epi-H compound2, characterized by NMR; IccE converts it to parent1. Purified C-His IccD converts acyclic4 to2 and N-His IccE converts2 to1. Native production by DH2 is not established by these donor/host experiments. |
| R033-JACS-SI | https://ndownloader.figshare.com/files/14703596; Official SI Methods S4–S7; original TableS6 S13 structure, NOESY drawing and NMR; exact source preparations and assay scope | supports | TableS6 specifies all five tetrahedral centres of compound2, including the propenyl-bearing carbon numbered C17 in this paper, corresponding to C9 in the Molecules drawing. HRMS and optical rotation accompany the NMR assignment. The donor strain is HXQ-H-1 and the production host is FGSC A1145. The exact target MIC40 µg/mL versus parent0.4 µg/mL cannot be replaced by H/J MIC6.3 µg/mL from the other study. |
| R033-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/155888/; Complete exact response inspected | supports | Released CHEBI155888 is two-star and cites PMID30905148 for the fully specified epimer, full key BYVVOONSAAQMKI-NMEWZTTESA-N. It is an identity corroboration lead, ineligible for the existing three-star grounding/replacement rule. Its API SMILES fails aromatic kekulization; the official MOL and InChI were checked separately rather than silently repairing that string. |
| R033-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/155888/; Complete exact response inspected | supports | The official connection table parses to five assigned centres and the full epimer key BYVVOONSAAQMKI-NMEWZTTESA-N. It agrees with the authority InChI and one completion of the owner missing centre. |
| R033-CHEMISTRY | /private/tmp/npm-review-work/033/identity/stereo-comparison.json; RDKit enumeration of the single unspecified owner centre; official MOL comparison retained separately | supports | The unspecified zero-based atom11 bears the propenyl group: Molecules C9/JACS C17. Its two completions give distinct keys NMEWZTTESA (S) and PVSUOEAJSA (R); the current CVCLIUOFSA key distinguishes neither. The epimer-defining carbonyl-bearing C8 is already assigned. The original incomplete graph is internally consistent and honestly flagged, but does not uniquely denote the fully assigned named product. |
| R033-TAXON | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1735992&amp;retmode=xml; Complete exact response inspected | supports | NCBI1735992 is Neonectria sp. DH2, assigned species rank under unclassified Neonectria. Correct taxonomy does not establish production of this particular epimer. |
| R033-GENOME | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=RQWH01000002.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text; Original GenBank header, complete source feature and contig length; unrelated sequence not experimentally reassessed | supports | RQWH01000002.1 is the 3,797,617-bp DH2 contig000001F, taxon1735992, BioProjectPRJNA507358/BioSampleSAMN10492166. Its source says strainDH2 isolated from Meconopsis grandis plant root. The stored locus interval lies inside the contig. This supports accession provenance but not exact target formation or a purified IliD assay. |
| R033-CLASS | data/raw/npclassifier.tsv; Complete exact-key pinned row | context_only | The owner preserves the versioned Alkaloids/Nicotinic acid alkaloids/Pyridine alkaloids prediction separately from source NRPS/PKS assertions. Filing consistency does not repair either exact stereochemistry or a wrong product-to-source association. |
| R033-LOADERS | src/naturalproductmech/curate/structure_corrections.py; Complete structure correction loader plus seeder source-claim emission and WITHDRAW branches | context_only | The existing structure correction accepts only a unique structured three-star ChEBI target and preserves source context. Two-star155888 is not accepted. WITHDRAW only removes method applicability and leaves producer/locus assertions; with no methods already present it cannot suppress this unsupported association. The seeder unconditionally emits a named MIBiG producer. Claim-reference and strain consumers reject incompatible structure corrections. A coordinated, tested source/structure correction route is needed. |
| R033-SEARCH | /private/tmp/npm-review-work/033/identity/local-search.txt; Ignored-inclusive exact target/key/slug search through corpus, maintained inputs, code and review evidence | context_only | The scoped search identifies the sole current target source and historical inventories. It does not establish an eligible current three-star exact replacement or an existing consumed correction for this target. Candidate full-key uniqueness must be independently checked before a structure-changing implementation. |
| R033-IMODULON | https://imodulondb.org/; Complete retained 28-dataset catalogue | context_only | No Neonectria, Penicillium variabile or A. nidulans dataset occurs in the inspected catalogue. No expression-module evidence is substituted for the actual donor/host experiments. |

## Limits And Additional Notes

- The complete cited Molecules body and supplement text were read, and main Figures1/3 were visually inspected. Raw NMR spectra, unrelated genome bases and complete recombinant construct sequences were not reanalysed.
- The JACS main body, relevant original SI methods and TableS6 structure/NOESY drawing were inspected. Primary absolute-configuration experiments were not repeated. The two papers use different atom numbering and have distinct products and strain contexts.
- The ChEBI candidate is two-star and its current API SMILES fails RDKit kekulization; the official connection table and InChI agree on the fully specified candidate. No authority status was altered and no invalid SMILES was silently repaired.
- The appropriate consumed structural/admission correction capability does not yet exist for this combined case. The actions describe concrete required implementation and validation, not an assertion that existing citation or method overlays alone perform it.
- The configured identifier-label gate accepts 499 warning-level mismatches and 35 explicit exceptions and skips 4,744 no-adapter pairs; exit 0 does not independently verify every identifier or scientific claim.
- The quality suite reports 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). Skipped tests are not counted as passing tests. Existing ontology caches were used; no multi-gigabyte cache download was required.
- Native gates assess deterministic consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy, or literature-level claim support.
- No scientific owner, inventory, curation table, native status or history was edited. Actions are proposed work.
- Shared baseline gates and target strict validation retain their actual fresh command receipts for this base. Scientific failed or unavailable checks are distinct from bundle validation.
- An independent reviewer checked the primary drawings, product scope and composed correction requirements; receipt /private/tmp/npm-review-work/033/root-packet-qa.json retains its actual review time and packet hash.

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
review_id: 20261021T102312Z-8-epi-ilicicolin-h
title: '8-epi-ilicicolin H: incomplete stereochemistry and unsupported source association'
started_at: '2026-10-21T10:08:27.255647Z'
finished_at: '2026-10-21T10:23:12.693481Z'
completion: completed
verdict: needs_curation
scientific_review: true
summary: The named epimer is encoded with one unresolved propenyl-bearing stereocentre,
  while the primary Icc study specifies that centre. The cited Neonectria DH2 work
  establishes ilicicolin H and J; exact 8-epi-ilicicolin H is demonstrated in a different
  donor-locus/heterologous-host system. Correcting chemistry and source claims therefore
  requires coordinated, guarded implementation. Existing method withdrawal and citation
  replacement cannot suppress the unsupported association. No scientific data was
  edited.
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
  - path: data/natural_products/alkaloids/8-epi-ilicicolin-h.yaml
    sha256: 7587f4884a204badc7996b016272879acd6ec1c35b4ec9ab6bd919ec6aa93973
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
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
    role: context
  - path: src/naturalproductmech/grading.py
    sha256: ece54c4a2c0803f034ac59de51b1006cf79ea8d6b6256d75757d4adb88ea9630
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 33, batch 004, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated pending-PR targets.
    At selection, 84 of 3116 current records had campaign coverage and 3032 remained.
    The population search included ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-1cc1aa7754
targets:
- target_id: naturalproductmech:mibig-1cc1aa7754
  path: data/natural_products/alkaloids/8-epi-ilicicolin-h.yaml
  label: 8-epi-ilicicolin H
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
  - naturalproductmech:mibig-1cc1aa7754
  command: just validate-strict data/natural_products/alkaloids/8-epi-ilicicolin-h.yaml
    --out /private/tmp/npm-review-work/033/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T10:08:30.687629Z
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
  scope_note: 'Fresh read-only execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055340+00:00;
    finished 2026-10-21T09:55:22.727768+00:00. Exact receipt: /private/tmp/npm-native-checks/batch-004/verify-corpus.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-corpus.log. No earlier
    baseline result is reused.'
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
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
  scope_note: 'Fresh read-only execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055361+00:00;
    finished 2026-10-21T09:56:44.050706+00:00. Exact receipt: /private/tmp/npm-native-checks/batch-004/verify-reproduction.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-reproduction.log.
    No earlier baseline result is reused.'
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
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
  scope_note: 'Fresh read-only execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.057401+00:00;
    finished 2026-10-21T09:54:38.468783+00:00. Exact receipt: /private/tmp/npm-native-checks/batch-004/review-queue.json;
    transcript: /private/tmp/npm-native-checks/batch-004/review-queue.log. No earlier
    baseline result is reused.'
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
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
  scope_note: 'Fresh read-only execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.061733+00:00;
    finished 2026-10-21T09:56:36.296159+00:00. Exact receipt: /private/tmp/npm-native-checks/batch-004/validate-products.json;
    transcript: /private/tmp/npm-native-checks/batch-004/validate-products.log. No
    earlier baseline result is reused.'
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
- check_id: shared-qc
  name: Full repository quality gate on the current main baseline
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed against the new main revision.
    Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured
    lint, governance, documentation, provenance, source-queue, schema, rendering,
    reproduction, filing-integrity and reporting stages completed successfully.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh read-only execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:30.560925+00:00;
    finished 2026-10-21T10:04:44.806799+00:00. Exact receipt: /private/tmp/npm-native-checks/batch-004/qc.json;
    transcript: /private/tmp/npm-native-checks/batch-004/qc.log. No earlier baseline
    result is reused.'
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
- check_id: R033-C-IDENTITY
  name: Exact supported stereochemical resolution
  status: failed
  required: true
  summary: One stereocentre of the named fully specified product is absent from the
    source graph.
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  evidence_ids:
  - R033-CHEMISTRY
  - R033-JACS-SI
  - R033-MOL
- check_id: R033-C-SOURCE
  name: Exact-product producer and locus applicability
  status: failed
  required: true
  summary: The cited DH2/ili experiments demonstrate H/J, not this named epimer; the
    exact product is supported by another donor/host/locus experiment.
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  evidence_ids:
  - R033-CITED-MAIN
  - R033-CITED-SI
  - R033-CITED-FIG3
  - R033-JACS-MAIN
- check_id: R033-C-IMODULON
  name: Applicable fungal expression dataset
  status: not_applicable
  required: false
  summary: No applicable fungal dataset appears in the complete retained catalogue.
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  evidence_ids:
  - R033-IMODULON
evidence:
- evidence_id: R033-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/8-epi-ilicicolin-h.yaml
  locator: Complete owner and resolved view, source concept and both seed events
  accessed_at: '2026-10-21T10:17:32.829814Z'
  support: supports
  summary: The named epimer has four assigned centres and one unspecified centre,
    correctly flagged stereo_complete:false. Its only imported producer/locus is Neonectria
    sp. DH2/BGC0002035, with SOURCE_ASSERTION and CLUSTER_UNSTATED; no occurrence,
    chemical xref, pathway, graph or activity claim is asserted.
  snapshot_sha256: 7587f4884a204badc7996b016272879acd6ec1c35b4ec9ab6bd919ec6aa93973
- evidence_id: R033-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: Complete BGC0002035:3 version3 row
  accessed_at: '2026-10-21T10:17:32.829814Z'
  support: supports
  summary: The source contains the same incomplete stereochemical graph, Neonectria
    taxon1735992, RQWH01000002.1:1095186..1116947 and PMID31216742, with no locus
    methods. Canonical full-row SHA256 fb39874b95050f740b756b4a04de6a25fa9b4b93c7116d9b2d04d57d53c796c0.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: R033-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002035.3/annotations.json
  locator: Complete exact response inspected
  accessed_at: '2026-10-21T10:09:10.781952Z'
  support: supports
  summary: Version3 is active and lists parent H, J and 8-epi-H, with an empty locus
    method list. The owner copies compound3 faithfully. The sole source citation is
    PMID31216742; active database status does not establish exact-product support.
  snapshot_sha256: 05ac8e4b43110e099e7619efec68da864fdd23a66a52c02a3443e7fb38abfe30
- evidence_id: R033-CITED-MAIN
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6631495/fullTextXML
  locator: DOI10.3390/molecules24122267, PMID31216742; full main Introduction, Results,
    Methods, Conclusions and figure captions
  accessed_at: '2026-10-21T10:09:11.021162Z'
  support: supports
  summary: The full cited Molecules paper identifies native Neonectria DH2 parent
    ilicicolin H and heterologous A. nidulans production of H/J. It explicitly contrasts
    its results with the separate Penicillium variabile icc study that produced 8-epi-H.
    It reports no exact 8-epi-H production by DH2 or its transferred ili locus. Purified
    IliD was expressed but the absence of substrate prevented its enzymatic assay.
  snapshot_sha256: 4ab7c924311d2f0244f1a19f7f99701cb41894ed3f1a2ca0a6bcf307412e5477
- evidence_id: R033-CITED-SI
  kind: primary_source
  reference: https://mdpi-res.com/d_attachment/molecules/molecules-24-02267/article_deploy/molecules-24-02267-s001.pdf
  locator: Complete 18-page publisher SI text, tables, captions and protein sequence
    text; no raw spectral reprocessing
  accessed_at: '2026-10-21T10:10:15.211517Z'
  support: supports
  summary: The complete supplement text, tables and captions concern H/J, recombinant
    plasmids, IliD expression, negative H↔J host-feeding tests and H/J spectra/assays.
    No exact 8-epi-H experimental product appears in this inspected supplement. Plasmid/gene
    labels differ among body, Figure3 and SI tables; these cannot be converted into
    verified exact recombinant genotype claims without reconciliation.
  snapshot_sha256: 5c5b4c31e787c29dda3869497828f985fca9230e8b36ccaa406b86d3d8d3bf87
- evidence_id: R033-CITED-FIG1
  kind: primary_source
  reference: https://mdpi-res.com/molecules/molecules-24-02267/article_deploy/html/images/molecules-24-02267-g001.png
  locator: Original full-resolution Figure1A pixels; Molecules atom numbering
  accessed_at: '2026-10-21T10:10:15.382025Z'
  support: supports
  summary: The original Figure1A depicts the named epimer as contextual third structure,
    without a product number. Its propenyl-bearing centre is left without a wedge,
    whereas its carbonyl-bearing C8 is shown opposite to parent H. This source drawing
    is consistent with the incomplete database encoding, but it is not a complete
    exact-epimer assignment.
  snapshot_sha256: ca60f31b42aed06d87f56a64c1c84146207f98fbdca1be47b2d48d26edfd64d7
- evidence_id: R033-CITED-FIG3
  kind: primary_source
  reference: https://mdpi-res.com/molecules/molecules-24-02267/article_deploy/html/images/molecules-24-02267-g003.png
  locator: Original full-resolution Figure3A/B pixels
  accessed_at: '2026-10-21T10:10:15.501299Z'
  support: supports
  summary: The original chromatograms label products1 and2 as H and J, and show native
    DH2 and recombinant-host profiles. They do not label or authenticate target 8-epi-H.
    The gene labels are inconsistent with some prose/table labels and are not used
    to infer exact unsequenced constructs.
  snapshot_sha256: 490fbc084acc801ab64ccfe4d762d8bd7209706d63acaa40d727aa1b4be299e4
- evidence_id: R033-JACS-MAIN
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=6585442&retmode=xml
  locator: DOI10.1021/jacs.9b02204, PMID30905148; complete main Results and Discussion
  accessed_at: '2026-10-21T09:30:20.559822Z'
  support: supports
  summary: The independent icc study expresses genes from P. variabile HXQ-H-1 in
    A. nidulans A1145. IccA/B/C/D produce exact 8-epi-H compound2, characterized by
    NMR; IccE converts it to parent1. Purified C-His IccD converts acyclic4 to2 and
    N-His IccE converts2 to1. Native production by DH2 is not established by these
    donor/host experiments.
  snapshot_sha256: 977ef883f284598b118772a3e870a338067eb835fa9cb18c76e1d5c140dbd754
- evidence_id: R033-JACS-SI
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/14703596
  locator: Official SI Methods S4–S7; original TableS6 S13 structure, NOESY drawing
    and NMR; exact source preparations and assay scope
  accessed_at: '2026-10-21T09:30:54.013486Z'
  support: supports
  summary: TableS6 specifies all five tetrahedral centres of compound2, including
    the propenyl-bearing carbon numbered C17 in this paper, corresponding to C9 in
    the Molecules drawing. HRMS and optical rotation accompany the NMR assignment.
    The donor strain is HXQ-H-1 and the production host is FGSC A1145. The exact target
    MIC40 µg/mL versus parent0.4 µg/mL cannot be replaced by H/J MIC6.3 µg/mL from
    the other study.
  snapshot_sha256: 48957963c20a0a7072201d3583c53e964e0d654c9e869f53785a572cfa9eb773
- evidence_id: R033-CHEBI
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/155888/
  locator: Complete exact response inspected
  accessed_at: '2026-10-21T10:12:49.747252Z'
  support: supports
  summary: Released CHEBI155888 is two-star and cites PMID30905148 for the fully specified
    epimer, full key BYVVOONSAAQMKI-NMEWZTTESA-N. It is an identity corroboration
    lead, ineligible for the existing three-star grounding/replacement rule. Its API
    SMILES fails aromatic kekulization; the official MOL and InChI were checked separately
    rather than silently repairing that string.
  snapshot_sha256: 6bdabfae91601e7c50dc79480940a92e30820dfde1f15724dea692705db306f4
- evidence_id: R033-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/155888/
  locator: Complete exact response inspected
  accessed_at: '2026-10-21T10:13:57.661556Z'
  support: supports
  summary: The official connection table parses to five assigned centres and the full
    epimer key BYVVOONSAAQMKI-NMEWZTTESA-N. It agrees with the authority InChI and
    one completion of the owner missing centre.
  snapshot_sha256: 4c50007c694978f174fea79ddf8d1cf8c688bbdf5c817e63bba4342302811ae7
- evidence_id: R033-CHEMISTRY
  kind: validation
  reference: /private/tmp/npm-review-work/033/identity/stereo-comparison.json
  locator: RDKit enumeration of the single unspecified owner centre; official MOL
    comparison retained separately
  accessed_at: '2026-10-21T10:13:39.363917Z'
  support: supports
  summary: 'The unspecified zero-based atom11 bears the propenyl group: Molecules
    C9/JACS C17. Its two completions give distinct keys NMEWZTTESA (S) and PVSUOEAJSA
    (R); the current CVCLIUOFSA key distinguishes neither. The epimer-defining carbonyl-bearing
    C8 is already assigned. The original incomplete graph is internally consistent
    and honestly flagged, but does not uniquely denote the fully assigned named product.'
  snapshot_sha256: 991a5c776af5698966309a470212f11d7ed8fbbf32777ad45bcf3d916b216b62
- evidence_id: R033-TAXON
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1735992&retmode=xml
  locator: Complete exact response inspected
  accessed_at: '2026-10-21T10:09:11.205422Z'
  support: supports
  summary: NCBI1735992 is Neonectria sp. DH2, assigned species rank under unclassified
    Neonectria. Correct taxonomy does not establish production of this particular
    epimer.
  snapshot_sha256: e50415edf2bd2d0122de89c9b6c30814cccb7195a34be289fb147c18c1d1aaac
- evidence_id: R033-GENOME
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=RQWH01000002.1&db=nuccore&report=genbank&retmode=text
  locator: Original GenBank header, complete source feature and contig length; unrelated
    sequence not experimentally reassessed
  accessed_at: '2026-10-21T10:10:15.535872Z'
  support: supports
  summary: RQWH01000002.1 is the 3,797,617-bp DH2 contig000001F, taxon1735992, BioProjectPRJNA507358/BioSampleSAMN10492166.
    Its source says strainDH2 isolated from Meconopsis grandis plant root. The stored
    locus interval lies inside the contig. This supports accession provenance but
    not exact target formation or a purified IliD assay.
  snapshot_sha256: 0cb4b305b62c6bb8c9fdc8f2fd97267348c77bd47659b9ad04be389b5d2749c4
- evidence_id: R033-CLASS
  kind: record_content
  reference: data/raw/npclassifier.tsv
  locator: Complete exact-key pinned row
  accessed_at: '2026-10-21T10:17:32.829814Z'
  support: context_only
  summary: The owner preserves the versioned Alkaloids/Nicotinic acid alkaloids/Pyridine
    alkaloids prediction separately from source NRPS/PKS assertions. Filing consistency
    does not repair either exact stereochemistry or a wrong product-to-source association.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: R033-LOADERS
  kind: record_content
  reference: src/naturalproductmech/curate/structure_corrections.py
  locator: Complete structure correction loader plus seeder source-claim emission
    and WITHDRAW branches
  accessed_at: '2026-10-21T10:17:32.829814Z'
  support: context_only
  summary: The existing structure correction accepts only a unique structured three-star
    ChEBI target and preserves source context. Two-star155888 is not accepted. WITHDRAW
    only removes method applicability and leaves producer/locus assertions; with no
    methods already present it cannot suppress this unsupported association. The seeder
    unconditionally emits a named MIBiG producer. Claim-reference and strain consumers
    reject incompatible structure corrections. A coordinated, tested source/structure
    correction route is needed.
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
- evidence_id: R033-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/033/identity/local-search.txt
  locator: Ignored-inclusive exact target/key/slug search through corpus, maintained
    inputs, code and review evidence
  accessed_at: '2026-10-21T10:09:35.679431Z'
  support: context_only
  summary: The scoped search identifies the sole current target source and historical
    inventories. It does not establish an eligible current three-star exact replacement
    or an existing consumed correction for this target. Candidate full-key uniqueness
    must be independently checked before a structure-changing implementation.
  snapshot_sha256: 1b4caa26c2f7ba9865e76949fc6747abb40bd75bac54d8aab6eafec5dc91da91
  search_scope: rg --no-ignore --hidden -n -i naturalproductmech:mibig-1cc1aa7754|8-epi-ilicicolin-h|BYVVOONSAAQMKI-CVCLIUOFSA-N
    curation data/raw data/natural_products reviews src scripts
- evidence_id: R033-IMODULON
  kind: database
  reference: https://imodulondb.org/
  locator: Complete retained 28-dataset catalogue
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: No Neonectria, Penicillium variabile or A. nidulans dataset occurs in the
    inspected catalogue. No expression-module evidence is substituted for the actual
    donor/host experiments.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
assessments:
- assessment_id: R033-IDENTITY
  area: identity
  topic: Published exact epimer versus incomplete source graph
  outcome: concern
  summary: The current graph has one unresolved centre, explicitly flagged false,
    whereas the exact primary product is fully specified. The missing centre is the
    propenyl-bearing C9/C17, not epimer-defining C8. The full candidate graph requires
    a guarded identity migration and cannot be made an xref-equivalent of the broader
    key.
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  evidence_ids:
  - R033-OWNER
  - R033-CITED-FIG1
  - R033-JACS-SI
  - R033-CHEBI
  - R033-MOL
  - R033-CHEMISTRY
  dimensions:
  - name: stereochemical_resolution
    value: 4 specified + 1 unspecified owner centre; primary product has5 specified
    definition: Tetrahedral resolution of the stored owner versus the separately characterized
      exact product.
    evidence_ids:
    - R033-CHEMISTRY
    - R033-JACS-SI
- assessment_id: R033-SOURCE-SCOPE
  area: scope
  topic: Native donor, heterologous host and congener identity
  outcome: concern
  summary: DH2/ili evidence concerns H/J, while the exact epimer is demonstrated in
    A1145 expressing HXQ-H-1 icc genes. Correcting the citation alone would transfer
    evidence across donor taxa and loci. The current sole producer/locus association
    needs explicit suppression or replacement through an implemented source route.
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  evidence_ids:
  - R033-RAW
  - R033-CITED-MAIN
  - R033-CITED-SI
  - R033-CITED-FIG3
  - R033-JACS-MAIN
  - R033-JACS-SI
  dimensions:
  - name: current_source
    value: BGC0002035 version3; Neonectria sp. DH2; RQWH01000002.1
    definition: Database source attached to this owner, whose cited experiments do
      not establish this exact product.
    evidence_ids:
    - R033-MIBIG
    - R033-CITED-MAIN
  - name: demonstrated_exact_product_context
    value: P. variabile HXQ-H-1 genes expressed in A. nidulans FGSC A1145
    definition: Donor and production host of the separate exact-epimer experiment;
      not native DH2 production.
    evidence_ids:
    - R033-JACS-MAIN
    - R033-JACS-SI
- assessment_id: R033-ORIGIN
  area: evidence
  topic: Biological formation of the fully specified candidate
  outcome: supported
  summary: The JACS study supplies exact-product heterologous production and purified-enzyme
    conversion. This supports a biological route for the fully assigned candidate,
    while current source admission must be repaired without presenting donor-gene
    provenance as native occurrence.
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  evidence_ids:
  - R033-JACS-MAIN
  - R033-JACS-SI
- assessment_id: R033-LOCAL
  area: provenance
  topic: Source fidelity, taxonomy, filing and audit
  outcome: supported
  summary: The current YAML faithfully reproduces its active source and partial stereo
    flag. Taxon and deposited-contig metadata resolve, computed filing is attributed
    and both seed events retain SEEDED. These deterministic and provenance positives
    coexist with the scientific identity/source defects.
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  evidence_ids:
  - R033-OWNER
  - R033-RAW
  - R033-MIBIG
  - R033-TAXON
  - R033-GENOME
  - R033-CLASS
- assessment_id: R033-OPTIONAL
  area: completeness
  topic: Unasserted optional activity and mechanisms
  outcome: not_applicable
  summary: The owner makes no assay, enzyme or graph assertion. Optional content need
    not be added to fix the record. If later expanded, exact epimer assays and icc
    experiments must remain separate from parent H/J activity and proposed IliD chemistry.
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  evidence_ids:
  - R033-OWNER
  - R033-CITED-MAIN
  - R033-JACS-MAIN
findings:
- finding_id: R033-F-STEREO
  issue_key: mibig-bgc0002035-compound3-incomplete-exact-stereochemistry
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The named epimer remains unresolved at one published stereocentre
  description: The owner truthfully declares incomplete stereo, but its unspecified
    propenyl-bearing centre allows two different full structures. The primary JACS
    compound2 and official ChEBI MOL specify the exact 8-epi product. This is a resolution
    mismatch, not a false stereo_complete:true flag or a missing C8 assignment.
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  field_paths:
  - chemical_structure
  - source_concepts
  - grounding_status
  evidence_ids:
  - R033-OWNER
  - R033-JACS-SI
  - R033-MOL
  - R033-CHEMISTRY
  - R033-LOADERS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Implemented guarded exact-structure correction capability
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Future consumed full-row-pinned structural decision
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic identity and source-admission composition
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Explicit generated-owner migration bookkeeping after full-key adjudication
- finding_id: R033-F-SOURCE
  issue_key: mibig-bgc0002035-compound3-wrong-product-producer-locus
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The cited DH2 study does not demonstrate this epimer
  description: PMID31216742 reports native and transferred DH2 ili production of ilicicolin
    H/J and cites the distinct HXQ-H-1 icc study for 8-epi-H. The imported native
    producer/locus pair therefore lacks exact-product support. Empty locus methods
    and SOURCE_ASSERTION accurately describe the database import but do not cure the
    misassociation. A simple citation replacement would conflate different loci and
    production hosts.
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  field_paths:
  - producer_organisms[0]
  - biosynthetic_gene_clusters[0]
  - biosynthesis_origin
  evidence_ids:
  - R033-RAW
  - R033-MIBIG
  - R033-CITED-MAIN
  - R033-CITED-SI
  - R033-CITED-FIG3
  - R033-JACS-MAIN
  - R033-JACS-SI
  - R033-LOADERS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Current unconditional MIBiG producer and locus emission; required consumed
      claim-suppression/replacement capability
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Immutable reviewed source row and original assertion provenance
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Guarded correction composition; citation replacement alone is insufficient
actions:
- action_id: R033-A-IDENTITY
  description: Implement and test an explicit primary-source-backed exact-structure
    correction route for BGC0002035:3, pinning complete raw row fb39874b95050f740b756b4a04de6a25fa9b4b93c7116d9b2d04d57d53c796c0
    and the inspected primary structure evidence. Independently confirm the five-centre
    candidate BYVVOONSAAQMKI-NMEWZTTESA-N and collision/migration scope. Existing
    REPLACE_WITH_CHEBI cannot accept two-star155888; do not promote its status or
    silently repair its API SMILES. Use the verified official MOL and primary drawing
    to inform a guarded source route. Coordinate this structural change with the source-claim
    action so that the corrected key does not inherit an unsupported DH2 producer/locus.
    Preserve original assertions as explicitly superseded provenance.
  finding_ids:
  - R033-F-STEREO
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Implemented guarded exact-structure correction capability
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Future consumed full-row-pinned structural decision
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic identity and source-admission composition
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Explicit generated-owner migration bookkeeping after full-key adjudication
  generator: scripts/seed_from_sources.py after an explicitly implemented guarded
    correction extension
  acceptance_checks:
  - The exact five-centre structure is independently confirmed against the original
    compound2 drawing, with C9/C17 distinguished from C8; SMILES/InChI/full key/stereo
    flag agree.
  - A gitignore-independent full-key search and complete source-table comparison establish
    all collisions and affected owners before any migration; old and new keys are
    not asserted equivalent.
  - The complete original source row and replacement chemistry/evidence are pinned;
    source or replacement drift fails closed. No unconsumed decisions.tsv entry or
    ineligible two-star ChEBI grounding is used.
  - The structural and producer/locus corrections compose under explicit tested guards;
    no existing guard is bypassed by refreshing hashes.
  - Canary output, migration/PATHS checks, strict validation, exact byte reproduction
    and repository QC pass before the correction is accepted.
- action_id: R033-A-SOURCE
  description: 'Implement a source-pinned claim suppression/replacement path that
    prevents BGC0002035:3 from emitting unsupported DH2 production or ili-locus attribution
    for this epimer. Retain the original MIBiG row as historical source provenance.
    Re-establish the corrected exact product through an effective reproducible admission
    route anchored to PMID30905148: distinguish HXQ-H-1 donor genes, the deposited
    icc locus and FGSC A1145 heterologous production, with Enzymatic assays/Heterologous
    expression only where directly supported. Merely changing the source PMID or applying
    WITHDRAW is insufficient: WITHDRAW leaves the assertions present and existing
    methods are already empty. Treat any native-donor occurrence as unresolved unless
    separately evidenced.'
  finding_ids:
  - R033-F-SOURCE
  target_ids:
  - naturalproductmech:mibig-1cc1aa7754
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Current unconditional MIBiG producer and locus emission; required consumed
      claim-suppression/replacement capability
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Immutable reviewed source row and original assertion provenance
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Guarded correction composition; citation replacement alone is insufficient
  generator: scripts/seed_from_sources.py with explicit consumed source-admission
    and claim correction support
  depends_on:
  - R033-A-IDENTITY
  acceptance_checks:
  - No DH2 producer or RQWH01000002.1 ili association remains asserted for the corrected
    epimer solely on PMID31216742; original source provenance remains inspectable.
  - The exact corrected product has a valid reproducible biological-origin admission
    route and source evidence; do not leave an orphan record or infer membership from
    chemical resemblance.
  - The donor organism, production host, native versus heterologous context and actual
    source locus are independently grounded and separately qualified; do not reuse
    BGC0002035 for the icc experiment.
  - Keep H/J parent activities and proposed unassayed IliD chemistry off the epimer.
    Do not introduce native DH2 or native HXQ-H-1 production without exact-compound
    evidence.
  - Composition tests cover source drift, structure correction, suppression, replacement,
    source provenance and corpus reproduction; run canary, strict, filing-integrity
    and full repository gates.
limitations:
- The complete cited Molecules body and supplement text were read, and main Figures1/3
  were visually inspected. Raw NMR spectra, unrelated genome bases and complete recombinant
  construct sequences were not reanalysed.
- The JACS main body, relevant original SI methods and TableS6 structure/NOESY drawing
  were inspected. Primary absolute-configuration experiments were not repeated. The
  two papers use different atom numbering and have distinct products and strain contexts.
- The ChEBI candidate is two-star and its current API SMILES fails RDKit kekulization;
  the official connection table and InChI agree on the fully specified candidate.
  No authority status was altered and no invalid SMILES was silently repaired.
- The appropriate consumed structural/admission correction capability does not yet
  exist for this combined case. The actions describe concrete required implementation
  and validation, not an assertion that existing citation or method overlays alone
  perform it.
- The configured identifier-label gate accepts 499 warning-level mismatches and 35
  explicit exceptions and skips 4,744 no-adapter pairs; exit 0 does not independently
  verify every identifier or scientific claim.
- The quality suite reports 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21).
  Skipped tests are not counted as passing tests. Existing ontology caches were used;
  no multi-gigabyte cache download was required.
- Native gates assess deterministic consistency and configured invariants. They do
  not establish biological production, stereochemical specificity, evidence adequacy,
  or literature-level claim support.
notes:
- No scientific owner, inventory, curation table, native status or history was edited.
  Actions are proposed work.
- Shared baseline gates and target strict validation retain their actual fresh command
  receipts for this base. Scientific failed or unavailable checks are distinct from
  bundle validation.
- An independent reviewer checked the primary drawings, product scope and composed
  correction requirements; receipt /private/tmp/npm-review-work/033/root-packet-qa.json
  retains its actual review time and packet hash.
tags:
- path-order-campaign
- batch-004
```
