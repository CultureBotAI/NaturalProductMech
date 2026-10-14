# lomaiviticin-d-2: bounded curation follow-up

- Review: 20261014T054340Z-lomaiviticin-d-2-followup
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-14T05:41:56.410970Z
- Finished UTC: 2026-10-14T05:43:40.879870Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Reassessed bounded corrections; native identity conflicts remain open. No deterministic or publication gate is scientific identity sign-off.

## Scope And Provenance

Complete corrected exact owner and targeted maintained corrections, reassessed against the original inspected evidence.

Selection: Explicit follow-up of 20261014T053819Z-lomaiviticin-d-2
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7d6b4d16acc9a28e2b4c9de4244f205beb0da157.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-ba6ee9b824 | data/natural_products/polyketides/lomaiviticin-d-2.yaml | generated | lomaiviticin D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| focused-verified | passed | True | naturalproductmech:mibig-ba6ee9b824 | Actual bounded correction check passed. |
| strict-final | passed | True | naturalproductmech:mibig-ba6ee9b824 | Actual bounded correction check passed. |
| delta | passed | True | naturalproductmech:mibig-ba6ee9b824 | Actual bounded correction check passed. |
| Full authoritative GitHub QC for corrections | unavailable | True | naturalproductmech:mibig-ba6ee9b824 | Not yet run for the correction commit at this observation time. Original baseline QC is not counted as validation of later edits. Exact-head PR and merge-queue QC remain mandatory publication gates. |
| Primary exact-product closure | unavailable | True | naturalproductmech:mibig-ba6ee9b824 | Original structural access/inspection limits remain; no new replacement key or D structural adjudication was established. |
| curate | failed | False | naturalproductmech:mibig-ba6ee9b824 | Initial temporary mutator used EvidenceItem fields inside SupportingReference; the guarded writer rejected the first owner before any mutation. Corrected and rerun. |
| focused-final | failed | False | naturalproductmech:mibig-ba6ee9b824 | Initial test command named a nonexistent test file; no tests ran. The verified existing test files were then executed successfully. |

## Scientific And Domain Assessments

### Chemical identity remains open

identity: concern. Targets: naturalproductmech:mibig-ba6ee9b824.

Open curator discussion represents, but does not resolve, the original chemical finding. D certainty remains provisional; C replacement identity requires primary structural adjudication.

### Strain and locus claim boundaries

scope: supported. Targets: naturalproductmech:mibig-ba6ee9b824.

DPJ-0016 source locus is no longer graded by other-strain experiments; C production is qualified from the paper and D strain support remains explicitly unknown. Existing DPJ-0019 protein assays remain separately scoped.

### Bounded mechanism and conflict representation

graph: supported. Targets: naturalproductmech:mibig-ba6ee9b824.

Only pathway/final-product qualifications and open discussions were added; upstream supported edges, proteins, chemistry and pre-existing history remain.

## Findings

### identity-conflict: Competing D formulas remain unadjudicated

major / open / provisional; issue key: lomaiviticin-d-2-bgc0000240-identity-conflict.

This owner encodes C69H84N4O24, while the other D owner encodes C69H86N4O24. Their first InChIKey blocks and bond saturation differ, so they are not just complete/incomplete stereochemical versions of one structure. Inspected papers identify D by name but do not establish this exact deposited encoding at the required resolution. Primary2012 full text/spectra are unavailable, and the2021 A-C revision must not automatically be extended to D. Which D representation needs replacement remains unresolved.

Disposition: Still open: native OPEN discussion and qualified pathway/product-edge notes expose the conflict but do not establish a replacement structure. Chemistry and scientific status are unchanged; representation issue #979 is distinct from scientific adjudication.

### locus-scope: DPJ-0019 experiments and a CNB-440 citation grade a DPJ-0016 locus

major / resolved / confirmed; issue key: lomaiviticin-d-2-bgc0000240-locus-scope.

BGC0000240 names KF731828.1 (DPJ-0016), but its carried Knock-out studies&#124;Enzymatic assays grades and PMID23649992 do not establish experiments on that locus. Kersten used CNB-440; Janso disrupted DPJ-0019 lom58; Waldman assayed DPJ-0019 proteins from KF515737.1. DPJ-0016 and DPJ-0019 Lom62/Lom63 sequences differ. Preserve species351187 but expose DPJ-0016 locus provenance, qualify/remove inapplicable exact-locus methods, and route references separately. Do not silently replace the locus with DPJ-0019 or treat its already qualified curator graph as the DPJ-0016 experiment. Janso explicitly reports DPJ-0016 C and DPJ-0019 C-E production; the inspected text does not establish DPJ-0016 D production. This is a bounded evidence gap, not proof of nonproduction.

Disposition: Issue #977 corrected by source-pinned method withdrawal and separate citation routing. C producer is qualified as DPJ-0016; D is not assigned that strain without compound-specific evidence. The deposited locus remains KF731828.1 and the assayed graph remains DPJ-0019. D production in DPJ-0016 remains an explicit bounded evidence gap, not a demonstrated claim.

## Recommended Actions And Acceptance Checks

### adjudicate-identity

Resolve the exact product structure from primary structural evidence; retain an explicit conflict meanwhile. Do not merge same-name owners, infer new stereocenters or manufacture a revised SMILES from prose. The existing correction table accepts only a unique eligible three-star ChEBI target; none is established in the pinned inventory, so a source refresh or separately designed and audited identity-migration path may be needed.

- Independently check the revised structure, exact formula, bond connectivity and absolute stereochemistry against accessible primary figures/spectra; for D do not assume the A-C revision applies.
- Use the pinned RDKit to reproduce SMILES, Standard InChI, InChIKey and mass; adjudicate each named source concept and each same-name owner separately.
- Inventory occupied destination keys before any migration; preserve history and re-audit every producer/pathway/graph claim against the new exact owner. No automatic merge or copied assay links.
- Use validated record/component writers and appended curation events for authorized curator changes; preserve raw provenance and the PATHS filing contract.
- Run a canary before seeding, then strict validation, verify-corpus, verify-reproduction and full QC. Do not hand-edit generated pages or use reserved decisions.tsv.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| original | reviews/structured/20261014T053819Z-lomaiviticin-d-2/review.yaml | partial | Immutable original scientific assessment retains primary citations, scope, retrieval hashes and access limitations. |
| native | data/natural_products/polyketides/lomaiviticin-d-2.yaml | supports | Complete corrected owner inspected: original chemistry and protein identities retained; open conflicts and product-edge qualifications visible; provenance fixes scoped to reviewed source rows. |
| packet | reviews/evidence/20261014-lomaiviticin/manifest.json | supports | Portable database/analysis payload hashes and exact historical owner bindings verified by regression tests. Primary full text is not republished or claimed portable. |

## Limits And Additional Notes

- This is a bounded follow-up, not a new full primary spectral analysis. Original ACS403/PMC challenge and uninspected figure/spectra limitations remain.
- The final publication commit still needs its own canonical contract and required PR checks.
- No status promotion, identity substitution, owner merge or extension of the A-C revision to D.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T054340Z-lomaiviticin-d-2-followup
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'lomaiviticin-d-2: bounded curation follow-up'
started_at: '2026-10-14T05:41:56.410970Z'
finished_at: '2026-10-14T05:43:40.879870Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Separate adversarial pass by implementing assistant, not independent
    peer review.
skill: .claude/skills/curate-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: SEEDED; exact-product identity remains unresolved
scientific_review: true
summary: Reassessed bounded corrections; native identity conflicts remain open. No
  deterministic or publication gate is scientific identity sign-off.
source:
  git_revision: 7d6b4d16acc9a28e2b4c9de4244f205beb0da157
  state: working_tree
  inputs:
  - path: curation/mibig_claim_references.tsv
    sha256: f87a4fa580dede966366bece28ccfb6542bdec4a0f810e40cdfc719811407a05
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: b27c2e61e696a285c38bc88c852dbbdc6c06fec8c4584343f2b9146462eea6cf
    role: context
  - path: data/natural_products/polyketides/lomaiviticin-d-2.yaml
    sha256: e4edfc651b76dbf95cbb77837b1520964bdba464bd7f0387bdca06f2f6a98c49
    role: target
  - path: reviews/evidence/20261014-lomaiviticin/manifest.json
    sha256: e42cecd1a26c4b0d902d1d0dc982e4063206c7cd1a61b6f8bb3b68771bd979cf
    role: context
  - path: reviews/evidence/20261014-lomaiviticin/source-analysis.json
    sha256: 005e78550dac54d34003865d9fc12448c5f502e4817561fd562f40fde02f39fd
    role: context
  - path: tests/test_lomaiviticin_curation.py
    sha256: 52267ca7a3932711d3cc54bd57e29320261a126727a0a40fadc04fda8e26f700
    role: context
targets:
- target_id: naturalproductmech:mibig-ba6ee9b824
  path: data/natural_products/polyketides/lomaiviticin-d-2.yaml
  label: lomaiviticin D
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned structure and producer/locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated owner emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Guarded exact-structure adjudication with source pins
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Reviewed exact-locus evidence corrections
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Claim-specific reference routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/lomaiviticin-d-2.yaml
    role: Curator-owned pathways and graphs only through guarded writer and curation
      events
scope:
  description: Complete corrected exact owner and targeted maintained corrections,
    reassessed against the original inspected evidence.
  selection: Explicit follow-up of 20261014T053819Z-lomaiviticin-d-2
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-ba6ee9b824
checks:
- check_id: focused-verified
  name: focused-verified
  status: passed
  required: true
  command: uv run pytest -q tests/test_lomaiviticin_curation.py tests/test_mibig_locus_evidence_overrides.py
    tests/test_claim_references.py tests/test_producer_strains.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  summary: Actual bounded correction check passed.
  scope_note: 2026-10-14T05:41:52.426390Z..2026-10-14T05:42:04.316212Z; SHA256 6cf9a9058b4c5fe3472b768b8bd4e1aaaef2b01dd16a57d794db23b432f93bc1
- check_id: strict-final
  name: strict-final
  status: passed
  required: true
  command: just validate-strict data/natural_products/polyketides/lomaiviticin-c-2.yaml
    data/natural_products/polyketides/lomaiviticin-c.yaml data/natural_products/polyketides/lomaiviticin-d-2.yaml
    data/natural_products/polyketides/lomaiviticin-d.yaml --out /private/tmp/npmech-lomaiviticin-review-89PDr2/strict-final.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  summary: Actual bounded correction check passed.
  scope_note: 2026-10-14T05:41:13.447967Z..2026-10-14T05:41:21.081102Z; SHA256 40566d08c649377556158239052783d5d2b0cd64839e109555272ec088318e2d
- check_id: delta
  name: delta
  status: passed
  required: true
  command: uv run python /private/tmp/npmech-lomaiviticin-review-89PDr2/delta.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  summary: Actual bounded correction check passed.
  scope_note: 2026-10-14T05:41:20.879786Z..2026-10-14T05:41:24.927331Z; SHA256 21586761f0a38086213761e63d35b3af58d627c910f6cee361e70c209d71ac8a
- check_id: ci-qc
  name: Full authoritative GitHub QC for corrections
  status: unavailable
  required: true
  command: just qc
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  summary: Not yet run for the correction commit at this observation time. Original
    baseline QC is not counted as validation of later edits. Exact-head PR and merge-queue
    QC remain mandatory publication gates.
- check_id: primary-closure
  name: Primary exact-product closure
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  summary: Original structural access/inspection limits remain; no new replacement
    key or D structural adjudication was established.
- check_id: curate
  name: curate
  status: failed
  required: false
  command: uv run python /private/tmp/npmech-lomaiviticin-review-89PDr2/curate.py
  exit_code: 1
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  summary: Initial temporary mutator used EvidenceItem fields inside SupportingReference;
    the guarded writer rejected the first owner before any mutation. Corrected and
    rerun.
  scope_note: Retained log SHA256 a8a2a826a0918b24f318126349c24f88cef8135f947b90fc74c1797f2169deae
- check_id: focused-final
  name: focused-final
  status: failed
  required: false
  command: uv run pytest -q tests/test_lomaiviticin_curation.py tests/test_mibig_locus_evidence_overrides.py
    tests/test_claim_references.py tests/test_producer_strains.py tests/test_curator_discussions.py
  exit_code: 4
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  summary: Initial test command named a nonexistent test file; no tests ran. The verified
    existing test files were then executed successfully.
  scope_note: Retained log SHA256 fabc01081eb9de9995c1c4af0e528de8fe6e35e7cdeae99bf92eb6e7ed42e24e
evidence:
- evidence_id: original
  kind: prior_review
  reference: reviews/structured/20261014T053819Z-lomaiviticin-d-2/review.yaml
  summary: Immutable original scientific assessment retains primary citations, scope,
    retrieval hashes and access limitations.
  accessed_at: '2026-10-14T05:43:40.878686Z'
  support: partial
  snapshot_sha256: af35be33ee62fa413ac40a3d764250e903eb904369a2a8e49bb65bc6c313ae23
- evidence_id: native
  kind: record_content
  reference: data/natural_products/polyketides/lomaiviticin-d-2.yaml
  accessed_at: '2026-10-14T05:43:40.879142Z'
  summary: 'Complete corrected owner inspected: original chemistry and protein identities
    retained; open conflicts and product-edge qualifications visible; provenance fixes
    scoped to reviewed source rows.'
  support: supports
  snapshot_sha256: e4edfc651b76dbf95cbb77837b1520964bdba464bd7f0387bdca06f2f6a98c49
- evidence_id: packet
  kind: validation
  reference: reviews/evidence/20261014-lomaiviticin/manifest.json
  accessed_at: '2026-10-14T05:43:40.879436Z'
  summary: Portable database/analysis payload hashes and exact historical owner bindings
    verified by regression tests. Primary full text is not republished or claimed
    portable.
  support: supports
  snapshot_sha256: e42cecd1a26c4b0d902d1d0dc982e4063206c7cd1a61b6f8bb3b68771bd979cf
assessments:
- assessment_id: identity
  area: identity
  topic: Chemical identity remains open
  outcome: concern
  summary: Open curator discussion represents, but does not resolve, the original
    chemical finding. D certainty remains provisional; C replacement identity requires
    primary structural adjudication.
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  evidence_ids:
  - original
  - native
- assessment_id: provenance
  area: scope
  topic: Strain and locus claim boundaries
  outcome: supported
  summary: DPJ-0016 source locus is no longer graded by other-strain experiments;
    C production is qualified from the paper and D strain support remains explicitly
    unknown. Existing DPJ-0019 protein assays remain separately scoped.
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  evidence_ids:
  - original
  - native
  - packet
- assessment_id: representation
  area: graph
  topic: Bounded mechanism and conflict representation
  outcome: supported
  summary: Only pathway/final-product qualifications and open discussions were added;
    upstream supported edges, proteins, chemistry and pre-existing history remain.
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  evidence_ids:
  - native
  - packet
findings:
- finding_id: identity-conflict
  issue_key: lomaiviticin-d-2-bgc0000240-identity-conflict
  category: identity
  severity: major
  status: open
  certainty: provisional
  title: Competing D formulas remain unadjudicated
  description: This owner encodes C69H84N4O24, while the other D owner encodes C69H86N4O24.
    Their first InChIKey blocks and bond saturation differ, so they are not just complete/incomplete
    stereochemical versions of one structure. Inspected papers identify D by name
    but do not establish this exact deposited encoding at the required resolution.
    Primary2012 full text/spectra are unavailable, and the2021 A-C revision must not
    automatically be extended to D. Which D representation needs replacement remains
    unresolved.
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  field_paths:
  - chemical_structure
  - source_concepts[0]
  - biosynthetic_pathway[0]
  - causal_graphs[0]
  evidence_ids:
  - original
  - native
  - packet
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Upstream exact-structure extraction; preserve raw provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Guarded emission and explicit identity migration
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Only REPLACE_WITH_CHEBI when an eligible unique target has been established
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Pinned identity-to-path mapping, never direct filename renaming
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/lomaiviticin-d-2.yaml
    role: Only curator-owned discussions, pathway and graph claims through guarded
      writer and an appended event
  rule_id: review-checklist:identity-and-conflict-preservation
  native_severity: major
  normalization_reason: The material exact-form support gap is major; unavailable
    structural evidence does not justify declaring either D encoding definitively
    wrong or assigning a replacement.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261014T053819Z-lomaiviticin-d-2
    finding_id: identity-conflict
  disposition_reason: 'Still open: native OPEN discussion and qualified pathway/product-edge
    notes expose the conflict but do not establish a replacement structure. Chemistry
    and scientific status are unchanged; representation issue #979 is distinct from
    scientific adjudication.'
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/976
- finding_id: locus-scope
  issue_key: lomaiviticin-d-2-bgc0000240-locus-scope
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: DPJ-0019 experiments and a CNB-440 citation grade a DPJ-0016 locus
  description: BGC0000240 names KF731828.1 (DPJ-0016), but its carried Knock-out studies|Enzymatic
    assays grades and PMID23649992 do not establish experiments on that locus. Kersten
    used CNB-440; Janso disrupted DPJ-0019 lom58; Waldman assayed DPJ-0019 proteins
    from KF515737.1. DPJ-0016 and DPJ-0019 Lom62/Lom63 sequences differ. Preserve
    species351187 but expose DPJ-0016 locus provenance, qualify/remove inapplicable
    exact-locus methods, and route references separately. Do not silently replace
    the locus with DPJ-0019 or treat its already qualified curator graph as the DPJ-0016
    experiment. Janso explicitly reports DPJ-0016 C and DPJ-0019 C-E production; the
    inspected text does not establish DPJ-0016 D production. This is a bounded evidence
    gap, not proof of nonproduction.
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  field_paths:
  - producer_organisms[0]
  - biosynthetic_gene_clusters[0]
  evidence_ids:
  - original
  - native
  - packet
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Source-pinned withdrawal of inapplicable exact-locus experiments
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Independently route producer and locus references
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Only compound-supported producer strain qualification; a locus strain alone
      is insufficient
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Reproduce qualified generated claims without changing raw assertions
  rule_id: conf/producer_evidence.tsv:exact-native-organism-and-locus
  native_severity: major
  normalization_reason: Experimental evidence transferred between distinct strain
    deposits inflates the exact-locus grade and obscures claim provenance; this is
    major even though the source vocabulary was imported faithfully.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261014T053819Z-lomaiviticin-d-2
    finding_id: locus-scope
  disposition_reason: 'Issue #977 corrected by source-pinned method withdrawal and
    separate citation routing. C producer is qualified as DPJ-0016; D is not assigned
    that strain without compound-specific evidence. The deposited locus remains KF731828.1
    and the assayed graph remains DPJ-0019. D production in DPJ-0016 remains an explicit
    bounded evidence gap, not a demonstrated claim.'
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/977
actions:
- action_id: adjudicate-identity
  finding_ids:
  - identity-conflict
  target_ids:
  - naturalproductmech:mibig-ba6ee9b824
  description: Resolve the exact product structure from primary structural evidence;
    retain an explicit conflict meanwhile. Do not merge same-name owners, infer new
    stereocenters or manufacture a revised SMILES from prose. The existing correction
    table accepts only a unique eligible three-star ChEBI target; none is established
    in the pinned inventory, so a source refresh or separately designed and audited
    identity-migration path may be needed.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Upstream exact-structure extraction; preserve raw provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Guarded emission and explicit identity migration
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Only REPLACE_WITH_CHEBI when an eligible unique target has been established
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Pinned identity-to-path mapping, never direct filename renaming
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/lomaiviticin-d-2.yaml
    role: Only curator-owned discussions, pathway and graph claims through guarded
      writer and an appended event
  generator: scripts/seed_from_sources.py only after authorized maintained-input and
    identity-migration changes
  acceptance_checks:
  - Independently check the revised structure, exact formula, bond connectivity and
    absolute stereochemistry against accessible primary figures/spectra; for D do
    not assume the A-C revision applies.
  - Use the pinned RDKit to reproduce SMILES, Standard InChI, InChIKey and mass; adjudicate
    each named source concept and each same-name owner separately.
  - Inventory occupied destination keys before any migration; preserve history and
    re-audit every producer/pathway/graph claim against the new exact owner. No automatic
    merge or copied assay links.
  - Use validated record/component writers and appended curation events for authorized
    curator changes; preserve raw provenance and the PATHS filing contract.
  - Run a canary before seeding, then strict validation, verify-corpus, verify-reproduction
    and full QC. Do not hand-edit generated pages or use reserved decisions.tsv.
limitations:
- This is a bounded follow-up, not a new full primary spectral analysis. Original
  ACS403/PMC challenge and uninspected figure/spectra limitations remain.
- The final publication commit still needs its own canonical contract and required
  PR checks.
- No status promotion, identity substitution, owner merge or extension of the A-C
  revision to D.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261014T053819Z-lomaiviticin-d-2
  relationship: Reassesses exact findings after bounded curation
links:
- https://github.com/CultureBotAI/NaturalProductMech/issues/977
tags:
- lomaiviticin
- partial
- curation-followup
```
