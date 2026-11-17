# Chuangxinmycin: exact authority and sibling identity with locus-citation correction

- Review: 20261021T184823Z-chuangxinmycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T18:41:47.517924Z
- Finished UTC: 2026-10-21T18:48:23.822712Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The stored graph, eligible ChEBI MOL and valid InChI of the exact pinned AntibioticMech record agree; invalid upstream SMILES are not used as identity proof. Original production and antibacterial evidence remain appropriately scoped. The cxm locus incorrectly reuses the original compound-bioactivity citation instead of the recoverable 2018 study, a confirmed minor finding that fails the required citation check. Missing original stereochemical and detailed main-text evidence keeps the review partial; proposed correction preserves distinct native and heterologous stocks.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 133, batch 014, selected in path order from the fresh-main authoritative validated catalogue and the separately validated targets in earlier batch commits (publication tracked separately). At selection, 184 of 3116 current records had campaign coverage and 2932 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:79391 | data/natural_products/alkaloids/chuangxinmycin.yaml | generated | (−)-chuangxinmycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | CHEBI:79391 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | CHEBI:79391 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | CHEBI:79391 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | CHEBI:79391 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:79391 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | CHEBI:79391 | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Complete owner and captured-source scope | passed | True | CHEBI:79391 | Successful official intake and a fresh root full-owner/read receipt precede this authoring. All six officially captured sets and the separate seventh PubChem preparation match; the external component set is empty. |
| Claim-local locus citation | failed | True | CHEBI:79391 | The imported COMPOUND_BIOACTIVITY citation is the 1977 study, whereas the stored cxm accession and exact heterologous experiments belong to JNP 2018. |
| Original isolation and detailed 2018 main access | unavailable | True | CHEBI:79391 | Full 1977 and JNP 2018 bodies remain unavailable; stock/chemical detail is not inferred beyond the retained positive abstract, official SI and deposit. |
| Stored chemical representation and complete source row | passed | True | CHEBI:79391 | Fresh intake derivation agrees with the stored graph; the source selector, full row and prepared snapshot were independently rechecked. |
| Literal chemical identifiers and namespace resolution | passed | True | CHEBI:79391 | Each present literal NPAtlas or PubChem cross-reference returned the exact stored Standard and fixed-H graph. Legacy five-digit NPAtlas requests were queried literally and their returned canonical identifiers retained. ChEBI and Wikidata precision or tautomer differences are described separately. |
| Exact pinned sibling identity and link | passed | True | CHEBI:79391 | Exact committed valid InChI, configured commit, row and projected link/class agree; the invalid sibling SMILES remains a bounded source representation defect. |
| Original exact absolute-hand protocol | unavailable | True | CHEBI:79391 | The detailed original 1977 body and hand determination were not recovered in the retained primary access. No opposite hand or unsupported source absence is inferred. |

## Scientific And Domain Assessments

### Native status and complete audit history

provenance: supported. Targets: CHEBI:79391.

All 3 retained events are SEEDED_FROM_SOURCES. Native status remains SEEDED; these are provenance events, not earlier structured-review passes, and no scientific content or history is changed.

### Complete optional-assertion inventory

completeness: supported. Targets: CHEBI:79391.

The complete structure-specific definition, ANTIBACTERIAL summary and AntibioticMech SAME_STRUCTURE/SAME_INCHIKEY relation to CHEBI:79391 at source version 74f6cc836249 are present. Their exact identity, pinned sibling and activity support require the chemistry/science assessments; this completeness inventory does not endorse them by presence alone. No assay observation or pathway is emitted.

### Exact-key computed classification provenance

representation: supported. Targets: CHEBI:79391.

The exact-key NPClassifier projection and version npclassifier.gnps2.org@2026-09-07 reproduce the owner filing, superclass/class labels and glycoside value false. Computed labels are not independent precursor, mechanism or natural-origin evidence. Any accepted new identity requires reclassification for its effective key.

### Taxonomic names versus experimental stocks

provenance: supported. Targets: CHEBI:79391.

NCBI 2039464 is Actinoplanes tsinanensis. Its type material CPCC 200056 does not by itself prove equivalence to experimental CPCC 240351; actual producing and genome-source stocks require the separately inspected primary/deposit bridge.

### Producer transcriptomic applicability

completeness: not_applicable. Targets: CHEBI:79391.

No exact native producer species/strain dataset is represented in the inspected catalogue. Related species and possible experimental hosts do not establish a construct/condition match; no gene/module or compound-production inference is made.

### Native production and deposited source stock

evidence: supported. Targets: CHEBI:79391.

The original A. tsinanensis production assertion remains supported at its species/abstract resolution. The accession names CPCC 240351; this does not equate it with CPCC 200056 or prove native knockout.

### Exact cxm evidence and two grading tiers

evidence: concern. Targets: CHEBI:79391.

The empty imported methods are faithful, but a recoverable exact locus citation and heterologous final-product experiment are omitted from the claim. A source-pinned citation/method correction can preserve the native SOURCE_ASSERTION while documenting CLUSTER_DEMONSTRATED.

### Original occurrence and activity scope

scope: supported. Targets: CHEBI:79391.

The ChEBI occurrence cites the original 1977 isolation, which remains an appropriate species-level source; it should not be replaced simply because it predates the locus. ANTIBACTERIAL is compatible with the source abstract. The exact sibling SAME_STRUCTURE link is handled by independent chemistry/context review, not a transfer of detailed mechanisms.

### Stored representation and source-concept provenance

identity: supported. Targets: CHEBI:79391.

The complete source row BGC0001485:1 and source-concept hash reproduce this stored representation; this does not establish that the upstream compound label is correct. Formula, charge, Standard and fixed-H distinctions are independently recorded. Primary support and any conflicting exact xref are assessed separately.

### Exact authority eligibility and source representation

provenance: supported. Targets: CHEBI:79391.

Exactly one committed three-star default ChEBI row matches; its current graph is checked separately.

### Official MOL, JSON SMILES and chemical Wikidata fields

representation: supported. Targets: CHEBI:79391.

The retained comparisons distinguish valid official MOL structures from default JSON SMILES that fail parsing. Only exact eligible three-star rows can ground this corpus. Canonical Wikidata P233, isomeric P2017 and declared InChI/key fields are separate assertions; a matching Standard key does not guarantee fixed-H identity. No invalid JSON SMILES is proposed for copying.

### Exact eligible authority and historical sibling identity

identity: supported. Targets: CHEBI:79391.

The owner valid graph, eligible CHEBI:79391 official MOL and pinned sibling valid InChI agree on full identity. Invalid default JSON/sibling SMILES must not be copied. Primary experimental absolute certainty is separately unknown.

## Findings

### S133-F-ROUTING: The locus uses an original compound-bioactivity citation

minor / open / confirmed; issue key: mibig-bgc0001485-citation-method-scope.

The source-faithful empty grade is not false, but the locus reuses the 1977 compound-bioactivity reference instead of the recoverable 2018 cxm study and its exact heterologous product support.

## Recommended Actions And Acceptance Checks

### S133-ACT-ROUTING

Use BGC0001485:1 and complete raw SHA256 9e50f70ed6d17242896d30d300b0752d12c7617640870ca4bba0399ed12bda86 in mibig_claim_references.tsv: producer_reference PMID:327539, locus_reference PMID:29565122, source_reference DOI:10.1021/acs.jnatprod.7b00835, with explicit source-stock/host limits. Pair with REPLACE Heterologous expression for naturalproductmech:mibig-9cbda6ee27 only after accepting the deposited cxm-to-tested-construct bridge at the documented resolution. The consumed citation row supplies the full-row guard omitted by legacy REPLACE. Preserve the original url-prefixed citation/reference_basis in raw history; use valid PMID/DOI forms in the new table. Do not transfer CPCC 200056 or heterologous deletions into native Knock-out studies.

- The original producer/occurrence citation remains local to original isolation; the 2018 citation reaches the locus.
- Original raw bytes and COMPOUND_BIOACTIVITY provenance are retained.
- The combined rows fail on any full source-row drift; source identity and chemistry are unchanged.
- No native producer upgrade or cross-stock equality is emitted; full-main limits remain explicit.
- Future authorized canary, reproduction and QC demonstrate both decisions compose and target only BGC0001485:1.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R133-OWNER | data/natural_products/alkaloids/chuangxinmycin.yaml; Complete post-intake owner, optional assertions and all history events | supports | Root read the complete owner after successful official intake: 1 occurrence, 1 producer and 1 locus assertions. No referenced external component is present. Optional fields: definition, bioactivity_summary, related_records. |
| R133-LOCAL | /private/tmp/npm-review-work/133/local-sources.json; Complete resolved owner and all six officially captured raw row sets | context_only | All six captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB and NPClassifier sets match the frozen preparation, including empty sets. The separate seventh PubChem inventory comparison is distinguished below. Source fidelity does not itself establish experimental support. |
| R133-PUBCHEM-PREP | data/raw/pubchem_bioassay.tsv; Exact-key rows compared with the separate provisional seventh source set | context_only | The separate committed PubChem raw set contains 0 matching rows and reproduces the frozen preparation. This is not part of the official six-set intake. Empty or no-assay-data rows are not tested outcomes; no emitted assay assertion is inferred. |
| R133-TAXON-CONTEXT | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=1048205,1288082,145745,162425,1883,2039464,227321,229533,29852,378258,446321,50193,50206,5073,5076,5081,5128,73504; Exact relevant TaxId, ScientificName, Rank, ParentTaxId and OtherNames fields | context_only | NCBI 2039464 is Actinoplanes tsinanensis. Its type material CPCC 200056 does not by itself prove equivalence to experimental CPCC 240351; actual producing and genome-source stocks require the separately inspected primary/deposit bridge. |
| R133-IMODULON | https://imodulondb.org/api/datasets; Complete 20-organism, 28-dataset official catalogue | context_only | The full retained catalogue establishes membership only. None of these exact native producer labels occurs in it. Listed Streptomyces coelicolor or E. coli datasets do not establish an introduced biosynthetic construct, recombinant protein or native production. |
| S133-E-OWNER | data/natural_products/alkaloids/chuangxinmycin.yaml; Complete actual owner after official batch014 intake; exact resolved owner and all six captured source sets reconciled with frozen preparation | supports | The complete selected owner was read by root after successful official intake. Its resolved contents and all six captured raw sets equal the frozen source preparation. This adoption preserves original external retrieval times and does not reclassify old literature preparation as newly retrieved evidence. |
| S133-E-RAW | data/raw/mibig_compounds.tsv; BGC0001485:1 | supports | Exact raw row BGC0001485:1 was compared with the tentative snapshot. Complete parsed source-row SHA256 9e50f70ed6d17242896d30d300b0752d12c7617640870ca4bba0399ed12bda86 includes all fields and empty values. |
| S133-E-GRADING | conf/producer_evidence.tsv; Complete method vocabulary and inspected grading implementation | supports | The configured Knock-out studies label assumes loss of production in the native organism. Heterologous expression and Enzymatic assays support only the locus. Empty methods faithfully yield SOURCE_ASSERTION / CLUSTER_UNSTATED. |
| S133-E-ROUTES | /private/tmp/npm-review-work/shared-next-batch014/curator-routing/routing-notes.json; Complete static consumer feasibility notes, exact raw guards and flattened implementation pins | supports | Current consumers and static tests distinguish nonempty method REPLACE, seven-field WITHDRAW, full-row-pinned citation/strain context, and exact-triple occurrence exclusions. REPLACE expected_* fields alone are not enforced. No proposed curation or test was executed. |
| S133-E-1977 | https://pubmed.ncbi.nlm.nih.gov/327539/; PMID 327539 abstract only | supports | The retained original abstract reports chuangxinmycin isolation from A. tsinanensis and biological/structural characterization. It does not establish the later MG824991.1 locus. |
| S133-E-2018-ABSTRACT | https://doi.org/10.1021/acs.jnatprod.7b00835; Original publisher abstract and SI listing | supports | The JNP primary abstract identifies the cxm cluster through heterologous expression and intermediate/gene-inactivation work. The detailed main body remains inaccessible. |
| S133-E-2018-SI | https://ndownloader.figshare.com/files/10823837; Complete SI text; strain/construct tables and original Figure S3/S4 pixels | supports | Complete official SI and original page 16 show exact final chuangxinmycin 1 in J1074/cxm and K4-114/cxm with host controls. Gene-inactivation constructs use heterologous A3(2). Native CPCC 240351 chromosomal knockout is not shown by these experiments. |
| S133-E-LOCUS | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=MG824991.1&amp;rettype=gb&amp;retmode=text; Header and all feature qualifiers/translations; ORIGIN not retranslated | supports | The exact 10,917 bp deposited cxm region names A. tsinanensis CPCC 240351 and the JNP 2018 study. Complete feature qualifiers were read; no independent sequence-level construct equality is asserted. |
| S133-E-OTHER-STOCK | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5925218/fullTextXML; Complete PMC5925218 scientific body, methods, tables/captions and references | supports | The separate complete cxn paper uses CPCC 200056. Native CxnR overexpression and heterologous M1146 CxnD truncation/rescue are specific to that context and cannot be transferred to CPCC 240351 merely from species identity. |
| S133-E-ACCESS | /private/tmp/npm-review-work/shared-next-batch014/review-support/source-notes-v2.json; Frozen bounded access/read scopes | unknown | Original 1977 body and JNP 2018 main were not recovered. Official SI and deposited sequence supply positive narrower evidence; no entire-paper absence inference follows. |
| S133-E-ADOPTION | /private/tmp/npm-review-work/133/local-sources.json; Actual official local-sources snapshot and guarded adoption reconciliation | context_only | Fresh selection, actual exit0 intake/strict receipts, root full-read receipt, exact target identity, complete owner equality and six captured source-set equality were required before adopting the prepared scientific scope. Other authority/root assessments and overall completion remain separately adjudicated. |
| C133-OWNER | data/natural_products/alkaloids/chuangxinmycin.yaml; Complete owner and all local-source rows; no referenced components | supports | The complete owner denotes (−)-chuangxinmycin under CHEBI:79391. Its exact source selector is BGC0001485:1, version 4, with complete parsed raw-row SHA256 9e50f70ed6d17242896d30d300b0752d12c7617640870ca4bba0399ed12bda86. The official intake and prepared owner bytes agree. |
| C133-GRAPH | /private/tmp/npm-review-work/133/chemistry.json; Fresh intake RDKit result and frozen Standard/fixed-H comparison | supports | The stored SMILES recomputes to DKHFLDXCKWDVMF-UPONEAKYSA-N, formula C12H11NO2S, formal charge 0; stored InChI/key agree. These are representation checks, not experimental identity proof. |
| C133-COMPARISON | /private/tmp/npm-review-work/shared-next-batch014/chemistry-prep/chemical-comparison.json; Record 133; exact source rows and each graph comparison | supports | Exact Standard, fixed-H, formula, charge and stereo comparisons of the retained owner, complete raw rows and current authority responses; primary experimental proof is assessed separately. |
| C133-LOCAL-SEARCH | /private/tmp/npm-review-work/133/chemistry-search-receipt.json; Exact full key, label, slug and source selector in raw/owner/curation trees | supports | Ignored-inclusive bounded search preserves all matching paths; an absent curation decision does not imply a missing scientific source. |
| C133-CHEBI-SEARCH-1 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=DKHFLDXCKWDVMF-UPONEAKYSA-N&amp;size=100; Literal key search; chebi-key-chuangxinmycin.json | supports | 1 returned name/key results; evaluate exact key and stars, not name similarity. |
| C133-CHEBI-SEARCH-2 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=%28%E2%88%92%29-chuangxinmycin&amp;size=100; Literal name search; chebi-name-chuangxinmycin.json | supports | 1 returned name/key results; evaluate exact key and stars, not name similarity. |
| C133-AUTH-1 | https://mibig.secondarymetabolites.org/repository/BGC0001485.4/annotations.json; compounds[].structure; BGC0001485.4.json | supports | current MIBiG BGC0001485:1: representation parses=True; parsed key DKHFLDXCKWDVMF-UPONEAKYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C133-AUTH-2 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/79391/; default_structure.smiles; CHEBI79391.json | context_only | ChEBI JSON 79391: representation parses=False; parsed key None; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C133-AUTH-3 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/79391/; official molfile endpoint; CHEBI79391-official.mol | supports | ChEBI MOL 79391: representation parses=True; parsed key DKHFLDXCKWDVMF-UPONEAKYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C133-SIBLING | https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/chuangxinmycin.yaml; Complete exact committed AntibioticMech owner and independently recomputed Git blob | supports | At commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976 the sibling identifier, valid InChI/full key and ANTIBACTERIAL class match. Its invalid literal SMILES is not used to prove identity; the valid InChI reproduces the owner Standard and fixed-H graph. The complete sibling has no mechanism graph or molecular-target fields. |
| C133-SIBLING-CHECK | /private/tmp/npm-review-work/shared-next-batch014/chemistry-prep/sibling-addendum-001/comparison.json; Pinned tree/blob, full inventory row, configured commit and exact link projection | supports | The public committed bytes match Git blob 6d628f9b5e86e7a587ce33d981936f1d26920e0c; the complete local row, shortened source_version and class-only seeder mapping reproduce the owner link and summary. No sibling checkout was accessed. |
| C133-PRIMARY-ORIGIN | PMID:327539; Original 1977 bibliographic abstract only | supports | The primary abstract reports chuangxinmycin isolation and structural characterization; it does not expose the detailed absolute-hand experiment. The owner definition and exact eligible ChEBI graph encode 2R,3S, but copied authority agreement is not a substitute for that protocol. |

## Limits And Additional Notes

- The root section inventories present claims and source routing; chemical identities, source-specific experiments, definition claims and optional sibling/activity assertions require their separately scoped scientific assessments.
- The original 1977 paper and detailed JNP 2018 main remain unavailable. Exact absolute-configuration and current sibling/authority comparisons belong to the independent chemistry packet.
- No optional protein/pathway absence is treated as a finding.
- Authority matches establish the representations actually returned at their retained access times; they are not independent experimental structure or absolute-hand determinations. Root and science sections separately assess organism, locus, classification and history claims.
- Current authority and literal identifier agreement is representation evidence. It neither supplies a missing natural absolute-hand experiment nor proves a specific producing stock.
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
review_id: 20261021T184823Z-chuangxinmycin
title: 'Chuangxinmycin: exact authority and sibling identity with locus-citation correction'
started_at: '2026-10-21T18:41:47.517924Z'
finished_at: '2026-10-21T18:48:23.822712Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The stored graph, eligible ChEBI MOL and valid InChI of the exact pinned
  AntibioticMech record agree; invalid upstream SMILES are not used as identity proof.
  Original production and antibacterial evidence remain appropriately scoped. The
  cxm locus incorrectly reuses the original compound-bioactivity citation instead
  of the recoverable 2018 study, a confirmed minor finding that fails the required
  citation check. Missing original stereochemical and detailed main-text evidence
  keeps the review partial; proposed correction preserves distinct native and heterologous
  stocks.
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
  - path: PLAN.md
    sha256: 5360993626369fec5462d45f3cfc68cb1653690ad72de10de6cad32d870e6035
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
  - path: data/natural_products/alkaloids/chlorizidine-a.yaml
    sha256: cabd7d83d653e3d654b5d50295b23c241d0cd9a7fd27e8b9707794701961183d
    role: context
  - path: data/natural_products/alkaloids/chrysogine.yaml
    sha256: ce45bc2502d8a7ee3fd67c527de804c159d93a5f7d484b90dfe4e4f185c197be
    role: context
  - path: data/natural_products/alkaloids/chuangxinmycin.yaml
    sha256: 36c51885afcfddf9394c244f4b88b5687c1557d7b1a04087db41126006af496d
    role: target
  - path: data/natural_products/alkaloids/cichorine.yaml
    sha256: 101e241cd5acb4d0c02a42db84cbaabbc03ab869d5b0c4d5fabea18af1d552a3
    role: context
  - path: data/natural_products/alkaloids/citridone-a.yaml
    sha256: f910abc10d84b3c48dac02b1861d45c0065869314116902be46c8428e63d589a
    role: context
  - path: data/natural_products/alkaloids/citridone-b-2.yaml
    sha256: fd5aa4ffd3ac824ecbc47379f9b1c8f7dbb49ed2968793d4acc090dd2a3e4695
    role: context
  - path: data/natural_products/alkaloids/citridone-b.yaml
    sha256: 8b4377a61db1fb773fd214ff55e3c62ebce361387fe812fb3ab6e2889844a240
    role: context
  - path: data/natural_products/alkaloids/cj-15-696.yaml
    sha256: fda593243686f09a350ff7e603bb4bfba5d678685dfde151ee2e0528dcddbbca
    role: context
  - path: data/natural_products/alkaloids/cj-16-173.yaml
    sha256: 7200f279eec270a9fa7f8976a078b809cff2b3f6594d6b1b2c76f4e866e9d795
    role: context
  - path: data/natural_products/alkaloids/cladoniamide-a.yaml
    sha256: cfc868919d5cc38ed1607726d5af2b7e49986e7703bb3cb8fe839f07f6d23971
    role: context
  - path: data/natural_products/alkaloids/cladoniamide-b.yaml
    sha256: ebf1d143c88e640e485cad9d9e61dec31a196ddbd8be287ab0afc071ed04b36b
    role: context
  - path: data/natural_products/alkaloids/cladoniamide-c.yaml
    sha256: eb4d74869ecd66c8ac1c3c09ab4e66ef3e1d2cf0207d53acb07733cf4898fc5f
    role: context
  - path: data/natural_products/alkaloids/cladoniamide-d.yaml
    sha256: 8f0d5db52d4d3b0630cc37ffcd014e084565e71ceaf40b5059536e5bd5e7b644
    role: context
  - path: data/natural_products/alkaloids/cladoniamide-e.yaml
    sha256: 1168e4142c33233dd96970d1eb3f96fd586744ff797966456ec105b2f66c7177
    role: context
  - path: data/natural_products/alkaloids/cladoniamide-f.yaml
    sha256: 5c677ca21eaa238f47eb732e36352dc4a781d351e5e724e7f0723d5675d3dc58
    role: context
  - path: data/natural_products/alkaloids/cladoniamide-g.yaml
    sha256: 6e4f7889efac34bc17f169d7c64850847595d2195d0bb9be94f463ac9bbaecd8
    role: context
  - path: data/natural_products/alkaloids/closoxazole-a.yaml
    sha256: 1ffa0b3e5e9581d47032c4d771045adba5287fdc621288537464a2d7b93f4b5d
    role: context
  - path: data/natural_products/alkaloids/closoxazole-b.yaml
    sha256: bc546837be7dc0d0c34602447f9de24ab507da8cc05ae2a900e7323a492c9f2e
    role: context
  - path: data/natural_products/alkaloids/closthioamide.yaml
    sha256: 0a19c731af050a326b5cdb447ed85c90e5cfca98b9a41cc215d7ae31c8c7d388
    role: context
  - path: data/natural_products/alkaloids/coenzyme-f430.yaml
    sha256: 8eed1aa5a67e40b5478c5edbd79a198c2684683b2cb19fe6302cbf7e7f85e92d
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
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
  - path: scripts/extract_antibioticmech.py
    sha256: 701314987037b1b82ef9539af731dcbb6ec2542b304058385014abb4339a3439
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
  - path: src/naturalproductmech/curate/lotus_exclusions.py
    sha256: 6352cac7c587eab5a56d907c523cc899d02d197009081624bf8649c675ee30f7
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
  - path: tests/test_claim_references.py
    sha256: 11b2fc60dbe32154df63fb2e8c784c7c8ba6585581c09bba2eebe2c5192d4c06
    role: context
  - path: tests/test_lotus_exclusions.py
    sha256: 3e3aa443714202e1bc41f0fb236e6bf69caabd68a16af23b972323f5f846386c
    role: context
  - path: tests/test_mibig_locus_evidence_overrides.py
    sha256: 9177b5bd24f6e47cc4743857179217d9e0d4add9560b2ce3faefaebe53ba09a0
    role: context
  - path: tests/test_producer_strains.py
    sha256: 17002ef1640464777f1925d12d842ed83c9098aad6de724ae0ea236ecccc4ff3
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 133, batch 014, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated targets in earlier
    batch commits (publication tracked separately). At selection, 184 of 3116 current
    records had campaign coverage and 2932 remained. The population search included
    ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:79391
targets:
- target_id: CHEBI:79391
  path: data/natural_products/alkaloids/chuangxinmycin.yaml
  label: (−)-chuangxinmycin
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
  - CHEBI:79391
  command: just validate-strict data/natural_products/alkaloids/chuangxinmycin.yaml
    --out /private/tmp/npm-review-work/133/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T18:41:49.157922Z
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
    for batch014 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch014. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:79391
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
    Reused for batch014 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch014. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:79391
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
    for batch014 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch014. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:79391
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
    for batch014 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch014. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:79391
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
    transcript: /private/tmp/npm-native-checks/batch-004/qc.log. Reused for batch014
    only after a fresh fetch/clean branch, equal commit/tree and two reads of all
    9,182 tracked byte streams and modes (208,070,649 bytes), including a recheck
    after the fresh authoritative catalogue. This gate was not rerun for batch014.
    Original execution times, scope, warnings, exceptions and skips are retained.'
  target_ids:
  - CHEBI:79391
- check_id: R133-FULL-OWNER
  name: Complete owner and captured-source scope
  status: passed
  required: true
  summary: Successful official intake and a fresh root full-owner/read receipt precede
    this authoring. All six officially captured sets and the separate seventh PubChem
    preparation match; the external component set is empty.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - R133-OWNER
  - R133-LOCAL
  - R133-PUBCHEM-PREP
- check_id: S133-C-CITATION
  name: Claim-local locus citation
  status: failed
  required: true
  summary: The imported COMPOUND_BIOACTIVITY citation is the 1977 study, whereas the
    stored cxm accession and exact heterologous experiments belong to JNP 2018.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - S133-E-RAW
  - S133-E-1977
  - S133-E-LOCUS
  - S133-E-2018-SI
- check_id: S133-C-MAIN
  name: Original isolation and detailed 2018 main access
  status: unavailable
  required: true
  summary: Full 1977 and JNP 2018 bodies remain unavailable; stock/chemical detail
    is not inferred beyond the retained positive abstract, official SI and deposit.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - S133-E-1977
  - S133-E-2018-ABSTRACT
  - S133-E-2018-SI
  - S133-E-ACCESS
- check_id: C133-C-REPRESENTATION
  name: Stored chemical representation and complete source row
  status: passed
  required: true
  summary: Fresh intake derivation agrees with the stored graph; the source selector,
    full row and prepared snapshot were independently rechecked.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - C133-OWNER
  - C133-GRAPH
  - C133-COMPARISON
- check_id: C133-C-LITERAL-XREFS
  name: Literal chemical identifiers and namespace resolution
  status: passed
  required: true
  summary: Each present literal NPAtlas or PubChem cross-reference returned the exact
    stored Standard and fixed-H graph. Legacy five-digit NPAtlas requests were queried
    literally and their returned canonical identifiers retained. ChEBI and Wikidata
    precision or tautomer differences are described separately.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - C133-COMPARISON
  - C133-AUTH-1
  - C133-AUTH-2
  - C133-AUTH-3
- check_id: C133-C-SIBLING
  name: Exact pinned sibling identity and link
  status: passed
  required: true
  summary: Exact committed valid InChI, configured commit, row and projected link/class
    agree; the invalid sibling SMILES remains a bounded source representation defect.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - C133-SIBLING
  - C133-SIBLING-CHECK
  - C133-GRAPH
- check_id: C133-C-ABSOLUTE
  name: Original exact absolute-hand protocol
  status: unavailable
  required: true
  summary: The detailed original 1977 body and hand determination were not recovered
    in the retained primary access. No opposite hand or unsupported source absence
    is inferred.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - C133-PRIMARY-ORIGIN
  - C133-COMPARISON
evidence:
- evidence_id: R133-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/chuangxinmycin.yaml
  locator: Complete post-intake owner, optional assertions and all history events
  accessed_at: '2026-10-21T18:42:56.783639Z'
  support: supports
  summary: 'Root read the complete owner after successful official intake: 1 occurrence,
    1 producer and 1 locus assertions. No referenced external component is present.
    Optional fields: definition, bioactivity_summary, related_records.'
  snapshot_sha256: 36c51885afcfddf9394c244f4b88b5687c1557d7b1a04087db41126006af496d
- evidence_id: R133-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/133/local-sources.json
  locator: Complete resolved owner and all six officially captured raw row sets
  accessed_at: '2026-10-21T18:42:56.783639Z'
  support: context_only
  summary: All six captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB and
    NPClassifier sets match the frozen preparation, including empty sets. The separate
    seventh PubChem inventory comparison is distinguished below. Source fidelity does
    not itself establish experimental support.
  snapshot_sha256: a9e7ffbcd39abf2286938b5d7a334c14faf655398b8f002de548a97eda4135ee
- evidence_id: R133-PUBCHEM-PREP
  kind: record_content
  reference: data/raw/pubchem_bioassay.tsv
  locator: Exact-key rows compared with the separate provisional seventh source set
  accessed_at: '2026-10-21T18:43:01.213568Z'
  support: context_only
  summary: The separate committed PubChem raw set contains 0 matching rows and reproduces
    the frozen preparation. This is not part of the official six-set intake. Empty
    or no-assay-data rows are not tested outcomes; no emitted assay assertion is inferred.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: R133-TAXON-CONTEXT
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=1048205,1288082,145745,162425,1883,2039464,227321,229533,29852,378258,446321,50193,50206,5073,5076,5081,5128,73504
  locator: Exact relevant TaxId, ScientificName, Rank, ParentTaxId and OtherNames
    fields
  accessed_at: '2026-10-21T18:06:35.286307Z'
  support: context_only
  summary: NCBI 2039464 is Actinoplanes tsinanensis. Its type material CPCC 200056
    does not by itself prove equivalence to experimental CPCC 240351; actual producing
    and genome-source stocks require the separately inspected primary/deposit bridge.
  snapshot_sha256: d9a4adfefcd1a126125ab99439e14c0972874451f3b99b65dc1f6073f3ef4ad9
- evidence_id: R133-IMODULON
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete 20-organism, 28-dataset official catalogue
  accessed_at: '2026-10-21T18:06:34.789679Z'
  support: context_only
  summary: The full retained catalogue establishes membership only. None of these
    exact native producer labels occurs in it. Listed Streptomyces coelicolor or E.
    coli datasets do not establish an introduced biosynthetic construct, recombinant
    protein or native production.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: S133-E-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/chuangxinmycin.yaml
  locator: Complete actual owner after official batch014 intake; exact resolved owner
    and all six captured source sets reconciled with frozen preparation
  accessed_at: '2026-10-21T18:42:56.783639Z'
  support: supports
  summary: The complete selected owner was read by root after successful official
    intake. Its resolved contents and all six captured raw sets equal the frozen source
    preparation. This adoption preserves original external retrieval times and does
    not reclassify old literature preparation as newly retrieved evidence.
  snapshot_sha256: 36c51885afcfddf9394c244f4b88b5687c1557d7b1a04087db41126006af496d
- evidence_id: S133-E-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: BGC0001485:1
  accessed_at: '2026-10-21T18:28:52.308417Z'
  support: supports
  summary: Exact raw row BGC0001485:1 was compared with the tentative snapshot. Complete
    parsed source-row SHA256 9e50f70ed6d17242896d30d300b0752d12c7617640870ca4bba0399ed12bda86
    includes all fields and empty values.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: S133-E-GRADING
  kind: record_content
  reference: conf/producer_evidence.tsv
  locator: Complete method vocabulary and inspected grading implementation
  accessed_at: '2026-10-21T18:28:52.308417Z'
  support: supports
  summary: The configured Knock-out studies label assumes loss of production in the
    native organism. Heterologous expression and Enzymatic assays support only the
    locus. Empty methods faithfully yield SOURCE_ASSERTION / CLUSTER_UNSTATED.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: S133-E-ROUTES
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch014/curator-routing/routing-notes.json
  locator: Complete static consumer feasibility notes, exact raw guards and flattened
    implementation pins
  accessed_at: '2026-10-21T18:28:52.308417Z'
  support: supports
  summary: Current consumers and static tests distinguish nonempty method REPLACE,
    seven-field WITHDRAW, full-row-pinned citation/strain context, and exact-triple
    occurrence exclusions. REPLACE expected_* fields alone are not enforced. No proposed
    curation or test was executed.
  snapshot_sha256: 26bf7b4ad7d6bbd8792ab2eb6bd1aa8e874c2cc11f7b5f510a9d7547ced8ca6d
- evidence_id: S133-E-1977
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/327539/
  locator: PMID 327539 abstract only
  accessed_at: '2026-10-21T17:40:30.669761Z'
  support: supports
  summary: The retained original abstract reports chuangxinmycin isolation from A.
    tsinanensis and biological/structural characterization. It does not establish
    the later MG824991.1 locus.
  snapshot_sha256: f30df3a13c35e2fae67c720a307c20fe05e694711cb2241188ce5347f3091c2a
- evidence_id: S133-E-2018-ABSTRACT
  kind: primary_source
  reference: https://doi.org/10.1021/acs.jnatprod.7b00835
  locator: Original publisher abstract and SI listing
  accessed_at: '2026-10-21T18:09:24Z'
  support: supports
  summary: The JNP primary abstract identifies the cxm cluster through heterologous
    expression and intermediate/gene-inactivation work. The detailed main body remains
    inaccessible.
  snapshot_sha256: 76af1cb48ffe8ccbd950e9ff6ccf066c44ade865d7f4cba7b1f13b9a49779de6
- evidence_id: S133-E-2018-SI
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/10823837
  locator: Complete SI text; strain/construct tables and original Figure S3/S4 pixels
  accessed_at: '2026-10-21T18:06:33.996489Z'
  support: supports
  summary: Complete official SI and original page 16 show exact final chuangxinmycin
    1 in J1074/cxm and K4-114/cxm with host controls. Gene-inactivation constructs
    use heterologous A3(2). Native CPCC 240351 chromosomal knockout is not shown by
    these experiments.
  snapshot_sha256: 69b008122519c39914e46373a3949df555c536f7edff392fb972fab25cebac0f
- evidence_id: S133-E-LOCUS
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=MG824991.1&rettype=gb&retmode=text
  locator: Header and all feature qualifiers/translations; ORIGIN not retranslated
  accessed_at: '2026-10-21T18:03:30.450153Z'
  support: supports
  summary: The exact 10,917 bp deposited cxm region names A. tsinanensis CPCC 240351
    and the JNP 2018 study. Complete feature qualifiers were read; no independent
    sequence-level construct equality is asserted.
  snapshot_sha256: e825587442b8ce09491ceef89e252b0acb2059497a86df19a199368ca0264c5b
- evidence_id: S133-E-OTHER-STOCK
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5925218/fullTextXML
  locator: Complete PMC5925218 scientific body, methods, tables/captions and references
  accessed_at: '2026-10-21T18:05:22.977981Z'
  support: supports
  summary: The separate complete cxn paper uses CPCC 200056. Native CxnR overexpression
    and heterologous M1146 CxnD truncation/rescue are specific to that context and
    cannot be transferred to CPCC 240351 merely from species identity.
  snapshot_sha256: 8099d40c830bd5b6fd0b00247a0048d3fa26f68c88d212584b36be673a210d9e
- evidence_id: S133-E-ACCESS
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch014/review-support/source-notes-v2.json
  locator: Frozen bounded access/read scopes
  accessed_at: '2026-10-21T18:28:52.308417Z'
  support: unknown
  summary: Original 1977 body and JNP 2018 main were not recovered. Official SI and
    deposited sequence supply positive narrower evidence; no entire-paper absence
    inference follows.
  snapshot_sha256: ae69a817b47ad86bbe78c791945216cb6ea03923bc68665cb2fdc43125853cc4
  search_scope: Exact DOI/PubMed, official Figshare SI, accession and public full-text
    routes documented in attempts 001–010. No repeat failed route or new network search
    during provisional drafting.
- evidence_id: S133-E-ADOPTION
  kind: record_content
  reference: /private/tmp/npm-review-work/133/local-sources.json
  locator: Actual official local-sources snapshot and guarded adoption reconciliation
  accessed_at: '2026-10-21T18:42:56.783639Z'
  snapshot_sha256: a9e7ffbcd39abf2286938b5d7a334c14faf655398b8f002de548a97eda4135ee
  support: context_only
  summary: Fresh selection, actual exit0 intake/strict receipts, root full-read receipt,
    exact target identity, complete owner equality and six captured source-set equality
    were required before adopting the prepared scientific scope. Other authority/root
    assessments and overall completion remain separately adjudicated.
- evidence_id: C133-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/chuangxinmycin.yaml
  locator: Complete owner and all local-source rows; no referenced components
  accessed_at: '2026-10-21T18:44:13.946145Z'
  support: supports
  summary: The complete owner denotes (−)-chuangxinmycin under CHEBI:79391. Its exact
    source selector is BGC0001485:1, version 4, with complete parsed raw-row SHA256
    9e50f70ed6d17242896d30d300b0752d12c7617640870ca4bba0399ed12bda86. The official
    intake and prepared owner bytes agree.
  snapshot_sha256: 36c51885afcfddf9394c244f4b88b5687c1557d7b1a04087db41126006af496d
- evidence_id: C133-GRAPH
  kind: validation
  reference: /private/tmp/npm-review-work/133/chemistry.json
  locator: Fresh intake RDKit result and frozen Standard/fixed-H comparison
  accessed_at: '2026-10-21T18:41:48.163964Z'
  support: supports
  summary: The stored SMILES recomputes to DKHFLDXCKWDVMF-UPONEAKYSA-N, formula C12H11NO2S,
    formal charge 0; stored InChI/key agree. These are representation checks, not
    experimental identity proof.
  snapshot_sha256: dc32c9f38bad8aacb134acf92385b4640bf5e10fce4e347a4cc5557c51f90405
- evidence_id: C133-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch014/chemistry-prep/chemical-comparison.json
  locator: Record 133; exact source rows and each graph comparison
  accessed_at: '2026-10-21T17:41:08.268885Z'
  support: supports
  summary: Exact Standard, fixed-H, formula, charge and stereo comparisons of the
    retained owner, complete raw rows and current authority responses; primary experimental
    proof is assessed separately.
  snapshot_sha256: 35270d1dd852f3ca15712a2ecb46220b711b9df3c549d4b721a79ee0121f0987
- evidence_id: C133-LOCAL-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/133/chemistry-search-receipt.json
  locator: Exact full key, label, slug and source selector in raw/owner/curation trees
  accessed_at: '2026-10-21T18:44:14.053878Z'
  support: supports
  summary: Ignored-inclusive bounded search preserves all matching paths; an absent
    curation decision does not imply a missing scientific source.
  snapshot_sha256: f05f476f36060cef10364efda15230297da2a6f3b6d9a183a6e24a92b002427f
  search_scope: rg --no-ignore --hidden; data/natural_products, data/raw and curation;
    exact full key, current label, slug and BGC:compound_index. No claim beyond these
    trees.
- evidence_id: C133-CHEBI-SEARCH-1
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=DKHFLDXCKWDVMF-UPONEAKYSA-N&size=100
  locator: Literal key search; chebi-key-chuangxinmycin.json
  accessed_at: '2026-10-21T17:40:14.551984Z'
  support: supports
  summary: 1 returned name/key results; evaluate exact key and stars, not name similarity.
  snapshot_sha256: 300e515174ba27631e7bdc704188871b72bec44621ff96f80468dded85816029
  search_scope: Official ChEBI es_search bounded key request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C133-CHEBI-SEARCH-2
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=%28%E2%88%92%29-chuangxinmycin&size=100
  locator: Literal name search; chebi-name-chuangxinmycin.json
  accessed_at: '2026-10-21T17:40:14.746218Z'
  support: supports
  summary: 1 returned name/key results; evaluate exact key and stars, not name similarity.
  snapshot_sha256: c7063618c9b64c51c784fca8bae40bab36befb50a23b7b06fee470e6d2ae5b11
  search_scope: Official ChEBI es_search bounded name request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C133-AUTH-1
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0001485.4/annotations.json
  locator: compounds[].structure; BGC0001485.4.json
  accessed_at: '2026-10-21T17:40:14.292344Z'
  support: supports
  summary: 'current MIBiG BGC0001485:1: representation parses=True; parsed key DKHFLDXCKWDVMF-UPONEAKYSA-N;
    exact stored Standard key match=True, fixed-H match=True. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: 3c8aca5d19cd7081e8e443cd427541889303cb76a5759ca65605607194e01d0a
- evidence_id: C133-AUTH-2
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/79391/
  locator: default_structure.smiles; CHEBI79391.json
  accessed_at: '2026-10-21T17:40:14.943850Z'
  support: context_only
  summary: 'ChEBI JSON 79391: representation parses=False; parsed key None; exact
    stored Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: b01b1c690ae43cf7e55736d7bfc0f3836e68e49a30b32515d3452ca3011f35dd
- evidence_id: C133-AUTH-3
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/79391/
  locator: official molfile endpoint; CHEBI79391-official.mol
  accessed_at: '2026-10-21T17:40:14.896035Z'
  support: supports
  summary: 'ChEBI MOL 79391: representation parses=True; parsed key DKHFLDXCKWDVMF-UPONEAKYSA-N;
    exact stored Standard key match=True, fixed-H match=True. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: 32d29927ed11a3cd57c8e2f41651dd8b15eb31cae4da2bf3ec98e1dd041d3139
- evidence_id: C133-SIBLING
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/chuangxinmycin.yaml
  locator: Complete exact committed AntibioticMech owner and independently recomputed
    Git blob
  accessed_at: '2026-10-21T18:30:19.690343Z'
  support: supports
  summary: At commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976 the sibling identifier,
    valid InChI/full key and ANTIBACTERIAL class match. Its invalid literal SMILES
    is not used to prove identity; the valid InChI reproduces the owner Standard and
    fixed-H graph. The complete sibling has no mechanism graph or molecular-target
    fields.
  snapshot_sha256: 518d2af245f40120e7567c57a30ca639d30ba71b1a01d23213c8608267f0d6d7
- evidence_id: C133-SIBLING-CHECK
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch014/chemistry-prep/sibling-addendum-001/comparison.json
  locator: Pinned tree/blob, full inventory row, configured commit and exact link
    projection
  accessed_at: '2026-10-21T18:31:11.117792Z'
  support: supports
  summary: The public committed bytes match Git blob 6d628f9b5e86e7a587ce33d981936f1d26920e0c;
    the complete local row, shortened source_version and class-only seeder mapping
    reproduce the owner link and summary. No sibling checkout was accessed.
  snapshot_sha256: c7679e9d4900c7cf2026109cdc7f75ee86a4f96d0cdaf218e0c3b902d805f455
- evidence_id: C133-PRIMARY-ORIGIN
  kind: primary_source
  reference: PMID:327539
  locator: Original 1977 bibliographic abstract only
  accessed_at: '2026-10-21T17:40:30.669761Z'
  support: supports
  summary: The primary abstract reports chuangxinmycin isolation and structural characterization;
    it does not expose the detailed absolute-hand experiment. The owner definition
    and exact eligible ChEBI graph encode 2R,3S, but copied authority agreement is
    not a substitute for that protocol.
  snapshot_sha256: f30df3a13c35e2fae67c720a307c20fe05e694711cb2241188ce5347f3091c2a
assessments:
- assessment_id: R133-HISTORY
  area: provenance
  topic: Native status and complete audit history
  outcome: supported
  summary: All 3 retained events are SEEDED_FROM_SOURCES. Native status remains SEEDED;
    these are provenance events, not earlier structured-review passes, and no scientific
    content or history is changed.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - R133-OWNER
- assessment_id: R133-OPTIONAL
  area: completeness
  topic: Complete optional-assertion inventory
  outcome: supported
  summary: The complete structure-specific definition, ANTIBACTERIAL summary and AntibioticMech
    SAME_STRUCTURE/SAME_INCHIKEY relation to CHEBI:79391 at source version 74f6cc836249
    are present. Their exact identity, pinned sibling and activity support require
    the chemistry/science assessments; this completeness inventory does not endorse
    them by presence alone. No assay observation or pathway is emitted.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - R133-OWNER
  - R133-LOCAL
- assessment_id: R133-FILING
  area: representation
  topic: Exact-key computed classification provenance
  outcome: supported
  summary: The exact-key NPClassifier projection and version npclassifier.gnps2.org@2026-09-07
    reproduce the owner filing, superclass/class labels and glycoside value false.
    Computed labels are not independent precursor, mechanism or natural-origin evidence.
    Any accepted new identity requires reclassification for its effective key.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - R133-OWNER
  - R133-LOCAL
- assessment_id: R133-TAXON-SCOPE
  area: provenance
  topic: Taxonomic names versus experimental stocks
  outcome: supported
  summary: NCBI 2039464 is Actinoplanes tsinanensis. Its type material CPCC 200056
    does not by itself prove equivalence to experimental CPCC 240351; actual producing
    and genome-source stocks require the separately inspected primary/deposit bridge.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - R133-TAXON-CONTEXT
  - R133-OWNER
- assessment_id: R133-IMODULON-SCOPE
  area: completeness
  topic: Producer transcriptomic applicability
  outcome: not_applicable
  summary: No exact native producer species/strain dataset is represented in the inspected
    catalogue. Related species and possible experimental hosts do not establish a
    construct/condition match; no gene/module or compound-production inference is
    made.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - R133-OWNER
  - R133-IMODULON
- assessment_id: S133-A-PRODUCER
  area: evidence
  topic: Native production and deposited source stock
  outcome: supported
  summary: The original A. tsinanensis production assertion remains supported at its
    species/abstract resolution. The accession names CPCC 240351; this does not equate
    it with CPCC 200056 or prove native knockout.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - S133-E-1977
  - S133-E-LOCUS
  - S133-E-OTHER-STOCK
  dimensions:
  - name: native_vs_heterologous_context
    value: CPCC 240351 cxm deposit; J1074/K4-114 final-product hosts; A3(2) gene-inactivation
      host
    definition: Keep CPCC 200056/cxn experiments separate.
    evidence_ids:
    - S133-E-LOCUS
    - S133-E-2018-SI
    - S133-E-OTHER-STOCK
- assessment_id: S133-A-LOCUS
  area: evidence
  topic: Exact cxm evidence and two grading tiers
  outcome: concern
  summary: The empty imported methods are faithful, but a recoverable exact locus
    citation and heterologous final-product experiment are omitted from the claim.
    A source-pinned citation/method correction can preserve the native SOURCE_ASSERTION
    while documenting CLUSTER_DEMONSTRATED.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - S133-E-RAW
  - S133-E-GRADING
  - S133-E-LOCUS
  - S133-E-2018-SI
  - S133-E-ROUTES
  dimensions:
  - name: producer_locus_evidence_tiers
    value: Current SOURCE_ASSERTION / CLUSTER_UNSTATED; supported heterologous enrichment
      only
    definition: The producer is not promoted by heterologous expression.
    evidence_ids:
    - S133-E-RAW
    - S133-E-GRADING
    - S133-E-2018-SI
- assessment_id: S133-A-OCCURRENCE
  area: scope
  topic: Original occurrence and activity scope
  outcome: supported
  summary: The ChEBI occurrence cites the original 1977 isolation, which remains an
    appropriate species-level source; it should not be replaced simply because it
    predates the locus. ANTIBACTERIAL is compatible with the source abstract. The
    exact sibling SAME_STRUCTURE link is handled by independent chemistry/context
    review, not a transfer of detailed mechanisms.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - S133-E-OWNER
  - S133-E-1977
- assessment_id: C133-A-IDENTITY
  area: identity
  topic: Stored representation and source-concept provenance
  outcome: supported
  summary: The complete source row BGC0001485:1 and source-concept hash reproduce
    this stored representation; this does not establish that the upstream compound
    label is correct. Formula, charge, Standard and fixed-H distinctions are independently
    recorded. Primary support and any conflicting exact xref are assessed separately.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - C133-OWNER
  - C133-GRAPH
  - C133-COMPARISON
  dimensions:
  - name: mibig_source_selector
    value: BGC0001485:1
    definition: Accession plus compound_index, distinct from the entry-level accession.
    evidence_ids:
    - C133-OWNER
  - name: complete_raw_row_sha256
    value: 9e50f70ed6d17242896d30d300b0752d12c7617640870ca4bba0399ed12bda86
    definition: Sorted compact ASCII JSON of every parsed TSV field, including empty
      values.
    evidence_ids:
    - C133-OWNER
- assessment_id: C133-A-GROUNDING
  area: provenance
  topic: Exact authority eligibility and source representation
  outcome: supported
  summary: Exactly one committed three-star default ChEBI row matches; its current
    graph is checked separately.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - C133-OWNER
  - C133-COMPARISON
  - C133-LOCAL-SEARCH
  - C133-CHEBI-SEARCH-1
  - C133-CHEBI-SEARCH-2
- assessment_id: C133-A-AUTHORITY-REPRESENTATION
  area: representation
  topic: Official MOL, JSON SMILES and chemical Wikidata fields
  outcome: supported
  summary: The retained comparisons distinguish valid official MOL structures from
    default JSON SMILES that fail parsing. Only exact eligible three-star rows can
    ground this corpus. Canonical Wikidata P233, isomeric P2017 and declared InChI/key
    fields are separate assertions; a matching Standard key does not guarantee fixed-H
    identity. No invalid JSON SMILES is proposed for copying.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - C133-COMPARISON
  - C133-AUTH-1
  - C133-AUTH-2
  - C133-AUTH-3
- assessment_id: C133-A-EXACT
  area: identity
  topic: Exact eligible authority and historical sibling identity
  outcome: supported
  summary: The owner valid graph, eligible CHEBI:79391 official MOL and pinned sibling
    valid InChI agree on full identity. Invalid default JSON/sibling SMILES must not
    be copied. Primary experimental absolute certainty is separately unknown.
  target_ids:
  - CHEBI:79391
  evidence_ids:
  - C133-GRAPH
  - C133-COMPARISON
  - C133-SIBLING
  - C133-SIBLING-CHECK
findings:
- finding_id: S133-F-ROUTING
  issue_key: mibig-bgc0001485-citation-method-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The locus uses an original compound-bioactivity citation
  description: The source-faithful empty grade is not false, but the locus reuses
    the 1977 compound-bioactivity reference instead of the recoverable 2018 cxm study
    and its exact heterologous product support.
  target_ids:
  - CHEBI:79391
  field_paths:
  - biosynthetic_gene_clusters[0].evidence[0]
  - biosynthetic_gene_clusters[0].link_evidence_basis
  - producer_organisms[0].evidence[0]
  evidence_ids:
  - S133-E-RAW
  - S133-E-1977
  - S133-E-LOCUS
  - S133-E-2018-SI
  - S133-E-ROUTES
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Separate original producer and modern locus citations with full-row guard
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Exact heterologous method enrichment
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Consumed full-row and claim-local provenance guard
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Paired citation/method emission
actions:
- action_id: S133-ACT-ROUTING
  finding_ids:
  - S133-F-ROUTING
  target_ids:
  - CHEBI:79391
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Separate original producer and modern locus citations with full-row guard
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Exact heterologous method enrichment
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Consumed full-row and claim-local provenance guard
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Paired citation/method emission
  generator: scripts/seed_from_sources.py
  description: 'Use BGC0001485:1 and complete raw SHA256 9e50f70ed6d17242896d30d300b0752d12c7617640870ca4bba0399ed12bda86
    in mibig_claim_references.tsv: producer_reference PMID:327539, locus_reference
    PMID:29565122, source_reference DOI:10.1021/acs.jnatprod.7b00835, with explicit
    source-stock/host limits. Pair with REPLACE Heterologous expression for naturalproductmech:mibig-9cbda6ee27
    only after accepting the deposited cxm-to-tested-construct bridge at the documented
    resolution. The consumed citation row supplies the full-row guard omitted by legacy
    REPLACE. Preserve the original url-prefixed citation/reference_basis in raw history;
    use valid PMID/DOI forms in the new table. Do not transfer CPCC 200056 or heterologous
    deletions into native Knock-out studies.'
  acceptance_checks:
  - The original producer/occurrence citation remains local to original isolation;
    the 2018 citation reaches the locus.
  - Original raw bytes and COMPOUND_BIOACTIVITY provenance are retained.
  - The combined rows fail on any full source-row drift; source identity and chemistry
    are unchanged.
  - No native producer upgrade or cross-stock equality is emitted; full-main limits
    remain explicit.
  - Future authorized canary, reproduction and QC demonstrate both decisions compose
    and target only BGC0001485:1.
limitations:
- The root section inventories present claims and source routing; chemical identities,
  source-specific experiments, definition claims and optional sibling/activity assertions
  require their separately scoped scientific assessments.
- The original 1977 paper and detailed JNP 2018 main remain unavailable. Exact absolute-configuration
  and current sibling/authority comparisons belong to the independent chemistry packet.
- No optional protein/pathway absence is treated as a finding.
- Authority matches establish the representations actually returned at their retained
  access times; they are not independent experimental structure or absolute-hand determinations.
  Root and science sections separately assess organism, locus, classification and
  history claims.
- Current authority and literal identifier agreement is representation evidence. It
  neither supplies a missing natural absolute-hand experiment nor proves a specific
  producing stock.
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
- batch-014
```
