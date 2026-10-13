# ferrichrome: scoped xref and exact-form qualification disposition

- Review: 20261013T174145Z-ferrichrome-scoped-disposition
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T17:19:58.064754Z
- Finished UTC: 2026-10-13T17:41:45.137222Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Resolve missing isotope-specific qualification only; experimental product attribution remains unknown.

## Scope And Provenance

One exact owner; scoped predecessor disposition, not a new full-record review.

Selection: User-authorized adversarial PR review and issue remediation.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base fe0973229440c2a9c42a3e633a311d8b731391e9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-91bcef2bc6 | data/natural_products/amino_acids_and_peptides/ferrichrome.yaml | generated | ferrichrome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| focused | passed | True | naturalproductmech:mibig-91bcef2bc6 | 202 focused tests passed, including exclusion scope, qualification carry-forward, archive integrity, full campaign accounting and shared seeder safeguards. |
| strict | passed | True | naturalproductmech:mibig-91bcef2bc6 | Both exact owners passed closed-schema strict validation with zero errors. |
| reseed-a | passed | True | naturalproductmech:mibig-91bcef2bc6 | The C26 owner re-seeded byte-identically with one unchanged record. |
| reseed-b | passed | True | naturalproductmech:mibig-91bcef2bc6 | The iron-55 owner re-seeded byte-identically with one unchanged record. |
| scope-audit | passed | True | naturalproductmech:mibig-91bcef2bc6 | All 3115 owners and 243 components retained. Only the two intended owners changed; all other 3113 owners, raw inventories, path lock and 32 prior review pairs are unchanged. |
| render | passed | True | naturalproductmech:mibig-91bcef2bc6 | All 3115 pages regenerated; only two record pages, browse/search xref data and discussion count changed. |
| qc-final | passed | True | naturalproductmech:mibig-91bcef2bc6 | Full native QC passed; consult the retained log for exact test and skip counts. Lint, pinned governance, documentation, raw provenance, source queue, tests, all-owner strict validation, site consistency, exact reproduction and path-lock gates passed. This is not biological sign-off. |
| labels | passed | True | naturalproductmech:mibig-91bcef2bc6 | Fresh configured label gate passed; warning mismatches and no-adapter skips remain nonblocking and do not certify exact chemical identity. |
| Initial full QC before statistics refresh | failed | False | naturalproductmech:mibig-91bcef2bc6 | Initial QC correctly rejected stale README discussion coverage. The generated statistics were refreshed and qc-final reran the full gate successfully. |
| Experimental exact-product attribution | unavailable | True | naturalproductmech:mibig-91bcef2bc6 | Previously denied primary text remains unavailable. No alternative retrieval or newly inspected experimental identity is claimed. This successor is partial. |

## Scientific And Domain Assessments

### Exact-owner repair and qualification

scope: supported. Targets: naturalproductmech:mibig-91bcef2bc6.

The iron-55 form and incomplete stereochemistry are visibly qualified; no exact chemical information or PubChem equivalence was deleted to conceal the attribution uncertainty.

### Unresolved exact experimental product

identity: unknown. Targets: naturalproductmech:mibig-91bcef2bc6.

Missing qualification is repaired, but whether iron-55 denotes a tracer, source error or intended product remains unresolved. No whole-record pass or REVIEWED promotion.

### Maintained ownership and immutable history

provenance: supported. Targets: naturalproductmech:mibig-91bcef2bc6.

Maintained source-row decision plus guarded writer and curation events; same-key re-seed preserves qualifications. All unrelated inputs and prior observations remain unchanged. Full QC verifies reproducibility, not scientific completeness.

## Findings

### F1: Exact 55Fe product attribution is unqualified and experimentally unresolved

major / resolved / provisional; issue key: mibig-BGC0000901-compound-1-unqualified-55Fe-origin.

The stored graph and exact PubChem644246 match encode iron-55, with three undefined peptide stereocenters. The name, NATURAL_PRODUCT origin, producer and locus assertions do not qualify that isotopic form. The abstract identifies ferrichrome production but does not establish this isotope-specific product; the cited full paper returned403. The available locus patent describes gene cloning and an enzyme assay rather than characterizing this isotope-specific complete product. The isotope encoding is confirmed, but whether it is an erroneous source drawing, an experimental tracer or an intentionally scoped product remains provisional. Do not call the constitution wrong, delete an exact xref, silently remove the isotope, assign missing stereochemistry, or assume the organism cannot incorporate labeled iron.

Disposition: Resolve only the missing exact-form qualification: a cited OPEN discussion explicitly identifies iron-55, unspecified centers and the unresolved source drawing/tracer/product alternatives. Experimental attribution remains unknown; the exact CID, isotope, stereochemistry, evidence grades and SEEDED status are preserved.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/amino_acids_and_peptides/ferrichrome.yaml; Entire current YAML, including exact graph and append-only history | supports | Cited OPEN qualification is present. Chemistry, source concepts, conservative evidence grades and SEEDED status are unchanged. Only the nonexact CID on the C26 owner was removed. |
| prior | reviews/structured/20261013T170122Z-ferrichrome/review.yaml; Exact predecessor findings | supports | The immutable original remains the historical full-record assessment; this successor only assesses disposition. |
| xref-table | curation/mibig_xref_exclusions.tsv; BGC0000900:1 / pubchem:644246 | supports | Complete untouched row pin 78b115cce5a8a133196da68d8dd417a75f5a8f42aa0344a1d3c76d389e58f791 scopes the exclusion to the C26 owner; the separate iron-55 owner retains the same CID. |
| scope-proof | /private/tmp/npmech-ferrichrome-publish-i31W5V/scope-audit.json; Complete filesystem and field comparison | supports | All owner/component and review denominators preserved; no identity migration or unrelated scientific change. |
| regressions | /private/tmp/npmech-ferrichrome-publish-i31W5V/focused.log; 202 focused tests | supports | Decision pinning, exact-owner preservation, same-key-only carry-forward and durable evidence checks passed. |
| archive | reviews/evidence/20261013-ferrichrome/manifest.json; 116 retained artifacts, 13 explicit reference-only sources | supports | Evidence snapshots and source receipts survive publication without redistributing publisher/patent text. |
| chemistry | /private/tmp/npmech-ferrichrome-resume-mXOYL5/chemistry.json; RDKit2026.03.5 result ferrichrome and authority comparisons; same retained capture used for scoped disposition, not a fresh network retrieval | supports | Computed C27H42FeN9O12, net charge 0, monoisotopic mass 739.233586184 Da; 0 specified/3 undefined tetrahedral centers; acetyl/formyl hydroxamates 3/0; iron isotope list [55]. Exact owner InChI/key roundtrip passed. Calculations are not measurements. Normalization is diagnostic, not authorized identity replacement. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/90658043,644246/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; PropertyTable.Properties for CID90658043 and CID644246; HTTP200 capture 2026-10-13T16:45:00.740185Z..2026-10-13T16:45:01.117565Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/pubchem-resume.json; receipt SHA256 b21e89ec88fb8064682ed966bdcddcbf7970d431e58f8fa33026a716cac9749b; same retained capture used for scoped disposition, not a fresh network retrieval | supports | Recovered HTTP200: CID90658043 matches ZZDYFKJSJLUQON-UFYCRDLUSA-N; CID644246 matches GGUNGDGGXMHBMJ-HCMAANCNSA-N. Both formulae and exact InChIs were recomputed. Registry equivalence is not evidence for biosynthesis. |
| chebi-ferrichrome | https://www.ebi.ac.uk/chebi/backend/api/public/compound/5019/; CHEBI5019 default_structure, chemical_data, stars and definition; HTTP200 capture 2026-10-13T16:45:34.903592Z..2026-10-13T16:45:35.832294Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/CHEBI5019-resume.json; receipt SHA256 bf6c76369978dbde977d07416b9e6451269b02318a10419e24b3d807aaa704c0; same retained capture used for scoped disposition, not a fresh network retrieval | context_only | Live 3-star ferrichrome agrees with the pinned default graph: GGUNGDGGXMHBMJ-OCIDDWSYSA-N, C27H42FeN9O12, three specified peptide centers, no isotope label. Its three N-acetyl groups distinguish it from the C26 record. Representation of coordination is not interpreted as physical negative iron oxidation state. |
| chebi-deferrichrome | https://www.ebi.ac.uk/chebi/backend/api/public/compound/90132/; CHEBI90132 default_structure, chemical_data, stars and definition; HTTP200 capture 2026-10-13T16:45:56.396094Z..2026-10-13T16:45:57.051939Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/CHEBI90132-resume.json; receipt SHA256 a3cd2f780cd4c2d44ccd4d8d9332479ef56bc91c2cdd23be6fd177743bb1cf19; same retained capture used for scoped disposition, not a fresh network retrieval | context_only | Live 3-star deferrichrome agrees with pinned ZFDAUYPBCXMSBF-ACRUOGEOSA-N, C27H45N9O12, three acetyl hydroxamates and no iron. It is not the C26 form. Occurrences and roles on this nonexact candidate are not transferred. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0000901.5/annotations.json; compounds[0], taxonomy, loci, biosynthesis classes and legacy references; HTTP200 capture 2026-10-13T15:36:56.181570Z..2026-10-13T15:36:57.088898Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/BGC0000901.5.json; receipt SHA256 8c3da05226706d36e16ae78a92cf9c22adc95079b8e30dae96b79ae828f1ec1a; same retained capture used for scoped disposition, not a fresh network retrieval | supports | Exact active version5 chemistry, host and references match the raw row. Empty locus methods and 0..0 unspecified bounds are not experiments or real coordinates. OTHER is source asserted; questionable quality and placeholder reviewers are not scientific truth signals. No assertion this is the latest version. |
| paper-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25062661%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; EuropePMC exact PMID25062661/DOI10.1093/bfgp/elu026 abstract and metadata; HTTP200 capture 2026-10-13T15:37:03.219491Z..2026-10-13T15:37:04.129729Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/PMID25062661.json; receipt SHA256 d27c4fe61474bd061f94f98e0b9d755178ed766233aadb8b731c6e50c287277c; same retained capture used for scoped disposition, not a fresh network retrieval | partial | The abstract reports A.niger HPLC ferrichrome production, coprogenB and effects of sreA deletion. It does not establish55Fe-specific product identity, exact strain/locus attribution or a method for DJ389528.1. Full text is subscription-only with no PMCID. |
| paper-access | https://doi.org/10.1093/bfgp/elu026; Error response only; HTTP403 capture 2026-10-13T15:38:50.178129Z..2026-10-13T15:38:51.102439Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/paper25062661.html; receipt SHA256 39d71fcbfa349eb6307e485a001f050c576812f2a5bdbaa32689a6e3cd7d6da3; same retained capture used for scoped disposition, not a fresh network retrieval | unknown | Publisher HTTP403; no full-text experimental sections or supporting information inspected and no alternate retrieval. |
| locus-patent | https://patents.google.com/patent/JP2003230381A/en; JP2003230381A prose0017-0027,0031-0045 including table1; cited independently by GenBank, not an alternate copy of the denied paper; HTTP200 capture 2026-10-13T16:45:59.626111Z..2026-10-13T16:46:00.120752Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/patent-DJ389528.html; receipt SHA256 b27940bb11ffbd355471506afe2021f87603b1224843850da7437d88c494268b; same retained capture used for scoped disposition, not a fresh network retrieval | partial | The locus patent identifies IFO4067 genomic DNA for nsb1/nsb2 cloning and tests expressed nsb1 enzyme activity in E.coli. This is useful strain/locus context, not complete55Fe product characterization. General family/member terminology and machine-translation errors require care; sequence figures were not visually audited. |

## Limits And Additional Notes

- Partial, scoped successor: no newly assessed owner and no native status promotion.
- Experimental product attribution remains unresolved. Earlier primary access limits remain; publication does not retry denied endpoints or declare missing evidence false.
- The exact inspected input tree is retained by review-base/ferrichrome-remediation-20261013. The full QC rerun follows the generated README count correction in c1583b769; all 17 inspected scientific and review inputs still match the tagged tree. Canonical successor checks and PR/merge-queue CI follow saving.
- Full QC preceded these new review bundles; their canonical and contract validation is separate.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T174145Z-ferrichrome-scoped-disposition
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'ferrichrome: scoped xref and exact-form qualification disposition'
started_at: '2026-10-13T17:19:58.064754Z'
finished_at: '2026-10-13T17:41:45.137222Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant implemented the changes and performed a separate
    adversarial pass; not independent human review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Resolve missing isotope-specific qualification only; experimental product
  attribution remains unknown.
source:
  git_revision: fe0973229440c2a9c42a3e633a311d8b731391e9
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: a4627732141b210992a2bac02fc4dc24eb7edb01b810873ce0f03cdcada7b5f7
    role: context
  - path: data/natural_products/amino_acids_and_peptides/ferrichrome.yaml
    sha256: afa5399ee038283d1b11d3d3258371a271598f3c948958018aa90191ae3d7f5e
    role: target
  - path: data/raw/mibig_compounds.tsv
    sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
    role: context
  - path: docs/CURATION.md
    sha256: 245df036e09a00a2f92a5f78c70eadb210cef7d70046e8ee35377a9e636cd30b
    role: context
  - path: docs/record-review-profile.md
    sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: reviews/evidence/20261013-ferrichrome/manifest.json
    sha256: efc55cc93e8ab57c4e5923c5c0c2fae7edd77c2b794cf990331d22db56fd8792
    role: context
  - path: reviews/structured/20261013T170122Z-ferrichrome/review.yaml
    sha256: ca4ec33d30c2a7ee597844cdf53ae5e60d1a960630620caec21dd6930d30ffae
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 8d82d7633e0492e9fe16011f6e5af6f8024f573e80c8a24176b65e2941478b71
    role: context
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
    role: context
  - path: src/naturalproductmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: tests/test_ferrichrome_curation.py
    sha256: 70fefc22ec85b952617e7370aee395c948e2d6477e3431507e8c5451c32b94ad
    role: context
  - path: tests/test_ferrichrome_review_archive.py
    sha256: 1ec2e7276e65f8960d5c55ea7d1c3e642e58d409466ee49f917dcc83e7aadcce
    role: context
targets:
- target_id: naturalproductmech:mibig-91bcef2bc6
  path: data/natural_products/amino_acids_and_peptides/ferrichrome.yaml
  label: ferrichrome
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
scope:
  description: One exact owner; scoped predecessor disposition, not a new full-record
    review.
  selection: User-authorized adversarial PR review and issue remediation.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  exclusions:
  - target: All other 3114 owners and earlier unresolved scientific checks
    reason: No additional scientific coverage; campaign stays 3115 owners and 243
      components.
checks:
- check_id: focused
  name: focused
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_ferrichrome_curation.py tests/test_ferrichrome_review_archive.py
    tests/test_xref_exclusions.py tests/test_seed_skeleton.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  summary: 202 focused tests passed, including exclusion scope, qualification carry-forward,
    archive integrity, full campaign accounting and shared seeder safeguards.
  scope_note: Actual run 2026-10-13T17:17:28.514359+00:00 to 2026-10-13T17:17:37.787287+00:00;
    log SHA256 a20569d547a7ce95d033903421694d2010e640b2ebf26acd6d92ede3c3171fe6
- check_id: strict
  name: strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml
    data/natural_products/amino_acids_and_peptides/ferrichrome.yaml --out /private/tmp/npmech-ferrichrome-publish-i31W5V/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  summary: Both exact owners passed closed-schema strict validation with zero errors.
  scope_note: Actual run 2026-10-13T17:18:01.594132+00:00 to 2026-10-13T17:18:06.284461+00:00;
    log SHA256 0f49547f1b7e873ab96bf58d078c0a75540fc427c8cd518460a1ffe627e8ed82
- check_id: reseed-a
  name: reseed-a
  status: passed
  required: true
  command: .venv/bin/python scripts/seed_from_sources.py --only naturalproductmech:mibig-ab69cdf6e5
    --apply
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  summary: The C26 owner re-seeded byte-identically with one unchanged record.
  scope_note: Actual run 2026-10-13T17:18:28.711529+00:00 to 2026-10-13T17:18:37.879729+00:00;
    log SHA256 67e92562fe50792bab3f0f4aac51f3fb0afa9d85dd044b9cfbde8fbb6bdc6d39
- check_id: reseed-b
  name: reseed-b
  status: passed
  required: true
  command: .venv/bin/python scripts/seed_from_sources.py --only naturalproductmech:mibig-91bcef2bc6
    --apply
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  summary: The iron-55 owner re-seeded byte-identically with one unchanged record.
  scope_note: Actual run 2026-10-13T17:18:48.432634+00:00 to 2026-10-13T17:18:54.891747+00:00;
    log SHA256 67e92562fe50792bab3f0f4aac51f3fb0afa9d85dd044b9cfbde8fbb6bdc6d39
- check_id: scope-audit
  name: scope-audit
  status: passed
  required: true
  command: .venv/bin/python /private/tmp/npmech-ferrichrome-publish-i31W5V/scope_audit.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  summary: All 3115 owners and 243 components retained. Only the two intended owners
    changed; all other 3113 owners, raw inventories, path lock and 32 prior review
    pairs are unchanged.
  scope_note: Actual run 2026-10-13T17:18:00.423156+00:00 to 2026-10-13T17:18:02.568855+00:00;
    log SHA256 d54c2c4009fcb9cb4d1df267fff75c5605f00566e4c0e4518d9798f478618acd
- check_id: render
  name: render
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  summary: All 3115 pages regenerated; only two record pages, browse/search xref data
    and discussion count changed.
  scope_note: Actual run 2026-10-13T17:17:29.678348+00:00 to 2026-10-13T17:18:58.307056+00:00;
    log SHA256 7355dd2b2c7840ab9ec8e4e68754f2bf241e7820e0f8156079359a86150d6202
- check_id: qc-final
  name: qc-final
  status: passed
  required: true
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  summary: Full native QC passed; consult the retained log for exact test and skip
    counts. Lint, pinned governance, documentation, raw provenance, source queue,
    tests, all-owner strict validation, site consistency, exact reproduction and path-lock
    gates passed. This is not biological sign-off.
  scope_note: Actual run 2026-10-13T17:24:47.000564+00:00 to 2026-10-13T17:40:26.517808+00:00;
    log SHA256 c3dc994ed600f4cfe333f1e439034d99b5e7694cd732d669cb622d313615bfa3
- check_id: labels
  name: labels
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  summary: Fresh configured label gate passed; warning mismatches and no-adapter skips
    remain nonblocking and do not certify exact chemical identity.
  scope_note: Actual run 2026-10-13T17:18:27.442433+00:00 to 2026-10-13T17:21:28.414718+00:00;
    log SHA256 556ef5804e095767472c0aa8a542d5bff7e332470383a992e6b260103034414b
- check_id: qc-initial
  name: Initial full QC before statistics refresh
  status: failed
  required: false
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  exit_code: 1
  expected_exit_code: 0
  command: .venv/bin/python scripts/run_qc.py
  summary: Initial QC correctly rejected stale README discussion coverage. The generated
    statistics were refreshed and qc-final reran the full gate successfully.
- check_id: exact-primary
  name: Experimental exact-product attribution
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  summary: Previously denied primary text remains unavailable. No alternative retrieval
    or newly inspected experimental identity is claimed. This successor is partial.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/amino_acids_and_peptides/ferrichrome.yaml
  locator: Entire current YAML, including exact graph and append-only history
  accessed_at: '2026-10-13T17:41:45.136016Z'
  support: supports
  summary: Cited OPEN qualification is present. Chemistry, source concepts, conservative
    evidence grades and SEEDED status are unchanged. Only the nonexact CID on the
    C26 owner was removed.
  snapshot_sha256: afa5399ee038283d1b11d3d3258371a271598f3c948958018aa90191ae3d7f5e
- evidence_id: prior
  kind: record_content
  reference: reviews/structured/20261013T170122Z-ferrichrome/review.yaml
  locator: Exact predecessor findings
  accessed_at: '2026-10-13T17:41:45.136122Z'
  support: supports
  summary: The immutable original remains the historical full-record assessment; this
    successor only assesses disposition.
  snapshot_sha256: ca4ec33d30c2a7ee597844cdf53ae5e60d1a960630620caec21dd6930d30ffae
- evidence_id: xref-table
  kind: record_content
  reference: curation/mibig_xref_exclusions.tsv
  locator: BGC0000900:1 / pubchem:644246
  accessed_at: '2026-10-13T17:41:45.136314Z'
  support: supports
  summary: Complete untouched row pin 78b115cce5a8a133196da68d8dd417a75f5a8f42aa0344a1d3c76d389e58f791
    scopes the exclusion to the C26 owner; the separate iron-55 owner retains the
    same CID.
  snapshot_sha256: a4627732141b210992a2bac02fc4dc24eb7edb01b810873ce0f03cdcada7b5f7
- evidence_id: scope-proof
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-publish-i31W5V/scope-audit.json
  locator: Complete filesystem and field comparison
  accessed_at: '2026-10-13T17:41:45.136417Z'
  support: supports
  summary: All owner/component and review denominators preserved; no identity migration
    or unrelated scientific change.
  snapshot_sha256: 7edb36b75199ca1dd2f893c5996daac1602103232cc44826fa7e71745cf2c645
- evidence_id: regressions
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-publish-i31W5V/focused.log
  locator: 202 focused tests
  accessed_at: '2026-10-13T17:41:45.136514Z'
  support: supports
  summary: Decision pinning, exact-owner preservation, same-key-only carry-forward
    and durable evidence checks passed.
  snapshot_sha256: a20569d547a7ce95d033903421694d2010e640b2ebf26acd6d92ede3c3171fe6
- evidence_id: archive
  kind: validation
  reference: reviews/evidence/20261013-ferrichrome/manifest.json
  locator: 116 retained artifacts, 13 explicit reference-only sources
  accessed_at: '2026-10-13T17:41:45.136589Z'
  support: supports
  summary: Evidence snapshots and source receipts survive publication without redistributing
    publisher/patent text.
  snapshot_sha256: efc55cc93e8ab57c4e5923c5c0c2fae7edd77c2b794cf990331d22db56fd8792
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-resume-mXOYL5/chemistry.json
  locator: RDKit2026.03.5 result ferrichrome and authority comparisons; same retained
    capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.136827Z'
  support: supports
  summary: Computed C27H42FeN9O12, net charge 0, monoisotopic mass 739.233586184 Da;
    0 specified/3 undefined tetrahedral centers; acetyl/formyl hydroxamates 3/0; iron
    isotope list [55]. Exact owner InChI/key roundtrip passed. Calculations are not
    measurements. Normalization is diagnostic, not authorized identity replacement.
  snapshot_sha256: dbc9e4241c6a271fa92a0dfb53f35e16a0c8d8159e6f4f8a7538a9dd435c9014
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/90658043,644246/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: PropertyTable.Properties for CID90658043 and CID644246; HTTP200 capture
    2026-10-13T16:45:00.740185Z..2026-10-13T16:45:01.117565Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/pubchem-resume.json;
    receipt SHA256 b21e89ec88fb8064682ed966bdcddcbf7970d431e58f8fa33026a716cac9749b;
    same retained capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.136842Z'
  support: supports
  summary: 'Recovered HTTP200: CID90658043 matches ZZDYFKJSJLUQON-UFYCRDLUSA-N; CID644246
    matches GGUNGDGGXMHBMJ-HCMAANCNSA-N. Both formulae and exact InChIs were recomputed.
    Registry equivalence is not evidence for biosynthesis.'
  snapshot_sha256: a2bf6a9ecde781f75da334f05f76cca8b34b429794ee23e1249f67339572b452
- evidence_id: chebi-ferrichrome
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/5019/
  locator: CHEBI5019 default_structure, chemical_data, stars and definition; HTTP200
    capture 2026-10-13T16:45:34.903592Z..2026-10-13T16:45:35.832294Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/CHEBI5019-resume.json;
    receipt SHA256 bf6c76369978dbde977d07416b9e6451269b02318a10419e24b3d807aaa704c0;
    same retained capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.136853Z'
  support: context_only
  summary: 'Live 3-star ferrichrome agrees with the pinned default graph: GGUNGDGGXMHBMJ-OCIDDWSYSA-N,
    C27H42FeN9O12, three specified peptide centers, no isotope label. Its three N-acetyl
    groups distinguish it from the C26 record. Representation of coordination is not
    interpreted as physical negative iron oxidation state.'
  snapshot_sha256: 119bd8da9e64ea03fbe7a3fc2f37c5fe3e66a6bd151e090fd3a568e9727286ac
- evidence_id: chebi-deferrichrome
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/90132/
  locator: CHEBI90132 default_structure, chemical_data, stars and definition; HTTP200
    capture 2026-10-13T16:45:56.396094Z..2026-10-13T16:45:57.051939Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/CHEBI90132-resume.json;
    receipt SHA256 a3cd2f780cd4c2d44ccd4d8d9332479ef56bc91c2cdd23be6fd177743bb1cf19;
    same retained capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.136863Z'
  support: context_only
  summary: Live 3-star deferrichrome agrees with pinned ZFDAUYPBCXMSBF-ACRUOGEOSA-N,
    C27H45N9O12, three acetyl hydroxamates and no iron. It is not the C26 form. Occurrences
    and roles on this nonexact candidate are not transferred.
  snapshot_sha256: 43a98c9dc374a79365dd55e6e19bf19f36ac8a29162ee1f2065607e30289d215
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000901.5/annotations.json
  locator: compounds[0], taxonomy, loci, biosynthesis classes and legacy references;
    HTTP200 capture 2026-10-13T15:36:56.181570Z..2026-10-13T15:36:57.088898Z; payload
    /private/tmp/npmech-ferrichrome-review-W2MXlZ/BGC0000901.5.json; receipt SHA256
    8c3da05226706d36e16ae78a92cf9c22adc95079b8e30dae96b79ae828f1ec1a; same retained
    capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.136872Z'
  support: supports
  summary: Exact active version5 chemistry, host and references match the raw row.
    Empty locus methods and 0..0 unspecified bounds are not experiments or real coordinates.
    OTHER is source asserted; questionable quality and placeholder reviewers are not
    scientific truth signals. No assertion this is the latest version.
  snapshot_sha256: d578aef294a2ebf3c41e6b5ea6a086a4f22dd9448f58b9e639ab2f80705c210a
- evidence_id: paper-metadata
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25062661%20AND%20SRC%3AMED&format=json&resultType=core
  locator: EuropePMC exact PMID25062661/DOI10.1093/bfgp/elu026 abstract and metadata;
    HTTP200 capture 2026-10-13T15:37:03.219491Z..2026-10-13T15:37:04.129729Z; payload
    /private/tmp/npmech-ferrichrome-review-W2MXlZ/PMID25062661.json; receipt SHA256
    d27c4fe61474bd061f94f98e0b9d755178ed766233aadb8b731c6e50c287277c; same retained
    capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.136883Z'
  support: partial
  summary: The abstract reports A.niger HPLC ferrichrome production, coprogenB and
    effects of sreA deletion. It does not establish55Fe-specific product identity,
    exact strain/locus attribution or a method for DJ389528.1. Full text is subscription-only
    with no PMCID.
  snapshot_sha256: 03d412fc53e29630237a50836c34fe0a9fc82ab14ec74da22d23d7895c60f1c2
- evidence_id: paper-access
  kind: search
  reference: https://doi.org/10.1093/bfgp/elu026
  locator: Error response only; HTTP403 capture 2026-10-13T15:38:50.178129Z..2026-10-13T15:38:51.102439Z;
    payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/paper25062661.html; receipt
    SHA256 39d71fcbfa349eb6307e485a001f050c576812f2a5bdbaa32689a6e3cd7d6da3; same
    retained capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.136893Z'
  support: unknown
  summary: Publisher HTTP403; no full-text experimental sections or supporting information
    inspected and no alternate retrieval.
  snapshot_sha256: 038bc337c4986fbb402dad8086f108158878da733c92d4745d8f98cdc8a3df65
  search_scope: Preserved exact DOI request10.1093/bfgp/elu026; stopped after403.
    Abstract remains a narrower source, not a substitute for the missing experiment.
- evidence_id: locus-patent
  kind: primary_source
  reference: https://patents.google.com/patent/JP2003230381A/en
  locator: JP2003230381A prose0017-0027,0031-0045 including table1; cited independently
    by GenBank, not an alternate copy of the denied paper; HTTP200 capture 2026-10-13T16:45:59.626111Z..2026-10-13T16:46:00.120752Z;
    payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/patent-DJ389528.html; receipt
    SHA256 b27940bb11ffbd355471506afe2021f87603b1224843850da7437d88c494268b; same
    retained capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.136909Z'
  support: partial
  summary: The locus patent identifies IFO4067 genomic DNA for nsb1/nsb2 cloning and
    tests expressed nsb1 enzyme activity in E.coli. This is useful strain/locus context,
    not complete55Fe product characterization. General family/member terminology and
    machine-translation errors require care; sequence figures were not visually audited.
  snapshot_sha256: e1d8853141181eb1ee83dd6199591dbaad96f7d36a61882c656158d782f4d291
assessments:
- assessment_id: scoped-repair
  area: scope
  topic: Exact-owner repair and qualification
  outcome: supported
  summary: The iron-55 form and incomplete stereochemistry are visibly qualified;
    no exact chemical information or PubChem equivalence was deleted to conceal the
    attribution uncertainty.
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  evidence_ids:
  - owner
  - pubchem
  - xref-table
  - regressions
- assessment_id: identity-limit
  area: identity
  topic: Unresolved exact experimental product
  outcome: unknown
  summary: Missing qualification is repaired, but whether iron-55 denotes a tracer,
    source error or intended product remains unresolved. No whole-record pass or REVIEWED
    promotion.
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  evidence_ids:
  - owner
  - prior
  - chemistry
  - chebi-ferrichrome
- assessment_id: preserved-inputs
  area: provenance
  topic: Maintained ownership and immutable history
  outcome: supported
  summary: Maintained source-row decision plus guarded writer and curation events;
    same-key re-seed preserves qualifications. All unrelated inputs and prior observations
    remain unchanged. Full QC verifies reproducibility, not scientific completeness.
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  evidence_ids:
  - owner
  - scope-proof
  - archive
  - regressions
findings:
- finding_id: F1
  issue_key: mibig-BGC0000901-compound-1-unqualified-55Fe-origin
  category: evidence
  severity: major
  status: resolved
  certainty: provisional
  title: Exact 55Fe product attribution is unqualified and experimentally unresolved
  description: The stored graph and exact PubChem644246 match encode iron-55, with
    three undefined peptide stereocenters. The name, NATURAL_PRODUCT origin, producer
    and locus assertions do not qualify that isotopic form. The abstract identifies
    ferrichrome production but does not establish this isotope-specific product; the
    cited full paper returned403. The available locus patent describes gene cloning
    and an enzyme assay rather than characterizing this isotope-specific complete
    product. The isotope encoding is confirmed, but whether it is an erroneous source
    drawing, an experimental tracer or an intentionally scoped product remains provisional.
    Do not call the constitution wrong, delete an exact xref, silently remove the
    isotope, assign missing stereochemistry, or assume the organism cannot incorporate
    labeled iron.
  target_ids:
  - naturalproductmech:mibig-91bcef2bc6
  field_paths:
  - label
  - chemical_structure.smiles
  - biosynthesis_origin
  - producer_organisms
  - biosynthetic_gene_clusters
  - discussions
  evidence_ids:
  - owner
  - prior
  - chemistry
  - pubchem
  - scope-proof
  - regressions
  - paper-metadata
  - paper-access
  - locus-patent
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Guarded complete-row-pinned REPLACE_WITH_CHEBI, only after exact target
      adjudication
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Untouched versioned source compound, producer and locus row
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG source extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated identity and source harmonization
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/ferrichrome.yaml
    role: Only a curator-owned cited qualification through the validated writer; not
      direct seeded-field edits
  rule_id: review-checklist:Structure/Producer organisms/Gene clusters; exact chemical
    form and evidence scope
  native_severity: major
  normalization_reason: Potentially unsupported isotope-specific natural-product attribution
    is material, while missing primary evidence precludes a confirmed wrong-product
    verdict.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T170122Z-ferrichrome
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/920
  disposition_reason: 'Resolve only the missing exact-form qualification: a cited
    OPEN discussion explicitly identifies iron-55, unspecified centers and the unresolved
    source drawing/tracer/product alternatives. Experimental attribution remains unknown;
    the exact CID, isotope, stereochemistry, evidence grades and SEEDED status are
    preserved.'
actions: []
limitations:
- 'Partial, scoped successor: no newly assessed owner and no native status promotion.'
- Experimental product attribution remains unresolved. Earlier primary access limits
  remain; publication does not retry denied endpoints or declare missing evidence
  false.
- The exact inspected input tree is retained by review-base/ferrichrome-remediation-20261013.
  The full QC rerun follows the generated README count correction in c1583b769; all
  17 inspected scientific and review inputs still match the tagged tree. Canonical
  successor checks and PR/merge-queue CI follow saving.
- Full QC preceded these new review bundles; their canonical and contract validation
  is separate.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261013T170122Z-ferrichrome
  relationship: Scoped disposition; original full assessment remains immutable.
links:
- https://github.com/CultureBotAI/NaturalProductMech/pull/917
```
