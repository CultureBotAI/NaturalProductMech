# Scientific review of muraymycin C1

- Review: 20261029T011323Z-muraymycin-c1
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-29T01:01:01.272318Z
- Finished UTC: 2026-10-29T01:13:23.639006Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

muraymycin C1 retains internally reproducible normalized InChI/key diagnostics with distinct canonical representations and no complete atom map. The own 2011 abstract supplies muraymycin-family production and locus context, while the 2002/2018 metadata supplies bibliographic scope. Exact C1 structure, native-versus-mutant production and assay applicability remain unresolved. The current official intake passed; this partial assessment records the remaining scientific limits.

## Scope And Provenance

Read-only scientific review of the exact muraymycin C1 owner, complete retained source rows, saved dual-encoding diagnostics, the2011 biosynthesis abstract and2002/2018 bibliographic metadata. Family-level production/inactivation support remains distinct from exact C1 structure, native-versus-mutant provenance and pure-compound activity.

Selection: One current unreviewed record selected in canonical path order; official batch89 selection and intake exactly reconcile the frozen owner and source evidence.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-9913db0837 | data/natural_products/amino_acids_and_peptides/muraymycin-c1.yaml | generated | muraymycin C1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-9913db0837 | Fresh corpus gate passed:3116 PATHS.tsv rows and3116 files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-9913db0837 | Fresh reproduction gate passed:all3116 records are byte-identical to seeding from maintained inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-9913db0837 | Fresh deterministic review queue produced8922 rows across12 queues; this is not scientific review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-9913db0837 | Fresh configured identifier-label gate passed:13472 canonical,657 synonym and35 exception matches;499 nonblocking mismatches and4898 no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-9913db0837 | Fresh full quality gate passed:1024 tests passed,4 skipped,2 dependency warnings;3116 closed-schema records have zero errors; site freshness, reproduction and lockfile checks passed, alongside22 governed artifacts and15 raw inventories. |
| Native strict target validation | passed | True | naturalproductmech:mibig-9913db0837 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Saved encodings and stereochemical resolution | passed | True | naturalproductmech:mibig-9913db0837 | Both saved parses reproduce formula C38H63N11O17, formal charge 0, one connected component, the declared key and the same normalized Standard InChI. Both canonical SMILES comparisons are false, and the complete atom map is empty. Both parses have 15 specified tetrahedral sites. The SMILES parse reports one unspecified potential double-bond site and the InChI parse reports four. Representation-dependent double-bond flags do not establish a wrong natural stereoisomer. No biological identity follows from these diagnostics. |
| Exact natural compound and configured form | unavailable | True | naturalproductmech:mibig-9913db0837 | Muraymycin C1 is represented by one configured glycosylated peptide graph with formula C38H63N11O17 and key GOFOFDWFFIGTML-IZAYEQDHSA-N, matching its retained MIBiG strings. The inspected 2011 abstract and the 2002/2018 titles concern muraymycins without supplying a complete C1 graph-to-compound/configuration map. The two saved encodings normalize to one InChI while their carbonyl/imine and heterocycle representations differ. Exact natural C1 correspondence remains unresolved; no replacement graph or wrong-isomer finding follows. |
| Producer, occurrence and strain scope | unavailable | True | naturalproductmech:mibig-9913db0837 | MIBiG BGC0001020/version 5 retains Streptomyces sp. NRRL 30471, NCBITaxon:996287, as SOURCE_ASSERTION. Own PMID21180767 reports muraymycin production by that strain at family level. The 2018 own title refers to mutant strains of the same named strain, while LOTUS occurrence rows are genus-level Streptomyces. Exact C1 production by the native versus modified strains and taxon-ID validation remain unverified; no heterologous host or engineered derivative is equated with this owner. |
| Citation identity and exact occurrence applicability | unavailable | True | naturalproductmech:mibig-9913db0837 | All three retained genus-level Streptomyces occurrence citations now have own bibliographic identity support: the 2018 mutant-strain DOI, the 2002 muraymycin-structure DOI and the 2011 biosynthesis PubMed article with DOI10.1039/c0mb00237b. That corroborates the cited works, not each full-key compound–organism relationship. Family titles and strain-level abstract claims do not automatically resolve every genus-level C1 occurrence. |
| Exact locus and compound-specific biosynthesis | unavailable | True | naturalproductmech:mibig-9913db0837 | The retained active BGC0001020/version 5 row is marked questionable quality and unknown completeness, carries NRPS and PKS classes, and records HQ257512.1 without locus coordinates or locus-method entries. Own PMID21180767 reports loss of muraymycin production after independent gene inactivations and has databank accession HQ257512. This is substantive family-level locus evidence, but the inspected abstract does not establish the exact C1 graph, retained accession version or compound-specific experiment. Preserve CLUSTER_UNSTATED for the retained owner claim pending that correspondence; do not infer that the publication lacks a mechanism. |
| Compound-specific assays and target evidence | unavailable | True | naturalproductmech:mibig-9913db0837 | The 2011 abstract describes muraymycin as a translocase I inhibitor; the 2002 title names peptidoglycan biosynthesis inhibitors and the 2018 title names antibacterial muraymycins. These are family-level statements. No inspected pure-C1 assay, target binding result, potency value, unit or experimental setting supports a new owner annotation. The local owner and exact-key assay/target rows contain none; this does not establish inactivity or absence of literature evidence. |
| Pathway, target and causal-graph completeness | unavailable | True | naturalproductmech:mibig-9913db0837 | The whole owner contains no biosynthetic_pathway, molecular_targets, bioactivities, inline causal_graphs or causal_graph_refs, and the nine-table exact-key joins contain no assay/target evidence. No causal edge or protein identity can be populated from a bibliographic title. The family-level inactivation statement is retained as a reading limitation rather than converted into an exact C1 pathway. Missing optional mechanism fields are a coverage limit, not a finding that the compound lacks a mechanism. |
| Broad filing and asserted classification axes | passed | True | naturalproductmech:mibig-9913db0837 | The file is in amino_acids_and_peptides and retains NPClassifier pathway Amino acids and Peptides, superclass Oligopeptides, class Linear peptides and is_glycoside=true. The stored peptide-containing representation and retained classifier row are compatible with that broad filing. NRPS and PKS remain separate source-asserted biosynthetic classes; computed filing is not proof of natural identity or biosynthetic causality. |
| Versions, evidence placement and current intake continuity | passed | True | naturalproductmech:mibig-9913db0837 | MIBiG BGC0001020/version 5 and NPClassifier npclassifier.gnps2.org@2026-09-07 are retained source versions. Two seed-history events remain unchanged. All nine raw-table joins and the current official intake resolved owner/six source arrays were compared literally. Each actual inspection captures 37 source inputs, including regular AGENTS.md; row counts and source-input counts are different. The original diagnostic/retrieval/intake clocks remain distinct from this scientific reading. Publication dates do not certify current database versions. |
| Minted identity and external equivalence | unavailable | True | naturalproductmech:mibig-9913db0837 | The minted identifier and BGC0001020/version 5 source concept remain linked to the retained C1 graph. NPAtlas NPA06302 is an unverified retained cross-reference. Own PMID21180767 verifies DOI10.1039/c0mb00237b and databank HQ257512 as publication identifiers; it does not itself establish NPAtlas equivalence, the HQ257512.1 version content or a chemical synonym. The historical ChEBI grounding assertion was not independently renewed. |
| Inspected source extent and unresolved coverage | unavailable | True | naturalproductmech:mibig-9913db0837 | The inspected publication evidence comprises the own 2011 PubMed abstract/databank fields and the own Crossref metadata of the 2002 and 2018 works. The two Crossref responses supply no abstract. Full article structure figures, supplementary material, compound tables, assay methods and external taxon/chemical authorities were not inspected. Abstract omission is not a claim that the full articles omit C1 or relevant experiments. |

## Scientific And Domain Assessments

### Saved encodings and stereochemical resolution

consistency: supported. Targets: naturalproductmech:mibig-9913db0837.

Both saved parses reproduce formula C38H63N11O17, formal charge 0, one connected component, the declared key and the same normalized Standard InChI. Both canonical SMILES comparisons are false, and the complete atom map is empty. Both parses have 15 specified tetrahedral sites. The SMILES parse reports one unspecified potential double-bond site and the InChI parse reports four. Representation-dependent double-bond flags do not establish a wrong natural stereoisomer. No biological identity follows from these diagnostics.

### Exact natural compound and configured form

identity: unknown. Targets: naturalproductmech:mibig-9913db0837.

Muraymycin C1 is represented by one configured glycosylated peptide graph with formula C38H63N11O17 and key GOFOFDWFFIGTML-IZAYEQDHSA-N, matching its retained MIBiG strings. The inspected 2011 abstract and the 2002/2018 titles concern muraymycins without supplying a complete C1 graph-to-compound/configuration map. The two saved encodings normalize to one InChI while their carbonyl/imine and heterocycle representations differ. Exact natural C1 correspondence remains unresolved; no replacement graph or wrong-isomer finding follows.

### Producer, occurrence and strain scope

provenance: unknown. Targets: naturalproductmech:mibig-9913db0837.

MIBiG BGC0001020/version 5 retains Streptomyces sp. NRRL 30471, NCBITaxon:996287, as SOURCE_ASSERTION. Own PMID21180767 reports muraymycin production by that strain at family level. The 2018 own title refers to mutant strains of the same named strain, while LOTUS occurrence rows are genus-level Streptomyces. Exact C1 production by the native versus modified strains and taxon-ID validation remain unverified; no heterologous host or engineered derivative is equated with this owner.

### Citation identity and exact occurrence applicability

evidence: unknown. Targets: naturalproductmech:mibig-9913db0837.

All three retained genus-level Streptomyces occurrence citations now have own bibliographic identity support: the 2018 mutant-strain DOI, the 2002 muraymycin-structure DOI and the 2011 biosynthesis PubMed article with DOI10.1039/c0mb00237b. That corroborates the cited works, not each full-key compound–organism relationship. Family titles and strain-level abstract claims do not automatically resolve every genus-level C1 occurrence.

### Exact locus and compound-specific biosynthesis

evidence: unknown. Targets: naturalproductmech:mibig-9913db0837.

The retained active BGC0001020/version 5 row is marked questionable quality and unknown completeness, carries NRPS and PKS classes, and records HQ257512.1 without locus coordinates or locus-method entries. Own PMID21180767 reports loss of muraymycin production after independent gene inactivations and has databank accession HQ257512. This is substantive family-level locus evidence, but the inspected abstract does not establish the exact C1 graph, retained accession version or compound-specific experiment. Preserve CLUSTER_UNSTATED for the retained owner claim pending that correspondence; do not infer that the publication lacks a mechanism.

### Compound-specific assays and target evidence

evidence: unknown. Targets: naturalproductmech:mibig-9913db0837.

The 2011 abstract describes muraymycin as a translocase I inhibitor; the 2002 title names peptidoglycan biosynthesis inhibitors and the 2018 title names antibacterial muraymycins. These are family-level statements. No inspected pure-C1 assay, target binding result, potency value, unit or experimental setting supports a new owner annotation. The local owner and exact-key assay/target rows contain none; this does not establish inactivity or absence of literature evidence.

### Pathway, target and causal-graph completeness

completeness: unknown. Targets: naturalproductmech:mibig-9913db0837.

The whole owner contains no biosynthetic_pathway, molecular_targets, bioactivities, inline causal_graphs or causal_graph_refs, and the nine-table exact-key joins contain no assay/target evidence. No causal edge or protein identity can be populated from a bibliographic title. The family-level inactivation statement is retained as a reading limitation rather than converted into an exact C1 pathway. Missing optional mechanism fields are a coverage limit, not a finding that the compound lacks a mechanism.

### Broad filing and asserted classification axes

representation: supported. Targets: naturalproductmech:mibig-9913db0837.

The file is in amino_acids_and_peptides and retains NPClassifier pathway Amino acids and Peptides, superclass Oligopeptides, class Linear peptides and is_glycoside=true. The stored peptide-containing representation and retained classifier row are compatible with that broad filing. NRPS and PKS remain separate source-asserted biosynthetic classes; computed filing is not proof of natural identity or biosynthetic causality.

### Versions, evidence placement and current intake continuity

provenance: supported. Targets: naturalproductmech:mibig-9913db0837.

MIBiG BGC0001020/version 5 and NPClassifier npclassifier.gnps2.org@2026-09-07 are retained source versions. Two seed-history events remain unchanged. All nine raw-table joins and the current official intake resolved owner/six source arrays were compared literally. Each actual inspection captures 37 source inputs, including regular AGENTS.md; row counts and source-input counts are different. The original diagnostic/retrieval/intake clocks remain distinct from this scientific reading. Publication dates do not certify current database versions.

### Minted identity and external equivalence

grounding: unknown. Targets: naturalproductmech:mibig-9913db0837.

The minted identifier and BGC0001020/version 5 source concept remain linked to the retained C1 graph. NPAtlas NPA06302 is an unverified retained cross-reference. Own PMID21180767 verifies DOI10.1039/c0mb00237b and databank HQ257512 as publication identifiers; it does not itself establish NPAtlas equivalence, the HQ257512.1 version content or a chemical synonym. The historical ChEBI grounding assertion was not independently renewed.

### Inspected source extent and unresolved coverage

scope: unknown. Targets: naturalproductmech:mibig-9913db0837.

The inspected publication evidence comprises the own 2011 PubMed abstract/databank fields and the own Crossref metadata of the 2002 and 2018 works. The two Crossref responses supply no abstract. Full article structure figures, supplementary material, compound tables, assay methods and external taxon/chemical authorities were not inspected. Abstract omission is not a claim that the full articles omit C1 or relevant experiments.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI890-LOCAL | /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/muraymycin-c1.yaml; whole owner; chemical_structure, producer_organisms, occurrences, biosynthetic_gene_clusters, np_classification, source_concepts, xrefs and curation_history | context_only | The whole current muraymycin C1 owner retains key GOFOFDWFFIGTML-IZAYEQDHSA-N, MIBiG-derived structure and separate database producer/locus/occurrence claims. The present corpus bytes remain unchanged. |
| SCI890-ROWS | /private/tmp/npm-review-work/shared-next-batch089-tentative/bgc-tentative89-owner-source-reconnaissance-DATA-001.json; /records/9/retained_rows and supplemental_rows; exact nine-table full-key joins and original row_guards | context_only | The exact full key joins one MIBiG compound, 3 LOTUS occurrence rows and one NPClassifier row. The other six named table joins contain zero rows for this key. These are local database assertions and bounded local row observations. |
| SCI890-ENCODINGS | /private/tmp/npm-review-work/shared-next-batch089-tentative/source-science-preparation/native-tentative89-ten-owner-dual-encoding-results-001.json; /records/9/smiles, inchi, stereo_counts, comparisons and atom_correspondence | supports | Both saved parses reproduce formula C38H63N11O17, formal charge 0, one connected component, the declared key and the same normalized Standard InChI. Both canonical SMILES comparisons are false, and the complete atom map is empty. Both parses have 15 specified tetrahedral sites. The SMILES parse reports one unspecified potential double-bond site and the InChI parse reports four. Representation-dependent double-bond flags do not establish a wrong natural stereoisomer. No biological identity follows from these diagnostics. |
| SCI890-CROSSREF1 | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-six-unresolved-crossref-001/doi-02.json; /message/DOI, /message/title, /message/container-title, /message/volume, /message/issue, /message/page, /message/published-print, /message/published-online; whole own message checked for abstract | partial | Own Crossref DOI 10.1021/acs.jnatprod.7b01054 identifies the 2018 paper Antibacterial Muraymycins from Mutant Strains of Streptomyces sp. NRRL 30471. The response supplies no abstract. Its title establishes bibliographic scope, without proving that this C1 structure was a native or engineered isolate or transferring any antibacterial result. |
| SCI890-CROSSREF2 | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-six-unresolved-crossref-001/doi-03.json; /message/DOI, /message/title, /message/container-title, /message/volume, /message/issue, /message/page, /message/published-print, /message/published-online; whole own message checked for abstract | partial | Own Crossref DOI 10.1021/ja017748h identifies the 2002 paper Structures of the Muraymycins, Novel Peptidoglycan Biosynthesis Inhibitors. The response supplies no abstract. This family-level title does not identify the retained C1 graph, absolute configuration or a pure-compound assay. |
| SCI890-PUBMED | /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-three-unattempted-PubMed-001/pmid-21180767.xml; PubmedArticle/MedlineCitation/PMID; Article/ArticleTitle, ELocationID, Abstract/AbstractText and DataBankList; PubmedData/ArticleIdList | partial | Own PMID21180767 and DOI10.1039/c0mb00237b identify the muraymycin biosynthesis article. Its abstract reports production by Streptomyces sp. NRRL 30471 and loss of muraymycin production after independent gene inactivations; its own databank field is HQ257512. This supports family-level production and locus context. The abstract does not furnish a complete C1 structure-to-experiment or accession-version mapping. |
| SCI890-INTAKE | /private/tmp/npm-review-work/890/intake-receipt.json; whole original intake receipt; order/path/exit_code/strict_exit_code/intake_passed | supports | The actual current intake completed with exit 0 and strict exit 0. This is saved administrative validation evidence; it does not establish natural structure, producer or publication correctness. |

## Limits And Additional Notes

- Muraymycin C1 is represented by one configured glycosylated peptide graph with formula C38H63N11O17 and key GOFOFDWFFIGTML-IZAYEQDHSA-N, matching its retained MIBiG strings. The inspected 2011 abstract and the 2002/2018 titles concern muraymycins without supplying a complete C1 graph-to-compound/configuration map. The two saved encodings normalize to one InChI while their carbonyl/imine and heterocycle representations differ. Exact natural C1 correspondence remains unresolved; no replacement graph or wrong-isomer finding follows.
- MIBiG BGC0001020/version 5 retains Streptomyces sp. NRRL 30471, NCBITaxon:996287, as SOURCE_ASSERTION. Own PMID21180767 reports muraymycin production by that strain at family level. The 2018 own title refers to mutant strains of the same named strain, while LOTUS occurrence rows are genus-level Streptomyces. Exact C1 production by the native versus modified strains and taxon-ID validation remain unverified; no heterologous host or engineered derivative is equated with this owner.
- The retained active BGC0001020/version 5 row is marked questionable quality and unknown completeness, carries NRPS and PKS classes, and records HQ257512.1 without locus coordinates or locus-method entries. Own PMID21180767 reports loss of muraymycin production after independent gene inactivations and has databank accession HQ257512. This is substantive family-level locus evidence, but the inspected abstract does not establish the exact C1 graph, retained accession version or compound-specific experiment. Preserve CLUSTER_UNSTATED for the retained owner claim pending that correspondence; do not infer that the publication lacks a mechanism.
- The 2011 abstract describes muraymycin as a translocase I inhibitor; the 2002 title names peptidoglycan biosynthesis inhibitors and the 2018 title names antibacterial muraymycins. These are family-level statements. No inspected pure-C1 assay, target binding result, potency value, unit or experimental setting supports a new owner annotation. The local owner and exact-key assay/target rows contain none; this does not establish inactivity or absence of literature evidence.
- The inspected publication evidence comprises the own 2011 PubMed abstract/databank fields and the own Crossref metadata of the 2002 and 2018 works. The two Crossref responses supply no abstract. Full article structure figures, supplementary material, compound tables, assay methods and external taxon/chemical authorities were not inspected. Abstract omission is not a claim that the full articles omit C1 or relevant experiments.
- This partial scientific review uses the accepted current intake and saved source evidence. Full natural identity, producer and locus correspondence remain unresolved.
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
review_id: 20261029T011323Z-muraymycin-c1
title: Scientific review of muraymycin C1
started_at: '2026-10-29T01:01:01.272318Z'
finished_at: '2026-10-29T01:13:23.639006Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: muraymycin C1 retains internally reproducible normalized InChI/key diagnostics
  with distinct canonical representations and no complete atom map. The own 2011 abstract
  supplies muraymycin-family production and locus context, while the 2002/2018 metadata
  supplies bibliographic scope. Exact C1 structure, native-versus-mutant production
  and assay applicability remain unresolved. The current official intake passed; this
  partial assessment records the remaining scientific limits.
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
  - path: data/natural_products/amino_acids_and_peptides/muraymycin-c1.yaml
    sha256: 5bc9d114c25e128fb3526833dc23c0064e0513374abb66dbd2a4ef6dce29dd49
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
- target_id: naturalproductmech:mibig-9913db0837
  path: data/natural_products/amino_acids_and_peptides/muraymycin-c1.yaml
  label: muraymycin C1
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
  description: Read-only scientific review of the exact muraymycin C1 owner, complete
    retained source rows, saved dual-encoding diagnostics, the2011 biosynthesis abstract
    and2002/2018 bibliographic metadata. Family-level production/inactivation support
    remains distinct from exact C1 structure, native-versus-mutant provenance and
    pure-compound activity.
  selection: One current unreviewed record selected in canonical path order; official
    batch89 selection and intake exactly reconcile the frozen owner and source evidence.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-9913db0837
  exclusions:
  - target: Complete natural structure and stereochemistry
    reason: Full primary bodies, structure figure pixels, supplementary data and complete
      atom-level correspondence were not inspected; normalized InChI agreement is
      bounded representation evidence.
  - target: Exact C1 strain, sequence and experimental correspondence
    reason: The inspected abstract supplies family-level locus and production context;
      the exact C1 graph, HQ257512.1 sequence version and native-versus-mutant assay
      assignments were not independently resolved.
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
  - naturalproductmech:mibig-9913db0837
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
  - naturalproductmech:mibig-9913db0837
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
  - naturalproductmech:mibig-9913db0837
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
  - naturalproductmech:mibig-9913db0837
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
  - naturalproductmech:mibig-9913db0837
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/muraymycin-c1.yaml
    --out /private/tmp/npm-review-work/890/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-29T01:01:02.642082Z. Original
    receipt: /private/tmp/npm-review-work/890/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-9913db0837
- check_id: SCI890-ENCODINGS
  name: Saved encodings and stereochemical resolution
  status: passed
  required: true
  summary: Both saved parses reproduce formula C38H63N11O17, formal charge 0, one
    connected component, the declared key and the same normalized Standard InChI.
    Both canonical SMILES comparisons are false, and the complete atom map is empty.
    Both parses have 15 specified tetrahedral sites. The SMILES parse reports one
    unspecified potential double-bond site and the InChI parse reports four. Representation-dependent
    double-bond flags do not establish a wrong natural stereoisomer. No biological
    identity follows from these diagnostics.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ENCODINGS
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI890-IDENTITY
  name: Exact natural compound and configured form
  status: unavailable
  required: true
  summary: Muraymycin C1 is represented by one configured glycosylated peptide graph
    with formula C38H63N11O17 and key GOFOFDWFFIGTML-IZAYEQDHSA-N, matching its retained
    MIBiG strings. The inspected 2011 abstract and the 2002/2018 titles concern muraymycins
    without supplying a complete C1 graph-to-compound/configuration map. The two saved
    encodings normalize to one InChI while their carbonyl/imine and heterocycle representations
    differ. Exact natural C1 correspondence remains unresolved; no replacement graph
    or wrong-isomer finding follows.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-ENCODINGS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI890-PRODUCER
  name: Producer, occurrence and strain scope
  status: unavailable
  required: true
  summary: MIBiG BGC0001020/version 5 retains Streptomyces sp. NRRL 30471, NCBITaxon:996287,
    as SOURCE_ASSERTION. Own PMID21180767 reports muraymycin production by that strain
    at family level. The 2018 own title refers to mutant strains of the same named
    strain, while LOTUS occurrence rows are genus-level Streptomyces. Exact C1 production
    by the native versus modified strains and taxon-ID validation remain unverified;
    no heterologous host or engineered derivative is equated with this owner.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI890-OCCURRENCE
  name: Citation identity and exact occurrence applicability
  status: unavailable
  required: true
  summary: 'All three retained genus-level Streptomyces occurrence citations now have
    own bibliographic identity support: the 2018 mutant-strain DOI, the 2002 muraymycin-structure
    DOI and the 2011 biosynthesis PubMed article with DOI10.1039/c0mb00237b. That
    corroborates the cited works, not each full-key compound–organism relationship.
    Family titles and strain-level abstract claims do not automatically resolve every
    genus-level C1 occurrence.'
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI890-BIOSYNTHESIS
  name: Exact locus and compound-specific biosynthesis
  status: unavailable
  required: true
  summary: The retained active BGC0001020/version 5 row is marked questionable quality
    and unknown completeness, carries NRPS and PKS classes, and records HQ257512.1
    without locus coordinates or locus-method entries. Own PMID21180767 reports loss
    of muraymycin production after independent gene inactivations and has databank
    accession HQ257512. This is substantive family-level locus evidence, but the inspected
    abstract does not establish the exact C1 graph, retained accession version or
    compound-specific experiment. Preserve CLUSTER_UNSTATED for the retained owner
    claim pending that correspondence; do not infer that the publication lacks a mechanism.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI890-BIOACTIVITY
  name: Compound-specific assays and target evidence
  status: unavailable
  required: true
  summary: The 2011 abstract describes muraymycin as a translocase I inhibitor; the
    2002 title names peptidoglycan biosynthesis inhibitors and the 2018 title names
    antibacterial muraymycins. These are family-level statements. No inspected pure-C1
    assay, target binding result, potency value, unit or experimental setting supports
    a new owner annotation. The local owner and exact-key assay/target rows contain
    none; this does not establish inactivity or absence of literature evidence.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI890-GRAPH
  name: Pathway, target and causal-graph completeness
  status: unavailable
  required: true
  summary: The whole owner contains no biosynthetic_pathway, molecular_targets, bioactivities,
    inline causal_graphs or causal_graph_refs, and the nine-table exact-key joins
    contain no assay/target evidence. No causal edge or protein identity can be populated
    from a bibliographic title. The family-level inactivation statement is retained
    as a reading limitation rather than converted into an exact C1 pathway. Missing
    optional mechanism fields are a coverage limit, not a finding that the compound
    lacks a mechanism.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI890-CLASSIFICATION
  name: Broad filing and asserted classification axes
  status: passed
  required: true
  summary: The file is in amino_acids_and_peptides and retains NPClassifier pathway
    Amino acids and Peptides, superclass Oligopeptides, class Linear peptides and
    is_glycoside=true. The stored peptide-containing representation and retained classifier
    row are compatible with that broad filing. NRPS and PKS remain separate source-asserted
    biosynthetic classes; computed filing is not proof of natural identity or biosynthetic
    causality.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-ENCODINGS
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI890-PROVENANCE
  name: Versions, evidence placement and current intake continuity
  status: passed
  required: true
  summary: MIBiG BGC0001020/version 5 and NPClassifier npclassifier.gnps2.org@2026-09-07
    are retained source versions. Two seed-history events remain unchanged. All nine
    raw-table joins and the current official intake resolved owner/six source arrays
    were compared literally. Each actual inspection captures 37 source inputs, including
    regular AGENTS.md; row counts and source-input counts are different. The original
    diagnostic/retrieval/intake clocks remain distinct from this scientific reading.
    Publication dates do not certify current database versions.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-ENCODINGS
  - SCI890-INTAKE
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI890-GROUNDING
  name: Minted identity and external equivalence
  status: unavailable
  required: true
  summary: The minted identifier and BGC0001020/version 5 source concept remain linked
    to the retained C1 graph. NPAtlas NPA06302 is an unverified retained cross-reference.
    Own PMID21180767 verifies DOI10.1039/c0mb00237b and databank HQ257512 as publication
    identifiers; it does not itself establish NPAtlas equivalence, the HQ257512.1
    version content or a chemical synonym. The historical ChEBI grounding assertion
    was not independently renewed.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
- check_id: SCI890-AVAILABILITY
  name: Inspected source extent and unresolved coverage
  status: unavailable
  required: true
  summary: The inspected publication evidence comprises the own 2011 PubMed abstract/databank
    fields and the own Crossref metadata of the 2002 and 2018 works. The two Crossref
    responses supply no abstract. Full article structure figures, supplementary material,
    compound tables, assay methods and external taxon/chemical authorities were not
    inspected. Abstract omission is not a claim that the full articles omit C1 or
    relevant experiments.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
  scope_note: Bounded scientific assessment of retained owner rows, saved diagnostics
    and inspected publication evidence. Executed command checks and their original
    receipts are listed separately.
evidence:
- evidence_id: SCI890-LOCAL
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/muraymycin-c1.yaml
  locator: whole owner; chemical_structure, producer_organisms, occurrences, biosynthetic_gene_clusters,
    np_classification, source_concepts, xrefs and curation_history
  accessed_at: '2026-10-28T23:47:10.384990Z'
  snapshot_sha256: 5bc9d114c25e128fb3526833dc23c0064e0513374abb66dbd2a4ef6dce29dd49
  support: context_only
  summary: The whole current muraymycin C1 owner retains key GOFOFDWFFIGTML-IZAYEQDHSA-N,
    MIBiG-derived structure and separate database producer/locus/occurrence claims.
    The present corpus bytes remain unchanged.
- evidence_id: SCI890-ROWS
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/bgc-tentative89-owner-source-reconnaissance-DATA-001.json
  locator: /records/9/retained_rows and supplemental_rows; exact nine-table full-key
    joins and original row_guards
  accessed_at: '2026-10-28T23:47:10.384990Z'
  snapshot_sha256: 1fb4869ecc967e2a94b073ff4b524f8b9d084f2e15f3b7e8aa9429d9734ea6e2
  support: context_only
  summary: The exact full key joins one MIBiG compound, 3 LOTUS occurrence rows and
    one NPClassifier row. The other six named table joins contain zero rows for this
    key. These are local database assertions and bounded local row observations.
- evidence_id: SCI890-ENCODINGS
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/source-science-preparation/native-tentative89-ten-owner-dual-encoding-results-001.json
  locator: /records/9/smiles, inchi, stereo_counts, comparisons and atom_correspondence
  accessed_at: '2026-10-28T23:59:21.473730Z'
  snapshot_sha256: 356c8827be928050a8b7082816ba6ea6f707f5a5881cf0f1ceecf15e16e37570
  support: supports
  summary: Both saved parses reproduce formula C38H63N11O17, formal charge 0, one
    connected component, the declared key and the same normalized Standard InChI.
    Both canonical SMILES comparisons are false, and the complete atom map is empty.
    Both parses have 15 specified tetrahedral sites. The SMILES parse reports one
    unspecified potential double-bond site and the InChI parse reports four. Representation-dependent
    double-bond flags do not establish a wrong natural stereoisomer. No biological
    identity follows from these diagnostics.
- evidence_id: SCI890-CROSSREF1
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-six-unresolved-crossref-001/doi-02.json
  locator: /message/DOI, /message/title, /message/container-title, /message/volume,
    /message/issue, /message/page, /message/published-print, /message/published-online;
    whole own message checked for abstract
  accessed_at: '2026-10-29T00:57:18.571734Z'
  snapshot_sha256: e76e346dfb5e576583782c08d0465e91400fafd1d8ea2e17ecae268d60dfde98
  support: partial
  summary: Own Crossref DOI 10.1021/acs.jnatprod.7b01054 identifies the 2018 paper
    Antibacterial Muraymycins from Mutant Strains of Streptomyces sp. NRRL 30471.
    The response supplies no abstract. Its title establishes bibliographic scope,
    without proving that this C1 structure was a native or engineered isolate or transferring
    any antibacterial result.
- evidence_id: SCI890-CROSSREF2
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-six-unresolved-crossref-001/doi-03.json
  locator: /message/DOI, /message/title, /message/container-title, /message/volume,
    /message/issue, /message/page, /message/published-print, /message/published-online;
    whole own message checked for abstract
  accessed_at: '2026-10-29T00:57:19.578161Z'
  snapshot_sha256: 4f4da27230ed3eb5d084177056054eb48aa45e1bf74ee0ee1099f282e3adff0f
  support: partial
  summary: Own Crossref DOI 10.1021/ja017748h identifies the 2002 paper Structures
    of the Muraymycins, Novel Peptidoglycan Biosynthesis Inhibitors. The response
    supplies no abstract. This family-level title does not identify the retained C1
    graph, absolute configuration or a pure-compound assay.
- evidence_id: SCI890-PUBMED
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch089-tentative/literature-preparation/public-metadata-three-unattempted-PubMed-001/pmid-21180767.xml
  locator: PubmedArticle/MedlineCitation/PMID; Article/ArticleTitle, ELocationID,
    Abstract/AbstractText and DataBankList; PubmedData/ArticleIdList
  accessed_at: '2026-10-29T00:31:37.450264Z'
  snapshot_sha256: ac5c4668e8a1f31adb743c866ce7921ce3ebcda885e99ec96882419177672379
  support: partial
  summary: Own PMID21180767 and DOI10.1039/c0mb00237b identify the muraymycin biosynthesis
    article. Its abstract reports production by Streptomyces sp. NRRL 30471 and loss
    of muraymycin production after independent gene inactivations; its own databank
    field is HQ257512. This supports family-level production and locus context. The
    abstract does not furnish a complete C1 structure-to-experiment or accession-version
    mapping.
- evidence_id: SCI890-INTAKE
  kind: validation
  reference: /private/tmp/npm-review-work/890/intake-receipt.json
  locator: whole original intake receipt; order/path/exit_code/strict_exit_code/intake_passed
  accessed_at: '2026-10-29T01:01:02.698625Z'
  snapshot_sha256: da8dcbb234ae0d658c4088fa4cf020b6a1028cd27f55c4a0eb09df1ffcbf63f2
  support: supports
  summary: The actual current intake completed with exit 0 and strict exit 0. This
    is saved administrative validation evidence; it does not establish natural structure,
    producer or publication correctness.
assessments:
- assessment_id: SCI890-ENCODINGS
  area: consistency
  topic: Saved encodings and stereochemical resolution
  outcome: supported
  summary: Both saved parses reproduce formula C38H63N11O17, formal charge 0, one
    connected component, the declared key and the same normalized Standard InChI.
    Both canonical SMILES comparisons are false, and the complete atom map is empty.
    Both parses have 15 specified tetrahedral sites. The SMILES parse reports one
    unspecified potential double-bond site and the InChI parse reports four. Representation-dependent
    double-bond flags do not establish a wrong natural stereoisomer. No biological
    identity follows from these diagnostics.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ENCODINGS
  dimensions:
  - name: stereochemical_resolution
    value: Both parses have 15 specified tetrahedral sites. The SMILES parse reports
      one unspecified potential double-bond site and the InChI parse reports four.
      The retained stereo_complete flag is true.
    definition: Literal flag and separate saved graph diagnostics; normalized identifiers
      do not prove atom-mapped or experimental stereochemical equivalence.
    evidence_ids:
    - SCI890-LOCAL
    - SCI890-ENCODINGS
- assessment_id: SCI890-IDENTITY
  area: identity
  topic: Exact natural compound and configured form
  outcome: unknown
  summary: Muraymycin C1 is represented by one configured glycosylated peptide graph
    with formula C38H63N11O17 and key GOFOFDWFFIGTML-IZAYEQDHSA-N, matching its retained
    MIBiG strings. The inspected 2011 abstract and the 2002/2018 titles concern muraymycins
    without supplying a complete C1 graph-to-compound/configuration map. The two saved
    encodings normalize to one InChI while their carbonyl/imine and heterocycle representations
    differ. Exact natural C1 correspondence remains unresolved; no replacement graph
    or wrong-isomer finding follows.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-ENCODINGS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
- assessment_id: SCI890-PRODUCER
  area: provenance
  topic: Producer, occurrence and strain scope
  outcome: unknown
  summary: MIBiG BGC0001020/version 5 retains Streptomyces sp. NRRL 30471, NCBITaxon:996287,
    as SOURCE_ASSERTION. Own PMID21180767 reports muraymycin production by that strain
    at family level. The 2018 own title refers to mutant strains of the same named
    strain, while LOTUS occurrence rows are genus-level Streptomyces. Exact C1 production
    by the native versus modified strains and taxon-ID validation remain unverified;
    no heterologous host or engineered derivative is equated with this owner.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
  dimensions:
  - name: taxon_strain
    value: MIBiG Streptomyces sp. NRRL 30471 / NCBITaxon:996287; LOTUS Streptomyces
      / NCBITaxon:1883; native-versus-mutant exact C1 scope unresolved
    definition: Source-specific taxon/strain literals and their distinct producer/occurrence
      roles; no unverified taxonomy or congener equivalence.
    evidence_ids:
    - SCI890-LOCAL
    - SCI890-ROWS
    - SCI890-CROSSREF1
    - SCI890-CROSSREF2
    - SCI890-PUBMED
- assessment_id: SCI890-OCCURRENCE
  area: evidence
  topic: Citation identity and exact occurrence applicability
  outcome: unknown
  summary: 'All three retained genus-level Streptomyces occurrence citations now have
    own bibliographic identity support: the 2018 mutant-strain DOI, the 2002 muraymycin-structure
    DOI and the 2011 biosynthesis PubMed article with DOI10.1039/c0mb00237b. That
    corroborates the cited works, not each full-key compound–organism relationship.
    Family titles and strain-level abstract claims do not automatically resolve every
    genus-level C1 occurrence.'
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
- assessment_id: SCI890-BIOSYNTHESIS
  area: evidence
  topic: Exact locus and compound-specific biosynthesis
  outcome: unknown
  summary: The retained active BGC0001020/version 5 row is marked questionable quality
    and unknown completeness, carries NRPS and PKS classes, and records HQ257512.1
    without locus coordinates or locus-method entries. Own PMID21180767 reports loss
    of muraymycin production after independent gene inactivations and has databank
    accession HQ257512. This is substantive family-level locus evidence, but the inspected
    abstract does not establish the exact C1 graph, retained accession version or
    compound-specific experiment. Preserve CLUSTER_UNSTATED for the retained owner
    claim pending that correspondence; do not infer that the publication lacks a mechanism.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
  dimensions:
  - name: evidence_tier
    value: DATABASE_ASSERTION; producer SOURCE_ASSERTION; locus CLUSTER_UNSTATED;
      own PubMed abstract family evidence and Crossref bibliographic metadata
    definition: Bibliographic identity, family experimental context, producer assertion
      and locus grade answer different questions; none alone certifies the exact natural
      graph.
    evidence_ids:
    - SCI890-LOCAL
    - SCI890-ROWS
    - SCI890-CROSSREF1
    - SCI890-CROSSREF2
    - SCI890-PUBMED
- assessment_id: SCI890-BIOACTIVITY
  area: evidence
  topic: Compound-specific assays and target evidence
  outcome: unknown
  summary: The 2011 abstract describes muraymycin as a translocase I inhibitor; the
    2002 title names peptidoglycan biosynthesis inhibitors and the 2018 title names
    antibacterial muraymycins. These are family-level statements. No inspected pure-C1
    assay, target binding result, potency value, unit or experimental setting supports
    a new owner annotation. The local owner and exact-key assay/target rows contain
    none; this does not establish inactivity or absence of literature evidence.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
- assessment_id: SCI890-GRAPH
  area: completeness
  topic: Pathway, target and causal-graph completeness
  outcome: unknown
  summary: The whole owner contains no biosynthetic_pathway, molecular_targets, bioactivities,
    inline causal_graphs or causal_graph_refs, and the nine-table exact-key joins
    contain no assay/target evidence. No causal edge or protein identity can be populated
    from a bibliographic title. The family-level inactivation statement is retained
    as a reading limitation rather than converted into an exact C1 pathway. Missing
    optional mechanism fields are a coverage limit, not a finding that the compound
    lacks a mechanism.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
- assessment_id: SCI890-CLASSIFICATION
  area: representation
  topic: Broad filing and asserted classification axes
  outcome: supported
  summary: The file is in amino_acids_and_peptides and retains NPClassifier pathway
    Amino acids and Peptides, superclass Oligopeptides, class Linear peptides and
    is_glycoside=true. The stored peptide-containing representation and retained classifier
    row are compatible with that broad filing. NRPS and PKS remain separate source-asserted
    biosynthetic classes; computed filing is not proof of natural identity or biosynthetic
    causality.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-ENCODINGS
- assessment_id: SCI890-PROVENANCE
  area: provenance
  topic: Versions, evidence placement and current intake continuity
  outcome: supported
  summary: MIBiG BGC0001020/version 5 and NPClassifier npclassifier.gnps2.org@2026-09-07
    are retained source versions. Two seed-history events remain unchanged. All nine
    raw-table joins and the current official intake resolved owner/six source arrays
    were compared literally. Each actual inspection captures 37 source inputs, including
    regular AGENTS.md; row counts and source-input counts are different. The original
    diagnostic/retrieval/intake clocks remain distinct from this scientific reading.
    Publication dates do not certify current database versions.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-ENCODINGS
  - SCI890-INTAKE
  dimensions:
  - name: source_version
    value: MIBiG BGC0001020/version 5; NPClassifier npclassifier.gnps2.org@2026-09-07
    definition: Retained source/model versions and unchanged history, independent
      of publication dates or live-authority freshness.
    evidence_ids:
    - SCI890-LOCAL
    - SCI890-ROWS
- assessment_id: SCI890-GROUNDING
  area: grounding
  topic: Minted identity and external equivalence
  outcome: unknown
  summary: The minted identifier and BGC0001020/version 5 source concept remain linked
    to the retained C1 graph. NPAtlas NPA06302 is an unverified retained cross-reference.
    Own PMID21180767 verifies DOI10.1039/c0mb00237b and databank HQ257512 as publication
    identifiers; it does not itself establish NPAtlas equivalence, the HQ257512.1
    version content or a chemical synonym. The historical ChEBI grounding assertion
    was not independently renewed.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-ROWS
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
- assessment_id: SCI890-AVAILABILITY
  area: scope
  topic: Inspected source extent and unresolved coverage
  outcome: unknown
  summary: The inspected publication evidence comprises the own 2011 PubMed abstract/databank
    fields and the own Crossref metadata of the 2002 and 2018 works. The two Crossref
    responses supply no abstract. Full article structure figures, supplementary material,
    compound tables, assay methods and external taxon/chemical authorities were not
    inspected. Abstract omission is not a claim that the full articles omit C1 or
    relevant experiments.
  target_ids:
  - naturalproductmech:mibig-9913db0837
  evidence_ids:
  - SCI890-LOCAL
  - SCI890-CROSSREF1
  - SCI890-CROSSREF2
  - SCI890-PUBMED
findings: []
actions: []
limitations:
- Muraymycin C1 is represented by one configured glycosylated peptide graph with formula
  C38H63N11O17 and key GOFOFDWFFIGTML-IZAYEQDHSA-N, matching its retained MIBiG strings.
  The inspected 2011 abstract and the 2002/2018 titles concern muraymycins without
  supplying a complete C1 graph-to-compound/configuration map. The two saved encodings
  normalize to one InChI while their carbonyl/imine and heterocycle representations
  differ. Exact natural C1 correspondence remains unresolved; no replacement graph
  or wrong-isomer finding follows.
- MIBiG BGC0001020/version 5 retains Streptomyces sp. NRRL 30471, NCBITaxon:996287,
  as SOURCE_ASSERTION. Own PMID21180767 reports muraymycin production by that strain
  at family level. The 2018 own title refers to mutant strains of the same named strain,
  while LOTUS occurrence rows are genus-level Streptomyces. Exact C1 production by
  the native versus modified strains and taxon-ID validation remain unverified; no
  heterologous host or engineered derivative is equated with this owner.
- The retained active BGC0001020/version 5 row is marked questionable quality and
  unknown completeness, carries NRPS and PKS classes, and records HQ257512.1 without
  locus coordinates or locus-method entries. Own PMID21180767 reports loss of muraymycin
  production after independent gene inactivations and has databank accession HQ257512.
  This is substantive family-level locus evidence, but the inspected abstract does
  not establish the exact C1 graph, retained accession version or compound-specific
  experiment. Preserve CLUSTER_UNSTATED for the retained owner claim pending that
  correspondence; do not infer that the publication lacks a mechanism.
- The 2011 abstract describes muraymycin as a translocase I inhibitor; the 2002 title
  names peptidoglycan biosynthesis inhibitors and the 2018 title names antibacterial
  muraymycins. These are family-level statements. No inspected pure-C1 assay, target
  binding result, potency value, unit or experimental setting supports a new owner
  annotation. The local owner and exact-key assay/target rows contain none; this does
  not establish inactivity or absence of literature evidence.
- The inspected publication evidence comprises the own 2011 PubMed abstract/databank
  fields and the own Crossref metadata of the 2002 and 2018 works. The two Crossref
  responses supply no abstract. Full article structure figures, supplementary material,
  compound tables, assay methods and external taxon/chemical authorities were not
  inspected. Abstract omission is not a claim that the full articles omit C1 or relevant
  experiments.
- This partial scientific review uses the accepted current intake and saved source
  evidence. Full natural identity, producer and locus correspondence remain unresolved.
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
