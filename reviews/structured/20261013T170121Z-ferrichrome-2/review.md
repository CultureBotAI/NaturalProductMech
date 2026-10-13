# Ferrichrome (BGC0000900.5): exact-form scientific review

- Review: 20261013T170121Z-ferrichrome-2
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T16:44:43.374066Z
- Finished UTC: 2026-10-13T17:01:21.998347Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed blocker in named chemical identity and one confirmed major nonexact PubChem link; primary occurrence verification remains unavailable.

## Scope And Provenance

One exact owner at merged504e6b184; campaign denominator remains3115 owners and243 components.

Selection: Next exact pending owner in the exhaustive identity-priority campaign, not a sample.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 504e6b18472feaa68e45b2f53293330e9a7e13bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-ab69cdf6e5 | data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml | generated | ferrichrome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| ferrichrome-2-inspect | passed | True | naturalproductmech:mibig-ab69cdf6e5 | Canonical pre-assessment inspection captured the exact merged Git revision and input hashes. |
| strict-ferrichrome-2-native | passed | True | naturalproductmech:mibig-ab69cdf6e5 | The documented native strict-validator script passed for this owner; no graph components are attached. |
| corpus | passed | True | naturalproductmech:mibig-ab69cdf6e5 | Full-corpus filesystem and PATHS.tsv audit passed for all3115 owners. |
| qc | passed | True | naturalproductmech:mibig-ab69cdf6e5 | Full native QC passed: 747 tests passed, 3 skipped and 2 dependency warnings; all-owner strict validation, history/component invariants, provenance, generated site and exact reproduction passed. This run precedes saving these two reviews; their canonical checks are run afterward. Deterministic consistency is not scientific approval. |
| labels | passed | True | naturalproductmech:mibig-ab69cdf6e5 | Configured ID-label gate passed: 13434 canonical, 646 synonym and 35 exception matches, with 499 nonblocking warning mismatches and 4649 no-adapter skips. Exact chemical identity was assessed separately. |
| chemistry-native | passed | True | naturalproductmech:mibig-ab69cdf6e5 | RDKit2026.03.5 regenerated owner InChI/key, checked stereo flags, verified source-row digests and matched the live PubChem and ChEBI graphs. |
| local-search | passed | False | naturalproductmech:mibig-ab69cdf6e5 | Ignored-inclusive identifier/name/slug search covered curation, data/raw, owner/component corpus, reviews, docs, scripts, src, conf and tests. |
| queue | passed | False | naturalproductmech:mibig-ab69cdf6e5 | Exhaustive native pending-record diagnostics regenerated to a temporary TSV; no status or tracked queue edit. |
| strict-ferrichrome-2 | failed | False | naturalproductmech:mibig-ab69cdf6e5 | Initial just wrapper failed before validation because sandboxed uv could not access its global cache; the exact native script was then run successfully. |
| chemistry | failed | False | naturalproductmech:mibig-ab69cdf6e5 | Initial chemistry helper could not import the local package from the separate pinned runtime; adding repository src to PYTHONPATH enabled the completed run. |
| Exact compound primary evidence | unavailable | True | naturalproductmech:mibig-ab69cdf6e5 | Required occurrence primary text and secondary organism identifier remain unavailable after HTTP403. |
| Structured expression-source applicability | not_applicable | False | naturalproductmech:mibig-ab69cdf6e5 | The owner names no gene/protein/regulator or transcriptomics dataset. MIBiG, taxonomy and GenBank adapters were inspected first. Contextual patent genes are not owner assertions; no iModulonDB coverage or absence claim is made. |

## Scientific And Domain Assessments

### Exact named chemical form

identity: concern. Targets: naturalproductmech:mibig-ab69cdf6e5.

Confirmed C26/N-formyl versus C27/triacetyl identity conflict; neither removing iron nor choosing the other same-label owner solves it. The exact patent product and any replacement remain unselected.

### Internal chemistry and pinned source representation

consistency: supported. Targets: naturalproductmech:mibig-ab69cdf6e5.

Stored SMILES, InChI and key roundtrip and agree with versioned MIBiG. stereo_complete correctly describes the encoded peptide centers. Formal charge and coordination depiction do not independently establish biological chemical form.

### Minted rationale and exact registry links

grounding: concern. Targets: naturalproductmech:mibig-ab69cdf6e5.

Minted status is consistent with the absence of an exact pinned ChEBI default key. CID90658043 is exact; CID644246 is nonexact and needs withholding. No parent/congener assertion is present.

### Chemical filing and asserted taxonomy facets

representation: supported. Targets: naturalproductmech:mibig-ab69cdf6e5.

NPClassifier@2026-09-07 cyclic-peptide/oligopeptide and nonglycoside output matches the pinned row and AMINO_ACIDS_AND_PEPTIDES filing. OTHER remains the database BGC class rather than a predicted enzyme class. FUNGAL producer grouping matches NCBI. OTHER_BACTERIAL correctly groups the E.coli occurrence without converting it to a producer.

### Natural versus engineered exact-product origin

scope: concern. Targets: naturalproductmech:mibig-ab69cdf6e5.

NATURAL_PRODUCT is database-derived, not classifier-derived, but exact chemical attribution inherits F1. Host engineering and enzyme expression in a patent do not by themselves establish biosynthesis of the stored complete molecule. Do not silently reclassify as engineered either.

### Producer identity, strain and evidence tier

evidence: unknown. Targets: naturalproductmech:mibig-ab69cdf6e5.

The species taxon is correct and SOURCE_ASSERTION faithfully reflects the database rather than an isolation experiment. Patent source-strain context must be reconciled only after exact product identity; do not infer species-wide experimental production or copy an expression host into native producers. The sequence source alone supplies no strain.

### Exact BGC version, locus and compound-level method

evidence: unknown. Targets: naturalproductmech:mibig-ab69cdf6e5.

Active version5 and genome accession are confirmed. Unstated source bounds/methods correctly remain omitted/CLUSTER_UNSTATED. Independent genomic and enzyme context does not establish the complete exact product or justify upgrading a whole locus. Gene coordinates in live to_add annotations were not owner-curated claims.

### Detection versus biosynthesis

scope: unknown. Targets: naturalproductmech:mibig-ab69cdf6e5.

The LOTUS triple is faithfully imported as DATABASE_ASSERTION occurrence, not production. NCBITaxon562 is correct, but the1961 experiment and Q25419 linkage remain unavailable. Neither assume the paper proves production nor declare the occurrence false from its title.

### Pure-compound assays, summaries and molecular targets

scope: supported. Targets: naturalproductmech:mibig-ab69cdf6e5.

No activity, molecular target or activity summary is asserted. The uncited MIBiG siderophore annotation was not elevated into an assay. Empty PubChem no-assay placeholders do not mean inactivity; patent enzyme assays are not bioactivity of the complete natural product.

### Pathway and complete causal/assembly mechanism

graph: not_applicable. Targets: naturalproductmech:mibig-ab69cdf6e5.

No pathway steps, protein examples, inline graphs or external components are attached. Optional absence is not a scientific defect; generic family biosynthesis must not be fabricated as this structure-specific mechanism.

### Clinical, dataset, cross-corpus and relationship claims

completeness: not_applicable. Targets: naturalproductmech:mibig-ab69cdf6e5.

No clinical status, dataset list, related_records, parent_compounds or congener_of assertions require review. The embedded BGC accession was checked separately. Exact-key sibling scans were bounded to the committed inventory, not a global absence claim.

### History, sign-off and maintained owners

provenance: supported. Targets: naturalproductmech:mibig-ab69cdf6e5.

Both events are seeding events and SEEDED is appropriate. No curator discussion resolves the new concerns. Reviews do not mutate native status or history. Future source corrections use implemented pinned tables or a separately tested transform; decisions.tsv is reserved and not consumed.

## Findings

### F1: The stored C26 N-formyl structure is not the ferrichrome named by the record

blocker / open / confirmed; issue key: mibig-BGC0000900-compound-1-ferrichrome-constitution.

The owner and versioned MIBiG source encode C26H43N9O12 with two N-acetyl hydroxamates and one N-formyl hydroxamate, without iron. Authoritative ferrichrome is a C27 iron chelate with three N-acetyl groups; its metal-free ligand is also C27 and triacetylated. This is not merely metal dissociation, isotope choice or unspecified stereochemistry. PubChem90658043 agrees with the imported graph, but agreement among database depictions does not establish the named natural-product identity. The conflict affects exact product attribution; it does not prove this C26 molecule cannot exist or select the patent product/replacement automatically.

### F2: PubChem644246 is a nonexact chemical cross-reference

major / open / confirmed; issue key: mibig-BGC0000900-compound-1-pubchem-644246-nonexact.

The live PubChem response resolves CID644246 to GGUNGDGGXMHBMJ-HCMAANCNSA-N, C27H42FeN9O12 with explicit 55Fe and three undefined centers, not this C26 iron-free key. CID90658043 is exact for the stored graph. The nonexact CID is inherited from the complete BGC0000900:1 row; it needs its own disposition even if the larger identity conflict remains unresolved. No current owner assay is falsely attributed: the pinned assay rows are empty placeholders, not measurements.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the exact chemical form before any structure migration. First add a cited curator-owned conflict/qualification through the validated writer. Only use REPLACE_WITH_CHEBI after a unique experimental target, destination ownership, source row and target row are independently established; otherwise retain the explicit unresolved conflict. Never transfer old-key occurrences, assays or graphs automatically.

- Inspect primary exact product/isotope/stereo evidence; distinguish named compound from family and native from engineered context.
- Recompute InChI/key with pinned RDKit, audit source joins and all old-key claims, and inspect guarded one-record canary.
- Run just validate-strict, just verify-reproduction, just verify-corpus, just validate-products and just qc; preserve history and component ownership.

### A2

For the current unchanged structure, withhold literal pubchem:644246 through the implemented complete-row-pinned xref exclusion for BGC0000900:1. Preserve exact pubchem:90658043 and raw provenance. If A1 instead changes structure, adjudicate xrefs with that migration; concurrent structure replacement and xref exclusion are intentionally incompatible.

- Pin complete source row SHA25678b115cce5a8a133196da68d8dd417a75f5a8f42aa0344a1d3c76d389e58f791 and cite the live PubChem identity evidence.
- Generated xrefs omit644246 but retain90658043 for the unchanged owner; source-conflict provenance remains visible.
- Test source-row drift, duplicate decisions and incompatible corrections; run strict validation, reproduction and full QC.

### A3

Complete unavailable primary checks through authorized access or user-provided source text, and reconcile source-strain context after identity adjudication. Preserve species identifiers and conservative producer/locus grades until exact evidence justifies a change.

- Inspect the complete cited study and exact product/strain/experimental context; preserve each403 limitation until resolved.
- Do not reuse family-level claims, isotope tracers, or expression-host enzyme activity as native complete-product proof.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml; Entire raw YAML including both history entries | supports | One exact MINTED/SEEDED owner, not a label-level compound class. No curator discussion, pathway, activity, target, clinical, dataset, parent/congener, cross-corpus or graph assertion is present. |
| resolved | /private/tmp/npmech-ferrichrome-resume-mXOYL5/ferrichrome-2-resolved.json; Complete native read_natural_product result | supports | Resolved full mechanism agrees with the raw owner and has no inline graphs or component references. |
| inventories | /private/tmp/npmech-ferrichrome-review-W2MXlZ/source-rows.json; BGC0000900:1 version5; complete parsed TSV rows with row_digest and line numbers | supports | MIBiG line983 and NPClassifier line3113; one LOTUS occurrence line10224 and two no-assay placeholders lines11457-11458. No exact-key pinned ChEBI default or AntibioticMech join. Fresh chemistry helper reverified all selected rows against unchanged inventories. |
| chemistry | /private/tmp/npmech-ferrichrome-resume-mXOYL5/chemistry.json; RDKit2026.03.5 result ferrichrome-2 and authority comparisons | supports | Computed C26H43N9O12, net charge 0, monoisotopic mass 673.303117816 Da; 3 specified/0 undefined tetrahedral centers; acetyl/formyl hydroxamates 2/1; iron isotope list []. Exact owner InChI/key roundtrip passed. Calculations are not measurements. Normalization is diagnostic, not authorized identity replacement. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0000900.5/annotations.json; compounds[0], taxonomy, loci, biosynthesis classes and legacy references; HTTP200 capture 2026-10-13T15:36:52.703897Z..2026-10-13T15:36:54.661079Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/BGC0000900.5.json; receipt SHA256 f2c3eee2344b4c89e4a93229867b284f06e697a9e9fd55d0e7c900f57df8e357 | supports | Exact active version5 chemistry, host and references match the raw row. Empty locus methods and 0..0 unspecified bounds are not experiments or real coordinates. OTHER is source asserted; questionable quality and placeholder reviewers are not scientific truth signals. No assertion this is the latest version. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/90658043,644246/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; PropertyTable.Properties for CID90658043 and CID644246; HTTP200 capture 2026-10-13T16:45:00.740185Z..2026-10-13T16:45:01.117565Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/pubchem-resume.json; receipt SHA256 b21e89ec88fb8064682ed966bdcddcbf7970d431e58f8fa33026a716cac9749b | refutes | Recovered HTTP200: CID90658043 matches ZZDYFKJSJLUQON-UFYCRDLUSA-N; CID644246 matches GGUNGDGGXMHBMJ-HCMAANCNSA-N. Both formulae and exact InChIs were recomputed. Registry equivalence is not evidence for biosynthesis. |
| chebi-ferrichrome | https://www.ebi.ac.uk/chebi/backend/api/public/compound/5019/; CHEBI5019 default_structure, chemical_data, stars and definition; HTTP200 capture 2026-10-13T16:45:34.903592Z..2026-10-13T16:45:35.832294Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/CHEBI5019-resume.json; receipt SHA256 bf6c76369978dbde977d07416b9e6451269b02318a10419e24b3d807aaa704c0 | refutes | Live 3-star ferrichrome agrees with the pinned default graph: GGUNGDGGXMHBMJ-OCIDDWSYSA-N, C27H42FeN9O12, three specified peptide centers, no isotope label. Its three N-acetyl groups distinguish it from the C26 record. Representation of coordination is not interpreted as physical negative iron oxidation state. |
| chebi-deferrichrome | https://www.ebi.ac.uk/chebi/backend/api/public/compound/90132/; CHEBI90132 default_structure, chemical_data, stars and definition; HTTP200 capture 2026-10-13T16:45:56.396094Z..2026-10-13T16:45:57.051939Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/CHEBI90132-resume.json; receipt SHA256 a3cd2f780cd4c2d44ccd4d8d9332479ef56bc91c2cdd23be6fd177743bb1cf19 | refutes | Live 3-star deferrichrome agrees with pinned ZFDAUYPBCXMSBF-ACRUOGEOSA-N, C27H45N9O12, three acetyl hydroxamates and no iron. It is not the C26 form. Occurrences and roles on this nonexact candidate are not transferred. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=5062,5061,562&amp;retmode=xml; Direct Taxon nodes5062,5061,562; HTTP200 capture 2026-10-13T15:38:57.471335Z..2026-10-13T15:38:58.268464Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/taxonomy.xml; receipt SHA256 3c5b41d8d87e3eb2e3ac86b1540dbf25328f458390c64c51c78268918b86a020 | supports | NCBI resolves Aspergillus oryzae5062 and Aspergillus niger5061 at species rank with fungal lineage, and Escherichia coli562 at species rank in Bacteria. Taxonomy does not establish production or a strain. |
| genome | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=BD306272.1,DJ389528.1&amp;rettype=gbwithparts&amp;retmode=xml; Exact accession-version, definition, source feature and references; HTTP200 capture 2026-10-13T15:39:42.133857Z..2026-10-13T15:39:42.621788Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/sequences.xml; receipt SHA256 30d35df4b5eb9ed3fe53fbae6e845689bc3e46d5dac3013aaa109ce54eff13d2 | supports | BD306272.1 is9052nt from A.oryzae5062 and cites JP2003125779-A sequence10; DJ389528.1 is23114nt from A.niger5061 and cites JP2003230381-A sequence2. Neither source feature supplies a strain. Whole-sequence lengths do not specify cluster bounds. |
| scope-proof | /private/tmp/npmech-ferrichrome-resume-mXOYL5/capture.json; Ignored-inclusive owner/component enumeration and prior-review hashes | supports | All3115 owners,243 components and30 predecessor review pairs match the prior merged checkpoint. Every new inspected input matches Git504e6b184. Only context change since interrupted research is the unrelated BGC0002321:4 strain row, whose diff was read. |
| search | /private/tmp/npmech-ferrichrome-resume-mXOYL5/local-search.log; rg ignored-inclusive bounded search | supports | Search found source inventories and exact owners but no applicable existing ferrichrome curation-table decision or prior canonical review. Complete owner parsing supports optional-field absence only within these exact files. |
| qc-evidence | /private/tmp/npmech-ferrichrome-resume-mXOYL5/qc.log; Full actual native QC log | supports | Read-only consistency gates; results do not promote SEEDED status. |
| labels-evidence | /private/tmp/npmech-ferrichrome-resume-mXOYL5/labels.log; Configured full-corpus label check | supports | Warnings and no-adapter skips retained; NCBITaxon names/ranks independently verified. |
| queue-evidence | /private/tmp/npmech-ferrichrome-resume-mXOYL5/queue.tsv; Exhaustive pending-record queue | supports | All3115 owners remain in the native pending population; scientific review coverage is separately recorded. |
| patent | https://patents.google.com/patent/JP2003125779A/en; JP2003125779A description0004,0015-0025,0027-0051; prose, not visual sequence figures; HTTP200 capture 2026-10-13T15:38:47.295850Z..2026-10-13T15:38:47.924509Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/patent.html; receipt SHA256 14b7bf9f5d25f505db153aef26ea20d5fb83096391b4d8693208a877b8f0992c | partial | The patent discusses a ferrichrome family/member rather than proving this C26 structure. It names O-1013 genomic material and a distinct1013-niaD example host; asb3 expression in E.coli tests acetylation, not whole-product biosynthesis. Japanese member spelling is not automatically equated with ferricrocin. Machine translation is imperfect. |
| occurrence-metadata | https://api.crossref.org/works/10.1021/ja01468a020; Crossref DOI, title, authors and print date; HTTP200 capture 2026-10-13T15:37:06.389836Z..2026-10-13T15:37:06.717560Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/occurrence-crossref.json; receipt SHA256 07eef161388a13863ec3b30ad43f427ba4bf76616bed9d60470cf39b289dd39b | partial | DOI10.1021/ja01468a020 resolves to Emery/Neilands, Structure of the Ferrichrome Compounds, JACS83:1626-1628,1961. The2002 online date is not a new experiment. Metadata contains no inspected experimental occurrence evidence. |
| occurrence-access | https://doi.org/10.1021/ja01468a020; Error response only; HTTP403 capture 2026-10-13T15:38:53.604610Z..2026-10-13T15:38:54.001755Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/occurrence.html; receipt SHA256 a9c32e8c5ffea6d102a22b8ee51d379218d4fad16774522d7845146471789df3 | unknown | HTTP403; primary content/identifier response not inspected. No alternate route attempted. |
| wikidata-access | https://www.wikidata.org/wiki/Special:EntityData/Q25419.json; Error response only; HTTP403 capture 2026-10-13T15:45:20.406431Z..2026-10-13T15:45:20.473573Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/wikidata-Q25419.json; receipt SHA256 8ba01772d3ffaa63bbd8433543bb97afeed2f03d8f46f2bc4719bfce265924cb | unknown | HTTP403; primary content/identifier response not inspected. No alternate route attempted. |

## Limits And Additional Notes

- Required primary material is unavailable; partial coverage is not a whole-record scientific pass or eligibility for REVIEWED.
- Prior research captures are preserved with original retrieval times; fresh merged-state inspection and computation revalidated unchanged inputs. The unrelated strain-table addition was separately read.
- Earlier PubChem503 and ChEBI504 events remain in the historical202-access-limitation ledger. One new-turn retry recovered both PubChem IDs and both ChEBI authorities; these four identities are no longer currently unavailable. No403 endpoint was retried via an alternate path.
- Patent prose and tabular text were inspected; DNA/protein sequence images and original Japanese legal document facsimiles were not visually audited. Machine translation can misname organisms, enzymes and ferrichrome-family members.
- Optional absent fields are not counted as deficiencies. No full-corpus scientific conclusion follows from native consistency tests.
- The initial uv wrapper and isolated-runtime import failures are retained as execution history; their native-script retries passed.
- Temporary evidence paths are session-local; stable source URLs, source-row digests, exact Git inputs and payload hashes are included. No scientific record, status, history, raw inventory, generated page or GitHub object was changed.
- Full objective remains review of every3115 owner and its attached components; unassessed and partial work is not redefined as complete.
- Original interrupted research began2026-10-13T15:35:47.926332Z. This review uses actual resumed assessment timestamps, not a backdated filename.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T170121Z-ferrichrome-2
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Ferrichrome (BGC0000900.5): exact-form scientific review'
started_at: '2026-10-13T16:44:43.374066Z'
finished_at: '2026-10-13T17:01:21.998347Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant/thread as corpus research and prior curation;
    not independent human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One confirmed blocker in named chemical identity and one confirmed major
  nonexact PubChem link; primary occurrence verification remains unavailable.
source:
  git_revision: 504e6b18472feaa68e45b2f53293330e9a7e13bf
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
    sha256: 20bad44941e6634deadcb4afc20445db5f439fe1b5cd6ebf57306bb3c031a115
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: 21f15282d9684d75bd9146dd08087d257500ff1c0f4307d4612db8f95450c63f
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml
    sha256: cdd8f39d64885874c67a5c95d489905e6bfed47dd86ddbaf0761bd301f87b38d
    role: target
  - path: data/natural_products/amino_acids_and_peptides/ferrichrome.yaml
    sha256: b053166dcd2036c20d09228063544916b77c0ab7053bd3f3c2e73cccbcafea11
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
  - path: uv.lock
    sha256: c62a5739e3ffeb12cc57b3bf12a31dcf9cdfbf00b417f4ba3a801d51ef9efbe3
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
  description: One exact owner at merged504e6b184; campaign denominator remains3115
    owners and243 components.
  selection: Next exact pending owner in the exhaustive identity-priority campaign,
    not a sample.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  exclusions:
  - target: Other3114 owners
    reason: Outside this immutable single-record observation; retained in the campaign
      checkpoint.
checks:
- check_id: ferrichrome-2-inspect
  name: ferrichrome-2-inspect
  status: passed
  required: true
  command: .venv/bin/python scripts/record_review.py inspect --targets /private/tmp/npmech-ferrichrome-resume-mXOYL5/ferrichrome-2-targets.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/review-yaml-record/SKILL.md --input CLAUDE.md --input conf/id_label_targets.yaml
    --input conf/producer_evidence.tsv --input conf/record_review.yaml --input curation/decisions.tsv
    --input curation/mibig_locus_evidence_overrides.tsv --input curation/mibig_producer_strains.tsv
    --input curation/mibig_structure_corrections.tsv --input curation/mibig_xref_exclusions.tsv
    --input data/natural_products/PATHS.tsv --input data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml
    --input data/natural_products/amino_acids_and_peptides/ferrichrome.yaml --input
    data/raw/MANIFEST.yaml --input data/raw/antibioticmech_inchikeys.tsv --input data/raw/chebi_origins.tsv
    --input data/raw/chebi_structures.tsv --input data/raw/corpus_taxa.obo --input
    data/raw/lotus_occurrences.tsv --input data/raw/mibig_compounds.tsv --input data/raw/npclassifier.tsv
    --input data/raw/pubchem_bioassay.tsv --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/record-review-profile.md --input docs/record-reviews.md --input justfile
    --input pyproject.toml --input schema/record_review.yaml --input scripts/extract_lotus.py
    --input scripts/extract_mibig.py --input scripts/record_review.py --input scripts/run_qc.py
    --input scripts/seed_from_sources.py --input src/naturalproductmech/curate/producer_strains.py
    --input src/naturalproductmech/curate/structure_corrections.py --input src/naturalproductmech/curate/xref_exclusions.py
    --input src/naturalproductmech/graph_components.py --input src/naturalproductmech/schema/history.yaml
    --input src/naturalproductmech/schema/mech_shared.yaml --input src/naturalproductmech/schema/naturalproductmech.yaml
    --input uv.lock
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: Canonical pre-assessment inspection captured the exact merged Git revision
    and input hashes.
  scope_note: Actual run 2026-10-13T16:44:45.039169Z..2026-10-13T16:44:48.993602Z;
    /private/tmp/npmech-ferrichrome-resume-mXOYL5/ferrichrome-2-inspect.json; SHA256
    23cc3755107cfc9e641a34e756de6b92b3faa8562edd5b9a3bb1a07d1e5561a6
- check_id: strict-ferrichrome-2-native
  name: strict-ferrichrome-2-native
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml
    --out /private/tmp/npmech-ferrichrome-resume-mXOYL5/strict-ferrichrome-2.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: The documented native strict-validator script passed for this owner; no
    graph components are attached.
  scope_note: Actual run 2026-10-13T16:45:09.292390Z..2026-10-13T16:45:12.575308Z;
    /private/tmp/npmech-ferrichrome-resume-mXOYL5/strict-ferrichrome-2-native.log;
    SHA256 fe5c8cb61760149a232c546d65c69388b9a3619badb2fdc909a2d2ad1f6b85a2
- check_id: corpus
  name: corpus
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py --summary
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: Full-corpus filesystem and PATHS.tsv audit passed for all3115 owners.
  scope_note: Actual run 2026-10-13T16:45:52.205568Z..2026-10-13T16:47:05.887104Z;
    /private/tmp/npmech-ferrichrome-resume-mXOYL5/corpus.log; SHA256 f41149d35ddb3ab65a8fe2fdf8bfd6242ff6753e740c3482f9ed0f0bb7122b50
- check_id: qc
  name: qc
  status: passed
  required: true
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: 'Full native QC passed: 747 tests passed, 3 skipped and 2 dependency warnings;
    all-owner strict validation, history/component invariants, provenance, generated
    site and exact reproduction passed. This run precedes saving these two reviews;
    their canonical checks are run afterward. Deterministic consistency is not scientific
    approval.'
  scope_note: Actual run 2026-10-13T16:46:21.483850Z..2026-10-13T17:00:27.303003Z;
    /private/tmp/npmech-ferrichrome-resume-mXOYL5/qc.log; SHA256 0715e841e01e87c16ccdaf2df40b501ae40ed1d33a0a66e027597fabc4367407
- check_id: labels
  name: labels
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: 'Configured ID-label gate passed: 13434 canonical, 646 synonym and 35 exception
    matches, with 499 nonblocking warning mismatches and 4649 no-adapter skips. Exact
    chemical identity was assessed separately.'
  scope_note: Actual run 2026-10-13T16:47:48.856401Z..2026-10-13T16:49:51.405963Z;
    /private/tmp/npmech-ferrichrome-resume-mXOYL5/labels.log; SHA256 556ef5804e095767472c0aa8a542d5bff7e332470383a992e6b260103034414b
- check_id: chemistry-native
  name: chemistry-native
  status: passed
  required: true
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/src:/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-ferrichrome-resume-mXOYL5/chemistry.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: RDKit2026.03.5 regenerated owner InChI/key, checked stereo flags, verified
    source-row digests and matched the live PubChem and ChEBI graphs.
  scope_note: Actual run 2026-10-13T16:47:58.515601Z..2026-10-13T16:48:02.371441Z;
    /private/tmp/npmech-ferrichrome-resume-mXOYL5/chemistry-native.log; SHA256 341d6db0ba4fae5f05f61434075e8cbdc9e9f92a68b6cc2e990724056ad81a04
- check_id: local-search
  name: local-search
  status: passed
  required: false
  command: rg --no-ignore --hidden -l 'ZZDYFKJSJLUQON|GGUNGDGGXMHBMJ|BGC0000900|BGC0000901|mibig-ab69cdf6e5|mibig-91bcef2bc6|ferrichrome'
    curation data/raw data/natural_products data/causal_graphs reviews docs scripts
    src conf tests
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: Ignored-inclusive identifier/name/slug search covered curation, data/raw,
    owner/component corpus, reviews, docs, scripts, src, conf and tests.
  scope_note: Actual run 2026-10-13T16:46:00.605026Z..2026-10-13T16:46:00.701802Z;
    /private/tmp/npmech-ferrichrome-resume-mXOYL5/local-search.log; SHA256 4dfd86adef065096ed66fbbdc0cc86b50a035508afcb480171488fb34a7707b7
- check_id: queue
  name: queue
  status: passed
  required: false
  command: .venv/bin/python scripts/curation_worklist.py --review-records --limit
    0 --tsv /private/tmp/npmech-ferrichrome-resume-mXOYL5/queue.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: Exhaustive native pending-record diagnostics regenerated to a temporary
    TSV; no status or tracked queue edit.
  scope_note: Actual run 2026-10-13T16:48:13.966613Z..2026-10-13T16:48:59.929320Z;
    /private/tmp/npmech-ferrichrome-resume-mXOYL5/queue.log; SHA256 9d15004f45ba0fd5d62fe0c7e6187b91d000bb7848184d04475442a1a7557afd
- check_id: strict-ferrichrome-2
  name: strict-ferrichrome-2
  status: failed
  required: false
  command: just validate-strict data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml
    --out /private/tmp/npmech-ferrichrome-resume-mXOYL5/strict-ferrichrome-2.tsv
  exit_code: 2
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: Initial just wrapper failed before validation because sandboxed uv could
    not access its global cache; the exact native script was then run successfully.
  scope_note: Actual run 2026-10-13T16:45:01.260643Z..2026-10-13T16:45:01.332071Z;
    /private/tmp/npmech-ferrichrome-resume-mXOYL5/strict-ferrichrome-2.log; SHA256
    7cea79a6718778043c9f4f3ca465b9588cd0a5d2494525266620a2dbd097489e
- check_id: chemistry
  name: chemistry
  status: failed
  required: false
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-ferrichrome-resume-mXOYL5/chemistry.py
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: Initial chemistry helper could not import the local package from the separate
    pinned runtime; adding repository src to PYTHONPATH enabled the completed run.
  scope_note: Actual run 2026-10-13T16:47:22.490332Z..2026-10-13T16:47:25.606782Z;
    /private/tmp/npmech-ferrichrome-resume-mXOYL5/chemistry.log; SHA256 ebedd0769af224b5cab8b965a413dca4caf4d2526b60ef660736b90d0d955fdc
- check_id: primary-claims
  name: Exact compound primary evidence
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - occurrence-access
  - wikidata-access
  summary: Required occurrence primary text and secondary organism identifier remain
    unavailable after HTTP403.
- check_id: imodulondb
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  summary: The owner names no gene/protein/regulator or transcriptomics dataset. MIBiG,
    taxonomy and GenBank adapters were inspected first. Contextual patent genes are
    not owner assertions; no iModulonDB coverage or absence claim is made.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml
  locator: Entire raw YAML including both history entries
  accessed_at: '2026-10-13T17:01:21.988184Z'
  support: supports
  summary: One exact MINTED/SEEDED owner, not a label-level compound class. No curator
    discussion, pathway, activity, target, clinical, dataset, parent/congener, cross-corpus
    or graph assertion is present.
  snapshot_sha256: cdd8f39d64885874c67a5c95d489905e6bfed47dd86ddbaf0761bd301f87b38d
- evidence_id: resolved
  kind: record_content
  reference: /private/tmp/npmech-ferrichrome-resume-mXOYL5/ferrichrome-2-resolved.json
  locator: Complete native read_natural_product result
  accessed_at: '2026-10-13T17:01:21.988513Z'
  support: supports
  summary: Resolved full mechanism agrees with the raw owner and has no inline graphs
    or component references.
  snapshot_sha256: 1c0eb18aa63180f8c37579725bb16eb51028bf40ca647eee71f880960ca87704
- evidence_id: inventories
  kind: database
  reference: /private/tmp/npmech-ferrichrome-review-W2MXlZ/source-rows.json
  locator: BGC0000900:1 version5; complete parsed TSV rows with row_digest and line
    numbers
  accessed_at: '2026-10-13T17:01:21.988619Z'
  support: supports
  summary: MIBiG line983 and NPClassifier line3113; one LOTUS occurrence line10224
    and two no-assay placeholders lines11457-11458. No exact-key pinned ChEBI default
    or AntibioticMech join. Fresh chemistry helper reverified all selected rows against
    unchanged inventories.
  snapshot_sha256: 40ee7b439f5cc13f51288042fd80ab2e0d89de5859e4ff6bf73e48520fb26e68
  search_scope: Full structured scans of mibig_compounds, npclassifier, lotus_occurrences,
    chebi_structures, chebi_origins, antibioticmech_inchikeys and pubchem_bioassay;
    exact keys plus ferrichrom label context. Not global registry absence.
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-resume-mXOYL5/chemistry.json
  locator: RDKit2026.03.5 result ferrichrome-2 and authority comparisons
  accessed_at: '2026-10-13T17:01:21.988764Z'
  support: supports
  summary: Computed C26H43N9O12, net charge 0, monoisotopic mass 673.303117816 Da;
    3 specified/0 undefined tetrahedral centers; acetyl/formyl hydroxamates 2/1; iron
    isotope list []. Exact owner InChI/key roundtrip passed. Calculations are not
    measurements. Normalization is diagnostic, not authorized identity replacement.
  snapshot_sha256: dbc9e4241c6a271fa92a0dfb53f35e16a0c8d8159e6f4f8a7538a9dd435c9014
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000900.5/annotations.json
  locator: compounds[0], taxonomy, loci, biosynthesis classes and legacy references;
    HTTP200 capture 2026-10-13T15:36:52.703897Z..2026-10-13T15:36:54.661079Z; payload
    /private/tmp/npmech-ferrichrome-review-W2MXlZ/BGC0000900.5.json; receipt SHA256
    f2c3eee2344b4c89e4a93229867b284f06e697a9e9fd55d0e7c900f57df8e357
  accessed_at: '2026-10-13T17:01:21.989159Z'
  support: supports
  summary: Exact active version5 chemistry, host and references match the raw row.
    Empty locus methods and 0..0 unspecified bounds are not experiments or real coordinates.
    OTHER is source asserted; questionable quality and placeholder reviewers are not
    scientific truth signals. No assertion this is the latest version.
  snapshot_sha256: 4f198d7a4a3a2c50ca51aebd288d948e9eff7c7abd9eceead7ae5f6c24193d80
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/90658043,644246/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: PropertyTable.Properties for CID90658043 and CID644246; HTTP200 capture
    2026-10-13T16:45:00.740185Z..2026-10-13T16:45:01.117565Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/pubchem-resume.json;
    receipt SHA256 b21e89ec88fb8064682ed966bdcddcbf7970d431e58f8fa33026a716cac9749b
  accessed_at: '2026-10-13T17:01:21.989507Z'
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
    receipt SHA256 bf6c76369978dbde977d07416b9e6451269b02318a10419e24b3d807aaa704c0
  accessed_at: '2026-10-13T17:01:21.989850Z'
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
    receipt SHA256 a3cd2f780cd4c2d44ccd4d8d9332479ef56bc91c2cdd23be6fd177743bb1cf19
  accessed_at: '2026-10-13T17:01:21.990214Z'
  support: refutes
  summary: Live 3-star deferrichrome agrees with pinned ZFDAUYPBCXMSBF-ACRUOGEOSA-N,
    C27H45N9O12, three acetyl hydroxamates and no iron. It is not the C26 form. Occurrences
    and roles on this nonexact candidate are not transferred.
  snapshot_sha256: 43a98c9dc374a79365dd55e6e19bf19f36ac8a29162ee1f2065607e30289d215
- evidence_id: taxonomy
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5062,5061,562&retmode=xml
  locator: Direct Taxon nodes5062,5061,562; HTTP200 capture 2026-10-13T15:38:57.471335Z..2026-10-13T15:38:58.268464Z;
    payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/taxonomy.xml; receipt SHA256
    3c5b41d8d87e3eb2e3ac86b1540dbf25328f458390c64c51c78268918b86a020
  accessed_at: '2026-10-13T17:01:21.990730Z'
  support: supports
  summary: NCBI resolves Aspergillus oryzae5062 and Aspergillus niger5061 at species
    rank with fungal lineage, and Escherichia coli562 at species rank in Bacteria.
    Taxonomy does not establish production or a strain.
  snapshot_sha256: 304bc03819953205926afe20a2511a4840bdd27668fd4614dbd7a0c1e3142cb8
- evidence_id: genome
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=BD306272.1,DJ389528.1&rettype=gbwithparts&retmode=xml
  locator: Exact accession-version, definition, source feature and references; HTTP200
    capture 2026-10-13T15:39:42.133857Z..2026-10-13T15:39:42.621788Z; payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/sequences.xml;
    receipt SHA256 30d35df4b5eb9ed3fe53fbae6e845689bc3e46d5dac3013aaa109ce54eff13d2
  accessed_at: '2026-10-13T17:01:21.991255Z'
  support: supports
  summary: BD306272.1 is9052nt from A.oryzae5062 and cites JP2003125779-A sequence10;
    DJ389528.1 is23114nt from A.niger5061 and cites JP2003230381-A sequence2. Neither
    source feature supplies a strain. Whole-sequence lengths do not specify cluster
    bounds.
  snapshot_sha256: 17fcbc35ec66b72ddcbef600dcb8ad1633d4723ac15e466a9124891d296e6177
- evidence_id: scope-proof
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-resume-mXOYL5/capture.json
  locator: Ignored-inclusive owner/component enumeration and prior-review hashes
  accessed_at: '2026-10-13T17:01:21.991424Z'
  support: supports
  summary: All3115 owners,243 components and30 predecessor review pairs match the
    prior merged checkpoint. Every new inspected input matches Git504e6b184. Only
    context change since interrupted research is the unrelated BGC0002321:4 strain
    row, whose diff was read.
  snapshot_sha256: 68dce8d62be62dc68e2039130f0725edf7c0a48251b7bfbf23a302fa732403fa
- evidence_id: search
  kind: search
  reference: /private/tmp/npmech-ferrichrome-resume-mXOYL5/local-search.log
  locator: rg ignored-inclusive bounded search
  accessed_at: '2026-10-13T17:01:21.991534Z'
  support: supports
  summary: Search found source inventories and exact owners but no applicable existing
    ferrichrome curation-table decision or prior canonical review. Complete owner
    parsing supports optional-field absence only within these exact files.
  snapshot_sha256: 4dfd86adef065096ed66fbbdc0cc86b50a035508afcb480171488fb34a7707b7
  search_scope: rg --no-ignore --hidden -l with both keys, accessions, minted IDs
    and ferrichrome over curation data/raw data/natural_products data/causal_graphs
    reviews docs scripts src conf tests. Ignored/hidden files included in those directories;
    external caches, Git objects and virtual environments not covered.
- evidence_id: qc-evidence
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-resume-mXOYL5/qc.log
  locator: Full actual native QC log
  accessed_at: '2026-10-13T17:01:21.991619Z'
  support: supports
  summary: Read-only consistency gates; results do not promote SEEDED status.
  snapshot_sha256: 0715e841e01e87c16ccdaf2df40b501ae40ed1d33a0a66e027597fabc4367407
- evidence_id: labels-evidence
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-resume-mXOYL5/labels.log
  locator: Configured full-corpus label check
  accessed_at: '2026-10-13T17:01:21.991716Z'
  support: supports
  summary: Warnings and no-adapter skips retained; NCBITaxon names/ranks independently
    verified.
  snapshot_sha256: 556ef5804e095767472c0aa8a542d5bff7e332470383a992e6b260103034414b
- evidence_id: queue-evidence
  kind: validation
  reference: /private/tmp/npmech-ferrichrome-resume-mXOYL5/queue.tsv
  locator: Exhaustive pending-record queue
  accessed_at: '2026-10-13T17:01:21.991797Z'
  support: supports
  summary: All3115 owners remain in the native pending population; scientific review
    coverage is separately recorded.
  snapshot_sha256: 95ec05957b30a82f7508a4b2bd12635b9e038c9f5fce6b9e9002c94979fee27c
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/JP2003125779A/en
  locator: JP2003125779A description0004,0015-0025,0027-0051; prose, not visual sequence
    figures; HTTP200 capture 2026-10-13T15:38:47.295850Z..2026-10-13T15:38:47.924509Z;
    payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/patent.html; receipt SHA256
    14b7bf9f5d25f505db153aef26ea20d5fb83096391b4d8693208a877b8f0992c
  accessed_at: '2026-10-13T17:01:21.996515Z'
  support: partial
  summary: The patent discusses a ferrichrome family/member rather than proving this
    C26 structure. It names O-1013 genomic material and a distinct1013-niaD example
    host; asb3 expression in E.coli tests acetylation, not whole-product biosynthesis.
    Japanese member spelling is not automatically equated with ferricrocin. Machine
    translation is imperfect.
  snapshot_sha256: 324b325a0cd6eeb5f1d00f1ea809dc432f679c9de383c7e1ec4a617e462db0e2
- evidence_id: occurrence-metadata
  kind: database
  reference: https://api.crossref.org/works/10.1021/ja01468a020
  locator: Crossref DOI, title, authors and print date; HTTP200 capture 2026-10-13T15:37:06.389836Z..2026-10-13T15:37:06.717560Z;
    payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/occurrence-crossref.json;
    receipt SHA256 07eef161388a13863ec3b30ad43f427ba4bf76616bed9d60470cf39b289dd39b
  accessed_at: '2026-10-13T17:01:21.997491Z'
  support: partial
  summary: DOI10.1021/ja01468a020 resolves to Emery/Neilands, Structure of the Ferrichrome
    Compounds, JACS83:1626-1628,1961. The2002 online date is not a new experiment.
    Metadata contains no inspected experimental occurrence evidence.
  snapshot_sha256: d1f67cc332b7862abc329179be6a95402d76bfbbb636e6306e71a899edf9a082
- evidence_id: occurrence-access
  kind: search
  reference: https://doi.org/10.1021/ja01468a020
  locator: Error response only; HTTP403 capture 2026-10-13T15:38:53.604610Z..2026-10-13T15:38:54.001755Z;
    payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/occurrence.html; receipt
    SHA256 a9c32e8c5ffea6d102a22b8ee51d379218d4fad16774522d7845146471789df3
  accessed_at: '2026-10-13T17:01:21.997867Z'
  support: unknown
  summary: HTTP403; primary content/identifier response not inspected. No alternate
    route attempted.
  snapshot_sha256: 60b5de42330659dc2460b2deaea08e8376ee864d1ceb15faf81d5e09194ceb09
  search_scope: Single preserved exact-URL request and receipt; stopped after403.
    Does not imply the claim is false or absent from the source.
- evidence_id: wikidata-access
  kind: search
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q25419.json
  locator: Error response only; HTTP403 capture 2026-10-13T15:45:20.406431Z..2026-10-13T15:45:20.473573Z;
    payload /private/tmp/npmech-ferrichrome-review-W2MXlZ/wikidata-Q25419.json; receipt
    SHA256 8ba01772d3ffaa63bbd8433543bb97afeed2f03d8f46f2bc4719bfce265924cb
  accessed_at: '2026-10-13T17:01:21.998236Z'
  support: unknown
  summary: HTTP403; primary content/identifier response not inspected. No alternate
    route attempted.
  snapshot_sha256: 165da4d5af47d0a2008597750d184a3cef870aff9d0a5005b71d6bd17a75672e
  search_scope: Single preserved exact-URL request and receipt; stopped after403.
    Does not imply the claim is false or absent from the source.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact named chemical form
  outcome: concern
  summary: Confirmed C26/N-formyl versus C27/triacetyl identity conflict; neither
    removing iron nor choosing the other same-label owner solves it. The exact patent
    product and any replacement remain unselected.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - chemistry
  - chebi-ferrichrome
  - chebi-deferrichrome
  - pubchem
  dimensions:
  - name: exact-key
    value: ZZDYFKJSJLUQON-UFYCRDLUSA-N
    definition: Stored owner identity, not a proposed replacement
    evidence_ids:
    - owner
    - chemistry
  - name: stereo-resolution
    value: 3 specified/0 undefined centers
    definition: Encoded tetrahedral resolution, not experimental assignment
    evidence_ids:
    - chemistry
- assessment_id: representation
  area: consistency
  topic: Internal chemistry and pinned source representation
  outcome: supported
  summary: Stored SMILES, InChI and key roundtrip and agree with versioned MIBiG.
    stereo_complete correctly describes the encoded peptide centers. Formal charge
    and coordination depiction do not independently establish biological chemical
    form.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - chemistry
  - mibig
- assessment_id: grounding
  area: grounding
  topic: Minted rationale and exact registry links
  outcome: concern
  summary: Minted status is consistent with the absence of an exact pinned ChEBI default
    key. CID90658043 is exact; CID644246 is nonexact and needs withholding. No parent/congener
    assertion is present.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - inventories
  - pubchem
  - chemistry
- assessment_id: classification
  area: representation
  topic: Chemical filing and asserted taxonomy facets
  outcome: supported
  summary: NPClassifier@2026-09-07 cyclic-peptide/oligopeptide and nonglycoside output
    matches the pinned row and AMINO_ACIDS_AND_PEPTIDES filing. OTHER remains the
    database BGC class rather than a predicted enzyme class. FUNGAL producer grouping
    matches NCBI. OTHER_BACTERIAL correctly groups the E.coli occurrence without converting
    it to a producer.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - inventories
  - mibig
  - taxonomy
- assessment_id: origin
  area: scope
  topic: Natural versus engineered exact-product origin
  outcome: concern
  summary: NATURAL_PRODUCT is database-derived, not classifier-derived, but exact
    chemical attribution inherits F1. Host engineering and enzyme expression in a
    patent do not by themselves establish biosynthesis of the stored complete molecule.
    Do not silently reclassify as engineered either.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - mibig
  - chemistry
  - patent
- assessment_id: producer
  area: evidence
  topic: Producer identity, strain and evidence tier
  outcome: unknown
  summary: The species taxon is correct and SOURCE_ASSERTION faithfully reflects the
    database rather than an isolation experiment. Patent source-strain context must
    be reconciled only after exact product identity; do not infer species-wide experimental
    production or copy an expression host into native producers. The sequence source
    alone supplies no strain.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - mibig
  - taxonomy
  - genome
  - patent
  dimensions:
  - name: taxon-rank
    value: species
    definition: NCBI rank for the record producer identifier
    evidence_ids:
    - taxonomy
  - name: producer-grade
    value: SOURCE_ASSERTION
    definition: Native imported grade; not upgraded
    evidence_ids:
    - owner
    - mibig
- assessment_id: cluster
  area: evidence
  topic: Exact BGC version, locus and compound-level method
  outcome: unknown
  summary: Active version5 and genome accession are confirmed. Unstated source bounds/methods
    correctly remain omitted/CLUSTER_UNSTATED. Independent genomic and enzyme context
    does not establish the complete exact product or justify upgrading a whole locus.
    Gene coordinates in live to_add annotations were not owner-curated claims.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - mibig
  - genome
  - patent
- assessment_id: occurrence
  area: scope
  topic: Detection versus biosynthesis
  outcome: unknown
  summary: The LOTUS triple is faithfully imported as DATABASE_ASSERTION occurrence,
    not production. NCBITaxon562 is correct, but the1961 experiment and Q25419 linkage
    remain unavailable. Neither assume the paper proves production nor declare the
    occurrence false from its title.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - inventories
  - taxonomy
  - occurrence-metadata
  - occurrence-access
  - wikidata-access
- assessment_id: activity
  area: scope
  topic: Pure-compound assays, summaries and molecular targets
  outcome: supported
  summary: No activity, molecular target or activity summary is asserted. The uncited
    MIBiG siderophore annotation was not elevated into an assay. Empty PubChem no-assay
    placeholders do not mean inactivity; patent enzyme assays are not bioactivity
    of the complete natural product.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - inventories
  - mibig
- assessment_id: mechanism
  area: graph
  topic: Pathway and complete causal/assembly mechanism
  outcome: not_applicable
  summary: No pathway steps, protein examples, inline graphs or external components
    are attached. Optional absence is not a scientific defect; generic family biosynthesis
    must not be fabricated as this structure-specific mechanism.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - resolved
- assessment_id: optional
  area: completeness
  topic: Clinical, dataset, cross-corpus and relationship claims
  outcome: not_applicable
  summary: No clinical status, dataset list, related_records, parent_compounds or
    congener_of assertions require review. The embedded BGC accession was checked
    separately. Exact-key sibling scans were bounded to the committed inventory, not
    a global absence claim.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - inventories
  - resolved
- assessment_id: audit
  area: provenance
  topic: History, sign-off and maintained owners
  outcome: supported
  summary: Both events are seeding events and SEEDED is appropriate. No curator discussion
    resolves the new concerns. Reviews do not mutate native status or history. Future
    source corrections use implemented pinned tables or a separately tested transform;
    decisions.tsv is reserved and not consumed.
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  evidence_ids:
  - owner
  - scope-proof
  - search
  - qc-evidence
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
  - inventories
  - chemistry
  - mibig
  - chebi-ferrichrome
  - chebi-deferrichrome
  - pubchem
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
- finding_id: F2
  issue_key: mibig-BGC0000900-compound-1-pubchem-644246-nonexact
  category: grounding
  severity: major
  status: open
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
  - inventories
  - chemistry
  - pubchem
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
actions:
- action_id: A1
  description: Adjudicate the exact chemical form before any structure migration.
    First add a cited curator-owned conflict/qualification through the validated writer.
    Only use REPLACE_WITH_CHEBI after a unique experimental target, destination ownership,
    source row and target row are independently established; otherwise retain the
    explicit unresolved conflict. Never transfer old-key occurrences, assays or graphs
    automatically.
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
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/ferrichrome-2.yaml
    role: Guarded curator-owned discussion and audit event only
  generator: scripts/seed_from_sources.py, only after separately authorized curation
    and canary; never direct seeded-field edits
  acceptance_checks:
  - Inspect primary exact product/isotope/stereo evidence; distinguish named compound
    from family and native from engineered context.
  - Recompute InChI/key with pinned RDKit, audit source joins and all old-key claims,
    and inspect guarded one-record canary.
  - Run just validate-strict, just verify-reproduction, just verify-corpus, just validate-products
    and just qc; preserve history and component ownership.
- action_id: A2
  description: For the current unchanged structure, withhold literal pubchem:644246
    through the implemented complete-row-pinned xref exclusion for BGC0000900:1. Preserve
    exact pubchem:90658043 and raw provenance. If A1 instead changes structure, adjudicate
    xrefs with that migration; concurrent structure replacement and xref exclusion
    are intentionally incompatible.
  finding_ids:
  - F2
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
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
  generator: scripts/seed_from_sources.py guarded canary and regeneration
  acceptance_checks:
  - Pin complete source row SHA25678b115cce5a8a133196da68d8dd417a75f5a8f42aa0344a1d3c76d389e58f791
    and cite the live PubChem identity evidence.
  - Generated xrefs omit644246 but retain90658043 for the unchanged owner; source-conflict
    provenance remains visible.
  - Test source-row drift, duplicate decisions and incompatible corrections; run strict
    validation, reproduction and full QC.
- action_id: A3
  description: Complete unavailable primary checks through authorized access or user-provided
    source text, and reconcile source-strain context after identity adjudication.
    Preserve species identifiers and conservative producer/locus grades until exact
    evidence justifies a change.
  finding_ids: []
  target_ids:
  - naturalproductmech:mibig-ab69cdf6e5
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented source-row-pinned strain qualification when exact context is
      established
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
  - Inspect the complete cited study and exact product/strain/experimental context;
    preserve each403 limitation until resolved.
  - Do not reuse family-level claims, isotope tracers, or expression-host enzyme activity
    as native complete-product proof.
limitations:
- Required primary material is unavailable; partial coverage is not a whole-record
  scientific pass or eligibility for REVIEWED.
- Prior research captures are preserved with original retrieval times; fresh merged-state
  inspection and computation revalidated unchanged inputs. The unrelated strain-table
  addition was separately read.
- Earlier PubChem503 and ChEBI504 events remain in the historical202-access-limitation
  ledger. One new-turn retry recovered both PubChem IDs and both ChEBI authorities;
  these four identities are no longer currently unavailable. No403 endpoint was retried
  via an alternate path.
- Patent prose and tabular text were inspected; DNA/protein sequence images and original
  Japanese legal document facsimiles were not visually audited. Machine translation
  can misname organisms, enzymes and ferrichrome-family members.
- Optional absent fields are not counted as deficiencies. No full-corpus scientific
  conclusion follows from native consistency tests.
- The initial uv wrapper and isolated-runtime import failures are retained as execution
  history; their native-script retries passed.
- Temporary evidence paths are session-local; stable source URLs, source-row digests,
  exact Git inputs and payload hashes are included. No scientific record, status,
  history, raw inventory, generated page or GitHub object was changed.
notes:
- Full objective remains review of every3115 owner and its attached components; unassessed
  and partial work is not redefined as complete.
- Original interrupted research began2026-10-13T15:35:47.926332Z. This review uses
  actual resumed assessment timestamps, not a backdated filename.
```
