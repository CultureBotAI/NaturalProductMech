# Review fluopsin C against retained local evidence

- Review: 20261107T105522Z-fluopsin-c
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T10:47:05.271832Z
- Finished UTC: 2026-11-07T10:55:22.915626Z
- Reviewer: Codex ROOT with Bgc/Support scientific reviewers and Native local checks (unknown)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The retained copper-complex identity, two curator-supplied producer claims and complete mechanism are traceable locally. The two stored representations agree after Standard InChI normalization but differ in explicit Cu coordination. No material local defect was established; physiological, strain-specific and primary-literature conclusions remain unverified.

## Scope And Provenance

Complete local reading of this one selected owner, its history and any declared mechanism components; scientific verification remains partial. The current campaign corpus contains3136 records.

Selection: Batch288, order2871: one of the first ten sorted currently unreviewed paths in the reconciled catalogue (1758 covered,1378 remaining before this batch). This bundle assesses only this target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 18ca5dd6b9023670f10355084b45a8757a7a4e9e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:222417 | data/natural_products/alkaloids/fluopsin-c.yaml | generated | fluopsin C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical target and source capture | passed | True | CHEBI:222417 | Captured this exact generated target and its regular-file source inputs at fresh main18ca; current input hashes remain unchanged. |
| Maintained local gate: strict_ten | passed | True | CHEBI:222417 | All ten selected whole owners passed closed validation; zero error rows. |
| Maintained local gate: strict_full | passed | True | CHEBI:222417 | All3136 current owners passed full closed validation with component-inventory audit; zero error rows. |
| Maintained local gate: lockfile | passed | True | CHEBI:222417 | All3136 owner paths agree with PATHS.tsv and filing pins, including component inventory checks. |
| Maintained local gate: reproduction | passed | True | CHEBI:222417 | All3136 records are byte-identical to the current seeder output. Carried curator mechanism claims are preserved, not independently proven. |
| Maintained local gate: queue | passed | True | CHEBI:222417 | The complete current review queue was generated locally:8919 rows across12 queues. Queue membership does not establish scientific review. |
| Local stored-form molecular diagnostic | passed | True | CHEBI:222417 | Exactly two stored encodings were parsed for this record (20 across the batch). Their normalized Standard InChI, key, computed formula and net charge agree; graph/canonical-SMILES equivalence and natural sample identity are not inferred. Record-specific differences remain in the scientific assessments. |
| Complete maintained mechanism read | passed | True | CHEBI:222417 | The actual maintained reader returned this whole owner unchanged, including all declared graphs and histories. {"graphs": 1, "nodes": 5, "edges": 4, "pathway_steps": 1, "molecular_targets": 2, "history": 2, "component_refs": 0} Technical readability does not prove cited experiments. |
| Superseded intake preparation attempt | failed | False | CHEBI:222417 | Initial alias input was rejected before capture; the required canonical intake above passed after selecting the existing regular guidance file. This was not a saved-review validation attempt. |
| Full repository QC | unavailable | True | CHEBI:222417 | Not run: maintained full QC reaches the vendored-sync fetch. The five local gates do not substitute for full QC. |
| Complete OAK identifier-label correspondence | unavailable | True | CHEBI:222417 | Not run: a complete pinned offline CHEBI/GO adapter boundary was not established. No ontology download or remote resolver was permitted. |
| Fresh source, literature, taxonomy and structured database verification | unavailable | True | CHEBI:222417 | Not run under the source-request hold. Database assertions, gene/pathway annotations, citations, exact forms and strain claims are assessed only against retained local evidence; no fresh resolution or primary-paper authentication is claimed. |

## Scientific And Domain Assessments

### Stored identity and representation

identity: supported. Targets: CHEBI:222417.

CHEBI:222417 is the Cu-containing complex, not the free ligand or ferric fluopsin F. Both stored forms give C4H8CuN2O2S2 and net charge zero. The connected SMILES has 11 atoms/12 bonds and two Cu-containing five-member cycles; reconstructed InChI has 11 atoms/8 bonds, two anionic ligands and Cu2+ in three fragments. Canonical strings, bond counts and atom correspondence differ. The literal formula-layer comparator is also false for this multicomponent InChI; its parsed formula agrees. These observations do not show a wrong natural identity.

### Source and producer claim ownership

provenance: supported. Targets: CHEBI:222417.

Curated rows 12–13 distinguish PAO1 BGC_CHARACTERIZED (PMID:34793213; flcA–E deletion/reconstitution) from M18 AXENIC_CULTURE (PMID:5549384). The latter note only names Pseudomonas sp.; the retained excerpt does not itself establish the species/strain specificity. ChEBI P. fluorescens MCRL-10107 occurrence and P. aeruginosa occurrence remain separate claims, with no extra independent-publication credit for repeated citations.

### Cached taxon and strain scope

grounding: supported. Targets: CHEBI:222417.

Cached IDs 208964, 287 and 294 retain PAO1, P. aeruginosa and P. fluorescens respectively. Species-level cache labels do not prove M18 or MCRL-10107 producer attribution.

### Pathway and graph claims

graph: unknown. Targets: CHEBI:222417.

The one FlcA–E pathway step describes ligand synthesis followed by Cu complexation; its enzyme-group field does not imply one enzyme catalyses every transformation. The BIOACTIVITY graph links ligand/Cu to the complex and copper transport. The Fe edge describes metal exchange to distinct fluopsin F, so it must not be read as preservation of the Cu complex. The maintained reader preserved all 5 nodes, 4 edges, one step and two histories; this verifies representation only.

### Metal targets, activity and material scope

evidence: unknown. Targets: CHEBI:222417.

The two curator-held targets distinguish Cu coordination from ferric transmetallation (PMIDs 5549384, 34793213 and 4927254). The exact AntibioticMech link asserts ANTIBACTERIAL at corpus commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976; it is not a retained quantitative assay. Exact-key PubChem/BindingDB frames are empty, which neither verifies nor refutes the recorded metal claims.

### Maintained ownership and curation history

consistency: supported. Targets: CHEBI:222417.

Imported ChEBI chemistry/definition and curated-table producer claims have different owners from record-held mechanisms. The two saved events record seeding and an agent-assisted RECORD_CURATED promotion to REVIEWED; that status is historical metadata, not this review’s validation of every citation. Any correction must follow its maintained source or the validated curator writer, preserving provenance.

### Review completeness

completeness: unknown. Targets: CHEBI:222417.

All current source fields, complete owner/history, saved molecular tables and maintained returned owner were considered. Full QC, current OAK/remote taxonomy and primary literature verification are held by the no-request instruction. Local read/parse success does not certify catalytic specificity, binding constants, natural stereochemistry or all citations. Completion remains partial.

### Bounded positive local validation and normalized chemical representation

consistency: supported. Targets: CHEBI:222417.

The selected record is well-formed under the current closed schema and reproduces from maintained inputs. The two stored molecular encodings generate the declared Standard InChIKey and agree in parsed formula and net charge. These positive local results do not establish natural identity, exact graph equivalence, strain-specific production or primary-paper support.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| BGC288-2871-owner | data/natural_products/alkaloids/fluopsin-c.yaml; Complete record; chemical_structure, producer_organisms, biosynthetic_pathway, molecular_targets, causal_graphs[0], curation_history | partial | Complete raw owner and both histories read. Actual maintained complete_view equals that exact retained owner; record-held PRIMARY_EXPERIMENT labels are attributed annotations, not current primary-paper access. |
| BGC288-2871-source | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch288-reconciled-preflight/support-prep/current288-retained-source-extraction-001.json; records[0].frames[0:20]; positive rows retain physical_lines, full row dictionaries and raw_span | partial | All 20 exact local selector frames read: 7 row placements, 65 fields. Includes ChEBI full row, classifier and curated evidence; zero selected assay rows. Shared-BGC metadata is not exact identity. |
| BGC288-2871-curated | curation/curated_compounds.tsv; Physical TSV lines 12–13; chebi_id=CHEBI:222417 | partial | All 16 fields per matched row read; expected_chebi_row_sha256 equals the exact retained ChEBI row digest. Producer basis, strain, reference, curator/date and chemistry are retained assertions. |
| BGC288-2871-chemistry | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/chemistry-local/diagnostic-DATA-001.json; records[0].smiles.computed and inchi.computed: complete atoms/bonds/rings/potential_stereo/motifs; comparisons and atom_correspondence | partial | Connected metal coordination versus three-component ionic reconstruction; 11/12 versus 11/8 atoms/bonds. Both canonical comparisons false, map empty, full_graph_identity_established false. |
| BGC288-2871-reader | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/maintained-readers-DATA-001.json; records[0].complete_view, whole_view_equals_capture and counts | supports | One actual maintained call preserved the whole owner, 1 graph, 5 nodes/4 edges, 1 steps, 2 molecular targets and two histories. No components or molecular parse in this reader call; technical preservation only. |
| BGC288-2871-taxonomy | data/raw/corpus_taxa.obo; Complete [Term] stanzas: NCBITaxon:208964, NCBITaxon:287, NCBITaxon:294 | partial | Cached IDs 208964, 287 and 294 retain PAO1, P. aeruginosa and P. fluorescens respectively. Species-level cache labels do not prove M18 or MCRL-10107 producer attribution. |
| BGC288-2871-ownership | scripts/seed_from_sources.py; CURATOR_OWNED_CARRIED_FIELDS and carry_curator_owned_fields, lines 315–425 | partial | Pathways, ecological roles, graphs and CURATOR molecular targets are preserved on exact nonempty structure-key match. Reproduction does not independently validate their biology or citations. |
| BGC288-2871-curated-policy | src/naturalproductmech/curate/curated_compounds.py; load_curated_compounds, complete function | partial | Maintained curated admission validates row/structure pins, causal producer labels and citation syntax. These guards do not independently authenticate the cited experiment. |
| EV288-intake | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/inspect-2871-002/stdout; Retained original execution output; exact SHA256 below. | supports | Captured this exact generated target and its regular-file source inputs at fresh main18ca; current input hashes remain unchanged. |
| EV288-strict_ten | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-strict-ten-001/stdout; Retained original execution output; exact SHA256 below. | supports | All ten selected whole owners passed closed validation; zero error rows. |
| EV288-strict_full | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-strict-full-001/stdout; Retained original execution output; exact SHA256 below. | supports | All3136 current owners passed full closed validation with component-inventory audit; zero error rows. |
| EV288-lockfile | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-lockfile-001/stdout; Retained original execution output; exact SHA256 below. | supports | All3136 owner paths agree with PATHS.tsv and filing pins, including component inventory checks. |
| EV288-reproduction | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-reproduction-001/stdout; Retained original execution output; exact SHA256 below. | supports | All3136 records are byte-identical to the current seeder output. Carried curator mechanism claims are preserved, not independently proven. |
| EV288-queue | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-queue-001/stdout; Retained original execution output; exact SHA256 below. | supports | The complete current review queue was generated locally:8919 rows across12 queues. Queue membership does not establish scientific review. |
| EV288-molecular | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/chemistry-local/diagnostic-DATA-001.json; Retained original execution output; exact SHA256 below. | supports | Exactly two stored encodings were parsed for this record (20 across the batch). Their normalized Standard InChI, key, computed formula and net charge agree; graph/canonical-SMILES equivalence and natural sample identity are not inferred. Record-specific differences remain in the scientific assessments. |
| EV288-reader | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/maintained-readers-DATA-001.json; Retained original execution output; exact SHA256 below. | supports | The actual maintained reader returned this whole owner unchanged, including all declared graphs and histories. {"graphs": 1, "nodes": 5, "edges": 4, "pathway_steps": 1, "molecular_targets": 2, "history": 2, "component_refs": 0} Technical readability does not prove cited experiments. |
| EV288-initial-capture | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/inspect-2871-001/stderr; Retained original execution output; exact SHA256 below. | context_only | An initial preparation capture rejected the redundant CLAUDE.md symlink before source capture. The successful capture uses its existing regular AGENTS.md source; no source content was changed. |

## Limits And Additional Notes

- No external request or fresh primary-literature/remote-taxonomy verification was performed; full QC and OAK remain unavailable.
- Only the two original stored encodings were parsed by the actual diagnostic. Global stderr warnings are retained without assigning individual warning lines to records; canonical similarity is not a natural-identity proof.
- Curator-held PRIMARY_EXPERIMENT labels, quantitative binding claims and REVIEWED status are retained assertions, not current authentication of source articles.
- Full QC, complete OAK label checks and fresh external-source verification are unavailable. Completion remains partial despite successful local gates.
- The review source is a working-tree input attestation at the captured Git base. Saved validation does not promote native record status or close unrelated historical findings.
- Complete first-five owner reading and actual complete_view equality were used together; no source/record/curation status was changed.
- Source extraction rows are overlapping retained evidence, not additional experiments. Review timestamps reflect this local access.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T105522Z-fluopsin-c
kind: record
repository: CultureBotAI/NaturalProductMech
title: Review fluopsin C against retained local evidence
started_at: '2026-11-07T10:47:05.271832Z'
finished_at: '2026-11-07T10:55:22.915626Z'
reviewer:
  identity: Codex ROOT with Bgc/Support scientific reviewers and Native local checks
  kind: agent
  independence: unknown
  independence_basis: Read-only review in an isolated owned checkout. Authorship independence
    from historical record curation is not established; local technical checks and
    domain assessments were assigned separately.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: The retained copper-complex identity, two curator-supplied producer claims
  and complete mechanism are traceable locally. The two stored representations agree
  after Standard InChI normalization but differ in explicit Cu coordination. No material
  local defect was established; physiological, strain-specific and primary-literature
  conclusions remain unverified.
source:
  git_revision: 18ca5dd6b9023670f10355084b45a8757a7a4e9e
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: AGENTS.md
    sha256: 69e4037f8dc97d4b00bb7bb83b41ceca025f6ef578d5c0bf8086f3400becde0b
    role: context
  - path: conf/id_label_targets.yaml
    sha256: c3a6935589e9db0fdff25c518a31e2d5b02b99d9110a33f6ff6335455e03601c
    role: context
  - path: conf/np_roles.tsv
    sha256: 0660a4067b6b9b23c0929ddbe2a42b470c41bf77575ea7f83008c450bbf91dd3
    role: context
  - path: conf/producer_evidence.tsv
    sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
    role: context
  - path: conf/record_review.yaml
    sha256: e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8
    role: context
  - path: conf/sources.yaml
    sha256: d5e8ab63eeebb376589a0c9bf6f7eb92f45913b84243de20d820442ec88d5a98
    role: context
  - path: curation/curated_compounds.tsv
    sha256: 371b3a8b453dc9706e6a8f7f615bf6604809b1c42f4a38b7e9e921ffcbbad064
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
    sha256: 2917836665e5117aebf1947cb148711bc0df7f1475bd2fdbfad0cd6d411e6cc7
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
    role: context
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: curation/unresolved_taxa.tsv
    sha256: 86efbda9c09388723a4f24da35e18404032f1549a9088192fbd2020cb846fa43
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 364ec7b1bbd49467cde7fe69f66964e4640020638ba80fccfc62e2162ede7f42
    role: context
  - path: data/natural_products/alkaloids/fluopsin-c.yaml
    sha256: f17d9d8c41472fbe731f931ae8ad2dc2921cc665198ad383d173edf69e2dcfe5
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 3370e0835cefa2f4d08fe496e81f7dc3ad8783ee76fd9b2a222465e1f5e31937
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
    sha256: f62f89df12bd373e0663a7e11e56e46733ca174f8495ec116ec57679c2279f35
    role: context
  - path: data/raw/pathwaymech_products.tsv
    sha256: 28ff699b83648614928f7ea5d8e8f5aee49a34ebbc9b6e9dbfece255383b7e04
    role: context
  - path: data/raw/pubchem_bioassay.tsv
    sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
    role: context
  - path: data/raw/taxon_groups.tsv
    sha256: f73f228d57d79a1d85a1441efa6829917b1ffecac08cb7bdd4fc855046255f8f
    role: context
  - path: data/raw/taxon_merged.tsv
    sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
    role: context
  - path: data/raw/taxon_names.tsv
    sha256: 9058b9a99260eb483ea21ce7cc9713fd336177031d883f0b5fb50325c7b2c371
    role: context
  - path: data/raw/taxon_non_organism.tsv
    sha256: f2c1ee257bbbcb0854528196ab1f809d658c27f1c7b2036f7f71f088b52935bb
    role: context
  - path: docs/CURATION.md
    sha256: 397dc32b7978f9115229f13232f3d9e9c5fac4ce5265e2f9e9cef13b6a9842f9
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
  - path: scripts/check_reproduction.py
    sha256: b00efb72ebf81c84760ccb4a0a491a596d1198d1e21613df6cb417e68caff868
    role: context
  - path: scripts/curation_worklist.py
    sha256: 913508ca8df2eb5c037cd9e4769b14b027869ab78c7306f33b59e1c7e383a1c3
    role: context
  - path: scripts/extract_chebi.py
    sha256: 46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/seed_from_sources.py
    sha256: d6650a80685b7f778050f79cc72de1fc3bbf281c57336401a5c773755de56324
    role: context
  - path: scripts/validate_strict.py
    sha256: e9b844d10fb7d2889521677716098da5883c7fd7d3c887a5cb600b87bbca0c21
    role: context
  - path: scripts/verify_corpus.py
    sha256: 3e79d6e18e43010a84e2ef7857625655185796d447ee12979a94cd836d756b60
    role: context
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: c57128ce7815cd3e336e427e9699e374836fa263905da875055ca9defea55f01
    role: context
  - path: src/naturalproductmech/curate/curated_compounds.py
    sha256: fdafad9ed1d94c78c996083632c75f3bafc1620a31da5aa7b9a37e558a187915
    role: context
  - path: src/naturalproductmech/curate/lotus_exclusions.py
    sha256: 6352cac7c587eab5a56d907c523cc899d02d197009081624bf8649c675ee30f7
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
    role: context
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
    role: context
  - path: src/naturalproductmech/grading.py
    sha256: ece54c4a2c0803f034ac59de51b1006cf79ea8d6b6256d75757d4adb88ea9630
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
  - path: src/naturalproductmech/validation/write_validated.py
    sha256: 4728cfb7d3406b971c02f2bc81e1dfb97679ea0914d27563282ce4c5185f474a
    role: context
  - path: tests/test_curated_compounds.py
    sha256: 01af0ae1e13811d6238227f5c82ac627f4e9effa870ecc50b922cb7de2d144cc
    role: context
  - path: tests/test_record_review_contract.py
    sha256: 7be08e684dcd235ddeae8f3c6a5d45b0ee74a60d1c1818cc81467e38901e5d56
    role: context
  - path: uv.lock
    sha256: c62a5739e3ffeb12cc57b3bf12a31dcf9cdfbf00b417f4ba3a801d51ef9efbe3
    role: context
scope:
  description: Complete local reading of this one selected owner, its history and
    any declared mechanism components; scientific verification remains partial. The
    current campaign corpus contains3136 records.
  selection: 'Batch288, order2871: one of the first ten sorted currently unreviewed
    paths in the reconciled catalogue (1758 covered,1378 remaining before this batch).
    This bundle assesses only this target.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:222417
targets:
- target_id: CHEBI:222417
  path: data/natural_products/alkaloids/fluopsin-c.yaml
  label: fluopsin C
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/fluopsin-c.yaml
    role: Curator-owned pathway, graphs, molecular targets and audit history; retain
      imported source-owned fields through the seeder.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained source harmonization and guarded emission of generated record
      fields.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned structure/source inventory; changes belong in the maintained extractor
      or reviewed supported curation lane.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/curated_compounds.tsv
    role: Maintained literature-backed ChEBI admission, chemistry and exact strain-qualified
      producer assertions.
  ownership_note: Review only. Imported rows remain source-owned; curator-owned mechanisms
    require the validated writer and an artifact-specific event for any future change.
    Reserved curation/decisions.tsv is not an effective seeder input.
checks:
- check_id: CK288-intake
  name: Canonical target and source capture
  status: passed
  required: true
  summary: Captured this exact generated target and its regular-file source inputs
    at fresh main18ca; current input hashes remain unchanged.
  target_ids:
  - CHEBI:222417
  command: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/.venv/bin/python
    scripts/record_review.py inspect --targets /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/intakes-001/2871-targets-001.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/review-yaml-record/SKILL.md --input AGENTS.md --input conf/id_label_targets.yaml
    --input conf/np_roles.tsv --input conf/producer_evidence.tsv --input conf/record_review.yaml
    --input conf/sources.yaml --input curation/curated_compounds.tsv --input curation/lotus_occurrence_exclusions.tsv
    --input curation/mibig_claim_references.tsv --input curation/mibig_locus_evidence_overrides.tsv
    --input curation/mibig_producer_isolates.tsv --input curation/mibig_producer_strains.tsv
    --input curation/mibig_structure_corrections.tsv --input curation/mibig_xref_exclusions.tsv
    --input curation/pubchem_bioassay_exclusions.tsv --input curation/unresolved_taxa.tsv
    --input data/natural_products/PATHS.tsv --input data/raw/MANIFEST.yaml --input
    data/raw/antibioticmech_inchikeys.tsv --input data/raw/bindingdb_targets.tsv --input
    data/raw/chebi_origins.tsv --input data/raw/chebi_structures.tsv --input data/raw/corpus_taxa.obo
    --input data/raw/cyanometdb_occurrences.tsv --input data/raw/lotus_occurrences.tsv
    --input data/raw/mibig_compounds.tsv --input data/raw/npclassifier.tsv --input
    data/raw/pathwaymech_products.tsv --input data/raw/pubchem_bioassay.tsv --input
    data/raw/taxon_groups.tsv --input data/raw/taxon_merged.tsv --input data/raw/taxon_names.tsv
    --input data/raw/taxon_non_organism.tsv --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/record-review-profile.md --input docs/record-reviews.md --input justfile
    --input pyproject.toml --input schema/record_review.yaml --input scripts/check_reproduction.py
    --input scripts/curation_worklist.py --input scripts/extract_chebi.py --input
    scripts/extract_mibig.py --input scripts/record_review.py --input scripts/seed_from_sources.py
    --input scripts/validate_strict.py --input scripts/verify_corpus.py --input src/naturalproductmech/curate/bioassay_exclusions.py
    --input src/naturalproductmech/curate/claim_references.py --input src/naturalproductmech/curate/curated_compounds.py
    --input src/naturalproductmech/curate/lotus_exclusions.py --input src/naturalproductmech/curate/producer_strains.py
    --input src/naturalproductmech/curate/structure_corrections.py --input src/naturalproductmech/curate/xref_exclusions.py
    --input src/naturalproductmech/grading.py --input src/naturalproductmech/graph_components.py
    --input src/naturalproductmech/schema/history.yaml --input src/naturalproductmech/schema/mech_shared.yaml
    --input src/naturalproductmech/schema/naturalproductmech.yaml --input src/naturalproductmech/validation/write_validated.py
    --input tests/test_curated_compounds.py --input tests/test_record_review_contract.py
    --input uv.lock
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV288-intake
- check_id: CK288-strict_ten
  name: 'Maintained local gate: strict_ten'
  status: passed
  required: true
  summary: All ten selected whole owners passed closed validation; zero error rows.
  target_ids:
  - CHEBI:222417
  command: /opt/homebrew/bin/just validate-strict data/natural_products/alkaloids/fluopsin-c.yaml
    data/natural_products/alkaloids/pyochelin-ii.yaml data/natural_products/alkaloids/rhizobactin-1021.yaml
    data/natural_products/amino_acids_and_peptides/achromobactin-free-acid.yaml data/natural_products/amino_acids_and_peptides/deferrichrome.yaml
    data/natural_products/amino_acids_and_peptides/desferrialbomycin-2.yaml data/natural_products/amino_acids_and_peptides/desferricoprogen-b.yaml
    data/natural_products/amino_acids_and_peptides/desferriexochelin-772ms.yaml data/natural_products/amino_acids_and_peptides/n-2-3-dihydroxybenzoyl-l-serine.yaml
    data/natural_products/amino_acids_and_peptides/radamycin.yaml --workers 2 --quiet
    --out /Users/marcin/agent-work/NaturalProductMech/npm-native-checks/batch-288/selected-strict-001.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV288-strict_ten
- check_id: CK288-strict_full
  name: 'Maintained local gate: strict_full'
  status: passed
  required: true
  summary: All3136 current owners passed full closed validation with component-inventory
    audit; zero error rows.
  target_ids:
  - CHEBI:222417
  command: /opt/homebrew/bin/just validate-strict --workers 2 --quiet --out /Users/marcin/agent-work/NaturalProductMech/npm-native-checks/batch-288/full-strict-001.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV288-strict_full
- check_id: CK288-lockfile
  name: 'Maintained local gate: lockfile'
  status: passed
  required: true
  summary: All3136 owner paths agree with PATHS.tsv and filing pins, including component
    inventory checks.
  target_ids:
  - CHEBI:222417
  command: /opt/homebrew/bin/just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV288-lockfile
- check_id: CK288-reproduction
  name: 'Maintained local gate: reproduction'
  status: passed
  required: true
  summary: All3136 records are byte-identical to the current seeder output. Carried
    curator mechanism claims are preserved, not independently proven.
  target_ids:
  - CHEBI:222417
  command: /opt/homebrew/bin/just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV288-reproduction
- check_id: CK288-queue
  name: 'Maintained local gate: queue'
  status: passed
  required: true
  summary: The complete current review queue was generated locally:8919 rows across12
    queues. Queue membership does not establish scientific review.
  target_ids:
  - CHEBI:222417
  command: /opt/homebrew/bin/just review-queue --tsv /Users/marcin/agent-work/NaturalProductMech/npm-native-checks/batch-288/review-queue-001.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV288-queue
- check_id: CK288-molecular
  name: Local stored-form molecular diagnostic
  status: passed
  required: true
  summary: Exactly two stored encodings were parsed for this record (20 across the
    batch). Their normalized Standard InChI, key, computed formula and net charge
    agree; graph/canonical-SMILES equivalence and natural sample identity are not
    inferred. Record-specific differences remain in the scientific assessments.
  target_ids:
  - CHEBI:222417
  command: /usr/bin/sandbox-exec -p '(version 1)(allow default)(deny network*)' /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/.venv/bin/python
    -I -S -B /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/read-and-diagnose-local-002.py
    diagnostic
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV288-molecular
- check_id: CK288-reader
  name: Complete maintained mechanism read
  status: passed
  required: true
  summary: 'The actual maintained reader returned this whole owner unchanged, including
    all declared graphs and histories. {"graphs": 1, "nodes": 5, "edges": 4, "pathway_steps":
    1, "molecular_targets": 2, "history": 2, "component_refs": 0} Technical readability
    does not prove cited experiments.'
  target_ids:
  - CHEBI:222417
  command: /usr/bin/sandbox-exec -p '(version 1)(allow default)(deny network*)' /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/.venv/bin/python
    -I -S -B /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/read-and-diagnose-local-002.py
    readers
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV288-reader
- check_id: CK288-initial-capture
  name: Superseded intake preparation attempt
  status: failed
  required: false
  summary: Initial alias input was rejected before capture; the required canonical
    intake above passed after selecting the existing regular guidance file. This was
    not a saved-review validation attempt.
  target_ids:
  - CHEBI:222417
  command: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/.venv/bin/python
    scripts/record_review.py inspect --targets /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/intakes-001/2871-targets-001.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/review-yaml-record/SKILL.md --input AGENTS.md --input CLAUDE.md
    --input conf/id_label_targets.yaml --input conf/np_roles.tsv --input conf/producer_evidence.tsv
    --input conf/record_review.yaml --input conf/sources.yaml --input curation/curated_compounds.tsv
    --input curation/lotus_occurrence_exclusions.tsv --input curation/mibig_claim_references.tsv
    --input curation/mibig_locus_evidence_overrides.tsv --input curation/mibig_producer_isolates.tsv
    --input curation/mibig_producer_strains.tsv --input curation/mibig_structure_corrections.tsv
    --input curation/mibig_xref_exclusions.tsv --input curation/pubchem_bioassay_exclusions.tsv
    --input curation/unresolved_taxa.tsv --input data/natural_products/PATHS.tsv --input
    data/raw/MANIFEST.yaml --input data/raw/antibioticmech_inchikeys.tsv --input data/raw/bindingdb_targets.tsv
    --input data/raw/chebi_origins.tsv --input data/raw/chebi_structures.tsv --input
    data/raw/corpus_taxa.obo --input data/raw/cyanometdb_occurrences.tsv --input data/raw/lotus_occurrences.tsv
    --input data/raw/mibig_compounds.tsv --input data/raw/npclassifier.tsv --input
    data/raw/pathwaymech_products.tsv --input data/raw/pubchem_bioassay.tsv --input
    data/raw/taxon_groups.tsv --input data/raw/taxon_merged.tsv --input data/raw/taxon_names.tsv
    --input data/raw/taxon_non_organism.tsv --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/record-review-profile.md --input docs/record-reviews.md --input justfile
    --input pyproject.toml --input schema/record_review.yaml --input scripts/check_reproduction.py
    --input scripts/curation_worklist.py --input scripts/extract_chebi.py --input
    scripts/extract_mibig.py --input scripts/record_review.py --input scripts/seed_from_sources.py
    --input scripts/validate_strict.py --input scripts/verify_corpus.py --input src/naturalproductmech/curate/bioassay_exclusions.py
    --input src/naturalproductmech/curate/claim_references.py --input src/naturalproductmech/curate/curated_compounds.py
    --input src/naturalproductmech/curate/lotus_exclusions.py --input src/naturalproductmech/curate/producer_strains.py
    --input src/naturalproductmech/curate/structure_corrections.py --input src/naturalproductmech/curate/xref_exclusions.py
    --input src/naturalproductmech/grading.py --input src/naturalproductmech/graph_components.py
    --input src/naturalproductmech/schema/history.yaml --input src/naturalproductmech/schema/mech_shared.yaml
    --input src/naturalproductmech/schema/naturalproductmech.yaml --input src/naturalproductmech/validation/write_validated.py
    --input tests/test_curated_compounds.py --input tests/test_record_review_contract.py
    --input uv.lock
  exit_code: 1
  evidence_ids:
  - EV288-initial-capture
- check_id: CK288-full-qc
  name: Full repository QC
  status: unavailable
  required: true
  summary: 'Not run: maintained full QC reaches the vendored-sync fetch. The five
    local gates do not substitute for full QC.'
  target_ids:
  - CHEBI:222417
- check_id: CK288-ontology
  name: Complete OAK identifier-label correspondence
  status: unavailable
  required: true
  summary: 'Not run: a complete pinned offline CHEBI/GO adapter boundary was not established.
    No ontology download or remote resolver was permitted.'
  target_ids:
  - CHEBI:222417
- check_id: CK288-fresh-authorities
  name: Fresh source, literature, taxonomy and structured database verification
  status: unavailable
  required: true
  summary: Not run under the source-request hold. Database assertions, gene/pathway
    annotations, citations, exact forms and strain claims are assessed only against
    retained local evidence; no fresh resolution or primary-paper authentication is
    claimed.
  target_ids:
  - CHEBI:222417
evidence:
- evidence_id: BGC288-2871-owner
  kind: record_content
  reference: data/natural_products/alkaloids/fluopsin-c.yaml
  locator: Complete record; chemical_structure, producer_organisms, biosynthetic_pathway,
    molecular_targets, causal_graphs[0], curation_history
  accessed_at: '2026-11-07T10:53:21.411233Z'
  support: partial
  summary: Complete raw owner and both histories read. Actual maintained complete_view
    equals that exact retained owner; record-held PRIMARY_EXPERIMENT labels are attributed
    annotations, not current primary-paper access.
  snapshot_sha256: f17d9d8c41472fbe731f931ae8ad2dc2921cc665198ad383d173edf69e2dcfe5
- evidence_id: BGC288-2871-source
  kind: search
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch288-reconciled-preflight/support-prep/current288-retained-source-extraction-001.json
  locator: records[0].frames[0:20]; positive rows retain physical_lines, full row
    dictionaries and raw_span
  accessed_at: '2026-11-07T10:53:21.411233Z'
  support: partial
  summary: 'All 20 exact local selector frames read: 7 row placements, 65 fields.
    Includes ChEBI full row, classifier and curated evidence; zero selected assay
    rows. Shared-BGC metadata is not exact identity.'
  snapshot_sha256: 9964292610e52e0175cf4a68aa9d8c556eef5380fe9c8fd5ca523094b8a00910
  search_scope: The exact twenty local file-selector frames enumerated in the referenced
    retained-source extraction, including their saved predicates, positive rows and
    zero-result frames. Named local files were read directly without gitignore filtering.
    Results are bounded to these frozen files; no remote query or global literature-absence
    inference.
- evidence_id: BGC288-2871-curated
  kind: database
  reference: curation/curated_compounds.tsv
  locator: Physical TSV lines 12–13; chebi_id=CHEBI:222417
  accessed_at: '2026-11-07T10:53:21.411233Z'
  support: partial
  summary: All 16 fields per matched row read; expected_chebi_row_sha256 equals the
    exact retained ChEBI row digest. Producer basis, strain, reference, curator/date
    and chemistry are retained assertions.
  snapshot_sha256: 371b3a8b453dc9706e6a8f7f615bf6604809b1c42f4a38b7e9e921ffcbbad064
- evidence_id: BGC288-2871-chemistry
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/chemistry-local/diagnostic-DATA-001.json
  locator: 'records[0].smiles.computed and inchi.computed: complete atoms/bonds/rings/potential_stereo/motifs;
    comparisons and atom_correspondence'
  accessed_at: '2026-11-07T10:53:21.411233Z'
  support: partial
  summary: Connected metal coordination versus three-component ionic reconstruction;
    11/12 versus 11/8 atoms/bonds. Both canonical comparisons false, map empty, full_graph_identity_established
    false.
  snapshot_sha256: 0c6f6295b3f1d3c0755d8d902df0f9a375b3f23a1878346ad94584b492b8021c
- evidence_id: BGC288-2871-reader
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/maintained-readers-DATA-001.json
  locator: records[0].complete_view, whole_view_equals_capture and counts
  accessed_at: '2026-11-07T10:53:21.411233Z'
  support: supports
  summary: One actual maintained call preserved the whole owner, 1 graph, 5 nodes/4
    edges, 1 steps, 2 molecular targets and two histories. No components or molecular
    parse in this reader call; technical preservation only.
  snapshot_sha256: 68398e58af6b7cc02b67978b7c92a04f2e9321941a9d230735eb808d12b8bf54
- evidence_id: BGC288-2871-taxonomy
  kind: authority
  reference: data/raw/corpus_taxa.obo
  locator: 'Complete [Term] stanzas: NCBITaxon:208964, NCBITaxon:287, NCBITaxon:294'
  accessed_at: '2026-11-07T10:53:21.411233Z'
  support: partial
  summary: Cached IDs 208964, 287 and 294 retain PAO1, P. aeruginosa and P. fluorescens
    respectively. Species-level cache labels do not prove M18 or MCRL-10107 producer
    attribution.
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: BGC288-2871-ownership
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: CURATOR_OWNED_CARRIED_FIELDS and carry_curator_owned_fields, lines 315–425
  accessed_at: '2026-11-07T10:53:21.411233Z'
  support: partial
  summary: Pathways, ecological roles, graphs and CURATOR molecular targets are preserved
    on exact nonempty structure-key match. Reproduction does not independently validate
    their biology or citations.
  snapshot_sha256: d6650a80685b7f778050f79cc72de1fc3bbf281c57336401a5c773755de56324
- evidence_id: BGC288-2871-curated-policy
  kind: record_content
  reference: src/naturalproductmech/curate/curated_compounds.py
  locator: load_curated_compounds, complete function
  accessed_at: '2026-11-07T10:53:21.411233Z'
  support: partial
  summary: Maintained curated admission validates row/structure pins, causal producer
    labels and citation syntax. These guards do not independently authenticate the
    cited experiment.
  snapshot_sha256: fdafad9ed1d94c78c996083632c75f3bafc1620a31da5aa7b9a37e558a187915
- evidence_id: EV288-intake
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/inspect-2871-002/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:47:06.412170Z'
  support: supports
  summary: Captured this exact generated target and its regular-file source inputs
    at fresh main18ca; current input hashes remain unchanged.
  snapshot_sha256: b61e523d2202049dc800dc49b1b337c927e6e23ecaa2c6924a98ac29b9f60220
- evidence_id: EV288-strict_ten
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-strict-ten-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:46:17.912716Z'
  support: supports
  summary: All ten selected whole owners passed closed validation; zero error rows.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: EV288-strict_full
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-strict-full-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:46:38.119885Z'
  support: supports
  summary: All3136 current owners passed full closed validation with component-inventory
    audit; zero error rows.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: EV288-lockfile
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-lockfile-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:46:59.185110Z'
  support: supports
  summary: All3136 owner paths agree with PATHS.tsv and filing pins, including component
    inventory checks.
  snapshot_sha256: 06b20cd71ef4e0ce9f998515c0dbd4076f81b0f420e22e4949fc19494217de24
- evidence_id: EV288-reproduction
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-reproduction-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:47:41.032280Z'
  support: supports
  summary: All3136 records are byte-identical to the current seeder output. Carried
    curator mechanism claims are preserved, not independently proven.
  snapshot_sha256: 6375bbedfde712e0de5fd1fd6c8f939e45bd2cab4fecb4be7f8fc5b11ab7337d
- evidence_id: EV288-queue
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-queue-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:47:54.538368Z'
  support: supports
  summary: The complete current review queue was generated locally:8919 rows across12
    queues. Queue membership does not establish scientific review.
  snapshot_sha256: 386216f171f1a0c3aac15fbc6e76ee6eedda8235755ec8abb80a2c173f297369
- evidence_id: EV288-molecular
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/chemistry-local/diagnostic-DATA-001.json
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:49:27.530710Z'
  support: supports
  summary: Exactly two stored encodings were parsed for this record (20 across the
    batch). Their normalized Standard InChI, key, computed formula and net charge
    agree; graph/canonical-SMILES equivalence and natural sample identity are not
    inferred. Record-specific differences remain in the scientific assessments.
  snapshot_sha256: 0c6f6295b3f1d3c0755d8d902df0f9a375b3f23a1878346ad94584b492b8021c
- evidence_id: EV288-reader
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/maintained-readers-DATA-001.json
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:49:26.820823Z'
  support: supports
  summary: 'The actual maintained reader returned this whole owner unchanged, including
    all declared graphs and histories. {"graphs": 1, "nodes": 5, "edges": 4, "pathway_steps":
    1, "molecular_targets": 2, "history": 2, "component_refs": 0} Technical readability
    does not prove cited experiments.'
  snapshot_sha256: 68398e58af6b7cc02b67978b7c92a04f2e9321941a9d230735eb808d12b8bf54
- evidence_id: EV288-initial-capture
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/inspect-2871-001/stderr
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:46:15.164110Z'
  support: context_only
  summary: An initial preparation capture rejected the redundant CLAUDE.md symlink
    before source capture. The successful capture uses its existing regular AGENTS.md
    source; no source content was changed.
  snapshot_sha256: ddd4bc83b3092140f3b71f2e59a9c970664a1bfb9a7e4f1a90fa6023a8ee761a
assessments:
- assessment_id: BGC288-AS-2871-identity
  area: identity
  topic: Stored identity and representation
  outcome: supported
  summary: CHEBI:222417 is the Cu-containing complex, not the free ligand or ferric
    fluopsin F. Both stored forms give C4H8CuN2O2S2 and net charge zero. The connected
    SMILES has 11 atoms/12 bonds and two Cu-containing five-member cycles; reconstructed
    InChI has 11 atoms/8 bonds, two anionic ligands and Cu2+ in three fragments. Canonical
    strings, bond counts and atom correspondence differ. The literal formula-layer
    comparator is also false for this multicomponent InChI; its parsed formula agrees.
    These observations do not show a wrong natural identity.
  target_ids:
  - CHEBI:222417
  evidence_ids:
  - BGC288-2871-owner
  - BGC288-2871-source
  - BGC288-2871-chemistry
  dimensions:
  - name: record_identity
    value: CHEBI:222417; retain exact source form and full key.
    definition: Identity scope of this one owner.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-source
    - BGC288-2871-chemistry
  - name: structure_representation
    value: Connected metal coordination versus three-component ionic reconstruction;
      11/12 versus 11/8 atoms/bonds. Both canonical comparisons false, map empty,
      full_graph_identity_established false.
    definition: Comparison of the two stored encodings, not a natural-identity proof.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-source
    - BGC288-2871-chemistry
  - name: stereochemistry
    value: No potential tetrahedral sites were reported. The curated true flag does
      not establish square-planar metal geometry or natural sample identity.
    definition: Specified and unspecified atom/bond scope.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-source
    - BGC288-2871-chemistry
- assessment_id: BGC288-AS-2871-provenance
  area: provenance
  topic: Source and producer claim ownership
  outcome: supported
  summary: Curated rows 12–13 distinguish PAO1 BGC_CHARACTERIZED (PMID:34793213; flcA–E
    deletion/reconstitution) from M18 AXENIC_CULTURE (PMID:5549384). The latter note
    only names Pseudomonas sp.; the retained excerpt does not itself establish the
    species/strain specificity. ChEBI P. fluorescens MCRL-10107 occurrence and P.
    aeruginosa occurrence remain separate claims, with no extra independent-publication
    credit for repeated citations.
  target_ids:
  - CHEBI:222417
  evidence_ids:
  - BGC288-2871-owner
  - BGC288-2871-source
  - BGC288-2871-curated
  - BGC288-2871-curated-policy
  dimensions:
  - name: source_versions
    value: ChEBI 3-star CHEBI:222417 chemistry is pinned by both curated-row digests.
      NPClassifier 2026-10-30 Alkaloids is a model prediction; the antibacterial sibling-corpus
      assertion has its own fixed version.
    definition: Retained source versions and model/experimental distinctions.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-source
    - BGC288-2871-curated
    - BGC288-2871-curated-policy
  - name: producer_evidence
    value: Curated causal grades remain attributed to the exact row, strain and citation;
      no current paper verification.
    definition: Evidence for production is separate from occurrence and locus metadata.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-source
    - BGC288-2871-curated
    - BGC288-2871-curated-policy
- assessment_id: BGC288-AS-2871-taxonomy
  area: grounding
  topic: Cached taxon and strain scope
  outcome: supported
  summary: Cached IDs 208964, 287 and 294 retain PAO1, P. aeruginosa and P. fluorescens
    respectively. Species-level cache labels do not prove M18 or MCRL-10107 producer
    attribution.
  target_ids:
  - CHEBI:222417
  evidence_ids:
  - BGC288-2871-owner
  - BGC288-2871-taxonomy
  - BGC288-2871-curated
  dimensions:
  - name: taxon_grounding
    value: Cached IDs 208964, 287 and 294 retain PAO1, P. aeruginosa and P. fluorescens
      respectively. Species-level cache labels do not prove M18 or MCRL-10107 producer
      attribution.
    definition: Local cached names do not establish fresh strain equivalence.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-taxonomy
    - BGC288-2871-curated
- assessment_id: BGC288-AS-2871-mechanism
  area: graph
  topic: Pathway and graph claims
  outcome: unknown
  summary: The one FlcA–E pathway step describes ligand synthesis followed by Cu complexation;
    its enzyme-group field does not imply one enzyme catalyses every transformation.
    The BIOACTIVITY graph links ligand/Cu to the complex and copper transport. The
    Fe edge describes metal exchange to distinct fluopsin F, so it must not be read
    as preservation of the Cu complex. The maintained reader preserved all 5 nodes,
    4 edges, one step and two histories; this verifies representation only.
  target_ids:
  - CHEBI:222417
  evidence_ids:
  - BGC288-2871-owner
  - BGC288-2871-reader
  - BGC288-2871-chemistry
  - BGC288-2871-ownership
  dimensions:
  - name: biosynthesis_mechanism
    value: FlcA–E/PA3515–PA3519 and spontaneous Cu complexation are retained literature-attributed
      steps; no current sequence comparison or paper inspection.
    definition: Claim-level scope of retained enzyme/pathway annotations.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-reader
    - BGC288-2871-chemistry
    - BGC288-2871-ownership
  - name: graph_causality
    value: Whole graph and history preserved; causal experiments and biological completeness
      not freshly verified.
    definition: Technical readability versus scientific causal support.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-reader
    - BGC288-2871-chemistry
    - BGC288-2871-ownership
- assessment_id: BGC288-AS-2871-activity
  area: evidence
  topic: Metal targets, activity and material scope
  outcome: unknown
  summary: The two curator-held targets distinguish Cu coordination from ferric transmetallation
    (PMIDs 5549384, 34793213 and 4927254). The exact AntibioticMech link asserts ANTIBACTERIAL
    at corpus commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976; it is not a retained
    quantitative assay. Exact-key PubChem/BindingDB frames are empty, which neither
    verifies nor refutes the recorded metal claims.
  target_ids:
  - CHEBI:222417
  evidence_ids:
  - BGC288-2871-owner
  - BGC288-2871-source
  - BGC288-2871-reader
  - BGC288-2871-chemistry
  dimensions:
  - name: molecular_targets
    value: Cu-bound owner, free ligand and Fe-bound fluopsin F remain distinct chemical
      entities.
    definition: Exact ligand/complex, target and experiment scope.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-source
    - BGC288-2871-reader
    - BGC288-2871-chemistry
  - name: bioactivity_scope
    value: No exact-key PubChem or BindingDB rows returned in the retained extraction;
      no universal activity absence inferred.
    definition: Bounds of local assay inventory and record-held evidence.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-source
    - BGC288-2871-reader
    - BGC288-2871-chemistry
- assessment_id: BGC288-AS-2871-ownership
  area: consistency
  topic: Maintained ownership and curation history
  outcome: supported
  summary: Imported ChEBI chemistry/definition and curated-table producer claims have
    different owners from record-held mechanisms. The two saved events record seeding
    and an agent-assisted RECORD_CURATED promotion to REVIEWED; that status is historical
    metadata, not this review’s validation of every citation. Any correction must
    follow its maintained source or the validated curator writer, preserving provenance.
  target_ids:
  - CHEBI:222417
  evidence_ids:
  - BGC288-2871-owner
  - BGC288-2871-ownership
  - BGC288-2871-curated-policy
  dimensions:
  - name: ownership_history
    value: Source changes use the maintained source/curation lane; mechanism changes
      use the validated writer plus artifact-specific history.
    definition: Correct owner of a future change; no edits performed.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-ownership
    - BGC288-2871-curated-policy
- assessment_id: BGC288-AS-2871-limits
  area: completeness
  topic: Review completeness
  outcome: unknown
  summary: All current source fields, complete owner/history, saved molecular tables
    and maintained returned owner were considered. Full QC, current OAK/remote taxonomy
    and primary literature verification are held by the no-request instruction. Local
    read/parse success does not certify catalytic specificity, binding constants,
    natural stereochemistry or all citations. Completion remains partial.
  target_ids:
  - CHEBI:222417
  evidence_ids:
  - BGC288-2871-owner
  - BGC288-2871-source
  - BGC288-2871-chemistry
  - BGC288-2871-reader
  - BGC288-2871-taxonomy
  dimensions:
  - name: review_completeness
    value: Partial scientific review of this one owner; external authorities and full
      QC unavailable.
    definition: Completed local scope and explicitly unperformed verification.
    evidence_ids:
    - BGC288-2871-owner
    - BGC288-2871-source
    - BGC288-2871-chemistry
    - BGC288-2871-reader
    - BGC288-2871-taxonomy
- assessment_id: AS288-local-consistency
  area: consistency
  topic: Bounded positive local validation and normalized chemical representation
  outcome: supported
  summary: The selected record is well-formed under the current closed schema and
    reproduces from maintained inputs. The two stored molecular encodings generate
    the declared Standard InChIKey and agree in parsed formula and net charge. These
    positive local results do not establish natural identity, exact graph equivalence,
    strain-specific production or primary-paper support.
  target_ids:
  - CHEBI:222417
  evidence_ids:
  - EV288-strict_ten
  - EV288-reproduction
  - EV288-molecular
findings: []
actions: []
limitations:
- No external request or fresh primary-literature/remote-taxonomy verification was
  performed; full QC and OAK remain unavailable.
- Only the two original stored encodings were parsed by the actual diagnostic. Global
  stderr warnings are retained without assigning individual warning lines to records;
  canonical similarity is not a natural-identity proof.
- Curator-held PRIMARY_EXPERIMENT labels, quantitative binding claims and REVIEWED
  status are retained assertions, not current authentication of source articles.
- Full QC, complete OAK label checks and fresh external-source verification are unavailable.
  Completion remains partial despite successful local gates.
- The review source is a working-tree input attestation at the captured Git base.
  Saved validation does not promote native record status or close unrelated historical
  findings.
notes:
- Complete first-five owner reading and actual complete_view equality were used together;
  no source/record/curation status was changed.
- Source extraction rows are overlapping retained evidence, not additional experiments.
  Review timestamps reflect this local access.
tags:
- batch-288
- local-evidence
- partial-review
```
