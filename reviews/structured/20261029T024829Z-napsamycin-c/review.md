# Scientific review of napsamycin C

- Review: 20261029T024829Z-napsamycin-c
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-29T02:34:04.279078Z
- Finished UTC: 2026-10-29T02:48:29.031005Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

napsamycin C: complete local owner/source joins and saved encoding diagnostics are preserved; exact natural congener, producer/locus and assay support remain bounded by the inspected source scope. This partial scientific review retains the unresolved claims and source limits described below.

## Scope And Provenance

Read-only partial scientific review. Exact napsamycin C local structure and retained source provenance, including separately scoped LOTUS occurrences and napsamycin-family biosynthetic evidence. Occurrence is not promoted to production.

Selection: One current unreviewed record selected in canonical path order; official batch90 selection and intake exactly reconcile the frozen owner and source evidence.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-4c0d1526ef | data/natural_products/amino_acids_and_peptides/napsamycin-c.yaml | generated | napsamycin C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-4c0d1526ef | Fresh corpus gate passed:3116 PATHS.tsv rows and3116 files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-4c0d1526ef | Fresh reproduction gate passed:all3116 records are byte-identical to seeding from maintained inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-4c0d1526ef | Fresh deterministic review queue produced8922 rows across12 queues; this is not scientific review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-4c0d1526ef | Fresh configured identifier-label gate passed:13472 canonical,657 synonym and35 exception matches;499 nonblocking mismatches and4898 no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-4c0d1526ef | Fresh full quality gate passed:1024 tests passed,4 skipped,2 dependency warnings;3116 closed-schema records have zero errors; site freshness, reproduction and lockfile checks passed, alongside22 governed artifacts and15 raw inventories. |
| Native strict target validation | passed | True | naturalproductmech:mibig-4c0d1526ef | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Saved encodings and stereochemical resolution | passed | True | naturalproductmech:mibig-4c0d1526ef | Both saved parses reproduce formula C39H50N8O12S, formal charge 0, 1 component, the declared full key and the same normalized Standard InChI. Both canonical SMILES comparisons are false, and no complete atom correspondence was obtained. SMILES has 0 specified and 7 unspecified tetrahedral sites, plus 1 specified and 0 unspecified potential double-bond sites. InChI has 0 specified and 7 unspecified tetrahedral sites, plus 1 specified and 3 unspecified potential double-bond sites. The saved strings contain C(=O)-N versus C(OH)=N representation differences; additional InChI double-bond diagnostics are not automatically missing natural stereochemical assignments. No biological identity is proved by normalization. |
| Exact natural compound and congener scope | unavailable | True | naturalproductmech:mibig-4c0d1526ef | The owner preserves the distinct napsamycin C encoding and its own full InChIKey; the A/B/C/D records are not collapsed. Own PMID21290549 describes a 29-gene napsamycin cluster in Streptomyces sp. DSM5940 and heterologous production of napsamycins and mureidomycins in S. coelicolor M1154. These are family-level product and cluster observations; the abstract does not verify this exact congener, full InChIKey, absolute stereochemistry or quantitative assay. Chemical indexing of napsamycin C in that PubMed record is indexing context and does not provide an atom-mapped structure or transfer a result to another congener. |
| Producer, occurrence and strain scope | unavailable | True | naturalproductmech:mibig-4c0d1526ef | The owner and BGC0000950/version5 row assert Streptomyces sp. DSM5940 (NCBITaxon:991132) as SOURCE_ASSERTION. The abstract independently supports the native cluster context and distinguishes S. coelicolor M1154 as heterologous host and S. roseosporus NRRL15998 as the probe-source comparator. It does not establish a congener-specific producer experiment or an exact current taxonomic/accession version mapping. LOTUS Pseudomonas and S. filamentosus entries remain occurrence assertions, not additional native producers. |
| Own citation and occurrence applicability | unavailable | True | naturalproductmech:mibig-4c0d1526ef | The exact-key LOTUS rows cite DOI10.7164/ANTIBIOTICS.47.595 for Pseudomonas (NCBITaxon:286) and DOI10.1038/SREP14111 for Streptomyces filamentosus (NCBITaxon:67294). Their own primary texts were not inspected. These source-specific occurrences are not established by the DSM5940 family abstract and are not promoted to production. |
| Exact locus and compound-specific biosynthesis | unavailable | True | naturalproductmech:mibig-4c0d1526ef | MIBiG BGC0000950/version5 asserts HQ287563.1 with Heterologous expression and CLUSTER_DEMONSTRATED. Own PMID21290549 describes a 29-gene napsamycin cluster in Streptomyces sp. DSM5940 and heterologous production of napsamycins and mureidomycins in S. coelicolor M1154. These are family-level product and cluster observations; the abstract does not verify this exact congener, full InChIKey, absolute stereochemistry or quantitative assay. The retained ENTRY reference is not an independently inspected modern accession-version/sequence annotation or congener-specific enzyme experiment. Original database grades are preserved; no new protein, locus-coordinate or reaction assignment is inferred. |
| Exact compound assays and targets | unavailable | True | naturalproductmech:mibig-4c0d1526ef | The named exact-key local assay/target arrays contain no measured activity row. PMID21290549 gives family-level translocase-I inhibition context; it supplies no congener-specific potency or direct target assay for this retained encoding. No target/protein accession or quantitative activity is transferred. |
| Mechanism and target representation | unavailable | True | naturalproductmech:mibig-4c0d1526ef | The whole owner contains no inline/referenced causal graph, biosynthetic_pathway or molecular-target annotation; complete current owner and exact local arrays support only that representation observation. Family biosynthetic context could motivate later claim-specific representation, but the inspected abstract does not ground exact organism-specific proteins or every congener reaction. No absence of a mechanism in nature or complete scientific coverage is claimed. |
| Broad filing and classification axes | passed | True | naturalproductmech:mibig-4c0d1526ef | The current filing amino_acids_and_peptides and np_pathway=AMINO_ACIDS_AND_PEPTIDES is compatible at broad level with the retained peptide-containing structure. NPClassifier npclassifier.gnps2.org@2026-09-07 supplies pathway 'Amino acids and Peptides', superclass 'Oligopeptides', class 'Linear peptides' and is_glycoside=true; those exact computational labels match the owner. The separate BGC classes NRPS&#124;other are biosynthetic database assertions. Filing and classifier agreement do not independently verify linearity, glycosylation chemistry, natural origin or exact congener identity. |
| Source versions, evidence placement and clock continuity | passed | True | naturalproductmech:mibig-4c0d1526ef | MIBiG BGC0000950/version5 and NPClassifier npclassifier.gnps2.org@2026-09-07 are retained source/model versions, not publication access dates. All 2 original history entries, exact raw arrays and 37 original AGENTS-context source placements are preserved. Original local parsing, saved diagnostic and publication retrieval clocks remain separate from this later scientific reading. The official intake was reconciled to these unchanged owner and source bytes before this review was authored. |
| Minted identity and external equivalence | unavailable | True | naturalproductmech:mibig-4c0d1526ef | The record retains minted identifier naturalproductmech:mibig-4c0d1526ef and source identity BGC0000950; exact-key local ChEBI rows are empty. This is bounded to the named local tables, not a global authority search. Retained xrefs ['npatlas:NPA01280'] remain database identifiers whose live exact-structure equivalence was not independently checked here. No grounding or synonym replacement is selected. |
| Inspected source extent and unresolved coverage | unavailable | True | naturalproductmech:mibig-4c0d1526ef | The inspected external evidence is saved own PubMed metadata and abstract for PMID21290549, not full primary text, figures, spectra or supplementary material. Current20 source-hold events/116 event leaves/125 held leaves and separate contextual6 remain unchanged and are not assertions that this record's distinct citation routes were attempted. Retrieval clocks are preserved separately from later reading; no new request is selected. |

## Scientific And Domain Assessments

### Saved encodings and stereochemical resolution

consistency: supported. Targets: naturalproductmech:mibig-4c0d1526ef.

Both saved parses reproduce formula C39H50N8O12S, formal charge 0, 1 component, the declared full key and the same normalized Standard InChI. Both canonical SMILES comparisons are false, and no complete atom correspondence was obtained. SMILES has 0 specified and 7 unspecified tetrahedral sites, plus 1 specified and 0 unspecified potential double-bond sites. InChI has 0 specified and 7 unspecified tetrahedral sites, plus 1 specified and 3 unspecified potential double-bond sites. The saved strings contain C(=O)-N versus C(OH)=N representation differences; additional InChI double-bond diagnostics are not automatically missing natural stereochemical assignments. No biological identity is proved by normalization.

### Exact natural compound and congener scope

identity: unknown. Targets: naturalproductmech:mibig-4c0d1526ef.

The owner preserves the distinct napsamycin C encoding and its own full InChIKey; the A/B/C/D records are not collapsed. Own PMID21290549 describes a 29-gene napsamycin cluster in Streptomyces sp. DSM5940 and heterologous production of napsamycins and mureidomycins in S. coelicolor M1154. These are family-level product and cluster observations; the abstract does not verify this exact congener, full InChIKey, absolute stereochemistry or quantitative assay. Chemical indexing of napsamycin C in that PubMed record is indexing context and does not provide an atom-mapped structure or transfer a result to another congener.

### Producer, occurrence and strain scope

provenance: unknown. Targets: naturalproductmech:mibig-4c0d1526ef.

The owner and BGC0000950/version5 row assert Streptomyces sp. DSM5940 (NCBITaxon:991132) as SOURCE_ASSERTION. The abstract independently supports the native cluster context and distinguishes S. coelicolor M1154 as heterologous host and S. roseosporus NRRL15998 as the probe-source comparator. It does not establish a congener-specific producer experiment or an exact current taxonomic/accession version mapping. LOTUS Pseudomonas and S. filamentosus entries remain occurrence assertions, not additional native producers.

### Own citation and occurrence applicability

evidence: unknown. Targets: naturalproductmech:mibig-4c0d1526ef.

The exact-key LOTUS rows cite DOI10.7164/ANTIBIOTICS.47.595 for Pseudomonas (NCBITaxon:286) and DOI10.1038/SREP14111 for Streptomyces filamentosus (NCBITaxon:67294). Their own primary texts were not inspected. These source-specific occurrences are not established by the DSM5940 family abstract and are not promoted to production.

### Exact locus and compound-specific biosynthesis

evidence: unknown. Targets: naturalproductmech:mibig-4c0d1526ef.

MIBiG BGC0000950/version5 asserts HQ287563.1 with Heterologous expression and CLUSTER_DEMONSTRATED. Own PMID21290549 describes a 29-gene napsamycin cluster in Streptomyces sp. DSM5940 and heterologous production of napsamycins and mureidomycins in S. coelicolor M1154. These are family-level product and cluster observations; the abstract does not verify this exact congener, full InChIKey, absolute stereochemistry or quantitative assay. The retained ENTRY reference is not an independently inspected modern accession-version/sequence annotation or congener-specific enzyme experiment. Original database grades are preserved; no new protein, locus-coordinate or reaction assignment is inferred.

### Exact compound assays and targets

evidence: unknown. Targets: naturalproductmech:mibig-4c0d1526ef.

The named exact-key local assay/target arrays contain no measured activity row. PMID21290549 gives family-level translocase-I inhibition context; it supplies no congener-specific potency or direct target assay for this retained encoding. No target/protein accession or quantitative activity is transferred.

### Mechanism and target representation

completeness: unknown. Targets: naturalproductmech:mibig-4c0d1526ef.

The whole owner contains no inline/referenced causal graph, biosynthetic_pathway or molecular-target annotation; complete current owner and exact local arrays support only that representation observation. Family biosynthetic context could motivate later claim-specific representation, but the inspected abstract does not ground exact organism-specific proteins or every congener reaction. No absence of a mechanism in nature or complete scientific coverage is claimed.

### Broad filing and classification axes

representation: supported. Targets: naturalproductmech:mibig-4c0d1526ef.

The current filing amino_acids_and_peptides and np_pathway=AMINO_ACIDS_AND_PEPTIDES is compatible at broad level with the retained peptide-containing structure. NPClassifier npclassifier.gnps2.org@2026-09-07 supplies pathway 'Amino acids and Peptides', superclass 'Oligopeptides', class 'Linear peptides' and is_glycoside=true; those exact computational labels match the owner. The separate BGC classes NRPS&#124;other are biosynthetic database assertions. Filing and classifier agreement do not independently verify linearity, glycosylation chemistry, natural origin or exact congener identity.

### Source versions, evidence placement and clock continuity

provenance: supported. Targets: naturalproductmech:mibig-4c0d1526ef.

MIBiG BGC0000950/version5 and NPClassifier npclassifier.gnps2.org@2026-09-07 are retained source/model versions, not publication access dates. All 2 original history entries, exact raw arrays and 37 original AGENTS-context source placements are preserved. Original local parsing, saved diagnostic and publication retrieval clocks remain separate from this later scientific reading. The official intake was reconciled to these unchanged owner and source bytes before this review was authored.

### Minted identity and external equivalence

grounding: unknown. Targets: naturalproductmech:mibig-4c0d1526ef.

The record retains minted identifier naturalproductmech:mibig-4c0d1526ef and source identity BGC0000950; exact-key local ChEBI rows are empty. This is bounded to the named local tables, not a global authority search. Retained xrefs ['npatlas:NPA01280'] remain database identifiers whose live exact-structure equivalence was not independently checked here. No grounding or synonym replacement is selected.

### Inspected source extent and unresolved coverage

scope: unknown. Targets: naturalproductmech:mibig-4c0d1526ef.

The inspected external evidence is saved own PubMed metadata and abstract for PMID21290549, not full primary text, figures, spectra or supplementary material. Current20 source-hold events/116 event leaves/125 held leaves and separate contextual6 remain unchanged and are not assertions that this record's distinct citation routes were attempted. Retrieval clocks are preserved separately from later reading; no new request is selected.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI899-LOCAL | /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/napsamycin-c.yaml; whole owner; chemical_structure, source_concepts, producer_organisms, occurrences, biosynthetic_gene_clusters, np_classification, xrefs and curation_history | context_only | Whole napsamycin C owner and original history were read. The declared full key is MFEPAAMYDYMBSN-XHPQRKPJSA-N; local source assertions remain distinct from independently verified natural identity. |
| SCI899-ROWS | /private/tmp/npm-review-work/shared-next-batch090-tentative/review-support-tentative90-owner-source-reconnaissance-DATA-001.json; /records/8/retained_rows, supplemental_rows and row_guards; complete exact-key joins across nine named local tables | supports | Literal local-source provenance and classification reconstruction only: 4 rows across nine arrays, with table counts {'mibig_compounds': 1, 'lotus_occurrences': 2, 'chebi_structures': 0, 'chebi_origins': 0, 'npclassifier': 1, 'cyanometdb_occurrences': 0, 'pubchem_bioassay': 0, 'bindingdb_targets': 0, 'antibioticmech_inchikeys': 0}. Empty exact-key arrays and blank-AID sentinels do not establish biological absence or assay outcomes. |
| SCI899-ENCODINGS | /private/tmp/npm-review-work/shared-next-batch090-tentative/source-science-preparation/native-tentative90-ten-owner-dual-encoding-results-001.json; /records/8/smiles, inchi, stereo_counts, comparisons and atom_correspondence | supports | Both saved parses reproduce formula C39H50N8O12S, formal charge 0, 1 component, the declared full key and the same normalized Standard InChI. Both canonical SMILES comparisons are false, and no complete atom correspondence was obtained. SMILES has 0 specified and 7 unspecified tetrahedral sites, plus 1 specified and 0 unspecified potential double-bond sites. InChI has 0 specified and 7 unspecified tetrahedral sites, plus 1 specified and 3 unspecified potential double-bond sites. The saved strings contain C(=O)-N versus C(OH)=N representation differences; additional InChI double-bond diagnostics are not automatically missing natural stereochemical assignments. No biological identity is proved by normalization. |
| SCI899-PUBMED | /private/tmp/npm-review-work/shared-next-batch090-tentative/literature-preparation/public-metadata-five-PubMed-001/pmid-21290549.xml; ./PubmedArticle/MedlineCitation/Article, ChemicalList and ./PubmedArticle/PubmedData/ArticleIdList; whole own title and abstract availability | partial | Own PMID21290549 describes a 29-gene napsamycin cluster in Streptomyces sp. DSM5940 and heterologous production of napsamycins and mureidomycins in S. coelicolor M1154. These are family-level product and cluster observations; the abstract does not verify this exact congener, full InChIKey, absolute stereochemistry or quantitative assay. Chemical indexing separately lists mureidomycin A/B and napsamycin C; this is not synonym or atom-graph proof. |

## Limits And Additional Notes

- The owner preserves the distinct napsamycin C encoding and its own full InChIKey; the A/B/C/D records are not collapsed. Own PMID21290549 describes a 29-gene napsamycin cluster in Streptomyces sp. DSM5940 and heterologous production of napsamycins and mureidomycins in S. coelicolor M1154. These are family-level product and cluster observations; the abstract does not verify this exact congener, full InChIKey, absolute stereochemistry or quantitative assay. Chemical indexing of napsamycin C in that PubMed record is indexing context and does not provide an atom-mapped structure or transfer a result to another congener.
- The owner and BGC0000950/version5 row assert Streptomyces sp. DSM5940 (NCBITaxon:991132) as SOURCE_ASSERTION. The abstract independently supports the native cluster context and distinguishes S. coelicolor M1154 as heterologous host and S. roseosporus NRRL15998 as the probe-source comparator. It does not establish a congener-specific producer experiment or an exact current taxonomic/accession version mapping. LOTUS Pseudomonas and S. filamentosus entries remain occurrence assertions, not additional native producers.
- MIBiG BGC0000950/version5 asserts HQ287563.1 with Heterologous expression and CLUSTER_DEMONSTRATED. Own PMID21290549 describes a 29-gene napsamycin cluster in Streptomyces sp. DSM5940 and heterologous production of napsamycins and mureidomycins in S. coelicolor M1154. These are family-level product and cluster observations; the abstract does not verify this exact congener, full InChIKey, absolute stereochemistry or quantitative assay. The retained ENTRY reference is not an independently inspected modern accession-version/sequence annotation or congener-specific enzyme experiment. Original database grades are preserved; no new protein, locus-coordinate or reaction assignment is inferred.
- The named exact-key local assay/target arrays contain no measured activity row. PMID21290549 gives family-level translocase-I inhibition context; it supplies no congener-specific potency or direct target assay for this retained encoding. No target/protein accession or quantitative activity is transferred.
- The inspected external evidence is saved own PubMed metadata and abstract for PMID21290549, not full primary text, figures, spectra or supplementary material. Current20 source-hold events/116 event leaves/125 held leaves and separate contextual6 remain unchanged and are not assertions that this record's distinct citation routes were attempted. Retrieval clocks are preserved separately from later reading; no new request is selected.
- Scientific coverage is partial. Official intake and native strict validation establish configured consistency; they do not resolve the source limitations described here. No scientific corpus record or maintained source was changed.
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
review_id: 20261029T024829Z-napsamycin-c
title: Scientific review of napsamycin C
started_at: '2026-10-29T02:34:04.279078Z'
finished_at: '2026-10-29T02:48:29.031005Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: 'napsamycin C: complete local owner/source joins and saved encoding diagnostics
  are preserved; exact natural congener, producer/locus and assay support remain bounded
  by the inspected source scope. This partial scientific review retains the unresolved
  claims and source limits described below.'
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
  - path: data/natural_products/amino_acids_and_peptides/napsamycin-c.yaml
    sha256: 64faa7d2d4bc82a2a26bbda2ea73321c886134250d11dc545c82848e9ef38c6f
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
- target_id: naturalproductmech:mibig-4c0d1526ef
  path: data/natural_products/amino_acids_and_peptides/napsamycin-c.yaml
  label: napsamycin C
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
  description: Read-only partial scientific review. Exact napsamycin C local structure
    and retained source provenance, including separately scoped LOTUS occurrences
    and napsamycin-family biosynthetic evidence. Occurrence is not promoted to production.
  selection: One current unreviewed record selected in canonical path order; official
    batch90 selection and intake exactly reconcile the frozen owner and source evidence.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  exclusions:
  - target: Full primary structure, experimental and exact biological-source verification
    reason: The family abstract does not assign every exact congener or occurrence
      taxon. Pseudomonas genus-level and Streptomyces filamentosus occurrence rows
      do not independently establish biosynthetic production.
  - target: Fresh external authority resolution
    reason: Retained identifiers and local source joins were inspected. Complete live
      chemical, taxon and protein authority equivalence was not established.
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
  - naturalproductmech:mibig-4c0d1526ef
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
  - naturalproductmech:mibig-4c0d1526ef
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
  - naturalproductmech:mibig-4c0d1526ef
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
  - naturalproductmech:mibig-4c0d1526ef
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
  - naturalproductmech:mibig-4c0d1526ef
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/napsamycin-c.yaml
    --out /private/tmp/npm-review-work/899/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-29T02:34:05.626869Z. Original
    receipt: /private/tmp/npm-review-work/899/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
- check_id: SCI899-ENCODINGS
  name: Saved encodings and stereochemical resolution
  status: passed
  required: true
  summary: Both saved parses reproduce formula C39H50N8O12S, formal charge 0, 1 component,
    the declared full key and the same normalized Standard InChI. Both canonical SMILES
    comparisons are false, and no complete atom correspondence was obtained. SMILES
    has 0 specified and 7 unspecified tetrahedral sites, plus 1 specified and 0 unspecified
    potential double-bond sites. InChI has 0 specified and 7 unspecified tetrahedral
    sites, plus 1 specified and 3 unspecified potential double-bond sites. The saved
    strings contain C(=O)-N versus C(OH)=N representation differences; additional
    InChI double-bond diagnostics are not automatically missing natural stereochemical
    assignments. No biological identity is proved by normalization.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ENCODINGS
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
- check_id: SCI899-IDENTITY
  name: Exact natural compound and congener scope
  status: unavailable
  required: true
  summary: The owner preserves the distinct napsamycin C encoding and its own full
    InChIKey; the A/B/C/D records are not collapsed. Own PMID21290549 describes a
    29-gene napsamycin cluster in Streptomyces sp. DSM5940 and heterologous production
    of napsamycins and mureidomycins in S. coelicolor M1154. These are family-level
    product and cluster observations; the abstract does not verify this exact congener,
    full InChIKey, absolute stereochemistry or quantitative assay. Chemical indexing
    of napsamycin C in that PubMed record is indexing context and does not provide
    an atom-mapped structure or transfer a result to another congener.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
  - SCI899-ENCODINGS
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
- check_id: SCI899-PRODUCER
  name: Producer, occurrence and strain scope
  status: unavailable
  required: true
  summary: The owner and BGC0000950/version5 row assert Streptomyces sp. DSM5940 (NCBITaxon:991132)
    as SOURCE_ASSERTION. The abstract independently supports the native cluster context
    and distinguishes S. coelicolor M1154 as heterologous host and S. roseosporus
    NRRL15998 as the probe-source comparator. It does not establish a congener-specific
    producer experiment or an exact current taxonomic/accession version mapping. LOTUS
    Pseudomonas and S. filamentosus entries remain occurrence assertions, not additional
    native producers.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
- check_id: SCI899-OCCURRENCE
  name: Own citation and occurrence applicability
  status: unavailable
  required: true
  summary: The exact-key LOTUS rows cite DOI10.7164/ANTIBIOTICS.47.595 for Pseudomonas
    (NCBITaxon:286) and DOI10.1038/SREP14111 for Streptomyces filamentosus (NCBITaxon:67294).
    Their own primary texts were not inspected. These source-specific occurrences
    are not established by the DSM5940 family abstract and are not promoted to production.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
- check_id: SCI899-BIOSYNTHESIS
  name: Exact locus and compound-specific biosynthesis
  status: unavailable
  required: true
  summary: MIBiG BGC0000950/version5 asserts HQ287563.1 with Heterologous expression
    and CLUSTER_DEMONSTRATED. Own PMID21290549 describes a 29-gene napsamycin cluster
    in Streptomyces sp. DSM5940 and heterologous production of napsamycins and mureidomycins
    in S. coelicolor M1154. These are family-level product and cluster observations;
    the abstract does not verify this exact congener, full InChIKey, absolute stereochemistry
    or quantitative assay. The retained ENTRY reference is not an independently inspected
    modern accession-version/sequence annotation or congener-specific enzyme experiment.
    Original database grades are preserved; no new protein, locus-coordinate or reaction
    assignment is inferred.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
- check_id: SCI899-BIOACTIVITY
  name: Exact compound assays and targets
  status: unavailable
  required: true
  summary: The named exact-key local assay/target arrays contain no measured activity
    row. PMID21290549 gives family-level translocase-I inhibition context; it supplies
    no congener-specific potency or direct target assay for this retained encoding.
    No target/protein accession or quantitative activity is transferred.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
- check_id: SCI899-GRAPH
  name: Mechanism and target representation
  status: unavailable
  required: true
  summary: The whole owner contains no inline/referenced causal graph, biosynthetic_pathway
    or molecular-target annotation; complete current owner and exact local arrays
    support only that representation observation. Family biosynthetic context could
    motivate later claim-specific representation, but the inspected abstract does
    not ground exact organism-specific proteins or every congener reaction. No absence
    of a mechanism in nature or complete scientific coverage is claimed.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
- check_id: SCI899-CLASSIFICATION
  name: Broad filing and classification axes
  status: passed
  required: true
  summary: The current filing amino_acids_and_peptides and np_pathway=AMINO_ACIDS_AND_PEPTIDES
    is compatible at broad level with the retained peptide-containing structure. NPClassifier
    npclassifier.gnps2.org@2026-09-07 supplies pathway 'Amino acids and Peptides',
    superclass 'Oligopeptides', class 'Linear peptides' and is_glycoside=true; those
    exact computational labels match the owner. The separate BGC classes NRPS|other
    are biosynthetic database assertions. Filing and classifier agreement do not independently
    verify linearity, glycosylation chemistry, natural origin or exact congener identity.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
- check_id: SCI899-PROVENANCE
  name: Source versions, evidence placement and clock continuity
  status: passed
  required: true
  summary: MIBiG BGC0000950/version5 and NPClassifier npclassifier.gnps2.org@2026-09-07
    are retained source/model versions, not publication access dates. All 2 original
    history entries, exact raw arrays and 37 original AGENTS-context source placements
    are preserved. Original local parsing, saved diagnostic and publication retrieval
    clocks remain separate from this later scientific reading. The official intake
    was reconciled to these unchanged owner and source bytes before this review was
    authored.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
- check_id: SCI899-GROUNDING
  name: Minted identity and external equivalence
  status: unavailable
  required: true
  summary: The record retains minted identifier naturalproductmech:mibig-4c0d1526ef
    and source identity BGC0000950; exact-key local ChEBI rows are empty. This is
    bounded to the named local tables, not a global authority search. Retained xrefs
    ['npatlas:NPA01280'] remain database identifiers whose live exact-structure equivalence
    was not independently checked here. No grounding or synonym replacement is selected.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
- check_id: SCI899-AVAILABILITY
  name: Inspected source extent and unresolved coverage
  status: unavailable
  required: true
  summary: The inspected external evidence is saved own PubMed metadata and abstract
    for PMID21290549, not full primary text, figures, spectra or supplementary material.
    Current20 source-hold events/116 event leaves/125 held leaves and separate contextual6
    remain unchanged and are not assertions that this record's distinct citation routes
    were attempted. Retrieval clocks are preserved separately from later reading;
    no new request is selected.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
  scope_note: Scientific coverage is partial. Official intake and native strict validation
    establish configured consistency; they do not resolve the source limitations described
    here. No scientific corpus record or maintained source was changed.
evidence:
- evidence_id: SCI899-LOCAL
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/napsamycin-c.yaml
  locator: whole owner; chemical_structure, source_concepts, producer_organisms, occurrences,
    biosynthetic_gene_clusters, np_classification, xrefs and curation_history
  accessed_at: '2026-10-29T01:32:49.148943Z'
  snapshot_sha256: 64faa7d2d4bc82a2a26bbda2ea73321c886134250d11dc545c82848e9ef38c6f
  support: context_only
  summary: Whole napsamycin C owner and original history were read. The declared full
    key is MFEPAAMYDYMBSN-XHPQRKPJSA-N; local source assertions remain distinct from
    independently verified natural identity.
- evidence_id: SCI899-ROWS
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch090-tentative/review-support-tentative90-owner-source-reconnaissance-DATA-001.json
  locator: /records/8/retained_rows, supplemental_rows and row_guards; complete exact-key
    joins across nine named local tables
  accessed_at: '2026-10-29T01:32:49.148943Z'
  snapshot_sha256: e3143ea89c8b59dabbc5bea95021b1dfc9043a14c02ee19fd57914c053a96a0d
  support: supports
  summary: 'Literal local-source provenance and classification reconstruction only:
    4 rows across nine arrays, with table counts {''mibig_compounds'': 1, ''lotus_occurrences'':
    2, ''chebi_structures'': 0, ''chebi_origins'': 0, ''npclassifier'': 1, ''cyanometdb_occurrences'':
    0, ''pubchem_bioassay'': 0, ''bindingdb_targets'': 0, ''antibioticmech_inchikeys'':
    0}. Empty exact-key arrays and blank-AID sentinels do not establish biological
    absence or assay outcomes.'
- evidence_id: SCI899-ENCODINGS
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch090-tentative/source-science-preparation/native-tentative90-ten-owner-dual-encoding-results-001.json
  locator: /records/8/smiles, inchi, stereo_counts, comparisons and atom_correspondence
  accessed_at: '2026-10-29T01:47:58.104996Z'
  snapshot_sha256: 170ac63b58dee88ccc18cb595f92443113ef53aec6e672f563309dc801dc5a32
  support: supports
  summary: Both saved parses reproduce formula C39H50N8O12S, formal charge 0, 1 component,
    the declared full key and the same normalized Standard InChI. Both canonical SMILES
    comparisons are false, and no complete atom correspondence was obtained. SMILES
    has 0 specified and 7 unspecified tetrahedral sites, plus 1 specified and 0 unspecified
    potential double-bond sites. InChI has 0 specified and 7 unspecified tetrahedral
    sites, plus 1 specified and 3 unspecified potential double-bond sites. The saved
    strings contain C(=O)-N versus C(OH)=N representation differences; additional
    InChI double-bond diagnostics are not automatically missing natural stereochemical
    assignments. No biological identity is proved by normalization.
- evidence_id: SCI899-PUBMED
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch090-tentative/literature-preparation/public-metadata-five-PubMed-001/pmid-21290549.xml
  locator: ./PubmedArticle/MedlineCitation/Article, ChemicalList and ./PubmedArticle/PubmedData/ArticleIdList;
    whole own title and abstract availability
  accessed_at: '2026-10-29T02:00:25.306935Z'
  snapshot_sha256: 3d5126d79bcc1db6ada831ecc679e6f27c8986f0722c847e422c86f741dae3bb
  support: partial
  summary: Own PMID21290549 describes a 29-gene napsamycin cluster in Streptomyces
    sp. DSM5940 and heterologous production of napsamycins and mureidomycins in S.
    coelicolor M1154. These are family-level product and cluster observations; the
    abstract does not verify this exact congener, full InChIKey, absolute stereochemistry
    or quantitative assay. Chemical indexing separately lists mureidomycin A/B and
    napsamycin C; this is not synonym or atom-graph proof.
assessments:
- assessment_id: SCI899-ENCODINGS
  area: consistency
  topic: Saved encodings and stereochemical resolution
  outcome: supported
  summary: Both saved parses reproduce formula C39H50N8O12S, formal charge 0, 1 component,
    the declared full key and the same normalized Standard InChI. Both canonical SMILES
    comparisons are false, and no complete atom correspondence was obtained. SMILES
    has 0 specified and 7 unspecified tetrahedral sites, plus 1 specified and 0 unspecified
    potential double-bond sites. InChI has 0 specified and 7 unspecified tetrahedral
    sites, plus 1 specified and 3 unspecified potential double-bond sites. The saved
    strings contain C(=O)-N versus C(OH)=N representation differences; additional
    InChI double-bond diagnostics are not automatically missing natural stereochemical
    assignments. No biological identity is proved by normalization.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ENCODINGS
  dimensions:
  - name: stereochemical_resolution
    value: SMILES has 0 specified and 7 unspecified tetrahedral sites, plus 1 specified
      and 0 unspecified potential double-bond sites. InChI has 0 specified and 7 unspecified
      tetrahedral sites, plus 1 specified and 3 unspecified potential double-bond
      sites. Retained stereo_complete=False.
    definition: Literal flag and separate saved explicit-graph diagnostics; no normalized-key
      or potential-site equality proves experimental configuration.
    evidence_ids:
    - SCI899-LOCAL
    - SCI899-ENCODINGS
- assessment_id: SCI899-IDENTITY
  area: identity
  topic: Exact natural compound and congener scope
  outcome: unknown
  summary: The owner preserves the distinct napsamycin C encoding and its own full
    InChIKey; the A/B/C/D records are not collapsed. Own PMID21290549 describes a
    29-gene napsamycin cluster in Streptomyces sp. DSM5940 and heterologous production
    of napsamycins and mureidomycins in S. coelicolor M1154. These are family-level
    product and cluster observations; the abstract does not verify this exact congener,
    full InChIKey, absolute stereochemistry or quantitative assay. Chemical indexing
    of napsamycin C in that PubMed record is indexing context and does not provide
    an atom-mapped structure or transfer a result to another congener.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
  - SCI899-ENCODINGS
- assessment_id: SCI899-PRODUCER
  area: provenance
  topic: Producer, occurrence and strain scope
  outcome: unknown
  summary: The owner and BGC0000950/version5 row assert Streptomyces sp. DSM5940 (NCBITaxon:991132)
    as SOURCE_ASSERTION. The abstract independently supports the native cluster context
    and distinguishes S. coelicolor M1154 as heterologous host and S. roseosporus
    NRRL15998 as the probe-source comparator. It does not establish a congener-specific
    producer experiment or an exact current taxonomic/accession version mapping. LOTUS
    Pseudomonas and S. filamentosus entries remain occurrence assertions, not additional
    native producers.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
  dimensions:
  - name: taxon_strain
    value: The owner and BGC0000950/version5 row assert Streptomyces sp. DSM5940 (NCBITaxon:991132)
      as SOURCE_ASSERTION. The abstract independently supports the native cluster
      context and distinguishes S. coelicolor M1154 as heterologous host and S. roseosporus
      NRRL15998 as the probe-source comparator. It does not establish a congener-specific
      producer experiment or an exact current taxonomic/accession version mapping.
      LOTUS Pseudomonas and S. filamentosus entries remain occurrence assertions,
      not additional native producers.
    definition: Source-specific native producer, host, comparator and occurrence roles;
      no unsupported taxonomic/strain equivalence.
    evidence_ids:
    - SCI899-LOCAL
    - SCI899-ROWS
    - SCI899-PUBMED
- assessment_id: SCI899-OCCURRENCE
  area: evidence
  topic: Own citation and occurrence applicability
  outcome: unknown
  summary: The exact-key LOTUS rows cite DOI10.7164/ANTIBIOTICS.47.595 for Pseudomonas
    (NCBITaxon:286) and DOI10.1038/SREP14111 for Streptomyces filamentosus (NCBITaxon:67294).
    Their own primary texts were not inspected. These source-specific occurrences
    are not established by the DSM5940 family abstract and are not promoted to production.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
- assessment_id: SCI899-BIOSYNTHESIS
  area: evidence
  topic: Exact locus and compound-specific biosynthesis
  outcome: unknown
  summary: MIBiG BGC0000950/version5 asserts HQ287563.1 with Heterologous expression
    and CLUSTER_DEMONSTRATED. Own PMID21290549 describes a 29-gene napsamycin cluster
    in Streptomyces sp. DSM5940 and heterologous production of napsamycins and mureidomycins
    in S. coelicolor M1154. These are family-level product and cluster observations;
    the abstract does not verify this exact congener, full InChIKey, absolute stereochemistry
    or quantitative assay. The retained ENTRY reference is not an independently inspected
    modern accession-version/sequence annotation or congener-specific enzyme experiment.
    Original database grades are preserved; no new protein, locus-coordinate or reaction
    assignment is inferred.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
  dimensions:
  - name: evidence_tier
    value: Retained DATABASE_ASSERTION; producer SOURCE_ASSERTION; locus CLUSTER_DEMONSTRATED;
      inspected publication scope own abstract family context
    definition: Database grade, bibliographic identity, family context and exact-congener
      experimental support remain separate.
    evidence_ids:
    - SCI899-LOCAL
    - SCI899-ROWS
    - SCI899-PUBMED
- assessment_id: SCI899-BIOACTIVITY
  area: evidence
  topic: Exact compound assays and targets
  outcome: unknown
  summary: The named exact-key local assay/target arrays contain no measured activity
    row. PMID21290549 gives family-level translocase-I inhibition context; it supplies
    no congener-specific potency or direct target assay for this retained encoding.
    No target/protein accession or quantitative activity is transferred.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
- assessment_id: SCI899-GRAPH
  area: completeness
  topic: Mechanism and target representation
  outcome: unknown
  summary: The whole owner contains no inline/referenced causal graph, biosynthetic_pathway
    or molecular-target annotation; complete current owner and exact local arrays
    support only that representation observation. Family biosynthetic context could
    motivate later claim-specific representation, but the inspected abstract does
    not ground exact organism-specific proteins or every congener reaction. No absence
    of a mechanism in nature or complete scientific coverage is claimed.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
- assessment_id: SCI899-CLASSIFICATION
  area: representation
  topic: Broad filing and classification axes
  outcome: supported
  summary: The current filing amino_acids_and_peptides and np_pathway=AMINO_ACIDS_AND_PEPTIDES
    is compatible at broad level with the retained peptide-containing structure. NPClassifier
    npclassifier.gnps2.org@2026-09-07 supplies pathway 'Amino acids and Peptides',
    superclass 'Oligopeptides', class 'Linear peptides' and is_glycoside=true; those
    exact computational labels match the owner. The separate BGC classes NRPS|other
    are biosynthetic database assertions. Filing and classifier agreement do not independently
    verify linearity, glycosylation chemistry, natural origin or exact congener identity.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
- assessment_id: SCI899-PROVENANCE
  area: provenance
  topic: Source versions, evidence placement and clock continuity
  outcome: supported
  summary: MIBiG BGC0000950/version5 and NPClassifier npclassifier.gnps2.org@2026-09-07
    are retained source/model versions, not publication access dates. All 2 original
    history entries, exact raw arrays and 37 original AGENTS-context source placements
    are preserved. Original local parsing, saved diagnostic and publication retrieval
    clocks remain separate from this later scientific reading. The official intake
    was reconciled to these unchanged owner and source bytes before this review was
    authored.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  dimensions:
  - name: source_version
    value: MIBiG BGC0000950/version5; NPClassifier npclassifier.gnps2.org@2026-09-07
    definition: Original database/model versions and immutable history, separate from
      retrieval and later reading clocks.
    evidence_ids:
    - SCI899-LOCAL
    - SCI899-ROWS
- assessment_id: SCI899-GROUNDING
  area: grounding
  topic: Minted identity and external equivalence
  outcome: unknown
  summary: The record retains minted identifier naturalproductmech:mibig-4c0d1526ef
    and source identity BGC0000950; exact-key local ChEBI rows are empty. This is
    bounded to the named local tables, not a global authority search. Retained xrefs
    ['npatlas:NPA01280'] remain database identifiers whose live exact-structure equivalence
    was not independently checked here. No grounding or synonym replacement is selected.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
- assessment_id: SCI899-AVAILABILITY
  area: scope
  topic: Inspected source extent and unresolved coverage
  outcome: unknown
  summary: The inspected external evidence is saved own PubMed metadata and abstract
    for PMID21290549, not full primary text, figures, spectra or supplementary material.
    Current20 source-hold events/116 event leaves/125 held leaves and separate contextual6
    remain unchanged and are not assertions that this record's distinct citation routes
    were attempted. Retrieval clocks are preserved separately from later reading;
    no new request is selected.
  target_ids:
  - naturalproductmech:mibig-4c0d1526ef
  evidence_ids:
  - SCI899-LOCAL
  - SCI899-ROWS
  - SCI899-PUBMED
findings: []
actions: []
limitations:
- The owner preserves the distinct napsamycin C encoding and its own full InChIKey;
  the A/B/C/D records are not collapsed. Own PMID21290549 describes a 29-gene napsamycin
  cluster in Streptomyces sp. DSM5940 and heterologous production of napsamycins and
  mureidomycins in S. coelicolor M1154. These are family-level product and cluster
  observations; the abstract does not verify this exact congener, full InChIKey, absolute
  stereochemistry or quantitative assay. Chemical indexing of napsamycin C in that
  PubMed record is indexing context and does not provide an atom-mapped structure
  or transfer a result to another congener.
- The owner and BGC0000950/version5 row assert Streptomyces sp. DSM5940 (NCBITaxon:991132)
  as SOURCE_ASSERTION. The abstract independently supports the native cluster context
  and distinguishes S. coelicolor M1154 as heterologous host and S. roseosporus NRRL15998
  as the probe-source comparator. It does not establish a congener-specific producer
  experiment or an exact current taxonomic/accession version mapping. LOTUS Pseudomonas
  and S. filamentosus entries remain occurrence assertions, not additional native
  producers.
- MIBiG BGC0000950/version5 asserts HQ287563.1 with Heterologous expression and CLUSTER_DEMONSTRATED.
  Own PMID21290549 describes a 29-gene napsamycin cluster in Streptomyces sp. DSM5940
  and heterologous production of napsamycins and mureidomycins in S. coelicolor M1154.
  These are family-level product and cluster observations; the abstract does not verify
  this exact congener, full InChIKey, absolute stereochemistry or quantitative assay.
  The retained ENTRY reference is not an independently inspected modern accession-version/sequence
  annotation or congener-specific enzyme experiment. Original database grades are
  preserved; no new protein, locus-coordinate or reaction assignment is inferred.
- The named exact-key local assay/target arrays contain no measured activity row.
  PMID21290549 gives family-level translocase-I inhibition context; it supplies no
  congener-specific potency or direct target assay for this retained encoding. No
  target/protein accession or quantitative activity is transferred.
- The inspected external evidence is saved own PubMed metadata and abstract for PMID21290549,
  not full primary text, figures, spectra or supplementary material. Current20 source-hold
  events/116 event leaves/125 held leaves and separate contextual6 remain unchanged
  and are not assertions that this record's distinct citation routes were attempted.
  Retrieval clocks are preserved separately from later reading; no new request is
  selected.
- Scientific coverage is partial. Official intake and native strict validation establish
  configured consistency; they do not resolve the source limitations described here.
  No scientific corpus record or maintained source was changed.
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
