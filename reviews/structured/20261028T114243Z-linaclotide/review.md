# Scientific review of linaclotide

- Review: 20261028T114243Z-linaclotide
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-28T11:15:38.481449Z
- Finished UTC: 2026-10-28T11:42:43.002948Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Linaclotide’s exact parent identity and internal encodings agree with the inspected authority. GC-C pharmacology has own abstract support. The retained natural-origin, E. coli producer and occurrence assertions conflict with exact-parent authority classification and require curation; the full 1989 primary was unavailable, so the cause and any replacement remain unresolved.

## Scope And Provenance

Whole current owner and exact retained/current intake sources, saved internal chemistry and specifically inspected own metadata, primary passages and authority within stated applicability limits.

Selection: One exact owner selected from the unreviewed corpus in canonical path order; whole local owner and retained rows were read, with the bounded scientific verification described here.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:68551 | data/natural_products/amino_acids_and_peptides/linaclotide.yaml | generated | linaclotide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | CHEBI:68551 | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | CHEBI:68551 | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | CHEBI:68551 | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:68551 | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | CHEBI:68551 | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | CHEBI:68551 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Whole owner and exact retained source joins | passed | True | CHEBI:68551 | The whole current owner and exact source joins agree: one MIBiG compound row, one LOTUS occurrence row, one exact-key ChEBI structure row, one NPClassifier row and five PubChem rows. The official intake arrays contain four rows and the assay rows remain separately retained. The two human GC-C entries cite the same AID with different references, not two demonstrated independent experiments. Five seed-history entries do not validate natural origin. |
| Saved representation consistency | passed | True | CHEBI:68551 | Saved SMILES, Standard InChI and the retained exact-key ChEBI alternative agree internally on KXGCNMMJRFDFNR-WDRJZQOASA-N and C59H79N15O21S6; current intake agrees. Both owner encodings have 14 specified tetrahedral centres, consistent with the retained stereo_complete flag. The additional InChI-local C(-O)=N labels are representation diagnostics, not evidence of missing natural carbon configurations. This validates representation consistency, not biological origin. |
| Exact-parent authority identification | passed | True | CHEBI:68551 | The exact full key agrees with the retained ChEBI parent and the inspected IUPHAR/BPS ligand 5017 authority. This supports parent identification and distinguishes the acetate entry. It does not prove natural biosynthesis, occurrence or an independently measured complete natural configuration. |
| Exact-parent biological-origin support | failed | True | CHEBI:68551 | The exact-parent authority calls linaclotide a synthetic analogue, while the owner asserts NATURAL_PRODUCT with E. coli production and occurrence. This is a confirmed material source-applicability conflict. Its cause and natural absence remain unproved; neither automatic SYNTHETIC replacement nor a wrong-structure conclusion is justified. |
| Exact-parent producer applicability | unavailable | True | CHEBI:68551 | The retained MIBiG E. coli assertion resolves to the same 1989 work as the LOTUS DOI. Own metadata and front matter establish that publication identity, but do not establish natural production of this exact linaclotide parent. They are not two independent confirmations. No taxon replacement or universal nonproduction conclusion is selected. |
| Exact-parent locus applicability | unavailable | True | CHEBI:68551 | BGC0000621 version 3, M18346.1 and the RIBOSOMAL label are retained source assertions graded CLUSTER_UNSTATED, with no stored interval. Their applicability to this exact analogue remains unresolved. The own PMC response contains no substantive body, and no sequence, engineering procedure or inferred locus mechanism is extracted. |
| Exact-parent occurrence applicability | unavailable | True | CHEBI:68551 | The exact-key LOTUS E. coli triple is faithfully retained but its 1989 citation does not establish exact-parent occurrence in the inspected material. Occurrence and production need separate adjudication; the authority/record conflict does not by itself prove the LOTUS citation false or authorize exclusion. |
| Chemical class and definition scope | passed | True | CHEBI:68551 | The cyclic-peptide classification and retained ChEBI parent description are consistent with the internally matching encodings and exact-parent authority. Computational classification and the historical therapeutic definition do not establish natural origin or current clinical guidance. The RIBOSOMAL source assertion is assessed separately as an unresolved exact-parent locus relation. |
| Original assay calls and endpoints | passed | True | CHEBI:68551 | The five PubChem rows preserve the human and rat GC-C active annotations and two separate screening results. The CHIKV row remains INACTIVE with source Potency 3.0458 uM; the SARS-S pseudoparticle row remains inconclusive/NOT_DETERMINED with Potency 19.9526 uM. Neither number establishes positive inhibition or a verified molecular target mechanism. The two human GC-C rows share AID 1345486; publication count is not experiment count. |
| Named-drug GC-C pharmacology | passed | True | CHEBI:68551 | The own PubMed abstract reports human T84 GC-C receptor-binding Ki values of 1.23–1.64 nM and a distinct intracellular cGMP functional EC50 of 99 nM. Rat secretion/transit context is not a rat-receptor affinity measurement. These endpoints support pharmacological applicability to the named drug, not natural origin, and are not inserted into blank raw assay-value fields. |
| Assay-specific quantitative and target grounding | unavailable | True | CHEBI:68551 | The original individual assay pages and species-specific target accession mappings were not independently verified. Human-cell binding Ki and functional EC50 remain distinct; no human potency is assigned to the rat row. The retained viral UniProt labels are source annotations and the inactive/inconclusive calls do not establish a positive antiviral mechanism. |
| Optional graph and pathway detail | unavailable | False | CHEBI:68551 | No detailed pathway or causal graph is present. Named-drug GC-C pharmacology is supported at abstract level, while exact-parent biosynthetic mechanism is unresolved. Empty optional fields are not themselves defects and related enterotoxin mechanisms are not transferred to this parent. |
| Source tiers, history and grounding | passed | True | CHEBI:68551 | Current owner, source concepts, retained row placements, original timestamps and seed history are preserved. Exact database/key joins and mechanical intake success establish reproducible provenance, not full scientific correctness. Bibliography entries are not own publication aliases; retained source citation levels and inspected primary/authority tiers remain explicit. |
| Remaining source and authority limits | unavailable | True | CHEBI:68551 | Independent complete configuration, all current authority mappings and uninspected source material remain outside verified scope. Required unavailable checks remain explicit; no optional absence, source access failure or baseline pass is converted into a scientific finding. |

## Scientific And Domain Assessments

### Whole owner and exact retained source joins

provenance: supported. Targets: CHEBI:68551.

The whole current owner and exact source joins agree: one MIBiG compound row, one LOTUS occurrence row, one exact-key ChEBI structure row, one NPClassifier row and five PubChem rows. The official intake arrays contain four rows and the assay rows remain separately retained. The two human GC-C entries cite the same AID with different references, not two demonstrated independent experiments. Five seed-history entries do not validate natural origin.

### Saved representation consistency

representation: supported. Targets: CHEBI:68551.

Saved SMILES, Standard InChI and the retained exact-key ChEBI alternative agree internally on KXGCNMMJRFDFNR-WDRJZQOASA-N and C59H79N15O21S6; current intake agrees. Both owner encodings have 14 specified tetrahedral centres, consistent with the retained stereo_complete flag. The additional InChI-local C(-O)=N labels are representation diagnostics, not evidence of missing natural carbon configurations. This validates representation consistency, not biological origin.

### Exact-parent authority identification

representation: supported. Targets: CHEBI:68551.

The exact full key agrees with the retained ChEBI parent and the inspected IUPHAR/BPS ligand 5017 authority. This supports parent identification and distinguishes the acetate entry. It does not prove natural biosynthesis, occurrence or an independently measured complete natural configuration.

### Exact-parent biological-origin support

evidence: concern. Targets: CHEBI:68551.

The exact-parent authority calls linaclotide a synthetic analogue, while the owner asserts NATURAL_PRODUCT with E. coli production and occurrence. This is a confirmed material source-applicability conflict. Its cause and natural absence remain unproved; neither automatic SYNTHETIC replacement nor a wrong-structure conclusion is justified.

### Exact-parent producer applicability

evidence: concern. Targets: CHEBI:68551.

The retained MIBiG E. coli assertion resolves to the same 1989 work as the LOTUS DOI. Own metadata and front matter establish that publication identity, but do not establish natural production of this exact linaclotide parent. They are not two independent confirmations. No taxon replacement or universal nonproduction conclusion is selected.

### Exact-parent locus applicability

evidence: unknown. Targets: CHEBI:68551.

BGC0000621 version 3, M18346.1 and the RIBOSOMAL label are retained source assertions graded CLUSTER_UNSTATED, with no stored interval. Their applicability to this exact analogue remains unresolved. The own PMC response contains no substantive body, and no sequence, engineering procedure or inferred locus mechanism is extracted.

### Exact-parent occurrence applicability

evidence: concern. Targets: CHEBI:68551.

The exact-key LOTUS E. coli triple is faithfully retained but its 1989 citation does not establish exact-parent occurrence in the inspected material. Occurrence and production need separate adjudication; the authority/record conflict does not by itself prove the LOTUS citation false or authorize exclusion.

### Chemical class and definition scope

representation: supported. Targets: CHEBI:68551.

The cyclic-peptide classification and retained ChEBI parent description are consistent with the internally matching encodings and exact-parent authority. Computational classification and the historical therapeutic definition do not establish natural origin or current clinical guidance. The RIBOSOMAL source assertion is assessed separately as an unresolved exact-parent locus relation.

### Original assay calls and endpoints

evidence: supported. Targets: CHEBI:68551.

The five PubChem rows preserve the human and rat GC-C active annotations and two separate screening results. The CHIKV row remains INACTIVE with source Potency 3.0458 uM; the SARS-S pseudoparticle row remains inconclusive/NOT_DETERMINED with Potency 19.9526 uM. Neither number establishes positive inhibition or a verified molecular target mechanism. The two human GC-C rows share AID 1345486; publication count is not experiment count.

### Named-drug GC-C pharmacology

evidence: supported. Targets: CHEBI:68551.

The own PubMed abstract reports human T84 GC-C receptor-binding Ki values of 1.23–1.64 nM and a distinct intracellular cGMP functional EC50 of 99 nM. Rat secretion/transit context is not a rat-receptor affinity measurement. These endpoints support pharmacological applicability to the named drug, not natural origin, and are not inserted into blank raw assay-value fields.

### Assay-specific quantitative and target grounding

evidence: unknown. Targets: CHEBI:68551.

The original individual assay pages and species-specific target accession mappings were not independently verified. Human-cell binding Ki and functional EC50 remain distinct; no human potency is assigned to the rat row. The retained viral UniProt labels are source annotations and the inactive/inconclusive calls do not establish a positive antiviral mechanism.

### Optional graph and pathway detail

completeness: unknown. Targets: CHEBI:68551.

No detailed pathway or causal graph is present. Named-drug GC-C pharmacology is supported at abstract level, while exact-parent biosynthetic mechanism is unresolved. Empty optional fields are not themselves defects and related enterotoxin mechanisms are not transferred to this parent.

### Source tiers, history and grounding

provenance: supported. Targets: CHEBI:68551.

Current owner, source concepts, retained row placements, original timestamps and seed history are preserved. Exact database/key joins and mechanical intake success establish reproducible provenance, not full scientific correctness. Bibliography entries are not own publication aliases; retained source citation levels and inspected primary/authority tiers remain explicit.

### Remaining source and authority limits

completeness: unknown. Targets: CHEBI:68551.

Independent complete configuration, all current authority mappings and uninspected source material remain outside verified scope. Required unavailable checks remain explicit; no optional absence, source access failure or baseline pass is converted into a scientific finding.

## Findings

### F820-EXACT-PARENT-ORIGIN-SUPPORT-CONFLICT: Exact-parent linaclotide origin assertions require reconciliation

major / open / confirmed; issue key: linaclotide-chebi68551-exact-parent-natural-origin-support-conflict.

The retained linaclotide parent, keyed KXGCNMMJRFDFNR-WDRJZQOASA-N, is labelled NATURAL_PRODUCT and linked to E. coli production and occurrence. The IUPHAR/BPS entry bearing that exact full key classifies linaclotide as a synthetic analogue of bacterial enterotoxins. The retained MIBiG and LOTUS citations resolve to one1989 enterotoxin publication; the inspected own metadata/front matter does not establish natural production or occurrence of this exact parent. This confirms a material conflict in source applicability that prevents treating the retained biological-origin claims as scientifically resolved. Conflation of a related natural parent family with this analogue is a provisional explanation, not a demonstrated upstream cause. Synthetic manufacture alone does not prove universal natural absence; the inaccessible full primary prevents a definitive source-misassignment judgment. No replacement structure, origin value, taxon, salt equivalence or exclusion is selected.

## Recommended Actions And Acceptance Checks

### A820-RECONCILE-EXACT-PARENT-ORIGIN

Reconcile the exact parent identity and natural-origin evidence before changing its source-to-record admission, producer, occurrence or locus assertions. Preserve original source rows and held attempts; implement only separately adjudicated, reproducible corrections.

- Reproduce the exact full-key join to IUPHAR ligand5017 and the complete retained MIBiG BGC0000621:1 version3 and LOTUS E. coli/1989 DOI rows. Keep the parent and acetate identifiers separate.
- Determine whether an inspected primary or authoritative exact-material source supports natural occurrence or biosynthesis of this parent rather than a related family, synthetic analogue, manufactured preparation or salt. Preserve inaccessible-source limitations; do not equate manufacture with proof of natural absence.
- Keep PMID2643580 and DOI10.1128/iai.57.2.645-648.1989 as one publication. Do not infer exact source misassignment from metadata or bodyless access alone, and do not retrieve procedures or engineering details for this review.
- Reassess biological origin, producer, occurrence and locus applicability separately. A pharmacological GC-C observation may remain relevant to the exact drug even if a natural-origin assertion is withdrawn; distinguish binding and functional endpoints and retain inactive/inconclusive assay calls.
- If a particular LOTUS triple is demonstrated unsupported, use only the documented full-row-pinned occurrence exclusion after separate authorization. Citation rerouting, locus-evidence grading or a structure correction must not be used as an implicit origin replacement.
- If the verified origin correction needs a new maintained-input or admission rule, review and test that implementation before migration. Do not use reserved decisions.tsv, edit generated YAML directly, choose SYNTHETIC automatically or silently rewrite raw inventories.
- After separately authorized curation, run the appropriate seed canary, guarded reproduction and documented validation gates; preserve applicable claims, graphs and history. No lifecycle invocation is performed by this proposal.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI820-LOCAL | /private/tmp/npm-review-work/shared-next-batch082-tentative/tentative-owner-source-inventory-001.json; /entries/9/owner_document; /entries/9/rows; /entries/9/supplemental_retained_rows; /entries/9/expected_official_intake_rows | context_only | The whole current owner and exact source joins agree: one MIBiG compound row, one LOTUS occurrence row, one exact-key ChEBI structure row, one NPClassifier row and five PubChem rows. The official intake arrays contain four rows and the assay rows remain separately retained. The two human GC-C entries cite the same AID with different references, not two demonstrated independent experiments. Five seed-history entries do not validate natural origin. |
| SCI820-ENCODINGS | /private/tmp/npm-review-work/shared-next-batch082-tentative/source-science-preparation/root-tentative82-local-chemical-consistency-and-neighbors-001.json; /records/9/smiles; /records/9/inchi; /records/9/comparisons; /records/9/chebi_alternatives | supports | Saved SMILES, Standard InChI and the retained exact-key ChEBI alternative agree internally on KXGCNMMJRFDFNR-WDRJZQOASA-N and C59H79N15O21S6; current intake agrees. Both owner encodings have 14 specified tetrahedral centres, consistent with the retained stereo_complete flag. The additional InChI-local C(-O)=N labels are representation diagnostics, not evidence of missing natural carbon configurations. This validates representation consistency, not biological origin. |
| CAND820-EXACT-PARENT-AUTHORITY | https://www.guidetopharmacology.org/GRAC/LigandDisplayForward?ligandId=5017&amp;tab=structure; Saved IUPHAR/BPS ligand5017 structure extraction L68-L70 and L83; tool-call bounds, not raw HTTP clocks | partial | The authority assigns the retained full InChIKey to linaclotide and calls that ligand a synthetic analogue of bacterial heat-stable enterotoxins. It distinguishes the parent ligand from its acetate form. This is an exact-identifier database assertion, not new chemical computation or proof of universal natural absence. |
| CAND820-RETAINED-ORIGIN-CONTEXT | /private/tmp/npm-review-work/shared-next-batch082-tentative/tentative-owner-source-inventory-001.json; /entries/9/owner_document; /entries/9/rows/mibig_compounds/0; /entries/9/rows/lotus_occurrences/0; /entries/9/rows/chebi_structures/0 | supports | The exact retained parent has NATURAL_PRODUCT origin, an E. coli producer assertion from BGC0000621:1 version3 and an E. coli LOTUS occurrence. The producer grade is SOURCE_ASSERTION and the locus CLUSTER_UNSTATED. MIBiG cites PMID2643580 and LOTUS cites its own verified1989 DOI; these are one publication, not independent corroboration. |
| CAND820-OWN-1989-METADATA | PMID:2643580; Own MedlineCitation/Article title and abstract; own PubmedData/ArticleIdList | partial | Own metadata verifies PMID2643580, the retained1989 DOI and PMC313148. It concerns E. coli enterotoxin alleles; it does not identify linaclotide as the exact naturally produced parent. No sequence, residue changes or experimental procedure are extracted. |
| CAND820-OWN-PRIMARY-LIMIT | PMCID:PMC313148; Own JATS front/article-meta identifiers/title/abstract; body absent | context_only | The HTTP200 response matches the own publication IDs but contains front matter and abstract only. The original bodyless guard failure is held. This limits source adjudication and is not a scientific refutation, nor authority for a sequence-based source-misassignment conclusion. |
| CAND820-ADMISSION-RUBRIC | CLAUDE.md; docs/record-reviews.md; Semantic invariants: origin assertion; Verdict And Severity: major | context_only | Admission requires an origin assertion applicable to the record, while materially unsupported claims or scope inflation are major. The present concern is exact-parent origin support; wrong natural identity or universal absence is not established. |
| CAND820-GENERATED-ORIGIN-INTERFACE | scripts/seed_from_sources.py; Current read lines988-1002: initial MIBiG-derived document and NATURAL_PRODUCT field | context_only | The inspected document-construction callsite emits NATURAL_PRODUCT from the retained source group. It identifies the generator boundary for a future reviewed fix, without proving the upstream cause or a general defect across unrelated records. |
| CAND820-MAINTAINED-CORRECTION-BOUNDARY | docs/CURATION.md; Decision file; MIBiG claim-specific reference corrections; LOTUS occurrence exclusions | context_only | Existing citation-routing and LOTUS exclusion interfaces are narrow and require independently supported, exact-row decisions. Neither supplies an automatic origin replacement; reserved decisions.tsv is not consumed. Preserve original inventories and use a reviewed implemented harmonization path. |
| SCI820-PM17694454 | PMID:17694454; ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract | partial | The own historical title/abstract names linaclotide as a therapeutic GC-C agonist. It does not establish the exact parent’s natural producer, locus, complete experimental structure or current treatment guidance. |
| SCI820-PM20863829 | PMID:20863829; ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText | partial | The own PubMed abstract reports human T84 GC-C receptor-binding Ki values of 1.23–1.64 nM and a distinct intracellular cGMP functional EC50 of 99 nM. Rat secretion/transit context is not a rat-receptor affinity measurement. These endpoints support pharmacological applicability to the named drug, not natural origin, and are not inserted into blank raw assay-value fields. |
| SCI820-ASSAY-ROWS | data/raw/pubchem_bioassay.tsv; exact retained CID16158208 rows 3521..3525; inventory /entries/9/rows/pubchem_bioassay | partial | The five PubChem rows preserve the human and rat GC-C active annotations and two separate screening results. The CHIKV row remains INACTIVE with source Potency 3.0458 uM; the SARS-S pseudoparticle row remains inconclusive/NOT_DETERMINED with Potency 19.9526 uM. Neither number establishes positive inhibition or a verified molecular target mechanism. The two human GC-C rows share AID 1345486; publication count is not experiment count. |

## Limits And Additional Notes

- The exact IUPHAR parent key and synthetic-analogue classification are verified in a saved web extraction. Tool-call bounds are not raw HTTP clocks; the FDA oversized-fetch failure supplies no scientific evidence.
- The 1989 own PubMed/PMC identifiers match, but the PMC response is front matter and abstract only. Missing body is an access limitation, not scientific refutation or proof of a wrong citation.
- Confirmed refers to the exact-parent authority/current-record support conflict. Universal natural absence, upstream conflation, wrong structure, salt equivalence, taxon replacement and automatic SYNTHETIC classification remain unproved.
- Own pharmacological abstracts are metadata-level evidence. Species, assay-material identity, binding and functional endpoints remain distinct; inactive and inconclusive screening calls are preserved.
- No primary sequence, residue-level engineering detail, manufacturing procedure or experimental protocol is extracted. No source or generated record is changed.
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
- Original owner/source reading, two-encoding computation, neighbor inspection, HTTP retrieval and later metadata reading retain separate clocks. Official intake separately computed SMILES facts.
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
review_id: 20261028T114243Z-linaclotide
title: Scientific review of linaclotide
started_at: '2026-10-28T11:15:38.481449Z'
finished_at: '2026-10-28T11:42:43.002948Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: Linaclotide’s exact parent identity and internal encodings agree with the
  inspected authority. GC-C pharmacology has own abstract support. The retained natural-origin,
  E. coli producer and occurrence assertions conflict with exact-parent authority
  classification and require curation; the full 1989 primary was unavailable, so the
  cause and any replacement remain unresolved.
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
  - path: data/natural_products/amino_acids_and_peptides/linaclotide.yaml
    sha256: 52e2e744275166e9b64123304aa7b03ede0f68f49290c17fad04ac038b9fc97e
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
- target_id: CHEBI:68551
  path: data/natural_products/amino_acids_and_peptides/linaclotide.yaml
  label: linaclotide
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
    path: data/natural_products/amino_acids_and_peptides/linaclotide.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
scope:
  description: Whole current owner and exact retained/current intake sources, saved
    internal chemistry and specifically inspected own metadata, primary passages and
    authority within stated applicability limits.
  selection: One exact owner selected from the unreviewed corpus in canonical path
    order; whole local owner and retained rows were read, with the bounded scientific
    verification described here.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CHEBI:68551
  exclusions:
  - target: Complete independent natural configuration and uninspected figure/SI evidence
    reason: Outside the inspected evidence and bounded scientific verification of
      this review.
  - target: Unverified current authority, stock or locus-coordinate assignments
    reason: Outside the inspected evidence and bounded scientific verification of
      this review.
  - target: Activity or mechanism transfer across congeners, taxa, salts or assay
      endpoints
    reason: Outside the inspected evidence and bounded scientific verification of
      this review.
  - target: Operational production, sequence engineering or assay procedures
    reason: Outside the inspected evidence and bounded scientific verification of
      this review.
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
    Reused for batch082 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch082. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:68551
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
    Reused for batch082 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch082. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:68551
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
    Reused for batch082 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch082. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:68551
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
    Reused for batch082 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch082. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:68551
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
    Reused for batch082 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch082. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:68551
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/linaclotide.yaml
    --out /private/tmp/npm-review-work/820/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-28T11:15:39.852247Z. Original
    receipt: /private/tmp/npm-review-work/820/strict-receipt.json.'
  target_ids:
  - CHEBI:68551
- check_id: SCI820-LOCAL-JOINS
  name: Whole owner and exact retained source joins
  status: passed
  required: true
  summary: 'The whole current owner and exact source joins agree: one MIBiG compound
    row, one LOTUS occurrence row, one exact-key ChEBI structure row, one NPClassifier
    row and five PubChem rows. The official intake arrays contain four rows and the
    assay rows remain separately retained. The two human GC-C entries cite the same
    AID with different references, not two demonstrated independent experiments. Five
    seed-history entries do not validate natural origin.'
  evidence_ids:
  - SCI820-LOCAL
  target_ids:
  - CHEBI:68551
- check_id: SCI820-ENCODINGS
  name: Saved representation consistency
  status: passed
  required: true
  summary: Saved SMILES, Standard InChI and the retained exact-key ChEBI alternative
    agree internally on KXGCNMMJRFDFNR-WDRJZQOASA-N and C59H79N15O21S6; current intake
    agrees. Both owner encodings have 14 specified tetrahedral centres, consistent
    with the retained stereo_complete flag. The additional InChI-local C(-O)=N labels
    are representation diagnostics, not evidence of missing natural carbon configurations.
    This validates representation consistency, not biological origin.
  evidence_ids:
  - SCI820-ENCODINGS
  target_ids:
  - CHEBI:68551
- check_id: SCI820-IDENTITY
  name: Exact-parent authority identification
  status: passed
  required: true
  summary: The exact full key agrees with the retained ChEBI parent and the inspected
    IUPHAR/BPS ligand 5017 authority. This supports parent identification and distinguishes
    the acetate entry. It does not prove natural biosynthesis, occurrence or an independently
    measured complete natural configuration.
  evidence_ids:
  - SCI820-LOCAL
  - SCI820-ENCODINGS
  - CAND820-EXACT-PARENT-AUTHORITY
  target_ids:
  - CHEBI:68551
- check_id: SCI820-ORIGIN
  name: Exact-parent biological-origin support
  status: failed
  required: true
  summary: The exact-parent authority calls linaclotide a synthetic analogue, while
    the owner asserts NATURAL_PRODUCT with E. coli production and occurrence. This
    is a confirmed material source-applicability conflict. Its cause and natural absence
    remain unproved; neither automatic SYNTHETIC replacement nor a wrong-structure
    conclusion is justified.
  evidence_ids:
  - CAND820-EXACT-PARENT-AUTHORITY
  - CAND820-RETAINED-ORIGIN-CONTEXT
  - CAND820-OWN-1989-METADATA
  target_ids:
  - CHEBI:68551
- check_id: SCI820-PRODUCER
  name: Exact-parent producer applicability
  status: unavailable
  required: true
  summary: The retained MIBiG E. coli assertion resolves to the same 1989 work as
    the LOTUS DOI. Own metadata and front matter establish that publication identity,
    but do not establish natural production of this exact linaclotide parent. They
    are not two independent confirmations. No taxon replacement or universal nonproduction
    conclusion is selected.
  evidence_ids:
  - CAND820-RETAINED-ORIGIN-CONTEXT
  - CAND820-OWN-1989-METADATA
  - CAND820-OWN-PRIMARY-LIMIT
  target_ids:
  - CHEBI:68551
- check_id: SCI820-LOCUS
  name: Exact-parent locus applicability
  status: unavailable
  required: true
  summary: BGC0000621 version 3, M18346.1 and the RIBOSOMAL label are retained source
    assertions graded CLUSTER_UNSTATED, with no stored interval. Their applicability
    to this exact analogue remains unresolved. The own PMC response contains no substantive
    body, and no sequence, engineering procedure or inferred locus mechanism is extracted.
  evidence_ids:
  - CAND820-RETAINED-ORIGIN-CONTEXT
  - CAND820-OWN-PRIMARY-LIMIT
  target_ids:
  - CHEBI:68551
- check_id: SCI820-OCCURRENCE
  name: Exact-parent occurrence applicability
  status: unavailable
  required: true
  summary: The exact-key LOTUS E. coli triple is faithfully retained but its 1989
    citation does not establish exact-parent occurrence in the inspected material.
    Occurrence and production need separate adjudication; the authority/record conflict
    does not by itself prove the LOTUS citation false or authorize exclusion.
  evidence_ids:
  - CAND820-RETAINED-ORIGIN-CONTEXT
  - CAND820-OWN-1989-METADATA
  - CAND820-EXACT-PARENT-AUTHORITY
  target_ids:
  - CHEBI:68551
- check_id: SCI820-CLASSIFICATION
  name: Chemical class and definition scope
  status: passed
  required: true
  summary: The cyclic-peptide classification and retained ChEBI parent description
    are consistent with the internally matching encodings and exact-parent authority.
    Computational classification and the historical therapeutic definition do not
    establish natural origin or current clinical guidance. The RIBOSOMAL source assertion
    is assessed separately as an unresolved exact-parent locus relation.
  evidence_ids:
  - SCI820-LOCAL
  - SCI820-ENCODINGS
  - CAND820-EXACT-PARENT-AUTHORITY
  target_ids:
  - CHEBI:68551
- check_id: SCI820-ACTIVITY-CALLS
  name: Original assay calls and endpoints
  status: passed
  required: true
  summary: The five PubChem rows preserve the human and rat GC-C active annotations
    and two separate screening results. The CHIKV row remains INACTIVE with source
    Potency 3.0458 uM; the SARS-S pseudoparticle row remains inconclusive/NOT_DETERMINED
    with Potency 19.9526 uM. Neither number establishes positive inhibition or a verified
    molecular target mechanism. The two human GC-C rows share AID 1345486; publication
    count is not experiment count.
  evidence_ids:
  - SCI820-LOCAL
  - SCI820-ASSAY-ROWS
  target_ids:
  - CHEBI:68551
- check_id: SCI820-PHARMACOLOGY
  name: Named-drug GC-C pharmacology
  status: passed
  required: true
  summary: The own PubMed abstract reports human T84 GC-C receptor-binding Ki values
    of 1.23–1.64 nM and a distinct intracellular cGMP functional EC50 of 99 nM. Rat
    secretion/transit context is not a rat-receptor affinity measurement. These endpoints
    support pharmacological applicability to the named drug, not natural origin, and
    are not inserted into blank raw assay-value fields.
  evidence_ids:
  - SCI820-PM20863829
  - SCI820-PM17694454
  target_ids:
  - CHEBI:68551
- check_id: SCI820-ACTIVITY-VALIDATION
  name: Assay-specific quantitative and target grounding
  status: unavailable
  required: true
  summary: The original individual assay pages and species-specific target accession
    mappings were not independently verified. Human-cell binding Ki and functional
    EC50 remain distinct; no human potency is assigned to the rat row. The retained
    viral UniProt labels are source annotations and the inactive/inconclusive calls
    do not establish a positive antiviral mechanism.
  evidence_ids:
  - SCI820-ASSAY-ROWS
  - SCI820-PM20863829
  target_ids:
  - CHEBI:68551
- check_id: SCI820-MECHANISM
  name: Optional graph and pathway detail
  status: unavailable
  required: false
  summary: No detailed pathway or causal graph is present. Named-drug GC-C pharmacology
    is supported at abstract level, while exact-parent biosynthetic mechanism is unresolved.
    Empty optional fields are not themselves defects and related enterotoxin mechanisms
    are not transferred to this parent.
  evidence_ids:
  - SCI820-LOCAL
  - SCI820-PM20863829
  - CAND820-OWN-PRIMARY-LIMIT
  target_ids:
  - CHEBI:68551
- check_id: SCI820-PROVENANCE
  name: Source tiers, history and grounding
  status: passed
  required: true
  summary: Current owner, source concepts, retained row placements, original timestamps
    and seed history are preserved. Exact database/key joins and mechanical intake
    success establish reproducible provenance, not full scientific correctness. Bibliography
    entries are not own publication aliases; retained source citation levels and inspected
    primary/authority tiers remain explicit.
  evidence_ids:
  - SCI820-LOCAL
  target_ids:
  - CHEBI:68551
- check_id: SCI820-SOURCE-LIMITS
  name: Remaining source and authority limits
  status: unavailable
  required: true
  summary: Independent complete configuration, all current authority mappings and
    uninspected source material remain outside verified scope. Required unavailable
    checks remain explicit; no optional absence, source access failure or baseline
    pass is converted into a scientific finding.
  evidence_ids:
  - SCI820-LOCAL
  - SCI820-ENCODINGS
  target_ids:
  - CHEBI:68551
evidence:
- evidence_id: SCI820-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch082-tentative/tentative-owner-source-inventory-001.json
  accessed_at: '2026-10-28T10:07:36.390765Z'
  locator: /entries/9/owner_document; /entries/9/rows; /entries/9/supplemental_retained_rows;
    /entries/9/expected_official_intake_rows
  snapshot_sha256: 477c551faa157bcada534b89a49041cd2ebe4582b8e06b867faa7da3ceb90f9e
  support: context_only
  summary: 'The whole current owner and exact source joins agree: one MIBiG compound
    row, one LOTUS occurrence row, one exact-key ChEBI structure row, one NPClassifier
    row and five PubChem rows. The official intake arrays contain four rows and the
    assay rows remain separately retained. The two human GC-C entries cite the same
    AID with different references, not two demonstrated independent experiments. Five
    seed-history entries do not validate natural origin.'
- evidence_id: SCI820-ENCODINGS
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch082-tentative/source-science-preparation/root-tentative82-local-chemical-consistency-and-neighbors-001.json
  accessed_at: '2026-10-28T11:16:04.877538Z'
  locator: /records/9/smiles; /records/9/inchi; /records/9/comparisons; /records/9/chebi_alternatives
  snapshot_sha256: 3c5d366cde6ad2f87ce2c630576aaaa92a80e9ccaeec1486b3bcea71d66ea2b1
  support: supports
  summary: Saved SMILES, Standard InChI and the retained exact-key ChEBI alternative
    agree internally on KXGCNMMJRFDFNR-WDRJZQOASA-N and C59H79N15O21S6; current intake
    agrees. Both owner encodings have 14 specified tetrahedral centres, consistent
    with the retained stereo_complete flag. The additional InChI-local C(-O)=N labels
    are representation diagnostics, not evidence of missing natural carbon configurations.
    This validates representation consistency, not biological origin.
- evidence_id: CAND820-EXACT-PARENT-AUTHORITY
  kind: authority
  reference: https://www.guidetopharmacology.org/GRAC/LigandDisplayForward?ligandId=5017&tab=structure
  accessed_at: '2026-10-28T10:54:00Z'
  locator: Saved IUPHAR/BPS ligand5017 structure extraction L68-L70 and L83; tool-call
    bounds, not raw HTTP clocks
  snapshot_sha256: 7cbb4d126c1152daff45d0e10355d588257d64e96c8ebaaa2eda97469191e447
  support: partial
  summary: The authority assigns the retained full InChIKey to linaclotide and calls
    that ligand a synthetic analogue of bacterial heat-stable enterotoxins. It distinguishes
    the parent ligand from its acetate form. This is an exact-identifier database
    assertion, not new chemical computation or proof of universal natural absence.
- evidence_id: CAND820-RETAINED-ORIGIN-CONTEXT
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch082-tentative/tentative-owner-source-inventory-001.json
  accessed_at: '2026-10-28T10:07:36.390765Z'
  locator: /entries/9/owner_document; /entries/9/rows/mibig_compounds/0; /entries/9/rows/lotus_occurrences/0;
    /entries/9/rows/chebi_structures/0
  snapshot_sha256: 477c551faa157bcada534b89a49041cd2ebe4582b8e06b867faa7da3ceb90f9e
  support: supports
  summary: The exact retained parent has NATURAL_PRODUCT origin, an E. coli producer
    assertion from BGC0000621:1 version3 and an E. coli LOTUS occurrence. The producer
    grade is SOURCE_ASSERTION and the locus CLUSTER_UNSTATED. MIBiG cites PMID2643580
    and LOTUS cites its own verified1989 DOI; these are one publication, not independent
    corroboration.
- evidence_id: CAND820-OWN-1989-METADATA
  kind: database
  reference: PMID:2643580
  accessed_at: '2026-10-28T10:43:35.687058Z'
  locator: Own MedlineCitation/Article title and abstract; own PubmedData/ArticleIdList
  snapshot_sha256: c93a19e138631a4b798c43efab86779c8359551845767073f5ff97de5bcf5629
  support: partial
  summary: Own metadata verifies PMID2643580, the retained1989 DOI and PMC313148.
    It concerns E. coli enterotoxin alleles; it does not identify linaclotide as the
    exact naturally produced parent. No sequence, residue changes or experimental
    procedure are extracted.
- evidence_id: CAND820-OWN-PRIMARY-LIMIT
  kind: database
  reference: PMCID:PMC313148
  accessed_at: '2026-10-28T11:04:24.041324Z'
  locator: Own JATS front/article-meta identifiers/title/abstract; body absent
  snapshot_sha256: 05f6e22951a33495fff76a3431af69af86b521f1aebd94eff2dd9490f4529ba8
  support: context_only
  summary: The HTTP200 response matches the own publication IDs but contains front
    matter and abstract only. The original bodyless guard failure is held. This limits
    source adjudication and is not a scientific refutation, nor authority for a sequence-based
    source-misassignment conclusion.
- evidence_id: CAND820-ADMISSION-RUBRIC
  kind: record_content
  reference: CLAUDE.md; docs/record-reviews.md
  accessed_at: '2026-10-28T11:14:11.097820Z'
  locator: 'Semantic invariants: origin assertion; Verdict And Severity: major'
  snapshot_sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
  support: context_only
  summary: Admission requires an origin assertion applicable to the record, while
    materially unsupported claims or scope inflation are major. The present concern
    is exact-parent origin support; wrong natural identity or universal absence is
    not established.
- evidence_id: CAND820-GENERATED-ORIGIN-INTERFACE
  kind: record_content
  reference: scripts/seed_from_sources.py
  accessed_at: '2026-10-28T11:14:11.097956Z'
  locator: 'Current read lines988-1002: initial MIBiG-derived document and NATURAL_PRODUCT
    field'
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
  support: context_only
  summary: The inspected document-construction callsite emits NATURAL_PRODUCT from
    the retained source group. It identifies the generator boundary for a future reviewed
    fix, without proving the upstream cause or a general defect across unrelated records.
- evidence_id: CAND820-MAINTAINED-CORRECTION-BOUNDARY
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-28T11:14:11.097889Z'
  locator: Decision file; MIBiG claim-specific reference corrections; LOTUS occurrence
    exclusions
  snapshot_sha256: c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa
  support: context_only
  summary: Existing citation-routing and LOTUS exclusion interfaces are narrow and
    require independently supported, exact-row decisions. Neither supplies an automatic
    origin replacement; reserved decisions.tsv is not consumed. Preserve original
    inventories and use a reviewed implemented harmonization path.
- evidence_id: SCI820-PM17694454
  kind: database
  reference: PMID:17694454
  accessed_at: '2026-10-28T10:43:02.938057Z'
  locator: ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract
  snapshot_sha256: e1a833efe65d80f0858618b5ff6cb6fdde1fafdf447e6d0a457da340eff4f3ca
  support: partial
  summary: The own historical title/abstract names linaclotide as a therapeutic GC-C
    agonist. It does not establish the exact parent’s natural producer, locus, complete
    experimental structure or current treatment guidance.
- evidence_id: SCI820-PM20863829
  kind: database
  reference: PMID:20863829
  accessed_at: '2026-10-28T10:43:34.584843Z'
  locator: ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText
  snapshot_sha256: 917c4b583449c02811034ef89ffb587e6cd2bb2e40fa6e0d279f303cce1877e4
  support: partial
  summary: The own PubMed abstract reports human T84 GC-C receptor-binding Ki values
    of 1.23–1.64 nM and a distinct intracellular cGMP functional EC50 of 99 nM. Rat
    secretion/transit context is not a rat-receptor affinity measurement. These endpoints
    support pharmacological applicability to the named drug, not natural origin, and
    are not inserted into blank raw assay-value fields.
- evidence_id: SCI820-ASSAY-ROWS
  kind: database
  reference: data/raw/pubchem_bioassay.tsv
  accessed_at: '2026-10-28T10:07:36.390765Z'
  locator: exact retained CID16158208 rows 3521..3525; inventory /entries/9/rows/pubchem_bioassay
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
  support: partial
  summary: The five PubChem rows preserve the human and rat GC-C active annotations
    and two separate screening results. The CHIKV row remains INACTIVE with source
    Potency 3.0458 uM; the SARS-S pseudoparticle row remains inconclusive/NOT_DETERMINED
    with Potency 19.9526 uM. Neither number establishes positive inhibition or a verified
    molecular target mechanism. The two human GC-C rows share AID 1345486; publication
    count is not experiment count.
assessments:
- assessment_id: SCI820-LOCAL-JOINS
  area: provenance
  topic: Whole owner and exact retained source joins
  outcome: supported
  summary: 'The whole current owner and exact source joins agree: one MIBiG compound
    row, one LOTUS occurrence row, one exact-key ChEBI structure row, one NPClassifier
    row and five PubChem rows. The official intake arrays contain four rows and the
    assay rows remain separately retained. The two human GC-C entries cite the same
    AID with different references, not two demonstrated independent experiments. Five
    seed-history entries do not validate natural origin.'
  evidence_ids:
  - SCI820-LOCAL
  target_ids:
  - CHEBI:68551
- assessment_id: SCI820-ENCODINGS
  area: representation
  topic: Saved representation consistency
  outcome: supported
  summary: Saved SMILES, Standard InChI and the retained exact-key ChEBI alternative
    agree internally on KXGCNMMJRFDFNR-WDRJZQOASA-N and C59H79N15O21S6; current intake
    agrees. Both owner encodings have 14 specified tetrahedral centres, consistent
    with the retained stereo_complete flag. The additional InChI-local C(-O)=N labels
    are representation diagnostics, not evidence of missing natural carbon configurations.
    This validates representation consistency, not biological origin.
  evidence_ids:
  - SCI820-ENCODINGS
  target_ids:
  - CHEBI:68551
  dimensions:
  - name: stereochemical_resolution
    value: stereo_complete=true; 14 specified tetrahedral centres in each saved owner
      encoding, exact parent authority key match. Internal configuration consistency
      is distinct from proof of natural biosynthesis.
    definition: Retained and computed stereochemical resolution is distinct from independent
      natural-material configuration proof.
    evidence_ids:
    - SCI820-ENCODINGS
    - CAND820-EXACT-PARENT-AUTHORITY
- assessment_id: SCI820-IDENTITY
  area: representation
  topic: Exact-parent authority identification
  outcome: supported
  summary: The exact full key agrees with the retained ChEBI parent and the inspected
    IUPHAR/BPS ligand 5017 authority. This supports parent identification and distinguishes
    the acetate entry. It does not prove natural biosynthesis, occurrence or an independently
    measured complete natural configuration.
  evidence_ids:
  - SCI820-LOCAL
  - SCI820-ENCODINGS
  - CAND820-EXACT-PARENT-AUTHORITY
  target_ids:
  - CHEBI:68551
- assessment_id: SCI820-ORIGIN
  area: evidence
  topic: Exact-parent biological-origin support
  outcome: concern
  summary: The exact-parent authority calls linaclotide a synthetic analogue, while
    the owner asserts NATURAL_PRODUCT with E. coli production and occurrence. This
    is a confirmed material source-applicability conflict. Its cause and natural absence
    remain unproved; neither automatic SYNTHETIC replacement nor a wrong-structure
    conclusion is justified.
  evidence_ids:
  - CAND820-EXACT-PARENT-AUTHORITY
  - CAND820-RETAINED-ORIGIN-CONTEXT
  - CAND820-OWN-1989-METADATA
  target_ids:
  - CHEBI:68551
- assessment_id: SCI820-PRODUCER
  area: evidence
  topic: Exact-parent producer applicability
  outcome: concern
  summary: The retained MIBiG E. coli assertion resolves to the same 1989 work as
    the LOTUS DOI. Own metadata and front matter establish that publication identity,
    but do not establish natural production of this exact linaclotide parent. They
    are not two independent confirmations. No taxon replacement or universal nonproduction
    conclusion is selected.
  evidence_ids:
  - CAND820-RETAINED-ORIGIN-CONTEXT
  - CAND820-OWN-1989-METADATA
  - CAND820-OWN-PRIMARY-LIMIT
  target_ids:
  - CHEBI:68551
  dimensions:
  - name: taxon_strain
    value: 'Retained producer and occurrence: Escherichia coli, NCBITaxon:562, no
      strain field. Exact-parent biological applicability is unresolved; no taxon
      or strain replacement is selected.'
    definition: Exact retained taxon/strain context is distinguished from the inspected
      source material and verification status.
    evidence_ids:
    - SCI820-LOCAL
    - CAND820-OWN-1989-METADATA
    - CAND820-EXACT-PARENT-AUTHORITY
- assessment_id: SCI820-LOCUS
  area: evidence
  topic: Exact-parent locus applicability
  outcome: unknown
  summary: BGC0000621 version 3, M18346.1 and the RIBOSOMAL label are retained source
    assertions graded CLUSTER_UNSTATED, with no stored interval. Their applicability
    to this exact analogue remains unresolved. The own PMC response contains no substantive
    body, and no sequence, engineering procedure or inferred locus mechanism is extracted.
  evidence_ids:
  - CAND820-RETAINED-ORIGIN-CONTEXT
  - CAND820-OWN-PRIMARY-LIMIT
  target_ids:
  - CHEBI:68551
- assessment_id: SCI820-OCCURRENCE
  area: evidence
  topic: Exact-parent occurrence applicability
  outcome: concern
  summary: The exact-key LOTUS E. coli triple is faithfully retained but its 1989
    citation does not establish exact-parent occurrence in the inspected material.
    Occurrence and production need separate adjudication; the authority/record conflict
    does not by itself prove the LOTUS citation false or authorize exclusion.
  evidence_ids:
  - CAND820-RETAINED-ORIGIN-CONTEXT
  - CAND820-OWN-1989-METADATA
  - CAND820-EXACT-PARENT-AUTHORITY
  target_ids:
  - CHEBI:68551
- assessment_id: SCI820-CLASSIFICATION
  area: representation
  topic: Chemical class and definition scope
  outcome: supported
  summary: The cyclic-peptide classification and retained ChEBI parent description
    are consistent with the internally matching encodings and exact-parent authority.
    Computational classification and the historical therapeutic definition do not
    establish natural origin or current clinical guidance. The RIBOSOMAL source assertion
    is assessed separately as an unresolved exact-parent locus relation.
  evidence_ids:
  - SCI820-LOCAL
  - SCI820-ENCODINGS
  - CAND820-EXACT-PARENT-AUTHORITY
  target_ids:
  - CHEBI:68551
- assessment_id: SCI820-ACTIVITY-CALLS
  area: evidence
  topic: Original assay calls and endpoints
  outcome: supported
  summary: The five PubChem rows preserve the human and rat GC-C active annotations
    and two separate screening results. The CHIKV row remains INACTIVE with source
    Potency 3.0458 uM; the SARS-S pseudoparticle row remains inconclusive/NOT_DETERMINED
    with Potency 19.9526 uM. Neither number establishes positive inhibition or a verified
    molecular target mechanism. The two human GC-C rows share AID 1345486; publication
    count is not experiment count.
  evidence_ids:
  - SCI820-LOCAL
  - SCI820-ASSAY-ROWS
  target_ids:
  - CHEBI:68551
- assessment_id: SCI820-PHARMACOLOGY
  area: evidence
  topic: Named-drug GC-C pharmacology
  outcome: supported
  summary: The own PubMed abstract reports human T84 GC-C receptor-binding Ki values
    of 1.23–1.64 nM and a distinct intracellular cGMP functional EC50 of 99 nM. Rat
    secretion/transit context is not a rat-receptor affinity measurement. These endpoints
    support pharmacological applicability to the named drug, not natural origin, and
    are not inserted into blank raw assay-value fields.
  evidence_ids:
  - SCI820-PM20863829
  - SCI820-PM17694454
  target_ids:
  - CHEBI:68551
- assessment_id: SCI820-ACTIVITY-VALIDATION
  area: evidence
  topic: Assay-specific quantitative and target grounding
  outcome: unknown
  summary: The original individual assay pages and species-specific target accession
    mappings were not independently verified. Human-cell binding Ki and functional
    EC50 remain distinct; no human potency is assigned to the rat row. The retained
    viral UniProt labels are source annotations and the inactive/inconclusive calls
    do not establish a positive antiviral mechanism.
  evidence_ids:
  - SCI820-ASSAY-ROWS
  - SCI820-PM20863829
  target_ids:
  - CHEBI:68551
- assessment_id: SCI820-MECHANISM
  area: completeness
  topic: Optional graph and pathway detail
  outcome: unknown
  summary: No detailed pathway or causal graph is present. Named-drug GC-C pharmacology
    is supported at abstract level, while exact-parent biosynthetic mechanism is unresolved.
    Empty optional fields are not themselves defects and related enterotoxin mechanisms
    are not transferred to this parent.
  evidence_ids:
  - SCI820-LOCAL
  - SCI820-PM20863829
  - CAND820-OWN-PRIMARY-LIMIT
  target_ids:
  - CHEBI:68551
- assessment_id: SCI820-PROVENANCE
  area: provenance
  topic: Source tiers, history and grounding
  outcome: supported
  summary: Current owner, source concepts, retained row placements, original timestamps
    and seed history are preserved. Exact database/key joins and mechanical intake
    success establish reproducible provenance, not full scientific correctness. Bibliography
    entries are not own publication aliases; retained source citation levels and inspected
    primary/authority tiers remain explicit.
  evidence_ids:
  - SCI820-LOCAL
  target_ids:
  - CHEBI:68551
  dimensions:
  - name: source_version
    value: MIBiG BGC0000621 version 3; retained ChEBI source_version='3-star' is a
      quality marker, not a release version; NPClassifier npclassifier.gnps2.org@2026-09-07;
      LOTUS/PubChem release version not stated. Source labels do not validate origin.
    definition: Literal source version/release labels are retained; unstated versions
      are not guessed.
    evidence_ids:
    - SCI820-LOCAL
  - name: evidence_tier
    value: Retained database assertions; own PubMed title/abstract metadata; own PMC
      front matter/abstract only; saved exact-key IUPHAR authority web extraction.
      No substantive 1989 primary body or experimental structure reanalysis.
    definition: Own metadata, database assertions, inspected primary passages and
      exact authority are credited at their actual tiers.
    evidence_ids:
    - SCI820-LOCAL
    - SCI820-PM20863829
    - CAND820-OWN-PRIMARY-LIMIT
    - CAND820-EXACT-PARENT-AUTHORITY
- assessment_id: SCI820-SOURCE-LIMITS
  area: completeness
  topic: Remaining source and authority limits
  outcome: unknown
  summary: Independent complete configuration, all current authority mappings and
    uninspected source material remain outside verified scope. Required unavailable
    checks remain explicit; no optional absence, source access failure or baseline
    pass is converted into a scientific finding.
  evidence_ids:
  - SCI820-LOCAL
  - SCI820-ENCODINGS
  target_ids:
  - CHEBI:68551
findings:
- finding_id: F820-EXACT-PARENT-ORIGIN-SUPPORT-CONFLICT
  issue_key: linaclotide-chebi68551-exact-parent-natural-origin-support-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Exact-parent linaclotide origin assertions require reconciliation
  description: The retained linaclotide parent, keyed KXGCNMMJRFDFNR-WDRJZQOASA-N,
    is labelled NATURAL_PRODUCT and linked to E. coli production and occurrence. The
    IUPHAR/BPS entry bearing that exact full key classifies linaclotide as a synthetic
    analogue of bacterial enterotoxins. The retained MIBiG and LOTUS citations resolve
    to one1989 enterotoxin publication; the inspected own metadata/front matter does
    not establish natural production or occurrence of this exact parent. This confirms
    a material conflict in source applicability that prevents treating the retained
    biological-origin claims as scientifically resolved. Conflation of a related natural
    parent family with this analogue is a provisional explanation, not a demonstrated
    upstream cause. Synthetic manufacture alone does not prove universal natural absence;
    the inaccessible full primary prevents a definitive source-misassignment judgment.
    No replacement structure, origin value, taxon, salt equivalence or exclusion is
    selected.
  target_ids:
  - CHEBI:68551
  field_paths:
  - biosynthesis_origin
  - producer_organisms[0]
  - biosynthetic_gene_clusters[0]
  - occurrences[0]
  - source_concepts
  evidence_ids:
  - CAND820-EXACT-PARENT-AUTHORITY
  - CAND820-RETAINED-ORIGIN-CONTEXT
  - CAND820-OWN-1989-METADATA
  - CAND820-OWN-PRIMARY-LIMIT
  - CAND820-ADMISSION-RUBRIC
  - CAND820-GENERATED-ORIGIN-INTERFACE
  - CAND820-MAINTAINED-CORRECTION-BOUNDARY
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Preserve complete original BGC0000621:1 version3 structure, organism, locus
      and citation context.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Preserve exact-key E. coli/1989 DOI triple; assess occurrence separately
      from production.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Preserve exact parent identity and distinguish salt or related enterotoxin
      material.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Conditional occurrence-only correction after a specific unsupported triple
      is independently established; not selected here.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Conditional citation-only rerouting if supported; it does not repair identity,
      natural origin or producer grade.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintain the source-to-record origin/producer admission and reproducible
      emission path after separate scientific adjudication.
  - repository: CultureBotAI/NaturalProductMech
    path: docs/CURATION.md
    role: Document and test any necessary maintained-input extension before applying
      it.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/linaclotide.yaml
    role: Generated output only; no YAML-only correction.
  rule_id: biological-origin-evidence-must-apply-to-exact-parent
  native_severity: major for a material unresolved exact-parent biological-origin
    support conflict
  normalization_reason: The observed authority/record discrepancy and shared-publication
    provenance are confirmed. Their biological explanation and any wrong-natural-identity
    or universal-absence claim remain unproven. Major follows materially unsupported
    or overextended source applicability, without promoting this limited evidence
    to an identity blocker.
actions:
- action_id: A820-RECONCILE-EXACT-PARENT-ORIGIN
  finding_ids:
  - F820-EXACT-PARENT-ORIGIN-SUPPORT-CONFLICT
  target_ids:
  - CHEBI:68551
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Preserve complete original BGC0000621:1 version3 structure, organism, locus
      and citation context.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Preserve exact-key E. coli/1989 DOI triple; assess occurrence separately
      from production.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Preserve exact parent identity and distinguish salt or related enterotoxin
      material.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Conditional occurrence-only correction after a specific unsupported triple
      is independently established; not selected here.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Conditional citation-only rerouting if supported; it does not repair identity,
      natural origin or producer grade.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintain the source-to-record origin/producer admission and reproducible
      emission path after separate scientific adjudication.
  - repository: CultureBotAI/NaturalProductMech
    path: docs/CURATION.md
    role: Document and test any necessary maintained-input extension before applying
      it.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/linaclotide.yaml
    role: Generated output only; no YAML-only correction.
  description: Reconcile the exact parent identity and natural-origin evidence before
    changing its source-to-record admission, producer, occurrence or locus assertions.
    Preserve original source rows and held attempts; implement only separately adjudicated,
    reproducible corrections.
  acceptance_checks:
  - Reproduce the exact full-key join to IUPHAR ligand5017 and the complete retained
    MIBiG BGC0000621:1 version3 and LOTUS E. coli/1989 DOI rows. Keep the parent and
    acetate identifiers separate.
  - Determine whether an inspected primary or authoritative exact-material source
    supports natural occurrence or biosynthesis of this parent rather than a related
    family, synthetic analogue, manufactured preparation or salt. Preserve inaccessible-source
    limitations; do not equate manufacture with proof of natural absence.
  - Keep PMID2643580 and DOI10.1128/iai.57.2.645-648.1989 as one publication. Do not
    infer exact source misassignment from metadata or bodyless access alone, and do
    not retrieve procedures or engineering details for this review.
  - Reassess biological origin, producer, occurrence and locus applicability separately.
    A pharmacological GC-C observation may remain relevant to the exact drug even
    if a natural-origin assertion is withdrawn; distinguish binding and functional
    endpoints and retain inactive/inconclusive assay calls.
  - If a particular LOTUS triple is demonstrated unsupported, use only the documented
    full-row-pinned occurrence exclusion after separate authorization. Citation rerouting,
    locus-evidence grading or a structure correction must not be used as an implicit
    origin replacement.
  - If the verified origin correction needs a new maintained-input or admission rule,
    review and test that implementation before migration. Do not use reserved decisions.tsv,
    edit generated YAML directly, choose SYNTHETIC automatically or silently rewrite
    raw inventories.
  - After separately authorized curation, run the appropriate seed canary, guarded
    reproduction and documented validation gates; preserve applicable claims, graphs
    and history. No lifecycle invocation is performed by this proposal.
  generator: scripts/seed_from_sources.py only after separately reviewed maintained-input/admission
    adjudication
limitations:
- The exact IUPHAR parent key and synthetic-analogue classification are verified in
  a saved web extraction. Tool-call bounds are not raw HTTP clocks; the FDA oversized-fetch
  failure supplies no scientific evidence.
- The 1989 own PubMed/PMC identifiers match, but the PMC response is front matter
  and abstract only. Missing body is an access limitation, not scientific refutation
  or proof of a wrong citation.
- Confirmed refers to the exact-parent authority/current-record support conflict.
  Universal natural absence, upstream conflation, wrong structure, salt equivalence,
  taxon replacement and automatic SYNTHETIC classification remain unproved.
- Own pharmacological abstracts are metadata-level evidence. Species, assay-material
  identity, binding and functional endpoints remain distinct; inactive and inconclusive
  screening calls are preserved.
- No primary sequence, residue-level engineering detail, manufacturing procedure or
  experimental protocol is extracted. No source or generated record is changed.
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
- Original owner/source reading, two-encoding computation, neighbor inspection, HTTP
  retrieval and later metadata reading retain separate clocks. Official intake separately
  computed SMILES facts.
- No scientific record, maintained input or native curation status was changed. Any
  findings and actions record ROOT-adopted proposed work; exact-source limitations
  and unavailable checks remain explicit.
```
