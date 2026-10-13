# Bacilysin: anhydride identity conflict and FZB42 evidence scope

- Review: 20261013T140252Z-bacilysin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T13:19:20.112934Z
- Finished UTC: 2026-10-13T14:02:52.291755Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed blocker: the stored anhydride is not the reported bacilysin dipeptide. Source/PubChem agreement does not repair identity. FZB42 experiments and all six occurrences require correct chemical scope; full stereo/method/citation adjudication remains partial.

## Scope And Provenance

One exact owner; same-name sibling and authority records are context only. The full campaign remains3115 owners and243 components.

Selection: Next exact pending owner from the exhaustive campaign checkpoint; all unfinished records remain in scope.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 9191a148302dce8d04699b8436a68b84329d20b8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-080d9481a3 | data/natural_products/amino_acids_and_peptides/bacilysin.yaml | generated | bacilysin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict | passed | True | naturalproductmech:mibig-080d9481a3 | Both exact owners passed strict validation with zero errors; no graph refs exist. |
| labels | passed | True | naturalproductmech:mibig-080d9481a3 | Configured label gate passed:13434 canonical,646 synonyms,35 exceptions,499 nonblocking warning mismatches and4649 no-adapter skips. Minted compound identity was separately checked, not certified by this gate. |
| chemistry | passed | True | naturalproductmech:mibig-080d9481a3 | Pinned RDKit calculations succeeded and located connectivity/stereo differences; no experimental assignment inferred. |
| ignored-inclusive-search | passed | False | naturalproductmech:mibig-080d9481a3 | Name, identifiers, keys and selected citations searched with ignored/hidden files included; only .git and .venv excluded. Curation tables/consumers were independently read; no implemented bacilysin-specific correction row was found in that bounded scope. |
| qc | passed | True | naturalproductmech:mibig-080d9481a3 | Full native QC passed: 723 passed, 3 skipped, 2 warnings in 624.50s (0:10:24). Strict corpus schema, history/graph tests, provenance, lint, vendored sync, site, reproduction and path lock passed. Run began before PR904 publication; all reviewed inputs remain byte-identical. It did not collect the later archive-only tests, which do not alter the scientific inputs. |
| review-queue | passed | False | naturalproductmech:mibig-080d9481a3 | Full native diagnostic queue computed in the original review attempt; diagnostic rows are not scientific review completions. |
| queue-fresh | passed | False | naturalproductmech:mibig-080d9481a3 | Full pending-record queue regenerated after this batch assessment; all3115 owners remain included. The extra unresolved_taxa.tsv diagnostics are not owners. |
| Primary experimental and exact chemical-form verification | unavailable | True | naturalproductmech:mibig-080d9481a3 | Full methods, chemical figures/spectra, isolate stereochemistry and exact occurrence citations remain unverified. Abstracts were read without pretending full-text completion. The newly identified1993 C4-reassignment paper is also unavailable after two same-page timeouts. |
| Structured expression-source applicability | not_applicable | False | naturalproductmech:mibig-080d9481a3 | Owners contain no named gene/protein/regulator/module claims. MIBiG and sequence/chemical authority APIs were consulted first. Genes in contextual source annotations do not create a transcriptomic assertion; no iModulon dataset-absence claim is made. |
| Historical versus current NPAtlas structure comparison | passed | True | naturalproductmech:mibig-080d9481a3 | Historical/current NPAtlas graphs and embedded classification structure mapped explicitly. Current identity was not inferred from an old classifier payload. |

## Scientific And Domain Assessments

### Connectivity and supported stereochemical resolution

identity: concern. Targets: naturalproductmech:mibig-080d9481a3.

The encoded anhydride has no peptide bond and therefore is not the reported bacilysin dipeptide. Matching MIBiG/PubChem identifiers, mass and formula do not repair identity. F1 blocks exact-structure origin and occurrence attribution. NPAtlas explicitly retains a historical exact-owner structure but identifies a different current form with a1993 reassignment citation. Primary revision details must be checked before selecting an authority or altering stereochemistry.

### Exact equivalence and grounding candidates

grounding: supported. Targets: naturalproductmech:mibig-080d9481a3.

The PubChem xref exactly matches the stored graph. That is accurate database equivalence, not correct natural-product identity. ChEBI and the sibling bacilysin key differ; withholding a same-name join is appropriate. NPAtlas explicitly retains a historical exact-owner structure but identifies a different current form with a1993 reassignment citation. Primary revision details must be checked before selecting an authority or altering stereochemistry.

### Computed filing versus asserted chemistry and taxonomic facets

provenance: supported. Targets: naturalproductmech:mibig-080d9481a3.

NPClassifier filing, Small peptides/Dipeptides, tool/version and non-glycoside output match pinned rows. Source BGC OTHER remains a separate assertion, as do OTHER_BACTERIAL taxon facets. A computed dipeptide prediction is not validation of an amide bond.

### Strain, source tier and condition-specific experimental context

evidence: concern. Targets: naturalproductmech:mibig-080d9481a3.

Native FZB42 knockout/complementation context supports biological bacilysin at abstract level, consistent with a characterized evidence tier. It does not demonstrate production of the JJOS anhydride. F1 blocks chemical scope despite correct taxon/strain provenance.

### Versioned entry, genomic interval and exact locus methods

evidence: unknown. Targets: naturalproductmech:mibig-080d9481a3.

Active version4 and the7298bp requested FZB42 window agree with bac gene context. Knockout evidence is supported at abstract level, but the separate producer-expression/production-correlation method remains unverified. Target-organism expression changes in later papers cannot substitute for it. No method withdrawal follows from missing full text.

### Every LOTUS citation and taxonomic scope

evidence: concern. Targets: naturalproductmech:mibig-080d9481a3.

All six DOI identities and organism notes resolve at metadata/label level. The1970,1988,1990 andFZB42 studies concern biological bacilysin, not JJOS. Fengycin and difficidin-paper abstracts do not establish bacilysin occurrence, but full-paper silence/false citation is not proven. F1 blocks exact-key attribution; every occurrence needs individual adjudication before any identity correction transfers claims.

### Optional assays, mechanisms, proteins, clinical assertions and history

completeness: unknown. Targets: naturalproductmech:mibig-080d9481a3.

Complete resolved owners have no graphs/components, pathway steps, assays, targets, clinical assertions or related_records. These optional omissions are not false claims. The BioAssay placeholder is correctly not used as activity. Literature gives leads for future mechanism curation only after exact identity and full experimental support are established; no evidence/history/status change was made.

### Native deterministic validation and exhaustive scope preservation

schema: supported. Targets: naturalproductmech:mibig-080d9481a3.

Native strict, label, full QC and queue checks passed with their real receipts. Captured sources match the original9191a148 tree and current745da66f; all3115 owners/243 components/23 prior pairs remain unchanged. Deterministic validation does not certify scientific correctness or close any prior finding.

## Findings

### F1: Stored anhydride is not the bacilysin dipeptide

blocker / open / confirmed; issue key: bacilysin-BGC0001184-anhydride-wrong-connectivity.

JJOSOKMLZZVGKD-INVWQFOESA-N has an acid-anhydride linkage, zero amide bonds and two free primary amines. Biological bacilysin is the alanine/anticapsin dipeptide supported by the inspected primary abstracts and ChEBI definition. MIBiG and PubChem reproduce the same wrong graph; a formula/mass match or exact-to-current-graph xref does not validate it. Producer, origin, cluster-product and occurrence assertions cannot be carried onto this chemically different graph.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate and repair or quarantine BGC0001184:1 through a tested source-pinned path, with exact stereochemical resolution and chemical-form scope. Do not select ChEBI blindly: the pinned bacilysin/zwitterion pair shares a key that the current replacement consumer rejects as ambiguous. Do not merge into the differently stereospecified sibling or transfer its claims by name. Removing PubChem alone is not an identity repair.

- Inspect the1993 Crossley/Stamford C4-reassignment paper and reconcile its actual figures/assignments with NPAtlas historical/current payloads and ChEBI; infer no correction direction from title alone.
- Confirm primary peptide connectivity, supported isolate stereochemistry and intended protonation/form; recompute SMILES/InChI/key without inventing assignments.
- Resolve ChEBI72687/84311 key ambiguity and the relationship to the occupied XFOU-PCPU sibling explicitly; audit identifier/PATHS migration where needed.
- Adjudicate all six LOTUS occurrences individually, especially the fengycin/difficidin citations; preserve full-text gaps and transfer no old-key claims automatically.
- Reassess compound-specific producer/cluster methods and xrefs; preserve original source rows, attribution, history and any unaffected curated content.
- Run guarded canary, strict/source/corpus/reproduction/site/full QC; prove unrelated owners/components and prior reviews unchanged.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/amino_acids_and_peptides/bacilysin.yaml; Complete raw YAML and all history entries; independently resolved via read_natural_product | supports | One exact minted, SEEDED owner. Neither owner has inline graphs or component references; optional mechanism, assay, clinical and target fields are absent. Histories are seeding events, not scientific sign-off. |
| resolved-owner | /private/tmp/npmech-bacilysin-review-ixdJYA/bacilysin-resolved.json; Complete native resolved JSON view; raw-YAML hash is separately attached to owner evidence | supports | The resolved object equals the complete owner content and has no component claims to hide from this inspection. |
| inventories | /private/tmp/npmech-bacilysin-review-ixdJYA/source-rows.json; Selected complete parsed rows with TSV line numbers; complete source-file hashes are in source.inputs | supports | MIBiG rows967/1406 preserve two distinct compound keys. LOTUS rows3039..3044 and9544..9545 attach six/two occurrences respectively. NPClassifier2026-09-07 calls both Small peptides/Dipeptides; a computed class does not establish peptide connectivity. Neither exact owner key occurs in pinned3-star ChEBI or AntibioticMech joins. |
| chemistry | /private/tmp/npmech-bacilysin-review-ixdJYA/chemistry.json; Pinned RDKit2026.03.5 roundtrips, functional-group SMARTS and graph-isomorphism-mapped CIP centers | supports | Every tested SMILES roundtrips its own InChI/key and neutral C12H18N2O5, exact mass270.121571676 Da. XFOU-PCPU has one amide, one acid, one primary amine, one epoxide,3 specified/2 unspecified centers. JJOS has zero amides/acids, one anhydride, two primary amines, one epoxide,4 specified/1 unspecified center. NPAtlas adds two stereo assignments to XFOU-PCPU. ChEBI disagrees at the mapped ring center; NPAtlas and ChEBI also disagree at alanine. These computations locate differences, not the correct experimental stereoisomer. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0001184.4/annotations.json; Exact version/status, compound chemistry/xrefs, taxonomy, locus bounds/methods and legacy references | supports | BGC0001184v4 is active and exactly matches stored JJOS chemistry, PubChem160175, FZB42 taxon326423 and CP000560.1:3593877..3601174. It asserts Knock-out studies and Gene expression correlated with compound production. PMID19061923 is the selected entry citation;25261512 and26268540 are additional legacy references. Source agreement does not validate the wrong graph. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/160175/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES,IsomericSMILES/JSON; CID160175 SMILES, InChI, InChIKey and formula | supports | PubChem160175 exactly matches JJOSOKMLZZVGKD-INVWQFOESA-N, not the XFOU-PCPU owner. Thus it is a nonexact xref on bacilysin-2 but an exact-to-encoded-graph xref on bacilysin; deleting the latter xref alone would not repair its wrong biological identity. |
| npatlas | https://www.npatlas.org/api/v1/compound/NPA015870?include=classifications; NPA015870 structure and original isolation metadata; mol_structures versions1/2, reassignments and embedded ClassyFire structure | supports | NPA015870 encodes XFOUAXMJRHNTOP-NWQNCHOTSA-N, with all five centers specified. Connectivity matches XFOU-PCPU but it adds alanine R and anticapsin alpha S assignments at mapped atoms1/6. It cites DOI10.1042/bj1180563. This is not exact equivalence to the partially specified owner and is not authority to fill its unknown centers. The source organism string has a spelling defect and a genus-level taxonomy field. The payload marks version1/1970 and embedded ClassyFire as the owner PCPUDTNWSA-N key, while current version2 cites DOI10.1071/ch9931443 and has NWQN. Historical agreement does not make the unversioned current xref exact; it must be qualified by version/representation. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/72687/; Released3-star CHEBI72687 definition and default structure; pinned CHEBI84311 row as protonation context | supports | CHEBI72687 describes L-alanyl and anticapsin joined by a peptide bond and encodes XFOUAXMJRHNTOP-PFQXTLEHSA-N. Its mapped ring center is S versus owner/NPA R; its alanine is S versus NPA R. Pinned CHEBI84311 is a zwitterion sharing the same StandardInChIKey. Neither is an exact owner match, and the current replacement consumer rejects this ambiguous target key. The authority disagreement requires primary stereo adjudication, not an automatic ChEBI choice. |
| pmid20070370 | PMID:20070370; EuropePMC core metadata result id=20070370; DOI:10.1111/j.1574-6968.2009.01882.x; complete returned abstract, not full text | partial | The2010 CS93 follow-up acknowledges earlier bacilysin production, sequences bacABCDE, and reports nondetection of bacilysin/chlorotetaine in its later culture-supernatant analysis. This is condition-specific, not proof that CS93 never produces bacilysin. The cited LOTUS genus occurrence needs provenance/condition qualification. |
| pmid19061923 | PMID:19061923; EuropePMC core metadata result id=19061923; DOI:10.1016/j.jbiotec.2008.10.015; complete returned abstract, not full text | partial | The FZB42 study reports residual antagonism in difficidin or sfp mutants and loss in a Delta-sfp/Delta-bac double mutant. It explicitly calls bacilysin a dipeptide. This supports a native knockout context for biological bacilysin, not the stored anhydride. The antagonism readout alone does not validate exact chemical form or the separate expression/production-correlation method. |
| pmid3121591 | PMID:3121591; EuropePMC core metadata result id=3121591; DOI:10.1128/jb.170.1.482-484.1988; complete returned abstract, not full text | partial | B.subtilis168 aro mutants were deficient in bacilysin accumulation but retained synthetase activity; tyrA/pheA mutants produced normal levels. This supports a defined precursor-pathway context, not an experiment on the JJOS anhydride. |
| pmid1841868 | PMID:1841868; EuropePMC core metadata result id=1841868; DOI:10.1007/bf02884030; complete returned abstract, not full text | partial | The study reports bacilysin-production feedback and pH/temperature effects; maximal production near pH6.8 and25C in the abstract. Detailed strain/culture/identification methods are uninspected. No assay observation is added. |
| pmid3123448 | PMID:3123448; EuropePMC core metadata result id=3123448; DOI:10.7164/antibiotics.40.1677; complete returned abstract, not full text | partial | The abstract concerns difficidin/oxydifficidin production in B.subtilis ATCC39320/39374. It does not establish bacilysin detection. Full-paper inspection is needed before accepting or rejecting the LOTUS citation; abstract silence is not whole-paper absence. |
| pmid3093430 | PMID:3093430; EuropePMC core metadata result id=3093430; DOI:10.7164/antibiotics.39.888; complete returned abstract, not full text | partial | The abstract concerns fengycin from B.subtilis F-29-3, with its chemistry/activity. It does not establish bacilysin detection. Full-paper inspection is needed before accepting or rejecting the LOTUS citation; no automatic occurrence deletion follows. |
| pmid4991476 | PMID:4991476; EuropePMC core metadata result id=4991476; DOI:10.1042/bj1180563; complete returned abstract, not full text | partial | The1970 structure abstract reports mass270, N-terminal alanine, an epoxide-ketone and a C-terminal amino acid. Its stereo assignment used an explicit reversed-Octant-rule assumption. Full chemical figures/spectra were unavailable; abstract-level identity supports a peptide, not JJOS anhydride, but does not resolve the current database stereochemical conflict. |
| pmid25261512 | PMID:25261512; EuropePMC core metadata result id=25261512; DOI:10.1128/aem.02605-14; complete returned abstract, not full text | partial | FZB42 bacB disruption abolished anticyanobacterial effect and complementation restored it; GlcNAc antagonized it. Reported expression changes concern target-organism genes and are not automatically correlation of producer bac expression with compound production. Full methods and exact product identification remain unverified. |
| pmid26268540 | PMID:26268540; EuropePMC core metadata result id=26268540; DOI:10.1038/srep12975; complete returned abstract, not full text | partial | The abstract reports FZB42 bacilysin/difficidin activity against rice-pathogen Xanthomonas, microscopy and target-organism gene-expression changes. Those expression changes do not by themselves support the stored producer-expression/production-correlation method. |
| pmid14711701 | PMID:14711701; EuropePMC core metadata result id=14711701; DOI:10.1128/aem.70.1.631-634.2004; complete returned abstract, not full text | partial | The earlier CS93 study reports HPLC and mass-spectrometric identification of bacilysin, chlorotetaine and iturin. This provides positive production/detection context despite later nondetection. FullTextXML retrieval failed twice with HTTP500, so analytical figures and exact form remain unverified. |
| literature-search | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=CS93%20AND%20bacilysin%20AND%20FIRST_PDATE:%5B1900-01-01%20TO%202010-12-31%5D&amp;format=json&amp;resultType=core&amp;pageSize=100; EuropePMC refined query CS93 AND bacilysin AND FIRST_PDATE:[1900-01-01 TO 2010-12-31] | context_only | The refined query returned two hits, the2004 identification study and2010 follow-up; both abstracts were inspected. The initial broad CS93 query returned50 hits but only25 rows and was not exhaustive. This search resolves the earlier-study lead, not absence of all other literature. |
| sequence | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=CP000560.1&amp;seq_start=3593877&amp;seq_stop=3601174&amp;rettype=gbwithparts&amp;retmode=xml; NCBI gbwithparts XML exact accession, source qualifiers and CDS features | supports | The requested CP000560.1 window3593877..3601174 is7298bp and contains complement-strand ywfG,bacE,bacD,bacC,bacB,bacA,ywfA annotations. Its feature coordinates are rebased to1..7298, not genomic coordinates. FZB42/taxon326423 source qualifiers agree; the older definition name is not a strain conflict. Sequence context does not repair the wrong chemical form. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1386,1423,679622,492670,326423&amp;retmode=xml; NCBI TaxIds1386,1423,679622,492670,326423; labels/ranks/parent relationships | supports | Labels agree with pinned records: Bacillus genus1386, B.subtilis species1423, Bacillus sp.CS93 species-rank679622, B.velezensis species492670 and FZB42 strain-rank326423. FZB42 is not the entire species. OTHER_BACTERIAL is consistent with these lineages. |
| sequence-taxonomy-audit | /private/tmp/npmech-bacilysin-review-ixdJYA/sequence-taxonomy-audit.json; Structured local parsing of both sequence snapshots, taxonomy and bounded pinned sibling candidate scan | supports | Retains sequence-window limitations and exact source features. The sibling bacilysin row is CHEBI72687/XFOU-PFQ at commit74f6cc8362498900f2fe2c13d0b6fdb66dd30976, not either owner key; absence of an automatic related_records join is correct. |
| wikidata-Q212032 | https://www.wikidata.org/wiki/Q212032; Web page title and taxon label inspected during this resumed review | supports | Q212032 resolves to Bacillus. This verifies the LOTUS organism note, not compound detection or production. |
| wikidata-Q131238 | https://www.wikidata.org/wiki/Q131238; Web page title and taxon label inspected during this resumed review | supports | Q131238 resolves to Bacillus subtilis. This verifies the LOTUS organism note, not compound detection or production. |
| wikidata-Q62873335 | https://www.wikidata.org/wiki/Q62873335; Web page title and taxon label inspected during this resumed review | supports | Q62873335 resolves to Bacillus velezensis. This verifies the LOTUS organism note, not compound detection or production. |
| bioassay-placeholder | data/raw/pubchem_bioassay.tsv; TSV9868, XFOU-PCPU/CID160175 row; complete selected row retained in source-rows.json | supports | The row is a no-assay-data placeholder with no AID, outcome, value or target. Neither owner asserts an assay from it. The CID mismatch is not hidden assay evidence and no activity is inferred. |
| governance | docs/CURATION.md; Structure correction, source-row-pinned PubChem exclusion, method-withdrawal and generated-file boundaries | supports | The replacement consumer rejects ambiguous ChEBI keys and occupied targets. Xref exclusion supports literal PubChem only, not NPAtlas. Reserved decisions.tsv is not consumed. A primary method gap alone does not authorize WITHDRAW, and no generated record or source assertion was edited. |
| resumption | /private/tmp/npmech-bacilysin-review-ixdJYA/resumption.json; Gitignore-independent full population verification; source hashes checked against original captured commit and current745da66f | supports | All3115 owners,243 components,23 prior pairs and22 receipt hashes verified. Every captured input equals both9191a148 and the resumed checkout745da66f. The intervening PR904 was publication-only administrative progress; original pre-judgement capture is retained. |
| access | /private/tmp/npmech-bacilysin-review-ixdJYA/access-limitations-final.json; Eleven source-specific limits and aliases plus182 inherited restrictions; publisher timeouts distinguished from access barriers | context_only | Full primary experimental/stereo/citation verification remains unavailable. reCAPTCHA/authorization barriers, web retrieval failures and repeated same-endpoint500 failures are distinguished. No blocked full-text source was retried through another host or tool in this continuation. |
| reassignment1993 | DOI:10.1071/ch9931443; Crossref title, authors, year and publisher URL; message.abstract is an empty jats:p element | context_only | Crossley and Stamford1993, Australian Journal of Chemistry46:1443-1446, is titled as a stereocontrolled synthesis of C4 epimers and revision of anticapsin/bacilysin configurations. NPAtlas points its current structure to this paper. Only bibliographic metadata was obtained; the title does not prove which configuration is correct or validate the NPAtlas graph. |
| reassignment-chemistry | /private/tmp/npmech-bacilysin-review-ixdJYA/reassignment-chemistry.json; RDKit comparison of NPAtlas mol_structures version1/version2 and embedded ClassyFire SMILES | supports | The NPAtlas historical version1 and embedded classifier both recompute to XFOU-PCPU, exactly the owner key. Current version2 recomputes to XFOU-NWQN. Their mapped ring centers are identical in this payload; version2 adds the two previously unspecified centers. This describes database representations, not what the1993 primary figure experimentally revised. |

## Limits And Additional Notes

- This review assesses exact committed inputs captured before judgement at9191a148. All input bytes were rechecked against current745da66f after publication; no silent hash refresh or scientific mutation occurred.
- Primary full text, chemical figures/spectra, isolate stereochemistry and detailed experimental methods remain unavailable for the eleven listed sources. Metadata/abstracts are not claimed as full-paper reading.
- Source stereo conflicts remain unresolved. ChEBI and NPAtlas are not interchangeable exact authorities, and StandardInChIKey can collapse the pinned neutral/zwitterion distinction.
- Abstract silence in fengycin/difficidin papers is not proof of absent bacilysin data; later CS93 nondetection is not proof of universal nonproduction.
- Exact versioned MIBiG JSON status was checked. Latest unversioned alias resolution or absence of a newer version is not independently established.
- Sequence context is limited to a partial CS93 cluster and the requested FZB42 genomic window with rebased feature coordinates; it is not genome-wide absence evidence.
- Native label gate includes documented skips/warnings; these are not exact-structure certification. Both records remain SEEDED.
- Review continuation only: no records, inventories, curation tables, generated pages, old reviews or GitHub objects were changed. Proposed actions are not completed curation.
- Campaign denominator remains3115; partial observations do not count as scientific completions. All prior findings and182 inherited access limits are preserved alongside eleven new limits.
- The1993 reassignment metadata has no usable abstract. Two same-publisher-page timeouts left full text unavailable; no alternative route was used. This is a retrieval limitation, not an asserted publisher denial.
- Canonical validation/save/check results are recorded after authoring, not retroactively claimed as pre-save checks.
- The optional method/citation gaps are explicit unknown assessments rather than confirmed false claims or automatic withdrawals.
- Initial validated drafts were not saved because subsequent complete NPAtlas inspection revealed a1993 reassignment lead. These final observations include that lead and preserve earlier draft/validation evidence without rewriting a saved bundle.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T140252Z-bacilysin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Bacilysin: anhydride identity conflict and FZB42 evidence scope'
started_at: '2026-10-13T13:19:20.112934Z'
finished_at: '2026-10-13T14:02:52.291755Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant/thread as earlier corpus and publication work;
    not independent human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One confirmed blocker: the stored anhydride is not the reported bacilysin
  dipeptide. Source/PubChem agreement does not repair identity. FZB42 experiments
  and all six occurrences require correct chemical scope; full stereo/method/citation
  adjudication remains partial.'
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
  - path: data/natural_products/amino_acids_and_peptides/bacilysin-2.yaml
    sha256: 7404ad2713870d8d6c5d96a2f44ed0acb73c982ae26caebf3c5321ca5b749489
    role: context
  - path: data/natural_products/amino_acids_and_peptides/bacilysin.yaml
    sha256: 47223019314c805cf63136f782a1ce259492901d987fea85cb8fa4207fa850ed
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
  - path: data/raw/pubchem_bioassay.tsv
    sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
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
- target_id: naturalproductmech:mibig-080d9481a3
  path: data/natural_products/amino_acids_and_peptides/bacilysin.yaml
  label: bacilysin
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
  description: One exact owner; same-name sibling and authority records are context
    only. The full campaign remains3115 owners and243 components.
  selection: Next exact pending owner from the exhaustive campaign checkpoint; all
    unfinished records remain in scope.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-080d9481a3
  exclusions:
  - target: Other3114 owners
    reason: Not scientifically assessed by this single-record observation; preserved
      in the full campaign checkpoint.
checks:
- check_id: strict
  name: strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/natural_products/amino_acids_and_peptides/bacilysin-2.yaml
    data/natural_products/amino_acids_and_peptides/bacilysin.yaml --out /private/tmp/npmech-bacilysin-review-ixdJYA/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  summary: Both exact owners passed strict validation with zero errors; no graph refs
    exist.
  scope_note: 'Actual run: 2026-10-13T13:19:45.015936Z to 2026-10-13T13:19:48.861148Z;
    log SHA256 137cd09860edb44bb65a94b9ffdf973b95eda4312a04e04d408261f3e8c9d1b0'
- check_id: labels
  name: labels
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  summary: Configured label gate passed:13434 canonical,646 synonyms,35 exceptions,499
    nonblocking warning mismatches and4649 no-adapter skips. Minted compound identity
    was separately checked, not certified by this gate.
  scope_note: 'Actual run: 2026-10-13T13:21:53.442743Z to 2026-10-13T13:24:37.987635Z;
    log SHA256 556ef5804e095767472c0aa8a542d5bff7e332470383a992e6b260103034414b'
- check_id: chemistry
  name: chemistry
  status: passed
  required: true
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-bacilysin-review-ixdJYA/chemistry.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  summary: Pinned RDKit calculations succeeded and located connectivity/stereo differences;
    no experimental assignment inferred.
  scope_note: 'Actual run: 2026-10-13T13:23:52.343220Z to 2026-10-13T13:23:55.776599Z;
    log SHA256 173bab471e73e274e912b85d5d946bb1efc3a7af50f87b608f51eb50a57833ee'
- check_id: ignored-inclusive-search
  name: ignored-inclusive-search
  status: passed
  required: false
  command: rg --no-ignore --hidden -l -i 'bacilysin|BGC0000888|BGC0001184|XFOUAXMJRHNTOP|JJOSOKMLZZVGKD|20070370|19061923|BJ1180563'
    . -g '!.git/**' -g '!.venv/**'
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  summary: Name, identifiers, keys and selected citations searched with ignored/hidden
    files included; only .git and .venv excluded. Curation tables/consumers were independently
    read; no implemented bacilysin-specific correction row was found in that bounded
    scope.
  scope_note: 'Actual run: 2026-10-13T13:21:54.617182Z to 2026-10-13T13:21:54.861344Z;
    log SHA256 9af702b44dbe06498fa215a16a4277335c980c1ed687ca94f3b19fc1c03633dd'
- check_id: qc
  name: qc
  status: passed
  required: true
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  summary: 'Full native QC passed: 723 passed, 3 skipped, 2 warnings in 624.50s (0:10:24).
    Strict corpus schema, history/graph tests, provenance, lint, vendored sync, site,
    reproduction and path lock passed. Run began before PR904 publication; all reviewed
    inputs remain byte-identical. It did not collect the later archive-only tests,
    which do not alter the scientific inputs.'
  scope_note: 'Actual run: 2026-10-13T13:19:43.765126Z to 2026-10-13T13:36:44.155545Z;
    log SHA256 5a0fec569bec0ad114a824c40f0eb5c8ad7a3f5f633fd3c813f49c4655b4e7c7'
- check_id: review-queue
  name: review-queue
  status: passed
  required: false
  command: .venv/bin/python scripts/curation_worklist.py --review-records --limit
    0 --tsv /private/tmp/npmech-bacilysin-review-ixdJYA/review-queue.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  summary: Full native diagnostic queue computed in the original review attempt; diagnostic
    rows are not scientific review completions.
  scope_note: 'Actual run: 2026-10-13T13:23:02.612435Z to 2026-10-13T13:24:10.580618Z;
    log SHA256 50af024fad103f35cea534dcb2175c00762261088ed58d5fc510c57559844da5'
- check_id: queue-fresh
  name: queue-fresh
  status: passed
  required: false
  command: .venv/bin/python scripts/curation_worklist.py --review-records --limit
    0 --tsv /private/tmp/npmech-bacilysin-review-ixdJYA/queue-fresh.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  summary: Full pending-record queue regenerated after this batch assessment; all3115
    owners remain included. The extra unresolved_taxa.tsv diagnostics are not owners.
  scope_note: 'Actual run: 2026-10-13T13:54:52.733389Z to 2026-10-13T13:55:34.941553Z;
    log SHA256 40d1ca7d32e428bd1f9e88c9c4a9bddc6e8e87f62190cc47fe2c7dbe935a0086'
- check_id: fulltext
  name: Primary experimental and exact chemical-form verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  evidence_ids:
  - access
  - pmid4991476
  - pmid20070370
  - pmid19061923
  - pmid14711701
  - reassignment1993
  summary: Full methods, chemical figures/spectra, isolate stereochemistry and exact
    occurrence citations remain unverified. Abstracts were read without pretending
    full-text completion. The newly identified1993 C4-reassignment paper is also unavailable
    after two same-page timeouts.
- check_id: imodulondb
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  summary: Owners contain no named gene/protein/regulator/module claims. MIBiG and
    sequence/chemical authority APIs were consulted first. Genes in contextual source
    annotations do not create a transcriptomic assertion; no iModulon dataset-absence
    claim is made.
- check_id: reassignment-chemistry
  name: Historical versus current NPAtlas structure comparison
  status: passed
  required: true
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-bacilysin-review-ixdJYA/reassignment_chemistry.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  evidence_ids:
  - reassignment-chemistry
  summary: Historical/current NPAtlas graphs and embedded classification structure
    mapped explicitly. Current identity was not inferred from an old classifier payload.
  scope_note: 'Actual run: 2026-10-13T14:01:29.688841Z to 2026-10-13T14:01:32.129437Z;
    log SHA256 ce7a368e996a15234a786cfa5f194654865259aba5dc6776ea84c0562444f1e3'
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/amino_acids_and_peptides/bacilysin.yaml
  locator: Complete raw YAML and all history entries; independently resolved via read_natural_product
  accessed_at: '2026-10-13T13:59:37.703143Z'
  support: supports
  summary: One exact minted, SEEDED owner. Neither owner has inline graphs or component
    references; optional mechanism, assay, clinical and target fields are absent.
    Histories are seeding events, not scientific sign-off.
  snapshot_sha256: 47223019314c805cf63136f782a1ce259492901d987fea85cb8fa4207fa850ed
- evidence_id: resolved-owner
  kind: record_content
  reference: /private/tmp/npmech-bacilysin-review-ixdJYA/bacilysin-resolved.json
  locator: Complete native resolved JSON view; raw-YAML hash is separately attached
    to owner evidence
  accessed_at: '2026-10-13T13:59:37.703449Z'
  support: supports
  summary: The resolved object equals the complete owner content and has no component
    claims to hide from this inspection.
  snapshot_sha256: 8d2eb425622f5b472de1faf6fbf16739184eaead972cc15692cf327a6e75dce3
- evidence_id: inventories
  kind: database
  reference: /private/tmp/npmech-bacilysin-review-ixdJYA/source-rows.json
  locator: Selected complete parsed rows with TSV line numbers; complete source-file
    hashes are in source.inputs
  accessed_at: '2026-10-13T13:59:37.703622Z'
  support: supports
  summary: MIBiG rows967/1406 preserve two distinct compound keys. LOTUS rows3039..3044
    and9544..9545 attach six/two occurrences respectively. NPClassifier2026-09-07
    calls both Small peptides/Dipeptides; a computed class does not establish peptide
    connectivity. Neither exact owner key occurs in pinned3-star ChEBI or AntibioticMech
    joins.
  snapshot_sha256: ff66f226a1839ca5af00708b058e01399cf1fd337bb410e6cfdf1fe128e40473
  search_scope: Complete structured scans of pinned source TSVs, including ignored
    files; exact owner keys plus bacilysin name/near-key candidates were inspected.
    Repository rg --no-ignore --hidden excluded only .git object data and .venv runtime
    packages. No universal live-database absence claim.
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-bacilysin-review-ixdJYA/chemistry.json
  locator: Pinned RDKit2026.03.5 roundtrips, functional-group SMARTS and graph-isomorphism-mapped
    CIP centers
  accessed_at: '2026-10-13T13:59:37.703751Z'
  support: supports
  summary: Every tested SMILES roundtrips its own InChI/key and neutral C12H18N2O5,
    exact mass270.121571676 Da. XFOU-PCPU has one amide, one acid, one primary amine,
    one epoxide,3 specified/2 unspecified centers. JJOS has zero amides/acids, one
    anhydride, two primary amines, one epoxide,4 specified/1 unspecified center. NPAtlas
    adds two stereo assignments to XFOU-PCPU. ChEBI disagrees at the mapped ring center;
    NPAtlas and ChEBI also disagree at alanine. These computations locate differences,
    not the correct experimental stereoisomer.
  snapshot_sha256: 596ac9818c52d8d56289374a583ba04c346c3129deaec58dc7804110262f19dc
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0001184.4/annotations.json
  locator: Exact version/status, compound chemistry/xrefs, taxonomy, locus bounds/methods
    and legacy references
  accessed_at: '2026-10-13T13:20:12.944187Z'
  support: supports
  summary: BGC0001184v4 is active and exactly matches stored JJOS chemistry, PubChem160175,
    FZB42 taxon326423 and CP000560.1:3593877..3601174. It asserts Knock-out studies
    and Gene expression correlated with compound production. PMID19061923 is the selected
    entry citation;25261512 and26268540 are additional legacy references. Source agreement
    does not validate the wrong graph.
  snapshot_sha256: f9ed77859cd8ac86a01f44a912d0c32ec368fe2d225ebdbd3601b4279bf3f966
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/160175/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES,IsomericSMILES/JSON
  locator: CID160175 SMILES, InChI, InChIKey and formula
  accessed_at: '2026-10-13T13:20:17.282597Z'
  support: supports
  summary: PubChem160175 exactly matches JJOSOKMLZZVGKD-INVWQFOESA-N, not the XFOU-PCPU
    owner. Thus it is a nonexact xref on bacilysin-2 but an exact-to-encoded-graph
    xref on bacilysin; deleting the latter xref alone would not repair its wrong biological
    identity.
  snapshot_sha256: 263eaadbf04fe0154071792f26fc33c00815c2ae10433a8548c11b20ab64f6fb
- evidence_id: npatlas
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA015870?include=classifications
  locator: NPA015870 structure and original isolation metadata; mol_structures versions1/2,
    reassignments and embedded ClassyFire structure
  accessed_at: '2026-10-13T13:20:23.911363Z'
  support: supports
  summary: NPA015870 encodes XFOUAXMJRHNTOP-NWQNCHOTSA-N, with all five centers specified.
    Connectivity matches XFOU-PCPU but it adds alanine R and anticapsin alpha S assignments
    at mapped atoms1/6. It cites DOI10.1042/bj1180563. This is not exact equivalence
    to the partially specified owner and is not authority to fill its unknown centers.
    The source organism string has a spelling defect and a genus-level taxonomy field.
    The payload marks version1/1970 and embedded ClassyFire as the owner PCPUDTNWSA-N
    key, while current version2 cites DOI10.1071/ch9931443 and has NWQN. Historical
    agreement does not make the unversioned current xref exact; it must be qualified
    by version/representation.
  snapshot_sha256: ff0412d0908fee40733b2435110045b36d7599eae1ab7e7483cca087f89b8688
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/72687/
  locator: Released3-star CHEBI72687 definition and default structure; pinned CHEBI84311
    row as protonation context
  accessed_at: '2026-10-13T13:22:33.136900Z'
  support: supports
  summary: CHEBI72687 describes L-alanyl and anticapsin joined by a peptide bond and
    encodes XFOUAXMJRHNTOP-PFQXTLEHSA-N. Its mapped ring center is S versus owner/NPA
    R; its alanine is S versus NPA R. Pinned CHEBI84311 is a zwitterion sharing the
    same StandardInChIKey. Neither is an exact owner match, and the current replacement
    consumer rejects this ambiguous target key. The authority disagreement requires
    primary stereo adjudication, not an automatic ChEBI choice.
  snapshot_sha256: 355f9d2300a67e633da4ac311071640b3d17a4e995045ff4b10520d664192b2d
- evidence_id: pmid20070370
  kind: primary_source
  reference: PMID:20070370
  locator: EuropePMC core metadata result id=20070370; DOI:10.1111/j.1574-6968.2009.01882.x;
    complete returned abstract, not full text
  accessed_at: '2026-10-13T13:20:28.848749Z'
  support: partial
  summary: The2010 CS93 follow-up acknowledges earlier bacilysin production, sequences
    bacABCDE, and reports nondetection of bacilysin/chlorotetaine in its later culture-supernatant
    analysis. This is condition-specific, not proof that CS93 never produces bacilysin.
    The cited LOTUS genus occurrence needs provenance/condition qualification.
  snapshot_sha256: 3b037a2e611745c1f615a607f7ac97eed10c2cb6e7c1a316cc224abdd1c3f937
- evidence_id: pmid19061923
  kind: primary_source
  reference: PMID:19061923
  locator: EuropePMC core metadata result id=19061923; DOI:10.1016/j.jbiotec.2008.10.015;
    complete returned abstract, not full text
  accessed_at: '2026-10-13T13:20:28.848749Z'
  support: partial
  summary: The FZB42 study reports residual antagonism in difficidin or sfp mutants
    and loss in a Delta-sfp/Delta-bac double mutant. It explicitly calls bacilysin
    a dipeptide. This supports a native knockout context for biological bacilysin,
    not the stored anhydride. The antagonism readout alone does not validate exact
    chemical form or the separate expression/production-correlation method.
  snapshot_sha256: 3b037a2e611745c1f615a607f7ac97eed10c2cb6e7c1a316cc224abdd1c3f937
- evidence_id: pmid3121591
  kind: primary_source
  reference: PMID:3121591
  locator: EuropePMC core metadata result id=3121591; DOI:10.1128/jb.170.1.482-484.1988;
    complete returned abstract, not full text
  accessed_at: '2026-10-13T13:20:28.848749Z'
  support: partial
  summary: B.subtilis168 aro mutants were deficient in bacilysin accumulation but
    retained synthetase activity; tyrA/pheA mutants produced normal levels. This supports
    a defined precursor-pathway context, not an experiment on the JJOS anhydride.
  snapshot_sha256: 3b037a2e611745c1f615a607f7ac97eed10c2cb6e7c1a316cc224abdd1c3f937
- evidence_id: pmid1841868
  kind: primary_source
  reference: PMID:1841868
  locator: EuropePMC core metadata result id=1841868; DOI:10.1007/bf02884030; complete
    returned abstract, not full text
  accessed_at: '2026-10-13T13:20:28.848749Z'
  support: partial
  summary: The study reports bacilysin-production feedback and pH/temperature effects;
    maximal production near pH6.8 and25C in the abstract. Detailed strain/culture/identification
    methods are uninspected. No assay observation is added.
  snapshot_sha256: 3b037a2e611745c1f615a607f7ac97eed10c2cb6e7c1a316cc224abdd1c3f937
- evidence_id: pmid3123448
  kind: primary_source
  reference: PMID:3123448
  locator: EuropePMC core metadata result id=3123448; DOI:10.7164/antibiotics.40.1677;
    complete returned abstract, not full text
  accessed_at: '2026-10-13T13:20:28.848749Z'
  support: partial
  summary: The abstract concerns difficidin/oxydifficidin production in B.subtilis
    ATCC39320/39374. It does not establish bacilysin detection. Full-paper inspection
    is needed before accepting or rejecting the LOTUS citation; abstract silence is
    not whole-paper absence.
  snapshot_sha256: 3b037a2e611745c1f615a607f7ac97eed10c2cb6e7c1a316cc224abdd1c3f937
- evidence_id: pmid3093430
  kind: primary_source
  reference: PMID:3093430
  locator: EuropePMC core metadata result id=3093430; DOI:10.7164/antibiotics.39.888;
    complete returned abstract, not full text
  accessed_at: '2026-10-13T13:20:28.848749Z'
  support: partial
  summary: The abstract concerns fengycin from B.subtilis F-29-3, with its chemistry/activity.
    It does not establish bacilysin detection. Full-paper inspection is needed before
    accepting or rejecting the LOTUS citation; no automatic occurrence deletion follows.
  snapshot_sha256: 3b037a2e611745c1f615a607f7ac97eed10c2cb6e7c1a316cc224abdd1c3f937
- evidence_id: pmid4991476
  kind: primary_source
  reference: PMID:4991476
  locator: EuropePMC core metadata result id=4991476; DOI:10.1042/bj1180563; complete
    returned abstract, not full text
  accessed_at: '2026-10-13T13:20:28.848749Z'
  support: partial
  summary: The1970 structure abstract reports mass270, N-terminal alanine, an epoxide-ketone
    and a C-terminal amino acid. Its stereo assignment used an explicit reversed-Octant-rule
    assumption. Full chemical figures/spectra were unavailable; abstract-level identity
    supports a peptide, not JJOS anhydride, but does not resolve the current database
    stereochemical conflict.
  snapshot_sha256: 3b037a2e611745c1f615a607f7ac97eed10c2cb6e7c1a316cc224abdd1c3f937
- evidence_id: pmid25261512
  kind: primary_source
  reference: PMID:25261512
  locator: EuropePMC core metadata result id=25261512; DOI:10.1128/aem.02605-14; complete
    returned abstract, not full text
  accessed_at: '2026-10-13T13:21:18.320611Z'
  support: partial
  summary: FZB42 bacB disruption abolished anticyanobacterial effect and complementation
    restored it; GlcNAc antagonized it. Reported expression changes concern target-organism
    genes and are not automatically correlation of producer bac expression with compound
    production. Full methods and exact product identification remain unverified.
  snapshot_sha256: fb8a023743633d0f3d2048df2b4bb1e99c0854661208fd0c831a00b0a1907fad
- evidence_id: pmid26268540
  kind: primary_source
  reference: PMID:26268540
  locator: EuropePMC core metadata result id=26268540; DOI:10.1038/srep12975; complete
    returned abstract, not full text
  accessed_at: '2026-10-13T13:21:18.320611Z'
  support: partial
  summary: The abstract reports FZB42 bacilysin/difficidin activity against rice-pathogen
    Xanthomonas, microscopy and target-organism gene-expression changes. Those expression
    changes do not by themselves support the stored producer-expression/production-correlation
    method.
  snapshot_sha256: fb8a023743633d0f3d2048df2b4bb1e99c0854661208fd0c831a00b0a1907fad
- evidence_id: pmid14711701
  kind: primary_source
  reference: PMID:14711701
  locator: EuropePMC core metadata result id=14711701; DOI:10.1128/aem.70.1.631-634.2004;
    complete returned abstract, not full text
  accessed_at: '2026-10-13T13:24:28.213945Z'
  support: partial
  summary: The earlier CS93 study reports HPLC and mass-spectrometric identification
    of bacilysin, chlorotetaine and iturin. This provides positive production/detection
    context despite later nondetection. FullTextXML retrieval failed twice with HTTP500,
    so analytical figures and exact form remain unverified.
  snapshot_sha256: 420e5ed3e679b35ed8e0a20ca562efc06163f40db6244dab25fbf52c25058e37
- evidence_id: literature-search
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=CS93%20AND%20bacilysin%20AND%20FIRST_PDATE:%5B1900-01-01%20TO%202010-12-31%5D&format=json&resultType=core&pageSize=100
  locator: EuropePMC refined query CS93 AND bacilysin AND FIRST_PDATE:[1900-01-01
    TO 2010-12-31]
  accessed_at: '2026-10-13T13:24:28.213945Z'
  support: context_only
  summary: The refined query returned two hits, the2004 identification study and2010
    follow-up; both abstracts were inspected. The initial broad CS93 query returned50
    hits but only25 rows and was not exhaustive. This search resolves the earlier-study
    lead, not absence of all other literature.
  snapshot_sha256: 420e5ed3e679b35ed8e0a20ca562efc06163f40db6244dab25fbf52c25058e37
  search_scope: One provider and explicit date/name query; refined hitCount2/pageSize100.
    Initial broad query was truncated to25 of50 and is not used for absence.
- evidence_id: sequence
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=CP000560.1&seq_start=3593877&seq_stop=3601174&rettype=gbwithparts&retmode=xml
  locator: NCBI gbwithparts XML exact accession, source qualifiers and CDS features
  accessed_at: '2026-10-13T13:21:27.020992Z'
  support: supports
  summary: The requested CP000560.1 window3593877..3601174 is7298bp and contains complement-strand
    ywfG,bacE,bacD,bacC,bacB,bacA,ywfA annotations. Its feature coordinates are rebased
    to1..7298, not genomic coordinates. FZB42/taxon326423 source qualifiers agree;
    the older definition name is not a strain conflict. Sequence context does not
    repair the wrong chemical form.
  snapshot_sha256: c1aa1542c1c11d48d2580fac1b98b1be63dc74239af71aef18176cb997f14ffe
- evidence_id: taxonomy
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1386,1423,679622,492670,326423&retmode=xml
  locator: NCBI TaxIds1386,1423,679622,492670,326423; labels/ranks/parent relationships
  accessed_at: '2026-10-13T13:21:53.291743Z'
  support: supports
  summary: 'Labels agree with pinned records: Bacillus genus1386, B.subtilis species1423,
    Bacillus sp.CS93 species-rank679622, B.velezensis species492670 and FZB42 strain-rank326423.
    FZB42 is not the entire species. OTHER_BACTERIAL is consistent with these lineages.'
  snapshot_sha256: 94395e7c21734b9fcf57714fb767cb383271478de590c27178532b388e5faefc
- evidence_id: sequence-taxonomy-audit
  kind: validation
  reference: /private/tmp/npmech-bacilysin-review-ixdJYA/sequence-taxonomy-audit.json
  locator: Structured local parsing of both sequence snapshots, taxonomy and bounded
    pinned sibling candidate scan
  accessed_at: '2026-10-13T13:59:37.713303Z'
  support: supports
  summary: Retains sequence-window limitations and exact source features. The sibling
    bacilysin row is CHEBI72687/XFOU-PFQ at commit74f6cc8362498900f2fe2c13d0b6fdb66dd30976,
    not either owner key; absence of an automatic related_records join is correct.
  snapshot_sha256: 2a0ccd40e746f08ef82219fa7937af53c23b83042d7870e0654b342d78d17a56
- evidence_id: wikidata-Q212032
  kind: database
  reference: https://www.wikidata.org/wiki/Q212032
  locator: Web page title and taxon label inspected during this resumed review
  accessed_at: '2026-10-13T13:59:37.713469Z'
  support: supports
  summary: Q212032 resolves to Bacillus. This verifies the LOTUS organism note, not
    compound detection or production.
- evidence_id: wikidata-Q131238
  kind: database
  reference: https://www.wikidata.org/wiki/Q131238
  locator: Web page title and taxon label inspected during this resumed review
  accessed_at: '2026-10-13T13:59:37.713478Z'
  support: supports
  summary: Q131238 resolves to Bacillus subtilis. This verifies the LOTUS organism
    note, not compound detection or production.
- evidence_id: wikidata-Q62873335
  kind: database
  reference: https://www.wikidata.org/wiki/Q62873335
  locator: Web page title and taxon label inspected during this resumed review
  accessed_at: '2026-10-13T13:59:37.713481Z'
  support: supports
  summary: Q62873335 resolves to Bacillus velezensis. This verifies the LOTUS organism
    note, not compound detection or production.
- evidence_id: bioassay-placeholder
  kind: database
  reference: data/raw/pubchem_bioassay.tsv
  locator: TSV9868, XFOU-PCPU/CID160175 row; complete selected row retained in source-rows.json
  accessed_at: '2026-10-13T13:59:37.713500Z'
  support: supports
  summary: The row is a no-assay-data placeholder with no AID, outcome, value or target.
    Neither owner asserts an assay from it. The CID mismatch is not hidden assay evidence
    and no activity is inferred.
- evidence_id: governance
  kind: record_content
  reference: docs/CURATION.md
  locator: Structure correction, source-row-pinned PubChem exclusion, method-withdrawal
    and generated-file boundaries
  accessed_at: '2026-10-13T13:59:37.713503Z'
  support: supports
  summary: The replacement consumer rejects ambiguous ChEBI keys and occupied targets.
    Xref exclusion supports literal PubChem only, not NPAtlas. Reserved decisions.tsv
    is not consumed. A primary method gap alone does not authorize WITHDRAW, and no
    generated record or source assertion was edited.
- evidence_id: resumption
  kind: validation
  reference: /private/tmp/npmech-bacilysin-review-ixdJYA/resumption.json
  locator: Gitignore-independent full population verification; source hashes checked
    against original captured commit and current745da66f
  accessed_at: '2026-10-13T13:59:37.713522Z'
  support: supports
  summary: All3115 owners,243 components,23 prior pairs and22 receipt hashes verified.
    Every captured input equals both9191a148 and the resumed checkout745da66f. The
    intervening PR904 was publication-only administrative progress; original pre-judgement
    capture is retained.
  snapshot_sha256: 3210e0cfa8cd199f1d4dca40292855e4e6839e60f51c51a2b18a7176e48cfbf8
- evidence_id: access
  kind: validation
  reference: /private/tmp/npmech-bacilysin-review-ixdJYA/access-limitations-final.json
  locator: Eleven source-specific limits and aliases plus182 inherited restrictions;
    publisher timeouts distinguished from access barriers
  accessed_at: '2026-10-13T14:02:52.291577Z'
  support: context_only
  summary: Full primary experimental/stereo/citation verification remains unavailable.
    reCAPTCHA/authorization barriers, web retrieval failures and repeated same-endpoint500
    failures are distinguished. No blocked full-text source was retried through another
    host or tool in this continuation.
  snapshot_sha256: 47f68baa42b8bbf56605cd1cf24916318eae2c210cdc871f27d9173cdd096950
- evidence_id: reassignment1993
  kind: database
  reference: DOI:10.1071/ch9931443
  locator: Crossref title, authors, year and publisher URL; message.abstract is an
    empty jats:p element
  accessed_at: '2026-10-13T14:00:28.982267Z'
  support: context_only
  snapshot_sha256: 5cd859dbb609271817db4649771dc9da994a8adda97dc2a319e24fa7256de9e0
  summary: Crossley and Stamford1993, Australian Journal of Chemistry46:1443-1446,
    is titled as a stereocontrolled synthesis of C4 epimers and revision of anticapsin/bacilysin
    configurations. NPAtlas points its current structure to this paper. Only bibliographic
    metadata was obtained; the title does not prove which configuration is correct
    or validate the NPAtlas graph.
- evidence_id: reassignment-chemistry
  kind: validation
  reference: /private/tmp/npmech-bacilysin-review-ixdJYA/reassignment-chemistry.json
  locator: RDKit comparison of NPAtlas mol_structures version1/version2 and embedded
    ClassyFire SMILES
  accessed_at: '2026-10-13T14:01:32.129437Z'
  support: supports
  snapshot_sha256: 7a5eee97afad8bfe8c99209b9f5b511536c2f0adab288731e56efc117feeb388
  summary: The NPAtlas historical version1 and embedded classifier both recompute
    to XFOU-PCPU, exactly the owner key. Current version2 recomputes to XFOU-NWQN.
    Their mapped ring centers are identical in this payload; version2 adds the two
    previously unspecified centers. This describes database representations, not what
    the1993 primary figure experimentally revised.
assessments:
- assessment_id: identity
  area: identity
  topic: Connectivity and supported stereochemical resolution
  outcome: concern
  summary: The encoded anhydride has no peptide bond and therefore is not the reported
    bacilysin dipeptide. Matching MIBiG/PubChem identifiers, mass and formula do not
    repair identity. F1 blocks exact-structure origin and occurrence attribution.
    NPAtlas explicitly retains a historical exact-owner structure but identifies a
    different current form with a1993 reassignment citation. Primary revision details
    must be checked before selecting an authority or altering stereochemistry.
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  evidence_ids:
  - owner
  - chemistry
  - chebi
  - npatlas
  - pmid4991476
  - pmid19061923
  - reassignment1993
  - reassignment-chemistry
  dimensions:
  - name: exact-key
    value: JJOSOKMLZZVGKD-INVWQFOESA-N
    definition: Current owner key, not a replacement proposal
    evidence_ids:
    - owner
    - chemistry
  - name: stereo-resolution
    value: 4 specified/1 unspecified center
    definition: Encoded RDKit chiral centers; not independent experimental assignments
    evidence_ids:
    - chemistry
- assessment_id: xref
  area: grounding
  topic: Exact equivalence and grounding candidates
  outcome: supported
  summary: The PubChem xref exactly matches the stored graph. That is accurate database
    equivalence, not correct natural-product identity. ChEBI and the sibling bacilysin
    key differ; withholding a same-name join is appropriate. NPAtlas explicitly retains
    a historical exact-owner structure but identifies a different current form with
    a1993 reassignment citation. Primary revision details must be checked before selecting
    an authority or altering stereochemistry.
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  evidence_ids:
  - owner
  - pubchem
  - npatlas
  - chebi
  - chemistry
  - sequence-taxonomy-audit
  - reassignment1993
  - reassignment-chemistry
- assessment_id: classification
  area: provenance
  topic: Computed filing versus asserted chemistry and taxonomic facets
  outcome: supported
  summary: NPClassifier filing, Small peptides/Dipeptides, tool/version and non-glycoside
    output match pinned rows. Source BGC OTHER remains a separate assertion, as do
    OTHER_BACTERIAL taxon facets. A computed dipeptide prediction is not validation
    of an amide bond.
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  evidence_ids:
  - inventories
  - mibig
  - taxonomy
  - chemistry
- assessment_id: producer
  area: evidence
  topic: Strain, source tier and condition-specific experimental context
  outcome: concern
  summary: Native FZB42 knockout/complementation context supports biological bacilysin
    at abstract level, consistent with a characterized evidence tier. It does not
    demonstrate production of the JJOS anhydride. F1 blocks chemical scope despite
    correct taxon/strain provenance.
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  evidence_ids:
  - owner
  - mibig
  - taxonomy
  - sequence
  - pmid14711701
  - pmid20070370
  - pmid19061923
  - pmid25261512
  dimensions:
  - name: strain-context
    value: FZB42; NCBITaxon326423 (strain rank)
    definition: Source strain context and live taxonomic rank; not broader species-wide
      experiments
    evidence_ids:
    - taxonomy
    - sequence
  - name: stored-evidence-tier
    value: BGC_CHARACTERIZED; CLUSTER_DEMONSTRATED
    definition: Existing source-derived taxon and locus grades, not review upgrades
    evidence_ids:
    - owner
    - mibig
- assessment_id: bgc
  area: evidence
  topic: Versioned entry, genomic interval and exact locus methods
  outcome: unknown
  summary: Active version4 and the7298bp requested FZB42 window agree with bac gene
    context. Knockout evidence is supported at abstract level, but the separate producer-expression/production-correlation
    method remains unverified. Target-organism expression changes in later papers
    cannot substitute for it. No method withdrawal follows from missing full text.
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  evidence_ids:
  - mibig
  - sequence
  - sequence-taxonomy-audit
  - pmid19061923
  - pmid25261512
  - pmid26268540
- assessment_id: occurrences
  area: evidence
  topic: Every LOTUS citation and taxonomic scope
  outcome: concern
  summary: All six DOI identities and organism notes resolve at metadata/label level.
    The1970,1988,1990 andFZB42 studies concern biological bacilysin, not JJOS. Fengycin
    and difficidin-paper abstracts do not establish bacilysin occurrence, but full-paper
    silence/false citation is not proven. F1 blocks exact-key attribution; every occurrence
    needs individual adjudication before any identity correction transfers claims.
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  evidence_ids:
  - inventories
  - pmid20070370
  - pmid14711701
  - pmid4991476
  - pmid3121591
  - pmid1841868
  - pmid3093430
  - pmid3123448
  - pmid19061923
  - taxonomy
  - wikidata-Q212032
  - wikidata-Q131238
  - wikidata-Q62873335
- assessment_id: completeness
  area: completeness
  topic: Optional assays, mechanisms, proteins, clinical assertions and history
  outcome: unknown
  summary: Complete resolved owners have no graphs/components, pathway steps, assays,
    targets, clinical assertions or related_records. These optional omissions are
    not false claims. The BioAssay placeholder is correctly not used as activity.
    Literature gives leads for future mechanism curation only after exact identity
    and full experimental support are established; no evidence/history/status change
    was made.
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  evidence_ids:
  - owner
  - resolved-owner
  - bioassay-placeholder
  - sequence-taxonomy-audit
  - pmid25261512
  - pmid3121591
  - governance
- assessment_id: validation
  area: schema
  topic: Native deterministic validation and exhaustive scope preservation
  outcome: supported
  summary: Native strict, label, full QC and queue checks passed with their real receipts.
    Captured sources match the original9191a148 tree and current745da66f; all3115
    owners/243 components/23 prior pairs remain unchanged. Deterministic validation
    does not certify scientific correctness or close any prior finding.
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  evidence_ids:
  - owner
  - resumption
  - governance
findings:
- finding_id: F1
  issue_key: bacilysin-BGC0001184-anhydride-wrong-connectivity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stored anhydride is not the bacilysin dipeptide
  description: JJOSOKMLZZVGKD-INVWQFOESA-N has an acid-anhydride linkage, zero amide
    bonds and two free primary amines. Biological bacilysin is the alanine/anticapsin
    dipeptide supported by the inspected primary abstracts and ChEBI definition. MIBiG
    and PubChem reproduce the same wrong graph; a formula/mass match or exact-to-current-graph
    xref does not validate it. Producer, origin, cluster-product and occurrence assertions
    cannot be carried onto this chemically different graph.
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  field_paths:
  - label
  - chemical_structure
  - biosynthesis_origin
  - producer_organisms
  - biosynthetic_gene_clusters
  - occurrences
  evidence_ids:
  - owner
  - chemistry
  - mibig
  - pubchem
  - chebi
  - pmid4991476
  - pmid19061923
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned original compound, producer and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Pinned original exact-key organism/citation triples
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: Occurrence extraction and provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained source harmonization and generated record emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Narrow REPLACE_WITH_CHEBI path; ambiguous keys and occupied targets rejected
  rule_id: review-checklist:Identity; Structure; docs/HARMONIZATION.md:The unit of
    the corpus is a structure
  native_severity: blocker
  normalization_reason: Wrong bond connectivity changes the molecule denoted by the
    record and blocks exact-structure biological attribution.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-080d9481a3
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned original compound, producer and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Pinned original exact-key organism/citation triples
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: Occurrence extraction and provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained source harmonization and generated record emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Narrow REPLACE_WITH_CHEBI path; ambiguous keys and occupied targets rejected
  description: 'Adjudicate and repair or quarantine BGC0001184:1 through a tested
    source-pinned path, with exact stereochemical resolution and chemical-form scope.
    Do not select ChEBI blindly: the pinned bacilysin/zwitterion pair shares a key
    that the current replacement consumer rejects as ambiguous. Do not merge into
    the differently stereospecified sibling or transfer its claims by name. Removing
    PubChem alone is not an identity repair.'
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Inspect the1993 Crossley/Stamford C4-reassignment paper and reconcile its actual
    figures/assignments with NPAtlas historical/current payloads and ChEBI; infer
    no correction direction from title alone.
  - Confirm primary peptide connectivity, supported isolate stereochemistry and intended
    protonation/form; recompute SMILES/InChI/key without inventing assignments.
  - Resolve ChEBI72687/84311 key ambiguity and the relationship to the occupied XFOU-PCPU
    sibling explicitly; audit identifier/PATHS migration where needed.
  - Adjudicate all six LOTUS occurrences individually, especially the fengycin/difficidin
    citations; preserve full-text gaps and transfer no old-key claims automatically.
  - Reassess compound-specific producer/cluster methods and xrefs; preserve original
    source rows, attribution, history and any unaffected curated content.
  - Run guarded canary, strict/source/corpus/reproduction/site/full QC; prove unrelated
    owners/components and prior reviews unchanged.
limitations:
- This review assesses exact committed inputs captured before judgement at9191a148.
  All input bytes were rechecked against current745da66f after publication; no silent
  hash refresh or scientific mutation occurred.
- Primary full text, chemical figures/spectra, isolate stereochemistry and detailed
  experimental methods remain unavailable for the eleven listed sources. Metadata/abstracts
  are not claimed as full-paper reading.
- Source stereo conflicts remain unresolved. ChEBI and NPAtlas are not interchangeable
  exact authorities, and StandardInChIKey can collapse the pinned neutral/zwitterion
  distinction.
- Abstract silence in fengycin/difficidin papers is not proof of absent bacilysin
  data; later CS93 nondetection is not proof of universal nonproduction.
- Exact versioned MIBiG JSON status was checked. Latest unversioned alias resolution
  or absence of a newer version is not independently established.
- Sequence context is limited to a partial CS93 cluster and the requested FZB42 genomic
  window with rebased feature coordinates; it is not genome-wide absence evidence.
- Native label gate includes documented skips/warnings; these are not exact-structure
  certification. Both records remain SEEDED.
- 'Review continuation only: no records, inventories, curation tables, generated pages,
  old reviews or GitHub objects were changed. Proposed actions are not completed curation.'
- Campaign denominator remains3115; partial observations do not count as scientific
  completions. All prior findings and182 inherited access limits are preserved alongside
  eleven new limits.
- The1993 reassignment metadata has no usable abstract. Two same-publisher-page timeouts
  left full text unavailable; no alternative route was used. This is a retrieval limitation,
  not an asserted publisher denial.
notes:
- Canonical validation/save/check results are recorded after authoring, not retroactively
  claimed as pre-save checks.
- The optional method/citation gaps are explicit unknown assessments rather than confirmed
  false claims or automatic withdrawals.
- Initial validated drafts were not saved because subsequent complete NPAtlas inspection
  revealed a1993 reassignment lead. These final observations include that lead and
  preserve earlier draft/validation evidence without rewriting a saved bundle.
```
