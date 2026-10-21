# 13-epi-dorrigocin A: exact identity and nonenzymatic origin qualification

- Review: 20261021T071115Z-13-epi-dorrigocin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T07:03:18.854149Z
- Finished UTC: 2026-10-21T07:11:15.379289Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact structure, five absolute configurations, three alkene geometries, both xrefs, minted grounding and culture occurrence are supported. Primary studies establish formation by water-mediated rearrangement of biosynthesized iso-migrastatin. The record needs one coordinated origin/producer/locus qualification that preserves this indirect biological connection without implying a directly assayed biosynthetic endpoint.

## Scope And Provenance

One complete generated owner and resolved mechanism, with every asserted field group assessed against local provenance and accessible primary evidence.

Selection: Seventh unreviewed path in deterministic order from the initial validated list: 91 bundles covered 54 of 3,116 records and 3,062 remained. Ignored bundles were included in coverage counting. This bundle assesses one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-2bd59ca78c | data/natural_products/alkaloids/13-epi-dorrigocin-a.yaml | generated | 13-epi-dorrigocin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and component validation | passed | True | naturalproductmech:mibig-2bd59ca78c | One complete owner validated with zero ERROR rows. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-2bd59ca78c | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-2bd59ca78c | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-2bd59ca78c | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-2bd59ca78c | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Initial QC attempt before installing the pinned linter | failed | False | naturalproductmech:mibig-2bd59ca78c | The first full QC invocation stopped at lint because the isolated copied Python environment lacked Ruff. Exact uv.lock version Ruff 0.16.6 was subsequently installed and lint passed on later invocations. |
| QC attempt without network access | failed | False | naturalproductmech:mibig-2bd59ca78c | After Ruff installation, QC passed lint and stopped at vendored-sync because sandbox DNS could not reach the pinned public CLAW governance source. Approved network access allowed the next invocation to verify all 22 governed artifacts. |
| QC attempt before restoring the required provenance tag | failed | False | naturalproductmech:mibig-2bd59ca78c | QC passed lint, vendored sync, documentation, provenance and source queue, then stopped at tests: 998 passed, 1 failed, 4 skipped. The sole failure was the isolated clone lacking refs/tags/review-base/gentamicin-20261013; it was not a failed archive-content assertion. The tag was subsequently fetched from origin. |
| Targeted verification after restoring the provenance tag | passed | False | naturalproductmech:mibig-2bd59ca78c | After restoring the required tag, the exact previously failed gentamicin archive test passed (1 passed). No repository content was edited for this remediation. |
| Diagnosis of the suite skip conditions | passed | False | naturalproductmech:mibig-2bd59ca78c | The four observed skip cases were reproduced with pytest skip reasons enabled: the optional sibling AntibioticMech comparison has no sibling checkout in the isolated clone, and three command-frontmatter tests have empty parameter sets. This diagnostic invocation executed no passing tests; it reported four skips. |
| Full repository quality gate after environment repair | passed | True | naturalproductmech:mibig-2bd59ca78c | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Exact identity, occurrence and precursor-versus-shunt evidence | passed | True | naturalproductmech:mibig-2bd59ca78c | The original official supplement, exact primary structure figure and complete later primary manuscripts establish the exact isolated compound and nonenzymatic conversion. The 2009 knockout conclusion is bounded to inspected original text/caption and corroborating later primary account. |
| Occurrence organism provenance identifier | passed | True | naturalproductmech:mibig-2bd59ca78c | Official API resolves the recorded Wikidata organism to NCBI Taxonomy 58346. |
| Expression-module source applicability | not_applicable | False | naturalproductmech:mibig-2bd59ca78c | No expression-module or regulatory assertion is used. Direct compound and causal pathway sources were inspected. |

## Scientific And Domain Assessments

### Exact linear dorrigocin congener and consistent encoding

identity: supported. Targets: naturalproductmech:mibig-2bd59ca78c.

The owner encodes the exact 13-epi-dorrigocin A structure with five assigned centres and three E alkenes. Formula, full InChI and full key agree across the local encoding and both stored chemical xrefs.

### Exact equivalence of both chemical xrefs

identity: supported. Targets: naturalproductmech:mibig-2bd59ca78c.

NPA015916 and PubChem 44543739 each match the complete stereochemical identity, including the C13 epimeric distinction. No xref-equivalence defect was found.

### Minted identifier follows the eligible ChEBI rule

grounding: supported. Targets: naturalproductmech:mibig-2bd59ca78c.

The current exact ChEBI candidate is two-star and the pinned eligible inventory has no matching connectivity row. Retaining MINTED is supported.

### Published absolute configuration maps to the exact stored structure

evidence: supported. Targets: naturalproductmech:mibig-2bd59ca78c.

Original supporting data identify compound 5, and the authors' later primary paper explicitly reports established relative and absolute stereochemistry. Its exact-compound figure independently maps to C8S/C9S/C10R/C13S/C14S and all three E alkenes. This supports the recorded configuration while leaving the source-of-occurrence and shunt-metabolite interpretation to the corresponding assessments.

### Exact culture-associated occurrence and organism provenance

evidence: supported. Targets: naturalproductmech:mibig-2bd59ca78c.

The listed 2005 primary abstract explicitly reports this exact congener in S. platensis NRRL 18993 fermentation. The species-level LOTUS occurrence and its Wikidata taxon are supported. Occurrence remains correct even though the paper attributes formation to aqueous rearrangement of a biosynthesized precursor.

### Nonenzymatic formation and the meaning of biosynthesis_origin

evidence: concern. Targets: naturalproductmech:mibig-2bd59ca78c.

The primary source distinguishes this shunt product from the directly biosynthesized parent. The current origin and strong producer/locus assertions need a coordinated qualification that retains the exact observed compound and its provenance. Whether NATURAL_PRODUCT remains suitable under an explicit shunt policy is an adjudication question; the evidence does not justify calling the compound wholly synthetic. The related experimental scope and follow-up are grouped in the locus assessment and action.

### Computed NPClassifier filing and seed history

provenance: supported. Targets: naturalproductmech:mibig-2bd59ca78c.

The exact-key inventory supports the recorded Alkaloids/Lysine alkaloids/Piperidine alkaloids output and pinned model version. The separate PKS source class reflects biosynthetic categorization, so this difference alone is not a contradiction. SEEDED and its two seed events make no claim of scientific sign-off.

### Full resolved optional assertions

scope: not_applicable. Targets: naturalproductmech:mibig-2bd59ca78c.

The complete owner and resolved view contain no optional mechanisms, target, assay, clinical or cross-record assertions to assess. Their absence alone is not treated as a defect.

### NRRL 18993 strain and mgs sequence bridge

grounding: supported. Targets: naturalproductmech:mibig-2bd59ca78c.

The exact source compound, PKS class, GQ274953.1 and taxon 684832 match the accession and primary study. The experimental strain is explicitly NRRL 18993; no cross-strain substitution is needed.

### Demonstrated precursor production versus exact shunt endpoint

evidence: concern. Targets: naturalproductmech:mibig-2bd59ca78c.

The mgs locus is experimentally established for iso-MGS, and the exact target is a chemically established downstream rearrangement product. This is a supported indirect causal connection. The current unqualified experimental producer/locus grades and origin field conceal the nonenzymatic step; the inspected experiments do not establish direct biosynthesis of exact 13-epi-dorrigocin A.

### Native culture occurrence remains distinct from biosynthetic formation

evidence: supported. Targets: naturalproductmech:mibig-2bd59ca78c.

The 2005 report supports the exact compound occurring in NRRL 18993 fermentation. The nonenzymatic conversion is a reason to qualify origin and producer mechanisms, not to delete the supported occurrence or call the structure synthetic automatically.

## Findings

### bgc-shunt-origin-scope: Direct biosynthesis claims omit the established nonenzymatic origin of 13-epi-dorrigocin A

major / open / confirmed; issue key: mibig-bgc0000177-compound5-nonenzymatic-origin-scope.

The record combines NATURAL_PRODUCT, BGC_CHARACTERIZED native producer and CLUSTER_DEMONSTRATED locus without disclosing that the exact target forms by water-mediated rearrangement of biosynthesized iso-MGS. Knockout and heterologous assays establish the precursor pathway; the exact target has supported fermentation occurrence and a supported indirect connection to that pathway. The defect is the missing mechanistic qualification and unchecked transfer of experimental grades, not absence of any biological connection. The origin enum needs an explicit corpus decision for this known nonenzymatic product, rather than an automatic SYNTHETIC replacement.

## Recommended Actions And Acceptance Checks

### represent-shunt-origin-explicitly

Maintain a source-pinned qualification for BGC0000177:5 that names iso-migrastatin as the biosynthesized precursor and water-mediated nonenzymatic ring opening/rearrangement as formation of exact 13-epi-dorrigocin A. Scope PMID:19726666 and PMID:19010685 to precursor knockout/heterologous evidence and PMID:15700980 to the exact conversion and occurrence. Withdraw inherited methods for a direct exact-product claim through the existing locus override mechanism unless the corpus explicitly permits an experimentally connected indirect product grade and emits that qualification. Adjudicate admission/origin semantics in the maintained schema and seeder, adding an explicit reproducible mechanism/origin qualification rather than leaving the unconditional default or relabelling SYNTHETIC by inference. Retain the supported occurrence and NRRL 18993 source context.

- Generated evidence distinguishes experimentally biosynthesized iso-MGS from chemical formation of the exact target.
- Producer and locus grades no longer imply an assayed direct biosynthetic endpoint for 13-epi-dorrigocin A; any retained indirect grade is explicitly defined and qualified.
- Origin handling is explicit and reproducible; no automatic SYNTHETIC label, denial of the precursor relationship or withdrawal of the supported LOTUS occurrence occurs.
- Use just seed-canary naturalproductmech:mibig-2bd59ca78c, inspect output, then documented regeneration and just validate-strict data/natural_products/alkaloids/13-epi-dorrigocin-a.yaml, just verify-reproduction, just verify-corpus --summary and just qc.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-IDENTITY-LOCAL | data/natural_products/alkaloids/13-epi-dorrigocin-a.yaml; Complete owner; label, chemical_structure, xrefs and grounding_notes | supports | The owner represents 13-epi-dorrigocin A with full key HJCZOTBHYAPUHT-FFMZNCFZSA-N, five assigned centres and three specified alkenes. Chemical xrefs are NPA015916 and PubChem 44543739; identity remains minted. |
| E-NPATLAS | https://www.npatlas.org/api/v1/compound/NPA015916?include=classifications; original_name, smiles, inchi, inchikey, origin_reference and reassignments | supports | NPA015916 names 13-epi-dorrigocin A and exactly matches the full record InChI and key. Its origin reference is DOI 10.1021/ja043808i, PMID 15700980, and reassignments is empty. |
| E-PUBCHEM | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/44543739/property/InChI,InChIKey,IsomericSMILES,IUPACName/JSON; PropertyTable.Properties[0] | supports | CID 44543739 exactly matches the full record InChI and key. Its systematic name specifies 2E,6E,8S,9S,10R,11E,13S,14S; there is no stereochemical collapse in this xref. |
| E-CHEBI-IDENTITY | https://www.ebi.ac.uk/chebi/backend/api/public/compound/219677/; name, stars and default_structure id3425154 | supports | CHEBI:219677 is an exact full-structure candidate named 13-epi-dorrigocin A, but it has two stars. It does not meet the repository three-star grounding threshold. |
| E-CHEMISTRY-IDENTITY | /private/tmp/npm-review-work/007/chemistry.json; RDKit 2026.03.5 result generated 2026-10-21T07:03:20.363363Z; complete result inspected | supports | The SMILES regenerates the stored InChI/key, neutral formula C27H41NO8 and exact mass 507.283217272. Assigned centres are zero-based atoms 2:S, 12:S, 14:R, 19:S and 21:S; none is unassigned. |
| E-GROUNDING-SEARCH | data/raw/chebi_structures.tsv; Complete pinned eligible inventory; connectivity prefix, exact label and slug | supports | The pinned eligible inventory contains no match for HJCZOTBHYAPUHT, the exact compound label or its slug. The current exact two-star candidate does not change the eligible-grounding result. |
| E-GROUNDING-POLICY | docs/HARMONIZATION.md; Unambiguous three-star ChEBI default-structure rule | supports | Automatic ChEBI grounding requires an unambiguous matching three-star default structure. |
| E-PRIMARY-SI-METADATA | https://api.figshare.com/v2/articles/3300907; Original supporting-information metadata, DOI 10.1021/ja043808i.s001, file 5138641 | supports | The official publisher repository binds ja043808i_si_001.pdf to the 2005 paper and explicitly identifies 13-epi-dorrigocin A as compound 5. Its abstract reports established stereochemistry for compounds 2–5 except C11 of 3 and 4, so that exception does not concern compound 5. |
| E-PRIMARY-IDENTITY | https://api.figshare.com/v2/file/download/5138641; Ju et al., DOI 10.1021/ja043808i, supporting information S3–S4 and Tables S1/S2 on S5–S6 | supports | The original SI identifies compound 5 as 13-epi-dorrigocin A, reports formula C27H41NO8, [alpha]D25 +14.6 (c 0.13, MeOH), HR-MALDI sodium-adduct mass 530.2736, and position-specific proton/carbon NMR tables. Water-generated compound 5 had ESI-MS, proton NMR and optical rotation identical to the corresponding fermentation isolate. This supports exact molecule identification without interpreting it as directly biosynthesized. |
| E-PRIMARY-STEREOCHEMISTRY | https://pmc.ncbi.nlm.nih.gov/articles/PMC2555980/; Ju et al., DOI 10.1021/ol062470p; paragraph P3 and Figure 1, compound 2c | supports | The original authors explicitly state that relative and absolute stereochemistry of these metabolites, including 13-epi-dorrigocin A, had been established in their 2005 studies. Figure 1 identifies this exact compound as 2c and labels its C13 configuration S. The structure is a linear dorrigocin, not cyclic iso-migrastatin. |
| E-PRIMARY-STEREO-FIGURE | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/867d/2555980/526f0f7ad2df/nihms63829f1.jpg; Figure 1 bottom-left drawing, 2a (13R) and 2c (13S) | supports | The shared drawing specifies the other four centre orientations with OMe solid, OH hashed and two methyl hashed wedges. Compound 2c is explicitly 13S; 2a is the 13R congener. The three alkene geometries are E. |
| E-STEREO-MAPPING | /private/tmp/npm-review-work/007/stereo-mapping.json; Independent transcription of the primary Figure 1 wedges and explicit C13 label | supports | All five owner tetrahedral tags were removed before primary-figure transcription. Natural C8, C9, C10, C13 and C14 map to zero-based atoms 2, 12, 14, 19 and 21; their configurations S, S, R, S and S regenerate the exact owner InChI/key. C2=C3, C6=C7 and C11=C12 were checked visually as E. |
| R-LOCAL | data/natural_products/alkaloids/13-epi-dorrigocin-a.yaml; Complete owner, resolved read_natural_product view and exact-key source rows | supports | The complete record has one MIBiG source, one LOTUS occurrence, two chemical xrefs, producer and locus claims and computed NPClassifier classes. It retains SEEDED and two seed events. No optional pathway, molecular target, bioactivity, clinical, related-record or causal graph assertions are present in the complete view. |
| R-2005-PRIMARY | https://pubmed.ncbi.nlm.nih.gov/15700980/; Complete primary abstract, DOI:10.1021/ja043808i; independently retrieved official PubMed XML | partial | Ju et al. identify exact 13-epi-dorrigocin A as compound 5 accumulated in Streptomyces platensis NRRL 18993 fermentations. Adding XAD-16 resin gives iso-migrastatin instead. In vitro aqueous conversion of iso-migrastatin produces the exact congener and other rearrangement products; water isotope incorporation supports the mechanism. The authors distinguish biosynthesized iso-migrastatin from these shunt metabolites. This supports culture-associated occurrence and requires qualification of direct biosynthetic origin. |
| R-WIKIDATA-SPECIES | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q26291839&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Q26291839 English label, P225 scientific name and P685 NCBI taxonomy identifier | supports | Official API resolves the recorded provenance URI to Streptomyces platensis and NCBI Taxonomy 58346. It identifies the occurrence species; it does not independently equate all strains or establish biosynthesis. |
| R-ORIGIN-POLICY | docs/CURATION.md; docs/HARMONIZATION.md; src/naturalproductmech/schema/naturalproductmech.yaml; scripts/seed_from_sources.py; Origin review criterion and producer/occurrence distinction; schema biosynthesis_origin description and enum; seeder line 1001 | context_only | Repository policy requires the declared producer grade to address biosynthesis of the exact compound by that taxon. Occurrence alone is a separate claim. The seeder assigns NATURAL_PRODUCT by construction; allowed origin values also include SEMISYNTHETIC, SYNTHETIC and UNKNOWN. The supplied descriptions do not by themselves decide how a documented nonenzymatic fermentation shunt should be represented, so adjudication must preserve that mechanism and cannot simply substitute SYNTHETIC. |
| bgc-v5-source | https://mibig.secondarymetabolites.org/repository/BGC0000177.5/annotations.json; compounds[4], loci[0], taxonomy, biosynthesis and legacy_references | supports | Version 5 lists the matching exact 13-epi-dorrigocin A structure as compound index 5, with no compound evidence; entry-wide methods are Knock-out studies and Heterologous expression. The source locus is GQ274953.1, taxon 684832, PKS/Type I; 0/0 unspecified bounds are correctly omitted. References include PMID:19726666, 23394593, 12002995 and 15700980. Source status is active, quality questionable, completeness complete. |
| bgc-gq274953 | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=GQ274953.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text; LOCUS, DEFINITION, VERSION, source feature and REFERENCE 2 | supports | The 53,336 bp deposit explicitly identifies Streptomyces platensis subsp. rosaceus strain NRRL 18993, taxon 684832, and the dorrigocin/migrastatin cluster; it cites PMID:19726666. This bridges the same experimental strain to the source locus and PKS class. The taxon label is a subspecies name; NRRL 18993 is supplied by the accession and experimental paper rather than inferred from the label. |
| bgc-primary-knockout | https://pmc.ncbi.nlm.nih.gov/articles/PMC2785606/; DOI:10.1074/jbc.M109.046805; Experimental Procedures fermentation; Results and Figure 3 caption; Discussion Cluster Naming Rationale and Identification of the iso-MGS Biosynthetic Gene Cluster | partial | The original 2009 paper demonstrates the mgs locus in NRRL 18993 using gene disruptions, including loss of iso-MGS after mgsF inactivation. It explicitly places water-mediated nonenzymatic rearrangement after iso-MGS biosynthesis. The Figure 3 chromatogram caption labels iso-MGS, MGS, DGN A and DGN B; exact 13-epi-DGN A is not separately identified in that caption. The experimentally supported locus-to-precursor association is strong, but it is not direct enzymatic formation of the reviewed shunt product. |
| bgc-primary-heterologous | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=3075207&amp;retmode=xml; PMID:19010685 / DOI:10.1016/j.bmc.2008.10.074, paragraphs P6, P12-P14, P21 and P25-P26; Figure 4 | partial | The complete original manuscript describes pBS11001 from NRRL 18993 introduced into five Streptomyces hosts. Fermentation used XAD-16 resin; the measured product was iso-MGS, identified by retention time, UV, co-injection, LC-MS and NMR. The paper separately explains the DGNs as nonenzymatic rearrangement products. Thus this experiment demonstrates heterologous precursor production and should not be rendered as a directly assayed exact 13-epi-dorrigocin A biosynthetic endpoint. |
| bgc-primary-postpks | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=3582021&amp;retmode=xml; PMID:23394593 / DOI:10.1021/ja4002635; paragraphs P3, P5-P6 and Figure 1 | supports | The complete 2013 primary manuscript explicitly identifies 13-epi-DGN A as compound 4 and states that compounds 2-5 result from water-mediated nonenzymatic rearrangement of iso-MGS (1). It summarizes the knockout and heterologous work as establishing necessity and sufficiency for iso-MGS production. Its new tailoring-gene experiments concern biosynthetic intermediates 10-17, not an enzyme that makes the exact reviewed shunt product. |
| bgc-primary-shunt-2005 | https://pubmed.ncbi.nlm.nih.gov/15700980/; Primary abstract; DOI:10.1021/ja043808i, exact target compound 5 | supports | The primary abstract reports exact 13-epi-dorrigocin A accumulating in NRRL 18993 fermentation and forming from purified iso-MGS in aqueous solution. Resin-supplemented fermentation instead yields iso-MGS. The authors distinguish the biosynthesized precursor from its water-mediated shunt products, supported by oxygen-18 incorporation. This supports occurrence and the nonenzymatic origin distinction simultaneously; it does not make the organism-compound occurrence false. |
| bgc-local-origin-grades | data/raw/mibig_compounds.tsv; scripts/seed_from_sources.py; src/naturalproductmech/schema/naturalproductmech.yaml; conf/producer_evidence.tsv; Exact source row 230/BGC0000177:5; seeder line 1001; schema origin lines 222-227 and grade definitions 875-906 | supports | The target inherits both entry methods, yielding BGC_CHARACTERIZED producer and CLUSTER_DEMONSTRATED locus, while the seeder unconditionally emits NATURAL_PRODUCT. Current definitions describe taxa that biosynthesize the compound and loci that make it; they do not explicitly distinguish biological precursor formation from later nonenzymatic conversion. Existing source-pinned locus withdrawals can qualify methods, but origin/precursor semantics require an explicit maintained decision. No exact-target correction was found in the inspected evidence/reference/strain tables. |

## Limits And Additional Notes

- The original main article was unavailable through the inspected publisher and mirror routes. The official original supporting information and the authors' freely available 2006 primary article were inspected instead.
- The primary figure was mapped atom by atom, but this review does not independently reinterpret the NMR experiments or absolute-configuration experiment from raw spectra.
- The grounding search covers the complete pinned eligible inventory and the identified current exact ChEBI candidate, not every current ontology entry.
- The original 2005 main article could not be retrieved directly. Its official full supplement was inspected by the identity reviewer and supplies exact-isolate and conversion data; no original spectra or isotope incorporation data were independently reanalysed.
- The 2009 primary body was inspected through official indexed PMC text because direct HTML served a browser challenge and its XML endpoint permits metadata only. Figure 3 conclusions are bounded to the inspected caption and experimental text.
- Current schema wording does not explicitly adjudicate nonenzymatic natural-precursor products. The scientific mechanism is established; the appropriate corpus origin enum and treatment of an indirect causal locus link require a maintained, documented decision.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- No scientific owner, source inventory, component, status or seed history was edited. All actions are proposed follow-up.
- A supported fermentation occurrence and indirect precursor-locus connection are retained. The review does not automatically classify a nonenzymatic shunt as synthetic or confer native REVIEWED status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T071115Z-13-epi-dorrigocin-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: '13-epi-dorrigocin A: exact identity and nonenzymatic origin qualification'
started_at: '2026-10-21T07:03:18.854149Z'
finished_at: '2026-10-21T07:11:15.379289Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Exact structure, five absolute configurations, three alkene geometries, both
  xrefs, minted grounding and culture occurrence are supported. Primary studies establish
  formation by water-mediated rearrangement of biosynthesized iso-migrastatin. The
  record needs one coordinated origin/producer/locus qualification that preserves
  this indirect biological connection without implying a directly assayed biosynthetic
  endpoint.
source:
  git_revision: 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b
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
  - path: data/natural_products/alkaloids/13-epi-dorrigocin-a.yaml
    sha256: f961b94f682771fc081d40ee6411c9e8242e7900846bdeff2f301082aac033d9
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete generated owner and resolved mechanism, with every asserted
    field group assessed against local provenance and accessible primary evidence.
  selection: 'Seventh unreviewed path in deterministic order from the initial validated
    list: 91 bundles covered 54 of 3,116 records and 3,062 remained. Ignored bundles
    were included in coverage counting. This bundle assesses one target.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-2bd59ca78c
targets:
- target_id: naturalproductmech:mibig-2bd59ca78c
  path: data/natural_products/alkaloids/13-epi-dorrigocin-a.yaml
  label: 13-epi-dorrigocin A
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
    role: CyanoMetDB exact structure occurrence source
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated owner transform
checks:
- check_id: C-STRICT
  name: Closed-schema and component validation
  status: passed
  required: true
  summary: One complete owner validated with zero ERROR rows.
  command: just validate-strict data/natural_products/alkaloids/13-epi-dorrigocin-a.yaml
    --out /private/tmp/npm-review-work/007/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned
    filing pathways.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016808Z; finished 2026-10-21T06:37:52.997020Z. Exact
    session transcript: /private/tmp/npm-native-checks/verify-corpus.log.'
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3,116 records are byte-identical to the seeder output from committed
    inventories and maintained curation inputs.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-reproduction
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016703Z; finished 2026-10-21T06:38:35.570687Z. Exact
    session transcript: /private/tmp/npm-native-checks/verify-reproduction.log.'
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The documented exhaustive queue command produced 8,928 diagnostic rows
    in 12 queues; deterministic queue output does not establish scientific review.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just review-queue
    --tsv /private/tmp/npm-review-queue-initial.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016598Z; finished 2026-10-21T06:37:11.018366Z. Exact
    session transcript: /private/tmp/npm-native-checks/review-queue.log.'
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'Full configured gate passed using existing CHEBI and GO caches plus the
    committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35
    documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because
    their prefixes have no adapter.'
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.498212Z; finished 2026-10-21T06:38:54.776253Z. Exact
    session transcript: /private/tmp/npm-native-checks/validate-products.log.'
- check_id: qc-environment-attempt1
  name: Initial QC attempt before installing the pinned linter
  status: failed
  required: false
  summary: The first full QC invocation stopped at lint because the isolated copied
    Python environment lacked Ruff. Exact uv.lock version Ruff 0.16.6 was subsequently
    installed and lint passed on later invocations.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.497107Z; finished 2026-10-21T06:36:56.918133Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc.log.'
- check_id: qc-network-attempt2
  name: QC attempt without network access
  status: failed
  required: false
  summary: After Ruff installation, QC passed lint and stopped at vendored-sync because
    sandbox DNS could not reach the pinned public CLAW governance source. Approved
    network access allowed the next invocation to verify all 22 governed artifacts.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:37:57.661447Z; finished 2026-10-21T06:37:59.874785Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt2.log.'
- check_id: qc-tag-attempt3
  name: QC attempt before restoring the required provenance tag
  status: failed
  required: false
  summary: 'QC passed lint, vendored sync, documentation, provenance and source queue,
    then stopped at tests: 998 passed, 1 failed, 4 skipped. The sole failure was the
    isolated clone lacking refs/tags/review-base/gentamicin-20261013; it was not a
    failed archive-content assertion. The tag was subsequently fetched from origin.'
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:38:17.713062Z; finished 2026-10-21T06:45:43.079802Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt3.log.'
- check_id: qc-tag-remediation
  name: Targeted verification after restoring the provenance tag
  status: passed
  required: false
  summary: After restoring the required tag, the exact previously failed gentamicin
    archive test passed (1 passed). No repository content was edited for this remediation.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just test -q
    tests/test_gentamicin_review_archive.py::test_gentamicin_archive_and_scoped_dispositions
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:45:52.383490Z; finished 2026-10-21T06:45:54.030116Z. Exact
    session transcript: /private/tmp/npm-native-checks/gentamicin-tag-check.log.'
- check_id: qc-skip-diagnosis
  name: Diagnosis of the suite skip conditions
  status: passed
  required: false
  summary: 'The four observed skip cases were reproduced with pytest skip reasons
    enabled: the optional sibling AntibioticMech comparison has no sibling checkout
    in the isolated clone, and three command-frontmatter tests have empty parameter
    sets. This diagnostic invocation executed no passing tests; it reported four skips.'
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just test -q
    -rs tests/test_schema.py::test_shared_mech_modules_are_byte_identical_to_the_fleet
    tests/test_skill_frontmatter.py::test_command_frontmatter_has_no_duplicate_keys
    tests/test_skill_frontmatter.py::test_command_frontmatter_is_valid_yaml tests/test_skill_frontmatter.py::test_command_declares_a_usable_description
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:30.259937Z; finished 2026-10-21T06:46:31.251048Z. Exact
    session transcript: /private/tmp/npm-native-checks/skipped-tests-diagnosis.log.'
- check_id: shared-qc
  name: Full repository quality gate after environment repair
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed after installing the pinned
    linter, allowing the read-only governance fetch, and restoring the required provenance
    tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116
    records and zero errors. Documentation, provenance, source queue, governed artifacts,
    generated pages, reproduction, filing integrity and corpus reporting all passed.'
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:02.058886Z; finished 2026-10-21T06:54:53.950582Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt4.log.'
- check_id: C-PRIMARY-SCOPE
  name: Exact identity, occurrence and precursor-versus-shunt evidence
  status: passed
  required: true
  summary: The original official supplement, exact primary structure figure and complete
    later primary manuscripts establish the exact isolated compound and nonenzymatic
    conversion. The 2009 knockout conclusion is bounded to inspected original text/caption
    and corroborating later primary account.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - E-PRIMARY-IDENTITY
  - E-PRIMARY-STEREO-FIGURE
  - bgc-primary-heterologous
  - bgc-primary-postpks
- check_id: C-PROVENANCE-URI
  name: Occurrence organism provenance identifier
  status: passed
  required: true
  summary: Official API resolves the recorded Wikidata organism to NCBI Taxonomy 58346.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - R-WIKIDATA-SPECIES
- check_id: C-IMODULON
  name: Expression-module source applicability
  status: not_applicable
  required: false
  summary: No expression-module or regulatory assertion is used. Direct compound and
    causal pathway sources were inspected.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
evidence:
- evidence_id: E-IDENTITY-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/13-epi-dorrigocin-a.yaml
  locator: Complete owner; label, chemical_structure, xrefs and grounding_notes
  accessed_at: '2026-10-21T07:05:35Z'
  support: supports
  summary: The owner represents 13-epi-dorrigocin A with full key HJCZOTBHYAPUHT-FFMZNCFZSA-N,
    five assigned centres and three specified alkenes. Chemical xrefs are NPA015916
    and PubChem 44543739; identity remains minted.
  snapshot_sha256: f961b94f682771fc081d40ee6411c9e8242e7900846bdeff2f301082aac033d9
- evidence_id: E-NPATLAS
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA015916?include=classifications
  locator: original_name, smiles, inchi, inchikey, origin_reference and reassignments
  accessed_at: '2026-10-21T07:05:54Z'
  support: supports
  summary: NPA015916 names 13-epi-dorrigocin A and exactly matches the full record
    InChI and key. Its origin reference is DOI 10.1021/ja043808i, PMID 15700980, and
    reassignments is empty.
  snapshot_sha256: d474fde1fe16177fdcdc878c32766d751eecb811a45cf899f8c70793fca3a32e
- evidence_id: E-PUBCHEM
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/44543739/property/InChI,InChIKey,IsomericSMILES,IUPACName/JSON
  locator: PropertyTable.Properties[0]
  accessed_at: '2026-10-21T07:05:54Z'
  support: supports
  summary: CID 44543739 exactly matches the full record InChI and key. Its systematic
    name specifies 2E,6E,8S,9S,10R,11E,13S,14S; there is no stereochemical collapse
    in this xref.
  snapshot_sha256: 864efed038a1d7704857a7182f4bc4d5c822055849d8ac9fde858357d88a7c4c
- evidence_id: E-CHEBI-IDENTITY
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/219677/
  locator: name, stars and default_structure id3425154
  accessed_at: '2026-10-21T07:06:20Z'
  support: supports
  summary: CHEBI:219677 is an exact full-structure candidate named 13-epi-dorrigocin
    A, but it has two stars. It does not meet the repository three-star grounding
    threshold.
  snapshot_sha256: 72ffe948df3304014d0420be384973deb1aa172e5757220ebc5380325aaaa581
- evidence_id: E-CHEMISTRY-IDENTITY
  kind: validation
  reference: /private/tmp/npm-review-work/007/chemistry.json
  locator: RDKit 2026.03.5 result generated 2026-10-21T07:03:20.363363Z; complete
    result inspected
  accessed_at: '2026-10-21T07:05:35Z'
  support: supports
  summary: The SMILES regenerates the stored InChI/key, neutral formula C27H41NO8
    and exact mass 507.283217272. Assigned centres are zero-based atoms 2:S, 12:S,
    14:R, 19:S and 21:S; none is unassigned.
  snapshot_sha256: 8a59c33846dffcf8740a211f4284d17bcc335b5b7525248c559e119d5accad89
- evidence_id: E-GROUNDING-SEARCH
  kind: search
  reference: data/raw/chebi_structures.tsv
  locator: Complete pinned eligible inventory; connectivity prefix, exact label and
    slug
  accessed_at: '2026-10-21T07:05:54Z'
  support: supports
  summary: The pinned eligible inventory contains no match for HJCZOTBHYAPUHT, the
    exact compound label or its slug. The current exact two-star candidate does not
    change the eligible-grounding result.
  search_scope: Searched the entire explicitly named inventory with rg --no-ignore
    --hidden for HJCZOTBHYAPUHT, 13-epi-dorrigocin A and 13-epi-dorrigocin-a. Ignored
    files were included; no matching row was returned.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: E-GROUNDING-POLICY
  kind: authority
  reference: docs/HARMONIZATION.md
  locator: Unambiguous three-star ChEBI default-structure rule
  accessed_at: '2026-10-21T06:45:28Z'
  support: supports
  summary: Automatic ChEBI grounding requires an unambiguous matching three-star default
    structure.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: E-PRIMARY-SI-METADATA
  kind: primary_source
  reference: https://api.figshare.com/v2/articles/3300907
  locator: Original supporting-information metadata, DOI 10.1021/ja043808i.s001, file
    5138641
  accessed_at: '2026-10-21T07:07:51Z'
  support: supports
  summary: The official publisher repository binds ja043808i_si_001.pdf to the 2005
    paper and explicitly identifies 13-epi-dorrigocin A as compound 5. Its abstract
    reports established stereochemistry for compounds 2–5 except C11 of 3 and 4, so
    that exception does not concern compound 5.
  snapshot_sha256: 9c662349da5a15c6a68ca9039ec512e70de48709d9379abe93b4a9a2d88a16c6
- evidence_id: E-PRIMARY-IDENTITY
  kind: primary_source
  reference: https://api.figshare.com/v2/file/download/5138641
  locator: Ju et al., DOI 10.1021/ja043808i, supporting information S3–S4 and Tables
    S1/S2 on S5–S6
  accessed_at: '2026-10-21T07:08:21Z'
  support: supports
  summary: The original SI identifies compound 5 as 13-epi-dorrigocin A, reports formula
    C27H41NO8, [alpha]D25 +14.6 (c 0.13, MeOH), HR-MALDI sodium-adduct mass 530.2736,
    and position-specific proton/carbon NMR tables. Water-generated compound 5 had
    ESI-MS, proton NMR and optical rotation identical to the corresponding fermentation
    isolate. This supports exact molecule identification without interpreting it as
    directly biosynthesized.
  snapshot_sha256: e9ff9cd430082f6d88b68f6c30ad65b8ae1e008222b80a05d7298b5d2513c62e
- evidence_id: E-PRIMARY-STEREOCHEMISTRY
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2555980/
  locator: Ju et al., DOI 10.1021/ol062470p; paragraph P3 and Figure 1, compound 2c
  accessed_at: '2026-10-21T07:08:21Z'
  support: supports
  summary: The original authors explicitly state that relative and absolute stereochemistry
    of these metabolites, including 13-epi-dorrigocin A, had been established in their
    2005 studies. Figure 1 identifies this exact compound as 2c and labels its C13
    configuration S. The structure is a linear dorrigocin, not cyclic iso-migrastatin.
  snapshot_sha256: 94328b87c0c7e084ccdc7ee765d1e2e5bf9f03110fc62147fbfdce872294800f
- evidence_id: E-PRIMARY-STEREO-FIGURE
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/867d/2555980/526f0f7ad2df/nihms63829f1.jpg
  locator: Figure 1 bottom-left drawing, 2a (13R) and 2c (13S)
  accessed_at: '2026-10-21T07:08:41Z'
  support: supports
  summary: The shared drawing specifies the other four centre orientations with OMe
    solid, OH hashed and two methyl hashed wedges. Compound 2c is explicitly 13S;
    2a is the 13R congener. The three alkene geometries are E.
  snapshot_sha256: bfc9b22bd25064baeae6d3f0f5b9211e3ba6ac13d3fa471d9acc83cc7d791d5c
- evidence_id: E-STEREO-MAPPING
  kind: validation
  reference: /private/tmp/npm-review-work/007/stereo-mapping.json
  locator: Independent transcription of the primary Figure 1 wedges and explicit C13
    label
  accessed_at: '2026-10-21T07:09:28.960386Z'
  support: supports
  summary: All five owner tetrahedral tags were removed before primary-figure transcription.
    Natural C8, C9, C10, C13 and C14 map to zero-based atoms 2, 12, 14, 19 and 21;
    their configurations S, S, R, S and S regenerate the exact owner InChI/key. C2=C3,
    C6=C7 and C11=C12 were checked visually as E.
  snapshot_sha256: 31b9086847626db372d5a8c062ce79ddf8067602cdfbefb0e1b4960480d496be
- evidence_id: R-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/13-epi-dorrigocin-a.yaml
  locator: Complete owner, resolved read_natural_product view and exact-key source
    rows
  accessed_at: '2026-10-21T07:07:27.244264Z'
  support: supports
  summary: The complete record has one MIBiG source, one LOTUS occurrence, two chemical
    xrefs, producer and locus claims and computed NPClassifier classes. It retains
    SEEDED and two seed events. No optional pathway, molecular target, bioactivity,
    clinical, related-record or causal graph assertions are present in the complete
    view.
  snapshot_sha256: f961b94f682771fc081d40ee6411c9e8242e7900846bdeff2f301082aac033d9
- evidence_id: R-2005-PRIMARY
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15700980/
  locator: Complete primary abstract, DOI:10.1021/ja043808i; independently retrieved
    official PubMed XML
  accessed_at: '2026-10-21T07:06:23.339186Z'
  support: partial
  summary: Ju et al. identify exact 13-epi-dorrigocin A as compound 5 accumulated
    in Streptomyces platensis NRRL 18993 fermentations. Adding XAD-16 resin gives
    iso-migrastatin instead. In vitro aqueous conversion of iso-migrastatin produces
    the exact congener and other rearrangement products; water isotope incorporation
    supports the mechanism. The authors distinguish biosynthesized iso-migrastatin
    from these shunt metabolites. This supports culture-associated occurrence and
    requires qualification of direct biosynthetic origin.
  snapshot_sha256: 1a2a050f0414dd3fc2745a35ecf12a59734adf54cae6b8391ffb91f13c16e0c2
- evidence_id: R-WIKIDATA-SPECIES
  kind: database
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q26291839&props=labels%7Cclaims&languages=en&format=json
  locator: Q26291839 English label, P225 scientific name and P685 NCBI taxonomy identifier
  accessed_at: '2026-10-21T07:06:23.339657Z'
  support: supports
  summary: Official API resolves the recorded provenance URI to Streptomyces platensis
    and NCBI Taxonomy 58346. It identifies the occurrence species; it does not independently
    equate all strains or establish biosynthesis.
  snapshot_sha256: 6540a304eb8b2aa1c20bc3241ff2636b6971aae7cacfb21442fe250c681c705f
- evidence_id: R-ORIGIN-POLICY
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; src/naturalproductmech/schema/naturalproductmech.yaml;
    scripts/seed_from_sources.py
  locator: Origin review criterion and producer/occurrence distinction; schema biosynthesis_origin
    description and enum; seeder line 1001
  accessed_at: '2026-10-21T07:07:27.244264Z'
  support: context_only
  summary: Repository policy requires the declared producer grade to address biosynthesis
    of the exact compound by that taxon. Occurrence alone is a separate claim. The
    seeder assigns NATURAL_PRODUCT by construction; allowed origin values also include
    SEMISYNTHETIC, SYNTHETIC and UNKNOWN. The supplied descriptions do not by themselves
    decide how a documented nonenzymatic fermentation shunt should be represented,
    so adjudication must preserve that mechanism and cannot simply substitute SYNTHETIC.
- evidence_id: bgc-v5-source
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000177.5/annotations.json
  locator: compounds[4], loci[0], taxonomy, biosynthesis and legacy_references
  accessed_at: '2026-10-21T07:06:39Z'
  support: supports
  summary: Version 5 lists the matching exact 13-epi-dorrigocin A structure as compound
    index 5, with no compound evidence; entry-wide methods are Knock-out studies and
    Heterologous expression. The source locus is GQ274953.1, taxon 684832, PKS/Type
    I; 0/0 unspecified bounds are correctly omitted. References include PMID:19726666,
    23394593, 12002995 and 15700980. Source status is active, quality questionable,
    completeness complete.
- evidence_id: bgc-gq274953
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=GQ274953.1&db=nuccore&report=genbank&retmode=text
  locator: LOCUS, DEFINITION, VERSION, source feature and REFERENCE 2
  accessed_at: '2026-10-21T07:06:50Z'
  support: supports
  summary: The 53,336 bp deposit explicitly identifies Streptomyces platensis subsp.
    rosaceus strain NRRL 18993, taxon 684832, and the dorrigocin/migrastatin cluster;
    it cites PMID:19726666. This bridges the same experimental strain to the source
    locus and PKS class. The taxon label is a subspecies name; NRRL 18993 is supplied
    by the accession and experimental paper rather than inferred from the label.
- evidence_id: bgc-primary-knockout
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2785606/
  locator: DOI:10.1074/jbc.M109.046805; Experimental Procedures fermentation; Results
    and Figure 3 caption; Discussion Cluster Naming Rationale and Identification of
    the iso-MGS Biosynthetic Gene Cluster
  accessed_at: '2026-10-21T07:07:38Z'
  support: partial
  summary: The original 2009 paper demonstrates the mgs locus in NRRL 18993 using
    gene disruptions, including loss of iso-MGS after mgsF inactivation. It explicitly
    places water-mediated nonenzymatic rearrangement after iso-MGS biosynthesis. The
    Figure 3 chromatogram caption labels iso-MGS, MGS, DGN A and DGN B; exact 13-epi-DGN
    A is not separately identified in that caption. The experimentally supported locus-to-precursor
    association is strong, but it is not direct enzymatic formation of the reviewed
    shunt product.
  search_scope: PubMed XML and extensive official PMC indexed primary text inspected.
    Direct PMC HTML returned a browser challenge; PMC XML explicitly supplies metadata
    only for this publisher. No uninspected graphical absence claim is made.
- evidence_id: bgc-primary-heterologous
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3075207&retmode=xml
  locator: PMID:19010685 / DOI:10.1016/j.bmc.2008.10.074, paragraphs P6, P12-P14,
    P21 and P25-P26; Figure 4
  accessed_at: '2026-10-21T07:07:54Z'
  support: partial
  summary: The complete original manuscript describes pBS11001 from NRRL 18993 introduced
    into five Streptomyces hosts. Fermentation used XAD-16 resin; the measured product
    was iso-MGS, identified by retention time, UV, co-injection, LC-MS and NMR. The
    paper separately explains the DGNs as nonenzymatic rearrangement products. Thus
    this experiment demonstrates heterologous precursor production and should not
    be rendered as a directly assayed exact 13-epi-dorrigocin A biosynthetic endpoint.
- evidence_id: bgc-primary-postpks
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3582021&retmode=xml
  locator: PMID:23394593 / DOI:10.1021/ja4002635; paragraphs P3, P5-P6 and Figure
    1
  accessed_at: '2026-10-21T07:07:14Z'
  support: supports
  summary: The complete 2013 primary manuscript explicitly identifies 13-epi-DGN A
    as compound 4 and states that compounds 2-5 result from water-mediated nonenzymatic
    rearrangement of iso-MGS (1). It summarizes the knockout and heterologous work
    as establishing necessity and sufficiency for iso-MGS production. Its new tailoring-gene
    experiments concern biosynthetic intermediates 10-17, not an enzyme that makes
    the exact reviewed shunt product.
- evidence_id: bgc-primary-shunt-2005
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15700980/
  locator: Primary abstract; DOI:10.1021/ja043808i, exact target compound 5
  accessed_at: '2026-10-21T07:06:56Z'
  support: supports
  summary: The primary abstract reports exact 13-epi-dorrigocin A accumulating in
    NRRL 18993 fermentation and forming from purified iso-MGS in aqueous solution.
    Resin-supplemented fermentation instead yields iso-MGS. The authors distinguish
    the biosynthesized precursor from its water-mediated shunt products, supported
    by oxygen-18 incorporation. This supports occurrence and the nonenzymatic origin
    distinction simultaneously; it does not make the organism-compound occurrence
    false.
- evidence_id: bgc-local-origin-grades
  kind: record_content
  reference: data/raw/mibig_compounds.tsv; scripts/seed_from_sources.py; src/naturalproductmech/schema/naturalproductmech.yaml;
    conf/producer_evidence.tsv
  locator: Exact source row 230/BGC0000177:5; seeder line 1001; schema origin lines
    222-227 and grade definitions 875-906
  accessed_at: '2026-10-21T07:08:36Z'
  support: supports
  summary: The target inherits both entry methods, yielding BGC_CHARACTERIZED producer
    and CLUSTER_DEMONSTRATED locus, while the seeder unconditionally emits NATURAL_PRODUCT.
    Current definitions describe taxa that biosynthesize the compound and loci that
    make it; they do not explicitly distinguish biological precursor formation from
    later nonenzymatic conversion. Existing source-pinned locus withdrawals can qualify
    methods, but origin/precursor semantics require an explicit maintained decision.
    No exact-target correction was found in the inspected evidence/reference/strain
    tables.
  search_scope: Full target, raw exact-key source row and relevant implemented transform/schema
    blocks read. Correction-table searches included ignored files in the scoped paths.
    No claims about unreviewed congeners are made.
assessments:
- assessment_id: A-IDENTITY-REPRESENTATION
  area: identity
  topic: Exact linear dorrigocin congener and consistent encoding
  outcome: supported
  summary: The owner encodes the exact 13-epi-dorrigocin A structure with five assigned
    centres and three E alkenes. Formula, full InChI and full key agree across the
    local encoding and both stored chemical xrefs.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-NPATLAS
  - E-PUBCHEM
  - E-CHEMISTRY-IDENTITY
- assessment_id: A-XREF-EQUIVALENCE
  area: identity
  topic: Exact equivalence of both chemical xrefs
  outcome: supported
  summary: NPA015916 and PubChem 44543739 each match the complete stereochemical identity,
    including the C13 epimeric distinction. No xref-equivalence defect was found.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-NPATLAS
  - E-PUBCHEM
- assessment_id: A-GROUNDING
  area: grounding
  topic: Minted identifier follows the eligible ChEBI rule
  outcome: supported
  summary: The current exact ChEBI candidate is two-star and the pinned eligible inventory
    has no matching connectivity row. Retaining MINTED is supported.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-CHEBI-IDENTITY
  - E-GROUNDING-SEARCH
  - E-GROUNDING-POLICY
- assessment_id: A-PRIMARY-STEREOCHEMISTRY
  area: evidence
  topic: Published absolute configuration maps to the exact stored structure
  outcome: supported
  summary: Original supporting data identify compound 5, and the authors' later primary
    paper explicitly reports established relative and absolute stereochemistry. Its
    exact-compound figure independently maps to C8S/C9S/C10R/C13S/C14S and all three
    E alkenes. This supports the recorded configuration while leaving the source-of-occurrence
    and shunt-metabolite interpretation to the corresponding assessments.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - E-PRIMARY-SI-METADATA
  - E-PRIMARY-IDENTITY
  - E-PRIMARY-STEREOCHEMISTRY
  - E-PRIMARY-STEREO-FIGURE
  - E-STEREO-MAPPING
- assessment_id: R-OCCURRENCE
  area: evidence
  topic: Exact culture-associated occurrence and organism provenance
  outcome: supported
  summary: The listed 2005 primary abstract explicitly reports this exact congener
    in S. platensis NRRL 18993 fermentation. The species-level LOTUS occurrence and
    its Wikidata taxon are supported. Occurrence remains correct even though the paper
    attributes formation to aqueous rearrangement of a biosynthesized precursor.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - R-LOCAL
  - R-2005-PRIMARY
  - R-WIKIDATA-SPECIES
- assessment_id: R-SHUNT-ORIGIN
  area: evidence
  topic: Nonenzymatic formation and the meaning of biosynthesis_origin
  outcome: concern
  summary: The primary source distinguishes this shunt product from the directly biosynthesized
    parent. The current origin and strong producer/locus assertions need a coordinated
    qualification that retains the exact observed compound and its provenance. Whether
    NATURAL_PRODUCT remains suitable under an explicit shunt policy is an adjudication
    question; the evidence does not justify calling the compound wholly synthetic.
    The related experimental scope and follow-up are grouped in the locus assessment
    and action.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - R-2005-PRIMARY
  - R-ORIGIN-POLICY
  - R-LOCAL
- assessment_id: R-CLASSIFICATION
  area: provenance
  topic: Computed NPClassifier filing and seed history
  outcome: supported
  summary: The exact-key inventory supports the recorded Alkaloids/Lysine alkaloids/Piperidine
    alkaloids output and pinned model version. The separate PKS source class reflects
    biosynthetic categorization, so this difference alone is not a contradiction.
    SEEDED and its two seed events make no claim of scientific sign-off.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - R-LOCAL
- assessment_id: R-OPTIONAL
  area: scope
  topic: Full resolved optional assertions
  outcome: not_applicable
  summary: The complete owner and resolved view contain no optional mechanisms, target,
    assay, clinical or cross-record assertions to assess. Their absence alone is not
    treated as a defect.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - R-LOCAL
- assessment_id: bgc-strain-locus-supported
  area: grounding
  topic: NRRL 18993 strain and mgs sequence bridge
  outcome: supported
  summary: The exact source compound, PKS class, GQ274953.1 and taxon 684832 match
    the accession and primary study. The experimental strain is explicitly NRRL 18993;
    no cross-strain substitution is needed.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - bgc-v5-source
  - bgc-gq274953
- assessment_id: bgc-precursor-causal-link
  area: evidence
  topic: Demonstrated precursor production versus exact shunt endpoint
  outcome: concern
  summary: The mgs locus is experimentally established for iso-MGS, and the exact
    target is a chemically established downstream rearrangement product. This is a
    supported indirect causal connection. The current unqualified experimental producer/locus
    grades and origin field conceal the nonenzymatic step; the inspected experiments
    do not establish direct biosynthesis of exact 13-epi-dorrigocin A.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - bgc-primary-knockout
  - bgc-primary-heterologous
  - bgc-primary-postpks
  - bgc-primary-shunt-2005
  - bgc-local-origin-grades
- assessment_id: bgc-occurrence-retain
  area: evidence
  topic: Native culture occurrence remains distinct from biosynthetic formation
  outcome: supported
  summary: The 2005 report supports the exact compound occurring in NRRL 18993 fermentation.
    The nonenzymatic conversion is a reason to qualify origin and producer mechanisms,
    not to delete the supported occurrence or call the structure synthetic automatically.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  evidence_ids:
  - bgc-primary-shunt-2005
  - bgc-primary-postpks
findings:
- finding_id: bgc-shunt-origin-scope
  issue_key: mibig-bgc0000177-compound5-nonenzymatic-origin-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Direct biosynthesis claims omit the established nonenzymatic origin of 13-epi-dorrigocin
    A
  description: The record combines NATURAL_PRODUCT, BGC_CHARACTERIZED native producer
    and CLUSTER_DEMONSTRATED locus without disclosing that the exact target forms
    by water-mediated rearrangement of biosynthesized iso-MGS. Knockout and heterologous
    assays establish the precursor pathway; the exact target has supported fermentation
    occurrence and a supported indirect connection to that pathway. The defect is
    the missing mechanistic qualification and unchecked transfer of experimental grades,
    not absence of any biological connection. The origin enum needs an explicit corpus
    decision for this known nonenzymatic product, rather than an automatic SYNTHETIC
    replacement.
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  field_paths:
  - biosynthesis_origin
  - producer_organisms[0].evidence_basis
  - producer_organisms[0].notes
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - biosynthetic_gene_clusters[0].link_evidence_basis
  - biosynthetic_gene_clusters[0].evidence
  evidence_ids:
  - bgc-v5-source
  - bgc-primary-knockout
  - bgc-primary-heterologous
  - bgc-primary-postpks
  - bgc-primary-shunt-2005
  - bgc-local-origin-grades
  rule_id: 'review-yaml-record Evidence Rules: exact product and origin; producer-versus-occurrence
    distinction'
  native_severity: 'major: unqualified direct biological origin and experimental grading
    obscure an explicitly established nonenzymatic formation mechanism'
  normalization_reason: One combined issue covers origin, producer and locus semantics
    because all require the same precursor-versus-shunt correction. Supported occurrence
    is retained and is not counted as a separate error.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: pin exact-congener assay applicability and mechanism qualification
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: route precursor biosynthesis and chemical conversion references to their
      respective claims
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: BGC0000177 compound index 5 source row
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: generated origin and producer/locus claims
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/schema/naturalproductmech.yaml
    role: origin and experimental-grade semantics for nonenzymatic products
actions:
- action_id: represent-shunt-origin-explicitly
  description: Maintain a source-pinned qualification for BGC0000177:5 that names
    iso-migrastatin as the biosynthesized precursor and water-mediated nonenzymatic
    ring opening/rearrangement as formation of exact 13-epi-dorrigocin A. Scope PMID:19726666
    and PMID:19010685 to precursor knockout/heterologous evidence and PMID:15700980
    to the exact conversion and occurrence. Withdraw inherited methods for a direct
    exact-product claim through the existing locus override mechanism unless the corpus
    explicitly permits an experimentally connected indirect product grade and emits
    that qualification. Adjudicate admission/origin semantics in the maintained schema
    and seeder, adding an explicit reproducible mechanism/origin qualification rather
    than leaving the unconditional default or relabelling SYNTHETIC by inference.
    Retain the supported occurrence and NRRL 18993 source context.
  finding_ids:
  - bgc-shunt-origin-scope
  target_ids:
  - naturalproductmech:mibig-2bd59ca78c
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: pin exact-congener assay applicability and mechanism qualification
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: route precursor biosynthesis and chemical conversion references to their
      respective claims
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: BGC0000177 compound index 5 source row
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: generated origin and producer/locus claims
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/schema/naturalproductmech.yaml
    role: origin and experimental-grade semantics for nonenzymatic products
  generator: scripts/seed_from_sources.py with maintained source-pinned evidence/origin
    qualification; schema semantics must state how nonenzymatic natural-precursor
    products are handled
  acceptance_checks:
  - Generated evidence distinguishes experimentally biosynthesized iso-MGS from chemical
    formation of the exact target.
  - Producer and locus grades no longer imply an assayed direct biosynthetic endpoint
    for 13-epi-dorrigocin A; any retained indirect grade is explicitly defined and
    qualified.
  - Origin handling is explicit and reproducible; no automatic SYNTHETIC label, denial
    of the precursor relationship or withdrawal of the supported LOTUS occurrence
    occurs.
  - Use just seed-canary naturalproductmech:mibig-2bd59ca78c, inspect output, then
    documented regeneration and just validate-strict data/natural_products/alkaloids/13-epi-dorrigocin-a.yaml,
    just verify-reproduction, just verify-corpus --summary and just qc.
limitations:
- The original main article was unavailable through the inspected publisher and mirror
  routes. The official original supporting information and the authors' freely available
  2006 primary article were inspected instead.
- The primary figure was mapped atom by atom, but this review does not independently
  reinterpret the NMR experiments or absolute-configuration experiment from raw spectra.
- The grounding search covers the complete pinned eligible inventory and the identified
  current exact ChEBI candidate, not every current ontology entry.
- The original 2005 main article could not be retrieved directly. Its official full
  supplement was inspected by the identity reviewer and supplies exact-isolate and
  conversion data; no original spectra or isotope incorporation data were independently
  reanalysed.
- The 2009 primary body was inspected through official indexed PMC text because direct
  HTML served a browser challenge and its XML endpoint permits metadata only. Figure
  3 conclusions are bounded to the inspected caption and experimental text.
- Current schema wording does not explicitly adjudicate nonenzymatic natural-precursor
  products. The scientific mechanism is established; the appropriate corpus origin
  enum and treatment of an indirect causal locus link require a maintained, documented
  decision.
- The configured full identifier-label gate accepts 499 warning-level taxon-label
  mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus;
  its exit 0 is not independent verification of every identifier or of this record's
  scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison
  because the isolated clone has no sibling checkout, and skips three command-frontmatter
  cases because their parameter sets are empty. Pinned-hash and network governance
  checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants.
  They do not establish biological production, stereochemical specificity, evidence
  adequacy or literature-level claim support.
notes:
- No scientific owner, source inventory, component, status or seed history was edited.
  All actions are proposed follow-up.
- A supported fermentation occurrence and indirect precursor-locus connection are
  retained. The review does not automatically classify a nonenzymatic shunt as synthetic
  or confer native REVIEWED status.
tags:
- path-order-campaign
- batch-001
- dorrigocin
```
