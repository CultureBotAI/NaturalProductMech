# ferrichrome-2: scoped xref and exact-form qualification disposition

- Review: 20261013T174145Z-ferrichrome-2-scoped-disposition
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T17:19:53.414574Z
- Finished UTC: 2026-10-13T17:41:45.030084Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Resolve only F2; F1 remains open despite explicit mitigation.

## Scope And Provenance

One exact owner; scoped predecessor disposition, not a new full-record review.

Selection: User-authorized adversarial PR review and issue remediation.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base fe0973229440c2a9c42a3e633a311d8b731391e9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-ab69cdf6e5 | data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml | generated | ferrichrome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| focused | passed | True | naturalproductmech:mibig-ab69cdf6e5 | 202 focused tests passed, including exclusion scope, qualification carry-forward, archive integrity, full campaign accounting and shared seeder safeguards. |
| strict | passed | True | naturalproductmech:mibig-ab69cdf6e5 | Both exact owners passed closed-schema strict validation with zero errors. |
| reseed-a | passed | True | naturalproductmech:mibig-ab69cdf6e5 | The C26 owner re-seeded byte-identically with one unchanged record. |
| reseed-b | passed | True | naturalproductmech:mibig-ab69cdf6e5 | The iron-55 owner re-seeded byte-identically with one unchanged record. |
| scope-audit | passed | True | naturalproductmech:mibig-ab69cdf6e5 | All 3115 owners and 243 components retained. Only the two intended owners changed; all other 3113 owners, raw inventories, path lock and 32 prior review pairs are unchanged. |
| render | passed | True | naturalproductmech:mibig-ab69cdf6e5 | All 3115 pages regenerated; only two record pages, browse/search xref data and discussion count changed. |
| qc-final | passed | True | naturalproductmech:mibig-ab69cdf6e5 | Full native QC passed; consult the retained log for exact test and skip counts. Lint, pinned governance, documentation, raw provenance, source queue, tests, all-owner strict validation, site consistency, exact reproduction and path-lock gates passed. This is not biological sign-off. |
| labels | passed | True | naturalproductmech:mibig-ab69cdf6e5 | Fresh configured label gate passed; warning mismatches and no-adapter skips remain nonblocking and do not certify exact chemical identity. |
| Initial full QC before statistics refresh | failed | False | naturalproductmech:mibig-ab69cdf6e5 | Initial QC correctly rejected stale README discussion coverage. The generated statistics were refreshed and qc-final reran the full gate successfully. |
| Experimental exact-product attribution | unavailable | True | naturalproductmech:mibig-ab69cdf6e5 | Previously denied primary text remains unavailable. No alternative retrieval or newly inspected experimental identity is claimed. This successor is partial. |

## Scientific And Domain Assessments

### Exact-owner repair and qualification

scope: supported. Targets: naturalproductmech:mibig-ab69cdf6e5.

Nonexact CID removed only from C26 owner; qualification states the constitutional conflict without choosing a replacement.

### Unresolved exact experimental product

identity: concern. Targets: naturalproductmech:mibig-ab69cdf6e5.

C26 versus named C27 constitution remains a confirmed blocker in #918.

### Maintained ownership and immutable history

provenance: supported. Targets: naturalproductmech:mibig-ab69cdf6e5.

Maintained source-row decision plus guarded writer and curation events; same-key re-seed preserves qualifications. All unrelated inputs and prior observations remain unchanged. Full QC verifies reproducibility, not scientific completeness.

## Findings

### F1: The stored C26 N-formyl structure is not the ferrichrome named by the record

blocker / open / confirmed; issue key: mibig-BGC0000900-compound-1-ferrichrome-constitution.

The owner and versioned MIBiG source encode C26H43N9O12 with two N-acetyl hydroxamates and one N-formyl hydroxamate, without iron. Authoritative ferrichrome is a C27 iron chelate with three N-acetyl groups; its metal-free ligand is also C27 and triacetylated. This is not merely metal dissociation, isotope choice or unspecified stereochemistry. PubChem90658043 agrees with the imported graph, but agreement among database depictions does not establish the named natural-product identity. The conflict affects exact product attribution; it does not prove this C26 molecule cannot exist or select the patent product/replacement automatically.

Disposition: Cited OPEN constitutional-conflict discussion mitigates silent reuse, but no experimentally established replacement was selected. The blocker remains open; qualification is not correction of identity or exact-product origin.

### F2: PubChem644246 is a nonexact chemical cross-reference

major / resolved / confirmed; issue key: mibig-BGC0000900-compound-1-pubchem-644246-nonexact.

The live PubChem response resolves CID644246 to GGUNGDGGXMHBMJ-HCMAANCNSA-N, C27H42FeN9O12 with explicit 55Fe and three undefined centers, not this C26 iron-free key. CID90658043 is exact for the stored graph. The nonexact CID is inherited from the complete BGC0000900:1 row; it needs its own disposition even if the larger identity conflict remains unresolved. No current owner assay is falsely attributed: the pinned assay rows are empty placeholders, not measurements.

Disposition: The row-pinned exclusion removes only nonexact CID644246 from the C26 owner, retaining CID90658043, raw provenance and all unrelated claims. The iron-55 owner retains its exact CID644246. Re-seed, strict, tests and full QC pass.

## Recommended Actions And Acceptance Checks

### A1

Establish the exact primary product before any structure migration; retain the OPEN qualification until then.

- Inspect exact product, isotope and stereochemical evidence.
- Audit all old-key joins; use supported source corrections and guarded migration only.
- Canary, strict validation, reproduction and full QC must pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml; Entire current YAML, including exact graph and append-only history | supports | Cited OPEN qualification is present. Chemistry, source concepts, conservative evidence grades and SEEDED status are unchanged. Only the nonexact CID on the C26 owner was removed. |
| prior | reviews/structured/20261013T170121Z-ferrichrome-2/review.yaml; Exact predecessor findings | supports | The immutable original remains the historical full-record assessment; this successor only assesses disposition. |
| xref-table | curation/mibig_xref_exclusions.tsv; BGC0000900:1 / pubchem:644246 | supports | Complete untouched row pin 78b115cce5a8a133196da68d8dd417a75f5a8f42aa0344a1d3c76d389e58f791 scopes the exclusion to the C26 owner; the separate iron-55 owner retains the same CID. |
| scope-proof | /private/tmp/npmech-ferrichrome-publish-i31W5V/scope-audit.json; Complete filesystem and field comparison | supports | All owner/component and review denominators preserved; no identity migration or unrelated scientific change. |
| regressions | /private/tmp/npmech-ferrichrome-publish-i31W5V/focused.log; 202 focused tests | supports | Decision pinning, exact-owner preservation, same-key-only carry-forward and durable evidence checks passed. |
| archive | reviews/evidence/20261013-ferrichrome/manifest.json; 116 retained artifacts, 13 explicit reference-only sources | supports | Evidence snapshots and source receipts survive publication without redistributing publisher/patent text. |
| chemistry | /private/tmp/npmech-ferrichrome-resume-mXOYL5/chemistry.json; RDKit2026.03.5 result ferrichrome-2 and authority comparisons; same retained capture used for scoped disposition, not a fresh network retrieval | supports | Computed C26H43N9O12, net charge 0, monoisotopic mass 673.303117816 Da; 3 specified/0 undefined tetrahedral centers; acetyl/formyl hydroxamates 2/1; iron isotope list []. Exact owner InChI/key roundtrip passed. Calculations are not measurements. Normalization is diagnostic, not authorized identity replacement. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/90658043,644246/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; PropertyTable.Properties for CID90658043 and CID644246; HTTP200 capture 2026-10-13T16:45:00.740185Z..2026-10-13T16:45:01.117565Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/pubchem-resume.json; receipt SHA256 b21e89ec88fb8064682ed966bdcddcbf7970d431e58f8fa33026a716cac9749b; same retained capture used for scoped disposition, not a fresh network retrieval | refutes | Recovered HTTP200: CID90658043 matches ZZDYFKJSJLUQON-UFYCRDLUSA-N; CID644246 matches GGUNGDGGXMHBMJ-HCMAANCNSA-N. Both formulae and exact InChIs were recomputed. Registry equivalence is not evidence for biosynthesis. |
| chebi-ferrichrome | https://www.ebi.ac.uk/chebi/backend/api/public/compound/5019/; CHEBI5019 default_structure, chemical_data, stars and definition; HTTP200 capture 2026-10-13T16:45:34.903592Z..2026-10-13T16:45:35.832294Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/CHEBI5019-resume.json; receipt SHA256 bf6c76369978dbde977d07416b9e6451269b02318a10419e24b3d807aaa704c0; same retained capture used for scoped disposition, not a fresh network retrieval | refutes | Live 3-star ferrichrome agrees with the pinned default graph: GGUNGDGGXMHBMJ-OCIDDWSYSA-N, C27H42FeN9O12, three specified peptide centers, no isotope label. Its three N-acetyl groups distinguish it from the C26 record. Representation of coordination is not interpreted as physical negative iron oxidation state. |
| chebi-deferrichrome | https://www.ebi.ac.uk/chebi/backend/api/public/compound/90132/; CHEBI90132 default_structure, chemical_data, stars and definition; HTTP200 capture 2026-10-13T16:45:56.396094Z..2026-10-13T16:45:57.051939Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/CHEBI90132-resume.json; receipt SHA256 a3cd2f780cd4c2d44ccd4d8d9332479ef56bc91c2cdd23be6fd177743bb1cf19; same retained capture used for scoped disposition, not a fresh network retrieval | refutes | Live 3-star deferrichrome agrees with pinned ZFDAUYPBCXMSBF-ACRUOGEOSA-N, C27H45N9O12, three acetyl hydroxamates and no iron. It is not the C26 form. Occurrences and roles on this nonexact candidate are not transferred. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0000900.5/annotations.json; compounds[0], taxonomy, loci, biosynthesis classes and legacy references; HTTP200 capture 2026-10-13T15:36:52.703897Z..2026-10-13T15:36:54.661079Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/BGC0000900.5.json; receipt SHA256 f2c3eee2344b4c89e4a93229867b284f06e697a9e9fd55d0e7c900f57df8e357; same retained capture used for scoped disposition, not a fresh network retrieval | supports | Exact active version5 chemistry, host and references match the raw row. Empty locus methods and 0..0 unspecified bounds are not experiments or real coordinates. OTHER is source asserted; questionable quality and placeholder reviewers are not scientific truth signals. No assertion this is the latest version. |

## Limits And Additional Notes

- Partial, scoped successor: no newly assessed owner and no native status promotion.
- Experimental product attribution remains unresolved. Earlier primary access limits remain; publication does not retry denied endpoints or declare missing evidence false.
- The exact inspected input tree is retained by review-base/ferrichrome-remediation-20261013. The full QC rerun follows the generated README count correction in c1583b769; all 17 inspected scientific and review inputs still match the tagged tree. Canonical successor checks and PR/merge-queue CI follow saving.
- Full QC preceded these new review bundles; their canonical and contract validation is separate.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T174145Z-ferrichrome-2-scoped-disposition
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'ferrichrome-2: scoped xref and exact-form qualification disposition'
started_at: '2026-10-13T17:19:53.414574Z'
finished_at: '2026-10-13T17:41:45.030084Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant implemented the changes and performed a separate
    adversarial pass; not independent human review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Resolve only F2; F1 remains open despite explicit mitigation.
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
  - path: data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml
    sha256: 2e10d2c966e68e68bfaa3c23f4a77b70f4c6ff395c0f27d0b32d6cef783b5f48
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
  - path: reviews/structured/20261013T170121Z-ferrichrome-2/review.yaml
    sha256: cc02cee96616f0746019577947bfda86e2e87bf81395e58fba21e932549d7aff
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
- target_id: naturalproductmech:mibig-ab69cdf6e5
  path: data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml
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
  - naturalproductmech:mibig-ab69cdf6e5
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
  - naturalproductmech:mibig-ab69cdf6e5
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
  - naturalproductmech:mibig-ab69cdf6e5
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
  - naturalproductmech:mibig-ab69cdf6e5
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
  - naturalproductmech:mibig-ab69cdf6e5
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
  - naturalproductmech:mibig-ab69cdf6e5
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
  - naturalproductmech:mibig-ab69cdf6e5
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
  - naturalproductmech:mibig-ab69cdf6e5
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
  - naturalproductmech:mibig-ab69cdf6e5
  summary: Fresh configured label gate passed; warning mismatches and no-adapter skips
    remain nonblocking and do not certify exact chemical identity.
  scope_note: Actual run 2026-10-13T17:18:27.442433+00:00 to 2026-10-13T17:21:28.414718+00:00;
    log SHA256 556ef5804e095767472c0aa8a542d5bff7e332470383a992e6b260103034414b
- check_id: qc-initial
  name: Initial full QC before statistics refresh
  status: failed
  required: false
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
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
  - naturalproductmech:mibig-ab69cdf6e5
  summary: Previously denied primary text remains unavailable. No alternative retrieval
    or newly inspected experimental identity is claimed. This successor is partial.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml
  locator: Entire current YAML, including exact graph and append-only history
  accessed_at: '2026-10-13T17:41:45.028592Z'
  support: supports
  summary: Cited OPEN qualification is present. Chemistry, source concepts, conservative
    evidence grades and SEEDED status are unchanged. Only the nonexact CID on the
    C26 owner was removed.
  snapshot_sha256: 2e10d2c966e68e68bfaa3c23f4a77b70f4c6ff395c0f27d0b32d6cef783b5f48
- evidence_id: prior
  kind: record_content
  reference: reviews/structured/20261013T170121Z-ferrichrome-2/review.yaml
  locator: Exact predecessor findings
  accessed_at: '2026-10-13T17:41:45.028863Z'
  support: supports
  summary: The immutable original remains the historical full-record assessment; this
    successor only assesses disposition.
  snapshot_sha256: cc02cee96616f0746019577947bfda86e2e87bf81395e58fba21e932549d7aff
- evidence_id: xref-table
  kind: record_content
  reference: curation/mibig_xref_exclusions.tsv
  locator: BGC0000900:1 / pubchem:644246
  accessed_at: '2026-10-13T17:41:45.029071Z'
  support: supports
  summary: Complete untouched row pin 78b115cce5a8a133196da68d8dd417a75f5a8f42aa0344a1d3c76d389e58f791
    scopes the exclusion to the C26 owner; the separate iron-55 owner retains the
    same CID.
  snapshot_sha256: a4627732141b210992a2bac02fc4dc24eb7edb01b810873ce0f03cdcada7b5f7
- evidence_id: scope-proof
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-publish-i31W5V/scope-audit.json
  locator: Complete filesystem and field comparison
  accessed_at: '2026-10-13T17:41:45.029174Z'
  support: supports
  summary: All owner/component and review denominators preserved; no identity migration
    or unrelated scientific change.
  snapshot_sha256: 7edb36b75199ca1dd2f893c5996daac1602103232cc44826fa7e71745cf2c645
- evidence_id: regressions
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-publish-i31W5V/focused.log
  locator: 202 focused tests
  accessed_at: '2026-10-13T17:41:45.029289Z'
  support: supports
  summary: Decision pinning, exact-owner preservation, same-key-only carry-forward
    and durable evidence checks passed.
  snapshot_sha256: a20569d547a7ce95d033903421694d2010e640b2ebf26acd6d92ede3c3171fe6
- evidence_id: archive
  kind: validation
  reference: reviews/evidence/20261013-ferrichrome/manifest.json
  locator: 116 retained artifacts, 13 explicit reference-only sources
  accessed_at: '2026-10-13T17:41:45.029371Z'
  support: supports
  summary: Evidence snapshots and source receipts survive publication without redistributing
    publisher/patent text.
  snapshot_sha256: efc55cc93e8ab57c4e5923c5c0c2fae7edd77c2b794cf990331d22db56fd8792
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-resume-mXOYL5/chemistry.json
  locator: RDKit2026.03.5 result ferrichrome-2 and authority comparisons; same retained
    capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.029618Z'
  support: supports
  summary: Computed C26H43N9O12, net charge 0, monoisotopic mass 673.303117816 Da;
    3 specified/0 undefined tetrahedral centers; acetyl/formyl hydroxamates 2/1; iron
    isotope list []. Exact owner InChI/key roundtrip passed. Calculations are not
    measurements. Normalization is diagnostic, not authorized identity replacement.
  snapshot_sha256: dbc9e4241c6a271fa92a0dfb53f35e16a0c8d8159e6f4f8a7538a9dd435c9014
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/90658043,644246/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: PropertyTable.Properties for CID90658043 and CID644246; HTTP200 capture
    2026-10-13T16:45:00.740185Z..2026-10-13T16:45:01.117565Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/pubchem-resume.json;
    receipt SHA256 b21e89ec88fb8064682ed966bdcddcbf7970d431e58f8fa33026a716cac9749b;
    same retained capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.029636Z'
  support: refutes
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
  accessed_at: '2026-10-13T17:41:45.029648Z'
  support: refutes
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
  accessed_at: '2026-10-13T17:41:45.029659Z'
  support: refutes
  summary: Live 3-star deferrichrome agrees with pinned ZFDAUYPBCXMSBF-ACRUOGEOSA-N,
    C27H45N9O12, three acetyl hydroxamates and no iron. It is not the C26 form. Occurrences
    and roles on this nonexact candidate are not transferred.
  snapshot_sha256: 43a98c9dc374a79365dd55e6e19bf19f36ac8a29162ee1f2065607e30289d215
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000900.5/annotations.json
  locator: compounds[0], taxonomy, loci, biosynthesis classes and legacy references;
    HTTP200 capture 2026-10-13T15:36:52.703897Z..2026-10-13T15:36:54.661079Z; payload
    /private/tmp/npmech-ferrichrome-review-W2MXlZ/BGC0000900.5.json; receipt SHA256
    f2c3eee2344b4c89e4a93229867b284f06e697a9e9fd55d0e7c900f57df8e357; same retained
    capture used for scoped disposition, not a fresh network retrieval
  accessed_at: '2026-10-13T17:41:45.029668Z'
  support: supports
  summary: Exact active version5 chemistry, host and references match the raw row.
    Empty locus methods and 0..0 unspecified bounds are not experiments or real coordinates.
    OTHER is source asserted; questionable quality and placeholder reviewers are not
    scientific truth signals. No assertion this is the latest version.
  snapshot_sha256: 4f198d7a4a3a2c50ca51aebd288d948e9eff7c7abd9eceead7ae5f6c24193d80
assessments:
- assessment_id: scoped-repair
  area: scope
  topic: Exact-owner repair and qualification
  outcome: supported
  summary: Nonexact CID removed only from C26 owner; qualification states the constitutional
    conflict without choosing a replacement.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - pubchem
  - xref-table
  - regressions
- assessment_id: identity-limit
  area: identity
  topic: Unresolved exact experimental product
  outcome: concern
  summary: 'C26 versus named C27 constitution remains a confirmed blocker in #918.'
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
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
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - scope-proof
  - archive
  - regressions
findings:
- finding_id: F1
  issue_key: mibig-BGC0000900-compound-1-ferrichrome-constitution
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The stored C26 N-formyl structure is not the ferrichrome named by the record
  description: The owner and versioned MIBiG source encode C26H43N9O12 with two N-acetyl
    hydroxamates and one N-formyl hydroxamate, without iron. Authoritative ferrichrome
    is a C27 iron chelate with three N-acetyl groups; its metal-free ligand is also
    C27 and triacetylated. This is not merely metal dissociation, isotope choice or
    unspecified stereochemistry. PubChem90658043 agrees with the imported graph, but
    agreement among database depictions does not establish the named natural-product
    identity. The conflict affects exact product attribution; it does not prove this
    C26 molecule cannot exist or select the patent product/replacement automatically.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  field_paths:
  - label
  - chemical_structure
  - biosynthesis_origin
  - producer_organisms
  - biosynthetic_gene_clusters
  evidence_ids:
  - owner
  - prior
  - chemistry
  - pubchem
  - scope-proof
  - regressions
  - chebi-ferrichrome
  - chebi-deferrichrome
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
  rule_id: review-checklist:Identity/Structure; docs/HARMONIZATION.md:The unit of
    the corpus is a structure
  native_severity: blocker
  normalization_reason: A confirmed constitution/name conflict makes the individual-structure
    record denote the wrong named molecule.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T170121Z-ferrichrome-2
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/918
  disposition_reason: Cited OPEN constitutional-conflict discussion mitigates silent
    reuse, but no experimentally established replacement was selected. The blocker
    remains open; qualification is not correction of identity or exact-product origin.
- finding_id: F2
  issue_key: mibig-BGC0000900-compound-1-pubchem-644246-nonexact
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: PubChem644246 is a nonexact chemical cross-reference
  description: 'The live PubChem response resolves CID644246 to GGUNGDGGXMHBMJ-HCMAANCNSA-N,
    C27H42FeN9O12 with explicit 55Fe and three undefined centers, not this C26 iron-free
    key. CID90658043 is exact for the stored graph. The nonexact CID is inherited
    from the complete BGC0000900:1 row; it needs its own disposition even if the larger
    identity conflict remains unresolved. No current owner assay is falsely attributed:
    the pinned assay rows are empty placeholders, not measurements.'
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  field_paths:
  - xrefs[1]
  evidence_ids:
  - owner
  - prior
  - chemistry
  - pubchem
  - scope-proof
  - regressions
  - xref-table
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Implemented complete-row-pinned literal xref exclusion
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Untouched versioned source compound, producer and locus row
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG source extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated identity and source harmonization
  rule_id: review-checklist:Equivalence; docs/HARMONIZATION.md:an xref means the same
    structure
  native_severity: major
  normalization_reason: A false exact-equivalence edge changes downstream structure
    joins without independently selecting the correct product identity.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T170121Z-ferrichrome-2
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/919
  disposition_reason: The row-pinned exclusion removes only nonexact CID644246 from
    the C26 owner, retaining CID90658043, raw provenance and all unrelated claims.
    The iron-55 owner retains its exact CID644246. Re-seed, strict, tests and full
    QC pass.
actions:
- action_id: A1
  description: Establish the exact primary product before any structure migration;
    retain the OPEN qualification until then.
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
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
  acceptance_checks:
  - Inspect exact product, isotope and stereochemical evidence.
  - Audit all old-key joins; use supported source corrections and guarded migration
    only.
  - Canary, strict validation, reproduction and full QC must pass.
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
  review_id: 20261013T170121Z-ferrichrome-2
  relationship: Scoped disposition; original full assessment remains immutable.
links:
- https://github.com/CultureBotAI/NaturalProductMech/pull/917
```
