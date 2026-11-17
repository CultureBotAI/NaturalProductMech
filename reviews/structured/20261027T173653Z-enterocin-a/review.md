# Scientific review of enterocin A

- Review: 20261027T173653Z-enterocin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-27T17:36:05.312141Z
- Finished UTC: 2026-10-27T17:36:53.140586Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The retained enterocin A encodings are internally consistent but conflict with the cited mature-peptide description: C49H70N14O16 contains no sulfur, whereas the own abstract reports 47 residues including four cysteines. A bounded identity-curation finding records this conflict; exact replacement structure and strain/locus linkage remain unresolved. The attempted PMC response contains no full body.

## Scope And Provenance

Bounded review of enterocin A: retained owner and exact MIBiG structure row, saved encoding/neighbor diagnostics, the cited mature-peptide abstract and the PMC front-matter/access limitation. The sulfur-free representation versus four-cysteine mature-material conflict is assessed without selecting a replacement structure or establishing strain/accession linkage.

Selection: One exact owner record: data/natural_products/amino_acids_and_peptides/enterocin-a.yaml (naturalproductmech:mibig-c53d1bae68); retained source assertions, saved diagnostics and inspected own-source material are assessed separately.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-c53d1bae68 | data/natural_products/amino_acids_and_peptides/enterocin-a.yaml | generated | enterocin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-c53d1bae68 | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-c53d1bae68 | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-c53d1bae68 | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-c53d1bae68 | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-c53d1bae68 | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | naturalproductmech:mibig-c53d1bae68 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Saved two-encoding internal consistency | passed | True | naturalproductmech:mibig-c53d1bae68 | Saved RDKit 2026.03.5 diagnostics regenerate UDJYWZUEIHCKKJ-UHFFFAOYSA-N from both retained encodings, with formula C49H70N14O16, one fragment and formal charge zero. Standard InChI also agrees. This supports internal representation consistency, not experimental natural identity or current authority validity. |
| Exact retained owner and source joins | passed | True | naturalproductmech:mibig-c53d1bae68 | The whole owner and all seven retained arrays, six separate intake projections and two supplemental arrays match their original snapshot guards. |
| Own abstract and PMC identity | passed | True | naturalproductmech:mibig-c53d1bae68 | The PubMed article and PMC front matter match PMID 8633865, PMC167941 and DOI 10.1128/aem.62.5.1676-1682.1996. They are the same study. |
| Stored representation versus cited mature material | failed | True | naturalproductmech:mibig-c53d1bae68 | The retained owner and exact MIBiG BGC0000618:1 version 3 row encode C49H70N14O16 with no sulfur. Both saved encodings reproduce that formula and full key. The cited paper’s own abstract instead defines enterocin A as a 47-residue mature peptide containing four cysteines, with reported mass 4,829. The sulfur-free graph cannot represent that cysteine-containing mature material as described. This is a concrete representation-versus-cited-material conflict; its source of error, exact replacement sequence/graph, disulfide topology, stock and accession mapping remain unresolved. |
| Substantive article body and exact replacement | unavailable | True | naturalproductmech:mibig-c53d1bae68 | The attempted PMC source provides no body. Exact sequence tables, disulfide mapping and stock/accession relationship remain uninspected; no replacement structure is inferred from the abstract. |
| Current taxon, sequence and chemical authorities | unavailable | True | naturalproductmech:mibig-c53d1bae68 | No current external taxon, sequence, protein or chemical authority was inspected. Internal key agreement and retained accessions do not verify those authorities. |

## Scientific And Domain Assessments

### Internal chemical representation

representation: supported. Targets: naturalproductmech:mibig-c53d1bae68.

Saved RDKit 2026.03.5 diagnostics regenerate UDJYWZUEIHCKKJ-UHFFFAOYSA-N from both retained encodings, with formula C49H70N14O16, one fragment and formal charge zero. Standard InChI also agrees. This supports internal representation consistency, not experimental natural identity or current authority validity.

### Formula versus cited mature peptide

identity: concern. Targets: naturalproductmech:mibig-c53d1bae68.

The retained owner and exact MIBiG BGC0000618:1 version 3 row encode C49H70N14O16 with no sulfur. Both saved encodings reproduce that formula and full key. The cited paper’s own abstract instead defines enterocin A as a 47-residue mature peptide containing four cysteines, with reported mass 4,829. The sulfur-free graph cannot represent that cysteine-containing mature material as described. This is a concrete representation-versus-cited-material conflict; its source of error, exact replacement sequence/graph, disulfide topology, stock and accession mapping remain unresolved.

### What the paper positively reports

evidence: supported. Targets: naturalproductmech:mibig-c53d1bae68.

The own PMID 8633865 abstract describes enterocin A purified from an Enterococcus faecium strain, with primary structure established by amino-acid and DNA sequencing: 47 mature residues and four cysteines, calculated molecular weight 4,829 assuming intramolecular disulfides, confirmed by mass spectrometry. It also reports an 18-residue N-terminal leader removed during maturation. These are abstract-level statements; no full sequence or replacement chemical graph is reconstructed.

### Stored stereochemical incompleteness

representation: unknown. Targets: naturalproductmech:mibig-c53d1bae68.

Each encoding has 10 unassigned tetrahedral carbon sites. The 10 additional unspecified double-bond observations in parsed InChI are C(-O)=N environments, not additional unassigned C=C configurations. The declared stereo_complete=false is consistent with that local state. These sites are not assigned from a different mature peptide.

### Species versus exact producer strain

provenance: unknown. Targets: naturalproductmech:mibig-c53d1bae68.

The abstract supports isolation from an E. faecium strain; it does not identify the stored DO strain or align CP003583.1:2312434–2313194. The retained SOURCE_ASSERTION / CLUSTER_UNSTATED qualifiers and separate LOTUS species occurrence remain distinct. The structure conflict also prevents unqualified transfer of the paper’s production claim to the stored graph.

### Ribosomal origin and precursor

provenance: unknown. Targets: naturalproductmech:mibig-c53d1bae68.

The abstract supports a chromosomal structural gene and removal of an 18-residue leader, consistent with broad ribosomal peptide origin. It does not independently verify the current BGC0000618 locus coordinates or establish that this sulfur-free stored molecule is the mature product.

### Activity and putative immunity

completeness: unknown. Targets: naturalproductmech:mibig-c53d1bae68.

The title describes an antilisterial pediocin-family bacteriocin, but no quantitative activity or molecular target is assigned to the stored graph. A downstream 103-residue ORF is described as a putative immunity factor; the abstract does not establish that mechanism experimentally.

## Findings

### F689-CITED-MATURE-MATERIAL: Stored enterocin A structure conflicts with the cited mature peptide

major / open / provisional; issue key: enterocin-a-bgc0000618-sulfur-free-structure-conflicts-cited-mature-peptide.

The retained owner and exact MIBiG BGC0000618:1 version 3 row encode C49H70N14O16 with no sulfur. Both saved encodings reproduce that formula and full key. The cited paper’s own abstract instead defines enterocin A as a 47-residue mature peptide containing four cysteines, with reported mass 4,829. The sulfur-free graph cannot represent that cysteine-containing mature material as described. This is a concrete representation-versus-cited-material conflict; its source of error, exact replacement sequence/graph, disulfide topology, stock and accession mapping remain unresolved.

## Recommended Actions And Acceptance Checks

### A689-RECONCILE-MATURE-STRUCTURE

After separate maintainer authorization, reconcile BGC0000618:1 version 3 and the exact stored full key with the cited mature sequence, disulfide state, source stock and accession. Establish the intended exact compound before changing any structure or source concept. If a verified unambiguous 3-star ChEBI target meets the implemented guards, use the pinned maintained correction path and explicit owner migration; otherwise implement and test a narrowly scoped evidence-backed path. Preserve raw source facts and history, and re-audit all old-key occurrences, xrefs and classifications rather than carrying them onto a different graph. No replacement is selected here.

- Pin the whole original MIBiG row (source_id BGC0000618:1, version 3, row SHA256 8c8186b26ad24cd51407c94ef312f491bad106a3b572f4018accfe55d7b99ffd) and establish source drift checks.
- Inspect exact primary mature sequence and material-specific chemistry; reconcile four cysteines, maturation and mass without substituting the 18-residue leader or a fragment for the mature peptide.
- Document independent identity evidence for any chosen target and re-audit NPA015771, LOTUS old-key occurrence and producer/locus links; no implicit equivalence or cross-key claim transfer.
- Use validated migration with preserved history/PATHS.tsv where required, then run maintained structure-correction tests, documented strict validation, corpus checks and just verify-reproduction. These are future acceptance steps, not commands run by this DATA preparation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI689-LOCAL | /private/tmp/npm-review-work/shared-next-batch069-tentative/tentative-owner-source-inventory-001.json; /entries/8/owner_document; /entries/8/rows; /entries/8/row_guards; /entries/8/supplemental_retained_rows | context_only | The whole retained enterocin A owner and seven source arrays contain three rows: one MIBiG compound row, one LOTUS occurrence and one NPClassifier result. Both supplemental arrays are empty. The owner has no activity annotations or causal graph. Producer and locus grades, occurrence qualification and histories are preserved as retained assertions. |
| SCI689-CHEM | /private/tmp/npm-review-work/shared-next-batch069-tentative/source-science-preparation/native-tentative69-local-chemical-consistency-and-neighbors-001.json; /records/8/comparisons; /records/8/smiles; /records/8/inchi | supports | Saved RDKit 2026.03.5 diagnostics regenerate UDJYWZUEIHCKKJ-UHFFFAOYSA-N from both retained encodings, with formula C49H70N14O16, one fragment and formal charge zero. Standard InChI also agrees. This supports internal representation consistency, not experimental natural identity or current authority validity. Each encoding has 10 unassigned tetrahedral carbon sites. The 10 additional unspecified double-bond observations in parsed InChI are C(-O)=N environments, not additional unassigned C=C configurations. |
| SCI689-ROOT-CHEM-READ | /private/tmp/npm-review-work/shared-next-batch069-tentative/source-science-preparation/root-tentative69-saved-chemical-neighbor-interpretation-001.json; /observations; /limits | context_only | ROOT inspected the saved chemical comparisons and selected neighbors at the recorded time. This preserves the original computation interval and adds no external natural-identity or authority verification. |
| SCI689-OWN-ABSTRACT | /private/tmp/npm-review-work/shared-next-batch069-tentative/literature-preparation/public-metadata-001/pmid-8633865.xml; ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText; ./PubmedArticle/PubmedData/ArticleIdList/ArticleId | supports | The own PMID 8633865 abstract describes enterocin A purified from an Enterococcus faecium strain, with primary structure established by amino-acid and DNA sequencing: 47 mature residues and four cysteines, calculated molecular weight 4,829 assuming intramolecular disulfides, confirmed by mass spectrometry. It also reports an 18-residue N-terminal leader removed during maturation. These are abstract-level statements; no full sequence or replacement chemical graph is reconstructed. |
| SCI689-PMC-ABSTRACT | /private/tmp/npm-review-work/shared-next-batch069-tentative/literature-preparation/public-primary-001/pmc-167941.xml; ./article/front/article-meta/article-id; ./article/front/article-meta/abstract/p | supports | The matched PMC167941 response repeats the same study abstract, including 47 residues, four cysteines, reported mass 4,829 and an 18-residue leader. This is a second response for the same paper, not independent experimental corroboration. It supplies no full article body. |
| SCI689-FULLTEXT-LIMIT | /private/tmp/npm-review-work/shared-next-batch069-tentative/literature-preparation/public-primary-001/pmc-167941.xml.access.json; /http_status; /complete_body; /success; /error; /body; matched XML article comment and absence of ./article/body | context_only | The request returned complete HTTP 200 XML, but the publisher restriction leaves only front matter and abstract, with no substantive body. The collector recorded success=false and exited 1 at its body gate. This is a source-access limitation, not an official review-validation failure; sequence tables, figures and experimental methods remain unread. |
| SCI689-MAINTENANCE | /private/tmp/npm-record-reviews-20261021/docs/CURATION.md; MIBiG structure corrections; scripts/seed_from_sources.py::apply_structure_corrections and write_records; src/naturalproductmech/curate/structure_corrections.py | context_only | The maintained structure-correction interface pins an exact MIBiG compound row and an independently supported unambiguous 3-star ChEBI target. It does not supply a verified replacement here. Existing owner relocation requires a separately audited migration and re-audit of old-key claims; generated YAML must not be patched alone. A fresh source refresh or narrowly implemented alternative correction would require its own evidence and tests. |

## Limits And Additional Notes

- Only the cited study abstract is available from both PubMed and the attempted PMC source. The complete HTTP response is not full-text access; no sequence table, figure or full experimental method was inspected.
- The formula/text conflict is directly observed. Whether the source structure is a fragment, another compound or another mapping error remains unresolved; no alternative molecular graph, natural configuration or disulfide topology is selected.
- The exact DO strain and listed genomic interval are not established by the inspected abstract; do not infer absence of production by that strain.
- Original owner/raw reading, saved computation, HTTP access and subsequent source interpretation have distinct clocks; full_owner_scientific_read remains false.
- No source row, structure, producer grade, locus, activity annotation or corpus file is changed by this review.
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
review_id: 20261027T173653Z-enterocin-a
title: Scientific review of enterocin A
started_at: '2026-10-27T17:36:05.312141Z'
finished_at: '2026-10-27T17:36:53.140586Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The retained enterocin A encodings are internally consistent but conflict
  with the cited mature-peptide description: C49H70N14O16 contains no sulfur, whereas
  the own abstract reports 47 residues including four cysteines. A bounded identity-curation
  finding records this conflict; exact replacement structure and strain/locus linkage
  remain unresolved. The attempted PMC response contains no full body.'
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
  - path: data/natural_products/amino_acids_and_peptides/enterocin-a.yaml
    sha256: ba08d2b743c32502cf201363c01cac9ea7e1d3b237822de2dc2112eede426fa3
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
- target_id: naturalproductmech:mibig-c53d1bae68
  path: data/natural_products/amino_acids_and_peptides/enterocin-a.yaml
  label: enterocin A
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
  description: 'Bounded review of enterocin A: retained owner and exact MIBiG structure
    row, saved encoding/neighbor diagnostics, the cited mature-peptide abstract and
    the PMC front-matter/access limitation. The sulfur-free representation versus
    four-cysteine mature-material conflict is assessed without selecting a replacement
    structure or establishing strain/accession linkage.'
  selection: 'One exact owner record: data/natural_products/amino_acids_and_peptides/enterocin-a.yaml
    (naturalproductmech:mibig-c53d1bae68); retained source assertions, saved diagnostics
    and inspected own-source material are assessed separately.'
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-c53d1bae68
  exclusions:
  - target: Replacement molecular graph, mature sequence and stock/accession assignment
    reason: The retrieved PMC response lacks a substantive body. No full sequence
      table, disulfide topology or verified replacement is selected; the observed
      sulfur/text conflict does not by itself identify the source of the mapping error.
  - target: Current chemical, taxon, protein and sequence authorities and full-owner
      scientific verification
    reason: No current external authority query or complete primary/figure/SI verification
      is supplied by this review; internal encoding consistency does not establish
      natural identity.
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
    Reused for batch069 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch069. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
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
    Reused for batch069 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch069. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
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
    Reused for batch069 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch069. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
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
    Reused for batch069 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch069. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
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
    Reused for batch069 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch069. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/enterocin-a.yaml
    --out /private/tmp/npm-review-work/689/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-27T17:36:06.649319Z. Original
    receipt: /private/tmp/npm-review-work/689/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- check_id: SCI689-ENCODING
  name: Saved two-encoding internal consistency
  status: passed
  required: true
  summary: Saved RDKit 2026.03.5 diagnostics regenerate UDJYWZUEIHCKKJ-UHFFFAOYSA-N
    from both retained encodings, with formula C49H70N14O16, one fragment and formal
    charge zero. Standard InChI also agrees. This supports internal representation
    consistency, not experimental natural identity or current authority validity.
  evidence_ids:
  - SCI689-CHEM
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- check_id: SCI689-LOCAL-JOINS
  name: Exact retained owner and source joins
  status: passed
  required: true
  summary: The whole owner and all seven retained arrays, six separate intake projections
    and two supplemental arrays match their original snapshot guards.
  evidence_ids:
  - SCI689-LOCAL
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- check_id: SCI689-OWN-ID
  name: Own abstract and PMC identity
  status: passed
  required: true
  summary: The PubMed article and PMC front matter match PMID 8633865, PMC167941 and
    DOI 10.1128/aem.62.5.1676-1682.1996. They are the same study.
  evidence_ids:
  - SCI689-OWN-ABSTRACT
  - SCI689-PMC-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- check_id: SCI689-CITED-MATERIAL
  name: Stored representation versus cited mature material
  status: failed
  required: true
  summary: The retained owner and exact MIBiG BGC0000618:1 version 3 row encode C49H70N14O16
    with no sulfur. Both saved encodings reproduce that formula and full key. The
    cited paper’s own abstract instead defines enterocin A as a 47-residue mature
    peptide containing four cysteines, with reported mass 4,829. The sulfur-free graph
    cannot represent that cysteine-containing mature material as described. This is
    a concrete representation-versus-cited-material conflict; its source of error,
    exact replacement sequence/graph, disulfide topology, stock and accession mapping
    remain unresolved.
  evidence_ids:
  - SCI689-LOCAL
  - SCI689-CHEM
  - SCI689-OWN-ABSTRACT
  - SCI689-PMC-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- check_id: SCI689-FULLTEXT
  name: Substantive article body and exact replacement
  status: unavailable
  required: true
  summary: The attempted PMC source provides no body. Exact sequence tables, disulfide
    mapping and stock/accession relationship remain uninspected; no replacement structure
    is inferred from the abstract.
  evidence_ids:
  - SCI689-FULLTEXT-LIMIT
  - SCI689-PMC-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- check_id: SCI689-AUTHORITIES
  name: Current taxon, sequence and chemical authorities
  status: unavailable
  required: true
  summary: No current external taxon, sequence, protein or chemical authority was
    inspected. Internal key agreement and retained accessions do not verify those
    authorities.
  evidence_ids:
  - SCI689-LOCAL
  - SCI689-CHEM
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
evidence:
- evidence_id: SCI689-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch069-tentative/tentative-owner-source-inventory-001.json
  accessed_at: '2026-10-27T16:40:42.118890Z'
  locator: /entries/8/owner_document; /entries/8/rows; /entries/8/row_guards; /entries/8/supplemental_retained_rows
  snapshot_sha256: 1631e32dfca9a0ce9a2ba8290529bb15ad890e173c9de3b719b10edd7a44e9c1
  support: context_only
  summary: 'The whole retained enterocin A owner and seven source arrays contain three
    rows: one MIBiG compound row, one LOTUS occurrence and one NPClassifier result.
    Both supplemental arrays are empty. The owner has no activity annotations or causal
    graph. Producer and locus grades, occurrence qualification and histories are preserved
    as retained assertions.'
- evidence_id: SCI689-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch069-tentative/source-science-preparation/native-tentative69-local-chemical-consistency-and-neighbors-001.json
  accessed_at: '2026-10-27T16:50:39.486276Z'
  locator: /records/8/comparisons; /records/8/smiles; /records/8/inchi
  snapshot_sha256: b07a5f198bf2d4d697bffd7cce9213ae55d3b646f9cbf095d47524be65e5d58e
  support: supports
  summary: Saved RDKit 2026.03.5 diagnostics regenerate UDJYWZUEIHCKKJ-UHFFFAOYSA-N
    from both retained encodings, with formula C49H70N14O16, one fragment and formal
    charge zero. Standard InChI also agrees. This supports internal representation
    consistency, not experimental natural identity or current authority validity.
    Each encoding has 10 unassigned tetrahedral carbon sites. The 10 additional unspecified
    double-bond observations in parsed InChI are C(-O)=N environments, not additional
    unassigned C=C configurations.
- evidence_id: SCI689-ROOT-CHEM-READ
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch069-tentative/source-science-preparation/root-tentative69-saved-chemical-neighbor-interpretation-001.json
  accessed_at: '2026-10-27T16:53:08.042379Z'
  locator: /observations; /limits
  snapshot_sha256: 6217ca22284fc43b81947162e1c1946c7f7c1aa6cdcf4deecfc2b24467c953cf
  support: context_only
  summary: ROOT inspected the saved chemical comparisons and selected neighbors at
    the recorded time. This preserves the original computation interval and adds no
    external natural-identity or authority verification.
- evidence_id: SCI689-OWN-ABSTRACT
  kind: primary_source
  reference: /private/tmp/npm-review-work/shared-next-batch069-tentative/literature-preparation/public-metadata-001/pmid-8633865.xml
  accessed_at: '2026-10-27T16:52:24.510646Z'
  locator: ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText;
    ./PubmedArticle/PubmedData/ArticleIdList/ArticleId
  snapshot_sha256: df409dad2b41b9ef3dee601ead05c4aa81e022451d0cd55840828c7201863f26
  support: supports
  summary: 'The own PMID 8633865 abstract describes enterocin A purified from an Enterococcus
    faecium strain, with primary structure established by amino-acid and DNA sequencing:
    47 mature residues and four cysteines, calculated molecular weight 4,829 assuming
    intramolecular disulfides, confirmed by mass spectrometry. It also reports an
    18-residue N-terminal leader removed during maturation. These are abstract-level
    statements; no full sequence or replacement chemical graph is reconstructed.'
- evidence_id: SCI689-PMC-ABSTRACT
  kind: primary_source
  reference: /private/tmp/npm-review-work/shared-next-batch069-tentative/literature-preparation/public-primary-001/pmc-167941.xml
  accessed_at: '2026-10-27T17:06:04.671192Z'
  locator: ./article/front/article-meta/article-id; ./article/front/article-meta/abstract/p
  snapshot_sha256: ca1d9a445bddfc4a4369ac47f8a37dc0f6deec4cfabf640f9e11326a3035ce77
  support: supports
  summary: The matched PMC167941 response repeats the same study abstract, including
    47 residues, four cysteines, reported mass 4,829 and an 18-residue leader. This
    is a second response for the same paper, not independent experimental corroboration.
    It supplies no full article body.
- evidence_id: SCI689-FULLTEXT-LIMIT
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch069-tentative/literature-preparation/public-primary-001/pmc-167941.xml.access.json
  accessed_at: '2026-10-27T17:05:25.694924Z'
  locator: /http_status; /complete_body; /success; /error; /body; matched XML article
    comment and absence of ./article/body
  snapshot_sha256: b84ad9bfae85513d131d18f6857850f391af564e3f7d5b0e370702da3468c072
  support: context_only
  summary: The request returned complete HTTP 200 XML, but the publisher restriction
    leaves only front matter and abstract, with no substantive body. The collector
    recorded success=false and exited 1 at its body gate. This is a source-access
    limitation, not an official review-validation failure; sequence tables, figures
    and experimental methods remain unread.
- evidence_id: SCI689-MAINTENANCE
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/CURATION.md
  accessed_at: '2026-10-27T17:12:05.432230Z'
  locator: MIBiG structure corrections; scripts/seed_from_sources.py::apply_structure_corrections
    and write_records; src/naturalproductmech/curate/structure_corrections.py
  snapshot_sha256: c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa
  support: context_only
  summary: The maintained structure-correction interface pins an exact MIBiG compound
    row and an independently supported unambiguous 3-star ChEBI target. It does not
    supply a verified replacement here. Existing owner relocation requires a separately
    audited migration and re-audit of old-key claims; generated YAML must not be patched
    alone. A fresh source refresh or narrowly implemented alternative correction would
    require its own evidence and tests.
assessments:
- assessment_id: SCI689-ENCODING
  area: representation
  topic: Internal chemical representation
  outcome: supported
  summary: Saved RDKit 2026.03.5 diagnostics regenerate UDJYWZUEIHCKKJ-UHFFFAOYSA-N
    from both retained encodings, with formula C49H70N14O16, one fragment and formal
    charge zero. Standard InChI also agrees. This supports internal representation
    consistency, not experimental natural identity or current authority validity.
  evidence_ids:
  - SCI689-CHEM
  - SCI689-ROOT-CHEM-READ
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- assessment_id: SCI689-IDENTITY-CONFLICT
  area: identity
  topic: Formula versus cited mature peptide
  outcome: concern
  summary: The retained owner and exact MIBiG BGC0000618:1 version 3 row encode C49H70N14O16
    with no sulfur. Both saved encodings reproduce that formula and full key. The
    cited paper’s own abstract instead defines enterocin A as a 47-residue mature
    peptide containing four cysteines, with reported mass 4,829. The sulfur-free graph
    cannot represent that cysteine-containing mature material as described. This is
    a concrete representation-versus-cited-material conflict; its source of error,
    exact replacement sequence/graph, disulfide topology, stock and accession mapping
    remain unresolved.
  evidence_ids:
  - SCI689-LOCAL
  - SCI689-CHEM
  - SCI689-OWN-ABSTRACT
  - SCI689-PMC-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- assessment_id: SCI689-MATERIAL
  area: evidence
  topic: What the paper positively reports
  outcome: supported
  summary: 'The own PMID 8633865 abstract describes enterocin A purified from an Enterococcus
    faecium strain, with primary structure established by amino-acid and DNA sequencing:
    47 mature residues and four cysteines, calculated molecular weight 4,829 assuming
    intramolecular disulfides, confirmed by mass spectrometry. It also reports an
    18-residue N-terminal leader removed during maturation. These are abstract-level
    statements; no full sequence or replacement chemical graph is reconstructed.'
  evidence_ids:
  - SCI689-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- assessment_id: SCI689-STEREO
  area: representation
  topic: Stored stereochemical incompleteness
  outcome: unknown
  summary: Each encoding has 10 unassigned tetrahedral carbon sites. The 10 additional
    unspecified double-bond observations in parsed InChI are C(-O)=N environments,
    not additional unassigned C=C configurations. The declared stereo_complete=false
    is consistent with that local state. These sites are not assigned from a different
    mature peptide.
  evidence_ids:
  - SCI689-LOCAL
  - SCI689-CHEM
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- assessment_id: SCI689-PRODUCER
  area: provenance
  topic: Species versus exact producer strain
  outcome: unknown
  summary: The abstract supports isolation from an E. faecium strain; it does not
    identify the stored DO strain or align CP003583.1:2312434–2313194. The retained
    SOURCE_ASSERTION / CLUSTER_UNSTATED qualifiers and separate LOTUS species occurrence
    remain distinct. The structure conflict also prevents unqualified transfer of
    the paper’s production claim to the stored graph.
  evidence_ids:
  - SCI689-LOCAL
  - SCI689-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- assessment_id: SCI689-LOCUS
  area: provenance
  topic: Ribosomal origin and precursor
  outcome: unknown
  summary: The abstract supports a chromosomal structural gene and removal of an 18-residue
    leader, consistent with broad ribosomal peptide origin. It does not independently
    verify the current BGC0000618 locus coordinates or establish that this sulfur-free
    stored molecule is the mature product.
  evidence_ids:
  - SCI689-LOCAL
  - SCI689-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
- assessment_id: SCI689-MECHANISM
  area: completeness
  topic: Activity and putative immunity
  outcome: unknown
  summary: The title describes an antilisterial pediocin-family bacteriocin, but no
    quantitative activity or molecular target is assigned to the stored graph. A downstream
    103-residue ORF is described as a putative immunity factor; the abstract does
    not establish that mechanism experimentally.
  evidence_ids:
  - SCI689-OWN-ABSTRACT
  - SCI689-PMC-ABSTRACT
  - SCI689-LOCAL
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
findings:
- finding_id: F689-CITED-MATURE-MATERIAL
  issue_key: enterocin-a-bgc0000618-sulfur-free-structure-conflicts-cited-mature-peptide
  category: identity
  severity: major
  status: open
  certainty: provisional
  title: Stored enterocin A structure conflicts with the cited mature peptide
  description: The retained owner and exact MIBiG BGC0000618:1 version 3 row encode
    C49H70N14O16 with no sulfur. Both saved encodings reproduce that formula and full
    key. The cited paper’s own abstract instead defines enterocin A as a 47-residue
    mature peptide containing four cysteines, with reported mass 4,829. The sulfur-free
    graph cannot represent that cysteine-containing mature material as described.
    This is a concrete representation-versus-cited-material conflict; its source of
    error, exact replacement sequence/graph, disulfide topology, stock and accession
    mapping remain unresolved.
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
  field_paths:
  - chemical_structure
  - source_concepts[0]
  evidence_ids:
  - SCI689-LOCAL
  - SCI689-CHEM
  - SCI689-OWN-ABSTRACT
  - SCI689-PMC-ABSTRACT
  - SCI689-FULLTEXT-LIMIT
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: maintained
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: maintained
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: maintained
  rule_id: exact-compound-representation-must-match-cited-material
  native_severity: material identity and representation conflict
  normalization_reason: The absence of sulfur and the cited four-cysteine description
    are directly observed. Provisional applies to the record-to-material adjudication
    and unresolved corrective mapping; it does not diminish the observed conflict
    or assert a verified replacement.
actions:
- action_id: A689-RECONCILE-MATURE-STRUCTURE
  finding_ids:
  - F689-CITED-MATURE-MATERIAL
  target_ids:
  - naturalproductmech:mibig-c53d1bae68
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: maintained
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: maintained
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: maintained
  description: After separate maintainer authorization, reconcile BGC0000618:1 version
    3 and the exact stored full key with the cited mature sequence, disulfide state,
    source stock and accession. Establish the intended exact compound before changing
    any structure or source concept. If a verified unambiguous 3-star ChEBI target
    meets the implemented guards, use the pinned maintained correction path and explicit
    owner migration; otherwise implement and test a narrowly scoped evidence-backed
    path. Preserve raw source facts and history, and re-audit all old-key occurrences,
    xrefs and classifications rather than carrying them onto a different graph. No
    replacement is selected here.
  acceptance_checks:
  - Pin the whole original MIBiG row (source_id BGC0000618:1, version 3, row SHA256
    8c8186b26ad24cd51407c94ef312f491bad106a3b572f4018accfe55d7b99ffd) and establish
    source drift checks.
  - Inspect exact primary mature sequence and material-specific chemistry; reconcile
    four cysteines, maturation and mass without substituting the 18-residue leader
    or a fragment for the mature peptide.
  - Document independent identity evidence for any chosen target and re-audit NPA015771,
    LOTUS old-key occurrence and producer/locus links; no implicit equivalence or
    cross-key claim transfer.
  - Use validated migration with preserved history/PATHS.tsv where required, then
    run maintained structure-correction tests, documented strict validation, corpus
    checks and just verify-reproduction. These are future acceptance steps, not commands
    run by this DATA preparation.
  generator: scripts/seed_from_sources.py::apply_structure_corrections / write_records;
    src/naturalproductmech/curate/structure_corrections.py
limitations:
- Only the cited study abstract is available from both PubMed and the attempted PMC
  source. The complete HTTP response is not full-text access; no sequence table, figure
  or full experimental method was inspected.
- The formula/text conflict is directly observed. Whether the source structure is
  a fragment, another compound or another mapping error remains unresolved; no alternative
  molecular graph, natural configuration or disulfide topology is selected.
- The exact DO strain and listed genomic interval are not established by the inspected
  abstract; do not infer absence of production by that strain.
- Original owner/raw reading, saved computation, HTTP access and subsequent source
  interpretation have distinct clocks; full_owner_scientific_read remains false.
- No source row, structure, producer grade, locus, activity annotation or corpus file
  is changed by this review.
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
