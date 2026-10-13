# capsular-polysaccharide-2: deposited-context disposition

- Review: 20261013T211427Z-capsular-polysaccharide-2-scoped-disposition
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T21:13:02.090353Z
- Finished UTC: 2026-10-13T21:14:27.714177Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Missing deposited context resolved; exact-product identity remains open and visibly qualified.

## Scope And Provenance

One exact owner; scoped finding disposition, not a second full assessment.

Selection: User-authorized issue remediation and publication.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b87e2fa3e2acc7896755a7c4eaa09d48fe0159e8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-6a3f1200b4 | data/natural_products/carbohydrates/capsular-polysaccharide-2.yaml | generated | capsular polysaccharide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| publish-focused | passed | True | naturalproductmech:mibig-6a3f1200b4 | Actual execution 2026-10-13T21:09:44.915797Z to 2026-10-13T21:09:46.690564Z, exit 0. Full QC is deterministic validation, not scientific completion. |
| publish-strict | passed | True | naturalproductmech:mibig-6a3f1200b4 | Actual execution 2026-10-13T21:10:26.056669Z to 2026-10-13T21:10:29.776317Z, exit 0. Full QC is deterministic validation, not scientific completion. |
| publish-scope | passed | True | naturalproductmech:mibig-6a3f1200b4 | Actual execution 2026-10-13T21:10:13.855373Z to 2026-10-13T21:10:15.806947Z, exit 0. Full QC is deterministic validation, not scientific completion. |
| Outstanding exact-product primary evidence | unavailable | True | naturalproductmech:mibig-6a3f1200b4 | All predecessor access limitations remain; no new retrieval or exact-product adjudication in this disposition. |

## Scientific And Domain Assessments

### Deposited strain/isolate and serotype scope

provenance: supported. Targets: naturalproductmech:mibig-6a3f1200b4.

Exact qualifiers agree with the deposited source context; no biological scope or evidence-grade change.

### Remaining exact-product uncertainty

identity: concern. Targets: naturalproductmech:mibig-6a3f1200b4.

OPEN qualification is mitigation, not identity adjudication. Full-owner assessment and primary access limits remain partial.

## Findings

### F1: Exact capsule-product assignment is unsupported across deposited serotypes

blocker / open / confirmed; issue key: capsular-polysaccharide-2-exact-product-assignment.

Five deposited K5/K20/K54 loci share one finite, stereochemically undefined six-ring graph. PubChem names that graph as K15. The inspected study abstract concerns genotyping and clinical/serum-resistance comparisons, not exact product structural assignment. Registry names/MeSH associations are name-based and are not independent chemical certification. Exact PubChem graph agreement is verified; deleting its xref alone would not repair the biological assignment. The confirmed defect is unsupported exact-product assignment across the recorded contexts, not an experimentally established replacement structure.

Disposition: Mitigated by a cited OPEN discussion. The per-locus exact chemical product and representation boundary remain unadjudicated; no replacement structure or broader equivalence is inferred.

### F2: Deposited strain and serotype qualifications are missing

minor / resolved / confirmed; issue key: capsular-polysaccharide-2-deposited-strain-context.

5 source qualifiers are available but not explicitly carried into producer strain/evidence context.

Disposition: Exact deposited strain/isolate qualifiers and serotype rationale are now preserved through pinned curation rows and guarded generation; all narrow invariants pass. This resolves only missing context, not chemical identity.

## Recommended Actions And Acceptance Checks

### A1

Preserve an OPEN identity qualification, then adjudicate exact locus-to-product and occurrence assignments from accessible primary chemistry before migration; do not rename all entries to the registry serotype.

- Per-source structure and polymer/form boundary justified by inspected primary chemistry.
- Use a supported maintained migration/exclusion path, preserve provenance, and pass strict validation, reproduction and full QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-genbank | https://www.ncbi.nlm.nih.gov/nuccore/; GBSeq accession-version; source feature strain/isolate, serotype and db_xref qualifiers | supports | AB289645.1: Kauffmann E5051, serotype K5; AB289646.1: NTUH-K9534, serotype K5; AB289647.1: 889/50, serotype K20; AB289648.1: NTUH-KP13, serotype K20; AB289650.1: NTUH-KP35, serotype K54 |
| E-matrix | reviews/evidence/20261013-capsular/manifest.json; matrix.json | supports | Exact-source mapping, complete raw-row SHA256 pins and deposited context; no taxon or product inference. |
| E-pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/3083199; RecordTitle and MeSH/Synonyms; no identity inferred from names alone | context_only | Names and Identifiers record title associates this graph with K15; MeSH names explicitly use name-based association, not chemical equivalence certification. |
| E-chemistry | reviews/evidence/20261013-capsular/manifest.json; data/natural_products/carbohydrates/capsular-polysaccharide-2.yaml | supports | RDKit 2026.03.5 reproduces stored Standard InChI and key and matches PubChem. Formula C36H60O32; 0 assigned and 30 undefined centers; stereo_complete flag is computationally consistent. Finite graph, not a variable-degree polymer; this does not validate its biological assignment. |
| E-literature | PMID:17599305; Europe PMC result id 17599305 | partial | Five deposited K5/K20/K54 loci share one finite, stereochemically undefined six-ring graph. PubChem names that graph as K15. The inspected study abstract concerns genotyping and clinical/serum-resistance comparisons, not exact product structural assignment. Metadata and abstract only for this cited paper; full text was denied and was not retrieved through an alternate route. |
| E-current | data/natural_products/carbohydrates/capsular-polysaccharide-2.yaml | supports | Entire current owner reread: exact deposited qualifiers and cited OPEN identity discussion added; original source assertions, keys, grades and SEEDED status unchanged. |
| E-prior | reviews/structured/20261013T210832Z-capsular-polysaccharide-2/review.yaml | supports | Immutable partial full-owner assessment, including scientific findings and unavailable source checks. |
| E-strains | curation/mibig_producer_strains.tsv | supports | Seventeen exact-row-pinned GenBank qualifications, with serotypes in rationale and isolate 72-14676 explicitly marked as isolate; no taxon-ID reassignment. |
| E-scope | /private/tmp/npmech-capsular-publish-7cKqTV/scope-audit.json | supports | All 3115 owners, 243 components and 42 preexisting pairs checked: only three selected owners changed, with limited qualifiers, OPEN discussions and appended history. |
| E-publish-focused | /private/tmp/npmech-capsular-resume-6vn9Sp/publish-focused.log | supports | Actual execution 2026-10-13T21:09:44.915797Z to 2026-10-13T21:09:46.690564Z, exit 0. Full QC is deterministic validation, not scientific completion. |
| E-publish-strict | /private/tmp/npmech-capsular-resume-6vn9Sp/publish-strict.log | supports | Actual execution 2026-10-13T21:10:26.056669Z to 2026-10-13T21:10:29.776317Z, exit 0. Full QC is deterministic validation, not scientific completion. |
| E-publish-scope | /private/tmp/npmech-capsular-resume-6vn9Sp/publish-scope.log | supports | Actual execution 2026-10-13T21:10:13.855373Z to 2026-10-13T21:10:15.806947Z, exit 0. Full QC is deterministic validation, not scientific completion. |

## Limits And Additional Notes

- Scoped disposition only; no new owner coverage or native REVIEWED promotion.
- All predecessor primary and authority access limits persist. No additional primary retrieval or access bypass.
- Source state is working_tree: current input bytes were inspected and archived, not claimed to exist at the base commit.
- Full QC is still running at authoring; canonical checks and final CI follow. An initial local QC lint failure was corrected before restarting. Only the recorded focused tests, strict validation and object-level scope audit are claimed here.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T211427Z-capsular-polysaccharide-2-scoped-disposition
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'capsular-polysaccharide-2: deposited-context disposition'
started_at: '2026-10-13T21:13:02.090353Z'
finished_at: '2026-10-13T21:14:27.714177Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Implementing assistant performing a separate adversarial pass;
    not independent human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Missing deposited context resolved; exact-product identity remains open and
  visibly qualified.
source:
  git_revision: b87e2fa3e2acc7896755a7c4eaa09d48fe0159e8
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
    sha256: f3f808ad1e58d79947aa82ecf1272e465cfbef57e5a4cd646731af23bb48ce75
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: a1eb14fec4a7cee0c2fc25c43091e75af24ae62c44c4f7659ed7aedf0e6a0e6c
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 1cdea1a2338304087cb64ee0eedac76e6e0adb97babed2c64d808eda4835225c
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: ac01b66bb97bc2c4e16558227fed641e28daa3c5926a09e213e98c38a09856a2
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/carbohydrates/capsular-polysaccharide-2.yaml
    sha256: 615b844a9c7d6124382cb3729dd8b67d70d4c4e21afee3000b0e891f16687685
    role: target
  - path: data/natural_products/carbohydrates/capsular-polysaccharide-3.yaml
    sha256: c5927554e070322ff10577948c0d513fad2348d0983d851eba037224bcfe3a47
    role: context
  - path: data/natural_products/unclassified/capsular-polysaccharide.yaml
    sha256: 310d06bd8576f8abae494cdc781e87c15ed85006329b881bded473988e51c814
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
    sha256: aba5606d7e5e7c2887e66294655db26a10e853a42893d71aab8f015dc9b91c71
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/run_qc.py
    sha256: ff44ed3e40a9b3582eb84e38a81301745ae80d16445756d09a7efb2a480b1abb
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 21fd298fb528f1179286125bc3d12f36ae72ca6c1e0f783cf94dcace2648f292
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: 6026ddca19f0989d499b1681f7724fbab23918de8d3957750b49bbfe1a9c0bff
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
  - path: tests/test_capsular_curation.py
    sha256: 33fc880aa197ac90693ae75a59e79a93bbf22e65d544b1762616fdc54fa85001
    role: context
  - path: uv.lock
    sha256: c62a5739e3ffeb12cc57b3bf12a31dcf9cdfbf00b417f4ba3a801d51ef9efbe3
    role: context
targets:
- target_id: naturalproductmech:mibig-6a3f1200b4
  path: data/natural_products/carbohydrates/capsular-polysaccharide-2.yaml
  label: capsular polysaccharide
  record_class: NaturalProductRecord
  kind: generated
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
    path: curation/mibig_claim_references.tsv
    role: Implemented pinned claim-specific citation routing
scope:
  description: One exact owner; scoped finding disposition, not a second full assessment.
  selection: User-authorized issue remediation and publication.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-6a3f1200b4
checks:
- check_id: publish-focused
  name: publish-focused
  required: true
  status: passed
  command: uv run pytest -q tests/test_capsular_curation.py tests/test_producer_strains.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-6a3f1200b4
  evidence_ids:
  - E-publish-focused
  summary: Actual execution 2026-10-13T21:09:44.915797Z to 2026-10-13T21:09:46.690564Z,
    exit 0. Full QC is deterministic validation, not scientific completion.
- check_id: publish-strict
  name: publish-strict
  required: true
  status: passed
  command: just validate-strict data/natural_products/carbohydrates/capsular-polysaccharide-2.yaml
    data/natural_products/carbohydrates/capsular-polysaccharide-3.yaml data/natural_products/unclassified/capsular-polysaccharide.yaml
    --out /private/tmp/npmech-capsular-publish-7cKqTV/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-6a3f1200b4
  evidence_ids:
  - E-publish-strict
  summary: Actual execution 2026-10-13T21:10:26.056669Z to 2026-10-13T21:10:29.776317Z,
    exit 0. Full QC is deterministic validation, not scientific completion.
- check_id: publish-scope
  name: publish-scope
  required: true
  status: passed
  command: uv run python /private/tmp/npmech-capsular-publish-7cKqTV/scope_audit.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-6a3f1200b4
  evidence_ids:
  - E-publish-scope
  summary: Actual execution 2026-10-13T21:10:13.855373Z to 2026-10-13T21:10:15.806947Z,
    exit 0. Full QC is deterministic validation, not scientific completion.
- check_id: primary-remaining
  name: Outstanding exact-product primary evidence
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-6a3f1200b4
  summary: All predecessor access limitations remain; no new retrieval or exact-product
    adjudication in this disposition.
evidence:
- evidence_id: E-genbank
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/
  accessed_at: '2026-10-13T19:48:10.386471Z'
  support: supports
  summary: 'AB289645.1: Kauffmann E5051, serotype K5; AB289646.1: NTUH-K9534, serotype
    K5; AB289647.1: 889/50, serotype K20; AB289648.1: NTUH-KP13, serotype K20; AB289650.1:
    NTUH-KP35, serotype K54'
  snapshot_sha256: d48604e4364f1f43d70fe261e4ce7f52a45acb1bb7926d771aae79f1f261c54f
  locator: GBSeq accession-version; source feature strain/isolate, serotype and db_xref
    qualifiers
- evidence_id: E-matrix
  kind: validation
  reference: reviews/evidence/20261013-capsular/manifest.json
  accessed_at: '2026-10-13T21:08:32.680917Z'
  support: supports
  summary: Exact-source mapping, complete raw-row SHA256 pins and deposited context;
    no taxon or product inference.
  snapshot_sha256: 6f79ff99a15f8b25f3df3dc09b9993d6222933129d982e9dca01d9cf0727a83f
  locator: matrix.json
- evidence_id: E-pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/3083199
  accessed_at: '2026-10-13T20:59:07.129627Z'
  support: context_only
  summary: Names and Identifiers record title associates this graph with K15; MeSH
    names explicitly use name-based association, not chemical equivalence certification.
  snapshot_sha256: ccfe74f105545b6063849ca88f2a980136e7bcb528497f0b1baafcec6977a6ea
  locator: RecordTitle and MeSH/Synonyms; no identity inferred from names alone
- evidence_id: E-chemistry
  kind: validation
  reference: reviews/evidence/20261013-capsular/manifest.json
  accessed_at: '2026-10-13T21:08:32.681915Z'
  support: supports
  summary: RDKit 2026.03.5 reproduces stored Standard InChI and key and matches PubChem.
    Formula C36H60O32; 0 assigned and 30 undefined centers; stereo_complete flag is
    computationally consistent. Finite graph, not a variable-degree polymer; this
    does not validate its biological assignment.
  snapshot_sha256: ced3910a68670247d484823025f55eb213ba7c071b2a499f28d008ac0ef00095
  locator: data/natural_products/carbohydrates/capsular-polysaccharide-2.yaml
- evidence_id: E-literature
  kind: primary_source
  reference: PMID:17599305
  accessed_at: '2026-10-13T19:47:09.197319Z'
  support: partial
  summary: Five deposited K5/K20/K54 loci share one finite, stereochemically undefined
    six-ring graph. PubChem names that graph as K15. The inspected study abstract
    concerns genotyping and clinical/serum-resistance comparisons, not exact product
    structural assignment. Metadata and abstract only for this cited paper; full text
    was denied and was not retrieved through an alternate route.
  snapshot_sha256: 1f6a507b2df32cd81f07fe2829af7f07f1a6c240dae48d0c218f55e359b373a1
  locator: Europe PMC result id 17599305
- evidence_id: E-current
  kind: record_content
  reference: data/natural_products/carbohydrates/capsular-polysaccharide-2.yaml
  accessed_at: '2026-10-13T21:14:27.710531Z'
  support: supports
  summary: 'Entire current owner reread: exact deposited qualifiers and cited OPEN
    identity discussion added; original source assertions, keys, grades and SEEDED
    status unchanged.'
  snapshot_sha256: 615b844a9c7d6124382cb3729dd8b67d70d4c4e21afee3000b0e891f16687685
- evidence_id: E-prior
  kind: prior_review
  reference: reviews/structured/20261013T210832Z-capsular-polysaccharide-2/review.yaml
  accessed_at: '2026-10-13T21:14:27.710964Z'
  support: supports
  summary: Immutable partial full-owner assessment, including scientific findings
    and unavailable source checks.
  snapshot_sha256: 20fa5a8652239bfc8ef460543f4dde0957dff1713a21f3b60867717fe6b1d0ef
- evidence_id: E-strains
  kind: record_content
  reference: curation/mibig_producer_strains.tsv
  accessed_at: '2026-10-13T21:14:27.711170Z'
  support: supports
  summary: Seventeen exact-row-pinned GenBank qualifications, with serotypes in rationale
    and isolate 72-14676 explicitly marked as isolate; no taxon-ID reassignment.
  snapshot_sha256: 1cdea1a2338304087cb64ee0eedac76e6e0adb97babed2c64d808eda4835225c
- evidence_id: E-scope
  kind: validation
  reference: /private/tmp/npmech-capsular-publish-7cKqTV/scope-audit.json
  accessed_at: '2026-10-13T21:14:27.711328Z'
  support: supports
  summary: 'All 3115 owners, 243 components and 42 preexisting pairs checked: only
    three selected owners changed, with limited qualifiers, OPEN discussions and appended
    history.'
  snapshot_sha256: 3d8b5114b9a194409a96d413173c08b079b535b108b8d5c3a1a46b5bc7ebe63d
- evidence_id: E-publish-focused
  kind: validation
  reference: /private/tmp/npmech-capsular-resume-6vn9Sp/publish-focused.log
  accessed_at: '2026-10-13T21:14:27.712435Z'
  support: supports
  summary: Actual execution 2026-10-13T21:09:44.915797Z to 2026-10-13T21:09:46.690564Z,
    exit 0. Full QC is deterministic validation, not scientific completion.
  snapshot_sha256: 69641c993313ce2ba07b76ec74753dfb56dd5c9c445e13219b5bc03139c22332
- evidence_id: E-publish-strict
  kind: validation
  reference: /private/tmp/npmech-capsular-resume-6vn9Sp/publish-strict.log
  accessed_at: '2026-10-13T21:14:27.713418Z'
  support: supports
  summary: Actual execution 2026-10-13T21:10:26.056669Z to 2026-10-13T21:10:29.776317Z,
    exit 0. Full QC is deterministic validation, not scientific completion.
  snapshot_sha256: 28d92bc566c696560d912fb7a73ba8b896948acd710951b7f2ac54f206ade90e
- evidence_id: E-publish-scope
  kind: validation
  reference: /private/tmp/npmech-capsular-resume-6vn9Sp/publish-scope.log
  accessed_at: '2026-10-13T21:14:27.714009Z'
  support: supports
  summary: Actual execution 2026-10-13T21:10:13.855373Z to 2026-10-13T21:10:15.806947Z,
    exit 0. Full QC is deterministic validation, not scientific completion.
  snapshot_sha256: 3d8b5114b9a194409a96d413173c08b079b535b108b8d5c3a1a46b5bc7ebe63d
findings:
- finding_id: F1
  issue_key: capsular-polysaccharide-2-exact-product-assignment
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Exact capsule-product assignment is unsupported across deposited serotypes
  description: Five deposited K5/K20/K54 loci share one finite, stereochemically undefined
    six-ring graph. PubChem names that graph as K15. The inspected study abstract
    concerns genotyping and clinical/serum-resistance comparisons, not exact product
    structural assignment. Registry names/MeSH associations are name-based and are
    not independent chemical certification. Exact PubChem graph agreement is verified;
    deleting its xref alone would not repair the biological assignment. The confirmed
    defect is unsupported exact-product assignment across the recorded contexts, not
    an experimentally established replacement structure.
  target_ids:
  - naturalproductmech:mibig-6a3f1200b4
  field_paths:
  - chemical_structure
  - producer_organisms
  - biosynthetic_gene_clusters
  evidence_ids:
  - E-current
  - E-prior
  - E-genbank
  - E-matrix
  - E-strains
  - E-scope
  - E-publish-focused
  - E-chemistry
  - E-pubchem
  - E-literature
  rule_id: 'CLAUDE.md: A record is a structure; review-checklist: Identity and Gene
    clusters'
  native_severity: blocker
  normalization_reason: The compound identity assigned to biological source claims
    is not established; a valid graph and generic capsule name do not prove equivalence.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported chemical, producer and cluster assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated harmonization and grading
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Implemented pinned structure corrections
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/935
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T210832Z-capsular-polysaccharide-2
    finding_id: F1
  disposition_reason: Mitigated by a cited OPEN discussion. The per-locus exact chemical
    product and representation boundary remain unadjudicated; no replacement structure
    or broader equivalence is inferred.
- finding_id: F2
  issue_key: capsular-polysaccharide-2-deposited-strain-context
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Deposited strain and serotype qualifications are missing
  description: 5 source qualifiers are available but not explicitly carried into producer
    strain/evidence context.
  target_ids:
  - naturalproductmech:mibig-6a3f1200b4
  field_paths:
  - producer_organisms[].strain
  - producer_organisms[].evidence
  evidence_ids:
  - E-current
  - E-prior
  - E-genbank
  - E-matrix
  - E-strains
  - E-scope
  - E-publish-focused
  rule_id: 'review-checklist: Producer organisms'
  native_severity: minor
  normalization_reason: Bounded provenance repair that can be made without deciding
    chemical identity or evidence grade.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented pinned strain qualifications
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/938
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T210832Z-capsular-polysaccharide-2
    finding_id: F2
  disposition_reason: Exact deposited strain/isolate qualifiers and serotype rationale
    are now preserved through pinned curation rows and guarded generation; all narrow
    invariants pass. This resolves only missing context, not chemical identity.
assessments:
- assessment_id: fixed-context
  area: provenance
  topic: Deposited strain/isolate and serotype scope
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-6a3f1200b4
  evidence_ids:
  - E-current
  - E-strains
  - E-genbank
  - E-matrix
  - E-scope
  summary: Exact qualifiers agree with the deposited source context; no biological
    scope or evidence-grade change.
- assessment_id: identity-open
  area: identity
  topic: Remaining exact-product uncertainty
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-6a3f1200b4
  evidence_ids:
  - E-current
  - E-prior
  - E-chemistry
  - E-pubchem
  - E-literature
  summary: OPEN qualification is mitigation, not identity adjudication. Full-owner
    assessment and primary access limits remain partial.
actions:
- action_id: A1
  description: Preserve an OPEN identity qualification, then adjudicate exact locus-to-product
    and occurrence assignments from accessible primary chemistry before migration;
    do not rename all entries to the registry serotype.
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-6a3f1200b4
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported chemical, producer and cluster assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated harmonization and grading
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Implemented pinned structure corrections
  acceptance_checks:
  - Per-source structure and polymer/form boundary justified by inspected primary
    chemistry.
  - Use a supported maintained migration/exclusion path, preserve provenance, and
    pass strict validation, reproduction and full QC.
  generator: scripts/seed_from_sources.py
limitations:
- Scoped disposition only; no new owner coverage or native REVIEWED promotion.
- All predecessor primary and authority access limits persist. No additional primary
  retrieval or access bypass.
- 'Source state is working_tree: current input bytes were inspected and archived,
  not claimed to exist at the base commit.'
- Full QC is still running at authoring; canonical checks and final CI follow. An
  initial local QC lint failure was corrected before restarting. Only the recorded
  focused tests, strict validation and object-level scope audit are claimed here.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261013T210832Z-capsular-polysaccharide-2
  relationship: Exact predecessor disposition; preserve immutable full-owner partial
    assessment.
```
