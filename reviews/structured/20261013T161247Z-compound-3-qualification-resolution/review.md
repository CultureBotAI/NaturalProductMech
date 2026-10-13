# Compound 3: scoped proposed-identity and producer-strain resolution

- Review: 20261013T161247Z-compound-3-qualification-resolution
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T15:58:47.110462Z
- Finished UTC: 2026-10-13T16:12:47.324159Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Resolve only predecessor F1/F2: preserve proposed-structure confidence and exact APC1.2 isolate context. Experimental identity remains unresolved, all other owner claims are unchanged, and native status stays SEEDED.

## Scope And Provenance

One exact owner, bounded disposition of predecessor F1/F2; full campaign remains 3115 owners and 243 components.

Selection: User-authorized PR remediation of the two confirmed findings.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 247fb8a3a3f1b91ffed18a53a273c7f36ccc776e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-0dd7b68dcd | data/natural_products/amino_acids_and_peptides/compound-3.yaml | generated | compound 3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| focused-fixed | passed | True | naturalproductmech:mibig-0dd7b68dcd | 185 focused tests passed, including strain scoping and same-key discussion carry-forward. |
| archive-tests | passed | True | naturalproductmech:mibig-0dd7b68dcd | Five curation/archive tests passed, including every historical evidence digest and campaign denominator. |
| strict | passed | True | naturalproductmech:mibig-0dd7b68dcd | The changed owner passed strict closed-schema validation with zero errors. |
| reseed | passed | True | naturalproductmech:mibig-0dd7b68dcd | One exact-owner re-seed reported one unchanged record; the captured owner hash remains identical. |
| scope-audit | passed | True | naturalproductmech:mibig-0dd7b68dcd | Only the intended owner changed; all other 3114 owners, 243 components and 29 prior observations are byte-identical. |
| qc | passed | True | naturalproductmech:mibig-0dd7b68dcd | Full native QC passed: 745 tests passed, 4 skipped, 2 dependency warnings; lint, pinned governance, documentation, raw provenance, source queue, all-owner strict validation, site, exact reproduction and path lock passed. The optional governance-network check separately passed on retry. |
| labels | passed | True | naturalproductmech:mibig-0dd7b68dcd | Fresh configured label gate passed. Existing warning mismatches and no-adapter skips are not chemical identity certification. |
| governance-network | passed | True | naturalproductmech:mibig-0dd7b68dcd | The focused optional network snapshot test passed on retry (1 passed); the full suite receipt retains its original skip count. |
| qualify | failed | False | naturalproductmech:mibig-0dd7b68dcd | Initial guarded write was rejected because discussion references do not accept evidence_type; no invalid record was written. Corrected to SupportingReference.evidence_source. |
| focused | failed | False | naturalproductmech:mibig-0dd7b68dcd | The initial regression run found the missing discussion after the rejected write. Superseded by focused-fixed after the schema-correct guarded write. |

## Scientific And Domain Assessments

### Proposed identity is visibly qualified

evidence: supported. Targets: naturalproductmech:mibig-0dd7b68dcd.

The discussion states that the molecular graph is proposed, not definitively elucidated, distinguishes composition/backbone support from full connectivity and stereochemistry, and cites the exact primary source. F1 is resolved without claiming a replacement structure.

### Exact experimental isolate context

scope: supported. Targets: naturalproductmech:mibig-0dd7b68dcd.

APC1.2 (CCOS978) matches the paper and source accession. The qualification is pinned to BGC0002321:4 and does not upgrade the species taxon, cluster host or correlation grades. F2 is resolved.

### Experimental identity remains proposed

identity: unknown. Targets: naturalproductmech:mibig-0dd7b68dcd.

This disposition repairs confidence wording, not experimental elucidation. The two stereocenters remain unspecified and full connectivity is not experimentally settled. No native REVIEWED status is warranted by the fixes.

### Ownership, audit and unchanged scientific scope

provenance: supported. Targets: naturalproductmech:mibig-0dd7b68dcd.

Native seeding adds the strain through its maintained consumer; the discussion uses the guarded writer with a codex-attributed event. All unrelated fields, owners and components remain unchanged. Current full QC is deterministic verification, not an all-corpus scientific assessment.

## Findings

### F1: The proposed chemical identity lacks its primary-source qualification

major / resolved / confirmed; issue key: compound3-BGC0002321-proposed-structure-unqualified.

The owner preserves a definite molecular graph but its only discussion concerns naming. The source identifies compound3 as a proposed di-N-hydroxylated intermediate/shunt product; Figure2 marks its structure as proposed and S4 supports composition/backbone rather than definitive connectivity. MIBiG attribution and stereo_complete:false do not communicate this separate constitutional uncertainty. Add an explicit cited qualification; this finding does not establish a different correct structure or justify deleting the owner.

Disposition: The cited curator-owned discussion now preserves the primary source proposed-identity limitation. Same-key reseed, strict validation, regression tests, rendered page and full QC pass. This closes the missing qualification, not the experimental identity question.

### F2: The experimentally named APC1.2 strain is omitted

minor / resolved / confirmed; issue key: compound3-BGC0002321-missing-APC1-2-strain.

PMID31081214 methods identify APC1.2(CCOS978), and CP034458.1 names strain APC1.2. The producer uses species-rank NCBITaxon2163413 without a strain field. Retain the isolate context without changing the taxon ID, grading, BGC host or proposed structural assignment.

Disposition: The complete-row-pinned maintained decision now emits APC1.2 (CCOS978) with separate curator evidence. Source chemistry, taxon, native grade and all unrelated owners/components are unchanged. Reproduction and full QC pass; the omission is fixed without inferring species-wide production.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/amino_acids_and_peptides/compound-3.yaml; Complete current raw YAML and resolved owner, including all audit events | supports | Exactly one species-rank producer now carries APC1.2 (CCOS978) and separate curator evidence. The OPEN curator discussion explicitly qualifies the proposed structure. Chemistry, source concepts, both correlated evidence grades and SEEDED status remain unchanged. No graphs, occurrences, pure-compound activities or other optional biological claims were added. |
| prior | reviews/structured/20261013T152822Z-compound-3/review.yaml; F1 and F2, exact issue keys and source scope | supports | Original immutable assessment with one major qualification defect and one minor strain omission. |
| strain-table | curation/mibig_producer_strains.tsv; BGC0002321:4, complete source row SHA256 80d41d4998165dd6b2d6796304411bc824c7fda7c7f11d20a20ead4f36cc7817 | supports | Maintained qualification names the WT isolate, retains the taxon and evidence grade, and distinguishes W8/complemented derivatives. |
| paper | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6851878/fullTextXML; PMID31081214; DOI10.1111/mmi.14272; PMC6851878; Results compound analysis, PUL transcription and SNF2 complementation, Discussion and Experimental Procedures; captured 2026-10-13T15:03:30.715087Z; local payload /private/tmp/npmech-compound3-review-2EX0Ug/paper31081214.xml; same retained source capture re-inspected for this scoped disposition, not a new network retrieval | supports | APC1.2(CCOS978) wild type, W8(CCOS1866) spontaneous snf2 mutant and complemented derivatives were studied. The paper properly designates the isolate M.aff.pulcherrima. Compound3 is proposed as a di-N-hydroxylated cyclodileucine intermediate or shunt product, not a fully characterized identity. UPLC-HR-HESI-MS and isotope feeding support C12H22N2O4 and a two-leucine-derived backbone. Reduced PUL transcripts and restored compound secretion after SNF2 complementation support correlation at the PUL locus, not a direct PUL-gene knockout. The antifungal assays compare whole yeast cells, not purified compound3. |
| figure | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6851878/supplementaryFiles; Figure2B, bottom compound3 structure and question mark; Figure2A, WT/W8/complemented chromatograms; same retained source capture re-inspected for this scoped disposition, not a new network retrieval | supports | Visually inspected proposed connectivity has two carbonyls, two N-hydroxyls and two isobutyl substituents without assigned stereochemistry, matching the stored graph. Caption reports compound3 m/z259.165[M+H]+ and C12H22N2O4. The panel and accompanying text qualify the identity as proposed. |
| supplement | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6851878/supplementaryFiles; Supplemental FiguresS1-S6 text; S4 spectra on PDFpages5-6 and S5/S6 on pages8-9 visually inspected; same retained source capture re-inspected for this scoped disposition, not a new network retrieval | supports | S3 compares a synthetic standard for compound1, not compound3. S4 compound3 spectra support incorporation of two leucine carbon backbones; neither mass shifts nor formula determine all bond positions or stereochemistry. S5/S6 localize the regulatory mutation to SNF2/MPUL0C08850 and document random-genomic complementation, not perturbation of the PUL cluster. |
| genome | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=CP034458.1&amp;seq_start=1429481&amp;seq_stop=1436146&amp;rettype=gbwithparts&amp;retmode=xml; GBSeq and source/CDS features within the exact requested BGC interval; returned coordinates are rebased to the window; captured 2026-10-13T15:06:10.688465Z; local payload /private/tmp/npmech-compound3-review-2EX0Ug/CP034458.1-region.xml; same retained source capture re-inspected for this scoped disposition, not a new network retrieval | supports | CP034458.1 interval1429481..1436146 is 6666nt, chromosomeIII, strain APC1.2. CDS annotations connect MPUL0C04960/70/80/90 to Pul3/4/2/1 and QBM88525.1..QBM88528.1. These are contextual mappings, not new native protein assertions. |
| scope-proof | /private/tmp/npmech-compound3-pr-4lLMj6/scope-audit.json; Ignored-inclusive complete filesystem hash comparison | supports | The only scientific delta is the strain qualifier/evidence, proposed-identity discussion and two audit events. All 3115 owners and 243 components remain in scope; all 29 historical review pairs are immutable. |
| archive | reviews/evidence/20261013-compound3/manifest.json; All three historical observations and every snapshot mapping | supports | 121 compressed artifacts preserve local receipts, computations and full checkpoint. Eleven publisher-derived artifacts remain explicitly reference-only; no blocked paper was retried. Tests verify bytes and mapping. |
| regressions | /private/tmp/npmech-compound3-pr-4lLMj6/focused-fixed.log; 185 focused tests | supports | Exact source pin, unchanged imported claims, retained incomplete stereochemistry and grade, cited discussion and carry-forward limited to the same key all pass. |

## Limits And Additional Notes

- Scoped partial successor, not a new whole-record scientific pass. The original full assessment remains historical; this observation adds no newly assessed owner.
- The proposed connectivity and unresolved stereochemistry remain explicit. No direct PUL-gene experiment or purified-compound antifungal activity is inferred.
- The two other paper-local Compound 3 owners remain partial and distinct; their publisher 403 limits and all 195 campaign access limitations are retained.
- Source state is git_commit: all 23 captured inputs were checked against the exact tagged implementation commit. The provenance tag is retained across the required squash merge.
- The initial failed guarded write and regression run are retained as superseded attempts, not hidden successes. Canonical successor checks and final PR/merge-queue CI follow persistence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T161247Z-compound-3-qualification-resolution
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Compound 3: scoped proposed-identity and producer-strain resolution'
started_at: '2026-10-13T15:58:47.110462Z'
finished_at: '2026-10-13T16:12:47.324159Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant implemented and separately adversarially checked
    the changes; not independent human review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: 'Resolve only predecessor F1/F2: preserve proposed-structure confidence and
  exact APC1.2 isolate context. Experimental identity remains unresolved, all other
  owner claims are unchanged, and native status stays SEEDED.'
source:
  git_revision: 247fb8a3a3f1b91ffed18a53a273c7f36ccc776e
  state: git_commit
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 20bad44941e6634deadcb4afc20445db5f439fe1b5cd6ebf57306bb3c031a115
    role: context
  - path: data/natural_products/amino_acids_and_peptides/compound-3.yaml
    sha256: b1dea24c1261381cd4f6c7787972b18e7df08ad1c73a1c70dfb012768cd030ad
    role: target
  - path: data/raw/mibig_compounds.tsv
    sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
    role: context
  - path: data/raw/npclassifier.tsv
    sha256: 7b9b9f78f5b14aea9fabb163bbaa9e842920a7e9b07deac8f98c97666e9e23fc
    role: context
  - path: docs/CURATION.md
    sha256: 245df036e09a00a2f92a5f78c70eadb210cef7d70046e8ee35377a9e636cd30b
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
  - path: pages/amino_acids_and_peptides/compound-3.html
    sha256: 158c071c11a2178129a33046c9efdc2511ddf17d1008204b2d93b37e649fdf94
    role: context
  - path: reviews/evidence/20261013-compound3/artifacts/CP034458.1-region.xml.gz
    sha256: a48f8d3716386c3f93894bf2d2e223b79d3a72cfd14edf4c6970f3cefa1926e7
    role: context
  - path: reviews/evidence/20261013-compound3/artifacts/chemistry.json.gz
    sha256: ecd4475583f35ee62c41aaa487cddb1987250c895d2e6e08bdf62a5620b5b07c
    role: context
  - path: reviews/evidence/20261013-compound3/manifest.json
    sha256: 2823f78191ddb2f60730eda96c168e5b52e9da6702d3b94fad4a7c934bebf205
    role: context
  - path: reviews/structured/20261013T152822Z-compound-3/review.yaml
    sha256: d6a3c0c88e4275114f84ae1dfb9fd9ecdb79d46ef544b4bc564661af58971273
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 8d82d7633e0492e9fe16011f6e5af6f8024f573e80c8a24176b65e2941478b71
    role: context
  - path: src/naturalproductmech/curate/curation_event.py
    sha256: dd39419502a9a7acf40e134a7642c5e310808cea33708eef300c62ba76dad6a5
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: 6026ddca19f0989d499b1681f7724fbab23918de8d3957750b49bbfe1a9c0bff
    role: context
  - path: src/naturalproductmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: src/naturalproductmech/validation/write_validated.py
    sha256: eb35df21c03c2e6272e665ea4d179f870a1ec6db61d52939058add44a0edde7f
    role: context
  - path: tests/test_compound3_curation.py
    sha256: 0455a48e25ec56f5d5fa141c3318fee860e47a7885ee75cab36f6c42f7acd785
    role: context
  - path: tests/test_compound3_review_archive.py
    sha256: ab119d39e5217f486452d0fab7d71de20f39033aeb52768f45826e8f61651e05
    role: context
targets:
- target_id: naturalproductmech:mibig-0dd7b68dcd
  path: data/natural_products/amino_acids_and_peptides/compound-3.yaml
  label: compound 3
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
    role: Implemented complete-row-pinned literal PubChem and NPAtlas exclusions;
      no decision applies here
scope:
  description: One exact owner, bounded disposition of predecessor F1/F2; full campaign
    remains 3115 owners and 243 components.
  selection: User-authorized PR remediation of the two confirmed findings.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  exclusions:
  - target: Other 3114 owners and prior scientific limitations
    reason: No new assessment or scope reduction; all previous observations are retained.
checks:
- check_id: focused-fixed
  name: focused-fixed
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_compound3_curation.py tests/test_producer_strains.py
    tests/test_seed_skeleton.py tests/test_render_pages.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  summary: 185 focused tests passed, including strain scoping and same-key discussion
    carry-forward.
  scope_note: Actual run 2026-10-13T15:54:50.887563Z to 2026-10-13T15:54:55.570679Z;
    log SHA256 1b239f23c81d1b84367506523a732c0cb67b7485ddb7102cc810eed294ada5b6
- check_id: archive-tests
  name: archive-tests
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_compound3_review_archive.py tests/test_compound3_curation.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  summary: Five curation/archive tests passed, including every historical evidence
    digest and campaign denominator.
  scope_note: Actual run 2026-10-13T15:56:33.609437Z to 2026-10-13T15:56:37.551799Z;
    log SHA256 ae5fba65d921fdac1d07df2d4c0621785efbaf2180961712ad6328bf7b56e222
- check_id: strict
  name: strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/natural_products/amino_acids_and_peptides/compound-3.yaml
    --out /private/tmp/npmech-compound3-pr-4lLMj6/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  summary: The changed owner passed strict closed-schema validation with zero errors.
  scope_note: Actual run 2026-10-13T15:57:04.991900Z to 2026-10-13T15:57:10.596361Z;
    log SHA256 2fc9884ca6d4eed9cee8c2ef401c8e316ab39e692caff391241d800baf4b9315
- check_id: reseed
  name: reseed
  status: passed
  required: true
  command: .venv/bin/python scripts/seed_from_sources.py --apply --only naturalproductmech:mibig-0dd7b68dcd
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  summary: One exact-owner re-seed reported one unchanged record; the captured owner
    hash remains identical.
  scope_note: Actual run 2026-10-13T15:57:22.602765Z to 2026-10-13T15:57:26.233777Z;
    log SHA256 67e92562fe50792bab3f0f4aac51f3fb0afa9d85dd044b9cfbde8fbb6bdc6d39
- check_id: scope-audit
  name: scope-audit
  status: passed
  required: true
  command: .venv/bin/python /private/tmp/npmech-compound3-pr-4lLMj6/scope_audit.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  summary: Only the intended owner changed; all other 3114 owners, 243 components
    and 29 prior observations are byte-identical.
  scope_note: Actual run 2026-10-13T15:57:03.753239Z to 2026-10-13T15:57:05.082663Z;
    log SHA256 2845f3c8205bee011094e8720964800b099c742034554d69ef553459c4c53bb4
- check_id: qc
  name: qc
  status: passed
  required: true
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  summary: 'Full native QC passed: 745 tests passed, 4 skipped, 2 dependency warnings;
    lint, pinned governance, documentation, raw provenance, source queue, all-owner
    strict validation, site, exact reproduction and path lock passed. The optional
    governance-network check separately passed on retry.'
  scope_note: Actual run 2026-10-13T15:58:18.162764Z to 2026-10-13T16:12:35.642216Z;
    log SHA256 78c1d36441ce61891cb7eac6b885ce4c82d0b7733f6c99db9071f1a5cb9c1e33
- check_id: labels
  name: labels
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  summary: Fresh configured label gate passed. Existing warning mismatches and no-adapter
    skips are not chemical identity certification.
  scope_note: Actual run 2026-10-13T15:59:21.452345Z to 2026-10-13T16:00:59.167782Z;
    log SHA256 556ef5804e095767472c0aa8a542d5bff7e332470383a992e6b260103034414b
- check_id: governance-network
  name: governance-network
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q -rs tests/test_vendored_artifacts.py::test_snapshot_matches_claw_at_the_pin
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  summary: The focused optional network snapshot test passed on retry (1 passed);
    the full suite receipt retains its original skip count.
  scope_note: Actual run 2026-10-13T16:08:06.910830Z to 2026-10-13T16:08:08.967049Z;
    log SHA256 016a4093788648644b08006f7d1d171ca7639313677f5aa929f004d4a3e52465
- check_id: qualify
  name: qualify
  status: failed
  required: false
  command: .venv/bin/python /private/tmp/npmech-compound3-pr-4lLMj6/qualify_structure.py
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  summary: Initial guarded write was rejected because discussion references do not
    accept evidence_type; no invalid record was written. Corrected to SupportingReference.evidence_source.
- check_id: focused
  name: focused
  status: failed
  required: false
  command: .venv/bin/python -m pytest -q tests/test_compound3_curation.py tests/test_producer_strains.py
    tests/test_seed_skeleton.py tests/test_render_pages.py
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  summary: The initial regression run found the missing discussion after the rejected
    write. Superseded by focused-fixed after the schema-correct guarded write.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/amino_acids_and_peptides/compound-3.yaml
  locator: Complete current raw YAML and resolved owner, including all audit events
  accessed_at: '2026-10-13T16:12:47.322792Z'
  support: supports
  summary: Exactly one species-rank producer now carries APC1.2 (CCOS978) and separate
    curator evidence. The OPEN curator discussion explicitly qualifies the proposed
    structure. Chemistry, source concepts, both correlated evidence grades and SEEDED
    status remain unchanged. No graphs, occurrences, pure-compound activities or other
    optional biological claims were added.
  snapshot_sha256: b1dea24c1261381cd4f6c7787972b18e7df08ad1c73a1c70dfb012768cd030ad
- evidence_id: prior
  kind: record_content
  reference: reviews/structured/20261013T152822Z-compound-3/review.yaml
  locator: F1 and F2, exact issue keys and source scope
  accessed_at: '2026-10-13T16:12:47.323205Z'
  support: supports
  summary: Original immutable assessment with one major qualification defect and one
    minor strain omission.
  snapshot_sha256: d6a3c0c88e4275114f84ae1dfb9fd9ecdb79d46ef544b4bc564661af58971273
- evidence_id: strain-table
  kind: record_content
  reference: curation/mibig_producer_strains.tsv
  locator: BGC0002321:4, complete source row SHA256 80d41d4998165dd6b2d6796304411bc824c7fda7c7f11d20a20ead4f36cc7817
  accessed_at: '2026-10-13T16:12:47.323306Z'
  support: supports
  summary: Maintained qualification names the WT isolate, retains the taxon and evidence
    grade, and distinguishes W8/complemented derivatives.
  snapshot_sha256: 20bad44941e6634deadcb4afc20445db5f439fe1b5cd6ebf57306bb3c031a115
- evidence_id: paper
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6851878/fullTextXML
  locator: PMID31081214; DOI10.1111/mmi.14272; PMC6851878; Results compound analysis,
    PUL transcription and SNF2 complementation, Discussion and Experimental Procedures;
    captured 2026-10-13T15:03:30.715087Z; local payload /private/tmp/npmech-compound3-review-2EX0Ug/paper31081214.xml;
    same retained source capture re-inspected for this scoped disposition, not a new
    network retrieval
  accessed_at: '2026-10-13T16:12:47.323334Z'
  support: supports
  summary: APC1.2(CCOS978) wild type, W8(CCOS1866) spontaneous snf2 mutant and complemented
    derivatives were studied. The paper properly designates the isolate M.aff.pulcherrima.
    Compound3 is proposed as a di-N-hydroxylated cyclodileucine intermediate or shunt
    product, not a fully characterized identity. UPLC-HR-HESI-MS and isotope feeding
    support C12H22N2O4 and a two-leucine-derived backbone. Reduced PUL transcripts
    and restored compound secretion after SNF2 complementation support correlation
    at the PUL locus, not a direct PUL-gene knockout. The antifungal assays compare
    whole yeast cells, not purified compound3.
  snapshot_sha256: 00573c7671713b66848a385e87ec0361761213736bd51f24d89e5456056c88f3
- evidence_id: figure
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6851878/supplementaryFiles
  locator: Figure2B, bottom compound3 structure and question mark; Figure2A, WT/W8/complemented
    chromatograms; same retained source capture re-inspected for this scoped disposition,
    not a new network retrieval
  accessed_at: '2026-10-13T16:12:47.323350Z'
  support: supports
  summary: Visually inspected proposed connectivity has two carbonyls, two N-hydroxyls
    and two isobutyl substituents without assigned stereochemistry, matching the stored
    graph. Caption reports compound3 m/z259.165[M+H]+ and C12H22N2O4. The panel and
    accompanying text qualify the identity as proposed.
  snapshot_sha256: 7a01582311881e378a41e0275cddafd2c01e2af7ab44406ea206b2529f79a0cf
- evidence_id: supplement
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6851878/supplementaryFiles
  locator: Supplemental FiguresS1-S6 text; S4 spectra on PDFpages5-6 and S5/S6 on
    pages8-9 visually inspected; same retained source capture re-inspected for this
    scoped disposition, not a new network retrieval
  accessed_at: '2026-10-13T16:12:47.323363Z'
  support: supports
  summary: S3 compares a synthetic standard for compound1, not compound3. S4 compound3
    spectra support incorporation of two leucine carbon backbones; neither mass shifts
    nor formula determine all bond positions or stereochemistry. S5/S6 localize the
    regulatory mutation to SNF2/MPUL0C08850 and document random-genomic complementation,
    not perturbation of the PUL cluster.
  snapshot_sha256: c8b7e8430a74e2ff825a82c21e4930e2d9e0bc96b862424cc78f6b3094d0c85d
- evidence_id: genome
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=CP034458.1&seq_start=1429481&seq_stop=1436146&rettype=gbwithparts&retmode=xml
  locator: GBSeq and source/CDS features within the exact requested BGC interval;
    returned coordinates are rebased to the window; captured 2026-10-13T15:06:10.688465Z;
    local payload /private/tmp/npmech-compound3-review-2EX0Ug/CP034458.1-region.xml;
    same retained source capture re-inspected for this scoped disposition, not a new
    network retrieval
  accessed_at: '2026-10-13T16:12:47.323373Z'
  support: supports
  summary: CP034458.1 interval1429481..1436146 is 6666nt, chromosomeIII, strain APC1.2.
    CDS annotations connect MPUL0C04960/70/80/90 to Pul3/4/2/1 and QBM88525.1..QBM88528.1.
    These are contextual mappings, not new native protein assertions.
  snapshot_sha256: b83cbe3ffd264cfa2e48463a794c4bf7f79077ea021211ecf4e7ed6f525aa7d7
- evidence_id: scope-proof
  kind: validation
  reference: /private/tmp/npmech-compound3-pr-4lLMj6/scope-audit.json
  locator: Ignored-inclusive complete filesystem hash comparison
  accessed_at: '2026-10-13T16:12:47.323472Z'
  support: supports
  summary: The only scientific delta is the strain qualifier/evidence, proposed-identity
    discussion and two audit events. All 3115 owners and 243 components remain in
    scope; all 29 historical review pairs are immutable.
  snapshot_sha256: 622f0948a4c0aa859ae4e679a7d9beb116b21001d043a91b2c93ea29302eb2fd
- evidence_id: archive
  kind: validation
  reference: reviews/evidence/20261013-compound3/manifest.json
  locator: All three historical observations and every snapshot mapping
  accessed_at: '2026-10-13T16:12:47.323721Z'
  support: supports
  summary: 121 compressed artifacts preserve local receipts, computations and full
    checkpoint. Eleven publisher-derived artifacts remain explicitly reference-only;
    no blocked paper was retried. Tests verify bytes and mapping.
  snapshot_sha256: 2823f78191ddb2f60730eda96c168e5b52e9da6702d3b94fad4a7c934bebf205
- evidence_id: regressions
  kind: validation
  reference: /private/tmp/npmech-compound3-pr-4lLMj6/focused-fixed.log
  locator: 185 focused tests
  accessed_at: '2026-10-13T16:12:47.323812Z'
  support: supports
  summary: Exact source pin, unchanged imported claims, retained incomplete stereochemistry
    and grade, cited discussion and carry-forward limited to the same key all pass.
  snapshot_sha256: 1b239f23c81d1b84367506523a732c0cb67b7485ddb7102cc810eed294ada5b6
assessments:
- assessment_id: qualification
  area: evidence
  topic: Proposed identity is visibly qualified
  outcome: supported
  summary: The discussion states that the molecular graph is proposed, not definitively
    elucidated, distinguishes composition/backbone support from full connectivity
    and stereochemistry, and cites the exact primary source. F1 is resolved without
    claiming a replacement structure.
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  evidence_ids:
  - owner
  - paper
  - figure
  - supplement
  - regressions
- assessment_id: strain
  area: scope
  topic: Exact experimental isolate context
  outcome: supported
  summary: APC1.2 (CCOS978) matches the paper and source accession. The qualification
    is pinned to BGC0002321:4 and does not upgrade the species taxon, cluster host
    or correlation grades. F2 is resolved.
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  evidence_ids:
  - owner
  - paper
  - genome
  - strain-table
  - regressions
- assessment_id: unresolved-identity
  area: identity
  topic: Experimental identity remains proposed
  outcome: unknown
  summary: This disposition repairs confidence wording, not experimental elucidation.
    The two stereocenters remain unspecified and full connectivity is not experimentally
    settled. No native REVIEWED status is warranted by the fixes.
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  evidence_ids:
  - owner
  - paper
  - figure
  - supplement
- assessment_id: preserved-scope
  area: provenance
  topic: Ownership, audit and unchanged scientific scope
  outcome: supported
  summary: Native seeding adds the strain through its maintained consumer; the discussion
    uses the guarded writer with a codex-attributed event. All unrelated fields, owners
    and components remain unchanged. Current full QC is deterministic verification,
    not an all-corpus scientific assessment.
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  evidence_ids:
  - owner
  - scope-proof
  - archive
  - regressions
findings:
- finding_id: F1
  issue_key: compound3-BGC0002321-proposed-structure-unqualified
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: The proposed chemical identity lacks its primary-source qualification
  description: The owner preserves a definite molecular graph but its only discussion
    concerns naming. The source identifies compound3 as a proposed di-N-hydroxylated
    intermediate/shunt product; Figure2 marks its structure as proposed and S4 supports
    composition/backbone rather than definitive connectivity. MIBiG attribution and
    stereo_complete:false do not communicate this separate constitutional uncertainty.
    Add an explicit cited qualification; this finding does not establish a different
    correct structure or justify deleting the owner.
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  field_paths:
  - chemical_structure
  - discussions
  evidence_ids:
  - owner
  - paper
  - figure
  - supplement
  - regressions
  - scope-proof
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/compound-3.yaml
    role: Only curator-prefixed discussion content is a maintained curator input;
      chemical_structure remains seeder-owned
  - repository: CultureBotAI/NaturalProductMech
    path: docs/CURATION.md
    role: Guarded discussion carry-forward and curation-event contract
  rule_id: review-checklist:Structure; review-checklist:Discussions; docs/CURATION.md:Preserve
    disagreement
  native_severity: major
  normalization_reason: The omitted evidence status materially overstates confidence
    in exact chemical identity. It is not a blocker because the stored graph matches
    the proposed source figure and wrong connectivity has not been proved.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T152822Z-compound-3
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/914
  disposition_reason: The cited curator-owned discussion now preserves the primary
    source proposed-identity limitation. Same-key reseed, strict validation, regression
    tests, rendered page and full QC pass. This closes the missing qualification,
    not the experimental identity question.
- finding_id: F2
  issue_key: compound3-BGC0002321-missing-APC1-2-strain
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: The experimentally named APC1.2 strain is omitted
  description: PMID31081214 methods identify APC1.2(CCOS978), and CP034458.1 names
    strain APC1.2. The producer uses species-rank NCBITaxon2163413 without a strain
    field. Retain the isolate context without changing the taxon ID, grading, BGC
    host or proposed structural assignment.
  target_ids:
  - naturalproductmech:mibig-0dd7b68dcd
  field_paths:
  - producer_organisms[0].strain
  evidence_ids:
  - owner
  - paper
  - genome
  - strain-table
  - regressions
  - scope-proof
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented complete-source-row-pinned strain qualification
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Validated strain decision consumer
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Guarded generated producer emission
  rule_id: review-checklist:Producer organisms
  native_severity: minor
  normalization_reason: 'A bounded provenance omission: the source taxon and conservative
    evidence grade are not wrong, but the known strain qualifier is missing.'
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T152822Z-compound-3
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/915
  disposition_reason: The complete-row-pinned maintained decision now emits APC1.2
    (CCOS978) with separate curator evidence. Source chemistry, taxon, native grade
    and all unrelated owners/components are unchanged. Reproduction and full QC pass;
    the omission is fixed without inferring species-wide production.
actions: []
limitations:
- Scoped partial successor, not a new whole-record scientific pass. The original full
  assessment remains historical; this observation adds no newly assessed owner.
- The proposed connectivity and unresolved stereochemistry remain explicit. No direct
  PUL-gene experiment or purified-compound antifungal activity is inferred.
- The two other paper-local Compound 3 owners remain partial and distinct; their publisher
  403 limits and all 195 campaign access limitations are retained.
- 'Source state is git_commit: all 23 captured inputs were checked against the exact
  tagged implementation commit. The provenance tag is retained across the required
  squash merge.'
- The initial failed guarded write and regression run are retained as superseded attempts,
  not hidden successes. Canonical successor checks and final PR/merge-queue CI follow
  persistence.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261013T152822Z-compound-3
  relationship: Scoped resolution of F1 and F2 only
links:
- https://github.com/CultureBotAI/NaturalProductMech/pull/913
- https://github.com/CultureBotAI/NaturalProductMech/issues/914
- https://github.com/CultureBotAI/NaturalProductMech/issues/915
- https://github.com/CultureBotAI/NaturalProductMech/issues/916
```
