# Review rhabdopeptide 4 against retained local evidence

- Review: 20261107T112919Z-rhabdopeptide-4
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T11:21:25.805155Z
- Finished UTC: 2026-11-07T11:29:19.555526Z
- Reviewer: Codex ROOT with Bgc/Support scientific reviewers and Native local checks (unknown)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retained source identity and distinct N-methylated linear-peptide structure are locally coherent at the stated scope. Producer/locus grades remain database-attributed; canonical representation differences and limits of stored stereochemical assignments are explicit. Scientific completion remains partial.

## Scope And Provenance

Complete local reading of this one selected owner, its history and any declared mechanism components; scientific verification remains partial. The current campaign corpus contains 3136 records.

Selection: Batch289, order 2885: one of the first ten sorted currently unreviewed paths in the reconciled catalogue (1768 covered,1368 remaining before this batch). This bundle assesses only this target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 18ca5dd6b9023670f10355084b45a8757a7a4e9e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-df07ad2dd4 | data/natural_products/amino_acids_and_peptides/rhabdopeptide-4.yaml | generated | rhabdopeptide 4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical target and source capture | passed | True | naturalproductmech:mibig-df07ad2dd4 | Captured this exact generated target and its regular-file source inputs at the selected fresh main commit; current input hashes remain unchanged. |
| Maintained local gate: strict_ten | passed | True | naturalproductmech:mibig-df07ad2dd4 | All ten selected whole owners passed closed validation; zero error rows. |
| Maintained local gate: strict_full | passed | True | naturalproductmech:mibig-df07ad2dd4 | All 3136 current owners passed full closed validation with component-inventory audit; zero error rows. |
| Maintained local gate: lockfile | passed | True | naturalproductmech:mibig-df07ad2dd4 | All 3136 owner paths agree with PATHS.tsv and filing pins, including component inventory checks. |
| Maintained local gate: reproduction | passed | True | naturalproductmech:mibig-df07ad2dd4 | All 3136 records are byte-identical to the current seeder output. Carried curator mechanism claims are preserved, not independently proven. |
| Maintained local gate: queue | passed | True | naturalproductmech:mibig-df07ad2dd4 | The complete current review queue was generated locally: 8919 rows across 12 queues. Queue membership does not establish scientific review. |
| Local stored-form molecular diagnostic | passed | True | naturalproductmech:mibig-df07ad2dd4 | Exactly two stored encodings were parsed for this record (20 across the batch). Their normalized Standard InChI, key, computed formula and net charge agree; graph/canonical-SMILES equivalence and natural sample identity are not inferred. Record-specific differences remain in the scientific assessments. |
| Complete maintained mechanism read | not_applicable | False | naturalproductmech:mibig-df07ad2dd4 | The fully read owner has no graph, component-reference, pathway or molecular-target roots. No maintained mechanism-reader call was made for this target. The absence of these optional roots is not itself a scientific defect. |
| Full repository QC | unavailable | True | naturalproductmech:mibig-df07ad2dd4 | Not run: maintained full QC reaches the vendored-sync fetch. The five local gates do not substitute for full QC. |
| Complete OAK identifier-label correspondence | unavailable | True | naturalproductmech:mibig-df07ad2dd4 | Not run: a complete pinned offline CHEBI/GO adapter boundary was not established. No ontology download or remote resolver was permitted. |
| Fresh source, literature, taxonomy and structured database verification | unavailable | True | naturalproductmech:mibig-df07ad2dd4 | Not run under the source-request hold. Database assertions, gene/pathway annotations, citations, exact forms and strain claims are assessed only against retained local evidence; no fresh resolution or primary-paper authentication is claimed. |

## Scientific And Domain Assessments

### Exact identity, chemical representation and stereochemistry

identity: supported. Targets: naturalproductmech:mibig-df07ad2dd4.

Both neutral C39H68N6O5 forms have 50 atoms/50 bonds, a linear chain and one phenyl ring. Five SMILES amides become four retained N-methyl amides and one C(OH)=N site at the phenethylamide terminus. All five tetrahedral centres remain specified R. The additional potential C=N geometry belongs to the reconstruction; methylation/residue placement distinguishes this structure from compound 3. Both canonical SMILES comparisons are false and the chirality-aware atom map is empty; full_graph_identity_established remains false. Formula, charge, atom/bond counts, Standard InChI and full declared key agree. These bounded results do not prove natural-sample identity or exact graph equivalence.

### Producer, locus and source versions

provenance: supported. Targets: naturalproductmech:mibig-df07ad2dd4.

BGC0000416:4 version 5 is active, with questionable quality/complete entry metadata. Xenorhabdus nematophila ATCC 19061 (406817) is BGC_CHARACTERIZED; knockout and gene-expression-correlation methods retain CLUSTER_DEMONSTRATED locus linkage. PMID:24038745 is an entry-level database citation; compound-specific yield, knockout scope and enzyme function were not freshly verified. Questionable/complete/unknown are entry metadata, not automatic truth or defect signals.

### Minted identity and cached taxon scope

grounding: supported. Targets: naturalproductmech:mibig-df07ad2dd4.

Each indexed BGC0000416 compound has a distinct full key; the other three selected siblings are context, not equivalent identities. Cached 406817 explicitly names Xenorhabdus nematophila ATCC 19061 and supplies strain-name synonyms. Cached species 628 and DOI:10.1002/CBIC.201300205 support the separate LOTUS occurrence only; its independence from the entry citation is unverified.

### Pathway and mechanism applicability

graph: not_applicable. Targets: naturalproductmech:mibig-df07ad2dd4.

The entire owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway or molecular_targets. No maintained-reader call applies. A complete pathway is not required for this seeded record; neither the BGC interval nor the NRPS label establishes a missing enzyme, regulatory circuit or mechanism defect.

### Activity, exact source matches and equivalence limits

evidence: not_applicable. Targets: naturalproductmech:mibig-df07ad2dd4.

No bioactivities, bioactivity_summary or related_records root is retained. Exact full-key PubChem, BindingDB, AntibioticMech and PathwayMech frames contain no rows. This is bounded local absence, not evidence of inactivity. No bioactivity, receptor or mechanism is transferred among shared-BGC congeners.

### Classification, generated ownership and audit history

consistency: supported. Targets: naturalproductmech:mibig-df07ad2dd4.

NPClassifier Linear peptides (npclassifier.gnps2.org@2026-09-07) is a computed filing result, structurally compatible at this broad level. NRPS/Type I remains a separate MIBiG class. Both September 2026 SEEDED_FROM_SOURCES events and native SEEDED status remain historical. Exact correction selectors found no applicable row; no source-only defect requiring a curator action was established.

### Earned work and unresolved authority

completeness: unknown. Targets: naturalproductmech:mibig-df07ad2dd4.

Complete current owner/history, exact source frames, canonical intake and both saved molecular forms were assessed. No material defect was established within that local scope. Full QC, complete OAK checks and fresh primary/source/taxonomy verification remain unavailable or held. Normalized chemistry and cached database claims cannot replace them.

### Bounded positive local validation and normalized chemical representation

consistency: supported. Targets: naturalproductmech:mibig-df07ad2dd4.

The selected record is well-formed under the current closed schema and reproduces from maintained inputs. The two stored molecular encodings generate the declared Standard InChIKey and agree in parsed formula and net charge. These positive local results do not establish natural identity, exact graph equivalence, strain-specific production or primary-paper support.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| BGC289-2885-owner | data/natural_products/amino_acids_and_peptides/rhabdopeptide-4.yaml; Complete owner, all top-level fields and both curation_history events. | partial | Whole owner personally read; exact current raw pin agrees with accepted intake and diagnostic. Native SEEDED status and both historical seed events remain unchanged. |
| BGC289-2885-sources | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch289-conditional-preflight/bgc-prep/conditional289-first-five-retained-source-capture-001.json; records[4].frames[0:20]; physical_rows keyed by source path and exact physical span. | partial | All 20 selector frames read: 7 row placements/138 fields, including repeated BGC metadata. No exact selected assay, target, ChEBI or implemented correction row. Repeated rows are not independent support. |
| BGC289-2885-mibig | data/raw/mibig_compounds.tsv; Physical line 564; all 25 fields; source_id BGC0000416:4. | partial | Exact compound row, structure strings, source version/status, strain, locus methods and entry-level citation read. BGC metadata and primary-reference labels are database assertions, not freshly read experiments. |
| BGC289-2885-chemistry | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/chemistry-local/diagnostic-DATA-001.json; records[4].smiles.computed and .inchi.computed: all atoms, bonds, rings, potential_stereo, motifs; .comparisons and .atom_correspondence. | partial | Both complete saved forms personally read. The original diagnostic parsed only the two stored strings; no alternative structure or new parse was attempted by this reviewer. |
| BGC289-2885-taxonomy | data/raw/corpus_taxa.obo; Complete [Term] stanzas NCBITaxon:406817, NCBITaxon:628. | partial | Complete cached names and EXACT synonyms read. Cache agreement supports retained label/strain scope only; no live taxonomic resolution or general strain-to-species equivalence is inferred. |
| BGC289-2885-intake | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/inspect-2885-001/stdout; source and targets, complete canonical inspection result. | partial | Actual successful canonical capture of the exact target and 70 regular-file inputs at base18ca; all current pins match. Inspection establishes provenance, not scientific truth. |
| BGC289-2885-stereo-method | scripts/extract_mibig.py; structure_fields, lines 142–173. | partial | stereo_complete uses FindMolChiralCenters with includeUnassigned=True and question-mark atom tags. It does not certify every double-bond geometry or independently establish natural configuration. |
| BGC289-2885-source-method | scripts/seed_from_sources.py; Lines 790–850 and 1040–1155: corrections, exact accession:index identity, producer and locus emission. | partial | Imported fields follow maintained source and implemented correction inputs. Producer evidence_basis and locus link_evidence_basis remain separate. Reserved decisions.tsv is not an effective correction route. |
| EV289-intake | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/inspect-2885-001/stdout; Retained original execution output; exact SHA256 below. | supports | Captured this exact generated target and its regular-file source inputs at the selected fresh main commit; current input hashes remain unchanged. |
| EV289-strict_ten | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-strict-ten-001/stderr; Retained original execution output; exact SHA256 below. | supports | All ten selected whole owners passed closed validation; zero error rows. |
| EV289-strict_full | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-strict-full-001/stderr; Retained original execution output; exact SHA256 below. | supports | All 3136 current owners passed full closed validation with component-inventory audit; zero error rows. |
| EV289-lockfile | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-lockfile-001/stdout; Retained original execution output; exact SHA256 below. | supports | All 3136 owner paths agree with PATHS.tsv and filing pins, including component inventory checks. |
| EV289-reproduction | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-reproduction-001/stdout; Retained original execution output; exact SHA256 below. | supports | All 3136 records are byte-identical to the current seeder output. Carried curator mechanism claims are preserved, not independently proven. |
| EV289-queue | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-queue-001/stdout; Retained original execution output; exact SHA256 below. | supports | The complete current review queue was generated locally: 8919 rows across 12 queues. Queue membership does not establish scientific review. |
| EV289-molecular | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/chemistry-local/diagnostic-DATA-001.json; Retained original execution output; exact SHA256 below. | supports | Exactly two stored encodings were parsed for this record (20 across the batch). Their normalized Standard InChI, key, computed formula and net charge agree; graph/canonical-SMILES equivalence and natural sample identity are not inferred. Record-specific differences remain in the scientific assessments. |

## Limits And Additional Notes

- Both canonical SMILES comparisons are false and the chirality-aware atom map is empty; full_graph_identity_established remains false. Formula, charge, atom/bond counts, Standard InChI and full declared key agree. These bounded results do not prove natural-sample identity or exact graph equivalence.
- Full QC, complete OAK checks and fresh primary/source/taxonomy verification remain unavailable or held. Normalized chemistry and cached database claims cannot replace them.
- No primary paper, sequence accession, NPAtlas record, assay or current external taxon authority was retrieved. Database assertions and historical seed events are not promoted to fresh experimental verification.
- No record or native status was changed, and this new observation does not close earlier findings. ROOT supplies the original common check records; this fragment does not invent their commands or results.
- Full QC, complete OAK label checks and fresh external-source verification are unavailable. Completion remains partial despite successful local gates.
- The review source is a working-tree input attestation at the captured Git base. Saved validation does not promote native record status or close unrelated historical findings.
- Source base 18ca5dd6b9023670f10355084b45a8757a7a4e9e; the earlier conditional source capture was carried only after actual input hashes matched.
- Both actual stored forms parsed with empty diagnostic stderr. No alternate parse or maintained-reader target was run by this reviewer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T112919Z-rhabdopeptide-4
kind: record
repository: CultureBotAI/NaturalProductMech
title: Review rhabdopeptide 4 against retained local evidence
started_at: '2026-11-07T11:21:25.805155Z'
finished_at: '2026-11-07T11:29:19.555526Z'
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
summary: Retained source identity and distinct N-methylated linear-peptide structure
  are locally coherent at the stated scope. Producer/locus grades remain database-attributed;
  canonical representation differences and limits of stored stereochemical assignments
  are explicit. Scientific completion remains partial.
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
  - path: data/natural_products/amino_acids_and_peptides/rhabdopeptide-1.yaml
    sha256: 919794fcc106d80b286a927225c50a3cc1cdd3f29f22f1c90baf123e7c7215f1
    role: context
  - path: data/natural_products/amino_acids_and_peptides/rhabdopeptide-2.yaml
    sha256: ad172f31b4fa71dd464229e065e39b798d7c9361436671918c844dcb4e940d7f
    role: context
  - path: data/natural_products/amino_acids_and_peptides/rhabdopeptide-3.yaml
    sha256: ecaa76cedffcd70e55be3f693ec57f618f8fbbe81d0e53c6eab0875f368b2383
    role: context
  - path: data/natural_products/amino_acids_and_peptides/rhabdopeptide-4.yaml
    sha256: 49eb7e7a3289da273d915433c1615a66d5699b5401daa40fe26b7e6464c641e4
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
    current campaign corpus contains 3136 records.
  selection: 'Batch289, order 2885: one of the first ten sorted currently unreviewed
    paths in the reconciled catalogue (1768 covered,1368 remaining before this batch).
    This bundle assesses only this target.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-df07ad2dd4
targets:
- target_id: naturalproductmech:mibig-df07ad2dd4
  path: data/natural_products/amino_acids_and_peptides/rhabdopeptide-4.yaml
  label: rhabdopeptide 4
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained source harmonization and guarded emission of generated records.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Maintained MIBiG structure, producer and locus evidence extraction.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned imported structure and compound-specific BGC assertions; correct
      through the maintained extractor or implemented supported curation inputs.
  ownership_note: Review only. Mechanism roots are absent in the complete selected
    owner. Source-specific correction actions must name the applicable implemented
    input; reserved curation/decisions.tsv is not consumed.
checks:
- check_id: CK289-intake
  name: Canonical target and source capture
  status: passed
  required: true
  summary: Captured this exact generated target and its regular-file source inputs
    at the selected fresh main commit; current input hashes remain unchanged.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  command: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/.venv/bin/python
    scripts/record_review.py inspect --targets /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/intakes-001/2885-targets-001.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/review-yaml-record/SKILL.md --input AGENTS.md --input conf/id_label_targets.yaml
    --input conf/np_roles.tsv --input conf/producer_evidence.tsv --input conf/record_review.yaml
    --input conf/sources.yaml --input curation/curated_compounds.tsv --input curation/lotus_occurrence_exclusions.tsv
    --input curation/mibig_claim_references.tsv --input curation/mibig_locus_evidence_overrides.tsv
    --input curation/mibig_producer_isolates.tsv --input curation/mibig_producer_strains.tsv
    --input curation/mibig_structure_corrections.tsv --input curation/mibig_xref_exclusions.tsv
    --input curation/pubchem_bioassay_exclusions.tsv --input curation/unresolved_taxa.tsv
    --input data/natural_products/PATHS.tsv --input data/natural_products/amino_acids_and_peptides/rhabdopeptide-1.yaml
    --input data/natural_products/amino_acids_and_peptides/rhabdopeptide-2.yaml --input
    data/natural_products/amino_acids_and_peptides/rhabdopeptide-3.yaml --input data/raw/MANIFEST.yaml
    --input data/raw/antibioticmech_inchikeys.tsv --input data/raw/bindingdb_targets.tsv
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
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-intake
- check_id: CK289-strict_ten
  name: 'Maintained local gate: strict_ten'
  status: passed
  required: true
  summary: All ten selected whole owners passed closed validation; zero error rows.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  command: /opt/homebrew/bin/just validate-strict data/natural_products/amino_acids_and_peptides/rc-aip1.yaml
    data/natural_products/amino_acids_and_peptides/rhabdopeptide-1.yaml data/natural_products/amino_acids_and_peptides/rhabdopeptide-2.yaml
    data/natural_products/amino_acids_and_peptides/rhabdopeptide-3.yaml data/natural_products/amino_acids_and_peptides/rhabdopeptide-4.yaml
    data/natural_products/amino_acids_and_peptides/rhizocticin-a.yaml data/natural_products/amino_acids_and_peptides/ririwpeptide-a.yaml
    data/natural_products/amino_acids_and_peptides/ririwpeptide-b.yaml data/natural_products/amino_acids_and_peptides/ristocetin-a.yaml
    data/natural_products/amino_acids_and_peptides/ristocetin-b.yaml --workers 2 --quiet
    --out /Users/marcin/agent-work/NaturalProductMech/npm-native-checks/batch-289/selected-strict-001.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-strict_ten
- check_id: CK289-strict_full
  name: 'Maintained local gate: strict_full'
  status: passed
  required: true
  summary: All 3136 current owners passed full closed validation with component-inventory
    audit; zero error rows.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  command: /opt/homebrew/bin/just validate-strict --workers 2 --quiet --out /Users/marcin/agent-work/NaturalProductMech/npm-native-checks/batch-289/full-strict-001.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-strict_full
- check_id: CK289-lockfile
  name: 'Maintained local gate: lockfile'
  status: passed
  required: true
  summary: All 3136 owner paths agree with PATHS.tsv and filing pins, including component
    inventory checks.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  command: /opt/homebrew/bin/just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-lockfile
- check_id: CK289-reproduction
  name: 'Maintained local gate: reproduction'
  status: passed
  required: true
  summary: All 3136 records are byte-identical to the current seeder output. Carried
    curator mechanism claims are preserved, not independently proven.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  command: /opt/homebrew/bin/just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-reproduction
- check_id: CK289-queue
  name: 'Maintained local gate: queue'
  status: passed
  required: true
  summary: 'The complete current review queue was generated locally: 8919 rows across
    12 queues. Queue membership does not establish scientific review.'
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  command: /opt/homebrew/bin/just review-queue --tsv /Users/marcin/agent-work/NaturalProductMech/npm-native-checks/batch-289/review-queue-001.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-queue
- check_id: CK289-molecular
  name: Local stored-form molecular diagnostic
  status: passed
  required: true
  summary: Exactly two stored encodings were parsed for this record (20 across the
    batch). Their normalized Standard InChI, key, computed formula and net charge
    agree; graph/canonical-SMILES equivalence and natural sample identity are not
    inferred. Record-specific differences remain in the scientific assessments.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  command: /usr/bin/sandbox-exec -p '(version 1)(allow default)(deny network*)' /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/.venv/bin/python
    -I -S -B /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/diagnose289-001.py
    diagnostic
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV289-molecular
- check_id: CK289-reader
  name: Complete maintained mechanism read
  status: not_applicable
  required: false
  summary: The fully read owner has no graph, component-reference, pathway or molecular-target
    roots. No maintained mechanism-reader call was made for this target. The absence
    of these optional roots is not itself a scientific defect.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
- check_id: CK289-full-qc
  name: Full repository QC
  status: unavailable
  required: true
  summary: 'Not run: maintained full QC reaches the vendored-sync fetch. The five
    local gates do not substitute for full QC.'
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
- check_id: CK289-ontology
  name: Complete OAK identifier-label correspondence
  status: unavailable
  required: true
  summary: 'Not run: a complete pinned offline CHEBI/GO adapter boundary was not established.
    No ontology download or remote resolver was permitted.'
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
- check_id: CK289-fresh-authorities
  name: Fresh source, literature, taxonomy and structured database verification
  status: unavailable
  required: true
  summary: Not run under the source-request hold. Database assertions, gene/pathway
    annotations, citations, exact forms and strain claims are assessed only against
    retained local evidence; no fresh resolution or primary-paper authentication is
    claimed.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
evidence:
- evidence_id: BGC289-2885-owner
  kind: record_content
  reference: data/natural_products/amino_acids_and_peptides/rhabdopeptide-4.yaml
  locator: Complete owner, all top-level fields and both curation_history events.
  accessed_at: '2026-11-07T11:28:11.521419Z'
  support: partial
  summary: Whole owner personally read; exact current raw pin agrees with accepted
    intake and diagnostic. Native SEEDED status and both historical seed events remain
    unchanged.
  snapshot_sha256: 49eb7e7a3289da273d915433c1615a66d5699b5401daa40fe26b7e6464c641e4
- evidence_id: BGC289-2885-sources
  kind: search
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch289-conditional-preflight/bgc-prep/conditional289-first-five-retained-source-capture-001.json
  locator: records[4].frames[0:20]; physical_rows keyed by source path and exact physical
    span.
  accessed_at: '2026-11-07T11:28:11.521419Z'
  support: partial
  summary: 'All 20 selector frames read: 7 row placements/138 fields, including repeated
    BGC metadata. No exact selected assay, target, ChEBI or implemented correction
    row. Repeated rows are not independent support.'
  snapshot_sha256: 527c571154821c82a0850615600be75a15640c587006c9858134d25007c7e1c0
  search_scope: Nineteen named local TSV files pinned in this capture, read directly
    without gitignore filtering. Exact full InChIKey, selected identifier, accession:compound_index
    and owned-BGC predicates are recorded in every frame. Negative results apply only
    to these retained files and predicates; no remote or global literature absence
    claim.
- evidence_id: BGC289-2885-mibig
  kind: database
  reference: data/raw/mibig_compounds.tsv
  locator: Physical line 564; all 25 fields; source_id BGC0000416:4.
  accessed_at: '2026-11-07T11:28:11.521419Z'
  support: partial
  summary: Exact compound row, structure strings, source version/status, strain, locus
    methods and entry-level citation read. BGC metadata and primary-reference labels
    are database assertions, not freshly read experiments.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: BGC289-2885-chemistry
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/chemistry-local/diagnostic-DATA-001.json
  locator: 'records[4].smiles.computed and .inchi.computed: all atoms, bonds, rings,
    potential_stereo, motifs; .comparisons and .atom_correspondence.'
  accessed_at: '2026-11-07T11:28:11.521419Z'
  support: partial
  summary: Both complete saved forms personally read. The original diagnostic parsed
    only the two stored strings; no alternative structure or new parse was attempted
    by this reviewer.
  snapshot_sha256: 4c5fc29dbe122c1cf52903fa7f8c29ee51d8bc5ed33fec85a221d4b65b591ba2
- evidence_id: BGC289-2885-taxonomy
  kind: authority
  reference: data/raw/corpus_taxa.obo
  locator: Complete [Term] stanzas NCBITaxon:406817, NCBITaxon:628.
  accessed_at: '2026-11-07T11:28:11.521419Z'
  support: partial
  summary: Complete cached names and EXACT synonyms read. Cache agreement supports
    retained label/strain scope only; no live taxonomic resolution or general strain-to-species
    equivalence is inferred.
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: BGC289-2885-intake
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/inspect-2885-001/stdout
  locator: source and targets, complete canonical inspection result.
  accessed_at: '2026-11-07T11:28:11.521419Z'
  support: partial
  summary: Actual successful canonical capture of the exact target and 70 regular-file
    inputs at base18ca; all current pins match. Inspection establishes provenance,
    not scientific truth.
  snapshot_sha256: 1ca4bb5a81ac5bb028d49384c8609806f7882e72cc8400dfd8e3634f1bdec0ef
- evidence_id: BGC289-2885-stereo-method
  kind: record_content
  reference: scripts/extract_mibig.py
  locator: structure_fields, lines 142–173.
  accessed_at: '2026-11-07T11:28:11.521419Z'
  support: partial
  summary: stereo_complete uses FindMolChiralCenters with includeUnassigned=True and
    question-mark atom tags. It does not certify every double-bond geometry or independently
    establish natural configuration.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: BGC289-2885-source-method
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: 'Lines 790–850 and 1040–1155: corrections, exact accession:index identity,
    producer and locus emission.'
  accessed_at: '2026-11-07T11:28:11.521419Z'
  support: partial
  summary: Imported fields follow maintained source and implemented correction inputs.
    Producer evidence_basis and locus link_evidence_basis remain separate. Reserved
    decisions.tsv is not an effective correction route.
  snapshot_sha256: d6650a80685b7f778050f79cc72de1fc3bbf281c57336401a5c773755de56324
- evidence_id: EV289-intake
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/inspect-2885-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:21:26.979098Z'
  support: supports
  summary: Captured this exact generated target and its regular-file source inputs
    at the selected fresh main commit; current input hashes remain unchanged.
  snapshot_sha256: 1ca4bb5a81ac5bb028d49384c8609806f7882e72cc8400dfd8e3634f1bdec0ef
- evidence_id: EV289-strict_ten
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-strict-ten-001/stderr
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:22:30.692246Z'
  support: supports
  summary: All ten selected whole owners passed closed validation; zero error rows.
  snapshot_sha256: 64fa4be75844498991904765d1286900d9908e3a3d6a6cc5e74e4479178ee54b
- evidence_id: EV289-strict_full
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-strict-full-001/stderr
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:22:52.233216Z'
  support: supports
  summary: All 3136 current owners passed full closed validation with component-inventory
    audit; zero error rows.
  snapshot_sha256: d957eed8e15bb928f2ae3c3f22989ac01713bea2f869c39f80fa858c596a2311
- evidence_id: EV289-lockfile
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-lockfile-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:23:14.056358Z'
  support: supports
  summary: All 3136 owner paths agree with PATHS.tsv and filing pins, including component
    inventory checks.
  snapshot_sha256: 06b20cd71ef4e0ce9f998515c0dbd4076f81b0f420e22e4949fc19494217de24
- evidence_id: EV289-reproduction
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-reproduction-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:23:51.297984Z'
  support: supports
  summary: All 3136 records are byte-identical to the current seeder output. Carried
    curator mechanism claims are preserved, not independently proven.
  snapshot_sha256: 6375bbedfde712e0de5fd1fd6c8f939e45bd2cab4fecb4be7f8fc5b11ab7337d
- evidence_id: EV289-queue
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/local-executions/native-queue-001/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:24:04.393915Z'
  support: supports
  summary: 'The complete current review queue was generated locally: 8919 rows across
    12 queues. Queue membership does not establish scientific review.'
  snapshot_sha256: 386216f171f1a0c3aac15fbc6e76ee6eedda8235755ec8abb80a2c173f297369
- evidence_id: EV289-molecular
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch289/chemistry-local/diagnostic-DATA-001.json
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T11:25:50.467442Z'
  support: supports
  summary: Exactly two stored encodings were parsed for this record (20 across the
    batch). Their normalized Standard InChI, key, computed formula and net charge
    agree; graph/canonical-SMILES equivalence and natural sample identity are not
    inferred. Record-specific differences remain in the scientific assessments.
  snapshot_sha256: 4c5fc29dbe122c1cf52903fa7f8c29ee51d8bc5ed33fec85a221d4b65b591ba2
assessments:
- assessment_id: BGC289-2885-AS-identity
  area: identity
  topic: Exact identity, chemical representation and stereochemistry
  outcome: supported
  summary: Both neutral C39H68N6O5 forms have 50 atoms/50 bonds, a linear chain and
    one phenyl ring. Five SMILES amides become four retained N-methyl amides and one
    C(OH)=N site at the phenethylamide terminus. All five tetrahedral centres remain
    specified R. The additional potential C=N geometry belongs to the reconstruction;
    methylation/residue placement distinguishes this structure from compound 3. Both
    canonical SMILES comparisons are false and the chirality-aware atom map is empty;
    full_graph_identity_established remains false. Formula, charge, atom/bond counts,
    Standard InChI and full declared key agree. These bounded results do not prove
    natural-sample identity or exact graph equivalence.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  evidence_ids:
  - BGC289-2885-owner
  - BGC289-2885-mibig
  - BGC289-2885-chemistry
  - BGC289-2885-stereo-method
  dimensions:
  - name: full_key
    definition: Exact retained normalized key.
    value: HBHJZHOBEKLHMW-SLXQPGMDSA-N
    evidence_ids:
    - BGC289-2885-owner
    - BGC289-2885-mibig
    - BGC289-2885-chemistry
  - name: comparison_limits
    definition: Scope of stored-form agreement.
    value: Both canonical SMILES comparisons are false and the chirality-aware atom
      map is empty; full_graph_identity_established remains false. Formula, charge,
      atom/bond counts, Standard InChI and full declared key agree. These bounded
      results do not prove natural-sample identity or exact graph equivalence.
    evidence_ids:
    - BGC289-2885-chemistry
  - name: stereochemistry
    definition: Assigned versus unresolved atomic centres.
    value: 5 specified R centres; source flag true covers atomic centres only.
    evidence_ids:
    - BGC289-2885-chemistry
    - BGC289-2885-stereo-method
- assessment_id: BGC289-2885-AS-provenance
  area: provenance
  topic: Producer, locus and source versions
  outcome: supported
  summary: BGC0000416:4 version 5 is active, with questionable quality/complete entry
    metadata. Xenorhabdus nematophila ATCC 19061 (406817) is BGC_CHARACTERIZED; knockout
    and gene-expression-correlation methods retain CLUSTER_DEMONSTRATED locus linkage.
    PMID:24038745 is an entry-level database citation; compound-specific yield, knockout
    scope and enzyme function were not freshly verified. Questionable/complete/unknown
    are entry metadata, not automatic truth or defect signals.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  evidence_ids:
  - BGC289-2885-owner
  - BGC289-2885-mibig
  - BGC289-2885-sources
  - BGC289-2885-source-method
  dimensions:
  - name: source_grade
    definition: Database producer/locus evidence distinction.
    value: BGC_CHARACTERIZED / CLUSTER_DEMONSTRATED; entry-level citation, not fresh
      primary verification.
    evidence_ids:
    - BGC289-2885-mibig
    - BGC289-2885-source-method
  - name: strain_scope
    definition: Producer versus occurrence grain.
    value: ATCC 19061/406817 is the strain-level producer; species 628 is a separate
      LOTUS occurrence.
    evidence_ids:
    - BGC289-2885-owner
    - BGC289-2885-mibig
    - BGC289-2885-sources
- assessment_id: BGC289-2885-AS-grounding
  area: grounding
  topic: Minted identity and cached taxon scope
  outcome: supported
  summary: Each indexed BGC0000416 compound has a distinct full key; the other three
    selected siblings are context, not equivalent identities. Cached 406817 explicitly
    names Xenorhabdus nematophila ATCC 19061 and supplies strain-name synonyms. Cached
    species 628 and DOI:10.1002/CBIC.201300205 support the separate LOTUS occurrence
    only; its independence from the entry citation is unverified.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  evidence_ids:
  - BGC289-2885-owner
  - BGC289-2885-mibig
  - BGC289-2885-sources
  - BGC289-2885-taxonomy
  dimensions:
  - name: taxon_resolution
    definition: Bounded cached names and source strains.
    value: ATCC 19061/406817 is the strain-level producer; species 628 is a separate
      LOTUS occurrence.
    evidence_ids:
    - BGC289-2885-taxonomy
    - BGC289-2885-owner
- assessment_id: BGC289-2885-AS-graph
  area: graph
  topic: Pathway and mechanism applicability
  outcome: not_applicable
  summary: The entire owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway
    or molecular_targets. No maintained-reader call applies. A complete pathway is
    not required for this seeded record; neither the BGC interval nor the NRPS label
    establishes a missing enzyme, regulatory circuit or mechanism defect.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  evidence_ids:
  - BGC289-2885-owner
  - BGC289-2885-sources
  dimensions:
  - name: mechanism_scope
    definition: Observed owner roots, not global biological absence.
    value: All mechanism/component roots absent in the complete owner; no function
      inferred.
    evidence_ids:
    - BGC289-2885-owner
- assessment_id: BGC289-2885-AS-activity
  area: evidence
  topic: Activity, exact source matches and equivalence limits
  outcome: not_applicable
  summary: No bioactivities, bioactivity_summary or related_records root is retained.
    Exact full-key PubChem, BindingDB, AntibioticMech and PathwayMech frames contain
    no rows. This is bounded local absence, not evidence of inactivity. No bioactivity,
    receptor or mechanism is transferred among shared-BGC congeners.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  evidence_ids:
  - BGC289-2885-owner
  - BGC289-2885-sources
  dimensions:
  - name: activity_scope
    definition: Experiment and context authority.
    value: No selected retained assay or target evidence; fresh activity/source verification
      held.
    evidence_ids:
    - BGC289-2885-sources
    - BGC289-2885-owner
- assessment_id: BGC289-2885-AS-consistency
  area: consistency
  topic: Classification, generated ownership and audit history
  outcome: supported
  summary: NPClassifier Linear peptides (npclassifier.gnps2.org@2026-09-07) is a computed
    filing result, structurally compatible at this broad level. NRPS/Type I remains
    a separate MIBiG class. Both September 2026 SEEDED_FROM_SOURCES events and native
    SEEDED status remain historical. Exact correction selectors found no applicable
    row; no source-only defect requiring a curator action was established.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  evidence_ids:
  - BGC289-2885-owner
  - BGC289-2885-sources
  - BGC289-2885-mibig
  - BGC289-2885-source-method
  dimensions:
  - name: classification
    definition: Computed filing versus asserted BGC class.
    value: NPClassifier Linear peptides (npclassifier.gnps2.org@2026-09-07) is a computed
      filing result, structurally compatible at this broad level. NRPS/Type I remains
      a separate MIBiG class.
    evidence_ids:
    - BGC289-2885-sources
    - BGC289-2885-mibig
  - name: audit_ownership
    definition: Status and effective correction route.
    value: Two historical seed events; maintained extractor/seeder and implemented
      exact-row corrections own future fixes. No record/status edit.
    evidence_ids:
    - BGC289-2885-owner
    - BGC289-2885-source-method
- assessment_id: BGC289-2885-AS-completeness
  area: completeness
  topic: Earned work and unresolved authority
  outcome: unknown
  summary: Complete current owner/history, exact source frames, canonical intake and
    both saved molecular forms were assessed. No material defect was established within
    that local scope. Full QC, complete OAK checks and fresh primary/source/taxonomy
    verification remain unavailable or held. Normalized chemistry and cached database
    claims cannot replace them.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  evidence_ids:
  - BGC289-2885-owner
  - BGC289-2885-sources
  - BGC289-2885-intake
  - BGC289-2885-chemistry
  - BGC289-2885-taxonomy
  dimensions:
  - name: earned_scope
    definition: Personally read evidence.
    value: Whole owner, 20 source frames, both complete saved forms; 70 actual input
      pins current.
    evidence_ids:
    - BGC289-2885-owner
    - BGC289-2885-sources
    - BGC289-2885-intake
    - BGC289-2885-chemistry
  - name: unavailable_scope
    definition: Checks not claimed.
    value: Full QC, complete OAK checks and fresh primary/source/taxonomy verification
      remain unavailable or held. Normalized chemistry and cached database claims
      cannot replace them.
    evidence_ids:
    - BGC289-2885-intake
    - BGC289-2885-sources
- assessment_id: AS289-local-consistency
  area: consistency
  topic: Bounded positive local validation and normalized chemical representation
  outcome: supported
  summary: The selected record is well-formed under the current closed schema and
    reproduces from maintained inputs. The two stored molecular encodings generate
    the declared Standard InChIKey and agree in parsed formula and net charge. These
    positive local results do not establish natural identity, exact graph equivalence,
    strain-specific production or primary-paper support.
  target_ids:
  - naturalproductmech:mibig-df07ad2dd4
  evidence_ids:
  - EV289-strict_ten
  - EV289-reproduction
  - EV289-molecular
findings: []
actions: []
limitations:
- Both canonical SMILES comparisons are false and the chirality-aware atom map is
  empty; full_graph_identity_established remains false. Formula, charge, atom/bond
  counts, Standard InChI and full declared key agree. These bounded results do not
  prove natural-sample identity or exact graph equivalence.
- Full QC, complete OAK checks and fresh primary/source/taxonomy verification remain
  unavailable or held. Normalized chemistry and cached database claims cannot replace
  them.
- No primary paper, sequence accession, NPAtlas record, assay or current external
  taxon authority was retrieved. Database assertions and historical seed events are
  not promoted to fresh experimental verification.
- No record or native status was changed, and this new observation does not close
  earlier findings. ROOT supplies the original common check records; this fragment
  does not invent their commands or results.
- Full QC, complete OAK label checks and fresh external-source verification are unavailable.
  Completion remains partial despite successful local gates.
- The review source is a working-tree input attestation at the captured Git base.
  Saved validation does not promote native record status or close unrelated historical
  findings.
notes:
- Source base 18ca5dd6b9023670f10355084b45a8757a7a4e9e; the earlier conditional source
  capture was carried only after actual input hashes matched.
- Both actual stored forms parsed with empty diagnostic stderr. No alternate parse
  or maintained-reader target was run by this reviewer.
tags:
- batch-289
- local-evidence
- partial-review
```
