# Review desferricoprogen B against retained local evidence

- Review: 20261107T105931Z-desferricoprogen-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T10:47:12.603831Z
- Finished UTC: 2026-11-07T10:59:31.480359Z
- Reviewer: Codex ROOT with Bgc/Support scientific reviewers and Native local checks (unknown)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Coherent retained desferricoprogen B scaffold and fungal source assertions, with two diketopiperazine amide/imidic changes and bounded ferric-complex claims. Scientific review is partial because full QC, complete OAK and fresh primary/external verification remain unavailable or held.

## Scope And Provenance

Complete local reading of this one selected owner, its history and any declared mechanism components; scientific verification remains partial. The current campaign corpus contains3136 records.

Selection: Batch288, order2877: one of the first ten sorted currently unreviewed paths in the reconciled catalogue (1758 covered,1378 remaining before this batch). This bundle assesses only this target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 18ca5dd6b9023670f10355084b45a8757a7a4e9e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:133861 | data/natural_products/amino_acids_and_peptides/desferricoprogen-b.yaml | generated | desferricoprogen B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical target and source capture | passed | True | CHEBI:133861 | Captured this exact generated target and its regular-file source inputs at fresh main18ca; current input hashes remain unchanged. |
| Maintained local gate: strict_ten | passed | True | CHEBI:133861 | All ten selected whole owners passed closed validation; zero error rows. |
| Maintained local gate: strict_full | passed | True | CHEBI:133861 | All3136 current owners passed full closed validation with component-inventory audit; zero error rows. |
| Maintained local gate: lockfile | passed | True | CHEBI:133861 | All3136 owner paths agree with PATHS.tsv and filing pins, including component inventory checks. |
| Maintained local gate: reproduction | passed | True | CHEBI:133861 | All3136 records are byte-identical to the current seeder output. Carried curator mechanism claims are preserved, not independently proven. |
| Maintained local gate: queue | passed | True | CHEBI:133861 | The complete current review queue was generated locally:8919 rows across12 queues. Queue membership does not establish scientific review. |
| Local stored-form molecular diagnostic | passed | True | CHEBI:133861 | Exactly two stored encodings were parsed for this record (20 across the batch). Their normalized Standard InChI, key, computed formula and net charge agree; graph/canonical-SMILES equivalence and natural sample identity are not inferred. Record-specific differences remain in the scientific assessments. |
| Complete maintained mechanism read | passed | True | CHEBI:133861 | The actual maintained reader returned this whole owner unchanged, including all declared graphs and histories. {"graphs": 1, "nodes": 7, "edges": 6, "pathway_steps": 1, "molecular_targets": 1, "history": 2, "component_refs": 0} Technical readability does not prove cited experiments. |
| Full repository QC | unavailable | True | CHEBI:133861 | Not run: maintained full QC reaches the vendored-sync fetch. The five local gates do not substitute for full QC. |
| Complete OAK identifier-label correspondence | unavailable | True | CHEBI:133861 | Not run: a complete pinned offline CHEBI/GO adapter boundary was not established. No ontology download or remote resolver was permitted. |
| Fresh source, literature, taxonomy and structured database verification | unavailable | True | CHEBI:133861 | Not run under the source-request hold. Database assertions, gene/pathway annotations, citations, exact forms and strain claims are assessed only against retained local evidence; no fresh resolution or primary-paper authentication is claimed. |

## Scientific And Domain Assessments

### Exact source identity and congener boundary

identity: supported. Targets: CHEBI:133861.

CHEBI:133861 and XRSRJBBRTCEBNS-CAGSISFISA-N join the exact ChEBI row and two digest-checked curated entries. The definition describes a diketopiperazine dimer esterified to a third hydroxyornithine-derived unit, consistent with the saved scaffold. This supports retained source identity rather than a newly identified natural sample.

### Complete saved-form chemical interpretation

representation: supported. Targets: CHEBI:133861.

Both neutral C33H54N6O12 forms contain 51 atoms/51 bonds in one component, one six-member diketopiperazine ring and no metal. SMILES six carbonyls/five strict amides/one ester become four carbonyls/three strict amides plus two C(OH)=N sites at the secondary ring amides. Three N-hydroxy acyl groups, one primary amine and the ester remain; there is no free carboxylic acid. Three tetrahedral centres and three actual STEREOE side-chain bonds remain specified in both forms. Local potential-stereo Bond_Cis descriptors are not relabelled as Z. The true atom-centre stereo_complete flag does not independently establish natural absolute configuration. Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized Standard InChI/key, declared key, formula, charge and atom/bond counts agree. The saved chirality-aware atom map is empty and full_graph_identity_established is false. Motif-level interpretation does not establish full graph or natural-sample identity.

### Producer, locus, occurrence and source grain

provenance: supported. Targets: CHEBI:133861.

Curated rows 26–27 assert Neurospora crassa ATCC 10816 (5141), AXENIC_CULTURE/PMID:5484314, and Aspergillus niger N402 (5061), BGC_CHARACTERIZED/PMID:25062661, with SidA/SidD deletion in the latter note. There is no concrete BGC accession; the grade does not invent one. The ChEBI A. niger N402 occurrence repeats PMID:25062661 and is not independent publication evidence. Fusarium dimerum appears in a producer note, not an additional structured producer row. Exact-key assay frames are empty without refuting the curated iron target.

### Pathway ownership, actors and target-evidence scope

graph: supported. Targets: CHEBI:133861.

The complete returned view retains seven nodes/six edges, one SidD owner-producing step with proposed absent, one target and two histories. SidA hydroxylation, acyl supply and SidD assembly are attributed to PMID:25062661/5484314; the labelled SidD node remains ungrounded. Three N-hydroxy acyl groups are compatible with the hydroxamate class, but the ligand-only diagnostic does not measure Fe(III) affinity, coordination geometry or transport. Ferric coprogen B and metal-free desferricoprogen B are kept distinct in the target/transport interpretation.

### Citation attribution and complete retained history

evidence: supported. Targets: CHEBI:133861.

The seed and llm_assisted REVIEWED events preserve historical curation. Their primary-experiment labels and expanded pathway/target prose are not fresh experimental verification. The SidA/SidD causal and ferric-transport claims remain retained cited assertions; the repeated A. niger citation is not independent corroboration.

### Structure-compatible filing and model boundaries

consistency: supported. Targets: CHEBI:133861.

The amino-acid/peptide filing and 2,5-diketopiperazine description agree with the scaffold. Empty NPClassifier superclass/class arrays are missing model labels, not a demonstrated biological deficit. Structural interpretation, model classification and pathway verification remain separate.

### Earned scientific work and remaining authority

completeness: supported. Targets: CHEBI:133861.

Whole current owner/history, every assigned retained source frame, exact canonical intake and both complete saved-form tables were assessed. The entire returned maintained-reader view was read and equals capture. Full QC, complete OAK and fresh external primary-source/taxonomic verification remain unavailable or held. Curated assertions, local reader success and stored-form parsing do not replace those checks.

### Bounded positive local validation and normalized chemical representation

consistency: supported. Targets: CHEBI:133861.

The selected record is well-formed under the current closed schema and reproduces from maintained inputs. The two stored molecular encodings generate the declared Standard InChIKey and agree in parsed formula and net charge. These positive local results do not establish natural identity, exact graph equivalence, strain-specific production or primary-paper support.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| S288-2877-owner | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/desferricoprogen-b.yaml; complete current owner, all roots and complete history | supports | CHEBI:133861 and XRSRJBBRTCEBNS-CAGSISFISA-N join the exact ChEBI row and two digest-checked curated entries. The definition describes a diketopiperazine dimer esterified to a third hydroxyornithine-derived unit, consistent with the saved scaffold. This supports retained source identity rather than a newly identified natural sample. |
| S288-2877-source | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch288-reconciled-preflight/support-prep/current288-retained-source-extraction-001.json; /records/6/frames: all positive columns/physical raw spans and all exact-scope negative frames | partial | Curated rows 26–27 assert Neurospora crassa ATCC 10816 (5141), AXENIC_CULTURE/PMID:5484314, and Aspergillus niger N402 (5061), BGC_CHARACTERIZED/PMID:25062661, with SidA/SidD deletion in the latter note. There is no concrete BGC accession; the grade does not invent one. The ChEBI A. niger N402 occurrence repeats PMID:25062661 and is not independent publication evidence. Fusarium dimerum appears in a producer note, not an additional structured producer row. Exact-key assay frames are empty without refuting the curated iron target. |
| S288-2877-source-reading | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch288-reconciled-preflight/support-prep/current288-selected-source-reading-001.json; /records/6 | context_only | Complete personal retained-source reading; scientific interpretations here supersede the earlier lead-only status. |
| S288-2877-intake | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/inspect-2877-002/stdout; complete original canonical inspect stdout/input_files | supports | Actual successful current-base canonical inspection captured 74 exact input files for this owner. |
| S288-2877-intake-receipt | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/inspect-2877-002/receipt.json; command, exit_code, start/finish times, environment | supports | Original local canonical inspection exit 0; no replay by this author. |
| S288-2877-chemistry | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/chemistry-local/diagnostic-DATA-001.json; /records/6/{smiles,inchi}/computed; complete atoms,bonds,rings,potential_stereo,motifs, comparisons and atom_correspondence | partial | Both neutral C33H54N6O12 forms contain 51 atoms/51 bonds in one component, one six-member diketopiperazine ring and no metal. SMILES six carbonyls/five strict amides/one ester become four carbonyls/three strict amides plus two C(OH)=N sites at the secondary ring amides. Three N-hydroxy acyl groups, one primary amine and the ester remain; there is no free carboxylic acid. Three tetrahedral centres and three actual STEREOE side-chain bonds remain specified in both forms. Local potential-stereo Bond_Cis descriptors are not relabelled as Z. The true atom-centre stereo_complete flag does not independently establish natural absolute configuration. Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized Standard InChI/key, declared key, formula, charge and atom/bond counts agree. The saved chirality-aware atom map is empty and full_graph_identity_established is false. Motif-level interpretation does not establish full graph or natural-sample identity. |
| S288-2877-chemistry-receipt | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/diagnostic-original-001/receipt.json; original command, exit_code, timestamps and stderr | supports | Original twenty-stored-string diagnostic exit 0, no error or denied diagnostic event. |
| S288-2877-global-stderr | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/diagnostic-original-001/stderr; complete 454-byte global stderr | context_only | The original 454-byte stderr has one combined unusual-valence/metal-disconnection warning and eight undefined-stereochemistry warnings. These are globally unattributed and are not assigned to any owner or form. |
| S288-2877-curated-loader | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/src/naturalproductmech/curate/curated_compounds.py; complete exact ChEBI row-digest/key admission and curated producer loader | context_only | Maintained row admission supports source provenance, not fresh experimental verification. |
| S288-2877-seeder | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/scripts/seed_from_sources.py; curated_compounds source integration and retained curator-owned graph/pathway/target fields | context_only | Curated producer generation and carried mechanism fields have distinct provenance. |
| S288-2877-schema | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; PathwayStep, MolecularTarget, EvidenceItem and stereo_complete semantics | context_only | Owner pathway, target species and evidence classifications constrain interpretation. |
| S288-2877-stereo-policy | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/scripts/extract_mibig.py; structure_fields and FindMolChiralCenters(includeUnassigned=True) ? tags | context_only | Maintained stereo_complete checks atomic centres; it does not prove all bond geometry or natural stereochemistry. |
| S288-2877-table-1 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; physical lines 37596; selector exact_identifier_or_full_key | partial | 1 retained row placements/6 dictionary fields; full payload/span in extraction. BGC-metadata rows are contextual unless their exact compound key matches. |
| S288-2877-table-2 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; physical lines 14414; selector chebi_ids_from_exact_identifier_or_full_key | partial | 1 retained row placements/7 dictionary fields; full payload/span in extraction. BGC-metadata rows are contextual unless their exact compound key matches. |
| S288-2877-table-3 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2844; selector exact_full_key_or_curated_chebi_identifier | partial | 1 retained row placements/7 dictionary fields; full payload/span in extraction. BGC-metadata rows are contextual unless their exact compound key matches. |
| S288-2877-table-10 | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/curated_compounds.tsv; physical lines 26, 27; selector exact_full_key_or_curated_chebi_identifier | partial | 2 retained row placements/32 dictionary fields; full payload/span in extraction. BGC-metadata rows are contextual unless their exact compound key matches. |
| S288-2877-reader | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/maintained-readers-DATA-001.json; /records/6/complete_view and counts | partial | The complete returned view retains seven nodes/six edges, one SidD owner-producing step with proposed absent, one target and two histories. SidA hydroxylation, acyl supply and SidD assembly are attributed to PMID:25062661/5484314; the labelled SidD node remains ungrounded. Three N-hydroxy acyl groups are compatible with the hydroxamate class, but the ligand-only diagnostic does not measure Fe(III) affinity, coordination geometry or transport. Ferric coprogen B and metal-free desferricoprogen B are kept distinct in the target/transport interpretation. |
| S288-2877-reader-receipt | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/readers-original-001/receipt.json; nine original maintained-reader calls; complete owner equality | context_only | One import-time IPv6 socket capability probe was denied before action; no external request. Exact owner equality is retention evidence, not biological validation. |
| S288-2877-mechanism | /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/desferricoprogen-b.yaml; complete causal_graphs, biosynthetic_pathway, molecular_targets and citation lists; complete root scope when absent | partial | The complete returned view retains seven nodes/six edges, one SidD owner-producing step with proposed absent, one target and two histories. SidA hydroxylation, acyl supply and SidD assembly are attributed to PMID:25062661/5484314; the labelled SidD node remains ungrounded. Three N-hydroxy acyl groups are compatible with the hydroxamate class, but the ligand-only diagnostic does not measure Fe(III) affinity, coordination geometry or transport. Ferric coprogen B and metal-free desferricoprogen B are kept distinct in the target/transport interpretation. |
| EV288-intake | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/inspect-2877-002/stdout; Retained original execution output; exact SHA256 below. | supports | Captured this exact generated target and its regular-file source inputs at fresh main18ca; current input hashes remain unchanged. |
| EV288-strict_ten | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-strict-ten-001/stderr; Retained original execution output; exact SHA256 below. | supports | All ten selected whole owners passed closed validation; zero error rows. |
| EV288-strict_full | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-strict-full-001/stderr; Retained original execution output; exact SHA256 below. | supports | All3136 current owners passed full closed validation with component-inventory audit; zero error rows. |
| EV288-lockfile | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-lockfile-001/stdout; Retained original execution output; exact SHA256 below. | supports | All3136 owner paths agree with PATHS.tsv and filing pins, including component inventory checks. |
| EV288-reproduction | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-reproduction-001/stdout; Retained original execution output; exact SHA256 below. | supports | All3136 records are byte-identical to the current seeder output. Carried curator mechanism claims are preserved, not independently proven. |
| EV288-queue | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-queue-001/stdout; Retained original execution output; exact SHA256 below. | supports | The complete current review queue was generated locally:8919 rows across12 queues. Queue membership does not establish scientific review. |
| EV288-molecular | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/chemistry-local/diagnostic-DATA-001.json; Retained original execution output; exact SHA256 below. | supports | Exactly two stored encodings were parsed for this record (20 across the batch). Their normalized Standard InChI, key, computed formula and net charge agree; graph/canonical-SMILES equivalence and natural sample identity are not inferred. Record-specific differences remain in the scientific assessments. |
| EV288-reader | /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/maintained-readers-DATA-001.json; Retained original execution output; exact SHA256 below. | supports | The actual maintained reader returned this whole owner unchanged, including all declared graphs and histories. {"graphs": 1, "nodes": 7, "edges": 6, "pathway_steps": 1, "molecular_targets": 1, "history": 2, "component_refs": 0} Technical readability does not prove cited experiments. |

## Limits And Additional Notes

- Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized Standard InChI/key, declared key, formula, charge and atom/bond counts agree. The saved chirality-aware atom map is empty and full_graph_identity_established is false. Motif-level interpretation does not establish full graph or natural-sample identity.
- The seed and llm_assisted REVIEWED events preserve historical curation. Their primary-experiment labels and expanded pathway/target prose are not fresh experimental verification. The SidA/SidD causal and ferric-transport claims remain retained cited assertions; the repeated A. niger citation is not independent corroboration.
- The original 454-byte stderr has one combined unusual-valence/metal-disconnection warning and eight undefined-stereochemistry warnings. These are globally unattributed and are not assigned to any owner or form.
- Full QC, complete OAK and fresh external primary-source/taxonomic verification remain unavailable or held. Curated assertions, local reader success and stored-form parsing do not replace those checks.
- Full QC, complete OAK label checks and fresh external-source verification are unavailable. Completion remains partial despite successful local gates.
- The review source is a working-tree input attestation at the captured Git base. Saved validation does not promote native record status or close unrelated historical findings.
- Current source base is 18ca5dd6b9023670f10355084b45a8757a7a4e9e. No source, native state or saved review was edited by this author.
- Record-held PRIMARY_EXPERIMENT tags are attributed source classifications, not a claim that the underlying papers were freshly read.
- ROOT adds the original common intake/native/held-check templates; no duplicate common check IDs are introduced.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T105931Z-desferricoprogen-b
kind: record
repository: CultureBotAI/NaturalProductMech
title: Review desferricoprogen B against retained local evidence
started_at: '2026-11-07T10:47:12.603831Z'
finished_at: '2026-11-07T10:59:31.480359Z'
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
summary: Coherent retained desferricoprogen B scaffold and fungal source assertions,
  with two diketopiperazine amide/imidic changes and bounded ferric-complex claims.
  Scientific review is partial because full QC, complete OAK and fresh primary/external
  verification remain unavailable or held.
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
  - path: data/natural_products/alkaloids/pyochelin-i.yaml
    sha256: e9807db4f2cf2c81d7fa88b08e15ccbe33f1e45e5b8a52f4de182bdc83294706
    role: context
  - path: data/natural_products/amino_acids_and_peptides/albomycin-1.yaml
    sha256: dd035286f4410a027dfc85b57f9f988fa988e7f65900178ad9362fbbd9a5f819
    role: context
  - path: data/natural_products/amino_acids_and_peptides/albomycin-delta2.yaml
    sha256: 6fb56ccaab1682fa0e95be688a29d13818e6efae02a985d3697950889a316cce
    role: context
  - path: data/natural_products/amino_acids_and_peptides/albomycin-epsilon.yaml
    sha256: f229d9fc2ef02b3ea586aaa69b60a5e888189b89b463a1a81ff276e018591c68
    role: context
  - path: data/natural_products/amino_acids_and_peptides/desferricoprogen-b.yaml
    sha256: d55787d1f159f8aad71c6bcc5809bf37173f3ed1934b5ea2eabae9f6794139db
    role: target
  - path: data/natural_products/unclassified/desferrimycobactin-t.yaml
    sha256: 46e7810da0635d6e9b3ff392b5ef46ebb7dddbe89634d4835f7b757542809db7
    role: context
  - path: data/natural_products/unclassified/enterobactin.yaml
    sha256: b0f9e5adb294c3a7f26d2e12244297338177eb1665418e57d96e581237d5d0af
    role: context
  - path: data/natural_products/unclassified/mycobactin.yaml
    sha256: fc91d693e764769bdc2f937b8a8d0d809208334088f4e78a593101b7953e0c82
    role: context
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
  selection: 'Batch288, order2877: one of the first ten sorted currently unreviewed
    paths in the reconciled catalogue (1758 covered,1378 remaining before this batch).
    This bundle assesses only this target.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:133861
targets:
- target_id: CHEBI:133861
  path: data/natural_products/amino_acids_and_peptides/desferricoprogen-b.yaml
  label: desferricoprogen B
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/desferricoprogen-b.yaml
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
  - CHEBI:133861
  command: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/.venv/bin/python
    scripts/record_review.py inspect --targets /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/intakes-001/2877-targets-001.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/review-yaml-record/SKILL.md --input AGENTS.md --input conf/id_label_targets.yaml
    --input conf/np_roles.tsv --input conf/producer_evidence.tsv --input conf/record_review.yaml
    --input conf/sources.yaml --input curation/curated_compounds.tsv --input curation/lotus_occurrence_exclusions.tsv
    --input curation/mibig_claim_references.tsv --input curation/mibig_locus_evidence_overrides.tsv
    --input curation/mibig_producer_isolates.tsv --input curation/mibig_producer_strains.tsv
    --input curation/mibig_structure_corrections.tsv --input curation/mibig_xref_exclusions.tsv
    --input curation/pubchem_bioassay_exclusions.tsv --input curation/unresolved_taxa.tsv
    --input data/natural_products/PATHS.tsv --input data/natural_products/alkaloids/pyochelin-i.yaml
    --input data/natural_products/amino_acids_and_peptides/albomycin-1.yaml --input
    data/natural_products/amino_acids_and_peptides/albomycin-delta2.yaml --input data/natural_products/amino_acids_and_peptides/albomycin-epsilon.yaml
    --input data/natural_products/unclassified/desferrimycobactin-t.yaml --input data/natural_products/unclassified/enterobactin.yaml
    --input data/natural_products/unclassified/mycobactin.yaml --input data/raw/MANIFEST.yaml
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
  - EV288-intake
- check_id: CK288-strict_ten
  name: 'Maintained local gate: strict_ten'
  status: passed
  required: true
  summary: All ten selected whole owners passed closed validation; zero error rows.
  target_ids:
  - CHEBI:133861
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
  - CHEBI:133861
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
  - CHEBI:133861
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
  - CHEBI:133861
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
  - CHEBI:133861
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
  - CHEBI:133861
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
    all declared graphs and histories. {"graphs": 1, "nodes": 7, "edges": 6, "pathway_steps":
    1, "molecular_targets": 1, "history": 2, "component_refs": 0} Technical readability
    does not prove cited experiments.'
  target_ids:
  - CHEBI:133861
  command: /usr/bin/sandbox-exec -p '(version 1)(allow default)(deny network*)' /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/.venv/bin/python
    -I -S -B /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/read-and-diagnose-local-002.py
    readers
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV288-reader
- check_id: CK288-full-qc
  name: Full repository QC
  status: unavailable
  required: true
  summary: 'Not run: maintained full QC reaches the vendored-sync fetch. The five
    local gates do not substitute for full QC.'
  target_ids:
  - CHEBI:133861
- check_id: CK288-ontology
  name: Complete OAK identifier-label correspondence
  status: unavailable
  required: true
  summary: 'Not run: a complete pinned offline CHEBI/GO adapter boundary was not established.
    No ontology download or remote resolver was permitted.'
  target_ids:
  - CHEBI:133861
- check_id: CK288-fresh-authorities
  name: Fresh source, literature, taxonomy and structured database verification
  status: unavailable
  required: true
  summary: Not run under the source-request hold. Database assertions, gene/pathway
    annotations, citations, exact forms and strain claims are assessed only against
    retained local evidence; no fresh resolution or primary-paper authentication is
    claimed.
  target_ids:
  - CHEBI:133861
evidence:
- evidence_id: S288-2877-owner
  kind: record_content
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/desferricoprogen-b.yaml
  locator: complete current owner, all roots and complete history
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: supports
  summary: CHEBI:133861 and XRSRJBBRTCEBNS-CAGSISFISA-N join the exact ChEBI row and
    two digest-checked curated entries. The definition describes a diketopiperazine
    dimer esterified to a third hydroxyornithine-derived unit, consistent with the
    saved scaffold. This supports retained source identity rather than a newly identified
    natural sample.
  snapshot_sha256: d55787d1f159f8aad71c6bcc5809bf37173f3ed1934b5ea2eabae9f6794139db
- evidence_id: S288-2877-source
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch288-reconciled-preflight/support-prep/current288-retained-source-extraction-001.json
  locator: '/records/6/frames: all positive columns/physical raw spans and all exact-scope
    negative frames'
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: partial
  summary: Curated rows 26–27 assert Neurospora crassa ATCC 10816 (5141), AXENIC_CULTURE/PMID:5484314,
    and Aspergillus niger N402 (5061), BGC_CHARACTERIZED/PMID:25062661, with SidA/SidD
    deletion in the latter note. There is no concrete BGC accession; the grade does
    not invent one. The ChEBI A. niger N402 occurrence repeats PMID:25062661 and is
    not independent publication evidence. Fusarium dimerum appears in a producer note,
    not an additional structured producer row. Exact-key assay frames are empty without
    refuting the curated iron target.
  snapshot_sha256: 9964292610e52e0175cf4a68aa9d8c556eef5380fe9c8fd5ca523094b8a00910
- evidence_id: S288-2877-source-reading
  kind: authority
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/next-batch288-reconciled-preflight/support-prep/current288-selected-source-reading-001.json
  locator: /records/6
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: context_only
  summary: Complete personal retained-source reading; scientific interpretations here
    supersede the earlier lead-only status.
  snapshot_sha256: 2f26309cc606ffd46b7146726810a32d36b369c3de8af699b3e01d018a5dcd88
- evidence_id: S288-2877-intake
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/inspect-2877-002/stdout
  locator: complete original canonical inspect stdout/input_files
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: supports
  summary: Actual successful current-base canonical inspection captured 74 exact input
    files for this owner.
  snapshot_sha256: 10087e006a3eda011a9c460db425c56f9d50df82b7fe67b4b73557bdb0462467
- evidence_id: S288-2877-intake-receipt
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/inspect-2877-002/receipt.json
  locator: command, exit_code, start/finish times, environment
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: supports
  summary: Original local canonical inspection exit 0; no replay by this author.
  snapshot_sha256: 36a0c3588a848baf565978875eae3b00a7ab9c2e7f459e84936f6e00a9a79308
- evidence_id: S288-2877-chemistry
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/{smiles,inchi}/computed; complete atoms,bonds,rings,potential_stereo,motifs,
    comparisons and atom_correspondence
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: partial
  summary: Both neutral C33H54N6O12 forms contain 51 atoms/51 bonds in one component,
    one six-member diketopiperazine ring and no metal. SMILES six carbonyls/five strict
    amides/one ester become four carbonyls/three strict amides plus two C(OH)=N sites
    at the secondary ring amides. Three N-hydroxy acyl groups, one primary amine and
    the ester remain; there is no free carboxylic acid. Three tetrahedral centres
    and three actual STEREOE side-chain bonds remain specified in both forms. Local
    potential-stereo Bond_Cis descriptors are not relabelled as Z. The true atom-centre
    stereo_complete flag does not independently establish natural absolute configuration.
    Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized
    Standard InChI/key, declared key, formula, charge and atom/bond counts agree.
    The saved chirality-aware atom map is empty and full_graph_identity_established
    is false. Motif-level interpretation does not establish full graph or natural-sample
    identity.
  snapshot_sha256: 0c6f6295b3f1d3c0755d8d902df0f9a375b3f23a1878346ad94584b492b8021c
- evidence_id: S288-2877-chemistry-receipt
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/diagnostic-original-001/receipt.json
  locator: original command, exit_code, timestamps and stderr
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: supports
  summary: Original twenty-stored-string diagnostic exit 0, no error or denied diagnostic
    event.
  snapshot_sha256: 7c3c7db5d6195ae8d2662002e041fb767a311713f1cc60535cfe3ed2618c031a
- evidence_id: S288-2877-global-stderr
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/diagnostic-original-001/stderr
  locator: complete 454-byte global stderr
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: context_only
  summary: The original 454-byte stderr has one combined unusual-valence/metal-disconnection
    warning and eight undefined-stereochemistry warnings. These are globally unattributed
    and are not assigned to any owner or form.
  snapshot_sha256: eeecdff321e0db585ddaadc0e94efe6d9c7e1db3d5e20e5475d874c93e3f114b
- evidence_id: S288-2877-curated-loader
  kind: authority
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/src/naturalproductmech/curate/curated_compounds.py
  locator: complete exact ChEBI row-digest/key admission and curated producer loader
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: context_only
  summary: Maintained row admission supports source provenance, not fresh experimental
    verification.
  snapshot_sha256: fdafad9ed1d94c78c996083632c75f3bafc1620a31da5aa7b9a37e558a187915
- evidence_id: S288-2877-seeder
  kind: authority
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: curated_compounds source integration and retained curator-owned graph/pathway/target
    fields
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: context_only
  summary: Curated producer generation and carried mechanism fields have distinct
    provenance.
  snapshot_sha256: d6650a80685b7f778050f79cc72de1fc3bbf281c57336401a5c773755de56324
- evidence_id: S288-2877-schema
  kind: authority
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: PathwayStep, MolecularTarget, EvidenceItem and stereo_complete semantics
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: context_only
  summary: Owner pathway, target species and evidence classifications constrain interpretation.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: S288-2877-stereo-policy
  kind: authority
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: structure_fields and FindMolChiralCenters(includeUnassigned=True) ? tags
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: context_only
  summary: Maintained stereo_complete checks atomic centres; it does not prove all
    bond geometry or natural stereochemistry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: S288-2877-table-1
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: physical lines 37596; selector exact_identifier_or_full_key
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: partial
  summary: 1 retained row placements/6 dictionary fields; full payload/span in extraction.
    BGC-metadata rows are contextual unless their exact compound key matches.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: S288-2877-table-2
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: physical lines 14414; selector chebi_ids_from_exact_identifier_or_full_key
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: partial
  summary: 1 retained row placements/7 dictionary fields; full payload/span in extraction.
    BGC-metadata rows are contextual unless their exact compound key matches.
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: S288-2877-table-3
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2844; selector exact_full_key_or_curated_chebi_identifier
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: partial
  summary: 1 retained row placements/7 dictionary fields; full payload/span in extraction.
    BGC-metadata rows are contextual unless their exact compound key matches.
  snapshot_sha256: f62f89df12bd373e0663a7e11e56e46733ca174f8495ec116ec57679c2279f35
- evidence_id: S288-2877-table-10
  kind: database
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/curation/curated_compounds.tsv
  locator: physical lines 26, 27; selector exact_full_key_or_curated_chebi_identifier
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: partial
  summary: 2 retained row placements/32 dictionary fields; full payload/span in extraction.
    BGC-metadata rows are contextual unless their exact compound key matches.
  snapshot_sha256: 371b3a8b453dc9706e6a8f7f615bf6604809b1c42f4a38b7e9e921ffcbbad064
- evidence_id: S288-2877-reader
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/maintained-readers-DATA-001.json
  locator: /records/6/complete_view and counts
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: partial
  summary: The complete returned view retains seven nodes/six edges, one SidD owner-producing
    step with proposed absent, one target and two histories. SidA hydroxylation, acyl
    supply and SidD assembly are attributed to PMID:25062661/5484314; the labelled
    SidD node remains ungrounded. Three N-hydroxy acyl groups are compatible with
    the hydroxamate class, but the ligand-only diagnostic does not measure Fe(III)
    affinity, coordination geometry or transport. Ferric coprogen B and metal-free
    desferricoprogen B are kept distinct in the target/transport interpretation.
  snapshot_sha256: 68398e58af6b7cc02b67978b7c92a04f2e9321941a9d230735eb808d12b8bf54
- evidence_id: S288-2877-reader-receipt
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/readers-original-001/receipt.json
  locator: nine original maintained-reader calls; complete owner equality
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: context_only
  summary: One import-time IPv6 socket capability probe was denied before action;
    no external request. Exact owner equality is retention evidence, not biological
    validation.
  snapshot_sha256: dc25e6693f4833444a2fd025fd13d20d4155857aa97e0bfffcc104d6f0d1a1db
- evidence_id: S288-2877-mechanism
  kind: record_content
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/desferricoprogen-b.yaml
  locator: complete causal_graphs, biosynthetic_pathway, molecular_targets and citation
    lists; complete root scope when absent
  accessed_at: '2026-11-07T10:58:29.699485Z'
  support: partial
  summary: The complete returned view retains seven nodes/six edges, one SidD owner-producing
    step with proposed absent, one target and two histories. SidA hydroxylation, acyl
    supply and SidD assembly are attributed to PMID:25062661/5484314; the labelled
    SidD node remains ungrounded. Three N-hydroxy acyl groups are compatible with
    the hydroxamate class, but the ligand-only diagnostic does not measure Fe(III)
    affinity, coordination geometry or transport. Ferric coprogen B and metal-free
    desferricoprogen B are kept distinct in the target/transport interpretation.
  snapshot_sha256: d55787d1f159f8aad71c6bcc5809bf37173f3ed1934b5ea2eabae9f6794139db
- evidence_id: EV288-intake
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/inspect-2877-002/stdout
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:47:13.764916Z'
  support: supports
  summary: Captured this exact generated target and its regular-file source inputs
    at fresh main18ca; current input hashes remain unchanged.
  snapshot_sha256: 10087e006a3eda011a9c460db425c56f9d50df82b7fe67b4b73557bdb0462467
- evidence_id: EV288-strict_ten
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-strict-ten-001/stderr
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:46:17.912716Z'
  support: supports
  summary: All ten selected whole owners passed closed validation; zero error rows.
  snapshot_sha256: f27cc4305f99346ce232c497e20eed0e0b6a60ecb60c79c18e2c1ec3a97ba614
- evidence_id: EV288-strict_full
  kind: validation
  reference: /Users/marcin/agent-work/NaturalProductMech/npm-review-work/shared-next-batch288/local-executions/native-strict-full-001/stderr
  locator: Retained original execution output; exact SHA256 below.
  accessed_at: '2026-11-07T10:46:38.119885Z'
  support: supports
  summary: All3136 current owners passed full closed validation with component-inventory
    audit; zero error rows.
  snapshot_sha256: 210749c3fb55154cd48a727fe43622e1db2ef79bddabb38b299f55ff887e4f0f
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
    all declared graphs and histories. {"graphs": 1, "nodes": 7, "edges": 6, "pathway_steps":
    1, "molecular_targets": 1, "history": 2, "component_refs": 0} Technical readability
    does not prove cited experiments.'
  snapshot_sha256: 68398e58af6b7cc02b67978b7c92a04f2e9321941a9d230735eb808d12b8bf54
assessments:
- assessment_id: S288-2877-identity
  area: identity
  topic: Exact source identity and congener boundary
  summary: CHEBI:133861 and XRSRJBBRTCEBNS-CAGSISFISA-N join the exact ChEBI row and
    two digest-checked curated entries. The definition describes a diketopiperazine
    dimer esterified to a third hydroxyornithine-derived unit, consistent with the
    saved scaffold. This supports retained source identity rather than a newly identified
    natural sample.
  outcome: supported
  target_ids:
  - CHEBI:133861
  evidence_ids:
  - S288-2877-owner
  - S288-2877-source
  - S288-2877-source-reading
  - S288-2877-intake
  - S288-2877-intake-receipt
  - S288-2877-curated-loader
  - S288-2877-seeder
  - S288-2877-table-1
  - S288-2877-table-2
  - S288-2877-table-3
  - S288-2877-table-10
  dimensions:
  - name: full_key
    definition: Complete retained compound key.
    value: XRSRJBBRTCEBNS-CAGSISFISA-N
    evidence_ids:
    - S288-2877-owner
    - S288-2877-source
    - S288-2877-source-reading
    - S288-2877-intake
    - S288-2877-intake-receipt
    - S288-2877-curated-loader
    - S288-2877-seeder
    - S288-2877-table-1
    - S288-2877-table-2
    - S288-2877-table-3
    - S288-2877-table-10
  - name: identity_scope
    definition: Source identity versus independent natural identity.
    value: CHEBI:133861 and XRSRJBBRTCEBNS-CAGSISFISA-N join the exact ChEBI row and
      two digest-checked curated entries. The definition describes a diketopiperazine
      dimer esterified to a third hydroxyornithine-derived unit, consistent with the
      saved scaffold. This supports retained source identity rather than a newly identified
      natural sample.
    evidence_ids:
    - S288-2877-owner
    - S288-2877-source
    - S288-2877-source-reading
    - S288-2877-intake
    - S288-2877-intake-receipt
    - S288-2877-curated-loader
    - S288-2877-seeder
    - S288-2877-table-1
    - S288-2877-table-2
    - S288-2877-table-3
    - S288-2877-table-10
- assessment_id: S288-2877-representation
  area: representation
  topic: Complete saved-form chemical interpretation
  summary: Both neutral C33H54N6O12 forms contain 51 atoms/51 bonds in one component,
    one six-member diketopiperazine ring and no metal. SMILES six carbonyls/five strict
    amides/one ester become four carbonyls/three strict amides plus two C(OH)=N sites
    at the secondary ring amides. Three N-hydroxy acyl groups, one primary amine and
    the ester remain; there is no free carboxylic acid. Three tetrahedral centres
    and three actual STEREOE side-chain bonds remain specified in both forms. Local
    potential-stereo Bond_Cis descriptors are not relabelled as Z. The true atom-centre
    stereo_complete flag does not independently establish natural absolute configuration.
    Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized
    Standard InChI/key, declared key, formula, charge and atom/bond counts agree.
    The saved chirality-aware atom map is empty and full_graph_identity_established
    is false. Motif-level interpretation does not establish full graph or natural-sample
    identity.
  outcome: supported
  target_ids:
  - CHEBI:133861
  evidence_ids:
  - S288-2877-owner
  - S288-2877-chemistry
  - S288-2877-chemistry-receipt
  - S288-2877-global-stderr
  - S288-2877-stereo-policy
  - S288-2877-intake
  dimensions:
  - name: saved_topology
    definition: Interpretation of the complete saved atom/bond/ring/stereo/motif tables.
    value: Both neutral C33H54N6O12 forms contain 51 atoms/51 bonds in one component,
      one six-member diketopiperazine ring and no metal. SMILES six carbonyls/five
      strict amides/one ester become four carbonyls/three strict amides plus two C(OH)=N
      sites at the secondary ring amides. Three N-hydroxy acyl groups, one primary
      amine and the ester remain; there is no free carboxylic acid. Three tetrahedral
      centres and three actual STEREOE side-chain bonds remain specified in both forms.
      Local potential-stereo Bond_Cis descriptors are not relabelled as Z. The true
      atom-centre stereo_complete flag does not independently establish natural absolute
      configuration.
    evidence_ids:
    - S288-2877-owner
    - S288-2877-chemistry
    - S288-2877-chemistry-receipt
    - S288-2877-global-stderr
    - S288-2877-stereo-policy
    - S288-2877-intake
  - name: comparison_limit
    definition: Exact limited comparison result.
    value: Both canonical isomeric and nonisomeric SMILES comparisons are false while
      normalized Standard InChI/key, declared key, formula, charge and atom/bond counts
      agree. The saved chirality-aware atom map is empty and full_graph_identity_established
      is false. Motif-level interpretation does not establish full graph or natural-sample
      identity.
    evidence_ids:
    - S288-2877-owner
    - S288-2877-chemistry
    - S288-2877-chemistry-receipt
    - S288-2877-global-stderr
    - S288-2877-stereo-policy
    - S288-2877-intake
- assessment_id: S288-2877-provenance
  area: provenance
  topic: Producer, locus, occurrence and source grain
  summary: Curated rows 26–27 assert Neurospora crassa ATCC 10816 (5141), AXENIC_CULTURE/PMID:5484314,
    and Aspergillus niger N402 (5061), BGC_CHARACTERIZED/PMID:25062661, with SidA/SidD
    deletion in the latter note. There is no concrete BGC accession; the grade does
    not invent one. The ChEBI A. niger N402 occurrence repeats PMID:25062661 and is
    not independent publication evidence. Fusarium dimerum appears in a producer note,
    not an additional structured producer row. Exact-key assay frames are empty without
    refuting the curated iron target.
  outcome: supported
  target_ids:
  - CHEBI:133861
  evidence_ids:
  - S288-2877-owner
  - S288-2877-source
  - S288-2877-source-reading
  - S288-2877-intake
  - S288-2877-intake-receipt
  - S288-2877-curated-loader
  - S288-2877-seeder
  - S288-2877-table-1
  - S288-2877-table-2
  - S288-2877-table-3
  - S288-2877-table-10
  dimensions:
  - name: claim_grain
    definition: Causal grades, occurrence and source/compound specificity.
    value: Curated rows 26–27 assert Neurospora crassa ATCC 10816 (5141), AXENIC_CULTURE/PMID:5484314,
      and Aspergillus niger N402 (5061), BGC_CHARACTERIZED/PMID:25062661, with SidA/SidD
      deletion in the latter note. There is no concrete BGC accession; the grade does
      not invent one. The ChEBI A. niger N402 occurrence repeats PMID:25062661 and
      is not independent publication evidence. Fusarium dimerum appears in a producer
      note, not an additional structured producer row. Exact-key assay frames are
      empty without refuting the curated iron target.
    evidence_ids:
    - S288-2877-owner
    - S288-2877-source
    - S288-2877-source-reading
    - S288-2877-intake
    - S288-2877-intake-receipt
    - S288-2877-curated-loader
    - S288-2877-seeder
    - S288-2877-table-1
    - S288-2877-table-2
    - S288-2877-table-3
    - S288-2877-table-10
- assessment_id: S288-2877-mechanism
  area: graph
  topic: Pathway ownership, actors and target-evidence scope
  summary: The complete returned view retains seven nodes/six edges, one SidD owner-producing
    step with proposed absent, one target and two histories. SidA hydroxylation, acyl
    supply and SidD assembly are attributed to PMID:25062661/5484314; the labelled
    SidD node remains ungrounded. Three N-hydroxy acyl groups are compatible with
    the hydroxamate class, but the ligand-only diagnostic does not measure Fe(III)
    affinity, coordination geometry or transport. Ferric coprogen B and metal-free
    desferricoprogen B are kept distinct in the target/transport interpretation.
  outcome: supported
  target_ids:
  - CHEBI:133861
  evidence_ids:
  - S288-2877-owner
  - S288-2877-mechanism
  - S288-2877-schema
  - S288-2877-source
  - S288-2877-curated-loader
  - S288-2877-seeder
  - S288-2877-reader
  - S288-2877-reader-receipt
  dimensions:
  - name: mechanistic_scope
    definition: Whole returned owner and claim-specific biological limits.
    value: The complete returned view retains seven nodes/six edges, one SidD owner-producing
      step with proposed absent, one target and two histories. SidA hydroxylation,
      acyl supply and SidD assembly are attributed to PMID:25062661/5484314; the labelled
      SidD node remains ungrounded. Three N-hydroxy acyl groups are compatible with
      the hydroxamate class, but the ligand-only diagnostic does not measure Fe(III)
      affinity, coordination geometry or transport. Ferric coprogen B and metal-free
      desferricoprogen B are kept distinct in the target/transport interpretation.
    evidence_ids:
    - S288-2877-owner
    - S288-2877-mechanism
    - S288-2877-schema
    - S288-2877-source
    - S288-2877-curated-loader
    - S288-2877-seeder
    - S288-2877-reader
    - S288-2877-reader-receipt
- assessment_id: S288-2877-evidence
  area: evidence
  topic: Citation attribution and complete retained history
  summary: The seed and llm_assisted REVIEWED events preserve historical curation.
    Their primary-experiment labels and expanded pathway/target prose are not fresh
    experimental verification. The SidA/SidD causal and ferric-transport claims remain
    retained cited assertions; the repeated A. niger citation is not independent corroboration.
  outcome: supported
  target_ids:
  - CHEBI:133861
  evidence_ids:
  - S288-2877-owner
  - S288-2877-source
  - S288-2877-source-reading
  - S288-2877-intake
  - S288-2877-intake-receipt
  - S288-2877-curated-loader
  - S288-2877-seeder
  - S288-2877-table-1
  - S288-2877-table-2
  - S288-2877-table-3
  - S288-2877-table-10
  - S288-2877-mechanism
  - S288-2877-schema
  - S288-2877-reader
  - S288-2877-reader-receipt
  dimensions:
  - name: history_and_evidence
    definition: Historical curation and primary-citation limits.
    value: The seed and llm_assisted REVIEWED events preserve historical curation.
      Their primary-experiment labels and expanded pathway/target prose are not fresh
      experimental verification. The SidA/SidD causal and ferric-transport claims
      remain retained cited assertions; the repeated A. niger citation is not independent
      corroboration.
    evidence_ids:
    - S288-2877-owner
    - S288-2877-source
    - S288-2877-source-reading
    - S288-2877-intake
    - S288-2877-intake-receipt
    - S288-2877-curated-loader
    - S288-2877-seeder
    - S288-2877-table-1
    - S288-2877-table-2
    - S288-2877-table-3
    - S288-2877-table-10
    - S288-2877-mechanism
    - S288-2877-schema
    - S288-2877-reader
    - S288-2877-reader-receipt
- assessment_id: S288-2877-classification
  area: consistency
  topic: Structure-compatible filing and model boundaries
  summary: The amino-acid/peptide filing and 2,5-diketopiperazine description agree
    with the scaffold. Empty NPClassifier superclass/class arrays are missing model
    labels, not a demonstrated biological deficit. Structural interpretation, model
    classification and pathway verification remain separate.
  outcome: supported
  target_ids:
  - CHEBI:133861
  evidence_ids:
  - S288-2877-owner
  - S288-2877-source
  - S288-2877-source-reading
  - S288-2877-intake
  - S288-2877-intake-receipt
  - S288-2877-curated-loader
  - S288-2877-seeder
  - S288-2877-table-1
  - S288-2877-table-2
  - S288-2877-table-3
  - S288-2877-table-10
  - S288-2877-chemistry
  - S288-2877-schema
  dimensions:
  - name: classification_scope
    definition: Model/source classes versus structural or experimental interpretation.
    value: The amino-acid/peptide filing and 2,5-diketopiperazine description agree
      with the scaffold. Empty NPClassifier superclass/class arrays are missing model
      labels, not a demonstrated biological deficit. Structural interpretation, model
      classification and pathway verification remain separate.
    evidence_ids:
    - S288-2877-owner
    - S288-2877-source
    - S288-2877-source-reading
    - S288-2877-intake
    - S288-2877-intake-receipt
    - S288-2877-curated-loader
    - S288-2877-seeder
    - S288-2877-table-1
    - S288-2877-table-2
    - S288-2877-table-3
    - S288-2877-table-10
    - S288-2877-chemistry
    - S288-2877-schema
- assessment_id: S288-2877-completeness
  area: completeness
  topic: Earned scientific work and remaining authority
  summary: Whole current owner/history, every assigned retained source frame, exact
    canonical intake and both complete saved-form tables were assessed. The entire
    returned maintained-reader view was read and equals capture. Full QC, complete
    OAK and fresh external primary-source/taxonomic verification remain unavailable
    or held. Curated assertions, local reader success and stored-form parsing do not
    replace those checks.
  outcome: supported
  target_ids:
  - CHEBI:133861
  evidence_ids:
  - S288-2877-owner
  - S288-2877-source
  - S288-2877-source-reading
  - S288-2877-intake
  - S288-2877-intake-receipt
  - S288-2877-curated-loader
  - S288-2877-seeder
  - S288-2877-table-1
  - S288-2877-table-2
  - S288-2877-table-3
  - S288-2877-table-10
  - S288-2877-chemistry
  - S288-2877-chemistry-receipt
  - S288-2877-global-stderr
  - S288-2877-stereo-policy
  - S288-2877-mechanism
  - S288-2877-schema
  - S288-2877-reader
  - S288-2877-reader-receipt
  dimensions:
  - name: earned_scope
    definition: Substantive local work completed.
    value: Whole current owner/history, every assigned retained source frame, exact
      canonical intake and both complete saved-form tables were assessed. The entire
      returned maintained-reader view was read and equals capture. Full QC, complete
      OAK and fresh external primary-source/taxonomic verification remain unavailable
      or held. Curated assertions, local reader success and stored-form parsing do
      not replace those checks.
    evidence_ids:
    - S288-2877-owner
    - S288-2877-source
    - S288-2877-source-reading
    - S288-2877-intake
    - S288-2877-intake-receipt
    - S288-2877-curated-loader
    - S288-2877-seeder
    - S288-2877-table-1
    - S288-2877-table-2
    - S288-2877-table-3
    - S288-2877-table-10
    - S288-2877-chemistry
    - S288-2877-chemistry-receipt
    - S288-2877-global-stderr
    - S288-2877-stereo-policy
    - S288-2877-mechanism
    - S288-2877-schema
    - S288-2877-reader
    - S288-2877-reader-receipt
  - name: remaining_limits
    definition: Checks and authority not established by local computation.
    value: Full QC, complete OAK and fresh external primary-source/taxonomic verification
      remain unavailable or held. Curated assertions, local reader success and stored-form
      parsing do not replace those checks.
    evidence_ids:
    - S288-2877-owner
    - S288-2877-source
    - S288-2877-source-reading
    - S288-2877-intake
    - S288-2877-intake-receipt
    - S288-2877-curated-loader
    - S288-2877-seeder
    - S288-2877-table-1
    - S288-2877-table-2
    - S288-2877-table-3
    - S288-2877-table-10
    - S288-2877-chemistry
    - S288-2877-chemistry-receipt
    - S288-2877-global-stderr
    - S288-2877-stereo-policy
    - S288-2877-mechanism
    - S288-2877-schema
    - S288-2877-reader
    - S288-2877-reader-receipt
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
  - CHEBI:133861
  evidence_ids:
  - EV288-strict_ten
  - EV288-reproduction
  - EV288-molecular
findings: []
actions: []
limitations:
- Both canonical isomeric and nonisomeric SMILES comparisons are false while normalized
  Standard InChI/key, declared key, formula, charge and atom/bond counts agree. The
  saved chirality-aware atom map is empty and full_graph_identity_established is false.
  Motif-level interpretation does not establish full graph or natural-sample identity.
- The seed and llm_assisted REVIEWED events preserve historical curation. Their primary-experiment
  labels and expanded pathway/target prose are not fresh experimental verification.
  The SidA/SidD causal and ferric-transport claims remain retained cited assertions;
  the repeated A. niger citation is not independent corroboration.
- The original 454-byte stderr has one combined unusual-valence/metal-disconnection
  warning and eight undefined-stereochemistry warnings. These are globally unattributed
  and are not assigned to any owner or form.
- Full QC, complete OAK and fresh external primary-source/taxonomic verification remain
  unavailable or held. Curated assertions, local reader success and stored-form parsing
  do not replace those checks.
- Full QC, complete OAK label checks and fresh external-source verification are unavailable.
  Completion remains partial despite successful local gates.
- The review source is a working-tree input attestation at the captured Git base.
  Saved validation does not promote native record status or close unrelated historical
  findings.
notes:
- Current source base is 18ca5dd6b9023670f10355084b45a8757a7a4e9e. No source, native
  state or saved review was edited by this author.
- Record-held PRIMARY_EXPERIMENT tags are attributed source classifications, not a
  claim that the underlying papers were freshly read.
- ROOT adds the original common intake/native/held-check templates; no duplicate common
  check IDs are introduced.
tags:
- batch-288
- local-evidence
- partial-review
```
