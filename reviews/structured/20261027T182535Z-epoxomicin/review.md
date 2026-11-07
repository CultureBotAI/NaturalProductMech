# Scientific review of epoxomicin

- Review: 20261027T182535Z-epoxomicin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-27T18:24:14.870823Z
- Finished UTC: 2026-10-27T18:25:35.108399Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Epoxomicin has internally consistent encodings, abstract-supported heterologous biosynthesis and directly checked yeast beta5 covalent-binding context. Four NSD2-associated enzyme-inhibitor annotations exceed the cell-viability assay evidence; a narrow maintained-source correction is proposed without changing imported observations or the proteasome graph.

## Scope And Provenance

Review epoxomicin's retained identity, biosynthesis abstract, selected yeast beta5 mmCIF/UniProt mapping, and the exact descriptions of NSD2-associated AIDs 1645876/1645877. Adjudicate the four imported ENZYME_INHIBITOR classifications against their 72-hour cell-viability endpoint and the maintained classifier logic, preserving the 18 unrelated activity rows and the proteasome graph.

Selection: One owner selected in canonical unreviewed path order as campaign review 695; whole retained owner and local source rows read, with bounded scientific interpretation.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:42265 | data/natural_products/amino_acids_and_peptides/epoxomicin.yaml | generated | epoxomicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | CHEBI:42265 | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | CHEBI:42265 | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | CHEBI:42265 | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:42265 | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | CHEBI:42265 | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | CHEBI:42265 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Retained owner/source consistency | passed | True | CHEBI:42265 | Whole retained source rows match original table indices and hashes; retained inventory arrays and the separate official-intake projections remain distinct. |
| Saved two-encoding consistency | passed | True | CHEBI:42265 | Saved RDKit 2026.03.5 results reproduce the declared full key DOGIDQKFVLKMLQ-JTHVHQAWSA-N and formula C28H50N4O7 from both encodings, with one fragment and formal charge zero. No unspecified tetrahedral carbon sites were reported. Internal consistency does not verify natural identity or all stereochemical assignments. |
| Own assay identity and mode | passed | True | CHEBI:42265 | Both exact AID identities, whole protocol/result-definition equality and cell-viability scope were checked. No fresh compound-result rows were retrieved. |
| Assay-specific class support | failed | True | CHEBI:42265 | The four retained NSD2-associated ENZYME_INHIBITOR labels are not supported by these cell-viability assays as direct enzymatic-inhibition evidence. This is a scientific support check, not a validator execution. |
| Yeast protein and deposition mapping | passed | True | CHEBI:42265 | Selected entity, sequence, covalent-link and reciprocal accession fields agree with the stored two-node binding graph. All-coordinate validation and the complete article were not performed. |
| Exact natural identity and chemical authority | unavailable | True | CHEBI:42265 | No fresh compound authority or complete primary structural assignment was inspected. Saved encoding consistency is a bounded positive result. |

## Scientific And Domain Assessments

### Internal chemical encoding

representation: supported. Targets: CHEBI:42265.

Saved RDKit 2026.03.5 results reproduce the declared full key DOGIDQKFVLKMLQ-JTHVHQAWSA-N and formula C28H50N4O7 from both encodings, with one fragment and formal charge zero. No unspecified tetrahedral carbon sites were reported. Internal consistency does not verify natural identity or all stereochemical assignments.

### Natural stereochemical scope

identity: unknown. Targets: CHEBI:42265.

The 3 parsed-InChI unspecified double-bond observations are imidic C(-O)=N environments, not missing alkene configurations. No experimental reassignment or natural-identity conclusion follows from the local encoding check.

### Donor strain versus production host

provenance: unknown. Targets: CHEBI:42265.

The abstract supports ATCC 53904 as the epoxomicin cluster donor and S. albus J1046 as the heterologous host. The retained Goodfellowiella coeruleoviolacea NCBITaxon:334858 label is not independently resolved by the abstract and is not treated as a demonstrated conflict.

### Biosynthetic locus scope

provenance: supported. Targets: CHEBI:42265.

Whole-pathway heterologous production supports the broad retained CLUSTER_DEMONSTRATED scope of BGC0000346 version 5/KF647219.1. Exact boundaries, constructs and individual functions remain unverified; putative derivatives are not substituted for epoxomicin.

### Cell viability versus enzyme inhibition

evidence: concern. Targets: CHEBI:42265.

Owner bioactivities[6–9] are four source projections of two viability assays, including blank-target and O96028 target-dimension rows. Generic inhibition wording does not establish direct NSD2 inhibition. Preserve their ACTIVE calls, values 0.0073/0.0129 uM, source Potency endpoint and OTHER measurement type while correcting the unsupported activity-class inference.

### Epoxomicin binding to yeast beta5

graph: supported. Targets: CHEBI:42265.

The retained two-node/one-edge graph is supported within the saved deposition scope: chains 3/4 form covalent adducts with mature Thr1 of PRE2 K/Y, reciprocally mapped to UniProt P30656 Thr76. This organism-specific binding evidence neither supplies an NSD2 mechanism nor verifies all claims in the crystal article.

### Imported observations and aggregate support

quantity: unknown. Targets: CHEBI:42265.

All 22 owner annotations and 23 retained PubChem rows remain distinct source records; the empty CID 9915668 row is not an assay. No automatic deduplication, changed potency, direct NSD2 IC50 or new classification is assigned. The proteasome evidence does not rescue the four assay-specific class labels; it also prevents interpreting their defect as proof that epoxomicin lacks enzyme-inhibitor activity generally.

### Bounded scientific coverage

completeness: unknown. Targets: CHEBI:42265.

Original local reading, saved computation and each external source inspection retain separate clocks. Uninspected primary methods, reference lists, exact chemical authority and other experimental claims remain limitations.

## Findings

### F695-NSD2-VIABILITY-CLASS: Cell-viability assays are presented as enzyme-inhibition evidence

major / open / confirmed; issue key: epoxomicin-nsd2-1645876-1645877-viability-as-enzyme-inhibition.

Four epoxomicin annotations for PubChem AID 1645876/1645877 carry ENZYME_INHIBITOR. Both own assay protocols instead measure 72-hour CellTiter-Glo viability in isogenic RCH-ACV mutant 9B or WT 2C cells. Their source target metadata and generic inhibitors-of titles do not establish direct NSD2 enzymatic inhibition. Exact classifier replay identifies the generic-title fallback as the source of the four labels. The concern is the assay-specific classification and resulting aggregate provenance, not assay validity, the recorded numeric results, absence of NSD2 inhibition or absence of epoxomicin proteasome activity.

## Recommended Actions And Acceptance Checks

### A695-BOUND-NSD2-ASSAY-CLASSIFICATION

In later curation, change the maintained classifier using exact inspected AIDs/titles or an equivalently guarded assay-mode rule so these viability records no longer support direct enzyme inhibition merely through generic title wording. An unset class is acceptable until a separately justified replacement is selected. Reassess whether target_enzyme on the two O96028 projections overstates a mechanistic target; retain the exact O96028 source label and assay context even if a different documented representation is required. Preserve the raw inventory, all four target-dimension observations, source calls, OTHER/Potency values and unrelated 18 annotations; rederive the aggregate only from valid supported inputs. Keep the separately supported yeast proteasome graph intact.

- Add exact AID 1645876/1645877 title/protocol regression fixtures and a source-title drift guard; verify the narrow correction does not globally remove legitimate enzyme assays.
- Verify both paired target/no-target rows remain present with ACTIVE, OTHER, source Potency notes, 0.0129 uM (mutant) and 0.0073 uM (WT); do not relabel them as direct NSD2 IC50/Ki.
- Rebuild the epoxomicin fixture and check all 22 annotations, unaffected 18 values, source target provenance and aggregate provenance; explicitly distinguish target metadata from direct inhibition and preserve the P30656/1G65 graph.
- Run the maintained classifier/endpoint/summary regression tests and documented strict validation plus just verify-reproduction after authorized regeneration. These are future acceptance checks, not executions by this preparation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI695-LOCAL | /private/tmp/npm-review-work/shared-next-batch070-tentative/tentative-owner-source-inventory-001.json; /entries/4/owner_document; /entries/4/rows; /entries/4/row_guards; /entries/4/supplemental_retained_rows | context_only | The whole retained owner, seven arrays (26 raw rows), supplemental arrays, inline graphs and history were read. Producer/locus and other source assertions retain their original grades. |
| SCI695-CHEM | /private/tmp/npm-review-work/shared-next-batch070-tentative/source-science-preparation/root-tentative70-local-chemical-consistency-and-neighbors-001.json; /records/4/comparisons; /records/4/smiles; /records/4/inchi | supports | Saved RDKit 2026.03.5 results reproduce the declared full key DOGIDQKFVLKMLQ-JTHVHQAWSA-N and formula C28H50N4O7 from both encodings, with one fragment and formal charge zero. No unspecified tetrahedral carbon sites were reported. Internal consistency does not verify natural identity or all stereochemical assignments. |
| SCI695-BIOSYNTHESIS-ABSTRACT | /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-metadata-001/pmid-24168704.xml; ./PubmedArticle/MedlineCitation/PMID; ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText; ./PubmedArticle/PubmedData/ArticleIdList/ArticleId | partial | The own PMID 24168704 abstract identifies the epoxomicin cluster in actinobacterial strain ATCC 53904 and reports heterologous whole-pathway production in Streptomyces albus J1046. Broad hybrid NRPS/PKS and redox-enzyme context is supported; exact current Goodfellowiella taxon mapping and individual gene functions are not resolved. |
| SCI695-STRUCTURE-BIBLIOGRAPHY | /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-metadata-crossref-001/doi-10.1021-ja993588m.json; /message/DOI; /message/title; absence of supplied /message/abstract | context_only | The own DOI 10.1021/ja993588m metadata identifies the epoxomicin–20S proteasome crystal study but supplies no abstract. The separate saved deposition and UniProt fields supply the bounded structural checks below. |
| SCI695-ASSAY-MUTANT | /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-assay-structure-001/aid-1645876-description.json; /PC_AssayContainer/0/assay/descr/{aid,name,description,protocol,comment,target,results} | supports | Own AID 1645876 specifies RCH-ACV cell viability after 72 hours of compound exposure, measured with CellTiter-Glo. The matched protocol and results define a cell-killing concentration-response endpoint; Potency is AC50. NSD2 protein/gene target metadata does not make this a direct enzyme-activity assay. |
| SCI695-ASSAY-WT | /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-assay-structure-001/aid-1645877-description.json; /PC_AssayContainer/0/assay/descr/{aid,name,description,protocol,comment,target,results} | supports | Own AID 1645877 specifies RCH-ACV cell viability after 72 hours of compound exposure, measured with CellTiter-Glo. The matched protocol and results define a cell-killing concentration-response endpoint; Potency is AC50. NSD2 protein/gene target metadata does not make this a direct enzyme-activity assay. |
| SCI695-PDB | /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-assay-structure-001/1G65.cif; _entry.id=1G65; _entity.id11,15; _entity_poly.entity_id11,15; _struct_ref.pdbx_db_accession=P30656; _struct_ref_seq; _pdbx_poly_seq_scheme; _struct_conn.id=covale1..4; _chem_comp.id=04D | supports | Selected deposition rows identify PRE2 entity 11/P30656 on author chains K/Y and epoxomicin peptide entity 15 on author chains 3/4 (label CA/DA). Four covalent links connect terminal reacted 04D atoms C/C29 to Thr1 OG1/N. This supports the stored yeast beta5 binding graph; 04D is a reacted subcomponent, not the free intact compound. |
| SCI695-UNIPROT | /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-assay-structure-001/P30656.json; /primaryAccession; /proteinDescription; /organism; /genes; /sequence; /features[type=Propeptide,Chain,Active site]; /uniProtKBCrossReferences[database=PDB,id=1G65] | supports | Reviewed P30656 is Saccharomyces cerevisiae S288c PRE2/beta5, a 287-residue precursor with propeptide 1–75 and mature chain 76–287; Thr76 is the nucleophile. Its reciprocal 1G65 mapping is K/Y=76–287, consistent with mature Thr1 in the deposition. This is an organism-specific protein mapping, not a human target or potency measurement. |
| SCI695-CLASSIFIER | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; ACTIVITY_CLASS_PATTERNS; classify_activity; active assignment and summary derivation around lines128–178 and1357–1380 | supports | An isolated AST replay of the literal regex table and pure classifier maps both exact assay titles to ENZYME_INHIBITOR solely through generic inhibitors-of wording. The seeder attaches it to ACTIVE rows and derives the summary from emitted classifications. Maintained tests preserve source calls, numeric endpoints and unclassified observations. |

## Limits And Additional Notes

- The exact two assay descriptions were inspected, but no fresh compound-result table, raw dose-response curve or independent potency validation was obtained. Other 18 assay annotations retain their individual unverified experimental scopes.
- The selected mmCIF and UniProt fields support the yeast beta5 binding mapping; all atomic coordinates, the full crystal article, supplementary material and human-target extrapolation were not reviewed. Reacted 04D is not a free-compound identity standard.
- The biosynthesis abstract supports broad donor/host and whole-pathway claims; current taxonomic synonymy, exact constructs and full gene-by-gene mechanisms remain unresolved.
- The four assay-specific class labels are assessed within the stated source scope. No replacement class or corpus edit is made by this review.
- Full-owner scientific verification is not claimed. Official selection and intake were reconciled separately; this report records ROOT’s bounded scientific adjudication and preserves original evidence/access clocks.
- Configured consistency only; independent scientific claim support and unrestricted remote authority refresh are not implied.
- FailedQC001 is retained for an explicit separate network-enabled retry; no artifact will be overwritten.
- Fresh QC attempt001 failed on public canonical-artifact DNS retrieval after lint and before downstream tests. Its actual exit1/log/input capture/root observation remain pinned; the selected successful canonical QC attempt002 is separately timed. No individual-review validation failure or counter reset is claimed.
- 499non-blocking identifier-label warnings,35configured exceptions and4898no-adapter skips remain unverified within this gate.
- The QC test suite reported four skipped tests and two dependency deprecation warnings; this pass does not assert skipped checks ran.
- Canonical reproduction retains five unresolved assay-organism annotations,42 withheld nonsingle-organism producer claims and161 configured taxon-ID rewrites.
- This QC is a configured consistency gate, not an independent primary-source biological or stereochemical verification.
- Native baseline gates establish configured consistency, not independent biological production, exact stereochemistry or primary-source adequacy.
- The full configured gate logs retain warnings, skipped tests, identifier exceptions and no-adapter pairs; a successful command does not convert these into verified scientific claims.
- Ontology caches may be reused by the canonical identifier-label gate. Fresh command execution is not proof every remote authority was refreshed.
- Every tracked byte stream/mode and ignored-inclusive corpus/review YAML population was checked; external caches and generated bytecode are not asserted to be independently byte-pinned.
- The whole local owner and retained source rows were read. Full-owner scientific verification remains false; scientific_review denotes the bounded scientific interpretation in this report.
- Original owner/source reading, two-encoding computation, neighbor inspection, HTTP retrieval and later metadata reading retain separate clocks. Official intake separately computed SMILES facts.
- No scientific record, maintained input or native curation status was changed. Any findings and actions record ROOT-adopted proposed work; exact-source limitations and unavailable checks remain explicit.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
kind: record
repository: CultureBotAI/NaturalProductMech
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
review_id: 20261027T182535Z-epoxomicin
title: Scientific review of epoxomicin
started_at: '2026-10-27T18:24:14.870823Z'
finished_at: '2026-10-27T18:25:35.108399Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: Epoxomicin has internally consistent encodings, abstract-supported heterologous
  biosynthesis and directly checked yeast beta5 covalent-binding context. Four NSD2-associated
  enzyme-inhibitor annotations exceed the cell-viability assay evidence; a narrow
  maintained-source correction is proposed without changing imported observations
  or the proteasome graph.
source:
  git_revision: 14373517042b407747272446f79953ae86d51fa4
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: CLAUDE.md
    sha256: c783814c18591ea92aaa628fde98e6b0dbf1f59d45d240fe349682eec753e63f
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
    sha256: bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/amino_acids_and_peptides/epoxomicin.yaml
    sha256: 7560e7ff8564b7b234077cc832a8d6aee9cb72407517c254ff446985e7e997e4
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
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
    sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
    role: context
  - path: data/raw/pubchem_bioassay.tsv
    sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
    role: context
  - path: docs/CURATION.md
    sha256: c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_chebi.py
    sha256: 46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
targets:
- target_id: CHEBI:42265
  path: data/natural_products/amino_acids_and_peptides/epoxomicin.yaml
  label: epoxomicin
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: MIBiG source identity, producer and locus
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: LOTUS occurrence triples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: CyanoMetDB exact-structure occurrence source
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated owner transform
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/epoxomicin.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
scope:
  description: Review epoxomicin's retained identity, biosynthesis abstract, selected
    yeast beta5 mmCIF/UniProt mapping, and the exact descriptions of NSD2-associated
    AIDs 1645876/1645877. Adjudicate the four imported ENZYME_INHIBITOR classifications
    against their 72-hour cell-viability endpoint and the maintained classifier logic,
    preserving the 18 unrelated activity rows and the proteasome graph.
  selection: One owner selected in canonical unreviewed path order as campaign review
    695; whole retained owner and local source rows read, with bounded scientific
    interpretation.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CHEBI:42265
  exclusions:
  - target: Uninspected primary experiments and external authority claims
    reason: No new compound-result table, dose-response curve, independent potency
      test, full crystal article or complete atomic-coordinate audit was obtained.
      Yeast reacted 04D is not a free-compound standard or human-target proof; the
      assay descriptions neither establish direct NSD2 enzyme inhibition nor establish
      absence of an NSD2 effect.
  - target: Whole-owner scientific verification
    reason: The full-owner scientific-read flag remains false. Configured validation
      and internal chemical agreement do not establish every natural-product claim.
checks:
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its
    pinned path.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-verify-corpus-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.783967Z;
    finished 2026-10-25T22:37:16.453216Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-corpus.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-corpus.log.
    Reused for batch070 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch070. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:42265
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: Fresh canonical reproduction gate passed:all3116 records byte-identical
    to source seeding; source warnings remain retained.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-verify-reproduction-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.784055Z;
    finished 2026-10-25T22:37:31.682209Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-reproduction.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-reproduction.log.
    Reused for batch070 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch070. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:42265
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: Fresh deterministic review queue completed:8922 rows across12 queues. Queue
    output is not scientific-review coverage.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-review-queue-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just review-queue --tsv /private/tmp/npm-review-queue-batch-036-fresh14373517-001.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.781802Z;
    finished 2026-10-25T22:37:08.229737Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/review-queue.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/review-queue.log.
    Reused for batch070 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch070. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:42265
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking
    mismatches and4898no-adapter skips remain explicit.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-validate-products-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.784040Z;
    finished 2026-10-25T22:37:32.251879Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/validate-products.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/validate-products.log.
    Reused for batch070 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch070. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:42265
- check_id: shared-qc
  name: Full repository quality gate on the fresh main baseline
  status: passed
  required: true
  summary: Canonical just qc completed with actual terminal exit0:1024 tests passed,4
    skipped,2 dependency warnings;3116 records passed closed schema validation, site
    freshness, byte reproduction and lockfile integrity.22 governed artifacts and15
    raw inventories passed. Prior DNS failed001 remains preserved.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-qc-attempt-002
    PYTHONDONTWRITEBYTECODE=1 just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-002 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:40:55.179857Z;
    finished 2026-10-25T22:46:28.974296Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-002/qc.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-002/qc.log.
    Reused for batch070 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch070. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:42265
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/epoxomicin.yaml
    --out /private/tmp/npm-review-work/695/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-27T18:24:16.240735Z. Original
    receipt: /private/tmp/npm-review-work/695/strict-receipt.json.'
  target_ids:
  - CHEBI:42265
- check_id: SCI695-LOCAL-JOINS
  name: Retained owner/source consistency
  status: passed
  required: true
  summary: Whole retained source rows match original table indices and hashes; retained
    inventory arrays and the separate official-intake projections remain distinct.
  evidence_ids:
  - SCI695-LOCAL
  target_ids:
  - CHEBI:42265
- check_id: SCI695-ENCODING
  name: Saved two-encoding consistency
  status: passed
  required: true
  summary: Saved RDKit 2026.03.5 results reproduce the declared full key DOGIDQKFVLKMLQ-JTHVHQAWSA-N
    and formula C28H50N4O7 from both encodings, with one fragment and formal charge
    zero. No unspecified tetrahedral carbon sites were reported. Internal consistency
    does not verify natural identity or all stereochemical assignments.
  evidence_ids:
  - SCI695-CHEM
  target_ids:
  - CHEBI:42265
- check_id: SCI695-ASSAY-ID
  name: Own assay identity and mode
  status: passed
  required: true
  summary: Both exact AID identities, whole protocol/result-definition equality and
    cell-viability scope were checked. No fresh compound-result rows were retrieved.
  evidence_ids:
  - SCI695-ASSAY-MUTANT
  - SCI695-ASSAY-WT
  target_ids:
  - CHEBI:42265
- check_id: SCI695-CLASSIFICATION
  name: Assay-specific class support
  status: failed
  required: true
  summary: The four retained NSD2-associated ENZYME_INHIBITOR labels are not supported
    by these cell-viability assays as direct enzymatic-inhibition evidence. This is
    a scientific support check, not a validator execution.
  evidence_ids:
  - SCI695-LOCAL
  - SCI695-ASSAY-MUTANT
  - SCI695-ASSAY-WT
  - SCI695-CLASSIFIER
  target_ids:
  - CHEBI:42265
- check_id: SCI695-GRAPH
  name: Yeast protein and deposition mapping
  status: passed
  required: true
  summary: Selected entity, sequence, covalent-link and reciprocal accession fields
    agree with the stored two-node binding graph. All-coordinate validation and the
    complete article were not performed.
  evidence_ids:
  - SCI695-PDB
  - SCI695-UNIPROT
  target_ids:
  - CHEBI:42265
- check_id: SCI695-NATURAL-IDENTITY
  name: Exact natural identity and chemical authority
  status: unavailable
  required: true
  summary: No fresh compound authority or complete primary structural assignment was
    inspected. Saved encoding consistency is a bounded positive result.
  evidence_ids:
  - SCI695-LOCAL
  - SCI695-CHEM
  target_ids:
  - CHEBI:42265
evidence:
- evidence_id: SCI695-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch070-tentative/tentative-owner-source-inventory-001.json
  accessed_at: '2026-10-27T17:23:43.759851Z'
  locator: /entries/4/owner_document; /entries/4/rows; /entries/4/row_guards; /entries/4/supplemental_retained_rows
  snapshot_sha256: 13cf767342df76d1d021a671c40f3bc92ce39c66ccb901c6e2c8f5fb4d930f08
  support: context_only
  summary: The whole retained owner, seven arrays (26 raw rows), supplemental arrays,
    inline graphs and history were read. Producer/locus and other source assertions
    retain their original grades.
- evidence_id: SCI695-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch070-tentative/source-science-preparation/root-tentative70-local-chemical-consistency-and-neighbors-001.json
  accessed_at: '2026-10-27T17:34:35.695152Z'
  locator: /records/4/comparisons; /records/4/smiles; /records/4/inchi
  snapshot_sha256: 94aeb03505761a40ae670223d66cd990460a37bccbde68b2dc93172bb42f88f5
  support: supports
  summary: Saved RDKit 2026.03.5 results reproduce the declared full key DOGIDQKFVLKMLQ-JTHVHQAWSA-N
    and formula C28H50N4O7 from both encodings, with one fragment and formal charge
    zero. No unspecified tetrahedral carbon sites were reported. Internal consistency
    does not verify natural identity or all stereochemical assignments.
- evidence_id: SCI695-BIOSYNTHESIS-ABSTRACT
  kind: primary_source
  reference: /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-metadata-001/pmid-24168704.xml
  accessed_at: '2026-10-27T17:36:20.209220Z'
  locator: ./PubmedArticle/MedlineCitation/PMID; ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText;
    ./PubmedArticle/PubmedData/ArticleIdList/ArticleId
  snapshot_sha256: e1aa214a4dfc83620c7d1307650ce101b7a518102653d40578d3664068cf3a9c
  support: partial
  summary: The own PMID 24168704 abstract identifies the epoxomicin cluster in actinobacterial
    strain ATCC 53904 and reports heterologous whole-pathway production in Streptomyces
    albus J1046. Broad hybrid NRPS/PKS and redox-enzyme context is supported; exact
    current Goodfellowiella taxon mapping and individual gene functions are not resolved.
- evidence_id: SCI695-STRUCTURE-BIBLIOGRAPHY
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-metadata-crossref-001/doi-10.1021-ja993588m.json
  accessed_at: '2026-10-27T17:38:25.620363Z'
  locator: /message/DOI; /message/title; absence of supplied /message/abstract
  snapshot_sha256: d5716b8ab995c6cb474ccb8699b1c8a6cd48acbfe0c4885d784e3e94680e9081
  support: context_only
  summary: The own DOI 10.1021/ja993588m metadata identifies the epoxomicin–20S proteasome
    crystal study but supplies no abstract. The separate saved deposition and UniProt
    fields supply the bounded structural checks below.
- evidence_id: SCI695-ASSAY-MUTANT
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-assay-structure-001/aid-1645876-description.json
  accessed_at: '2026-10-27T17:48:05.277496Z'
  locator: /PC_AssayContainer/0/assay/descr/{aid,name,description,protocol,comment,target,results}
  snapshot_sha256: a636ef9f2e3879b7597d67423670e9f051caa526c9602ae897e4de8e5e7aad68
  support: supports
  summary: Own AID 1645876 specifies RCH-ACV cell viability after 72 hours of compound
    exposure, measured with CellTiter-Glo. The matched protocol and results define
    a cell-killing concentration-response endpoint; Potency is AC50. NSD2 protein/gene
    target metadata does not make this a direct enzyme-activity assay.
- evidence_id: SCI695-ASSAY-WT
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-assay-structure-001/aid-1645877-description.json
  accessed_at: '2026-10-27T17:48:05.277496Z'
  locator: /PC_AssayContainer/0/assay/descr/{aid,name,description,protocol,comment,target,results}
  snapshot_sha256: 4f4dea48ef0f9481627fc9771fbf9b5b0fffbccfde3c480fb7cde3661d3fcb27
  support: supports
  summary: Own AID 1645877 specifies RCH-ACV cell viability after 72 hours of compound
    exposure, measured with CellTiter-Glo. The matched protocol and results define
    a cell-killing concentration-response endpoint; Potency is AC50. NSD2 protein/gene
    target metadata does not make this a direct enzyme-activity assay.
- evidence_id: SCI695-PDB
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-assay-structure-001/1G65.cif
  accessed_at: '2026-10-27T17:48:05.277496Z'
  locator: _entry.id=1G65; _entity.id11,15; _entity_poly.entity_id11,15; _struct_ref.pdbx_db_accession=P30656;
    _struct_ref_seq; _pdbx_poly_seq_scheme; _struct_conn.id=covale1..4; _chem_comp.id=04D
  snapshot_sha256: cafc790ecbf3b7558d66e1cafe77b37a579cc1d03b595b510e30a1fe5ec6cd53
  support: supports
  summary: Selected deposition rows identify PRE2 entity 11/P30656 on author chains
    K/Y and epoxomicin peptide entity 15 on author chains 3/4 (label CA/DA). Four
    covalent links connect terminal reacted 04D atoms C/C29 to Thr1 OG1/N. This supports
    the stored yeast beta5 binding graph; 04D is a reacted subcomponent, not the free
    intact compound.
- evidence_id: SCI695-UNIPROT
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-assay-structure-001/P30656.json
  accessed_at: '2026-10-27T17:48:05.277496Z'
  locator: /primaryAccession; /proteinDescription; /organism; /genes; /sequence; /features[type=Propeptide,Chain,Active
    site]; /uniProtKBCrossReferences[database=PDB,id=1G65]
  snapshot_sha256: 96ebfae67dfa532e7d9da2c1c3555d0ee2b904aa3de5ac8c2662f218324a4e61
  support: supports
  summary: Reviewed P30656 is Saccharomyces cerevisiae S288c PRE2/beta5, a 287-residue
    precursor with propeptide 1–75 and mature chain 76–287; Thr76 is the nucleophile.
    Its reciprocal 1G65 mapping is K/Y=76–287, consistent with mature Thr1 in the
    deposition. This is an organism-specific protein mapping, not a human target or
    potency measurement.
- evidence_id: SCI695-CLASSIFIER
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  accessed_at: '2026-10-27T17:51:52.553748Z'
  locator: ACTIVITY_CLASS_PATTERNS; classify_activity; active assignment and summary
    derivation around lines128–178 and1357–1380
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
  support: supports
  summary: An isolated AST replay of the literal regex table and pure classifier maps
    both exact assay titles to ENZYME_INHIBITOR solely through generic inhibitors-of
    wording. The seeder attaches it to ACTIVE rows and derives the summary from emitted
    classifications. Maintained tests preserve source calls, numeric endpoints and
    unclassified observations.
assessments:
- assessment_id: SCI695-ENCODING
  area: representation
  topic: Internal chemical encoding
  outcome: supported
  summary: Saved RDKit 2026.03.5 results reproduce the declared full key DOGIDQKFVLKMLQ-JTHVHQAWSA-N
    and formula C28H50N4O7 from both encodings, with one fragment and formal charge
    zero. No unspecified tetrahedral carbon sites were reported. Internal consistency
    does not verify natural identity or all stereochemical assignments.
  evidence_ids:
  - SCI695-CHEM
  target_ids:
  - CHEBI:42265
- assessment_id: SCI695-STEREO
  area: identity
  topic: Natural stereochemical scope
  outcome: unknown
  summary: The 3 parsed-InChI unspecified double-bond observations are imidic C(-O)=N
    environments, not missing alkene configurations. No experimental reassignment
    or natural-identity conclusion follows from the local encoding check.
  evidence_ids:
  - SCI695-CHEM
  target_ids:
  - CHEBI:42265
- assessment_id: SCI695-PRODUCER
  area: provenance
  topic: Donor strain versus production host
  outcome: unknown
  summary: The abstract supports ATCC 53904 as the epoxomicin cluster donor and S.
    albus J1046 as the heterologous host. The retained Goodfellowiella coeruleoviolacea
    NCBITaxon:334858 label is not independently resolved by the abstract and is not
    treated as a demonstrated conflict.
  evidence_ids:
  - SCI695-LOCAL
  - SCI695-BIOSYNTHESIS-ABSTRACT
  target_ids:
  - CHEBI:42265
- assessment_id: SCI695-LOCUS
  area: provenance
  topic: Biosynthetic locus scope
  outcome: supported
  summary: Whole-pathway heterologous production supports the broad retained CLUSTER_DEMONSTRATED
    scope of BGC0000346 version 5/KF647219.1. Exact boundaries, constructs and individual
    functions remain unverified; putative derivatives are not substituted for epoxomicin.
  evidence_ids:
  - SCI695-LOCAL
  - SCI695-BIOSYNTHESIS-ABSTRACT
  target_ids:
  - CHEBI:42265
- assessment_id: SCI695-ASSAY-MODE
  area: evidence
  topic: Cell viability versus enzyme inhibition
  outcome: concern
  summary: Owner bioactivities[6–9] are four source projections of two viability assays,
    including blank-target and O96028 target-dimension rows. Generic inhibition wording
    does not establish direct NSD2 inhibition. Preserve their ACTIVE calls, values
    0.0073/0.0129 uM, source Potency endpoint and OTHER measurement type while correcting
    the unsupported activity-class inference.
  evidence_ids:
  - SCI695-LOCAL
  - SCI695-ASSAY-MUTANT
  - SCI695-ASSAY-WT
  - SCI695-CLASSIFIER
  target_ids:
  - CHEBI:42265
- assessment_id: SCI695-GRAPH
  area: graph
  topic: Epoxomicin binding to yeast beta5
  outcome: supported
  summary: 'The retained two-node/one-edge graph is supported within the saved deposition
    scope: chains 3/4 form covalent adducts with mature Thr1 of PRE2 K/Y, reciprocally
    mapped to UniProt P30656 Thr76. This organism-specific binding evidence neither
    supplies an NSD2 mechanism nor verifies all claims in the crystal article.'
  evidence_ids:
  - SCI695-LOCAL
  - SCI695-PDB
  - SCI695-UNIPROT
  target_ids:
  - CHEBI:42265
- assessment_id: SCI695-ACTIVITY-SCOPE
  area: quantity
  topic: Imported observations and aggregate support
  outcome: unknown
  summary: All 22 owner annotations and 23 retained PubChem rows remain distinct source
    records; the empty CID 9915668 row is not an assay. No automatic deduplication,
    changed potency, direct NSD2 IC50 or new classification is assigned. The proteasome
    evidence does not rescue the four assay-specific class labels; it also prevents
    interpreting their defect as proof that epoxomicin lacks enzyme-inhibitor activity
    generally.
  evidence_ids:
  - SCI695-LOCAL
  - SCI695-ASSAY-MUTANT
  - SCI695-ASSAY-WT
  - SCI695-PDB
  target_ids:
  - CHEBI:42265
- assessment_id: SCI695-COVERAGE
  area: completeness
  topic: Bounded scientific coverage
  outcome: unknown
  summary: Original local reading, saved computation and each external source inspection
    retain separate clocks. Uninspected primary methods, reference lists, exact chemical
    authority and other experimental claims remain limitations.
  evidence_ids:
  - SCI695-LOCAL
  - SCI695-CHEM
  target_ids:
  - CHEBI:42265
findings:
- finding_id: F695-NSD2-VIABILITY-CLASS
  issue_key: epoxomicin-nsd2-1645876-1645877-viability-as-enzyme-inhibition
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Cell-viability assays are presented as enzyme-inhibition evidence
  description: Four epoxomicin annotations for PubChem AID 1645876/1645877 carry ENZYME_INHIBITOR.
    Both own assay protocols instead measure 72-hour CellTiter-Glo viability in isogenic
    RCH-ACV mutant 9B or WT 2C cells. Their source target metadata and generic inhibitors-of
    titles do not establish direct NSD2 enzymatic inhibition. Exact classifier replay
    identifies the generic-title fallback as the source of the four labels. The concern
    is the assay-specific classification and resulting aggregate provenance, not assay
    validity, the recorded numeric results, absence of NSD2 inhibition or absence
    of epoxomicin proteasome activity.
  target_ids:
  - CHEBI:42265
  field_paths:
  - bioactivities[6].activity_class
  - bioactivities[7].activity_class
  - bioactivities[8].activity_class
  - bioactivities[9].activity_class
  - bioactivity_summary
  evidence_ids:
  - SCI695-LOCAL
  - SCI695-ASSAY-MUTANT
  - SCI695-ASSAY-WT
  - SCI695-CLASSIFIER
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: maintained
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_seed_skeleton.py
    role: maintained
  rule_id: assay-classification-must-match-inspected-assay-mode
  native_severity: unsupported assay-level mechanism inference
  normalization_reason: 'Major source-support concern: direct protocol evidence and
    exact source trace establish the unsupported classification. No replacement class
    or whole-compound mechanism verdict is inferred.'
actions:
- action_id: A695-BOUND-NSD2-ASSAY-CLASSIFICATION
  finding_ids:
  - F695-NSD2-VIABILITY-CLASS
  target_ids:
  - CHEBI:42265
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: maintained
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_seed_skeleton.py
    role: maintained
  description: In later curation, change the maintained classifier using exact inspected
    AIDs/titles or an equivalently guarded assay-mode rule so these viability records
    no longer support direct enzyme inhibition merely through generic title wording.
    An unset class is acceptable until a separately justified replacement is selected.
    Reassess whether target_enzyme on the two O96028 projections overstates a mechanistic
    target; retain the exact O96028 source label and assay context even if a different
    documented representation is required. Preserve the raw inventory, all four target-dimension
    observations, source calls, OTHER/Potency values and unrelated 18 annotations;
    rederive the aggregate only from valid supported inputs. Keep the separately supported
    yeast proteasome graph intact.
  acceptance_checks:
  - Add exact AID 1645876/1645877 title/protocol regression fixtures and a source-title
    drift guard; verify the narrow correction does not globally remove legitimate
    enzyme assays.
  - Verify both paired target/no-target rows remain present with ACTIVE, OTHER, source
    Potency notes, 0.0129 uM (mutant) and 0.0073 uM (WT); do not relabel them as direct
    NSD2 IC50/Ki.
  - Rebuild the epoxomicin fixture and check all 22 annotations, unaffected 18 values,
    source target provenance and aggregate provenance; explicitly distinguish target
    metadata from direct inhibition and preserve the P30656/1G65 graph.
  - Run the maintained classifier/endpoint/summary regression tests and documented
    strict validation plus just verify-reproduction after authorized regeneration.
    These are future acceptance checks, not executions by this preparation.
  generator: scripts/seed_from_sources.py::classify_activity and build_records
limitations:
- The exact two assay descriptions were inspected, but no fresh compound-result table,
  raw dose-response curve or independent potency validation was obtained. Other 18
  assay annotations retain their individual unverified experimental scopes.
- The selected mmCIF and UniProt fields support the yeast beta5 binding mapping; all
  atomic coordinates, the full crystal article, supplementary material and human-target
  extrapolation were not reviewed. Reacted 04D is not a free-compound identity standard.
- The biosynthesis abstract supports broad donor/host and whole-pathway claims; current
  taxonomic synonymy, exact constructs and full gene-by-gene mechanisms remain unresolved.
- The four assay-specific class labels are assessed within the stated source scope.
  No replacement class or corpus edit is made by this review.
- Full-owner scientific verification is not claimed. Official selection and intake
  were reconciled separately; this report records ROOT’s bounded scientific adjudication
  and preserves original evidence/access clocks.
- Configured consistency only; independent scientific claim support and unrestricted
  remote authority refresh are not implied.
- FailedQC001 is retained for an explicit separate network-enabled retry; no artifact
  will be overwritten.
- Fresh QC attempt001 failed on public canonical-artifact DNS retrieval after lint
  and before downstream tests. Its actual exit1/log/input capture/root observation
  remain pinned; the selected successful canonical QC attempt002 is separately timed.
  No individual-review validation failure or counter reset is claimed.
- 499non-blocking identifier-label warnings,35configured exceptions and4898no-adapter
  skips remain unverified within this gate.
- The QC test suite reported four skipped tests and two dependency deprecation warnings;
  this pass does not assert skipped checks ran.
- Canonical reproduction retains five unresolved assay-organism annotations,42 withheld
  nonsingle-organism producer claims and161 configured taxon-ID rewrites.
- This QC is a configured consistency gate, not an independent primary-source biological
  or stereochemical verification.
- Native baseline gates establish configured consistency, not independent biological
  production, exact stereochemistry or primary-source adequacy.
- The full configured gate logs retain warnings, skipped tests, identifier exceptions
  and no-adapter pairs; a successful command does not convert these into verified
  scientific claims.
- Ontology caches may be reused by the canonical identifier-label gate. Fresh command
  execution is not proof every remote authority was refreshed.
- Every tracked byte stream/mode and ignored-inclusive corpus/review YAML population
  was checked; external caches and generated bytecode are not asserted to be independently
  byte-pinned.
notes:
- The whole local owner and retained source rows were read. Full-owner scientific
  verification remains false; scientific_review denotes the bounded scientific interpretation
  in this report.
- Original owner/source reading, two-encoding computation, neighbor inspection, HTTP
  retrieval and later metadata reading retain separate clocks. Official intake separately
  computed SMILES facts.
- No scientific record, maintained input or native curation status was changed. Any
  findings and actions record ROOT-adopted proposed work; exact-source limitations
  and unavailable checks remain explicit.
```
