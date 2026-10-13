# vibrioferrin: scoped source-correction disposition

- Review: 20261013T201544Z-vibrioferrin-scoped-disposition
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T20:01:56.894109Z
- Finished UTC: 2026-10-13T20:15:44.115196Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Nonexact xref, claim citation routing and WP1 qualifier resolved; indirect occurrence provenance remains open.

## Scope And Provenance

One exact owner; scoped predecessor disposition, not a new whole-record assessment.

Selection: User-authorized PR, adversarial review and issue remediation.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 38cab91d99604c44daf896f2a7e762235667efbf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:84585 | data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml | generated | vibrioferrin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| focused-corrected | passed | True | CHEBI:84585 | 309 focused tests passed after correcting a malformed synthetic structure-correction fixture. |
| focused-curation | passed | True | CHEBI:84585 | 26 focused curation, citation and archive tests passed; a further qualification-preservation regression is covered by full QC. |
| strict | passed | True | CHEBI:84585 | Both exact owners passed strict closed-schema validation with zero errors. |
| reseed-a | passed | True | CHEBI:84585 | CHEBI:84585 regenerates byte-identically, including curator qualifications and history. |
| reseed-b | passed | True | CHEBI:84585 | BGC0000947 owner regenerates byte-identically, including qualification and history. |
| scope-audit | passed | True | CHEBI:84585 | All3115owners/243components retained; two owners changed,3113unchanged. Raw inventories, path lock and40prior review pairs unchanged. |
| labels | passed | True | CHEBI:84585 | Configured label check passed with499existing nonblocking mismatches and4649no-adapter skips; not chemical equivalence approval. |
| qc | passed | True | CHEBI:84585 | Fresh full native QC passed:786tests,3skips,2dependency warnings; all-owner strict validation, reproduction, site, provenance and governance passed. Exact receipts are retained. |
| focused initial attempt | failed | False | CHEBI:84585 | One synthetic test fixture omitted the required structure-correction citation;308tests passed and1failed. Corrected fixture and subsequent focused/full QC runs pass. |
| docs-stats initial attempt | failed | False | CHEBI:84585 | Initial check detected stale generated statistics; docs-write regenerated them and full QC passed the documentation check. |
| Uncompleted exact-source scientific checks | unavailable | True | CHEBI:84585 | All predecessor full-text and authority-access limits remain. No new primary retrieval, exact-strain identity adjudication or full-record sign-off is claimed. |

## Scientific And Domain Assessments

### Exact-owner source corrections

scope: supported. Targets: CHEBI:84585.

Nonexact xref, claim citation routing and WP1 qualifier resolved; indirect occurrence provenance remains open. The field-by-field comparison preserves all other scientific assertions.

### Remaining scientific uncertainty

evidence: concern. Targets: CHEBI:84585.

OPEN qualifications are not completed identity or native occurrence adjudication. Both owners remain SEEDED and their earlier access limitations still apply.

### Immutable history and durable evidence

provenance: supported. Targets: CHEBI:84585.

Original40observations remain unchanged; scoped successors retire only supported defects. Full campaign coverage is not inflated.

## Findings

### F1: PubChem197680 is not an exact chemical cross-reference

major / resolved / confirmed; issue key: chebi84585-nonexact-pubchem197680.

The official PubChem response encodes FPHRKFJYHKRDFJ-LWYCVJHGSA-N, whereas this owner and ChEBI84585 encode IGQXNKDXMPSELX-BIAKFKOBSA-N. RDKit and visual comparison confirm four free acids/no ester versus three free acids/one ester. Equal formula and exact mass do not establish equivalence. The incorrect xref originates in BGC0000946:1; BGC0002527:1 contributes a separate NPAtlas identifier whose equivalence remains unknown after403. Withhold only the proven nonexact PubChem assertion, not the NPAtlas identifier.

Disposition: Resolved the false exact cross-reference through a complete-row-pinned exclusion of pubchem:197680 on0946 only. The source assertion remains in the unchanged inventory and a resolved table-owned discussion. Neither a replacement CID nor NPAtlas equivalence is inferred.

### F2: A compound-bioactivity citation displaces the entry-specific taxon/locus reference

major / resolved / confirmed; issue key: mibig-BGC0002527-bioactivity-reference-used-for-locus.

BGC0002527.2 attaches DOI10.1021/ic9016883 to siderophore bioactivity and retains PMID26452553 at entry level. The extractor chooses the former through its generic priority rule, and mibig_evidence reuses it for both the CA producer and CP005094.1 locus. The inspected2009 abstract concerns iron binding/photochemistry and marine bacteria; the2016 abstract explicitly concerns Azotobacter vibrioferrin and genome-based capacity. This confirms cross-claim citation selection, not a claim to have read either full paper or proved their every negative. Preserve the original database assertion and route claim-appropriate references separately. Full2016 evidence is still needed before assigning experimental grades or asserting those coordinates were tested.

Disposition: Resolved this2527 citation-routing defect with an implemented tested full-row-pinned correction. PMID26452553 remains DATABASE_ASSERTION; separate CURATOR_INFERENCE preserves the original activity DOI/level and decision source. This does not fix generic extraction for unreviewed rows, validate the full primary experiment or upgrade grades.

### F3: The ChEBI alginolyticus origin citation is indirect, not that study's detection experiment

minor / open / confirmed; issue key: chebi84585-alginolyticus-indirect-origin-citation.

The full PMID22146715 paper does mention V.alginolyticus and V.parahaemolyticus as previously known sources. Its experiment, however, produces structurally characterized vibrioferrin in E.coli from sediment clone MG93-1; the donor taxon is not established by the protein homology comparisons. ChEBI84585 repeats the alginolyticus origin/PMID pair, so the import is faithful. Treat this as indirect prior-literature support and trace the actual isolation/biosynthesis source. Do not infer that alginolyticus cannot produce vibrioferrin, delete the occurrence merely because the paper is indirect, or turn the metagenomic clone into an identified native producer.

Disposition: A cited OPEN discussion qualifies the ChEBI origin as indirect prior-literature context. The upstream occurrence remains unchanged; native detection provenance is not yet resolved and no taxon is reassigned.

### F4: The deposited WP1 strain is missing from the producer claim

minor / resolved / confirmed; issue key: mibig-BGC0000946-vibrioferrin-source-strain.

AB082123.1 names V.parahaemolyticus strain WP1, but the corresponding BGC0000946 producer has only species-rank NCBITaxon670. The AQ3354 detection_context in a different ChEBI occurrence is not this accession's strain and must not be copied across. CA is already represented by strain-rank NCBITaxon1283330 and needs no inferred taxon replacement.

Disposition: Resolved missing deposited strain context only. WP1 stays separate from AQ3354; MVPO1 is the GenBank literal and MVP01 the explicitly retained publisher spelling. No canonical spelling, strain taxid, species-wide production or evidence upgrade is inferred.

## Recommended Actions And Acceptance Checks

### A3

Trace primary native alginolyticus detection or biosynthesis evidence for the retained ChEBI occurrence. The OPEN indirect-citation qualification is already present. Do not replace its taxon with the heterologous E.coli host or infer the environmental donor; any generated-row correction needs its own implemented tested path.

- Distinguish background organism mention, sequence homology, experimental host and natural producer.
- Any retained direct detection citation supports the exact product and taxon.
- Do not delete a biologically plausible occurrence merely because its current source is indirect.
- Use maintained input/transform with regression tests; do not patch generated scientific fields.
- For authorized curation: validated writer and append-only event, seeder dry run/canary, exact diff, strict validation, verify-corpus, verify-reproduction and full qc.
- Retain raw source assertions, taxon IDs, source versions and independent producer/locus evidence grades.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml; Entire current owner and append-only history | supports | Reviewed citation/xref/strain changes and OPEN qualifications are visible. Chemistry, organism assertions, evidence grades and SEEDED status remain unchanged. |
| prior | reviews/structured/20261013T193947Z-vibrioferrin/review.yaml; Immutable predecessor findings and access limitations | supports | The full-record partial assessment remains intact. This successor is limited to disposition of its findings. |
| strain-table | curation/mibig_producer_strains.tsv; Current maintained input; distinct-owner changes are context only | supports | Exact full-row-pinned WP1 and MVPO1 qualifiers; MVP01 publisher spelling and AQ3354 occurrence context remain distinct. |
| xref-table | curation/mibig_xref_exclusions.tsv; Current maintained input; distinct-owner changes are context only | supports | Only BGC0000946 PubChem197680 exact equivalence is withheld; BGC0000947 CID and CHEBI84585 NPAtlas assertion remain. |
| citation-table | curation/mibig_claim_references.tsv; Current maintained input; distinct-owner changes are context only | supports | The2527 source entry PMID is routed to producer and locus with separate curator attribution; raw bioactivity citation is retained. |
| citation-code | src/naturalproductmech/curate/claim_references.py; Current maintained input; distinct-owner changes are context only | supports | Guarded source-pinned loader rejects drift and malformed decisions; routing preserves other qualifications and evidence grades. |
| archive | reviews/evidence/20261013-vibrioferrin/manifest.json; Current maintained input; distinct-owner changes are context only | supports | 115retained artifacts and21reference-only sources preserve input hashes, receipt lineage and the whole-corpus checkpoint. |
| scope-proof | /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/scope-audit.json; Full corpus hashes and object-level comparison | supports | Only the reviewed claims and two OPEN qualifications changed; no owner migration, occurrence reassignment or unrelated scientific edit. |
| regressions | /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/focused-curation.log; Focused remediation and archive tests | supports | 26tests passed before an additional qualification-preservation regression in full QC. |
| native-qc | /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/qc.log; Fresh full native quality gate | supports | All native gates passed; deterministic consistency is not scientific completion. |
| chemistry | /private/tmp/npmech-vibrioferrin-resume-42VRr6/chemistry.json; Owner/MIBiG/ChEBI/PubChem roundtrips and functional-group counts; same captured source reassessed for scoped disposition, not a new retrieval | supports | Both neutral structures calculate C16H22N2O12 and434.117274144Da, charge0. FPHR has two assigned/two undefined centers, four free acids and no ester; IGQX has two assigned/one undefined center, three free acids and one ester. Stereo flags are internally correct; mass equality cannot select identity. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/197680/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; Official PUG REST properties: InChI, InChIKey, SMILES and formula; captured 2026-10-13T18:33:28.326859Z..2026-10-13T18:33:28.758788Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/pubchem197680.json; receipt SHA256 6798e11f45164c0b91d74083154b2591cf47638599ddd9cccbd2993ca0c3dbc2; same captured source reassessed for scoped disposition, not a new retrieval | supports | CID197680 exactly matches FPHRKFJYHKRDFJ-LWYCVJHGSA-N, not IGQXNKDXMPSELX-BIAKFKOBSA-N. This validates registry representation, not the biological assignment. |
| sequences | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=DQ201184.2,AB082123.1&amp;rettype=gbwithparts&amp;retmode=xml; DQ201184.2 and AB082123.1 source features, organism/strain/taxid and references; captured 2026-10-13T18:33:30.484659Z..2026-10-13T18:33:30.890466Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/sequences.xml; receipt SHA256 5c0014fba10c8bba3e915e2db8346b87fd29d2ed1ff9a286e03a6d24f30e45e7; same captured source reassessed for scoped disposition, not a new retrieval | supports | DQ201184.2=V.alginolyticus/MVPO1 (letter O), citation PMID17593352; AB082123.1=V.parahaemolyticus/WP1, citation PMID14617658. Sequence annotation anchors the deposit, not the exact product structure. |
| metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fj.1574-6968.1992.tb05311.x%22+OR+DOI%3A%2210.1007%2Fs00203-007-0261-6%22+OR+DOI%3A%2210.1021%2Fic9016883%22+OR+DOI%3A%2210.1021%2Fic9016883%22+OR+DOI%3A%2210.1093%2Foxfordjournals.jbchem.a124432%22+OR+DOI%3A%2210.1111%2Fj.1574-6968.2011.02389.x%22+OR+DOI%3A%2210.1128%2Faem.03160-15%22+OR+DOI%3A%2210.1128%2Fjb.00162-13%22+OR+DOI%3A%2210.1128%2Fjb.185.23.6938-6949.2003%22+OR+DOI%3A%2210.1271%2Fbbb.110379%22+OR+%28EXT_ID%3A14617658+AND+SRC%3AMED%29+OR+%28EXT_ID%3A17593352+AND+SRC%3AMED%29+OR+%28EXT_ID%3A22146715+AND+SRC%3AMED%29&amp;format=json&amp;resultType=core&amp;pageSize=100; Eight EuropePMC core records and full returned abstracts; DOI/PMID aliases resolved; captured 2026-10-13T18:33:25.693443Z..2026-10-13T18:33:26.796795Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/metadata.json; receipt SHA256 ab6411f5f6962beeb566a5547362070ee3641826d86380b97ea5f7573617009f; same captured source reassessed for scoped disposition, not a new retrieval | partial | 1994 identifies a citrate ester with equilibrating epimers;2003/2007 describe native siderophore disruption;2011 receptor work concerns uptake;2013 concerns RyhB/Hfq regulation;2009 concerns iron binding/photochemistry;2016 concerns Azotobacter chelome;2011 metagenomic expression is verified against full text. Abstract-only evidence does not settle all strain and product claims. |
| primary2011 | https://www.jstage.jst.go.jp/article/bbb/75/12/75_110379/_pdf; All five PDF pages; pp2284-2285 Figures1,3/Table1 visually inspected; pp2286-2287 methods/reference list; captured 2026-10-13T19:30:16.635878Z..2026-10-13T19:30:18.149789Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-resume-42VRr6/jstage2011.pdf; receipt SHA256 105381ec17c439d7bd021afe21c95c7871a7957b9cb9afd35ce9b61b5c4684ea; same captured source reassessed for scoped disposition, not a new retrieval | supports | Purified MG93-1 E.coli product has citrate-ethanolamine ester connectivity and interconverting aminal epimers. Native Vibrio species are prior-literature context; environmental donor remains unidentified. Figure4 is explicitly hypothetical, based on homology, and does not establish individual enzyme steps experimentally. |
| primary2007 | https://doi.org/10.1007/s00203-007-0261-6; Publisher abstract, source references and subscription preview notice; captured 2026-10-13T19:32:33.829658Z..2026-10-13T19:32:36.516188Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-resume-42VRr6/primary2007.html; receipt SHA256 195fce28fee626bbf37df8e1babf0d08f4cd67adfefcba0141475e40141d2c83; same captured source reassessed for scoped disposition, not a new retrieval | partial | MVP01 (zero) is the publisher spelling. Abstract reports native pvsA/pvsD disruption and siderophore rescue. Full experiment/structure details require subscription and were not accessed; no alternate retrieval. |
| mibig-BGC0002527.2 | https://mibig.secondarymetabolites.org/repository/BGC0002527.2/annotations.json; Exact accession/version/status, compounds[0], taxonomy,loci,classes and legacy_references; captured 2026-10-13T18:33:27.611612Z..2026-10-13T18:33:28.223442Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/BGC0002527.2.json; receipt SHA256 b49582e3f48e34e9c117758e05143fdadb777215648bcf2836d61a83101f753b; same captured source reassessed for scoped disposition, not a new retrieval | supports | Active versioned source matches the imported graph/taxon/accession. Locus evidence methods are empty, correctly imported as SOURCE_ASSERTION/CLUSTER_UNSTATED; quality and review placeholders are not truth signals. No claim of latest version. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/84585/; Default structure, three-star status, definition, chemical_data and both compound_origins; captured 2026-10-13T18:33:28.873693Z..2026-10-13T18:33:29.543360Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/CHEBI84585.json; receipt SHA256 7f8d4be564eecc439576597a8182658e8ea4ea8163f644d003505a5031e92e42; same captured source reassessed for scoped disposition, not a new retrieval | supports | CHEBI84585 matches the neutral IGQX structure, definition and imported origins. The alginolyticus/PMID22146715 pairing is upstream, not invented by the seeder. AQ3354 is occurrence context only. |

## Limits And Additional Notes

- Scoped partial disposition only; no newly assessed owner and no full scientific sign-off.
- All predecessor primary and authority access limitations remain. No alternate retrieval after denial.
- Full QC preceded saving these successors; canonical append-only checks and contract tests follow saving.
- Exact inspected commit is retained by review-base/vibrioferrin-remediation-20261013.
- Generic extractor citation selection for other unreviewed rows remains unchanged; the new correction is explicitly source-scoped.
- The campaign retains3088unassessed owners and26partial assessments;1historical completed full assessment is not native REVIEWED promotion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T201544Z-vibrioferrin-scoped-disposition
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'vibrioferrin: scoped source-correction disposition'
started_at: '2026-10-13T20:01:56.894109Z'
finished_at: '2026-10-13T20:15:44.115196Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: The implementing assistant performed a separate adversarial
    pass; not an independent human review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Nonexact xref, claim citation routing and WP1 qualifier resolved; indirect
  occurrence provenance remains open.
source:
  git_revision: 38cab91d99604c44daf896f2a7e762235667efbf
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: f3f808ad1e58d79947aa82ecf1272e465cfbef57e5a4cd646731af23bb48ce75
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 3188b61104388bf7725540c7e29f83f65ae3a0b458710c6e42de6a0c4bff215e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: ac01b66bb97bc2c4e16558227fed641e28daa3c5926a09e213e98c38a09856a2
    role: context
  - path: data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
    sha256: 856383c41c683326dd289838cbadc920443ae4f64a2d0f44feead447b3f206ad
    role: target
  - path: data/raw/mibig_compounds.tsv
    sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
    role: context
  - path: docs/CURATION.md
    sha256: aba5606d7e5e7c2887e66294655db26a10e853a42893d71aab8f015dc9b91c71
    role: context
  - path: docs/record-review-profile.md
    sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: reviews/evidence/20261013-vibrioferrin/manifest.json
    sha256: adfc0f32df445bb55b10feb3bd106079ba585f4167ae1a80ed7b9eee54c6c8e4
    role: context
  - path: reviews/structured/20261013T193947Z-vibrioferrin/review.yaml
    sha256: d903c9ad25aa4cb29cad6c12dbf74a7396aab8432a7d1e21dcbe83a4e83797e1
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 21fd298fb528f1179286125bc3d12f36ae72ca6c1e0f783cf94dcace2648f292
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: 6026ddca19f0989d499b1681f7724fbab23918de8d3957750b49bbfe1a9c0bff
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
  - path: tests/test_claim_references.py
    sha256: a9e366a1a2db5971fac3c3fcc328a0c9a6b4c85f9e9042deeccb051e79a3434d
    role: context
  - path: tests/test_vibrioferrin_curation.py
    sha256: ddb97fbb867386d070e6f4cc00ed0e8b1d33483cc66cebd1b7ce93e14f909edb
    role: context
  - path: tests/test_vibrioferrin_review_archive.py
    sha256: c55d0b11e3574fcf2925e86eee46c494a6985b028347d582e4950de4d9b5c606
    role: context
targets:
- target_id: CHEBI:84585
  path: data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
  label: vibrioferrin
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
  description: One exact owner; scoped predecessor disposition, not a new whole-record
    assessment.
  selection: User-authorized PR, adversarial review and issue remediation.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CHEBI:84585
  exclusions:
  - target: Other owners and remaining predecessor scientific checks
    reason: No new whole-owner coverage. Full scope remains3115owners and243components.
checks:
- check_id: focused-corrected
  name: focused-corrected
  status: passed
  required: true
  command: .venv/bin/pytest -q tests/test_claim_references.py tests/test_producer_strains.py
    tests/test_xref_exclusions.py tests/test_seed_skeleton.py tests/test_structure_corrections.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: 309 focused tests passed after correcting a malformed synthetic structure-correction
    fixture.
  scope_note: Executed 2026-10-13T19:56:08.138573Z to 2026-10-13T19:56:28.130651Z;
    log /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/focused-corrected.log; SHA256
    071d1c686c2fe61edb0fbd103c81225d6801c8d37e61c0c78ba05f3488617da4
- check_id: focused-curation
  name: focused-curation
  status: passed
  required: true
  command: .venv/bin/pytest -q tests/test_vibrioferrin_curation.py tests/test_vibrioferrin_review_archive.py
    tests/test_claim_references.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: 26 focused curation, citation and archive tests passed; a further qualification-preservation
    regression is covered by full QC.
  scope_note: Executed 2026-10-13T19:57:56.885651Z to 2026-10-13T19:57:59.919599Z;
    log /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/focused-curation.log; SHA256
    66e4a220cf3d7b036a87ba412db973015c003cac4303bbe95eeae2a39b3f888f
- check_id: strict
  name: strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
    data/natural_products/amino_acids_and_peptides/vibrioferrin-2.yaml --out /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Both exact owners passed strict closed-schema validation with zero errors.
  scope_note: Executed 2026-10-13T19:58:17.537188Z to 2026-10-13T19:58:20.752834Z;
    log /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/strict.log; SHA256 9186d5c5a9f68da83b9611ddc6e40f92ba4a123642c731675153d77cefb98a84
- check_id: reseed-a
  name: reseed-a
  status: passed
  required: true
  command: .venv/bin/python scripts/seed_from_sources.py --apply --only CHEBI:84585
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: CHEBI:84585 regenerates byte-identically, including curator qualifications
    and history.
  scope_note: Executed 2026-10-13T19:59:13.833993Z to 2026-10-13T19:59:17.419142Z;
    log /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/reseed-a.log; SHA256 67e92562fe50792bab3f0f4aac51f3fb0afa9d85dd044b9cfbde8fbb6bdc6d39
- check_id: reseed-b
  name: reseed-b
  status: passed
  required: true
  command: .venv/bin/python scripts/seed_from_sources.py --apply --only naturalproductmech:mibig-c1b0b2a6f8
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: BGC0000947 owner regenerates byte-identically, including qualification
    and history.
  scope_note: Executed 2026-10-13T19:59:14.999711Z to 2026-10-13T19:59:18.623003Z;
    log /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/reseed-b.log; SHA256 67e92562fe50792bab3f0f4aac51f3fb0afa9d85dd044b9cfbde8fbb6bdc6d39
- check_id: scope-audit
  name: scope-audit
  status: passed
  required: true
  command: .venv/bin/python /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/scope_audit.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: All3115owners/243components retained; two owners changed,3113unchanged.
    Raw inventories, path lock and40prior review pairs unchanged.
  scope_note: Executed 2026-10-13T19:58:52.065286Z to 2026-10-13T19:58:52.723882Z;
    log /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/scope-audit.log; SHA256 36d3cbde777aa272195f1430c9a4925fa85da25336d27e69520498f11c57f02c
- check_id: labels
  name: labels
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Configured label check passed with499existing nonblocking mismatches and4649no-adapter
    skips; not chemical equivalence approval.
  scope_note: Executed 2026-10-13T19:59:22.655098Z to 2026-10-13T20:01:08.793802Z;
    log /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/labels.log; SHA256 556ef5804e095767472c0aa8a542d5bff7e332470383a992e6b260103034414b
- check_id: qc
  name: qc
  status: passed
  required: true
  command: env RECORD_REVIEW_BASE=39811a084202d1c1a47472622e3008bed7000083 .venv/bin/python
    scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Fresh full native QC passed:786tests,3skips,2dependency warnings; all-owner
    strict validation, reproduction, site, provenance and governance passed. Exact
    receipts are retained.
  scope_note: Executed 2026-10-13T20:00:48.273646Z to 2026-10-13T20:15:27.185311Z;
    log /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/qc.log; SHA256 d91567f32734439fa52bc42dc38ba6264bdb8c5a7d056e68745552da87b4ec8a
- check_id: focused-initial
  name: focused initial attempt
  status: failed
  required: false
  command: .venv/bin/pytest -q tests/test_claim_references.py tests/test_producer_strains.py
    tests/test_xref_exclusions.py tests/test_seed_skeleton.py tests/test_structure_corrections.py
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: One synthetic test fixture omitted the required structure-correction citation;308tests
    passed and1failed. Corrected fixture and subsequent focused/full QC runs pass.
- check_id: docs-stats-initial
  name: docs-stats initial attempt
  status: failed
  required: false
  command: .venv/bin/python scripts/check_docs.py
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - CHEBI:84585
  summary: Initial check detected stale generated statistics; docs-write regenerated
    them and full QC passed the documentation check.
- check_id: remaining-primary
  name: Uncompleted exact-source scientific checks
  status: unavailable
  required: true
  target_ids:
  - CHEBI:84585
  summary: All predecessor full-text and authority-access limits remain. No new primary
    retrieval, exact-strain identity adjudication or full-record sign-off is claimed.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
  locator: Entire current owner and append-only history
  accessed_at: '2026-10-13T20:15:44.113467Z'
  support: supports
  summary: Reviewed citation/xref/strain changes and OPEN qualifications are visible.
    Chemistry, organism assertions, evidence grades and SEEDED status remain unchanged.
  snapshot_sha256: 856383c41c683326dd289838cbadc920443ae4f64a2d0f44feead447b3f206ad
- evidence_id: prior
  kind: record_content
  reference: reviews/structured/20261013T193947Z-vibrioferrin/review.yaml
  locator: Immutable predecessor findings and access limitations
  accessed_at: '2026-10-13T20:15:44.113572Z'
  support: supports
  summary: The full-record partial assessment remains intact. This successor is limited
    to disposition of its findings.
  snapshot_sha256: d903c9ad25aa4cb29cad6c12dbf74a7396aab8432a7d1e21dcbe83a4e83797e1
- evidence_id: strain-table
  kind: record_content
  reference: curation/mibig_producer_strains.tsv
  locator: Current maintained input; distinct-owner changes are context only
  accessed_at: '2026-10-13T20:15:44.113763Z'
  support: supports
  summary: Exact full-row-pinned WP1 and MVPO1 qualifiers; MVP01 publisher spelling
    and AQ3354 occurrence context remain distinct.
  snapshot_sha256: 3188b61104388bf7725540c7e29f83f65ae3a0b458710c6e42de6a0c4bff215e
- evidence_id: xref-table
  kind: record_content
  reference: curation/mibig_xref_exclusions.tsv
  locator: Current maintained input; distinct-owner changes are context only
  accessed_at: '2026-10-13T20:15:44.113841Z'
  support: supports
  summary: Only BGC0000946 PubChem197680 exact equivalence is withheld; BGC0000947
    CID and CHEBI84585 NPAtlas assertion remain.
  snapshot_sha256: ac01b66bb97bc2c4e16558227fed641e28daa3c5926a09e213e98c38a09856a2
- evidence_id: citation-table
  kind: record_content
  reference: curation/mibig_claim_references.tsv
  locator: Current maintained input; distinct-owner changes are context only
  accessed_at: '2026-10-13T20:15:44.113914Z'
  support: supports
  summary: The2527 source entry PMID is routed to producer and locus with separate
    curator attribution; raw bioactivity citation is retained.
  snapshot_sha256: f3f808ad1e58d79947aa82ecf1272e465cfbef57e5a4cd646731af23bb48ce75
- evidence_id: citation-code
  kind: record_content
  reference: src/naturalproductmech/curate/claim_references.py
  locator: Current maintained input; distinct-owner changes are context only
  accessed_at: '2026-10-13T20:15:44.113981Z'
  support: supports
  summary: Guarded source-pinned loader rejects drift and malformed decisions; routing
    preserves other qualifications and evidence grades.
  snapshot_sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
- evidence_id: archive
  kind: record_content
  reference: reviews/evidence/20261013-vibrioferrin/manifest.json
  locator: Current maintained input; distinct-owner changes are context only
  accessed_at: '2026-10-13T20:15:44.114057Z'
  support: supports
  summary: 115retained artifacts and21reference-only sources preserve input hashes,
    receipt lineage and the whole-corpus checkpoint.
  snapshot_sha256: adfc0f32df445bb55b10feb3bd106079ba585f4167ae1a80ed7b9eee54c6c8e4
- evidence_id: scope-proof
  kind: validation
  reference: /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/scope-audit.json
  locator: Full corpus hashes and object-level comparison
  accessed_at: '2026-10-13T20:15:44.114266Z'
  support: supports
  summary: Only the reviewed claims and two OPEN qualifications changed; no owner
    migration, occurrence reassignment or unrelated scientific edit.
  snapshot_sha256: be4ad8bd99b619d220a0aad2374f44320e7c4266976afc7f9877342eb61856fe
- evidence_id: regressions
  kind: validation
  reference: /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/focused-curation.log
  locator: Focused remediation and archive tests
  accessed_at: '2026-10-13T20:15:44.114343Z'
  support: supports
  summary: 26tests passed before an additional qualification-preservation regression
    in full QC.
  snapshot_sha256: 66e4a220cf3d7b036a87ba412db973015c003cac4303bbe95eeae2a39b3f888f
- evidence_id: native-qc
  kind: validation
  reference: /private/tmp/npmech-vibrioferrin-publish-PRF5Nf/qc.log
  locator: Fresh full native quality gate
  accessed_at: '2026-10-13T20:15:44.114442Z'
  support: supports
  summary: All native gates passed; deterministic consistency is not scientific completion.
  snapshot_sha256: d91567f32734439fa52bc42dc38ba6264bdb8c5a7d056e68745552da87b4ec8a
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-vibrioferrin-resume-42VRr6/chemistry.json
  locator: Owner/MIBiG/ChEBI/PubChem roundtrips and functional-group counts; same
    captured source reassessed for scoped disposition, not a new retrieval
  accessed_at: '2026-10-13T20:15:44.114564Z'
  support: supports
  summary: Both neutral structures calculate C16H22N2O12 and434.117274144Da, charge0.
    FPHR has two assigned/two undefined centers, four free acids and no ester; IGQX
    has two assigned/one undefined center, three free acids and one ester. Stereo
    flags are internally correct; mass equality cannot select identity.
  snapshot_sha256: 331b305cb023d835a515a09e65b5d21e6e30dc40180c12cae9b6cdb15e147507
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/197680/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: 'Official PUG REST properties: InChI, InChIKey, SMILES and formula; captured
    2026-10-13T18:33:28.326859Z..2026-10-13T18:33:28.758788Z; HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/pubchem197680.json;
    receipt SHA256 6798e11f45164c0b91d74083154b2591cf47638599ddd9cccbd2993ca0c3dbc2;
    same captured source reassessed for scoped disposition, not a new retrieval'
  accessed_at: '2026-10-13T20:15:44.114578Z'
  support: supports
  summary: CID197680 exactly matches FPHRKFJYHKRDFJ-LWYCVJHGSA-N, not IGQXNKDXMPSELX-BIAKFKOBSA-N.
    This validates registry representation, not the biological assignment.
  snapshot_sha256: 4edd74b20923622244a9f3f8485c619e4376b9898b42d2a0129b45fa47ab0ba5
- evidence_id: sequences
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=DQ201184.2,AB082123.1&rettype=gbwithparts&retmode=xml
  locator: DQ201184.2 and AB082123.1 source features, organism/strain/taxid and references;
    captured 2026-10-13T18:33:30.484659Z..2026-10-13T18:33:30.890466Z; HTTP200; payload
    /private/tmp/npmech-vibrioferrin-review-eZIUfP/sequences.xml; receipt SHA256 5c0014fba10c8bba3e915e2db8346b87fd29d2ed1ff9a286e03a6d24f30e45e7;
    same captured source reassessed for scoped disposition, not a new retrieval
  accessed_at: '2026-10-13T20:15:44.114603Z'
  support: supports
  summary: DQ201184.2=V.alginolyticus/MVPO1 (letter O), citation PMID17593352; AB082123.1=V.parahaemolyticus/WP1,
    citation PMID14617658. Sequence annotation anchors the deposit, not the exact
    product structure.
  snapshot_sha256: 44c416b5845230dc813b9dadc0df98e04391648993dfe4d96bed1b02eca13526
- evidence_id: metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fj.1574-6968.1992.tb05311.x%22+OR+DOI%3A%2210.1007%2Fs00203-007-0261-6%22+OR+DOI%3A%2210.1021%2Fic9016883%22+OR+DOI%3A%2210.1021%2Fic9016883%22+OR+DOI%3A%2210.1093%2Foxfordjournals.jbchem.a124432%22+OR+DOI%3A%2210.1111%2Fj.1574-6968.2011.02389.x%22+OR+DOI%3A%2210.1128%2Faem.03160-15%22+OR+DOI%3A%2210.1128%2Fjb.00162-13%22+OR+DOI%3A%2210.1128%2Fjb.185.23.6938-6949.2003%22+OR+DOI%3A%2210.1271%2Fbbb.110379%22+OR+%28EXT_ID%3A14617658+AND+SRC%3AMED%29+OR+%28EXT_ID%3A17593352+AND+SRC%3AMED%29+OR+%28EXT_ID%3A22146715+AND+SRC%3AMED%29&format=json&resultType=core&pageSize=100
  locator: Eight EuropePMC core records and full returned abstracts; DOI/PMID aliases
    resolved; captured 2026-10-13T18:33:25.693443Z..2026-10-13T18:33:26.796795Z; HTTP200;
    payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/metadata.json; receipt
    SHA256 ab6411f5f6962beeb566a5547362070ee3641826d86380b97ea5f7573617009f; same
    captured source reassessed for scoped disposition, not a new retrieval
  accessed_at: '2026-10-13T20:15:44.114612Z'
  support: partial
  summary: 1994 identifies a citrate ester with equilibrating epimers;2003/2007 describe
    native siderophore disruption;2011 receptor work concerns uptake;2013 concerns
    RyhB/Hfq regulation;2009 concerns iron binding/photochemistry;2016 concerns Azotobacter
    chelome;2011 metagenomic expression is verified against full text. Abstract-only
    evidence does not settle all strain and product claims.
  snapshot_sha256: b069f711e5635e005035d88fdfcbe09a4931e5536f69aec123134f801680276d
- evidence_id: primary2011
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/bbb/75/12/75_110379/_pdf
  locator: All five PDF pages; pp2284-2285 Figures1,3/Table1 visually inspected; pp2286-2287
    methods/reference list; captured 2026-10-13T19:30:16.635878Z..2026-10-13T19:30:18.149789Z;
    HTTP200; payload /private/tmp/npmech-vibrioferrin-resume-42VRr6/jstage2011.pdf;
    receipt SHA256 105381ec17c439d7bd021afe21c95c7871a7957b9cb9afd35ce9b61b5c4684ea;
    same captured source reassessed for scoped disposition, not a new retrieval
  accessed_at: '2026-10-13T20:15:44.114620Z'
  support: supports
  summary: Purified MG93-1 E.coli product has citrate-ethanolamine ester connectivity
    and interconverting aminal epimers. Native Vibrio species are prior-literature
    context; environmental donor remains unidentified. Figure4 is explicitly hypothetical,
    based on homology, and does not establish individual enzyme steps experimentally.
  snapshot_sha256: 9c277977a917aaaa97e4585dc8e4422447cefd04c5966089c4c4820484d9c16a
- evidence_id: primary2007
  kind: primary_source
  reference: https://doi.org/10.1007/s00203-007-0261-6
  locator: Publisher abstract, source references and subscription preview notice;
    captured 2026-10-13T19:32:33.829658Z..2026-10-13T19:32:36.516188Z; HTTP200; payload
    /private/tmp/npmech-vibrioferrin-resume-42VRr6/primary2007.html; receipt SHA256
    195fce28fee626bbf37df8e1babf0d08f4cd67adfefcba0141475e40141d2c83; same captured
    source reassessed for scoped disposition, not a new retrieval
  accessed_at: '2026-10-13T20:15:44.114629Z'
  support: partial
  summary: MVP01 (zero) is the publisher spelling. Abstract reports native pvsA/pvsD
    disruption and siderophore rescue. Full experiment/structure details require subscription
    and were not accessed; no alternate retrieval.
  snapshot_sha256: f24ea9624dc26e15ee7b98820c11683e9192def334a249cb804bf0be607ba38f
- evidence_id: mibig-BGC0002527.2
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002527.2/annotations.json
  locator: Exact accession/version/status, compounds[0], taxonomy,loci,classes and
    legacy_references; captured 2026-10-13T18:33:27.611612Z..2026-10-13T18:33:28.223442Z;
    HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/BGC0002527.2.json;
    receipt SHA256 b49582e3f48e34e9c117758e05143fdadb777215648bcf2836d61a83101f753b;
    same captured source reassessed for scoped disposition, not a new retrieval
  accessed_at: '2026-10-13T20:15:44.114638Z'
  support: supports
  summary: Active versioned source matches the imported graph/taxon/accession. Locus
    evidence methods are empty, correctly imported as SOURCE_ASSERTION/CLUSTER_UNSTATED;
    quality and review placeholders are not truth signals. No claim of latest version.
  snapshot_sha256: a2e65114d495800febb990ea92cf8f6c4dbd5126d85e817e12f48a0a5cf59494
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/84585/
  locator: Default structure, three-star status, definition, chemical_data and both
    compound_origins; captured 2026-10-13T18:33:28.873693Z..2026-10-13T18:33:29.543360Z;
    HTTP200; payload /private/tmp/npmech-vibrioferrin-review-eZIUfP/CHEBI84585.json;
    receipt SHA256 7f8d4be564eecc439576597a8182658e8ea4ea8163f644d003505a5031e92e42;
    same captured source reassessed for scoped disposition, not a new retrieval
  accessed_at: '2026-10-13T20:15:44.114646Z'
  support: supports
  summary: CHEBI84585 matches the neutral IGQX structure, definition and imported
    origins. The alginolyticus/PMID22146715 pairing is upstream, not invented by the
    seeder. AQ3354 is occurrence context only.
  snapshot_sha256: e6fc9b11e3497b91083ab04d102260c96513548a22d0539172fbdd9a562d7b0b
findings:
- finding_id: F1
  issue_key: chebi84585-nonexact-pubchem197680
  category: identity
  severity: major
  status: resolved
  certainty: confirmed
  title: PubChem197680 is not an exact chemical cross-reference
  description: The official PubChem response encodes FPHRKFJYHKRDFJ-LWYCVJHGSA-N,
    whereas this owner and ChEBI84585 encode IGQXNKDXMPSELX-BIAKFKOBSA-N. RDKit and
    visual comparison confirm four free acids/no ester versus three free acids/one
    ester. Equal formula and exact mass do not establish equivalence. The incorrect
    xref originates in BGC0000946:1; BGC0002527:1 contributes a separate NPAtlas identifier
    whose equivalence remains unknown after403. Withhold only the proven nonexact
    PubChem assertion, not the NPAtlas identifier.
  target_ids:
  - CHEBI:84585
  field_paths:
  - xrefs[0]
  evidence_ids:
  - owner
  - prior
  - scope-proof
  - regressions
  - native-qc
  - pubchem
  - chemistry
  - xref-table
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Implemented literal xref exclusion with complete source-row pin
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Guarded xref exclusion loader
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Versioned source compound, taxon and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and citation-level selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Grouping and claim-specific evidence emission
  rule_id: review-checklist:Equivalence; docs/CURATION.md:MIBiG chemical xref exclusions
  native_severity: major
  normalization_reason: False external equivalence is material, while this owner retains
    internally consistent ChEBI-grounded identity.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T193947Z-vibrioferrin
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/930
  disposition_reason: Resolved the false exact cross-reference through a complete-row-pinned
    exclusion of pubchem:197680 on0946 only. The source assertion remains in the unchanged
    inventory and a resolved table-owned discussion. Neither a replacement CID nor
    NPAtlas equivalence is inferred.
- finding_id: F2
  issue_key: mibig-BGC0002527-bioactivity-reference-used-for-locus
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: A compound-bioactivity citation displaces the entry-specific taxon/locus
    reference
  description: BGC0002527.2 attaches DOI10.1021/ic9016883 to siderophore bioactivity
    and retains PMID26452553 at entry level. The extractor chooses the former through
    its generic priority rule, and mibig_evidence reuses it for both the CA producer
    and CP005094.1 locus. The inspected2009 abstract concerns iron binding/photochemistry
    and marine bacteria; the2016 abstract explicitly concerns Azotobacter vibrioferrin
    and genome-based capacity. This confirms cross-claim citation selection, not a
    claim to have read either full paper or proved their every negative. Preserve
    the original database assertion and route claim-appropriate references separately.
    Full2016 evidence is still needed before assigning experimental grades or asserting
    those coordinates were tested.
  target_ids:
  - CHEBI:84585
  field_paths:
  - producer_organisms[1].evidence
  - biosynthetic_gene_clusters[1].evidence
  evidence_ids:
  - owner
  - prior
  - scope-proof
  - regressions
  - native-qc
  - mibig-BGC0002527.2
  - citation-table
  - citation-code
  - metadata
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Versioned source compound, taxon and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and citation-level selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Grouping and claim-specific evidence emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Implemented complete-source-row-pinned citation correction
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Guarded loader and claim-specific evidence routing
  rule_id: review-checklist:Evidence standard/Producer organisms/Gene clusters; nearest
    source must support the same claim
  native_severity: major
  normalization_reason: Confirmed source-transform mismatch affects material taxon/locus
    attribution. The record discloses the bioactivity level and correctly remains
    DATABASE_ASSERTION, but disclosure does not supply the missing claim-specific
    reference.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T193947Z-vibrioferrin
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/931
  disposition_reason: Resolved this2527 citation-routing defect with an implemented
    tested full-row-pinned correction. PMID26452553 remains DATABASE_ASSERTION; separate
    CURATOR_INFERENCE preserves the original activity DOI/level and decision source.
    This does not fix generic extraction for unreviewed rows, validate the full primary
    experiment or upgrade grades.
- finding_id: F3
  issue_key: chebi84585-alginolyticus-indirect-origin-citation
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The ChEBI alginolyticus origin citation is indirect, not that study's detection
    experiment
  description: The full PMID22146715 paper does mention V.alginolyticus and V.parahaemolyticus
    as previously known sources. Its experiment, however, produces structurally characterized
    vibrioferrin in E.coli from sediment clone MG93-1; the donor taxon is not established
    by the protein homology comparisons. ChEBI84585 repeats the alginolyticus origin/PMID
    pair, so the import is faithful. Treat this as indirect prior-literature support
    and trace the actual isolation/biosynthesis source. Do not infer that alginolyticus
    cannot produce vibrioferrin, delete the occurrence merely because the paper is
    indirect, or turn the metagenomic clone into an identified native producer.
  target_ids:
  - CHEBI:84585
  field_paths:
  - occurrences[1].evidence
  evidence_ids:
  - owner
  - prior
  - scope-proof
  - regressions
  - native-qc
  - chebi
  - primary2011
  - primary2007
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Source origin assertions, not editable without maintained provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Occurrence evidence emission; a new correction path needs implementation
      and tests
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
    role: Only curator-owned cited qualification through validated writer/event; never
      hand-edit seeded fields
  rule_id: review-checklist:Occurrences and narrowest claim evidence; preserve database
    assertion versus experiment
  native_severity: minor
  normalization_reason: The named organism is explicitly discussed by the source and
    the record says DATABASE_ASSERTION. The defect is weak/indirect detection provenance,
    not a confirmed false biological occurrence.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T193947Z-vibrioferrin
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/932
  disposition_reason: A cited OPEN discussion qualifies the ChEBI origin as indirect
    prior-literature context. The upstream occurrence remains unchanged; native detection
    provenance is not yet resolved and no taxon is reassigned.
- finding_id: F4
  issue_key: mibig-BGC0000946-vibrioferrin-source-strain
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: The deposited WP1 strain is missing from the producer claim
  description: AB082123.1 names V.parahaemolyticus strain WP1, but the corresponding
    BGC0000946 producer has only species-rank NCBITaxon670. The AQ3354 detection_context
    in a different ChEBI occurrence is not this accession's strain and must not be
    copied across. CA is already represented by strain-rank NCBITaxon1283330 and needs
    no inferred taxon replacement.
  target_ids:
  - CHEBI:84585
  field_paths:
  - producer_organisms[0].strain
  evidence_ids:
  - owner
  - prior
  - scope-proof
  - regressions
  - native-qc
  - strain-table
  - sequences
  - primary2007
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented complete-source-row-pinned strain qualifier
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Guarded strain qualification loader
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Versioned source compound, taxon and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and citation-level selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Grouping and claim-specific evidence emission
  rule_id: review-checklist:Producer organisms; docs/CURATION.md:MIBiG producer strain
    context
  native_severity: minor
  normalization_reason: A bounded source-strain omission with exact accession traceability
    retained.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T193947Z-vibrioferrin
    finding_id: F4
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/933
  disposition_reason: Resolved missing deposited strain context only. WP1 stays separate
    from AQ3354; MVPO1 is the GenBank literal and MVP01 the explicitly retained publisher
    spelling. No canonical spelling, strain taxid, species-wide production or evidence
    upgrade is inferred.
assessments:
- assessment_id: bounded-fixes
  area: scope
  topic: Exact-owner source corrections
  outcome: supported
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - prior
  - strain-table
  - xref-table
  - citation-table
  - scope-proof
  - regressions
  summary: Nonexact xref, claim citation routing and WP1 qualifier resolved; indirect
    occurrence provenance remains open. The field-by-field comparison preserves all
    other scientific assertions.
- assessment_id: remaining
  area: evidence
  topic: Remaining scientific uncertainty
  outcome: concern
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - owner
  - prior
  - primary2011
  - primary2007
  summary: OPEN qualifications are not completed identity or native occurrence adjudication.
    Both owners remain SEEDED and their earlier access limitations still apply.
- assessment_id: audit
  area: provenance
  topic: Immutable history and durable evidence
  outcome: supported
  target_ids:
  - CHEBI:84585
  evidence_ids:
  - prior
  - archive
  - scope-proof
  - native-qc
  summary: Original40observations remain unchanged; scoped successors retire only
    supported defects. Full campaign coverage is not inflated.
actions:
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - CHEBI:84585
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Source origin assertions, not editable without maintained provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Occurrence evidence emission; a new correction path needs implementation
      and tests
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/vibrioferrin.yaml
    role: Only curator-owned cited qualification through validated writer/event; never
      hand-edit seeded fields
  description: Trace primary native alginolyticus detection or biosynthesis evidence
    for the retained ChEBI occurrence. The OPEN indirect-citation qualification is
    already present. Do not replace its taxon with the heterologous E.coli host or
    infer the environmental donor; any generated-row correction needs its own implemented
    tested path.
  acceptance_checks:
  - Distinguish background organism mention, sequence homology, experimental host
    and natural producer.
  - Any retained direct detection citation supports the exact product and taxon.
  - Do not delete a biologically plausible occurrence merely because its current source
    is indirect.
  - Use maintained input/transform with regression tests; do not patch generated scientific
    fields.
  - 'For authorized curation: validated writer and append-only event, seeder dry run/canary,
    exact diff, strict validation, verify-corpus, verify-reproduction and full qc.'
  - Retain raw source assertions, taxon IDs, source versions and independent producer/locus
    evidence grades.
limitations:
- Scoped partial disposition only; no newly assessed owner and no full scientific
  sign-off.
- All predecessor primary and authority access limitations remain. No alternate retrieval
  after denial.
- Full QC preceded saving these successors; canonical append-only checks and contract
  tests follow saving.
- Exact inspected commit is retained by review-base/vibrioferrin-remediation-20261013.
- Generic extractor citation selection for other unreviewed rows remains unchanged;
  the new correction is explicitly source-scoped.
- The campaign retains3088unassessed owners and26partial assessments;1historical completed
  full assessment is not native REVIEWED promotion.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261013T193947Z-vibrioferrin
  relationship: Scoped disposition of exact predecessor findings; immutable whole-record
    assessment retained.
links:
- https://github.com/CultureBotAI/NaturalProductMech/pull/928
```
