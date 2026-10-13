# Aborycin: anhydride connectivity conflicts with the reported natural product

- Review: 20261013T131439Z-aborycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T12:55:13.493962Z
- Finished UTC: 2026-10-13T13:14:39.496952Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed blocker: stored graph has an anhydride/free amino-Cys instead of the reported N-terminal macrolactam. PubChem matches the same wrong graph. Exact biochemical origin cannot be attributed to it. Full experimental/stereochemical assessment remains access-limited.

## Scope And Provenance

One exact resolved owner; same-label sibling used only as identity/locus context. Full campaign remains3115 owners and243 components.

Selection: Next exact pending owner in the verified full campaign checkpoint; all pending owners remain in scope, not a sample.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 9191a148302dce8d04699b8436a68b84329d20b8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-90494a0512 | data/natural_products/amino_acids_and_peptides/aborycin.yaml | generated | aborycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict | passed | True | naturalproductmech:mibig-90494a0512 | Two exact owners and their referenced components: zero schema errors. |
| labels | passed | True | naturalproductmech:mibig-90494a0512 | Full configured gate:13434 canonical,646 synonym,35 exception,499 nonblocking warning mismatches and4649 no-adapter skips. Minted chemical IDs are skipped; their identity was checked separately. |
| chemistry | passed | True | naturalproductmech:mibig-90494a0512 | Pinned RDKit calculations and topology reconstruction succeeded; result is computational context, not experimental sign-off. |
| sequence-audit | failed | False | naturalproductmech:mibig-90494a0512 | Initial audit failed because ordinary GenBank XML supplied a RefSeq CONTIG pointer without bases. No scientific conclusion used the failed attempt. |
| sequence-audit-with-parts | passed | True | naturalproductmech:mibig-90494a0512 | Retry with official gbwithparts XML succeeded; source accessions, feature locations and bounded exact sequence searches are retained. |
| ignored-inclusive-search | passed | False | naturalproductmech:mibig-90494a0512 | Identifier, name, key and DOI search included hidden/gitignored repository text; only .git and .venv runtime data excluded. Search did not find an implemented aborycin correction row. Source table and consumer semantics were inspected separately. |
| qc | passed | True | naturalproductmech:mibig-90494a0512 | Full native just qc passed: 723 passed, 3 skipped, 2 warnings in 448.24s (0:07:28). Includes strict corpus schema, tests/history/graph invariants, lint, pinned vendored sync, source provenance, generated site, reproduction and path-lock checks. Deterministic success is not scientific sign-off. |
| review-queue | passed | False | naturalproductmech:mibig-90494a0512 | Full native pending-record queue regenerated in the private workspace. Multiple diagnostic rows are not distinct owners or completed scientific reviews. |
| validate-drafts | failed | False | naturalproductmech:mibig-90494a0512 | Premature draft validation failed because the draft builder was waiting for the still-running QC receipt and had not written the draft files. No bundle was saved; this sequencing failure is retained before the later successful validation. |
| Structured expression-source applicability | not_applicable | False | naturalproductmech:mibig-90494a0512 | Owners contain no named gene, protein, regulator or transcriptomic-module claims. MIBiG, public sequence APIs and chemical authority APIs were used first. Gene annotations inspected as sequence context do not create expression claims; no iModulon coverage-absence inference is made. |
| Complete primary experimental and isolate-form verification | unavailable | True | naturalproductmech:mibig-90494a0512 | Primary abstracts were inspected, but experimental details, chemical figures/spectra and cloned-locus boundaries remain access-limited. No full scientific completion or native status promotion. |
| Independent resolution of LOTUS organism note | unavailable | False | naturalproductmech:mibig-90494a0512 | Q22285749 page unavailable through the web tool; taxon35619 independently verifies at NCBI. Applies to the aborycin-2 occurrence, consulted as sibling context for aborycin. |
| Independent current-alias status check | unavailable | True | naturalproductmech:mibig-90494a0512 | Exact versioned entries are active in their inspected JSON. Unversioned annotations endpoints returned404 and repository pages were inaccessible; current-alias resolution or absence of later versions is not independently proven. Do not infer retirement from this result. |

## Scientific And Domain Assessments

### Exact bond connectivity and supported stereochemical resolution

identity: concern. Targets: naturalproductmech:mibig-90494a0512.

FHQR reproduces the upstream MIBiG/PubChem graph but leaves Cys1 amino free and uses an anhydride linkage instead of the reported N-terminal macrolactam. The graph conflicts with aborycin identity independently of the incomplete stereo flag. The issue is not cured by matching the formula or PubChem.

### Exact external equivalence and minted grounding

grounding: supported. Targets: naturalproductmech:mibig-90494a0512.

The stored xref exactly matches the stored chemical graph. No exact-key3-star ChEBI row occurs in the pinned inventory. Database identity agreement does not settle whether the label is scientifically correct; no arbitrary grounding or merger was made.

### Computed filing, asserted BGC class and taxon facets

provenance: supported. Targets: naturalproductmech:mibig-90494a0512.

The pinned classifier and RIBOSOMAL source assertion are separated. Taxon identifiers and labels agree with current NCBI and pinned names; ACTINOBACTERIAL is consistent. No computed class or taxonomic facet was used to prove origin.

### Native producer versus heterologous experimental host

evidence: concern. Targets: naturalproductmech:mibig-90494a0512.

The named producer is supported for biological aborycin at abstract level, but that evidence cannot establish production of the wrong FHQR graph. SOURCE_ASSERTION is correctly attributed as a database assertion, yet the exact-structure origin remains blocked by F1.

### Exact versioned cluster and genomic interval

evidence: supported. Targets: naturalproductmech:mibig-90494a0512.

The active entry/version and coordinates match the source, and contig39 contains the expected precursor/cyclase context within the interval. CLUSTER_UNSTATED honestly reports no method in this entry; the2019 abstract offers an upgrade lead only after exact experiment and identity adjudication. Genomic context does not repair F1.

### LOTUS exact-key occurrence and taxonomic scope

evidence: concern. Targets: naturalproductmech:mibig-90494a0512.

The LOTUS genus occurrence cites the same2019 study as the MIBiG producer, not independent corroboration. The abstract supports biological aborycin, not the conflicting FHQR graph. F1 therefore also blocks the exact-key occurrence interpretation.

### Optional assays, pathways, targets, graphs and history

completeness: unknown. Targets: naturalproductmech:mibig-90494a0512.

Complete owners and histories have no stored graphs/components, pathway steps, protein examples, assays, targets, clinical assertions or sibling joins. These optional omissions are not false claims. Literature offers bounded mechanism/assay leads, but full methods and exact compound-form support must precede additions. No evidence/status/history mutation occurred.

### Native deterministic checks and provenance

schema: supported. Targets: naturalproductmech:mibig-90494a0512.

Strict target validation, configured label gate and full native QC pass. All3115 owner hashes,243 components and21 pre-existing review pairs were verified against the prior merged checkpoint. This does not scientifically review their content or close earlier findings.

## Findings

### F1: Encoded anhydride graph is not the reported aborycin macrolactam

blocker / open / confirmed; issue key: aborycin-BGC0002015-anhydride-wrong-connectivity.

FHQRLPHOFHPTCX-BDHXJCCSSA-N contains an anhydride and free amino-Cys instead of the Cys1-N to Asp9-side-chain amide explicitly described by the original isolation abstract. The current PubChem and MIBiG entries reproduce this same defect. Removing stereochemistry does not make it AJFZ; deposited-core reconstruction with the reported bonds yields AJFZ. The formula and database xref match are insufficient to carry aborycin production/occurrence claims onto this different graph.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the source chemistry and repair or quarantine the BGC0002015:1 identity through a maintained, tested source-pinned path. Resolve its relationship to the occupied AJFZ sibling explicitly. The current REPLACE_WITH_CHEBI consumer cannot replace with an arbitrary graph or merge occupied owners; reserved decisions.tsv does nothing. Do not simply drop the exact-to-current-graph PubChem xref or hand-edit generated YAML.

- Confirm primary bond pattern, isolate stereochemical resolution and intended source compound; preserve uncertainty rather than invent stereocenters.
- Demonstrate absence of the spurious anhydride/free N-terminal amino group in any corrected aborycin structure; recompute SMILES/InChI/key.
- Explicitly adjudicate existing-owner collision, identifiers/PATHS, both source concepts and each exact-key occurrence/xref; transfer no claims by name alone.
- Preserve raw assertions, source-row hashes and curation attribution; test missing/duplicate/drift/conflict inputs.
- Run guarded canary, strict validation, provenance, corpus/path lock, reproduction, generated site and full QC; preserve all unrelated owners/components.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/amino_acids_and_peptides/aborycin.yaml; Complete raw YAML, all history entries and read_natural_product resolved view | supports | Exactly one minted, SEEDED owner; no graph refs or inline graphs. Full contents were read before judgement. Both stored histories are unchanged seeding events, not scientific sign-off. The same-label sibling is context only. |
| inventories | data/raw/mibig_compounds.tsv; BGC0002015:1 at TSV2301; BGC0002285:1 at TSV2762; exact-key LOTUS and classifier rows | supports | Both owners reproduce their distinct imported chemical keys. LOTUS joins by exact key; no exact-key ChEBI or AntibioticMech row was found in the complete pinned TSV scans. NPClassifier2026-09-07 reports Amino acids and Peptides/Oligopeptides/Cyclic peptides for both. This is filing provenance, not an experimental classification or live universal ChEBI absence claim. |
| chemistry | /private/tmp/npmech-aborycin-review-JJKFYR/chemistry.json; RDKit2026.03.5 owner roundtrip, functional-group matches, stereo removal and deposited-core topology reconstruction | supports | Both SMILES reproduce stored InChI/keys, neutral C97H131N23O26S4 and exact mass2161.851845312 Da. AJFZ has18 unspecified centers,22 amide carbonyls,one acid and no free amino-Cys/anhydride. FHQR has17 specified/one unspecified center,21 amide carbonyls,one free amino-Cys and one anhydride,no acid. Both contain two disulfides. The deposited21-residue core with the1994 abstract bond pattern reconstructs AJFZ after removing stereo, not FHQR; this does not establish lasso threading or absolute configuration. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0002015.4/annotations.json; Exact entry version/status, compound structure/xref, taxonomy, locus accession/bounds/method and cited reference | supports | Active BGC0002015v4 asserts NZ_MKCP01000039.1:18549..30566, taxon1904044, no locus method, FHQR chemistry and PubChem136150874. PMID30795576 is the legacy reference. Source agreement does not establish correct chemistry. |
| xref | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/136150874/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES,IsomericSMILES/JSON; Exact SMILES, InChIKey, formula and cited isolation source where provided | supports | PubChem136150874 exactly matches FHQR and the stored SMILES/InChI. This is a correct database xref for the encoded graph, not independent proof that the graph represents the natural product. Removing only the xref would not repair the identity defect. |
| paper1994 | DOI:10.1002/jlac.199419940716; Publisher-deposited abstract in Crossref message.abstract; title/year/DOI | partial | The abstract reports isolation from S.griseoflavus TU4072, purification and structural analysis of a21-residue peptide. It explicitly assigns Asp9-side-chain to Cys1-N-terminal closure and Cys1-Cys13/Cys7-Cys19 disulfides. Full spectra, stereochemical assignments and figure were not inspected. |
| paper2019 | PMID:30795576; EuropePMC resultList.result[0].abstractText and PMID/DOI/PMCID aliases | partial | The abstract reports aborycin isolation from SCSIO ZS0098 and production after heterologous expression in S.coelicolor M1152. It describes a ribosomal type I lasso peptide. This supports the named compound/organism context, not either exact imported contig or the FHQR bond graph; experimental methods remain uninspected. |
| sequence-source | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=MKCP01000045.1,NZ_MKCP01000039.1&amp;rettype=gbwithparts&amp;retmode=xml; GBSeq records, source features, exact accession versions, complete sequence and CDS feature tables | supports | MKCP01000045.1 is816609bp contig5; NZ_MKCP01000039.1 is120871bp contig44 with a CONTIG link to MKCP01000039.1. Both source features specify ZS0098 and taxon1904044. The latter contains precursor22746..22874 and cyclase22936..24747 plus B1/B2 annotations. These annotations explicitly derive from computational PGAP methods, not new biochemical experiments. |
| sequence-audit | /private/tmp/npmech-aborycin-review-JJKFYR/sequence-audit.json; Complete structured feature scan of each claimed interval; exact129nt precursor query on both full contigs/both strands | supports | The MKCP01000045.1 interval contains oxidoreductase, proline-racemase, sugar/sulfate transport and regulator annotations. The exact129nt precursor from contig39 occurs once on contig39 and not on either strand of contig45. Bounds18549..30566 and extended34000 fit annotated genes on contig39. This is a substantial accession-context conflict, not proof that all divergent/unannotated lasso genes are absent. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1904044,1883,35619&amp;retmode=xml; TaxIds1904044,1883,35619; corresponding pinned corpus_taxa.obo terms | supports | Live NCBI and the pinned labels agree: Streptomyces sp. ZS0098(species rank), Streptomyces(genus), S.griseoflavus(species). Both sequence source features retain ZS0098. ACTINOBACTERIAL is consistent with the lineage; genus occurrence does not imply every member produces the compound. |
| wiki-context | https://www.wikidata.org/wiki/Q1144013; Organism label and rank; Q22285749 retrieval limitation | partial | Q1144013 resolves to genus Streptomyces. Q22285749 could not be independently inspected after two web-tool failures; its S.griseoflavus association is retained only as committed LOTUS provenance, with the NCBI species verified separately. |
| governance | docs/CURATION.md; Identity/sign-off, narrow curation inputs and generated boundaries; docs/HARMONIZATION.md producer/locus separation; conf/producer_evidence.tsv | supports | SOURCE_ASSERTION is a database producer tier; heterologous expression grades only the locus. Method absence stays CLUSTER_UNSTATED. The structure correction consumer supports only an unoccupied3-star ChEBI target, not arbitrary replacement or merger into the existing AJFZ owner. decisions.tsv is reserved and not consumed. No correction, merge or status promotion was performed. |
| access | /private/tmp/npmech-aborycin-review-JJKFYR/access-limitations.json; Actual web-tool rate limit, failed DOI resolution and denied alternate publisher command | context_only | 2019 full text returned429. The1994 DOI did not yield source text and auto-review denied the subsequent publisher request before execution. No alternate full-text retrieval followed. Abstracts were inspected independently. All180 inherited stops remain; these two primary-source limits and the unresolved Wikidata check are explicit. |

## Limits And Additional Notes

- This observation assesses exact committed inputs at9191a148; their current bytes were checked against git show. No record, raw inventory, curation decision, generated page or prior review was edited.
- Full primary methods, spectra, chemical figure, isolate stereochemistry and cloned-locus endpoints remain unverified. Neither abstract evidence nor RDKit/PGAP computation substitutes for those checks.
- Both primary access limits, all180 inherited stops and the unresolved Wikidata species note are retained. No paid research, contacts, alternate retrieval after barriers or GitHub mutations.
- The exact precursor search is limited to the two fetched contigs and literal nucleotide equality; it cannot prove absence of divergent or unannotated lasso genes.
- The repository interpreter lacked Biopython; structured NCBI XML and standard ElementTree were used without installing dependencies. The initial missing-sequence parse failure is retained and superseded by the explicit gbwithparts check.
- Single-record denominator1; the campaign denominator3115 is unchanged. Partial observations do not count as completed scientific reviews.
- Only new immutable review bundles are authorized; actions are proposed, not executed.
- Two separate source entries and different first InChIKey blocks do not authorize a merge. Here the specific bond conflict, not the hash difference alone, supports the identity finding.
- The final canonical saver/contract check is recorded separately after these drafts are validated; it is not retroactively claimed as a pre-save command.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T131439Z-aborycin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Aborycin: anhydride connectivity conflicts with the reported natural product'
started_at: '2026-10-13T12:55:13.493962Z'
finished_at: '2026-10-13T13:14:39.496952Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant/thread as prior corpus work; this is not independent
    human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One confirmed blocker: stored graph has an anhydride/free amino-Cys instead
  of the reported N-terminal macrolactam. PubChem matches the same wrong graph. Exact
  biochemical origin cannot be attributed to it. Full experimental/stereochemical
  assessment remains access-limited.'
source:
  git_revision: 9191a148302dce8d04699b8436a68b84329d20b8
  state: git_commit
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
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: a1eb14fec4a7cee0c2fc25c43091e75af24ae62c44c4f7659ed7aedf0e6a0e6c
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 8762b6c3e9b048d64965049aad4addbaefdf76e817f6043e42301c68e301c25a
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: 7f2c7a379c0ccf72311ae69c49d5f68c65b56768fd4c785ce9ef47ee7d1bf7b2
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/amino_acids_and_peptides/aborycin-2.yaml
    sha256: f4647c9a8a389711cbac96ee2750ffbf9c5a3e0d844303f46ad07ec5ff42a535
    role: context
  - path: data/natural_products/amino_acids_and_peptides/aborycin.yaml
    sha256: dc0d052e7052a1db26d5cb39b7cadd37479574f2c2902667b48d47221ed9a13d
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
  - path: docs/CURATION.md
    sha256: 73a0fd94ffd5d283f3e12bdd291a4906b61257c99bd78e18165c941c4583e5d4
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
    sha256: 8d82d7633e0492e9fe16011f6e5af6f8024f573e80c8a24176b65e2941478b71
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: 6026ddca19f0989d499b1681f7724fbab23918de8d3957750b49bbfe1a9c0bff
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: a8b8834788b4714cf1cb0d1cc410d5c2f88112a32ad8621c8e043f0a4bc38a9d
    role: context
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: ea8720cae8461b30fad3a64e32211de965a6a0d6b1ec3c3d9f3db27ab904282a
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
  - path: uv.lock
    sha256: c62a5739e3ffeb12cc57b3bf12a31dcf9cdfbf00b417f4ba3a801d51ef9efbe3
    role: context
targets:
- target_id: naturalproductmech:mibig-90494a0512
  path: data/natural_products/amino_acids_and_peptides/aborycin.yaml
  label: aborycin
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
    role: Implemented exact-row-pinned PubChem xref exclusions
scope:
  description: One exact resolved owner; same-label sibling used only as identity/locus
    context. Full campaign remains3115 owners and243 components.
  selection: Next exact pending owner in the verified full campaign checkpoint; all
    pending owners remain in scope, not a sample.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-90494a0512
  exclusions:
  - target: Other3114 owners
    reason: Not scientifically assessed by this single-owner observation; retained
      in the exhaustive campaign checkpoint.
checks:
- check_id: strict
  name: strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/natural_products/amino_acids_and_peptides/aborycin-2.yaml
    data/natural_products/amino_acids_and_peptides/aborycin.yaml --out /private/tmp/npmech-aborycin-review-JJKFYR/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-90494a0512
  summary: 'Two exact owners and their referenced components: zero schema errors.'
  scope_note: 'Actual execution: 2026-10-13T12:55:37.660505Z to 2026-10-13T12:55:41.049600Z;
    logSHA256 9f43836abd34ebc1a3b1b25fa6ceb2c8aeb34feb7836b3b296f1e922719f9c0a'
- check_id: labels
  name: labels
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-90494a0512
  summary: Full configured gate:13434 canonical,646 synonym,35 exception,499 nonblocking
    warning mismatches and4649 no-adapter skips. Minted chemical IDs are skipped;
    their identity was checked separately.
  scope_note: 'Actual execution: 2026-10-13T12:56:34.564901Z to 2026-10-13T12:58:21.287065Z;
    logSHA256 556ef5804e095767472c0aa8a542d5bff7e332470383a992e6b260103034414b'
- check_id: chemistry
  name: chemistry
  status: passed
  required: true
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-aborycin-review-JJKFYR/chemistry.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-90494a0512
  summary: Pinned RDKit calculations and topology reconstruction succeeded; result
    is computational context, not experimental sign-off.
  scope_note: 'Actual execution: 2026-10-13T12:59:12.775066Z to 2026-10-13T12:59:15.383570Z;
    logSHA256 5f4415de17e020b9b386f9edd9ac1968ec6cca04aaaab876152aa5412a95f172'
- check_id: sequence-audit
  name: sequence-audit
  status: failed
  required: false
  command: .venv/bin/python /private/tmp/npmech-aborycin-review-JJKFYR/sequence_audit.py
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-90494a0512
  summary: Initial audit failed because ordinary GenBank XML supplied a RefSeq CONTIG
    pointer without bases. No scientific conclusion used the failed attempt.
  scope_note: 'Actual execution: 2026-10-13T13:00:33.181029Z to 2026-10-13T13:00:33.356380Z;
    logSHA256 bf942b35f4e53fa99baa52e6baf825c402d770338486f1e607cac8d7cdc2c766'
- check_id: sequence-audit-with-parts
  name: sequence-audit-with-parts
  status: passed
  required: true
  command: .venv/bin/python /private/tmp/npmech-aborycin-review-JJKFYR/sequence_audit.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-90494a0512
  summary: Retry with official gbwithparts XML succeeded; source accessions, feature
    locations and bounded exact sequence searches are retained.
  scope_note: 'Actual execution: 2026-10-13T13:01:24.890965Z to 2026-10-13T13:01:25.202941Z;
    logSHA256 cd286b40870a68a335ca2a09488bb30a19b23618acafb5387b43c81d73e610db'
- check_id: ignored-inclusive-search
  name: ignored-inclusive-search
  status: passed
  required: false
  command: rg --no-ignore --hidden -l -i 'aborycin|BGC0002015|BGC0002285|AJFZCVFYMNSDFP|FHQRLPHOFHPTCX|md17020127|199419940716'
    . -g '!.git/**' -g '!.venv/**'
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-90494a0512
  summary: Identifier, name, key and DOI search included hidden/gitignored repository
    text; only .git and .venv runtime data excluded. Search did not find an implemented
    aborycin correction row. Source table and consumer semantics were inspected separately.
  scope_note: 'Actual execution: 2026-10-13T12:57:58.412522Z to 2026-10-13T12:57:58.642305Z;
    logSHA256 69de095c6582ff90af33f9eb9c736418fc45ae91dded06c99ae93acb6fd876eb'
- check_id: qc
  name: qc
  status: passed
  required: true
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-90494a0512
  summary: 'Full native just qc passed: 723 passed, 3 skipped, 2 warnings in 448.24s
    (0:07:28). Includes strict corpus schema, tests/history/graph invariants, lint,
    pinned vendored sync, source provenance, generated site, reproduction and path-lock
    checks. Deterministic success is not scientific sign-off.'
  scope_note: 'Actual execution: 2026-10-13T12:55:36.464744Z to 2026-10-13T13:14:32.308462Z;
    logSHA256 ce22cda9aa173d3e8cace4b487e88e12a9b430fc3c0dd8923ccc5550b3158751'
- check_id: review-queue
  name: review-queue
  status: passed
  required: false
  command: .venv/bin/python scripts/curation_worklist.py --review-records --limit
    0 --tsv /private/tmp/npmech-aborycin-review-JJKFYR/review-queue.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-90494a0512
  summary: Full native pending-record queue regenerated in the private workspace.
    Multiple diagnostic rows are not distinct owners or completed scientific reviews.
  scope_note: 'Actual execution: 2026-10-13T13:02:19.751200Z to 2026-10-13T13:03:38.066731Z;
    logSHA256 b56a7a660be0b9f646fd83f6aae8ea825f8c82cdc19a608cb74a9f0d034fff5e'
- check_id: validate-drafts
  name: validate-drafts
  status: failed
  required: false
  command: .venv/bin/python scripts/record_review.py validate /private/tmp/npmech-aborycin-review-JJKFYR/aborycin-2-review.yaml
    /private/tmp/npmech-aborycin-review-JJKFYR/aborycin-review.yaml
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-90494a0512
  summary: Premature draft validation failed because the draft builder was waiting
    for the still-running QC receipt and had not written the draft files. No bundle
    was saved; this sequencing failure is retained before the later successful validation.
  scope_note: 'Actual execution: 2026-10-13T13:05:50.399653Z to 2026-10-13T13:05:53.429467Z;
    logSHA256 99951329b2114b54b393aafb9b3288f7b11c9d591ebbe93f3780b731bde58687'
- check_id: imodulondb
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  target_ids:
  - naturalproductmech:mibig-90494a0512
  summary: Owners contain no named gene, protein, regulator or transcriptomic-module
    claims. MIBiG, public sequence APIs and chemical authority APIs were used first.
    Gene annotations inspected as sequence context do not create expression claims;
    no iModulon coverage-absence inference is made.
- check_id: primary-fulltext
  name: Complete primary experimental and isolate-form verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - access
  - paper1994
  - paper2019
  summary: Primary abstracts were inspected, but experimental details, chemical figures/spectra
    and cloned-locus boundaries remain access-limited. No full scientific completion
    or native status promotion.
- check_id: wikidata-species
  name: Independent resolution of LOTUS organism note
  status: unavailable
  required: false
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - wiki-context
  - taxonomy
  summary: Q22285749 page unavailable through the web tool; taxon35619 independently
    verifies at NCBI. Applies to the aborycin-2 occurrence, consulted as sibling context
    for aborycin.
- check_id: mibig-latest
  name: Independent current-alias status check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - mibig
  - access
  summary: Exact versioned entries are active in their inspected JSON. Unversioned
    annotations endpoints returned404 and repository pages were inaccessible; current-alias
    resolution or absence of later versions is not independently proven. Do not infer
    retirement from this result.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/amino_acids_and_peptides/aborycin.yaml
  locator: Complete raw YAML, all history entries and read_natural_product resolved
    view
  accessed_at: '2026-10-13T13:14:39.477327Z'
  support: supports
  summary: Exactly one minted, SEEDED owner; no graph refs or inline graphs. Full
    contents were read before judgement. Both stored histories are unchanged seeding
    events, not scientific sign-off. The same-label sibling is context only.
  snapshot_sha256: 3c4ab2b40bf6f3a8aefd4015148319333a8b6893091f31ae47f725d005e950cb
- evidence_id: inventories
  kind: database
  reference: data/raw/mibig_compounds.tsv
  locator: BGC0002015:1 at TSV2301; BGC0002285:1 at TSV2762; exact-key LOTUS and classifier
    rows
  accessed_at: '2026-10-13T13:14:39.477966Z'
  support: supports
  summary: Both owners reproduce their distinct imported chemical keys. LOTUS joins
    by exact key; no exact-key ChEBI or AntibioticMech row was found in the complete
    pinned TSV scans. NPClassifier2026-09-07 reports Amino acids and Peptides/Oligopeptides/Cyclic
    peptides for both. This is filing provenance, not an experimental classification
    or live universal ChEBI absence claim.
  snapshot_sha256: 9516340f936ca7ec7d0dbbf81707c8a39ca9823ce0ecd0a72bbc8ab1e64dc194
  search_scope: Complete csv.DictReader scans of six pinned TSVs; no gitignore filtering.
    Repository identifier/name search also included hidden and ignored files, excluding
    only .git object data and .venv runtime packages.
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-aborycin-review-JJKFYR/chemistry.json
  locator: RDKit2026.03.5 owner roundtrip, functional-group matches, stereo removal
    and deposited-core topology reconstruction
  accessed_at: '2026-10-13T13:14:39.478169Z'
  support: supports
  summary: Both SMILES reproduce stored InChI/keys, neutral C97H131N23O26S4 and exact
    mass2161.851845312 Da. AJFZ has18 unspecified centers,22 amide carbonyls,one acid
    and no free amino-Cys/anhydride. FHQR has17 specified/one unspecified center,21
    amide carbonyls,one free amino-Cys and one anhydride,no acid. Both contain two
    disulfides. The deposited21-residue core with the1994 abstract bond pattern reconstructs
    AJFZ after removing stereo, not FHQR; this does not establish lasso threading
    or absolute configuration.
  snapshot_sha256: 15fe59ed29ea3453de0565f2e434ed42070205d832fa15ef4450354f6d2de14f
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002015.4/annotations.json
  locator: Exact entry version/status, compound structure/xref, taxonomy, locus accession/bounds/method
    and cited reference
  accessed_at: '2026-10-13T12:55:47.082318Z'
  support: supports
  summary: Active BGC0002015v4 asserts NZ_MKCP01000039.1:18549..30566, taxon1904044,
    no locus method, FHQR chemistry and PubChem136150874. PMID30795576 is the legacy
    reference. Source agreement does not establish correct chemistry.
  snapshot_sha256: 43ff2b671e7af2d2654821784c18deaf3775121ba64de6113f31bff828328b30
- evidence_id: xref
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/136150874/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES,IsomericSMILES/JSON
  locator: Exact SMILES, InChIKey, formula and cited isolation source where provided
  accessed_at: '2026-10-13T12:56:00.708311Z'
  support: supports
  summary: PubChem136150874 exactly matches FHQR and the stored SMILES/InChI. This
    is a correct database xref for the encoded graph, not independent proof that the
    graph represents the natural product. Removing only the xref would not repair
    the identity defect.
  snapshot_sha256: 9895e4c530c7713c57f20ae9231c120cf0c241fcdde86da389f62ccf63cecdc3
- evidence_id: paper1994
  kind: primary_source
  reference: DOI:10.1002/jlac.199419940716
  locator: Publisher-deposited abstract in Crossref message.abstract; title/year/DOI
  accessed_at: '2026-10-13T12:56:53.979320Z'
  support: partial
  summary: The abstract reports isolation from S.griseoflavus TU4072, purification
    and structural analysis of a21-residue peptide. It explicitly assigns Asp9-side-chain
    to Cys1-N-terminal closure and Cys1-Cys13/Cys7-Cys19 disulfides. Full spectra,
    stereochemical assignments and figure were not inspected.
  snapshot_sha256: fb345f6a1934467a5286e224175b4cb2b9cbfc139f873efc5e9540921271fb41
- evidence_id: paper2019
  kind: primary_source
  reference: PMID:30795576
  locator: EuropePMC resultList.result[0].abstractText and PMID/DOI/PMCID aliases
  accessed_at: '2026-10-13T12:56:27.930031Z'
  support: partial
  summary: The abstract reports aborycin isolation from SCSIO ZS0098 and production
    after heterologous expression in S.coelicolor M1152. It describes a ribosomal
    type I lasso peptide. This supports the named compound/organism context, not either
    exact imported contig or the FHQR bond graph; experimental methods remain uninspected.
  snapshot_sha256: 0579f3c31ae4b26aad315145df968796a40860fbcdc31bd2644da2513659190c
- evidence_id: sequence-source
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=MKCP01000045.1,NZ_MKCP01000039.1&rettype=gbwithparts&retmode=xml
  locator: GBSeq records, source features, exact accession versions, complete sequence
    and CDS feature tables
  accessed_at: '2026-10-13T13:00:55.741999Z'
  support: supports
  summary: MKCP01000045.1 is816609bp contig5; NZ_MKCP01000039.1 is120871bp contig44
    with a CONTIG link to MKCP01000039.1. Both source features specify ZS0098 and
    taxon1904044. The latter contains precursor22746..22874 and cyclase22936..24747
    plus B1/B2 annotations. These annotations explicitly derive from computational
    PGAP methods, not new biochemical experiments.
  snapshot_sha256: 512c66a8d3fc9f3d8881cc8d76dfd7c7ff58e3e29c8971f1869bd30399962f9d
- evidence_id: sequence-audit
  kind: validation
  reference: /private/tmp/npmech-aborycin-review-JJKFYR/sequence-audit.json
  locator: Complete structured feature scan of each claimed interval; exact129nt precursor
    query on both full contigs/both strands
  accessed_at: '2026-10-13T13:14:39.491709Z'
  support: supports
  summary: The MKCP01000045.1 interval contains oxidoreductase, proline-racemase,
    sugar/sulfate transport and regulator annotations. The exact129nt precursor from
    contig39 occurs once on contig39 and not on either strand of contig45. Bounds18549..30566
    and extended34000 fit annotated genes on contig39. This is a substantial accession-context
    conflict, not proof that all divergent/unannotated lasso genes are absent.
  snapshot_sha256: 6bcc1cf1c969e83ae8e898387256705ae321fa3a1358b48f97a56161fb5f6047
  search_scope: Full fetched contigs, both strands, exact nucleotide query only; all
    overlapping CDS features in the claimed intervals. No alignment, gene prediction
    or global genome-wide absence claim.
- evidence_id: taxonomy
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1904044,1883,35619&retmode=xml
  locator: TaxIds1904044,1883,35619; corresponding pinned corpus_taxa.obo terms
  accessed_at: '2026-10-13T12:57:58.154576Z'
  support: supports
  summary: 'Live NCBI and the pinned labels agree: Streptomyces sp. ZS0098(species
    rank), Streptomyces(genus), S.griseoflavus(species). Both sequence source features
    retain ZS0098. ACTINOBACTERIAL is consistent with the lineage; genus occurrence
    does not imply every member produces the compound.'
  snapshot_sha256: 37572b116d8dd8c4e3ff8dc191d0f71e4dc1ce57fa13d987812536b3221c8b43
- evidence_id: wiki-context
  kind: database
  reference: https://www.wikidata.org/wiki/Q1144013
  locator: Organism label and rank; Q22285749 retrieval limitation
  accessed_at: '2026-10-13T13:14:39.492263Z'
  support: partial
  summary: Q1144013 resolves to genus Streptomyces. Q22285749 could not be independently
    inspected after two web-tool failures; its S.griseoflavus association is retained
    only as committed LOTUS provenance, with the NCBI species verified separately.
- evidence_id: governance
  kind: record_content
  reference: docs/CURATION.md
  locator: Identity/sign-off, narrow curation inputs and generated boundaries; docs/HARMONIZATION.md
    producer/locus separation; conf/producer_evidence.tsv
  accessed_at: '2026-10-13T13:14:39.492277Z'
  support: supports
  summary: SOURCE_ASSERTION is a database producer tier; heterologous expression grades
    only the locus. Method absence stays CLUSTER_UNSTATED. The structure correction
    consumer supports only an unoccupied3-star ChEBI target, not arbitrary replacement
    or merger into the existing AJFZ owner. decisions.tsv is reserved and not consumed.
    No correction, merge or status promotion was performed.
- evidence_id: access
  kind: validation
  reference: /private/tmp/npmech-aborycin-review-JJKFYR/access-limitations.json
  locator: Actual web-tool rate limit, failed DOI resolution and denied alternate
    publisher command
  accessed_at: '2026-10-13T13:14:39.492303Z'
  support: context_only
  summary: 2019 full text returned429. The1994 DOI did not yield source text and auto-review
    denied the subsequent publisher request before execution. No alternate full-text
    retrieval followed. Abstracts were inspected independently. All180 inherited stops
    remain; these two primary-source limits and the unresolved Wikidata check are
    explicit.
  snapshot_sha256: 8c568e24a2049cddcf617d3b272fc3e1b01aff5f35174c692daf57c02e914aa7
assessments:
- assessment_id: identity
  area: identity
  topic: Exact bond connectivity and supported stereochemical resolution
  outcome: concern
  summary: FHQR reproduces the upstream MIBiG/PubChem graph but leaves Cys1 amino
    free and uses an anhydride linkage instead of the reported N-terminal macrolactam.
    The graph conflicts with aborycin identity independently of the incomplete stereo
    flag. The issue is not cured by matching the formula or PubChem.
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - owner
  - chemistry
  - paper1994
  - sequence-source
  - xref
  - mibig
  dimensions:
  - name: exact-key
    value: FHQRLPHOFHPTCX-BDHXJCCSSA-N
    definition: Current owner chemical key, not a proposed replacement
    evidence_ids:
    - owner
    - chemistry
  - name: stereochemistry
    value: 17 specified and1 unspecified center
    definition: RDKit interpretation of encoded structure; experimental assignment
      not fully assessed
    evidence_ids:
    - chemistry
- assessment_id: xref
  area: grounding
  topic: Exact external equivalence and minted grounding
  outcome: supported
  summary: The stored xref exactly matches the stored chemical graph. No exact-key3-star
    ChEBI row occurs in the pinned inventory. Database identity agreement does not
    settle whether the label is scientifically correct; no arbitrary grounding or
    merger was made.
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - inventories
  - xref
  - chemistry
  - governance
- assessment_id: classification
  area: provenance
  topic: Computed filing, asserted BGC class and taxon facets
  outcome: supported
  summary: The pinned classifier and RIBOSOMAL source assertion are separated. Taxon
    identifiers and labels agree with current NCBI and pinned names; ACTINOBACTERIAL
    is consistent. No computed class or taxonomic facet was used to prove origin.
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - inventories
  - mibig
  - taxonomy
  - governance
- assessment_id: producer
  area: evidence
  topic: Native producer versus heterologous experimental host
  outcome: concern
  summary: The named producer is supported for biological aborycin at abstract level,
    but that evidence cannot establish production of the wrong FHQR graph. SOURCE_ASSERTION
    is correctly attributed as a database assertion, yet the exact-structure origin
    remains blocked by F1.
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - owner
  - paper2019
  - taxonomy
  - sequence-source
  - governance
  dimensions:
  - name: strain-context
    value: native:SCSIO ZS0098; heterologous:S.coelicolor M1152
    definition: Distinct contexts from primary abstract; only native database taxon
      claim is stored
    evidence_ids:
    - paper2019
  - name: stored-evidence-tier
    value: SOURCE_ASSERTION;CLUSTER_UNSTATED
    definition: Stored producer and locus grades, not new upgrades
    evidence_ids:
    - owner
    - mibig
- assessment_id: bgc
  area: evidence
  topic: Exact versioned cluster and genomic interval
  outcome: supported
  summary: The active entry/version and coordinates match the source, and contig39
    contains the expected precursor/cyclase context within the interval. CLUSTER_UNSTATED
    honestly reports no method in this entry; the2019 abstract offers an upgrade lead
    only after exact experiment and identity adjudication. Genomic context does not
    repair F1.
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - mibig
  - sequence-source
  - sequence-audit
  - paper2019
  - governance
- assessment_id: occurrence
  area: evidence
  topic: LOTUS exact-key occurrence and taxonomic scope
  outcome: concern
  summary: The LOTUS genus occurrence cites the same2019 study as the MIBiG producer,
    not independent corroboration. The abstract supports biological aborycin, not
    the conflicting FHQR graph. F1 therefore also blocks the exact-key occurrence
    interpretation.
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - inventories
  - paper2019
  - paper1994
  - taxonomy
  - wiki-context
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Optional assays, pathways, targets, graphs and history
  outcome: unknown
  summary: Complete owners and histories have no stored graphs/components, pathway
    steps, protein examples, assays, targets, clinical assertions or sibling joins.
    These optional omissions are not false claims. Literature offers bounded mechanism/assay
    leads, but full methods and exact compound-form support must precede additions.
    No evidence/status/history mutation occurred.
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - owner
  - inventories
  - paper2019
  - governance
- assessment_id: validation
  area: schema
  topic: Native deterministic checks and provenance
  outcome: supported
  summary: Strict target validation, configured label gate and full native QC pass.
    All3115 owner hashes,243 components and21 pre-existing review pairs were verified
    against the prior merged checkpoint. This does not scientifically review their
    content or close earlier findings.
  target_ids:
  - naturalproductmech:mibig-90494a0512
  evidence_ids:
  - owner
  - inventories
  - governance
findings:
- finding_id: F1
  issue_key: aborycin-BGC0002015-anhydride-wrong-connectivity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Encoded anhydride graph is not the reported aborycin macrolactam
  description: FHQRLPHOFHPTCX-BDHXJCCSSA-N contains an anhydride and free amino-Cys
    instead of the Cys1-N to Asp9-side-chain amide explicitly described by the original
    isolation abstract. The current PubChem and MIBiG entries reproduce this same
    defect. Removing stereochemistry does not make it AJFZ; deposited-core reconstruction
    with the reported bonds yields AJFZ. The formula and database xref match are insufficient
    to carry aborycin production/occurrence claims onto this different graph.
  target_ids:
  - naturalproductmech:mibig-90494a0512
  field_paths:
  - label
  - chemical_structure
  - biosynthesis_origin
  - producer_organisms
  - occurrences
  - biosynthetic_gene_clusters
  evidence_ids:
  - owner
  - chemistry
  - paper1994
  - xref
  - mibig
  - sequence-source
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned imported compound/locus assertions; preserve original bytes
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Pinned occurrence rows keyed to the represented chemical form
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained harmonization and generated owner emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Only REPLACE_WITH_CHEBI is implemented; occupied targets are rejected
  rule_id: review-checklist:Identity; Structure; docs/HARMONIZATION.md:The unit of
    the corpus is a structure
  native_severity: blocker
  normalization_reason: Wrong connectivity makes the record denote a different molecule
    and invalidates exact-structure origin attribution, matching the shared blocker
    definition.
actions:
- action_id: A1
  description: Adjudicate the source chemistry and repair or quarantine the BGC0002015:1
    identity through a maintained, tested source-pinned path. Resolve its relationship
    to the occupied AJFZ sibling explicitly. The current REPLACE_WITH_CHEBI consumer
    cannot replace with an arbitrary graph or merge occupied owners; reserved decisions.tsv
    does nothing. Do not simply drop the exact-to-current-graph PubChem xref or hand-edit
    generated YAML.
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-90494a0512
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned imported compound/locus assertions; preserve original bytes
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Pinned occurrence rows keyed to the represented chemical form
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained harmonization and generated owner emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Only REPLACE_WITH_CHEBI is implemented; occupied targets are rejected
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Confirm primary bond pattern, isolate stereochemical resolution and intended source
    compound; preserve uncertainty rather than invent stereocenters.
  - Demonstrate absence of the spurious anhydride/free N-terminal amino group in any
    corrected aborycin structure; recompute SMILES/InChI/key.
  - Explicitly adjudicate existing-owner collision, identifiers/PATHS, both source
    concepts and each exact-key occurrence/xref; transfer no claims by name alone.
  - Preserve raw assertions, source-row hashes and curation attribution; test missing/duplicate/drift/conflict
    inputs.
  - Run guarded canary, strict validation, provenance, corpus/path lock, reproduction,
    generated site and full QC; preserve all unrelated owners/components.
limitations:
- This observation assesses exact committed inputs at9191a148; their current bytes
  were checked against git show. No record, raw inventory, curation decision, generated
  page or prior review was edited.
- Full primary methods, spectra, chemical figure, isolate stereochemistry and cloned-locus
  endpoints remain unverified. Neither abstract evidence nor RDKit/PGAP computation
  substitutes for those checks.
- Both primary access limits, all180 inherited stops and the unresolved Wikidata species
  note are retained. No paid research, contacts, alternate retrieval after barriers
  or GitHub mutations.
- The exact precursor search is limited to the two fetched contigs and literal nucleotide
  equality; it cannot prove absence of divergent or unannotated lasso genes.
- The repository interpreter lacked Biopython; structured NCBI XML and standard ElementTree
  were used without installing dependencies. The initial missing-sequence parse failure
  is retained and superseded by the explicit gbwithparts check.
- Single-record denominator1; the campaign denominator3115 is unchanged. Partial observations
  do not count as completed scientific reviews.
notes:
- Only new immutable review bundles are authorized; actions are proposed, not executed.
- Two separate source entries and different first InChIKey blocks do not authorize
  a merge. Here the specific bond conflict, not the hash difference alone, supports
  the identity finding.
- The final canonical saver/contract check is recorded separately after these drafts
  are validated; it is not retroactively claimed as a pre-save command.
```
