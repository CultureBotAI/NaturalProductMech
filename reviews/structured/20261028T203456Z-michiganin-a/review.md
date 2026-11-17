# Scientific review of michiganin A

- Review: 20261028T203456Z-michiganin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-28T19:59:11.126210Z
- Finished UTC: 2026-10-28T20:34:56.451869Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The owner names michiganin A and marks its retained structure stereochemically complete. PMID 16957199 explicitly identifies michiganin A and reports a modified peptide with three methyllanthionine bridges, providing relevant named-compound context. Neither the inspected abstract nor the frontmatter-only PMC response establishes the complete atom-by-atom bridge correspondence and configuration of this stored graph. The representation-dependent C=N differences do not alone establish missing natural stereochemistry or justify a replacement. The owner asserts Clavibacter michiganensis subsp. michiganensis NCPPB382, NCBITaxon:443906, with SOURCE_ASSERTION. The abstract names the subspecies but does not establish NCPPB382 as the exact source of this stored product. The separate LOTUS occurrence is Clavibacter michiganensis, NCBITaxon:28447. Species, subspecies and strain assertions remain distinct.

## Scope And Provenance

Bounded scientific review of michiganin A using the whole current owner and retained source rows, saved dual-encoding diagnostics, and verified own publication metadata or abstracts. Exact structure, origin, producer, occurrence, locus, pathway and activity claims retain their stated evidence limits.

Selection: One record selected in canonical path order as order 851 of batch86 from the accepted unreviewed-record inventory.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-a87ca2aefb | data/natural_products/amino_acids_and_peptides/michiganin-a.yaml | generated | michiganin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-a87ca2aefb | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-a87ca2aefb | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-a87ca2aefb | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-a87ca2aefb | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-a87ca2aefb | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | naturalproductmech:mibig-a87ca2aefb | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Whole owner and retained source joins | passed | True | naturalproductmech:mibig-a87ca2aefb | The whole michiganin A owner retains one MIBiG compound row, one LOTUS occurrence and one NPClassifier row, with two seed-history entries. All other retained source sets and supplemental sets for this owner are empty. No inline causal_graphs, biosynthetic_pathway, bioactivities or molecular_targets field is present. These are scoped observations of the pinned owner and complete selected rows, not evidence of biological absence. |
| Saved encoding agreement and representation limits | passed | True | naturalproductmech:mibig-a87ca2aefb | The two saved default parses agree on neutral C92H145N25O26S4 and key MTKXZQFBKJNJJF-MJLJTCNBSA-N. Both describe four sulfur atoms, including three ring thioether environments and one degree-one sulfur, and 21 specified tetrahedral centres. Their explicit canonical SMILES and whole atom correspondence do not match; the InChI-derived form has more unspecified C=N environments. Standardization agreement and encoded sulfur topology do not independently verify the natural bridge assignments, full configuration or physiological protonation. |
| Exact congener and natural configuration | unavailable | True | naturalproductmech:mibig-a87ca2aefb | The owner names michiganin A and marks its retained structure stereochemically complete. PMID 16957199 explicitly identifies michiganin A and reports a modified peptide with three methyllanthionine bridges, providing relevant named-compound context. Neither the inspected abstract nor the frontmatter-only PMC response establishes the complete atom-by-atom bridge correspondence and configuration of this stored graph. The representation-dependent C=N differences do not alone establish missing natural stereochemistry or justify a replacement. |
| Biological origin versus exact stored-form correspondence | unavailable | True | naturalproductmech:mibig-a87ca2aefb | The own abstract reports isolation of michiganin A from Clavibacter michiganensis subsp. michiganensis. This is positive biological-source context for the NATURAL_PRODUCT assertion. Exact correspondence of the isolated product to every feature of this retained encoding remains unresolved; no natural-absence or synthetic-only conclusion follows from the held primary response. |
| Claim-specific producer and taxon/strain support | unavailable | True | naturalproductmech:mibig-a87ca2aefb | The owner asserts Clavibacter michiganensis subsp. michiganensis NCPPB382, NCBITaxon:443906, with SOURCE_ASSERTION. The abstract names the subspecies but does not establish NCPPB382 as the exact source of this stored product. The separate LOTUS occurrence is Clavibacter michiganensis, NCBITaxon:28447. Species, subspecies and strain assertions remain distinct. |
| Separately attributed occurrence assertions | passed | True | naturalproductmech:mibig-a87ca2aefb | The LOTUS occurrence cites DOI 10.1128/AEM.00639-06; own PubMed ArticleIdList verifies that DOI with PMID 16957199. The abstract reports the named product from the retained subspecies, supporting the broader species occurrence context. This does not establish the separate NCPPB382 assertion or full structural correspondence. |
| Retained locus grade and citation applicability | unavailable | True | naturalproductmech:mibig-a87ca2aefb | MIBiG BGC0000528 entry version 5 retains AM711867.1:2216380..2224562, ribosomal/RiPP classification and CLUSTER_UNSTATED. The own abstract discusses a michiganin gene, while its own DataBank list supplies DQ458780. Neither the abstract nor this accession label verifies the retained AM711867.1 interval or a strain-specific cluster experiment. Different accession strings are not treated as a demonstrated conflict or as aliases. |
| Encoded classification and biosynthetic context | passed | True | naturalproductmech:mibig-a87ca2aefb | The peptide filing, retained Lanthipeptides/RiPPs model labels and encoded sulfur-containing rings are compatible with the abstract’s lantibiotic context. The model classification and local encoded motifs do not demonstrate the entire biosynthetic pathway or experimentally assign the stored ring topology. |
| Exact-compound assay and target limits | not_applicable | True | naturalproductmech:mibig-a87ca2aefb | The abstract reports growth inhibition of Clavibacter michiganensis subsp. sepedonicus by michiganin A. This is qualitative named-product activity context. The pinned owner and selected tables contain no quantitative assay or molecular-target assertion to verify, and the abstract does not support importing a potency, exact target, or assay conditions for this stored structure. |
| Source versions and distinct evidence tiers | passed | True | naturalproductmech:mibig-a87ca2aefb | MIBiG BGC0000528 version 5 remains quality questionable and completeness unknown; NPClassifier retains npclassifier.gnps2.org@2026-09-07. Whole local rows, model output, saved default-parser diagnostics, own PubMed metadata and the PMC frontmatter-only failure are distinct evidence tiers. The original access clocks and two seed-history entries are preserved without upgrading a successful HTTP status to a complete primary reading. |

## Scientific And Domain Assessments

### Saved encoding agreement and representation limits

consistency: supported. Targets: naturalproductmech:mibig-a87ca2aefb.

The two saved default parses agree on neutral C92H145N25O26S4 and key MTKXZQFBKJNJJF-MJLJTCNBSA-N. Both describe four sulfur atoms, including three ring thioether environments and one degree-one sulfur, and 21 specified tetrahedral centres. Their explicit canonical SMILES and whole atom correspondence do not match; the InChI-derived form has more unspecified C=N environments. Standardization agreement and encoded sulfur topology do not independently verify the natural bridge assignments, full configuration or physiological protonation.

### Exact congener and natural configuration

identity: unknown. Targets: naturalproductmech:mibig-a87ca2aefb.

The owner names michiganin A and marks its retained structure stereochemically complete. PMID 16957199 explicitly identifies michiganin A and reports a modified peptide with three methyllanthionine bridges, providing relevant named-compound context. Neither the inspected abstract nor the frontmatter-only PMC response establishes the complete atom-by-atom bridge correspondence and configuration of this stored graph. The representation-dependent C=N differences do not alone establish missing natural stereochemistry or justify a replacement.

### Biological origin versus exact stored-form correspondence

evidence: unknown. Targets: naturalproductmech:mibig-a87ca2aefb.

The own abstract reports isolation of michiganin A from Clavibacter michiganensis subsp. michiganensis. This is positive biological-source context for the NATURAL_PRODUCT assertion. Exact correspondence of the isolated product to every feature of this retained encoding remains unresolved; no natural-absence or synthetic-only conclusion follows from the held primary response.

### Claim-specific producer and taxon/strain support

evidence: unknown. Targets: naturalproductmech:mibig-a87ca2aefb.

The owner asserts Clavibacter michiganensis subsp. michiganensis NCPPB382, NCBITaxon:443906, with SOURCE_ASSERTION. The abstract names the subspecies but does not establish NCPPB382 as the exact source of this stored product. The separate LOTUS occurrence is Clavibacter michiganensis, NCBITaxon:28447. Species, subspecies and strain assertions remain distinct.

### Separately attributed occurrence assertions

evidence: supported. Targets: naturalproductmech:mibig-a87ca2aefb.

The LOTUS occurrence cites DOI 10.1128/AEM.00639-06; own PubMed ArticleIdList verifies that DOI with PMID 16957199. The abstract reports the named product from the retained subspecies, supporting the broader species occurrence context. This does not establish the separate NCPPB382 assertion or full structural correspondence.

### Retained locus grade and citation applicability

evidence: unknown. Targets: naturalproductmech:mibig-a87ca2aefb.

MIBiG BGC0000528 entry version 5 retains AM711867.1:2216380..2224562, ribosomal/RiPP classification and CLUSTER_UNSTATED. The own abstract discusses a michiganin gene, while its own DataBank list supplies DQ458780. Neither the abstract nor this accession label verifies the retained AM711867.1 interval or a strain-specific cluster experiment. Different accession strings are not treated as a demonstrated conflict or as aliases.

### Encoded classification and biosynthetic context

scope: supported. Targets: naturalproductmech:mibig-a87ca2aefb.

The peptide filing, retained Lanthipeptides/RiPPs model labels and encoded sulfur-containing rings are compatible with the abstract’s lantibiotic context. The model classification and local encoded motifs do not demonstrate the entire biosynthetic pathway or experimentally assign the stored ring topology.

### Exact-compound assay and target limits

quantity: not_applicable. Targets: naturalproductmech:mibig-a87ca2aefb.

The abstract reports growth inhibition of Clavibacter michiganensis subsp. sepedonicus by michiganin A. This is qualitative named-product activity context. The pinned owner and selected tables contain no quantitative assay or molecular-target assertion to verify, and the abstract does not support importing a potency, exact target, or assay conditions for this stored structure.

### Source versions and distinct evidence tiers

provenance: supported. Targets: naturalproductmech:mibig-a87ca2aefb.

MIBiG BGC0000528 version 5 remains quality questionable and completeness unknown; NPClassifier retains npclassifier.gnps2.org@2026-09-07. Whole local rows, model output, saved default-parser diagnostics, own PubMed metadata and the PMC frontmatter-only failure are distinct evidence tiers. The original access clocks and two seed-history entries are preserved without upgrading a successful HTTP status to a complete primary reading.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI851-LOCAL | /private/tmp/npm-review-work/shared-next-batch086-tentative/tentative-owner-source-inventory-001.json; /entries/0/owner_document; /entries/0/rows; /entries/0/supplemental_retained_rows | context_only | The whole michiganin A owner retains one MIBiG compound row, one LOTUS occurrence and one NPClassifier row, with two seed-history entries. All other retained source sets and supplemental sets for this owner are empty. No inline causal_graphs, biosynthetic_pathway, bioactivities or molecular_targets field is present. These are scoped observations of the pinned owner and complete selected rows, not evidence of biological absence. |
| SCI851-ENCODINGS | /private/tmp/npm-review-work/shared-next-batch086-tentative/source-science-preparation/bgc-tentative86-ten-owner-dual-encoding-results-001.json; /records/0/smiles; /records/0/inchi; /records/0/comparisons; /records/0/atom_correspondence | supports | The two saved default parses agree on neutral C92H145N25O26S4 and key MTKXZQFBKJNJJF-MJLJTCNBSA-N. Both describe four sulfur atoms, including three ring thioether environments and one degree-one sulfur, and 21 specified tetrahedral centres. Their explicit canonical SMILES and whole atom correspondence do not match; the InChI-derived form has more unspecified C=N environments. Standardization agreement and encoded sulfur topology do not independently verify the natural bridge assignments, full configuration or physiological protonation. |
| SCI851-PUBMED | /private/tmp/npm-review-work/shared-next-batch086-tentative/literature-preparation/public-metadata-pubmed-001/pmid-16957199.xml; /PubmedArticleSet/PubmedArticle[1]/MedlineCitation/PMID; /PubmedArticleSet/PubmedArticle[1]/MedlineCitation/Article/ArticleTitle; /PubmedArticleSet/PubmedArticle[1]/MedlineCitation/Article/Abstract; /PubmedArticleSet/PubmedArticle[1]/PubmedData/ArticleIdList; /PubmedArticleSet/PubmedArticle[1]/MedlineCitation/Article/DataBankList | partial | Own PMID 16957199/DOI 10.1128/AEM.00639-06/PMC1563628 title and abstract identify michiganin A, its subspecies source, modified-peptide context, gene-related context and qualitative inhibition. The DataBank list supplies DQ458780. The inspected metadata does not verify NCPPB382, the retained AM711867.1 interval, or complete atom/configuration correspondence. |
| SCI851-PRIMARY-HOLD | /private/tmp/npm-review-work/shared-next-batch086-tentative/literature-preparation/public-primary-five-own-PMC-001/pmc1563628.xml.access.json; /http_status; /identity/frontmatter_only; /success; /finished_at; /body | context_only | The exact own-PMC XML access records HTTP 200, a complete received response, matching own frontmatter, zero article-body text characters and success:false because no substantive article body was returned. This receipt establishes a bounded source-access limitation; it does not verify the natural structure or refute the biological claims. |

## Limits And Additional Notes

- The owner names michiganin A and marks its retained structure stereochemically complete. PMID 16957199 explicitly identifies michiganin A and reports a modified peptide with three methyllanthionine bridges, providing relevant named-compound context. Neither the inspected abstract nor the frontmatter-only PMC response establishes the complete atom-by-atom bridge correspondence and configuration of this stored graph. The representation-dependent C=N differences do not alone establish missing natural stereochemistry or justify a replacement.
- The owner asserts Clavibacter michiganensis subsp. michiganensis NCPPB382, NCBITaxon:443906, with SOURCE_ASSERTION. The abstract names the subspecies but does not establish NCPPB382 as the exact source of this stored product. The separate LOTUS occurrence is Clavibacter michiganensis, NCBITaxon:28447. Species, subspecies and strain assertions remain distinct.
- MIBiG BGC0000528 entry version 5 retains AM711867.1:2216380..2224562, ribosomal/RiPP classification and CLUSTER_UNSTATED. The own abstract discusses a michiganin gene, while its own DataBank list supplies DQ458780. Neither the abstract nor this accession label verifies the retained AM711867.1 interval or a strain-specific cluster experiment. Different accession strings are not treated as a demonstrated conflict or as aliases.
- The abstract reports growth inhibition of Clavibacter michiganensis subsp. sepedonicus by michiganin A. This is qualitative named-product activity context. The pinned owner and selected tables contain no quantitative assay or molecular-target assertion to verify, and the abstract does not support importing a potency, exact target, or assay conditions for this stored structure.
- The exact own-PMC XML request returned HTTP200 and correct own frontmatter, but no substantive article body. The original access records success:false and frontmatter_only:true. ROOT retained this source failure with six original leaves and prohibited retry/alternate/old remaining-phase use. It is a source-availability limit, not a canonical validation failure or evidence that the biological claims are false.
- Configured consistency only; independent scientific claim support and unrestricted remote authority refresh are not implied.
- FailedQC001 is retained for an explicit separate network-enabled retry; no artifact will be overwritten.
- Fresh QC attempt001 failed on public canonical-artifact DNS retrieval after lint and before downstream tests. Its actual exit1/log/input capture/root observation remain pinned; the selected successful canonical QC attempt002 is separately timed. No individual-review validation failure or counter reset is claimed.
- 499non-blocking identifier-label warnings,35configured exceptions and4898no-adapter skips remain unverified within this gate.
- The QC test suite reported four skipped tests and two dependency deprecation warnings; this pass does not assert skipped checks ran.
- Canonical reproduction retains five unresolved assay-organism annotations,42 withheld nonsingle-organism producer claims and161 configured taxon-ID rewrites.
- This QC is a configured consistency gate, not an independent primary-source biological or stereochemical verification.
- Native baseline gates establish configured consistency, not independent biological production, exact stereochemistry or primary-source adequacy.
- The full configured gate logs retain warnings, skipped tests, identifier exceptions and no-adapter pairs; a successful command does not convert these into verified scientific claims.
- Ontology caches may be reused by the canonical identifier-label gate. Fresh command execution is not proof every remote authority was refreshed.
- Every tracked byte stream/mode and ignored-inclusive corpus/review YAML population was checked; external caches and generated bytecode are not asserted to be independently byte-pinned.
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
review_id: 20261028T203456Z-michiganin-a
title: Scientific review of michiganin A
started_at: '2026-10-28T19:59:11.126210Z'
finished_at: '2026-10-28T20:34:56.451869Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: The owner names michiganin A and marks its retained structure stereochemically
  complete. PMID 16957199 explicitly identifies michiganin A and reports a modified
  peptide with three methyllanthionine bridges, providing relevant named-compound
  context. Neither the inspected abstract nor the frontmatter-only PMC response establishes
  the complete atom-by-atom bridge correspondence and configuration of this stored
  graph. The representation-dependent C=N differences do not alone establish missing
  natural stereochemistry or justify a replacement. The owner asserts Clavibacter
  michiganensis subsp. michiganensis NCPPB382, NCBITaxon:443906, with SOURCE_ASSERTION.
  The abstract names the subspecies but does not establish NCPPB382 as the exact source
  of this stored product. The separate LOTUS occurrence is Clavibacter michiganensis,
  NCBITaxon:28447. Species, subspecies and strain assertions remain distinct.
source:
  git_revision: 14373517042b407747272446f79953ae86d51fa4
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
  - path: data/natural_products/amino_acids_and_peptides/michiganin-a.yaml
    sha256: 041cc3f3b956a2694e98592ce07d33af177e78b4f26e74c91fe9eee600c8136c
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
- target_id: naturalproductmech:mibig-a87ca2aefb
  path: data/natural_products/amino_acids_and_peptides/michiganin-a.yaml
  label: michiganin A
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
scope:
  description: Bounded scientific review of michiganin A using the whole current owner
    and retained source rows, saved dual-encoding diagnostics, and verified own publication
    metadata or abstracts. Exact structure, origin, producer, occurrence, locus, pathway
    and activity claims retain their stated evidence limits.
  selection: One record selected in canonical path order as order 851 of batch86 from
    the accepted unreviewed-record inventory.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-a87ca2aefb
  exclusions:
  - target: Complete primary structural and stereochemical verification
    reason: Primary figures, supporting data and complete article bodies were not
      inspected; internal encoding agreement does not establish the natural structure.
  - target: Current external accession and organism authorities
    reason: Retained accession versions, strain/taxon mappings and any protein identity
      claims were not independently reverified against current authority records.
  - target: Exact-compound claims inferred from related compounds or hosts
    reason: Family, congener and recombinant-host context does not independently establish
      the retained compound-specific claim.
checks:
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its
    pinned path.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-verify-corpus-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.783967Z;
    finished 2026-10-25T22:37:16.453216Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-corpus.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-corpus.log.
    Reused for batch086 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch086. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: Fresh canonical reproduction gate passed:all3116 records byte-identical
    to source seeding; source warnings remain retained.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-verify-reproduction-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.784055Z;
    finished 2026-10-25T22:37:31.682209Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-reproduction.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-reproduction.log.
    Reused for batch086 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch086. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: Fresh deterministic review queue completed:8922 rows across12 queues. Queue
    output is not scientific-review coverage.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-review-queue-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just review-queue --tsv /private/tmp/npm-review-queue-batch-036-fresh14373517-001.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.781802Z;
    finished 2026-10-25T22:37:08.229737Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/review-queue.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/review-queue.log.
    Reused for batch086 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch086. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking
    mismatches and4898no-adapter skips remain explicit.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-validate-products-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.784040Z;
    finished 2026-10-25T22:37:32.251879Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/validate-products.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/validate-products.log.
    Reused for batch086 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch086. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: shared-qc
  name: Full repository quality gate on the fresh main baseline
  status: passed
  required: true
  summary: Canonical just qc completed with actual terminal exit0:1024 tests passed,4
    skipped,2 dependency warnings;3116 records passed closed schema validation, site
    freshness, byte reproduction and lockfile integrity.22 governed artifacts and15
    raw inventories passed. Prior DNS failed001 remains preserved.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-qc-attempt-002
    PYTHONDONTWRITEBYTECODE=1 just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-002 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:40:55.179857Z;
    finished 2026-10-25T22:46:28.974296Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-002/qc.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-002/qc.log.
    Reused for batch086 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch086. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/michiganin-a.yaml
    --out /private/tmp/npm-review-work/851/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-28T19:59:12.547682Z. Original
    receipt: /private/tmp/npm-review-work/851/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: SCI851-LOCAL-JOINS
  name: Whole owner and retained source joins
  status: passed
  required: true
  summary: The whole michiganin A owner retains one MIBiG compound row, one LOTUS
    occurrence and one NPClassifier row, with two seed-history entries. All other
    retained source sets and supplemental sets for this owner are empty. No inline
    causal_graphs, biosynthetic_pathway, bioactivities or molecular_targets field
    is present. These are scoped observations of the pinned owner and complete selected
    rows, not evidence of biological absence.
  evidence_ids:
  - SCI851-LOCAL
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: SCI851-CHECK-ENCODINGS
  name: Saved encoding agreement and representation limits
  status: passed
  required: true
  summary: The two saved default parses agree on neutral C92H145N25O26S4 and key MTKXZQFBKJNJJF-MJLJTCNBSA-N.
    Both describe four sulfur atoms, including three ring thioether environments and
    one degree-one sulfur, and 21 specified tetrahedral centres. Their explicit canonical
    SMILES and whole atom correspondence do not match; the InChI-derived form has
    more unspecified C=N environments. Standardization agreement and encoded sulfur
    topology do not independently verify the natural bridge assignments, full configuration
    or physiological protonation.
  evidence_ids:
  - SCI851-ENCODINGS
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: SCI851-CHECK-IDENTITY
  name: Exact congener and natural configuration
  status: unavailable
  required: true
  summary: The owner names michiganin A and marks its retained structure stereochemically
    complete. PMID 16957199 explicitly identifies michiganin A and reports a modified
    peptide with three methyllanthionine bridges, providing relevant named-compound
    context. Neither the inspected abstract nor the frontmatter-only PMC response
    establishes the complete atom-by-atom bridge correspondence and configuration
    of this stored graph. The representation-dependent C=N differences do not alone
    establish missing natural stereochemistry or justify a replacement.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-ENCODINGS
  - SCI851-PUBMED
  - SCI851-PRIMARY-HOLD
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: SCI851-CHECK-ORIGIN
  name: Biological origin versus exact stored-form correspondence
  status: unavailable
  required: true
  summary: The own abstract reports isolation of michiganin A from Clavibacter michiganensis
    subsp. michiganensis. This is positive biological-source context for the NATURAL_PRODUCT
    assertion. Exact correspondence of the isolated product to every feature of this
    retained encoding remains unresolved; no natural-absence or synthetic-only conclusion
    follows from the held primary response.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-ENCODINGS
  - SCI851-PUBMED
  - SCI851-PRIMARY-HOLD
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: SCI851-CHECK-PRODUCER
  name: Claim-specific producer and taxon/strain support
  status: unavailable
  required: true
  summary: The owner asserts Clavibacter michiganensis subsp. michiganensis NCPPB382,
    NCBITaxon:443906, with SOURCE_ASSERTION. The abstract names the subspecies but
    does not establish NCPPB382 as the exact source of this stored product. The separate
    LOTUS occurrence is Clavibacter michiganensis, NCBITaxon:28447. Species, subspecies
    and strain assertions remain distinct.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-PUBMED
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: SCI851-CHECK-OCCURRENCE
  name: Separately attributed occurrence assertions
  status: passed
  required: true
  summary: The LOTUS occurrence cites DOI 10.1128/AEM.00639-06; own PubMed ArticleIdList
    verifies that DOI with PMID 16957199. The abstract reports the named product from
    the retained subspecies, supporting the broader species occurrence context. This
    does not establish the separate NCPPB382 assertion or full structural correspondence.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-PUBMED
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: SCI851-CHECK-LOCUS
  name: Retained locus grade and citation applicability
  status: unavailable
  required: true
  summary: MIBiG BGC0000528 entry version 5 retains AM711867.1:2216380..2224562, ribosomal/RiPP
    classification and CLUSTER_UNSTATED. The own abstract discusses a michiganin gene,
    while its own DataBank list supplies DQ458780. Neither the abstract nor this accession
    label verifies the retained AM711867.1 interval or a strain-specific cluster experiment.
    Different accession strings are not treated as a demonstrated conflict or as aliases.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-PUBMED
  - SCI851-PRIMARY-HOLD
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: SCI851-CHECK-CLASSIFICATION
  name: Encoded classification and biosynthetic context
  status: passed
  required: true
  summary: The peptide filing, retained Lanthipeptides/RiPPs model labels and encoded
    sulfur-containing rings are compatible with the abstract’s lantibiotic context.
    The model classification and local encoded motifs do not demonstrate the entire
    biosynthetic pathway or experimentally assign the stored ring topology.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-ENCODINGS
  - SCI851-PUBMED
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: SCI851-CHECK-ACTIVITY
  name: Exact-compound assay and target limits
  status: not_applicable
  required: true
  summary: The abstract reports growth inhibition of Clavibacter michiganensis subsp.
    sepedonicus by michiganin A. This is qualitative named-product activity context.
    The pinned owner and selected tables contain no quantitative assay or molecular-target
    assertion to verify, and the abstract does not support importing a potency, exact
    target, or assay conditions for this stored structure.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-PUBMED
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- check_id: SCI851-CHECK-PROVENANCE
  name: Source versions and distinct evidence tiers
  status: passed
  required: true
  summary: MIBiG BGC0000528 version 5 remains quality questionable and completeness
    unknown; NPClassifier retains npclassifier.gnps2.org@2026-09-07. Whole local rows,
    model output, saved default-parser diagnostics, own PubMed metadata and the PMC
    frontmatter-only failure are distinct evidence tiers. The original access clocks
    and two seed-history entries are preserved without upgrading a successful HTTP
    status to a complete primary reading.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-PUBMED
  - SCI851-PRIMARY-HOLD
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
evidence:
- evidence_id: SCI851-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch086-tentative/tentative-owner-source-inventory-001.json
  locator: /entries/0/owner_document; /entries/0/rows; /entries/0/supplemental_retained_rows
  accessed_at: '2026-10-28T18:46:17.134070Z'
  snapshot_sha256: d3f90060011e640e1876fb055bfc8b9fef7fcf9044c0b2bef2e6a6cca8bb2124
  support: context_only
  summary: The whole michiganin A owner retains one MIBiG compound row, one LOTUS
    occurrence and one NPClassifier row, with two seed-history entries. All other
    retained source sets and supplemental sets for this owner are empty. No inline
    causal_graphs, biosynthetic_pathway, bioactivities or molecular_targets field
    is present. These are scoped observations of the pinned owner and complete selected
    rows, not evidence of biological absence.
- evidence_id: SCI851-ENCODINGS
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch086-tentative/source-science-preparation/bgc-tentative86-ten-owner-dual-encoding-results-001.json
  locator: /records/0/smiles; /records/0/inchi; /records/0/comparisons; /records/0/atom_correspondence
  accessed_at: '2026-10-28T18:52:14.255443Z'
  snapshot_sha256: 7f7b5d7d56cc1cbb1fd965e021f94d1d0b5cdeabe80413b06b9a23dd0a55349a
  support: supports
  summary: The two saved default parses agree on neutral C92H145N25O26S4 and key MTKXZQFBKJNJJF-MJLJTCNBSA-N.
    Both describe four sulfur atoms, including three ring thioether environments and
    one degree-one sulfur, and 21 specified tetrahedral centres. Their explicit canonical
    SMILES and whole atom correspondence do not match; the InChI-derived form has
    more unspecified C=N environments. Standardization agreement and encoded sulfur
    topology do not independently verify the natural bridge assignments, full configuration
    or physiological protonation.
- evidence_id: SCI851-PUBMED
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch086-tentative/literature-preparation/public-metadata-pubmed-001/pmid-16957199.xml
  locator: /PubmedArticleSet/PubmedArticle[1]/MedlineCitation/PMID; /PubmedArticleSet/PubmedArticle[1]/MedlineCitation/Article/ArticleTitle;
    /PubmedArticleSet/PubmedArticle[1]/MedlineCitation/Article/Abstract; /PubmedArticleSet/PubmedArticle[1]/PubmedData/ArticleIdList;
    /PubmedArticleSet/PubmedArticle[1]/MedlineCitation/Article/DataBankList
  accessed_at: '2026-10-28T19:30:21.751513Z'
  snapshot_sha256: 511920d05699b98227b4a345469f073d937cd20ab65207c3cbfa3800aa73c4b2
  support: partial
  summary: Own PMID 16957199/DOI 10.1128/AEM.00639-06/PMC1563628 title and abstract
    identify michiganin A, its subspecies source, modified-peptide context, gene-related
    context and qualitative inhibition. The DataBank list supplies DQ458780. The inspected
    metadata does not verify NCPPB382, the retained AM711867.1 interval, or complete
    atom/configuration correspondence.
- evidence_id: SCI851-PRIMARY-HOLD
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch086-tentative/literature-preparation/public-primary-five-own-PMC-001/pmc1563628.xml.access.json
  locator: /http_status; /identity/frontmatter_only; /success; /finished_at; /body
  accessed_at: '2026-10-28T19:50:08.453912Z'
  snapshot_sha256: 85b1765fced8c3a0f47f804e7651c8f1e6bb58476ad4a9acb73d65aa4a06676f
  support: context_only
  summary: The exact own-PMC XML access records HTTP 200, a complete received response,
    matching own frontmatter, zero article-body text characters and success:false
    because no substantive article body was returned. This receipt establishes a bounded
    source-access limitation; it does not verify the natural structure or refute the
    biological claims.
assessments:
- assessment_id: SCI851-ENCODINGS
  area: consistency
  topic: Saved encoding agreement and representation limits
  outcome: supported
  summary: The two saved default parses agree on neutral C92H145N25O26S4 and key MTKXZQFBKJNJJF-MJLJTCNBSA-N.
    Both describe four sulfur atoms, including three ring thioether environments and
    one degree-one sulfur, and 21 specified tetrahedral centres. Their explicit canonical
    SMILES and whole atom correspondence do not match; the InChI-derived form has
    more unspecified C=N environments. Standardization agreement and encoded sulfur
    topology do not independently verify the natural bridge assignments, full configuration
    or physiological protonation.
  evidence_ids:
  - SCI851-ENCODINGS
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- assessment_id: SCI851-IDENTITY
  area: identity
  topic: Exact congener and natural configuration
  outcome: unknown
  summary: The owner names michiganin A and marks its retained structure stereochemically
    complete. PMID 16957199 explicitly identifies michiganin A and reports a modified
    peptide with three methyllanthionine bridges, providing relevant named-compound
    context. Neither the inspected abstract nor the frontmatter-only PMC response
    establishes the complete atom-by-atom bridge correspondence and configuration
    of this stored graph. The representation-dependent C=N differences do not alone
    establish missing natural stereochemistry or justify a replacement.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-ENCODINGS
  - SCI851-PUBMED
  - SCI851-PRIMARY-HOLD
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
  dimensions:
  - name: stereochemical_resolution
    value: 21 specified tetrahedral centres in both encodings; explicit bond-order
      forms and C=N specificity differ. The owner’s true stereo_complete flag is not
      independently confirmed against natural structural data.
    definition: Encoded specificity and representation differences are distinguished
      from experimental natural configuration.
    evidence_ids:
    - SCI851-LOCAL
    - SCI851-ENCODINGS
- assessment_id: SCI851-ORIGIN
  area: evidence
  topic: Biological origin versus exact stored-form correspondence
  outcome: unknown
  summary: The own abstract reports isolation of michiganin A from Clavibacter michiganensis
    subsp. michiganensis. This is positive biological-source context for the NATURAL_PRODUCT
    assertion. Exact correspondence of the isolated product to every feature of this
    retained encoding remains unresolved; no natural-absence or synthetic-only conclusion
    follows from the held primary response.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-ENCODINGS
  - SCI851-PUBMED
  - SCI851-PRIMARY-HOLD
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- assessment_id: SCI851-PRODUCER
  area: evidence
  topic: Claim-specific producer and taxon/strain support
  outcome: unknown
  summary: The owner asserts Clavibacter michiganensis subsp. michiganensis NCPPB382,
    NCBITaxon:443906, with SOURCE_ASSERTION. The abstract names the subspecies but
    does not establish NCPPB382 as the exact source of this stored product. The separate
    LOTUS occurrence is Clavibacter michiganensis, NCBITaxon:28447. Species, subspecies
    and strain assertions remain distinct.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-PUBMED
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
  dimensions:
  - name: taxon_strain
    value: Retained NCPPB382 NCBITaxon:443906 SOURCE_ASSERTION; abstract subspecies
      source; LOTUS species NCBITaxon:28447.
    definition: Species, subspecies, strain, occurrence and producer claims require
      separate source correspondence.
    evidence_ids:
    - SCI851-LOCAL
    - SCI851-PUBMED
- assessment_id: SCI851-OCCURRENCE
  area: evidence
  topic: Separately attributed occurrence assertions
  outcome: supported
  summary: The LOTUS occurrence cites DOI 10.1128/AEM.00639-06; own PubMed ArticleIdList
    verifies that DOI with PMID 16957199. The abstract reports the named product from
    the retained subspecies, supporting the broader species occurrence context. This
    does not establish the separate NCPPB382 assertion or full structural correspondence.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-PUBMED
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- assessment_id: SCI851-LOCUS
  area: evidence
  topic: Retained locus grade and citation applicability
  outcome: unknown
  summary: MIBiG BGC0000528 entry version 5 retains AM711867.1:2216380..2224562, ribosomal/RiPP
    classification and CLUSTER_UNSTATED. The own abstract discusses a michiganin gene,
    while its own DataBank list supplies DQ458780. Neither the abstract nor this accession
    label verifies the retained AM711867.1 interval or a strain-specific cluster experiment.
    Different accession strings are not treated as a demonstrated conflict or as aliases.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-PUBMED
  - SCI851-PRIMARY-HOLD
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- assessment_id: SCI851-CLASSIFICATION
  area: scope
  topic: Encoded classification and biosynthetic context
  outcome: supported
  summary: The peptide filing, retained Lanthipeptides/RiPPs model labels and encoded
    sulfur-containing rings are compatible with the abstract’s lantibiotic context.
    The model classification and local encoded motifs do not demonstrate the entire
    biosynthetic pathway or experimentally assign the stored ring topology.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-ENCODINGS
  - SCI851-PUBMED
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- assessment_id: SCI851-ACTIVITY
  area: quantity
  topic: Exact-compound assay and target limits
  outcome: not_applicable
  summary: The abstract reports growth inhibition of Clavibacter michiganensis subsp.
    sepedonicus by michiganin A. This is qualitative named-product activity context.
    The pinned owner and selected tables contain no quantitative assay or molecular-target
    assertion to verify, and the abstract does not support importing a potency, exact
    target, or assay conditions for this stored structure.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-PUBMED
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
- assessment_id: SCI851-PROVENANCE
  area: provenance
  topic: Source versions and distinct evidence tiers
  outcome: supported
  summary: MIBiG BGC0000528 version 5 remains quality questionable and completeness
    unknown; NPClassifier retains npclassifier.gnps2.org@2026-09-07. Whole local rows,
    model output, saved default-parser diagnostics, own PubMed metadata and the PMC
    frontmatter-only failure are distinct evidence tiers. The original access clocks
    and two seed-history entries are preserved without upgrading a successful HTTP
    status to a complete primary reading.
  evidence_ids:
  - SCI851-LOCAL
  - SCI851-PUBMED
  - SCI851-PRIMARY-HOLD
  target_ids:
  - naturalproductmech:mibig-a87ca2aefb
  dimensions:
  - name: source_version
    value: MIBiG BGC0000528 version 5; NPClassifier npclassifier.gnps2.org@2026-09-07.
    definition: Literal retained versions are distinct from access times and independent
      verification.
    evidence_ids:
    - SCI851-LOCAL
  - name: evidence_tier
    value: Whole retained owner/rows; saved default-parser diagnostics; own PubMed
      metadata/abstract; held own-PMC frontmatter-only response.
    definition: Evidence is credited only at its inspected scope.
    evidence_ids:
    - SCI851-LOCAL
    - SCI851-ENCODINGS
    - SCI851-PUBMED
    - SCI851-PRIMARY-HOLD
findings: []
actions: []
limitations:
- The owner names michiganin A and marks its retained structure stereochemically complete.
  PMID 16957199 explicitly identifies michiganin A and reports a modified peptide
  with three methyllanthionine bridges, providing relevant named-compound context.
  Neither the inspected abstract nor the frontmatter-only PMC response establishes
  the complete atom-by-atom bridge correspondence and configuration of this stored
  graph. The representation-dependent C=N differences do not alone establish missing
  natural stereochemistry or justify a replacement.
- The owner asserts Clavibacter michiganensis subsp. michiganensis NCPPB382, NCBITaxon:443906,
  with SOURCE_ASSERTION. The abstract names the subspecies but does not establish
  NCPPB382 as the exact source of this stored product. The separate LOTUS occurrence
  is Clavibacter michiganensis, NCBITaxon:28447. Species, subspecies and strain assertions
  remain distinct.
- MIBiG BGC0000528 entry version 5 retains AM711867.1:2216380..2224562, ribosomal/RiPP
  classification and CLUSTER_UNSTATED. The own abstract discusses a michiganin gene,
  while its own DataBank list supplies DQ458780. Neither the abstract nor this accession
  label verifies the retained AM711867.1 interval or a strain-specific cluster experiment.
  Different accession strings are not treated as a demonstrated conflict or as aliases.
- The abstract reports growth inhibition of Clavibacter michiganensis subsp. sepedonicus
  by michiganin A. This is qualitative named-product activity context. The pinned
  owner and selected tables contain no quantitative assay or molecular-target assertion
  to verify, and the abstract does not support importing a potency, exact target,
  or assay conditions for this stored structure.
- The exact own-PMC XML request returned HTTP200 and correct own frontmatter, but
  no substantive article body. The original access records success:false and frontmatter_only:true.
  ROOT retained this source failure with six original leaves and prohibited retry/alternate/old
  remaining-phase use. It is a source-availability limit, not a canonical validation
  failure or evidence that the biological claims are false.
- Configured consistency only; independent scientific claim support and unrestricted
  remote authority refresh are not implied.
- FailedQC001 is retained for an explicit separate network-enabled retry; no artifact
  will be overwritten.
- Fresh QC attempt001 failed on public canonical-artifact DNS retrieval after lint
  and before downstream tests. Its actual exit1/log/input capture/root observation
  remain pinned; the selected successful canonical QC attempt002 is separately timed.
  No individual-review validation failure or counter reset is claimed.
- 499non-blocking identifier-label warnings,35configured exceptions and4898no-adapter
  skips remain unverified within this gate.
- The QC test suite reported four skipped tests and two dependency deprecation warnings;
  this pass does not assert skipped checks ran.
- Canonical reproduction retains five unresolved assay-organism annotations,42 withheld
  nonsingle-organism producer claims and161 configured taxon-ID rewrites.
- This QC is a configured consistency gate, not an independent primary-source biological
  or stereochemical verification.
- Native baseline gates establish configured consistency, not independent biological
  production, exact stereochemistry or primary-source adequacy.
- The full configured gate logs retain warnings, skipped tests, identifier exceptions
  and no-adapter pairs; a successful command does not convert these into verified
  scientific claims.
- Ontology caches may be reused by the canonical identifier-label gate. Fresh command
  execution is not proof every remote authority was refreshed.
- Every tracked byte stream/mode and ignored-inclusive corpus/review YAML population
  was checked; external caches and generated bytecode are not asserted to be independently
  byte-pinned.
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
