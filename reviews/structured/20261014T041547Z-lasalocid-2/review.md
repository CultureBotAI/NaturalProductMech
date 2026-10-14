# lasalocid-2: exact-owner scientific review

- Review: 20261014T041547Z-lasalocid-2
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-14T03:58:11.233622Z
- Finished UTC: 2026-10-14T04:15:47.631253Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Stored chemistry is internally consistent. An unrepresented strain-source conflict prevents exact locus attribution.

## Scope And Provenance

Whole exact owner, complete resolved mechanism view, pinned inventories and bounded primary/database checks.

Selection: Next exact owner in the3115-record campaign; same-name sibling assessed separately.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 64c095104e5352fb88ad3177c47995ccfd4275d5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-73ba44dafe | data/natural_products/polyketides/lasalocid-2.yaml | generated | lasalocid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict | passed | True | naturalproductmech:mibig-73ba44dafe | Passed within actual recorded scope. |
| labels | passed | True | naturalproductmech:mibig-73ba44dafe | Passed with499 existing nonblocking mismatches and4647 no-adapter skips; not universal ontology verification. |
| qc | passed | True | naturalproductmech:mibig-73ba44dafe | Passed within actual recorded scope. |
| queue | passed | True | naturalproductmech:mibig-73ba44dafe | Passed within actual recorded scope. |
| chemistry-pinned | passed | True | naturalproductmech:mibig-73ba44dafe | Passed within actual recorded scope. |
| crosschecks | passed | True | naturalproductmech:mibig-73ba44dafe | Passed within actual recorded scope. |
| imodulondb | passed | False | naturalproductmech:mibig-73ba44dafe | Dataset listing succeeded; no applicable native-producer dataset. |
| Initial repository chemistry-extra attempt | failed | False | naturalproductmech:mibig-73ba44dafe | Pinned RDKit has no wheel for this macOS x86_64 platform. Replaced by successful existing exact-version environment; no dependency change. |
| Primary exact-form and strain/locus closure | unavailable | True | naturalproductmech:mibig-73ba44dafe | Some primary full texts inaccessible; original stereochemistry, salt processing and disputed strain attribution not fully adjudicated. No bypass. |

## Scientific And Domain Assessments

### Exact structure and same-name boundary

identity: supported. Targets: naturalproductmech:mibig-73ba44dafe.

Faithful unspecified sodium-salt encoding; PubChem matches and stereo_complete:false is honest. Do not merge with the free acid or invent stereochemistry.

### Primary identity resolution

evidence: unknown. Targets: naturalproductmech:mibig-73ba44dafe.

Database agreement does not independently certify the biological product at every stereocenter or establish processing/counterion state. No structure replacement or owner migration proposed as automatic.

### Producer strain and evidence tier

scope: concern. Targets: naturalproductmech:mibig-73ba44dafe.

Species-level database assertions retain cautious grades, but exact strain context is omitted and the AB449340 deposit conflicts with its primary paper.

### BGC activity, locus and primary support

evidence: concern. Targets: naturalproductmech:mibig-73ba44dafe.

Both active entries reproduce. Empty source methods do not deny published experiments; any overrides require exact strain/form adjudication, and purified enzyme activity does not upgrade the native producer.

### Independent classification facets

representation: supported. Targets: naturalproductmech:mibig-73ba44dafe.

POLYKETIDES and polyether subclasses remain versioned NPClassifier output; PKS is a cluster assertion; ACTINOBACTERIAL is taxonomic. NATURAL_PRODUCT reflects the origin assertion, not a claim that all experimental strains are unmodified.

### Occurrence versus production

scope: not_applicable. Targets: naturalproductmech:mibig-73ba44dafe.

No occurrences are asserted on this owner; no free-acid claims are transferred.

### Activity and sibling ownership

provenance: not_applicable. Targets: naturalproductmech:mibig-73ba44dafe.

No native assay, target or summary is asserted; the raw no-data sentinel is not negative efficacy evidence.

### Pathway and graph completeness

graph: not_applicable. Targets: naturalproductmech:mibig-73ba44dafe.

No native pathway, graph or protein example is declared. Missing optional mechanisms are not false assertions; a future graph must distinguish prediction, enzyme conversion and native deletion experiments.

### Generated boundaries and history

ownership: supported. Targets: naturalproductmech:mibig-73ba44dafe.

Native SEEDED status and both seed-history events remain unchanged. Proposed fixes name maintained tables or guarded curator discussions; curation/decisions.tsv is reserved and is not an effective fix path.

## Findings

### strain-conflict: AB449340 strain conflict is unrepresented in the native record

major / open / confirmed; issue key: lasalocid-bgc0000086-strain-provenance-conflict.

The source deposit names ATCC31180 while the inspected study assigns AB449340 to ATCC35851. The owner has neither strain nor a discussion of this conflict. Preserve both assertions before grade changes; do not silently equate type strain NRRL3382 with NRRL3382R or choose one source. FM173265 separately names NRRL3382R.

## Recommended Actions And Acceptance Checks

### address-strain-conflict

The source deposit names ATCC31180 while the inspected study assigns AB449340 to ATCC35851. The owner has neither strain nor a discussion of this conflict. Preserve both assertions before grade changes; do not silently equate type strain NRRL3382 with NRRL3382R or choose one source. FM173265 separately names NRRL3382R.

- Inspect claim-specific primary evidence at exact strain, locus and chemical-form scope; retain source conflicts.
- Preserve raw assertions and complete-row pins; generated corrections require canary, reproduction, strict validation and full QC.
- Any native owner discussion uses a curator-prefixed ID, guarded writer and curation event; do not hand-edit generated fields.
- No automatic salt/free-acid merge, stereochemical upgrade, taxon remap or evidence-grade promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/polyketides/lasalocid-2.yaml; Exact base 64c095104e5352fb88ad3177c47995ccfd4275d5 | supports | Entire owner and identical read_natural_product view inspected, including all source concepts, discussions and history. No inline graphs or graph refs are declared. No scientific field changed. |
| chemistry | /private/tmp/npmech-lasalocid-review-dQoF9p/source-inspection.json; chemistry; independent source checks in crosschecks.log | supports | RDKit2026.03.5 reproduces stored SMILES/InChI/key. Formula C34H53NaO8; net charge 0; 2 component(s), ten chiral centers all unspecified, matching stereo_complete:false. |
| inventory | data/raw/MANIFEST.yaml; source-inspection.json inventories; native complete input hashes retained in source | supports | Exact-key scans cover all rows: three MIBiG rows, two NPClassifier rows, one ChEBI structure/origin, two LOTUS occurrences, one exact sibling match. The single salt PubChem row is an explicit no-assay sentinel, not an activity result; no exact BindingDB rows. Raw rows and full-row digests retained in temporary audit. |
| registry | pubchem:2724110; Complete registry JSON; exact pinned-RDKit crosschecks; retrieval URL https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2724110/property/InChI,InChIKey,MolecularFormula,IUPACName/JSON | supports | Current PubChem exactly matches the nonstereospecific sodium salt; the xref is not a wrong-compound transfer. |
| BGC0000086 | https://mibig.secondarymetabolites.org/repository/BGC0000086.5/; Entire annotations.json including compounds, loci, taxonomy and legacy_references; retrieval URL https://mibig.secondarymetabolites.org/repository/BGC0000086.5/annotations.json | supports | Active version5 entry matches native structure, taxon and accession; locus evidence list is empty. SOURCE_ASSERTION and CLUSTER_UNSTATED faithfully reflect the database, not a conclusion that no experiments exist. Zero placeholder bounds are not meaningful genomic coordinates. |
| BGC0000087 | https://mibig.secondarymetabolites.org/repository/BGC0000087.5/; Entire annotations.json including compounds, loci, taxonomy and legacy_references; retrieval URL https://mibig.secondarymetabolites.org/repository/BGC0000087.5/annotations.json | supports | Active version5 entry matches native structure, taxon and accession; locus evidence list is empty. SOURCE_ASSERTION and CLUSTER_UNSTATED faithfully reflect the database, not a conclusion that no experiments exist. Zero placeholder bounds are not meaningful genomic coordinates. |
| genbank | genbank:AB449340.1; GBSeq definition, source qualifiers, lengths and references; sequence payload retained, not an independent nucleotide reassembly; retrieval URL https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=AB449340.1,FM173265.1,KT591188.1&amp;rettype=gb&amp;retmode=xml | refutes | AB449340.1 is an81959-bp pKSL sequence with current source strain ATCC31180; its linked2009 paper instead names ATCC35851. FM173265.1 is110927bp and names NRRL3382R. This confirms a source disagreement, not which strain is correct. |
| primary2009 | DOI:10.1271/bbb.80631; Advance-view PDF pages1-3,6; Scheme1 and Figure1 visually inspected on pages2-3. PMID19129623 is the same publication.; retrieval URL https://www.jstage.jst.go.jp/article/bbb/advpub/0/advpub_80631/_pdf/-char/en | partial | Methods identify ATCC35851/pKSL and deposit AB449340. Inactivation attempts failed; biochemical Lsd19 conversion is distinct from predicted steps. This paper does not substantiate FXJ1.172/KT591188. |
| primary2008 | PMID:18710235; PMID:19025863; Complete public PubMed abstracts and DOI mappings; not full papers or supplements; retrieval URL https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=18710235,19025863,19129623,32228806&amp;retmode=xml | partial | The first abstract reports purified recombinant Lsd19 converting synthetic bisepoxyprelasalocid to lasalocid A. The second reports lasC and lasB deletion outcomes. They suggest different evidence routes, but abstract-level evidence does not reconcile strain provenance or certify the stored unspecified sodium form. |
| taxonomy | NCBITaxon:324833; NCBITaxon:1931; NCBITaxon:1883; TaxaSet names, ranks and lineage; source inventories retain source taxon IDs; retrieval URL https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=324833,1931,1883&amp;retmode=xml | supports | 324833 is S.lasalocidi, with lasaliensis among historical names;1931 is Streptomyces sp.;1883 is genus Streptomyces. Their lineage supports ACTINOBACTERIAL. Preserve species/genus/strain distinctions and source spellings. |
| adapter | /private/tmp/npmech-lasalocid-review-dQoF9p/imodulondb.log; Actual kg-microbe-sources imodulondb datasets command | context_only | Full28-dataset list has no S.lasalocidi/lasaliensis or FXJ1.172 dataset. Other Streptomyces datasets and E.coli expression hosts are not substitutes for this native BGC context. Not applicable, not negative biological evidence. |
| search | local repository and campaign checkpoint; rg --no-ignore --hidden in curation/conf/reviews/structured/.claude; file-name search at repo root; canonical hidden-inclusive final check | context_only | Ignored/hidden-inclusive search found native records, rendered pages, queue entries and incidental lasalocidi context in a different record review. All75 prior canonical bundles were inventoried and hash-verified; these exact owners had no prior campaign assessment. This is not a global literature-absence assertion. |

## Limits And Additional Notes

- Primary absolute stereochemistry and exact counterion/isolation processing are not fully adjudicated. No merge or new compound assignment.
- The2008 abstracts were inspected; ACS full text denied and Wiley full text unavailable. The2023 PMC page challenged access; search excerpts were leads only. No bypass.
- The1970 LOTUS citation was checked only through its publisher abstract. The2020 taxonomy source was abstract-only. No supplement/NMR reassessment.
- The2009 PDF is an advance-view version; relevant methods/results and page2/3 figures inspected. No claim of independent experimental reproduction.
- iModulonDB has no matching native-producer dataset. Missing optional graph or target fields are not defects by themselves.
- Temporary payloads, scripts and receipts under /private/tmp/npmech-lasalocid-review-dQoF9p are not committed evidence snapshots; canonical review retains URLs, content hashes, provenance and bounded conclusions.
- Review preserves all3115 native owners,243 components and75 prior review bundles. All other unassessed owners and partial follow-ups remain in the full campaign.
- Ignored/hidden files included in absence searches and canonical bundle discovery.
- Initial chemistry environment failure is retained; exact-version chemistry check succeeded via existing environment.
- Source retrieval receipts: {"BGC0000086.5.json.receipt.json": {"bytes": 1582, "content_type": "application/json", "final_url": "https://mibig.secondarymetabolites.org/repository/BGC0000086.5/annotations.json", "finished_at": "2026-10-14T03:59:01.256394Z", "sha256": "6bfdab1b76d8d2fa7bd75bd846a8283ca6017a09051f588b333682cd4ba144c7", "started_at": "2026-10-14T03:59:00.102276Z", "status": 200, "url": "https://mibig.secondarymetabolites.org/repository/BGC0000086.5/annotations.json"}, "BGC0000087.5.json.receipt.json": {"bytes": 1939, "content_type": "application/json", "final_url": "https://mibig.secondarymetabolites.org/repository/BGC0000087.5/annotations.json", "finished_at": "2026-10-14T03:59:03.997101Z", "sha256": "14a317e7076931d2f6e37d817b540f5de7bed7801c53a718e816be05cd1c0a99", "started_at": "2026-10-14T03:59:03.385910Z", "status": 200, "url": "https://mibig.secondarymetabolites.org/repository/BGC0000087.5/annotations.json"}, "BGC0001648.5.json.receipt.json": {"bytes": 1711, "content_type": "application/json", "final_url": "https://mibig.secondarymetabolites.org/repository/BGC0001648.5/annotations.json", "finished_at": "2026-10-14T03:59:07.350787Z", "sha256": "3aab14980429e3cbcd3976a6c82e1a51a1e979d51e8696eeb9a648d12a3f9139", "started_at": "2026-10-14T03:59:06.794315Z", "status": 200, "url": "https://mibig.secondarymetabolites.org/repository/BGC0001648.5/annotations.json"}, "abstracts.xml.receipt.json": {"bytes": 30048, "content_type": "text/xml; charset=UTF-8", "final_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=18710235,19025863,19129623,32228806&amp;retmode=xml", "finished_at": "2026-10-14T03:59:17.804990Z", "sha256": "bdd359304ff1fcc118f90e05c3065f60f234b6153c1e60de389a22e1b11877f1", "started_at": "2026-10-14T03:59:17.418892Z", "status": 200, "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=18710235,19025863,19129623,32228806&amp;retmode=xml"}, "chebi-92181.json.receipt.json": {"bytes": 12198, "content_type": "application/json", "final_url": "https://www.ebi.ac.uk/chebi/backend/api/public/compound/92181/", "finished_at": "2026-10-14T03:59:10.755914Z", "sha256": "2ac7af3d70359bd8e7f5bd358161fcef05bc96e212a8139d231fddf414a0a86a", "started_at": "2026-10-14T03:59:09.823809Z", "status": 200, "url": "https://www.ebi.ac.uk/chebi/backend/api/public/compound/92181/"}, "genbank.xml.receipt.json": {"bytes": 615677, "content_type": "text/xml", "final_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=AB449340.1,FM173265.1,KT591188.1&amp;rettype=gb&amp;retmode=xml", "finished_at": "2026-10-14T03:59:20.723050Z", "sha256": "b9ed775e6f9f32f06877b051f3d33970ec6071d2956045f567b59e78b32c5b18", "started_at": "2026-10-14T03:59:20.165263Z", "status": 200, "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=AB449340.1,FM173265.1,KT591188.1&amp;rettype=gb&amp;retmode=xml"}, "primary2009.pdf.receipt.json": {"bytes": 336309, "content_type": "application/pdf;charset=UTF-8", "final_url": "https://www.jstage.jst.go.jp/article/bbb/advpub/0/advpub_80631/_pdf/-char/en", "finished_at": "2026-10-14T04:00:58.728023Z", "sha256": "ca760420cc5eb183366c6f9c5a1345238dbe8be5a83aa649f7fe4f7c7d28e8db", "started_at": "2026-10-14T04:00:56.706882Z", "status": 200, "url": "https://www.jstage.jst.go.jp/article/bbb/advpub/0/advpub_80631/_pdf/-char/en"}, "pubchem-2724110.json.receipt.json": {"bytes": 604, "content_type": "application/json", "final_url": "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2724110/property/InChI,InChIKey,MolecularFormula,IUPACName/JSON", "finished_at": "2026-10-14T03:59:15.315891Z", "sha256": "a41b25a7ed67deb62673f2bab168e104fe8648e9ae5c92e030f6a3ca92498560", "started_at": "2026-10-14T03:59:14.927940Z", "status": 200, "url": "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2724110/property/InChI,InChIKey,MolecularFormula,IUPACName/JSON"}, "taxonomy-fxj.xml.receipt.json": {"bytes": 2386, "content_type": "text/xml; charset=UTF-8", "final_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=710705&amp;retmode=xml", "finished_at": "2026-10-14T04:02:28.675999Z", "sha256": "111756ce9d75e97aeae1f4b2336780173de341eb9a9dc43a515140cc703ceaac", "started_at": "2026-10-14T04:02:28.389030Z", "status": 200, "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=710705&amp;retmode=xml"}, "taxonomy.xml.receipt.json": {"bytes": 8879, "content_type": "text/xml; charset=UTF-8", "final_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=324833,1931,1883&amp;retmode=xml", "finished_at": "2026-10-14T03:59:23.179267Z", "sha256": "e1f3b51050ad851dff2350877dd2fadd4ff35537fdf72160e8a0f667aabd144f", "started_at": "2026-10-14T03:59:22.857244Z", "status": 200, "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=324833,1931,1883&amp;retmode=xml"}}
- Source row digests: {"antibioticmech_inchikeys": [{"row_number": 113, "sha256": "be3c312736134653c4104b1321adb4de047918023ab771d94f10d5c4ccd961a2"}], "bindingdb_targets": [], "chebi_origins": [{"row_number": 12383, "sha256": "b9612ef4e1c4b127c605b6c0f56405c1467a559476778ed3b34e205310b5b951"}], "chebi_structures": [{"row_number": 35610, "sha256": "34d659802905abe18c27341f69cc9540b2a0d93bae13c4d55bc2c06ffcb97d57"}], "lotus_occurrences": [{"row_number": 446, "sha256": "2c497a96594e567e0868120e3778d2963b7395b7cce75745ca2042e6b1b56bdf"}, {"row_number": 447, "sha256": "01efae50d80e9da5666566b92745be9a8349c832f2fe26ce76d800dcc1e77ffa"}], "mibig_compounds": [{"row_number": 116, "sha256": "16ae9dfc4c84ec0707b885b9f5c28a39ddcb173ee6b73d74895bb387bfd2f07d"}, {"row_number": 117, "sha256": "93ef8326d2e0f579cdf8975bc7d49334ed6d4112c4e2d790c5a3e8ee27786291"}, {"row_number": 1969, "sha256": "fbb9c924907a87713a15ff6323080124a5dea60a58dead6a941dcf34b7c83b58"}], "npclassifier": [{"row_number": 141, "sha256": "272679a9549e4851abd68c5c485b8755b64a1d75ecc2d2326be6bac0377edb50"}, {"row_number": 2092, "sha256": "31af37f2f96fd96a03f1cea20d2084a104ac4f0063dcf2e64d91ac7e1bd16232"}], "pubchem_bioassay": [{"row_number": 6102, "sha256": "33a445d33a227c2d5a5e1a75781928ee82bcf0dc4360ffc4fbdc840073c22bfb"}]}

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T041547Z-lasalocid-2
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'lasalocid-2: exact-owner scientific review'
started_at: '2026-10-14T03:58:11.233622Z'
finished_at: '2026-10-14T04:15:47.631253Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same campaign assistant; not independent peer review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: SEEDED unchanged; unresolved primary scope
scientific_review: true
summary: Stored chemistry is internally consistent. An unrepresented strain-source
  conflict prevents exact locus attribution.
source:
  git_revision: 64c095104e5352fb88ad3177c47995ccfd4275d5
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
  - path: conf/sibling_pins.yaml
    sha256: 39a1d007ee65ba546567e8a34b7a309f75270b872809e1f783fe1fcee55866f2
    role: context
  - path: curation/decisions.tsv
    sha256: 7214a74975fb2cb65521da18dd14ea1c65665f50060106976dc0db9caf887805
    role: context
  - path: curation/lotus_occurrence_exclusions.tsv
    sha256: 4bc422b93002508b0abb86e0fa0afa49aff88745b5b0dd3bcbf351a68725d766
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: a0d43a9ba94c7e0044a5e9bc85f829ad5d010264f44c4a3470739eb7511c9740
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7d3e07b98587b27ec843ce73e7c5cf75b74d6fecb4ab8fdc29ca54fa04352a53
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 6f879bb9f2c9be6b6e8de8c013dbaebe09075b7e106790ea303a17006761ea11
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
    role: context
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/polyketides/lasalocid-2.yaml
    sha256: 79b95ce009f3cac2cbd631f63e7ed8d5b0ac6c269b5cfeb7fd055407f5e4fb24
    role: target
  - path: data/natural_products/polyketides/lasalocid.yaml
    sha256: e7240d0a9c3926f085bd34497dc51bdacb998f809bc5c5f9fca1000e7bc93bd4
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 373f049029be3db137e062ff5f872a2400a9d5b423f3e108ea44ebde2f8dcc7d
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
    sha256: 90420425c90529cc99b474cb38cfedc7209c0e825b851f105f418868575a0a61
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
    sha256: c7531c2ff57eb55174c1c358c8bdbd507b25f4446d20e163f9b60b1161e48415
    role: context
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
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
- target_id: naturalproductmech:mibig-73ba44dafe
  path: data/natural_products/polyketides/lasalocid-2.yaml
  label: lasalocid
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated owner emission and source harmonization
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG extraction and source chemistry
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned raw MIBiG assertions; preserve provenance
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned grounding structures
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Pinned origin assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Pinned occurrence assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned computed filing decisions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned exact sibling join
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Reviewed method overrides
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Pinned strain qualifications
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Pinned nonexact chemical xref exclusions
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Pinned unsupported occurrence exclusions
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Claim-specific source-pinned citation routing
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/lasalocid-2.yaml
    role: Only future curator-prefixed discussions through guarded writer/event; generated
      fields remain source-owned
scope:
  description: Whole exact owner, complete resolved mechanism view, pinned inventories
    and bounded primary/database checks.
  selection: Next exact owner in the3115-record campaign; same-name sibling assessed
    separately.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-73ba44dafe
checks:
- check_id: strict
  name: strict
  status: passed
  required: true
  command: just validate-strict data/natural_products/polyketides/lasalocid-2.yaml
    data/natural_products/polyketides/lasalocid.yaml --out /private/tmp/npmech-lasalocid-review-dQoF9p/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  summary: Passed within actual recorded scope.
  scope_note: 2026-10-14T03:58:35.328865Z..2026-10-14T03:58:38.888124Z; log /private/tmp/npmech-lasalocid-review-dQoF9p/strict.log;
    SHA256 f4c64d3fd6109c27afab98cfba65b7f22aabd34bea3fc78e12ebdd349d64ca7d
- check_id: labels
  name: labels
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  summary: Passed with499 existing nonblocking mismatches and4647 no-adapter skips;
    not universal ontology verification.
  scope_note: 2026-10-14T03:58:42.677830Z..2026-10-14T04:00:26.841009Z; log /private/tmp/npmech-lasalocid-review-dQoF9p/labels.log;
    SHA256 3a35478c0f50d04f173e629252d86cf81839ab6d9d291ca88a9631d93d0cca64
- check_id: qc
  name: qc
  status: passed
  required: true
  command: just qc
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  summary: Passed within actual recorded scope.
  scope_note: 2026-10-14T03:58:38.792003Z..2026-10-14T04:15:05.573233Z; log /private/tmp/npmech-lasalocid-review-dQoF9p/qc.log;
    SHA256 0b54c8178a223113e9037f84f44884213c93d65e21c818d7604c15a4868c2cf5
- check_id: queue
  name: queue
  status: passed
  required: true
  command: just review-queue --tsv /private/tmp/npmech-lasalocid-review-dQoF9p/review-queue.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  summary: Passed within actual recorded scope.
  scope_note: 2026-10-14T04:03:23.959722Z..2026-10-14T04:04:06.466632Z; log /private/tmp/npmech-lasalocid-review-dQoF9p/queue.log;
    SHA256 ca732d7611d6886ce47b43a814e1eff9fc0863c4d75d1449167ee2499abd8697
- check_id: chemistry-pinned
  name: chemistry-pinned
  status: passed
  required: true
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-lasalocid-review-dQoF9p/inspect_sources.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  summary: Passed within actual recorded scope.
  scope_note: 2026-10-14T04:00:53.045517Z..2026-10-14T04:00:54.385563Z; log /private/tmp/npmech-lasalocid-review-dQoF9p/chemistry-pinned.log;
    SHA256 87bca78263e12cf0a24cc7f6896588935393df63954a41608aaf7533b2894e76
- check_id: crosschecks
  name: crosschecks
  status: passed
  required: true
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-lasalocid-review-dQoF9p/verify_claims.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  summary: Passed within actual recorded scope.
  scope_note: 2026-10-14T04:06:26.553275Z..2026-10-14T04:06:27.368686Z; log /private/tmp/npmech-lasalocid-review-dQoF9p/crosschecks.log;
    SHA256 6169ede5b8fb0f63ca3ab014a404d8beaeb4a6c7158cb45aa6b91c59cfac96b0
- check_id: imodulondb
  name: imodulondb
  status: passed
  required: false
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  summary: Dataset listing succeeded; no applicable native-producer dataset.
  scope_note: 2026-10-14T03:59:38.143504Z..2026-10-14T03:59:38.661957Z; log /private/tmp/npmech-lasalocid-review-dQoF9p/imodulondb.log;
    SHA256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- check_id: chemistry-wheel-attempt
  name: Initial repository chemistry-extra attempt
  status: failed
  required: false
  command: uv run --extra chemistry python /private/tmp/npmech-lasalocid-review-dQoF9p/inspect_sources.py
  exit_code: 2
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  summary: Pinned RDKit has no wheel for this macOS x86_64 platform. Replaced by successful
    existing exact-version environment; no dependency change.
  scope_note: Failure log SHA256 8720b8ec37cd9da492008f08327edaf2506cf47c3eb81fcf049b7c6a6bed80d8
- check_id: primary-closure
  name: Primary exact-form and strain/locus closure
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  summary: Some primary full texts inaccessible; original stereochemistry, salt processing
    and disputed strain attribution not fully adjudicated. No bypass.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/polyketides/lasalocid-2.yaml
  summary: Entire owner and identical read_natural_product view inspected, including
    all source concepts, discussions and history. No inline graphs or graph refs are
    declared. No scientific field changed.
  locator: Exact base 64c095104e5352fb88ad3177c47995ccfd4275d5
  accessed_at: '2026-10-14T04:15:47.621838Z'
  support: supports
  snapshot_sha256: 017bed75a63e5327bb61239ca8685e4cd1a57693d31727a3314908da96d9e20f
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-lasalocid-review-dQoF9p/source-inspection.json
  summary: RDKit2026.03.5 reproduces stored SMILES/InChI/key. Formula C34H53NaO8;
    net charge 0; 2 component(s), ten chiral centers all unspecified, matching stereo_complete:false.
  locator: chemistry; independent source checks in crosschecks.log
  accessed_at: '2026-10-14T04:15:47.623097Z'
  support: supports
  snapshot_sha256: 4fc04455b8dedf4676266714065df6ad8c5fe8297ec4d7d3241cddd0709143af
- evidence_id: inventory
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  summary: 'Exact-key scans cover all rows: three MIBiG rows, two NPClassifier rows,
    one ChEBI structure/origin, two LOTUS occurrences, one exact sibling match. The
    single salt PubChem row is an explicit no-assay sentinel, not an activity result;
    no exact BindingDB rows. Raw rows and full-row digests retained in temporary audit.'
  locator: source-inspection.json inventories; native complete input hashes retained
    in source
  accessed_at: '2026-10-14T04:15:47.623542Z'
  support: supports
  snapshot_sha256: 4fc04455b8dedf4676266714065df6ad8c5fe8297ec4d7d3241cddd0709143af
- evidence_id: registry
  kind: database
  reference: pubchem:2724110
  summary: Current PubChem exactly matches the nonstereospecific sodium salt; the
    xref is not a wrong-compound transfer.
  locator: Complete registry JSON; exact pinned-RDKit crosschecks; retrieval URL https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2724110/property/InChI,InChIKey,MolecularFormula,IUPACName/JSON
  accessed_at: '2026-10-14T03:59:15.315891Z'
  support: supports
  snapshot_sha256: a41b25a7ed67deb62673f2bab168e104fe8648e9ae5c92e030f6a3ca92498560
- evidence_id: BGC0000086
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000086.5/
  summary: Active version5 entry matches native structure, taxon and accession; locus
    evidence list is empty. SOURCE_ASSERTION and CLUSTER_UNSTATED faithfully reflect
    the database, not a conclusion that no experiments exist. Zero placeholder bounds
    are not meaningful genomic coordinates.
  locator: Entire annotations.json including compounds, loci, taxonomy and legacy_references;
    retrieval URL https://mibig.secondarymetabolites.org/repository/BGC0000086.5/annotations.json
  accessed_at: '2026-10-14T03:59:01.256394Z'
  support: supports
  snapshot_sha256: 6bfdab1b76d8d2fa7bd75bd846a8283ca6017a09051f588b333682cd4ba144c7
- evidence_id: BGC0000087
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000087.5/
  summary: Active version5 entry matches native structure, taxon and accession; locus
    evidence list is empty. SOURCE_ASSERTION and CLUSTER_UNSTATED faithfully reflect
    the database, not a conclusion that no experiments exist. Zero placeholder bounds
    are not meaningful genomic coordinates.
  locator: Entire annotations.json including compounds, loci, taxonomy and legacy_references;
    retrieval URL https://mibig.secondarymetabolites.org/repository/BGC0000087.5/annotations.json
  accessed_at: '2026-10-14T03:59:03.997101Z'
  support: supports
  snapshot_sha256: 14a317e7076931d2f6e37d817b540f5de7bed7801c53a718e816be05cd1c0a99
- evidence_id: genbank
  kind: database
  reference: genbank:AB449340.1
  summary: AB449340.1 is an81959-bp pKSL sequence with current source strain ATCC31180;
    its linked2009 paper instead names ATCC35851. FM173265.1 is110927bp and names
    NRRL3382R. This confirms a source disagreement, not which strain is correct.
  locator: GBSeq definition, source qualifiers, lengths and references; sequence payload
    retained, not an independent nucleotide reassembly; retrieval URL https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB449340.1,FM173265.1,KT591188.1&rettype=gb&retmode=xml
  accessed_at: '2026-10-14T03:59:20.723050Z'
  support: refutes
  snapshot_sha256: b9ed775e6f9f32f06877b051f3d33970ec6071d2956045f567b59e78b32c5b18
- evidence_id: primary2009
  kind: primary_source
  reference: DOI:10.1271/bbb.80631
  summary: Methods identify ATCC35851/pKSL and deposit AB449340. Inactivation attempts
    failed; biochemical Lsd19 conversion is distinct from predicted steps. This paper
    does not substantiate FXJ1.172/KT591188.
  locator: Advance-view PDF pages1-3,6; Scheme1 and Figure1 visually inspected on
    pages2-3. PMID19129623 is the same publication.; retrieval URL https://www.jstage.jst.go.jp/article/bbb/advpub/0/advpub_80631/_pdf/-char/en
  accessed_at: '2026-10-14T04:00:58.728023Z'
  support: partial
  snapshot_sha256: ca760420cc5eb183366c6f9c5a1345238dbe8be5a83aa649f7fe4f7c7d28e8db
- evidence_id: primary2008
  kind: primary_source
  reference: PMID:18710235; PMID:19025863
  summary: The first abstract reports purified recombinant Lsd19 converting synthetic
    bisepoxyprelasalocid to lasalocid A. The second reports lasC and lasB deletion
    outcomes. They suggest different evidence routes, but abstract-level evidence
    does not reconcile strain provenance or certify the stored unspecified sodium
    form.
  locator: Complete public PubMed abstracts and DOI mappings; not full papers or supplements;
    retrieval URL https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=18710235,19025863,19129623,32228806&retmode=xml
  accessed_at: '2026-10-14T03:59:17.804990Z'
  support: partial
  snapshot_sha256: bdd359304ff1fcc118f90e05c3065f60f234b6153c1e60de389a22e1b11877f1
- evidence_id: taxonomy
  kind: database
  reference: NCBITaxon:324833; NCBITaxon:1931; NCBITaxon:1883
  summary: 324833 is S.lasalocidi, with lasaliensis among historical names;1931 is
    Streptomyces sp.;1883 is genus Streptomyces. Their lineage supports ACTINOBACTERIAL.
    Preserve species/genus/strain distinctions and source spellings.
  locator: TaxaSet names, ranks and lineage; source inventories retain source taxon
    IDs; retrieval URL https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=324833,1931,1883&retmode=xml
  accessed_at: '2026-10-14T03:59:23.179267Z'
  support: supports
  snapshot_sha256: e1f3b51050ad851dff2350877dd2fadd4ff35537fdf72160e8a0f667aabd144f
- evidence_id: adapter
  kind: database
  reference: /private/tmp/npmech-lasalocid-review-dQoF9p/imodulondb.log
  summary: Full28-dataset list has no S.lasalocidi/lasaliensis or FXJ1.172 dataset.
    Other Streptomyces datasets and E.coli expression hosts are not substitutes for
    this native BGC context. Not applicable, not negative biological evidence.
  locator: Actual kg-microbe-sources imodulondb datasets command
  accessed_at: '2026-10-14T04:15:47.630871Z'
  support: context_only
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: local repository and campaign checkpoint
  summary: Ignored/hidden-inclusive search found native records, rendered pages, queue
    entries and incidental lasalocidi context in a different record review. All75
    prior canonical bundles were inventoried and hash-verified; these exact owners
    had no prior campaign assessment. This is not a global literature-absence assertion.
  locator: rg --no-ignore --hidden in curation/conf/reviews/structured/.claude; file-name
    search at repo root; canonical hidden-inclusive final check
  accessed_at: '2026-10-14T04:15:47.631017Z'
  support: context_only
  search_scope: Exact keys, lasalocid label and BGC0000086/87/1648; ignored files
    included. Primary search limited to source citations and FXJ1.172 follow-up.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure and same-name boundary
  outcome: supported
  summary: Faithful unspecified sodium-salt encoding; PubChem matches and stereo_complete:false
    is honest. Do not merge with the free acid or invent stereochemistry.
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  evidence_ids:
  - owner
  - chemistry
  - registry
  dimensions:
  - name: chemical-form
    value: nonstereospecific sodium salt
    definition: Stored chemical form, not a conclusion about isolation processing
    evidence_ids:
    - chemistry
    - registry
- assessment_id: primary-identity
  area: evidence
  topic: Primary identity resolution
  outcome: unknown
  summary: Database agreement does not independently certify the biological product
    at every stereocenter or establish processing/counterion state. No structure replacement
    or owner migration proposed as automatic.
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  evidence_ids:
  - registry
  - primary2009
  - primary2008
- assessment_id: producer
  area: scope
  topic: Producer strain and evidence tier
  outcome: concern
  summary: Species-level database assertions retain cautious grades, but exact strain
    context is omitted and the AB449340 deposit conflicts with its primary paper.
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  evidence_ids:
  - owner
  - genbank
  - primary2009
  - taxonomy
  dimensions:
  - name: native-evidence-tier
    value: SOURCE_ASSERTION / CLUSTER_UNSTATED
    definition: Two separate imported grades; neither is experimental sign-off
    evidence_ids:
    - owner
- assessment_id: clusters
  area: evidence
  topic: BGC activity, locus and primary support
  outcome: concern
  summary: Both active entries reproduce. Empty source methods do not deny published
    experiments; any overrides require exact strain/form adjudication, and purified
    enzyme activity does not upgrade the native producer.
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  evidence_ids:
  - genbank
  - primary2009
  - primary2008
  - BGC0000086
  - BGC0000087
- assessment_id: classification
  area: representation
  topic: Independent classification facets
  outcome: supported
  summary: POLYKETIDES and polyether subclasses remain versioned NPClassifier output;
    PKS is a cluster assertion; ACTINOBACTERIAL is taxonomic. NATURAL_PRODUCT reflects
    the origin assertion, not a claim that all experimental strains are unmodified.
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  evidence_ids:
  - inventory
  - taxonomy
  - owner
- assessment_id: occurrences
  area: scope
  topic: Occurrence versus production
  outcome: not_applicable
  summary: No occurrences are asserted on this owner; no free-acid claims are transferred.
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  evidence_ids:
  - owner
- assessment_id: activity
  area: provenance
  topic: Activity and sibling ownership
  outcome: not_applicable
  summary: No native assay, target or summary is asserted; the raw no-data sentinel
    is not negative efficacy evidence.
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  evidence_ids:
  - owner
  - inventory
- assessment_id: mechanism
  area: graph
  topic: Pathway and graph completeness
  outcome: not_applicable
  summary: No native pathway, graph or protein example is declared. Missing optional
    mechanisms are not false assertions; a future graph must distinguish prediction,
    enzyme conversion and native deletion experiments.
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  evidence_ids:
  - owner
  - primary2008
  - primary2009
- assessment_id: audit
  area: ownership
  topic: Generated boundaries and history
  outcome: supported
  summary: Native SEEDED status and both seed-history events remain unchanged. Proposed
    fixes name maintained tables or guarded curator discussions; curation/decisions.tsv
    is reserved and is not an effective fix path.
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  evidence_ids:
  - owner
  - inventory
findings:
- finding_id: strain-conflict
  issue_key: lasalocid-bgc0000086-strain-provenance-conflict
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: AB449340 strain conflict is unrepresented in the native record
  description: The source deposit names ATCC31180 while the inspected study assigns
    AB449340 to ATCC35851. The owner has neither strain nor a discussion of this conflict.
    Preserve both assertions before grade changes; do not silently equate type strain
    NRRL3382 with NRRL3382R or choose one source. FM173265 separately names NRRL3382R.
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  field_paths:
  - producer_organisms
  - biosynthetic_gene_clusters
  - discussions
  evidence_ids:
  - genbank
  - primary2009
  - owner
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/lasalocid-2.yaml
    role: Future curator-prefixed conflict discussion via guarded writer/event
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Only separately adjudicated strain qualification
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: No grade change before strain/form adjudication
  rule_id: docs/CURATION.md:claim-scope-and-conflict-preservation
  native_severity: major
  normalization_reason: Material claim-specific provenance conflict is major; bounded
    omitted strain qualification without a stronger-grade claim is minor. No identity
    blocker inferred from honest incomplete stereochemistry.
actions:
- action_id: address-strain-conflict
  description: The source deposit names ATCC31180 while the inspected study assigns
    AB449340 to ATCC35851. The owner has neither strain nor a discussion of this conflict.
    Preserve both assertions before grade changes; do not silently equate type strain
    NRRL3382 with NRRL3382R or choose one source. FM173265 separately names NRRL3382R.
  finding_ids:
  - strain-conflict
  target_ids:
  - naturalproductmech:mibig-73ba44dafe
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/lasalocid-2.yaml
    role: Future curator-prefixed conflict discussion via guarded writer/event
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Only separately adjudicated strain qualification
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: No grade change before strain/form adjudication
  acceptance_checks:
  - Inspect claim-specific primary evidence at exact strain, locus and chemical-form
    scope; retain source conflicts.
  - Preserve raw assertions and complete-row pins; generated corrections require canary,
    reproduction, strict validation and full QC.
  - Any native owner discussion uses a curator-prefixed ID, guarded writer and curation
    event; do not hand-edit generated fields.
  - No automatic salt/free-acid merge, stereochemical upgrade, taxon remap or evidence-grade
    promotion.
  generator: scripts/seed_from_sources.py only for authorized maintained-table changes
limitations:
- Primary absolute stereochemistry and exact counterion/isolation processing are not
  fully adjudicated. No merge or new compound assignment.
- The2008 abstracts were inspected; ACS full text denied and Wiley full text unavailable.
  The2023 PMC page challenged access; search excerpts were leads only. No bypass.
- The1970 LOTUS citation was checked only through its publisher abstract. The2020
  taxonomy source was abstract-only. No supplement/NMR reassessment.
- The2009 PDF is an advance-view version; relevant methods/results and page2/3 figures
  inspected. No claim of independent experimental reproduction.
- iModulonDB has no matching native-producer dataset. Missing optional graph or target
  fields are not defects by themselves.
- Temporary payloads, scripts and receipts under /private/tmp/npmech-lasalocid-review-dQoF9p
  are not committed evidence snapshots; canonical review retains URLs, content hashes,
  provenance and bounded conclusions.
- Review preserves all3115 native owners,243 components and75 prior review bundles.
  All other unassessed owners and partial follow-ups remain in the full campaign.
notes:
- Ignored/hidden files included in absence searches and canonical bundle discovery.
- Initial chemistry environment failure is retained; exact-version chemistry check
  succeeded via existing environment.
- 'Source retrieval receipts: {"BGC0000086.5.json.receipt.json": {"bytes": 1582, "content_type":
  "application/json", "final_url": "https://mibig.secondarymetabolites.org/repository/BGC0000086.5/annotations.json",
  "finished_at": "2026-10-14T03:59:01.256394Z", "sha256": "6bfdab1b76d8d2fa7bd75bd846a8283ca6017a09051f588b333682cd4ba144c7",
  "started_at": "2026-10-14T03:59:00.102276Z", "status": 200, "url": "https://mibig.secondarymetabolites.org/repository/BGC0000086.5/annotations.json"},
  "BGC0000087.5.json.receipt.json": {"bytes": 1939, "content_type": "application/json",
  "final_url": "https://mibig.secondarymetabolites.org/repository/BGC0000087.5/annotations.json",
  "finished_at": "2026-10-14T03:59:03.997101Z", "sha256": "14a317e7076931d2f6e37d817b540f5de7bed7801c53a718e816be05cd1c0a99",
  "started_at": "2026-10-14T03:59:03.385910Z", "status": 200, "url": "https://mibig.secondarymetabolites.org/repository/BGC0000087.5/annotations.json"},
  "BGC0001648.5.json.receipt.json": {"bytes": 1711, "content_type": "application/json",
  "final_url": "https://mibig.secondarymetabolites.org/repository/BGC0001648.5/annotations.json",
  "finished_at": "2026-10-14T03:59:07.350787Z", "sha256": "3aab14980429e3cbcd3976a6c82e1a51a1e979d51e8696eeb9a648d12a3f9139",
  "started_at": "2026-10-14T03:59:06.794315Z", "status": 200, "url": "https://mibig.secondarymetabolites.org/repository/BGC0001648.5/annotations.json"},
  "abstracts.xml.receipt.json": {"bytes": 30048, "content_type": "text/xml; charset=UTF-8",
  "final_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=18710235,19025863,19129623,32228806&retmode=xml",
  "finished_at": "2026-10-14T03:59:17.804990Z", "sha256": "bdd359304ff1fcc118f90e05c3065f60f234b6153c1e60de389a22e1b11877f1",
  "started_at": "2026-10-14T03:59:17.418892Z", "status": 200, "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=18710235,19025863,19129623,32228806&retmode=xml"},
  "chebi-92181.json.receipt.json": {"bytes": 12198, "content_type": "application/json",
  "final_url": "https://www.ebi.ac.uk/chebi/backend/api/public/compound/92181/", "finished_at":
  "2026-10-14T03:59:10.755914Z", "sha256": "2ac7af3d70359bd8e7f5bd358161fcef05bc96e212a8139d231fddf414a0a86a",
  "started_at": "2026-10-14T03:59:09.823809Z", "status": 200, "url": "https://www.ebi.ac.uk/chebi/backend/api/public/compound/92181/"},
  "genbank.xml.receipt.json": {"bytes": 615677, "content_type": "text/xml", "final_url":
  "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB449340.1,FM173265.1,KT591188.1&rettype=gb&retmode=xml",
  "finished_at": "2026-10-14T03:59:20.723050Z", "sha256": "b9ed775e6f9f32f06877b051f3d33970ec6071d2956045f567b59e78b32c5b18",
  "started_at": "2026-10-14T03:59:20.165263Z", "status": 200, "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB449340.1,FM173265.1,KT591188.1&rettype=gb&retmode=xml"},
  "primary2009.pdf.receipt.json": {"bytes": 336309, "content_type": "application/pdf;charset=UTF-8",
  "final_url": "https://www.jstage.jst.go.jp/article/bbb/advpub/0/advpub_80631/_pdf/-char/en",
  "finished_at": "2026-10-14T04:00:58.728023Z", "sha256": "ca760420cc5eb183366c6f9c5a1345238dbe8be5a83aa649f7fe4f7c7d28e8db",
  "started_at": "2026-10-14T04:00:56.706882Z", "status": 200, "url": "https://www.jstage.jst.go.jp/article/bbb/advpub/0/advpub_80631/_pdf/-char/en"},
  "pubchem-2724110.json.receipt.json": {"bytes": 604, "content_type": "application/json",
  "final_url": "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2724110/property/InChI,InChIKey,MolecularFormula,IUPACName/JSON",
  "finished_at": "2026-10-14T03:59:15.315891Z", "sha256": "a41b25a7ed67deb62673f2bab168e104fe8648e9ae5c92e030f6a3ca92498560",
  "started_at": "2026-10-14T03:59:14.927940Z", "status": 200, "url": "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2724110/property/InChI,InChIKey,MolecularFormula,IUPACName/JSON"},
  "taxonomy-fxj.xml.receipt.json": {"bytes": 2386, "content_type": "text/xml; charset=UTF-8",
  "final_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=710705&retmode=xml",
  "finished_at": "2026-10-14T04:02:28.675999Z", "sha256": "111756ce9d75e97aeae1f4b2336780173de341eb9a9dc43a515140cc703ceaac",
  "started_at": "2026-10-14T04:02:28.389030Z", "status": 200, "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=710705&retmode=xml"},
  "taxonomy.xml.receipt.json": {"bytes": 8879, "content_type": "text/xml; charset=UTF-8",
  "final_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=324833,1931,1883&retmode=xml",
  "finished_at": "2026-10-14T03:59:23.179267Z", "sha256": "e1f3b51050ad851dff2350877dd2fadd4ff35537fdf72160e8a0f667aabd144f",
  "started_at": "2026-10-14T03:59:22.857244Z", "status": 200, "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=324833,1931,1883&retmode=xml"}}'
- 'Source row digests: {"antibioticmech_inchikeys": [{"row_number": 113, "sha256":
  "be3c312736134653c4104b1321adb4de047918023ab771d94f10d5c4ccd961a2"}], "bindingdb_targets":
  [], "chebi_origins": [{"row_number": 12383, "sha256": "b9612ef4e1c4b127c605b6c0f56405c1467a559476778ed3b34e205310b5b951"}],
  "chebi_structures": [{"row_number": 35610, "sha256": "34d659802905abe18c27341f69cc9540b2a0d93bae13c4d55bc2c06ffcb97d57"}],
  "lotus_occurrences": [{"row_number": 446, "sha256": "2c497a96594e567e0868120e3778d2963b7395b7cce75745ca2042e6b1b56bdf"},
  {"row_number": 447, "sha256": "01efae50d80e9da5666566b92745be9a8349c832f2fe26ce76d800dcc1e77ffa"}],
  "mibig_compounds": [{"row_number": 116, "sha256": "16ae9dfc4c84ec0707b885b9f5c28a39ddcb173ee6b73d74895bb387bfd2f07d"},
  {"row_number": 117, "sha256": "93ef8326d2e0f579cdf8975bc7d49334ed6d4112c4e2d790c5a3e8ee27786291"},
  {"row_number": 1969, "sha256": "fbb9c924907a87713a15ff6323080124a5dea60a58dead6a941dcf34b7c83b58"}],
  "npclassifier": [{"row_number": 141, "sha256": "272679a9549e4851abd68c5c485b8755b64a1d75ecc2d2326be6bac0377edb50"},
  {"row_number": 2092, "sha256": "31af37f2f96fd96a03f1cea20d2084a104ac4f0063dcf2e64d91ac7e1bd16232"}],
  "pubchem_bioassay": [{"row_number": 6102, "sha256": "33a445d33a227c2d5a5e1a75781928ee82bcf0dc4360ffc4fbdc840073c22bfb"}]}'
tags:
- lasalocid
- record-review-campaign
- partial
```
