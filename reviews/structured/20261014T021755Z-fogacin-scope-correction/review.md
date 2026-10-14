# Fogacin: scoped locus-grade and caption-provenance correction

- Review: 20261014T021755Z-fogacin-scope-correction
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-14T02:17:53.254885Z
- Finished UTC: 2026-10-14T02:17:55.430383Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact-compound inherited locus method is withdrawn and the mutant context retained separately. Caption provenance is distinguished from abstract-only XML. Primary structure and native-production adjudication remain incomplete; SEEDED is retained.

## Scope And Provenance

Entire exact owner and resolved mechanism, source identifiers and bounded primary evidence.

Selection: Next exact owner in3115-record campaign; the other same-label owner is assessed separately.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 54f772c74310759803ad65527dc73d567f953211.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-a4fac30c3f | data/natural_products/polyketides/fogacin.yaml | generated | fogacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| chemistry | passed | True | naturalproductmech:mibig-a4fac30c3f | Executed successfully within declared scope. |
| strict | passed | True | naturalproductmech:mibig-a4fac30c3f | Executed successfully within declared scope. |
| labels | passed | True | naturalproductmech:mibig-a4fac30c3f | 499 nonblocking label warnings and4649 no-adapter skips. |
| local-search | passed | True | naturalproductmech:mibig-a4fac30c3f | Executed successfully within declared scope. |
| Exact-base native QC | unavailable | True | naturalproductmech:mibig-a4fac30c3f | Full corrected-branch QC has not completed at assessment time; baseline QC does not cover the native correction. Final CI must pass before merge. |
| Exact-product primary scientific closure | unavailable | True | naturalproductmech:mibig-a4fac30c3f | Primary structural assignments and exact wild-type production remain unresolved; no full-text access bypass. |
| Corrective regression-final | passed | True | naturalproductmech:mibig-a4fac30c3f | Actual successful scoped execution; native status is not promoted. |
| Corrective strict-final | passed | True | naturalproductmech:mibig-a4fac30c3f | Actual successful scoped execution; native status is not promoted. |
| Corrective reproduction | passed | True | naturalproductmech:mibig-a4fac30c3f | Actual successful scoped execution; native status is not promoted. |
| Corrective portable-replay | passed | True | naturalproductmech:mibig-a4fac30c3f | Actual successful scoped execution; native status is not promoted. |
| Corrective render | passed | True | naturalproductmech:mibig-a4fac30c3f | Actual successful scoped execution; native status is not promoted. |
| Corrective lint-final | passed | True | naturalproductmech:mibig-a4fac30c3f | Actual successful scoped execution; native status is not promoted. |

## Scientific And Domain Assessments

### Structure and encoded stereochemical resolution

consistency: supported. Targets: naturalproductmech:mibig-a4fac30c3f.

Stored chemistry and stereo_complete agree; no primary absolute-configuration certification.

### Primary structure and same-name boundary

identity: unknown. Targets: naturalproductmech:mibig-a4fac30c3f.

Two distinct graphs are preserved. Same label does not establish equivalence or select a corrected identity.

### Exact pinned joins

grounding: supported. Targets: naturalproductmech:mibig-a4fac30c3f.

Minted identity is consistent with no pinned exact-key ChEBI match; no name-based transfer.

### Computed classification and asserted taxonomic facets

representation: supported. Targets: naturalproductmech:mibig-a4fac30c3f.

POLYKETIDES/classifier model provenance, asserted PKS and actinobacterial facets reproduce. Model subclass output is not asserted chemistry.

### Producer and experimental context

scope: unknown. Targets: naturalproductmech:mibig-a4fac30c3f.

SOURCE_ASSERTION is retained. Neither native exact-product production nor ENGINEERED molecular origin is inferred from heterologous expression.

### Compound-specific locus grade

evidence: supported. Targets: naturalproductmech:mibig-a4fac30c3f.

Only the exact compound method is withdrawn. CLUSTER_UNSTATED and separate CURATOR_INFERENCE preserve the mutant context, while the original database assertion remains.

### Optional mechanisms and activities

graph: not_applicable. Targets: naturalproductmech:mibig-a4fac30c3f.

No native pathways, targets, activities, graph components or datasets to audit. Optional absence is not a defect.

### Web caption versus abstract-only hash

provenance: supported. Targets: naturalproductmech:mibig-a4fac30c3f.

Successor explicitly separates the inspected web observation from the efetch payload and subsequent browser challenge.

## Findings

### locus-scope: Entry-level method overgrades the exact fogacin locus claim

major / resolved / confirmed; issue key: fogacin-bgc0000248-intact-locus-grade.

The recorded intact deposited locus is CLUSTER_DEMONSTRATED without the mutant experimental qualification. Withdraw applicability of the inherited method for this exact source compound while preserving the original database assertion and separately cited experiment context.

Disposition: Source-pinned exact-compound WITHDRAW, regenerated owner and sibling/drift regressions resolve this bounded grade inflation. This does not resolve the independent identity and production uncertainties in #963.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/polyketides/fogacin.yaml; Working-tree successor at archived base54f772c74 | supports | Entire corrected raw/resolved owner re-read; chemical identity, source assertion and SEEDED remain. One guarded seed history event records the table-driven correction. |
| chemistry | reviews/evidence/20261014-fogacin/source-inspection.json; chemistry; pinned RDKit2026.03.5, atom indices are graph indices not paper numbering | supports | Stored SMILES, InChI and key round-trip. C16H16O6 has two specified centers; C16H18O6 has two specified and one undefined center. These are different hydrogenation states, not interchangeable stereochemical resolutions. |
| inventory | reviews/evidence/20261014-fogacin/source-inspection.json; inventories; ChEBI origins joined through exact-key ChEBI IDs; bounded committed inventory scope | supports | Exact-key full scans find one MIBiG and one NPClassifier row per owner, no ChEBI structure/origin or AntibioticMech match. Only WGM has two LOTUS rows and a PubChem no-assay-data sentinel, not an activity observation. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0000248.5/annotations.json; Entire versioned JSON; quality is not a truth signal | supports | Active version5, compound2, native SMILES, DSM40737 label, species taxon29301 and JAKQYH010000014.1 bounds match. Heterologous expression is entry-level; legacy citation10206788 differs from pathway citation37989784. |
| taxonomy | reviews/evidence/20261014-fogacin/source-inspection.json; taxonomy, source features and wikidata; sequence annotations do not prove protein function | supports | NCBI512565 is strain431;29301 is S.arenae species, not DSM40737 strain rank. GenBank source qualifiers preserve431/NBRC102363 and DSM40737 respectively. Occurrence IDs1866/1883 are species/genus, independently matching both Wikidata P685 values. |
| primary | PMID:10206788; Complete PubMed abstract and PMID/DOI mapping; no full-text adjudication | context_only | The1999 abstract concerns naphthocyclinones and minimal-PKS mutactin/dehydromutactin experiments; it does not establish exact fogacin production. |
| experiment | https://pubmed.ncbi.nlm.nih.gov/37989784/; Previously inspected public abstract and Figure2B web caption; the old hash attested abstracts-extra.xml only, not this caption. No raw caption snapshot is archived. Details in primary-observations.json. | refutes | Abstract and public Figure2 caption distinguish intact ncn-cluster expression from fogacin accumulation in S.albus carrying an ncnN deletion. Complementation restores naphthocyclinone production. |
| search | reviews/evidence/20261014-fogacin/local-search.log; Command and log in checks.json | context_only | Hidden/ignored-inclusive search and prior68-bundle checkpoint found no prior exact-owner canonical review. Compressed contents excluded. |
| adapter | reviews/evidence/20261014-fogacin/imodulondb.log; Full structured adapter inventory | context_only | The28-dataset inventory has no matching A.missouriensis or S.arenae dataset. Other Streptomyces datasets are not substitutes; no component query applies. |
| base-qc | https://github.com/CultureBotAI/NaturalProductMech/actions/runs/38497123596; Merge QC; log SHA256e1896e5e78f1e6cb44e4939a950279b0d4f34ad33c0047f0914d9072b2315c47 | supports | Historical baseline-only full QC, not QC of this corrected native record. Fresh scoped checks and reproduction are retained separately; final full PR QC is still pending at this observation. |
| remediation | reviews/evidence/20261014-fogacin/remediation-checks.json; Actual commands, UTC times, exit codes and retained log hashes | supports | 94 focused tests, strict validation, guarded canary, rendering and full corpus reproduction passed. Portable replay from outside the checkout equals the baseline output. |
| caption-provenance | reviews/evidence/20261014-fogacin/primary-observations.json; Separate web-caption observation, abstract-only digest and later HTTP203 challenge; raw article not redistributed | supports | Corrects the prior implication that abstract XML also attested the caption. This file hashes reviewer observations, not a captured caption payload. |
| delta | reviews/evidence/20261014-fogacin/native-delta.json; All baseline-tracked owners/components/raw inputs/prior review files compared with historical Git bytes | supports | Only fogacin.yaml differs among3115 owners;3114 other owners,243 components, raw inputs and68 prior bundles are byte-identical. |

## Limits And Additional Notes

- Primary structure/hydrogenation and absolute stereochemistry remain unadjudicated; no automatic merge or replacement.
- PMC10697411 returned a browser/CAPTCHA challenge; Wiley2019 was unavailable to the web tool; Nature2006 PDF redirected to HTML with cookies_not_supported. No alternate full-text retrieval after these stops.
- The1999 paper was assessed only through its abstract. PubMed2023 public caption is not full-text or figure-image inspection.
- NCBITaxon29301 is species-ranked; DSM40737 is source strain context. NCBITaxon512565 is strain-ranked.
- No exhaustive live chemical-registry search. Negative joins are limited to the scanned pinned inventories.
- No native status promotion, curation event or optional graph fabrication follows from this review.
- Corrected-branch full QC is pending at assessment time and must pass before merge; scoped regression/reproduction success is not a substitute.
- The original experiment evidence attached an abstract-only digest to a caption observation. The successor removes that misleading implication. A later direct PubMed capture returned a browser challenge; no alternate retrieval followed.
- Source base54f772c74 is retained by annotated tag review-base/fogacin-20261014; fetch this tag in restricted clones. Working-tree input hashes attest the corrected bytes, not the unchanged historical tree.
- Issue965 is corrected through successor provenance, not by rewriting the initial review. Issue963 remains open.
- Initial focused/lint invocations were blocked by uv cache permissions and passed on authorized reruns; both attempts are retained. The unsaved initial fogacin draft used invalid assessment outcome concerning; canonical validation rejected it, and concern was used before initial persistence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T021755Z-fogacin-scope-correction
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Fogacin: scoped locus-grade and caption-provenance correction'
started_at: '2026-10-14T02:17:53.254885Z'
finished_at: '2026-10-14T02:17:55.430383Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same campaign assistant, not an independent reviewer.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
native_verdict: SEEDED retained; primary identity closure incomplete
scientific_review: true
summary: The exact-compound inherited locus method is withdrawn and the mutant context
  retained separately. Caption provenance is distinguished from abstract-only XML.
  Primary structure and native-production adjudication remain incomplete; SEEDED is
  retained.
source:
  git_revision: 54f772c74310759803ad65527dc73d567f953211
  state: working_tree
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
    sha256: a0d43a9ba94c7e0044a5e9bc85f829ad5d010264f44c4a3470739eb7511c9740
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7d3e07b98587b27ec843ce73e7c5cf75b74d6fecb4ab8fdc29ca54fa04352a53
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
  - path: data/natural_products/polyketides/fogacin-2.yaml
    sha256: 583bc7a30caa9e09498d5c42a657629f1132e4e4c0a4951adeb6270cba04f57b
    role: context
  - path: data/natural_products/polyketides/fogacin.yaml
    sha256: c7a8e08e33b04eadee3ba1017ee37fc32f043403e58ce411d30311909c679e90
    role: target
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
  - path: reviews/evidence/20261014-fogacin/.gitattributes
    sha256: 1729abd77269b6269250d91e547dda99551c356ef2d37304d4f1b85a2455145b
    role: context
  - path: reviews/evidence/20261014-fogacin/README.md
    sha256: 5cd384d626185b2e789a08b39833621318566c1dd2f9b79a86e3ca0fe2d5f2ac
    role: context
  - path: reviews/evidence/20261014-fogacin/canary.log
    sha256: 13c90ab3dc86eefb95c0884607a7571272a5254e691729c0f98dabf5b2b6cf93
    role: context
  - path: reviews/evidence/20261014-fogacin/checks.json
    sha256: 512612484e049831379a2122d9b8a42f21b1a45871778dcfb933c2db06d6e55b
    role: context
  - path: reviews/evidence/20261014-fogacin/chemistry.log
    sha256: 8d6205343d87c16f1a7bde34b7cf42b7648cec9a8c30875027079102da2fd7c1
    role: context
  - path: reviews/evidence/20261014-fogacin/docs-stats.log
    sha256: d6df4fbeba089d7a874e963ccc436a301e2bbf8f98f621e4ab5d87eb37699160
    role: context
  - path: reviews/evidence/20261014-fogacin/focused-retry.log
    sha256: ce2fae86fbeefc5c9f71c183dce8606a5bac2c308b46ea84825db9f7a143ae5c
    role: context
  - path: reviews/evidence/20261014-fogacin/focused.log
    sha256: b51fba8fc74f9b458a4bbbbe3846cf46757c3ef1baeb95a7d7d0e90fbc09253e
    role: context
  - path: reviews/evidence/20261014-fogacin/imodulondb.log
    sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
    role: context
  - path: reviews/evidence/20261014-fogacin/inputs/AP012319.1-region.xml
    sha256: ddca04c73d65c5d1eed971c814e89303bf2f9397edf5f403deca2be19a58c733
    role: context
  - path: reviews/evidence/20261014-fogacin/inputs/BGC0000248.5.json
    sha256: 4f4ef8b412947d43b953ac465dfb88d9a285022d982f8eefa9feebad8966b510
    role: context
  - path: reviews/evidence/20261014-fogacin/inputs/BGC0002021.3.json
    sha256: 6cf7ca6757ff3b37bd159eb85a667f2f99a62b80bfa28704e385f19927ac3c5d
    role: context
  - path: reviews/evidence/20261014-fogacin/inputs/JAKQYH010000014.1-region.xml
    sha256: ae3d3807a8960ac3a9c4179ab0c12eb97319a3d29e163a74b74355c25481c2bd
    role: context
  - path: reviews/evidence/20261014-fogacin/inputs/pubchem-11493248.json
    sha256: ae3c73a001f1599e3dc83cdef05372483e077a9d4417add617b99cb9b90b668f
    role: context
  - path: reviews/evidence/20261014-fogacin/inputs/taxonomy.xml
    sha256: 922d89a54a0d1638d9ee29812e852484f3f373577af498a83bff1fd64bc24afa
    role: context
  - path: reviews/evidence/20261014-fogacin/inputs/wikidata-Q1144013.json
    sha256: a17f3d23992752d0d727900478ea5df9bcf9814a57400b127d4e57fa42e4aa79
    role: context
  - path: reviews/evidence/20261014-fogacin/inputs/wikidata-Q25834569.json
    sha256: 0aecb345208cd24499955cbc0909bd773d7e6020da66f5fc28851296524b52f6
    role: context
  - path: reviews/evidence/20261014-fogacin/inspect_sources.py
    sha256: e6d16abd5080a96539e5b5ddd7c273b71d48b626885717b9e43049497a5def2e
    role: context
  - path: reviews/evidence/20261014-fogacin/labels.log
    sha256: 19a4f6cca7894851de23ee2062f52d29b32def53c7b4f59edbc6c45ec4ce9828
    role: context
  - path: reviews/evidence/20261014-fogacin/lint-final.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reviews/evidence/20261014-fogacin/lint-retry.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reviews/evidence/20261014-fogacin/lint.log
    sha256: b51fba8fc74f9b458a4bbbbe3846cf46757c3ef1baeb95a7d7d0e90fbc09253e
    role: context
  - path: reviews/evidence/20261014-fogacin/local-search.log
    sha256: 47fdb954f1d8dae2a9b8c25b0112d3c8b3d9af6e09a9ce14290b843aefe05a2b
    role: context
  - path: reviews/evidence/20261014-fogacin/native-delta.json
    sha256: d1bbd9a92000626fb728b916d1ce1f5502d16e6448a7ff66b31050e92bef3ba9
    role: context
  - path: reviews/evidence/20261014-fogacin/portable-replay.log
    sha256: 8d6205343d87c16f1a7bde34b7cf42b7648cec9a8c30875027079102da2fd7c1
    role: context
  - path: reviews/evidence/20261014-fogacin/primary-observations.json
    sha256: c2664f2462983a403b98360823466f3dab9668ba9a321cba7fa4f48015a208cd
    role: context
  - path: reviews/evidence/20261014-fogacin/regression-final.log
    sha256: 52097e7e40c97373f6d33c8d41dff4813cedbc9ae6a66e6c66129d56779b1ebb
    role: context
  - path: reviews/evidence/20261014-fogacin/regression.log
    sha256: 6a8e07742cd5f05bbfc2c2d8eedd21c1e9bf6b008b4e48005df3a5bc370dafdf
    role: context
  - path: reviews/evidence/20261014-fogacin/remediation-checks.json
    sha256: f7d0b8ab369641027c951a5437dcc2d4306abdca99bd3c0b09320e271afea012
    role: context
  - path: reviews/evidence/20261014-fogacin/render.log
    sha256: 0fa955c283693392d54d1f3a948782c946130b110b7d122b54d24752d44583b4
    role: context
  - path: reviews/evidence/20261014-fogacin/replay-inputs.json
    sha256: 2a2bedff98aa728401bc5de48cb73579d7223b7bf1e59a57f26c6bf623121574
    role: context
  - path: reviews/evidence/20261014-fogacin/reproduction.log
    sha256: 09ea1c9d8fc0b6e788d9641568c46b0addcd7e1fe17bd98439f0232f02607d42
    role: context
  - path: reviews/evidence/20261014-fogacin/seed-dry.log
    sha256: 1e21022b634eb9244ded56fff873c445a64269f52e12c89026316df7d03c8aee
    role: context
  - path: reviews/evidence/20261014-fogacin/source-inspection.json
    sha256: 032244ccd462c161ba22b1095c3790bebefb5568a0e7129f179128566f898017
    role: context
  - path: reviews/evidence/20261014-fogacin/sources.json
    sha256: 031515fcfff022852dd301a737a98cef8fabdc72bf9b6a8446c6d480b2ab6dc0
    role: context
  - path: reviews/evidence/20261014-fogacin/strict-final.log
    sha256: ebb1d51f14d50ce7a8d6224f7dd9ae63cb559484d5964430980d905082581241
    role: context
  - path: reviews/evidence/20261014-fogacin/strict.log
    sha256: c915369a707b1d14f66296f135f1f7bf69a2dc976fa5959eb59c249b9d3294b7
    role: context
  - path: reviews/structured/20261014T020900Z-fogacin/review.yaml
    sha256: b8520bb6f4be7089a02d837fc672dc01b34926ece4eb71ad642413e5cf48baf0
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
  - path: tests/test_fogacin_locus_scope.py
    sha256: 7562d539700576ad848b548699f6d4c7d7dfe4ad7a1c04d3b4db1bc8457ef129
    role: context
  - path: tests/test_fogacin_review_archive.py
    sha256: 5f359359f994f795454aacc854ef530e33d0b35f729ae64e73b6c78d54952f4f
    role: context
  - path: uv.lock
    sha256: c62a5739e3ffeb12cc57b3bf12a31dcf9cdfbf00b417f4ba3a801d51ef9efbe3
    role: context
targets:
- target_id: naturalproductmech:mibig-a4fac30c3f
  path: data/natural_products/polyketides/fogacin.yaml
  label: fogacin
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
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Implemented full-row-pinned claim-specific citation routing
scope:
  description: Entire exact owner and resolved mechanism, source identifiers and bounded
    primary evidence.
  selection: Next exact owner in3115-record campaign; the other same-label owner is
    assessed separately.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-a4fac30c3f
checks:
- check_id: chemistry
  name: chemistry
  status: passed
  required: true
  exit_code: 0
  command: /private/tmp/npmech-rdkit-2026.03.5/bin/python reviews/evidence/20261014-fogacin/inspect_sources.py
    --output reviews/evidence/20261014-fogacin/source-inspection.json
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  summary: Executed successfully within declared scope.
  scope_note: 2026-10-14T02:06:50.327253Z..2026-10-14T02:06:53.561596Z; checks.json
    and log SHA256 8d6205343d87c16f1a7bde34b7cf42b7648cec9a8c30875027079102da2fd7c1
    Baseline observation; fresh corrective checks below.
- check_id: strict
  name: strict
  status: passed
  required: true
  exit_code: 0
  command: just validate-strict data/natural_products/polyketides/fogacin-2.yaml data/natural_products/polyketides/fogacin.yaml
    --out /private/tmp/npmech-fogacin-review-TbRFcN/strict.tsv
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  summary: Executed successfully within declared scope.
  scope_note: 2026-10-14T01:59:25.531715Z..2026-10-14T01:59:28.900257Z; checks.json
    and log SHA256 c915369a707b1d14f66296f135f1f7bf69a2dc976fa5959eb59c249b9d3294b7
    Baseline observation; fresh corrective checks below.
- check_id: labels
  name: labels
  status: passed
  required: true
  exit_code: 0
  command: just validate-products
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  summary: 499 nonblocking label warnings and4649 no-adapter skips.
  scope_note: 2026-10-14T01:59:28.985837Z..2026-10-14T02:01:25.253281Z; checks.json
    and log SHA256 19a4f6cca7894851de23ee2062f52d29b32def53c7b4f59edbc6c45ec4ce9828
    Baseline observation; fresh corrective checks below.
- check_id: local-search
  name: local-search
  status: passed
  required: true
  exit_code: 0
  command: rg --no-ignore --hidden -l -i 'WGMNUJNCGZFZPD|QHMHMPAPKQFGRV|fogacin|BGC0002021|BGC0000248'
    curation conf reviews .claude data/raw/mibig_compounds.tsv data/raw/lotus_occurrences.tsv
    data/raw/chebi_structures.tsv data/raw/antibioticmech_inchikeys.tsv
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  summary: Executed successfully within declared scope.
  scope_note: 2026-10-14T02:01:43.623535Z..2026-10-14T02:01:43.739680Z; checks.json
    and log SHA256 47fdb954f1d8dae2a9b8c25b0112d3c8b3d9af6e09a9ce14290b843aefe05a2b
    Baseline observation; fresh corrective checks below.
- check_id: qc
  name: Exact-base native QC
  status: unavailable
  required: true
  command: just qc (reused exact-base merge CI)
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - base-qc
  summary: Full corrected-branch QC has not completed at assessment time; baseline
    QC does not cover the native correction. Final CI must pass before merge.
- check_id: primary-closure
  name: Exact-product primary scientific closure
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  summary: Primary structural assignments and exact wild-type production remain unresolved;
    no full-text access bypass.
  scope_note: ' Baseline observation; fresh corrective checks below.'
- check_id: corrective-regression-final
  name: Corrective regression-final
  status: passed
  required: true
  command: uv run pytest -q tests/test_fogacin_locus_scope.py tests/test_fogacin_review_archive.py
    tests/test_mibig_locus_evidence_overrides.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - remediation
  summary: Actual successful scoped execution; native status is not promoted.
  scope_note: 2026-10-14T02:14:58.835820Z..2026-10-14T02:15:02.980515Z; SHA256 52097e7e40c97373f6d33c8d41dff4813cedbc9ae6a66e6c66129d56779b1ebb
- check_id: corrective-strict-final
  name: Corrective strict-final
  status: passed
  required: true
  command: just validate-strict data/natural_products/polyketides/fogacin.yaml data/natural_products/polyketides/fogacin-2.yaml
    --out /private/tmp/npmech-fogacin-review-TbRFcN/strict-final.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - remediation
  summary: Actual successful scoped execution; native status is not promoted.
  scope_note: 2026-10-14T02:13:44.815190Z..2026-10-14T02:13:50.865902Z; SHA256 ebb1d51f14d50ce7a8d6224f7dd9ae63cb559484d5964430980d905082581241
- check_id: corrective-reproduction
  name: Corrective reproduction
  status: passed
  required: true
  command: just verify-reproduction
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - remediation
  summary: Actual successful scoped execution; native status is not promoted.
  scope_note: 2026-10-14T02:13:48.997714Z..2026-10-14T02:16:20.153093Z; SHA256 09ea1c9d8fc0b6e788d9641568c46b0addcd7e1fe17bd98439f0232f02607d42
- check_id: corrective-portable-replay
  name: Corrective portable-replay
  status: passed
  required: true
  command: /private/tmp/npmech-rdkit-2026.03.5/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/reviews/evidence/20261014-fogacin/inspect_sources.py
    --output /private/tmp/npmech-fogacin-review-TbRFcN/portable-replay.json
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - remediation
  summary: Actual successful scoped execution; native status is not promoted.
  scope_note: 2026-10-14T02:15:00.144057Z..2026-10-14T02:15:04.238539Z; SHA256 8d6205343d87c16f1a7bde34b7cf42b7648cec9a8c30875027079102da2fd7c1
- check_id: corrective-render
  name: Corrective render
  status: passed
  required: true
  command: just render
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - remediation
  summary: Actual successful scoped execution; native status is not promoted.
  scope_note: 2026-10-14T02:13:25.841432Z..2026-10-14T02:14:27.040961Z; SHA256 0fa955c283693392d54d1f3a948782c946130b110b7d122b54d24752d44583b4
- check_id: corrective-lint-final
  name: Corrective lint-final
  status: passed
  required: true
  command: uv run ruff check reviews/evidence/20261014-fogacin/inspect_sources.py
    tests/test_fogacin_review_archive.py tests/test_fogacin_locus_scope.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - remediation
  summary: Actual successful scoped execution; native status is not promoted.
  scope_note: 2026-10-14T02:13:06.785082Z..2026-10-14T02:13:06.877129Z; SHA256 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/polyketides/fogacin.yaml
  summary: Entire corrected raw/resolved owner re-read; chemical identity, source
    assertion and SEEDED remain. One guarded seed history event records the table-driven
    correction.
  locator: Working-tree successor at archived base54f772c74
  accessed_at: '2026-10-14T02:17:55.429775Z'
  support: supports
- evidence_id: chemistry
  kind: validation
  reference: reviews/evidence/20261014-fogacin/source-inspection.json
  summary: Stored SMILES, InChI and key round-trip. C16H16O6 has two specified centers;
    C16H18O6 has two specified and one undefined center. These are different hydrogenation
    states, not interchangeable stereochemical resolutions.
  locator: chemistry; pinned RDKit2026.03.5, atom indices are graph indices not paper
    numbering
  accessed_at: '2026-10-14T02:09:00.303548Z'
  support: supports
  snapshot_sha256: 032244ccd462c161ba22b1095c3790bebefb5568a0e7129f179128566f898017
- evidence_id: inventory
  kind: record_content
  reference: reviews/evidence/20261014-fogacin/source-inspection.json
  summary: Exact-key full scans find one MIBiG and one NPClassifier row per owner,
    no ChEBI structure/origin or AntibioticMech match. Only WGM has two LOTUS rows
    and a PubChem no-assay-data sentinel, not an activity observation.
  locator: inventories; ChEBI origins joined through exact-key ChEBI IDs; bounded
    committed inventory scope
  accessed_at: '2026-10-14T02:09:00.303778Z'
  support: supports
  snapshot_sha256: 032244ccd462c161ba22b1095c3790bebefb5568a0e7129f179128566f898017
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000248.5/annotations.json
  summary: Active version5, compound2, native SMILES, DSM40737 label, species taxon29301
    and JAKQYH010000014.1 bounds match. Heterologous expression is entry-level; legacy
    citation10206788 differs from pathway citation37989784.
  locator: Entire versioned JSON; quality is not a truth signal
  accessed_at: '2026-10-14T02:09:00.303979Z'
  support: supports
  snapshot_sha256: 4f4ef8b412947d43b953ac465dfb88d9a285022d982f8eefa9feebad8966b510
- evidence_id: taxonomy
  kind: database
  reference: reviews/evidence/20261014-fogacin/source-inspection.json
  summary: NCBI512565 is strain431;29301 is S.arenae species, not DSM40737 strain
    rank. GenBank source qualifiers preserve431/NBRC102363 and DSM40737 respectively.
    Occurrence IDs1866/1883 are species/genus, independently matching both Wikidata
    P685 values.
  locator: taxonomy, source features and wikidata; sequence annotations do not prove
    protein function
  accessed_at: '2026-10-14T02:09:00.304101Z'
  support: supports
  snapshot_sha256: 032244ccd462c161ba22b1095c3790bebefb5568a0e7129f179128566f898017
- evidence_id: primary
  kind: primary_source
  reference: PMID:10206788
  summary: The1999 abstract concerns naphthocyclinones and minimal-PKS mutactin/dehydromutactin
    experiments; it does not establish exact fogacin production.
  locator: Complete PubMed abstract and PMID/DOI mapping; no full-text adjudication
  accessed_at: '2026-10-14T02:09:00.304303Z'
  support: context_only
  snapshot_sha256: 2a05345ccd071045a85d544bf31a09bb4ee38dfb6cafcc835249ff4c72b23c5f
- evidence_id: experiment
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/37989784/
  summary: Abstract and public Figure2 caption distinguish intact ncn-cluster expression
    from fogacin accumulation in S.albus carrying an ncnN deletion. Complementation
    restores naphthocyclinone production.
  locator: Previously inspected public abstract and Figure2B web caption; the old
    hash attested abstracts-extra.xml only, not this caption. No raw caption snapshot
    is archived. Details in primary-observations.json.
  accessed_at: '2026-10-14T02:17:55.429790Z'
  support: refutes
- evidence_id: search
  kind: search
  reference: reviews/evidence/20261014-fogacin/local-search.log
  summary: Hidden/ignored-inclusive search and prior68-bundle checkpoint found no
    prior exact-owner canonical review. Compressed contents excluded.
  locator: Command and log in checks.json
  accessed_at: '2026-10-14T02:09:00.304592Z'
  support: context_only
  search_scope: curation,conf,reviews,.claude and named MIBiG/LOTUS/ChEBI/AntibioticMech
    raw TSVs; exact keys, fogacin labels and BGCs; ignored/hidden included
  snapshot_sha256: 47fdb954f1d8dae2a9b8c25b0112d3c8b3d9af6e09a9ce14290b843aefe05a2b
- evidence_id: adapter
  kind: database
  reference: reviews/evidence/20261014-fogacin/imodulondb.log
  summary: The28-dataset inventory has no matching A.missouriensis or S.arenae dataset.
    Other Streptomyces datasets are not substitutes; no component query applies.
  locator: Full structured adapter inventory
  accessed_at: '2026-10-14T02:09:00.304695Z'
  support: context_only
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: base-qc
  kind: validation
  reference: https://github.com/CultureBotAI/NaturalProductMech/actions/runs/38497123596
  summary: Historical baseline-only full QC, not QC of this corrected native record.
    Fresh scoped checks and reproduction are retained separately; final full PR QC
    is still pending at this observation.
  locator: Merge QC; log SHA256e1896e5e78f1e6cb44e4939a950279b0d4f34ad33c0047f0914d9072b2315c47
  accessed_at: '2026-10-14T02:09:00.304780Z'
  support: supports
- evidence_id: remediation
  kind: validation
  reference: reviews/evidence/20261014-fogacin/remediation-checks.json
  locator: Actual commands, UTC times, exit codes and retained log hashes
  accessed_at: '2026-10-14T02:17:55.429833Z'
  support: supports
  snapshot_sha256: f7d0b8ab369641027c951a5437dcc2d4306abdca99bd3c0b09320e271afea012
  summary: 94 focused tests, strict validation, guarded canary, rendering and full
    corpus reproduction passed. Portable replay from outside the checkout equals the
    baseline output.
- evidence_id: caption-provenance
  kind: record_content
  reference: reviews/evidence/20261014-fogacin/primary-observations.json
  locator: Separate web-caption observation, abstract-only digest and later HTTP203
    challenge; raw article not redistributed
  accessed_at: '2026-10-14T02:17:55.430050Z'
  support: supports
  snapshot_sha256: c2664f2462983a403b98360823466f3dab9668ba9a321cba7fa4f48015a208cd
  summary: Corrects the prior implication that abstract XML also attested the caption.
    This file hashes reviewer observations, not a captured caption payload.
- evidence_id: delta
  kind: validation
  reference: reviews/evidence/20261014-fogacin/native-delta.json
  locator: All baseline-tracked owners/components/raw inputs/prior review files compared
    with historical Git bytes
  accessed_at: '2026-10-14T02:17:55.430179Z'
  support: supports
  snapshot_sha256: d1bbd9a92000626fb728b916d1ce1f5502d16e6448a7ff66b31050e92bef3ba9
  summary: Only fogacin.yaml differs among3115 owners;3114 other owners,243 components,
    raw inputs and68 prior bundles are byte-identical.
assessments:
- assessment_id: encoding
  area: consistency
  topic: Structure and encoded stereochemical resolution
  outcome: supported
  summary: Stored chemistry and stereo_complete agree; no primary absolute-configuration
    certification.
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - owner
  - chemistry
  - mibig
- assessment_id: identity
  area: identity
  topic: Primary structure and same-name boundary
  outcome: unknown
  summary: Two distinct graphs are preserved. Same label does not establish equivalence
    or select a corrected identity.
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - chemistry
  - mibig
  - primary
- assessment_id: grounding
  area: grounding
  topic: Exact pinned joins
  outcome: supported
  summary: Minted identity is consistent with no pinned exact-key ChEBI match; no
    name-based transfer.
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - inventory
- assessment_id: facets
  area: representation
  topic: Computed classification and asserted taxonomic facets
  outcome: supported
  summary: POLYKETIDES/classifier model provenance, asserted PKS and actinobacterial
    facets reproduce. Model subclass output is not asserted chemistry.
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - inventory
  - taxonomy
- assessment_id: origin
  area: scope
  topic: Producer and experimental context
  outcome: unknown
  summary: SOURCE_ASSERTION is retained. Neither native exact-product production nor
    ENGINEERED molecular origin is inferred from heterologous expression.
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - owner
  - primary
  - taxonomy
- assessment_id: cluster
  area: evidence
  topic: Compound-specific locus grade
  outcome: supported
  summary: Only the exact compound method is withdrawn. CLUSTER_UNSTATED and separate
    CURATOR_INFERENCE preserve the mutant context, while the original database assertion
    remains.
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - owner
  - experiment
  - remediation
- assessment_id: optional
  area: graph
  topic: Optional mechanisms and activities
  outcome: not_applicable
  summary: No native pathways, targets, activities, graph components or datasets to
    audit. Optional absence is not a defect.
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - owner
  - inventory
  - adapter
- assessment_id: caption-method
  area: provenance
  topic: Web caption versus abstract-only hash
  outcome: supported
  summary: Successor explicitly separates the inspected web observation from the efetch
    payload and subsequent browser challenge.
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  evidence_ids:
  - caption-provenance
findings:
- finding_id: locus-scope
  issue_key: fogacin-bgc0000248-intact-locus-grade
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Entry-level method overgrades the exact fogacin locus claim
  description: The recorded intact deposited locus is CLUSTER_DEMONSTRATED without
    the mutant experimental qualification. Withdraw applicability of the inherited
    method for this exact source compound while preserving the original database assertion
    and separately cited experiment context.
  target_ids:
  - naturalproductmech:mibig-a4fac30c3f
  field_paths:
  - biosynthetic_gene_clusters[0].link_evidence_basis
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  evidence_ids:
  - owner
  - experiment
  - remediation
  - delta
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Source-pinned exact-compound locus-method withdrawal
  rule_id: docs/CURATION.md:cluster-grade-versus-producer-grade
  native_severity: major
  normalization_reason: Compound-specific experimental scope inflation; not a confirmed
    replacement structure or denial of all natural production.
  disposition_reason: 'Source-pinned exact-compound WITHDRAW, regenerated owner and
    sibling/drift regressions resolve this bounded grade inflation. This does not
    resolve the independent identity and production uncertainties in #963.'
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261014T020900Z-fogacin
    finding_id: locus-scope
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/962
actions: []
limitations:
- Primary structure/hydrogenation and absolute stereochemistry remain unadjudicated;
  no automatic merge or replacement.
- PMC10697411 returned a browser/CAPTCHA challenge; Wiley2019 was unavailable to the
  web tool; Nature2006 PDF redirected to HTML with cookies_not_supported. No alternate
  full-text retrieval after these stops.
- The1999 paper was assessed only through its abstract. PubMed2023 public caption
  is not full-text or figure-image inspection.
- NCBITaxon29301 is species-ranked; DSM40737 is source strain context. NCBITaxon512565
  is strain-ranked.
- No exhaustive live chemical-registry search. Negative joins are limited to the scanned
  pinned inventories.
- No native status promotion, curation event or optional graph fabrication follows
  from this review.
- Corrected-branch full QC is pending at assessment time and must pass before merge;
  scoped regression/reproduction success is not a substitute.
- The original experiment evidence attached an abstract-only digest to a caption observation.
  The successor removes that misleading implication. A later direct PubMed capture
  returned a browser challenge; no alternate retrieval followed.
- Source base54f772c74 is retained by annotated tag review-base/fogacin-20261014;
  fetch this tag in restricted clones. Working-tree input hashes attest the corrected
  bytes, not the unchanged historical tree.
tags:
- fogacin
- record-review-campaign
- partial
- experimental-scope
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261014T020900Z-fogacin
  relationship: Resolves the bounded locus-grade finding and corrects caption provenance
    without rewriting the original observation.
links:
- https://github.com/CultureBotAI/NaturalProductMech/issues/962
- https://github.com/CultureBotAI/NaturalProductMech/issues/963
- https://github.com/CultureBotAI/NaturalProductMech/issues/965
notes:
- Issue965 is corrected through successor provenance, not by rewriting the initial
  review. Issue963 remains open.
- Initial focused/lint invocations were blocked by uv cache permissions and passed
  on authorized reruns; both attempts are retained. The unsaved initial fogacin draft
  used invalid assessment outcome concerning; canonical validation rejected it, and
  concern was used before initial persistence.
```
