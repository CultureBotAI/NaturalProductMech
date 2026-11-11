# Acinetobactin: resolve historical structure assignment and incompatible PubChem link

- Review: 20261021T103933Z-acinetobactin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T10:26:33.353397Z
- Finished UTC: 2026-10-21T10:39:33.268660Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The stored historical oxazoline lacks two specified centres and does not identify the rearranged structure assigned to acinetobactin by later primary work. The PubChem link resolves to a distinct tautomer and stereochemical entity. The required 2004 native experiment remains inaccessible, so primary-backed identity migration and source-claim admission must be adjudicated together through maintained, guarded inputs.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 40, batch 004, selected in path order from the fresh-main authoritative validated catalogue and the separately validated pending-PR targets. At selection, 84 of 3116 current records had campaign coverage and 3032 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-75969a8e53 | data/natural_products/alkaloids/acinetobactin.yaml | generated | acinetobactin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-75969a8e53 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-75969a8e53 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-75969a8e53 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-75969a8e53 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-75969a8e53 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-75969a8e53 | The full documented just qc recipe passed against the new main revision. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Primary structure, name and stereochemical identity | failed | True | naturalproductmech:mibig-75969a8e53 | The historical name and partial oxazoline graph do not resolve to one exact modern product. The primary revision and two explicitly different drawings require a guarded identity/source-admission decision. |
| Exact chemical cross-reference equivalence | failed | True | naturalproductmech:mibig-75969a8e53 | NPAtlas matches the current partial graph, but PubChem5492097 asserts a different tautomer/stereochemical entity and cannot be retained as an exact xref. |
| Exact historical native product and cluster experiment verification | unavailable | True | naturalproductmech:mibig-75969a8e53 | The required 2004 original main body was unavailable. Its abstract cannot assign each native production/disruptant phenotype to the fully specified precursor or rearranged product, so native method upgrades and automatic claim transfer remain unresolved. |

## Scientific And Domain Assessments

### Revised name, constitutional isomer and stereochemistry

identity: concern. Targets: naturalproductmech:mibig-75969a8e53.

The source graph is internally consistent and truthfully incomplete, but a single natural-product identity is not resolved. Neutral primary-drawing candidates are precursor FCWIGDCVHNNXFS-RNCFNFMXSA-N and modern acinetobactin YQXURFXJBIFMOA-ZANVPECISA-N. Select neither merely by name or database consensus; adjudicate source claims and a maintained migration.

### Authority equivalence and current grounding

identity: concern. Targets: naturalproductmech:mibig-75969a8e53.

NPA018669 and two-star CHEBI:211033 reproduce the historical partial graph; neither resolves the modern nomenclature. MINTED is appropriate for that graph under the three-star rule. PubChem5492097 fails exact equivalence. No eligible current replacement has been established; candidate-key API failures are not absence proof.

### Native origin, occurrence and citation independence

evidence: unknown. Targets: naturalproductmech:mibig-75969a8e53.

Native A. baumannii siderophore production is documented at historical-name level, with ATCC19606 in the 1994/2004 abstracts and ATCC17978 natural modern material in the 2016 SI. The one LOTUS occurrence and MIBiG producer cite the same 2004 publication. Exact modern-isomer applicability of that historical row remains unverified; no automatic old-key claim transfer or whole-species negative inference is justified.

### Native locus and method applicability

evidence: unknown. Targets: naturalproductmech:mibig-75969a8e53.

The generated AB101202.1 interval, species, PMID and empty-method SOURCE_ASSERTION/CLUSTER_UNSTATED grades faithfully match current MIBiG. The 2004 abstract reports selected disruptants but does not provide the target-resolved experiment details needed here. Later Pseudomonas enzyme reconstitution and recombinant BauA binding cannot upgrade this native biosynthetic claim.

### Taxonomy, source provenance and generated audit history

provenance: supported. Targets: naturalproductmech:mibig-75969a8e53.

NCBITaxon:470 and Wikidata Q3241189 agree on A. baumannii. The source uses the species rank; ATCC19606 is the historical study stock and current taxon type material. The owner preserves source version and the same-publication warning. SEEDED status/history correctly record generation; this review does not alter them.

### Computed chemical classification and source BGC class

provenance: supported. Targets: naturalproductmech:mibig-75969a8e53.

ALKALOIDS and the NPClassifier Histidine alkaloids/Imidazole alkaloids/non-glycoside output match the exact committed old-key prediction; NRPS is separately the MIBiG locus class. These are different classifications. Any future full-key correction must re-evaluate the generated prediction rather than carry the old-key result without provenance.

### Optional mechanisms, proteins, bioactivity and regulation

completeness: not_applicable. Targets: naturalproductmech:mibig-75969a8e53.

No protein, molecular target, pathway step, graph or activity claim is present, and the source PubChem inventory has no assay data. Rich later ligand-binding and proposed pathway literature does not create an omission finding. A. baumannii precise139 is an available iModulon lead, but no owner gene assertion supplies a justified target-specific regulatory mapping.

## Findings

### S040-F-IDENTITY: The historical name and partial graph do not define the modern exact product

blocker / open / confirmed; issue key: mibig-bgc0000294-compound1-historical-identity-resolution.

The owner retains the historical acinetobactin name for an unspecified oxazoline. Primary reassignment and explicit later drawings distinguish stereodefined preacinetobactin from rearranged modern acinetobactin. The false equivalence is confirmed; the correct migration destination for the historical source assertions still needs claim-specific adjudication. This is more than an optional synonym or missing stereo_complete flag.

### S040-F-XREF: PubChem5492097 does not identify the stored exact structure

major / open / confirmed; issue key: mibig-bgc0000294-compound1-pubchem5492097-not-exact.

The current linked CID assigns a keto/enamine tautomer, Z geometry and two R centres, while the stored graph has two unspecified centres. Primary preacinetobactin instead assigns C4-prime S/C5-prime R. The modern rearranged acinetobactin is a different heavy-atom graph. Shared formula, historical label or tautomer canonicalization that drops stereo cannot establish exact equivalence. This xref can be withheld independently before the larger identity decision.

## Recommended Actions And Acceptance Checks

### S040-A-RESOLVE-IDENTITY

Adjudicate BGC0000294:1 version 5 against the 2009 revision, 2016 SI Tables S2/S3 and 2018 Figure1, pinning complete raw-row SHA256 bf1c35da9f7064b24c9ecdf90aa8cceacb3bf2d25a030584d18fc7839d84324f. Implement a consumed manual primary-backed name/structure and claim-admission extension in the structure-correction loader/seeder before entering its decision in curation/mibig_structure_corrections.tsv; the existing two ChEBI-only actions cannot admit two-star CHEBI:211033 or an arbitrary primary structure. The neutral primary candidates are preacinetobactin FCWIGDCVHNNXFS-RNCFNFMXSA-N and modern acinetobactin YQXURFXJBIFMOA-ZANVPECISA-N. Do not choose one merely from a name lookup. Retrieve the required 2004 exact experimental context or explicitly withhold/qualify unresolved native and occurrence claims using a tested consumed admission mechanism. Retain raw source labels and full rows as provenance. Bind any admitted ATCC19606 producer, locus reference and old-key LOTUS triple (SHA256 d7747f3cf812e61457e7535e22ea5d7ee724dd45b8d32a53a7f983e917f24d2e) to the adjudicated chemical entity; do not transfer them silently. If a unique eligible three-star target later becomes available, verify its complete structure before using that existing route. Reserved decisions.tsv is not a consumer.

- Source chemistry, name, taxon, citation, interval, methods and xrefs are covered by the full raw-row pin; any drift fails closed. Primary transcriptions recompute the intended key, formula, stereocentres and neutral-parent form, with TFA salt provenance retained.
- The emitted owner has one unambiguous primary-supported label/full structure and an explicit identity/path migration; it neither merges precursor and rearranged product nor treats the old incomplete key as an exact synonym. Collision searches include ignored files.
- Each retained producer, locus and occurrence assertion is independently admitted for that exact candidate. Historical PMID/DOI equivalence is preserved; insufficient exact-isomer evidence is withheld or explicitly scoped rather than upgraded from an abstract. ATCC19606 and ATCC17978 contexts remain distinct.
- A combined canary tests structural correction with xref exclusions, claim-reference routing, strain/isolate qualification and old-key LOTUS provenance. Current structure_correction_note guards must be deliberately extended with target-specific pins; merely refreshing existing pins or suppressing errors is insufficient.
- The old-key LOTUS and PubChem no-assay rows remain traceable and are not automatically copied to a new key. Stale chemical xrefs are withheld; any admitted replacement is independently exact. NPClassifier output is regenerated or explicitly left unresolved for a changed key.
- Strict validation, source reproducibility, reviewable PATHS/identifier migration and repository quality gates pass after implementation; no optional activity, protein or regulatory assertion is manufactured.

### S040-A-EXCLUDE-XREF

Add the literal pubchem:5492097 exclusion for BGC0000294:1 to curation/mibig_xref_exclusions.tsv, with full raw-row SHA256 bf1c35da9f7064b24c9ecdf90aa8cceacb3bf2d25a030584d18fc7839d84324f, stable primary/authority reference, curator/date and rationale distinguishing tautomer representation from the independent stereochemical mismatch. Keep raw database_ids unchanged and retain exclusion provenance. This existing loader supports withholding the current xref now. If combined with the identity correction, implement explicit composition or retire/supersede the exclusion with equivalent pinned provenance after all old xrefs are withheld; the current seeder rejects the simultaneous structure-correction/exclusion combination.

- The exact current raw row and literal pubchem:5492097 assertion match the pinned SHA; drift or a missing source xref fails closed.
- An isolated generation removes only this incompatible generated xref at the current identity, preserves the raw assertion and emits the exclusion rationale; NPA018669 is not falsely rejected for its faithful match to the current partial graph.
- No source row, alias normalization or later generator pass reintroduces the excluded CID. Equal formula or stereo-erasing tautomer normalization does not pass exact equivalence.
- The combined identity/xref case is explicitly tested and either composes under new target-specific guards or has a documented provenance-preserving supersession; the unsupported current combination is not assumed to work.
- Strict validation and seed reproducibility pass after the maintained correction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| S040-OWNER | data/natural_products/alkaloids/acinetobactin.yaml; Complete generated owner and resolved content, including all source, occurrence, producer, locus, classification, identifier and history fields | supports | The owner calls a two-centre-unspecified oxazoline acinetobactin, full key FCWIGDCVHNNXFS-UHFFFAOYSA-N. It has one LOTUS species occurrence and one MIBiG source-asserted producer/locus; no activity, named protein, biosynthetic step or graph is asserted. stereo_complete:false accurately describes the stored graph. |
| S040-RAW | data/raw/mibig_compounds.tsv; Complete BGC0000294:1 version 5 row; matched LOTUS, NPClassifier and PubChem no-assay rows compared separately | supports | The raw MIBiG row exactly reproduces the old oxazoline graph, source label, NPA018669/PubChem5492097 identifiers, taxon 470, AB101202.1:3950..30424 and PMID:15289555 with empty locus methods. Full canonical MIBiG row SHA256 bf1c35da9f7064b24c9ecdf90aa8cceacb3bf2d25a030584d18fc7839d84324f. The single LOTUS row uses the same old key and DOI:10.1099/MIC.0.27141-0; full LOTUS row SHA256 d7747f3cf812e61457e7535e22ea5d7ee724dd45b8d32a53a7f983e917f24d2e. |
| S040-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0000294.5/annotations.json; BGC0000294 version 5: complete compounds[0], taxonomy, locus and legacy reference | supports | Current MIBiG retains the source graph and label, two original xrefs, A. baumannii taxon 470, NRPS Type I, active/questionable/unknown status and AB101202.1:3950..30424 with no locus evidence methods. PMID:15289555 is entry-level. Source fidelity does not resolve the later primary structure revision. |
| S040-NPATLAS | https://www.npatlas.org/api/v1/compound/NPA018669; NPA018669 complete current chemical data, original source and organism | supports | NPAtlas NPA018669 exactly matches the current owner full InChIKey and its unspecified stereochemistry. Its Acinetobactin name and A. baumannii origin trace to the original 1994 DOI:10.1007/bf00301846; the current entry does not implement the later structural reassignment. It is a faithful xref to the current partial graph, not independent proof that the modern named product is that graph. |
| S040-PUBCHEM | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5492097/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES,IsomericSMILES/JSON; CID 5492097 complete returned InChI, key, formula and SMILES | supports | The stored xref now resolves to DYESEQWBWHUEDV-PVBSNRTBSA-N, C16H18N4O5: a keto/enamine representation with an exocyclic Z alkene and two assigned centres. Its heavy-atom connectivity layer matches the oxazoline graph, not the rearranged modern isoxazolidinone. The stereochemical mapping is C4-prime R/C5-prime R, differing from primary preacinetobactin C4-prime S/C5-prime R as well as from the owner’s unspecified graph. |
| S040-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/211033/; CHEBI:211033 rating, default Standard InChI and compound origin; corroborating official MOL | supports | The current released entry is two-star, named Acinetobactin, and carries the exact old partial key FCWIGDCVHNNXFS-UHFFFAOYSA-N. Its origin again cites the historical 1994 paper. The official MOL independently recomputes this key with two unspecified centres. It is ineligible for the repository’s three-star grounding/structure-replacement route. |
| S040-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/211033/; Complete official CHEBI:211033 MOL parsed without modifying its chemistry | supports | The official MOL is chemically parseable and has the owner’s exact Standard InChIKey with two unspecified stereocentres. This avoids relying on an unbracketed imidazole SMILES representation or silently changing it. |
| S040-TAXON | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=470&amp;retmode=xml; Complete taxon 470 scientific name, rank, lineage and type material | supports | NCBITaxon:470 is the bacterial species Acinetobacter baumannii; ATCC 19606 is listed as type material. The current broad species label and OTHER_BACTERIAL grouping are consistent. The exact 2004 study stock is ATCC 19606T, not ATCC 17978 used for the later natural-versus-synthetic comparison. |
| S040-WIKIDATA | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q3241189&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Q3241189 English label and P685 taxon value | supports | The exact organism identifier retained in the LOTUS note resolves to Acinetobacter baumannii and NCBI taxonomy 470. |
| S040-REVISION | https://pmc.ncbi.nlm.nih.gov/articles/PMC2676571/; DOI:10.1021/ja900815w; PMID:19320483; complete main narrative and Figure 2 caption, especially the final reassignment paragraphs | supports | The primary authors reassign acinetobactin to isoxazolidinone compound 5 because its proton NMR agrees with the original isolation data; they rename oxazoline 1 pre-acinetobactin. The experimental assembly uses purified Pseudomonas entomophila PmsD/PmsE/PmsG with substituted 2,3-dihydroxybenzoate, threonine and synthetic N-hydroxyhistamine; a spontaneous nonenzymatic rearrangement follows. These experiments do not directly characterize native A. baumannii Bas proteins or prove natural Pseudomonas secretion. |
| S040-SI-STRUCTURE | https://s3-eu-west-1.amazonaws.com/pstorage-acs-6854636/3636072/id5b00145_si_001.pdf; DOI:10.1021/acsinfecdis.5b00145; original Tables S2/S3 and drawings on S24/S32; synthesis S4-S8; all SI text and captions read | supports | The primary numbered drawings distinguish pre-acinetobactin 1a, C4-prime S/C5-prime R, from rearranged acinetobactin 1b, C4-prime S/C5-prime S. Both NMR tables concern TFA salts. Neutral-parent graph candidates were transcribed by omitting the counterion; they are not claims that the assayed material was a free base. The synthesis starts with L-threonine benzyl ester. Detailed spectra were not independently reinterpreted. |
| S040-SI-SCOPE | https://s3-eu-west-1.amazonaws.com/pstorage-acs-6854636/3636072/id5b00145_si_001.pdf; S11-S23 and S40-S41: Table S1, Figures S13-S16 and S35-S36; proposed Scheme S1 S2-S3 | supports | The SI reports pH-dependent nonenzymatic conversion, natural ATCC 17978 acinetobactin versus synthetic material by CD and MS/MS, and supplied ferric-ligand growth responses in ATCC 17978 and ATCC 19606 with specified mutant labels. MS/MS fragments alone do not distinguish the isomers. The Bas/Bau/Bar scheme is explicitly proposed, and these data do not individually demonstrate every biosynthetic or transport reaction. No native ATCC 19606 exact-isomer production assignment is inferred from ATCC 17978 CD or from supplied-ligand growth. |
| S040-BAUA | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6300358/fullTextXML; DOI:10.7554/eLife.42270; PMID:30558715; complete Results, Discussion and Methods, Tables 1-2 and original Figure 1A pixels | supports | Figure 1 independently confirms the two structures and stereochemical drawings. Recombinant mature BauA from ATCC 19606, expressed in E. coli and purified, binds ferric preacinetobactin by ITC; the purified acinetobactin-only samples do not show detected binding. The mixed ferric preacinetobactin/acinetobactin complex and impurity control support a ligand-recognition distinction. Whole-cell transport and every proposed downstream step were not directly measured in this structural study; the reported minor crystal diastereomer is not an established natural configuration. |
| S040-HISTORICAL | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:7802543%20OR%20EXT_ID:27624967%20OR%20EXT_ID:15289555&amp;format=json&amp;resultType=core; Complete original abstracts and PMID/DOI metadata for PMID:7802543, PMID:15289555 and PMID:27624967 | supports | The 1994 abstract reports low-iron native ATCC 19606 material under the original oxazoline assignment. PMID:15289555 exactly maps to DOI:10.1099/mic.0.27141-0 and describes the ATCC 19606T cluster, selected disruptants and phenotypes mixed with homology-based functions. This is the same publication as the LOTUS DOI, so the two database assertions are not independent experiments. Abstracts establish source and stock context but do not resolve which modern exact isomer each historical measurement established. |
| S040-COMPARISON | /private/tmp/npm-review-work/040/identity/primary-structure-comparison.json; RDKit 2026.03.5 primary-drawing transcription, neutral parents, official MOL and returned PubChem InChI comparison | supports | The owner/MOL recompute FCWIGDCVHNNXFS-UHFFFAOYSA-N with two unspecified centres. Primary neutral precursor candidate is FCWIGDCVHNNXFS-RNCFNFMXSA-N (C4-prime S/C5-prime R); modern product is YQXURFXJBIFMOA-ZANVPECISA-N (S/S), both C16H18N4O5. PubChem5492097 is DYESEQWBWHUEDV-PVBSNRTBSA-N (C4-prime R/C5-prime R plus Z). Tautomer canonicalization can erase C4-prime stereo and reached a transform limit; it was used only as a bounded graph diagnostic, never an equivalence proof. |
| S040-SEARCH | /private/tmp/npm-review-work/040/identity/ignored-inclusive-search.json; Ignored-inclusive exact key-prefix/source-id search of raw sources, generated corpus, curation, code and reviews | supports | The search finds the current owner, raw MIBiG/LOTUS/NPClassifier entries and historical queue artifacts. No additional generated owner or consumed correction for either fully specified primary candidate was found within these searched paths. The PubChem source row says no assay data, consistent with no activity assertions. This is a bounded repository collision/correction search, not a global chemical database absence claim. |
| S040-LIVE-SEARCH | /private/tmp/npm-review-work/040/identity/support-extra-access-network.json; Bounded official ChEBI candidate-key and PubChem name queries; earlier ChEBI exact-owner/name results | supports | Official owner-key and acinetobactin-name ChEBI searches each return only the two-star old partial structure. Candidate full-key ChEBI queries returned HTTP 404 and are not treated as proof of global absence. PubChem acinetobactin-name lookup returns CID139588300 with the old partial key; preacinetobactin-name lookup returned 404. Name lookup does not override primary structural evidence or select a candidate. |
| S040-ACCESS | /private/tmp/npm-review-work/shared-next-batch004/final-access.json; Retained bounded original-source access receipts, read locally now; exact 2004 response received 2026-10-21T09:27:24.561858Z | supports | The positively located 2004 PDF route returned a 9,528-byte HTML archive/challenge response, not a PDF or main body. The 1994 full body and 2016 main body were not obtained in the retained bounded attempts. The accessible 2016 SI and 2009/2018 bodies were read as their own sources; no failed response or search snippet was promoted to full-text evidence. |
| S040-LOADERS | src/naturalproductmech/curate/structure_corrections.py; Complete structure correction loader; consumed xref, strain, claim-reference and LOTUS overlay guards; seed_from_sources.py composition branches | supports | Current structure correction accepts only REPLACE_WITH_CHEBI or SPLIT_SHARED_WITH_CHEBI to a unique structured three-star ChEBI target with source/target row pins, withholds old xrefs and does not transfer old-key joins. It has no manual primary-backed name/structure decision. The seeder rejects xref/strain/isolate overlays after structure_correction_note and claim_references.py likewise rejects reference correction. LOTUS decisions require an exact full-row-pinned triple and must reach an emitted owner. Pin updates alone cannot make these corrections compose. |
| S040-IMODULON | /private/tmp/npm-review-work/010/imodulon-datasets.txt; Previously retrieved iModulonDB dataset catalogue: a_baumannii/precise139 | supports | The catalogue has an A. baumannii precise139 dataset lead. The current record asserts no named gene, protein or regulatory graph to map; the catalogue alone supplies no exact siderophore, locus or stock-specific regulation claim. Its presence is recorded without inventing a missing-regulation finding. |

## Limits And Additional Notes

- The required 2004 main body was unavailable after preserved bounded free-access attempts. Historical exact-isomer production, native disruptant applicability and biosynthetic method grades remain unresolved; the review must be partial despite confirmed identity and xref findings.
- The 2009 main narrative was read completely, but its SI and original 1994 full drawings were not obtained. The 2016 official SI was read in full text/captions with original S24/S32 structure pixels and retained S16/S17/S40/S41 views; raw spectra were not independently reprocessed. The 2016 main body remains unavailable.
- The complete 2018 body, Methods and captions were read, with original Figure1 pixels. Crystal coordinates, complete ligand refinement and spectral integrations were not reprocessed. Recombinant binding is not whole-cell transport proof.
- Primary-drawing candidates are neutral parents of the depicted TFA salts, confirmed by independent visual wedge/CIP comparison. They are structurally useful candidates, not an automatic assignment of the 1994/2004 native material or a declaration that neutral free bases were assayed.
- Current full-source comparison covers MIBiG metadata and chemical authority records; the entire AB101202.1 locus was not independently retranslated. The earlier bounded BauA sequence preparation does not validate all biosynthetic genes, and no protein claim is present in this owner.
- Only the current owner-key/name ChEBI search yielded an inspected two-star result. Fully specified candidate searches returned HTTP404; this does not establish global absence of eligible authorities. The manual correction route is required unless an independently verified eligible target becomes available.
- Default RDKit tautomer canonicalization reached its transform limit for some inputs and removes the tautomerizable C4-prime stereocentre. The original InChI and direct atom mapping, not normalized equality, support the xref finding.
- A. baumannii precise139 is an applicable organism-level iModulon dataset lead; no exact-gene component or target-specific regulatory evidence was inferred from its catalogue presence.
- The configured identifier-label gate accepts 499 warning-level mismatches and 35 explicit exceptions and skips 4,744 no-adapter pairs; exit 0 does not independently verify every identifier or scientific claim.
- The quality suite reports 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). Skipped tests are not counted as passing tests. Existing ontology caches were used; no multi-gigabyte cache download was required.
- Native gates assess deterministic consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy, or literature-level claim support.
- No scientific owner, inventory, curation table, native status or history was edited. Actions are proposed work.
- Shared baseline gates and target strict validation retain their actual fresh command receipts for this base. Scientific failed or unavailable checks are distinct from bundle validation.

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
review_id: 20261021T103933Z-acinetobactin
title: 'Acinetobactin: resolve historical structure assignment and incompatible PubChem
  link'
started_at: '2026-10-21T10:26:33.353397Z'
finished_at: '2026-10-21T10:39:33.268660Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The stored historical oxazoline lacks two specified centres and does not
  identify the rearranged structure assigned to acinetobactin by later primary work.
  The PubChem link resolves to a distinct tautomer and stereochemical entity. The
  required 2004 native experiment remains inaccessible, so primary-backed identity
  migration and source-claim admission must be adjudicated together through maintained,
  guarded inputs.
source:
  git_revision: 1c2402097718c138b081e00943de8f04de0541cd
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
    sha256: 4bc422b93002508b0abb86e0fa0afa49aff88745b5b0dd3bcbf351a68725d766
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: f87a4fa580dede966366bece28ccfb6542bdec4a0f810e40cdfc719811407a05
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: b27c2e61e696a285c38bc88c852dbbdc6c06fec8c4584343f2b9146462eea6cf
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
  - path: data/natural_products/alkaloids/acinetobactin.yaml
    sha256: 35a460b693ed1b43f7b597edea8a984b1eaab0b3eb176f2cc3d953bbd2d8b8f2
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
    sha256: 6873daace2f9e2225ef3d6830e993ac8cf8d01cec66b779fa5829309d77b3eaf
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
    sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/lotus_exclusions.py
    sha256: 6352cac7c587eab5a56d907c523cc899d02d197009081624bf8649c675ee30f7
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
    role: context
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 40, batch 004, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated pending-PR targets.
    At selection, 84 of 3116 current records had campaign coverage and 3032 remained.
    The population search included ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-75969a8e53
targets:
- target_id: naturalproductmech:mibig-75969a8e53
  path: data/natural_products/alkaloids/acinetobactin.yaml
  label: acinetobactin
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
checks:
- check_id: C-STRICT
  name: Closed-schema target validation
  status: passed
  required: true
  summary: The documented target strict validator completed; scientific support is
    assessed separately.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  command: just validate-strict data/natural_products/alkaloids/acinetobactin.yaml
    --out /private/tmp/npm-review-work/040/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T10:26:36.086739Z
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 current record files agree with PATHS.tsv and their pinned filing
    pathways.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh read-only execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055340+00:00;
    finished 2026-10-21T09:55:22.727768+00:00. Exact receipt: /private/tmp/npm-native-checks/batch-004/verify-corpus.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-corpus.log. No earlier
    baseline result is reused.'
  target_ids:
  - naturalproductmech:mibig-75969a8e53
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3,116 current records passed the documented byte-reproduction gate
    against committed inventories and maintained curation inputs.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh read-only execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055361+00:00;
    finished 2026-10-21T09:56:44.050706+00:00. Exact receipt: /private/tmp/npm-native-checks/batch-004/verify-reproduction.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-reproduction.log.
    No earlier baseline result is reused.'
  target_ids:
  - naturalproductmech:mibig-75969a8e53
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The exhaustive review queue produced 8,928 diagnostic rows across 12 queues;
    this deterministic output does not establish scientific review.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just review-queue --tsv /private/tmp/npm-review-queue-batch-004.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh read-only execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.057401+00:00;
    finished 2026-10-21T09:54:38.468783+00:00. Exact receipt: /private/tmp/npm-native-checks/batch-004/review-queue.json;
    transcript: /private/tmp/npm-native-checks/batch-004/review-queue.log. No earlier
    baseline result is reused.'
  target_ids:
  - naturalproductmech:mibig-75969a8e53
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'The configured identifier-label gate passed using the existing ontology
    caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions,
    499 warning-only mismatches and 4,744 pairs skipped because their prefixes have
    no adapter.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh read-only execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.061733+00:00;
    finished 2026-10-21T09:56:36.296159+00:00. Exact receipt: /private/tmp/npm-native-checks/batch-004/validate-products.json;
    transcript: /private/tmp/npm-native-checks/batch-004/validate-products.log. No
    earlier baseline result is reused.'
  target_ids:
  - naturalproductmech:mibig-75969a8e53
- check_id: shared-qc
  name: Full repository quality gate on the current main baseline
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed against the new main revision.
    Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured
    lint, governance, documentation, provenance, source-queue, schema, rendering,
    reproduction, filing-integrity and reporting stages completed successfully.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh read-only execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:30.560925+00:00;
    finished 2026-10-21T10:04:44.806799+00:00. Exact receipt: /private/tmp/npm-native-checks/batch-004/qc.json;
    transcript: /private/tmp/npm-native-checks/batch-004/qc.log. No earlier baseline
    result is reused.'
  target_ids:
  - naturalproductmech:mibig-75969a8e53
- check_id: S040-C-IDENTITY
  name: Primary structure, name and stereochemical identity
  status: failed
  required: true
  summary: The historical name and partial oxazoline graph do not resolve to one exact
    modern product. The primary revision and two explicitly different drawings require
    a guarded identity/source-admission decision.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  evidence_ids:
  - S040-OWNER
  - S040-REVISION
  - S040-SI-STRUCTURE
  - S040-BAUA
  - S040-COMPARISON
- check_id: S040-C-XREF
  name: Exact chemical cross-reference equivalence
  status: failed
  required: true
  summary: NPAtlas matches the current partial graph, but PubChem5492097 asserts a
    different tautomer/stereochemical entity and cannot be retained as an exact xref.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  evidence_ids:
  - S040-NPATLAS
  - S040-PUBCHEM
  - S040-COMPARISON
- check_id: S040-C-HISTORICAL
  name: Exact historical native product and cluster experiment verification
  status: unavailable
  required: true
  summary: The required 2004 original main body was unavailable. Its abstract cannot
    assign each native production/disruptant phenotype to the fully specified precursor
    or rearranged product, so native method upgrades and automatic claim transfer
    remain unresolved.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  evidence_ids:
  - S040-HISTORICAL
  - S040-ACCESS
  - S040-REVISION
evidence:
- evidence_id: S040-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/acinetobactin.yaml
  locator: Complete generated owner and resolved content, including all source, occurrence,
    producer, locus, classification, identifier and history fields
  accessed_at: '2026-10-21T10:38:15.482479Z'
  support: supports
  summary: The owner calls a two-centre-unspecified oxazoline acinetobactin, full
    key FCWIGDCVHNNXFS-UHFFFAOYSA-N. It has one LOTUS species occurrence and one MIBiG
    source-asserted producer/locus; no activity, named protein, biosynthetic step
    or graph is asserted. stereo_complete:false accurately describes the stored graph.
  snapshot_sha256: 35a460b693ed1b43f7b597edea8a984b1eaab0b3eb176f2cc3d953bbd2d8b8f2
- evidence_id: S040-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: Complete BGC0000294:1 version 5 row; matched LOTUS, NPClassifier and PubChem
    no-assay rows compared separately
  accessed_at: '2026-10-21T10:38:15.482479Z'
  support: supports
  summary: The raw MIBiG row exactly reproduces the old oxazoline graph, source label,
    NPA018669/PubChem5492097 identifiers, taxon 470, AB101202.1:3950..30424 and PMID:15289555
    with empty locus methods. Full canonical MIBiG row SHA256 bf1c35da9f7064b24c9ecdf90aa8cceacb3bf2d25a030584d18fc7839d84324f.
    The single LOTUS row uses the same old key and DOI:10.1099/MIC.0.27141-0; full
    LOTUS row SHA256 d7747f3cf812e61457e7535e22ea5d7ee724dd45b8d32a53a7f983e917f24d2e.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: S040-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000294.5/annotations.json
  locator: 'BGC0000294 version 5: complete compounds[0], taxonomy, locus and legacy
    reference'
  accessed_at: '2026-10-21T10:26:53.974266Z'
  support: supports
  summary: Current MIBiG retains the source graph and label, two original xrefs, A.
    baumannii taxon 470, NRPS Type I, active/questionable/unknown status and AB101202.1:3950..30424
    with no locus evidence methods. PMID:15289555 is entry-level. Source fidelity
    does not resolve the later primary structure revision.
  snapshot_sha256: 623b13f46e7d659839600075cda5b4124720be7b9940bcc6b9f9a99540297d1b
- evidence_id: S040-NPATLAS
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA018669
  locator: NPA018669 complete current chemical data, original source and organism
  accessed_at: '2026-10-21T10:26:54.007057Z'
  support: supports
  summary: NPAtlas NPA018669 exactly matches the current owner full InChIKey and its
    unspecified stereochemistry. Its Acinetobactin name and A. baumannii origin trace
    to the original 1994 DOI:10.1007/bf00301846; the current entry does not implement
    the later structural reassignment. It is a faithful xref to the current partial
    graph, not independent proof that the modern named product is that graph.
  snapshot_sha256: e39670e8ca3cc664a116d73d112e54912445f2c41e8fd7e2d0d7ba551bea5de6
- evidence_id: S040-PUBCHEM
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5492097/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES,IsomericSMILES/JSON
  locator: CID 5492097 complete returned InChI, key, formula and SMILES
  accessed_at: '2026-10-21T10:26:54.210525Z'
  support: supports
  summary: 'The stored xref now resolves to DYESEQWBWHUEDV-PVBSNRTBSA-N, C16H18N4O5:
    a keto/enamine representation with an exocyclic Z alkene and two assigned centres.
    Its heavy-atom connectivity layer matches the oxazoline graph, not the rearranged
    modern isoxazolidinone. The stereochemical mapping is C4-prime R/C5-prime R, differing
    from primary preacinetobactin C4-prime S/C5-prime R as well as from the owner’s
    unspecified graph.'
  snapshot_sha256: 9cfda5bcf6b2b062f8472930b0fddd89693b1225300b3a64c8e4ea21ff4a6d24
- evidence_id: S040-CHEBI
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/211033/
  locator: CHEBI:211033 rating, default Standard InChI and compound origin; corroborating
    official MOL
  accessed_at: '2026-10-21T10:27:44.207458Z'
  support: supports
  summary: The current released entry is two-star, named Acinetobactin, and carries
    the exact old partial key FCWIGDCVHNNXFS-UHFFFAOYSA-N. Its origin again cites
    the historical 1994 paper. The official MOL independently recomputes this key
    with two unspecified centres. It is ineligible for the repository’s three-star
    grounding/structure-replacement route.
  snapshot_sha256: e7ecfa76d5fc3ed13196fb1a918bed79a152ad6ce6c83ae8b099df46453ce270
- evidence_id: S040-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/211033/
  locator: Complete official CHEBI:211033 MOL parsed without modifying its chemistry
  accessed_at: '2026-10-21T10:27:44.854184Z'
  support: supports
  summary: The official MOL is chemically parseable and has the owner’s exact Standard
    InChIKey with two unspecified stereocentres. This avoids relying on an unbracketed
    imidazole SMILES representation or silently changing it.
  snapshot_sha256: 0934642e47592a4d663cfac93b0d78acafe2b979a0ea3c60ecb6e262dcfa1197
- evidence_id: S040-TAXON
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=470&retmode=xml
  locator: Complete taxon 470 scientific name, rank, lineage and type material
  accessed_at: '2026-10-21T10:26:54.612033Z'
  support: supports
  summary: NCBITaxon:470 is the bacterial species Acinetobacter baumannii; ATCC 19606
    is listed as type material. The current broad species label and OTHER_BACTERIAL
    grouping are consistent. The exact 2004 study stock is ATCC 19606T, not ATCC 17978
    used for the later natural-versus-synthetic comparison.
  snapshot_sha256: 25c9f786e05dfc037876360a2f492736d6599c87e73678d395637f04272b62f0
- evidence_id: S040-WIKIDATA
  kind: authority
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q3241189&props=labels%7Cclaims&languages=en&format=json
  locator: Q3241189 English label and P685 taxon value
  accessed_at: '2026-10-21T10:34:59.496815Z'
  support: supports
  summary: The exact organism identifier retained in the LOTUS note resolves to Acinetobacter
    baumannii and NCBI taxonomy 470.
  snapshot_sha256: 3f9a3647ed7a7243a6b0e56e96f4f754a892047b041e1be496ae756318781b21
- evidence_id: S040-REVISION
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2676571/
  locator: DOI:10.1021/ja900815w; PMID:19320483; complete main narrative and Figure
    2 caption, especially the final reassignment paragraphs
  accessed_at: '2026-10-21T09:27:22.802702Z'
  support: supports
  summary: The primary authors reassign acinetobactin to isoxazolidinone compound
    5 because its proton NMR agrees with the original isolation data; they rename
    oxazoline 1 pre-acinetobactin. The experimental assembly uses purified Pseudomonas
    entomophila PmsD/PmsE/PmsG with substituted 2,3-dihydroxybenzoate, threonine and
    synthetic N-hydroxyhistamine; a spontaneous nonenzymatic rearrangement follows.
    These experiments do not directly characterize native A. baumannii Bas proteins
    or prove natural Pseudomonas secretion.
  snapshot_sha256: 0a6d2420c454ec9f168bc54a4321a044268f784aacc63ba791d6a746f91a24f1
- evidence_id: S040-SI-STRUCTURE
  kind: primary_source
  reference: https://s3-eu-west-1.amazonaws.com/pstorage-acs-6854636/3636072/id5b00145_si_001.pdf
  locator: DOI:10.1021/acsinfecdis.5b00145; original Tables S2/S3 and drawings on
    S24/S32; synthesis S4-S8; all SI text and captions read
  accessed_at: '2026-10-21T09:26:43.726510Z'
  support: supports
  summary: The primary numbered drawings distinguish pre-acinetobactin 1a, C4-prime
    S/C5-prime R, from rearranged acinetobactin 1b, C4-prime S/C5-prime S. Both NMR
    tables concern TFA salts. Neutral-parent graph candidates were transcribed by
    omitting the counterion; they are not claims that the assayed material was a free
    base. The synthesis starts with L-threonine benzyl ester. Detailed spectra were
    not independently reinterpreted.
  snapshot_sha256: 8eb8875ad7d23b4d7a806c6b09decf5c04624d7f634b1dd2d6d35cd270d79501
- evidence_id: S040-SI-SCOPE
  kind: primary_source
  reference: https://s3-eu-west-1.amazonaws.com/pstorage-acs-6854636/3636072/id5b00145_si_001.pdf
  locator: 'S11-S23 and S40-S41: Table S1, Figures S13-S16 and S35-S36; proposed Scheme
    S1 S2-S3'
  accessed_at: '2026-10-21T09:26:43.726510Z'
  support: supports
  summary: The SI reports pH-dependent nonenzymatic conversion, natural ATCC 17978
    acinetobactin versus synthetic material by CD and MS/MS, and supplied ferric-ligand
    growth responses in ATCC 17978 and ATCC 19606 with specified mutant labels. MS/MS
    fragments alone do not distinguish the isomers. The Bas/Bau/Bar scheme is explicitly
    proposed, and these data do not individually demonstrate every biosynthetic or
    transport reaction. No native ATCC 19606 exact-isomer production assignment is
    inferred from ATCC 17978 CD or from supplied-ligand growth.
  snapshot_sha256: 8eb8875ad7d23b4d7a806c6b09decf5c04624d7f634b1dd2d6d35cd270d79501
- evidence_id: S040-BAUA
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6300358/fullTextXML
  locator: DOI:10.7554/eLife.42270; PMID:30558715; complete Results, Discussion and
    Methods, Tables 1-2 and original Figure 1A pixels
  accessed_at: '2026-10-21T09:26:26.362689Z'
  support: supports
  summary: Figure 1 independently confirms the two structures and stereochemical drawings.
    Recombinant mature BauA from ATCC 19606, expressed in E. coli and purified, binds
    ferric preacinetobactin by ITC; the purified acinetobactin-only samples do not
    show detected binding. The mixed ferric preacinetobactin/acinetobactin complex
    and impurity control support a ligand-recognition distinction. Whole-cell transport
    and every proposed downstream step were not directly measured in this structural
    study; the reported minor crystal diastereomer is not an established natural configuration.
  snapshot_sha256: 6f4cec4b7e5a9e31e57136c73482bc1fb56aaab05cc634c2d61e8ace9ae5807b
- evidence_id: S040-HISTORICAL
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:7802543%20OR%20EXT_ID:27624967%20OR%20EXT_ID:15289555&format=json&resultType=core
  locator: Complete original abstracts and PMID/DOI metadata for PMID:7802543, PMID:15289555
    and PMID:27624967
  accessed_at: '2026-10-21T09:29:34.306318Z'
  support: supports
  summary: The 1994 abstract reports low-iron native ATCC 19606 material under the
    original oxazoline assignment. PMID:15289555 exactly maps to DOI:10.1099/mic.0.27141-0
    and describes the ATCC 19606T cluster, selected disruptants and phenotypes mixed
    with homology-based functions. This is the same publication as the LOTUS DOI,
    so the two database assertions are not independent experiments. Abstracts establish
    source and stock context but do not resolve which modern exact isomer each historical
    measurement established.
  snapshot_sha256: 98ecb49eb67b101d07dbea36f79f56ce4208a42367dc6031e92719343f371110
- evidence_id: S040-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/040/identity/primary-structure-comparison.json
  locator: RDKit 2026.03.5 primary-drawing transcription, neutral parents, official
    MOL and returned PubChem InChI comparison
  accessed_at: '2026-10-21T10:34:42.965888Z'
  support: supports
  summary: The owner/MOL recompute FCWIGDCVHNNXFS-UHFFFAOYSA-N with two unspecified
    centres. Primary neutral precursor candidate is FCWIGDCVHNNXFS-RNCFNFMXSA-N (C4-prime
    S/C5-prime R); modern product is YQXURFXJBIFMOA-ZANVPECISA-N (S/S), both C16H18N4O5.
    PubChem5492097 is DYESEQWBWHUEDV-PVBSNRTBSA-N (C4-prime R/C5-prime R plus Z).
    Tautomer canonicalization can erase C4-prime stereo and reached a transform limit;
    it was used only as a bounded graph diagnostic, never an equivalence proof.
  snapshot_sha256: e1d92b67006335683e8c07c03e319cfddcec7fcc7bfe58c49cc639e777b96960
- evidence_id: S040-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/040/identity/ignored-inclusive-search.json
  locator: Ignored-inclusive exact key-prefix/source-id search of raw sources, generated
    corpus, curation, code and reviews
  accessed_at: '2026-10-21T10:35:21.573617Z'
  support: supports
  summary: The search finds the current owner, raw MIBiG/LOTUS/NPClassifier entries
    and historical queue artifacts. No additional generated owner or consumed correction
    for either fully specified primary candidate was found within these searched paths.
    The PubChem source row says no assay data, consistent with no activity assertions.
    This is a bounded repository collision/correction search, not a global chemical
    database absence claim.
  snapshot_sha256: b1c922bfa506dfea3ca2cd94427a2844e031f327fbb513abebf04d8c70c0531f
  search_scope: rg --no-ignore --hidden -n -i for FCWIGDCVHNNXFS, YQXURFXJBIFMOA,
    DYESEQWBWHUEDV, BGC0000294 and mibig-75969a8e53 across data/raw, data/natural_products,
    curation, src, scripts and reviews; all 35 matching lines retained; ignored files
    included.
- evidence_id: S040-LIVE-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/040/identity/support-extra-access-network.json
  locator: Bounded official ChEBI candidate-key and PubChem name queries; earlier
    ChEBI exact-owner/name results
  accessed_at: '2026-10-21T10:35:01.318429Z'
  support: supports
  summary: Official owner-key and acinetobactin-name ChEBI searches each return only
    the two-star old partial structure. Candidate full-key ChEBI queries returned
    HTTP 404 and are not treated as proof of global absence. PubChem acinetobactin-name
    lookup returns CID139588300 with the old partial key; preacinetobactin-name lookup
    returned 404. Name lookup does not override primary structural evidence or select
    a candidate.
  snapshot_sha256: 31992ca11d4aa6b3fc0b737e3495e9c355091aeaa9812303a8569e62bc16968a
  search_scope: Official ChEBI es_search size=100 for exact owner key and acinetobactin
    name at 10:26Z, then the two fully specified primary keys at 10:35Z; PubChem PUG
    REST exact acinetobactin/preacinetobactin names at 10:27Z. No global absence inference.
- evidence_id: S040-ACCESS
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch004/final-access.json
  locator: Retained bounded original-source access receipts, read locally now; exact
    2004 response received 2026-10-21T09:27:24.561858Z
  accessed_at: '2026-10-21T10:38:37.671830Z'
  support: supports
  summary: The positively located 2004 PDF route returned a 9,528-byte HTML archive/challenge
    response, not a PDF or main body. The 1994 full body and 2016 main body were not
    obtained in the retained bounded attempts. The accessible 2016 SI and 2009/2018
    bodies were read as their own sources; no failed response or search snippet was
    promoted to full-text evidence.
  snapshot_sha256: a7fe654fc3d5bd649ebe5168e91dc159e7839a8991f3d782fc25ce95b3e0e1b4
  search_scope: Retained initial-access.json, more-access.json and final-access.json
    attempts in shared-next-batch004, exact original DOI/PMID routes and positively
    located free copies only; the 2004 route yielded HTML, ACS 2016 full body returned
    403 and its located mirror was unreachable. No new repetition of failed historical
    routes.
- evidence_id: S040-LOADERS
  kind: record_content
  reference: src/naturalproductmech/curate/structure_corrections.py
  locator: Complete structure correction loader; consumed xref, strain, claim-reference
    and LOTUS overlay guards; seed_from_sources.py composition branches
  accessed_at: '2026-10-21T10:38:15.482479Z'
  support: supports
  summary: Current structure correction accepts only REPLACE_WITH_CHEBI or SPLIT_SHARED_WITH_CHEBI
    to a unique structured three-star ChEBI target with source/target row pins, withholds
    old xrefs and does not transfer old-key joins. It has no manual primary-backed
    name/structure decision. The seeder rejects xref/strain/isolate overlays after
    structure_correction_note and claim_references.py likewise rejects reference correction.
    LOTUS decisions require an exact full-row-pinned triple and must reach an emitted
    owner. Pin updates alone cannot make these corrections compose.
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
- evidence_id: S040-IMODULON
  kind: search
  reference: /private/tmp/npm-review-work/010/imodulon-datasets.txt
  locator: 'Previously retrieved iModulonDB dataset catalogue: a_baumannii/precise139'
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: supports
  summary: The catalogue has an A. baumannii precise139 dataset lead. The current
    record asserts no named gene, protein or regulatory graph to map; the catalogue
    alone supplies no exact siderophore, locus or stock-specific regulation claim.
    Its presence is recorded without inventing a missing-regulation finding.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  search_scope: Read retained complete datasets output and original successful command
    receipt; bounded species-level applicability only, no component/gene or phenotype
    inference.
assessments:
- assessment_id: S040-A-IDENTITY
  area: identity
  topic: Revised name, constitutional isomer and stereochemistry
  outcome: concern
  summary: The source graph is internally consistent and truthfully incomplete, but
    a single natural-product identity is not resolved. Neutral primary-drawing candidates
    are precursor FCWIGDCVHNNXFS-RNCFNFMXSA-N and modern acinetobactin YQXURFXJBIFMOA-ZANVPECISA-N.
    Select neither merely by name or database consensus; adjudicate source claims
    and a maintained migration.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  evidence_ids:
  - S040-OWNER
  - S040-REVISION
  - S040-SI-STRUCTURE
  - S040-BAUA
  - S040-COMPARISON
- assessment_id: S040-A-XREF
  area: identity
  topic: Authority equivalence and current grounding
  outcome: concern
  summary: NPA018669 and two-star CHEBI:211033 reproduce the historical partial graph;
    neither resolves the modern nomenclature. MINTED is appropriate for that graph
    under the three-star rule. PubChem5492097 fails exact equivalence. No eligible
    current replacement has been established; candidate-key API failures are not absence
    proof.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  evidence_ids:
  - S040-NPATLAS
  - S040-PUBCHEM
  - S040-CHEBI
  - S040-MOL
  - S040-COMPARISON
  - S040-LIVE-SEARCH
- assessment_id: S040-A-OCCURRENCE
  area: evidence
  topic: Native origin, occurrence and citation independence
  outcome: unknown
  summary: Native A. baumannii siderophore production is documented at historical-name
    level, with ATCC19606 in the 1994/2004 abstracts and ATCC17978 natural modern
    material in the 2016 SI. The one LOTUS occurrence and MIBiG producer cite the
    same 2004 publication. Exact modern-isomer applicability of that historical row
    remains unverified; no automatic old-key claim transfer or whole-species negative
    inference is justified.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  evidence_ids:
  - S040-RAW
  - S040-HISTORICAL
  - S040-SI-SCOPE
  - S040-REVISION
  - S040-TAXON
- assessment_id: S040-A-BGC
  area: evidence
  topic: Native locus and method applicability
  outcome: unknown
  summary: The generated AB101202.1 interval, species, PMID and empty-method SOURCE_ASSERTION/CLUSTER_UNSTATED
    grades faithfully match current MIBiG. The 2004 abstract reports selected disruptants
    but does not provide the target-resolved experiment details needed here. Later
    Pseudomonas enzyme reconstitution and recombinant BauA binding cannot upgrade
    this native biosynthetic claim.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  evidence_ids:
  - S040-MIBIG
  - S040-HISTORICAL
  - S040-REVISION
  - S040-BAUA
  - S040-ACCESS
- assessment_id: S040-A-TAXON
  area: provenance
  topic: Taxonomy, source provenance and generated audit history
  outcome: supported
  summary: NCBITaxon:470 and Wikidata Q3241189 agree on A. baumannii. The source uses
    the species rank; ATCC19606 is the historical study stock and current taxon type
    material. The owner preserves source version and the same-publication warning.
    SEEDED status/history correctly record generation; this review does not alter
    them.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  evidence_ids:
  - S040-OWNER
  - S040-RAW
  - S040-MIBIG
  - S040-TAXON
  - S040-WIKIDATA
  - S040-HISTORICAL
- assessment_id: S040-A-CLASSIFICATION
  area: provenance
  topic: Computed chemical classification and source BGC class
  outcome: supported
  summary: ALKALOIDS and the NPClassifier Histidine alkaloids/Imidazole alkaloids/non-glycoside
    output match the exact committed old-key prediction; NRPS is separately the MIBiG
    locus class. These are different classifications. Any future full-key correction
    must re-evaluate the generated prediction rather than carry the old-key result
    without provenance.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  evidence_ids:
  - S040-OWNER
  - S040-RAW
  - S040-MIBIG
  - S040-SEARCH
- assessment_id: S040-A-COMPLETENESS
  area: completeness
  topic: Optional mechanisms, proteins, bioactivity and regulation
  outcome: not_applicable
  summary: No protein, molecular target, pathway step, graph or activity claim is
    present, and the source PubChem inventory has no assay data. Rich later ligand-binding
    and proposed pathway literature does not create an omission finding. A. baumannii
    precise139 is an available iModulon lead, but no owner gene assertion supplies
    a justified target-specific regulatory mapping.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  evidence_ids:
  - S040-OWNER
  - S040-SEARCH
  - S040-BAUA
  - S040-SI-SCOPE
  - S040-IMODULON
findings:
- finding_id: S040-F-IDENTITY
  issue_key: mibig-bgc0000294-compound1-historical-identity-resolution
  category: identity
  severity: blocker
  native_severity: blocker
  normalization_reason: The checklist treats a chemically unresolved or wrong exact
    identity as a blocker; the modern name denotes a rearranged constitutional isomer
    and the stored precursor graph also lacks two published stereocentres.
  status: open
  certainty: confirmed
  title: The historical name and partial graph do not define the modern exact product
  description: The owner retains the historical acinetobactin name for an unspecified
    oxazoline. Primary reassignment and explicit later drawings distinguish stereodefined
    preacinetobactin from rearranged modern acinetobactin. The false equivalence is
    confirmed; the correct migration destination for the historical source assertions
    still needs claim-specific adjudication. This is more than an optional synonym
    or missing stereo_complete flag.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  field_paths:
  - label
  - chemical_structure
  - source_concepts
  - producer_organisms
  - biosynthetic_gene_clusters
  - occurrences
  - grounding_status
  evidence_ids:
  - S040-OWNER
  - S040-RAW
  - S040-REVISION
  - S040-SI-STRUCTURE
  - S040-BAUA
  - S040-COMPARISON
  - S040-LOADERS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Future consumed primary-backed identity decision after the loader is extended
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Guarded manual exact-structure and label capability required for a non-three-star
      target
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Claim admission, overlay composition and deterministic owner migration
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Exact-target reference admission and structure-correction composition
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Adjudicated ATCC19606 stock qualification, if the retained native claim
      supports it
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/lotus_exclusions.py
    role: Preservation and adjudication of the old-key occurrence triple
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Explicit generated owner and identifier migration bookkeeping
- finding_id: S040-F-XREF
  issue_key: mibig-bgc0000294-compound1-pubchem5492097-not-exact
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: PubChem5492097 does not identify the stored exact structure
  description: The current linked CID assigns a keto/enamine tautomer, Z geometry
    and two R centres, while the stored graph has two unspecified centres. Primary
    preacinetobactin instead assigns C4-prime S/C5-prime R. The modern rearranged
    acinetobactin is a different heavy-atom graph. Shared formula, historical label
    or tautomer canonicalization that drops stereo cannot establish exact equivalence.
    This xref can be withheld independently before the larger identity decision.
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  field_paths:
  - xrefs
  evidence_ids:
  - S040-PUBCHEM
  - S040-COMPARISON
  - S040-SI-STRUCTURE
  - S040-LOADERS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Consumed literal PubChem5492097 exclusion
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Full raw-row guard and exclusion provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: No reintroduction and explicit composition with future identity correction
actions:
- action_id: S040-A-RESOLVE-IDENTITY
  description: Adjudicate BGC0000294:1 version 5 against the 2009 revision, 2016 SI
    Tables S2/S3 and 2018 Figure1, pinning complete raw-row SHA256 bf1c35da9f7064b24c9ecdf90aa8cceacb3bf2d25a030584d18fc7839d84324f.
    Implement a consumed manual primary-backed name/structure and claim-admission
    extension in the structure-correction loader/seeder before entering its decision
    in curation/mibig_structure_corrections.tsv; the existing two ChEBI-only actions
    cannot admit two-star CHEBI:211033 or an arbitrary primary structure. The neutral
    primary candidates are preacinetobactin FCWIGDCVHNNXFS-RNCFNFMXSA-N and modern
    acinetobactin YQXURFXJBIFMOA-ZANVPECISA-N. Do not choose one merely from a name
    lookup. Retrieve the required 2004 exact experimental context or explicitly withhold/qualify
    unresolved native and occurrence claims using a tested consumed admission mechanism.
    Retain raw source labels and full rows as provenance. Bind any admitted ATCC19606
    producer, locus reference and old-key LOTUS triple (SHA256 d7747f3cf812e61457e7535e22ea5d7ee724dd45b8d32a53a7f983e917f24d2e)
    to the adjudicated chemical entity; do not transfer them silently. If a unique
    eligible three-star target later becomes available, verify its complete structure
    before using that existing route. Reserved decisions.tsv is not a consumer.
  finding_ids:
  - S040-F-IDENTITY
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Future consumed primary-backed identity decision after the loader is extended
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Guarded manual exact-structure and label capability required for a non-three-star
      target
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Claim admission, overlay composition and deterministic owner migration
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Exact-target reference admission and structure-correction composition
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Adjudicated ATCC19606 stock qualification, if the retained native claim
      supports it
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/lotus_exclusions.py
    role: Preservation and adjudication of the old-key occurrence triple
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Explicit generated owner and identifier migration bookkeeping
  generator: scripts/seed_from_sources.py after an explicitly implemented and tested
    guarded manual identity/admission extension
  acceptance_checks:
  - Source chemistry, name, taxon, citation, interval, methods and xrefs are covered
    by the full raw-row pin; any drift fails closed. Primary transcriptions recompute
    the intended key, formula, stereocentres and neutral-parent form, with TFA salt
    provenance retained.
  - The emitted owner has one unambiguous primary-supported label/full structure and
    an explicit identity/path migration; it neither merges precursor and rearranged
    product nor treats the old incomplete key as an exact synonym. Collision searches
    include ignored files.
  - Each retained producer, locus and occurrence assertion is independently admitted
    for that exact candidate. Historical PMID/DOI equivalence is preserved; insufficient
    exact-isomer evidence is withheld or explicitly scoped rather than upgraded from
    an abstract. ATCC19606 and ATCC17978 contexts remain distinct.
  - A combined canary tests structural correction with xref exclusions, claim-reference
    routing, strain/isolate qualification and old-key LOTUS provenance. Current structure_correction_note
    guards must be deliberately extended with target-specific pins; merely refreshing
    existing pins or suppressing errors is insufficient.
  - The old-key LOTUS and PubChem no-assay rows remain traceable and are not automatically
    copied to a new key. Stale chemical xrefs are withheld; any admitted replacement
    is independently exact. NPClassifier output is regenerated or explicitly left
    unresolved for a changed key.
  - Strict validation, source reproducibility, reviewable PATHS/identifier migration
    and repository quality gates pass after implementation; no optional activity,
    protein or regulatory assertion is manufactured.
- action_id: S040-A-EXCLUDE-XREF
  description: Add the literal pubchem:5492097 exclusion for BGC0000294:1 to curation/mibig_xref_exclusions.tsv,
    with full raw-row SHA256 bf1c35da9f7064b24c9ecdf90aa8cceacb3bf2d25a030584d18fc7839d84324f,
    stable primary/authority reference, curator/date and rationale distinguishing
    tautomer representation from the independent stereochemical mismatch. Keep raw
    database_ids unchanged and retain exclusion provenance. This existing loader supports
    withholding the current xref now. If combined with the identity correction, implement
    explicit composition or retire/supersede the exclusion with equivalent pinned
    provenance after all old xrefs are withheld; the current seeder rejects the simultaneous
    structure-correction/exclusion combination.
  finding_ids:
  - S040-F-XREF
  target_ids:
  - naturalproductmech:mibig-75969a8e53
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Consumed literal PubChem5492097 exclusion
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Full raw-row guard and exclusion provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: No reintroduction and explicit composition with future identity correction
  generator: scripts/seed_from_sources.py using the existing literal MIBiG xref-exclusion
    loader, with composition implemented before simultaneous structure correction
  acceptance_checks:
  - The exact current raw row and literal pubchem:5492097 assertion match the pinned
    SHA; drift or a missing source xref fails closed.
  - An isolated generation removes only this incompatible generated xref at the current
    identity, preserves the raw assertion and emits the exclusion rationale; NPA018669
    is not falsely rejected for its faithful match to the current partial graph.
  - No source row, alias normalization or later generator pass reintroduces the excluded
    CID. Equal formula or stereo-erasing tautomer normalization does not pass exact
    equivalence.
  - The combined identity/xref case is explicitly tested and either composes under
    new target-specific guards or has a documented provenance-preserving supersession;
    the unsupported current combination is not assumed to work.
  - Strict validation and seed reproducibility pass after the maintained correction.
limitations:
- The required 2004 main body was unavailable after preserved bounded free-access
  attempts. Historical exact-isomer production, native disruptant applicability and
  biosynthetic method grades remain unresolved; the review must be partial despite
  confirmed identity and xref findings.
- The 2009 main narrative was read completely, but its SI and original 1994 full drawings
  were not obtained. The 2016 official SI was read in full text/captions with original
  S24/S32 structure pixels and retained S16/S17/S40/S41 views; raw spectra were not
  independently reprocessed. The 2016 main body remains unavailable.
- The complete 2018 body, Methods and captions were read, with original Figure1 pixels.
  Crystal coordinates, complete ligand refinement and spectral integrations were not
  reprocessed. Recombinant binding is not whole-cell transport proof.
- Primary-drawing candidates are neutral parents of the depicted TFA salts, confirmed
  by independent visual wedge/CIP comparison. They are structurally useful candidates,
  not an automatic assignment of the 1994/2004 native material or a declaration that
  neutral free bases were assayed.
- Current full-source comparison covers MIBiG metadata and chemical authority records;
  the entire AB101202.1 locus was not independently retranslated. The earlier bounded
  BauA sequence preparation does not validate all biosynthetic genes, and no protein
  claim is present in this owner.
- Only the current owner-key/name ChEBI search yielded an inspected two-star result.
  Fully specified candidate searches returned HTTP404; this does not establish global
  absence of eligible authorities. The manual correction route is required unless
  an independently verified eligible target becomes available.
- Default RDKit tautomer canonicalization reached its transform limit for some inputs
  and removes the tautomerizable C4-prime stereocentre. The original InChI and direct
  atom mapping, not normalized equality, support the xref finding.
- A. baumannii precise139 is an applicable organism-level iModulon dataset lead; no
  exact-gene component or target-specific regulatory evidence was inferred from its
  catalogue presence.
- The configured identifier-label gate accepts 499 warning-level mismatches and 35
  explicit exceptions and skips 4,744 no-adapter pairs; exit 0 does not independently
  verify every identifier or scientific claim.
- The quality suite reports 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21).
  Skipped tests are not counted as passing tests. Existing ontology caches were used;
  no multi-gigabyte cache download was required.
- Native gates assess deterministic consistency and configured invariants. They do
  not establish biological production, stereochemical specificity, evidence adequacy,
  or literature-level claim support.
notes:
- No scientific owner, inventory, curation table, native status or history was edited.
  Actions are proposed work.
- Shared baseline gates and target strict validation retain their actual fresh command
  receipts for this base. Scientific failed or unavailable checks are distinct from
  bundle validation.
tags:
- path-order-campaign
- batch-004
```
