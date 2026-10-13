# gentamicin-2: scoped source-defect disposition

- Review: 20261013T222146Z-gentamicin-2-scoped-disposition
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T22:21:44.796862Z
- Finished UTC: 2026-10-13T22:21:46.775362Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Confirmed source defects resolved within exact scope; product-identity assignment remains open.

## Scope And Provenance

One exact owner; scoped finding disposition, not another full-owner assessment.

Selection: User-authorized issue remediation and PR publication.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 232d46bacaa6e70ca9f309cb22aae3b1585c4a3c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-b697ac65fb | data/natural_products/carbohydrates/gentamicin-2.yaml | generated | gentamicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| publish-focused | passed | True | naturalproductmech:mibig-b697ac65fb | Actual execution 2026-10-13T22:20:43.197067Z to 2026-10-13T22:21:10.556897Z, exit0. Deterministic check, not scientific completion. |
| publish-strict | passed | True | naturalproductmech:mibig-b697ac65fb | Actual execution 2026-10-13T22:20:44.353448Z to 2026-10-13T22:20:47.691779Z, exit0. Deterministic check, not scientific completion. |
| publish-scope | passed | True | naturalproductmech:mibig-b697ac65fb | Actual execution 2026-10-13T22:20:42.036790Z to 2026-10-13T22:20:43.429841Z, exit0. Deterministic check, not scientific completion. |
| Exact-product primary-source closure | unavailable | True | naturalproductmech:mibig-b697ac65fb | All predecessor access limitations persist. No new retrieval or exact-congener adjudication in this scoped disposition. |

## Scientific And Domain Assessments

### Scoped maintained-input corrections

provenance: supported. Targets: naturalproductmech:mibig-b697ac65fb.

Guarded regeneration preserves exact identities, original assertions and grades while correcting reviewed context and nonexact source claims.

### Unresolved exact-product assignment

identity: concern. Targets: naturalproductmech:mibig-b697ac65fb.

OPEN qualification is not identity adjudication. Native SEEDED and all original source-access limits remain.

## Findings

### F1: Generic gentamicin name obscures the X2 precursor and unresolved stereochemical scope

major / open / confirmed; issue key: gentamicin-2-exact-product-assignment.

HFLK connectivity matches the X2 candidate, not the clinically used C complex. Both the2015cited abstract and2004Figure3 distinguish that precursor. No specific congener label or qualification is present. Exact stereochemical and experimental strain attribution remain incomplete; this is not a demand to invent stereo or evidence grades.

Disposition: Cited OPEN discussion mitigates the ambiguity. Exact product/congener and stereochemical assignment remain unresolved under issue941; no structure migration, merge or REVIEWED promotion.

### F2: Producer omits the deposited strain qualification

minor / resolved / confirmed; issue key: gentamicin-2-deposited-strain-context.

KY971520.1 source feature supplies ATCC 15835, whereas the record gives only species1877. DSMZ lists DSM43036 andATCC15835 as equivalent collection numbers; this is lost context, not evidence of mismatched strains. A strain qualification alone does not prove this exact metabolite is produced.

Disposition: Deposited literal strain is preserved through complete-row-pinned qualification and guarded seeding. Original species and database tier remain unchanged. Resolves only missing context (issue944).

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the exact congener against primary structure evidence and source-version provenance. Preserve the raw generic label, then implement a tested maintained qualification or correction path for the reviewed product. Do not merge the two owners, transfer mixture claims, replace with a stereo-different CID, or use reserved decisions.tsv. A source correction requiring a non-ChEBI destination needs separately implemented ownership/migration logic.

- Primary evidence resolves named congener and supported stereochemical resolution.
- Every producer, occurrence, xref and assay is re-audited for the selected exact structure.
- Future tests prove no silent same-name merge or transfer between BDTQ and HFLK; reproduction and native gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| chemistry | /private/tmp/npmech-gentamicin-review-c2YN3q/inspection.json; records chemistry; structures.png visually inspected | supports | Pinned RDKit2026.03.5 roundtrips both SMILES to their recorded InChI and key. HFLKNINDVFJPQT has C19H38N4O10 and14 unassigned centers; BDTQHFBWYNCGHN has C18H36N4O10 and14 assigned centers. Both neutral. Internal agreement does not establish biological identity. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/72396,15574862/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; Official properties for both CIDs; original retrieval 2026-10-13T22:00:44.082843Z..2026-10-13T22:00:44.942044Z, HTTP 200; payload /private/tmp/npmech-gentamicin-review-c2YN3q/pubchem.json; receipt SHA256 812b00d278a1488738eedbd671c8247ecfd20b609b2e30917aab4f906cbc8f6d. accessed_at records local reinspection. | supports | CID72396 is VEGXETMJINRLTH-BOZYPMBZSA-N/C19H39N5O7, not the BDTQ owner. CID15574862 is HFLKNINDVFJPQT-ZFAMMYHGSA-N/C19H38N4O10; it shares connectivity, not stereochemical identity, with the HFLK owner. |
| pubchem-a3 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/86490/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; CID86490 properties; original retrieval 2026-10-13T22:03:22.935227Z..2026-10-13T22:03:23.454929Z, HTTP 200; payload /private/tmp/npmech-gentamicin-review-c2YN3q/pubchem-A3.json; receipt SHA256 69be490e975e8cba3223ef6641f1cbe0e82a03f436469c589e6223c0fedd1eb5. accessed_at records local reinspection. | supports | CID86490 has BDTQHFBWYNCGHN-UHFFFAOYSA-N: connectivity matches the BDTQ owner but stereo does not. It is a candidate for identity research, not an exact replacement xref. |
| sequences | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=AJ628149.4,KY971520.1&amp;rettype=gbwithparts&amp;retmode=xml; Source features and references of both exact accession versions; original retrieval 2026-10-13T22:00:45.134607Z..2026-10-13T22:00:45.780343Z, HTTP 200; payload /private/tmp/npmech-gentamicin-review-c2YN3q/sequences.xml; receipt SHA256 8f1094d122aa9f5c2bc866a600cb21e210eb4e038e8637b63d30b8e08dded1a4. accessed_at records local reinspection. | supports | AJ628149.4 is deposited with strain DSM43036; KY971520.1 with ATCC15835 and culture_collection ATCC:15835. Both use taxon1877 and have unpublished/direct-submission references. The deposits establish sequence context, not the experimental identity of a product. |
| primary2004 | https://www.jstage.jst.go.jp/article/antibiotics1968/57/7/57_7_436/_pdf/-char/en; DOI10.7164/antibiotics.57.436, all ten pages text inspected; Table1 p437, Figure2 p442 and Figure3 p443 visually inspected; original retrieval 2026-10-13T22:00:54.909277Z..2026-10-13T22:00:58.396615Z, HTTP 200; payload /private/tmp/npmech-gentamicin-review-c2YN3q/primary2004.pdf; receipt SHA256 695767ce0bc23d65185cd4c50e897d8fd5ad18f2839bf2c292f3b69df817e29f. accessed_at records local reinspection. | supports | Unwin et al. study the gentamicin C complex in ATCC15835 using a gntB insertion and an immunoassay. The deposited sequence named in Methods is AY524043. Figure3 distinguishes A/A2/X2 intermediates from C congeners; it presents predicted enzyme assignments. This does not identify the BDTQ graph as their measured product. |
| dsmz | https://webshop.dsmz.de/en/bacteria/Micromonospora-echinospora-subsp-echinospora-oxid-2.html; DSM No. and Other collection no.; official web page inspected during this review; accessed_at is reinspection of returned source text | supports | DSMZ explicitly lists ATCC15835 among the equivalent collection numbers for DSM43036. Different collection labels therefore do not prove different strains. Different sequence deposits still need exact locus mapping. |
| np-atlas | https://www.npatlas.org/api/v1/compound/NPA009026?include=classifications; Official export linked from compound page; inchikey/inchi/smiles/formula, origin and mol_structures; version2024_09. Returned API text reinspected; not redistributed. | supports | NPA009026 (resolving the shorter NPA09026 alias) exactly matches BDTQHFBWYNCGHN-CUYCKOLISA-N and its molecular formula. The origin is Micromonospora sp. and DOI10.1021/jm00340a034. Exact database agreement is retained; it does not validate the historical assignment to the complex. |
| primary2015-abstract | https://hero.epa.gov/reference/7214436/; Huang et al., PMID25641167, DOI10.1016/j.chembiol.2014.12.012; primary abstract reproduced by EPA HERO. PubMed page displayed reCAPTCHA; no challenge bypass or full-paper retrieval. | partial | The reproduced primary abstract identifies gentamicin X2 as a precursor of the C complex and reports native mutations plus enzyme reconstitution. Only that abstract was inspected; the paper, figures, supplements and exact experimental strain were not verified. |
| assay | https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1195/JSON?cid=72396; PC_AssaySubmit.assay.descr.protocol/results and data[0]; original dose units retained in source, not converted to MIC; original retrieval 2026-10-13T22:01:13.729676Z..2026-10-13T22:01:14.195513Z, HTTP 200; payload /private/tmp/npmech-gentamicin-review-c2YN3q/assay1195-cid72396.json; receipt SHA256 4e0949e9625ee728f4707bdd638627902199679984cb91653374c4d2160bd8f0. accessed_at records local reinspection. | supports | AID1195 assigns Active to every substance with a reported maximum recommended daily dose. The CID72396 query returns SID48416051 and dose metadata, not a pure-BDTQ-compound assay. This administrative outcome is not positive biological activity. |
| current | data/natural_products/carbohydrates/gentamicin-2.yaml | supports | Complete current owner and diff inspected: deposited context and OPEN product qualification; BDTQ also withholds nonexact CID72396 and AID1195. No chemistry, grade or status promotion. |
| prior | reviews/structured/20261013T221636Z-gentamicin-2/review.yaml | supports | Immutable full-owner partial assessment; source limitations and original findings remain historical evidence. |
| strains | curation/mibig_producer_strains.tsv | supports | Two exact source-row-pinned deposited qualifiers; no experiment or product assertion inferred from a sequence feature. |
| xrefs | curation/mibig_xref_exclusions.tsv | supports | Only CID72396 is excluded from the BDTQ owner; exact NPAtlas equivalence retained. |
| assay-decision | curation/pubchem_bioassay_exclusions.tsv | supports | One complete historical row is withheld with protocol citation and independent CID mismatch rationale. The other 23 AID1195 rows and future importer policy are separate issue945. |
| scope | /private/tmp/npmech-gentamicin-publish-gxrmx8/scope-audit.json | supports | All3115owners,243components and48prior review pairs verified; only two owners changed within authorized fields. |
| publish-focused | /private/tmp/npmech-gentamicin-review-c2YN3q/publish-focused.log | supports | Actual execution 2026-10-13T22:20:43.197067Z to 2026-10-13T22:21:10.556897Z, exit0. Deterministic check, not scientific completion. |
| publish-strict | /private/tmp/npmech-gentamicin-review-c2YN3q/publish-strict.log | supports | Actual execution 2026-10-13T22:20:44.353448Z to 2026-10-13T22:20:47.691779Z, exit0. Deterministic check, not scientific completion. |
| publish-scope | /private/tmp/npmech-gentamicin-review-c2YN3q/publish-scope.log | supports | Actual execution 2026-10-13T22:20:42.036790Z to 2026-10-13T22:20:43.429841Z, exit0. Deterministic check, not scientific completion. |

## Limits And Additional Notes

- Scoped disposition only; no additional owner coverage or native REVIEWED promotion.
- No new primary retrieval. All predecessor source-access limitations remain; no access bypass.
- Current working-tree input hashes are attestations, not a claim these bytes existed at the base commit.
- Only recorded focused/strict/scope checks are asserted here. Final full QC, review contract checks and CI follow before merge.
- Initial draft serialization/search-scope/check-status errors and two test-fixture failures were corrected before this observation; failed test receipts are retained.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T222146Z-gentamicin-2-scoped-disposition
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'gentamicin-2: scoped source-defect disposition'
started_at: '2026-10-13T22:21:44.796862Z'
finished_at: '2026-10-13T22:21:46.775362Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Implementing assistant performing a separate adversarial pass;
    not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Confirmed source defects resolved within exact scope; product-identity assignment
  remains open.
source:
  git_revision: 232d46bacaa6e70ca9f309cb22aae3b1585c4a3c
  state: working_tree
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
  - path: curation/mibig_claim_references.tsv
    sha256: f3f808ad1e58d79947aa82ecf1272e465cfbef57e5a4cd646731af23bb48ce75
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: a1eb14fec4a7cee0c2fc25c43091e75af24ae62c44c4f7659ed7aedf0e6a0e6c
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 6f879bb9f2c9be6b6e8de8c013dbaebe09075b7e106790ea303a17006761ea11
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: f61d7ba85ffd21837cd2b625f83c4681c4663e72503466b40eba3f4ab0204bc1
    role: context
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 18b61c1e5a69112c99cea1373791cd1ec571b7084bfd9198ab68fa551f5d531a
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/carbohydrates/gentamicin-2.yaml
    sha256: 312651cca89fb24beeb8da8adfc42e42f513d55072b52176d79a34e30f53edad
    role: target
  - path: data/natural_products/carbohydrates/gentamicin.yaml
    sha256: 27df7d729218f2daaa46aa64271f799db1c558caf7bfac26688aab63d9bdf123
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
    sha256: 17619dbf804fe07f90811b2cc1e5bd330299853b9677c07b49781ce904d9e28a
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
  - path: reviews/structured/20261013T221636Z-gentamicin-2/review.yaml
    sha256: a05eafd39edc330a337a9269e8868cf10053a23719204c9023a86f4dc8f13250
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
  - path: scripts/extract_pubchem_bioassay.py
    sha256: 24f9d794e7cf97c420351cb751f8767f7d81a5f22aed01669b2318d6755e7c00
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/run_qc.py
    sha256: ff44ed3e40a9b3582eb84e38a81301745ae80d16445756d09a7efb2a480b1abb
    role: context
  - path: scripts/seed_from_sources.py
    sha256: da98c0acf5b3cb14dd59e5b8ab905cec2364323be0814d297b356cbb257a9428
    role: context
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
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
  - path: tests/test_bioassay_exclusions.py
    sha256: 099a0b8f6f51ce93406344440b63d99db7203486ed92797d90990005bdb6bbd0
    role: context
  - path: tests/test_gentamicin_curation.py
    sha256: 7330dacb16aace87281368b0801eed5988ad90970a22152072368effe81976ff
    role: context
  - path: uv.lock
    sha256: c62a5739e3ffeb12cc57b3bf12a31dcf9cdfbf00b417f4ba3a801d51ef9efbe3
    role: context
targets:
- target_id: naturalproductmech:mibig-b697ac65fb
  path: data/natural_products/carbohydrates/gentamicin-2.yaml
  label: gentamicin
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
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Imported compound-specific assay observations
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_pubchem_bioassay.py
    role: BioAssay extraction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Scoped assay remediation input or regression
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Scoped assay remediation input or regression
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_bioassay_exclusions.py
    role: Scoped assay remediation input or regression
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_gentamicin_curation.py
    role: Scoped assay remediation input or regression
scope:
  description: One exact owner; scoped finding disposition, not another full-owner
    assessment.
  selection: User-authorized issue remediation and PR publication.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-b697ac65fb
checks:
- check_id: publish-focused
  name: publish-focused
  status: passed
  required: true
  command: uv run pytest -q tests/test_bioassay_exclusions.py tests/test_gentamicin_curation.py
    tests/test_xref_exclusions.py tests/test_producer_strains.py tests/test_structure_corrections.py
    tests/test_seed_skeleton.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-b697ac65fb
  evidence_ids:
  - publish-focused
  summary: Actual execution 2026-10-13T22:20:43.197067Z to 2026-10-13T22:21:10.556897Z,
    exit0. Deterministic check, not scientific completion.
- check_id: publish-strict
  name: publish-strict
  status: passed
  required: true
  command: just validate-strict data/natural_products/carbohydrates/gentamicin.yaml
    data/natural_products/carbohydrates/gentamicin-2.yaml --out /private/tmp/npmech-gentamicin-publish-gxrmx8/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-b697ac65fb
  evidence_ids:
  - publish-strict
  summary: Actual execution 2026-10-13T22:20:44.353448Z to 2026-10-13T22:20:47.691779Z,
    exit0. Deterministic check, not scientific completion.
- check_id: publish-scope
  name: publish-scope
  status: passed
  required: true
  command: uv run python /private/tmp/npmech-gentamicin-publish-gxrmx8/scope_audit.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-b697ac65fb
  evidence_ids:
  - publish-scope
  summary: Actual execution 2026-10-13T22:20:42.036790Z to 2026-10-13T22:20:43.429841Z,
    exit0. Deterministic check, not scientific completion.
- check_id: primary-remaining
  name: Exact-product primary-source closure
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b697ac65fb
  summary: All predecessor access limitations persist. No new retrieval or exact-congener
    adjudication in this scoped disposition.
evidence:
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-gentamicin-review-c2YN3q/inspection.json
  locator: records chemistry; structures.png visually inspected
  accessed_at: '2026-10-13T22:16:34.050199Z'
  support: supports
  summary: Pinned RDKit2026.03.5 roundtrips both SMILES to their recorded InChI and
    key. HFLKNINDVFJPQT has C19H38N4O10 and14 unassigned centers; BDTQHFBWYNCGHN has
    C18H36N4O10 and14 assigned centers. Both neutral. Internal agreement does not
    establish biological identity.
  snapshot_sha256: 47fb0302f9b214192dfdc03dfa5bc8918bd8db6c5c2748e6410fdd0a859139d5
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/72396,15574862/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: Official properties for both CIDs; original retrieval 2026-10-13T22:00:44.082843Z..2026-10-13T22:00:44.942044Z,
    HTTP 200; payload /private/tmp/npmech-gentamicin-review-c2YN3q/pubchem.json; receipt
    SHA256 812b00d278a1488738eedbd671c8247ecfd20b609b2e30917aab4f906cbc8f6d. accessed_at
    records local reinspection.
  accessed_at: '2026-10-13T22:16:34.050641Z'
  support: supports
  summary: CID72396 is VEGXETMJINRLTH-BOZYPMBZSA-N/C19H39N5O7, not the BDTQ owner.
    CID15574862 is HFLKNINDVFJPQT-ZFAMMYHGSA-N/C19H38N4O10; it shares connectivity,
    not stereochemical identity, with the HFLK owner.
  snapshot_sha256: b61555527d3e752c2a5a48467eebad9b34ff8ed1bf3b9c2b929f47c5e37d12bf
- evidence_id: pubchem-a3
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/86490/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: CID86490 properties; original retrieval 2026-10-13T22:03:22.935227Z..2026-10-13T22:03:23.454929Z,
    HTTP 200; payload /private/tmp/npmech-gentamicin-review-c2YN3q/pubchem-A3.json;
    receipt SHA256 69be490e975e8cba3223ef6641f1cbe0e82a03f436469c589e6223c0fedd1eb5.
    accessed_at records local reinspection.
  accessed_at: '2026-10-13T22:16:34.050897Z'
  support: supports
  summary: 'CID86490 has BDTQHFBWYNCGHN-UHFFFAOYSA-N: connectivity matches the BDTQ
    owner but stereo does not. It is a candidate for identity research, not an exact
    replacement xref.'
  snapshot_sha256: 5b3ebf3c1f72b6938f0d37910ef6d75f87d639d46be87835e89eb2add0fd1018
- evidence_id: sequences
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AJ628149.4,KY971520.1&rettype=gbwithparts&retmode=xml
  locator: Source features and references of both exact accession versions; original
    retrieval 2026-10-13T22:00:45.134607Z..2026-10-13T22:00:45.780343Z, HTTP 200;
    payload /private/tmp/npmech-gentamicin-review-c2YN3q/sequences.xml; receipt SHA256
    8f1094d122aa9f5c2bc866a600cb21e210eb4e038e8637b63d30b8e08dded1a4. accessed_at
    records local reinspection.
  accessed_at: '2026-10-13T22:16:34.051646Z'
  support: supports
  summary: AJ628149.4 is deposited with strain DSM43036; KY971520.1 with ATCC15835
    and culture_collection ATCC:15835. Both use taxon1877 and have unpublished/direct-submission
    references. The deposits establish sequence context, not the experimental identity
    of a product.
  snapshot_sha256: 701076e79da9eb1c73dc29f60dceb636e8d6b9d9f2e38ac9e044bac8b0a54498
- evidence_id: primary2004
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/antibiotics1968/57/7/57_7_436/_pdf/-char/en
  locator: DOI10.7164/antibiotics.57.436, all ten pages text inspected; Table1 p437,
    Figure2 p442 and Figure3 p443 visually inspected; original retrieval 2026-10-13T22:00:54.909277Z..2026-10-13T22:00:58.396615Z,
    HTTP 200; payload /private/tmp/npmech-gentamicin-review-c2YN3q/primary2004.pdf;
    receipt SHA256 695767ce0bc23d65185cd4c50e897d8fd5ad18f2839bf2c292f3b69df817e29f.
    accessed_at records local reinspection.
  accessed_at: '2026-10-13T22:16:34.052863Z'
  support: supports
  summary: Unwin et al. study the gentamicin C complex in ATCC15835 using a gntB insertion
    and an immunoassay. The deposited sequence named in Methods is AY524043. Figure3
    distinguishes A/A2/X2 intermediates from C congeners; it presents predicted enzyme
    assignments. This does not identify the BDTQ graph as their measured product.
  snapshot_sha256: 8a4e6efbb5bb223ec82117a68afaab45b1ae9e9597e907a6f1309597858956f5
- evidence_id: dsmz
  kind: authority
  reference: https://webshop.dsmz.de/en/bacteria/Micromonospora-echinospora-subsp-echinospora-oxid-2.html
  locator: DSM No. and Other collection no.; official web page inspected during this
    review; accessed_at is reinspection of returned source text
  accessed_at: '2026-10-13T22:16:34.056933Z'
  support: supports
  summary: DSMZ explicitly lists ATCC15835 among the equivalent collection numbers
    for DSM43036. Different collection labels therefore do not prove different strains.
    Different sequence deposits still need exact locus mapping.
- evidence_id: np-atlas
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA009026?include=classifications
  locator: Official export linked from compound page; inchikey/inchi/smiles/formula,
    origin and mol_structures; version2024_09. Returned API text reinspected; not
    redistributed.
  accessed_at: '2026-10-13T22:16:34.056946Z'
  support: supports
  summary: NPA009026 (resolving the shorter NPA09026 alias) exactly matches BDTQHFBWYNCGHN-CUYCKOLISA-N
    and its molecular formula. The origin is Micromonospora sp. and DOI10.1021/jm00340a034.
    Exact database agreement is retained; it does not validate the historical assignment
    to the complex.
- evidence_id: primary2015-abstract
  kind: primary_source
  reference: https://hero.epa.gov/reference/7214436/
  locator: Huang et al., PMID25641167, DOI10.1016/j.chembiol.2014.12.012; primary
    abstract reproduced by EPA HERO. PubMed page displayed reCAPTCHA; no challenge
    bypass or full-paper retrieval.
  accessed_at: '2026-10-13T22:16:34.056951Z'
  support: partial
  summary: The reproduced primary abstract identifies gentamicin X2 as a precursor
    of the C complex and reports native mutations plus enzyme reconstitution. Only
    that abstract was inspected; the paper, figures, supplements and exact experimental
    strain were not verified.
- evidence_id: assay
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1195/JSON?cid=72396
  locator: PC_AssaySubmit.assay.descr.protocol/results and data[0]; original dose
    units retained in source, not converted to MIC; original retrieval 2026-10-13T22:01:13.729676Z..2026-10-13T22:01:14.195513Z,
    HTTP 200; payload /private/tmp/npmech-gentamicin-review-c2YN3q/assay1195-cid72396.json;
    receipt SHA256 4e0949e9625ee728f4707bdd638627902199679984cb91653374c4d2160bd8f0.
    accessed_at records local reinspection.
  accessed_at: '2026-10-13T22:16:34.058254Z'
  support: supports
  summary: AID1195 assigns Active to every substance with a reported maximum recommended
    daily dose. The CID72396 query returns SID48416051 and dose metadata, not a pure-BDTQ-compound
    assay. This administrative outcome is not positive biological activity.
  snapshot_sha256: 6fa650fd1bff8ceb6715b56ca6b321f403c68a93ff117b7298d5a80a3550b50a
- evidence_id: current
  kind: record_content
  reference: data/natural_products/carbohydrates/gentamicin-2.yaml
  accessed_at: '2026-10-13T22:21:46.773191Z'
  support: supports
  summary: 'Complete current owner and diff inspected: deposited context and OPEN
    product qualification; BDTQ also withholds nonexact CID72396 and AID1195. No chemistry,
    grade or status promotion.'
  snapshot_sha256: 312651cca89fb24beeb8da8adfc42e42f513d55072b52176d79a34e30f53edad
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261013T221636Z-gentamicin-2/review.yaml
  accessed_at: '2026-10-13T22:21:46.773323Z'
  support: supports
  summary: Immutable full-owner partial assessment; source limitations and original
    findings remain historical evidence.
  snapshot_sha256: a05eafd39edc330a337a9269e8868cf10053a23719204c9023a86f4dc8f13250
- evidence_id: strains
  kind: record_content
  reference: curation/mibig_producer_strains.tsv
  accessed_at: '2026-10-13T22:21:46.773545Z'
  support: supports
  summary: Two exact source-row-pinned deposited qualifiers; no experiment or product
    assertion inferred from a sequence feature.
  snapshot_sha256: 6f879bb9f2c9be6b6e8de8c013dbaebe09075b7e106790ea303a17006761ea11
- evidence_id: xrefs
  kind: record_content
  reference: curation/mibig_xref_exclusions.tsv
  accessed_at: '2026-10-13T22:21:46.773666Z'
  support: supports
  summary: Only CID72396 is excluded from the BDTQ owner; exact NPAtlas equivalence
    retained.
  snapshot_sha256: f61d7ba85ffd21837cd2b625f83c4681c4663e72503466b40eba3f4ab0204bc1
- evidence_id: assay-decision
  kind: record_content
  reference: curation/pubchem_bioassay_exclusions.tsv
  accessed_at: '2026-10-13T22:21:46.773761Z'
  support: supports
  summary: One complete historical row is withheld with protocol citation and independent
    CID mismatch rationale. The other 23 AID1195 rows and future importer policy are
    separate issue945.
  snapshot_sha256: 18b61c1e5a69112c99cea1373791cd1ec571b7084bfd9198ab68fa551f5d531a
- evidence_id: scope
  kind: validation
  reference: /private/tmp/npmech-gentamicin-publish-gxrmx8/scope-audit.json
  accessed_at: '2026-10-13T22:21:46.773868Z'
  support: supports
  summary: All3115owners,243components and48prior review pairs verified; only two
    owners changed within authorized fields.
  snapshot_sha256: 79d09ede1bda0fb7367f3e5a8241c5bcf8a820e86d9ef777a31b1ec0db4f9a85
- evidence_id: publish-focused
  kind: validation
  reference: /private/tmp/npmech-gentamicin-review-c2YN3q/publish-focused.log
  accessed_at: '2026-10-13T22:21:46.774246Z'
  support: supports
  summary: Actual execution 2026-10-13T22:20:43.197067Z to 2026-10-13T22:21:10.556897Z,
    exit0. Deterministic check, not scientific completion.
  snapshot_sha256: ed7eb4685bf844c6fe67f089c0b75f2029c953ef53d598622910fd33e2b6ac3b
- evidence_id: publish-strict
  kind: validation
  reference: /private/tmp/npmech-gentamicin-review-c2YN3q/publish-strict.log
  accessed_at: '2026-10-13T22:21:46.774778Z'
  support: supports
  summary: Actual execution 2026-10-13T22:20:44.353448Z to 2026-10-13T22:20:47.691779Z,
    exit0. Deterministic check, not scientific completion.
  snapshot_sha256: 0a7bcf69659b3ac40ea2bafcb85bd213fbb1b7531ae23c715f060fb8295dad86
- evidence_id: publish-scope
  kind: validation
  reference: /private/tmp/npmech-gentamicin-review-c2YN3q/publish-scope.log
  accessed_at: '2026-10-13T22:21:46.775092Z'
  support: supports
  summary: Actual execution 2026-10-13T22:20:42.036790Z to 2026-10-13T22:20:43.429841Z,
    exit0. Deterministic check, not scientific completion.
  snapshot_sha256: 79d09ede1bda0fb7367f3e5a8241c5bcf8a820e86d9ef777a31b1ec0db4f9a85
findings:
- finding_id: F1
  issue_key: gentamicin-2-exact-product-assignment
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Generic gentamicin name obscures the X2 precursor and unresolved stereochemical
    scope
  description: HFLK connectivity matches the X2 candidate, not the clinically used
    C complex. Both the2015cited abstract and2004Figure3 distinguish that precursor.
    No specific congener label or qualification is present. Exact stereochemical and
    experimental strain attribution remain incomplete; this is not a demand to invent
    stereo or evidence grades.
  target_ids:
  - naturalproductmech:mibig-b697ac65fb
  field_paths:
  - label
  - chemical_structure
  - producer_organisms
  - biosynthetic_gene_clusters
  evidence_ids:
  - current
  - prior
  - scope
  - publish-focused
  - chemistry
  - pubchem
  - primary2004
  rule_id: 'NaturalProductRecord checklist: identity'
  native_severity: major
  normalization_reason: A materially ambiguous or unsupported identity/evidence claim
    requires correction before scientific sign-off.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source-specific compound naming and structure extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Exact-key grouping and generated identity
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned source assertion; do not rewrite without reviewed provenance
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T221636Z-gentamicin-2
    finding_id: F1
  disposition_reason: Cited OPEN discussion mitigates the ambiguity. Exact product/congener
    and stereochemical assignment remain unresolved under issue941; no structure migration,
    merge or REVIEWED promotion.
- finding_id: F2
  issue_key: gentamicin-2-deposited-strain-context
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Producer omits the deposited strain qualification
  description: KY971520.1 source feature supplies ATCC 15835, whereas the record gives
    only species1877. DSMZ lists DSM43036 andATCC15835 as equivalent collection numbers;
    this is lost context, not evidence of mismatched strains. A strain qualification
    alone does not prove this exact metabolite is produced.
  target_ids:
  - naturalproductmech:mibig-b697ac65fb
  field_paths:
  - producer_organisms[0].strain
  evidence_ids:
  - current
  - prior
  - scope
  - publish-focused
  - sequences
  - strains
  - dsmz
  rule_id: 'NaturalProductRecord checklist: provenance'
  native_severity: minor
  normalization_reason: Bounded provenance loss; repairing it does not resolve the
    independent exact-product question.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented complete-row-pinned producer-strain qualifications
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T221636Z-gentamicin-2
    finding_id: F2
  disposition_reason: Deposited literal strain is preserved through complete-row-pinned
    qualification and guarded seeding. Original species and database tier remain unchanged.
    Resolves only missing context (issue944).
assessments:
- assessment_id: fixed
  area: provenance
  topic: Scoped maintained-input corrections
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-b697ac65fb
  evidence_ids:
  - current
  - strains
  - xrefs
  - assay-decision
  - scope
  - publish-focused
  summary: Guarded regeneration preserves exact identities, original assertions and
    grades while correcting reviewed context and nonexact source claims.
- assessment_id: identity-open
  area: identity
  topic: Unresolved exact-product assignment
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-b697ac65fb
  evidence_ids:
  - current
  - prior
  - chemistry
  - primary2004
  summary: OPEN qualification is not identity adjudication. Native SEEDED and all
    original source-access limits remain.
actions:
- action_id: A1
  description: Adjudicate the exact congener against primary structure evidence and
    source-version provenance. Preserve the raw generic label, then implement a tested
    maintained qualification or correction path for the reviewed product. Do not merge
    the two owners, transfer mixture claims, replace with a stereo-different CID,
    or use reserved decisions.tsv. A source correction requiring a non-ChEBI destination
    needs separately implemented ownership/migration logic.
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-b697ac65fb
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source-specific compound naming and structure extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Exact-key grouping and generated identity
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned source assertion; do not rewrite without reviewed provenance
  acceptance_checks:
  - Primary evidence resolves named congener and supported stereochemical resolution.
  - Every producer, occurrence, xref and assay is re-audited for the selected exact
    structure.
  - Future tests prove no silent same-name merge or transfer between BDTQ and HFLK;
    reproduction and native gates pass.
  generator: 'Authorized curation only: maintained input change, canary seeding and
    guarded writer with history; then just verify-reproduction, just render and just
    qc. No changes made by this review.'
limitations:
- Scoped disposition only; no additional owner coverage or native REVIEWED promotion.
- No new primary retrieval. All predecessor source-access limitations remain; no access
  bypass.
- Current working-tree input hashes are attestations, not a claim these bytes existed
  at the base commit.
- Only recorded focused/strict/scope checks are asserted here. Final full QC, review
  contract checks and CI follow before merge.
- Initial draft serialization/search-scope/check-status errors and two test-fixture
  failures were corrected before this observation; failed test receipts are retained.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261013T221636Z-gentamicin-2
  relationship: Exact predecessor; scoped findings disposition.
```
