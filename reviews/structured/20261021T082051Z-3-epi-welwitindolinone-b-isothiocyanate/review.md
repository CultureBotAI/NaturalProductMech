# 3-epi-welwitindolinone B: disputed N-substitution and claim-specific evidence

- Review: 20261021T082051Z-3-epi-welwitindolinone-b-isothiocyanate
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T07:59:49.451341Z
- Finished UTC: 2026-10-21T08:20:51.920530Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

A primary drawing assigns the named congener an N–H group, conflicting with the N-methyl graph shared by the owner and databases. Identity correction remains provisional pending original isolation evidence. The locus claim has confirmed citation-routing and method-scope defects; two 1987 occurrence citations remain unresolved, and CyanoMetDB NMR wording overstates a usage flag.

## Scope And Provenance

One complete owner, exact chemical identity and stereochemistry, all xrefs and occurrence citations, producer/locus scope, current grounding, classification and history.

Selection: Sixteenth initially unreviewed path, sixth in batch 002 from fresh origin/main. Review starts and saves follow path order. The fresh-main authoritative list has 91 valid bundles covering 54 of 3,116 records; ten pending PR 1000 targets are additional campaign coverage. Ignored files were included. This bundle reviews one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-1439bab61e | data/natural_products/alkaloids/3-epi-welwitindolinone-b-isothiocyanate.yaml | generated | 3-epi-welwitindolinone B isothiocyanate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-1439bab61e | The entire owner validates with zero ERROR rows. This does not settle scientific identity. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-1439bab61e | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-1439bab61e | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-1439bab61e | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-1439bab61e | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate after environment repair | passed | True | naturalproductmech:mibig-1439bab61e | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Encoded graph and current authority agreement | passed | True | naturalproductmech:mibig-1439bab61e | The full encoded N-methyl structure, formula and five centres reproduce the stored InChI/key and current database records. This is internal/source consistency only. |
| Original exact named congener identity | unavailable | True | naturalproductmech:mibig-1439bab61e | A later primary drawing names an N–H congener while current databases encode N-methyl. Original1994 drawing and complete absolute stereochemical argument remain unavailable; neither a final replacement nor exact natural-origin sign-off is established. |
| Exact target/taxon scope in both1987 occurrence citations | unavailable | True | naturalproductmech:mibig-1439bab61e | Official titles concern H. fontinalis; full article bodies are unavailable. The imported H. welwitschii triples require direct adjudication and are not excluded from titles alone. |
| Claim-specific reference and demonstrated-product scope | failed | True | naturalproductmech:mibig-1439bab61e | The generated sole locus reference is compound NMR metadata. Inspected pathway experiments concern precursors and C congeners, so those results cannot supply exact 3-epi-B demonstration. Reference routing needs correction and target-specific method adjudication. |
| Native expression-source applicability | not_applicable | False | naturalproductmech:mibig-1439bab61e | The complete returned catalogue has no native Hapalosiphon dataset. |

## Scientific And Domain Assessments

### Name-to-structure and N-substitution

identity: concern. Targets: naturalproductmech:mibig-1439bab61e.

The encoded graph is internally coherent and consistently reproduced by linked databases, but a primary drawing explicitly assigns the name to an N–H congener. Database consensus cannot settle this identity conflict. The computed demethylated candidate is a lead, not an approved replacement.

### C3 epimer and absolute stereochemical scope

identity: unknown. Targets: naturalproductmech:mibig-1439bab61e.

All five centres are encoded, so stereo_complete=true accurately describes the representation. The later primary note corroborates C3S; the original abstract only promises relative configurations for minor congeners. Complete primary absolute stereochemical confirmation remains unavailable and the N-substitution conflict must be resolved first.

### Exact database graph equivalence

identity: supported. Targets: naturalproductmech:mibig-1439bab61e.

NPA019701 and CyanoMetDB 1513 carry the same exact current graph/key. This structural equivalence does not certify the label’s natural-product identity. CyanoMetDB’s alternative epimer CID and synonym are correctly not copied into owner xrefs.

### Current minted identifier and ChEBI eligibility

grounding: supported. Targets: naturalproductmech:mibig-1439bab61e.

For the currently encoded graph the exact live ChEBI match is only two-star 216541, consistent with MINTED under the project rule. Regrounding and minted identity migration must be reassessed if chemical identity changes.

### 1994 LOTUS/CyanoMetDB occurrence and exact isolation

evidence: unknown. Targets: naturalproductmech:mibig-1439bab61e.

The databases explicitly retain the 1994 H. welwitschii/UHIC-52-3 attribution. The inspected original abstract supports the family and culture, but not the exact named congener’s N-substitution or complete structure. Thus source import is verified while the individual cited occurrence remains unverified.

### Two separate 1987 LOTUS citations

evidence: concern. Targets: naturalproductmech:mibig-1439bab61e.

Both official DOI records describe H. fontinalis alkaloids, whereas the retained triples assert the current exact graph in H. welwitschii. Their applicability needs primary-body adjudication. No exclusion is justified solely by article titles, nor may positive 1994 family evidence validate these separate citations.

### Species, strain and cyanobacterial grouping

grounding: supported. Targets: naturalproductmech:mibig-1439bab61e.

All NCBI IDs and the Wikidata species URI resolve consistently. The UHIC-52-3 occurrence string remains distinct from UTEX B1830 producer/locus context; grouping as CYANOBACTERIAL is appropriate.

### CyanoMetDB method flag wording

evidence: concern. Targets: naturalproductmech:mibig-1439bab61e.

NMR_used=yes is faithfully imported but rendered as “structure confirmed by yes”. The wording promotes a method-usage flag into a generic confirmation statement, especially misleading while exact identity remains disputed.

### Computed filing versus source cluster classes

scope: supported. Targets: naturalproductmech:mibig-1439bab61e.

ALKALOIDS follows the pinned NPClassifier Alkaloids result for the current graph, retaining tool/version and empty lower classes. TERPENE and OTHER preserve MIBiG BGC-class assertions on a separate axis. Neither result is primary evidence that this exact encoded structure was isolated.

### Natural-product admission and exact graph

evidence: unknown. Targets: naturalproductmech:mibig-1439bab61e.

The named welwitindolinone is a reported natural-product lead and the source asserts natural origin. The disputed N-methyl graph must be reconciled before treating the present exact structure’s occurrence or biosynthetic origin as independently verified.

### Mechanism, activity, quantities, datasets and clinical fields

completeness: not_applicable. Targets: naturalproductmech:mibig-1439bab61e.

The complete owner has no optional mechanism graphs, pathway steps, activity measurements or summary, targets, datasets, clinical status or related-record assertions to audit. These absences alone are not findings. The complete returned iModulonDB catalogue has no Hapalosiphon dataset.

### Source concept, SEEDED status and audit trail

provenance: supported. Targets: naturalproductmech:mibig-1439bab61e.

The source concept remains versioned MIBiG BGC0000668 and the two explicit seed events describe inventory imports. SEEDED accurately avoids scientific sign-off; this review does not promote status or rewrite history. Native checks are documented separately from scientific evidence.

### Exact MIBiG compound, locus and strain metadata

grounding: supported. Targets: naturalproductmech:mibig-1439bab61e.

Compound 11 agrees with the owner as a current database graph and label. This source consistency does not independently settle the historical name-to-structure identity, which is under separate review for a possible N–H versus N-methyl conflict. The genome accession is the stated UTEX B1830 strain, and source class/unspecified coordinates are faithfully represented. Native producer SOURCE_ASSERTION remains separate from locus methods.

### Claim-specific citation and exact-congener demonstration

evidence: concern. Targets: naturalproductmech:mibig-1439bab61e.

The sole claim DOI is imported from compound NMR metadata, while the actual source pathway references are omitted. Inspected primary experiments demonstrate precursors and a different welwitindolinone, leaving exact 3-epi-B demonstration unsubstantiated by those results. The citation-routing defect is confirmed; all-literature absence is not asserted.

### Native producer scope and culture status

evidence: supported. Targets: naturalproductmech:mibig-1439bab61e.

Retaining SOURCE_ASSERTION is appropriate. Xenic UTEX B1830 metabolite/genome association and recombinant pathway enzymology are not an axenic native knockout or exact-target sufficiency experiment. Species-level historical isolation and IC-52-3 material must remain distinct from this strain-specific claim.

## Findings

### S016-F-IDENTITY: Named 3-epi-B conflicts with the encoded N-methyl graph

blocker / open / provisional; issue key: mibig-bgc0000668-compound11-n-substitution.

The inspected later-primary Figure 1 assigns the name to an N–H structure, whereas the owner and current source databases encode N-methyl. The conflict is observed directly; the correct final graph remains provisional because the original 1994 drawing is unavailable. Resolve this before chemical identity sign-off or transferring source assertions to a replacement graph.

### S016-F-1987: Two 1987 occurrence citations need exact taxon and congener verification

major / open / provisional; issue key: lotus-3-epi-welwitindolinone-b-1987-citation-scope.

The metadata for DOI 10.1021/JO00226A009 and 10.1021/JO00382A012 names H. fontinalis studies, conflicting with the imported H. welwitschii occurrence context. The full bodies were not available, so exact article coverage is unknown. Keep this citation-specific concern separate from 1994 isolation and from the locus routing defect.

### S016-F-NMR: NMR-used flag is rendered as generic structure confirmation

minor / open / confirmed; issue key: cyanometdb-nmr-used-rendered-as-structure-confirmed.

The source says NMR_used=yes. The emitter produces “structure confirmed by yes”, an ungrammatical and overbroad claim that does not express the method flag’s actual scope.

### bgc016-claim-scope: Exact 3-epi-B locus claim reuses compound NMR citation and entry-wide methods

major / open / confirmed; issue key: mibig-bgc0000668-compound11-link-evidence.

The BGC0000668:11 producer and demonstrated-locus fields both cite only DOI 10.1021/jo00226a009, selected from compound NMR metadata. The primary pathway papers cited by MIBiG are omitted. Their inspected experiments establish precursor chemistry and other congeners, including WelM formation of N-methylwelwitindolinone C isothiocyanate, without a reported exact 3-epi-B product demonstration in the inspected material. Route references by claim and adjudicate the inherited methods specifically for this target. The 1987 body and exact 2014 supplementary target panel were not inspected; the finding does not assert those articles lack every mention or that no later exact study exists.

## Recommended Actions And Acceptance Checks

### S016-A-IDENTITY

Adjudicate the original 1994 named congener against Figure 1 compound 4 and its N-substitution, formula and all stereocentres. If N–H is confirmed, pin BGC0000668:11 source SHA 898e4cc1c18baee06f71050e4213d7898482e8fd806306a433335106004e3266 and implement the correction through maintained inputs. The existing loader requires an eligible three-star ChEBI target; otherwise extend and test it for a fully pinned manual structure rather than fabricating a supported action. Preserve old-key provenance and audit identity migration, xrefs, occurrences, classifier output and locus applicability by exact new key. Do not automatically promote the computed VLJMTNLRJHJRGI-GLTYWKJESA-N candidate or transfer old-key claims. The current claim-reference loader rejects a row carrying structure_correction_note; producer strain/isolate qualifiers also reject that state. Stage identity adjudication before re-adjudicating claim scope. If both corrections are needed together, implement and test compatible guarded composition rather than assuming that refreshed pins alone make the existing overlays composable.

- Primary drawing, name, N-substitution, formula and full stereo mapping are explicitly reconciled; uncertainty is retained if unresolved.
- Source-row drift rejects the correction; a new manual mode has tested pins, chemistry validation and collision handling.
- Changed connectivity receives an explicit identity migration; old-key xrefs/occurrences are not silently equated.
- Target seed canary, strict validation, reproduction verification, corpus verification and required QC pass.
- A changed-structure row cannot bypass current claim/strain/isolate conflict guards. Any combined correction has explicit new-identity evidence, source pins, tested composition and refusal on drift.

### S016-A-1987

Inspect the two original 1987 papers for the exact named structure and taxon. If a triple is unsupported, withhold only that full-key/NCBITaxon162986/DOI triple through curation/lotus_occurrence_exclusions.tsv with its canonical source-row SHA. Retain raw provenance and independently adjudicate the 1994 and CyanoMetDB claims. A primary title alone is not enough to exclude.

- Each retained 1987 triple has an exact primary compound/taxon locator.
- Any exclusion pins the complete current source row and leaves other DOI/strain triples intact.
- Seed canary and reproduction verification show only the adjudicated occurrence changes.

### S016-A-NMR

Change the CyanoMetDB note emitter to report the source field as NMR used according to CyanoMetDB: yes (and analogously no/unspecified) while retaining DATABASE_ASSERTION and the original flag. Do not claim full absolute structure confirmation from this metadata.

- Regenerated note accurately states NMR usage and preserves its database provenance.
- Yes/no/missing values have sensible wording; strict and reproduction checks pass.

### bgc016-reconcile-claims

Use curation/mibig_claim_references.tsv for BGC0000668:11 with expected_source_row_sha256 898e4cc1c18baee06f71050e4213d7898482e8fd806306a433335106004e3266 to route the locus association to PMID:24677572 and the native source assertion to the versioned MIBiG record unless exact strain-specific primary production evidence is verified. Preserve the original 1987 compound citation in raw provenance and adjudicate occurrence independently. The inspected precursor/C-congener experiments do not justify exact-target Enzymatic assays or Heterologous expression methods. Qualify or withdraw inapplicable methods through the implemented target-specific override; WITHDRAW must pin version 5, taxon NCBITaxon:1433842, KF811479.1, explicit empty bounds, full key RBPIZRWOMRMEOB-ADDAZVEVSA-N and original methods Enzymatic assays&#124;Heterologous expression. If an exact-product experiment instead justifies replacement methods, pair REPLACE with the SHA-pinned claim-reference row or extend and test loader enforcement; expected_* columns alone currently guard only WITHDRAW. Retain native SOURCE_ASSERTION and explicit xenic-culture limitations. Do not assign a new predicted/correlated grade without its own evidence. The current claim-reference loader rejects a row carrying structure_correction_note; producer strain/isolate qualifiers also reject that state. Stage identity adjudication before re-adjudicating claim scope. If both corrections are needed together, implement and test compatible guarded composition rather than assuming that refreshed pins alone make the existing overlays composable.

- A reviewer can identify the exact product, enzyme/locus, strain and experiment for every retained demonstrated method; precursor/C-congener assays remain scoped to their actual products.
- The sole locus reference is no longer a compound NMR citation; raw provenance retains the original citation and its COMPOUND_EVIDENCE basis.
- Changing any source-row field invalidates the paired SHA-pinned correction. WITHDRAW verifies all explicit context including empty bounds; a REPLACE action is not described as guarded by unenforced expected_* fields.
- Run the target seed canary, inspect generated claim grades/citations and qualification notes, then strict validation, reproduction verification, corpus verification and required QC.
- A changed-structure row cannot bypass current claim/strain/isolate conflict guards. Any combined correction has explicit new-identity evidence, source pins, tested composition and refusal on drift.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| S016-OWNER | data/natural_products/alkaloids/3-epi-welwitindolinone-b-isothiocyanate.yaml; Entire owner and resolved view, all source rows; read 08:00:03Z and reread 08:06Z | supports | One SEEDED MIBiG-derived owner with five assigned centres, two chemical xrefs, four species-level database occurrences, one strain-level SOURCE_ASSERTION producer and one demonstrated locus. No inline or referenced graph, pathway steps, bioactivities, molecular targets, clinical assertions or cross-corpus links are present in this owner. |
| S016-RAW | data/raw/mibig_compounds.tsv; data/raw/lotus_occurrences.tsv; data/raw/cyanometdb_occurrences.tsv; data/raw/npclassifier.tsv; Exact rows extracted in 016/local-sources.json; pinned source hashes are in inspection.json | supports | MIBiG BGC0000668:11 and all joined chemical rows carry RBPIZRWOMRMEOB-ADDAZVEVSA-N. LOTUS retains three separate DOI triples. CyanoMetDB contributes the 1994 DOI, UHIC-52-3 strain string and nmr_used=yes. NPClassifier contributes Alkaloids, empty superclass/class and no glycoside. This verifies import fidelity, not independent natural-product identity. |
| S016-NPA | https://www.npatlas.org/api/v1/compound/NPA019701?include=classifications; NPA019701 current structure v1, origin_reference, origin_organism, npclassifier | supports | NPA019701 resolves to the owner full InChI/key and N-methyl C22H23ClN2O2S graph. Its original label matches, but its origin reference is DOI 10.1021/jo00226a009, the 1987 fontonamide paper. No structure reassignment is listed. Database agreement does not adjudicate the later-primary N–H conflict. |
| S016-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/216541/; CHEBI:216541 stars, default_structure 3412621, chemical_data and origins | supports | CHEBI:216541 is two-star and its default N-methyl graph has the exact owner full InChI/key and formula. It is therefore ineligible for the repository three-star grounding rule. Its origin citation repeats the 1987 DOI, so it is not independent evidence for the named natural structure. |
| S016-CHEBI-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/216541/; Official default molfile; independently parsed with RDKit | supports | The default molfile produces RBPIZRWOMRMEOB-ADDAZVEVSA-N and the same full InChI as the owner; all five encoded centres agree. |
| S016-CHEBI-SEARCH | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=RBPIZRWOMRMEOB-ADDAZVEVSA-N&amp;size=100; Exact full InChIKey search, returned one entry | supports | The official search returned only two-star CHEBI:216541 for the current full key. This bounded result supports retaining a minted identifier for the encoded graph, pending identity adjudication. |
| S016-PUBCHEM | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/RBPIZRWOMRMEOB-ADDAZVEVSA-N/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; PUG REST full-key property response, CID 139588580 | supports | CID 139588580 has the exact current full key, InChI and C22H23ClN2O2S formula. This is a current structural cross-check, not a primary isolation or stereochemical determination. |
| S016-PARENT-EPIMER | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/101959988/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; PUG REST properties for CID 101959988, supplied as second CID in original CyanoMetDB row | context_only | CID 101959988 instead has RBPIZRWOMRMEOB-AGRNFKIVSA-N, differing at the oxindole C3 stereocentre. It is not an exact xref for this owner. The source alias N-Methylwelwitindolinone B and this second CID must not be imported as equivalent without resolving the chemical conflict. |
| S016-CYANO | https://zenodo.org/records/13854577/files/CyanoMetDB_V03_2024.csv?download=1; Original v03 row CyanoMetDB_1513, re-extracted from inspected 002/cyanometdb-v03.csv at08:02Z | partial | The row names 3-epi-welwitindolinone B, encodes the current N-methyl graph, cites DOI 10.1021/ja00101a015 and reports H. welwitschii UHIC-52-3 with NMR_used=yes. Its alternate name and secondary CID point to N-methylwelwitindolinone B, a distinct epimer in PubChem. NMR_used is a usage flag, not proof that every structural detail is confirmed. |
| S016-TAXA | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=162986,1433842,1524913&amp;retmode=xml; NCBI Taxonomy 162986,1433842,1524913 names, ranks and lineage | supports | 162986 is Hapalosiphon welwitschii; 1433842 is strain UTEX B1830 and 1524913 is strain UHIC-52-3. Both strains descend from that species in the cyanobacterial lineage. They are distinct strain taxa; the original isolation strain cannot be silently equated to the sequenced UTEX strain. |
| S016-WIKIDATA | https://www.wikidata.org/wiki/Special:EntityData/Q67340456.json; entity Q67340456 revision 2543823250, label/en and claims P225/P685 | supports | Reinspection of the previously fetched entity confirms Q67340456 identifies Hapalosiphon welwitschii and NCBI 162986, matching this owner’s three LOTUS provenance URIs. Original retrieval time is retained. |
| S016-1994-ABSTRACT | https://pure.psu.edu/en/publications/welwitindolinones-unusual-alkaloids-from-the-blue-green-algae-hap/; Author institutional abstract of Stratmann et al.1994, DOI 10.1021/ja00101a015 | partial | The abstract reports welwitindolinones and minor alkaloids from H. welwitschii UHIC-52-3, with gross structures and relative configurations for compounds 1–6 and 8–15. X-ray absolute configuration is stated only for major compound 7. It does not enumerate the exact 3-epi target or verify its N-substitution, complete configuration or UTEX occurrence. |
| S016-1987-HAPALINDOLES | https://api.crossref.org/works/10.1021/jo00382a012; Official DOI title, authors, year and journal | partial | DOI 10.1021/jo00382a012 is the 1987 J. Org. Chem. paper Hapalindoles, antibacterial and antimycotic alkaloids from the cyanophyte Hapalosiphon fontinalis,52:1036–1043. This is a citation/taxon warning for the H. welwitschii triple, not proof that the uninspected whole body never discusses the target. |
| S016-2012 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=3368435; PMC3368435 complete body and reference 17; DOI 10.1021/ja210793x, PMID22235963 | partial | Reference 17 explicitly identifies the 3-epi-B isothiocyanate C3 configuration as S, citing the original isolation report. The paper’s actual syntheses concern C congeners; it does not establish all five centres or the target’s N-substitution. The owner atom 4, oxindole C3, is S. |
| S016-2014-DRAWING | https://file1.lookchem.com/doi/2022/3/29/c99d78a2-2dca-4bbc-ac30-bcffd75dfa9b.pdf; Publisher-format author primary paper DOI 10.1021/ol5020043, Figure 1 compound 4 and adjacent prose, pageA; PDF visually inspected08:03:45Z and08:06Z | refutes | Figure 1 draws compound 4 with oxindole N–H, and prose names 4 as 3-epi-welwitindolinone B isothiocyanate. N-methylwelwitindolinone B is separately compound 2. The current owner instead encodes N-methyl. This is an explicit primary-versus-database conflict; the paper studies synthetic progress toward 2, not an original isolation or complete synthesis of 4. |
| S016-2014-REFERENCE | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=25124334&amp;retmode=xml; PMID 25124334 title/authors/DOI | supports | The official PubMed record maps Leah Cleary, Jennifer Pitzen, John A.Brailsford and Kenneth J.Shea’s Progress toward the Total Synthesis of N-Methylwelwitindolinone B Isothiocyanate to DOI 10.1021/ol5020043, matching the inspected publisher-format PDF. |
| S016-CHEMISTRY | /private/tmp/npm-review-work/016/identity-chemistry.json; RDKit2026.03.5 complete owner and authority graph comparison; atom-labelled owner drawing in016/record-stereo-atomlabels.png | supports | Owner SMILES yields its stored full InChI/key, C22H23ClN2O2S, neutral charge and assigned centres 4S,11S,17R,19R,21S (zero-based owner SMILES order). All inspected exact database structures match. The lactam N1 bears methyl atom 0. Removing only that methyl yields a computed N–H candidate C21H21ClN2O2S, key VLJMTNLRJHJRGI-GLTYWKJESA-N; this calculated candidate has not been adjudicated against the original isolation drawing. |
| S016-1994-ACCESS | https://pubs.acs.org/doi/abs/10.1021/ja00101a015?journalCode=jacsat; Bounded original-paper search/access receipts in016/1994-bounded-access-evidence.json | unknown | Focused searches and direct official access did not provide a free original 1994 drawing/body. The publisher returned403; SI routes returned202 with zero bytes and Figshare DOI search returned no result. The institutional abstract is the only inspected original text. No negative scientific inference is made from access failure. |
| S016-OWNERSHIP | src/naturalproductmech/curate/structure_corrections.py; curation/mibig_structure_corrections.tsv; curation/lotus_occurrence_exclusions.tsv; scripts/seed_from_sources.py; src/naturalproductmech/curate/claim_references.py; Full correction-loader functions and exact occurrence-note emitter read08:06Z; target correction search08:07Z | supports | Structure corrections currently accept only pinned REPLACE_WITH_CHEBI or SPLIT_SHARED_WITH_CHEBI to an eligible three-star structured ChEBI row, not a free-form manual N–H replacement. LOTUS exclusions are exact key/taxon/DOI source-row pinned. The CyanoMetDB emitter substitutes nmr_used directly into “structure confirmed by …”. No target-specific maintained correction was found in the inspected curation/code scope. Root also inspected claim_references.py lines52–57 and seeder strain/isolate guards: structure_correction_note causes rejection of those combined overlays. Refreshing pins alone is insufficient; compatible guarded composition needs an explicit tested implementation. |
| bgc016-source | https://mibig.secondarymetabolites.org/repository/BGC0000668.5/annotations.json; Full v5 JSON; compounds[10], loci, taxonomy, classes and legacy references | supports | Exact compound 11 is 3-epi-welwitindolinone B isothiocyanate with the stored stereochemical SMILES, C22H23ClN2O2S, NPA019701 and CyanoMetDB 1513. Its compound evidence is NMR with DOI 10.1021/jo00226a009. Entry-wide locus methods are Enzymatic assays and Heterologous expression, without method-level references. Separate legacy references are PMID:24677572 and PMID:25218740. The active, complete, questionable-quality entry gives KF811479.1 and taxon 1433842; 0/0 bounds are unspecified, correctly omitted. |
| bgc016-genome | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KF811479.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text; LOCUS, DEFINITION, VERSION, source feature, REFERENCE1 and WelM/WelO5 CDSs | supports | The deposited 36570-bp partial indolinone cluster is explicitly from H. welwitschii UTEX B1830, taxon 1433842, and links to PMID:24677572. WelM is AHI58817.1 at complement(1779..2822), while WelO5 is AHI58816.1 at complement(126..998). These annotations establish the native accession and strain bridge; no historical construct equivalence or exact 3-epi-B formation follows from annotation alone. |
| bgc016-old-citation | https://api.crossref.org/works/10.1021/jo00226a009; Official DOI metadata, title, year, journal and article pages; primary body access remains limited | partial | The sole producer/locus DOI resolves to the 1987 J. Org. Chem. paper Fontonamide and anhydrohapaloxindole A, two new alkaloids from the blue-green alga Hapalosiphon fontinalis,52:3773–3777. It is the compound NMR reference in MIBiG, not the 2014 study that identified KF811479.1. Its whole-body compound coverage was not inspected, so no article-wide absence claim is made. |
| bgc016-primary2014-cluster | https://pmc.ncbi.nlm.nih.gov/articles/PMC4382313/; PMID:24677572, DOI 10.1002/cbic.201300794; complete body P1–P11 and captions F1–F5 re-read in004/wel2014-primary.xml at08:02–08:03Z; original retrieval retained | partial | The study sequenced xenic UTEX B1830 and linked the 36-kb wel cluster to this family. Its characterized products are precursor 10 from WelI1–3, GPP from WelP2, and N-methylwelwitindolinone C isothiocyanate 3b from WelM plus 3a. The latter is a different congener from exact 3-epi-B. P8–P10 treat WelO1–4 oxidative maturation and sulfur donation as proposals. The inspected body therefore supports pathway association, not direct target formation; exact target-specific supplementary panels remain unverified. |
| bgc016-primary2014-halogenase | https://www.nature.com/articles/nchembio.1625; PMID:25218740 / DOI 10.1038/nchembio.1625; primary abstract, with previously retrieved005/welo5-2014-si.pdf and text, especially Figure S1 and product HRMS/NMR sections | partial | WelO5 assays concern free 12-epi-fischerindole U to G and 12-epi-hapalindole C to E. The source supplement explicitly distinguishes these characterized reactions from proposed later WelO1–4 steps. These exact products differ from 3-epi-welwitindolinone B; precursor chlorination is not target-product reconstitution. No main-body access beyond the abstract is claimed. |
| bgc016-primary2017-cyclase | https://pubs.rsc.org/en/content/articlehtml/2017/cc/c7cc00782e; PMID:28225144 / DOI 10.1039/c7cc00782e; original primary abstract inspection reused, independently resurfaced in bounded current search | partial | The primary abstract identifies WelU1 and WelU3 formation of 12-epi-fischerindole U and 12-epi-hapalindole C. Those precursor-family results do not establish formation of this late oxidized, sulfur-containing 3-epi-B target. No UTEX/IC-52-3 enzyme result is silently transferred. |
| bgc016-routing-and-guards | scripts/extract_mibig.py; scripts/seed_from_sources.py; src/naturalproductmech/curate/claim_references.py; data/raw/mibig_compounds.tsv; Full owner read08:02:31Z; exact raw BGC0000668:11 row; extractor primary_reference()/locus_evidence_methods(); seeder override functions and claim-reference loader inspected08:03:42Z | supports | The extractor prioritizes compound NMR references and copies entry-wide methods to each compound. This exact raw row then generates both producer/locus citations from the 1987 DOI. Its canonical full-row SHA256 is 898e4cc1c18baee06f71050e4213d7898482e8fd806306a433335106004e3266. The implemented claim-reference table enforces that SHA. WITHDRAW validates expected version, taxon, accession, bounds, full key and original methods. REPLACE currently does not enforce expected_* fields; any replacement requires a paired SHA-pinned claim-reference row or a loader extension. |
| bgc016-search-scope | https://pubmed.ncbi.nlm.nih.gov/28225144/; Bounded exact-name and enzyme/WelO searches at08:02–08:03Z; primary leads checked against the inspected papers | unknown | No retrieved primary result in this bounded search directly established production of exact 3-epi-welwitindolinone B by the recorded locus. Search results primarily concerned common intermediates, other congeners or chemical synthesis. This does not establish absence of all later target-specific studies. |
| R-IMODULON | /private/tmp/npm-review-work/010/imodulon-datasets.txt; Complete 28-row installed runner response, original010/imodulon-context-receipts.json | context_only | The complete returned catalogue has no Hapalosiphon dataset. No native-strain expression-module query is applicable; this is source coverage rather than absence of biosynthesis. |

## Limits And Additional Notes

- The 1987 primary body remains uninspected; official metadata and its MIBiG NMR placement are known. No article-wide absence conclusion rests on the title.
- The 2014 cluster main text and captions were fully re-read. Its original supplementary target-specific panels were not inspected here. Main-text common-precursor and WelM product scope is explicit and sufficient to distinguish the demonstrated products from exact 3-epi-B.
- The 2014 halogenase abstract and previously obtained official supplement apply to different exact products. The 2017 cyclase abstract likewise concerns C/U, not the late oxidized target. No unsupported transfer between congeners or strains is used.
- The search is bounded to the named primary sources and recorded queries; no assertion that the target can never be made by this locus or that no later exact study exists is made.
- The identity reviewer reported a primary drawing conflict between the named natural compound and the current N-methyl database graph. This BGC packet verifies current source/owner consistency only and does not resolve that chemical identity. Any future method or citation correction must be re-pinned if identity adjudication changes the source graph. Both candidate target interpretations remain distinct from the characterized N-methylwelwitindolinone C product.
- The original 1994 body/drawing and full absolute stereochemical argument were unavailable after bounded free access attempts. Later primary Figure 1 conflicts with database N-substitution; this warrants a provisional identity blocker, not an unconditional replacement.
- The free 2014 paper is publisher-format text hosted by a public mirror. DOI/title/authors match official PubMed; only the actual inspected Figure 1/prose is used. Its synthetic experiments target N-methylB and are not exact 3-epi-B production evidence.
- Original 1987 full texts were not inspected. Metadata raises a concrete citation/taxon concern, but cannot prove article-wide absence.
- Database cross-reference equivalence establishes agreement among encoded graphs, not independent confirmation of isolation or all absolute configurations.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- No scientific record, maintained correction table, source inventory or native status/history was edited. The provisional identity blocker is a review finding and does not stop the authorized corpus-review campaign.
- Baseline deterministic checks reuse actual successful receipts from the identical tracked base. Target strict validation ran afresh. Scientific failed/unavailable checks are distinct from review-bundle validation.
- Identity adjudication precedes any final correction. Current source pins must be refreshed and all exact-key joins re-evaluated if the chemical structure changes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082051Z-3-epi-welwitindolinone-b-isothiocyanate
kind: record
repository: CultureBotAI/NaturalProductMech
title: '3-epi-welwitindolinone B: disputed N-substitution and claim-specific evidence'
started_at: '2026-10-21T07:59:49.451341Z'
finished_at: '2026-10-21T08:20:51.920530Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: A primary drawing assigns the named congener an N–H group, conflicting with
  the N-methyl graph shared by the owner and databases. Identity correction remains
  provisional pending original isolation evidence. The locus claim has confirmed citation-routing
  and method-scope defects; two 1987 occurrence citations remain unresolved, and CyanoMetDB
  NMR wording overstates a usage flag.
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
  - path: data/natural_products/alkaloids/3-epi-welwitindolinone-b-isothiocyanate.yaml
    sha256: 24123a47cb40eba95bb93c3415488d6e0f2612dc5674065c3af8e96d73dd784e
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
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete owner, exact chemical identity and stereochemistry, all
    xrefs and occurrence citations, producer/locus scope, current grounding, classification
    and history.
  selection: Sixteenth initially unreviewed path, sixth in batch 002 from fresh origin/main.
    Review starts and saves follow path order. The fresh-main authoritative list has
    91 valid bundles covering 54 of 3,116 records; ten pending PR 1000 targets are
    additional campaign coverage. Ignored files were included. This bundle reviews
    one target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-1439bab61e
targets:
- target_id: naturalproductmech:mibig-1439bab61e
  path: data/natural_products/alkaloids/3-epi-welwitindolinone-b-isothiocyanate.yaml
  label: 3-epi-welwitindolinone B isothiocyanate
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
  summary: The entire owner validates with zero ERROR rows. This does not settle scientific
    identity.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  command: just validate-strict data/natural_products/alkaloids/3-epi-welwitindolinone-b-isothiocyanate.yaml
    --out /private/tmp/npm-review-work/016/strict.tsv
  exit_code: 0
  scope_note: Actual target command finished 2026-10-21T07:59:53.457272Z
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
    for batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-1439bab61e
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
    Reused for batch 002 because the tracked source tree and HEAD remain the exact
    same base commit; this command was not rerun for batch 002. The review author
    must assign the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-1439bab61e
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
    for batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-1439bab61e
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
    Reused for batch 002 because the tracked source tree and HEAD remain the exact
    same base commit; this command was not rerun for batch 002. The review author
    must assign the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-1439bab61e
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
    for batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-1439bab61e
- check_id: C-GRAPH-CONSISTENCY
  name: Encoded graph and current authority agreement
  status: passed
  required: true
  summary: The full encoded N-methyl structure, formula and five centres reproduce
    the stored InChI/key and current database records. This is internal/source consistency
    only.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-CHEMISTRY
  - S016-NPA
  - S016-CHEBI-MOL
  - S016-PUBCHEM
- check_id: C-PRIMARY-IDENTITY
  name: Original exact named congener identity
  status: unavailable
  required: true
  summary: A later primary drawing names an N–H congener while current databases encode
    N-methyl. Original1994 drawing and complete absolute stereochemical argument remain
    unavailable; neither a final replacement nor exact natural-origin sign-off is
    established.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-2014-DRAWING
  - S016-1994-ABSTRACT
  - S016-1994-ACCESS
  - S016-CHEMISTRY
- check_id: C-1987-CITATIONS
  name: Exact target/taxon scope in both1987 occurrence citations
  status: unavailable
  required: true
  summary: Official titles concern H. fontinalis; full article bodies are unavailable.
    The imported H. welwitschii triples require direct adjudication and are not excluded
    from titles alone.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-1987-HAPALINDOLES
  - bgc016-old-citation
  - S016-RAW
- check_id: C-BGC-PLACEMENT
  name: Claim-specific reference and demonstrated-product scope
  status: failed
  required: true
  summary: The generated sole locus reference is compound NMR metadata. Inspected
    pathway experiments concern precursors and C congeners, so those results cannot
    supply exact 3-epi-B demonstration. Reference routing needs correction and target-specific
    method adjudication.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - bgc016-routing-and-guards
  - bgc016-primary2014-cluster
  - bgc016-primary2014-halogenase
- check_id: C-IMODULON
  name: Native expression-source applicability
  status: not_applicable
  required: false
  summary: The complete returned catalogue has no native Hapalosiphon dataset.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - R-IMODULON
evidence:
- evidence_id: S016-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/3-epi-welwitindolinone-b-isothiocyanate.yaml
  locator: Entire owner and resolved view, all source rows; read 08:00:03Z and reread
    08:06Z
  accessed_at: '2026-10-21T08:00:03Z'
  support: supports
  summary: One SEEDED MIBiG-derived owner with five assigned centres, two chemical
    xrefs, four species-level database occurrences, one strain-level SOURCE_ASSERTION
    producer and one demonstrated locus. No inline or referenced graph, pathway steps,
    bioactivities, molecular targets, clinical assertions or cross-corpus links are
    present in this owner.
  snapshot_sha256: 24123a47cb40eba95bb93c3415488d6e0f2612dc5674065c3af8e96d73dd784e
- evidence_id: S016-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv; data/raw/lotus_occurrences.tsv; data/raw/cyanometdb_occurrences.tsv;
    data/raw/npclassifier.tsv
  locator: Exact rows extracted in 016/local-sources.json; pinned source hashes are
    in inspection.json
  accessed_at: '2026-10-21T08:00:03Z'
  support: supports
  summary: MIBiG BGC0000668:11 and all joined chemical rows carry RBPIZRWOMRMEOB-ADDAZVEVSA-N.
    LOTUS retains three separate DOI triples. CyanoMetDB contributes the 1994 DOI,
    UHIC-52-3 strain string and nmr_used=yes. NPClassifier contributes Alkaloids,
    empty superclass/class and no glycoside. This verifies import fidelity, not independent
    natural-product identity.
- evidence_id: S016-NPA
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA019701?include=classifications
  locator: NPA019701 current structure v1, origin_reference, origin_organism, npclassifier
  accessed_at: '2026-10-21T08:01:00.799312Z'
  support: supports
  summary: NPA019701 resolves to the owner full InChI/key and N-methyl C22H23ClN2O2S
    graph. Its original label matches, but its origin reference is DOI 10.1021/jo00226a009,
    the 1987 fontonamide paper. No structure reassignment is listed. Database agreement
    does not adjudicate the later-primary N–H conflict.
  snapshot_sha256: 36f496c4aadaa4780330ef7a295975be0f443365876c7b64d65af0f9aded2dc1
- evidence_id: S016-CHEBI
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/216541/
  locator: CHEBI:216541 stars, default_structure 3412621, chemical_data and origins
  accessed_at: '2026-10-21T08:01:00.799063Z'
  support: supports
  summary: CHEBI:216541 is two-star and its default N-methyl graph has the exact owner
    full InChI/key and formula. It is therefore ineligible for the repository three-star
    grounding rule. Its origin citation repeats the 1987 DOI, so it is not independent
    evidence for the named natural structure.
  snapshot_sha256: 956a527904a174c03a4e78462365a80b11a9316d0253fe706734736e3a698807
- evidence_id: S016-CHEBI-MOL
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/216541/
  locator: Official default molfile; independently parsed with RDKit
  accessed_at: '2026-10-21T08:01:00.799204Z'
  support: supports
  summary: The default molfile produces RBPIZRWOMRMEOB-ADDAZVEVSA-N and the same full
    InChI as the owner; all five encoded centres agree.
  snapshot_sha256: 4aa8f3b5f4d736554e9f747eba17800f78b6cf2d22deed57f69445db10d58fc4
- evidence_id: S016-CHEBI-SEARCH
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=RBPIZRWOMRMEOB-ADDAZVEVSA-N&size=100
  locator: Exact full InChIKey search, returned one entry
  accessed_at: '2026-10-21T08:01:00.798550Z'
  support: supports
  summary: The official search returned only two-star CHEBI:216541 for the current
    full key. This bounded result supports retaining a minted identifier for the encoded
    graph, pending identity adjudication.
  snapshot_sha256: c98f064290e935d69a4c4ae2441020bae6e56c570b4b0f095ec7961a127184ae
  search_scope: Official ChEBI public es_search exact term RBPIZRWOMRMEOB-ADDAZVEVSA-N,
    size100; returned one result, independently inspected default structure and rating.
    No assertion about every alternate tautomer or future entry.
- evidence_id: S016-PUBCHEM
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/RBPIZRWOMRMEOB-ADDAZVEVSA-N/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: PUG REST full-key property response, CID 139588580
  accessed_at: '2026-10-21T08:01:00.799431Z'
  support: supports
  summary: CID 139588580 has the exact current full key, InChI and C22H23ClN2O2S formula.
    This is a current structural cross-check, not a primary isolation or stereochemical
    determination.
  snapshot_sha256: 048805b5a5b3e68b15026a2e1d72a8cc41880de2b7031bd08a770d0845e50421
- evidence_id: S016-PARENT-EPIMER
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/101959988/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: PUG REST properties for CID 101959988, supplied as second CID in original
    CyanoMetDB row
  accessed_at: '2026-10-21T08:03:00.973675Z'
  support: context_only
  summary: CID 101959988 instead has RBPIZRWOMRMEOB-AGRNFKIVSA-N, differing at the
    oxindole C3 stereocentre. It is not an exact xref for this owner. The source alias
    N-Methylwelwitindolinone B and this second CID must not be imported as equivalent
    without resolving the chemical conflict.
  snapshot_sha256: 9da2b4577170a1782fd2221ad8e5aa5c6a6a355b74466475c58a2d0558cef60c
- evidence_id: S016-CYANO
  kind: database
  reference: https://zenodo.org/records/13854577/files/CyanoMetDB_V03_2024.csv?download=1
  locator: Original v03 row CyanoMetDB_1513, re-extracted from inspected 002/cyanometdb-v03.csv
    at08:02Z
  accessed_at: '2026-10-21T06:43:53Z'
  support: partial
  summary: The row names 3-epi-welwitindolinone B, encodes the current N-methyl graph,
    cites DOI 10.1021/ja00101a015 and reports H. welwitschii UHIC-52-3 with NMR_used=yes.
    Its alternate name and secondary CID point to N-methylwelwitindolinone B, a distinct
    epimer in PubChem. NMR_used is a usage flag, not proof that every structural detail
    is confirmed.
  snapshot_sha256: 91aa57146c9e803d5eeef656fc0e5cfc8f804531b1b83718757e96aa848a4121
- evidence_id: S016-TAXA
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=162986,1433842,1524913&retmode=xml
  locator: NCBI Taxonomy 162986,1433842,1524913 names, ranks and lineage
  accessed_at: '2026-10-21T08:01:01.273326Z'
  support: supports
  summary: 162986 is Hapalosiphon welwitschii; 1433842 is strain UTEX B1830 and 1524913
    is strain UHIC-52-3. Both strains descend from that species in the cyanobacterial
    lineage. They are distinct strain taxa; the original isolation strain cannot be
    silently equated to the sequenced UTEX strain.
  snapshot_sha256: 2969b1d9c98a33a8ef7e6e05ef98611af57f8cb558bec93951c74452378ad990
- evidence_id: S016-WIKIDATA
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q67340456.json
  locator: entity Q67340456 revision 2543823250, label/en and claims P225/P685
  accessed_at: '2026-10-21T06:44:23.635771Z'
  support: supports
  summary: Reinspection of the previously fetched entity confirms Q67340456 identifies
    Hapalosiphon welwitschii and NCBI 162986, matching this owner’s three LOTUS provenance
    URIs. Original retrieval time is retained.
  snapshot_sha256: 53fdaac9788b1ac4ea420b9173248f248da507f8d3a1ab73fa39607f8c6cd4fb
- evidence_id: S016-1994-ABSTRACT
  kind: primary_source
  reference: https://pure.psu.edu/en/publications/welwitindolinones-unusual-alkaloids-from-the-blue-green-algae-hap/
  locator: Author institutional abstract of Stratmann et al.1994, DOI 10.1021/ja00101a015
  accessed_at: '2026-10-21T08:01:01.845418Z'
  support: partial
  summary: The abstract reports welwitindolinones and minor alkaloids from H. welwitschii
    UHIC-52-3, with gross structures and relative configurations for compounds 1–6
    and 8–15. X-ray absolute configuration is stated only for major compound 7. It
    does not enumerate the exact 3-epi target or verify its N-substitution, complete
    configuration or UTEX occurrence.
  snapshot_sha256: 3a25bc9d93388efbacdb4d15df7084aaa8f38b364b977ac02cb00c1ae6f334ff
- evidence_id: S016-1987-HAPALINDOLES
  kind: authority
  reference: https://api.crossref.org/works/10.1021/jo00382a012
  locator: Official DOI title, authors, year and journal
  accessed_at: '2026-10-21T08:01:01.570313Z'
  support: partial
  summary: DOI 10.1021/jo00382a012 is the 1987 J. Org. Chem. paper Hapalindoles, antibacterial
    and antimycotic alkaloids from the cyanophyte Hapalosiphon fontinalis,52:1036–1043.
    This is a citation/taxon warning for the H. welwitschii triple, not proof that
    the uninspected whole body never discusses the target.
  snapshot_sha256: 32b5826e8d208f15059f46f4273818455fd012208138f39349a34b68a8423dde
- evidence_id: S016-2012
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3368435
  locator: PMC3368435 complete body and reference 17; DOI 10.1021/ja210793x, PMID22235963
  accessed_at: '2026-10-21T08:02:11.938645Z'
  support: partial
  summary: Reference 17 explicitly identifies the 3-epi-B isothiocyanate C3 configuration
    as S, citing the original isolation report. The paper’s actual syntheses concern
    C congeners; it does not establish all five centres or the target’s N-substitution.
    The owner atom 4, oxindole C3, is S.
  snapshot_sha256: d679fd59351f2387c036efcc3c232443cf5a19ea9caf519a61951849139698eb
- evidence_id: S016-2014-DRAWING
  kind: primary_source
  reference: https://file1.lookchem.com/doi/2022/3/29/c99d78a2-2dca-4bbc-ac30-bcffd75dfa9b.pdf
  locator: Publisher-format author primary paper DOI 10.1021/ol5020043, Figure 1 compound
    4 and adjacent prose, pageA; PDF visually inspected08:03:45Z and08:06Z
  accessed_at: '2026-10-21T08:03:14.638610Z'
  support: refutes
  summary: Figure 1 draws compound 4 with oxindole N–H, and prose names 4 as 3-epi-welwitindolinone
    B isothiocyanate. N-methylwelwitindolinone B is separately compound 2. The current
    owner instead encodes N-methyl. This is an explicit primary-versus-database conflict;
    the paper studies synthetic progress toward 2, not an original isolation or complete
    synthesis of 4.
  snapshot_sha256: 0b4c61a49a543cef4b358bc7b74297ccfbfbbbdd5244d26d197d837d4c1eea93
- evidence_id: S016-2014-REFERENCE
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=25124334&retmode=xml
  locator: PMID 25124334 title/authors/DOI
  accessed_at: '2026-10-21T08:03:01.474696Z'
  support: supports
  summary: The official PubMed record maps Leah Cleary, Jennifer Pitzen, John A.Brailsford
    and Kenneth J.Shea’s Progress toward the Total Synthesis of N-Methylwelwitindolinone
    B Isothiocyanate to DOI 10.1021/ol5020043, matching the inspected publisher-format
    PDF.
  snapshot_sha256: a20eba21304210233971695360084bcc7a6558389dd4232e776a5635fca2c161
- evidence_id: S016-CHEMISTRY
  kind: validation
  reference: /private/tmp/npm-review-work/016/identity-chemistry.json
  locator: RDKit2026.03.5 complete owner and authority graph comparison; atom-labelled
    owner drawing in016/record-stereo-atomlabels.png
  accessed_at: '2026-10-21T08:07:26.032895Z'
  support: supports
  summary: Owner SMILES yields its stored full InChI/key, C22H23ClN2O2S, neutral charge
    and assigned centres 4S,11S,17R,19R,21S (zero-based owner SMILES order). All inspected
    exact database structures match. The lactam N1 bears methyl atom 0. Removing only
    that methyl yields a computed N–H candidate C21H21ClN2O2S, key VLJMTNLRJHJRGI-GLTYWKJESA-N;
    this calculated candidate has not been adjudicated against the original isolation
    drawing.
  snapshot_sha256: 5758118786ec5a4f4a546bab55586d25fc04e11560f8ef43df1ffbc0d137d582
- evidence_id: S016-1994-ACCESS
  kind: search
  reference: https://pubs.acs.org/doi/abs/10.1021/ja00101a015?journalCode=jacsat
  locator: Bounded original-paper search/access receipts in016/1994-bounded-access-evidence.json
  accessed_at: '2026-10-21T08:03:55Z'
  support: unknown
  summary: Focused searches and direct official access did not provide a free original
    1994 drawing/body. The publisher returned403; SI routes returned202 with zero
    bytes and Figshare DOI search returned no result. The institutional abstract is
    the only inspected original text. No negative scientific inference is made from
    access failure.
  search_scope: Two focused original DOI/title search batches, official ACS open,
    official Figshare DOI/SI routes, and author institutional metadata. Search results
    and later-paper leads were not treated as original-paper content.
- evidence_id: S016-OWNERSHIP
  kind: record_content
  reference: src/naturalproductmech/curate/structure_corrections.py; curation/mibig_structure_corrections.tsv;
    curation/lotus_occurrence_exclusions.tsv; scripts/seed_from_sources.py; src/naturalproductmech/curate/claim_references.py
  locator: Full correction-loader functions and exact occurrence-note emitter read08:06Z;
    target correction search08:07Z
  accessed_at: '2026-10-21T08:09:26.165627Z'
  support: supports
  summary: 'Structure corrections currently accept only pinned REPLACE_WITH_CHEBI
    or SPLIT_SHARED_WITH_CHEBI to an eligible three-star structured ChEBI row, not
    a free-form manual N–H replacement. LOTUS exclusions are exact key/taxon/DOI source-row
    pinned. The CyanoMetDB emitter substitutes nmr_used directly into “structure confirmed
    by …”. No target-specific maintained correction was found in the inspected curation/code
    scope. Root also inspected claim_references.py lines52–57 and seeder strain/isolate
    guards: structure_correction_note causes rejection of those combined overlays.
    Refreshing pins alone is insufficient; compatible guarded composition needs an
    explicit tested implementation.'
  search_scope: rg --no-ignore --hidden over curation, src/naturalproductmech/curate,
    scripts and docs for target identifier, BGC0000668:11, full connectivity key and
    exact name; ignored files included. The reserved decisions.tsv is not proposed
    as an active consumer.
- evidence_id: bgc016-source
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000668.5/annotations.json
  locator: Full v5 JSON; compounds[10], loci, taxonomy, classes and legacy references
  accessed_at: '2026-10-21T08:03:41.799030Z'
  support: supports
  summary: Exact compound 11 is 3-epi-welwitindolinone B isothiocyanate with the stored
    stereochemical SMILES, C22H23ClN2O2S, NPA019701 and CyanoMetDB 1513. Its compound
    evidence is NMR with DOI 10.1021/jo00226a009. Entry-wide locus methods are Enzymatic
    assays and Heterologous expression, without method-level references. Separate
    legacy references are PMID:24677572 and PMID:25218740. The active, complete, questionable-quality
    entry gives KF811479.1 and taxon 1433842; 0/0 bounds are unspecified, correctly
    omitted.
  snapshot_sha256: cebbf3a80dd3eb5699df94e3ac7d461c046e4dd91b75d258e7fb85518edfdb54
- evidence_id: bgc016-genome
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KF811479.1&db=nuccore&report=genbank&retmode=text
  locator: LOCUS, DEFINITION, VERSION, source feature, REFERENCE1 and WelM/WelO5 CDSs
  accessed_at: '2026-10-21T08:03:41.799482Z'
  support: supports
  summary: The deposited 36570-bp partial indolinone cluster is explicitly from H.
    welwitschii UTEX B1830, taxon 1433842, and links to PMID:24677572. WelM is AHI58817.1
    at complement(1779..2822), while WelO5 is AHI58816.1 at complement(126..998).
    These annotations establish the native accession and strain bridge; no historical
    construct equivalence or exact 3-epi-B formation follows from annotation alone.
  snapshot_sha256: 1f965890a89cf00a42751d6ff0f62e8997ec4debf87d7ac353a907195563ee1f
- evidence_id: bgc016-old-citation
  kind: authority
  reference: https://api.crossref.org/works/10.1021/jo00226a009
  locator: Official DOI metadata, title, year, journal and article pages; primary
    body access remains limited
  accessed_at: '2026-10-21T08:01:01.490184Z'
  support: partial
  summary: The sole producer/locus DOI resolves to the 1987 J. Org. Chem. paper Fontonamide
    and anhydrohapaloxindole A, two new alkaloids from the blue-green alga Hapalosiphon
    fontinalis,52:3773–3777. It is the compound NMR reference in MIBiG, not the 2014
    study that identified KF811479.1. Its whole-body compound coverage was not inspected,
    so no article-wide absence claim is made.
  snapshot_sha256: 2ab8205bb0e7440bbb01f2e93eacfbc504fce857116e9d76ee2a9af6189d8472
- evidence_id: bgc016-primary2014-cluster
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4382313/
  locator: PMID:24677572, DOI 10.1002/cbic.201300794; complete body P1–P11 and captions
    F1–F5 re-read in004/wel2014-primary.xml at08:02–08:03Z; original retrieval retained
  accessed_at: '2026-10-21T06:53:50Z'
  support: partial
  summary: The study sequenced xenic UTEX B1830 and linked the 36-kb wel cluster to
    this family. Its characterized products are precursor 10 from WelI1–3, GPP from
    WelP2, and N-methylwelwitindolinone C isothiocyanate 3b from WelM plus 3a. The
    latter is a different congener from exact 3-epi-B. P8–P10 treat WelO1–4 oxidative
    maturation and sulfur donation as proposals. The inspected body therefore supports
    pathway association, not direct target formation; exact target-specific supplementary
    panels remain unverified.
  snapshot_sha256: 2535abb9ec5c9d4f7d4a8e030b0c71821d2f23b1b6a9f9eee55ca88f1e3a8678
- evidence_id: bgc016-primary2014-halogenase
  kind: primary_source
  reference: https://www.nature.com/articles/nchembio.1625
  locator: PMID:25218740 / DOI 10.1038/nchembio.1625; primary abstract, with previously
    retrieved005/welo5-2014-si.pdf and text, especially Figure S1 and product HRMS/NMR
    sections
  accessed_at: '2026-10-21T06:58:15Z'
  support: partial
  summary: WelO5 assays concern free 12-epi-fischerindole U to G and 12-epi-hapalindole
    C to E. The source supplement explicitly distinguishes these characterized reactions
    from proposed later WelO1–4 steps. These exact products differ from 3-epi-welwitindolinone
    B; precursor chlorination is not target-product reconstitution. No main-body access
    beyond the abstract is claimed.
- evidence_id: bgc016-primary2017-cyclase
  kind: primary_source
  reference: https://pubs.rsc.org/en/content/articlehtml/2017/cc/c7cc00782e
  locator: PMID:28225144 / DOI 10.1039/c7cc00782e; original primary abstract inspection
    reused, independently resurfaced in bounded current search
  accessed_at: '2026-10-21T06:50:18Z'
  support: partial
  summary: The primary abstract identifies WelU1 and WelU3 formation of 12-epi-fischerindole
    U and 12-epi-hapalindole C. Those precursor-family results do not establish formation
    of this late oxidized, sulfur-containing 3-epi-B target. No UTEX/IC-52-3 enzyme
    result is silently transferred.
- evidence_id: bgc016-routing-and-guards
  kind: record_content
  reference: scripts/extract_mibig.py; scripts/seed_from_sources.py; src/naturalproductmech/curate/claim_references.py;
    data/raw/mibig_compounds.tsv
  locator: Full owner read08:02:31Z; exact raw BGC0000668:11 row; extractor primary_reference()/locus_evidence_methods();
    seeder override functions and claim-reference loader inspected08:03:42Z
  accessed_at: '2026-10-21T08:05:35.539870Z'
  support: supports
  summary: The extractor prioritizes compound NMR references and copies entry-wide
    methods to each compound. This exact raw row then generates both producer/locus
    citations from the 1987 DOI. Its canonical full-row SHA256 is 898e4cc1c18baee06f71050e4213d7898482e8fd806306a433335106004e3266.
    The implemented claim-reference table enforces that SHA. WITHDRAW validates expected
    version, taxon, accession, bounds, full key and original methods. REPLACE currently
    does not enforce expected_* fields; any replacement requires a paired SHA-pinned
    claim-reference row or a loader extension.
  search_scope: rg --no-ignore --hidden searched exact identifier and BGC0000668:11
    in curation and relevant extractor/seeder paths, including ignored files; no existing
    target-specific correction row was found. Source row compared directly to the
    committed parsed TSV.
- evidence_id: bgc016-search-scope
  kind: search
  reference: https://pubmed.ncbi.nlm.nih.gov/28225144/
  locator: Bounded exact-name and enzyme/WelO searches at08:02–08:03Z; primary leads
    checked against the inspected papers
  accessed_at: '2026-10-21T08:05:35.539870Z'
  support: unknown
  summary: No retrieved primary result in this bounded search directly established
    production of exact 3-epi-welwitindolinone B by the recorded locus. Search results
    primarily concerned common intermediates, other congeners or chemical synthesis.
    This does not establish absence of all later target-specific studies.
  search_scope: 'Queries: exact quoted 3-epi-welwitindolinone B with biosynthesis/enzyme;
    welwitindolinone B with WelO; welwitindolinone biosynthesis oxygenase WelO1 WelO2.
    Reviewed primary 2014 cluster,2014 halogenase and 2017 cyclase scope; review articles
    and thesis snippets used only as leads, not proof.'
- evidence_id: R-IMODULON
  kind: search
  reference: /private/tmp/npm-review-work/010/imodulon-datasets.txt
  locator: Complete 28-row installed runner response, original010/imodulon-context-receipts.json
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: The complete returned catalogue has no Hapalosiphon dataset. No native-strain
    expression-module query is applicable; this is source coverage rather than absence
    of biosynthesis.
  search_scope: All28 returned dataset rows, reused at original access time and explicitly
    compared with the native species/strains in this owner.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
assessments:
- assessment_id: S016-IDENTITY
  area: identity
  topic: Name-to-structure and N-substitution
  outcome: concern
  summary: The encoded graph is internally coherent and consistently reproduced by
    linked databases, but a primary drawing explicitly assigns the name to an N–H
    congener. Database consensus cannot settle this identity conflict. The computed
    demethylated candidate is a lead, not an approved replacement.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-OWNER
  - S016-2014-DRAWING
  - S016-CHEMISTRY
  - S016-NPA
  - S016-CYANO
- assessment_id: S016-STEREO
  area: identity
  topic: C3 epimer and absolute stereochemical scope
  outcome: unknown
  summary: All five centres are encoded, so stereo_complete=true accurately describes
    the representation. The later primary note corroborates C3S; the original abstract
    only promises relative configurations for minor congeners. Complete primary absolute
    stereochemical confirmation remains unavailable and the N-substitution conflict
    must be resolved first.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-CHEMISTRY
  - S016-2012
  - S016-1994-ABSTRACT
  - S016-1994-ACCESS
- assessment_id: S016-XREFS
  area: identity
  topic: Exact database graph equivalence
  outcome: supported
  summary: NPA019701 and CyanoMetDB 1513 carry the same exact current graph/key. This
    structural equivalence does not certify the label’s natural-product identity.
    CyanoMetDB’s alternative epimer CID and synonym are correctly not copied into
    owner xrefs.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-NPA
  - S016-CYANO
  - S016-PARENT-EPIMER
  - S016-CHEMISTRY
- assessment_id: S016-GROUNDING
  area: grounding
  topic: Current minted identifier and ChEBI eligibility
  outcome: supported
  summary: For the currently encoded graph the exact live ChEBI match is only two-star
    216541, consistent with MINTED under the project rule. Regrounding and minted
    identity migration must be reassessed if chemical identity changes.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-CHEBI
  - S016-CHEBI-SEARCH
  - S016-OWNER
- assessment_id: S016-1994-OCCURRENCE
  area: evidence
  topic: 1994 LOTUS/CyanoMetDB occurrence and exact isolation
  outcome: unknown
  summary: The databases explicitly retain the 1994 H. welwitschii/UHIC-52-3 attribution.
    The inspected original abstract supports the family and culture, but not the exact
    named congener’s N-substitution or complete structure. Thus source import is verified
    while the individual cited occurrence remains unverified.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-RAW
  - S016-CYANO
  - S016-1994-ABSTRACT
  - S016-1994-ACCESS
  - S016-2014-DRAWING
- assessment_id: S016-1987-OCCURRENCES
  area: evidence
  topic: Two separate 1987 LOTUS citations
  outcome: concern
  summary: Both official DOI records describe H. fontinalis alkaloids, whereas the
    retained triples assert the current exact graph in H. welwitschii. Their applicability
    needs primary-body adjudication. No exclusion is justified solely by article titles,
    nor may positive 1994 family evidence validate these separate citations.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-RAW
  - S016-1987-HAPALINDOLES
  - bgc016-old-citation
- assessment_id: S016-TAXONOMY
  area: grounding
  topic: Species, strain and cyanobacterial grouping
  outcome: supported
  summary: All NCBI IDs and the Wikidata species URI resolve consistently. The UHIC-52-3
    occurrence string remains distinct from UTEX B1830 producer/locus context; grouping
    as CYANOBACTERIAL is appropriate.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-TAXA
  - S016-WIKIDATA
  - S016-OWNER
- assessment_id: S016-NMR
  area: evidence
  topic: CyanoMetDB method flag wording
  outcome: concern
  summary: NMR_used=yes is faithfully imported but rendered as “structure confirmed
    by yes”. The wording promotes a method-usage flag into a generic confirmation
    statement, especially misleading while exact identity remains disputed.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-CYANO
  - S016-OWNERSHIP
- assessment_id: S016-CLASSIFICATION
  area: scope
  topic: Computed filing versus source cluster classes
  outcome: supported
  summary: ALKALOIDS follows the pinned NPClassifier Alkaloids result for the current
    graph, retaining tool/version and empty lower classes. TERPENE and OTHER preserve
    MIBiG BGC-class assertions on a separate axis. Neither result is primary evidence
    that this exact encoded structure was isolated.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-RAW
  - S016-NPA
  - bgc016-source
- assessment_id: S016-NATURAL-ORIGIN
  area: evidence
  topic: Natural-product admission and exact graph
  outcome: unknown
  summary: The named welwitindolinone is a reported natural-product lead and the source
    asserts natural origin. The disputed N-methyl graph must be reconciled before
    treating the present exact structure’s occurrence or biosynthetic origin as independently
    verified.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-CYANO
  - S016-1994-ABSTRACT
  - S016-2014-DRAWING
- assessment_id: S016-OPTIONAL
  area: completeness
  topic: Mechanism, activity, quantities, datasets and clinical fields
  outcome: not_applicable
  summary: The complete owner has no optional mechanism graphs, pathway steps, activity
    measurements or summary, targets, datasets, clinical status or related-record
    assertions to audit. These absences alone are not findings. The complete returned
    iModulonDB catalogue has no Hapalosiphon dataset.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-OWNER
  - R-IMODULON
- assessment_id: S016-HISTORY
  area: provenance
  topic: Source concept, SEEDED status and audit trail
  outcome: supported
  summary: The source concept remains versioned MIBiG BGC0000668 and the two explicit
    seed events describe inventory imports. SEEDED accurately avoids scientific sign-off;
    this review does not promote status or rewrite history. Native checks are documented
    separately from scientific evidence.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - S016-OWNER
  - S016-RAW
- assessment_id: bgc016-metadata
  area: grounding
  topic: Exact MIBiG compound, locus and strain metadata
  outcome: supported
  summary: Compound 11 agrees with the owner as a current database graph and label.
    This source consistency does not independently settle the historical name-to-structure
    identity, which is under separate review for a possible N–H versus N-methyl conflict.
    The genome accession is the stated UTEX B1830 strain, and source class/unspecified
    coordinates are faithfully represented. Native producer SOURCE_ASSERTION remains
    separate from locus methods.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - bgc016-source
  - bgc016-genome
  - bgc016-routing-and-guards
- assessment_id: bgc016-primary-scope
  area: evidence
  topic: Claim-specific citation and exact-congener demonstration
  outcome: concern
  summary: The sole claim DOI is imported from compound NMR metadata, while the actual
    source pathway references are omitted. Inspected primary experiments demonstrate
    precursors and a different welwitindolinone, leaving exact 3-epi-B demonstration
    unsubstantiated by those results. The citation-routing defect is confirmed; all-literature
    absence is not asserted.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - bgc016-source
  - bgc016-old-citation
  - bgc016-primary2014-cluster
  - bgc016-primary2014-halogenase
  - bgc016-primary2017-cyclase
  - bgc016-routing-and-guards
- assessment_id: bgc016-native-boundary
  area: evidence
  topic: Native producer scope and culture status
  outcome: supported
  summary: Retaining SOURCE_ASSERTION is appropriate. Xenic UTEX B1830 metabolite/genome
    association and recombinant pathway enzymology are not an axenic native knockout
    or exact-target sufficiency experiment. Species-level historical isolation and
    IC-52-3 material must remain distinct from this strain-specific claim.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  evidence_ids:
  - bgc016-primary2014-cluster
  - bgc016-genome
  - bgc016-source
findings:
- finding_id: S016-F-IDENTITY
  issue_key: mibig-bgc0000668-compound11-n-substitution
  category: identity
  severity: blocker
  status: open
  certainty: provisional
  title: Named 3-epi-B conflicts with the encoded N-methyl graph
  description: The inspected later-primary Figure 1 assigns the name to an N–H structure,
    whereas the owner and current source databases encode N-methyl. The conflict is
    observed directly; the correct final graph remains provisional because the original
    1994 drawing is unavailable. Resolve this before chemical identity sign-off or
    transferring source assertions to a replacement graph.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  field_paths:
  - label
  - chemical_structure
  - source_concepts[0]
  - xrefs
  evidence_ids:
  - S016-2014-DRAWING
  - S016-2014-REFERENCE
  - S016-CHEMISTRY
  - S016-CYANO
  - S016-1994-ACCESS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: guarded adjudicated structure correction when supported
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: current three-star-only correction loader; extension required for an ungrounded
      manual replacement
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: identity migration, exact-key joins and regenerated owner
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: preserved source row BGC0000668:11
- finding_id: S016-F-1987
  issue_key: lotus-3-epi-welwitindolinone-b-1987-citation-scope
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Two 1987 occurrence citations need exact taxon and congener verification
  description: The metadata for DOI 10.1021/JO00226A009 and 10.1021/JO00382A012 names
    H. fontinalis studies, conflicting with the imported H. welwitschii occurrence
    context. The full bodies were not available, so exact article coverage is unknown.
    Keep this citation-specific concern separate from 1994 isolation and from the
    locus routing defect.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  field_paths:
  - occurrences[1]
  - occurrences[2]
  evidence_ids:
  - S016-RAW
  - S016-1987-HAPALINDOLES
  - bgc016-old-citation
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: exact unsupported-triple exclusion after source adjudication
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: guarded generated occurrence assembly
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: original source triples remain preserved
- finding_id: S016-F-NMR
  issue_key: cyanometdb-nmr-used-rendered-as-structure-confirmed
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: NMR-used flag is rendered as generic structure confirmation
  description: The source says NMR_used=yes. The emitter produces “structure confirmed
    by yes”, an ungrammatical and overbroad claim that does not express the method
    flag’s actual scope.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  field_paths:
  - occurrences[3].evidence[0].notes
  evidence_ids:
  - S016-CYANO
  - S016-OWNERSHIP
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: CyanoMetDB evidence-note emitter
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: preserved source NMR usage flag
- finding_id: bgc016-claim-scope
  issue_key: mibig-bgc0000668-compound11-link-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Exact 3-epi-B locus claim reuses compound NMR citation and entry-wide methods
  description: The BGC0000668:11 producer and demonstrated-locus fields both cite
    only DOI 10.1021/jo00226a009, selected from compound NMR metadata. The primary
    pathway papers cited by MIBiG are omitted. Their inspected experiments establish
    precursor chemistry and other congeners, including WelM formation of N-methylwelwitindolinone
    C isothiocyanate, without a reported exact 3-epi-B product demonstration in the
    inspected material. Route references by claim and adjudicate the inherited methods
    specifically for this target. The 1987 body and exact 2014 supplementary target
    panel were not inspected; the finding does not assert those articles lack every
    mention or that no later exact study exists.
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  field_paths:
  - producer_organisms[0].evidence
  - biosynthetic_gene_clusters[0].evidence
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - biosynthetic_gene_clusters[0].link_evidence_basis
  evidence_ids:
  - bgc016-source
  - bgc016-old-citation
  - bgc016-primary2014-cluster
  - bgc016-primary2014-halogenase
  - bgc016-routing-and-guards
  rule_id: 'review-yaml-record Evidence Rules: claim-level citation placement and
    exact strain/congener scope'
  native_severity: 'major: sole claim citation is misrouted and exact-product demonstration
    cannot be inherited from other congeners'
  normalization_reason: Citation selection and inherited method applicability form
    one underlying evidence-scope problem, recorded once. Confirmed routing defect
    is distinguished from bounded uncertainty about exact-product proof.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: SHA-pinned producer versus locus citation routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: compound-specific method applicability and qualification
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: exact BGC0000668:11 source row, retained as imported provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: compound citation selection and entry-method propagation
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: generated claims and guarded locus-method application
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: existing full-source-row SHA enforcement
actions:
- action_id: S016-A-IDENTITY
  description: Adjudicate the original 1994 named congener against Figure 1 compound
    4 and its N-substitution, formula and all stereocentres. If N–H is confirmed,
    pin BGC0000668:11 source SHA 898e4cc1c18baee06f71050e4213d7898482e8fd806306a433335106004e3266
    and implement the correction through maintained inputs. The existing loader requires
    an eligible three-star ChEBI target; otherwise extend and test it for a fully
    pinned manual structure rather than fabricating a supported action. Preserve old-key
    provenance and audit identity migration, xrefs, occurrences, classifier output
    and locus applicability by exact new key. Do not automatically promote the computed
    VLJMTNLRJHJRGI-GLTYWKJESA-N candidate or transfer old-key claims. The current
    claim-reference loader rejects a row carrying structure_correction_note; producer
    strain/isolate qualifiers also reject that state. Stage identity adjudication
    before re-adjudicating claim scope. If both corrections are needed together, implement
    and test compatible guarded composition rather than assuming that refreshed pins
    alone make the existing overlays composable.
  finding_ids:
  - S016-F-IDENTITY
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: guarded adjudicated structure correction when supported
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: current three-star-only correction loader; extension required for an ungrounded
      manual replacement
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: identity migration, exact-key joins and regenerated owner
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: preserved source row BGC0000668:11
  generator: Adjudicated correction via structure_corrections and scripts/seed_from_sources.py
  acceptance_checks:
  - Primary drawing, name, N-substitution, formula and full stereo mapping are explicitly
    reconciled; uncertainty is retained if unresolved.
  - Source-row drift rejects the correction; a new manual mode has tested pins, chemistry
    validation and collision handling.
  - Changed connectivity receives an explicit identity migration; old-key xrefs/occurrences
    are not silently equated.
  - Target seed canary, strict validation, reproduction verification, corpus verification
    and required QC pass.
  - A changed-structure row cannot bypass current claim/strain/isolate conflict guards.
    Any combined correction has explicit new-identity evidence, source pins, tested
    composition and refusal on drift.
- action_id: S016-A-1987
  description: Inspect the two original 1987 papers for the exact named structure
    and taxon. If a triple is unsupported, withhold only that full-key/NCBITaxon162986/DOI
    triple through curation/lotus_occurrence_exclusions.tsv with its canonical source-row
    SHA. Retain raw provenance and independently adjudicate the 1994 and CyanoMetDB
    claims. A primary title alone is not enough to exclude.
  finding_ids:
  - S016-F-1987
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: exact unsupported-triple exclusion after source adjudication
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: guarded generated occurrence assembly
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: original source triples remain preserved
  generator: scripts/seed_from_sources.py with implemented LOTUS exclusion loader
  acceptance_checks:
  - Each retained 1987 triple has an exact primary compound/taxon locator.
  - Any exclusion pins the complete current source row and leaves other DOI/strain
    triples intact.
  - Seed canary and reproduction verification show only the adjudicated occurrence
    changes.
- action_id: S016-A-NMR
  description: 'Change the CyanoMetDB note emitter to report the source field as NMR
    used according to CyanoMetDB: yes (and analogously no/unspecified) while retaining
    DATABASE_ASSERTION and the original flag. Do not claim full absolute structure
    confirmation from this metadata.'
  finding_ids:
  - S016-F-NMR
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: CyanoMetDB evidence-note emitter
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: preserved source NMR usage flag
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Regenerated note accurately states NMR usage and preserves its database provenance.
  - Yes/no/missing values have sensible wording; strict and reproduction checks pass.
- action_id: bgc016-reconcile-claims
  description: Use curation/mibig_claim_references.tsv for BGC0000668:11 with expected_source_row_sha256
    898e4cc1c18baee06f71050e4213d7898482e8fd806306a433335106004e3266 to route the
    locus association to PMID:24677572 and the native source assertion to the versioned
    MIBiG record unless exact strain-specific primary production evidence is verified.
    Preserve the original 1987 compound citation in raw provenance and adjudicate
    occurrence independently. The inspected precursor/C-congener experiments do not
    justify exact-target Enzymatic assays or Heterologous expression methods. Qualify
    or withdraw inapplicable methods through the implemented target-specific override;
    WITHDRAW must pin version 5, taxon NCBITaxon:1433842, KF811479.1, explicit empty
    bounds, full key RBPIZRWOMRMEOB-ADDAZVEVSA-N and original methods Enzymatic assays|Heterologous
    expression. If an exact-product experiment instead justifies replacement methods,
    pair REPLACE with the SHA-pinned claim-reference row or extend and test loader
    enforcement; expected_* columns alone currently guard only WITHDRAW. Retain native
    SOURCE_ASSERTION and explicit xenic-culture limitations. Do not assign a new predicted/correlated
    grade without its own evidence. The current claim-reference loader rejects a row
    carrying structure_correction_note; producer strain/isolate qualifiers also reject
    that state. Stage identity adjudication before re-adjudicating claim scope. If
    both corrections are needed together, implement and test compatible guarded composition
    rather than assuming that refreshed pins alone make the existing overlays composable.
  finding_ids:
  - bgc016-claim-scope
  target_ids:
  - naturalproductmech:mibig-1439bab61e
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: SHA-pinned producer versus locus citation routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: compound-specific method applicability and qualification
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: exact BGC0000668:11 source row, retained as imported provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: compound citation selection and entry-method propagation
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: generated claims and guarded locus-method application
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: existing full-source-row SHA enforcement
  generator: scripts/seed_from_sources.py through the implemented claim-reference
    correction and locus-evidence override tables; guarded canary then regeneration
  acceptance_checks:
  - A reviewer can identify the exact product, enzyme/locus, strain and experiment
    for every retained demonstrated method; precursor/C-congener assays remain scoped
    to their actual products.
  - The sole locus reference is no longer a compound NMR citation; raw provenance
    retains the original citation and its COMPOUND_EVIDENCE basis.
  - Changing any source-row field invalidates the paired SHA-pinned correction. WITHDRAW
    verifies all explicit context including empty bounds; a REPLACE action is not
    described as guarded by unenforced expected_* fields.
  - Run the target seed canary, inspect generated claim grades/citations and qualification
    notes, then strict validation, reproduction verification, corpus verification
    and required QC.
  - A changed-structure row cannot bypass current claim/strain/isolate conflict guards.
    Any combined correction has explicit new-identity evidence, source pins, tested
    composition and refusal on drift.
limitations:
- The 1987 primary body remains uninspected; official metadata and its MIBiG NMR placement
  are known. No article-wide absence conclusion rests on the title.
- The 2014 cluster main text and captions were fully re-read. Its original supplementary
  target-specific panels were not inspected here. Main-text common-precursor and WelM
  product scope is explicit and sufficient to distinguish the demonstrated products
  from exact 3-epi-B.
- The 2014 halogenase abstract and previously obtained official supplement apply to
  different exact products. The 2017 cyclase abstract likewise concerns C/U, not the
  late oxidized target. No unsupported transfer between congeners or strains is used.
- The search is bounded to the named primary sources and recorded queries; no assertion
  that the target can never be made by this locus or that no later exact study exists
  is made.
- The identity reviewer reported a primary drawing conflict between the named natural
  compound and the current N-methyl database graph. This BGC packet verifies current
  source/owner consistency only and does not resolve that chemical identity. Any future
  method or citation correction must be re-pinned if identity adjudication changes
  the source graph. Both candidate target interpretations remain distinct from the
  characterized N-methylwelwitindolinone C product.
- The original 1994 body/drawing and full absolute stereochemical argument were unavailable
  after bounded free access attempts. Later primary Figure 1 conflicts with database
  N-substitution; this warrants a provisional identity blocker, not an unconditional
  replacement.
- The free 2014 paper is publisher-format text hosted by a public mirror. DOI/title/authors
  match official PubMed; only the actual inspected Figure 1/prose is used. Its synthetic
  experiments target N-methylB and are not exact 3-epi-B production evidence.
- Original 1987 full texts were not inspected. Metadata raises a concrete citation/taxon
  concern, but cannot prove article-wide absence.
- Database cross-reference equivalence establishes agreement among encoded graphs,
  not independent confirmation of isolation or all absolute configurations.
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
- No scientific record, maintained correction table, source inventory or native status/history
  was edited. The provisional identity blocker is a review finding and does not stop
  the authorized corpus-review campaign.
- Baseline deterministic checks reuse actual successful receipts from the identical
  tracked base. Target strict validation ran afresh. Scientific failed/unavailable
  checks are distinct from review-bundle validation.
- Identity adjudication precedes any final correction. Current source pins must be
  refreshed and all exact-key joins re-evaluated if the chemical structure changes.
tags:
- path-order-campaign
- batch-002
- welwitindolinone
- identity-conflict
- source-evidence
```
