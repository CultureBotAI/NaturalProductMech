# Ambiguine H isonitrile: resolve enantiomer conflict before attaching enzyme evidence

- Review: 20261021T120745Z-ambiguine-h-isonitrile
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T11:52:43.452347Z
- Finished UTC: 2026-10-21T12:07:45.738073Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The stored four-centre H graph agrees with MIBiG, NPAtlas and Wikidata, but the explicitly named 2015 product drawing and eligible ChEBI MOL/InChI encode the opposite enantiomer. This exact-identity conflict blocks accepting the named product. The candidate ChEBI SMILES is also invalid, so repair requires a consumed valid representation before a guarded structure/method composition. FamD1 directly forms the depicted H and its method can be added only with that identity repair. Original 2007 assignment methods and the extra occurrence citation remain incompletely verified.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 56, batch 006, selected in path order from the fresh-main authoritative validated catalogue and the separately validated pending-PR targets. At selection, 104 of 3116 current records had campaign coverage and 3012 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-eb25c9b521 | data/natural_products/alkaloids/ambiguine-h-isonitrile.yaml | generated | ambiguine H isonitrile |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-eb25c9b521 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-eb25c9b521 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-eb25c9b521 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-eb25c9b521 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-eb25c9b521 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-eb25c9b521 | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Exact authority structure and fixed-H comparison | passed | True | naturalproductmech:mibig-eb25c9b521 | Compared 7 representations against the owner; full Standard/fixed-H agreement is explicitly recorded. |
| Complete raw rows, source-concept hash and local identity collision scan | passed | True | naturalproductmech:mibig-eb25c9b521 | All complete local source projections match the independently parsed committed inventories; source row SHA256 and minted identifier are reproduced, and the current ignored-inclusive exact-identity matches were inspected. |
| Named H primary depiction and eligible authority versus owner | failed | True | naturalproductmech:mibig-eb25c9b521 | The four-centre primary H depiction and eligible ChEBI graph are the owner enantiomer; the current target representation also cannot safely be consumed unchanged. |
| Primary H depiction versus current exact owner | failed | True | naturalproductmech:mibig-eb25c9b521 | The primary four-centre H product drawing is the opposite enantiomer to the current owner; identifier packet carries the single structural finding. |
| Original H isolation and extra occurrence citation | unavailable | True | naturalproductmech:mibig-eb25c9b521 | Original 2007 methods and the extra malevamide citation full body remain unavailable; completion remains partial. |
| Complete owner and component scope | passed | True | naturalproductmech:mibig-eb25c9b521 | The complete owner and all present fields were read. The parsed component-reference set is empty, so no referenced component was omitted. All existing inspection input hashes still match. |

## Scientific And Domain Assessments

### Exact encoded structure and resolving authority identifiers

identity: concern. Targets: naturalproductmech:mibig-eb25c9b521.

Current MIBiG, NPAtlas and LOTUS-linked Wikidata agree with the owner enantiomer, but the explicit 2015 H drawing and eligible ChEBI:65400 MOL/InChI encode its opposite at all four centres. Agreement among the former databases does not settle the discrepancy.

### Eligible grounding and stable source-concept identity

provenance: concern. Targets: naturalproductmech:mibig-eb25c9b521.

The source-concept hash is stable and correct. A bounded old-key query had no match, but a separate depicted-key lookup resolves eligible CHEBI:65400. Adoption must await explicit identity adjudication and a consumed repair of its invalid SMILES; current raw/target pins and exact-key collision checks are recorded.

### Genus, species and strain identifier boundaries

scope: supported. Targets: naturalproductmech:mibig-eb25c9b521.

Current NCBI and Wikidata mappings resolve the asserted taxa and preserve their distinct ranks. The deposited locus carries UTEX 1903 metadata; genus-only or species-only occurrences remain distinct from strain-specific producer evidence.

### Predicted filing and separate BGC class scope

identity: supported. Targets: naturalproductmech:mibig-eb25c9b521.

The exact-key NPClassifier output supports Alkaloids filing and the attributed hapalindole/tryptophan classes. The source BGC classes retain their separate annotation meaning.

### Exact named H and stereochemical identity

identity: concern. Targets: naturalproductmech:mibig-eb25c9b521.

The primary named H graph is constitutionally identical but opposite at all four encoded centres. Positive NMR/HRMS assignment does not establish the current enantiomer. Preserve the original absolute-assignment method gap while correcting the representation through the separate identifier finding.

### FamD1 exact H assay and repair dependency

evidence: concern. Targets: naturalproductmech:mibig-eb25c9b521.

The source directly demonstrates the depicted H product using recombinant purified FamD1 from the UTEX 1903 locus. Once the primary-supported identity is adopted through the guarded structure decision, add Enzymatic assays with the existing PMID26629885 and SOURCE_ASSERTION/CLUSTER_DEMONSTRATED. Do not transfer the assay to the current opposite enantiomer. The structure decision already pins the complete original source row; require simultaneous structure-plus-method composition and review classification, cross-references and old-key occurrence provenance. No unchanged-citation overlay is necessary solely to duplicate that guard.

### Native versus recombinant context

evidence: supported. Targets: naturalproductmech:mibig-eb25c9b521.

The original abstract positively establishes biological isolation of named H from cultured Fischerella; the later native UTEX 1903 gene source and purified-protein assay are separate contexts. SOURCE_ASSERTION remains the honest native-producer grade. No native H knockout, de novo whole-cluster heterologous production or exact original Israeli-strain equivalence is asserted.

### Both stored genus-level occurrences

evidence: unknown. Targets: naturalproductmech:mibig-eb25c9b521.

The NP060495R abstract supports named H in Fischerella at genus level; the current enantiomeric source key needs coordinated provenance handling. NP070346O instead describes marine Symploca depsipeptides at inspected abstract/first-page scope. Its exact H occurrence is unresolved rather than proven false solely from a short abstract. Coarse genus rank is source-faithful and is not itself a defect.

### Whole-owner scientific scope and optional claims

completeness: unknown. Targets: naturalproductmech:mibig-eb25c9b521.

All present scientific assertions were reviewed. Original isolation-method and extra occurrence access gaps remain required. The sparse owner has no optional activity table or mechanistic graph; their absence alone does not require additions. Root and identifier packets cover current authorities, computed classification and history.

### Native status and retained seed history

provenance: supported. Targets: naturalproductmech:mibig-eb25c9b521.

The two dated seed events and SEEDED status accurately describe generated provenance. This review does not relabel the owner REVIEWED or treat seed history as scientific approval. Existing discussions, where present, remain part of the evidence to adjudicate.

### Optional mechanism and application content

completeness: not_applicable. Targets: naturalproductmech:mibig-eb25c9b521.

The owner does not assert pathway steps, causal edges, organism-specific proteins, molecular targets, bioactivities or synthetic-biology applications. Their absence alone is not a defect in this source-generated record. No enzyme, target, activity or engineering claim is inferred from the congener name or chemical class.

### Structured transcriptomic context

completeness: not_applicable. Targets: naturalproductmech:mibig-eb25c9b521.

iModulonDB is not applicable for the named cyanobacterial producer and occurrence organisms in the inspected dataset catalogue. No matching organism/dataset supports a gene or module lookup. This coverage limit is not negative evidence about natural-product production or function.

## Findings

### ID056-F-ENANTIOMER: The stored H enantiomer disagrees with the explicit primary product drawing

blocker / open / confirmed; issue key: ambiguine-h-primary-depiction-enantiomer-and-unsafe-chebi-representation.

The owner encodes DBOXZAYTFKDLHJ-KPQBMEGNSA-N, whereas 2015 SI S6 explicitly named ambiguine H and current three-star CHEBI:65400 MOL/InChI encode DBOXZAYTFKDLHJ-CSOFANMDSA-N. Every one of four corresponding centres is opposite. The 2015 FamD1 result therefore cannot be unconditionally attached to the stored enantiomer. This confirms a representation/evidence disagreement, not new absolute experimental proof; the original 2007 full methods remain unavailable. Repair has a concrete additional prerequisite: both the committed target SMILES and current default SMILES contain an aromatic representation that RDKit cannot kekulize, despite valid agreeing MOL/InChI. The present correction loader would accept and copy that invalid text.

## Recommended Actions And Acceptance Checks

### ID056-ACTION-IDENTITY

Adjudicate the explicit source depiction, then implement a consumed representation extension before using REPLACE_WITH_CHEBI for BGC0001612:1 version 3. Pin complete original row SHA256 6eb7dabb0ddacef8fad927b861aa73dead7e1652ee9ef1696912f6cead6524c7 and complete CHEBI:65400 target row SHA256 e3907f95f890384299169cb7564df91125532d6cc9ee0e579cb0dfda76ad961b; preserve both raw inventories unchanged. The existing target SMILES is invalid and must not be copied. Extend the maintained correction schema/consumer to accept an explicitly attributed alternative isomeric SMILES derived from the pinned official MOL SHA256 00cc7baed9ee239a18c806c5c842288bc63a6ac568857780db7c50806991a882, and enforce MOL/SMILES/Standard-InChI full-key and fixed-H agreement with DBOXZAYTFKDLHJ-CSOFANMDSA-N, formula C26H32N2, charge zero and four complete centres. The derived candidate string is [C-]#[N+][C@@H]1[C@@H]2c3c(C(C)(C)C=C)[nH]c4cccc(c34)C(C)(C)[C@H]2CC[C@]1(C)C=C. Such fields are a required implementation change, not a presently consumed option. Retain curator, actual decision date and DOI:10.1021/jacs.5b10136 plus the original-assignment limitation. Once this exact graph is adopted, compose a method REPLACE for the same minted source concept with Enzymatic assays; the paired structure decision supplies the enforced full-row guard. Keep SOURCE_ASSERTION for native production and use CLUSTER_DEMONSTRATED only for the purified FamD1 product assay. The existing PMID26629885 already names that study. Do not add a redundant claim-reference overlay solely for guarding; if citation, strain or isolate overlays are introduced later, first implement/test their presently rejected structure-correction composition. Clear old NPAtlas/source xrefs, never transfer old-key LOTUS rows or classifier output by name, and regenerate through the normal seed pathway.

- Reject changed source/target row digests, MOL snapshot, selected key, graph or stereochemistry; verify unique source/target and zero colliding MIBiG/current owners. Candidate target digest is e3907f95f890384299169cb7564df91125532d6cc9ee0e579cb0dfda76ad961b; existing consumer acceptance in the diagnostic is not safe chemistry validation.
- Reconcile candidate-key classification explicitly: current NPClassifier has only the old key. Obtain an attributed valid new-key classification through the documented source workflow and verify resulting Alkaloids filing, rather than silently losing classification or copying the old-key row. Expected grounded identity is CHEBI:65400; use documented canonical owner/PATHS migration and preserve the minted MIBiG source concept.
- Old-key LOTUS rows have full selectors/digests in the diagnostic and remain in provenance; they must not be automatically copied to the new enantiomer. Corrected-key ChEBI origin is genus Fischerella/PMID17315959, with no strain. Its full row SHA256 is d83184c1cea3ea1760e713a8353ba4bded2b4847cee47074f42b186e039112ee. Reconcile original 2007 and extra malevamide citation limitations claim by claim.
- The candidate key has an existing pinned AntibioticMech CHEBI:65400 link at commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976, raw-row SHA256 0b241499005f913f580c9675ec175f2c65925cb6b4e7bd5f81d08da804f8424b. A generated SAME_STRUCTURE link may use that exact-key bridge after repair; do not transfer its mechanisms or imply a newly inspected sibling owner.
- Exercise structure + method composition together: the full raw source pin must fail on any field drift, empty original methods must not be mistaken for pre-existing assays, and the resulting grades must be SOURCE_ASSERTION/CLUSTER_DEMONSTRATED without native knockout or de novo whole-cell production claims.
- Run strict target chemistry/schema, provenance, corpus integrity, exact reproduction and required QC after authorized implementation. Keep review completion partial until required original-isolation and extra-citation access gaps are resolved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ID056-OWNER | /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/ambiguine-h-isonitrile.yaml; Entire generated owner and complete resolved local source packet | supports | The owner stores ambiguine H isonitrile, C26H32N2, net formal charge 0, full key DBOXZAYTFKDLHJ-KPQBMEGNSA-N and 4 assigned tetrahedral centres. The stereochemistry-completeness flag describes the encoded graph; it does not independently prove a historical absolute assignment. |
| ID056-COMPARISON | /private/tmp/npm-review-work/056/identity/identifier-comparison.json; Independently parsed owner and source graphs; complete exact-key inventory projections; full-row digests and source-concept hash | supports | 7 independently parsed representations were compared by full Standard and fixed-H InChI, formula and formal charge. All agree: True and fixed-H agreement: True. The exact MIBiG row is BGC0001612:1 version 3, canonical complete-row SHA256 6eb7dabb0ddacef8fad927b861aa73dead7e1652ee9ef1696912f6cead6524c7. Hashing MIBIG, a NUL separator and BGC0001612:1 reproduces naturalproductmech:mibig-eb25c9b521; the key is a source-concept hash, not a chemical-graph hash. |
| ID056-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0001612.3/annotations.json; Complete retained response, exact relevant identifier and structure fields | supports | The official snapshot resolves BGC0001612:1 version 3 with its exact named structure and explicit identifiers. Status is active, quality questionable and completeness unknown. It names taxon NCBITaxon:230521 and accession KX451322.1. Source location 0/0 is unspecified and is not converted to a curated full-accession interval. Entry-level methods remain database assertions pending the separate primary congener-specific assessment. |
| ID056-XREF-1 | https://www.npatlas.org/api/v1/compound/NPA018261; Complete retained response, exact relevant identifier and structure fields | supports | Literal source identifier npatlas:NPA018261 resolves to the retained exact record. Its full standardized graph agrees with the owner in the independent comparison. The returned canonical identifier is NPA018261; any legacy spelling is an observed resolving alias, not guessed padding. Database origin metadata is not independent primary support for a strain or absolute assignment. |
| ID056-CHEBI-SEARCH | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=DBOXZAYTFKDLHJ-KPQBMEGNSA-N&amp;size=100; Complete exact-key endpoint result and response receipt | supports | The exact full-key request returned an explicit no-compound-match response. This is a successful bounded negative search for this submitted key, not universal absence by name or across authorities. |
| ID056-WIKI-CHEM-Q104246384 | https://www.wikidata.org/wiki/Special:EntityData/Q104246384.json; Entity label and all P234/P235/P2017 chemical identity claims | supports | The exact LOTUS-linked compound Q104246384 has an InChIKey/Standard InChI and isomeric SMILES that were checked against this owner's complete stereochemical graph. Non-isomeric SMILES is not substituted for the explicit stereochemical property. |
| ID056-TAXON-STRAIN | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=230521&amp;retmode=xml; Complete top-level Taxon name/rank/parent/other names and lineage | supports | NCBI 230521 is strain-ranked Fischerella ambigua UTEX 1903 beneath species 56108 and genus 1190. Fischerella sp. UTEX 1903 is an explicit equivalent name. This does not identify an unspecified Fischerella isolation culture as UTEX 1903. |
| ID056-TAXON-OCCURRENCES | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1190,210996,56108&amp;retmode=xml; Complete top-level requested Taxon records, names, ranks, parent IDs and lineage | supports | NCBI 1190 is genus Fischerella, 56108 is species Fischerella ambigua (Scytonema ambiguum synonym), and 210996 is species Hapalosiphon delicatulus. All are cyanobacterial. Their ranks and names are kept separate from strain 230521 and from primary isolation identity. |
| ID056-WIKI-TAX-Q27438671 | https://www.wikidata.org/wiki/Special:EntityData/Q27438671.json; English label, scientific name and all P685 taxonomy claims | supports | LOTUS organism Q27438671 resolves to Fischerella; explicit P685 values 1190 agree with the row's NCBI identifiers 1190. This confirms identifier mapping rather than occurrence or strain production. |
| ID056-GENBANK | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=KF664586.1,KX451322.1&amp;rettype=gb&amp;retmode=text; Complete KX451322.1 header, publication identifiers and source feature qualifiers; no whole-sequence translation or construct equivalence claim | supports | KX451322.1 is 41,276 bp and identifies Fischerella ambigua UTEX 1903, strain qualifier UTEX 1903, taxon:230521. Its publication bridge and source metadata resolve the deposited locus. The whole sequence length does not supply missing MIBiG interval coordinates, prove exact-congener enzyme chemistry, or establish equivalence to the other amb/fam submission. |
| ID056-SEARCH | /private/tmp/npm-review-work/056/identity/local-search.txt; All returned ignored-inclusive current corpus, curation and configuration matches | supports | The exact full key, minted identifier and filing slug match the current owner and PATHS mapping. The inspected matches contain no additional owner or maintained decision for this exact target within the searched paths. Complete relevant inventories were separately parsed in the comparison. |
| ID056-CLASS | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Complete exact-key classifier row | context_only | The pinned NPClassifier npclassifier.gnps2.org@2026-09-07 row records ['Alkaloids'], ['Tryptophan alkaloids'] and ['Hapalindole alkaloids'], with glycoside=False. The single Alkaloids pathway maps to the alkaloids path. MIBiG ['OTHER'] is a separate BGC classification, not a contradictory predicted chemical filing. |
| ID056-SEED | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; mint_identifier, choose_pathway, three-star structure lookup and MIBiG source-concept projection | context_only | The consumed seed code hashes the source tag and accession:index, selects filing from a unique predicted pathway, matches eligible ChEBI by full key and retains source concept IDs independently of the graph. These are the actual transformation semantics used to assess the stored grounding. |
| ID056-PRIMARY-H | DOI:10.1021/jacs.5b10136; Official SI S6 Figure 3 labelled H product; source pixels independently viewed | refutes | The published product drawing explicitly encodes C10S, C11R, C12R and C15S. This differs at all four centres from the owner, while constitution and formula agree. It is a direct source-depiction comparison, not independent experimental proof of absolute configuration. |
| ID056-DEPICTION | /private/tmp/npm-review-work/056/primary-2015-S6-H-comparison.json; Complete transcription, numbering, stereo directions and derived graph; independent visual and code QA | refutes | Erasing all input stereo and transcribing the four observed wedges/dashes gives DBOXZAYTFKDLHJ-CSOFANMDSA-N. The official ChEBI MOL and Standard InChI give the same complete Standard/fixed-H graph. S25 alone omits one explicit centre; no enantiomeric conclusion is derived from achiral NMR. |
| ID056-CANDIDATE-JSON | https://www.ebi.ac.uk/chebi/backend/api/public/compound/65400/; Entire official entry metadata or MOL atom/bond graph | supports | Current CHEBI:65400 is three-star ambiguine H. The MOL and Standard InChI encode the primary depicted CSOFANMD enantiomer. The entry attributes genus Fischerella, NCBITaxon:1190, to PMID17315959 and does not identify an isolation strain. Its default SMILES has a separate invalid aromatic representation. |
| ID056-CANDIDATE-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/65400/; Entire official entry metadata or MOL atom/bond graph | supports | Current CHEBI:65400 is three-star ambiguine H. The MOL and Standard InChI encode the primary depicted CSOFANMD enantiomer. The entry attributes genus Fischerella, NCBITaxon:1190, to PMID17315959 and does not identify an isolation strain. Its default SMILES has a separate invalid aromatic representation. |
| ID056-CANDIDATE-GUARDS | /private/tmp/npm-review-work/056/identity/proposed-guard-composition.json; Complete source/target rows, row SHA pins, original-key and corrected-key joins, current consumer simulation | partial | The existing correction consumer accepts the pinned target and composes with a method REPLACE, but copies target SMILES that RDKit cannot kekulize. This diagnostic therefore explicitly marks safe_to_execute=false. Candidate key is unique in eligible ChEBI and absent from all MIBiG rows. No candidate current owner was found in the recorded ignored-inclusive search. Corrected-key LOTUS/Cyano/classifier joins are empty; one exact-key ChEBI genus occurrence and one pinned AntibioticMech link exist. |
| ID056-REPAIR-CODE | src/naturalproductmech/curate/structure_corrections.py; scripts/extract_chebi.py; scripts/seed_from_sources.py; src/naturalproductmech/curate/claim_references.py; Complete relevant consumers and extractor; actual code hashes in diagnostic | context_only | The ChEBI extractor copies default SMILES without parsing. REPLACE_WITH_CHEBI pins full raw and target rows but copies that SMILES without chemistry validation. A paired correction enforces the full original-row digest before the method REPLACE, which by itself does not enforce expected fields. Existing claim-reference, strain and isolate overlays reject structure-corrected rows; any additional overlay requires explicit reviewed composition, not invented columns. |
| S056-E-LOCAL | data/natural_products/alkaloids/ambiguine-h-isonitrile.yaml; Whole owner and resolved local source projection | supports | Exact H owner DBOXZAYTFKDLHJ-KPQBMEGNSA-N encodes four assigned centres. BGC0001612:1 version 3 asserts UTEX 1903, KX451322.1, PMID:26629885, empty bounds and empty methods, giving SOURCE_ASSERTION/CLUSTER_UNSTATED. Both LOTUS genus-level DOI rows were read separately. The canonical complete raw MIBiG row digest is 6eb7dabb0ddacef8fad927b861aa73dead7e1652ee9ef1696912f6cead6524c7. |
| S056-E-2015 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=4681624; DOI:10.1021/jacs.5b10136; full main body and figures/captions | supports | The study sequences the fam locus from Fischerella ambigua UTEX 1903 and reports that only FamD1 prenylates supplied hapalindole U with DMAPP to ambiguine H. FamD1/D2 are purified His-tagged proteins expressed in E. coli. The separate FamD2/FamC1 cyclase endpoint is 12-epi-hapalindole U; it is not an H whole-pathway or native knockout experiment. |
| S056-E-SI | https://ndownloader.figshare.com/files/3731911; Official 2015 SI, S2-S4 cloning/purification/assays; S6 Figure 3; S25 H NMR and HRMS | supports | Genes were amplified from UTEX 1903 DNA, cloned in pET28a and expressed in E. coli BL21(DE3). Hapalindole U was supplied by Phil Baran. Only the FamD1 + hapalindole U + DMAPP assay forms the labelled H peak; GPP and FamD2 comparisons do not. Product was isolated from a scaled 5 mL assay; S25 compares proton NMR with the 2007 H spectrum and reports [M+H]+ 373.2638 calculated and found. This is purified-enzyme evidence for the depicted product, not native H isolation or whole-cell heterologous synthesis. |
| S056-E-DRAWING | /private/tmp/npm-review-work/056/primary-2015-S6-H-comparison.json; S6 labelled H product; four independently transcribed stereo bonds and per-atom mapping | refutes | The complete S6 product drawing has C10S, C11R, C12R and C15S. After erasing all input stereo and entering its observed wedges/dashes, the graph gives DBOXZAYTFKDLHJ-CSOFANMDSA-N. All four corresponding owner centres are inverted. S25 explicitly shows only three centres, so the full comparison uses S6; achiral NMR alone is not used to establish an enantiomer. The identity packet owns the single structural finding. |
| S056-E-2007 | https://pubmed.ncbi.nlm.nih.gov/17315959/; Original abstract, exact H/I/J names, culture description | partial | The original DOI10.1021/np060495r abstract names H as compound 1 among new H-I-J isolates from cultured Fischerella sp. collected in Israel. The abstract supports the genus-level named occurrence but does not supply a UTEX 1903 bridge or the original absolute-versus-relative assignment procedure. |
| S056-E-2007-GAP | https://doi.org/10.1021/np060495r; Bounded original body and SI access; institutional abstract and archive searches | unknown | The original 2007 full paper and supplement remain unavailable. The later 2015 supplement reprints an H spectrum and supplies a complete product drawing, but does not substitute for direct inspection of all original culture and stereochemical methods. |
| S056-E-MALEVAMIDE | https://pubmed.ncbi.nlm.nih.gov/18361518/; Original abstract of stored extra DOI10.1021/np070346o | unknown | This article is Isolation and Structure Determination of Malevamide E, a Dolastatin 14 Analogue, from the Marine Cyanobacterium Symploca laete-viridis. Its original abstract describes malevamide E and dolastatin 14 from field-collected Symploca, not the asserted H/Fischerella pair. Indexed original first-page text is consistent. The entire paper was not obtained, so this is a suspicious citation association rather than demonstrated absence of H from its complete contents. |
| S056-E-NEW-GAP | https://doi.org/10.1021/np070346o; Recorded new citation retrieval receipt | unknown | The positive full-PDF mirror lead could not be reached and no full body was inspected. The empty failed PDF artifact is not treated as a source. The extra occurrence must remain citation-specifically unverified pending original content or a proven source mapping error. |
| S056-E-CONSUMERS | scripts/seed_from_sources.py; src/naturalproductmech/curate/claim_references.py; src/naturalproductmech/grading.py; Method REPLACE and WITHDRAW application; SHA guard and structure-correction rejection | supports | Enzymatic assays maps to CLUSTER_DEMONSTRATED while retaining SOURCE_ASSERTION. H may receive this exact-product evidence only together with the approved primary-backed structure correction. The paired REPLACE_WITH_CHEBI decision enforces the complete original MIBiG row SHA256; an accompanying method REPLACE may rely on that active consumed guard rather than adding a redundant claim-reference row. The existing PMID26629885 remains correct. The eligible ChEBI representation must first be made parseable under the independently specified identity repair, and tests must require the structure and method decisions together. A future citation overlay would need an explicit composition contract because the current claim-reference consumer rejects structure_correction_note. |
| R056-OWNER | data/natural_products/alkaloids/ambiguine-h-isonitrile.yaml; Complete owner YAML, including both history entries, all source claims and any discussions | supports | Root read the complete ambiguine H isonitrile owner after its individual intake. It has one MIBiG source concept, 2 occurrence entries, one producer and one locus. There are no inline or referenced mechanism graphs, pathway steps, molecular targets, bioactivity rows or synthetic-biology applications in this owner. The complete parsed owner was inspected; ignored-file filters were not used to infer field absence. |
| R056-LOCAL-SOURCES | /private/tmp/npm-review-work/056/local-sources.json; Complete target-specific MIBiG, LOTUS, CyanoMetDB, ChEBI and NPClassifier slices | context_only | Root read every matching local source row and compared it with the complete emitted owner. The separate scientific and identifier assessments decide claim support; deterministic reproduction does not establish primary evidence. |
| R056-IMODULON-DATASETS | /private/tmp/npm-review-work/010/imodulon-datasets.txt; Complete 28-row dataset catalogue; actual command receipt in 010/imodulon-context-receipts.json | context_only | The successful structured-adapter dataset listing retrieved at 07:21:15 UTC was fully re-read for this target. It contains no Fischerella or Hapalosiphon dataset, including no UTEX 1903 match. This same-session catalogue is reused with its original retrieval time; a fresh request is not claimed. |

## Limits And Additional Notes

- Agreement between authority structures does not independently establish the absolute configuration or organism of the original isolated material; primary source limitations are assessed separately.
- GenBank header/source verification establishes accession metadata, not equivalence of whole amb/fam sequences, assay constructs or congener-specific enzymatic function.
- The old-key ChEBI negative query and depicted-key positive query have distinct scopes. Three-star status does not validate every serialized representation.
- The original 2007 full isolation and absolute-assignment methods remain unavailable; the observed later drawing/authority agreement does not replace experimental stereochemical proof.
- The 2007 full isolation paper and SI remain unavailable; exact original culture accession and absolute stereochemical assignment procedure were not inferred from later database records.
- The 2015 assay establishes the depicted named H product. Its complete drawing disagrees with the owner enantiomer; achiral NMR/HRMS cannot resolve that discrepancy alone.
- The extra malevamide article was inspected at original abstract and indexed first-page scope only; no whole-paper absence claim or automatic occurrence exclusion follows.
- This review audits the present assertions and the concrete source questions they raise; it does not claim exhaustive discovery of every later activity or biosynthetic study. Optional enrichment remains distinct from correcting an unsupported current assertion.
- The configured identifier-label gate accepts 499 warning-level mismatches and 35 explicit exceptions and skips 4,744 no-adapter pairs; exit 0 does not independently verify every identifier or scientific claim.
- The quality suite reports 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). Skipped tests are not counted as passing tests. Existing ontology caches were used; no multi-gigabyte cache download was required.
- Native gates assess deterministic consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy, or literature-level claim support.
- The five reused gates retain their batch004 execution times and cached ontology results. Reuse establishes unchanged repository inputs; it is not a new remote authority query or new assertion of ontology freshness.
- The ignored-inclusive check enumerates record and saved-review YAML paths, and all tracked files are hashed. Generated Python bytecode and external tool caches are not claimed to have been independently byte-pinned at the prior execution.
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
review_id: 20261021T120745Z-ambiguine-h-isonitrile
title: 'Ambiguine H isonitrile: resolve enantiomer conflict before attaching enzyme
  evidence'
started_at: '2026-10-21T11:52:43.452347Z'
finished_at: '2026-10-21T12:07:45.738073Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The stored four-centre H graph agrees with MIBiG, NPAtlas and Wikidata, but
  the explicitly named 2015 product drawing and eligible ChEBI MOL/InChI encode the
  opposite enantiomer. This exact-identity conflict blocks accepting the named product.
  The candidate ChEBI SMILES is also invalid, so repair requires a consumed valid
  representation before a guarded structure/method composition. FamD1 directly forms
  the depicted H and its method can be added only with that identity repair. Original
  2007 assignment methods and the extra occurrence citation remain incompletely verified.
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
  - path: data/natural_products/alkaloids/ambiguine-h-isonitrile.yaml
    sha256: f1d2f802102e93cfcdf367a7d501e2abbd349f071dddd48865e2cf4657095b7c
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
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
  - path: data/raw/pathwaymech_products.tsv
    sha256: 28ff699b83648614928f7ea5d8e8f5aee49a34ebbc9b6e9dbfece255383b7e04
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
  - path: src/naturalproductmech/grading.py
    sha256: ece54c4a2c0803f034ac59de51b1006cf79ea8d6b6256d75757d4adb88ea9630
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 56, batch 006, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated pending-PR targets.
    At selection, 104 of 3116 current records had campaign coverage and 3012 remained.
    The population search included ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-eb25c9b521
targets:
- target_id: naturalproductmech:mibig-eb25c9b521
  path: data/natural_products/alkaloids/ambiguine-h-isonitrile.yaml
  label: ambiguine H isonitrile
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
  - naturalproductmech:mibig-eb25c9b521
  command: just validate-strict data/natural_products/alkaloids/ambiguine-h-isonitrile.yaml
    --out /private/tmp/npm-review-work/056/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T11:52:46.307649Z
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
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055340+00:00;
    finished 2026-10-21T09:55:22.727768+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/verify-corpus.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-corpus.log. Reused
    for batch006 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch006. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
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
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055361+00:00;
    finished 2026-10-21T09:56:44.050706+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/verify-reproduction.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-reproduction.log.
    Reused for batch006 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch006. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
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
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.057401+00:00;
    finished 2026-10-21T09:54:38.468783+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/review-queue.json;
    transcript: /private/tmp/npm-native-checks/batch-004/review-queue.log. Reused
    for batch006 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch006. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
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
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.061733+00:00;
    finished 2026-10-21T09:56:36.296159+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/validate-products.json;
    transcript: /private/tmp/npm-native-checks/batch-004/validate-products.log. Reused
    for batch006 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch006. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
- check_id: shared-qc
  name: Full repository quality gate on the current main baseline
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed on the unchanged main baseline
    during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21).
    All configured lint, governance, documentation, provenance, source-queue, schema,
    rendering, reproduction, filing-integrity and reporting stages completed successfully.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:30.560925+00:00;
    finished 2026-10-21T10:04:44.806799+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/qc.json;
    transcript: /private/tmp/npm-native-checks/batch-004/qc.log. Reused for batch006
    only after a fresh fetch/clean branch, equal commit/tree and two reads of all
    9,182 tracked byte streams and modes (208,070,649 bytes), including a recheck
    after the fresh authoritative catalogue. This gate was not rerun for batch006.
    Original execution times, scope, warnings, exceptions and skips are retained.'
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
- check_id: ID056-CHEMICAL-CHECK
  name: Exact authority structure and fixed-H comparison
  status: passed
  required: true
  summary: Compared 7 representations against the owner; full Standard/fixed-H agreement
    is explicitly recorded.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - ID056-COMPARISON
  - ID056-CHEBI-SEARCH
- check_id: ID056-SOURCE-CHECK
  name: Complete raw rows, source-concept hash and local identity collision scan
  status: passed
  required: true
  summary: All complete local source projections match the independently parsed committed
    inventories; source row SHA256 and minted identifier are reproduced, and the current
    ignored-inclusive exact-identity matches were inspected.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - ID056-COMPARISON
  - ID056-SEARCH
  - ID056-SEED
- check_id: ID056-DEPICTED-IDENTITY
  name: Named H primary depiction and eligible authority versus owner
  status: failed
  required: true
  summary: The four-centre primary H depiction and eligible ChEBI graph are the owner
    enantiomer; the current target representation also cannot safely be consumed unchanged.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - ID056-PRIMARY-H
  - ID056-DEPICTION
  - ID056-CANDIDATE-GUARDS
- check_id: S056-C-IDENTITY
  name: Primary H depiction versus current exact owner
  status: failed
  required: true
  summary: The primary four-centre H product drawing is the opposite enantiomer to
    the current owner; identifier packet carries the single structural finding.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - S056-E-DRAWING
  - S056-E-SI
- check_id: S056-C-PRIMARY
  name: Original H isolation and extra occurrence citation
  status: unavailable
  required: true
  summary: Original 2007 methods and the extra malevamide citation full body remain
    unavailable; completion remains partial.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - S056-E-2007-GAP
  - S056-E-NEW-GAP
- check_id: R056-FULL-OWNER
  name: Complete owner and component scope
  status: passed
  required: true
  summary: The complete owner and all present fields were read. The parsed component-reference
    set is empty, so no referenced component was omitted. All existing inspection
    input hashes still match.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - R056-OWNER
  - R056-LOCAL-SOURCES
evidence:
- evidence_id: ID056-OWNER
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/ambiguine-h-isonitrile.yaml
  locator: Entire generated owner and complete resolved local source packet
  accessed_at: '2026-10-21T11:59:22.093626Z'
  support: supports
  summary: The owner stores ambiguine H isonitrile, C26H32N2, net formal charge 0,
    full key DBOXZAYTFKDLHJ-KPQBMEGNSA-N and 4 assigned tetrahedral centres. The stereochemistry-completeness
    flag describes the encoded graph; it does not independently prove a historical
    absolute assignment.
  snapshot_sha256: f1d2f802102e93cfcdf367a7d501e2abbd349f071dddd48865e2cf4657095b7c
- evidence_id: ID056-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/056/identity/identifier-comparison.json
  locator: Independently parsed owner and source graphs; complete exact-key inventory
    projections; full-row digests and source-concept hash
  accessed_at: '2026-10-21T11:59:17.350118Z'
  support: supports
  summary: '7 independently parsed representations were compared by full Standard
    and fixed-H InChI, formula and formal charge. All agree: True and fixed-H agreement:
    True. The exact MIBiG row is BGC0001612:1 version 3, canonical complete-row SHA256
    6eb7dabb0ddacef8fad927b861aa73dead7e1652ee9ef1696912f6cead6524c7. Hashing MIBIG,
    a NUL separator and BGC0001612:1 reproduces naturalproductmech:mibig-eb25c9b521;
    the key is a source-concept hash, not a chemical-graph hash.'
  snapshot_sha256: dfb45d16daea30e1f42e61eeb8d4af53c339f4dc520c80e809c9b620c6a3c75a
- evidence_id: ID056-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0001612.3/annotations.json
  locator: Complete retained response, exact relevant identifier and structure fields
  accessed_at: '2026-10-21T11:35:21.027845Z'
  support: supports
  summary: The official snapshot resolves BGC0001612:1 version 3 with its exact named
    structure and explicit identifiers. Status is active, quality questionable and
    completeness unknown. It names taxon NCBITaxon:230521 and accession KX451322.1.
    Source location 0/0 is unspecified and is not converted to a curated full-accession
    interval. Entry-level methods remain database assertions pending the separate
    primary congener-specific assessment.
  snapshot_sha256: e58c0037e493229d5539485492086e4692905dce80cf507b3baba0c0fc421166
- evidence_id: ID056-XREF-1
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA018261
  locator: Complete retained response, exact relevant identifier and structure fields
  accessed_at: '2026-10-21T11:35:27.187590Z'
  support: supports
  summary: Literal source identifier npatlas:NPA018261 resolves to the retained exact
    record. Its full standardized graph agrees with the owner in the independent comparison.
    The returned canonical identifier is NPA018261; any legacy spelling is an observed
    resolving alias, not guessed padding. Database origin metadata is not independent
    primary support for a strain or absolute assignment.
  snapshot_sha256: 3fadbaebdec0d7e23f2800c4b32c13d7b9ba73f92d448507571c96fe43273eb9
- evidence_id: ID056-CHEBI-SEARCH
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=DBOXZAYTFKDLHJ-KPQBMEGNSA-N&size=100
  locator: Complete exact-key endpoint result and response receipt
  accessed_at: '2026-10-21T11:35:27.132164Z'
  support: supports
  summary: The exact full-key request returned an explicit no-compound-match response.
    This is a successful bounded negative search for this submitted key, not universal
    absence by name or across authorities.
  snapshot_sha256: 078ab9af79309c508223ffe9b6469916c92609499a3d11d3dea2b1412e9ed6be
- evidence_id: ID056-WIKI-CHEM-Q104246384
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q104246384.json
  locator: Entity label and all P234/P235/P2017 chemical identity claims
  accessed_at: '2026-10-21T11:59:09.925085Z'
  support: supports
  summary: The exact LOTUS-linked compound Q104246384 has an InChIKey/Standard InChI
    and isomeric SMILES that were checked against this owner's complete stereochemical
    graph. Non-isomeric SMILES is not substituted for the explicit stereochemical
    property.
  snapshot_sha256: b9e2e3abde330091bf756f45812c8d9fa9579f5334af38376e79281f391b22bb
- evidence_id: ID056-TAXON-STRAIN
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=230521&retmode=xml
  locator: Complete top-level Taxon name/rank/parent/other names and lineage
  accessed_at: '2026-10-21T11:35:21.028483Z'
  support: supports
  summary: NCBI 230521 is strain-ranked Fischerella ambigua UTEX 1903 beneath species
    56108 and genus 1190. Fischerella sp. UTEX 1903 is an explicit equivalent name.
    This does not identify an unspecified Fischerella isolation culture as UTEX 1903.
  snapshot_sha256: 84b3ff21a49675b724449bf16c412bb6880913a14b9f9903ab3489f0510a4c67
- evidence_id: ID056-TAXON-OCCURRENCES
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1190,210996,56108&retmode=xml
  locator: Complete top-level requested Taxon records, names, ranks, parent IDs and
    lineage
  accessed_at: '2026-10-21T11:54:07.054060Z'
  support: supports
  summary: NCBI 1190 is genus Fischerella, 56108 is species Fischerella ambigua (Scytonema
    ambiguum synonym), and 210996 is species Hapalosiphon delicatulus. All are cyanobacterial.
    Their ranks and names are kept separate from strain 230521 and from primary isolation
    identity.
  snapshot_sha256: 5227e567b8e4bc66783de8101d68963bbafa29b7ed7ce183f6dc3d519cb3fa43
- evidence_id: ID056-WIKI-TAX-Q27438671
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q27438671.json
  locator: English label, scientific name and all P685 taxonomy claims
  accessed_at: '2026-10-21T11:54:06.799480Z'
  support: supports
  summary: LOTUS organism Q27438671 resolves to Fischerella; explicit P685 values
    1190 agree with the row's NCBI identifiers 1190. This confirms identifier mapping
    rather than occurrence or strain production.
  snapshot_sha256: b051c935aa9cad66d1df3e6b261376ca39de5b9e7eddd50a2c817242f4cb3bd8
- evidence_id: ID056-GENBANK
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=KF664586.1,KX451322.1&rettype=gb&retmode=text
  locator: Complete KX451322.1 header, publication identifiers and source feature
    qualifiers; no whole-sequence translation or construct equivalence claim
  accessed_at: '2026-10-21T11:35:21.028304Z'
  support: supports
  summary: KX451322.1 is 41,276 bp and identifies Fischerella ambigua UTEX 1903, strain
    qualifier UTEX 1903, taxon:230521. Its publication bridge and source metadata
    resolve the deposited locus. The whole sequence length does not supply missing
    MIBiG interval coordinates, prove exact-congener enzyme chemistry, or establish
    equivalence to the other amb/fam submission.
  snapshot_sha256: 7ccdab82716749e3ae45c09f74e84e852ff969ff243275522a9e8d6c4e164391
- evidence_id: ID056-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/056/identity/local-search.txt
  locator: All returned ignored-inclusive current corpus, curation and configuration
    matches
  accessed_at: '2026-10-21T11:59:17.349978Z'
  support: supports
  summary: The exact full key, minted identifier and filing slug match the current
    owner and PATHS mapping. The inspected matches contain no additional owner or
    maintained decision for this exact target within the searched paths. Complete
    relevant inventories were separately parsed in the comparison.
  snapshot_sha256: 92423a1abedd353d79023ce8bf5b7204e4ea8a68ca17436f04fef4f119f9bb98
  search_scope: rg --no-ignore --hidden -n -F -e DBOXZAYTFKDLHJ-KPQBMEGNSA-N -e naturalproductmech:mibig-eb25c9b521
    -e ambiguine-h-isonitrile data/natural_products curation conf
- evidence_id: ID056-CLASS
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Complete exact-key classifier row
  accessed_at: '2026-10-21T11:59:22.093626Z'
  support: context_only
  summary: The pinned NPClassifier npclassifier.gnps2.org@2026-09-07 row records ['Alkaloids'],
    ['Tryptophan alkaloids'] and ['Hapalindole alkaloids'], with glycoside=False.
    The single Alkaloids pathway maps to the alkaloids path. MIBiG ['OTHER'] is a
    separate BGC classification, not a contradictory predicted chemical filing.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: ID056-SEED
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: mint_identifier, choose_pathway, three-star structure lookup and MIBiG
    source-concept projection
  accessed_at: '2026-10-21T11:59:22.093626Z'
  support: context_only
  summary: The consumed seed code hashes the source tag and accession:index, selects
    filing from a unique predicted pathway, matches eligible ChEBI by full key and
    retains source concept IDs independently of the graph. These are the actual transformation
    semantics used to assess the stored grounding.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: ID056-PRIMARY-H
  kind: primary_source
  reference: DOI:10.1021/jacs.5b10136
  locator: Official SI S6 Figure 3 labelled H product; source pixels independently
    viewed
  accessed_at: '2026-10-21T11:29:18.239895Z'
  support: refutes
  summary: The published product drawing explicitly encodes C10S, C11R, C12R and C15S.
    This differs at all four centres from the owner, while constitution and formula
    agree. It is a direct source-depiction comparison, not independent experimental
    proof of absolute configuration.
  snapshot_sha256: 9b91ab700a8f3fb72dac76b8ab6d9ef2d2b868a0e67402c613f76bbc9071108a
- evidence_id: ID056-DEPICTION
  kind: validation
  reference: /private/tmp/npm-review-work/056/primary-2015-S6-H-comparison.json
  locator: Complete transcription, numbering, stereo directions and derived graph;
    independent visual and code QA
  accessed_at: '2026-10-21T11:59:38.823660Z'
  support: refutes
  summary: Erasing all input stereo and transcribing the four observed wedges/dashes
    gives DBOXZAYTFKDLHJ-CSOFANMDSA-N. The official ChEBI MOL and Standard InChI give
    the same complete Standard/fixed-H graph. S25 alone omits one explicit centre;
    no enantiomeric conclusion is derived from achiral NMR.
  snapshot_sha256: ce6e5c9ad98ec749d4ea1a68fe9d4c2f33908c54e522649d3b15ded363130b3d
- evidence_id: ID056-CANDIDATE-JSON
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/65400/
  locator: Entire official entry metadata or MOL atom/bond graph
  accessed_at: '2026-10-21T12:02:18.049335Z'
  support: supports
  summary: Current CHEBI:65400 is three-star ambiguine H. The MOL and Standard InChI
    encode the primary depicted CSOFANMD enantiomer. The entry attributes genus Fischerella,
    NCBITaxon:1190, to PMID17315959 and does not identify an isolation strain. Its
    default SMILES has a separate invalid aromatic representation.
  snapshot_sha256: 014320675ee6df7e5d900f47640279fa659cfea755bcac93c9a6ce3a4717f60a
- evidence_id: ID056-CANDIDATE-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/65400/
  locator: Entire official entry metadata or MOL atom/bond graph
  accessed_at: '2026-10-21T12:02:18.887171Z'
  support: supports
  summary: Current CHEBI:65400 is three-star ambiguine H. The MOL and Standard InChI
    encode the primary depicted CSOFANMD enantiomer. The entry attributes genus Fischerella,
    NCBITaxon:1190, to PMID17315959 and does not identify an isolation strain. Its
    default SMILES has a separate invalid aromatic representation.
  snapshot_sha256: 00cc7baed9ee239a18c806c5c842288bc63a6ac568857780db7c50806991a882
- evidence_id: ID056-CANDIDATE-GUARDS
  kind: validation
  reference: /private/tmp/npm-review-work/056/identity/proposed-guard-composition.json
  locator: Complete source/target rows, row SHA pins, original-key and corrected-key
    joins, current consumer simulation
  accessed_at: '2026-10-21T12:04:52.931287Z'
  support: partial
  summary: The existing correction consumer accepts the pinned target and composes
    with a method REPLACE, but copies target SMILES that RDKit cannot kekulize. This
    diagnostic therefore explicitly marks safe_to_execute=false. Candidate key is
    unique in eligible ChEBI and absent from all MIBiG rows. No candidate current
    owner was found in the recorded ignored-inclusive search. Corrected-key LOTUS/Cyano/classifier
    joins are empty; one exact-key ChEBI genus occurrence and one pinned AntibioticMech
    link exist.
  snapshot_sha256: f58a7c4211934cab7a2dbc215b92bef13e82d127ab9dac4bdd931a24d8ac8a3d
- evidence_id: ID056-REPAIR-CODE
  kind: record_content
  reference: src/naturalproductmech/curate/structure_corrections.py; scripts/extract_chebi.py;
    scripts/seed_from_sources.py; src/naturalproductmech/curate/claim_references.py
  locator: Complete relevant consumers and extractor; actual code hashes in diagnostic
  accessed_at: '2026-10-21T12:06:14.904034Z'
  support: context_only
  summary: The ChEBI extractor copies default SMILES without parsing. REPLACE_WITH_CHEBI
    pins full raw and target rows but copies that SMILES without chemistry validation.
    A paired correction enforces the full original-row digest before the method REPLACE,
    which by itself does not enforce expected fields. Existing claim-reference, strain
    and isolate overlays reject structure-corrected rows; any additional overlay requires
    explicit reviewed composition, not invented columns.
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
- evidence_id: S056-E-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/ambiguine-h-isonitrile.yaml
  locator: Whole owner and resolved local source projection
  accessed_at: '2026-10-21T12:01:06.360400Z'
  support: supports
  summary: Exact H owner DBOXZAYTFKDLHJ-KPQBMEGNSA-N encodes four assigned centres.
    BGC0001612:1 version 3 asserts UTEX 1903, KX451322.1, PMID:26629885, empty bounds
    and empty methods, giving SOURCE_ASSERTION/CLUSTER_UNSTATED. Both LOTUS genus-level
    DOI rows were read separately. The canonical complete raw MIBiG row digest is
    6eb7dabb0ddacef8fad927b861aa73dead7e1652ee9ef1696912f6cead6524c7.
  snapshot_sha256: f1d2f802102e93cfcdf367a7d501e2abbd349f071dddd48865e2cf4657095b7c
- evidence_id: S056-E-2015
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=4681624
  locator: DOI:10.1021/jacs.5b10136; full main body and figures/captions
  accessed_at: '2026-10-21T11:28:49.085487Z'
  support: supports
  summary: The study sequences the fam locus from Fischerella ambigua UTEX 1903 and
    reports that only FamD1 prenylates supplied hapalindole U with DMAPP to ambiguine
    H. FamD1/D2 are purified His-tagged proteins expressed in E. coli. The separate
    FamD2/FamC1 cyclase endpoint is 12-epi-hapalindole U; it is not an H whole-pathway
    or native knockout experiment.
  snapshot_sha256: b493006b4131f3355b9aaa68e0aad0a79306291a8f0c5f47397037143b6dd35b
- evidence_id: S056-E-SI
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/3731911
  locator: Official 2015 SI, S2-S4 cloning/purification/assays; S6 Figure 3; S25 H
    NMR and HRMS
  accessed_at: '2026-10-21T11:29:18.239895Z'
  support: supports
  summary: Genes were amplified from UTEX 1903 DNA, cloned in pET28a and expressed
    in E. coli BL21(DE3). Hapalindole U was supplied by Phil Baran. Only the FamD1
    + hapalindole U + DMAPP assay forms the labelled H peak; GPP and FamD2 comparisons
    do not. Product was isolated from a scaled 5 mL assay; S25 compares proton NMR
    with the 2007 H spectrum and reports [M+H]+ 373.2638 calculated and found. This
    is purified-enzyme evidence for the depicted product, not native H isolation or
    whole-cell heterologous synthesis.
  snapshot_sha256: 9b91ab700a8f3fb72dac76b8ab6d9ef2d2b868a0e67402c613f76bbc9071108a
- evidence_id: S056-E-DRAWING
  kind: validation
  reference: /private/tmp/npm-review-work/056/primary-2015-S6-H-comparison.json
  locator: S6 labelled H product; four independently transcribed stereo bonds and
    per-atom mapping
  accessed_at: '2026-10-21T11:59:38.823660Z'
  support: refutes
  summary: The complete S6 product drawing has C10S, C11R, C12R and C15S. After erasing
    all input stereo and entering its observed wedges/dashes, the graph gives DBOXZAYTFKDLHJ-CSOFANMDSA-N.
    All four corresponding owner centres are inverted. S25 explicitly shows only three
    centres, so the full comparison uses S6; achiral NMR alone is not used to establish
    an enantiomer. The identity packet owns the single structural finding.
  snapshot_sha256: ce6e5c9ad98ec749d4ea1a68fe9d4c2f33908c54e522649d3b15ded363130b3d
- evidence_id: S056-E-2007
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/17315959/
  locator: Original abstract, exact H/I/J names, culture description
  accessed_at: '2026-10-21T11:28:49.085947Z'
  support: partial
  summary: The original DOI10.1021/np060495r abstract names H as compound 1 among
    new H-I-J isolates from cultured Fischerella sp. collected in Israel. The abstract
    supports the genus-level named occurrence but does not supply a UTEX 1903 bridge
    or the original absolute-versus-relative assignment procedure.
  snapshot_sha256: ab0898e2ccc0e312ea63dd3ebeed2c039e6c849c7c9c452603b90c3bd0d65cb3
- evidence_id: S056-E-2007-GAP
  kind: search
  reference: https://doi.org/10.1021/np060495r
  locator: Bounded original body and SI access; institutional abstract and archive
    searches
  accessed_at: '2026-10-21T11:35:01.532032Z'
  support: unknown
  summary: The original 2007 full paper and supplement remain unavailable. The later
    2015 supplement reprints an H spectrum and supplies a complete product drawing,
    but does not substitute for direct inspection of all original culture and stereochemical
    methods.
  snapshot_sha256: d22a74f61e07b6f32893153dc0e0deddc6e81385ddd770956e0c6c6ebcf25f3d
  search_scope: Previously recorded official ACS/Figshare attempts, exact DOI/PMID
    and institutional/PMC leads; source preparation searched retained files including
    ignored files. No repeated blocked route or exhaustive literature absence claim.
- evidence_id: S056-E-MALEVAMIDE
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/18361518/
  locator: Original abstract of stored extra DOI10.1021/np070346o
  accessed_at: '2026-10-21T11:54:03.620424Z'
  support: unknown
  summary: This article is Isolation and Structure Determination of Malevamide E,
    a Dolastatin 14 Analogue, from the Marine Cyanobacterium Symploca laete-viridis.
    Its original abstract describes malevamide E and dolastatin 14 from field-collected
    Symploca, not the asserted H/Fischerella pair. Indexed original first-page text
    is consistent. The entire paper was not obtained, so this is a suspicious citation
    association rather than demonstrated absence of H from its complete contents.
  snapshot_sha256: d065f93be7e8ae83fa693101c7b19b583cffdfee48862d485cd998867306bc9a
- evidence_id: S056-E-NEW-GAP
  kind: search
  reference: https://doi.org/10.1021/np070346o
  locator: Recorded new citation retrieval receipt
  accessed_at: '2026-10-21T12:01:06.360400Z'
  support: unknown
  summary: The positive full-PDF mirror lead could not be reached and no full body
    was inspected. The empty failed PDF artifact is not treated as a source. The extra
    occurrence must remain citation-specifically unverified pending original content
    or a proven source mapping error.
  snapshot_sha256: 6f8efdf3198f3298da3cff5f312f23e39d143476df4009fc07d6fae45768570c
  search_scope: Exact PMID original XML, official/indexed primary title and abstract,
    one new original-PDF mirror lead and bounded primary-copy search; no all-paper
    absence inference.
- evidence_id: S056-E-CONSUMERS
  kind: record_content
  reference: scripts/seed_from_sources.py; src/naturalproductmech/curate/claim_references.py;
    src/naturalproductmech/grading.py
  locator: Method REPLACE and WITHDRAW application; SHA guard and structure-correction
    rejection
  accessed_at: '2026-10-21T12:01:06.360400Z'
  support: supports
  summary: Enzymatic assays maps to CLUSTER_DEMONSTRATED while retaining SOURCE_ASSERTION.
    H may receive this exact-product evidence only together with the approved primary-backed
    structure correction. The paired REPLACE_WITH_CHEBI decision enforces the complete
    original MIBiG row SHA256; an accompanying method REPLACE may rely on that active
    consumed guard rather than adding a redundant claim-reference row. The existing
    PMID26629885 remains correct. The eligible ChEBI representation must first be
    made parseable under the independently specified identity repair, and tests must
    require the structure and method decisions together. A future citation overlay
    would need an explicit composition contract because the current claim-reference
    consumer rejects structure_correction_note.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: R056-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/ambiguine-h-isonitrile.yaml
  locator: Complete owner YAML, including both history entries, all source claims
    and any discussions
  accessed_at: '2026-10-21T11:55:04.699932Z'
  support: supports
  summary: Root read the complete ambiguine H isonitrile owner after its individual
    intake. It has one MIBiG source concept, 2 occurrence entries, one producer and
    one locus. There are no inline or referenced mechanism graphs, pathway steps,
    molecular targets, bioactivity rows or synthetic-biology applications in this
    owner. The complete parsed owner was inspected; ignored-file filters were not
    used to infer field absence.
  snapshot_sha256: f1d2f802102e93cfcdf367a7d501e2abbd349f071dddd48865e2cf4657095b7c
- evidence_id: R056-LOCAL-SOURCES
  kind: record_content
  reference: /private/tmp/npm-review-work/056/local-sources.json
  locator: Complete target-specific MIBiG, LOTUS, CyanoMetDB, ChEBI and NPClassifier
    slices
  accessed_at: '2026-10-21T11:55:04.699932Z'
  support: context_only
  summary: Root read every matching local source row and compared it with the complete
    emitted owner. The separate scientific and identifier assessments decide claim
    support; deterministic reproduction does not establish primary evidence.
  snapshot_sha256: 99c4804e40630875fee4dff2b35bc476cf5fa72a92efa0357518efacb3ec4797
- evidence_id: R056-IMODULON-DATASETS
  kind: database
  reference: /private/tmp/npm-review-work/010/imodulon-datasets.txt
  locator: Complete 28-row dataset catalogue; actual command receipt in 010/imodulon-context-receipts.json
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: The successful structured-adapter dataset listing retrieved at 07:21:15
    UTC was fully re-read for this target. It contains no Fischerella or Hapalosiphon
    dataset, including no UTEX 1903 match. This same-session catalogue is reused with
    its original retrieval time; a fresh request is not claimed.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
assessments:
- assessment_id: ID056-IDENTITY
  area: identity
  topic: Exact encoded structure and resolving authority identifiers
  outcome: concern
  summary: Current MIBiG, NPAtlas and LOTUS-linked Wikidata agree with the owner enantiomer,
    but the explicit 2015 H drawing and eligible ChEBI:65400 MOL/InChI encode its
    opposite at all four centres. Agreement among the former databases does not settle
    the discrepancy.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - ID056-OWNER
  - ID056-COMPARISON
  - ID056-PRIMARY-H
  - ID056-DEPICTION
  - ID056-CANDIDATE-MOL
- assessment_id: ID056-GROUNDING
  area: provenance
  topic: Eligible grounding and stable source-concept identity
  outcome: concern
  summary: The source-concept hash is stable and correct. A bounded old-key query
    had no match, but a separate depicted-key lookup resolves eligible CHEBI:65400.
    Adoption must await explicit identity adjudication and a consumed repair of its
    invalid SMILES; current raw/target pins and exact-key collision checks are recorded.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - ID056-COMPARISON
  - ID056-CANDIDATE-JSON
  - ID056-CANDIDATE-GUARDS
  - ID056-REPAIR-CODE
- assessment_id: ID056-TAXONOMY
  area: scope
  topic: Genus, species and strain identifier boundaries
  outcome: supported
  summary: Current NCBI and Wikidata mappings resolve the asserted taxa and preserve
    their distinct ranks. The deposited locus carries UTEX 1903 metadata; genus-only
    or species-only occurrences remain distinct from strain-specific producer evidence.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - ID056-TAXON-STRAIN
  - ID056-TAXON-OCCURRENCES
  - ID056-GENBANK
- assessment_id: ID056-CLASSIFICATION
  area: identity
  topic: Predicted filing and separate BGC class scope
  outcome: supported
  summary: The exact-key NPClassifier output supports Alkaloids filing and the attributed
    hapalindole/tryptophan classes. The source BGC classes retain their separate annotation
    meaning.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - ID056-CLASS
  - ID056-SEED
  - ID056-MIBIG
  - ID056-SEARCH
- assessment_id: S056-A-IDENTITY
  area: identity
  topic: Exact named H and stereochemical identity
  outcome: concern
  summary: The primary named H graph is constitutionally identical but opposite at
    all four encoded centres. Positive NMR/HRMS assignment does not establish the
    current enantiomer. Preserve the original absolute-assignment method gap while
    correcting the representation through the separate identifier finding.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - S056-E-LOCAL
  - S056-E-DRAWING
  - S056-E-SI
  - S056-E-2007-GAP
- assessment_id: S056-A-METHOD
  area: evidence
  topic: FamD1 exact H assay and repair dependency
  outcome: concern
  summary: The source directly demonstrates the depicted H product using recombinant
    purified FamD1 from the UTEX 1903 locus. Once the primary-supported identity is
    adopted through the guarded structure decision, add Enzymatic assays with the
    existing PMID26629885 and SOURCE_ASSERTION/CLUSTER_DEMONSTRATED. Do not transfer
    the assay to the current opposite enantiomer. The structure decision already pins
    the complete original source row; require simultaneous structure-plus-method composition
    and review classification, cross-references and old-key occurrence provenance.
    No unchanged-citation overlay is necessary solely to duplicate that guard.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - S056-E-2015
  - S056-E-SI
  - S056-E-DRAWING
  - S056-E-CONSUMERS
- assessment_id: S056-A-ORIGIN
  area: evidence
  topic: Native versus recombinant context
  outcome: supported
  summary: The original abstract positively establishes biological isolation of named
    H from cultured Fischerella; the later native UTEX 1903 gene source and purified-protein
    assay are separate contexts. SOURCE_ASSERTION remains the honest native-producer
    grade. No native H knockout, de novo whole-cluster heterologous production or
    exact original Israeli-strain equivalence is asserted.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - S056-E-2007
  - S056-E-2015
  - S056-E-SI
- assessment_id: S056-A-OCCURRENCES
  area: evidence
  topic: Both stored genus-level occurrences
  outcome: unknown
  summary: The NP060495R abstract supports named H in Fischerella at genus level;
    the current enantiomeric source key needs coordinated provenance handling. NP070346O
    instead describes marine Symploca depsipeptides at inspected abstract/first-page
    scope. Its exact H occurrence is unresolved rather than proven false solely from
    a short abstract. Coarse genus rank is source-faithful and is not itself a defect.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - S056-E-LOCAL
  - S056-E-2007
  - S056-E-MALEVAMIDE
  - S056-E-NEW-GAP
- assessment_id: S056-A-COMPLETENESS
  area: completeness
  topic: Whole-owner scientific scope and optional claims
  outcome: unknown
  summary: All present scientific assertions were reviewed. Original isolation-method
    and extra occurrence access gaps remain required. The sparse owner has no optional
    activity table or mechanistic graph; their absence alone does not require additions.
    Root and identifier packets cover current authorities, computed classification
    and history.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - S056-E-LOCAL
  - S056-E-2007-GAP
  - S056-E-NEW-GAP
- assessment_id: R056-HISTORY
  area: provenance
  topic: Native status and retained seed history
  outcome: supported
  summary: The two dated seed events and SEEDED status accurately describe generated
    provenance. This review does not relabel the owner REVIEWED or treat seed history
    as scientific approval. Existing discussions, where present, remain part of the
    evidence to adjudicate.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - R056-OWNER
- assessment_id: R056-OPTIONAL
  area: completeness
  topic: Optional mechanism and application content
  outcome: not_applicable
  summary: The owner does not assert pathway steps, causal edges, organism-specific
    proteins, molecular targets, bioactivities or synthetic-biology applications.
    Their absence alone is not a defect in this source-generated record. No enzyme,
    target, activity or engineering claim is inferred from the congener name or chemical
    class.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - R056-OWNER
  - R056-LOCAL-SOURCES
- assessment_id: R056-IMODULON
  area: completeness
  topic: Structured transcriptomic context
  outcome: not_applicable
  summary: iModulonDB is not applicable for the named cyanobacterial producer and
    occurrence organisms in the inspected dataset catalogue. No matching organism/dataset
    supports a gene or module lookup. This coverage limit is not negative evidence
    about natural-product production or function.
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  evidence_ids:
  - R056-OWNER
  - R056-IMODULON-DATASETS
findings:
- finding_id: ID056-F-ENANTIOMER
  issue_key: ambiguine-h-primary-depiction-enantiomer-and-unsafe-chebi-representation
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The stored H enantiomer disagrees with the explicit primary product drawing
  description: 'The owner encodes DBOXZAYTFKDLHJ-KPQBMEGNSA-N, whereas 2015 SI S6
    explicitly named ambiguine H and current three-star CHEBI:65400 MOL/InChI encode
    DBOXZAYTFKDLHJ-CSOFANMDSA-N. Every one of four corresponding centres is opposite.
    The 2015 FamD1 result therefore cannot be unconditionally attached to the stored
    enantiomer. This confirms a representation/evidence disagreement, not new absolute
    experimental proof; the original 2007 full methods remain unavailable. Repair
    has a concrete additional prerequisite: both the committed target SMILES and current
    default SMILES contain an aromatic representation that RDKit cannot kekulize,
    despite valid agreeing MOL/InChI. The present correction loader would accept and
    copy that invalid text.'
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  field_paths:
  - chemical_structure
  - grounding_status
  - grounding_notes
  - xrefs
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - biosynthetic_gene_clusters[0].link_evidence_basis
  evidence_ids:
  - ID056-OWNER
  - ID056-PRIMARY-H
  - ID056-DEPICTION
  - ID056-CANDIDATE-JSON
  - ID056-CANDIDATE-MOL
  - ID056-CANDIDATE-GUARDS
  - ID056-REPAIR-CODE
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Consumed source/target-pinned identity decision; schema extension required
      for the valid derived representation
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Implement and enforce explicit valid representation pins and graph checks
      before copying a candidate
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Add the exact depicted-product enzymatic method only in the same composed
      repair
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Preserve original-source guards, corrected-key joins and canonical migration
      during regeneration
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_chebi.py
    role: Source representation ingestion and reproducible provenance; raw source
      bytes must remain attributable
  rule_id: 'review-checklist: exact full structure and claim-specific experiment scope'
  native_severity: 'blocker: unresolved exact enantiomeric identity prevents reliable
    representation of the named biological product'
  normalization_reason: The skill classifies wrong exact identity as blocker. The
    confirmed all-centre conflict prevents accepting one exact named product until
    adjudicated, while the unavailable original absolute-assignment methods remain
    explicit. One composed identity repair covers valid representation and the dependent
    enzyme method; no duplicate method-only finding is added.
actions:
- action_id: ID056-ACTION-IDENTITY
  finding_ids:
  - ID056-F-ENANTIOMER
  target_ids:
  - naturalproductmech:mibig-eb25c9b521
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Consumed source/target-pinned identity decision; schema extension required
      for the valid derived representation
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Implement and enforce explicit valid representation pins and graph checks
      before copying a candidate
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Add the exact depicted-product enzymatic method only in the same composed
      repair
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Preserve original-source guards, corrected-key joins and canonical migration
      during regeneration
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_chebi.py
    role: Source representation ingestion and reproducible provenance; raw source
      bytes must remain attributable
  description: Adjudicate the explicit source depiction, then implement a consumed
    representation extension before using REPLACE_WITH_CHEBI for BGC0001612:1 version
    3. Pin complete original row SHA256 6eb7dabb0ddacef8fad927b861aa73dead7e1652ee9ef1696912f6cead6524c7
    and complete CHEBI:65400 target row SHA256 e3907f95f890384299169cb7564df91125532d6cc9ee0e579cb0dfda76ad961b;
    preserve both raw inventories unchanged. The existing target SMILES is invalid
    and must not be copied. Extend the maintained correction schema/consumer to accept
    an explicitly attributed alternative isomeric SMILES derived from the pinned official
    MOL SHA256 00cc7baed9ee239a18c806c5c842288bc63a6ac568857780db7c50806991a882, and
    enforce MOL/SMILES/Standard-InChI full-key and fixed-H agreement with DBOXZAYTFKDLHJ-CSOFANMDSA-N,
    formula C26H32N2, charge zero and four complete centres. The derived candidate
    string is [C-]#[N+][C@@H]1[C@@H]2c3c(C(C)(C)C=C)[nH]c4cccc(c34)C(C)(C)[C@H]2CC[C@]1(C)C=C.
    Such fields are a required implementation change, not a presently consumed option.
    Retain curator, actual decision date and DOI:10.1021/jacs.5b10136 plus the original-assignment
    limitation. Once this exact graph is adopted, compose a method REPLACE for the
    same minted source concept with Enzymatic assays; the paired structure decision
    supplies the enforced full-row guard. Keep SOURCE_ASSERTION for native production
    and use CLUSTER_DEMONSTRATED only for the purified FamD1 product assay. The existing
    PMID26629885 already names that study. Do not add a redundant claim-reference
    overlay solely for guarding; if citation, strain or isolate overlays are introduced
    later, first implement/test their presently rejected structure-correction composition.
    Clear old NPAtlas/source xrefs, never transfer old-key LOTUS rows or classifier
    output by name, and regenerate through the normal seed pathway.
  generator: scripts/seed_from_sources.py with an explicitly extended src/naturalproductmech/curate/structure_corrections.py
    and the existing method override consumer
  acceptance_checks:
  - Reject changed source/target row digests, MOL snapshot, selected key, graph or
    stereochemistry; verify unique source/target and zero colliding MIBiG/current
    owners. Candidate target digest is e3907f95f890384299169cb7564df91125532d6cc9ee0e579cb0dfda76ad961b;
    existing consumer acceptance in the diagnostic is not safe chemistry validation.
  - 'Reconcile candidate-key classification explicitly: current NPClassifier has only
    the old key. Obtain an attributed valid new-key classification through the documented
    source workflow and verify resulting Alkaloids filing, rather than silently losing
    classification or copying the old-key row. Expected grounded identity is CHEBI:65400;
    use documented canonical owner/PATHS migration and preserve the minted MIBiG source
    concept.'
  - Old-key LOTUS rows have full selectors/digests in the diagnostic and remain in
    provenance; they must not be automatically copied to the new enantiomer. Corrected-key
    ChEBI origin is genus Fischerella/PMID17315959, with no strain. Its full row SHA256
    is d83184c1cea3ea1760e713a8353ba4bded2b4847cee47074f42b186e039112ee. Reconcile
    original 2007 and extra malevamide citation limitations claim by claim.
  - The candidate key has an existing pinned AntibioticMech CHEBI:65400 link at commit
    74f6cc8362498900f2fe2c13d0b6fdb66dd30976, raw-row SHA256 0b241499005f913f580c9675ec175f2c65925cb6b4e7bd5f81d08da804f8424b.
    A generated SAME_STRUCTURE link may use that exact-key bridge after repair; do
    not transfer its mechanisms or imply a newly inspected sibling owner.
  - 'Exercise structure + method composition together: the full raw source pin must
    fail on any field drift, empty original methods must not be mistaken for pre-existing
    assays, and the resulting grades must be SOURCE_ASSERTION/CLUSTER_DEMONSTRATED
    without native knockout or de novo whole-cell production claims.'
  - Run strict target chemistry/schema, provenance, corpus integrity, exact reproduction
    and required QC after authorized implementation. Keep review completion partial
    until required original-isolation and extra-citation access gaps are resolved.
limitations:
- Agreement between authority structures does not independently establish the absolute
  configuration or organism of the original isolated material; primary source limitations
  are assessed separately.
- GenBank header/source verification establishes accession metadata, not equivalence
  of whole amb/fam sequences, assay constructs or congener-specific enzymatic function.
- The old-key ChEBI negative query and depicted-key positive query have distinct scopes.
  Three-star status does not validate every serialized representation.
- The original 2007 full isolation and absolute-assignment methods remain unavailable;
  the observed later drawing/authority agreement does not replace experimental stereochemical
  proof.
- The 2007 full isolation paper and SI remain unavailable; exact original culture
  accession and absolute stereochemical assignment procedure were not inferred from
  later database records.
- The 2015 assay establishes the depicted named H product. Its complete drawing disagrees
  with the owner enantiomer; achiral NMR/HRMS cannot resolve that discrepancy alone.
- The extra malevamide article was inspected at original abstract and indexed first-page
  scope only; no whole-paper absence claim or automatic occurrence exclusion follows.
- This review audits the present assertions and the concrete source questions they
  raise; it does not claim exhaustive discovery of every later activity or biosynthetic
  study. Optional enrichment remains distinct from correcting an unsupported current
  assertion.
- The configured identifier-label gate accepts 499 warning-level mismatches and 35
  explicit exceptions and skips 4,744 no-adapter pairs; exit 0 does not independently
  verify every identifier or scientific claim.
- The quality suite reports 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21).
  Skipped tests are not counted as passing tests. Existing ontology caches were used;
  no multi-gigabyte cache download was required.
- Native gates assess deterministic consistency and configured invariants. They do
  not establish biological production, stereochemical specificity, evidence adequacy,
  or literature-level claim support.
- The five reused gates retain their batch004 execution times and cached ontology
  results. Reuse establishes unchanged repository inputs; it is not a new remote authority
  query or new assertion of ontology freshness.
- The ignored-inclusive check enumerates record and saved-review YAML paths, and all
  tracked files are hashed. Generated Python bytecode and external tool caches are
  not claimed to have been independently byte-pinned at the prior execution.
notes:
- No scientific owner, inventory, curation table, native status or history was edited.
  Actions are proposed work.
- Baseline gates retain their actual original receipts after byte-for-byte input verification;
  target strict validation ran afresh. Scientific failed or unavailable checks are
  distinct from bundle validation.
tags:
- path-order-campaign
- batch-006
```
