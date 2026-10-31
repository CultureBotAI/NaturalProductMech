# Review of 7-epi-cylindrospermopsin

- Review: 20261021T092041Z-7-epi-cylindrospermopsin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T09:02:15.284318Z
- Finished UTC: 2026-10-21T09:20:41.223921Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The epimer identity and four culture-occurrence assertions are supported. Four parent-named MIBiG concepts carry its distinct stereostructure, and three occurrence claims misroute historical parent or synthesis citations. Five other occurrences and exact congener assignment of the four loci remain unresolved within documented access limits. A separate generator defect overstates the NMR-use flag.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 29, batch 003, selected in path order from the fresh-main authoritative validated catalogue and the separately validated pending-PR targets. At selection, 74 of 3116 current records had campaign coverage and 3042 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:88049 | data/natural_products/alkaloids/7-epi-cylindrospermopsin.yaml | generated | 7-epi-cylindrospermopsin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | CHEBI:88049 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | CHEBI:88049 | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | CHEBI:88049 | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | CHEBI:88049 | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:88049 | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate after environment repair | passed | True | CHEBI:88049 | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Exact current identity and parent stereochemical comparison | passed | True | CHEBI:88049 | The epimer owner, current PubChem and ChEBI agree exactly. Parent comparison independently confirms the one-centre S/R difference and distinct neutral/zwitterionic representations. |
| Exact inventory, current source and deposited-locus identity mapping | passed | True | CHEBI:88049 | All four versioned source rows match their current compound structure, taxon, locus and publication identifiers. The independent audit detects the persistent parent-name/epimer-structure mismatch; this passed mapping check does not endorse the biological associations. |
| Current taxon and synonym interpretation | passed | True | CHEBI:88049 | The stored taxon identifiers resolve and the changed ovalisporum genus labels are explicit synonyms. No lineage rename is treated as a different strain or evidence for another epimer. |
| Exact-congener primary citation inspection | passed | True | CHEBI:88049 | All 12 occurrence claims and four producer/locus associations were assessed using the named actually inspected primary text and explicit access limitations; confirmed and provisional scopes are separated. |
| Required complete primary-body coverage | unavailable | True | CHEBI:88049 | Complete original 1992,1994,2000 isotope/isolation,2001 CY-Thai and 2010 Stuken bodies were not obtained in bounded public routes. For 2008 Mihali and 2010 Mazmouz only specified original-body sections were exposed; uninspected portions are not used for absence claims. This leaves the review partial. |
| Structured expression-source applicability | not_applicable | True | CHEBI:88049 | No exact organism in the complete 28-dataset catalogue matches this record; unrelated cyanobacterial context was not transferred. |

## Scientific And Domain Assessments

### Legitimate epimer owner and exact external cross-reference

identity: supported. Targets: CHEBI:88049.

CHEBI:88049, its six-centre structure and PubChem 115005 are internally consistent. Retain this exact epimer identity while separating any parent-only source claims; replacing the entire owner with the parent would discard independent epimer origin evidence.

### Persistent upstream parent-name and epimer-structure mismatch

consistency: concern. Targets: CHEBI:88049.

All four MIBiG compound concepts use the parent name with the epimer structure and historical parent-pathway citations. This mismatch is confirmed at the current source level. The primary reviewer must determine which producer and locus claims require transfer, withdrawal or separate congener support; shared connectivity and locus names do not settle that decision.

### Parent candidates and representation ambiguity

grounding: concern. Targets: CHEBI:88049.

Neutral parent CHEBI:88046 is a verified three-star exact parent stereostructure candidate. Parent zwitterion CHEBI:88044 is separately maintained and shares its Standard InChIKey, so selecting a target requires explicit representation adjudication. Neither identifier is equivalent to the current 7-epi owner.

### Current taxonomic labels and original strain bridges

nomenclature: supported. Targets: CHEBI:88049.

Umezakia, Aphanizomenon and Chrysosporum ovalisporum labels refer to the same current taxon 75695. The AWT205, 10E9, 22D11 and 10E6 GenBank strain qualifiers match their specific source concepts. The 10E6 deposit explicitly provides NIVA:CYA 626; no accession is inferred for the other cultures.

### Collective correction constraints and preservation of the epimer

ownership: concern. Targets: CHEBI:88049.

The current loader cannot represent migrating these four rows to one parent key using four ordinary structure corrections: duplicate parent ChEBI keys, repeated correction targets and loss of the last old-key MIBiG owner violate explicit guards. Any justified collective correction needs a tested maintained extension or migration that selects representation, pins all source and target rows, preserves the independent epimer owner, withholds stale xrefs, and leaves other inventories joined only to scientifically appropriate exact structures.

### occurrences[0]: LOTUS Oscillatoria DOI

evidence: supported. Targets: CHEBI:88049.

Exact epi detected against standards in axenic Oscillatoria cultures; genus rank is broad but not an assertion that every member produces it.

### occurrences[1]: ChEBI Oscillatoria PCC6506 PMID

evidence: supported. Targets: CHEBI:88049.

Same primary experiment as occurrence 0; strain context PCC6506 is explicit and exact epi is chromatographically distinguished from parent.

### occurrences[2]: LOTUS Aphanizomenon 2010 genus claim

evidence: unknown. Targets: CHEBI:88049.

The abstract covers parent-CYN study strains, while the reference list includes original ovalisporum epi isolation. Full-body citation context remains unavailable; do not exclude this genus occurrence solely from the abstract.

### occurrences[3]: LOTUS Umezakia 1994 claim

evidence: unknown. Targets: CHEBI:88049.

Inspected primary abstract concerns parent cylindrospermopsin. Exact epi occurrence is provisionally questionable, but unavailable full methods prevent a definitive whole-article absence finding.

### occurrences[4]: LOTUS ovalisporum original 2000 isolation

evidence: supported. Targets: CHEBI:88049.

Exact epi isolation is directly reported by the original primary abstract; current taxonomy/synonym equivalence is checked independently.

### occurrences[5]: ChEBI ovalisporum original 2000 isolation

evidence: supported. Targets: CHEBI:88049.

PMID:10757726 is the same original publication as DOI:10.1021/np990498m; it supports this exact occurrence, rather than a second independent culture experiment.

### occurrences[6]: LOTUS C. raciborskii 1994 hepatocyte paper

evidence: unknown. Targets: CHEBI:88049.

The inspected abstract tests named parent toxin; the exact provenance and congener in the inaccessible body remain unverified for modern epi. No activity measured for parent is transferred to epi.

### occurrences[7]: LOTUS C. raciborskii 2001 CY-Thai isolation

evidence: unknown. Targets: CHEBI:88049.

The primary abstract explicitly identifies parent and deoxy-CYN; exact epi is not demonstrated by those inspected claims. Full-body availability gap remains, so no blanket congener-absence assertion is made.

### occurrences[8]: LOTUS original 1992 parent citation

evidence: concern. Targets: CHEBI:88049.

Later inspected primary stereochemical revision explicitly maps the original 1992 material to parent cylindrospermopsin. Routing it to the modern epi owner by the old drawing is a confirmed historical-identity mismatch; original 1992 detailed methods remain unavailable.

### occurrences[9]: LOTUS 2005 synthesis citation at C. raciborskii

evidence: concern. Targets: CHEBI:88049.

The inspected primary distinguishes C. raciborskii parent isolation from natural epi in A. ovalisporum, and uses synthesis for absolute identity. It does not support this exact epi/taxon occurrence triple.

### occurrences[10]: LOTUS 2000 isotope-feeding citation

evidence: unknown. Targets: CHEBI:88049.

The inspected abstract and complete SI concern named parent precursor incorporation; a pre-revision drawing cannot establish modern epi. This remains a provisional exact-congener concern pending the main body.

### occurrences[11]: CyanoMetDB original 1992 parent citation

evidence: concern. Targets: CHEBI:88049.

The raw row itself is named Cylindrospermopsin and cites the original parent paper. The later primary revision distinguishes that material from modern epi. NMR-used=yes does not cure the compound identity conflict; the separate rendering assessment addresses the misleading generic NMR-rendering phrase.

### Producer/locus 0: exact 7-epi scope for AWT205

evidence: unknown. Targets: CHEBI:88049.

The cited study and native accession bridge concern a named parent-CYN cluster. Source-level producer assertion and unstated locus grade are faithful to imported metadata, but exact-epimer applicability is not resolved by that fidelity. Do not upgrade to knockout/heterologous/assay evidence or transfer the row to another identity without congener-specific adjudication. This is part of identifier finding ID029-F-SOURCE-CONFLATION, not a duplicate finding.

### Producer/locus 1: exact 7-epi scope for 10E9

evidence: unknown. Targets: CHEBI:88049.

The cited study and native accession bridge concern a named parent-CYN cluster. Source-level producer assertion and unstated locus grade are faithful to imported metadata, but exact-epimer applicability is not resolved by that fidelity. Do not upgrade to knockout/heterologous/assay evidence or transfer the row to another identity without congener-specific adjudication. This is part of identifier finding ID029-F-SOURCE-CONFLATION, not a duplicate finding.

### Producer/locus 2: exact 7-epi scope for 22D11

evidence: unknown. Targets: CHEBI:88049.

The cited study and native accession bridge concern a named parent-CYN cluster. Source-level producer assertion and unstated locus grade are faithful to imported metadata, but exact-epimer applicability is not resolved by that fidelity. Do not upgrade to knockout/heterologous/assay evidence or transfer the row to another identity without congener-specific adjudication. This is part of identifier finding ID029-F-SOURCE-CONFLATION, not a duplicate finding.

### Producer/locus 3: exact 7-epi scope for 10E6

evidence: unknown. Targets: CHEBI:88049.

The cited study and native accession bridge concern a named parent-CYN cluster. Source-level producer assertion and unstated locus grade are faithful to imported metadata, but exact-epimer applicability is not resolved by that fidelity. Do not upgrade to knockout/heterologous/assay evidence or transfer the row to another identity without congener-specific adjudication. This is part of identifier finding ID029-F-SOURCE-CONFLATION, not a duplicate finding.

### Natural epimer versus synthetic identity confirmation

identity: supported. Targets: CHEBI:88049.

Original culture isolation and independent axenic-culture detection support natural origin. Later synthesis and sulfation identify the epimer; they do not show that natural material was generated during extraction. Exact current stereostructure and authority mapping are supplied by the independent identifier packet.

### Mechanism, activity and source-only classification boundaries

completeness: supported. Targets: CHEBI:88049.

The owner does not assert a fully reconstituted pathway, individual enzyme mechanism, cytotoxicity value or target. No parent-only toxicity measurement or heterologous CyrI homolog result is inserted. Computed filing and existing source disagreement discussions are appropriate; the disagreement still requires curation.

### iModulon applicability

completeness: not_applicable. Targets: CHEBI:88049.

No exact organism dataset is available in the inspected structured catalogue; no biology-grade or absence inference follows.

### Source NMR-use field and emitted confirmation wording

evidence: concern. Targets: CHEBI:88049.

A source flag saying NMR was used is rendered as generic structure confirmation. The note must preserve its database method-use meaning even after exact parent/epimer source adjudication.

## Findings

### ID029-F-SOURCE-CONFLATION: Four parent-named MIBiG concepts carry the distinct 7-epimer structure

major / open / confirmed; issue key: cylindrospermopsin-parent-epimer-source-conflation.

BGC0000978:1 through BGC0000981:1 currently and locally name cylindrospermopsin but store the exact 7-epi stereostructure. The official parent and epimer molfiles differ at one hydroxyl-bearing carbon, R versus S, and have different full keys. This is a persistent upstream source identity mismatch, already exposed by the owner discussions, rather than a PubChem structure mismatch or an invalid CHEBI:88049 owner. Primary citation-specific adjudication must decide disposition of each linked biological claim before a collective migration.

### F029-OCCURRENCE-EPIMER: Parent-isolation and synthesis citations are routed to epimer occurrences

major / open / confirmed; issue key: 7-epi-cylindrospermopsin-parent-occurrence-citation-routing.

The 1992 LOTUS/CyanoMetDB origin claims and 2005 LOTUS C. raciborskii claim conflate historical parent material with the modern 7-epi identity. The inspected 2002/2005 primary stereochemical revision identifies the old parent drawing error and explicitly distinguishes parent C. raciborskii isolation from natural epi in A. ovalisporum. Other parent-focused occurrence citations have incomplete full-text coverage and remain provisional concerns, not additional confirmed wrong triples. This finding does not assert that C. raciborskii can never produce epi.

### R029-NMR-WORDING: The NMR-use flag is rendered as full structure confirmation

minor / open / confirmed; issue key: cyanometdb-nmr-used-rendered-as-structure-confirmed.

The exact source row says nmr_used=yes; the generated occurrence says structure confirmed by yes. This both loses the method-use meaning and overstates what the database flag establishes. Parent-versus-epimer applicability is a separate source-scoping problem, and correcting it does not fix the shared note emitter.

## Recommended Actions And Acceptance Checks

### R029-ADJUDICATE-PARENT-SOURCES

Adjudicate each parent-named MIBiG source against its exact strain/congener experiment before moving biological claims. Preserve the legitimate CHEBI:88049 epimer owner, its exact PubChem115005 xref and independently supported epimer origins. If the original concept is parent cylindrospermopsin, correct that source graph through an explicit tested collective migration; if direct epimer evidence instead supports its graph, reconcile the source label and retain the precise evidence. Do not select disposition from the name alone. Pin every participating complete raw row: BGC0000978:1=c886c76a437042cb87aa4eacc38bd12341d069d4b7d8606ee31180c3f4e59c3a; BGC0000979:1=cec492bc57a16dd650d5058151a0e1967292376bb4d502c38c7f07090d5d67f0; BGC0000980:1=0fe1abb1cbee91e257aa138620f7e8c09caa40669a3896f25cf3d50ed73af1a4; BGC0000981:1=bdcbfd395b761adacb964fa26b74460a53ac62a49874b7faea1643946644d70e. Pin the exact neutral/zwitterionic parent and epimer ChEBI rows: CHEBI:88044=6002daba769f405d3ca3f74c115824362d1cb6c8be87c78ab7dd9c52419d790c; CHEBI:88046=61c0b6ce91a67712286e51ff0ab414fa8c0e84dfd5f41452eb6f6539b1252d60; CHEBI:88049=6467623ad7cb8d611d3e93b341648df63a9c2c81f1dd9a34a210e282f0726deb. The existing loader cannot perform four ordinary corrections because both parent ontology entries share a Standard key, repeated target keys are forbidden, and a shared-key split must leave a MIBiG owner at the old key. Extend the maintained correction/generation path to select the intended representation explicitly and preserve the epimer population even if all four MIBiG concepts move. Preserve upstream assertions and per-claim adjudication in generated discussions; do not patch the generated owner or mutate the raw inventories.

- Each source concept has an exact primary locator distinguishing the named parent, the 7-epimer and the experimental strain. Unavailable exact-congener evidence remains explicitly unresolved rather than being upgraded or silently transferred.
- Require all raw source and target-row digests, unique consumption and explicit neutral-versus-zwitterionic representation; stale, incomplete, repeated or conflicting decisions fail. Do not equate CHEBI:88044 and CHEBI:88046 merely because their Standard keys match.
- A canary regenerates separate scientifically supported parent and epimer identities. CHEBI:88049, its six assigned centres, PubChem115005 and independently supported ovalisporum/PCC6506 epimer evidence survive even if no old-key MIBiG row remains.
- Source-owned xrefs are rechecked for each destination; PubChem115005 cannot follow a parent correction. Existing LOTUS, ChEBI-origin and CyanoMetDB rows are joined or withheld only after their own exact-structure adjudication, without blanket movement of old-key occurrences.
- Exercise mixed and all-four migrations, representation collisions, owner preservation, exact-key lookup/PATHS changes, retained source discussions and referenced-record resolution. Structure-corrected rows currently cannot compose with claim-reference and producer-strain/isolate overlays; explicitly test any required extension rather than merely refreshing their hashes.
- Run focused migration/composition tests, strict target validation, source reproduction and required repository QC. Preserve source-method grades conservatively until claim-specific primary evidence warrants a change.

### ACT029-OCCURRENCE-EPIMER

Adjudicate the two confirmed LOTUS 77022 DOI tuples and the parent-named CyanoMetDB 1992 row using the primary stereochemical revision. Preserve the original raw rows. Before any LOTUS exclusion, extend and test the unique-row loader to accept an explicitly reviewed complete row set or exact immutable raw-row selectors; each tuple currently has two raw rows. For exact key LHJPHMKIGRLKDR-YUQKHPEDSA-N and taxon NCBITaxon:77022, pin these complete raw rows: 10.1021/JA00046A067 / Cylindrospermopsis raciborskii / Q5199329 = 3e016b050fa088ae0a6522f719e2c2ca621f0fd23448733f3796547e07a4d89b; 10.1021/JA00046A067 / Raphidiopsis raciborskii / Q67338126 = d5a59afe8f7fc4e83e8311331daa6262b3b2b3bfaf1b0aa0414a2e5d31f5de53; 10.1021/JO0486387 / Cylindrospermopsis raciborskii / Q5199329 = 13e53a6f7a024f553096318b9a79b2d8b255606df5f3773795f2f979ecf240d8; 10.1021/JO0486387 / Raphidiopsis raciborskii / Q67338126 = f5d769f27d7bb4806800f017e5d02a791d95318386f5a6d1114fbeab78b99353. Reject added, removed or changed members. Then withhold the confirmed wrong epi occurrences with auditable source discussions, or reroute only through an explicitly reviewed identity-aware mechanism. Implement and test an explicitly consumed CyanoMetDB identity/occurrence decision path before emission, pinned to complete raw-row SHA256 1fdaecc81ca115f57542f6f5ecc4f7e28062284477929d562ac72df5040055ea; the present emitter has no such adjudication hook. Preserve its original assertion and the primary revision rationale in a discussion. Resolve parent-versus-epimer routing before regeneration; do not hand-edit the emitted occurrence or use NMR-used as identity proof. Leave the five unresolved occurrence claims unchanged pending their missing primary-body context, and retain all four positively supported epi occurrences.

- Both duplicate-label raw rows per confirmed LOTUS tuple are pinned, and every source row-set change fails closed.
- The new CyanoMetDB decision is consumed exactly once and rejects stale complete-row hashes, duplicate or unmatched decisions and reintroduction of the excluded assertion; a changed parent destination never silently transfers unrelated epimer origins.
- The 1992 parent material and 2005 synthesis context no longer appear as unqualified exact epi/C. raciborskii occurrences.
- All four supported A. ovalisporum/Oscillatoria occurrences survive, and unresolved citations are not silently deleted.
- The epi owner and its ChEBI identity survive any separate MIBiG source migration; neutral parent and zwitterionic parent collisions are explicitly adjudicated by the separate identity action.
- Targeted seed canary, strict validation, source provenance and required reproduction/QC checks pass.

### R029-CORRECT-NMR-NOTE

Change the maintained CyanoMetDB note emitter to preserve NMR usage as source metadata, for example NMR used according to CyanoMetDB: yes. Keep DATABASE_ASSERTION and the original flag; do not infer complete or absolute structure confirmation. Coordinate this wording fix with the separate exact-congener occurrence adjudication.

- Yes, no and missing NMR-use values have accurate wording without a generic structure-confirmed claim.
- Raw source flags, references and taxon/strain context are preserved; only independently adjudicated exact-congener decisions alter occurrence membership.
- Seed canary, strict validation and reproduction/QC pass; the fix remains in the maintained emitter rather than a generated YAML patch.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ID029-CHEBI-EPI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/88049/; /private/tmp/npm-review-work/029/identifiers/chebi-88049.json | supports | Current three-star CHEBI:88049 identifies 7-epi-cylindrospermopsin with the owner full key LHJPHMKIGRLKDR-YUQKHPEDSA-N, including S configuration at the hydroxyl-bearing carbon. Its two origin entries remain Aphanizomenon ovalisporum/75695 with PMID 10757726 and Oscillatoria sp./1159, PCC 6506, with PMID 20525864. |
| ID029-EPI-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/88049/; /private/tmp/npm-review-work/029/identifiers/chebi-88049.mol | supports | The official 7-epi molfile independently regenerates the owner full key and formula C15H21N5O7S. It has six assigned carbon stereocentres and no formally charged atoms. |
| ID029-PUBCHEM | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/115005/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; /private/tmp/npm-review-work/029/identifiers/pubchem-115005.json | supports | Current PubChem CID 115005 supplies exactly the owner SMILES, complete Standard InChI and full 7-epi key. Thus the stored PubChem cross-reference is chemically exact for the current epimer owner; any historical parent name associated with this CID does not change its retrieved stereostructure. |
| ID029-CHEBI-SEARCH | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=cylindrospermopsin&amp;size=100; /private/tmp/npm-review-work/029/identifiers/chebi-search.json | supports | The complete current name query returned seven entries on one page. Neutral parent CHEBI:88046 and parent zwitterion CHEBI:88044 are both three-star and share LHJPHMKIGRLKDR-VDPNAHCISA-N; neutral epimer CHEBI:88049 is three-star with YUQKHPEDSA. The generic class and deoxy analogues are not exact replacements. |
| ID029-CHEBI-PARENT | https://www.ebi.ac.uk/chebi/backend/api/public/compound/88046/; /private/tmp/npm-review-work/029/identifiers/chebi-88046.json | supports | Current three-star CHEBI:88046 is neutral cylindrospermopsin, C15H21N5O7S, key LHJPHMKIGRLKDR-VDPNAHCISA-N. Its definition explicitly specifies R at the hydroxyl-bearing carbon, contrasting with S in the epimer definition. This is a distinct parent candidate, not a replacement of the legitimate epimer owner. |
| ID029-PARENT-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/88046/; /private/tmp/npm-review-work/029/identifiers/chebi-88046.mol | supports | Independent atom mapping of the official neutral parent and epimer molfiles finds exactly one stereochemical change: hydroxyl-bearing carbon S in the epimer versus R in the parent. Connectivity, formula and the other five assigned stereocentres agree. |
| ID029-PARENT-ZWITTERION | https://www.ebi.ac.uk/chebi/backend/api/public/compound/88044/; /private/tmp/npm-review-work/029/identifiers/chebi-88044.json | supports | CHEBI:88044 is a separate three-star parent zwitterion entry. It shares the neutral parent Standard InChIKey but its representation transfers a proton from sulfate to a guanidine nitrogen. Standard InChIKey equality must not be treated as a choice between these two maintained ontology identifiers. |
| ID029-PARENT-ZWITTERION-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/88044/; /private/tmp/npm-review-work/029/identifiers/chebi-88044.mol | supports | The parent zwitterion molfile has internal −1/+1 formal charges and net charge zero, unlike the neutral parent with no charged atoms. It independently regenerates the same parent standard key; this confirms the representation distinction behind the two ChEBI entries. |
| ID029-MIBIG-0978 | https://mibig.secondarymetabolites.org/repository/BGC0000978.5/annotations.json; /private/tmp/npm-review-work/029/identifiers/mibig-0978-v5.json | partial | Official BGC0000978, version 5, retains compound name cylindrospermopsin while its exact SMILES regenerates the 7-epi owner key. Taxon/strain AWT205, locus EU140798.1 and PMID 18065631 agree with the parsed inventory. Compound and locus evidence arrays are empty and quality is questionable. The name/structure disagreement remains upstream; these metadata do not prove epimer biosynthesis. |
| ID029-MIBIG-0979 | https://mibig.secondarymetabolites.org/repository/BGC0000979.3/annotations.json; /private/tmp/npm-review-work/029/identifiers/mibig-0979-v3.json | partial | Official BGC0000979, version 3, retains compound name cylindrospermopsin while its exact SMILES regenerates the 7-epi owner key. Taxon/strain 10E9, locus GQ385959.1 and PMID 20430808 agree with the parsed inventory. Compound and locus evidence arrays are empty and quality is questionable. The name/structure disagreement remains upstream; these metadata do not prove epimer biosynthesis. |
| ID029-MIBIG-0980 | https://mibig.secondarymetabolites.org/repository/BGC0000980.3/annotations.json; /private/tmp/npm-review-work/029/identifiers/mibig-0980-v3.json | partial | Official BGC0000980, version 3, retains compound name cylindrospermopsin while its exact SMILES regenerates the 7-epi owner key. Taxon/strain 22D11, locus GQ385960.1 and PMID 20430808 agree with the parsed inventory. Compound and locus evidence arrays are empty and quality is questionable. The name/structure disagreement remains upstream; these metadata do not prove epimer biosynthesis. |
| ID029-MIBIG-0981 | https://mibig.secondarymetabolites.org/repository/BGC0000981.3/annotations.json; /private/tmp/npm-review-work/029/identifiers/mibig-0981-v3.json | partial | Official BGC0000981, version 3, retains compound name cylindrospermopsin while its exact SMILES regenerates the 7-epi owner key. Taxon/strain 10E6, locus GQ385961.1 and PMID 20430808 agree with the parsed inventory. Compound and locus evidence arrays are empty and quality is questionable. The name/structure disagreement remains upstream; these metadata do not prove epimer biosynthesis. |
| ID029-TAXONOMY | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1158,1159,1175,198593,75695,77022,478021,459665,459668,459664&amp;retmode=xml; /private/tmp/npm-review-work/029/identifiers/taxonomy.xml | supports | All ten requested stored taxon IDs resolve. Current 75695 is Umezakia ovalisporum, explicitly listing Aphanizomenon ovalisporum and Chrysosporum ovalisporum as synonyms. Current 77022 is Cylindrospermopsis raciborskii, with Raphidiopsis raciborskii as a synonym. Strain 478021 is AWT205; 459665/459668/459664 retain 10E9/22D11/10E6. Genus-level Oscillatoria/1158 and species-placeholder Oscillatoria sp./1159 are not promoted to a particular culture accession. |
| ID029-GENBANK | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=EU140798.1,GQ385959.1,GQ385960.1,GQ385961.1&amp;rettype=gb&amp;retmode=text; /private/tmp/npm-review-work/029/identifiers/genbank-four-loci.gb | supports | The four original deposits independently bridge locus, strain, taxon and publication. EU140798.1 is 42156 bp, AWT205/478021, PMID 18065631. GQ385959.1 and GQ385960.1 are 6921 bp partial cluster sequences for 10E9/459665 and 22D11/459668. GQ385961.1 is 57112 bp including flanks for 10E6/459664, explicitly NIVA:CYA 626. These three cite PMID 20430808 and Germany, 2004. All deposits name cylindrospermopsin; sequence metadata alone cannot assign an epimer or establish complete locus function. |
| ID029-COMPARISON | /private/tmp/npm-review-work/029/identifiers/comparison.json; /private/tmp/npm-review-work/029/check-identifiers.py | supports | The executed comparison confirms equality of the complete owner and resolved snapshot, exact owner/PubChem/ChEBI/MIBiG structure keys, six-centre stereochemistry and the single mapped parent/epimer difference, neutral-versus-zwitterion representations, full parsed source-row digests, taxon/locus/publication mappings and the ignored-inclusive local search. All comparison assertions passed. |
| ID029-LOCAL-SEARCH | /private/tmp/npm-review-work/029/identifiers/local-search.txt | supports | The ignored-inclusive search finds one generated owner for this connectivity, the current 7-epimer. Both parent representations are present in raw ChEBI structures and parent origins are present, but no generated parent owner or matching maintained correction is present in the searched scopes. The raw CyanoMetDB row and multiple LOTUS rows also carry the epimer key despite parent-oriented names/citations; citation-specific disposition belongs to the separate primary review. |
| ID029-CORRECTION-GUARDS | src/naturalproductmech/curate/structure_corrections.py; Complete file read; seed_from_sources.py lines 876–988 inspected for ChEBI ambiguity and grouping. SHA256 pins the correction module only. | supports | The existing correction loader requires exactly one raw ChEBI row per target key, forbids repeated target keys within a correction set, and requires a remaining old-key MIBiG owner for SPLIT_SHARED_WITH_CHEBI. Both parent representations share a key, and all four source rows currently share the epimer key. Ordinary four-row corrections therefore cannot implement a collective parent migration. The seeder deliberately retains ambiguous ChEBI matches as minted/REVIEW_NEEDED and builds this record population from MIBiG structure groups. |
| E029-OWNER | data/natural_products/alkaloids/7-epi-cylindrospermopsin.yaml; Entire owner including 12 occurrences, four producers/loci, source concepts, discussions and all history | supports | The owner is the exact 7-epi structure and already exposes the parent-name/source-structure disagreement. It contains no curated pathway, causal graph, protein example or molecular activity measurement. All 12 rendered occurrence claims and four locus associations are individually assessed below. |
| E029-RAW | data/raw/lotus_occurrences.tsv; All exact full-key source rows captured in /029/local-sources.json | supports | Fourteen LOTUS raw rows collapse to nine rendered LOTUS occurrences. Each of the five C. raciborskii DOI tuples has two raw rows with different historical labels/Wikidata IDs but the same taxon and full key. The two ChEBI origins and one CyanoMetDB row bring the rendered total to twelve. Synonym collapse is expected; it is not itself a duplicate-occurrence defect. |
| E029-BANKER | https://pubmed.ncbi.nlm.nih.gov/10757726/; Complete original 2000 abstract; DOI:10.1021/np990498m | supports | The original paper explicitly reports isolation of 7-epicylindrospermopsin from an Aphanizomenon ovalisporum culture originating in Lake Kinneret, with 2D NMR and HRMS. This supports both the LOTUS and ChEBI species occurrences. Its historical stereostructure must be interpreted with the later C7 reassignment; the inaccessible body does not justify any workup-artifact assertion. |
| E029-REVISION | https://pubmed.ncbi.nlm.nih.gov/11942831/; Complete primary 2002 abstract, corresponding selected main-text conclusions in shared web receipt | supports | Synthesis of the originally proposed parent structure gave NMR data matching natural 7-epicylindrospermopsin, while C7 inversion and chemical correlation established the revised parent. The historical drawing and the actual parent material must therefore not be treated as an unchanged modern epi identity. |
| E029-ABSOLUTE | https://www.lookchem.com/FreePDFArticle/812646-16-5.htm; Original 2005 paper text, printed 1970–1971 and final synthetic product; shared web receipt lines 1121–1178 | supports | The primary synthesis assigns natural 7-epi as (7S,8R,10S,12S,13R,14S), versus parent C7R with the other centres unchanged, using spectral comparison and optical rotation. Synthetic sulfation confirms identity; it is not evidence that natural 7-epi is an isolation artifact. |
| E029-2005-ORIGIN | https://www.lookchem.com/FreePDFArticle/812646-16-5.htm; Original 2005 Introduction printed 1963–1964; web lines 133–152,176–178,218–252 and cited source list; snapshot SHA pins the combined saved web-response receipt containing this exact passage, not a single-page download. | refutes | The paper explicitly associates the parent isolate with C. raciborskii and Umezakia natans, and the minor natural epimer with A. ovalisporum. It then explains why the original parent/epimer stereostructures were reversed. This supports chemical identity but contradicts importing this synthesis citation as an exact epi occurrence in C. raciborskii. The same original 1992 parent material must be interpreted under that revision. |
| E029-2005-SI | https://ndownloader.figshare.com/files/5133574; Official jo0486387_si_001.pdf, S103 named synthetic 7-epicylindrospermopsin 1; S1 and S103 inspected in preparation, S103 reinspected here | supports | The official SI labels the final synthetic spectrum as 7-epicylindrospermopsin 1. It supports the synthetic compound assignment and supplies no C. raciborskii culture-isolation experiment or natural-artifact test. |
| E029-FEEDING | https://pubmed.ncbi.nlm.nih.gov/10813909/; Complete 2000 primary abstract plus entire three-page official isotope SI read in preparation | partial | The paper follows cylindrospermopsin 1 in C. raciborskii by labeled precursor incorporation. It does not identify the investigated natural material as the separate 7-epi congener in the inspected abstract/SI. The pre-revision drawing cannot independently establish modern epimer identity. Main-body access remains unavailable, so a whole-article absence claim is not made. |
| E029-FEEDING-SI | https://ndownloader.figshare.com/files/5811339; All three original isotope-enriched spectra; page1 reinspected for this target | partial | The complete supplement contains isotope-enriched NMR data for the named parent biosynthesis investigation. No gene experiment follows from precursor incorporation, and its historical drawing is not an independent current absolute-configuration assignment. |
| E029-1992 | https://api.crossref.org/works/10.1021/ja00046a067; Official bibliographic record and exact original publication identified by the later primary revision | partial | This is the original 1992 cylindrospermopsin isolation paper. Its detailed body remains inaccessible here. The inspected 2005 primary explicitly connects this material to parent cylindrospermopsin and corrects the historical C7 assignment; the citation cannot be routed solely by that obsolete drawing to modern epi. |
| E029-1994-UMEZAKIA | https://pubmed.ncbi.nlm.nih.gov/7940590/; Complete original abstract; DOI:10.1016/0041-0101(94)90008-6 | partial | The abstract describes mouse pathology and biochemical assays of cylindrospermopsin isolated from Umezakia natans. It does not specifically identify 7-epi in the inspected text. The full body was not obtained; exact epi occurrence remains unverified rather than a claimed species-wide absence. |
| E029-1994-HEPATOCYTE | https://pubmed.ncbi.nlm.nih.gov/8198579/; Complete original abstract; DOI:10.1006/bbrc.1994.1694 | partial | The primary abstract concerns cytotoxicity and glutathione effects of named parent cylindrospermopsin in rat hepatocytes, with C. raciborskii origin context. No exact epi assay or occurrence is identified in that abstract. A complete-body chemical provenance check is unavailable. |
| E029-2001-THAI | https://pubmed.ncbi.nlm.nih.gov/11223086/; Complete original abstract; DOI:10.1016/S0041-0101(00)00236-1 | partial | CY-Thai is identified as C. raciborskii by morphology and 16S; parent CYN was matched to an HPLC standard and characterized by HPLC-MS/MS, alongside deoxy-CYN. The inspected abstract assigns these two congeners, not epi. The Griffith repository record has zero public bundles, and no full body was obtained; absence of epi elsewhere in the article is not asserted. |
| E029-OSC-PRIMARY | https://journals.asm.org/doi/full/10.1128/aem.00717-10; Original Methods and Results through intracellular/extracellular analysis; Table 2, Figure 4 caption and chromatographic separation paragraphs, web lines 103–237; snapshot SHA pins the combined saved web-response receipt containing this exact passage, not a single-page download. | supports | Axenic Oscillatoria PCC6506 grown in BG11 was tested against purchased standards. HPLC separated epi at 8.9 min from parent at 9.3 min, followed by LC-MS/MS. Exact epi was detected in cells and medium. Four additional strains were compared, with PCC6602 negative under tested conditions. Quantification assumes equal UV extinction coefficients; ELISA alone was explicitly nonspecific. These results support both Oscillatoria occurrence entries without conflating the two epimers. |
| E029-OSC-ABSTRACT | https://pubmed.ncbi.nlm.nih.gov/20525864/; Complete original abstract and exact DOI bridge 10.1128/AEM.00717-10 | supports | The abstract independently identifies exact epi as the major PCC6506 metabolite and reports positive observations in other Oscillatoria strains. It supports natural occurrence and the original publication equivalence between the LOTUS DOI and ChEBI PMID; those are two database assertions of one experiment, not independent publications. |
| E029-AWT205 | https://journals.asm.org/doi/10.1128/aem.01988-07; Original introduction, complete Methods, beginning Results and Tables1/2 inspected; web lines 92–122 and 172–233; snapshot SHA pins the combined saved web-response receipt containing this exact passage, not a single-page download. | partial | AWT205 was studied by genomic sequencing, domain/homology annotation and cyrJ PCR screening against reported parent-toxin phenotypes. Table1 calls AWT205 CYLN-positive and distinguishes parent from the epi literature in the introduction. These inspected experiments are not an exact-epi knockout, heterologous reconstruction or terminal enzyme assay. The complete Results narrative and figure pixels were not retrieved, so no whole-article negative claim is made. |
| E029-APH-BGC | https://pubmed.ncbi.nlm.nih.gov/20430808/; Complete original abstract; DOI:10.1099/mic.0.036988-0 | partial | The paper sequences the full parent-CYN cluster plus flanks from German 10E6 and approximately 7 kb fragments covering partial cyrC, cyrA and partial cyrB from 10E9 and 22D11. Comparative sequence/rearrangement analysis is explicit. The abstract does not resolve exact epi product formation in these three strains; the full body remained unavailable. |
| E029-APH-REFS | https://www.microbiologyresearch.org/content/journal/micro/10.1099/mic.0.036988-0; Official abstract and reference list; full-text loading endpoint unsuccessful; snapshot SHA pins the combined saved web-response receipt containing this exact passage, not a single-page download. | partial | The official reference list includes the original Banker 2000 A. ovalisporum epi-isolation paper. Consequently the genus-level Aphanizomenon occurrence could reflect an introductory literature statement, even though the abstract study strains concern parent CYN. Without the body it is unresolved, not a confirmed wrong occurrence. |
| E029-CYRI-BOUNDARY | https://pubmed.ncbi.nlm.nih.gov/29653078/; Complete 2018 abstract; PMID:21404419 metadata-only lead also inspected | context_only | The later 2018 biochemical work uses CyrI from Oscillatoria PCC7926/PCC6506 and engineered chimeras/mutants. It supports strain-dependent epimer formation but does not directly establish the four stored AWT205/Aphanizomenon associations. PMID:21404419 has no abstract in the retrieved official payload; no uninspected 2011 experimental details are imported. |
| E029-ACCESS | /private/tmp/npm-review-work/029/science-primary-access.json; Five bounded receipt files, web-primary-receipts.json and reused preparation failures | context_only | Original publisher, PMC, BioC, HAL and institutional repository leads were checked without paid access. PMC/HAL returned challenge HTML despite HTTP 200, BioC returned no-result text, publisher full-text endpoints returned HTTP 403, and Griffith reported zero bundles. Only the named successful original text passages, abstracts and SI pages were treated as inspected evidence. |
| E029-LOTUS-LOADER | src/naturalproductmech/curate/lotus_exclusions.py; Entire implemented loader, especially matches length equals 1 and unique exact tuple | supports | Each suspect 77022 DOI tuple has two complete raw rows. The loader rejects nonunique matches and repeated decision keys. A valid correction therefore needs a tested row-set or exact raw-row-selector extension; two ordinary exclusion rows cannot safely represent the decision. |
| E029-IMODULON | https://imodulondb.org/; Complete installed-runner 28-dataset catalogue captured in review 010 preparation; compared to all target genera | context_only | No catalogue dataset matches Cylindrospermopsis/Raphidiopsis, Aphanizomenon/Chrysosporum/Umezakia, or Oscillatoria. Synechococcus elongatus is a different organism and was not substituted. Structured expression context is not applicable to the present exact producer/occurrence claims. |
| E029-CLASSIFICATION | data/raw/npclassifier.tsv; Exact owner-key row in local-sources.json | supports | The computed Alkaloids/Guanidine alkaloids/Tricyclic guanidine alkaloids and nonglycoside values match the owner. This model filing is independent of the imported NRPS/PKS/OTHER cluster classes and does not establish product-to-locus specificity. |
| R029-CYANO | data/raw/cyanometdb_occurrences.tsv; Complete exact-key Cylindrospermopsin row and emitted occurrence 11 | supports | The source row carries the epimer full key, parent name Cylindrospermopsin, NCBITaxon:77022, DOI:10.1021/ja00046a067, strain n.a. and nmr_used=yes. The owner emits structure confirmed by yes. Exact modern congener applicability is separately adjudicated against primary sources; the Boolean NMR-use flag itself does not assert full structure confirmation. |
| R029-CYANO-EXTRACT | scripts/extract_cyanometdb.py; Source-column mapping for NMR_used into nmr_used | context_only | The extractor transfers the source NMR_used text as a method-use field. It does not reinterpret yes as an analytical technique name or an absolute-stereochemistry verdict. |
| R029-CYANO-SEED | scripts/seed_from_sources.py; CyanoMetDB occurrence evidence-note assembly, lines 1225–1235 | context_only | The emitter interpolates nmr_used after structure confirmed by, producing the overbroad and ungrammatical owner note. This is a shared generator defect, distinct from whether this particular original source refers to parent or epimer. |

## Limits And Additional Notes

- GenBank headers, bibliographic references and source qualifiers were inspected for all four deposits. No complete CDS translation or congener-specific biosynthetic function was inferred from those sequence records.
- Versioned MIBiG endpoints were retrieved for the four versions used by this owner. Their empty evidence arrays describe those database assertions, not proof that the cited literature lacks experiments.
- The ChEBI search is limited to its complete seven-result name query. The current parent representation collision is demonstrated by both official molfiles and raw rows, rather than inferred from names.
- This scientific section is intentionally partial because several required primary bodies remain unavailable. Abstract-level positive observations are retained without turning missing full text into evidence of absence.
- AWT205 Methods/Table 1/Table 2 and selected original 2010 Oscillatoria Methods/Results were inspected through official publisher text; figure pixels and unreturned body portions were not read. No complete-body claim is made for those sources.
- The original 2000 epi-isolation abstract directly supports occurrence, but detailed workup controls were not inspected. No inference of extraction-induced epimerization or synthetic origin is justified.
- The 2005 absolute-configuration and historical-origin passages were inspected through a public primary-paper mirror and official SI; the publisher main PDF was inaccessible.
- The 2010 Aphanizomenon genus occurrence is unresolved because its original body could contain a relevant ovalisporum literature statement. Its reference list alone is not treated as proof of that statement or proof of absence.
- The 1994 Umezakia, 1994 hepatocyte, 2001 CY-Thai and 2000 feeding exact-epi associations remain provisional concerns. They are not included in the confirmed occurrence-removal recommendation.
- Later CyrI studies on Oscillatoria proteins do not independently validate the four stored AWT205/Aphanizomenon exact-epi locus claims. No native knockout, exact-congener absence or universal species incapacity is inferred.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- Baseline reuse concerns the identical committed inputs and original executed checks; it does not claim a fresh network/governance or ontology-cache refresh.
- No scientific owner, inventory, curation table, native status or history was edited. Actions are proposed work.
- Baseline gates retain their actual original receipts after byte-for-byte input verification; target strict validation ran afresh. Scientific failed or unavailable checks are distinct from bundle validation.

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
review_id: 20261021T092041Z-7-epi-cylindrospermopsin
title: Review of 7-epi-cylindrospermopsin
started_at: '2026-10-21T09:02:15.284318Z'
finished_at: '2026-10-21T09:20:41.223921Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The epimer identity and four culture-occurrence assertions are supported.
  Four parent-named MIBiG concepts carry its distinct stereostructure, and three occurrence
  claims misroute historical parent or synthesis citations. Five other occurrences
  and exact congener assignment of the four loci remain unresolved within documented
  access limits. A separate generator defect overstates the NMR-use flag.
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
  - path: data/natural_products/alkaloids/7-epi-cylindrospermopsin.yaml
    sha256: cd0ecece8f5ee40265ca95af1571a3b0a0e66f92e3ca3740e43230f6e1b928d4
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
  - path: scripts/extract_cyanometdb.py
    sha256: cccfc32d65a5df99c768bf5055f7ea56ac9678b7029b9dd23483295603ec365e
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
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 29, batch 003, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated pending-PR targets.
    At selection, 74 of 3116 current records had campaign coverage and 3042 remained.
    The population search included ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:88049
targets:
- target_id: CHEBI:88049
  path: data/natural_products/alkaloids/7-epi-cylindrospermopsin.yaml
  label: 7-epi-cylindrospermopsin
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
    path: data/natural_products/alkaloids/7-epi-cylindrospermopsin.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
checks:
- check_id: C-STRICT
  name: Closed-schema target validation
  status: passed
  required: true
  summary: The documented target strict validator completed; scientific support is
    assessed separately.
  target_ids:
  - CHEBI:88049
  command: just validate-strict data/natural_products/alkaloids/7-epi-cylindrospermopsin.yaml
    --out /private/tmp/npm-review-work/029/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T09:02:19.221563Z
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned
    filing pathways.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016808+00:00; finished 2026-10-21T06:37:52.997020+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/verify-corpus.log. Reused
    for batch 003 after verifying exact HEAD/base/tree equality and all tracked worktree
    bytes against the original baseline. This command was not rerun for batch 003;
    original times and receipts are retained.'
  target_ids:
  - CHEBI:88049
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3,116 records are byte-identical to the seeder output from committed
    inventories and maintained curation inputs.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-reproduction
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016703+00:00; finished 2026-10-21T06:38:35.570687+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/verify-reproduction.log.
    Reused for batch 003 after verifying exact HEAD/base/tree equality and all tracked
    worktree bytes against the original baseline. This command was not rerun for batch
    003; original times and receipts are retained.'
  target_ids:
  - CHEBI:88049
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The documented exhaustive queue command produced 8,928 diagnostic rows
    in 12 queues; deterministic queue output does not establish scientific review.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just review-queue
    --tsv /private/tmp/npm-review-queue-initial.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016598+00:00; finished 2026-10-21T06:37:11.018366+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/review-queue.log. Reused
    for batch 003 after verifying exact HEAD/base/tree equality and all tracked worktree
    bytes against the original baseline. This command was not rerun for batch 003;
    original times and receipts are retained.'
  target_ids:
  - CHEBI:88049
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'Full configured gate passed using existing CHEBI and GO caches plus the
    committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35
    documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because
    their prefixes have no adapter.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.498212+00:00; finished 2026-10-21T06:38:54.776253+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/validate-products.log.
    Reused for batch 003 after verifying exact HEAD/base/tree equality and all tracked
    worktree bytes against the original baseline. This command was not rerun for batch
    003; original times and receipts are retained.'
  target_ids:
  - CHEBI:88049
- check_id: shared-qc
  name: Full repository quality gate after environment repair
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed after installing the pinned
    linter, allowing the read-only governance fetch, and restoring the required provenance
    tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116
    records and zero errors. Documentation, provenance, source queue, governed artifacts,
    generated pages, reproduction, filing integrity and corpus reporting all passed.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:02.058886+00:00; finished 2026-10-21T06:54:53.950582+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/qc-attempt4.log. Reused
    for batch 003 after verifying exact HEAD/base/tree equality and all tracked worktree
    bytes against the original baseline. This command was not rerun for batch 003;
    original times and receipts are retained.'
  target_ids:
  - CHEBI:88049
- check_id: ID029-C-STRUCTURES
  name: Exact current identity and parent stereochemical comparison
  status: passed
  required: true
  summary: The epimer owner, current PubChem and ChEBI agree exactly. Parent comparison
    independently confirms the one-centre S/R difference and distinct neutral/zwitterionic
    representations.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - ID029-CHEBI-EPI
  - ID029-EPI-MOL
  - ID029-PUBCHEM
  - ID029-CHEBI-PARENT
  - ID029-PARENT-MOL
  - ID029-PARENT-ZWITTERION
  - ID029-PARENT-ZWITTERION-MOL
  - ID029-COMPARISON
  command: .venv/bin/python /private/tmp/npm-review-work/029/check-identifiers.py
  exit_code: 0
  expected_exit_code: 0
- check_id: ID029-C-SOURCE-MAPPING
  name: Exact inventory, current source and deposited-locus identity mapping
  status: passed
  required: true
  summary: All four versioned source rows match their current compound structure,
    taxon, locus and publication identifiers. The independent audit detects the persistent
    parent-name/epimer-structure mismatch; this passed mapping check does not endorse
    the biological associations.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - ID029-MIBIG-0978
  - ID029-MIBIG-0979
  - ID029-MIBIG-0980
  - ID029-MIBIG-0981
  - ID029-GENBANK
  - ID029-COMPARISON
- check_id: ID029-C-TAXONOMY
  name: Current taxon and synonym interpretation
  status: passed
  required: true
  summary: The stored taxon identifiers resolve and the changed ovalisporum genus
    labels are explicit synonyms. No lineage rename is treated as a different strain
    or evidence for another epimer.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - ID029-TAXONOMY
  - ID029-GENBANK
- check_id: C029-SOURCE-SCOPE
  name: Exact-congener primary citation inspection
  status: passed
  required: true
  summary: All 12 occurrence claims and four producer/locus associations were assessed
    using the named actually inspected primary text and explicit access limitations;
    confirmed and provisional scopes are separated.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-OWNER
  - E029-BANKER
  - E029-OSC-PRIMARY
  - E029-AWT205
  - E029-APH-BGC
  - E029-2005-ORIGIN
- check_id: C029-FULLTEXT-GAPS
  name: Required complete primary-body coverage
  status: unavailable
  required: true
  summary: Complete original 1992,1994,2000 isotope/isolation,2001 CY-Thai and 2010
    Stuken bodies were not obtained in bounded public routes. For 2008 Mihali and
    2010 Mazmouz only specified original-body sections were exposed; uninspected portions
    are not used for absence claims. This leaves the review partial.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-ACCESS
  - E029-1992
  - E029-1994-UMEZAKIA
  - E029-1994-HEPATOCYTE
  - E029-2001-THAI
  - E029-APH-REFS
- check_id: C029-IMODULON
  name: Structured expression-source applicability
  status: not_applicable
  required: true
  summary: No exact organism in the complete 28-dataset catalogue matches this record;
    unrelated cyanobacterial context was not transferred.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-IMODULON
evidence:
- evidence_id: ID029-CHEBI-EPI
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/88049/
  locator: /private/tmp/npm-review-work/029/identifiers/chebi-88049.json
  accessed_at: '2026-10-21T09:09:30.946466Z'
  support: supports
  summary: Current three-star CHEBI:88049 identifies 7-epi-cylindrospermopsin with
    the owner full key LHJPHMKIGRLKDR-YUQKHPEDSA-N, including S configuration at the
    hydroxyl-bearing carbon. Its two origin entries remain Aphanizomenon ovalisporum/75695
    with PMID 10757726 and Oscillatoria sp./1159, PCC 6506, with PMID 20525864.
  snapshot_sha256: 46be84b889442b40cdaadd095b5c54dc6cb83170a69d538bac9b524e5074378c
- evidence_id: ID029-EPI-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/88049/
  locator: /private/tmp/npm-review-work/029/identifiers/chebi-88049.mol
  accessed_at: '2026-10-21T09:09:30.888157Z'
  support: supports
  summary: The official 7-epi molfile independently regenerates the owner full key
    and formula C15H21N5O7S. It has six assigned carbon stereocentres and no formally
    charged atoms.
  snapshot_sha256: 429e043b74abe135e2daaa2594c735dfee19c3a1624204c32d8e571677280946
- evidence_id: ID029-PUBCHEM
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/115005/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: /private/tmp/npm-review-work/029/identifiers/pubchem-115005.json
  accessed_at: '2026-10-21T09:09:30.508440Z'
  support: supports
  summary: Current PubChem CID 115005 supplies exactly the owner SMILES, complete
    Standard InChI and full 7-epi key. Thus the stored PubChem cross-reference is
    chemically exact for the current epimer owner; any historical parent name associated
    with this CID does not change its retrieved stereostructure.
  snapshot_sha256: 351f7c48898df691f96cc9e8d48f56c9db4294ba60425ec03ff2ad8a4cb00ee9
- evidence_id: ID029-CHEBI-SEARCH
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=cylindrospermopsin&size=100
  locator: /private/tmp/npm-review-work/029/identifiers/chebi-search.json
  accessed_at: '2026-10-21T09:09:31.066631Z'
  support: supports
  summary: The complete current name query returned seven entries on one page. Neutral
    parent CHEBI:88046 and parent zwitterion CHEBI:88044 are both three-star and share
    LHJPHMKIGRLKDR-VDPNAHCISA-N; neutral epimer CHEBI:88049 is three-star with YUQKHPEDSA.
    The generic class and deoxy analogues are not exact replacements.
  snapshot_sha256: 9af7b73fa4e3ca21d89e431eba0e3d08456c64b3a5c82db1196f2be300d5346d
  search_scope: Official ChEBI es_search term cylindrospermopsin, size 100, all seven
    returned entries on its single result page inspected on 2026-10-21.
- evidence_id: ID029-CHEBI-PARENT
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/88046/
  locator: /private/tmp/npm-review-work/029/identifiers/chebi-88046.json
  accessed_at: '2026-10-21T09:10:14.079553Z'
  support: supports
  summary: Current three-star CHEBI:88046 is neutral cylindrospermopsin, C15H21N5O7S,
    key LHJPHMKIGRLKDR-VDPNAHCISA-N. Its definition explicitly specifies R at the
    hydroxyl-bearing carbon, contrasting with S in the epimer definition. This is
    a distinct parent candidate, not a replacement of the legitimate epimer owner.
  snapshot_sha256: 7df042a0984bf81c6bef58288cb7918550f56497f8b2a87947a553456352e46f
- evidence_id: ID029-PARENT-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/88046/
  locator: /private/tmp/npm-review-work/029/identifiers/chebi-88046.mol
  accessed_at: '2026-10-21T09:10:13.908816Z'
  support: supports
  summary: 'Independent atom mapping of the official neutral parent and epimer molfiles
    finds exactly one stereochemical change: hydroxyl-bearing carbon S in the epimer
    versus R in the parent. Connectivity, formula and the other five assigned stereocentres
    agree.'
  snapshot_sha256: e1d36f26634ec61503ac1935de17ed2870103dc0fb10bb81aaf2a66f13ea5da7
- evidence_id: ID029-PARENT-ZWITTERION
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/88044/
  locator: /private/tmp/npm-review-work/029/identifiers/chebi-88044.json
  accessed_at: '2026-10-21T09:10:13.950812Z'
  support: supports
  summary: CHEBI:88044 is a separate three-star parent zwitterion entry. It shares
    the neutral parent Standard InChIKey but its representation transfers a proton
    from sulfate to a guanidine nitrogen. Standard InChIKey equality must not be treated
    as a choice between these two maintained ontology identifiers.
  snapshot_sha256: 9b14cdb757295e52003af9cb941dbb3f6a0c95060e9ee3cf5cc0786c23f95976
- evidence_id: ID029-PARENT-ZWITTERION-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/88044/
  locator: /private/tmp/npm-review-work/029/identifiers/chebi-88044.mol
  accessed_at: '2026-10-21T09:10:13.913041Z'
  support: supports
  summary: The parent zwitterion molfile has internal −1/+1 formal charges and net
    charge zero, unlike the neutral parent with no charged atoms. It independently
    regenerates the same parent standard key; this confirms the representation distinction
    behind the two ChEBI entries.
  snapshot_sha256: 98a7031aa0a11b4957546f974c340d45691f4b2047acda999fc538b4f63146d7
- evidence_id: ID029-MIBIG-0978
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000978.5/annotations.json
  locator: /private/tmp/npm-review-work/029/identifiers/mibig-0978-v5.json
  accessed_at: '2026-10-21T09:09:31.034287Z'
  support: partial
  summary: Official BGC0000978, version 5, retains compound name cylindrospermopsin
    while its exact SMILES regenerates the 7-epi owner key. Taxon/strain AWT205, locus
    EU140798.1 and PMID 18065631 agree with the parsed inventory. Compound and locus
    evidence arrays are empty and quality is questionable. The name/structure disagreement
    remains upstream; these metadata do not prove epimer biosynthesis.
  snapshot_sha256: 52bdb1b331fd87eba6019d5c384a87a55acf8d972e3220a4b247389764c7ef07
- evidence_id: ID029-MIBIG-0979
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000979.3/annotations.json
  locator: /private/tmp/npm-review-work/029/identifiers/mibig-0979-v3.json
  accessed_at: '2026-10-21T09:09:31.267456Z'
  support: partial
  summary: Official BGC0000979, version 3, retains compound name cylindrospermopsin
    while its exact SMILES regenerates the 7-epi owner key. Taxon/strain 10E9, locus
    GQ385959.1 and PMID 20430808 agree with the parsed inventory. Compound and locus
    evidence arrays are empty and quality is questionable. The name/structure disagreement
    remains upstream; these metadata do not prove epimer biosynthesis.
  snapshot_sha256: 35d011cd89a8b51d0bb5d539cf0464e779199264188647f9ba1dc3cf7731593e
- evidence_id: ID029-MIBIG-0980
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000980.3/annotations.json
  locator: /private/tmp/npm-review-work/029/identifiers/mibig-0980-v3.json
  accessed_at: '2026-10-21T09:09:31.442652Z'
  support: partial
  summary: Official BGC0000980, version 3, retains compound name cylindrospermopsin
    while its exact SMILES regenerates the 7-epi owner key. Taxon/strain 22D11, locus
    GQ385960.1 and PMID 20430808 agree with the parsed inventory. Compound and locus
    evidence arrays are empty and quality is questionable. The name/structure disagreement
    remains upstream; these metadata do not prove epimer biosynthesis.
  snapshot_sha256: 31112a1ed05aab90a53383b1f9d1fc285af095b1eeefe5da944943a8567a7acc
- evidence_id: ID029-MIBIG-0981
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000981.3/annotations.json
  locator: /private/tmp/npm-review-work/029/identifiers/mibig-0981-v3.json
  accessed_at: '2026-10-21T09:09:31.460757Z'
  support: partial
  summary: Official BGC0000981, version 3, retains compound name cylindrospermopsin
    while its exact SMILES regenerates the 7-epi owner key. Taxon/strain 10E6, locus
    GQ385961.1 and PMID 20430808 agree with the parsed inventory. Compound and locus
    evidence arrays are empty and quality is questionable. The name/structure disagreement
    remains upstream; these metadata do not prove epimer biosynthesis.
  snapshot_sha256: 9f5c3d70ff6b97d3ad8ce0bdb47834d45bd4d4d14f273771b64cf45f1219379d
- evidence_id: ID029-TAXONOMY
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1158,1159,1175,198593,75695,77022,478021,459665,459668,459664&retmode=xml
  locator: /private/tmp/npm-review-work/029/identifiers/taxonomy.xml
  accessed_at: '2026-10-21T09:09:30.761090Z'
  support: supports
  summary: All ten requested stored taxon IDs resolve. Current 75695 is Umezakia ovalisporum,
    explicitly listing Aphanizomenon ovalisporum and Chrysosporum ovalisporum as synonyms.
    Current 77022 is Cylindrospermopsis raciborskii, with Raphidiopsis raciborskii
    as a synonym. Strain 478021 is AWT205; 459665/459668/459664 retain 10E9/22D11/10E6.
    Genus-level Oscillatoria/1158 and species-placeholder Oscillatoria sp./1159 are
    not promoted to a particular culture accession.
  snapshot_sha256: 2da6a6794bbfc51eb2d11af288f269e9923f43108b058897148462d916197b59
- evidence_id: ID029-GENBANK
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=EU140798.1,GQ385959.1,GQ385960.1,GQ385961.1&rettype=gb&retmode=text
  locator: /private/tmp/npm-review-work/029/identifiers/genbank-four-loci.gb
  accessed_at: '2026-10-21T09:11:24.269993Z'
  support: supports
  summary: The four original deposits independently bridge locus, strain, taxon and
    publication. EU140798.1 is 42156 bp, AWT205/478021, PMID 18065631. GQ385959.1
    and GQ385960.1 are 6921 bp partial cluster sequences for 10E9/459665 and 22D11/459668.
    GQ385961.1 is 57112 bp including flanks for 10E6/459664, explicitly NIVA:CYA 626.
    These three cite PMID 20430808 and Germany, 2004. All deposits name cylindrospermopsin;
    sequence metadata alone cannot assign an epimer or establish complete locus function.
  snapshot_sha256: ca0738b032e605d84124277e7ecf008ad50c8ff420888e7fecd8a3dab49fc002
- evidence_id: ID029-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/029/identifiers/comparison.json
  locator: /private/tmp/npm-review-work/029/check-identifiers.py
  accessed_at: '2026-10-21T09:11:34.001342Z'
  support: supports
  snapshot_sha256: e4444bda0d4303185ffa8a7da7bddd7021ed3a6997467b3dddc8e3b2a5371bd9
  summary: The executed comparison confirms equality of the complete owner and resolved
    snapshot, exact owner/PubChem/ChEBI/MIBiG structure keys, six-centre stereochemistry
    and the single mapped parent/epimer difference, neutral-versus-zwitterion representations,
    full parsed source-row digests, taxon/locus/publication mappings and the ignored-inclusive
    local search. All comparison assertions passed.
- evidence_id: ID029-LOCAL-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/029/identifiers/local-search.txt
  accessed_at: '2026-10-21T09:11:34.001342Z'
  support: supports
  snapshot_sha256: a7b886bc7900b31f6ba78b2305331f4bbc906d50090ecd9093de6a2fcb9b28af
  search_scope: rg -n -i --no-ignore --hidden across data/natural_products, data/raw,
    curation, conf, src and scripts for the shared first-block key, both exact ChEBI
    IDs, all four BGC accessions and cylindrospermopsin names; all 70 result lines
    inspected.
  summary: The ignored-inclusive search finds one generated owner for this connectivity,
    the current 7-epimer. Both parent representations are present in raw ChEBI structures
    and parent origins are present, but no generated parent owner or matching maintained
    correction is present in the searched scopes. The raw CyanoMetDB row and multiple
    LOTUS rows also carry the epimer key despite parent-oriented names/citations;
    citation-specific disposition belongs to the separate primary review.
- evidence_id: ID029-CORRECTION-GUARDS
  kind: record_content
  reference: src/naturalproductmech/curate/structure_corrections.py
  locator: Complete file read; seed_from_sources.py lines 876–988 inspected for ChEBI
    ambiguity and grouping. SHA256 pins the correction module only.
  accessed_at: '2026-10-21T09:14:36.343473Z'
  support: supports
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
  summary: The existing correction loader requires exactly one raw ChEBI row per target
    key, forbids repeated target keys within a correction set, and requires a remaining
    old-key MIBiG owner for SPLIT_SHARED_WITH_CHEBI. Both parent representations share
    a key, and all four source rows currently share the epimer key. Ordinary four-row
    corrections therefore cannot implement a collective parent migration. The seeder
    deliberately retains ambiguous ChEBI matches as minted/REVIEW_NEEDED and builds
    this record population from MIBiG structure groups.
- evidence_id: E029-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/7-epi-cylindrospermopsin.yaml
  locator: Entire owner including 12 occurrences, four producers/loci, source concepts,
    discussions and all history
  accessed_at: '2026-10-21T09:19:00.660702Z'
  support: supports
  summary: The owner is the exact 7-epi structure and already exposes the parent-name/source-structure
    disagreement. It contains no curated pathway, causal graph, protein example or
    molecular activity measurement. All 12 rendered occurrence claims and four locus
    associations are individually assessed below.
  snapshot_sha256: cd0ecece8f5ee40265ca95af1571a3b0a0e66f92e3ca3740e43230f6e1b928d4
- evidence_id: E029-RAW
  kind: record_content
  reference: data/raw/lotus_occurrences.tsv
  locator: All exact full-key source rows captured in /029/local-sources.json
  accessed_at: '2026-10-21T09:19:00.660702Z'
  support: supports
  summary: Fourteen LOTUS raw rows collapse to nine rendered LOTUS occurrences. Each
    of the five C. raciborskii DOI tuples has two raw rows with different historical
    labels/Wikidata IDs but the same taxon and full key. The two ChEBI origins and
    one CyanoMetDB row bring the rendered total to twelve. Synonym collapse is expected;
    it is not itself a duplicate-occurrence defect.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: E029-BANKER
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/10757726/
  locator: Complete original 2000 abstract; DOI:10.1021/np990498m
  accessed_at: '2026-10-21T08:37:37.098424Z'
  support: supports
  summary: The original paper explicitly reports isolation of 7-epicylindrospermopsin
    from an Aphanizomenon ovalisporum culture originating in Lake Kinneret, with 2D
    NMR and HRMS. This supports both the LOTUS and ChEBI species occurrences. Its
    historical stereostructure must be interpreted with the later C7 reassignment;
    the inaccessible body does not justify any workup-artifact assertion.
  snapshot_sha256: 661e049d06ef68085f822773d3c43fc4b8c358dbfbc6343be60c0b0608d72189
- evidence_id: E029-REVISION
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/11942831/
  locator: Complete primary 2002 abstract, corresponding selected main-text conclusions
    in shared web receipt
  accessed_at: '2026-10-21T08:38:23.187808Z'
  support: supports
  summary: Synthesis of the originally proposed parent structure gave NMR data matching
    natural 7-epicylindrospermopsin, while C7 inversion and chemical correlation established
    the revised parent. The historical drawing and the actual parent material must
    therefore not be treated as an unchanged modern epi identity.
  snapshot_sha256: 240bf14390facc617a8c16824f0facc57bec8f4c84be311079f170268b89022c
- evidence_id: E029-ABSOLUTE
  kind: primary_source
  reference: https://www.lookchem.com/FreePDFArticle/812646-16-5.htm
  locator: Original 2005 paper text, printed 1970–1971 and final synthetic product;
    shared web receipt lines 1121–1178
  accessed_at: '2026-10-21T08:40:57Z'
  support: supports
  summary: The primary synthesis assigns natural 7-epi as (7S,8R,10S,12S,13R,14S),
    versus parent C7R with the other centres unchanged, using spectral comparison
    and optical rotation. Synthetic sulfation confirms identity; it is not evidence
    that natural 7-epi is an isolation artifact.
  snapshot_sha256: 214dc595bbbf0c7a166ce3ef578658bf406ab2001e4175acd8a89c932122c67a
- evidence_id: E029-2005-ORIGIN
  kind: primary_source
  reference: https://www.lookchem.com/FreePDFArticle/812646-16-5.htm
  locator: Original 2005 Introduction printed 1963–1964; web lines 133–152,176–178,218–252
    and cited source list; snapshot SHA pins the combined saved web-response receipt
    containing this exact passage, not a single-page download.
  accessed_at: '2026-10-21T09:13:54Z'
  support: refutes
  summary: The paper explicitly associates the parent isolate with C. raciborskii
    and Umezakia natans, and the minor natural epimer with A. ovalisporum. It then
    explains why the original parent/epimer stereostructures were reversed. This supports
    chemical identity but contradicts importing this synthesis citation as an exact
    epi occurrence in C. raciborskii. The same original 1992 parent material must
    be interpreted under that revision.
  snapshot_sha256: 25867ca17d416041a3999145015edc6bf7b37ed327d383238f37788649630948
- evidence_id: E029-2005-SI
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/5133574
  locator: Official jo0486387_si_001.pdf, S103 named synthetic 7-epicylindrospermopsin
    1; S1 and S103 inspected in preparation, S103 reinspected here
  accessed_at: '2026-10-21T08:39:20.481894Z'
  support: supports
  summary: The official SI labels the final synthetic spectrum as 7-epicylindrospermopsin
    1. It supports the synthetic compound assignment and supplies no C. raciborskii
    culture-isolation experiment or natural-artifact test.
  snapshot_sha256: c9ef7562269af2f081e2ae96ce82d5f94b1562c0a5515608d643c28e6c32bbe9
- evidence_id: E029-FEEDING
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/10813909/
  locator: Complete 2000 primary abstract plus entire three-page official isotope
    SI read in preparation
  accessed_at: '2026-10-21T08:38:23.187808Z'
  support: partial
  summary: The paper follows cylindrospermopsin 1 in C. raciborskii by labeled precursor
    incorporation. It does not identify the investigated natural material as the separate
    7-epi congener in the inspected abstract/SI. The pre-revision drawing cannot independently
    establish modern epimer identity. Main-body access remains unavailable, so a whole-article
    absence claim is not made.
  snapshot_sha256: 240bf14390facc617a8c16824f0facc57bec8f4c84be311079f170268b89022c
- evidence_id: E029-FEEDING-SI
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/5811339
  locator: All three original isotope-enriched spectra; page1 reinspected for this
    target
  accessed_at: '2026-10-21T08:39:20.482119Z'
  support: partial
  summary: The complete supplement contains isotope-enriched NMR data for the named
    parent biosynthesis investigation. No gene experiment follows from precursor incorporation,
    and its historical drawing is not an independent current absolute-configuration
    assignment.
  snapshot_sha256: 910d039b1273f419911404eddd299c26a95319f929453d5cb93159c2fc434ce9
- evidence_id: E029-1992
  kind: database
  reference: https://api.crossref.org/works/10.1021/ja00046a067
  locator: Official bibliographic record and exact original publication identified
    by the later primary revision
  accessed_at: '2026-10-21T08:37:37.410258Z'
  support: partial
  summary: This is the original 1992 cylindrospermopsin isolation paper. Its detailed
    body remains inaccessible here. The inspected 2005 primary explicitly connects
    this material to parent cylindrospermopsin and corrects the historical C7 assignment;
    the citation cannot be routed solely by that obsolete drawing to modern epi.
  snapshot_sha256: 60fadc429b18da00714773ac891f3d98a2d1c11107e693c6a16ec2279a5851e5
- evidence_id: E029-1994-UMEZAKIA
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/7940590/
  locator: Complete original abstract; DOI:10.1016/0041-0101(94)90008-6
  accessed_at: '2026-10-21T09:11:15.865290Z'
  support: partial
  summary: The abstract describes mouse pathology and biochemical assays of cylindrospermopsin
    isolated from Umezakia natans. It does not specifically identify 7-epi in the
    inspected text. The full body was not obtained; exact epi occurrence remains unverified
    rather than a claimed species-wide absence.
  snapshot_sha256: 587a705e2bd7dafe7fab0a68816f57e75daa0b4bd35fbc7d895cd446ebd1d305
- evidence_id: E029-1994-HEPATOCYTE
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/8198579/
  locator: Complete original abstract; DOI:10.1006/bbrc.1994.1694
  accessed_at: '2026-10-21T09:11:15.865290Z'
  support: partial
  summary: The primary abstract concerns cytotoxicity and glutathione effects of named
    parent cylindrospermopsin in rat hepatocytes, with C. raciborskii origin context.
    No exact epi assay or occurrence is identified in that abstract. A complete-body
    chemical provenance check is unavailable.
  snapshot_sha256: 587a705e2bd7dafe7fab0a68816f57e75daa0b4bd35fbc7d895cd446ebd1d305
- evidence_id: E029-2001-THAI
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/11223086/
  locator: Complete original abstract; DOI:10.1016/S0041-0101(00)00236-1
  accessed_at: '2026-10-21T09:11:15.865290Z'
  support: partial
  summary: CY-Thai is identified as C. raciborskii by morphology and 16S; parent CYN
    was matched to an HPLC standard and characterized by HPLC-MS/MS, alongside deoxy-CYN.
    The inspected abstract assigns these two congeners, not epi. The Griffith repository
    record has zero public bundles, and no full body was obtained; absence of epi
    elsewhere in the article is not asserted.
  snapshot_sha256: 587a705e2bd7dafe7fab0a68816f57e75daa0b4bd35fbc7d895cd446ebd1d305
- evidence_id: E029-OSC-PRIMARY
  kind: primary_source
  reference: https://journals.asm.org/doi/full/10.1128/aem.00717-10
  locator: Original Methods and Results through intracellular/extracellular analysis;
    Table 2, Figure 4 caption and chromatographic separation paragraphs, web lines
    103–237; snapshot SHA pins the combined saved web-response receipt containing
    this exact passage, not a single-page download.
  accessed_at: '2026-10-21T09:13:30Z'
  support: supports
  summary: Axenic Oscillatoria PCC6506 grown in BG11 was tested against purchased
    standards. HPLC separated epi at 8.9 min from parent at 9.3 min, followed by LC-MS/MS.
    Exact epi was detected in cells and medium. Four additional strains were compared,
    with PCC6602 negative under tested conditions. Quantification assumes equal UV
    extinction coefficients; ELISA alone was explicitly nonspecific. These results
    support both Oscillatoria occurrence entries without conflating the two epimers.
  snapshot_sha256: 25867ca17d416041a3999145015edc6bf7b37ed327d383238f37788649630948
- evidence_id: E029-OSC-ABSTRACT
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/20525864/
  locator: Complete original abstract and exact DOI bridge 10.1128/AEM.00717-10
  accessed_at: '2026-10-21T08:37:37.098424Z'
  support: supports
  summary: The abstract independently identifies exact epi as the major PCC6506 metabolite
    and reports positive observations in other Oscillatoria strains. It supports natural
    occurrence and the original publication equivalence between the LOTUS DOI and
    ChEBI PMID; those are two database assertions of one experiment, not independent
    publications.
  snapshot_sha256: 661e049d06ef68085f822773d3c43fc4b8c358dbfbc6343be60c0b0608d72189
- evidence_id: E029-AWT205
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/aem.01988-07
  locator: Original introduction, complete Methods, beginning Results and Tables1/2
    inspected; web lines 92–122 and 172–233; snapshot SHA pins the combined saved
    web-response receipt containing this exact passage, not a single-page download.
  accessed_at: '2026-10-21T09:12:32Z'
  support: partial
  summary: AWT205 was studied by genomic sequencing, domain/homology annotation and
    cyrJ PCR screening against reported parent-toxin phenotypes. Table1 calls AWT205
    CYLN-positive and distinguishes parent from the epi literature in the introduction.
    These inspected experiments are not an exact-epi knockout, heterologous reconstruction
    or terminal enzyme assay. The complete Results narrative and figure pixels were
    not retrieved, so no whole-article negative claim is made.
  snapshot_sha256: 25867ca17d416041a3999145015edc6bf7b37ed327d383238f37788649630948
- evidence_id: E029-APH-BGC
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/20430808/
  locator: Complete original abstract; DOI:10.1099/mic.0.036988-0
  accessed_at: '2026-10-21T08:37:37.098424Z'
  support: partial
  summary: The paper sequences the full parent-CYN cluster plus flanks from German
    10E6 and approximately 7 kb fragments covering partial cyrC, cyrA and partial
    cyrB from 10E9 and 22D11. Comparative sequence/rearrangement analysis is explicit.
    The abstract does not resolve exact epi product formation in these three strains;
    the full body remained unavailable.
  snapshot_sha256: 661e049d06ef68085f822773d3c43fc4b8c358dbfbc6343be60c0b0608d72189
- evidence_id: E029-APH-REFS
  kind: primary_source
  reference: https://www.microbiologyresearch.org/content/journal/micro/10.1099/mic.0.036988-0
  locator: Official abstract and reference list; full-text loading endpoint unsuccessful;
    snapshot SHA pins the combined saved web-response receipt containing this exact
    passage, not a single-page download.
  accessed_at: '2026-10-21T09:13:14Z'
  support: partial
  summary: The official reference list includes the original Banker 2000 A. ovalisporum
    epi-isolation paper. Consequently the genus-level Aphanizomenon occurrence could
    reflect an introductory literature statement, even though the abstract study strains
    concern parent CYN. Without the body it is unresolved, not a confirmed wrong occurrence.
  snapshot_sha256: 25867ca17d416041a3999145015edc6bf7b37ed327d383238f37788649630948
- evidence_id: E029-CYRI-BOUNDARY
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/29653078/
  locator: Complete 2018 abstract; PMID:21404419 metadata-only lead also inspected
  accessed_at: '2026-10-21T09:14:33.806039Z'
  support: context_only
  summary: The later 2018 biochemical work uses CyrI from Oscillatoria PCC7926/PCC6506
    and engineered chimeras/mutants. It supports strain-dependent epimer formation
    but does not directly establish the four stored AWT205/Aphanizomenon associations.
    PMID:21404419 has no abstract in the retrieved official payload; no uninspected
    2011 experimental details are imported.
  snapshot_sha256: 49ed535b4e0d44075d76b80b46d8279f7d1ccb13583abe943f172549c68842c5
- evidence_id: E029-ACCESS
  kind: search
  reference: /private/tmp/npm-review-work/029/science-primary-access.json
  locator: Five bounded receipt files, web-primary-receipts.json and reused preparation
    failures
  accessed_at: '2026-10-21T09:19:00.660702Z'
  support: context_only
  summary: Original publisher, PMC, BioC, HAL and institutional repository leads were
    checked without paid access. PMC/HAL returned challenge HTML despite HTTP 200,
    BioC returned no-result text, publisher full-text endpoints returned HTTP 403,
    and Griffith reported zero bundles. Only the named successful original text passages,
    abstracts and SI pages were treated as inspected evidence.
  snapshot_sha256: 97137f75e4185d256c5cdc220b31722113871fcd2daf1427455d4fd1d42beba5
  search_scope: Exact cited publications and narrowly relevant CyrI follow-up; no
    unrestricted literature-absence search. Earlier failed URLs were not repeatedly
    downloaded without a distinct public-source lead.
- evidence_id: E029-LOTUS-LOADER
  kind: record_content
  reference: src/naturalproductmech/curate/lotus_exclusions.py
  locator: Entire implemented loader, especially matches length equals 1 and unique
    exact tuple
  accessed_at: '2026-10-21T09:19:00.660702Z'
  support: supports
  summary: Each suspect 77022 DOI tuple has two complete raw rows. The loader rejects
    nonunique matches and repeated decision keys. A valid correction therefore needs
    a tested row-set or exact raw-row-selector extension; two ordinary exclusion rows
    cannot safely represent the decision.
  snapshot_sha256: 6352cac7c587eab5a56d907c523cc899d02d197009081624bf8649c675ee30f7
- evidence_id: E029-IMODULON
  kind: search
  reference: https://imodulondb.org/
  locator: Complete installed-runner 28-dataset catalogue captured in review 010 preparation;
    compared to all target genera
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: No catalogue dataset matches Cylindrospermopsis/Raphidiopsis, Aphanizomenon/Chrysosporum/Umezakia,
    or Oscillatoria. Synechococcus elongatus is a different organism and was not substituted.
    Structured expression context is not applicable to the present exact producer/occurrence
    claims.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  search_scope: All 28 returned dataset entries; source catalogue reused with original
    access time. This is resource applicability, not evidence that a pathway or phenotype
    is absent.
- evidence_id: E029-CLASSIFICATION
  kind: record_content
  reference: data/raw/npclassifier.tsv
  locator: Exact owner-key row in local-sources.json
  accessed_at: '2026-10-21T09:19:00.660702Z'
  support: supports
  summary: The computed Alkaloids/Guanidine alkaloids/Tricyclic guanidine alkaloids
    and nonglycoside values match the owner. This model filing is independent of the
    imported NRPS/PKS/OTHER cluster classes and does not establish product-to-locus
    specificity.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: R029-CYANO
  kind: record_content
  reference: data/raw/cyanometdb_occurrences.tsv
  locator: Complete exact-key Cylindrospermopsin row and emitted occurrence 11
  accessed_at: '2026-10-21T09:16:35.750000Z'
  support: supports
  summary: The source row carries the epimer full key, parent name Cylindrospermopsin,
    NCBITaxon:77022, DOI:10.1021/ja00046a067, strain n.a. and nmr_used=yes. The owner
    emits structure confirmed by yes. Exact modern congener applicability is separately
    adjudicated against primary sources; the Boolean NMR-use flag itself does not
    assert full structure confirmation.
  snapshot_sha256: f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8
- evidence_id: R029-CYANO-EXTRACT
  kind: record_content
  reference: scripts/extract_cyanometdb.py
  locator: Source-column mapping for NMR_used into nmr_used
  accessed_at: '2026-10-21T09:16:35.750000Z'
  support: context_only
  summary: The extractor transfers the source NMR_used text as a method-use field.
    It does not reinterpret yes as an analytical technique name or an absolute-stereochemistry
    verdict.
  snapshot_sha256: cccfc32d65a5df99c768bf5055f7ea56ac9678b7029b9dd23483295603ec365e
- evidence_id: R029-CYANO-SEED
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: CyanoMetDB occurrence evidence-note assembly, lines 1225–1235
  accessed_at: '2026-10-21T09:16:35.750000Z'
  support: context_only
  summary: The emitter interpolates nmr_used after structure confirmed by, producing
    the overbroad and ungrammatical owner note. This is a shared generator defect,
    distinct from whether this particular original source refers to parent or epimer.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
assessments:
- assessment_id: ID029-A-OWNER
  area: identity
  topic: Legitimate epimer owner and exact external cross-reference
  outcome: supported
  summary: CHEBI:88049, its six-centre structure and PubChem 115005 are internally
    consistent. Retain this exact epimer identity while separating any parent-only
    source claims; replacing the entire owner with the parent would discard independent
    epimer origin evidence.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - ID029-CHEBI-EPI
  - ID029-EPI-MOL
  - ID029-PUBCHEM
  - ID029-COMPARISON
- assessment_id: ID029-A-MIBIG
  area: consistency
  topic: Persistent upstream parent-name and epimer-structure mismatch
  outcome: concern
  summary: All four MIBiG compound concepts use the parent name with the epimer structure
    and historical parent-pathway citations. This mismatch is confirmed at the current
    source level. The primary reviewer must determine which producer and locus claims
    require transfer, withdrawal or separate congener support; shared connectivity
    and locus names do not settle that decision.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - ID029-MIBIG-0978
  - ID029-MIBIG-0979
  - ID029-MIBIG-0980
  - ID029-MIBIG-0981
  - ID029-CHEBI-EPI
  - ID029-CHEBI-PARENT
  - ID029-GENBANK
  - ID029-COMPARISON
- assessment_id: ID029-A-PARENT
  area: grounding
  topic: Parent candidates and representation ambiguity
  outcome: concern
  summary: Neutral parent CHEBI:88046 is a verified three-star exact parent stereostructure
    candidate. Parent zwitterion CHEBI:88044 is separately maintained and shares its
    Standard InChIKey, so selecting a target requires explicit representation adjudication.
    Neither identifier is equivalent to the current 7-epi owner.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - ID029-CHEBI-SEARCH
  - ID029-CHEBI-PARENT
  - ID029-PARENT-MOL
  - ID029-PARENT-ZWITTERION
  - ID029-PARENT-ZWITTERION-MOL
  - ID029-COMPARISON
- assessment_id: ID029-A-TAXA
  area: nomenclature
  topic: Current taxonomic labels and original strain bridges
  outcome: supported
  summary: Umezakia, Aphanizomenon and Chrysosporum ovalisporum labels refer to the
    same current taxon 75695. The AWT205, 10E9, 22D11 and 10E6 GenBank strain qualifiers
    match their specific source concepts. The 10E6 deposit explicitly provides NIVA:CYA
    626; no accession is inferred for the other cultures.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - ID029-TAXONOMY
  - ID029-GENBANK
- assessment_id: ID029-A-OWNERSHIP
  area: ownership
  topic: Collective correction constraints and preservation of the epimer
  outcome: concern
  summary: 'The current loader cannot represent migrating these four rows to one parent
    key using four ordinary structure corrections: duplicate parent ChEBI keys, repeated
    correction targets and loss of the last old-key MIBiG owner violate explicit guards.
    Any justified collective correction needs a tested maintained extension or migration
    that selects representation, pins all source and target rows, preserves the independent
    epimer owner, withholds stale xrefs, and leaves other inventories joined only
    to scientifically appropriate exact structures.'
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - ID029-CORRECTION-GUARDS
  - ID029-LOCAL-SEARCH
  - ID029-COMPARISON
  - ID029-CHEBI-PARENT
  - ID029-PARENT-ZWITTERION
- assessment_id: A029-OCC-00
  area: evidence
  topic: 'occurrences[0]: LOTUS Oscillatoria DOI'
  outcome: supported
  summary: Exact epi detected against standards in axenic Oscillatoria cultures; genus
    rank is broad but not an assertion that every member produces it.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-OSC-PRIMARY
  - E029-OSC-ABSTRACT
- assessment_id: A029-OCC-01
  area: evidence
  topic: 'occurrences[1]: ChEBI Oscillatoria PCC6506 PMID'
  outcome: supported
  summary: Same primary experiment as occurrence 0; strain context PCC6506 is explicit
    and exact epi is chromatographically distinguished from parent.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-OSC-PRIMARY
  - E029-OSC-ABSTRACT
- assessment_id: A029-OCC-02
  area: evidence
  topic: 'occurrences[2]: LOTUS Aphanizomenon 2010 genus claim'
  outcome: unknown
  summary: The abstract covers parent-CYN study strains, while the reference list
    includes original ovalisporum epi isolation. Full-body citation context remains
    unavailable; do not exclude this genus occurrence solely from the abstract.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-APH-BGC
  - E029-APH-REFS
  - E029-BANKER
- assessment_id: A029-OCC-03
  area: evidence
  topic: 'occurrences[3]: LOTUS Umezakia 1994 claim'
  outcome: unknown
  summary: Inspected primary abstract concerns parent cylindrospermopsin. Exact epi
    occurrence is provisionally questionable, but unavailable full methods prevent
    a definitive whole-article absence finding.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-1994-UMEZAKIA
  - E029-2005-ORIGIN
- assessment_id: A029-OCC-04
  area: evidence
  topic: 'occurrences[4]: LOTUS ovalisporum original 2000 isolation'
  outcome: supported
  summary: Exact epi isolation is directly reported by the original primary abstract;
    current taxonomy/synonym equivalence is checked independently.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-BANKER
  - E029-ABSOLUTE
- assessment_id: A029-OCC-05
  area: evidence
  topic: 'occurrences[5]: ChEBI ovalisporum original 2000 isolation'
  outcome: supported
  summary: PMID:10757726 is the same original publication as DOI:10.1021/np990498m;
    it supports this exact occurrence, rather than a second independent culture experiment.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-BANKER
  - E029-ABSOLUTE
- assessment_id: A029-OCC-06
  area: evidence
  topic: 'occurrences[6]: LOTUS C. raciborskii 1994 hepatocyte paper'
  outcome: unknown
  summary: The inspected abstract tests named parent toxin; the exact provenance and
    congener in the inaccessible body remain unverified for modern epi. No activity
    measured for parent is transferred to epi.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-1994-HEPATOCYTE
  - E029-2005-ORIGIN
- assessment_id: A029-OCC-07
  area: evidence
  topic: 'occurrences[7]: LOTUS C. raciborskii 2001 CY-Thai isolation'
  outcome: unknown
  summary: The primary abstract explicitly identifies parent and deoxy-CYN; exact
    epi is not demonstrated by those inspected claims. Full-body availability gap
    remains, so no blanket congener-absence assertion is made.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-2001-THAI
- assessment_id: A029-OCC-08
  area: evidence
  topic: 'occurrences[8]: LOTUS original 1992 parent citation'
  outcome: concern
  summary: Later inspected primary stereochemical revision explicitly maps the original
    1992 material to parent cylindrospermopsin. Routing it to the modern epi owner
    by the old drawing is a confirmed historical-identity mismatch; original 1992
    detailed methods remain unavailable.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-1992
  - E029-REVISION
  - E029-2005-ORIGIN
- assessment_id: A029-OCC-09
  area: evidence
  topic: 'occurrences[9]: LOTUS 2005 synthesis citation at C. raciborskii'
  outcome: concern
  summary: The inspected primary distinguishes C. raciborskii parent isolation from
    natural epi in A. ovalisporum, and uses synthesis for absolute identity. It does
    not support this exact epi/taxon occurrence triple.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-2005-ORIGIN
  - E029-ABSOLUTE
  - E029-2005-SI
- assessment_id: A029-OCC-10
  area: evidence
  topic: 'occurrences[10]: LOTUS 2000 isotope-feeding citation'
  outcome: unknown
  summary: The inspected abstract and complete SI concern named parent precursor incorporation;
    a pre-revision drawing cannot establish modern epi. This remains a provisional
    exact-congener concern pending the main body.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-FEEDING
  - E029-FEEDING-SI
  - E029-REVISION
- assessment_id: A029-OCC-11
  area: evidence
  topic: 'occurrences[11]: CyanoMetDB original 1992 parent citation'
  outcome: concern
  summary: The raw row itself is named Cylindrospermopsin and cites the original parent
    paper. The later primary revision distinguishes that material from modern epi.
    NMR-used=yes does not cure the compound identity conflict; the separate rendering
    assessment addresses the misleading generic NMR-rendering phrase.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-1992
  - E029-REVISION
  - E029-2005-ORIGIN
  - E029-RAW
- assessment_id: A029-BGC-0
  area: evidence
  topic: 'Producer/locus 0: exact 7-epi scope for AWT205'
  outcome: unknown
  summary: The cited study and native accession bridge concern a named parent-CYN
    cluster. Source-level producer assertion and unstated locus grade are faithful
    to imported metadata, but exact-epimer applicability is not resolved by that fidelity.
    Do not upgrade to knockout/heterologous/assay evidence or transfer the row to
    another identity without congener-specific adjudication. This is part of identifier
    finding ID029-F-SOURCE-CONFLATION, not a duplicate finding.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-AWT205
  - E029-CYRI-BOUNDARY
  - E029-OWNER
- assessment_id: A029-BGC-1
  area: evidence
  topic: 'Producer/locus 1: exact 7-epi scope for 10E9'
  outcome: unknown
  summary: The cited study and native accession bridge concern a named parent-CYN
    cluster. Source-level producer assertion and unstated locus grade are faithful
    to imported metadata, but exact-epimer applicability is not resolved by that fidelity.
    Do not upgrade to knockout/heterologous/assay evidence or transfer the row to
    another identity without congener-specific adjudication. This is part of identifier
    finding ID029-F-SOURCE-CONFLATION, not a duplicate finding.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-APH-BGC
  - E029-CYRI-BOUNDARY
  - E029-OWNER
- assessment_id: A029-BGC-2
  area: evidence
  topic: 'Producer/locus 2: exact 7-epi scope for 22D11'
  outcome: unknown
  summary: The cited study and native accession bridge concern a named parent-CYN
    cluster. Source-level producer assertion and unstated locus grade are faithful
    to imported metadata, but exact-epimer applicability is not resolved by that fidelity.
    Do not upgrade to knockout/heterologous/assay evidence or transfer the row to
    another identity without congener-specific adjudication. This is part of identifier
    finding ID029-F-SOURCE-CONFLATION, not a duplicate finding.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-APH-BGC
  - E029-CYRI-BOUNDARY
  - E029-OWNER
- assessment_id: A029-BGC-3
  area: evidence
  topic: 'Producer/locus 3: exact 7-epi scope for 10E6'
  outcome: unknown
  summary: The cited study and native accession bridge concern a named parent-CYN
    cluster. Source-level producer assertion and unstated locus grade are faithful
    to imported metadata, but exact-epimer applicability is not resolved by that fidelity.
    Do not upgrade to knockout/heterologous/assay evidence or transfer the row to
    another identity without congener-specific adjudication. This is part of identifier
    finding ID029-F-SOURCE-CONFLATION, not a duplicate finding.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-APH-BGC
  - E029-CYRI-BOUNDARY
  - E029-OWNER
- assessment_id: A029-ORIGIN
  area: identity
  topic: Natural epimer versus synthetic identity confirmation
  outcome: supported
  summary: Original culture isolation and independent axenic-culture detection support
    natural origin. Later synthesis and sulfation identify the epimer; they do not
    show that natural material was generated during extraction. Exact current stereostructure
    and authority mapping are supplied by the independent identifier packet.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-BANKER
  - E029-OSC-PRIMARY
  - E029-REVISION
  - E029-ABSOLUTE
- assessment_id: A029-COMPLETENESS
  area: completeness
  topic: Mechanism, activity and source-only classification boundaries
  outcome: supported
  summary: The owner does not assert a fully reconstituted pathway, individual enzyme
    mechanism, cytotoxicity value or target. No parent-only toxicity measurement or
    heterologous CyrI homolog result is inserted. Computed filing and existing source
    disagreement discussions are appropriate; the disagreement still requires curation.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-OWNER
  - E029-CLASSIFICATION
  - E029-CYRI-BOUNDARY
- assessment_id: A029-CONTEXT
  area: completeness
  topic: iModulon applicability
  outcome: not_applicable
  summary: No exact organism dataset is available in the inspected structured catalogue;
    no biology-grade or absence inference follows.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - E029-IMODULON
- assessment_id: R029-NMR
  area: evidence
  topic: Source NMR-use field and emitted confirmation wording
  outcome: concern
  summary: A source flag saying NMR was used is rendered as generic structure confirmation.
    The note must preserve its database method-use meaning even after exact parent/epimer
    source adjudication.
  target_ids:
  - CHEBI:88049
  evidence_ids:
  - R029-CYANO
  - R029-CYANO-EXTRACT
  - R029-CYANO-SEED
findings:
- finding_id: ID029-F-SOURCE-CONFLATION
  issue_key: cylindrospermopsin-parent-epimer-source-conflation
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Four parent-named MIBiG concepts carry the distinct 7-epimer structure
  description: BGC0000978:1 through BGC0000981:1 currently and locally name cylindrospermopsin
    but store the exact 7-epi stereostructure. The official parent and epimer molfiles
    differ at one hydroxyl-bearing carbon, R versus S, and have different full keys.
    This is a persistent upstream source identity mismatch, already exposed by the
    owner discussions, rather than a PubChem structure mismatch or an invalid CHEBI:88049
    owner. Primary citation-specific adjudication must decide disposition of each
    linked biological claim before a collective migration.
  target_ids:
  - CHEBI:88049
  field_paths:
  - source_concepts
  - producer_organisms
  - biosynthetic_gene_clusters
  - discussions
  evidence_ids:
  - ID029-CHEBI-EPI
  - ID029-CHEBI-PARENT
  - ID029-PARENT-MOL
  - ID029-MIBIG-0978
  - ID029-MIBIG-0979
  - ID029-MIBIG-0980
  - ID029-MIBIG-0981
  - ID029-COMPARISON
  - E029-AWT205
  - E029-APH-BGC
  - E029-REVISION
  - E029-ABSOLUTE
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Maintained decisions after explicit collective migration support
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Guarded source/target and representation adjudication
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Preserve separate parent and epimer owners and exact-source joins
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Original source assertions preserved unchanged
- finding_id: F029-OCCURRENCE-EPIMER
  issue_key: 7-epi-cylindrospermopsin-parent-occurrence-citation-routing
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Parent-isolation and synthesis citations are routed to epimer occurrences
  description: The 1992 LOTUS/CyanoMetDB origin claims and 2005 LOTUS C. raciborskii
    claim conflate historical parent material with the modern 7-epi identity. The
    inspected 2002/2005 primary stereochemical revision identifies the old parent
    drawing error and explicitly distinguishes parent C. raciborskii isolation from
    natural epi in A. ovalisporum. Other parent-focused occurrence citations have
    incomplete full-text coverage and remain provisional concerns, not additional
    confirmed wrong triples. This finding does not assert that C. raciborskii can
    never produce epi.
  target_ids:
  - CHEBI:88049
  field_paths:
  - occurrences[8]
  - occurrences[9]
  - occurrences[11]
  evidence_ids:
  - E029-RAW
  - E029-1992
  - E029-REVISION
  - E029-2005-ORIGIN
  - E029-ABSOLUTE
  - E029-LOTUS-LOADER
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: reviewed exact occurrence decisions after guard extension
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/lotus_exclusions.py
    role: row-set drift guard for duplicate-label source tuples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: preserved original assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: preserved original parent-named isolation assertion
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_cyanometdb.py
    role: maintained chemical-identity harmonization
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: occurrence emission and provenance retention
  rule_id: 'review-yaml-record Evidence Rules: exact chemical identity and narrow
    citation scope'
  native_severity: 'major: parent/epimer evidence conflation in exact occurrence claims'
  normalization_reason: The confirmed historical-identity routing error is reported
    once across the three rendered occurrences; unresolved full-text questions remain
    assessments. The four MIBiG source concept conflicts have a separate identifier
    finding.
- finding_id: R029-NMR-WORDING
  issue_key: cyanometdb-nmr-used-rendered-as-structure-confirmed
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The NMR-use flag is rendered as full structure confirmation
  description: The exact source row says nmr_used=yes; the generated occurrence says
    structure confirmed by yes. This both loses the method-use meaning and overstates
    what the database flag establishes. Parent-versus-epimer applicability is a separate
    source-scoping problem, and correcting it does not fix the shared note emitter.
  target_ids:
  - CHEBI:88049
  field_paths:
  - occurrences[11].evidence[0].notes
  evidence_ids:
  - R029-CYANO
  - R029-CYANO-EXTRACT
  - R029-CYANO-SEED
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: CyanoMetDB method-use note emitter
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: Unchanged source NMR-use metadata
actions:
- action_id: R029-ADJUDICATE-PARENT-SOURCES
  description: 'Adjudicate each parent-named MIBiG source against its exact strain/congener
    experiment before moving biological claims. Preserve the legitimate CHEBI:88049
    epimer owner, its exact PubChem115005 xref and independently supported epimer
    origins. If the original concept is parent cylindrospermopsin, correct that source
    graph through an explicit tested collective migration; if direct epimer evidence
    instead supports its graph, reconcile the source label and retain the precise
    evidence. Do not select disposition from the name alone. Pin every participating
    complete raw row: BGC0000978:1=c886c76a437042cb87aa4eacc38bd12341d069d4b7d8606ee31180c3f4e59c3a;
    BGC0000979:1=cec492bc57a16dd650d5058151a0e1967292376bb4d502c38c7f07090d5d67f0;
    BGC0000980:1=0fe1abb1cbee91e257aa138620f7e8c09caa40669a3896f25cf3d50ed73af1a4;
    BGC0000981:1=bdcbfd395b761adacb964fa26b74460a53ac62a49874b7faea1643946644d70e.
    Pin the exact neutral/zwitterionic parent and epimer ChEBI rows: CHEBI:88044=6002daba769f405d3ca3f74c115824362d1cb6c8be87c78ab7dd9c52419d790c;
    CHEBI:88046=61c0b6ce91a67712286e51ff0ab414fa8c0e84dfd5f41452eb6f6539b1252d60;
    CHEBI:88049=6467623ad7cb8d611d3e93b341648df63a9c2c81f1dd9a34a210e282f0726deb.
    The existing loader cannot perform four ordinary corrections because both parent
    ontology entries share a Standard key, repeated target keys are forbidden, and
    a shared-key split must leave a MIBiG owner at the old key. Extend the maintained
    correction/generation path to select the intended representation explicitly and
    preserve the epimer population even if all four MIBiG concepts move. Preserve
    upstream assertions and per-claim adjudication in generated discussions; do not
    patch the generated owner or mutate the raw inventories.'
  finding_ids:
  - ID029-F-SOURCE-CONFLATION
  target_ids:
  - CHEBI:88049
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Maintained decisions after explicit collective migration support
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Guarded source/target and representation adjudication
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Preserve separate parent and epimer owners and exact-source joins
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Original source assertions preserved unchanged
  generator: scripts/seed_from_sources.py with explicit guarded collective migration
    and representation selection
  acceptance_checks:
  - Each source concept has an exact primary locator distinguishing the named parent,
    the 7-epimer and the experimental strain. Unavailable exact-congener evidence
    remains explicitly unresolved rather than being upgraded or silently transferred.
  - Require all raw source and target-row digests, unique consumption and explicit
    neutral-versus-zwitterionic representation; stale, incomplete, repeated or conflicting
    decisions fail. Do not equate CHEBI:88044 and CHEBI:88046 merely because their
    Standard keys match.
  - A canary regenerates separate scientifically supported parent and epimer identities.
    CHEBI:88049, its six assigned centres, PubChem115005 and independently supported
    ovalisporum/PCC6506 epimer evidence survive even if no old-key MIBiG row remains.
  - Source-owned xrefs are rechecked for each destination; PubChem115005 cannot follow
    a parent correction. Existing LOTUS, ChEBI-origin and CyanoMetDB rows are joined
    or withheld only after their own exact-structure adjudication, without blanket
    movement of old-key occurrences.
  - Exercise mixed and all-four migrations, representation collisions, owner preservation,
    exact-key lookup/PATHS changes, retained source discussions and referenced-record
    resolution. Structure-corrected rows currently cannot compose with claim-reference
    and producer-strain/isolate overlays; explicitly test any required extension rather
    than merely refreshing their hashes.
  - Run focused migration/composition tests, strict target validation, source reproduction
    and required repository QC. Preserve source-method grades conservatively until
    claim-specific primary evidence warrants a change.
- action_id: ACT029-OCCURRENCE-EPIMER
  description: 'Adjudicate the two confirmed LOTUS 77022 DOI tuples and the parent-named
    CyanoMetDB 1992 row using the primary stereochemical revision. Preserve the original
    raw rows. Before any LOTUS exclusion, extend and test the unique-row loader to
    accept an explicitly reviewed complete row set or exact immutable raw-row selectors;
    each tuple currently has two raw rows. For exact key LHJPHMKIGRLKDR-YUQKHPEDSA-N
    and taxon NCBITaxon:77022, pin these complete raw rows: 10.1021/JA00046A067 /
    Cylindrospermopsis raciborskii / Q5199329 = 3e016b050fa088ae0a6522f719e2c2ca621f0fd23448733f3796547e07a4d89b;
    10.1021/JA00046A067 / Raphidiopsis raciborskii / Q67338126 = d5a59afe8f7fc4e83e8311331daa6262b3b2b3bfaf1b0aa0414a2e5d31f5de53;
    10.1021/JO0486387 / Cylindrospermopsis raciborskii / Q5199329 = 13e53a6f7a024f553096318b9a79b2d8b255606df5f3773795f2f979ecf240d8;
    10.1021/JO0486387 / Raphidiopsis raciborskii / Q67338126 = f5d769f27d7bb4806800f017e5d02a791d95318386f5a6d1114fbeab78b99353.
    Reject added, removed or changed members. Then withhold the confirmed wrong epi
    occurrences with auditable source discussions, or reroute only through an explicitly
    reviewed identity-aware mechanism. Implement and test an explicitly consumed CyanoMetDB
    identity/occurrence decision path before emission, pinned to complete raw-row
    SHA256 1fdaecc81ca115f57542f6f5ecc4f7e28062284477929d562ac72df5040055ea; the present
    emitter has no such adjudication hook. Preserve its original assertion and the
    primary revision rationale in a discussion. Resolve parent-versus-epimer routing
    before regeneration; do not hand-edit the emitted occurrence or use NMR-used as
    identity proof. Leave the five unresolved occurrence claims unchanged pending
    their missing primary-body context, and retain all four positively supported epi
    occurrences.'
  finding_ids:
  - F029-OCCURRENCE-EPIMER
  target_ids:
  - CHEBI:88049
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: reviewed exact occurrence decisions after guard extension
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/lotus_exclusions.py
    role: row-set drift guard for duplicate-label source tuples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: preserved original assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: preserved original parent-named isolation assertion
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_cyanometdb.py
    role: maintained chemical-identity harmonization
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: occurrence emission and provenance retention
  generator: Tested LOTUS exclusion guard extension plus maintained CyanoMetDB identity
    harmonization and seed regeneration; no direct raw-source or owner edit
  acceptance_checks:
  - Both duplicate-label raw rows per confirmed LOTUS tuple are pinned, and every
    source row-set change fails closed.
  - The new CyanoMetDB decision is consumed exactly once and rejects stale complete-row
    hashes, duplicate or unmatched decisions and reintroduction of the excluded assertion;
    a changed parent destination never silently transfers unrelated epimer origins.
  - The 1992 parent material and 2005 synthesis context no longer appear as unqualified
    exact epi/C. raciborskii occurrences.
  - All four supported A. ovalisporum/Oscillatoria occurrences survive, and unresolved
    citations are not silently deleted.
  - The epi owner and its ChEBI identity survive any separate MIBiG source migration;
    neutral parent and zwitterionic parent collisions are explicitly adjudicated by
    the separate identity action.
  - Targeted seed canary, strict validation, source provenance and required reproduction/QC
    checks pass.
- action_id: R029-CORRECT-NMR-NOTE
  description: 'Change the maintained CyanoMetDB note emitter to preserve NMR usage
    as source metadata, for example NMR used according to CyanoMetDB: yes. Keep DATABASE_ASSERTION
    and the original flag; do not infer complete or absolute structure confirmation.
    Coordinate this wording fix with the separate exact-congener occurrence adjudication.'
  finding_ids:
  - R029-NMR-WORDING
  target_ids:
  - CHEBI:88049
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: CyanoMetDB method-use note emitter
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: Unchanged source NMR-use metadata
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Yes, no and missing NMR-use values have accurate wording without a generic structure-confirmed
    claim.
  - Raw source flags, references and taxon/strain context are preserved; only independently
    adjudicated exact-congener decisions alter occurrence membership.
  - Seed canary, strict validation and reproduction/QC pass; the fix remains in the
    maintained emitter rather than a generated YAML patch.
limitations:
- GenBank headers, bibliographic references and source qualifiers were inspected for
  all four deposits. No complete CDS translation or congener-specific biosynthetic
  function was inferred from those sequence records.
- Versioned MIBiG endpoints were retrieved for the four versions used by this owner.
  Their empty evidence arrays describe those database assertions, not proof that the
  cited literature lacks experiments.
- The ChEBI search is limited to its complete seven-result name query. The current
  parent representation collision is demonstrated by both official molfiles and raw
  rows, rather than inferred from names.
- This scientific section is intentionally partial because several required primary
  bodies remain unavailable. Abstract-level positive observations are retained without
  turning missing full text into evidence of absence.
- AWT205 Methods/Table 1/Table 2 and selected original 2010 Oscillatoria Methods/Results
  were inspected through official publisher text; figure pixels and unreturned body
  portions were not read. No complete-body claim is made for those sources.
- The original 2000 epi-isolation abstract directly supports occurrence, but detailed
  workup controls were not inspected. No inference of extraction-induced epimerization
  or synthetic origin is justified.
- The 2005 absolute-configuration and historical-origin passages were inspected through
  a public primary-paper mirror and official SI; the publisher main PDF was inaccessible.
- The 2010 Aphanizomenon genus occurrence is unresolved because its original body
  could contain a relevant ovalisporum literature statement. Its reference list alone
  is not treated as proof of that statement or proof of absence.
- The 1994 Umezakia, 1994 hepatocyte, 2001 CY-Thai and 2000 feeding exact-epi associations
  remain provisional concerns. They are not included in the confirmed occurrence-removal
  recommendation.
- Later CyrI studies on Oscillatoria proteins do not independently validate the four
  stored AWT205/Aphanizomenon exact-epi locus claims. No native knockout, exact-congener
  absence or universal species incapacity is inferred.
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
- Baseline reuse concerns the identical committed inputs and original executed checks;
  it does not claim a fresh network/governance or ontology-cache refresh.
notes:
- No scientific owner, inventory, curation table, native status or history was edited.
  Actions are proposed work.
- Baseline gates retain their actual original receipts after byte-for-byte input verification;
  target strict validation ran afresh. Scientific failed or unavailable checks are
  distinct from bundle validation.
tags:
- path-order-campaign
- batch-003
- parent-epimer-conflation
- occurrence-citation-scope
- guarded-migration-required
```
