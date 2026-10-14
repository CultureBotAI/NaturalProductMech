# Cercosporin exact-owner review: cercosporin-2

- Review: 20261014T003703Z-cercosporin-2
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-14T00:30:22.263397Z
- Finished UTC: 2026-10-14T00:37:03.536547Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact-structure qualification required; confirmed citation routing and complemented-experiment scope defects.

## Scope And Provenance

Entire exact owner and resolved mechanism at immutable base41b0ea2.

Selection: Next owner in3115-record campaign; same-name sibling separately reviewed.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 41b0ea200e57390c2b191f2519ff2971d37e55ea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-acffdd16a2 | data/natural_products/polyketides/cercosporin-2.yaml | generated | cercosporin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cercosporin-2-inspect | passed | True | naturalproductmech:mibig-acffdd16a2 | Canonical inspection, strict validation, graph computation or label gate passed; no claim of primary scientific closure. |
| strict | passed | True | naturalproductmech:mibig-acffdd16a2 | Canonical inspection, strict validation, graph computation or label gate passed; no claim of primary scientific closure. |
| chemistry | passed | True | naturalproductmech:mibig-acffdd16a2 | Canonical inspection, strict validation, graph computation or label gate passed; no claim of primary scientific closure. |
| labels | passed | True | naturalproductmech:mibig-acffdd16a2 | Canonical inspection, strict validation, graph computation or label gate passed; no claim of primary scientific closure. |
| Full native QC on exact base | passed | True | naturalproductmech:mibig-acffdd16a2 | Applicable to base41b0ea2; branch edits need fresh gates. |
| Complete exact-product primary adjudication | unavailable | True | naturalproductmech:mibig-acffdd16a2 | Partial:2017 publisher PDF403;1957 ACS page403; no bypass. Primary structural figures/supplements and absolute/helical stereochemistry remain incomplete. |

## Scientific And Domain Assessments

### Exact stereochemical product and tautomer form

identity: concern. Targets: naturalproductmech:mibig-acffdd16a2.

F1 requires explicit qualification. A registry conflict or computed tautomer relation does not establish a replacement structure.

### Stored graph self-consistency

consistency: supported. Targets: naturalproductmech:mibig-acffdd16a2.

Both assigned side-chain centers and neutral formula round-trip. stereo_complete:true is consistent with detected tetrahedral encoding, not proof of complete experimental/helical assignment.

### Minted identity versus exact registry join

grounding: supported. Targets: naturalproductmech:mibig-acffdd16a2.

No exact3-star pinned ChEBI key; keep minted identity and avoid automatic stereoisomer/tautomer equivalence.

### Independent computed, asserted and taxonomic axes

representation: supported. Targets: naturalproductmech:mibig-acffdd16a2.

Pinned polyketide filing and class reproduce; MIBiG PKS is asserted separately; current fungal species IDs support fungal taxonomic facets. Experimental engineering does not automatically change compound-origin class.

### Producer, occurrence and experimental context

scope: concern. Targets: naturalproductmech:mibig-acffdd16a2.

SOURCE_ASSERTION and CLUSTER_UNSTATED remain database grades. The complemented transformant cannot be silently read as unmodified native production; LOTUS cites that same study.

### Exact version and locus support

evidence: concern. Targets: naturalproductmech:mibig-acffdd16a2.

Active version, taxon and deposited accession match the source. Bioactivity citation is misrouted; partial native locus has CTB7 pseudogene and is not the complemented construct.

### Activity, targets, mechanism and datasets

graph: not_applicable. Targets: naturalproductmech:mibig-acffdd16a2.

No activities, targets, clinical assertions, pathway, graphs, refs or datasets are asserted. Optional absence is not a defect; do not copy family-level claims.

### Native status and generated boundaries

ownership: supported. Targets: naturalproductmech:mibig-acffdd16a2.

SEEDED and all existing seed events retained. Use maintained inputs and guarded writers for separately authorized curation.

## Findings

### F1: Cercosporin exact-structure qualification remains unresolved

major / open / confirmed; issue key: cercosporin-1542-tautomer-adjudication.

R,R native graph differs from pinned CHEBI3556 in quinone/proton representation; default RDKit tautomer canonicalization agrees, but exact-key grounding/claim transfer is not established.

### F2: Compound-bioactivity citation is misrouted to producer and locus

major / open / confirmed; issue key: mibig-bgc0001542-claim-reference-routing.

The1978 DOI belongs to compound bioactivity; entry reference PMID28535078 concerns CTB7 and is also cited by KY656140.1.

### F3: Native deposited locus and complemented producer context are not distinguished

major / open / confirmed; issue key: cercosporin-zeina-complementation-scope.

The primary abstract identifies a complemented C.zeina transformant, while native in-vitro production was absent in reported conditions. The deposited native CTB7 is a pseudogene. Neither a species-wide absence nor natural production of this exact product follows.

## Recommended Actions And Acceptance Checks

### A1

Track955; add cited OPEN qualification, then adjudicate primary structures and each source/occurrence before any source-pinned correction or migration.

- No automatic stereoisomer/tautomer merge or old-key claim transfer.
- Primary absolute/helical stereochemistry and source-specific claims adjudicated; linked successor review; strict/reproduction/QC.

### A2

Fix954 using complete-row-pinned claim reference decision and guarded canary/re-emission.

- Both database references become PMID28535078; separate curator evidence retains original citation and source digest.
- No chemistry, taxon, locus or grade changes; regression, strict, reproduction and QC pass.

### A3

Track956; add OPEN qualification now, obtain authorized full primary evidence and implement pinned claim-level context or withholding after exact-product adjudication.

- Distinguish native KY656140.1/CTB7 pseudogene from C.zeae-maydis-CTB7 complemented construct.
- Audit LOTUS occurrence independently; do not infer molecule origin ENGINEERED or species-wide absence.
- Qualification alone does not close finding; require successor disposition and native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/polyketides/cercosporin-2.yaml; Exact base41b0ea2, before publication fixes | supports | Complete raw owner and resolved mechanism read, including all source assertions and history; no inline graphs or graph refs. |
| chemistry | /private/tmp/npmech-cercosporin-review-vwJpVK/source-inspection.json; chemistry and chebi sections; script and execution receipt retained | supports | RDKit2026.03.5 round-trips both neutral C29H26O10 owners. Cercosporin has S,S centers; cercosporin-2 has R,R centers. The latter canonicalizes to pinned CHEBI:3556 under the default tautomer enumerator. Both achiral canonical tautomers agree. ChEBI3556 is R,R; ChEBI146017 is a dianion. This is graph analysis, not experimental absolute/helical stereochemical proof or permission to merge keys. |
| registry | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/cercosporin/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; All four properties records inspected | context_only | Name lookup returns CID2674,91617,360901,90471707 with differing stereo resolution/configurations. Only CID91617 exactly matches cercosporin-2. A name hit is not exact equivalence and none is an independently validated biological origin. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0001542.3/annotations.json; Entire exact versioned JSON inspected; questionable source quality is not scientific validation | supports | Active v3 PKS entry matches stored structure, taxon348901 and KY656140.1; no locus methods and zero placeholder bounds. The1978 DOI occurs under compound bioactivity; entry legacy reference is PMID28535078. |
| primary | PMID:28535078; Full PubMed abstract | refutes | The inspected abstract describes lack of native C.zeina in-vitro cercosporin and one transformant complemented with C.zeae-maydis CTB7 producing cercosporin under nitrogen-limited/light conditions, identified by KOH,TLC and UPLC-QTOFMS. A variant during maize infection is proposed, not observed exact-product evidence. |
| sequence | https://www.ncbi.nlm.nih.gov/nuccore/KY656140.1; GenBank source qualifiers, references and CTB feature annotations; taxonomy XML confirms all three native taxon IDs as fungal species | supports | KY656140.1 is a partial CTB cluster and CTB7 pseudogene from deposited isolate CMW25467, citing PMID28535078. It is not the complemented construct. |
| inventory | data/raw/mibig_compounds.tsv; source-inspection.json inventories with row denominators; all rows scanned | supports | Complete structured scans reproduce exact MIBiG/LOTUS/NPClassifier joins. Neither native key has an exact pinned ChEBI or AntibioticMech match. No PubChem BioAssay row joins either key. Computed filing remains distinct from asserted PKS and fungal organism facets. |
| search | /private/tmp/npmech-cercosporin-review-vwJpVK/local-search.log; Exact rg command in local-search.receipt.json; capture.json attests previous pair hashes | context_only | Ignored/hidden-inclusive local search and the60-pair checkpoint identify no earlier canonical owner review. Historical deterministic queues are not scientific reviews. |
| adapter | /private/tmp/npmech-cercosporin-review-vwJpVK/imodulondb.log; Entire adapter output | context_only | Complete structured dataset inventory has no matching Cercospora dataset. No expression-module search/summarize applies; this is not negative biosynthesis evidence. |
| rules | docs/CURATION.md; Current ownership and scientific-status rules | supports | Identity, source support and producer scope are required before REVIEWED. Generated fields use maintained corrections; decisions.tsv is reserved and unconsumed. New curator controversies survive only same-key guarded re-emission. |
| base-qc | https://github.com/CultureBotAI/NaturalProductMech/actions/runs/38489507183; Exact-base merge QC log and receipt | supports | Successful merge-group QC on exact reviewed41b0ea2 includes corpus, history, strict, references, provenance and byte-identical reproduction. Reused commit-bound execution, not a new local run or scientific approval. |

## Limits And Additional Notes

- 2017 primary PDF and1957 ACS page returned403; no alternate fulltext retrieval. Full primary figures/supplements and absolute/helical stereo remain unadjudicated.
- 2018 main-text sections and captions were inspected, not rendered structural figures or supplements. Do not equate database graph consistency with experimental identity.
- Name-based PubChem results are not all exact matches. Default RDKit tautomer canonicalization is computational context only.
- Label gate warnings/skips are nonblocking technical outcomes, not taxonomic or scientific completeness.
- Base QC is explicitly reused; subsequent edits need fresh checks. Optional missing mechanisms are not findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T003703Z-cercosporin-2
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Cercosporin exact-owner review: cercosporin-2'
started_at: '2026-10-14T00:30:22.263397Z'
finished_at: '2026-10-14T00:37:03.536547Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same campaign assistant; separate scientific review, not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: SEEDED retained; primary closure incomplete
scientific_review: true
summary: Exact-structure qualification required; confirmed citation routing and complemented-experiment
  scope defects.
source:
  git_revision: 41b0ea200e57390c2b191f2519ff2971d37e55ea
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
  - path: curation/decisions.tsv
    sha256: 7214a74975fb2cb65521da18dd14ea1c65665f50060106976dc0db9caf887805
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: f3f808ad1e58d79947aa82ecf1272e465cfbef57e5a4cd646731af23bb48ce75
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: a1eb14fec4a7cee0c2fc25c43091e75af24ae62c44c4f7659ed7aedf0e6a0e6c
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 6f879bb9f2c9be6b6e8de8c013dbaebe09075b7e106790ea303a17006761ea11
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: f61d7ba85ffd21837cd2b625f83c4681c4663e72503466b40eba3f4ab0204bc1
    role: context
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 18b61c1e5a69112c99cea1373791cd1ec571b7084bfd9198ab68fa551f5d531a
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/polyketides/cercosporin-2.yaml
    sha256: a1a77b0f45699fc80a4a59a46fdf9937a8356fcca77d8206d9b1102a2d1caeac
    role: target
  - path: data/natural_products/polyketides/cercosporin.yaml
    sha256: e0aa33a0698f5c6d23255bcb8eefccde09d0216f696fa78c0e4fdfad9941144e
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 373f049029be3db137e062ff5f872a2400a9d5b423f3e108ea44ebde2f8dcc7d
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
    sha256: 3ab166b341e5f3f1eaaee1b2af2485ac575c1a1eab1570bbf1d8d2d3ba76e53e
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
    sha256: e810fb0f289bc11d6369c8ac00cc3d0ff6ed96888c13048de478f725e62fab3e
    role: context
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
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
- target_id: naturalproductmech:mibig-acffdd16a2
  path: data/natural_products/polyketides/cercosporin-2.yaml
  label: cercosporin
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported chemical, producer and cluster assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Imported structure-organism-reference triples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned ChEBI grounding inventory
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Pinned ChEBI occurrence inventory
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned computed classification
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned sibling exact-structure joins
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated harmonization and grading
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: LOTUS extraction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Implemented pinned structure corrections
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Implemented exact-context method corrections
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented pinned strain qualifications
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Implemented complete-row-pinned PubChem and NPAtlas exclusions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Imported compound-specific assay observations
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_pubchem_bioassay.py
    role: BioAssay extraction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_isolates.tsv
    role: Implemented pinned isolate context
scope:
  description: Entire exact owner and resolved mechanism at immutable base41b0ea2.
  selection: Next owner in3115-record campaign; same-name sibling separately reviewed.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-acffdd16a2
checks:
- check_id: cercosporin-2-inspect
  name: cercosporin-2-inspect
  status: passed
  required: true
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/npmech-cercosporin-review-vwJpVK/cercosporin-2-targets.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/review-yaml-record/SKILL.md --input CLAUDE.md --input conf/id_label_targets.yaml
    --input conf/producer_evidence.tsv --input conf/record_review.yaml --input curation/decisions.tsv
    --input curation/mibig_claim_references.tsv --input curation/mibig_locus_evidence_overrides.tsv
    --input curation/mibig_producer_isolates.tsv --input curation/mibig_producer_strains.tsv
    --input curation/mibig_structure_corrections.tsv --input curation/mibig_xref_exclusions.tsv
    --input curation/pubchem_bioassay_exclusions.tsv --input data/natural_products/PATHS.tsv
    --input data/natural_products/polyketides/cercosporin-2.yaml --input data/natural_products/polyketides/cercosporin.yaml
    --input data/raw/MANIFEST.yaml --input data/raw/antibioticmech_inchikeys.tsv --input
    data/raw/chebi_origins.tsv --input data/raw/chebi_structures.tsv --input data/raw/corpus_taxa.obo
    --input data/raw/lotus_occurrences.tsv --input data/raw/mibig_compounds.tsv --input
    data/raw/npclassifier.tsv --input data/raw/pubchem_bioassay.tsv --input docs/CURATION.md
    --input docs/HARMONIZATION.md --input docs/record-review-profile.md --input docs/record-reviews.md
    --input justfile --input pyproject.toml --input schema/record_review.yaml --input
    scripts/extract_lotus.py --input scripts/extract_mibig.py --input scripts/extract_pubchem_bioassay.py
    --input scripts/record_review.py --input scripts/run_qc.py --input scripts/seed_from_sources.py
    --input src/naturalproductmech/curate/bioassay_exclusions.py --input src/naturalproductmech/curate/producer_strains.py
    --input src/naturalproductmech/curate/structure_corrections.py --input src/naturalproductmech/curate/xref_exclusions.py
    --input src/naturalproductmech/graph_components.py --input src/naturalproductmech/schema/history.yaml
    --input src/naturalproductmech/schema/mech_shared.yaml --input src/naturalproductmech/schema/naturalproductmech.yaml
    --input uv.lock
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  summary: Canonical inspection, strict validation, graph computation or label gate
    passed; no claim of primary scientific closure.
  scope_note: 2026-10-14T00:30:22.277139Z..2026-10-14T00:30:24.243088Z; /private/tmp/npmech-cercosporin-review-vwJpVK/cercosporin-2-inspect.json;
    SHA256 4bcf68eb1f2c4d2f3311c5435c7c9e66c70ddc51711316276b85c1b90935517d
- check_id: strict
  name: strict
  status: passed
  required: true
  command: just validate-strict data/natural_products/polyketides/cercosporin-2.yaml
    data/natural_products/polyketides/cercosporin.yaml --out /private/tmp/npmech-cercosporin-review-vwJpVK/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  summary: Canonical inspection, strict validation, graph computation or label gate
    passed; no claim of primary scientific closure.
  scope_note: 2026-10-14T00:30:41.229915Z..2026-10-14T00:30:44.686678Z; /private/tmp/npmech-cercosporin-review-vwJpVK/strict.log;
    SHA256 f8ed408be0f86f31889752e48ed68be831d311235d6adc6521f7e4818bfb56b1
- check_id: chemistry
  name: chemistry
  status: passed
  required: true
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-cercosporin-review-vwJpVK/inspect_sources.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  summary: Canonical inspection, strict validation, graph computation or label gate
    passed; no claim of primary scientific closure.
  scope_note: 2026-10-14T00:34:33.062876Z..2026-10-14T00:34:36.251778Z; /private/tmp/npmech-cercosporin-review-vwJpVK/chemistry.log;
    SHA256 12ae1737d9d4cf931a12a33f3ae27eccd41d43c0909a3891d3d4ad2e445900ba
- check_id: labels
  name: labels
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  summary: Canonical inspection, strict validation, graph computation or label gate
    passed; no claim of primary scientific closure.
  scope_note: 2026-10-14T00:30:42.390452Z..2026-10-14T00:32:30.846487Z; /private/tmp/npmech-cercosporin-review-vwJpVK/labels.log;
    SHA256 19a4f6cca7894851de23ee2062f52d29b32def53c7b4f59edbc6c45ec4ce9828
- check_id: qc
  name: Full native QC on exact base
  command: just qc (reused exact-base CI execution)
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  evidence_ids:
  - base-qc
  summary: Applicable to base41b0ea2; branch edits need fresh gates.
- check_id: primary-closure
  name: Complete exact-product primary adjudication
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  summary: Partial:2017 publisher PDF403;1957 ACS page403; no bypass. Primary structural
    figures/supplements and absolute/helical stereochemistry remain incomplete.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/polyketides/cercosporin-2.yaml
  summary: Complete raw owner and resolved mechanism read, including all source assertions
    and history; no inline graphs or graph refs.
  locator: Exact base41b0ea2, before publication fixes
  accessed_at: '2026-10-14T00:37:03.529240Z'
  support: supports
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-cercosporin-review-vwJpVK/source-inspection.json
  summary: RDKit2026.03.5 round-trips both neutral C29H26O10 owners. Cercosporin has
    S,S centers; cercosporin-2 has R,R centers. The latter canonicalizes to pinned
    CHEBI:3556 under the default tautomer enumerator. Both achiral canonical tautomers
    agree. ChEBI3556 is R,R; ChEBI146017 is a dianion. This is graph analysis, not
    experimental absolute/helical stereochemical proof or permission to merge keys.
  locator: chemistry and chebi sections; script and execution receipt retained
  accessed_at: '2026-10-14T00:37:03.529373Z'
  support: supports
  snapshot_sha256: 7d722af792f828f06b8d3ac8c5af733b688ce28ad930b920b665f39d3709ac79
- evidence_id: registry
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/cercosporin/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  summary: Name lookup returns CID2674,91617,360901,90471707 with differing stereo
    resolution/configurations. Only CID91617 exactly matches cercosporin-2. A name
    hit is not exact equivalence and none is an independently validated biological
    origin.
  locator: All four properties records inspected
  accessed_at: '2026-10-14T00:37:03.529660Z'
  support: context_only
  snapshot_sha256: e2f80841bb2ad1154ae28e1d5b781d62385d957edb05382a7b93af66ababdd6c
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0001542.3/annotations.json
  summary: Active v3 PKS entry matches stored structure, taxon348901 and KY656140.1;
    no locus methods and zero placeholder bounds. The1978 DOI occurs under compound
    bioactivity; entry legacy reference is PMID28535078.
  locator: Entire exact versioned JSON inspected; questionable source quality is not
    scientific validation
  accessed_at: '2026-10-14T00:37:03.529957Z'
  support: supports
  snapshot_sha256: edc33d0bd49b7fbb8b8ba32111b235582e355e7d14aefb0fd7a4cc8ef24586da
- evidence_id: primary
  kind: primary_source
  reference: PMID:28535078
  summary: The inspected abstract describes lack of native C.zeina in-vitro cercosporin
    and one transformant complemented with C.zeae-maydis CTB7 producing cercosporin
    under nitrogen-limited/light conditions, identified by KOH,TLC and UPLC-QTOFMS.
    A variant during maize infection is proposed, not observed exact-product evidence.
  locator: Full PubMed abstract
  accessed_at: '2026-10-14T00:37:03.530393Z'
  support: refutes
  snapshot_sha256: e4cac8770a6d77509f61a33930b5e583055079d5e8627bc729bcee4095b4db69
- evidence_id: sequence
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/KY656140.1
  summary: KY656140.1 is a partial CTB cluster and CTB7 pseudogene from deposited
    isolate CMW25467, citing PMID28535078. It is not the complemented construct.
  locator: GenBank source qualifiers, references and CTB feature annotations; taxonomy
    XML confirms all three native taxon IDs as fungal species
  accessed_at: '2026-10-14T00:37:03.530867Z'
  support: supports
  snapshot_sha256: 6dede57a3bbeb81c94c68bcbc83c7c8bec124c93257f3918b84c1f5c01a10313
- evidence_id: inventory
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  summary: Complete structured scans reproduce exact MIBiG/LOTUS/NPClassifier joins.
    Neither native key has an exact pinned ChEBI or AntibioticMech match. No PubChem
    BioAssay row joins either key. Computed filing remains distinct from asserted
    PKS and fungal organism facets.
  locator: source-inspection.json inventories with row denominators; all rows scanned
  accessed_at: '2026-10-14T00:37:03.531530Z'
  support: supports
  snapshot_sha256: 7d722af792f828f06b8d3ac8c5af733b688ce28ad930b920b665f39d3709ac79
- evidence_id: search
  kind: search
  reference: /private/tmp/npmech-cercosporin-review-vwJpVK/local-search.log
  summary: Ignored/hidden-inclusive local search and the60-pair checkpoint identify
    no earlier canonical owner review. Historical deterministic queues are not scientific
    reviews.
  locator: Exact rg command in local-search.receipt.json; capture.json attests previous
    pair hashes
  accessed_at: '2026-10-14T00:37:03.531776Z'
  support: context_only
  search_scope: curation,conf,reviews,.claude and named MIBiG/LOTUS/ChEBI/AntibioticMech
    TSVs; both keys, label and accessions; ignored/hidden included; compressed contents
    excluded
  snapshot_sha256: 964bda6ac11a627f5988186289008bf7d9a7bc62880861527f71cd647bc78d55
- evidence_id: adapter
  kind: database
  reference: /private/tmp/npmech-cercosporin-review-vwJpVK/imodulondb.log
  summary: Complete structured dataset inventory has no matching Cercospora dataset.
    No expression-module search/summarize applies; this is not negative biosynthesis
    evidence.
  locator: Entire adapter output
  accessed_at: '2026-10-14T00:37:03.534075Z'
  support: context_only
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  summary: Identity, source support and producer scope are required before REVIEWED.
    Generated fields use maintained corrections; decisions.tsv is reserved and unconsumed.
    New curator controversies survive only same-key guarded re-emission.
  locator: Current ownership and scientific-status rules
  accessed_at: '2026-10-14T00:37:03.534439Z'
  support: supports
- evidence_id: base-qc
  kind: validation
  reference: https://github.com/CultureBotAI/NaturalProductMech/actions/runs/38489507183
  summary: Successful merge-group QC on exact reviewed41b0ea2 includes corpus, history,
    strict, references, provenance and byte-identical reproduction. Reused commit-bound
    execution, not a new local run or scientific approval.
  locator: Exact-base merge QC log and receipt
  accessed_at: '2026-10-14T00:37:03.534456Z'
  support: supports
  snapshot_sha256: 4dba7bb98c5bf06a58e883b6d35902927606115a4aa931e8887db1bfc9e01161
assessments:
- assessment_id: identity
  area: identity
  topic: Exact stereochemical product and tautomer form
  outcome: concern
  summary: F1 requires explicit qualification. A registry conflict or computed tautomer
    relation does not establish a replacement structure.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  evidence_ids:
  - owner
  - chemistry
  - registry
  - primary
- assessment_id: encoding
  area: consistency
  topic: Stored graph self-consistency
  outcome: supported
  summary: Both assigned side-chain centers and neutral formula round-trip. stereo_complete:true
    is consistent with detected tetrahedral encoding, not proof of complete experimental/helical
    assignment.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  evidence_ids:
  - owner
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Minted identity versus exact registry join
  outcome: supported
  summary: No exact3-star pinned ChEBI key; keep minted identity and avoid automatic
    stereoisomer/tautomer equivalence.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  evidence_ids:
  - inventory
  - chemistry
- assessment_id: classification
  area: representation
  topic: Independent computed, asserted and taxonomic axes
  outcome: supported
  summary: Pinned polyketide filing and class reproduce; MIBiG PKS is asserted separately;
    current fungal species IDs support fungal taxonomic facets. Experimental engineering
    does not automatically change compound-origin class.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  evidence_ids:
  - inventory
  - mibig
  - sequence
- assessment_id: origin
  area: scope
  topic: Producer, occurrence and experimental context
  outcome: concern
  summary: SOURCE_ASSERTION and CLUSTER_UNSTATED remain database grades. The complemented
    transformant cannot be silently read as unmodified native production; LOTUS cites
    that same study.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  evidence_ids:
  - owner
  - primary
  - sequence
  - inventory
- assessment_id: clusters
  area: evidence
  topic: Exact version and locus support
  outcome: concern
  summary: Active version, taxon and deposited accession match the source. Bioactivity
    citation is misrouted; partial native locus has CTB7 pseudogene and is not the
    complemented construct.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  evidence_ids:
  - mibig
  - sequence
  - primary
- assessment_id: optional
  area: graph
  topic: Activity, targets, mechanism and datasets
  outcome: not_applicable
  summary: No activities, targets, clinical assertions, pathway, graphs, refs or datasets
    are asserted. Optional absence is not a defect; do not copy family-level claims.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  evidence_ids:
  - owner
  - inventory
  - adapter
- assessment_id: audit
  area: ownership
  topic: Native status and generated boundaries
  outcome: supported
  summary: SEEDED and all existing seed events retained. Use maintained inputs and
    guarded writers for separately authorized curation.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  evidence_ids:
  - owner
  - rules
  - base-qc
findings:
- finding_id: F1
  issue_key: cercosporin-1542-tautomer-adjudication
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Cercosporin exact-structure qualification remains unresolved
  description: R,R native graph differs from pinned CHEBI3556 in quinone/proton representation;
    default RDKit tautomer canonicalization agrees, but exact-key grounding/claim
    transfer is not established.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  field_paths:
  - chemical_structure
  - grounding_notes
  - occurrences
  evidence_ids:
  - owner
  - chemistry
  - registry
  - primary
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Maintained input or generation owner
  rule_id: Exact identity and supported stereochemical resolution
  native_severity: major
  normalization_reason: Confirmed representation conflict requires qualification;
    experimental wrong identity is not established, so not a blocker.
- finding_id: F2
  issue_key: mibig-bgc0001542-claim-reference-routing
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Compound-bioactivity citation is misrouted to producer and locus
  description: The1978 DOI belongs to compound bioactivity; entry reference PMID28535078
    concerns CTB7 and is also cited by KY656140.1.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  field_paths:
  - producer_organisms[0].evidence
  - biosynthetic_gene_clusters[0].evidence
  evidence_ids:
  - owner
  - mibig
  - sequence
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained input or generation owner
  rule_id: Evidence on narrowest supported claim
  native_severity: major
  normalization_reason: Material claim-specific citation routing defect.
- finding_id: F3
  issue_key: cercosporin-zeina-complementation-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Native deposited locus and complemented producer context are not distinguished
  description: The primary abstract identifies a complemented C.zeina transformant,
    while native in-vitro production was absent in reported conditions. The deposited
    native CTB7 is a pseudogene. Neither a species-wide absence nor natural production
    of this exact product follows.
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  field_paths:
  - producer_organisms
  - occurrences
  - biosynthetic_gene_clusters
  evidence_ids:
  - owner
  - primary
  - sequence
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained input or generation owner
  rule_id: Native organism versus engineered experiment; occurrence is not production
  native_severity: major
  normalization_reason: Missing material experiment scope risks unsupported native
    production interpretation.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Maintained input or generation owner
  description: Track955; add cited OPEN qualification, then adjudicate primary structures
    and each source/occurrence before any source-pinned correction or migration.
  acceptance_checks:
  - No automatic stereoisomer/tautomer merge or old-key claim transfer.
  - Primary absolute/helical stereochemistry and source-specific claims adjudicated;
    linked successor review; strict/reproduction/QC.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained input or generation owner
  description: Fix954 using complete-row-pinned claim reference decision and guarded
    canary/re-emission.
  acceptance_checks:
  - Both database references become PMID28535078; separate curator evidence retains
    original citation and source digest.
  - No chemistry, taxon, locus or grade changes; regression, strict, reproduction
    and QC pass.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - naturalproductmech:mibig-acffdd16a2
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Maintained input or generation owner
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained input or generation owner
  description: Track956; add OPEN qualification now, obtain authorized full primary
    evidence and implement pinned claim-level context or withholding after exact-product
    adjudication.
  acceptance_checks:
  - Distinguish native KY656140.1/CTB7 pseudogene from C.zeae-maydis-CTB7 complemented
    construct.
  - Audit LOTUS occurrence independently; do not infer molecule origin ENGINEERED
    or species-wide absence.
  - Qualification alone does not close finding; require successor disposition and
    native gates.
limitations:
- 2017 primary PDF and1957 ACS page returned403; no alternate fulltext retrieval.
  Full primary figures/supplements and absolute/helical stereo remain unadjudicated.
- 2018 main-text sections and captions were inspected, not rendered structural figures
  or supplements. Do not equate database graph consistency with experimental identity.
- Name-based PubChem results are not all exact matches. Default RDKit tautomer canonicalization
  is computational context only.
- Label gate warnings/skips are nonblocking technical outcomes, not taxonomic or scientific
  completeness.
- Base QC is explicitly reused; subsequent edits need fresh checks. Optional missing
  mechanisms are not findings.
tags:
- cercosporin
- record-review-campaign
- stereochemistry
- production-context
```
